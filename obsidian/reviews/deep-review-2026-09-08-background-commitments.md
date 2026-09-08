---
title: "Deep Review - Three Background Commitments the Tenets Rest On"
created: 2026-09-08
modified: 2026-09-08
human_modified: null
ai_modified: 2026-09-08T07:51:40+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-08
last_curated: null
---

**Date**: 2026-09-08
**Article**: [[tenets/background-commitments|Three Background Commitments the Tenets Rest On]]
**Previous review**: [[reviews/deep-review-2026-07-28-background-commitments|2026-07-28]] (and [[reviews/deep-review-2026-07-16-background-commitments|2026-07-16]])
**Word count**: 1721 → 1751 (+30; 87.5% of the 2000 tenets soft threshold, hard 3000, critical 4000 — printed live from `tools.curate.length.THRESHOLDS`, not quoted)

## Scope of this pass

Targeted audit of the §*Collapse redundancy* paragraph (L60), rewritten 2026-09-08T01:35 — six hours before this review. Four scope questions were put to it. One is a genuine calibration error and was fixed; three clear. The rest of the article was re-checked against the two prior reviews' stability notes and found unchanged and stable.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Possibility/probability slippage: "live rather than permanent" asserted a disjunct the register keeps open.** The rewritten sentence read:

> "The redundancy tension is therefore live rather than permanent — a conditioned signature is the register in which it could be relieved, and none has yet returned a positive."

"Live rather than permanent" rules permanence *out*. [[positions/quantum-interface]] does not. P-Q1's *Would shift if* states the two-horn structure explicitly: horn (a) — a born-preserving conditional signature `P(O | do(C), X) ≠ q(O | X)` for some specifiable context X — is answered **only *in principle***, and **"horn (b) remains live"**, where horn (b) is the case in which "no grain of conditioning ever separates a selected from an unselected outcome" and "'selection' collapses to an epiphenomenal redescription of chance." P-Q1's *Band rationale* is explicit that in-principle specifiability is what kept the credence off *low*, while "the signature is currently **unmeasured**, horn (b) remains live, P-Q10 stands."

So the register supports *"the route is not closed"*, not *"the tension is not permanent"*. Converting in-principle specifiability of a signature into temporariness of the tension is exactly the pattern §2 classes as a calibration error rather than a bedrock disagreement: a tenet-accepting reviewer, reading P-Q1, would still flag it. On a tenets-tier page that everything downstream inherits from, this is the highest-cost place for it to sit. **Resolution**: replaced with an explicitly two-directional statement that names the contrary possibility in the register's own terms.

**2. Wrong-paragraph transplant: an instrument-scope clause imported over the cited anchor's own grounding.** The paragraph cites `[[tenets#^minimal-quantum-interaction|falsifiability status]]` — the **Tenet 2** anchor, `tenets.md` L75 — but transplanted its wording from the **Tenet 3** paragraph at `tenets.md` L107.

- L75 (Tenet 2, the anchor actually cited): "under any *unconditioned aggregate* test the mechanism is *empirically indistinguishable from chance*—**by construction, not by any sensitivity limit**."
- L107 (Tenet 3, the source of the transplanted phrase): "*empirically indistinguishable from chance* under any *unconditioned aggregate* test **current or foreseeable instruments could run**."

These do not say the same thing about what *grounds* the indistinguishability. L75 disavows sensitivity limits; L107's clause makes the claim instrument-relative. Importing L107's clause under L75's anchor misreports the cited tenet, and — because it leaves a false opening in the *unconditioned* register (better instruments might yet discriminate) — it also understates the structural fact the Map owns knowingly. **Resolution**: replaced the instrument clause with L75's own grounding, at zero net word cost.

### Medium Issues Found

**3. Redundant restatement with an internal scope wobble.** "so no aggregate statistic **now available** discriminates it from an idle posit" restated the preceding clause at a *narrower* instrument scope than that clause's own "current **or foreseeable**" — two different reaches inside one sentence. Folded into the fix for issue 2: "now available" removed, leaving the claim universal over *aggregate* statistics, which is what "by construction" licenses.

**4. "None has yet returned a positive" implies a search that has not happened.** Literally true, but it suggests a body of negative results. The actual record, per `tenets.md` L75 and P-Q3's discriminability line, is one coarse-grain instance — the preregistered intention-to-RNG nulls of Maier et al. (2018) — with "the finer grains no instruction reproduces stay untested." Restated as "the one coarse grain tried so far ran null," which is both accurate and *less* concessive than the original.

### Question 4 — over-concession in the other direction: NOT FOUND

Checked the paragraph for the tells (*no possible / cannot ever / in principle undetectable*). Before the edit: none; the strongest candidate, "current or foreseeable instruments could run", is bounded by "unconditioned aggregate" and does not concede blanket undetectability. After the edit: "by construction rather than by any sensitivity limit" is unbounded in *instrument*-space but bounded in *test*-space, which is precisely the canonical L75 form; and "no grain of conditioning ever separates a selected outcome from an unselected one" appears only as a *contrary possibility the register keeps live*, modalised, in P-Q1's own words. The revision reduces over-concession risk on both sides by making permanence and relief symmetrically open.

