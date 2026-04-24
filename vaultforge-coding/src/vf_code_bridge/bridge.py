"""Local execution helpers for the VaultForge Code bridge."""

from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from time import perf_counter

from .config import (
    load_runtime_config,
)
from .context_builder import build_context_manifest
from .event_writer import append_event_record, build_event_record, event_from_run_record
from .file_ops import ensure_bridge_layout
from .models import CliRequest, RunRecord
from .prompts import prompt_path_for_mode
from .usage_tracker import normalize_usage_payload, update_section_summary, write_run_record


def build_run_id(mode: str, timestamp: datetime) -> str:
    """Build a readable run id for one local execution."""

    safe_mode = "".join(char.lower() if char.isalnum() else "-" for char in mode.strip())
    normalized_mode = safe_mode.strip("-") or "run"
    return f"{timestamp.strftime('%Y%m%dT%H%M%S%f%z')}_{normalized_mode}"


def _ensure_unique_run_id(run_id: str, runs_dir: Path) -> str:
    """Avoid overwriting a previous run artifact when ids collide."""

    candidate = run_id
    suffix = 1
    while (runs_dir / f"{candidate}.json").exists():
        suffix += 1
        candidate = f"{run_id}_{suffix:02d}"
    return candidate


def _now_iso() -> str:
    """Return the current local timestamp in ISO-8601 form."""

    return datetime.now().astimezone().isoformat(timespec="seconds")


def _compose_notes(request: CliRequest, *extra_notes: str) -> str:
    """Build one stable note string for local-only runs."""

    note_parts = []
    if request.notes.strip():
        note_parts.append(request.notes.strip())
    note_parts.append("Local tracking run only; no external API usage was retrieved.")
    if request.dry_run:
        note_parts.append("Dry-run flag was set.")
    note_parts.extend(note for note in extra_notes if note)
    return " ".join(note_parts)


def _result_payload(
    *,
    run_record: RunRecord,
    run_artifact_path: Path,
    usage_summary_path: Path,
    events_log_path: Path,
    prompt_template: Path,
    context_manifest: dict[str, object],
    summary: dict[str, object],
    error: str | None = None,
) -> dict[str, object]:
    """Build the operator-facing result payload."""

    payload: dict[str, object] = {
        "run": asdict(run_record),
        "run_artifact": str(run_artifact_path),
        "usage_summary": summary,
        "usage_summary_path": str(usage_summary_path),
        "events_log_path": str(events_log_path),
        "prompt_template": str(prompt_template),
        "context": context_manifest,
        "exit_code": 0 if error is None else 1,
    }
    if error is not None:
        payload["error"] = error
    return payload


