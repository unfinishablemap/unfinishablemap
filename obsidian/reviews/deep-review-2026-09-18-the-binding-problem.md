---
title: "Deep Review - Varieties of the Binding Problem"
created: 2026-09-18
modified: 2026-09-18
human_modified:
ai_modified: 2026-09-18T02:05:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-18
last_curated:
---

**Date**: 2026-09-18
**Article**: [[the-binding-problem|Varieties of the Binding Problem]] (topics/ variant)
**Previous review**: [[deep-review-2026-07-18-the-binding-problem|2026-07-18]]

## Verdict: NOT a no-op — the prior stability note was falsified on its own primary lens

22nd review pass. The 2026-07-18 review closed with "Article is deeply converged; future
cosmetic cross-link bumps should not re-trigger a fresh pass." Treated per the driver's
standing instruction as **a marker of which lenses were not run, not as certification** — and
the marker was accurate. The single lens the prior ledger claimed to have discharged (§2.4
publisher-of-record) is the one that had not been run on the article's actual text.

### Lenses actually run this pass

1. Publisher-of-record citation web-verify, with **primary sources read, not metadata re-checked**
   (Revonsuo 1999 full PDF; Bayne & Chalmers 2003 full text; Baars et al. 2013 full text).
2. Cited-author-stance leg (§2.4 step 8).
3. Source/Map separation (§2.5).
4. Inline ↔ References orphan cross-reference (§2.4 step 5), measured rather than asserted.
5. Length gate, measured with apparatus share decomposed.
6. Corpus family-resolution sweep for the BP1/BP2 attribution.

Lenses **not** run: reasoning-mode re-classification of the MWI / deflationist / identity-theorist
engagements (verified stable and correctly Mode Three / Mode One by the 06-26 pass; no prose
change since), and the falsifier section (unchanged).

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Source/Map conflation at the article's foundational paragraph — FIXED.**

§The Foundational Distinction read:

> **BP2 (Phenomenal Binding)** asks why coordinated processing produces unified experience.
> … This is the [[hard-problem-of-consciousness]] applied to unity.

directly under the citation "(Revonsuo 1999)". Revonsuo's own BP2 is a *how*-question about
mechanisms — quoted verbatim from his p. 176: *"How do the brain mechanisms actually construct
the phenomenal object?"* — and he glosses consciousness-related binding as *"a problem of
finding the neural mechanisms which map the unified contents in phenomenal consciousness to
corresponding neural entites in the brain."* Grep of the full paper returns **zero** occurrences
of "hard problem", "explanatory gap", or "Chalmers". Revonsuo is a biological naturalist
(*Inner Presence*, 2006) who expects the question to yield to neuroscience.

The article therefore silently converted a tractable mechanism-identification question into
the hard problem and cited its source as authority for the escalation. This is the load-bearing
move of the whole article — the "BP2 gap" refrain recurs in all five varieties — so it is
critical rather than cosmetic. **Fixed**: BP2 now states Revonsuo's wording and his own
empirical intent, names his naturalism, and marks the escalation explicitly as the Map's
("That escalation to the hard problem is the Map's own"). Source exposition and Map
interpretation are now separated at the point of claim.

Note this defect survived 21 prior reviews *because* intra-corpus consistency ratified it: three
live articles carry the same "(Revonsuo 1999)" → BP1/BP2 cite and none had read the paper.

### Medium Issues Found

**2. Bayne & Chalmers over-read — FIXED.** §Cognitive Binding claimed their "conjoint
phenomenology" gives a character *"exceeding the sum of"* the parts. Their text (verified at
consc.net/papers/unity.html) defines it by **subsumption**: *"a phenomenology of having both
states at once that subsumes the phenomenology of the individual states"*; the conjoint state
*"carries with it"* the parts and involves *"at least the conjunction A&B"*. The string "exceed"
occurs 0 times in the paper against 74 occurrences of "subsume". The emergentist excess reading
is the Map's, and the companion [[binding-problem]] already states it correctly (subsumption
attributed to B&C, excess asserted separately as the Map's). Fixed by matching the companion's
split. The *"extends from perception to thought"* half **verified correct** — B&C explicitly
include *"perceptual, bodily, emotional, and cognitive experiences"*.

