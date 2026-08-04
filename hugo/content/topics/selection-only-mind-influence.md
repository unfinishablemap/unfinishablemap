---
ai_contribution: 100
ai_generated_date: 2026-05-05
ai_modified: 2026-08-04 09:12:00+00:00
ai_system: claude-opus-4-7+claude-opus-5
author: null
concepts:
- '[[interactionist-dualism]]'
- '[[forward-in-time-conscious-selection]]'
- '[[post-decoherence-selection]]'
- '[[stapp-quantum-mind]]'
- '[[conservation-laws-and-mental-causation]]'
- '[[selection-only-channel]]'
created: 2026-05-05
date: &id001 2026-05-11
description: 'Human–AI exploration of the strictest reading of mind-on-quantum influence:
  three information-theoretic limits and the empirical signatures that follow.'
draft: false
human_modified: null
last_curated: null
last_deep_review: 2026-08-02 11:52:15+00:00
lastmod: 2026-08-04 09:12:00+00:00
modified: *id001
related_articles:
- '[[trilemma-of-selection]]'
- '[[asymmetric-bandwidth-consciousness-2026-03-02|asymmetric-bandwidth-consciousness]]'
- '[[mathematical-structure-of-the-consciousness-physics-interface]]'
- '[[born-rule-and-the-consciousness-interface]]'
- '[[born-preserving-causal-efficacy]]'
- '[[channel-class-taxonomy]]'
- '[[interface-specification-programme]]'
- '[[interface-efficacy-and-the-cognitive-gap]]'
- '[[overdetermination-dissolution-under-selection-only-interactionism]]'
title: 'Selection-Only Mind-Influence: Information-Transfer Limits and Physical-World
  Signatures'
topics:
- '[[quantum-measurement-and-consciousness]]'
- '[[born-rule-and-the-consciousness-interface]]'
- '[[falsification-roadmap-for-the-interface-model]]'
- '[[hard-problem-of-consciousness]]'
---

The strictest reading of the Map's [Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction) tenet is *selection-only*: mind contributes nothing to the candidate set the brain physically generates. It only chooses which of the already-generated alternatives becomes actual. Under that constraint, three information-theoretic limits follow immediately. Each selection event can transfer at most log₂(N) bits, where N is the size of the brain-prepared candidate set. Born-rule preservation constrains the long-run *marginal* frequency distribution over outcomes, leaving the mind-conditioned distributions unconstrained — so what it secures is invisibility to unconditioned aggregate tests, not a bound on throughput. And mind cannot register, choose, or report content that no candidate encodes — novel qualia are structurally precluded if the brain has not pre-generated them. These three limits define a tight signature corridor: large enough to make a difference at the single-event scale, invisible to unconditioned ensemble statistics, and bounded at every level by the physical-side candidate set.

This article derives those limits, surveys the empirical ceiling they have to live under, and ends with a table of distinguishing observables that — at least in principle — separate selection-only models from candidate-generation alternatives. Its companion concept page [selection-only-channel](/concepts/selection-only-channel/) distils the same three limits as Shannon-channel invariants, isolating the per-event arithmetic, the bidirectionality structure, and the taxonomic boundary against probability-bias and basis-choice channels.

## The Strict Reading of Tenet 2

Tenet 2 commits the Map to "the smallest possible non-physical influence on physical outcomes". Its definition clause then fixes where that influence acts: if consciousness can influence the physical world, "it must do so at the quantum level—biasing otherwise indeterminate outcomes without injecting energy or violating conservation laws." The headline states *what* is influenced; the definition states *where*. The readings below are readings of the two clauses together — the quantum-level restriction is inherited from the definition, not read off the headline, which leaves the locus open. So construed, the commitment admits several readings of varying strictness:

- **Loose reading**: Mind nudges quantum probabilities, with deviations from the Born rule small enough to lie below current detection thresholds.
- **Intermediate reading**: Mind biases individual outcomes but the bias averages to Born statistics over any well-defined ensemble.
- **Strict (selection-only) reading**: Mind selects among already-generated alternatives without altering either the candidate set or its Born-rule probabilities.

