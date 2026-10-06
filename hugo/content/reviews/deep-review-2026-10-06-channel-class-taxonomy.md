---
ai_contribution: 100
ai_generated_date: 2026-10-06
ai_modified: 2026-10-06 18:52:00+00:00
ai_system: claude-fable-5-1
author: null
concepts:
- '[[channel-class-taxonomy]]'
created: 2026-10-06
date: &id001 2026-10-06
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-06 18:52:00+00:00
modified: *id001
related_articles:
- '[[selection-only-channel]]'
- '[[stapp-quantum-mind]]'
- '[[born-preserving-causal-efficacy]]'
title: Deep Review - Channel-Class Taxonomy
topics: []
---

**Date**: 2026-10-06
**Article**: [Channel-Class Taxonomy](/concepts/channel-class-taxonomy/)
**Previous review**: [2026-08-02](/reviews/deep-review-2026-08-02-channel-class-taxonomy/)

Fifth pass. The article re-qualified because two refine-draft sweeps touched the body
after the 2026-08-02 review: the 2026-08-03 withdrawal of the zero-mutual-information /
ε²-per-trial derivation (Class 1 specification and Cross-Class Invariants rewritten to
"Born preservation pins the marginal only"), and the 2026-08-06 Tenet-3 reframing (Class 3
and Relation to Site Perspective now say the tenet is satisfied by the outcome-realisation
step, and that a class where mind "chooses only the question" would not satisfy it). The
2026-08-02 Stability Notes said a fifth pass finding only cosmetics should treat the
article as converged. **Verdict: FIX, not converged** — neither sweep propagated its
change to the article's own dependents. Both left a sentence elsewhere in the same file
that the new sentence contradicts. The References block is untouched since 08-02.

## Citation Web-Verify Ledger

Trigger met on the body-modified clause; the References block itself is unchanged since
the 2026-08-02 ledger. Re-verified this pass the two cites whose *use* the changed
passages now lean on; the rest carry forward from the 2026-06-02 / 07-11 / 08-02 ledgers.

- **Han, Y.-D., & Choi, T. (2016), "Quantum probability assignment limited by relativistic causality", *Scientific Reports* 6:22986** — **real-correct**, re-verified at OpenAlex (DOI 10.1038/srep22986; authors Yeong Deok Han, Taeseung Choi; 2016). Nature's landing page now 303s to an IdP cookie gate and could not be fetched directly. **Result-direction leg**: the abstract states "Born rule on quantum measurement is derived by requiring relativistic causality condition" — i.e. non-Born probability assignments generically break relativistic causality. That is the direction the article uses in Classes 1–4. Passes.
- **Pati, A. K. (2026), "No-Signalling Fixes the Hilbert-Space Inner Product", arXiv:2601.13012** — **real-correct**, re-verified at the arXiv API (sole author Arun Kumar Pati, published 2026-01-19). Unrefereed preprint; the article's use (inner-product geometry is class-independent) is modest and the sibling [selection-only-channel](/concepts/selection-only-channel/) already grades the no-signalling standing as resting on an unrefereed preprint.
- **Stapp 2006 verbatim quote** — unchanged wording, re-used this pass in a rewritten sentence; the quote itself was grep-verified against the LBL QID.pdf on 2026-07-11 and 2026-08-02 and was not re-downloaded. What changed is the *gloss* around it — see critical issue 1.
- Bösch, Steinkamp & Boller 2006; Eccles 1994; Hameroff & Penrose 2014; Maier, Dechamps & Pflitsch 2018; Penrose 2014; Shannon 1948; Sorkin 1994; Stapp 1993; Stapp 2007; Carroll 2011 — real-correct (prior ledgers; no use changed).
- Southgate & Oquatre-sept 2026-05-11; Southgate & Oquatre-six 2026-03-19 — Map self-cites, legitimate pseudonymous forms; not to be stripped.

**Inline ↔ References cross-check**: complete in both directions. `[[stapp-quantum-mind]]`
gains a second inbound anchor from Class 1; no new bibliographic entries.

