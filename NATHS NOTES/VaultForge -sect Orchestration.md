This outlines how VaultForge is coordinated from the root `vaultforge\` directory and from the dedicated section bases. Root is the coordinator and architect. Section folders are worker bases with their own focused thread context.

## VaultForge Section Requirements

### All Sections

Each promoted section must keep these documents current:

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

All section documents must be tuned to that section. They should tell a new thread what to read, what the section owns, what it must not touch, what tasks are active, and how to report back upward.

- [x] Section structure and requirements put in place #nath #assist-required #ask 2026-04-13

# Section Structure And Requirements

```text
vaultforge\
  CODEX_START.md        root/orchestration start
  README.md             project overview and quick orientation
  SYSTEM.md             cross-lane rules and operating model
  PLAN.md               root direction, coordination priorities, watchpoints
  TASKS.md              cross-lane active pool and handoff tasks
  THREAD_MAP.md         where to work for what
  CHANGELOG.md          high-level cross-lane log
  ARCHITECTURE*.md      boundary decisions that affect multiple sections
  Nath's Notes\         operator notes, raw handoffs, and planning captures
```

Other root requirements:

- Root should not become the place where every worker task gets done.
- Root owns cross-lane decisions, section promotion, handoff quality, and documentation hygiene.
- Root should keep a short thread map so new threads know whether to work in root, engine, business, or art.
- Root should record cross-section changes in the root changelog and then point to the section changelog for detail.
- Root should only edit section files when setting up coordination, resolving conflicts, or making cross-lane documentation updates.

```text
vaultforge-engine\
  CODEX_START.md        engine-specific start
  SYSTEM.md             engine boundaries, contracts, and methods
  PLAN.md               engine plans and roadmap
  TASKS.md              active, next, and cross-section pending tasks
  CHANGELOG.md          timestamped engine changes
  SIGN_UP.md            new threads sign in here and list at least one role
```

Other engine requirements:

- tighter technical focus
- fewer lane-specific assumptions
- careful shared-contract mindset
- tests or dry-run verification for behavior changes
- wrapper compatibility notes when business or art could be affected

```text
vaultforge-business\
  CODEX_START.md        business-specific start
  SYSTEM.md             business boundaries, contracts, and methods
  PLAN.md               business plans and roadmap
  TASKS.md              active, next, and cross-section pending tasks
  CHANGELOG.md          timestamped business changes
  SIGN_UP.md            new threads sign in here and list at least one role
```

Other business requirements:

- keep client-facing workflow separate from art playground work
- keep prompt banks, client/job/tag naming, generated outputs, galleries, and review helpers lane-owned
- use `vaultforge-engine` for shared generation behavior instead of duplicating engine code
- report upward when business needs new engine features or when wrapper behavior changes
- protect client output routing and metadata conventions during parallel work

```text
vaultforge-art\
  CODEX_START.md        art-specific start
  SYSTEM.md             art boundaries, contracts, and methods
  PLAN.md               art plans and roadmap
  TASKS.md              active, next, and cross-section pending tasks
  CHANGELOG.md          timestamped art changes
  SIGN_UP.md            new threads sign in here and list at least one role
