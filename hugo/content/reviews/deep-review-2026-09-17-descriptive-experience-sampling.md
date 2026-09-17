---
ai_contribution: 100
ai_generated_date: 2026-09-17
ai_modified: 2026-09-17 17:58:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-17
date: &id001 2026-09-17
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-17 17:58:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Descriptive Experience Sampling
topics: []
---

**Date**: 2026-09-17
**Article**: [Descriptive Experience Sampling](/concepts/descriptive-experience-sampling/)
**Previous review**: [2026-08-16](/reviews/deep-review-2026-08-16-descriptive-experience-sampling/)
**Word count**: 2780 → 2895 (+115; soft_warning, 604 below hard 3500)

## Selection Note

The only change to this article since the 2026-08-16 deep review was a **single Further Reading cross-link** installed by a refine-draft pass on 2026-09-09 (`dd92a20b73`). This is the cosmetic-bump-re-qualifies-a-converged-article pattern the convergence damping exists to catch; the article has only one prior review, so damping did not exclude it.

The prior review ran an unusually complete publisher-of-record ledger, and the References block is byte-identical since. Per §2.4's own trigger ("the body or References block was modified since the last deep-review"), the full re-verify was **not** re-run. Instead this pass ran the lenses the prior review could not or did not: the unreviewed cross-link sentence, cross-article reciprocity, and a **raw-source grep** of the quotes the prior ledger certified from summarised/abstract text.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Attribution error in the 2026-09-09 cross-link: a two-member "instrument class" the cited synthesis does not declare.** The installed line read *"[phenomenal-contrast-method](/concepts/phenomenal-contrast-method/) — the sibling within-subject instrument: it grounds structure premises where sampling grounds frequency ones, and both are defensible against cross-subject phenomenal calibration rather than against each other"*, and its commit message asserted the two articles "are the two members of the within-subject instrument class the judging-the-map apex declares defensible."

  Measured against the source: `obsidian/apex/judging-the-map-as-science.md` contains **zero** occurrences of "descriptive experience sampling", "descriptive-experience-sampling", "Hurlburt", or "sampling" (all four greps return 0). DES is not in its `apex_sources` list. The apex's actual claim, at its decisions section, is *"within-subject contrast structures are the defensible instrument class; cross-subject phenomenal calibration claims are red flags whoever makes them"*, and its Further Reading names `[[phenomenal-contrast-method]] — the within-subject instrument class` **alone**. The class is defined by contrast structure, and the apex never extends it.

  This is a §2.5 misattribution — a claim attributed to a source that does not make it — not a philosophical disagreement. It is also a **source/Map conflation**: the Map's own (defensible) extension was presented as the synthesis's finding. Aggravating factor: the same sentence class-labels DES "within-subject" while the article's own limits register lists **"Population generalisation"** among what DES *cannot* establish and notes the canonical result "rests on thirty stratified college students" — i.e. the headline frequencies are cross-participant aggregates.

  **Resolution**: rewritten in both articles to (a) name the synthesis's class as *contrast structure, not DES*, (b) mark the extension to DES as the Map's own step, and (c) scope it to DES's *within-participant frequency profiles*, explicitly excluding the cross-participant percentages. What survives untouched: the link itself is a real and useful connection, the frequency/structure division of labour is correct, and the reciprocal pairing was the right instinct — only the attribution and the scope were wrong.

### Medium Issues Found

- **The scanner triangulation is reported without noting it forfeits the method's own pristine condition.** §method states pristine experience requires "random cueing in the participant's natural environment rather than a laboratory task"; §findings then presents Kühn et al. (2014) — conducted in 25-minute MRI sessions — as the one external triangulation, with no acknowledgement of the conflict. The paper's authors flag the cost themselves, and the article omitted it. **Resolution**: one paragraph added, sourced verbatim from the raw full text, recording that inner seeing filled eight in-scanner samples having *never* appeared in this participant's natural-environment sampling and is judged "likely to be an artifact of the scanner situation" — framed as a constraint on the neuroimaging route generally, not a flaw in the study.

- **The imaging contrast's actual base was unstated.** The article gave "thirty-six sampled moments" but not how many carried the phenomenon the contrast was computed over. **Resolution**: "eight of which the interview classified as inner speaking" added (+8 words), making the existing, already-good caution concrete rather than rhetorical.

### Checked and NOT changed

