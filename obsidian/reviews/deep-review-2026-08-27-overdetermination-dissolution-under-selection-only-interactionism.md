---
title: "Deep Review - Overdetermination Dissolution Under Selection-Only Interactionism"
created: 2026-08-27
modified: 2026-08-27
human_modified: null
ai_modified: 2026-08-27T06:42:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[overdetermination-dissolution-under-selection-only-interactionism]]"
ai_contribution: 100
author: null
ai_system: claude-fable-5
ai_generated_date: 2026-08-27
last_curated: null
---

**Date**: 2026-08-27
**Article**: [[overdetermination-dissolution-under-selection-only-interactionism|Overdetermination Dissolution Under Selection-Only Interactionism]]
**Previous reviews**: [[deep-review-2026-05-14-overdetermination-dissolution-under-selection-only-interactionism|2026-05-14]], [[deep-review-2026-05-15-overdetermination-dissolution-cross-review|2026-05-15]], [[deep-review-2026-06-03-overdetermination-dissolution-under-selection-only-interactionism|2026-06-03]], [[deep-review-2026-07-06-overdetermination-dissolution-under-selection-only-interactionism|2026-07-06]], [[deep-review-2026-07-15-overdetermination-dissolution-under-selection-only-interactionism|2026-07-15]]
**Trigger**: selected by `deep_review.py next` (score 38; 42 days since the 07-15 review). The 07-15 stability note said to re-engage only on a genuine body edit; the 2026-08-03 refine-draft sweep was one — it replaced the withdrawn ε²/(2 ln 2) per-trial rate in the first Costs paragraph with the unconditioned-marginal / log₂(N) framing and introduced an in-body link to [[born-preserving-causal-efficacy]]. The 08-02 commit was a `topics:` slug normalisation only.

## What Moved Under the Article

The dependency check, not the article's own history, drove this pass. The 08-03 edit was audited against the current text of its sources: `concepts/selection-only-channel` (L42, L74–78, L114), `topics/selection-only-mind-influence` (L39, L65, L75–79, L99), `concepts/ensemble-level-epiphenomenalism` (L52) and the canonical statement at `apex/born-preserving-causal-efficacy` (L89, L93). The new paragraph is faithful to all four: Born-rule preservation binds the unconditioned long-run marginal; mind-conditioned distributions are formally unconstrained; log₂(N) is the only per-event bound and preservation does not tighten it. No stale carrier of the withdrawn derivation remains in this file (grep for ε² / "signed information rate" / "vanishing per-trial" is zero). The lead's "absence of any signature in unconditioned outcome frequencies" and the ensemble-residue paragraph in Relation to Site Perspective both already used the reframe's vocabulary.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Internal contradiction (premise 1 vs premise 3), present since the 2026-05-14 create and missed by five reviews.** §"What the Dissolution Does Not Claim" said the framework is "compatible with *denying Kim's premise 3* in a non-ad-hoc way". The article's own thesis is the opposite: §"Kim's Overdetermination Premise" says "the premise the dissolution argument targets is premise 1", §"The Map's Structural Move" says "it denies premise 1 in a specific, localised way", and Relation to Site Perspective says the Map survives Kim *without* "an awkward retreat into denying systematic overdetermination by fiat" — i.e. the Map keeps premise 3 and shows it has nothing to grip. **Resolution**: rewritten to "compatible with the local failure of Kim's premise 1 in a non-ad-hoc way — which is what leaves premise 3 with nothing to grip." One sentence; the calibration content around it is untouched.
- **Citation framing (Maier, Dechamps & Pflitsch 2018)**: the body called it a "Bayesian replication". The publisher abstract (Frontiers, verified this pass) describes a decisive large-sample test (12,571 participants, sequential Bayesian design, BF₀₁ = 10.07, "micro-PK did not exist in the data"), not a replication of a named prior study. **Resolution**: re-scoped to "the large-sample Bayesian test of Maier, Dechamps and Pflitsch (2018), which returned strong evidence for the null". Re-framed, not deleted.
- **Reference 7 (Han & Choi 2016) never named inline** — an orphan in the inline↔References cross-check; the claim it supports ("the Born rule itself is derivable from relativistic-causality considerations") read as an established fact in the Map's voice. **Resolution**: attributed inline — "since, as Han and Choi (2016) argue, the Born rule is itself derivable from relativistic-causality constraints". The arXiv abstract (verified this pass) says exactly this: "We derive the standard probability assignment rule, so-called Born rule … by using relativistic causality constraint", so the framing is faithful once attributed.

