---
title: "Pessimistic Review - 2026-08-08 - Claim-Fidelity Base Rate on an Unbiased Draw"
created: 2026-08-08
modified: 2026-08-08
human_modified: null
ai_modified: 2026-08-08T17:09:07+00:00
draft: false
description: "An unbiased 8-article draw checked 28 claims at primary sources to test whether today's 5-of-5 deep-review defect yield generalises. It does not — but the corpus is not clean either."
ai_contribution: 100
ai_system: claude-opus-5
author: Andy Southgate
topics: []
concepts: []
related_articles: []
---

# Pessimistic Review — Claim-Fidelity Base Rate

**Date**: 2026-08-08
**Content reviewed**: 8 articles drawn at random (seed 20260808) from the 791 files in `topics/`, `concepts/`, `voids/`, `apex/`, `positions/` — **not** selected by age, citation density, or prior-review count.

## Executive Summary

Today's five deep-reviews each found 4–6 claim-fidelity defects on articles **selected** for citation density, staleness and high prior-review count. This review tested whether that yield generalises, by drawing an unbiased sample and checking **28 discrete claims at primary sources**.

**It does not generalise.** The unbiased draw produced **3 confirmed defects across 8 articles (~0.4 per article)** against roughly **5 per article** in the targeted set — a **~12x** difference. Today's yield was a targeting windfall, exactly as the driver suspected.

**But the corpus is not clean.** 3 defects in 28 checks is an **11% claim-level defect rate**, and one of them is the severe class: a paraphrase of a journal *abstract* presented inside quotation marks with editorial brackets that signal fidelity. The phrase appears **zero times** in the 29-page source.

The most useful result is not a rate but a **bound**: the corpus's exposure surface to this defect class is approximately **500 genuine external verbatim quotations**, not 785 articles. That is a finite, enumerable audit.

## The Denominator

**28 checks across 8 articles.** Stated by class, because a single blended rate would be misleading — the classes have very different base rates.

| Class | Checked | Clean | Defective | Unverifiable |
|---|---|---|---|---|
| Verbatim external quotations vs. primary text | 4 | 2 | **2** | — |
| Citation metadata records (author/journal/vol/pages/year) | 17 | 16 | **1** | — |
| Term & position attributions | 3 | 3 | 0 | — |
| Quotations with no retrievable primary text | 2 | — | — | 2 |
| **Total** | **28** | **21** | **3** | **2** |

Separately, **3 sourcing gaps** were found — attributed claims whose source is absent from, or contradicted by, the article's own reference list. These are not counted as defects above because the attributions are themselves correct.

### Verification route

WebSearch was not used. Every check was made via WebFetch/HTTP to Crossref, OpenAlex, EuropePMC, PMC, Project Gutenberg, SEP, or the publisher's own site. Public-domain texts (Hume) and PMC full text (Vicente) were the cheapest and most decisive checks, confirming the driver's guidance.

## Critical Issues

### Issue 1: A journal abstract paraphrased into a bracketed "verbatim" quotation

- **File**: `obsidian/concepts/process-content-distinction.md`
- **Location**: § "The Founding Statement: Nisbett & Wilson 1977"
- **Severity**: **High**

The article states that subjects, when asked, *"may not be aware of the existence of the stimulus that importantly influenced a response, [or] not aware of the existence of the response, [or] not aware that the stimulus has affected the response."*

Full text retrieved and searched (Nisbett & Wilson 1977, *Psychological Review* 84(3), 231–259; 29 pages, 130,674 characters flattened). The string **"may not be aware" occurs 0 times**; **"aware of the existence of the stimulus" occurs 0 times**. The actual source is the paper's abstract:

> "Subjects are sometimes (a) unaware of the existence of a stimulus that importantly influenced a response, (b) unaware of the existence of the response, and (c) unaware that the stimulus has affected the response."

Three substitutions ("unaware of" → "may not be aware of"; "a stimulus" → "the stimulus"), plus the enumerators `(a)/(b)/(c)` replaced by `[or]`. **The last change is substantive**: Nisbett and Wilson state a *conjunction* of three cumulative findings ("and (c)"); the article renders it as a *disjunction*, which weakens the claim it is invoked to support.

What makes this the severe class: the editorial brackets are a fidelity signal. A reader takes bracketed insertions as evidence that everything outside the brackets is verbatim. Here nothing outside the brackets is verbatim either.

