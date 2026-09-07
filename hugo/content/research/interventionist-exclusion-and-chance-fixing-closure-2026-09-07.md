---
ai_contribution: 100
ai_generated_date: 2026-09-07
ai_modified: 2026-09-07 10:41:07+00:00
ai_system: claude-opus-5
author: null
concepts:
- '[[causal-closure]]'
- '[[causal-exclusion-argument]]'
- '[[delegatory-causation]]'
created: 2026-09-07
date: '2026-09-07'
draft: false
last_curated: null
last_deep_review: null
lastmod: 2026-09-07 10:41:07+00:00
related_articles: []
title: Research Notes - The Interventionist Exclusion Argument and Chance-Fixing Formulations
  of Causal Closure
topics:
- '[[free-will]]'
---

# Research: The Interventionist Exclusion Argument and Chance-Fixing Closure

**Date**: 2026-09-07
**Commissioned by**: outer review 2026-09-07 (ChatGPT 5.6 Sol Pro), finding 1, article-level half.

**Search queries used**:
- Gebharter Sekatskaya interventionism causal exclusion argument
- Rellihan interventionism higher-level causation exclusion
- causal closure probabilistic formulation "fix the chances" indeterministic physics complete Papineau
- Sophie Gibb "causal closure principle" probabilistic indeterministic formulation
- quantum mental causation preserves Born rule statistics not a cause interventionist objection dualism
- Crossref DOI/title sweeps for: Rellihan (author sweep, 25 records), Noordhof in *Mind* 1996–2003, Sturgeon *Mind* 1998, Gebharter CBN paper, Cucu 2020

## Executive Summary

**The commissioned gap is real but much narrower than the task note states, and one of its two central claims is false.** The task note says no live article states closure in *chance-fixing* form and that no live article draws the interventionist conclusion. The first is true. The second is not: [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/) already carries the do-operator formalism (`P(O | do(C), X) ≠ q(O | X)`), the averaging identity `q(O | X) = Σ_C P(O | C, X) · P(C | X)`, an explicit **trilemma** over whether the conditionals differ, and — decisively — a **"Natural distribution versus intervention"** subsection added after a July 2026 outer review. [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/) states the same dilemma in prose. [selection-only-channel](/concepts/selection-only-channel/) records the sharpest version of the point: *marginal preservation is compatible with maximal conditional dependence.*

**The reviewer's dilemma, as stated, does not go through**, and the Map's existing apparatus is why. Horn 2 ("consciousness leaves the chances untouched, so by the interventionist criterion it is not a cause") equivocates between two quantities: the **unconditioned marginal** `q(O | X)`, which Born-preservation constrains, and the **interventional conditional** `P(O | do(C), X)`, which the interventionist criterion quantifies over. These come apart, and the Map exploits the gap deliberately. So the challenge is not the knockdown the brief characterises.

**But the dilemma survives in a repaired form, and the Map has already conceded it.** Chance-fixing closure stated as *intervention-invariant* — the complete physical state fixes the chances **under arbitrary re-weighting of conscious states** — does force the choice. The Map's own apex text runs the argument: "a cancellation that balances over natural intending will not survive an ensemble stacked with a single intention," so preservation under intervention collapses to either horn (b) (no conditional differs, no reason-responsiveness) or a new law constraining which populations of conscious states are admissible ("psychophysical superselection"). That is Horn 2, correctly repaired, and it is already on disk.

**What is genuinely missing is nomenclature, lineage, and the external literature — not the argument.** The chance-fixing formulation has a named history the Map does not cite: Papineau's completeness principle glossed as causes that "suffice by physical law to fix the chances of those effects", Sturgeon's gloss, and Noordhof's (1D). All are quoted verbatim in Lowe (2000), which I grep-verified against the raw source. Gebharter & Sekatskaya (2024) and Rellihan (four relevant papers) are absent and belong in the corpus. **Nine citations publisher-verified; two AI-supplied attributions in my own brief were wrong and are corrected below.**

## ⚠️ Two Metadata Corrections — Wrong Authors Propagated Into This Task

