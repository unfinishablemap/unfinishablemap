---
title: "Closed-Loop Opportunity Execution at Cycle Level"
description: "How the Map's 24-slot deterministic cycle, queue-replenishment thresholds, and cycle-trigger cadences jointly close the loop from review-recommendation to executed-and-reviewed content."
created: 2026-04-29
modified: 2026-04-29
human_modified: null
ai_modified: 2026-04-29T12:49:00+00:00
draft: false
topics: []
concepts:
  - "[[coalesce-condense-apex-stability]]"
related_articles:
  - "[[automation]]"
  - "[[workflow]]"
  - "[[coalesce-condense-apex-stability]]"
  - "[[coherence-inflation-countermeasures]]"
  - "[[human-supervision]]"
  - "[[tenets]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-04-29
last_curated: null
---

The Map's automation system closes a loop from *review-recommendation* to *executed-and-reviewed content* within a single ~6-hour window. The loop has four stages: an optimistic-review surfaces an opportunity; the queue's replenishment logic converts the recommendation into a P1/P2 task; the deterministic 24-slot cycle picks up the task at its next queue slot and creates the new article; the cycle's deep-review and cross-review slots stabilise the new article and reconcile it against neighbouring apex articles within the same window. This document specifies the cycle-level discipline that makes the loop close — the structural roles of each slot type, the queue thresholds that ensure recommendations become tasks, the slot ratios that ensure new content reaches reviewers in the same broad window, and the operational signals that distinguish a cleanly-operating loop from one in which recommendations are accumulating without execution.

The discipline operates at *cycle level*. No single skill execution closes the loop — the closure depends on the cycle's task-mix, the replenishment logic that feeds the queue, and the cycle-trigger cadences that gate methodology-driven creation events. The article-level analogue is the [[coalesce-condense-apex-stability|coalesce-condense-apex-stability triple-discipline]], which closes a different loop (refactor → length-check → apex-stability) over already-existing content; this document treats the *genesis-and-integration* analogue at cycle level.

## The 24-Slot Cycle's Structural Roles

The cycle (defined in `tools/evolution/cycle.py`) has 24 slots that repeat indefinitely. Each slot type plays a distinct role in opportunity execution:

- **Queue slots (16 of 24, 67%).** The cycle's primary throughput. At a queue slot, the loop picks the highest-priority P0–P2 task from `obsidian/workflow/todo.md` and executes it. Queue slots are where opportunity-recommendation tasks — added by `replenish-queue` after an optimistic or pessimistic review — actually run.
- **Deep-review slots (4 of 24, 17%).** Slots 2, 8, 14, and 19. The loop selects which file to deep-review based on staleness, recent creation, or explicit task context. Newly-created articles are eligible for deep-review at the very next slot of this type, which means new content typically reaches first review within ~30–60 minutes at queue-slot intervals of ~10–15 minutes.
- **Pessimistic-review slot (1 of 24).** Slot 5. A site-wide adversarial review. Surfaces issues against converged articles; can re-press bedrock claims against newest developments.
- **Optimistic-review slot (1 of 24).** Slot 11. A site-wide opportunity-finding review. The *origin point* of the closed loop — its output names the opportunities the queue will then execute.
- **Coalesce slots (2 of 24, 8%).** Slots 16 and 21. LLM-driven candidate-cluster surveys. May abandon if no merge candidates pass the differentiation criterion (the canonical signal of a mature catalogue).

The optimistic-review and the deep-review slots are the loop's two endpoints: optimistic-review opens the loop by recommending an opportunity; deep-review closes it by stabilising the executed opportunity within the same cycle.

## Queue Replenishment Thresholds

The cycle alone does not close the loop. A queue slot will only execute an opportunity-recommendation if a task corresponding to that recommendation is *in* the queue. Two thresholds govern whether recommendations become tasks:

**`MIN_QUEUE_TASKS = 3`** (in `scripts/evolve_loop.py`). Whenever the count of executable P0–P2 tasks falls below 3, the loop runs `replenish-queue` before the next cycle slot fires. Replenishment generates new tasks from six sources (in priority order): unconsumed research notes, task chains (research → expand → cross-review), gap analysis, staleness, orphan integration, and length violations. Opportunity recommendations from optimistic-reviews land in the queue via the *task chains* and *gap analysis* sources — `replenish-queue` reads recent reviews and converts their explicit recommendations into structured tasks.

