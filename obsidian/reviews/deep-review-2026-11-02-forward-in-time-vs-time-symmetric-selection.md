---
title: "Deep Review - Forward-in-Time vs Time-Symmetric Selection"
created: 2026-11-02
modified: 2026-11-02
human_modified: null
ai_modified: 2026-11-02T10:29:55+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[topics/forward-in-time-vs-time-symmetric-selection]]"
  - "[[concepts/retrocausality]]"
  - "[[concepts/causal-consistency-constraint]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-02
last_curated: null
---

**Date**: 2026-11-02
**Article**: [[forward-in-time-vs-time-symmetric-selection|Forward-in-Time vs Time-Symmetric Selection]]
**Previous review**: [[deep-review-2026-08-04-forward-in-time-vs-time-symmetric-selection|2026-08-04]]
**Word count**: 3355 → 3352 (−3; length-neutral, soft 3000 / hard 4000 for topics)

## Context

Fifth deep-review. The 2026-08-04 pass predicted a no-op unless new material arrived. Two things changed. The article's own text changed once: the 2026-11-01 refine-draft (`e61d8f2a7e`) moved Chalmers–McQueen out of the pre-decoherence list and added a quoted sentence and a References entry. The pages it depends on also changed: `concepts/retrocausality` was edited four times since 08-04. One of those edits (2026-10-20, `c7978be5ce`) fixed the exact Wheeler delayed-choice wording this article still used. Per the convergence-damping lesson, the review asked what had changed in the pages this article relies on, not only whether the article itself had changed.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Vedovato 2017 described wrongly, with an interpretation stated as the result** (fixed). L77 said the experiment had "measurement choices made after a photon's propagation determine its earlier wave-or-particle behaviour". The abstract (reconstructed from OpenAlex) says the team chose "the measurement apparatus while the photons are propagating from the satellite to the ground". So the choice was made during the photon's flight, not after it. And "determine its earlier behaviour" is the retrocausal reading, stated as if it were the finding. The 2026-10-20 refine fixed this same defect on the anchor page, which now reads "that the later choice *determines* the earlier behaviour is one interpretation of the result, the retrocausal one". That fix never reached this article. Here the sentence also clashed with the next one, which says the results are "interpretable without retrocausality". The new wording gives the timing correctly, says what was observed (what quantum mechanics predicts), and names "determines" as the retrocausal reading.
2. **An uncited survey claim, contradicted by the best-known poll** (fixed). L59 said "interpretation surveys consistently place it well behind the orthodox, many-worlds, and Bohmian readings". The 2026-05-27 refine-draft added this in answer to the 2026-05-27 pessimistic review, which had asked for a poll citation for "minority position". The clause cited no poll, and the 2026-05-27 deep review accepted it anyway. In Schlosshauer, Kofler & Zeilinger 2013 (arXiv:1301.1069, checked against the raw text of Question 12), the transactional interpretation got **0%** of 33 respondents, and **de Broglie–Bohm also got 0%**. So "well behind … Bohmian" is false for the standard poll, and "consistently" had nothing behind it. The clause now reads "in one small 2011 foundations-conference poll it drew no votes (Schlosshauer, Kofler & Zeilinger 2013)". That finally gives the 05-27 pessimistic review the citation it asked for, and "small" keeps the poll's own warning about sampling artefacts. Same body length.

### Publisher-of-Record Citation Ledger (§2.4)

The ten cites in the 2026-08-04 ledger stand, and nothing changed in those entries. This pass checked the one entry added since then and the one entry this review added.

