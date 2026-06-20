---
title: "Deep Review - Motor Selection and the Attention-Motor Interface"
created: 2026-06-20
modified: 2026-06-20
human_modified: null
ai_modified: 2026-06-20T07:19:20+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-20
last_curated: null
---

**Date**: 2026-06-20
**Article**: [[motor-selection|Motor Selection and the Attention-Motor Interface]]
**Previous review**: [[deep-review-2026-06-01-motor-selection|2026-06-01]]

## Summary

Seventh review — a GENUINE-DRIFT verification pass. `last_deep_review` was 2026-06-01 but
`ai_modified` had advanced to 2026-06-19 via two own-body refines that bumped `ai_modified` without
bumping `last_deep_review`, leaving both unverified:
1. **6822c9ede (2026-06-16)** — added a load-bearing "mechanism-debt" paragraph to the Honest-Gap
   section (the bias-without-deviation / Born-preservation crux + a deep-link to the
   quantum-interface register's `^mechanism-debt` anchor).
2. **f2521415c (2026-06-05)** — a corpus-wide Cai/Kaeser (2024) citation-metadata fix.

Both were verified this pass. The mechanism-debt paragraph is correctly calibrated. The Cai/Kaeser
"fix" was itself correct (no fix-introduced defect). A full publisher-of-record web-verify of every
substantive citation came back clean. One real defect surfaced and was fixed: **Fried 2011 had been
an orphan reference since the article's creation** (cited in References, never anchored inline) —
caught here for the first time across seven reviews.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Orphan reference: Fried, Mukamel & Kreiman (2011)** (FIXED). Reference #6 — a real,
  correctly-cited *Neuron* 69(3), 548-562 paper on SMA single-neuron preactivation predicting
  volition — was listed in References but never cited inline in any version of the body (present as
  an orphan since the original creation commit 3ee56b714). §2.4 treats inline↔References orphans as
  critical. Resolved by anchoring it inline in the Libet section, where it is topically exact: the
  single-cell complement to Schurger's stochastic-accumulator RP model. Length-neutral (offset by
  trimming a redundant effort-correlates-with-difficulty clause in the Stapp/Zeno paragraph that
  duplicated the point made twice elsewhere).

### Mechanism-debt paragraph verdict (PRIMARY check a)

