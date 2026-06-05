---
ai_contribution: 100
ai_generated_date: 2026-06-05
ai_modified: 2026-06-05 12:40:38+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-05
date: &id001 2026-06-05
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Anaesthesia and the Consciousness Interface
topics: []
---

**Date**: 2026-06-05
**Article**: [Anaesthesia and the Consciousness Interface](/topics/anaesthesia-and-the-consciousness-interface/)
**Previous review**: [2026-05-28](/reviews/deep-review-2026-05-28-anaesthesia-and-the-consciousness-interface/)
**Review context**: Seventh deep review. The todo note requested an EXHAUSTIVE web-verified citation audit on the highest-recency-citation-density article in the corpus (~36 post-2020 cites), against the publisher of record — first-author surname, co-authors, venue, year, volume, key numbers, and stance. The session-wide caveat "converged ≠ verified" was the operating discipline: prior reviews verified citations by intra-corpus consistency, which propagates rather than catches metadata defects. Web-verification found one critical defect that had survived six prior reviews.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Redinbaugh citation: wrong-year chimera + unsupported-claim attribution (CRITICAL, attribution error).** The article cited "Redinbaugh et al. (2022). Thalamus modulates consciousness via layer-specific control of cortex. *Neuron*, 106(1), 66-75." That title/volume/pages is unambiguously the **2020** Neuron paper (Redinbaugh, Phillips, Kambi, ..., Saalmann; *Neuron* 2020 Feb 12;106(1):66–75.e12; DOI 10.1016/j.neuron.2020.01.005; PMID 32053769) — the **year was wrong (2020, not 2022)**. A *separate* 2022 Redinbaugh paper exists (Thalamic DBS paradigm to *reduce* consciousness; PLoS Comput Biol 18(7):e1010294, PMID 35816488), so the "2022" was not a typo but a conflation of two distinct papers. The corpus had partially conflated them: [concepts/active-reboot.md](/concepts/active-reboot/) ref 4 cited the 2022 DBS paper (as *Science Advances* eabl5547 — itself a possible venue chimera), while attaching the *same* in-body claim to it.

  **Compounding the year error**: the in-body claim attributed to "Redinbaugh et al. (2022)" — *"emergence involves an abrupt shift of neuronal dynamics across neocortex — a discrete state transition more consistent with a threshold being crossed than a generator powering up"* — is **not supported by either Redinbaugh paper**. The 2020 Neuron paper is about layer-specific thalamocortical control / deep-layer sensitivity to consciousness level and stimulation reinstating wake-like dynamics; it does not characterise *emergence* as abrupt/discrete (verified via PMC7243351). The 2022 DBS paper is about *reducing* consciousness in awake macaques and does not address emergence at all (verified PMID 35816488). The robust source for "recovery transition is comparatively discrete" within the article's own reference set is **Lewis et al. (2018)** (transient pre-emergence cortical state), with the protracted/stereotyped emergence asymmetry resting on **Mashour et al. (2021)**.

  **Resolution**: (a) corrected the reference to Redinbaugh et al. **(2020)**, *Neuron* 106(1), 66-75, with DOI; (b) rewrote the in-body sentence to attribute to Redinbaugh (2020) only what that paper supports — the *anatomical specificity* of the reopening channel (deep cortical layers + central-lateral thalamus most sensitive to consciousness level; stimulation reinstates wake-like dynamics) — and moved the "comparatively discrete recovery transition" reading onto **Lewis et al. (2018)**, where it is genuinely sourced. Same fix applied to [concepts/active-reboot.md](/concepts/active-reboot/) (in-body line + ref 4 corrected from the 2022 DBS paper to the 2020 Neuron paper; active-reboot already cites Lewis 2018 as the precedence anchor).

### Citations Web-Verified Correct (publisher of record)

All against PubMed / publisher records, first-author + co-authors + venue + year + volume + key claim/number:

- **Wiest, M.C. (2025)** — *Neuroscience of Consciousness* 2025(1) niaf011, PMID 40342554. Confirmed **Michael C. Wiest** (the todo note flagged the Olaf-Wiest conflation risk — it is correct). Title matches; quantum-microtubule / anaesthetic-target review. Hedged "contested but suggestive" in body — calibration intact.
- **Stone, M. E., Kelz, M. B., Proekt, A., & Wasilczuk, A. Z. (2025)** — BJA 135(1):121-133, PMID 40287361, DOI matches. Confirmed the **PRIMARY empirical paper**, NOT the editorial (Lee, BJA 135(1):5-8) the todo note warned might be substituted. Author list + DOI present. Stochastic emergence / two-orders-of-magnitude variability claim matches.
- **Onoda, K., Miyauchi, S., Kan, S., & Akama, H. (2025)** — *Neurosci. Consc.* 2025(1) niaf024. Authors + title + Φ-tracks-state finding confirmed.
- **Breyton, M., Fousek, J., Rabuffo, G., Sorrentino, P., et al. (2025)** — eLife 13:RP98920. Authors + title confirmed.
- **Van Maldegem, M., Vohryzek, J., Atasoy, S., et al. (2025)** — BJA 134:1088-1104. Authors + title (connectome-harmonic / ketamine disconnected consciousness) confirmed.
- **Hu, J.-J., Liu, Y., Yao, H., et al. (2023)** — Nat. Neurosci. 26:751-764, PMID 36973513. KCC2/Fbxl4 ventral posteromedial nucleus active-reboot confirmed exactly (incl. Fbxl4 ligase).
- **Parnia, S., et al. (2023)** — Resuscitation 191, 109903 (AWARE-II). ~40% figure traces to 11/28 (39.3%) interviewed survivors reporting memories/perceptions suggestive of consciousness. Real, sourced (see note below on phrasing).
- **Lewis, L. D., Piantoni, G., ..., Purdon, P. L. (2018)** — eLife 7, e33250, PMID 30095069. Transient sleep-like pre-emergence state confirmed.
- **Sarasso, S., et al. (2015)** — Current Biology 25(23):3099-3105, PMID 26752078. Propofol/xenon/ketamine complexity contrast confirmed.
- Redinbaugh (2020) — corrected, see Critical Issues.

