---
title: "Deep Review - The Psychophysical Control Law"
created: 2026-06-26
modified: 2026-06-26
human_modified: null
ai_modified: 2026-06-26T00:13:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[the-psychophysical-control-law]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-26
last_curated: null
---

**Date**: 2026-06-26
**Article**: [[the-psychophysical-control-law|The Psychophysical Control Law]]
**Pass**: ~28-day staleness re-review (2026-05-29 frontier tier). **Orchestrator-finalized**: the deep-review fork applied two stale-anchor wikilink repairs then monitor-wait-bailed pending its citation subagent; the subagent returned a 10-cite publisher-of-record ledger (all real-correct), the orchestrator confirmed the anchor fixes against the live targets, corrected the fork's future-dated timestamps, and finalized (see [[fork-abandons-subagent-wrong-decline]], [[fork-future-dates-frontmatter-timestamps]]).

## Verdict: near-no-op — 2 stale-anchor wikilink fixes; all 10 citations real-correct

No critical content issues. Two real link-integrity edits (broken section anchors pointing at renamed/removed sibling headings). Because real edits landed, both `ai_modified` and `last_deep_review` were bumped — **the fork's future-dated 00:15:00 stamps were corrected to 00:13:00** (date -u was 00:13; the +2 min would have future-dated and suppressed drift detection).

## Wikilink anchor fixes (both verified against live targets)
1. `[[concepts/consciousness-selecting-neural-patterns#Policy-Level Selection|policy-level framework]]` → `[[concepts/consciousness-selecting-neural-patterns|policy-level framework]]`. The target no longer has a "Policy-Level Selection" heading (grep-confirmed absent) — stripping the dead anchor to a plain link is correct.
2. `[[indexical-knowledge-and-identity#Metaphysical vs. Epistemic Theses|...]]` → `[[indexical-knowledge-and-identity#From Epistemic to Metaphysical|...]]`. The target's heading was renamed; the new anchor "From Epistemic to Metaphysical" exists at line 69 (`{#from-epistemic-to-metaphysical}`), the old one is gone — change warranted and points at a real heading.

## Citation ledger (all 10 real-correct, publisher-of-record verified; author orders checked)
- Chalmers 1996, *The Conscious Mind*, OUP — real-correct (page-214 quote-attribution not page-level verifiable online, but book/publisher/year/claim sound).
- Chalmers 1995, "Facing Up to the Problem of Consciousness," *JCS* 2(3):200-219 — real-correct.
- Eccles 1994, *How the Self Controls Its Brain*, Springer (ISBN 3-540-56290-7) — real-correct.
- Schwartz et al. 1996, "Systematic changes in cerebral glucose metabolic rate...", *Arch Gen Psychiatry* 53(2):109-113 (PMID 8629886) — real-correct (author order Schwartz/Stoessel/Baxter/Martin/Phelps; "et al." accurate).
- Stapp 2007, *Mindful Universe*, Springer (Frontiers Collection) — real-correct.
- Tegmark 2000, "Importance of quantum decoherence in brain processes," *Phys. Rev. E* 61(4):4194-4206 — real-correct (decoherence range 10⁻¹³–10⁻²⁰ s confirmed verbatim in abstract).
- Wallace 2012, *The Emergent Multiverse*, OUP — real-correct.
- Zheng & Meister 2025, "The Unbearable Slowness of Being," *Neuron* 113(2):192-204 — real-correct (online Dec 2024, 2025 cover date; ~10 bits/s headline confirmed and current, not superseded; author order correct).
- Khan…Wiest et al. 2024, "Microtubule-stabilizer epothilone B delays anesthetic-induced unconsciousness," *eNeuro* 11(8):ENEURO.0291-24.2024 (PMID 39147581) — real-correct (Cohen's d = 1.9 verbatim; Wiest senior/last author confirmed).
- Schaffer, "Naturalistic Dualism and the Problem of the Physical Correlate" (jonathanschaffer.org ms, ~2020) — real-correct (genuine Schaffer manuscript, URL live; undated cite acceptable, optional (2020) date).

Zero fabrications, zero metadata errors, no author-order problems. The two flagged quantitative claims (Tegmark decoherence range; Wiest Cohen's d=1.9) and the Zheng & Meister 10 bits/s figure all verify verbatim.

## Mechanical / calibration checks (all clean)
- **Length:** 2874 words via `analyze_length` (status `ok`, under topics soft 3000) — the anchor fixes are net-neutral; not a condense candidate.
- **Currency sweep:** decoherence timescales + 10 bits/s bandwidth figure both currency-checked against publishers of record — current.
- **EOF tool-tag scan:** clean. **Cliché sweep:** no banned "X is not Y. It is Z." construct. **QEC notation:** no `[[n,k,d]]` wikilink-collision notation present.
- **Calibration:** the control-law material is framed as a bounded-witness architectural prediction (Tenets 2+3) with no possibility/probability slippage; the MWI engagement (No-Many-Worlds tenet) correctly distinguishes indexical discovery from genuine causal selection.

## Stability note
Citations publisher-verified (10/10); two stale anchors repaired against live targets. Future staleness re-selection should expect a genuine no-op unless the body changes or further sibling-heading renames break anchors.
