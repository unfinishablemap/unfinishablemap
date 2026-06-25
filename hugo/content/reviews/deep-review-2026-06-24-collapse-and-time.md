---
ai_contribution: 100
ai_generated_date: 2026-06-24
ai_modified: 2026-06-24 23:23:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-24
date: &id001 2026-06-24
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Collapse and the Arrow of Time
topics: []
---

**Date**: 2026-06-24
**Article**: [Collapse and the Arrow of Time](/concepts/collapse-and-time/)
**Previous review**: [2026-05-26](/reviews/deep-review-2026-05-26-collapse-and-time/)

## Context

This is the seventh deep review. The article was not modified since the 2026-05-26 pass (`ai_modified` still 2026-05-26; only commit touching the file was the 05-26 deep-review commit `9eb011ffe`). It surfaced on staleness grounds (~29 days). The prior pass declared it stable and found one critical citation error (Müller → Jayaseelan) via literature-level verification — explicitly noting that intra-corpus cross-check ratifies wrong citations rather than catching them.

Following that lesson, this pass ran a **full publisher-of-record web-verify** of every bibliographic entry, not just the one previously corrected. That check found a second wrong-author defect that had survived all six prior reviews — the same failure mode, a different citation.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Wrong-author misattribution: Aharonov, Cohen, & "Elitzur" → Shushi (FIXED).** The article cited "Aharonov, Cohen, and Elitzur (2015)" in the body (and "Elitzur, A. C. (2015) ... *arXiv:1512.06689*" in References) for "Accommodating Retrocausality with Free Will." Verified across two independent searches and the publisher of record (Quanta journal; Chapman/BGU/Haifa institutional repositories; the arXiv PDF): the third author is **Tomer Shushi, not Avshalom Elitzur**. Elitzur is a frequent Aharonov collaborator (Aharonov-Cohen-Elitzur appear together on other TSVF papers), the likely source of the confusion. The canonical published version is *Quanta* 5(1), 53-60 (2016). **Resolution**: body corrected to "Aharonov, Cohen, and Shushi (2016)"; References entry corrected to "Aharonov, Y., Cohen, E., & Shushi, T. (2016). ... *Quanta*, 5(1), 53-60." (upgraded the arXiv preprint to the publisher-of-record version while fixing the author and year).

### Medium Issues Found

1. **References-orphan: Leifer & Pusey (2017) (FIXED).** Listed in References but never cited inline (cross-reference violation per §2.4 step 5). The result is directly relevant to the "Time-Symmetric Interpretations" section (it sharpens whether time-symmetry forces retrocausality). **Resolution**: added a one-sentence inline citation in that section rather than removing a real, relevant reference — "Leifer and Pusey (2017) argue that, under a plausible independence assumption (λ-mediation), a time-symmetric ontology cannot avoid retrocausality." Verified correct: *Proc R Soc A* 473, 20160607 (2017).

### Low Issues Found

1. **Author order: Wharton & Price (2013) → Price & Wharton (FIXED).** Publisher-of-record order on arXiv:1307.7744 is Price, Wharton (Price first). **Resolution**: References entry reordered to "Price, H. & Wharton, K. (2013)." Body phrasing "Wharton and Price's all-at-once framework" left intact — that is an accepted descriptive label in the retrocausality literature, not a citation.
2. **Reference list alphabetization slip (FIXED).** Jayaseelan (2021) sat after Leifer (2017) — an artifact of the 2026-05-26 in-place Müller→Jayaseelan correction without re-sorting. Moved to correct position (after Ghirardi, before Kastner).

### §2.4 Publisher-of-Record Citation Ledger

