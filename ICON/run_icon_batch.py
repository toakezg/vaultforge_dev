from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import shutil
import subprocess
import sys
import time
import uuid
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path


BATCH_HELPER_EXTENSIONS = {".bat", ".cfg", ".cmd", ".conf", ".ini", ".json", ".ps1", ".py"}
BATCH_STATE_FILENAME = ".batch-state.json"
LIST_ITEM_PATTERN = re.compile(r"^(?:[-*+]|\d+\.)\s+")
MARKDOWN_HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.*\S)\s*$")
MARKDOWN_PROMPT_EXTENSIONS = {".md", ".markdown"}
PLACEHOLDER_PATTERN = re.compile(r"\{([A-Za-z][A-Za-z0-9_-]*)\}")
POOL_EXTENSIONS = (".md", ".txt", ".markdown")
PROMPT_FILE_EXTENSIONS = {"", ".md", ".markdown", ".txt"}
RULE_PATTERN = re.compile(r"^[-*_]{3,}$")


@dataclass(frozen=True)
class PromptEntry:
    path: Path
    prompt_text: str


@dataclass(frozen=True)
class PoolDefinition:
    name: str
    path: Path
    entries: tuple[str, ...]


class IconBatchError(RuntimeError):
    pass


class PoolResolver:
    def __init__(self, pool_dirs: list[Path]) -> None:
        self.pool_dirs = pool_dirs
        self._cache: dict[str, PoolDefinition] = {}

    def get_pool(self, name: str) -> PoolDefinition:
        cached = self._cache.get(name)
        if cached is not None:
            return cached

        for pool_dir in self.pool_dirs:
            for extension in POOL_EXTENSIONS:
                candidate = pool_dir / f"{name}{extension}"
                if not candidate.is_file():
                    continue

                entries = tuple(load_pool_entries(candidate))
                if not entries:
                    raise IconBatchError(
                        f"Pool file is empty after cleanup for placeholder {{{name}}}: {candidate}"
                    )

                pool = PoolDefinition(name=name, path=candidate, entries=entries)
                self._cache[name] = pool
                return pool

        searched = ", ".join(str(path) for path in self.pool_dirs) or "(no pool folders found)"
        raise IconBatchError(
            f"Missing pool file for placeholder {{{name}}}. "
            f"Expected {name}.md or {name}.txt in: {searched}"
        )


def parse_args() -> tuple[argparse.Namespace, list[str]]:
    parser = argparse.ArgumentParser(
        description=(
            "Resolve ICON prompt placeholders from pool files, then hand the resolved batch "
            "to the external art generator."
        )
    )
    parser.add_argument("--batch", required=True, help="Source prompt folder.")
    parser.add_argument("--output-dir", required=True, help="Output folder for generated images.")
    parser.add_argument(
        "--art-root",
        default=r"E:\tools\image_generation\vaultforge-art",
        help="External art project root.",
    )
    parser.add_argument(
        "--python",
        dest="python_path",
        help="Override the Python executable used to run the external art generator.",
    )
    parser.add_argument(
        "--script",
        dest="script_path",
        help="Override the external art generator script path.",
    )
    parser.add_argument(
        "--pool-dir",
        action="append",
        default=[],
        help="Optional pool directory. Repeat to add more than one search location.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=1,
        help="Repeat the resolved batch this many times (default: 1).",
    )
    parser.add_argument(
        "--rerun",
        action="append",
        default=[],
        metavar="FILE",
        help="Pass through rerun targets for prompt files that should force a fresh generation.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Resolve placeholders and show generator output paths without calling the API.",
    )
    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="Keep the resolved temporary batch folders for inspection.",
    )
    args, forward_args = parser.parse_known_args()
    return args, forward_args


def resolve_path(value: str) -> Path:
    return Path(value).expanduser().resolve()


def ensure_file(path: Path, description: str) -> None:
    if not path.is_file():
        raise IconBatchError(f"{description} not found: {path}")


def ensure_dir(path: Path, description: str) -> None:
    if not path.is_dir():
        raise IconBatchError(f"{description} not found: {path}")


def strip_frontmatter(lines: list[str]) -> list[str]:
    if not lines or lines[0].strip() != "---":
        return lines

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return lines[index + 1 :]

    return lines


def extract_markdown_prompt_text(prompt_text: str) -> str:
    stripped = prompt_text.strip()
    if not stripped:
        return ""

    lines = strip_frontmatter(stripped.splitlines())
    while lines and not lines[0].strip():
        lines = lines[1:]

    if not lines:
        return ""

    heading_match = MARKDOWN_HEADING_PATTERN.match(lines[0].strip())
    if heading_match:
        remainder = "\n".join(lines[1:]).strip()
        if remainder:
            return remainder
        return heading_match.group(1).strip()

    return "\n".join(lines).strip()