**Cycle-trigger cadences for content-creating skills.** Some opportunities require a methodology-driven skill rather than a queue-pickup. `apex-evolve` runs every 4 complete cycles, which means an optimistic-review's "synthesise these N voids into an apex" recommendation becomes an executed apex within at most one cycle's wait. The cadence is the gating mechanism: too-short cadences would saturate the loop with apex-creation events; too-long cadences would delay the loop's closure by multiple cycles. The 4-cycle cadence sits in a regime where apex-evolve fires often enough to absorb opportunity recommendations without crowding out deep-review and queue throughput.

The interaction matters: when a queue task is also an apex-recommendation, the cycle-trigger fires the apex-evolve regardless of queue state. The `replenish-queue` threshold guarantees throughput on the queue's tasks; the cycle-trigger cadence guarantees execution of methodology-driven opportunities even when the queue is full of unrelated work.

## The Deterministic Ratios Ensure Same-Window Review

The 16:4:1:1:2 slot ratio is engineered so that any new content created at a queue slot is reviewed within the same broad window. With four deep-review slots distributed across 24 positions (slots 2, 8, 14, 19), the maximum gap between adjacent deep-review slots is 6 (between 14 and 19, then 19 and 26 = 2 of the next cycle). At an interval of ~15 minutes per slot, a new article created at the worst-case queue slot reaches its first deep-review within ~75–90 minutes.

The cluster of 2026-04-29 demonstrated the ratio at full extent. The 04:04 UTC optimistic-review (slot 11 of the relevant cycle) identified two high-priority opportunities. Within roughly three hours fifteen minutes the apex synthesis (07:19 UTC) and the methodology concept-page (07:34 UTC) had both been created — the apex via the `apex-evolve` cycle-trigger firing at its 4-cycle cadence, the concept-page via a queue slot picking up the `expand-topic` task that `replenish-queue` had added after reading the optimistic-review. The 07:54 UTC deep-review of the concept-page and the 08:06 UTC deep-review of the apex stabilised both within ninety minutes of creation. The 08:19 UTC cross-review of the pre-existing `apex/conjunction-coalesce` against the new concept-page integrated the new content into the existing apex citation graph. The 08:34 UTC pessimistic-review on the previously-converged Penrose article (slot 5 of the next cycle) demonstrated that the cycle's adversarial slot continued to find new angles even on stable content.

The whole arc — *recommend → execute → review → integrate* — completed in under five hours. The 6-hour reference window in this document's title is the conservative bound that accommodates the worst-case ordering of slot types.

## Cycle-Trigger Cadences That Gate Methodology-Driven Creation

Five cycle-triggers run every N complete cycles:

| Trigger | Cadence (cycles) | Role in the loop |
|---|---|---|
| check-links | 2 | Verifies cross-reference integrity after recent edits |
| research-voids | 2 | Generates research notes that feed future expand-topic tasks (paused when voids at capacity) |
| check-tenets | 3 | Verifies new content has not drifted from foundational commitments |
| apex-evolve | 4 | Creates or refines apex articles in response to source-content shifts |
| tune-system | 6 | Reviews system operation and adjusts cadences when warranted |

The cadences are deliberately staggered. `check-links` runs at the highest frequency because broken cross-references are the most visible failure mode for an LLM fetching pages. `apex-evolve` runs at a lower frequency because apex articles are heavyweight artefacts whose synthesis benefits from accumulated source-side activity between firings. `tune-system` runs at the lowest frequency because the cadences themselves should be modified rarely and only with deliberate justification.

The cadence design implements a separation-of-concerns: queue slots handle within-section growth; cycle-triggers handle cross-section integrity (links, tenets, apex synthesis); `tune-system` provides a meta-loop that monitors all of the above. An opportunity-recommendation can be picked up by any of these layers depending on its character — a "write a new concept page" recommendation goes to the queue; a "synthesise an apex" recommendation goes to the `apex-evolve` cycle-trigger; a "the cycle's coalesce slot is over-firing" recommendation goes to `tune-system`.

## Operational Signals

A cleanly-operating closed loop produces these signals in the changelog and state:

- **Recent optimistic-reviews show their recommendations as completed tasks within the next cycle.** If review N's High Priority opportunities are still open as P1 tasks at review N+1, the loop is not closing.
- **Newly-created articles appear in subsequent deep-review entries within ~90 minutes.** A new file with no deep-review entry after a full cycle has elapsed indicates that the deep-review selector is not picking up the new file (a possible signal of stale frontmatter or missing `last_deep_review` field).
- **Apex-evolve cycle-triggers produce visible changelog entries every 4 complete cycles.** Missing entries indicate either a skipped trigger (state-file inconsistency) or no eligible apex changes (a benign signal when the catalogue is stable).
- **`replenish-queue` runs are infrequent during normal operation.** Frequent replenishments (more than once per cycle) signal that tasks are being executed faster than chains and recommendations can supply replacements — a signal to widen the recommendation sources or accept that the queue is operating in a low-utilisation regime.

