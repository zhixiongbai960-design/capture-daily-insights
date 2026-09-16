#!/usr/bin/env python3
"""Read-only structural checks; cannot verify truth, emotion or quote fidelity."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
from urllib.parse import unquote


def field(text: str, key: str) -> str:
    front = re.match(r"\A---\s*\n(.*?)\n---", text, re.S)
    match = re.search(r"^" + re.escape(key) + r":\s*(.*?)\s*$",
                      front.group(1) if front else "", re.M)
    return match.group(1).strip("'\"") if match else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--insights-dir", help="Optional legacy directory override")
    args = parser.parse_args()
    root = args.archive.resolve()
    errors, warnings = [], []
    readme = root / "README.md"
    if not readme.is_file():
        print("ERROR: missing README.md")
        return 1
    declaration = readme.read_text(encoding="utf-8")
    sid = field(declaration, "subject_id")
    if not sid:
        errors.append("README lacks subject_id")
    daily_name = args.insights_dir or field(declaration, "insights_dir")
    if not daily_name:
        candidates = [name for name in ("01_日常觉察记录", "02_觉察记录", "insights", "觉察记录", "日常觉察记录")
                      if (root / name).is_dir()]
        if len(candidates) > 1:
            print("ERROR: multiple insight directories; declare insights_dir or pass --insights-dir")
            return 1
        daily_name = candidates[0] if candidates else "02_觉察记录"
    daily = (root / daily_name).resolve()
    if root not in daily.parents:
        print("ERROR: insights_dir must be inside archive")
        return 1
    index = daily / "INDEX.md"
    index_text = index.read_text(encoding="utf-8") if index.is_file() else ""
    if not index.is_file():
        errors.append("Missing insight INDEX.md")
    ids = re.findall(r"^###\s+(\d+)\s+", index_text, re.M)
    normalized = [int(x) for x in ids]
    if len(set(normalized)) != len(normalized):
        errors.append("Duplicate permanent insight IDs")
    records = list(daily.glob("????-??-??_*.md"))
    for path in records:
        text = path.read_text(encoding="utf-8")
        schema = field(text, "record_schema")
        if schema not in ("insight-v2", "insight-v3"):
            warnings.append(f"{path.name}: legacy record; no automatic backfill")
            continue
        headings = ("背景与来源", "原话记录", "情绪与态度", "核心观点", "延伸思考") if schema == "insight-v3" else ("背景", "原话记录", "情绪与态度", "核心观点", "延伸思考")
        for heading in headings:
            section = re.search(r"^## " + heading + r"\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
            if not section or not section.group(1).strip():
                errors.append(f"{path.name}: empty or missing {heading}")
        if schema == "insight-v3":
            for key in ("subject_id", "date", "recorded_at", "source_type", "status"):
                if not field(text, key):
                    errors.append(f"{path.name}: missing {key}")
            if field(text, "subject_id") != sid:
                errors.append(f"{path.name}: subject mismatch")
            for key in ("date", "recorded_at"):
                try:
                    date.fromisoformat(field(text, key))
                except ValueError:
                    errors.append(f"{path.name}: invalid {key}")
            if field(text, "date") != path.name[:10]:
                errors.append(f"{path.name}: filename/date mismatch")
        if path.name not in unquote(index_text):
            warnings.append(f"{path.name}: not referenced by insight index")
    # Check archive content, not tools/skill source code fenced examples.
    graph = {}
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if any(part.startswith(".") or part == "skills" for part in rel.parts):
            continue
        if path.is_symlink():
            warnings.append(f"{rel}: symlink not traversed")
            continue
        text = re.sub(r"\x60\x60\x60.*?\x60\x60\x60", "", path.read_text(encoding="utf-8"), flags=re.S)
        targets = re.findall(r"\[[^\]]*\]\((<[^>]+>|[^)]+)\)", text)
        graph[path.resolve()] = set()
        for target in targets:
            target = unquote(target.strip("<>").split("#", 1)[0])
            if not target or re.match(r"^[a-zA-Z][\w+.-]*:", target):
                continue
            resolved = (path.parent / target).resolve()
            if root not in resolved.parents:
                warnings.append(f"{rel}: nonportable link {target}")
                continue
            if not resolved.exists():
                errors.append(f"{rel}: missing link {target}")
            elif resolved.suffix == ".md":
                graph[path.resolve()].add(resolved)
    seen, pending = set(), [readme.resolve()]
    while pending:
        current = pending.pop()
        if current not in seen:
            seen.add(current)
            pending.extend(graph.get(current, set()) - seen)
    for orphan in sorted(set(graph) - seen):
        warnings.append(f"{orphan.relative_to(root)}: unreachable from README")
    print(f"Archive: {root}\nDated records: {len(records)}\nErrors: {len(errors)}\nWarnings: {len(warnings)}")
    for item in errors:
        print("ERROR:", item)
    for item in warnings[:30]:
        print("WARN:", item)
    if len(warnings) > 30:
        print(f"WARN: {len(warnings) - 30} additional warnings")
    print("Semantic checks still required: original quotes, attribution, emotion evidence, consent.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
