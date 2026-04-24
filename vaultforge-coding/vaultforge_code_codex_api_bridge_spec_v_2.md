# VaultForge-Code — Codex API Bridge (v2)

## Goal
Create a `vaultforge-code` bridge that lets VaultForge run Codex-style coding and automation tasks through an OpenAI API key instead of ChatGPT/Codex weekly limits.

`vaultforge-code` should stay focused on the **work/execution side** of the ecosystem.

That means it is responsible for:
- task execution
- API-backed coding assistance
- project context gathering
- run logging
- usage tracking
- structured event emission for other VaultForge sections

It should **not** own the deeper XP4Life interpretation layer.
That belongs in a separate sibling section: `vaultforge-xp4l`.

---

## Boundary
### `vaultforge-code` owns
- coding task bridge
- OpenAI API calls
- CLI commands and batch launchers
- run manifests
- usage/cost tracking
- context building from project files
- structured activity events

### `vaultforge-xp4l` owns
- XP calculation
- quest generation
- achievement detection
- reward generation
- rarity/prestige heuristics
- Obsidian/XP4Life injection logic
- dashboard/game-system interpretation

### Relationship
`vaultforge-code` should report **what happened**.
`vaultforge-xp4l` should decide **what it means**.

---

## Primary use cases
1. Send a coding task prompt to the API.
2. Provide repo/project context from local files.
3. Save outputs to a run folder with logs and metadata.
4. Optionally write generated code/artifacts into a target folder later.
5. Track token/cost usage per run.
6. Emit structured activity events that can later be consumed by `vaultforge-xp4l`.
7. Support named presets such as `review`, `implement`, `tighten`, `audit`, `scaffold`.

---

## Proposed folder structure
```text
vaultforge-code/
  README.md
  SYSTEM.md
  CODEX_START.md
  VERIFICATION.md
  pyproject.toml
  requirements.txt
  .env.example
  run_code_bridge.bat
  open_code_venv_terminal.bat
  src/
    vf_code_bridge/
      __init__.py
      cli.py
      config.py
      bridge.py
      prompts.py
      context_builder.py
      usage_tracker.py
      event_writer.py
      file_ops.py
      models.py
  assets/
    prompts/
      review.md
      implement.md
      tighten.md
      audit.md
      scaffold.md
    runs/
      .gitkeep
    reports/
      .gitkeep
    events/
      .gitkeep
  tests/
    test_config.py
    test_context_builder.py
    test_usage_tracker.py
    test_event_writer.py
```

---

## MVP behavior
### Command example
```bat
run_code_bridge.bat implement --task "Add usage tracking JSON summaries to vaultforge-business" --project-root "E:\tools\vaultforge"
```

### CLI flags
- `mode` — preset/mode name (`review`, `implement`, `tighten`, `audit`, `scaffold`)
- `--task` — main instruction
- `--project-root` — project or repo root to inspect
- `--context` — optional extra context file/note
- `--output-dir` — optional output location
- `--model` — optional override
- `--dry-run` — do everything except call API
- `--save-prompt` — save compiled prompt text
- `--json` — request structured JSON output where appropriate
- `--max-files` — cap number of files loaded into context
- `--include` — glob/include hints
- `--exclude` — glob/exclude hints
- `--emit-event` — write a structured activity event after the run

---

## Execution flow
1. Load config from environment and defaults.
2. Read preset prompt template.
3. Build context from chosen files under project root.
4. Compile final instruction package.
5. Call OpenAI Responses API.
6. Save:
   - compiled prompt
   - raw response text
   - metadata JSON
   - usage JSON
   - summary markdown
7. Emit a structured event JSON for downstream systems.
8. Print a clean terminal summary.

---

## Suggested environment variables
```env
OPENAI_API_KEY=
VF_CODE_MODEL=gpt-5.4-mini
VF_CODE_ROOT=E:\tools\vaultforge\vaultforge-code
VF_CODE_RUNS_DIR=E:\tools\vaultforge\vaultforge-code\assets\runs
VF_CODE_REPORTS_DIR=E:\tools\vaultforge\vaultforge-code\assets\reports
VF_CODE_EVENTS_DIR=E:\tools\vaultforge\vaultforge-code\assets\events
VF_CODE_DEFAULT_MAX_FILES=20
VF_CODE_DEFAULT_MAX_CHARS=120000
```

---

## Output per run
Each run gets a timestamped folder:
```text
assets/runs/2026-04-16_213000_implement/
  prompt.txt
  response.txt
  response.json
  usage.json
  summary.md
  context_manifest.json
  event.json
```

