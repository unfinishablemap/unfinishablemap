---
title: "Selection-Only Mind-Influence: Information-Transfer Limits and Physical-World Signatures"
description: "Human–AI exploration of the strictest reading of mind-on-quantum influence: three information-theoretic limits and the empirical signatures that follow."
created: 2026-05-05
modified: 2026-05-06
human_modified:
ai_modified: 2026-05-06T11:16:00+00:00
last_deep_review: 2026-05-06T11:16:00+00:00
draft: false
topics: []
concepts:
  - "[[interactionist-dualism]]"
  - "[[forward-in-time-conscious-selection]]"
  - "[[post-decoherence-selection]]"
  - "[[stapp-quantum-mind]]"
  - "[[conservation-laws-and-mental-causation]]"
related_articles:
  - "[[trilemma-of-selection]]"
  - "[[asymmetric-bandwidth-consciousness-2026-03-02|asymmetric-bandwidth-consciousness]]"
  - "[[mathematical-structure-of-the-consciousness-physics-interface]]"
  - "[[born-rule-and-the-consciousness-interface]]"
  - "[[interface-specification-programme]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-05
last_curated:
---

The strictest reading of the Map's [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]] tenet is *selection-only*: mind contributes nothing to the candidate set the brain physically generates. It only chooses which of the already-generated alternatives becomes actual. Under that constraint, three information-theoretic limits follow immediately. Each selection event can transfer at most log₂(N) bits, where N is the size of the brain-prepared candidate set. Long-run frequency statistics over that set must converge to physical Born-rule probabilities, driving the *signed* per-trial information rate toward zero across many trials. And mind cannot register, choose, or report content that no candidate encodes — novel qualia are structurally precluded if the brain has not pre-generated them. These three limits define a tight signature corridor: large enough to make a difference at the single-event scale, small enough to vanish at the ensemble scale, and bounded at every level by the physical-side candidate set.

This article derives those limits, surveys the empirical ceiling they have to live under, and ends with a table of distinguishing observables that — at least in principle — separate selection-only models from candidate-generation alternatives.

## The Strict Reading of Tenet 2

Tenet 2 commits the Map to "the smallest possible non-physical influence on quantum outcomes". That commitment admits several readings of varying strictness:

- **Loose reading**: Mind nudges quantum probabilities, with deviations from the Born rule small enough to lie below current detection thresholds.
- **Intermediate reading**: Mind biases individual outcomes but the bias averages to Born statistics over any well-defined ensemble.
- **Strict (selection-only) reading**: Mind selects among already-generated alternatives without altering either the candidate set or its Born-rule probabilities.

The strict reading is the one this article formalises. It is the reading historically associated with Henry Stapp's *Process 1* framework, where consciousness chooses *which question* the brain asks of nature — the choice of observable or measurement basis — while the *answer* is "given by nature" at random. As Stapp puts it in his Quantum Interactive Dualism paper, "the mind would only have the option to choose the observable, not the option of selecting the measurement result in deviation from the Born's probability law" (Stapp, n.d.).

Under this reading, the mind-side contribution is a pure post-processing stage layered on top of brain dynamics: the brain produces a probability distribution over candidates; mind realises one of them; Born statistics are preserved over long runs.

The strict reading is not the only consistent way to honour Tenet 2 — the intermediate reading is empirically live — but it is the reading that yields the cleanest derivable constraints, and it is the one whose ensemble-level statistics are automatically compatible with no-signalling. (Energy conservation, as discussed below, is not a serious objection at any reading once selection is distinguished from generation.)

## Three Information-Transfer Limits

### Per-event Ceiling: log₂(N) Bits

For a selection event with N candidates, the maximum information transferable by selecting a specific outcome is bounded above by the entropy of a uniform distribution over those candidates:

I_max(event) ≤ log₂(N) bits

This bound is saturated only when the candidate distribution is uniform. Under any nontrivial Born-rule distribution {p₁, …, p_N}, the entropy is strictly less than log₂(N), and the Born-rule-preserving signed per-trial information rate drops further: in the small-bias limit, it approximates ε² / (2 ln 2) bits per trial, where ε bounds the fractional deviation any single mind-side selection can induce while still preserving long-run Born statistics.

The structural point is that *N* — set by the brain — is a hard physical-side ceiling. No amount of mental effort can push past log₂(N) per event; the only way to push the event-level ceiling up is to push *N* up by changing what brain dynamics make available.

