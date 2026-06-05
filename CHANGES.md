# Session 8 — Runtime Changes & Bug Fixes

> All changes made during the 05 Jun 2026 debugging session.
> Paths are relative to the project root:
> `Session8/MultiAgentDAGOrchestrationandSkillCatalogs/`

---

## Summary Table

| # | File(s) | Change |
|---|---|---|
| 1 | `gateway/main.py` | 3-second pre-call delay before every LLM request |
| 2 | `gateway/main.py` | Failover order enforced: groq → openrouter → ollama |
| 3 | `gateway/agent_routing.yaml` | All agent pins overhauled away from gemini |
| 4 | `code/perception.py`, `code/memory.py` | Removed hardcoded `provider="g"`; reverted to gemini via yaml |
| 5 | `code/prompts/coder.md` | Replaced stub with real coder prompt |
| 6 | `code/mcp_runner.py` | ExceptionGroup crash from MCP subprocess handled |
| 7 | `gateway/agent_routing.yaml` | formatter/summariser moved off groq (TPM exhaustion) |
| 8 | `code/prompts/planner.md` | Memory-hit shortcut guarded against local file queries |
| 9 | `code/agent_config.yaml` | Retriever given `index_document` + `read_file` tool access |
| 10 | `code/prompts/retriever.md` | Taught index-then-search pattern for local files |
| 11 | `code/skills.py` | `index_document` + `read_file` added to `_TOOL_CATALOG` |
| 12 | `code/prompts/retriever.md`, `code/agent_config.yaml` | Retriever stopping after index step; prompt, token limit, and output schema fixed |

---

## 1. 3-Second Pre-Call Delay Before Every LLM Request

**File:** `gateway/main.py`

**Why:** Upstream providers (Groq, OpenRouter) enforce per-minute rate windows.
Rapid successive calls from parallel DAG nodes burned through the quota in
seconds. A small mandatory pause gives the rate-limit window time to recover
between provider attempts.

**Where:** Inside the `/v1/chat` handler, inside the per-provider `try` block,
just before the `if req.stream` branch (fires for both streaming and
non-streaming paths).

```python
# ── Pre-call delay (3 s) ─────────────────────────────────────────
import asyncio as _pre
await _pre.sleep(3)
# ─────────────────────────────────────────────────────────────────
```

> The sleep fires on every provider attempt including failover retries —
> three-provider exhaustion costs ≥ 9 s. Adjust the constant in `main.py`
> if this becomes too slow for interactive use.

---

## 2. Enforced Failover Order: groq → openrouter → ollama

**File:** `gateway/main.py` — `DEFAULT_ORDER` constant.

**Why:** The original order put Ollama first, burning local resources before
trying faster cloud providers. The new order goes cloud-first.

```python
# Before
DEFAULT_ORDER = ["ollama", "gemini", "nvidia", "groq", "cerebras", "openrouter", "github"]

# After
DEFAULT_ORDER = ["groq", "openrouter", "ollama", "gemini", "nvidia", "cerebras", "github"]
```

> This order only applies when no `provider=` is explicitly pinned and
> `auto_route` is off. Tier-specific orders (`TIER_TO_ORDER` in `main.py`)
> take precedence when `auto_route` is active. Override at runtime via the
> `LLM_ORDER` env var in `.env`.

---

## 3. Agent Routing Overhaul

**File:** `gateway/agent_routing.yaml`

**Why:** All agents were originally pinned to `gemini`, which is an explicit
override that bypasses the failover order entirely. Calls showed `gemini` in
the OVERRIDE column of the dashboard for every single node.

**Final state (after all tuning in this session):**

| Skill | Provider | Rationale |
|---|---|---|
| `planner` | `gemini` | Strong reasoning needed for DAG decomposition |
| `researcher` | `groq` | Fast short queries; rarely exceeds TPM window |
| `distiller` | `openrouter` | Extraction task; avoids groq TPM |
| `summariser` | `openrouter` | Medium text; avoids groq TPM |
| `critic` | `gemini` | Pass/fail judgement; benefits from strong model |
| `formatter` | `openrouter` | Was 503-ing when pinned to groq |
| `retriever` | `openrouter` | Multi-hop tool calls consume more tokens |
| `sandbox_executor` | `ollama` | Local execution; no network needed |
| `coder` | `gemini` | Long code-generation outputs |
| `browser` | `gemini` | Reserved for Session 9 |

> Pins are **preferences**, not hard locks. If the pinned provider is in
> cooldown the gateway falls through `groq → openrouter → ollama`
> automatically. **Restart the gateway** after editing this file — it is
> loaded once at startup.

---

## 4. Removed Hardcoded `provider="g"` from Perception & Memory

**Files:** `code/perception.py` (line ~175), `code/memory.py` (line ~295)

**Why:** Both modules had `provider="g"` (the Gemini shortcut) hardcoded
directly in their `LLM().chat(...)` calls. An explicit `provider=` override
wins before `agent_routing.yaml` is consulted, so the failover order was
completely bypassed for these two cognitive modules.

