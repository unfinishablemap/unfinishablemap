---
ai_contribution: 100
ai_generated_date: 2026-05-27
ai_modified: 2026-05-27 21:52:13+00:00
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
title: Deep Review - Probability and Decision-Theory Objections to Many Worlds
topics: []
---

**Date**: 2026-05-27
**Article**: [Probability and Decision-Theory Objections to Many Worlds](/topics/probability-problem-in-many-worlds/)
**Previous review**: [2026-04-21](/reviews/deep-review-2026-04-21-probability-objections-many-worlds/) (5th review; prior: 2026-03-05, 2026-03-15, 2026-03-18, 2026-04-21)

## Web-Verification (Priority Remit)

Every load-bearing citation was checked against live literature this session. Prior "verified" marks and intra-corpus consistency were NOT trusted. Result: nine clean, one regressed factual error.

| Citation | Article form | Live-verified | Outcome |
|---|---|---|---|
| Sebens & Carroll 2018 | BJPS 69(1), 25-74 | BJPS 69(1), 25-74 (DOI 10.1093/bjps/axw004) | CLEAN |
| Saunders 2021 | Proc. R. Soc. A 477, 20210600 | Proc. R. Soc. A 477(2255):20210600 | CLEAN |
| Short 2023 | Quantum 7, 971 | Quantum 7, 971 (2023-04-06) | CLEAN |
| Lewis 2007 | SHPMP 38, 1-14 | SHPMP 38, 1-14 | CLEAN |
| Baker 2007 | SHPMP 38, 153-169 | SHPMP 38, 153-169 | CLEAN |
| Deutsch 1999 | Proc. R. Soc. A 455, 3129-3137 | Proc. R. Soc. A 455(1988), 3129-3137 | CLEAN |
| Vaidman 1998 | Int. Stud. Phil. Sci. 12(3), 245-261 | 12(3), 245-261 (Tandfonline) | CLEAN |
| Zurek 2005 | Phys. Rev. A 71, 052105 | Phys. Rev. A 71, 052105 | CLEAN |
| Graham 1973 | DeWitt vol., Princeton UP (no pages) | confirmed (1973mwiq.conf..229G; starts p.229) | CLEAN (deferred precision resolved — see below) |
| **Wallace 2003** | **SHPMP 34, 87-105** | **SHPMP 34(3), 415-439** | **CRITICAL — wrong page range, regressed** |

## Pessimistic Analysis Summary

