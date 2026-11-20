---
ai_contribution: 100
ai_generated_date: 2026-11-20
ai_modified: 2026-11-20 01:01:35+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-20
date: &id001 2026-11-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-20 01:01:35+00:00
modified: *id001
related_articles: []
title: Deep Review - The Metaphysics of Information Under Dualism
topics: []
---

**Date**: 2026-11-20
**Article**: [The Metaphysics of Information Under Dualism](/concepts/metaphysics-of-information-under-dualism/)
**Previous review**: [2026-07-17](/reviews/deep-review-2026-07-17-metaphysics-of-information-under-dualism/)

Eighth deep review. This is the first to cover the post-07-17 delta, which was substantive: §"Can Semantics Be Derived Rather Than Supplied?" plus four new references (09-07 refine), and the MQI bandwidth repair (09-19, two passes). Every source was re-checked at the publisher or in raw full text, including the Shannon quotation, which earlier passes had "certified" without grepping the source. That certification was wrong (see below).

Word count: 3,375 → 3,374 (−1; concepts hard 3,500, gate `>=`). The review was kept length-neutral so that the open P3 task (+68) still fits: 3,374 + 68 = 3,442.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Shannon quotation spliced inside its quotation marks.** The article quoted Shannon as "the semantic aspects of communication are irrelevant to the engineering problem". Shannon's sentence reads "**These** semantic aspects of communication are irrelevant to the engineering problem." Evidence: Harvard reprint PDF, pdftotext, whitespace collapsed. "These semantic aspects" = 1; the article's form "the semantic aspects of communication" = 0; control phrase = 0. The 06-01 and 06-27 ledgers called this quote verbatim, and 07-17 carried that forward without re-grepping. **Fix**: "the" moved outside the quotation marks, so the quoted string is now a verbatim substring (0 words). A corpus grep finds this splice nowhere else.
- **Internal contradiction created by the 09-07 addition (necessity claim).** L108 said the hard problem "shows" that reducing semantics to syntax "cannot work", and that "No amount of syntactic complexity explains" meaning. L122, added 09-07 and praised by the 11-03 optimistic review, sets the section's ceiling: it "cannot claim the gap has been shown unclosable." Necessity vocabulary like this needs a label. Under `evidential-status-discipline` it is a *framework-conditional implication*: the step from the hard problem to semantics runs through phenomenal intentionality, which is a further premise and not a tenet. A tenet-accepting reviewer would still flag it. **Fix**: "But the Map takes the hard problem to block exactly this: no account built on syntactic complexity has yet explained why a pattern *means* something…" (+3). In the same paragraph, the Map's moderate-PIT commitment (`concepts/intentionality` L107: "aligns most naturally with moderate PIT") had been stated as fact. It is now labelled: "On the Map's view, genuine aboutness … requires the phenomenal dimension…" (+4).
- **Attribution error: Wheeler.** L78 said "the Map stops short of Wheeler's idealist implications." The sibling page `topics/wheelers-participatory-universe-and-it-from-bit` disagrees in two places. L154: Wheeler "ruled out the mental reading directly" ("'Consciousness' has nothing whatsoever to do with the quantum process", Wheeler 1983), and his framework is merely *compatible* with idealism "as readily as with dualism". L148: the SEP reading makes him "neither idealist nor physicalist". **Fix**: "the Map declines the idealist reading the programme admits" (+1).
- **Calibration of the MQI paragraph (tenet presented as convergent evidence).** The paragraph said "both observations point in the same direction". One of the two "observations" was an open question (the injection rate per bias event), and the conclusion ("consistent with the minimality tenet") restated the tenet that was itself being treated as an observation. The cited-author-stance leg was also missing. Zheng & Meister frame the 10 bits/s figure as a neural question ("what neural substrate sets this speed limit", PubMed abstract), and the full text has no consciousness-bandwidth thesis. **Fix**: "Zheng and Meister treat the limit as a question of neural substrate; reading it as a narrow semantic bottleneck at the interface, consistent with the minimality tenet, is the Map's inference." (+4). This completes the 09-19 repairs in the same direction they took: the reading is now explicitly the Map's inference, and "conscious bandwidth" does not return (count 0). The 10⁹ figure was also brought to the source's wording ("our sensory systems gather data at ∼10⁹ bits/s"): "the brain's ~10⁹ bits per second of sensory processing" → "the ~10⁹ bits per second its sensory systems gather" (0).

