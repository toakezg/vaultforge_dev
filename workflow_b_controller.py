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
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from time import monotonic
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
DEFAULT_ESCAPE_HATCH_FILE = Path(r"F:\toakezg\workflows\esape-hatch.md")
TERMINAL_DETAIL = "compact"
TERMINAL_COLOR = "auto"

ANSI_RESET = "\033[0m"
ANSI = {
    "workflow": "\033[1;36m",
    "success": "\033[1;32m",
    "warning": "\033[1;33m",
    "danger": "\033[1;31m",
    "handoff": "\033[1;35m",
    "path": "\033[0;32m",
    "file": "\033[0;34m",
    "filetype": "\033[0;36m",
    "command": "\033[1;33m",
    "arg": "\033[0;36m",
    "fence": "\033[0;90m",
    "budget": "\033[0;33m",
}

TERMINAL_COLOR_PATTERNS = (
    (
        "fence",
        re.compile(r"(```(?:text|json|bat|powershell|python|md)?```|```(?:text|json|bat|powershell|python|md)?)", re.I),
    ),
    ("path", re.compile(r"\b[A-Za-z]:\\[^\s`\"')\]]+")),
    (
        "command",
        re.compile(
            r"\b(?:run_workflow_b_watch\.bat|run_workflow_b\.bat|python|py|codex|git|"
            r"run_workflow_b_watch|workflow_b_controller\.py)\b",
            re.I,
        ),
    ),
    ("arg", re.compile(r"(?<!\w)--[a-zA-Z0-9][a-zA-Z0-9-]*")),
    (
        "danger",
        re.compile(
            r"\b(?:hard gate|cancelled|canceled|failed|failure|error|unsafe|stop|stopped|"
            r"do not repeat|do not rerun|force-unlock|permission denied|access is denied)\b",
            re.I,
        ),
    ),
    (
        "success",
        re.compile(
            r"\b(?:agent_finished|cycle_finished|run_finished|completed|complete|verified|"
            r"approved|pass|ok)\b",
            re.I,
        ),
    ),
    (
        "warning",
        re.compile(
            r"\b(?:changed|dirty|modified|partial|uncertain|risk|warning|manual interrupt|"
            r"operator cancellation|no final signal block|budget_stop|timebox)\b",
            re.I,
        ),
    ),
    ("handoff", re.compile(r"\b(?:handoff|workflow-b-(?:stop|cancel)-handoff\.md)\b", re.I)),
    ("workflow", re.compile(r"(\[workflow-b\]|\bWorkflow B\b|\bWorkflow A\b|\bWORKFLOW_B_[A-Z_]+\b)", re.I)),
    ("budget", re.compile(r"\$\d+(?:\.\d+)?(?:/\$\d+(?:\.\d+)?)?|(?:\d+(?:\.\d+)?m/\d+(?:\.\d+)?m)")),
    (
        "file",
        re.compile(r"\b[\w.-]+\.(?:md|jsonl|json|py|bat|ps1|txt|yml|yaml|toml|cfg)\b", re.I),
    ),
    ("filetype", re.compile(r"\b(?:markdown|jsonl|json|python|batch|powershell|text)\b", re.I)),
)


class WorkflowBCancelled(Exception):
    """Raised when the operator requests a graceful Workflow B cancellation."""


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
    timebox_minutes: float
    usage_budget_usd: float
    estimated_agent_usd: float
    hard_gate_mode: str
    agents: tuple[AgentSpec, ...]


@dataclass(slots=True)
class BudgetState:
    """Mutable controller-side budget tracking."""

    started_monotonic: float
    timebox_minutes: float = 0.0
    usage_budget_usd: float = 0.0
    estimated_agent_usd: float = 0.0
    agent_runs_started: int = 0
    estimated_usage_usd: float = 0.0
    reported_usage_usd: float = 0.0


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
        "--timebox-minutes",
        type=float,
        default=0.0,
        help="Stop before starting more work after this many minutes. 0 disables.",
    )
    parser.add_argument(
        "--usage-budget-usd",
        type=float,
        default=0.0,
        help=(
            "Estimated usage budget in USD. 0 disables controller-side budget "
            "stops. Codex CLI does not expose reliable live cost here."
        ),
    )
    parser.add_argument(
        "--estimated-agent-usd",
        type=float,
        default=0.0,
        help=(
            "Estimated USD to reserve before starting each codex exec agent. "
            "Use with --usage-budget-usd for a conservative budget guard."
        ),
    )
    parser.add_argument(
        "--hard-gate-mode",
        default="switch-safe",
        choices=("stop", "switch-safe", "record-continue"),
        help=(
            "How Workflow B should respond when an agent reports a hard gate: "
            "stop, switch-safe, or record-continue."
        ),
    )
    parser.add_argument(
        "--terminal-detail",
        default="compact",
        choices=("compact", "verbose"),
        help=(
            "How much checkpoint detail to print to the terminal. "
            "Use verbose for a watch window."
        ),
    )
    parser.add_argument(
        "--terminal-color",
        default="auto",
        choices=("auto", "always", "never"),
        help=(
            "ANSI-color Workflow B controller terminal output. Auto uses color "
            "only for an interactive terminal and respects NO_COLOR."
        ),
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


def terminal_color_enabled() -> bool:
    if TERMINAL_COLOR == "never" or os.environ.get("NO_COLOR"):
        return False
    if TERMINAL_COLOR == "always":
        return True
    return sys.stdout.isatty()


def ansi_wrap(text: str, style: str) -> str:
    return f"{ANSI[style]}{text}{ANSI_RESET}"


def colorize_terminal_text(text: str) -> str:
    if not terminal_color_enabled() or not text:
        return text

    parts: list[str] = []
    index = 0
    while index < len(text):
        next_match: tuple[str, re.Match[str]] | None = None
        for style, pattern in TERMINAL_COLOR_PATTERNS:
            match = pattern.search(text, index)
            if match is None:
                continue
            if (
                next_match is None
                or match.start() < next_match[1].start()
                or (
                    match.start() == next_match[1].start()
                    and match.end() > next_match[1].end()
                )
            ):
                next_match = (style, match)

        if next_match is None:
            parts.append(text[index:])
            break

        style, match = next_match
        if match.start() > index:
            parts.append(text[index : match.start()])
        parts.append(ansi_wrap(match.group(0), style))
        index = match.end()

    return "".join(parts)


def tprint(*values: object, sep: str = " ", end: str = "\n", file=None, flush: bool = False) -> None:
    stream = sys.stdout if file is None else file
    text = sep.join(str(value) for value in values)
    if stream is sys.stdout:
        text = colorize_terminal_text(text)
    print(text, end=end, file=stream, flush=flush)


def run_process_with_terminal_color(
    command: Sequence[str],
    prompt_text: str,
) -> tuple[subprocess.Popen[str], int]:
    """Run a child process while colorizing only its live terminal stream."""

    if not terminal_color_enabled():
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        process.communicate(prompt_text)
        return process, process.returncode

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    try:
        if process.stdin is not None:
            process.stdin.write(prompt_text)
            process.stdin.close()
    except (BrokenPipeError, OSError):
        pass

    if process.stdout is not None:
        for line in process.stdout:
            sys.stdout.write(colorize_terminal_text(line))
            sys.stdout.flush()

    returncode = process.wait()
    return process, returncode


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
        root / "business-if-done.txt",
    ]
    if DEFAULT_EXTERNAL_WORKFLOW_FILE.exists():
        watched.append(DEFAULT_EXTERNAL_WORKFLOW_FILE)
    if DEFAULT_ESCAPE_HATCH_FILE.exists():
        watched.append(DEFAULT_ESCAPE_HATCH_FILE)
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


