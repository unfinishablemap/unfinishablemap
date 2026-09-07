---
title: "Deep Review - The Selection-Criterion Problem"
created: 2026-09-07
modified: 2026-09-07
human_modified:
ai_modified: 2026-09-07T07:51:09+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-07
last_curated:
---

**Date**: 2026-09-07
**Article**: [[selection-criterion-problem|The Selection-Criterion Problem]]
**Previous review**: [[deep-review-2026-07-06-selection-criterion-problem|2026-07-06]] (also 2026-06-06, 2026-05-25)

## Lens Selection

Three prior reviews covered: source-faithfulness of cross-referenced Map claims and wikilink
resolution (2026-05-25); publisher-of-record citation web-verify with a per-cite ledger, and
faithfulness of the constraint-phenomenology bullet (2026-06-06); cross-link three-location
consistency for `curated-mind` (2026-07-06). All three closed with "no critical issues" and stability
notes recording the article as converged.

The un-run lens is **downstream-dependency currency**: the prior passes verified that this article's
imported claims were faithful *to the source articles as they then stood*, and never asked whether
those sources had since moved. Two of them had, both *after* the last review:

| Upstream change | Commit | Date | Last review |
|---|---|---|---|
| `trilemma-of-selection` retracts its exhaustiveness / "no fourth option" argument | `3a919a8891` | 2026-07-16 | 2026-07-06 |
| `selection-only-mind-influence` withdraws its Born-preserving rate derivation and re-scopes Born-preservation to the *unconditioned marginal* | `536fe3493b` | 2026-08-03 | 2026-07-06 |

This is the clean-streak trap:
the article had not modified itself, so damping read it as stable, while the ground moved under it.
Citation web-verify (§2.4) was **not** re-triggered — the References block is byte-identical to the
2026-06-06 verified version and no new external citation was added.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. The trilemma's exhaustiveness claim was left standing after its only support was removed.**

The article read: *"The trilemma is exhaustive in the relevant sense: a criterion is either reducible
to structure (i), absent (ii), or an irreducible feature of phenomenal character (iii)."*

Provenance matters here. The claim was present in the original 2026-05-25 expand-topic (`5d090bf018`).
The 2026-05-25 deep review then *supplied its support*, recording: "Strengthened the exhaustiveness
claim with the parallel 'no fourth option' cross-link to [[trilemma-of-selection]]." That parallel was
retracted upstream on 2026-07-16, and the 2026-09-07T02:50 sweep correctly severed the now-stale
parallel — but kept the conclusion, on the judgement that this trilemma is a sound partition over a
criterion's *logical form* even though the agency trilemma is not.

**That judgement does not survive scrutiny.** The chain is: reducible to structure → (i); no criterion
at all → (ii); otherwise irreducible. The final step — from "irreducible and non-structural" to "a
feature of *phenomenal character*" — is substantive, not logical, and the corpus itself supplies two
counterexamples:

- **Agent-causal grounding.** `trilemma-of-selection` L70 and L125 commit the Map's *agency-level*
  horn 3 to agent-causal libertarianism with a "substance-agent selector." A criterion grounded in a
  substance exercising a power is neither reason-bearing structure, nor chance, nor a quality of the
  candidates. The Map's own one-level-up position falls outside its own criterion-level partition.
- **An indexical selection principle.** `apex/born-preserving-causal-efficacy` desideratum 5 — the
  passage that names *this article* as "the standing reminder that this primitive is unfilled" —
  enumerates candidate selection principles as "an indexical 'this-outcome-for-this-subject' rule, a
  valence-weighting, a maximisation principle." An indexical rule is not a feature of phenomenal
  character. The article's own designated sibling lists a fourth option while the article asserts
  there is none.

Note also that the origin article states the trilemma with **no exhaustiveness claim at all**
(`forward-in-time-conscious-selection` L163: "the selection follows one of three paths"). The
exhaustiveness was this article's own addition, never inherited.

**Resolved.** The claim is retracted and replaced with heuristic framing that keeps the mixture
argument (which does hold), names both fourth options, and rests the Map's route to horn (iii) on
best-of-the-foregrounded-options-given-the-tenets — the same footing `trilemma-of-selection` L125
adopted for its own third horn.

**2. Dropped qualifier on Born-preservation (§2.5 class).**

The article read: *"preserves Born statistics at the ensemble scale."* Since `536fe3493b` the source
is explicit that preservation binds the **unconditioned** long-run marginal only —
"leaving the mind-conditioned distributions unconstrained." "At the ensemble scale" without the
qualifier asserts exactly what the upstream revision exists to deny. Corrected to "leaves the
*unconditioned* long-run distribution over outcomes Born-exact."

**3. A stranded dependent: an open problem the corpus has since partly discharged.**

The article read: *"How a systematic bias coexists with preserved Born statistics is itself part of
the open problem, not a solved feature."* This was accurate when written and is now stale.
`born-preserving-causal-efficacy` L85 answers precisely that question — Born-preservation constrains
the marginal and "says nothing about whether the conditionals on the right depart from it… That is
what lets token-level efficacy and aggregate invisibility sit together without contradiction," with
`selection-only-mind-influence` L77 supplying the worked case (uniform binary C, O = C: Born-exact
marginal, I(C;O) = 1 bit, the alphabet maximum).

The same passage also carried a live inference error: *"A preference that produced Born-distributed
outcomes indistinguishable from chance would collapse back into horn (ii)"* trades on
Born-conformity implying absence of consciousness-specific bias, which is the inference the upstream
withdrawal explicitly refutes.

