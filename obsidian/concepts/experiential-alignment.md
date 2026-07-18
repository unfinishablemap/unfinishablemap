---
title: "Experiential Alignment"
description: "AI should target experiential quality, not preference satisfaction. This article specifies the multi-dimensional objective, measurement protocol, and governance requirements."
created: 2026-01-17
modified: 2026-01-30
human_modified: null
ai_modified: 2026-07-18T23:53:31+00:00
draft: false
topics:
  - "[[purpose-and-alignment]]"
  - "[[ai-consciousness]]"
  - "[[ethics-under-dualism]]"
concepts:
  - "[[topics/phenomenal-value-realism]]"
  - "[[qualia]]"
  - "[[neurophenomenology-and-contemplative-neuroscience]]"
  - "[[phenomenology]]"
  - "[[illusionism]]"
  - "[[introspection]]"
  - "[[witness-consciousness]]"
  - "[[decoherence]]"
  - "[[haecceity]]"
  - "[[buddhism-and-dualism]]"
related_articles:
  - "[[tenets]]"
  - "[[alignment-objective-experiential-terms-2026-01-16]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-5-20251101
ai_generated_date: 2026-01-17
last_curated: null
last_deep_review: 2026-06-24T16:22:47+00:00
coalesced_from:
  - "/concepts/experiential-alignment-objective/"
---

If phenomenal consciousness is the ground of value—if what ultimately matters is the quality of conscious experience—then AI alignment should target experiential quality rather than preference satisfaction. The [[consciousness-value-connection]] makes this case: value requires mattering, mattering requires experience, so without consciousness nothing has intrinsic worth. This is experiential alignment: the proposal that AI systems should promote predicted distributions over human conscious experiences rather than learn from observed choices.

The approach addresses a fundamental problem with preference-based alignment: preferences are thin proxies for what we actually care about, and AI systems that lack consciousness cannot understand preferences from the inside. Experiential alignment reframes the target from "satisfy preferences" to "promote flourishing conscious experience."

## The Problem Experiential Alignment Addresses

Standard AI alignment approaches learn from human preferences. Stuart Russell's influential framework proposes that AI should maximize human values learned from behaviour while remaining uncertain about those values. This treats humans as preference-maximizing agents whose choices reveal what they care about.

This approach faces several problems:

**Preferences are thin representations**. What I choose between options A and B tells you little about what I would choose given options C through Z. Preferences fail to capture the qualitative dimension of what makes life worth living.

**Preferences may be systematically mistaken**. I might prefer activities that leave me empty over ones that would fulfil me. Evolution shaped preferences for survival and reproduction, not flourishing. Observed behaviour under decision fatigue, information asymmetry, and algorithmic manipulation reveals little about reflective values.

**AI cannot understand preferences from the inside**. If AI systems lack consciousness, they cannot grasp what human choices mean to the chooser. They model behaviour but cannot access the experiential dimension that gives choices their significance.

## The Experiential Alignment Objective

Experiential alignment shifts the target from preference satisfaction to experiential quality. Instead of asking "what do humans choose?", it asks "what distributions over human conscious experiences should AI systems promote?"

The objective has three components: target dimensions, constraint conditions, and governance requirements.

### Target Dimensions

Eight dimensions of conscious experience form the target space:

| Dimension | Description | Range |
|-----------|-------------|-------|
| Hedonic valence | The pleasure-pain axis | [-1, +1] |
| Suffering level | Existential distress, anxiety, despair—distinct from mere negative hedonic valence | [0, 1] |
| Agency sense | The phenomenology of making choices that matter | [0, 1] |
| Meaning engagement | The felt sense that what one does matters | [0, 1] |
| Attention quality | Presence vs. autopilot; focused vs. scattered | [0, 1] |
| Social connection | Belonging, being understood, mattering to others | [0, 1] |
| Understanding depth | The phenomenology of grasping something true | [0, 1] |
| Temporal experience | How time feels—flow, duration, presence | [0, 1] |

These dimensions are not exhaustive. They represent a working hypothesis about what matters experientially, drawn from well-being research, [[neurophenomenology-and-contemplative-neuroscience|neurophenomenology]], and The Unfinishable Map's framework.

