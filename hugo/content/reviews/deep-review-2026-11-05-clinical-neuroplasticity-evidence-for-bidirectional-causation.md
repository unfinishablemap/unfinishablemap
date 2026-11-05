---
ai_contribution: 100
ai_generated_date: 2026-11-05
ai_modified: 2026-11-05 06:55:00+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-05
date: &id001 2026-11-05
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-05 06:55:00+00:00
modified: *id001
related_articles:
- '[[topics/clinical-neuroplasticity-evidence-for-bidirectional-causation]]'
title: Deep Review - Clinical Neuroplasticity Evidence for Bidirectional Causation
topics: []
---

**Date**: 2026-11-05
**Article**: [Clinical Neuroplasticity Evidence for Bidirectional Causation](/topics/clinical-neuroplasticity-evidence-for-bidirectional-causation/)
**Previous reviews**: [2026-07-13 (deep)](/reviews/deep-review-2026-07-13-clinical-neuroplasticity-evidence-for-bidirectional-causation/); 2026-06-21, 2026-06-05, 2026-05-26, 2026-03-22, 2026-03-21/21b (deep); pessimistic 2026-06-02, 2026-06-21.
**Context**: Selector pick (score 74; 115 days since the last deep review). Changes since then: the 09-02 Nakatani sweep, the 10-25 grade-unification refine (outer review 2026-10-25 Claude Fable 5.1, §2.4.3) and the 10-31 Siew & Yu redating. This pass ran the result-direction leg on every empirical cite, which earlier passes had not done. Six of the seven defects below survived 7 earlier reviews, each of which checked metadata only.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

1. **Result direction and an invented contrast, Yuan et al. 2022 (L56).** The page said the meta-analysis "found altered activation concentrated in prefrontal regions and the precuneus rather than at the synaptic periphery". The OpenAlex abstract reports *decreased* activation (left precuneus overall; left ACC and middle frontal gyrus in cognition tasks), and its emotion-task meta-analysis found no consistent region. The "synaptic periphery" contrast is not in the source, and fMRI cannot observe synapses. It was installed by the 05-26 deep review. The sibling `concepts/bidirectional-interaction` L99 already carries the correct direction and the emotion-task null. **Fixed**: the page now gives both. "CBT modulates brain activity top-down" (stated as fact) now reads "CBT is commonly modelled as modulating…".
2. **Unsourced claim since creation (L56).** "Anxiety treatment meta-analyses show decreased activation in the insula, anterior cingulate cortex, and dorsolateral prefrontal cortex" had no citation from the 03-21 expand onward. It matches Schrammen et al. 2022 (*Neurosci Biobehav Rev* 142:104895; PubMed 36179918, verified): 18 studies, n = 419, decreases in the right insula, ACC and dlPFC, "no region had increased activation". **Fixed**: cited and scoped, with ref #22 added. The "pattern that survives" sentence now says psychological intervention "alters activity in" prefrontal circuits rather than "engages" them, and it adds that the reported changes are decreases, which Schrammen et al. "tentatively read as normalisation" (the source says they "might indicate therapy-associated normalization"). L60 "engages" became "acts on" (0 words).
3. **Wrong statistic, Van Dam et al. 2018 (L82).** The page said "only ~1% of mindfulness studies comparing against active treatments". A grep of the PMC5758421 full text finds Van Dam reporting Dimidjian & Segal's estimate of "a mere 9% (of the total) at Stage 2b (… compared to active control)". The 1% is "research … conducted outside research contexts". The sibling `topics/clinical-evidence-quality-standards-consciousness-research` L68 fixed the same conflation on 2026-07-13; this page lacked that fix. **Fixed**: "reported an estimate that only about 9% of mindfulness-intervention research had tested efficacy against an active control".
4. **Wrong author on a real paper, ref #8.** "Álvarez, F. J. (2013)" is wrong. DOI 10.3389/fpsyg.2013.00412 resolves (Crossref, OpenAlex, PMC3706726) to **Askenasy, J., & Lehmann, J.** The research note `contemplative-neuroscience-meditation-2026-01-23` cites the same paper as "Berkovich-Ohana & Glicksohn". This is the fifth invented author name on this page's reference list, after Marzbani, Marueckova and Rodríguez-Martín (fixed 05-26 and 06-05) and the Manzotti & Moderato → Masi correction of 06-20. **Fixed** in the article and propagated to both research notes (family resolution). The reference is still an inline orphan. Prior reviews accepted that state, and it is not re-flagged here.
5. **Model misdescription, Schwartz, Stapp & Beauregard 2005 (L108).** The page said "closely spaced acts of attention hold neural patterns in place, preventing decoherence into alternative states". The PMC1569494 full text says the reverse: "Strong decoherence effects are certainly present, but they are automatically taken into account in the von Neumann formulation employed here". The Zeno effect holds the template for action against "very strong mechanical forces arising from process 2". **Fixed**: "hold a neural template for action in place against the brain's ordinary dynamics; the authors take decoherence into account rather than claiming attention prevents it". L110's decoherence-timescale objection, which is the critics' point, stands.
6. **Named idea cited to a work that does not use it, Nahm et al. 2012 (L114).** "Paradoxical lucidity in advanced dementia … (Nahm et al., 2012)". The PubMed abstract says "which we have called 'terminal lucidity'" and describes the "return of mental clarity and memory shortly before death" across tumours, strokes, meningitis, dementia and schizophrenia. The term "paradoxical lucidity" is later and is not Nahm's. **Fixed**: "Terminal lucidity—where patients with severely degraded neural tissue, including advanced dementia, briefly recover clarity shortly before death (Nahm et al., 2012)". L116 "paradoxical and terminal lucidity" is kept as the umbrella pair.
7. **Source/Map conflation, L42.** "evidence that conscious mental effort alone can normalise pathological brain activity" contradicted L46, where the protocol is "a modified CBT incorporating standard ERP". The Schwartz 1996 title says "behavior modification treatment". **Fixed**: "evidence that a drug-free psychological treatment, which Schwartz frames as conscious mental effort, can normalise…".

