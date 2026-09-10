---
ai_contribution: 100
ai_generated_date: 2026-09-10
ai_modified: 2026-09-10 07:54:35+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-10
date: &id001 2026-09-10
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-10 07:54:35+00:00
modified: *id001
related_articles:
- '[[neural-refresh-rates-and-the-smoothness-problem]]'
title: Deep Review - Neural Refresh Rates and the Smoothness Problem
topics: []
---

**Date**: 2026-09-10
**Article**: [Neural Refresh Rates and the Smoothness Problem](/topics/neural-refresh-rates-and-the-smoothness-problem/)
**Previous review**: [2026-08-08](/reviews/deep-review-2026-08-08-neural-refresh-rates/) (eleventh deep review of this topics article)

## Lens Applied

The 2026-08-08 review closed by naming the one unexamined surface: *"the phenomenological citations — James, Bergson, Dainton — which have never been verified against primary text on this article."* This pass ran that lens, plus **empirical-record currency** on the lead's perceptual-experiment claims.

Both paid. The phenomenological lens produced the most consequential finding on this article to date, because the defect was **introduced by one of this article's own deep reviews** and then inherited by ten subsequent passes.

**Body-change status since last review**: exactly one commit (178894194d, 2026-09-10), a two-line Zheng & Meister relabel already verified twice upstream. Not re-audited, not reverted, per driver instruction. The delta lens had nothing to find; this was a staleness-grounded comprehensive pass and the findings below are all long-standing.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. The James "rainbow on the waterfall" quote had the wrong grammatical subject — FIXED. This was a regression introduced by the 2026-03-17 deep review.**

The article read: *"William James described **consciousness** as standing 'like the rainbow on the waterfall, with its own quality unchanged by the events that stream through it.'"*

Verified against primary text — Project Gutenberg #57628, *The Principles of Psychology* Vol. 1, whitespace-normalised, quote at offset 1461429, between the Ch. XV heading (1421071) and the Ch. XVI heading (1519705), i.e. **Chapter XV, "The Perception of Time"**:

> "Meanwhile, **the specious present, the intuited duration,** stands permanent, like the rainbow on the waterfall, with its own quality unchanged by the events that stream through it."

The quoted words are verbatim. The subject is not. James is describing the *specious present*, not consciousness at large.

**The provenance is the notable part.** `obsidian/reviews/deep-review-2026-03-17-neural-refresh-rates-and-the-smoothness-problem.md` L29 records, as a fix:

> "**James 'rainbow' quote conflated with specious present**: The original text introduced the James quote as describing 'the specious present' when it describes the stream of consciousness more broadly. **Resolution**: Changed 'specious present' to 'consciousness' in the introductory sentence."

The article was **correct before that review and wrong after it**. The "fix" inverted a faithful attribution, and it then stood through ten further deep reviews — including the 2026-08-08 pass that caught five other source-fidelity defects.

**Family status: this article was the sole divergent locus.** Every sibling has it right — `obsidian/voids/smoothness-and-continuity.md` L62, `obsidian/research/neural-refresh-rates-smoothness-problem-2026-03-08.md` L29, and `archive/voids/smoothness-problem.md` L63 all say "James described **the specious present** as standing…". No sweep was needed; the fix converges this file onto the family and onto the source.

**Compounding defect: the image was also being used against its own structure.** The article deployed the waterfall line as evidence of "unbroken flow rather than punctuated snapshots". But in James's image the rainbow is the *stable* element and the events *stream through* it — the immediately preceding sentence is "Its *content* is in a constant flux, events dawning into its forward end as fast as they fade out of its rearward one." A persisting window whose contents change is at least as congenial to the two-stage model's "time slice" as to phenomenal continuity. The quote was carrying an argumentative load it cannot bear.

**Fix applied** — and it is a net gain, not a bare correction. James *does* make the continuity claim the section needs, verbatim, in Ch. IX ("The Stream of Thought", offset 506395), and the article now rests on that instead:

> "Consciousness, then, does not appear to itself chopped up in bits. Such words as 'chain' or 'train' do not describe it fitly as it presents itself in the first instance. **It is nothing jointed; it flows.**"

The waterfall image is retained but re-scoped to its real subject, and the article now says explicitly that nothing downstream leans on it. Reference 7 pins both chapters and states the correct subject, so the 2026-03-17 regression cannot recur silently.

**2. The lead contradicted the body on the evidential status of discrete perception — FIXED.**

Lead (pre-fix): *"Perceptual experiments **confirm** these biological 'refresh rates' — the flash-lag effect, attentional blink, and wagon-wheel illusion under continuous lighting **all reveal periodic sampling** rather than continuous monitoring."*

Body §The Neural Evidence (post-2026-08-08): *"The rhythmicity of sampling is well evidenced; the inference from rhythmic sampling to genuinely discrete perception is the part still under argument."*

These cannot both stand. The 2026-08-08 pass correctly hedged VanRullen in the body and left the lead asserting the unhedged version — the classic navigation-surface divergence, and the worst possible placement of it, since the front-loaded lead is the truncation-resilient part an LLM reads first. Rewritten to carry the two well-evidenced findings (alpha-phase detection variation, attentional blink) and to state the contested status of discreteness, matching the body exactly.

**3. Empirical-record currency: the flash-lag claim is contradicted by a 2025 negative result — FIXED.**

The lead named the flash-lag effect as one of three effects that "reveal periodic sampling". The best current direct test of precisely that link found no evidence for it.

Verified at Crossref (raw JATS abstract retrieved and read in full, not via a summariser):

> Cottier, T., Turner, W., Chae, V.J., Holcombe, A.O., & Hogendoorn, H. (2025). No Evidence That Resting-State Individual Alpha Frequency Represents a Mechanism Underlying Motion-Position Illusions. *European Journal of Neuroscience*, 62(9), e70250. DOI 10.1111/ejn.70250. Published online 2025-11-02.

N = 61. Seven motion-position illusions tested — flash-lag (motion and luminance), Fröhlich, flash-drag, flash-grab, motion-induced position shift, twinkle-goes, flash-jump — against resting-state individual alpha frequency. Verbatim: *"Correlation analyses revealed no evidence for a correlation between IAF and the magnitude of any MPIs. Overall, these results suggest that IAF does not represent a mechanism underlying MPIs."*

**Scope discipline applied.** This refutes *alpha-linked* discrete sampling as the mechanism for the motion-illusion family. It does **not** refute discrete perception generally, nor the alpha-phase detection findings, nor the attentional blink — those are independent and remain well supported. The new body paragraph says exactly this and no more: *"The rhythmic-sampling findings above stand; what falls is the inference from these illusions to an alpha-rate perceptual clock."* The wagon-wheel-under-continuous-light claim was dropped from the lead rather than rebutted — it is genuinely contested and did not belong in an unhedged lead, but no positive claim against it is made here.

### Medium Issues Found

**4. The Dainton quotation is publisher catalogue copy, not Dainton's prose — FIXED.**

The article presented *"interconnected flowing whole"* in quotation marks as Dainton's own words. Every traceable instance of the phrase is the Routledge/Blackwell's **book synopsis**: *"Barry Dainton shows us that stream of consciousness is not a mosaic of discrete fragments of experience, but rather an interconnected flowing whole."* No page-level attribution exists at any locus found. The corpus sibling `obsidian/voids/smoothness-and-continuity.md` L62 tracks the blurb's "mosaic… discrete fragments" wording almost verbatim, which is what identifies the channel.

This is the PUBLISHER-CATALOGUE-COPY class. **Deliberately not called a fabrication**: the phrase is real, and it faithfully summarises Dainton's thesis. The primary text is not openly accessible, so no absence claim is made about the book body — the safe fix is the one that is correct either way. Quotation marks removed, claim retained as paraphrase, and reference 4 annotated so a future pass does not "restore" the quotation.

