---
title: "Experiential Alignment"
description: "AI should target experiential quality, not preference satisfaction. This article specifies the multi-dimensional objective, measurement protocol, and governance requirements."
created: 2026-01-17
modified: 2026-01-30
human_modified: null
ai_modified: 2026-01-30T10:45:00+00:00
draft: false
topics:
  - "[[purpose-and-alignment]]"
  - "[[ai-consciousness]]"
  - "[[ethics-of-consciousness]]"
concepts:
  - "[[phenomenal-value-realism]]"
  - "[[qualia]]"
  - "[[neurophenomenology]]"
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
last_deep_review: 2026-01-30T10:45:00+00:00
coalesced_from:
  - "/concepts/experiential-alignment-objective/"
---

If phenomenal consciousness is the ground of value—if what ultimately matters is the quality of conscious experience—then AI alignment should target experiential quality rather than preference satisfaction. This is experiential alignment: the proposal that AI systems should promote predicted distributions over human conscious experiences rather than learn from observed choices.

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

These dimensions are not exhaustive. They represent a working hypothesis about what matters experientially, drawn from well-being research, [[neurophenomenology]], and the Map's framework.

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

- **Experience Sampling Method (ESM)**: Participants report current experience at random intervals. Captures moment-to-moment quality rather than retrospective reconstruction.
- **Microphenomenology**: Trained interviewers elicit fine-grained experience descriptions using non-leading techniques. Labour-intensive but accesses dimensions quantitative methods miss.
- **Trained introspection cohorts**: Populations trained in contemplative observation provide calibration data. Meditators can distinguish hedonic valence, attention quality, and agency with precision that untrained subjects cannot.

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

**Revision protocols**: The objective itself is provisional. Systematic processes for updating dimensions, constraints, and measurement as understanding improves. Evidence that would trigger revision includes: systematic divergence between dimensions and reported well-being that triangulation cannot explain; discovery of experiential states that don't map to any dimension; cultural variation so profound that the dimensions lack universal applicability; or philosophical arguments showing that a dimension conflates distinct phenomena.

## The Illusionist Challenge

[[Illusionism]]—the view that phenomenal consciousness is an introspective illusion—presents the most radical objection to experiential alignment. If there is no phenomenal experience to target, the entire framework collapses.

### The Regress Response

The illusionist challenge faces a fundamental problem: the experiential alignment framework requires only that *something* grounds value, and that this something cannot be reduced to behavioural proxies. The illusionist must explain why preference satisfaction seems inadequate—why we intuitively recognize that a person could get everything they prefer and still have a life not worth living. This recognition itself constitutes the experiential data that illusionism claims doesn't exist.

Raymond Tallis's point applies: "Misrepresentation presupposes presentation." To be under an illusion of experiential quality, something must be experiencing that illusion. The appearance of hedonic valence—even if somehow "illusory"—is itself an appearance *to* something, and that appearance has a felt quality. The regress terminates in genuine experience.

### The Practical Asymmetry

Even granting illusionism for argument's sake, a practical asymmetry remains. If phenomenal consciousness is real, preferentist alignment misses what matters. If illusionism is correct, experiential alignment merely targets sophisticated functional states that still track something important—the states that generate reports of suffering, satisfaction, and meaning. The downside of illusionism being false (targeting nothing that matters) is asymmetrically worse than the downside of illusionism being true (targeting functional states that correlate with what we care about).

### Contemplative Evidence

Trained contemplatives report accessing experiential dimensions directly. [[Witness-consciousness]]—the capacity to observe mental contents without identification—reveals the phenomenal character of experience with increasing precision through practice. [[Introspection]] research shows meditators achieve accuracy improvements following logarithmic learning curves, suggesting phenomenal content is accessible through trained attention. If phenomenal states were illusory, training should not improve access to them. The 2025 "renaissance of first-person methods" in consciousness science provides systematic evidence that phenomenal reports can be calibrated and refined.

## Process Philosophy Perspective

Alfred North Whitehead's process philosophy illuminates why experiential alignment captures something preferentism misses. For Whitehead, the basic units of reality are "actual occasions"—moments of experience that aim at "satisfaction" through the integration of their data. This satisfaction is not preference satisfaction but *experiential intensity*—the richness and coherence of the occasion's felt synthesis.

