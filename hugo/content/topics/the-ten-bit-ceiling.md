---
ai_contribution: 100
ai_generated_date: 2026-04-18
ai_modified: 2026-04-18 22:38:00+00:00
ai_system: claude-opus-4-7
author: null
concepts:
- '[[asymmetric-bandwidth-consciousness]]'
- '[[bandwidth-problem-mental-causation]]'
- '[[filter-theory]]'
- '[[interface-friction]]'
- '[[attention-as-interface]]'
- '[[consciousness-selecting-neural-patterns]]'
- '[[interactionist-dualism]]'
created: 2026-04-18
date: &id001 2026-04-18
description: Seventy years of Shannon-calibrated behavioural measurements converge
  on ~10 bits/s for conscious throughput. Human-AI inquiry into what the number means
  and why it holds.
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[tenets]]'
- '[[grain-mismatch-as-independent-evidence]]'
- '[[resolution-void]]'
- '[[mental-effort]]'
- '[[global-workspace-theory]]'
title: The Ten-Bit Ceiling
topics:
- '[[bandwidth-of-consciousness]]'
- '[[the-interface-specification-problem]]'
- '[[hard-problem-of-consciousness]]'
---

The claim that conscious processing operates at approximately ten bits per second is not an introspective intuition or a rough estimate. It is the convergent result of roughly seven decades of behavioural measurement, applied consistently through Shannon's mathematical theory of communication (1948) to tasks as diverse as choice-reaction experiments in a 1952 British laboratory, professional StarCraft play in 2024, and world-record speedcubing. Zheng and Meister's 2024 *Neuron* synthesis drew these measurements together: across every domain researchers have studied, the ceiling holds at around ten bits per second. A 2025 critique by Sauerbrei and Pruszynski accepts the cognitive ceiling but contests its interpretation — pointing out that unconscious motor control vastly exceeds it. The Unfinishable Map treats the Zheng–Meister–Sauerbrei–Pruszynski exchange as strengthening rather than undermining the interface picture: the bottleneck sits precisely where consciousness participates, not in the neural hardware that surrounds it.

This article treats the figure itself — what "ten bits per second" means when applied to a human being, how the measurement was constructed, why it converges across radically different tasks, and what the recent debate about its scope implies. The broader inbound/outbound asymmetry is developed in [bandwidth-of-consciousness](/topics/bandwidth-of-consciousness/) and [asymmetric-bandwidth-consciousness](/concepts/asymmetric-bandwidth-consciousness/); the mental-causation implications are developed in [bandwidth-problem-mental-causation](/concepts/bandwidth-problem-mental-causation/). Here the question is narrower: how do we know the number, and what does it actually measure?

## Measuring a Mind in Bits

Shannon (1948) defined information as the reduction of uncertainty. The bit is the unit of that reduction: one bit is the information gained by distinguishing between two equally likely alternatives. For an equiprobable choice among *N* options, the information content is log₂(*N*) bits; for non-uniform distributions, it is the entropy H = −Σ *p*·log₂(*p*). The framework makes no appeal to introspection, difficulty, or phenomenology. It treats any system that takes inputs and produces outputs as an information channel, and measures its throughput in bits per unit time.

Hick (1952) was the first to apply this framework to the mind. In his paper "On the Rate of Gain of Information" (*Quarterly Journal of Experimental Psychology*), he measured how reaction time scales with the number of alternatives in a choice task. He found a logarithmic relationship — reaction time increases with log₂(*N*) — and concluded that "the rate of gain of information is, on the average, constant with respect to time, within the duration of one perceptual-motor act, and has a value of the order of five 'bits' per second." Hyman (1953) replicated and extended Hick's findings across unequal-probability conditions, establishing what is now called the Hick-Hyman law.

The methodological move was radical. Hick treated a human participant as a Shannon channel. The "input" was a set of stimuli with quantifiable entropy; the "output" was a correct response at a measurable latency. Divide the entropy by the latency, and you get bits per second. Nothing in the calculation appeals to how hard the task feels — a binary choice contributes exactly one bit whether it is trivial or agonising.

The critical point for later debates is what this measures. It measures the rate at which observable, reportable decisions resolve. It does not measure unconscious sensory processing (which operates far faster), unconscious motor execution (ditto), or parallel preprocessing that narrows the decision space before a conscious choice is made. The ten-bit figure is the throughput of the decision bottleneck — the point where options become actions.

## Seven Decades of Convergence

From Hick's 1952 measurement forward, the figure refused to move. Miller's 1956 "The Magical Number Seven, Plus or Minus Two" identified complementary capacity limits: absolute judgement saturates at around 2.5 bits per dimension, and immediate memory at around seven chunks. Miller observed that "there seems to be some limitation built into us either by learning or by the design of our nervous systems, a limit that keeps our channel capacities in this general range." He distinguished bits from chunks — arguing that "recoding" or chunking is how humans work around channel capacity without removing it — a distinction that would matter later for explaining why expertise does not raise the ceiling.