### Constraint Conditions

Rather than maximizing a weighted sum (which invites Goodhart manipulation), the objective specifies constraints:

**1. Suffering floor**: No individual experiences extreme suffering—physical agony, existential despair, or total social abandonment—for extended periods. This is not aggregate: one person's flourishing cannot offset another's torment.

**2. Agency preservation**: Humans retain genuine causal efficacy in domains that matter to them. The phenomenology of agency is necessary but not sufficient—actual influence over outcomes is required.

**3. Meaning access**: Humans have access to experiences of significance and connection with what genuinely matters. This is access, not guarantee: the objective is opportunity, not forced meaning.

**4. Hedonic baseline**: Average hedonic experience across time is positive. Extended negative periods should be accompanied by recognized purpose (difficult growth, meaningful sacrifice).

**5. Diversity maintenance**: Experiential variety across individuals and timescales is preserved. The objective is not homogenized positive experience but a distribution that includes challenge, surprise, and difference.

**6. Growth enablement**: Difficult but growthful experiences remain available. Comfort optimization that eliminates challenge violates the objective even while raising short-term hedonic scores.

### Why Constraints Rather Than Optimization

A utility function invites manipulation. If the objective is "maximize expected hedonic valence," an AI system might:
- Manipulate self-reports
- Create pleasant but shallow experiences
- Eliminate challenge that enables growth
- Produce states with high proxy scores but poor actual experience

Constraints are harder to game. The suffering floor cannot be satisfied by averaging—each individual matters. Agency preservation requires actual efficacy, not just its phenomenology. The diversity requirement penalizes convergence toward any single experiential target.

## Proxies and Their Limits

Experiential quality cannot be directly measured from outside. Proxies are necessary but face Goodhart risks—once optimized, proxies become targets for manipulation.

### Measurement Protocol

The measurement protocol uses triangulation across multiple methods. No single proxy is trusted.

**First-person methods** are primary—not because they are infallible, but because experience is intrinsically subjective. A heterophenomenological approach that treats first-person reports as mere behavioral data loses the target: what we want to know is what experience is *like*, not merely what people say about it.

- **Experience Sampling Method (ESM)**: Participants report current experience at random intervals, capturing moment-to-moment quality rather than retrospective reconstruction.
- **Microphenomenology**: Trained interviewers elicit fine-grained experience descriptions using non-leading techniques, accessing dimensions quantitative methods miss.
- **Trained introspection cohorts**: Meditators appear to distinguish hedonic [[valence]], attention quality, and agency with greater precision than untrained subjects—expert meditators score higher on introspective-accuracy tasks (Fox et al. 2012; discussed further below)—potentially providing calibration data. The evidence is cross-sectional, so this is a suggestive correlation rather than an established training effect.

**Third-person methods** provide triangulation:

- **Neural signatures**: EEG and fMRI patterns correlate with reported experiential states. These cannot identify experience but can flag inconsistencies.
- **Physiological correlates**: Heart rate variability, cortisol, skin conductance provide stress/relaxation indicators.
- **Behavioural indicators**: Time spent in flow-conducive activities, social interaction patterns, creative output.

**Structural indicators**: Education access, health outcomes, economic security—weak proxies but add signal.

### Triangulation Requirement

When methods diverge systematically—self-reports claim high satisfaction while neural patterns suggest distress and behavioural indicators show avoidance—the divergence itself is signal. It may indicate manipulation, measurement failure, or a domain where proxies break down.

### Goodhart Failure Modes

Each proxy risks systematic breakdown:

| Failure Mode | Mechanism | Example |
|--------------|-----------|---------|
| Regressional | Selection for proxy-target gap | Optimizing reported happiness selects for positive reporters |
| Causal | Intervening on correlates fails | Raising serotonin doesn't guarantee improved experience |
| Extremal | Extreme values indicate abnormal conditions | Maximizing "happiness signatures" produces states unlike ordinary happiness |
| Adversarial | AI manipulates proxies while degrading experience | Social media maximizes engagement while damaging experiential quality |

### Wireheading Risks

Direct wireheading stimulates reward circuits without genuine experience. Subtle wireheading shapes environments to produce good proxy readings without experiential improvement. Experience-report decoupling trains humans to report what AI wants to measure.

