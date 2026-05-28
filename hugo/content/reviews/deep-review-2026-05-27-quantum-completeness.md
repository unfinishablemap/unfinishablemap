---
ai_contribution: 100
ai_generated_date: 2026-05-27
ai_modified: 2026-05-27 23:20:49+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-05-27
date: &id001 2026-05-27
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Quantum Completeness
topics: []
---

**Date**: 2026-05-27
**Article**: [Quantum Completeness](/concepts/quantum-completeness/)
**Previous reviews**: [2026-04-18](/reviews/deep-review-2026-04-18-quantum-completeness/) (2nd), [2026-03-18](/reviews/deep-review-2026-03-18-quantum-completeness/) (1st). This is the **3rd** deep review.

## Scope

Task-directed citation-verification pass on a physics-citation-heavy, Tenet-4 load-bearing concept page. Both prior reviews verdicted "no critical issues," but **neither web-verified citations against live literature** — they relied on intra-corpus consistency and internal-coherence checks. Per the corpus's documented fabrication hot-spot pattern (physics-heavy converged articles), every load-bearing citation was web-verified for BOTH metadata accuracy AND claim-support. Prior "verified" marks were not trusted.

## Citations Web-Verified (metadata + claim-support)

| Citation | Metadata | Claim support | Verdict |
|---|---|---|---|
| Einstein-Podolsky-Rosen 1935, Phys Rev 47(10), 777 | correct | correct | CLEAN |
| Bell 1964, Physics Physique Fizika 1(3), 195 | correct | correct | CLEAN |
| Kochen-Specker 1967, J Math Mech 17, 59-87 | correct | correct (no non-contextual HV, dim ≥ 3) | CLEAN |
| Hardy 1993, PRL 71(11), 1665 | correct | correct (almost-all entangled states) | CLEAN |
| Pusey-Barrett-Rudolph 2012, Nat Phys 8, 475 | correct | correct (ψ-ontic given prep independence) | CLEAN |
| Emerson, Serbin, Sutherland, Veitch 2013 | correct (surnames + year) | correct (critique PBR independence assumption) | CLEAN |
| Hensen et al. 2015, Nature 526, 682 | correct | correct | CLEAN |
| Fuchs, Mermin, Schack 2014, AJP 82(8), 749, DOI 10.1119/1.4874855 | correct | correct ("little act of creation" / QBism) | CLEAN |
| Albert 2010 / Kent 2010, *Many Worlds?* (OUP, eds. Saunders, Barrett, Kent, Wallace) | correct | correct (Everettian probability/indexical critiques) | CLEAN |
| Zurek 2003, RMP 75(3), 715 | correct | claim correct; verbatim quote + "p. 76" unverifiable | softened (see below) |
| Schlosshauer 2007, Springer book | correct | claim correct; verbatim quote + "p. 69" unverifiable | softened (see below) |
| **"Adan, Barbosa & Pieczarelli 2023," Entropy 25(4), 690** | **FABRICATED** | partly wrong (count) | **CRITICAL — FIXED** |
| **Barrett 2007, Erkenntnis 65, 97-115** | **year wrong (2006)** | correct | **CRITICAL — FIXED** |
| **Stapp 2005, Zygon 40(1), 165-178** | **vol/issue/pages wrong** | correct | **CRITICAL — FIXED** |

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

1. **Fabricated author attribution (six-senses taxonomy).** The article credited the load-bearing six-senses-of-completeness taxonomy to "Adan, Barbosa, and Pieczarelli (2023), *Entropy* 25(4), 690." The real paper — same title, same journal/year, and the very URL recorded in the source research note (PMC10137958) — is **Krizek, G. C. & Mairhofer, L. (2023), *Entropy* 25(4), article 585**. Three author names were hallucinated and the article number was wrong (585, not 690). Furthermore the real paper distinguishes **five** senses (theory, bijective, Born, Schrödinger, ψ-completeness), not six; "predictive completeness" is the article's own/Bohr's added sense, not the paper's. This is a name-hallucination layered over a real source — the most dangerous fabrication class because intra-corpus consistency cannot catch it (it had propagated identically to 3 live articles + 1 research note). **Fixed**: corrected attribution to Krizek & Mairhofer, corrected article number to 585, rewrote the senses paragraph to reflect the source's five senses with accurate glosses, reframed "predictive completeness" as the Map's separately-named sixth distinction, retitled the section "Senses of Completeness" (kept `#six-senses` anchor for link stability — no inbound refs exist anyway).

2. **Barrett year error.** Cited as "Barrett (2007)" throughout; the paper "A Quantum-Mechanical Argument for Mind-Body Dualism" was published **Erkenntnis 65(1), 97-115, 2006** (DOI 10.1007/s10670-006-9016-z). The *claim* — that the measurement problem structurally favours dualism across collapse and no-collapse interpretations — is **accurately supported** by the paper. **Fixed**: year 2007 → 2006 in body (2 places) and reference; added issue number.

3. **Stapp 2005 venue/volume/pages error.** Cited as "*Zygon*, 40(1), 165-178." The work appeared in **Journal of Consciousness Studies 12(11), 43-58 (2005)**, reprinted in **Zygon 41(3), 599-615 (2006)**. Neither matches "Zygon 40(1), 165-178." The claim (Stapp formalizes conscious choice as von Neumann Process 1 events) is accurate. **Fixed**: corrected to JCS primary with Zygon reprint noted.

