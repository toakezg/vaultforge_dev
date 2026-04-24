# Project Pack

Date: 2026-04-24
Status: first general-purpose draft

This package is a reusable documentation starter for projects that want a clear
operating model without importing repo-specific naming or structure.

It is designed to help you scaffold either:

- a whole project root plus active workstreams
- or one new active workstream inside an existing project

## Package layout

- `START_HERE.md` - quick operator guide for using the pack
- `ADOPT_THIS_PACK.md` - thread-facing adoption brief for morphing the pack
  into project docs
- `root/` - templates for the project coordination layer
- `workstream-core/` - the reusable six-file workstream starter pack
- `profiles/` - overlays that adapt a workstream to a specific role
- `examples/` - pre-assembled examples for common workstream shapes
- `operating-model.md` - the general rules for how these docs work together
- `install-guide.md` - step-by-step adoption guidance

## What this pack assumes

This pack assumes:

- the project benefits from one clear coordination layer
- threads should orient through project-level docs before deep local edits
- stable work areas should own their own local docs
- planning, tasks, handoffs, and changelog traces are operating documents
- commands, runtimes, and tooling choices should only be documented when they
  are real project decisions

## Workstream minimum

The base workstream pack is:

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

## Root package contents

The root starter set in `root/` includes:

- `README.md`
- `CODEX_START.md`
- `SYSTEM.md`
- `THREAD_MAP.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`

## Profile overlays

Start from `workstream-core/`, then choose the closest profile in `profiles/`:

- `shared-platform/` for shared runtime, contracts, adapters, or reusable core
- `delivery-lane/` for workflow, prompts, outputs, review, or operator-facing
  lanes
- `external-runtime/` for coordination above a tool, engine, or runtime that
  lives elsewhere
- `setup-tooling/` for bootstrapping, local setup, scripts, and tooling rules

## Recommended adoption flow

### To scaffold a full project

1. Copy `root/` into the project root.
2. Decide which folders are active workstreams.
3. Copy `workstream-core/` into each active workstream folder.
4. Apply the closest profile overlay to each workstream.
5. Use `ADOPT_THIS_PACK.md` to guide the first adoption thread.
6. Replace placeholders before the first real thread uses the docs.

### To scaffold one workstream inside an existing project

1. Copy `workstream-core/` into the target folder.
2. Apply the closest profile overlay from `profiles/`.
3. Add the workstream to the root `THREAD_MAP.md`.
4. Update root startup docs if the new workstream needs explicit routing.
5. Use `ADOPT_THIS_PACK.md` if you want a thread to reshape the pack into the
   local project's real docs.

## Placeholder fields used in this pack

Replace these before adoption:

- `{project_name}`
- `{workstream_name}`
- `{workstream_slug}`
- `{workstream_tag}`
- `{workstream_role}`
- `{workstream_owns}`
- `{workstream_does_not_own}`
- `{related_workstreams}`
- `{cross_stream_reporting_rule}`
- `{current_rule}`
- `{current_direction}`
- `{external_dependency_path_optional}`
- `{watchpoints}`
- `{forward_look}`

## Intent

This pack is meant to be:

- generic enough for outside projects
- specific enough to teach a thread how the docs are used
- light enough to customize quickly

It does not try to encode project history. It gives you:

- a project coordination layer
- an active-workstream starter pack
- profile-driven workstream adaptation

If you want the easiest first use, start with `START_HERE.md`.