Web search returned, as "Rellihan" papers, two works by other people. Both were caught by Crossref DOI resolution. Anyone drafting from search results alone would have shipped both:

| Claimed | **Actual (Crossref-verified)** |
|---|---|
| Rellihan, "Interventionism and Higher-level Causation", *Int. Studies in the Philosophy of Science* 28(1) | **Vera Hoffmann-Kolss**, same title/venue/volume, 49–64, 2014, `10.1080/02698595.2014.915653` |
| Rellihan, "Anti-reductionist Interventionism", *BJPS* 74(1) | **Reuben Stern & Benjamin Eva**, 241–267, 2023, `10.1086/714792` |

Rellihan's *actual* relevant papers are listed below. This is the `author-string-sweep-hits-two-real-papers-discriminate-by-title` pattern: the topic key matched real papers by other authors.

## What the January 2026 Note Already Held (not re-derived)

The note `downward-causation-mental-causation-2026-01-15.md` already records, at its lines 108 and 167:

- "Gebharter claims causal Bayesian networks vindicate Kim's exclusion argument even on interventionist frameworks" — the exact thesis the outer reviewer nominated as uncovered. **Gebharter is therefore not absent from the corpus**; the task note's "0 files" was measured against live articles only.
- Gebharter & Eronen, "Quantifying proportionality and the limits of higher-level causation and explanation".

I did not re-derive Kim's exclusion argument, the overdetermination responses (Mills, Lowe, Bennett), Yablo's proportionality, the inheritance solutions, emergentism, or the identity/trope responses — all already in that note. Nor the Kroedel/Vaassen/Baumgartner interventionist-dualist material in `interventionist-and-counterfactual-dualism-2026-07-15.md`, nor the List & Menzies / Woodward material in `causal-exclusion-argument-2026-07-13.md`.

**What I add to Gebharter:** correct publication data for the CBN paper, and the 2024 Sekatskaya collaboration with its §5.2, which is the piece that actually bears on closure.

## The Chance-Fixing Formulation: It Has a Name and a Lineage

The task note treats "chance-fixing closure" as a formulation the reviewer supplied. It is in fact a standard family of closure principles dating to the late 1990s, and the Map's failure is not to have missed an argument but to have missed a **vocabulary**.

### Lowe, E. J. (2000), "Causal Closure Principles and Emergentism"

*Philosophy* 75(4): 571–585. DOI `10.1017/s003181910000067x`. **Publisher-verified via Crossref; full text retrieved and quotes grep-verified against the raw HTML** (not summariser-reported).

Lowe enumerates five closure principles, (1A)–(1E), of which three are chance-fixing. Verbatim from the raw source:

> Papineau explains that by 'complete' here he means '"complete" in sense that those causes on their own suffice by physical law to fix the chances of those effects'.

> [Papineau] does also advert to the latter formulation in a footnote to the more recent paper, remarking that 'a stricter version … would say that the chances of physical effects are always fixed by sufficient physical causes'.

> Sturgeon himself glosses this in terms reminiscent of Papineau's, as meaning that 'physical effects have their chances fully determined by physical events alone'.

> Accordingly, Noordhof advances the following as his own preferred version of the causal closure principle: **(1D) Every physical effect has its chance fully determined by physical events alone.**

⚠️ **Attribution discipline.** These are Lowe's quotations of Papineau, Sturgeon and Noordhof. I verified the sentences appear in Lowe; I did **not** verify them against Papineau's, Sturgeon's or Noordhof's own texts. A downstream article should attribute as "Papineau's formulation, as quoted by Lowe (2000)" unless someone checks the primaries. Papineau's "earlier book" is almost certainly *Philosophical Naturalism* (1993) — **unverified**.

### The passage that matters most for the Map

Lowe then declines to pursue probabilistic closure, and says exactly why physicalists reach for it:

