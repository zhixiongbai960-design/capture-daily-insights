# Capture Daily Insights

把日常对话、决策、经历和会议材料中的有效认知，沉淀为可检索、可关联、可回顾的个人认知资产。

这是一个面向 Codex 及其他支持 `SKILL.md` 工作流的 Agent Skill。用户只需要自然讲述自己的观点或经历，Agent 会负责：

- 判断什么值得长期记录；
- 区分用户原话、他人观点和 Agent 分析；
- 保存独立 Markdown 记录；
- 更新永久序号索引；
- 连接真正相关的历史觉察；
- 追踪具体行动；
- 生成月度、季度和半年回顾。

## 一句话安装

复制下面整句话，发送给支持 Skill 的 Agent：

```text
请使用 Skill Installer 安装这个 Agent Skill：
https://github.com/zhixiongbai960-design/capture-daily-insights/tree/main/capture-daily-insights
安装完成后告诉我；如果需要重新加载或从下一轮对话开始生效，也请明确说明。
```

安装完成后，第一次使用可以直接说：

```text
使用 $capture-daily-insights，在当前工作区为我建立一个最小个人觉察档案。我的 subject_id 是 your-id，记录目录使用 insights/。
```

以后只需要自然表达，并在需要时补一句“帮我记一下”：

> 我今天意识到，真正让我不舒服的不是方案被拒绝，而是责任没有说清楚。帮我记一下。

## 为什么做这个 Skill

觉察记录不是流水账。它关注的是：

- 我看见了什么；
- 我形成了什么判断；
- 我为什么做出这个决定；
- 哪些经验可以复用；
- 我的观点如何随经历变化；
- 这条认知有没有真正转化成行动。

使用通用 Markdown 文件保存后，个人认知不再绑定某一个聊天窗口或 AI 工具。整个目录可以备份、搜索、交给新的 Agent 读取，也可以长期观察自己的认知演化。

## 仓库结构

```text
capture-daily-insights/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── archive-layout.md
│   ├── record-format.md
│   └── review-system.md
└── scripts/
    └── archive_check.py
```

仓库根目录的 `README.md` 和 `LICENSE` 用于公开发布，不属于 Skill 运行时必需文件。

## 也可以整理聊天或会议

> 下面是一段会议记录。先区分各方立场，再把属于我的观点整理成觉察。如果有多个独立主题，可以拆分。

如果所用 Agent 不支持自动安装 Skill，可以手动下载仓库中的 `capture-daily-insights/` 文件夹，整体放入该 Agent 的个人 Skill 目录。不要只复制 `SKILL.md`，否则模板、回顾规则和检查脚本不会一起安装。

## 最低档案结构

```text
personal-insight-archive/
├── README.md
└── insights/
    ├── INDEX.md
    └── YYYY-MM-DD_topic.md
```

记录稳定后，可以增加当前画像、信息管理规则、行动追踪、月度回顾、季度主题合集和半年行为分析。

## 核心原则

1. 一个档案只管理一个主体。
2. 用户原话、他人观点和 Agent 分析必须分开。
3. 不把一次情绪写成永久人格结论。
4. 新观点不覆盖旧观点，保留认知变化路径。
5. 只有真正相关的记录才建立历史关联。
6. 记录不是行动，具体行动需要持续追踪结果。
7. 家庭、客户、合同、金额和未公开项目默认属于私密材料。

## 校验档案

```bash
python3 capture-daily-insights/scripts/archive_check.py --archive /path/to/personal-insight-archive
```

校验器检查：

- `README.md` 和 `subject_id`；
- 觉察目录与 `INDEX.md`；
- 标准记录标题；
- 重复永久序号；
- 失效链接；
- 未进入索引的日期记录。

## 适配已有档案

Skill 不强制所有人使用同一语言或目录名。它可以识别：

- `insights/`
- `觉察记录/`
- `日常觉察记录/`

已有档案应保留原来的有效命名和索引方式，不需要为了使用 Skill 整体改名。

## 隐私提醒

觉察档案可能包含比普通笔记更敏感的内容。建议：

- 默认保存在本地或私有仓库；
- 公开案例前删除客户、合同、金额、联系方式和未脱敏对话；
- 不把他人的观点误记成自己的长期认知；
- 不把个人档案和这个公共 Skill 仓库混在一起提交。

## License

MIT
