# CHANGELOG

## 2026-05-13

- Recovered the stalled executable Workflow B interface run
  `20260513T032920-make-the-vaultforge-operator-interface-executabl`: the
  interface builder completed and launched the local app, but the controller
  stayed pinned behind the persistent builder child process. Stopped only that
  run's stale process chain, kept the interface server live on
  `http://127.0.0.1:4173/`, removed the tracked runtime lock, ignored future
  `.workflow-b.lock` files, and added controller per-agent timeout handling
  tied to the remaining timebox.
- Recorded Workflow B cycle 1 for run `20260513T023458-continue-the-approved-vaultforge-operator-interf`: root coordinator routed the approved interface-local preview/gallery and run-planning slice, the interface builder added draft-only run-planning controls, prompt and command draft ergonomics, and dynamic gallery/evidence cards, and the interface reviewer fixed the Edge smoke harness and committed the reviewed interface scope as `a40cd4f`. Reviewer verification passed `npm.cmd test` and `git diff --check -- interface`. No hard gate, real command execution, `--execute` command draft, engine/business/icon/XP4L/art/coding change, secret use, paid/API behavior, live generation, or cross-lane ownership change was recorded.
- Added Workflow B `interface` lane routing for the root-local operator UI work
  area, with scoped builder/reviewer write rules and thread-map documentation.
- Ran the approved 5-cycle, 18-minute Workflow B interface build from
  `Reference/build_draft.jpg`; the controller stopped at the timebox after the
  builder, then a local review tail refined and verified the first static
  operator interface under `interface/`.

## 2026-05-11

- Fixed root workflow hygiene for the controlled client-style pilot/demo run:
  repaired the invalid ignore glob that broke `rg`, added a local
  `.gitmodules` mapping for the nested `vaultforge-xp4l` lane so submodule
  status no longer errors, removed tracked Python bytecode artifacts from the
  trusted workflow surface, and verified the pilot path stops before HG-004
  live paid/API generation.
- Recorded the approved live pilot/demo pass: `ENGINE_KEY` was verified for
  Responses write access, the business lane generated two private review-only
  variants for the scoped prompt note, and local review surfaces were built.
- Recorded the approved rating-improvement rerun: two additional pilot-demo
  prompt notes generated four private review-only variants, refreshed the
  review surfaces, and moved the best reviewed result from rating 6 to rating 8.

## 2026-05-10

