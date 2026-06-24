---
ai_contribution: 100
ai_generated_date: 2026-06-24
ai_modified: 2026-06-24 18:15:14+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-24
date: &id001 2026-06-24
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Neurological Dissociations as Interface Architecture
topics: []
---

**Date**: 2026-06-24
**Article**: [Neurological Dissociations as Interface Architecture](/topics/neurological-dissociations-as-interface-architecture/)
**Previous review**: [2026-06-05](/reviews/deep-review-2026-06-05-neurological-dissociations-as-interface-architecture/)
**Focus**: Sixth deep review (heavily convergence-damped, score 15). Confirm the FND/motor-channel propagation fix landed; publisher-of-record web-verify the two citations newly added by that fix (Voon 2010, Edwards 2012); audit inline↔References completeness. Length-neutral / single-search-budget pass on a long-converged article.

## What Changed Since Last Review

Two commits touched the file since 2026-06-05:

1. **a3811a02f (refine-draft)** — the line-1847 FND/motor-channel propagation fix the 2026-06-05 review deferred. Body line 109 was rewritten from the BACKWARDS "disconnects the same descending motor channel through purely psychogenic functional decoupling—no lesion required" framing to the correct mechanism: *"an abnormally precise motor prior that actively generates the symptom—not a severed pathway: imaging shows increased amygdala-to-supplementary-motor-area connectivity (Voon et al., 2010), and the Bayesian account treats the symptom as inference dominated by a high-precision prior overriding sensory and volitional input (Edwards et al., 2012). The channel's output is functionally overridden, not disconnected."* This is the fix the 2026-06-04 Claude Opus 4.8 outer review called for. The deferred coordination item from the prior review is now **RESOLVED**.

2. Frontmatter timestamp churn (ai_modified bump).

The FND fix introduced two new inline citations (Voon 2010, Edwards 2012) and two new References entries. These are the only new bibliographic content since the last clean review and are the focus of this pass's web-verify budget.

## Citation Verification (Live Web, This Pass)

Per-cite ledger (publisher-of-record web-verified this pass for changed content; stable cites carry forward prior-pass verification):

- **Voon, V., Brezing, C., Gallea, C., et al. (2010). Emotional stimuli and motor conversion disorder. *Brain* 133(5), 1526–1536, doi:10.1093/brain/awq054** — state: **real-correct**. Verified against Oxford Academic + PMC (PMID 20371508). Authors, title, journal, volume, issue, pages, DOI all correct. Load-bearing body claim ("increased amygdala-to-supplementary-motor-area connectivity") faithful: the study reported a positive correlation in the amygdala→SMA path during affective processing in conversion disorder.
- **Edwards, M. J., Adams, R. A., Brown, H., Pareés, I., & Friston, K. J. (2012). A Bayesian account of 'hysteria'. *Brain* 135(11), 3495–3512, doi:10.1093/brain/aws129** — state: **real-correct**. Verified against Oxford Academic + PubMed (PMID 22641838). Authors, title, journal, volume, issue, pages, DOI all correct. Body claim ("inference dominated by a high-precision prior overriding sensory and volitional input") faithful to the abstract's hierarchical-Bayesian active-inference account.
- **Hu, J.-J., Liu, Y., Yao, H., et al. (2023). *Nature Neuroscience* 26, 751–764, doi:10.1038/s41593-023-01290-y** — state: **real-correct, but was an inline↔References orphan — FIXED**. The cite "(Hu et al. 2023)" appears inline (body line 171, KCC2 active-reboot mechanism) but had NO entry in the References block. The 2026-05-28 and 2026-06-05 reviews web-verified the cite as accurate (PMID 36973513) yet did not notice the missing bibliographic anchor. Re-verified canonical metadata this pass against Nature Neuroscience: full author list Hu/Liu/Yao et al., vol 26, pp 751–764. **Resolution: added the missing References entry** (cite is faithful; the §2.4 step-5 fix for a real cite missing its reference is to add the reference, not remove the cite). Inline claim (KCC2 downregulation is the active mechanism of emergence from anesthesia) faithful.
- **Stable cites not re-spent this pass** — Santander 2025 PNAS (re-verified 2026-06-05, PMID 41118210), Berthier 1988 (PMID 3415199), Geschwind 1965 (PMID 5318481), Mashour three-states taxonomy (attributed to "Mashour and colleagues", no dated-cite contamination), Nagel 1971, Weiskrantz 1986, Norretranders 1998, Grahek 2007. None attached to new or changed claims; verified in prior passes; not re-spent against the one-search budget.

**Empirical-record currency sweep**: `find_superlative_claims` returned no superlative phrases. The "1 cm of intact callosum preserves full integration" finding is phrased as redundancy, not a "current record" superlative, and was currency-checked in the prior pass. No superseded superlatives.

