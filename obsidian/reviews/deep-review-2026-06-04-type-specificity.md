---
title: "Deep Review - Type-Specificity (Post-Refine/Condense Calibration Audit)"
created: 2026-06-04
modified: 2026-06-04
human_modified:
ai_modified: 2026-06-04T20:41:00+00:00
draft: false
topics: []
concepts:
  - "[[type-specificity]]"
related_articles:
  - "[[type-specificity]]"
  - "[[the-binding-problem]]"
  - "[[apex/taxonomy-of-voids]]"
  - "[[evidential-status-discipline]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-04
last_curated:
---

**Date**: 2026-06-04
**Article**: [[type-specificity|Type-Specificity]]
**Previous review**: [[deep-review-2026-05-19-type-specificity|2026-05-19]] (cross-review); [[deep-review-2026-05-11-type-specificity|2026-05-11]] (initial)
**Review mode**: Diff-first audit of new four-criterion scoring + condense-survival + web-verify + anchor-seam
**Word count**: 3185 → 3185 (net 0; three small corrective edits)

## Diff Scoping

The two prior reviews (2026-05-11, 2026-05-19) both predate the new content. Two commits landed after the 2026-05-19 review:

1. **95410f798** (refine-draft) — added the §Independence Scoring of the Three Grains section: a four-criterion (+ fifth diagnostic) independence scoring of the vitalism / binding-unity / capacity grains. **This is genuinely new, never-reviewed own-content** — the meat of this pass.
2. **39bd325b7** (condense) — the article had hit 5264 words (105% of concepts critical); the condense collapsed the three per-grain scoring sub-sections into compressed paragraphs.

### Condense-survival check (per [[condense-regresses-calibration-qualifiers]])

**The 4-criterion scoring SURVIVED the condense intact.** Verified by reading the full condense diff:
- All per-grain scores preserved verbatim (signature specificity / structured persistence / cross-observer convergence / framework independence + the fifth *independence-of-deployment* diagnostic).
- The calibration verdicts survived word-for-word: *strongly supported* (recognising the structural feature) / *realistic possibility, contested* (evidential force against generic-mechanism reductions) / *live hypothesis* (role in the convergence verdict).
- The downward-calibration move ("at most *moderate* convergence ... not the *strong* convergence the three-fold parallel might suggest") survived.
- No load-bearing hedge or citation-framing dropped. The condense cut exposition and sub-headings, not calibration content. **No regression.**

## Pessimistic Analysis Summary

### Critical Issues Found and Fixed

1. **Wrong-year / wrong-author citation (real paper)** — The new scoring cited cross-species binding evidence as "Klein et al. 2024." Web-verify + corpus cross-check (`research/invertebrate-consciousness-interface-test-case-2026-04-06.md:62`) confirm the intended source is **Klein & Barron (2016)**, "Insects have the capacity for subjective experience," *Animal Sentience* 9(1) — not a 2024 paper. No 2024 Klein paper on cross-species perceptual unity/binding exists; the 2024 invertebrate-consciousness landmark is the New York Declaration / Andrews, not Klein. **3-state verdict: real-paper-wrong-year-and-author-form → FIX** (not fabrication, not drop). Corrected to "Klein and Barron 2016." This citation was introduced by the refine-draft (it is NOT in source `the-binding-problem.md`, which carries no cross-species citations), so the defect originated in the new content, consistent with the [[fresh-create-defect-tail]] pattern for newly-added factual content.

2. **Broken anchor + stale count claim (source drifted)** — The scoring linked twice to `[[apex/taxonomy-of-voids#two-worked-exhibits-in-independence-scoring]]`. The source heading has since been **retitled** to "### Worked Exhibits in Independence Scoring" (the taxonomy now carries four exhibits — surplus void, introspection-architecture, type-specificity itself, and medium-status cluster — so "Two" was dropped). The anchor no longer resolves, and the Further Reading line's bare "two worked exhibits" risked reading as "the taxonomy has only two." **Fixes**: anchor → `#worked-exhibits-in-independence-scoring`; count framing → "two *void-cluster* worked exhibits" (still true, since those two are the void-cluster exhibits type-specificity parallels).

### Web-Verify Results (all citations, by class)

