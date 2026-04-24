import json

from tests.helpers import reset_bridge_root
from vf_code_bridge.bridge import execute_local_run
from vf_code_bridge.models import CliRequest


def _seed_prompt(root, mode: str) -> None:
    prompts_dir = root / "assets" / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    (prompts_dir / f"{mode}.md").write_text(f"{mode} prompt", encoding="utf-8")


def test_execute_local_run_writes_run_event_and_summary_artifacts() -> None:
    bridge_root = reset_bridge_root("bridge_success")
    _seed_prompt(bridge_root, "implement")

    payload = execute_local_run(
        CliRequest(
            mode="implement",
            task="Smoke local tracking",
            model="gpt-5.4-mini",
            input_tokens=120,
            output_tokens=30,
            duration_ms=250,
            notes="bridge smoke",
        ),
        root=bridge_root,
    )

    run_artifact = (
        bridge_root
        / "assets"
        / "runs"
        / "live"
        / f"{payload['run']['run_id']}.json"
    )
    events_log = bridge_root / "assets" / "events" / "events.jsonl"
    summary_path = bridge_root / "assets" / "reports" / "usage_summary.json"

    assert payload["exit_code"] == 0
    assert payload["run"]["status"] == "completed"
    assert run_artifact.exists()
    assert events_log.exists()
    assert summary_path.exists()

    events = [
        json.loads(line)
        for line in events_log.read_text(encoding="utf-8").splitlines()
    ]
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert [event["event_type"] for event in events] == [
        "run_started",
        "run_completed",
    ]
    assert summary["total_runs"] == 1
    assert summary["completed_runs"] == 1


def test_execute_local_run_records_failed_runs(monkeypatch) -> None:
    bridge_root = reset_bridge_root("bridge_failure")
    _seed_prompt(bridge_root, "review")

    def _boom(*args, **kwargs):
        raise RuntimeError("context boom")

    monkeypatch.setattr("vf_code_bridge.bridge.build_context_manifest", _boom)

    payload = execute_local_run(
        CliRequest(
            mode="review",
            task="Force failure",
            model="gpt-5.4-mini",
            input_tokens=10,
            output_tokens=2,
        ),
        root=bridge_root,
    )

    events_log = bridge_root / "assets" / "events" / "events.jsonl"
    summary_path = bridge_root / "assets" / "reports" / "usage_summary.json"
    events = [
        json.loads(line)
        for line in events_log.read_text(encoding="utf-8").splitlines()
    ]
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert payload["exit_code"] == 1
    assert payload["run"]["status"] == "failed"
    assert [event["event_type"] for event in events] == [
        "run_started",
        "run_failed",
    ]
    assert summary["failed_runs"] == 1
