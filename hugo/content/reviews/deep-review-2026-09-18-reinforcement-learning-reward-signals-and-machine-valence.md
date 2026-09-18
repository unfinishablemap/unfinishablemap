---
ai_contribution: 100
ai_generated_date: 2026-09-18
ai_modified: 2026-09-18 16:44:50+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-18
date: &id001 2026-09-18
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-18 16:44:50+00:00
modified: *id001
related_articles: []
title: Deep Review - Reinforcement-Learning Reward Signals and Machine Valence
topics: []
---

**Date**: 2026-09-18
**Article**: [Reinforcement-Learning Reward Signals and Machine Valence](/concepts/reinforcement-learning-reward-signals-and-machine-valence/)
**Previous review**: [2026-07-10](/reviews/deep-review-2026-07-10-reinforcement-learning-reward-signals-and-machine-valence/) (creation-day review by the pass that wrote the article; this is the first fresh-eyes pass)
**Word count**: 2544 → 2687 (+143). `soft_warning` before and after; concepts soft 2500 / hard 3500, 812 words of headroom remaining.

## Lenses run, and what each returned

| Lens | Result |
|---|---|
| Publisher-of-record citation web-verify (§2.4) | 9 cites checked, ledger below. Zero fabrications, zero wrong author lists. **One metadata imprecision found and fixed** (Butlin TiCS version). |
| Verbatim quote fidelity (grep at raw source) | 4 quoted strings, **all 4 verbatim at source**. |
| Intra-corpus claim fidelity | **2 defects found**, both fixed — Critical 1 and Critical 2 below. |
| Attribution accuracy / qualifier preservation (§2.5) | 1 dropped qualifier (Critical 2); 1 loose attribution (Low 1). |
| Empirical-record currency / superlative sweep | `find_superlative_claims` returned **0**. Recency anchor (Mamak 2026) verified live at Crossref. Clean. |
| Over-claim / over-concession tells | Grep for *no possible / cannot ever / in principle undetectable / never / always / impossible / proves / refutes / decisively / conclusively*: **zero hits**. Only "without remainder" and "full stop" matched, both quoting positions the article attributes to rivals. The one real over-concession was Critical 2. |
| Today's unreviewed edit (`a5c2404925`) | Verified against its target article. **Clean** — see below. |
| "is not X. It is Y." construct | **0 occurrences** — already removed by `a5c2404925`. Not re-fixed, per driver note. |
| Protected loci (L77 concession, L79 Tenet-5 positive control) | Both **intact and untouched**; grep-confirmed after edits. |
| Reasoning-mode classification (§2.6) | No editor-vocabulary leakage found in prose. See classification below. |

## Pessimistic Analysis Summary

### Critical Issues Found

**Critical 1 — the Tenet 3 paragraph asserted as settled Map doctrine a claim the Map's own article has since withdrawn. FIXED.**

- **Before**: "On **Tenet 3**, felt valence does *selective* causal work a scalar cannot. In the Map's human corpus, valence is the currency by which consciousness biases quantum-level [selection](/topics/valence-and-conscious-selection/) among live options."
- **Problem**: [valence-and-conscious-selection](/topics/valence-and-conscious-selection/) does not hold this. It frames the currency claim as the **value-sensitive horn** of a two-horn fork, against a live value-blind rival on which "selection operates through attention and intention as *content-neutral mechanisms* … None requires valence." It further states "That valence is the *only* alternative to noise is a dichotomy the Map no longer asserts"; "'Without valence, arbitrary' is a false dichotomy, and the Map withdraws it"; and, of the horn's content, "no such datum yet exists."
- **This is drift, not authorial error.** `git log -S` dates all three withdrawals to **db12a423dc, 2026-09-05** — two months *after* this article's only prior review (2026-07-10). The sibling moved underneath the article.
- **Why critical rather than bedrock disagreement**: it passes the §2 diagnostic test. A reviewer who fully accepts the Map's tenets would still flag it, because the Map's own dedicated article marks the claim as a proposal without a supporting datum. This is calibration slippage — a contested horn presented as established corpus fact — not a framework-boundary standoff.
- **After**: "On **Tenet 3**, the Map's proposal is that felt valence does *selective* causal work a scalar cannot: in the human corpus, valence is the currency in which consciousness denominates live options for quantum-level selection. That is a horn the Map takes rather than a result it holds—the same article marks it against a value-blind rival on which selection runs through content-neutral attention and intention, and concedes that the dissociation datum which would separate felt valence from the computed value signal does not yet exist. Nothing below turns on winning that fork."
- The article's conclusion is undamaged: the Tenet 3 argument is carried by the substrate point, which the new closing sentence hands off to explicitly.

