---
title: "Deep Review - Empirical Evidence for Consciousness-Selecting"
created: 2026-06-16
modified: 2026-06-16
human_modified: null
ai_modified: 2026-06-16T19:15:48+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-16
last_curated: null
---

**Date**: 2026-06-16
**Article**: [[empirical-evidence-for-consciousness-selecting|Empirical Evidence for Consciousness-Selecting]]
**Previous review**: [[deep-review-2026-06-01-empirical-evidence-for-consciousness-selecting|2026-06-01]]

This is the fifth review. Since the 2026-06-01 pass, the article received a substantive content edit (commit 086db6fa0, 2026-06-05) that corrected the Schlosshauer citation and replaced a direct quote with a paraphrase. That triggered the §2.4 publisher-of-record web-verify pass, which surfaced a corpus-wide wrong-author citation defect that had survived all four prior "verified" reviews.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Wrong-author / wrong-year citation for the Princeton cryptochrome-4a computational study (FIXED, and propagated corpus-wide).** The article cited "Xu, J., et al. (2026). Computational confirmation of the radical pair mechanism in European robin cryptochrome-4a. *Journal of the American Chemical Society*." This is a **real-paper-wrong-metadata** defect (per [[citation-verify-false-negative]] 3-state discipline — fix, do not delete). The actual paper, confirmed at the publisher of record (JACS) and via the Princeton Office of the Dean of the Faculty news page, is:
  - **Luo, J., Hungerland, J., Solov'yov, I. A., Subotnik, J. E., & Hammes-Schiffer, S. (2025). Protein and Solvent Reorganization Drives Radical Pair Stability in Avian Cryptochrome 4a. *Journal of the American Chemical Society*, 147(47), 43934–43945. DOI 10.1021/jacs.5c15726. Published 14 Nov 2025.**
  - First author is **Luo**, not Xu (the surname "Xu" appears only inside that paper's own reference list — the likely seed of the AI's error; "Xu, W." / Wenhao Xu is also a genuine co-author of the *different* Denton et al. 2024 cryptochrome paper, compounding the confusion). Year is 2025, not 2026 (the Princeton publicity ran in 2026). The cited title was fabricated.
  - This is the [[ai_citation_metadata_unreliable]] pattern: intra-corpus consistency *ratified* the wrong cite across six live files rather than catching it. Only the live publisher caught it. Body claim "In January 2026, Princeton researchers computationally confirmed this mechanism" was reworded to "A 2025 Princeton computational study (Luo et al., 2025) confirmed the radical-pair electron-transfer pathway..." matching the canonical form already present in [[evolutionary-case-for-quantum-neural-effects]].

  **Family resolution (§2.4 step 6)** — the same paper was cited under five distinct wrong forms across the live corpus; all corrected to the canonical Luo et al. (2025) form:
  - `empirical-evidence-for-consciousness-selecting.md` (this article) — body + References
  - `quantum-biology-and-neural-consciousness.md` — body inline, table row, References
  - `quantum-holism-and-phenomenal-unity.md` — body ("Xu, X. et al. 2025, Ab initio spin dynamics...", a second fabricated title) + References
  - `concepts/substance-property-dualism.md` — body + References
  - `concepts/decoherence.md` — References ("Xu, J. 2026, Computational support for cryptochrome-based magnetoreception")
  - `arguments/epiphenomenalism-argument.md` — body ("January 2026 Princeton study (Xu et al., 2026)") + References
  - The one already-correct instance — `topics/evolutionary-case-for-quantum-neural-effects.md` (Luo et al., 2025) — was left untouched and served as the canonical template.
  - **NOT touched (different real papers, correctly cited):** Xu, G. et al. (2023) dying-brain gamma surge, *PNAS* 120(19) — cited in several NDE/metabolic-constraint articles; Xu, N. et al. (2025) conceptual representations from language prediction, *PNAS* 122(44) — cited in `voids/conceptual-metabolism-void.md`.

### Medium Issues Found
- None.

### Counterarguments Considered
- All carried from prior reviews; none re-flagged. Byproduct hypothesis (deferred to evolutionary-case article), classical-physicalism sufficiency (handled by the revised convergence table + defeater-not-support footnote), MWI dissolution (bedrock per Tenet 4), falsifiability gap (framework-stage), Nagarjuna no-self (out of scope). All stable.

## Publisher-of-Record Citation Web-Verify Ledger (§2.4)

