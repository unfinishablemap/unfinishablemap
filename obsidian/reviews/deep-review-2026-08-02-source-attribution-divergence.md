---
title: "Deep Review - Source-Attribution Divergence"
created: 2026-08-02
modified: 2026-08-02
human_modified:
ai_modified: 2026-08-02T11:12:31+00:00
draft: false
description: "Post-revision deep review of source-attribution-divergence: verifies the 2026-08-02 refine-draft pair landed cleanly and repairs one stranded pre-revision assertion that contradicted three revised loci."
topics: []
concepts: []
related_articles:
  - "[[source-attribution-divergence]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-02
last_curated:
---

**Date**: 2026-08-02
**Article**: [[source-attribution-divergence|Source-Attribution Divergence]]
**Previous review**: [[deep-review-2026-07-10-source-attribution-divergence|2026-07-10]] (web-verify pass; also [[deep-review-2026-06-02-source-attribution-divergence|2026-06-02]], [[deep-review-2026-05-09-source-attribution-divergence|2026-05-09]])

**Context — this is a post-revision audit, not a fresh adversarial pass.** The article
was substantively rewritten earlier today (10:08 UTC) across two `refine-draft`
commits (`bc2e3a647`, `e57a72ad0`) responding to
[[pessimistic-2026-08-02-source-attribution-divergence|the 2026-08-02 pessimistic review]],
which raised eight issues. The re-trigger of deep-review is therefore legitimate
(real content delta, not a cosmetic cross-link bump). The job here was to verify
the eight fixes landed, and to hunt for **regressions introduced by the revision** —
the failure mode a same-day rewrite is most exposed to. One was found and fixed.

## Verification of the 2026-08-02 revision (pessimistic Issues 1–8)

| # | Issue | Landed? | Locus |
|---|---|---|---|
| 1 | Matched-performance premise contradicts Empirical Signatures | **Yes** — took route (a), the honest one: lead ¶3 now states the difference in kind outright ("no matched-performance baseline exists"), and "Why Single-Species Variation Matters" repeats it | ¶3, §Why Single-Species |
| 2 | Option 1 mis-scored as anti-functionalist | **Yes** — re-scored: "Option 1 is the branch that costs the functionalist least, and the Map scores it that way" | §Wedge |
| 3 | Option 3 converts epistemic limit into metaphysical falsification | **Yes** — "leaves the identification … untested rather than refuted"; italicised "*establishes*, not merely suggests" gone; reconciled toward the compatibility concession | §Wedge |
| 4 | Dawes et al. 2020 mis-framed, breaches own firewall | **Yes** — retitled "Imagery-spectrum covariance—reported, not measured"; explicitly moved to the first-order-report side of the firewall; uncited false-memory clause removed | §Empirical Signatures |
| 5 | Mitchell & Johnson 2009 over-extended at two loci | **Partly — one locus regressed; see Critical below.** Typology and Neural-correlates loci correctly narrowed to aging/clinical group contrasts; the uncited frontoparietal-coupling sentence removed; "Mitchell-Johnson" format inconsistency fixed | §Typology, §Empirical Signatures |
| 6 | Trait premise asserted, never evidenced | **Yes** — "not noise around a uniform competence" replaced by an explicit unsettledness flag in the lead, plus a new closing caveat naming the missing retest-reliability coefficient and the group-effect variance-suppression trap | lead, §Empirical Signatures |
| 7 | Uncited 5–10% prevalence + uncited continuum claim + banned inversion | **Yes** — figure dropped for "prevalence estimates vary widely with the definition used"; continuum claim attributed to the Map | §Typology |
| 8 | Orphan / idle references | **Yes** — Pronin 2009 deployed at option 3 beside Schwitzgebel; Schacter et al. 1984 deployed at the History source-monitoring entry; Wegner and Wheatley (1999) given its year | §Wedge, §History, §Typology |