**Audit result: clean after the one fix.** One orphan-reference defect corrected (Hu 2023 added to References). No fabricated, wrong-metadata, dropped-qualifier, or currency-superseded cites.

## Cross-Article Consistency Check (FND framing)

Verified the corrected FND framing is now consistent with the sibling [conversion-disorder-as-consciousness-side-fault](/topics/conversion-disorder-as-consciousness-side-fault/) article. Both now describe the same mechanism: active over-generation of a precise inhibitory/motor prior (Edwards et al. 2012 Bayesian-FND account) with increased amygdala→SMA coupling — explicitly NOT a severed/disconnected channel. The two articles cite different but both-real Voon papers for the connectivity finding (this article: Voon 2010 *Brain*; conversion-disorder article: Voon 2011 *Movement Disorders*) — not a discrepancy, both are faithful. The backwards-framing defect that spanned the cluster is resolved in both files.

## Pessimistic Analysis Summary

### Critical Issues Found
One, now fixed: **Hu et al. 2023 inline↔References orphan** (faithful cite missing its bibliographic entry) — added the References entry. This is a correctable completeness defect, not a bedrock disagreement.

- **Attribution (§2.5)**: clean. Source exposition (Mashour taxonomy, Hu mechanism, PNAS callosum finding, Voon/Edwards FND mechanism) stays separated from Map interpretation. No conflation, no overstated positions, no false shared commitments. The new FND sentence correctly attributes the connectivity finding to Voon and the precision-prior account to Edwards/Friston without injecting Map framing into the source claims.
- **Reasoning-mode (§2.6)**: "Against Identity Theory" refutes naive identity on its own terms (predicts uniform degradation; dissociations contradict — Mode One) then marks the functionalist boundary honestly (Mode Three). Epiphenomenalism engagement concedes the rebuttal "logically available" while showing it "considerably more strained" — honest, not boundary-substitution. **No editor-vocabulary label leakage** (grep confirmed: no Mode-N / direct-refutation / evidential-status callouts in body).
- **Calibration**: No possibility/probability slippage. The compound-signature paragraph explicitly bounds the dualist inference to "compatibility-grade, not vindication-grade." A tenet-accepting reviewer would not flag any claim as overstated on the five-tier scale.

### Medium / Low Issues Found
None new. All prior additions remain in place and well-integrated.

### Counterarguments Considered
- Naive identity theorist: refuted on own terms (settled). Sophisticated functionalist: bedrock boundary, explicitly named. Epiphenomenalist "neural shadow": conceded logically available. MWI defender: indexical-identity framing. All stable — not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved
- Truncation-resilient two-paragraph opening stating the whole thesis.
- Dissociation-to-channel table + "What this maps" observation-then-interpretation pattern.
- The corrected FND paragraph now strengthens the convergence-of-three-routes argument: structural disconnection (alien hand) vs active functional capture (conversion disorder) are now correctly "mechanistically disjoint routes," which is exactly what makes the channel's separability a finding rather than a single-lesion artefact.
- Convergence-of-three-perturbation-routes argument, bounded to compatibility-grade.
- Mermaid six-channel synthesis diagram; self-model bypass of attentional gating.
- Honest epiphenomenalism engagement.

### Enhancements Made
- Added the missing Hu et al. 2023 References entry (bibliographic completeness; +1 line).

### Cross-links Added
None — already densely and accurately integrated.

## Remaining Items

None. The FND/motor-channel framing deferred by the 2026-06-05 review has been resolved (commit a3811a02f) and its new citations verified.

Length: 3153 → 3186 words (106% of 3000 soft target, soft_warning) → +33 (one reference line). Operated in length-neutral mode otherwise; no body expansion.

## Stability Notes
- Sixth deep review; article confirmed stable across 2026-04-17, 2026-05-28, 2026-06-05, and again here. The only substantive change since the last review was the FND-framing fix, which is correct and now publisher-verified.
- **The FND/motor-channel framing is now CORRECT** — active functional override (Edwards Bayesian prior + Voon amygdala→SMA), not channel disconnection. Future reviews should NOT re-introduce or re-flag the old "disconnects the same descending motor channel" framing; that was the defect, and it is fixed.
- Bedrock disagreements (naive identity refuted on own terms; sophisticated functionalist at boundary; epiphenomenalist; MWI defender) settled — do NOT re-flag.
- The compound-signature / convergence-of-three-routes argument and its compatibility-grade bound are load-bearing; preserve through future condensation.
- At soft threshold (106%) — any future addition must be length-neutral or paired with condensation.
- Citation ledger is now complete (every inline cite has a References entry, every References entry is cited or carries a paradigm-case wikilink). The Hu 2023 orphan that survived two prior web-verify passes (verified as accurate, but not checked for a reference anchor) is the lesson: §2.4 step 5 (inline↔References cross-reference) must run even when the cite itself verifies clean.