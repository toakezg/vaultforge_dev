# SYSTEM

## Role

This folder is the bootstrap and tooling lane for `Example Project`.

It is an active workstream in the root-and-workstreams model.

## Boundaries

This workstream owns:

- setup guidance
- local environment rules
- scaffold helpers
- tooling conventions

This workstream does not own:

- delivery behavior
- shared runtime contracts
- external runtime coordination

Related or dependent workstreams to respect:

- platform-core
- delivery-lane
- creative-runtime

External dependency path, if applicable:

- none by default

## Rules

- keep this workstream focused on setup and tooling guidance
- use root startup docs before deep local work
- report reusable cross-project setup ideas upward when they stabilize
- update local `CHANGELOG.md` for workstream changes
- keep `SIGN_UP.md` usable as a short thread trace
