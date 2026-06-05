import ast
import os
import json
from collections import defaultdict

ROOT = "/Users/avi/Documents/SessionNotes/Session8/MultiAgentDAGOrchestrationandSkillCatalogs"

# Step 1: collect all function definitions with fully qualified names
functions = {}
for dirpath, _, filenames in os.walk(ROOT):
    if "venv" in dirpath or "tests" in dirpath:
        continue
    for fn in filenames:
        if fn.endswith('.py'):
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, ROOT)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    source = f.read()
                tree = ast.parse(source)
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        func_name = node.name
                        full_name = f"{rel}::{func_name}"  # module path :: func
                        functions[full_name] = {'node': node, 'calls': set()}
            except Exception as e:
                pass

# Step 2: walk again to gather calls inside each function
for full_name, info in list(functions.items()):
    node = info['node']
    # find calls within function body
    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            # simple name resolution
            if isinstance(child.func, ast.Name):
                called = child.func.id
            elif isinstance(child.func, ast.Attribute):
                # get attribute name only (e.g., self.foo)
                called = child.func.attr
            else:
                continue
            # try to find a matching function in our set (same name)
            matches = [k for k in functions if k.endswith('::' + called)]
            for m in matches:
                info['calls'].add(m)

# Build adjacency list for mermaid
edges = []
for src, data in functions.items():
    for dst in data['calls']:
        edges.append((src, dst))

# Group by module for subgraph
module_groups = defaultdict(list)
for fn in functions:
    mod = fn.split('::')[0]
    module_groups[mod].append(fn.split('::')[1])

# Generate markdown with mermaid diagram
lines = ["# Function Call Mapping Graph", "", "```mermaid", "graph TD"]
# subgraph per module
for mod, funcs in module_groups.items():
    safe_mod = mod.replace('/', '_').replace('.', '_')
    lines.append(f"    subgraph {safe_mod}[{mod}]")
    for f in funcs:
        node_id = f"{safe_mod}_{f}".replace('-', '_')
        lines.append(f"        {node_id}[{f}]")
    lines.append("    end")
# edges
for src, dst in edges:
    src_mod, src_fun = src.split('::')
    dst_mod, dst_fun = dst.split('::')
    src_id = f"{src_mod.replace('/', '_').replace('.', '_')}_{src_fun}".replace('-', '_')
    dst_id = f"{dst_mod.replace('/', '_').replace('.', '_')}_{dst_fun}".replace('-', '_')
    lines.append(f"    {src_id} --> {dst_id}")
lines.append("```")

out_path = os.path.join(ROOT, "function_call_mapping.md")
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Mapping written to {out_path}")
