---
ai_contribution: 100
ai_generated_date: 2026-05-17
ai_modified: 2026-05-17 12:00:00+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-05-17
date: &id001 2026-05-17
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[writing-style]]'
- '[[direct-refutation-discipline]]'
- '[[evidential-status-discipline]]'
title: Deep Review - Writing Style Guide
topics: []
---

**Date**: 2026-05-17
**Article**: [Writing Style Guide](/project/writing-style/)
**Previous review**: Never (first deep review)

## Pessimistic Analysis Summary

### Critical Issues Found

- **Self-contradicting "Avoid" line (line 197)**: Said `Avoid: "the Map", "the Map", "this project"` — instructing avoidance of the exact canonical term the rest of the guide requires. Traced via `git log -p` to a regression: the original line was `Avoid: "this site", "the site", "this project"`, and an over-eager global rename of `the site → the Map` clobbered the negative examples. **Resolution**: restored to `"this site", "the site", "this project"`.

- **Stale AI pseudonym table (lines 401-404)**: Missing the `claude-opus-4-7 → Oquatre-sept, C.` and `claude-sonnet-4-7 → Sonquatre-sept, C.` entries. The frontmatter of this very file uses `ai_system: claude-opus-4-7`, and `grep` confirms `Oquatre-sept` is in active use across the catalogue (research notes, changelog entries, completed cross-review tasks). The expand-topic skill's identical pseudonym list at `.claude/skills/expand-topic/SKILL.md:159-162` already includes both. **Resolution**: added both rows so the canonical table matches the skill's table and the live usage.

- **Internal contradictions on capitalization (5 instances)**: The guide states (line 195) "Subsequent mentions: 'the Map' (lowercase 'the' mid-sentence, uppercase at sentence start)" but then violates the rule itself in bold-headed bullets at lines 135, 137, 139, 295, 303 ("**Confident, not hedged.** the Map takes positions...", etc.). After a bold-headed period, the next character is at a sentence start and must be capitalised. **Resolution**: capitalised "The Map" at all five sentence-start positions.

- **Length-guidelines staleness (lines 87-92, 113, 511)**: The guide declared `Short (500-800) / Medium (1000-1500) / Long (2000-3000)` and the checklist said "500-3000 words typically" — directly inconsistent with `tools/curate/length.py` (topics soft 3000, hard 4000; apex soft 4000, hard 5000; etc.) and inconsistent with the section-caps section of CLAUDE.md. This creates a false guidance signal that the routinely-produced 3000-4000-word articles violate style. **Resolution**: replaced with a section-keyed table matching the active thresholds (topics/concepts/apex/voids/project), with the 50,000-token context-window ceiling preserved as the absolute maximum.

### Medium Issues Found

- **Missing `description` frontmatter field**: Deep-review skill explicitly checks for this. **Resolution**: added a 200-char description summarising the guide's scope and the disciplines it ties to.

- **`the the truth` double-word typo (line 241)**: Standard typo, also fixed.

- **Mid-sentence "the the": none others found**. Grep across the file is clean after the fix.

### Counterarguments Considered

- *"Articles already use the section caps; the style guide's length guidance is read as soft suggestion."* — Considered and rejected. The guide is the canonical-document for style; when the canonical-document contradicts the enforcement tool, the tool wins by default but the contradiction degrades the guide's authority on *every* topic, including the disciplines it actually does carry uniquely. Better to keep the canonical-document calibrated.

- *"The capitalization 'the Map' at sentence start violates the bullet-as-clause convention rather than the start-of-sentence rule."* — Reviewed and rejected. Each bold heading ends with a period (`**Confident, not hedged.**`), which terminates a sentence; the next character is unambiguously at the start of the next sentence. The rule on line 195 applies.

### Attribution Accuracy Check

Source-based article check is N/A — the guide is a methodology document, not a paraphrase of an external work. The Frankish (2016) inline citation in the "Right" example at line 150 is the only attribution, and it tracks the standard illusionism-mechanistic-specification engagement; no claim is made about Frankish's beliefs.

### Reasoning-Mode Classification

The guide *describes* the engagement-mode discipline (it links to [direct-refutation-discipline](/project/direct-refutation-discipline/)) but does not itself engage a named opponent in its own prose. The illusionism "Right" example at line 150 is a *style example*, not an in-document argument. No mode-classification work required.

## Optimistic Analysis Summary

### Strengths Preserved

- **The "Right vs Wrong" before/after structure** in the Engaging Opponents and Evidential Calibration sections is genuinely instructive. Editors reading the guide can immediately see what label-leakage and bold-headed-callout failures look like and what the natural-prose replacements are. Preserved without modification.
- **The Label Blacklist (lines 178-185)** is a concrete operational checklist that catches the most-common regressions. Preserved.
- **The Citation Aging in Fast-Moving Empirical Fields section** is well-targeted: scoped to neuroimaging where the empirical churn is real, with the analogous-discipline clause covering other fast-moving fields. Preserved.
- **The Confidence Calibration table (lines 228-233)** gives a compact prose-pattern lookup for the four registers. Preserved.

### Enhancements Made

- **Length-guidelines table** now matches the enforcement tool and the CLAUDE.md section-caps table. Future automation can verify against the same numbers.
- **Pseudonym table** is now complete through the 4-7 generation, so newly-generated self-citations land on a valid pseudonym without editors having to chase the table back to the expand-topic skill.

### Cross-links Added

None added (the related_articles list is already substantive and the linked-to disciplines all back-link here).

## Stability Notes

- The "Length Guidelines" section was significantly out-of-date relative to the actual section caps. Future reviews should not undo the table-form update; the per-section numbers come from `tools/curate/length.py` and are the source of truth. If those thresholds change, the table here must be updated to match — not the other way around.
- The pseudonym table follows the canonical list in `.claude/skills/expand-topic/SKILL.md`. When new model generations land (4-8, 5-0, etc.), both lists need updating in lockstep.
- The five sentence-start "the Map" capitalisations were not stylistic disagreement — they were straightforward regressions from the guide's own rule. Re-flagging "the Map" capitalisation as a critical issue in a future review is appropriate *if* the lowercase variant returns at sentence-start positions; otherwise this is settled.
- The "Avoid:" line is now restored to its original (correct) form. If a future global-rename pass touches the `"the site"` / `"this site"` strings again, the negative examples must be excluded from the rename. Consider marking that line with a comment or moving the negative examples into a code block to discourage automated substitution.

## Remaining Items

None deferred. All issues identified in this pass were addressed.

## Word Count

3826 → 3900 (+74 words). The increase is from the length-guidelines table (which replaces three terse bullet lines with a five-row section-keyed table) and a new frontmatter `description` field. Net within length-neutral mode for a `project/` file already in hard_warning territory: the structural calibration fix is load-bearing for system coherence and the cost is small.