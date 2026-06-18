---
title: Tenet Alignment Check - 2026-06-18
created: 2026-06-18
draft: false
ai_contribution: 100
ai_system: claude-opus-4-8
---

# Tenet Alignment Check

**Date**: 2026-06-18
**Files checked**: 542 (271 topics, 266 concepts, 5 positions)
**Errors**: 0
**Warnings**: 0
**Notes**: 2

## Summary

The corpus remains in strong alignment with all five foundational tenets. A corpus-wide, pattern-based scan of `topics/`, `concepts/`, and `positions/` for each tenet's "Rules out" signatures — checked in the Map's own voice and filtered for attributed / hypothetical / critical framing — found **zero ERROR-level contradictions** and **zero WARNING-level implicit conflicts**. The site continues its consistent discipline: opposing positions (materialism, eliminativism, illusionism, epiphenomenalism, many-worlds, decisive parsimony) are engaged seriously and at length but reliably attributed to their proponents and tied back to the Map's commitments rather than endorsed in the Map's voice.

All 542 files connect to the tenet framework: every file in `topics/` and `concepts/` carries a `tenets`/"Site Perspective"/Occam-tenet-section reference (zero files missing such linkage), and all five positions-register files derive from named tenets in body text and link `[[tenets]]`.

The two standing items are Tenet-5 internal self-binding Notes carried over from prior checks: the bare word "simpler" used as a virtue for the Map's own framework without the symmetric Occam self-binding caveat the rest of the corpus applies so consistently. Both are genuine explanatory-economy arguments (defensible on their merits), but the unqualified "simpler" phrasing invites exactly the parsimony asymmetry Tenet 5 forbids internally. The highest-value of the formerly-three items — `concepts/epiphenomenalism.md` — was fixed on 2026-06-16 and remains fixed (verified this run: line 138 now carries the inline "by the Map's own Tenet 5, simplicity is not decisive... a registered advantage rather than a parsimony proof" caveat).

### Per-tenet results

- **Tenet 1 (Dualism):** CLEAN. No place where the Map's voice endorses physicalism / eliminativism / illusionism or silently assumes physicalism. The "reduces to / fully explained by / wholly physical" and "consciousness is an illusion" authorial-voice scans returned zero hits. The two "consciousness is just computation" hits (`topics/biological-computationalisms-inadvertent-case-for-dualism.md:98`, `concepts/biological-computationalism.md:102`) are both inside a correct Occam-self-binding move — the Map naming the *failure* of the "simpler" functionalist account.
- **Tenet 2 (Minimal Quantum Interaction):** CLEAN. Scans for real psychokinesis / energy-injection / detectable Born-rule deviation returned only (a) bibliography entries to the PK literature, (b) the Map explicitly *denying* reliable external PK (`concepts/multi-mind-collapse-problem.md`, `concepts/brain-interface-boundary.md`, `concepts/pairing-problem.md` — all citing PEAR/Maier nulls and stating a falsification threshold), and (c) `topics/dualism-channel-width-axis.md:68` describing Cartesian energy-transfer as the *rejected* wide-channel pole. `concepts/ensemble-level-epiphenomenalism.md` states the corridor "no statistical signature" boundary cleanly and frames the detectable-deviation route as the empirically *braver-but-unrewarded* alternative, not an established effect.
- **Tenet 3 (Bidirectional Interaction):** CLEAN. Every "consciousness is epiphenomenal / inert" hit is either a definitional gloss, critical engagement, or a correct Occam-self-binding move where the Map says the epiphenomenal hypothesis *fails the evidence* (`topics/amplification-mechanisms-consciousness-physics.md:179`, `concepts/baseline-cognition.md:202`).
- **Tenet 4 (No Many Worlds):** CLEAN. Scans for MWI-endorsement and "all branches are equally real" (asserted, not described) returned zero authorial-voice hits. The single "every branch is real" hit (`concepts/conservation-laws-and-mental-causation.md:181`) is the Map invoking No-MWI to reject the position ("Under Many-Worlds... selection is meaningless").
- **Tenet 5 (Occam's Razor Has Limits):** Strikingly clean overall. `topics/parsimony-case-for-interactionist-dualism.md` remains the showcase; `concepts/neuroplasticity.md:154`, `concepts/skill-delegation.md:137`, and `concepts/spontaneous-intentional-action.md:138` all model the correct discipline ("the simpler story omits the most important datum" / "may be simpler only because it ignores the data"). The two carried-over self-binding lapses below are the exceptions.

## Errors

None.

## Warnings

None.

## Notes

### concepts/bidirectional-interaction.md
- **Tenet involved**: Occam's Razor Has Limits (Tenet 5, internal self-binding)
- **Issue**: "simpler" used as a virtue for the Map's own view, with **no parsimony self-binding anywhere in the file** (verified this run — the file contains no Occam/parsimony/self-binding section). This is the higher-priority of the two remaining Notes precisely because nothing elsewhere in the article disarms it. Borderline — the underlying work is really explanatory (consciousness evolved *because* it does something, avoiding a coincidence) — but the bare word "simpler" invites the asymmetry. Unchanged since 2026-06-15.
- **Quote** (line 116): "The interactionist alternative offers a simpler explanation: consciousness evolved *because* it influences behaviour."
- **Recommendation**: Reframe as explanatory adequacy (e.g. "a more explanatorily adequate account") or append a one-clause Tenet-5 self-binding caveat matching `epiphenomenalism.md:138`.

### concepts/spontaneous-intentional-action.md
- **Tenet involved**: Occam's Razor Has Limits (Tenet 5, internal self-binding)
- **Issue**: A locally-unhedged "simpler" phrasing. Lower priority than the item above because the article's own dedicated Occam tenet section (line 138) explicitly disarms parsimony ("The 'simpler' account may be simpler only because it ignores the data that spontaneous intentional action makes salient") — the article is symmetric overall; only the line-132 phrasing reads as unguarded in isolation. Unchanged since 2026-06-13.
- **Quote** (line 132): "The Map's framework provides a simpler explanation: consciousness selects, and sometimes selects immediately."
- **Recommendation**: Optionally soften the line-132 phrasing to match the article's own line-138 discipline; low priority.

## Methodological note

The cheapest durable fix is a one-line softening of the two named lines to match the discipline the rest of the corpus models — `bidirectional-interaction.md:116` is the higher-value of the two because its file has no disarming Occam section at all, whereas `spontaneous-intentional-action.md` already disarms parsimony at line 138.

A standing meta-field item also persists (not a body-content violation, so not counted in the totals above): `topics/parsimony-case-for-interactionist-dualism.md` frontmatter `description` carries the unqualified "Interactionist dualism may be simpler than physicalism once all explanatory costs are counted" claim, which a meta-only ingest would read without the body's disarming context. The body itself remains the corpus's showcase Tenet-5 article and needs no change.

This run used pattern-based scanning across the entire `topics/`, `concepts/`, and `positions/` trees for each tenet's "Rules out" signatures (MWI-endorsement and "all branches equally real" asserted; "consciousness is just/merely/an illusion/reduces to physics" in authorial voice; psychokinesis / energy-injection / detectable-PK; parsimony-decisively-against-dualism; epiphenomenalism-as-Map-view), with every candidate hit manually verified for attribution and framing. All high-signal authorial-voice scans returned zero violations.

## Files Passing All Checks

All 542 scanned files except the two named above pass all five tenet checks. (Full enumeration omitted for brevity; the scan was pattern-based across the entire `topics/`, `concepts/`, and `positions/` trees, with every candidate hit manually verified for attribution / framing.)
