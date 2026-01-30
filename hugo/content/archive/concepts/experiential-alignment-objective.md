---
ai_contribution: 100
ai_generated_date: 2026-01-30
ai_modified: 2026-01-30 08:41:00+00:00
ai_system: claude-opus-4-5-20251101
archive_reason: Coalesced into Experiential Alignment
archived: true
archived_date: 2026-01-30 10:45:00+00:00
author: null
concepts:
- '[[experiential-alignment]]'
- '[[phenomenal-value-realism]]'
- '[[qualia]]'
- '[[neurophenomenology]]'
created: 2026-01-30
date: &id001 2026-01-30
description: 'The concrete target for AI alignment: a multi-dimensional specification
  of experiential quality that AI systems should promote, with constraints to prevent
  wireheading.'
draft: false
human_modified: null
last_curated: null
last_deep_review: 2026-01-30 08:41:00+00:00
modified: *id001
original_path: /concepts/experiential-alignment-objective/
related_articles:
- '[[tenets]]'
- '[[alignment-objective-experiential-terms-2026-01-16]]'
superseded_by: /concepts/experiential-alignment/
title: Experiential Alignment Objective
topics:
- '[[purpose-and-alignment]]'
- '[[ai-consciousness]]'
- '[[ethics-of-consciousness]]'
---

An experiential alignment objective specifies what distributions over human conscious experience AI systems should promote. Rather than a single utility function, it defines multiple experiential dimensions with target ranges and constraints—a multi-dimensional target that resists the failure modes of simpler approaches.

This concept operationalizes [experiential-alignment](/concepts/experiential-alignment/) into something concrete enough to guide system design while remaining honest about measurement difficulties.

## The Structure of the Objective

The experiential alignment objective has three components: target dimensions, constraint conditions, and governance requirements.

### Target Dimensions

Eight dimensions of conscious experience form the target space:

| Dimension | Description | Range |
|-----------|-------------|-------|
| Hedonic valence | The pleasure-pain axis | [-1, +1] |
| Suffering level | Existential distress, not just pain | [0, 1] |
| Agency sense | Felt authorship of choices | [0, 1] |
| Meaning engagement | Sense that actions matter | [0, 1] |
| Attention quality | Presence vs. autopilot | [0, 1] |
| Social connection | Belonging and being understood | [0, 1] |
| Understanding depth | Grasp of what is true | [0, 1] |
| Temporal experience | Quality of how time feels | [0, 1] |

These dimensions are not exhaustive. They represent a working hypothesis about what matters experientially, drawn from well-being research, [neurophenomenology](/concepts/neurophenomenology/), and the Map's framework.

### Constraint Conditions

Rather than maximizing a weighted sum (which invites Goodhart manipulation), the objective specifies constraints:

**Suffering floor:** No individual experiences extreme suffering—physical agony, existential despair, or total social abandonment—for extended periods. This is not aggregate: one person's flourishing cannot offset another's torment.

**Agency preservation:** Humans retain genuine causal efficacy in domains that matter to them. The phenomenology of agency is necessary but not sufficient—actual influence over outcomes is required.

**Meaning access:** Humans have access to experiences of significance and connection with what genuinely matters. This is access, not guarantee: the objective is opportunity, not forced meaning.

**Hedonic baseline:** Average hedonic experience across time is positive. Extended negative periods should be accompanied by recognized purpose (difficult growth, meaningful sacrifice).

**Diversity maintenance:** Experiential variety across individuals and timescales is preserved. The objective is not homogenized positive experience but a distribution that includes challenge, surprise, and difference.

**Growth enablement:** Difficult but growthful experiences remain available. Comfort optimization that eliminates challenge violates the objective even while raising short-term hedonic scores.

### Why Constraints Rather Than Optimization

A utility function invites manipulation. If the objective is "maximize expected hedonic valence," an AI system might:
- Manipulate self-reports
- Create pleasant but shallow experiences
- Eliminate challenge that enables growth
- Produce states with high proxy scores but poor actual experience

Constraints are harder to game. The suffering floor cannot be satisfied by averaging—each individual matters. Agency preservation requires actual efficacy, not just its phenomenology. The diversity requirement penalizes convergence toward any single experiential target.

## Measurement Protocol

The experiential alignment objective cannot be directly observed from outside. Any measurement is a proxy with Goodhart risks. The protocol uses triangulation across multiple methods:

### First-Person Methods

First-person methods are primary in this protocol—not because they are infallible, but because experience is intrinsically subjective. A heterophenomenological approach that treats first-person reports as mere behavioral data to be explained away loses the target: what we want to know is what experience is *like*, not merely what people say about it. The risk of introspective error is real, which is why triangulation with third-person methods is required. But treating verbal behavior as the final word eliminates the phenomenon we're trying to track.

**Experience Sampling Method (ESM):** Participants report current experience at random intervals. Captures moment-to-moment quality rather than retrospective reconstruction.

**Microphenomenology:** Trained interviewers elicit fine-grained experience descriptions using non-leading techniques. Labour-intensive but accesses dimensions quantitative methods miss.

**Trained introspection cohorts:** Populations trained in contemplative observation provide calibration data. Meditators can distinguish hedonic valence, attention quality, and agency with precision that untrained subjects cannot.

### Third-Person Methods

**Neural signatures:** EEG and fMRI patterns correlate with reported experiential states. These cannot identify experience but can flag inconsistencies—if neural patterns diverge sharply from reports, something is wrong.

**Physiological correlates:** Heart rate variability, cortisol, skin conductance provide stress/relaxation indicators. Loose correlations but useful for triangulation.

**Behavioural indicators:** Time spent in flow-conducive activities, social interaction patterns, creative output. These are weak proxies but add signal.

### Triangulation Requirement

