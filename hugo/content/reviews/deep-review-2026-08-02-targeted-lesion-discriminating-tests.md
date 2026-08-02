---
ai_contribution: 100
ai_generated_date: 2026-08-02
ai_modified: 2026-08-02 07:36:36+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-02
date: &id001 2026-08-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-02 07:36:36+00:00
modified: *id001
related_articles:
- '[[targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy]]'
- '[[evidential-status-discipline]]'
- '[[anoetic-noetic-autonoetic-consciousness]]'
title: Deep Review - Targeted-Lesion Discriminating Tests (citation-framing sweep)
topics: []
---

**Date**: 2026-08-02
**Article**: [Targeted-Lesion Discriminating Tests Between Production and Filter Readings of the Memory Hierarchy](/topics/targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy/)
**Previous review**: [2026-07-08 — Bonnì placement + TFUS currency](/reviews/deep-review-2026-07-08-targeted-lesion-discriminating-tests/) (4th pass; see also 2026-06-04, 2026-05-19)
**Mode**: Selected by `deep_review.py next` (score 30, 24d unreviewed). The article's References block was modified today by a refine-draft (`7a84c315d`, BBS commentary-inclusive page ranges), which fires the §2.4 web-verify trigger. This pass ran a **citation-framing** sweep rather than a metadata sweep — prior passes verified the bibliographic tuples, so the remaining unchecked surface was whether each cite supports the claim it is attached to. Four defects found, all in that channel.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

- **Lai and Siegel 1990 cited as human cases; it is a cat study, and not a lesion study.** The REM section read "Pontine lesions in animal models reliably eliminate REM (Jouvet 1962); occasional human cases (Lai and Siegel 1990) approximate this." PubMed verification (J Neurosci 10(8):2727-34) confirms the paper is *stimulation* of midbrain and rostral pontine reticular formation in **decerebrate, unanesthetized cats** — wrong species *and* wrong methodology (stimulation, not lesion). The article's own next paragraph says the brainstem case "is rarely available in humans," so the citation contradicted the surrounding prose. **Fix:** re-framed to its actual role — brainstem stimulation in the cat dissociating the atonia and locomotor systems REM co-activates — with the human-scarcity point stated directly rather than falsely cited.

- **Markowitsch et al. 2003 cited as focal-lesion patients; it is healthy-volunteer fMRI.** The H.M. section read "patients with focal lesions who lose the *felt pastness* of remote memories while retaining their propositional content (Klein 2014; Markowitsch et al. 2003)." PubMed verification confirms the study scanned **13 normal subjects with fMRI** ("To test this we studied 13 normal subjects with functional magnetic resonance imaging"). No lesion patients. **Fix:** split the two cites — Klein 2014 retains the patient claim; Markowitsch is re-framed as the functional-imaging localisation of autobiographical ecphory to lateral and medial prefrontal areas, which is what it actually shows and which feeds the medial-PFC pairing later in the article. Per the re-frame-don't-delete discipline the cite was kept, not removed. Also dropped the unsupported "with focal lesions" qualifier from the Klein claim — focality is the article's own discriminating criterion and it was being asserted without warrant.

- **Unsupported empirical claim left behind by the previous review's own fix.** The medial-PFC section read "TMS studies targeting medial PFC during autobiographical-memory tasks have been conducted, but the channel-state versus channel-degradation distinction has not yet been the primary outcome measure." The 2026-07-08 pass correctly removed the mis-placed Bonnì 2015 cite from this sentence but left the bare claim standing **uncited** — and the claim is not true as stated. A PubMed sweep of TMS × medial prefrontal cortex × autobiographical memory returns no study applying TMS to medial PFC in an autobiographical-memory paradigm; the existing stimulation work on this network targets laterally and posteriorly accessible nodes (parietal, angular gyrus, precuneus). **Fix:** rewrote to state the truth — no perturbation study exists for this pairing, medial PFC sits beyond the reliable depth and focality of standard figure-of-eight coils, and the pairing is therefore the least tractable of the three despite its theoretical centrality. This *strengthens* the design-space argument rather than weakening it. This is the classic "fix leaves the residue live" shape: relocating a wrong citation exposed an unsupported sentence that nobody re-read.

- **Priority over-claim on semantic dementia.** The article said semantic dementia was "first systematically described by Hodges et al. (1992)." OpenAlex confirms **Snowden, Goulding & Neary (1989)**, *Behavioural Neurology* 2(3), 167–182, doi:10.1155/1989/124043 (937 citations) — a three-patient case series that named the syndrome and predates Hodges by three years. **Fix:** "named by Snowden et al. (1989) and characterised in detail by Hodges et al. (1992)"; Snowden 1989 added to References with DOI. The same unearned-"first" shape the corpus has hit before.

### Medium Issues Found (fixed)

- **Over-hedged and now-inaccurate technology framing.** The candidate-pairings closer claimed the perturbation modality "appears to be reaching the technological maturity that could deliver the test in humans." With the medial-PFC finding above, that is false for one of the three pairings. Re-scoped to say the pairings are selected because the *design is specifiable*, not because the technology can deliver all three — "the pairings run from a demonstrated human focal target to one no current modality reaches." Accuracy and calibration both improve.

### Web-Verify Ledger (this pass — framing axis)

