"""VaultForge Workflow B cycle controller.

This controller creates a locked, inspectable run packet for repeated
Workflow A rotations. It can optionally invoke Codex CLI for each generated
agent prompt, but it defaults to planning only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence


ROOT_DOCS = (
    "CODEX_START.md",
    "README.md",
    "SYSTEM.md",
    "CURRENT_STATE.md",
    "THREAD_MAP.md",
    "PLAN.md",
    "TASKS.md",
    "CHANGELOG.md",
    "MULTI_AGENT_WORKFLOW.md",
    "MULTI_AGENT_WORKFLOW_B.md",
    "WORKFLOW_REVIEW.md",
)

SECTION_DOCS = (
    "CODEX_START.md",
    "SYSTEM.md",
    "PLAN.md",
    "TASKS.md",
    "CHANGELOG.md",
    "SIGN_UP.md",
)

DEFAULT_LANES = {
    "root": ".",
    "vaultforge-engine": "vaultforge-engine",
    "vaultforge-business": "vaultforge-business",
    "vaultforge-art": "vaultforge-art",
    "vaultforge-coding": "vaultforge-coding",
    "vaultforge-xp4l": "vaultforge-xp4l",
    "vaultforge-icon": "vaultforge-icon",
}

ROLE_ORDER = ("coordinator", "builder", "reviewer", "recorder")
DEFAULT_EXTERNAL_WORKFLOW_FILE = Path(r"F:\toakezg\workflows\workflow-types.md")


@dataclass(frozen=True)
class AgentSpec:
    """One logical agent prompt to generate or execute."""

    name: str
    lane: str
    role: str
    workdir: str
    write_scope: str
    tasks: tuple[str, ...]


@dataclass(frozen=True)
class RunPlan:
    """Serializable Workflow B run plan."""

    run_id: str
    created_at: str
    root: str
    cycles: int
    task: str
    execute: bool
    parallel: bool
    commit_mode: str
    commit_prefix: str
    workflow_review_every: int
    watch_workflows: bool
    watch_workflow_files: tuple[str, ...]
    agents: tuple[AgentSpec, ...]


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create or execute a VaultForge Workflow B multi-agent cycle plan."
    )
    parser.add_argument("--root", type=Path, help="VaultForge root folder.")
    parser.add_argument("--cycles", type=int, default=1, help="Cycle budget.")
    parser.add_argument(
        "--lane",
        action="append",
        choices=tuple(DEFAULT_LANES),
        help="Lane to include. Repeat for multiple lanes.",
    )
    parser.add_argument(
        "--task",
        required=True,
        help="Main build brief for the full run.",
    )
    parser.add_argument(
        "--agent-task",
        action="append",
        default=[],
        metavar="AGENT:TASK;TASK",
        help="Assign one or more semicolon-separated tasks to an agent.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Invoke codex exec for each generated prompt.",
    )
    parser.add_argument(
        "--parallel",
        action="store_true",
        help="Run same-cycle agents in parallel. Use only with disjoint write scopes.",
    )
    parser.add_argument(
        "--commit-mode",
        default="review",
        choices=("never", "review", "cycle", "agent"),
        help=(
            "Commit policy for spawned agents. Default review means commit only "
            "after a reviewer accepts scoped changes."
        ),
    )
    parser.add_argument(
        "--commit-prefix",
        default="workflow-b",
        help="Prefix to use in agent-created commit messages.",
    )
    parser.add_argument(
        "--workflow-review-every",
        type=int,
        default=2,
        help=(
            "Update WORKFLOW_REVIEW.md every N cycles. Use 0 to disable "
            "controller review snapshots."
        ),
    )
    parser.set_defaults(watch_workflows=True)
    parser.add_argument(
        "--watch-workflows",
        dest="watch_workflows",
        action="store_true",
        help="Watch workflow docs for changes between cycles (default).",
    )
    parser.add_argument(
        "--no-watch-workflows",
        dest="watch_workflows",
        action="store_false",
        help="Do not watch workflow docs for changes between cycles.",
    )
    parser.add_argument(
        "--watch-workflow-file",
        action="append",
        default=[],
        help="Extra workflow file to fingerprint and surface when it changes.",
    )
    parser.add_argument(
        "--model",
        help="Optional Codex model override passed to codex exec.",
    )
    parser.add_argument(
        "--sandbox",
        default="workspace-write",
        choices=("read-only", "workspace-write", "danger-full-access"),
        help=(
            "Codex exec sandbox setting. If Windows sandbox CryptUnprotectData "
            "errors appear, use --bypass-sandbox instead."
        ),
    )
    parser.add_argument(
        "--bypass-sandbox",
        action="store_true",
        help=(
            "Pass Codex CLI's dangerously-bypass-approvals-and-sandbox flag. "
            "Use only for trusted local VaultForge runs."
        ),
    )
    parser.add_argument(
        "--approval",
        default="never",
        choices=("untrusted", "on-request", "never"),
        help=(
            "Compatibility placeholder. Current Codex CLI builds may not expose "
            "an exec approval flag, so Workflow B does not pass this through."
        ),
    )
    parser.add_argument(
        "--codex-bin",
        help="Optional explicit path to codex.cmd or codex.exe.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Output directory for run packets. Defaults to runs/workflow-b.",
    )
    parser.add_argument(
        "--force-unlock",
        action="store_true",
        help="Remove a stale Workflow B lock before starting.",
    )
    return parser.parse_args(argv)


def resolve_codex_bin(explicit_path: str | None = None) -> str:
    """Resolve the Codex executable in a Windows-friendly way."""

    if explicit_path:
        candidate = Path(explicit_path).expanduser()
        if candidate.exists():
            return str(candidate)
        raise SystemExit(f"--codex-bin was provided but does not exist: {candidate}")

    names = ("codex.cmd", "codex.exe", "codex") if os.name == "nt" else ("codex",)
    for name in names:
        resolved = shutil.which(name)
        if resolved:
            return resolved
    raise SystemExit(
        "Could not find Codex CLI. Add it to PATH or pass "
        "--codex-bin C:\\Users\\natha\\AppData\\Roaming\\npm\\codex.cmd"
    )


def find_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if all((candidate / doc).exists() for doc in ("CODEX_START.md", "THREAD_MAP.md")):
            return candidate
    raise SystemExit("Could not find VaultForge root. Pass --root F:\\vaultforge.")


def read_text_if_exists(path: Path, max_chars: int = 8000) -> str:
    if not path.exists():
        return f"[missing: {path.name}]"
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) > max_chars:
        return text[:max_chars] + "\n\n[truncated for prompt packet]"
    return text


def file_fingerprint(path: Path) -> str:
    """Return a stable content fingerprint for a file, or a missing marker."""

    if not path.exists():
        return "missing"
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 128), b""):
            digest.update(chunk)
    return digest.hexdigest()


def workflow_watch_files(root: Path, extras: Sequence[str]) -> tuple[Path, ...]:
    """Build the workflow watch list from root docs and optional external files."""

    watched = [
        root / "MULTI_AGENT_WORKFLOW.md",
        root / "MULTI_AGENT_WORKFLOW_B.md",
        root / "WORKFLOW_REVIEW.md",
        root / "THREAD_MAP.md",
        root / "TASKS.md",
    ]
    if DEFAULT_EXTERNAL_WORKFLOW_FILE.exists():
        watched.append(DEFAULT_EXTERNAL_WORKFLOW_FILE)
    for item in extras:
        watched.append(Path(item))
    deduped: list[Path] = []
    seen = set()
    for path in watched:
        resolved = path.resolve()
        if str(resolved).lower() not in seen:
            seen.add(str(resolved).lower())
            deduped.append(resolved)
    return tuple(deduped)


def workflow_fingerprints(paths: Sequence[Path]) -> dict[str, str]:
    return {str(path): file_fingerprint(path) for path in paths}


def changed_workflow_files(
    previous: dict[str, str],
    current: dict[str, str],
) -> tuple[str, ...]:
    changed = []
    for path, fingerprint in current.items():
        if previous.get(path) != fingerprint:
            changed.append(path)
    return tuple(changed)


def workflow_change_note(changed_files: Sequence[str]) -> str:
    if not changed_files:
        return "No workflow document changes were detected before this cycle."
    lines = [
        "Workflow document changes were detected before this cycle.",
        "Treat the changed workflow docs as the newest operating guidance unless they conflict with hard gates.",
        "Changed files:",
    ]
    lines.extend(f"- {path}" for path in changed_files)
    return "\n".join(lines)


def normalize_run_id(task: str, timestamp: datetime) -> str:
    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in task)[:48]
    slug = "-".join(part for part in slug.split("-") if part) or "workflow-b"
    return f"{timestamp.strftime('%Y%m%dT%H%M%S')}-{slug}"


def parse_agent_tasks(items: Iterable[str]) -> dict[str, tuple[str, ...]]:
    parsed: dict[str, tuple[str, ...]] = {}
    for item in items:
        if ":" not in item:
            raise SystemExit(f"Invalid --agent-task value: {item}")
        agent, raw_tasks = item.split(":", 1)
        tasks = tuple(task.strip() for task in raw_tasks.split(";") if task.strip())
        if not tasks:
            raise SystemExit(f"No task text found in --agent-task value: {item}")
        parsed[agent.strip()] = tasks
    return parsed


def default_agents(
    *,
    root: Path,
    lanes: Sequence[str],
    base_task: str,
    assigned_tasks: dict[str, tuple[str, ...]],
) -> tuple[AgentSpec, ...]:
    agents: list[AgentSpec] = [
        AgentSpec(
            name="root-coordinator",
            lane="root",
            role="coordinator",
            workdir=str(root),
            write_scope="root coordination docs and the active Workflow B run packet",
            tasks=assigned_tasks.get("root-coordinator", (base_task,)),
        )
    ]

    for lane in lanes:
        if lane == "root":
            continue
        lane_path = root / DEFAULT_LANES[lane]
        agents.append(
            AgentSpec(
                name=f"{lane}-builder",
                lane=lane,
                role="builder",
                workdir=str(lane_path),
                write_scope=f"{lane} section files only unless root explicitly approves a handoff",
                tasks=assigned_tasks.get(f"{lane}-builder", (base_task,)),
            )
        )
        agents.append(
            AgentSpec(
                name=f"{lane}-reviewer",
                lane=lane,
                role="reviewer",
                workdir=str(lane_path),
                write_scope=f"{lane} verification notes, review findings, and safe docs updates",
                tasks=assigned_tasks.get(
                    f"{lane}-reviewer",
                    (f"Review the {lane} builder result for Workflow B task: {base_task}",),
                ),
            )
        )

    agents.append(
        AgentSpec(
            name="root-recorder",
            lane="root",
            role="recorder",
            workdir=str(root),
            write_scope="root handoff, root changelog, and affected section handoff notes only",
            tasks=assigned_tasks.get(
                "root-recorder",
                ("Record factual cycle results, gates, files touched, checks, and resume prompt.",),
            ),
        )
    )
    return tuple(agents)


def make_prompt(
    *,
    plan: RunPlan,
    agent: AgentSpec,
    cycle: int,
    root_docs: dict[str, str],
    section_docs: dict[str, str],
    run_dir: Path,
    workflow_note: str,
) -> str:
    task_lines = "\n".join(f"- {task}" for task in agent.tasks)
    root_doc_list = "\n".join(f"## {name}\n\n{text}" for name, text in root_docs.items())
    section_doc_list = "\n".join(
        f"## {name}\n\n{text}" for name, text in section_docs.items()
    )
    commit_policy = build_commit_policy(plan=plan, agent=agent, cycle=cycle)
    return f"""# VaultForge Workflow B Agent Prompt

