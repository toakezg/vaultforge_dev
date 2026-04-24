# VaultForge Code

`vaultforge-coding\` is the home of the VaultForge Code section.

The folder path stays `vaultforge-coding` to match the current workspace
layout. The section identity and bridge name are `VaultForge Code`.

## Goal

Build a local-first coding bridge that lets VaultForge run Codex-style coding
and automation tasks through an OpenAI API key using the Responses API instead
of relying only on ChatGPT/Codex weekly limits.

The bridge should stay:

- local-first
- Windows-friendly
- usable from terminal, batch files, and Obsidian Shell Commands
- safe by default
- easy to extend later into reports, queues, and downstream event handoffs

## Section Role

This section owns the VaultForge Code bridge work:

- bridge docs and planning
- Python project structure for the bridge
- prompt presets such as `review`, `implement`, `tighten`, `audit`, and
  `scaffold`
- local project-context building
- run-folder outputs, logs, metadata, and usage tracking
- structured activity event emission for downstream sections
- batch launchers and operator-facing bridge entry points

This section reports what happened during a run.

It should not own the deeper interpretation layer for XP, achievements, quests,
rewards, or dashboard logic. That belongs in a separate sibling section:
`vaultforge-xp4l`, when that lane exists.

## Current Status

- the implementation spec is captured in
  `vaultforge_code_codex_api_bridge_spec_v_2.md`
- the section is now promoted with its own doc set
- the bridge project now has a scaffolded Python package, prompt assets,
  placeholder tests, and verification notes
- the local tracking MVP now writes live run artifacts under
  `assets\runs\live`, keeps sample artifacts under `assets\runs\examples`,
  appends neutral lifecycle events to `assets\events\events.jsonl`, and
  rebuilds `assets\reports\usage_summary.json`
- environment-backed config loading now supports repo-local defaults plus
  validated overrides for section/model/provider, token rates, and asset paths
- prompt compilation, broader context collection, and OpenAI Responses API
  execution are still ahead

## Config Inputs

Optional environment overrides now cover:

- `VF_CODE_SECTION_NAME`
- `VF_CODE_PROVIDER`
- `VF_CODE_MODEL`
- `VF_CODE_INPUT_RATE`
- `VF_CODE_OUTPUT_RATE`
- `VF_CODE_RUNS_DIR`
- `VF_CODE_EVENTS_DIR`
- `VF_CODE_REPORTS_DIR`
- `VF_CODE_PROMPTS_DIR`

When those values are absent, the bridge keeps repo-local defaults. Invalid
numeric or path values fail early with a clear config error.

## Read Next

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`
- `vaultforge_code_codex_api_bridge_spec_v_2.md`

## Boundary

This section should stay focused on the code bridge, related reports/assets,
and neutral event emission.

It should not quietly become the catch-all worker lane for unrelated VaultForge
implementation tasks or the place where XP meaning gets calculated.