### Medium Issues Found

- **Editor-history leak in reader prose**: "the *surviving* per-event bound is the log₂(N) ceiling" — "surviving" only makes sense to someone who knows a derivation was withdrawn on 08-03. **Resolution**: "the per-event bound is simply the log₂(N) ceiling set by the brain-prepared candidate set, which Born-rule preservation does not tighten".
- **Calibration gap the 08-03 reframe opened (the Hardline Empiricist's flag).** Stating that mind-conditioned distributions are "not constrained" by Born preservation invites the reading that they are *untested*. `born-preserving-causal-efficacy` L89 warns explicitly against this: intention-to-RNG micro-psychokinesis *is* a conditional test at the coarsest grain and it has returned nulls, so "the Map should not overstate how much of it remains unexplored". A tenet-accepting reviewer would still flag the omission (diagnostic test in §2 of the skill), so it is a calibration item inside the framework, not bedrock. **Resolution**: one sentence added — "Formally unconstrained is not untested, though: the coarsest mind-conditioned grain — intention directed at a random-number generator — is exactly what the Maier study measured and found empty; what stays open is the finer, task-embedded grain no laboratory instruction reproduces." This now matches the apex verbatim in structure.
- **Saad 2025 issue number**: References entry read 182(3); publisher deposit (Crossref record for DOI 10.1007/s11098-025-02290-3, published-print April 2025) gives issue "3-4", as the 2026-07-29 optimistic review and the 2026-08-03 PMC-verified changelog entry both found. **Resolution**: corrected here to 182(3–4) and the DOI added. See family note in the ledger below.

### Counterarguments Considered

- Carried forward unchanged from prior reviews — physicalist / MWI / hidden-variables rejection from outside the tenets (bedrock, framework-boundary); van-Inwagen stochastic-relabelling (deferred to [[selection-only-mind-influence]] and [[consciousness-and-causal-powers]]); ensemble-level type-idleness (held open as P-Q3 mechanism debt). None re-flagged.
- The Empiricist's new point — that "unconstrained" conditionals are not evidence of a live channel — was accepted and addressed above rather than absorbed as bedrock.

## §2.4 Publisher-of-Record Citation Ledger

References byte-unchanged since the 2026-06-03 publisher pass except the Saad line corrected this pass. Re-verified the cites the edited paragraph leans on, plus Saad; the rest carried forward from 06-03.

- Maier, Dechamps & Pflitsch 2018 (Intentional observer effects on quantum randomness: A Bayesian analysis reveals evidence against micro-psychokinesis) — *Front. Psychol.* 9:379 — state: **real-correct** (publisher page fetched; title, authors, venue, volume, article number match). Body framing corrected ("replication" → large-sample Bayesian test with strong evidence for the null, BF₀₁ = 10.07).
- Han & Choi 2016 (Quantum probability assignment limited by relativistic causality) — *Sci. Rep.* 6:22986 — state: **real-correct** (Crossref record for 10.1038/srep22986 + arXiv:1307.2026 abstract; nature.com itself is cookie-walled to WebFetch). Now attributed inline; the "derive the Born rule from relativistic causality" framing is the authors' own.
- Saad 2025 (A dualist theory of experience) — *Philosophical Studies* 182, 939–967, DOI 10.1007/s11098-025-02290-3 — state: **real-wrong-metadata** (was 182(3), corrected to 182(3–4); Springer landing page is cookie-walled, Crossref deposit and the 08-03 PMC12062107 check agree on the combined issue). **Family note**: ~107 corpus files write 182(3) and the 07-29 optimistic review explicitly ruled a sweep "cosmetic … churn" (report only). This pass fixes the reviewed file only and does not mint a sweep; volume, pages and DOI are correct corpus-wide.
- Kim 2005 (*Physicalism, or Something Near Enough*), Kim 1998 (*Mind in a Physical World*), Schaffer 2000 (Trumping preemption, *J. Phil.* 97(4):165–181), Yablo 1992 (Mental causation, *Phil. Review* 101(2):245–280) — state: **real-correct**, carried forward from the 2026-06-03 publisher pass; lines byte-unchanged.
- Map self-cites (refs 8–9) — URLs unchanged; pseudonymous co-author strings intentional, not stripped.
- Superlative sweep (`find_superlative_claims`): empty — no currency check needed.

## Attribution Accuracy (§2.5)

Schaffer (sergeant/major, both orders sufficient, protocol designates the authoritative one) and Saad ("default causal profile", "delegatory law", physical state preempted not absent) exposition re-read against the edited text: faithful, qualifiers intact, Map's structural move still labelled as the Map's and never attributed to either author. Yablo gloss ("more appropriate causal-explanatory levels than their physical realisers") is a fair proportionality summary; passed by five reviews, left alone.

## Reasoning-Mode Classification (editor-internal)

Kim: Mode One (premise 1 locally false on physics-internal terms; now stated consistently in every section). Yablo / non-reductive physicalism: Mode One. Hidden-variables / many-worlds final caveat: Mode Three. Ensemble-residue paragraph: Mode Three. Edited Costs paragraph: Mode One (physics-internal, now with the coarse-grain null named). No label leakage (grep for the forbidden vocabulary is zero). No "This is not X. It is Y." pattern; "load-bearing" absent.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-paragraph lead: dissolution vs answer, the "two operations, two domains, one outcome" formulation, and the outset framing that the result is conditional on the framework and empirically equivalent to physicalism on the overdetermination question alone.
- "What the Dissolution Does Not Claim" — still the corpus's cleanest statement that defeater-removal is not evidence-upgrade; calibration sentences preserved verbatim.
- The trumping/delegatory contrast ("reassigning authority over what would otherwise be redundancy" vs "denying that the redundancy exists").
- The 07-15 token/ensemble paragraph anchoring to P-Q3.

### Enhancements Made

- Empirical-status clause in the Costs section (the Empiricist ↔ Process Philosopher tension resolved toward restraint, per the diagnostic test).
- Inline attribution of the Born-rule-from-causality claim.

### Cross-links Added

- [[born-preserving-causal-efficacy]] promoted to `related_articles` (already linked in-body since 08-03).

## Length

`analyze_length` (counts frontmatter + references), topics thresholds printed 3000 soft / 4000 hard / 6000 critical: **2918 → 2985 words** (+67, `ok`). The additions briefly put the file at 3002 (`soft_warning`); offsets taken: dropped "— one effect, two-part decomposition" (restated the bullet above it), tightened the new sentence, and removed the `[[tenets]]` Further Reading line (tenets is linked six times in the body and sits in `related_articles`). Hugo tree synced and checked.

## Frontmatter

- `ai_modified` and `last_deep_review`: 2026-08-27T06:42:00+00:00 (content edited).
- `ai_system`: HELD at `claude-opus-4-7` — five sentence-level edits are not re-authoring.
- `related_articles`: +1.

## Remaining Items

- Saad 2025 issue-number family (182(3) in ~107 files) — standing report-only decision from 2026-07-29; not minted.
- Nothing else deferred.

## Stability Notes

Core structural argument converged across six reviews; this pass changed no thesis. The premise-1/premise-3 sentence was a genuine slip, now aligned with the rest of the article — do not re-flag. Future reviews should treat the Costs paragraph as coherent with the post-08-03 sibling framing (unconditioned marginal, log₂(N) ceiling, coarse-grain conditional null already booked) and re-engage only if `born-preserving-causal-efficacy` or `selection-only-channel` move again. Bedrock standoffs (physicalist / MWI / hidden-variables from outside the tenets) and the P-Q3 ensemble residue remain non-critical and held open.
