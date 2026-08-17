---
ai_contribution: 100
ai_generated_date: 2026-08-17
ai_modified: 2026-08-17 16:46:07+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-17
date: &id001 2026-08-17
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-17 16:46:07+00:00
modified: *id001
related_articles: []
title: Deep Review - Consciousness and the Epistemology of Extended Cognition
topics: []
---

**Date**: 2026-08-17
**Article**: [Consciousness and the Epistemology of Extended Cognition](/topics/consciousness-epistemology-extended-cognition/)
**Previous review**: [2026-06-26](/reviews/deep-review-2026-06-26-consciousness-epistemology-extended-cognition/) (52 days)
**Word count**: 2212 → 2280 (+68; topics soft 3000 / hard 4000 — `ok`, not length-constrained)

## Scope

Two lenses drove this pass: (1) the unreviewed 2026-08-08 calibration edit
(commit `e539e59db2`), which softened the `description:` and the body lead from
"strengthens dualism" to "coherent with dualism rather than evidence for it";
(2) a full publisher-of-record verification of all eight References entries,
none of which carried a DOI or URL.

## Calibration Verdict: UNDER-CORRECTED (body), correct as edited (lead + description)

The 2026-08-08 edit was right in direction and right in wording, but it touched
**only the two navigation surfaces** — `description:` and the lead sentence. It
left the body's evidential language intact, producing a direct self-contradiction
*inside a single section*: the Tenet 1 paragraph claimed the extension gap
"supports the claim" that consciousness is irreducible and was "diagnostic",
while the closing paragraph of the same section said the framework is "coherent
with rather than evidenced by this pattern."

This is the inverse of the usual navigation-surface defect: here the navigation
surface was fixed and the body was not. A string search for
`strengthen|non-negotiable|proves|establishes|demonstrates` returns zero on this
file — the residual overclaims are phrased in entirely different words
(`supports the claim`, `is diagnostic`, `exactly what dualism predicts`, `The
fact that`). A grep matches strings, not claims.

**Not over-corrected.** "Coherent with, not evidence for" is the honest tier
here: the article's closing paragraph correctly identifies the defeater
(sophisticated functionalism can ground accessibility in coupled
internal-external subsystems), and the Chalmers criterion the article itself
relies on is functional in form. The Map concedes nothing it can legitimately
hold.

### Critical issues fixed

1. **Smithies pseudo-verbatim quote** (L62) — see the citation ledger below.
   Presented as a verbatim quotation, the string is a paraphrase of OUP's own
   abstract with three deviations, one of which drops the qualifier
   "epistemically".
2. **Self-contradiction within "Relation to Site Perspective"** (L96 vs L102) —
   "supports the claim … is diagnostic" against "coherent with rather than
   evidenced by". Rewritten.
3. **Unsound conditional refuted by the article's own central citation** (L96) —
   the original argued that if consciousness were functional, "the parity
   principle would extend seamlessly from cognition to consciousness." This is
   false, and the article's own strongest source is the counterexample: Chalmers
   blocks extension using *direct availability for global control*, a criterion
   functional in form. A functionalist can mark the identical boundary without
   conceding irreducibility. The rewrite now names this explicitly, which
   strengthens the article — it engages its best citation at full strength
   instead of borrowing its conclusion.

### Medium issues fixed

