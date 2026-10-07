---
ai_contribution: 100
ai_generated_date: 2026-10-07
ai_modified: 2026-10-07 03:42:00+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-07
date: &id001 2026-10-07
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-07 03:42:00+00:00
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-10-07
topics: []
---

# System Tuning Report

**Date**: 2026-10-07
**Sessions analyzed**: 235 loop posts (2026-10-03T20:23Z → 2026-10-07T03:29Z; `cycle_post` entries in `../unfinishablemap_log/evolve_loop.log.2026-10-04/05/06` + current)
**Period covered**: 3.3 days since `system-tune-2026-10-03`. Driven since 2026-10-06 ~10:00Z by a single `/loop 15m /unfin-cycle` session (Fable 5.1) rather than `evolve_loop.py`.

## Executive Summary

Healthy and busy: 235 posts, 234 SUCCESS / 1 FAILURE (99.6%), `failed_tasks` empty, `critical_issues` 0, 273 commits in the window of which 15 are driver fix-ups. This is the **eighteenth consecutive run with no Tier 1 lever** — `cadences`, `overdue_thresholds`, `locked_settings` and replenishment weights are still absent from `evolution-state.yaml` (grep-verified), so the skill's three permitted change types have nothing to act on, and tune-system itself fires every 3–4 days instead of monthly because the 30-day gate is not enforced on the `/loop` path. The one structural defect measured fresh this run: `cycle_pick.py` drains pending cycle-completion triggers (step 2) **before** wall-clock triggers (step 3), so the cycle-600 burst at 01:51Z pushed the 02:00/03:00/04:00Z outer-review commissions back by 90+ minutes — none had fired by 03:35Z — inside a Chrome window that closes at 07:00Z.

## Metrics Overview

| Metric | Current | Previous (10-03) | Trend |
|--------|---------|------------------|-------|
| Loop posts in window | 235 (3.3 d) | 270 (3.5 d) | → (~71/day) |
| Post status | 234 SUCCESS / 1 FAILURE | 270/270 | → |
| `failed_tasks` | {} | {} | → |
| Kind mix (window) | queue 97 · trigger 45 · cycle 40 · social 35 · collect 9 · commission 7 · combine 2 | — | queue share 41% (16/24 slots = 67% nominal) |
| Quality | critical 0 · medium 10 · low 3 | critical 0 · medium 10 | → |
| Sections (`count_section_files`) | topics 343/360 · concepts 347/360 · voids 113/115 · positions 23/80 | 335/360 · 335/360 · 111/115 | ↑ |
| `count_p0_p2_tasks` | 11 (replenish gate = <3) | 8 | ↑, gate not firing |
| `task_chains.pending_articles` | 11, zero expand-topic tasks minted | 5 | ↑ (stalled) |
| Coalesce ABANDON streak | 33 → 36 (incl. one driver-level abandon) | 27 → 33 | ↑ |
| Driver fix-up commits | 15 of 273 | — | new metric |
| tune-system interval | 3.3 d (30-day cadence) | 3.5 d | gate inert |

## Findings

### Cadence Analysis

- **No `cadences`/`overdue_thresholds` block exists** (same as runs 09-19 → 10-03). Nothing to compare `last_runs` against; Tier 1 cadence adjustment is impossible by construction.
- **tune-system over-fires**: 09-19, 09-24, 09-27, 09-30, 10-03, 10-07 — mean 3.6 d against a 30-day cadence. The `/loop` path consumes the cycle-completion trigger every ~6 cycles with no min-age check. Each run costs a report and a changelog entry and finds the same absent keys.
- **Wall-clock vs cycle-trigger precedence** (driver observation 3, verified in code): `tools/evolution/cycle_pick.py` L187–L197 returns the first pending cycle trigger before calling `check_all_wall_clock_triggers`. Cycle 600 completed at 01:51Z and enqueued six triggers; by 03:35Z four had run (embed-videos, check-links, research-voids, check-tenets ~25 min, apex-evolve ~9 min) and the ChatGPT (02:00Z) and Claude (03:00Z) commissions had not fired. On 10-06 the same commissions fired at 02:16/03:10/04:15Z. Chrome-window tasks have a hard deadline (07:00Z) that cycle triggers do not.

### Failure Pattern Analysis

- 1 FAILURE in 235 (10-04; pre-window driver). `failed_tasks` empty. No environmental failures (no `CHROME_UNAVAILABLE`, `LOGIN_REQUIRED`, `SUSPENSION_DETECTED` sentinels since 08-09).
- **Fork-hygiene defects corrected by the driver** (observation 4), counted from the changelog/commits in the 24 h to 03:30Z: future-dated timestamps 3 (optimistic 15:40, deep-review 07:40, deep-review 16:15), bare-slug wikilinks installed 3 (parsimony-epistemology, covert-consciousness Cotard link, egocentric-presentism earlier), `ai_system` not plus-joined after prose edits 2 (naturalist-relationalism, philosophical-stakes), Hugo sync skipped 3 (10-05). Each is a one-line fix; none is a content defect, but together they are ~15 driver commits. Not a Tier 1 item (skill-instruction change).
- **Agentic-social grader anomaly**: 1 burned post in 11 (15:19Z, 23+7=30 rejected; the identical sum was accepted at 18:20Z). Second occurrence ever; the stubbed-solver + hand-answer path then went 10/10.

