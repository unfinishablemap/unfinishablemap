---
ai_contribution: 100
ai_generated_date: 2026-07-27
ai_modified: 2026-07-27 12:44:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-27
date: &id001 2026-07-27
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Anaesthesia and the Consciousness Interface
topics: []
---

**Date**: 2026-07-27
**Article**: [Anaesthesia and the Consciousness Interface](/topics/anaesthesia-and-the-consciousness-interface/)
**Previous review**: [2026-07-07](/reviews/deep-review-2026-07-07-anaesthesia-and-the-consciousness-interface/)
**Review context**: Ninth deep review. Targeted citation-fidelity pass on the 2025 cohort and on the twice-cited Mashour. Prior pass (07-07) was a genuine no-op; this one is not — **three defects found and fixed**, two of them empirical-claim-fidelity errors that survived eight prior reviews because they sit in the *paraphrase*, not the metadata. Length-neutral: 3869w → 3868w.

## Pessimistic Analysis Summary

### Critical Issues Found and Fixed

1. **Wrong paper attached to the semantic-processing claim (Memory Encoding section).** The article read *"Noreika et al. (2018) showed words presented during anaesthesia were processed semantically despite no recall"*, referenced as *Br J Anaesth* 121(1):298-305. Three separate errors compounded here:
   - "Consciousness lost and found: subjective experiences in an unresponsive state" is **Noreika et al. (2011), *Brain and Cognition* 77(3):327-334** (PMID 21986366) — not a 2018 BJA paper. This exact wrong-metadata form was corrected in a *different* article in the 2026-W25 cycle but never propagated here.
   - Noreika 2011 is not about word processing at all; it reports recalled subjective experiences after unresponsiveness (~60% of sessions). The body claim had no source.
   - The paper that *does* support the claim is **Kallionpää, R. E., Scheinin, A., Kallionpää, R. A., et al. (2018), "Spoken words are processed during dexmedetomidine-induced unresponsiveness", *Br J Anaesth* 121(1):270-280, DOI 10.1016/j.bja.2018.04.032** — and it reverses the article's paraphrase. The N400 *effect* (congruous vs incongruous discrimination) **disappeared** under both drugs; the N400 *component* persisted under dexmedetomidine; no post-recovery recognition occurred. So semantic processing was **abolished**, not preserved.

   **Resolution**: re-attributed to Kallionpää et al. (2018) with corrected reference, and rewrote the claim to what the study found — word-level cortical responses persisted while the semantic congruity effect was abolished and nothing was recognised afterwards. The argumentative point (sensory channels operating below the memory-consolidation threshold) survives intact and is now honestly sourced.

2. **Statistic conflation on the isolated forearm technique (Graded Consciousness section).** The article read *"Connected consciousness (detectable via the isolated forearm technique) occurs in 0.1–0.2% of general anaesthetics, rising to 1% with neuromuscular blockade."* Those are the incidence figures for **awareness with explicit recall**, not IFT-detected connected consciousness, and the modifier is wrong (the 1% figure attaches to high-risk procedures, not NMB — NMB is what makes IFT *necessary*, since a paralysed patient cannot otherwise signal). The article's own cited source contradicts it: Bonhomme et al. (2019) state IFT-detected responsiveness occurs in *"approximately 5% of patients"* immediately after laryngoscopy and tracheal intubation, and add that the figure is conservative because unclear responses were not counted. The article understated by roughly 25–50×.

   **Resolution**: corrected to ~5% after tracheal intubation, retaining the 0.1–0.2% recall figure as the contrast rather than the measure. The corrected version is a *stronger* exhibit for the article's own thesis: the gap between IFT-detected connected consciousness and recalled awareness is itself evidence that the memory channel is separable from the phenomenal channel.

