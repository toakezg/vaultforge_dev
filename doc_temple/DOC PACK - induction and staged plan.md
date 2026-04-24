# Doc Pack - induction and staged plan

Date: 2026-04-16
Status: induction complete, planning only, no package build started yet

## What I have done so far

I started from root `CODEX_START.md` and followed the induction path through:

- root `README.md`
- root `SYSTEM.md`
- root `THREAD_MAP.md`
- root `PLAN.md`
- root `TASKS.md`
- root `CHANGELOG.md`

To understand the shared section pattern, I then reviewed the promoted section docs for:

- `vaultforge-art`
- `vaultforge-business`
- `vaultforge-engine`

Across those sections I reviewed the repeated core docs:

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

I also reviewed `vaultforge-engine/README.md` because engine is the clearest example of a section that already has a stronger runtime and contract identity.

I have not started building the reusable package yet.

## What I understand about how this system operates

### 1. Root versus section model

Root is the overhead coordinator.

It owns:

- cross-lane planning
- architecture decisions
- section promotion and parking
- task routing
- handoffs between sections
- coordination-level changelog truth

Promoted sections are focused worker bases.

Current promoted sections are:

- `vaultforge-engine`
- `vaultforge-business`
- `vaultforge-art`

### 2. Shared doc contract already in use

The real repeated section skeleton is:

- `CODEX_START.md`
- `SYSTEM.md`
- `PLAN.md`
- `TASKS.md`
- `CHANGELOG.md`
- `SIGN_UP.md`

That looks like the current minimum promoted-section operating pack.

`README.md` appears useful when a section has stronger runtime or tool identity, but it is not yet part of the strict repeated section minimum in the same way as the six files above.

### 3. Core operational rules that are already acting like system law

These show up strongly enough that I would treat them as template-grade rules:

- note-first, lightweight workspace style
- root coordinates, sections execute
- `THREAD_MAP.md` decides ownership before cross-section edits
- promoted sections keep their own local docs and own their own changelog/sign-up trace
- tasks require section tag plus task-type tag
- active and next tasks should carry section-local priority markers
- active and next tasks should carry stable task ids
- recurring tasks use recurring markers
- dependencies are expressed explicitly
- section task queries should self-populate with the local tag filter

### 4. Section differences that matter for a future pack

The shared pack cannot just be a blind copy. It needs a common core plus section adapters.

Current section identities are:

- Engine: shared contract base, reusable behavior, tested and lane-neutral
- Business: operator/client lane, wrapper-oriented, output routing, prompt banks, galleries
- Art: coordination base for the art lane, with the actual runtime still living outside this root workspace

So the pack likely needs:

- one shared foundational layer
- one promoted-section starter layer
- one lane-identity layer that can be swapped per section/project

## How I would like to start before full build planning

I want to separate the work into three thinking passes before I write the actual package:

1. extract the shared operating contract
2. isolate what is truly section-specific
3. decide what belongs in a generic reusable pack versus what should stay VaultForge-specific

That gives a cleaner package and reduces the risk of baking current local history into every future section or future project.

## Proposed stages from system learning to package drop

### Stage 1 - source audit

Goal:
identify the exact docs, rules, headings, and repeated structures that already form the live system contract.

Output:

- a shared-core inventory
- a section-specific inventory
- a keep/remove/parameterize decision list

### Stage 2 - template architecture

Goal:
design the package structure inside `doc_temple` before filling it out.

Likely shape:

- shared root/promoted-section foundations
- optional section adapters
- optional project adapter notes
- usage/install note

Output:

- final folder map
- file list
- variable/placeholders strategy

### Stage 3 - shared-core drafting

Goal:
write the transferable versions of the docs that are truly common.

Likely candidates:

- promoted section `CODEX_START.md`
- promoted section `SYSTEM.md`
- promoted section `PLAN.md`
- promoted section `TASKS.md`
- promoted section `CHANGELOG.md`
- promoted section `SIGN_UP.md`

Possibly also:

- root coordinator variants if you want a full root-plus-section starter kit rather than only section kits

### Stage 4 - section adapter drafting

Goal:
create example variants for section types or project lanes.

This would likely include:

- shared-contract base text
- engine-like adapter example
- business-like adapter example
- art-like adapter example
- guidance for creating new promoted sections from parked folders

### Stage 5 - package assembly

Goal:
assemble the package in `doc_temple` in a form that is easy to drop into another section or project.

This stage should produce:

- ready-to-copy templates
- example filled versions where helpful
- a short setup guide explaining what to rename, what to keep, and what to customize first

### Stage 6 - review and hardening

Goal:
check that the package is actually usable and not just tidy.

Review points:

- does a new section know what to read first
- does a new thread know where to sign in
- do task rules stay consistent
- do handoffs and changelogs stay visible
- is the split between shared and lane-specific content clear

## Information from you that would help

I can proceed without these right away, but these would sharpen the pack:

- whether this pack is primarily for new VaultForge sections, for outside projects, or both equally
- whether you want the pack to include root-level coordinator docs as well as section docs
- whether you want blank templates only, or blank templates plus example-filled versions
- which parked folders are most likely to be promoted next:
  - `vaultforge-core`
  - `vaultforge-design`
  - `vaultforge-system`
  - `vaultforge-coding`
  - `vaultforge-init`
- whether Obsidian-specific behavior should stay built in, or be optionalized where possible
- how opinionated you want the package to be:
  - strict and prescriptive
  - balanced
  - lighter and more adaptable

## Would multiple threads help

Yes, but only after the shared-contract audit is locked enough to avoid duplicate interpretation drift.

The clean split would be:

### Thread A - shared core extraction

Focus:
root plus promoted-section common contract only

Best use:
identify what is genuinely reusable across all sections

### Thread B - section delta extraction

Focus:
engine/business/art differences only

Best use:
separate lane-specific rules from the common pack

### Thread C - package assembly

Focus:
build the final `doc_temple` package structure and usage notes

Best use:
turn the audited contract into a clean drop-in kit

If you want to stay single-threaded, that is completely workable too. It will just be a bit more sequential.

## If you want to prepare things for me in parallel

The most useful preparation would be:

- flag which parked section is the most realistic next promotion target
- point out any docs you consider non-negotiable source-of-truth docs beyond what I already reviewed
- tell me whether the package should feel more VaultForge-native or more general-purpose

## Prompts you could use later if you want parallel help

### For a shared-core audit thread

"Audit root and promoted section docs and extract only the shared operational contract. Do not implement anything yet. Separate repeated rules, repeated file roles, and repeated startup behavior."

### For a section-delta thread

"Compare engine, business, and art docs against the shared contract and list only the lane-specific differences, constraints, and adapter needs."

### For a package-assembly thread

"Using the approved shared contract and lane deltas, assemble the first reusable documentation package in `./doc_temple` with templates, adapters, and a short usage guide."

## My preferred next move

Next I would like to do a deliberate audit pass that converts the current doc set into:

- shared core
- lane-specific adapters
- VaultForge-only context
- reusable-for-other-projects context

That gives us a strong base before the package writing starts.

Once you want me to proceed, I can move from this setup note into the first true extraction pass.
