# VaultForge Workflow B Agent Prompt

Run id: 20260509T213834-verify-budget-and-gate-flags-in-dry-run
Cycle: 1 of 2
Agent: root-coordinator
Role: coordinator
Lane: root
Working directory: F:\vaultforge
Write scope: root coordination docs and the active Workflow B run packet
Commit mode: review
Hard gate mode: switch-safe
Timebox minutes: 120.0
Usage budget USD: 3.0
Estimated agent USD: 0.08
Run packet: F:\vaultforge\runs\workflow-b-verify\20260509T213834-verify-budget-and-gate-flags-in-dry-run

## Main Run Brief

Verify budget and gate flags in dry run

## Assigned Tasks

- Verify budget and gate flags in dry run

## Required Operating Rules

- Follow `MULTI_AGENT_WORKFLOW.md` as Workflow A inside this cycle.
- Stay inside the named lane and write scope.
- Read the root/section docs included below before editing.
- Use `THREAD_MAP.md` for ownership and routing.
- Stop at hard gates from Workflow A and record a decision note.
- Soft gates should become tasks or handoff notes if another approved safe slice remains.
- Do not move, delete, or rewrite unrelated files.
- Keep evidence: files touched, verification run, blockers, and next prompt.
- If this role is reviewer, lead with findings and file/line references where possible.
- If this role is recorder, update only the relevant handoff/changelog/task notes.
- Respect the hard-gate mode:
  - `stop`: stop at a hard gate and leave a decision note.
  - `switch-safe`: stop the blocked slice, record the gate, then continue only with another approved safe slice if one exists.
  - `record-continue`: record the gate and continue only when the gate does not block the current safe work.
- Respect time and usage budgets. Prefer smaller safe slices as budget gets low.

## Required Final Signal

End your final answer with these exact lines so the controller can keep strict records:

```text
WORKFLOW_B_HARD_GATE: yes|no
WORKFLOW_B_SAFE_WORK_REMAINS: yes|no
WORKFLOW_B_USAGE_USD: 0.00
WORKFLOW_B_NEXT_ACTION: short next action
```

## Workflow Update Check

No workflow document changes were detected before this cycle.

## Commit Policy

- Do not commit from this role. Leave scoped changes for the reviewer after verification.
- Before editing, run `git status --short` and treat that as the dirty baseline.
- Never stage or commit pre-existing unrelated dirty files.
- Only stage files you changed for this agent role and write scope.
- If unsure whether a file is yours, leave it unstaged and record the question.

## Root Docs Snapshot

## CODEX_START.md

# CODEX START

You are working inside the VaultForge workspace.

Before starting substantial work:

1. Read `README.md`.
2. Read `SYSTEM.md`.
3. Read `CURRENT_STATE.md`.
4. Read `THREAD_MAP.md`.
5. Read `PLAN.md`.
6. Read `TASKS.md`.
7. Read `CHANGELOG.md`.
8. If the task uses a multi-agent/simple-build workflow, also read
   `MULTI_AGENT_WORKFLOW.md`.
9. If you are entering a section thread, also read that section's:
   - `CODEX_START.md`
   - `SYSTEM.md`
   - `PLAN.md`
   - `TASKS.md`
   - `CHANGELOG.md`
   - `SIGN_UP.md`
10. If the task touches engine extraction, also read:
   - `ARCHITECTURE - engine extraction.md`
   - `vaultforge-engine/README.md`
   - `vaultforge-engine/SYSTEM.md`
   - `vaultforge-engine/PLAN.md`
   - `vaultforge-engine/TASKS.md`
11. If the task touches XP4Life icons, also read:
   - `vaultforge-icon/CODEX_START.md`
   - `vaultforge-icon/SYSTEM.md`
   - `vaultforge-icon/PLAN.md`
   - `vaultforge-icon/TASKS.md`
   - `vaultforge-icon/CHANGELOG.md`
   - `vaultforge-icon/SIGN_UP.md`
   - `vaultforge-icon/NOTE/Icons - part A.md`
   - `vaultforge-icon/NOTE/Icons - part A - todo.md`
   - `vaultforge-icon/NOTE/Icons - part A - quick use guide.md`
12. Summarize your understanding before making large changes.

Default assumption:

- This repo should stay lightweight and note-driven.
- Root is the overhead coordinator; promoted section folders are worker bases.
- If the Codex app sidebar or thread list looks empty or incomplete, use `CURRENT_STATE.md` and `THREAD_MAP.md` as the recovery anchors.
- Use `THREAD_MAP.md` to decide where a task belongs before making cross-section edits.
- Shared image generation logic now has a verified prototype in `vaultforge-engine`.
- Some root/icon wrappers may still call the old art runtime/reference prototype at `F:\tools\image_generation\vaultforge-art` until they are explicitly retargeted.
- `vaultforge-icon` is the active icon lane; route icon notes, asset review, and SVG-Forge validation there.
- Vault-side wrappers and prompt banks belong here when they improve speed and reuse.

## README.md

# VaultForge

VaultForge is the vault-side control layer for reusable Obsidian workflows.

It now uses a root/section thread model:

