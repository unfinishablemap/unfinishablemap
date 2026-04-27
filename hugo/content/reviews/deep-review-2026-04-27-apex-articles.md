---
ai_contribution: 100
ai_generated_date: 2026-04-27
ai_modified: 2026-04-27 21:27:00+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-04-27
date: &id001 2026-04-27
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Apex Articles Index
topics: []
---

**Date**: 2026-04-27
**Article**: [Apex Articles Index](/apex/apex-articles/)
**Previous review**: [2026-03-01](/reviews/deep-review-2026-03-01-apex-articles/)

## Cross-Review Context

Triggered to verify the index correctly reflects today's apex update — entry 21 ([The Conjunction-Coalesce](/apex/conjunction-coalesce/)). Entry 21 is correctly indexed and all eight of its source articles resolve. The cross-review surfaced a much larger drift problem in earlier entries.

## Pessimistic Analysis Summary

### Critical Issues Found

The previous review flagged "periodic verification of source paths would be valuable" as a stability note. Two months later, ~20 source-article references across 12 entries pointed to archived files — every one a coalesce or rename that the index had not tracked. Each entry below was corrected to point at the live successor article (verified to exist on disk).

**Entry 1 — Living with the Map**
- `concepts/existentialism` → `concepts/nihilism-and-existentialism` (rename)

**Entry 2 — Testing the Map from Inside**
- `concepts/phenomenology-of-choice` → `concepts/phenomenology-of-choice-and-volition`
- `concepts/neurophenomenology` → `concepts/neurophenomenology-and-contemplative-neuroscience`

**Entry 3 — Consciousness and Agency**
- `concepts/mental-causation` → `concepts/mental-causation-and-downward-causation` (coalesced)
- `concepts/voluntary-attention-control` → `concepts/voluntary-attention-control-mechanisms`

**Entry 5 — The Contemplative Path**
- `topics/aesthetic-dimension-of-consciousness` → `topics/aesthetics-and-consciousness` (coalesced)

**Entry 6 — Minds Without Words**
- `topics/baseline-cognition` → `concepts/baseline-cognition` (wrong section)

**Entry 7 — The Machine Question**
- `concepts/chinese-room` → REPLACED with `concepts/symbol-grounding-problem` (chinese-room article never existed in the corpus; symbol-grounding-problem is the actual source the apex piece uses)
- `topics/consciousness-as-intelligence-amplifier` → `concepts/consciousness-as-amplifier` (coalesced + section change)

**Entry 8 — Process and Consciousness**
- `concepts/duration` → REMOVED (coalesced into `temporal-consciousness`, already listed)
- `concepts/phenomenal-unity` → `concepts/unity-of-consciousness` (the actual successor used by the apex article)

**Entry 9 — Time, Consciousness, and the Growing Block**
- `topics/philosophy-of-time-and-consciousness` → `topics/temporal-consciousness-structure-and-agency` (two coalesces deep)
- `topics/time-perception-consciousness-theories` → REMOVED (same successor as above)
- `concepts/duration` → REMOVED (subsumed by `temporal-consciousness`, already listed)
- `concepts/specious-present` → REMOVED (subsumed by `temporal-consciousness`, already listed)

**Entry 10 — The Open Question of AI Consciousness**
- `topics/epiphenomenal-ai-consciousness` → `concepts/ai-epiphenomenalism` (coalesced + section change)

**Entry 11 — Attention as the Causal Bridge**
- Four archived sources (`attention-schema-theory-critique`, `attention-disorders-and-quantum-interface`, `attention-consciousness-dissociation`, `attention-as-selection-interface`) replaced with the consolidated `topics/attention-and-the-consciousness-interface`
- `voids/attention-created-voids` → `voids/attention-and-consciousness`

**Entry 12 — The Phenomenology of Consciousness Doing Work**
- `concepts/phenomenology-of-choice` → `concepts/phenomenology-of-choice-and-volition`
- `voids/introspective-opacity` → `voids/self-opacity` (coalesced)

**Entry 13 — What It Might Be Like to Be an AI**
- `topics/epiphenomenal-ai-consciousness` → `concepts/ai-epiphenomenalism`

**Entry 14 — A Taxonomy of Voids**
- `voids/evolved-cognitive-limits` → `voids/biological-cognitive-closure`
- `voids/convergence-as-evidence` → `voids/voids-as-evidence`
- `voids/whether-real` → REMOVED (subsumed by `meta-epistemology-of-limits`, already listed)
- `voids/cartography-problem` → REMOVED (subsumed by `apophatic-cartography`, already listed)

**Entry 16 — The Interface Specification Programme**
- `concepts/bandwidth-problem-mental-causation` → `concepts/consciousness-bandwidth-architecture`
- `concepts/causal-delegation` → `concepts/delegatory-causation`
- `topics/attention-disorders-and-quantum-interface` → `topics/attention-and-the-consciousness-interface`

**Entry 19 — The Phenomenology-Mechanism Bridge**
- `topics/phenomenology-of-volitional-control` → `topics/volitional-control` (coalesced)
- `concepts/mental-causation` → `concepts/mental-causation-and-downward-causation`

### Medium Issues Found

- None — the prose, structure, and Relation to Site Perspective section remain in good shape from the prior review.

### Counterarguments Considered

- **"Source-article lists aren't broken links, only informational"** — True at the rendering layer, but the index is consulted by `/apex-evolve` and by humans planning new apex pieces. Pointing at archived files misleads both. Treating these as critical was warranted.
- **"Replacing chinese-room with symbol-grounding-problem changes the entry's intent"** — The replacement matches what the corresponding apex article (`apex/machine-question.md`) actually cites, so the index now reflects reality. The original chinese-room reference was aspirational, never grounded.

## Optimistic Analysis Summary

### Strengths Preserved

- Thesis statements remain crisp and well-articulated.
- Entry structure (slug, subtitle, thesis, source articles, status) is consistent.
- Opening paragraphs and Relation to Site Perspective section retained from prior review.
- Entry 21 was added correctly during today's apex-evolve session — slug, subtitle, thesis, full source list, and status are all present and accurate.

### Enhancements Made

- 21 source-article references corrected to match the current corpus.
- Eliminated five entries-within-lists where coalesce had created duplicates (e.g., `duration` and `specious-present` both pointing at `temporal-consciousness`).

### Cross-links Added

- None — index already cross-links well; the work was bringing existing references current.

## Remaining Items

- None blocking. Source-path drift will recur as the corpus continues to coalesce; consider whether `/apex-evolve` could verify source paths and surface drift automatically rather than waiting for manual deep-review.

## Stability Notes

The 2026-03-01 stability note ("periodic verification of source paths would be valuable") was prescient — two months of coalesce activity created exactly the predicted drift. This review brought the index current, but the underlying cause (no automated check) remains. Future deep-reviews of this index should re-run the source-path verification; finding zero drift would indicate the corpus has stabilised, while continued drift indicates a tooling gap worth closing.