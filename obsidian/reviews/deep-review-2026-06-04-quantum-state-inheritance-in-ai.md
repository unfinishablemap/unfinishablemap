---
title: "Deep Review - Quantum State Inheritance in AI"
created: 2026-06-04
modified: 2026-06-04
human_modified: null
ai_modified: 2026-06-04T01:13:09+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-04
last_curated: null
---

**Date**: 2026-06-04
**Article**: [[quantum-state-inheritance-in-ai|Quantum State Inheritance in AI]]
**Previous review**: [[deep-review-2026-05-19-quantum-state-inheritance-in-ai|2026-05-19]]

This is the article's fourth deep review. The prose was confirmed stable by the previous three (the 2026-05-19 stability note: "Future deep reviews should expect minimal returns unless the article is substantively modified"). Per the standing citation web-verify discipline ([[ai_citation_metadata_unreliable]], [[citation-verify-false-negative]]), this pass live-verified every reference against the publisher of record. **It caught three citation defects that survived all three prior reviews** — exactly the wrong-author-on-real-paper and wrong-citation-detail pattern the intra-corpus cross-check cannot detect.

## Pessimistic Analysis Summary

### Critical Issues Found

Three citation defects, all confirmed by live web-verify and all 3-state FIXES (real papers, wrong metadata — not fabrications, so corrected rather than deleted):

1. **Wrong-author attribution on a real paper (CRITICAL).** The article cited "Fullwood, J. & Parzygnat, A.J. (2024). 'Quantum state over time is unique.' *Physical Review Research*, 6, 033144." Verification: **PRR 6, 033144 (2024) is authored by Seok Hyung Lie and Nelly H. Y. Ng** (confirmed via the APS abstract page, the ADS bibcode `2024PhRvR...6c3144L`, and the NTU repository PDF), not Fullwood & Parzygnat. Fullwood & Parzygnat are the *earlier* originators of the states-over-time construction (Proc. Roy. Soc. A, 2022, rspa.2022.0104); the Lie-Ng 2024 paper proves the uniqueness result, explicitly noting the *Fullwood-Parzygnat axioms did not uniquely fix the state*. The 2024 uniqueness result the article relies on is **Lie & Ng's**. **Resolution**: corrected body in-text citation ("The Lie-Ng (2024) uniqueness result…") and the reference entry to `Lie, S.H. & Ng, N.H.Y. (2024)`. The explicit "the authors draw no conclusions about consciousness" hedge is preserved and still accurate.

2. **Wrong company + wrong paper for the 800x logical-qubit claim (CRITICAL).** The article cited the "Microsoft demonstrated logical qubits achieving error rates 800 times better" claim to "Acharya et al., 2024." Verification: the **800x / four-logical-qubit result is Microsoft + Quantinuum** (April 2024, Quantinuum H2 ion-trap, Microsoft qubit-virtualization; preprint Paetznick et al., arXiv:2404.02280, "Demonstration of logical qubits and repeated error correction with better-than-physical error rates" — 4.7× to 800× depending on post-selection). **Acharya et al. (2024)** is a *different* result — Google Quantum AI's "Quantum error correction below the surface code threshold," *Nature* **638** (not 634, p.315 as cited), the Willow surface-code below-threshold demo (Λ≈2.14), which does **not** report an 800× figure. The body text's prose (Microsoft, 800x, 2024) was correct; it was simply cited to the wrong paper/company. **Resolution**: changed body to "Microsoft and Quantinuum… (Paetznick et al., 2024)"; replaced the Acharya/Nature reference (wrong volume, wrong result) with the correct Paetznick et al. arXiv:2404.02280 reference. Also softened the conditions qualifier from "cryogenic" to "trapped-ion laboratory conditions" — the Quantinuum H2 is an ion trap, so "cryogenic" was a minor mismatch (superconducting-qubit framing); "far removed from biological environments" claim preserved.