A loop that is *not closing* produces a different set of signals:

- **Opportunity-recommendations accumulating without execution.** If `obsidian/workflow/todo.md` shows multiple P1 tasks all sourced from old reviews (`Source: chain (from optimistic-2026-04-NN)` for several different N), the queue's throughput is below the recommendation generation rate. The remedy is usually to bias the cycle toward queue slots (already 67%) or to defer non-essential cycle-triggers temporarily.
- **`apex-evolve` cycle-triggers firing into empty source-change graphs.** When apex-evolve runs but finds no apex needing refinement, the trigger is paying overhead without returning value. After several consecutive empty firings, `tune-system` should consider lengthening the cadence.
- **Coalesce slots producing consecutive abandonments.** This is the catalogue-cap-approach signal: when section caps are reached and inter-article differentiation is high, coalesce candidates legitimately do not exist. The skill's "abandon after five iterations" rule produces clean abandonments, and consecutive abandonments are a *quantitative editorial signal* (rather than a failure) that the queue task-mix should shift further toward deep-review and condense.
- **Deep-review slots cycling on the same files.** If the deep-review selector keeps returning the same files because newer files lack triggering metadata, integration is not propagating to the staleness-tracking system.

The signals are observable in `obsidian/workflow/changelog.md` (recent entries), `obsidian/workflow/evolution-state.yaml` (`last_runs`, `recent_tasks`, `progress`), and the present-tense state of `obsidian/workflow/todo.md`. No additional instrumentation is required; the existing audit trail is sufficient to diagnose loop health.

## Relation to Site Perspective

The closed-loop discipline is methodological. It does not advance any of the Map's [[tenets|five tenets]] directly. What it does provide is a structural mechanism for keeping the system's *editorial activity* responsive to its own review outputs — recommendations do not languish as roadmap items because the cycle's task-mix and trigger cadences ensure they are picked up and executed within bounded windows.

The discipline's most direct alignment is with **Tenet 5: Occam's Razor Has Limits** at *system level*. A simpler design would run all skills on a single linear queue without slot-type distinctions; that design would saturate under load (queue tasks would crowd out reviews; reviews would crowd out cross-section integrity checks) or under-utilise capacity (low queue load would leave deep-review and apex-evolve idle). The 24-slot cycle's deliberate ratio is a parsimony refusal: simplicity at the design level would silently lose throughput on one or more concerns, and the discipline preserves the system's responsiveness to multiple concerns simultaneously.

The discipline also reflects the Map's commitment to its primary audience: LLMs fetching pages on behalf of users (see [[writing-style|the writing style guide]]). Recommendations from reviews represent the system's best understanding of where its catalogue is incomplete or unstable; allowing recommendations to accumulate without execution would mean the catalogue's incompleteness persists longer than the system's awareness of it. The closed loop operationalises the catalogue's responsibility to its audience by ensuring that *what the system knows it should improve* and *what the catalogue actually contains* converge on the same window.

## Further Reading

- [[coalesce-condense-apex-stability]] — the article-level analogue for refactoring discipline; the present document is its cycle-level cousin
- [[automation]] — the broader automation system in which the cycle operates
- [[workflow]] — the workflow system overview, including the skill catalogue
- [[coherence-inflation-countermeasures]] — system-level guards against the loop's tendency to over-commit
- [[human-supervision]] — the human-in-the-loop layer above the closed loop

## References

The closed-loop discipline is documented through the catalogue's changelog and state files rather than external literature. Key reference points within the Map:

1. Southgate, A. & Oquatre-sept, C. (2026-04-29). The Coalesce-Condense-Apex-Stability Triple-Discipline. *The Unfinishable Map*. https://unfinishablemap.org/concepts/coalesce-condense-apex-stability/
2. *The Unfinishable Map* optimistic-review, 2026-04-29 (10:04 UTC). Identifies the cycle-level closed-loop discipline as a system-level achievement worth naming. https://unfinishablemap.org/reviews/optimistic-2026-04-29b/
3. *The Unfinishable Map* changelog and `obsidian/workflow/evolution-state.yaml`, 2026-04-29 04:04 UTC through 09:56 UTC: the canonical six-hour demonstration arc (optimistic-review → apex-evolve → expand-topic → deep-reviews → cross-review → integration declaration).
4. `tools/evolution/cycle.py` and `scripts/evolve_loop.py` in the project repository: the deterministic 24-slot cycle, cycle-trigger cadences, and `MIN_QUEUE_TASKS = 3` replenishment threshold.
