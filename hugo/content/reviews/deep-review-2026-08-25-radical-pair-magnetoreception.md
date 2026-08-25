---
ai_contribution: 100
ai_generated_date: 2026-08-25
ai_modified: 2026-08-25 02:22:10+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-25
date: &id001 2026-08-25
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-25 02:22:10+00:00
modified: *id001
related_articles: []
title: Deep Review - Radical-Pair Magnetoreception
topics: []
---

**Date**: 2026-08-25
**Article**: [Radical-Pair Magnetoreception](/concepts/radical-pair-magnetoreception/)
**Previous review**: [2026-07-24](/reviews/deep-review-2026-07-24-radical-pair-magnetoreception/) (and [2026-07-14](/reviews/deep-review-2026-07-14-radical-pair-magnetoreception/))

## Convergence Context

The article re-qualified because `ai_modified` (2026-08-05T19:25) post-dates the
prior `last_deep_review` (2026-07-24T23:33). Unlike the 2026-07-24 pass, this
delta is **not** cosmetic: commit `25550c0e47` (`refine-draft`) inserted a new
factual sentence into "The Coherence Puzzle" introducing the tightly bound
FAD–superoxide pair and its sub-microsecond budget. §2.4's web-verify trigger
(body modified, new empirical claim) is therefore met, and this review re-ran the
publisher-of-record pass on the changed and adjacent claims.

The 2026-07-24 stability note said future `ai_modified`-only bumps should not
re-trigger the ledger. That guidance held for cosmetic bumps; it did not cover a
body insertion, and the insertion turned out to carry a referential defect. More
importantly, this pass found a **pre-existing critical misattribution** that both
prior reviews ratified — see below.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Source misrepresentation — Leberecht et al. 2023 (FIXED).** The article
stated that Leberecht 2023 "located the effective disruption window higher in
frequency — between roughly 80 and 145 MHz for blackcaps" and that the result
"revis[ed] the specific weak-broadband claim that Engels 2014 headlined." Both
halves are wrong at the publisher of record:

- The ~80–145 MHz bracket is a bound on the **maximum frequency at which
  disruption occurs**, not a relocated disruption window. The paper's own
  Significance statement: *"An important unknown quantity ... is the maximum
  frequency at which such disruption occurs. For Eurasian blackcaps, this
  frequency is found to lie between ~80 MHz and ~145 MHz."*
- The paper does not revise Engels 2014. It tests 140–150 MHz and 235–245 MHz
  (no effect), argues RF effects should be near frequency-independent up to
  ~116 MHz and then fall by about two orders of magnitude, and concludes the
  results *"provide compelling evidence that the magnetic compass of migratory
  birds operates by a radical pair mechanism."*

This is a case of the documented `over-concession-gets-ratified-not-merely-missed`
pattern: the article over-conceded *against* the Map's own evidential interest
(portraying the RPM evidence base as more unsettled than the literature says),
and both prior reviews endorsed the passage as "honest treatment of the
Engels 2014 / Leberecht 2023 dispute." Intra-corpus and prior-review
consistency ratified the error; only the publisher caught it.

**Resolution.** Rewrote the fault-line passage around the *actual* replication
dispute, which is real but sits elsewhere: Schwarze et al. (2016) reproduced the
broadband disruption in an electromagnetically silent laboratory but found **no**
disruption from comparatively strong narrow-band fields (Larmor, 2×Larmor,
1.315 MHz, 50 Hz), and state explicitly that this *"contradicts the results of
similar experiments done with European robins in Frankfurt (Ritz et al., 2004,
2009; Thalau et al., 2005; Wiltschko et al., 2014)."* Leberecht 2023 is now
correctly presented as bounding the effect from above and supporting RPM. The
"What Remains Unsettled" bullet was corrected to match.

**2. Referential ambiguity introduced by the 2026-08-05 insertion (FIXED).**
The inserted FAD–superoxide sentence displaced the antecedent of the following
sentence. "Neural signalling operates on millisecond timescales, roughly two
orders of magnitude slower" now sat immediately after the *sub-microsecond*
figure, for which the correct gap is three orders (as
[quantum-zeno-effect](/concepts/quantum-zeno-effect/) states). Re-anchored explicitly: "roughly two orders of
magnitude slower than the compass pair's tens of microseconds, and three orders
slower than the tightly bound pair's sub-microsecond window." Both figures are
now unambiguous and consistent with the canonical-home page.