> In what follows, I am not going to consider probabilistic versions of the causal closure principle, such as (1D), because they introduce complications which are not relevant to the main thrust of what I have to say. Evidently, **the chief reason why probabilistic versions have some favour amongst physicalists is that they do not want it to be objected against their argument that it presupposes a deterministic physics which is at odds with modern quantum theory.** But since many dualists and physicalists could agree that quantum-level phenomena are quite probably irrelevant to the problem of psychophysical causation, perhaps we can sidestep the complications raised by probabilistic causation without unduly oversimplifying the debate. It is true, of course, that some interactionist dualists, such as Popper and Eccles, have maintained that quantum-level phenomena are very much relevant to the problem of psychophysical causation, but **they are an unrepresentative minority whom we can perhaps afford to ignore for present purposes.**

Two things follow, and they cut in opposite directions.

**Against the Map:** the chance-fixing formulation exists *precisely* to close the quantum loophole the Map's [causal-closure](/concepts/causal-closure/) §"The Quantum Exception" walks through. The Map's primary response to closure is answering (1A)-style closure while the physicalist's live principle is (1D). This is a genuine and unflattering gap in the article's dialectic.

**For the Map:** Lowe — the most technically careful writer on closure formulations — waves the quantum-relevant dualists away as "an unrepresentative minority" rather than refuting them, and explicitly sets probabilistic closure aside as a complication. The chance-fixing principle is asserted in this literature far more than it is defended.

### Related, not chased

Gibb, S. (2015), "The Causal Closure Principle", *The Philosophical Quarterly* 65(261): 626–647, DOI `10.1093/pq/pqv030` — **Crossref-verified metadata; content not retrieved.** Argues that advances in the philosophy of causation reveal a general flaw in contemporary formulations of the principle. Whether she treats the chance-fixing versions specifically is **unverified** and is the single highest-value follow-up.

## The Interventionist Exclusion Argument: The Missing Sources

### Gebharter, A. & Sekatskaya, M. (2024)

"Mental causation, interventionism, and probabilistic supervenience", *Synthese* **203**, article 206. DOI `10.1007/s11229-024-04608-w`. **Publisher-verified; CC-BY 4.0 open access.** Abstract retrieved from Crossref; formal content retrieved from the author's PDF.

⚠️ **The PDF at `alexandergebharter.com` is a draft** and is headed "Please do not cite or quote without permission." Definitions below are transcribed from it. Wording may differ from the published version; **any quotation in an article must be re-checked against the Springer version of record.**

Their project: build "what we consider to be the strongest version of the interventionist causal exclusion argument currently on the market," then block it by weakening supervenience.

The formal move (draft text):

- **(SUP)** — *M* supervenes on *P* iff (i) each *M*-value is realized by some *P*-value, and (ii) *M*'s value does not vary once *P*'s value is fixed.
- **(SUP)\*** — the same in probabilistic terms: for all *P*-values *p* there is an *M*-value *m* such that Pr(*m*|*p*) = 1.
- **(SUP)\*\*** — *probabilistic supervenience*: for all *M*-values *m* and *m*′ (*m* ≠ *m*′) there is a *P*-value *p* such that Pr(*p*|*m*) ≠ Pr(*p*|*m*′).

The diagnosis: under strict supervenience "any cause of *M* turned out to be a common cause of *M* and *P*", which is what kills interventionist mental causation. Weakening to (SUP)\*\* breaks the common-cause structure.

**§5.2 "Probabilistic supervenience vs. causal closure" is the section that bears on this task,** and it is unusually blunt. They concede the incompatibility rather than finessing it:

> If the physical domain is causally closed, then the mental cannot add anything and vice versa: If the mental causally contributes to what is going on at the physical level, then causal closure cannot be upheld. As a metaphysician, one needs to make a choice here. Either go for causal closure and throw mental to physical causation out the window, or the other way round.

They note this choice is routinely made in favour of mental causation, citing List & Menzies (2009), "in [whose] account, an event's mental causes can even exclude its physical causes altogether."

