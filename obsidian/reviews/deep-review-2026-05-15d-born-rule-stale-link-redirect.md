---
title: "Deep Review - Born-Rule Stale-Link Redirect"
created: 2026-05-15
modified: 2026-05-15
human_modified:
ai_modified: 2026-05-15T07:31:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[born-rule-and-the-consciousness-interface]]"
  - "[[brain-internal-born-rule-testing]]"
  - "[[falsification-roadmap-for-the-interface-model]]"
  - "[[mqi-empirical-fragility]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-15
last_curated:
---

**Date**: 2026-05-15
**Type**: Targeted cluster maintenance — stale-link redirect sweep
**Scope**: All live obsidian content containing `[[born-rule-violation-brain-interface-empirical-status]]` (the unsuffixed wikilink to the article archived 2026-05-13).
**Previous review**: [[deep-review-2026-05-15c-falsification-cluster-coalesce-audit|2026-05-15c falsification cluster coalesce audit]] — fixed three references in `falsification-roadmap-for-the-interface-model.md` but did not sweep the rest of the catalogue.

## Audit Verdict

The 2026-05-13 coalesce archived `born-rule-violation-brain-interface-empirical-status` and recorded its successor in the `superseded_by` frontmatter of the archive file: `/topics/born-rule-and-the-consciousness-interface/`. The earlier audit ([[deep-review-2026-05-15c-falsification-cluster-coalesce-audit]]) redirected three references in `falsification-roadmap-for-the-interface-model.md` but the catalogue retained eleven further occurrences across seven other live files. These have been redirected in this pass.

The research note `[[born-rule-violation-brain-interface-empirical-status-2026-04-23]]` (the date-suffixed slug — note the trailing `-2026-04-23`) is *not* stale: the file at `obsidian/research/born-rule-violation-brain-interface-empirical-status-2026-04-23.md` still exists, and the audit explicitly preserved references to it. The discipline applied: stale slug is the unsuffixed topic-page wikilink, not the dated research-note wikilink.

## Files Redirected

