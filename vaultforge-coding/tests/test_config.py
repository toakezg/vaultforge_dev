from pathlib import Path

import pytest

from vf_code_bridge.config import (
    ConfigError,
    default_cost_rates,
    default_model,
    default_paths,
    load_runtime_config,
    repository_root,
)


def test_default_paths_match_section_layout() -> None:
    root = repository_root()
    paths = default_paths()

    assert paths.workspace_root == root
    assert paths.package_root == root / "src" / "vf_code_bridge"
    assert paths.prompts_dir == root / "assets" / "prompts"
    assert paths.runs_root_dir == root / "assets" / "runs"
    assert paths.runs_dir == root / "assets" / "runs" / "live"
    assert paths.runs_examples_dir == root / "assets" / "runs" / "examples"
    assert paths.events_log_path == root / "assets" / "events" / "events.jsonl"
    assert paths.usage_summary_path == root / "assets" / "reports" / "usage_summary.json"


def test_env_override_loading_normalizes_values() -> None:
    root = repository_root()
    config = load_runtime_config(
        env={
            "VF_CODE_SECTION_NAME": "vaultforge-code-test",
            "VF_CODE_PROVIDER": "test-provider",
            "VF_CODE_MODEL": "gpt-test",
            "VF_CODE_INPUT_RATE": "2.5",
            "VF_CODE_OUTPUT_RATE": "8",
            "VF_CODE_RUNS_DIR": "custom/runs/live",
            "VF_CODE_EVENTS_DIR": "custom/events",
            "VF_CODE_REPORTS_DIR": "custom/reports",
            "VF_CODE_PROMPTS_DIR": "custom/prompts",
        }
    )

    assert config.section_name == "vaultforge-code-test"
    assert config.provider == "test-provider"
    assert config.model == "gpt-test"
    assert config.cost_rates.input_per_million == 2.5
    assert config.cost_rates.output_per_million == 8.0
    assert config.paths.prompts_dir == root / "custom" / "prompts"
    assert config.paths.runs_dir == root / "custom" / "runs" / "live"
    assert config.paths.runs_examples_dir == root / "custom" / "runs" / "examples"
    assert config.paths.events_dir == root / "custom" / "events"
    assert config.paths.reports_dir == root / "custom" / "reports"


def test_local_override_loading_wins_over_environment() -> None:
    config = load_runtime_config(
        env={"VF_CODE_MODEL": "gpt-env"},
        overrides={
            "model": "gpt-local",
            "provider": "local-provider",
            "runs_dir": Path("local_runs/live"),
        },
    )

    assert config.model == "gpt-local"
    assert config.provider == "local-provider"
    assert config.paths.runs_dir == repository_root() / "local_runs" / "live"


def test_default_cost_rates_support_legacy_environment_aliases(monkeypatch) -> None:
    monkeypatch.setenv("VF_CODE_INPUT_COST_PER_MILLION", "2.5")
    monkeypatch.setenv("VF_CODE_OUTPUT_COST_PER_MILLION", "15")

    rates = default_cost_rates()

    assert rates.input_per_million == 2.5
    assert rates.output_per_million == 15.0


def test_invalid_env_values_raise_clear_errors() -> None:
    with pytest.raises(ConfigError, match="VF_CODE_INPUT_RATE"):
        load_runtime_config(env={"VF_CODE_INPUT_RATE": "not-a-number"})

    with pytest.raises(ConfigError, match="VF_CODE_REPORTS_DIR"):
        load_runtime_config(env={"VF_CODE_REPORTS_DIR": "   "})


def test_default_model_validates_blank_environment_value() -> None:
    with pytest.raises(ConfigError, match="VF_CODE_MODEL"):
        default_model(env={"VF_CODE_MODEL": "   "})