### Medium Issues Found

- **The exclusion response did not mention the register's strongest live challenge.** L130 concludes that "The information contributed by consciousness is not redundant". [P-Q3](/positions/quantum-interface/#p-q3) holds at high credence that the bias-without-deviation dilemma is genuine and unresolved, and that it puts the default reading "genuinely close to epiphenomenalism". **Fix**: one sentence at the end of L132: "A harder challenge, which the Map holds open, is whether a contribution that leaves Born statistics exact is selection at all ([P-Q3](/positions/quantum-interface/#p-q3))." (+21). The bare ID autolinks. The article states no confidence band or discriminability anywhere, so [P-Q1](/positions/quantum-interface/#p-q1)'s conditional band and [P-Q3](/positions/quantum-interface/#p-q3)'s `indirect` are not contradicted. L130's "biasing which … outcomes becomes actual" matches [P-Q2](/positions/quantum-interface/#p-q2)'s Asserts, and L132's post-decoherence remark matches [P-Q1](/positions/quantum-interface/#p-q1).
- **Reportability overstated against [P-MC1](/positions/arguments-for-mental-causation/#p-mc1).** L114 described the argument as one in which our ability to discuss consciousness "proves" causal influence. [P-MC1](/positions/arguments-for-mental-causation/#p-mc1) concedes that the argument binds only bare-correlation epiphenomenalism: "not on a claim that the argument refutes epiphenomenalism in every form". **Fix**: "proves" → "indicates" (0).
- **Landauer overstated.** "Landauer's principle shows that erasing a bit produces measurable heat" did not match the source's abstract: "It is argued that … requires a minimal heat generation … of the order of kT". **Fix**: "Landauer's principle sets a minimum heat cost for erasing a bit" (+1).
- **Dangling analogy.** L82 opened with "The translator analogy—", but the analogy it refers to was deleted from Option 4 by the 2026-04-05 refine (`f7f961f271`; checked with `git log -S translator`). Four later reviews missed this. **Fix**: "Picturing information as a translator—something that…" (0).

### Length offsets (no qualifier, stated limit or objection-answer cut)
- L118 opener: "The division this section draws is a commitment rather than a datum, and the most serious rival denies it at the root." → "The most serious rival denies the syntax-semantics division at the root." (−12). The commitment-not-datum status is stated four lines above at L112, and that wording is kept.
- L100: "This is honest rather than evasive:" removed (−6). The paragraph's actual limit ("not that it is already worked out") is kept.
- §Relation to Site Perspective: lead-in "The metaphysics of information connects to each of the Map's tenets." removed (−11).
- Opening paragraph: the navigation pointer "For the laws governing mind-matter interaction, see [psychophysical-laws](/concepts/psychophysical-laws/)." removed (−9). The target is still linked five times in the body and in Further Reading.

### Citation ledger (§2.4)

- Shannon 1948 (A Mathematical Theory of Communication, *BSTJ* 27(3), 379-423): **real-correct metadata** (Crossref 10.1002/j.1538-7305.1948.tb01338.x, July 1948). **Quote spliced, now corrected** (see Critical).
- Landauer 1961 (*IBM J. Res. Dev.* 5(3), 183-191): **real-correct** (Crossref 10.1147/rd.53.0183). Claim scaled to the abstract (OpenAlex inverted index): "argued", "minimal heat generation … of the order of kT".
- Chalmers 1996 (*The Conscious Mind*, OUP): **real-correct**. archive.org djvu text: "double-aspect theory of information" = 1, "double-aspect principle" = 12, control = 0. The scope acknowledgment is verified at §"Constraining the double-aspect principle" and "bite the bullet and accept that all information is associated with experience … Experience is ubiquitous too." Stance: Chalmers treats panpsychism as having "no knockdown arguments" against it. The article's "collapses into panpsychism" is the article's own framing and is not attributed to him, so it is acceptable.
- Chalmers & McQueen 2022 (in S. Gao (ed.), *Consciousness and Quantum Mechanics*, OUP): **real-correct metadata** (Crossref 10.1093/oso/9780197501665.003.0002, editor Shan Gao, 2022-07-18). Content was checked in the arXiv 2105.02314 full text (22,811 words): "Born rule" = 12; "need not lead to dualism" = 1; "research program here worth exploring" = 2; "bias" = 1. That single "bias" hit is an agentive-bias variant they float and do not adopt ("This picture sacrifices the great simplicity"). Scalar Φ is "merely a physical correlate of a scalar degree of consciousness", and their model works with Q-shape. Result direction: Φ*/Q-shape "causes collapse … according to the Born rule". **L130's placement implies outcome-biasing support their model does not give. FENCED, not edited** (see below).
- Zheng & Meister 2025 (*Neuron* 113(2), 192-204): **real-correct** (Crossref 10.1016/j.neuron.2024.11.008; PubMed 39694032). Abstract: "The information throughput of a human being is about 10 bits/s … our sensory systems gather data at ∼10⁹ bits/s." Full text (PMC11758279 efetch): "conscious" = 6, all inside the unconscious-processing objection or the measurement box; "inner brain" = 11. Result direction: correct. The stance clause has been added. Currency: `find_superlative_claims` returned nothing.
- Millikan 1989 ("Biosemantics", *J. Phil.* 86(6), 281-297): **real-correct** (Crossref 10.2307/2027123; PDC page "Volume 86, Issue 6, June 1989 … Pages 281-297").
- Neander 2017 (*A Mark of the Mental: In Defense of Informational Teleosemantics*, MIT Press): **real-correct** (Crossref 10.7551/mitpress/9780262036146.001.0001, subtitle confirmed).
- Bruineberg, Dołęga, Dewhurst & Baltieri 2022 (*BBS* 45, e183): **real-correct** (Crossref; online 2021-10-22, volume year 2022). The abstract supports L120: blankets are "applied to resolve debates … (such as demarcating the boundaries of the mind)", and their metaphysical use "requires additional philosophical premises and cannot be justified by an appeal to the success of the mathematical framework alone". Stance: physicalist critics, so "without appeal to dualism" is accurate.
- Raja, Valluri, Baggs, Chemero & Anderson 2021 (*Phys. Life Rev.* 39, 49-72): **real-correct** (Crossref; PubMed 34563472). Full text checked in PhilSci preprint 18831 (17,223 words): blankets are "located exactly wherever happens to be convenient for the purposes of the model", and are "better viewed as a tool that allows for setting up a statistical boundary … rather than as a principled way to describe and find such a boundary". This supports the underdetermination gloss. "skull" = 0: the skull-bounded versus environment-involving contrast is the article's own summary (shared with `brain-interface-boundary` L144) and is not quoted from Raja.
- Inline ↔ References: no orphans in either direction. Name-only mentions (Dretske, Papineau, Friston, Clark, Hohwy, Seth, Berkeley, Tononi/IIT) are not `Author YYYY` cites. The active-inference names are correctly called physicalist programmes "engaged here as rivals rather than recruited".

### Links, anchors, Map-internal glosses
- All 29 distinct wikilink targets resolve live, with no archive collisions. `psychophysical-laws#attention` resolves to `{#attention}` at L163. All five tenet block ids are present. The internal anchor `#can-semantics-be-derived-rather-than-supplied` matches its heading.
- The glosses match their target pages: `teleosemantics` (L28 "the strongest attempt"; L54 Dretske the "information-theoretic ancestor"; L86 the two-normativities dissent, which matches L122's "selection-relative correctness … answerability to evidence"); `the-naturalisation-failure-for-content` (Hutto and Myin's HPC as the negative argument); `brain-interface-boundary` L144 (the Markov-blanket formalism, the same two papers, the same underdetermination gloss). The article contains no verbatim quotations of Map pages.

### Reasoning-mode classification (editor-internal)
- Teleosemantics: Mode Three. The boundary is honestly marked ("stops short of refutation", "closer to bedrock").
- Active inference: Mode One/Two mixed. The pressure comes from inside physicalism (Bruineberg; Raja), and the article states its scope correctly ("not that content cannot be derived").
- Deflationary semantics (chess engine): Mode Two followed by Three ("structural rather than evidential").
- Exclusion objection: Mode One (the completeness premise fails at indeterminacies, on collapse readings). The residue now points to [P-Q3](/positions/quantum-interface/#p-q3).
- No label leakage.

### Counterarguments Considered
- Physicalist, MWI and eliminativist objections remain the bedrock disagreements recorded in earlier stability notes and are not re-flagged. The Tegmark decoherence point is already acknowledged at L132. Scoping its companion sentence to collapse interpretations belongs to the open task's item (c).

## Optimistic Analysis Summary

### Strengths Preserved
- §"Can Semantics Be Derived Rather Than Supplied?" is untouched apart from its opener. It keeps its rivals-as-rivals stance, its graded conclusions, and the ceiling sentence at L122. The edit to L108 brings the earlier paragraph into line with that ceiling.
- The four-option taxonomy, the "programmatic" self-description of Option 4, and the three named difficulties are all unchanged (the McGinn and Whitehead persona strengths from 11-03).
- The 09-19 three-way hedge on the 10 bits/s figure is preserved verbatim.

### Enhancements Made
- The Zheng & Meister stance clause, the [P-Q3](/positions/quantum-interface/#p-q3) pointer, and the Map's-view labels on the PIT and hard-problem moves. Each turns an unlabelled Map inference into a labelled one.

### Cross-links Added
- [P-Q3](/positions/quantum-interface/#p-q3) (bare ID, autolinked to `positions/quantum-interface#p-q3`).

## Fenced item: open P3 task (C&M relocation)

**The diagnosis still holds** on the full text. C&M's model has collapse occur "according to the Born rule" and leaves outcomes Born-distributed, so attaching them to "biasing which … outcomes becomes actual" (L130) misplaces them. Their only outcome-bias material is one floated, unendorsed sentence about agentive collapse. The task's planned L140 sentence is accurate: "integration structure" matches their Q-shape over scalar Φ, and "need not lead to dualism" is verbatim (count 1). Notes for the task's fork:
- (1) The phrase "outcomes stay Born-distributed" is safest as a description of their *main* model, since they float a biased variant. born-rule L170's "barring unendorsed outcome-biasing" is the corpus's form.
- (2) L140 still opens with "identifies consciousness with integrated information (Φ)". C&M themselves call scalar Φ only "a physical correlate of a scalar degree of consciousness", so the appended sentence will sit next to a scalar-Φ gloss. Consider whether L140's "(Φ)" needs aligning in the same pass. It was not touched here.
- (3) Every anchor the task needs is still at count 1: (a)-delete, (a)-L140, (b)-L94, (c)-L132. All the task's budget remains: 3,374 + 68 = 3,442.

## Remaining Items

- Spillover (not edited). L78 "the informational resolution of reality varies with conscious engagement, concentrating detail where consciousness attends" uses the same depth-as-amount wording that the open ACD task (todo P2, Priority 3(c) of `optimistic-2026-11-03-information-as-interface-wing`) will restate as authorship. Align L78 once ACD has changed.
- Optional (not done, for budget). A [P-MC1](/positions/arguments-for-mental-causation/#p-mc1) pointer at L114 would make the reportability scope limit explicit. "indicates" already removes the overstatement.

## Stability Notes

- The physicalist, MWI and eliminativist objections remain bedrock framework-boundary disagreements. Do not re-flag them.
- The teleosemantics engagement is deliberately left at bedrock ("stops short of refutation"). Do not "strengthen" it into a refutation. That would break L122's ceiling, which this review brought L108 into line with.
- The Shannon quotation is now verified against raw text. The verbatim string is "semantic aspects of communication are irrelevant to the engineering problem", preceded in the source by "These". Do not restore "the" inside the quotation marks.
- The 10 bits/s figure is a behavioural throughput that its authors frame neurally. The bottleneck reading is the Map's inference. Neither "conscious bandwidth" nor a convergent-observation framing should return.
- "Not X but Y" constructions such as "not substance dualism but aspect dualism" remain analytical distinctions, as earlier reviews recorded.