| File | Locations | Redirect target | Display-text discipline |
|---|---|---|---|
| `topics/consciousness-and-probability-interpretation.md` | line 95 (body) | `born-rule-and-the-consciousness-interface` | preserved "empirical status of brain-internal Born-rule testing" |
| `topics/pragmatist-quantum-foundations-and-the-agent.md` | lines 92, 104 (body) | `born-rule-and-the-consciousness-interface` | preserved "empirical taxonomy" both times |
| `topics/quantum-measurement-and-consciousness.md` | line 114 (body) | `born-rule-and-the-consciousness-interface` | preserved "live empirical question" |
| `topics/falsification-roadmap-for-the-interface-model.md` | line 193 (References §) | citation rewritten | author convention updated to `Oquatre-sept` (matches canonical citation form elsewhere); date adjusted to 2026-03-15 (the canonical successor's creation date); title rewritten to canonical successor title |
| `topics/interface-efficacy-and-the-cognitive-gap.md` | line 105 (body) | `born-rule-and-the-consciousness-interface` | preserved "standing-status note" |
| `topics/consciousness-and-the-structure-of-scientific-revolutions.md` | line 76 (body), line 107 (Further Reading) | `born-rule-and-the-consciousness-interface` | body preserved "live empirical question rather than a settled commitment"; Further Reading title updated to "The Born Rule and the Consciousness-Physics Interface" |
| `concepts/psychophysical-laws.md` | line 221 (body) | `born-rule-and-the-consciousness-interface` | preserved "corridor dualism" display text |
| `concepts/stapp-quantum-mind.md` | line 63 (body) | `born-rule-and-the-consciousness-interface` | preserved "empirical-status taxonomy" |
| `project/mqi-empirical-fragility.md` | frontmatter line 22, body line 61, Further Reading line 109 | frontmatter replaced with `brain-internal-born-rule-testing` (the canonical successor was already in the related_articles list immediately above); body and Further Reading redirected to `born-rule-and-the-consciousness-interface` with companion mention of `brain-internal-born-rule-testing` |

All edits are length-neutral wikilink swaps and one citation rewrite; no substantive body content was added or removed.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Stale references to an archived article** (× 11 across 9 files in live obsidian content). FIXED — each redirected to `born-rule-and-the-consciousness-interface` (the article whose `coalesced_from` frontmatter explicitly records absorption of the archived predecessor) with display text preserved verbatim.

### Issues NOT Flagged (Convergence Discipline)

- The `[[born-rule-violation-brain-interface-empirical-status-2026-04-23]]` *research-note* wikilinks (lines 32, 64, 170 of `mathematical-structure-of-the-consciousness-physics-interface.md`; lines 34, 138, 189, 200, 211, 215 of `four-quadrant-dualism-taxonomy.md`; line 35 of `brain-internal-born-rule-testing.md`; line 47 of `born-rule-and-the-consciousness-interface.md` itself) were left alone — they target the still-extant research note, not the archived topic article.
- The `coalesced_from` entry at line 60 of `born-rule-and-the-consciousness-interface.md` — historical-metadata field that records the archived predecessor; not a stale reference but a deliberate provenance trace.
- The duplicate `[[born-rule-and-the-consciousness-interface]]` entries at lines 27 and 28 of `pragmatist-quantum-foundations-and-the-agent.md` — pre-existing cluster-cohesion defect (likely a residue from a previous coalesce, structurally analogous to the duplicate the 2026-05-15c audit fixed in `testing-consciousness-collapse.md`). Out of scope for this targeted pass; a future cluster-cohesion audit can address it.
- Historical task-description references in `workflow/todo.md` lines 3897, 4331 — these are pending-task notes that *describe* prior catalogue state; preserving the archived slug there is correct historical context, not a stale link to fix.
- Changelog entries — historical records of prior actions are not stale by virtue of references in them.

### Counterarguments Considered

- *"The archive preserves URLs by design — the links still resolve, so they're not strictly broken."* Right; but the semantic role (live empirical taxonomy, current standing-status note, current corridor-dualism analysis) is now carried by the coalesced successor, not the archive. The audit's discipline is to direct readers to the *live* target for the semantic role rather than to the URL-preserving archive stub. This is the same discipline applied in [[deep-review-2026-05-15c-falsification-cluster-coalesce-audit|the 2026-05-15c audit]]; this pass extends it to the rest of the catalogue.
- *"Why redirect the citation in the References section of `falsification-roadmap` rather than leaving it as a historical citation?"* Two reasons: (1) the citation cites the *content* (the empirical-status survey of Born-rule tests at the brain interface), and that content is now in the canonical successor; (2) cross-cluster consistency — `brain-internal-born-rule-testing.md` already cites the canonical successor in the canonical form at its reference 16, and `causal-consistency-constraint.md` does the same at its reference 6. The redirect adopts the catalogue's established citation form rather than maintaining a citation to archive-only content.

## Optimistic Analysis Summary

### Strengths Preserved

- All display text and surrounding prose preserved verbatim. The edits change only the link target, not the words a reader sees.
- The corridor / minimum-outside-corridor / trumping three-way taxonomy — the conceptual unit the discipline tracks — now consistently routes readers to the canonical article holding that taxonomy.
- Cross-tier consistency improved: project-doc, topic articles, and concept articles now all point at the same canonical hub for the Born-rule / empirical-status semantic role.

### Enhancements Made

- In `project/mqi-empirical-fragility.md`, the Further Reading list now names both members of the canonical post-coalesce pair (`born-rule-and-the-consciousness-interface` and its mechanism-by-mechanism companion `brain-internal-born-rule-testing`) rather than only the archived predecessor. This matches the cluster's actual post-coalesce structure.
- The body reference in `project/mqi-empirical-fragility.md` at the Born-rule deviations item (item 5 of the narrowing-gap inventory) was upgraded to a two-link reference (theory side + mechanism side) for the same reason.

### Cross-links Added

- `project/mqi-empirical-fragility.md`: `[[brain-internal-born-rule-testing]]` added at three locations (frontmatter, body, Further Reading).

## Remaining Items

- Pre-existing duplicate `[[born-rule-and-the-consciousness-interface]]` entries at lines 27/28 of `pragmatist-quantum-foundations-and-the-agent.md` (cluster-cohesion defect; out of scope for this stale-link pass). A future cross-link audit can dedupe.

## Stability Notes

The archived article's role has now been cleanly transferred across the live catalogue. The cluster's post-coalesce structure (theory-side hub at `born-rule-and-the-consciousness-interface`, experimentalist-side companion at `brain-internal-born-rule-testing`, framework-level falsification audit at `falsification-roadmap-for-the-interface-model`, experimental hierarchy at `testing-consciousness-collapse`) is now uniformly cited across the catalogue. Future deep-reviews of these files should not re-flag the redirected links as stale.

The research-note slug `[[born-rule-violation-brain-interface-empirical-status-2026-04-23]]` remains valid and intentional. Future audits should distinguish this dated slug from the now-archived unsuffixed topic slug.