- root `vaultforge\` = overhead coordination, architecture, and handoffs
- `vaultforge-engine\` = shared generation machinery and contracts
- `vaultforge-business\` = client/business workflow lane
- `vaultforge-coding\` = local-first code bridge and API-driven coding lane
- `vaultforge-xp4l\` = XP4Life interpretation and progression lane
- `vaultforge-art\` = planned fresh art lane, with the old runtime/reference prototype being harvested from `F:\tools\image_generation\vaultforge-art`
- `vaultforge-icon\` = lightweight icon workflow lane, including SVG-Forge

This workspace currently does seven useful things:

- keeps vault creation and launcher scripts in one place
- stores reusable notes and planning docs for future Codex threads
- hosts local pipeline wrappers that can hand work off to sibling tools such as the old art runtime/reference prototype at `F:\tools\image_generation\vaultforge-art`
- hosts the first shared generation prototype under `vaultforge-engine`
- carries the first dedicated code-automation bridge section under
  `vaultforge-coding`
- carries the first dedicated XP4Life interpretation section under
  `vaultforge-xp4l`
- carries the first lightweight icon lane under `vaultforge-icon`

## Engine Direction

VaultForge is moving toward a cleaner split:

- `vaultforge-engine` = stable shared generation core
- `vaultforge-art` = art-facing and experimental lane
- `vaultforge-business` = business and client-facing lane

The first shared engine prototype now lives at `vaultforge-engine\src\generate.py`.
`vaultforge-business` targets that shared engine directly. Some older/root
wrappers, including the XP4Life icon launcher, still call the sibling
`F:\tools\image_generation\vaultforge-art` generator until they get their own
explicit compatibility pass. See `ARCHITECTURE - engine extraction.md`.

## Key Docs

- `SYSTEM.md` explains how this workspace is meant to operate
- `CURRENT_STATE.md` is the quick recovery anchor when Codex app project/thread visibility gets confusing
- `PLAN.md` tracks the current direction
- `TASKS.md` holds the active work pool
- `THREAD_MAP.md` tells new threads which section should own a task
- `CHANGELOG.md` records notable structural changes
- `CODEX_START.md` gives new Codex threads a clean boot sequence

## XP4Life Icons Part A

The first implemented design lane is an XP4Life icon pipeline.

- reference note: `vaultforge-icon/NOTE/Icons - part A.md`
- attack plan: `vaultforge-icon/NOTE/Icons - part A - todo.md`
- quick guide: `vaultforge-icon/NOTE/Icons - part A - quick use guide.md`
- Obsidian use guide: `vaultforge-icon/NOTE/How to - Create XP4Life Icon set (obsidian).md`
- first output review: `vaultforge-icon/NOTE/Icons - part A - output review.md`
- prompt bank: `ICON/XP4Life/part-a/prompts/`
- launcher: `run-icons-part-a.bat`

The image engine is not duplicated in the XP4Life lane. This root launcher still
delegates to the existing Python generator in
`F:\tools\image_generation\vaultforge-art`.

## Quick Start

Dry-run the full prompt bank:

```bat
run-icons-part-a.bat --dry-run
```

Run only quests:

```bat
run-icons-part-a.bat quests
```

Generated files land in:

```text
ICON\XP4Life\part-a\generated\
```

## VaultForge Icons Branch

The broader client/logo-pack idea is captured in:

```text
vaultforge-icon\NOTE\VaultForge Icons - branch plan.md
```

Supporting draft references live in `Reference/`.

## Section Threading

New dedicated threads should start at root, use `THREAD_MAP.md` to choose the correct section, then read that section's `CODEX_START.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.

Section threads should update their own changelog first. Root `CHANGELOG.md` is for cross-lane or coordination-level changes.

## SYSTEM.md

# SYSTEM

## Purpose

This workspace is the VaultForge vault factory and workflow hub.

It exists to keep reusable vault assets, launchers, notes, and pipeline helpers together so new work can start from a clean and documented base.

Root also acts as the overhead coordinator for dedicated section threads.

## Operating Principles

- Keep the vault-side layer lightweight and note-friendly.
- Prefer thin wrappers over duplicated engines.
- Store prompt notes and planning notes in plain Markdown.
- Keep outputs local to the vault when that improves review and reuse.
- Treat sibling projects as dependencies when they already solve the heavy part of the workflow.
- Avoid baking domain-specific assumptions into every workflow unless they are clearly useful.
- Use root for coordination and section folders for focused worker tasks.
- Keep cross-section handoffs visible in `THREAD_MAP.md`, section changelogs, and root `CHANGELOG.md` when needed.

## Integration Rules

- Vault creation behavior lives in the root `.bat` launchers and `_template/`.
- Documentation and planning live in root Markdown notes.
- `THREAD_MAP.md` decides which section should own a task.
- Reusable prompt banks and output folders live under purpose-named folders such as `ICON/`.
- Shared reusable generation code now lives in `vaultforge-engine`.
- Some older/root wrappers may still delegate to the old art runtime/reference prototype at `F:\tools\image_generation\vaultforge-art` until each lane gets an explicit compatibility pass.
- Treat `vaultforge-art` as the art/playground lane, not the permanent shared engine.
- If a wrapper depends on another local project, the dependency path must be explicit and documented.

## Documentation Rules

- `PLAN.md` tracks direction, intent, tradeoffs, and watchpoints.
- `TASKS.md` tracks the actionable work pool.
- `CURRENT_STATE.md` records the current recovery snapshot for app UI/thread-list drift.
- `THREAD_MAP.md` maps thread roles, section ownership, and handoff rules.
- `CHANGELOG.md` records notable structural changes with newest entries first.
- `NOTE/` holds topic notes, implementation notes, and quick guides.
- `ICON/` holds icon-related prompt banks, generated outputs, and local assets.
- `CODEX_START.md` is the preferred boot note for new Codex threads.
- Promoted sections should keep their own `CODEX_START.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.
- Every Markdown task line must include at least one section tag and one task-type tag, for example `#engine #docs`, `#business #gallery`, `#coding #api`, `#xp4l #planning`, `#art #architecture`, or `#root #threading`.
- Active and next tasks should use Obsidian Tasks priority markers by section-local importance: 🔺 highest, ⏫ high, 🔼 medium, 🔽 low, ⏬ lowest. Leave no marker only for unranked inbox or backlog tasks.
- Active and next tasks should also carry a short stable `🆔` id so `before this` and `after this` links stay usable across sections.
- Use `🔁` only for true recurring work. Prefer `when done` for recurring maintenance or review loops.
- Use `⛔ task-id` for `before this` dependencies, and express `after this` by linking the follow-up task back to the current task's `🆔`.
- Hold `due`, `scheduled`, `start`, and `created` for a later rules pass.
- Each promoted section `TASKS.md` should include a `tasks` code block above manual active/next sections, filtered by that section tag, so open work self-populates without manual copying.

## Root And Section Model

- Root is the coordinator and architect.
- `vaultforge-engine` is the shared generator contract section.
- `vaultforge-business` is the client/business workflow section.
- `vaultforge-coding` is the local-first coding bridge section.
- `vaultforge-xp4l` is the XP4Life interpretation and progression section.
- `vaultforge-art` is the art/playground coordination section; its runtime worktree is still a sibling dependency until an explicit migration task changes that.
- `vaultforge-icon` is the icon workflow section; it owns icon notes, icon review, and the existing `svg-forge` subtool.
- Parked folders such as `vaultforge-core`, `vaultforge-design`, `vaultforge-system`, and `vaultforge-init` are not active thread bases until root promotes them.

## Current Design Decision

XP4Life Icons Part A is implemented here as a vault-local prompt bank plus a launcher batch file.

That launcher currently calls the existing sibling `vaultforge-art` Python generator with:

- prompt folders from this vault
- output folders in this vault
- the existing `icon` preset and compatible style flags from the art project

That keeps the workflow local and reusable without forking the image engine. Future wrapper changes should move toward `vaultforge-engine` only through explicit dry-run compatibility passes.

## CURRENT_STATE.md

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

## THREAD_MAP.md

# VaultForge Thread Map

Date: 2026-05-03

VaultForge now uses a root/section thread model.

Root is overhead coordination. Section folders are focused worker bases.

If the Codex app sidebar, project list, or thread list loses visible history, do not treat that as evidence that the project is empty. Reopen from `F:\vaultforge`, read `CURRENT_STATE.md`, then use this file to route the next thread.

## Root Thread

Use root for:

