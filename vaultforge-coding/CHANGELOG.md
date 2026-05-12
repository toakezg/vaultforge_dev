# Changelog

## 2026-05-13

- Added `src/vf_code_bridge/tool_runtime.py` and the `vaultforge-tool` console
  entry point for running fixed local tools from the generated tool catalog.
- Added selector mode for `vaultforge-tool` so batches can be chosen by family,
  priority, operation, and limit instead of manually passing every tool name.
- Added read-only catalog listing mode with `vaultforge-tool --list` for quick
  filtered handoffs before a build batch is selected.
- Added `tests/test_tool_runtime.py` covering catalog loading, scan/validate,
  dry versus live export, live batch result storage, selector filtering, list
  mode, and blocked outside-root targets.
- Live-tested four local example batches under
  `tools/example-tool-result-build`: 30 registry tools, 20 `.4` queue tools,
  20 cost-route tools, and 20 tool-builder tools.
- Added `tools/tool-runtime-build-status.md` to record the runtime surface,
  supported operations, example batches, verification commands, and next build
  slice.
- Added the first `tool-list-to-builder-workflow` pass over
  `tools/tool-list.md`, generating tagged JSONL index and compact contract
  artifacts for all 1,825 listed tools.
- Added `tools/tool-list-builder-workflow.md` as the pre-build sweep report
  covering catalog integrity, merge candidates, near-duplicates, inferred
  priority/safety/family/shape tags, shared-handler groups, and next sweep
  guidance without selecting or implementing a first build batch.
- Linked the generated workflow artifacts from the top of `tools/tool-list.md`
  so future builder threads can use the structured index and contract layer
  without reparsing the raw catalog.

## 2026-04-17

- Split run artifacts into `assets\runs\live` for active outputs and
  `assets\runs\examples` for sample/reference artifacts, then moved the first
  sample run artifact into the examples folder.
- Added env-backed config loading with validated overrides for section name,
  provider, model, token-rate fields, and prompt/run/event/report paths while
  preserving repo-local defaults when env values are absent.
- Updated the bridge and CLI to load runtime config deterministically and fail
  with clear config errors when invalid env values are present.
- Implemented the first local tracking MVP: each local execution can now write
  a per-run JSON artifact under `assets\runs\live`, append lifecycle events to
  `assets\events\events.jsonl`, and rebuild `assets\reports\usage_summary.json`
  from stored run records.
- Replaced the placeholder usage/event helpers with typed run, event, usage,
  and section-summary models plus configurable token-cost rate defaults.
- Wired the CLI through a smoke-safe local execution path that accepts manual
  usage values without faking external API retrieval.
- Added bridge-level tests for completed and failed local runs plus coverage for
  usage normalization, summary rebuilding, config overrides, and event JSONL
  appends.
- Scaffolded the `vaultforge-code` Python project under `src\vf_code_bridge`
  with module placeholders for CLI, config, prompt discovery, context building,
  bridge orchestration, usage tracking, event shaping, and file operations.
- Added the initial bridge asset layout under `assets\prompts`, `assets\runs`,
  `assets\reports`, and `assets\events`.
- Added `pyproject.toml`, `requirements.txt`, and `VERIFICATION.md` so the
  section has an install shape, smoke-test guidance, and a clear MVP boundary.
- Added lightweight smoke tests for scaffolded config, context, usage, and
  event modules.

## 2026-04-16

- Promoted `vaultforge-coding` into the VaultForge Code section.
- Added the first section doc set: `README.md`, `CODEX_START.md`, `SYSTEM.md`,
  `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.
- Revised the section docs around
  `vaultforge_code_codex_api_bridge_spec_v_2.md`.
- Reframed the section as the work/execution and factual-reporting side of the
  bridge, with structured event emission included but XP interpretation kept out
  of scope for a future sibling `vaultforge-xp4l` section.
- Locked the naming note that keeps the folder path as `vaultforge-coding\`
  while the section and bridge identity are `VaultForge Code` / `vaultforge-code`.
