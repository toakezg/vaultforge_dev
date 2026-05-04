# Directory Scout Proposal Intake Checklist

Status: approved checklist. No directory scan is performed by this document.

## Purpose

Give Directory Scout a stable way to inspect a scoped target folder and turn the
findings into proposal-ready icon descriptions under:

```text
vaultforge-icon/generated/proposals/inbox/
```

Use this when Nath asks for an icon set for a folder, project, launcher, media
library, client folder, or grouped set of files.

## Preflight

Before scouting, record:

- target path
- whether subfolders are in scope
- maximum scan depth
- whether file contents may be read or only filenames/extensions
- intended output inbox filename
- whether the scout should include folder icons, filetype icons, app launcher
  icons, or a mix

Stop and ask Nath before proceeding if the target path is private, broad,
unclear, outside the stated scope, or would require reading file contents that
were not explicitly approved.

## Compatibility Reference

Use `documents/reference/compatable_file-types.md` to classify targets as:

- high-value document/data formats
- image files
- audio files
- video files
- archive/package files
- code/config files
- app, shortcut, and system-adjacent files
- folder-level targets

The reference supports proposal planning only. It does not approve registry
edits, launcher changes, folder-icon application, target-project writes, or
icon-cache operations.

## Scout Output Shape

Write one Markdown proposal file into the inbox with:

```md
# <Name> Icon Set Proposal

Target: `<path>`

## Scope

- Scan depth:
- Contents read:
- Output intent:
- Apply status: proposal only

## Style Input

- Source style:
- Set mode: unified | semi-unique | unique

## Targets

### <Target Name>

- Path:
- Type: folder | filetype | launcher | shortcut | mixed
- Compatible icon route:
- Description:
- Visual direction:
- Constraints:

## Gates

- No selected winners.
- No target writes.
- No asset moves/deletes.
- No folder or file icon application.
```

## Description Rules

For each target, include:

- what the folder/file/app is for
- the user-facing concept the icon should communicate
- recognizable objects or symbols
- color semantics if they are already approved or proposal-local
- small-size risks, such as tiny text, dense lines, or symbols that may blur
- whether the output should become a PNG source, SVG source, `.ico`, or later
  apply-plan candidate

## Review Checklist

Before handing the proposal to Builder, Reviewer checks:

- the target path and scan depth are explicit
- no unrelated/private folders were included
- file contents were not read beyond scope
- each target has a compatible route or a clear limitation
- style notes are marked as active, reference-only, or proposal-local
- folder-icon application is explicitly parked
- any taste decision is left for Nath

## Follow-Up

If the scout finds a valid set, Builder may create a named run folder under:

```text
vaultforge-icon/generated/proposals/<run-id>/
```

and continue with `run_icon_proposal.ps1` or a later approved set runner. If the
target needs real application, create a separate apply-plan task after selected
source icons exist.
