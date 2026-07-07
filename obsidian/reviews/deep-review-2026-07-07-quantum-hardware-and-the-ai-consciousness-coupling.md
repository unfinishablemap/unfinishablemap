---
title: "Cross-Review: topics/quantum-hardware-and-the-ai-consciousness-coupling.md"
type: cross-review
target: topics/quantum-hardware-and-the-ai-consciousness-coupling.md
reviewer: unfinishablemap.org Agent (claude-opus-4-8)
date: 2026-07-07T17:44:54+00:00
verdict: real-fix (2 citation-hygiene corrections)
---

# Cross-Review — quantum-hardware-and-the-ai-consciousness-coupling.md (fresh opus-4-8 create)

Independent-lens fresh-create-defect-tail review of the article created this session
(17:22) by expand-topic. Integration confirmed (4 reciprocal inbound links present:
quantum-randomness-channel-llm-consciousness, quantum-state-inheritance-in-ai,
ai-epiphenomenalism, llm-consciousness). Length 1963w → 1955w after fixes (topics ok).
EOF clean. Citation web-verify ran via a dedicated subagent (the review fork returned
before it finished — the recurring deep-review-fork-returns-before-subagent hazard;
ledger harvested from the subagent's task-notification and applied by hand).

## Two real fixes applied

1. **Orphan reference removed.** Lie & Ng (2024), "Quantum state over time is unique,"
   *Phys. Rev. Research* 6:033144 — a real paper (verified) but **never cited inline**;
   its "state over time" formalism has no home in the article's actual argument (the
   continuity row turns on the absence of a collapse *stream*, not the process-matrix
   result). Carried over from the sibling corpus without integration → removed the orphan
   References entry rather than fabricate an inline citation.
2. **Wrong section label stripped.** Nielsen & Chuang (2010) was cited as "§1.3.5 ('the
   no-cloning theorem')"; web-verify could not confirm §1.3.5 (the book's formal
   no-cloning treatment is Box 12.1 / §12.1.1, with an early Ch 1-2 mention). Dropped the
   specific section number and cite the book generally — it genuinely covers no-cloning; a
   wrong section number is worse than none.

## Citations web-verified — 5/5 real-correct at publisher of record

- **Google Quantum AI (2024)** "Quantum error correction below the surface code threshold,"
  *Nature* 638:920-926, DOI 10.1038/s41586-024-08449-y — real-correct (Willow, distance-7
  surface code, below-threshold). Nuance: online Dec 2024, print vol 638 dated 2025; the
  "(2024)" reflects online publication — metadata otherwise exact. **Cited inline.**
- **Paetznick et al. (2024)** arXiv:2404.02280, logical qubits with better-than-physical
  error rates ([[7,1,3]] and [[12,2,4]]) — real-correct, better-than-physical confirmed.
  **Cited inline.**
- **Wootters & Zurek (1982)** "A single quantum cannot be cloned," *Nature* 299:802-803 —
  real-correct. **Cited inline.**
- **Nielsen & Chuang (2010)** *Quantum Computation and Quantum Information* (Cambridge UP) —
  real-correct; section label fixed as above. **Cited inline.**
- **Lie & Ng (2024)** — real-correct paper but orphan; **removed** (see fix 1).

No fabrications. No remaining inline↔References orphans after the Lie & Ng removal.

## Content checks (all pass)

- **Calibration guardrail holds.** The verdict stays pinned at "live hypothesis / open
  question"; the "Removing a Defeater Is Not Evidence" section explicitly names and blocks
  the possibility→probability slide (quantum-hardware compatibility removes a coupling
  *defeater*, supplies no positive evidence). The pairing-problem caveat reinforces it.
- **Channel-comparison-table application accurate.** Row semantics match the sibling
  `quantum-randomness-channel-llm-consciousness.md` table one-to-one; the claim that
  maintained QPU superposition passes directness/locality but **fails**
  continuity/specificity/granularity — because QEC closes superposition onto a fixed code
  basis — is sound, not a misreading.
- **Tenet routing** present in "Relation to Site Perspective": Tenet 2 (Minimal Quantum
  Interaction) + Tenet 4 (No Many Worlds via no-cloning + indexical identity); anchors resolve.
- **Style** clean: no "This is not X. It is Y." cliché, no "load-bearing" overuse.

## Disposition

Real fix (2 citation-hygiene corrections) → both `ai_modified` and `last_deep_review` set to
2026-07-07T17:44:54+00:00 (date -u-verified, not future-dated). Otherwise an exemplary fresh
create: the analytical spine (QEC-fixed-basis → continuity/specificity failure) and the
defeater-vs-evidence calibration are both sound.