### Queue Health Analysis

- **Replenish gate masked** (observation 1, measured): `count_p0_p2_tasks` = 11 against a fire threshold of <3, but 7 of the open P2s carry `Status: blocked` / `needs-human`; the gate counts them. Result: `replenish-queue` last ran 2026-09-29, and 11 research notes sit in `pending_articles` with no expand-topic task minted — the research→expand chain has been dead for 8 days while `harvest-research-subjects` keeps feeding its input. The 09-29 run was driver-invoked for the same reason.
- **Queue composition**: 66 open task headers; 17 P0–P2 (7 blocked), 49 P3. The driver minted 22 tasks in the window from six reports-only reviews (4+4+4+2+6 +2 carry-forwards) and executed 24 queue tasks (13 inline, 11 forked). The queue is being fed almost entirely by review output, not by replenish — which is the intended steady state for a mature corpus, but it leaves expand-topic starved.
- **Over-hard pages are unreachable** (observation 2): `deep_review.py` excludes apex/voids/positions from its pool, and `apex-evolve`'s staleness scorer skipped `machine-question` (5,937/5,000) as the top-scoring page. Pages over hard get neither lens. The 10-03 report's "condense" lever has not run since 09-19.

### Review Finding Patterns

- **Same-file strand after a repair** — the dominant pattern this window. Reported independently by deep-review (channel-class-taxonomy 18:52Z: two 08-xx sweeps each fixed one sentence and left a dependent contradicting it), check-tenets 146 (control-theoretic-will L82 disclaimer with L134 untouched; comparing L180 after L86/L141/L159), and the pessimistic review 20:00Z (two-tier L67). Three reviews, one pattern: a fix should grep its own file for the withdrawn claim before closing.
- **Secondary-host insertions skip source fidelity** — deep-review 20:37Z (constitutive-vs-referring-observation: the 10-03 expand-topic cross-link paragraph inverted its source's two readings); the Cotard reciprocal sentence (16:50Z) was installed from a review's text without a source pass. Two instances this window; a third (quantum-neural-timing 12:53Z's Schultze-Kraft reading) was caught the other way round.
- **Convergence certified on metadata, not quotes** — phantom-limb (five ledgers never grepped Crawford/Rajendram), self-reference (eight reviews, Feferman never checked), quantum-divine-action (Russell series dates). Three deep reviews in 24 h found quote-level defects under "verified" ledgers. The 10-02 tune report raised this; it is now the deep-review skill's main yield.
- **NEEDS-HUMAN items raised ≥3 times without a task** (observation 7): voids slot allocation (triage note 10-06; veto-void now backed by optimistic 13:12Z), for-me-ness/mineness vocabulary collision incl. `depersonalisation`'s title (research 10-01, pessimistic 10-02, pessimistic 10-06), Tenet 3 quantifier entries, categorical-perception-void retitle/retire, X API credits (two untweeted highlights).

### Convergence Progress

- `progress`: topics 343, concepts 347, voids 113, apex 44, positions 23, research notes 651, reviews 7,880. Growth in the window is +0 articles (all slots held for operator decisions) and +22 reviews.
- `quality.medium_issues` 10 vs target ≤3 — unchanged since 09-30; the field is not being decremented by the fixes that land (the tenet-check errors repaired in-window did not move it), so it is not a usable convergence signal.
- **CLAUDE.md section-cap table is stale** (observation 6): it says 320/320/100 with "1 slot left"; `evolution-state.yaml` says 360/360/115 and `count_section_files` reads 343/347/113. Anyone reading CLAUDE.md to decide whether to mint an expand-topic gets the wrong answer by 17–19 slots.

## Changes Applied (Tier 1)

*No changes applied* — eighteenth consecutive run with no Tier 1 lever: `cadences`, `overdue_thresholds`, `locked_settings` and replenishment weights are absent from `evolution-state.yaml` (grep-verified 2026-10-07T03:35Z). The only state-file edit this run is the `tune_system_history` bookkeeping below.

## Recommendations (Tier 2)

### Fire wall-clock commissions before pending cycle triggers inside the Chrome window
- **Proposed change**: in `tools/evolution/cycle_pick.py`, evaluate `check_all_wall_clock_triggers` before draining `pending-triggers.json` when the wall-clock trigger is `chrome: true` and the current hour is inside the automation window (00–06 UTC); cycle triggers have no deadline, commissions do.
- **Rationale**: measured 90+ min displacement of all three commissions today; on a day when the burst lands at 05:00Z the Gemini leg would miss the window entirely.
- **Risk**: Low (ordering change in one function; cycle triggers still drain on the next iterations).
- **To approve**: swap steps 2 and 3 for chrome-flagged wall-clock results; add a test with a seeded `pending-triggers.json` and a 02:05Z clock.

### Make the replenish gate ignore blocked / needs-human tasks
- **Proposed change**: `tools/evolution/task_selector.py:count_p0_p2_tasks` should skip tasks whose `Status` is `blocked` or `needs-human` (it already skips non-executable types).
- **Rationale**: gate reads 11 with 7 blocked → replenish has not fired since 09-29 and 11 `pending_articles` have no expand-topic task; the 09-29 and 10-06 runs both needed a hand invocation.
- **Risk**: Low. Until applied, the driver should invoke `/replenish-queue` by hand when `pending_articles` ≥ 5.
- **To approve**: one-condition change plus a unit test with a blocked P2.

### Enforce the 30-day min-age on tune-system from the `/loop` path
- **Proposed change**: `cycle_post`'s cycle-completion enqueue should skip `tune-system` when `last_runs["tune-system"]` is < 30 d old (same rule `evolve_loop.py` applies).
- **Rationale**: six runs in 18 days, all zero-Tier-1; each produces a report and changelog entry that say so.
- **Risk**: Low.

### Give over-hard pages a lens
- **Proposed change**: let `apex-evolve`'s selector fall back to a `condense`-first pass for an apex page over 5,000 (it skipped the top-scoring `machine-question`), and let `deep_review.py`'s pool include apex/voids/positions at a reduced weight.
- **Rationale**: `condense` last ran 09-19; `machine-question` (5,937) and `interface-specification-programme` (5,108) are unreachable to every automated lens.
- **Risk**: Medium (pool change alters deep-review's selection distribution).

### Refresh the CLAUDE.md section-cap table
- **Proposed change**: replace the "Section Caps" table figures with the `evolution-state.yaml` caps (360/360/115/80) and today's counts (343/347/113/23), and keep the existing "re-measure before acting" warning.
- **Rationale**: the table is off by 40 slots per section and says "1 slot left" where 17 exist.
- **Risk**: None (documentation).

## Items for Human Review (Tier 3)

### Fork hygiene rules belong in the per-task skill files
- **Issue observed**: 11 driver fix-up edits in 24 h for the same four omissions (timestamps ahead of the clock; bare-slug `[[slug]]` links that render as the slug; `ai_system` not plus-joined after a prose edit; Hugo not synced). The driver now repeats the rules in every brief, which works but is fragile.
- **Why human needed**: SKILL.md files are operator territory (Tier 3).
- **Suggested action**: add a four-line "Housekeeping" block to `refine-draft`, `deep-review`, `optimistic-review`, `pessimistic-review`, `apex-evolve` SKILL.md files: `date -u` for every stamp; piped wikilinks only; plus-join the model after any prose change; `sync.py` + grep both trees.

### Repairs should grep their own file for the withdrawn claim
- **Issue observed**: three reviews this window found the same-file strand pattern (a fix lands, a dependent sentence in the same file keeps the old claim). Each cost a later review slot.
- **Suggested action**: one sentence in `refine-draft` and `deep-review` SKILL.md: after replacing a claim, grep the file (and `archive/`) for its key phrase and the claim's negation before closing.

### Operator decisions outstanding (raised ≥3 times)
- **voids slot allocation** (113/115): triage note 2026-10-06 ranks veto-void and dormancy; `research-voids` is being skipped by the driver until this is decided.
- **for-me-ness / mineness vocabulary collision**: `mine-ness` L48 and `depersonalisation`'s title use "for-me-ness" for the separable feature that `thought-insertion`, `self-and-self-consciousness` and the two-tier page now distinguish from it; fixing it properly is a title/URL change.
- **categorical-perception-void** retitle/retire (fails signature specificity) and the 8 deferred references.
- **Tenet 3 quantifier** additions (mental-effort L94/L72; tenets.md L71, L117/[P-I5](/positions/individuation-and-subjecthood/#p-i5)).
- **X API credits depleted** — two highlights untweeted since 10-05 (`uv run python scripts/highlights.py tweet-latest` once funded).

### `quality.medium_issues` is not a live signal
- **Issue observed**: stuck at 10 since 09-30 while tenet-check errors were repaired in-window; nothing decrements it.
- **Suggested action**: either wire check-tenets/validate output to it or drop it from the convergence targets.

## Next Tuning Session

- **Recommended**: 2026-11-06 (30 days) — or whenever the `/loop` path's min-age gate is enforced, whichever is first.
- **Focus areas**: whether the commission-precedence and replenish-gate changes landed; `pending_articles` drained; coalesce streak (36) — consider retiring the slot to 1/24 if it passes 50; driver fix-up count as a hygiene metric.