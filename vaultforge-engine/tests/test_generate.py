import io
import sys
import tempfile
import unittest
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