- cross-lane planning
- architecture decisions
- section promotion or parking
- thread routing
- multi-agent/simple-build workflow coordination
- handoffs between engine, business, art, coding, and xp4l
- high-level changelog updates

Read first:

- `CODEX_START.md`
- `README.md`
- `SYSTEM.md`
- `CURRENT_STATE.md`
- `MULTI_AGENT_WORKFLOW.md` when a run uses agent roles or decision gates
- `PLAN.md`
- `TASKS.md`
- `THREAD_MAP.md`
- `CHANGELOG.md`

Report changes to:

- `CHANGELOG.md`
- affected section changelogs when root changes a section contract

## Engine Thread

Use `vaultforge-engine` for:

- shared generator behavior
- CLI flags and config behavior
- presets/styles/mods that are shared
- output contracts
- metadata behavior
- dry-run behavior
- wrapper compatibility
- tests

Read first:

- `..\CODEX_START.md`
- `..\SYSTEM.md`
- `..\CURRENT_STATE.md`
- `..\THREAD_MAP.md`
- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

Report changes to:

- `vaultforge-engine\CHANGELOG.md`
- root `CHANGELOG.md` when the change affects multiple sections
- affected business or art notes when wrappers need updates

## Business Thread

Use `vaultforge-business` for:

- client packs
- prompt banks
- business wrappers
- markdown-bank runners
- gallery and review tooling
- Dataview and Obsidian operator surfaces
- business output routing

Read first:

- `..\CODEX_START.md`
- `..\SYSTEM.md`
- `..\CURRENT_STATE.md`
- `..\THREAD_MAP.md`
- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

Report changes to:

- `vaultforge-business\CHANGELOG.md`
- root `CHANGELOG.md` when the change affects coordination or engine contracts
- engine tasks when business needs shared engine features

## Code Thread

Use `vaultforge-coding` for:

- local-first code bridge implementation
- Responses API calling for coding tasks
- preset prompts such as `review`, `implement`, `tighten`, `audit`, and
  `scaffold`
- local project-context building
- usage and cost tracking for coding runs
- structured activity events for downstream sections
- batch, terminal, and Obsidian-facing bridge entry points

Current status:

- the folder path remains `vaultforge-coding\`
- the section and bridge identity are `VaultForge Code` / `vaultforge-code`
- this section should report what happened, not what it means for XP or
  rewards

Read first:

- `..\CODEX_START.md`
- `..\SYSTEM.md`
- `..\CURRENT_STATE.md`
- `..\THREAD_MAP.md`
- `README.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`
- `vaultforge_code_codex_api_bridge_spec_v_2.md`

Report changes to:

- `vaultforge-coding\CHANGELOG.md`
- root `CHANGELOG.md` when the change affects coordination or shared contracts
- affected section notes when a later code bridge integration changes their
  workflow

## XP4L Thread

Use `vaultforge-xp4l` for:

- event interpretation
- XP calculation
- quest generation
- achievement detection
- reward assignment
- rarity, prestige, and contribution heuristics
- XP4Life vault injection targets
- dashboard-ready progression outputs

Current status:

- `vaultforge-xp4l\` is now an active section with a docs-first pack
- this section should interpret what upstream activity means, not execute tasks
- command or runner details should be chosen during implementation, not frozen in
  the pack

Read first:

- `..\CODEX_START.md`
- `..\SYSTEM.md`
- `..\CURRENT_STATE.md`
- `..\THREAD_MAP.md`
- `README.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`
- `vaultforge_xp_4_l_codex_spec_v_1.md`

Report changes to:

- `vaultforge-xp4l\CHANGELOG.md`
- root `CHANGELOG.md` when the change affects coordination or shared contracts
- affected section notes when upstream event contracts or downstream XP4L
  expectations change

## Art Thread

Use `vaultforge-art` for:

- playground and creative prompt packs
- art presets, styles, and modifiers
- visual experiments
- art output curation
- art bridge checks against `vaultforge-engine`

Current status:

- `vaultforge-art\` under this root is a coordination base.
- The old runtime/reference art worktree is `F:\tools\image_generation\vaultforge-art`; the planned fresh art lane is `F:\vaultforge\vaultforge-art`.
- Do not migrate or rewrite the sibling art worktree without an explicit art migration task.

Read first:

- `..\CODEX_START.md`
- `..\SYSTEM.md`
- `..\CURRENT_STATE.md`
- `..\THREAD_MAP.md`
- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

Report changes to:

- `vaultforge-art\CHANGELOG.md`
- root `CHANGELOG.md` when the change affects coordination or engine contracts
- engine tasks when art needs shared behavior moved into the engine

## Icon Thread

Use `vaultforge-icon` for:

- icon workflow coordination
- XP4Life icon notes and follow-up planning
- VaultForge Icons branch notes before they become business/client work
- icon asset review and local icon pack handoffs
- SVG-Forge validation and small improvements

Current status:

- `vaultforge-icon\` is an active lightweight section.
- `vaultforge-icon\svg-forge\` is the first existing subtool in the lane.
- Do not rewrite SVG-Forge, move/delete icon assets, or run live generation
  without an explicit icon-lane task and Nath approval when a gate applies.

Read first:

- `..\CODEX_START.md`
- `..\SYSTEM.md`
- `..\CURRENT_STATE.md`
- `..\THREAD_MAP.md`
- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`
- `svg-forge\README.md` and `svg-forge\CHANGELOG.md` when touching SVG-Forge

Report changes to:

- `vaultforge-icon\CHANGELOG.md`
- root `CHANGELOG.md` when the change affects coordination or routing
- engine, art, or business tasks only when icon work needs shared behavior,
  art experiments, or client packaging

## Parked Or Supporting Folders

These folders exist in root but are not promoted thread bases yet:

- `vaultforge-core`
- `vaultforge-design`
- `vaultforge-system`
- `vaultforge-init`

Use root to promote one of these into an active section. Promotion means adding the required section docs and updating this thread map.

## Task Tag Rule

Every task in root or a promoted section must include:

- a section tag such as `#root`, `#engine`, `#business`, `#coding`, `#xp4l`, or `#art`
- a task-type tag such as `#docs`, `#threading`, `#planning`, `#architecture`, `#tests`, `#gallery`, `#api`, or `#validation`

This applies to active, next, later, and landed task lines so combined task views can be filtered cleanly.

## Task Query Rule

Each promoted section `TASKS.md` should include an automatic Tasks query above its manual active/next sections.

Use the section tag as the filter:

```tasks
not done
tag includes engine
```

Swap `engine` for the local section tag, such as `business`, `coding`,
`xp4l`, `art`, or `root`.

Root `TASKS.md` may also keep a system-wide `not done` query so overhead can see all open work across sections.

## Task Priority Rule

Priority is section-local first. A section task's priority answers: how important is this for this section right now?

Root can later compare section priorities across VaultForge, but section threads should not flatten everything into root-level priority unless they are doing root coordination.