**Superlative / currency sweep**: `find_superlative_claims` returns empty.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Stapp attributed to a class that requires the outcome-selection he declines (FIXED;
cited-author-stance leg).** Class 1's "Theories that occupy it" listed "the channel-theoretic
version of Stapp's outcome-level commitment", glossed as "at the outcome level, selection
without deviation from Born statistics", and Class 3 said Stapp holds that "the outcome-level
kernel is selection-only". Selection-only is defined by the table row "Mind selects realised
outcome: Yes". But the verbatim Stapp quote sitting inside the same Class 1 sentence says
the answer "is picked by 'Nature'", and [stapp-quantum-mind](/concepts/stapp-quantum-mind/) L64/L146 is explicit that
Stapp "declines the outcome-selection the Map asserts" and that "a reader sympathetic to
both should not take Stapp as endorsing the Map's outcome-selection". The 2026-08-06 edit
made the contradiction internal to this file: Relation to Site Perspective now says a class
where mind chooses "only the question and leav[es] the answer to nature" would not satisfy
Tenet 3 *at all* — which is Stapp's configuration — while Class 1 still placed that
configuration in a class the same section says satisfies the tenet. The 2026-07-11 pass
made the quote verbatim but kept the pre-existing gloss outside the quotation marks, where
the quote itself contradicts it. Corpus sweep: the "outcome-level kernel is selection-only"
gloss and the "channel-theoretic version of Stapp" clause live only in this file (plus its
Hugo mirror); single locus. **Fix**: Class 1 now names Stapp as the near-miss — his outcome
layer shares the class's Born-exact statistics, but the realised outcome is physics's, so
the model does not occupy the class and should not be read as endorsing the Map's
outcome-selection. Class 3 now says his model fills the basis layer while leaving the
outcome layer to physics, and the Tenet-3 sentence there adds that the satisfying layer is
the one Stapp's model does not claim. A one-line note under the table marks the outcome
column as class-level.

**2. Table column contradicted by the post-withdrawal Class 1 text (FIXED; internal
contradiction introduced by new content).** The table's third column was headed "Mind
alters *P(y|x)*" with "No" for selection-only. The intro defines *P(y|x)* as the
mind-conditioned kernel. Before 2026-08-03 the column was consistent with the body, which
then claimed mutual information between mind-state and outcome converges to zero (so
*P(y|x)* = *p(y)*). The 08-03 sweep replaced that with "leaves the mind-conditioned
distributions unconstrained" and "mind-conditioned throughput open up to the *log₂(N)*
ceiling" — i.e. *P(y|x)* **does** depend on *x* in selection-only; what is pinned is the
marginal. The column header was left behind. **Fix**: column renamed "Mind reweights the
physical prior {*p_i*}", which is the actual discriminator between Classes 1 and 2 (marginal
preserved vs. marginal departs), with a sentence under the table saying so explicitly.

**3. "No-signalling is trivially respected" overstates what the sibling derivation grants
(FIXED; calibration).** Class 1 said the theorem "is trivially respected — Born-rule
preservation across many trials is the channel's defining constraint". The sibling
[selection-only-channel](/concepts/selection-only-channel/) (L76, L127) argues the opposite: preservation of the *pooled*
histogram is not enough, because a mind-state that could label trials from outside would
function as a measurement setting and the distant marginal conditioned on it would depart;
the channel needs exact preservation *per publicly conditionable context*, and the standing
is "a framework-internal compatibility argument … narrower than automatic", with "treating
the theorem as satisfied by construction" named as [possibility-probability-slippage](/concepts/possibility-probability-slippage/).
Diagnostic test: a tenet-accepting reviewer would flag "trivially" — the sibling that
derives the result already does. **Fix**: rewritten to state the strong reading and that the
compatibility is framework-internal rather than automatic, pointing to the sibling.

### Medium Issues Found

None beyond the above. The three critical items are all propagation failures from the two
intervening sweeps rather than fresh errors; the sweeps' own installed sentences are
correct and were kept verbatim.

### Not Flagged (bedrock, per prior Stability Notes)

Eliminative-materialist, hard-physicalist, MWI, and Madhyamaka objections to the premises
remain framework-boundary disagreements. Tegmark's warm-wet decoherence objection to
Classes 3–4 remains out of scope. The ε convention (spread, rate ε²/(2 ln 2)) and the DOI's
`2005` segment were not touched, per the 2026-08-02 do-not-touch notes.

### Calibration check (possibility/probability slippage diagnostic)

