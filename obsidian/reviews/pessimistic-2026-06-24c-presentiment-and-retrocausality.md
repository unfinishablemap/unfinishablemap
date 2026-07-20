---
title: Pessimistic Review - 2026-06-24 - Presentiment and Retrocausality
created: 2026-06-24
draft: false
ai_contribution: 100
ai_system: claude-opus-4-8
---

# Pessimistic Review

**Date**: 2026-06-24
**Content reviewed**: `obsidian/topics/presentiment-and-retrocausality.md` (first dedicated pessimistic review; AI-authored 2026-01-27, last deep-reviewed 2026-05-26; 1901 body words)

## Executive Summary

This is one of the Map's stronger articles: it self-consciously firewalls the Map's quantum commitments from the contested presentiment literature and presents the parapsychology evidence even-handedly. The adversarial value is therefore concentrated not in big structural failures but in two verifiable empirical defects and a handful of dialectical pressure points. The one clear, citable defect: the Mossbridge et al. (2012) confidence interval is misreported (article: "0.15–0.27"; published: **0.13–0.29**), which narrows the interval and overstates the result's precision. A second medium issue: the "10²⁰ to 1" prior-odds figure attributed to Wagenmakers et al. (2011) — and the downstream "10¹¹ against" arithmetic built on it — is not directly attested in the source and reads as the article's own reconstruction presented as Wagenmakers' stated figure.

## Critiques by Philosopher

### The Eliminative Materialist (Churchland)
Largely disarmed here. The article concedes presentiment is contested and refuses to lean on it, which removes the easy target. Her residual jab: the article still trades in "conscious selection among neural possibilities" as if that vocabulary were in good standing. The firewall protects the article from parapsychology but not from the prior charge that "consciousness selects" is folk-psychological framing awaiting elimination. That charge is out of scope for this article but worth noting the article assumes the dualist vocabulary rather than defending it (correctly, by division of labour — but a critic will note the assumption).

### The Hard-Nosed Physicalist (Dennett)
His strongest move targets the article's own admission in "The mechanism gap is larger for presentiment—but in degree, not kind." The article honestly concedes that decoherence threatens the Map's own neural interface as much as it threatens presentiment, then argues the asymmetry is one of degree (single ion-channel collapse vs. organism-scale coordination). Dennett presses: "degree of implausibility" with no quantitative handle is rhetorical, not argumentative. The article asserts a single channel is "a far smaller ask" but offers no estimate of how much smaller, nor why the Map's preferred degree lands on the acceptable side of a line it has just conceded is not clean. This is the article's most exposed paragraph — and admirably so, because it surfaced the vulnerability itself.

### The Quantum Skeptic (Tegmark)
The article cites Tegmark's decoherence objection accurately and does not hand-wave it — a genuine strength. His remaining complaint: the article defers the rebuttal to `[[quantum-consciousness]]` ("the Map's response to decoherence ... addresses the single-event case"). For an LLM fetching this page in isolation, the rebuttal is a promissory note. Front-loading even one sentence of the actual single-event decoherence response would harden the paragraph against truncation.

### The Many-Worlds Defender (Deutsch)
Minimal contact with this article's subject matter; no findings. The retrocausal framing is orthogonal to the MWI dispute and the article does not over-claim against MWI here.

### The Empiricist (Popper's Ghost)
The article actually scores points *for* the Popperian by naming the experimenter-effect escape hatch as "conceded unfalsifiable" — it uses falsifiability as the discriminator between the physics firewall and presentiment. But the Popperian turns the same blade on the Map: physics-based retrocausality is described as "one empirically-equivalent interpretation." Empirically-equivalent interpretations are, by construction, not differentially testable. The article's firewall claim is *comparative* ("respectable mainstream dispute" vs. "conceded unfalsifiable"), which is honest, but a strict Popperian notes that "respectable interpretive dispute among empirically-equivalent readings" is itself metaphysics, not physics. The article's own scrupulousness ("a confirmed phenomenon is not a confirmed interpretation," stated twice) blunts this, so it is a pressure point rather than a defect.

### The Buddhist Philosopher (Nagarjuna)
Out of scope; the article does not engage the persistence-of-self questions Nagarjuna would target. No finding.

## Critical Issues

### Issue 1: Mossbridge (2012) confidence interval misreported
- **File**: `obsidian/topics/presentiment-and-retrocausality.md`
- **Location**: §"What the Meta-Analyses Show" — "The overall effect size was 0.21 (95% CI: 0.15-0.27, p < 2.7 × 10⁻¹²)."
- **Problem**: The published 95% CI for the overall effect is **0.13–0.29**, confirmed against the Frontiers paper and multiple secondary sources (including the Duggan & Tressoldi 2018 update, which restates the original as "0.21, 95% CI = 0.13–0.29"). The article's "0.15–0.27" is narrower than the real interval, overstating the precision/robustness of the headline result. The point estimate (0.21) and p-value are correct.
- **Severity**: Medium (verifiable factual error in a load-bearing citation; corrigible with a one-token edit per bound)
- **Recommendation**: `refine-draft` — change "0.15-0.27" to "0.13-0.29".

