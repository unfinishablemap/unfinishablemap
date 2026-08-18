---
ai_contribution: 100
ai_generated_date: 2026-07-30
ai_modified: 2026-07-30 14:52:44+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-30
date: &id001 2026-07-30
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-30 14:52:44+00:00
modified: *id001
related_articles: []
title: Deep Review - Mental Effort
topics: []
---

**Date**: 2026-07-30
**Article**: [Mental Effort](/concepts/mental-effort/)
**Previous review**: [2026-07-07](/reviews/deep-review-2026-07-07-mental-effort/)
**Lenses run**: quote-fidelity (never previously run) and citation-framing / claim-match (never previously run). Metadata was ledgered 2026-07-07 and was **not** re-spent. Tenth deep review; the article is well-converged on structure and calibration, so this pass targeted only the two unchecked surfaces.

## Quote-Fidelity Pass

The `"[^"]\{30,\}"` regex returns **16 spans**. Triage: 10 are frontmatter wikilinks inside YAML quotes, 1 is the `description:` field, 1 is a regex artifact spanning the gap between two separate short quotes in the Occam's-Razor paragraph, and 1 is the Map's own position-label (`"felt effort just is what the operation feels like"`). **Three are externally attributed**, plus one borderline gloss. Real count: **3 verifiable + 1 gloss**.

- **James, "sustained voluntary attention is a repetition of successive efforts"** — **verbatim-correct**. Verified at primary text (Principles of Psychology, Ch. XI, p. 420, psychclassics.yorku.ca). Full sentence: "What is called sustained voluntary attention is a repetition of successive efforts which bring back the topic to the mind." The article quotes the leading fragment and drops the trailing clause; the retained span is exact and the truncation does not alter the sense.
- **James, "Volition is nothing but attention"** — **verbatim-correct, correct work**. Verified at primary text, Principles Ch. XI, p. 447, in the section "Is Voluntary Attention a Resultant or a Force?": "when we see (as in the chapter on the Will we shall see) that volition is nothing but attention". James asserts this as his own view rather than reporting an opponent's. Sentence-initial capitalisation in the article is normal quoting convention. No defect.
- **Tallis, "misrepresentation presupposes presentation"** — **DEFECT: paraphrase wrapped as verbatim quotation. De-quoted.** See below.
- **Inzlicht signal gloss, "this is no longer worth your while; switch"** — not a defect. Second-person address makes it plainly the *content* of the signal rather than a bibliographic quotation. Left as-is, recorded here so a future pass does not mistake it for an attributed quote and "verify" it.

### The Tallis defect

The article attributed `"misrepresentation presupposes presentation"` to Raymond Tallis as a verbatim quotation. **The phrase does not appear in the primary text.** Verified at Tallis, "The Illusion of Illusionism", *Philosophy Now* issue 161 (2024) — the source the corpus's own prior reviews name for it. What Tallis actually writes is: "The reflection of a cloud in a puddle becomes a representation only when it is observed by a phenomenally conscious subject. Similarly, all illusions presuppose experience."

Tallis genuinely makes the argument; the *wording* is not his. The probable origin is [research/illusionism-consciousness-2026-01-14.md](/research/illusionism-consciousness-2026-01-14/) L146, where the phrase appears **without quote marks** as the Map's own summary of the regress objection. Quote marks were added downstream and the formulation acquired an attribution it never had.

**Self-contamination note.** A search for the phrase returns results that are *entirely* unfinishablemap.org — prior deep reviews of illusionism, downward-causation, against-functionalism, purpose-and-ai-alignment and experiential-alignment all "confirming" it. This is exactly the circular-ratification pattern in `[[quote-verify-self-contamination-via-own-page]]`: the corpus had verified the quote against itself fifteen times. Only the primary text catches it.

