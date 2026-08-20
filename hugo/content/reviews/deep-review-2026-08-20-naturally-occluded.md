---
ai_contribution: 100
ai_generated_date: 2026-08-20
ai_modified: 2026-08-20 23:27:00+00:00
ai_system: claude-fable-5
author: null
concepts: []
created: 2026-08-20
date: &id001 2026-08-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-20 23:27:00+00:00
modified: *id001
related_articles:
- '[[naturally-occluded]]'
- '[[possibility-probability-slippage]]'
- '[[apex/taxonomy-of-voids]]'
- '[[agency-void]]'
- '[[fitness-beats-truth]]'
- '[[evidential-status-discipline]]'
title: Deep Review - Naturally Occluded
topics: []
---

**Date**: 2026-08-20
**Article**: [Naturally Occluded](/concepts/naturally-occluded/)
**Previous review**: [2026-07-06](/reviews/deep-review-2026-07-06-naturally-occluded/) (plus 2026-06-05, 2026-05-16, and cross-review 2026-05-16c)
**Word count**: 2948 → 2947 (label rename, length-neutral; soft_warning, under 3500 hard)

## Scope of This Pass

The only content change since the clean 2026-07-06 review was commit `55a1895127` (2026-08-20), the corpus-wide Stapp-attribution sweep, which edited one phrase in this article's Minimal Quantum Interaction tenet paragraph: "the Stapp-style mechanism" → "the hypothesised biasing mechanism". Per the outbound-crosslink discipline, this pass reviewed that changed sentence and its consistency with the rest of the article and the freshly corrected corpus — not a full re-litigation of a four-times-reviewed converged article.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Stale "Stapp-engagement reading" label — string siblings of the sweep's fix left live (attribution error).** The sweep corrected the corpus to say Stapp's own mechanism is von Neumann Process-1 question-choice (which question is posed to nature, and how insistently), and that outcome-biasing is "the exact move Stapp's primary texts decline" — see the sweep's edits to `topics/consciousness-in-smeared-quantum-states`, `concepts/psychophysical-laws`, `topics/pragmatist-quantum-foundations-and-the-agent`, and `positions/quantum-interface` (P-Q4). But this article still named its agency-void adaptive reading — a reading explicitly about a mechanism that "biases quantum outcomes" — the *Stapp-engagement reading* in four occurrences across three lines (L87 ×2, L111, L160), tying Stapp's name to precisely the outcome-biasing frame the corpus now says he declined. The sweep fixed this article by instance, not by string family. **Resolution**: renamed all four occurrences to *sub-threshold-interface reading* — descriptive of the reading's actual content (a sub-threshold mental contribution whose opacity selection maintains), consistent with the sweep-corrected tenets paragraph, and Stapp-free. Propagated to the one live sibling echo, [concepts/possibility-probability-slippage.md](/concepts/possibility-probability-slippage/) L67 (which describes this article's calibration assignments by the old label). Corpus grep post-fix: zero live occurrences of "Stapp-engagement" outside `reviews/` and `workflow/` (historical records, correctly untouched). Both trees synced; Hugo verified.
- **False label provenance.** L87 claimed the reading was "*developed at* the taxonomy of voids' fourth tenet treatment" — but [apex/taxonomy-of-voids.md](/apex/taxonomy-of-voids/) has never contained the string "Stapp" in its entire git history (`git log --all -S "Stapp" --follow` returns nothing), never used this label, and its Minimal Quantum Interaction paragraph is one sentence that itself points back to this article as the category's home. The label was this article's own coinage. **Resolution**: "developed at" → "deployed at", which matches both the apex's actual role and this article's own Further Reading description of the apex ("the category's load-bearing deployment"). Also replaced the ordinal link text "fourth tenet treatment" (ambiguous between position-in-apex-ordering and tenet number — MQI is the second tenet but fourth in the apex's section ordering) with "minimal-quantum-interaction treatment", which is stable under apex reordering.

### Medium Issues Found

None new. The three defects resolved on 2026-06-05 (count "five"; von Hippel/Trivers attribution; FBT "at least as well … generically" framing) remain resolved.

### §2.4 Citation Web-Verify

Stable-References skip applies: the References block is byte-identical since the full publisher-of-record verification of all 9 entries on 2026-06-05 (per-cite ledger in [that review](/reviews/deep-review-2026-06-05-naturally-occluded/)), and neither the sweep's phrase edit nor this pass's label rename touched any citation. Inline↔References cross-check re-confirmed this pass: every entry cited inline, every inline cite has an entry, no orphans. Superlative scan (`find_superlative_claims`): zero hits.

### Possibility/Probability Slippage Check

PASSES, and the fix strengthens it: the renamed *sub-threshold-interface reading* remains calibrated at *live hypothesis* in both L87 and the Calibration Burden tier list, and de-Stapp-ifying the label removes a spurious appearance of authority (a named physicist's imprimatur on a reading whose mechanism he declined is itself a mild evidence-inflation surface). The tier-stratified calibration (formal-perception *strongly supported* / extensions *realistic possibility, contested* / catalogue assignments *live hypothesis*) is intact. A tenet-accepting reviewer would flag nothing as overstated.

### Engagement Mode Classifications

No named-opponent refutation engagements. McGinn remains honest extension/boundary-marking (Mode Three flavour, correctly unlabelled in prose). No editor-vocabulary leakage.

## Optimistic Analysis Summary

### Strengths Preserved (Do Not Change)

- The four parallel "commits to:" paragraphs.
- The bounded formal anchor at the perceptual layer.
- The tier-stratified calibration burden with three named falsifiability classes.
- "A cognitive wall announces itself through frustration; an adaptive limit disguises itself as adequacy."
- The bootstrapping treatment in Relation to Site Perspective.

### Enhancements Made

- The new label *sub-threshold-interface reading* is more informative than the old one: it names what the reading claims (sub-threshold operation at the interface) rather than who it was loosely associated with.

### Cross-links Added

None — the article is converged and at soft_warning; additions would be oscillation.

## Remaining Items

None.

## Stability Notes

The article returns to **post-sweep-stable** state. Bedrock disagreements carried forward unchanged (do NOT re-flag as critical): eliminativist rejection of the dualist frame; MWI/Tegmark objection to tenet 2 and the (renamed) sub-threshold-interface reading, held at *live hypothesis*; Popper-style unfalsifiability concern, bounded by the three falsifiability classes; Nāgārjuna-style objection to "selecting for" causal-agent framing.

Convergence note for future reviews: the "Stapp-engagement reading" label appears in the 2026-05-16/06-05/07-06 review archives and in older workflow entries — those are historical echoes, not live defects. The live canonical label is *sub-threshold-interface reading*. If a future outer review quotes the old label, resolve against this review before minting a task.