# Apply Icon Apply-Plan Contract

Status: docs-only contract. Approved apply-plan format drafted; do not build
`apply_icon.py` yet.

## Purpose

`$apply-icon` is a future icon-lane workflow for placing already-selected icons
onto approved target folders.

The first useful version should make the proposed placement reviewable before
anything changes on disk. It should not generate images, call APIs, move or
delete assets, apply folder icons, or decide which visual direction wins.

## Scope

This contract defines the apply-plan format only. It does not create
`apply_icon.py`, create `run_apply_icon.bat`, create generated outputs, create
output folders, generate images, call APIs, move/delete assets, or apply folder
icons.

## Coordinator Brief

- Target: define the reviewable apply-plan shape needed before `$apply-icon`
  implementation.
- Budget: one Coordinator -> Builder -> Reviewer -> Recorder rotation.
- Success check: a future dry-run can show exact planned folder-icon changes
  from a stable plan without implying anything was applied.
- Stop condition: stop before scripts, folder-icon application, asset writes,
  asset moves/deletes, generated outputs, API calls, image generation, or taste
  decisions.

## Current Safe Shape

For now, `$apply-icon` means a manual contract-guided planning workflow:

1. Read the selected icon source and target folder context.
2. Draft one apply-plan entry per target.
3. Mark every entry as `draft`, `reviewed`, or `approved`.
4. Record expected dry-run output and rollback notes.
5. Stop before any filesystem or folder-icon change.

## Approved Plan Location

Future planned apply-plan text may use:

- Markdown review plan: `vaultforge-icon/generated/apply-plans/`
- Optional machine-readable plan: `vaultforge-icon/generated/apply-plans/`

These paths are preview defaults only. The folders remain parked and uncreated
until a later approved write task explicitly allows generated artifacts.

## Required Plan Fields

Each apply-plan must include:

- `plan_id`
- `created_at`
- `created_by`
- `scope`
- `status`, one of `draft`, `reviewed`, or `approved`
- `targets`
- `no_write_preview`
- `approval_note`
- `stop_gates`

Each target entry must include:

- `target_path`
- `target_kind`, such as `folder`, `lane`, `client`, or `task`
- `icon_source`
- `icon_source_status`, such as `selected`, `reviewed`, or `approved`
- `intended_use`, such as `folder_icon`, `lane_identity`, or `client_pack`
- `planned_action`
- `expected_existing_icon_state`, such as `unknown`, `none`, or `has_icon`
- `backup_or_rollback_note`
- `apply_status`, one of `draft`, `reviewed`, `approved`, or `blocked`
- `blockers`

## Markdown Plan Template

```text
# Icon Apply Plan - <plan_id>

Status: draft
No-write preview: true

## Scope

- Plan id:
- Created at:
- Created by:
- Purpose:
- Approval note:

## Targets

### <target label>

- Target path:
- Target kind:
- Icon source:
- Icon source status:
- Intended use:
- Planned action:
- Expected existing icon state:
- Backup or rollback note:
- Apply status:
- Blockers:

## Dry-Run Preview

- Would inspect:
- Would change:
- Would create files:
- Would move/delete assets:
- Would apply folder icons:

## Stop Gates

- Stop before applying any folder icon.
- Stop if target path or icon source is ambiguous.
- Stop if an existing icon would be overwritten without explicit approval.
- Stop if the action needs live generation, API calls, cloud auth, or paid work.
- Stop if choosing between visual directions requires Nath's taste decision.
```

## JSON Shape Preview

```json
{
  "plan_id": "apply-plan-example",
  "created_at": "YYYY-MM-DD",
  "created_by": "manual-docs-contract",
  "scope": "folder-icon application preview",
  "status": "draft",
  "no_write_preview": true,
  "approval_note": "Not approved for apply. Review only.",
  "targets": [
    {
      "target_path": "vaultforge-icon/svg-forge",
      "target_kind": "folder",
      "icon_source": "path/to/selected-icon.ico",
      "icon_source_status": "selected",
      "intended_use": "folder_icon",
      "planned_action": "set folder icon",
      "expected_existing_icon_state": "unknown",
      "backup_or_rollback_note": "Record existing desktop.ini/icon state before any apply task.",
      "apply_status": "draft",
      "blockers": ["No apply task approved"]
    }
  ],
  "stop_gates": [
    "folder icon application",
    "asset move/delete",
    "ambiguous target or icon source",
    "overwrite without explicit approval",
    "live generation or API call",
    "taste decision"
  ]
}
```

## Dry-Run Transcript Requirements

A future `$apply-icon --dry-run` transcript must show:

- source plan path
- plan status
- target count
- target paths
- icon source paths
- planned actions
- current no-write mode
- created files count
- moved/deleted assets count
- applied folder icons count
- blocked entries and blocker reasons

For the current contract, every dry-run preview must report:

```text
created_files: 0
moved_or_deleted_assets: 0
applied_folder_icons: 0
```

## Pass Criteria

An apply-plan passes this contract when:

- every target has a path, icon source, planned action, and approval state
- `no_write_preview` is true for planning and dry-run modes
- approved entries are distinguishable from draft or blocked entries
- overwrite, rollback, and ambiguity notes are visible before apply
- the plan does not require scripts, generated outputs, asset operations, API
  calls, image generation, or folder-icon application to review

## Fail Criteria

An apply-plan fails this contract if it:

- treats `$apply-icon` as a live runnable command today
- creates `apply_icon.py` or a launcher
- creates `vaultforge-icon/generated/`
- applies a folder icon
- moves, deletes, renames, or overwrites assets
- generates images or calls an API
- hides approval state per target
- omits overwrite or rollback notes
- chooses a visual direction without Nath approval

## Activation Conditions

Keep `apply_icon.py` parked until all of these are true:

- selected icon sources exist and are approved for the target use
- at least one manual apply-plan has been reviewed without major shape changes
- dry-run transcript requirements are accepted
- generated apply-plan output paths are explicitly approved for writes
- folder-icon application behavior and rollback expectations are approved
- Nath approves moving from contract to script

## Reviewer Notes

- Scope stayed docs-only.
- The approved format is for review and dry-run planning, not live application.
- No apply-plan artifacts or generated folders were created.
- `$apply-icon`, `apply_icon.py`, and `run_apply_icon.bat` remain parked.

## Recorder Handoff

The next safe work should not implement `$apply-icon` yet. A later docs-only
review can test this contract against one manual apply-plan, or Nath can choose
the next approved icon-lane task. Folder-icon application remains a hard stop.