**Fix applied here**: de-quoted, attribution to Tallis preserved — "Tallis's claim that illusions presuppose experience". This is true regardless of which Tallis text carries the argument, so it is robust to the possibility that some other Tallis work (e.g. *Aping Mankind*) phrases it differently. Per `[[verbatim-quote-cited-to-wrong-work]]` discipline the cite is re-framed, not deleted.

## Claim-Match / Citation-Framing Pass

Per-cite ledger (framing and claim-match only; metadata not re-spent):

- **Naccache et al. (2005)** — **framing correct, claim-match exact.** Verified against the published abstract (*Neuropsychologia* 43(9):1318-28). Every load-bearing detail checks out: left mesio-frontal lesion including ACC; normal executive control; residual right anterior cingulate activity on ERPs; "our patient experienced no conscious feeling of mental effort and showed no SCR"; and in normal subjects "subjective increases in effort associated with executive control correlate with higher skin-conductance responses". The article's line-94 use — the SCR coupling present in normals and absent in the patient as the residue that survives on the dualist side — is faithful. **This is the article's single most load-bearing empirical claim and it is clean.**
- **Hagger et al. (2016)** — **framing correct.** d=0.04, 95% CI [−0.07, 0.15], 23 labs, N=2,141, all match. Correctly enrolled as the *collapse* of the strength-resource model, not alongside depletion-supporting sources. No direction inversion.
- **Inzlicht & Schmeichel (2012) / Inzlicht et al. (2021) / Kurzban et al. (2013)** — **framing exemplary.** Line 88 explicitly places them on the materialist side: "These are functionalist absorption stories, not witnesses for the dualist reading... They belong on the materialist side of the ledger and must be engaged as such, not enlisted as convergent support." Kurzban's opportunity-cost model is correctly presented as a rival to resource depletion rather than a version of it. Line 100 re-uses them as "the serious non-epiphenomenalist reply". This is the discipline working exactly as intended; preserve.
- **Westbrook et al. (2020)** — **DEFECT: claim-match error + scope over-extension at line 146. Fixed.** The publisher record (*Science* 367(6484):1362-1366) shows the study used methylphenidate and sulpiride, examined **cognitive effort only**, and demonstrates that dopamine "boosts the perceived benefits versus costs of cognitive effort by modulating striatal dopamine signaling" — it alters cost-benefit decision-making, explicitly **not** the subjective sensation of effort. The article asserted Westbrook "show striatal dopamine modulation shifts *felt effort*", and then leaned on "(they don't, on the dopamine evidence)" to settle a **mental-versus-physical** currency question a cognitive-effort-only study cannot settle. Both corrected. The line-88 use of the same paper ("shifts willingness to engage demanding tasks") was already accurate and is unchanged.
- **Tegmark (2000)** — **DEFECT: quantitative misattribution. Fixed.** The article gave "~10⁻¹⁵ s" as Tegmark's neural decoherence figure. The published abstract gives "decoherence timescales ~10^{-13}-10^{-20} seconds" against "relevant dynamical timescales (~0.001-0.1 seconds)". 10⁻¹⁵ is not a figure Tegmark states. **Family-resolution check**: every other corpus locus — `timing-gap-problem.md`, `stapp-quantum-mind.md`, `interface-friction.md`, `access-consciousness.md`, `quantum-biology-and-neural-consciousness.md`, `motor-control-quantum-zeno.md` and others — gives **10⁻¹³**. This article was the sole outlier; corrected to 10⁻¹³ and the paired upper bound aligned to the corpus-canonical "hundreds of milliseconds (~10⁻¹ s)", which is what makes "twelve orders of magnitude" derive correctly.
- **Howard et al. (2016)** — **DEFECT: unsupported extension. Fixed.** The abstract (*Cognition* 157:114-125) supports the implicit half exactly: "Intentional binding was greater under low than high effort." It reports no explicit-agency result. The article's parenthetical claimed effort disrupts implicit agency "even as the explicit sense often rises", attributing a positive explicit-measure finding to a paper that does not report one. Trimmed to what the study found; the surrounding argument (felt-causal signals whose machinery is hidden) is carried entirely by the implicit finding and loses nothing.
- **Sauerbrei & Pruszynski (2025)** — **checked as a suspected direction inversion; NOT a defect. No change.** The concern was that a published rebuttal to Zheng & Meister sits in a joint parenthetical behind "measurements converge on ~10 bits/s". Investigation shows the framing is deliberate and correct: the sentence scopes the figure to *conscious* throughput (italicised in the source) and enrols S&P for the second half — "unconscious processing runs orders of magnitude faster" — which is precisely their claim, that motor control in unpredictable environments exceeds the limit. The W16 changelog records this italicised scoping as having been installed *because of* S&P, and the W28 pass on `bandwidth-of-consciousness.md` web-verified that S&P **concede** the ~10 bit/s conscious-cognition ceiling and dispute only whole-brain scope. Re-litigating would have regressed a settled, correctly-calibrated distinction. Recorded so future passes do not re-open it.
- **Kral et al. (2022)** — **framing correct.** Used at line 108 for exactly what it found: a well-powered (N=218) active-controlled study finding **no structural** change from MBSR, deployed to *weaken* earlier cortical-thickness claims. This is the correct direction. The sibling-article defect noted in the brief (asserting "altered brain structure" against this paper) **does not occur here**.
- **Lutz et al. (2008)** — **framing correct.** Correctly identified as the *Trends in Cognitive Sciences* attention-regulation review and used for what it reviews: the novice/expert shift in effortful redirection and the finer-grained awareness of effortful-effortless transitions.
- **Yuan et al. (2022) / Schwartz et al. (1996) / Zheng & Meister (2025)** — framing unchanged and consistent with the 2026-07-07 ledger; not re-spent.