**The general point worth recording**: the bound that protects this sentence is the **test-space** bound ("unconditioned aggregate"), not any instrument-space bound. The [[concepts/pragmatism]] defect this was compared against was unbounded in *test* space ("no statistical trace that any presently conceivable instrument could resolve"), which is why it over-conceded. An instrument-space clause adds no protection and, as issue 2 shows, can actively mis-ground the claim.

### Citation check (§2.4)

Four references, unchanged since the 2026-07-28 pass whose ledger was complete for all four; the 2026-09-08 rewrite introduced **no new bibliographic cites** (its only references are internal wikilinks). Per that ledger's own re-verification condition, a full publisher-of-record re-run is not owed. Cross-reference check (step 5) re-run and clean:

- Saunders 2010 (Chance in the Everett Interpretation) — inline L48 ↔ References L68. No orphan.
- Wallace 2012 (The Emergent Multiverse) — inline L48 ↔ References L70. No orphan.
- Sebens and Carroll 2018 (Self-Locating Uncertainty…) — inline L48 ↔ References L69. No orphan.
- Wilson 2020 (The Nature of Contingency) — inline L52 ↔ References L71. No orphan.

Superlative-claim sweep (`find_superlative_claims`): zero hits, so no empirical-currency sub-pass owed.

### Reasoning-mode check (§2.6)

The article's one named-opponent engagement is with the Everettian (Saunders, Wallace, Sebens & Carroll, Wilson) at L50/L52. Mode Three — framework-boundary marking, correctly and explicitly: "It runs counter to the Map's foundational commitments, and that is the honest thing to say about it: the disagreement sits at the framework boundary." No boundary-substitution (the article does not claim to refute branch-local authorship from inside Everettianism; it names the global-exclusion posit as asserted rather than argued). Label-leakage grep for all forbidden editor-vocabulary terms: zero hits. No change needed.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-posit dependency audit is untouched. Its central move — refusing to let the measurement problem be double-counted as evidence for mind (L42) — remains the article's strongest contribution and is the reason prior reviews named it a *reference point* for the slippage discipline.
- L52's *nonactual*-versus-*occurrence* gloss, added 2026-07-28, still does its work: Wilson's indexical-actuality reading is pre-empted rather than left as an opening.
- L62's "one body of evidence has been presented as supporting two conclusions when it supports one" — kept verbatim; it is the cleanest sentence in the article.

### Enhancements Made

Symmetry restored to the redundancy paragraph's closing: the reader now gets both the relief route and the permanence route, with the empirical state (one coarse grain, null; finer grains untested) stated at its true size.

### Cross-links Added

None. The revision introduced **no new wikilinks**; the paragraph's two links (`tenets#^minimal-quantum-interaction`, `positions/quantum-interface#^mechanism-debt`) are unchanged and both targets and the `^mechanism-debt` anchor were confirmed present. Zero new push-blocker surface.

## Remaining Items

**`tenets.md` carries two non-identical scope statements, and L107 asserts they are identical.** L107 describes its own clause as "the same scoped indistinguishability registered under [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]] above", but L75 grounds the claim "by construction, not by any sensitivity limit" while L107 grounds it in "current or foreseeable instruments". A downstream page transplanting from L107 while citing L75 — which is exactly what happened here — inherits the weaker, mis-grounded form and reads as scoped when it is grounded differently. This is a canonical-page finding, out of scope for a deep review of a dependent article, and left for a dedicated pass rather than edited here.

## Stability Notes

- **Carried forward and still binding** from 2026-07-16 and 2026-07-28: (a) the Many-Worlds Defender's and physicalist's rejection of Posit Two and of the indexical "I" is bedrock, not a fixable flaw; (b) the absence of a "Relation to Site Perspective" section is not a defect here — the article *is* an audit of the site's foundational commitments; (c) the *nonactual*/occurrence question raised by Wilson is answered in-text and should not be re-opened as "the Everettian can satisfy global exclusion."
- **Narrowed**: the 2026-07-28 note that this article is "calibration-honest by construction and should be treated as a reference point for the slippage discipline, not a candidate for it" held for the text that existed on 2026-07-28. The 2026-09-08 rewrite of L60 introduced a slippage into new post-note content, which is why this pass flagged one. The note should be read as a claim about the three-posit argument, not a standing exemption for the whole file — new claim-bearing prose on this page is auditable like any other.
- **New**: the §*Collapse redundancy* closing is now two-directional by design. A future reviewer should not "tighten" it back toward "live rather than permanent" — the symmetry is the correction, and it tracks P-Q1's live horn (b). Conversely it should not be pushed to flat permanence: horn (a) is specifiable in principle, which is what keeps relief open.
- The instrument-scope-versus-test-scope point under Question 4 above is the reusable lesson: on this claim, only the *test*-space bound protects against over-concession.