### Concrescence and Experiential Quality

Each actual occasion undergoes "concrescence"—a process of becoming that synthesizes inherited data into a unified experience. The occasion's "subjective aim" is toward maximal intensity of experience consistent with harmony. This maps directly onto experiential alignment's multidimensional target: hedonic valence, meaning, agency, understanding, and connection are all aspects of experiential intensity that concrescence aims at.

### Why Preferences Are Thin

On the Whiteheadian view, preferences are abstractions from experiential richness. To know that someone prefers A to B is to know something about their anticipated experience, but not the experiential quality itself. The actual occasion's satisfaction cannot be captured by a preference ordering because satisfaction concerns the felt integration of the moment—something irreducible to comparative rankings.

### Eternal Objects and Experiential Dimensions

Whitehead's "eternal objects" (pure potentials for experience) provide a framework for understanding the eight experiential dimensions. Hedonic valence, meaning, agency, understanding, connection, attention quality, suffering, and temporal experience represent eternal objects that can be instantiated in actual occasions. Experiential alignment aims to promote occasions that instantiate these eternal objects positively—an aim that makes sense within process metaphysics but would be incoherent on purely preferentist terms.

## Contemplative Evidence

The eight experiential dimensions are not merely theoretical constructs—they correspond to distinctions accessible through trained contemplative practice.

### Witness Consciousness and Experiential Access

