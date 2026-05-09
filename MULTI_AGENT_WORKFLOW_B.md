# VaultForge Multi-Agent Workflow B

Workflow B is the long-run controller layer for Workflow A.

Workflow A defines the role order for one build rotation:

```text
Coordinator -> Builder -> Reviewer -> Recorder
```

Workflow B repeats that rotation across a cycle budget and keeps each lane run
locked to VaultForge routing, section docs, explicit write scopes, and durable
handoff files.

## Purpose

Use Workflow B when Nath wants a longer run such as:

```bat
run_workflow_b.bat --cycles 7 --lane vaultforge-engine --lane vaultforge-business --task "Build the approved engine/business slices from TASKS.md"
```

The controller does not replace Codex judgment. It creates the run packet,
agent prompts, cycle manifests, and optional `codex exec` calls that keep the
long run from drifting away from the root/section model.

## Workflow Patterns Used

Workflow B borrows practical patterns from `F:\toakezg\workflows\workflow-types.md`:

- Router-Triage: classify mixed work by lane, risk, and next workflow before deep execution.
- Memory-Context Refresh: reread current root/section docs and dirty state at cycle starts.
- Planner-Executor-Verifier: default build pattern for each lane.
- Parallel Specialist Review: use reviewers as risk lenses rather than rubber stamps.
- Sequential Builder-Critic Loop: refine docs, specs, prompts, and plans across bounded passes.
- Test-Driven Agent Loop: use concrete checks when code or CLI behavior is involved.
- Human-In-The-Loop Approval: stop for destructive, external, paid, secret, live, or taste-heavy gates.

## Commit Policy

Workflow B can instruct agents to commit as they work. The controller does not
blindly run `git add .` because VaultForge often has unrelated dirty files,
generated outputs, or active lane work in the same root.

Default commit mode is review:

```bat
run_workflow_b.bat --cycles 7 --execute --commit-mode review --lane vaultforge-engine --lane vaultforge-business --task "Run approved section-local build slices"
```

Modes:

| Mode | Behavior |
|---|---|
| `never` | Do not commit. Record changed files and suggested commit messages in handoffs. |
| `review` | Reviewer commits only after scoped lane changes pass review. This is the default. |
| `cycle` | Recorder commits at the end of each cycle after build and review notes are captured. |
| `agent` | Each agent may commit after its own coherent scoped work. Use sparingly. |

Every commit-capable prompt tells the agent to:

- run `git status --short` before editing and treat it as the dirty baseline
- never stage pre-existing unrelated dirty files
- stage only files changed by that agent inside its write scope
- inspect `git diff --cached --stat` before committing
- record the commit hash in the run packet or handoff note

Use `--commit-prefix` to change the start of generated commit messages.

## Control Script

- Python controller: `workflow_b_controller.py`
- Batch launcher: `run_workflow_b.bat`
- Default run output: `runs/workflow-b/<timestamp-slug>/`
- Lock file: `.workflow-b.lock`
- Workflow review note: `WORKFLOW_REVIEW.md`

The script can be run from root or from a section folder. When run from a
section folder, pass `--root F:\vaultforge` if auto-detection cannot find the
root docs.

## Operating Modes

### Plan/Dry Run

Default behavior is plan-first and no Codex execution.

```bat
run_workflow_b.bat --cycles 3 --lane vaultforge-engine --task "Prepare the next safe engine docs/build slice"
```

This writes:

- `workflow-b-plan.json`
- `workflow-b-plan.md`
- per-cycle prompt files
- a status JSONL file

### Execute

Add `--execute` only when the run is meant to launch Codex CLI agents.

```bat
run_workflow_b.bat --cycles 7 --execute --lane vaultforge-engine --lane vaultforge-business --task "Run approved section-local build slices"
```

Each agent prompt is sent through `codex exec` with a section-aware working
directory. The default is sequential execution. Add `--parallel` only when the
selected lanes have disjoint write scopes.

## Agent Model

Workflow B keeps the Workflow A roles but lets them repeat and split by lane.

Default agents:

- `root-coordinator`: reads root docs, routes slices, checks gates
- `<lane>-builder`: performs one safe section-local task per cycle
- `<lane>-reviewer`: reviews the builder's result and records issues
- `root-recorder`: updates handoff/changelog/task notes when the cycle allows

You can assign more than one task to an agent:

```bat
run_workflow_b.bat --cycles 5 --lane vaultforge-coding --agent-task vaultforge-coding-builder:"finish context collection; add prompt saving"
```

