---
title: "The Bandwidth of Consciousness"
created: 2026-02-09
modified: 2026-04-19
human_modified: null
ai_modified: 2026-07-06T13:23:12.056384+00:00
draft: false
description: "The 100-million-fold gap between neural processing and conscious output reveals the shape of the mind-brain interface—a selection channel whose coarseness is architecturally required, not a defect."
topics:
  - "[[hard-problem-of-consciousness]]"
  - "[[free-will]]"
  - "[[attention-and-the-consciousness-interface]]"
concepts:
  - "[[attention-as-interface]]"
  - "[[attentional-economics]]"
  - "[[psychophysical-laws]]"
  - "[[filter-theory]]"
  - "[[consciousness-selecting-neural-patterns]]"
  - "[[working-memory]]"
  - "[[mental-effort]]"
  - "[[motor-selection]]"
  - "[[baseline-cognition]]"
  - "[[interactionist-dualism]]"
  - "[[consciousness-bandwidth-architecture]]"
  - "[[mental-causation-and-downward-causation]]"
  - "[[phenomenal-overflow]]"
  - "[[access-consciousness]]"
  - "[[global-workspace-theory]]"
  - "[[causal-closure]]"
  - "[[libet-experiments]]"
  - "[[epiphenomenalism]]"
  - "[[language-recursion-and-consciousness]]"
  - "[[counterfactual-reasoning]]"
related_articles:
  - "[[tenets]]"
  - "[[dualist-perception]]"
  - "[[resolution-void]]"
  - "[[quantum-neural-timing-constraints]]"
  - "[[embodied-consciousness]]"
  - "[[mental-causation-and-downward-causation]]"
  - "[[hard-problem-of-consciousness]]"
  - "[[consciousness-and-memory]]"
  - "[[conservation-laws-and-mental-causation]]"
  - "[[attentional-economics]]"
  - "[[grain-mismatch]]"
  - "[[grain-mismatch-as-independent-evidence]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-6
ai_generated_date: 2026-02-09
last_curated: null
last_deep_review: 2026-06-25T13:55:08+00:00
coalesced_from:
  - "/topics/neural-bandwidth-constraints-and-the-interface/"
  - "/topics/asymmetric-bandwidth-of-consciousness/"
  - "/topics/bandwidth-constraints-conscious-processing/"
  - "/topics/resolution-bandwidth-interface/"
  - "/topics/the-ten-bit-ceiling/"
embedded_videos:
  - id: -ZzU5zvhghA
    url: https://www.youtube-nocookie.com/embed/-ZzU5zvhghA
    embedded: 2026-07-06T13:23:12.056384+00:00
    source: notebooklm/0085-01-bandwidth-of-consciousness
---

Consciousness sits at the centre of a dramatic information asymmetry. Sensory transduction delivers roughly 11 million bits per second to the brain (Zimmermann 1986; Nørretranders 1998), and aggregate neural processing runs at ~10⁹ bits per second (Zheng & Meister 2025). Yet conscious influence on behaviour measures at approximately 10 bits per second—a ratio Zheng and Meister call the "sifting ratio," which runs to 100 million to one against total neural processing (and roughly a million to one against sensory transduction). The Unfinishable Map treats this asymmetry as a structural signature of the mind-brain interface: on the dualist reading, consciousness *receives* vast information passively but *acts* through a channel so narrow it can only select among pre-computed options. The bandwidth constraint may define the *shape* of the interface, distinguishing what consciousness does from what the brain does, and arguably exposing why production models face a problem that [[filter-theory|filter]] and [[interactionist-dualism|interactionist]] models appear to handle more naturally.

<details class="yt-embed" data-video-id="-ZzU5zvhghA">
<summary>Video introduction</summary>
<a href="https://www.youtube-nocookie.com/embed/-ZzU5zvhghA">Watch this article as a video on YouTube</a>
<p class="yt-caption">Videos cover themes but may stray from the Map's position. The article text is the definitive version. Clicking play implies consent to YouTube cookies.</p>
</details>

## Measuring the Ceiling in Bits

