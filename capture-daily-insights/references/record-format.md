# Record format

## Contents

1. New record
2. Supplement an existing record
3. Index entry
4. Tags and dates

## 1. New record

Use the archive's language. Preserve the subject's first-person voice.

```markdown
---
record_type: daily-insight
subject_id: stable-subject-id
date: YYYY-MM-DD
source_type: conversation | experience | decision | external-content | chat-history
status: active
---

# Topic title

**Date:** YYYY-MM-DD
**Tags:** #tag1 #tag2 #tag3

---

## Background

Describe the trigger, scene, event, and necessary participants. Keep original timestamps for chat or meeting material. Use aliases for sensitive participants when appropriate.

## Core viewpoint

Preserve the subject's own words, structure, lists, tables, metaphors, and tone. Bold only unusually precise or powerful original sentences.

## Extended thinking

### Why this is worth preserving

Use one to three sentences. Make a judgment about durable value, not a generic reaction.

### Quotable line

Extract only an original sentence that can stand alone without changing its meaning. Otherwise write: `No separate quote needed.`

### Historical connections

- Related to YYYY-MM-DD, “Title”: explain the continuation, correction, conflict, counterexample, or shared mechanism.

When none exists, write: `No directly related historical record.`

### Direct application, when relevant

Describe a concrete application. When evidence is insufficient, do not force one.
```

## 2. Supplement an existing record

Do not rewrite the original body. Append:

```markdown
## YYYY-MM-DD supplement

### New context

Explain the new event or conversation.

### Added viewpoint

Preserve the subject's current words.

### Effect on the earlier judgment

State whether this continues, corrects, contradicts, supplies a counterexample, or adds an applicability boundary.
```

## 3. Index entry

```markdown
## YYYY-MM-DD

### 001 Topic title

- Record: [Topic title](YYYY-MM-DD_topic.md)
- Core idea: one faithful sentence summarizing the subject's judgment
```

IDs are permanent. Assign the global maximum plus one and never renumber old entries.

## 4. Tags and dates

- Use two to five stable, reusable topic tags.
- Do not diagnose personality through tags.
- Prefer the event or decision date. Use the recording date when the event date is unknown, and explain that in `Background`.
- Treat current projects, prices, relationships, and plans as dated status, not permanent facts.