### Medium Issues Found
- **Goyal et al. 2014 framing (L82)**: "comparable to active controls such as exercise or CBT" upgrades the abstract's "no evidence that meditation programs were better than any active treatment". It also dropped the qualifier "mindfulness meditation programs" and the 8-week time point. **Fixed** against PubMed 24395196.
- **L44** "its hyperactivity drives the repetitive thought patterns" stated a circuit model as fact. **Fixed**: "is thought to drive".
- **L64** "routes meeting on shared structures as often as diverging" was an unsupported quantification. **Fixed**: "as well as diverging", matching L102.
- **Orphan ref #1 (Schwartz 1998)**: now cited inline at L44, "(Schwartz et al., 1996; Schwartz, 1998)". The PubMed 9829025 abstract reports CBT changing caudate metabolic activity in relation to outcome, and SSB 2005 cites the two papers together for the same claim. This costs +2 words and is not oscillation: prior reviews deferred the orphan only to avoid renumbering, and none is needed.
- **Ref #18 (Perez 2025)**: volume and article number were missing. Added "48, 103874" (Crossref).
- **Redundancy trims to offset length**: removed L98 "The meditation structural evidence, once cited as a fourth pillar, has been substantially weakened…", the fourth statement of that point (lead, L68 and L86 keep it), and L100 "The fact that medication produces similar brain changes to CBT in some conditions…", the third statement (L48 and L102 keep it). `git log -S` traces both to the 03-29 qualify pass. No review or task names either sentence.

### Counterarguments Considered (bedrock, not re-flagged)
- Physicalist input-modality deflation (route vs. direction, L64): Mixed. An in-framework argument followed by honest boundary-marking ("declined rather than refuted"). Unchanged.
- Identity-theorist symmetric reading of placebo content-specificity (L94): Mode Three. Unchanged.
- Production-theorist symmetric accommodation of the anomalous cases (L116): Mode Three. Unchanged.
- Engagement with the Hebbian materialist account (L48, L100, L104): Mode Three, with the boundary marked ("the data do not adjudicate"). No label leakage in the prose.

## §2.4 Publisher-of-Record Citation Ledger

Each line gives metadata state; result-direction state; cited-author stance.

