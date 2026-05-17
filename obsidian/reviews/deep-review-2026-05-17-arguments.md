---
title: "Deep Review - Arguments"
created: 2026-05-17
modified: 2026-05-17
human_modified: null
ai_modified: 2026-05-17T11:05:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-17
last_curated: null
---

**Date**: 2026-05-17
**Article**: [[arguments|Arguments]] (section index)
**Previous review**: [[deep-review-2026-01-31-arguments|2026-01-31]]

## Context

Since the 2026-01-31 review the section index has accumulated three substantive changes:
- A new "Occam's Razor Has Limits" subsection was added (2026-03-14) summarising the dedicated `arguments/epistemological-limits-of-occams-razor.md` article.
- Slug-rename fixes touched some wikilinks (2026-03 sweeps).
- The `arguments/materialism-argument.md`, `arguments/functionalism-argument.md`, and `arguments/many-worlds-argument.md` detail pages have all received deep reviews and refinements that the index summaries should reflect accurately.

This pass audits the index's accuracy against the current state of each detail page and tightens the routing so each "Discussion" line points to the dedicated argument article first, then to relevant concept or void pages.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Argument-count mismatch (Epiphenomenalism)**. The index claimed *"five arguments showing that epiphenomenalism is self-undermining"* but `arguments/epiphenomenalism-argument.md` numbers exactly four arguments (Self-Stultification, Evolutionary Objection, Knowledge Argument Reversed, Introspection and Self-Knowledge). **Resolution**: corrected to "four arguments" and added the missing Knowledge-Argument-Reversed bullet so the four "Key claims" mirror the four numbered arguments in the detail page. The previous fourth bullet ("the self-knowledge problem") collapsed two separable concerns into one; rewritten to track the introspection argument as the detail page does.
- **Mismatched Discussion link (Occam's Razor)**. The "Key claims" for the Occam's Razor section paraphrase the *arguments* page (precondition unmet, simplicity fragments, transfer failure, historical failures), but the only Discussion link `[[epistemological-limits-occams-razor]]` resolved to `voids/epistemological-limits-occams-razor` (*The Parsimony Void*), which treats the topic as a cognitive-bias void rather than as the philosophical argument. **Resolution**: discussion line now points to `[[epistemological-limits-of-occams-razor]]` first (the arguments page that matches the key-claims summary), then to `[[parsimony-case-for-interactionist-dualism]]` (the positive case), then to `[[epistemological-limits-occams-razor]]` (The Parsimony Void) for the cognitive-architecture angle.

### Medium Issues Found

- **Materialism Discussion link pointed only to concept page**, breaking the routing pattern established by Many-Worlds (which links to both argument + concept). **Resolution**: now links to `[[materialism-argument|Against Materialism]]` first, then `[[concepts/materialism|Materialism]]`.
- **Functionalism Discussion link used the archived alias** `[[arguments/functionalism|functionalism]]` (resolves via redirect from the archived rename). **Resolution**: now links to `[[functionalism-argument|Against Functionalism]]` first, then `[[concepts/functionalism|Functionalism]]`, matching the Many-Worlds and Materialism patterns.
- **Opening paragraph LLM-cliché**: *"These are not balanced 'both sides' treatments—they are explicit defenses of the map we're building"* matched the "This is not X. It is Y." pattern flagged in the writing-style guide. **Resolution**: rephrased to *"The treatments here are openly partisan—explicit defences of the map we're building rather than balanced 'both sides' surveys"*, keeping the same partisan-disclosure work while removing the LLM cadence.

### Low Issues Found

- The Materialism "Key claims" mention "eliminative, reductive, and non-reductive physicalism" while the detail page now also treats the phenomenal-concept strategy as a fourth form. Deferred — adding a fourth bullet to the index summary would lengthen it without proportionate gain; the detail page is where that nuance properly lives.

### Counterarguments Considered

Six adversarial personas re-applied to the index page:
- **Eliminative Materialist**: bullet on "explanatory gap is not merely epistemic" is an in-Map summary claim pointing to a detail page; appropriate framing for an index. Not critical.
- **Hard-Nosed Physicalist**: would dispute every key claim — but the page's opening paragraph explicitly discloses partisan framing, which absorbs the methodological complaint at the section-introduction level (Mode Three boundary-marking, implicit at the section level).
- **Quantum Skeptic**: the claim *"Quantum mechanics is not causally closed in the way materialism requires"* is the single most contentious index-level assertion. It is correctly presented as a summary pointing to detail pages, not as a stand-alone claim. Acceptable for an index, though the detail page (`materialism-argument.md`) carries the load of defending it.
- **Many-Worlds Defender**: bedrock disagreement on the indexical argument is expected at the framework boundary. Not critical.
- **Empiricist**: would complain that "presents X arguments" sounds empirical when the section is metaphysical; the wording is accurate description of what each detail page does, not a claim of empirical confirmation. Acceptable.
- **Buddhist Philosopher**: the "explicit defences" framing is honest about partisanship; no critique surfaces here that the detail pages don't already absorb.

### Attribution Accuracy Check

- "Seven arguments" claim for Interactionist Dualism: ✓ verified against `concepts/interactionist-dualism.md` line 94–96 ("Seven arguments converge on the interactionist conclusion").
- "Four arguments" for Epiphenomenalism: ✓ now matches the four numbered arguments in `arguments/epiphenomenalism-argument.md`.
- "Five arguments" for Functionalism: ✓ matches the five numbered arguments in `arguments/functionalism-argument.md`.
- "Chalmers' zombie argument": ✓ standard attribution.
- No source/Map conflation; no dropped qualifiers; no internal contradictions.

### Reasoning-Mode Classification (editor-internal)

This is an index/landing page. It does not engage named opponents in argumentative dialogue — it points to detail pages that do. The opening paragraph's partisan-disclosure is Mode Three boundary-marking *for the section as a whole*; persona engagement happens on the detail pages. No label leakage; no editor-vocabulary in prose. No engagement classifications needed at the index level.

### Calibration Check (possibility/probability slippage)

The index summaries make qualitative claims about what each detail page argues — no evidential-status tier is asserted at the index level. No slippage between defeater-removal and evidence-upgrade detected. Calibration verdict: clean.

## Optimistic Analysis Summary

### Strengths Preserved

- Honest "openly partisan" framing in opening (refined from prior "These are not… they are…" cliché but the partisan disclosure is preserved and arguably strengthened).
- "Key claims" + "Discussion" structure for each section — excellent for LLM truncation resilience; the bullets front-load the substantive claims before the reader reaches a link.
- The "Relation to Site Perspective" section's cumulative-case paragraph: *"rejecting materialism motivates dualism; rejecting epiphenomenalism requires interaction; the mechanism for interaction requires collapse interpretations that reject many-worlds"* — preserved unchanged. This is the index's most distinctive contribution: it doesn't just list arguments, it explains how they interlock.
- All five tenet anchors used in the Relation section — full coverage of the foundational commitments the arguments defend.

### Enhancements Made

- **Fixed Epiphenomenalism argument count** (5 → 4) and added the missing Knowledge-Argument-Reversed bullet so the four bullets match the four numbered arguments in the detail page.
- **Repaired the Occam's Razor routing**: the dedicated arguments page (`epistemological-limits-of-occams-razor`) is now the primary Discussion link; the positive case (`parsimony-case-for-interactionist-dualism`) is now linked alongside it; the void (`epistemological-limits-occams-razor`) remains as the cognitive-architecture pointer.
- **Normalised Discussion-line pattern across all sections**: every section now points to its dedicated argument page first, then to relevant concept/void pages, matching the Many-Worlds pattern that was already correct. Materialism and Functionalism now follow the same routing convention.
- **Removed "X is not Y. It is Z." LLM-cliché** from the opening paragraph while preserving the partisan-disclosure work.

### Cross-links Added

- `[[materialism-argument|Against Materialism]]` (was missing — the dedicated arguments page is now linked from the index for the first time).
- `[[functionalism-argument|Against Functionalism]]` (replaces the archived-alias link that was going through a redirect).
- `[[concepts/functionalism|Functionalism]]` (concept page now linked alongside the arguments page).
- `[[epistemological-limits-of-occams-razor|Epistemological Limits of Occam's Razor]]` (the dedicated arguments page — previously the section only pointed to the voids page despite using arguments-page language in its key claims).
- `[[parsimony-case-for-interactionist-dualism|The Parsimony Case for Interactionist Dualism]]` (the positive parsimony case, now connected from the section that previously only offered the defensive case).

### Effective Patterns

- The bullet-then-Discussion-link pattern is preserved and now uniformly applied: every section has 3–5 substantive "Key claims" bullets followed by a Discussion line that points to one or more detail pages. This is index-design done right for LLM consumption — the key claims survive even if the link list is truncated.

## Remaining Items

None. The article is stable.

## Stability Notes

- This is the second deep review (first was 2026-01-31). The first review added the "Relation to Site Perspective" section; this review fixes routing/attribution issues that accumulated as detail pages were added and renamed.
- **Future reviews should NOT re-flag the partisan-disclosure paragraph as a problem**. The framing is the page's most distinctive feature and is the intended philosophical stance of the section.
- **Future reviews should NOT re-flag the "Quantum mechanics is not causally closed" bullet as critical**. It is an index summary pointing to a detail page that defends it; treating the index as the load-bearing claim would be a category mistake.
- **Bedrock disagreements that future reviews should NOT re-flag**: MWI defenders will reject the indexical-problem bullet; eliminativists will reject the explanatory-gap bullet; functionalists will reject the absent-qualia bullet. These are expected framework-boundary disagreements, not flaws.
- Word count: 725 → 759 (+34 words; +5%). Well below soft threshold of 2500. The added words come almost entirely from expanded Discussion lines (one extra link target plus display text); the body argument text is essentially unchanged in length.
- Future reviews should fire only on:
  - New sections added to the index (e.g., a new argument category).
  - Detail-page renames that break the wikilinks here.
  - Argument-count changes on linked detail pages (the failure mode caught this pass).
  - Style-guide changes that affect the index pattern.
