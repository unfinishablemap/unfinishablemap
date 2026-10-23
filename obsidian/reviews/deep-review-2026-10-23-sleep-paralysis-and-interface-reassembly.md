---
title: "Deep Review - Sleep Paralysis, Hypnopompia, and Interface Reassembly"
created: 2026-10-23
modified: 2026-10-23
human_modified:
ai_modified: 2026-10-23T22:50:45+00:00
draft: false
description: "Second deep review of the sleep-paralysis reassembly article. A raw-source re-read of Wang 2024 found the thalamus-fastest and motor-last orderings unsupported; also fixed a Myers founder claim and three quote frames."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-23
last_curated:
---

**Date**: 2026-10-23
**Article**: [[sleep-paralysis-and-interface-reassembly|Sleep Paralysis, Hypnopompia, and Interface Reassembly]]
**Previous review**: [[deep-review-2026-08-16-sleep-paralysis-and-interface-reassembly|2026-08-16]]
**Word count**: 3171 → 3249 (+78; prose ~2552 → 2614, reference apparatus ~632 → 651)

Only one change had reached the article since the last review: a 2026-10-23 19:36Z sentence at the end of the L62 paragraph, added by the new [[tonic-immobility-and-awareness]]. This pass reviewed that sentence against its source's guards. It then re-read every quotation and every Wang 2024 result against the raw open-access full text, rather than relying on the prior ledger.

## Pessimistic Analysis Summary

### Publisher-of-Record Citation Ledger (§2.4)

All 17 cited works plus one added work (Cheyne 2003) were checked against Crossref: every DOI resolves, and authors, year, venue, volume, issue and pages match. Full texts were taken from Europe PMC open access for Stevner, Kim, Sodré, Herrero, Wang, Ghibellini & Meier, and Jalal 2021, and every quotation was grep-checked in the raw text. Abstracts were used for Mainieri, Sharpless & Barber, Balkin, Ohayon, both Cheyne 1999 papers, Jalal & Ramachandran, and Jalal 2014; the Europe PMC full-text endpoint returned HTTP 500 for Mainieri and Sharpless. Alcaraz-Sánchez was read on the publisher's page, and Cheyne 2003 through its OpenAlex abstract.

