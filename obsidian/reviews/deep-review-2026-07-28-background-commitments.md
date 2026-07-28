---
title: "Deep Review - Three Background Commitments the Tenets Rest On"
created: 2026-07-28
modified: 2026-07-28
human_modified: null
ai_modified: 2026-07-28T18:22:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-07-28
last_curated: null
---

**Date**: 2026-07-28
**Article**: [[background-commitments|Three Background Commitments the Tenets Rest On]]
**Previous review**: [[deep-review-2026-07-16-background-commitments|2026-07-16]]

**Scope**: the 2026-07-16 review covered the two-posit version. Commit `ecaa657af` (2026-07-27) added **Posit Three: Global Exclusion of Unchosen Alternatives**, a third coherence tension (*agency overreach*), and the article's first References section. This review targets that delta; §2.4 web-verify is mandatory because the References block is new.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Broken heading anchor (fixed)**. The opening paragraph linked `[[tenets#Two Background Posits the Tenets Rest On|…]]`, rendering as `/tenets/#two-background-posits-the-tenets-rest-on`. The target heading in `tenets.md` was retitled to `## Three Background Posits the Tenets Rest On` (L178) in the downstream propagation pass, so the anchor pointed at nothing. Corrected to `Three`. Confirmed the rendered form in `hugo/content/tenets/background-commitments.md` L30 was the dead one; all other wikilinks in the file resolve (`tenets`, `project/direct-refutation-discipline`, `where-the-substance-commitment-enters`, `agent-causation`, `substance-property-dualism`, `free-will`, `prebiotic-collapse`, `many-worlds-argument` in `arguments/`, `agency-void` in `voids/`), and the four `^`-block anchors (`^dualism`, `^bidirectional-interaction`, `^no-many-worlds`, `^minimal-quantum-interaction`) all exist in `tenets.md`.

### §2.4 Publisher-of-Record Citation Ledger

Triggered: References section is new since the last review. Every cite verified at publisher of record.

- **Saunders, S. (2010), "Chance in the Everett Interpretation"** — state: **real-wrong-metadata (incomplete, completed)**. Chapter verified at Oxford Academic (`academic.oup.com/book/11755`) and against the author's own reprint (arXiv:1609.04720, whose footnote 1 names the volume). Editors are S. Saunders, J. Barrett, A. Kent and D. Wallace; full volume title *Many Worlds? Everett, Quantum Theory, and Reality*; chapter pages 181-205. The entry had "S. Saunders et al. (eds.), *Many Worlds?*" with no page range; expanded to the full tuple.
- **Sebens, C. T. and Carroll, S. M. (2018)** — state: **real-correct**. *British Journal for the Philosophy of Science* 69(1), 25-74, DOI `10.1093/bjps/axw004`, March 2018. Author order verified: Sebens first, Carroll second (arXiv:1405.7577 metadata and the OUP article page `academic.oup.com/bjps/article/69/1/25/2669754`). Note for future reviews: PhilPapers carries a duplicate record (`CARSUA-2`) with the order reversed, and search summarisers echo it — the publisher order is Sebens/Carroll.
- **Wallace, D. (2012), *The Emergent Multiverse*** — state: **real-wrong-metadata (subtitle restored)**. OUP 2012 verified (`academic.oup.com/book/25622`, ISBN 9780199546961). Subtitle *Quantum Theory according to the Everett Interpretation* added.
- **Wilson, A. (2020), *The Nature of Contingency: Quantum Physics as Modal Realism*** — state: **real-correct (newly added this pass)**. OUP 2020, xi+219 pp., verified at `academic.oup.com/book/36927`; the indexical-actuality doctrine confirmed against the NDPR review ("an indexical conception of actuality", p. 38 of the book) before the claim was written.

Currency sweep: `find_superlative_claims` returns empty — no superlative empirical claims in the file. Inline ↔ References cross-reference: all four entries are cited inline; no orphans in either direction.

### Attribution / Framing Issues Found (§2.5)

- **Sebens and Carroll over-read (fixed, low)**. The article had them "supply the self-locating perspective from which the branch's outcome is the agent's own." Their contribution is the Epistemic Separability Principle and the credence assignment it licenses for an agent who is self-locatingly uncertain *after* branching; the ownership gloss reads more into it than the paper claims. Rewritten to "formalise the self-locating standpoint of an agent who, after branching, occupies exactly one branch and assigns her credences from inside it." The argument the sentence serves is unaffected.
- **Saunders/Wallace framing — verified accurate, no change.** The chapter text (arXiv reprint) contains explicit treatment of indexical/de se knowledge, self-location and personal identity (§ around lines 480-560 of the reprint), so "preserve psychological continuity, indexically owned memories and a determinate history along each branch" is faithfully attributed.

### Medium Issues Found

