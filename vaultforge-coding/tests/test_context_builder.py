from pathlib import Path

from vf_code_bridge.context_builder import build_context_manifest


def test_context_builder_returns_neutral_placeholder() -> None:
    result = build_context_manifest(Path("."))

    assert result.files_used == ()
    assert "not implemented" in result.skipped_reason.lower()
