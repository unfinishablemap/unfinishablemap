---
title: Pessimistic Review - 2026-06-03 - brain-internal-born-rule-testing
created: 2026-06-03
draft: false
ai_contribution: 100
ai_system: claude-opus-4-8
---

# Pessimistic Review

**Date**: 2026-06-03
**Content reviewed**: [[topics/brain-internal-born-rule-testing]]

## Executive Summary

This is a strongly-calibrated, heavily-reviewed article (deep-reviewed 2026-06-02) whose central
move — answering the "looks unfalsifiable" charge against the corridor reading of Tenet 2 by
cataloguing what would make it empirically *superfluous* rather than overclaiming refutability — is
disciplined and explicitly honours the evidential-status discipline. Its three-way taxonomy
(refutation of related mechanisms / consistency criterion / theoretical supersession) is a genuine
calibration strength, not a weakness. **One genuine medium-severity finding**: a load-bearing
citation gloss attributes to Han & Choi (2016) a result that paper does not establish. All four
high-risk specialist citations (Han & Choi 2016, Torres Alegre 2025 arXiv, Arana 2025 PhilArchive,
Kerskens & López Pérez 2022) were web-verified as genuine with otherwise-accurate metadata.

## Critical Issues

### Issue 1: Han & Choi (2016) supports a different claim than the one attributed to it

- **File**: obsidian/topics/brain-internal-born-rule-testing.md
- **Location**: §"What the Corridor Is" (L55):
  *"by Han and Choi's (2016) result on Born-compliant channels under the no-signalling constraint,
  the per-trial information-theoretic capacity of such channels vanishes asymptotically as the
  number of trials grows, so the channel cannot transmit ensemble-level information without
  violating Born statistics."*
- **Problem**: Web-verified — Han & Choi (2016, *Sci. Rep.* 6:22986; arXiv:1307.2026) derive the
  Born rule from a *strengthened relativistic-causality* condition (stronger than no-signalling for
  binary devices) and bound the upper limit of quantum nonlocality via the probability-assignment
  rule. The paper does **not** prove a result about the *per-trial information-theoretic capacity of
  a selection channel vanishing asymptotically with the number of trials*. That quantitative,
  trials-indexed capacity claim is the article's own inference, presented as Han & Choi's "result."
  The genuine, supportable claim in the vicinity is the qualitative one the very next clause already
  states: Born-deviating probability assignments enable superluminal signalling, so no-signalling
  forces Born compliance (this is also what the article's *other* cite, Torres Alegre 2025, actually
  proves: Φ(p)=p is the unique no-signalling-consistent assignment). The "per-trial capacity
  vanishes asymptotically as trials grow" framing is not in either paper.
- **Severity**: Medium. The article's *conclusion* (a strict selection-only channel transmits no
  ensemble-level information) survives on the qualitative no-signalling argument; only the specific
  quantitative attribution is unsupported. But it is load-bearing dressing — it makes an informal
  corollary look like a proven information-theoretic theorem, which is exactly the
  possibility→theorem upgrade the evidential-status discipline guards against.
- **Recommendation**: `refine-draft` — either (a) downgrade to the qualitative claim the source
  supports ("Han & Choi (2016) show that Born-deviating probability assignments under their
  relativistic-causality condition enable superluminal signalling; a strictly Born-compliant
  selection channel therefore transmits no ensemble-level information"), or (b) if the per-trial
  capacity-vanishing result is wanted, source it to a paper that actually proves it (or mark it as
  the Map's own derived corollary, not Han & Choi's result). Do not assert-fabricated — the cite is
  real; the *gloss of what it proves* is the defect.

## Critiques by Philosopher (brief — most standard attacks are already handled in-text)

### The Empiricist (Popper's Ghost)
The "looks unfalsifiable" charge is the article's explicit subject and is handled with unusual
honesty: it concedes the strict corridor "cannot be directly falsified by Born-rule tests alone,"
distinguishes refutation from motivation-loss, and refuses to claim Popperian foreclosure. No
genuine new finding — the discipline the Popperian would demand is already enforced. The one place
a Popperian retains traction is Issue 1: an over-specified citation gloss makes a corollary look
like a proven theorem.

### The Quantum Skeptic (Tegmark)
Tegmark's 2000 10^-13 s vs 10^-3 s decoherence argument is cited *by name* as the central live
objection (L65, L91) and treated as unresolved-against-Orch-OR rather than waved away. Wiest 2025's
contestation is explicitly marked as disputed by mainstream physics. Already handled.

### The Many-Worlds Defender (Deutsch)
The Tenet-4 subsection (L142) openly concedes the framing is in-Map work conditional on single-
outcome ontology, that MWI "dissolves rather than answers" the question, and that no within-MWI
refutation is available "because the framework boundary is exactly where the disagreement lives."
This is correct framework-boundary marking per direct-refutation-discipline (honest boundary, not
boundary-substitution dressed as refutation). Already handled — no finding.

### Eliminative Materialist / Hard-Nosed Physicalist / Buddhist
Out of scope for this article's specific argument (it is a test-design/falsifiability catalogue, not
a metaphysics-of-qualia piece); the standard rebuttals live in the linked tenet and interface
articles. No new findings.

## Already-Addressed Critiques Dismissed (per standing discipline 1)

- **"Unfalsifiable ⇒ unscientific"** — explicitly the article's subject; handled via the
  superfluity/three-criteria framing. Not re-flagged.
- **"Corridor = epiphenomenalism"** — L101 directly concedes Born-rule indistinguishability from
  epiphenomenalism and cashes the distinction out through causal-structure evidence + disclosed
  metaphysical motivation. Handled.
- **"Quantum-in-warm-brain is dead (Tegmark)"** — cited by name, treated as live and unresolved.
  Handled.
- **MWI dismissal** — handled as framework-boundary, openly disclosed. Handled.
- **Citations look recent/specialist/unverifiable** — four hot-zone cites web-verified GENUINE
  (Han & Choi 2016, Torres Alegre arXiv:2512.12636, Arana 2025 PhilArchive ARATCQ-2, Kerskens &
  López Pérez 2022 JPhysCommun 6:105001). Torres Alegre and Arana correctly flagged in-text as
  pre-publication / phenomenological-not-QM-modification. Only the *interpretation* of Han & Choi is
  defective (Issue 1), not its existence.

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| Han & Choi (2016) prove per-trial channel capacity vanishes asymptotically with trial count | §"What the Corridor Is" (L55) | Source does not establish this; downgrade to the qualitative no-signalling claim or re-source. See Issue 1. |

## Strengths (Brief — preserve during revision)

- The refutation / consistency-criterion / theoretical-supersession trichotomy (L105–113) is a
  model of evidential-status discipline: it refuses to call corridor-consistent nulls "foreclosure"
  and names "motivation-loss vs refutation" as load-bearing.
- Citation hygiene is excellent (pre-publication status flagged on the two preprints; the
  Masanes-Galley-Müller contestation in the literature is disclosed at L63).
- Tenet-4/MWI boundary handled honestly, no boundary-substitution.
- Issue 1 is narrow and surgical — do not let a refine pass disturb the surrounding calibrated prose.
