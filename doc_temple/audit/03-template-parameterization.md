# Template Parameterization Map

Date: 2026-04-16
Status: draft audit, ready for package architecture

## Purpose of this note

This note answers a practical question:

when the package is built, what should stay fixed, what should become a
placeholder, and what should be removed from the reusable version entirely.

## Keep as fixed shared contract

These should stay stable across the package unless we later choose to loosen the
system on purpose.

### Startup and reading discipline

- root-first orientation for meaningful work
- explicit read order in `CODEX_START.md`
- section-level startup after root orientation

### Promoted-section file contract

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

### Task hygiene defaults

- section tag required
- task-type tag required
- priority markers for active and next work
- stable task ids for active and next work
- explicit dependency notation
- recurrence markers only for genuine recurring work
- automatic section task query above manual task sections

### Changelog and handoff discipline

- newest-first changelog entries
- local section changes logged locally
- cross-lane changes reported upward when relevant
- sign-up entry shape with role/scope/read/changed/handoff

## Parameterize

These should become placeholders or profile-driven fragments.

### Identity fields

- project name
- section name
- section slug/tag
- section label used in headers

### Role and boundary fields

- section role sentence
- owns list
- does-not-own list
- depends-on list
- reports-to guidance

### Startup fields

- section-specific read list after root docs
- current rule warning
- destructive-change warning
- external runtime path if any

### Planning fields

- current direction bullets
- watchpoints
- forward-look bullets
- phase names where the lane is phase-driven

### Task fields

- automatic query tag filter
- section-specific task headings such as `Now`, `Active Pool`, `Next`, `Later`
- starter recurring doc-hygiene task ids

### Optional file set

- include/exclude `README.md`
- include/exclude compatibility notes
- include/exclude verification notes
- include/exclude gallery/review helpers

## Remove from reusable templates

These are too historical, local, or implementation-specific to ship as default
template truth.

- dated changelog entries
- live project task pools
- hard-coded task dependencies from existing sections
- current external absolute paths unless explicitly presented as placeholders
- project-specific examples such as XP4Life as default content
- current engine compatibility history
- current business preset/style/mod inventories as universal defaults

## Keep as example material only

These are useful, but should be clearly marked as examples or optional sample
content.

- example changelog entry
- example sign-up entry
- example task block with ids and dependencies
- example root/section relationship text
- example external-runtime warning
- example operator-lane naming rules

## Placeholder fields the package should support

Recommended placeholder set:

- `{project_name}`
- `{root_folder_name}`
- `{section_name}`
- `{section_slug}`
- `{section_tag}`
- `{section_role}`
- `{section_owns}`
- `{section_does_not_own}`
- `{upstream_sections}`
- `{cross_lane_reporting_rule}`
- `{current_rule}`
- `{external_runtime_path_optional}`
- `{task_query_filter}`
- `{watchpoints}`
- `{forward_look}`

If we want stronger profile support, add:

- `{profile_type}`
- `{has_runtime_readme}`
- `{has_external_runtime}`
- `{has_gallery_layer}`
- `{has_verification_notes}`

## Recommended package structure based on this audit

### Option A - simple template pack

- `root/`
- `promoted-section/`
- `examples/`

Good for:

- quick manual copying

Tradeoff:

- lighter, but less expressive for different section types

### Option B - profile-based template pack

- `root/`
- `section-core/`
- `profiles/shared-contract/`
- `profiles/operator-lane/`
- `profiles/external-runtime-coordination/`
- `profiles/setup-tooling/`
- `examples/`
- `install-guide.md`

Good for:

- repeatable setup across multiple section types and future projects

Tradeoff:

- slightly more setup complexity

## Recommended direction

Use Option B.

Why:

- the current VaultForge sections already differ too much for one flat section
  template
- the differences are structured enough to model as profiles
- parked folders suggest more archetypes are likely coming

## Audit result

The package should be built from:

1. one shared contract layer
2. one root coordinator layer
3. multiple section profiles
4. optional example content

That will give the package the best chance of being:

- reusable inside VaultForge
- transferable to other projects
- still opinionated enough to produce consistent operations