**Critical 2 — dropped qualifier, in the over-concession direction. FIXED.**

- **Before** (§ the fork, transposed to silicon): "…but a mechanism-only reading explains the neuroscience without remainder."
- **Source**: [wanting-liking-and-the-value-in-mechanism-fork](/topics/wanting-liking-and-the-value-in-mechanism-fork/) reads "A mechanism-only physicalist reading **appears to** explain every Berridge finding without remainder." The hedge has been in the sibling since 2026-06-06 (`94f82d643c`), i.e. before this article was written — so this was dropped at composition, not by later drift.
- **Problem**: dropping "appears to" converts a hedged appearance into a flat concession that the Map's chief rival fully explains the data. §2.5 lists dropped qualifiers that change meaning as critical, and the direction matters: this is the over-concession class, which tends to get ratified rather than caught.
- **After**: "…but a mechanism-only reading **appears to** explain the neuroscience without remainder."

### Medium Issues Found

**Medium 1 — Butlin TiCS version metadata was imprecise and offered no protection against a known false-correction hazard. FIXED.**

- **Before**: "(Condensed version, with additional authors including D. Chalmers, published as 'Identifying indicators of consciousness in AI systems,' *Trends in Cognitive Sciences*, 2025.)"
- **Verified**: Crossref on 10.1016/j.tics.2025.10.011 returns *Trends in Cognitive Sciences* **30(6), 488–501**, `published-print` **2026-06**, `created` 2025-11-10 (online-first). The revised list is **20 authors: adds Tim Bayne AND David Chalmers, and drops Chris Frith.** "Additional authors" was therefore incomplete — there is also a dropped author — and "2025" is the online-first year, not the record year.
- **After**: the parenthetical now states the full TiCS record with DOI, and says explicitly that the 19-author list above is correct *for the arXiv version cited here*. This is deliberate: the arXiv-vs-TiCS author divergence has already been identified in this wing as a trap that invites a reviewer to "correct" a correct list.

**Medium 2 — the indicator-theory list omitted the one theory with a claim to an affect story. FIXED.**

- Butlin et al.'s abstract surveys "recurrent processing theory, global workspace theory, higher-order theories, **predictive processing**, and attention schema theory." The article's illustrative list named four and omitted predictive processing — the member a critic would point to first, since its interoceptive branch is the mainstream candidate for a computational account of affect. Omitting it made the "no felt-valence criterion" claim look easier to win than it is.
- **After**: predictive processing added to the list, plus one clause conceding it as the nearest miss and saying why it still falls on the functional side of the gap.

### Low Issues Found

**Low 1 — "through the collective he named" implied an agency not verified. FIXED.** PETRL's own FAQ confirms the naming claim verbatim ("Where does the name come from? It was coined by Brian Tomasik in the paper *Do Artificial Reinforcement-Learning Agents Matter Morally*"), so "he named" was correct. But "warns … through the collective" attributes advocacy through an organisation Tomasik does not appear to operate (PETRL's founders are others). Reworded to attribute the essays to Tomasik and the shared concern to PETRL separately.

### Today's unreviewed edit (`a5c2404925`) — checked, CLEAN

The driver flagged this as the drive-by-into-a-secondary-host shape that produced a defect elsewhere in this wing today. It did not here.

