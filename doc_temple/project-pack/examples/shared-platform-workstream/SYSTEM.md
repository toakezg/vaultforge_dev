# SYSTEM

## Role

This folder is the shared runtime and contract foundation for `Example Project`.

It is an active workstream in the root-and-workstreams model.

## Boundaries

This workstream owns:

- shared contracts
- adapters
- reusable low-level helpers
- compatibility-sensitive foundations

This workstream does not own:

- workflow wrappers
- review surfaces
- setup tooling

Related or dependent workstreams to respect:

- delivery-lane
- creative-runtime
- project-setup

External dependency path, if applicable:

- none by default

## Rules

- keep this workstream focused on shared foundations
- use root startup docs before deep local work
- report shared shape changes upward before downstream confusion spreads
- update local `CHANGELOG.md` for workstream changes
- keep `SIGN_UP.md` usable as a short thread trace
