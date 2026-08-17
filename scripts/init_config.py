from __future__ import annotations

import argparse
import json
from pathlib import Path

TOKEN_NAMES = {
    "ACCOUNT_NAME_JSON": "account_name",
    "BRAND_NAME_JSON": "brand_name",
    "PRIMARY_GOAL_JSON": "primary_goal",
    "WORKSPACE_ROOT_JSON": "workspace_root",
}


def render_config(
    template: str,
    *,
    account_name: str,
    brand_name: str,
    primary_goal: str,
    workspace_root: str,
) -> str:
    values = {
        "account_name": account_name,
        "brand_name": brand_name,
        "primary_goal": primary_goal,
        "workspace_root": workspace_root,
    }
    rendered = template
    for token, value_name in TOKEN_NAMES.items():
        rendered = rendered.replace(
            "{{" + token + "}}",
            json.dumps(values[value_name], ensure_ascii=False),
        )
    return rendered


def write_config(
    output: Path,
    *,
    account_name: str,
    brand_name: str,
    primary_goal: str,
    workspace_root: str,
    force: bool = False,
) -> Path:
    if output.exists() and not force:
        raise FileExistsError(f"配置已存在：{output}；如需覆盖请使用 --force")

    template_path = Path(__file__).resolve().parent.parent / "assets" / "douyin-ops.template.yaml"
    template = template_path.read_text(encoding="utf-8")
    rendered = render_config(
        template,
        account_name=account_name,
        brand_name=brand_name,
        primary_goal=primary_goal,
        workspace_root=workspace_root,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    return output


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="从模板创建抖音运营配置")
    parser.add_argument("--output", type=Path, required=True, help="输出 YAML 路径")
    parser.add_argument("--account-name", required=True, help="抖音账号名称")
    parser.add_argument("--brand-name", required=True, help="品牌或项目名称")
    parser.add_argument("--primary-goal", required=True, help="当前唯一运营目标")
    parser.add_argument("--workspace-root", required=True, help="证据文件所在工作区")
    parser.add_argument("--force", action="store_true", help="覆盖已有配置")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        output = write_config(
            args.output,
            account_name=args.account_name,
            brand_name=args.brand_name,
            primary_goal=args.primary_goal,
            workspace_root=args.workspace_root,
            force=args.force,
        )
    except FileExistsError as error:
        raise SystemExit(str(error)) from error
    print(output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