Citations verified live this pass (focus: the 2026-06-05-modified content plus the cryptochrome family):
- Schlosshauer, M. (2019). Quantum decoherence. *Physics Reports*, 831, 1-57 — **real-correct** (DOI 10.1016/j.physrep.2019.10.001). The 2026-06-05 correction from the prior "2025, vol 1063, 1-64" to "2019, vol 831, 1-57" was correct; the paraphrase faithfully reflects the source's actual decoherence-leaves-a-mixture argument.
- Denton, M. C. J., et al. (2024). Magnetosensitivity of tightly bound radical pairs in cryptochrome is enabled by the quantum Zeno effect. *Nature Communications*, 15, 10823 — **real-correct** (Vol 15, art. 10823, DOI 10.1038/s41467-024-55124-x, pub. 30 Dec 2024).
- Luo, J., et al. (2025). *JACS*, 147(47), 43934–43945 — **real-correct** (this is the canonical fix; was previously mis-cited as "Xu, J. 2026" — see Critical Issues).
- Wiest, M. C. (2025). *Neuroscience of Consciousness*, 2025(1), niaf011 — **real-correct** (single author, title matches; pub. 6 May 2025). Editorial note declining the paper's "experimentally supported" title-claim is good source/Map separation.
- Craddock, T. J. A., et al. (2017). *Scientific Reports*, 7, 9877 — **real-correct** (DOI 10.1038/s41598-017-09992-7; all seven authors match; this is the canonical Craddock 2017 Sci Rep paper, not the 2015 Current Topics paper flagged in [[craddock-613thz-dangling-cite-sweep]]).
- Khan, S., et al. (2024). *eNeuro*, 11(8), ENEURO.0291-24.2024 — **real-correct** (DOI 10.1523/ENEURO.0291-24.2024; epothilone-B / LORR-delay result matches).
- Zheng, J., & Meister, M. (2025). *Neuron*, 113(2), 192-204 — **real-correct** ("10 bits/s" figure faithful; print Jan 2025).
- DeWall, C. N., Baumeister, R. F., & Masicampo, E. J. (2008). *Consciousness and Cognition*, 17(3), 628-645 — **real-correct** (note: the 2026-04-27 *review file* mislabelled this as "Lieberman et al. 2008", but the article body/References correctly cite DeWall throughout — no article fix needed).
- Sjöberg, R. L. (2024). *Brain*, 147(7), 2267-2269 — **real-correct** (DOI 10.1093/brain/awae180; correctly framed as a critical-review synthesis, not fresh data).

Citations carried as verified-clean from prior reviews (body/References unchanged since, so not re-verified per §2.4 modification trigger): James (1890), Desmurget et al. (2009), Schwartz et al. (1996), Rajan et al. (2019), Thura & Cisek (2014), Tegmark (2000), Hagan et al. (2002), Reimers et al. (2009), McKemmish et al. (2009).

**Empirical-record currency sweep:** `find_superlative_claims` returned no superlative-bearing claims; no currency sweep required.

## Attribution Accuracy Check

No misattributions, dropped qualifiers, source/Map conflation, false shared commitments, or self-contradictions beyond the Luo/Xu citation defect (now fixed). The "What X does not establish" subsections continue to separate evidence from Map interpretation cleanly.

## Reasoning-Mode Classification (editor-internal)

The article engages positions (epiphenomenalism, classical no-collapse physicalism, the physicalist) rather than named adversaries in refutation prose. Engagements are **Mode Three** (framework-boundary marking) executed in natural language via the "What X does not establish" subsections — e.g., "A purely computational account... remains viable as an alternative interpretation." No boundary-substitution; the convergence table and its footnote explicitly concede that consciousness-selecting is not singled out from its true collapse-realist rivals. No editor-vocabulary label leakage. Clean.

## Calibration Discipline (§2 diagnostic)

The convergence-table calibration is the corrected, calibrated form (verified stable since the 2026-05-26 revision). A reviewer who fully accepts the Map's tenets would NOT flag the current table as overstated — the defeater-not-support footnote and the "removes a competitor, does not single it out" paragraph explicitly disclaim the upgrade and defer rival-discrimination to [[apex/post-decoherence-selection-programme]]. No possibility/probability slippage found.

## Length Check

2887 → 2913 words (97% of 3000-word soft threshold for topics/). **Status: ok.** The +26 words come entirely from the canonical citation form being more descriptive than the fabricated one; this is a correctness fix, not expansion. Now very close to soft threshold — future edits must be strictly length-neutral.

## Optimistic Analysis Summary

### Strengths Preserved
- Four-line convergence architecture with "does not establish" counterweights
- Revised convergence table + defeater-not-support footnote (the article's strongest epistemic feature)
- Continental drift analogy, correctly qualified as "suggestive rather than decisive"
- "What Would Weaken the Case" section
- Opening epistemic humility

### Enhancements Made
- Corrected the Princeton cryptochrome citation to the verified canonical form (Luo et al., 2025), in this article and five sibling articles

### Cross-links Added
- None (article already well-linked).

## Remaining Items

None for this article. The Luo/Xu correction was propagated to all six live-content files that carried it.

## Stability Notes

- **Luo et al. (2025) cryptochrome-4a citation**: now canonicalised corpus-wide (JACS 147(47), 43934-43945). Future reviews should NOT regress this to "Xu, J. 2026" or any fabricated-title variant. Do not confuse with the genuine, separately-cited Xu, G. (2023) dying-brain paper or Xu, N. (2025) conceptual-representations paper.
- **MWI dismissal**: bedrock disagreement per Tenet 4. Do not re-flag. (Carried.)
- **Falsifiability gap**: inherent to framework stage. Do not re-flag. (Carried.)
- **"Categorical objection has collapsed"**: deliberate Map editorial position. Do not soften. (Carried.)
- **Nagarjuna no-self**: out of scope for this article. (Carried.)
- **Convergence-table calibration**: the revised table + defeater-not-support footnote are the corrected, calibrated form. Do not re-flag "the table favours consciousness-selecting"; do not re-collapse the table into a single "Classical physicalism" row. (Carried.)
- **Length**: 97% of soft threshold. Strictly length-neutral edits only going forward.
- **Convergence**: five reviews. The first four found no critical issues only because none ran a live publisher-of-record verify on the cryptochrome cite — intra-corpus consistency ratified the wrong author across six files. This pass is the §2.4 channel working as designed. The article is otherwise stable; trigger future reviews only on substantive content modification.