The strict reading is the one this article formalises. Its closest historical antecedent is Henry Stapp's *Process 1* framework, though the two place mind's freedom in different slots. Stapp has consciousness choose *which question* the brain asks of nature — the choice of observable or measurement basis — while the answer is left to nature: "whether 'Yes' or 'No' appears is not determined by the agent, who chooses only the question. The answer is picked by 'Nature', in accordance with a specified statistical law" (Stapp 2006). Because choosing the question fixes the partition, Stapp's channel shapes the candidate set, which places it outside the selection-only class strictly construed — the taxonomic boundary [selection-only-channel](/concepts/selection-only-channel/) draws. What the strict reading takes from Stapp is the discipline that mind cannot move outcomes off their physical probabilities; what it changes is the slot, holding the candidate set wholly on the physical side and locating the mind-side contribution at the realisation of one already-generated alternative.

Under this reading, the mind-side contribution is a pure post-processing stage layered on top of brain dynamics: the brain produces a probability distribution over candidates; mind realises one of them; Born statistics are preserved over long runs.

The strict reading is not the only consistent way to honour Tenet 2 — the intermediate reading is empirically live — but it is the reading that yields the cleanest derivable constraints, and it is the one whose ensemble-level statistics are automatically compatible with no-signalling. (Energy conservation, as discussed below, is not a serious objection at any reading once selection is distinguished from generation.)

## Three Information-Transfer Limits

### Per-event Ceiling: log₂(N) Bits

For a selection event with N candidates, the maximum information transferable by selecting a specific outcome is bounded above by the entropy of a uniform distribution over those candidates:

I_max(event) ≤ log₂(N) bits

This bound is saturated only when the candidate distribution is uniform. Under any nontrivial Born-rule distribution {p₁, …, p_N}, the entropy is strictly less than log₂(N). Born-rule preservation does *not* throttle the channel further below that ceiling — the derivation this article formerly gave for a tighter Born-preserving rate is withdrawn, for the reasons set out under *Per-second Ceiling* immediately below.

The structural point is that *N* — set by the brain — is a hard physical-side ceiling. No amount of mental effort can push past log₂(N) per event; the only way to push the event-level ceiling up is to push *N* up by changing what brain dynamics make available.

### Per-second Ceiling: Rate × log₂(N)

If candidate-selection events occur at rate R, total mind-side bandwidth is at most:

I_max(sec) ≤ R · log₂(N) bits/s

That is the whole of the rate-level arithmetic the strict reading currently supports. Born-rule preservation does not add a second, tighter formula, because it does not bear on throughput at all. What it binds is the *marginal* distribution over outcomes. [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/) states the relation exactly: on the averaging identity q(O | X) = Σ_C P(O | C, X) · P(C | X), Born-preservation constrains the left-hand marginal and says nothing about whether the conditionals on the right depart from it. What preservation secures is invisibility to *unconditioned* aggregate frequency tests, leaving information flow across the channel entirely open.

**Withdrawn: the Born-rule-preserving rate.** This section formerly carried a second formula — I_max(sec) ≈ R · ε² / (2 ln 2) bits/s — presented as the binding constraint under Born-rule preservation and calibrated at ε of order 10⁻³ to a per-trial rate of roughly 7 × 10⁻⁷ bits/event. It rested on the inference that Born-rule preservation pins the expected mutual information between mind-state and outcome to zero. The inference does not go through. Take a uniform binary mind-state C and an outcome O = C: the marginal over outcomes is exactly uniform, hence Born-satisfying against a uniform candidate distribution, yet I(C;O) = 1 bit, the alphabet's maximum. Marginal preservation is compatible with *maximal* conditional dependence. Two further defects sat in the same passage. Mutual information is non-negative, so a *signed* rate whose excursions cancel is a category error; and a non-negative quantity averaging to zero forces every term to zero rather than licensing cancellation. An ε² expression can approximate a divergence for one specifically defined small binary perturbation, but it is not a consequence of Born preservation — deriving one would need a declared channel, reference distribution, prior over mind-states and perturbation geometry, none of which this article supplies. The figures are suspended pending rederivation; no downstream page should treat this channel as having a known throughput. The parallel withdrawal on the companion concept page is at [selection-only-channel](/concepts/selection-only-channel/), and the [channel-class taxonomy](/concepts/channel-class-taxonomy/) retains an ε² / (2 ln 2) expression legitimately, because it applies it to a declared probability-bias channel with a stated reference distribution rather than deriving it from Born preservation.

