# CURRENT STATE

Date: 2026-05-03

Use this file as the quick recovery anchor when the Codex app sidebar, project list, or thread list stops showing the expected VaultForge history.

## Why This Exists

VaultForge has enough sections and prior Codex threads that the app UI is no longer a reliable source of truth for coordination by itself. The filesystem, git root, and repo docs are the durable anchors.

If the visible Codex project/thread list looks empty or incomplete, assume UI grouping or filtering first. Do not assume the repo or prior work is gone.

## Verified Local Anchors

- Workspace root: `F:\vaultforge`
- Git root: `F:\vaultforge`
- Current branch during this refresh: `master`
- Active section in this cleanup pass: `vaultforge-icon` lane promotion
- Current engine folder: `F:\vaultforge\vaultforge-engine`
- Codex session storage exists separately under `C:\Users\nvn4_\.codex\sessions`
- Codex memory records exist for prior `vaultforge-engine` threads

## First Read Order For Any New VaultForge Thread

1. `CODEX_START.md`
2. `CURRENT_STATE.md`
3. `THREAD_MAP.md`
4. `PLAN.md`
5. `TASKS.md`
6. The target section's `CODEX_START.md`
7. The target section's `PLAN.md`
8. The target section's `TASKS.md`
9. The target section's `SIGN_UP.md`
10. The target section's `CHANGELOG.md`

## Current Routing Snapshot

- Root owns coordination, cross-lane planning, section promotion, and thread routing.
- `vaultforge-engine` owns shared generator behavior, CLI/config contracts, dry-run behavior, metadata, compatibility, and tests.
- `vaultforge-business` owns client/business workflows, prompt banks, wrappers, output routing, galleries, and review surfaces.
- `vaultforge-art` is the planned fresh art lane under `F:\vaultforge\vaultforge-art`; the old runtime/reference prototype is being harvested from `F:\tools\image_generation\vaultforge-art`.
- `vaultforge-icon` owns icon workflow coordination, icon notes, icon asset review, and the existing `svg-forge` raster-to-SVG subtool.
- `vaultforge-coding` owns the local-first code bridge and factual run/event reporting.
- `vaultforge-xp4l` owns interpretation, XP/progression, quests, achievements, and dashboard-ready outputs.
- `vaultforge-core`, `vaultforge-design`, `vaultforge-system`, and `vaultforge-init` are still supporting or parked areas unless root promotes them.

## Current Engine Snapshot

- Shared engine entrypoint: `vaultforge-engine\src\generate.py`
- Engine launcher: `vaultforge-engine\run_engine.bat`
- Engine contract already includes native `--client`, `--job`, `--tag`, and `--variants`.
- Business targets the shared engine directly while preserving business output routing.
- Open engine work is still around config-safe dry-runs, shared manifest contract review, and edit/reference image contract definition.

## Known UI Risk

Codex app sidebar/project grouping may become confusing after root-level git changes or when a section folder is opened inside a larger repo. Treat the sidebar as a convenience, not the coordination record.

Recovery rule:

- If a thread disappears from view, reopen from `F:\vaultforge`, read this file, then route through `THREAD_MAP.md`.
- If a section-specific thread is needed, open the section folder only after checking root routing.
- If prior chat detail is needed, ask Codex to search memory for the relevant section and task keywords.

## Dashboard Idea For Later

A separate dashboard is plausible later, especially if Codex UI visibility keeps drifting. The lightest useful version would be a repo-local Markdown or small static HTML dashboard that reads:

- `CURRENT_STATE.md`
- `THREAD_MAP.md`
- root and section `TASKS.md`
- root and section `CHANGELOG.md`
- section `SIGN_UP.md`

Do not build that yet unless it becomes its own explicit task. For now, keep this recovery file and the existing docs spine current.
