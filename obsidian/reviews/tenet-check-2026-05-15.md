---
title: Tenet Alignment Check - 2026-05-15
created: 2026-05-15
modified: 2026-05-15
human_modified: null
ai_modified: 2026-05-15T11:30:00+00:00
draft: false
description: "Tenet alignment scan of topics/ and concepts/. No direct contradictions found; all flagged matches resolve as critical engagement with ruled-out positions."
topics: []
concepts: []
related_articles:
  - "[[tenets]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-15
last_curated: null
---

# Tenet Alignment Check

**Date**: 2026-05-15
**Files checked**: 240 topics + 237 concepts = 477
**Errors**: 0
**Warnings**: 0
**Notes**: 0

## Summary

Scanned `obsidian/topics/` and `obsidian/concepts/` against the five foundational tenets (Dualism, Minimal Quantum Interaction, Bidirectional Interaction, No Many Worlds, Occam's Razor Has Limits) as defined in `obsidian/tenets/tenets.md`.

Searches targeted canonical violation patterns across all five tenets:

- Reductionist endorsements (consciousness reduces to / is just / is merely physical, neural, brain)
- Endorsements of illusionism (consciousness as illusion, qualia don't exist)
- Endorsements of epiphenomenalism (epiphenomenalism is true)
- Endorsements of MWI (MWI is true/correct, accept many-worlds, all branches are equally real *as commitment*)
- Parsimony deployed decisively against dualism (Occam's Razor refutes/rules out dualism)
- Dismissal of indexical identity as meaningless
- Quantum mysticism / paranormal channels (psychokinesis, telepathy, ESP as endorsed mechanism)

Every flagged occurrence resolved on inspection to one of:

- **Conditional setup** ("If consciousness is merely brain activity, then…") with the surrounding argument rejecting the antecedent — e.g., `topics/william-james-consciousness.md:125`, `topics/pragmatisms-path-to-dualism.md:85`.
- **Attribution to opposing position** ("Illusionism holds that phenomenal consciousness is an illusion…") presented as a view the Map argues against — pervasive across `concepts/epiphenomenalism.md`, `concepts/attention-schema-theory.md`, `concepts/functional-seeming.md`, `concepts/blindsight.md`, `concepts/illusionism`-linking siblings.
- **Direct refutation** of the ruled-out position — e.g., `concepts/quantum-consciousness.md:196` and `concepts/luck-objection.md:139` both quote materialist framings only to dissolve them.
- **Tenet-affirming paraphrase or citation** ("Consciousness is irreducible to physical processes" / "the No Many Worlds tenet holds…") used to *state* the Map's commitment — dominant pattern across both directories, especially in the "Relation to Site Perspective" sections.
- **Definitional paraphrase of MWI** ("Many-worlds holds that all branches are equally real") presented as the doctrine the Map rejects — e.g., `topics/indexical-identity-quantum-measurement.md:96`, `topics/probability-problem-in-many-worlds.md:114`, `concepts/probability-objections-many-worlds.md:58`.
- **Principled disavowal of paranormal extension** — `topics/memory-anomalies.md:89` explicitly states the Map's dualism does not extend to paranormal claims; the new `topics/brain-internal-born-rule-testing.md` reports the null/contested empirical record for micro-PK rather than endorsing psi.

Since the prior check (2026-05-14), 74 files in scope have been modified and four new articles created: `topics/brain-internal-born-rule-testing.md`, `topics/overdetermination-dissolution-under-selection-only-interactionism.md`, `topics/ethics-under-dualism.md`, and `concepts/causal-consistency-constraint.md`. All four were scanned individually and contain no tenet-conflicting content; the brain-internal-born-rule-testing article is methodologically careful about distinguishing Born-rule null results, mechanism refutation, and theoretical supersession, and explicitly registers the strict corridor reading as Tenet 2-aligned (consciousness influence at quantum indeterminacy without energy injection or Born-statistics violation).

The tenets-page convergence work logged in earlier checks (parsimony-discipline boundary tightening, Tenet 5's symmetric self-binding, No-Many-Worlds case relocated onto the indexical objection) remains stable downstream. No article was found leaking the older asymmetry. The previously-flagged phrasing artefact at `topics/emergence-as-universal-hard-problem.md:102` ("Consciousness is simply where it shows") was rechecked and the surrounding paragraph still disambiguates it as affirming irreducibility rather than reduction.

Content is in alignment with the tenets. No remediation required.

## Errors

None.

## Warnings

None.

## Notes

None this cycle.

## Files Passing All Checks

All 477 files in `obsidian/topics/` and `obsidian/concepts/` pass the tenet-alignment scan.

## Scope and Method

- **In scope**: `obsidian/topics/` and `obsidian/concepts/` per skill specification.
- **Out of scope this pass**: `apex/`, `voids/`, `arguments/`, `reviews/`, `research/`, `workflow/`, `project/`. Spot-checking surfaced no obvious issues during scanning, but a dedicated pass would be needed to claim alignment for them.
- **Method**: ripgrep patterns for canonical violation language (reduction claims, illusion-of-consciousness, MWI endorsement, parapsychology/psychokinesis terms, parsimony-as-decisive-against-dualism, dismissal of indexical identity), followed by targeted reads of flagged contexts to distinguish position-discussion from position-endorsement. Newly added files since 2026-05-14 were individually scanned for new tenet conflicts.