### `summary.md` should contain
- mode
- task
- model
- project root
- files used for context
- token usage
- estimated cost
- output file list
- short human-readable result summary

---

## Structured event output
The bridge should emit an event that other systems can consume.

### Example event
```json
{
  "event_type": "run_completed",
  "timestamp": "2026-04-16T21:30:00+10:00",
  "section": "vaultforge-code",
  "mode": "implement",
  "task": "Add usage tracking JSON summaries to vaultforge-business",
  "project_root": "E:\\tools\\vaultforge",
  "files_used": [
    "vaultforge-business/README.md",
    "vaultforge-business/run_business.ps1"
  ],
  "input_tokens": 4200,
  "output_tokens": 1100,
  "total_tokens": 5300,
  "estimated_cost": 0.37,
  "duration_seconds": 92,
  "tags": ["code", "implement", "tracking", "vaultforge"]
}
```

This event is the handoff surface for `vaultforge-xp4l`.

---

## Safety defaults
- default to read-only generation unless a write-capable phase is added later
- never overwrite files in MVP
- save all prompts/responses for traceability
- always write usage metadata
- clamp context size to avoid runaway cost
- activity events should be append-only and traceable

---

## Usage tracking requirements
Track at minimum:
- timestamp
- mode
- model
- task
- input tokens
- output tokens
- total tokens
- estimated cost
- duration
- project root
- whether event emission succeeded

Also maintain append-only aggregate files:
- `assets/reports/usage_log.jsonl`
- `assets/reports/run_log.jsonl`
- `assets/reports/usage_summary.md`

---

## Event requirements for XP4L handoff
Every completed run should be able to emit a compact event record for `vaultforge-xp4l`.

Suggested fields:
- event_type
- timestamp
- section
- mode
- task
- summary
- project_root
- files_used
- tags
- duration_seconds
- token usage
- estimated_cost
- optional notes

These events should remain neutral/factual.
They should not attempt to calculate XP or achievements inside `vaultforge-code`.

---

## Revised implementation order
### Phase 0
- config loader
- CLI entry
- usage tracker
- run manifest writer
- event writer

### Phase 1
- code-task bridge modes (`review`, `implement`, `tighten`, `audit`, `scaffold`)
- context builder
- prompt loader
- saved run artifacts

### Phase 2
- optional patch writer
- diff generation
- approval mode before write
- batch/queue mode
- richer downstream event shaping

### Out of scope for this section
- XP formulas
- quest generation
- achievement unlocking
- reward generation
- XP4Life dashboard injection

Those belong in `vaultforge-xp4l`.

---

## Build prompt for Codex
```text
Build a new local-first Python project section named `vaultforge-code` inside the VaultForge ecosystem.

Goal:
Create a Codex API Bridge that runs coding tasks through an OpenAI API key using the Responses API, so I can keep working when ChatGPT/Codex weekly limits are low.

Important boundary:
- `vaultforge-code` owns execution, logging, usage tracking, and structured event emission.
- `vaultforge-code` must NOT own XP calculation, quest generation, achievements, rewards, or XP4Life dashboard injection.
- Those belong in a separate sibling section: `vaultforge-xp4l`.

Requirements:
- Windows-friendly
- Python project with venv-friendly structure
- runnable from batch file
- clean README, SYSTEM, and CODEX_START docs
- local run folders with saved prompt, response, metadata, usage, summary, and event files
- usage/cost tracking per run plus aggregate JSONL logs
- modular code split into config, CLI, context builder, bridge caller, usage tracker, and event writer
- support modes/presets: review, implement, tighten, audit, scaffold
- safe default behavior: no direct file overwrite in MVP
- include tests for config loading, context building, usage tracking, and event writing

Implementation details:
- use the official OpenAI Python SDK
- use environment variable `OPENAI_API_KEY`
- default model should be configurable with a sensible code-oriented default
- compile prompt from a preset + task + selected file contents from a project root
- save every run into `assets/runs/<timestamp>_<mode>/`
- maintain `assets/reports/usage_log.jsonl`
- maintain structured event output under `assets/events/` or per-run `event.json`
- create `run_code_bridge.bat`
- create `.env.example`
- include clear verification notes

Deliverables:
- working Python package under `src/vf_code_bridge`
- batch launcher
- docs
- smoke-testable CLI example
- clear verification notes

Do not modify unrelated VaultForge sections.
Keep this isolated to `vaultforge-code`.
Prefer practical MVP over over-engineering.
```