def is_batch_prompt_file(path: Path) -> bool:
    if not path.is_file() or path.name.startswith("."):
        return False

    suffix = path.suffix.lower()
    if suffix in BATCH_HELPER_EXTENSIONS:
        return False

    return suffix in PROMPT_FILE_EXTENSIONS


def read_prompt_file(prompt_file: Path) -> PromptEntry | None:
    try:
        raw_text = prompt_file.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as error:
        raise IconBatchError(f"Prompt file is not valid UTF-8 text: {prompt_file}") from error

    if prompt_file.suffix.lower() in MARKDOWN_PROMPT_EXTENSIONS:
        prompt_text = extract_markdown_prompt_text(raw_text)
    else:
        prompt_text = raw_text.strip()

    if not prompt_text:
        print(f"Skipping empty prompt file: {prompt_file.name}", file=sys.stderr)
        return None

    return PromptEntry(path=prompt_file, prompt_text=prompt_text)


def load_prompt_entries(batch_dir: Path) -> list[PromptEntry]:
    ensure_dir(batch_dir, "Batch input folder")

    prompt_entries: list[PromptEntry] = []
    for prompt_file in sorted(path for path in batch_dir.iterdir() if is_batch_prompt_file(path)):
        prompt_entry = read_prompt_file(prompt_file)
        if prompt_entry is not None:
            prompt_entries.append(prompt_entry)

    if not prompt_entries:
        raise IconBatchError(
            "No usable prompt files were found in "
            f"{batch_dir}. Add one .txt, .md, .markdown, or extensionless prompt file."
        )

    return prompt_entries


def discover_pool_dirs(batch_dir: Path, explicit_pool_dirs: list[str]) -> list[Path]:
    pool_dirs: list[Path] = []
    seen: set[Path] = set()

    for raw_dir in explicit_pool_dirs:
        pool_dir = resolve_path(raw_dir)
        ensure_dir(pool_dir, "Pool folder")
        if pool_dir not in seen:
            pool_dirs.append(pool_dir)
            seen.add(pool_dir)

    current = batch_dir
    while True:
        candidate = (current / "pools").resolve()
        if candidate.is_dir() and candidate not in seen:
            pool_dirs.append(candidate)
            seen.add(candidate)

        if current.parent == current:
            break
        current = current.parent

    return pool_dirs


def load_pool_entries(pool_file: Path) -> list[str]:
    try:
        raw_text = pool_file.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as error:
        raise IconBatchError(f"Pool file is not valid UTF-8 text: {pool_file}") from error

    lines = strip_frontmatter(raw_text.splitlines())
    entries: list[str] = []
    for raw_line in lines:
        line = raw_line.strip()
        if not line or RULE_PATTERN.match(line):
            continue
        if line.startswith("#"):
            continue

        line = LIST_ITEM_PATTERN.sub("", line).strip()
        if not line:
            continue

        entries.append(line)

    return entries


def find_placeholders(prompt_text: str) -> list[str]:
    return sorted(set(PLACEHOLDER_PATTERN.findall(prompt_text)))


def resolve_prompt_text(
    prompt_text: str,
    placeholder_names: list[str],
    resolver: PoolResolver,
    rng: random.Random,
) -> tuple[str, dict[str, str], dict[str, Path]]:
    replacements: dict[str, str] = {}
    pool_paths: dict[str, Path] = {}

    for name in placeholder_names:
        pool = resolver.get_pool(name)
        replacements[name] = rng.choice(pool.entries)
        pool_paths[name] = pool.path

    resolved_prompt = PLACEHOLDER_PATTERN.sub(lambda match: replacements[match.group(1)], prompt_text)
    return resolved_prompt, replacements, pool_paths


def normalize_rerun_targets(values: list[str]) -> set[str]:
    return {value.strip().lower() for value in values if value and value.strip()}


def load_wrapper_state(batch_dir: Path) -> dict[str, dict[str, object]]:
    state_path = batch_dir / BATCH_STATE_FILENAME
    if not state_path.is_file():
        return {}

    try:
        raw_data = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    entries = raw_data.get("entries", {})
    if not isinstance(entries, dict):
        return {}

    normalized: dict[str, dict[str, object]] = {}
    for key, value in entries.items():
        if isinstance(key, str) and isinstance(value, dict):
            normalized[key] = dict(value)
    return normalized


