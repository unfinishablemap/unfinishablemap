---
ai_contribution: 100
ai_generated_date: 2026-08-26
ai_modified: 2026-08-26 23:58:00+00:00
ai_system: claude-fable-5
author: null
concepts:
- '[[causal-consistency-constraint]]'
created: 2026-08-26
date: &id001 2026-08-26
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-26 23:58:00+00:00
modified: *id001
related_articles:
- '[[generalised-probabilistic-theories]]'
- '[[post-decoherence-selection]]'
- '[[sorkin-higher-order-interference]]'
title: Deep Review - Causal Consistency Constraint
topics: []
---

**Date**: 2026-08-26
**Article**: [Causal Consistency Constraint](/concepts/causal-consistency-constraint/)
**Previous review**: [2026-07-14](/reviews/deep-review-2026-07-14-causal-consistency-constraint/) (converged no-op); earlier [2026-06-03](/reviews/deep-review-2026-06-03-causal-consistency-constraint/) (full per-cite web-verify), [2026-05-15](/reviews/deep-review-2026-05-15-causal-consistency-constraint/), [2026-05-14](/reviews/deep-review-2026-05-14-causal-consistency-constraint/).
**Verdict**: Substantive-change pass, not a converged no-op. Four commits touched the file after the 07-14 review (07-16 GPT cross-link; 08-02 reconstruction-list References fix; 08-02 improper-mixture paragraph; 08-17 purification-uniqueness clause). One source-fidelity defect fixed, one References title restored, two cross-links added. Word count 2416 → 2455 (concepts soft 2500; `ok`).

## What changed since 07-14 (the review's scope)

- **Purification definition** now carries the uniqueness clause ("unique up to reversible channels on the purifying system"). Verified against the paper body at arXiv 2512.12636v3: "purifications are essentially unique: any two purifications are related by a reversible transformation on the purifying system", citing Chiribella, D'Ariano and Perinotti 2010. **Faithful.**
- **Improper-mixture / category-error paragraph** in the corridor subsection. Checked against [post-decoherence-selection](/concepts/post-decoherence-selection/) L52, which states the category-error reading in nearly the same words. **Consistent; no drift between the two.**
- **Reconstruction list** now reads "Wallace (2003, 2012), Zurek (2005, envariance)" with matching References entries 5–8, and Arana (2025) has a References entry. Cross-reference inline ↔ References is now closed in both directions (see ledger).

## Pessimistic Analysis Summary

### Critical Issues Found

- **Source misdescription of the theorem's relation (fixed).** The article said the identity holds "between the geometric inner product of two states and their predictive probability". The paper's relation is between the *geometric transition probability* τ(ψ,φ) := sup{e(ψ): e(φ)=1} and P(φ|ψ); in quantum theory τ = |⟨φ|ψ⟩|², the *squared* inner product (paper, Remark 1). "Inner product" with an identity relation would read as P = ⟨φ|ψ⟩, which is wrong. Rewritten to name the transition probability, gloss it, and identify it with the squared inner product. Same sentence: the paper reaches the Hilbert-space Born form only "combined with standard reconstruction results" (its Section 7 / Corollary 2); the article had "in the standard Hilbert-space formulation, this gives …", which elided that dependency. Now reads "Combined with the standard reconstruction results that fix the Hilbert-space form, this gives …".
- **Zurek 2005 title truncated (fixed).** Crossref for 10.1103/PhysRevA.71.052105 gives "Probabilities from entanglement, Born's rule p_k=|ψ_k|² from envariance"; the References entry dropped the formula. Restored.

### Medium Issues Found

- None. The 08-17 purification clause and the 08-02 improper-mixture paragraph both check out against their sources (above).

### Low Issues Found

- `description` was 162 chars (spec 150–160); trimmed to 160 with no loss of content.
- "This distinction is load-bearing for the Map's reading" — default-intensifier use flagged by the style guide; rephrased to "The Map's reading depends on this distinction."

### Counterarguments Considered

- *Quantum Skeptic / Empiricist*: "the theorem's premises are untested in neural tissue, so the constraint says nothing about the brain." Already the article's own first Qualification; not re-flagged.
- *Many-Worlds Defender*: Deutsch–Wallace derive the Born rule without any actualisation. The article lists them in the reconstruction sequence and marks Everettian readings as outside the tenet space — honest boundary-marking, bedrock, not re-flagged.
- *Eliminativist / Physicalist*: the "any participant, physical or non-physical" scope extension is the Map's, not the paper's. The article already says so explicitly ("a Map-side inference, not a source-side claim"); re-confirmed this session that the paper's language is purely operational (Alice/Bob), so the separation is accurate.

### Possibility/probability slippage

None. Calibration unchanged from 07-14: mathematical-theorem on the five-tier scale, preprint status flagged in the lead and the References, default corridor reading named as signature-free and preferred on conservatism grounds only. Diagnostic test (would a tenet-accepting reviewer flag any claim as overstated?): no.

### Reasoning-mode classification (editor-internal)

The article names Stapp, Chalmers–McQueen, Arana and Penrose–Hameroff as proposal *families* the constraint bears on, not as opponents it refutes — no refutation is claimed, so no boundary-substitution risk. Everettian / Bohmian / orthodox-pragmatist: Mode Three, explicit ("lies outside the Map's tenet space and is not addressed here"). No editor-vocabulary leakage found (grep for the forbidden labels: zero hits).

