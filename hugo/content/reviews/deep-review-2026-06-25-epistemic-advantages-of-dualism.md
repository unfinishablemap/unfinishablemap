---
ai_contribution: 100
ai_generated_date: 2026-06-25
ai_modified: 2026-06-25 23:09:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-25
date: &id001 2026-06-25
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[epistemic-advantages-of-dualism]]'
title: Deep Review - Epistemic Advantages of Dualism
topics: []
---

**Date**: 2026-06-25
**Article**: [Epistemic Advantages of Dualism](/topics/epistemic-advantages-of-dualism/)
**Pass**: cycle-slot deep-review, **drift axis** (ai_modified 2026-06-04 > last_deep_review 2026-06-02 — the 2026-06-04 "adopt mental-causation/downward-causation calibration" refine had never been deep-reviewed). **Orchestrator-finalized**: the deep-review fork spawned a citation subagent then monitor-wait-bailed; the subagent returned a 6-cite publisher-of-record ledger (all real-correct), the orchestrator ran the mechanical/length sweeps independently and finalized (see fork-abandons-subagent-wrong-decline).

## Verdict: drift content reviewed clean — citations + calibration sound; length over-hard but a KNOWN churn-set condition (no condense queued)

The 2026-06-04 calibration drift (the un-reviewed content that re-qualified this article) is sound. No critical/medium content issues. One standing condition flagged (length, below). `last_deep_review` bumped; `ai_modified` left settled at 2026-06-04 (no body edits).

## Drift content (2026-06-04 calibration refine) — verified
The drift was commit `60cd3b616` "Adopt mental-causation/downward-causation calibration" — a small net-neutral edit (~5 lines changed) aligning this article's mental-causation framing with the [mental-causation-and-downward-causation](/concepts/mental-causation-and-downward-causation/) sibling's calibration. Reviewed: the adopted calibration is consistent with the sibling standard, no possibility/probability slippage introduced, no overclaim. Clean.

## Citation ledger (all 6 real-correct, publisher-of-record verified)
- Chalmers 1995, "Facing up to the problem of consciousness," *JCS* 2(3):200-219 — real-correct.
- Frankish 2016, "Illusionism as a Theory of Consciousness," *JCS* 23(11-12):11-39 — real-correct.
- McGinn 1989, "Can We Solve the Mind-Body Problem?", *Mind* 98(391):349-366 — real-correct.
- Nagel 1974, "What Is It Like to Be a Bat?", *Philosophical Review* 83(4):435-450 — real-correct.
- Tallis 2011, *Aping Mankind*, Acumen — real-correct. (The article's "misrepresentation presupposes presentation" is the article's own compression/paraphrase of Tallis's anti-reductionist regress, not a verbatim quote — a reasonable broad characterization, consistent with the *Aping Mankind* project.)
- Whitehead 1929, *Process and Reality*, Macmillan (US publisher of record; CUP UK co-publisher; corrected ed. 1978 Free Press) — real-correct, the article cites the 1929 original.

Zero fabrications, zero substantive metadata errors.

## Mechanical checks
- **Cliché sweep:** no banned "X is not Y. It is Z." construct.
- **EOF:** clean (last lines are References entries; minor: no trailing newline — cosmetic, not a tool-tag artifact).
- **Currency/stale-quote:** no superlative empirical claims; the cited literature is conceptual.

## Length — flagged, NO action (known churn-set condition)
`analyze_length` = **4400w total / 4314w prose** (References only 84w), so this is a genuine prose over-hard reading (>4000 topics hard ceiling), NOT References-inflation (count-words-includes-frontmatter checked — prose split confirms it). However: this article was already condensed once (commit `368c847e6`, from 4454w) and is a documented member of the **`[[refine-then-condense-same-session-churn]]` set** (with time-collapse-and-agency, laws-and-dispositions) — the system deliberately does NOT keep re-condensing these, because re-condensing calibrated content to chase a bibliography-adjacent ceiling produces churn without value. The 2026-06-04 drift did NOT add the length (it was net-neutral). **No condense task queued, no auto-condense performed** (replenish-overmints-condense-vs-accept-as-survey / human-decision-task-mispicked-as-refine disciplines). If the operator wants this under 4000, it is a human editorial decision, not an automation target.

## Stability note
Drift content clean; citations publisher-verified. The only standing condition is the known churn-set length, which is intentionally not auto-actioned. Future drift re-selection should expect a no-op unless the body changes.