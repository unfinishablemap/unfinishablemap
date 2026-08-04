---
title: "Deep Review - The Interpreter Module and the Narrative Construction of Unity"
created: 2026-08-04
modified: 2026-08-04
human_modified:
ai_modified: 2026-08-04T06:54:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-04
last_curated:
---

**Date**: 2026-08-04
**Article**: [[interpreter-module-narrative-construction-unity|The Interpreter Module and the Narrative Construction of Unity]]
**Previous review**: [[deep-review-2026-07-16-interpreter-module-narrative-construction-unity|2026-07-16]]

**Delta since last review**: one commit (`60318067c`) added the anarchic-hand mirror-case paragraph and its Further Reading entry. That paragraph was uncited on arrival, and re-reading the article around it surfaced two source-fidelity defects that the 2026-07-16 metadata ledger did not reach — both running in the Map's favour, which is why a clean metadata pass missed them.

## Publisher-of-Record Citation Ledger (§2.4)

The 2026-07-16 ledger verified all six then-current entries as real-correct. This pass re-opened the two cites whose *claims* the body leans on, and verified the three new entries. Metadata for Dennett 1992, Gazzaniga & LeDoux 1978, Gazzaniga 2011 and Nisbett & Wilson 1977 is carried forward unchanged from that ledger — those References lines were not modified and their bodies' use of them was not in question this pass.