## Citation Web-Verification (per-citation ledger)

Trigger: References block modified since the last deep-review (entries 5–9 added 08-02). Entries whose text is unchanged since the 06-03 ledger are carried, not re-fetched, per §2.4.

- Torres Alegre, E. O. (2025), arXiv:2512.12636 — **real-correct** (re-verified this session: v3, 4 Feb 2026, still unrefereed; byline Enso O. Torres Alegre; Theorem 1 and Remark 1 match the corrected body sentence).
- Deutsch, D. (1999), Proc. R. Soc. Lond. A 455(1988):3129–3137 — **real-correct** (Crossref 10.1098/rspa.1999.0443; Royal Society page 403s WebFetch).
- Wallace, D. (2003), SHPMP 34(3):415–439 — **real-correct** (ADS 2003SHPMP..34..415W; arXiv quant-ph/0303050).
- Wallace, D. (2012), *The Emergent Multiverse*, OUP — **real-correct** (OUP ISBN 978-0-19-954696-1).
- Zurek, W. H. (2005), Phys. Rev. A 71(5):052105 — **real-wrong-metadata** (title truncated; was "Probabilities from Entanglement, Born's Rule from Envariance", corrected to "… Born's Rule p_k = |ψ_k|² from Envariance"; Crossref 10.1103/PhysRevA.71.052105; APS page 403s WebFetch).
- Arana, A. (2025), PhilArchive ARATCQ-2 — **carried from 06-03 ledger** (verified there against the PhilArchive record; PhilArchive and PhilPapers both 403 WebFetch this session; entry text unchanged, only its position in the list is new).
- Masanes–Galley–Müller (2019), Gleason (1957), Agrawal–Wilson (2025) arXiv:2511.21355, Tonetto (PhilArchive TONWPA) — **carried, real-correct** (unchanged since the 06-03 per-cite pass; Tonetto quote independently re-verified 07-14).
- Southgate & Oquatre-sept / Oquatre-six (2026) — Map self-cites, not externally verifiable, intentionally retained.
- Inline ↔ References cross-check: every inline cite (Gleason, Deutsch, Wallace ×2, Zurek, MGM, Agrawal–Wilson, Torres Alegre, Arana, Tonetto) has an entry; every entry is cited inline except the two Map self-cites. **Closed.**
- Superlative sweep (`find_superlative_claims`): empty; no currency check needed.

## Optimistic Analysis Summary

### Strengths Preserved

- Form/existence partition and its tie to [completeness-in-physics-under-dualism](/topics/completeness-in-physics-under-dualism/).
- The three-family taxonomy with the explicit "favours no reading" disclaimer.
- The candour paragraph (default corridor reading is signature-free; preference rests on conservatism).
- Source/Map separation paragraph ("a Map-side inference, not a source-side claim").
- "Two Qualifications" section as a pre-emption of the metaphysical-decisive reading.
- The Hardline Empiricist and the Process Philosopher were not in tension anywhere: the article never lets tenet-coherence lift the evidential tier.

### Enhancements Made

- Theorem sentence now states the relation the paper actually proves (transition probability, not inner product) and names the reconstruction-results dependency — a precision gain that also makes the "form, not existence" claim sharper, since the paper itself splits the causal-consistency step from the Hilbert-space step.

### Cross-links Added

- [generalised-probabilistic-theories](/concepts/generalised-probabilistic-theories/) — already linked twice in the body; now also in `concepts:` and Further Reading.
- [sorkin-higher-order-interference](/concepts/sorkin-higher-order-interference/) — added to `related_articles` and Further Reading. The Sorkin page supplies the measured coordinate (κ) of the Born form this article derives structurally; the two were explicitly complementary with no reciprocal link. This is item (1) of the P3 task "Cross-links from optimistic review 2026-07-16 (born-rule/GPT cluster)"; items (2) and (3) target other files and are untouched.

## Remaining Items

- The P3 task just mentioned sits at todo.md line ~22182, which is **below the `## Vetoed Tasks` header (line 19145)** — the task parser will never execute it there. Item (1) is now done by this pass; if items (2)–(3) are still wanted the task needs re-homing above `## Completed Tasks`. Not re-homed here (human call).
- Arana (2025) has not been re-fetched at PhilArchive since 06-03 because the host 403s WebFetch; a future pass with a working fetch path could close that.

## Stability Notes

- Fifth review. The only defect this pass found was in a sentence untouched since creation — the transition-probability/inner-product conflation — which four prior passes and a per-cite ledger did not catch because it is a *reading* error, not a metadata error. Future passes: the corrected sentence is verified verbatim against Theorem 1 / Remark 1 / Corollary 2 of 2512.12636v3; do not "simplify" it back to "inner product".
- Torres Alegre initials are **E. O.** — do NOT revert to J./G./S.
- Purification-with-uniqueness clause is the paper's own wording; do not strip the uniqueness half.
- Candour paragraph, source/Map-separation paragraph, and the improper-mixture paragraph are calibration content — do not unwind.
- Tonetto quote verbatim and correctly attributed — do not re-flag.
- Bedrock: MWI/Bohmian/orthodox readings lie outside the tenet space by the article's own statement; not a flaw.