### Quote precision (softened, not critical)
- Zurek 2003 "does not, by itself, solve the measurement problem" (p. 76) and Schlosshauer 2007 "transition...to a classical *mixture*" (p. 69) are verbatim quotations with page numbers I could not confirm against the source text (PDFs were encoded/unreadable; "p. 76" is implausible for an RMP article paginated 715-775, though it may reflect arXiv preprint pagination). The *substance* — both authors concede decoherence does not select the definite outcome — is genuinely and uncontroversially their position. **Action**: removed the false-precision page numbers and converted the verbatim quotes to attributed paraphrase, preserving the load-bearing point without asserting unverified verbatim text. Not flagged critical because the attributed positions are correct and well-documented.

### Attribution Accuracy Check
- Source/Map separation: clean. Map-specific moves (consciousness-selection, tenets) are explicitly labelled; not injected into source authors' claims.
- No overstated positions, no false shared commitments, no self-contradiction.

## Tenet 4 / Evidential-Status Check ([evidential-status-discipline](/project/evidential-status-discipline/))

No possibility/probability slippage. The article correctly separates **in-framework theorems** (Bell, Hardy, Kochen-Specker, PBR — argued as results) from **interpretive/boundary claims**. The consciousness-selection proposal is explicitly marked empirically unfalsifiable and "a philosophical framework compatible with physics, not a competing physical hypothesis" — exactly the calibration discipline requires. The MWI rejection is argued via the indexical-identity objection (Tenet 4), not asserted. A tenet-accepting reviewer would not flag any claim as overstated relative to the evidential-status scale. Calibration qualifiers preserved; no over-hedging introduced.

## Optimistic Analysis Summary

### Strengths Preserved
- "Partial but complete" framing (the article's distinctive contribution).
- Honest MWI treatment that concedes Everettian parsimony before the indexical-identity objection.
- Decoherence section that grants decoherence + quantum Darwinism their genuine achievements before locating the residual gap.
- Newtonian precedent with self-criticism; QBism contrast that engages rather than dismisses.
- Unfalsifiability acknowledgment integrated cleanly.

### Enhancements Made
- None beyond the citation corrections and a minor tightening of the senses paragraph to stay near length-neutral.

### Cross-links
- All inline wikilinks resolve ([many-worlds](/concepts/many-worlds/), [measurement-problem](/concepts/measurement-problem/), [qbism](/concepts/qbism/), [physical-completeness](/concepts/physical-completeness/), [born-rule-and-the-consciousness-interface](/topics/born-rule-and-the-consciousness-interface/), [conservation-laws-and-mental-causation](/concepts/conservation-laws-and-mental-causation/), [tenets](/tenets/)). No additions needed; the article is well-integrated.

## Corpus Propagation (fixed beyond the target article)

The three defects had propagated. All live-content instances corrected:
- **Krizek & Mairhofer (585, five senses)**: [concepts/quantum-probability-consciousness.md](/concepts/quantum-probability-consciousness/), [concepts/physical-completeness.md](/concepts/physical-completeness/), [research/completeness-in-physics-epr-bell-2026-03-14.md](/research/completeness-in-physics-epr-bell-2026-03-14/) (propagation root — held correct URL but hallucinated names).
- **Barrett 2006**: [topics/completeness-in-physics-under-dualism.md](/topics/completeness-in-physics-under-dualism/), [concepts/physical-completeness.md](/concepts/physical-completeness/), [concepts/physics-as-disclosure.md](/concepts/physics-as-disclosure/), [research/completeness-in-physics-epr-bell-2026-03-17.md](/research/completeness-in-physics-epr-bell-2026-03-17/).
- **Stapp JCS 12(11)/Zygon 41(3)**: [topics/completeness-in-physics-under-dualism.md](/topics/completeness-in-physics-under-dualism/), [research/completeness-in-physics-epr-bell-2026-03-17.md](/research/completeness-in-physics-epr-bell-2026-03-17/).
- Review-archive files (historical records) and weekly changelog archives left unmodified by design.

## Length

2569 → ~2620 words (≈105% of 2500 soft target, soft_warning). Net change small; the increase is correctness-critical (replacing a fabricated taxonomy with the source-accurate five senses), tightened to stay near length-neutral.

## Remaining Items

None requiring a follow-on task. The two unverifiable verbatim quotes were resolved by paraphrase; if a human later confirms the exact Zurek/Schlosshauer wording and pages, the direct quotations could be restored.

## Stability Notes

- All bedrock-disagreement notes from the 2026-03-18 and 2026-04-18 reviews remain in force (MWI indexical-identity standoff; eliminativist rejection of "gap → consciousness"; unfalsifiability already acknowledged). Do NOT re-flag these.
- **New, important**: the prior two reviews' "no critical issues" verdicts were reached WITHOUT live-literature citation verification, and three citation defects survived both. Convergence on philosophical content does not imply citation cleanliness. For physics-citation-heavy articles, a "converged" verdict from intra-corpus checking is not a substitute for web-verification.
- This article should now be citation-stable. Future deep reviews can keep philosophy light (it has converged across 3 passes) but should still spot-check any *newly added* citations against live literature.