Run id: {plan.run_id}
Cycle: {cycle} of {plan.cycles}
Agent: {agent.name}
Role: {agent.role}
Lane: {agent.lane}
Working directory: {agent.workdir}
Write scope: {agent.write_scope}
Commit mode: {plan.commit_mode}
Run packet: {run_dir}

## Main Run Brief

{plan.task}

## Assigned Tasks

{task_lines}

## Required Operating Rules

- Follow `MULTI_AGENT_WORKFLOW.md` as Workflow A inside this cycle.
- Stay inside the named lane and write scope.
- Read the root/section docs included below before editing.
- Use `THREAD_MAP.md` for ownership and routing.
- Stop at hard gates from Workflow A and record a decision note.
- Soft gates should become tasks or handoff notes if another approved safe slice remains.
- Do not move, delete, or rewrite unrelated files.
- Keep evidence: files touched, verification run, blockers, and next prompt.
- If this role is reviewer, lead with findings and file/line references where possible.
- If this role is recorder, update only the relevant handoff/changelog/task notes.

## Workflow Update Check

{workflow_note}

## Commit Policy

{commit_policy}

## Root Docs Snapshot

{root_doc_list}

## Section Docs Snapshot

{section_doc_list or "[root agent: use root docs snapshot]"}
"""


def build_commit_policy(*, plan: RunPlan, agent: AgentSpec, cycle: int) -> str:
    """Return role-aware git commit instructions for generated prompts."""

    base = [
        "- Before editing, run `git status --short` and treat that as the dirty baseline.",
        "- Never stage or commit pre-existing unrelated dirty files.",
        "- Only stage files you changed for this agent role and write scope.",
        "- If unsure whether a file is yours, leave it unstaged and record the question.",
    ]

    if plan.commit_mode == "never":
        return "\n".join(
            (
                "- Do not create git commits in this run.",
                "- Record changed files and suggested commit message in the handoff instead.",
                *base,
            )
        )

    message = (
        f"{plan.commit_prefix}: cycle {cycle} {agent.lane} {agent.role} - "
        f"{plan.task[:72]}"
    )
    commit_steps = [
        f"- Suggested commit message: `{message}`",
        "- Use `git diff --cached --stat` before committing to verify the staged scope.",
        "- After committing, record the commit hash in the run packet or handoff note.",
    ]

    if plan.commit_mode == "agent":
        return "\n".join(
            (
                "- Commit after this agent finishes its own scoped work, if and only if the result is coherent.",
                *base,
                *commit_steps,
            )
        )
    if plan.commit_mode == "cycle":
        if agent.role == "recorder":
            return "\n".join(
                (
                    "- Commit at the end of this cycle after builder and reviewer outputs are recorded.",
                    *base,
                    *commit_steps,
                )
            )
        return "\n".join(
            (
                "- Do not commit from this role. Leave scoped changes for the cycle recorder.",
                *base,
            )
        )
    if plan.commit_mode == "review":
        if agent.role == "reviewer":
            return "\n".join(
                (
                    "- Commit after review only if the scoped lane changes pass review.",
                    "- If review finds blocking issues, do not commit; record findings and the next safe fix.",
                    *base,
                    *commit_steps,
                )
            )
        return "\n".join(
            (
                "- Do not commit from this role. Leave scoped changes for the reviewer after verification.",
                *base,
            )
        )

    return "\n".join(("- Unknown commit mode; do not commit.", *base))


def write_plan_files(plan: RunPlan, run_dir: Path) -> None:
    json_payload = asdict(plan)
    (run_dir / "workflow-b-plan.json").write_text(
        json.dumps(json_payload, indent=2) + "\n",
        encoding="utf-8",
    )
    agents = "\n".join(
        f"- {agent.name}: {agent.role}, lane `{agent.lane}`, workdir `{agent.workdir}`"
        for agent in plan.agents
    )
    lane_args = " ".join(
        f"--lane {agent.lane}"
        for agent in plan.agents
        if agent.role == "builder" and agent.lane != "root"
    )
    if not lane_args:
        lane_args = "--lane root"
    escaped_task = plan.task.replace('"', '\\"')
    summary = f"""# Workflow B Plan

