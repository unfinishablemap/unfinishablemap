---
title: "Deep Review - Vestibular Consciousness and the Interface"
created: 2026-09-20
modified: 2026-09-20
human_modified: null
ai_modified: 2026-09-20T09:35:00+00:00
draft: false
description: "Third deep review of the vestibular spoke: the first to re-run the publisher-of-record citation pass after two metadata-only ledgers, finding three result-direction defects that intra-corpus consistency had ratified."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-20
last_curated: null
last_deep_review: null
---

**Date**: 2026-09-20
**Article**: [[vestibular-consciousness-and-the-interface|Vestibular Consciousness and the Interface]]
**Previous reviews**: [[deep-review-2026-07-07-vestibular-consciousness-and-the-interface|2026-07-07]], [[deep-review-2026-06-22-vestibular-consciousness-and-the-interface|2026-06-22]]

## Summary

**Third deep review. Three critical citation/result-direction defects found and fixed — the first non-no-op pass on this article.** Both prior deep reviews were no-op convergence passes, and both closed the §2.4 web-verify step by reference rather than by re-running it: 2026-06-22 certified all seven external cites `real-correct`, and 2026-07-07 explicitly declined to re-run on the grounds that the body had not changed. The 2026-09-20 08:38 refine-draft pass changed the body, so the trigger fired. Re-running it at the publisher of record found that the 2026-06-22 ledger had certified **metadata**, and that three of the seven cites carry a **result-direction or claim-strength** error that metadata verification cannot see. This is the pattern the corpus keeps paying for: intra-corpus consistency *ratifies* a wrong reading rather than catching it.

Word count 3094 → **3179** (+85). Topics section, soft 3000 / hard 4000 → `soft_warning`, headroom 820. Comfortably inside the driver's 905-word budget.

**Lenses run this pass** (named so an unrun lens is visible rather than implied clean): publisher-of-record citation web-verify (all 9 References entries, all inline cites); verbatim-quote fidelity by `grep -F` against NFKC-normalised raw source; result-direction / null-result leg; cited-author-stance leg; inline ↔ References cross-reference; corpus family-resolution sweep; calibration / possibility-probability slippage; editor-vocabulary label-leakage grep; over-concession tell grep; banned-construct grep; length; both-tree sync verification. **Lenses NOT run**: a fresh six-persona adversarial sweep beyond the calibration and attribution legs (both prior reviews ran it to a clean result and recorded stability notes; re-running it would have oscillated), and cross-link/integration analysis (covered five hours earlier by `reviews/optimistic-2026-09-20-cross-modal-capability-division-wing.md`).

## Verdict on the 45-minute-old insertion (08:38, commit `6333e926`)

**Sound. No changes made to it.** Three checks:

1. **Fidelity to its source.** The inserted paragraph restates the apex's own common-cause finding. Compared against `apex/cross-modal-capability-division` L100 verbatim: the apex has "the vestibular signal *is* multisensory integration, with no separate channel to converge from beyond the temporo-parietal hub it shares with vision, touch, and proprioception" and "extending what the asymmetry *means* without adding to how strongly it is confirmed". The insertion reproduces both clauses accurately. No drift in the internal quote channel.
2. **Link path.** The insertion used `[[project/common-cause-null|…]]`, which resolves — `obsidian/project/common-cause-null.md` exists and renders at `/project/common-cause-null/` (confirmed in the Hugo tree). Note that the optimistic wing review that commissioned this fix named the target as `concepts/common-cause-null`, which does **not** exist; a path-qualified wikilink is string-built by the resolver and is never membership-validated, so taking the review's path literally would have shipped a **silent 404**. The refine pass corrected it. Worth recording as a near-miss.
3. **The +0 register citation and the "adds" → "supplies" swap** at L98 are both correct and both word-neutral.

The one thing the 08:38 pass did *not* do is look past its own single target word. It swapped the evidential "adds" at L98 and stopped; the same over-strong register survived at L88 ("The depersonalization findings **show** that…"), which this pass has now downgraded to "indicate" at +0 words. Flagged not as a criticism of that pass but as the expected shape of a single-word fix.

## Pessimistic Analysis Summary

### Critical Issues Found — and fixed

