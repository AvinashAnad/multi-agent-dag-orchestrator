# Project Modules Documentation

## Module: `extract_funcs.py`

### Function: `get_type_name`
- **Description**: *(Analyzed from source)* Performs the 'Get type name' operation. Returns a computed result.
- **Input Parameters**: `node` (`Any`)
- **Output Type**: `Any`

## Module: `code/vector_index.py`

### Function: `_l2_normalize`
- **Description**: L2-normalize a 1D vector. After normalization, inner product equals cosine similarity.
- **Input Parameters**: `vec` (`np.ndarray`)
- **Output Type**: `np.ndarray`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `store_dir` (`Path`)
- **Output Type**: `Any`

### Function: `_load`
- **Description**: *(Analyzed from source)* Performs the ' load' operation.
- **Input Parameters**: `None`
- **Output Type**: `None`

### Function: `persist`
- **Description**: *(Analyzed from source)* Performs the 'Persist' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `None`

### Function: `clear`
- **Description**: *(Analyzed from source)* Performs the 'Clear' operation.
- **Input Parameters**: `None`
- **Output Type**: `None`

### Function: `add`
- **Description**: *(Analyzed from source)* Performs the 'Add' operation. May raise exceptions under certain conditions.
- **Input Parameters**: `item_id` (`str`), `embedding` (`list[float]`)
- **Output Type**: `None`

### Function: `search`
- **Description**: Return up to k `(item_id, similarity)` pairs, ranked by similarity.
- **Input Parameters**: `query_embedding` (`list[float]`), `k` (`int`)
- **Output Type**: `list[tuple[Tuple[str, float]]]`

### Function: `size`
- **Description**: *(Analyzed from source)* Performs the 'Size' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `int`

### Function: `dim`
- **Description**: *(Analyzed from source)* Performs the 'Dim' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `int | None`

## Module: `code/gateway.py`

### Function: `_is_up`
- **Description**: *(Analyzed from source)* Performs the ' is up' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `bool`

### Function: `ensure_gateway`
- **Description**: Start V8 if it is not already running. Idempotent.
- **Input Parameters**: `None`
- **Output Type**: `None`

### Function: `embed`
- **Description**: Compute an embedding for `text` via the gateway's embed endpoint.  Returns the full response dict: `{embedding, dim, model, provider, latency_ms, ...}`. The chosen embedding model is fixed at the gateway level. Changing it invalidates every FAISS index built against the old vectors, so callers should treat the model as a project-level constant.
- **Input Parameters**: `text` (`str`), `task_type` (`str`)
- **Output Type**: `dict`

## Module: `code/persistence.py`

### Function: `_atomic_write`
- **Description**: *(Analyzed from source)* Performs the ' atomic write' operation.
- **Input Parameters**: `path` (`Path`), `data` (`bytes | str`)
- **Output Type**: `None`

### Function: `list_sessions`
- **Description**: *(Analyzed from source)* Performs the 'List sessions' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `list[str]`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `session_id` (`str`)
- **Output Type**: `Any`

### Function: `query_path`
- **Description**: *(Analyzed from source)* Performs the 'Query path' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Path`

### Function: `graph_path`
- **Description**: *(Analyzed from source)* Performs the 'Graph path' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Path`