| Priority | Tasks Marker | Section Meaning | Use When |
|---|---|---|---|
| No priority | none | Captured but not ranked yet | Inbox, backlog, unclear value, or needs review before ranking |
| Lowest | ⏬ | Nice-to-have | Cleanup, polish, future convenience |
| Low | 🔽 | 

[truncated for prompt packet]
## PLAN.md

# PLAN

## Role

This note keeps the active direction, implementation decisions, and watchpoints for the VaultForge workspace.

`TASKS.md` holds the actionable work pool.

## Current Direction

Date: 2026-04-27

- Keep this repo focused on reusable vault structure, launcher helpers, and note-first workflow setup.
- Run VaultForge through a root/section thread model: root coordinates, sections execute focused work.
- Keep `CURRENT_STATE.md` as the app-UI-independent recovery anchor when Codex project or thread visibility drifts.
- Use `THREAD_MAP.md` before cross-section edits so dedicated threads know where to operate.
- Promote active worker bases with section docs: `CODEX_START.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.
- Use sibling tools when they already do the heavy lifting well.
- Continue the engine split now that `vaultforge-engine\src\generate.py` exists as the shared core prototype.
- Treat `vaultforge-art` as the art/playground lane and `vaultforge-business` as the client lane.
- Promote `vaultforge-coding` as the local-first VaultForge Code bridge
  section around the Codex/OpenAI API bridge spec.
- Activate `vaultforge-xp4l` as the XP4Life interpretation and progression
  section that consumes structured upstream events without taking over execution.
- Promote `vaultforge-icon` as the lightweight icon workflow section with
  SVG-Forge as its first existing subtool.
- Keep VaultForge Code on the execution/reporting side and leave deeper XP
  interpretation for a future sibling section instead of folding it into the
  bridge lane.
- Build XP4Life Icons Part A as a concrete, repeatable lane rather than leaving it as a loose idea.
- Keep the icon workflow editable from notes first, then runnable from a simple batch entry point.
- Route icon outputs into this vault so prompts, docs, and results stay reviewable together.
- Seed only the operator-facing icon assets into `_template/` so new vaults inherit the workflow without inheriting the implementation planning notes.
- Treat the successful XP4Life run as proof that a broader VaultForge Icons branch is worth planning, but keep client/logo workflow work staged and selective.

## XP4Life Icons Part A Implementation Shape

- Source of truth for the concept lives in `vaultforge-icon/NOTE/Icons - part A.md`.
- Execution planning lives in `vaultforge-icon/NOTE/Icons - part A - todo.md`.
- Quick operator guidance lives in `vaultforge-icon/NOTE/Icons - part A - quick use guide.md`.
- Recommended prompts live in `ICON/XP4Life/part-a/prompts/`.
- The local launcher lives in `run-icons-part-a.bat`.
- The launcher may still delegate image generation directly to the old runtime/reference prototype at `F:\tools\image_generation\vaultforge-art\generate_art.py`.

## Watchpoints

- The Codex app sidebar can lose or regroup visible project/thread history; repo docs must remain strong enough to recover coordination without relying on that UI.
- Dedicated section threads can drift if they skip root `THREAD_MAP.md` or fail to update their section changelog.
- Root should not quietly become the worker space for tasks that belong in engine, business, or art.
- The coding bridge section can sprawl if it starts acting like the general
  implementation lane for unrelated VaultForge work.
- The coding bridge should emit factual events, not XP meaning, or it will blur
  into a future interpretation lane.
- XP4L can sprawl if it starts absorbing execution concerns before its event and
  output contracts are stable.
- `vaultforge-art` now has a root coordination base; the old runtime/reference prototype is `F:\tools\image_generation\vaultforge-art`, and the planned fresh lane is `F:\vaultforge\vaultforge-art`.
- The XP4Life launcher currently depends on a fixed sibling project path.
- The shared engine prototype is in this workspace, but the XP4Life launcher has not been retargeted to it yet.
- Prompt quality has one successful live Part A run, but Part B selection and packaging still need operator review.
- The current art project has a general `icon` preset, not a dedicated XP4Life preset yet.
- `vaultforge-icon/svg-forge` should be validated with dry-run checks before
  any feature work or cleanup.
- If XP4Life grows beyond Part A, prompt organization and naming rules will matter more than raw prompt volume.
- `_template/` now carries the optional icon lane, so future vault creation should be reviewed to make sure that remains helpful rather than noisy.
- Generated examples currently exist in `_template/` because the successful run was launched there; decide later whether template seed examples are helpful or should be moved into a separate demo pack.

## Forward Look

- The next dedicated engine thread should boot from root, then engine, then handle the engine-specific step 7 handoff from the business notes.
- Each active section should assign or naturally maintain one thread to keep `SIGN_UP.md`, `CHANGELOG.md`, and root handoff notes current.
- `vaultforge-engine/` now holds the first verified shared generator prototype.
- `vaultforge-business` now targets the shared engine directly while preserving business output routing.
- The next dedicated coding thread should scaffold the VaultForge Code bridge
  MVP inside `vaultforge-coding` without modifying unrelated sections.
- If VaultForge later promotes an XP interpretation section, it should consume
  coding events rather than push that logic back into `vaultforge-coding`.
- The next dedicated XP4L thread should lock the event contract and output
  contract before deeper progression heuristics harden.
- The next shared-core steps are safer dry-run semantics, wrapper parity checks, and only then native shared features such as variants, input images, tweaks, and galleries.
- If the first results are strong, Part B can add tighter naming rules, export selection, and curation notes.
- A dedicated XP4Life preset inside `vaultforge-art` may become worthwhile later.
- The next template decision is no longer whether to seed the lane, but whether the seeded version should be expanded, reduced, or split into optional packs later.
- A gallery note may become useful once this vault has real generated icon outputs to curate.
- VaultForge Icons can grow into a client/logo branch with YAML client intake, usage stats, price/ad reference docs, and image-reference editing, but those should be implemented after Part B selection/packaging.

## TASKS.md

# TASKS

## Todays Goal/Bonus
-*NEW*-  Todays Goal/Bonus. Achievable goal(s) that may be aimed for and reward both XP and Bonus-XP (XPLife) . To encourage reaching minor or Major milestones or even just some fun. Keep in mind these are not mandatory and priority tasks still take precedence.
```tasks
path includes TODAYS GOAL 
```

## Not Done System wide
```tasks
not done
sort by priority
```

## Active Pool

- [x] 🔺 Start the dedicated engine thread for the engine-specific step 7 handoff after it reads root `CODEX_START.md`, root `THREAD_MAP.md`, and engine section docs #engine #threading #nath 2026-04-13 ✅ 2026-04-13
- [ ] ⏫ Keep `THREAD_MAP.md` current as sections are promoted, parked, or moved #root #threading 🆔 root-thread-map-review 🔁 every week when done 2026-04-13
- [ ] 🔽 Decide whether parked folders such as `vaultforge-core`, `vaultforge-design`, `vaultforge-system`, and `vaultforge-init` should become promoted sections with full doc sets #root #planning 🆔 root-promote-parked-sections 2026-04-13
      #decided Yes these sections should be promoted with docs that reflect current vaultforge practices.
- [ ] 🔽 Decide when or whether the sibling art runtime should be migrated under root instead of only represented by the `vaultforge-art` coordination base #art #architecture 🆔 root-art-runtime-migration-decision ⛔ art-bridge-inventory 2026-04-13
- [ ] 🔼 Build Part B for XP4Life Icons: copy selected outputs into `selected/`, rename them cleanly, and create an icon index note #root #icons #xp4life 🆔 root-xp4life-part-b 2026-04-11
- [ ] 🔽 Decide whether XP4Life should earn a dedicated preset inside `vaultforge-art` instead of relying on the shared `icon` preset #root #icons #planning 🆔 root-xp4life-preset-decision 2026-04-11
- [ ] 🔽 Review whether the `_template/` version of the icon lane feels useful after a couple of real vault creates, or whether it should be reduced to a lighter stub #root #template #planning 🆔 root-template-lane-review 2026-04-11
- [ ] 🔽 Decide whether generated example PNGs should stay in `_template/` or move into a separate demo/example pack #root #template #icons 🆔 root-template-png-location 2026-04-11
- [ ] 🔼 Extend Part B once category naming, reward rules, and title rules settle from Part A output review #root #xp4life #planning 🆔 root-xp4life-part-b-extend ⛔ root-xp4life-part-b 2026-04-11
- [ ] 🔼 Prototype `VaultForge Icons` client job storage with `client.yaml`, references, generated, selected, delivery, and usage files #root #vaultforge-icons #clients 🆔 root-vaultforge-icons-client-storage 2026-04-11
- [ ] 🔽 Plan image-input and tweak/edit flags for VaultForge Icons after reviewing what belongs in `vaultforge-engine` versus lane wrappers #root #vaultforge-icons #api 🆔 root-vaultforge-icons-edit-flags 2026-04-11
- [ ] 🔽 Decide whether usage stats should start as CSV only or become JSON/YAML plus CSV exports #root #vaultforge-icons #stats 🆔 root-vaultforge-icons-stats-format ⛔ root-vaultforge-icons-client-storage 2026-04-11

## Landed Work

- [x] Promote `vaultforge-icon` as a lightweight active icon lane with section docs and SVG-Forge routed as the first existing subtool #icon #docs #threading 2026-05-03
- [x] Add Workflow B as a root long-run controller for repeated multi-agent Workflow A cycles, with a Python controller, batch launcher, cycle packets, lane scopes, and optional `codex exec` execution #root #threading #docs 2026-05-09
- [x] Add Workflow B commit policy handling so long-run agents can commit after review or per cycle without staging unrelated dirty files #root #threading #git 2026-05-09
- [x] Add root `WORKFLOW_REVIEW.md` and Workflow B change watching so long runs periodically review workflow health and refresh prompts when workflow docs change #root #threading #docs 2026-05-09
- [x] Add `business-if-done.txt` as a watched business-lane direction input for Workflow B business prompts #root #business #threading 2026-05-09
- [x] Add Workflow B timebox, estimated usage budget, and hard-gate mode controls for bounded long runs #root #threading #budget 2026-05-09
- [x] Add `MULTI_AGENT_WORKFLOW.md` as a lightweight root guide for simple Codex build runs with coordinator, builder, reviewer, recorder, decision gates, and handoff prompts #root #threading #docs 2026-05-03
- [x] Add `CURRENT_STATE.md` as a root recovery anchor for Codex app project/thread visibility drift, and link it from startup and routing docs #root #threading #docs 2026-04-27
- [x] Activate `vaultforge-xp4l` as an active section in root coordination docs
  and thread routing #xp4l #docs 2026-04-16
- [x] Promote `vaultforge-coding` into the VaultForge Code section and add its first local doc set #coding #docs 2026-04-16
- [x] Add the root/section thread model, root `THREAD_MAP.md`, section sign-up pattern, and art coordination base #root #docs #threading #nath 2026-04-13
- [x] Update `vaultforge-business` to target `vaultforge-engine` after the copied engine passed dry-run checks, while preserving current business output routing #business #engine 2026-04-12
- [x] Rename the shared engine entrypoint to `vaultforge-engine\src\generate.py` and refresh root docs around the current engine split #engine #docs 2026-04-12
- [x] Compare business wrapper dry-run behavior against direct engine calls before changing business defaults #business #engine 2026-04-12
- [x] Add the art compatibility bridge so `vaultforge-art\run_art.bat` delegates to `vaultforge-engine` while preserving art-root defaults #engine #compatibility 2026-04-12
- [x] Prototype `vaultforge-engine` by copying reusable generator code and tests from the dirty sibling `vaultforge-art` worktree without breaking current wrappers #engine #architecture 2026-04-12
- [x] Add `vaultforge-engine` documentation skeleton and root architecture note for staged engine extraction #engine #architecture 2026-04-11
- [x] Validate one live XP4Life Icons Part A generation run from `_template/` and copy examples into workspace outputs for review #root #icons #validation 2026-04-11
- [x] Add a lightweight output review note with the first successful icon examples #root #icons #docs 2026-04-11
- [x] Rewrite `How to - Create XP4Life Icon set (obsidian).md` with a transferable Obsidian icon-set method and required plugin ID #root #icons #obsidian 2026-04-11
- [x] Capture the broader `VaultForge Icons` branch plan from phone notes, including client templates, usage stats, pricing, ads, and future image-input flags #root #vaultforge-icons #planning 2026-04-11
- [x] Distill `Icons - part A` into a clean local reference note and attack-plan note #root #icons #docs 2026-04-11
- [x] Create a quick-use note with runnable commands and recommended prompts for XP4Life Icons Part A #root #icons #docs 2026-04-11
- [x] Add a reusable prompt bank for quests, achievements, titles, and rewards under `ICON/XP4Life/part-a/prompts/` #root #icons #prompts 2026-04-11
- [x] Add `run-icons-part-a.bat` as a local launcher that delegates generation to `vaultforge-art` while keeping prompts and outputs in this vault #root #icons #cli 2026-04-11
- [x] Verify the Part A launcher in `--dry-run` mode across quests, achievements, titles, and rewards #root #icons #validation 2026-04-11
- [x] Mirror the operator-facing Part A assets into `_template/` and add a small seeded `Home.md` entry point #root #icons #template 2026-04-11
- [x] Establish the core workspace docs for future Codex threads: `README.md`, `SYSTEM.md`, `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `CODEX_START.md` #root #docs #planning 2026-04-11

