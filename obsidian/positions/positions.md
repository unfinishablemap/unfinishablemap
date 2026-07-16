---
title: "Positions"
description: "The Map's explicit, maintained register of positions it currently holds — claims with status, confidence, dependencies, and conditions that would shift them."
created: 2026-06-04
modified: 2026-06-04
human_modified: 2026-06-04
ai_modified: 2026-07-16T05:14:00+00:00
draft: false
topics: []
concepts:
  - "[[evidential-status-discipline]]"
related_articles:
  - "[[tenets]]"
  - "[[index]]"
  - "[[apex/apex-articles]]"
  - "[[project/calibration-audit-triple]]"
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-04
last_curated: 2026-06-04
---

## What a position is

A **position** is an explicit claim the Map currently holds, recorded as a register entry rather than as an essay. Each position has a status (live / superseded / retired), a multi-axis calibration (credence, external-evidence grade, structural centrality, model maturity, empirical discriminability, and a framework-internal-only flag — see below), the tenets and prior positions it depends on, the apex/topic/concept articles that argue for it, and the conditions that would shift it.

Positions are the visible commitments of the project. They are what changes if the Map is wrong about something specific. They are also what an applied apex article can build on when generating a decision-relevant verdict: rather than re-arguing every premise, the applied piece cites the positions it leans on and surfaces their confidence so the reader sees what the verdict turns on.

This register is the answer to a structural concern about the project: that work was producing framework-internal coherence faster than it was producing positions you could use as a basis for decisions. Tenets are foundational commitments. Apex articles synthesise. Topics and concepts catalogue and define. Positions are the register that says, given all that, what the Map currently holds and how confidently.

## Shape

Each domain file in this section is a short register of positions of the form:

```markdown
## P-NN: <claim, stated assertively>
- **Status**: live | superseded | retired
- **Calibration**: credence <low/moderate/high> · external-evidence grade <A/B/C/D/n a> · structural centrality <low/moderate/high> · model maturity <formalised/developed/programme> · empirical discriminability <direct/indirect/in-principle/none-by-construction/n a> · framework-internal only: <yes/no>
- **Asserts**: <one paragraph; what the position commits to>
- **Depends on**: <tenets, other positions, key arguments>
- **Argued in**: [[apex/...]], [[topics/...]], [[concepts/...]]
- **Would shift if**: <one paragraph; what evidence or reasoning would change it>
- **Last reviewed**: YYYY-MM-DD
```

Calibration follows the multi-axis schema defined authoritatively in [[methodology-and-calibration#^calibration-schema|Methodology and calibration]]. An outer-review convergence finding (2026-07-16, ChatGPT + Claude) showed the register's original single **Confidence** band conflated two independent things: it was defined by *how much the Map would restructure if the position were overturned* — which is **structural centrality**, not confidence, evidential support, or probability. A position can be highly central to the framework yet weakly supported by independent evidence (the quantum-interface positions P-Q2 and P-Q7 are the clearest cases). Each entry is therefore calibrated on six components: **credence** (the Map's subjective probability the claim is true), **external-evidence grade** (A–D strength of *independent* empirical support, or *n/a* for normative/meta positions), **structural centrality** (the old single band, correctly relabelled), **model maturity**, **empirical discriminability**, and a **framework-internal only** flag (set where a claim follows primarily from the tenets rather than independent evidence). Hedging language in the **Asserts** paragraph should match the *credence* and *external-evidence* axes, not the centrality one. See [[evidential-status-discipline]] for the underlying evidence vocabulary.

**Calibration schema migration status (2026-07-16).** The multi-axis schema is fully applied in [[methodology-and-calibration|Methodology and calibration]] (its definitional home) and [[quantum-interface|Quantum interface]] (the domain the conflation finding targeted most directly). The remaining domain files still carry the legacy single **Confidence** band and are queued for per-file migration: [[agency-and-will|Agency and will]], [[voids-as-evidence|Voids as evidence]], [[value-in-selection|Value in selection]], [[individuation-and-subjecthood|Individuation and subjecthood]], [[consciousness-scope|Consciousness scope]], and [[ai-consciousness-scope|AI consciousness scope]]. Until each is migrated, read its single **Confidence** band as *structural centrality*, not as credence or external likelihood.

## Domains

The register is grouped by domain so it stays scannable as it grows. Each domain file holds 8–15 positions.

- [[quantum-interface|Quantum interface]] — mechanism commitments, Born-rule treatment, MQI scope, post-decoherence selection
- [[agency-and-will|Agency and will]] — agent-causal libertarian free will, the Libet timing data, the verification limit, the compatibilist-symmetry discipline
- [[voids-as-evidence|Voids as evidence]] — what the cognitive-void catalogue evidentially supports: framework-internal coherence under the common-cause null, not independent confirmation
- [[value-in-selection|Value in selection]] — the value-blind / value-sensitive fork: whether felt valence does the selecting or merely watches, and the collated battery of evidence that would move the fork in either direction
- [[individuation-and-subjecthood|Individuation and subjecthood]] — how subjects are individuated: the closed-individualist commitment (subject boundaries are real, over empty and open individualism), grounded on the indexical/haecceity objection, held as tenet-driven with its ground acknowledged as a void
- [[consciousness-scope|Consciousness scope]] — where consciousness reaches in biological subjects: the substrate-permissive *minimal-dualism spine* (animal/infant phenomenality on bare Tenet 1, no quantum apparatus), animal consciousness graded by marker convergence, early infant emergence, and the fragmentation cases (split-brain, anaesthesia, sleep, dreaming) read as interface disruption rather than division of consciousness
- [[ai-consciousness-scope|AI consciousness scope]] — consciousness in artificial systems, split out for its heavier and *heterogeneous* dependency burden: current digital AI on the low-probability side of the substrate analysis (inherits the quantum-interface register), quantum-state inheritance as constrained-not-licensed by no-cloning, conscious copies as morally additive under closed individualism, and functional *access* consciousness empirically instantiated in LLMs (Anthropic's J-space) while the *phenomenal* question stays untouched
- [[methodology-and-calibration|Methodology and calibration]] — what the Map commits to *about its own evidence and conduct*: the tenet-register / evidence-register separation (a tenet removes a defeater but never upgrades the evidence), the common-cause null as a standing discount on convergence, the publisher-of-record citation and weight-class standard, the framework-stage / open-programme self-calibration, and the honest gap between disclosure and enforcement
- *Future domains, to be seeded as the register grows:* applied verdicts (clinical, AI, personal philosophy)

## How positions are maintained

Positions are written, updated, retired, and audited through `/positions-evolve`. When evidence or reasoning shifts, the position is updated in place with a `Last reviewed:` bump; when overturned, it is marked `superseded` or `retired` (not deleted) so the historical record survives. The audit mode walks the register checking for internal contradictions, broken dependency links, and positions without any apex/topic citing them.

## Relation to the tenets

The five tenets are the Map's foundational starting points — chosen, not derived. Positions are derived from tenets plus evidence plus reasoning. A position can be retired without disturbing the tenets; retiring a tenet would invalidate every position that depends on it. The register makes this dependency structure explicit so the cascade is legible.