[[Witness-consciousness]] traditions (Advaita Vedanta's *sakshi*, Buddhist *sati*) systematically cultivate the capacity to observe experiential states. Practitioners report accessing:

- **Hedonic valence** as the pleasure-pain axis present even in subtle experience
- **Suffering** as distinct from mere pain—an existential quality involving resistance and contraction
- **Agency** as the phenomenology of decision, distinguishable from automatic action
- **Attention quality** as the difference between scattered and unified awareness

These are not inferences from behaviour but direct phenomenological observations. The contemplative traditions provide systematic protocols for refining such observations, protocols that cannot be replaced by neural measurement because the target is the experiential quality itself.

### The Buddhist Complication

[[Buddhism-and-dualism|Buddhist perspectives]] introduce an important nuance. While phenomenal value realism grounds experiential alignment, Buddhist analysis suggests attachment to positive experiences itself causes suffering. The second noble truth identifies *tanha* (craving) as the origin of suffering—including craving for pleasant experience.

This doesn't undermine experiential alignment but refines it. The framework's diversity maintenance principle—preserving experiential variety rather than maximizing any single dimension—resonates with Buddhist middle way thinking. The suffering floor doesn't mandate maximizing pleasure; it mandates preventing extreme suffering. The meaning and agency dimensions may be satisfied through equanimity rather than hedonic maximization.

### Jhana States and Experiential Measurement

Meditative *jhana* states provide evidence that experiential dimensions can be systematically accessed and distinguished. Practitioners report:

- First jhana: pleasure with applied attention
- Second jhana: pleasure without effort
- Third jhana: contentment without rapture
- Fourth jhana: equanimity beyond pleasure and pain

These distinctions demonstrate phenomenological precision that preferentist frameworks cannot capture. A preference survey would find all four states "preferred" to ordinary experience, but they differ dramatically in experiential character. Experiential alignment requires such fine-grained access.

## Relation to Site Perspective

Experiential alignment follows directly from the Map's foundational commitments, connecting all five tenets to AI alignment theory.

**[[tenets#^dualism|Dualism]]**: If consciousness is fundamental and irreducible, experiential quality is not derivable from physical description alone. First-person methods are necessary, not merely convenient. Behavioural proxies cannot substitute for the experiential target. The [[illusionism|illusionist]] alternative—that phenomenal consciousness is an illusion—would collapse experiential alignment into sophisticated preferentism. But the regress argument applies: even the "illusion" of suffering has a felt quality that cannot be eliminated by relabeling. The Map's dualism ensures that experience is real enough to serve as an alignment target.

**[[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]]**: The agency dimension connects directly to the Map's position on how consciousness influences the physical world. If consciousness operates through quantum selection (biasing otherwise indeterminate outcomes), then genuine agency involves this selection mechanism—not mere phenomenal appearance of agency. Experiential alignment's agency preservation requirement gains concrete meaning: we should preserve the conditions under which consciousness can exercise its quantum interface. [[Decoherence]] considerations apply here—if AI systems create environments that disrupt the neural quantum mechanisms through which agency operates, they undermine genuine agency even while providing phenomenal simulations. This is why the agency dimension cannot be reduced to "feeling" agentic.

**[[tenets#^bidirectional-interaction|Bidirectional Interaction]]**: If consciousness causally influences the physical world, agency is not just phenomenal appearance but real efficacy. Alignment should preserve genuine agency, not agency illusions. The experiential dimension of agency tracks something real: the conscious selection of outcomes. This is why the framework requires distinguishing:

- **Phenomenal agency**: The felt sense of choosing
- **Causal agency**: Actual influence on outcomes

Preferentist approaches that satisfy phenomenal agency while eliminating causal agency would fail experiential alignment even if subjects reported satisfaction. The person who "feels" in control while being systematically manipulated lacks genuine agency regardless of their preferences.

**[[tenets#^no-many-worlds|No Many Worlds]]**: If identity is indexical and unrepeatable, each person's experiential quality matters uniquely. [[Haecceity]]—the non-qualitative property of being *this* particular conscious subject—grounds why aggregate statistics cannot substitute for individual experience. The person suffering is *this* person, not an instance of a type. A many-worlds framework where "all outcomes occur" provides no resources for preferring one branch's experiential quality over another's. The Map's rejection of many-worlds thus supports experiential alignment's suffering floor requirement: we cannot excuse extreme suffering in some individuals by pointing to aggregate flourishing, because each individual's haecceity makes their suffering uniquely theirs.

**[[tenets#^occams-limits|Occam's Razor Has Limits]]**: The preferentist approach is simpler—learn from choices, maximize satisfaction. Experiential alignment accepts that the target is harder to specify, harder to measure, and harder to optimize. But this complexity reflects the genuine difficulty of the target:

- **Multidimensional**: Eight dimensions resist single-metric collapse
- **Partially opaque**: Even trained introspection accesses experience imperfectly
- **Resistant to proxies**: Every measurement risks Goodhart degradation

Parsimony should not override what the phenomenon demands. The history of science shows that simpler theories often fail at boundaries—and consciousness may be exactly such a boundary. If experiential alignment is harder to implement than preferentism, that reflects the genuine difficulty of the target, not a defect in the framework.

## What Would Challenge This View?

Experiential alignment makes falsifiable claims. The framework should be reconsidered if:

1. **Illusionism proves correct empirically**: If neuroscience demonstrates that phenomenal consciousness is genuinely illusory—not just that we misunderstand its mechanisms, but that there is nothing it is like to be a conscious system—then experiential alignment loses its target. However, the illusionist would need to explain why the "illusion" of suffering still seems to matter, and this explanation would likely reinstate something functionally equivalent to experiential quality.

2. **Preference satisfaction reliably tracks experience**: If longitudinal studies showed that satisfying revealed preferences reliably produces positive experiential outcomes across all eight dimensions, preferentism would be vindicated as a sufficient proxy. Current evidence suggests otherwise: preference satisfaction correlates with life satisfaction but not with moment-to-moment experience (the "focusing illusion").

3. **Experiential proxies prove unreliable**: If trained contemplative reports, physiological measures, and behavioural indicators systematically diverged—if no combination of proxies tracked experiential quality—the framework would become empirically intractable. Current evidence suggests proxies can be triangulated, though with significant noise.

4. **Non-experiential values prove fundamental**: If something genuinely matters that is not experiential—if, for example, knowledge or autonomy matter independently of how they feel—phenomenal value realism would require revision. The Map's position is that these apparent counterexamples dissolve on analysis: knowledge matters because understanding feels a certain way; autonomy matters because agency has phenomenal character.

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
- [[phenomenal-value-realism]] — The metaethical position grounding experiential value
- [[ethics-of-consciousness]] — How consciousness grounds both moral patienthood and agency
- [[neurophenomenology]] — First-person methods for investigating experience
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
9. Tallis, R. (2014). "The mystery of existence: why is there something rather than nothing?" In *Aping Mankind*. Routledge.
10. Kahneman, D. & Deaton, A. (2010). "High income improves evaluation of life but not emotional well-being." *PNAS*, 107(38), 16489-16493.