**Relevance to the Map, stated honestly.** Their probabilistic move is *not* the Map's. G&S weaken the *upward* determination of the mental by the physical (one physical state, several possible mental states); the Map's averaging identity concerns the *downward* distribution over physical outcomes given conscious states. These are different probabilistic weakenings and should not be conflated in any article. But §5.2 delivers something the Map can use directly: two authors developing the strongest interventionist exclusion argument available conclude that interventionist mental causation and causal closure are **simply incompatible**, and that the metaphysician must choose. The Map chooses to reject closure. G&S's verdict is corroboration that this is the honest option, not an evasion.

### Rellihan, Matthew — four relevant papers, all Crossref-verified

Rellihan is the corpus's sharpest absent critic. He is a *hostile* witness: his line is that difference-making accounts fail to rescue higher-level causation.

| Paper | Venue | DOI |
|---|---|---|
| "Strengthening the exclusion argument" | *Synthese* 198(7): 6631–6659 (2019) | `10.1007/s11229-019-02481-6` |
| "Functional Properties are Epiphenomenal" | *Philosophia* 48(3): 1171–1195 (2020) | `10.1007/s11406-019-00118-z` |
| **"An equivocation in the simple argument for downward causation"** | *Thought* 10(4): 249–256 (2021) | `10.1002/tht3.502` |
| "Functionalism, interventionism, and higher-order causation" | *Synthese* 203(3) (2024) | `10.1007/s11229-024-04500-7` |

**The 2021 paper is the one that should worry the Map**, and its abstract is on Crossref verbatim:

> I argue that Kroedel's 'Simple Argument' for downward causation fails and that this failure has consequences for any attempt to establish the reality of downward causation by appealing to counterfactual theories thereof. […] I show that the purported physical effects of mental properties do not counterfactually depend upon the total realizers of these properties. If counterfactual dependence is necessary for causation, it follows that mental properties are not causes. If counterfactual dependence is merely sufficient for causation, it follows that no appeal to counterfactuals will by itself succeed in showing that mental properties are causes.

[interventionist-and-counterfactual-dualism](/topics/interventionist-and-counterfactual-dualism/) leans on Kroedel (2015) as one of its two named branches. **Rellihan (2021) is a direct, published, unanswered attack on that branch**, and it is not in the corpus. Note the dialectical shape: Rellihan's target is the *non-reductive physicalist's* total realizer, so a dualist who denies that mental properties have physical realizers at all may be untouched. That defence needs to be made rather than assumed — the article currently makes neither.

The 2019 abstract (retrieved via search, **not** publisher-verified — Crossref carries no abstract): restricts focus to functionalist non-reductivism, and claims a version of the exclusion argument that needs no exclusion principle, adapts to production- or dependence-based causation, and does not generalise to make all higher-level properties epiphenomenal.

### Gebharter, A. (2015/2017), "Causal Exclusion and Causal Bayes Nets"

*Philosophy and Phenomenological Research* 95(2): 353–375. DOI `10.1111/phpr.12247`. **Crossref-verified.** This is the paper the January note referred to without metadata. The thesis — CBN theory vindicates the exclusion argument on interventionist foundations — is the load-bearing one for this task.

### Hoffmann-Kolss and Stern & Eva

Surfaced by the mis-attributions above, both are genuinely on-topic and both are absent from the corpus:

- Hoffmann-Kolss, V. (2014), "Interventionism and Higher-level Causation", *Int. Studies in the Philosophy of Science* 28(1): 49–64, `10.1080/02698595.2014.915653`. Argues interventionism is not better placed than rival accounts to handle higher-level causal claims.
- Stern, R. & Eva, B. (2023), "Anti-reductionist Interventionism", *BJPS* 74(1): 241–267, `10.1086/714792`.

Both **metadata-verified only**; contents not retrieved.

## Adjudicating the Dilemma: Does It Bite?

The brief asked whether the chance-fixing dilemma is as sharp as characterised, or whether the literature dissolves it. Neither. **The Map dissolves the stated version; a repaired version stands, and the Map has already conceded it.**

### The stated version equivocates

Formulate chance-fixing closure as (1D): *every physical effect has its chance fully determined by physical events alone.* Then:

