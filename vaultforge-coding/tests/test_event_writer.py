import json

from vf_code_bridge.event_writer import append_event_record, build_event_record
from tests.helpers import clear_matching_files, runtime_path


def test_event_writer_appends_jsonl_records() -> None:
    events_dir = runtime_path("event_writer")
    events_log = events_dir / "events.jsonl"
    clear_matching_files(events_dir, "*.jsonl")
    append_event_record(
        build_event_record(
            "run_started",
            run_id="run-001",
            timestamp="2026-04-17T10:00:00+10:00",
            section="vaultforge-code",
            thread="vaultforge-coding",
            task_type="implement",
            prompt_name="implement",
            status="started",
            model="gpt-5.4-mini",
            provider="openai",
        ),
        events_log,
    )
    append_event_record(
        build_event_record(
            "run_completed",
            run_id="run-001",
            timestamp="2026-04-17T10:00:01+10:00",
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
            duration_ms=150,
        ),
        events_log,
    )

    entries = [
        json.loads(line)
        for line in events_log.read_text(encoding="utf-8").splitlines()
    ]

    assert len(entries) == 2
    assert entries[0]["event_type"] == "run_started"
    assert entries[1]["event_type"] == "run_completed"
    assert entries[1]["total_tokens"] == 120