1. **Lopez, Lenggenhager & Blanke 2010 over-attributed and its qualifier dropped** (§When the Frame Fails). The article read "**Galvanic and caloric** vestibular stimulation modulate the rubber-hand illusion and illusory hand ownership". The paper tested **galvanic stimulation only** — the abstract states "we investigated whether galvanic vestibular stimulation (GVS) interferes with the mechanisms underlying ownership, touch, and the localization of one's own hand … by using the 'rubber hand illusion' paradigm" — and its result is polarity- and side-specific: "**only left anodal GVS**" increased illusory ownership of the fake hand and illusory location of touch. Caloric stimulation enters that paper only as reviewed prior work on neurological patients, a different phenomenon (somatoparaphrenic disownership) under a different citation. **Fixed**: the sentence now names galvanic stimulation alone and carries the left-anodal qualifier and the actual reported outcome. The follow-on sentence's "which hand feels like one's own" — which read as *which of two real hands* — was tightened to "whether a seen hand feels like one's own".

2. **Cento et al. 2026 upgraded from guarded association to causal claim** (§When the Frame Fails). The article read "A systematic review **finds that** vestibular disorders **trigger or exacerbate** depersonalization and derealization", and then stated a mediation mechanism — "spatial disorientation and the anxiety it provokes **mediate** the slide into depersonalization symptoms" — that the review does not claim. The publisher abstract's own conclusion is "vestibular alterations **may contribute to** the emergence of DD symptoms", explicitly bounded by "substantial heterogeneity in the studied populations, experimental paradigms, and assessment methodologies **limits clear conclusions**"; anxiety and spatial disorientation are reported as **co-occurring** in 82.61% of studies, "suggesting an interaction", not as mediators. The review's own proposed framework is that "vestibular alterations disrupt multisensory integration in parietotemporal, insular, and hippocampal regions". **Fixed**: the passage now reports what the review measured (23 studies, DD symptoms in 86.9%, co-occurrence in 82.61%), quotes its guarded conclusion, substitutes the review's actual neurofunctional framework for the invented mediation mechanism, and carries its heterogeneity caveat. The downstream sentence at L88 was softened from "show" to "indicate" so the conclusion does not outrun the repaired premise.

3. **Laurens & Droulez 2007's prior mislocated** (§The Strongest Rival). The article read "the brain … infer[s] the most probable cause given **a prior encoding Earth's gravity**". In the L&D model, gravity is not the prior — the priors favour low motion, and gravity is a fixed constant in the internal model. The paper's own abstract: the processing "is related to the statistics of natural head movements. This would create a perceptual bias in favour of **low velocity and acceleration**." An OA re-implementation working directly from L&D's notation (Irmak, Pool, Happee et al. 2023, *Exp. Brain Res.*, PMC10258185, §"Particle filter model") is explicit on both halves: "the magnitude of gravity |G| … is earth referenced and **assumed** … to be constant at −9.81 ms⁻²", while "the particles that are **closest to zero acceleration and angular velocity** are weighted the highest". **Fixed**: the sentence now states the low-motion priors and derives the gravity attribution as their consequence — "an ambiguous otolith signal defaults to gravity rather than to self-motion". The string sibling four paragraphs later ("the Bayesian-inference account predicts the silence, **the gravity prior**") was corrected in the same pass to "the gravity default", +0 words — a fix-by-file that left this sibling live would have been a half-fix.

### Medium Issues Found — and fixed

- **The twice-deferred uncited motor-prediction claim** (§Relation to Site Perspective, Bidirectional Interaction). Both prior reviews flagged it and both deferred it, 2026-06-22 explicitly leaving it "for a future pass only if a publisher-verified efference-copy/self-motion source is added to the corpus pool". Such a source now exists and was verified OA at the publisher this pass: **Laurens & Angelaki 2017**, "A unified internal model theory to resolve the paradox of active versus passive self-motion sensation", *eLife* 6:e28074 (PMID 29043978, PMC5839740), whose full text was fetched and grepped. **Fixed**: the claim is now cited. The wording was also corrected in the same edit — the article said active and passive motion "are **estimated** differently", which runs against the cited paper's *unified* thesis (the estimation machinery is the same; what differs is that predicted consequences are subtracted, so only mismatches drive the vestibular pathways). It now reads "which is why active and passive motion **drive vestibular pathways** so differently".

- **Cento References entry incomplete.** Volume, issue and pages were missing. Verified at Crossref and PubMed: *Journal of Vestibular Research*, **36(5), 326–351**. Added in place; the References list uses `1.` markdown auto-numbering throughout, so inserting the new Laurens & Angelaki entry renumbered nothing.

### Counterarguments Considered

Nothing new. Both prior reviews' bedrock findings were re-read before starting and are not re-litigated: the physicalist rejection of the "felt point of view" residue, and the oblique quantum/MWI objections, remain framework-boundary standoffs. The optimistic wing review's two **cleared** suspicions (the spoke does not conscript its naturalist sources; the thermal sibling does not over-read the thermal grill) were likewise not re-raised — I independently confirmed the first in passing while running the cited-author-stance leg, and it holds.

