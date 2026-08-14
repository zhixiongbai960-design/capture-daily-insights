#!/usr/bin/env python3
"""Validate a portable personal insight archive without modifying it."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DATED_RECORD = re.compile(r"^(\d{4}-\d{2}-\d{2})_(.+)\.md$")
INDEX_ENTRY = re.compile(r"^###\s+(\d+)\s+(.+)$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+\.md)\)")
REQUIRED_HEADINGS = {
    "en": ("## Background", "## Core viewpoint", "## Extended thinking"),
    "zh": ("## 背景", "## 核心观点", "## 延伸思考"),
}


def discover_insights_dir(archive: Path, requested: str | None) -> Path:
    if requested:
        return archive / requested
    for name in ("insights", "觉察记录", "日常觉察记录"):
        candidate = archive / name
        if candidate.is_dir():
            return candidate
    return archive / "insights"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--insights-dir")
    args = parser.parse_args()

    archive = args.archive.resolve()
    insights = discover_insights_dir(archive, args.insights_dir)
    index = insights / "INDEX.md"
    errors: list[str] = []
    warnings: list[str] = []

    readme = archive / "README.md"
    if not readme.is_file():
        errors.append("Missing README.md")
    else:
        readme_text = readme.read_text(encoding="utf-8")
        if "subject_id:" not in readme_text:
            errors.append("README.md does not declare subject_id")

    if not insights.is_dir():
        errors.append(f"Missing insights directory: {insights.relative_to(archive)}")

    records: dict[str, Path] = {}
    if insights.is_dir():
        for path in sorted(insights.glob("*.md")):
            if not DATED_RECORD.match(path.name):
                continue
            records[path.name] = path
            record_text = path.read_text(encoding="utf-8")
            if "record_type: daily-insight" in record_text:
                valid_schema = any(
                    all(heading in record_text for heading in headings)
                    for headings in REQUIRED_HEADINGS.values()
                )
                if not valid_schema:
                    errors.append(f"{path.name}: missing standard record headings")

    if not index.is_file():
        errors.append(f"Missing index: {index.relative_to(archive)}")
    else:
        index_text = index.read_text(encoding="utf-8")
        entries = INDEX_ENTRY.findall(index_text)
        ids = [int(entry[0]) for entry in entries]
        duplicates = sorted({item for item in ids if ids.count(item) > 1})
        if duplicates:
            errors.append(f"INDEX.md contains duplicate IDs: {duplicates}")

        linked: set[str] = set()
        for target in MARKDOWN_LINK.findall(index_text):
            target_path = (insights / target).resolve()
            if not target_path.is_file():
                errors.append(f"INDEX.md link does not exist: {target}")
            linked.add(Path(target).name)

        missing = sorted(set(records) - linked)
        if missing:
            warnings.append(f"{len(missing)} dated record(s) are not linked from INDEX.md")

    print(f"Archive: {archive}")
    print(f"Insights directory: {insights}")
    print(f"Dated records: {len(records)}")
    print(f"Errors: {len(errors)}")
    for item in errors:
        print(f"ERROR: {item}")
    print(f"Warnings: {len(warnings)}")
    for item in warnings:
        print(f"WARN: {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
