# ADOPT THIS PACK

This note is for the first thread that picks up a repository after
`project-pack` has been dropped into it.

Your job is to adopt this pack into the real project.
Do not preserve it literally if the repository needs a different shape.

## Core intent

- audit the repository as it exists today
- work out how the project actually operates
- turn this starter pack into a project-tailored docs home
- prefer truthful structure over template purity

For most repositories, the final docs home should become `./docs/`.
If the project already has an established docs location, use that instead.

## Read first

Before making substantial doc changes, read:

1. `README.md`
2. `operating-model.md`
3. `install-guide.md`
4. the `root/` templates
5. the `workstream-core/` templates
6. the most relevant profile in `profiles/`
7. the closest example in `examples/`, if useful

Then audit the actual repository:

- existing docs
- top-level folders
- apps, packages, or major modules
- scripts and tooling markers
- active work areas
- shared or ambiguous ownership zones

## Adoption phases

### Phase 1 - audit and shape

- summarize the project structure
- decide whether the repo should use root-only docs or root plus active
  workstreams
- scale the doc structure to the actual size and maturity of the repository
- identify missing information, risks, and unclear ownership
- suggest additional threads only if they would materially help, with exact
  scopes

### Phase 2 - morph the pack

- create or update the real project docs home, usually `./docs/`
- turn the pack templates into project-specific docs
- replace placeholders with truthful local wording
- point routing docs at the real folders in the repo
- create only the workstream docs justified by stable ownership and recurring
  work
- keep command, runtime, and tooling details out unless they are already real in
  the project

### Phase 3 - handoff

- explain the adopted docs structure
- record what was created or reshaped
- note what should be refined later as the project becomes clearer

## Rules

- document reality first, improvement second
- do not assume this repo uses VaultForge naming or structure
- do not force multiple workstreams if the repo is still small
- do not invent old changelog history
- do not hard-code CLI commands or runtime steps unless they already exist in
  the repo
- if a workstream should exist, create it and explain why
- if planning should come before implementation, write the plan first, then
  continue unless blocked

## Good default destination

If the repo has no strong existing docs home, use:

- `./docs/README.md`
- `./docs/CODEX_START.md`
- `./docs/SYSTEM.md`
- `./docs/THREAD_MAP.md`
- `./docs/PLAN.md`
- `./docs/TASKS.md`
- `./docs/CHANGELOG.md`
- `./docs/workstreams/<slug>/...`

If the repo already has a better-established documentation location, adapt to
that instead of forcing `./docs/`.

## Suggested opening response style

After reading the pack and the repo, briefly report:

- the project shape you found
- the doc shape you plan to adopt
- whether root-only docs are enough or whether workstreams are justified
- any risks or missing information
- whether extra threads would actually help

Then continue with the adoption unless something is genuinely blocked.