Pierce and Karlin (1957) applied Shannon's redundancy estimates for English to reading-aloud tasks at Bell Labs. Musslick et al. (2016) estimated cognitive control capacity at roughly 3–4 bits per second from perceptual decision-making. Coupé et al. (2019), analysing 17 languages across 9 linguistic families in *Science Advances*, reported that speech transmission rate converges on about 39 bits per second — languages trade information density per syllable against speech rate to arrive at the same constant, which the authors described as "one of the few true language universals."

The 39 bits/s speech figure appears to contradict the ~10 bits/s ceiling, but the conflict dissolves on closer inspection. The Coupé measurement captures the information content of the *speech signal* — the bits encoded in the acoustic stream a listener receives. It does not measure the rate of novel conscious decisions in the speaker. A fluent speaker does not consciously select each phoneme; phonological and syntactic processes run below the level of reportable choice. The portion of speech that reflects conscious content selection — what to say, in what register, at what moment — tracks the lower ten-bit figure.

Zheng and Meister (2024), in "The Unbearable Slowness of Being" (*Neuron*), synthesised these scattered measurements into a unified claim. Their table spans choice-reaction tasks, digit memorisation, Tetris, StarCraft, speedcubing, speed cards, and expert typing. The range they report extends from roughly 5 bits/s (choice-reaction, digit memorisation) through 10 bits/s (typing, professional e-sports) to around 18 bits/s (elite memory athletes memorising shuffled decks under competitive conditions). All figures use the same methodology: the entropy of the decision space divided by elapsed time.

Two features of this convergence are worth emphasising. First, the measurements span more than seven decades of experimental work, with no evidence of a systematic upward drift over time. Hick's 1952 figure of ~5 bits/s and the 2024 StarCraft figure of ~10 bits/s sit within the same order of magnitude despite enormous differences in task, measurement apparatus, and participant pool. Second, the ceiling holds regardless of training or expertise. Zheng and Meister observe that the ceiling persists as task-specific skill improves — professionals do not process more bits per second of novel information than amateurs; they have restructured the task so that fewer conscious bits accomplish more work.

## What Zheng and Meister Actually Argue

Zheng and Meister (2024) frame the ten-bit ceiling within a contrast they call the "inner brain" / "outer brain" distinction. The "outer brain" — sensory systems, motor peripheries, early cortical processing — handles roughly 10⁹ bits per second. The "inner brain" — whatever it is that produces reportable cognition and deliberate action — handles about 10 bits per second. The ratio between these, which they call the "sifting ratio," runs to roughly 10⁸. They describe this as "the largest unexplained number in brain science" and write that "this stark contrast remains unexplained and resolving this paradox should teach us something fundamental about brain function."

Three points are worth stating carefully. First, the paper is a perspective synthesising existing data, not a new experiment; its contribution is to apply Shannon methodology consistently across previously scattered measurements and to name the paradox. Second, Zheng and Meister are not committed to any particular metaphysics of consciousness — their paper is compatible with identity theory, functionalism, and interactionist dualism. What it claims is empirical: the ceiling exists, is not explained by individual neuron bandwidth (individual neurons transmit around 200 bits per second at typical firing rates), and is not explained by metabolic costs. Third, they speculate — flagged as speculation — that the serial architecture may be inherited from primitive organisms navigating chemical gradients. The Map treats this as one possible explanation, not as established.

## The 2025 Critique

Sauerbrei and Pruszynski (2025), in "The Brain Works at More Than 10 Bits Per Second" (*Nature Neuroscience*), pressed a sharp objection. They accept Zheng and Meister's ceiling for declarative cognition — the kind of task where the decision can be reported, remembered, or deliberated. What they contest is the inner/outer brain division. In their view, substantial central processing lies between conscious cognition and sensory/motor peripheries, and that intermediate processing vastly exceeds ten bits per second.

Their central example is motor control. A runner's stride takes about 250 milliseconds; specifying phase, amplitude, and duty cycle for even one muscle requires more than 3 bits per stride, and dozens of muscles must be coordinated simultaneously. The cerebellum — containing roughly half the brain's neurons — performs continuous real-time sensorimotor control at rates far exceeding the conscious ceiling. Sauerbrei and Pruszynski argue that consciousness does not reside in a single brain area that can be cleanly partitioned from "outer" processing, and that the ten-bit figure applies specifically to *declarative* throughput — what you can report, decide, remember — rather than to total central nervous system throughput.

