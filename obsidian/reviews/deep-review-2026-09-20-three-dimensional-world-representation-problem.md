---
title: "Deep Review - The 3D World Representation Problem"
created: 2026-09-20
modified: 2026-09-20
human_modified: null
ai_modified: 2026-09-20T06:41:15+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-20
last_curated: null
---

**Date**: 2026-09-20
**Article**: [[three-dimensional-world-representation-problem|The 3D World Representation Problem]]
**Previous review**: [[deep-review-2026-06-23-three-dimensional-world-representation-problem|2026-06-23]] (sixth prior; series began 2026-03-09)

## Summary

**Verdict: NOT converged — one sourcing defect and one citation-apparatus defect found and fixed.** Six prior reviews (2026-03-09, 03-10, 04-02, 05-19, 06-04, 06-23) certified this article, the last two as explicit no-ops. The lens those reviews never ran is **citation density / uncited claims**: the article carried three References for 3453 words and, as measured this cycle, **zero inline citations**, so all three entries were orphans and no body claim was tied to a source. Running that lens against the publisher of record found a load-bearing empirical claim supported by neither of the article's two scientific references.

Word count 3453 → 3570 (+117). Status `soft_warning` before and after; 429 words of headroom remain to the 3999 usable ceiling.

## Lenses Run (named, so unrun lenses are visible)

