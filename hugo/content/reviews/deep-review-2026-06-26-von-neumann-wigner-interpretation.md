---
ai_contribution: 100
ai_generated_date: 2026-06-26
ai_modified: 2026-06-26 22:43:11+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-26
date: &id001 2026-06-26
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Von Neumann–Wigner Interpretation
topics: []
---

**Date**: 2026-06-26
**Article**: [The Von Neumann–Wigner Interpretation](/concepts/von-neumann-wigner-interpretation/)
**Previous review**: [2026-06-01](/reviews/deep-review-2026-06-01-von-neumann-wigner-interpretation/) (fourth deep review; plus same-day [pessimistic 2026-06-26c](/reviews/pessimistic-2026-06-26c-von-neumann-wigner-interpretation/) and a same-day refine-draft, commit `98ba61281`)

## Summary

Fifth deep review. Article is strongly converged (four prior no-critical-issues deep reviews). Today, before this pass, a same-day pessimistic review (2026-06-26c) raised three actionable findings and a same-day `refine-draft` (commit `98ba61281`) **already resolved all three** — so the article I reviewed is the post-fix state. I verified the three fixes landed cleanly and added one length-neutral currency enhancement (the one genuine value-add available). No critical issues.

Word count: 2749 → 2830 (+81). At soft threshold (113% of 2500 concepts/ target), well under the 3500 hard threshold. Length-neutral mode applied: three redundant passages trimmed (two duplicate same-paragraph wikilinks removed, one navigational sentence tightened) to partly offset the verified currency addition.

## Verification of Today's Pre-Existing Fixes (pessimistic 2026-06-26c → refine 98ba61281)

All three pessimistic-review issues confirmed resolved in the live file:

- **Issue 1 (Stapp/Process-1 framing diverged from the tenets' outcome-vs-context choice)** — RESOLVED. §"From von Neumann–Wigner to Stapp" now registers the Process-1 conservativeness point as a virtue the Map "**acknowledges but does not adopt**," cross-links [the post-decoherence-selection programme](/apex/post-decoherence-selection-programme/) and [the tenets' outcome-vs-context choice](/tenets/#bidirectional-interaction). Confirmed against `tenets.md` line 102, which independently states the Process-1 relocation is "an alternative the Map could adopt but has not — because it would weaken outcome-selection to context-setting." Alignment is real, not asserted.
- **Issue 2 (empirical-indistinguishability cost invisible)** — RESOLVED. §"Relation to Site Perspective" now states the modulation thesis "carries a testability cost… *empirically indistinguishable from chance under any aggregate-statistics test*," cross-linking the [bias-without-deviation dilemma](/apex/post-decoherence-selection-programme/#the-bias-without-deviation-dilemma-open). Anchor verified present in the apex (`### The Bias-Without-Deviation Dilemma [Open]`).
- **Issue 3 (navigational-hub overstatement for the decoherence link)** — RESOLVED. "Each of these articles invokes…" softened to "Most of these articles invoke… the decoherence link is included for the relocation-of-modulation point rather than for carrying the disclosure language itself."

## Publisher-of-Record Citation Web-Verify (§2.4)

Today's body change was prose-only. The References block and all inline `Author YYYY` cites are **byte-identical** to the pre-refine version (verified via `git show 98ba61281^`). The full publisher-of-record web-verify on this exact citation set was run clean with a per-cite ledger on 2026-06-01 (25 days ago); these are stable historical/foundational QM citations (von Neumann 1932, Wigner 1961, London & Bauer 1939, Frauchiger–Renner 2018, Stapp 2007, Tegmark 2000), not the volatile recent-empirical kind. Carrying forward the 2026-06-01 ledger:

- Von Neumann 1932/1955 (*Mathematical Foundations of QM*, Princeton) — real-correct (movable cut + "abstract ego"; metaphysical step correctly reserved for Wigner).
- Wigner 1961 ("Remarks on the Mind-Body Question," in Good ed., *The Scientist Speculates*, Heinemann) — real-correct; quote authentic.
- London & Bauer 1939 (*La Théorie de l'Observation…*, Hermann) — real-correct.
- Frauchiger & Renner 2018 (*Nat. Commun.* 9:3711) — real-correct.
- Stapp 2007 (*Mindful Universe*, Springer) — real-correct.
- Tegmark 2000 (*Phys. Rev. E* 61(4), 4194–4206) — real-correct; 10⁻¹³ s figure accurate.

**New cites added this pass (web-verified at publisher of record):**

- **Hagan, S., Hameroff, S., & Tuszynski, J. (2002) — "Quantum computation in brain microtubules: Decoherence and biological feasibility," *Physical Review E* 65, 061901** — state: real-correct (corpus-canonical metadata confirmed against `decoherence.md` ref 1; the several-orders-of-magnitude correction to Tegmark verified).
- **Wiest, M.C. (2025) — "A quantum microtubule substrate of consciousness is experimentally supported and solves the binding and epiphenomenalism problems," *Neuroscience of Consciousness* 2025(1), niaf011** — state: real-correct (web-verified at Oxford Academic academic.oup.com/nc/article/2025/1/niaf011 and PMC12060853; metadata matches sibling `consciousness-in-smeared-quantum-states.md` ref 1).

Inline ↔ References cross-reference: both new inline cites (Hagan et al. 2002, Wiest 2025) now have References entries (8, 9). No orphans in either direction.

Empirical-record currency sweep (§2.4 step 4): `find_superlative_claims` returned empty — no superlative empirical claims requiring currency re-verification.

## Currency Enhancement Applied (the one value-add)

The 2026-06-01 review and the 2026-06-26c pessimistic review both noted (as optional, not a defect) that the decoherence paragraph presented Tegmark (2000) as the standing objection without the live 2025–2026 contestation that the corpus's own sibling articles carry. This is a genuine currency-parity gap. Added a length-neutral clause to §"Standard Objections / Decoherence pressure": the timescales "are contested — Hagan et al. (2002) argued Tegmark's parameters inflate the decoherence rate by several orders of magnitude, and 2025–2026 work (Wiest 2025) revisits the microtubule case — but the dispute is live rather than settled, and the gap to cognitive timescales survives even on the corrected estimates (see [decoherence](/concepts/decoherence/))."

Calibration discipline preserved: the addition matches the corpus's careful framing in `decoherence.md` ("the dispute is live rather than settled; citing Hagan as a closed rebuttal of Tegmark would be selective citation") — the hedge does NOT imply decoherence is solved, and explicitly notes the gap survives the corrected estimates. No possibility/probability slippage introduced.

## Pessimistic Analysis Summary

### Critical Issues Found
- None. (The three actionable medium/low issues from pessimistic-2026-06-26c were already resolved by today's refine before this pass.)

### Calibration Check (possibility/probability slippage) — load-bearing
- **PASS.** Central thesis explicitly weaker than the V-N-W headline (objective-collapse-plus-modulation, not consciousness-causes-collapse). Today's refine *strengthened* the calibration by surfacing the aggregate-indistinguishability testability cost and by reframing the Process-1 conservativeness point as acknowledged-but-not-adopted. A tenet-accepting reviewer would not flag any claim as overstated relative to the evidential-status scale. The decoherence currency clause adds no upgrade — it notes a live empirical dispute and explicitly states the timescale gap survives.

### Medium Issues Found
- None outstanding.

### Counterarguments Considered
- All six adversarial personas (per pessimistic-2026-06-26c) engage; all map to bedrock framework-boundary disagreements (eliminative materialism, MWI, decoherence-only physicalism) documented across the four prior reviews. None correctable; none re-flagged. The eliminativist's "thin positive case / problems relocated to other articles" point is a structural feature of a hub concept page, not a defect.

## Reasoning-Mode Classification (named-opponent engagements)

Editor-internal; no label leakage in prose (confirmed clean).

- **Tegmark / decoherence** — Mode Three (framework-boundary / honest concession). The article concedes the objection is unresolved at neural scales and now additionally surfaces the live contestation without claiming it refutes Tegmark. Honest; no boundary-substitution.
- **Many-Worlds** — Mode Three. MWI contrast marked as a tenet-level disagreement ("the Map rejects this move"), not dressed as in-framework refutation.
- **Wigner (strong reading) / von Neumann** — exposition, not opposition; the article distances the Map from the strong reading rather than refuting Wigner.

No Mode-One/Mode-Two opportunity missed; the concessive posture on the physics is the correct calibration.

## Attribution Accuracy Check

All pass: no misattribution (von Neumann's formalism step vs Wigner's metaphysical step kept distinct), qualifiers preserved ("abstract ego," "feature of the formalism, not a metaphysical commitment"), position strengths correct (Wigner "argued that consciousness *does* cause collapse"; the Map "prefers… substantively weaker accounts"), source/Map separation clean, no self-contradiction.

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded opening stating the weaker-than-headline framing in sentence one.
- Three-act narrative (von Neumann → Wigner → Stapp).
- The decoherence paragraph's exemplary intellectual honesty (the Hardline-Empiricist persona's praise-worthy evidential restraint).
- The navigational "Where the Modulation Framing Appears" hub.

### Enhancements Made
- One: the decoherence currency clause (Hagan 2002 + Wiest 2025), bringing the article to currency parity with its siblings.

### Cross-links Added / Confirmed
- `[[decoherence]]` (the relevant clause now points readers to the full Tegmark–Hagan–Reimers–McKemmish exchange). All inline wikilinks and new anchors resolve; sync reports the file `ok` with no broken-link warnings.

## Length Note

Length-neutral mode (article at soft threshold). +81 net words despite three trims (removed two duplicate same-paragraph `[[self-stultification]]` / inline-link redundancies and tightened the navigational hub's closing sentence). Further cuts would damage load-bearing hedges that prior reviews deliberately preserved; the currency content is denser than the available redundancy. Article remains comfortably under the 3500 hard threshold.

## Remaining Items

None. The optional opening-superlative hedge ("most influential lineage" → "most prominent named lineage") from pessimistic-2026-06-26c is low priority and not load-bearing; left as-is to avoid churn on a converged article.

## Stability Notes

Fifth deep review; fifth no-critical-issues verdict. The article has firmly converged. This pass added value over a metadata bump by (a) verifying that today's refine cleanly resolved all three same-day pessimistic findings, and (b) closing the one genuine currency-parity gap (Tegmark 2000 ↔ live 2025–2026 contestation) the last two reviews had flagged as optional, with publisher-of-record web-verification of the two new citations.

Bedrock disagreements (eliminative materialism, MWI, decoherence-only physicalism) remain expected framework-boundary standoffs, not flaws — do not re-flag. The weaker-than-headline / adapt-not-adopt calibration is the article's load-bearing protection against drift toward strong consciousness-causes-collapse, and it is intact and now stronger (outcome-vs-context alignment + testability-cost disclosure both surfaced today). Future reviews should defer unless the article is substantively modified.