- Pinto, Neville, Otten, Corballis, Lamme, de Haan, Foschi & Fabri 2017 (*Brain* 140(5), 1231–1237) — **real-correct metadata, but the body's use was incomplete**. Verified at Europe PMC; full eight-author tuple matches; **DOI 10.1093/brain/aww358 recovered and added** (the entry previously carried none). Abstract states n = **two** patients and *"we replicate the standard finding that stimuli cannot be compared across visual half-fields"* — neither fact was in the article. Conclusion quoted into the body verbatim from the abstract: *"splits visual perception, but does not create two independent conscious perceivers within one brain."*
- Johansson, Hall, Sikström & Olsson 2005 (*Science* 310(5745), 116–119, doi:10.1126/science.1111709) — **real-correct metadata; body claim corrected.** OpenAlex confirms the tuple. (OpenAlex renders the second author as "Lars Häll"; the article's "Hall" is the correct form per the publisher PDF title page — an aggregator normalisation artefact, not a corpus defect.)
- Johansson, Hall, Sikström, Tärning & Lind 2006 (*Consciousness and Cognition* 15(4), 673–692) — **new entry, real-correct**, verified against the publisher PDF title page (five authors, Lund University Cognitive Science). Added as the locus of the detection-rate figure now quoted.
- Schechter & Bayne 2021 (Consciousness after split-brain surgery: The recent challenge to the classical picture, *Neuropsychologia* 160, 107987, doi:10.1016/j.neuropsychologia.2021.107987) — **new entry, real-correct** via OpenAlex. Matches the entry already carried by `topics/split-brain-consciousness` ref 10.
- Della Sala, Marchetti & Spinnler 1991 (Right-sided anarchic (alien) hand: a longitudinal study, *Neuropsychologia* 29(11), 1113–1127, doi:10.1016/0028-3932(91)90081-I) — **new entry, real-correct** via Europe PMC. Sources the previously-uncited too-hot-cup case.
- Southgate & Oquatre-six 2026 — Map self-cite; legitimate per [[fabricated-map-self-cite-pseudonym-false-alarm]]. Not stripped.

Superlative sweep: `find_superlative_claims` returned zero. Inline ↔ References cross-reference: complete in both directions after the additions.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Pinto 2017 was cited selectively, and the correction was one click away in the article's own flagship.** The article introduced Pinto as an "empirical crack" in the fragmentation premise without stating that the sample is two patients, without stating that the *same study replicates* the cross-field comparison failure, and without the standing objection that `topics/split-brain-consciousness` L78 already carries — Schechter and Bayne's (2021) argument that responding as a single organism establishes unity of *agency*, not unity of *experience*. The article's own sentence claimed it "cites this without over-claiming"; the material qualifiers were absent, so the claim about its own discipline was not yet earned.

This passes the §2 diagnostic test: a reviewer who fully accepts the Map's tenets would still flag it, because the Map's stated evidential rules require the qualifiers. It is a **cluster-inheritance failure**, the same shape as the one recorded in the 2026-08-04 `concepts/episodic-memory` pass — the cautious page and the unqualified page were one link apart, and the unqualified one is the concept page most likely to be read alone.

*Resolution applied*: the paragraph was split in two. The first now gives n = 2, the radiologically-confirmed-complete-transection detail, and Pinto's conclusion as a verbatim quotation. The second states the three qualifications explicitly — sample size, the replicated cross-field failure, and the Schechter and Bayne objection — and then draws the symmetry that makes the concession affordable: the agency/experience distinction has the *same shape* as the narration/phenomenal-unity distinction the article is built on, so it blocks the illusionist and the Map alike. What the Map wanted from Pinto (the fragmentation premise is live rather than settled) survives intact; what it never needed (Pinto as evidence *for* phenomenal unity) is explicitly disclaimed. Cross-link to `[[split-brain-consciousness|The flagship treatment]]` added at the point of dispute rather than only in Further Reading.

**2. A per-trial detection rate was restated as a per-participant one.** The body read "Most participants failed to notice the swap." The published figure is a rate per *manipulated trial*: verified verbatim at the publisher — *"Tallying across all the different conditions of the experiment, no more than 26% of all manipulation trials (M-trials) were exposed"* (Johansson, Hall, Sikström, Tärning & Lind 2006, restating the 2005 study). Participants each faced multiple manipulated trials, so a per-trial miss rate does not license a claim about how many participants noticed nothing across a session — and the error ran in the direction that strengthens the confabulation case, the congenial direction that survives ordinary review.

*Resolution applied*: replaced with the verified figure, the explicit unit ("a rate per manipulated trial rather than a count of participants who noticed nothing all session"), and a sentence locating the result's force where the paper actually puts it — in the confabulation that follows an *undetected* swap. The confabulation datum the article needs is unweakened; the restatement is now defensible.

**3. Family resolution — dropped co-author propagating from a research note.** `obsidian/research/voids-narrative-void-2026-02-25.md` L253 carried Johansson 2006 as four authors, dropping Lind, A., and truncating the subtitle. The publisher PDF title page reads *Petter Johansson, Lars Hall, Sverker Sikström, Betty Tärning, Andreas Lind*. Corrected in the research note per [[research-note-self-flagged-gaps-propagate-to-the-article]] — the note is where the variant would have entered the next article. `obsidian/research/voids-source-attribution-void-2026-04-21.md` L243 already carried the correct five-author form; no other locus in `obsidian/`, `archive/` or `hugo/content/` carries the truncated variant (grep on "Tärning" across all three trees).

### Medium Issues Found
- The anarchic-hand paragraph made a clinical claim (unbuttoning a shirt; lifting a too-hot cup) with no source in this article. Resolved: inline attribution to Della Sala, Marchetti and Spinnler (1991) plus a References entry. Verified against `topics/anarchic-hand-and-action-ownership` L48, which sources the same longitudinal case; the terminology is used correctly (anarchic hand — disowned *act*, ownership intact — not alien hand).
- Pinto entry lacked a DOI. Resolved.

### Reasoning-Mode Classification (§2.6, editor-internal)
- Engagement with Dennett/Gazzaniga illusionism: **Mixed (Mode Two + Mode Three)** — unchanged from 2026-07-16 and not re-litigated. Mode Two is the "arrives too late" argument; Mode Three is the declared under-determination.
- Engagement with Schechter and Bayne (new this pass): **not an opponent reply**. It is a concession absorbed from a *sympathetic* source, with the article stating which of its claims survives the concession and why. Deliberately not dressed as a refutation, and deliberately turned against the Map's own possible over-reading as well as the illusionist's.
- Label-leakage sweep: clean. No forbidden editor vocabulary in prose. The two existing links to `project/` discipline pages (`direct-refutation-discipline` aliased as "possibility-not-proof result", and a parenthetical `evidential-status-discipline`) are reference links to live public pages, not mode labels, and were left alone.

### Counterarguments Considered
- *The "already-conscious contents" premise begs the question against illusionism.* Marked bedrock at the framework boundary by the previous review; not re-flagged, per the convergence rule.
- *Adding Schechter and Bayne weakens the Map's position.* It does not: the objection is symmetric, and stating it is what makes the article's "without over-claiming" self-description true. Removing Pinto entirely would have been over-concession per [[over-concession-gets-ratified-not-merely-missed]] — the fragmentation premise is genuinely destabilised by the study, just not as far as the article implied.

## Optimistic Analysis Summary

### Strengths Preserved
- The confabulation/present-unity distinction and the "arrives too late" argument — untouched. This remains the article's core and it is precisely drawn.
- The front-loaded summary (lines 28–30), which survives standalone truncation.
- The four-way entailment ledger under "Disputed Implications", which keeps "follows from the data" separate from "follows only if strong illusionism is accepted". The Pinto repair was written to sit inside that discipline rather than beside it.
- The anarchic-hand mirror paragraph's actual argumentative move (authorship is computed and can fail in either direction, which is a claim about the signal and not yet about the subject) — kept verbatim; only its sourcing changed.

### Enhancements Made
- Pinto passage rebuilt with sample size, the replicated cross-field failure, a verbatim publisher quotation, and the Schechter and Bayne objection turned symmetrically against both sides.
- Choice-blindness statistic corrected to the published per-trial rate with its unit made explicit.
- Three verified references added; one DOI recovered.

### Cross-links Added
- [[split-brain-consciousness]] — now linked from the body at the point of the Pinto dispute, not only from Further Reading. (Article already carries thirteen inbound links from live content; graph integration was not a defect here.)

## Sibling Sweep (§2.4 step 6, extended to the empirical claim)

Critical issue 2 was not confined to the reviewed article. Grepping "choice blindness" across `obsidian/topics|concepts|voids|apex|positions` and `archive/` found **two further live loci** restating the same per-trial rate as a per-participant claim:

- `obsidian/topics/source-attribution-divergence.md` L81 — "the original study reports only that most participants failed to notice, and runs no individual-differences analysis."
- `obsidian/topics/introspection-architecture-independence-scoring.md` L87 — "most subjects accepted and justified the substitute."

Checked and **not** defective: `topics/pupillometry-behavioural-channel.md` L56 gets the unit right ("A substantial proportion of swaps go undetected in verbal report") and is the propagation template; `topics/authorship-of-action-divergence.md` and `topics/phenomenal-authority-and-first-person-evidence.md` state no rate at all.

These were not fixed in this pass — they are substantive articles with their own review histories, and the `source-attribution-divergence` sentence carries a second, correct point (the absence of an individual-differences analysis) that a careless repair would destroy. A P2 `refine-draft` task was minted instead, carrying the verified publisher quotation, the per-locus repair instruction, the correct exemplar to propagate, and an explicit do-not-fix list. Checked for task pileup first per [[outer-review-same-file-task-pileup]]: the only other open task on either file is an unrelated P3 cross-link item.

## Remaining Items

One minted P2 (the sibling sweep above). Word count 1937 → 2222 (+285), status `ok` at 89% of the `concepts/` 2500-word soft threshold — no length-neutral trading was required, and no existing argument was cut to make room.

## Stability Notes

- The bedrock item stands as recorded on 2026-07-16: whether the interpreter *constructs* phenomenal unity or *narrates over* an already-present one is a framework-boundary standoff the article itself declares under-determined. Future reviews should not re-flag "the physicalist finds the already-conscious premise question-begging" as critical.
- **New stability note.** Pinto 2017 is now fully qualified in this article (n = 2, cross-field failure replicated, Schechter and Bayne 2021 registered). Future reviews should not re-flag "over-reliance on Pinto" here, and should not resolve the agency-versus-experience question in either direction — the article's position is that the question is open and that the openness is symmetric. The general lesson is transferable rather than local: this defect was a *congenial* over-read, invisible to metadata review because every citation was real and correct. The lens that caught it was comparing the concept page's use of a source against the flagship sibling's use of the same source.