### Critical Issues Found
1. **Wallace (2003) page-range error (regressed factual error + corpus propagation).** Reference #12 listed "*Studies in History and Philosophy of Modern Physics*, 34, 87-105." The actual publication is **vol. 34, issue 3, pp. 415-439** (DOI 10.1016/S1355-2198(03)00036-4; full title "Everettian rationality: defending Deutsch's approach to probability in the Everett interpretation"). The page range 87-105 is wrong.
   - This is a **regression**: the 2026-03-05 deep review of this same article explicitly recorded "Wallace (2003) wrong page numbers: Listed as pp. 87-105, actual pages are 415-439. Resolution: Corrected." The error reappeared (the corrected form did not persist in this file), and survived the 2026-03-15, 2026-03-18, and 2026-04-21 reviews — a uniformly-propagated wrong citation that looked consistent and so escaped intra-corpus cross-check. Only live-literature verification caught it.
   - **Resolution**: Corrected to "34(3), 415-439" with full title here.
   - **Propagation fixed** (grep'd corpus incl. research/ and archive/): same wrong "34, 87-105" found and fixed in [topics/probability-problem-in-many-worlds.md](/topics/probability-problem-in-many-worlds/) (#16), [research/probability-decision-theory-against-many-worlds-2026-03-04.md](/research/probability-decision-theory-against-many-worlds-2026-03-04/), and `archive/topics/decision-theory-cannot-save-many-worlds.md` (#10). Two files ([arguments/many-worlds-argument.md](/arguments/many-worlds-argument/) and one other) already carried the correct 415-439 form; standardized all to 415-439 to match.

### Medium Issues Found
None. No new style, attribution, or argument defects. The two "This is not X. It is Y." clichés removed in the 2026-04-21 review have not recurred.

### Counterarguments Considered
All six adversarial personas re-engaged. No new bedrock issues. The MWI defender's standing dissatisfaction with the structural "every outcome occurs → no space of unrealised possibilities" thesis remains a framework-boundary disagreement per the No Many Worlds tenet — not re-flagged (see Stability Notes).

### Unsupported Claims
None. The calibration line — "the Born rule has not yet been extracted from MWI's resources without smuggling it in" / Short 2023 "confirms the problem remains open, with no consensus that any strategy succeeds" — correctly tracks the corpus position ("sustained in-framework objections, dispute remains live"). The Deutsch-Wallace program is NOT overstated as "refuted." Calibration honest.

## Attribution Accuracy Check
- Misattribution: clear. Wallace authored the incoherence/quantitative distinction (2003); Baker and Price independently identified the circularity; Graham authored the branch-counting result; Saunders (2021) "proposed a state-dependent rule" (not "proved," not "conceded" — the earlier interpretive overstatement corrected in a prior review remains corrected).
- Qualifier preservation: "has not yet been extracted" (historical) and the structural "not the kind of difficulty incremental progress resolves" (logical) preserved as distinct claims. "Rationally permissible weighting among several" intact.
- Source/Map separation: "Relation to Site Perspective" cleanly partitions Map commitments (No Many Worlds, Minimal Quantum Interaction, Occam's Razor Has Limits) from body source-exposition.
- Self-contradiction: none.

## Reasoning-Mode Classification (editor-internal; not in article prose)
- Wallace (circularity defence): **Mode One** — in-framework; the reply argues structural smallness requires a norm and the physically relevant norm is the Born-rule norm (Baker presses this on Everettian terms).
- Sebens & Carroll (epistemic separability): **Mode One** — argues the symmetry principle itself encodes amplitude information (internal-to-the-program).
- Zurek (envariance): **Mode One** — identifying "swaps"/"environment" presupposes the decoherence framework (in-framework circularity).
- Kent / Lewis (decision theory): **Mode One** — Lewis shows formally that alternative weightings satisfy equally defensible rationality constraints.
- Structural "every outcome occurs" thesis (Relation to Site Perspective): **Mode Three** — framework-boundary; rests on the indexical / No Many Worlds tenet commitment, honestly declared as the Map's position.
- No boundary-substitution detected; no editor-vocabulary label leakage in prose.

## Optimistic Analysis Summary

### Strengths Preserved
- Four-objection taxonomy with clean H2 structure.
- Numbered circularity cycle (Born rule → decoherence → branches → probability → Born rule).
- Albert's "fatness" metaphor presented vividly without distortion.
- "Convergence of Strategies—and Their Common Difficulty" meta-synthesis.
- Three-tenet connection; appropriate concept-page scope (depth deferred to companion topic page).

### Enhancements Made
- None beyond the citation correction. This is a converged article; no expansion warranted.

### Cross-links Added
None. All body cross-links verified to resolve to live files; reciprocity confirmed (companion topic page and many-worlds concept page link back). Tenet anchors (`^no-many-worlds`, `^minimal-quantum-interaction`, `^occams-limits`) verified present in tenets.md.

## Word Count
- Before: 1894 words
- After: 1894 words (citation correction is net-neutral; 76% of the 2500 concept soft threshold — no length action)

## Remaining Items
- **Graham (1973) deferred-precision item RESOLVED.** The 2026-04-21 review deferred "Graham (1973) attribution precision (requires source verification against the DeWitt-Graham volume)." Verified this session: the paper is real (NASA/ADS 1973mwiq.conf..229G), correctly attributed to Neill Graham in *The Many-Worlds Interpretation of Quantum Mechanics* (eds. DeWitt & Graham, Princeton UP, 1973), starting p. 229. The citation as written (no page numbers) is accurate, not a fabrication. Adding the start page is optional polish, not a defect; deferral closed.
- None else.

## Stability Notes
- 5th review. The article is mature and stable; the only substantive change this session was the regressed Wallace page-range fix (a factual error, not a philosophical shift).
- **Citation-regression lesson**: a wrong citation that has propagated uniformly across the corpus passes intra-corpus consistency checks and can survive multiple reviews (this one survived four after being "corrected" once). Live-literature web-verification is the only reliable catch. Future reviews of physics-heavy converged articles must web-verify rather than trust prior "verified" marks.
- MWI defenders will always find the structural "no genuine probability" framing unsatisfying — bedrock framework-boundary disagreement per No Many Worlds. Not to be re-flagged.
- The "collapse posits probability" framing and the concept-page scope (do NOT significantly expand; depth belongs in [probability-problem-in-many-worlds](/topics/probability-problem-in-many-worlds/)) are deliberate editorial choices. Not to be re-flagged.
- If the next review finds only the (now-clean) citations and no new defects, that is a SUCCESS. Do not invent issues.