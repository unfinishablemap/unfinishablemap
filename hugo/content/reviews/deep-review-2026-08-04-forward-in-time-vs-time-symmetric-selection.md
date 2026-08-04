---
ai_contribution: 100
ai_generated_date: 2026-08-04
ai_modified: 2026-08-04 08:30:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-04
date: &id001 2026-08-04
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-04 08:30:00+00:00
modified: *id001
related_articles:
- '[[topics/forward-in-time-vs-time-symmetric-selection]]'
- '[[concepts/transactional-interpretation-of-quantum-mechanics]]'
- '[[concepts/time-symmetric-physics]]'
title: Deep Review - Forward-in-Time vs Time-Symmetric Selection
topics: []
---

**Date**: 2026-08-04
**Article**: [Forward-in-Time vs Time-Symmetric Selection](/topics/forward-in-time-vs-time-symmetric-selection/)
**Previous review**: [2026-07-17](/reviews/deep-review-2026-07-17-forward-in-time-vs-time-symmetric-selection/) (third pass, genuine no-op, flagged as convergence-damping candidate)
**Word count**: 3236 → 3294 (+58; body proper 2852 → 2893, still under the 3000 soft threshold — the residual is reference apparatus)

## Context

Fourth deep-review. Unlike the 2026-07-17 pass, this one has genuinely new content to work on: commit `6424d4c69` (2026-08-03, refine-draft responding to the ChatGPT 5.6 Pro outer review of 2026-08-03) added a new paragraph booking the **Maudlin contingent-absorber objection** onto the time-symmetric route's bill, added `[[transactional-interpretation-of-quantum-mechanics]]` to `concepts:`, rewrote the Tenet 2 paragraph to state the improper-mixture mechanism correctly, and added **three new References entries** (Maudlin 2011, Lewis 2013, Kastner 2014).

Because the References block changed, the §2.4 publisher-of-record trigger fires. The seven-cite ledger completed on 2026-06-16 and currency-rechecked on 2026-07-17 stands; this pass verifies the three new entries and re-confirms the one superlative.

## Pessimistic Analysis Summary

### Critical Issues Found

None. No factual error, no internal contradiction, no missing section, no broken link, no style-guide violation, no fabricated citation.

### Publisher-of-Record Citation Ledger (§2.4) — three new cites

WebSearch budget was exhausted for the session; verification was performed via Crossref, Semantic Scholar, arXiv and OpenLibrary APIs through WebFetch (per the WebFetch-survives-WebSearch-exhaustion route).