| Citation | Class | Verdict |
|---|---|---|
| Klein "et al. 2024" → Klein & Barron 2016 | inline, new | **FIXED** (wrong year+author on real paper) |
| Mather and Dickel 2017 (cephalopod cognition) | inline, new | Verified real (*Curr. Opin. Behav. Sci.* 16:131-137); kept |
| Treisman 1980 (feature-integration) | inline | Verified real (*Cognitive Psychology* 12:97-136); kept |
| Crick and Koch 1990 (40-Hz binding) | inline | Verified real (*Seminars in the Neurosciences* 2:263-275); kept |
| Singer 1995-2010, Tononi 2004 | inline | Standard binding-literature, correctly characterised; kept |
| Suddendorf & Corballis / Penn et al. / Tomasello / Henrich / Carruthers | inline, no-year | Standard comparative-cognition figures, correctly named; kept |
| Chalmers 1996 (*The Conscious Mind*, OUP) | formal ref | Canonical; kept |
| Revonsuo 2006 (*Inner Presence*, MIT) | formal ref | Verified (ISBN 0-262-18249-1); kept |
| Cowan 2001 (*BBS* 24(1), "magical number 4") | formal ref | Verified; kept |

### Calibration Audit (the load-bearing question)

**The scoring is applied honestly — it deflates, it does not game toward dualism.** Diagnostic test (would a tenet-accepting reviewer still flag any claim as overstated?): **No.** Specifically:
- The section opens by naming the "three independent confirmations" temptation as a *trap* (the cluster-coherence move [[evidential-status-discipline]] and [[common-cause-null]] flag).
- It scores *framework independence* as the **weakest** face across all three grains and uses that to calibrate the cumulative weight **down** — "at most *moderate* convergence ... not the *strong* convergence the three-fold parallel might suggest."
- No possibility→probability slippage: the article never uses a tenet to remove a defeater and then treat that as upgrading evidence. The "realistic possibility, contested" tier is explicitly qualified "coherent but framework-internally so" — i.e., it flags the coherence-≠-evidence distinction rather than committing it.
- The "independence-of-deployment" positive result is correctly scoped to *formulation-independence* (each grain statable without the others as premises) and is firewalled from the *framework-independence* (cross-tradition) face it scores weak. The honest move is keeping these two senses of "independent" separate — done.

### Anchoring

`evaluate_anchoring` returns `[]` (no flags) both before and after edits. No over-claim at underdetermination points, no over-hedging-into-mush.

## Optimistic Analysis Summary

### Strengths Preserved
- The self-deflating scoring discipline — naming its own cluster-coherence temptation and calibrating down — is the article's load-bearing virtue and a model application of [[evidential-status-discipline]]. Preserved untouched.
- Block-quote discipline (verbatim from source exhibits) — the two prior reviews verified both quotes; unchanged this pass.
- The three-grain parallel-applications structure tying together three other Map articles under one discipline.

### Enhancements Made
- Citation corrected to the real intended source (credibility).
- Cross-link integrity restored (anchor now resolves; count claim future-proofed against the source's growth to four exhibits).

## Remaining Items

**Optional follow-on (out of scope this pass, NOT queued as blocking):** The taxonomy-of-voids source now states the **medium-status cluster** exhibit "discharges in part" the same-hand / unfavourable-case burden. Type-specificity's closing paragraph still says "a clean unfavourable case ... remains the open burden." This is mild forward-staleness (type-specificity can't forward-reference an exhibit added later), and its own-vantage claim is still defensible, so no edit forced — over-coupling the two articles risks more harm than the staleness. Left for a future apex-evolve/cross-review if the coupling is judged worth tightening.

## Stability Notes

- **Convergence with a real defect tail**: The 2026-05-11 and 2026-05-19 reviews verified the *inherited* exhibit content (quotes, capacity-list) as faithful and stable. This pass found two real defects — both confined to the **post-review-added** scoring section (a mis-cited cross-species reference + a source-drift anchor break), exactly the [[fresh-create-defect-tail]] pattern: new factual content carries a remediation tail the converged inherited content does not. Future reviews should treat the inherited three-grain summary as converged and focus scrutiny on the scoring section's citations and its anchor-coupling to the (still-evolving) taxonomy-of-voids.
- **Calibration is honest and converged**: The scoring's downward-calibration discipline should NOT be re-flagged or "strengthened" toward higher tiers. Bedrock disagreements (eliminativist/illusionist explanandum-denial; MWI/quantum-skeptic non-engagement; Nagarjuna non-determinate phenomenal kinds) remain framework-boundary, not critical — do not re-flag.
- **Source-coupling watch**: type-specificity's scoring section is tightly coupled to taxonomy-of-voids' "Worked Exhibits" section, which is actively evolving (now four exhibits). The anchor and the exhibit-count framing are the drift-vulnerable seams; both fixed this pass.
