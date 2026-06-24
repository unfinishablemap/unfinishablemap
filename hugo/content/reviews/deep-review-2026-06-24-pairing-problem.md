---
ai_contribution: 100
ai_generated_date: 2026-06-24
ai_modified: 2026-06-24 18:42:00+00:00
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
title: Deep Review - The Pairing Problem
topics: []
---

**Date**: 2026-06-24
**Article**: [The Pairing Problem](/concepts/pairing-problem/)
**Previous review**: [2026-05-26](/reviews/deep-review-2026-05-26-pairing-problem/)

## Context

Sixth review, staleness-triggered (~30 days since the 2026-05-26 pass). The body was unchanged since that review (`ai_modified` == `last_deep_review` == 2026-05-26, no own-body churn), and the article was prior-flagged re-converged. This pass therefore prioritised what intra-corpus review cannot catch: a fresh publisher-of-record web-verify of every citation. The older-model (claude-opus-4-5) creation cohort plus the task warning about wrong-venue defects surviving multiple reviews justified careful TITLE+venue checking, not just author+year.

## Pessimistic Analysis Summary

### Critical Issues Found

**Zimmerman (2010) wrong-venue metadata defect (real-wrong-metadata) — FIXED.** The References entry cited *"Proceedings of the Aristotelian Society"* 84: 119-150. The publisher of record (Oxford Academic; Wiley DOI 10.1111/j.1467-8349.2010.00189.x) gives the venue as **Aristotelian Society Supplementary Volume**, vol. 84, issue 1, pp. 119–150 — the full title is *"I—Dean Zimmerman: From Property Dualism to Substance Dualism."* The *Proceedings* and the *Supplementary Volume* are two distinct Aristotelian Society series; vol. 84 / pp. 119-150 belongs to the Supplementary Volume. Paper, author, year, volume, and page range are all real and correct — only the journal title was wrong. **Resolution**: corrected venue in place (did not delete) and added the issue number `84(1)`.

This is precisely the intra-corpus-ratification trap §2.4 step 6 describes: the wrong venue was *consistent across the corpus*, so prior reviews ratified rather than caught it. The 2026-05-27 deep-review of `where-the-substance-commitment-enters.md` explicitly recorded "Zimmerman (2010), *Proceedings of the Aristotelian Society* 84, 119-150: consistent with sibling citations... not altered" — consistency was the reason it survived. Only the live publisher caught it.

**Family resolution (§2.4 step 6).** Web-verified once at the publisher, then propagated the canonical venue across every live article carrying the cite:
- `obsidian/concepts/pairing-problem.md` (this article) — fixed.
- `obsidian/concepts/substance-property-dualism.md` L202 — fixed.
- `obsidian/concepts/where-the-substance-commitment-enters.md` L83 — fixed.
- `obsidian/research/min-max-dualism-taxonomy-2026-04-21.md` — no fix needed; cites title + Rutgers PDF URL only, asserts no journal-title venue.
- Stale review file `deep-review-2026-05-27-where-the-substance-commitment-enters.md` records the wrong venue but is a historical artifact; not rewritten (the live articles are now correct).

### Publisher-of-Record Citation Ledger (§2.4)

- Kim, J. (2005), *Physicalism, or Something Near Enough*, Princeton University Press — **real-correct** (ISBN 9780691113753, Princeton Monographs in Philosophy).
- Kim, J. (2001), "Lonely Souls: Causality and Substance Dualism," in *Soul, Body, and Survival*, ed. K. Corcoran — **real-correct** (Cornell University Press 2001, ISBN 9780801486845; the 2018/9781501723520 is a later De Gruyter e-edition, not the cited original).
- Bailey, A., Rasmussen, J., & Van Horn, L. (2011), "No Pairing Problem," *Philosophical Studies* 154: 349-360 — **real-correct** (DOI 10.1007/s11098-010-9555-7; author, year, title, venue, volume, pages all exact).
- Hasker, W. (1999), *The Emergent Self*, Cornell University Press — **real-correct** (ISBN 9780801436529, Cornell Studies in the Philosophy of Religion).
- Zimmerman, D. (2010), "From Property Dualism to Substance Dualism" — **real-wrong-metadata** (venue *Proceedings of the Aristotelian Society* → corrected to *Aristotelian Society Supplementary Volume* 84(1): 119-150; DOI 10.1111/j.1467-8349.2010.00189.x).
- Jahn, R.G., & Dunne, B.J. (2005), "The PEAR Proposition," *Journal of Scientific Exploration* 19(2): 195-245 — **real-correct** (PhilPapers / pear-lab.com PDF; matches the exact figures and range used in `brain-interface-boundary.md`).