## Working Rules

- Keep actionable work here.
- Keep direction and tradeoffs in `PLAN.md`.
- Add new completed structural changes to `CHANGELOG.md`.
- If a workflow needs a short operator note, prefer a topic quick guide in `NOTE/`.
- Tag every task with at least one section tag and one task-type tag, for example `#root #threading` or `#engine #docs`.
- Set priority by section-local importance using Tasks markers: 🔺 highest, ⏫ high, 

[truncated for prompt packet]
## CHANGELOG.md

# CHANGELOG

## 2026-05-09

- Recorded Workflow B cycle 1 for run `20260509T204905-run-approved-section-local-build-slices`: engine dry-run smoke/manifest work and business native metadata bridge both passed reviewer checks with no hard gates and no live generation.
- Recorded a Workflow B cycle 1 root-recorder blocker for run `20260509T201250-run-approved-section-local-build-slices`: local shell inspection failed before PowerShell started with `windows sandbox: CryptUnprotectData failed: 2148073483`, so the recorder handoff explicitly avoids inferring builder or reviewer results.
- Added engine-local `.env` API-key loading and lane override flags in `vaultforge-engine`, with the default model pinned to `gpt-image-2-2026-04-21`.
- Added engine-native image input/reference support in `vaultforge-engine`: direct `--input-image` / `--reference-image` files and embedded images inside Markdown prompt notes can now be sent with the prompt for reference-driven generation and edits.
- Added Workflow B as a root long-run controller design with `MULTI_AGENT_WORKFLOW_B.md`, `workflow_b_controller.py`, and `run_workflow_b.bat`; it creates locked cycle packets and can optionally launch section-scoped `codex exec` agents.
- Added Workflow B commit policy flags so spawned agents can commit scoped work after review, per cycle, per agent, or never, while avoiding pre-existing dirty files.
- Added `WORKFLOW_REVIEW.md` and Workflow B workflow-change watching so long runs can refresh root workflow docs between cycles, detect changed workflow guidance, and surface updates in later prompts.
- Added `business-if-done.txt` as a watched business-lane direction input for Workflow B business agents.
- Added Workflow B timebox, estimated usage budget, and hard-gate response modes, with controller budget snapshots, stop handoffs, and agent final signal parsing.

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