- **Orphan reference entries** (six). The 2026-08-16 review recorded keeping these as a deliberate convention for a method reference page. Re-litigating would be oscillation. Unchanged.
- **Hurlburt 1990 publisher** ("Springer US" vs CV's "Plenum Press"). Prior review found both defensible. Unchanged.
- **The full citation ledger.** References block unmodified since a complete publisher-of-record pass; §2.4 trigger not met. Not re-run, by rule rather than by omission.

## Raw-Source Quote Grep (the lens the prior ledger could not run)

Memory discipline: *a quotation certified without a grep of the raw source is uncertified.* Kühn et al. 2014 is open access (PMC4260673); full text pulled from the Europe PMC REST API, tag-stripped and **NFKC-normalised** before matching (ligature/diacritic splitter guard). Every figure the article stakes its calibration on verifies **verbatim**:

- "does not set out to inquire whether a participant is innerly speaking, or is innerly seeing, or so on" — **verbatim at offset 10345**. Confirms the attribution to Kühn et al. as the describing source, and the paper in turn credits the term to Hurlburt & Heavey 2006, so the article's "(Kühn et al. 2014, describing the procedure)" hedge is exactly right.
- "open-beginninged" — **verbatim** (hyphenated; the unhyphenated variant returns −1, a live false-zero trap).
- Five recruited / **one** reported: *"we only report here on one of those participants, 'Lara,' an 18 year-old-woman"* — verbatim. (Note "eighteen"/"18-year-old" both return −1 against the raw spelling "18 year-old-woman"; the figure is right, the spelling differs.)
- Nine sessions, thirty-six moments: *"repeated a total of nine times, resulting in 4 × 9 = 36 random samples of experience occurring in 25 × 9 = 225 min of fMRI scanning"* — verbatim.
- Left IFG: *"activation in classic speech processing areas including left inferior frontal gyrus"* — verbatim.
- The validity overclaim the article refuses: *"These results highlight the precision and validity of the DES method"* — **verbatim in the abstract**. The article's decision to quote the proof-of-principle framing and decline the validity claim is correct on the source's own words.
- Inner speaking base: *"Inner speaking occurred in 8 (22%) of Lara's 36 in-scanner samples"* — verbatim (new to the article this pass).
- Scanner artifact: *"inner seeing had never occurred in Lara's natural environment DES sampling, so it seemed likely to be an artifact of the scanner situation"* — verbatim (new to the article this pass).

**Result-direction leg**: no inversions found. **Cited-author-stance leg**: unchanged and correct — the article states Hurlburt's programme has "no stated metaphysics of mind" and must "never be enlisted as though it argued for one".

⚠️ Caution for the next reviewer: inner *seeing* and inner *speaking* each occurred in exactly 8 (22%) of the 36 samples. The two 8s are genuinely distinct findings, not a duplication error.

## Link Integrity

- All fifteen wikilink targets resolve (checked against `obsidian/` excluding `reviews/`).
- New link `[[judging-the-map-as-science]]` uses the **bare** form: the slug is unique corpus-wide, so the bare target is validated at sync (a bad path-qualified target 404s silently).
- **Reciprocity confirmed and repaired symmetrically.** `phenomenal-contrast-method.md:137` carried the mirror image of the same misattribution ("the other member of that instrument class"). Fixed in the same pass — a fix-by-file would have left the string sibling live.

## Reasoning-Mode Classification (§2.6, editor-internal)

- **Dennett / heterophenomenology**: Mode Three, unchanged. The article still concedes DES cannot adjudicate realist versus deflationary readings of its own transcripts.
- **Schwitzgebel**: Mode Three, unchanged and still well executed.
- **The psychometric tradition**: Mode Two, unchanged.
- No new engagements introduced; no editor-vocabulary leakage in either edited article.

## Optimistic Analysis Summary

### Strengths Preserved

- The lead's Hurlburt quotation and the pluralism landing point installed by the prior review — untouched, as its stability note directs.
- The Kühn calibration. This pass **strengthened** rather than softened it: the new sample-base figure and the scanner-artifact paragraph both cut in the article's own sceptical direction, which is the Hardline Empiricist's preferred outcome.
- "Its own fidelity — the bracketing claim is a claim." Untouched.
- The Relation to Site Perspective refusal to enlist Hurlburt for dualism. Untouched.

### Enhancements Made

- Three: the sample-base figure, the scanner/pristine paragraph, and the corrected cross-link pair.

### Cross-links Added

None new. The existing `[[phenomenal-contrast-method]]` pair was corrected in place.

## Length

Length-neutral mode (2780 ≥ soft 2500). Additions were offset by two trims: the iterative-skill paragraph merged, and a redundant clause in §fidelity-validity ("rather than as a point local to the dispute that occasioned it") whose work is already done by the later, sharper "The generalisation is the Map's, not Hurlburt's". `git log -S` confirmed the trimmed clause was original-create text, not review-installed — no live refutation stranded. Net +115 measured, leaving 604 words of headroom below hard.

## Remaining Items

None requiring a follow-up task.

## Stability Notes

Carried forward from 2026-08-16 and still in force:

- The **realist-versus-deflationary reading of DES transcripts** is bedrock. Do not re-flag.
- **Schwitzgebel's introspective pessimism** is bedrock; the deliberate asymmetry (adopt his scepticism, disclaim his agreement) is intentional.
- The Map's "most disciplined available way" judgement survives the pluralism finding; the corrected lead does not license a downgrade.

Added this pass:

- **The DES ↔ phenomenal-contrast-method pairing is the Map's own extension of the judging-the-map synthesis, not a finding of it.** This scope marker is load-bearing and was installed to correct a live misattribution. A future pass that shortens either Further Reading line must keep the "the synthesis names contrast structure alone / this is the Map's own step" qualifier, or the attribution error returns. Per §2.6's stability-note scope rule, this note exempts nothing empirical — it fences an attribution, which is exactly what stability notes may fence.
- **The citation ledger is certified as of 2026-08-16 and re-certified for Kühn et al. 2014 against raw full text as of 2026-09-17.** If the References block changes, §2.4 re-triggers in full; a cosmetic body edit alone does not.