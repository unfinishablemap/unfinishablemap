---
title: "Deep Review - Phenomenal Acquaintance"
created: 2026-11-19
modified: 2026-11-19
human_modified: null
ai_modified: 2026-11-19T16:41:21+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-19
last_curated: null
---

**Date**: 2026-11-19
**Article**: [[phenomenal-acquaintance|Phenomenal Acquaintance]]
**Previous review**: [[deep-review-2026-07-30-phenomenal-acquaintance|2026-07-30]]

This is the seventh pass. Its primary lens was **sibling consistency**. Since July the corpus has gained three pages that state what acquaintance is and how strongly the Map holds it: `concepts/revelation-thesis` (10-01), `topics/acquaintance-without-causation` (10-19) and `topics/singular-thought-and-acquaintance` (10-21). Four edits also landed on this page after the 07-30 review and had never been reviewed: the singular-thought sentence at L50 (10-21), the revelation-thesis link at L140 (10-01), the 11-09 rewrite of the Bidirectional Interaction and Occam paragraphs (`d0693adfc4`), and the 11-18 language-anchoring change at L110 (`a41af6f79a`). The 08-02 Chalmers 2006/2007 settlement (`ef3ba9200b`) reached the References entry.

Result: four sibling or tenet inconsistencies were fixed, and a calibration overclaim that the 2026-10-20 tenet check had flagged at L144 but never queued was discharged. The body argument, the two-step architecture and every Stability Note item are unchanged.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Misattribution in the new Bidirectional Interaction paragraph (FIXED).** The 11-09 rewrite read "The physicalist's answer is a common cause rather than a coincidence: on Jackson's (1982) structure the brain state produces both experience and report". The paragraph's opponent is the epiphenomenalist ("If acquaintance were epiphenomenal…"). In 1982 Jackson was an epiphenomenalist property dualist, and the anchor section this sentence links to, `self-stultification#The Coincidence Response`, opens "The epiphenomenalist need not call the correlation luck: on Jackson's (1982) common-cause structure…". **Verified at the primary source**: JSTOR scan of "Epiphenomenal Qualia", *Phil. Quarterly* 32(127), Apr 1982, pp. 127–136 (sfu.ca/~jillmc/JacksonfromJStore.pdf, pdftotext, whitespace collapsed). §IV reply (i), p. 133: "The epiphenomenalist can say exactly the same about the connection between, for example, hurtfulness and behaviour. It is simply a consequence of the fact that certain happenings in the brain cause both." The behaviour includes "saying 'It hurts'". Fix: "The physicalist's answer" → "The epiphenomenalist's answer".

- **Report-only reading contradicted by the page it links (FIXED).** The same paragraph said "the pressure falls on the report channel, since asserting what acquaintance reveals is an outbound physical act." `acquaintance-without-causation`, the link target of the clause before it, keeps causation for **use and voice** ("*Using* what one knows (inference, memory, perceptual justification) and *voicing* it (report, assertion) still do", L37). It calls its conclusion "broader than a report-only reading, because against Chalmers's property dualist the use channel presses at least as hard as the voice channel" (L88). This page stated exactly the reading its sibling rejects. Fix: "the pressure falls on what is done with that knowledge—reasoning from it, and reporting it in an outbound physical act." The debt sentence followed: "lets a report voice what acquaintance knows" → "lets reasoning and report proceed *from* what acquaintance knows".