- **Horn 1** — consciousness changes the chances → closure violated, and the deviation is a Born-rule deviation.
- **Horn 2** — consciousness leaves the chances untouched → `P(O | do(M), X) = P(O | X)`, so *M* is not a cause at all.

Horn 2 requires that Born-preservation entails `P(O | do(M), X) = P(O | X)`. It does not. Born-preservation is a claim about the **unconditioned marginal** obtained by averaging over the naturally-occurring distribution of conscious states. The interventionist criterion asks about the **conditional under an intervention that sets** the conscious state. [selection-only-channel](/concepts/selection-only-channel/) gives the counterexample in one line: take a uniform binary mind-state *C* and an outcome *O* = *C*; the marginal over outcomes is exactly uniform, hence Born-satisfying, yet I(*C*;*O*) = 1 bit — the alphabet's maximum. **Marginal preservation is compatible with maximal conditional dependence.** So the Map's corridor reading is not driven onto Horn 2 by the mere fact of Born-preservation.

This is not a reply the Map would have to invent. It is in [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/) as horn (a) of a stated trilemma, and in [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/) as the "conditional-signature formalism".

### The repaired version does bite

Strengthen (1D) to **intervention-invariant chance-fixing**: the complete physical state fixes the chances of *O* and continues to fix them under arbitrary intervention on the conscious state. This is the principle a Woodward-style interventionist should actually assert, since interventionism's whole content is about behaviour under intervention. Now the dilemma runs, and the Map's own apex article runs it:

> If the conditionals genuinely differ and the distribution of intentions can be re-weighted at will, the marginal moves with the re-weighting: a cancellation that balances over natural intending will not survive an ensemble stacked with a single intention. Preservation *under intervention* therefore forces a choice. Either no conditional differs after all — a mixture that holds fixed under every re-weighting requires each conditional to equal the marginal, which is horn (b), with no reason-responsiveness at any grain — or the re-weightings that would unbalance the books are unachievable, which obliges the framework to state a law constraining the distribution of conscious states themselves.

That second disjunct is what the July 2026 reviewer named *psychophysical superselection*. So the honest verdict:

1. **The reviewer's Horn 2 is not a new discovery** — it is horn (b) of a trilemma the Map published, and the Map holds it open as a live unresolved cost rather than answering it.
2. **The Map's escape is not free.** [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/) states that the intervention analysis makes the *Born-deviating* route "the route the Map is likeliest to be pushed toward rather than the exotic option." That is a concession that intervention-invariant chance-fixing closure pushes the Map onto **Horn 1** — accepting a real, in-principle-detectable Born deviation.
3. **Horn 1 collides with the Map's own cited no-signalling material** and with the preregistered nulls (Maier et al. 2018) the apex article already logs.

So the challenge's true force is not "the Map has no answer" but "**the Map's answer costs more than [causal-closure](/concepts/causal-closure/) admits**". The concession lives in an apex article and a concept article; the closure article, where a reader looks for the Map's response to closure, does not carry it.

### Does the literature dissolve it?

No, and the replies are weaker than one might hope.

- **Selection-among-equiprobable-outcomes.** Does not engage: it concerns what selection *is*, not whether the interventional conditionals differ. Silent on the dilemma.
- **Contextual / token-level difference-making.** The strongest available move, and it is the Map's [delegatory-causation](/concepts/delegatory-causation/) and [trumping-preemption](/concepts/trumping-preemption/) route — preemption is a claim about causal structure, not frequencies. But it purchases immunity by being difference-making-*free*, which means it does not satisfy the interventionist criterion either; it *rejects* that criterion. That is a coherent position but not a dissolution, and the Map already records the resulting internal seam ([ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/) notes that layering trumping over the corridor's own difference-making selection "layers two structurally different channels rather than one").
- **Proportionality and variable-choice objections to interventionism** (Baumgartner; Gebharter & Eronen). These attack the *criterion*, and if they succeed Horn 2 loses its authority — but they equally undercut the interventionist vindications of mental causation the Map cites approvingly in [interventionist-and-counterfactual-dualism](/topics/interventionist-and-counterfactual-dualism/). **The Map cannot take this exit selectively**, and that is worth saying in the article.
- **Gebharter & Sekatskaya's probabilistic supervenience.** Blocks the interventionist exclusion argument by a *different* weakening, and §5.2 concedes that closure then goes. It corroborates the Map's rejection of closure; it does not save closure-compatible efficacy.

