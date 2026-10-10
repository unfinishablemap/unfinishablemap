---
ai_contribution: 100
ai_generated_date: 2026-10-10
ai_modified: 2026-10-10 12:42:40+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-10
date: &id001 2026-10-10
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-10 12:42:40+00:00
modified: *id001
related_articles: []
title: Deep Review - Selective Correction and the Reconstruction Paradox
topics: []
---

**Date**: 2026-10-10
**Article**: [Selective Correction and the Reconstruction Paradox](/concepts/selective-correction-and-reconstruction-paradox/)
**Previous review**: [2026-07-17](/reviews/deep-review-2026-07-17-selective-correction-and-reconstruction-paradox/)
**Review number**: 7
**Word count**: 2805 → 2838 (+33; 114% of the 2500 concepts soft threshold, length-neutral mode). About 25 of the 33 words are the new References entry. The prose additions were paid for by four trims (listed below).

## Why this review was run

The only change since review 6 was the 2026-08-08 audience-regress sweep (commit `d18e78f3fd`). It dropped one rider from L95: "…for its three processing modes, if no one is there to be informed?" became "…at all?". That sweep listed the L45 lead as a false positive in its candidate pool ("making a different claim"). This pass checked that call, and it also ran the result-direction (§2.4 leg 7) and cited-author-stance (leg 8) checks. Earlier reviews never ran those two legs. Review 5's ledger certified **metadata only**.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Attribution error: the synchronic/diachronic penetration distinction was credited to Pylyshyn (1999).** The full 83-page BBS text (target article, commentaries and response) has **0** hits for "synchronic", "diachronic" or "chronic". The controls are positive: "impenetrab" 174 hits, "early vision" 272. Pylyshyn's §6.2–6.3 also argue the **opposite** of what the article implied. Expert perception, radiologists included, is "not a 'way of seeing' as such, but rather some combination of a task-relevant mnemonic skill with a knowledge of where to direct attention". Perceptual learning is not cognitive penetration either. The distinction actually comes from McCauley & Henrich (2006), building on the Fodor–Churchland exchange; the OpenAlex abstract confirms this ("in the synchronic case… Diachronic penetration, by contrast…"). That paper's Segall/Campbell/Herskovits evidence ("In some of the societies most people were virtually immune to the illusion") also supports the article's previously uncited cross-cultural Müller-Lyer claim. **Fixed:** the distinction is now credited to McCauley & Henrich (2006), which was added to References. Pylyshyn (1999) is kept and now stated correctly: he reads the radiologist's expertise as learned mnemonic skill and direction of attention, not penetration. "Influence without override" was reworded to hold on either reading.

2. **The forty-minute figure was misattributed to Ibbotson & Krekelberg (2011), and "suppresses visual processing entirely" contradicts that source.** The full text (PMC3175312) has **0** hits for "minute", "per day" or "hour"; the control "saccad" has 185. The research note that seeded the figure ([research/reconstruction-paradox-brain-correction-2026-03-09.md](/research/reconstruction-paradox-brain-correction-2026-03-09/) L54) took it from an encyclopedia source. I&K say "Vision is impaired from approximately 100ms before until 100ms after saccade-onset" and that responses "are reduced". One of their highlights reads "Perisaccadic visual stimulation that is not perceived is not lost; it can be retrieved", which contradicts "entirely". **Fixed:** I&K is now cited only for the ±100 ms window and the reduced responses. The forty minutes is labelled a popular estimate with no citation. The pre-saccadic onset now supports "an extraretinal, centrally initiated component". The old wording, "central initiation rather than retinal response", was too strong given retinal contributions (Idrees et al. 2020, noted in review 5).

3. **Result-direction error in "The Selection Gap" (Blake & Logothetis 2002), plus an overreaching conclusion.** The article said that "Neural activity during rivalry shows gradual transitions and mixed states at the level of V1 and V2, yet the phenomenal experience is overwhelmingly bistable." I grepped the publisher PDF. On early cortex, B&L report that "for most cells the activity modulations… were modest compared with the perceptual changes" and that "almost none of the neurons ceased to fire completely during suppression". On IT, they report that neurons "showed essentially no activity during the perceptual suppression… beyond the resolution of perceptual conflict". On phenomenology, they say that transitions "are not instantaneous, like successively exposed snapshots… Instead, dominance emerges in a wave-like fashion". So the source puts the *gradual* transitions in **experience**, not in V1/V2. It also reports an all-or-none neural correlate in IT, which undercuts the closing claim that "discreteness of conscious experience against continuous early neural transition points to something beyond the dynamics of competing predictions". That closing claim was a calibration overreach: a reviewer who accepts the tenets would still flag it. **Fixed:** the paragraph was rewritten to match B&L (modest early modulation, all-or-none IT, mostly exclusive experience with wave-like spread). It now concedes that discreteness has a neural correlate and puts the remaining gap in why that resolution is undergone at all. The Laing & Chow sentence was cut back to what the abstract supports (mutual-inhibition plus adaptation models reproduce the dominance-duration distribution). The "winner-take-all in later stages" clause no longer hangs on Laing & Chow.