**Fix:** Removed the `provider="g"` argument from both calls. Both retain
`auto_route=` so the gateway still applies agent-level routing.

**Note:** Perception and memory were subsequently **re-pinned to Gemini** by
adding them to `agent_routing.yaml`. The key difference is that the pin now
lives in the yaml (one place to change) rather than in source code.

> Going forward: to change the provider for perception or memory, edit
> `agent_routing.yaml`, not the Python files.

---

## 5. Fixed: `sandbox_executor` Failing in 0.1s — Stub Coder Prompt

**File:** `code/prompts/coder.md`

**Why:** The coder prompt was a student placeholder:
```
STUB — STUDENT ASSIGNMENT.
```
The LLM returned free-form prose instead of the required
`{"code": "...", "rationale": "..."}` JSON. `skills.py` checks
`r["output"].get("code")` — finding nothing, it returned
`AgentResult(success=False)` immediately. This triggered:

```
recovery → planner → coder → sandbox_executor → recovery → planner → ...
```

The loop ran until the 60-node hard cap (`MAX_NODES`) was hit.

**Fix:** Replaced the stub with a working prompt explaining:
- Sandbox working directory is `/sandbox`; paths are relative (e.g. `papers/attention.md`)
- Constraints: no network, no `pip install`, standard library only
- Required JSON output format with field names
- A concrete example showing the expected response

---

## 6. Fixed: `retriever` — `ExceptionGroup` Crash

**File:** `code/mcp_runner.py`

**Why:** `stdio_client` (the MCP client library) uses `asyncio.TaskGroup`
internally. When the MCP subprocess crashes or exits unexpectedly, Python 3.11+
raises an `ExceptionGroup` instead of a plain exception. The `except Exception`
handler in `flow.py`'s `_run_one` dispatcher **does not catch** `ExceptionGroup`,
so the crash propagated upward and killed the entire `asyncio.gather` batch —
losing the results of all sibling nodes running in the same tick.

**Fix:** Wrapped the `stdio_client` block with `except* Exception` to intercept
`ExceptionGroup`, unwrap its inner exceptions, and re-raise as a plain
`RuntimeError`:

```python
except* Exception as eg:
    causes = eg.exceptions if hasattr(eg, "exceptions") else [eg]
    raise RuntimeError(
        f"MCP session failed: {'; '.join(str(e) for e in causes)}"
    ) from eg
```

`flow.py`'s `except Exception` then catches it, classifies it as
`upstream_failure`, and queues a recovery planner node — instead of crashing
the whole gather.

---

## 7. Fixed: `formatter` / `summariser` 503 — Groq TPM Exhaustion

**File:** `gateway/agent_routing.yaml`

**Why:** Groq enforces **6,000 TPM / 30 RPM**. When researcher, distiller,
summariser, formatter, and retriever were all routed to Groq simultaneously,
the token budget was exhausted in seconds. The cascade:

```
Groq 429 → gateway backs off Groq (60s)
         → tries OpenRouter → also rate-limited
         → 503: all providers unavailable
```

The formatter and summariser were then classified as `transient` failures
(`recovery.py` checks for `"503"` in the error string) and skipped, not
re-planned — so the run ended with no final answer.

**Fix:** Moved `formatter`, `summariser`, `distiller`, and `retriever` to
`openrouter`. Only `researcher` stays on Groq (short initial queries that
rarely fill the TPM window alone).

---

## 8. Fixed: Planner Routes to `retriever` Without Indexing First

**File:** `code/prompts/planner.md`

**Why:** The planner prompt contained:

> *"If MEMORY HITS appear, prefer routing the answer through the existing
> knowledge base: emit a `retriever`..."*

The run had 7 prior memory hits. The planner saw them and emitted
`retriever → formatter` — but `papers/attention.md` had never been indexed
into the FAISS knowledge base. The retriever searched an empty index, found
nothing, and the formatter returned *"unable to locate the file"*.

The rule had **no guard** distinguishing "query references a local file on
disk" from "query asks about already-indexed material".

**Fix:** Split the rule into two cases:

```
If MEMORY HITS appear AND the query does NOT reference a specific local file
(e.g. "papers/foo.md"), use the knowledge base shortcut — emit retriever or
go straight to formatter.

If the query DOES reference a specific local file path, always emit a
`retriever` node — the retriever will call `index_document` first, then
`search_knowledge`.
```

---

## 9. Fixed: Retriever Skill Has No Access to `index_document` / `read_file`

**File:** `code/agent_config.yaml`

**Why:** The retriever's `tools_allowed` only listed `[search_knowledge]`. Even
after the planner was fixed to route correctly, the retriever could not call
`index_document` to index the file before searching.

```yaml
# Before
tools_allowed: [search_knowledge]

# After
tools_allowed: [search_knowledge, index_document, read_file]
```

