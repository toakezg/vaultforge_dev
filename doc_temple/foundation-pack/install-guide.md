# Foundation Pack Install Guide

Date: 2026-04-16
Status: first install guide

This guide shows how to use the `foundation-pack` without having to reverse
engineer the package structure first.

## Choose your starting shape

Use one of these two paths:

### Path A - build from the base pack

Use this when you want the cleanest, most customizable install.

Copy:

- `root/` if you need a coordinator layer
- `section-core/` for each promoted section
- the matching profile from `profiles/`

Best for:

- new projects
- projects that already know their section roles
- users who want fine control over wording

### Path B - start from a pre-assembled example

Use this when you already know the section shape and want a quicker start.

Copy from:

- `examples/root-coordinator/`
- `examples/shared-contract-section/`
- `examples/operator-lane-section/`
- `examples/external-runtime-coordination-section/`
- `examples/setup-tooling-section/`

Best for:

- quick promotion of a parked folder
- rapid section setup
- users who want a strong starter shape before customizing

## Full project install

1. Copy `root/` into the project root.
2. Decide which folders are promoted sections.
3. For each promoted section, copy `section-core/` into that folder.
4. Apply the closest matching profile from `profiles/`.
5. Update root `THREAD_MAP.md` with the real sections.
6. Replace placeholders before the first live thread uses the docs.
7. Add an initial `CHANGELOG.md` entry and `SIGN_UP.md` entry where relevant.

## New section install

1. Pick the target folder.
2. Copy `section-core/` into it.
3. Apply the matching profile overlay.
4. Replace placeholders with real lane language.
5. Add the section to root `THREAD_MAP.md`.
6. Check root `CODEX_START.md` if the section startup path should be explicit.

## Placeholder replacement checklist

Replace these first:

- project name
- section name
- section tag
- role sentence
- owns list
- does-not-own list
- upstream sections
- current rule
- current direction
- watchpoints
- forward look
- external runtime path if the section depends on one

## First-use quality check

Before a real thread starts working from the installed docs, check:

- does root clearly own routing and coordination
- does each section clearly own its lane
- does each section have a valid task query tag
- do startup docs point through root first
- do changelog and sign-up notes exist where needed
- are any dangerous runtime paths called out explicitly

## Promotion checklist for a parked folder

A parked folder is ready to promote when:

- it has a clear role
- it has a local doc pack
- it has been added to root `THREAD_MAP.md`
- its ownership boundaries are clearer than before

## Multi-thread use

If you split the work later:

- use `doc_temple/audit/04-parallel-thread-briefs.md` for handoff prompts
- keep one thread on package assembly
- hand shared-core and profile work to separate threads only if the contract is
  already stable
