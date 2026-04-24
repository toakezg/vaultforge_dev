# External-Runtime Profile

Use this profile when a workstream coordinates assets, outputs, or behavior that
depends on a tool, engine, runtime, or system that lives outside the current
project folder.

Good fits:

- creative pipelines
- export lanes
- engine integration layers
- coordination around a separate runtime

## Apply these changes to `workstream-core/`

### `CODEX_START.md`

Make the current rule explicit about:

- respecting the external runtime boundary
- documenting assumptions before changing bridge behavior
- recording dependency-sensitive changes carefully

### `SYSTEM.md`

Emphasize:

- the external dependency path
- what is coordinated here versus what lives outside the repo
- asset or output ownership
- bridge boundaries

### `PLAN.md`

Use direction bullets around:

- dependency clarity
- integration safety
- external version sensitivity
- output stability

### `TASKS.md`

Expect task types such as:

- `#integration`
- `#assets`
- `#exports`
- `#bridge`
- `#runtime`

## Optional extra files

Consider adding:

- a local `README.md`
- dependency note
- export note
- verification note