| Lens | Run? | Outcome |
|---|---|---|
| Uncited-claim audit (driver's requested lens) | Yes | **2 findings, both fixed** |
| Publisher-of-record citation web-verify (§2.4) | Yes | 3 pre-existing cites verified + 2 new cites verified; per-cite ledger below |
| Inline ↔ References cross-reference (§2.4 step 5) | Yes | **Critical: 3/3 entries were orphans. Fixed.** |
| Result-direction / null-result leg (§2.4 step 7) | Yes | All cited results positive and in the claimed direction |
| Empirical-record currency (superlatives) | Yes | `find_superlative_claims` returns **0** — no sweep required |
| Diff audit of commit `caa06a8168` (unreviewed crosslink prose) | Yes | Both new links hold; see below |
| Wikilink + block-anchor resolution (all 54 link forms) | Yes | All resolve; both `tenets#^…` anchors found |
| Calibration / over-concession | Yes | No new slippage; prior calibration ladder intact |
| Reasoning-mode classification + label leakage | Yes | No leakage; modes unchanged from 2026-06-04 audit |
| Attribution accuracy (§2.5) | Yes | One item examined and cleared — see Medium |
| Length / length-neutral mode | Yes | +117 accepted as corrective, not expansive; see Length Check |
| Lexical anchoring-hedge count | **Deliberately not run** — base rate on this corpus is 8 straight false highs, 0 true positives |

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Border cells were supported by neither reference — FIXED.** §"The Computational Achievement" asserted "border cells respond to environmental boundaries" alongside place, grid and head-direction cells, with the two scientific References (O'Keefe & Nadel 1978; Moser et al. 2008) as the only candidate sources. I fetched the Moser et al. 2008 PDF, NFKC-normalised it and grepped with printed counts against a live control: `grep place cell` = 82, `grid cell` = 56, `head direction`/`head-direction` = 6+4 — index demonstrably live — while **`border cell` = 0 and `boundary` = 0**. The five `Solstad` hits in that paper are to Solstad et al. 2006 (grid→place mathematical model) and Solstad et al. 2007 (grid expansion), not to border cells. The reason is chronological: border cells were first reported in Solstad, Boccara, Kropff, Moser & Moser (2008), *Science* 322(5909):1865–1868, published **19 December 2008**, five months *after* the July 2008 Annual Review. The claim was true but sourced to a paper that predates its discovery. Fixed by citing Solstad et al. 2008 inline and appending it as References entry 4 (appended, not renumbered).

2. **All three References entries were orphans — FIXED.** Measured in the body (lines 50+): `et al.` = 0, `O'Keefe` = 0 outside the References block. No body claim named any source. §2.4 step 5 treats orphans in either direction as critical. Fixed by attaching `(O'Keefe & Nadel 1978; Moser et al. 2008)` and `(Solstad et al. 2008)` to the cell-type roster they support. The self-cite (entry 3) is reached from the body through the `[[capability-division-problem]]` wikilink rather than by name — left as is, since the link does the referential work at zero word cost.

3. **The Friston claim was a bare assertion about a named living researcher's programme — FIXED.** §"What Would Challenge This View?" asserted that "Friston-style active-inference models routinely derive perspectival representations from sensor-fusion principles" with nothing behind it. Verified at PubMed/Elsevier: Rudrauf, Bennequin, Granic, Landini, **Friston** & Williford (2017), "A mathematical model of embodied consciousness", *J. Theor. Biol.* 428:106–131, DOI 10.1016/j.jtbi.2017.05.032. Its abstract states the Projective Consciousness Model holds "the spatial field of consciousness (FoC) is structured by a projective geometry and under the control of a process of active inference", that the FoC "combines multisensory evidence with prior beliefs in memory and frames them by selecting points of view and perspectives", and that the model "can account for ... the characteristic spatial phenomenology of subjective experience".

   This is a *sharper* fact than the article knew. The strongest exemplar of the class does not merely derive a perspectival representation; it explicitly claims the phenomenology. Naming it strengthens rather than weakens the article's response, because the article's point is that no current empirical criterion separates deriving phenomenal space from deriving a representation that reports it — and PCM is precisely a model making the stronger claim without an instrument that would settle it. The edit names the claimant and its claim without conceding it.

### Medium Issues Found

- **Dennett / heterophenomenology gloss — examined, left.** §"The Phenomenal Residue" attributes to "a heterophenomenologist (Dennett)" the view that functional indistinguishability is "evidence for the reports-are-all-there-is position". Heterophenomenology is by Dennett's own account a *method* claimed to be metaphysically neutral, so the gloss is the critic's reading rather than Dennett's self-description. The article frames it as a persona's reading of the situation, not as Dennett's stated thesis, and four prior reviews audited this passage as an honest Mode Three boundary-marking. Re-flagging would be oscillation. Recorded as examined-and-cleared so a future review need not re-derive it.
- **Dorsal/ventral stream claim (Goodale & Milner) has no citation in this article** — but it now carries the `[[capability-division-in-vision]]` wikilink installed by commit `caa06a8168`, and that article cites Goodale, Milner, Jakobson & Carey (1991) and Goodale & Milner (1992) for exactly this claim. Sourcing is discharged by the link at zero word cost. No edit.

### Diff Audit — commit `caa06a8168` (2026-09-19, crosslink integration; unreviewed prose)

Two sentences were touched. Both crosslink claims verified true of their targets, not merely topically adjacent:

- `[[capability-division-in-vision|dorsal visual stream]]` — target has 6 `dorsal` hits and states at L44/L64 that "the dorsal pathway ('where/how') computes spatial relationships and motor parameters" and "handles visuomotor coordination". The host sentence says the dorsal stream "processes spatial relationships and guides action". **Holds.**
- `[[auditory-consciousness-and-the-interface|auditory localisation]]` — target states at L53 "We do localise sound sources, but localisation is computed from interaural timing and level differences", and at L55 that this output is bound into "the single cross-modal arena described by the 3D world representation problem". Reciprocal: the target's Further Reading (L96) links back here naming exactly this relation. **Holds, and is reciprocal.**

No other body bytes changed in that commit. The `ai_modified` bump it produced was, as the 2026-06-23 review predicted, cosmetic — but the *pre-existing* citation defects it re-exposed the article for were real, so the re-qualification was productive this time.

### Citation Web-Verify Ledger (publisher of record)

- O'Keefe, J. & Nadel, L. (1978), *The Hippocampus as a Cognitive Map* — **state: real-correct.** Crossref surfaces the 1979 *Psychological Medicine* book-review record giving "Clarendon Press: Oxford. 1978", 570 pp. Clarendon Press is OUP's imprint; "Oxford University Press" is the standard citation form and is not a metadata error. No edit.
- Moser, E.I., Kropff, E. & Moser, M.-B. (2008), *Annual Review of Neuroscience* 31, 69–89 — **state: real-correct.** Crossref: DOI 10.1146/annurev.neuro.31.061307.090723, vol 31 issue 1, pp. 69–89, issued 2008-07-01, authors exactly as cited. Result-direction leg: the paper is a review of place/grid/head-direction coding; the article's use of it is faithful *except* for border cells, handled as Critical 1.
- Southgate, A. & Oquatre-six, C. (2026-03-09), The Capability Division Problem — **state: real-correct** (Map self-cite; the pseudonymous co-author is the expected in-house form and must not be stripped). URL path `/voids/capability-division-problem/` matches the file's actual home `obsidian/voids/capability-division-problem.md`. No edit.
- Solstad, T., Boccara, C.N., Kropff, E., Moser, M.-B. & Moser, E.I. (2008), *Science* 322(5909), 1865–1868 — **state: real-correct, newly added.** Verified twice independently: PubMed PMID 19095945 (Science 2008 Dec 19;322(5909):1865-8) and Crossref (DOI 10.1126/science.1166466, vol 322 issue 5909, pp. 1865–1868). Result-direction leg: abstract reports the positive existence of "an entorhinal cell type that fires when an animal is close to the borders of the proximal environment", named "border cells" — the article's claim is in the same direction, and its wording was tightened to match the abstract ("fire when the animal is close to the boundaries of its enclosure").
- Rudrauf, D., Bennequin, D., Granic, I., Landini, G., Friston, K. & Williford, K. (2017), *Journal of Theoretical Biology* 428, 106–131 — **state: real-correct, newly added.** Verified at PubMed PMID 28554611, DOI 10.1016/j.jtbi.2017.05.032, author list and page range exactly as cited. Friston's co-authorship is what makes "Friston-style" literally accurate rather than a loose label. **Cited-author-stance leg**: Rudrauf et al. are *not* dualists and PCM is offered as a functional-computational model of consciousness; the article cites them as the strongest instance of the position it is pressing against, not as support for the Map's reading, and the surrounding prose makes that direction explicit.

### Counterarguments Considered (bedrock; not re-flagged)

Eliminative materialist, MWI defender, quantum skeptic, empiricist, and the Madhyamaka framework-boundary contestation at §"The Perspective Problem" are unchanged framework-boundary disagreements, audited across all six prior reviews. No calibration slippage found: the article's conclusions still sit where the 2026-06-04 honesty-upgrade pass put them ("looks harder", three aspects explicitly *not* three independent confirmations, "net falsifiability genuinely modest").

## Optimistic Analysis Summary

### Strengths Preserved

- The 2026-06-04 calibration ladder (content-reports above architectural-organisational reports), the deflationary falsifiability partition, and the two-layer separation in §"Relation to Site Perspective" are byte-identical and were deliberately not touched.
- The article's distinctive value is that it argues *down* its own case where the case does not carry. That direction was preserved in every edit: the Rudrauf insertion names a rival that claims more than the article grants, rather than a friendly source.

### Enhancements Made

- Three inline citation anchors, one corrected sourcing attribution, one named exemplar for a previously bare literature claim, two appended References entries.

### Cross-links Added

- None. Link density is already high (54 wikilink forms, all resolving) and the budget was better spent on the citation apparatus.

## Length Check

3453 → 3570 words (+117) against 3000 soft / 4000 hard. Status `soft_warning` both before and after; 429 words of headroom remain.

Length-neutral mode nominally applies above the soft threshold. I did **not** offset the +117 with a trim, deliberately: the four passes since 2026-06-04 have marked the calibration prose as the load-bearing invariant, and the only plausible trim targets are inside it. Removing prose that prior reviews installed as a guard to satisfy a soft-threshold convention would regress the discipline for a length figure that did not change status. The addition is corrective (citation apparatus), not expansive, and the article is 429 words from any ceiling that forces a decision.

## Remaining Items

- **"Standing Agnostic Challenge" still has no home article and no wikilink** — now used across **17** non-review files. Carried forward from the 2026-06-04 and 2026-06-23 reviews. **New information this cycle**: a research note now exists at `obsidian/research/standing-agnostic-challenge-2026-06-24.md`, dated the day after the last review, so this is no longer a pure gap — it is **unconsumed research** and is eligible for `replenish-queue`'s highest-priority category. Not minted here: `topics/` has ~1 slot and this is concept-shaped; flagging it so the replenish pass can see it rather than manufacturing a task from a single-article review.

## Stability Notes

- **Do not read six clean reviews as a clean file.** This pass is the counter-example to its own series: five convergence-class reviews and two explicit no-ops certified an article whose entire citation apparatus was orphaned and one of whose empirical claims was sourced to a paper published before the finding existed. The prior reviews compared the sentences present; none asked which claims had nothing behind them. **When nominating this article as converged, name the lens you ran.**
- The 2026-06-04 / 2026-06-23 invariants stand and are reaffirmed: keep "looks harder" (not "is actually harder"); keep the three aspects framed as *not* three independent confirmations; keep the conditional-instrumentation framing on challenges (1) and (3); keep architectural-introspection reports below content-grade. A future review tempted to strengthen the falsifiability list is regressing the discipline.
- Functionalist (Mode Two → Mixed), Dennett (Mode Three), Madhyamaka (Mode Three) engagements unchanged and honest at their modes. No editor-vocabulary leakage in body prose (grep clean).
- The Rudrauf citation is **adversarial**, not supporting. A future editor must not re-purpose it as evidence for the Map's reading: PCM claims to account for spatial phenomenology on functional grounds, which is the position the article is pressing against.
- The `(O'Keefe & Nadel 1978; Moser et al. 2008)` anchor covers place, grid and head-direction cells only. **Border cells belong to Solstad et al. 2008 and to no earlier reference.** If that sentence is ever restructured, keep the two attributions separate.