---

## 10. Fixed: Retriever Prompt Has No Instructions for Local Files

**File:** `code/prompts/retriever.md`

**Why:** The old retriever prompt only described `search_knowledge`. It had no
awareness of local sandbox files or when to call `index_document`. Even with
the tool added to `tools_allowed`, the LLM had no guidance to use it.

**Fix:** Rewrote the prompt to teach a two-step procedure:

1. If the question references a **specific local file path** → call
   `index_document(path)` first, then `search_knowledge`.
2. If **no specific file** is referenced → call `search_knowledge` directly.
3. Retry with a rephrased query if the first search returns too little.
4. Hard cap: ≤ 2 `index_document` calls, ≤ 3 `search_knowledge` calls per run.

Also clarified the path convention: paths are relative to the sandbox root
(e.g. `papers/attention.md`) — do **not** prefix with `/sandbox/`.

---

## 11. Fixed: `index_document` / `read_file` Not Exposed to the LLM

**File:** `code/skills.py` — `_TOOL_CATALOG` dict

**Why:** This was the actual root cause of all the "retriever finds nothing"
failures. `skills.py` maintains a hardcoded `_TOOL_CATALOG` dict. The
`tool_payload()` function filters `tools_allowed` against it:

```python
def tool_payload(tool_names: list[str]) -> list[dict] | None:
    return [_TOOL_CATALOG[n] for n in tool_names if n in _TOOL_CATALOG]
```

`index_document` and `read_file` were added to `agent_config.yaml`'s
`tools_allowed` (fix #9) but **not** to `_TOOL_CATALOG`. The filter silently
dropped them. The LLM was never offered those tools in the `tools=` payload
sent to the gateway, so it could only call `search_knowledge`.

**Fix:** Added both entries to `_TOOL_CATALOG` with descriptions that include
the path convention warning:

```python
"index_document": {
    "name": "index_document",
    "description": (
        "Chunk a sandbox file and write each chunk into Memory as a "
        "searchable fact. Call this BEFORE search_knowledge when the "
        "user references a specific local file path (e.g. "
        "'papers/attention.md'). Path is relative to the sandbox root — "
        "do NOT prefix with '/sandbox/'."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {"type": "string"},
            "chunk_size": {"type": "integer", "default": 400},
            "overlap": {"type": "integer", "default": 80},
        },
        "required": ["path"],
    },
},
"read_file": {
    "name": "read_file",
    "description": (
        "Read the raw text of a sandbox file. Use for quick one-shot "
        "inspection when you don't need the content to persist in Memory. "
        "Path is relative to the sandbox root."
    ),
    "input_schema": {
        "type": "object",
        "properties": {"path": {"type": "string"}},
        "required": ["path"],
    },
},
```

> **Lesson:** Adding a tool to `agent_config.yaml`'s `tools_allowed` is not
> enough. It must also be registered in `_TOOL_CATALOG` in `skills.py`, or
> `tool_payload()` will silently drop it and the LLM will never see it.

---

## 12. Fixed: Retriever Stops After Indexing Without Searching

**Files:** `code/prompts/retriever.md`, `code/agent_config.yaml`

**Symptom:** The query reported "only fetching attention.md from papers" —
the file was being indexed but the actual question (three key contributions)
was never answered.

**Why (three compounding causes):**

| Cause | Detail |
|---|---|
| LLM stops after `index_document` | The prompt described indexing and searching as equal steps. The LLM interpreted a successful `index_document` call as task complete and stopped before calling `search_knowledge` |
| Token limit hit mid-loop | `max_tokens: 1200` was too low for the full tool-call loop: index → search → emit JSON output. The model was being cut off before it could produce the search step |
| Formatter had nothing to work with | Output schema used `"preview": "<first 200 chars>"` per chunk — not nearly enough for the formatter to identify and describe three specific technical contributions |

### Fix 1 — `code/prompts/retriever.md` (rewrite)

Rewrote the prompt with unambiguous mandatory steps and a bold warning:

```
MANDATORY PROCEDURE:

  Step 1. Call index_document(path)
  Step 2. IMMEDIATELY call search_knowledge(...)  ← MUST follow, never skip
  Step 3. Retry search once if fewer than 3 chunks returned
  Step 4. Emit output JSON

IMPORTANT: index_document is PREPARATION, not the answer.
After calling it you MUST call search_knowledge before stopping.
```

Also changed the output schema from a truncated preview to full chunk content:
```json
// Before
{"source": "...", "preview": "<first 200 chars>"}

// After
{"source": "...", "content": "<full chunk text — do not truncate>"}
```

### Fix 2 — `code/agent_config.yaml`

Increased `max_tokens` for the retriever skill:

```yaml
# Before
max_tokens: 1200

# After
max_tokens: 3000
```

The retriever runs a multi-turn tool-use loop (index → search → produce JSON
with full chunk content). 1200 tokens was exhausted before `search_knowledge`
could even be called.
