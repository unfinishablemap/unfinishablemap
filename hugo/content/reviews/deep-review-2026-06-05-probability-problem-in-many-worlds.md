---
ai_contribution: 100
ai_generated_date: 2026-06-05
ai_modified: 2026-06-05 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-05
date: &id001 2026-06-05
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Probability Problem in Many Worlds
topics: []
---

**Date**: 2026-06-05
**Article**: [The Probability Problem in Many Worlds](/topics/probability-problem-in-many-worlds/)
**Previous review**: [2026-05-26](/reviews/deep-review-2026-05-26-probability-problem-in-many-worlds/) (ninth review)

## Review Context

Tasked as a citation-heavy Tenet-4 audit: web-verify EVERY citation's first-author / co-authors / venue / year / volume / pages / stance against the publisher of record — not just load-bearing cites. The article was lightly modified since the 2026-05-26 review (3766 → 3784 words pre-edit). Length-neutral expectations apply (topics hard cap 4000); post-edit length 3831 words, still under the hard cap.

Every one of the 21 → 23 reference entries was independently web-verified this pass ("converged ≠ verified"). The article is otherwise well-converged across nine reviews; calibration, reasoning-mode, source/Map separation, and self-contradiction were re-confirmed clean (matching the 2026-05-26 findings) and are not re-litigated below.

## Pessimistic Analysis Summary

### Critical Issues Found (Citation Audit) — 4 fixed

1. **Wallace (2003) page range — DOCUMENTED REGRESSION, FIXED.** Reference #16 read `415-439`. The publisher of record (DOI 10.1016/S1355-2198(03)00036-4 / SHPMP 34(3)), PhilPapers (WALERD-2), ADS (2003SHPMP..34..415W), and SciRP all give **415-438**. The wrong "439" end page is exactly the propagated error flagged in the task watch-note. Corrected to 415-438.

2. **Zhang (2026) scope overstatement — FIXED.** Body line 133 claimed Zhang covers "Gleason's theorem, Deutsch-Wallace decision theory, Zurek's envariance, and the epistemic and frequentist routes." The actual paper (arXiv:2603.06211, abstract verified) analyzes five named derivations: Gleason's Theorem, Busch's extension of it, Deutsch-Wallace, Zurek's envariance, and the Finkelstein-Hartle Theorem. It does NOT cover an "epistemic" (self-locating / Sebens-Carroll) derivation. Rewritten to match the paper's stated scope: "Gleason's theorem and Busch's extension of it, Deutsch-Wallace decision theory, Zurek's envariance, and the Finkelstein-Hartle frequency-operator route." Hedge ("a preprint not yet independently verified") preserved.

3. **Everett (1957) — DANGLING INLINE CITE, FIXED.** Cited inline twice (lines 57, 133) with no References entry. Added entry: Everett, H. (1957). "Relative state" formulation of quantum mechanics. *Reviews of Modern Physics*, 29(3), 454-462. (Verified against ADS 1957RvMP...29..454E — real, foundational MWI paper; de-citing would be wrong, so added rather than removed.)

4. **Wallace (2007) — DANGLING INLINE CITE, FIXED.** Cited inline at line 63 ("Wallace (2003, 2007, 2010)") with no 2007 References entry (2003, 2010, 2012 entries existed). Verified real: "Quantum probability from subjective likelihood: improving on Deutsch's proof of the probability rule," SHPMP 38(2), 311-332. Added as reference #18.

### Citations Verified Correct (no change)

All verified against publisher of record this pass — author(s), venue, year, volume, pages, and stance:

