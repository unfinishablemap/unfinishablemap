---
title: "Deep Review - Contemplative Evidence Convergence Across Traditions"
created: 2026-03-02
modified: 2026-03-02
human_modified:
ai_modified: 2026-03-02T03:52:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-4-6
ai_generated_date: 2026-03-02
last_curated:
---

**Date**: 2026-03-02
**Article**: [[contemplative-evidence-convergence-across-traditions|Contemplative Evidence Convergence Across Traditions]]
**Previous review**: [[deep-review-2026-02-22-contemplative-evidence-convergence-across-traditions|2026-02-22]]

## Finding: Stale Hugo File from Coalesce Operation

This deep review was triggered by orphan detection: the file had no inbound links. Investigation revealed the article was **coalesced** into [[contemplative-evidence-for-consciousness|Contemplative Evidence for Consciousness]] on 2026-02-22, but a stale copy remained at `hugo/content/topics/contemplative-evidence-convergence-across-traditions.md`.

### Root Cause

The coalesce operation on 2026-02-22 correctly:
- Merged content into `contemplative-evidence-for-consciousness.md`
- Moved the obsidian source to `archive/topics/contemplative-evidence-convergence-across-traditions.md`
- Created the archive redirect at `hugo/content/archive/topics/`

But it failed to delete the original `hugo/content/topics/` copy. The sync script (`scripts/sync.py`) does not clean up hugo content files that no longer have obsidian sources, so the stale file persisted.

### Resolution

- **Deleted** `hugo/content/topics/contemplative-evidence-convergence-across-traditions.md` (stale duplicate)
- **Verified** archive redirect at `hugo/content/archive/topics/` is correct (`superseded_by: /topics/contemplative-evidence-for-consciousness/`)
- **Verified** successor article has 110+ inbound links — well-integrated, no orphan concern
- **Verified** no active content files link to the old slug (only historical changelog/review references)
- **Removed** stale integrate-orphan task from todo.md

### No Content Review Needed

A full deep review was not applicable because:
1. The obsidian source no longer exists (archived)
2. The content was already reviewed before coalescence (deep-review-2026-02-22)
3. The successor article has been reviewed four times and reached stability (deep-review-2026-02-24)

## Systemic Note

The sync script should ideally detect and clean up hugo content files that have no corresponding obsidian or archive source. This would prevent stale coalesce leftovers from appearing as orphans.