- Added `ARCHIT

[truncated for prompt packet]
## MULTI_AGENT_WORKFLOW.md

# VaultForge Multi-Agent Workflow

Use this as the first lightweight operating model for a simple build that needs
more than one Codex pass without losing the thread.

The goal is not to build a full agent platform yet. The goal is to make one
build run inspectable, resumable, and easy to hand back to Nath when a decision
matters.

## First Shape

Start with four roles:

- Coordinator: owns the task brief, routes work, keeps the handoff current, and
  decides whether to continue, pause, or ask Nath.
- Builder: makes the smallest useful code or doc change inside one section.
- Reviewer: checks the Builder's result for bugs, drift, missing tests, and
  scope creep.
- Recorder: updates the repo-facing notes, changelog, task status, and next
  handoff prompt.

For Codex chat work, one agent can play multiple roles when the task is tiny.
The important part is that the roles happen in order and leave evidence.

## Simple Build Run

1. Pick one task from root or section `TASKS.md`.
2. Write a short build brief before editing:
   - target section
   - files likely to change
   - success check
   - stop/ask condition
3. Coordinator routes the task through `THREAD_MAP.md`.
4. Builder implements the smallest useful version.
5. Reviewer runs a meaningful verification.
6. Recorder updates the handoff notes and changelog.
7. Coordinator decides one of:
   - continue
   - pause with a clean handoff
   - ask Nath for a decision

## Rotation Continuation

The workflow should not stop just because one role found a review note or a
future approval need.

Use this split:

- Hard gate: stop and ask Nath.
- Soft gate: record the blocker or decision need as a task, then continue if
  there is an approved safe next slice.
- Live-required gate: record the needed live run as a `#live-required` task and
  continue with dry-run or build work if the live run is not required for the
  current safe milestone.
- Scoped local write: allowed when the task explicitly names the write scope
  and every written path stays inside that scope.

A run may continue into another Coordinator -> Builder -> Reviewer -> Recorder
rotation when all of these are true:

- the next slice is already scoped in `TASKS.md`
- the next slice is docs-only, dry-run, or otherwise safe
- any local writes are explicitly scoped and stay inside the approved
  lane/write scope
- the next slice does not change the main goal or require a new hard-gate Nath
  decision
- the current handoff stays updated
- the run remains inside its stated cycle budget

When a task requires Nath to approve, decide, unblock, or step in at a hard
gate, tag it with `#nath` in the relevant `TASKS.md`. When Nath has explicitly
cleared a task, tag it with `#approved`. When a task only needs a future
non-dry-run/live validation, tag it with `#live-required` and state what live
run is missing.

For tiny docs-only runs, a single rotation may land the active task plus up to
two small related tasks. Larger runs should state the intended cycle budget up
front and continue until that budget is spent or a hard gate appears.

## Decision Gates

Stop and ask Nath when the workflow reaches one of these gates:

- the next step changes architecture or ownership between sections
- the task changes direction away from the agreed main goal
- a secret, account, or external service needs a new permission
- there are two reasonable paths and the tradeoff is product/workflow taste
- there are two reasonable paths and the tradeoff is quantity/quality taste
- the task needs cloud notifications, remote runners, or persistent background
  work

Do not stop only because a future live run will eventually be needed. Record the
missing live step as `#live-required`, say exactly what live run is needed, and
continue with dry-run/build work when possible.

Do not treat scoped local file/folder writes as a hard gate by themselves when
the task explicitly approves them and the paths stay inside the lane/write
scope. This does not approve secrets/cloud auth, paid/API work, generated
artifacts without path approval, asset move/delete, folder-icon application,
ownership changes, or taste decisions.

When a gate happens, leave a short decision note with:

- what was done
- what is blocked
- the options
- the recommended option
- esitmated token usage so far and to contnue toward next milestone 
- the exact command or prompt to resume

If the gate is not blocking the current safe work, park it as `#nath` only when
it is a true hard gate. Otherwise use `#live-required` or a normal follow-up
task and continue with the next `#approved` docs-only, dry-run, or build task
instead of ending the run immediately.

## Handoff File Pattern

For a simple build, create or update a handoff note near the work:

- root coordination: `CURRENT_STATE.md` andor a short root note
- engine work: `vaultforge-engine/SIGN_UP.md` andor `vaultforge-engine/TASKS.md` 
- business work: `vaultforge-business/SIGN_UP.md` andor `vaultforge-business/TASKS.md`
- coding bridge work: `vaultforge-coding/SIGN_UP.md` andor
  `vaultforge-coding/TASKS.
- icon bridge work: `vaultforge-icon/SIGN_UP.md` andor
  `vaultforge-icon/TASKS.md` 



Keep the handoff short enough that a new thread can read it quickly.

Recommended shape:

```md
## Multi-Agent Handoff

