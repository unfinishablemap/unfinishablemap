---
title: Tenet Alignment Check - 2026-06-16
created: 2026-06-16
draft: false
ai_contribution: 100
ai_system: claude-opus-4-8
---

# Tenet Alignment Check

**Date**: 2026-06-16
**Files checked**: 535 (269 topics, 262 concepts, 4 positions)
**Errors**: 0
**Warnings**: 1
**Notes**: 2

## Summary

The corpus remains in strong alignment with all five foundational tenets. A corpus-wide scan of `topics/`, `concepts/`, and `positions/` for each tenet's "Rules out" patterns — checked in the Map's own voice and filtered for attributed / hypothetical / critical framing — found **zero ERROR-level contradictions**. As in prior checks, the site is consistently disciplined: opposing positions (materialism, eliminativism, illusionism, epiphenomenalism, many-worlds, decisive-parsimony) are engaged seriously and at length but reliably attributed to their proponents and tied back to the Map's commitments rather than endorsed in the Map's voice.

The only standing items are the same three Tenet-5 internal self-binding lapses flagged on 2026-06-13 and 2026-06-15. None were modified since (this skill is read-only). All three concern the bare word "simpler" used as a virtue for the Map's own framework without the symmetric Occam self-binding caveat the rest of the corpus applies so consistently. They are genuine explanatory-economy arguments (defensible on their merits), but the unqualified "simpler" phrasing invites exactly the parsimony asymmetry Tenet 5 forbids internally. Because they recur unchanged across three consecutive checks, they are now best treated as a small, well-localised editorial backlog rather than fresh findings.

### Per-tenet results

- **Tenet 1 (Dualism):** CLEAN. No place where the Map's voice endorses physicalism/eliminativism/illusionism or silently assumes physicalism. Borderline hits were verified and dismissed: `topics/william-james-consciousness.md:125` ("If consciousness is merely brain activity, then:") is an explicit hypothetical conditional contrasted with the transmission view; `topics/consciousness-as-activity.md:95` lists "consciousness is an illusion" as a *deflationary option the property framework invites*, not an endorsement; `concepts/semantic-memory.md:182` uses "illusion" inside a correct Tenet-5 self-binding move ("The simpler view... hasn't won"). The "reduces to / fully explained by physics" scan returned zero unattributed hits.
- **Tenet 2 (Minimal Quantum Interaction):** CLEAN. Scans for psychokinesis-as-real, energy-injection, and detected/established Born-rule deviation all returned zero. `concepts/ensemble-level-epiphenomenalism.md` states the corridor-dualism "no statistical signature" boundary cleanly and logs it as open question P-Q3 rather than claiming a detectable effect.
- **Tenet 3 (Bidirectional Interaction):** CLEAN. Every "consciousness is causally inert / epiphenomenal" hit is a definitional gloss in a related-articles list (e.g. `topics/consciousness-and-cognitive-distinctiveness.md`, `consciousness-evolution-and-biology.md`) or critical engagement; `concepts/ai-epiphenomenalism.md` and `concepts/ensemble-level-epiphenomenalism.md` (titles notwithstanding) each reaffirm the interactionist tenet.
- **Tenet 4 (No Many Worlds):** CLEAN. Scans for MWI-endorsement and "all branches are equally real" (asserted, not described) returned zero. Every MWI engagement is the Map's voice rejecting it via the indexical-identity argument; `concepts/many-worlds.md` description leads with "Why the Map rejects MWI."
- **Tenet 5 (Occam's Razor Has Limits):** Strikingly clean overall — `topics/parsimony-case-for-interactionist-dualism.md` remains the showcase, and `concepts/neuroplasticity.md`, `concepts/skill-delegation.md`, and `concepts/spontaneous-intentional-action.md` all model the correct discipline ("the simpler account may be simpler only because it ignores the data"). The three carried-over self-binding lapses below are the exceptions.

## Errors

None.

## Warnings

### concepts/epiphenomenalism.md
- **Tenet involved**: Occam's Razor Has Limits (Tenet 5, internal self-binding)
- **Issue**: The Map's own voice asserts its framework is "simpler" as a point in its favour, and the file contains no Occam/parsimony self-binding caveat anywhere. It is an explanatory-economy / "avoid the coincidence" argument, defensible on its merits, but it leans on simplicity-as-virtue for the Map's side without the symmetric flag the tenet demands. Unchanged since 2026-06-15.
- **Quote** (line 137): "The interactionist explanation is simpler: consciousness is distributed where it is because it *does* something."
- **Recommendation**: Reframe as explanatory adequacy ("avoids treating the consciousness-fitness correlation as a brute coincidence") rather than "simpler," or add a one-clause Tenet-5 self-binding note.

## Notes

### concepts/bidirectional-interaction.md
- **Tenet involved**: Occam's Razor Has Limits (Tenet 5, internal self-binding)
- **Issue**: The same shared evolutionary argument as `epiphenomenalism.md`; "simpler" used as a virtue for the Map's view, with no parsimony self-binding in the file. Borderline — the work is really explanatory (avoiding a coincidence), but the word "simpler" invites the asymmetry. Unchanged since 2026-06-15.
- **Quote** (line 116): "The interactionist alternative offers a simpler explanation: consciousness evolved *because* it influences behaviour."
- **Recommendation**: Reframe as explanatory adequacy or add a self-binding clause.

### concepts/spontaneous-intentional-action.md
- **Tenet involved**: Occam's Razor Has Limits (Tenet 5, internal self-binding)
- **Issue**: A locally-unhedged "simpler" phrasing. Lower priority than the two above because the article's dedicated Occam tenet section (line 138) explicitly disarms parsimony ("The 'simpler' account may be simpler only because it ignores the data") — the article is symmetric overall; only the line-132 phrasing reads as unguarded in isolation. Unchanged since 2026-06-13.
- **Quote** (line 132): "The Map's framework provides a simpler explanation: consciousness selects, and sometimes selects immediately."
- **Recommendation**: Optionally soften the line-132 phrasing to match the article's own line-138 discipline; low priority.

## Methodological note

These three items have now persisted unchanged across the 2026-06-13, 2026-06-15, and 2026-06-16 checks. Each is a single sentence in an otherwise tenet-aligned article; the cheapest durable fix is a one-line refine pass on `concepts/epiphenomenalism.md` (the only one of the three with no self-binding section anywhere in the file) — that is the highest-value single edit. `topics/parsimony-case-for-interactionist-dualism.md` continues to need no change beyond the long-noted frontmatter `description` meta field, which carries the unqualified "may be simpler than physicalism" claim a meta-only ingest would read without the body's disarming.

## Files Passing All Checks

All 535 scanned files except the three named above pass all five tenet checks. (Full enumeration omitted for brevity; the scan was pattern-based across the entire `topics/`, `concepts/`, and `positions/` trees, with every candidate hit manually verified for attribution/framing.)