def budget_snapshot(state: BudgetState) -> dict[str, object]:
    """Return the current controller-side budget snapshot."""

    elapsed_seconds = monotonic() - state.started_monotonic
    elapsed_minutes = elapsed_seconds / 60.0
    remaining_minutes = (
        max(state.timebox_minutes - elapsed_minutes, 0.0)
        if state.timebox_minutes
        else None
    )
    remaining_usage = (
        max(state.usage_budget_usd - state.estimated_usage_usd, 0.0)
        if state.usage_budget_usd
        else None
    )
    return {
        "elapsed_seconds": round(elapsed_seconds, 1),
        "elapsed_minutes": round(elapsed_minutes, 3),
        "timebox_minutes": state.timebox_minutes,
        "remaining_minutes": None
        if remaining_minutes is None
        else round(remaining_minutes, 3),
        "timebox_used_percent": None
        if not state.timebox_minutes
        else round(min(elapsed_minutes / state.timebox_minutes * 100.0, 999.0), 2),
        "usage_budget_usd": state.usage_budget_usd,
        "estimated_agent_usd": state.estimated_agent_usd,
        "agent_runs_started": state.agent_runs_started,
        "estimated_usage_usd": round(state.estimated_usage_usd, 6),
        "reported_usage_usd": round(state.reported_usage_usd, 6),
        "remaining_estimated_usage_usd": None
        if remaining_usage is None
        else round(remaining_usage, 6),
        "estimated_usage_used_percent": None
        if not state.usage_budget_usd
        else round(min(state.estimated_usage_usd / state.usage_budget_usd * 100.0, 999.0), 2),
    }


def budget_stop_reason(state: BudgetState, *, before_agent: bool = False) -> str | None:
    """Return a budget stop reason, if the next work unit should not start."""

    elapsed_minutes = (monotonic() - state.started_monotonic) / 60.0
    if state.timebox_minutes and elapsed_minutes >= state.timebox_minutes:
        return (
            f"timebox reached: {elapsed_minutes:.2f} minutes elapsed "
            f"of {state.timebox_minutes:.2f}"
        )
    if (
        before_agent
        and state.usage_budget_usd
        and state.estimated_agent_usd
        and state.estimated_usage_usd + state.estimated_agent_usd
        > state.usage_budget_usd
    ):
        return (
            "estimated usage budget would be exceeded: "
            f"{state.estimated_usage_usd:.4f} used + "
            f"{state.estimated_agent_usd:.4f} reserved > "
            f"{state.usage_budget_usd:.4f}"
        )
    return None


def write_stop_handoff(
    *,
    run_dir: Path,
    reason: str,
    cycle: int | None,
    state: BudgetState,
    next_action: str,
    gate_question: str = "",
) -> Path:
    """Write a small stop handoff for budget or gate stops."""

    path = run_dir / "workflow-b-stop-handoff.md"
    cycle_text = "before cycle start" if cycle is None else str(cycle)
    gate_question_text = (
        f"- Gate question: {gate_question}\n" if gate_question.strip() else ""
    )
    text = f"""# Workflow B Stop Handoff

- Stopped: `{datetime.now().astimezone().isoformat(timespec="seconds")}`
- Cycle: `{cycle_text}`
- Reason: {reason}
{gate_question_text}- Next action: {next_action}

## Budget Snapshot

```json
{json.dumps(budget_snapshot(state), indent=2)}
```
"""
    path.write_text(text, encoding="utf-8")
    return path


def git_status_short(root: Path) -> str:
    try:
        completed = subprocess.run(
            ["git", "status", "--short"],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return f"[git status unavailable: {exc}]"
    output = (completed.stdout or "").strip()
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout or "").strip()
        return f"[git status failed: {detail}]"
    return output or "[clean or no tracked changes reported]"


