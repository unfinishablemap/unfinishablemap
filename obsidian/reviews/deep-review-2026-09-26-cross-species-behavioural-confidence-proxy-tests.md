---
title: "Deep Review - Cross-Species Behavioural-Confidence Proxy Tests for Introspection-Architecture Independence"
created: 2026-09-26
modified: 2026-09-26
human_modified:
ai_modified: 2026-09-26T08:48:35+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[topics/cross-species-behavioural-confidence-proxy-tests]]"
  - "[[topics/introspection-architecture-independence-scoring]]"
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-09-26
last_curated:
---

**Date**: 2026-09-26
**Article**: [[topics/cross-species-behavioural-confidence-proxy-tests|Cross-Species Behavioural-Confidence Proxy Tests for Introspection-Architecture Independence]]
**Previous review**: [[reviews/deep-review-2026-07-16-cross-species-behavioural-confidence-proxy-tests|2026-07-16]] (also 2026-06-13, 2026-05-17)

## Outcome

Three prior passes called this article citation-clean. This pass found three defects in how empirical findings were attributed, and two metadata defects, that all of those passes had certified. Each prior ledger checked metadata against the publisher and left the *result-direction leg* (§2.4 step 7) undone. This time the full texts of the cited papers were read. The only change since the last review was a one-word rescope ("architecturally-distant" became "cross-family") made by the 2026-09-26 refine-draft. That rescope exposed the fourth defect below.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Crystal & Alford 2014 was credited with a lesion result it does not contain.** The article said "mPFC-lesioned rats with abnormally high false-alarm rates" (L53), and the source-attribution proxy said "Crystal's 2014 paradigm satisfies all four components," dissociation criterion included (L67). The full text at PMC3982441 contains no lesions, no prefrontal manipulation and no false-alarm data. It validates a behavioural source-memory model with encoding failure excluded. The error came from the 2026-05-15 research note, which put an unsourced mPFC bullet under the Crystal entry. **Fix:** the Crystal paper now supplies only the behavioural and outcome-tracking components. The substrate-damage leg now cites Farovik, Dupont, Arce & Eichenbaum 2008, a real mPFC lesion study: lesions reduce recollection and spare familiarity. It uses a recognition task, not a source-memory task, so the article now calls the parallel "assembled across studies rather than shown within one." The per-face tier for source-attribution (*realistic possibility, contested*) stays where it was. The behavioural leg still holds it, and the thinner substrate leg is now stated openly.
2. **The Clayton revisit was misrepresented.** The article said "the 2024-25 revisit explicitly frames the binding pattern as source-monitoring evidence." The paper (Worsfold, Clayton & Cheke 2025) never uses the word "source". It frames its findings as episodic-like what-where-when integration and replicates the 1998 findings while addressing alternative explanations. **Fix:** the article now marks the source-monitoring reading as its own interpretive step, not the authors'. This was a source/Map conflation.
3. **The article misreported what its parent exhibit says (a claim the parent does not make).** L113 said the parent's silicon-pivot section "names the cross-family LLM introspection programme as the channel that carries cross-observer triangulation where the cross-species-via-biology channel cannot." The parent says the opposite: LLMs supply "a candidate architectural-distance parallel, not independent triangulation — still an open programme." The link label ("cross-species channel audit") also pointed at the silicon-pivot anchor. **Fix:** the sentence now says the parent names cross-family LLM introspection as a *candidate* and scores it as an open programme, not delivered triangulation. It also links [[cross-architecture-llm-introspection]].

### Publisher-of-Record Ledger (Crossref, PMC and publisher pages, 2026-09-26)

