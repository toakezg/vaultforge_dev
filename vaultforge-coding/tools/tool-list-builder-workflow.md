# Tool List Builder Workflow Pass

Status: generated pre-build sweep from `tools/tool-list.md`.
Phase: merge, tagging, detail, and shared-handler grouping. No implementation performed.

## Source Integrity
- Source: `tools/tool-list.md`
- Tool entries parsed: 1825
- ID range: T0001-T1825
- Missing IDs: 0
- Duplicate tool names: 0
- Categories: 37

## Generated Artifacts
- `tools/tool-list-index.jsonl`: one JSONL record per tool with inferred priority, safety, family, shape, and shared-handler key.
- `tools/tool-list-contracts.jsonl`: one JSONL compact contract per tool using `inputs | outputs | reads | writes | blocked | proof`.

## Tag Summary

Priority tags:
- p1-high-use: 905
- p0-foundation: 555
- p3-later: 235
- p2-specialized: 130

Safety tags:
- read-only: 1462
- preview-write: 369
- external-gated: 175
- live-write-gated: 61
- paid-gated: 60
- destructive-blocked: 25

Implementation shapes:
- path-list: 365
- status-summary: 365
- handoff-pack: 365
- markdown-report: 351
- diff-summary: 200
- routing-decision: 165
- queue-report: 14

Top families:
- cost-route: 100
- dot4-queue: 75
- vaultforge-section: 65
- codex-run: 65
- mcp-proof: 55
- obsidian-plugin: 55
- windows-local: 55
- builder-packet: 55
- registry: 50
- workspace-discovery: 50
- context-pack: 50
- prompt-handoff: 50
- run-artifact: 50
- requirements: 50
- verification: 50
- review: 50
- docs: 50
- git-change: 50
- environment: 50
- security-privacy: 50

## Merge Candidate Sweep

Repeated operation families should usually share handler substrates while keeping separate fixed contracts. Highest-yield groups:
- cost-route::scan::path-list: 20 tools
- cost-route::validate::status-summary: 20 tools
- cost-route::summarize::handoff-pack: 20 tools
- cost-route::export::markdown-report: 20 tools
- dot4-queue::scan::path-list: 15 tools
- dot4-queue::validate::status-summary: 15 tools
- dot4-queue::summarize::handoff-pack: 15 tools
- dot4-queue::route::routing-decision: 15 tools
- vaultforge-section::scan::path-list: 13 tools
- vaultforge-section::validate::status-summary: 13 tools
- vaultforge-section::summarize::handoff-pack: 13 tools
- vaultforge-section::route::routing-decision: 13 tools
- codex-run::scan::path-list: 13 tools
- codex-run::validate::status-summary: 13 tools
- codex-run::summarize::handoff-pack: 13 tools
- codex-run::route::routing-decision: 13 tools
- codex-run::export::markdown-report: 13 tools
- vaultforge-section::export::markdown-report: 12 tools
- mcp-proof::scan::path-list: 11 tools
- mcp-proof::validate::status-summary: 11 tools
- mcp-proof::summarize::handoff-pack: 11 tools
- mcp-proof::route::routing-decision: 11 tools
- obsidian-plugin::scan::path-list: 11 tools
- obsidian-plugin::validate::status-summary: 11 tools
- obsidian-plugin::summarize::handoff-pack: 11 tools
- obsidian-plugin::route::routing-decision: 11 tools
- obsidian-plugin::export::markdown-report: 11 tools
- windows-local::scan::path-list: 11 tools
- windows-local::validate::status-summary: 11 tools
- windows-local::summarize::handoff-pack: 11 tools
- windows-local::route::routing-decision: 11 tools
- builder-packet::scan::path-list: 11 tools
- builder-packet::validate::status-summary: 11 tools
- builder-packet::summarize::handoff-pack: 11 tools
- builder-packet::route::routing-decision: 11 tools
- builder-packet::export::markdown-report: 11 tools
- registry::scan::path-list: 10 tools
- registry::validate::status-summary: 10 tools
- registry::summarize::handoff-pack: 10 tools
- registry::diff::diff-summary: 10 tools

Common handler rule: do not create broad arbitrary runners. Shared handlers should dispatch through fixed tool names, fixed schemas, allowlisted roots, and representative tests.

## Near-Duplicate Sweep