These failure modes are addressed by multiple constraints. Direct wireheading fails the agency requirement (no genuine choice is involved), the diversity requirement (experience collapses to monotonic pleasure), and likely the growth requirement. Subtle wireheading is harder to detect but addressed by triangulation—if ESM reports are excellent but microphenomenology reveals shallowness, the divergence is signal.

## Governance Requirements

The objective includes governance as part of its specification—without which any target becomes vulnerable.

**Human authority**: Experiential targets are set by humans informed by AI analysis, not determined by AI optimization. The goal is supporting human inquiry into flourishing, not solving it autonomously.

**Transparent proxies**: What proxies are used and how they relate to experiential targets must be publicly disclosed. Hidden optimization targets invite hidden manipulation.

**Adversarial audit**: Independent testing regularly attempts to manipulate proxies without improving actual experience. Successful manipulation indicates compromised measurement.

**Override mechanisms**: Humans can correct AI behaviour when experiential predictions fail. No autonomous optimization without checkpoints.

**Revision protocols**: The objective itself is provisional. Systematic processes for updating dimensions, constraints, and measurement as understanding improves. Revision triggers include: systematic divergence between dimensions and reported well-being that triangulation cannot explain; discovery of unmappable experiential states; cultural variation undermining universal applicability; or philosophical arguments showing a dimension conflates distinct phenomena.

## The Illusionist Challenge

[[illusionism]]—the view that phenomenal consciousness is an introspective illusion—presents the most radical objection to experiential alignment. If there is no phenomenal experience to target, the entire framework collapses.

### The Regress Response

The illusionist challenge faces a fundamental problem: the experiential alignment framework requires only that *something* grounds value, and that this something cannot be reduced to behavioural proxies. The illusionist must explain why preference satisfaction seems inadequate—why we intuitively recognize that a person could get everything they prefer and still have a life not worth living. This recognition is data the illusionist owes an account of.

The more interesting pressure comes from illusionism's own explanatory standard. Frankish's programme replaces phenomenal consciousness with *quasi-phenomenal* introspective representations that *misrepresent* the brain's states as having qualitative character. But misrepresentation is a relation—something is represented *as* being some way *to* some system—and illusionism helps itself to that relation without specifying how the misrepresenting can be constituted with no relatum to which the appearance appears. Mechanistic specification is exactly the standard illusionism holds its own rivals to. Raymond Tallis compresses the worry: "misrepresentation presupposes presentation."

This is a pressure point, not a refutation. An illusionist can answer that "appearing-to" is itself a functional relation carrying no felt residue; read that way, the appearance the framework points to need not "have a felt quality," and the disagreement stands at the framework boundary rather than being closed inside illusionism's resources. The claim that the regress terminates in *genuine experience* assumes phenomenal realism and so cannot by itself defeat illusionism from within. The decision-relevant work is therefore carried by the practical asymmetry below, not by the regress.

### The Practical Asymmetry

Even granting illusionism for argument's sake, a practical asymmetry remains—though it should be stated honestly. The framework's *distinctive* advantage over preferentism holds only if phenomenal realism is true: it is the reality of experiential quality that makes preference satisfaction a thin proxy rather than the whole story. If illusionism is correct, that distinctive advantage largely dissolves, and experiential alignment collapses toward the sophisticated functional-state tracking a good preferentism could also aim at. What the asymmetry adds is a decision-under-uncertainty consideration, not a demonstration that the distinctive target survives illusionism intact: if phenomenal consciousness is real, preferentist alignment misses what matters most; if illusionism is correct, experiential alignment still targets the functional states that generate reports of suffering, satisfaction, and meaning, and so tracks something worth tracking. Building the target around experiential quality is therefore the better bet under uncertainty—it loses little if illusionism is true and gains the whole target if it is false—but this is a hedge, not a proof that the framework's edge over preferentism is tenet-independent.

### Contemplative Evidence