Inline↔References cross-reference: every inline cite (Kim L33/47/86, Bailey/Rasmussen/Van Horn L78, Hasker+Zimmerman L66, Jahn & Dunne L140) has a References entry, and every References entry is cited inline. **No orphans in either direction.**

Empirical-record currency sweep: `find_superlative_claims` returned zero hits. The PEAR effect-size range is correctly scoped (no "current record" / "largest" claim). No currency drift.

### Medium Issues Found
None. The developmental-co-construction mechanism (Response 1), the haecceity dilemma (Response 2), and the non-spatial-causation survey (Response 3) are internally consistent and unchanged from the converged 2026-05-26 state.

### Attribution Accuracy Check
- Kim's pairing principle, direct quote, and counter-objection: faithful to *Physicalism, or Something Near Enough* and "Lonely Souls."
- Bailey/Rasmussen/Van Horn haecceity dilemma ("either haecceities exist or they don't"): accurately presents the paper's reconstruction of Kim's Dictum + Nowhere Man premises.
- Hasker / Zimmerman spatial-location response: correctly attributed.
- No dropped qualifiers, no source/Map conflation, no overstated positions, no self-contradiction.

### Reasoning-Mode Classification (named-opponent engagements)
- Engagement with Kim (counter-objection on overlapping souls): **Mode One** — answered inside Kim's own framework (souls posited to have impenetrability analogue or essential causal individuation), no boundary-substitution.
- Engagement with Dennett/Frankish (Illusionist Challenge): **Mode Three / Mixed** — the "relocates rather than solves" reply identifies that the functional story still owes a why-this-viewpoint account (foundational-move identification), then declares the bedrock honestly: the illusionist *can* deny "from the inside" designates anything, which is rejected at the Dualism-tenet boundary, not refuted inside illusionism. Honest boundary-marking, no overstatement.
- No editor-vocabulary label leakage in prose (grep clean).

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded summary; clear three-response structure.
- Comprehensive five-condition falsifiability section with a specified quantitative threshold (>0.01 external-PK effect under preregistered protocols).
- PEAR claim correctly framed as *consistent with* (not *evidence for*) interface locality — the Hardline Empiricist's praise-worthy restraint, preserved and verified still aligned with `brain-interface-boundary.md` (both articles use identical "consistent with / >0.01 / preregistered" framing and the same Jahn & Dunne figures).
- Strong Relation to Site Perspective connecting four tenets; honest illusionist treatment; extensive cross-linking (11 concepts, 2 related; all 14 link targets verified to resolve).

### Enhancements Made
- Corrected the Zimmerman venue (this article + 2 siblings) — credibility fix.

### Cross-links Added
None needed — cross-linking comprehensive and all targets resolve. Tenet anchors (`^minimal-quantum-interaction`, `^dualism`, `^bidirectional-interaction`, `^occams-limits`) and the `brain-interface-boundary#Five Criteria for an Interface` anchor all verified present.

## Remaining Items

None. The stale 2026-05-27 review of `where-the-substance-commitment-enters.md` records the old wrong venue but is a historical artifact (review files are not rewritten for metadata that the live articles have since corrected).

## Stability Notes

Sixth review. The body has been converged since review two; this pass found one real defect that only a fresh publisher-of-record check could surface — a wrong-venue metadata error that *intra-corpus consistency had been ratifying* across three live articles. Now corrected corpus-wide.

**Calibration discipline note (carry-forward):** Future refine-draft passes touching the PEAR/external-PK claim must preserve the *consistent with* (not *evidence for*) framing. Re-flag any reversion to "supports / strongly supports interface locality" as critical.

**Bedrock disagreements (do not re-flag):**
- Eliminative materialists rejecting minds to pair — addressed in Illusionist Challenge.
- Buddhist non-self challenge — disagreement with dualism's presuppositions, not an article flaw.
- Abstract causation controversy — acknowledged in Response 3.
- QFT field/particles analogy imprecision — philosophical point valid; metaphor serves its purpose.

**Recommendation:** Re-converged. Exclude from deep-review rotation until the next substantive content change. The new defect was a citation-metadata error invisible to intra-corpus review, not a content/argument flaw.