"""CLI entry point for the local VaultForge Code bridge."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .bridge import execute_local_run
from .config import ConfigError, DEFAULT_MAX_FILES, default_model, default_provider
from .models import CliRequest
from .prompts import PRESET_MODES


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser shape described in the spec."""

    parser = argparse.ArgumentParser(
        prog="vaultforge-code",
        description="Local CLI for the VaultForge Code bridge.",
    )
    parser.add_argument("mode", choices=PRESET_MODES, help="Preset mode to prepare.")
    parser.add_argument("--task", required=True, help="Main instruction for the run.")
    parser.add_argument(
        "--project-root",
        type=Path,
        help="Project or repo root to inspect during a later context pass.",
    )
    parser.add_argument("--context", type=Path, help="Optional extra context file.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Optional output location for a later write-capable phase.",
    )
    parser.add_argument(
        "--model",
        default=default_model(),
        help="Model label to record for this local run.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Keep the run local-only and note that no external API call was made.",
    )
    parser.add_argument(
        "--save-prompt",
        action="store_true",
        help="Mark that the compiled prompt should be saved once implemented.",
    )
    parser.add_argument(
        "--json",
        dest="json_output",
        action="store_true",
        help="Print the local run result as JSON.",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=DEFAULT_MAX_FILES,
        help="Cap future project context collection.",
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Repeatable include hint for a later context pass.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Repeatable exclude hint for a later context pass.",
    )
    parser.set_defaults(emit_event=True)
    parser.add_argument(
        "--emit-event",
        dest="emit_event",
        action="store_true",
        help="Emit lifecycle events to the shared JSONL log (default).",
    )
    parser.add_argument(
        "--no-emit-event",
        dest="emit_event",
        action="store_false",
        help="Skip lifecycle event writes for this run.",
    )
    parser.add_argument(
        "--provider",
        default=default_provider(),
        help="Provider label to record in local artifacts.",
    )
    parser.add_argument(
        "--input-tokens",
        type=int,
        help="Manual input token count for a local sample run.",
    )
    parser.add_argument(
        "--output-tokens",
        type=int,
        help="Manual output token count for a local sample run.",
    )
    parser.add_argument(
        "--total-tokens",
        type=int,
        help="Optional total token count override.",
    )
    parser.add_argument(
        "--duration-ms",
        type=int,
        help="Optional duration override in milliseconds.",
    )
    parser.add_argument(
        "--notes",
        default="",
        help="Optional operator note to persist with the run record.",
    )
    return parser


def namespace_to_request(namespace: argparse.Namespace) -> CliRequest:
    """Convert parser output into the shared request model."""

    return CliRequest(
        mode=namespace.mode,
        task=namespace.task,
        project_root=namespace.project_root,
        context=namespace.context,
        output_dir=namespace.output_dir,
        model=namespace.model,
        dry_run=namespace.dry_run,
        save_prompt=namespace.save_prompt,
        json_output=namespace.json_output,
        max_files=namespace.max_files,
        include=tuple(namespace.include),
        exclude=tuple(namespace.exclude),
        emit_event=namespace.emit_event,
        provider=namespace.provider,
        input_tokens=namespace.input_tokens,
        output_tokens=namespace.output_tokens,
        total_tokens=namespace.total_tokens,
        duration_ms=namespace.duration_ms,
        notes=namespace.notes,
    )


def format_result_text(payload: dict[str, object]) -> str:
    """Render a concise operator-facing summary."""

    run = payload["run"]
    summary = payload["usage_summary"]
    lines = [
        "VaultForge Code local tracking run",
        f"run id: {run['run_id']}",
        f"status: {run['status']}",
        f"task type: {run['task_type']}",
        f"model: {run['model']}",
        f"prompt template: {payload['prompt_template']}",
        f"run artifact: {payload['run_artifact']}",
        f"event log: {payload['events_log_path']}",
        f"usage summary: {payload['usage_summary_path']}",
        (
            "tokens: "
            f"{run['input_tokens']} in / {run['output_tokens']} out / "
            f"{run['total_tokens']} total"
        ),
        f"estimated cost: {run['estimated_cost']}",
        f"section runs tracked: {summary['total_runs']}",
    ]
    if "error" in payload:
        lines.append(f"error: {payload['error']}")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point."""

    try:
        parser = build_parser()
        namespace = parser.parse_args(argv)
        payload = execute_local_run(namespace_to_request(namespace))
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 2

    if namespace.json_output:
        print(json.dumps(payload, indent=2, default=str))
    else:
        print(format_result_text(payload))
    return int(payload["exit_code"])