- Run id: `{plan.run_id}`
- Created: `{plan.created_at}`
- Root: `{plan.root}`
- Cycles: `{plan.cycles}`
- Execute: `{plan.execute}`
- Parallel: `{plan.parallel}`
- Commit mode: `{plan.commit_mode}`
- Workflow review every: `{plan.workflow_review_every}`
- Watch workflows: `{plan.watch_workflows}`
- Task: {plan.task}

## Agents

{agents}

## Resume

```bat
run_workflow_b.bat --cycles {plan.cycles} {lane_args} --task "{escaped_task}"
```
"""
    (run_dir / "workflow-b-plan.md").write_text(summary, encoding="utf-8")


def update_workflow_review_doc(
    *,
    root: Path,
    plan: RunPlan,
    cycle: int,
    run_dir: Path,
    changed_files: Sequence[str],
    reason: str,
) -> Path:
    """Update the root workflow review snapshot without clobbering the whole note."""

    path = root / "WORKFLOW_REVIEW.md"
    start = "<!-- workflow-b-controller-snapshot:start -->"
    end = "<!-- workflow-b-controller-snapshot:end -->"
    if path.exists():
        existing = path.read_text(encoding="utf-8", errors="replace")
    else:
        existing = """# VaultForge Workflow Review

This note is the root review surface for Workflow A and Workflow B.