def save_wrapper_state(batch_dir: Path, entries: dict[str, dict[str, object]]) -> None:
    state_path = batch_dir / BATCH_STATE_FILENAME
    payload = {
        "version": 1,
        "entries": entries,
    }
    state_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def wait_for_file(path: Path, *, timeout_seconds: float = 5.0, interval_seconds: float = 0.25) -> bool:
    deadline = time.time() + timeout_seconds
    while time.time() <= deadline:
        if path.is_file():
            return True
        time.sleep(interval_seconds)
    return path.is_file()


def matches_rerun_target(prompt_entry: PromptEntry, rerun_targets: set[str]) -> bool:
    return (
        prompt_entry.path.name.lower() in rerun_targets
        or prompt_entry.path.stem.lower() in rerun_targets
    )


def build_wrapper_request_hash(prompt_text: str, output_dir: Path, forward_args: list[str]) -> str:
    payload = {
        "forward_args": list(forward_args),
        "output_dir": str(output_dir),
        "prompt_text": prompt_text,
    }
    serialized = json.dumps(payload, sort_keys=True)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def verify_generated_outputs(
    temp_batch_dir: Path,
    runnable_entries: list[tuple[str, str]],
) -> dict[str, dict[str, object]]:
    temp_state = load_wrapper_state(temp_batch_dir)
    missing_outputs: list[str] = []

    for file_name, _ in runnable_entries:
        temp_entry = temp_state.get(file_name)
        if not isinstance(temp_entry, dict):
            missing_outputs.append(f"{file_name}: missing batch-state entry")
            continue

        last_output = temp_entry.get("last_output")
        if not isinstance(last_output, str) or not last_output.strip():
            missing_outputs.append(f"{file_name}: missing last_output")
            continue

        output_path = Path(last_output)
        if not wait_for_file(output_path):
            missing_outputs.append(f"{file_name}: output file not found at {output_path}")

    if missing_outputs:
        raise IconBatchError(
            "Art generator reported success, but expected output files were missing: "
            + "; ".join(missing_outputs)
        )

    return temp_state


def validate_rerun_targets(rerun_targets: set[str], prompt_entries: list[PromptEntry]) -> None:
    if not rerun_targets:
        return

    matched_targets: set[str] = set()
    for prompt_entry in prompt_entries:
        aliases = {prompt_entry.path.name.lower(), prompt_entry.path.stem.lower()}
        matched_targets.update(rerun_targets & aliases)

    missing_targets = sorted(rerun_targets - matched_targets)
    if missing_targets:
        raise IconBatchError(
            "Rerun target(s) not found in the ICON batch folder: " + ", ".join(missing_targets)
        )


def print_resolved_values(
    pass_index: int,
    limit: int,
    batch_dir: Path,
    resolved_logs: list[tuple[str, dict[str, str], dict[str, Path]]],
) -> None:
    print("")
    print(f"ICON wrapper pass {pass_index}/{limit}: {batch_dir}")
    if not resolved_logs:
        print("  No placeholders detected in this batch.")
        return

    for file_name, replacements, pool_paths in resolved_logs:
        print(f"  {file_name}")
        for name in sorted(replacements):
            print(f"    {name}={replacements[name]}  ({pool_paths[name].name})")


def build_engine_command(
    *,
    python_path: Path,
    script_path: Path,
    temp_batch_dir: Path,
    output_dir: Path,
    dry_run: bool,
    forward_args: list[str],
) -> list[str]:
    command = [
        str(python_path),
        str(script_path),
        "--batch",
        str(temp_batch_dir),
        "--output-dir",
        str(output_dir),
    ]

    if dry_run:
        command.append("--dry-run")

    command.extend(forward_args)

    return command


def create_temp_root(batch_dir: Path) -> Path:
    local_temp_base = batch_dir.parent / ".icon-wrapper-temp"
    local_temp_base.mkdir(parents=True, exist_ok=True)
    temp_root = local_temp_base / f"vaultforge-icon-batch-{uuid.uuid4().hex}"
    temp_root.mkdir(parents=True, exist_ok=False)
    return temp_root