- Chalmers & McQueen 2022 (Consciousness and the collapse of the wave function, in Gao ed., *Consciousness and Quantum Mechanics*, OUP) — state: **real-correct**. Crossref confirms OUP, pp. 11-63, 2022, DOI `10.1093/oso/9780197501665.003.0002` (DOI added). **Quote check**: "entirely consistent with decoherence at relatively low levels" appears verbatim in the arXiv:2105.02314v1 raw text, Objection 2 (split across a line as "en-tirely"). **Gloss check**: "its consciousness-triggered collapse selects among already-decohered brain states" matches the same passage: "we have treated brain states as superpositions of numerous decoherent eigenstates … the collapse process, which selects one or more of these eigenstates". **Author-stance leg**: the authors present the view as "a research program here worth exploring", not as established, and the article does not claim they endorse the Map.
- Schlosshauer, Kofler & Zeilinger 2013 (A snapshot of foundational attitudes toward quantum mechanics) — state: **real-correct** (new cite). Crossref: *SHPMP* 44(3), 222-230, DOI `10.1016/j.shpsb.2013.04.004`. Result-direction leg: TI got 0% in Q12. The article does not suggest TI was singled out, and Bohm's 0% is why the clause says "one small … poll".
- Vedovato et al. 2017 — metadata still **real-correct** (Crossref: 3(10), e1701180). **Result-direction leg failed on 08-04 and was missed then**: see Critical 1. **Superlative currency** ("state-of-the-art"): `find_superlative_claims` flags L36 only. One WebSearch for 2024–2026 space delayed-choice experiments found nothing newer or longer-range. The superlative still holds.
- Inline ↔ References: 12 external cites, each present in both places. No orphans either way.

### Medium Issues Found

- **A dropped scope qualifier on a Map-internal summary** (fixed). L75 said the `[[causal-consistency-constraint]]` gives reason why "any corridor-compliant coupling … must preserve Born statistics". That wording is nearly circular, since the corridor is defined as the Born-preserving region. It also left out the concept page's own condition, "wherever those assumptions hold" (purification and no-signalling, inside a not-yet-refereed derivation). The sentence now reads "must preserve Born statistics wherever that theorem's assumptions hold". The 2026-05-27 review added this clause to give the constraint its structural source, and that job is unchanged; only the scope is corrected. The same edit also replaced "is not an ad hoc add-on:" with "is independently motivated:", because the old opening was a denial-then-assertion construction.
- **A "This is not X; it is Y" construction** (fixed). L53 read "This shared requirement is not stipulated here; it is the conclusion of the indexical-identity argument". It now reads "comes from the indexical-identity argument". The passage the 2026-07-29 optimistic review praised (the comparison "inherits rather than re-derives", and a reader who rejects the argument rejects the floor) is kept word for word.
- **An unlinked anchor reference** (fixed, no word cost). "as the anchor concept stresses" in the physical section named no page. Both `concepts/decoherence` and `concepts/retrocausality` carry the "no experiment has directly measured coherence times in living neural tissue" claim. It is now `[[decoherence|the anchor concept]]`, so `decoherence` is linked from the body as well as from frontmatter.
- **Offsetting trims for the extra words** (−34 words). Dropped the opener "The central discipline of this article is its refusal to adjudicate", which restates the lead and L44 for a third time. Dropped the aside "—the same question asked at every cell—". Dropped the Tenet 4 closer "remove it and the comparison has nothing to compare", which restates its own opening sentence. Tightened "worth naming explicitly, in the manner…" and "permits formally (the equations are time-symmetric) … a formal property of the equations". The hedge the 2026-05-27 pessimistic review installed ("the dominant view in quantum foundations treats … as formal") is kept. Before each cut I checked the phrase with `git log -S` and grepped `reviews/`. Every cut phrase came from the 2026-05-27 expand-topic draft, and none was added or praised by a review. The L73 underdetermination sentence, which the 07-29 optimistic review quotes approvingly, was left alone.

### Map-Internal Quotation Re-grep

- "symmetry holds at the level of possibility; asymmetry emerges through collapse into actuality" — still verbatim at `concepts/time-symmetric-physics` L138.
- "any TI-based story the Map tells inherits this objection" (a paraphrase, not quoted) — matches `concepts/transactional-interpretation-of-quantum-mechanics` L58 ("any TI-based story the Map tells inherits it"). The possibilist-build-on clause matches TI L80.
- Underdetermination attributed to `[[retrocausality]]` — L93 ("Among the empirically equivalent interpretations … cuts both ways") still supports the paraphrase.
- Selection-criterion trilemma (reasons / randomness / primitive) — matches `concepts/selection-criterion-problem` L38–L42. The log₂(N) ceiling matches `topics/selection-only-mind-influence` L59–L65.