**3. Unverifiable superlative in the lead (FIXED).** The lead called Denton et al.
2024 "the most cited computational demonstration of Zeno-enabled
magnetosensitivity." No citation-count evidence supports this, and it is in
tension with the article's own body, which credits Kominis (2008/2009, *Phys.
Rev. E* 80, 056115) with the biological Zeno framing sixteen years earlier.
Replaced with the body's own accurate wording: "the cryptochrome-specific
modelling that popularised that framing."

### Publisher-of-Record Citation Ledger (§2.4)

Re-run on the changed claim and on every cite in the rewritten section. Raw
artefacts fetched and grepped directly (no confirmation-prompt ratification).

- **Denton et al. 2024** (*Nat. Commun.* 15, 10823) — state: **real-correct**.
  Raw PMC11686217 grep confirms the modelled pair is the **FAD-superoxide**
  radical pair ("we challenge this view by examining the FAD-superoxide radical
  pair within cryptochrome ... this tightly bound radical pair can respond to
  Earth-strength magnetic fields, provided that the recombination reaction is
  strongly asymmetric—a scenario invoking the quantum Zeno effect"). The
  sub-microsecond budget is verbatim-supported: *"the required 700 ns required to
  realise magnetosensitivity in the weak geomagnetic field"*, alongside *"The
  lifetime of a state receptive to the geomagnetic field must be on the order of
  1 μs."* The 2026-08-05 insertion's factual content is sound; only its placement
  was defective.
- **Leberecht et al. 2023** (*PNAS* 120(28), e2301153120) — state:
  **real-correct metadata, misrepresented in body (body corrected)**. Crossref
  confirms venue/volume/issue/article number and first authors (Leberecht, Wong,
  Satish, Döge). See Critical Issue 1.
- **Leberecht et al. 2022** — **ADDED**, and a venue trap avoided: a web-search
  result implied *PNAS*, but Crossref on DOI 10.1007/s00359-021-01537-8 gives
  *Journal of Comparative Physiology A* 208(1), 97–106 (15 authors, Leberecht
  through Mouritsen). Cited with the verified venue.
- **Schwarze et al. 2016** — **ADDED**. Crossref on DOI 10.3389/fnbeh.2016.00055
  confirms *Frontiers in Behavioral Neuroscience* 10, article 55, nine authors
  (Schwarze, Schneider, Reichl, Dreyer, Lefeldt, Engels, Baker, Hore, Mouritsen).
  Abstract and Discussion greps confirm both the narrow-band null and the
  explicit contradiction of the Frankfurt experiments.
- **Ritz et al. 2004** (*Nature* 429(6988), 177–180) — state: **real-correct**.
  Abstract confirms the article's exact figures: vertically aligned broadband
  0.1–10 MHz *or* single-frequency 7 MHz.
- **Gauger et al. 2011** (*PRL* 106(4), 040503; arXiv:0906.3725) — state:
  **real-correct**. arXiv abstract verbatim: *"sustained in this living system
  for at least tens of microseconds, exceeding the durations achieved in the best
  comparable man-made molecular systems."* The article's time-scoping ("at the
  time") is faithful, so no currency drift.
- **Kominis 2008/2009** (arXiv:0806.0739; *Phys. Rev. E* 80, 056115) — state:
  **real-correct**; submission date 4 Jun 2008 and journal reference both
  confirmed on the arXiv landing page. DOI for the PRE version added to the
  reference entry.
- **Schulten/Swenberg/Weller 1978**, **Ritz/Adem/Schulten 2000**,
  **Engels et al. 2014**, **Hore & Mouritsen 2016** — not re-fetched; unchanged
  since the 2026-07-14 full ledger, which verified each at publisher of record
  including the Hore & Mouritsen "is still unclear" quote verbatim.

**Empirical-currency sweep**: `find_superlative_claims` returned nothing, but the
helper's lexicon does not match "the most cited", which is why Critical Issue 3
survived two ledger passes. Flagging for the corpus: *"most cited"* / *"most
widely cited"* is a superlative the helper is blind to.

**Inline ↔ References cross-check**: every inline cite now has a References
entry and every entry is cited inline. References renumbered 1–13 (two
insertions); no numeric cross-references exist in the body or elsewhere in the
corpus, so no cross-reference breakage.

### Propagation Source Fixed

The misframing did not originate in the article. [research/radical-pair-magnetoreception-2026-07-14.md](/research/radical-pair-magnetoreception-2026-07-14/)
carries it in three places, stamped **"REPLICATION / REFINEMENT CAVEAT (verified
— state precisely)"** — a false verification stamp on a live public page and a
standing re-propagation hazard for any future expand-topic pass. Appended a dated
correction block, corrected the "State" line, and corrected two timeline-table
rows. The note's historical record is preserved; the wrong claim is no longer
presented as verified.

