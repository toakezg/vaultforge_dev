# SYSTEM

## Purpose

This workspace is the root coordination layer for `{project_name}`.

It exists to keep reusable planning, routing, handoff, and system-wide
documentation together so new work can start from a clear operating base.

## Operating Principles

- keep the root layer lightweight
- use root for coordination, not lane clutter
- prefer documented ownership over implied ownership
- route work through `THREAD_MAP.md` before cross-section edits
- keep planning notes and operational notes in plain Markdown
- keep handoffs visible enough that future threads can recover context fast

## Root Responsibilities

Root owns:

- architecture decisions
- section promotion and parking
- thread routing
- cross-lane planning
- coordination-level tasks
- coordination-level changelog updates

Root does not own:

- focused lane implementation that belongs inside promoted sections
- duplicated copies of section-owned rules when the section can hold them locally

## Documentation Rules

- `CODEX_START.md` is the preferred boot note for new threads
- `THREAD_MAP.md` decides which section should own a task
- `PLAN.md` tracks direction, intent, tradeoffs, and watchpoints
- `TASKS.md` tracks actionable coordinator work
- `CHANGELOG.md` records notable coordination changes with newest entries first
- promoted sections should keep their own `CODEX_START.md`, `SYSTEM.md`,
  `PLAN.md`, `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`

## Task Rules

- every task line should include at least one section tag and one task-type tag
- active and next tasks should use section-local priority markers
- active and next tasks should carry short stable ids when practical
- recurring work should use recurrence markers only for genuine loops
- dependency links should be explicit
- promoted sections should include an automatic `tasks` query above manual task
  sections

## Root And Section Model

- root is the coordinator and architect
- promoted sections are worker bases
- parked folders are not active worker bases until root promotes them