- Schwartz 1998 (*Br J Psychiatry* 173 Suppl 35:38-44) — real-correct (PubMed 9829025). The abstract supports L44, so it is now cited inline. Stance: Schwartz is a mental-force advocate, presented as such at L48.
- Schwartz, Stapp & Beauregard 2005 (*PTRS B* 360(1458):1309-1327) — real-correct (Crossref). The L108 quote "Contemporary physical theory brings directly and irreducibly … made by human agents about how they will act." was **re-grepped verbatim in the raw PMC1569494 text this pass**. The model description was wrong-direction on decoherence and is fixed (Critical 5). Stance: quantum-interactionist advocates; L110 and L122 keep it as "speculative" and "does not commit".
- Schwartz & Begley 2002 (*The Mind and the Brain*) — real-correct (trade book). Coiner check: SSB 2005 says "A recent review … has coined the term 'self-directed neuroplasticity' … (Schwartz & Begley 2002)". L48's "Schwartz coined the term", cited to Schwartz & Begley, is accepted (Schwartz is a co-coiner and the cite names Begley).
- Yuan et al. 2022 (*Front Psychol* 13:853804) — metadata real-correct (Crossref, 10 authors). **Result-direction: wrong (fixed, Critical 1).**
- Calderone et al. 2024 (*Biomedicines* 12(11):2613) — real-correct (Crossref, 7 authors).
- Seymour & Mathers 2024 (*Front Psychiatry* 14:1301143; online 2024-01-10) — real-correct. The full text has "The EMBARC studies provide coincidental data that placebo induces fronto-limbic stimulation of neuroplasticity", so the L92 gloss is faithful. The label "Neuroplasticity Placebo Theory" is theirs ("referred to in this article as"). The underlying hypothesis, that placebo stimulates neuroplasticity, they credit to Rief et al. The page does not credit them with that hypothesis.
- Masi 2023 (*Front Psychol* 14:1150605) — real-correct (Crossref, sole author). The full text has "reducing the brain's size to 50–75% compared to its normal volume" for the 44-year-old Feuillet et al. 2007 case, so the L114 figure is faithful. Stance: an anti-identity-theory advocate. The page flags the source as "advocacy-leaning" (L116).
- Askenasy & Lehmann 2013 (*Front Psychol* 4:412) — **real-wrong-metadata (was "Álvarez, F. J.", corrected)**. Inline orphan, accepted state.
- Nahm, Greyson, Kelly & Haraldsson 2012 (*Arch Gerontol Geriatr* 55(1):138-142) — metadata real-correct (PubMed 21764150). **Term misattributed (fixed, Critical 6).**
- Kral et al. 2022 (*Sci Adv* 8(20):eabk3316) — real-correct (Crossref, 10 authors). The direction (null) is faithful. Currency check on "the most rigorous test to date": one search turned up no larger or better-controlled MBSR structural RCT from 2023-2026, so the superlative holds. Longer-duration training (months rather than 8 weeks) remains an open question that the claim does not cover.
- Goyal et al. 2014 (*JAMA Intern Med* 174(3):357-368) — metadata real-correct (PubMed 24395196). **Framing fixed** (Medium).
- Van Dam et al. 2018 (*Perspect Psychol Sci* 13(1):36-61, 15 authors) — metadata real-correct (Crossref). **Figure wrong (fixed, Critical 3).**
- Lazar et al. 2005 (*NeuroReport* 16(17):1893-1897) and Hölzel et al. 2011 (*Psychiatry Res Neuroimaging* 191(1):36-43) — real-correct (Crossref). Cited only as "earlier claims", so the direction is not at issue.
- Schwartz et al. 1996 (*Arch Gen Psychiatry* 53(2):109-113) and Baxter et al. 1992 (49(9):681-689) — real-correct (Crossref; content verified 07-13).
- Perez et al. 2025 (*NeuroImage: Clinical* 48:103874; 4 authors) — real-correct; volume added.
- Siew & Yu 2023 (*Sci Rep* 13:18469; retraction note 15:25545, 2025-07-15) — real-correct. The nature.com retraction note has "four null-finding papers accounting for data from 40% of participants were excluded" and "Both Authors disagree with this retraction", so the L78 gloss is faithful.
- Nakatani et al. 2003 (*Psychiatry Res Neuroimaging* 124(2):113-120) — real-correct (Crossref). From the abstract, via a secondary listing because PubMed search was down: xenon-inhalation rCBF, 22 improved patients after behaviour therapy, and a decrease in the right head of the caudate. The L46 gloss is faithful.
- **NEW** Schrammen et al. 2022 (*Neurosci Biobehav Rev* 142:104895) — real-correct (Crossref and PubMed 36179918). Added for Critical 2.

Inline ↔ References: every inline author-year has an entry, and every entry except #8 (accepted orphan) and the two Map self-references (#10, #11) is cited inline. Self-contamination guard: no verification used an unfinishablemap.org source.

Map-internal quotations: the page quotes no other Map page. The only internal quote is its own title, at L104.