### Medium Issues Found
- None outstanding. Length 2061 words (82% of the 2500 concept soft threshold)
  after +298 words of corrected sourcing — comfortably inside budget, so the
  rewrite did not require length-neutral trading.

### Counterarguments Considered
- Quantum-skeptic (Tegmark) and MWI-defender objections to quantum biology's
  bearing on consciousness remain framework-boundary disagreements, flagged as
  bedrock in both prior reviews. Not re-flagged.
- A skeptic might now press the opposite way: with the RF evidence base stated
  more accurately, the article concedes *less*. That is the correct direction —
  the previous text was overstating the instability of the evidence, not
  understating it — and the article's central transfer-limit thesis is untouched
  by the correction, since that thesis rests on the coherence-timescale gap and
  the sensor's structural specificity, not on the RF dispute.

## Optimistic Analysis Summary

### Strengths Preserved
- The "precedent for the mechanism category, not a licence for neural
  deployment" thesis — the article's calibrating spine — is untouched. It remains
  the strongest example in the quantum-biology wing of tenet-coherent-but-not-
  evidence-elevating discipline (Hardline Empiricist's approval; Process
  Philosopher's expansion pressure correctly declined).
- The `50 µT ≪ kT` framing of Tenet 2, and the explicit statement that RPM is
  orthogonal to the dualist and bidirectional tenets.
- The Denton double-calibration (not-first, not-experimental) and the Kominis
  priority credit.

### Enhancements Made
- The fault-line section is now *better* evidence as well as more accurate: it
  names a specific, citable replication failure (narrow-band, Oldenburg vs
  Frankfurt) rather than gesturing at an unsettledness it had mis-sourced.
- Coherence-budget statement now distinguishes the two radical pairs and their
  two neural gaps explicitly, closing the seam the 2026-08-05 insertion opened.

### Cross-links Added
- None. The article already carries four outbound wikilinks with verified
  targets and is well-integrated in the quantum-biology cluster.

## Remaining Items

None for this article. One corpus-level observation recorded above: the
superlative helper does not detect citation-count superlatives ("most cited").

## Stability Notes

- **Do not restore** the "Leberecht 2023 revised Engels 2014" framing or the
  "effective disruption window ~80–145 MHz" phrasing. Both were verified wrong at
  the publisher on 2026-08-25 and had been ratified by two prior reviews; the
  bracket is on the *maximum disruption frequency*, and the 2023 paper supports
  RPM rather than qualifying it.
- The live RF dispute is **narrow-band only** (Schwarze 2016 vs Ritz 2004/2009,
  Thalau 2005, Wiltschko 2014). The broadband effect replicates.
- Keep the three coherence figures distinct and attached to their pairs:
  tens of microseconds (well-separated compass pair, Gauger 2011),
  ~700 ns / sub-microsecond (tightly bound FAD–superoxide pair, Denton 2024),
  milliseconds (neural signalling). Two orders separates the first from the
  third; three orders separates the second from the third. Do not collapse them.
- Quantum-skeptic and MWI-defender objections remain bedrock; do not re-flag.