def list_run_artifacts(run_dir: Path, *, limit: int = 40) -> str:
    if not run_dir.exists():
        return "[run directory missing]"
    files = sorted(
        (path for path in run_dir.rglob("*") if path.is_file()),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if not files:
        return "[no run artifacts found]"
    lines = []
    for path in files[:limit]:
        rel = path.relative_to(run_dir)
        lines.append(f"- `{rel}` ({path.stat().st_size} bytes)")
    if len(files) > limit:
        lines.append(f"- [... {len(files) - limit} more artifacts omitted]")
    return "\n".join(lines)


def write_cancel_handoff(
    *,
    run_dir: Path,
    plan: RunPlan,
    cycle: int | None,
    agent: AgentSpec | None,
    state: BudgetState,
) -> Path:
    """Write a cancellation handoff when the operator stops the run."""

    path = run_dir / "workflow-b-cancel-handoff.md"
    cycle_text = "before cycle start" if cycle is None else str(cycle)
    agent_text = "none active"
    if agent is not None:
        agent_text = (
            f"{agent.name} (lane `{agent.lane}`, role `{agent.role}`, "
            f"workdir `{agent.workdir}`)"
        )
    resume_lanes = " ".join(
        f"--lane {agent.lane}"
        for agent in plan.agents
        if agent.role == "builder" and agent.lane != "root"
    )
    if not resume_lanes:
        resume_lanes = "--lane root"
    escaped_task = plan.task.replace('"', '\\"')
    current_stage = "before cycle start" if cycle is None else f"cycle {cycle} of {plan.cycles}"
    if agent is not None:
        current_stage += f", active agent {agent.name}"
    root = Path(plan.root)
    git_status = git_status_short(root)
    artifacts = list_run_artifacts(run_dir)
    text = f"""# Workflow B Cancel Handoff

- Cancelled: `{datetime.now().astimezone().isoformat(timespec="seconds")}`
- Run id: `{plan.run_id}`
- Cycle: `{cycle_text}` of `{plan.cycles}`
- Active agent: {agent_text}
- Reason: operator requested cancellation with Ctrl+C or batch termination.
- Escape hatch workflow: `{DEFAULT_ESCAPE_HATCH_FILE}`

## Escape Hatch Summary

Stop reason:
: operator cancellation / manual interrupt

Active workflow:
: VaultForge Workflow B running Workflow A-style lane agents

Current stage:
: {current_stage}

Completed:
: Review `checkpoints.jsonl` and `status.jsonl` for all `agent_finished`,
  `cycle_finished`, and verification records before the cancellation point.

Partial or uncertain:
: The active agent and any outputs without a matching final signal block should
  be treated as partial or uncertain.

Changed files/artifacts:

```text
{git_status}
```

Run artifacts:

{artifacts}

Commands/checks already run:
: The controller command is represented by `workflow-b-plan.md`; agent-level
  checks are recorded in each `cycle-XX/outputs/*.last-message.md` file when
  the agent completed cleanly.

Known errors or risks:
: Cancellation may leave the active lane with partial edits or no final
  `WORKFLOW_B_*` signal block. Do not assume the active agent completed.

Do not repeat without checking:
: Do not rerun the same lane slice blindly until the run packet, dirty git
  status, and active agent output are reviewed.

Recommended resume workflow:
: Esape Hatch verification cycle, then Workflow B with a narrower task if the
  interrupted lane is clean enough to continue.

First next action:
: Inspect this handoff, `workflow-b-live-status.md`, `checkpoints.jsonl`, and
  `status.jsonl`; then check the active lane's git diff before continuing.

Verification before continuing:
: Confirm whether the active agent produced a final message and whether any
  changed files are complete, incomplete, uncertain, or unsafe to repeat.

## What To Review

- `workflow-b-live-status.md`
- `checkpoints.jsonl`
- `status.jsonl`
- latest `cycle-XX/outputs/*.last-message.md` files
- any changed files from the active lane before resuming

## Budget Snapshot

```json
{json.dumps(budget_snapshot(state), indent=2)}
```

## Resume Shape

Start a fresh run after reviewing the partial outputs:

```bat
run_workflow_b_watch.bat --cycles {plan.cycles} {resume_lanes} --timebox-minutes {plan.timebox_minutes} --usage-budget-usd {plan.usage_budget_usd} --estimated-agent-usd {plan.estimated_agent_usd} --hard-gate-mode {plan.hard_gate_mode} --commit-mode {plan.commit_mode} --task "{escaped_task}"
```

Do not use `--force-unlock` unless `.workflow-b.lock` remains and no Workflow B
Python process is active.
"""
    path.write_text(text, encoding="utf-8")
    return path


def parse_agent_signal(output_path: Path) -> dict[str, str]:
    """Parse a small Workflow B signal block from an agent final message."""

    signal: dict[str, str] = {}
    if not output_path.exists():
        return signal
    for raw_line in output_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line.upper().startswith("WORKFLOW_B_") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        signal[key.strip().upper()] = value.strip()
    return signal


def signal_is_yes(signal: dict[str, str], key: str) -> bool:
    return signal.get(key, "").strip().lower() in {"yes", "true", "1"}


def signal_usage_usd(signal: dict[str, str]) -> float:
    value = signal.get("WORKFLOW_B_USAGE_USD", "").strip().lstrip("$")
    if not value:
        return 0.0
    try:
        return max(float(value), 0.0)
    except ValueError:
        return 0.0


def ask_hard_gate_decision(*, agent: AgentSpec, question: str) -> int | None:
    """Ask the present operator to decide a clearly stated gate question."""

    question = question.strip()
    if not question or not sys.stdin.isatty():
        return None
    tprint("")
    tprint(f"Workflow B hard gate question from {agent.name}:")
    tprint(question)
    tprint("Reply 0 to keep the gate closed. Reply 1 to pass this gate.")
    while True:
        try:
            answer = input("Workflow B hard gate decision [0/1]: ").strip()
        except EOFError:
            return None
        if answer in {"0", "1"}:
            return int(answer)
        tprint("Enter 0 or 1.")


def handle_hard_gate_signal(
    *,
    signal: dict[str, str],
    mode: str,
    status_path: Path,
    run_dir: Path,
    cycle: int,
    agent: AgentSpec,
    state: BudgetState,
) -> bool:
    """Return True when the controller should stop for a hard gate."""

    if not signal_is_yes(signal, "WORKFLOW_B_HARD_GATE"):
        return False

    safe_work_remains = signal_is_yes(signal, "WORKFLOW_B_SAFE_WORK_REMAINS")
    next_action = signal.get("WORKFLOW_B_NEXT_ACTION", "review hard gate")
    gate_question = signal.get("WORKFLOW_B_GATE_QUESTION", "").strip()
    append_status(
        status_path,
        {
            "event": "hard_gate_reported",
            "cycle": cycle,
            "agent": agent.name,
            "mode": mode,
            "safe_work_remains": safe_work_remains,
            "gate_question": gate_question,
            "next_action": next_action,
            "budget": budget_snapshot(state),
        },
    )

    operator_decision = ask_hard_gate_decision(agent=agent, question=gate_question)
    if operator_decision is not None:
        event = (
            "hard_gate_operator_passed"
            if operator_decision == 1
            else "hard_gate_operator_closed"
        )
        append_status(
            status_path,
            {
                "event": event,
                "cycle": cycle,
                "agent": agent.name,
                "gate_question": gate_question,
                "operator_decision": operator_decision,
                "next_action": next_action,
            },
        )
        if operator_decision == 1:
            tprint("Workflow B hard gate passed by operator decision 1.")
            return False
        write_stop_handoff(
            run_dir=run_dir,
            reason=f"hard gate kept closed by operator decision 0 from {agent.name}",
            cycle=cycle,
            state=state,
            next_action=next_action,
            gate_question=gate_question,
        )
        tprint(f"Workflow B stopped for hard gate. Run packet: {run_dir}")
        append_status(
            status_path,
            {
                "event": "hard_gate_stop",
                "cycle": cycle,
                "agent": agent.name,
                "next_action": next_action,
                "operator_decision": operator_decision,
            },
        )
        return True

    if mode == "record-continue":
        return False
    if mode == "switch-safe" and safe_work_remains:
        append_status(
            status_path,
            {
                "event": "hard_gate_switch_safe",
                "cycle": cycle,
                "agent": agent.name,
                "next_action": next_action,
            },
        )
        return False

    write_stop_handoff(
        run_dir=run_dir,
        reason=f"hard gate reported by {agent.name}",
        cycle=cycle,
        state=state,
        next_action=next_action,
        gate_question=gate_question,
    )
    tprint(f"Workflow B stopped for hard gate. Run packet: {run_dir}")
    append_status(
        status_path,
        {
            "event": "hard_gate_stop",
            "cycle": cycle,
            "agent": agent.name,
            "next_action": next_action,
        },
    )
    return True


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
Hard gate mode: {plan.hard_gate_mode}
Timebox minutes: {plan.timebox_minutes}
Usage budget USD: {plan.usage_budget_usd}
Estimated agent USD: {plan.estimated_agent_usd}
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
- Respect the hard-gate mode:
  - `stop`: stop at a hard gate and leave a decision note.
  - `switch-safe`: stop the blocked slice, record the gate, then continue only with another approved safe slice if one exists.
  - `record-continue`: record the gate and continue only when the gate does not block the current safe work.
- Respect time and usage budgets. Prefer smaller safe slices as budget gets low.

## Required Final Signal

End your final answer with these exact lines so the controller can keep strict records:

```text
WORKFLOW_B_HARD_GATE: yes|no
WORKFLOW_B_SAFE_WORK_REMAINS: yes|no
WORKFLOW_B_GATE_QUESTION: blank unless a present operator can decide this gate with 0 closed or 1 pass
WORKFLOW_B_USAGE_USD: 0.00
WORKFLOW_B_NEXT_ACTION: short next action
```

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
    budget_args = []
    if plan.timebox_minutes:
        budget_args.append(f"--timebox-minutes {plan.timebox_minutes}")
    if plan.usage_budget_usd:
        budget_args.append(f"--usage-budget-usd {plan.usage_budget_usd}")
    if plan.estimated_agent_usd:
        budget_args.append(f"--estimated-agent-usd {plan.estimated_agent_usd}")
    if plan.hard_gate_mode != "switch-safe":
        budget_args.append(f"--hard-gate-mode {plan.hard_gate_mode}")
    budget_arg_text = " ".join(budget_args)
    if budget_arg_text:
        budget_arg_text += " "
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
- Timebox minutes: `{plan.timebox_minutes}`
- Usage budget USD: `{plan.usage_budget_usd}`
- Estimated agent USD: `{plan.estimated_agent_usd}`
- Hard gate mode: `{plan.hard_gate_mode}`
- Task: {plan.task}

## Agents

{agents}

## Resume

```bat
run_workflow_b.bat --cycles {plan.cycles} {lane_args} {budget_arg_text}--task "{escaped_task}"
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
- Timebox minutes: `{plan.timebox_minutes}`
- Usage budget USD: `{plan.usage_budget_usd}`
- Hard gate mode: `{plan.hard_gate_mode}`
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
    payload = {
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        **payload,
    }
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, sort_keys=True))
        handle.write("\n")


def format_minutes(value: object) -> str:
    if value is None:
        return "none"
    try:
        minutes = float(value)
    except (TypeError, ValueError):
        return str(value)
    total_tenths = int(round(max(minutes, 0.0) * 10))
    hours, rem_tenths = divmod(total_tenths, 600)
    rem_minutes = rem_tenths / 10.0
    if hours >= 1:
        return f"{hours}h {rem_minutes:.1f}m"
    return f"{rem_minutes:.1f}m"


def money_or_none(value: object) -> str:
    if value is None:
        return "none"
    try:
        return f"${float(value):.4f}"
    except (TypeError, ValueError):
        return str(value)


def checkpoint_payload(
    *,
    plan: RunPlan,
    state: BudgetState,
    phase: str,
    cycle: int | None = None,
    agent: AgentSpec | None = None,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    """Build a consistent checkpoint payload for long-run visibility."""

    budget = budget_snapshot(state)
    total_agent_slots = plan.cycles * len(plan.agents)
    remaining_cycles = None if cycle is None else max(plan.cycles - cycle, 0)
    cycle_percent = None
    if cycle is not None and plan.cycles:
        cycle_percent = round(min(cycle / plan.cycles * 100.0, 100.0), 2)

    payload: dict[str, object] = {
        "event": "checkpoint",
        "phase": phase,
        "run_id": plan.run_id,
        "execute": plan.execute,
        "parallel": plan.parallel,
        "commit_mode": plan.commit_mode,
        "hard_gate_mode": plan.hard_gate_mode,
        "cycle": {
            "current": cycle,
            "max": plan.cycles,
            "remaining_after_current": remaining_cycles,
            "percent_of_max": cycle_percent,
        },
        "agents": {
            "count_this_cycle": len(plan.agents),
            "started": state.agent_runs_started,
            "total_slots": total_agent_slots,
            "remaining_slots": max(total_agent_slots - state.agent_runs_started, 0),
        },
        "runtime": {
            "elapsed_seconds": budget["elapsed_seconds"],
            "elapsed_minutes": budget["elapsed_minutes"],
            "elapsed_human": format_minutes(budget["elapsed_minutes"]),
            "timebox_minutes": budget["timebox_minutes"],
            "timebox_human": format_minutes(budget["timebox_minutes"]),
            "remaining_minutes": budget["remaining_minutes"],
            "remaining_human": format_minutes(budget["remaining_minutes"]),
            "timebox_used_percent": budget["timebox_used_percent"],
        },
        "usage": {
            "budget_usd": budget["usage_budget_usd"],
            "estimated_agent_usd": budget["estimated_agent_usd"],
            "estimated_used_usd": budget["estimated_usage_usd"],
            "reported_used_usd": budget["reported_usage_usd"],
            "remaining_estimated_usd": budget["remaining_estimated_usage_usd"],
            "estimated_used_percent": budget["estimated_usage_used_percent"],
        },
    }
    if agent is not None:
        payload["agent"] = {
            "name": agent.name,
            "lane": agent.lane,
            "role": agent.role,
            "workdir": agent.workdir,
        }
    if extra:
        payload["extra"] = extra
    return payload


def print_checkpoint(payload: dict[str, object]) -> None:
    cycle = payload["cycle"]
    runtime = payload["runtime"]
    usage = payload["usage"]
    agent = payload.get("agent")
    cycle_text = f"{cycle['current']}/{cycle['max']}" if cycle["current"] else f"0/{cycle['max']}"
    time_text = (
        f"{runtime['elapsed_human']}/{runtime['timebox_human']}"
        if runtime["timebox_minutes"]
        else f"{runtime['elapsed_human']}/no timebox"
    )
    usage_text = (
        f"{money_or_none(usage['estimated_used_usd'])}/{money_or_none(usage['budget_usd'])}"
        if usage["budget_usd"]
        else f"{money_or_none(usage['estimated_used_usd'])}/no usage budget"
    )
    agent_text = f" | agent {agent['name']}" if isinstance(agent, dict) else ""
    tprint(
        "[workflow-b] "
        f"{payload['phase']} | cycle {cycle_text} | elapsed {time_text} | "
        f"est usage {usage_text} | agents {payload['agents']['started']}/"
        f"{payload['agents']['total_slots']}{agent_text}"
    )
    if TERMINAL_DETAIL != "verbose":
        return

    tprint(
        "  runtime: "
        f"remaining {runtime['remaining_human']} | "
        f"timebox used {runtime['timebox_used_percent']}%"
    )
    tprint(
        "  usage: "
        f"reported {money_or_none(usage['reported_used_usd'])} | "
        f"remaining est {money_or_none(usage['remaining_estimated_usd'])} | "
        f"used {usage['estimated_used_percent']}%"
    )
    tprint(
        "  cycles: "
        f"remaining after current {cycle['remaining_after_current']} | "
        f"progress {cycle['percent_of_max']}%"
    )
    if isinstance(agent, dict):
        tprint(
            "  agent: "
            f"lane {agent['lane']} | role {agent['role']} | workdir {agent['workdir']}"
        )
    extra = payload.get("extra")
    if isinstance(extra, dict) and extra:
        for key in ("output", "handoff", "reason", "path"):
            if key in extra:
                tprint(f"  {key}: {extra[key]}")


def write_live_status(run_dir: Path, payload: dict[str, object]) -> None:
    runtime = payload["runtime"]
    usage = payload["usage"]
    cycle = payload["cycle"]
    agent = payload.get("agent")
    agent_lines = ""
    if isinstance(agent, dict):
        agent_lines = f"""
## Current Agent

- Name: `{agent['name']}`
- Lane: `{agent['lane']}`
- Role: `{agent['role']}`
- Workdir: `{agent['workdir']}`
"""
    text = f"""# Workflow B Live Status

- Last checkpoint: `{payload.get('recorded_at', datetime.now().astimezone().isoformat(timespec="seconds"))}`
- Run id: `{payload['run_id']}`
- Phase: `{payload['phase']}`
- Cycle: `{cycle['current']}` of `{cycle['max']}`
- Remaining cycles after current: `{cycle['remaining_after_current']}`
- Execute: `{payload['execute']}`
- Parallel: `{payload['parallel']}`
- Commit mode: `{payload['commit_mode']}`
- Hard gate mode: `{payload['hard_gate_mode']}`

## Runtime

- Elapsed: `{runtime['elapsed_human']}` (`{runtime['elapsed_minutes']}` minutes)
- Timebox: `{runtime['timebox_human']}`
- Remaining timebox: `{runtime['remaining_human']}`
- Timebox used percent: `{runtime['timebox_used_percent']}`

## Usage

- Estimated used: `{money_or_none(usage['estimated_used_usd'])}`
- Reported used: `{money_or_none(usage['reported_used_usd'])}`
- Usage budget: `{money_or_none(usage['budget_usd'])}`
- Remaining estimated usage: `{money_or_none(usage['remaining_estimated_usd'])}`
- Estimated used percent: `{usage['estimated_used_percent']}`
- Estimated per-agent reserve: `{money_or_none(usage['estimated_agent_usd'])}`

## Agent Slots

- Agents started: `{payload['agents']['started']}`
- Total possible slots: `{payload['agents']['total_slots']}`
- Remaining slots: `{payload['agents']['remaining_slots']}`
{agent_lines}
## Latest Extra

```json
{json.dumps(payload.get('extra', {}), indent=2)}
```
"""
    (run_dir / "workflow-b-live-status.md").write_text(text, encoding="utf-8")


def record_checkpoint(
    *,
    run_dir: Path,
    status_path: Path,
    plan: RunPlan,
    state: BudgetState,
    phase: str,
    cycle: int | None = None,
    agent: AgentSpec | None = None,
    extra: dict[str, object] | None = None,
    print_line: bool = True,
) -> dict[str, object]:
    payload = {
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        **checkpoint_payload(
            plan=plan,
            state=state,
            phase=phase,
            cycle=cycle,
            agent=agent,
            extra=extra,
        ),
    }
    append_status(status_path, payload)
    checkpoint_path = run_dir / "checkpoints.jsonl"
    with checkpoint_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, sort_keys=True))
        handle.write("\n")
    write_live_status(run_dir, payload)
    if print_line:
        print_checkpoint(payload)
    return payload


def explain_codex_failure(
    *,
    returncode: int | None,
    output_path: Path | None = None,
    exception: BaseException | None = None,
) -> dict[str, object]:
    """Return a practical operator-facing explanation for a Codex CLI failure."""

    snippets: list[str] = []
    if output_path and output_path.exists():
        snippets.append(output_path.read_text(encoding="utf-8", errors="replace")[-4000:])
    if exception is not None:
        snippets.append(str(exception))
    combined = "\n".join(snippets).lower()

    issue = "codex_cli_failure"
    meaning = "Codex CLI returned a non-zero exit code before Workflow B could continue."
    next_steps = [
        "Open the agent output file if one exists.",
        "Check the terminal lines immediately above the failure.",
        "Rerun with --terminal-detail verbose for more controller checkpoints.",
    ]

    if isinstance(exception, FileNotFoundError) or "could not find codex cli" in combined:
        issue = "codex_cli_not_found"
        meaning = "Workflow B could not find codex.cmd, codex.exe, or the provided --codex-bin path."
        next_steps = [
            "Confirm Codex CLI is installed and available on PATH.",
            r"Or pass --codex-bin C:\Users\natha\AppData\Roaming\npm\codex.cmd.",
        ]
    elif "cryptunprotectdata" in combined or returncode in {-1, 4294967295}:
        issue = "windows_sandbox_or_tool_failure"
        meaning = (
            "Codex reported a Windows sandbox/tool execution failure. "
            "The common local symptom is CryptUnprotectData failed."
        )
        next_steps = [
            "For trusted local VaultForge runs, add --bypass-sandbox.",
            "If --bypass-sandbox was already used, inspect the agent output and Codex terminal lines for the failing tool.",
        ]
    elif "unexpected argument" in combined:
        issue = "codex_cli_argument_mismatch"
        meaning = "The installed Codex CLI rejected one of the flags Workflow B passed through."
        next_steps = [
            "Run codex exec --help and compare supported flags.",
            "Keep Workflow B controller compatibility flags out of the Codex command path.",
        ]
    elif "plugin" in combined or "plugins" in combined:
        issue = "codex_plugin_warning_or_failure"
        meaning = (
            "Codex mentioned plugins while running. If the agent exited 0, this is usually a warning; "
            "if it exited non-zero, a plugin/tool load or permission issue may have blocked the agent."
        )
        next_steps = [
            "Check whether the run continued after the warning.",
            "If the return code is non-zero, inspect Codex plugin/tool configuration and rerun the same single agent prompt if needed.",
        ]

    return {
        "issue": issue,
        "returncode": returncode,
        "meaning": meaning,
        "next_steps": next_steps,
        "output_path": None if output_path is None else str(output_path),
        "exception": None if exception is None else repr(exception),
    }


def print_failure_explanation(explanation: dict[str, object]) -> None:
    tprint("[workflow-b] Codex failure explanation")
    tprint(f"  issue: {explanation['issue']}")
    tprint(f"  returncode: {explanation['returncode']}")
    tprint(f"  meaning: {explanation['meaning']}")
    for step in explanation["next_steps"]:
        tprint(f"  next: {step}")
    if explanation.get("output_path"):
        tprint(f"  output: {explanation['output_path']}")


def stop_child_process(process: subprocess.Popen[str], *, label: str) -> None:
    """Best-effort cleanup for a Codex child when Workflow B is cancelled."""

    if process.poll() is not None:
        return
    tprint(f"[workflow-b] stopping active Codex process for {label}...")
    try:
        process.terminate()
        process.wait(timeout=8)
    except subprocess.TimeoutExpired:
        tprint(f"[workflow-b] Codex process for {label} did not stop; killing it.")
        process.kill()
        process.wait(timeout=8)
    except OSError as exc:
        tprint(f"[workflow-b] could not stop Codex process for {label}: {exc}")


def write_error_guide(
    *,
    run_dir: Path,
    cycle: int,
    agent: AgentSpec,
    explanation: dict[str, object],
) -> Path:
    path = run_dir / "workflow-b-error-guide.md"
    steps = "\n".join(f"- {step}" for step in explanation["next_steps"])
    text = f"""# Workflow B Error Guide

- Recorded: `{datetime.now().astimezone().isoformat(timespec="seconds")}`
- Cycle: `{cycle}`
- Agent: `{agent.name}`
- Lane: `{agent.lane}`
- Role: `{agent.role}`
- Workdir: `{agent.workdir}`
- Issue: `{explanation['issue']}`
- Return code: `{explanation['returncode']}`
- Output path: `{explanation['output_path']}`

## Meaning

{explanation['meaning']}

## Next Steps

{steps}

## Raw Explanation

```json
{json.dumps(explanation, indent=2)}
```
"""
    path.write_text(text, encoding="utf-8")
    return path


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
    plan: RunPlan,
    agent: AgentSpec,
    prompt_path: Path,
    output_path: Path,
    run_dir: Path,
    status_path: Path,
    state: BudgetState,
    cycle: int,
) -> tuple[int, dict[str, str]]:
    command = build_codex_command(
        args=args,
        agent=agent,
        prompt_path=prompt_path,
        output_path=output_path,
    )
    state.agent_runs_started += 1
    if state.estimated_agent_usd:
        state.estimated_usage_usd += state.estimated_agent_usd
    append_status(
        status_path,
        {
            "event": "agent_started",
            "cycle": cycle,
            "agent": agent.name,
            "workdir": agent.workdir,
            "output": str(output_path),
            "budget": budget_snapshot(state),
        },
    )
    record_checkpoint(
        run_dir=run_dir,
        status_path=status_path,
        plan=plan,
        state=state,
        phase="agent_started",
        cycle=cycle,
        agent=agent,
        extra={"output": str(output_path), "workdir": agent.workdir},
    )
    prompt_text = prompt_path.read_text(encoding="utf-8")
    process: subprocess.Popen[str] | None = None
    try:
        process, returncode = run_process_with_terminal_color(command, prompt_text)
    except KeyboardInterrupt:
        if process is not None:
            stop_child_process(process, label=agent.name)
        raise WorkflowBCancelled
    except OSError as exc:
        explanation = explain_codex_failure(
            returncode=None,
            output_path=output_path,
            exception=exc,
        )
        print_failure_explanation(explanation)
        append_status(
            status_path,
            {
                "event": "agent_launch_failed",
                "cycle": cycle,
                "agent": agent.name,
                "explanation": explanation,
                "budget": budget_snapshot(state),
            },
        )
        record_checkpoint(
            run_dir=run_dir,
            status_path=status_path,
            plan=plan,
            state=state,
            phase="agent_launch_failed",
            cycle=cycle,
            agent=agent,
            extra=explanation,
        )
        return 127, {}
    signal = parse_agent_signal(output_path)
    reported_usage = signal_usage_usd(signal)
    if reported_usage:
        state.reported_usage_usd += reported_usage
    append_status(
        status_path,
        {
            "event": "agent_finished",
            "cycle": cycle,
            "agent": agent.name,
            "returncode": returncode,
            "signal": signal,
            "budget": budget_snapshot(state),
        },
    )
    record_checkpoint(
        run_dir=run_dir,
        status_path=status_path,
        plan=plan,
        state=state,
        phase="agent_finished",
        cycle=cycle,
        agent=agent,
        extra={
            "returncode": returncode,
            "signal": signal,
            "output": str(output_path),
        },
    )
    if returncode != 0:
        explanation = explain_codex_failure(
            returncode=returncode,
            output_path=output_path,
        )
        guide = write_error_guide(
            run_dir=run_dir,
            cycle=cycle,
            agent=agent,
            explanation=explanation,
        )
        print_failure_explanation(explanation)
        append_status(
            status_path,
            {
                "event": "agent_failed_explained",
                "cycle": cycle,
                "agent": agent.name,
                "guide": str(guide),
                "explanation": explanation,
                "budget": budget_snapshot(state),
            },
        )
        record_checkpoint(
            run_dir=run_dir,
            status_path=status_path,
            plan=plan,
            state=state,
            phase="agent_failed_explained",
            cycle=cycle,
            agent=agent,
            extra={"guide": str(guide), **explanation},
        )
    return returncode, signal


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
    docs = {doc: read_text_if_exists(lane_path / doc) for doc in SECTION_DOCS}
    if lane == "vaultforge-business":
        docs["../business-if-done.txt"] = read_text_if_exists(
            root / "business-if-done.txt",
            max_chars=12000,
        )
    return docs


def main(argv: Sequence[str] | None = None) -> int:
    global TERMINAL_COLOR, TERMINAL_DETAIL
    args = parse_args(argv)
    TERMINAL_DETAIL = args.terminal_detail
    TERMINAL_COLOR = args.terminal_color
    if args.cycles < 1:
        raise SystemExit("--cycles must be 1 or greater.")
    if args.workflow_review_every < 0:
        raise SystemExit("--workflow-review-every must be 0 or greater.")
    if args.timebox_minutes < 0:
        raise SystemExit("--timebox-minutes must be 0 or greater.")
    if args.usage_budget_usd < 0:
        raise SystemExit("--usage-budget-usd must be 0 or greater.")
    if args.estimated_agent_usd < 0:
        raise SystemExit("--estimated-agent-usd must be 0 or greater.")

    root = find_root(args.root or Path.cwd())
    lanes = tuple(dict.fromkeys(args.lane or ["root"]))
    timestamp = datetime.now().astimezone()
    run_id = normalize_run_id(args.task, timestamp)
    out_root = (args.out or (root / "runs" / "workflow-b")).resolve()
    run_dir = out_root / run_id
    status_path = run_dir / "status.jsonl"
    run_dir.mkdir(parents=True, exist_ok=False)
    budget_state = BudgetState(
        started_monotonic=monotonic(),
        timebox_minutes=args.timebox_minutes,
        usage_budget_usd=args.usage_budget_usd,
        estimated_agent_usd=args.estimated_agent_usd,
    )
    plan: RunPlan | None = None
    current_cycle: int | None = None
    current_agent: AgentSpec | None = None

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
            timebox_minutes=args.timebox_minutes,
            usage_budget_usd=args.usage_budget_usd,
            estimated_agent_usd=args.estimated_agent_usd,
            hard_gate_mode=args.hard_gate_mode,
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
        append_status(
            status_path,
            {
                "event": "plan_created",
                "run_id": run_id,
                "budget": budget_snapshot(budget_state),
            },
        )
        record_checkpoint(
            run_dir=run_dir,
            status_path=status_path,
            plan=plan,
            state=budget_state,
            phase="plan_created",
            cycle=None,
            extra={"run_dir": str(run_dir), "watch_files": list(plan.watch_workflow_files)},
        )

        for cycle in range(1, args.cycles + 1):
            current_cycle = cycle
            current_agent = None
            cycle_stop_reason = budget_stop_reason(budget_state)
            if cycle_stop_reason:
                handoff = write_stop_handoff(
                    run_dir=run_dir,
                    reason=cycle_stop_reason,
                    cycle=cycle,
                    state=budget_state,
                    next_action="Resume with a fresh budget or lower-risk task selection.",
                )
                append_status(
                    status_path,
                    {
                        "event": "budget_stop",
                        "cycle": cycle,
                        "reason": cycle_stop_reason,
                        "handoff": str(handoff),
                        "budget": budget_snapshot(budget_state),
                    },
                )
                record_checkpoint(
                    run_dir=run_dir,
                    status_path=status_path,
                    plan=plan,
                    state=budget_state,
                    phase="budget_stop",
                    cycle=cycle,
                    extra={"reason": cycle_stop_reason, "handoff": str(handoff)},
                )
                tprint(f"Workflow B stopped for budget/timebox. Handoff: {handoff}")
                return 0
            cycle_dir = run_dir / f"cycle-{cycle:02d}"
            outputs_dir = cycle_dir / "outputs"
            outputs_dir.mkdir(parents=True, exist_ok=True)
            append_status(
                status_path,
                {
                    "event": "cycle_started",
                    "cycle": cycle,
                    "budget": budget_snapshot(budget_state),
                },
            )
            record_checkpoint(
                run_dir=run_dir,
                status_path=status_path,
                plan=plan,
                state=budget_state,
                phase="cycle_started",
                cycle=cycle,
                extra={"cycle_dir": str(cycle_dir), "outputs_dir": str(outputs_dir)},
            )
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
                    record_checkpoint(
                        run_dir=run_dir,
                        status_path=status_path,
                        plan=plan,
                        state=budget_state,
                        phase="workflow_docs_changed",
                        cycle=cycle,
                        extra={"files": list(changed_files)},
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
                record_checkpoint(
                    run_dir=run_dir,
                    status_path=status_path,
                    plan=plan,
                    state=budget_state,
                    phase="workflow_review_updated",
                    cycle=cycle,
                    extra={"path": str(review_path)},
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
            record_checkpoint(
                run_dir=run_dir,
                status_path=status_path,
                plan=plan,
                state=budget_state,
                phase="prompts_ready",
                cycle=cycle,
                extra={"prompt_count": len(prompt_jobs)},
            )

            if args.execute:
                if args.parallel:
                    processes = []
                    for agent, prompt_path, output_path in prompt_jobs:
                        current_agent = agent
                        command = build_codex_command(
                            args=args,
                            agent=agent,
                            prompt_path=prompt_path,
                            output_path=output_path,
                        )
                        start_reason = budget_stop_reason(budget_state, before_agent=True)
                        if start_reason:
                            handoff = write_stop_handoff(
                                run_dir=run_dir,
                                reason=start_reason,
                                cycle=cycle,
                                state=budget_state,
                                next_action="Resume with more budget or fewer parallel agents.",
                            )
                            append_status(
                                status_path,
                                {
                                    "event": "budget_stop",
                                    "cycle": cycle,
                                    "agent": agent.name,
                                    "reason": start_reason,
                                    "handoff": str(handoff),
                                    "budget": budget_snapshot(budget_state),
                                },
                            )
                            record_checkpoint(
                                run_dir=run_dir,
                                status_path=status_path,
                                plan=plan,
                                state=budget_state,
                                phase="budget_stop",
                                cycle=cycle,
                                agent=agent,
                                extra={"reason": start_reason, "handoff": str(handoff)},
                            )
                            tprint(f"Workflow B stopped for budget/timebox. Handoff: {handoff}")
                            return 0
                        budget_state.agent_runs_started += 1
                        if budget_state.estimated_agent_usd:
                            budget_state.estimated_usage_usd += budget_state.estimated_agent_usd
                        append_status(
                            status_path,
                            {
                                "event": "agent_started",
                                "cycle": cycle,
                                "agent": agent.name,
                                "workdir": agent.workdir,
                                "output": str(output_path),
                                "budget": budget_snapshot(budget_state),
                            },
                        )
                        record_checkpoint(
                            run_dir=run_dir,
                            status_path=status_path,
                            plan=plan,
                            state=budget_state,
                            phase="agent_started",
                            cycle=cycle,
                            agent=agent,
                            extra={
                                "mode": "parallel",
                                "output": str(output_path),
                                "workdir": agent.workdir,
                            },
                        )
                        prompt_text = prompt_path.read_text(encoding="utf-8")
                        try:
                            process = subprocess.Popen(
                                    command,
                                    stdin=subprocess.PIPE,
                                    text=True,
                                    encoding="utf-8",
                                    errors="replace",
                            )
                        except OSError as exc:
                            explanation = explain_codex_failure(
                                returncode=None,
                                output_path=output_path,
                                exception=exc,
                            )
                            guide = write_error_guide(
                                run_dir=run_dir,
                                cycle=cycle,
                                agent=agent,
                                explanation=explanation,
                            )
                            print_failure_explanation(explanation)
                            append_status(
                                status_path,
                                {
                                    "event": "agent_launch_failed",
                                    "cycle": cycle,
                                    "agent": agent.name,
                                    "guide": str(guide),
                                    "explanation": explanation,
                                    "budget": budget_snapshot(budget_state),
                                },
                            )
                            record_checkpoint(
                                run_dir=run_dir,
                                status_path=status_path,
                                plan=plan,
                                state=budget_state,
                                phase="agent_launch_failed",
                                cycle=cycle,
                                agent=agent,
                                extra={"guide": str(guide), **explanation},
                            )
                            return 127
                        processes.append(
                            (
                                agent,
                                output_path,
                                process,
                                prompt_text,
                            )
                        )
                    try:
                        for agent, output_path, process, prompt_text in processes:
                            current_agent = agent
                            process.communicate(prompt_text)
                            returncode = process.returncode
                            signal = parse_agent_signal(output_path)
                            reported_usage = signal_usage_usd(signal)
                            if reported_usage:
                                budget_state.reported_usage_usd += reported_usage
                            append_status(
                                status_path,
                                {
                                    "event": "agent_finished",
                                    "cycle": cycle,
                                    "agent": agent.name,
                                    "returncode": returncode,
                                    "signal": signal,
                                    "budget": budget_snapshot(budget_state),
                                },
                            )
                            record_checkpoint(
                                run_dir=run_dir,
                                status_path=status_path,
                                plan=plan,
                                state=budget_state,
                                phase="agent_finished",
                                cycle=cycle,
                                agent=agent,
                                extra={
                                    "mode": "parallel",
                                    "returncode": returncode,
                                    "signal": signal,
                                    "output": str(output_path),
                                },
                            )
                            if returncode != 0:
                                explanation = explain_codex_failure(
                                    returncode=returncode,
                                    output_path=output_path,
                                )
                                guide = write_error_guide(
                                    run_dir=run_dir,
                                    cycle=cycle,
                                    agent=agent,
                                    explanation=explanation,
                                )
                                print_failure_explanation(explanation)
                                append_status(
                                    status_path,
                                    {
                                        "event": "agent_failed_explained",
                                        "cycle": cycle,
                                        "agent": agent.name,
                                        "guide": str(guide),
                                        "explanation": explanation,
                                        "budget": budget_snapshot(budget_state),
                                    },
                                )
                                record_checkpoint(
                                    run_dir=run_dir,
                                    status_path=status_path,
                                    plan=plan,
                                    state=budget_state,
                                    phase="agent_failed_explained",
                                    cycle=cycle,
                                    agent=agent,
                                    extra={"guide": str(guide), **explanation},
                                )
                                return returncode
                            if handle_hard_gate_signal(
                                signal=signal,
                                mode=args.hard_gate_mode,
                                status_path=status_path,
                                run_dir=run_dir,
                                cycle=cycle,
                                agent=agent,
                                state=budget_state,
                            ):
                                return 3
                    except KeyboardInterrupt:
                        for stop_agent, _output_path, process, _prompt_text in processes:
                            stop_child_process(process, label=stop_agent.name)
                        raise WorkflowBCancelled
                else:
                    for agent, prompt_path, output_path in prompt_jobs:
                        current_agent = agent
                        start_reason = budget_stop_reason(budget_state, before_agent=True)
                        if start_reason:
                            handoff = write_stop_handoff(
                                run_dir=run_dir,
                                reason=start_reason,
                                cycle=cycle,
                                state=budget_state,
                                next_action="Resume with more budget or fewer agent runs.",
                            )
                            append_status(
                                status_path,
                                {
                                    "event": "budget_stop",
                                    "cycle": cycle,
                                    "agent": agent.name,
                                    "reason": start_reason,
                                    "handoff": str(handoff),
                                    "budget": budget_snapshot(budget_state),
                                },
                            )
                            record_checkpoint(
                                run_dir=run_dir,
                                status_path=status_path,
                                plan=plan,
                                state=budget_state,
                                phase="budget_stop",
                                cycle=cycle,
                                agent=agent,
                                extra={"reason": start_reason, "handoff": str(handoff)},
                            )
                            tprint(f"Workflow B stopped for budget/timebox. Handoff: {handoff}")
                            return 0
                        returncode, signal = run_agent(
                            args=args,
                            plan=plan,
                            agent=agent,
                            prompt_path=prompt_path,
                            output_path=output_path,
                            run_dir=run_dir,
                            status_path=status_path,
                            state=budget_state,
                            cycle=cycle,
                        )
                        if returncode != 0:
                            return returncode
                        if handle_hard_gate_signal(
                            signal=signal,
                            mode=args.hard_gate_mode,
                            status_path=status_path,
                            run_dir=run_dir,
                            cycle=cycle,
                            agent=agent,
                            state=budget_state,
                        ):
                            return 3

            append_status(
                status_path,
                {
                    "event": "cycle_finished",
                    "cycle": cycle,
                    "budget": budget_snapshot(budget_state),
                },
            )
            record_checkpoint(
                run_dir=run_dir,
                status_path=status_path,
                plan=plan,
                state=budget_state,
                phase="cycle_finished",
                cycle=cycle,
                extra={"cycle_dir": str(cycle_dir)},
            )
            current_agent = None

        append_status(
            status_path,
            {
                "event": "run_finished",
                "run_id": run_id,
                "budget": budget_snapshot(budget_state),
            },
        )
        record_checkpoint(
            run_dir=run_dir,
            status_path=status_path,
            plan=plan,
            state=budget_state,
            phase="run_finished",
            cycle=args.cycles,
            extra={"run_dir": str(run_dir)},
        )
        tprint(f"Workflow B run packet: {run_dir}")
        if not args.execute:
            tprint("Plan/dry-run only. Add --execute to launch codex exec agents.")
        return 0
    except (KeyboardInterrupt, WorkflowBCancelled):
        tprint()
        tprint("[workflow-b] cancellation requested; writing handoff and clearing lock.")
        if plan is not None:
            handoff = write_cancel_handoff(
                run_dir=run_dir,
                plan=plan,
                cycle=current_cycle,
                agent=current_agent,
                state=budget_state,
            )
            append_status(
                status_path,
                {
                    "event": "cancel_requested",
                    "cycle": current_cycle,
                    "agent": None if current_agent is None else current_agent.name,
                    "handoff": str(handoff),
                    "budget": budget_snapshot(budget_state),
                },
            )
            record_checkpoint(
                run_dir=run_dir,
                status_path=status_path,
                plan=plan,
                state=budget_state,
                phase="cancel_requested",
                cycle=current_cycle,
                agent=current_agent,
                extra={"handoff": str(handoff)},
            )
            tprint(f"Workflow B cancelled. Handoff: {handoff}")
        else:
            tprint("Workflow B cancelled before the run plan was fully created.")
        return 130
    finally:
        if lock_path.exists():
            lock_path.unlink()


if __name__ == "__main__":
    sys.exit(main())
