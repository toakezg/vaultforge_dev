# Project Pack Operating Model

This note explains the method behind the pack so it can be reused in projects
that do not already know this operating model.

## Core ideas

- start from the project root before making large local assumptions
- keep one coordination layer for architecture, routing, planning, and shared
  documentation
- give stable ownership areas their own local doc packs
- prefer plain Markdown truth over perfect-looking but stale docs
- document real decisions, not speculative tool choices

## Document roles

### Root docs

- `README.md` states what the project is and what the root layer is for
- `CODEX_START.md` gives new threads the startup order
- `SYSTEM.md` defines the operating model and ownership rules
- `THREAD_MAP.md` routes work and records which folders own which kinds of
  changes
- `PLAN.md` holds direction, watchpoints, tradeoffs, and forward look
- `TASKS.md` holds actionable project-level work
- `CHANGELOG.md` records notable coordination-level changes

### Workstream docs

- `CODEX_START.md` boots a thread into the local lane after root orientation
- `SYSTEM.md` defines lane boundaries and local rules
- `PLAN.md` holds local direction and local watchpoints
- `TASKS.md` holds actionable lane work
- `CHANGELOG.md` records notable lane changes
- `SIGN_UP.md` keeps a short thread trace so handoff recovery is easier

## What gets updated and when

- update `README.md` when the role of the folder changes materially
- update `CODEX_START.md` when the startup path changes
- update `SYSTEM.md` when ownership, boundaries, or rules change
- update `THREAD_MAP.md` when routing or ownership moves
- update `PLAN.md` when direction, tradeoffs, or watchpoints change
- update `TASKS.md` as work becomes active, blocked, landed, or no longer real
- update `CHANGELOG.md` when something meaningful lands
- update `SIGN_UP.md` when a new thread starts substantial work in a workstream

## Working method

### Root first

Threads should read the project root docs before deep work in a local folder.
This keeps changes routed through the current project model instead of through
stale assumptions.

### Ownership before action

When work might touch more than one folder, use `THREAD_MAP.md` to decide where
it belongs before editing across the project.

### Keep direction separate from tasks

`PLAN.md` is for direction, tradeoffs, and watchpoints.
`TASKS.md` is for actionable work.
Do not turn one into a messy copy of the other.

### Keep commands out until they are real

Do not fill these docs with presumed CLI commands, script names, or runtime
steps unless the project has actually chosen them. This pack is intentionally
neutral on implementation details.

## Adopting into an existing project

- document the project as it is now, not as you wish it already was
- start with the root pack plus only the workstreams that clearly own real work
- do not backfill fake changelog history
- do not force every folder into being an active workstream
- keep placeholders visible until you know the right wording

## When to add a new workstream

Add a workstream pack when a folder has:

- stable ownership
- recurring work
- rules or boundaries worth keeping local
- enough activity that future threads will benefit from a local startup note

If a folder does not meet that bar yet, keep it simple and let root continue to
coordinate it.