def main() -> int:
    try:
        args, forward_args = parse_args()

        if args.limit < 1:
            raise IconBatchError("--limit must be 1 or greater.")

        batch_dir = resolve_path(args.batch)
        output_dir = resolve_path(args.output_dir)
        art_root = resolve_path(args.art_root)
        python_path = resolve_path(args.python_path) if args.python_path else art_root / ".venv" / "Scripts" / "python.exe"
        script_path = resolve_path(args.script_path) if args.script_path else art_root / "generate_art.py"

        ensure_dir(batch_dir, "Batch input folder")
        output_dir.mkdir(parents=True, exist_ok=True)
        ensure_dir(art_root, "Art project root")
        ensure_file(python_path, "Art Python executable")
        ensure_file(script_path, "Art generator script")

        prompt_entries = load_prompt_entries(batch_dir)
        rerun_targets = normalize_rerun_targets(args.rerun)
        validate_rerun_targets(rerun_targets, prompt_entries)

        pool_dirs = discover_pool_dirs(batch_dir, args.pool_dir)
        resolver = PoolResolver(pool_dirs)

        placeholders_by_file: dict[str, list[str]] = {}
        auto_rerun_targets: set[str] = set()
        for prompt_entry in prompt_entries:
            placeholder_names = find_placeholders(prompt_entry.prompt_text)
            placeholders_by_file[prompt_entry.path.name] = placeholder_names
            if placeholder_names:
                auto_rerun_targets.add(prompt_entry.path.stem.lower())
                for placeholder_name in placeholder_names:
                    resolver.get_pool(placeholder_name)

        temp_root = create_temp_root(batch_dir)

        print(f"ICON source batch: {batch_dir}")
        print(f"ICON output dir: {output_dir}")
        print(f"ICON pool dirs: {', '.join(str(path) for path in pool_dirs) or '(none)'}")
        print(f"ICON loop limit: {args.limit}")
        if rerun_targets:
            print(f"ICON user reruns: {', '.join(sorted(rerun_targets))}")
        if auto_rerun_targets:
            print(f"ICON placeholder reruns: {', '.join(sorted(auto_rerun_targets))}")
        print(f"ICON temp root: {temp_root}")
        sys.stdout.flush()

        rng = random.Random()
        source_state = load_wrapper_state(batch_dir)

        try:
            for pass_index in range(1, args.limit + 1):
                temp_batch_dir = temp_root / f"pass-{pass_index:02d}"
                temp_batch_dir.mkdir(parents=True, exist_ok=True)

                resolved_logs: list[tuple[str, dict[str, str], dict[str, Path]]] = []
                runnable_entries: list[tuple[str, str]] = []
                skipped_entries: list[str] = []

                for prompt_entry in prompt_entries:
                    placeholder_names = placeholders_by_file[prompt_entry.path.name]
                    resolved_prompt = prompt_entry.prompt_text
                    replacements: dict[str, str] = {}
                    pool_paths: dict[str, Path] = {}
                    if placeholder_names:
                        resolved_prompt, replacements, pool_paths = resolve_prompt_text(
                            prompt_entry.prompt_text,
                            placeholder_names,
                            resolver,
                            rng,
                        )
                        resolved_logs.append((prompt_entry.path.name, replacements, pool_paths))

                    request_hash = build_wrapper_request_hash(
                        resolved_prompt,
                        output_dir,
                        forward_args,
                    )
                    force_run = (
                        matches_rerun_target(prompt_entry, rerun_targets)
                        or prompt_entry.path.stem.lower() in auto_rerun_targets
                    )
                    previous_entry = source_state.get(prompt_entry.path.name, {})
                    if not force_run and previous_entry.get("request_hash") == request_hash:
                        skipped_entries.append(prompt_entry.path.name)
                        continue

                    (temp_batch_dir / prompt_entry.path.name).write_text(
                        resolved_prompt,
                        encoding="utf-8",
                    )
                    runnable_entries.append((prompt_entry.path.name, request_hash))

                print_resolved_values(pass_index, args.limit, batch_dir, resolved_logs)
                for file_name in skipped_entries:
                    print(f"  Skipping unchanged prompt file: {file_name}")
                sys.stdout.flush()

                if not runnable_entries:
                    status = "dry run" if args.dry_run else "live run"
                    print(
                        f"ICON wrapper pass {pass_index}/{args.limit}: no prompt files need generation "
                        f"for this {status}."
                    )
                    continue

                command = build_engine_command(
                    python_path=python_path,
                    script_path=script_path,
                    temp_batch_dir=temp_batch_dir,
                    output_dir=output_dir,
                    dry_run=args.dry_run,
                    forward_args=forward_args,
                )
                sys.stdout.flush()

                completed = subprocess.run(command, check=False)
                if completed.returncode != 0:
                    return completed.returncode

                temp_state = {} if args.dry_run else verify_generated_outputs(temp_batch_dir, runnable_entries)
                now = datetime.now().isoformat(timespec="seconds")
                for file_name, request_hash in runnable_entries:
                    temp_entry = dict(temp_state.get(file_name, {}))
                    temp_entry["last_run_at"] = temp_entry.get("last_run_at", now)
                    temp_entry["request_hash"] = request_hash
                    source_state[file_name] = temp_entry

                if not args.dry_run:
                    save_wrapper_state(batch_dir, source_state)

            return 0
        finally:
            if not args.keep_temp and temp_root.exists():
                shutil.rmtree(temp_root, ignore_errors=True)
    except IconBatchError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
