from vf_code_bridge.models import RunRecord
from tests.helpers import clear_matching_files, runtime_path
from vf_code_bridge.usage_tracker import (
    empty_usage,
    normalize_usage_payload,
    update_section_summary,
    write_run_record,
)


def test_empty_usage_starts_zeroed() -> None:
    usage = empty_usage()

    assert usage.input_tokens == 0
    assert usage.output_tokens == 0
    assert usage.total_tokens == 0
    assert usage.estimated_cost == 0.0
    assert usage.duration_ms == 0


def test_normalize_usage_payload_handles_missing_and_manual_values() -> None:
    usage = normalize_usage_payload(
        {"prompt_tokens": "120", "completion_tokens": 30, "total_tokens": 100},
        duration_ms="250",
    )

    assert usage.input_tokens == 120
    assert usage.output_tokens == 30
    assert usage.total_tokens == 150
    assert usage.duration_ms == 250


def test_update_section_summary_rebuilds_from_run_artifacts() -> None:
    runs_dir = runtime_path("usage", "runs", "live")
    reports_dir = runtime_path("usage", "reports")
    summary_path = reports_dir / "usage_summary.json"
    clear_matching_files(runs_dir, "*.json")
    clear_matching_files(reports_dir, "*.json")

    write_run_record(
        RunRecord(
            run_id="run-001",
            timestamp="2026-04-17T10:00:00+10:00",
            section="vaultforge-code",
            thread="vaultforge-coding",
            task_type="implement",
            prompt_name="implement",
            status="completed",
            model="gpt-5.4-mini",
            provider="openai",
            input_tokens=100,
            output_tokens=20,
            total_tokens=120,
            estimated_cost=0.000325,
            duration_ms=200,
        ),
        runs_dir,
    )
    write_run_record(
        RunRecord(
            run_id="run-002",
            timestamp="2026-04-17T10:05:00+10:00",
            section="vaultforge-code",
            thread="vaultforge-coding",
            task_type="review",
            prompt_name="review",
            status="failed",
            model="gpt-5.4-mini",
            provider="openai",
            input_tokens=40,
            output_tokens=5,
            total_tokens=45,
            estimated_cost=0.0001,
            duration_ms=150,
        ),
        runs_dir,
    )

    summary = update_section_summary(
        runs_dir,
        summary_path,
        section="vaultforge-code",
        thread="vaultforge-coding",
        generated_at="2026-04-17T10:06:00+10:00",
    )

    assert summary.total_runs == 2
    assert summary.completed_runs == 1
    assert summary.failed_runs == 1
    assert summary.total_tokens == 165
    assert summary.last_run_id == "run-002"
