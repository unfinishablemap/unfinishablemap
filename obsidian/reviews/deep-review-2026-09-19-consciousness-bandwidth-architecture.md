---
title: "Deep Review - Consciousness Bandwidth Architecture"
created: 2026-09-19
modified: 2026-09-19
human_modified: null
ai_modified: 2026-09-19T07:12:06+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-19
last_curated: null
---

**Date**: 2026-09-19
**Article**: [[consciousness-bandwidth-architecture|Consciousness Bandwidth Architecture]]
**Previous review**: [[deep-review-2026-07-25-consciousness-bandwidth-architecture|2026-07-25]] (no-op) · [[deep-review-2026-07-11-consciousness-bandwidth-architecture|2026-07-11]] (full publisher-of-record verify) · [[deep-review-2026-06-06-consciousness-bandwidth-architecture|2026-06-06]] · [[deep-review-2026-05-26-consciousness-bandwidth-architecture|2026-05-26]]
**Selection rationale**: 5th review, driver-assigned. `last_deep_review` 2026-07-25, `ai_modified` 2026-08-17 — three weeks of drift unseen by any review, and the sibling [[bandwidth-of-consciousness]] was itself amended on 2026-08-17 in a way that bears directly on this article's tenet section.

**Length budget**: 3489 → **3490** words (concepts soft 2500 / hard 3500; gate fires at `>= 3500`, so the ceiling is 3499). Net **+1**. Every fix was swap- or trim-shaped; two repairs were paid for by a deletion. 9 words of margin remain (3490 of a 3499 ceiling). No condense task warranted or minted.

## Cross-Article Claim-Fidelity Lens (PRIORITY 1) — 2 CRITICAL, both fixed

This pair has a documented history of contradicting each other (commit `801eaaa68e`, epiphenomenalism). It fired twice more.

### CRITICAL 1 — rate→grain over-derivation in the Minimal Quantum Interaction tenet (fixed)

The sibling was amended on 2026-08-17 (`df71b72807`) to establish, at `topics/bandwidth-of-consciousness` L169:

> The ~10 bits/s figure is *behavioural* throughput, and **rate does not fix grain: one bit selects among arbitrarily complex prepared policies.** … Pattern-level selection … is the interface model's commitment; **consistency with Minimal Quantum Interaction falls short of establishing it.**

This article asserted the exact inference the sibling disowns, and in the stronger direction:

> ~~Minimality is not merely a philosophical preference—the bandwidth constraint *requires* it. A 10-bit/second conscious channel cannot perform large-scale causal intervention. It can perform small-scale selection among prepared alternatives. The tenet and the empirical constraint converge.~~

Two defects in one passage. (a) It derives a bound on the *scale/grain* of intervention from a bound on *rate* — invalid on the sibling's own reasoning, since one bit can select among arbitrarily complex prepared policies, so a low-rate channel is not thereby a small-effect channel. (b) It runs a measurement→tenet *entailment* ("requires", "converge") where the corpus's adjudicated position is consistency-without-establishment. This is a calibration error inside the Map's framework, not a bedrock disagreement: a fully tenet-accepting reviewer flags it, and the article's own in-house standard three sections earlier ("What the figure does is make the epiphenomenal story *less parsimonious*") is the measure it fails.

Repaired to:

> The bandwidth constraint fits minimality without establishing it. Rate does not fix grain—one bit can select among arbitrarily complex prepared policies—so ~10 bits/second bounds how often consciousness selects, not the scale of each selection.

Net −1 word. This also retires a variant of the CLAUDE.md-flagged "cannot X. It can Y." construct.

### CRITICAL 2 — withdrawn discriminator still live in the Dualism tenet (fixed)

The sibling's Global Workspace Objection section records a withdrawal that runs against the Map's own interest:

> The feature the filter reading treats as its natural fit—that the bottleneck sits at conscious access rather than at sensory transduction or motor output—is exactly what GWT makes its *defining* feature. A datum both accounts predict cannot adjudicate between them, and **the Map has accordingly withdrawn the bandwidth argument as a discriminator**.

This article's Dualism paragraph still ran the withdrawn leg: "the specific location of the constraint at conscious access … is more naturally predicted by a view that treats the two directions as different kinds of process." Repaired to concede location explicitly and retain only the surviving leg (the inbound/outbound asymmetry), which is also what this article's own "Implications for Interface Models" section already identifies as GWT's residual puzzle. Net +9.

**Not a contradiction (checked, cleared)**: `Filter models` L109 says the asymmetry is *accommodated* naturally — the sibling's own word is "accommodation, not discrimination", so this is consistent. L93's "roughly 3–4 selections per second" is corpus-consistent: the sibling derives it explicitly at its Temporal Grain section from ~3 bits per selection. L79's enumeration argument is stated conditionally and survives "rate does not fix grain". L127–129's epiphenomenalism paragraph matches the sibling near-verbatim — the 2026-08 amendment did not disturb it.

