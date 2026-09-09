---
title: "Deep Review - One Structure, Three Vocabularies"
created: 2026-09-09
modified: 2026-09-09
human_modified:
ai_modified: 2026-09-09T15:23:50+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-09
last_curated:
---

**Date**: 2026-09-09
**Article**: [[one-structure-three-vocabularies|One Structure, Three Vocabularies]]
**Previous reviews**: [[deep-review-2026-07-17-one-structure-three-vocabularies|2026-07-17]], [[deep-review-2026-06-06-one-structure-three-vocabularies|2026-06-06]], [[deep-review-2026-05-26-one-structure-three-vocabularies|2026-05-26]]

## Summary

Fourth deep review, selected at 54 days stale (score 56.8, top of a 381-candidate
pool). **Two critical findings, both in the same paragraph, both fixed.** The
article's grain-match argument rested on "three independently motivated
coarsenesses"; one of the three is derived from another by the Map's own source
article, and a second was labelled a mathematical necessity when it is an
inference from a caveated behavioural measurement.

The shape is worth recording: **this is the corpus's best statement of the
coherence-versus-confirmation distinction, and it over-read one of its own
legs.** The rigour of its `## The Discipline: Coherence, Not Confirmation`
section is exactly what made the earlier grain claim look pre-audited. Three
prior reviews passed over it — the 2026-07-17 pass explicitly *preserved* the
defective sentence as a strength (see Retired Strength below).

## Pessimistic Analysis Summary

### Critical Issue 1 — dependent leg presented as independent (internal contradiction)

The grain-match paragraph claimed:

> "Three independently motivated coarsenesses landing at the same grain is the
> kind of fit that makes 'one structure' a natural hypothesis."

Register C's policy-level grain is **not** an independent motivation. Its source,
[[delegation-meets-quantum-selection]], derives it *from the bandwidth figure*,
under a section headed "The Bandwidth Constraint as Delegation Scope":

> "Consciousness, **on the bandwidth figures**, cannot plausibly delegate at the
> level of individual quantum events. **At ~10 bits per second**, selection would
> be policy-level…"

The article quotes that very sentence as its Register C motivation, so the
dependence was visible in its own text. Registers B and C therefore share one
source; there are two independently motivated coarsenesses, not three.

**Independent corroboration — the article contradicted itself.** Its own register
table lists, for the Quantum selection row, `Leaves open: The causal logic; the
grain`. The table says the quantum register does *not* supply grain; the
paragraph counted it as supplying an independent coarseness. This is internal
contradiction, critical by the §2 severity definitions, not a bedrock
disagreement.

**Resolution applied.** The paragraph was rewritten to three paragraphs which
walk each leg's provenance, state that there are two independent coarsenesses
rather than three, note that the third agreement is guaranteed by construction,
and turn the article's own discipline on the finding: *"agreement guaranteed by
construction is exactly what [the discipline section below] calls evidentially
inert."* The conclusion is downgraded to "a mild reason to prefer the unified
reading, and a smaller one than a three-way convergence of independent
constraints would have supplied." Cross-references the table explicitly so the
two surfaces can no longer drift apart.

### Critical Issue 2 — "by mathematical necessity" on the ~10 bits figure

The paragraph claimed the bandwidth channel is coarse **"by mathematical
necessity (~10 bits cannot specify fine grain)"**. Measured in the pre-edit file:
`behavioural output` −1, `output bandwidth` −1, `upper bound` −1; `Zheng` and
`Meister` appeared **only in the reference list** (`find('Zheng')` on the body
before `## References` returned −1). The figure did load-bearing work three times
in prose with none of the corpus's standing caveat attached.

The corpus caveat, verified verbatim at `apex/interface-specification-programme.md:84`
and `apex/dualism-cartography.md:133`:

> "the ~10 bits/second figure (Zheng & Meister 2025) measures *behavioural
> output* bandwidth—observed typing, speaking, choice rates—not the
> consciousness-physics interface. The Map treats it as an **approximate upper
> bound** on conscious selection bandwidth, and future psychophysical work may
> revise the estimate."

The parent [[bandwidth-of-consciousness]] carries a **stronger** qualification
than the caveat alone: the figure is "measured as behavioural output and
converging at the order-of-magnitude level"; Sauerbrei and Pruszynski call the
ceiling **"a lower bound, not an upper bound, on the maximum information
throughput of an entire human"**; and "the distinction between 'hard ceiling' and
'typical operating point' has not been definitively resolved."

