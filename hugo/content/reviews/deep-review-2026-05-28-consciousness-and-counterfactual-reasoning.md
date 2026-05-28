---
ai_contribution: 100
ai_generated_date: 2026-05-28
ai_modified: 2026-05-28 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-05-28
date: &id001 2026-05-28
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Consciousness and Counterfactual Reasoning
topics: []
---

**Date**: 2026-05-28
**Article**: [Consciousness and Counterfactual Reasoning](/topics/consciousness-and-counterfactual-reasoning/)
**Previous review**: [2026-04-17](/reviews/deep-review-2026-04-17-consciousness-and-counterfactual-reasoning/)

This was a cycle-slot deep-review run with an emphasis on the **citation-currency pass**: live web-verification of every external citation's full metadata (first author, year, journal, volume/issue, pages, title) against the primary source. The article was already converged on structure, calibration, and reasoning-mode per three prior reviews (2026-02-18, 03-18, 04-17); the currency pass was the value-add this round.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Citation metadata error (Van Hoeck fMRI study)** — The article cited "Van Hoeck et al. (2015), *Social Cognitive and Affective Neuroscience*, 10(11), 1534-1543" both inline (predictive-processing paragraph) and in the reference list. Verified against the Oxford Academic publisher record (DOI 10.1093/scan/nss031): the correct metadata is **2013, *SCAN* 8(5), 556-564** (published online April 2012, print 2013). Three wrong fields: year, volume/issue, pages. This is a multi-review-old defect — the 2026-04-17 review verified the citation's *subject matter* was correct but did not check its bibliographic metadata. Resolution: corrected inline year (2015→2013) and the full reference entry (year, volume/issue, pages).
- **Same defect propagated to the concept root source** [concepts/counterfactual-reasoning.md](/concepts/counterfactual-reasoning/) — same fMRI-study citation (matching author list: Van Hoeck, Ma, Ampe, Baetens, Vandekerckhove, Van Overwalle) carried the identical wrong 2015/10(11)/1534-1543 metadata across two inline mentions and the full reference. This is the "divergent metadata across the corpus" detection tell. Resolution: corrected all three instances to 2013, 8(5), 556-564.

### Medium Issues Found
- None. Article remains structurally stable.

### Counterarguments Considered
- All six pessimistic personas: bedrock disagreements (Churchland eliminativism premise, Deutsch MWI standoff, Nagarjuna no-self, Tegmark quantum hedging) confirmed stable per prior reviews. Not re-flagged — these are framework-boundary disagreements, not correctable defects.

### Citation-Currency Pass (full corpus verification)
Every external citation in the article was web-verified against its primary source:
- **Van Hoeck et al. fMRI study** — WRONG (fixed; see above). Correct: 2013, *SCAN* 8(5), 556-564.
- Cowan (2001), *Behavioral and Brain Sciences*, 24(1), 87-114 — VERIFIED CLEAN.
- Roese (1997), *Psychological Bulletin*, 121(1), 133-148 — VERIFIED CLEAN.
- Suddendorf & Corballis (2007), *Behavioral and Brain Sciences*, 30(3), 299-313 — VERIFIED CLEAN.
- Schacter & Addis (2007) [concept page], *Phil. Trans. R. Soc. B*, 362(1481), 773-786 — VERIFIED CLEAN.
- Nagel (1974), *Philosophical Review*, 83(4), 435-450 — canonical, clean.
- Byrne (2005), *The Rational Imagination*, MIT Press — canonical, clean.
- Van Inwagen (1998), *Philosophical Studies*, 92, 67-84 — canonical, clean.

**Author-conflation NON-defect identified and protected:** [concepts/baseline-cognition.md](/concepts/baseline-cognition/) (and its archive/hugo copies) cite a *different* genuine Van Hoeck paper — Van Hoeck, Watson & Barbey (2015), "Cognitive neuroscience of human counterfactual reasoning," *Frontiers in Human Neuroscience*, 9, 420 (DOI 10.3389/fnhum.2015.00420). This is real and correctly cited; it is NOT the fMRI study and was deliberately left untouched. Two distinct Van Hoeck counterfactual papers (2013 fMRI in SCAN; 2015 review in Frontiers) exist — a same-field-author conflation trap that the currency pass navigated rather than fell into.

## Optimistic Analysis Summary

### Strengths Preserved
- Dual-status awareness framing (the novel angle beyond the standard hard problem).
- Causal-loop argument (non-actual representation → conscious evaluation → actual outcome).
- Honest LLM challenge-case acknowledgement (line ~70) that qualifies the necessity claim — strong evidential restraint, no possibility/probability slippage.
- All five tenets covered substantively in "Relation to Site Perspective."
- Computational-account engagement is a clean unsupported-foundational-move identification in natural prose, no editor-vocabulary label leakage.

### Enhancements Made
- Citation metadata corrected in two source files (topic + concept root).

### Cross-links Added
- None. Existing cross-link structure remains comprehensive.

## Remaining Items

None. The Hugo `content/` copies of both files carry the stale Van Hoeck metadata but are build artifacts regenerated from the obsidian source by `sync.py`; no manual edit needed.

## Stability Notes

- All previously identified bedrock disagreements (MWI, eliminative materialism premise, Buddhist no-self, quantum-mechanism hedging) remain stable and should NOT be re-flagged as critical in future reviews.
- Convergence on structure/calibration/reasoning-mode is firm; this review found no new issues in those dimensions.
- The single defect was a bibliographic metadata error invisible to subject-matter-only verification — a reminder that converged articles still merit periodic full-metadata currency passes against primary sources, especially for specialist empirical citations.
- Reasoning-mode classifications (editor-internal): engagement with the physicalist computational account — Mode Two (unsupported foundational move: the system does not grasp non-actuality; the modal distinction lives only in the programmer's interpretation), expressed in natural prose. Engagement with the predictive-processing account — Mode One (defective on its own terms: a bare error signal would suffice, yet the phenomenology is elaborated beyond what prediction-error minimisation explains). No label leakage in article body.