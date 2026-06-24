---
ai_contribution: 100
ai_generated_date: 2026-06-24
ai_modified: 2026-06-24 14:02:57+00:00
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
title: Deep Review - Indexical Identity and Quantum Measurement
topics: []
---

**Date**: 2026-06-24
**Article**: [Indexical Identity and Quantum Measurement](/topics/indexical-identity-quantum-measurement/)
**Previous review**: [2026-05-26](/reviews/deep-review-2026-05-26-indexical-identity-quantum-measurement/)

## Context

Ninth deep review (eleventh review file overall counting earlier short passes). The article was modified since the 2026-05-26 review: the Many-Minds Interpretation paragraph was extended/integrated and two Further Reading links (many-minds-interpretation, egocentric-presentism) were added on 2026-06-17 (commits bf1c45336, 8c29a0db6). Because the body was modified, the §2.4 publisher-of-record web-verify pass was re-run rather than skipped — and it caught two long-standing citation-metadata defects that survived all ten prior reviews because intra-corpus consistency had not been checked against the live publisher. Convergence discipline otherwise applied: bedrock disagreements not re-flagged, no oscillation of stable prose.

## Pessimistic Analysis Summary

### Critical Issues Found

Two citation-metadata defects (real-wrong-metadata; papers exist, metadata wrong — fixed in place, not deleted). Both were the article's *only* corpus outliers on these two references; sibling articles already carry the correct forms (family-resolution confirmed).

**Publisher-of-record citation ledger (§2.4):**

- Albert, D. — "Probability in the Everett Picture" — state: **real-wrong-metadata** (was "2015 / *The Wave Function: Essays on the Metaphysics of Quantum Mechanics*"; corrected to "2010 / *Many Worlds? Everett, Quantum Theory, and Reality*, Saunders, Barrett, Kent & Wallace eds., OUP, pp. 355–368"). Verified against PhilPapers ALBPIT and oxfordindex.oup.com (DOI 10.1093/acprof:oso/9780199560561.003.0013). The named book *The Wave Function* (2013, eds. Ney & Albert) contains a *different* Albert chapter ("Wave-function Realism"), not this one — so both year and venue were wrong. Corpus family-resolution: five other live articles (`probability-problem-in-many-worlds`, `quantum-completeness`, `concepts/many-worlds`, `probability-objections-many-worlds`, plus the research note) already cite the correct 2010 / *Many Worlds?* form; this article was the outlier.

- Friederich, S. & Dawid, R. (2022) — state: **real-wrong-metadata** (was title "Against probability in many-worlds quantum mechanics" / venue *Erkenntnis*; corrected to "Epistemic Separability and Everettian Branches: A Critique of Sebens and Carroll" / *British Journal for the Philosophy of Science*, 73(3), 711–721). Authors, year, and the article's in-text characterization (their critique that self-locating uncertainty "presupposes the Born rule rather than deriving it") are all faithful — only the title and venue were fabricated. Verified against PhilPapers DAWESA-3, academic.oup.com (DOI 10.1093/bjps/axaa002), journals.uchicago.edu (BJPS vol 73 no 3). The 2026-05-26 changelog ledger had recorded this paper as "BJPS 73(3) 711-721 (real-correct)" — but that verification was against the *concept* article (`indexical-knowledge-and-identity`), which already carries the correct form; the wrong title/venue in *this* topic article was never separately checked. Corpus family-resolution: `indexical-knowledge-and-identity`, `probability-problem-in-many-worlds`, and `qm-interpretations-beyond-many-worlds` already cite the correct BJPS title; this article was the sole outlier.

**Remaining attribution / calibration / reasoning-mode checks — all pass (re-verified):**

- **Attribution Accuracy Check** — pass. Fuchs quotes, Albert "irreducibly indexical" paraphrase, Von Neumann/Wigner/London-Bauer dating, Rovelli's explicit rejection of the consciousness-dependent reading, Wallace (2012) decision-theoretic framing all faithful. The Many-Minds paragraph (the new content) accurately summarizes the `many-minds-interpretation` article: single unbranching physical reality, continuum of minds distributed across outcomes, and the unanswered "which post-measurement mind is the actual continuant I" gap. No source/Map conflation; the "Consciousness as indexical ground" proposal is clearly labelled the Map's.
- **Possibility/probability slippage check (§2)** — pass. The "Empirical status" paragraph keeps the indexical-ground proposal honestly "metaphysical rather than empirically testable," noting all readings "predict identical experimental outcomes." A tenet-accepting reviewer would not flag any claim as overstated. No calibration error.
- **Reasoning-mode / named-opponent check (§2.6)** — pass. MWI / Albert / Friederich-Dawid / QBism engagements in natural journal-quality prose. No editor-vocabulary label leakage (grep-verified). The MWI engagement honestly marks the framework boundary while importing the in-framework circularity critique. No boundary-substitution.
- **Required sections** — front-loaded summary present; "Relation to Site Perspective" substantive across all five tenets; `description` present.
- **Internal anchors** — all body anchors (`#qbism`, `#collapse`, `#relational`, `#mwi`, `#interpretations`, `tenets#no-many-worlds`, `tenets#minimal-quantum-interaction`, `indexical-knowledge-and-identity#from-epistemic-to-metaphysical`) verified to resolve. The bare `[[tenets#no-many-worlds]]` form renders to `/tenets/#no-many-worlds`, which matches Hugo's auto-generated heading IDs — not broken.