- Recorded Workflow B cycle 1 for run `20260510T130343-hard-gate-doc-updated-with-0-or-1-approvals-b`: `HARD_GATES.md` carried explicit 0/1 approvals, root coordinator routed the approved registry slice to engine/business, engine added business-facing preset/style aliases plus separate production constraints committed as `c0e2d37`, business adopted the accepted aliases/constraints in `run_business.ps1` and docs committed as `4e59f85`, icon correctly no-oped with clean lane verification, and XP4L recorded a scope-only hard-gate note committed in the XP4L repo as `ea89b37`. Reviewer checks passed for engine tests/dry-runs, business parser/WhatIf/DryRun previews, icon no-op scope, and XP4L tests. No live generation, paid/API call, generated art, contact-sheet renderer implementation, public launch, pricing/licensing commitment, asset move/delete, folder-icon apply work, XP scoring/progression change, event-source expansion, root controller edit, or unapproved cross-lane ownership expansion was recorded.
- Added the repo-local `vaultforge-operator` Codex plugin scaffold under `plugins/vaultforge-operator`, registered it in `.agents/plugins/marketplace.json`, and included a read-only snapshot helper for root docs, section docs, task hygiene, hard gates, and recent Workflow B visibility.
- Recorded Workflow B cycle 1 for run `20260510T061633-prepare-nath-facing-business-decision-notes-only`: root coordinator routed the note-only paid launch decision slice to `vaultforge-business`, business added `BUSINESS_PAID_LAUNCH_DECISION_NOTE.md` and linked it from `README.md` and `NATH_START.md`, reviewer found no blocking issues, verified docs-only scope with `git diff --check`, gated-language checks, trailing-whitespace checks, and no generated/log output changes, and the reviewed business section commit is `15aa39f`. No hard gate was hit during note preparation, and no live generation, paid/API call, public launch, pricing/licensing commitment, publication, asset move/delete, engine registry change, or cross-lane ownership change was recorded. Nath still needs to choose `0` or `1` in the decision note before any pilot generation or paid-service launch work.
- Recorded Workflow B cycle 2 for run `20260510T055419-run-approved-build-slices-while-analyzing-workfl`: the controller detected changed `MULTI_AGENT_WORKFLOW_B.md` and `WORKFLOW_REVIEW.md`, refreshed cycle prompts, root coordinator safe-switched the generated engine slot to evidence-only verification because `engine-contact-sheet-renderer` remains `#live-required`, engine builder and reviewer kept renderer work parked, reviewer verification passed `py -B -m unittest discover -s tests` with 24 tests OK plus smoke dry-run and gallery-index guard checks, and the reviewed engine section commit is `31d14dd`. No hard gate, live generation, generated art, renderer implementation, fixture-policy decision, sidecar contract expansion, paid/API work, root Workflow B controller edit, destructive file operation, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 1 for run `20260510T055419-run-approved-build-slices-while-analyzing-workfl`: root coordinator safe-switched the generated engine slot to evidence-only verification because `engine-contact-sheet-renderer` remains `#live-required`, engine builder and reviewer kept renderer work parked, reviewer verification passed `py -B -m unittest discover -s tests` with 24 tests OK plus smoke dry-run and gallery-index guard checks, and the reviewed engine section commit is `a667192`. No hard gate, live generation, generated art, renderer implementation, fixture-policy decision, paid/API work, root Workflow B controller edit, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 1 for run `20260510T015750-use-multiagents-to-perform-a-clean-up-of-documen`: root coordinator routed the safe cleanup/orientation slice to `vaultforge-business`, business added the operator-facing `NATH_START.md` and related discoverability fixes, reviewer verification passed parser checks for all business PowerShell scripts, direct and markdown-bank `-WhatIf` previews, pack-preview `-WhatIf` with execution-policy bypass, smoke dry-run, and `git diff --check` with only LF-to-CRLF warnings, and the reviewed business section commit is `da7301f`. No hard gate, live generation, paid/API work, pricing/licensing/publication change, asset move/delete, root contract change, or engine registry change was recorded.
- Recorded Workflow B cycle 2 for run `20260510T005905-run-approved-section-local-build-slices-while-an`: the controller detected the changed `WORKFLOW_REVIEW.md`, refreshed cycle prompts, routed the safe work to `vaultforge-xp4l`, XP4L added the section-local `HEURISTIC_BOUNDARIES.md`, reviewer verification passed `python -m unittest discover -s tests -v` with 21 tests OK, and the reviewed XP4L section commit is `4cb82fc`. No hard gate, runtime behavior change, live vault write, scoring value/config change, event-contract/source change, parser behavior change, fixture/test change, persistent progression design change, paid/API work, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 2 for run `20260510T005900-run-approved-section-local-build-slices-while-an`: the controller detected the changed `WORKFLOW_REVIEW.md`, refreshed cycle prompts, root coordinator safe-switched the generated engine slot to verification/evidence only because no approved engine implementation slice remained, engine builder and reviewer kept `engine-contact-sheet-renderer` parked as `#live-required`, and reviewer verification passed `py -B -m unittest discover -s tests` with 24 tests OK plus smoke dry-run and gallery-index guard checks. No commit was made because the engine docs were already dirty with mixed pre-existing Workflow B entries. No hard gate, live generation, generated art, renderer implementation, fixture-policy decision, paid/API work, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 1 for run `20260510T005905-run-approved-section-local-build-slices-while-an`: root coordinator routed the safe work to `vaultforge-xp4l`, XP4L added the section-local `XP_RULES_SURFACE.md`, reviewer verification passed `python -m unittest discover -s tests -v` with 21 tests OK, and the reviewed XP4L section commit is `cdb65e6`. No hard gate, runtime behavior change, live vault write, scoring value/config change, event-contract/source change, parser behavior change, fixture/test change, persistent progression design change, paid/API work, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 1 for run `20260510T005903-run-approved-section-local-build-slices-while-an`: root coordinator routed the safe work to `vaultforge-icon` as verification/evidence only after the media-style proposal decision, icon builder and reviewer confirmed the media style guide remains inactive/reference-only, no `run_icon_proposal.ps1`/paid/API generation ran, no media proposal output directory exists, and no new icon-lane commit was made because the lane was already clean. No hard gate, generated output, selected/applied output, asset operation, folder-icon application, live generation, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 1 for run `20260510T005900-run-approved-section-local-build-slices-while-an`: root coordinator routed the safe work to `vaultforge-engine` as verification/evidence only, engine confirmed the contact-sheet renderer remains `#live-required`, reviewer verification passed `py -B -m unittest discover -s tests` with 24 tests OK plus smoke dry-run and gallery-index guard checks, and the reviewed engine section commit is `d400135`. No hard gate, live generation, generated art, renderer implementation, fixture-policy decision, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 1 for run `20260510T004645-run-approved-section-local-build-slices-while-an`: root coordinator routed the safe work to `vaultforge-xp4l`, XP4L added the section-local `OUTPUT_CONTRACT.md`, reviewer verification passed `python -m unittest discover -s tests -v` with 21 tests OK, and the reviewed XP4L section commit is `9c0dfa2`. No hard gate, runtime behavior change, live vault write, scoring change, event-contract change, persistent progression design change, paid/API work, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 1 for run `20260510T004631-run-approved-section-local-build-slices-while-an`: root coordinator routed the safe work to `vaultforge-engine` as verification/evidence only, engine confirmed the contact-sheet renderer remains `#live-required`, reviewer verification passed `py -B -m unittest discover -s tests` with 24 tests OK plus smoke dry-run and gallery-index guard checks, and the reviewed engine section commit is `a7e92e3`. No hard gate, live generation, generated art, renderer implementation, fixture-policy decision, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 2 for run `20260510T001258-run-approved-section-local-build-slices-while-an`: the controller detected the changed `WORKFLOW_REVIEW.md`, refreshed cycle prompts, routed the safe work to `vaultforge-xp4l`, XP4L added verification criteria documentation, reviewer verification passed `python -m unittest discover -s tests -v` with 21 tests OK, and the reviewed XP4L section commit is `ef5c6a6`. No hard gate, live vault write, scoring change, event-contract change, or cross-lane ownership change was recorded.
- Recorded Workflow B cycle 1 for run `20260510T001258-run-approved-section-local-build-slices-while-an`: the controller routed this executable review-mode cycle to `vaultforge-xp4l`, root coordinator confirmed no hard gate, XP4L documented engine boundaries, reviewer verification passed `python -m unittest discover -s tests -v` with 21 tests OK, and the reviewed XP4L section commit is `e0b76bf`. No live vault write or cross-lane ownership change was recorded.

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
