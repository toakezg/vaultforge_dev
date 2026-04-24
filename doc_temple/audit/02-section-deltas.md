# Section Delta Audit

Date: 2026-04-16
Status: draft audit, ready for adapter design

## Purpose of this note

This note captures what is not shared.

These deltas are the reason the future package should use adapters or section
profiles instead of one single blind template.

## Current section archetypes

The current promoted sections already suggest four useful archetypes:

1. root coordinator
2. shared-contract runtime section
3. operator workflow lane
4. coordination base with an external runtime dependency

Those map cleanly to the current folders:

- root = coordinator
- engine = shared-contract runtime section
- business = operator workflow lane
- art = coordination base with external runtime dependency

## Root coordinator delta

### What makes root different

Root does not behave like a normal section.

It owns:

- thread routing
- architecture decisions
- section promotion and parking
- cross-lane planning
- coordination-level changelog truth

### Root-only files or concepts

- `THREAD_MAP.md` is a root-level operating document
- root also carries the broad workspace `README.md`
- root tasks can include system-wide oversight items rather than only local work

### Adapter implication

If the package is meant to scaffold a full project and not just promoted
sections, root needs its own template family.

Root should not be treated as merely "another section."

## Engine delta - shared-contract runtime section

### What makes engine distinct

Engine is the most complete example of a section that owns shared behavior and
runtime contract.

It is characterized by:

- lane-neutral positioning
- shared contract language
- verification and compatibility emphasis
- optional runtime-oriented `README.md`
- stronger relationship to implementation and tests

### Engine-specific patterns worth preserving as an adapter

- "boring, reusable, tested, and lane-neutral" identity
- explicit ownership of shared primitives
- explicit non-ownership of lane-specific workflows
- compatibility and verification language in plan/tasks/changelog

### Adapter implication

The package should include a "shared-contract section" adapter.

This adapter is likely useful beyond engine specifically. Future `core` or
`system` sections may need a similar pattern.

## Business delta - operator workflow lane

### What makes business distinct

Business is not the engine and not only coordination.

It owns workflow surfaces and operator-facing organization:

- wrappers
- prompt banks
- output routing
- review surfaces
- galleries
- delivery-oriented metadata

### Business-specific patterns worth preserving as an adapter

- wrapper-first stance
- clear separation from engine ownership
- output-routing and metadata emphasis
- lane-owned presets/styles/mods until proven shared
- operator-facing naming rules

### Adapter implication

The package should include an "operator lane" adapter.

This adapter would likely be useful for future sections such as:

- design
- coding
- client packs
- print/social/output lanes

## Art delta - coordination base with external runtime dependency

### What makes art distinct

Art is a promoted section, but it is intentionally not the runtime owner yet.

Its current shape includes:

- coordination-base identity
- explicit warning not to treat itself as a migrated runtime
- hard boundary around an external sibling runtime path
- focus on prompts, experiments, curation, and bridge expectations

### Art-specific patterns worth preserving as an adapter

- strong "do not migrate/rewrite external runtime" warning
- external runtime path as a first-class configuration item
- bridge-to-shared-core expectation
- careful distinction between experiments and reusable shared behavior

### Adapter implication

The package should include an "external-runtime coordination" adapter.

This is an important edge-case template because many projects grow sections
before they actually migrate the runtime underneath them.

## Parked-section signals

The parked folders currently do not contain promoted-section doc sets.

What they do show:

- `vaultforge-core`
- `vaultforge-design`
- `vaultforge-system`
- `vaultforge-coding`

currently look like placeholder MOC/index folders

and:

- `vaultforge-init`

already behaves more like a tool-bearing lane or setup/runtime helper folder

### Adapter implication from parked folders

Likely future adapter candidates:

- `core` = shared-contract section or architecture section
- `system` = shared-contract section or coordinator-adjacent section
- `design` = operator lane or review/asset lane
- `coding` = operator lane or delivery lane
- `init` = setup/tooling lane with stronger runtime/docs needs

This suggests the package should not stop at only three example section types.

## Delta categories the package should support

Instead of thinking only in named sections, the package should support these
changeable categories:

### Role sentence

Examples:

- coordinator
- shared-contract base
- operator lane
- coordination base
- setup/tooling lane

### Ownership boundaries

Each section needs editable:

- owns
- does not own
- reports to
- depends on

### Runtime relationship

A section may be:

- runtime owner
- wrapper around shared runtime
- coordination layer over external runtime
- non-runtime documentation lane

### Extra files

Some sections may need:

- `README.md`
- compatibility notes
- verification notes
- dashboard or gallery notes
- local quick-start docs

### Warning mode

Some sections need stronger startup warnings than others:

- do not move sibling runtime
- keep backwards compatibility
- do not mix lane ownership
- do not duplicate shared logic locally

## Adapter design result

The reusable package should support at least these profiles:

- root coordinator
- promoted shared-contract section
- promoted operator lane
- promoted coordination base over external runtime
- promoted setup/tooling lane

If we do not support profile-based variation, the package will either be too
generic to be useful or too VaultForge-specific to transfer cleanly.
