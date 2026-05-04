# Inspired-Agent Proposals Decision

Date: 2026-05-04

Status: approved for proposal documents and live proposal image generation.

## Decision

Nath approves inspired-agent proposal docs as guidance for future live icon
proposal runs.

`vaultforge-icon/generated/proposals/` is approved as the lane-local destination
for proposal documents, supporting proposal metadata, generated proposal
images, and run metadata.

This approval includes API/paid generation for scoped proposal runs when the
task names the target, output path, approximate count, and prompt source.

This approval does not approve:

- printing secrets
- adding new cloud auth
- final taste decisions
- asset moves/deletes
- folder-icon application
- selected or applied icon outputs

## Use

Inspiration Scout and Coordinator may use inspired-agent proposal docs to shape
aimed icon proposal runs for XP4Life, VaultForge jobs, client use, or personal
use.

Reviewer must keep those proposals bounded: they are direction material, not
current build requirements and not final taste approval.

## First Safe Next Task

Run the first approved inspired-agent icon proposal pass into
`vaultforge-icon/generated/proposals/`, writing proposal Markdown plus a small
set of generated proposal images. Stop before printing secrets, adding new cloud
auth, asset moves/deletes, folder-icon application, selected/applied outputs, or
Nath taste decisions.