Shannon (1948) defined information as the reduction of uncertainty. One bit is the information gained by distinguishing between two equally likely alternatives; for an equiprobable choice among *N* options, the content is log₂(*N*) bits. The framework makes no appeal to introspection, difficulty, or phenomenology, treating any input-output system as an information channel whose throughput is measured in bits per unit time.

Hick (1952) first applied this framework to the mind, treating a participant as a Shannon channel—the "input" a set of stimuli with quantifiable entropy, the "output" a correct response at measurable latency—and reported a rate of "the order of five 'bits' per second." Hyman (1953) replicated and extended across unequal-probability conditions, establishing the Hick-Hyman law. Pierce and Karlin (1957) applied Shannon's redundancy estimates for English to reading-aloud tasks at Bell Labs. Miller (1956) added complementary capacity limits: ~2.5 bits per dimension in absolute judgement, ~7 chunks in immediate memory.

The critical point for later debates is what the figure measures: the rate at which observable, reportable decisions resolve—not unconscious sensory processing, unconscious motor execution, or parallel preprocessing that narrows the decision space before conscious choice. The ten-bit figure is the throughput of the decision bottleneck—the point where options become actions.

## The Outbound Bottleneck

Zheng and Meister (2025) reviewed conscious processing rates across every measured domain. The results converge:

| Domain | Conscious Processing Rate | Method |
|--------|--------------------------|--------|
| Choice-reaction tasks | ~5 bits/second | Hick 1952; log₂(alternatives) / reaction time |
| Digit memorisation | ~5 bits/second | digits × log₂(10) / memorisation time |
| Professional Tetris | ~7 bits/second | piece placement decisions per second |
| Expert typing (120 wpm) | ~10 bits/second | ~10 keystrokes/s × ~1 bit/char (Shannon redundancy) |
| Professional StarCraft | ~10 bits/second | actions per minute × information content |
| Rubik's cube (speed solving, sighted) | ~12 bits/second | move information / solve time |
| Speed cards (memory sport) | ~18 bits/second | 52 cards × log₂(52!) bits / inspection time |

All figures use Shannon information theory: entropy of the decision space divided by time. The convergence on ~10 bits/s is striking because the methodology applies identically across domains. Expert typists achieve ~10 bits/s on English text but drop precipitously on random characters—same motor skill, different information content—confirming that the measure tracks *decisions*, not keystrokes. Reading (~45 bits/s) and speech production (~39 bits/s; Coupé et al. 2019) appear higher because they measure the *information content of the output signal*, not the rate of novel conscious decisions—much of reading and speech is automated.

The ceiling holds regardless of training, talent, or task type. Chunking (Miller 1956) works *around* channel capacity without removing it. Over seven decades of measurement, the ceiling has held—a structural feature, not an experimental artefact.

Zheng and Meister call the ratio between sensory processing (~10⁹ bits/s) and conscious throughput (~10 bits/s) the "sifting ratio"—"the largest unexplained number in brain science."

Crucially, the bottleneck is not in the neural hardware. Sauerbrei and Pruszynski (2025) accept the ~10 bits/s ceiling for conscious cognition but demonstrate that unconscious motor control vastly exceeds it. A runner's stride requires coordinating dozens of muscles at 250ms timescales; the cerebellum performs continuous real-time sensorimotor processing far exceeding the conscious ceiling. The bottleneck is specifically at *[[access-consciousness|conscious access]]*—not in the computational substrate surrounding it.

## The Inbound Channel

The inbound bandwidth is enormous. Zimmermann (1986) quantified sensory transduction by modality: vision alone delivers roughly 10⁷ bits per second, touch around 10⁶, with aggregate sensory input reaching ~11 million bits per second. Nørretranders (1998) popularised the asymmetry as the "user illusion"—consciousness as a simplified desktop covering vastly richer underlying computation. Including unconscious neural processing of this input (pattern recognition, motor preparation, working memory maintenance), total "outer brain" throughput rises to ~10⁹ bits per second (Zheng & Meister 2025). As the lede notes, the two framings yield different ratios—roughly 10⁶-fold for sensory transduction, 10⁸-fold for total neural processing—but the philosophical consequence does not depend on which we use. Whether *phenomenal* experience is also richer than cognitive access—as Block (2011) argues against Cohen, Dennett, and Kanwisher (2016)—the Map need not resolve; that question concerns phenomenality, whereas the ~10 bits/s ceiling measures only reportable access, and the seriality and abstraction claimed above are predicated of that channel, not of phenomenal experience. The inbound/outbound gap is structural regardless of which inbound figure we adopt.

