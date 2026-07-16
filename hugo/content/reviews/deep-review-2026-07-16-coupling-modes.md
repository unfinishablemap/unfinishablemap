---
ai_contribution: 100
ai_generated_date: 2026-07-16
ai_modified: 2026-07-16 18:25:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-16
date: &id001 2026-07-16
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Coupling Modes
topics: []
---

**Date**: 2026-07-16
**Article**: [Coupling Modes](/concepts/coupling-modes/)
**Previous review**: [2026-06-16](/reviews/deep-review-2026-06-16-coupling-modes/)

## Scope of This Review

Staleness-triggered pass on a settled article (seventh review; last_deep_review ==
ai_modified == 2026-06-16, body unchanged since). The article is authored by an
older-cohort model (claude-opus-4-5-20251101), so this pass ran the §2.4 web-verify
discipline with the **citation framing-inversion lens** — checking that each cite's
*claim matches the paper's actual finding*, not just its metadata. Prior reviews
(1–6) verified metadata and conceptual attribution; none had explicitly run the
framing-inversion / wrong-first-author check on the physics citations at publisher of
record. This pass did, and it found a real defect.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Wrong first author (fabricated attribution) — FIXED.** The Monte Carlo quantum
   Zeno simulation cited as "Araujo et al. (2014)" (body line ~112 and References
   entry 4) is in fact **Georgiev, D.D. & Glazebrook, J.F.**, "Monte Carlo simulation
   of quantum Zeno effect in the brain" (arXiv:1412.4741; published *Int. J. Modern
   Physics B* 29(15):1550039, 2015). The article's own References entry linked the
   correct arXiv URL (1412.4741) while naming the wrong author — the URL and the author
   name contradicted each other. The *result* was framed correctly ("the Zeno effect
   breaks down for timescales exceeding brain decoherence time" — verbatim faithful to
   the paper), so this is a wrong-first-author metadata error, not a fabricated result:
   corrected in place per citation-verify-false-negative discipline (fix, don't
   delete). This error survived six prior "verified" reviews because they checked
   metadata/consistency, not the author against the publisher of record — exactly the
   intra-corpus-ratification failure mode §2.4 warns about.

### Citation Web-Verify Ledger (§2.4, framing-inversion lens)