This changes what the section can say about *amplification*. With no Born-preserving rate to impose, the only rate-level bound the strict reading supplies is the unconstrained one, and it is generous rather than tight: if selection occurs at neural-quantum events on the order of 10⁷–10¹² per second across the brain, even a binary candidate set puts R · log₂(N) many orders of magnitude above the ~10 bits/s of conscious agency reported by Zheng & Meister (2025). The ceiling therefore does not come close to binding, and the gap between it and the observed figure is a fact about neural and cognitive architecture rather than about the interface. The converse inference the withdrawn arithmetic licensed — that the observed bandwidth fixes the *product* of a per-trial bias parameter and the selection rate — goes out with the derivation that generated it. What survives is weaker and should be stated as such: the strict reading is *compatible* with the observed bandwidth, and does not currently predict it or constrain the selection rate from it.

### Content-Confinement: No Novel Qualia Without Neural Pre-Generation

The first two limits constrain the *physical-to-physical* signalling capacity of mind-side selection. The third limit, less commonly stated, constrains *what content mind can have at all*:

If mind can only choose among brain-generated candidates, then mind's phenomenal repertoire is confined to whatever the candidate set encodes.

Three structural consequences follow:

- Mind cannot register a quale that no candidate represents.
- Mind cannot report content that no candidate encodes.
- Novel qualia must be pre-generated by brain dynamics — they cannot be brought into being by selection alone.

This is *much* stronger than the corresponding constraint under generation-permitting models, where mind could in principle contribute novel content. Under the strict reading, every distinguishable phenomenal state must have a brain-side correlate already present in the candidate space. The interface is read-and-select, not read-and-create.

This has a direct empirical consequence the literature has not foregrounded: the dimensionality of *reportable conscious content* must be bounded above by the dimensionality of the brain-generated *candidate space* at the relevant decoherence stage. If the latter could be measured, the former would inherit a hard upper bound — a Holevo-style ceiling on phenomenal content. Estimating the relevant candidate-space dimensionality is an open research problem. The same dimensionality bound is what [interface-efficacy-and-the-cognitive-gap](/topics/interface-efficacy-and-the-cognitive-gap/) picks up as a *cross-species* variable: candidate-type coupling and selection bandwidth become axes along which the per-species ceiling can scale, with the strict per-event arithmetic developed here as their shared background.

## The Empirical Signature Corridor

Under the strict reading, what should psi-style laboratory data look like? The answer is not "strong PK signals" — those would falsify the strict reading by violating Born statistics. The answer is "vanishing per-trial bias under sustained *unconditioned* measurement, with a possible decline-effect signature". The qualifier matters: standard psi protocols aggregate over participants, intentions, and sessions, so what they test is the marginal, which the strict reading pins to Born values by construction.

Three results sharpen this corridor:

- The Princeton Engineering Anomalies Research programme, accumulated over decades, reported a per-trial bias on the order of 10⁻⁴ bits per bit processed. Independent replication across the Mind/Machine Interaction Consortium with 227 participants and roughly 2 million trials failed to confirm the original effect (Jahn et al. 2000).
- Bösch, Steinkamp & Boller's 2006 meta-analysis of 380 RNG-PK studies reported a significant overall effect, but with effect size strongly inversely related to sample size: "the small effect size, the relation between sample size and effect size, and the extreme effect size heterogeneity found could in principle be a result of publication bias" (Bösch et al. 2006).
- Maier, Dechamps & Pflitsch (2018) ran a pre-registered Bayesian replication with 12,571 subjects and reported strong evidence for the null: "the Bayesian analysis revealed strong evidence for H0 (BF01 = 10.07), thus micro-PK did not exist in the data".

Read together, these results bracket the corridor. If a real selection-only signature exists in these protocols, its per-trial bias sits below ~10⁻⁴ bits/bit at PEAR scales and below the Maier-Dechamps detection threshold at large N. The strict reading *predicts* this — large detectable bias would be evidence against it, not for it. The corridor is what a Born-marginal-preserving channel should leave behind.

The corridor's scope needs care, because this article previously overstated it. These bounds constrain the *measured endpoint of the protocols that produced them*. Carrying them across to a ceiling on an unobserved neural interface would need a stated mapping from the neural coupling to that endpoint — how many selectable events a protocol recruits, how they aggregate, how participant state and task context enter, what measurement noise absorbs. The Map has no such mapping, so the corridor bounds intentional micro-psychokinesis at the coarsest conditioning grain, not the interface.