### Function: `_legacy_graph_path`
- **Description**: *(Analyzed from source)* Performs the ' legacy graph path' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Path`

### Function: `write_query`
- **Description**: *(Analyzed from source)* Performs the 'Write query' operation.
- **Input Parameters**: `query` (`str`)
- **Output Type**: `None`

### Function: `read_query`
- **Description**: *(Analyzed from source)* Performs the 'Read query' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `str`

### Function: `write_graph`
- **Description**: Serialise the DiGraph to JSON via nx.node_link_data. Per-node `result` is an AgentResult (Pydantic) — dump it to a dict so the JSON encoder is happy. Reviving on read restores the Pydantic shape.
- **Input Parameters**: `graph_obj` (`nx.DiGraph`)
- **Output Type**: `None`

### Function: `read_graph`
- **Description**: *(Analyzed from source)* Performs the 'Read graph' operation. Returns a computed result. May raise exceptions under certain conditions. Includes logging or printing.
- **Input Parameters**: `None`
- **Output Type**: `nx.DiGraph | None`

### Function: `_node_path`
- **Description**: *(Analyzed from source)* Performs the ' node path' operation. Returns a computed result.
- **Input Parameters**: `node_id` (`str`)
- **Output Type**: `Path`

### Function: `write_node`
- **Description**: *(Analyzed from source)* Performs the 'Write node' operation.
- **Input Parameters**: `state` (`NodeState`)
- **Output Type**: `None`

### Function: `read_node`
- **Description**: *(Analyzed from source)* Performs the 'Read node' operation. Returns a computed result.
- **Input Parameters**: `node_id` (`str`)
- **Output Type**: `NodeState | None`

### Function: `read_all_nodes`
- **Description**: Load every persisted NodeState in this session. Corrupt or partially-written files (the typical cause is a process kill between the temp-file write and the atomic rename) are skipped with a clear warning to stderr — never silently dropped. NOTES_RUNS feedback P0 #2: a bare `except Exception: continue` here was killing resume invisibly when one node file was bad.
- **Input Parameters**: `None`
- **Output Type**: `list[NodeState]`

## Module: `code/recovery.py`

### Function: `classify_failure`
- **Description**: *(Analyzed from source)* Performs the 'Classify failure' operation. Returns a computed result.
- **Input Parameters**: `error_text` (`str`)
- **Output Type**: `RecoveryReason`

### Function: `plan_recovery`
- **Description**: Decide what to do with a node failure that is NOT a critic-verdict failure. The critic-fail path is handled separately in the Executor because it needs access to the critic node's metadata (target, child) and a per-target cap that is run-scoped state — this function is the purely-local predicate.  Decision table (all coverage):   reason=transient                          → skip (gateway already retried)   reason=validation_error                   → skip (prompt bug, not runtime)   reason=upstream_failure, failed=planner   → skip (would loop on Planner errors)   reason=upstream_failure, failed=other     → replan
- **Input Parameters**: `None`
- **Output Type**: `RecoveryDecision`

### Function: `handle_critic_verdict`
- **Description**: Critic-fail policy (P1 #5). Returns True when the caller should skip the normal `extend_from` (because the Critic emitted `fail` and we handled it by splicing a recovery Planner). False on `pass`.  Two shapes of Critic appear in S8: auto-inserted Critics (Graph.extend_from inserts one whenever a `critic:true` skill has outgoing edges) which carry `target` + `child` in metadata, and Planner-emitted Critics which do not — for the latter we derive both from graph structure.
- **Input Parameters**: `nid` (`str`), `result` (`Any`), `graph` (`Any`), `recovered_branches` (`dict`), `cap_hit` (`list`)
- **Output Type**: `bool`

## Module: `code/skills.py`

### Function: `resolve_inputs`
- **Description**: Materialise each input id into a dict the prompt can serialise.  Recognised input forms:   - "USER_QUERY"  → the original user query text   - "n:<i>"       → the AgentResult.output of that completed node   - "art:<sha>"   → the bytes of an artifact, decoded as utf-8 best-effort   - any other     → passed through as a free-form string  `graph_nodes` is the nx node-view dict from flow.Graph; we read each upstream node's `result` attribute (set when the orchestrator marks the node complete).
- **Input Parameters**: `node_inputs` (`list[str]`), `graph_nodes` (`Any`), `query` (`str`)
- **Output Type**: `list[dict]`

### Function: `_format_memory_hits`
- **Description**: Compact rendering of FAISS-ranked MemoryItem hits for the prompt.  Each hit is shown as one line: kind, descriptor, source, plus a 400-char preview of `value.chunk` when present (indexed-document chunks) or of `value.raw` (classifier facts). The full chunk would blow the prompt, but the descriptor + preview is enough for the Planner to decide whether memory already covers the query and for downstream skills to synthesise from indexed material without an extra Retriever round-trip.
- **Input Parameters**: `hits` (`list`)
- **Output Type**: `str`

### Function: `render_prompt`
- **Description**: *(Analyzed from source)* Performs the 'Render prompt' operation. Returns a computed result.
- **Input Parameters**: `skill` (`Skill`), `query` (`str`), `resolved` (`list[dict]`), `failure_report` (`str | None`), `memory_hits` (`list | None`), `question` (`str | None`)
- **Output Type**: `str`

### Function: `parse_skill_json`
- **Description**: Skills return a single top-level JSON object. Strip markdown fences if the model added them despite being told not to.
- **Input Parameters**: `text` (`str`)
- **Output Type**: `dict`

### Function: `tool_payload`
- **Description**: *(Analyzed from source)* Performs the 'Tool payload' operation. Returns a computed result.
- **Input Parameters**: `tool_names` (`list[str]`)
- **Output Type**: `list[dict] | None`

### Function: `run_skill`
- **Description**: Dispatch one node. Returns (result, rendered_prompt).  `memory_hits` is the FAISS-ranked MemoryItem list captured once at session start by Executor.run and threaded through here so every skill's prompt can see the same hits. This is the S7 promise carried forward — Memory works in S8 because the orchestrator delivers the hits, not just because the FAISS index is on disk.  sandbox_executor bypasses the gateway: it picks the `code` field out of its upstream coder node and runs sandbox.run_python directly. All other skills are LLM-backed and route through the V8 gateway with agent=<skill_name> so agent_routing.yaml + cost-by-agent kick in.
- **Input Parameters**: `skill` (`Skill`), `node_id` (`str`), `graph_nodes` (`Any`), `session_id` (`str`), `query` (`str`), `failure_report` (`str | None`)
- **Output Type**: `tuple[Tuple[AgentResult, str]]`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `name` (`str`), `cfg` (`dict`)
- **Output Type**: `Any`

### Function: `prompt_template`
- **Description**: *(Analyzed from source)* Performs the 'Prompt template' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `str`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `get`
- **Description**: *(Analyzed from source)* Performs the 'Get' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `name` (`str`)
- **Output Type**: `Skill`

### Function: `names`
- **Description**: *(Analyzed from source)* Performs the 'Names' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `list[str]`

## Module: `code/memory.py`

### Function: `_load`
- **Description**: *(Analyzed from source)* Performs the ' load' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `list[MemoryItem]`

### Function: `_save`
- **Description**: *(Analyzed from source)* Performs the ' save' operation.
- **Input Parameters**: `items` (`list[MemoryItem]`)
- **Output Type**: `None`

### Function: `_index`
- **Description**: Return a freshly-loaded FAISS index every call.  Re-reading the index file is cheap at S7 scale and keeps the agent process consistent with writes made by the MCP subprocess (which runs `index_document` in a separate Python process and persists to the same disk files). On cold start (no index files on disk), the index is rebuilt from items already persisted in `memory.json`.
- **Input Parameters**: `None`
- **Output Type**: `VectorIndex`

### Function: `_try_embed`
- **Description**: Compute an embedding via the gateway. Returns None if the gateway is unavailable. The caller decides whether to persist a non-embedded item.
- **Input Parameters**: `text` (`str`), `task_type` (`str`)
- **Output Type**: `list[float] | None`

### Function: `_tokens`
- **Description**: *(Analyzed from source)* Performs the ' tokens' operation. Returns a computed result.
- **Input Parameters**: `text` (`str`)
- **Output Type**: `set[str]`

### Function: `_keyword_search`
- **Description**: *(Analyzed from source)* Performs the ' keyword search' operation. Returns a computed result.
- **Input Parameters**: `query` (`str`), `history` (`list[dict] | None`)
- **Output Type**: `list[MemoryItem]`

### Function: `_vector_search`
- **Description**: *(Analyzed from source)* Performs the ' vector search' operation. Returns a computed result.
- **Input Parameters**: `query` (`str`)
- **Output Type**: `list[MemoryItem]`

### Function: `read`
- **Description**: Vector first, keyword as fallback when vector returns nothing.
- **Input Parameters**: `query` (`str`), `history` (`list[dict] | None`)
- **Output Type**: `list[MemoryItem]`

### Function: `_persist_item`
- **Description**: Append `item` to the JSON store and, if it has an embedding, to the FAISS index. Returns the same item for caller convenience.
- **Input Parameters**: `item` (`MemoryItem`)
- **Output Type**: `MemoryItem`

### Function: `_fallback_remember`
- **Description**: Deterministic write when the classifier LLM is unavailable. Keyword extraction is naive (top word tokens); kind defaults to fact. The embedding is still attempted; if it fails the item persists without a vector and stays reachable through the keyword fallback.
- **Input Parameters**: `raw_text` (`str`)
- **Output Type**: `MemoryItem`

### Function: `remember`
- **Description**: LLM-classified write for ambiguous content (user input, free-form observation). One classifier call plus one embed call. If the classifier fails, the deterministic fallback handles the write.
- **Input Parameters**: `raw_text` (`str`)
- **Output Type**: `MemoryItem`

### Function: `_llm_classify`
- **Description**: *(Analyzed from source)* Performs the ' llm classify' operation. Returns a computed result.
- **Input Parameters**: `raw_text` (`str`), `schema` (`dict`)
- **Output Type**: `dict`

### Function: `record_outcome`
- **Description**: Zero-LLM-classify write for a deterministic tool outcome. Kind is `tool_outcome` by construction. Embedding is computed from the descriptor so the outcome remains retrievable by semantic similarity.
- **Input Parameters**: `None`
- **Output Type**: `MemoryItem`

### Function: `add_fact`
- **Description**: Direct fact write used by document-indexing tools. Skips the LLM classifier (kind is known) but still embeds the descriptor.
- **Input Parameters**: `descriptor` (`str`)
- **Output Type**: `MemoryItem`

### Function: `clear`
- **Description**: Wipe persistent memory and the vector index. Useful between assignment attempts.
- **Input Parameters**: `None`
- **Output Type**: `None`

## Module: `code/flow.py`

### Function: `main`
- **Description**: *(Analyzed from source)* Performs the 'Main' operation.
- **Input Parameters**: `None`
- **Output Type**: `None`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `add_node`
- **Description**: *(Analyzed from source)* Performs the 'Add node' operation. Returns a computed result.
- **Input Parameters**: `skill` (`str`), `inputs` (`list[str]`), `metadata` (`dict | None`)
- **Output Type**: `str`

### Function: `mark`
- **Description**: *(Analyzed from source)* Performs the 'Mark' operation.
- **Input Parameters**: `nid` (`str`), `status` (`str`)
- **Output Type**: `None`

### Function: `ready_nodes`
- **Description**: *(Analyzed from source)* Performs the 'Ready nodes' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `list[str]`

### Function: `has_running`
- **Description**: *(Analyzed from source)* Performs the 'Has running' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `bool`

### Function: `extend_from`
- **Description**: Splice in dynamic successors, static internal_successors, and critic auto-insertion. Returns the list of new node ids.  Resolves label-based input references (`n:<label>`) against the `metadata.label` of nodes added in the same batch. The Planner is encouraged to name its nodes by label so it can reference them without knowing the integer ids the orchestrator will hand out.
- **Input Parameters**: `src_nid` (`str`), `result` (`AgentResult`)
- **Output Type**: `list[str]`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `registry` (`SkillRegistry | None`)
- **Output Type**: `Any`

### Function: `run`
- **Description**: *(Analyzed from source)* Performs the 'Run' operation. Returns a computed result. May raise exceptions under certain conditions. Includes logging or printing.
- **Input Parameters**: `query` (`str`)
- **Output Type**: `str`

### Function: `_run_one`
- **Description**: *(Analyzed from source)* Performs the ' run one' operation. Returns a computed result.
- **Input Parameters**: `nid` (`str`), `graph` (`Graph`), `sid` (`str`), `query` (`str`), `store` (`SessionStore`), `memory_hits` (`list`)
- **Output Type**: `tuple[Tuple[str, AgentResult, str]]`

## Module: `code/decision.py`

### Function: `_format_hits`
- **Description**: *(Analyzed from source)* Performs the ' format hits' operation. Returns a computed result.
- **Input Parameters**: `hits` (`list[MemoryItem]`)
- **Output Type**: `str`

### Function: `_format_history`
- **Description**: *(Analyzed from source)* Performs the ' format history' operation. Returns a computed result.
- **Input Parameters**: `history` (`list[dict]`)
- **Output Type**: `str`

### Function: `_format_attached`
- **Description**: *(Analyzed from source)* Performs the ' format attached' operation. Returns a computed result.
- **Input Parameters**: `attached` (`list[tuple[Tuple[str, bytes]]]`)
- **Output Type**: `str`

### Function: `next_step`
- **Description**: *(Analyzed from source)* Performs the 'Next step' operation. Returns a computed result.
- **Input Parameters**: `goal` (`Goal`), `hits` (`list[MemoryItem]`), `attached` (`list[tuple[Tuple[str, bytes]]]`), `history` (`list[dict]`), `mcp_tools` (`list[dict]`)
- **Output Type**: `DecisionOutput`

## Module: `code/action.py`

### Function: `_result_to_text`
- **Description**: Collapse an MCP CallToolResult into one text string.
- **Input Parameters**: `result` (`Any`)
- **Output Type**: `str`

### Function: `execute`
- **Description**: Run one MCP tool call. Returns (descriptor, artifact_id_or_None).  When the result is larger than ARTIFACT_THRESHOLD_BYTES, the full bytes are written to the artifact store and the returned descriptor is a short preview plus the artifact id.
- **Input Parameters**: `session` (`ClientSession`), `tool_call` (`ToolCall`)
- **Output Type**: `tuple[Tuple[str, str | None]]`

## Module: `code/sandbox.py`

### Function: `_truncate`
- **Description**: *(Analyzed from source)* Performs the ' truncate' operation. Returns a computed result.
- **Input Parameters**: `b` (`bytes`), `cap` (`int`)
- **Output Type**: `tuple[Tuple[str, bool]]`

### Function: `run_python`
- **Description**: Execute `code` in a subprocess. Returns a dict shaped for AgentResult.output:      {       "exit_code": int,       "stdout": str,             # decoded, possibly truncated       "stdout_truncated": bool,       "stderr": str,       "stderr_truncated": bool,       "files_written": [{"name": str, "size_bytes": int}, ...],       "timed_out": bool,       "cwd": str,                # the temp dir, kept for the artifact pipeline     }
- **Input Parameters**: `code` (`str`)
- **Output Type**: `dict`

## Module: `code/replay.py`

### Function: `_print_block`
- **Description**: *(Analyzed from source)* Performs the ' print block' operation. Includes logging or printing.
- **Input Parameters**: `i` (`int`), `n` (`int`), `st` (`NodeState`)
- **Output Type**: `None`

### Function: `_expand_prompt`
- **Description**: *(Analyzed from source)* Performs the ' expand prompt' operation. Includes logging or printing.
- **Input Parameters**: `st` (`NodeState`)
- **Output Type**: `None`

### Function: `_expand_output`
- **Description**: *(Analyzed from source)* Performs the ' expand output' operation. Includes logging or printing.
- **Input Parameters**: `st` (`NodeState`)
- **Output Type**: `None`

### Function: `replay`
- **Description**: *(Analyzed from source)* Performs the 'Replay' operation. Returns a computed result. Includes logging or printing.
- **Input Parameters**: `session_id` (`str`)
- **Output Type**: `int`

### Function: `main`
- **Description**: *(Analyzed from source)* Performs the 'Main' operation. Returns a computed result. Includes logging or printing.
- **Input Parameters**: `None`
- **Output Type**: `int`

## Module: `code/schemas.py`

### Function: `new_id`
- **Description**: *(Analyzed from source)* Performs the 'New id' operation. Returns a computed result.
- **Input Parameters**: `prefix` (`str`)
- **Output Type**: `str`

### Function: `all_done`
- **Description**: *(Analyzed from source)* Performs the 'All done' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `bool`

### Function: `next_unfinished`
- **Description**: *(Analyzed from source)* Performs the 'Next unfinished' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Goal | None`