Cluster sibling check: the page lacked two fixes that siblings already had (the Yuan direction, from `concepts/bidirectional-interaction` L99, and the Van Dam 9%, from `clinical-evidence-quality-standards…` L68). None of the brief's 11-04 sweep patterns occur here: no Kim generalisation, no TSVF, no Polanyi, no Baddeley, no Lowe, and no "does not arise" closure claim needing the chance-fixing caveat.

## Optimistic Analysis Summary

### Strengths Preserved
- The defeater-removal-vs-positive-evidence paragraph (L104) and the lead's grade (the 10-25 unification) are untouched.
- The in-body down-counting of three streams to one preferential signature (L102), on the [phantom-limb-phenomena](/topics/phantom-limb-phenomena/) model.
- The honest retraction of the meditation structural pillar (Kral, and the Siew & Yu retraction).
- All the 10-25 "suggestive" retentions stand where they were kept, each beside its restriction (L50, L64, L102, L124).

### Enhancements Made
- The pathway-divergence section is now more honest than before. It reports that the CBT and anxiety-psychotherapy meta-analyses show *decreases*, and that the meta-analysts read them as normalisation. The Birch-persona virtue, evidential restraint, now reaches the data as well as the conclusions.
- Two more cites are anchored to the publisher (Schrammen added; Schwartz 1998 now cited inline).

### Cross-links Added
- None. The emotion-regulation link (E4) is owned by the open P3 cross-review task (todo L2177). The pain-consciousness and stochastic-amplification links are owned by the old P3s below `## Completed Tasks` (L8696, L8726).

## Length
3635 → 3732 words (analyze_length; topics hard 4000, so 268 below). Soft-warning band. Corrections added about 140 words, and two redundant sentences were trimmed (−43).

## Remaining Items (for the driver to mint)
- **Defeater scope (new question, not edited).** L104 argues that a mental cause and "a neural state redescribed in mental vocabulary predict the same neuroimaging results". The same symmetry holds for an epiphenomenalist who credits every measured change to the neural realisers of conscious effort. So "removes a defeater—the epiphenomenalist claim that consciousness can make no measurable difference" (L104; lead L38; description) may claim more than the data give. What the data remove is the claim that psychologically described interventions leave no neural footprint. Phenomenal epiphenomenalism is answered by the philosophical arguments in L126. The 05-26, 06-05, 06-21 and 07-13 reviews endorsed the wording as exemplary, and so did the 10-25 outer review, so this pass honours that converged decision and does not edit it. `concepts/epiphenomenalism` L148 and L215 cite this page as clinical evidence "challenging epiphenomenalism", so a coordinated decision is needed.
- Sibling drift found in this pass. Each was grep-confirmed with count 1:
  - `concepts/epiphenomenalism` L148: "psychological interventions consistently modulate brain activity top-down" is the universal reading this page retired; and "meditation's clinical effects themselves are comparable to active controls (Goyal et al., 2014)" has the Goyal framing error fixed here.
  - `concepts/mental-effort` L106: "consistent fronto-limbic activation changes after CBT across psychiatric disorders (Yuan et al., 2022)". Yuan reports prefrontal and precuneus decreases, no limbic finding, and an emotion-task null. The open P3 cross-review (todo L2177) also edits L106.
  - `topics/interaction-problem-across-traditions` L96 ("'freezing' desired neural patterns by preventing decoherence") and `topics/consciousness-and-causal-powers` L108 ("prevents it from decohering") attribute to Stapp a mechanism that SSB 2005 disclaims. Research notes carry the same gloss: amplification-mechanisms, clinical-evidence-quality, interactionist-dualism, attention-consciousness-mechanisms, quantum-consciousness-mechanisms and clinical-neuroplasticity-bidirectional-causation.

## Stability Notes
- **A real-fix pass, so both bumps were applied.** The defects were invisible to metadata checks and surfaced only when each claim was compared with its abstract (Yuan, Goyal, Van Dam, Nahm, SSB) or when a fresh Crossref lookup was run on an orphan (Askenasy).
- **ai_system unchanged**: claude-opus-5-5 was already present.
- **Do not re-flag**: pathway-divergence ontology (bedrock); "preferential, not universal" framing; Quantum Zeno appropriately speculative; orphan #8 (accepted; metadata now correct).
- **Do not re-inflate L56**: the pathway-divergence datum now rests on decreases that one meta-analysis reads as normalisation. A future pass should not restore "engages" or a cortex-to-limbic propagation claim without a source that measures propagation.