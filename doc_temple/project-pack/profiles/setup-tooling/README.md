# Setup-Tooling Profile

Use this profile when a workstream owns project bootstrap, local environment
setup, scripts, scaffolding, or tooling conventions.

Good fits:

- project init
- local setup
- tooling wrappers
- scaffold generators

## Apply these changes to `workstream-core/`

### `CODEX_START.md`

Make the current rule explicit about:

- keeping setup rules reproducible
- separating chosen tooling from provisional ideas
- reporting cross-project reuse candidates upward

### `SYSTEM.md`

Emphasize:

- setup ownership
- bootstrap steps
- tooling boundaries
- environment assumptions

State clearly what this workstream owns versus what should remain in root or in
project-specific lanes.

### `PLAN.md`

Use direction bullets around:

- bootstrap simplicity
- setup reliability
- toolchain clarity
- reuse potential

### `TASKS.md`

Expect task types such as:

- `#setup`
- `#tooling`
- `#scripts`
- `#bootstrap`
- `#env`

## Optional extra files

Consider adding:

- a local `README.md`
- environment note
- install checklist
- bootstrap decision log