These are not automatic deletions. Treat them as family-link or merge-review candidates during the next pass:
- `quest-notes`: 10 tools across 2 categories; sample T0916, T0917, T0918, T0919, T0920, T1641, T1642, T1643
- `acceptance-criteria`: 5 tools across 1 categories; sample T0306, T0307, T0308, T0309, T0310
- `acceptance-prompts`: 5 tools across 1 categories; sample T0191, T0192, T0193, T0194, T0195
- `accessibility-labels`: 5 tools across 1 categories; sample T0781, T0782, T0783, T0784, T0785
- `agent-interruption`: 5 tools across 1 categories; sample T1091, T1092, T1093, T1094, T1095
- `agent-roles`: 5 tools across 1 categories; sample T0701, T0702, T0703, T0704, T0705
- `api-changes`: 5 tools across 1 categories; sample T0436, T0437, T0438, T0439, T0440
- `api-docs`: 5 tools across 1 categories; sample T0456, T0457, T0458, T0459, T0460
- `api-endpoints`: 5 tools across 1 categories; sample T0756, T0757, T0758, T0759, T0760
- `archive-snapshots`: 5 tools across 1 categories; sample T1616, T1617, T1618, T1619, T1620
- `argument-parsers`: 5 tools across 1 categories; sample T1501, T1502, T1503, T1504, T1505
- `artifact-evidence`: 5 tools across 1 categories; sample T1491, T1492, T1493, T1494, T1495
- `artifact-ids`: 5 tools across 1 categories; sample T0291, T0292, T0293, T0294, T0295
- `artifact-packet`: 5 tools across 1 categories; sample T1436, T1437, T1438, T1439, T1440
- `artifact-replay`: 5 tools across 1 categories; sample T1816, T1817, T1818, T1819, T1820
- `asset-checks`: 5 tools across 1 categories; sample T1591, T1592, T1593, T1594, T1595
- `asset-exports`: 5 tools across 1 categories; sample T1736, T1737, T1738, T1739, T1740
- `asset-files`: 5 tools across 1 categories; sample T0081, T0082, T0083, T0084, T0085
- `assumptions`: 5 tools across 1 categories; sample T0321, T0322, T0323, T0324, T0325
- `audit-trails`: 5 tools across 1 categories; sample T0646, T0647, T0648, T0649, T0650
- `auth-gates`: 5 tools across 1 categories; sample T0791, T0792, T0793, T0794, T0795
- `auth-state`: 5 tools across 1 categories; sample T1156, T1157, T1158, T1159, T1160
- `backlink-checks`: 5 tools across 1 categories; sample T0941, T0942, T0943, T0944, T0945
- `batch-manifests`: 5 tools across 1 categories; sample T1791, T1792, T1793, T1794, T1795
- `batch-planners`: 5 tools across 1 categories; sample T0991, T0992, T0993, T0994, T0995
- `batch-wrappers`: 5 tools across 1 categories; sample T1336, T1337, T1338, T1339, T1340
- `behavior-deltas`: 5 tools across 1 categories; sample T1456, T1457, T1458, T1459, T1460
- `blame-context`: 5 tools across 1 categories; sample T0531, T0532, T0533, T0534, T0535
- `blockers`: 5 tools across 1 categories; sample T0331, T0332, T0333, T0334, T0335
- `branch-info`: 5 tools across 1 categories; sample T0506, T0507, T0508, T0509, T0510

## Detail Sweep Readiness

- Every parsed tool now has an inferred compact contract in `tools/tool-list-contracts.jsonl`.
- Contracts are intentionally conservative and should be tightened with exact roots, schemas, and proof commands during detailed sweeps.
- Live-write, external connector, paid API, tunnel, destructive, and broad filesystem behaviors remain gated in generated contracts.

## Batch Selection Status

- No first build batch was written back into `tools/tool-list.md` in this pass.
- The list is now ready for a human-approved first batch selection or a focused detail sweep by family.
- Recommended next sweep target: p0-foundation tools in families `registry`, `tool-builder`, `cost-route`, `run-artifact`, `context-pack`, and `dot4-queue`.

## Suggested Next Commands

```powershell
$tools = Get-Content .\tools\tool-list-index.jsonl | ConvertFrom-Json
$tools | Group-Object family | Sort-Object Count -Descending | Select-Object Count,Name
$tools | Where-Object priority_tag -eq "p0-foundation" | Group-Object family | Sort-Object Count -Descending
$contracts = Get-Content .\tools\tool-list-contracts.jsonl | ConvertFrom-Json
$contracts | Where-Object family -eq "dot4-queue" | Select-Object id,tool,operation,implementation_shape
```
