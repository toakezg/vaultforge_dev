"""Environment-backed configuration loading for the local bridge."""

from __future__ import annotations

import math
import os
from collections.abc import Mapping
from pathlib import Path

from .models import BridgePaths, CostRates, RuntimeConfig

DEFAULT_MODEL = "gpt-5.4-mini"
DEFAULT_PROVIDER = "openai"
DEFAULT_SECTION_NAME = "vaultforge-code"
DEFAULT_THREAD_NAME = "vaultforge-coding"
DEFAULT_MAX_FILES = 20
DEFAULT_MAX_CHARS = 120_000
DEFAULT_INPUT_RATE = 1.25
DEFAULT_OUTPUT_RATE = 10.0


class ConfigError(ValueError):
    """Raised when environment or local config input is invalid."""


def repository_root() -> Path:
    """Return the local section root."""

    return Path(__file__).resolve().parents[2]


def _env_source(env: Mapping[str, str] | None) -> Mapping[str, str]:
    """Return the active environment source."""

    return os.environ if env is None else env


def _overrides_source(
    overrides: Mapping[str, object] | None,
) -> Mapping[str, object]:
    """Return the active local override source."""

    return {} if overrides is None else overrides


def _first_present(
    mapping: Mapping[str, object],
    keys: tuple[str, ...],
) -> object | None:
    """Return the first present non-``None`` value from a mapping."""

    for key in keys:
        if key in mapping and mapping[key] is not None:
            return mapping[key]
    return None


def _normalized_text(value: object, *, label: str) -> str:
    """Normalize a required text setting."""

    text = str(value).strip()
    if not text:
        raise ConfigError(f"{label} must not be empty.")
    return text


def _normalized_rate(value: object, *, label: str) -> float:
    """Normalize a non-negative finite rate value."""

    try:
        rate = float(value)
    except (TypeError, ValueError) as exc:
        raise ConfigError(f"{label} must be a valid number.") from exc
    if not math.isfinite(rate):
        raise ConfigError(f"{label} must be finite.")
    if rate < 0:
        raise ConfigError(f"{label} must be zero or greater.")
    return rate


def _normalized_path(value: object, *, label: str, root: Path) -> Path:
    """Normalize a configurable path value into an absolute path."""

    if isinstance(value, Path):
        candidate = value
    else:
        text = str(value).strip()
        if not text:
            raise ConfigError(f"{label} must not be empty.")
        candidate = Path(text)
    if not candidate.is_absolute():
        candidate = root / candidate
    return candidate.resolve()


def _read_text_setting(
    primary_env: str,
    *,
    default: str,
    env: Mapping[str, str],
    overrides: Mapping[str, object],
    env_aliases: tuple[str, ...] = (),
    override_keys: tuple[str, ...] = (),
) -> str:
    """Read one normalized text setting from overrides, env, or default."""

    override_value = _first_present(
        overrides,
        override_keys + (primary_env,) + env_aliases,
    )
    if override_value is not None:
        return _normalized_text(override_value, label=primary_env)

    env_value = _first_present(env, (primary_env,) + env_aliases)
    if env_value is None:
        return default
    return _normalized_text(env_value, label=primary_env)


def _read_rate_setting(
    primary_env: str,
    *,
    default: float,
    env: Mapping[str, str],
    overrides: Mapping[str, object],
    env_aliases: tuple[str, ...] = (),
    override_keys: tuple[str, ...] = (),
) -> float:
    """Read one normalized numeric rate setting."""

    override_value = _first_present(
        overrides,
        override_keys + (primary_env,) + env_aliases,
    )
    if override_value is not None:
        return _normalized_rate(override_value, label=primary_env)

    env_value = _first_present(env, (primary_env,) + env_aliases)
    if env_value is None:
        return default
    return _normalized_rate(env_value, label=primary_env)


def _read_path_setting(
    primary_env: str,
    *,
    default: Path,
    root: Path,
    env: Mapping[str, str],
    overrides: Mapping[str, object],
    env_aliases: tuple[str, ...] = (),
    override_keys: tuple[str, ...] = (),
) -> Path:
    """Read one normalized path setting."""

    override_value = _first_present(
        overrides,
        override_keys + (primary_env,) + env_aliases,
    )
    if override_value is not None:
        return _normalized_path(override_value, label=primary_env, root=root)

    env_value = _first_present(env, (primary_env,) + env_aliases)
    if env_value is None:
        return default.resolve()
    return _normalized_path(env_value, label=primary_env, root=root)