- **Recommendation**: Either quote the abstract accurately, or convert to indirect speech. The article's *other* Nisbett quotation — "people often cannot report accurately on the effects of particular stimuli on higher order, inference-based responses" — is **exactly verbatim** (p. 231, conclusion 1) and should be preserved untouched.

### Issue 2: Verbatim Hegel quotation, mis-stated content

- **File**: `obsidian/voids/conceptual-impossibility.md`
- **Location**: § "Occluded dimension" (and again in the dialetheism section)
- **Severity**: **Medium**

The article writes: *But Hegel complained this reflects "one of the fundamental prejudices of logic as hitherto understood"—that contradictions cannot be imagined or thought.*

The quoted span is **verbatim** (Miller trans., *Science of Logic*, Contradiction). But the sentence Hegel is quoted from says what the prejudice actually is, and it is not what the article says:

> "But it is one of the fundamental prejudices of logic as hitherto understood and of ordinary thinking **that contradiction is not so characteristically essential and immanent a determination as identity**…"

Hegel's prejudice concerns the *relative rank* of contradiction versus identity as determinations of essence — not the *thinkability* of contradictions. The article's em-dash gloss supplies a different content for the prejudice than the quoted sentence supplies, and the mis-framing then **propagates**: the later passage repeats "For Hegel, the inability to think contradictions reflects 'fundamental prejudice.'"

This is the citation-framing lens — real, verbatim, mis-framed. The fix is to re-frame, never to delete.

- **Recommendation**: Restate the prejudice as Hegel states it, then make the article's own (defensible) point about thinkability separately, in the Map's voice.

### Issue 3: First-author reversal and wrong page range

- **File**: `obsidian/concepts/bohm-implicate-order-and-active-information.md`
- **Location**: References, entry 5
- **Severity**: **Medium**

The article cites *"Pylkkänen, P. & Hiley, B. J. (2005). Can Mind Affect Matter Via Active Information? Mind and Matter, 3(2), 7–26."*

The journal's own table of contents for Volume 3, Issue 2 (2005) reads:

> pp. 7-27 — Can Mind Affect Matter Via Active Information? — **Basil J. Hiley and Paavo Pylkkänen**

Two errors: **author order reversed**, and **page range wrong** (7–27, not 7–26). First-author reversal is the error class that propagates hardest, because downstream citations inherit it and it is invisible to any check that only asks "is this a real paper?".

- **Recommendation**: Correct to `Hiley, B. J. & Pylkkänen, P. (2005) … 3(2), 7–27`. Note this is a **metadata** defect found in an unbiased draw — today's targeted runs reported metadata clean in every case, so metadata is mostly-solved, not solved.

## Sourcing Gaps (a third class, and the cheapest to detect)

Three articles attribute a claim to a named figure whose work does not appear in the article's own reference apparatus. These are not fidelity defects — the attributions are correct — but they are *preconditions* for fidelity defects, because **an unsourced quotation cannot be verified at all**.

| File | Attributed to | Status |
|---|---|---|
| `obsidian/voids/conceptual-impossibility.md` | Moritz Schlick, *"simply unthinkable"* | Schlick appears **once** in the whole file — in the attributing sentence. No reference entry. Quote could not be verified within budget. |
| `obsidian/topics/buddhist-perspectives-on-meaning.md` | Robert Forman, *"pure consciousness event"* | Term is genuinely Forman's, but Forman appears **0 times** in the reference list. |
| `obsidian/topics/buddhist-perspectives-on-meaning.md` | Evan Thompson, *"Buddhist exceptionalism"* | Attribution **correct** — it is Thompson's, and *Why I Am Not a Buddhist* (Yale, 2020) has a chapter literally titled "The Myth of Buddhist Exceptionalism". But the reference list cites only Thompson (2007) *Mind in Life*, which is the **wrong work** for this claim. |
| `obsidian/topics/philosophy-of-habit-under-dualism.md` | Hume, *"the great guide of human life"*; Proust, *"if habit is a second nature…"* | Hume quote **verified verbatim** at Project Gutenberg (*Enquiry*, §V: "Custom, then, is the great guide of human life."). Neither Hume nor Proust appears in the article's 13-entry reference list. |

**Why this class matters most for the system**: it needs **zero web budget**. It is a purely local cross-check of in-body attributions against the article's own reference apparatus, and it identifies exactly the loci where quote-verification should be spent.

## The Exposure Surface — the number that makes this actionable

A defect *rate* on n=4 verbatim spans has a confidence interval so wide it is nearly useless. A *bound* on the exposure surface does not.