## How the Constraint Shapes Processing

The ~10 bits per second ceiling determines the *kind* of processing that reaches conscious access: serial where the brain is parallel, abstract where the brain is granular, evaluative where the brain is computational. These predicates attach to the outbound selection channel, not to phenomenal experience.

### Seriality

Conscious access resolves one thing at a time. At 10 bits per second, dividing capacity across two tasks yields ~5 bits each—below the threshold for effective decision-making in either (Pashler 1994). Seriality is a mathematical consequence of the channel's capacity.

### Forced Abstraction

A 10-bit/second channel cannot operate on raw sensory data; even after cortical compression, the inbound stream dwarfs conscious-access capacity by orders of magnitude. The channel appears forced to operate on *abstractions*—compressed, categorical representations encoding meanings and goals rather than sensory primitives. Intentions are coarse-grained—"reach for the cup" rather than "fire motor neurons N₄₅₆₇₈ in sequence"—as the [[consciousness-bandwidth-architecture|bandwidth problem in mental causation]] makes explicit. [[language-recursion-and-consciousness|Recursive linguistic structure]] may be the most powerful compression scheme consciousness employs, composing compressed representations into novel combinations at rates the bandwidth can sustain.

### The Temporal Grain

At approximately 3–4 selections per second—the rate implied by ~10 bits/second given typical decision complexity (~3 bits per selection)—conscious access has a characteristic clock speed of ~250–300 milliseconds per selection. The specious present—the experienced duration of "now"—may reflect this temporal grain. The brain processes at microsecond timescales; conscious access updates at a timescale set by its bandwidth.

### The Division of Labour