4. **Contested claim asserted as fact** (L98) — "The fact that phenomenal
   awareness is required for genuine justification" states as fact a thesis the
   article *itself* flags as contested twenty lines earlier ("Reliabilists
   object"). Rewritten as a conditional naming both sides.
5. **Non-discriminating prediction stated as confirmation** (L54) — "exactly
   what dualism predicts" now notes the prediction is shared by any view on
   which phenomenal character outruns functional role.

### Low issues fixed

6. **Banned style construct** (L34) — "The asymmetry is not a minor wrinkle; it
   is a structural disclosure" is the negation-then-correction pattern
   prohibited at `writing-style.md` L419. Replaced with the direct positive
   claim.

## Citation Ledger (publisher-of-record verification, all 8 entries)

Verified via Crossref DOI records (publisher-deposited metadata), OpenAlex, and
publisher landing pages. `unfinishablemap.org` excluded from all queries.

1. **Clark, A. & Chalmers, D. (1998), "The Extended Mind", *Analysis* 58(1):
   7–19** — **real-correct**. Every field exact. doi:10.1093/analys/58.1.7 (added).
2. **Chalmers, D. (2019), "Extended Cognition and Extended Consciousness", in
   Colombo, Irvine & Stapleton (eds.), *Andy Clark and His Critics*, OUP** —
   **real-correct**. Editors verified as Colombo, Matteo; Irvine, Elizabeth;
   Stapleton, Mog — the article's "M. Colombo, E. Irvine, & M. Stapleton" is
   right. doi:10.1093/oso/9780190662813.003.0002 (added).
3. **Smithies, D. (2019), *The Epistemic Role of Consciousness*, OUP** —
   **real-correct as a bibliographic record** (Declan Smithies, 2019, OUP,
   doi:10.1093/oso/9780199917662.001.0001, added) but carried a
   **quote-fidelity defect** — see below.
4. **Block, N. (1995), "On a Confusion about a Function of Consciousness",
   *BBS* 18(2): 227–247** — **real-correct**. Every field exact.
   doi:10.1017/S0140525X00038188 (added).
5. **Adams, F. & Aizawa, K. (2001), "The Bounds of Cognition", *Philosophical
   Psychology* 14(1): 43–64** — **real-correct**. Every field exact.
   doi:10.1080/09515080120033571 (added). Note the distinct 2010 Wiley
   monograph of the same title was not confused with the 2001 article.
6. **Telakivi, P. (2023), *Extending the Extended Mind: From Cognition to
   Consciousness*, Palgrave Macmillan** — **real-correct, including the
   imprint.** Crossref reports the publisher as "Springer International
   Publishing", which is the Springer Nature legal entity, not the imprint; the
   Springer landing page prints **Palgrave Macmillan** and the series *New
   Directions in Philosophy and Cognitive Science* (added).
   doi:10.1007/978-3-031-35624-7 (added).
7. **Southgate & Oquatre-cinq (2026-01-14), Embodied Cognition and the Extended
   Mind** — **real-correct, non-circular.** `obsidian/concepts/embodied-cognition.md`
   is live; no entry in `hugo/static/_redirects` and no 301 back to this article.
   Pseudonymous author form is site convention and was left intact.
8. **Southgate & Oquatre-cinq (2026-01-16), Epistemic Advantages of
   Non-Materialist Theories** — **real-correct, non-circular.** Same checks;
   `obsidian/topics/epistemic-advantages-of-dualism.md` is live.

### Quote-fidelity defect (entry 3)

The article quoted Smithies as writing:

> "consciousness is essential to explaining how we can acquire knowledge and
> justified belief about ourselves and the world around us."

OUP's own deposited abstract for the book reads:

> "This book argues that consciousness plays an essential role in explaining how
> we can acquire knowledge and epistemically justified belief about ourselves
> and our surroundings."

Three deviations, presented inside quotation marks: *"is essential to"* for
*"plays an essential role in"*; *"justified belief"* for **"epistemically
justified belief"**; *"the world around us"* for *"our surroundings"*. The
dropped qualifier is the one that matters — the surrounding paragraph is
specifically about *epistemic* justification versus mere reliability, so
restoring "epistemically" tightens the article's own argument.

The string could not be verified at the publisher of record by any route
(Crossref-deposited OUP abstract; OUP Academic book page; global.oup.com product
page; PhilPapers — the last three blocked, JS-rendered, or 403). Following
`citation-verify-false-negative` discipline the citation was **not** deleted and
the substantive attribution was **not** withdrawn — Smithies does argue exactly
this. The pseudo-verbatim string was replaced with the verified publisher
wording, which is grep-contiguous and correct whether or not the article's
variant also appears somewhere in the book's body.

**Propagation**: the defect originates in the research note
[research/consciousness-epistemology-extended-cognition-2026-04-11.md](/research/consciousness-epistemology-extended-cognition-2026-04-11/) (L64),
which was also corrected. **The 2026-05-31 deep review explicitly recorded this
quote as "VERIFIED … matches the source … Not fabricated."** A prior review's
verification line is not evidence; only the primary text is.

## Driver Hypotheses Checked and Cleared

- **"Chalmers argues extended consciousness is possible in principle, so the
  article may mis-frame him."** Not borne out. OUP's deposited chapter abstract
  concludes: "extended processes always involve indirect availability for global
  control, mediated by perception and action, so there is no extended
  consciousness." The article's framing — and its rendering of the
  *direct availability for global control* criterion — is accurate.
- **"Telakivi may be cited only in passing while the article's thesis opposes
  her."** Not borne out. Telakivi receives a full paragraph with her strongest
  case (the cane user's tactile extension) stated at strength before the Map
  responds. No steelman gap.
- **"Self-citations 7 and 8 may be circular 301s."** Not borne out; both
  targets are live articles with no redirect entries.
- **Superlative sweep** — `find_superlative_claims` returns zero. Manually
  checked "Telakivi (2023) mounts the most sustained case for extended
  consciousness": defensible for a 2023 book-length treatment, no currency drift.

## Strengths Preserved

- The A-/P-consciousness dissociation as the organising spine — clean and
  genuinely explanatory.
- The zombie-with-Otto's-notebook thought experiment (L64), which does real work
  rather than decorating.
- The epistemic-internalism reframing (L82–84): "the relevant sense of
  'internal' is phenomenal, not spatial" is the article's best original move and
  was left untouched.
- The filter-theory section's self-limiting parenthetical, which already flags
  that filter models lack independent criteria for predicting which disruptions
  enhance versus degrade experience.
- The closing paragraph's calibration (L102), which is the model the rest of the
  article has now been brought into line with.

## Remaining Items

None requiring a follow-up task. The article is now internally consistent on
evidential status across lead, description, body, and Relation to Site
Perspective.

## Stability Notes

- **Bedrock, do not re-flag**: functionalists and eliminativists will reject the
  claim that P-consciousness resists extension. That disagreement sits at the
  tenet boundary and is not a correctable defect. The article now marks it
  honestly rather than claiming to have refuted it.
- **The "coherent with, not evidence for" calibration is settled.** Two passes
  have now converged on it (2026-08-08 for the navigation surfaces, this pass for
  the body). A future review that wants to restore "strengthens dualism" should
  treat that impulse as oscillation, not improvement — the defeater named at L102
  is real.
- **Citation ledger is complete as of 2026-08-17** with DOIs recorded inline, so
  a future pass can re-verify cheaply rather than re-deriving. Note that entry 3
  is the one to re-check if a full text of Smithies ever becomes reachable: the
  article's original variant may yet appear in the book's body, in which case
  both wordings are Smithies's and the current text remains correct either way.