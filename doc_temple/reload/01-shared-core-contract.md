# Shared Core Contract Audit

Date: 2026-04-16
Status: draft audit, ready for template extraction

## Purpose of this note

This note identifies the documentation contract that is already shared strongly
enough across VaultForge root and promoted sections to be treated as reusable
template material.

## Source set used

Root sources:

- `CODEX_START.md`
- `README.md`
- `SYSTEM.md`
- `THREAD_MAP.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`

Promoted section sources:

- `vaultforge-art`
- `vaultforge-business`
- `vaultforge-engine`

Reviewed repeated section docs:

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

## Core operating model

### Shared truth 1 - root and sections are intentionally different

The system is not a flat repo.

It is a two-level operating model:

- root acts as coordinator, router, and architecture layer
- promoted sections act as focused worker bases

This distinction is foundational and should be part of the reusable pack.

### Shared truth 2 - threads are expected to boot in a defined order

Every meaningful thread begins with root orientation first.

The current recurring startup pattern is:

1. root `CODEX_START.md`
2. root operating docs
3. root `THREAD_MAP.md`
4. section startup docs if the task belongs to a promoted section

This means the package should preserve startup order, not only file presence.

### Shared truth 3 - docs are operational, not decorative

These files are not passive references. Each one has an active job:

- `CODEX_START.md` boots the thread
- `SYSTEM.md` defines role, boundaries, and rules
- `PLAN.md` holds direction and watchpoints
- `TASKS.md` holds actionable work and task format rules
- `CHANGELOG.md` records meaningful change history
- `SIGN_UP.md` records thread role, scope, and handoff

This file-role clarity is reusable and should be preserved.

## Minimum promoted-section doc pack

The current minimum promoted-section pack is:

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

Observed note:

- `README.md` is useful for stronger runtime/tool sections such as engine
- but it is not currently part of the strict minimum promoted-section set

Template implication:

- the package should treat `README.md` as optional or archetype-driven
- the six-file pack above should be treated as required for promoted sections

## Shared file roles

### `CODEX_START.md`

Current shared role:

- boot note for new threads
- reading order
- section-specific startup warnings
- explicit current rule or current-state constraint

Template-worthy structure:

- opening identity line
- "read these first" sequence
- current rule block
- special warnings for destructive or cross-lane risk

### `SYSTEM.md`

Current shared role:

- define what the folder is for
- define what it does not own
- define operating rules
- define task formatting expectations

Template-worthy structure:

- role
- boundaries
- rules
- ownership and non-ownership lines

### `PLAN.md`

Current shared role:

- capture direction, phases, watchpoints, and forward look
- explain what the section is trying to become
- separate intent from immediate tasks

Template-worthy structure:

- section thread model
- current direction or phase view
- watchpoints
- forward look

### `TASKS.md`

Current shared role:

- expose automatic open-task query
- keep active and next work visible
- hold working rules for task formatting

Template-worthy structure:

- automatic `tasks` query filtered by section tag
- active/now section
- next section
- later or landed section where helpful
- working rules block

### `CHANGELOG.md`

Current shared role:

- keep newest entries first
- record structural or operational changes
- capture section-level changes locally
- capture cross-lane changes at root when needed

Template-worthy structure:

- newest-first date sections
- concise bullet entries
- explicit cross-lane reporting expectation

### `SIGN_UP.md`

Current shared role:

- compact sign-in and handoff trace for threads
- tells future threads who changed what and why

Template-worthy structure:

- reusable entry shape:
  - date/thread label
  - role
  - scope
  - read
  - changed
  - handoff

## Shared operating rules

These rules recur strongly enough to be treated as system-level defaults.

### Ownership and routing

- root coordinates and promoted sections execute
- `THREAD_MAP.md` should be consulted before cross-section edits
- cross-lane effects should be reported upward when relevant

### Documentation hygiene

- each promoted section owns its local changelog and sign-up trail
- root changelog is used for coordination-level or cross-lane changes
- docs are expected to stay current enough to guide future threads

### Task formatting and visibility

- every task line needs at least one section tag
- every task line needs at least one task-type tag
- active and next tasks should carry section-local priority markers
- active and next tasks should carry stable ids
- recurring work should use recurrence markers
- dependency chains should be explicit
- promoted sections should include an automatic `tasks` query above manual task sections

### Style of operation

- note-first
- lightweight
- wrapper-oriented where practical
- avoid duplication when another lane or sibling tool already owns the heavy part

## What is shared enough to template directly

These elements look safe to standardize in a reusable pack:

- root-first startup sequencing
- six-file promoted-section pack
- file-role definitions
- sign-up entry shape
- task tagging rule
- task priority rule
- task id/dependency rule
- auto-query rule for section tasks
- newest-first changelog habit

## What is shared but should stay configurable

These are consistent in pattern, but not in exact wording:

- lane role statement
- ownership boundaries
- cross-lane reporting directions
- current-rule warning in `CODEX_START.md`
- phase names in `PLAN.md`
- exact task section names such as `Now`, `Next`, `Later`, `Landed`

## What should not be templated as fixed truth

These belong to the local section or local project context:

- hard-coded external paths
- historical task ids
- dated changelog content
- section-specific preset/style/mod lists
- local engine or wrapper implementation facts
- active project names such as XP4Life unless included as examples only

## Shared-core extraction result

The current system already supports a reusable shared-core template set.

That set should include:

- a promoted-section starter pack
- a root coordinator starter pack if you want full-project scaffolding
- a rules layer for task hygiene and handoff discipline

The main design challenge is no longer whether a template exists.

It is how cleanly to separate:

- universal operating rules
- VaultForge defaults
- lane-specific adapters
- historical examples