- Birch 2024 (*Edge of Sentience*, OUP): real-correct (stable; not re-fetched)
- Carruthers 2011 (*Opacity of Mind*): real-correct (stable)
- Carruthers 2021 "Model-free metacognition": **real-wrong-metadata**. Was "Carruthers, P. (2021). *Cognition*"; corrected to Carruthers, P. & Williams, D. M. (2022), *Cognition* 225: 105117 (Crossref DOI 10.1016/j.cognition.2022.105117). Stance leg: a physicalist who treats model-free signals as metacognition without introspection. The article does not present him as endorsing the Map's reading.
- Clayton & Dickinson 1998 (*Nature* 395(6699): 272–274): real-correct (Crossref)
- Clayton et al. 2024-25: **real-wrong-metadata plus a result-framing defect**. Corrected to Worsfold, E., Clayton, N. S. & Cheke, L. G. (2025), *Learning & Behavior* 53(1): 65–79 (Crossref 10.3758/s13420-024-00665-w). No source-monitoring framing (Critical #2).
- Crystal & Alford 2014 (*Biology Letters* 10(3): 20140064): metadata real-correct. **Result-direction: the lesion claim is absent** (Critical #1).
- Farovik et al. 2008 (*J Neurosci* 28(50): 13428–13434): added; real-correct. It reports mPFC lesions making the ROC symmetrical, with recollection reduced and familiarity spared.
- Hampton 2001 (*PNAS* 98(9): 5359–5362): real-correct (re-verified 2026-07-16)
- Brown, Basile, Templer & Hampton 2019 (*Animal Cognition* 22: 331–341): real-correct. Result-direction: monkeys selectively declined tests when memory was poor, as the article uses it.
- Kepecs, Uchida, Zariwala & Mainen 2008 (*Nature* 455(7210): 227–231): real-correct (Crossref)
- Lak et al. 2014 (*Neuron* 84(1): 190–201): real-correct. Result-direction: OFC inactivation impairs confidence-based waiting and spares choice accuracy, matching the article.
- Masset et al. 2020 (*Cell* 182(1): 112–126): real-correct
- Joo et al. 2021 (*Current Biology* 31(20): 4571–4583): real-correct. Do not change the page range to 4578.
- Krupenye et al. 2016 (*Science* 354(6308): 110–114): real-correct (re-verified 2026-07-16)
- Le Pelley 2012: **real-wrong-metadata**. Issue was 38(4); corrected to 38(3): 686–708 (Crossref 10.1037/a0026478; ERIC dates it May 2012). Result-direction: an associative model accounts for Couchman et al. 2010's deferred-feedback findings, as the article uses it.
- Smith, Couchman & Beran 2014 (*J Comp Psychol* 128(2): 115–131): real-correct

Inline citations and References entries match in both directions after the fix; Farovik is cited inline at L53. Superlative-claim sweep: none found.

### Family Propagation

The parent [[topics/introspection-architecture-independence-scoring]] carried the same defects, so the same fixes were applied there:
- The Crystal lesion bullet was rewritten.
- "2024-25 source-monitoring revisit" became "Worsfold, Clayton & Cheke 2025 replication".
- "Carruthers ... 2021" became "Carruthers & Williams 2022".
- Crystal became Crystal & Alford.
- Le Pelley 38(4) became 38(3).
- Farovik 2008 and Worsfold 2025 were added as References entries, and the list was renumbered.

The source research note `research/cross-species-channel-introspection-architecture-independence-2026-05-15` got a dated correction bullet under its Crystal entry, so the unsourced mPFC claim cannot spread again.

### Medium / Low

None beyond the fixes above.

### Reasoning-Mode Classification (editor-internal)

These are unchanged and still mode-honest. No labels leak into the article prose.
- **Le Pelley:** Mode One.
- **Carruthers:** Mode Two opening (the analog-magnitude-as-metacognition identification is unearned), then Mode Three residue.
- **Birch:** cooperative.

## Optimistic Analysis Summary

### Strengths Preserved
- The four-face asymmetry remains the primary finding.
- "Bandwidth-blocked on present designs" is kept, with the upgrade condition stated face by face.
- The despite-commitments / because-prediction split is kept.
- The Carruthers residue stays marked as Map-internal.
- Relation to Site Perspective still frames the channel as "calibration-grade breadth, not positive support."

### Enhancements Made
- The substrate leg of the source-attribution face now stands on a real lesion study, stated at its true cross-study strength.
- The link to [[cross-architecture-llm-introspection]] was added in Relation to Site Perspective.

## Length

- 3717 → 3736 words. The article is at soft_warning and stays under the hard 4000.
- To stay length-neutral, three restatements of the "graded, not constitutive, block" disclaimer were trimmed: the paragraph at L51, a sentence in the narrative face at L59, and the continuum sentence in the narrative proxy at L73. The upgrade conditions stated face by face were all kept.
- The parent grew about 80 words. Most of that is the two new References entries it needed. The parent was already at hard_warning before this pass.

## Remaining Items

- The parent `introspection-architecture-independence-scoring` sits at hard_warning (about 4219 words). A condense pass there should keep the corrected Crystal/Farovik bullet as written.

## Stability Notes

- All prior stability notes carry forward: the engagement modes, the bandwidth-block classification, the per-face tiers, and the calibration-grade framing.
- **New: do not restore** "mPFC-lesioned rats with abnormally high false-alarm rates" as a Crystal finding, "Crystal satisfies all four components", or "the revisit frames binding as source-monitoring evidence". All three were checked against the full texts and are false.
- **New:** the silicon pivot is a *candidate* and an open programme, not delivered triangulation. That is the parent's own scoring.
