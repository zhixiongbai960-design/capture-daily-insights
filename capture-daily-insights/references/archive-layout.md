# Archive layout

## Contents

1. Minimum archive
2. Full archive
3. Discovery and compatibility
4. Initialization templates
5. Privacy boundaries

## 1. Minimum archive

Use the minimum layout when the user is starting:

```text
personal-insight-archive/
├── README.md
└── insights/
    └── INDEX.md
```

Each new insight is an independent Markdown file inside `insights/`.

## 2. Full archive

Add components only when the user needs them:

```text
personal-insight-archive/
├── README.md
├── current-profile.md
├── information-rules.md
├── update-log.md
└── insights/
    ├── INDEX.md
    ├── ACTIONS.md
    ├── YYYY-MM-DD_topic.md
    ├── monthly-reviews/
    ├── topic-collections/
    └── behavior-analysis/
```

Responsibilities:

- `README.md`: subject identity, archive entry point, reading order, and configured paths.
- `current-profile.md`: current valid facts, projects, durable preferences, and collaboration rules.
- `information-rules.md`: fact types, conflict priority, privacy, and propagation rules.
- `insights/`: dated first-person evidence and historical evolution.
- `INDEX.md`: permanent IDs, links, and one-sentence summaries.
- `ACTIONS.md`: observable action states across review periods.
- Review folders: monthly contradictions, quarterly topic evolution, and half-year behavior analysis.

## 3. Discovery and compatibility

Prefer paths declared in `README.md` frontmatter:

```yaml
archive_type: personal-insight-archive
subject_id: unique-subject-id
subject_name: Display Name
insights_dir: insights
profile_file: current-profile.md
```

Support existing archives without forcing a rename. Common insight directory names include:

- `insights`
- `觉察记录`
- `日常觉察记录`

If an existing archive already has a valid index and naming convention, preserve it.

When no archive exists, create `personal-insight-archive/` in the current writable workspace. If that path already contains unrelated data, choose the next unused name such as `personal-insight-archive-2/`. Never overwrite an existing `README.md` or repurpose an unrelated project as an archive.

## 4. Initialization templates

Create `README.md`:

```markdown
---
archive_type: personal-insight-archive
subject_id: archive-owner
insights_dir: insights
---

# Personal Insight Archive

This archive manages one subject only. Other people, organizations, projects, and sources appear only as context for the subject's experiences and judgments.
```

Create `insights/INDEX.md`:

```markdown
---
index_type: daily-insights
order: date-desc
---

# Insight Index

New records use the current maximum permanent ID plus one.
```

Do not interrupt the first record to request identity or storage configuration. Use `archive-owner` as the stable internal ID when the user has not provided an unambiguous name, and omit `subject_name`. If the user later provides a name, add `subject_name` without changing the existing ID. These are internal archive fields, not prerequisites the user must understand.

## 5. Privacy boundaries

Treat these as private by default:

- Family and health information.
- Contact details and precise location.
- Customers, contracts, prices, revenue, and unpublished business data.
- Conflict, emotions, failure, and private history.
- Unredacted meeting transcripts and case materials.

Use private information to improve internal understanding only. Do not publish, upload, or reuse it in public content without explicit authorization.