- Stevner et al. 2019 (*Nat Commun* 10:1035) — **real-correct**. The full "Our results confirm…consolidated sleep" sentence is verbatim in the full text (1 hit), and "57 participants" is confirmed.
- Wang et al. 2024 (*Sci Rep* 14:1537) — **real-wrong-claim**: the article's ordering was not the paper's result (Critical 1). Confirmed: N = 21; one pre-sleep scan plus three post-waking scans; thalamus lag ~8 s at A1 → ~2.5 s at A3; ACC shifting earlier from Pre to A2 and "returns to its baseline state by 'A3'"; "the cortical sensorimotor areas did not present the alterations of EEG-fMRI coupling" (1 hit). Result-direction leg: the thalamus is significantly delayed at **both** A1 and A2 relative to A3 (Friedman p = 0.025), so its coupling does not recover "fastest". The sensorimotor null holds across all four sessions, Pre included, so it reports no disturbance at all rather than a late return. The authors call their result "potential dynamicity of NVC".
- Balkin et al. 2002 (*Brain* 125(10):2308–2319) — **real-correct**. The new inline quote "most rapidly re-established in centrencephalic regions (e.g. brainstem and thalamus)" is verbatim in the abstract (1 hit). This is where the thalamus-first ordering actually comes from.
- Kim, Moon, Mashour & Lee 2018 (*PLOS Comput Biol* 14(8):e1006424) — **real-correct metadata, two framing defects** (Medium 1). Both quotes are verbatim (1 hit each). The "topographic similarities" sentence comes from the empirical EEG (15 ketamine and 7 sevoflurane subjects), not from simulations. The "not a pharmacokinetic attribute" sentence opens "Neural inertia suggests that hysteresis…", citing Friedman et al. 2010; it is Kim's gloss on prior work, not a finding of their own. Kim's sleep-hysteresis references (their refs 6–7) are models, not measurements.
- Sodré et al. 2023 (*J Clin Med* 12(12):3876) — **real-correct, subject spliced** (Medium 2). The quote is verbatim, but its source subject is "motor, sensory, and cognitive abnormalities that usually happen…". The article had written "whose episodes", and "dissociated" where the source has "dissociative". Both corrected.
- Sharpless & Barber 2011 (*Sleep Med Rev* 15(5):311–315) — **real-correct**. Thirty-five studies, N = 36,533, 7.6% and 28.3% are confirmed in the abstract. The DOI (10.1016/j.smrv.2011.01.007) was missing and has been added.
- Mainieri et al. 2021 (*J Clin Sleep Med* 17(4):719–727) — **real-correct, modal dropped** (Medium 3). Both quotes and the 70.8 / 89.7 / 21.2% figures are verbatim in the abstract. The source says the theta rhythm "suggests that the brain…is not in an awake but in a dreaming state"; the article had presented this as "their own conclusion is that". Restored to "suggest".
- Herrero et al. 2025 (*Sci Rep* 15:33586) — **real-correct, subject spliced** (low). The quote is verbatim; its source subject is "the sample size and number of episodes per state were limited, which may affect…". The article now reads "the limited sample and episode count". The n = 7 (2 SP, 2 OBE) and OBE spectral details were re-confirmed.
- Ghibellini & Meier 2023 (*J Sleep Res* 32(1):e13719) — **real-correct**. The definition sentence is verbatim apart from a U+2010 hyphen in "sleep‐offset", which is why a plain-ASCII grep returns 0. Confirmed: "In this review, we use the term hypnagogic states to refer to" both; Maury 1848 coined *hypnagogic*; Myers (1904 edition) coined *hypnopompic*.
- Ohayon et al. 1996 (*Br J Psychiatry* 169(4):459–467) — **real-correct**. N = 4,972 and the "Thirty-seven per cent…12.5%" sentence are verbatim, and "may be a better indicator" is preserved. The DOI (10.1192/bjp.169.4.459) was missing and has been added.
- Cheyne, Rueffer & Newby-Clark 1999 (*Conscious Cogn* 8(3):319–337) — **real-correct**. The abstract confirms the Intruder, Incubus and "Unusual Bodily Experiences" factor labels.
- Cheyne, Newby-Clark & Rueffer 1999 (*J Sleep Res* 8(4):313–317) — **real-correct**. The abstract treats "hypnagogic and hypnopompic hallucinoid experiences" as one class.
- **Cheyne 2003 (*Dreaming* 13(3):163–179, doi:10.1023/A:1025373412722) — ADDED.** Its abstract already names the third factor "vestibular-motor (V-M) bodily sensations". The article had credited the relabel to "Cheyne's later work with Girard" (Critical 4).
- Jalal & Ramachandran 2014 (*Med Hypotheses* 83(6):755–757) — **real-correct metadata, mechanism spliced** (Critical 3).
- Jalal, Simons-Rudolph, Jalal & Hinton 2014 (*Transcult Psychiatry* 51(2):158–175) — **real-correct**. "nearly half (48%)…caused by the Jinn" is confirmed.
- Jalal, Romanelli & Hinton 2021 (*Transcult Psychiatry* 58(3):427–439) — **real-correct**. The Pandafeche and Abruzzo details are confirmed in the full text.
- Hufford 1982 — **real-correct**. Title and year are confirmed at Open Library.
- Alcaraz-Sánchez 2024 (*Philos Mind Sci* 5) — **real-correct**. All five dimensions and the clear-light-sleep case study are confirmed on the publisher page.
- Southgate & Oquatre-six 2026; Southgate & Oquatre-huit 2026 — Map self-citations, wikilinked in the body. Legitimate.

**Orphan check, keyed on (surname, year), both directions.** Every inline pair has a reference entry and every reference is cited inline. Kim 2018 and Cheyne, Rueffer & Newby-Clark 1999 appear in multi-author prose form. Both same-surname-same-year pairs (Cheyne 1999 ×2; Jalal 2014 ×2) are cited distinctly. The one gap was an unreferenced attribution ("Cheyne's later work with Girard", with no year and no entry), now resolved by the Cheyne 2003 citation. Maury 1848 and Myers are attributed through Ghibellini & Meier, which is acceptable. The superlative helper returned no hits.