Deployments checked for accuracy, not just presence: Schacter, Harbluk & McLachlan
1984 does isolate origin-loss from content-loss in amnesic patients (the "a decade
earlier" relative to 1993 is a fair approximation of nine years); Wegner & Wheatley
1999 is the correct home of the I-Spy paradigm; Pronin 2009 is the introspection-illusion
source and belongs exactly where it was placed. All three are correct deployments of
already-verified references.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Internal contradiction — a stranded pre-revision assertion survived the rewrite.**
  The History section's Mitchell-and-Johnson paragraph still ended with
  "Population spread is settled by 2009." That sentence belonged to the pre-revision
  article, whose whole frame was that the population spread is an established trait
  fact. The revision demolished that frame at three separate loci — the lead
  ("Whether that spread is stable trait variance or partly measurement error is
  unsettled"), the Typology bullet ("the healthy-adult distribution's shape is
  **not settled** there"), and the Empirical Signatures caveat ("the spread is
  established as condition-sensitive variation in performance, not as stable trait
  variance") — and left the sentence standing.

  Two defects in one: (a) a flat self-contradiction with the lead and the closing
  caveat; (b) a re-instatement of exactly the source over-extension pessimistic
  Issue 5 was raised to remove — the article now said the *same* 2009 review both
  settled the population spread and left the healthy-adult distribution's shape
  unsettled, within four hundred words of each other. **Resolution: sentence deleted.**
  Nothing is lost — the History paragraph closes cleanly on the Schnider
  pathological-extreme anchor, and the spread's evidential status is handled twice
  elsewhere with the correct calibration.

### Medium Issues Found

- **Residual superlative inconsistent with the revision's own downgrade.**
  "This case is the cluster's least dramatic but most architecturally diagnostic."
  The revision established that this leg runs on a weaker and differently-shaped
  premise than its siblings, that it "may be locally absorbable", and that it
  delivers "less [pressure] than a matched-performance contrast would have
  delivered". Calling it the *most* architecturally diagnostic of the three then
  cuts against the article's own re-calibration. **Resolution: superlative dropped**
  ("the cluster's least dramatic leg"); the following two sentences already carry
  the substantive point about why subtlety is worth counting.

- **Negation-then-correction construct** (`writing-style.md` §Overused Words):
  "the divergence is not a peripheral curiosity but a structural feature of how
  cognition handles its own provenance". The pessimistic review caught the same
  construct in the voice-hearing bullet and the revision fixed that one; this
  instance survived. **Resolution: rephrased to the positive claim directly.**

### Low Issues Found

- **Residual unsupported assertion**: "The forms cluster only partially." stood
  immediately before the sentence conceding that inter-form prediction "has not been
  measured". **Resolution: removed**; the framework-expectation clause that follows
  carries the claim at the right strength, and the section's opening sentence already
  frames the typology as partly-independent pieces.

- "is empirically falsified across the cohort" (Occam's Limits) — pessimistic review
  proposed softening to "is not supported by the cohort data". **Not changed, and
  deliberately.** The falsification target is the naive *direct-readout* model, which
  makes a strong prediction (no source errors) that the misinformation and
  source-amnesia literatures straightforwardly defeat. That falsification does not
  depend on the trait claim the revision downgraded, so the verb survives the
  re-calibration intact. Recorded here so a future review does not re-open it.

### Counterarguments Considered

- **Churchland: "the source-monitoring framework is a tag-free account and you lean
  on it."** Not re-flagged as a defect. The article states the framework's tag-free
  character plainly in its own words ("memories lack native source tags"), concedes
  at the Site Perspective section that the data "are also fully compatible with
  reconstructive-cognition physicalism", and caps its conclusion at "pressure on the
  simple identification … rather than its falsification". The objection also lands
  more on vocabulary than substance: the trichotomy quantifies over *phenomenal
  source-confidence* (the felt sense of knowing where a content came from), which is
  not a contested posit, rather than over a reified tag. Absorbing it further would
  cost words the article does not have.
- Eliminative-materialist / hard-physicalist / Many-Worlds objections remain bedrock
  framework-boundary disagreements per three prior stability notes. Not re-flagged.

## Citation Web-Verify (§2.4)

**Satisfied by re-affirmation, not re-run — and the grounds are recorded so this is
auditable.** The References block was **not modified** by either 2026-08-02 commit
(verified: the diff contains no `+`/`-` line touching a reference entry), and the
block carries two independent publisher-of-record verifications:

- [[deep-review-2026-07-10-source-attribution-divergence|2026-07-10]] — full per-cite
  ledger, all 13 external academic cites verified at PubMed / DOI / publisher, all
  **real-correct**, no defects. That ledger stands and is not re-litigated here, per
  its own stability note.
- [[pessimistic-2026-08-02-source-attribution-divergence|2026-08-02]] (this morning) —
  re-verified all fourteen references' bibliographic metadata and the single external
  quotation (Nisbett and Wilson, "there may be little or no direct introspective access
  to higher order cognitive processes") verbatim at OpenAlex/DOI, plus targeted abstract
  checks on Dawes 2020, Mitchell & Johnson 2009 and Johansson 2005 that produced
  Issues 4 and 5.

What this pass did check, because it was new since both ledgers: the three newly-added
*inline deployments* (Schacter 1984, Wegner & Wheatley 1999, Pronin 2009) — all correct,
see the table above. Empirical-currency superlative sweep
(`find_superlative_claims`): **zero candidates**, unchanged from 2026-07-10.

## Optimistic Analysis Summary

### Strengths Preserved

- **The revision's central gain, and it should not be reversed**: lead ¶3 now states
  the difference-in-kind *at the outset* rather than smoothing it into a shared
  structural lesson. An article that concedes its own premise is weaker than its
  siblings' — in the lead, where a truncating LLM reader will still see it — is doing
  something the corpus should imitate.
- The firewall move (first-order phenomenal reports vs. second-order cohort-level
  calibration measures), and the newly-explicit marking-off of the imagery item as
  falling on the report side of it. The instrument was always right; the revision
  fixed what was run through it.
- The self-membership concession (the article both *uses* and *contributes to* the
  cluster it counts) and the conditional evidential tiering on common-cause-null
  survival. Untouched by every issue raised in three reviews.
- The option-2 "unpaid bill" analysis, including the pre-emptive admission that the
  trichotomy "could otherwise read as a false trilemma converging on the conclusion".
- "not 'I should have known' so much as 'I had no idea I could not tell'".

### Enhancements Made

None beyond the three repairs above — see Length.

### Cross-links

All 18 distinct wikilink targets re-resolved against `obsidian/` and `archive/`,
including the two section anchors (`aphantasia#cognitive-equivalence-and-the-function-gap`,
`synaesthesia#relation-to-site-perspective`) and the in-page `#empirical-signatures`
anchor added by the revision. **All live.** No new links added (length-neutral mandate).

## Length

3978 → **3960 words** (132% of the 3000 soft threshold, under the 4000 hard threshold).
The 2026-08-02 revision added ~520 words to the 3455-word 2026-07-10 state — the cost
of the calibration apparatus it installed, and worth it — which pushed the article to
within 22 words of hard. This pass ran **length-negative** accordingly: every repair
above removes text, none adds. No condensation attempted; the over-soft content is the
calibration prose four reviews have now protected, and a reduction below soft is a
human editorial call.

## Remaining Items

None pressing. If a future pass ever takes the article below soft threshold, the
Churchland tag-free concession (see Counterarguments) is the one addition that would
earn its words.

## Stability Notes

- **The 2026-08-02 revision is sound and should not be reverted or re-litigated.**
  All eight pessimistic issues landed; the only defect it introduced (the stranded
  "Population spread is settled by 2009") is fixed here. A future review that reads
  the pre-revision commits should not restore the trait framing.
- **Do not re-upgrade the leg.** The article now says, correctly and in three places,
  that it lacks the siblings' matched-performance premise and delivers less pressure
  than they do. That downgrade is the honest state, not a hedge to be tightened back
  up. Watch specifically for superlatives ("most diagnostic", "most architecturally
  telling") creeping back in — one had already survived from the pre-revision text.
- **Do not re-flag "empirically falsified across the cohort"** (Occam's Limits). It
  targets the naive direct-readout model, not the trait claim; the reasoning is
  recorded under Low Issues above.
- **The 2026-07-10 per-cite ledger remains authoritative.** The References block is
  unmodified since it was written. Do not re-run 15 publisher lookups unless a
  reference entry actually changes.
- Bedrock-style disagreement from eliminative-materialist / hard-physicalist /
  Many-Worlds personas is expected; do not re-flag as critical (fourth review to say so).
- The memory-anomalies pairing is independent-via-shared-root (cryptomnesia), not
  double-counting; do not "fix" it.
- **Convergence status: high.** Four deep reviews plus one pessimistic. The article's
  argument is now calibrated at the level its evidence supports. The next pass should
  expect a no-op and should treat finding nothing as the correct outcome.
