# START HERE

Use this note when you are about to drop `project-pack` into a new or existing
repository and want the easiest path to first adoption.

## What this pack is

`project-pack` is starter scaffolding for project docs.

It is not meant to stay frozen in place.
Its job is to be read, audited against the real repo, and then reshaped into
the project's actual documentation home.

For most repositories, that final home should become `./docs/`.

## Best default workflow

1. Copy the whole `project-pack` folder into the target repo.
2. Start a thread in that repo.
3. Direct the thread to read `ADOPT_THIS_PACK.md`.
4. Let the thread audit the repo before it rewrites the docs.
5. Let the thread morph the pack into project-specific docs.

## What the thread should usually do

The first thread should:

- read the pack
- audit the real repo shape
- decide whether the project needs root-only docs or root plus workstreams
- create a project-tailored docs home, usually `./docs/`
- replace placeholders with truthful language
- avoid inventing commands, tooling, or fake history

## Recommended final shape

For a medium or large project, a good default shape is:

- `./docs/README.md`
- `./docs/CODEX_START.md`
- `./docs/SYSTEM.md`
- `./docs/THREAD_MAP.md`
- `./docs/PLAN.md`
- `./docs/TASKS.md`
- `./docs/CHANGELOG.md`
- `./docs/workstreams/<slug>/...`

For a small project, root-only docs may be enough at first.

## What to tell the thread

Use one of these:

### Short version

```text
Read `ADOPT_THIS_PACK.md` and carry out the adoption flow for this repository.
```

### Strong default version

```text
A general `project-pack` has been dropped into this repository as starter
material. Read `ADOPT_THIS_PACK.md` and adopt it into this project. Audit the
repo first, then morph the pack into a project-tailored docs home, usually
`./docs/`, based on how the repository actually operates.
```

## When to slow down

Pause and plan before heavy doc creation if:

- the repo already has substantial docs
- folder ownership is unclear
- there are multiple unrelated apps or packages
- the project is large enough that parallel thread suggestions may help

In those cases, the thread should write an adoption plan first, then continue.
