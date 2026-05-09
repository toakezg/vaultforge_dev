# CHANGELOG

## 2026-05-09

- Recorded Workflow B cycle 1 for run `20260509T233547-run-approved-section-local-build-slices-while-an`: root recorded a hard gate on the business fragment-library ownership/registry move, engine verified the contact-sheet renderer remains `#live-required` and committed the live-required gate evidence as `a50bc48`, and business added the delivery package skeleton committed as `d574b8c`. No live generation was recorded.
- Recorded Workflow B cycle 1 for run `20260509T231222-run-approved-section-local-build-slices-while-an`: root recorded a hard gate on moving business fragments into shared engine registries, engine gallery `--dry-run` guard verification passed for commit `cd9a86d`, and business client-ready criteria passed reviewer checks and was committed as `e89fe60`. No live generation was recorded.
- Recorded Workflow B cycle 1 for run `20260509T223050-run-approved-section-local-build-slices-while-an`: business pack `-WhatIf` logging passed reviewer checks and was committed as `2279fcb`, while the engine gallery-index hook was reopened for a safe dry-run guard because `--gallery-index --dry-run` still writes JSON output. No hard gate or live generation was recorded.
- Recorded Workflow B cycle 1 for run `20260509T204905-run-approved-section-local-build-slices`: engine dry-run smoke/manifest work and business native metadata bridge both passed reviewer checks with no hard gates and no live generation.
- Recorded a Workflow B cycle 1 root-recorder blocker for run `20260509T201250-run-approved-section-local-build-slices`: local shell inspection failed before PowerShell started with `windows sandbox: CryptUnprotectData failed: 2148073483`, so the recorder handoff explicitly avoids inferring builder or reviewer results.
- Added engine-local `.env` API-key loading and lane override flags in `vaultforge-engine`, with the default model pinned to `gpt-image-2-2026-04-21`.
- Added engine-native image input/reference support in `vaultforge-engine`: direct `--input-image` / `--reference-image` files and embedded images inside Markdown prompt notes can now be sent with the prompt for reference-driven generation and edits.
- Added Workflow B as a root long-run controller design with `MULTI_AGENT_WORKFLOW_B.md`, `workflow_b_controller.py`, and `run_workflow_b.bat`; it creates locked cycle packets and can optionally launch section-scoped `codex exec` agents.
- Added Workflow B commit policy flags so spawned agents can commit scoped work after review, per cycle, per agent, or never, while avoiding pre-existing dirty files.
- Added `WORKFLOW_REVIEW.md` and Workflow B workflow-change watching so long runs can refresh root workflow docs between cycles, detect changed workflow guidance, and surface updates in later prompts.
- Added `business-if-done.txt` as a watched business-lane direction input for Workflow B business agents.
- Added Workflow B timebox, estimated usage budget, and hard-gate response modes, with controller budget snapshots, stop handoffs, and agent final signal parsing.
- Added Workflow B checkpoint logging so long runs now write `checkpoints.jsonl`, update `workflow-b-live-status.md`, enrich `status.jsonl`, and print elapsed runtime, cycle progress, agent slots, and budget usage at controller checks.
- Added `run_workflow_b_watch.bat`, `--terminal-detail verbose`, and Workflow B failure guides so watched runs stay open after exit and Codex CLI/plugin/sandbox failures get operator-facing explanations.
- Added a Workflow B Ctrl+C cancellation path that stops active Codex children, writes `workflow-b-cancel-handoff.md`, records `cancel_requested`, clears the lock, and returns exit code `130`.
- Wired the external Esape Hatch workflow (`F:\toakezg\workflows\esape-hatch.md`) into Workflow B cancellation handoffs and workflow-change watching.

## 2026-05-03

- Promoted `vaultforge-icon` into a lightweight active icon lane with its own
  section docs and routed `svg-forge` as the first existing subtool.
- Added `MULTI_AGENT_WORKFLOW.md` as a lightweight root guide for simple Codex build runs with coordinator, builder, reviewer, recorder, decision gates, and handoff prompts.
- Linked the multi-agent workflow from `CODEX_START.md` and `THREAD_MAP.md` so future threads know when to read it.

## 2026-04-27

- Added `CURRENT_STATE.md` as a root recovery anchor for cases where the Codex app sidebar, project list, or thread list loses visible VaultForge context.
- Updated root startup, routing, system, plan, and README docs so new threads read the recovery snapshot before routing into a section.
- Refreshed `THREAD_MAP.md` date and read-order guidance so root/section coordination remains recoverable from the repo even when the app UI grouping changes.

## 2026-04-16

- Activated `vaultforge-xp4l` as an XP4Life interpretation/progression section
  in the root coordination docs and thread map.
- Added XP4L-aware routing language to root docs so execution stays with
  `vaultforge-coding` while interpretation lives in `vaultforge-xp4l`.

