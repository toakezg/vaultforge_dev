# SYSTEM

## Purpose

This workspace is the root coordination layer for `Example Project`.

It exists to keep planning, routing, handoff, and system-wide documentation in
one place so section threads have a reliable overhead base.

## Operating Principles

- keep root lightweight
- use root for coordination, not lane clutter
- prefer explicit ownership over guesswork
- route work through `THREAD_MAP.md` before cross-section edits
- keep handoffs visible enough for future threads to recover context fast

## Root Responsibilities

Root owns:

- architecture decisions
- section promotion and parking
- thread routing
- cross-lane planning
- coordination-level task tracking
- coordination-level changelog updates

Root does not own:

- shared runtime implementation that belongs in `shared-core`
- delivery workflow behavior that belongs in `delivery-lane`
- external runtime experimentation that belongs behind `creative-bridge`
- setup tooling details that belong in `project-init`
