# HARD_GATES

Purpose: Pre-decide future Workflow B hard gates with explicit 0/1 fields.

Interpretation:
- 1 = approved exactly as scoped.
- 0 = blocked.
- blank = unresolved and must be treated as not approved.

Last reviewed: 2026-05-10
Generated from: root docs, Workflow B docs, and listed lane docs

## Active Gates

### HG-001 - Workflow B Executable Long Run Controls
decision_0_or_1:  1
lane_scope: root
gate_type: other
trigger_condition: When Workflow B is about to run executable agents with broad cycle budgets, `--parallel`, `--bypass-sandbox`, non-default commit behavior, or changed hard-gate behavior beyond a plan-only packet.
why_hard_gate: Root controls cross-lane execution, write scopes, commit policy, budget/timebox behavior, and whether agents may continue after gates; a mistaken setting can affect multiple lanes at once.
decision_1_allows: One Workflow B run using the exact listed lanes, cycle/time/budget limits, execution flags, commit mode, and hard-gate mode recorded in the launch brief.
decision_0_blocks: Executable Workflow B launch outside plan/dry-run mode until Nath approves the exact run controls.
default_if_blank: stop/report before acting
source_files: MULTI_AGENT_WORKFLOW_B.md; WORKFLOW_REVIEW.md; TASKS.md; NATH_START.md
notes:

### HG-002 - Engine Contact Sheet Renderer Evidence
decision_0_or_1: 
lane_scope: vaultforge-engine
gate_type: live-generation
trigger_condition: When Workflow B reaches `engine-contact-sheet-renderer` and needs real sidecar examples, generated art, or an approved fixture strategy before implementing the renderer.
why_hard_gate: The renderer is explicitly parked as `#live-required`; building it against empty or synthetic evidence would harden an output contract without real generated examples.
decision_1_allows: The exact approved path for renderer evidence: either one named live/evidence capture with output path and budget, or one root-approved fixture strategy scoped to the renderer implementation.
decision_0_blocks: Contact-sheet renderer implementation and any live/generated evidence capture for that renderer.
default_if_blank: stop/report before acting #live-required
source_files: vaultforge-engine/TASKS.md; vaultforge-engine/SIGN_UP.md; vaultforge-engine/RUN_MANIFEST.md; CHANGELOG.md
notes:

### HG-003 - Business Fragment Registry Migration
decision_0_or_1: 
lane_scope: vaultforge-business, vaultforge-engine
gate_type: cross-lane-ownership
trigger_condition: When stable business preset/style/mod fragments are ready to move from business-owned candidate review into shared engine registries or shared lane aliases.
why_hard_gate: Moving business fragments into engine libraries changes shared registry ownership, production constraints, alias behavior, and future art/business coupling.
decision_1_allows: Moving only the reviewed business fragments named in the migration brief into the approved engine registry shape, with business compatibility checks preserved.
decision_0_blocks: Any migration of business preset/style/mod fragments into engine-owned registries or shared aliases.
default_if_blank: stop/report before acting
source_files: vaultforge-business/PLAN.md; vaultforge-business/TASKS.md; vaultforge-business/BUSINESS_FRAGMENT_LIBRARY_CANDIDATES.md; vaultforge-engine/PLAN.md
notes:

### HG-004 - Business Paid Pilot Or Launch
decision_0_or_1:
lane_scope: vaultforge-business
gate_type: paid-api
trigger_condition: When business work moves from docs, WhatIf, dry-run, or internal demo packaging into a private paid pilot, live paid/API generation, pricing, licensing, publication, or public launch.
why_hard_gate: Paid/public work combines product positioning, budget spend, rights language, privacy, output quality, and client-facing promises.
decision_1_allows: One private paid-pilot/demo package with fixed scope, limited live generation, manual review, no public listing, no legal/trademark claims, and the scope/budget/output path recorded before generation.
decision_0_blocks: Paid pilot work, public launch work, binding pricing/licensing claims, and live paid/API generation for business packages.
default_if_blank: stop/report before acting #live-required
source_files: vaultforge-business/BUSINESS_PAID_LAUNCH_DECISION_NOTE.md; vaultforge-business/PLAN.md; vaultforge-business/TASKS.md; vaultforge-business/SIGN_UP.md
notes:

