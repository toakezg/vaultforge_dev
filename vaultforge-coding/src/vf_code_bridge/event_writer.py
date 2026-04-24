"""Append-only event logging for the VaultForge Code bridge."""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from .file_ops import append_jsonl
from .models import EventRecord, RunRecord

SUPPORTED_EVENT_TYPES = frozenset({"run_started", "run_completed", "run_failed"})


def build_event_record(
    event_type: str,
    *,
    run_id: str,
    timestamp: str,
    section: str,
    thread: str,
    task_type: str,
    prompt_name: str,
    status: str,
    model: str,
    provider: str,
    input_tokens: int = 0,
    output_tokens: int = 0,
    total_tokens: int = 0,
    estimated_cost: float = 0.0,
    duration_ms: int = 0,
    notes: str = "",
) -> EventRecord:
    """Build one typed lifecycle event."""

    if event_type not in SUPPORTED_EVENT_TYPES:
        valid = ", ".join(sorted(SUPPORTED_EVENT_TYPES))
        raise ValueError(f"Unsupported event type '{event_type}'. Expected one of: {valid}")

    return EventRecord(
        event_type=event_type,
        timestamp=timestamp,
        run_id=run_id,
        section=section,
        thread=thread,
        task_type=task_type,
        prompt_name=prompt_name,
        status=status,
        model=model,
        provider=provider,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        estimated_cost=estimated_cost,
        duration_ms=duration_ms,
        notes=notes,
    )


def event_from_run_record(
    event_type: str,
    run_record: RunRecord,
    *,
    timestamp: str,
    notes: str | None = None,
) -> EventRecord:
    """Build an event directly from a stored run record."""

    return build_event_record(
        event_type,
        run_id=run_record.run_id,
        timestamp=timestamp,
        section=run_record.section,
        thread=run_record.thread,
        task_type=run_record.task_type,
        prompt_name=run_record.prompt_name,
        status=run_record.status,
        model=run_record.model,
        provider=run_record.provider,
        input_tokens=run_record.input_tokens,
        output_tokens=run_record.output_tokens,
        total_tokens=run_record.total_tokens,
        estimated_cost=run_record.estimated_cost,
        duration_ms=run_record.duration_ms,
        notes=run_record.notes if notes is None else notes,
    )


def append_event_record(event_record: EventRecord, events_log_path: Path) -> Path:
    """Append one event to the shared section event log."""

    return append_jsonl(events_log_path, asdict(event_record))
