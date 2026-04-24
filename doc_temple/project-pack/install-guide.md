# Project Pack Install Guide

Date: 2026-04-24
Status: first install guide

This guide shows how to use `project-pack` in a new or already-running project
without having to reverse engineer the package structure.

If you want to hand the pack directly to a thread after dropping it into a
repo, start with `START_HERE.md` and `ADOPT_THIS_PACK.md`.

## Choose your starting shape

Use one of these two paths:

### Path A - build from the base pack

Use this when you want the cleanest, most customizable install.

Copy:

- `root/` if you need a coordination layer
- `workstream-core/` for each active workstream
- the matching profile from `profiles/`

Best for:

- new projects
- established projects that are ready to document real ownership
- users who want fine control over wording

### Path B - start from a pre-assembled example

Use this when you already know the rough shape and want a quicker start.

Copy from:

- `examples/root-coordinator/`
- `examples/shared-platform-workstream/`
- `examples/delivery-lane-workstream/`
- `examples/external-runtime-workstream/`
- `examples/setup-tooling-workstream/`

Best for:

- quick setup of a project root
- rapid documentation of one active workstream
- users who want a strong starter shape before customizing

## New project install

1. Copy `root/` into the project root.
2. Decide which folders should be active workstreams.
3. For each active workstream, copy `workstream-core/` into that folder.
4. Apply the closest profile from `profiles/`.
5. Use `ADOPT_THIS_PACK.md` to guide the first adoption thread.
6. Replace placeholders before the first live thread uses the docs.
7. Add an initial `CHANGELOG.md` entry only for real setup work you are doing
   now.

## Existing project install

1. Copy `root/` into the project root.
2. Describe the project as it actually operates today.
3. Add only the workstreams that already have clear ownership.
4. Use `THREAD_MAP.md` to describe real routing before making large cross-folder
   changes.
5. Use `ADOPT_THIS_PACK.md` to drive the first audit-and-morph pass.
6. Replace placeholders in the adopted docs.
7. Do not invent old changelog history.

## New workstream install

1. Pick the target folder.
2. Copy `workstream-core/` into it.
3. Apply the matching profile overlay.
4. Replace placeholders with real local language.
5. Add the workstream to root `THREAD_MAP.md`.
6. Check root `CODEX_START.md` if the startup path should be explicit.

## Direct adoption flow

If you want to drop the pack into a repo and point a thread at it:

1. Copy the whole `project-pack` folder into the target repo.
2. Tell the thread to read `START_HERE.md`.
3. Tell the thread to follow `ADOPT_THIS_PACK.md`.
4. Let the thread morph the pack into a project-tailored `./docs` folder or
   another project-specific docs home if the repo already has one.

That flow is usually the best fit for established projects because it lets the
thread scale the docs to the real repo instead of forcing a fixed shape.

## Placeholder replacement checklist

Replace these first:

- project name
- workstream name
- workstream tag
- role sentence
- owns list
- does-not-own list
- related workstreams
- current rule
- current direction
- watchpoints
- forward look
- external dependency path if the workstream needs one

## First-use quality check

Before a real thread starts working from the installed docs, check:

- does root clearly own coordination and routing
- does each workstream clearly own its lane
- do startup docs point through root first
- do task tags make sense
- are tasks separate from direction notes
- are changelog and sign-up traces present where needed
- are dangerous dependencies or external runtimes called out explicitly

## Small-project rule

Not every project needs multiple workstreams.

If the project is small, start with root only. Add workstream packs when the
project actually has stable local lanes worth documenting.
