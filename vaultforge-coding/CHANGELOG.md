# Changelog

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