**Resolved,** and the debt restated in its current, sharper form rather than deleted: preservation
*under intervention* on the distribution of conscious states forces either that no conditional differs
(horn (ii) by another route) or a law constraining admissible populations of intentions; and a
value-sensitive criterion — which is exactly what horn (iii) proposes — inherits the compensation
consequence (L101 of the apex: a tilt toward better outcomes for a subject demands a compensating tilt
toward worse outcomes elsewhere, under an unstated conservation law on outcome-luck). The apex flags
this as something "value-sensitive applied articles inherit rather than discharge"; this article is
the one that owns the value-sensitive criterion, and had not booked it.

### Reasoning-Mode Classification (§2.6)
Unchanged and still correct. Engagement with the functionalist (horn i): **Mode Three** —
"internally coherent; it is simply a different metaphysics." Engagement with the
randomness/spontaneous-collapse reading (horn ii): **Mode Three** — "a reviewer who rejects the
tenets can take horn (i) or (ii) without inconsistency." No boundary-substitution. No label leakage
(grep-verified clean for mode labels, persona names, `Engagement classification:`,
`direct-refutation-discipline` meta-commentary, and bold `**Evidential status:**` callouts).

### Medium Issues Found
- `born-preserving-causal-efficacy` was a load-bearing dependency cited nowhere in the article
  despite naming this article twice. Resolved: added to body (twice), `related_articles`, and
  Further Reading — the three-location consistency the 2026-06-06 and 2026-07-06 reviews established.

### Counterarguments Considered
Eliminative-materialist / Many-Worlds / Buddhist rejection of the phenomenal-valuation primitive and
the empiricist "unfalsifiable primitive" objection — bedrock framework-boundary disagreements per all
three prior stability notes. **Not re-flagged.**

### Calibration Diagnostic
Applied to every load-bearing claim: *would a tenet-accepting reviewer still flag it as overstated?*
Post-edit, no. Notably the exhaustiveness claim **did** fail this test before the edit — a reviewer
who fully accepts dualism and bidirectional interaction would still reject "the partition is
exhaustive," because agent-causal and indexical criteria are available *inside* the tenets. That
makes it a correctable defect rather than a bedrock disagreement.

## Optimistic Analysis Summary

### Strengths Preserved
- The honest "neither horn is *impossible*; each is ruled out by a tenet the Map holds" paragraph —
  untouched, and the retraction above brings the trilemma section into line with it.
- The Evidential Status section's hardline-empiricist restraint (tenets remove a defeater without
  upgrading evidence) — preserved verbatim.
- The Phenomenal Valuation Law modest/ambitious framing split — untouched.
- "Where the Primitive Already Does Work" — the highest-value section across three reviews; only its
  closing summary sentence was compressed, no bullet altered.
- The decision-void opacity argument — untouched.

### Enhancements Made
- The retraction now makes the article *more* honest than before rather than less useful: it names
  two concrete rivals to horn (iii) instead of asserting there are none.
- The Born-preservation debt is stated in its live form, which is more demanding than the vague
  version it replaces.

### Cross-links Added
- [[born-preserving-causal-efficacy]] (body ×2, `related_articles`, Further Reading)
- [[agent-causation]] (body)

## Length

2375 → 2606 words (+231). Crossed the concepts/ soft threshold (2500); 894 words under hard (3500).
The additions are corrections rather than expansion, and were partially offset: the new trilemma
prose was compressed once written, and two redundant summary passages were trimmed (the
"Consolidating it here…" sentence, duplicated by the Relation to Site Perspective closing, and that
closing's second sentence).

## Remaining Items

**Possible sibling loci — not swept, flagged for a future pass.** The stale-dependency pattern found
here is by construction not confined to one file. `selection-only-mind-influence`'s 2026-08-03
withdrawal has other downstream readers, and a corpus grep for unqualified "preserves Born statistics"
returns hits in `positions/`, `tenets.md`, `apex/` and several `topics/` — most of which are correctly
scoped to P-Q2's *exact* marginal preservation and are fine. This review verified only the one file it
covered. A genuine sweep would need to check each
locus for the *unconditioned* qualifier rather than for the string.

## Stability Notes

Carry forward from prior reviews, unchanged:

- The functionalist reading of horn (i) and the eliminative-materialist / Many-Worlds / Buddhist
  rejection of the phenomenal-valuation primitive are **bedrock framework-boundary disagreements**.
  Do NOT re-flag as critical.
- The Evidential Status section is correctly calibrated. Do NOT let a future optimistic pass upgrade
  the Phenomenal Valuation Law toward "live hypothesis."
- Citations were publisher-of-record verified 2026-06-06 (Chalmers 1996; Chalmers & McQueen 2021,
  arXiv:2105.02314; Kane 1996) and the References block is unchanged since. No re-verification needed
  absent a new citation.

New, and the correction to the prior three:

- **A three-review clean streak on this article measured self-modification, not dependency freshness.**
  Both defects found here entered while the article sat untouched. The heuristic that earned its keep:
  ask what moved *under* the article — `git log -S` on the specific claims it imports — rather than
  what changed *in* it.
- **The exhaustiveness claim should stay retracted.** It is now the third time a "no fourth option"
  argument in this cluster has been walked back. If a future pass is tempted to restore it, the
  counterexamples are `trilemma-of-selection` L70/L125 (agent-causal grounding) and
  `born-preserving-causal-efficacy` desideratum 5 (indexical rule) — both in-corpus, neither
  requiring a tenet-rejecting reviewer to press.