### Per-second Ceiling: Rate × log₂(N)

If candidate-selection events occur at rate R, total mind-side bandwidth is at most:

I_max(sec) ≤ R · log₂(N) bits/s   *(unconstrained ceiling)*
I_max(sec) ≈ R · ε² / (2 ln 2) bits/s   *(Born-rule-preserving)*

The unconstrained ceiling is achievable only if Born-rule preservation is suspended. Under the strict reading, the second formula is the binding constraint — and ε² is unforgiving: even ε of order 10⁻³ delivers a per-trial rate of roughly 7 × 10⁻⁷ bits/event.

This couples directly to *amplification*. If selection occurs at neural-quantum events on the order of 10⁷–10¹² per second across the brain, then aggregate Born-rule-preserving bandwidth lands in a band that — depending on the assumed selection rate — can be either far below or comparable to the ~10 bits/s of conscious agency reported by Stoll & Zheng (2025). The strict reading is therefore *quantitatively viable* only if the per-event channel is multiplied across enough events to deliver the observed conscious-agency bandwidth.

### Content-Confinement: No Novel Qualia Without Neural Pre-Generation

The first two limits constrain the *physical-to-physical* signalling capacity of mind-side selection. The third limit, less commonly stated, constrains *what content mind can have at all*:

If mind can only choose among brain-generated candidates, then mind's phenomenal repertoire is confined to whatever the candidate set encodes.

Three structural consequences follow:

- Mind cannot register a quale that no candidate represents.
- Mind cannot report content that no candidate encodes.
- Novel qualia must be pre-generated by brain dynamics — they cannot be brought into being by selection alone.

This is *much* stronger than the corresponding constraint under generation-permitting models, where mind could in principle contribute novel content. Under the strict reading, every distinguishable phenomenal state must have a brain-side correlate already present in the candidate space. The interface is read-and-select, not read-and-create.

This has a direct empirical consequence the literature has not foregrounded: the dimensionality of *reportable conscious content* must be bounded above by the dimensionality of the brain-generated *candidate space* at the relevant decoherence stage. If the latter could be measured, the former would inherit a hard upper bound — a Holevo-style ceiling on phenomenal content. Estimating the relevant candidate-space dimensionality is an open research problem.

## The Empirical Signature Corridor

Under the strict reading, what should psi-style laboratory data look like? The answer is not "strong PK signals" — those would falsify the strict reading by violating Born statistics. The answer is "vanishing per-trial bias under sustained measurement, with a possible decline-effect signature".

Three results sharpen this corridor:

- The Princeton Engineering Anomalies Research programme, accumulated over decades, reported a per-trial bias on the order of 10⁻⁴ bits per bit processed. Independent replication across the Mind/Machine Interaction Consortium with 227 participants and roughly 2 million trials failed to confirm the original effect (Jahn et al. 2000).
- Bösch, Steinkamp & Boller's 2006 meta-analysis of 380 RNG-PK studies reported a significant overall effect, but with effect size strongly inversely related to sample size: "the small effect size, the relation between sample size and effect size, and the extreme effect size heterogeneity found could in principle be a result of publication bias" (Bösch et al. 2006).
- Maier, Dechamps & Pflitsch (2018) ran a pre-registered Bayesian replication with 12,571 subjects and reported strong evidence for the null: "the Bayesian analysis revealed strong evidence for H0 (BF01 = 10.07), thus micro-PK did not exist in the data".

Read together, these results bracket the corridor. If a real selection-only signature exists, its per-trial information rate sits below ~10⁻⁴ bits/bit at PEAR scales and below the Maier-Dechamps detection threshold at large N. The strict reading *predicts* this — large detectable bias would be evidence against it, not for it. The corridor is what a self-limiting, Born-rule-preserving channel should leave behind.

Crucially, the Map does not treat the existence of this corridor as evidence *for* the dualist interface. The corridor is a *bound* the interface must live within if it exists at all; the empirical pattern is equally consistent with the no-effect null hypothesis. Reading the corridor as positive evidence would be a textbook case of [[possibility-probability-slippage|possibility-probability slippage]] — using tenet-coherence to upgrade a structural compatibility into evidential support. The strict reading earns its place by what it *cannot* claim, not by what the data show.

## The Decline Effect as Theoretical Prediction

