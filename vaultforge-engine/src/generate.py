from __future__ import annotations

import argparse
import base64
from dataclasses import dataclass
import hashlib
import json
import mimetypes
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Iterable

from openai import APIError, OpenAI


MODULE_DIR = Path(__file__).resolve().parent
DEFAULT_PROJECT_ROOT = MODULE_DIR.parent if MODULE_DIR.name == "src" else MODULE_DIR
PROJECT_ROOT_ENV_VAR = "VAULTFORGE_ENGINE_PROJECT_ROOT"


def get_project_root() -> Path:
    root_override = os.getenv(PROJECT_ROOT_ENV_VAR)
    if root_override:
        return Path(root_override).expanduser().resolve()
    return DEFAULT_PROJECT_ROOT


PROJECT_ROOT = get_project_root()
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "assets" / "generated"
DEFAULT_GALLERY_INDEX_PATH = PROJECT_ROOT / "assets" / "gallery-index.json"
DEFAULT_BATCH_INPUT_DIR = PROJECT_ROOT / "assets" / "batch-input"
DEFAULT_SMOKE_BATCH_INPUT_DIR = PROJECT_ROOT / "assets" / "batch-input-smoke"
DEFAULT_ENV_FILE = PROJECT_ROOT / ".env"
BATCH_STATE_FILENAME = ".batch-state.json"
GALLERY_INDEX_VERSION = 1
DEFAULT_MODEL = "gpt-image-2-2026-04-21"
DEFAULT_FALLBACK_MODELS = ("gpt-image-2", "gpt-5.5", "gpt-5.2")
SUPPORTED_FORMATS = {"png", "jpeg", "webp"}
SUPPORTED_INPUT_IMAGE_EXTENSIONS = {".gif", ".ico", ".jpeg", ".jpg", ".png", ".svg", ".webp"}
INPUT_IMAGE_MIME_TYPES = {
    ".ico": "image/x-icon",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".webp": "image/webp",
}
PROMPT_FILE_EXTENSIONS = {"", ".md", ".markdown", ".txt"}
MARKDOWN_PROMPT_EXTENSIONS = {".md", ".markdown"}
BATCH_HELPER_EXTENSIONS = {".bat", ".cfg", ".cmd", ".conf", ".ini", ".json", ".ps1"}
API_KEY_ENV_VAR = "VAULTFORGE_ENGINE_OPENAI_API_KEY"
API_KEY_ENV_VARS = (
    API_KEY_ENV_VAR,
    "IMAGE_GENERATION_KEY_B_OPENAI_API_KEY",
    "OPENAI_API_KEY",
)
GPT_IMAGE_MODEL_PREFIXES = ("gpt-image-", "chatgpt-image")
STYLE_PROMPTS = {
    "fine-line": "fine-line illustration, delicate contours, sparse shading, precise ornamental detail",
    "geometric": "geometric construction, crisp vector-like edges, balanced shapes, strong symbolic clarity",
    "cinematic": "cinematic lighting, dramatic framing, rich atmosphere, polished concept-art finish",
    "painterly": "painterly brushwork, layered textures, expressive strokes, artbook quality",
    "mystica": "mystical symbolism, arcane ornament, luminous sigils, ethereal ritual atmosphere",
    "photoreal": "photoreal detail, grounded materials, natural lighting, realistic lens treatment",
    "blueprint": "clean blueprint styling, annotated design language, crisp linework, technical presentation",
    "pixel": "pixel-art rendering, deliberate sprite-era shapes, limited palette discipline, readable silhouettes",
    "dreamlike": "dreamlike mood, surreal color harmonies, soft glow, evocative fantasy imagery",
    "renaissance-soft-light": "renaissance-inspired composition, soft directional light, luminous skin tones, gentle sacred-painting atmosphere",
}
PRESET_PROMPTS = {
    "icon": "single centered icon subject, clean emblem silhouette, minimal background distraction, readable small-format design",
    "vaultforge": "fantasy forge aesthetics, relic-crafting motifs, ancient vault architecture, premium key art composition",
    "artifact-card": "centered artifact subject, clear silhouette, collectible-card readability, subtle backdrop support",
    "obsidian-cover": "strong cover-image composition, bold focal subject, readable negative space, moody editorial finish",
    "sacred-scene": "sacred tableau composition, reverent symbolism, ceremonial details, serene focal storytelling",
}
MOOD_PROMPTS = {
    "peaceful": "peaceful emotional tone, calm stillness, soft visual rhythm, restorative atmosphere",
    "hopeful": "hopeful emotional tone, uplifting light, quiet optimism, forward-looking warmth",
    "compassionate": "compassionate emotional tone, tender presence, humane warmth, gentle emotional clarity",
}

MARKDOWN_HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.*\S)\s*$")
MARKDOWN_IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
WIKI_IMAGE_PATTERN = re.compile(r"!\[\[([^|\]#]+)(?:[#|][^\]]*)?\]\]")
HTML_IMAGE_PATTERN = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"'][^>]*>", re.IGNORECASE)


@dataclass(frozen=True)
class ImageReference:
    path: Path
    source: str

class ConfigFileArgumentParser(argparse.ArgumentParser):
    def convert_arg_line_to_args(self, arg_line: str) -> list[str]:
        stripped = arg_line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith(";"):
            return []

        option, separator, remainder = stripped.partition(" ")
        if not separator:
            option, separator, remainder = stripped.partition("\t")
        if not separator:
            return [strip_optional_quotes(stripped)]

        return [
            strip_optional_quotes(option),
            strip_optional_quotes(remainder.strip()),
        ]


def slugify(value: str, max_length: int = 48, fallback: str = "art") -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return (slug or fallback)[:max_length].rstrip("-")


