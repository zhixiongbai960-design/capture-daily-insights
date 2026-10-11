#!/usr/bin/env python3
"""Create a portable insight archive without overwriting existing files."""
from __future__ import annotations

import argparse
from pathlib import Path
import uuid


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", required=True, type=Path)
    args = parser.parse_args()
    root = args.archive.expanduser().resolve()
    skill = Path(__file__).resolve().parents[1]
    if root == skill or skill in root.parents:
        parser.error("Archive must not be inside the skill installation.")
    readme = root / "README.md"
    if readme.exists() and "archive_type: personal-insight-archive" not in readme.read_text(encoding="utf-8"):
        parser.error("Existing archive or unrelated README: inspect and adapt manually; nothing overwritten.")
    if root.exists() and not readme.exists() and any(root.iterdir()):
        parser.error("Nonempty directory without an archive declaration; choose a dedicated directory.")
    if readme.exists():
        # This initializer only knows its own default layout. Custom layouts
        # belong to the Agent, not to a guessed migration.
        existing = readme.read_text(encoding="utf-8")
        for line in ("insights_dir: 02_觉察记录", "profile_dir: 01_个人画像",
                     "exploration_dir: 00_个人探索", "reviews_dir: 03_复盘与行动",
                     "guides_dir: 99_使用说明"):
            if line not in existing:
                parser.error("Customized layout: inspect manually; nothing overwritten.")
    sid = uuid.uuid4().hex
    files = {
        "README.md": f"""---
archive_type: personal-insight-archive
subject_id: {sid}
insights_dir: 02_觉察记录
profile_dir: 01_个人画像
exploration_dir: 00_个人探索
reviews_dir: 03_复盘与行动
guides_dir: 99_使用说明
---

# 个人觉察档案

个人资料默认私密，不因安装 Skill 而授权公开或外发。
可以直接说“记一下”，或“带我梳理热爱、擅长和价值观”。两者可以并行。
需要总结时说“整理画像”，Agent 会结合问卷与近半年记录更新画像，并保留完整历史版本。
先讨论不记录时请直接说明，批量材料可等发完再整理。

- [个人探索](00_个人探索/INDEX.md)
- [个人画像](01_个人画像/INDEX.md)
- [觉察记录](02_觉察记录/INDEX.md)
- [复盘与行动](03_复盘与行动/INDEX.md)
- [使用说明](99_使用说明/INDEX.md)
""",
        "00_个人探索/INDEX.md": """# 个人探索

[档案入口](../README.md)

可自行填写后上传，也可让 Agent 分轮提问；不适用或不愿回答的题可以跳过。

- [热爱擅长价值观](热爱擅长价值观_空白模板.md)
- [人生关键事件](人生关键事件_空白模板.md)
""",
        "01_个人画像/INDEX.md": "# 个人画像\n\n[档案入口](../README.md)\n\n尚未建立画像。说“整理画像”后，根据有来源的回答与记录生成；实质更新保留完整历史版本。\n",
        "02_觉察记录/INDEX.md": "# 觉察记录\n\n[档案入口](../README.md)\n\n按日期倒序，记录永久序号从 001 开始。\n",
        "03_复盘与行动/INDEX.md": "# 复盘与行动\n\n[档案入口](../README.md)\n\n- [行动追踪](行动追踪.md)\n\n月度、季度和年度报告生成后在此链接。\n",
        "03_复盘与行动/行动追踪.md": """# 行动追踪

[复盘索引](INDEX.md)

只有本人确认的行动计入承诺；无反馈不等于未行动。

| ID | 来源 | 动作 | 采纳状态 | 确认日期 | 观察标准／时点 | 进展 | 结果证据 | 更新时间 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
""",
        "99_使用说明/INDEX.md": "# 使用说明\n\n[档案入口](../README.md)\n\n- [自动复盘任务提示词](自动复盘任务提示词.md)\n- [复盘规则](复盘规则.md)\n",
    }
    for source, dest in (("self-discovery.md", "热爱擅长价值观_空白模板.md"),
                         ("life-events.md", "人生关键事件_空白模板.md")):
        files["00_个人探索/" + dest] = (skill / "assets" / source).read_text(encoding="utf-8")
    prompts = (skill / "references/automation-prompts.md").read_text(encoding="utf-8")
    prompts = prompts[prompts.index("## 月度任务"):]
    files["99_使用说明/自动复盘任务提示词.md"] = (
        "# 自动复盘任务提示词\n\n[使用说明](INDEX.md)\n\n"
        "以下仅是提示词，尚未创建任何任务。分别复制给支持定时任务的 Agent。\n\n"
        + prompts.replace("{{ARCHIVE_PATH}}", str(root)))
    reviews = (skill / "references/reviews.md").read_text(encoding="utf-8")
    reviews = reviews[reviews.index("## 共通规则"):]
    files["99_使用说明/复盘规则.md"] = "# 复盘规则\n\n[使用说明](INDEX.md)\n\n" + reviews
    # Refuse symlinked destinations before any mutation.
    for rel in files:
        target = root / rel
        if target.is_symlink() or root not in target.resolve().parents:
            parser.error("Unsafe destination: " + str(target))
    for rel in ("02_觉察记录/附件", "03_复盘与行动/月度复盘",
                "03_复盘与行动/季度复盘", "03_复盘与行动/年度复盘"):
        target = root / rel
        if target.is_symlink() or root not in target.resolve().parents:
            parser.error("Unsafe directory: " + str(target))
        target.mkdir(parents=True, exist_ok=True)
    created = 0
    for rel, content in files.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with target.open("x", encoding="utf-8") as stream:
                stream.write(content)
            created += 1
        except FileExistsError:
            pass
    print(f"Archive: {root}\nCreated: {created}\nExisting files preserved. No scheduled tasks created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