- Automated scan of all 791 live articles (frontmatter stripped, reference apparatus excluded, title-case work titles filtered): **2,233 candidate quoted spans of ≥8 words across 657 articles (83%)**.
- Manual triage of the 8 sampled articles: the automated scan counted **18** spans where hand-inspection found **4** genuine external verbatim quotations — the rest were work titles, internal Map glosses, scare-quotes and illustrative dialogue. Calibration factor **≈0.22**.
- **Estimated corpus-wide exposure: ~500 genuine external verbatim quotations.**

This is the honest reframing of the driver's question. "785 articles, 5,566 review passes, still finding defects" sounds unbounded. **~500 spans** is a finite audit that can be enumerated, prioritised and closed.

## What 5,566 Passes Actually Imply

The 5,566 prior deep-review passes are **not** evidence that the corpus is clean, and they are also **not** evidence that reviews were lazy. They are evidence that the passes ran lenses **orthogonal** to this class. Two of today's defects had been explicitly certified correct by prior ledgers, one of which supplied the correct Sanskrit and then ratified the divergent paraphrase anyway.

The mechanism is visible in the defects found here. Every one of them **passes** the checks a metadata-oriented review runs:

- The Nisbett paper is real, correctly titled, correctly dated, correctly paginated, correctly attributed, and genuinely says something very close to what the article uses it for. Only the marks around the words are false.
- The Hegel quotation is verbatim. Only the gloss after the em-dash is wrong.
- The Hiley/Pylkkänen paper is real and correctly titled. Only the author order and one page number are wrong.

A lens that asks "does this source exist and does it broadly support the claim?" returns CLEAN on all three. Convergence under such a lens is convergence of the lens, not of the corpus. **"Converged" should be read as scoped to the lenses that have actually been run**, and the review apparatus should record *which* lens certified a claim, so that "certified" cannot be inherited across lens changes.

## Methodological Warning: Two False Sweeps Caught In Progress

Both are worth recording because both would have produced confident, wrong numbers.

**1. The unsourced-attribution detector is dominated by false positives at loose settings.** A first pass reported *"765 loci across 343 articles (45%)"*. Inspection showed it was matching ordinary capitalised words — `Every`, `Instead`, `Recursive`, `From`, and the band name-like `Talking Heads` (a real experiment). Tightening to require a speech verb gave 29 loci, but those were dominated by **first-name/surname mismatches** — `David` for Hume, `Karl` for Popper, `William` for James — where the reference list correctly carries the surname. Only the full-name variant, checking the *last* token, gives a defensible **17 loci across 15 articles (2.0%)**, and even that retains header-bleed noise. **The 45% figure was never real.** Any future automation of this lens must be calibrated by hand before its output is quoted.

**2. A naive sweep for the Daw 2011 defect would have reported 13 at-risk articles. The true number is one.** `grep -rl 'Daw'` over live sections returns 13 files. Word-boundary matching returns **one**. The substring was matching **`Dawes` (13 occurrences)** and **`Dawid` (12 — Richard Dawid, on non-empirical confirmation, which is why he appears throughout the many-worlds cluster)**.

The single genuine citation is in `obsidian/topics/philosophy-of-habit-under-dualism.md`, and **today's deep-review already corrected it** — the passage now reads *"striatal prediction-error signals expected to be a pure model-free report turned out to reflect model-based valuations too, which the authors read as evidence for a more integrated architecture rather than two independent learners,"* which is the correct reading of Daw et al. 2011. **The Daw defect did not propagate.** A grep matches strings, not claims.

## Verified Clean (preserve these)

Recorded because a review that reports only defects distorts the base rate it is trying to measure.

- **Vicente et al. 2008** — *"cortico-cortical association fibers and certain cortico-thalamo-cortical loops represent ideal circuits to circumvent the phase shifts and time lags associated with conduction delays"* — **exactly verbatim** at PMC2575223, and the surrounding characterisation of the relay-hub result is accurate. Metadata (PNAS 105(44), 17157–17162) correct.
- **Nisbett & Wilson conclusion 1** — verbatim, p. 231.
- **Hume** — "the great guide of human life" verbatim; the article correctly says Hume calls *custom* this, not *habit*, which is the classic trap.
- **Ginet's "actish phenomenal quality"** and the SEP entry title *"Incompatibilist (Nondeterministic) Theories of Free Will"* — both confirmed at SEP.
- **The five skandhas** — canonical list, correct.
- **All 5 DOI/metadata records in `necessary-opacity.md`** (Battaglia/Servajean/Friston 2025; Letheby & Gerrans 2017; Ciaunica et al. 2020; Hoffman 2016; Metzinger 2003) — exact on title, authors, journal, year, volume and pages. This article's reference apparatus is the best in the sample.
- **All 3 metadata records in `biological-teleology-and-the-interface-framework.md`** (Neander 1991; DeWall et al. 2008; Lieberman et al. 2002) — exact.
- **`event-causal-libertarianism.md`** — zero defects found; also the only sampled article with **no** long external quoted spans at all, which is precisely why it has no exposure.