### Function: `is_answer`
- **Description**: *(Analyzed from source)* Performs the 'Is answer' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `bool`

## Module: `code/artifacts.py`

### Function: `put`
- **Description**: Write blob (deduped by content hash) and return its handle.
- **Input Parameters**: `blob` (`bytes`)
- **Output Type**: `str`

### Function: `get_bytes`
- **Description**: *(Analyzed from source)* Performs the 'Get bytes' operation. Returns a computed result.
- **Input Parameters**: `artifact_id` (`str`)
- **Output Type**: `bytes`

### Function: `get_meta`
- **Description**: *(Analyzed from source)* Performs the 'Get meta' operation. Returns a computed result.
- **Input Parameters**: `artifact_id` (`str`)
- **Output Type**: `Artifact`

### Function: `exists`
- **Description**: *(Analyzed from source)* Performs the 'Exists' operation. Returns a computed result.
- **Input Parameters**: `artifact_id` (`str`)
- **Output Type**: `bool`

## Module: `code/perception.py`

### Function: `_snapshot_history`
- **Description**: *(Analyzed from source)* Performs the ' snapshot history' operation. Returns a computed result.
- **Input Parameters**: `history` (`list[dict]`)
- **Output Type**: `list[dict]`

### Function: `_snapshot_hits`
- **Description**: Render the memory hits the LLM sees. Artifacts are indexed (i) so Perception can point at them by integer; non-artifact hits show i=null.
- **Input Parameters**: `hits` (`list[MemoryItem]`)
- **Output Type**: `list[dict]`

