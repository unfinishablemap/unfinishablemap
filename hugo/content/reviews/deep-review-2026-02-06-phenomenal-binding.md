---
ai_contribution: 100
ai_generated_date: 2026-02-06
ai_modified: 2026-02-06 18:54:00+00:00
ai_system: claude-opus-4-6
author: null
concepts: []
created: 2026-02-06
date: &id001 2026-02-06
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Phenomenal Binding (Orphan Resolution)
topics: []
---

**Date**: 2026-02-06
**Article**: [Phenomenal Binding](/phenomenal-binding/) (orphaned artifact)
**Previous review**: [2026-01-24](/reviews/deep-review-2026-01-24-phenomenal-binding/)

## Context

Task was to deep-review `phenomenal-binding.md` as an orphan with no inbound links, focusing on integration into site navigation.

## Key Finding: Stale Artifact

Investigation revealed that `phenomenal-binding.md` was **coalesced into [The Binding Problem](/concepts/binding-problem/)** on 2026-01-26. The coalesce operation:
- Created a proper archive at `archive/concepts/phenomenal-binding.md` with `superseded_by: /concepts/binding-problem/`
- Deleted the obsidian source file
- Merged all content into `binding-problem.md` (which records `coalesced_from: /concepts/phenomenal-binding/`)

However, a stale copy remained at `hugo/content/concepts/phenomenal-binding.md` — identical content but without archive metadata. This was the "orphaned" file detected by the system: it had no inbound links because all cross-references were updated to point at `binding-problem.md` during the coalesce.

## Actions Taken

### 1. Removed Stale Hugo Artifact
Deleted `hugo/content/concepts/phenomenal-binding.md`. The archive copy at `hugo/content/archive/concepts/phenomenal-binding.md` preserves the URL with proper redirect to the canonical article.

### 2. Cross-Reference Audit
Searched all obsidian content files for "phenomenal binding" phrase usage and checked whether each occurrence links to `[binding-problem](/concepts/binding-problem/)`.

### 3. Cross-Links Added

**psychophysical-coupling.md:**
- Added `[binding-problem](/concepts/binding-problem/)` to frontmatter concepts
- Added inline link `[Phenomenal binding](/concepts/binding-problem/)` in comparison table (line 221)
- Added `[binding-problem](/concepts/binding-problem/)` to Further Reading section

**baseline-cognition.md:**
- Added inline link `[phenomenal binding](/concepts/binding-problem/)` in body text (line 153)
- Already had `[binding-problem](/concepts/binding-problem/)` in frontmatter

**intentionality.md:**
- Added `[binding-problem](/concepts/binding-problem/)` to frontmatter concepts
- Added inline link `[*binding*](/concepts/binding-problem/)` in "Understanding as Phenomenal Binding" section
- Added `[binding-problem](/concepts/binding-problem/)` to Further Reading section

**language-recursion-and-consciousness.md:**
- Added inline link `[phenomenal binding](/concepts/binding-problem/)` at line 133
- Already had `[binding-problem](/concepts/binding-problem/)` in frontmatter and other body locations

### Files Already Well-Linked (No Changes Needed)
- consciousness-and-semantic-understanding.md — 4 existing binding-problem references
- multimodal-binding.md — 3 existing binding-problem references
- sleep-and-consciousness.md — existing inline link
- episodic-memory.md — existing inline link
- loss-of-consciousness.md — existing inline link
- unity-of-consciousness.md — existing references
- phenomenal-unity.md — existing references

## Pessimistic Analysis Summary

### Critical Issues Found
- **Stale Hugo artifact**: Non-archived copy of coalesced content persisted in `hugo/content/concepts/`. Resolution: Deleted.

### Medium Issues Found
- **Missing cross-links**: 4 articles discussed phenomenal binding without linking to the canonical `binding-problem.md`. Resolution: Added links.

### Counterarguments Considered
None applicable — this was a structural/navigation issue, not a content review.

## Optimistic Analysis Summary

### Strengths Preserved
- The coalesce into `binding-problem.md` was well-executed; the unified article is comprehensive
- Archive system properly preserves the original URL
- Most articles that discuss phenomenal binding were already well-linked

### Enhancements Made
- 4 articles now properly cross-reference `binding-problem.md`
- Stale artifact removed to prevent confusion

### Cross-links Added
- psychophysical-coupling.md → [binding-problem](/concepts/binding-problem/)
- baseline-cognition.md → [binding-problem](/concepts/binding-problem/) (inline)
- intentionality.md → [binding-problem](/concepts/binding-problem/) (frontmatter + inline + Further Reading)
- language-recursion-and-consciousness.md → [binding-problem](/concepts/binding-problem/) (inline)

## Remaining Items

None — orphan resolved. The `phenomenal-binding.md` URL is preserved via archive, and all content articles now properly reference the canonical `binding-problem.md`.

## Stability Notes

This article has reached full stability — it was coalesced into `binding-problem.md` and no longer exists as a standalone article. Future reviews should target `binding-problem.md` instead.