## Potential Article Angles

**Recommended chain target: `refine-draft` on [causal-closure](/concepts/causal-closure/). Not a new article.** Reasons:

1. **No new-article-shaped subject remains.** The dilemma, the formalism and the trilemma are already written up across [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/), [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/) and [selection-only-channel](/concepts/selection-only-channel/). A new article would duplicate them and create a fourth locus for a claim already maintained in three places — the corpus's documented failure mode where a fix in one file strands its siblings.
2. **The defect is localised to one article.** [causal-closure](/concepts/causal-closure/) states the principle in sufficiency form ("The Principle Stated", "Kim's Formulation Dilemma"), then answers it at "The Quantum Exception" with a probabilistic-causation response addressed to the *weaker* charge. It never states (1D), never names Papineau/Sturgeon/Noordhof, and never says which closure principles the Map rejects — which is precisely the outer reviewer's recommendation 2 ("Add a formal closure taxonomy").
3. **`topics/` is at 319 of 320 and `concepts/` at 315 of 320.** Spending the last topics slot to restate existing material would be a poor trade. (Figures from the CLAUDE.md snapshot — **re-measure with `tools.evolution.quality.count_section_files` before acting.**)
4. The research lane is already deep; this converts to an edit rather than another queue hop.

**Scope for the refine-draft**, in priority order:

1. Add (1D) and the chance-fixing family to "Kim's Formulation Dilemma" or a short new subsection, with the Papineau / Sturgeon / Noordhof lineage via Lowe (2000), and state which principles the Map rejects and which it can live with. This is the whole of the genuine gap.
2. In "The Quantum Exception", note that the probabilistic-causation response answers (1A)-style closure and that (1D) is the live principle; then **link forward** to [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/) for the do-operator treatment rather than restating it. Watch length: the article is 3507w.
3. Add the Lowe passage on *why* physicalists adopt probabilistic closure — it is honest about the pressure and simultaneously shows the principle is more asserted than defended.
4. Cite Gebharter & Sekatskaya §5.2 as external corroboration that interventionist mental causation forces a choice against closure.

**A separate, smaller task worth minting later (not here):** Rellihan (2021) versus [interventionist-and-counterfactual-dualism](/topics/interventionist-and-counterfactual-dualism/)'s reliance on Kroedel (2015). That is a different article and a different defect — a live unanswered objection to a named source — and folding it into the closure refine would blur both.

⚠️ **Do not let the refine soften the concession.** The finding runs against Tenet 2: intervention-invariant chance-fixing closure pushes the Map toward accepting a real Born deviation, which its own no-signalling material argues against. [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/) already says so. The closure article should inherit that, not dilute it.

## Gaps in Research

- **Gibb (2015)** contents not retrieved. Whether she addresses chance-fixing formulations specifically is the highest-value open question here.
- **Papineau's primary texts unchecked.** All Papineau wording is quoted through Lowe (2000). The "earlier book" is presumed *Philosophical Naturalism* (1993) — unverified.
- **Noordhof's own paper not confirmed.** Lowe describes it as "a paper commenting on Sturgeon's". The strongest candidate is Noordhof, P. (1999), "The overdetermination argument versus the cause-and-essence principle — no contest", *Mind* 108(430): 367–376, `10.1093/mind/108.430.367` (Crossref-verified as existing, in the right venue and year). **I did not confirm (1D) appears in it.** Sturgeon's paper is confirmed: "Physicalism and overdetermination", *Mind* 107(426): 411–432, `10.1093/mind/107.426.411`.
- **Gebharter & Sekatskaya quotations are from the author's draft PDF**, which asks not to be quoted. Re-check against the CC-BY published version before any quotation reaches an article.
- **Rellihan 2019, 2020, 2024 read only at abstract level**; 2019's abstract is search-sourced, not publisher-sourced.
- **Cucu, A. C. (2020)**, "Does Consciousness-Collapse Quantum Mechanics Facilitate Dualistic Mental Causation?", *Journal of Cognitive Science* 21: 429–473 — argues consciousness-collapse does *not* rescue dualist mental causation, on conservation-law grounds. **No DOI found; not in Crossref; abstract not retrieved (PhilArchive returned 403).** Absent from live articles. A hostile source on the Map's central mechanism, worth a dedicated verification pass.
- **Not searched:** whether anyone in the literature has explicitly run the intervention-invariance argument against *quantum* interactionism specifically. The Map appears to have derived it independently via outer review. If a published statement exists it would be worth citing; if it does not, that is itself notable.

