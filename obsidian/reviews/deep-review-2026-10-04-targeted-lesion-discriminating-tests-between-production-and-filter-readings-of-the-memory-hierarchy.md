---
title: "Deep Review - Targeted-Lesion Discriminating Tests (witness-mode cross-link, mPFC currency, Klein framing)"
created: 2026-10-04
modified: 2026-10-04
human_modified:
ai_modified: 2026-10-04T08:29:34+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy]]"
  - "[[brain-stimulation-and-the-witness-mode]]"
  - "[[memory-channel-interface-evidence]]"
  - "[[mine-ness]]"
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-04
last_curated:
---

**Date**: 2026-10-04
**Article**: [[targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy|Targeted-Lesion Discriminating Tests Between Production and Filter Readings of the Memory Hierarchy]]
**Previous review**: [[deep-review-2026-08-02-targeted-lesion-discriminating-tests|2026-08-02 — citation-framing sweep]] (5th pass; see also 2026-07-08, 2026-06-04, 2026-05-19)
**Mode**: Cycle slot, top candidate from `deep_review.py next` (score 79). The only content change since 08-02 was one clause added by the 2026-10-04 01:30Z brain-stimulation expand-topic to the precuneus/PCC paragraph. The pass ran four briefed lenses: that clause's fidelity, the 08-02 medial-PFC currency watch, the 08-02 Klein 2014 open item, and calibration and style. Per the 08-02 Stability Notes, citation metadata was not re-verified, and Bonnì placement, ATN/tFUS currency and Verhagen/Cain metadata were not re-flagged.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

- **Klein 2014 cited for the wrong phenomenon and the wrong patient class (lens 3; closes the 08-02 open item).** The H.M. section read: "Some retrograde-amnesia cases approximate this: patients who lose the *felt pastness* of remote memories while retaining their propositional content (Klein 2014)." OUP Academic returned HTTP 403, so the publisher-deposited abstracts were retrieved through OpenAlex. The book abstract says the evidence is "self-reports from case studies of individuals who suffer from a chronic or temporary loss of their sense of personal ownership of their mental states". The Chapter 5 abstract (*Empirical Evidence and the Ontological and Epistemological Selves*, doi:10.1093/acprof:oso/9780199349968.003.0005) names "patients suffering anosognosia, depersonalization, schizophrenic thought insertion" who "lose one's sense of personal ownership of one's mental states (e.g., the thought/memory is in my head, but it is not mine!)". So the book's cases concern lost **ownership**, not lost **pastness**, and they are not retrograde-amnesia cases. **Fix:** re-framed, not deleted. The cases now "approximate the finer probing: patients who find a thought or memory in their head but not theirs, its [[mine-ness|felt ownership]] lost and its content intact (Klein 2014)". The follow-on sentence moves from "autonoetic-without-pastness" to "content-without-ownership". The piped link adds zero words. **Scope of the claim:** two abstracts cannot show the book never discusses pastness. They do show what its case evidence is, and the article now claims only that. The cases are not lesion cases, so they are now said to approximate the second requirement (finer-grained probing), not the narrow-lesion requirement.

- **The 08-02 closer was false: "the pairings run from a demonstrated human focal target to one no current modality reaches" (lens 2).** The currency sweep found transcranial focused ultrasound aimed at the human **left anterior medial prefrontal cortex**, 11 sessions in 20 participants, in an open-label depression trial (Schachtner et al. 2025, *Frontiers in Psychiatry* 16, 1451828, NCT06320028). Its abstract says "future work including control arms is required", and a companion paper from the same trial (doi:10.3389/fpsyt.2025.1722575) is titled "an open-label pilot trial". A 2019 systematic review (Marques et al., *Braz J Psychiatry*, doi:10.1590/1516-4446-2019-0344) also covers six mPFC rTMS trials. The section's opening sentence, "Unlike the other two pairings, this one has no perturbation study to point to", was false in the same sense. The ATN comparator it relied on, Krishna 2023, is itself a non-memory perturbation trial. **Fix:** dropped the false contrast sentence. Added one cited sentence: "Focused ultrasound has since been aimed at anterior medial PFC, but in an open-label depression trial that did not probe memory (Schachtner et al. 2025)." The closer now reads "…to one never yet perturbed during memory testing", and "not because the perturbation technology can yet deliver all three. It cannot:" became "has delivered all three:", which removes a modal over-claim. The narrower negative still stands: no perturbation at this target has been paired with memory probing. **Shape:** the 08-02 negative was searched as TMS × mPFC × autobiographical memory, which cannot see a clinical tFUS trial that probes no memory. The closer then generalised that narrow negative into "no modality reaches".

