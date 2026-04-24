# Shared-Contract Profile

Use this profile when a section owns reusable shared behavior or cross-lane
contracts.

Good fits:

- engine
- core
- system
- API or contract-heavy sections

## Apply these changes to `section-core/`

### `CODEX_START.md`

Make the current rule explicit about preserving compatibility, protecting
upstream runtimes if needed, and avoiding destructive migration moves.

### `SYSTEM.md`

Emphasize:

- reusable shared behavior
- lane-neutral boundaries
- tests, compatibility, and verification

State clearly that lane-specific workflow logic should stay outside this
section until it proves reusable.

### `PLAN.md`

Use phases that suit a contract section:

- boundary skeleton
- compatibility
- feature growth
- verification

### `TASKS.md`

Expect task types such as:

- `#tests`
- `#compatibility`
- `#api`
- `#metadata`
- `#validation`

## Optional extra file

Add a local `README.md` when the section has a stronger runtime or tool
identity and needs a short orientation note beyond the six core files.
