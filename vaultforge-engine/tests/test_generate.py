import io
import json
import os
import sys
import tempfile
import unittest
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import patch

import generate


class LoadBatchPromptsTests(unittest.TestCase):
    def test_text_prompt_keeps_filename_stem(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            batch_dir = Path(temp_dir)
            (batch_dir / "forge.txt").write_text(
                "A glowing forge hidden inside an ancient mountain vault",
                encoding="utf-8",
            )

            entries = generate.load_batch_prompts(batch_dir)

            self.assertEqual(len(entries), 1)
            self.assertEqual(
                entries[0],
                (
                    batch_dir / "forge.txt",
                    "A glowing forge hidden inside an ancient mountain vault",
                    "forge",
                    [],
                ),
            )

    def test_markdown_prompt_strips_frontmatter_and_heading(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            batch_dir = Path(temp_dir)
            markdown_note = """---
kind: prompt
source: obsidian
---

# Random Vault Note

A glowing forge hidden inside an ancient mountain vault.
Ancient brass tools resting in ember light.
"""
            (batch_dir / "random-title.md").write_text(markdown_note, encoding="utf-8")
            (batch_dir / "ignored.json").write_text('{"note": true}', encoding="utf-8")

            entries = generate.load_batch_prompts(batch_dir)

            self.assertEqual(len(entries), 1)
            expected_prompt = (
                "A glowing forge hidden inside an ancient mountain vault.\n"
                "Ancient brass tools resting in ember light."
            )
            self.assertEqual(entries[0][1], expected_prompt)
            self.assertEqual(entries[0][2], 'random-title')
            self.assertEqual(entries[0][3], [])

    def test_markdown_heading_only_becomes_the_prompt(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            batch_dir = Path(temp_dir)
            (batch_dir / "untitled.md").write_text(
                "# Sacred scene prompt",
                encoding="utf-8",
            )

            entries = generate.load_batch_prompts(batch_dir)

            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0][1], "Sacred scene prompt")
            self.assertEqual(entries[0][2], "untitled")
            self.assertEqual(entries[0][3], [])

    def test_markdown_prompt_extracts_embedded_image_references(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            batch_dir = Path(temp_dir)
            image_path = batch_dir / "style ref.png"
            image_path.write_bytes(b"fake-png")
            (batch_dir / "with-ref.md").write_text(
                "# Forest character\n\nUse this as a style reference:\n\n![style](style%20ref.png)\n\nMake a calm portrait.",
                encoding="utf-8",
            )

            entries = generate.load_batch_prompts(batch_dir)

            self.assertEqual(len(entries), 1)
            self.assertEqual(
                entries[0][1],
                "Use this as a style reference:\nMake a calm portrait.",
            )
            self.assertEqual(entries[0][3], [
                generate.ImageReference(path=image_path.resolve(), source="embed:with-ref.md")
            ])

    def test_markdown_prompt_extracts_raw_space_image_paths(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            batch_dir = Path(temp_dir)
            image_path = batch_dir / "style ref.png"
            image_path.write_bytes(b"fake-png")
            (batch_dir / "with-spaces.md").write_text(
                "# Forest character\n\n![style](style ref.png)\n\nMake a calm portrait.",
                encoding="utf-8",
            )

            entries = generate.load_batch_prompts(batch_dir)

            self.assertEqual(entries[0][1], "Make a calm portrait.")
            self.assertEqual(entries[0][3], [
                generate.ImageReference(path=image_path.resolve(), source="embed:with-spaces.md")
            ])


class PromptBuildingBlocksTests(unittest.TestCase):
    def test_compose_prompt_supports_icon_and_new_styles(self):
        prompt = generate.compose_prompt(
            "An arcane key sigil",
            "icon",
            ["geometric", "fine-line", "mystica"],
            [],
        )

        self.assertIn(generate.PRESET_PROMPTS["icon"], prompt)
        self.assertIn(generate.STYLE_PROMPTS["geometric"], prompt)
        self.assertIn(generate.STYLE_PROMPTS["fine-line"], prompt)
        self.assertIn(generate.STYLE_PROMPTS["mystica"], prompt)

    def test_parse_args_accepts_icon_and_new_styles(self):
        argv = [
            "generate.py",
            "Arcane icon prompt",
            "--preset",
            "icon",
            "--style",
            "geometric",
            "--style",
            "fine-line",
            "--style",
            "mystica",
        ]

        with patch.object(sys, "argv", argv):
            args = generate.parse_args()

        self.assertEqual(args.preset, "icon")
        self.assertEqual(args.style, ["geometric", "fine-line", "mystica"])

    def test_compose_prompt_keeps_business_aliases_and_constraints_out_of_moods(self):
        prompt = generate.compose_prompt(
            "Premium app tile",
            "business-icon",
            ["vector-crisp"],
            ["hopeful"],
            ["small-size-readable", "transparent-bg-ready"],
        )

        self.assertIn(generate.PRESET_PROMPTS["icon"], prompt)
        self.assertIn(generate.STYLE_PROMPTS["geometric"], prompt)
        self.assertIn(generate.MOOD_PROMPTS["hopeful"], prompt)
        self.assertIn(generate.PRODUCTION_CONSTRAINT_PROMPTS["small-size-readable"], prompt)
        self.assertIn(generate.PRODUCTION_CONSTRAINT_PROMPTS["transparent-bg-ready"], prompt)
        self.assertNotIn("business-icon", generate.MOOD_PROMPTS)
        self.assertNotIn("small-size-readable", generate.MOOD_PROMPTS)

    def test_parse_args_accepts_business_aliases_and_constraints(self):
        argv = [
            "generate.py",
            "Premium app tile",
            "--preset",
            "business-icon",
            "--style",
            "vector-crisp",
            "--constraint",
            "small-size-readable",
            "--constraint",
            "transparent-bg-ready",
        ]

        with patch.object(sys, "argv", argv):
            args = generate.parse_args()

        self.assertEqual(args.preset, "business-icon")
        self.assertEqual(args.style, ["vector-crisp"])
        self.assertEqual(args.constraint, ["small-size-readable", "transparent-bg-ready"])

    def test_parse_args_accepts_reference_image(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = Path(temp_dir) / "reference.jpeg"
            image_path.write_bytes(b"fake-jpeg")
            argv = [
                "generate.py",
                "Minor style tweak",
                "--reference-image",
                str(image_path),
            ]

            with patch.object(sys, "argv", argv):
                args = generate.parse_args()

            self.assertEqual(args.reference_image, [str(image_path)])
            self.assertEqual(args.cli_image_references, [
                generate.ImageReference(path=image_path.resolve(), source="--reference-image")
            ])

    def test_parse_args_accepts_business_context_flags(self):
        argv = [
            "generate.py",
            "Premium logo direction",
            "--client",
            "Empower You",
            "--job",
            "logo-pack-01",
            "--tag",
            "local, premium",
            "--variants",
            "3",
        ]

        with patch.object(sys, "argv", argv):
            args = generate.parse_args()

        self.assertEqual(args.client, "Empower You")
        self.assertEqual(args.job, "logo-pack-01")
        self.assertEqual(args.tag, "local, premium")
        self.assertEqual(args.variants, 3)

    def test_parse_args_accepts_lane_api_key_env(self):
        argv = [
            "generate.py",
            "Premium logo direction",
            "--api-key-env",
            "VAULTFORGE_ICON_OPENAI_API_KEY",
        ]

        with patch.object(sys, "argv", argv):
            args = generate.parse_args()

        self.assertEqual(args.api_key_env, ["VAULTFORGE_ICON_OPENAI_API_KEY"])

    def test_parse_args_rejects_zero_variants(self):
        argv = [
            "generate.py",
            "Premium logo direction",
            "--variants",
            "0",
        ]

        with patch.object(sys, "argv", argv), patch.object(sys, "stderr", io.StringIO()):
            with self.assertRaises(SystemExit):
                generate.parse_args()

    def test_output_path_uses_context_prefix_and_variant_suffix(self):
        output_path = generate.build_output_path(
            "Premium logo direction",
            "png",
            None,
            Path("generated"),
            context_prefix="empower-you__job-logo-pack-01__local-premium",
            variant_index=2,
            variant_count=3,
        )

        self.assertTrue(
            output_path.name.endswith(
                "-empower-you__job-logo-pack-01__local-premium__premium-logo-direction__v02.png"
            )
        )

    def test_run_metadata_preserves_raw_and_slug_context(self):
        args = generate.argparse.Namespace(
            client="Empower You",
            job="Logo Pack 01",
            tag="local, premium",
            variants=2,
            preset="icon",
            style=["geometric"],
            mod=[],
            size="1024x1024",
            quality="medium",
            format="png",
            background="auto",
            cli_image_references=[],
        )

        metadata = generate.build_run_metadata(
            args,
            prompt="Premium logo direction",
            composed_prompt="Premium logo direction. icon fragment.",
            output_path=Path("generated/output.png"),
            models_to_try=["gpt-5"],
            selected_model="gpt-5",
            variant_index=1,
        )

        self.assertEqual(metadata["client"], "Empower You")
        self.assertEqual(metadata["client_slug"], "empower-you")
        self.assertEqual(metadata["job"], "Logo Pack 01")
        self.assertEqual(metadata["job_slug"], "logo-pack-01")
        self.assertEqual(metadata["tag"], "local, premium")
        self.assertEqual(metadata["tag_slug"], "local-premium")
        self.assertEqual(metadata["variants"], 2)
        self.assertEqual(metadata["variant"], 1)

    def test_build_responses_input_adds_image_data_urls(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = Path(temp_dir) / "reference.svg"
            image_path.write_text("<svg></svg>", encoding="utf-8")
            references = [
                generate.ImageReference(path=image_path, source="--reference-image")
            ]

            responses_input = generate.build_responses_input("Match this style", references)

            self.assertIsInstance(responses_input, list)
            content = responses_input[0]["content"]
            self.assertEqual(content[0], {"type": "input_text", "text": "Match this style"})
            self.assertEqual(content[1]["type"], "input_image")
            self.assertTrue(content[1]["image_url"].startswith("data:image/svg+xml;base64,"))

    def test_direct_image_model_request_omits_image_generation_tool(self):
        calls = []

        class FakeResponses:
            def create(self, **kwargs):
                calls.append(kwargs)
                return SimpleNamespace(output=[])

        client = SimpleNamespace(responses=FakeResponses())
        args = generate.argparse.Namespace(
            size="1024x1024",
            quality="medium",
            format="png",
            background="auto",
        )

        generate.request_image(
            client,
            model=generate.DEFAULT_MODEL,
            prompt="Draw a forge",
            image_references=[],
            args=args,
        )

        self.assertEqual(calls[0]["model"], "gpt-image-2-2026-04-21")
        self.assertNotIn("tools", calls[0])


class GalleryIndexTests(unittest.TestCase):
    def test_parse_args_accepts_gallery_index_without_prompt(self):
        argv = [
            "generate.py",
            "--gallery-index",
            "--gallery-source",
            "assets/generated",
            "--gallery-output",
            "assets/gallery-index.json",
        ]

        with patch.object(sys, "argv", argv):
            args = generate.parse_args()

        self.assertTrue(args.gallery_index)
        self.assertEqual(args.gallery_source_path, generate.PROJECT_ROOT / "assets" / "generated")
        self.assertEqual(args.gallery_output_path, generate.PROJECT_ROOT / "assets" / "gallery-index.json")

    def test_parse_args_rejects_gallery_index_dry_run(self):
        argv = [
            "generate.py",
            "--gallery-index",
            "--dry-run",
            "--gallery-source",
            "assets/generated",
            "--gallery-output",
            "assets/gallery-index.json",
        ]

        with patch.object(sys, "argv", argv), patch.object(sys, "stderr", io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                generate.parse_args()

        self.assertEqual(raised.exception.code, 2)

    def test_build_gallery_index_collects_valid_sidecars(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_dir = Path(temp_dir) / "generated"
            source_dir.mkdir()
            sidecar_path = source_dir / "sample.json"
            sidecar_path.write_text(
                """{
  "background": "auto",
  "client": "Empower You",
  "client_slug": "empower-you",
  "composed_prompt": "Premium logo direction. icon fragment.",
  "constraint": ["small-size-readable"],
  "created_at": "2026-05-09T22:45:00",
  "format": "png",
  "job": "Logo Pack 01",
  "job_slug": "logo-pack-01",
  "model": "gpt-image-2-2026-04-21",
  "models_to_try": ["gpt-image-2-2026-04-21"],
  "output_path": "generated/sample.png",
  "preset": "icon",
  "prompt": "Premium logo direction",
  "quality": "medium",
  "size": "1024x1024",
  "style": ["geometric"],
  "tag": "local, premium",
  "tag_slug": "local-premium",
  "variant": 1,
  "variants": 1,
  "version": 1
}""",
                encoding="utf-8",
            )
            (source_dir / "not-a-sidecar.json").write_text('{"version": 1}', encoding="utf-8")

            index = generate.build_gallery_index(source_dir)

        self.assertEqual(index["version"], 1)
        self.assertEqual(index["entry_count"], 1)
        self.assertEqual(index["ignored_count"], 1)
        entry = index["entries"][0]
        self.assertEqual(entry["client_slug"], "empower-you")
        self.assertEqual(entry["constraint"], ["small-size-readable"])
        self.assertEqual(entry["output_path"], "generated/sample.png")
        self.assertTrue(str(entry["sidecar_path"]).endswith("sample.json"))

    def test_write_gallery_index_creates_json_output(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            source_dir = temp_path / "generated"
            source_dir.mkdir()
            output_path = temp_path / "index" / "gallery-index.json"

            written_path = generate.write_gallery_index(source_dir, output_path)
            payload = json.loads(written_path.read_text(encoding="utf-8"))

        self.assertEqual(written_path, output_path)
        self.assertEqual(payload["entry_count"], 0)
        self.assertEqual(payload["entries"], [])


class ApiKeyLoadingTests(unittest.TestCase):
    def test_get_api_key_prefers_explicit_key(self):
        args = generate.argparse.Namespace(
            api_key="sk-explicit",
            api_key_env=[],
            dry_run=False,
        )

        source, value = generate.get_api_key_for_run(args)

        self.assertEqual(source, "--api-key")
        self.assertEqual(value, "sk-explicit")

    def test_get_api_key_reads_engine_env_file(self):
        args = generate.argparse.Namespace(
            api_key=None,
            api_key_env=[],
            dry_run=False,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            env_file = Path(temp_dir) / ".env"
            env_file.write_text(
                "VAULTFORGE_ENGINE_OPENAI_API_KEY=sk-env-file\n",
                encoding="utf-8",
            )
            with patch.object(generate, "DEFAULT_ENV_FILE", env_file), patch.dict(os.environ, {}, clear=True):
                source, value = generate.get_api_key_for_run(args)

        self.assertEqual(source, ".env:VAULTFORGE_ENGINE_OPENAI_API_KEY")
        self.assertEqual(value, "sk-env-file")

    def test_get_api_key_reads_lane_env_before_engine_default(self):
        args = generate.argparse.Namespace(
            api_key=None,
            api_key_env=["VAULTFORGE_ICON_OPENAI_API_KEY"],
            dry_run=False,
        )

        with patch.dict(
            os.environ,
            {
                "VAULTFORGE_ICON_OPENAI_API_KEY": "sk-icon",
                "VAULTFORGE_ENGINE_OPENAI_API_KEY": "sk-engine",
            },
            clear=True,
        ):
            source, value = generate.get_api_key_for_run(args)

        self.assertEqual(source, "VAULTFORGE_ICON_OPENAI_API_KEY")
        self.assertEqual(value, "sk-icon")

    def test_get_api_key_reads_engine_key_from_env_file(self):
        args = generate.argparse.Namespace(
            api_key=None,
            api_key_env=[],
            dry_run=False,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            env_file = Path(temp_dir) / ".env"
            env_file.write_text("ENGINE_KEY=sk-engine-key\n", encoding="utf-8")
            with patch.object(generate, "DEFAULT_ENV_FILE", env_file), patch.dict(os.environ, {}, clear=True):
                source, value = generate.get_api_key_for_run(args)

        self.assertEqual(source, ".env:ENGINE_KEY")
        self.assertEqual(value, "sk-engine-key")


class EngineProjectRootTests(unittest.TestCase):
    def test_project_root_resolves_to_engine_folder_not_src(self):
        self.assertEqual(generate.PROJECT_ROOT.name, "vaultforge-engine")
        self.assertEqual(generate.DEFAULT_OUTPUT_DIR, generate.PROJECT_ROOT / "assets" / "generated")

    def test_project_root_can_be_overridden_by_environment(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch.dict(generate.os.environ, {generate.PROJECT_ROOT_ENV_VAR: temp_dir}):
                self.assertEqual(generate.get_project_root(), Path(temp_dir).resolve())


if __name__ == "__main__":
    unittest.main()


