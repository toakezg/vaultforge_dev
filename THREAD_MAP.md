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
| Low | 🔽 | Useful but not urgent | Improves section quality but does not unblock work |
| Medium | 🔼 | Normal planned work | Worth doing in the section's active or next flow |
| High | ⏫ | Important to this section | Blocks or strongly improves current section progress |
| Highest | 🔺 | Section-critical | Must happen before meaningful progress continues, urgent handoff, broken workflow, or user-directed priority |

Active and next tasks should normally have a priority marker. New inbox or parked backlog tasks may be left with no priority until the section reviews them.

## Task Property Rule

Use the Obsidian Tasks modal or Tasks auto-suggest when adding special task properties. It keeps the field order clean and reduces malformed task lines.

Active and next tasks should also carry a short stable `🆔` id so `before this` and `after this` links can be added without rewriting the task text.

| Property | Use Now? | VaultForge Rule |
|---|---|---|
| `🆔` task id | Yes | Give active and next tasks a short stable id, usually `section-topic-action`. |
| `🔁` recurs | Yes | Use only for genuine recurring work. Prefer `when done` for maintenance loops. |
| `before this` | Yes | In Markdown, put `⛔ prerequisite-id` on the blocked task and make sure the prerequisite task has its own `🆔`. |
| `after this` | Yes | In Markdown, give the current task a `🆔` and link the follow-up task with `⛔ current-id`. Do not duplicate the relationship if the next task already uses `before this`. |
| `due`, `scheduled`, `start` | Not yet | Hold these for a later planning pass. |
| `created` | Not yet | Do not standardize this yet. |
| `done (x)` | Already in use | Keep using `[x]` plus completion dates when helpful. |
| `cancelled (-)` | Already in use | Use `[-]` only when the work is intentionally dropped. |

We are not standardizing completion-side follow-up properties beyond these rules yet.