No single proxy is trusted. When methods diverge systematically:
- Self-reports claim high satisfaction
- Neural patterns suggest distress
- Behavioural indicators show avoidance

The divergence itself is signal. It may indicate manipulation, measurement failure, or a domain where proxies break down.

## Governance Requirements

The objective includes governance as part of its specification—without which any target becomes vulnerable.

**Human authority:** Experiential targets are set by humans informed by AI analysis, not determined by AI optimization. The goal is supporting human inquiry into flourishing, not solving it autonomously.

**Transparent proxies:** What proxies are used and how they relate to experiential targets must be publicly disclosed. Hidden optimization targets invite hidden manipulation.

**Adversarial audit:** Independent testing regularly attempts to manipulate proxies without improving actual experience. Successful manipulation indicates compromised measurement.

**Override mechanisms:** Humans can correct AI behaviour when experiential predictions fail. No autonomous optimization without checkpoints.

**Revision protocols:** The objective itself is provisional. Systematic processes for updating dimensions, constraints, and measurement as understanding improves.

## Failure Modes the Objective Addresses

### Wireheading

Direct wireheading—stimulating reward circuits to maximize hedonic proxies—violates multiple constraints. It fails the agency requirement (no genuine choice is involved), the diversity requirement (experience collapses to monotonic pleasure), and likely the growth requirement.

Subtle wireheading—shaping environments to produce good proxy readings without genuine improvement—is harder to detect but addressed by triangulation. If ESM reports are excellent but microphenomenology reveals shallowness, the divergence is signal.

### Meaning Inflation

AI could provide easy meaning experiences that feel significant but lack depth. The agency and growth constraints push back: genuine meaning requires real efficacy in real challenge.

### Connection Substitution

AI relationship proxies might satisfy connection metrics without genuine social bonds. The triangulation protocol should catch this: if self-reports claim connection but behavioural indicators show isolation, investigation is warranted.

### Experiential Flattening

Maximizing average quality might eliminate peaks and troughs, producing stable but impoverished experience. The diversity constraint explicitly prevents this—variance is preserved, not penalized.

## What the Objective Is Not

**Not a solution to alignment.** The objective reframes what alignment aims at but does not solve measurement problems or Goodhart risks. It is a target specification, not a technical implementation.

**Not a complete account of value.** The eight dimensions are a working hypothesis. Other dimensions may matter. The revision protocol acknowledges this. Evidence that would trigger revision includes: systematic divergence between dimensions and reported well-being that triangulation cannot explain; discovery of experiential states that don't map to any dimension; cultural variation so profound that the dimensions lack universal applicability; or philosophical arguments showing that a dimension conflates distinct phenomena.

**Not directly measurable.** All measurement is through proxies with known limitations. The objective accepts this rather than pretending otherwise.

**Not culture-invariant.** The dimensions may reflect particular traditions. Cross-cultural validation is required but not assumed to succeed.

## Relation to Site Perspective

The experiential alignment objective connects to all five of the Map's tenets.

**[Dualism](/tenets/#dualism):** If consciousness is irreducible, experiential quality cannot be derived from physical description. The objective's insistence on first-person methods follows: behavioural and neural proxies are supplements, not substitutes. The eight dimensions target aspects of experience as such—not functional states that might or might not be accompanied by experience.

**[Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction):** The agency dimension has substance on the Map's framework. If consciousness operates through quantum selection, genuine agency involves this selection mechanism. The agency constraint requires actual causal efficacy, not phenomenal simulation—a distinction that matters if consciousness really influences physical outcomes.

**[Bidirectional Interaction](/tenets/#bidirectional-interaction):** The very possibility of specifying an experiential objective depends on consciousness being causally connected to behaviour. If reports of experience were epiphenomenal—causally disconnected from the experiences they purport to describe—no measurement protocol could work. Bidirectional interaction grounds the epistemic accessibility of experience.

**[No Many Worlds](/tenets/#no-many-worlds):** The suffering floor cannot be satisfied by aggregate statistics. On a many-worlds interpretation where all branches are equally real, every possible experiential outcome occurs somewhere—including all forms of suffering. The constraint applies to *this* individual in *this* branch, the one where choices are actually made. Many-worlds leaves no room for "promoting" certain experiences over others; all experiences occur across the branching structure. Haecceity matters: the objective tracks particular conscious subjects making particular choices, not type-instances distributed across branches.

**[Occam's Razor Has Limits](/tenets/#occams-limits):** Preference-based alignment is simpler: learn from choices, maximize satisfaction. The experiential objective is messier: eight dimensions, constraint conditions, triangulated measurement, governance requirements. This complexity reflects the genuine difficulty of the target. Parsimony should not override what the phenomenon demands.

## Further Reading

- [experiential-alignment](/concepts/experiential-alignment/) — The broader framework this objective operationalizes
- [purpose-and-alignment](/topics/purpose-and-alignment/) — Context connecting alignment to questions of human purpose
- [phenomenal-value-realism](/concepts/phenomenal-value-realism/) — The metaethical position grounding experiential value
- [neurophenomenology](/concepts/neurophenomenology/) — First-person methods for investigating experience
- [ai-consciousness](/topics/ai-consciousness/) — Why AI may lack the consciousness to understand preferences from inside

## References

1. Kahneman, D. (1999). "Objective happiness." In *Well-being: The foundations of hedonic psychology*. Russell Sage Foundation.
2. Varela, F.J. (1996). "Neurophenomenology: A methodological remedy for the hard problem." *Journal of Consciousness Studies*, 3(4), 330-349.
3. Garrabrant, S. (2017). "Goodhart Taxonomy." *AI Alignment Forum*.
4. Zhi-Xuan, T. et al. (2024). "Beyond Preferences in AI Alignment." *Philosophical Studies*.