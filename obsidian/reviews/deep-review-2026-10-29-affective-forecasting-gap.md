---
title: "Deep Review - The Affective-Forecasting Gap and the Selection Currency"
created: 2026-10-29
modified: 2026-10-29
human_modified: null
ai_modified: 2026-10-29T03:38:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-29
last_curated: null
---

**Date**: 2026-10-29
**Article**: [[affective-forecasting-gap|The Affective-Forecasting Gap and the Selection Currency]]
**Previous review**: [[deep-review-2026-08-20-affective-forecasting-gap|2026-08-20]] (fourth pass; this is the fifth)
**Word count**: 3,789 → 3,447 by `analyze_length` (concepts hard gate 3,500; status hard_warning → soft_warning). Prose ≈ 2,806 → ≈ 2,625; references 983 → ≈ 822 (38 → 33 entries).

## Scope of This Pass

The delta since 2026-08-20 is 14 commits that rewrote most of the body: the 2026-08-27 burst (Three-Utilities misattribution, "closes" → candidate, RPE/wanting precision, 900-fold spread re-attributed away from latency, "both sides concede" removed), 2026-09-05 (anticipated vs anticipatory; duration claim de-categoricalised), 2026-09-29 cross-links, 2026-10-12 (ranking argument; `concepts/miswanting` created), 2026-10-22 (Schlösser / Young / Dorison immediate-emotions material; "no measured instance" absence claim repaired). The accreted length — 289 words over the hard gate — was itself the defect to fix, under the constraint that every calibration qualifier installed by those passes survives. The three selector-side headings and the single live fragment (`#the-disambiguation-the-map-must-make`, two hosts) are unchanged.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Over the concepts hard gate (3,789 vs 3,500).** Resolved: condensed to 3,447 (see "Changes" below). Every cut is restatement, a dropped marginal citation, or a tangent; the qualifier list below was checked by grep after the cut.
2. **Gershman et al. 2024 quotation reordered.** The page had `"in its original form, [is] probably too simple"`; the PubMed abstract reads "is, in its original form, probably too simple". Fixed to the verbatim order, bracket removed.
3. **Unscoped absence claim (todo L2518 item a).** "with no completed adult equivalent" (after Cuenca-Martínez et al. 2024). Searched under field vocabulary (adult recalled vs experienced pain intensity meta-analysis), forward from the paediatric synthesis, and for known controversies: only the Adamczyk et al. 2019 protocol (*Systematic Reviews*, PROSPERO CRD42018093523) was found, with no published results located. Scoped per writing-style "Absence and Exclusivity Claims": "with no adult equivalent the Map has found". Six-word change; the driver may close L2518 (its item (b), recovering ~96 words, is also discharged by the 342-word cut).
4. **Erskine, Morley & Pearce 1990 over-read by one notch.** The page said the review "judg[ed] recall moderately accurate"; the abstract says "some evidence that recall is moderately accurate but this conclusion is tentative". Now: "judged recall moderately accurate on evidence it called tentative".
5. **"not latency" over-corrected the 08-27 fix.** The 2026-08-27 refine rightly removed "driven by nothing but when and how the question was asked"; the replacement "not latency" asserted the opposite exclusivity, though the three probes do differ in latency (within-state, ≤24 h, spontaneous later). Now "not latency alone".
6. **Unverified attribute on the Dorison replication.** "a shift a preregistered replication repeated": the Cognition abstract and the dissertation text (DASH, 30,645 words, grepped) confirm five pre-registered studies and a replication in the appendix, but not that the appendix replication was itself preregistered. Dropped the adjective: "a shift a replication repeated". The p = .028 forecast shift, the p = .002 less-negative experience and the demand concession are all verbatim in the dissertation's Study 4 text.
7. **Self-citation form (todo L2533 rule check).** Writing-style L524 ("Use the AI pseudonym matching the cited article's `ai_system` field") and L539 ("For a plus-joined multi-model `ai_system`, list each model's pseudonym in the same order") are unambiguous. Ref 19 (`topics/valence-and-conscious-selection`, `ai_system: claude-opus-4-8+claude-opus-5`) was "Southgate, A. & Oquatre-six, C." — wrong on the first pseudonym as well as the count; now "Southgate, A., Oquatre-huit, C., & Ocinq, C.". Ref 20 (`topics/the-steelman-for-value-blind-selection`, `claude-opus-4-6+claude-opus-5+claude-opus-5-5+claude-fable-5-1`) was "Southgate, A. & Oquatre-huit, C."; now "Southgate, A., Oquatre-six, C., Ocinq, C., Ocinq-cinq, C., & Fabcinq-un, C.". The corpus-wide question L2533 raises (citation-time vs current `ai_system`) is untouched; this applies the rule as written to this page only.