### Medium Issues Found

None requiring action in this article. Out-of-scope corpus notes recorded for future tasks (see Remaining Items).

### Counterarguments Considered

All six pessimistic personas engaged; no new issues beyond the citation fixes.
- **Eliminative Materialist / Hard-Nosed Physicalist**: bedrock disagreement at tenet boundary (unchanged; not re-flagged).
- **Quantum Skeptic**: empirical-status section remains honest about the proposal being metaphysical, not testable.
- **Many-Worlds Defender**: fair treatment of self-locating uncertainty + decision-theoretic derivations; the new Many-Minds paragraph strengthens the case by showing that even *writing minds into the formalism* (MMI) leaves the indexical gap untouched — boundary disagreement honestly noted, not dressed as internal refutation.
- **Empiricist**: no regression.
- **Buddhist Philosopher**: anti-haecceitism / dissolution remains bedrock at tenet level (unchanged).

## Optimistic Analysis Summary

### Strengths Preserved

- Core indexical-gap concept and systematic interpretation survey (QBism, consciousness-collapse, relational QM, Many-Worlds).
- Epistemic/metaphysical thesis distinction — clearly drawn and load-bearing.
- "Consciousness as indexical ground" proposal — clearly demarcated from consciousness-collapse.
- New Many-Minds Interpretation paragraph: a genuinely sharpening addition — MMI is the strongest test of "can adding minds close the indexical gap?" and the article correctly diagnoses that it relocates rather than solves the problem, reinforcing the article's central thesis.
- Conservation-law argument; honest empirical-status acknowledgment (Hardline Empiricist counterweight satisfied).
- Effective italic *this*/*I* emphasis pattern throughout.

### Enhancements Made

None to prose (length-neutral; article stable). Edits limited to two citation-metadata corrections in the References block and frontmatter timestamps.

### Cross-links Added

None — cross-linking already comprehensive (the 2026-06-17 integration added the many-minds and egocentric-presentism links).

## Word Count

**Before**: 2847 words
**After**: 2847 words (citation-metadata corrections only; net word change negligible). 95% of soft threshold (3000) — within limits, length-neutral mode not triggered.

## Remaining Items

Out-of-scope corpus-hygiene findings surfaced during family-resolution, for separate tasks (NOT fixed here — they live in other files):

1. `concepts/quantum-probability-consciousness.md:213` cites Albert "Probability in the Everett Picture" in *After Physics* (Harvard UP, 2015) — *After Physics* is a real Albert book but does not contain this chapter; same defect class as the one fixed here. Should be corrected to the 2010 / *Many Worlds?* form.
2. `topics/probability-problem-in-many-worlds.md:175` and `topics/qm-interpretations-beyond-many-worlds.md:202` cite the Friederich & Dawid BJPS paper with end page **711–736**; publisher of record is **711–721**. Minor page-range drift to normalize corpus-wide.

These are candidates for a low-priority corpus citation-normalization sweep.

## Stability Notes

- This article is at stable prose equilibrium; the only substantive work this pass was citation-metadata correction caught by the §2.4 web-verify pass (re-triggered because the body was modified since the last review). This vindicates the rule that a body modification re-arms the web-verify pass even on a long-converged article — ten prior reviews ratified two wrong citations via intra-corpus consistency; only the live publisher caught them.
- **Bedrock disagreements** (eliminative materialism, heterophenomenology, anti-haecceitism, Buddhist dissolution) are tenet-level commitments at the framework boundary, not article flaws. Future reviews must NOT re-flag these.
- **No calibration error**: the empirical-status disclaimer keeps the indexical-ground proposal honestly metaphysical; no possibility/probability slippage.
- **Both fixed citations were the article's only corpus outliers** — sibling articles already carried the canonical forms, so no propagation *from* this article is needed; the two Remaining Items are independent pre-existing defects in other files.
- Future reviews should expect no prose work unless the article is substantively modified again. Continued re-review at the current cadence yields diminishing returns; candidate for a longer review interval — but a body modification should always re-arm the §2.4 web-verify pass.