So "by mathematical necessity" failed twice over: the necessity attaches to
measured *output*, not to the channel, and the figure's status as a ceiling is
itself under live published dispute in the literature the parent article carries.

**Resolution applied.** Two changes. (a) A new caveat paragraph in Register B
records the provenance, the approximate-upper-bound treatment as an inference
from the behavioural bottleneck, the unresolved hard-ceiling question, and the
lower-bound commentary — closing with "The register's shape survives a revision
to 50 or 100 bits per second, since the interface argument needs only a large
asymmetry. What does not survive is any claim that depends on the figure being
exact." (b) The necessity claim became "an inference from the caveated figure
rather than a mathematical necessity."

### Retired Strength (prior-review correction, not oscillation)

The 2026-07-17 review listed "Three independently motivated coarsenesses landing
at the same grain" under **Strengths Preserved**. That endorsement is retired on
evidence. This is not oscillation under the convergence rule: the three prior
reviews ran quote-fidelity and metadata lenses, and all in-quote strings *were*
faithful — the defect was never in the quotations but in whether the three
motivations were mutually independent, which no prior pass examined. A future
review should not restore the three-way phrasing.

### §2.4 Publisher-of-Record Citation Web-Verify

Per-cite ledger. The References block is unchanged since the 2026-06-06
publisher-of-record pass; the body/References modification this cycle added no
new bibliographic entries, so the prior ledger carries forward:

- Saad, B. 2025, *A dualist theory of experience*, *Philosophical Studies*
  182(3-4), 939-967, DOI 10.1007/s11098-025-02290-3 — **real-correct**.
  ⚠️ Session fence accepted and re-confirmed: the `182(3-4)` form in this file is
  the *correct* one (Crossref gives volume 182, issue 3-4, pp. 939-967). The
  corpus-wide 142-locus `182(3)` majority is the wrong form. **Left as-is; no
  normalisation task minted** — that ~200-locus matter is already recorded for
  the operator.
- Zheng, J. & Meister, M. 2025, *Neuron* 113(2), 192-204 — **real-correct**.
  Currency note: the *superlative* status of the figure is contested rather than
  superseded; handled by the new caveat paragraph rather than by re-scoping a
  claim.
- Schultze-Kraft, M. et al. 2016, *PNAS* 113(4), 1080-1085 — **real-correct**.

Inline ↔ References cross-check: no orphans in either direction. The four Map
self-cites resolve. `find_superlative_claims` returned **0** claims.

### Internal-quote fidelity (all six re-grepped against current sources)

Checked because 12 of 13 dependencies moved (58 commits) since the last review.
**All six verbatim — zero drift:**

| quote | source | state |
|---|---|---|
| "cannot plausibly delegate at the level of individual quantum events" | `delegation-meets-quantum-selection.md` | verbatim |
| "can only select among pre-computed options" | `bandwidth-of-consciousness.md` | verbatim |
| "earns its keep by the coherence it buys, not by independent observation of the entity it quantifies over" | `delegatory-dualism.md` | verbatim |
| "would produce in the absence of any experience taking over" | `delegatory-dualism.md` | verbatim |
| "the load-bearing primitive of the whole theory…" | `delegatory-dualism.md` | verbatim |
| "empirically equivalent to alternatives on which the default causal profile is a classical-statistical object" | `delegation-meets-quantum-selection.md` | verbatim |

### High-movement dependency audit

- **`project/evidential-status-discipline` (7 commits)** — the article's cited
  operative phrasing *"alignment raises coherence rather than evidential
  status"* is **still verbatim** in the discipline. No drift.
- **`topics/bandwidth-of-consciousness` (7 commits)** — **drift found**, and it
  is Critical Issue 2. The parent accumulated caveats (behavioural-output
  framing, the lower-bound commentary, the unresolved hard-ceiling question)
  that this article never inherited. Now inherited.