Crucially, the Map does not treat the existence of this corridor as evidence *for* the dualist interface. The corridor is a *bound* the interface must live within if it exists at all; the empirical pattern is equally consistent with the no-effect null hypothesis. Reading the corridor as positive evidence would be a textbook case of [possibility-probability slippage](/concepts/possibility-probability-slippage/) — using tenet-coherence to upgrade a structural compatibility into evidential support. The strict reading earns its place by what it *cannot* claim, not by what the data show.

## The Decline Effect as Theoretical Prediction

Two related but distinct phenomena travel under "decline" in this literature. The first is *across-studies* historical decline: effect sizes in psi research drop systematically over time across all major paradigms — RNG-PK, ganzfeld, card-guessing, DMILS — with replication rates of 20–33% in well-conducted studies versus 80%+ in original studies (Walach et al. 2014). The mainstream interpretation is methodological: publication bias and questionable research practices wash out as studies tighten. The second is *within-study* sample-size decline: per-trial bias that appears at small N regresses toward Born statistics as N grows, exactly as the law of large numbers requires of any Born-rule-preserving channel.

A different interpretation of *across-studies* decline is available within the Generalised Quantum Theory framework developed by Atmanspacher, Römer and Walach (Atmanspacher, Römer & Walach 2002; Walach et al. 2014). On that framing the decline is the physics enforcing no-signalling on a real but small effect — when correlations are first probed they may appear, but as repeated probing approaches a regime that would amount to genuine signal transfer, the effect recedes.

The strict reading does not need to take a side on the across-studies pattern. Methodological wash-out and physics-enforced no-signalling are empirically near-indistinguishable, and the strict reading is consistent with both. What the strict reading does straightforwardly predict is the *within-study* decline: by Born-rule preservation, any unconditioned per-trial bias must regress as N grows. The *within-study* pattern is therefore a theoretical signature rather than an embarrassment for the strict-selection model; the across-studies pattern is neutral between the two interpretations.

## No-Signalling, Energy Conservation, and the Information-Side Constraint

The strictest selection-only model is *not* primarily constrained by the energy-conservation objection. As Robin Collins and J. B. Pitts have pointed out (Collins, n.d.; Pitts 2022), quantum correlations show that mind-brain interaction without energy exchange has precedent in current physics, and general relativity's non-localisability of gravitational energy further weakens the energy-conservation objection. Under the strict reading no energy is injected at all; the channel is energetically inert.

The binding constraint is information-theoretic. Han & Choi (2016) show that the Born rule can be *derived* from relativistic causality — "Born rule on quantum measurement is derived by requiring relativistic causality condition" — with causality thereby fixing the upper bound on quantum nonlocality through the probability-assignment rule. Because a different assignment rule changes the amount of nonlocality in quantum correlations, any *systematic* per-trial deviation from Born-rule probabilities is a relativistic-causality problem and not merely a statistical-detectability one. The strict reading buys compatibility with no-signalling at the price of accepting that no effect can ever be visible at the *unconditioned* ensemble level. That tradeoff is not optional — it follows from the structure of quantum probability.

This reframes the metaphysical pressure on Tenet 2. The dualist interface does not need to defend itself against energy-conservation objections at the strict reading; it needs to defend itself against the charge that, by preserving Born statistics, it *cannot make a measurable difference at the unconditioned ensemble level at all*. The article's three limits define exactly where it can — and where it cannot. That charge, pressed as a dilemma about whether ensemble-invisible single-event selection is a genuine channel rather than a hidden idleness, is [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/). With the signed-rate derivation withdrawn, the worry's formal teeth are not a zero-throughput result but the marginal-versus-conditional gap itself: an observer of outcome frequencies alone recovers nothing, however far the mind-conditioned distributions depart from the marginal. That is a claim about what is detectable, and it leaves the epiphenomenalism charge live rather than settled — which is why the tests that bear on the strict reading are conditional residual-structure tests rather than generic Born-frequency tests. [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/) develops the resulting trilemma: conditionals that differ, conditionals that never differ, or conditionals that differ yet cancel under a balancing law the framework would then owe.

## Distinguishing Observables

