---
ai_contribution: 100
ai_generated_date: 2026-05-29
ai_modified: 2026-05-29 12:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-05-29
date: &id001 2026-05-29
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Mapping Mind-Space
topics: []
---

**Date**: 2026-05-29
**Article**: [Mapping Mind-Space](/voids/mapping-mind-space/)
**Previous review**: [2026-04-17](/reviews/deep-review-2026-04-17-mapping-mind-space/)

This was a queued staleness deep-review (42 days). Per the standing steer, the pass ran the CITATION-CURRENCY + CALIBRATION protocol on a converged article. The 2026-04-17 review found no critical issues and declared convergence; this pass confirms that for the *arguments* but caught one propagated citation misattribution that prior reviews and the cross-corpus check had not surfaced.

## Pessimistic Analysis Summary

### Critical Issues Found

**Citation misattribution (author vector) — FIXED.** Reference 7 (and the in-body attribution in "Convergent Arguments for Missing Dimensions") attributed "On the Origins and Evolution of Qualia: An Experience-Space Perspective" (*Frontiers in Systems Neuroscience*, 16, 945722, 2022) to **Barron, A.B. & Klein, C.** Web-verification against the Frontiers page (DOI 10.3389/fnsys.2022.945722, PMC9399462) and PubMed confirms the paper is by **Thurston Lacalli** (sole author, University of Victoria). The title, journal, volume, article number, year, and the quoted E-space claim ("at least several times as many dimensions as there are categories of qualia") are all correct — only the author was wrong. Barron & Klein have a *different*, real qualia paper (PNAS 2016, "What insects can tell us about the origins of consciousness"), which is the likely source of the conflation.

This is the citation-metadata-unreliability pattern from project memory: the defect had **propagated** across the corpus in three divergent wrong forms:
- "Barron, A.B. & Klein, C." — [voids/mapping-mind-space.md](/voids/mapping-mind-space/) (body + ref), `archive/voids/dimensionality-void.md` (ref), [research/voids-dimensionality-void-2026-03-23.md](/research/voids-dimensionality-void-2026-03-23/) (heading + ref)
- "Barton, Robert A." — [research/voids-qualitative-novelty-void-2026-02-16.md](/research/voids-qualitative-novelty-void-2026-02-16/) (ref) — a third, doubly-wrong form
- title-only (no author) — [research/voids-synesthetic-void-2026-02-23.md](/research/voids-synesthetic-void-2026-02-23/) — clean, left as-is

Fixed the propagation roots (both `research/` notes) FIRST, then the article body + reference, then the archive copy. All now read "Lacalli, Thurston / Lacalli, T." The hugo/content/ copies are build artifacts that regenerate on sync; not hand-edited.

### Other Citations Verified (no defect)

- **Arsiwalla & Verschure (2023)**, *NeuroSci*, 4(2), 9 — CORRECT (confirmed MDPI + PubMed 39483317, published 2023-03-27). NOTE: a divergent form ("*Minds and Machines*, 2024") survives in [research/voids-mind-space-void-2026-02-23.md](/research/voids-mind-space-void-2026-02-23/); the *article* carries the correct form (a 2026-W11 changelog records that fix). The research-note divergence is the suspect, not the article — left unchanged as it does not feed the article's current text, but flagged here.
- **Jolly & Chang (2019)**, *Topics in Cognitive Science*, 11(2), 433–454 — CORRECT (Wiley DOI 10.1111/tops.12404). Source-conclusion: the article's "preference for low-dimensional models driven by tractability rather than evidence" accurately represents the Flatland-fallacy thesis.
- **Schwitzgebel (2024)**, *The Weirdness of the World*, Princeton UP — CORRECT. Quote "the truth — whatever it is — is weird" is verbatim from the book's central claim.
- Canonical citations (Nagel 1974 bat + quote, McGinn 1989, Abbott 1884, Shanahan 2010, Sjöstedt-Hughes 2021, Carr 2015, James 1902, Lewis 1979, Bostrom 2002, Perry 1979) — verified in predecessor reviews; cross-corpus grep surfaced no divergence. Not re-verified line-by-line.

### Medium Issues Found
None.

### Counterarguments Considered
No change from 2026-04-17. Bedrock disagreements (eliminativist, functionalist/morphospace, MWI branch-relative, Buddhist no-self) remain as recorded; not re-flagged. No named-opponent refutation engagements, so no reasoning-mode classification applies. No editor-vocabulary label leakage found.

## Optimistic Analysis Summary

### Strengths Preserved
All strengths from the prior review preserved unchanged: front-loaded opening (both facets), Copernican analogy, recursive Flatland framing, four distinct convergent arguments, five edge-phenomenology observations, five substantive tenet connections, the "dimensional ignorance" original contribution, and the MWI branch-relative-indexicality engagement (which is more precise than the predecessor's "every position simultaneously occupied").

### Enhancements Made
None. Citation correction only.

### Cross-links Added
None.

## Calibration Pass

This is a VOID article (primarily unexplorable). The void claim ("the geometry of mind-space is inaccessible from within") is calibrated as a structural/phenomenological observation, not as established empirical fact. No possibility/probability slippage detected:
- The strongest assertion, "morphospace is almost certainly incomplete under dualism," is explicitly *conditional on the dualism tenet* ("if consciousness is not reducible to functional properties, the relevant dimensions may be entirely non-physical") — a logical consequence correctly scoped, not a tenet-coherence-to-evidence upgrade.
- Speculative frameworks (Barron→Lacalli E-space, Arsiwalla morphospace, Carr 5D) all use "propose"/"may." The diagnostic test (would a tenet-accepting reviewer flag overstatement?) returns no for every load-bearing claim. Honours [evidential-status-discipline](/project/evidential-status-discipline/).

## Length

2111 words (106% of 2000 voids/ soft target, soft_warning). Operated length-neutral; the only body change was an author-name swap (+1 word). No expansion.

## Remaining Items

- Research-note metadata hygiene (non-blocking): [research/voids-mind-space-void-2026-02-23.md](/research/voids-mind-space-void-2026-02-23/) still carries the divergent "Arsiwalla & Verschure, *Minds and Machines*, 2024" form. The article is correct; the stale note could be corrected in a future research-hygiene sweep but does not feed live content.

## Stability Notes

The article's *arguments* remain converged (confirmed third review running). The one defect this pass caught was a propagated citation author-misattribution invisible to argument-level review and to intra-corpus cross-checking (the wrong form was the *majority* form across the corpus) — only live web-verification of the author vector caught it, consistent with the project-memory note that AI-authored citation metadata carries a real misattribution rate. Future reviews should NOT re-flag the bedrock disagreements (eliminativist / functionalist / MWI / Buddhist). The Lacalli attribution is now correct corpus-wide in the live tree (obsidian + archive).