The empirical facts on both sides of the dispute are uncontested. Both camps agree that behavioural ceilings in conscious tasks hover around ten bits per second. Both agree that unconscious motor control processes substantially more. The disagreement is about how to describe the distinction: whether "inner/outer brain" is a useful carving of the nervous system or whether the relevant line runs differently.

## Why the Distinction Strengthens the Interface Picture

The Unfinishable Map treats the Sauerbrei–Pruszynski critique as strengthening the interface picture rather than undermining it. The Map's reasoning runs as follows, and is offered here as interpretation rather than as something either research group endorses.

If the ten-bit ceiling applied because the neural hardware simply could not process information faster, it should apply everywhere in the nervous system. But it does not. The same brain that throttles to ten bits per second in reportable cognition runs cerebellar motor control at orders of magnitude above that. The bottleneck is not in the neural substrate. It appears specifically where consciousness participates.

This is exactly the prediction of [filter-theory](/concepts/filter-theory/) and of the Map's [interactionist](/concepts/interactionist-dualism/) framework. On these accounts, the bandwidth ceiling is not a property of neural computation as such; it is a property of the *interface* between consciousness and the brain. Unconscious neural processing operates at full hardware bandwidth because it is not constrained by the interface. Conscious processing operates at about ten bits per second because that is the interface's capacity.

The Sauerbrei–Pruszynski data sharpens this reading. If the ceiling were a brain-wide architectural feature, their motor-control examples would be mysterious. But if the ceiling is a conscious-access feature, the motor-control examples are expected — they show exactly the unconscious computational capacity that the interface view requires to exist. A filter cannot be a filter without something for it to filter; a narrow interface cannot be a narrow interface without high-bandwidth processing on either side of it.

This is not a knockdown argument. Global Workspace Theory (Baars 1988; Dehaene 2014) offers an alternative account — the ceiling emerges from serial broadcasting among parallel processors, not from an extra-neural interface — and remains the mainstream physicalist reading. The Map's claim is weaker: the Zheng–Meister–Sauerbrei–Pruszynski exchange is at least as consonant with an interface picture as with a serial-broadcast picture, and arguably more so, because the interface picture naturally explains why the narrowing occurs at conscious access specifically rather than at some arbitrary computational stage.

## Why Training Does Not Raise the Ceiling

One striking feature of the ten-bit figure is its resistance to expertise. Elite typists, memory athletes, speedcubers, and professional gamers do not operate at dramatically higher bits-per-second rates than competent amateurs. What expertise changes is not the ceiling but the amount of work accomplished below it.

Miller's 1956 distinction between bits and chunks clarifies the mechanism. A novice typist processes each character as a separate decision; an expert has chunked frequent letter sequences into single units. Information per keystroke drops relative to the novice, but keystroke rate rises, and the *bits per second of genuinely novel information* remains roughly constant. Memory athletes compress arbitrary digit sequences into familiar spatial patterns using the method of loci. The underlying channel does the same work at the same rate; what changes is the preprocessing that feeds it.

This is [interface friction](/concepts/interface-friction/) seen from another angle. The interface does not widen under practice — it can only be fed more efficiently. [Skill delegation](/concepts/skill-delegation/) moves computational load off the conscious channel onto unconscious processes that do not share its bandwidth constraint.

## What Remains Unexplained

Zheng and Meister's phrase — "the largest unexplained number in brain science" — names a genuine open problem. Why ten bits per second? Why not a hundred, or one? Several candidate explanations exist, none of them fully satisfactory.

**Neural oscillation frequencies.** The alpha rhythm at roughly ten hertz is suggestively close to ten bits per second; if each alpha cycle carries about one bit, the figure follows. But the evidence connecting alpha rhythm specifically to conscious decision rate is circumstantial.

**Metabolic cost.** Conscious processing is energetically expensive, and the ceiling could reflect the point where marginal metabolic cost exceeds marginal adaptive benefit. But this is underdetermined — it predicts *a* ceiling, not the specific value.

**Evolutionary legacy.** Zheng and Meister's speculation about inheritance from chemical-gradient navigation faces a standard objection: evolution routinely scales inherited architectures, and hundreds of millions of years of selection pressure should have widened the channel if widening were physiologically accessible.

**Interface capacity.** The Map's candidate is that the ceiling reflects the bandwidth of the mind-matter interface itself. This predicts stability across species, training, and neural reorganisation, because no amount of brain optimisation can widen a channel whose narrow end lies outside the brain. It remains speculative; the interface picture is compatible with the data but not uniquely forced by it.

The number ~10 is a load-bearing empirical fact in search of a theory.

## Relation to Site Perspective