## Citation Web-Verify Ledger (Publisher of Record)

Nine References entries: seven external, two house self-citations. Every external cite re-verified this pass at the publisher of record, not at an aggregator; every verbatim quote grepped with `grep -F` against NFKC-normalised raw source with printed counts; a control query was run on each artefact before any absence was recorded.

- **de Vignemont, F. 2024** (*Bodily Awareness*, SEP) — state: **real-correct**. Fetched the live canonical entry (HTTP 200, 123,754 bytes; header "First published Tue Aug 9, 2011; **substantive revision Fri Sep 20, 2024**" — the 2024 year is right). Control grep "bodily awareness" → present. All four quoted strings grep-verified verbatim, each as its own fixed-string key, 1 occurrence each: "Besides cases of dizziness, there seems to be indeed a paucity of vestibular experiences in normal consciousness"; "sensitive to motion acceleration as our head moves in space"; "sensitive to the pull of gravity"; "Which way is up?" / "Where am I heading?". The surrounding SEP paragraph was read in full to confirm no splice and no over-read. Note for future reviewers: "vestibular" occurs **3 times in the whole entry**, all inside one paragraph — this is a one-paragraph source carrying four of the article's quotations, which is a thin but honest base, and the article does not claim more from it than it says.
- **Pfeiffer, C., Serino, A. & Blanke, O. 2014** (*Front. Integr. Neurosci.* 8:31) — state: **real-correct**. Crossref confirms title, all three authors in order, journal and volume 8, issued 2014-04-17. Full text via Europe PMC (PMC4028995, 178KB XML). Control grep "vestibular" → 215 hits. All three quoted strings verbatim, 1 occurrence each, with surrounding context read: the "no such unisensory vestibular cortex" quote, the distributed-network definition, and "what we call spatial aspects of bodily self-consciousness, i.e., self-location and first-person perspective". The last is correctly glossed by the article as the review's focus — the source sentence is "This review will mainly focus on…".
- **Blanke, O. & Arzy, S. 2005** (*The Neuroscientist* 11(1):16–24) — state: **real-correct**. PubMed 15632275 confirms title, both authors, journal, 11(1), 16-24, 2005. Abstract confirms the article's stance attribution: "OBEs are related to a failure to integrate multisensory information from one's own body at the temporo-parietal junction (TPJ)", producing "illusory self-location, illusory perspective". The article's finer claim about the vestibular/visual disintegration specifically is **consistent with, but not verifiable in, the abstract** — the paper is paywalled (unpaywall lists only an EPFL Infoscience record, whose PDF I could not retrieve). Recording this honestly as *genuine but not fully grep-verifiable at this depth* rather than claiming a verification I did not perform.
- **Lopez, C., Lenggenhager, B. & Blanke, O. 2010** (*Conscious. Cogn.* 19(1):33–47) — state: **real-wrong-usage → corrected**. PubMed 20047844 confirms all metadata exactly as cited (this is why two metadata ledgers passed it). The defect is in the *use*: galvanic-only, left-anodal-only. See Critical Issue 1. Not OA in Europe PMC; the publisher abstract is decisive on what was tested.
- **Laurens, J. & Droulez, J. 2007** (*Biol. Cybern.* 96(4):389–404) — state: **real-wrong-usage → corrected**. PubMed 17146661 confirms all metadata exactly as cited; page range independently corroborated by a third-party reference list. Not OA (unpaywall `is_oa: false`; Semantic Scholar `status: CLOSED`; no HAL deposit; Google Books returns no volume). The prior mislocation (Critical Issue 3) therefore rests on the publisher abstract plus an OA re-implementation of the same model, both quoted above — sufficient to correct, and the correction is stated conservatively.
- **Laurens, J. & Angelaki, D. E. 2017** (*eLife* 6:e28074) — state: **real-correct, newly added**. Europe PMC PMC5839740, PMID 29043978, DOI 10.7554/elife.28074. Full text fetched and grepped: "motor commands" 77 hits, "active and passive" 54, "efference copy" 10. The eLife digest states the thesis the article now cites it for: "the brain predicts in advance how each movement will affect the vestibular organs … Only mismatches between the two activate the brain's vestibular regions."
- **Cento, S., Gammeri, R., Zavattaro, C., Cirillo, E., Serra, H. & Ricci, R. 2026** (*J. Vestib. Res.*) — state: **real-wrong-usage + incomplete metadata → both corrected**. Crossref and PubMed (41499789) confirm the title and all six author surnames in the cited order, and supply the missing 36(5), 326–351. Claim-strength defect at Critical Issue 2.
- **Southgate & Oquatre-huit (2026-06-16, 2026-06-20)** — house self-citation byline convention, flagged as deliberate by both prior reviews; dates match the sibling articles' `created` fields. No action.