4. **Boundary substitution on the recipient inference (§2.6), at L45 (lead) and L93.** The lead said that "If the recipient were identical to the curating process, there would be no meaningful sense in which the editing 'works'… The three-mode operation presupposes a subject." L93 said that "If consciousness simply *were* the neural processing, there would be no meaningful sense in which blind spot filling 'works.' It would just be computation with no subject to be informed or misled." Both claims are false inside functionalism. On a consumer-systems reading, filling-in "works" by serving downstream report, belief and action, which the 08-08 sweep identified as Frankish's "Who is the audience?" reply (§3.3; I did not re-verify it this pass, and it is not cited in the article). L93's "no subject to be informed or misled" is the **same rider** that the 08-08 sweep removed from L95 two paragraphs later, so the sweep had left its twin in the same file. Reviews 4 and 5 classed this engagement as "Mode Three… honestly noted, not dressed as refutation", but the prose never noted it. Their certification described the prose they expected, not the prose on the page. This is re-flagged under the "resolution actually incorrect" exception. **Fixed:** the lead now defines the paradox by the qualitative-difference datum and states the recipient reading as where the Map and functionalism part company, with a forward anchor to the article's `#the-paradox` section. L93 now gives the functionalist consumer reply in natural prose and says the in-framework pressure comes from the qualitative difference. The 06-20 Mode-Two argument at L95 is unchanged.

### Medium Issues Found

- **Carter et al. 2005 was overstated.** "Sometimes indefinitely — compared to non-meditators" became "Tibetan Buddhist monks practising one-point (focused-attention) meditation held a single percept markedly longer, the most experienced for an entire five-minute trial". "Indefinitely" overstated a five-minute ceiling, and the rivalry effect was specific to one-point meditation (compassion meditation showed none). Nature News (doi:10.1038/news050606-8) and the UQ release confirm "the whole five minutes" for the most experienced retreatants. This also eases the tension with "cannot prevent switching entirely".
- **"Cannot prevent switching entirely" was under-supported.** The L&L 1999 abstract supports voluntary and attentional influence but does not state the limit. **Added** Blake & Logothetis 2002, which says verbatim that "observers cannot maintain dominance of one rival figure to the exclusion of another".
- **A flat necessity claim, "These limits… cannot be explained from the outside by purely computational accounts" (L103).** **Cut**; it is necessity vocabulary that nothing argues for.
- **A flat tenet assertion in Minimal Quantum Interaction ("Consciousness influences the physical world through quantum-level selection").** **Cut**; it repeated the hedged version already in the Bidirectional paragraph.

### Publisher-of-Record Ledger (metadata re-confirmed against review 5; legs 7 and 8 run for the first time)

- Blake & Logothetis 2002 (Visual competition, *Nat Rev Neurosci* 3:13–21): metadata real-correct. **Result-direction: was wrong** (gradual and mixed attributed to V1/V2; gradual is phenomenal per the source). Corrected. Stance: neuroscientists, no dualist reading attributed.
- Carter et al. 2005 (*Curr Biol* 15(11):R412–R413): metadata real-correct. **Result-direction: overstated** ("indefinitely"; non-meditator comparison). Rescoped.
- Clark 2013 / Clark 2023: real-correct. Cited for the precision-weighting framework only; the three-condition synthesis is labelled the Map's. Stance: Clark is a naturalist and is not presented as endorsing dualism.
- Fodor 1983: real-correct. Informational encapsulation is correctly attributed.
- Friston 2005: real-correct. Framework citation only.
- Ibbotson & Krekelberg 2011 (*Curr Opin Neurobiol* 21(4):553–558): metadata real-correct. **Result-direction: forty-minute figure absent and "entirely" contradicted.** Corrected.
- Laing & Chow 2002 (*J Comput Neurosci* 12(1):39–53): metadata real-correct. **Over-attributed** (winner-take-all at later stages and "noise-driven"). Rescoped to what the abstract supports.
- Leopold & Logothetis 1999 (*TICS* 3(7):254–264): real-correct. The abstract supports voluntary and attentional influence; it is now paired with B&L 2002 for the limit.
- **McCauley & Henrich 2006** (*Philosophical Psychology* 19(1):79–101, DOI 10.1080/09515080500462347): **new, real-correct**. Crossref confirmed the authors, title, volume, issue and pages; the abstract (OpenAlex) confirmed the synchronic/diachronic framing and the cross-cultural immunity finding. Stance: naturalists arguing against Fodor's theory-neutral observation. They are not presented as endorsing anything Map-specific.
- Pylyshyn 1984: real-correct.
- **Pylyshyn 1999** (*BBS* 22(3):341–365): metadata real-correct. **Attribution: wrong.** The synchronic/diachronic distinction is not his, and his position on expertise is the opposite of what was implied. Corrected.
- Ramachandran 1992 (*Sci Am* 266(5):86–91): metadata real-correct. The size claim is physically accurate: a blind spot of about 5–7° spans about 5–7 cm at arm's length. The "lemon" simile is not verified in the source but is not presented as a quote.