def strip_optional_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def optional_slug(value: str, fallback: str) -> str:
    if not value or not value.strip():
        return ""
    return slugify(value, fallback=fallback)


def build_context_slugs(args: argparse.Namespace) -> dict[str, str]:
    return {
        "client_slug": optional_slug(args.client, "unsorted"),
        "job_slug": optional_slug(args.job, "manual"),
        "tag_slug": optional_slug(args.tag, "tag"),
    }


def build_context_filename_prefix(args: argparse.Namespace) -> str:
    slugs = build_context_slugs(args)
    pieces: list[str] = []
    if slugs["client_slug"]:
        pieces.append(slugs["client_slug"])
    if slugs["job_slug"]:
        pieces.append(f"job-{slugs['job_slug']}")
    if slugs["tag_slug"]:
        pieces.append(slugs["tag_slug"])
    return "__".join(pieces)


def has_context_metadata(args: argparse.Namespace) -> bool:
    return any(
        bool(value and value.strip())
        for value in (args.client, args.job, args.tag)
    )


def should_write_run_metadata(args: argparse.Namespace) -> bool:
    return has_context_metadata(args) or args.variants > 1 or bool(args.cli_image_references)


def resolve_project_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path


def resolve_input_image_path(value: str, *, base_dir: Path | None = None) -> Path:
    path = Path(strip_markdown_target(value)).expanduser()
    if not path.is_absolute():
        candidates: list[Path] = []
        if base_dir is not None:
            candidates.append(base_dir / path)
        candidates.append(Path.cwd() / path)
        candidates.append(PROJECT_ROOT / path)
        for candidate in candidates:
            if candidate.exists():
                path = candidate
                break
        else:
            path = candidates[0]
    return path.resolve()


def strip_markdown_target(value: str) -> str:
    cleaned = value.strip()
    if cleaned.startswith('"') and '"' in cleaned[1:]:
        cleaned = cleaned[1:].split('"', 1)[0].strip()
    elif cleaned.startswith("'") and "'" in cleaned[1:]:
        cleaned = cleaned[1:].split("'", 1)[0].strip()
    elif " " in cleaned and '"' in cleaned:
        cleaned = cleaned.split('"', 1)[0].strip()
    cleaned = cleaned.strip("'\"").strip("<>")
    if "#" in cleaned:
        cleaned = cleaned.split("#", 1)[0]
    if "?" in cleaned:
        cleaned = cleaned.split("?", 1)[0]
    return cleaned.replace("%20", " ")


def is_supported_input_image(path: Path) -> bool:
    return path.suffix.lower() in SUPPORTED_INPUT_IMAGE_EXTENSIONS


def build_cli_image_references(args: argparse.Namespace) -> list[ImageReference]:
    references: list[ImageReference] = []
    for label, values in (
        ("input-image", args.input_image),
        ("reference-image", args.reference_image),
    ):
        for value in values:
            path = resolve_input_image_path(value)
            references.append(ImageReference(path=path, source=f"--{label}"))
    return references


def validate_image_references(
    parser: argparse.ArgumentParser,
    references: Iterable[ImageReference],
) -> None:
    for reference in references:
        if not reference.path.exists():
            parser.error(f"{reference.source} image does not exist: {reference.path}")
        if not reference.path.is_file():
            parser.error(f"{reference.source} image is not a file: {reference.path}")
        if not is_supported_input_image(reference.path):
            supported = ", ".join(sorted(SUPPORTED_INPUT_IMAGE_EXTENSIONS))
            parser.error(
                f"{reference.source} has unsupported image type: {reference.path}. "
                f"Supported: {supported}"
            )


def ensure_image_references_exist(references: Iterable[ImageReference]) -> None:
    for reference in references:
        if not reference.path.exists():
            raise RuntimeError(f"{reference.source} image does not exist: {reference.path}")
        if not reference.path.is_file():
            raise RuntimeError(f"{reference.source} image is not a file: {reference.path}")
        if not is_supported_input_image(reference.path):
            supported = ", ".join(sorted(SUPPORTED_INPUT_IMAGE_EXTENSIONS))
            raise RuntimeError(
                f"{reference.source} has unsupported image type: {reference.path}. "
                f"Supported: {supported}"
            )