## Publisher-of-Record Citation Ledger (PRIORITY 2)

Re-verified this pass at the publisher: the three load-bearing 2025/2016 cites plus the one empirical figure the article stated without a source. The pre-2010 canonical layer carries forward from the 2026-05-26 primary-source ledger and the 2026-07-11 full verify; metadata does not drift.

- Sauerbrei, B.A. & Pruszynski, J.A. 2025, *Nat Neurosci* **28(7):1365–1366**, "The brain works at more than 10 bits per second", DOI 10.1038/s41593-025-01997-0 — **real-correct** (Crossref + Semantic Scholar + PMC12320479 full text). **Stance check passed**: the driver's concern that the Map might be enlisting a paper that rejects the claim is a *false alarm*. Verbatim abstract: *"Although this speed limit appears to hold for high-level cognitive functions, we argue that unconscious processing for real-time control of movement … substantially exceeds this limit."* Their target is the *whole-human upper-bound* reading ("The 10 bits/s speed limit, then, is a lower bound, not an upper bound, on the maximum information throughput of an entire human"), which this article never asserts — it attributes the high throughput to the brain's side of the interface. One over-claim fixed: article said S&P "**demonstrates**" the motor point; they write "we argue". Changed to "argues" (0 words).
- Sauerbrei & Pruszynski empirical detail — **real-correct**, verified against PMC full text: 250 ms stride ✓ ("the total output of our runner's nervous system over an entire 250 ms stride could be described with approximately three binary bits. However, the phase, amplitude, and duty cycle for even a single muscle … cannot be specified with only three bits"); "dozens of muscles" ✓; cerebellum "about half the neurons in the brain" ✓.
- **"Individual neurons transmit ~200 bits per second" — FABRICATED PRECISION + DROPPED QUALIFIER + MISATTRIBUTION. REMOVED.** Three independent faults. (1) The number is absent from Sauerbrei & Pruszynski at any magnitude — the sentence sat inside the S&P paragraph with no other anchor, so it read as theirs. (2) Zheng & Meister's actual sentence is *"The example of retinal ganglion cells suggests that when driven to high firing rates, individual neurons **may** transmit **hundreds** of bits per second"* — a hedged, qualifier-bound claim about hard-driven retinal cells. Their *typical* cortical figure is the opposite of the article's: *"even under those conditions, a single neuron will transmit ~10 bits/s."* (3) "~200" is a Map-internal back-of-envelope, visible in the archived predecessor as "(Zheng and Meister 2025, based on ~2 bits per spike at ~100 spikes per second)" — the coalesce into this article dropped the parenthetical and left the derived number wearing S&P's authority.
  **Precedent**: this exact clause was already adjudicated and *deleted* from the sibling on 2026-06-26 (changelog W26: *"removed the '~200 bits/neuron' clause and its Sauerbrei & Pruszynski attribution entirely — two full-text PMC fetches confirm NO per-neuron bit-rate at any magnitude is in that paper"*). The fix was applied by file and the string sibling here stayed live — [[fix-by-file-leaves-string-siblings-live]] — surviving a full publisher-of-record verify on 2026-07-11 and a no-op pass on 2026-07-25, because metadata verification does not touch an unattributed in-body figure ([[empirical-claim-fidelity-orthogonal-to-metadata-and-quotes]]). Removal (not repair) follows the adjudicated precedent; the "substrate runs far above the conscious ceiling" point is already carried by the cerebellum sentence. −7 words, which paid for both tenet repairs.
- Zheng, J. & Meister, M. 2025, *Neuron* **113(2):192–204** — **real-correct**; verified afresh against arXiv 2408.10234v2 full text this pass (not carried). "Sifting number" term and the *"largest unexplained number in brain science"* quote re-confirmed in the raw source by grep, not by prior-review certification ([[quote-must-be-grep-verifiable-in-raw-source]]).
- Wu, T., Dufford, A.J., Mackie, M.-A., Egan, L.J. & Fan, J. 2016, *Sci Rep* 6:34025 — **real-correct**; ~3–4 bits/s cognitive-control finding used correctly, and used consistently with the sibling. The 2026-05-26 Wu-vs-Musslick author correction has held.
- Canonical layer (Zimmermann 1986, Nørretranders 1998, Hick 1952, Hyman 1953, Miller 1956, Baars 1988, Dehaene & Naccache 2001, Kim 2005, Stapp 2007 *Mindful Universe* — title-disambiguated, NOT the 2005 QID paper — Mandik 2010, Block 2011, Coupé et al. 2019, Cohen/Dennett/Kanwisher 2016) — **real-correct**, carried from the 2026-05-26 primary-source ledger and 2026-07-11 re-verify.

