---
title: "Deep Review - Neurophenomenology and Contemplative Neuroscience"
created: 2026-07-13
modified: 2026-07-13
human_modified: null
ai_modified: 2026-07-13T03:19:17+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-6
ai_generated_date: 2026-07-13
last_curated: null
---

**Date**: 2026-07-13
**Article**: [[neurophenomenology-and-contemplative-neuroscience|Neurophenomenology and Contemplative Neuroscience]]
**Previous review**: [[deep-review-2026-06-18-neurophenomenology-and-contemplative-neuroscience|2026-06-18]]

## Context

Ninth deep review (staleness-selected, ~25-day gap). This was a targeted citation-metadata / attribution-accuracy / quote-fidelity / empirical-currency pass, NOT a rewrite. The article is argument-converged (prior passes 05-11, 06-04, 06-18 all declared convergence on prose and adversarial engagements). The 06-04 pass ran a publisher-of-record web-verify of the *empirical-thesis* citation cluster (Varela, Kral, Lutz, Demir, Fox, Laukkonen, Pernet, Weng) and 06-18 verified the new Sandved-Smith body cite. This pass re-ran live publisher web-verification on the **DMN / functional-connectivity citation cluster that prior archives had not explicitly logged** (Bremer/"Parkinson", Garrison, Brewer, Lazar) — and it surfaced one real wrong-author defect that survived all eight prior reviews (intra-corpus cross-check ratifies rather than catches author-conflation; only live publisher verify catches it).

## Pessimistic Analysis Summary

### Critical Issues Found (one wrong-author, fixed)

1. **Wrong-author citation (real-paper / wrong-author, 3-state).** The article cited **"Parkinson, T.D. et al. (2022). Mindfulness meditation increases default mode, salience, and central executive network connectivity. *Scientific Reports*, 12, 13219"** for the functional-connectivity claim (DMN ↔ salience ↔ central-executive). The exact title, venue, volume and article number (Sci Rep 2022, 12:13219, DOI 10.1038/s41598-022-17325-6) are correct, but the paper's first author is **Benno Bremer**, not Parkinson. Full author list verified at Nature and PMC (PMC9346127): Bremer, Wu, Mora Álvarez, Hölzel, Wilhelm, Hell, Tavacioglu, Torske, Koch. "Parkinson TD" appears only as **reference 38 *inside* the Bremer paper** — i.e. this is an author-conflation (the citing article grabbed a cited author from the paper's own bibliography), directly analogous to the Pernet/Sezer conflation caught on 2026-06-04. It is NOT a fabrication: the paper and all its figures are real and faithful. **Resolution**: reference-list entry and footnote re-attributed to **Bremer, B. et al. (2022)**; footnote key renamed `[^parkinson]` → `[^bremer2022]` (chose `bremer2022` over `bremer` to avoid visual collision with the existing `[^brewer]` key on the same line). Body claim, venue, DOI, and figures unchanged.

### Citations Web-Verified at Publisher of Record (3-state)

