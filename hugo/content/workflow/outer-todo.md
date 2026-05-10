---
ai_contribution: 0
ai_generated_date: 2026-05-09
ai_modified: null
ai_system: null
author: Andy Southgate
concepts: []
created: 2026-05-09
date: &id001 2026-05-09
draft: false
human_modified: 2026-05-09
last_curated: null
modified: *id001
related_articles:
- '[[project]]'
- '[[pending-reviews]]'
title: Outer Review Subject Queue
topics: []
---

This is the user-curated subject queue for the outer-review system. The next cycle (chatgpt 02:00, claude 03:00, gemini 04:00 UTC) consumes the top-priority open task here, and **all three services review the same subject on the same day**. The synthesis pass (`/combine-outer-reviews`) then weights findings by how many reviewers converged.

## When this list is empty

The system falls back to:

1. A **full-site review** if none has run in the last 7 days, else
2. An **un-outer-reviewed article** modified between 7 and 60 days ago (7-day buffer for SEO indexing; 60-day window for re-eligibility).

If both fallbacks come up empty, the cycle skips quietly.

## How to add a task

Append a `### P{N}: {title}` block. P0 jumps the queue; P1/P2/P3 are FIFO within their priority class. Just ask Claude to add one.

```
### P1: How robust is the dualism-as-ai-risk-mitigation argument under serious AI-safety scrutiny?
- **Articles**: topics/dualism-as-ai-risk-mitigation.md, apex/consciousness-and-ai-risk.md
- **Notes**: Recent rapid expansion; want a stress-test from outside the project's assumptions.
- **Added**: 2026-05-09
```

`Articles` and `Notes` are optional but recommended — they steer prompt composition.

When a task is consumed, the `### P{N}:` line is rewritten in place to `### ✓ {cycle-date}:` with a `- **Reviewed**: cycle YYYY-MM-DD` footer, matching `todo.md`'s completion convention. The file thus serves as both queue and audit log.

## Tasks

### ✓ 2026-05-10: Review topics/phenomenology-of-memory-and-the-self.md
- **Articles**: topics/phenomenology-of-memory-and-the-self.md
- **Added**: 2026-05-09
- **Reviewed**: cycle 2026-05-10

### ✓ 2026-05-10: Test subject — does the dualism-as-ai-risk-mitigation argument survive AI-safety scrutiny?
- **Articles**: topics/dualism-as-ai-risk-mitigation.md, apex/consciousness-and-ai-risk.md
- **Notes**: Recent rapid expansion; want a stress-test from outside the project's assumptions.
- **Added**: 2026-05-09
- **Reviewed**: cycle 2026-05-10