It should stay short enough for long-running agents to reread quickly.

## Review Cadence

- Workflow B controller updates the snapshot block every configured review interval.
- Root recorder or coordinator may add human-readable notes above the controller block.
- Major changes still belong in `MULTI_AGENT_WORKFLOW.md`, `MULTI_AGENT_WORKFLOW_B.md`, `THREAD_MAP.md`, `TASKS.md`, and `CHANGELOG.md`.

"""

    changed_text = "\n".join(f"- `{item}`" for item in changed_files) or "- none detected"
    snapshot = f"""{start}
## Controller Review Snapshot

- Updated: `{datetime.now().astimezone().isoformat(timespec="seconds")}`
- Reason: {reason}
- Run id: `{plan.run_id}`
- Cycle: `{cycle}` of `{plan.cycles}`
- Run packet: `{run_dir}`
- Commit mode: `{plan.commit_mode}`
- Watched workflow changes this cycle:
{changed_text}

## Current Workflow Lessons

- Use Router-Triage at the front of mixed or vague long-run tasks.
- Use Memory-Context Refresh at the start of each cycle so agents respect current docs and dirty state.
- Use Planner-Executor-Verifier as the default build lane pattern.
- Use Parallel Specialist Review when review needs multiple risk lenses.
- Use Test-Driven Agent Loop for code or CLI behavior with concrete checks.
- Use Human-In-The-Loop gates for destructive, external, paid, secret, or taste-heavy decisions.
- Keep Workflow B adaptive by refreshing workflow docs between cycles rather than freezing the first prompt forever.
{end}
"""
    if start in existing and end in existing:
        before, rest = existing.split(start, 1)
        _, after = rest.split(end, 1)
        updated = before.rstrip() + "\n\n" + snapshot + after
    else:
        updated = existing.rstrip() + "\n\n" + snapshot
    path.write_text(updated, encoding="utf-8")
    return path


def append_status(path: Path, payload: dict[str, object]) -> None:
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, sort_keys=True))
        handle.write("\n")


def build_codex_command(
    *,
    args: argparse.Namespace,
    agent: AgentSpec,
    prompt_path: Path,
    output_path: Path,
) -> list[str]:
    command = [
        resolve_codex_bin(args.codex_bin),
        "exec",
        "--cd",
        agent.workdir,
        "--output-last-message",
        str(output_path),
    ]
    if args.bypass_sandbox:
        command.insert(2, "--dangerously-bypass-approvals-and-sandbox")
    else:
        command[4:4] = ["--sandbox", args.sandbox]
    if args.model:
        command.extend(["--model", args.model])
    command.append("-")
    return command


def run_agent(
    *,
    args: argparse.Namespace,
    agent: AgentSpec,
    prompt_path: Path,
    output_path: Path,
    status_path: Path,
) -> int:
    command = build_codex_command(
        args=args,
        agent=agent,
        prompt_path=prompt_path,
        output_path=output_path,
    )
    append_status(
        status_path,
        {
            "event": "agent_started",
            "agent": agent.name,
            "workdir": agent.workdir,
            "output": str(output_path),
        },
    )
    prompt_text = prompt_path.read_text(encoding="utf-8")
    completed = subprocess.run(
        command,
        input=prompt_text,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    append_status(
        status_path,
        {
            "event": "agent_finished",
            "agent": agent.name,
            "returncode": completed.returncode,
        },
    )
    return completed.returncode


def acquire_lock(root: Path, run_id: str, force: bool) -> Path:
    lock_path = root / ".workflow-b.lock"
    if lock_path.exists():
        if not force:
            raise SystemExit(
                f"Workflow B lock exists at {lock_path}. "
                "Use --force-unlock only after confirming no run is active."
            )
        lock_path.unlink()
    lock_path.write_text(
        json.dumps({"run_id": run_id, "pid": os.getpid()}, indent=2) + "\n",
        encoding="utf-8",
    )
    return lock_path


def lane_docs(root: Path, lane: str) -> dict[str, str]:
    if lane == "root":
        return {}
    lane_path = root / DEFAULT_LANES[lane]
    return {doc: read_text_if_exists(lane_path / doc) for doc in SECTION_DOCS}


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.cycles < 1:
        raise SystemExit("--cycles must be 1 or greater.")
    if args.workflow_review_every < 0:
        raise SystemExit("--workflow-review-every must be 0 or greater.")

    root = find_root(args.root or Path.cwd())
    lanes = tuple(dict.fromkeys(args.lane or ["root"]))
    timestamp = datetime.now().astimezone()
    run_id = normalize_run_id(args.task, timestamp)
    out_root = (args.out or (root / "runs" / "workflow-b")).resolve()
    run_dir = out_root / run_id
    status_path = run_dir / "status.jsonl"
    run_dir.mkdir(parents=True, exist_ok=False)

    lock_path = acquire_lock(root, run_id, args.force_unlock)
    try:
        assigned_tasks = parse_agent_tasks(args.agent_task)
        plan = RunPlan(
            run_id=run_id,
            created_at=timestamp.isoformat(timespec="seconds"),
            root=str(root),
            cycles=args.cycles,
            task=args.task,
            execute=args.execute,
            parallel=args.parallel,
            commit_mode=args.commit_mode,
            commit_prefix=args.commit_prefix,
            workflow_review_every=args.workflow_review_every,
            watch_workflows=args.watch_workflows,
            watch_workflow_files=tuple(str(path) for path in workflow_watch_files(root, args.watch_workflow_file)),
            agents=default_agents(
                root=root,
                lanes=lanes,
                base_task=args.task,
                assigned_tasks=assigned_tasks,
            ),
        )
        watched_workflow_files = workflow_watch_files(root, args.watch_workflow_file)
        workflow_state = workflow_fingerprints(watched_workflow_files)
        root_docs = {doc: read_text_if_exists(root / doc) for doc in ROOT_DOCS}
        write_plan_files(plan, run_dir)
        append_status(status_path, {"event": "plan_created", "run_id": run_id})

        for cycle in range(1, args.cycles + 1):
            cycle_dir = run_dir / f"cycle-{cycle:02d}"
            outputs_dir = cycle_dir / "outputs"
            outputs_dir.mkdir(parents=True, exist_ok=True)
            append_status(status_path, {"event": "cycle_started", "cycle": cycle})
            changed_files: tuple[str, ...] = ()
            if args.watch_workflows:
                current_workflow_state = workflow_fingerprints(watched_workflow_files)
                changed_files = changed_workflow_files(workflow_state, current_workflow_state)
                if changed_files:
                    append_status(
                        status_path,
                        {
                            "event": "workflow_docs_changed",
                            "cycle": cycle,
                            "files": list(changed_files),
                        },
                    )
                    workflow_state = current_workflow_state
                root_docs = {doc: read_text_if_exists(root / doc) for doc in ROOT_DOCS}
            workflow_note = workflow_change_note(changed_files)
            (cycle_dir / "workflow-update-note.md").write_text(
                workflow_note + "\n",
                encoding="utf-8",
            )
            if args.workflow_review_every and (
                cycle == 1 or cycle % args.workflow_review_every == 0 or changed_files
            ):
                review_path = update_workflow_review_doc(
                    root=root,
                    plan=plan,
                    cycle=cycle,
                    run_dir=run_dir,
                    changed_files=changed_files,
                    reason="cycle review cadence"
                    if not changed_files
                    else "workflow file change detected",
                )
                append_status(
                    status_path,
                    {
                        "event": "workflow_review_updated",
                        "cycle": cycle,
                        "path": str(review_path),
                    },
                )
                root_docs = {doc: read_text_if_exists(root / doc) for doc in ROOT_DOCS}
                workflow_state = workflow_fingerprints(watched_workflow_files)

            prompt_jobs = []
            for agent in plan.agents:
                prompt_path = cycle_dir / f"{agent.name}.prompt.md"
                output_path = outputs_dir / f"{agent.name}.last-message.md"
                prompt_path.write_text(
                    make_prompt(
                        plan=plan,
                        agent=agent,
                        cycle=cycle,
                        root_docs=root_docs,
                        section_docs=lane_docs(root, agent.lane),
                        run_dir=run_dir,
                        workflow_note=workflow_note,
                    ),
                    encoding="utf-8",
                )
                prompt_jobs.append((agent, prompt_path, output_path))

            if args.execute:
                if args.parallel:
                    processes = []
                    for agent, prompt_path, output_path in prompt_jobs:
                        command = build_codex_command(
                            args=args,
                            agent=agent,
                            prompt_path=prompt_path,
                            output_path=output_path,
                        )
                        append_status(
                            status_path,
                            {
                                "event": "agent_started",
                                "agent": agent.name,
                                "workdir": agent.workdir,
                                "output": str(output_path),
                            },
                        )
                        prompt_text = prompt_path.read_text(encoding="utf-8")
                        processes.append(
                            (
                                agent,
                                process := subprocess.Popen(
                                    command,
                                    stdin=subprocess.PIPE,
                                    text=True,
                                    encoding="utf-8",
                                    errors="replace",
                                ),
                                prompt_text,
                            )
                        )
                    for agent, process, prompt_text in processes:
                        process.communicate(prompt_text)
                        returncode = process.returncode
                        append_status(
                            status_path,
                            {
                                "event": "agent_finished",
                                "agent": agent.name,
                                "returncode": returncode,
                            },
                        )
                        if returncode != 0:
                            return returncode
                else:
                    for agent, prompt_path, output_path in prompt_jobs:
                        returncode = run_agent(
                            args=args,
                            agent=agent,
                            prompt_path=prompt_path,
                            output_path=output_path,
                            status_path=status_path,
                        )
                        if returncode != 0:
                            return returncode

            append_status(status_path, {"event": "cycle_finished", "cycle": cycle})

        append_status(status_path, {"event": "run_finished", "run_id": run_id})
        print(f"Workflow B run packet: {run_dir}")
        if not args.execute:
            print("Plan/dry-run only. Add --execute to launch codex exec agents.")
        return 0
    finally:
        if lock_path.exists():
            lock_path.unlink()


if __name__ == "__main__":
    sys.exit(main())
