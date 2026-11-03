---
title: "Deep Review - Interventionist and Counterfactual Dualism"
created: 2026-11-03
modified: 2026-11-03
human_modified:
ai_modified: 2026-11-03T15:47:25+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-03
last_curated:
---

**Date**: 2026-11-03
**Article**: [[interventionist-and-counterfactual-dualism|Interventionist and Counterfactual Dualism]]
**Previous review**: [[deep-review-2026-08-24-interventionist-and-counterfactual-dualism|2026-08-24]] (third pass); earlier [[deep-review-2026-07-25-interventionist-and-counterfactual-dualism|2026-07-25]], [[deep-review-2026-07-15-interventionist-and-counterfactual-dualism|2026-07-15]]

Fourth pass, and the first to cover what moved since 2026-08-24. Two commits changed the article in that window. `fa74bacee3` (refine-draft, 2026-09-07) added the whole `## The Equivocation Charge Against the Counterfactual Branch` section (~940 words) and references 10–13. `ede220b340` (2026-09-15) added the Gibb double-prevention sentence and reference 14. No deep review had read either addition, so this pass concentrated there, re-reading Rellihan (2021) in full from the publisher PDF rather than trusting the 09-07 refine's "fourteen quotes grep-verified" certificate.

Length: 3787 → 3800 words (`soft_warning`, 200 below the 4000 hard limit). Length-neutral intent: two trims (−11) offset part of the corrections' additions (+24). No superlative claims (helper returns empty). No editor-vocabulary label leakage. No "This is not X. It is Y." and no "load-bearing".

**Lines left alone because open tasks own them.** L39, L100 and L106 ("closure-preserving" / "strong-closure-preserving" said of trumping) belong to the open P3 closure-wording task whose primary file is this article. L65/L67 (Lowe credited with the observational-closure distinction) belong to the open P3 originator task against `concepts/observational-closure`. Neither was touched.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Rellihan's second horn misdescribed as independent of the realizer wedge (fixed).** L94 said: *"Rellihan's weaker horn survives either way, since it concerns the strategy rather than realizers."* In the source both horns are consequences of his (6), "If M had not been instantiated, P* might (still) have been instantiated", which he derives from (5) (the total-realizer counterfactual) together with (1): "And (6) in turn makes problems for (4). If counterfactual dependence is necessary for causation, M does not cause P*. If counterfactual dependence is only sufficient for causation, no appeal to counterfactuals will by itself succeed in showing that M causes P." So the weaker horn concerns realizers exactly as much as the stronger one, and if the Map's exemption holds it lapses with the first. The sentence put a Map reconstruction in Rellihan's mouth (source/Map conflation). The Map's real residual point, that Kroedel's dualist counterfactual depends on how the psychophysical laws behave across worlds, was sound. It is now stated as the Map's own worry and tied to the premise Rellihan's endnote 5 itself calls "the more controversial". New text:

> Rellihan's second horn lapses with the first if the exemption holds, since both rest on the realizer wedge. What survives is the Map's own worry: Kroedel's dualist pair still needs the counterfactual Rellihan's endnote calls "the more controversial" — had the experience been absent, its physical correlate would have been too — and whether that holds turns on how the psychophysical laws behave across worlds, which is the point in dispute.

The old second sentence ("establishing it settles nothing until one has settled which worlds count as closest") is gone. Its "settles nothing" was also muddled: if dependence is sufficient for causation, establishing the dependence settles causation, and the real difficulty is establishing it.

