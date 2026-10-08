---
ai_contribution: 100
ai_generated_date: 2026-10-08
ai_modified: 2026-10-08 01:40:28+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-08
date: &id001 2026-10-08
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-08 01:40:28+00:00
modified: *id001
related_articles: []
title: Deep Review - Pain Asymbolia
topics: []
---

**Date**: 2026-10-08
**Article**: [Pain Asymbolia](/concepts/pain-asymbolia/)
**Previous review**: [2026-07-16](/reviews/deep-review-2026-07-16-pain-asymbolia/) (7th prior review; also 2026-02-20, 2026-02-23, 2026-03-19, 2026-04-23, 2026-06-02, 2026-06-19)

Eighth deep review of a strongly converged article. It re-qualified legitimately: four refine-draft commits since 2026-07-16 (54220f1a99, 9b1e76b101, 597c8f2ce9, e6ae985948) added two new body paragraphs, five new citations (Feinstein 2016; Klein 2015; Gerrans 2020; Gerrans 2024; plus cross-modal-capability-division scaffolding) and four quoted phrases that no review had grep-verified against the raw source. Scrutiny was scoped to that strand plus the result-direction leg on the pre-existing empirical cites. Bedrock standoffs recorded in prior stability notes were not re-litigated.

**Word count**: 2889 → 2968 (+79; concepts gate 3500).

## Pessimistic Analysis Summary

### Critical Issues Found

**Wrong-work attribution: the anterior-cingulate PET finding was credited to Rainville et al. (1999), which reports no imaging — FIXED.** §"Complementary Dissociations" read: *"Rainville et al. (1999) found that hypnotic suggestions targeting unpleasantness modulate anterior cingulate activity while preserving primary somatosensory responses."* The 1999 *Pain* paper (82(2), 159–171; PMID 10467921) is a three-experiment psychophysical study — intensity and unpleasantness ratings plus heart rate, no PET — whose result is that unpleasantness modulation was "largely independent of variations in perceived pain intensity". The ACC-but-not-S1 result is Rainville, Duncan, Price, Carrier & Bushnell (1997), *Science* 277(5328), 968–971, doi 10.1126/science.277.5328.968, whose abstract reads "Positron emission tomography revealed significant changes in pain-evoked activity within anterior cingulate cortex ... whereas primary somatosensory cortex activation was unaltered." The 2026-07-16 ledger had marked the 1999 cite "real-correct ... correctly the 1999 hypnotic-modulation paper, not the 1997 Science sibling" — a metadata-only certification that ratified the wrong-originator error (the (surname, YEAR) axis: two real Rainville papers, the result pinned to the wrong one). Fix: split the sentence so each paper carries its own finding, and added the 1997 entry to References. Corpus grep: no other live or archived page carries the 1999 misattribution (the research note `research/voids-suggestion-void-2026-08-06` already cites 1997 correctly).

### Medium Issues Found

**"Not a graded reduction ... no affective dimension at all" overstated relative to the primary series — FIXED.** Berthier et al.'s abstract records "absent *or inadequate* emotional responses to painful stimuli", so the all-or-nothing wording outran the source the paragraph rests on, and sat in mild tension with the Gerrans 2024 "not as clean" quote two paragraphs later. Re-scoped: *"The dissociation is not a graded reduction of the kind analgesia produces: asymbolia patients do not report mild discomfort where they should feel agony. Berthier et al. record emotional responses to painful stimuli that were "absent or inadequate", with no affective dimension at all in the clearest cases."* The quoted phrase is verbatim from the abstract (PMID 3415199).

### Citation web-verify ledger (§2.4)

Quote-fidelity lens (grep of raw source, not summariser):
- Feinstein et al. 2016 (Brain Struct Funct 221(3):1499–1511; PMC4734900) — **real-correct; quote verbatim.** "No studies have replicated the original finding of pain asymbolia following insula damage" grep-hit in the PMC full text; the surrounding paraphrase (parietal operculum / S2 / supramarginal gyrus extension; "unclear ... whether the insula damage was the primary cause") is faithful to the adjacent sentence. Result direction: title and body report *preserved* emotional awareness of pain — matches the article.
- Klein 2015 (Mind 124(494):493–516; doi 10.1093/mind/fzu185) — **real-correct; quote verbatim.** "Properly understood, asymbolics have lost a general capacity to care about their bodily integrity" grep-hit in the ANU research-portal abstract; Crossref confirms volume/issue/pages. The paraphrase "breakdown in the relation between pains and subjects rather than a fact about pain's intrinsic nature" tracks the abstract's next sentence; the depersonalisation tie is in the abstract's last sentence.
- Gerrans 2020 (Front Psychol 11:523710) — **real-correct; attribution verbatim.** Publisher full text: "pain asymbolia is a form of 'depersonalization for pain' as Klein puts it" and "aptly described by Klein (2015) as 'depersonalization for pain'" — so the article's "in a phrase he takes from Klein" is correct on the originator axis. Anterior-insula self-modelling gloss matches the abstract.
- Gerrans 2024 (Neurosci Conscious 2024(1):niae002; PMC10860504) — **real-correct; quote verbatim.** "dissociations at either the level of neurocircuitry or phenomenology are not as clean as predicted by a 'strictly' modular componential processing architecture for pain" grep-hit in the Europe PMC full-text XML.
- Berthier, Starkstein & Leiguarda 1988 (Ann Neurol 24(1):41–49; doi 10.1002/ana.410240109) — **real-correct.** Abstract confirms six patients, threatening gestures (6/6), verbal menaces (5/6), "rapidly resolving hemiparesis, cortical-type sensory loss, unilateral neglect, and body-schema disorders", insula damaged in all six. Result direction matches the article's comorbidity paragraph.
- Rainville et al. 1999 (Pain 82(2):159–171) — **real-correct metadata; result-direction defect (wrong work for the ACC claim) — fixed, see Critical.**
- Rainville et al. 1997 (Science 277(5328):968–971) — **added; verified at Crossref + Europe PMC abstract.**
- Grahek 2007 (MIT Press), Griffith & Kind 2024 (psa.2023.167), Duval & Klein 2025/2026 (psa.2025.10098), Rubins & Friedman 1948, Geschwind 1965 — unchanged since their last verification (2026-06-02, 2026-07-16, 2026-09-05); skip condition met.

