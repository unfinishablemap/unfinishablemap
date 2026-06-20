---
ai_contribution: 100
ai_generated_date: 2026-06-20
ai_modified: 2026-06-20 09:23:42+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-20
date: &id001 2026-06-20
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Functionalism
topics: []
---

**Date**: 2026-06-20
**Article**: [Functionalism](/concepts/functionalism/)
**Previous review**: [2026-06-01](/reviews/deep-review-2026-06-01-functionalism/) (seventh deep review)
**Word count**: 2971 (body) → 2971 (+0; converged no-op, no body change)
**Review type**: GENUINE-DRIFT verification (floor-restore mint). The drift since the 06-01 review is commit `23421a1c1` (2026-06-10 refine "Fix dangling Craddock (2017) reference + 3 prose findings"), which edited this file's own body — a refine bumps `ai_modified` but not `last_deep_review`, leaving those fixes unverified.

## Pessimistic Analysis Summary

### Craddock verdict — CORRECTLY RESOLVED (variant i → removed, not variant ii)

The 2026-06-10 refine did **not** wire the Craddock cite into the correct paper; it **removed the orphan References entry entirely** — which is the correct fix. Verified from git history:

- Pre-commit (`23421a1c1~1`): "Craddock, T.J.A., et al. (2017). 'Anesthetic Alterations of Collective Terahertz Oscillations in Tubulin Correlate with Clinical Potency.' *Scientific Reports*, 7, 9877." existed **only** in the References section (line 197) with **NO inline citation anywhere in the body** (grep-confirmed: no Craddock/terahertz/tubulin/microtubule/613/anesthetic-microtubule mention in body prose). This is the benign **variant (i) DANGLING** case from craddock-613thz-dangling-cite-sweep, a residue of the 2026-05-23 corpus 613 THz sweep.
- The removed entry's metadata was the **correct** Craddock et al. 2017 *Sci Rep* 7:9877 paper (DOI 10.1038/s41598-017-09992-7) — NOT the WRONG-PAPER variant (ii) (which mis-points at the 2015 *Current Topics in Medicinal Chemistry* paper with fabricated 2017 metadata). The distinct 2015 paper is correctly cited elsewhere ([anaesthesia-and-the-consciousness-interface](/topics/anaesthesia-and-the-consciousness-interface/)); no confusion between the two occurred here.
- Per §2.4 step 5, an orphan References entry must be cited inline or removed; since the body makes no microtubule/terahertz claim to support, removal is the lower-risk and appropriate resolution. **Correctly resolved.** No residual Craddock orphan; no fabricated metadata left behind.

### Prose-findings verdict — CORRECTLY RESOLVED (1 real fix + 2 justified NO-OPs)

The commit title says "+3 prose findings"; the refine's own changelog/todo documentation shows the substance was 1 real edit and 2 documented NO-OPs (the task carried an explicit "LICENSE TO NO-OP" on the prose points):

- **(b) Illusionism "self-undermining" rebuttal — REAL FIX, correctly calibrated.** The prior wording ("the Map sides with the anti-illusionist intuition *because the alternative is self-undermining*") begged the question against Frankish-style functional-judgement intuitions. The refine downgraded it to honest framework-boundary marking: it now supplies the illusionist's available reply (judgements retain evidential weight without phenomenal seemings, so the charge "does not refute illusionism on its own terms") and notes the Map's reliance on phenomenal seemings as itself a non-functionalist commitment, "noted as such." This is a clean Mode Three (framework-boundary marking) per [direct-refutation-discipline](/project/direct-refutation-discipline/) — bedrock declared honestly, not dressed as in-framework refutation. The Map still states its side (no over-correction into mush). No editor-vocabulary leakage in the prose. **Correctly resolved.**
- **(a) supervenience→separability bridge (line ~53-55) — NO-OP justified.** Already adequately hedged ("if truly non-physical") and forward-anchored to the zombie argument and the formal-arguments page ([functionalism-argument](/arguments/functionalism-argument/)). No drift.
- **(c) concession-convergence narrative parity (Putnam 67 / Milinkovic & Aru) — NO-OP justified.** Both readings already carry the calibration hedge ("a favoured interpretation, not one the data force" for Putnam; "the same caveat … fully compatible with physicalism" for biological computationalism). No possibility/probability slippage.

functionalism is the Map's central physicalist rival; the article engages it on its own terms (Mode Two on the sufficiency claim — "functionalism helps itself to the sufficiency claim without supplying that explanation," invoking functionalism's own standard) and marks framework-boundary disagreement honestly elsewhere. The critique does not read as refuting functionalism by fiat or via tenet-protective bracketing.

### Citation web-verify ledger (publisher of record, this session)

Re-verified the empirical/Physarum cluster (References block was modified by the drift — one line removed — so §2.4 trigger applies) plus the newest cite:

- Boisseau, Vogel & Dussutour 2016 (*Proc. R. Soc. B* 283, 20160446) — **real-correct** (Royal Society DOI 10.1098/rspb.2016.0446; title verbatim).
- Tero et al. 2010 (*Science* 327(5964), 439-442) — **real-correct** (DOI 10.1126/science.1177894; title verbatim).
- Oizumi, Albantakis & Tononi 2014 (*PLOS Comput. Biol.* 10(5), e1003588) — **real-correct** (DOI 10.1371/journal.pcbi.1003588; title verbatim).
- Nakagaki, Yamada & Tóth 2000 (*Nature* 407, 470) — **real-correct** (DOI 10.1038/35035159, PMID 11028990; cited title is the article's own title under the "Intelligence:" Brief-Communications heading).
- Milinkovic & Aru 2026 (*Neurosci. Biobehav. Rev.* 181, 106524) — **real-correct** (re-verified ScienceDirect/CoLab, DOI 10.1016/j.neubiorev.2025.106524; authors + title + venue match). Corpus-consistent (archive task notes say "(2025)" = epub year; live articles use 2026 print year).
- Morgan & Bhatt 2015 (book chapter "Anesthetic Action in *C. elegans*", in *C. elegans: Methods and Applications*, 2nd ed.) — **real-wrong-metadata SUSPECTED, deferred (see Remaining Items).** Three searches confirm the book (MMB 1327, Humana/Springer, 2nd ed., 2015, DOI 10.1007/978-1-4939-2842-2) and that Philip G. Morgan is a real C. elegans anesthesia researcher, but the article lists the book editor as "Bhatt, D.H." whereas the actual 2nd-edition editors are **Gal Haspel & Anne C. Hart**. The exact chapter title/page range was not confirmable. NOT fabrication (author + book + topic are genuine), but the editor attribution looks wrong. Pre-existing (survived 7 prior reviews), untouched by the drift, and out of scope for this drift-verification pass; over-correcting on incomplete verification risks a new error. Flagged for a dedicated follow-up.

Verified ledger inherited stable from the 06-01 publisher-of-record pass (References block unchanged except the Craddock removal): Block 1995 *BBS* 18(2):227-247; Cogitate/Melloni 2025 *Nature* 642:133-142; Melloni 2023 *PLOS ONE* 18(2):e0268577; Putnam 1967 (Capitan & Merrill eds., Univ. Pittsburgh Press); Putnam 1988 *Representation and Reality* (MIT). Not re-litigated.

### Inline ↔ References completeness

- The Craddock removal closed the one orphan the drift targeted; no new orphan created in either direction by the drift.
- **Pre-existing loose anchors (NOT drift-introduced, left in place):** Lewis 1972 and Frankish 2016 have no inline `Author YEAR` anchor (Frankish's view is discussed in the illusionism section without naming him inline); Block 1978 is loosely anchored by a single "Block" mention. These are identical pre- and post-drift (git-confirmed) and on a 8th-review converged article are below the over-correction threshold; not churned. Noted for awareness only.

### Currency / construct / leakage sweep

- `find_superlative_claims`: 0 hits — no empirical-record currency exposure.
- No banned "This is not X. It is Y." construct.
- No editor-vocabulary label leakage in body prose (grep clean for Mode One/Two/Three, classification headers, bold Evidential-status callouts, etc.).
- Length: 2971w body, soft_warning (119% of 2500 concepts soft; ~529w to 3500 hard). NOT a condense candidate. Review kept length-neutral.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded opening rejection with the description/ontology distinction.
- IIT + biological-computationalism framed as *physicalist* rejections of functional sufficiency (substrate matters without dualism) — the correct, calibration-honest framing.
- The illusionism section now models exactly the desired discipline: states the Map's side, supplies the opponent's strongest available reply, declares the bedrock honestly.
- Specification Problem (C. elegans / Physarum) presented as a *dilemma for functionalism*, never as evidence those organisms are conscious.
- Phenomenal non-compositionality argument in the Hard Problem section; Mode-Two engagement with the sufficiency claim on functionalism's own standard.
- Calibrated "What Would Challenge This View?" section separating logical refutation from motivational erosion.

### Enhancements Made

None. Converged no-op after real scrutiny of the post-refine content.

### Cross-links Added

None. The cross-link mesh is mature and reciprocated.

## Remaining Items

- **Follow-up (Medium): Morgan & Bhatt 2015 book-chapter editor attribution.** The References entry lists the book editor as "Bhatt, D.H." but the 2nd-edition (MMB 1327, 2015) editors are Gal Haspel & Anne C. Hart. A dedicated pass should (i) confirm the exact chapter title/author list and page range via Springer/PubMed, (ii) correct the editor field, or (iii) if the chapter cannot be confirmed, replace the cite with a confirmable C. elegans-anesthesia source for the "responds to volatile anesthetics similarly to vertebrates" claim (Morgan's published work amply supports it). Do NOT delete the body claim. Queued as a refine-draft task.

## Stability Notes

- **Eighth deep review (counting prior functionalism deep-reviews), zero critical issues.** The drift commit's two substantive decisions (Craddock orphan removal; illusionism downgrade to framework-boundary marking) are both correct; the "+3 prose findings" title overstated what changed (2 were documented NO-OPs), but the underlying calls are sound.
- Bedrock disagreements (functionalist multiple-realizability defence, type-B physicalist contest of conceivability→possibility, illusionist denial of phenomenal residue, Dennett/Churchland opposition) are framework-boundary standoffs and must NOT be re-flagged as critical in future reviews.
- The Morgan & Bhatt editor-attribution defect is the only open item and is pre-existing, not drift-related; it is a metadata correction, not a content or calibration problem.
- Article remains strongly converged; future reviews should be triggered by substantive content modification, not routine staleness.