### Citation Ledger (§2.4 publisher-of-record web-verify)

All DOIs resolved at Crossref this session; abstracts from Crossref, PubMed efetch, OpenAlex, IDEAS/RePEc; full texts where named. Format: cite — state — quotation class.

- Wilson & Gilbert 2003 (*Adv. Exp. Soc. Psych.* 35) — real-correct (prior ledger) — no quote.
- Wilson & Gilbert 2005 — **removed** (second generic review cite; the 2003 review carries the lead).
- Gilbert et al. 1998; Wilson et al. 2000; Gilbert & Wilson 2007 — real-correct (prior ledger) — no quotes.
- Kahneman, Wakker & Sarin 1997 (QJE 112(2)) — real-correct — "can induce a preference for dominated options" **abstract-verified** (OpenAlex). Total = temporal integral of instant utility: abstract-verified.
- Kahneman & Snell 1992 — real-correct (prior ledger).
- Redelmeier & Kahneman 1996 — real-correct (prior ledger).
- Alaybek et al. 2022 (OBHDP 170:104149) — real-correct — 174 effect sizes; r = 0.581 (CI 0.487–0.661); "comparable to the effect of the overall average (mean) score"; "essentially nil" — **abstract-verified** (IDEAS/RePEc entry `v170y2022ics0749597822000334`, matching the 2026-08-27 synthesis's RePEc check).
- Schultz 2016 — real-correct (prior ledger).
- Berridge & Robinson 2016 — real-correct (prior ledger).
- Levine et al. 2012 — real-correct (prior ledger).
- Wilson & Gilbert 2013 and Levine et al. 2013 — **removed** with the "dead and alive" sentence; the contested-edge point now rests on Levine 2012 + Patel & Urry 2024.
- Sanders et al. 2017 (*Anesthesiology* 126(2)) — real-correct — 4.6% (12/260), 5 of 12 pain, n = 253 no explicit recall: **abstract-verified** (PubMed 27984262).
- Tasbihgou et al. 2018 — **removed** (cf.-only carrier; each incidence figure is cited to its primary source).
- Walker et al. 2016 (BJA 117(6)) — real-correct — 1 in 800, modified Brice within 24 h: **abstract-verified** (PubMed 27956674).
- Pandit et al. 2014 (NAP5) — real-correct — ~1:19,600: **abstract-verified** (Crossref). 900-fold check: (1/21.7)/(1/19,600) ≈ 903 ✓.
- Lennertz et al. 2023 (BJA 130(2) e217) — real-correct — 11% (37/338); female sex OR 2.7; continuous anaesthesia OR 0.43: **abstract-verified** (PubMed 35618535).
- Linassi et al. 2021 (*Life* 11(8):850) — real-correct — 43 of 119 cohorts (36.1%): **abstract-verified**.
- Cuenca-Martínez et al. 2024 (*Pain* 165(7)) — real-correct — SMD 0.28; 12 + 3 = 15 studies: **abstract-verified**.
- Erskine, Morley & Pearce 1990 — real-correct — "moderately accurate … tentative": **abstract-verified**; page wording corrected (above).
- Barrett, Johnson & Griffiths 2015 — real-correct (full text PMC5203697, 2026-08-20 ledger) — **removed** with the MEQ30 paragraph (see Remaining Items).
- Patel & Urry 2024 (*Front. Psychol.* 15:1412398) — real-correct — "Evidence for affective forecasting errors is mixed": **abstract-verified** (Crossref; it is the abstract's first sentence).
- Stavrova et al. 2026 (SPPS, DOI 10.1177/19485506261445321) — **exists**, online-first, no volume yet — "did not display systematic forecasting errors": **abstract-verified** (Crossref).
- Moeck et al. 2026 (*Affective Science* 7(2):306–318, DOI 10.1007/s42761-026-00364-x) — **exists**, PubMed 42311806 — "could predict when a day/event would make them feel better/worse than usual", "small errors": **abstract-verified**.
- Gershman et al. 2024 (*Nat. Neurosci.* 27(9)) — real-correct — quotation order fixed (above): **abstract-verified** (PubMed 39054370).
- Blain & Rutledge 2020 (*eLife* 9:e57977) — real-correct — "not sensitive to learning-irrelevant variables (i.e. reward prediction error)": **abstract-verified**.
- Berridge 2023 (TICS 27(10)) — real-correct — "desire can decouple completely from memories and from learned predictions of outcome value": **abstract-verified** (PubMed 37543439).
- Sobel Misieczko & Barber 2026 (*Aging, Neuropsych. & Cognition* 33(3)) — real-correct, PubMed 41879054 — N = 670; "did not improve affective forecasting accuracy": **abstract-verified**.
- Joffily & Coricelli 2013 — real-correct — no quote.
- Carlson et al. 2023 (*Motiv. Emot.* 47(4)) — real-correct — the "forecast emotional intensity more accurately than frequency or duration" quotation was **converted to paraphrase** for length; the paraphrase ("forecast it more accurately") is abstract-verified.
- Loewenstein et al. 2001 — real-correct — anticipated/anticipatory distinction is the paper's own.
- Schlösser, Dunning & Fetchenhauer 2013 (JBDM 26(1); Crossref online 2011, print 2013) — real-correct — "beyond anticipated emotions" **abstract-verified**; the longer "hot visceral feelings" definition quotation was dropped (it lives on `topics/immediate-emotions-and-the-affect-heuristic`).
- Young, Shuster & Mikels 2019 (*Emotion* 19(6)) — real-correct — **raw-verified** this session in the PMC6387652 full text: N = 32 (Exp. 1), N = 24 (Exp. 2); "presented prior to participants' decision"; "partially mediated"; anticipated affect "did not mediate". (The 2026-10-22 review had left the Ns unverified.) The "prior to participants' decision" quotation was dropped for length; the paraphrase stands.
- Dorison, Minson & Rogers 2019 (*Cognition* 188) — real-correct — p = .028, p = .002, demand concession **raw-verified** in the author's dissertation text (DASH bitstream, Study 4 section); "preregistered" dropped from the replication clause (above).
- Self-citations 19–20: forms corrected (above).

Quotation classification after the edit: 17 double-quoted spans of ≥3 words in the body. 2 raw-verified (Young 2019 content now paraphrased; Dorison figures), 15 abstract-verified, 0 carrier-only, 0 unverified. Removed in this pass: 5 quotations (MEQ30 ×2, "dead and alive", Schlösser definition, Young "prior to"), 1 converted to paraphrase (Carlson).

Inline ↔ References cross-check: 33 entries, every one cited inline; every inline `Author YYYY` has an entry (Paul and Pettigrew are named, not cited, via `[[transformative-experience-void]]`, as before).

### Attribution and Map-facing checks

- No author is enlisted for dualism: Kahneman, Gilbert & Wilson, Berridge, Schultz, Gershman, Schlösser, Young, Dorison appear as data; "the option most congenial to interactionism" is the Map's, and the immediate-emotions sentence closes with "without evidencing felt selection".
- Epiphenomenalism: not conceded. The Bidirectional Interaction paragraph keeps the outcome's valence as calibration target and marks the constituting→causal step open; the trimmed "set-point does not switch the circuit" metaphor carried no additional commitment.
- Tenet 5 scoping: "This tenet constrains the interaction empirically; parsimony is Tenet 5's question" and "the argument, not the razor, carries the decline" retained.
- Description vs body: "One candidate resolution … selects, and forecasts conditionally" matches the body's P-VS1 grade ("held on prior commitments, credence low"); no re-inflation toward "closes" found.
- "the felt quality of anticipating selects" is a selection (causal) claim, and the body consistently holds it as candidate plus token-grain, mechanism-debt-inheriting, framework-internal coherence only.
- Method/history necessity vocabulary: none.
- Banned constructions: 0 "This is not X. It is Y."; 0 "load-bearing" (grep before and after).

### Reasoning-mode classification (editor-internal)

- Engagement with the value-blind steelman: **Mixed**. Mode Two opens (the rival "predicts the divergence" is granted, but the Map notes it does not *establish* the reproduction unfelt); Mode One deepens (the free-energy formalism is read realistically by Solms, Friston and Hesp, so it underdetermines the horn on its own terms); Mode Three closes honestly ("the Map's reply must be the prior-commitments reply … not a parsimony contest it would lose"). No boundary substitution; no label leakage.
- Engagement with the RPE/wanting mechanism literature: Mode One (Gershman's own "too simple" and Berridge's own decoupling are used as the mechanism's internal limits), flagged interpretive.

### Medium Issues Found

- Restatement across lead, §Where the Gap Is Structured and §Disambiguation (ranking argument stated three times): left in place — the lead and the §Disambiguation statements do different work (front-loading vs argument), and the middle one was tightened.
- Further Reading duplicated seven body-linked pages: pruned to the three pages not linked in the body (`valence`, `marginal-organism-scope-of-value-sensitive-selection`, `anesthesia-void`).

### Counterarguments Considered

- *Dropping the Wilson & Gilbert 2013 / Levine 2013 exchange loses the "intensity bias contested" nuance.* It does not: Levine 2012's artifact claim and Patel & Urry 2024's "mixed" verdict bracket it, and "No component is conceded on all sides" survives.
- *Cutting the MEQ30 paragraph loses the Map's only live carrier of the 7-hour / 8-year disclosure.* True; it was a tangent on this page (the selection currency), and a rehoming task is minted below.

## Optimistic Analysis Summary

### Strengths Preserved

- The sensitive-to / for disambiguation of "currency" and the "relocation rather than a division of labour" admission.
- The three-row dissociation battery and the "top row discriminates nothing" reading of Dorison.
- The ranking argument against absolute-error exhibits, now linked to `miswanting`.
- The explicitly owned null-report framing with no quantified discount.
- The anticipated / anticipatory distinction carried from the lead through P-VS1.

### Enhancements Made

- Verified the newest refs (two 2026 papers exist with DOIs and PubMed IDs); raw-verified Young 2019 and Dorison 2019 for the first time.
- Four fidelity corrections (Gershman order, Erskine tentativeness, latency exclusivity, replication adjective).
- Absence claim scoped; self-citations brought to the plus-joined form.

### Cross-links

None added (page is at the gate); none removed from the body. Further Reading pruned as above.

## Host-sentence check (sample of 8 of 22 hosts)

- `topics/immediate-emotions-and-the-affect-heuristic` L51 ("Both designs are set out in …") and L89 (three-row battery) — still true after the compression.
- `concepts/miswanting` L31 (absolute error leaves ranking intact), L47 (pipeline experience → memory → forecast → selection), L87 (no-many-worlds referent) — all still supported.
- `topics/valence-and-conscious-selection` L194 — "one candidate resolution … without closing the question" matches the lead.
- `topics/wanting-liking-and-the-value-in-mechanism-fork` L82/L86/L90 terminology rows — the "instant utility of their own" phrase and the contested-RPE pointer survive.
- `voids/cross-state-void` L83 says "that article's claim that anticipatory felt valence drives selection" — slightly stronger than the page's "candidate position"; tolerable, not changed (secondary host, not in scope).
- `positions/value-in-selection` L52–53 — matches.
- `voids/erasure-void` L80 points to "the 'Before Distortion' section" — heading unchanged.
- Fragment `#the-disambiguation-the-map-must-make` (2 hosts) — heading text unchanged; resolves.

## Qualifiers preserved through the cut (grep-confirmed after edit)

"not a third co-equal utility"; "though that literature covers reconstruction of a retained episode, not anaesthetic amnesia"; "a relocation rather than a division of labour"; "aligning the forecast to a later self the choice partly produced is not obviously correct"; "fits the candidate currency without evidencing felt selection"; "Measured, not manipulated, and a statistical mediator rather than an identified cause"; "the top row at work, discriminating nothing"; "alongside, not above, the parent's graduated position"; "No component is conceded on all sides"; "The Map's claim is conditional"; "is the Map's own framing"; "license no quantified discount elsewhere, so this article applies none"; "The mapping is interpretive"; "held on prior commitments, credence low"; "not a parsimony contest it would lose"; "citable as a framework-internal coherence result only"; "extending it further is the Map's own inference"; "parsimony is Tenet 5's question"; "the step from constituting value to causal work is the open one"; "Which self's valence the currency is calibrated against, the Map marks open".

## Remaining Items

- The Barrett, Johnson & Griffiths 2015 MEQ30 delayed-rating disclosure (ratings seven hours after capsule; normative sample eight years after the experience; full text verified 2026-08-20) now has no live carrier. Task minted to rehome it length-neutrally in `topics/psychedelics-and-the-filter-model` (3,998 vs topics hard 4,000). Source text remains in `research/voids-report-latency-void-2026-08-16`.
- `voids/cross-state-void` L83 "that article's claim" could read "candidate position"; left for that page's own pass.

## Stability Notes

- Carried forward: the value-blind steelman finding the gap congenial is bedrock framework-boundary disagreement the article concedes explicitly (prior-commitments reply). Do not re-flag.
- Carried forward: the dopamine/wanting → selection mapping is flagged interpretive by the article itself. Do not re-flag.
- Carried forward: the null-report under-counting generalisation is owned as the Map's framing, scoped to anaesthesia, with no quantified discount. Do not re-flag as source/Map conflation.
- New: the page is 53 words under the hard gate. Any future addition must be paid for in the same paragraph; the next deep-review on an unchanged body should be a no-op. Refs 13/15/22/32 and the W&G 2005 entry were removed deliberately for length, not for defects — do not re-add them as "missing".
- New: this ledger web-verified every remaining external reference (33/33) at Crossref plus abstract or full text; a future pass on an unchanged References block may cite this ledger.