### Function: `observe`
- **Description**: *(Analyzed from source)* Performs the 'Observe' operation. Returns a computed result.
- **Input Parameters**: `query` (`str`), `hits` (`list[MemoryItem]`), `history` (`list[dict]`), `prior_goals` (`list[Goal]`), `run_id` (`str`)
- **Output Type**: `Observation`

## Module: `code/mcp_runner.py`

### Function: `_dispatch_tool`
- **Description**: Run one MCP tool call and return its result as one text blob.
- **Input Parameters**: `session` (`ClientSession`), `name` (`str`), `args` (`dict`)
- **Output Type**: `str`

### Function: `run_with_tools`
- **Description**: Multi-turn chat: dispatch tool_calls via MCP, keep going until the model returns text. Returns the FINAL gateway reply dict (so callers can read `text`, `provider`, etc. the same way they would for a one-shot call).
- **Input Parameters**: `None`
- **Output Type**: `dict`

### Function: `_chat`
- **Description**: *(Analyzed from source)* Performs the ' chat' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `dict`

## Module: `code/mcp_server.py`

### Function: `_safe`
- **Description**: *(Analyzed from source)* Performs the ' safe' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `path` (`str`)
- **Output Type**: `Path`

### Function: `_empty_usage`
- **Description**: *(Analyzed from source)* Performs the ' empty usage' operation. Returns a computed result.
- **Input Parameters**: `month` (`str`)
- **Output Type**: `dict`

### Function: `_load_usage`
- **Description**: *(Analyzed from source)* Performs the ' load usage' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `dict`

### Function: `_save_usage`
- **Description**: *(Analyzed from source)* Performs the ' save usage' operation.
- **Input Parameters**: `data` (`dict`)
- **Output Type**: `None`

### Function: `_bump`
- **Description**: *(Analyzed from source)* Performs the ' bump' operation.
- **Input Parameters**: `provider` (`str`), `field` (`str`)
- **Output Type**: `None`

### Function: `_under_cap`
- **Description**: *(Analyzed from source)* Performs the ' under cap' operation. Returns a computed result.
- **Input Parameters**: `provider` (`str`)
- **Output Type**: `bool`

### Function: `_tavily_search`
- **Description**: *(Analyzed from source)* Performs the ' tavily search' operation. Returns a computed result.
- **Input Parameters**: `query` (`str`), `max_results` (`int`)
- **Output Type**: `list[dict]`

### Function: `_ddg_search`
- **Description**: *(Analyzed from source)* Performs the ' ddg search' operation. Returns a computed result.
- **Input Parameters**: `query` (`str`), `max_results` (`int`)
- **Output Type**: `list[dict]`

### Function: `_crawl4ai_fetch`
- **Description**: *(Analyzed from source)* Performs the ' crawl4ai fetch' operation. Returns a computed result.
- **Input Parameters**: `url` (`str`)
- **Output Type**: `dict`

### Function: `web_search`
- **Description**: Search the web (Tavily primary, DDG fallback). Hard-capped at 5 results. Example: web_search("python asyncio tutorial", 3).
- **Input Parameters**: `query` (`str`), `max_results` (`int`)
- **Output Type**: `list[dict]`

### Function: `fetch_url`
- **Description**: Fetch clean markdown from a URL via crawl4ai (headless Chromium). Example: fetch_url("https://example.com").
- **Input Parameters**: `url` (`str`), `timeout` (`int`)
- **Output Type**: `dict`

### Function: `get_time`
- **Description**: Current time in a named IANA timezone. Example: get_time("Asia/Kolkata").
- **Input Parameters**: `timezone` (`str`)
- **Output Type**: `dict`

### Function: `currency_convert`
- **Description**: Convert money between ISO-3 currencies via frankfurter.dev. Example: currency_convert(100, "USD", "INR").
- **Input Parameters**: `amount` (`float`), `from_currency` (`str`), `to_currency` (`str`)
- **Output Type**: `dict`

