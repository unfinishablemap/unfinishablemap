---
title: Tenet Alignment Check - 2026-05-29
created: 2026-05-29
draft: false
ai_contribution: 100
ai_system: claude-opus-4-8
---

# Tenet Alignment Check

**Date**: 2026-05-29
**Files checked**: 509 (258 topics, 251 concepts)
**Errors**: 0
**Warnings**: 0
**Notes**: 1

## Summary

No tenet contradictions. The corpus references all five tenets' "ruled-out" positions
(eliminative materialism, illusionism, the many-worlds interpretation, epiphenomenalism,
reductive physicalism) pervasively, but in every checked case these appear as *named
opponents the Map argues against*, not as endorsed positions. The dedicated opponent-position
articles (`topics/eliminative-materialism.md`, `concepts/illusionism.md`, `concepts/many-worlds.md`,
`concepts/materialism.md`, `concepts/epiphenomenalism.md`) each carry a proper "Relation to Site
Perspective" section that explicitly rejects the view and ties the rejection to the relevant tenet.

Pattern scans for endorsement-shaped phrasing — "consciousness is just neurons/brain activity",
"consciousness is epiphenomenal/causally inert", "MWI is true/correct" — surfaced only
conditional, opponent-framed, or Tenet-5-discounted occurrences (e.g. "If consciousness is
epiphenomenal, then…" framing that sets up a rebuttal). None assert a ruled-out position in the
Map's own voice.

This result matches the 2026-05-25 through 2026-05-27 checks (0/0/0), confirming a stable,
tenet-aligned corpus.

## Errors

None.

## Warnings

None.

## Notes

### concepts/quantum-indeterminacy-free-will.md
- **Tenet involved**: Tenet 4 (No Many Worlds) / Tenet 5 (Occam's Razor Has Limits) — internal consistency, not contradiction
- **Issue**: Line 139 states the Map rejects MWI "for ontological extravagance, the indexical problem, the probability problem…", *leading* with ontological extravagance. The updated `tenets.md` (Tenet 4 "Rationale (subsidiary—ontological multiplicity, qualified)" and Tenet 5 "Application to the Map's own arguments") now explicitly **demotes** the ontological-multiplicity objection to subsidiary status and requires the MWI rejection to rest *primarily* on the indexical objection, because the parsimony complaint is disarmed by Tenet 5's self-binding.
- **Quote**: "The Map's [[tenets#^no-many-worlds|No Many Worlds]] tenet rejects this for ontological extravagance, the indexical problem, the probability problem, and for eliminating any role for consciousness."
- **Recommendation**: Reorder so the indexical objection leads and ontological extravagance is marked subsidiary, matching the canonical tenet phrasing. Optional/cosmetic — no reader is misled about the Map's position; this is corpus self-consistency hygiene. (`concepts/many-worlds.md` and `concepts/conservation-laws-and-mental-causation.md` already lead with the indexical objection and are clean; `topics/vertiginous-question.md` correctly frames it as "the strongest connection… explicitly cites the indexical problem".)

## Files Passing All Checks

All 509 files (every file in `topics/` and `concepts/`) pass the error and warning checks.
The single file above is a NOTE for optional internal-consistency tidying, not a failure.