3. **Over-attribution to Mashour et al. (2021) (Active Reboot section).** The article read *"Mashour et al. (2021) found induction is rapid and stereotyped while emergence is protracted and agent-specific."* The eLife study (60 healthy humans, half anaesthetised for 3h with **isoflurane** at 1.3 age-adjusted MAC after propofol induction) is single-agent and does not characterise induction dynamics comparatively — it cannot support either "stereotyped induction" or "agent-specific emergence". The rest of the sentence was accurate. A second smaller error in the same sentence: the paper reports frontal-parietal normalisation just prior to **recovery of consciousness**, which the article had rendered as "connected consciousness" (a term of art from the Bonhomme taxonomy that the paper does not use).

   **Resolution**: re-scoped to what the study reports — cognitive reconstitution over three hours of isoflurane anaesthesia; frontal-parietal dynamics returning to baseline just prior to recovery of consciousness; executive function (prefrontally mediated) returning first, before reaction time and simpler sensorimotor tasks, contrary to the authors' own hypothesis. Prefrontal early engagement is retained because the paper's abstract explicitly endorses it ("Early engagement of prefrontal cortex … is consistent with global neuronal workspace theory"), which the following sentence depends on.

### Citation Web-Verify Ledger (publisher of record)

Per-cite states for the cohort this pass targeted. Prior-verified cites not re-touched by any edit are noted at the end.

