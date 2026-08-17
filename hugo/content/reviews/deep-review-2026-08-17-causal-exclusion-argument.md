---
ai_contribution: 100
ai_generated_date: 2026-08-17
ai_modified: 2026-08-17 10:05:39+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-17
date: &id001 2026-08-17
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-17 10:05:39+00:00
modified: *id001
related_articles: []
title: Deep Review - Kim's Causal Exclusion Argument
topics: []
---

**Date**: 2026-08-17
**Article**: [Kim's Causal Exclusion Argument](/concepts/causal-exclusion-argument/)
**Previous review**: [2026-07-20](/reviews/deep-review-2026-07-20-causal-exclusion-argument/) (and [2026-07-13](/reviews/deep-review-2026-07-13-causal-exclusion-argument/))

Quote-fidelity pass. The two prior reviews built a publisher-of-record ledger for the *reference block* and found it clean; neither checked the **body's quoted spans** against primary sources. That is an orthogonal axis, and it is where this pass found defects. "Ledger complete" is not "verbatim checked" — three of the article's body quotations were wrong, one of them reversing the polarity of the author it paraphrased.

Two structural gaps in the prior ledgers were also closed: five references (Shoemaker 2001/2007, Wilson 1999/2011, Yablo 1992) were added to the article *after* the 2026-07-13 ledger was compiled and had therefore never been publisher-verified; and three inline `Author YYYY` cites had no References entry at all.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

**1. Polarity inversion of Kim's own "far from obvious" remark.** The article read: *Whether reduction can be guaranteed at every physical level "is far from obvious," which is exactly why Block's worry has traction.* Kim's actual claim in "Blocking Causal Drainage" runs the other way: for powers to drain, the reduction option must be **ruled out** at every purely physical level, and Kim holds it far from obvious that *this* can be done. The article took Kim's burden-shifting hedge, flipped the proposition it attached to, and deployed it in support of Block — i.e. against the very reply the paragraph was describing.

This was also an **internal contradiction** detectable without the web check: the preceding sentence states that Kim "argues the descent is blocked at the physical levels because *reduction* is available there," and the next sentence then had Kim doubting that reduction is available. **Resolution**: restated Kim's burden-shift in his own direction, and moved the "reduction all the way down is an assumption, not a result" point to the critics, where it belongs. The article's substantive claim that Block's worry retains traction is preserved — it is now correctly attributed.

**2. False verbatim — `"no work left to do."`** Presented in quotation marks as Kim's wording for the supervenience worry. Kim's wording is not this. The nearest genuine Kim phrasing found is "No causal work is left for M" (cited in the secondary literature to *Mind in a Physical World* 1998, 126 n. 6), and the interrogative form "what causal work is left over for [the] mental property to do?". The article's string is a compression that reads more assertively than any located Kim sentence. The identical quoted string also appears in the IEP entry on the exclusion problem as the *encyclopedia author's own paraphrase* (Dwayne Moore's dormitivity example), not as a Kim quote — a plausible route by which it entered the corpus wearing quotation marks.

**Resolution**: de-quoted to plain paraphrase ("this leaves no causal work for M to do"). Deliberately **not** re-quoted to the "No causal work is left for M" form: that string reached me only through a search-result summary, never through the primary text, and minting a new verbatim claim plus a page/footnote cite on aggregator evidence is the failure this discipline exists to prevent. No citation was destroyed by de-quoting — the original quoted phrase carried no author or page.

**3. Misattributed phrase — `"screened off"`, framed as "in his phrase" (i.e. Kim's).** "Screening off" is standard vocabulary in the mental-causation literature descending from Reichenbach's probabilistic notion; SEP's *Mental Causation* entry uses it as the encyclopedia's own vocabulary and notes LePore and Loewer conceding that "mental properties are screened off by physical properties." No source located attributes the phrase to Kim as his coinage; it does not appear in Kim's own *Précis of Mind in a Physical World*, nor anywhere in the IEP exclusion entry. **Resolution**: replaced "in his phrase" with "in the literature's shorthand." The scare quotes are kept — they now mark a term of art rather than assert a quotation. Note this is a *weakening of an unsupported attribution*, safe in both directions: it does not assert that Kim never used the term, only that the article stops claiming he coined it.

**4. Orphan inline citations (three).** `Ehring 1996`, `Funkhouser 2006`, and a year-less "Bermúdez and Cahen" were cited inline with no References entries. **Resolution**: all three publisher-verified and added to References; the Bermúdez & Cahen cite gained its year (2015) and a note that it replies to Menzies directly in the same issue.

### Medium Issues Found

- **Lead name-attribution imprecision (fixed).** The lead listed "supervenience argument" and "master argument" as bare alternative names. Kim's *Précis* is explicit: *"My main argument is what I call 'the supervenience argument', sometimes also called 'the exclusion argument' in the literature."* "Master argument" is a commentator's label (e.g. *Philosophical Psychology* 21(5), "Assessing Kim's Master Argument"), not Kim's. Lead now distinguishes Kim's own label from the commentators'.

### Leads that came back FALSE (no change made)

- **The long Yablo quotation is genuine.** The driver flagged *"any credible reconstruction of the exclusion principle must respect the truism that determinates do not contend with their determinables for causal influence"* as reading like a later commentator rather than Yablo. It is Yablo's. SEP's *Determinables and Determinates* entry (§1.4) reproduces it as a direct quotation with the identical page cite, "(1992: 259)" — matching the article exactly, including the page. **Verbatim and correctly attributed; left untouched.** The primary PDF at MIT is an image scan with no text layer, so the SEP direct quotation is the best available anchor; it independently corroborates both wording and page.
- **Kim's causal-inheritance gloss** — accurate to the principle as standardly stated. No change.
- **List & Menzies' two-directional exclusion principle and realization-insensitivity** — correctly reported, including the striking downward direction. No change.
- **Evidence-kind disclosure** — see below; already compliant.

### Publisher-of-Record Citation Ledger

Body quotations (the new axis this pass added):

- Yablo 1992: 259, "any credible reconstruction…" — **real-correct, verbatim, page correct** (SEP direct quotation)
- Kim, `"no work left to do."` — **not verbatim** (de-quoted to paraphrase)
- Kim, `"screened off"` as *"in his phrase"* — **misattributed** (reframed as the literature's shorthand)
- Kim, `"is far from obvious,"` — **polarity-inverted** (restated in Kim's own direction)
- Kim, `"supervenience argument"` — **real-correct**, Kim's own label per his *Précis*
- `"master argument"` — real, but a commentator's label, not Kim's (lead now says so)
- Block, `"drains away"` / `"causal drainage"` — real-correct, standard
- Block's *epistemic* / *modal* two-version split — **framing softened.** The taxonomy under these two labels was located only in a later commentator reconstructing Block ("Causal Exclusion Without Causal Drainage"), not in Block's own text, which I could not retrieve. The article had asserted "Block frames this in two versions"; it now says "The worry has an *epistemic* strand… and a *modal* one," which is true regardless of who coined the labels. **Unresolved rather than disproved** — a failed retrieval is not evidence Block lacks the distinction, which is why the fix weakens the attribution instead of deleting the content.

References never previously verified (added after the 2026-07-13 ledger; all checked at publisher this pass):

- Shoemaker 2001, "Realization and Mental Causation," in Gillett & Loewer (eds.), *Physicalism and its Discontents*, CUP, 74–98 — **real-correct** (Cambridge Core + Crossref)
- Shoemaker 2007, *Physical Realization*, OUP — **real-correct** (OUP catalog)
- Wilson 1999, *The Philosophical Quarterly* 49(194): 33–52 — **real-correct** (Oxford Academic + Crossref)
- Wilson 2011, *The Monist* 94(1): 121–154 — **real-correct** (JSTOR + Crossref + OpenAlex)
- Yablo 1992, *The Philosophical Review* 101(2): 245–280 — **real-correct** (Crossref + PDC record)

Newly added (were inline orphans):

- Ehring 1996, "Mental Causation, Determinables and Property Instances," *Noûs* 30(4): 461–480 — **real-correct** (Crossref + Ehring's own SMU publications page). Publisher form has no Oxford comma before "and"; used the publisher form.
- Funkhouser 2006, "The Determinable–Determinate Relation," *Noûs* 40(3): 548–569 — **real-correct** (Wiley + Crossref + Funkhouser's own site)
- Bermúdez & Cahen 2015, "Mental Causation and Exclusion: Why the Difference-making Account of Causation is No Help," *Humana.Mente* 8(29): 47–68 — **real-correct at the journal of record**

⚠️ **Two metadata traps recorded for future passes.** (a) Bermúdez's own TAMU CV lists the 2015 paper as *Humana Mente* **21**; the journal itself says Vol. 8, **No. 29**. Pages agree. Do not "correct" 29 to 21 on CV evidence. (b) SEP's *Mental Causation* bibliography returned **two mutually inconsistent Funkhouser lines across two fetches**, both pointing at *Philosophical Studies* rather than *Noûs*, and one of them misfiled a 2002 *Pacific Philosophical Quarterly* paper as *Philosophy of Science*. That page's rendering is unreliable for this author — do not re-point the Noûs citation on an SEP lookup.

No superlative or currency claims in the body; empirical-record sweep not applicable (this is a philosophical-argument article, not an empirical one).

### Evidence-kind and decisive-assumption disclosure (standard adopted 2026-08-17)

**Compliant — no change needed.** This article is the first natural test of the new standard, and it passes on the counterfactual test: the prose would *not* read the same had Kim's argument been an experiment. The exclusion argument is introduced as "a set of individually plausible commitments that cannot all be true," the five premises are enumerated and named, and every response is tied to the specific premise it rejects (Bennett → premise 4; the subset account → premise 4 never engages; Yablo → non-rivalry via determination; the interventionists → the exclusion principle's necessity; Kim's own horn → premise 3; the three dualist options → premises 2 and 5 explicitly). The decisive assumption is stated for each move rather than left implicit. Block's drainage worry is likewise presented as an argument turning on whether a bottom level exists, not as a finding.

## Optimistic Analysis Summary

### Strengths Preserved

- The neutral-anatomy framing, and the discipline of deferring the Map's own premise-5 move to [overdetermination-dissolution-under-selection-only-interactionism](/topics/overdetermination-dissolution-under-selection-only-interactionism/) rather than re-arguing it here.
- The premise-by-premise mapping of the responses literature — this is what carries the evidence-kind compliance, and it was already right.
- The framework-boundary honesty in the subset and determinable paragraphs: both explicitly say the Map declines the route on a boundary rather than claiming to find a fault inside the account ("the subset strategy may work perfectly well for the non-reductive physicalist it was built for"). That is correctly-marked boundary engagement, not boundary substitution.
- The galilean-exclusion disambiguation in the lead.
- The Vaassen branch-splitting installed by the 2026-07-20 review — verified still intact and uncorrupted.

### Enhancements Made

- Kim's drainage reply now states his actual dialectical position, which makes the paragraph argue rather than merely gesture.
- Attribution precision in the lead (Kim's label vs. commentators').
- Three orphan cites resolved into a complete, publisher-verified References block.

### Cross-links Added

None. All outbound wikilinks already resolve; the article is well-integrated and does not need more.

## Reasoning-Mode Classification (editor-internal)

- Engagement with Kim (reductionist horn): **Mode Three — framework-boundary marking.** The article says the horn "is not on the table: it denies premise 3, the dualist's founding commitment." Honest boundary declaration, no claimed refutation. Correct.
- Engagement with the subset account (Shoemaker, Wilson): **Mode Three.** Explicitly marked as a boundary disagreement, with the concession that the strategy works for its intended non-reductive-physicalist audience. Correct.
- Engagement with Yablo: **Mode Three.** Same structure; the Map's refusal is located at premise 3.
- Block's drainage pressure on Kim: **Mode One — defective on its own terms**, correctly framed as internal to physicalism ("applies pressure to the exclusion reasoning from *within* physicalism, independent of any dualist commitment").

No boundary substitution found. No editor-vocabulary label leakage into article prose.

## Length

2532 → 2588 raw words (soft_warning at 103% of the 2500 concepts soft threshold). **This is a false over-length and was not treated as one.** Decomposed: body prose is 2147 words (86% of soft); the References block (247→~300) and Further Reading block (135) account for 382+ words of reference apparatus. The +56 is almost entirely the three publisher-verified References entries that closed the orphan-cite defect. Prose was deliberately **not** trimmed to offset apparatus growth — that would be metric-gaming at the cost of a correction.

## Propagation Check

Grepped both `obsidian/` and `hugo/content/` plus `archive/`, content only (excluding `reviews/` and `workflow/`, where pre-fix wording legitimately survives as an echo):

- `"no work left to do."` as a **quoted** Kim attribution: 2 content loci — this article and its source research note [causal-exclusion-argument-2026-07-13](/research/causal-exclusion-argument-2026-07-13/). **Both fixed** (the note seeded the article's phrasing). A third hit in [functional-seeming](/concepts/functional-seeming/) is unquoted ordinary prose about the Map's own argument, not a Kim attribution — correctly left alone.
- `"screened off"` / `"screens off"`: 10 content loci across the corpus. **Only this article attributed the phrase to Kim.** Every other locus uses it as unattributed term-of-art shorthand, which matches SEP's own practice and is correct. No corpus-wide fix required.

## Remaining Items

- **[type-token-causation](/concepts/type-token-causation/) line 58** carries `"If anything is causally efficacious in bringing about a physical event, it must itself be physical" (Kim, 2005, p. 17, paraphrased)` — quotation marks wrapped around something the article itself labels a paraphrase. That is the fabricated-verbatim shape even though it is self-flagged, and it sits in a different file, so it was out of scope here. Worth a targeted pass: either verify at the primary and drop "paraphrased", or de-quote.
- **Bermúdez & Cahen gloss** — the article says they "argue difference-making does not deliver the metaphysical exclusion Kim needs denied." Their actual thesis is sharper: the difference-making account entails ubiquitous violation of causal closure. The current gloss is not false, only vague; sharpening it needs the paper itself, which was not retrieved this pass.
- **Block's primary text was never retrieved** (NYU page returns empty, philarchive 403s, archive.org unreachable). The epistemic/modal attribution is softened rather than settled. A future pass with journal access could confirm whether the labels are Block's own and restore the stronger attribution if so.

## Stability Notes

- The Yablo 1992: 259 quotation is now **verified verbatim with a correct page cite** against SEP's direct quotation. Do not de-quote it. It has now survived one explicit fabrication challenge; record that here so the next pass does not re-litigate it.
- The three de-quoted/reframed Kim spans should stay de-quoted unless someone reaches Kim's primary text and can pin exact wording *and* page. Re-quoting from a search summary or an aggregator is the specific error being guarded against.
- Physicalists, eliminativists, and MWI defenders reject the Map's non-identity and quantum-interaction premises from outside the framework — bedrock disagreement, not a defect. Do not re-flag. (Carried from both prior reviews.)
- The five-premise reconstruction here vs. the four-premise one in [overdetermination-dissolution-under-selection-only-interactionism](/topics/overdetermination-dissolution-under-selection-only-interactionism/) are both standard. Do not harmonise. (Carried.)
- Vaassen must not be re-collapsed into the accept-benign-overdetermination branch. (Carried from 2026-07-20; verified intact this pass.)
- The raw word count will keep reading `soft_warning` because of the reference apparatus. Decompose before condensing — the prose is at 86%.