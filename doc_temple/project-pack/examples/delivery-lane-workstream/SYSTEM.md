# SYSTEM

## Role

This folder is the workflow, routing, and output lane for `Example Project`.

It is an active workstream in the root-and-workstreams model.

## Boundaries

This workstream owns:

- wrappers
- routing
- review surfaces
- output shaping

This workstream does not own:

- shared low-level contracts
- setup tooling
- external runtime coordination

Related or dependent workstreams to respect:

- platform-core
- creative-runtime
- project-setup

External dependency path, if applicable:

- none by default

## Rules

- keep this workstream focused on workflow and outputs
- use root startup docs before deep local work
- report reusable shared fragments upward once they stabilize
- update local `CHANGELOG.md` for workstream changes
- keep `SIGN_UP.md` usable as a short thread trace