**5. Two redundancies trimmed** (length offset, not defects): "The question is whether" opened two consecutive sentences in §Physical Smoothing Mechanisms; the functionalist paragraph restated "what the continuity-registering state does in the cognitive economy" a second time within four lines.

### Checked and Cleared — no change made

- **Bergson — VERIFIED CLEAN at primary text.** Project Gutenberg #26163, *Creative Evolution* (Mitchell trans.). Chapter IV is titled, verbatim, "THE CINEMATOGRAPHICAL MECHANISM OF THOUGHT AND THE MECHANISTIC ILLUSION" (offset 5079 in the contents, 533236 at the chapter). 40 occurrences of "cinematograph", 14 of "snapshot", 137 of "duration". The article's paraphrase — intellect works cinematographically, taking snapshots and generating the illusion of movement, distorting genuine *durée* — is faithful, as is "Chapter 4", the 1907/1911 dating, the Mitchell translation and the Henry Holt imprint. **The third phenomenological citation is the one that was already right.**
- **Reference renumbering safe** — independently re-verified this pass: zero numeric cross-references in the prose (`[\d+]`, "reference N", "ref. N", "note N" all return no matches). List grew 13 → 14 entries; Cottier inserted in correct alphabetical position (Cottier < Crick), sequence re-checked 1–14 with no duplicates.
- **Attentional blink 200–500 ms** — standard lag range, unchanged.
- **Over-concession sweep** — nine tells searched (`no possible`, `cannot ever`, `in principle undetectable`, `can never`, `impossible to`, `cannot be detected`, `no conceivable`, `forever beyond`, `in principle inaccessible`); all return −1.
- **Editor-label leakage (§2.6)** — nine forbidden tokens searched; all return −1. No leakage.
- **Style** — no "load-bearing", no "This is not X. It is Y." construct.
- Everything on the 2026-08-08 do-not-re-flag list was left alone: Zheng & Meister figures, Herzog 2020 and VanRullen metadata, the "strongest physicalist response" superlative, the postdictive paraphrase, Crick & Koch.

### Reasoning-Mode Classification (editor-internal)