def parse_args() -> argparse.Namespace:
    parser = ConfigFileArgumentParser(
        description="Generate images from a prompt with OpenAI's Responses API.",
        fromfile_prefix_chars="@",
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Prompt to send to the image generation tool.",
    )
    parser.add_argument(
        "--batch",
        nargs="?",
        const=str(DEFAULT_BATCH_INPUT_DIR),
        metavar="FOLDER",
        help=(
            "Generate one image per prompt file from the batch folder. "
            "Defaults to assets/batch-input when no folder is supplied."
        ),
    )
    parser.add_argument(
        "--batch-smoke",
        action="store_true",
        help="Generate from the built-in smoke-test batch folder at assets/batch-input-smoke.",
    )
    parser.add_argument(
        "--batch-input",
        dest="batch_input_legacy",
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--gallery-index",
        action="store_true",
        help=(
            "Build a gallery index JSON from existing engine sidecar metadata "
            "and exit without generating images."
        ),
    )
    parser.add_argument(
        "--gallery-source",
        default=str(DEFAULT_OUTPUT_DIR),
        metavar="FOLDER",
        help="Folder to scan for sidecar JSON when using --gallery-index.",
    )
    parser.add_argument(
        "--gallery-output",
        default=str(DEFAULT_GALLERY_INDEX_PATH),
        metavar="FILE",
        help="Output JSON file for --gallery-index (default: assets/gallery-index.json).",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Primary Responses model to use (default: {DEFAULT_MODEL}).",
    )
    parser.add_argument(
        "--fallback-model",
        action="append",
        dest="fallback_models",
        help=(
            "Optional fallback model to try if the primary model cannot run image generation. "
            "Repeat to add more than one."
        ),
    )
    parser.add_argument(
        "--no-model-fallback",
        action="store_true",
        help="Disable automatic fallback model handling.",
    )
    parser.add_argument(
        "--api-key",
        help=(
            "Explicit OpenAI API key for this run. "
            "Intended for lane wrappers that provide their own key."
        ),
    )
    parser.add_argument(
        "--api-key-env",
        action="append",
        default=[],
        metavar="ENV_VAR",
        help=(
            "Environment variable name to read the OpenAI API key from before "
            "engine defaults. Repeat to allow multiple lane-specific names."
        ),
    )
    parser.add_argument(
        "--style",
        action="append",
        choices=sorted(STYLE_PROMPTS),
        default=[],
        help="Named style prompt fragment to append. Repeat to combine multiple styles.",
    )
    parser.add_argument(
        "--preset",
        choices=sorted(PRESET_PROMPTS),
        help="Named prompt preset for repeatable VaultForge-oriented outputs.",
    )
    parser.add_argument(
        "--mod",
        action="append",
        choices=sorted(MOOD_PROMPTS),
        default=[],
        help="Named mood modifier to append. Repeat to combine multiple moods.",
    )
    parser.add_argument(
        "--size",
        default="1024x1024",
        help="Image size for the generation tool (default: 1024x1024).",
    )
    parser.add_argument(
        "--quality",
        default="medium",
        choices=("low", "medium", "high"),
        help="Image quality (default: medium).",
    )
    parser.add_argument(
        "--format",
        default="png",
        choices=sorted(SUPPORTED_FORMATS),
        help="Output image format (default: png).",
    )
    parser.add_argument(
        "--background",
        default="auto",
        choices=("auto", "transparent", "opaque"),
        help="Background handling for the image tool (default: auto).",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Output folder for generated images (default: assets/generated).",
    )
    parser.add_argument(
        "--filename",
        help="Optional output filename without extension. Defaults to a prompt-based slug.",
    )
    parser.add_argument(
        "--input-image",
        action="append",
        default=[],
        metavar="PATH",
        help=(
            "Local image to include as an editable input/reference. "
            "Repeat for multiple images."
        ),
    )
    parser.add_argument(
        "--reference-image",
        action="append",
        default=[],
        metavar="PATH",
        help=(
            "Local reference image to include with the prompt. "
            "Repeat for multiple references."
        ),
    )
    parser.add_argument(
        "--client",
        default="",
        help="Optional operator-facing client metadata for output naming and run manifests.",
    )
    parser.add_argument(
        "--job",
        default="",
        help="Optional operator-facing job metadata for output naming and run manifests.",
    )
    parser.add_argument(
        "--tag",
        default="",
        help="Optional operator-facing tag metadata for output naming and run manifests.",
    )
    parser.add_argument(
        "--variants",
        type=int,
        default=1,
        help="Number of image variants to generate for each prompt (default: 1).",
    )
    parser.add_argument(
        "--rerun",
        action="append",
        default=[],
        metavar="FILE",
        help=(
            "In batch mode, force the named prompt file to run again even if unchanged. "
            "Repeat to rerun more than one file."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the composed request and output path without calling the API.",
    )
    args = parser.parse_args()
    validate_args(parser, args)
    return args


def validate_args(parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    args.output_dir_path = resolve_project_path(args.output_dir)
    args.gallery_source_path = resolve_project_path(args.gallery_source)
    args.gallery_output_path = resolve_project_path(args.gallery_output)
    args.batch_folder = resolve_batch_folder(parser, args)

    if args.gallery_index:
        if args.prompt:
            parser.error("The prompt argument cannot be used with --gallery-index.")
        if args.batch is not None or args.batch_smoke or args.batch_input_legacy:
            parser.error("--gallery-index cannot be combined with batch generation options.")
        if args.dry_run:
            parser.error("--gallery-index cannot be combined with --dry-run because it writes an index file.")
        if args.rerun:
            parser.error("--rerun can only be used together with --batch or --batch-smoke.")
        return

    args.cli_image_references = build_cli_image_references(args)
    validate_image_references(parser, args.cli_image_references)

    if args.variants < 1:
        parser.error("--variants must be 1 or greater.")

    if args.batch_folder is not None:
        if args.prompt:
            parser.error("The prompt argument cannot be used with --batch or --batch-smoke.")
        if args.filename:
            parser.error(
                "--filename cannot be used with batch mode because each prompt file gets its own output name."
            )
        return

    if args.rerun:
        parser.error("--rerun can only be used together with --batch or --batch-smoke.")

    if not args.prompt:
        parser.error("A prompt is required unless you use --batch or --batch-smoke.")

    if args.batch_input_legacy:
        parser.error("--batch-input can only be used together with --batch.")


def resolve_batch_folder(
    parser: argparse.ArgumentParser,
    args: argparse.Namespace,
) -> Path | None:
    if args.batch_smoke:
        if args.batch is not None:
            parser.error("--batch and --batch-smoke cannot be used together.")
        if args.batch_input_legacy:
            parser.error("--batch-input cannot be used with --batch-smoke.")
        return DEFAULT_SMOKE_BATCH_INPUT_DIR

    if args.batch_input_legacy:
        if (
            args.batch is not None
            and resolve_project_path(args.batch).resolve() != DEFAULT_BATCH_INPUT_DIR.resolve()
        ):
            parser.error("Use either --batch [folder] or --batch-input, not both.")
        print(
            "Warning: --batch-input is deprecated; use --batch [folder] instead.",
            file=sys.stderr,
        )
        return resolve_project_path(args.batch_input_legacy)

    if args.batch is not None:
        return resolve_project_path(args.batch)

    return None


def load_env_file(env_file: Path | None = None) -> dict[str, str]:
    env_file = env_file or DEFAULT_ENV_FILE
    if not env_file.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in env_file.read_text(encoding="utf-8-sig").splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith(";"):
            continue
        key, separator, value = stripped.partition("=")
        if not separator:
            continue
        key = key.strip()
        if not key:
            continue
        values[key] = strip_optional_quotes(value.strip())
    return values


def find_api_key_in_sources(
    names: Iterable[str],
    *,
    env_values: dict[str, str],
) -> tuple[str, str] | None:
    for name in names:
        cleaned = name.strip()
        if not cleaned:
            continue
        value = os.environ.get(cleaned)
        if value:
            return cleaned, value
        value = env_values.get(cleaned)
        if value:
            return f"{DEFAULT_ENV_FILE.name}:{cleaned}", value
    return None


def get_api_key(args: argparse.Namespace) -> tuple[str, str]:
    if args.api_key:
        return "--api-key", args.api_key

    env_values = load_env_file()
    candidate_names = [*args.api_key_env, *API_KEY_ENV_VARS]
    found = find_api_key_in_sources(candidate_names, env_values=env_values)
    if found:
        return found

    raise RuntimeError(
        "OpenAI API key not found. Add one to "
        f"{DEFAULT_ENV_FILE} as {API_KEY_ENV_VAR}=sk-... or pass --api-key / --api-key-env."
    )


def get_api_key_for_run(args: argparse.Namespace) -> tuple[str, str | None]:
    if args.api_key:
        return "--api-key" + (" (dry run)" if args.dry_run else ""), args.api_key

    env_values = load_env_file()
    candidate_names = [*args.api_key_env, *API_KEY_ENV_VARS]
    found = find_api_key_in_sources(candidate_names, env_values=env_values)
    if found:
        source, value = found
        if args.dry_run:
            return f"{source} (dry run)", value
        return source, value

    if args.dry_run:
        return "dry run (API key not required)", None

    api_env_var, api_key = get_api_key(args)
    return api_env_var, api_key


def unique_models(primary: str, fallbacks: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for model in [primary, *fallbacks]:
        cleaned = model.strip()
        if not cleaned or cleaned in seen:
            continue
        ordered.append(cleaned)
        seen.add(cleaned)
    return ordered


def compose_prompt(
    prompt: str,
    preset: str | None,
    styles: list[str],
    mods: list[str],
) -> str:
    fragments = [prompt.strip()]
    if preset:
        fragments.append(PRESET_PROMPTS[preset])
    if styles:
        fragments.append("; ".join(STYLE_PROMPTS[style] for style in styles))
    if mods:
        fragments.append("; ".join(MOOD_PROMPTS[mod] for mod in mods))
    return ". ".join(fragment for fragment in fragments if fragment)


def extract_image_bytes(response) -> bytes:
    for output in response.output:
        result = extract_base64_image_value(output)
        if result:
            return base64.b64decode(result)

    raise RuntimeError(
        "The API response completed, but it did not include base64 image bytes."
    )


def extract_base64_image_value(value) -> str | None:
    if isinstance(value, dict):
        for key in ("result", "b64_json", "image_base64", "base64"):
            found = value.get(key)
            if isinstance(found, str) and found:
                return found
        for nested in value.values():
            found = extract_base64_image_value(nested)
            if found:
                return found
        return None

    for key in ("result", "b64_json", "image_base64", "base64"):
        found = getattr(value, key, None)
        if isinstance(found, str) and found:
            return found

    nested_values = []
    content = getattr(value, "content", None)
    if content is not None:
        nested_values.append(content)
    data = getattr(value, "data", None)
    if data is not None:
        nested_values.append(data)

    if isinstance(value, (list, tuple)):
        nested_values.extend(value)

    for nested in nested_values:
        found = extract_base64_image_value(nested)
        if found:
            return found
    return None


def build_output_path(
    prompt: str,
    extension: str,
    filename: str | None,
    output_dir: Path,
    *,
    output_stem: str | None = None,
    context_prefix: str = "",
    variant_index: int = 1,
    variant_count: int = 1,
) -> Path:
    base_name = filename or output_stem or slugify(prompt)
    if context_prefix and not filename:
        base_name = f"{context_prefix}__{base_name}"
    if variant_count > 1:
        base_name = f"{base_name}__v{variant_index:02d}"
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return output_dir / f"{timestamp}-{base_name}.{extension}"


def build_output_paths(
    prompt: str,
    extension: str,
    filename: str | None,
    output_dir: Path,
    *,
    output_stem: str | None,
    context_prefix: str,
    variant_count: int,
) -> list[tuple[int, Path]]:
    return [
        (
            variant_index,
            build_output_path(
                prompt,
                extension,
                filename,
                output_dir,
                output_stem=output_stem,
                context_prefix=context_prefix,
                variant_index=variant_index,
                variant_count=variant_count,
            ),
        )
        for variant_index in range(1, variant_count + 1)
    ]


def build_run_metadata(
    args: argparse.Namespace,
    *,
    prompt: str,
    composed_prompt: str,
    output_path: Path,
    models_to_try: list[str],
    selected_model: str | None,
    variant_index: int,
    image_references: list[ImageReference] | None = None,
    prompt_file: Path | None = None,
) -> dict[str, object]:
    context_slugs = build_context_slugs(args)
    payload: dict[str, object] = {
        "version": 1,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "client": args.client,
        "client_slug": context_slugs["client_slug"],
        "job": args.job,
        "job_slug": context_slugs["job_slug"],
        "tag": args.tag,
        "tag_slug": context_slugs["tag_slug"],
        "variant": variant_index,
        "variants": args.variants,
        "model": selected_model,
        "models_to_try": models_to_try,
        "prompt": prompt,
        "composed_prompt": composed_prompt,
        "preset": args.preset,
        "style": list(args.style),
        "mod": list(args.mod),
        "size": args.size,
        "quality": args.quality,
        "format": args.format,
        "background": args.background,
        "output_path": str(output_path),
    }
    if image_references:
        payload["image_references"] = [
            {
                "path": str(reference.path),
                "source": reference.source,
                "sha256": hash_file(reference.path),
            }
            for reference in image_references
        ]
    if prompt_file is not None:
        payload["prompt_file"] = str(prompt_file)
    return payload


def write_run_metadata(output_path: Path, payload: dict[str, object]) -> Path:
    metadata_path = output_path.with_suffix(".json")
    metadata_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return metadata_path


def is_gallery_sidecar_payload(payload: object) -> bool:
    if not isinstance(payload, dict):
        return False

    required_string_fields = (
        "created_at",
        "output_path",
        "prompt",
        "composed_prompt",
        "size",
        "quality",
        "format",
        "background",
    )
    if payload.get("version") != 1:
        return False
    if any(not isinstance(payload.get(field), str) for field in required_string_fields):
        return False
    if not isinstance(payload.get("variant"), int):
        return False
    if not isinstance(payload.get("variants"), int):
        return False
    return True


def build_gallery_entry(sidecar_path: Path, payload: dict[str, object]) -> dict[str, object]:
    entry_fields = (
        "created_at",
        "output_path",
        "prompt_file",
        "prompt",
        "composed_prompt",
        "model",
        "models_to_try",
        "preset",
        "style",
        "mod",
        "size",
        "quality",
        "format",
        "background",
        "client",
        "client_slug",
        "job",
        "job_slug",
        "tag",
        "tag_slug",
        "variant",
        "variants",
        "image_references",
    )
    entry = {
        field: payload[field]
        for field in entry_fields
        if field in payload
    }
    entry["sidecar_path"] = to_project_relative_path(sidecar_path)
    return entry


def build_gallery_index(source_dir: Path) -> dict[str, object]:
    if not source_dir.exists():
        raise RuntimeError(f"Gallery source folder does not exist: {source_dir}")
    if not source_dir.is_dir():
        raise RuntimeError(f"Gallery source is not a folder: {source_dir}")

    entries: list[dict[str, object]] = []
    ignored = 0
    for sidecar_path in sorted(source_dir.rglob("*.json")):
        try:
            payload = json.loads(sidecar_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            ignored += 1
            continue

        if not is_gallery_sidecar_payload(payload):
            ignored += 1
            continue
        assert isinstance(payload, dict)
        entries.append(build_gallery_entry(sidecar_path, payload))

    entries.sort(
        key=lambda entry: (
            str(entry.get("created_at", "")),
            str(entry.get("output_path", "")),
            str(entry.get("sidecar_path", "")),
        )
    )
    return {
        "version": GALLERY_INDEX_VERSION,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source_dir": str(source_dir),
        "entry_count": len(entries),
        "ignored_count": ignored,
        "entries": entries,
    }


def write_gallery_index(source_dir: Path, output_path: Path) -> Path:
    payload = build_gallery_index(source_dir)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return output_path


def build_batch_state_path(batch_input: Path) -> Path:
    return batch_input / BATCH_STATE_FILENAME


def load_batch_state(batch_input: Path) -> dict[str, dict[str, str]]:
    state_path = build_batch_state_path(batch_input)
    if not state_path.exists():
        return {}

    try:
        raw_data = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(
            f"Warning: Could not read batch state file {state_path}: {error}. Starting fresh.",
            file=sys.stderr,
        )
        return {}

    if not isinstance(raw_data, dict):
        print(
            f"Warning: Batch state file {state_path} is not a JSON object. Starting fresh.",
            file=sys.stderr,
        )
        return {}

    entries = raw_data.get("entries", {})
    if not isinstance(entries, dict):
        print(
            f"Warning: Batch state entries in {state_path} are invalid. Starting fresh.",
            file=sys.stderr,
        )
        return {}

    normalized_entries: dict[str, dict[str, str]] = {}
    for key, value in entries.items():
        if isinstance(key, str) and isinstance(value, dict):
            normalized_entries[key] = {
                str(sub_key): str(sub_value) for sub_key, sub_value in value.items()
            }
    return normalized_entries


def save_batch_state(batch_input: Path, entries: dict[str, dict[str, str]]) -> None:
    state_path = build_batch_state_path(batch_input)
    payload = {
        "version": 1,
        "entries": entries,
    }
    state_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def build_batch_request_hash(
    prompt_text: str,
    *,
    image_references: list[ImageReference],
    models_to_try: list[str],
    args: argparse.Namespace,
) -> str:
    payload = {
        "background": args.background,
        "client": args.client,
        "format": args.format,
        "image_references": [
            {
                "path": str(reference.path),
                "sha256": hash_file(reference.path),
                "source": reference.source,
            }
            for reference in image_references
        ],
        "job": args.job,
        "mods": list(args.mod),
        "models_to_try": models_to_try,
        "output_dir": str(args.output_dir_path.resolve()),
        "preset": args.preset,
        "prompt_text": prompt_text,
        "quality": args.quality,
        "size": args.size,
        "style": list(args.style),
        "tag": args.tag,
        "variants": args.variants,
    }
    serialized = json.dumps(payload, sort_keys=True)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file_handle:
        for chunk in iter(lambda: file_handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_batch_prompt_file(path: Path) -> bool:
    if not path.is_file() or path.name.startswith("."):
        return False

    suffix = path.suffix.lower()
    if suffix in BATCH_HELPER_EXTENSIONS:
        return False

    return suffix in PROMPT_FILE_EXTENSIONS


def extract_markdown_prompt_text(prompt_text: str) -> str:
    stripped = prompt_text.strip()
    if not stripped:
        return ""

    lines = stripped.splitlines()
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                lines = lines[index + 1 :]
                break

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


def extract_markdown_image_targets(prompt_text: str) -> list[str]:
    targets: list[str] = []
    for pattern in (MARKDOWN_IMAGE_PATTERN, WIKI_IMAGE_PATTERN, HTML_IMAGE_PATTERN):
        targets.extend(match.group(1).strip() for match in pattern.finditer(prompt_text))
    return targets


def strip_markdown_image_embeds(prompt_text: str) -> str:
    text = MARKDOWN_IMAGE_PATTERN.sub("", prompt_text)
    text = WIKI_IMAGE_PATTERN.sub("", text)
    text = HTML_IMAGE_PATTERN.sub("", text)
    lines = [line.rstrip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line.strip()).strip()


def extract_markdown_image_references(
    prompt_text: str,
    *,
    prompt_file: Path,
) -> list[ImageReference]:
    references: list[ImageReference] = []
    for target in extract_markdown_image_targets(prompt_text):
        stripped = strip_markdown_target(target)
        if not stripped:
            continue
        path = resolve_input_image_path(stripped, base_dir=prompt_file.parent)
        if not is_supported_input_image(path):
            continue
        references.append(ImageReference(path=path, source=f"embed:{prompt_file.name}"))
    return references


def dedupe_image_references(references: Iterable[ImageReference]) -> list[ImageReference]:
    deduped: list[ImageReference] = []
    seen: set[Path] = set()
    for reference in references:
        key = reference.path.resolve()
        if key in seen:
            continue
        deduped.append(reference)
        seen.add(key)
    return deduped


def read_batch_prompt_file(prompt_file: Path) -> tuple[Path, str, str, list[ImageReference]] | None:
    try:
        raw_text = prompt_file.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as error:
        raise RuntimeError(
            f"Prompt file is not valid UTF-8 text: {prompt_file}"
        ) from error

    suffix = prompt_file.suffix.lower()
    image_references: list[ImageReference] = []
    if suffix in MARKDOWN_PROMPT_EXTENSIONS:
        image_references = extract_markdown_image_references(raw_text, prompt_file=prompt_file)
        prompt_text = strip_markdown_image_embeds(extract_markdown_prompt_text(raw_text))
    else:
        prompt_text = raw_text.strip()

    output_stem = slugify(prompt_file.stem)

    if not prompt_text:
        print(f"Skipping empty prompt file: {prompt_file.name}", file=sys.stderr)
        return None

    return (prompt_file, prompt_text, output_stem, image_references)

def load_batch_prompts(batch_input: Path) -> list[tuple[Path, str, str, list[ImageReference]]]:
    is_default_batch_dir = batch_input.resolve() == DEFAULT_BATCH_INPUT_DIR.resolve()

    if not batch_input.exists():
        if is_default_batch_dir:
            batch_input.mkdir(parents=True, exist_ok=True)
        else:
            raise RuntimeError(f"Batch input folder does not exist: {batch_input}")

    if not batch_input.is_dir():
        raise RuntimeError(f"Batch input path is not a folder: {batch_input}")

    prompt_files = sorted(
        path
        for path in batch_input.iterdir()
        if is_batch_prompt_file(path)
    )
    if not prompt_files:
        raise RuntimeError(
            "No prompt files were found in "
            f"{batch_input}. Add one .txt, .md, .markdown, or extensionless prompt file and rerun the batch."
        )

    prompts: list[tuple[Path, str, str, list[ImageReference]]] = []
    for prompt_file in prompt_files:
        prompt_entry = read_batch_prompt_file(prompt_file)
        if prompt_entry is None:
            continue

        prompts.append(prompt_entry)

    if not prompts:
        raise RuntimeError(
            "Batch input files were found, but all of them were empty. "
            f"Add prompt text to files in {batch_input} and rerun."
        )

    return prompts


def normalize_rerun_targets(values: Iterable[str]) -> set[str]:
    return {value.strip().lower() for value in values if value and value.strip()}


def matches_rerun_target(prompt_file: Path, rerun_targets: set[str]) -> bool:
    return prompt_file.name.lower() in rerun_targets or prompt_file.stem.lower() in rerun_targets


def validate_rerun_targets(
    rerun_targets: set[str],
    prompt_entries: list[tuple[Path, str, str, list[ImageReference]]],
) -> None:
    if not rerun_targets:
        return

    matched_targets: set[str] = set()
    for prompt_file, _, _, _ in prompt_entries:
        aliases = {prompt_file.name.lower(), prompt_file.stem.lower()}
        matched_targets.update(rerun_targets & aliases)

    missing_targets = sorted(rerun_targets - matched_targets)
    if missing_targets:
        raise RuntimeError(
            "Rerun target(s) not found in the batch folder: "
            f"{', '.join(missing_targets)}"
        )


def to_project_relative_path(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def describe_image_references(references: Iterable[ImageReference]) -> list[str]:
    return [
        f"{reference.source}: {to_project_relative_path(reference.path)}"
        for reference in references
    ]


def image_to_data_url(path: Path) -> str:
    mime_type = INPUT_IMAGE_MIME_TYPES.get(path.suffix.lower())
    if mime_type is None:
        mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def build_responses_input(prompt: str, image_references: list[ImageReference]):
    if not image_references:
        return prompt
    content: list[dict[str, str]] = [{"type": "input_text", "text": prompt}]
    for reference in image_references:
        content.append(
            {
                "type": "input_image",
                "image_url": image_to_data_url(reference.path),
            }
        )
    return [{"role": "user", "content": content}]


def is_direct_image_model(model: str) -> bool:
    return model.startswith(GPT_IMAGE_MODEL_PREFIXES)


def should_try_fallback(error: APIError) -> bool:
    message = str(error).lower()
    fallback_signals = (
        "model",
        "not found",
        "unsupported",
        "not support",
        "does not exist",
        "not available",
        "tool_choice",
        "image_generation",
    )
    return any(signal in message for signal in fallback_signals)


def request_image(
    client: OpenAI,
    *,
    model: str,
    prompt: str,
    image_references: list[ImageReference],
    args: argparse.Namespace,
):
    if is_direct_image_model(model):
        return client.responses.create(
            model=model,
            input=build_responses_input(prompt, image_references),
        )

    return client.responses.create(
        model=model,
        input=build_responses_input(prompt, image_references),
        tools=[
            {
                "type": "image_generation",
                "size": args.size,
                "quality": args.quality,
                "output_format": args.format,
                "background": args.background,
            }
        ],
        tool_choice={"type": "image_generation"},
    )


def generate_with_fallback(
    client: OpenAI,
    models: list[str],
    prompt: str,
    image_references: list[ImageReference],
    args: argparse.Namespace,
):
    errors: list[tuple[str, str]] = []

    for index, model in enumerate(models):
        try:
            response = request_image(
                client,
                model=model,
                prompt=prompt,
                image_references=image_references,
                args=args,
            )
            return model, response, errors
        except APIError as error:
            errors.append((model, str(error)))
            is_last_model = index == len(models) - 1
            if is_last_model or not should_try_fallback(error):
                break
            print(
                f"Model '{model}' failed for image generation, trying fallback '{models[index + 1]}'.",
                file=sys.stderr,
            )

    attempted = ", ".join(model for model, _ in errors) or "none"
    details = " | ".join(f"{model}: {message}" for model, message in errors)
    raise RuntimeError(
        "Image generation request failed. "
        f"Attempted models: {attempted}. Details: {details}"
    )


def run_batch(
    client: OpenAI | None,
    *,
    api_env_var: str,
    models_to_try: list[str],
    args: argparse.Namespace,
) -> int:
    assert args.batch_folder is not None
    batch_input = args.batch_folder
    prompt_entries = load_batch_prompts(batch_input)
    rerun_targets = normalize_rerun_targets(args.rerun)
    validate_rerun_targets(rerun_targets, prompt_entries)
    batch_state = load_batch_state(batch_input)
    total = len(prompt_entries)
    context_prefix = build_context_filename_prefix(args)
    write_metadata = should_write_run_metadata(args)

    print(f"API key source: {api_env_var}")
    print(f"Models to try: {', '.join(models_to_try)}")
    print(f"Batch input: {batch_input}")
    print(f"Output dir: {args.output_dir_path}")
    print(f"Batch state: {build_batch_state_path(batch_input)}")
    if has_context_metadata(args):
        context_slugs = build_context_slugs(args)
        print(
            "Context metadata: "
            f"client={args.client or ''} ({context_slugs['client_slug'] or 'none'}), "
            f"job={args.job or ''} ({context_slugs['job_slug'] or 'none'}), "
            f"tag={args.tag or ''} ({context_slugs['tag_slug'] or 'none'})"
        )
    if args.variants > 1:
        print(f"Variants: {args.variants}")
    if rerun_targets:
        print(f"Forced reruns: {', '.join(sorted(rerun_targets))}")

    successes = 0
    skipped = 0
    failures: list[tuple[Path, str]] = []

    for index, (prompt_file, prompt_text, output_stem, embedded_references) in enumerate(prompt_entries, start=1):
        image_references = dedupe_image_references(
            [*args.cli_image_references, *embedded_references]
        )
        ensure_image_references_exist(image_references)
        request_hash = build_batch_request_hash(
            prompt_text,
            image_references=image_references,
            models_to_try=models_to_try,
            args=args,
        )
        force_rerun = matches_rerun_target(prompt_file, rerun_targets)
        previous_entry = batch_state.get(prompt_file.name, {})
        if previous_entry.get("request_hash") == request_hash and not force_rerun:
            skipped += 1
            print(
                f"[{index}/{total}] Skipping unchanged prompt file: {prompt_file.name} "
                f"(use --rerun {prompt_file.stem} to force a new image)"
            )
            continue

        output_paths = build_output_paths(
            prompt_text,
            args.format,
            None,
            args.output_dir_path,
            output_stem=output_stem,
            context_prefix=context_prefix,
            variant_count=args.variants,
        )
        composed_prompt = compose_prompt(prompt_text, args.preset, args.style, args.mod)
        write_metadata_for_entry = write_metadata or bool(image_references)

        if args.dry_run:
            status_suffix = " (forced rerun)" if force_rerun else ""
            print(f"[{index}/{total}] Source: {prompt_file}{status_suffix}")
            print(f"[{index}/{total}] Prompt: {composed_prompt}")
            if image_references:
                print(f"[{index}/{total}] Image references: {len(image_references)}")
                for description in describe_image_references(image_references):
                    print(f"[{index}/{total}] - {description}")
            for variant_index, output_path in output_paths:
                label = "Output path"
                if args.variants > 1:
                    label = f"Output path v{variant_index:02d}"
                print(f"[{index}/{total}] {label}: {output_path}")
                if write_metadata_for_entry:
                    print(f"[{index}/{total}] Metadata path: {output_path.with_suffix('.json')}")
            continue

        try:
            assert client is not None
            saved_outputs: list[str] = []
            saved_metadata: list[str] = []
            for variant_index, output_path in output_paths:
                selected_model, response, prior_errors = generate_with_fallback(
                    client,
                    models=models_to_try,
                    prompt=composed_prompt,
                    image_references=image_references,
                    args=args,
                )
                image_bytes = extract_image_bytes(response)
                output_path.write_bytes(image_bytes)
                successes += 1
                saved_outputs.append(to_project_relative_path(output_path))

                if write_metadata_for_entry:
                    metadata_path = write_run_metadata(
                        output_path,
                        build_run_metadata(
                            args,
                            prompt=prompt_text,
                            composed_prompt=composed_prompt,
                            output_path=output_path,
                            models_to_try=models_to_try,
                            selected_model=selected_model,
                            variant_index=variant_index,
                            image_references=image_references,
                            prompt_file=prompt_file,
                        ),
                    )
                    saved_metadata.append(to_project_relative_path(metadata_path))

                variant_suffix = ""
                if args.variants > 1:
                    variant_suffix = f", variant {variant_index:02d}/{args.variants:02d}"

                if prior_errors:
                    print(
                        f"[{index}/{total}] Saved image to: {output_path} "
                        f"(source: {prompt_file.name}{variant_suffix}, "
                        f"after fallback to model '{selected_model}')"
                    )
                else:
                    print(
                        f"[{index}/{total}] Saved image to: {output_path} "
                        f"(source: {prompt_file.name}{variant_suffix})"
                    )

            batch_state[prompt_file.name] = {
                "last_output": saved_outputs[0] if saved_outputs else "",
                "last_outputs": saved_outputs,
                "last_metadata": saved_metadata,
                "last_run_at": datetime.now().isoformat(timespec="seconds"),
                "request_hash": request_hash,
            }
        except Exception as error:
            failures.append((prompt_file, str(error)))
            print(
                f"[{index}/{total}] Error for {prompt_file.name}: {error}",
                file=sys.stderr,
            )

    if args.dry_run:
        would_run = total - skipped
        if args.variants > 1:
            print(
                f"Batch dry run complete: {would_run} prompt file(s) would run, "
                f"{would_run * args.variants} image request(s) would be made, "
                f"{skipped} would skip."
            )
        else:
            print(
                f"Batch dry run complete: {would_run} prompt file(s) would run, "
                f"{skipped} would skip."
            )
        return 0

    if successes:
        save_batch_state(batch_input, batch_state)

    if failures:
        print(
            f"Batch finished with {successes} success(es), {skipped} skipped, "
            f"and {len(failures)} failure(s).",
            file=sys.stderr,
        )
        return 1

    print(
        f"Batch finished successfully: {successes} image(s) saved and {skipped} skipped."
    )
    return 0


def main() -> int:
    args = parse_args()

    try:
        if args.gallery_index:
            gallery_path = write_gallery_index(
                args.gallery_source_path,
                args.gallery_output_path,
            )
            print(f"Gallery index written: {gallery_path}")
            return 0

        args.output_dir_path.mkdir(parents=True, exist_ok=True)
        api_env_var, api_key = get_api_key_for_run(args)
        fallback_models = (
            []
            if args.no_model_fallback
            else (args.fallback_models or list(DEFAULT_FALLBACK_MODELS))
        )
        models_to_try = unique_models(args.model, fallback_models)

        if args.batch_folder is not None:
            client = None if args.dry_run else OpenAI(api_key=api_key)
            return run_batch(
                client,
                api_env_var=api_env_var,
                models_to_try=models_to_try,
                args=args,
            )

        assert args.prompt is not None
        composed_prompt = compose_prompt(args.prompt, args.preset, args.style, args.mod)
        image_references = dedupe_image_references(args.cli_image_references)
        context_prefix = build_context_filename_prefix(args)
        write_metadata = should_write_run_metadata(args)
        output_paths = build_output_paths(
            args.prompt,
            args.format,
            args.filename,
            args.output_dir_path,
            output_stem=None,
            context_prefix=context_prefix,
            variant_count=args.variants,
        )

        if args.dry_run:
            print(f"API key source: {api_env_var}")
            print(f"Models to try: {', '.join(models_to_try)}")
            print(f"Output dir: {args.output_dir_path}")
            if has_context_metadata(args):
                context_slugs = build_context_slugs(args)
                print(
                    "Context metadata: "
                    f"client={args.client or ''} ({context_slugs['client_slug'] or 'none'}), "
                    f"job={args.job or ''} ({context_slugs['job_slug'] or 'none'}), "
                    f"tag={args.tag or ''} ({context_slugs['tag_slug'] or 'none'})"
                )
            if args.variants > 1:
                print(f"Variants: {args.variants}")
            print(f"Prompt: {composed_prompt}")
            if image_references:
                print(f"Image references: {len(image_references)}")
                for description in describe_image_references(image_references):
                    print(f"- {description}")
            for variant_index, output_path in output_paths:
                label = "Output path"
                if args.variants > 1:
                    label = f"Output path v{variant_index:02d}"
                print(f"{label}: {output_path}")
                if write_metadata:
                    print(f"Metadata path: {output_path.with_suffix('.json')}")
            return 0

        assert api_key is not None
        client = OpenAI(api_key=api_key)
        for variant_index, output_path in output_paths:
            selected_model, response, prior_errors = generate_with_fallback(
                client,
                models=models_to_try,
                prompt=composed_prompt,
                image_references=image_references,
                args=args,
            )
            image_bytes = extract_image_bytes(response)
            output_path.write_bytes(image_bytes)

            if write_metadata:
                write_run_metadata(
                    output_path,
                    build_run_metadata(
                        args,
                        prompt=args.prompt,
                        composed_prompt=composed_prompt,
                        output_path=output_path,
                        models_to_try=models_to_try,
                        selected_model=selected_model,
                        variant_index=variant_index,
                        image_references=image_references,
                    ),
                )

            variant_suffix = ""
            if args.variants > 1:
                variant_suffix = f" (variant {variant_index:02d}/{args.variants:02d})"

            if prior_errors:
                print(
                    f"Saved image to: {output_path}{variant_suffix} "
                    f"(after fallback to model '{selected_model}')"
                )
            else:
                print(f"Saved image to: {output_path}{variant_suffix}")
        return 0
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

