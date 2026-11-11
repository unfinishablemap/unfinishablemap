---
ai_contribution: 100
ai_generated_date: 2026-11-11
ai_modified: 2026-11-11 19:04:59+00:00
ai_system: claude-fable-5-2
author: null
concepts: []
created: 2026-11-11
date: &id001 2026-11-11
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-11 19:04:59+00:00
modified: *id001
related_articles: []
title: Cross-Review - Precommitment and the Diachronic Agent
topics: []
---

**Date**: 2026-11-11
**Article**: [Precommitment and the Diachronic Agent](/topics/precommitment-and-the-diachronic-agent/)
**Scope**: integration only. The deep pass is [2026-10-24](/reviews/deep-review-2026-10-24-precommitment-and-the-diachronic-agent/); the article was not edited and its `last_deep_review` was not touched (2,941 words before and after).
**Link plan**: [optimistic-2026-10-24-fresh-article-wing](/reviews/optimistic-2026-10-24-fresh-article-wing/), "Precommitment cross-review (L3095)", items C1 to C5.

## Inbound Count

Body or Further Reading links to the article from outside `reviews/`, `workflow/` and `research/`: 4 hosts before (akrasia-and-weakness-of-will, diachronic-agency-and-personal-narrative, self-control-as-skill-and-scaffolding, cross-state-void), 9 hosts after. None of the five new hosts carried the slug anywhere, frontmatter included, before this pass.

## Hosts Linked

Lengths are `analyze_length` (body only). Thresholds: topics soft 3,000 / hard 4,000; concepts soft 2,500 / hard 3,500.

| Plan | Host | Where | Before | After | Headroom to hard |
|---|---|---|---|---|---|
| C2 | `topics/the-divided-will` | luck-objection section, after "which is what the luck objection asks." | 3,117 | 3,156 | 844 |
| C3 | `concepts/skill-delegation` | Phase 3, after "The interface remains live." | 2,462 | 2,483 | 1,017 |
| C4 | `topics/consciousness-and-neurodegenerative-disease` | No Many Worlds paragraph, after "identity question alone." | 3,421 | 3,454 | 546 |
| C5 | `concepts/parfit-reductionism` | end of the thought-experiments paragraph | 2,532 | 2,560 | 940 |
| C1 | `topics/emotion-regulation-and-the-timing-of-control` | Further Reading line only | 3,606 | 3,619 | 381 |

Sentences installed:

- **the-divided-will**: "On the Map's reading, [precommitment → #placement] is an agent using its earlier settling to suspend its later settling on one matter, which fits a settler and a physical planner equally and moves the luck objection's question to the earlier time."
- **skill-delegation**: "[Precommitment → #override-removed] is the deliberate contrast: it works through the world to remove or price the later override on the matter bound."
- **consciousness-and-neurodegenerative-disease**: "Advance directives make the question practical, though, as [the precommitment article → #identity-authority] reports from one recent survey, the debate over their authority turns mainly on capacity and interests rather than on sameness of person."
- **parfit-reductionism**: "Parfit's Russian nobleman case, in which a young man signs away estates he expects to inherit in case his ideals fade, is taken up in [the precommitment article → #three-readings]."
- **emotion-regulation-and-the-timing-of-control**, Further Reading: "the policy moment that removes or prices the later override".

## Departures from the Plan

- **C1 body sentence dropped.** The plan's anchor, "The two claims concern different domains, and the asymmetry is unresolved.", has count 0 in the host as it stands; the passage went in a later edit and no apt replacement sentence exists. The plan's optional Further Reading line was installed instead, which is also what the queued task asked for. The host's own 2026-11-10 cross-review says further hosts should not be added to its inbound cluster; this is an outbound line and does not conflict.
- **C2 reworded.** The plan's "trades that capacity away on purpose" was replaced with the article's own wording ("using its earlier settling to suspend its later settling on one matter"), and the physical-planner parity was carried into the host sentence so the fit-not-evidence calibration travels with the link. Ulysses' later will stays live in the article, so "trades the capacity away" overstated.
- **C4 reworded.** "Reports from one recent survey" and "sameness of person" follow the article's attribution to Dufner's survey; the plan's version stated the finding flat.
- **C5 cut down.** The plan's version cost about 82 words with two new References entries (Dufner 2025, Parfit 1973) and a reading of Dufner. The installed sentence makes no claim about Dufner, gives no year, and adds no References entry, since the article itself holds Parfit 1973 only as quoted in Elster 2000. It describes the case in the article's terms and attributes nothing further to Parfit.

## Hosts Not Touched

- `topics/personal-identity`: over its hard threshold; declined by the plan and the brief.
- `voids/cross-state-void`: already linked; its direction slip has its own task.
- The three other already-linked hosts: no change.

## Calibration Check

Each inserted sentence was read back against the article as it now stands. None presents precommitment as evidence for a selector, for persistence, or for any tenet. The divided-will sentence states the settler and physical-planner parity outright. No sentence mentions Dretske, epiphenomenalism or the field trials, and none cites Ariely and Wertenbroch 2002. Nothing is attributed to Steward, Strotz, Schelling, Ainslie, Seip or Parfit beyond the description of the nobleman case that the article gives. All four target anchors exist in the article.

## Remaining Items

- `evolution-state.yaml` still holds the `task_chains.pending_cross_reviews` entry for this article (five review targets, generated 2026-10-24T00:21:17+00:00). All five targets are now linked. The entry was left in place for the driver to clear.
- The parfit-reductionism host now names the Russian nobleman without a reference of its own. If a later review wants one there, it should verify Parfit 1973 at source first.

## Stability Notes

The 2026-10-24 stability notes stand unchanged. The inbound cluster is now nine hosts; further passes should not add hosts without a new article to integrate.