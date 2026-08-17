from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PROJECT_SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TEMPLATE_SUFFIX = ".template.md"


def normalize_inline(value: str, field_name: str) -> str:
    normalized = " ".join(value.split())
    if not normalized:
        raise ValueError(f"{field_name} 不能为空")
    return normalized


def validate_project_slug(project_slug: str) -> str:
    if not PROJECT_SLUG_PATTERN.fullmatch(project_slug):
        raise ValueError("project_slug 只能包含小写字母、数字和单个连字符")
    return project_slug


def render_template(template: str, values: dict[str, str]) -> str:
    rendered = template
    for name, value in values.items():
        rendered = rendered.replace("{{" + name + "}}", value)
    return rendered


def write_video_project(
    output_root: Path,
    *,
    project_slug: str,
    title: str,
    primary_metric: str,
    changed_variable: str,
    force: bool = False,
) -> Path:
    project_slug = validate_project_slug(project_slug)
    values = {
        "PROJECT_SLUG": project_slug,
        "TITLE": normalize_inline(title, "title"),
        "PRIMARY_METRIC": normalize_inline(primary_metric, "primary_metric"),
        "CHANGED_VARIABLE": normalize_inline(changed_variable, "changed_variable"),
    }
    template_root = Path(__file__).resolve().parent.parent / "assets" / "video-project"
    templates = sorted(template_root.glob(f"*{TEMPLATE_SUFFIX}"))
    if not templates:
        raise FileNotFoundError(f"未找到视频项目模板：{template_root}")

    project_root = output_root / project_slug
    output_files = [
        project_root / template.name.replace(TEMPLATE_SUFFIX, ".md") for template in templates
    ]
    manifest_path = project_root / "project.json"
    existing = [path for path in [*output_files, manifest_path] if path.exists()]
    if existing and not force:
        raise FileExistsError(f"视频项目已存在：{project_root}；如需覆盖模板文件请使用 --force")

    project_root.mkdir(parents=True, exist_ok=True)
    for directory in ("assets/raw", "assets/selected", "assets/audio", "exports"):
        (project_root / directory).mkdir(parents=True, exist_ok=True)

    for index, template in enumerate(templates):
        output = output_files[index]
        content = render_template(template.read_text(encoding="utf-8"), values)
        output.write_text(content, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "project_slug": project_slug,
        "title": values["TITLE"],
        "primary_metric": values["PRIMARY_METRIC"],
        "changed_variable": values["CHANGED_VARIABLE"],
        "status": "brief",
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return project_root


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="创建可追踪的抖音视频项目目录")
    parser.add_argument("--output-root", type=Path, required=True, help="视频项目根目录")
    parser.add_argument(
        "--project-slug",
        required=True,
        help="小写字母、数字和连字符组成的项目标识",
    )
    parser.add_argument("--title", required=True, help="视频工作标题")
    parser.add_argument("--primary-metric", required=True, help="本次实验主指标")
    parser.add_argument("--changed-variable", required=True, help="本次唯一主变量")
    parser.add_argument("--force", action="store_true", help="覆盖已存在的模板文件")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        project_root = write_video_project(
            args.output_root,
            project_slug=args.project_slug,
            title=args.title,
            primary_metric=args.primary_metric,
            changed_variable=args.changed_variable,
            force=args.force,
        )
    except (FileExistsError, FileNotFoundError, ValueError) as error:
        raise SystemExit(str(error)) from error
    print(project_root.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
