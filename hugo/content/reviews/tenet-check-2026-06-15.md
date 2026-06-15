---
ai_contribution: 100
ai_system: claude-opus-4-8
concepts: []
created: 2026-06-15
date: '2026-06-15'
draft: false
related_articles: []
title: Tenet Alignment Check - 2026-06-15
---

# Tenet Alignment Check

**Date**: 2026-06-15
**Files checked**: 535 (268 topics, 263 concepts, 4 positions)
**Errors**: 0
**Warnings**: 1
**Notes**: 2

## Summary

The corpus is in strong alignment with all five foundational tenets. A parallel scan across `topics/` and `concepts/` for each tenet's "Rules out" patterns found **zero ERROR-level contradictions**. The site is consistently and unusually disciplined about its editorial convention: opposing positions (materialism, eliminativism, illusionism, epiphenomenalism, many-worlds, decisive-parsimony) are engaged seriously and at length, but are reliably attributed to their proponents and tied back to the Map's commitments rather than endorsed in the Map's own voice.

The only items worth flagging are three places in the parsimony self-binding discipline (Tenet 5). All three sit at WARNING/NOTE level and concern the same shared evolutionary "avoid-the-coincidence" argument: the word "simpler" is used as a virtue for the Map's own framework without the Tenet-5 self-binding caveat that the rest of the corpus applies so consistently. These are explanatory-economy arguments (defensible on their merits), but the bare "simpler" phrasing invites exactly the parsimony asymmetry Tenet 5 forbids internally.

### Per-tenet results

- **Tenet 1 (Dualism):** CLEAN. No place where the Map's voice endorses physicalism/eliminativism/illusionism or silently assumes physicalism. [concepts/materialism.md](/concepts/materialism/) explicitly states "The Unfinishable Map's tenets reject materialism"; all "it is brain activity" phrasings are attributed to the described view ("On this view...").
- **Tenet 2 (Minimal Quantum Interaction):** CLEAN. Repeated explicit disavowals ("Not psychokinesis", "not an endorsement of 'quantum woo'"). Parapsychology null results (PEAR, Bösch 2006, Maier-Dechamps 2018) are treated as the empirical *bound* the minimal interface must respect, never as positive evidence. No claim of an established/real detectable Born-rule deviation.
- **Tenet 3 (Bidirectional Interaction):** CLEAN. Every epiphenomenalism/causal-inertness mention is critical engagement, hypothetical framing, or attributed to other theories. [concepts/ensemble-level-epiphenomenalism.md](/concepts/ensemble-level-epiphenomenalism/) and [concepts/ai-epiphenomenalism.md](/concepts/ai-epiphenomenalism/) (titles notwithstanding) each explicitly reaffirm the interactionist tenet.
- **Tenet 4 (No Many Worlds):** CLEAN. Every MWI engagement is the Map's voice rejecting it via the indexical-identity argument. The corpus is notably careful to distinguish a tenet-level framework-boundary commitment from an in-framework refutation ("honestly noted as such, not a refutation on MWI's own terms").
- **Tenet 5 (Occam's Razor Has Limits):** Strikingly clean overall (showcase article: [topics/parsimony-case-for-interactionist-dualism.md](/topics/parsimony-case-for-interactionist-dualism/)), with the three minor self-binding lapses below.

## Errors

None.

## Warnings

### concepts/epiphenomenalism.md
- **Tenet involved**: Occam's Razor Has Limits (Tenet 5, internal self-binding)
- **Issue**: The Map's own voice asserts its framework is "simpler" as a point in its favour, and the file contains **no Occam/parsimony self-binding caveat anywhere** (grep confirms zero occurrences of "occam"/"parsimony"). It is an explanatory-economy / "avoid the coincidence" argument, defensible on its merits, but it leans on simplicity-as-virtue for the Map's side without the symmetric flag the tenet demands.
- **Quote** (line 137): "The interactionist explanation is simpler: consciousness is distributed where it is because it *does* something."
- **Recommendation**: Reframe as explanatory adequacy ("avoids treating the consciousness-fitness correlation as a brute coincidence") rather than "simpler," or add a one-clause Tenet-5 self-binding note.

## Notes

### concepts/bidirectional-interaction.md
- **Tenet involved**: Occam's Razor Has Limits (Tenet 5, internal self-binding)
- **Issue**: The same shared evolutionary argument as `epiphenomenalism.md`; "simpler" used as a virtue for the Map's view, with no parsimony self-binding in the file. Borderline — the work is really explanatory (avoiding a coincidence), but the word "simpler" invites the asymmetry.
- **Quote** (line 116): "The interactionist alternative offers a simpler explanation: consciousness evolved *because* it influences behaviour."
- **Recommendation**: Same as above — reframe as explanatory adequacy or add a self-binding clause.

### concepts/spontaneous-intentional-action.md
- **Tenet involved**: Occam's Razor Has Limits (Tenet 5, internal self-binding)
- **Issue**: A locally-unhedged "simpler" phrasing. Lower priority than the two above because the article's dedicated Occam tenet section (line 138) explicitly disarms parsimony ("The 'simpler' account may be simpler only because it ignores the data") — the article is symmetric overall; only the line-132 phrasing reads as unguarded in isolation.
- **Quote** (line 132): "The Map's framework provides a simpler explanation: consciousness selects, and sometimes selects immediately."
- **Recommendation**: Optionally soften the line-132 phrasing to match the article's own line-138 discipline; low priority.

## Methodological note

[topics/parsimony-case-for-interactionist-dualism.md](/topics/parsimony-case-for-interactionist-dualism/) is the tenet's showcase and needs no change: despite a title and frontmatter `description` that read like an asymmetry violation ("Interactionist dualism may be simpler than physicalism"), the body is a model of correct self-binding ("The Map does not endorse the inference *simpler-therefore-truer* here... self-binding applies to parsimony arguments *for* dualism exactly as it applies to those *against* it"). The one place the unqualified "simpler" claim survives is the frontmatter `description` meta field — a reader/LLM ingesting only the meta description gets the asymmetric claim without the disarming. Minor; noted for completeness, not actioned here.

## Files Passing All Checks

All 535 checked files pass at the ERROR level. The three files listed under Warnings/Notes pass at the ERROR level and carry only minor self-binding-phrasing flags for human review.