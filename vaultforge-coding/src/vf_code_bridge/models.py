"""Shared dataclasses for the VaultForge Code bridge."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class BridgePaths:
    """Known package and asset paths for the bridge."""

    workspace_root: Path
    package_root: Path
    assets_dir: Path
    prompts_dir: Path
    runs_root_dir: Path
    runs_dir: Path
    runs_examples_dir: Path
    reports_dir: Path
    events_dir: Path
    events_log_path: Path
    usage_summary_path: Path


@dataclass(frozen=True, slots=True)
class CostRates:
    """Simple per-million token rates used for local cost estimates."""

    input_per_million: float
    output_per_million: float


@dataclass(frozen=True, slots=True)
class RuntimeConfig:
    """Normalized runtime configuration for the local bridge."""

    section_name: str
    thread_name: str
    provider: str
    model: str
    cost_rates: CostRates
    paths: BridgePaths


@dataclass(frozen=True, slots=True)
class CliRequest:
    """CLI inputs captured for a future bridge run."""

    mode: str
    task: str
    project_root: Path | None = None
    context: Path | None = None
    output_dir: Path | None = None
    model: str | None = None
    dry_run: bool = False
    save_prompt: bool = False
    json_output: bool = False
    max_files: int | None = None
    include: tuple[str, ...] = ()
    exclude: tuple[str, ...] = ()
    emit_event: bool = True
    provider: str | None = None
    input_tokens: int | None = None
    output_tokens: int | None = None
    total_tokens: int | None = None
    duration_ms: int | None = None
    notes: str = ""
    usage_payload: dict[str, object] | None = None


@dataclass(frozen=True, slots=True)
class PromptTemplate:
    """Named prompt template location."""

    mode: str
    path: Path


@dataclass(frozen=True, slots=True)
class UsageSnapshot:
    """Normalized token, duration, and cost values for one run."""

    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    estimated_cost: float = 0.0
    duration_ms: int = 0


@dataclass(frozen=True, slots=True)
class RunRecord:
    """One local run artifact written under ``assets/runs``."""

    run_id: str
    timestamp: str
    section: str
    thread: str
    task_type: str
    prompt_name: str
    status: str
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    estimated_cost: float
    duration_ms: int
    files_read: tuple[str, ...] = ()
    files_written: tuple[str, ...] = ()
    notes: str = ""


@dataclass(frozen=True, slots=True)
class EventRecord:
    """One JSONL event entry emitted during a run lifecycle."""

    event_type: str
    timestamp: str
    run_id: str
    section: str
    thread: str
    task_type: str
    prompt_name: str
    status: str
    model: str
    provider: str
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    estimated_cost: float = 0.0
    duration_ms: int = 0
    notes: str = ""


@dataclass(frozen=True, slots=True)
class SectionSummary:
    """Aggregate usage summary rebuilt from local run artifacts."""

    section: str
    thread: str
    generated_at: str
    total_runs: int = 0
    completed_runs: int = 0
    failed_runs: int = 0
    other_runs: int = 0
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_tokens: int = 0
    total_estimated_cost: float = 0.0
    last_run_id: str = ""
    last_status: str = ""
    last_timestamp: str = ""
    models: tuple[str, ...] = ()
    providers: tuple[str, ...] = ()
