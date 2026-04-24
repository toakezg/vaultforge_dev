# Plan

## Section Thread Model

- VaultForge Code is a promoted worker section under root coordination.
- section threads should read root startup docs before local section docs.
- this section should stay focused on the code bridge rather than becoming the
  general worker lane for unrelated coding tasks.

## Current Direction

- promote `vaultforge-coding\` as the home of the VaultForge Code bridge
- keep the MVP local-first, Windows-friendly, and safe by default
- build the bridge around the Responses API using the official OpenAI Python SDK
- keep run artifacts, usage logs, summaries, and event outputs local to the
  section
- keep direct file overwrites and patch application out of MVP until approval
  flow is designed
- keep this section on the work/execution side and leave XP interpretation to a
  future sibling `vaultforge-xp4l` section

## Phase 0 - Core Skeleton

- create the section doc set
- lock the naming and boundary rules
- scaffold the Python project layout under `src\vf_code_bridge`
- add `.env.example`, launcher batch files, `VERIFICATION.md`, and local asset
  folders for runs, reports, prompts, and events
- build config loading, CLI entry, usage tracking, run-manifest writing, and
  event writing

## Phase 1 - Bridge MVP

- load preset prompt templates by mode
- accept a task plus optional extra context note
- build project context from a chosen project root with include/exclude guards
- compile the final instruction package cleanly
- call the OpenAI Responses API
- save prompt, response text, response JSON, usage JSON, summary markdown,
  context manifest, and per-run `event.json`
- print a clean terminal summary for each run

## Phase 2 - Reports, Tests, And Safer Growth

- maintain append-only `usage_log.jsonl` and `run_log.jsonl`
- build `usage_summary.md`
- add tests for config loading, context building, usage tracking, and event
  writing
- keep the CLI smoke-testable from batch usage
- add optional patch writer, diff generation, approval mode before write,
  batch/queue mode, and richer downstream event shaping later

## Out Of Scope For This Section

- XP formulas
- quest generation
- achievement unlocking
- reward generation
- XP4Life dashboard injection

## Watchpoints

- the bridge can sprawl into a general automation layer if boundaries stay weak
- direct write behavior is risky before approval flow exists
- context collection can get expensive if caps are not enforced
- the section name and folder name can drift if the naming note is ignored
- cross-section integrations should not be implied before the bridge MVP is real
- event emission can get muddy if the section starts writing interpretation
  instead of factual run records

## Forward Look

- finish the bridge MVP before expanding into approval-mode writes
- treat future integrations with business, art, or a future `vaultforge-xp4l`
  section as explicit follow-on tasks
- keep the section useful from terminal and batch usage before chasing richer
  automation surfaces