### Critical Issues Found

1. **Wang 2024 ordering invented: "thalamus fastest … motor-adjacent cortex last" (lead L38; L52; L54).** Read against the raw full text, the paper's thalamic coupling is delayed at both A1 and A2 and back by A3. The ACC makes an excursion at A2 and is back by A3. Sensorimotor coupling shows no alteration across Pre–A3. The data therefore give three unlike region-specific schedules but no fast-to-slow order. The sensorimotor result in particular is a **null against the pre-sleep baseline**, so "motor-adjacent cortex last — the channel whose delayed return sleep paralysis makes phenomenally obvious" read the null as a late return. The motor closure of sleep paralysis is also a brainstem-spinal atonia (L60), which no Wang region measures.
   - *Fix:* the lead and L52 now describe the three schedules as reported. The thalamus-first ordering is reassigned to Balkin 2002's CBF measure, with a verbatim quote. The "motor last" clause is replaced with "The motor closure of sleep paralysis, a brainstem-spinal atonia, lies outside what was measured."
   - *Why earlier passes missed it:* the prior review rightly fixed "ACC intermediate" and verified the lag numbers. It verified the numbers, not the ordering built on them. The anti-single-dial argument (L56) still stands, since three unlike schedules are not one clock.

2. **Occam section counted an anaesthesia result as a natural-sleep test (L92).** "Fails three separate empirical tests … and thresholds (hysteresis)" contradicted the article's own falsifier 4 (natural-sleep hysteresis not yet directly measured). It also contradicted the Dualism section's warning against counting sleep-side and anaesthesia-side asymmetries separately. And it drifted above the spoke: [[direction-of-interface-change]] (rewritten 2026-08-18, after this hub's last review) says hysteresis reaches the sleep boundary "through an argument … rather than through direct measurement of sleep thresholds, which remains undone". Kim 2018's human data are anaesthetic only.
   - *Fix:* the section now reads "fails two direct empirical tests … Hysteresis tells against it only by extension from anaesthesia." L48 now names the anaesthetic EEG basis.

3. **Jalal & Ramachandran mechanism spliced across two regions and two sources (L70).** The abstract places the disturbed "multisensory processing of body and self" at the **temporoparietal junction**, and the hallucinated hard-wired body image in the **right superior parietal lobule**. The 2026-08-16 fix ("temporoparietal" → "right superior parietal") merged the two roles into one region, so that resolution was incomplete. "Runs without confirming afferent input" is the research note's gloss of *Cheyne 1999's* vestibular factor (research note L45), grafted onto this paper. "Explain" also overstated a *Medical Hypotheses* postulate that the authors themselves propose testing.
   - *Fix:* "propose that the intruder is a hallucinated projection of the subject's own hard-wired body image, which they place in the right superior parietal lobule, arising from disturbed multisensory processing of body and self at the temporoparietal junction."

4. **Coiner lens: Myers as "founder of the filter tradition"; V-M relabel credited to the wrong work (L82, L70).** [[terminal-lucidity-and-filter-transmission-theory]] does not treat Myers's theory as "a founding statement". It names Bergson (1896) and James's 1898 "permissive or transmissive" lecture as the proposals, and says Myers "developed the transmission idea with extensive case evidence" (1903). [[filter-theory]] credits James, Bergson and Huxley. So the hub misreported its own sibling page and credited a developer as the founder. The framing originated at research note L161.
   - *Fix:* Myers is now "the psychical researcher who, as the terminal-lucidity article recounts, developed the transmission idea of Bergson and James with extensive case evidence", and "A chief developer of the filter tradition…". The historical irony the prior review praised survives intact.
   - *Separately:* "vestibular-motor" is already in Cheyne's solo 2003 *Dreaming* paper, so "Cheyne's later work with Girard renames" named the wrong originating work. It is now "Cheyne's later work renames vestibular-motor (Cheyne, 2003)".

### Medium Issues Found

1. **Kim 2018 framing (L48).** Fixed: "in their simulations and empirical comparisons" became "In EEG from volunteers under ketamine or sevoflurane"; the neural-inertia sentence is now framed as Kim's reading ("they read neural inertia as suggesting that hysteresis…", keeping the source's "suggests"); and "with no reference to consciousness" became "with no experiential term", since the paper's subject *is* conscious-state transitions.
2. **Sodré subject splice and "dissociated" (L60).** Fixed, as in the ledger.
3. **Mainieri dropped modal (L64).** Fixed, as in the ledger.
4. **Over-concession: "Nothing about the state is mechanistically mysterious" (L60).** This sweeping absence claim overstated the science. Atonia is characterised, but why it outlasts arousal, and the hallucination mechanisms (one still a hypothesis), are not settled. The sentence was also stronger than the Map needs. Replaced with "The Map's use of the state depends on no mechanistic mystery." (−5 words)
5. **"Full awareness" (L60) against "Metacognition is substantially restored" (L62) and a "dreaming state" (L64).** This was an internal quantifier tension next to the new TI sentence. Changed to "waking awareness" at zero cost.
6. **Hub-over-spoke: Dualism section and Further Reading said the sleep evidence "joins" the direction-of-interface-change family.** The spoke calls the sleep-wake boundary a candidate fourth domain whose "fit is partial". The Dualism section now carries "where the sleep-wake fit is only partial", and the Further Reading line reads "may join". "Restore independently" became "settle on separate schedules", which is what the data show.
7. **Prevalence gloss (L92).** "Reported roughly three times as often" read as a per-event frequency, but Ohayon reports the share of respondents. Now "roughly three times as many people report".