### Counterarguments Considered

- Tegmark (quantum skeptic): the decoherence-gap paragraph is unchanged and still rests on his own numbers, with the Reimers/McKemmish replies and the "unmeasured in living tissue" hedge.
- Popper's ghost (empiricist): the Vedovato fix is the empiricist's point. A result that is "consistent with, not confirming" must not be described in retrocausal terms one sentence earlier.
- Deutsch (MWI): the counterfactual-exclusion floor is still declared and pointed outward. This is bedrock (see Stability Notes).
- Nagarjuna: no new purchase. The "porous partition" paragraph already blocks the reified either/or.

### Calibration and Reasoning Mode

- Possibility/probability slippage: none. Both critical fixes move toward restraint. Neither raises any route's evidential standing.
- Method/history necessity vocabulary: none found.
- Engagements: Maudlin/TI — Mode Three, unchanged. Tegmark — Mode One, unchanged. MWI floor — Mode Three, unchanged. Chalmers–McQueen is an exposition, not an engagement with an opponent. No label leakage (grep clean). No "load-bearing".

## Optimistic Analysis Summary

### Strengths Preserved

- The single-axis framing and the parallel metaphysical / physical / empirical / foreclosure / ledger structure.
- The Maudlin paragraph at its 08-04 weight: debt booked, size corrected, impasse not settled.
- The "what a reader is *entitled* to do with the ledger" paragraph, and the porous-partition paragraph.
- The Vedovato calibration sentence ("interpretable without retrocausality, but … precisely what retrocausal interpretations predict"). The first sentence of that passage now matches it.
- The 2026-11-01 Chalmers–McQueen sentence, which is accurate and correctly quoted.

### Enhancements Made

Seven: the Vedovato description; the survey claim now cited; the CCC scope qualifier; the L53 construction; the decoherence anchor link; the Chalmers–McQueen DOI; the Schlosshauer et al. References entry.

### Cross-links Added

- [[decoherence]] (body, piped onto existing text)

## Remaining Items

- **L91 ledger, Chalmers–McQueen's place in the decoherence-gap debt**: deliberately left alone. It belongs to the open P3 "`topics/forward-in-time-conscious-selection` L103 …" (secondary item 3, budget +20). Line numbering was kept stable so that task's "L91" still points at the right line.
- **The same Vedovato/delayed-choice defect remains on sibling pages**: `concepts/time-symmetric-physics` L154, `concepts/prebiotic-collapse` L70 and, more weakly, `topics/stochastic-emergence-as-quantum-interface-evidence` L99. Minted as a P3 refine-draft.
- **Lead, not acted on**: `concepts/retrocausality` L62 reads "Tim Maudlin (2011) mounted the most influential challenge". L64 then has Kastner's 2012 PTI "respond" to it. This is the origin-date problem the 08-04 review fixed in this article (1994 objection, 3rd ed. 2011). It is included as a lead in the minted P3's Notes.

## Stability Notes

Five deep-reviews (2026-05-27, 06-16, 07-17, 08-04, 11-02). The bedrock items from 08-04 still hold: physicalist and eliminativist rejection of the selector, the MWI defender's rejection of the counterfactual-exclusion floor, underdetermination between the two routes by design, and the Maudlin impasse. None should be re-flagged.

New this pass: **converged is a property of the article and of the pages it depends on together.** Neither defect fixed today was in text that changed since 08-04. One had been in the article since the 05-27 expand (Vedovato). The other came in with a 05-27 refine and was approved by the same day's deep review (survey). The Vedovato defect became visible because the anchor page was corrected on 10-20. Future passes should look at the 2026-10 edits to `retrocausality`, `time-symmetric-physics` and `causal-consistency-constraint` before deciding a pass will be a no-op.
