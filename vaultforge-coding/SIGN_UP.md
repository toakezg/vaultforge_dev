# VaultForge Code Sign Up

New coding-section threads should add a short entry here before or after their
first meaningful change.

Use this shape:

```text
## YYYY-MM-DD - thread label

- Role:
- Scope:
- Read:
- Changed:
- Handoff:
```

## 2026-04-16 - section promotion setup

- Role: promote `vaultforge-coding` into the VaultForge Code section
- Scope: section docs, root handoff, naming note, and startup requirements
- Read: root startup docs, root thread map, the code bridge spec, and the
  foundation-pack material
- Changed: added the first local section doc set and grounded it in the bridge
  MVP spec, then realigned it to the v2 execution/reporting boundary
- Handoff: the next coding thread should scaffold the bridge project, including
  neutral event emission, without modifying unrelated VaultForge sections or
  pulling XP interpretation into this lane

## 2026-04-17 - bridge skeleton scaffold

- Role: scaffold the first working package layout for `vaultforge-code`
- Scope: Python package structure, prompt assets, asset folders, verification
  notes, and smoke-testable placeholders
- Read: root `CODEX_START.md`, root `SYSTEM.md`, root `THREAD_MAP.md`,
  section `CODEX_START.md`, `README.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`,
  `CHANGELOG.md`, `SIGN_UP.md`, and
  `vaultforge_code_codex_api_bridge_spec_v_2.md`
- Changed: added `pyproject.toml`, `requirements.txt`, `VERIFICATION.md`,
  prompt presets, scaffold modules under `src\vf_code_bridge`, and placeholder
  tests under `tests\`
- Handoff: build config loading and environment-backed path resolution next, then
  wire prompt compilation and bridge execution without adding write-capable file
  mutation or XP interpretation

## 2026-05-13 - tool-list builder workflow pass

- Role: apply `tool-list-to-builder-workflow` to the local tool catalog
- Scope: listing/pre-build artifacts only; no tool implementation and no first
  build batch selection
- Read: `CODEX_START.md`, `README.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`,
  `CHANGELOG.md`, `SIGN_UP.md`, `VERIFICATION.md`,
  `vaultforge_code_codex_api_bridge_spec_v_2.md`, and `tools/tool-list.md`
- Changed: generated `tools/tool-list-builder-workflow.md`,
  `tools/tool-list-index.jsonl`, and `tools/tool-list-contracts.jsonl`, then
  linked those artifacts from `tools/tool-list.md`
- Handoff: use the generated index and contracts for the next merge/detail
  sweep; do not build tools until a bounded batch is explicitly selected

## 2026-05-13 - fixed tool runtime build

- Role: build the first local fixed-contract tool runtime and live example
  batch surface
- Scope: `vaultforge-tool`, generated catalog execution, local dry/live examples,
  tests, and status docs; no external MCP/GPT live calls
- Read: section operating docs, generated tool index/contracts, and the
  tool-list builder workflow report
- Changed: added `src/vf_code_bridge/tool_runtime.py`,
  `tests/test_tool_runtime.py`, `tools/tool-runtime-build-status.md`, and
  `tools/example-tool-result-build/` examples; updated `pyproject.toml`,
  `README.md`, `CHANGELOG.md`, `SIGN_UP.md`, and `tools/tool-list.md`
- Handoff: next cycle should enrich family-specific validation and catalog
  status/export summaries before attempting live external or write-capable
  integrations