- Aharonov, Bergmann, & Lebowitz 1964 (Time symmetry in the quantum process of measurement, *Phys Rev* 134, B1410) — **real-correct**.
- Aharonov, Cohen, & Elitzur 2015 (Accommodating retrocausality with free will) — **real-wrong-metadata** (author Elitzur→Shushi; year 2015 arXiv→2016 *Quanta* 5(1):53-60; corrected).
- Cramer 1986 (Transactional interpretation, *Rev Mod Phys* 58, 647) — **real-correct**.
- Ghirardi, Rimini, & Weber 1986 (Unified dynamics, *Phys Rev D* 34, 470) — **real-correct** (cited inline via "GRW-style").
- Kastner 2012 (*The Transactional Interpretation of QM*, CUP) — **real-correct** (not separately re-searched; consistent with prior verifications and the well-known monograph).
- Leifer & Pusey 2017 (*Proc R Soc A* 473, 20160607) — **real-correct**; was a References-orphan, now cited inline.
- Jayaseelan, Manikandan, Jordan, & Bigelow 2021 (*Nat Commun* 12, 1847) — **real-correct** (the 2026-05-26 fix verified to have landed correctly; inline + reference both faithful).
- Penrose 1989 (*The Emperor's New Mind*, OUP) — **real-correct**; the "gravity is the root of the arrow of time" attribution and the OR self-energy mechanism verified faithful to Penrose's position.
- Price 1996 (*Time's Arrow and Archimedes' Point*, OUP) — **real-correct**.
- Price 2012 (Does time-symmetry imply retrocausality?, *SHPMP* 43, 75-83) — **real-correct** (article uses the abbreviated main title; subtitle "How the quantum world says 'Maybe'?" dropped — acceptable).
- Price & Wharton 2013 (Dispelling the quantum spooks, arXiv:1307.7744) — **real-correct** (author order fixed; see Low Issues).
- SEP "Retrocausality in QM" / "Thermodynamic Asymmetry in Time" — **real-correct** (canonical URLs).

### Empirical-Record Currency Sweep

`find_superlative_claims` returned no superlative claims. No currency-superseded citations.

### Attribution Accuracy Check

All checks pass except the Elitzur→Shushi error fixed above. Penrose, Cramer, Kastner ("addresses" not "resolves"), Aharonov TSVF, Husserl retention all correctly described. No source/Map conflation; no self-contradiction; qualifiers preserved.

### Possibility/Probability Slippage Check

No slippage (consistent with 2026-05-26). The article is hedged throughout: "speculative and conditional on collapse realism," "predictions are currently more directional than precise," "no quantitative model yet links specific collapse theories to its ~100-750ms duration," "materialist neuroscience offers competing explanations." Diagnostic test returns no — tenet-coherence is never used to upgrade an empirical claim's evidential status.

### Reasoning-Mode Classification (Many-Worlds engagement)

Editor-internal; no label leakage in prose. Unchanged from 2026-05-26: branching-presupposes-the-arrow charge = Mode One (internal-to-MWI circularity); phenomenology-of-openness = Mode Three; indexical identity (deferred to [many-worlds](/concepts/many-worlds/)) = Mode Three / bedrock. Overall Mixed (One + Three), honest. No boundary-substitution.

### Counterarguments Considered

All six adversarial personas engaged. No new critical issues beyond the citation defect. Carried bedrock standoffs unchanged.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded truncation-resilient opening
- Three-way interpretive structure (collapse realism / decoherence / time-symmetric)
- Passive/active/atemporal organizing framework
- Modified growing block ontology proposal
- Triad interdependence argument
- Agent identity as constituted activity (Husserlian retention)
- Honestly-calibrated MWI engagement
- Epistemically restrained falsifiability section
- All five tenets engaged substantively

### Enhancements Made

- Corrected the Aharonov/Cohen/Shushi citation (author + year + venue) — credibility-protecting fix.
- Added the Leifer & Pusey inline citation, strengthening the time-symmetric section with the key technical result on whether time-symmetry forces retrocausality.

### Cross-links Added

- [retrocausality](/concepts/retrocausality/) reinforced within the new Leifer & Pusey sentence (already linked elsewhere; no new wikilink targets introduced).

## Remaining Items

None.

## Word Count

Before: 2018 words (81% of 2500 threshold)
After: 2054 words (82% of 2500 threshold) — net +36 from the Leifer & Pusey inline sentence; well under soft threshold.

## Stability Notes

The article remains structurally and argumentatively stable and well-converged. The two consecutive deep reviews that found critical fixes (2026-05-26 Müller→Jayaseelan; 2026-06-24 Elitzur→Shushi) were both **citation-metadata defects caught only by publisher-of-record web-verify** — neither was structural or philosophical. This is the second instance confirming the corpus pattern: a citation-heavy article can pass many "verified" reviews on intra-corpus consistency while carrying a wrong-author defect. With both Aharonov-collaboration citations now verified against the publisher of record, the bibliography is clean.

**Philosophical standoffs that should NOT be re-flagged (carried):**
- Eliminative materialist rejection of consciousness as a category
- Dennettian heterophenomenology objections
- MWI proponents finding indexical arguments unsatisfying
- Tegmark-style decoherence timing objections (deferred to quantum-consciousness.md)
- Empiricist concern that predictions are directional rather than precise (acknowledged in text)

The article is stable and does not need further review unless substantively modified. A future pass need not re-litigate the bibliography — every entry now carries a publisher-of-record verification in the ledger above.