**Inline ↔ References cross-check**: clean in both directions, programmatically. 16 entries, zero orphans either way.

**Currency sweep**: one superlative (`to date`, Evolutionary Puzzle) — appropriately scoped as a current-measurement claim with cross-species data explicitly flagged sparse. No [[empirical-record-currency-drift]] defect. The live 2025 dispute (S&P) concerns whole-brain scope, not the conscious-access ceiling, and the article already handles it.

## Lenses Run — Clean Returns

- **Attribution accuracy (§2.5)**: clean apart from the two citation fixes above. Source/Map separation holds — Stapp's Zeno proposal is marked "one proposed mechanism … whether this specific mechanism works remains contested"; the hierarchical-selection resolution is labelled the Map's throughout.
- **Reasoning-mode / label leakage (§2.6)**: **no leakage** (grepped for all seven forbidden editor labels — zero hits). GWT (Baars/Dehaene) Mode Three, now *more* honestly so after the Dualism repair. Identity response: Mode Three, boundary declared ("for dualists … identity is unavailable by definition"). Epiphenomenalism: Mode Three with an explicit concession that the measurement carries no traction.
- **Internal contradiction**: clean. The Dualism repair removed the one live tension with the article's own Interface Models section.
- **Possibility/probability slippage (§2)**: the MQI passage *was* the slippage instance (tenet-coherence read as derivation) and is fixed. No other instance; the interactionist "prediction rather than puzzle" framing remains bounded by "the asymmetry alone does not decide between them".
- **Structure / style**: front-loaded lead intact, "Relation to Site Perspective" substantive across all five tenets, `description` present, no QEC-notation hazard, EOF clean.

## Optimistic Analysis Summary

### Strengths Preserved (do not churn)
- The 10⁹:10 "two faces" lead; capacity/grain/format decomposition; the "Distinguishing the Challenges" table; the Two Failed Alternatives pair; the honest epiphenomenalism paragraph, which is the in-house calibration standard the MQI fix was measured against.

### Enhancements Made
- None additive. At 3490/3499 the article has no expansion budget; both tenet repairs were paid for by the removed fabricated figure.

### Cross-links Added
- None. Link inventory unchanged.

## Remaining Items

**Archive-tree string siblings of the removed defect (out of scope for this file, not minted here).** The `~200 bits/neuron` clause is still live in two archived articles, which render at live URLs and are visible to the machine-metadata surface ([[noindex-does-not-suppress-the-machine-metadata-surface]], [[outer-reviewers-critique-archived-articles-at-live-urls]]):

- `archive/concepts/asymmetric-bandwidth-consciousness.md` L52 — carries the clause *with* its self-disclosing parenthetical, so it is the least harmful instance.
- `archive/topics/the-ten-bit-ceiling.md` L69 — worst instance: "individual neurons transmit around 200 bits per second **at typical firing rates**", attributed to Zheng and Meister. The qualifier is *inverted* — Zheng & Meister give ~10 bits/s at typical cortical rates and "hundreds" only when driven hard.
- `hugo/content/research/bandwidth-constraints-10-bits-2026-03-29.md` L109 — the research note that seeded the figure, stating the ~2 bits/spike × ~100 spikes/s derivation.

These need a corpus sweep rather than a single-file task; flagged for the driver to queue against the archive tree.

## Stability Notes

- **Not converged after all.** Four prior reviews classified this article as converged and the last two were no-op-class; this pass found two critical cross-article calibration defects and one fabricated empirical figure. The lens that found all three is *cross-article claim fidelity against a sibling amended after the last review* — a lens no prior pass on this file ran, and one that convergence damping actively suppresses. A convergence nomination marks an unrun lens, not a clean file.
- **Bedrock disagreements — do NOT re-flag as critical**: MWI proponents find the "No Many Worlds" connection thin; eliminative materialists and hard physicalists reject the behavioural→conscious-bandwidth interpretive step from outside the Map's tenets. Framework-boundary standoffs.
- **Scope limit on the above (per §2.9)**: the stability note covers the *framework commitment* only. The *empirical-support claims* attached to it — every citation, every figure, and the article's agreement with its sibling — stay reviewable every pass. The ~200 bits/neuron figure survived four reviews precisely because it sat under an over-broad stability umbrella.
- **Standing instruction for the next review of either file**: diff `topics/bandwidth-of-consciousness` against this article before anything else. Three separate contradictions have now been found on this pair (epiphenomenalism `801eaaa68e`; rate→grain and the withdrawn discriminator, this pass). Treat the sibling's most recent amendment as the authority.
- **Length**: 3490/3499. The next cross-link install or any addition over 9 words must be paid for by a trim.
