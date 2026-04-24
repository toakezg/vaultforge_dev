# SYSTEM

## Purpose

This workspace root is the coordination layer for `{project_name}`.

It exists to keep reusable planning, routing, handoff, and project-wide
documentation together so new work can start from a clear operating base.

## Operating Principles

- keep the root layer lightweight
- use root for coordination, not lane clutter
- prefer documented ownership over implied ownership
- route work through `THREAD_MAP.md` before cross-workstream edits
- keep planning notes and operational notes in plain Markdown
- keep handoffs visible enough that future threads can recover context fast
- avoid baking in unchosen implementation details

## Root Responsibilities

Root owns:

- project architecture decisions
- workstream routing
- cross-workstream planning
- coordination-level tasks
- coordination-level changelog updates
- project-level operating rules

Root does not own:

- focused implementation that belongs inside active workstreams
- duplicated copies of local rules when a workstream can hold them locally

## Documentation Rules

- `CODEX_START.md` is the preferred boot note for new threads
- `THREAD_MAP.md` decides which folder should own a task
- `PLAN.md` tracks direction, intent, tradeoffs, and watchpoints
- `TASKS.md` tracks actionable project-level work
- `CHANGELOG.md` records notable project-level changes with newest entries first
- active workstreams should keep their own `CODEX_START.md`, `SYSTEM.md`,
  `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`

## Task Rules

- every task line should include at least one workstream tag and one task-type
  tag
- active and next tasks should use local priority markers
- active and next tasks should carry short stable ids when practical
- dependency links should be explicit
- recurring work should use recurrence markers only for genuine loops
- if you use the Tasks plugin, keep an automatic `tasks` query above manual
  task sections

## Root And Workstream Model

- root is the coordinator and architect
- active workstreams are focused ownership areas
- not every folder needs to be an active workstream
- add a local workstream pack when a folder has stable boundaries and recurring
  work