**Currency check**: `find_superlative_claims` returns **zero**. No superlative or record claim to currency-verify. The replication-crisis reckoning the brief flagged as a risk is already carried — Hagger is front-and-centre in the "Depletion" section and the resource model is described as having "collapsed under preregistration".

## Pessimistic Analysis Summary

### Critical Issues Found
1. **Tallis quote fabricated-as-verbatim** (L126) — RESOLVED (de-quoted, attribution preserved).
2. **Westbrook claim-match error + scope over-extension** (L146) — RESOLVED.
3. **Tegmark quantitative misattribution, sole corpus outlier** (L118) — RESOLVED.
4. **Howard explicit-agency extension unsupported** (L92) — RESOLVED.

### Calibration / Slippage Check
Clean. No possibility/probability slippage. The constrain-vs-establish discipline (L50, L94) and the functionalist-absorption ledger (L88) are intact and are the article's strongest calibration features. The diagnostic test — would a tenet-accepting reviewer still flag any claim as overstated? — returns no on all surviving passages. Note that the Westbrook fix *improved* calibration in a tenet section, which is where over-claim is most costly.

### Reasoning-Mode Classification (editor-internal)
- Strict epiphenomenalism (L98): Mode One — internal selection-pressure argument. Intact.
- Inzlicht/Kurzban process models (L100): Mixed — Mode Two foundational pressure plus Mode Three boundary-marking. Intact.
- Illusionism / Graziano AST (L126): Mode Mixed — the regress is *disowned*, not deployed, with pressure relocated to the tractability of the seeming-question and an explicit boundary marker. The 2026-07-29 calibration (commit `5e52ddcf4`) holds; my edit touched only the quotation, not the argument.
- MWI (L150): Mode Three — explicit boundary marking. Intact.

No editor-vocabulary leakage in prose. No "This is not X. It is Y." construct. "load-bearing" not used in body.

## Optimistic Analysis Summary