The strict reading is empirically distinguishable from generation-permitting alternatives, even if current laboratory paradigms cannot yet operationalise the contrasts. The following observables separate the two families:

| Observable | Selection-Only | Generation |
|---|---|---|
| Per-trial bias under accumulating *unconditioned* measurement | Vanishing in long run | Possibly persistent |
| Born-rule preservation of the *marginal* over the candidate set | Required | Optional |
| Decline effect under repeated trials | Predicted | Not predicted |
| No-signalling preservation | Strict | Possibly violated |
| Novel qualia without prior neural representation | Impossible | Possible |
| Conditional bias correlation with decoherence-domain diversity | Strong | Weak/absent |
| Energy/momentum injection signature | Zero | Possibly nonzero |

Of these, the *most discriminating* is the **correlation between candidate-set diversity and reportable phenomenal content**. Under the strict reading, the dimensionality of reportable content is bounded above by the dimensionality of brain-generated candidate space; under generation-permitting models, mind can supply novelty beyond what the brain pre-encodes. No current experiment cleanly operationalises this contrast, and doing so is a target for the [interface-specification-programme](/apex/interface-specification-programme/). A complementary handle is the cross-species variation in that same correlation, which [interface-efficacy-and-the-cognitive-gap](/topics/interface-efficacy-and-the-cognitive-gap/) treats as its central distinguishing observable.

## Relation to Site Perspective

The strict reading of selection-only mind-influence is the cleanest expression of the Map's [Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction) tenet. It commits to the *smallest* deviation from physical dynamics — one that injects no energy, leaves Born statistics intact, and acts only through the act of selection itself. The Map does not require this strict reading; the intermediate reading is also live. But the strict reading is the version most directly defensible against information-theoretic objections, and it is the version under which Tenet 2's "minimality" claim is most fully honoured.