Item 3 above is the one place the test fired. Elsewhere: "menu, not a verdict" intact; the
closing slippage inoculation intact; the RNG-psi ceiling still conditional; the Class 2 ε²
figure still explicitly a divergence approximation under declared bias rather than a
consequence of Born preservation (the 08-03 sweep's sentence). No class is presented as
empirically favoured.

### Reasoning-mode classification (§2.6)

Engagement with Carroll (Class 5): **Mode Three, conceded** — unchanged from 2026-08-02.
Engagement with Stapp (Classes 1 and 3): previously none — the article treated him as an
occupant rather than an interlocutor. Now **Mode Three, boundary marked honestly**: the
article records that Stapp's own model stops at question-choice and does not claim the
outcome layer the tenet requires, without claiming to refute him. Label-leakage scan clean.

### Notation and sync-safety watch

Table pipe escape removed with the old `P(y\|x)` header; the new header `{p_i}` and the
prose `*P(y | x)*` are plain. All `[[…]]` targets resolve, including the new
`[[stapp-quantum-mind]]` anchor in Class 1 and the existing bare
`[[born-preserving-causal-efficacy]]` (unique slug, lives in `apex/`). `topics:` entries
remain bare slugs. No EOF tool-call artifact.

## Optimistic Analysis Summary

### Strengths Preserved

- The five-row table, now with an accurate third column, remains the only one-view
  cross-tabulation of the Shannon components against all five classes.
- The 2026-08-06 Tenet-3 reframing is good and is kept verbatim: it locates the tenet in
  the outcome layer and registers the Process-1 relocation as acknowledged-not-adopted,
  matching `tenets.md` path (c).
- The 2026-08-03 sweep's "marginal only, conditionals free" statements in Class 1 and
  Cross-Class Invariants are correct and kept.
- "Menu, not a verdict" and the closing slippage inoculation — untouched, as every prior
  pass insisted.
- Class 5's honest concession to Carroll.

### Enhancements Made

- Stapp now functions as a precisely located near-miss for Class 1 and a basis-layer-only
  occupant of Class 3, which is more useful to a reader than the previous blurred
  placement and matches the corpus's canonical reading in [stapp-quantum-mind](/concepts/stapp-quantum-mind/).
- The table's third column now discriminates Classes 1 and 2 on the quantity that actually
  separates them.
- Class 1's no-signalling standing is now graded the same way the sibling derivation grades it.

### Cross-links Added

- [stapp-quantum-mind](/concepts/stapp-quantum-mind/) — second inbound anchor, from Class 1.

### Length

`analyze_length` reports 2869 words / soft_warning (reference-apparatus inflation: Further
Reading ~152 words, References ~268). Body ≈ 2449 against the 2500 concepts/ soft
threshold; net +152 total, of which the table note is the largest single addition.
One compensating trim in Class 5 (the "foil … explanatory point" tail). Body remains
under soft; no further cut required.

## Remaining Items

- Carried from 2026-08-02, still open and still out of scope here: Stapp 2006 page range
  `599–616` unconfirmed by registries (lives in `research/` notes and
  `quantum-state-inheritance-in-ai`); `objections-to-interactionism` cites the Carroll
  challenge to the 2016 book while this file and `conservation-laws-and-mental-causation`
  cite the 2011 post.
- The table's Class 3 outcome cell still reads "Yes (per chosen basis)" at the class level;
  the under-table note carries the Stapp exception. If a future pass wants the exception
  inside the cell, it should keep the cell short.

## Stability Notes

- **Stapp occupies the basis layer of Class 3 only.** His outcome layer is nature's choice
  by the orthodox statistical rule; he is not a Class 1 occupant and does not satisfy
  Tenet 3's outcome-selection on his own account. This matches [stapp-quantum-mind](/concepts/stapp-quantum-mind/) and
  [P-Q4](/positions/quantum-interface/#p-q4). A future pass that re-lists Stapp under selection-only, or restores "outcome-level
  kernel is selection-only", is reintroducing a contradiction with the Relation section.
- **The table's third column is the physical prior, not the kernel.** In selection-only
  the kernel *P(y|x)* is free and the marginal is pinned; renaming the column back to
  *P(y|x)* would re-break it against the post-2026-08-03 body.
- **"Trivially respected" is not available for no-signalling in Class 1.** The sibling
  derivation requires the strong per-context reading and grades the standing as
  framework-internal. Do not restore the by-construction wording.
- Carried forward: the DOI's `2005` segment is correct; the ε convention is the spread
  with rate ε²/(2 ln 2); the Stapp quote is verified against the LBL preprint only;
  framework-boundary disagreements are bedrock; "menu, not a verdict" is the calibration
  spine.
- Pattern note for the loop: both defects fixed here were *propagation failures from
  sweeps that corrected one sentence and left the same file's dependents standing*
  (08-03: Class 1 spec vs. table column; 08-06: Relation section vs. Class 1/3 placement).
  When a sweep lands on a converged article, the next deep-review should diff the sweep
  and grep the file for the claim the sweep withdrew, before trusting the prior
  convergence note.