### The New TI Sentence (L62), Checked Against the Guards of [[tonic-immobility-and-awareness]]

- *Awareness during TI is known only from later report:* not stated explicitly before, and "weeks to years" understated the spoke's "minutes to decades". The sentence now says "the awareness beside it is known only from reports given minutes to decades afterwards", the spoke's own wording.
- *The cascade predicts the shutdown with no experiential term:* the sentence makes no evidential claim for TI, so the guard is not violated. It was not added, to save length.
- *Disanalogy explicit, no independent-confirmation counting:* the disanalogy ("in waking and under threat") was already present. The sentence now adds "it serves for comparison, not as a second confirmation", which mirrors the spoke's "The family serves comparison, not counting."
- *Nothing says TI subjects are "fully aware":* confirmed (0 hits for "fully aware" or "full awareness" after the L60 change).
- Net +11 words for the sentence.

### Counterarguments Considered

- *A production model explains staggered restoration as generators restarting at different rates.* Already conceded in the lead and in L56; bedrock (see the prior Stability Notes).
- *Wang's authors hedge their result as "potential dynamicity", so L56's "rule out the single-dial picture" is too strong.* Considered and **declined**. The prior review stress-tested this sentence twice for its internal consistency with falsifier 1 and recorded a do-not-re-flag note. The claim it makes is scoped by "on one clock", and the region-specific session effects (thalamus and ACC significant, sensorimotor null) are what that scope requires. This pass's correction does not weaken that reading.

### Reasoning-Mode Classification (§2.6, editor-internal)

As in the prior review, there are no named individual opponents. Engagement with the single-dial arousal account is Mode One: the coupling data are used against it on its own empirical terms, now with a correctly described dataset. Engagement with production models is Mode Three, declared outright. There is no boundary substitution, and a grep for the forbidden-label set returned zero hits in article prose; a positive-control grep was run first.

## Optimistic Analysis Summary

### Strengths Preserved

- The status-first lead and the "explanatory debts" close.
- "The evidence permits both; the Map notes which it expects" (Tenet 3, fits without evidencing). The section never concedes epiphenomenalism and makes no strong-revelation move, and it was left untouched.
- The non-independence caution in the Dualism section, now extended to the TI comparison.
- The Myers/Maury irony paragraph. It is reframed rather than cut, and its point survives with the correct attribution.
- The four falsifiers. Falsifier 4 is now consistent with the Occam section instead of contradicted by it.

### Enhancements Made

- The Wang description is now more informative than before: a pre-sleep baseline, both delayed thalamic scans, and the ACC baseline. The anti-single-dial argument rests on what was measured.
- A verbatim Balkin quote now carries the thalamus-first ordering, assigned to the measure that actually showed it.