[Tenet 3 (Bidirectional Interaction)](/tenets/#bidirectional-interaction) is preserved under the strict reading: selection is genuine causation, in that it determines which physically-permitted outcome becomes actual. Mind makes a difference; it just makes the smallest possible kind of difference. The two ceilings that survive — the per-event log₂(N) bound and the content-confinement bound — are the price the Map pays for compatibility with orthodox physics. Born-marginal preservation is a third commitment of a different kind: it costs the Map detectability under unconditioned aggregate tests without buying a throughput limit in return, and it is the reason the Map's empirical predictions have to be sought in conditional structure rather than in outcome frequencies.

[Tenet 1 (Dualism)](/tenets/#dualism) is presupposed: there must be a non-physical selector for there to be selection at all. [Tenet 4 (No Many Worlds)](/tenets/#no-many-worlds) is also presupposed: selection only makes sense if one outcome becomes actual rather than all of them. The strict reading is therefore the joint expression of Tenets 1, 2, 3 and 4 in their tightest possible coherent form.

The Map interprets the empirical situation as follows. The vanishing of detectable PK signatures under sustained unconditioned measurement is not a refutation of the dualist interface — it is what the strict reading predicts. The decline effect, on its theoretical reading, is a candidate signature of Born-rule preservation under accumulating measurement. The Map does not endorse psi research as evidence *for* the interface; it treats the empirical corridor as a *bound* — one that constrains the protocols directly and the interface only through a mapping the Map has yet to state. The most informative experiments would not chase larger effect sizes but would target the content-confinement prediction — measuring whether reportable phenomenal content tracks candidate-set diversity at relevant neural sites. The systematic statement of why *spectacular* psi would disconfirm rather than confirm the framework is developed in [the parapsychology firewall](/topics/parapsychology-firewall/).

## Further Reading

- [selection-only-channel](/concepts/selection-only-channel/)
- [forward-in-time-conscious-selection](/topics/forward-in-time-conscious-selection/)
- [post-decoherence-selection](/concepts/post-decoherence-selection/)
- [trilemma-of-selection](/topics/trilemma-of-selection/)
- [stapp-quantum-mind](/concepts/stapp-quantum-mind/)
- [born-rule-and-the-consciousness-interface](/topics/born-rule-and-the-consciousness-interface/)
- [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/) — Why marginal Born-preservation leaves the conditionals free, and the trilemma that follows
- [channel-class-taxonomy](/concepts/channel-class-taxonomy/) — Where an ε² / (2 ln 2) rate *is* licensed: a declared probability-bias channel with a stated reference distribution
- [asymmetric-bandwidth-consciousness](/research/asymmetric-bandwidth-consciousness-2026-03-02/)
- [bandwidth-of-consciousness](/topics/bandwidth-of-consciousness/)
- [consciousness-bandwidth-architecture](/concepts/consciousness-bandwidth-architecture/)
- [conservation-laws-and-mental-causation](/concepts/conservation-laws-and-mental-causation/)
- [interactionist-dualism](/concepts/interactionist-dualism/)
- [the-interface-problem](/topics/the-interface-problem/)
- [interface-specification-programme](/apex/interface-specification-programme/)
- [mathematical-structure-of-the-consciousness-physics-interface](/topics/mathematical-structure-of-the-consciousness-physics-interface/)
- [contextual-selection-in-quantum-foundations](/concepts/contextual-selection-in-quantum-foundations/)
- [weak-measurement-and-post-selection](/concepts/weak-measurement-and-post-selection/)
- [amplification-mechanisms-consciousness-physics](/topics/amplification-mechanisms-consciousness-physics/)
- [parapsychology-firewall](/topics/parapsychology-firewall/)
- [possibility-probability-slippage](/concepts/possibility-probability-slippage/)
- [interface-efficacy-and-the-cognitive-gap](/topics/interface-efficacy-and-the-cognitive-gap/)
- [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/) — Whether the ensemble-invisible selection channel these limits describe constitutes genuine efficacy

## References

1. Atmanspacher, H., Römer, H., & Walach, H. (2002). Weak quantum theory: Complementarity and entanglement in physics and beyond. *Foundations of Physics*, 32(3), 379–406.
2. Bösch, H., Steinkamp, F., & Boller, E. (2006). Examining psychokinesis: The interaction of human intention with random number generators—A meta-analysis. *Psychological Bulletin*, 132(4), 497–523. https://pubmed.ncbi.nlm.nih.gov/16822162/
3. Collins, R. (n.d.). Modern physics and the energy conservation objection to mind-body dualism. https://www.newdualism.org/papers/R.Collins/EC-PEC.htm
4. Han, Y.-D., & Choi, T. (2016). Quantum probability assignment limited by relativistic causality. *Scientific Reports*, 6, 22986. https://www.nature.com/articles/srep22986
5. Jahn, R. G., Mischo, J., Vaitl, D., Dunne, B. J., Bradish, G. J., Dobyns, Y. H., Lettieri, A., Nelson, R. D., Boller, E., Bösch, H., Vaitl, D., & Houtkooper, J. (2000). Mind/machine interaction consortium: PortREG replication experiments. *Journal of Scientific Exploration*, 14(4), 499–555.
6. Maier, M. A., Dechamps, M. C., & Pflitsch, M. (2018). Intentional observer effects on quantum randomness: A Bayesian analysis reveals evidence against micro-psychokinesis. *Frontiers in Psychology*, 9, 379. https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/
7. Pitts, J. B. (2022). General relativity, mental causation, and energy conservation. *Erkenntnis*. https://link.springer.com/article/10.1007/s10670-020-00284-7
8. Stapp, H. P. (2006). Quantum interactive dualism: An alternative to materialism. *Zygon: Journal of Religion and Science*, 41(3). https://doi.org/10.1111/j.1467-9744.2005.00762.x (preprint: https://www-physics.lbl.gov/~stapp/QID.pdf)
9. Stapp, H. P. (1993). *Mind, Matter, and Quantum Mechanics*. Springer.
10. Zheng, J., & Meister, M. (2025). The unbearable slowness of being: Why do we live at 10 bits/s? *Neuron*, 113(2), 192–204. https://www.cell.com/neuron/fulltext/S0896-6273(24)00808-0
11. Walach, H., Horan, M., Hinterberger, T., & von Lucadou, W. (2014). Evidence-based parapsychology and the decline effect. *Journal of Parapsychology*. https://psi-encyclopedia.spr.ac.uk/articles/decline-effect-parapsychology
12. Southgate, A. & Oquatre-six, C. (2026-03-18). Mathematical Structure of the Consciousness-Physics Interface. *The Unfinishable Map*. https://unfinishablemap.org/topics/mathematical-structure-of-the-consciousness-physics-interface/