### HG-005 - Coding Bridge Live Responses API Use
decision_0_or_1: 
lane_scope: vaultforge-coding
gate_type: secret
trigger_condition: When the coding bridge MVP moves from local smoke/manual usage artifacts into real OpenAI Responses API calls requiring a loaded key, spend, model choice, or remote request.
why_hard_gate: This introduces secret handling, paid/API usage, model/provider behavior, context-cost risk, and externally generated responses.
decision_1_allows: One named coding bridge live run using the approved key source, model/provider, context cap, project root, output run folder, and budget ceiling.
decision_0_blocks: Live Responses API calls from the coding bridge; local smoke/test artifact work may continue.
default_if_blank: stop/report before acting
source_files: vaultforge-coding/CODEX_START.md; vaultforge-coding/SYSTEM.md; vaultforge-coding/PLAN.md; vaultforge-coding/TASKS.md
notes:

### HG-006 - Coding Bridge Write Or Patch Mode
decision_0_or_1:
lane_scope: vaultforge-coding
gate_type: destructive-move
trigger_condition: When the coding bridge proposes approval-gated write mode, patch application, direct file overwrite, or richer downstream event shaping that changes project files rather than only reporting.
why_hard_gate: The MVP intentionally excludes unsafe file mutation; adding write mode changes the bridge from report generator to code-changing automation.
decision_1_allows: Implementing only the approved write/patch mode design with explicit approval prompts, diff preview, target-root limits, and no automatic overwrite outside the approved scope.
decision_0_blocks: Any bridge feature that writes patches, overwrites files, or mutates project files.
default_if_blank: stop/report before acting
source_files: vaultforge-coding/SYSTEM.md; vaultforge-coding/PLAN.md; vaultforge-coding/TASKS.md; vaultforge-coding/vaultforge_code_codex_api_bridge_spec_v_2.md
notes:

### HG-007 - XP4L Live Vault Materialization
decision_0_or_1:
lane_scope: vaultforge-xp4l
gate_type: other
trigger_condition: When XP4L moves from dry-run, mirror, or docs-only output checks into non-dry-run writes against the live `E:\XP4Life` vault.
why_hard_gate: Live vault writes can change XP logs, quests, achievements, rewards, dashboards, state files, and managed-note updates in the user's real vault.
decision_1_allows: One scoped live materialization run against the named XP4Life target paths after backup/write-safety expectations, event batch path, dry-run evidence, and verification commands are recorded.
decision_0_blocks: Non-dry-run writes to the live XP4Life vault; dry-run, mirror validation, and docs/tests may continue.
default_if_blank: stop/report before acting #live-required
source_files: vaultforge-xp4l/PLAN.md; vaultforge-xp4l/TASKS.md; vaultforge-xp4l/SIGN_UP.md; vaultforge-xp4l/VAULT_OUTPUT_SHAPE.md; vaultforge-xp4l/HOW_TO_RUN_LIVE_XP4L.md
notes:

### HG-008 - XP4L Scoring And Progression Semantics
decision_0_or_1:
lane_scope: vaultforge-xp4l
gate_type: taste-quality
trigger_condition: When a run changes XP values, scoring semantics, rarity/prestige rules, achievement/reward thresholds, persistent progression behavior, or rule config meaning.
why_hard_gate: These choices define progression feel and reward balance; they are not purely mechanical implementation details.
decision_1_allows: The exact scoring/progression rule changes listed in the brief, with before/after examples and tests or dry-run evidence.
decision_0_blocks: Any change to scoring values, progression semantics, rarity/prestige behavior, or persistent state meaning.
default_if_blank: stop/report before acting
source_files: vaultforge-xp4l/XP_RULES_SURFACE.md; vaultforge-xp4l/HEURISTIC_BOUNDARIES.md; vaultforge-xp4l/PERSISTENT_PROGRESSION_STATE.md; vaultforge-xp4l/TASKS.md
notes:

### HG-009 - XP4L Event Source Expansion
decision_0_or_1:
lane_scope: vaultforge-xp4l, vaultforge-coding, vaultforge-business, vaultforge-art
gate_type: cross-lane-ownership
trigger_condition: When XP4L starts accepting new event sources beyond the current contract, especially art or business-derived signals, or when upstream lanes must change event payloads for XP4L.
why_hard_gate: Event source expansion changes cross-lane contracts, source identity, interpretation expectations, and downstream progression meaning.
decision_1_allows: Adding only the named source identity and event fields in the approved contract update, with fixture coverage and no upstream execution ownership moving into XP4L.
decision_0_blocks: New XP4L event sources, event fields, or upstream payload changes for XP4L.
default_if_blank: stop/report before acting
source_files: vaultforge-xp4l/EVENT_CONTRACT.md; vaultforge-xp4l/SYSTEM.md; vaultforge-xp4l/PLAN.md; THREAD_MAP.md
notes:

### HG-010 - Art Runtime Migration Or Rewrite
decision_0_or_1:
lane_scope: vaultforge-art
gate_type: destructive-move
trigger_condition: When a run proposes moving, deleting, rewriting, or migrating the sibling art runtime at `E:\tools\image_generation\vaultforge-art` into the VaultForge root.
why_hard_gate: The art folder under root is a coordination base, not the runtime owner; runtime migration can disturb dirty experiments, wrappers, engine assumptions, and external paths.
decision_1_allows: The specific migration or copy plan named in the brief, after an art bridge inventory and rollback/compatibility plan are recorded.
decision_0_blocks: Moving, deleting, rewriting, or migrating the sibling art runtime or experiments.
default_if_blank: stop/report before acting
source_files: vaultforge-art/CODEX_START.md; vaultforge-art/SYSTEM.md; vaultforge-art/PLAN.md; vaultforge-art/TASKS.md; ARCHITECTURE - engine extraction.md
notes:

### HG-011 - Icon Proposal Generation And Taste Selection
decision_0_or_1:
lane_scope: vaultforge-icon
gate_type: taste-quality
trigger_condition: When icon work leaves approved dry-run/docs paths and needs paid/API proposal generation, generated output folders, selection of a winning visual direction, reroll/resize taste decisions, or activation of an inactive style guide.
why_hard_gate: Icon proposals mix spend, generated artifacts, style taste, path approval, and whether outputs become selected/applied work.
decision_1_allows: One named icon proposal or selection action using the approved input note, output path, live/API budget if any, and review purpose, without applying icons or writing target-project files.
decision_0_blocks: Paid/API proposal generation, new generated proposal outputs, rerolls, selected/applied outputs, and taste selection decisions.
default_if_blank: stop/report before acting #live-required
source_files: vaultforge-icon/SYSTEM.md; vaultforge-icon/PLAN.md; vaultforge-icon/TASKS.md; vaultforge-icon/SIGN_UP.md; vaultforge-icon/documents/decisions/MEDIA_STYLE_PROPOSAL_STATUS_GATE.md
notes:

### HG-012 - Icon Apply Plan, Asset Moves, And Folder Icons
decision_0_or_1:
lane_scope: vaultforge-icon
gate_type: asset-move-delete
trigger_condition: When icon work proposes building or running `apply_icon.py`, creating apply-plan artifacts, moving/deleting/renaming assets, writing target-project files, or applying folder/file icons.
why_hard_gate: Apply work changes real assets or user-facing folder/project state, and the current contracts are review/dry-run planning only.
decision_1_allows: The exact apply-plan or asset operation listed in the brief, with selected source icons, target paths, output path approval, rollback expectations, and dry-run transcript evidence.
decision_0_blocks: `apply_icon.py` implementation or execution, generated apply-plan artifacts, asset move/delete/rename operations, target-project writes, and folder/file icon application.
default_if_blank: stop/report before acting
source_files: vaultforge-icon/CODEX_START.md; vaultforge-icon/SYSTEM.md; vaultforge-icon/PLAN.md; vaultforge-icon/documents/contracts/APPLY_ICON_APPLY_PLAN_CONTRACT.md
notes:

## Archived Gates