def load_runtime_config(
    *,
    root: Path | None = None,
    env: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
) -> RuntimeConfig:
    """Load normalized runtime config from defaults, env, and local overrides."""

    workspace_root = (root or repository_root()).resolve()
    env_source = _env_source(env)
    override_source = _overrides_source(overrides)
    assets_dir = workspace_root / "assets"

    section_name = _read_text_setting(
        "VF_CODE_SECTION_NAME",
        default=DEFAULT_SECTION_NAME,
        env=env_source,
        overrides=override_source,
        env_aliases=("VF_CODE_SECTION",),
        override_keys=("section_name", "section"),
    )
    thread_name = _read_text_setting(
        "VF_CODE_THREAD",
        default=DEFAULT_THREAD_NAME,
        env=env_source,
        overrides=override_source,
        override_keys=("thread_name", "thread"),
    )
    provider = _read_text_setting(
        "VF_CODE_PROVIDER",
        default=DEFAULT_PROVIDER,
        env=env_source,
        overrides=override_source,
        override_keys=("provider",),
    )
    model = _read_text_setting(
        "VF_CODE_MODEL",
        default=DEFAULT_MODEL,
        env=env_source,
        overrides=override_source,
        override_keys=("model",),
    )
    input_rate = _read_rate_setting(
        "VF_CODE_INPUT_RATE",
        default=DEFAULT_INPUT_RATE,
        env=env_source,
        overrides=override_source,
        env_aliases=("VF_CODE_INPUT_COST_PER_MILLION",),
        override_keys=("input_rate", "input_per_million"),
    )
    output_rate = _read_rate_setting(
        "VF_CODE_OUTPUT_RATE",
        default=DEFAULT_OUTPUT_RATE,
        env=env_source,
        overrides=override_source,
        env_aliases=("VF_CODE_OUTPUT_COST_PER_MILLION",),
        override_keys=("output_rate", "output_per_million"),
    )

    prompts_dir = _read_path_setting(
        "VF_CODE_PROMPTS_DIR",
        default=assets_dir / "prompts",
        root=workspace_root,
        env=env_source,
        overrides=override_source,
        override_keys=("prompts_dir",),
    )
    runs_dir = _read_path_setting(
        "VF_CODE_RUNS_DIR",
        default=assets_dir / "runs" / "live",
        root=workspace_root,
        env=env_source,
        overrides=override_source,
        override_keys=("runs_dir",),
    )
    events_dir = _read_path_setting(
        "VF_CODE_EVENTS_DIR",
        default=assets_dir / "events",
        root=workspace_root,
        env=env_source,
        overrides=override_source,
        override_keys=("events_dir",),
    )
    reports_dir = _read_path_setting(
        "VF_CODE_REPORTS_DIR",
        default=assets_dir / "reports",
        root=workspace_root,
        env=env_source,
        overrides=override_source,
        override_keys=("reports_dir",),
    )

    runs_root_dir = runs_dir.parent
    paths = BridgePaths(
        workspace_root=workspace_root,
        package_root=workspace_root / "src" / "vf_code_bridge",
        assets_dir=assets_dir,
        prompts_dir=prompts_dir,
        runs_root_dir=runs_root_dir,
        runs_dir=runs_dir,
        runs_examples_dir=runs_root_dir / "examples",
        reports_dir=reports_dir,
        events_dir=events_dir,
        events_log_path=events_dir / "events.jsonl",
        usage_summary_path=reports_dir / "usage_summary.json",
    )
    return RuntimeConfig(
        section_name=section_name,
        thread_name=thread_name,
        provider=provider,
        model=model,
        cost_rates=CostRates(
            input_per_million=input_rate,
            output_per_million=output_rate,
        ),
        paths=paths,
    )


def default_section(
    env: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
) -> str:
    """Return the normalized section name."""

    return _read_text_setting(
        "VF_CODE_SECTION_NAME",
        default=DEFAULT_SECTION_NAME,
        env=_env_source(env),
        overrides=_overrides_source(overrides),
        env_aliases=("VF_CODE_SECTION",),
        override_keys=("section_name", "section"),
    )


def default_thread(
    env: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
) -> str:
    """Return the normalized thread name."""

    return _read_text_setting(
        "VF_CODE_THREAD",
        default=DEFAULT_THREAD_NAME,
        env=_env_source(env),
        overrides=_overrides_source(overrides),
        override_keys=("thread_name", "thread"),
    )


def default_provider(
    env: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
) -> str:
    """Return the normalized provider value."""

    return _read_text_setting(
        "VF_CODE_PROVIDER",
        default=DEFAULT_PROVIDER,
        env=_env_source(env),
        overrides=_overrides_source(overrides),
        override_keys=("provider",),
    )


def default_model(
    env: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
) -> str:
    """Return the normalized model value."""

    return _read_text_setting(
        "VF_CODE_MODEL",
        default=DEFAULT_MODEL,
        env=_env_source(env),
        overrides=_overrides_source(overrides),
        override_keys=("model",),
    )


def default_cost_rates(
    env: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
) -> CostRates:
    """Return the normalized token-rate fields."""

    config = load_runtime_config(env=env, overrides=overrides)
    return config.cost_rates


def default_paths(
    root: Path | None = None,
    env: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
) -> BridgePaths:
    """Return normalized asset and package paths."""

    config = load_runtime_config(root=root, env=env, overrides=overrides)
    return config.paths
