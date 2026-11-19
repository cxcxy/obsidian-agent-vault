#!/usr/bin/env python3
"""Add a reusable Obsidian vault structure without replacing existing files."""

import argparse
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parents[1] / "assets" / "vault"
DIRECTORIES = (
    "00-收件箱",
    "05-关于我",
    "10-进行中",
    "20-专业沉淀/AI与工程",
    "20-专业沉淀/内容与创作",
    "20-专业沉淀/业务与商业",
    "30-决策与复盘",
    "40-生活与阅历",
    "50-人脉与合作",
    "80-已归档",
    "90-系统底座/附件",
    "90-系统底座/模板",
    "90-系统底座/视图",
    ".obsidian",
)
FILES = (
    ".obsidian/app.json",
    ".obsidian/templates.json",
    ".gitignore",
    "AGENTS.md",
    "CLAUDE.md",
    "SOURCE_OF_TRUTH.md",
    "首页看板.base",
    "90-系统底座/模板/知识卡片.md",
    "90-系统底座/模板/决策复盘.md",
    "90-系统底座/视图/Web-Clipper-收件箱.json",
    "90-系统底座/常用口令.md",
)


def check_destination(root, relative, directory):
    path = root / relative
    for parent in (path, *path.parents):
        if parent == root.parent:
            break
        if parent.is_symlink():
            raise ValueError(f"路径中有符号链接，请指定实际库目录：{parent}")
        if parent.exists():
            expects_directory = parent != path or directory
            matches_type = parent.is_dir() if expects_directory else parent.is_file()
            if not matches_type:
                raise ValueError(f"路径存在同名的其他类型项目：{parent}")
    return path


def initialize(root, dry_run):
    directories = [check_destination(root, item, True) for item in DIRECTORIES]
    files = [
        (check_destination(root, item, False), (TEMPLATE / item).read_bytes())
        for item in FILES
    ]

    print(f"知识库  {root}")
    for directory in directories:
        if not directory.exists():
            print(f"{'将创建目录' if dry_run else '创建目录'}  {directory.relative_to(root)}")
            if not dry_run:
                directory.mkdir(parents=True, exist_ok=True)

    for target, content in files:
        relative = target.relative_to(root)
        if dry_run or target.exists():
            print(f"{'保留文件' if target.exists() else '将创建文件'}  {relative}")
            continue
        try:
            file = target.open("xb")
        except FileExistsError:
            print(f"保留文件  {relative}")
            continue
        try:
            with file:
                file.write(content)
        except OSError:
            target.unlink()
            raise
        print(f"创建文件  {relative}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, required=True, help="Obsidian 知识库根目录")
    parser.add_argument("--dry-run", action="store_true", help="只查看将创建和保留的项目")
    args = parser.parse_args()
    try:
        root = args.vault.expanduser().absolute()
        if root.is_symlink():
            raise ValueError("请使用知识库的实际目录路径")
        root = root.resolve()
        if root in (Path.home().resolve(), Path(root.anchor)):
            raise ValueError("请为知识库指定一个单独的子目录")
        initialize(root, args.dry_run)
    except (OSError, ValueError) as exc:
        print(f"初始化中止：{exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