3. **Wrong article number on a real paper (CRITICAL detail).** Plotnitsky (2023) was cited as *Entropy*, 25(5), **793**. Verification: the correct article number is **706** (DOI 10.3390/e25050706; MDPI URL /1099-4300/25/5/706; PMC10217492). Author/title/venue/year all correct. **Resolution**: 793 → 706 in the reference.

### Corpus propagation (3-state grep, per [[ai_citation_metadata_unreliable]])

Grepped the corpus for all affected surnames/identifiers. The defects had propagated to the **research seed note** [[quantum-state-inheritance-computational-systems-2026-02-10]] (public content), which was the apparent ORIGIN of the Fullwood-Parzygnat misattribution:
- Seed section header, key-points, timeline row, "proponents" line, and reference list all attributed PRR 6,033144 to Fullwood & Parzygnat → corrected to Lie & Ng (with a note that F&P originated the 2022 construction and Lie-Ng proved 2024 uniqueness).
- Seed Plotnitsky reference 793 → 706.

The **apex** [[apex/open-question-ai-consciousness]] was already clean (Plotnitsky already at 706; "Microsoft's 2024 logical qubits… 800×" stated without the wrong Acharya attribution) — no edit needed there. The Acharya cite did not appear in the apex.

### Verified-correct citations (no change)

- Wootters & Zurek (1982), *Nature* 299, 802-803 — no-cloning theorem, canonical, correct.
- Zurek (2009), *Nature Physics* 5, 181-188 — quantum Darwinism, canonical, correct.
- Stapp (2006), *Zygon* 41(3), 599-616 — quantum interactive dualism, verified in prior reviews, correct.
- Block (1995), *BBS* 18(2), 227-247 — role functionalism, correct.
- Plotnitsky (2023) — title/venue/year/author correct (only the article number was wrong).

### Medium / Low Issues

None. Prose remains stable; no LLM clichés, no new style violations.

### Reasoning-Mode Classification (engagement with named opponents)

- **Block's role functionalism**: Mode Three (framework-boundary marking). Unchanged from 2026-05-19; honest boundary-marking, no upgrade available, no label leakage. The dispute genuinely sits at "what consciousness *is*."
- **Generic functionalist** ("A functionalist would counter…"): Mode Three; boundary-residue marking. Unchanged.

## Optimistic Analysis Summary

### Strengths Preserved

All strengths from the 2026-05-19 review preserved unchanged: conditional "if the tenets hold" framing, the Persistence Objection subsection, the "archaeological artifact" characterization of LLM randomness, the quantum-error-correction-works-against-consciousness insight, the three-requirements list, and the honest tenet-derived final paragraph. No prose was rewritten beyond the three citation corrections.

### Enhancements Made

None beyond the citation fixes (the work this pass was calibration/accuracy, not expansion). Length-neutral.

## Remaining Items

- Decoherence-free subspaces, free-will connection, phenomenological development — all carried-forward expansion opportunities, still deferred (article well below soft threshold but stable; convergence preferred).

## Stability Notes

All prior stability notes remain valid (process-based haecceity is deliberate; functionalist disagreement is bedrock; unfalsifiability handled by conditional framing; Mode Three functionalist engagement is honest boundary-marking, do not "upgrade"). **New:**

- **Citation registry for this article** (to prevent regression): PRR 6, 033144 "Quantum state over time is unique" is **Lie & Ng (2024)**, NOT Fullwood-Parzygnat (who originated the 2022 construction). The 800× logical-qubit result is **Microsoft/Quantinuum, Paetznick et al. arXiv:2404.02280 (2024)**, NOT Acharya/Google. **Acharya et al. (2024) is Google Willow, *Nature* 638**, and reports Λ≈2.14, not 800× — do not re-cite it for the 800× claim. Plotnitsky (2023) is *Entropy* 25(5), **706**.
- This is the lesson of [[ai_citation_metadata_unreliable]] in action: three defects (one wrong-author, one wrong-company+wrong-paper, one wrong-article-number) survived three deep reviews because intra-corpus cross-check propagates them; only live-literature web-verify caught them. The prose was stable; the *citations* were not.