- **The paragraph omitted the cost its sibling says the repair carries (FIXED, Medium-to-Critical).** AWC L106–108: plain interactionism does no better than epiphenomenalism at the use and voice channels. The Map clears the bar only through its tenet clause that consciousness biases outcomes "toward patterns that express its content", which the tenets hold as a posit ("a posit the interface argument leaves open, not a result it secures", `tenets#^tenet-3-standing`). Without that sentence the page pressed the debt on the epiphenomenalist and was silent about the Map's matching one. A tenet-accepting reviewer would flag that asymmetry. Added: "The Map's own interactionism meets that demand only if consciousness acts in virtue of what it presents, which the tenets [[tenets#^tenet-3-standing|posit without securing]]." The rendered anchor `/tenets/#tenet-3-standing` is live; AWC uses it too.

- **Calibration overclaim in the Dualism paragraph (FIXED).** L144 closed with "Acquaintance provides the starting datum; the philosophical arguments establish that the datum points beyond the physical." It contradicted three texts. The page's own L98 says "The recognitional account remains a live rival, not a refuted one". `revelation-thesis` L80 says the Dualism tenet "continues to rest on the explanatory gap and conceivability", which are contested. `singular-thought-and-acquaintance` L87 calls the dualist step "argued and contested in [[phenomenal-acquaintance]]'s treatment of Loar". **The 2026-10-20 tenet check (item 9) flagged this exact sentence and proposed a replacement, but no task was minted.** The 11-09 refine-draft fixed L146 only (grep of open todo: no task owns L144). Fix: "Acquaintance provides the starting datum; carrying it beyond the physical is the work of further arguments, which the recognitional account still contests." That is +6 words, and "it" refers to the datum.

- **Lead labelled the Map's case "substance dualism" (FIXED).** The lead said acquaintance's irreducibility is central to the Map's case "for substance dualism: the claim that what acquaintance reveals belongs to a domain that physical description cannot in principle reach." The Dualism tenet's Definition (tenets L53) says the commitment "is neutral between substance and property dualism … What matters is irreducibility". The contrast with non-reductive physicalism, which rejects property dualism as well, also needs only dualism, and the gloss after the colon is already neutral between the two. The text has been there since 2026-02-20 (`6f0c49a46d`) and no prior review flagged it. Fix: "for substance dualism:" → "for dualism:" (−1 word). The Stability Note's "do not re-open the lead's Russell split" is untouched: the Russell sentence was not edited.

### Medium Issues Found

- **Moderate PIT inconsistency (FIXED).** L122 said "Without acquaintance, intentionality reduces to functional covariation". The Map adopts *moderate* phenomenal intentionality theory (`intentionality` L103–107; `singular-thought-and-acquaintance` L89: "all non-phenomenal intentionality derives from phenomenal intentionality"). On moderate PIT, standing beliefs and a book's or an LLM's words have **derived** intentionality, which is neither acquaintance nor mere covariation (`singular-thought-and-acquaintance` L37: "The model's words can still refer derivatively"). Fix: "Intentionality that neither involves acquaintance nor derives from a mind that has it reduces to functional covariation…" The preceding sentence, "Acquaintance is the mechanism", which AWC L56 quotes, is untouched.

- **Occam paragraph (11-09; reviewed, kept).** "The reductions still owe an account of why Mary's encounter *feels* novel." A Loar defender would say the new recognitional concept supplies that account, so the clause is the Map's judgement. It sits inside a sentence already in the Map's voice ("The Map lets neither…"), and the paragraph applies Tenet 5 symmetrically, so I did not add a further hedge.

- **L110 language anchoring (11-18; reviewed, kept).** It agrees with `symbol-grounding-problem` L49, which reports that Coelho Mollo and Millière (2026) give LLMs a route to referential grounding that the Map contests. It also agrees with `voids/consciousness-only-territories` L59, whose sentence it mirrors. "Information processing alone" stays inside CoT L51's "does not by itself yield first-person knowing".

### Publisher-of-Record Citation Ledger

The References block changed only through `ef3ba9200b`, which expanded the Chalmers 2007 tuple. The body gained one inline cite, "Jackson's (1982)", on 11-09. Both were re-verified at source this pass. Entries with DOIs were re-checked through Crossref. Entries without DOIs are unchanged since the 07-30 publisher check, and that check is carried forward.

- Russell 1910, "Knowledge by Acquaintance and Knowledge by Description," *Proc. Arist. Soc.* 11:108–128. State: **real-correct (volume-year convention)**. Crossref 10.1093/aristotelian/11.1.108 confirms vol 11, issue 1, pp. 108–128, issue date 1911-06-01, and SEP cites "1910–11". "1910" is the first year of the session volume. The corpus splits 6 (1910) to 2 (1910–11, including `singular-thought-and-acquaintance`). This is a convention, so it is not changed.
- Russell 1912, *The Problems of Philosophy*. State: real-correct (carried forward from 07-30).
- Nagel 1974. State: **real-correct** (Crossref 10.2307/2183914: *Phil. Review* 83(4), p. 435).
- Jackson 1982, "Epiphenomenal Qualia," *Phil. Quarterly* 32:127–136. State: **real-correct** (Crossref 10.2307/2960077: vol 32, no 127, Apr 1982). **Inline claim verified at the JSTOR scan, p. 133** (see Critical). **Result-direction leg**: the paper reports the common-cause structure as the *epiphenomenalist's* reply, and the page now says so. **Author-stance leg**: Jackson was an epiphenomenalist property dualist in 1982 and later became a physicalist. He is not presented as endorsing interactionism.
- Lewis 1988; Nemirow 1990; McDowell 1994; Loar 1997; Rosenthal 2005; Chalmers 2010; Gertler 2012. State: real-correct (carried forward from 07-30; the entries are unchanged).
- Harnad 1990. State: **real-correct** (Crossref 10.1016/0167-2789(90)90087-6: *Physica D* 42(1–3):335–346).
- Conee 1994. State: **real-correct** (Crossref 10.1080/00048409412345971: *AJP* 72(2):136–150). The stance clause, physicalist ally of the category and opponent of the conclusion, is retained.
- Kelly 2001. State: **real-correct** (Crossref 10.1215/00318108-110-3-397: *Phil. Review* 110(3):397–420). Not re-litigated.
- Chalmers 2007, "Phenomenal Concepts and the Explanatory Gap," in Alter & Walter (eds), OUP, pp. 167–194, doi 10.1093/acprof:oso/9780195171655.003.0009. State: **real-correct**. Crossref gives 2007 and pp. 167–194, and the year follows the 08-02 corpus settlement (2007 across 15+ live files). **Author stance**: naturalistic property dualist, not an interactionist; the page uses only his zombie dilemma against Loar.

**Superlative sweep**: `find_superlative_claims` returned nothing. **Verbatim quotes**: none on the page (terms of art only).

### Map-Internal Quotation and Paraphrase Re-grep

- AWC quotes this page five times: L70 "No inference, representation, or intermediary stands between subject and quality" and "where causal chains mediate between perceiver and world"; L132 "supplies *apodictic* evidence for the existence of experience"; L130 "the relation from judgements based on it"; L122 "is the mechanism". **All are still verbatim**, because none of the edited sentences contains them.
- This page's paraphrases of other pages were checked against their current text: `self-stultification#The Coincidence Response` (the misattribution was fixed); `constitutive-vs-referring-observation` L51–55 ("partial precursor", consistent with "metaphysical descendant"); `acquaintance-void` L69/L113; `phenomenal-presentation` L34 ("passive, felt showing-up"); `phenomenal-authority-and-first-person-evidence` §Phenomenal Conservatism and §Husserl's Evidence Taxonomy (both anchors live); `consciousness-only-territories` L51/L59; `symbol-grounding-problem` L49. All agree.
- Sentences elsewhere in the corpus that quoted the replaced wording: grep found only `reviews/tenet-check-2026-10-20.md` (the L144 flag this pass discharges).

### Sibling-Consistency Table

| Page | Claim about acquaintance / this page | Agrees? | Action |
|---|---|---|---|
| `revelation-thesis` L36–38, L76–80 | Map holds weak Revelation (existence plus part of character), denies strong; "experience reveals that the quality is non-physical" would over-reach; Dualism rests on the gap and conceivability | Yes for L132 (apodictic presence, fallible content) and L98 (separate steps). **No for L144 "establish"** | L144 recalibrated |
| `revelation-thesis` L72, L84 | This page is "the axis of" Cortesi's A-Rev; "The relation whose strength Revelation parametrises" | Yes | none |
| `revelation-thesis` L72 (two transparency senses) | Corpus uses Metzinger's sense, not Goff's | Yes. L140 uses the representationalist (diaphanousness) sense, linked to the Metzinger page | none |
| `acquaintance-without-causation` L37, L80–88 | Knowing needs no causation; pressure on use **and** voice; not report-only | **No**: L146 was report-only | L146 fixed |
| `acquaintance-without-causation` L106–108 | Map's escape runs through the content-efficacy clause, an open posit | **No**: L146 was silent | cost sentence added |
| `acquaintance-without-causation` L47–56, L126 | Five quotes of this page; "the relation granted here to the epiphenomenalist" | Yes (verbatim) | none |
| `self-stultification` L147 | Common-cause reply is the **epiphenomenalist's**, on Jackson 1982 | **No**: L146 said "physicalist's" | fixed, primary-verified |
| `singular-thought-and-acquaintance` L47–49 | Russell's principle, description of particulars, Caesar | Yes (L50) | none |
| `singular-thought-and-acquaintance` L87, L121 | Dualist step "argued and contested" in this page's Loar section; "the dualist step" | Yes (L98); L144 now matches | via L144 fix |
| `singular-thought-and-acquaintance` L37, L89 + `intentionality` L103–107 | Map adopts moderate PIT; derived intentionality exists | **No**: L122 "Without acquaintance … reduces to functional covariation" | L122 fixed |
| `tenets` L53 | Dualism tenet neutral between substance and property dualism | **No**: lead said "substance dualism" | lead fixed |
| `intrinsic-nature` L71, L112 | Acquaintance as "the contested relation by which consciousness is supposed to know its own intrinsic nature" | Yes. The page never claims acquaintance delivers a quiddity | none |
| `consciousness-only-territories` L59; `symbol-grounding-problem` L49 | Anchoring sentence; referential-grounding concession | Yes (11-18 edit mirrors them) | none |

### The Acquaintance-Premise Stance This Page Takes

The page states in the Map's voice (L144) that "qualitative character is intrinsic and non-structural", so that what acquaintance reveals lies beyond physical description. On *holding* a non-structural item, this puts it on the same side as `ontic-structural-realism` L89. It explicitly does **not** rest that claim on acquaintance. L98 reads: "Direct epistemic access and the conclusion that its object lies beyond physical description are therefore separate steps. The second carries the dualist result, and it must be argued rather than read off the first." L144 now reads: "carrying it beyond the physical is the work of further arguments, which the recognitional account still contests." On what acquaintance itself *delivers*, the page therefore sides with `revelation-thesis` L76. It never uses the Russellian "the one intrinsic nature" or quiddity wording that the 11-19 optimistic review traced from OSR to `intrinsic-nature` L77. In effect the page already states the consistent grade that review proposed: acquaintance at weak strength, with the non-structural claim held as a separately argued and contested premise. The revelation/OSR tension was **not** resolved here; the open P3 owns it. One residual: L124, "acquaintance … reveals the qualitative character that structure and function do not encode", is the sentence closest to the "acquaintance gives one non-structural item directly" form. It is left unchanged (watch item below).

### Named-Opponent Engagement Classification (editor-internal)

- Epiphenomenalist (Jackson 1982 common cause): **Mode Three**. The common cause is conceded to make the tracking lawful. The residue is marked as an explanatory cost, not a refutation, and the Map's own matching debt is now stated.
- Loar (recognitional concepts): **Mixed** (Mode Two opening, Mode Three residue; "live rival, not a refuted one"). Unchanged.
- Conee: **Mode Three**. Unchanged.
- Dennett, Lewis, HOT and representationalist replies: **Mode One**. Unchanged.
- Label-leakage grep (editor vocabulary, "load-bearing", bold "Evidential status:"): none in the body.

### Calibration Check

Two possibility-to-probability slippages were removed: "establish" at L144, and the one-sided debt at L146. The lead's "substance dualism" was a framework-statement error, not a slippage, but it is correctable inside the Map's own framework. After the fixes, a tenet-accepting reviewer would flag nothing as overstated. The L124 watch item is the only candidate.

## Optimistic Analysis Summary

### Strengths Preserved

- The two-step architecture: acquaintance secures the datum, and separate argument carries the ontology. L144 now closes it at the same calibration as L98.
- The 11-09 Occam paragraph's symmetric Tenet 5 use ("neither that apparent simplicity nor any economy claimed for its own view").
- The 11-09 grant that knowing needs no causal link. It is the right concession, and AWC's whole argument depends on it.
- The Conee stance clause, the Russell "the so-and-so" exegesis, the apodictic/assertoric resolution, and the maps/territory image.

### Enhancements Made

- One sentence stating the Map's own content-efficacy debt (Bidirectional Interaction), closing the gap between this page and AWC.

### Cross-links Added

- [[tenets#^tenet-3-standing]] (new anchor link in the Bidirectional paragraph).

## Word Count

`analyze_length`: 3,106 → 3,149 (+43; concepts hard 3,500, gate `>=`, 350 words of room left). Additions: L146 about +28, L122 +10, L144 +6, lead −1. No qualifier, stated limit or objection-answer was cut.

## Remaining Items

- **L96 first sentence, "denies it requires substance dualism"**, is accurate (non-reductive physicalists do deny substance dualism) but narrower than the lead now is. It was left untouched because the open P3 "Chalmers 2007 master-argument dilemma misread on three more concept pages" (todo ~L2917) owns L96. That fork could change it to "dualism" at zero cost. The "the same apparent gap" sentence was not touched.
- **`self-stultification` L149** still words the Coincidence Response's debt as "*knowledge* of experience without causal traffic from it". This page and AWC concede that for knowing, so the debt now concerns use and voice. The open P3 on the self-stultification hub ("finish the narrowing", todo, directly below the Chalmers P3) is the natural owner. No new task.
- **Watch item (L90)**: "every reductive strategy must either deny that Mary learns anything or redefine 'learning'…" sits loosely beside L86, which says Loar grants a new concept. It was stable through six passes and is read as the Map's verdict, so it was not changed.
- **Watch item (L124)**: see the stance section.
- **Russell year convention**: the corpus splits 1910 vs 1910–11 (6:2). Not a defect; any harmonisation should be corpus-wide.

## Stability Notes

Standing notes remain in force: eliminative and Dennettian denials of acquaintance, the Buddhist presupposed-subject concern, and MWI or physicalist dissatisfaction with the two-step case are bedrock. Do not re-open the Kelly 2001 citation, the Husserl evidence taxonomy, or the lead's Russell two-way split (do not re-introduce "ability knowledge"). Conee is a physicalist ally of the third category and an opponent of the dualist conclusion; keep the clause. Russell's knowledge by description is particular.

**New standing notes.**
1. The common-cause reply at L146 is the **epiphenomenalist's** (Jackson 1982, p. 133, primary-verified). Do not relabel it "physicalist".
2. The pressure after the acquaintance concession falls on **use and voice**, not report alone, matching `acquaintance-without-causation`. The Map's own content-efficacy debt sentence is the calibration; do not trim it as hedging.
3. The Dualism tenet is neutral between substance and property dualism. Do not re-introduce "substance dualism" as the target of the Map's case.
4. L122 follows moderate PIT: derived intentionality is neither acquaintance nor bare covariation.
5. L144's close ("which the recognitional account still contests") matches L98. Do not upgrade it back to "establish".

**Convergence assessment.** The body argument is converged. Every defect found this pass came in on the sibling axis: new pages restated the Map's commitments, or an edit after July imported a framing the anchor page had already corrected. Future triggers from cross-link bumps can be deprioritised. A re-check is warranted only if `acquaintance-without-causation`, `revelation-thesis` or the tenets' Tenet 3 standing paragraph changes.