- Promoted `vaultforge-coding` into the VaultForge Code section and added the
  first local section doc set: `README.md`, `CODEX_START.md`, `SYSTEM.md`,
  `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.
- Updated root coordination docs so `vaultforge-coding` is no longer treated as
  a parked folder and now routes code-bridge work through its own section.
- Tightened the coding-section contract around the v2 bridge spec: the section
  now owns execution, logging, usage tracking, and neutral event emission while
  leaving XP interpretation to a future sibling lane.

- Added a wrapper-owned ICON placeholder pool system under `ICON/` so prompt files can use generic `{name}` placeholders backed by matching pool files such as `weapon_type.md`, with clear missing-pool errors, resolved-value logging, and wrapper-level loop support via `--limit`.
- Rewired `run-icons-part-a.bat` and `run_loop_rewards.bat` to use the new local ICON wrapper instead of handing raw batch folders straight to the external art generator.
- Converted the XP4Life rewards `weapon.md` prompt into a placeholder-driven template and added the first dedicated `ICON\XP4Life\part-a\pools\` files for weapon type, element, theme, and tier values.

- Added the task-property rule across root and promoted section docs: active and next tasks should carry stable `🆔` ids, recurring loops should use `🔁`, and dependency chains should use `⛔` for `before this` and reverse-linked follow-up tasks for `after this`.
- Kept `due`, `scheduled`, `start`, and `created` out of the standard task format for now so section priorities stay clean before date-driven urgency rules are adopted.
- Backfilled stable ids, recurrence markers, and dependency links into the current open root, engine, business, and art task pools where the sequencing or repeat pattern is clear.

## 2026-04-14

- Added the task-query rule: root and promoted section `TASKS.md` files should use automatic `tasks` code blocks above manual active/next lists.

## 2026-04-13

- Added the section-local task priority rule and marked current open root tasks with Obsidian Tasks priority markers.
- Hard-set the task tag rule across root and promoted section docs: every task should include at least one section tag and one task-type tag.
- Added the root/section thread model: root now acts as overhead coordinator while promoted section folders act as focused worker bases.
- Added `THREAD_MAP.md` to route new threads between root, engine, business, and art.
- Added section sign-up expectations and refreshed root docs around dedicated section thread startup.
- Added a root `vaultforge-art` coordination base while leaving the sibling art runtime/reference prototype at `F:\tools\image_generation\vaultforge-art`.
- Filled the placeholder sections in Nath's orchestration note with root, business, art, and thread-routing requirements.

## 2026-04-12

- Refreshed root docs to reflect that `vaultforge-engine\src\generate.py` is now the verified shared engine prototype while XP4Life root wrappers still use the sibling art generator.
- Cleaned up business engine wording after the retarget: `run_business.ps1` now uses `EngineRoot` as the primary parameter name with `ArtRoot` preserved as an alias, and the business docs/helper terminal text now describe the shared engine accurately.
- Renamed the shared engine entrypoint from `vaultforge-engine\src\generate_art.py` to `vaultforge-engine\src\generate.py` and updated engine wrappers, business wrappers, tests, and compatibility docs to use the neutral core name.
- Retargeted `vaultforge-business\run_business.ps1` from the old art-owned generator path to `vaultforge-engine\src\generate.py` with no change to business output routing, prompt composition, preset/style mapping, or metadata writing.
- Added `vaultforge-engine\COMPATIBILITY_BUSINESS.md` with business dry-run parity findings and a recommendation to retarget business directly to `vaultforge-engine\src\generate.py` in a later pass.
- Verified business smoke and multi-variant dry-runs against direct engine equivalents without changing business defaults.
- Added a compatibility bridge: `vaultforge-art\run_art.bat` now delegates to `vaultforge-engine\src\generate.py` while preserving `vaultforge-art` as the effective project root.
- Added `VAULTFORGE_ENGINE_PROJECT_ROOT` support to the copied engine so lane wrappers can preserve their own default input/output paths.
- Added `vaultforge-engine\COMPATIBILITY.md` with parity findings, dry-run commands, results, cleanup note, and remaining blockers before business retargeting.
- Added the first copy-based `vaultforge-engine` prototype with copied generator source, copied/adapted tests, packaging metadata, engine smoke prompt, verification notes, and `run_engine.bat`.
- Verified the copied engine with unit tests, direct dry-run, batch-smoke dry-run, and launcher dry-run.

## 2026-04-11

- Added `ARCHITECTURE - engine extraction.md` to document the staged move from `vaultforge-art` as de facto engine toward a dedicated `vaultforge-engine`.
- Added the first `vaultforge-engine/` documentation skeleton with README, SYSTEM, PLAN, TASKS, and CODEX_START.
- Updated root docs to frame `vaultforge-engine` as the future shared core while preserving current sibling generator behavior.
- Recorded the first successful XP4Life Icons Part A live generation run and copied the generated examples from `_template/` into the workspace output folders.
- Added `NOTE/Icons - part A - output review.md` with generated example embeds and first-pass tuning notes.
- Rewrote `NOTE/How to - Create XP4Life Icon set (obsidian).md` as a transferable Obsidian icon-set workflow and listed the required `iconic` plugin ID.
- Added `NOTE/VaultForge Icons - branch plan.md` to capture the broader client/logo-pack direction from the phone notes.
- Added draft reference notes for client intake, usage stats, pricing, and Facebook ad copy under `Reference/`.
- Added the core workspace docs: `README.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, and `CODEX_START.md`.
- Added XP4Life Icons Part A reference docs under `NOTE/`.
- Added a local XP4Life Icons Part A prompt bank under `ICON/XP4Life/part-a/prompts/`.
- Added `run-icons-part-a.bat` to route this vault's prompt folders into the existing `vaultforge-art` image generator while keeping outputs in this workspace.
- Verified the local launcher in `--dry-run` mode across all four Part A categories.
- Reserved `ICON/XP4Life/part-a/generated/` as the local output destination for this lane.
- Mirrored the operator-facing Part A assets into `_template/` and added `_template/Home.md` as a simple entry point for newly created vaults.