```

Other art requirements:

- treat this root section as the art coordination base until the actual art worktree is migrated
- current art runtime remains at `E:\tools\image_generation\vaultforge-art`
- keep experiments, playground presets, prompt packs, and unstable creative trials out of engine/business
- report upward before changing shared wrappers or moving any reusable behavior into engine
- do not delete or flatten messy art experiments just to make the section look tidy

## Section Threads

Multiple threads per section will be standard. Each section thread should get guidance from:

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

Each section thread should also read the overhead context:

1. `vaultforge\CODEX_START.md`
2. `vaultforge\SYSTEM.md`
3. `vaultforge\THREAD_MAP.md`

Note:

- Allocate one thread in each section to keep section `CHANGELOG.md`, section `SIGN_UP.md`, and root `THREAD_MAP.md` aligned.
- Section work should happen in the section folder unless the task is explicitly cross-lane.
- Cross-lane blockers should be reported to root instead of being solved by quiet edits across unrelated sections.
- Tasks should be tagged and prioritized inside the section first. Root can compare section priorities later, but each section should mark what is important for its own work.
- Each section `TASKS.md` should show its open tasks with a `tasks` code block above manual active/next sections, filtered by section tag.

Example:

```tasks
not done
tag includes business
```

## Task Priority Reference

| Priority | Tasks Marker | Section Meaning | Use When |
|---|---|---|---|
| No priority | none | Captured but not ranked yet | Inbox, backlog, unclear value, or needs review before ranking |
| Lowest | ⏬ | Nice-to-have | Cleanup, polish, future convenience |
| Low | 🔽 | Useful but not urgent | Improves section quality but does not unblock work |
| Medium | 🔼 | Normal planned work | Worth doing in the section's active or next flow |
| High | ⏫ | Important to this section | Blocks or strongly improves current section progress |
| Highest | 🔺 | Section-critical | Must happen before meaningful progress continues, urgent handoff, broken workflow, or user-directed priority |

## Task Property Reference

Use the Obsidian Tasks modal or auto-suggest when adding special task properties so field order stays valid.

Active and next tasks should carry a short stable `🆔` id so `before this` and `after this` links can be applied without rewriting the task text.

| Property | Use Now? | Section Rule |
|---|---|---|
| `🆔` task id | Yes | Give active and next tasks a short stable id, usually `section-topic-action`. |
| `🔁` recurs | Yes | Use only for genuine recurring work. Prefer `when done` for maintenance loops. |
| `before this` | Yes | In Markdown, the blocked task gets `⛔ prerequisite-id`, and the prerequisite task needs its own `🆔`. |
| `after this` | Yes | In Markdown, the current task gets a `🆔` and the follow-up task points back to it with `⛔ current-id`. Skip duplicate linking if the next task already uses `before this`. |
| `due`, `scheduled`, `start` | Not yet | Leave unused until a later planning pass. |
| `created` | Not yet | Leave unused for now. |
| `done (x)` | Already in use | Keep using `[x]` plus completion dates when useful. |
| `cancelled (-)` | Already in use | Use `[-]` when the work is intentionally dropped. |

## Root And Sections: When To Use

All sections have their own time to be used.

Summary:

- Use root when coordinating, deciding direction, comparing lanes, or preparing handoffs.
- Use `vaultforge-engine` when changing shared generator code, CLI behavior, output contracts, dry-run behavior, metadata, or tests.
- Use `vaultforge-business` when changing client packs, prompt banks, business wrappers, gallery/review tooling, Dataview, or business output routing.
- Use `vaultforge-art` when changing art/playground workflows, creative prompt packs, experimental presets, or art output curation.

### Root Use

Root is for overhead work:

- decide which section owns a task
- promote or park sections
- update `THREAD_MAP.md`
- coordinate handoffs between business, engine, and art
- keep root docs aligned with the real folder model
- capture broad architecture decisions and cross-section risks
- record high-level changes in root `CHANGELOG.md`

Root should avoid making deep lane changes unless the job is specifically a coordination pass or a cross-lane fix.

### Engine Use

For engine work, the thread should focus on:

- CLI contracts
- shared presets/styles/mods
- output behavior
- batch behavior
- dry-run behavior
- metadata behavior
- compatibility with wrappers
- tests

It should report back upward by updating engine docs/changelog and, when relevant, leaving a short note for business/art saying what changed.

### Business Use

For business work, the thread should focus on:

- client pack structure
- prompt-bank templates and status tracking
- business wrappers and markdown-bank runners
- client/job/tag naming rules
- generated output routing
- gallery, contact-sheet, and review helpers
- Dataview or Obsidian operator surfaces

It should report upward when it needs shared engine support or when a business wrapper change could affect engine contracts.

### Art Use

For art work, the thread should focus on:

- playground and creative prompt packs
- art-specific presets, styles, and modifiers
- experiments and visual exploration
- art output curation
- compatibility checks for the art bridge to `vaultforge-engine`

It should report upward before moving reusable behavior into engine or before changing anything that business depends on.

## Mental Model

```text
vaultforge root
= air traffic control and architect

vaultforge-engine
= shared machinery and contracts

vaultforge-business
= client/business workflow lane

vaultforge-art
= art/playground workflow lane
```

## VaultForge Thread Map

```text
# VaultForge Thread Map

## Root Thread
Use for cross-lane planning, architecture decisions, thread routing, section promotion, and handoffs.

Read:
- CODEX_START.md
- README.md
- SYSTEM.md
- PLAN.md
- TASKS.md
- THREAD_MAP.md
- CHANGELOG.md

Report changes to:
- CHANGELOG.md
- affected section CHANGELOG.md files when root changes section contracts

## Engine Thread
Use for shared generator behavior, CLI flags, presets/styles/mods, output contracts, metadata, dry-run behavior, compatibility, and tests.

Read:
- ../CODEX_START.md
- ../SYSTEM.md
- ../THREAD_MAP.md
- ./CODEX_START.md
- ./SYSTEM.md
- ./PLAN.md
- ./TASKS.md
- ./CHANGELOG.md
- ./SIGN_UP.md

Report changes to:
- ./CHANGELOG.md
- ../CHANGELOG.md when the change affects multiple sections
- affected lane notes if wrappers need updates

## Business Thread
Use for client packs, prompt banks, business wrappers, gallery/review tooling, Dataview, and business output routing.

Read:
- ../CODEX_START.md
- ../SYSTEM.md
- ../THREAD_MAP.md
- ./CODEX_START.md
- ./SYSTEM.md
- ./PLAN.md
- ./TASKS.md
- ./CHANGELOG.md
- ./SIGN_UP.md

Report changes to:
- ./CHANGELOG.md
- ../CHANGELOG.md when the change affects root coordination or engine contracts

## Art Thread
Use for playground/art presets, creative workflows, experiments, art bridge checks, and art lane output.

Read:
- ../CODEX_START.md
- ../SYSTEM.md
- ../THREAD_MAP.md
- ./CODEX_START.md
- ./SYSTEM.md
- ./PLAN.md
- ./TASKS.md
- ./CHANGELOG.md
- ./SIGN_UP.md

Report changes to:
- ./CHANGELOG.md
- ../CHANGELOG.md when the change affects root coordination or engine contracts
```