Two related but distinct phenomena travel under "decline" in this literature. The first is *across-studies* historical decline: effect sizes in psi research drop systematically over time across all major paradigms — RNG-PK, ganzfeld, card-guessing, DMILS — with replication rates of 20–33% in well-conducted studies versus 80%+ in original studies (Walach et al. 2014). The mainstream interpretation is methodological: publication bias and questionable research practices wash out as studies tighten. The second is *within-study* sample-size decline: per-trial bias that appears at small N regresses toward Born statistics as N grows, exactly as the law of large numbers requires of any Born-rule-preserving channel.

A different interpretation of *across-studies* decline is available within the Generalised Quantum Theory framework developed by Atmanspacher, Römer and Walach (Atmanspacher, Römer & Walach 2002; Walach et al. 2014). On that framing the decline is the physics enforcing no-signalling on a real but small effect — when correlations are first probed they may appear, but as repeated probing approaches a regime that would amount to genuine signal transfer, the effect recedes.

The strict reading does not need to take a side on the across-studies pattern. Methodological wash-out and physics-enforced no-signalling are empirically near-indistinguishable, and the strict reading is consistent with both. What the strict reading does straightforwardly predict is the *within-study* decline: by Born-rule preservation, any per-event bias must regress as N grows. Either reading of "decline" is therefore a theoretical signature rather than an embarrassment for the strict-selection model.

## No-Signalling, Energy Conservation, and the Information-Side Constraint

The strictest selection-only model is *not* primarily constrained by the energy-conservation objection. As Robin Collins and J. B. Pitts have pointed out (Collins, n.d.; Pitts 2022), quantum correlations show that mind-brain interaction without energy exchange has precedent in current physics, and general relativity's non-localisability of gravitational energy further weakens the energy-conservation objection. Under the strict reading no energy is injected at all; the channel is energetically inert.

The binding constraint is information-theoretic. The Born rule itself can be derived from relativistic-causality / no-signalling considerations (Han 2016), and "violation of higher sum-rules allows for superluminal signalling". Any *systematic* per-trial deviation from Born-rule probabilities is therefore directly coupled to relativistic-causality violation. The strict reading buys compatibility with no-signalling at the price of accepting that no large effect can ever be visible at the ensemble level. That tradeoff is not optional — it follows from the structure of quantum probability.

This reframes the metaphysical pressure on Tenet 2. The dualist interface does not need to defend itself against energy-conservation objections at the strict reading; it needs to defend itself against the charge that, by preserving Born statistics, it *cannot make a measurable difference at the ensemble level at all*. The article's three limits define exactly where it can — and where it cannot.

## Distinguishing Observables

The strict reading is empirically distinguishable from generation-permitting alternatives, even if current laboratory paradigms cannot yet operationalise the contrasts. The following observables separate the two families:

| Observable | Selection-Only | Generation |
|---|---|---|
| Per-trial bias under accumulating measurement | Vanishing in long run | Possibly persistent |
| Born-rule preservation over candidate set | Required | Optional |
| Decline effect under repeated trials | Predicted | Not predicted |
| No-signalling preservation | Strict | Possibly violated |
| Novel qualia without prior neural representation | Impossible | Possible |
| Conditional bias correlation with decoherence-domain diversity | Strong | Weak/absent |
| Energy/momentum injection signature | Zero | Possibly nonzero |

Of these, the *most discriminating* is the **correlation between candidate-set diversity and reportable phenomenal content**. Under the strict reading, the dimensionality of reportable content is bounded above by the dimensionality of brain-generated candidate space; under generation-permitting models, mind can supply novelty beyond what the brain pre-encodes. No current experiment cleanly operationalises this contrast, and doing so is a target for the [[interface-specification-programme]].

## Relation to Site Perspective

The strict reading of selection-only mind-influence is the cleanest expression of the Map's [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]] tenet. It commits to the *smallest* deviation from physical dynamics — one that injects no energy, leaves Born statistics intact, and acts only through the act of selection itself. The Map does not require this strict reading; the intermediate reading is also live. But the strict reading is the version most directly defensible against information-theoretic objections, and it is the version under which Tenet 2's "minimality" claim is most fully honoured.