**Inline ↔ References**: complete in both directions, 13 entries. `find_superlative_claims`: none.

### Counterarguments Considered

- **Functionalist consumer systems** (the recipient is downstream report, belief and action): now stated in the article as the boundary.
- **Dennett, "filling in versus finding out"** (*Consciousness Explained*, 1991): the strongest named opponent for the blind-spot paradigm case. Not added because of length, and because it would need a verified citation. Deferred (see Remaining Items).
- **Illusionism at L95:** Mode Two per review 5's stability note. Unchanged.

### Reasoning-Mode Classification (editor-internal)

- Functionalism and the recipient inference (L45, L93): **Mode Three**, now honestly marked. It was previously boundary substitution.
- Dennett/illusionism, thermostat and functional seemings (L95): **Mode Two**, unchanged.
- Eliminativist and Buddhist subject critiques: **Mode Three**, bedrock.
- No editor-vocabulary leakage.

## Optimistic Analysis Summary

### Strengths Preserved

The three-mode taxonomy and front-loaded opening, the blindsight "full range" sentence, the thermostat rejoinder, "influence without override" (kept and made robust to either reading of diachronic change), the three transparency profiles, "The brain proposes; consciousness disposes", and the hedged quantum speculation.

### Enhancements Made

- The Selection Gap now leans on a stronger and faithful observation: discreteness has a neural correlate, and the residue is the experiential question. That calibration is harder to attack (Hardline Empiricist).
- The Pylyshyn correction strengthens the attention-as-interface tie, since Pylyshyn puts cognitive intervention in focal attention.
- Length-neutral trims: the duplicate Fodor/Pylyshyn restatement at L99 (it repeated L59), the redundant perceptual-degradation summary sentence at L57 (its link survives in the same paragraph), a tightened menu-choice contrast at L69, and two flat assertions (L103, L111).

### Cross-links Added

- None. Cross-linking was already comprehensive. Added an in-page anchor from the lead to the article's `#the-paradox` section.

## Remaining Items

- **Archive siblings carry the same defects. NOT edited**, per the open P3 NEEDS-HUMAN archive-policy task in `todo.md` ("Do NOT action this from the loop"). This is a further data point for that decision:
  - `archive/concepts/perceptual-reconstruction-paradox.md` L67: Pylyshyn credited with synchronic/diachronic. L45: ~40 minutes.
  - `archive/concepts/selective-perceptual-correction.md` L50: "suppresses visual processing entirely" plus forty minutes cited to I&K.
  - `archive/voids/reconstruction-paradox.md` L49: forty minutes.
  - `archive/concepts/perceptual-reconstruction-selection.md`: "gradual transitions and mixed states" (B&L inversion).
- **Optional expansion, if headroom appears:** one sentence on Dennett's "filling in versus finding out" and the later evidence for active neural filling-in. That evidence does not by itself reinstate an audience.

## Stability Notes

- The recipient inference is now explicitly a **framework-boundary point**. Future reviews should not strengthen it back into an in-framework refutation, and should not flag the functionalist reply as a concession.
- Pylyshyn (1999) is cited for his attention-based reading of expertise, **not** for the synchronic/diachronic distinction, which belongs to McCauley & Henrich (2006). Do not revert.
- I&K 2011 supports only the ±100 ms window and reduced responses. The forty minutes is an uncited popular estimate, and is labelled so on purpose.
- All earlier stability notes stand: illusionism at Mode Two, hedged quantum speculation, bedrock Buddhist and eliminativist disagreement.