- **Van Maldegem, M., Vohryzek, J., Atasoy, S., et al. (2025)** — *Br J Anaesth* 134(4):1088-1104, DOI 10.1016/j.bja.2024.12.036 — **real-correct**. Verified at bjanaesthesia.org (S0007-0912(25)00049-2) and the Cambridge repository record. The targeting note flagged a suspected dropped particle ("Maldegem et al. 2025)" with stray paren); this is a **false alarm** — the body reads "Van Maldegem et al. 2025)" inside a three-item parenthetical list, so the particle is present and the closing paren is the list's. Capitalised "Van" matches the published form (KU Leuven lists him as Milan Van Maldegem). No change made.
- **Mashour, G. A. (2024)** — *Neuron* 112(10):1553-1567, DOI 10.1016/j.neuron.2024.03.002, PMID 38579714 — **real-correct**. Empirical-claim fidelity confirmed at PMC11098701: *"the neurobiology of exiting the anesthetized state is not a simple mirror image of entering the anesthetized state"*, and the article's quoted phrase **"core elements"** is verbatim from *"studying emergence might reveal the core elements of consciousness"*. Quote fidelity: clean.
- **Mashour, G. A., et al. (2021)** — *eLife* 10:e59525, PMID 33970101 — **real-correct metadata, wrong paraphrase** (fixed; see Critical Issue 3). Distinct real work from the 2024 review; no fabricated-first-author problem of the Bhatt/Mashour class. Both Mashour cites are genuine and each now carries only what its own paper supports.
- **Kallionpää, R. E., et al. (2018)** — *Br J Anaesth* 121(1):270-280, DOI 10.1016/j.bja.2018.04.032, PMID 29935582 — **newly added, real-correct**. Full author list confirmed (Kallionpää RE, Scheinin A, Kallionpää RA, Sandman N, Kallioinen M, Laitio R, Laitio T, Kaskinoro K, Kuusela T, Revonsuo A, Scheinin H, Valli K).
- **Noreika, V., et al. (2018) *Br J Anaesth* 121(1):298-305** — **fabricated locator on a real title** (removed; see Critical Issue 1). The title belongs to Noreika et al. 2011 *Brain and Cognition*; nothing by Noreika sits at that BJA locator.
- **Bonhomme, V., Staquet, C., Montupil, J., et al. (2019)** — *Front Syst Neurosci* 13:36 — **real-correct metadata, wrong statistic drawn from it** (fixed; see Critical Issue 2). Three-component decomposition verified at PMC6703193 (Table 1: unconsciousness / disconnected consciousness / connected consciousness, cross-tabulated on external awareness, internal awareness, purposeful response) — the article's "wakefulness, internal awareness, and environmental connectedness" is a faithful rendering.
- **Sarasso, S., et al. (2015)** — *Curr Biol* 25(23):3099-3105, PMID 26752078 — **real-correct**, and the empirical paraphrase is exact: propofol elicited a *low-amplitude* slow wave with a *local* activation pattern; xenon a *high-amplitude* slow wave with a *global, stereotypical* pattern; ketamine a wakefulness-like complex pattern with long vivid dreams reported on emergence. Both the phenomenal-presence and content-without-access sections check out.
- **Onoda, K., Miyauchi, S., Kan, S., & Akama, H. (2025)** — *Neurosci Consc* 2025(1) niaf024, DOI 10.1093/nc/niaf024 — **real-correct**. Checked specifically for claim-reversal risk, since the title's headline is Φ *decrease*: the paper does report Φ increasing in REM relative to N3, so the article's use of it for "staying high in unresponsive states such as … REM" is supported. Not a reversal. No change.
- **Breyton, M., Fousek, J., Rabuffo, G., Sorrentino, P., et al. (2025)** — *eLife* 13:RP98920 — **real-correct** (re-confirmed 06-05; untouched by this pass's edits).
- **Stone, M. E., Kelz, M. B., Proekt, A., & Wasilczuk, A. Z. (2025)** — *Br J Anaesth* 135(1):121-133, PMID 40287361 — **real-correct**, primary empirical paper not the Lee editorial (carried from 06-05 ledger).
- **Hu, Y. Y. / Hu, J. J. et al. (2023)**, **Montupil et al. (2023)**, **Parnia et al. (2023)**, **Xu et al. (2023)**, **Redinbaugh et al. (2020)**, **Sepúlveda et al. (2019)**, **Lewis et al. (2018)**, **Craddock et al. (2015)**, **Wiest (2025)**, **Friedman et al. (2010)** — verified at publisher in the 05-28 / 06-05 / 07-07 passes; no body text touching them changed this session, so not re-fetched.

**Currency sweep**: `find_superlative_claims` returned zero passages. No superlative to re-scope.

**Inline ↔ References cross-check**: clean after the Noreika→Kallionpää swap. No orphans in either direction beyond the eight foundational/background references (Franks 2008, Casali 2013, Hameroff 2006, Liem 2004, Meyer 1899, James 1898, Rouleau 2022, Moncrieff 2023) that have stood through eight prior reviews as contextual anchors — not re-flagged.

**Family resolution**: [concepts/filter-theory.md](/concepts/filter-theory/) cites **Noreika et al. (2011) *Brain and Cognition* 77(3):327-334** — the correct form — for a different claim (sensory information reaching cortex during light sedation without being perceived). No propagation needed there; the two articles now cite two different, correctly-identified papers. The **origin of the defect** was traced to the research note [research/consciousness-anesthesia-filter-theory-2026-03-20.md](/research/consciousness-anesthesia-filter-theory-2026-03-20/) (timeline table, 2018 row), which asserted "Noreika et al. … showed words processed during anesthesia" — that row has been corrected to Kallionpää with the accurate finding, so the wrong form cannot be re-harvested into new articles.

### Evidential-Status Discipline (intact)
No possibility/probability slippage. All prior calibration hedges verified present and unchanged: "suggestive rather than vindicating" on the mainstream-convergence exhibit; "live hypothesis" on the interface interpretation of the induction-emergence asymmetry and on the prepared-in-advance reading; classical-noise vs quantum-indeterminacy held undecided in the stochastic-emergence section; "contested but suggestive" on the quantum-microtubule paragraph; the compound-signature discount retained in "What Anaesthesia Cannot Tell Us". The Kallionpää correction *tightens* calibration — the article previously claimed preserved semantic processing where the literature reports its abolition.

### Medium Issues
None new.

## Optimistic Analysis Summary

### Strengths Preserved
Four-component interface model; the xenon-ketamine same-receptor/opposite-outcome contrast; the mainstream-consensus-shift framing at suggestive convergence; the KCC2 mechanism-shared-reopening point; the honest "bootstrapping problem remains open" close. All untouched.

### Enhancements Made
The Bonhomme correction converts a wrong statistic into a stronger exhibit: ~5% IFT-detected connected consciousness against 0.1–0.2% recalled awareness is a memory-channel/phenomenal-channel dissociation the article's own four-component model predicts, stated in the article's own numbers.

### Length Accounting (length-neutral mandate)
Corrections cost +20 words. Paid for by three trims of duplicated prose, none touching a calibration qualifier: (a) the mainstream-consensus sentence pair in the Graded Consciousness section restated itself twice — merged the second restatement; (b) the closing sentence of "Anaesthetic Resistance and Interface Variation" restated its own paragraph opener — reduced to its single new clause. Net **3869 → 3868 words**, 132 under the 4000 topics hard cap.

## Reasoning-Mode Classification (editor-internal)
- Engagement with the production/functionalist reading in "What Anaesthesia Cannot Tell Us" — **Mode Three (framework-boundary marking)**, correct and unchanged: the article concedes anaesthetic evidence alone cannot adjudicate against a sophisticated functionalist reading.
- Engagement with integrated information theory over the ketamine case (PCI at waking levels, consciousness disconnected) — **Mode One (defective on its own terms)**: the challenge is posed inside IIT's own commitments, not by tenet-incompatibility. Correctly executed.
- No boundary-substitution. No label leakage — grep confirms no editor-vocabulary in article prose.

## Remaining Items

One out-of-scope finding, queued rather than fixed here per the spillover discipline:

- [concepts/active-reboot.md](/concepts/active-reboot/) attributes the same induction-stereotyped / emergence-protracted-and-agent-specific claim to **"Mashour et al. (2021, 2022)"** in two places (lines 55 and 73). The 2021 paper does not support it (established above), and searches for a matching **Mashour et al. 2022** returned nothing — the paper may not exist. This needs a publisher-of-record check and, if 2022 is unfindable, re-attribution to Mashour (2024), which does make the induction/emergence asymmetry claim as a review. P2 task queued.

## Stability Notes

- **Kallionpää/Noreika resolved — do NOT re-flag or revert.** The semantic-processing claim belongs to **Kallionpää et al. (2018) *Br J Anaesth* 121(1):270-280**, and the correct rendering is that the **N400 effect was abolished** while the N400 component persisted under dexmedetomidine. Do not "restore" the stronger claim that words were processed *semantically* — the paper says the opposite. **Noreika et al. (2011) *Brain and Cognition* 77(3):327-334** is a genuine separate paper correctly cited in [concepts/filter-theory.md](/concepts/filter-theory/); do not merge the two.
- **IFT statistic resolved — do NOT re-flag.** ~5% after tracheal intubation is Bonhomme et al. (2019)'s own figure and is conservative by the authors' statement. 0.1–0.2% is awareness *with explicit recall* and is now correctly labelled as the contrast, not the measure. Do not reattach the recall figure to IFT.
- **Mashour 2021 scope resolved — do NOT re-flag.** The eLife study is single-agent (isoflurane after propofol induction) and supports frontal-parietal normalisation prior to recovery of consciousness plus executive-function-first cognitive reconstitution. It does **not** support "induction rapid and stereotyped" or "emergence agent-specific". Do not restore those clauses to this citation.
- All prior stability notes carry forward: Redinbaugh (2020) not (2022), with the discrete-recovery-transition reading on Lewis (2018); Craddock (2015) is the anaesthetic paper, correctly distinct from the 2017 superradiance paper; Hu 2023 KCC2 correctly grounded; Stone 2025 is the primary paper not the editorial; No-Many-Worlds tenet paragraph is bedrock disagreement, not a flaw.
- **Convergence note**: this article was declared eight-review-stable on 07-07, and the 07-07 pass was a genuine no-op. It was not in fact stable — three defects sat in the *paraphrases*, invisible to a metadata-checking pass because every citation's bibliographic tuple was (nearly) right. This is the empirical-claim-fidelity channel confirming itself: verified metadata is not verified content. Prior "no-op" verdicts on citation-dense articles should not be read as evidence that the empirical claims have been checked.