The controller treats semicolon-separated items as separate tasks inside that
agent's cycle prompt.

## Cycle Rules

Each cycle follows this shape:

1. Root coordinator rereads `CODEX_START.md`, `CURRENT_STATE.md`,
   `THREAD_MAP.md`, `TASKS.md`, and `MULTI_AGENT_WORKFLOW.md`.
2. Lane agents reread their section `CODEX_START.md`, `SYSTEM.md`, `PLAN.md`,
   `TASKS.md`, `CHANGELOG.md`, and `SIGN_UP.md`.
3. Builders do the smallest safe slice in their lane write scope.
4. Reviewers verify the result and name any missing tests or drift.
5. Recorder writes the factual handoff and logs the next safe step.
6. Coordinator either continues, records a soft gate, or stops at a hard gate.
7. If the commit policy allows it, the reviewer or recorder commits only the
   scoped work from that review/cycle.
8. The controller checks watched workflow docs before the next cycle and
   refreshes prompts if workflow guidance changed.

The cycle budget is a hard cap. `--cycles 7` means at most seven rotations, not
seven unlimited builds.

## Workflow Change Watching

Workflow B watches workflow documents between cycles by default.

Watched files include:

- `MULTI_AGENT_WORKFLOW.md`
- `MULTI_AGENT_WORKFLOW_B.md`
- `WORKFLOW_REVIEW.md`
- `THREAD_MAP.md`
- `TASKS.md`
- `F:\toakezg\workflows\workflow-types.md` when present

If any watched file changes while the run is active, the controller:

- records a `workflow_docs_changed` event in `status.jsonl`
- writes `cycle-XX/workflow-update-note.md`
- refreshes root doc snapshots for the next agent prompts
- updates `WORKFLOW_REVIEW.md`

This does not mean agents may rewrite the workflow freely mid-task. It means
new cycle prompts will include the latest workflow guidance and continue
forward under the updated rules unless a hard gate appears.

Controls:

```bat
run_workflow_b.bat --workflow-review-every 2 --watch-workflows ...
run_workflow_b.bat --no-watch-workflows ...
run_workflow_b.bat --watch-workflow-file "F:\path\to\extra-workflow.md" ...
```

## Lane Safety

Root can coordinate multiple lanes, but each lane must own its own write scope.

Default write scopes:

| Lane | Working Directory | Write Scope |
|---|---|---|
| root | `F:\vaultforge` | root coordination docs and run packet |
| vaultforge-engine | `F:\vaultforge\vaultforge-engine` | engine docs, source, tests, changelog |
| vaultforge-business | `F:\vaultforge\vaultforge-business` | business wrappers, prompt bank, review docs |
| vaultforge-art | `F:\vaultforge\vaultforge-art` | art lane docs and wrappers only |
| vaultforge-coding | `F:\vaultforge\vaultforge-coding` | code bridge package, assets, reports |
| vaultforge-xp4l | `F:\vaultforge\vaultforge-xp4l` | XP4L contracts, event intake, outputs |
| vaultforge-icon | `F:\vaultforge\vaultforge-icon` | icon docs, icon workflow, SVG-Forge tasks |

`--parallel` is only appropriate when these scopes do not overlap and the
brief does not ask two agents to change the same shared contract.

## Gates

Workflow B inherits Workflow A gates.

Stop and ask Nath when:

- ownership changes between sections
- architecture changes beyond the approved brief
- secrets, paid services, or new account permissions are needed
- generated assets, live runs, or file moves/deletes need approval
- two valid paths depend on taste, quality/quantity, or product direction

Soft gates are recorded as tasks or handoff notes and the run continues only
when there is another approved safe slice.

## Output Packet

Each run packet should be enough for a new Codex thread to resume without
guessing:

```text
runs/workflow-b/<run-id>/
  workflow-b-plan.json
  workflow-b-plan.md
  status.jsonl
  cycle-01/
    root-coordinator.prompt.md
    vaultforge-engine-builder.prompt.md
    vaultforge-engine-reviewer.prompt.md
    root-recorder.prompt.md
    outputs/
  cycle-02/
    ...
```

## Recommended First Use

Start with a dry run:

```bat
run_workflow_b.bat --cycles 2 --lane vaultforge-engine --lane vaultforge-business --task "Prepare the next approved Workflow A slices without live generation"
```

Review `workflow-b-plan.md`. If the lane scopes and tasks are correct, rerun
with `--execute`.