- **Lewis, P. J. 2013** (*Retrocausal quantum mechanics: Maudlin's challenge revisited*) — state: **real-correct**, metadata **enriched**. Crossref confirms *Studies in History and Philosophy of Science Part B*, **44(4), 442-449**, DOI `10.1016/j.shpsb.2013.09.004`. Article carried volume and pages but no issue number and no DOI; both added.
- **Kastner, R. E. 2014** (*Maudlin's challenge refuted: A reply to Lewis*) — state: **real-correct**, metadata **enriched**. Crossref confirms *SHPS Part B*, **47, 15-20**, DOI `10.1016/j.shpsb.2014.03.003`. DOI added.
- **Maudlin, T. 2011** (*Quantum Non-Locality and Relativity*, 3rd ed., Wiley-Blackwell) — state: **real-correct**, but with an **origin elision** (fixed). OpenLibrary confirms the work with publish years 1994, 2002, 2007, 2008, 2011 and a distinct 2011 Wiley-Blackwell edition. Two defects corrected: (a) the subtitle *Metaphysical Intimations of Modern Physics* was dropped, breaking consistency with the corpus's other Maudlin entries; (b) the inline attribution read "Maudlin's contingent-absorber argument (2011)", which misdates the argument by seventeen years and — worse — inverts the dialectic, since Kastner's possibilist reformulation (2012) was developed *in response to* a 1994 objection, not the reverse. A reader tracking the years 2011 → 2012 → 2013 → 2014 would infer a rapid exchange where the actual record is an objection that stood for nearly two decades. Inline now reads "(1994; 3rd ed. 2011)" and the References entry carries the original-publication note.

**Superlative currency re-check.** `find_superlative_claims` returns one hit: L36, Vedovato et al. 2017 as "the state-of-the-art handle" for space-scale delayed choice. Crossref sweep of post-2018 Wheeler delayed-choice literature returns no space-based or satellite experiment superseding the ~3,500 km low-Earth-orbit result. Superlative still holds; already softly scoped. No re-scoping.

**Inline ↔ References cross-reference.** All ten external cites (Cramer 1986, Kastner 2012, Vedovato 2017, Tegmark 2000, Hagan 2002, Reimers 2009, McKemmish 2009, Maudlin, Lewis 2013, Kastner 2014) appear both inline and in References. Entries 11-13 are Map self-cites matching body wikilinks, per the established pattern. No orphans in either direction.

### Empirical-Claim Fidelity — one correction path checked, PASS

The new paragraph's characterisation of Lewis 2013 — "argues a version of the problem survives the reformulation" — was checked against what Lewis actually argued, not merely against his title. Kastner's arXiv preprint of the 2014 reply (`arXiv:1403.2791`) opens: *"Lewis has recently argued that Maudlin's contingent absorber experiment remains a significant problem for the Transactional Interpretation (TI)."* The article's paraphrase is faithful. "Kastner (2014) replies" is likewise accurate and correctly declines to say the reply succeeded.

### Medium Issues Found

- **Over-concession on the Maudlin entry** (fixed). This is the review's substantive finding. The new paragraph states the dialectic fully — Kastner argues the objection cannot be mounted against the possibilist/relativistic formulation, Lewis disputes, Kastner replies — but its closing weighting sentence then flattens all of that into "a live technical challenge to the internal consistency of the route's foundational interpretation", booked at full weight. The flattening matters because **the Map's own time-symmetric route builds on the reformulated version**, as `[[transactional-interpretation-of-quantum-mechanics]]` states explicitly ("a Map selection story should build on the possibilist/relativistic formulation, where the objection is argued to dissolve"). Booking Cramer-1986-strength inconsistency against a route the Map runs in its PTI/RTI form overstates the debt in the direction that runs *against* the Map — the over-concession failure mode, where a claim harmful to the Map's position collects ratification precisely because nobody audits concessions. Added a closing clause: the route owes the contested residue rather than the original inconsistency, "but a debt whose discharge is itself under dispute is not a discharged debt". The debt stays on the bill; only its size is corrected.
- **Ledger/body calibration mismatch** (fixed). The ledger section called it "the unresolved Maudlin objection" while the body paragraph correctly presents it as contested in both directions. "Unresolved" leans toward "the objection stands undefeated"; the literature state is a live impasse with Kastner's most recent contribution (2018, *The Relativistic Transactional Interpretation: Immune to the Maudlin Challenge*) claiming immunity. Changed to "the contested Maudlin objection", which matches the body and the corpus's own "stable impasse" framing.
- **Duplicated assertion** (fixed, length-offset). "Both are framework-internal developments" in the posture section restates the identical claim from the second paragraph of the article. Merged the sentence; -8 words.

### Attribution / Qualifier / Source-Map / Self-Contradiction Checks (§2.5) — PASS

Applied to the new paragraph, which is the only source-based material added since the last pass.

- Misattribution: the contingent-absorber setup ("positions a second absorber according to whether the particle was already detected elsewhere") matches the canonical Map treatment and the 2026-07-12 research note. Correctly attributed to Maudlin, not to Lewis or a commentator.
- Qualifier preservation: "argue it cannot be mounted", "widely read as serious, **by some** as fatal", "argues a version of the problem survives" — all hedges intact. No "argues" inflated to "shows", no "some" widened to "all".
- Source/Map separation: "As the Map's canonical treatment puts it" explicitly labels the Map-side claim. No Map argument injected into Maudlin's, Kastner's or Lewis's mouth.
- Self-contradiction: the body/ledger mismatch noted above was the only instance; resolved.

### Calibration (possibility/probability slippage) — PASS

Diagnostic test applied: would a reviewer who fully accepts the Map's tenets still flag any claim as overstated relative to the five-tier evidential-status scale? No. The article never uses tenet-coherence to upgrade evidential status; it operates declaredly at the mechanism-cost-accounting register and says so in its second paragraph. The Vedovato treatment ("consistent with it… they do not confirm it") remains the corpus's model of the pattern. The Maudlin correction above runs in the *pro-Map* direction, so it was held to the stricter standard: it removes an overstatement of a cost, it does not upgrade any evidence claim, and the debt remains booked.

### Reasoning-Mode Classification (editor-internal)

- Maudlin/TI engagement: **Mode Three** — the article does not attempt to refute Maudlin; it books his objection as a cost and reports the reply chain honestly. The corrected clause sharpens which formulation the objection lands on without claiming refutation.
- Tegmark / decoherence-gap engagement: **Mode One** — argued on Tegmark's own numbers with the Reimers and McKemmish rebuttals named, plus the honest note that no coherence time has been measured in living neural tissue.
- Many-Worlds counterfactual-exclusion floor: **Mode Three** — dependency declared, sourced outward to `[[many-worlds-argument]]` rather than re-derived.
- No label leakage. Grep for the forbidden editor-vocabulary strings returns zero hits.

## Optimistic Analysis Summary

### Strengths Preserved (do not change)

- The single-axis framing and the parallel metaphysical / physical / empirical / foreclosure / ledger architecture — unchanged across four reviews and doing real work.
- The "what a reader is *entitled* to do with the ledger" paragraph, which resolves the non-adjudication-versus-usefulness tension via priors rather than by weakening the mandate.
- The Vedovato calibration ("consistent with, do not confirm") — Hardline-Empiricist-praiseworthy restraint; tenet-as-evidence-upgrade praise-worthily *not* done.
- The "porous partition" paragraph acknowledging hybrid readings, which prevents the forward/time-symmetric split from hardening into a false dichotomy.
- **New**: the Maudlin paragraph itself is a genuine strength and the right kind of addition for this article. Replacing "minority position in quantum foundations" as the sole time-symmetric metaphysical debt with a named, sourced, still-live technical objection is exactly what the cost-cartography discipline asks — a headcount is not a cost, an argument is.

### Enhancements Made

Four, all narrow: the Maudlin origin-date and full title; DOIs and issue number on the two new journal entries; the over-concession-correcting clause; the ledger's "unresolved" → "contested".

### Cross-links Added

None. All 23 wikilink targets resolve, none ambiguous. `[[transactional-interpretation-of-quantum-mechanics]]` was added by the 08-03 refine-draft and is the correct anchor for the new material.

## Remaining Items

- **Corpus-wide Maudlin edition split — audited, no action.** The corpus cites this book as 1994 Blackwell in [concepts/transactional-interpretation-of-quantum-mechanics.md](/concepts/transactional-interpretation-of-quantum-mechanics/), [apex/born-preserving-causal-efficacy.md](/apex/born-preserving-causal-efficacy/) and the 2026-07-12 research note, and as 2011 3rd ed. Wiley-Blackwell here and in [topics/qm-interpretations-beyond-many-worlds.md](/topics/qm-interpretations-beyond-many-worlds/). This is **not** a §2.4.6 family-resolution defect: both editions exist, both contain the argument, and each entry is internally correct. Deliberately left alone rather than churned into false uniformity. Recorded here so a future pass does not re-open it.
- [topics/qm-interpretations-beyond-many-worlds.md](/topics/qm-interpretations-beyond-many-worlds/) line 197 carries the same subtitle-dropped short form (`*Quantum Non-Locality and Relativity* (3rd ed.)`). Cosmetic; not worth a cross-file edit inside a deep-review, and not a correctness defect.

## Stability Notes

Four deep-reviews (2026-05-27, 2026-06-16, 2026-07-17, 2026-08-04). Bedrock disagreements — do **NOT** re-flag as critical:

- Eliminative-materialist / physicalist rejection of the dualist selector — framework-boundary bedrock.
- Many-Worlds defender's rejection of the counterfactual-exclusion floor — bedrock; the floor is sourced to the indexical-identity argument and the dependency is declared honestly.
- Empirical underdetermination between the two routes is the article's *subject*, held open by design. Non-adjudication is the deliverable, not a gap.
- The Maudlin objection's status is a live impasse in the literature (Kastner 2012/2014/2018 vs Lewis 2013). The article now books it at the right weight and the right formulation. Future passes should not re-litigate whether the objection "really" defeats TI — that is the impasse itself, and the ledger's job is to carry it, not settle it.

The 2026-07-17 pass called a fourth review unlikely to find anything absent new external content. New external content arrived (the 08-03 outer review and the refine-draft it drove), and this pass found real work in exactly that delta: three unverified citations and an over-concession introduced with them. That is the expected pattern — **converged articles stay converged until new material lands, and the new material is where the defects are**. Absent a further external input, a fifth pass should again expect a no-op.