- **Unqualified "an Everettian dualist could grant it" (fixed)**. As written, the clause sat in tension with the Map's own account of what conscious causation *is*: Tenet 3 commits to outcome-selection, influence over which definite outcome becomes actual, which has no purchase where no outcome is excluded. The claim the argument needs is only that *some* mental causation is available branch-locally. Rewritten to grant that "mind makes a causal difference" while noting that a branching dualist forgoes the Map's particular mechanism and must route the influence elsewhere. This preserves the point (conscious causation is not the discriminator) and removes the collision with Posit Two.
- **"Globally nonactual" left *actual* unanalysed (fixed, expansion)**. The section's central condition demands that incompatible alternatives be "globally nonactual" / not occur "anywhere," but the corpus supplies no reading of *actual* strong enough to do the work. Wilson's quantum modal realism is the counterexample: branches are genuinely existing worlds whose actuality is indexical, so an Everettian of that stripe satisfies the letter of the condition and keeps the branching. Fixed by adding the gloss "—unrealised anywhere" to the posit's canonical italic statement plus a paragraph explaining why the gloss is needed. This is in the section's own register (state the commitment, then state what it costs) and strengthens rather than softens the article's thesis: the posit is heavier than its original phrasing suggested.
- **Terminology decision — the canonical phrase was deliberately NOT changed.** The first fix attempt replaced "globally nonactual" with "globally unrealised" throughout, including in `tenets.md`'s summary. Reverted: `todo.md` L1624 carries an in-flight consolidated calibration task (9 of 12 files done) whose Rule (A) instructs downstream articles to ground authorship claims on alternatives being "*globally nonactual*", and three already-calibrated articles (`topics/consciousness-and-moral-agency-under-duress.md`, `topics/responsibility-gradient-from-attentional-capacity.md`, `topics/biological-teleology-and-the-interface-framework.md`) use that exact phrase. Changing the canonical wording mid-propagation would have split the corpus's vocabulary and desynchronised the running task for a purely verbal gain. The strengthening is carried as a gloss instead, so the greppable phrase survives and the substance is still fixed. `tenets.md` was edited and reverted; its diff is empty and its 6374-word `critical` length is untouched.

### Counterarguments Considered

- **Many-Worlds Defender (Deutsch)**: "the Map's exclusion demand is a verbal victory — nothing is 'actual' but this branch anyway." Now addressed in-text via the Wilson paragraph rather than left for the reader to spot.
- **Empiricist (Popper's ghost)**: "what observation could bear on global exclusion?" — none, and the article already says so; the corridor bias is registered as empirically indistinguishable from chance and the posit is held as a chosen starting point. No new defect.
- **Eliminative Materialist / Hard-Nosed Physicalist**: reject the determinate persisting subject of Posit One outright. Bedrock framework-boundary disagreement, already recorded in the 2026-07-16 stability notes. Not re-flagged.

### §2.6 Reasoning-Mode Classification

- Engagement with the Everettian (Saunders / Wallace / Sebens-Carroll / Wilson): **Mode Three — framework-boundary marking**, correctly applied. The section explicitly declines to claim refutation ("is not refuted by anything inside the Map's agency case… the disagreement sits at the framework boundary"), which is the honest classification given that every weaker condition is branch-locally satisfiable. No boundary-substitution: the article is if anything the corpus's model of the opposite discipline, since its whole purpose is to withdraw an overstated entailment.
- Label-leakage scan: clean. The prose uses the writing-style guide's sanctioned natural forms ("helps itself to that condition without showing why", "runs counter to the Map's foundational commitments") and carries none of the forbidden editor-vocabulary tokens.

### Possibility/Probability Slippage Check

- **None.** The article again runs the opposite direction: Posit Three's whole function is to *withdraw* a claimed entailment (No-MWI from sourcehood) and re-describe it as resting on an asserted posit, and the "agency overreach" tension names one body of evidence having been presented as supporting two conclusions when it supports one. A tenet-accepting reviewer would find the calibration honest throughout; the changes in this pass push in the same direction.

## Optimistic Analysis Summary

### Strengths Preserved

- The two-move shape of each posit section — state the commitment, then state plainly in bold what it costs — is the corpus's cleanest instrument for auditing its own foundations. Preserved unchanged.
- The enumeration in Posit Three (psychological continuity, indexically owned memories, determinate branch history, local counterfactual control, reasons-responsiveness, ownership of the actual action, single-history persistence, conscious causation) is what makes the global-exclusion demand visible; it does real work and was left intact.
- The closing accounting — conscious selection stands or falls with the agency evidence, the rejection of many-worlds on agency grounds stands or falls with global exclusion — is precise and was not touched.

### Enhancements Made

- Wilson (2020) paragraph closing the *actuality* gap in the global-exclusion condition, with the posit restated in the stronger occurrence form.
- Everettian-dualist clause qualified so it no longer collides with Tenet 3's outcome-selection commitment.
- Sebens/Carroll framing brought back inside what the paper claims.
- References completed to full publisher tuples.

### Cross-links Added

- None. The article is already densely and accurately cross-linked; the new material attaches to `[[many-worlds-argument]]`, which the section already links.

## Remaining Items

None blocking. Length 1473 → 1646 words (82% of the 2000 soft threshold); no trimming was required and none of the additions displaced existing argument.

One optional follow-up, deliberately not taken here: the twelve articles being calibrated under the `todo.md` L1624 consolidated task state the posit as "globally nonactual" without the "unrealised anywhere" gloss. They are not wrong — they link to this file as canonical — but a future pass on that task could carry the gloss along as it goes. Not worth a dedicated task; the canonical statement now carries it.

## Stability Notes

- Carried forward from 2026-07-16 and still binding: (a) the Many-Worlds Defender's and physicalist's rejection of Posit Two and of the indexical "I" is bedrock, not a fixable flaw; (b) the absence of a "Relation to Site Perspective" section is not a defect here — the whole article is an audit of the site's foundational commitments; (c) the article is calibration-honest by construction and should be treated as a reference point for the slippage discipline, not a candidate for it.
- New: the *actuality* question raised by Wilson is now answered in-text. A future reviewer should not re-open it as "the Everettian can satisfy global exclusion" — the article now states the occurrence form of the posit, and the residual disagreement (whether branch-local authorship is enough) is bedrock.
- The citation ledger above is complete for all four references as of 2026-07-28. Re-verification is owed only if new cites are added.