- **Deutsch (1999)** — Proc. R. Soc. A 455, 3129-3137. ✓
- **Sebens & Carroll (2018)** — BJPS 69(1), 25-74. ✓ (author order varies preprint↔journal; "Sebens and Carroll" matches the conventional/PhilPapers citation)
- **Saunders (2021)** — Proc. R. Soc. A 477(2255), 20210600. ✓ (state-dependent decoherent-histories branch-counting rule, accurately characterized)
- **Friederich & Dawid (2022)** — BJPS 73(3), 711-736. ✓ (Friederich-first per journal record; ESP-QM circularity stance faithful)
- **Vaidman (1998)** — Int. Studies Phil. Sci. 12(3), 245-261. ✓
- **Zurek (2005)** — Phys. Rev. A 71, 052105. ✓
- **Zurek (2003)** — Rev. Mod. Phys. 75(3), 715-775. ✓
- **Short (2023)** — Quantum 7, 971 (Anthony J. Short). ✓
- **Barnum, Caves, Finkelstein, Fuchs & Schack (2000)** — Proc. R. Soc. A 456, 1175-1182. ✓ (all five authors correct)
- **Mohrhoff (2004)** — Int. J. Quantum Inf. 2(2), 221-229. ✓
- **Lewis (2007)** — SHPMP 38, 1-14. ✓ ("spurious / in the wrong place" stance verbatim)
- **Baker (2007)** — SHPMP 38, 153-169. ✓
- **Kent (2010)** — *Many Worlds?* (OUP). ✓ (title verbatim; axioms-not-constitutive stance accurate)
- **Graham (1973)** — DeWitt & Graham (eds.), *The Many-Worlds Interpretation of QM*, Princeton UP. ✓
- **Albert (2010), Price (2010), Saunders (2010), Wallace (2010)** — chapters in the *Many Worlds?* OUP 2010 edited volume; consistent with the catalog and standard scholarship.
- **Wallace (2012)** *The Emergent Multiverse* (OUP) — ✓.

3-state de-citation discipline applied: no fabricated/chimera citation found. The two dangling inline cites resolved to REAL papers (state: real-correct), so the fix was to add the missing References entries, not to remove content.

### Inline ↔ References Cross-Check (both directions)
- Forward (inline → References): all inline author-year mentions now have entries (Everett 1957 and Wallace 2007 gaps closed).
- Reverse (References → inline): every reference entry is cited in the body. No orphan references.

### Attribution / Source-Map / Self-Contradiction / Reasoning-Mode / Calibration
Re-confirmed clean (unchanged from 2026-05-26). The Map's framework-boundary marking on Deutsch-Wallace branching indifference and on the Saunders/Sebens-Carroll indexical reply remains honest and explicit; no boundary-substitution; no label leakage; no possibility/probability slippage; parsimony explicitly disarmed in both directions (Tenet 5). A tenet-accepting reviewer would not flag any claim as overstated.

## Optimistic Analysis Summary

### Strengths Preserved
- Two-problems framing (incoherence vs. quantitative).
- Baker-Price circularity chain (Born rule → decoherence → branches → probability → Born rule).
- Albert's betting-vs-frequency distinction, well-isolated.
- "What Would Success Even Look Like?" counterfactual section.
- "Where the Map's Disagreement Actually Falls" — model framework-boundary marking.

### Enhancements Made
- None beyond the citation corrections. Article is converged; length-neutral mode.

### Cross-links Added
- None needed.

## Word Count
- Before: 3784 words
- After: 3831 words (+47; two reference lines added to close dangling inline cites; under 4000 hard cap)

## Remaining Items
None.

## Stability Notes
- The Zhang (2026) characterization is now anchored to the paper's actual five-derivation scope. If the preprint fails replication, the proliferation argument stands on the older sources (Kent, Albert, Baker, Price) regardless — hedge preserved.
- The Wallace (2003) `415-438` page range is the publisher-of-record consensus; do NOT let `415-439` propagate back in. This is the documented sibling-corpus regression.
- MWI defenders (Deutsch, Wallace, Saunders, Sebens-Carroll) will always find the tenet-driven indexical reservation unsatisfying — bedrock framework-boundary disagreement, explicitly marked in the article. NOT a flaw to fix.
- Article sits at 128% of soft target, below hard cap. Future reviews: length-neutral; do NOT expand.
- All prior eight reviews' stability notes carry forward.