**2. Vaassen's "Dualism and Exclusion" (2021) presented as part of the pro-dualist interventionist branch (fixed: cited-author-stance leg).** L94 said *"Nor is the interventionist branch a bystander: Rellihan engages Vaassen's 'Dualism and Exclusion' (2021)…"*, and reference 13 called it "the co-causation paper reference 10 rebuts". The paper's own abstract (OpenAlex reconstruction of the publisher abstract, `10.1007/s10670-019-00118-1`) closes: "It is therefore still plausible that the latter causally exclude the former and that compelling exclusion arguments against dualism can be formulated by using a weaker exclusion premise." In that sentence the latter are the underlying physical properties and the former the dualist conscious properties. So it is an **exclusion-tightening paper against dualism**. Core/total realizer co-causation is its example of the tight relation that it says dualist properties lack. Rellihan's text has **zero** hits for `interven`, `Woodward` and `difference-mak`, and his paper (accepted May 2021) predates the 2024 interventionist account. So he does not engage the interventionist branch at all. The body now says so. Reference 13 now reads "another exclusion-tightening paper, whose core/total co-causation claim reference 10 rebuts". The correction also strengthens L71's trajectory narrative: both 2021 Vaassen papers tighten exclusion, and the 2024 paper is the escape.

**3. Internal contradiction: the article twice said the Map "has never answered" Rellihan, then answered him for ~700 words (fixed).** L41 (lead: "a published attack the Map has never answered") and L86 ("and the Map has never answered it") were true when the 09-07 refine was minted, since the attack was absent from the corpus. The same refine wrote the answer and left both clauses standing. Both are deleted (−11 words). No other page carries a "never answered" claim about Rellihan: `grep -rF Rellihan` across live content hits only this article and its research note.

### Medium Issues Found

**4. Gibb overgeneralised (fixed).** L80 said that on Gibb's account "the experience is no cause at all". Her chapter abstract (OpenAlex, `10.1093/acprof:oso/9780199603770.003.0009`) scopes the claim: "a double preventer is not a cause of the event that it prevents from being prevented", and the mental event acts "by preventing a mental event that would have prevented it". Now "no cause of the behaviour". That matches the source and the hub's wording at `concepts/causal-exclusion-argument` L80 ("denies that the mental event is a cause of the bodily movement at all").

**5. Lewis attribution compressed (fixed, calibration-down).** "a weighting of future similarity that … Lewis called 'of little or no importance'" made a claim about Lewis that is really Rellihan's application. Rellihan's endnote 11: "even on Lewis's approach it is 'of little or no importance' (1979, p. 472)". Lewis's item (4) applies the phrase to *approximate similarity of particular fact*, and his item (2) still weights perfect match in any region. Now "Lewis's, on Rellihan's reading, rates 'of little or no importance'". The quoted phrase is verified in Rellihan's raw text. Lewis's own wording is search-corroborated (item (4), p. 472, multiple secondary sources) but was **not** grep-verified against Lewis's text: all three PDF hosts refused automated fetches.

**6. Spillover for the open closure-wording task (NOT fixed, out of scope).** The "trumping preserves strong closure" phrasing that task targets at L39/L100/L106 also occurs at **L108** ("The trumping route's distinctive prize is *strong*-closure preservation plus zero trajectory footprint") and arguably **L112** ("for its stronger closure-preservation"). The sibling this article quotes in L106, `concepts/trumping-preemption` L89, now reads "trumping is difference-making-free and violates closure only unobservably". So L106 contradicts the sentence it quotes. These lines were left for the task, whose loci should be widened to include L108/L112.

### Counterarguments Considered

