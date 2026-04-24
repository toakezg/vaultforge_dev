# Setup-Tooling Profile

Use this profile when a section mainly owns setup flows, bootstrap tooling,
launchers, installers, environment prep, or project initialization helpers.

Good fits:

- init
- tooling
- bootstrap
- environment setup sections

## Apply these changes to `section-core/`

### `CODEX_START.md`

Make the current rule explicit about:

- protecting bootstrap scripts from casual churn
- documenting environment assumptions clearly
- avoiding hidden setup dependencies

### `SYSTEM.md`

Emphasize:

- setup ownership
- launcher and script boundaries
- environment expectations
- operator safety and repeatability

### `PLAN.md`

Use direction bullets around:

- installation flow quality
- repeatable setup
- dependency clarity
- future simplification or consolidation

### `TASKS.md`

Expect task types such as:

- `#setup`
- `#tooling`
- `#cli`
- `#docs`
- `#validation`

## Optional extra files

Consider adding:

- install guide
- environment note
- troubleshooting note
- quick-start script map
