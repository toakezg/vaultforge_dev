# Make Icon Output Path Review

Status: docs-only review. Planned text output paths accepted for preview shape
only; output folders remain uncreated.

## Scope

Review the planned `$make-icon` output path assumptions from
`documents/contracts/MAKE_ICON_INTERFACE_PLAN.md` and `documents/contracts/MAKE_ICON_DRY_RUN_TRANSCRIPT_CHECK.md`.

This review does not create `vaultforge-icon/generated/`, create briefs or
metadata artifacts, create scripts, generate images, call APIs, move/delete
assets, or apply folder icons.

## Coordinator Brief

- Target: decide whether `vaultforge-icon/generated/briefs/` and
  `vaultforge-icon/generated/metadata/` should stay, change, or remain parked.
- Budget: one Coordinator -> Builder -> Reviewer -> Recorder rotation.
- Success check: future `$make-icon` planning can show stable planned paths
  without implying folders or artifacts already exist.
- Stop condition: stop before filesystem creation, generated artifacts, API
  calls, scripts, live generation, asset operations, or folder icon application.

## Reviewed Sources

- `documents/contracts/MAKE_ICON_INTERFACE_PLAN.md`
- `documents/reviews/MAKE_ICON_INTERFACE_REVIEW.md`
- `documents/contracts/MAKE_ICON_DRY_RUN_TRANSCRIPT_CHECK.md`
- `documents/contracts/MAKE_ICON_CONTRACT.md`
- `TASKS.md`, `PLAN.md`, `SYSTEM.md`, `CHANGELOG.md`, and `SIGN_UP.md`

## Decision

Keep these planned text-output paths:

- planned briefs: `vaultforge-icon/generated/briefs/`
- planned metadata: `vaultforge-icon/generated/metadata/`

They stay because they are clear, lane-local, and separate reviewable text
planning artifacts from source docs, notes, scripts, and final assets.

They also remain parked. In current docs, these paths are defaults for no-write
preview output only. The folder tree must not be created until a later approved
implementation or artifact-writing task explicitly allows writes.

## Why Not Change Them Now

- `vaultforge-icon/NOTE/` already holds human-authored notes and manual briefs;
  generated brief drafts should not be mixed into that source-note area.
- `svg-forge/` and other subtool folders should not become the default storage
  location for cross-target `$make-icon` planning output.
- Root `ICON/` already carries XP4Life prompt banks and generated image output;
  future `$make-icon` planning artifacts should stay inside the icon lane until
  a packaging or client task routes them elsewhere.
- `vaultforge-engine` owns shared generation behavior, not icon-lane planning
  artifacts.

## Parked Items

Keep these unresolved until separate approved tasks:

- image output folders
- selected or applied icon folders
- `$apply-icon` apply-plan paths
- final metadata schema locking
- real invocation form for `$make-icon`
- `make_icon.py` and any launcher script

## Dry-Run Transcript Implication

Future no-write transcripts may show the default planned root as:

```text
output_root: vaultforge-icon/generated
```

But they must still report:

```text
created_files: 0
created_folders: 0
```

Any transcript that implies the folders already exist, were created, or contain
generated artifacts fails the current no-write contract.

## Reviewer Notes

- Scope stayed docs-only.
- The planned `generated/` paths do not currently exist in the workspace.
- Accepting the path names for preview does not approve implementation.
- `make_icon.py` remains parked behind the existing contract and Nath approval
  gates.

## Recorder Handoff

The next safe docs-only tool task is the approved `$apply-icon` apply-plan
contract. It should define an apply-plan format only and must not implement
`apply_icon.py`, apply folder icons, move/delete assets, or create generated
outputs.
