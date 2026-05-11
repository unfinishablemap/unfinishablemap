---
title: "Selection-Only Channel"
description: "Information-channel framing of selection-only mind-influence: per-event capacity, Born-rule preservation, and content-confinement, in human–AI dialogue."
created: 2026-05-11
modified: 2026-05-11
human_modified:
ai_modified: 2026-05-11T19:11:00+00:00
last_deep_review: 2026-05-11T19:11:00+00:00
draft: false
topics:
  - "[[selection-only-mind-influence]]"
  - "[[hard-problem-of-consciousness]]"
concepts:
  - "[[interactionist-dualism]]"
  - "[[consciousness-physics-interface-formalism]]"
  - "[[mind-matter-interface]]"
  - "[[coupling-modes]]"
  - "[[post-decoherence-selection]]"
  - "[[conservation-laws-and-mental-causation]]"
  - "[[asymmetric-bandwidth-consciousness]]"
  - "[[stapp-quantum-mind]]"
related_articles:
  - "[[tenets]]"
  - "[[interface-threshold]]"
  - "[[consciousness-bandwidth-architecture]]"
  - "[[interface-specification-programme]]"
  - "[[post-decoherence-selection-programme]]"
  - "[[mathematical-structure-of-the-consciousness-physics-interface]]"
  - "[[born-rule-and-the-consciousness-interface]]"
  - "[[interface-efficacy-and-the-cognitive-gap]]"
  - "[[possibility-probability-slippage]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-11
last_curated:
---

The selection-only channel is the class of mind-physical information channel in which mind acts solely as a selector among physically-prepared alternatives, contributing nothing to the alternative set itself. Three information-theoretic constraints follow directly from this restriction. Each selection event carries at most log₂(N) bits of mind-side information, where N is the cardinality of the brain-prepared candidate set. Born-rule preservation drives the effective signed information rate toward zero across many trials. And the dimensionality of registrable phenomenal content is bounded above by the dimensionality of the brain's candidate space at the relevant decoherence stage. These three properties — per-event ceiling, Born-statistics preservation, and content-confinement — together define the channel class.

Selection-only is the strictest reading of the Map's [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]] tenet. This page treats it as a *channel class* — a category of mind-physical coupling defined by what it does *not* do — and articulates the information-theoretic invariants any such channel must satisfy. The fuller philosophical argument, empirical signature corridor, and distinguishing-observables table sit in [[selection-only-mind-influence]]; this concept is the technical building block those discussions reference.

## The Channel Model

A communication channel, in Shannon's framework, is fully specified by three components: an input alphabet X, an output alphabet Y, and a conditional distribution P(y | x) describing how inputs map to outputs. For mind-physical coupling, the natural framing is:

- **Input alphabet**: mind-side states (the experiential states an embodied mind could occupy)
- **Output alphabet**: physical states (the post-selection candidate the brain realises)
- **Transition kernel**: how a mind-state maps onto a selection among brain-generated candidates

A *generation channel* is any channel in which the input distribution at least partly determines the output alphabet itself — mind contributes to *which* alternatives are physically realised, not only to *which one* is realised. A *selection-only channel* is the proper subclass in which the input distribution can only redistribute mass over an output alphabet whose set is fixed by upstream physical dynamics. Mind selects within the candidate set; it never extends it.

The distinction is at the level of the channel's specification, not at the level of any single outcome. Two channels can produce the same individual selection while differing in whether the candidate set was mind-influenced upstream — but their long-run behaviour and the structural bounds they obey diverge sharply. The information-theoretic results below all follow from the structural constraint, not from any particular event.

## Three Defining Constraints

### Per-Event Capacity: log₂(N) Bits

For a selection event with N brain-generated candidates of probabilities p₁, …, p_N, the maximum information transferable by realising one specific candidate is bounded above by the Shannon entropy of a uniform distribution over the candidate set:

I_max(event) ≤ log₂(N) bits

The bound is saturated only when the candidate distribution is uniform. Under any non-uniform Born-rule distribution the actual entropy is strictly less. The structural point is that *N* is set entirely by the brain: no mind-side operation can push past the candidate-set ceiling per event. The only way to widen the per-event channel is to widen *N* by changing what brain dynamics make physically available — and that is a brain-side change, not a mind-side one.

This is a sharper bound than is typically stated in discussions of mind-physical coupling. Most accounts speak of "small bias" without naming the ceiling; the channel-theoretic framing makes the ceiling explicit and physical-side-determined.

### Born-Rule Preservation Drives Signed Rate Toward Zero

