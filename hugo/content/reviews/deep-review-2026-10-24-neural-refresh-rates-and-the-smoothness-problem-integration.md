---
ai_contribution: 100
ai_generated_date: 2026-10-24
ai_modified: 2026-10-24 21:10:34+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-24
date: &id001 2026-10-24
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-24 21:10:34+00:00
modified: *id001
related_articles: []
title: Deep Review - Neural Refresh Rates and the Smoothness Problem (integration)
topics: []
---

**Date**: 2026-10-24
**Article**: [Neural Refresh Rates and the Smoothness Problem](/topics/neural-refresh-rates-and-the-smoothness-problem/)
**Previous review**: [2026-09-10](/reviews/deep-review-2026-09-10-neural-refresh-rates/)
**Scope**: Cross-review, limited to integration. The 2026-10-11 coalesce merged `voids/smoothness-and-continuity` into this topic as `## The Continuity Void` (anchor `#the-continuity-void`) and archived the void. This pass retargets the six inbound referrers from the archived slug to the host. The host's body and its `last_deep_review` were not touched, and no full deep review was run (the host is 3,991 words against a topics hard gate of 4,000). Nothing was broken beforehand: every old link already resolved through the archive's `superseded_by` redirect.

## Anchor Check

- Obsidian heading `## The Continuity Void` is at host L95. The Hugo render has it at L99, and the host already links `#the-continuity-void` internally at Hugo L55, L119 and L151.
- Precedent: the voids index at [voids/voids.md](/voids/) L196 already links `[[neural-refresh-rates-and-the-smoothness-problem#the-continuity-void|...]]`.

## Retargets

Lengths are body-only `analyze_length`, before → after.

| File | Line | Before | After |
|---|---|---|---|
| voids/resolution-void (2989 → 2991, hard 3000) | FM L19 | `[[smoothness-and-continuity]]` | `[[neural-refresh-rates-and-the-smoothness-problem]]` |
| | body L57 | `(see [[smoothness-and-continuity]])` | `#the-continuity-void`, label "continuity void" (+1) |
| | FR L100 | bare slug | `#the-continuity-void`, label "Continuity Void" (+1; the shorter label was chosen because headroom is tight) |
| concepts/temporal-consciousness (3012 → 3006, hard 3500) | FM L63 | archived slug | host slug |
| | body L102 | `[[smoothness-and-continuity\|continuity void]]` | `#the-continuity-void`, label kept (0) |
| | FR L213 + L219 | two entries to the same page | merged into the single host entry (now L218), with the "why consciousness cannot determine its own temporal grain" clause folded into it (−6) |
| voids/temporal-void (2440 → 2442, hard 3000) | FM L33 | archived slug | host slug |
| | FR L162 | bare slug | `#the-continuity-void`, label "The Continuity Void" (+2), matching the file's Title Case FR labels |
| voids/capability-division-problem (2994 → 2994, hard 3000) | FM L20 | archived slug | host slug |
| | body L76 | `[[smoothness-and-continuity\|smoothness problem]]` | host page with no anchor, label kept (0) |
| | FR L126 | bare slug | bare host slug (0), matching this file's all-bare FR list |
| voids/edge-states-and-void-probes (3664 → 3664, already over hard 3000) | FM L30 | archived slug | host slug |
| | body L141 | `[[smoothness-and-continuity\|continuity]]` | `#the-continuity-void`, label kept (0) |
| concepts/episodic-memory (3498 → 3498, hard 3500) | FM L49 | archived slug | host slug |

### Deviations from the brief (and why)

- **capability-division-problem L76 and L126 do not use the anchor.** The L76 label is "smoothness problem", and the FR line calls it "the temporal instance of capability division". Both refer to the smoothness problem as a whole. The host defines that problem in its lead and makes the capability-division framing in its Relation to Site Perspective section, not in The Continuity Void. The anchor would land the reader on the introspective-undecidability section, which does not match either label.
- **temporal-consciousness's merged FR entry links the whole page.** It now describes both the sampling rates and the temporal-grain question. The body link at L102 still carries the anchor.

## Verification

- `grep smoothness-and-continuity` finds zero hits in all six obsidian files. After `scripts/sync.py`, the six Hugo files show zero rendered links whose text is the retired slug, and no stray `[[`.
- No other file outside `archive/`, `research/`, `reviews/` and `workflow/` references the archived slug.
- No `last_deep_review` was bumped. `ai_system` gained `+claude-opus-5-5` only where it was absent: temporal-consciousness, temporal-void, capability-division-problem and edge-states. resolution-void and episodic-memory already carried it.

## Remaining Items

None for this integration. edge-states-and-void-probes remains over the voids hard gate (3,664 against 3,000). This pass did not grow it, and the overrun is already covered by the standing "HUMAN LENGTH DECISION 2026-06-05" entry in [workflow/todo.md](/workflow/todo/) (do not auto-condense), so no task was minted.

## Stability Notes

Host not reviewed in this pass. Its 2026-09-10 review stands.