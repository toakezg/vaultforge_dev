# Operator-Lane Profile

Use this profile when a section is a workflow lane for operators, clients,
review surfaces, prompt banks, outputs, or delivery helpers.

Good fits:

- business
- design
- coding
- output or review sections

## Apply these changes to `section-core/`

### `CODEX_START.md`

Make the current rule explicit about:

- keeping the lane thin and wrapper-oriented where practical
- not duplicating shared engine or contract logic locally
- reporting shared needs upward when they stabilize

### `SYSTEM.md`

Emphasize:

- wrappers
- prompt banks
- output routing
- review or delivery surfaces
- operator-facing naming rules if needed

State clearly what stays lane-owned versus what should move into shared
contracts later.

### `PLAN.md`

Use direction bullets around:

- lane ownership
- wrapper stability
- routing and metadata
- future migration of stable fragments into shared sections

### `TASKS.md`

Expect task types such as:

- `#prompts`
- `#gallery`
- `#routing`
- `#review`
- `#clients`

## Optional extra files

Consider adding:

- a local `README.md`
- naming-rules note
- quick-run guide
- gallery or dashboard note