### Strengths Preserved
- The line-88 functionalist-absorption ledger — explicitly declining to enlist Inzlicht/Kurzban as convergent support — is the single best piece of citation discipline in the article and is exactly what the brief's direction-inversion concern was testing for. Untouched.
- Naccache SCR residue as the honest survivor on the dualist side: verified exact, and it is doing real argumentative work in two places.
- Stapp/Tegmark objection stated against interest, with the post-decoherence-selection pivot rather than a dismissal.
- Three-faces structure (Calibration / Depletion / Modulation) and front-loaded lead.

### Cross-links
No new cross-links added — the article is at `soft_warning` and converged. All existing wikilinks resolve.

## Length

- **Before**: 3081 words total / **2492 authored prose** (apparatus 589w) — 8 words under the 2500 concepts soft threshold.
- **After**: 3099 words total / **2510 authored prose** (apparatus unchanged at 589w) — 10 words over soft.
- Net **+18 words**, **401 words to the 3500 hard threshold**.

The gain is entirely the irreducible cost of naming what two studies actually found in place of shorter over-claims: the Westbrook correction (+~20) partially offset by the Howard trim (−7) and a near-neutral Tallis de-quote. No argument was cut to chase the total, per the brief's guidance that the 3081 figure is apparatus-inflated.

## Remaining Items

**The Tallis quote is fabricated-as-verbatim at 15 further live loci.** Not touched — each needs its own context-sensitive rewording and this is a single-file review. Loci: [concepts/illusionism.md](/concepts/illusionism/) L89, [concepts/experiential-alignment.md](/concepts/experiential-alignment/) L151, [concepts/semantic-memory.md](/concepts/semantic-memory/) L130, [concepts/neural-correlates-of-consciousness.md](/concepts/neural-correlates-of-consciousness/) L126, [concepts/psychophysical-laws.md](/concepts/psychophysical-laws/) L213, [concepts/dualism.md](/concepts/dualism/) L143, [concepts/sleep-and-consciousness.md](/concepts/sleep-and-consciousness/) L122, [concepts/phenomenology-of-choice-and-volition.md](/concepts/phenomenology-of-choice-and-volition/) L146, [concepts/witness-consciousness.md](/concepts/witness-consciousness/) L143, [topics/epistemic-advantages-of-dualism.md](/topics/epistemic-advantages-of-dualism/) L112, [topics/attention-and-the-consciousness-interface.md](/topics/attention-and-the-consciousness-interface/) L98, [topics/consciousness-in-simple-organisms.md](/topics/consciousness-in-simple-organisms/) L191, [topics/meaning-of-life.md](/topics/meaning-of-life/) L162, [apex/attention-as-causal-bridge.md](/apex/attention-as-causal-bridge/) L136, [arguments/many-worlds-argument.md](/arguments/many-worlds-argument/) L156. Three further loci ([concepts/phenomenal-concepts-strategy.md](/concepts/phenomenal-concepts-strategy/) L149, [concepts/luck-objection.md](/concepts/quantum-indeterminacy-free-will/) L126, [research/illusionism-consciousness-2026-01-14.md](/research/illusionism-consciousness-2026-01-14/) L146) already use the phrase **unquoted** as prose and need no change — these are likely the uncorrupted originals.

## Stability Notes

Settled, do not re-flag: MWI bedrock (L150); decoherence/Zeno hedging; process-model physicalism as a genuine rival the Map cannot dispatch by phenomenal evidence alone; Schwartz OCD single-group limitation already disclosed; strict epiphenomenalism; Naccache modal-case framing.

**Newly settled by this pass — do not re-open:**
- The **Sauerbrei & Pruszynski joint parenthetical at L64 is correct**, not a direction inversion. The italicised *conscious* scoping is deliberate. Verified twice now (W16 install, W28 bandwidth-article web-verify, this pass).
- **Tegmark's figure is 10⁻¹³ s**, matching the whole corpus. Any future pass reintroducing 10⁻¹⁵ is a regression.
- **James's two quotes are verbatim at primary text.** Do not re-verify.
- **Naccache 2005 claim-match is exact including the SCR asymmetry.** Do not re-verify.