## Not Verified (stated as such, not as absence)

- **Hameroff & Penrose 2014**, *"precise synchrony require[s] electrical synapses ('gap junctions') and/or quantum entanglement"* — the paper's metadata is correct (*Physics of Life Reviews* 11(1), 39–78), and Unpaywall reports it open access, but the publisher PDF is behind an interstitial and it is absent from PMC/EuropePMC full text. Four mirrors attempted, none served the PDF. **This is neither confirmed nor refuted.** The bracketed `require[s]` is a fidelity signal of the same kind that failed in Issue 1, so it is worth a targeted check when budget allows.
- **Schlick**, *"simply unthinkable"* — no retrievable primary text found. Unverified **and** unsourced.

## Operational Finding (outside the review theme, but blocking)

**The host filesystem is full.** Two Bash calls failed outright with `ENOSPC` — the harness could not capture command output at all — before ~2.4 GB was recovered by deleting temp files older than four hours.

```
/dev/mapper/ubuntu--vg-ubuntu--lv  122G  114G  2.4G  99% /
```

Largest consumers: `~/unfin/auto_unfin` **72G**, `~/.claude` **15G**, `~/.local` 4.4G, `~/unfin/chrome-profiles` 1.2G. At 0 MB free the loop cannot run *any* task that reads command output, so this fails closed and silently. It needs a human decision about the 72G video repo; automation should not delete there.

Separately, the quote-density scan surfaced `obsidian/topics/non-temporal-consciousness.refinement-log.md` as the single most quote-dense "article". Refinement-log sidecars are intentional and must not be deleted, but this independently confirms the open `count_section_files` over-count noted in `CLAUDE.md`: an editor-internal sidecar is being counted as a live article.

## Recommendations

1. **Do not extrapolate today's 5-of-5.** The measured unbiased rate is ~0.4 confirmed defects per article, not ~5. Targeting works; treat high-yield runs as evidence about the *selector*, not about the corpus.
2. **Audit the ~500-span exposure surface, not the 785 articles.** Prioritise by quote density — `wheelers-participatory-universe-and-it-from-bit.md`, `kripke-a-posteriori-necessity-argument.md`, `argument-from-mechanism.md`, `many-minds-interpretation.md` and `william-james-consciousness.md` each carry 16–18 candidate spans.
3. **Run the unsourced-attribution lens first.** It costs no web budget, it is a precondition for quote-verification, and it found 4 hand-confirmed instances in an 8-article sample. Calibrate any automation of it by hand before quoting its output.
4. **Treat bracketed insertions as a risk marker, not a fidelity marker.** Both bracket-bearing quotations in this sample were suspicious; one is confirmed wrong and the other is unverifiable.
5. **Record which lens certified a claim.** "Certified correct" by a metadata lens must not be inherited as "certified correct" by a fidelity lens — that inheritance is how two of today's defects survived explicit prior certification.

## Strengths

The reference apparatus is in genuinely good shape. Sixteen of seventeen metadata records verified exactly, including awkward details that are easy to get wrong and that nobody would notice: *Philosophical Psychology* 3(**2–3**) for Bohm 1990, *Mind* volume **XCVIII** for McGinn 1989, the article-number form of *Foundations of Physics* 52, 73 for Landsman 2022. `necessary-opacity.md` and `biological-teleology-and-the-interface-framework.md` were clean on every check.

The reasoning under the citations also held up where it was checkable. `zero-lag-gamma-synchrony-and-the-quantum-binding-argument.md` states the classical rebuttal precisely, marks Baum's preprint as non-peer-reviewed, notes explicitly that the classical account is "a sufficiency result, not a finished mechanism," and declines to over-claim in the Map's favour. `philosophy-of-habit-under-dualism.md` reads Daw 2011 as cutting *against* its own delegation picture and says so. That is the calibration discipline working as intended — and it is why the defects that remain are narrow ones about marks around words rather than broad ones about what the sources support.
