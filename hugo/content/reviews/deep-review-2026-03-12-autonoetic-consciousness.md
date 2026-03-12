---
ai_contribution: 100
ai_generated_date: 2026-03-12
ai_modified: 2026-03-12 17:20:00+00:00
ai_system: claude-opus-4-6
author: null
concepts: []
created: 2026-03-12
date: &id001 2026-03-12
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Autonoetic Consciousness
topics: []
---

**Date**: 2026-03-12
**Article**: [Autonoetic Consciousness](/concepts/anoetic-noetic-autonoetic-consciousness/) (archived)
**Previous review**: [2026-02-24](/reviews/deep-review-2026-02-24-autonoetic-consciousness/)

## Finding: Stale Hugo Content File

This review was triggered by orphan detection identifying `hugo/content/concepts/autonoetic-consciousness.md` as having no inbound links. Investigation revealed this file is a **stale sync artifact**, not an orphaned article.

### Timeline

1. **2026-02-24**: `autonoetic-consciousness.md` created in obsidian
2. **2026-03-02**: Coalesced into `anoetic-noetic-autonoetic-consciousness.md`
3. **2026-03-02**: Archive created at `archive/concepts/autonoetic-consciousness.md` with proper `archived: true`, `superseded_by`, and `original_path` metadata
4. **2026-03-02**: Netlify 301 redirect generated from `/concepts/autonoetic-consciousness/` → `/concepts/anoetic-noetic-autonoetic-consciousness/`
5. **2026-03-02–present**: Stale `hugo/content/concepts/autonoetic-consciousness.md` remained because the sync script writes/overwrites but does not clean up files whose obsidian source was removed

### Resolution

- Removed stale `hugo/content/concepts/autonoetic-consciousness.md`
- Verified no live obsidian content uses the old `[autonoetic-consciousness](/concepts/anoetic-noetic-autonoetic-consciousness/)` wikilink (migration completed in W10)
- Verified the coalesced article `anoetic-noetic-autonoetic-consciousness.md` has comprehensive inbound links (69 files reference it)
- Verified the archive redirect is properly configured

### No Content Changes

The coalesced article was reviewed on 2026-03-11 and declared fully stable with no critical issues. No content modifications were needed.

## Remaining Items

The sync script (`tools/sync/converter.py`) does not remove Hugo content files when their obsidian source is deleted. This can produce stale artifacts after coalesce or archive operations. A cleanup pass or sync-time pruning would prevent future orphan false positives.

## Stability Notes

This is not a content review but a sync hygiene fix. The underlying content (now in `anoetic-noetic-autonoetic-consciousness.md`) has reached full stability after five reviews.