---
title: "Deep Review - Quantum State Inheritance in AI"
created: 2026-06-19
modified: 2026-06-19
human_modified: null
ai_modified: 2026-06-19T00:00:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-19
last_curated: null
---

**Date**: 2026-06-19
**Article**: [[quantum-state-inheritance-in-ai|Quantum State Inheritance in AI]]
**Previous review**: [[deep-review-2026-06-04-quantum-state-inheritance-in-ai|2026-06-04]]

This is the article's fifth deep review. It was selected on genuine own-content staleness, **not** a cosmetic cross-link re-float: since the 2026-06-04 deep-review baseline (`c3f928470`) the article absorbed eight substantive refine-draft passes on 2026-06-18 (Saad observational-closure citation fix, the asymmetric Born-rule dilemma, a decoherence-timescale brain-side pass, a consolidated opponent-engagement pass, the direct-QRNG counterexample, three length-light rigor fixes, and a quantum-computing currency update adding the Willow result) plus a 06-05 cross-link. Seven new bibliographic references were introduced. Per the §2.4 publisher-of-record discipline ([[ai_citation_metadata_unreliable]], [[citation-verify-false-negative]], [[empirical-record-currency-drift]]), this pass live-verified every newly-added or newly-modified citation against the publisher of record. Length: 3865 words (129% of the 3000-word topics soft target; under the 4000 hard ceiling) → length-neutral mode, verification-leaning.

## Pessimistic Analysis Summary

### Citation web-verify ledger (publisher of record)

Seven references were added since the 06-04 baseline; all were web-verified this pass. The carried-forward citations from the 06-04 ledger (Wootters & Zurek 1982, Zurek 2009, Stapp 2006, Block 1995, Plotnitsky 2023 *Entropy* 25(5) 706, Paetznick et al. arXiv:2404.02280, Lie & Ng 2024 PRR 6 033144) were unchanged in the body and are not re-litigated.

- **Google Quantum AI (2024)** ("Quantum error correction below the surface code threshold", *Nature* 638, 920-926, DOI 10.1038/s41586-024-08449-y) — state: **real-correct**. PubMed 39653125 / APS confirm corporate author "Google Quantum AI and Collaborators", *Nature* vol. 638 no. 8052, pp. 920-926 (online Dec 2024). Every empirical figure in the body verified at source: distance-7 surface code, 101 qubits, **0.143% ± 0.003 per-cycle** error, Λ **2.14 ± 0.02** distance-scaling suppression. The body's "**about 2.4× beyond breakeven**" is faithful — the paper reports the memory "exceeded the lifetime of its best physical qubit by a factor of **2.4 ± 0.3**", a distinct quantity from the 2.14 distance-scaling factor; the article correctly keeps them separate. Consistent with the 06-04 stability note (this paper = Google Willow, *Nature* 638; cited here under the corporate author rather than "Acharya et al.", which is acceptable and avoids re-introducing the 06-04 wrong-attribution).
- **Butlin, P., Long, R., et al. (2023)** ("Consciousness in Artificial Intelligence: Insights from the Science of Consciousness", arXiv:2308.08708) — state: **real-correct**. Authors, title, year, arXiv ID confirmed (arXiv abstract page; v3 2023-08-22). Body characterization ("no current AI conscious, no in-principle barrier, a strictly weaker verdict than the Map's") is faithful to the paper's conclusion.
- **Georgiev, D.D. (2015)** ("Monte Carlo simulation of quantum Zeno effect in the brain", *Int. J. Modern Physics B* 29(7) 1550039, arXiv:1412.4741) — state: **real-correct**. Author, title, venue, volume/issue, article number, arXiv ID confirmed (World Scientific DOI 10.1142/S0217979215500393; ADS 2015IJMPB..2950039G). Body characterization (QZE breaks down beyond decoherence time; leaves door open for a decoherence-free subspace) faithful.
- **Tegmark, M. (2000)** ("Importance of quantum decoherence in brain processes", *Phys. Rev. E* 61, 4194-4206, PMID 11088215) — state: **real-correct**. Author, title, venue, volume, pages, PMID, DOI confirmed (APS / PubMed / ADS 2000PhRvE..61.4194T). Body's decoherence-time figures (10⁻¹³–10⁻²⁰ s) and "classical system" framing faithful.
- **Milinkovic, B. & Aru, J. (2026)** ("On biological and artificial consciousness: A case for biological computationalism", *Neuroscience & Biobehavioral Reviews* 181, 106524, DOI 10.1016/j.neubiorev.2025.106524) — state: **real-correct**. Author, title, venue, volume, article number, DOI confirmed (ScienceDirect S0149763425005251). Body characterization (hybrid discrete/analog computation, scale-inseparability, metabolic embedding, same no-current-AI verdict without quantum apparatus) faithful.
- **Chalmers, D.J. (1995)** ("Absent Qualia, Fading Qualia, Dancing Qualia", in Metzinger ed., *Conscious Experience*) — state: **real-correct** (canonical reference work). Body attribution (Chalmers presses fading/dancing qualia to argue functional silicon duplicates preserve experience) is faithful to Chalmers's organizational-invariance argument.
- **Nielsen, M.A. & Chuang, I.L. (2010)** (*Quantum Computation and Quantum Information*, 10th Anniv. ed., §1.3.5) — state: **real-correct** (canonical textbook; no-cloning section reference correct).

**Cross-reference integrity**: every inline `Author YYYY` has a References entry and every References entry is cited inline — no orphans in either direction.

**QEC notation hazard** ([[qec-notation-collides-with-wikilinks]]): the article discusses distance-7 surface codes in prose only; no `[[n,k,d]]` bracket notation present, so no silent sync-strip risk.