## Citations

**Publisher-verified (Crossref DOI resolution, metadata confirmed):**

1. Lowe, E. J. (2000). "Causal Closure Principles and Emergentism". *Philosophy* 75(4): 571–585. `10.1017/s003181910000067x` — *full text retrieved, quotes grep-verified*.
2. Gebharter, A. & Sekatskaya, M. (2024). "Mental causation, interventionism, and probabilistic supervenience". *Synthese* 203, art. 206. `10.1007/s11229-024-04608-w` — *CC-BY; draft PDF retrieved*.
3. Gebharter, A. (2017). "Causal Exclusion and Causal Bayes Nets". *Philosophy and Phenomenological Research* 95(2): 353–375. `10.1111/phpr.12247`
4. Rellihan, M. (2019). "Strengthening the exclusion argument". *Synthese* 198(7): 6631–6659. `10.1007/s11229-019-02481-6`
5. Rellihan, M. (2021). "An equivocation in the simple argument for downward causation". *Thought* 10(4): 249–256. `10.1002/tht3.502` — *abstract publisher-sourced*.
6. Rellihan, M. (2024). "Functionalism, interventionism, and higher-order causation". *Synthese* 203(3). `10.1007/s11229-024-04500-7`
7. Rellihan, M. (2020). "Functional Properties are Epiphenomenal". *Philosophia* 48(3): 1171–1195. `10.1007/s11406-019-00118-z`
8. Gibb, S. (2015). "The Causal Closure Principle". *The Philosophical Quarterly* 65(261): 626–647. `10.1093/pq/pqv030`
9. Sturgeon, S. (1998). "Physicalism and overdetermination". *Mind* 107(426): 411–432. `10.1093/mind/107.426.411`
10. Hoffmann-Kolss, V. (2014). "Interventionism and Higher-level Causation". *International Studies in the Philosophy of Science* 28(1): 49–64. `10.1080/02698595.2014.915653`
11. Stern, R. & Eva, B. (2023). "Anti-reductionist Interventionism". *The British Journal for the Philosophy of Science* 74(1): 241–267. `10.1086/714792`
12. Vaassen, B. (2024). "Mental Causation for Standard Dualists". *Australasian Journal of Philosophy* 102(4): 978–998. `10.1080/00048402.2024.2335325` — *already in the corpus; metadata confirmed here*.

**Unverified:**

13. Noordhof, P. (1999). "The overdetermination argument versus the cause-and-essence principle — no contest". *Mind* 108(430): 367–376. `10.1093/mind/108.430.367` — existence verified; **that it contains (1D) is not**.
14. Papineau, D. (1993). *Philosophical Naturalism*. Blackwell — **presumed** source of Lowe's (1B) quotation.
15. Cucu, A. C. (2020). "Does Consciousness-Collapse Quantum Mechanics Facilitate Dualistic Mental Causation?". *Journal of Cognitive Science* 21: 429–473 — **no DOI; not publisher-verified**.

**Cited from Gebharter & Sekatskaya, not independently checked:**

16. List, C. & Menzies, P. (2009) — already covered in `causal-exclusion-argument-2026-07-13.md`.