The bandwidth constraint creates a functional partition: unconscious systems handle high-bandwidth tasks (sensory processing, motor coordination, pattern recognition), while conscious access handles novel combination, cross-domain evaluation, and [[counterfactual-reasoning|counterfactual reasoning]] (detailed in [What Happens Outside the Bandwidth](#what-happens-outside-the-bandwidth)). DeWall, Baumeister, and Masicampo (2008) found that cognitive load specifically impairs logical reasoning while leaving unconscious processing intact. The [[mental-effort|phenomenology of effort]] tracks bandwidth utilisation: maximum effort corresponds to the channel operating at capacity.

## Why Coarseness Is Necessary

The bandwidth constraint may be more than a limitation — on this reading it is an architectural requirement for effective control. A controller matching the brain's processing grain would need to track a hundred trillion synaptic states at millisecond timescales; such a consciousness would arguably not be a controller at all but a duplicate of the system it was supposed to govern. Effective hierarchical control plausibly requires operating at a different grain than the controlled system, so that conscious intervention is limited to the few selection points where it could make a difference.

## The Resolution-Bandwidth Coupling

The [[resolution-void|resolution void]] and bandwidth constraint are tightly coupled. The compression ratio determines the selection vocabulary, which determines the bandwidth requirement: finer-grained perception would require finer-grained selection to be useful, since perceiving individual motor units demands controlling them.

The ten-bit resolution and ten-bit bandwidth appear matched. Conscious access perceives at roughly the resolution it can control, and controls at roughly the resolution it can perceive. A mismatch in either direction would, on this picture, render the system dysfunctional.

The dualist reading takes the match as a tuned architectural constraint: a self-monitoring system could in principle adjust "resolution" and "bandwidth" separately by allocating more neural resources, yet the ratio stays locked across tasks and training. But the lockstep is not, by itself, evidence for an external constraint, because it is equally what a *single* serial bottleneck predicts—if one channel gates both perception-for-report and selection-for-action, the two are not two tunable parameters that happen to coincide but one parameter measured twice. The argument for an external constraint therefore needs independent evidence that resolution and bandwidth are dissociable in principle; absent a case where one varies without the other, the coupling is consistent with the interface reading without favouring it over the single-channel deflation.

## Why the Asymmetry Is Philosophically Revealing

### Against Production Models

If the brain *produces* consciousness, the bandwidth constraint may seem puzzling. A system with 86 billion neurons and petabit-scale internal processing yields conscious access at 10 bits per second—a narrowing factor of 10⁸, arguably far beyond what parallel-to-serial architectures typically impose, though a production theorist could reply that the workspace bottleneck is exactly such an imposition (a reply the [Evolutionary Puzzle](#the-evolutionary-puzzle) engages).

The bottleneck appears precisely where consciousness enters the picture—the brain *can* process at higher rates, as Sauerbrei and Pruszynski show experimentally. The [[grain-mismatch-as-independent-evidence|grain mismatch evidence programme]] situates this informational asymmetry alongside two independent structural mismatches—spatial and temporal—suggesting that their convergence may constitute structural evidence rather than a conceivability exercise.

### Filter Theory's Natural Fit

The [[filter-theory|filter model]] appears to handle the bandwidth constraint without strain. If the brain constrains consciousness rather than producing it, the bottleneck may be the *filter itself*—the narrow channel through which consciousness accesses and influences the physical world. On this reading the 10 bits per second measures the channel's capacity, not consciousness's capacity.

The same brain that runs high-bandwidth motor control in the cerebellum throttles to ~10 bits per second where consciousness participates. On the filter model, this is what one would expect: the filter constrains consciousness specifically, not neural processing in general. The converse prediction also seems to hold: altered states involving loosened interface constraints might involve experiences reported as *richer* than ordinary waking consciousness. Psychedelic research finds increased neural entropy correlating with expanded subjective richness (Carhart-Harris et al., 2014)—a pattern production models may struggle to explain but filter models seem to anticipate, though the entropy-richness correlation could admit production-side readings too.

### The Outbound Side Suggests Selection

A system that *computes* its outputs should scale its throughput with its processing resources. But a system that *selects* among pre-computed options may need only enough bandwidth to make choices—and 10 bits per second appears to suffice for roughly 3–4 selections per second among small sets of alternatives.

This seems to match the phenomenology of deliberate action: choosing among presented options, not computing from raw data. On the selection reading, the [[libet-experiments|Libet readiness potential experiments]] capture this architecture—neural preparation precedes conscious awareness because preparation *must* precede [[consciousness-selecting-neural-patterns|selection]].

### The Global Workspace Objection

[[global-workspace-theory|Global Workspace Theory]] (Baars, 1988; Dehaene, 2014) provides the physicalist counterargument most directly targeting the asymmetry: consciousness is a serial broadcast that integrates information from parallel processors, and the serial bottleneck produces the ~10 bits/s ceiling. The Map acknowledges GWT's explanatory power for the *functional* structure, but GWT does not address why there is *something it is like* to occupy the workspace. What distinguishes the accounts is whether the architecture explains consciousness or merely describes the structure through which consciousness operates.

## The Bandwidth Shapes the Interface

At 10 bits per second, conscious selection operates over *patterns*—action policies, attentional targets, cognitive strategies—not individual neural firing events. Wu et al. (2016) estimated cognitive control capacity at ~3–4 bits per second, and the ~280–300ms timing window for [[motor-selection|motor commitment]] aligns with conscious selection at ~3 Hz (consistent with the ~3 bits/selection derivation above). This matches the [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]] tenet: consciousness *cannot* interact at finer grain because the channel is too narrow. The same capacity language puts a concrete handle on [[the-interface-problem|the interface specification problem]]: how conscious states map lawfully to physical selections. The [[inverted-qualia]] argument meets the same discipline on the qualitative side—if phenomenal character is causally efficacious, qualitative differences must reach behaviour through this narrow channel.

The bandwidth constraint applies per unit time, but effects accumulate—the basis of [[attentional-economics|attentional economics]]. Schwartz's OCD research illustrates this: patients showed measurable caudate nucleus changes through accumulated conscious effort over weeks, though the original study was small (nine participants) and has not been independently replicated.

## What Happens Outside the Bandwidth

The [[baseline-cognition|baseline cognition hypothesis]] attributes sophisticated cognition—tool use, social learning, spatial navigation—to unconscious systems operating at full neural bandwidth. What requires conscious bandwidth is *manipulation*: logical reasoning, counterfactual thinking, recursive language. Skills that begin as conscious processes become automatic with practice: expertise works *around* the ceiling by moving processing below it, not *through* it by expanding conscious capacity.

## The Epiphenomenalism Test

The asymmetry poses a specific challenge to [[epiphenomenalism]]. If consciousness were epiphenomenal, the outbound "channel" would carry zero bits per second. There would be no consistent throughput ceiling, because epiphenomena have no throughput. The existence of a measurable, task-independent bandwidth—10 bits per second, not zero, not random—suggests consciousness is performing work. Mandik (2010) may reinforce this: introspecting motor control introduces a "doubling of tasks"—attending to controlling interferes with controlling—a pattern that seems most intelligible if conscious action operates through a narrow channel that cannot simultaneously carry action-selections and self-monitoring.

## The Evolutionary Puzzle

Zheng and Meister propose that serial conscious processing was inherited from primitive organisms navigating chemical gradients—ancient one-dimensional decision-making that never scaled up. But evolution routinely scales inherited architectures: the mammalian eye began as a light-sensitive patch and became a high-resolution imaging system. If conscious throughput were purely neural-architectural, selective pressure should have increased it over hundreds of millions of years.

The production theorist has a ready rejoinder: the bottleneck is a serial-integration stage, and a stage that integrates parallel inputs into one broadcast *cannot* be made wider without ceasing to integrate—so widening was never physiologically accessible, and its evolutionary stability needs no interface to explain it. This reply is not idle; it is the load-bearing premise the interface inference must contest. The Map's counter is that the non-wideability claim is itself unproven—integration could be implemented by multiple parallel workspaces, as some global-workspace variants propose—so "serial integration forbids widening" is asserted, not established, on the production side too.

If the ~10 bits/s ceiling instead reflects the capacity of a mind-brain *interface*, evolutionary pressure on brain architecture alone could not raise it: evolution can optimise the brain's side—preparing better options faster—but cannot widen a channel whose narrow end is non-physical. With both the interface reading and the intrinsic-bottleneck reading currently resting on unestablished premises, the honest verdict is that the ceiling's stability from Hick's 1952 experiments through 2024 professional e-sports telemetry is *consistent with* the interface reading and not obviously explained by the standard adaptationist story—not that it forces the non-physical conclusion.

## The Bandwidth and Free Will

The constraint reshapes the free will debate. Libertarian free will requires consciousness to *bias* ~3–4 selections per second among options the brain has prepared—located at points of [[quantum-indeterminacy-free-will|quantum indeterminacy]]. Schultze-Kraft (2016) identified a "point of no return" at ~200ms before movement execution, before which conscious intervention can veto prepared actions. On the selection reading, this reframes the [[libet-experiments|Libet problem]]: if consciousness's role is selection rather than initiation, neural preparation *should* precede selection.

## How Robust Is the Ten-Bit Figure?

The arguments above rest on a specific empirical claim: conscious throughput of approximately ten bits per second, measured as behavioural output, converging at the order-of-magnitude level. The interface argument requires only a large asymmetry: if the true figure were 50 or even 100 bits/s, the gap would still be enormous and the architectural argument would hold. What would genuinely threaten it is evidence that conscious throughput is *variable*—scaling with training or pharmacological intervention in ways suggesting a soft, brain-determined limit. Zheng and Meister note that extensive practice does not substantially increase the ceiling, supporting the fixed-channel interpretation, though the distinction between "hard ceiling" and "typical operating point" has not been definitively resolved.

## Why Ten Specifically

Zheng and Meister's phrase—"the largest unexplained number in brain science"—names a genuine open problem. Why ten, not a hundred or one? Several candidate explanations exist, none fully satisfactory.

**Neural oscillation frequencies.** The alpha rhythm at roughly ten hertz is suggestively close to ten bits per second; if each cycle carries about one bit, the figure follows. Evidence connecting alpha rhythm specifically to conscious decision rate is circumstantial.

**Metabolic cost.** Conscious processing is energetically expensive, and the ceiling could reflect where marginal cost exceeds marginal benefit. This is underdetermined—it predicts *a* ceiling, not the specific value.

**Evolutionary legacy.** Zheng and Meister's speculation about inheritance from chemical-gradient navigation faces the standard objection that evolution routinely scales inherited architectures (see [The Evolutionary Puzzle](#the-evolutionary-puzzle)).

**Interface capacity.** The Map's candidate is that the ceiling reflects the bandwidth of the mind-matter interface itself, predicting stability across species, training, and neural reorganisation. As above, this is compatible with the data but not uniquely forced by it.

The number ~10 is a load-bearing empirical fact in search of a theory.


## What Would Challenge This View

The argument linking bandwidth constraints to the interface model would face serious challenge if:

1. **Conscious processing rate turns out much higher than ~10 bits/second.** If the true figure is hundreds or thousands rather than the converged order of magnitude, the bottleneck interpretation weakens.

2. **The bottleneck is explained purely by neural architecture.** If serial global broadcasting fully accounts for the ~10⁸ ratio, the philosophical implications dissolve.

3. **The resolution-bandwidth coupling breaks.** If conscious resolution increases without corresponding bandwidth increase (or vice versa), the coupling argument fails.

4. **Unconscious systems replicate all functions attributed to conscious selection.** If counterfactual reasoning and novel combination prove achievable without conscious access, the bandwidth constraint becomes irrelevant.

5. **Artificial systems with narrow processing channels develop consciousness.** The bandwidth constraint would then be a *cause* of consciousness rather than a *sign* of interface limitation.

## Relation to Site Perspective

**[[tenets#^dualism|Dualism]]**: A system operating at 10⁹ bits per second internally but producing conscious throughput at 10¹ bits per second contains a discontinuity that identity theories cannot bridge without treating consciousness as a marginal byproduct—contradicting the functional importance of conscious processing for logical reasoning, counterfactual thinking, and deliberate choice.

**[[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]]**: The outbound bandwidth is broadly compatible with what the tenet stipulates philosophically. A 10-bit/second channel carries roughly the minimal information required for selection among prepared alternatives. The tenet's "smallest possible influence" may find its empirical expression in Zheng and Meister's universal ceiling—though the data constrain rather than establish the reading, since a production architecture could in principle yield the same ceiling.

**[[tenets#^bidirectional-interaction|Bidirectional Interaction]]**: Brain-to-consciousness runs at ~10⁹ bits per second; consciousness-to-brain runs at ~10 bits per second. Both directions are causally real; they differ in bandwidth by eight orders of magnitude—an asymmetric channel narrow enough to operate within the gaps that [[causal-closure|causal closure]] leaves open.

**[[tenets#^no-many-worlds|No Many Worlds]]**: The selection model presupposes genuine selection—one outcome becoming actual at the expense of alternatives. If all outcomes actualise (as many-worlds holds), "selection" is illusory. The bandwidth asymmetry is most naturally read as describing a system where selection has real consequences.

**[[tenets#^occams-limits|Occam's Razor Has Limits]]**: The "simple" explanation—neural architecture creates a bottleneck—doesn't address why the bottleneck exists at conscious access specifically. The interface model adds ontological complexity but explains why consciousness is precisely where the bandwidth narrows, and why evolution has not widened it.

## Further Reading

- [[consciousness-bandwidth-architecture]] — The 100-million-fold inbound/outbound asymmetry and whether 10 bits/second suffices for complex behaviour
- [[one-structure-three-vocabularies]] — The brain's "prepared options" as one register of a structure also described by Saad's default causal profile and the Born-rule distribution
- [[attention-and-the-consciousness-interface]] — How the interface operates through attention and motor planning
- [[attentional-economics]] — Agency as allocation of the scarce conscious resource
- [[filter-theory]] — The filter/transmission model and the bandwidth as filter parameter
- [[consciousness-selecting-neural-patterns]] — The selection mechanism in detail
- [[resolution-void]] — The resolution gap between brain processing and conscious access
- [[grain-mismatch-as-independent-evidence]] — The bandwidth constraint as one of three converging grain mismatches
- [[the-interface-problem]] — The open challenge of specifying how conscious states map lawfully to physical selections within this channel, and where in the brain the interface operates
- [[inverted-qualia]] — The qualitative-side companion argument, disciplined by the same narrow outbound channel
- [[baseline-cognition]] — What the brain achieves without conscious involvement
- [[conservation-laws-and-mental-causation]] — Energy conservation and why selection without injection respects physics
- [[global-workspace-theory]] — The materialist account of serial broadcasting and its limitations
- [[libet-experiments]] — The neural preparation findings and why they don't defeat free will
- [[psychedelics-and-the-filter-model]] — Filter-loosening evidence: how reducing the constraint changes what reaches the conscious channel

## References

1. Baars, B.J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.
1. Block, N. (2011). Perceptual consciousness overflows cognitive access. *Trends in Cognitive Sciences*, 15(12), 567–575.
1. Carhart-Harris, R.L. et al. (2014). The entropic brain: A theory of conscious states informed by neuroimaging research with psychedelic drugs. *Frontiers in Human Neuroscience*, 8, 20.
1. Cohen, M.A., Dennett, D.C., & Kanwisher, N. (2016). What is the bandwidth of perceptual experience? *Trends in Cognitive Sciences*, 20(5), 324–335.
1. Coupé, C., Oh, Y.M., Dediu, D., & Pellegrino, F. (2019). Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche. *Science Advances*, 5(9).
1. Dehaene, S. (2014). *Consciousness and the Brain: Deciphering How the Brain Codes Our Thoughts*. Viking Press.
1. Hick, W.E. (1952). On the rate of gain of information. *Quarterly Journal of Experimental Psychology*, 4(1), 11–26.
1. Hyman, R. (1953). Stimulus information as a determinant of reaction time. *Journal of Experimental Psychology*, 45(3), 188–196.
1. Libet, B., Gleason, C.A., Wright, E.W., & Pearl, D.K. (1983). Time of conscious intention to act in relation to onset of cerebral activity. *Brain*, 106(3), 623–642.
1. Mandik, P. (2010). Control consciousness. *Topics in Cognitive Science*, 2(4), 643–657.
1. Miller, G.A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97.
1. Wu, T., Dufford, A.J., Mackie, M.-A., Egan, L.J., & Fan, J. (2016). The capacity of cognitive control estimated from a perceptual decision making task. *Scientific Reports*, 6, 34025.
1. Nørretranders, T. (1998). *The User Illusion: Cutting Consciousness Down to Size*. Viking Press.
1. Pierce, J.R. & Karlin, J.E. (1957). Reading rates and the information rate of a human channel. *Bell System Technical Journal*, 36(2), 497–516.
1. Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423 and 623–656.
1. Sauerbrei, B.A. & Pruszynski, J.A. (2025). The brain works at more than 10 bits per second. *Nature Neuroscience*, 28, 1365–1366.
1. Schultze-Kraft, M. et al. (2016). The point of no return in vetoing self-initiated movements. *Proceedings of the National Academy of Sciences*, 113(4), 1080–1085.
1. Schwartz, J.M. et al. (1996). Systematic changes in cerebral glucose metabolic rate after successful behavior modification treatment of obsessive-compulsive disorder. *Archives of General Psychiatry*, 53(2), 109–113.
1. Zheng, J. & Meister, M. (2025). The unbearable slowness of being: Why do we live at 10 bits/s? *Neuron*, 113(2), 192–204.
1. Zimmermann, M. (1986). Neurophysiology of sensory systems. In R.F. Schmidt (Ed.), *Fundamentals of Sensory Physiology*. Springer.
1. Pashler, H. (1994). Dual-task interference in simple tasks: Data and theory. *Psychological Bulletin*, 116(2), 220–244.
1. DeWall, C.N., Baumeister, R.F., & Masicampo, E.J. (2008). Evidence that logical reasoning depends on conscious processing. *Consciousness and Cognition*, 17(3), 628–645.