- **Calibration error and internal contradiction: "cross-state convergence on the ordering is established" (lens 4).** In "Honouring the Evidential-Status Discipline", the article labelled the cross-state convergence "established", the top tier. Its own Tenet 5 paragraph calls the same convergence "accommodation-evidence-grade". The parent has also been repaired twice since this sentence was written: on 2026-08-08 the dissociative row became "the cleanest accommodation case and the most contested", and on 2026-09-19 (`e2762d7039`) the convergence became "not as five independent confirmations" and the ordering "stable wherever the substrate itself degrades". The parent labels both patterns "accommodation evidence". The diagnostic test applies: a tenet-accepting reviewer would still flag "established". **Fix:** the parenthetical now reads "channel-separability is established; the cross-state ordering is accommodation evidence". The repair never reached this dependent, which is the pattern of a repair not propagating to its dependents.

### Medium Issues Found (fixed)

- **Witness-mode cross-link sentence (lens 1): effect-implying adjective, and sham status not stated.** The clause read "suppressive ultrasound has since been aimed at the human PCC in sham-controlled studies of mindfulness rather than memory ([[brain-stimulation-and-the-witness-mode]])". Against the source article and its research note (`research/brain-stimulation-and-the-witness-mode-2026-10-03`), the parts were checked one at a time:
  - *"suppressive"*: the sources use it for the protocols' **design intent**. The article L47 says "one group has aimed suppressive protocols at the PCC". The note calls Ehmann's sessions and Lord 2026 "PCC-suppressive", and Lord 2025 proposes "PCC-suppressive stimulation". As a bare adjective in a paragraph about reachability, it read as an achieved effect. Now "ultrasound intended to suppress the human PCC".
  - *"sham-controlled studies" (plural)*: accurate for exactly two studies. Lord et al. 2024 is a published, randomised, single-blind pilot (15 active / 15 sham), and its active-vs-sham contrasts were **null** ("a single model that contrasted active and sham groups found no significant effects"; phenomenology also null). Lord et al. 2026 is a bioRxiv preprint, read from the abstract only (16 active / 8 sham), and reports a DMN–CEN decoupling. **Ehmann et al. 2025 is open-label** and must not be counted. The new wording ("mindfulness studies that probed no memory, with sham-controlled results so far null or preprint-only") covers Ehmann as a mindfulness study without crediting it with a sham arm, and states the sham record without implying an effect.
  - *"rather than memory"*: accurate. None of the three probed memory. Kept as "probed no memory".
  - Net: +3 words on the clause.

- **Editor-vocabulary coinages in article prose (lens 4).** "premature bedrock-marking" and "a foundational-move callout against an unsupported substrate-channel assumption" are discipline-page coinages. They belong to the class named in the writing-style guide under "No Exposed Internal Labels", and "callout" mirrors the listed `unsupported-jump callout`. Rewritten as "being declared bedrock prematurely" and "refutation on one reading's own terms or expose an unearned substrate-channel assumption". Length-neutral.

- **Redundant section closer.** "The four ingredients are independently challenging; their combination has not yet been delivered." repeated L48's "none of which … reliably supplies in combination" and the fourth ingredient's "has not yet been attempted". Cut (−14) to fund the corrections. Also cut the redundant "at the catalogue's current developmental stage" after "stage-appropriate" (−6), and tightened the ATN clause to "making the anterior nucleus a demonstrated human focal target" (−4). The meaning is unchanged, and the wording now matches the closer's phrase.

### Web-Verify Ledger (this pass)