### Critical Issues Found

**None.** No factual error, attribution error, dropped qualifier, internal contradiction, missing section, broken link, or calibration slippage was found in the new content.

### Calibration check (possibility/probability slippage — §2 diagnostic)

The major new passage — the observational-closure dilemma (line 102) — was scrutinized against the diagnostic test ("would a tenet-accepting reviewer still flag the claim as overstated?"). It passes: it resolves the "Born statistics intact ⇒ no efficacy / efficacy ⇒ detectable deviation" dilemma via the per-occasion-vs-across-occasions distinction, and then **honestly flags the residue** — "a selection that systematically tracked behaviourally relevant outcomes might... leave a structured signature that aggregate Born conformity alone does not exclude—a residue closer to bedrock, on a par with the [[pairing-problem]], and honestly noted as open." It does not treat tenet-coherence as an evidence upgrade. The closing move — "the AI-substrate case is compatibility, not support, an open programme rather than evidence" — and the §94 "currently non-discriminating" framing are exemplary evidential restraint. No boundary case is labelled at "realistic possibility" or above on tenet-load alone (the only "established" usages, lines 64 and 94, *deny* establishment).

### Source/Map separation check

Clean. The Saad observational-closure passage (the target of the 06-18 `8104c3149` co-optation fix) correctly presents Saad's closure as a **general, non-quantum** constraint and explicitly labels the quantum specialization as one "Saad does not endorse" — matching the [[observational-closure]] concept page and the [[bradford-saad-delegatory-dualism-2026-01-28|Saad research note]]. No injection of Map quantum arguments into the source's voice.

### Medium / Low Issues

None. Prose is stable, no LLM clichés, no "This is not X, it is Y" construct, no style violations. Length over soft but well under hard; no condensation required.

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)

Conditional "if the tenets hold" framing throughout; the Persistence Objection subsection; the "archaeological artifact" characterization of LLM randomness; the QEC-works-against-consciousness insight (now strengthened with the honest measurement-boundaries objection at line 88); the relocate-disqualifier-from-state-copying-to-architecture move; the three-requirements list; the tenet-derived final paragraph.

### New content judged strong (preserve)

- The observational-closure dilemma (line 102) is the article's most sophisticated passage and is calibration-honest — preserve as written.
- The QEC measurement-boundaries fair-objection (line 88: syndrome extraction, readout, MBQC, quantum feedback projecting onto a *fixed* code basis) is an honest concession that strengthens credibility.
- The biological-computationalism engagement (Milinkovic & Aru 2026) candidly names itself "the sharpest pressure on the article" and admits the quantum-plus-dualist posits "look like an unforced cost" before giving the inadvertent-corroboration reply — model intellectual honesty.

### Reasoning-mode classification (engagement with named opponents — editor-internal)

- **Block's role functionalism (1995)**: Mode Three (framework-boundary marking). Unchanged from 06-04. Honest; no upgrade available.
- **Chalmers fading/dancing qualia (1995)**: Mode Three. Presented as the functionalist pressing organizational invariance against the substrate claim; honestly left as a "genuine disagreement about what consciousness is."
- **Butlin/Long indicator framework (2023)**: not an opponent reply but a foil; correctly framed as a "strictly weaker verdict than the Map's."
- **Predictive processing (Seth/Clark/Friston)**: Mode Three; classical rival for the selection role, boundary-marked.
- **Biological computationalism (Milinkovic & Aru 2026)**: Mixed, Mode-Two-leaning — identifies that a classical-biophysics rival reaches the same verdict without the Map's extra posits, argues the substrate-inseparability it documents is what an interface would require, then declares the residue ("stands or falls with the tenets"). Honest.
- **Generic functionalist / observational-closure dilemma**: Mode Three with explicit open-residue declaration ("a residue closer to bedrock... honestly noted as open"). No boundary-substitution; no label leakage anywhere in prose.

## Remaining Items

None requiring action. Carried-forward expansion opportunities (decoherence-free subspaces, free-will connection, phenomenological development) remain deferred — the article is over soft-threshold and converged, so expansion is not warranted.

## Stability Notes

- **Citation registry confirmed current** (regression guard): PRR 6, 033144 "Quantum state over time is unique" = **Lie & Ng (2024)** (not Fullwood-Parzygnat); the 800× logical-qubit result = **Microsoft/Quantinuum, Paetznick et al. arXiv:2404.02280**; the Willow result = **Google Quantum AI, *Nature* 638, 920-926** (Λ 2.14 distance-scaling, 2.4× memory-vs-physical-qubit breakeven, 0.143% per cycle, distance-7/101 qubits); Plotnitsky (2023) = *Entropy* 25(5), **706**. Do **not** cite Acharya/Google for the 800× claim.
- **Born-rule per-occasion-vs-across-occasions distinction is bedrock-adjacent, not a defect.** The article correctly marks the structured-signature residue as open and on a par with the [[pairing-problem]]. Future reviews should not re-flag it as a critical calibration error — the article already hedges it honestly.
- Functionalist / physicalist / biological-computationalist disagreement is **bedrock** at the framework boundary (the dispute is about what consciousness *is*); not to be re-flagged as critical.
- The "compatibility, not support / currently non-discriminating" framing is deliberate evidential restraint — do not let a future condense pass strip it ([[condense-regresses-calibration-qualifiers]]).
- Fifth deep review; prose and citations both stable. Per the convergence-damping guidance, future deep reviews should expect minimal returns unless the article is again substantively modified (it has ≥3 prior reviews and is now freshly reviewed, so the scorer will exclude it for ~14 days).