DMN / functional-connectivity cluster (this pass's focus — not previously logged in review archives):

- **Bremer, B. et al. (2022)** [was misattributed "Parkinson, T.D."] — *Scientific Reports* 12:13219 — **real-wrong-metadata (first author Parkinson→Bremer, corrected)**. Verified Nature + PMC9346127.
- **Garrison, K.A. et al. (2015)** "Meditation leads to reduced default mode network activity beyond an active task", *Cognitive, Affective, & Behavioral Neuroscience* 15(3):712-720 — **real-correct**. Verified Springer (s13415-015-0358-3) + PubMed 25904238.
- **Brewer, J.A. et al. (2011)** "Meditation experience is associated with differences in default mode network activity and connectivity", *PNAS* 108(50):20254-20259 — **real-correct**. Verified PNAS (10.1073/pnas.1112029108) + PubMed 22114193. (Full author list Brewer, Worhunsky, Gray, Tang, Weber, Kober.)
- **Lazar, S.W. et al. (2005)** "Meditation experience is associated with increased cortical thickness", *NeuroReport* 16(17):1893-1897 — **real-correct**. Verified journals.lww.com (DOI 10.1097/01.wnr.0000186598.66243.19). Correctly used as the "under scrutiny" earlier structural claim, honestly caveated against Kral 2022.

Re-confirmed converged-clean from prior passes (not re-litigated): Varela 1996 (coinage + subtitle), Kral 2022, Lutz 2004, Demir 2025, Fox 2012, Laukkonen 2023, Pernet 2021, Weng 2013, Sandved-Smith 2025.

### Attribution / Coinage (Task Locus 1)

- **Varela COINED "neurophenomenology" as "a methodological remedy for the hard problem"** — **CONFIRMED**. Varela, F.J. (1996), *Journal of Consciousness Studies* 3(4):330-349. Verified at Ingenta/PhilPapers/Avant: the paper introduces neurophenomenology as a research program responding to Chalmers' hard problem. The verbatim subtitle quote ("a methodological remedy for the hard problem") matches the paper title exactly (already verbatim-confirmed 06-04). The article's attribution of coinage to Varela is faithful.

### Empirical-Currency Sweep (Task Locus 2)

`find_superlative_claims` returned **no** superlative claims — the article carries no "first / largest / current record / to date" empirical claims to re-verify against the live literature. This is itself a calibration strength: the article's structural-claim exposure (the replication-crisis-prone cortical-thickening finding) is already explicitly downgraded in the opening paragraph and the "Structural changes (under scrutiny)" block via the well-powered **Kral et al. (2022)** null (218 participants, active controls). The neuroplasticity thesis is framed as *functional* changes providing "suggestive evidence" for bidirectional interaction, never as demonstration. No categorical/"demonstrates" over-claim to soften. Calibration preserved.

### Quote-Fidelity (Task Locus 3)

Only one attributed direct quote in the body: Varela's **"a methodological remedy for the hard problem"** — verbatim-correct against the 1996 paper title, in the specific cited work (no wrong-work error, no connective-word capture, no blurb-as-author-quote). All other quotation marks are terms-of-art scare quotes (*khanika*, "actual occasions", "how" vs "why", "present-centred", "seeming"). No misquote.

### Inline ↔ References / Footnote Integrity
- All 15 inline footnote refs reciprocate their definitions (verified programmatically post-fix; `[^muller]` is used inline on line 77 — the only "orphan" flagged was a regex-lookbehind artifact from adjacent `[^brewer][^muller]`, not a real orphan).
- Every References-list entry is cited inline or in a footnote; no orphans in either direction.
- No bare-slug markdown links; all wikilinks resolve (including the two dated research-note links, which are legitimate note targets, not memory-slug leaks). EOF clean.

### Reasoning-Mode Classification (changelog/editor-internal only)
No change from 06-04/06-18 — re-confirmed, not re-litigated. Dennett/Frankish illusionism = Mixed (Mode One regress + Mode Two empirical differential-prediction); Nisbett & Wilson = Mode One (process/content distinction); materialist on causal pathway = Mode Three (honest boundary marking). No label leakage; no editor-vocabulary in prose; no "This is not X. It is Y." cliché.

### Calibration Check (Possibility/Probability Slippage)
Applied the diagnostic test (would a tenet-accepting reviewer still flag any claim as overstated?). No instances. Functional findings remain "suggestive evidence"; structural claims downgraded post-Kral; compassion-content claim hedged with the standard differential-training alternative; Stapp Zeno "remains empirically open"; cessation "may represent complete filtering." No tenet-as-evidence-upgrade slippage.

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded summary with the Kral-2022 structural-null calibration in the opening paragraph.
- Eight-criterion "What Would Challenge This View?" falsification section.
- All five tenets substantively connected.
- Heterophenomenology empirical-refutation engagement; Buddhist anti-substantialism tension honestly acknowledged.
- The functional/structural distinction is handled with genuine restraint — a model for evidence-calibrated dualist content in a replication-crisis-exposed domain.

### Enhancements Made
- Corrected one citation-level wrong-author defect (Parkinson→Bremer) — net credibility gain. No prose growth.

### Cross-links Added
None (already densely cross-linked).

## Word Count
- 3031 words (121% of 2500 soft; under 3500 hard) — **soft_warning**, length-neutral mode.
- Author-name swap is word-neutral (3031 → 3031). No offsetting cuts required. Persistent soft_warning remains a human length-decision item, not a deep-review auto-condense target.

## Remaining Items
- Replace Davidson-2008 news citation with the peer-reviewed paper (long-standing, optional/future).
- Length: persistent soft_warning; condensation remains a human length-decision item.

## Stability Notes

The article remains converged on argument structure, adversarial engagements, and calibration. Do NOT re-flag: the heterophenomenology response, the MWI indexical argument, the Buddhist anti-substantialism tension, the Stapp Zeno hedging, or the Kral-2022 structural-null calibration — all bedrock or converged. This pass demonstrates (again, per the 06-04 lesson) that "argument-converged" ≠ "citation-clean": the Parkinson→Bremer author-conflation survived eight prior reviews because it lives in the DMN-connectivity cluster that only 06-04's partial web-verify touched, and intra-corpus cross-check propagates author-conflation rather than catching it. With the DMN cluster now publisher-verified alongside the empirical-thesis cluster, the citation set is comprehensively web-verified; the residual Davidson-2008 news-citation is the only known metadata item, and it is content-supported and optional. Future selection should be a metadata-only confirm unless the body changes.