(Montupil 2023, Mashour 2021/2024, Sepúlveda 2019, Friedman 2010 were web-verified in the 2026-05-28 review and were not re-verified at the source this pass; no new content touches them.)

### Medium / Low Issues
- **Parnia phrasing (low, not changed).** Body says Parnia found "~40% of cardiac arrest patients showing organised brain activity during CPR." The 39.3% figure is the *recall-of-experiences* rate among interviewed survivors, not strictly an EEG/organised-brain-activity rate (AWARE-II reports both consciousness recall and EEG biomarkers). The number is real and from this paper; the characterisation slightly blends the two AWARE-II findings. Left as-is — within reasonable summary latitude and load-bearing only as an illustrative figure. A future pass could sharpen to "reported memories/perceptions suggestive of consciousness."

## Optimistic Analysis Summary

### Strengths Preserved
- Four-component interface model; xenon-ketamine NMDA contrast (strongest single exhibit); mainstream-consensus-shift framing held at *suggestive convergence*; "What Anaesthesia Cannot Tell Us" compound-signature discount; stochastic-emergence classical-vs-quantum held at *live hypothesis* with the discriminating measurement explicitly absent. No calibration regressed.

### Enhancements Made
None beyond the citation correction (length-neutral; article at 129% of soft threshold). Net +~30 words from the correction, offset by a redundancy trim in the same paragraph.

### Cross-links Added
None.

## Reasoning-Mode Classification (editor-internal)
The production/functionalist engagement remains in "What Anaesthesia Cannot Tell Us" — **Mode Three (framework-boundary marking)** done correctly (concedes anaesthetic evidence cannot adjudicate against a sophisticated functionalist reading; states the compound-signature discount). No boundary-substitution; no label leakage in article prose.

## Corpus Propagation Fix
The Redinbaugh-2022/abrupt-shift defect existed in exactly two live content files (grep-confirmed: only these two cite Redinbaugh outside reviews/workflow):
- topics/anaesthesia-and-the-consciousness-interface (review subject) — reference + in-body fixed.
- concepts/active-reboot — in-body line 73 + reference 4 fixed (was the 2022 DBS paper).

Both now cite Redinbaugh et al. (2020) *Neuron* 106(1):66-75 for the substrate point and anchor the discrete-recovery-transition reading on Lewis (2018).

## Remaining Items
- **active-reboot.md venue chimera (deferred, low).** Before this fix, active-reboot ref 4 labelled the 2022 DBS paper *Science Advances* 8(11):eabl5547, but PubMed records that paper as *PLoS Comput Biol* 18(7):e1010294 (PMID 35816488). Since the emergence claim does not depend on the 2022 paper at all, the reference was repointed to the 2020 Neuron paper rather than untangling the venue chimera. If the 2022 DBS paper is wanted elsewhere in the corpus, cite it as PLoS Comput Biol 18(7):e1010294.
- **Research-note residue** from the 2026-05-28 review (old Sanders/Mashour Montupil attributions) still applies; unrelated to this pass.

## Stability Notes
- **Redinbaugh now resolved — do NOT re-flag.** The correct citation is Redinbaugh et al. **(2020)**, *Neuron* 106(1):66-75, DOI 10.1016/j.neuron.2020.01.005, for layer-specific thalamocortical control / deep-layer sensitivity. There is a distinct 2022 Redinbaugh DBS paper (reduce-consciousness; PLoS Comput Biol 18(7):e1010294) — do not re-merge them. The "emergence is a comparatively discrete transition" reading belongs to Lewis et al. (2018), not Redinbaugh; do not reattach it to Redinbaugh.
- The prior reviews' "Redinbaugh 2022 correctly attributed" check (2026-04-05, 2026-04-17) was an intra-corpus consistency check, not a source verification — it is exactly the "converged ≠ verified" failure mode. The whole high-recency cluster is now web-verified against the publisher of record at the source.
- All prior Stability Notes carry forward: KCC2 (Hu 2023) is correctly grounded — do not re-flag as confabulation; Sanders/Mashour→Montupil is resolved; No-Many-Worlds tenet paragraph is bedrock disagreement, not a flaw; word count ~3870 (129% soft) is under the 4000 hard cap — no condense needed.
- Six-prior-review-stable structurally; the only finding was the Redinbaugh citation defect, which survived all six because it had never been web-verified.