- Schachtner, Dahill-Fuchel, Allen, et al. 2025 (*Frontiers in Psychiatry* 16, 1451828, doi:10.3389/fpsyt.2025.1451828): **newly added, real-correct** at Crossref (title, venue, volume, article number, 9 authors, issued 2025-04-04). Framing checked against the Europe PMC abstract: target "anterior medial prefrontal cortex"; no control arm; outcomes are depression, repetitive negative thought and quality of life, with no memory measure.
- Klein 2014 (*The Two Selves*, OUP): book confirmed at Crossref (monograph doi:10.1093/acprof:oso/9780199349968.001.0001, online 2013-11-20; print year 2014 kept, as in prior passes). **Framing defect fixed** (pastness/retrograde amnesia → ownership/self-report cases); verified against publisher-deposited book and chapter abstracts via OpenAlex.
- Lord et al. 2024, Lord et al. 2026, Ehmann et al. 2025: **not cited here**. They sit behind the cross-link, and their designs were read from the source article and research note (lens 1 above), not re-fetched.
- All other entries: metadata verified in prior passes; not re-litigated per 08-02 Stability Notes.
- **Result-direction leg:** Schachtner 2025 reports within-group symptom decreases, open-label, and the article cites it only for targeting and design, not efficacy. Lord 2024 is null between groups, which the new clause states.
- **Cited-author-stance leg:** Klein's book abstract holds that the subjective aspect of self may lack "material instantiation", a view close to the Map's, but the article uses the book only for the clinical dissociation, not for the Map's conclusion. Schachtner et al. are clinical neuromodulation researchers, cited for a design fact.

### Currency Watch (lens 2): medial-PFC perturbation with autobiographical-memory probing

- **WebSearch was not run.** The session's budget was exhausted (200/200). Substitutes, both with a working-control check:
  - PubMed E-utilities, title/abstract: (focused ultrasound OR deep TMS OR deep transcranial magnetic OR H-coil) × (medial prefrontal OR mPFC OR vmPFC) × (autobiographical OR episodic memory) returned **0 hits**.
  - Europe PMC, full text: adds TFUS, LIFU and H7, with "autobiographical". It returned 65 hits; the **top 50 by relevance were screened** and none is a perturbation study probing autobiographical memory at medial PFC. They are reviews, conference-abstract compilations, and clinical depression and OCD work.
  - Control: an Europe PMC query for precuneus × TMS × source memory, 2015, recovered Bonnì et al. 2015 as hit 1.
- **Verdict:** the watch's trigger (a depth-capable focal modality reaching medial PFC **with** autobiographical-memory probing) has not fired within that coverage. The 15 lowest-ranked Europe PMC hits were not screened, and sources outside PubMed and Europe PMC were not searched. A sweep that had not run would have stayed silent on this; this one also found that the modality now reaches the target, and that fact repaired the closer.

### Inline ↔ References Cross-Check

24 References entries: 21 external plus 3 Map self-citations linked by wikilink. Every inline author-year cite has an entry and every external entry is cited inline. **No orphans in either direction.**

### Attribution / Reasoning-Mode / Calibration Checks

- **Design-space tier unchanged:** "named-but-not-yet-tested". No experiment has delivered the discriminator. Every change this pass moves confidence down or holds it level.
- **Reasoning mode** (editor-internal): the production-vs-filter engagement is empirical underdetermination throughout, discharged honestly. No boundary-substitution.
- **Style:** no "This is not X. It is Y." constructions (regex sweep returned none); "load-bearing" occurs 0 times; no superlatives flagged by `find_superlative_claims`. The LLM-first lead states purpose and calibration in paragraph one and is unchanged.
- **Tenet 3 quantifier** (actual vs capacity reading): not engaged by this article (its Relation section covers Tenets 1, 2, 5) and **not settled here**; it is referred to the operator per the brief.

## Optimistic Analysis Summary

### Strengths Preserved
- The four-ingredient decomposition and "What the Existing Data Cannot Deliver". Only one redundant closer was removed.
- The three-pairing gradient. It is now more informative: a demonstrated focal ablation target (ATN), memory TMS plus mindfulness tFUS (precuneus/PCC), and a clinically reached target never perturbed during memory testing (medial PFC).
- The animal-model trade-off framing and the Relation to Site Perspective section, both untouched.

### Enhancements Made
- The medial-PFC pairing now carries a cited, current fact in place of a false negative.
- The Klein cases now link to the Map's [[mine-ness]] treatment of ownership, which places them in the autonoetic channel's internal structure, the frame [[clinical-dissociation-as-systematic-evidence]] uses for depersonalisation.
- The witness-mode reciprocal link now carries the sham record honestly.

### Cross-links Added
- [[mine-ness]] (piped, zero words).

## Length Check