- Task:
- Current role:
- Last verified state:
- Files touched:
- Verification run:
- Blocker or decision:
- Resume prompt:
```

## Skill Adoption Loop

Use skills only after a workflow repeats enough to deserve one.

1. Do the workflow manually once.
2. Record the exact prompts, files, checks, and failure points.
3. Repeat it on a second small task.
4. Extract only the stable parts into a skill.
5. Keep repo-specific routing in VaultForge docs, not inside a generic skill.

Good first skill candidates:

- build-brief-maker
- review-handoff-writer
- vaultforge-section-router
- smoke-test-recorder

## Cloud Notification Later

Cloud work is a later adapter, not the first dependency.

The first useful notification loop would be:

1. Local or cloud runner reaches a decision gate.
2. It writes the decision note into the repo or a small queue.
3. It sends Nath a notification with the short options.
4. Nath replies with a decision.
5. The runner resumes from the recorded prompt.

Until that exists, the repo handoff is the notification surface.

## Starter Prompt

Use this when starting a small multi-agent build in Codex:

```text
Use the VaultForge multi-agent workflow for a simple build.

Read CODEX_START.md, CURRENT_STATE.md, THREAD_MAP.md, TASKS.md, and
MULTI_AGENT_WORKFLOW.md first.

Act as Coordinator first. Pick or confirm the target task, write a short build
brief, then move through Builder, Reviewer, and Recorder roles. Stop for Nath
only at a decision gate. Keep changes small, verify what you can, and leave a
resume handoff if the run cannot finish. 
```

## MULTI_AGENT_WORKFLOW_B.md

# VaultForge Multi-Agent Workflow B

Workflow B is the long-run controller layer for Workflow A.

Workflow A defines the role order for one build rotation:

```text
Coordinator -> Builder -> Reviewer -> Recorder
```

Workflow B repeats that rotation across a cycle budget and keeps each lane run
locked to VaultForge routing, section docs, explicit write scopes, and durable
handoff files.

## Purpose

Use Workflow B when Nath wants a longer run such as:

```bat
run_workflow_b.bat --cycles 7 --lane vaultforge-engine --lane vaultforge-business --task "Build the approved engine/business slices from TASKS.md"
```

The controller does not replace Codex judgment. It creates the run packet,
agent prompts, cycle manifests, and optional `codex exec` calls that keep the
long run from drifting away from the root/section model.

## Workflow Patterns Used

Workflow B borrows practical patterns from `F:\toakezg\workflows\workflow-types.md`:

- Router-Triage: classify mixed work by lane, risk, and next workflow before deep execution.
- Memory-Context Refresh: reread current root/section docs and dirty state at cycle starts.
- Planner-Executor-Verifier: default build pattern for each lane.
- Parallel Specialist Review: use reviewers as risk lenses rather than rubber stamps.
- Sequential Builder-Critic Loop: refine docs, specs, prompts, and plans across bounded passes.
- Test-Driven Agent Loop: use concrete checks when code or CLI behavior is involved.
- Human-In-The-Loop Approval: stop for destructive, external, paid, secret, live, or taste-heavy gates.

## Commit Policy

Workflow B can instruct agents to commit as they work. The controller does not
blindly run `git add .` because VaultForge often has unrelated dirty files,
generated outputs, or active lane work in the same root.

Default commit mode is review:

```bat
run_workflow_b.bat --cycles 7 --execute --commit-mode review --lane vaultforge-engine --lane vaultforge-business --task "Run approved section-local build slices"
```

Modes:

| Mode | Behavior |
|---|---|
| `never` | Do not commit. Record changed files and suggested commit messages in handoffs. |
| `review` | Reviewer commits only after scoped lane changes pass review. This is the default. |
| `cycle` | Recorder commits at the end of each cycle after build and review notes are captured. |
| `agent` | Each agent may commit after its own coherent scoped work. Use sparingly. |

Every commit-capable prompt tells the agent to:

- run `git status --short` before editing and treat it as the dirty baseline
- never stage pre-existing unrelated dirty files
- stage only files changed by that agent inside its write scope
- inspect `git diff --cached --stat` before committing
- record the commit hash in the run packet or handoff note

Use `--commit-prefix` to change the start of generated commit messages.

## Control Script

- Python controller: `workflow_b_controller.py`
- Batch launcher: `run_workflow_b.bat`
- Default run output: `runs/workflow-b/<timestamp-slug>/`
- Lock file: `.workflow-b.lock`
- Workflow review note: `WORKFLOW_REVIEW.md`

The script can be run from root or from a section folder. When run from a
section folder, pass `--root F:\vaultforge` if auto-detection cannot find the
root docs.

## Operating Modes

### Plan/Dry Run

Default behavior is plan-first and no Codex execution.

```bat
run_workflow_b.bat --cycles 3 --lane vaultforge-engine --task "Prepare the next safe engine docs/build slice"
```

This writes:

- `workflow-b-plan.json`
- `workflow-b-plan.md`
- per-cycle prompt files
- a status JSONL file

### Execute

Add `--execute` only when the run is meant to launch Codex CLI agents.

```bat
run_workflow_b.bat --cycles 7 --execute --lane vaultforge-engine --lane vaultforge-business --task "Run approved section-local build slices"
```

Each agent prompt is sent through `codex exec` with a section-aware working
directory. The default is sequential execution. Add `--parallel` only when the
selected lanes have disjoint write scopes.

## Time And Usage Budgets

Workflow B can run by cycle count, timebox, estimated usage budget, or all
three together.

Example 2-hour run:

```bat
run_workflow_b.bat --cycles 99 --timebox-minutes 120 --usage-budget-usd 3.00 --estimated-agent-usd 0.08 --execute --bypass-sandbox --lane vaultforge-engine --lane vaultforge-business --task "Run approved section-local build slices"
```

Budget flags:

| Flag | Behavior |
|---|---|
| `--timebox-minutes 120` | Stops before starting more work after the timebox is reached. |
| `--usage-budget-usd 3.00` | Sets an estimated controller-side USD ceiling. |
| `--estimated-agent-usd 0.08` | Reserves this much estimated budget before each `codex exec` agent starts. |

The usage budget is intentionally conservative. Codex CLI does not currently
give this controller a reliable live token/cost feed, so Workflow B enforces
the estimate it is given and also asks agents to report a final
`WORKFLOW_B_USAGE_USD` signal when they can.

When a time or estimated usage budget is reached, the controller writes:

- a `budget_stop` event in `status.jsonl`
- `workflow-b-stop-handoff.md`
- the current budget snapshot
- the suggested next action

## Hard Gate Modes

Workflow B prompts every agent to end with a small signal block:

```text
WORKFLOW_B_HARD_GATE: yes|no
WORKFLOW_B_SAFE_WORK_REMAINS: yes|no
WORKFLOW_B_USAGE_USD: 0.00
WORKFLOW_B_NEXT_ACTION: short next action
```

The controller reads that block after each agent run.

Modes:

| Mode | Behavior |
|---|---|
| `--hard-gate-mode stop` | Stop the run when an agent reports a hard gate. |
| `--hard-gate-mode switch-safe` | Default. Continue only if the agent reports another approved safe slice remains; otherwise stop. |
| `--hard-gate-mode record-continue` | Record the hard gate and continue. Use only when the task/prompt already makes the safe fallback clear. |

This does not remove Workflow A's hard gate rules. It gives the batch
controller a strict way to react when spawned agents report those gates.

## Agent Model

Workflow B keeps the Workflow A roles but lets them repeat and split by lane.

Default agents:

- `root-coordinator`: reads root docs, routes slices, checks gates
- `<lane>-builder`: performs one safe section-local task per cycle
- `<lane>-reviewer`: reviews the builder's result and records issues
- `root-recorder`: updates handoff/changelog/task notes when the cycle allows

You can assign more than one task to an agent:

```bat
run_workflow_b.bat --cycles 5 --lane vaultforge-coding --agent-task vaultforge-coding-builder:"finish context collection; add prompt saving"
```

The controller treats semicolon-separated items as separate tasks inside that
agent's cycle prompt.

## Cycle Rules

Each cycle follows this shape:

1. Root coordinator rereads `CODEX_START.md`, `CURRENT_STATE.md`,
   `THREAD_MAP.md`, `TASKS.md`, and `MULTI_AGENT_WORKFLOW.md`.
2. Lane agents reread their section `CODEX_START.md`, `SYSTEM.md`, `PLAN.md`,
   `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.
