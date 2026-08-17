from __future__ import annotations

import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

SCRIPT_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from init_config import render_config, write_config


class InitConfigTests(unittest.TestCase):
    def test_render_config_escapes_values_for_yaml(self) -> None:
        template = (
            "account: {{ACCOUNT_NAME_JSON}}\n"
            "brand: {{BRAND_NAME_JSON}}\n"
            "goal: {{PRIMARY_GOAL_JSON}}\n"
            "root: {{WORKSPACE_ROOT_JSON}}\n"
        )

        rendered = render_config(
            template,
            account_name='原相 "实验室"',
            brand_name="Elemento\nStudio",
            primary_goal="验证：内容 → 转化",
            workspace_root="/tmp/含 空格",
        )

        self.assertNotIn("{{", rendered)
        self.assertIn('account: "原相 \\"实验室\\""', rendered)
        self.assertIn('brand: "Elemento\\nStudio"', rendered)
        self.assertIn('goal: "验证：内容 → 转化"', rendered)
        self.assertIn('root: "/tmp/含 空格"', rendered)

    def test_write_config_creates_parent_and_keeps_method_defaults(self) -> None:
        with TemporaryDirectory() as directory:
            output = Path(directory) / "nested" / "douyin-ops.yaml"
            result = write_config(
                output,
                account_name="原相实验室",
                brand_name="Elemento",
                primary_goal="验证内容到首次有效转化",
                workspace_root="/workspace/douyin",
            )

            content = output.read_text(encoding="utf-8")
            self.assertEqual(result, output)
            self.assertIn('name: "原相实验室"', content)
            self.assertIn('brand_name: "Elemento"', content)
            self.assertIn('primary_goal: "验证内容到首次有效转化"', content)
            self.assertIn('root: "/workspace/douyin"', content)
            self.assertIn("min_aligned_posts_before_change: 10", content)
            self.assertIn("change_one_primary_variable: true", content)

    def test_write_config_refuses_overwrite_without_force(self) -> None:
        with TemporaryDirectory() as directory:
            output = Path(directory) / "douyin-ops.yaml"
            output.write_text("existing\n", encoding="utf-8")

            with self.assertRaisesRegex(FileExistsError, "--force"):
                write_config(
                    output,
                    account_name="账号",
                    brand_name="品牌",
                    primary_goal="目标",
                    workspace_root="/workspace",
                )

            self.assertEqual(output.read_text(encoding="utf-8"), "existing\n")

    def test_write_config_force_overwrites_existing_file(self) -> None:
        with TemporaryDirectory() as directory:
            output = Path(directory) / "douyin-ops.yaml"
            output.write_text("existing\n", encoding="utf-8")

            write_config(
                output,
                account_name="账号",
                brand_name="品牌",
                primary_goal="目标",
                workspace_root="/workspace",
                force=True,
            )

            self.assertIn('name: "账号"', output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