**3. Orphan References — FIXED.** The prior two reviews certified "Inline ↔ References
cross-reference intact, no orphans." Measured: only **2 of 9** entries (Revonsuo, Treisman &
Gelade) carried an inline author-year anchor. Five entries were named by content with no
attribution at all. Inline anchors added for Baars et al. 2013, Stein and Stanford 2008,
Mudrik et al. 2014, James 1890, Jerath and Beveridge 2019, plus a year on Nagel (1971) and
Bayne and Chalmers (2003). All 10 References entries now have an inline anchor.

### Checked and found sound — no defect (recorded to stop future re-litigation)

- **"~100ms" global-workspace claim.** I suspected this against Dehaene's ~270–300ms ignition
  figure. Wrong suspicion — the claim is cited to Baars, not Dehaene, and is faithful to the
  cited paper, which says *"A bound conscious gestalt may emerge from anywhere in the cerebrum,
  and spread globally to all other regions for ∼100 ms"*, *"the ∼100 ms conscious integration
  time of different sensory inputs"*, and *"conscious sensory events are integrated within 100 ms
  periods"*. The article's "cortical-thalamic workspace" also matches Baars's "cortico-thalamic
  (C-T) system". No change made.
- **Nagel split-brain passage.** The 07-18 review recorded a verbatim quote here as
  "verbatim-preserved and stable". That quote no longer exists — commit `7385ba8b35` (08-04)
  correctly replaced it with a paraphrase because the condensed quote had dropped Nagel's
  qualifier "in the specially contrived laboratory situations" without an ellipsis. The current
  paraphrase preserves the scope qualifier and is faithful. Resolved before this pass; recorded
  so the stale "verbatim quote" note in the 07-18 ledger is not trusted again.

### Per-cite ledger (publisher of record)

- Revonsuo, A. 1999, *Binding and the phenomenal unity of consciousness*, Consciousness and
  Cognition 8(2), 173-185 — **state: real-correct** (DOI 10.1006/ccog.1999.0384, PMID 10448000;
  full PDF read). ⚠️ The 06-26 and 07-18 ledgers both certified this entry as "**Revonsuo
  2006**", which is a different work (*Inner Presence*, MIT Press) and is not in this article's
  References. Those ledger lines certified a citation the article does not carry; the 1999 entry
  had never actually been verified until this pass.
- Smythies, J. R. 1994, *Requiem for the Identity Theory*, Inquiry 37(3), 311-329 — **state:
  real-correct, newly added.** See enhancement below.
- Treisman, A. & Gelade, G. 1980, Cognitive Psychology 12, 97-136 — real-correct.
- Bayne, T. & Chalmers, D. 2003, in Cleeremans (Ed.) *The Unity of Consciousness*, OUP —
  real-correct (full text read); article's *use* corrected, see Issue 2.
- Nagel, T. 1971, Synthese 22, 396-413 — real-correct.
- Baars, B. J., Franklin, S. & Ramsøy, T. Z. 2013, Frontiers in Psychology 4, 200 —
  real-correct; supporting empirical claim verified in the full text (see above).
- Mudrik, L., Faivre, N. & Koch, C. 2014, TiCS 18(9), 488-496 — real-correct.
- Stein, B. E. & Stanford, T. R. 2008, Nat Rev Neurosci 9(4), 255-266 — real-correct.
- Jerath, R. & Beveridge, C. 2019, Front Integr Neurosci 13, 2 — real-correct.
- James, W. 1890, *The Principles of Psychology* — real-correct.

Currency sweep: `find_superlative_claims` returns 0. No superlative or record claims. No
result-direction defects found — no cite in this article carries a quantitative comparative.

## Optimistic Analysis Summary

### Enhancement: the distinction's real provenance is better than the one the article had

Revonsuo does not claim BP1/BP2 as his own. He writes: *"As far as I can tell, there is only one
author in the literature, namely, John R. Smythies, who clearly distinguishes these two types of
binding"*, and quotes him coining the labels (Smythies 1994b, p. 321). **"Smythies" appeared in
zero files across the entire corpus** while the distinction is used in nine live articles.