- **`topics/epistemology-of-convergence-arguments` (6 commits)** — the article
  invokes "the independence proviso" by name. A literal grep for `independence
  proviso` returns **−1**, but that is a false absence: the source builds the
  term across two sentences — *"provided the routes are genuinely independent*.
  The epistemological challenge lies entirely in that **proviso**"* (line 62) and
  *"Their result sharpens the **proviso**"* (line 72). The formulation is the
  source's own vocabulary and the invocation is faithful. **No change.**
- **`concepts/cross-mechanism-convergence` (3 commits)** — the article's
  propofol/ketamine contrast is accurate: the source confirms mechanistic
  distinctness (propofol via GABA-A potentiation, ketamine via NMDA antagonism)
  producing "the same rank-order of vulnerabilities". No drift.
- Figure check: `~10⁹ bits per second` for neural processing matches the parent's
  `10⁹ bits per second (Zheng & Meister 2025)`. Correct.

### Possibility/Probability Slippage Check (§2)

The two critical issues above **are** the slippage, in its structural rather than
its tier-label form. No evidential-status tier was misassigned; instead a
dependent agreement was counted as an independent constraint, which is the same
inflation one level down. A tenet-accepting reviewer would flag it — the
diagnostic test is met — so it was treated as correctable, not as bedrock.
Post-fix, no slippage remains.

### §2.6 Reasoning-Mode / label leakage

No named-opponent refutation in this article; the physicalist reading is
explicitly *accommodated* rather than refuted ("compatible with a purely
physicalist reading"). No editor-vocabulary leakage: checked and absent —
`Evidential status:`, `bedrock-perimeter`, `unsupported-jump`,
`Engagement classification:`, `mode-mixed` all return −1.

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded warning before §1, and its anchor image: *"Stating the same
  thing three ways is not three witnesses agreeing. It is one witness with three
  accents."*
- The whole `## The Discipline: Coherence, Not Confirmation` section, which
  remains the corpus's best statement of the distinction — placing convergent
  redescription *below* cross-mechanism convergence on the ladder, and conceding
  that if the structure is a framing artefact the agreement is "guaranteed by
  construction, evidentially inert." Untouched.
- The menu / measure-over-the-menu / takeover-of-the-choice table and gloss.
- The honest closing: "Tidiness is a virtue of articulation. It is not a victory
  over the rivals."

### Enhancements Made

The fix turned out to be an enhancement of the article's own thesis rather than a
retreat from it. The discipline section's concession machinery was already strong
enough to convict the grain argument; applying it inward makes the article
self-consistent and gives it a live example of its own discipline biting on the
Map's side of the ledger.

### Cross-links Added

- [[interface-specification-programme]] — new inbound link; the caveat's canonical
  source, previously uncited here.
- [[bandwidth-of-consciousness]] — second contextual link, for the
  hard-ceiling/lower-bound qualifications.
- In-page named anchor to `#the-discipline-coherence-not-confirmation`
  (id/href match verified in built HTML).

## Length

2019 → **2358 words** (+339). 79% of the 3000-word `topics` soft target; status
`ok`. Not length-neutral mode — 642 words of headroom remain. No condensation
needed or performed.

## Remaining Items

None minted. One observation deliberately **not** turned into a task: the
`182(3)` vs `182(3-4)` corpus split (~200 loci) is already recorded for the
operator, and this file holds the correct form.

## Stability Notes

- **Do not restore "three independently motivated coarsenesses."** It is refuted
  by `delegation-meets-quantum-selection`'s own derivation and by this article's
  own register table. A prior review endorsed it; that endorsement is retired.
- **Do not strip the ~10 bits caveat paragraph** as redundant with the parent.
  The article's grain argument depends on the caveat, so the caveat has to be
  local. Its absence was the defect.
- The `182(3-4)` Saad form in this file is **correct**. Do not "normalise" it to
  the corpus-majority `182(3)`.
- Bedrock disagreement from physicalist, eliminativist and Many-Worlds personas
  remains expected — the article presupposes No-Many-Worlds and dualism and
  concedes as much. Do **not** re-flag as critical.
- Internal quotes were re-verified verbatim at the literal-string level this pass
  against current sources; re-grep only if a sibling source is rewritten.
- **Lens note for future passes on well-calibrated articles:** three reviews
  running quote-fidelity and metadata lenses all passed this article while a
  self-serving structural claim sat four paragraphs above its own refutation. The
  productive question was not "is each quote faithful?" but "does this article's
  own discipline convict any of its own arguments?"
