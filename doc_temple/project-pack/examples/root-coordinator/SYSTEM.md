# SYSTEM

## Purpose

This workspace root is the coordination layer for `Example Project`.

It keeps architecture, routing, planning, and shared documentation in one
recoverable place.

## Operating Principles

- keep root lean
- route cross-workstream work before editing broadly
- keep local rules in local folders when ownership is clear
- avoid documenting tools or commands until they are real project choices

## Root Responsibilities

Root owns:

- project architecture
- workstream routing
- cross-workstream planning
- project-level docs
- shared change tracking

Root does not own:

- focused workstream implementation
- duplicated copies of local rules

## Documentation Rules

- `CODEX_START.md` is the startup note
- `THREAD_MAP.md` routes work
- `PLAN.md` holds direction and watchpoints
- `TASKS.md` holds actionable project-level work
- `CHANGELOG.md` records notable project-level changes