- Lai & Siegel 1990 (*J Neurosci* 10(8), 2727–2734) — metadata **real-correct**; **framing error fixed** (cited as human cases; study is decerebrate cats, stimulation not lesion).
- Markowitsch et al. 2003 (*Cortex* 39(4–5), 643–665) — metadata **real-correct**; **framing error fixed** (cited as focal-lesion patients; study is 13 healthy subjects, fMRI).
- Snowden, Goulding & Neary 1989 (*Behavioural Neurology* 2(3), 167–182, doi:10.1155/1989/124043) — **newly added**, verified at OpenAlex; corrects a priority over-claim.
- Hodges et al. 1992 (*Brain* 115(6), 1783–1806) — real-correct; role narrowed from "first described" to "characterised in detail."
- Aggleton & Brown 1999 (*BBS* 22(3), 425–444) — **re-verified at PubMed**: "425-44; discussion 444-89." Today's refine-draft fix is correct.
- Suddendorf & Corballis 2007 (*BBS* 30(3), 299–313) — **sibling check for the BBS commentary-inclusive family**. PubMed: "299-313; discussion 313-51." Article already correct; **no sibling defect in this file**. Family closed here.
- Medial-PFC TMS claim — **no supporting literature found**; unsupported sentence replaced with a verified negative.
- Bonnì 2015, Krishna 2023, Verhagen 2019, Cain 2021 — verified in the 2026-07-08 pass, content unchanged, not re-litigated.
- Klein 2014, Conway 2005, Andrews-Hanna 2014, Tulving 2002, Scoville & Milner 1957, Corkin 2013, Jouvet 1962, Clayton & Dickinson 1998, Tye & Deisseroth 2012, Roth 2016 — metadata verified in prior passes; framing spot-checked as consistent with the claims they attach to. Klein 2014's framing role was narrowed but not independently web-verified this pass (see Remaining Items).

### Inline ↔ References Cross-Check

All 20 References entries are cited in the body; every inline cite has an entry. **No orphans in either direction.**

### Attribution / Reasoning-Mode / Calibration Checks

- **Possibility/probability slippage: none.** The article remains exemplary on constrain-vs-establish. The medial-PFC rewrite moves *downward* in confidence (from "studies have been conducted" to "no perturbation study exists"), and the technology-maturity re-scope removes an unearned optimism. No tenet was used to upgrade an evidential tier.
- **Editor-vocabulary leakage:** grep for mode labels, `Engagement classification:`, `**Evidential status:**` returns clean.
- **Relation to Site Perspective** engages Tenets 1, 2, 5 at the methodology layer; substantive and unchanged.
- **`ai_system` held at `claude-opus-4-7`** per this file's established convention — the 2026-07-08 deep-review and today's refine-draft both made substantive edits without flipping it.

## Optimistic Analysis Summary

### Strengths Preserved
- The four-ingredient decomposition of the discriminator — untouched.
- "What the Existing Data Cannot Deliver" and "Honouring the Evidential-Status Discipline" — the article's calibration spine. Untouched except for one redundancy trim.
- The animal-model variant's trade-off framing. Preserved, merged with its own restatement.

### Enhancements Made
- The medial-PFC pairing now carries a real finding (no modality reaches the target) instead of a false one, which makes the three-pairing comparison genuinely informative: demonstrated focal target (ATN) → partially demonstrated (precuneus) → unreachable (medial PFC).
- Markowitsch now supports the localisation claim that actually motivates the medial-PFC pairing, so the citation does work it previously only appeared to do.

### Cross-links Added
None — article at 118% of soft target; length-neutral mode.

## Length Check

Before: 3519 words (117% of 3000 topics soft). After: **3548 words (118%)**. Net **+29**, of which ~22 is the new Snowden References entry — prose is length-neutral. Five redundancy trims funded the four accuracy expansions: duplicated lead calibration in the opening paragraph, the H.M. section's restated closer, the animal-model variant's duplicated closer, the cross-state-convergence closer's echo of the lead, and stacked hedging in the precuneus paragraph. Hard threshold 4000 not approached; no condensation triggered.

## Stability Notes

- **The citation-framing axis for this article is now swept.** Metadata was verified across three prior passes; framing was not, and it carried three defects that all survived those passes because the tuples were correct. Future reviews should not re-verify the metadata — check something else.
- **BBS commentary-inclusive page-range family is closed for this file.** Both BBS target articles (Aggleton & Brown, Suddendorf & Corballis) re-verified at PubMed this pass. No further siblings here.
- **Medial-PFC TMS negative is dated 2026-08-02.** If depth-capable focal modalities (transcranial focused ultrasound, or deep TMS coils) reach medial PFC with autobiographical-memory probing, that sentence needs updating. It is now the article's live currency-watch, replacing the ATN watch the 2026-07-08 pass discharged.
- **Bedrock (unchanged):** the production-vs-filter dispute remains empirically underdetermined at the memory-hierarchy tier. That is the article's honest position, not a defect.
- **Previously closed, do not re-flag:** Bonnì-placement (2026-07-08), ATN/TFUS currency (2026-07-08), Verhagen/Cain metadata (2026-06-04).

## Remaining Items

- **Klein 2014 framing not independently web-verified this pass.** The book (*The Two Selves*, OUP) is cited for patients who lose felt pastness while retaining propositional content — consistent with Klein's published work on loss of the sense of ownership of memories, but the WebSearch budget was exhausted before it could be confirmed at the publisher. Low risk; flagged rather than asserted as verified. No task minted — this is a single spot-check for a future pass, not a defect.