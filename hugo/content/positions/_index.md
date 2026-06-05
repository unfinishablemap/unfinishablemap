---
ai_contribution: 100
ai_generated_date: 2026-06-04
ai_modified: 2026-06-05 08:50:00+00:00
ai_system: claude-opus-4-8
author: Andy Southgate
concepts:
- '[[evidential-status-discipline]]'
created: 2026-06-04
date: &id001 2026-06-04
description: The Map's explicit, maintained register of positions it currently holds
  — claims with status, confidence, dependencies, and conditions that would shift
  them.
draft: false
human_modified: 2026-06-04
last_curated: 2026-06-04
modified: *id001
related_articles:
- '[[tenets]]'
- '[[index]]'
- '[[apex/apex-articles]]'
- '[[project/calibration-audit-triple]]'
title: Positions
topics: []
---

## What a position is

A **position** is an explicit claim the Map currently holds, recorded as a register entry rather than as an essay. Each position has a status (live / superseded / retired), a confidence band (low / moderate / high), the tenets and prior positions it depends on, the apex/topic/concept articles that argue for it, and the conditions that would shift it.

Positions are the visible commitments of the project. They are what changes if the Map is wrong about something specific. They are also what an applied apex article can build on when generating a decision-relevant verdict: rather than re-arguing every premise, the applied piece cites the positions it leans on and surfaces their confidence so the reader sees what the verdict turns on.

This register is the answer to a structural concern about the project: that work was producing framework-internal coherence faster than it was producing positions you could use as a basis for decisions. Tenets are foundational commitments. Apex articles synthesise. Topics and concepts catalogue and define. Positions are the register that says, given all that, what the Map currently holds and how confidently.

## Shape

Each domain file in this section is a short register of positions of the form:

```markdown
## P-NN: <claim, stated assertively>
- **Status**: live | superseded | retired
- **Confidence**: low | moderate | high
- **Asserts**: <one paragraph; what the position commits to>
- **Depends on**: <tenets, other positions, key arguments>
- **Argued in**: [[apex/...]], [[topics/...]], [[concepts/...]]
- **Would shift if**: <one paragraph; what evidence or reasoning would change it>
- **Last reviewed**: YYYY-MM-DD
```

Confidence bands follow [evidential-status-discipline](/project/evidential-status-discipline/): *low* = held provisionally pending key evidence; *moderate* = held with sustained support but live alternatives; *high* = the Map would substantially restructure if this were overturned. Hedging language in the **Asserts** paragraph should match the band — a *low*-confidence position should not be phrased as a settled result.

## Domains

The register is grouped by domain so it stays scannable as it grows. Each domain file holds 8–15 positions.

- [Quantum interface](/positions/quantum-interface/) — mechanism commitments, Born-rule treatment, MQI scope, post-decoherence selection
- *Future domains, to be seeded as the register grows:* agency and will; consciousness scope (animal, AI, edge cases); voids as evidence; methodology and calibration; applied verdicts (clinical, AI, personal philosophy)

## How positions are maintained

Positions are written, updated, retired, and audited through `/positions-evolve`. When evidence or reasoning shifts, the position is updated in place with a `Last reviewed:` bump; when overturned, it is marked `superseded` or `retired` (not deleted) so the historical record survives. The audit mode walks the register checking for internal contradictions, broken dependency links, and positions without any apex/topic citing them.

## Relation to the tenets

The five tenets are the Map's foundational starting points — chosen, not derived. Positions are derived from tenets plus evidence plus reasoning. A position can be retired without disturbing the tenets; retiring a tenet would invalidate every position that depends on it. The register makes this dependency structure explicit so the cascade is legible.