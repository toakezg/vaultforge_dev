# Foundation Pack

Date: 2026-04-16
Status: first package draft

This is the first reusable documentation package built from the VaultForge
audit.

It is designed to help you scaffold either:

- a whole root-plus-sections project
- or a new promoted section inside an existing project

## Package layout

- `root/` - templates for the coordinator layer
- `section-core/` - the six-file promoted-section starter pack
- `profiles/` - overlays that adapt a section to a specific role
- `examples/` - pre-assembled example packs for common section shapes
- `install-guide.md` - step-by-step adoption guidance

## What is fixed in this pack

This pack assumes:

- root coordinates and sections execute
- threads should orient through root first
- promoted sections should use a six-file doc set
- task tags, priorities, ids, and dependencies matter
- changelog and sign-up traces are operating documents, not decoration

## Promoted-section minimum

The base promoted-section pack is:

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

## Root package contents

The root starter set in `root/` includes:

- `README.md`
- `CODEX_START.md`
- `SYSTEM.md`
- `THREAD_MAP.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`

## Profile overlays

Start from `section-core/`, then choose the closest profile in `profiles/`:

- `shared-contract/` for engine-like shared runtime or contract sections
- `operator-lane/` for business-like workflow and delivery sections
- `external-runtime-coordination/` for art-like coordination layers that sit
  above an external runtime
- `setup-tooling/` for init-like setup or tooling sections

## Recommended adoption flow

### To scaffold a full project

1. Copy `root/` into the project root.
2. Copy `section-core/` into each promoted section folder.
3. Apply the right profile overlay to each section.
4. Replace placeholders before the first real thread uses the docs.

### To scaffold one new promoted section

1. Copy `section-core/` into the target folder.
2. Apply the closest profile overlay from `profiles/`.
3. Add the new section to the root `THREAD_MAP.md`.
4. Update root `CODEX_START.md` if section startup rules need to be listed.

## Placeholder fields used in this pack

Replace these before adoption:

- `{project_name}`
- `{section_name}`
- `{section_slug}`
- `{section_tag}`
- `{section_role}`
- `{section_owns}`
- `{section_does_not_own}`
- `{upstream_sections}`
- `{cross_lane_reporting_rule}`
- `{current_rule}`
- `{current_direction}`
- `{external_runtime_path_optional}`
- `{watchpoints}`
- `{forward_look}`

## First-pass intent

This first draft is built to be usable, editable, and clear.

It does not try to encode project history. It gives you:

- a coordinator layer
- a promoted-section starter pack
- profile-driven section adaptation

If you want a later pass, the next sensible upgrade is to add example-filled
copies for specific section types or specific project archetypes.
