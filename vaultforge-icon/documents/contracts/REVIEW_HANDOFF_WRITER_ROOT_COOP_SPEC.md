# Review Handoff Writer Root-Cooperative Spec

Status: checklist/spec only. This is not a real Codex skill, script, or
automation file.

## Purpose

Define the manual shape for a future `$review-handoff-writer` that helps icon
lane work record review-ready handoffs in both icon-local docs and root
coordination surfaces when the change affects VaultForge-level state.

The first version should keep the human in charge. It should prepare a concise
handoff/checklist and make missing evidence obvious; it should not decide taste,
apply icons, move assets, call APIs, or rewrite root routing on its own.

## Intended Inputs

- target task id
- role being recorded, such as Builder, Reviewer, or Recorder
- files touched
- verification command, working directory, exit code, and result
- blocker or decision status
- hard-gate, soft-gate, or live-required classification
- resume prompt
- whether root docs need a coordination note

## Icon-Local Outputs

The checklist should help update these icon-lane surfaces when relevant:

- `SIGN_UP.md` current `Multi-Agent Handoff`
- a dated `SIGN_UP.md` entry
- `TASKS.md` task status, new follow-up task, or gate tag
- `CHANGELOG.md` newest-first bullet
- task-specific decision, review, or contract docs under `documents/`

## Root-Cooperative Outputs

Root updates are only appropriate when the icon change affects routing,
workflow behavior, cross-lane ownership, or Workflow B run records.

Allowed root-facing output shape:

- short status summary for root recorder use
- run id or task id
- lane and role
- files touched inside the icon lane
- verification evidence
- unresolved gate and exact resume prompt

The checklist should not edit root docs automatically unless a scoped task
explicitly grants that write scope. For normal icon-lane builder work, it should
produce text that a root recorder can copy into root `CHANGELOG.md`,
`WORKFLOW_REVIEW.md`, or a run packet handoff.

## Checklist

Use this order when recording an icon-to-root handoff:

1. Name the selected task id and current role.
2. State the write scope and confirm every changed file stayed inside it.
3. List files touched, grouped by icon local docs, generated proposal outputs,
   subtool files, and root-facing text if any.
4. Record verification with exact command, working directory, exit code, and
   inspected evidence.
5. Classify blockers as hard gate, soft gate, live-required, or no gate.
6. State forbidden actions that were not taken when relevant: API/paid work,
   secret printing, selected/applied outputs, asset moves/deletes, folder-icon
   application, ownership changes, and taste decisions.
7. Write a resume prompt that starts from the current task board and names the
   next safe action.
8. Decide whether root needs a coordination note or whether icon-local records
   are enough.

## Hard Gates

Stop and record a decision note instead of writing broader changes when the
handoff reveals any of these:

- root/section ownership change
- new shared workflow rule
- secret or cloud-auth permission
- paid/API generation that is not already scoped and approved
- selected/applied outputs
- asset movement or deletion
- folder-icon application
- final visual taste decision

## Non-Goals

This spec does not create:

- a real Codex skill
- a script
- generated proposal images
- selected or applied icon outputs
- root doc edits without explicit root write scope
- automation that stages or commits files

## Acceptance Check

A future review may accept this spec if it can support one icon builder or
reviewer handoff without missing:

- task id
- role
- files touched
- verification evidence
- gate classification
- root-note need
- exact resume prompt

If those fields remain stable across another root-cooperative run, a later
approved task may decide whether to turn this checklist into an actual skill.