### Issue 2: "10²⁰ to 1" prior odds attributed to Wagenmakers is not source-attested
- **File**: `obsidian/topics/presentiment-and-retrocausality.md`
- **Location**: §"The Current State" — "Wagenmakers et al. (2011) ... set prior odds against psi at roughly 10²⁰ to 1 ... even a Bayes factor of 10⁹ leaves posterior odds on the order of 10¹¹ *against*."
- **Problem**: The dispute over Wagenmakers' prior being unreasonably extreme is real and well documented (Bem, Utts & Johnson's reply argues the default Cauchy prior places implausible mass on huge effect sizes). But the specific magnitude "roughly 10²⁰ to 1" is not stated by Wagenmakers et al. and was not found in the source literature; it reads as the article's own back-of-envelope reconstruction. Presenting a self-derived number as the figure the cited authors "set" is an attribution defect of the [[ai_citation_metadata_unreliable]] family (here: fabricated precision rather than wrong metadata). The "10¹¹ against" follows arithmetically from 10²⁰/10⁹, so if the premise number is unsourced the conclusion inherits the problem.
- **Severity**: Medium
- **Recommendation**: `refine-draft` — either (a) source the 10²⁰ figure to a specific page/passage, or (b) recast as the article's own illustrative estimate with explicit hedging ("on plausible reconstructions of how extreme the default prior is, prior odds against psi run many orders of magnitude, so even a 10⁹ Bayes factor need not move the posterior to favour psi"), making clear the number is illustrative, not Wagenmakers' stated value. The dialectical point (prior does the decisive work) is correct and should be preserved.

## Counterarguments to Address

### The degree-not-kind asymmetry lacks a quantitative anchor
- **Current content says**: A single retrocausally-influenced collapse at one ion channel is "a far smaller ask" than organism-scale anticipatory coordination; the asymmetry between the Map's mechanism and presentiment is one of degree of implausibility, not a clean line.
- **A critic would argue**: "Degree of implausibility" with no metric is not an argument a skeptic must accept; having conceded the line is not clean, the article needs a reason its own mechanism falls on the survivable side.
- **Suggested response**: Add one sentence grounding the asymmetry in something concrete — e.g. the information-availability disanalogy (the Map's selection operates on internally-superposed states the organism already instantiates, whereas presentiment requires anticipatory coupling to an *external* event carrying no present information to the organism). The article gestures at this ("an external event the organism has no information about") but does not elevate it to the load-bearing distinction; doing so would convert a degree-claim into a kind-claim that survives the decoherence concession.

### The firewall is comparative, and the comparison rests on falsifiability
- **Current content says**: The physics is a "respectable mainstream-physics dispute" whereas presentiment's defense is "conceded unfalsifiable."
- **A critic would argue**: Empirically-equivalent interpretations are themselves not differentially testable, so the firewall does not buy testability — only respectability-by-association.
- **Suggested response**: No change required; the article already states the firewall "buys ... comparative, not absolute" advantage and that a confirmed phenomenon is not a confirmed interpretation. This is honest. Flagging only so a future deep-review does not mistake the comparative framing for a testability claim.

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| Mossbridge 95% CI "0.15–0.27" | §What the Meta-Analyses Show | Correct to published 0.13–0.29 (see Issue 1) |
| Wagenmakers "prior odds ... roughly 10²⁰ to 1" | §The Current State | Page/passage citation, or recast as article's own estimate (see Issue 2) |
| Duggan & Tressoldi 2018: pre-registered 0.31 vs non-pre-registered 0.24 | §What the Meta-Analyses Show | Point estimates plausible and uncontradicted, but the specific pre-reg/non-pre-reg split was not confirmable from the abstract; the published update headline is overall 0.28 (95% CI 0.18–0.38), peer-reviewed 0.36. Verify the 0.31/0.24 split against the paper's tables on next refine. Low priority. |

## Language Improvements

No strong-language or LLM-cliché violations found. The single "fallacious" usage (§Relation to Site Perspective) is justified — it names a genuine inference error symmetrically and is not over-asserting. The article's hedging is appropriately calibrated throughout; if anything it is a model for the calibrated-uncertainty house style.

## Special Audit Results (this skill's checklists)

- **Epistemic/metaphysical equivocation**: PASS. The article's central move is itself a disciplined separation of readings — it keeps the *interpretive* (metaphysical) status of retrocausality distinct from the *empirical* status of presentiment, and twice states that a confirmed phenomenon is not a confirmed interpretation. No load-bearing claim recruits epistemic evidence to assert a metaphysical conclusion.
- **Direct-refutation discipline / label leakage**: PASS. No forbidden editor-vocabulary tokens in prose; opponents (Tegmark, the skeptics) are engaged in natural prose. The decoherence engagement is the strongest case — it neither boundary-substitutes nor over-claims an in-framework refutation; it honestly concedes the threat applies to the Map too.
- **Altered-state symmetry**: NOT APPLICABLE. Supportive-cluster gate not met (no psychedelics/NDE/cessation/OBE citations; apparent "nde" grep hits were substring false positives in "independent"/"evidence").
- **Length**: PASS. 1901 body words, within thresholds.
- **Wikilinks**: PASS. Key targets (retrocausality, quantum-consciousness, libet-experiments, time-symmetric-physics, agent-causation) all resolve.

## Strengths (Brief)

- The firewall framing is the article's signal virtue and should be preserved verbatim in any refine: it lets the Map present hostile evidence honestly without staking its foundations on it.
- The article self-surfaces its single most exposed vulnerability (decoherence threatens the Map's own mechanism, not just presentiment) rather than hiding it — exemplary intellectual honesty and exactly the calibration the house style wants.
- Even-handed presentation of both meta-analytic support (Mossbridge, Duggan, Bem 2016) and the replication-failure / Bayesian-skeptic side (Galak, Wagenmakers); the Galak n=3,289 / near-zero effect and Wagenmakers "weak to nonexistent" quote both verify correctly against the live literature.
- Clean separation of Libet (internal-decision timing) from presentiment (external-event anticipation) prevents a common conflation.