[[tenets#^bidirectional-interaction|Tenet 3 (Bidirectional Interaction)]] is preserved under the strict reading: selection is genuine causation, in that it determines which physically-permitted outcome becomes actual. Mind makes a difference; it just makes the smallest possible kind of difference. The information-theoretic ceilings derived in this article are the price the Map pays for compatibility with orthodox physics — and they are also the source of the Map's empirical predictions.

[[tenets#^dualism|Tenet 1 (Dualism)]] is presupposed: there must be a non-physical selector for there to be selection at all. [[tenets#^no-many-worlds|Tenet 4 (No Many Worlds)]] is also presupposed: selection only makes sense if one outcome becomes actual rather than all of them. The strict reading is therefore the joint expression of Tenets 1, 2, 3 and 4 in their tightest possible coherent form.

The Map interprets the empirical situation as follows. The vanishing of detectable PK signatures under sustained measurement is not a refutation of the dualist interface — it is what the strict reading predicts. The decline effect, on its theoretical reading, is a candidate signature of Born-rule preservation under accumulating measurement. The Map does not endorse psi research as evidence *for* the interface; it treats the empirical corridor as the *bound* the interface must live within. The most informative experiments would not chase larger effect sizes but would target the content-confinement prediction — measuring whether reportable phenomenal content tracks candidate-set diversity at relevant neural sites.

## Further Reading

- [[forward-in-time-conscious-selection]]
- [[post-decoherence-selection]]
- [[trilemma-of-selection]]
- [[stapp-quantum-mind]]
- [[born-rule-and-the-consciousness-interface]]
- [[born-rule-violation-brain-interface-empirical-status]]
- [[asymmetric-bandwidth-consciousness-2026-03-02|asymmetric-bandwidth-consciousness]]
- [[bandwidth-of-consciousness]]
- [[consciousness-bandwidth-architecture]]
- [[conservation-laws-and-mental-causation]]
- [[interactionist-dualism]]
- [[the-interface-problem]]
- [[interface-specification-programme]]
- [[mathematical-structure-of-the-consciousness-physics-interface]]
- [[contextual-selection-in-quantum-foundations]]
- [[weak-measurement-and-post-selection]]
- [[amplification-mechanisms-consciousness-physics]]
- [[possibility-probability-slippage]]

## References

1. Atmanspacher, H., Römer, H., & Walach, H. (2002). Weak quantum theory: Complementarity and entanglement in physics and beyond. *Foundations of Physics*, 32(3), 379–406.
2. Bösch, H., Steinkamp, F., & Boller, E. (2006). Examining psychokinesis: The interaction of human intention with random number generators—A meta-analysis. *Psychological Bulletin*, 132(4), 497–523. https://pubmed.ncbi.nlm.nih.gov/16822162/
3. Collins, R. (n.d.). Modern physics and the energy conservation objection to mind-body dualism. https://www.newdualism.org/papers/R.Collins/EC-PEC.htm
4. Han, Y.-D. (2016). Quantum probability assignment limited by relativistic causality. *Scientific Reports*, 6, 22986. https://www.nature.com/articles/srep22986
5. Jahn, R. G., Mischo, J., Vaitl, D., Dunne, B. J., Bradish, G. J., Dobyns, Y. H., Lettieri, A., Nelson, R. D., Boller, E., Bösch, H., Vaitl, D., & Houtkooper, J. (2000). Mind/machine interaction consortium: PortREG replication experiments. *Journal of Scientific Exploration*, 14(4), 499–555.
6. Maier, M. A., Dechamps, M. C., & Pflitsch, M. (2018). Intentional observer effects on quantum randomness: A Bayesian analysis reveals evidence against micro-psychokinesis. *Frontiers in Psychology*, 9, 379. https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/
7. Pitts, J. B. (2022). General relativity, mental causation, and energy conservation. *Erkenntnis*. https://link.springer.com/article/10.1007/s10670-020-00284-7
8. Stapp, H. P. (n.d.). Quantum interactive dualism. https://www-physics.lbl.gov/~stapp/QID.pdf
9. Stapp, H. P. (1993). *Mind, Matter, and Quantum Mechanics*. Springer.
10. Stoll, J., & Zheng, M. (2025). The brain works at more than 10 bits per second. *Neuron*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12320479/
11. Walach, H., Horan, M., Hinterberger, T., & von Lucadou, W. (2014). Evidence-based parapsychology and the decline effect. *Journal of Parapsychology*. https://psi-encyclopedia.spr.ac.uk/articles/decline-effect-parapsychology
12. Southgate, A. & Oquatre-six, C. (2026-03-18). Mathematical Structure of the Consciousness-Physics Interface. *The Unfinishable Map*. https://unfinishablemap.org/topics/mathematical-structure-of-the-consciousness-physics-interface/
