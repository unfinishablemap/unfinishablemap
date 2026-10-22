---
title: "Deep Review - Kim's Causal Exclusion Argument"
created: 2026-10-22
modified: 2026-10-22
human_modified: null
ai_modified: 2026-10-22T16:47:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-22
last_curated: null
---

**Date**: 2026-10-22
**Article**: [[causal-exclusion-argument|Kim's Causal Exclusion Argument]]
**Previous review**: [[deep-review-2026-08-17-causal-exclusion-argument|2026-08-17]] (and 2026-07-20, 2026-07-13; plus [[pessimistic-2026-10-20-causal-exclusion-argument|pessimistic 2026-10-20]])

**Why this article.** `deep_review.py next` ranked it first (score 69, 66 days since the last deep review). The selection is genuine, not a cosmetic bump. Two refine-drafts changed the body after 08-17: on 09-15, route 4 (Gibb's double prevention, Davies 2016); on 10-20, Saad's polarity, the chance-fixing scope of route 3, the Tenet 4 bullet, the Tenet 5 conditional and the eliminativist sentence. Those passages and their three new references (Gibb 2013, Davies 2016, Saad 2025) had never been deep-reviewed.

**New axis this pass: claim-content fidelity of the response-family glosses.** The 07-13 and 08-17 ledgers verified the reference metadata and the body's quoted spans. Neither checked the unquoted paraphrases of what each critic or respondent argues against that author's own text. That axis found two defects that survived three "verified" reviews. Both were seeded by the 07-13 research note.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

**1. Bennett's counterfactual test was stated in the wrong direction (L63).** The article read: *"Under supervenience you cannot have the mental cause without its physical base, so that counterfactual is false or only vacuously true."*

Bennett's preferred move runs the other way. Her test has two counterfactuals:
- (O1): if m had happened without p, e would still have happened;
- (O2): if p had happened without m, e would still have happened.

The *physical base necessitates the mental property*, so p-without-m is impossible and (O2) is only vacuously true. Bennett explicitly *declines* to make (O1) vacuous, because "it is impossible for m to occur without p" would deny multiple realizability. The article stated the option Bennett rejects as if it were her view.

**Resolution**: "Under supervenience the base necessitates the mental property, so the counterfactual about the base occurring without it is only vacuously true." The first sentence also now says "either cause" and "not merely vacuously", so the reader can see why vacuity defeats the test.

- **Source**: Hallman, *Florida Philosophical Review* XVI(1), 2016, pp. 45–46. I grepped the raw PDF text: "Bennett's final solution ultimately sides with arguing for the vacuity of (O2)… For (O1) to be vacuous, one needs to argue that it is impossible for m to occur without p. This, however, undermines multiple realizability."
- **Corroboration**: a search summary of Morris 2015 (*Philosophia* 43(2): 435–453) and a summary of Aimar both describe Bennett as denying the *physical* independence condition, (P & ~M) □→ e. Those are aggregator summaries, not raw text.
- **Primary text not retrieved**: the Noûs paper is paywalled and the ANU repository copy is restricted. OpenAlex gives only the opening paragraph. The fix rests on a raw secondary text that reconstructs Bennett with section-level detail, plus the logic of upward necessitation, which fixes the direction independently.

**2. The Bermúdez & Cahen gloss attributed an argument the paper does not make (L69).** The article read: *"Critics (e.g. Bermúdez & Cahen 2015, replying directly to Menzies in the same issue) argue difference-making does not deliver the metaphysical exclusion Kim needs denied, and that proportionality can cut the other way."*

I downloaded the raw PDF from humanamente.eu (8,159 words):
- **"propor": 0 hits.** No proportionality objection appears anywhere in the paper.
- **"metaphysical exclusion": 0 hits.**
- **Actual thesis** (abstract, verbatim): "one consequence of Menzies's proposed solution to the problem of mental causation is a ubiquitous violation of the principle of closure — a fact that forces him into a trilemma to which we see no satisfactory response."
- **"Directly … in the same issue" was loose.** Menzies does have a paper in Humana.Mente 29 ("The Causal Closure Argument is No Threat to Non-Reductive Physicalism", pp. 21–46). But Bermúdez and Cahen's reference list cites Menzies 2013 (in Gibb, Lowe & Ingthorsson's OUP volume) and List & Menzies 2009, not the issue paper. Menzies's issue paper has 0 hits for "Berm" or "Cahen". The two papers are independent contributions to the same themed issue.

**Resolution**: "Critics press the cost: Bermúdez and Cahen (2015), replying to Menzies, argue that downward exclusion makes violations of physical closure ubiquitous, leaving him a trilemma for which they find no satisfactory response." This was the 08-17 review's open "sharpen the Bermúdez & Cahen gloss" item, which needed the paper itself. That item is now **closed**.

### Medium Issues Found

- **Route 4 contradicted route 3 on closure (L80, fixed).** "both keep closure's letter" sat against route 3's own "denies premise 2's *sufficiency*". The letter of premise 2 is the sufficiency formulation. It now reads "both aim to leave a closure principle standing, Gibb by moving the mental contribution to prevention, the Map by placing it where physics fixes only chances". That is chance-fixing closure, which route 3 grants since 10-20. "Aim to" records Davies's objection that Gibb's closure holds only by pre-ordained harmony. Word-neutral.
- **The Tenet 5 paragraph pointed the tenet at a rival's premise (L94, fixed).** "is illustrated by the no-overdetermination premise, which is a parsimony move" invited the reading that Tenet 5 counts against Kim's premise 5. The driver's calibration family and `tenets.md` L145 ("binds the Map's use of parsimony… symmetric") both rule that out. It now reads: "bears on the no-overdetermination premise, which is a parsimony move, but the Map does not use the tenet against it: route 3 leaves premise 5 standing." That is true: route 3 dissolves overdetermination by denying a sufficient physical cause, not by rejecting premise 5. The 10-20 conditional drainage sentences are untouched. This changes no doctrine and does not pre-empt NEEDS-HUMAN (doctrine) 2026-09-19.
- **Editorial verdict in the neutral anatomy (L55, fixed).** "and, for a non-partisan reader, the most telling" was cut (−9 words). The pessimistic review flagged it on 10-20 and the refine pass did not take it up.
- **"Which is what the physicalist picture denies" (L63, weakened).** The pessimistic review noted that Bennett is herself a physicalist. The critique exists (a 2024 *Philosophia* paper, Zhao, 52(4): 1165–1184, per a search summary): on a plausible physicalist picture the mental cause's sufficiency cannot be established. "Denies" overstated "cannot be established", so it now reads "does not secure". This weakening is safe in both directions, and no new attribution was added on aggregator evidence.
- **Lead construct (L33, fixed).** "The argument is not X and not Y — it is Z" echoed the banned construct. It now reads "Distinct from X and from Y, the argument is Z" (−1 word).
- **Saad named in route 1, his mechanism unnamed in route 3 (L79, fixed).** "Saad's delegatory-preemption reply" ties route 3's quantum-independent option back to route 1's softer variant (+1 word).
- **Self-citation pseudonyms (L136, fixed).** `mental-causation-and-downward-causation` has `ai_system: claude-opus-4-6+claude-opus-4-8+claude-opus-5-5`, so the citation now lists "Southgate, A., Oquatre-six, C., Oquatre-huit, C., & Ocinq-cinq, C.", per writing-style L539. The overdetermination-dissolution self-cite (`claude-opus-4-7` → Oquatre-sept) was already correct.

### Counterarguments Considered

- **Physicalist (chance-fixing restatement of exclusion).** Answered by the 10-20 edit and verified intact. Route 3 concedes chance-fixing closure under exact Born preservation, keeps the token-level claim, and marks settling-as-causing as the open P-Q3 question. Epiphenomenalism is neither conceded nor denied. This is consistent with `causal-closure` L138 and `positions/quantum-interface` P-Q3 L79, whose `^mechanism-debt` anchor resolves.
- **Quantum skeptic (amplification).** Not added. Route 3 is a pointer page, and the mechanism-debt link carries the amplification and toy-model debts (P-Q10). Adding them here would duplicate the register.
- **Buddhist (discrete-cause ontology).** Framework boundary. No sentence added; the page is over soft.

### Publisher-of-Record Citation Ledger

New since the last ledger (never previously deep-reviewed):
- Gibb 2013, "Mental Causation and Double Prevention," in Gibb, Lowe & Ingthorsson (eds.), *Mental Causation and Ontology*, OUP, 193–214, DOI …003.0009. State: **real-correct**. Crossref gives the chapter title, author and pages; the editors come from the book DOI …001.0001.
  - **Content**: verified against Gibb's own restatement of the same model in Gibb 2015, "Physical Determinability," *Humana.Mente* 29: 69–90 (raw PDF). "Enabling events are not causes, although they enable — or, in other words, permit — events to be caused"; "m1 prevents m2 from preventing n2 from causing b1"; "M1 is not a cause in the physical domain".
  - The route-4 gloss (a mental double preventer of a mental preventer; no causation on the powers theory; "permits") is faithful.
- Davies 2016, *Metaphysica* 17(1): 37–42, DOI 10.1515/mp-2016-0003. State: **real-correct**. The Crossref JATS abstract matches the article's gloss: "Closure is maintained only on the assumption of an implausible pre-ordained harmony between preventing and double-preventing mental events."
- Saad 2025, *Philosophical Studies* 182(3–4): 939–967, DOI 10.1007/s11098-025-02290-3. State: **real-correct**. Crossref abstract constraint (2): "ensure that experiences do not cause observable violations of the causal closure of the physical domain". "Keeps only observational closure" is faithful.

Body-claim fidelity (the new axis):
- Bennett 2003: metadata **real-correct** (Crossref: Noûs 37(3): 471–497). Gloss was **direction-inverted** and is now corrected (Critical 1).
- Bermúdez & Cahen 2015: metadata **real-correct** (raw PDF: *Humana.Mente* Vol. 29, 47–68). Gloss **misattributed** a proportionality objection and is now corrected to their actual closure-violation thesis (Critical 2).

Re-confirmed at Crossref this pass. All are real-correct and all match the References block:
- Kim 1989 (*Phil Perspectives* 3: 77–108)
- Kim 2003 (PPR 67(1): 151–176)
- Block 2003 (PPR 67(1): 133–150)
- List & Menzies 2009 (J Phil 106(9): 475–502)
- Woodward 2015 (PPR 91(2): 303–347; online 2014)
- Wilson 1999 (PQ 49(194): 33–52)
- Wilson 2011 (Monist 94(1): 121–154)
- Ehring 1996 (Noûs 30(4): 461ff)
- Funkhouser 2006 (Noûs 40(3): 548–569)

Carried from 08-17 and not re-litigated: Yablo 1992 (with the p. 259 quotation), Shoemaker 2001 and 2007, Kim 1998 and 2005.

**Orphan check, (surname, year), both directions.** There are no orphans. Kim 2003 is cited inline by title ("Blocking Causal Drainage"). Kroedel, Vaassen, Mills and Lowe appear without years as a pointer to [[interventionist-and-counterfactual-dualism]], which carries their references. Earlier reviews accepted this.

**Cited-author stance.**
- Gibb: dualist; the article presents her as a dualist.
- Davies: accepts the powers metaphysic and criticises Gibb.
- Saad: dualist (delegatory dualism).
- Bennett: non-reductive physicalist compatibilist.
- Bermúdez & Cahen: critics of Menzies who treat closure as "a core principle of physicalism". The article enlists none of them for the Map's conclusion.

**Superlative/currency sweep**: none in the body. The article is a philosophical anatomy.

## Optimistic Analysis Summary

### Strengths Preserved
- The premise-by-premise mapping of every response family.
- The framework-boundary concessions in the subset and Yablo paragraphs ("may work perfectly well for the non-reductive physicalist it was built for").
- Route 4's candour ("The Map has not priced double prevention and treats it as a live rival").
- The 10-20 chance-fixing scope in route 3 and the Relation section.
- The Tenet 4 bullet.
- The Vaassen branch split.
- The verified Yablo quotation.

### Enhancements Made
- Two content-fidelity corrections, for Bennett and for Bermúdez & Cahen. The Bermúdez & Cahen correction makes the interventionist paragraph sharper: the cost the critics press is closure itself.
- Internal consistency between routes 3 and 4 on closure.
- Tenet 5 scoped to the Map's own reasoning.

### Cross-links Added
None. All targets resolve, including `positions/quantum-interface#^mechanism-debt` and every tenet anchor.

## Reasoning-Mode Classification (editor-internal)
- Kim's reductionist horn: Mode Three (unchanged).
- Subset / Yablo: Mode Three (unchanged).
- Block vs Kim: Mode One, internal to physicalism (unchanged).
- Chance-fixing physicalist vs route 3: Mode Three. Settling-as-causing is marked as an open framework boundary and not claimed as a refutation.
- Eliminativist: Mode Three, a one-line boundary note.
- Gibb: a dualist rival presented and left unpriced, with no refutation claimed.

There is no boundary substitution and no label leakage. Zero hits for: load-bearing, bedrock, unsupported-jump, direct-refutation, mode-mixed, Evidential status, "This is not".

## Length

The concepts thresholds are soft 2500, hard 3500 and critical 5000. The hard gate is `>=`.

| | Before | After |
|---|---|---|
| Total (`analyze_length`) | 3051 | 3064 (+13), still `soft_warning`; headroom to hard 435 |
| Prose | 2562 | 2571 (+9) |
| Further Reading | 138 | 138 |
| References | 351 | 355 (+4; the three added self-citation pseudonyms) |

The page was edited in near-length-neutral mode. The prose additions were the Bennett direction fix and the Tenet 5 scope clause (about +21). They were offset by the L55 editorial cut (−9), the lead rephrase and the Bermúdez & Cahen rewrite.

## Propagation Check

- **Bennett direction**: 2 content loci, this article and its seed note `research/causal-exclusion-argument-2026-07-13` L74. **Both fixed.** No other corpus locus states Bennett's test, either through grep or through any of "mental cause without", "without its physical base" or "without the physical base", across `obsidian/` and `archive/` (reviews and workflow excluded).
- **Bermúdez & Cahen gloss**: 2 content loci, this article and the seed note L81. **Both fixed.** The note's L102 bare mention is accurate and was left alone.

## Remaining Items

- **Lead, not adjudicated: two Map pages name different originators of the observational-closure distinction.** `concepts/observational-closure` L32 says "Bradford Saad (2025) introduced this distinction". `topics/interventionist-and-counterfactual-dualism` L65 credits Lowe 2003 with distinguishing "*observational* closure… from closure full-stop". This is the "named idea cited to its populariser" tell. It is out of scope here; this article only attributes the softer variant to Saad, which is correct. Worth a targeted refine-draft on `observational-closure`, checked against Lowe 2003's text.
- **Bennett primary text still not retrieved.** A future pass with Noûs access could pin a page for the (O2)-vacuity move. The current wording quotes nothing, so no page cite is owed.
- **Block's primary text** is still unretrieved. This item is carried from 08-17; the epistemic/modal labels remain softened.

## Stability Notes

- **Bennett's test runs (O2)-vacuous**: the base necessitates the mental property, so base-without-mental is impossible. Do not "restore" the mental-without-base wording. Bennett rejects that move because it would deny multiple realizability.
- **Bermúdez & Cahen's thesis is closure violation, not proportionality.** Do not reintroduce a proportionality clause under their name. A proportionality critique of interventionism, if wanted, needs its own cite. The Yablo paragraph already notes that critics dispute whether proportionality constrains causation.
- **Route 3 concedes chance-fixing closure, and route 4 now matches it.** Do not reword either back to unscoped "nothing to exclude" or "closure's letter".
- **Tenet 5 here is scoped to the Map's own reasoning.** Do not re-expand it into a lesson against Kim's premise 5.
- Carried from earlier passes:
  - The Yablo 1992: 259 quotation is verbatim.
  - The de-quoted Kim spans stay de-quoted.
  - Vaassen stays out of the benign-overdetermination branch.
  - The five-premise and four-premise reconstructions are both standard.
  - Physicalist, eliminativist and MWI rejection of the Map's premises is bedrock disagreement.
- **This is the article's fourth deep review.** The body is converging. If the body is unchanged since this pass, the next review can be metadata-only.