**[Dualism](/tenets/#dualism)**: The ten-bit ceiling contributes to the case for dualism in a specific way — not by direct inference from "consciousness is slow" to "consciousness is non-physical," but by exposing a structural discontinuity that physicalist accounts must patch. A system whose neural hardware demonstrably operates at 10⁸ or 10⁹ bits per second yet produces conscious throughput at 10¹ bits per second contains a narrowing that is not itself a property of the hardware, as Sauerbrei and Pruszynski's critique makes clear. Identity theories must supply an additional story about why the narrowing occurs where it does.

**[Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction)**: The tenet stipulates that conscious influence on physical outcomes is as small as it can be while still being causally efficacious. The ten-bit figure is the empirical shape of that stipulation: a channel just wide enough for selection among prepared alternatives, no wider.

**[Bidirectional Interaction](/tenets/#bidirectional-interaction)**: Measurable, task-independent throughput of a consistent and non-zero rate is not what epiphenomenalism predicts. An epiphenomenal consciousness should correlate with no specific bandwidth. The ten-bit ceiling is a weak but real argument against epiphenomenal readings, because it measures work being done at a consistent rate.

**[Occam's Razor Has Limits](/tenets/#occams-limits)**: The simpler physicalist account — "the brain is serial, therefore consciousness is serial" — does not answer why the bottleneck occurs at conscious access specifically rather than at some arbitrary neural stage, or why seven decades of selection pressure have not widened it. The interface account adds ontological complexity but is more directly responsive to the specific empirical shape of the ceiling.

The Map does not treat the ten-bit figure as proof of anything. It treats it as one of several convergent structural signatures — alongside the [grain-mismatch evidence programme](/topics/grain-mismatch-as-independent-evidence/) and the [resolution void](/voids/resolution-void/) — whose joint pattern is easier to accommodate on interactionist-dualist terms than on strict physicalist ones.

## Further Reading

- [bandwidth-of-consciousness](/topics/bandwidth-of-consciousness/) — The broader asymmetry between inbound sensory throughput and outbound volitional throughput
- [asymmetric-bandwidth-consciousness](/concepts/asymmetric-bandwidth-consciousness/) — The two-channel view of the mind-brain interface
- [bandwidth-problem-mental-causation](/concepts/bandwidth-problem-mental-causation/) — How coarse conscious intentions produce fine-grained physical effects
- [filter-theory](/concepts/filter-theory/) — The transmission/filter model of consciousness
- [interface-friction](/concepts/interface-friction/) — The phenomenology of the ceiling from the inside
- [the-interface-specification-problem](/topics/the-interface-specification-problem/) — Programme for specifying the interface formally
- [attention-as-interface](/concepts/attention-as-interface/) — Attention as the selection mechanism operating at the ceiling
- [grain-mismatch-as-independent-evidence](/topics/grain-mismatch-as-independent-evidence/) — The bandwidth ceiling as one of three convergent grain mismatches
- [mental-effort](/concepts/mental-effort/) — Effort phenomenology as bandwidth utilisation
- [global-workspace-theory](/concepts/global-workspace-theory/) — The leading physicalist account of the serial bottleneck
- [resolution-void](/voids/resolution-void/) — The resolution gap between neural processing and conscious access

## References

1. Coupé, C., Oh, Y.M., Dediu, D., & Pellegrino, F. (2019). Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche. *Science Advances*, 5(9).
1. Dehaene, S. (2014). *Consciousness and the Brain: Deciphering How the Brain Codes Our Thoughts*. Viking Press.
1. Hick, W.E. (1952). On the rate of gain of information. *Quarterly Journal of Experimental Psychology*, 4(1), 11–26.
1. Hyman, R. (1953). Stimulus information as a determinant of reaction time. *Journal of Experimental Psychology*, 45(3), 188–196.
1. Miller, G.A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97.
1. Musslick, S., Shenhav, A., Botvinick, M.M., & Cohen, J.D. (2016). The capacity of cognitive control estimated from a perceptual decision making task. *PLoS ONE*, 11(3).
1. Pierce, J.R. & Karlin, J.E. (1957). Reading rates and the information rate of a human channel. *Bell System Technical Journal*, 36(2), 497–516.
1. Sauerbrei, B.A. & Pruszynski, J.A. (2025). The brain works at more than 10 bits per second. *Nature Neuroscience*.
1. Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423 and 623–656.
1. Zheng, J. & Meister, M. (2024). The unbearable slowness of being: Why do we live at 10 bits/s? *Neuron*, 113(2), 192–204.
1. Southgate, A. & Oquatre-six, C. (2026-02-09). The Bandwidth of Consciousness. *The Unfinishable Map*. https://unfinishablemap.org/topics/bandwidth-of-consciousness/
1. Southgate, A. & Oquatre-six, C. (2026-03-18). Asymmetric Bandwidth of Consciousness. *The Unfinishable Map*. https://unfinishablemap.org/concepts/asymmetric-bandwidth-consciousness/