Inline ↔ References cross-check: every inline cite has an entry and every entry is cited inline (12 entries after the addition). Superlative/currency sweep (`find_superlative_claims`): empty. Wikilink targets: all resolve.

### Reasoning-Mode Classification (editor-internal)
No new named-opponent replies since 2026-07-16. The Klein/Gerrans paragraph reports a third-party dissent about the subtraction picture and explicitly declines the self-model verdict ("records the reading without adopting the verdict"), routing the bridge question to [constitution-vs-causal-work](/concepts/constitution-vs-causal-work/) — that is Mode Three, honestly marked. Prior classifications stand (Functionalist Mode One/Two mixed; Epiphenomenalist Mode Three; Predictive-processing Mode Three). Label-leakage scan: none. "load-bearing": 0. "This is not X. It is Y.": 0.

### Possibility/probability slippage check
None. The new cross-modal paragraphs are calibration-tightening ("resolution rather than confirmation"; common-cause null applied), and the Bidirectional Interaction section keeps the "shared explanandum ... meeting it is not the same as being confirmed by it" discipline.

## Optimistic Analysis Summary

### Strengths Preserved
- The constrain-vs-establish passage in §"Causal Efficacy" (preserve-verbatim since 2026-06) is untouched.
- "What they cannot do is *care*"; "the hard problem in miniature"; the zombie-comparison caution; the Berthier broader-deficit honesty — all preserved.
- Hardline-Empiricist reading strengthened: the Feinstein localisation caveat and the Klein/Gerrans dissent are presented as live rather than absorbed, and the "resolution rather than confirmation" framing refuses to count the cross-modal survey as an independent converging line.

### Enhancements Made
- Hypnotic-analgesia paragraph now carries both Rainville results on their correct papers (imaging 1997; psychophysics 1999), which also makes the "graded approximation" caveat more informative.
- "Not graded" sentence now quotes the primary series instead of overstating it.

### Cross-links Added
None (link density already high; no new wikilinks).

## Remaining Items

Carried forward as enrichment, still deferred to avoid oscillation:
- Roger case (Feinstein et al. 2016 is now cited for the non-replication claim; its inverse-dissociation significance — preserved pain affect despite bilateral insula/ACC/amygdala loss — is only implicit at L52 and could be stated in one clause if a future pass has reason to touch that paragraph).
- Morphine/opioid analgesia pharmacological parallel — repeatedly deferred.
- CIPA — formally retired.

No follow-up tasks minted.

## Stability Notes

- **Eight deep reviews.** Legitimate re-qualification (new quotes and citations unverified by any prior review). Convergence-damping should continue to down-weight (~0.29× raw score). Consider inactive again unless body prose or the References block is substantively modified.
- **Bedrock disagreements** (do not re-flag as critical): epiphenomenalist objection; sophisticated-functionalist "not in pain" move; the constitution-vs-doing-work bridge with the predictive-processing rival; the Klein/Gerrans self-model reading (recorded, not adopted — Mode Three).
- **Resolved / verified citations** (do not re-open): all twelve References entries now carry a grep-verified quote or publisher-of-record metadata check. **Rainville split is canonical:** the ACC-not-S1 PET result is 1997 *Science*; the ratings-independence result is 1999 *Pain*. A future "both say the same thing, drop one" condense move would reintroduce the error — keep both, each on its own claim.
- Cambridge *Philosophy of Science* DOI trap (`S0031824…` content IDs are not DOIs) — unchanged from 2026-07-16.
- Terminology: "constitution-vs-doing-work" (prose) and "constitution-vs-causal-work" (slug) are intentionally interchangeable.