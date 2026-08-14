---
name: capture-daily-insights
description: Capture and maintain a single person's reflections as a structured, portable personal knowledge archive. Use when the user asks to record or save an insight, shares a reusable viewpoint, makes an important decision with reasons, extracts a lesson from experience, notices a pattern or counterintuitive idea, responds personally to external material, supplies chat or meeting history for organization, or requests monthly contradiction reviews, quarterly topic consolidation, half-year behavior analysis, index maintenance, or action follow-up. Do not use for temporary factual queries, pure task execution, casual chat without personal judgment, or external content the user has not adopted or commented on.
---

# Capture Daily Insights

Maintain a personal cognitive asset archive for exactly one subject. Treat other people, organizations, projects, and sources only as context for the subject's experiences and judgments.

## Locate or initialize the archive

Read [references/archive-layout.md](references/archive-layout.md) completely.

Resolve the archive root in this order:

1. Use the path explicitly provided by the user.
2. Use the current workspace when its `README.md` declares `archive_type: personal-insight-archive` or an equivalent single-person archive.
3. Use an existing workspace directory named `insights`, `觉察记录`, or `日常觉察记录`.
4. If no archive exists and the user asked to record, initialize the minimum archive described in `archive-layout.md` inside the current workspace.

Before writing, read the archive `README.md`, the insight index, and any information-management rules that exist. Read the current profile only when the new material could affect current identity, projects, collaboration rules, or long-term preferences.

## Decide whether to record

Record when any of these applies:

- The user explicitly says to record, save, or note something.
- The user states a reusable personal viewpoint, judgment, pattern, or counterintuitive idea.
- The user makes an important choice and explains why.
- The user extracts a reusable lesson from an experience.
- The user responds to external material with agreement, disagreement, correction, or personal inspiration.
- The user provides chat, meeting, or voice-transcript material for organization.

Do not record:

- Temporary lookups or pure task execution.
- Casual conversation with no durable personal judgment.
- Pure factual retelling with no personal interpretation.
- External content the user has not personally adopted or discussed.
- Agent-generated ideas the user has not confirmed.

When the user explicitly asks to record, proceed without asking for another confirmation. When the trigger is implicit and ambiguous, suggest recording instead of creating a low-value file.

## Verify ownership of every statement

Separate four voices before writing:

1. **Subject's own words**: place in `Core viewpoint`; preserve tone and structure.
2. **Other people or external sources**: place in `Background`; name the source or use a privacy-safe alias.
3. **Subject's response to external material**: record only the agreement, disagreement, addition, or correction the subject actually expressed.
4. **Agent inference**: place only in `Extended thinking`; label it as analysis or a hypothesis.

Never turn another person's business, identity, or opinion into the subject's information. Never turn one emotion or one statement into a permanent personality conclusion.

## Create or update records

Read [references/record-format.md](references/record-format.md) completely and follow it.

Before saving:

1. Search same-date, same-topic, and near-synonym filenames and index entries.
2. Append a dated supplement to an existing record when the new material extends the same insight.
3. Create separate records only when the material contains independent themes that users will need to retrieve separately.
4. Preserve the user's numbering, lists, tables, metaphors, and strong original sentences.
5. Do not beautify, academicize, or overinterpret the user's voice.

Save records as `YYYY-MM-DD_topic-keywords.md` in the configured insights directory.

## Update the index and actions

For every new record:

1. Assign the global maximum permanent index number plus one. Never reuse an ID.
2. Sort index entries by date descending and, within a date, by ID descending.
3. Add the title, relative link, and one-sentence summary.
4. Add an action to the action tracker only when it is concrete, observable, and can later be marked `observing`, `needs confirmation`, `not started`, `implemented`, or `abandoned`.

Link historical insights only when there is a real continuation, correction, conflict, counterexample, or shared mechanism. Do not connect entries merely because they share keywords.

## Propagate carefully

Default to adding only the insight and index entry.

Update a current profile only when:

- The user corrects an existing fact.
- The record contains an important current identity, project, collaboration, or status change.
- The user confirms a durable rule or preference.
- A pattern recurs across time and has behavioral or outcome evidence.

Preserve historical records even when the user's view changes. Add a dated note rather than rewriting the past to match the present.

## Run periodic reviews

For monthly, quarterly, or half-year reviews, read [references/review-system.md](references/review-system.md) completely and execute only the requested period.

Reviews exist to reveal change and close action loops, not to produce attractive summaries. Present contradictions without moral judgment. Distinguish changed beliefs, changed contexts, unfulfilled commitments, and genuine inconsistency.

## Validate and report

When the archive uses the standard layout, run:

```bash
python3 <skill-directory>/scripts/archive_check.py --archive <archive-root>
```

Fix problems caused by the current change. Report pre-existing issues without rewriting unrelated historical material.

Finish with a concise response containing:

- The recorded topic and file link.
- One sentence explaining its core value.
- A short note if records were split, the profile changed, or validation found issues.

Do not repeat a long essay after the files have already been written.