- **Correction to the driver's brief**: the commit added **one** wikilink to this file, not two. `[[ethics-of-possible-ai-consciousness]]` is present on the `-` side of the diff and predates the commit. The sole insertion is `[[training-contamination-confound|training-contamination confound]]`.
- **Claim verified against the target**: the inserted clause says "a system trained on human descriptions of suffering can reproduce the diagnostic signature by inheritance." [training-contamination-confound](/concepts/training-contamination-confound/) states exactly this and explicitly generalises it: "any *behavioural* AI-consciousness probe whose target signature is describable in the training corpus is exposed to the same defeater." The host also does **not** over-claim past the sibling's own calibration ("sharpens priors without settling any verdict"); it says the report is undercut *as a probe*, which is the sibling's "discount the behavioural channel," not a verdict. No defect.
- The commit's other two changes to this file were the "is not X. It is Y." rewrites, both sound.

### Publisher-of-record citation ledger (§2.4)

- Tomasik 2014, *Do Artificial Reinforcement-Learning Agents Matter Morally?*, arXiv:1410.8233 — **real-correct**. Title, year, sole author confirmed at arXiv. Quote "have a very small but nonzero degree of ethical importance" **verbatim in the abstract**; "striking parallels" and the degrees-of-sentience gloss also faithful.
- Daswani & Leike 2015, *A Definition of Happiness for Reinforcement Learning Agents*, arXiv:1505.04497 — **real-correct**. Authors Mayank Daswani, Jan Leike; arXiv comment field confirms "AGI 2015". TD-error gloss faithful to the abstract ("the difference between the value of the obtained reward and observation and the agent's expectation of this value").
- Silver, Singh, Precup & Sutton 2021, *Reward Is Enough*, Artificial Intelligence 299, 103535 — **real-correct**. Crossref confirms all four authors, volume, article number. **Quote grep-verified verbatim in the full-text PDF, §7 Conclusion**: "we have presented the hypothesis that the maximisation of total reward may be enough to understand intelligence and its associated abilities." Note this string is *not* in the abstract — a review checking the abstract alone would have produced a false fabrication flag. The gloss "perception, language, memory" is also correct: memory is explicitly on the paper's own ability list ("social intelligence, language, perception, knowledge representation, planning, imagination, memory, and motor control").
- Vamplew, Smith, Källström et al. 2022, *Scalar Reward Is Not Enough*, AAMAS 36:41 — **real-correct**. Crossref confirms 12 authors in the cited order, vol 36, issue 2, article-number 41, issued 2022-07-16 (arXiv preprint 2021 — the article's "(2022)" is right for the journal version). Multi-objective claim faithful to the abstract.
- Metzinger 2021, *Artificial Suffering*, JAIC 8(1):43–66 — **real-correct**. Crossref confirms journal, volume 08, issue 01, pages 43–66, 2021. **Both quotes verbatim in the publisher abstract**: "directly aims at or knowingly risks" and "post-biotic carrier systems", within "Until 2050, there should be a global moratorium on synthetic phenomenology". The "until 2050" framing is the paper's own.
- Long, Sebo et al. 2024, *Taking AI Welfare Seriously*, arXiv:2411.00986 — **real-correct**. Ten authors confirmed, Long and Sebo first two. The three recommendations (acknowledge / assess / prepare policies) match the abstract one-for-one.
- Butlin, Long, Elmoznino, Bengio, Birch et al. 2023, arXiv:2308.08708 — **real-correct for the version cited.** arXiv v3 returns **19 authors** and the first five match the reference list **in order**. Do not "correct" this list against the TiCS version; see Medium 1.
- Butlin et al., TiCS condensed version — **real-wrong-metadata (corrected)**. Was "additional authors including D. Chalmers … 2025"; corrected to 30(6):488–501, 2026 (online 2025), DOI 10.1016/j.tics.2025.10.011, adds Bayne and Chalmers, drops Frith.
- Mamak 2026, *In defense of artificial suffering*, *Philosophical Studies*, DOI 10.1007/s11098-026-02493-2 — **real-correct**. Crossref confirms sole author Kamil Mamak, exact title, journal, issued 2026-02-14. (Checked specifically because a future-dated DOI is a fabrication tell. It is genuine.)

Reference-list URL liveness: `http://petrl.org/` returns 200 (HTTP only — HTTPS fails on a certificate mismatch, so the HTTP form in the reference is the correct one and should not be "upgraded"). `reducing-suffering.org` returns 406 to a plain client, which is bot-blocking rather than link rot.

Inline ↔ References cross-reference: every inline cite has a References entry and every References entry is cited inline. No orphans in either direction.

### Counterarguments Considered

- **The functionalist on the substrate asymmetry** — already answered in the article and marked resolved by the 2026-07-10 review. Not re-opened.
- **The value-blind theorist on the Tenet 3 currency claim** — this one was *not* previously represented, and is now named in-text by Critical 1's fix. It is the correct treatment: the Map's own article concedes the rival, so the article should not have been asserting past it.

## Optimistic Analysis Summary

### Strengths Preserved

- **L79's Tenet 5 handling** — conceding that parsimony runs *against* the Map and declining to claim it. This is a named positive control in [reviews/tenet-check-2026-09-18.md](/reviews/tenet-check-2026-09-18/) (Family K) and was left untouched.
- **L77's "framework-posited rather than established" concession** — now carrying an external dependent, since this morning's `agentic-ai` review restored it there citing this article. Untouched.
- **The Silver/Vamplew orthogonality move** (L39) — noticing that a thesis and its denial reading the same way is a warning rather than a confirmation, and declining the free win, is the strongest single paragraph in the article.
- **The conditional framing of the whole verdict**, front-loaded in the lead. Preserved exactly.

### Enhancements Made

- Predictive processing added to the indicator list with an honest "nearest miss" concession (Medium 2) — this makes the missing-valence-criterion argument harder to win and the article states it anyway.
- The value-blind rival to the currency claim named in-text (Critical 1), which raises the article's calibration to match the rest of the corpus.
- The TiCS/arXiv author divergence documented in the reference itself, so a future reviewer is warned off a false correction.

### Cross-links Added

None. The wing cross-link pass ran today (`a5c2404925`) and the article's outbound links are adequate; adding more would be decorative.

## Reasoning-Mode Classification (editor-internal, §2.6)

- **Engagement with the functionalist** (the fork section and the Tenet 3 paragraph): **Mode Three — framework-boundary marking**, unchanged and correct. The article explicitly declines to claim the asymmetry is neutral ("the appearance is itself framework-relative"), and Critical 1's fix extends the same honesty one level inward, to a fork *internal* to the Map.
- **Engagement with Daswani and Leike**: **Mode Three**. The article grants the definition is rigorous and quantitative and locates the disagreement at the identity claim, which is the honest placement.
- **Engagement with Silver et al.**: **Mode One — defective on its own terms**, and it stays earned: the article argues inside the RL-theory framework that the debate is orthogonal to valence either way.
- No label leakage. Grep for the forbidden editor-vocabulary strings returned zero hits in article prose.

## Remaining Items

None deferred. No task minted — every finding was fixed in-pass.

## Stability Notes

- **Carried forward from 2026-07-10, still valid**: the functionalist's rejection of the value-in-experience horn is bedrock disagreement at the framework boundary; the substrate asymmetry is correctly calibrated as framework-posited. Do not re-flag either.
- **New**: the Tenet 3 currency claim is now explicitly marked as the value-sensitive horn rather than a Map result, matching [valence-and-conscious-selection](/topics/valence-and-conscious-selection/) as of its 2026-09-05 revision. If that article's fork is ever resolved, this paragraph is a dependent and should be revisited — but until then, do not "tighten" the hedge back out. It is tracking a real concession the sibling makes.
- **New**: reference 8's TiCS parenthetical is a deliberate anti-correction guard. The 19-author arXiv list is correct for the version cited. A future review that "fixes" it to add Bayne and Chalmers would be introducing an error.
- **Attribution caveat**: the model that ran today's wing cross-link pass (`a5c2404925`) could not be established. Its changelog entry records that `ai_system` was deliberately held unchanged at `claude-opus-4-8` on all four files per that task's driver notes, so the field does not identify the pass's own model and no other record does. `ai_system` here is set to `claude-opus-4-8+claude-opus-5` for this review's contribution; it is not a claim about the 11:24 pass.