**Correctly calibrated — neither over- nor under-concedes.** Verified against the register's own
framing at [[positions/quantum-interface#^mechanism-debt]]:
- The register says the position "sits genuinely close to epiphenomenalism," is "the strongest
  challenge to answer, not as a refutation," with a per-trial-vs-ensemble move marked a *candidate*
  resolution. The article's paragraph mirrors this exactly: "sits close to epiphenomenalism until a
  positive account survives review," and instructs the reader to "read the selection claims at the
  confidence level the register sets there, not above it."
- **Does not over-concede**: the selection account remains an ARGUED framework position throughout
  the body (PMTA extension, affordance competition, three-layer dopamine model), not a refuted one.
  The paragraph downgrades confidence to register level without retracting the argument.
- **Does not under-concede**: the bias-without-deviation dilemma is named as genuinely open
  ("until a positive account survives review", "no worked toy model").
- **Block-anchor link RESOLVES**: Hugo renders `[[positions/quantum-interface#^mechanism-debt]]` →
  `/positions/quantum-interface/#mechanism-debt`, and the target `<span id="mechanism-debt"></span>`
  exists at the P-Q3 framing in the built quantum-interface page. Live.
- **Coherent with sibling applied articles**: brain-specialness-boundary handles the same Born-
  preservation / epiphenomenalism pressure with consistent honest-marking (it calls brain-locality
  "a scope clause inside the Map's psychophysical coupling programme rather than a result derived
  from premises a critic would independently accept"). The mechanism-debt convention is propagated
  coherently across agency-and-will, value-in-selection, the four-quadrant taxonomy, and the apex
  decisions article. No divergence.

### Publisher-of-record web-verify ledger (PRIMARY check b)

- Cai, X., Liu, C. & Kaeser, P.S. (2024) (*Dopamine dynamics are dispensable for movement but
  promote reward responses*, Nature) — **state: real-correct**. Verified at nature.com /
  s41586-024-08038-z: vol **635**, issue **8038**, pages **406-414**. Author-list abbreviation
  (first two authors + senior author Kaeser, "et al." elided) is faithful — Cai is genuine first
  author, Kaeser genuine senior author. **The f2521415c corpus-wide fix was correct and introduced
  no defect.**
- Köhler, R.M., Binns, T.S., et al., Neumann, W.J. (2024) (*Dopamine and DBS accelerate the neural
  dynamics of volitional action*, Brain) — **state: real-correct**. *Brain* 147(10), 3358-3369,
  doi:10.1093/brain/awae219. First/senior authors and middle-author "et al." elision faithful.
- Chakroun, K., Wiehler, A., ... Peters, J. (2023) (*Dopamine regulates decision thresholds in
  human reinforcement learning in males*, Nat Commun) — **state: real-correct**. Vol 14, article
  5369, doi:10.1038/s41467-023-41130-y. Full author list and venue match.
- Cisek, P., & Kalaska, J.F. (2005) (*Neural correlates of reaching decisions in dorsal premotor
  cortex*, Neuron) — **state: real-correct**. Neuron 45, 801-814. The load-bearing **43%-of-cells**
  claim is faithful (source: "many (43%) task-related, directionally tuned cells in PMd"). Article
  uses a truncated title (full title has subtitle "...: Specification of Multiple Direction Choices
  and Final Selection of Action") — acceptable; author/year/venue/pages exact.
- Thura, D., & Cisek, P. (2014) (*Deliberation and commitment in the premotor and primary motor
  cortex*, Neuron) — **state: real-correct**. Neuron 81(6), 1401-1416, doi:10.1016/j.neuron.2014.01.031.
- Fine, J.M., & Hayden, B.Y. (2022) (*The whole prefrontal cortex is premotor cortex*, Phil Trans R
  Soc B) — **state: real-correct**. 377(1844), 20200524, doi:10.1098/rstb.2020.0524.
- Fried, I., Mukamel, R., & Kreiman, G. (2011) (*Internally generated preactivation...*, Neuron) —
  **state: real-correct** (metadata: Neuron 69(3), 548-562 — confirmed). Defect was ORPHAN status,
  not metadata; fixed by inline anchoring (see Critical Issues).
- Rajan et al. 2019, Schurger et al. 2012, Sjöberg 2024 — web-verified in the 2026-06-01 pass
  (incl. the Sjöberg page-range fix to 2267-2269, which matches the current file); References block
  unchanged for these since, so not re-litigated (convergence discipline).
- Hameroff & Penrose 2014, Libet 1983, Rizzolatti et al. 1994, Berridge 2007, Palmiter 2008,
  Frankish 2016, Tallis 2024, Schwartz/Stapp/Beauregard 2005, Stapp 2007 — stable canonical
  references, verified across the six prior reviews; no change.

### Inline ↔ References completeness

After the Fried fix: every References entry now has an inline anchor (by-name or, for the
Chakroun/Köhler "a 2023/2024 study" descriptions, by unambiguous description), and every inline
cite has a References entry. No remaining orphans in either direction.

### Currency sweep (PRIMARY check c)

`find_superlative_claims` returns empty — no "record/largest/latest/first/to date" superlatives in
the body. No currency-drift exposure. The empirical claims (43% cells, ~280ms commitment, ~10
bits/s bandwidth, decoherence timescales) are all qualified or framed as point findings, not
standing records.

### Calibration / leakage / banned-construct scan

- **No possibility/probability slippage.** The consciousness-selects interpretation carries no
  explicit evidential-tier label and is consistently framed conditionally ("if consciousness
  contributes by selecting", "the Map's extension... not a consequence they would accept",
  "proposes"). A tenet-accepting reviewer would not flag the calibration as overstated — the tenets
  remove the parsimony defeater without upgrading the empirical tier. Honest-Gap + mechanism-debt
  paragraphs explicitly cap confidence at the register's level.
- **No editor-vocabulary leakage** (grep clean for direct-refutation / unsupported-jump /
  bedrock-perimeter / Engagement classification / Evidential status: callouts).
- **No banned "not X but Y / This is not... It is" construct** (grep clean).

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded two-paragraph summary (truncation-resilient)
- Three-layer model (computation → dopamine → consciousness) and the capacity/initiation
  dissociation (Palmiter, Parkinson's)
- Desmurget double dissociation (intention vs execution)
- The new mechanism-debt paragraph — a genuinely strong honest-confidence-capping move that
  inherits debt rather than papering over it
- All five tenets addressed substantively; Honest-Gap section intact

### Enhancements Made

- Fried 2011 anchored inline as the single-cell complement to Schurger's RP-as-noise model
  (strengthens the Libet section AND resolves the orphan)
- Trimmed a redundant effort-correlates-with-difficulty clause (the point is made three times; once
  is enough) to keep the addition length-neutral

### Cross-links Added

None new this pass (the article's cross-linking was completed in prior passes; the mechanism-debt
deep-link added 2026-06-16 was verified rather than supplemented).

## Word Count Change

- Before: 3268 words (131% of 2500 soft threshold)
- After: 3302 words (132% of 2500 soft threshold)
- Net change: +34 (Fried inline anchor, offset by redundant-clause trim)
- Well below hard threshold (3500); soft_warning. No condensation required. Length-neutral honored.

## Remaining Items

None. Article remains a human-length-decision candidate parked above the concepts soft threshold,
but is ~198w below the 3500 hard ceiling and need not be cut.

## Stability Notes

Seventh review (2026-01-21, -01-26, -02-25, -03-22, -04-27, -06-01, -06-20). Convergence remains
firm. This pass verified two previously-unverified own-body refines (both sound) and caught one
since-creation orphan reference the prior six passes missed. No re-litigation of converged content.

Bedrock philosophical disagreements (stable across all seven reviews — do NOT re-flag as critical):
- **MWI proponents** find the "No Many Worlds" argument unsatisfying — framework-boundary disagreement
- **Decoherence skeptics** question quantum effects in warm tissue — Map flags this as speculative
  (Hameroff estimates qualified "though these figures remain disputed")
- **Eliminativists** deny the explanatory need for non-physical selection — worldview difference
- **Stochastic sufficiency advocates** resist the weighted-randomness vs genuine-choice distinction —
  explicitly engaged in "Why Neural Competition Doesn't Suffice"
- **Epiphenomenalism pressure on bias-without-deviation** — now explicitly marked in-body via the
  mechanism-debt paragraph; this is an honestly-named OPEN crux logged at the register, NOT a
  fixable defect. Future reviews should read it as the Map's acknowledged debt, not re-flag it.

Future reviews should only intervene on new substantive content, a source found to contradict a
specific empirical claim, a wikilink rename/archival, or a register-confidence change upstream that
the in-body mechanism-debt paragraph must track.