This is a genuine strengthening rather than a bare correction: Smythies coined BP1/BP2 in a paper
titled *Requiem for the Identity Theory* — an explicitly anti-identity-theory argument — while
its best-known transmitter is a biological naturalist who expects BP2 to reduce. The
distinction the Map leans on was born in a context congenial to the Map and popularised by
someone who is not. Added to §Foundational Distinction and to References.

### Strengths Preserved

- The BP1/BP2 scaffold applied across five varieties — the article's signature contribution.
- All calibration prose installed by the 2026-06-26 pessimistic pass left intact: the
  §Shared Structure underdetermination concession, the recalibration functional-reading
  downgrade, the quantum bias-only/entanglement-holism tension, and the deflationary-self
  paragraph. None re-collapsed; the doubled restatement trimmed from the IIT reply preserved
  both halves of the concession.
- The Mode Three MWI boundary-marking and Mode One identity-theorist reply, unchanged.

## Length

4089 → **3999** words (−90 net, after +104 of additions). Was **hard_warning**; now
soft_warning, one word under the ceiling. Note `length.py` gates on `>= hard`, so 4000 itself
trips — 3999 is the real target, not 4000.

**Measurement for future passes: this article's over-length is substantially apparatus.**
Further Reading + References + the video-embed boilerplate account for ~400 of the counted
words, so counted 4089 corresponded to roughly 3690 words of prose. Future passes should not
read a hard_warning here as prose bloat.

Trims taken, all genuine redundancy rather than budget-driven cuts:
- Two per-mechanism restatements in §What Neural Mechanisms Do Not Explain that the
  §Classical Approaches scorecard already makes verbatim ("availability is functional, not
  phenomenal").
- §Relation to Site Perspective Dualism bullet, which restated "across all five varieties" and
  the cross-modal starkness point immediately after both.
- Two of four duplicate "see [[binding-problem]]" pointers (two retained).
- Nine Further Reading entries **whose targets are still wikilinked in the body** — verified
  individually after removal, so the link graph is unchanged. The four body-unlinked targets
  ([[unity-of-consciousness]], [[mental-causation-and-downward-causation]],
  [[dualist-perception]], [[lucid-dreaming-and-dualist-rendering]]) were retained, as were the
  core companions. NB the first cut of this analysis wrongly counted frontmatter `concepts:` /
  `related_articles:` membership as body links, which would have stranded four targets;
  frontmatter membership is not a link.

## Remaining Items

- **Sibling loci for the BP2/hard-problem conflation.** Two further live articles cite
  "(Revonsuo 1999)" for the distinction: `topics/quantum-holism-and-phenomenal-unity` L52 and
  `concepts/binding-problem` L73. Both use more neutral framing than this article did
  ("Philosophers distinguish two versions", "distinguishes two challenges") and neither
  attaches the hard-problem reading directly to the cite, so neither is defective as this
  article was. But both would benefit from the Smythies provenance, and `concepts/binding-problem`
  is the companion that carries the mechanism argument. Task queued.
- "Unity as Primitive" remains the thinnest of the three theoretical positions (carried across
  all prior reviews). Still deferred under the length ceiling, which is now tighter.

## Stability Notes

Bedrock disagreements remain bedrock and must not be re-flagged as critical: the MWI defender's
indexical dissatisfaction (honest Mode Three boundary-marking), the Buddhist/Parfittian/Metzinger
deflationary-self standoff (Mode Three, given real space), the decoherence objection to quantum
binding (flagged in-article as open work), and eliminativist denial of phenomenal unity. No
possibility/probability slippage: entanglement binding is labelled "live hypothesis, not an
established result" and the MQI tenet passage says "candidate, not an established mechanism".

**Do not read the above as certification of convergence.** The 06-26 and 07-18 notes said the
article was converged and that the citation pass was discharged; both were wrong on the same
lens, and the error was a mis-transcribed year in a ledger that then justified skipping the
re-check for two cycles. The honest statement is narrower: *the reasoning-mode classifications
and calibration hedges are stable; the source-fidelity surface was unverified until this pass
and is now verified for all ten references against primary text.* A future pass that wants to
skip §2.4 here should confirm the References block is byte-identical to this one — and should
check the ledger's years against the article rather than against the previous ledger.