### Function: `read_file`
- **Description**: Read a UTF-8 text file from the sandbox. Example: read_file("notes.txt").
- **Input Parameters**: `path` (`str`)
- **Output Type**: `dict`

### Function: `list_dir`
- **Description**: List a directory inside the sandbox. Example: list_dir(".").
- **Input Parameters**: `path` (`str`)
- **Output Type**: `dict`

### Function: `create_file`
- **Description**: Create a new file in the sandbox; errors if it exists. Example: create_file("hello.txt", "hi").
- **Input Parameters**: `path` (`str`), `content` (`str`)
- **Output Type**: `dict`

### Function: `update_file`
- **Description**: Overwrite an existing sandbox file. Example: update_file("hello.txt", "new body").
- **Input Parameters**: `path` (`str`), `content` (`str`)
- **Output Type**: `dict`

### Function: `edit_file`
- **Description**: Find-and-replace inside a sandbox file. Example: edit_file("hello.txt", "foo", "bar").
- **Input Parameters**: `path` (`str`), `find` (`str`), `replace` (`str`), `replace_all` (`bool`)
- **Output Type**: `dict`

### Function: `_read_for_index`
- **Description**: Return (content, source_label) for an indexable file or artifact.
- **Input Parameters**: `path` (`str`)
- **Output Type**: `tuple[Tuple[str, str]]`

### Function: `_chunk_text`
- **Description**: Sliding-window chunking by word count. S7 default; semantic chunking arrives in Session 8.
- **Input Parameters**: `text` (`str`), `size` (`int`), `overlap` (`int`)
- **Output Type**: `list[str]`

### Function: `index_document`
- **Description**: Chunk a sandbox file or artifact and write each chunk into Memory as a searchable `fact`. Use this when the content must remain retrievable across later turns or runs (an indexing step before later vector queries). For one-shot inspection of a known file's contents in this turn, prefer `read_file` instead. Example: index_document("notes/spec.md").
- **Input Parameters**: `path` (`str`), `chunk_size` (`int`), `overlap` (`int`)
- **Output Type**: `dict`

### Function: `search_knowledge`
- **Description**: Vector search over indexed `fact` chunks. Returns up to k ranked chunks with provenance. Call this rather than re-fetching URLs or re-reading source files whenever Memory already contains indexed chunks for the topic — that is the whole point of having indexed the corpus. Example: search_knowledge("authentication flow", 5).
- **Input Parameters**: `query` (`str`), `k` (`int`)
- **Output Type**: `list[dict]`

## Module: `gateway/db.py`

### Function: `conn`
- **Description**: *(Analyzed from source)* Performs the 'Conn' operation. Yields data as a generator.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `init`
- **Description**: *(Analyzed from source)* Performs the 'Init' operation.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `log_call`
- **Description**: *(Analyzed from source)* Performs the 'Log call' operation.
- **Input Parameters**: `provider` (`Any`), `model` (`Any`), `input_tokens` (`Any`), `output_tokens` (`Any`), `latency_ms` (`Any`), `status` (`Any`), `error` (`Any`), `prompt_chars` (`Any`), `response_chars` (`Any`), `override` (`Any`), `attempted` (`Any`), `cache_create_tokens` (`Any`), `cache_read_tokens` (`Any`), `tool_calls` (`Any`), `reasoning_applied` (`Any`), `tool_dialect` (`Any`), `call_role` (`Any`), `router_decision` (`Any`), `embed_dim` (`Any`), `agent` (`Any`), `session` (`Any`), `retries` (`Any`)
- **Output Type**: `Any`

### Function: `by_agent`
- **Description**: V8: per-agent cost/token rollup. When `session` is set, scopes the rollup to a single flow-run; otherwise rolls up the calendar day.
- **Input Parameters**: `session` (`Any`), `since` (`Any`)
- **Output Type**: `Any`

### Function: `recent`
- **Description**: *(Analyzed from source)* Performs the 'Recent' operation. Returns a computed result.
- **Input Parameters**: `limit` (`Any`), `provider` (`Any`), `status` (`Any`)
- **Output Type**: `Any`

### Function: `aggregate`
- **Description**: *(Analyzed from source)* Performs the 'Aggregate' operation. Returns a computed result.
- **Input Parameters**: `call_role` (`Any`)
- **Output Type**: `Any`

## Module: `gateway/client.py`

### Function: `ask`
- **Description**: *(Analyzed from source)* Performs the 'Ask' operation. Returns a computed result.
- **Input Parameters**: `prompt` (`str`), `provider` (`str`), `**kw` (`Any`)
- **Output Type**: `str`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `base_url` (`str`), `timeout` (`float`)
- **Output Type**: `Any`

### Function: `chat`
- **Description**: *(Analyzed from source)* Performs the 'Chat' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `prompt` (`str`)
- **Output Type**: `dict`

### Function: `chat_batch`
- **Description**: Submit N chat requests to the gateway in a single round-trip. Each entry in `calls` is a dict matching ChatRequest. Returns the list of responses in input order; failed calls are returned as `{"error": ..., "status_code": ...}` rather than raising.
- **Input Parameters**: `calls` (`list[dict]`), `max_concurrency` (`int`)
- **Output Type**: `list[dict]`

### Function: `capabilities`
- **Description**: *(Analyzed from source)* Performs the 'Capabilities' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `cost_by_agent`
- **Description**: *(Analyzed from source)* Performs the 'Cost by agent' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `session` (`Optional[str]`)
- **Output Type**: `dict`

### Function: `embed`
- **Description**: Returns {provider, model, embedding, dim, latency_ms, attempted}.
- **Input Parameters**: `text` (`str`), `task_type` (`str`), `provider` (`Optional[str]`)
- **Output Type**: `dict`

## Module: `gateway/cache.py`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `ttl_seconds` (`int`)
- **Output Type**: `Any`

### Function: `_key`
- **Description**: *(Analyzed from source)* Performs the ' key' operation. Returns a computed result.
- **Input Parameters**: `model` (`str`), `text` (`str`)
- **Output Type**: `str`

### Function: `get_or_create`
- **Description**: Returns (cache_resource_name|None, cache_creation_input_tokens). cache_creation_input_tokens is non-zero only when we mint a fresh entry.
- **Input Parameters**: `api_key` (`str`), `model` (`str`), `text` (`str`), `base_url` (`str`)
- **Output Type**: `tuple[Tuple[Optional[str], int]]`

## Module: `gateway/embedders.py`

