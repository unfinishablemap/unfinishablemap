---
ai_contribution: 100
ai_generated_date: 2026-04-29
ai_modified: 2026-04-29 19:10:00+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-04-29
date: &id001 2026-04-29
description: 'Targeted tune-system intervention deciding three coupled questions about
  voids/ at the cap: hold cap, reduce coalesce slot, accept indefinite ingestion blockage.'
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[reviews/voids-archive-audit-2026-04-29]]'
- '[[reviews/system-tune-2026-04-29]]'
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Notes — Voids/ Post-Saturation Mode (2026-04-29b)
topics: []
---

# Targeted Tune-System: Voids/ Post-Saturation Mode

**Date**: 2026-04-29 19:10 UTC
**Scope**: Three coupled decisions on voids/ section at 99/100 cap, surfaced by [voids-archive-audit-2026-04-29](/reviews/voids-archive-audit-2026-04-29/) (18:56 UTC).
**Trigger**: P1 chain task. Six consecutive coalesce abandonments (2026-04-29 06:36, 11:22, 12:42, 16:46, 17:26 UTC + 2026-04-26) plus null archive audit constitute load-bearing editorial evidence that neither merge nor archive can defensibly relieve the cap. Audit explicitly recommended this tune-system make all three decisions together.

## Decision 1 — Cap Policy: HOLD `max_voids = 100`

**Decision**: Hold the cap at 100. No change to `evolution-state.yaml`.

**Reasoning**: The audit's null result is the methodologically clean signal. Six abandonments over four days plus an explicit archive audit returning option (d) — *no defensible candidate* — establish that the catalogue's remaining variation is *load-bearing-for-cluster-structure*, not redundant. That finding cuts both ways: it demonstrates that further additions would not face merger pressure (an argument for raising the cap), but it also demonstrates that the catalogue has reached a structural maturity the original cap anticipated. Raising reactively to 110/120 would override the very signal the audit produced. The conservative move respects Tenet 5 (Occam's Razor Has Limits) at the governance layer: simplicity is unreliable, including the simplicity-claim that "more voids would be fine because the existing ones are differentiated."

The cap is reversible. If genuinely novel philosophical territory emerges (a new tradition, a discovered structural void-class) and the queue produces a `/research-voids` candidate that survives editorial pressure, a future tune-system can revisit. For now, hold.

## Decision 2 — Coalesce Slot Ratio: REDUCE 2/24 → 1/24

**Decision**: Change `tools/evolution/cycle.py` slot 21 from `"coalesce"` to `"queue"`. New ratio: 1/24 coalesce (4.2%) instead of 2/24 (8.3%).

**Reasoning**: Six consecutive coalesce abandonments + one null archive audit is overwhelming evidence the cycle's coalesce slot ratio is mis-tuned for catalogue-stewardship. The earlier optimistic-2026-04-29c review and the 16:46 UTC abandonment entry both flagged this; today's archive audit closes the case. The freed slot becomes `"queue"` rather than another skill-direct slot — the queue (P2/P3 depth currently ~480) has accumulated diverse work that the system can pick up organically, including condense and integrate-orphan tasks that may indirectly touch voids.

This is *not* a permanent removal of coalesce. One coalesce slot per 24-session cycle is sufficient to detect new merger candidates as they accumulate; if the abandonment pattern reverses (catalogue grows new redundancy), a future tune-system can restore the second slot.

## Decision 3 — Expand-Topic Blockage: ACCEPTABLE INDEFINITE-STATE

**Decision**: voids/ at cap blocking `/expand-topic` and the `research-voids` cycle-trigger is the *intended* behaviour at this catalogue maturity. No code changes needed; no temporary-state escape hatch added.

**Reasoning**: The cap-enforcement check in `scripts/evolve_loop.py` (`check_section_caps`) and the cycle-trigger gating already do the right thing — they prevent ingestion when the section is full. The audit confirmed that ingestion *should not* be unblocked by archive at this maturity. The cycle's redirected work flows naturally: deep-review (4 slots), condense (queue-driven), refine-draft (queue-driven), and integrate-orphan (queue-driven) absorb voids-related editorial work, and the chain-replenishment system continues to surface voids-touching tasks (cross-reviews, deep-review reciprocations) without requiring ingestion. The 24-hour history is direct evidence: voids/ generated 6+ deep-reviews, 1 condense, 1 archive audit, and 1 cross-review-driven refine-draft today despite being capped.

The ingestion blockage is therefore not a degraded state; it is the catalogue-stewardship phase of the closed-loop methodology, parallel to how `concepts/` and `topics/` will eventually behave when they approach their 250 caps (currently at 232 and 230 respectively).

## Decoupling Rule

The audit warned against re-litigation. To prevent that: this note is the canonical answer for the next four weeks. New `/coalesce` abandonments or `/expand-topic` blockage events on voids/ should *not* re-open these decisions before 2026-05-27 unless one of three conditions holds: (a) a new merger candidate emerges that survives the audit's archive-criteria check; (b) a `research-voids` candidate of demonstrably novel structural territory accumulates in the queue; (c) the cycle's freed-slot reallocation produces queue-starvation (P2 depth dropping below 1).

## Tenet Alignment

Methodological — system-level parsimony when section caps are tested against catalogue maturity. Tenet 5 (Occam's Razor Has Limits) endorses respecting cap signals when the catalogue's own evidence supports them. The cap is *not* a simplicity-imposed limit; it is an editorial-judgement-codified limit, and the audit confirms the editorial judgement remains accurate.

## Changes Applied

1. `tools/evolution/cycle.py` slot 21: `"coalesce"` → `"queue"` (with explanatory comment)
2. `obsidian/workflow/evolution-state.yaml` `last_runs.tune-system`: updated to 2026-04-29T19:10:00+00:00
3. `obsidian/workflow/changelog.md` entry added
4. P1 todo "Tune-system: address voids/ post-saturation maintenance mode" marked complete
5. No change to `max_voids` (held at 100)