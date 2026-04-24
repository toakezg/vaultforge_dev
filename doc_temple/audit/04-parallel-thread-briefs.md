# Parallel Thread Briefs

Date: 2026-04-16
Status: ready to hand off if we split the work

## How to use this note

If we later choose a multi-thread route, each thread can be given:

- this brief note
- the matching audit note from this folder

That should be enough for a clean scoped start without re-reading everything.

## Thread A - shared core extraction

### Give this thread

- `README.md`
- `01-shared-core-contract.md`
- the original induction note if desired

### Objective

Turn the audited shared contract into a reusable document-core design without
yet building the final package.

### Focus

- confirm the six-file promoted-section minimum
- confirm root-first startup pattern
- confirm task, changelog, and sign-up rules
- propose clean reusable headings per file

### Do not do

- do not invent section-specific behavior
- do not build the package directory yet
- do not pull in historical project detail as default template content

### Deliverable

- one cleaned shared-core specification note
- one proposed heading map per file

## Thread B - section profile and adapter extraction

### Give this thread

- `02-section-deltas.md`
- `03-template-parameterization.md`

### Objective

Convert current section differences into a usable profile model for the future
package.

### Focus

- root coordinator profile
- shared-contract section profile
- operator-lane profile
- external-runtime coordination profile
- setup/tooling profile if justified

### Do not do

- do not flatten root into a normal section
- do not assume the current three promoted sections are the only future shapes
- do not copy live section content as if it were universal

### Deliverable

- one section-profile matrix
- one placeholder/fragment strategy for profile overrides

## Thread C - package assembly

### Give this thread

- `01-shared-core-contract.md`
- `02-section-deltas.md`
- `03-template-parameterization.md`

### Objective

Assemble the first usable drop-in package under `./doc_temple/`.

### Focus

- create package folder structure
- place shared core files
- place profile-specific overrides or examples
- add install/use guidance

### Do not do

- do not rewrite the audit findings
- do not re-open contract questions already settled by the audit
- do not mix sample project history into blank templates

### Deliverable

- first package draft ready for review

## Manual prompt text you can hand to another thread

### Shared core thread prompt

Review the audit files in `./doc_temple/audit/`, especially
`01-shared-core-contract.md`. Extract the reusable shared documentation contract
for promoted sections and root startup behavior. Do not build the package yet.
Return a clean shared-core specification with recommended headings per doc.

### Section profile thread prompt

Review the audit files in `./doc_temple/audit/`, especially
`02-section-deltas.md` and `03-template-parameterization.md`. Turn the current
section differences into a profile model that can drive reusable templates. Do
not build the package yet.

### Package assembly thread prompt

Review the audit files in `./doc_temple/audit/`. Using the approved contract and
profile model, build the first reusable documentation package under
`./doc_temple/` with clean blank templates, profile-aware overrides where
needed, and a short installation guide.