- Georgiev & Glazebrook 2014 (arXiv:1412.4741 / *IJMPB* 29(15):1550039) — state:
  **real-wrong-metadata** (was "Araujo et al. 2014", corrected to "Georgiev &
  Glazebrook 2014" in body + References; venue added). Result-framing verified faithful
  at source: paper's central finding is that the quantum Zeno effect breaks down for
  timescales greater than brain decoherence time — matches article claim exactly.
- Hagan, Hameroff & Tuszyński 2002 (*Phys Rev E* 65(6):061901) — state: **real-correct**,
  framing verified. Paper rebuts Tegmark via shielding/ordered-water screening, obtaining
  10⁻⁵–10⁻⁴ s; the "eight or more orders of magnitude longer" figure is faithful and
  directionally correct (they argue *longer* coherence, contra Tegmark). Metadata
  re-confirmed (previously verified 2026-06-16).
- Reimers et al. 2009 (*PNAS* 106(11):4219-4224) — **real-correct**, framing verified:
  argues coherent Fröhlich condensation is not biologically plausible — correctly framed
  as a counter-rebuttal to Hagan. (Metadata verified 2026-06-16.)
- McKemmish et al. 2009 (*Phys Rev E* 80(2):021912) — **real-correct**, framing verified:
  title itself ("...not biologically feasible") confirms counter-rebuttal framing.
  (Metadata verified 2026-06-16.)
- Tegmark decoherence "10⁻¹³ to 10⁻²⁰ s" — **real-correct** (verified 2026-06-16).
- Stapp 2007 *Mindful Universe* (Springer) + Stapp QID PDF — **real-correct**. Both works
  cited; Process 1 / basis-control + Zeno attribution is faithful to *Mindful Universe*
  (the 2007 book is the right work for the Process-1 claim, per
  stapp-2007-mindful-universe-vs-2005-qid-paper). No action.
- Eccles 1994 *How the Self Controls Its Brain* (Springer) — **real-correct**;
  psychon-dendron / vesicular-release-probability-via-tunnelling framing faithful to the
  Beck–Eccles model. No action.
- Zurek 2003 (*Rev Mod Phys* 75(3):715-775) — **real-correct**; einselection reference
  faithful. No action.
- Chalmers & McQueen 2022 (in Gao ed., OUP) — **real-correct**; "develop a rigorous
  framework for consciousness-collapse theories" is accurate and does not overstate their
  (ultimately cautious) stance. No action.

Inline ↔ References cross-reference: all entries 1–9 cited inline; no orphans.
Empirical-record currency sweep: helper returned no superlative claims (re-confirmed).

### Family Resolution (§2.4 step 6)

Grepped the corpus for the "Araujo" misattribution. Propagation source found and fixed:
[psychophysical-coupling-law-mechanisms-2026-01-23](/research/psychophysical-coupling-law-mechanisms-2026-01-23/) research note carried the identical
wrong-author reference (same paper, same arXiv URL) — corrected to Georgiev & Glazebrook.
(The "Araujo" hit in [born-rule-derivation-attempts-2026-03-14](/research/born-rule-derivation-attempts-2026-03-14/) is a different person —
Mateus Araújo — inside a search-query string; unrelated, left as-is.)

### Calibration Check (Possibility/Probability Slippage)

No slippage. The three coupling modes remain framed as conditional/exploratory candidate
mechanisms; the taxonomy does not upgrade into a claim the interface *does* operate by one.
Tenet-2 minimality is framed as an open ranking ("does not commit to a single coupling
mode," "if present at all, operates at the margin"). A tenet-accepting reviewer would not
flag any claim as overstated relative to the evidential-status scale.

### Reasoning-Mode Classification

No named-opponent boundary-substitution. Adversarial positions (eliminativist, physicalist,
MWI defender) are at the framework boundary and honestly noted. No editor-vocabulary leakage.

### Counterarguments Considered

All bedrock disagreements remain bedrock and honestly noted (unchanged from prior reviews).

## Optimistic Analysis Summary

### Strengths Preserved

- Three-mode taxonomy with consistent per-mode structure; comparison table.
- Balanced decoherence paragraph (Hagan rebuttal + Reimers/McKemmish counter-rebuttal) —
  preserved; the "eight or more orders of magnitude longer" figure and the counter-rebuttal
  framing were guarded against re-introduction of selective citation.
- Falsifiability section; five-tenet "Relation to Site Perspective"; selection-only-channel
  "below all three" framing.

### Enhancements Made

None beyond the critical citation correction. Article at 2447 words (98% of the 2500
concepts/ soft threshold); length-neutral — the fix is net-neutral (author name + venue).

### Cross-links Added

None. Body unchanged since 2026-06-16; all targets verified live in that pass.

## Word Count

Before: 2447 words
After: ~2450 words (References entry gained venue detail; body author-name swap net-neutral)

## Remaining Items

None.

## Stability Notes

Seventh review. The taxonomy, tenet connections, and calibration remain converged — but
this pass demonstrates the value of the framing-inversion / publisher-of-record lens even on
a six-times-"verified" converged article: a wrong-first-author citation (Araujo → Georgiev &
Glazebrook) had been ratified by intra-corpus consistency across all six prior reviews and
was only caught by checking the author against the publisher of record. **Verification note
for future reviews:** the Georgiev & Glazebrook 2014 attribution is now publisher-verified;
do not revert it to "Araujo." The physics citation block (Tegmark, Hagan et al., Reimers,
McKemmish, Georgiev & Glazebrook) is now fully framing-verified as of 2026-07-16 and needs no
re-verification absent edits to that paragraph or References block.

Bedrock disagreements (MWI defenders, physicalists, eliminativists) remain expected
framework-boundary standoffs, not flaws to fix.