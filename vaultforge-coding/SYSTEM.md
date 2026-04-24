# System

## Role

This folder is the VaultForge Code section.

It is the local-first coding bridge lane for VaultForge and a promoted section
in the root/section thread model.

## Boundaries

This section owns:

- the VaultForge Code bridge project and local Python package
- preset prompt templates and prompt-loading rules for the bridge
- project-context building for coding runs
- run-folder artifacts such as prompt, response, metadata, usage, and summary
- structured activity event output for downstream systems
- usage and cost reporting that belongs to the bridge itself
- batch launchers and operator-facing bridge entry points

This section does not own:

- unrelated implementation work in other VaultForge sections
- shared image-generation contracts from `vaultforge-engine`
- business/client workflow logic from `vaultforge-business`
- art runtime behavior or prompt experiments from `vaultforge-art`
- direct unsafe file overwrite behavior in the MVP
- XP calculation, quest generation, achievement detection, reward generation,
  rarity/prestige heuristics, or XP/dashboard interpretation

Sibling or upstream sections to respect:

- root coordination docs
- `vaultforge-engine` when a shared API or contract question affects more than
  this bridge
- `vaultforge-business` and `vaultforge-art` only when later integrations are
  explicit
- a future `vaultforge-xp4l` sibling section for deeper meaning and XP logic

## Rules

- keep this section local-first and tool-focused
- keep Windows batch usage first-class
- prefer modular bridge code over a single all-in-one script
- use the official OpenAI Python SDK for the API bridge
- default to read-only generation unless a later approved write mode exists
- save prompts, responses, usage, and summaries for traceability
- keep events factual, append-only, and neutral
- clamp context collection so costs do not run away
- update local `CHANGELOG.md` for section changes and root `CHANGELOG.md` when
  cross-lane coordination or contracts change
- use `SIGN_UP.md` as a compact thread trace
- tag every task with at least one section tag and one task-type tag
- active and next tasks should use stable ids and explicit dependencies when
  the sequencing matters
- keep an automatic `tasks` query above manual task sections

## Naming Note

- folder path: `vaultforge-coding\`
- section identity: `VaultForge Code`
- bridge/project identity: `vaultforge-code`

## Reporting Boundary

- `vaultforge-code` should report what happened
- `vaultforge-xp4l` should decide what it means