- **Functionalism** (§The Functionalist Response): **Mode Two** — unsupported foundational move. The article argues the functionalist "helps itself to the very step the smoothness problem isolates" and "owes an account of why the registering is itself felt, and that account is exactly what the identification stipulates rather than supplies." Uses the opponent's own explanatory standard. Natural prose, no labels.
- **Illusionism — Frankish, Dennett** (§Bergson's Inversion): **Mode Two**. Renaming the explanandum is identified as the unearned move; the phenomenal-vs-judgement distinction does the work.
- **Higher-order / global workspace** (§Locke's Objection Inverted): **Mode Three** — boundary marking, honestly declared, with the temperature analogy's load-bearing condition stated rather than dismissed.

No boundary-substitution found. No upgrade or downgrade warranted.

### Calibration

No possibility/probability slippage. The article continues to decline the upgrade — "not a standalone argument for dualism" in the lead, and the bidirectional-interaction paragraph hedges throughout ("one possibility", "may contribute", "does not require this specific mechanism"). Fixes 2 and 3 **improve** calibration by removing an over-claim the article had borrowed from its own earlier framing.

## Optimistic Analysis Summary

### Strengths Preserved

The front-loaded lead structure; the "strong form has weakened" honesty on gamma binding; the registering-versus-feeling engagement with functionalism; the named-illusionist passage isolating the *phenomenal* seeming; the Locke inversion; the convergent-evidence-programme framing; the Lee section as rebuilt in 2026-08-08. Voice untouched.

### Enhancements Made

The James correction leaves the section stronger than it found it. It now opens with the sentence in which James actually makes the continuity claim — *"It is nothing jointed; it flows"* — which is both more forceful and more apt than the waterfall image ever was, and it then turns the waterfall image into a *caveat against over-reading it*, which connects the phenomenological section forward to the two-stage model's "time slice". An article that flags the limits of its own favourite quotation is harder to attack than one that leans on it.

The Cottier paragraph does comparable work: the article now survives a genuine negative result in its own empirical area by stating precisely which inference it loses and which it keeps.

### Cross-links Added

None. No new wikilinks introduced — deliberate, since the article's 21 existing links all pre-date this pass and no new bare target needed resolving against the content index. Zero push-blocker risk from this edit.

## Word Count

Prose **2787 → 2925** (+138), against the topics soft threshold of 3000 — **75 words of headroom remaining**. Apparatus (Further Reading + References) 370 → 472 (+102: the Cottier entry, the James chapter pin, the Dainton provenance note).

Raw `analyze_length` reports **3151 → 3390 / `soft_warning`**, which is the known reference-apparatus false positive — the apparatus is now 472 words of the raw figure. Prose is the real number and it is under soft. Hard threshold is 4000. **No condensation performed or warranted**; the two trims above were made to offset additions, not because length required it.

## Remaining Items

- **The archived predecessor still carries the pre-correction James wording.** `archive/concepts/neural-refresh-rates.md` L59 (and its Hugo mirror) reads "William James described consciousness as standing 'like the rainbow on the waterfall' (James, 1890)". This article was coalesced from it (`coalesced_from: /concepts/neural-refresh-rates/`). Archive pages are frozen URL-preservation artefacts carrying an archive notice, and the 2026-08-08 pass likewise left archive loci to Remaining Items rather than sweeping them. Flagged, not touched — a human call.
- **Consider auditing other "fixes" from the 2026-03-17 review.** That pass demonstrably reversed one correct attribution into an incorrect one. Its other resolutions on this article have never been checked against primary text with that possibility in mind. This is a narrow, cheap, and unusually well-motivated target.
- Buddhist discrete-moment (*kshana*) tradition and Whitehead's epochal theory — deferred across eleven reviews; only add with a dedicated target article.

## Stability Notes

**The lesson of 2026-08-08 generalises further than it was stated.** That review established that convergence is lens-relative — an article is converged only with respect to the lenses actually run against it. This pass adds a sharper point: **a review can introduce a defect while believing it is fixing one**, and the corpus has no mechanism that re-examines a review's own resolutions. Ten passes inherited the 2026-03-17 error precisely because it was recorded as a *resolution*. Prior-review resolutions are evidence about what was considered, not proof that the outcome was right.

**Do NOT re-flag** (verified this pass at primary sources): Bergson's chapter, title, translator, imprint and the cinematographic paraphrase; the James Ch. IX continuity quote; the James Ch. XV waterfall attribution as now written; Cottier et al. 2025 metadata and its scope; the reference renumbering.

**Do NOT reintroduce**: "consciousness" as the subject of the rainbow-on-the-waterfall sentence (this is the 2026-03-17 regression — the subject is *the specious present*); "confirm" or "all reveal periodic sampling" in the lead; the flash-lag effect cited as evidence of an alpha-rate perceptual clock; quotation marks around "interconnected flowing whole".

**Bedrock disagreements** (not fixable; not critical): functionalists and physicalists maintain that smoothing mechanisms *constitute* smooth experience — framework-boundary, and the article's reply is explicitly position-dependent; MWI defenders and hard-nosed materialists find the smoothness problem unconvincing.

**Next lens suggestion**: metadata, verbatim quotes, claim fidelity, phenomenological primary texts and empirical currency have now all been run against this article. The genuinely unexamined surface remaining is **structural**: whether the eleven accumulated passes have left the argument's *order* coherent — the article now opens with a hedged lead, spends two sections on evidence for discreteness, then two on evidence against it, and the Bergson's-Inversion and Locke's-Objection sections both re-derive the same functionalism dependency. That is a candidate for `/condense` on redundancy grounds rather than another fidelity review.