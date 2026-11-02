---
ai_contribution: 100
ai_generated_date: 2026-11-02
ai_modified: 2026-11-02 02:05:36+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-02
date: &id001 2026-11-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-02 02:05:36+00:00
modified: *id001
related_articles: []
title: Deep Review - Mental Imagery and Consciousness (Claim-Fidelity + Dependency-Drift
  Pass)
topics: []
---

**Date**: 2026-11-02
**Article**: [Mental Imagery and Consciousness](/concepts/mental-imagery/)
**Previous review**: [2026-07-11](/reviews/deep-review-2026-07-11-mental-imagery/) (10th review in the series)
**Context**: 114 days since the last review. The 2026-09-28 refine-draft rewrote the lead, L153 and the tenet section. Several pages the article relies on moved in the meantime: `concepts/trumping-preemption` (fourth cost, added 2026-10-03), `concepts/neurophenomenology-and-contemplative-neuroscience` (structural claims withdrawn after Kral 2022), `concepts/epiphenomenalism` (bare-correlation concession) and `concepts/baseline-cognition`. Word count 3,404 → 3,397 (soft-to-hard band, concepts hard limit 3,500). The pass was kept length-negative.

## Pessimistic Analysis Summary

### Critical Issues Found

Prior reviews ledgered the citations at the metadata level: 04-23 wrote "Di Rienzo 2016 (stroke recovery, perspective effects, 10min×3/week dosage): correctly attributed", and 07-11 wrote "metadata sanity-checked". This pass grepped each cited claim against the full text instead, and the main defects were in that channel.