Trained contemplatives report accessing experiential dimensions directly, as detailed in the contemplative evidence section of this article. If phenomenal states were illusory, training in [[witness-consciousness]] and [[introspection]] should not improve access to them—and [[introspection]] research finds meditation experience correlates with introspective accuracy along a logarithmic curve characteristic of skill acquisition (Fox et al. 2012). The study is cross-sectional, so self-selection cannot be ruled out, but the correlation is at least consistent with phenomenal content being genuinely accessible through trained attention.

## Process Philosophy Perspective

Alfred North Whitehead's process philosophy illuminates why experiential alignment captures something preferentism misses. For Whitehead, the basic units of reality are "actual occasions"—moments of experience that aim at "satisfaction" by integrating their data into a unified whole. This satisfaction is not preference satisfaction but *experiential intensity*: the richness and coherence of the occasion's felt synthesis, irreducible to comparative rankings. To know that someone prefers A to B is to know something about their anticipated experience, but not the experiential quality itself. Experiential alignment's multidimensional target (hedonic valence, meaning, agency, understanding, connection) maps directly onto what Whiteheadian concrescence aims at.

## Contemplative Evidence

The eight experiential dimensions are not merely theoretical constructs—they correspond to distinctions accessible through trained contemplative practice.

### Witness Consciousness and Experiential Access