### Cross-links Added

None new. [[tonic-immobility-and-awareness]] was already linked by today's earlier insertion.

## Calibration Assessment

The diagnostic test is: would a reviewer who accepts the tenets still flag the claim? Before this pass it returned yes on two claims. The Occam section's "fails … hysteresis" counted an extension as a test, and the L54 "motor last" read a null as a confirming order. Both errors came from mis-scoped evidence, not from inflating the tenets, and both are corrected. The Bidirectional Interaction section's quantifier question is left open, as briefed.

## Hub-over-Spoke Spot-Check

| Spoke | Verdict on the hub before this pass | Action |
|---|---|---|
| [[direction-of-interface-change]] (L53, 2026-08-18) | Hub stronger: "joins"; hysteresis as a sleep test | Fixed (Dualism, Occam, Further Reading) |
| [[tonic-immobility-and-awareness]] | Recall interval understated; comparison-not-counting guard implicit | Fixed (L62) |
| [[terminal-lucidity-and-filter-transmission-theory]] / [[filter-theory]] | Hub credited Myers as founder; the spokes credit Bergson and James | Fixed (L82) |
| [[anaesthesia-and-the-consciousness-interface]] (L103, L113) | Consistent: Mashour 2021 "executive function returned first" is verbatim in the eLife abstract | None |
| [[hypnagogic-phenomenology-and-interface-modulation]] (L80) | Consistent: the retrospective-report weakness is acknowledged there | None |

## Family Resolution

The source research note, [[hypnopompia-and-sleep-paralysis-as-interface-reassembly-out-of-order-2026-08-12]], carried every defect in this cluster: "thalamus fastest" (L30, L100), "ACC intermediate" (L101, still present despite the prior NB at L30), "Thalamus > ACC > sensorimotor" (L230), the Girard-originated V-M label (L44, L222), and "Myers is the historical founder" (L161). Each now has a dated NB or a correction. The note's "companion" claim (Hilditch et al. 2023, *Netw Neurosci*, "sensorimotor network … still disconnected") is not in that paper's abstract, so it is marked UNVERIFIED rather than deleted. No other live page repeats these claims; inbound pages were grepped for thalamus, motor, fastest, hysteresis, founder and Myers.

## Remaining Items

None that need a task.

## Stability Notes

- **Wang 2024 gives region-specific schedules, not an order.** The thalamus is delayed at A1 and A2, the ACC makes an excursion at A2, and the sensorimotor null holds against the pre-sleep baseline. Do not restore "thalamus fastest", "motor-adjacent cortex last", or "Thalamus > ACC > sensorimotor". The thalamus-first ordering belongs to Balkin 2002 (CBF). This extends the prior note that the ACC is "non-monotonic, not intermediate".
- **Hysteresis is an anaesthesia measurement extended to sleep by argument.** Kim 2018's human data are under ketamine and sevoflurane only. Do not list it as a natural-sleep test the reversal picture "fails" unless a direct sleep-threshold measurement is cited (falsifier 4).
- **Myers developed the filter/transmission tradition; he did not found it.** The coinage of *hypnopompic* is his (Ghibellini & Meier 2023). The founding proposals the Map credits are Bergson 1896 and James 1898.
- **"Vestibular-motor" first appears in Cheyne 2003 (solo), not in the Girard collaboration.** This corrects the prior Stability Note, which said the label "postdates that paper by five years"; the gap is four years. The core instruction stands: do not put the label on Cheyne, Rueffer & Newby-Clark 1999.
- **Jalal & Ramachandran 2014: TPJ for the multisensory disturbance, right SPL for the body image.** Both regions are in the abstract with different roles. Collapsing them into either one alone is the defect, so do not "simplify" back.
- **Ghibellini's "sleep‐offset" uses U+2010.** A zero-hit ASCII grep is a false negative; the quote is verbatim.
- **Carried forward unchanged:** the production-model concession is bedrock; the 5-and-7-participant samples are already flagged and nominated as a falsifier; "rule out … on one clock" is consistent with falsifier 1; the Kim "topographic similarities" quote is verbatim.