### Function: `build_embedders`
- **Description**: Return (ordered list of available embedders, ordered list of names).  Order is read from EMBED_ORDER env var (comma-separated names) and defaults to ['ollama', '<fallback>']. An embedder is included only if its prerequisites are satisfied (Ollama URL reachable in principle is not checked here; an unset GEMINI_API_KEY drops the fallback).
- **Input Parameters**: `None`
- **Output Type**: `tuple[Tuple[list[EmbeddingProvider], list[str]]]`

### Function: `embed_with_failover`
- **Description**: Run the failover ring with per-provider rate-state gating.  Returns (name, result_dict, attempts, latency_ms).  For each candidate:   - call `state.can_use()` first; if rate-limited / cooled-down / in backoff,     skip to the next candidate (and record the reason in `attempts`)   - on a real call success: `state.record()`  (resets backoff)   - on a real call failure: `state.mark_failure(reason)`  (bumps backoff)  If `explicit` is set, only that provider is tried — failure becomes a 502 / rate-limit becomes a 429; the gateway does not silently fall back when the caller pinned a provider.
- **Input Parameters**: `embedders` (`list[EmbeddingProvider]`), `text` (`str`), `task_type` (`TaskType`), `explicit` (`str | None`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `msg` (`str`), `status` (`int | None`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `rpm` (`int`), `cooldown` (`float`)
- **Output Type**: `Any`

### Function: `_gc`
- **Description**: *(Analyzed from source)* Performs the ' gc' operation.
- **Input Parameters**: `None`
- **Output Type**: `None`

### Function: `can_use`
- **Description**: *(Analyzed from source)* Performs the 'Can use' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `tuple[Tuple[bool, str]]`

### Function: `record`
- **Description**: Call on success. Resets any active backoff.
- **Input Parameters**: `None`
- **Output Type**: `None`

### Function: `mark_failure`
- **Description**: Call on failure. Pushes the backoff window forward by one step.
- **Input Parameters**: `reason` (`str`)
- **Output Type**: `None`

### Function: `snapshot`
- **Description**: *(Analyzed from source)* Performs the 'Snapshot' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `dict`

### Function: `embed`
- **Description**: *(Analyzed from source)* Performs the 'Embed' operation. May raise exceptions under certain conditions.
- **Input Parameters**: `text` (`str`), `task_type` (`TaskType`)
- **Output Type**: `dict`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `model` (`str`), `base_url` (`str`)
- **Output Type**: `Any`

### Function: `embed`
- **Description**: *(Analyzed from source)* Performs the 'Embed' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `text` (`str`), `task_type` (`TaskType`)
- **Output Type**: `dict`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `api_key` (`str`), `model` (`str`), `output_dim` (`int`), `rpm` (`int`), `cooldown` (`float`)
- **Output Type**: `Any`

### Function: `embed`
- **Description**: *(Analyzed from source)* Performs the 'Embed' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `text` (`str`), `task_type` (`TaskType`)
- **Output Type**: `dict`

## Module: `gateway/providers.py`

### Function: `_flatten_system`
- **Description**: Returns (joined_text, raw_blocks, has_cache_marker).
- **Input Parameters**: `system_blocks` (`Any`)
- **Output Type**: `tuple[Tuple[str, list[dict], bool]]`

### Function: `_empty_result`
- **Description**: *(Analyzed from source)* Performs the ' empty result' operation. Returns a computed result.
- **Input Parameters**: `model` (`str`)
- **Output Type**: `dict`

### Function: `_model_supports_reasoning`
- **Description**: *(Analyzed from source)* Performs the ' model supports reasoning' operation. Returns a computed result.
- **Input Parameters**: `model` (`str`)
- **Output Type**: `bool`

### Function: `_gemini_supports_thinking`
- **Description**: *(Analyzed from source)* Performs the ' gemini supports thinking' operation. Returns a computed result.
- **Input Parameters**: `model` (`str`)
- **Output Type**: `bool`

### Function: `_gemini_thinking_knob`
- **Description**: Returns 'level' for thinkingLevel-capable models (2.5-pro, 3.x non-lite), 'budget' for thinkingBudget-only models (2.5-flash), or None for non-thinking.
- **Input Parameters**: `model` (`str`)
- **Output Type**: `Optional[str]`

### Function: `_gemini_inline_refs`
- **Description**: Resolve `$ref` references to `$defs` / `definitions` inline.  Pydantic emits refs for nested models. Gemini's responseSchema endpoint rejects `$ref`, so we inline before cleaning. This must run BEFORE `_gemini_clean_schema` (which strips `$defs`).
- **Input Parameters**: `schema` (`dict`)
- **Output Type**: `dict`

### Function: `_gemini_clean_schema`
- **Description**: Strip JSON-Schema keys Gemini rejects, after inlining `$ref` / `$defs`.
- **Input Parameters**: `schema` (`dict`)
- **Output Type**: `dict`

### Function: `_coerce_obj`
- **Description**: *(Analyzed from source)* Performs the ' coerce obj' operation. Returns a computed result.
- **Input Parameters**: `v` (`Any`)
- **Output Type**: `Any`

### Function: `_ollama_native_tools`
- **Description**: *(Analyzed from source)* Performs the ' ollama native tools' operation. Returns a computed result.
- **Input Parameters**: `model` (`str`)
- **Output Type**: `bool`

### Function: `_prompted_tool_system`
- **Description**: *(Analyzed from source)* Performs the ' prompted tool system' operation. Returns a computed result.
- **Input Parameters**: `tools` (`Any`)
- **Output Type**: `Any`

### Function: `_parse_prompted_tool_call`
- **Description**: *(Analyzed from source)* Performs the ' parse prompted tool call' operation. Returns a computed result.
- **Input Parameters**: `text` (`str`)
- **Output Type**: `Any`

### Function: `model_capabilities`
- **Description**: *(Analyzed from source)* Performs the 'Model capabilities' operation. Returns a computed result.
- **Input Parameters**: `provider_name` (`str`), `model` (`str`), `default_caps` (`dict`)
- **Output Type**: `dict`

### Function: `build_providers`
- **Description**: Worker pool — the LLMs that do real work for the agent.  V3 changes vs V2: - cerebras worker default: zai-glm-4.7 (was qwen-3-235b-a22b-instruct-2507, deprecating May 27 2026) - groq worker default: openai/gpt-oss-120b (was llama-3.3-70b-versatile, now moved to router pool)
- **Input Parameters**: `cache_store` (`Any`)
- **Output Type**: `Any`

### Function: `build_router_providers`
- **Description**: Router pool — same provider classes as workers, but separate instances with router-specific (smaller/faster) model defaults. Uses the same API keys as workers; per-provider rate budgets are independent because the providers we picked (Cerebras, Groq, NVIDIA, GitHub) all meter per-model, not per-key.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `msg` (`Any`), `status` (`Any`), `retryable` (`Any`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `api_key` (`str`), `model` (`str`), `base_url` (`str`)
- **Output Type**: `Any`

### Function: `chat`
- **Description**: *(Analyzed from source)* Performs the 'Chat' operation. May raise exceptions under certain conditions.
- **Input Parameters**: `messages` (`Any`)
- **Output Type**: `dict`

### Function: `stream`
- **Description**: *(Analyzed from source)* Performs the 'Stream' operation. Yields data as a generator.
- **Input Parameters**: `messages` (`Any`)
- **Output Type**: `AsyncIterator[str]`

### Function: `_headers`
- **Description**: *(Analyzed from source)* Performs the ' headers' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `_translate_tools`
- **Description**: *(Analyzed from source)* Performs the ' translate tools' operation. Returns a computed result.
- **Input Parameters**: `tools` (`Any`)
- **Output Type**: `Any`

### Function: `_translate_messages`
- **Description**: Translate canonical messages (incl role=tool) to OpenAI shape.
- **Input Parameters**: `messages` (`Any`), `system_text` (`Any`)
- **Output Type**: `Any`

### Function: `_apply_response_format`
- **Description**: *(Analyzed from source)* Performs the ' apply response format' operation. Returns a computed result.
- **Input Parameters**: `body` (`Any`), `response_format` (`Any`)
- **Output Type**: `Any`

### Function: `_apply_reasoning`
- **Description**: *(Analyzed from source)* Performs the ' apply reasoning' operation. Returns a computed result.
- **Input Parameters**: `body` (`Any`), `reasoning` (`Any`), `model` (`Any`)
- **Output Type**: `Any`

### Function: `chat`
- **Description**: *(Analyzed from source)* Performs the 'Chat' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `messages` (`Any`)
- **Output Type**: `Any`

### Function: `stream`
- **Description**: *(Analyzed from source)* Performs the 'Stream' operation. Returns a computed result. Yields data as a generator. May raise exceptions under certain conditions.
- **Input Parameters**: `messages` (`Any`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `api_key` (`Any`), `model` (`Any`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `api_key` (`Any`), `model` (`Any`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `api_key` (`Any`), `model` (`Any`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `api_key` (`Any`), `model` (`Any`)
- **Output Type**: `Any`

### Function: `_headers`
- **Description**: *(Analyzed from source)* Performs the ' headers' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `api_key` (`Any`), `model` (`Any`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `api_key` (`Any`), `model` (`Any`), `cache_store` (`Any`)
- **Output Type**: `Any`

### Function: `_translate_tools`
- **Description**: *(Analyzed from source)* Performs the ' translate tools' operation. Returns a computed result.
- **Input Parameters**: `tools` (`Any`)
- **Output Type**: `Any`

### Function: `_translate_messages`
- **Description**: *(Analyzed from source)* Performs the ' translate messages' operation. Returns a computed result.
- **Input Parameters**: `messages` (`Any`)
- **Output Type**: `Any`

### Function: `chat`
- **Description**: *(Analyzed from source)* Performs the 'Chat' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `messages` (`Any`)
- **Output Type**: `Any`

### Function: `walk`
- **Description**: *(Analyzed from source)* Performs the 'Walk' operation. Returns a computed result.
- **Input Parameters**: `node` (`Any`), `seen` (`frozenset[str]`)
- **Output Type**: `dict | list`

### Function: `strip`
- **Description**: *(Analyzed from source)* Performs the 'Strip' operation. Returns a computed result.
- **Input Parameters**: `node` (`Any`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `model` (`Any`), `base_url` (`Any`)
- **Output Type**: `Any`

### Function: `_translate_messages`
- **Description**: *(Analyzed from source)* Performs the ' translate messages' operation. Returns a computed result.
- **Input Parameters**: `messages` (`Any`), `system_text` (`Any`), `prompted_fallback` (`Any`)
- **Output Type**: `Any`

### Function: `chat`
- **Description**: *(Analyzed from source)* Performs the 'Chat' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `messages` (`Any`)
- **Output Type**: `Any`

## Module: `gateway/router.py`

### Function: `resolve`
- **Description**: *(Analyzed from source)* Performs the 'Resolve' operation. Returns a computed result.
- **Input Parameters**: `name` (`Any`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `_day_start`
- **Description**: *(Analyzed from source)* Performs the ' day start' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `gc`
- **Description**: *(Analyzed from source)* Performs the 'Gc' operation.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `can_use`
- **Description**: *(Analyzed from source)* Performs the 'Can use' operation. Returns a computed result.
- **Input Parameters**: `limits` (`Any`), `est_tokens` (`Any`)
- **Output Type**: `Any`

### Function: `record`
- **Description**: *(Analyzed from source)* Performs the 'Record' operation.
- **Input Parameters**: `tokens` (`Any`)
- **Output Type**: `Any`

### Function: `mark_unavailable`
- **Description**: *(Analyzed from source)* Performs the 'Mark unavailable' operation.
- **Input Parameters**: `seconds` (`float`), `reason` (`str`)
- **Output Type**: `Any`

### Function: `snapshot`
- **Description**: *(Analyzed from source)* Performs the 'Snapshot' operation. Returns a computed result.
- **Input Parameters**: `limits` (`Any`)
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `providers` (`dict`), `order` (`list[str]`)
- **Output Type**: `Any`

### Function: `candidates`
- **Description**: *(Analyzed from source)* Performs the 'Candidates' operation. Returns a computed result.
- **Input Parameters**: `override` (`Any`)
- **Output Type**: `Any`

### Function: `pick`
- **Description**: *(Analyzed from source)* Performs the 'Pick' operation. Returns a computed result.
- **Input Parameters**: `est_tokens` (`Any`), `candidates` (`Any`), `required_caps` (`list[str] | None`)
- **Output Type**: `Any`

### Function: `all_status`
- **Description**: *(Analyzed from source)* Performs the 'All status' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `__init__`
- **Description**: *(Analyzed from source)* Performs the '  init  ' operation.
- **Input Parameters**: `providers` (`dict`), `order` (`list[str]`)
- **Output Type**: `Any`

### Function: `candidates`
- **Description**: *(Analyzed from source)* Performs the 'Candidates' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `pick`
- **Description**: Pick first available router provider. Caps require nothing — router LLMs only need to emit one word, no tools/reasoning/structured needed.
- **Input Parameters**: `est_tokens` (`Any`)
- **Output Type**: `Any`

### Function: `all_status`
- **Description**: *(Analyzed from source)* Performs the 'All status' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

## Module: `gateway/main.py`

### Function: `_estimate_tokens`
- **Description**: words * 1.4 — deliberately rough. The router sample handles the cases where rough isn't good enough (code, CJK, base64).
- **Input Parameters**: `text` (`str`)
- **Output Type**: `int`

### Function: `_build_sample`
- **Description**: *(Analyzed from source)* Performs the ' build sample' operation. Returns a computed result.
- **Input Parameters**: `text` (`str`)
- **Output Type**: `str`

### Function: `_tier_from_count`
- **Description**: Deterministic fallback when the router LLM is unreachable or replies with garbage. Pure token-count rule, identical thresholds.
- **Input Parameters**: `tokens` (`int`)
- **Output Type**: `str`

### Function: `_parse_tier`
- **Description**: *(Analyzed from source)* Performs the ' parse tier' operation. Returns a computed result.
- **Input Parameters**: `text` (`str`)
- **Output Type**: `Optional[str]`

### Function: `_classify_tier`
- **Description**: Run a router-LLM classification. Returns a RouterDecision (without chosen_worker_* fields, which are filled in by the caller after worker pick).  Failover: try each router provider in order. Only fall back to the pure token-count rule when all routers in the pool have failed.
- **Input Parameters**: `req` (`ChatRequest`), `role` (`str`), `router_pool` (`RouterPool`), `prompt_text` (`str`)
- **Output Type**: `Any`

### Function: `lifespan`
- **Description**: *(Analyzed from source)* Performs the 'Lifespan' operation. Yields data as a generator.
- **Input Parameters**: `app` (`FastAPI`)
- **Output Type**: `Any`

### Function: `_normalize_messages`
- **Description**: *(Analyzed from source)* Performs the ' normalize messages' operation. Returns a computed result.
- **Input Parameters**: `req` (`ChatRequest`)
- **Output Type**: `Any`

### Function: `_system_blocks`
- **Description**: Returns the system_blocks payload to hand to the provider adapter.
- **Input Parameters**: `req` (`ChatRequest`)
- **Output Type**: `Any`

### Function: `_est_tokens`
- **Description**: *(Analyzed from source)* Performs the ' est tokens' operation. Returns a computed result.
- **Input Parameters**: `messages` (`Any`), `system_blocks` (`Any`), `max_tokens` (`Any`)
- **Output Type**: `Any`

### Function: `_backoff_for`
- **Description**: *(Analyzed from source)* Performs the ' backoff for' operation. Returns a computed result.
- **Input Parameters**: `err` (`Exception`), `has_model_override` (`bool`)
- **Output Type**: `Any`

### Function: `_attempts_str`
- **Description**: *(Analyzed from source)* Performs the ' attempts str' operation. Returns a computed result.
- **Input Parameters**: `attempts` (`Any`)
- **Output Type**: `Any`

### Function: `_required_caps`
- **Description**: *(Analyzed from source)* Performs the ' required caps' operation. Returns a computed result.
- **Input Parameters**: `req` (`ChatRequest`)
- **Output Type**: `Any`

### Function: `_validate_structured`
- **Description**: *(Analyzed from source)* Performs the ' validate structured' operation. Returns a computed result. May raise exceptions under certain conditions.
- **Input Parameters**: `text` (`str`), `schema` (`dict`)
- **Output Type**: `Any`

### Function: `chat`
- **Description**: *(Analyzed from source)* Performs the 'Chat' operation. Returns a computed result. Yields data as a generator. May raise exceptions under certain conditions.
- **Input Parameters**: `req` (`ChatRequest`)
- **Output Type**: `Any`

### Function: `chat_batch`
- **Description**: Run N chat requests concurrently with bounded parallelism. The gateway manages the rate-limit ladder centrally so callers do not need to open their own connection pools. Results are returned IN INPUT ORDER. Each inner call goes through the same `/v1/chat` pipeline (agent routing, retry, failover, db logging) — this endpoint is sugar on top.
- **Input Parameters**: `req` (`BatchChatRequest`)
- **Output Type**: `Any`

### Function: `cost_by_agent`
- **Description**: Per-agent rollup. With ?session=<sid> the rollup is scoped to one flow-run; without it, the calendar day. Used by the orchestrator's replay step to show how much each skill cost.
- **Input Parameters**: `session` (`Optional[str]`)
- **Output Type**: `Any`

### Function: `embed`
- **Description**: Single new V7 endpoint. Failover ring runs Ollama → configured fallback. `provider` pins the choice (returns 502 on failure with no fallback). Rejects inputs over MAX_INPUT_CHARS with 413 — caller must chunk.
- **Input Parameters**: `req` (`EmbedRequest`)
- **Output Type**: `Any`

### Function: `list_embedders`
- **Description**: *(Analyzed from source)* Performs the 'List embedders' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `list_providers`
- **Description**: *(Analyzed from source)* Performs the 'List providers' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `capabilities`
- **Description**: *(Analyzed from source)* Performs the 'Capabilities' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `status`
- **Description**: *(Analyzed from source)* Performs the 'Status' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `routers`
- **Description**: V3: router pool — separate from the worker pool. Shows which router LLMs are wired, the failover order, and live rate-state.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `calls`
- **Description**: *(Analyzed from source)* Performs the 'Calls' operation. Returns a computed result.
- **Input Parameters**: `limit` (`int`), `provider` (`Optional[str]`), `status` (`Optional[str]`)
- **Output Type**: `Any`

### Function: `index`
- **Description**: *(Analyzed from source)* Performs the 'Index' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `help_page`
- **Description**: *(Analyzed from source)* Performs the 'Help page' operation. Returns a computed result.
- **Input Parameters**: `None`
- **Output Type**: `Any`

### Function: `_one`
- **Description**: *(Analyzed from source)* Performs the ' one' operation. Returns a computed result.
- **Input Parameters**: `call` (`ChatRequest`)
- **Output Type**: `Any`

### Function: `gen`
- **Description**: *(Analyzed from source)* Performs the 'Gen' operation. Yields data as a generator.
- **Input Parameters**: `None`
- **Output Type**: `Any`