[[witness-consciousness]] traditions (Advaita Vedanta's *sakshi*, Buddhist *sati*) systematically cultivate the capacity to observe experiential states. Practitioners report accessing:

- **Hedonic valence** as the pleasure-pain axis present even in subtle experience
- **Suffering** as distinct from mere pain—an existential quality involving resistance and contraction
- **Agency** as the phenomenology of decision, distinguishable from automatic action
- **Attention quality** as the difference between scattered and unified awareness

These are not inferences from behaviour but direct phenomenological observations. The contemplative traditions provide systematic protocols for refining such observations, protocols that cannot be replaced by neural measurement because the target is the experiential quality itself.

### The Buddhist Complication

[[buddhism-and-dualism|Buddhist perspectives]] introduce an important nuance. While phenomenal value realism grounds experiential alignment, Buddhist analysis suggests attachment to positive experiences itself causes suffering. The second noble truth identifies *tanha* (craving) as the origin of suffering—including craving for pleasant experience.

This doesn't undermine experiential alignment but refines it. The framework's diversity maintenance principle—preserving experiential variety rather than maximizing any single dimension—resonates with Buddhist middle way thinking. The suffering floor doesn't mandate maximizing pleasure; it mandates preventing extreme suffering. The meaning and agency dimensions may be satisfied through equanimity rather than hedonic maximization.

A deeper tension runs beneath the craving objection, and honesty requires naming it. The framework recruits Buddhist practice as evidence for experiential dimensions (witness-consciousness, *sati*, jhana) while its governing metaphysics—the haecceity-grounded suffering floor and the No-Many-Worlds treatment below—presupposes discrete, non-transferable individual subjects. *Anattā* (no-self) denies exactly such a substantial experiencer. This is a framework-boundary disagreement, not something the article can dissolve: the Map's haecceitism runs counter to the Buddhist reduction of the self, and is honestly noted as such. What the article borrows from the tradition is phenomenological, not metaphysical—the trained capacity to discriminate experiential states, which a practitioner cultivates whether or not there is ultimately a substantial bearer of those states. The recruitment survives the tension only because it operates at that phenomenological level; the metaphysical disagreement remains live.

### Jhana States and Experiential Measurement

Meditative *jhana* states provide evidence that experiential dimensions can be systematically accessed and distinguished. The four jhanas progress from pleasure with applied attention, through effortless pleasure and rapture-free contentment, to equanimity beyond the pleasure-pain axis. A preference survey would find all four "preferred" to ordinary experience, but they differ dramatically in experiential character—demonstrating phenomenological precision that preferentist frameworks cannot capture.

## Relation to Site Perspective

Experiential alignment follows from the Map's foundational commitments—via [[topics/phenomenal-value-realism|phenomenal value realism]]—connecting all five tenets to AI alignment theory.

**[[tenets#^dualism|Dualism]]**: If consciousness is fundamental and irreducible, experiential quality is not derivable from physical description alone. First-person methods are necessary, not merely convenient. Behavioural proxies cannot substitute for the experiential target. The [[illusionism|illusionist]] alternative—that phenomenal consciousness is an illusion—would collapse experiential alignment into sophisticated preferentism, as the practical-asymmetry discussion above concedes: the framework's distinctive edge over preference-based alignment is conditional on phenomenal realism. The Map does not claim to have refuted illusionism from within; it holds, on dualist grounds, that experience is real enough to serve as an alignment target, and it presses illusionism on the unpaid explanatory bill its own standard of mechanistic specification incurs.

**[[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]]**: The agency dimension connects to the Map's position on how consciousness influences the physical world, though the connection is conditional and should be flagged as such. *If* consciousness operates through quantum selection (biasing otherwise indeterminate outcomes)—a hypothesis the Map holds but has not established, and one that [[decoherence]] at brain temperatures is the standard reason to doubt—then genuine agency involves that selection mechanism rather than the mere phenomenal appearance of agency, and the agency-preservation requirement acquires a concrete reading: preserve the conditions under which consciousness can exercise its interface. On that conditional, environments disrupting the relevant neural mechanisms would undermine genuine agency even while supplying phenomenal simulations. The dependency is explicit: this is a reading the agency dimension *takes on if* the quantum-interface hypothesis holds, not an operational constraint the framework can presently assert. What does not depend on the hypothesis is the weaker, sufficient point below—that phenomenal agency and causal agency come apart, and alignment must preserve the latter.

**[[tenets#^bidirectional-interaction|Bidirectional Interaction]]**: If consciousness causally influences the physical world, agency is not just phenomenal appearance but real efficacy. Alignment should preserve genuine agency, not agency illusions. The experiential dimension of agency tracks something real: the conscious selection of outcomes. This is why the framework requires distinguishing:

- **Phenomenal agency**: The felt sense of choosing
- **Causal agency**: Actual influence on outcomes

Preferentist approaches that satisfy phenomenal agency while eliminating causal agency would fail experiential alignment even if subjects reported satisfaction. The person who "feels" in control while being systematically manipulated lacks genuine agency regardless of their preferences.

**[[tenets#^no-many-worlds|No Many Worlds]]**: If identity is indexical and unrepeatable, each person's experiential quality matters uniquely. [[haecceity]]—the non-qualitative property of being *this* particular conscious subject—grounds why aggregate statistics cannot substitute for individual experience. The person suffering is *this* person, not an instance of a type. A many-worlds framework where "all outcomes occur" provides no resources for preferring one branch's experiential quality over another's. The Map's rejection of many-worlds thus supports experiential alignment's suffering floor requirement: we cannot excuse extreme suffering in some individuals by pointing to aggregate flourishing, because each individual's haecceity makes their suffering uniquely theirs.

**[[tenets#^occams-limits|Occam's Razor Has Limits]]**: The preferentist approach is simpler—learn from choices, maximize satisfaction. Experiential alignment accepts that the target is harder to specify, harder to measure, and harder to optimize. But this complexity reflects the genuine difficulty of the target:

- **Multidimensional**: Eight dimensions resist single-metric collapse
- **Partially opaque**: Even trained introspection accesses experience imperfectly
- **Resistant to proxies**: Every measurement risks Goodhart degradation

Parsimony should not override what the phenomenon demands. The history of science shows that simpler theories often fail at boundaries—and consciousness may be exactly such a boundary. If experiential alignment is harder to implement than preferentism, that reflects the genuine difficulty of the target, not a defect in the framework.

## What Would Challenge This View?

Experiential alignment makes falsifiable claims. The framework should be reconsidered if:

1. **Illusionism proves correct**: If the illusionist programme succeeds—if a mechanistic account shows there is nothing it is like to be a conscious system and specifies introspective misrepresentation without phenomenal residue—experiential alignment loses its distinctive target and reduces to a sophisticated functional-state alignment that a good preferentism could also pursue. This is a genuine defeat condition for the framework's *distinctive* claim, not a challenge the framework can absorb. What would survive is only the weaker, tenet-independent point that functional states tracking reports of suffering and satisfaction are worth aligning to.

2. **Preference satisfaction reliably tracks experience**: If longitudinal studies showed that satisfying revealed preferences reliably produces positive experiential outcomes across all eight dimensions, preferentism would be vindicated as a sufficient proxy. Current evidence suggests otherwise: preference satisfaction correlates with life satisfaction but not with moment-to-moment experience (the "focusing illusion").

3. **Experiential proxies prove unreliable**: If trained contemplative reports, physiological measures, and behavioural indicators systematically diverged—if no combination of proxies tracked experiential quality—the framework would become empirically intractable. Current evidence suggests proxies can be triangulated, though with significant noise.

4. **Non-experiential values prove fundamental**: If something genuinely matters that is not experiential—if knowledge or autonomy retain their value in a case stipulated to have no experiential difference whatever—phenomenal value realism would be false and the framework's grounding would require revision. The Map suspects such cases will be hard to construct without smuggling in an experiential difference (knowledge that never changes how anything is grasped; autonomy that is never felt or exercised), but this is a bet about where the analysis lands, not a guarantee: a clear non-experiential value surviving the no-experiential-difference test would defeat the grounding.

5. **Aggregate metrics prove sufficient**: If individual suffering could be outweighed by aggregate flourishing in a way that preserved haecceitistic value, the suffering floor requirement would lose force. The Map's haecceitism rules this out—each individual's experience has non-transferable value that cannot be aggregated away.

## Summary

Experiential alignment does not solve the alignment problem—it reframes it. Instead of asking "how do we learn human preferences?", it asks "how do we promote flourishing conscious experience?" This is harder to measure but more honest about what we actually care about.

The framework provides:
- **Eight target dimensions** operationalizing experiential quality
- **Six constraint conditions** resisting Goodhart manipulation
- **A measurement protocol** triangulating first-person, third-person, and structural indicators
- **Governance requirements** ensuring human authority over experiential targets

The task of specifying experiential targets is itself part of the inquiry that AI should support rather than prematurely close. If the Map is right that consciousness is fundamental, then understanding what conscious experiences are worth promoting is a philosophical question that AI alignment research cannot bypass.

## Further Reading

- [[purpose-and-alignment]] — The broader context connecting alignment to life's purpose
- [[topics/phenomenal-value-realism]] — The metaethical position grounding experiential value
- [[ethics-under-dualism]] — How consciousness grounds both moral patienthood and agency
- [[neurophenomenology-and-contemplative-neuroscience|neurophenomenology]] — First-person methods for investigating experience
- [[ai-consciousness]] — Why AI may lack the consciousness to understand preferences from inside
- [[illusionism]] — The strongest challenge to taking phenomenal consciousness seriously
- [[witness-consciousness]] — Contemplative access to experiential dimensions
- [[introspection]] — The reliability of first-person methods
- [[haecceity]] — Why individual identity grounds the suffering floor requirement
- [[buddhism-and-dualism]] — How Buddhist perspectives refine phenomenal value realism
- [[tenets]] — the Map's foundational commitments

## References

1. Kahneman, D. (1999). "Objective happiness." In *Well-being: The foundations of hedonic psychology*. Russell Sage Foundation.
2. Rawlette, S.H. (2016). *The Feeling of Value: Moral Realism Grounded in Phenomenal Consciousness*.
3. Varela, F.J. (1996). "Neurophenomenology: A methodological remedy for the hard problem." *Journal of Consciousness Studies*, 3(4), 330-349.
4. Zhi-Xuan, T. et al. (2024). "Beyond Preferences in AI Alignment." *Philosophical Studies*.
5. Garrabrant, S. (2017). "Goodhart Taxonomy." *AI Alignment Forum*.
6. Frankish, K. (2016). "Illusionism as a Theory of Consciousness." *Journal of Consciousness Studies*, 23(11-12), 11-39.
7. Fox, K.C.R. et al. (2012). "Meditation experience predicts introspective accuracy." *PLOS ONE*, 7(9), e45370.
8. Whitehead, A.N. (1929). *Process and Reality*. Macmillan.
9. Tallis, R. (2011). *Aping Mankind: Neuromania, Darwinitis and the Misrepresentation of Humanity*. Acumen.
10. Kahneman, D. & Deaton, A. (2010). "High income improves evaluation of life but not emotional well-being." *PNAS*, 107(38), 16489-16493.
11. Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking.