**Inline ↔ References cross-reference**: no orphans in either direction before or after the edit; the one added References entry has a matching inline cite, and the inline cite has a matching entry.

**Empirical-record currency sweep**: no superlative claims. The one "so far" in the lead is an internal Map-survey phrase, not an empirical-record superlative — same finding as 2026-06-22 and 2026-07-07.

**Cited-author-stance leg**: clean, and unusually well done. Every one of the eight named empirical authors is declared a non-ally twice, once in §The Strongest Rival ("None of them is an ally of the interface reading, and none is enlisted as one here") and once in §Relation to Site Perspective. Laurens & Angelaki 2017, added this pass, falls inside the Laurens/Droulez naming already present at both loci, so the firewall covers it without a new sentence. No conscription.

**Family resolution (§2.4 step 6)**: all three defects are inherited by `apex/cross-modal-capability-division`, which reuses this article's seven cites verbatim. A fixed-string corpus sweep of `obsidian/` and `archive/` found the defects in **exactly two live files** — this spoke and that apex; every other `caloric` hit in the corpus is the heat-substance caloric of the eliminativist and parsimony articles, and every other `Lopez` hit is a different Lopez (A. Lopez on IIT and on split-brain unity). The apex is **out of this pass's edit scope by driver instruction** — it is 6 words past its hard gate and a separate finding covers it — so a **P1 refine-draft task** was minted against it carrying the full per-defect evidence and word-neutral fixes, so the fix does not require re-verification.

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)

- The two-axis reframing of the apex asymmetry — vestibular as faint-object *yet* foundational-frame — which the apex adopts and the positions register encodes as "object-unity, owned affect, viewpoint-frame". Untouched.
- The inverted explanatory-gap register: choosing the modality with the least phenomenology to press the phenomenological question. Untouched.
- The co-optation firewall, which is exemplary and which survived the stance leg intact.
- The refusal to adjudicate the faint-phenomenology dispute, and the honestly-held-open had-versus-constitutive question. Untouched.

### Enhancements Made

Beyond the three critical repairs: one twice-deferred medium issue discharged with a publisher-verified OA source, and one incomplete reference entry completed. The Cento repair is a net *gain* in substance as well as accuracy — the passage now carries the review's actual numbers (23 studies, 86.9%, 82.61%) where it previously carried a mechanism nobody had published.

### Cross-links Added

None. Integration and cross-linking across this wing were reviewed five hours earlier by the optimistic wing pass, which made its recommendations and had one of them executed at 08:38. Adding more here would duplicate that work and spend budget the citation repairs needed.

## Remaining Items

- `apex/cross-modal-capability-division` carries all three defects; **P1 refine-draft task minted** with the full ledger. It is at `hard_warning` with −6 headroom, so all three fixes were specified word-neutral or subtractive.
- Blanke & Arzy 2005's vestibular-specific disintegration claim is consistent with the abstract but not grep-verifiable without the paywalled full text. Low priority; the stance attribution is not in doubt.

## Stability Notes

- ⚠️ **Do not read the two prior "converged, no-op" reviews as certifying the citations.** They certified metadata. Three of seven cites were wrong in *use* the whole time — wrong stimulation modality, wrong prior, wrong claim strength — and each was re-ratified by the next pass reading the previous ledger. **A `real-correct` ledger line discharges the metadata leg only.** The result-direction leg is per-pass and was run for the first time on 2026-09-20.
- **Convergence claims on this article should now be re-dated.** The "five agreeing creation-day passes" and the two no-op deep reviews agreed on an article that contained three citation defects. This is not an argument for oscillating the prose — the argument, structure and calibration really are stable, and none of them changed this pass — but it is an argument that "converged" meant "no unrun lens had been run", exactly the pattern the convergence-damping note warns about.
- **Bedrock disagreements (do NOT re-flag as critical)**, carried forward unchanged from 2026-06-22 and 2026-07-07: the eliminative-materialist / physicalist rejection of the "felt point of view" residue; the oblique quantum-skeptic and Many-Worlds objections, which the article disclaims explicitly.
- **Calibration is honest throughout and is now *more* honest**, not less. The three repairs all move claims *down* the evidential scale toward what the sources say. No possibility/probability slippage was found; the article's tenet paragraphs continue to disclaim rather than upgrade. Per the recorded corpus base rate, a lexical hedge-word count is not evidence of anchoring on this article and was not run as one.
- **The `concepts/common-cause-null` path is wrong; `project/common-cause-null` is right.** Recorded because a review file in this same wing names the wrong one, and a path-qualified wikilink fails silently.
