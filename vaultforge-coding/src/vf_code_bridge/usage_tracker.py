"""Local usage tracking helpers for the VaultForge Code bridge."""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from .config import default_cost_rates
from .file_ops import write_json
from .models import CostRates, RunRecord, SectionSummary, UsageSnapshot


def empty_usage() -> UsageSnapshot:
    """Return a zeroed usage snapshot."""

    return UsageSnapshot()


def _coerce_non_negative_int(value: object | None) -> int:
    """Normalize token and duration inputs into safe non-negative integers."""

    if value in (None, ""):
        return 0
    if isinstance(value, bool):
        return int(value)
    try:
        return max(int(float(value)), 0)
    except (TypeError, ValueError):
        return 0


def _value_from_keys(payload: Mapping[str, Any], keys: tuple[str, ...]) -> object | None:
    """Return the first present value from a mapping for the provided keys."""

    for key in keys:
        if key in payload:
            return payload[key]
    return None


def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    rates: CostRates | None = None,
) -> float:
    """Estimate cost from local per-million token rates."""

    active_rates = rates or default_cost_rates()
    estimated = (
        (input_tokens * active_rates.input_per_million)
        + (output_tokens * active_rates.output_per_million)
    ) / 1_000_000
    return round(estimated, 6)


def normalize_usage_payload(
    payload: Mapping[str, Any] | None = None,
    *,
    input_tokens: object | None = None,
    output_tokens: object | None = None,
    total_tokens: object | None = None,
    duration_ms: object | None = None,
    rates: CostRates | None = None,
) -> UsageSnapshot:
    """Normalize manual or API-shaped usage data into one stable record."""

    source = payload or {}
    nested_usage = source.get("usage") if isinstance(source.get("usage"), Mapping) else None
    usage_source: Mapping[str, Any] = nested_usage or source

    normalized_input = _coerce_non_negative_int(
        input_tokens
        if input_tokens is not None
        else _value_from_keys(
            usage_source,
            ("input_tokens", "prompt_tokens", "input", "input_token_count"),
        )
    )
    normalized_output = _coerce_non_negative_int(
        output_tokens
        if output_tokens is not None
        else _value_from_keys(
            usage_source,
            (
                "output_tokens",
                "completion_tokens",
                "output",
                "output_token_count",
            ),
        )
    )
    provided_total = _coerce_non_negative_int(
        total_tokens
        if total_tokens is not None
        else _value_from_keys(usage_source, ("total_tokens", "total"))
    )
    computed_total = normalized_input + normalized_output
    normalized_total = max(provided_total, computed_total)
    normalized_duration_ms = _coerce_non_negative_int(duration_ms)

    return UsageSnapshot(
        input_tokens=normalized_input,
        output_tokens=normalized_output,
        total_tokens=normalized_total,
        estimated_cost=estimate_cost(
            normalized_input,
            normalized_output,
            rates=rates,
        ),
        duration_ms=normalized_duration_ms,
    )


def _run_record_from_dict(payload: Mapping[str, Any]) -> RunRecord:
    """Convert stored JSON back into a typed run record."""

    return RunRecord(
        run_id=str(payload.get("run_id", "")),
        timestamp=str(payload.get("timestamp", "")),
        section=str(payload.get("section", "")),
        thread=str(payload.get("thread", "")),
        task_type=str(payload.get("task_type", "")),
        prompt_name=str(payload.get("prompt_name", "")),
        status=str(payload.get("status", "")),
        model=str(payload.get("model", "")),
        provider=str(payload.get("provider", "")),
        input_tokens=_coerce_non_negative_int(payload.get("input_tokens")),
        output_tokens=_coerce_non_negative_int(payload.get("output_tokens")),
        total_tokens=_coerce_non_negative_int(payload.get("total_tokens")),
        estimated_cost=round(float(payload.get("estimated_cost", 0.0)), 6),
        duration_ms=_coerce_non_negative_int(payload.get("duration_ms")),
        files_read=tuple(str(item) for item in payload.get("files_read", [])),
        files_written=tuple(str(item) for item in payload.get("files_written", [])),
        notes=str(payload.get("notes", "")),
    )


def write_run_record(run_record: RunRecord, runs_dir: Path) -> Path:
    """Write one run artifact to ``assets/runs``."""

    return write_json(runs_dir / f"{run_record.run_id}.json", run_record)


def load_run_records(runs_dir: Path) -> tuple[RunRecord, ...]:
    """Load all stored run artifacts from disk."""

    if not runs_dir.exists():
        return ()

    run_records = []
    for path in sorted(runs_dir.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        run_records.append(_run_record_from_dict(payload))
    return tuple(sorted(run_records, key=lambda item: (item.timestamp, item.run_id)))


def build_section_summary(
    run_records: tuple[RunRecord, ...],
    *,
    section: str,
    thread: str,
    generated_at: str | None = None,
) -> SectionSummary:
    """Aggregate local run artifacts into one section summary."""

    completed_runs = sum(1 for record in run_records if record.status == "completed")
    failed_runs = sum(1 for record in run_records if record.status == "failed")
    other_runs = len(run_records) - completed_runs - failed_runs
    last_record = run_records[-1] if run_records else None
    generated = generated_at or datetime.now().astimezone().isoformat(timespec="seconds")

    return SectionSummary(
        section=section,
        thread=thread,
        generated_at=generated,
        total_runs=len(run_records),
        completed_runs=completed_runs,
        failed_runs=failed_runs,
        other_runs=other_runs,
        total_input_tokens=sum(record.input_tokens for record in run_records),
        total_output_tokens=sum(record.output_tokens for record in run_records),
        total_tokens=sum(record.total_tokens for record in run_records),
        total_estimated_cost=round(
            sum(record.estimated_cost for record in run_records),
            6,
        ),
        last_run_id=last_record.run_id if last_record else "",
        last_status=last_record.status if last_record else "",
        last_timestamp=last_record.timestamp if last_record else "",
        models=tuple(sorted({record.model for record in run_records if record.model})),
        providers=tuple(
            sorted({record.provider for record in run_records if record.provider})
        ),
    )


def update_section_summary(
    runs_dir: Path,
    summary_path: Path,
    *,
    section: str,
    thread: str,
    generated_at: str | None = None,
) -> SectionSummary:
    """Rebuild the section summary JSON from all stored run artifacts."""

    run_records = load_run_records(runs_dir)
    summary = build_section_summary(
        run_records,
        section=section,
        thread=thread,
        generated_at=generated_at,
    )
    write_json(summary_path, asdict(summary))
    return summary
