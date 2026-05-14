---
title: Tenet Alignment Check - 2026-05-14
created: 2026-05-14
modified: 2026-05-14
human_modified: null
ai_modified: 2026-05-14T00:18:00+00:00
draft: false
description: "Tenet alignment scan of topics/ and concepts/. No direct contradictions found; all flagged matches resolve as critical engagement with ruled-out positions."
topics: []
concepts: []
related_articles:
  - "[[tenets]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-14
last_curated: null
---

# Tenet Alignment Check

**Date**: 2026-05-14
**Files checked**: 239 topics + 237 concepts = 476
**Errors**: 0
**Warnings**: 0
**Notes**: 0

## Summary

Scanned `obsidian/topics/` and `obsidian/concepts/` against the five foundational tenets (Dualism, Minimal Quantum Interaction, Bidirectional Interaction, No Many Worlds, Occam's Razor Has Limits) as defined in `obsidian/tenets/tenets.md`.

Searches targeted canonical violation patterns across all five tenets:

- Reductionist claims (consciousness reduces to / is just / is merely physical, neural, brain, neurons)
- Endorsements of illusionism (consciousness as illusion, qualia as illusory, qualia don't exist)
- Endorsements of epiphenomenalism (consciousness is epiphenomenal, epiphenomenalism is true)
- Endorsements of MWI (MWI is correct/true, accept many-worlds, all branches equally real as commitment)
- Parsimony deployed decisively against dualism (Occam's Razor refutes/rules out dualism)
- Dismissal of indexical identity as meaningless
- Quantum mysticism / paranormal channels (psychokinesis, telepathy, ESP as endorsed mechanism)

Every flagged occurrence resolved on inspection to one of:

- **Conditional setup** ("If consciousness is merely brain activity, then…") with the surrounding argument rejecting the antecedent — e.g., `topics/william-james-consciousness.md:125`.
- **Attribution to opposing position** ("Illusionism holds that phenomenal consciousness is an illusion…") presented as a view the Map argues against — pervasive across `concepts/epiphenomenalism.md`, `concepts/attention-schema-theory.md`, `concepts/functional-seeming.md`, etc.
- **Direct refutation** of the ruled-out position — e.g., `concepts/quantum-consciousness.md:196` and `concepts/luck-objection.md:139` both quote materialist framings only to dissolve them.
- **Tenet-affirming paraphrase** ("consciousness is not reducible to physical processes") used to *state* the Map's commitment — dominant pattern across both directories.
- **Principled disavowal of paranormal extension** — `topics/memory-anomalies.md:89` explicitly states "The Map's dualism is principled and does not extend to [paranormal] claims," and parapsychology references elsewhere serve to locate the interface boundary or report the null/contested empirical record rather than endorse psi.

The tenets-page convergence work logged in earlier checks (most recently 2026-05-11) — which tightened the parsimony-discipline boundary, registered Tenet 5's symmetric self-binding, and relocated the No-Many-Worlds case onto the indexical objection — appears stable downstream. No article was found leaking the older asymmetry, and no recent edits (the cluster modified 2026-05-13) introduced new asymmetries.

Content is in alignment with the tenets. No remediation required.

## Errors

None.

## Warnings

None.

## Notes

None this cycle. The single phrasing artefact flagged on 2026-05-11 (`topics/emergence-as-universal-hard-problem.md:102` "Consciousness is simply where it shows") was rechecked: the surrounding paragraph still disambiguates it as affirming irreducibility rather than reduction, and the article has not been recondensed in a way that would isolate the snippet.

## Files Passing All Checks

All 476 files in `obsidian/topics/` and `obsidian/concepts/` pass the tenet-alignment scan. The check operated by pattern-search across the directories with targeted reads of every flagged location.

## Scope and Method

- **In scope**: `obsidian/topics/` and `obsidian/concepts/` per skill specification.
- **Out of scope this pass**: `apex/`, `voids/`, `arguments/`, `reviews/`, `research/`, `workflow/`, `project/`. Spot-checking surfaced no obvious issues in those directories during scanning (the one match in `voids/conceptual-scheme-void.md` characterises MWI as ruled out, not endorsed), but a dedicated pass would be needed to claim alignment for them.
- **Method**: ripgrep patterns for canonical violation language (reduction claims, illusion-of-consciousness, MWI endorsement, parapsychology/psychokinesis terms, parsimony-as-decisive-against-dualism, dismissal of indexical identity), followed by targeted reads of all flagged contexts to distinguish position-discussion from position-endorsement.