Before: **3568** words (119% of 3000 topics soft; `analyze_length` counts the reference list). After: **3602** (120%). Net **+34**. About 22 words are the new Schachtner References entry, so prose is about +12. Cuts of 24 words (redundant closer −14, stage-redundancy −6, ATN tightening −4) funded about 36 words of corrections. Hard limit 4000 not approached.

## Remaining Items

- **Parent inconsistency, not edited here (out of scope), task minted.** In [[memory-channel-interface-evidence]], L88, after the 09-19 repair, says "The decoupling cases — ketamine, depersonalisation, DID — invert it [the ordering]". L118, from the same commit, says all five states "converge on the same ordering of channel vulnerability" and "The weight falls on the dissociative rows, which carry the ordering". Both cannot hold. The DID case as described in [[clinical-dissociation-as-systematic-evidence]] (cross-alter autonoetic access severed, semantic and procedural memory transferring) looks like the standard ordering, not an inversion. Only ketamine is an inversion on the parent's own table. **Driver correction (2026-10-04 08:50Z): this finding is stale and the task was withdrawn.** Commit `fb9b310675` (refine-draft, 2026-09-27) already repaired L88, which now reads "The ketamine row inverts it" and treats the dissociative rows as diagnostic of the ordering; `grep -c "decoupling cases"` on the live file is 0. The L88/L118 tension quoted above is the pre-09-27 text.
- **Research note stale against its article, no action.** `research/brain-stimulation-and-the-witness-mode-2026-10-03` says S19_137 had "no reported sham trial" (Findings 1, L112, L208, L297). The published article reports Vesuna et al. 2020 shams for him (11/13 vs one sham report). The article is the later, fuller reading, and research notes are not live content. [[brain-stimulation-and-the-witness-mode]] needs no fix for anything this lens checked.
- **Review-count blind spot.** `tools/curate/deep_review.py::_count_prior_reviews` suffix-matches the full article slug. The 07-08 and 08-02 reviews used the short slug `targeted-lesion-discriminating-tests`, so convergence damping counted 2 prior reviews, not 4. That is why this article was eligible inside the ≥3-reviews/14-day exclusion window. This review uses the full slug, so the count is now 3 and the exclusion will hold for 14 days. The two short-slug files were not renamed.

## Stability Notes

- **Klein 2014 framing is now verified and closed.** The book's case evidence is ownership loss, per the publisher abstracts. Do not restore "felt pastness" or "retrograde amnesia" to this cite. A future pass with full text may *add* a pastness case if the book has one, but must not re-derive the old framing from the parent's L69 "content vs manner" gloss.
- **Medial-PFC currency watch re-dated to 2026-10-04.** Live claim: depth-capable modalities reach human medial PFC (open-label clinical tFUS, Schachtner et al. 2025), but no perturbation there has been paired with memory testing. The trigger is unchanged: a sham-controlled or within-subject focal perturbation of medial PFC with autobiographical-memory probing. **Next check: re-run the full-text search including the 15 unscreened tail hits, and run one WebSearch when budget allows.**
- **Witness-mode clause closed.** It is calibrated to Lord 2024 (null), Lord 2026 (preprint, abstract) and Ehmann 2025 (open-label). Revisit only if Lord 2026 is published with full text, or a memory outcome is added to PCC tFUS.
- **"Mode Four" stays.** It names a defined category on the published, linked [[direct-refutation-discipline]] page in a methodology article, and four passes accepted it. It is not on the forbidden-label list. The unlinked coinages ("bedrock-marking", "callout") were the leak and are gone.
- **Calibration of the cross-state ordering is now pinned to the parent's "accommodation evidence".** If the parent's L88/L118 tension is resolved by dropping the dissociative rows from the ordering claim, this article's L44 ("the same ordering across the five clinical-state cases") should be re-checked against the result. (Driver note: the parent tension this conditional anticipates was resolved on 2026-09-27 in favour of keeping the dissociative rows in the ordering, so no re-check is pending.)
- **Bedrock (unchanged):** the production-vs-filter dispute is empirically underdetermined at the memory-hierarchy tier. That is the article's honest position, not a defect.
- **Previously closed, do not re-flag:** Bonnì placement (07-08), ATN/tFUS currency (07-08), Verhagen/Cain metadata (06-04), BBS page-range family (08-02), Lai & Siegel and Markowitsch framing (08-02), Snowden priority (08-02).