def execute_local_run(
    request: CliRequest,
    *,
    root: Path | None = None,
    timestamp: datetime | None = None,
) -> dict[str, object]:
    """Run the local-only tracking flow and persist its artifacts."""

    runtime_config = load_runtime_config(root=root)
    paths = ensure_bridge_layout(paths=runtime_config.paths)
    rates = runtime_config.cost_rates
    now = timestamp or datetime.now().astimezone()
    run_id = _ensure_unique_run_id(build_run_id(request.mode, now), paths.runs_dir)
    run_timestamp = now.isoformat(timespec="seconds")
    section = runtime_config.section_name
    thread = runtime_config.thread_name
    provider = request.provider or runtime_config.provider
    model = request.model or runtime_config.model
    prompt_template = prompt_path_for_mode(request.mode, paths=runtime_config.paths)
    project_root = request.project_root or paths.workspace_root
    run_artifact_path = paths.runs_dir / f"{run_id}.json"
    files_read = [str(prompt_template.resolve())]
    if request.context is not None:
        files_read.append(str(request.context.resolve()))

    started = perf_counter()
    try:
        if request.emit_event:
            append_event_record(
                build_event_record(
                    "run_started",
                    run_id=run_id,
                    timestamp=run_timestamp,
                    section=section,
                    thread=thread,
                    task_type=request.mode,
                    prompt_name=request.mode,
                    status="started",
                    model=model,
                    provider=provider,
                    notes=_compose_notes(request),
                ),
                paths.events_log_path,
            )

        context_manifest = asdict(
            build_context_manifest(
                project_root=project_root,
                include=request.include,
                exclude=request.exclude,
                max_files=request.max_files,
            )
        )
        for item in context_manifest.get("files_used", []):
            files_read.append(str(item))

        measured_duration_ms = max(int((perf_counter() - started) * 1000), 0)
        usage = normalize_usage_payload(
            request.usage_payload,
            input_tokens=request.input_tokens,
            output_tokens=request.output_tokens,
            total_tokens=request.total_tokens,
            duration_ms=(
                request.duration_ms
                if request.duration_ms is not None
                else measured_duration_ms
            ),
            rates=rates,
        )
        run_record = RunRecord(
            run_id=run_id,
            timestamp=run_timestamp,
            section=section,
            thread=thread,
            task_type=request.mode,
            prompt_name=request.mode,
            status="completed",
            model=model,
            provider=provider,
            input_tokens=usage.input_tokens,
            output_tokens=usage.output_tokens,
            total_tokens=usage.total_tokens,
            estimated_cost=usage.estimated_cost,
            duration_ms=usage.duration_ms,
            files_read=tuple(dict.fromkeys(files_read)),
            files_written=tuple(
                item
                for item in (
                    str(run_artifact_path),
                    str(paths.events_log_path) if request.emit_event else None,
                    str(paths.usage_summary_path),
                )
                if item is not None
            ),
            notes=_compose_notes(request),
        )
        write_run_record(run_record, paths.runs_dir)
        summary = update_section_summary(
            paths.runs_dir,
            paths.usage_summary_path,
            section=section,
            thread=thread,
        )
        completed_timestamp = _now_iso()
        if request.emit_event:
            append_event_record(
                event_from_run_record(
                    "run_completed",
                    run_record,
                    timestamp=completed_timestamp,
                ),
                paths.events_log_path,
            )

        return _result_payload(
            run_record=run_record,
            run_artifact_path=run_artifact_path,
            usage_summary_path=paths.usage_summary_path,
            events_log_path=paths.events_log_path,
            prompt_template=prompt_template,
            context_manifest=context_manifest,
            summary=asdict(summary),
        )
    except Exception as exc:
        failed_timestamp = _now_iso()
        failure_usage = normalize_usage_payload(
            request.usage_payload,
            input_tokens=request.input_tokens,
            output_tokens=request.output_tokens,
            total_tokens=request.total_tokens,
            duration_ms=max(int((perf_counter() - started) * 1000), 0),
            rates=rates,
        )
        failure_record = RunRecord(
            run_id=run_id,
            timestamp=failed_timestamp,
            section=section,
            thread=thread,
            task_type=request.mode,
            prompt_name=request.mode,
            status="failed",
            model=model,
            provider=provider,
            input_tokens=failure_usage.input_tokens,
            output_tokens=failure_usage.output_tokens,
            total_tokens=failure_usage.total_tokens,
            estimated_cost=failure_usage.estimated_cost,
            duration_ms=failure_usage.duration_ms,
            files_read=tuple(dict.fromkeys(files_read)),
            files_written=tuple(
                item
                for item in (
                    str(run_artifact_path),
                    str(paths.events_log_path) if request.emit_event else None,
                    str(paths.usage_summary_path),
                )
                if item is not None
            ),
            notes=_compose_notes(request, f"Run failed: {exc}"),
        )
        write_run_record(failure_record, paths.runs_dir)
        summary = update_section_summary(
            paths.runs_dir,
            paths.usage_summary_path,
            section=section,
            thread=thread,
        )
        if request.emit_event:
            append_event_record(
                event_from_run_record(
                    "run_failed",
                    failure_record,
                    timestamp=failed_timestamp,
                ),
                paths.events_log_path,
            )
        return _result_payload(
            run_record=failure_record,
            run_artifact_path=run_artifact_path,
            usage_summary_path=paths.usage_summary_path,
            events_log_path=paths.events_log_path,
            prompt_template=prompt_template,
            context_manifest={"error": str(exc)},
            summary=asdict(summary),
            error=str(exc),
        )