3. Builders do the smallest safe slice in their lane write scope.
4. Reviewers verify the result and name any missing tests or drift.
5. Recorder writes the factual handoff and logs the next safe step.
6. Coordinator either continues, records a soft gate, or stops at a hard gate.
7. If the commit policy allows it, the reviewer or recorder commits only the
   scoped work from that review/cycle.
8. The controller checks watched workflow docs before the next cycle and
   refreshes prompts if workflow guidance changed.

The cycle budget is a hard cap. `--cycles 7` means at most seven rotations, not
seven unlimited builds.

## Workflow Change Watching

Workflow B watches workflow documents between cycles by default.

Watched files include:

- `MULTI_AGENT_WORKFLOW.md`
- `MULTI_AGENT_WORKFLOW_B.md`
- `WORKFLOW_REVIEW.md`
- `THREAD_MAP.md`
- `TASKS.md`
- `business-if-done.txt`
- `F:\toakezg\workflows\workflow-types.md` when present

If any watched file changes while the r

[truncated for prompt packet]
## WORKFLOW_REVIEW.md

# VaultForge Workflow Review

This note is the root review surface for Workflow A and Workflow B.

It exists so long-running Workflow B runs have one short place to check whether
the workflow itself is still behaving well.

## Imported Lessons From Workflow Types

- Router-Triage should be the front door for vague or mixed work. Classify
  tasks by lane, risk, workflow type, and next action before sending agents out.
- Memory-Context Refresh should happen at the start of each cycle. Agents should
  reread current root/section docs, current dirty state, and handoff notes
  instead of relying only on cycle 1 context.
- Planner-Executor-Verifier is the default lane pattern for actual build work:
  inspect, plan, execute, verify, then narrow-fix if needed.
- Parallel Specialist Review fits review-heavy steps where multiple risk lenses
  matter, such as tests, contracts, scope drift, and operator workflow.
- Sequential Builder-Critic Loop fits docs, specs, prompt packs, and quality
  improvement over a small number of passes.
- Test-Driven Agent Loop fits code, CLIs, parsers, and repeatable behavior
  where checks can control the loop.
- Human-In-The-Loop Approval remains the hard gate for destructive, external,
  paid, secret, live, asset-moving, or taste-heavy decisions.

## Workflow B Review Cadence

- The controller updates the snapshot block every `--workflow-review-every`
  cycles. Default: every 2 cycles.
- The controller also updates this note when watched workflow docs change.
- Time and estimated usage budgets should be set on long runs when Nath wants a
  bounded session, such as a 2-hour work block.
- Hard gate mode should be explicit for unattended-ish runs. Default is
  `switch-safe`.
- Agents should treat this note as guidance, not permission to bypass
  `THREAD_MAP.md`, lane ownership, or decision gates.

## Watched Workflow Inputs

- `MULTI_AGENT_WORKFLOW.md`
- `MULTI_AGENT_WORKFLOW_B.md`
- `WORKFLOW_REVIEW.md`
- `THREAD_MAP.md`
- `TASKS.md`
- `business-if-done.txt` as business-lane direction when present
- `F:\toakezg\workflows\workflow-types.md` when it exists

## Review Questions

- Did the last cycle start from current root and section docs?
- Was the task routed to the right lane?
- Did each agent stay inside its write scope?
- Did reviewers verify real behavior or only restate intent?
- Did commit policy avoid pre-existing dirty files?
- Did any workflow change appear mid-run, and was it included in the next
  prompt?
- For business-lane work, did the agent check `business-if-done.txt` without
  treating it as a blank approval for broad changes?
- Did the run stay inside its time and estimated usage budgets?
- If a hard gate appeared, did the selected hard-gate mode handle it correctly?

<!-- workflow-b-controller-snapshot:start -->
## Controller Review Snapshot

- Updated: `2026-05-09T21:38:35+10:00`
- Reason: cycle review cadence
- Run id: `20260509T213834-verify-budget-and-gate-flags-in-dry-run`
- Cycle: `1` of `2`
- Run packet: `F:\vaultforge\runs\workflow-b-verify\20260509T213834-verify-budget-and-gate-flags-in-dry-run`
- Commit mode: `review`
- Timebox minutes: `120.0`
- Usage budget USD: `3.0`
- Hard gate mode: `switch-safe`
- Watched workflow changes this cycle:
- none detected

## Current Workflow Lessons

- Use Router-Triage at the front of mixed or vague long-run tasks.
- Use Memory-Context Refresh at the start of each cycle so agents respect current docs and dirty state.
- Use Planner-Executor-Verifier as the default build lane pattern.
- Use Parallel Specialist Review when review needs multiple risk lenses.
- Use Test-Driven Agent Loop for code or CLI behavior with concrete checks.
- Use Human-In-The-Loop gates for destructive, external, paid, secret, or taste-heavy decisions.
- Keep Workflow B adaptive by refreshing workflow docs between cycles rather than freezing the first prompt forever.
<!-- workflow-b-controller-snapshot:end -->








## Section Docs Snapshot

[root agent: use root docs snapshot]