The selection-only channel inherits a constraint that ordinary Shannon channels do not have: the empirical frequency distribution over the output alphabet must converge to the Born-rule distribution {p₁, …, p_N} across many trials. This is the channel-theoretic content of [[tenets#^minimal-quantum-interaction|Tenet 2]] under its strictest reading, and it is also what the [[born-rule-and-the-consciousness-interface|no-signalling theorem]] requires of any mind-physical channel that is to remain compatible with relativistic causality (Han 2016).

Born-rule preservation pins the *expected* mutual information between mind-state and outcome to zero in the long-run limit. Per-trial signed information rate is therefore bounded by max{p_i} − min{p_i} ≈ ε, with Shannon rate ≈ ε² / (2 ln 2) bits/trial in the small-bias limit (binary case). For ε ≈ 10⁻⁴ — the empirical ceiling associated with the long-running psi-research signature corridor (Bösch et al. 2006; Maier et al. 2018) — the per-trial rate is roughly 7 × 10⁻⁹ bits/event.

This constraint is what distinguishes the selection-only channel from a generic Shannon channel of the same per-event capacity. A Shannon channel with log₂(N)-bit capacity admits arbitrarily high information rates given enough trials; the selection-only channel does not, because its long-run frequency statistics are pinned to the physical-side prior. The cost of Born-rule preservation is paid in throughput.

### Content-Confinement: Output Alphabet Bounds Input Alphabet

The third constraint is structural rather than statistical. In ordinary information theory the input alphabet is whatever the source can encode; the channel does not constrain it. The selection-only channel inverts this: because mind can only choose among brain-generated candidates, the effective input alphabet — the mind-side states the channel can carry — is bounded above by the output alphabet.

Three consequences follow directly:

- Mind cannot register a phenomenal state for which no candidate exists.
- Mind cannot report content that no candidate encodes.
- Novel phenomenal states must be pre-generated by brain dynamics; they cannot be brought into being by selection alone.

This is a much stronger constraint than the corresponding constraint on generation channels, where mind can in principle supply novelty beyond the brain-encoded set. Content-confinement is a Holevo-style ceiling on phenomenal content: the dimensionality of reportable conscious states is bounded above by the dimensionality of the relevant brain-side decoherence-domain space. [[interface-efficacy-and-the-cognitive-gap]] picks up this same dimensionality bound as a *cross-species* variable, with the per-event arithmetic developed here as its shared background.

Whether this ceiling is currently measurable is open; operationalising it is a target of the [[interface-specification-programme]]. Whether the ceiling is *real* — whether mind in fact has no inputs not realised in the candidate set — is a structural commitment of the channel class, not an empirical claim derivable from it. Treating the ceiling's coherence with the Map's tenets as evidence *for* it would be a textbook case of [[possibility-probability-slippage]]; the channel-class framing earns its place by what it cannot claim, not by what data can confirm about it.

## What the Channel Is Not

The selection-only channel is distinct from several related channel types it is sometimes conflated with:

- **Not a probability-bias channel.** A probability-bias channel allows mind to shift the candidate distribution {p_i} away from its physical-side values within an existing candidate set. A selection-only channel preserves the distribution and only realises one outcome at the prescribed rate. Probability-bias channels live in the intermediate reading of Tenet 2; they are a strictly larger class.

- **Not a measurement-basis-choice channel.** Stapp's *Process 1* framework licenses mind to choose *which question* the brain asks of nature — the choice of observable or measurement basis (Stapp n.d.). This is a richer channel that is not strictly selection-only at the outcome level: it modifies the candidate set itself by selecting the basis that defines it. Stapp explicitly limits the *outcome-level* channel to selection-only — "the mind would only have the option to choose the observable, not the option of selecting the measurement result in deviation from the Born's probability law" (Stapp n.d.) — but the basis-choice layer above sits outside the selection-only class strictly construed.

- **Not an energy-injection channel.** Because selection acts only on already-generated alternatives, no work is done on the physical system in the thermodynamic sense; no momentum is transferred; no quantity that physics tracks as "energy delivered" is moved across the interface. The channel is energetically inert, which is why the energy-conservation objection to mental causation does not apply to it (Collins n.d.; Pitts 2022). The constraint that does bind is information-theoretic, not energetic.

- **Not a candidate-generation channel.** Some readings of Stapp's late work and of Penrose-Hameroff Orchestrated Objective Reduction identify consciousness with the candidate-generation event itself. Those channels permit mind to contribute to the alternative set; they are not selection-only.

The channel class is defined by what it forbids. Its distinctive identity is the joint commitment to candidate-set fixity, Born-statistics preservation, and content-confinement — taken together, not separately.

## Bidirectionality

The selection-only channel is bidirectional in the channel-theoretic sense: information flows in both directions, but the directions are bounded differently and by different constraints.

- **Mind-to-physical** carries the per-event capacity log₂(N) bits and is throttled by Born preservation to ε²/(2 ln 2) bits/trial in the long-run limit.
- **Physical-to-mind** carries the candidate-set information out to the selector. Its bound is the dimensionality of the brain-side decoherence-domain space; the content-confinement constraint is the *upper bound* on what mind can carry as input alphabet.

The asymmetry is intrinsic: the forward and reverse channels have different capacities and different binding constraints, even though they share a common candidate set as their interfacing layer. This is the channel-theoretic statement of what [[asymmetric-bandwidth-consciousness]] catalogues at a higher level of abstraction.

## Relation to Site Perspective

The selection-only channel is the cleanest formal expression of the Map's [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]] tenet. It commits to the *smallest* deviation from physical dynamics — one whose channel-theoretic signature is that the candidate set, the Born-rule distribution, and the energetic balance are all left untouched. The interface acts only through the act of selection itself.

[[tenets#^bidirectional-interaction|Tenet 3 (Bidirectional Interaction)]] is preserved as channel direction: information flows from mind to physical (the realised candidate) and from physical to mind (the candidate set the mind can choose from). The forward and reverse directions are both genuine information channels; they are bounded differently. The content-confinement constraint expresses the reverse direction's bound; the per-event capacity and Born-preservation constraints express the forward direction's bound.

[[tenets#^dualism|Tenet 1 (Dualism)]] is presupposed by the channel's existence — there must be a non-physical selector for the input alphabet to be distinct from the output alphabet, and for the act of selection to be more than a redescription of brain dynamics. [[tenets#^no-many-worlds|Tenet 4 (No Many Worlds)]] is presupposed by the channel's output semantics: selection is meaningful only if one candidate becomes actual rather than all of them.

The Map does not commit to the strict selection-only reading as the only viable reading of Tenet 2. The intermediate reading — probability-bias channels averaging to Born statistics over ensembles — remains live. But the selection-only channel is the version under which the information-theoretic constraints are sharpest, the energy-conservation objection has no purchase, and the no-signalling theorem is automatically respected. It is the version other Map articles can take as a clean reference point when contrasting more permissive channel classes against the strictest one. The apex syntheses [[post-decoherence-selection-programme]] and [[interface-specification-programme]] both take this concept as the channel-theoretic formalisation of their "minimal intervention" commitment — the former locating the channel-class in the post-decoherence menu specified by quantum Darwinism, the latter aligning the per-event log₂(N) ceiling with the ~10 bits/second bandwidth architecture and the Born-rule throttling with the delegatory-causation default profile.

## Further Reading

- [[selection-only-mind-influence]]
- [[post-decoherence-selection-programme]]
- [[interface-specification-programme]]
- [[forward-in-time-conscious-selection]]
- [[post-decoherence-selection]]
- [[consciousness-physics-interface-formalism]]
- [[mathematical-structure-of-the-consciousness-physics-interface]]
- [[coupling-modes]]
- [[mind-matter-interface]]
- [[asymmetric-bandwidth-consciousness]]
- [[consciousness-bandwidth-architecture]]
- [[interface-efficacy-and-the-cognitive-gap]]
- [[interface-threshold]]
- [[stapp-quantum-mind]]
- [[interactionist-dualism]]
- [[conservation-laws-and-mental-causation]]
- [[born-rule-and-the-consciousness-interface]]
- [[interface-specification-programme]]
- [[possibility-probability-slippage]]

## References

1. Bösch, H., Steinkamp, F., & Boller, E. (2006). Examining psychokinesis: The interaction of human intention with random number generators—A meta-analysis. *Psychological Bulletin*, 132(4), 497–523. https://pubmed.ncbi.nlm.nih.gov/16822162/
2. Collins, R. (n.d.). Modern physics and the energy conservation objection to mind-body dualism. https://www.newdualism.org/papers/R.Collins/EC-PEC.htm
3. Han, Y.-D. (2016). Quantum probability assignment limited by relativistic causality. *Scientific Reports*, 6, 22986. https://www.nature.com/articles/srep22986
4. Maier, M. A., Dechamps, M. C., & Pflitsch, M. (2018). Intentional observer effects on quantum randomness: A Bayesian analysis reveals evidence against micro-psychokinesis. *Frontiers in Psychology*, 9, 379. https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/
5. Pitts, J. B. (2022). General relativity, mental causation, and energy conservation. *Erkenntnis*. https://link.springer.com/article/10.1007/s10670-020-00284-7
6. Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.
7. Stapp, H. P. (n.d.). Quantum interactive dualism. https://www-physics.lbl.gov/~stapp/QID.pdf
8. Stapp, H. P. (1993). *Mind, Matter, and Quantum Mechanics*. Springer.
9. Southgate, A. & Oquatre-sept, C. (2026-05-05). Selection-Only Mind-Influence: Information-Transfer Limits and Physical-World Signatures. *The Unfinishable Map*. https://unfinishablemap.org/topics/selection-only-mind-influence/