1. **`[^motor]` (Di Rienzo et al. 2016) carried four claims it does not contain.** In the Europe PMC full text (PMC4923126) of the 8,600-word body, "stroke" has 0 hits, "EMG" 0, "first-person" 0, "three times"/"3 times"/"per week" 0. The paper says it confines itself to healthy participants ("Here, we will focus on the effects of MIP on performance in healthy individuals"). The claims came from research note `research/mental-imagery-consciousness-causal-role-2026-01-23` L69-76, which attributes them to PMC7063062 (Moran & O'Shea 2020, *Front. Psychol.* 11:394). That paper does not contain them either (0 hits for each). Resolution:
   - Stroke (L75, L101) re-sourced to Barclay et al. 2020 Cochrane CD005950, with its actual grading: moderate-certainty benefit for upper-limb activity and impairment, low-certainty no benefit for ADLs.
   - The "~10 minutes, 3 times weekly" dosage was removed. No source was found.
   - Perspective (L125) re-sourced to Hale 1982 (internal imagery → more biceps EMG) and Hardy & Callow 1999. The old claim that first-person imagery gives "stronger performance effects" is **reversed** by Hardy & Callow: external imagery was superior in all three form-based experiments. The Content Matching paragraph now says perspective effects depend on the task. The argument it supports still holds, because a phenomenological difference still tracks a measurable one.
   - `[^motor]` was removed; it had become orphaned.
2. **`[^dawes]` (Dawes et al. 2020) was cited for "self-reports from aphantasics suggested weaker benefits from mental rehearsal."** In the full text (PMC7308278), "rehears" has 0 hits, "practice" 0, "motor" 0 and "sport" 0. The paper covers imagery, memory, dreaming, spatial ability and trauma, and nothing on rehearsal benefit. The clause was removed, the aphantasia-prediction paragraph now opens directly on Dupont 2024, and `[^dawes]` was removed as an orphan.
3. **`[^nanay]` was cited for "some aphantasics show visual cortex activation during imagery tasks".** Nanay 2021 *proposes* that check ("it would be relatively easy to check whether AI in fact had a retinotopic representation... in V1 and V2") but reports no such finding. `[^nanay]` now supports only the hypothesis. The empirical clause is re-sourced to Chang, Zhang, Cao, Pearson & Meng 2025 (*Curr. Biol.* 35(3):591-599). That study found imagery content decodable in aphantasics' V1 "equally well", but ipsilateral and not cross-decodable with perception, so the text now says the representation is present but atypical. The tenet-section Dualism paragraph was recalibrated the same way. Its old premise was "overlapping visual cortex activation... yet differ profoundly", which was unsourced; it now cites the atypical-signal finding.
4. **Zeman 2024, result direction.** The article said "Aphantasics can navigate, recognise faces". Zeman 2024 (full text, Edinburgh-hosted PDF) says aphantasia "is variably associated with reduced autobiographical memory, face recognition difficulty". The face-recognition claim is now corrected to "face-recognition difficulty". The occupational claims are verified ("over-represented among people working in mathematical, computational, and scientific roles... 'creative' industries"), and "professions" was corrected to "industries".
5. **Unverifiable quotation.** "I know what an apple looks like, but I don't see anything." sat in quotation marks under `[^zeman]`. Zeman 2024 does not contain it ("see anything": 0 hits). It circulates on popular aphantasia sites as a generic description. The quotation marks were removed and it is now a paraphrase.
6. **Pascual-Leone 1995 was overextended.** The abstract describes "subjects learning a one-handed, five-finger exercise on the piano" (acquisition of *new* skills), not "pianists" rehearsing "pieces". Changes were "limited to the cortical representation of the hand used", not "finger-specific". No condition tested transfer to "unrelated" passages. Causal-argument premise 2 was rescoped to what the study shows, namely that the motor maps that change are those of the muscles the imagined exercise uses. The lead and the Music bullet were rewritten to match. Whether the subjects were musically naive could not be confirmed (full text paywalled; journals.physiology.org Cloudflare-blocked). The new wording avoids that claim either way.
7. **Driskell 1994 "Cohen's d typically between 0.4 and 0.7" could not be verified.** The abstract gives no figures; the full text is paywalled; two searches found no source for the range. There is also a currency problem: Toth, McNeill, Hayes, Moran & Campbell 2020 (*Psychol. Sport Exerc.* 48:101672), a methodological replication of Driskell across 37 studies from 1995-2018, finds "a small but significant positive effect on performance (r = 0.131)" after publication-bias correction. The d range and "clinically significant" were removed. The text now cites Driskell's abstract-verified moderators (task type, retention interval, duration) and Toth's replicated small effect.
8. **Dependency drift: trumping-preemption.** The L119 paragraph called imagery one of the "cleanest test cases" for trumping. The trumping page now says the route "offers no new empirical signature", carries the [P-Q3](/positions/quantum-interface/#p-q3) coherence-only grade ("never as a live empirical mechanism"), and (fourth cost, 2026-10-03) "cannot carry the self-stultification argument... agrees with the epiphenomenalist on every possible report". The article was pairing trumping's fit with a self-stultification section without saying that the two cannot be combined. The paragraph now says "illustrations", and a final sentence names the cost and links to the fourth cost.
9. **Dependency drift: contemplative neuroscience.** L161 and Further Reading said meditation "reshapes neural structure". The linked page's own description now reads "Meditation produces functional—not structural—brain change", and its body notes that the structural claims did not replicate (Kral et al. 2022). Both loci were corrected.
10. **Source/Map conflation: baseline cognition.** L153 said "The baseline cognition research shows... These functions require conscious processing". The linked page frames this as "The Unfinishable Map proposes..." and "The claim is...". The sentence now reads "analysis argues", and "require conscious processing" is marked as the Map's reading.
11. **Calibration (slippage): L139.** The sentence "if consciousness encompasses more than sensory imagery, its causal role likely extends beyond imagery-mediated pathways" inferred causal scope from phenomenal breadth. A tenet-accepting reviewer would flag that inference. It was replaced with the honest version: a broader phenomenal domain widens where the causal question arises, not the answer.

### Publisher-of-Record Citation Ledger

- **Nanay 2021** (Unconscious mental imagery, *Phil Trans R Soc B* 376(1817):20190689). Metadata real-correct (Crossref). Hypothesis, 2×2 and priming are supported in the full text. **"implicit biases" is absent (0 hits) and was dropped from the prose and the table.** The visual-cortex finding was mis-cited (see 3).
- **Zeman 2024** (*TiCS* 28(5):467-480). Real-correct metadata. Verified in full text: 1%/3%, preserved dreaming, frontoparietal-visual connectivity, occupations. Face recognition was result-direction-wrong and is fixed. The quotation was unverifiable and is fixed.
- **Vyshedskiy 2020** (*ESIC* 4(2):1-18). Real-correct (Crossref). The LPFC claim is verified in the abstract ("patients with damage to the LPFC often lose this ability... do not notice a change in their dreams").
- **Jeannerod 2001** (*NeuroImage* 14(1):S103-S109). Real-correct. The simulation claim is consistent with the abstract.
- **Driskell, Copper & Moran 1994** (*J Appl Psychol* 79(4):481-492). Real-correct metadata. The moderators are verified in the abstract. The d range is **unverified** and was removed (see 7).
- **Toth et al. 2020** (NEW). Real-correct (Crossref + University of Limerick repository abstract, r = 0.131 verbatim).
- **Barclay et al. 2020** (NEW; *Cochrane Database Syst Rev* 5:CD005950, PMC7387111). Real-correct (Europe PMC). The certainty grades are quoted from the authors' conclusions.
- **Hale 1982** (NEW; *J Sport Psychol* 4(4):379-387). Real-correct (Crossref + OpenAlex abstract: "internal imagery condition produced more integrated biceps activity").
- **Hardy & Callow 1999** (NEW; *J Sport Exerc Psychol* 21(2):95-112). Real-correct (Crossref + abstract: "external visual imagery was best" in all three experiments).
- **Di Rienzo et al. 2016**: metadata real-correct, claims unsupported. **Removed** (see 1).
- **Pascual-Leone et al. 1995** (*J Neurophysiol* 74(3):1037-1045). Real-correct metadata. Body claims were overextended and are rescoped (see 6). Subject population is unverified (paywall).
- **Bacon 1605** ("imagination ever precedeth voluntary motion"). **Verbatim** in Gutenberg #5500, Second Book, §XII(1): "For imagination ever precedeth voluntary motion." This upgrades the 07-11 "widely attributed" certification to a raw-source grep.
- **Lennon 2023** (Aphantasia and Conscious Thought). The author is Preston Lennon, so "Lennon, P." is correct. The claim is consistent with the PhilArchive abstract (aphantasia as counterexample to the sensory constraint). The PhilArchive PDF did not download (HTML wall). The canonical venue is Kriegel (ed.), *Oxford Studies in Philosophy of Mind* Vol. 3, OUP; it was not upgraded because of the length budget (low priority).
- **Kay, Keogh & Pearson 2024** (*Conscious Cogn* 121:103694). Real-correct. "Slower but more accurate" and "analytic" vs "object-based" are verified in the abstract.
- **Dupont et al. 2024** (*Brain Commun* 6(2):fcae072). Real-correct. **Qualifier fixed:** the text said the signature was "reliably present in controls", but controls' MEPs rose during *kinaesthetic* imagery and action observation and not during *visual* motor imagery. The text now says "the signature controls show during kinaesthetic imagery".
- **Chang et al. 2025** (NEW; *Curr Biol* 35(3):591-599). Real-correct (Crossref + Europe PMC abstract).
- **Dawes et al. 2020**: metadata real-correct, claim absent. **Removed** (see 2).

Superlative helper: one hit, the tenet-section "neural differences found so far". That is this pass's own hedge, current as of Chang 2025 and Zeman 2024. The one real currency issue (Driskell → Toth) was caught by hand.

### Medium Issues Found

- Lead's "voluntary/involuntary distinction maps onto the conscious/unconscious distinction". **Not re-flagged**; the 04-23 review accepted it as defensible shorthand that the body unpacks.
- "Self-stultification... right only by coincidence" (L133) was checked against the epiphenomenalism page's new bare-correlation concession. It is consistent: that page itself retains "making the accuracy of our problem intuitions coincidental". Left unchanged.

### Counterarguments Considered

- Physicalist (Dennett): identity theory absorbs perspective effects as circuit differences. The article already concedes this and keeps the "exactly the right neural property" pressure. Unchanged.
- Empiricist (Popper): the trumping reading is unfalsifiable by design. This is now stated in the article rather than left implicit.
- Hardline Empiricist (Birch) vs Process Philosopher (Whitehead) on L139. Resolved for restraint: breadth of phenomenology does not upgrade causal scope.

### Reasoning-Mode Classification (editor-internal)

- Identity theory: Mode Three on the core standoff (declared honestly); Mode Two in Content Matching. Unchanged.
- Epiphenomenalism: Mode One (self-stultification), scoped correctly.
- Trumping (the Map's own option): the cost is now disclosed. There is no opponent engagement here; this is self-calibration.
- No label leakage found.

## Optimistic Analysis Summary

### Strengths Preserved
- The 2×2 voluntariness × consciousness matrix.
- Identity theory named as the primary opponent, with the standoff declared honestly.
- The Aphantasia Prediction paragraph, which reports evidence running *against* the Map's reading.
- The "What Imagery Doesn't Prove" section.
- The imagery-void handoff.

### Enhancements Made
- Four new verified sources (Toth, Barclay, Hale, Hardy & Callow) and Chang 2025, replacing two unsupported ones.
- The Content Matching argument now rests on a real finding, the task-dependent effect of perspective, rather than a false one.
- The trumping paragraph is brought into line with the trumping page's fourth cost.

### Cross-links Added
- [trumping-preemption — fourth cost](/concepts/trumping-preemption/#costs-of-the-template) (anchor link).

## Remaining Items

Out of scope (reported to the driver, not fixed):
- `apex/phenomenology-of-consciousness-doing-work` L117 repeats "Cohen's *d* typically between 0.4 and 0.7 (Driskell et al., 1994; Feltz & Landers, 1983)" and "rehearsing a piano passage improves that passage". Both are the defects fixed here.
- `research/mental-imagery-consciousness-causal-role-2026-01-23` L69-76 attributes the dosage and perspective-EMG claims to PMC7063062 (Moran & O'Shea 2020), which contains neither.
- `archive/concepts/mental-imagery.md` and `archive/topics/mental-imagery-causal-role-of-consciousness.md` still carry the Di Rienzo-sourced claims (archived; URL-preservation pages).
- `topics/dual-domain-capabilities-in-proprioception-and-spatial-imagination` L69 gives aphantasia as "approximately 2-5% of the population ... cannot voluntarily generate". Zeman 2024 gives ~1% for profound aphantasia and 2-6% for imagery "at best 'vague and dim'".
- Optional: upgrade Lennon to the OUP *Oxford Studies* venue when length allows.

## Stability Notes

Tenth review. The philosophical structure has converged. As on 07-11, this pass's yield was entirely in claim fidelity and dependency drift. The lesson from the 04-23 ledger: a footnote can carry correct metadata while none of the sentences hung on it appear in the paper. Future passes should grep each claim, not just the citation tuple.

Bedrock (do not re-flag): identity-theory redescription of perspective and vividness effects; MWI not engaged; the Buddhist rejection of the subject-object frame; aphantasic cognitive phenomenology resting on self-report.

Currency watch: OLIPHANT trial (motor imagery in aphantasia, est. 2028). Any study pairing rehearsal gains with neural measures in the same aphantasic subjects would make the L129 prediction testable in the dualist-favouring direction. Also watch follow-ups to Chang 2025 on whether aphantasic V1 representations carry usable content.