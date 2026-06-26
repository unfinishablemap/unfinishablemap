---
title: "Deep Review - AI Automation System"
created: 2026-06-26
modified: 2026-06-26
human_modified: null
ai_modified: 2026-06-26T17:33:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[automation]]"
  - "[[closed-loop-opportunity-execution]]"
  - "[[bedrock-clash-vs-absorption]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-26
last_curated: null
---

**Date**: 2026-06-26
**Article**: [[automation|AI Automation System]]
**Previous review**: [[deep-review-2026-04-29-automation|2026-04-29]]

This is a system-documentation article, so the review is primarily a **fact-check against the live codebase** rather than a philosophical critique. Every quantitative claim was verified against source files (`tools/evolution/cycle.py`, `tools/evolution/cycle_pick.py`, `tools/evolution/time_trigger.py`, `tools/chrome_session.py`, the live `obsidian/reviews/outer-review-*` filenames, and the `.claude/skills/*` definitions). No external bibliographic citations are present, so §2.4 publisher-of-record web-verify does not apply. No named-opponent replies, so §2.6 reasoning-mode classification does not apply.

## Pessimistic Analysis Summary

### Critical Issues Found (factual drift)

- **Stale slot ratios (3 in-article locations + 1 sibling).** The article claimed Queue 16/24 and Coalesce 2/24 ("16:4:1:1:2 slot ratio"). The live `tools/evolution/cycle.py` has been **17:4:1:1:1** since tune-system 2026-04-29b cut the second coalesce slot (position 21) to a queue slot (voids/ post-saturation; six consecutive coalesce abandonments). Verified via `Counter(TASK_CYCLE)`: queue 17, deep-review 4, pessimistic 1, optimistic 1, coalesce 1. **Resolved** — updated the lead, the Mermaid diagram (16/24→17/24, 2/24→1/24 coalesce), the Task Queue section ("16 of every 24"→"17 of every 24"), and the methodology-disciplines "16:4:1:1:2"→"17:4:1:1:1" with the ratio key spelled out. The prior 2026-04-29 review *introduced* the 16/2 numbers on the same day the code changed, so this is drift the prior review could not have caught.
- **Stale Claude outer-review model.** The External Outer Reviews table listed Claude as "Opus 4.7 Adaptive". The live system runs **Fable 5 when available, else Opus 4.8 fallback** (CLAUDE.md time-triggered section; live review filenames are `claude-opus-4-8`, e.g. `outer-review-2026-06-26-claude-opus-4-8.md`). **Resolved** — updated to "Fable 5 (Opus 4.8 fallback)" and noted the self-healing across claude.ai "Fable 5 unavailable" episodes.

### Medium Issues Found

- **Optimistic Supporters table missing the 7th persona.** `/optimistic-review` and `/deep-review` now use seven sympathetic personas; the table listed only six, omitting **Jonathan Birch (Hardline Empiricist)** — the deliberate counterweight to the Process Philosopher against evidential-status slippage (confirmed in `.claude/skills/optimistic-review/SKILL.md`). **Resolved** — added the row plus a one-paragraph explanation of the productive Whitehead/Birch tension.
- **embed-videos cycle trigger omitted.** The lead said "five cycle-trigger cadences (links, tenets, research, apex synthesis, system tuning)" and the diagram listed the same five, both omitting **embed-videos** (the every-cycle trigger, `CYCLE_TRIGGERS["embed-videos"]=1`). **Resolved** — added embed-videos to the lead list and the diagram trigger box; reworded "five" to a non-counting phrasing so the list is no longer falsified by its own length.

### Items Verified Correct (no change needed)

- `MIN_QUEUE_TASKS = 3` — confirmed in both `cycle_pick.py:62` and `evolve_loop.py:82`.
- `fcntl` cross-repo lock — confirmed `fcntl.flock` at `~/unfin/chrome-profiles/.automation.lock` in `tools/chrome_session.py`.
- Chrome window "(00:00–07:00 UTC)" — `time_trigger.py` gates on `0 <= hour < 7`, so the half-open interval is correct; CLAUDE.md's 07:00–07:59 "buffer" is a finer distinction left out as a reasonable simplification (low priority, not changed).
- ChatGPT 5.5 Pro Extended 02:00 / Gemini 2.5 Pro 04:00 — match CLAUDE.md and live filenames.
- The 2026-05-03 (ChatGPT) and 2026-05-04 (ChatGPT, Claude) convergence claim — the cited review files all exist; the 2026-05-04 Claude leg was genuinely `claude-opus-4-7` at that historical date, so the historical reference is accurate (distinct from the *current*-model table fix above).
- All 14 wikilink targets resolve by basename (`coalesce-condense-apex-stability` lives in `concepts/`, not `project/`, but resolves).
- `scripts/run_workflow.py` exists, so the "Running Locally" command is valid.

### Counterarguments Considered

- **"evolve_loop.py is named as 'the main orchestrator' but the live path is `/loop unfin-cycle` + `cycle_post.py`."** `scripts/evolve_loop.py` still exists and remains a valid legacy orchestrator; CLAUDE.md documents both. The article's framing is dated but not false. Left as-is to avoid scope creep into the loop-vs-evolve_loop architecture question, which is a system-level documentation decision better handled by a deliberate refresh of both this page and CLAUDE.md together. Logged under Remaining Items.

## Optimistic Analysis Summary

### Strengths Preserved

- The Mermaid Human → Cycle → Triggers → Output topology — labels corrected, structure preserved.
- The two persona tables as a clean communication of the review architecture — pessimistic table kept verbatim (it is complete at six); optimistic table extended, not rewritten.
- The Methodology Disciplines section as first-class hub content — preserved (prior review's stability note honoured).
- Running Locally, Technical Details, Safety Mechanisms, Convergence Goal, Relation to Site Perspective — preserved verbatim.

### Enhancements Made

- Slot ratios corrected and the ratio key (queue : deep-review : pessimistic : optimistic : coalesce) spelled out in the disciplines section for self-documentation.
- Optimistic table now communicates the calibration-discipline tension (Process Philosopher vs Hardline Empiricist) that the rest of the corpus depends on.

### Cross-links Added

- None new (the article already links its full discipline cluster); existing links re-verified as resolving.

## Remaining Items

- **Sibling drift**: `obsidian/project/closed-loop-opportunity-execution.md` still states the stale "16:4:1:1:2 slot ratio". Out of scope for this single-file review; a P2 refine-draft follow-up has been queued.
- **evolve_loop vs /loop unfin-cycle framing**: the article names `scripts/evolve_loop.py` as the main orchestrator while the live driver is `/loop` + `unfin-cycle` + `cycle_post.py`. A deliberate joint refresh of automation.md + CLAUDE.md is the right vehicle; not done here to avoid a half-migration. Noted for a future human-steered pass.

## Stability Notes

- The prior review's two stability notes hold: (a) "AI-generated content is published directly" vs CLAUDE.md's "created as drafts" reflects an intent/implementation gap, not a contradiction to re-flag; (b) surfacing methodology disciplines as first-class hub content is deliberate, not inflation.
- The slot-ratio numbers are a recurring drift surface: they live in code (`cycle.py`), this article, CLAUDE.md, and `closed-loop-opportunity-execution.md`. Any future tune-system change to `TASK_CYCLE` must touch all four. This review aligned this article to code; CLAUDE.md ("Coalesce: 2 slots") and the sibling concept page remain stale and are the natural next sweep.
- No bedrock philosophical disagreements arose — this is documentation, and every finding was a verifiable code-fact, not a framework-boundary clash.