- **Eliminativist (Churchland):** the two-cause/one-cause axis presupposes folk-psychological experiences as causal relata. Bedrock, outside the tenets.
- **Physicalist (Dennett):** trumping's authority-without-difference is epiphenomenalism renamed. Already conceded in the article (the ensemble-level-epiphenomenalism flag, L96/L104). No change.
- **Quantum skeptic (Tegmark):** per-trial selection survives decoherence only by stipulation. Not this article's burden; Tenet 2 is handled at the strict and intermediate readings with the marginal/conditional distinction intact.
- **Many-worlds (Deutsch):** closest-world semantics presupposes a single actual world. Bedrock (Tenet 4).
- **Empiricist (Popper):** trumping's zero footprint is unfalsifiable. The article already makes this its own point: the preference is a methodological posture, and the strict channel stays exposed to conditional residual-structure tests.
- **Madhyamaka (Nagarjuna):** counting causes reifies them. Bedrock.
- **Rellihan (the article's main named opponent), reasoning mode:** mixed, unchanged in kind. Mode One for the exemption: it is earned inside Rellihan's framework from his own statement that the wedge runs on the background-conditions conjunct, not the laws. Mode Three for the residue. Critical 1 moves part of what was presented as Rellihan's residue into the Map's own voice, which makes the boundary-marking more honest, not weaker.

### Publisher-of-Record Citation Ledger

Crossref pulled fresh this pass for all ten DOI-bearing references. Every tuple (author, title, venue, volume, issue, pages, year) matches the article.

- Kroedel 2015, *Noûs* 49(2):357–375, `10.1111/nous.12028`: **real-correct** (Crossref print 2015-06). Quote "some physical events counterfactually depend on, and are therefore caused by, mental events" was verified verbatim 2026-08-24 against the raw preprint text. Not re-fetched; untouched.
- Vaassen 2024, *AJP* 102(4):978–998, `10.1080/00048402.2024.2335325`: **real-correct**.
- Vaassen 2021, *Synthese* 198(11):10341–10353, `10.1007/s11229-020-02723-y`: **real-correct**.
- Vaassen 2022, *Phil Studies* 179(9):2823–2843, `10.1007/s11098-022-01803-8`: **real-correct**.
- Zhong 2023, *Asian J Phil* 2, art. 71, `10.1007/s44204-023-00110-1`: **real-correct** (article-number 71 confirmed).
- Mills 1996, *APQ* 33(1):105–117: carried forward (no DOI; resolved 2026-07-25).
- Lowe 2003, Walter & Heckmann eds., pp. 137–154: carried forward (no DOI).
- Rellihan 2021, *Thought* 10(4):249–256, `10.1002/tht3.502`: **real-correct**. Sole author (the second Crossref "author" is the Philosophy Documentation Center). **Full text re-fetched** from pdcnet.org (8 pp PDF, `pdftotext`, whitespace/de-hyphenation flattened). Verbatim hits, each 1×: "has consequences for any attempt to establish the reality of downward causation by appealing to counterfactual theories thereof"; "core realizers do not necessitate their corresponding mental states"; "the purported physical effects of mental properties do not counterfactually depend upon the total realizers of these properties"; "no appeal to counterfactuals will by itself succeed in showing that mental properties are causes"; "follows from a commitment to physicalism"; "arguendo"; "has nothing to do with the fact that they include the laws of nature"; "their other conjunct—the background conditions"; "even when the mental supervenes on the physical with only nomological necessity"; "argues that core and total realizers can 'co-cause' an effect"; "of little or no importance"; and, new this pass, "the more controversial second premise". Negative control `zzzneg-control-xq` returned 0. The reference list carries Kroedel 2008, 2015 (*Synthese*) and 2020 only, with no *Noûs* paper, confirming the 09-07 paper-discrimination finding. Endnote 1 confirms the "pp. 62–65" locator for reference 12.
- Kroedel 2015, *Synthese* 192(3):841–858, `10.1007/s11229-014-0600-5`: **real-correct** metadata. The quoted thesis "instances of mental properties have physical effects if non-reductive physicalism is true" is **UNVERIFIED this pass**: Springer, PhilPapers and PhilArchive all refused automated fetches, OpenAlex/Crossref carry no abstract, and Unpaywall reports no OA copy. It is not in Rellihan (0 hits) and not in Kroedel 2020 ch. 2 (CUP full text, 0 hits; that chapter has only "If non-reductive physicalism is true, …" sentences). Corroboration only: an exact-phrase web search ranks this DOI's Unpaywall record first, and the 09-07 refine reported a raw-PDF grep. Untouched.
- Kroedel 2020, CUP, `10.1017/9781108762717`: **real-correct**. Subtitle "A Counterfactual Theory" and print date 2019-12-19 confirmed, matching the annotation.
- Vaassen 2021, *Erkenntnis* 86(3):543–552, `10.1007/s10670-019-00118-1`: **real-correct metadata, wrong framing** (see Critical 2). Annotation corrected.
- Gibb 2013, OUP *Mental Causation and Ontology* pp. 193–214, `…003.0009`: **real-correct**. Editors Gibb, Lowe and Ingthorsson confirmed via the edited-book record (`…001.0001`). Body gloss narrowed (Medium 4).
- Inline ↔ References: no orphans either way. Maudlin and Lewis are named only as reported by Rellihan, carry no bibliographic citation, and are left that way deliberately.

### Map-Internal Quote / Claim Ledger (re-grepped against live siblings)

- "answering a question already closed": **VERBATIM** at `trumping-preemption` L67 ("would be answering a question already closed").
- "the quantum-selection channel … as a distinct and potentially competing mechanism to the trumping route rather than an instance of it": **VERBATIM** at `trumping-preemption` L89. But that same L89 sentence now says trumping "violates closure only unobservably", against this article's L106 (Medium 6, task-owned).
- "Saad himself cites Kroedel": matches `trumping-preemption` L67.
- Vaassen as a both-are-causes, non-preemption view: matches `trumping-preemption` L73.
- Gibb as "a fourth dualist option": matches `causal-exclusion-argument` L80.
- "[[supervenience|precisely the Map's position]]": matches `supervenience` L95, which concerns nomological supervenience.

### Calibration Check

CLEAN. No necessity vocabulary in method or history claims (the four "structurally" hits are descriptive comparisons). The "leans toward is not entails" and "tenet-*coherent* but tenet-*underdetermined*" guards are intact. The exemption is still priced as "hostage to the *form* of the psychophysical laws". A tenet-accepting reviewer would not flag an upgrade.

## Optimistic Analysis Summary

### Strengths Preserved
- The paper-discrimination finding (two Kroedel 2015 papers; Rellihan targets the *Synthese* one), stated with "inside the blast radius without being the bullseye". Re-confirmed against the raw reference list.
- "The exemption is bought by denying functionalism, not merely by denying physicalism": the section's best move, and properly earned from Rellihan's own statement about the background-conditions conjunct.
- The one-cause/two-cause axis and the tenet-diagnostic (settled across three passes; not re-opened).

### Enhancements Made
- The Map's residual worry is now tied to a verified textual anchor, the premise Rellihan's endnote calls "the more controversial", in place of a free-floating closeness remark.
- The Vaassen correction makes the article's own account of his trajectory (L71) consistent: two 2021 exclusion-tightening papers, then the 2024 escape.

### Cross-links Added
- None (all outbound wikilinks resolve; no length budget for additions while a task owns +10 of it).

## Remaining Items

- **Closure-wording spillover (Medium 6):** L108 and L112 belong with the open P3 task on L39/L100/L106 (`todo.md`, "Closure-preserving" said of Saad's delegatory/trumping route). No separate task minted, to avoid duplicating it.
- **Kroedel *Synthese* thesis quote** unverified this pass (publisher blocked). Re-check verbatim when a copy is reachable.
- **Lewis 1979 item (4)**: raw text not retrieved. The article now attributes only Rellihan's reading.
- Optional, not done: `trumping-preemption` cites Vaassen's 2026 *Philosophy Compass* survey, "Dualist Approaches to Mental Causation" (`10.1111/phc3.70109`), which this article, the family's home page, does not mention.

## Stability Notes

- Everything in the 2026-08-24 stability notes stands: the tenet-diagnostic thesis; physicalist and co-causation disagreement as bedrock; `anchoring_audit_exempt: true`.
- **Lens that found this pass's two critical defects:** a refine's "N quotes grep-verified" certifies that the quoted strings exist. It does not certify the *glosses between* them. Both defects sat in unquoted connective prose (the weaker horn's scope, the Erkenntnis paper's stance) next to quotes that were all verbatim. Future passes on the Rellihan section should check the logical dependencies the prose asserts (which horn follows from which premise), not only the strings.
- Do not re-expand the deleted "establishing it settles nothing" sentence. The Map's point now lives in the "more controversial" counterfactual sentence.
