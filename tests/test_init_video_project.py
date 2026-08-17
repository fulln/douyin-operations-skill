from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

SCRIPT_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from init_video_project import validate_project_slug, write_video_project


class InitVideoProjectTests(unittest.TestCase):
    def test_write_video_project_creates_traceable_workflow(self) -> None:
        with TemporaryDirectory() as directory:
            root = write_video_project(
                Path(directory),
                project_slug="first-hook-test",
                title="开场留存测试",
                primary_metric="five_second_retention",
                changed_variable="opening_line",
            )

            expected_files = {
                "01-brief.md",
                "02-script.md",
                "03-shot-list.md",
                "04-edit-plan.md",
                "05-publish-pack.md",
                "06-review.md",
                "project.json",
            }
            actual_files = {path.name for path in root.iterdir() if path.is_file()}
            self.assertEqual(expected_files, actual_files)
            for relative_directory in ("assets/raw", "assets/selected", "assets/audio", "exports"):
                self.assertTrue((root / relative_directory).is_dir())

            brief = (root / "01-brief.md").read_text(encoding="utf-8")
            self.assertIn("开场留存测试", brief)
            self.assertIn("five_second_retention", brief)
            self.assertIn("opening_line", brief)
            self.assertNotIn("{{", brief)

            manifest = json.loads((root / "project.json").read_text(encoding="utf-8"))
            self.assertEqual("brief", manifest["status"])
            self.assertEqual("first-hook-test", manifest["project_slug"])

    def test_validate_project_slug_rejects_unsafe_names(self) -> None:
        for invalid in ("Uppercase", "has space", "../escape", "double--dash", ""):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                validate_project_slug(invalid)

    def test_write_video_project_refuses_overwrite_without_force(self) -> None:
        with TemporaryDirectory() as directory:
            output_root = Path(directory)
            arguments = {
                "project_slug": "same-project",
                "title": "标题",
                "primary_metric": "completion_rate",
                "changed_variable": "pacing",
            }
            root = write_video_project(output_root, **arguments)
            original = (root / "01-brief.md").read_text(encoding="utf-8")

            with self.assertRaisesRegex(FileExistsError, "--force"):
                write_video_project(output_root, **arguments)

            self.assertEqual(original, (root / "01-brief.md").read_text(encoding="utf-8"))

    def test_write_video_project_force_refreshes_templates(self) -> None:
        with TemporaryDirectory() as directory:
            output_root = Path(directory)
            root = write_video_project(
                output_root,
                project_slug="refresh-project",
                title="旧标题",
                primary_metric="completion_rate",
                changed_variable="pacing",
            )
            (root / "01-brief.md").write_text("modified\n", encoding="utf-8")

            write_video_project(
                output_root,
                project_slug="refresh-project",
                title="新标题",
                primary_metric="completion_rate",
                changed_variable="pacing",
                force=True,
            )

            self.assertIn("新标题", (root / "01-brief.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
