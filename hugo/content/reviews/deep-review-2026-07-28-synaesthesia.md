---
ai_contribution: 100
ai_generated_date: 2026-07-28
ai_modified: 2026-07-28 21:07:22+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-28
date: &id001 2026-07-28
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[synaesthesia]]'
- '[[predictive-processing-and-dualism]]'
- '[[phenomenology-vs-function-axis]]'
- '[[phenomenal-variation-within-a-species]]'
title: Deep Review - Synaesthesia
topics: []
---

**Date**: 2026-07-28
**Article**: [Synaesthesia](/topics/synaesthesia/)
**Previous reviews**: [2026-07-08](/reviews/deep-review-2026-07-08-synaesthesia/), [2026-06-17](/reviews/deep-review-2026-06-17-synaesthesia/), [2026-06-02](/reviews/deep-review-2026-06-02-synaesthesia/), [2026-05-08](/reviews/deep-review-2026-05-08-synaesthesia/)
**Argument prose**: 2317 → 2380 words (+63); full body incl. Further Reading + References 3048 → 3111
**Length status**: `analyze_length` reports 3082 → 3145 words, "soft_warning" (103% of the 3000 topics/ soft threshold). **False over-length**: the metric counts the 24-entry References block and the 15-entry Further Reading list. Authored argument prose is 2380 — 79% of threshold, comfortably clear. No condensation warranted; do NOT mint a condense task on this signal.
**Outcome**: substantive — one internal-consistency defect fixed, one calibration overreach in `description` fixed, one style violation fixed, three new citations web-verified.

## Why This Article / Diff Classification

Fifth review, convergence-damped (score 18). Unlike the 2026-07-08 verification-only no-op, this pass had a genuine content delta: commit `016125e0d` (today, 17:27 UTC, refine-draft) added **The Predictive-Processing Account** — a new ~350-word section plus three new References entries (Seth 2014, van Leeuwen et al. 2021, Reeder et al. 2024) and the `[[predictive-processing-and-dualism]]` cross-link. The delta is a *concession*: the section grants that predictive processing supplies the finer-grain functionalist rejoinder and that "Gray's second dissociation fails at that grain." Review focus accordingly: (a) publisher-of-record verification of the three new cites, (b) whether the concession was propagated to the claims downstream of it.

## Citation Web-Verification (§2.4) — new cites only

The pre-existing 19 cites were web-verified real-correct across the 2026-05-08 / 06-02 / 06-17 / 07-08 passes and are byte-identical since; not re-litigated. The three cites added today were verified fresh at the publisher of record, metadata *and* empirical-claim fidelity:

| Citation | State |
|---|---|
| **Seth, A.K. (2014). A Predictive Processing Theory of Sensorimotor Contingencies… *Cognitive Neuroscience*, 5(2), 97–118, doi:10.1080/17588928.2013.877880** | **real-correct.** Verified at PMC4037840 (and DOI resolves to the T&F record). Every metadata field exact. Empirical-claim fidelity confirmed: the paper states verbatim that "synesthetic concurrents are hypothesized to be counterfactually *poor*" because "the hidden causes giving rise to concurrent–related sensory signals do not embed a rich and deep statistical structure," and that presence rests on "counterfactually-*rich* HGMs." The article's further claim that Seth reaches the simultaneous-occupancy puzzle is **not** a Map extension — Seth explicitly addresses coexistence: "inducers are not substituted by concurrents," synaesthetes "continue to hear music as well as tasting it." No source/Map conflation. |
| **van Leeuwen, T.M., Sauer, A., Jurjut, A.-M., Wibral, M., Uhlhaas, P.J., Singer, W., & Melloni, L. (2021). Perceptual Gains and Losses in Synesthesia and Schizophrenia. *Schizophrenia Bulletin*, 47(3), 722–730, doi:10.1093/schbul/sbaa162** | **real-correct.** Verified at OUP. All seven authors, order, volume/issue/pages exact. Empirical-claim fidelity confirmed: synaesthetes showed "lowered thresholds exclusively for synesthesia-inducing stimuli" and performed identically to controls on neutral symbols, attributed to high-precision implicit *long-term* priors. The article's "detection thresholds fall for degraded stimuli that induce their concurrents but not for neutral ones" is faithful, including the exclusivity. |
| **Reeder, R.R., Sala, G., & van Leeuwen, T.M. (2024). A Novel Model of Divergent Predictive Perception. *Neuroscience of Consciousness*, 2024(1), niae006, doi:10.1093/nc/niae006** | **real-correct.** Verified at OUP. Metadata exact. Empirical-claim fidelity confirmed on the load-bearing detail: the paper's own phrase is "strong, intermediate-level priors" — the article's "intermediate-level" is the source's word, not an interpolation (an aggregator summary that renders it "low-level" is the unreliable text here, not the article). Psychosis contrast faithful: synaesthesia has "both unusually strong perceptual priors and high confidence in sensory evidence, with intact reality monitoring," and "the critical factor that distinguishes between psychosis-like and synaesthesia-like divergent perception is sensory confidence." The imagery→projector/associator claim is likewise the paper's own prediction: "synaesthetes with vivid imagery will be more likely to experience concurrents as sensory." |

Note on paraphrase: the article's "strong, **inflexible** intermediate-level priors" adds *inflexible*, which is the Map's gloss (the paper's own qualifier is "maladaptive"). Unquoted paraphrase, defensible given the decades-long stability the same paragraph cites — recorded here so a future pass does not mistake it for a dropped or invented source term.

**Superlative/currency sweep**: `find_superlative_claims` returns empty; the new section makes no superlative or record claim. "The dominant computational framework in perception science" is a field-status characterisation, accurate for 2026.

**Inline ↔ References cross-check**: complete both directions, including the three new entries (20/21/22) and the renumbered self-cites (23/24). No orphans. Two 2014 entries involve Seth (Bor et al. 2014, Seth 2014) but the inline forms — "Bor et al. (2014)" vs "Seth (2014)" — disambiguate cleanly.

**Wikilinks**: all 30 distinct targets resolve against `obsidian/` + `archive/`. `[[predictive-processing-and-dualism]]` exists at `obsidian/topics/`.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Unpropagated concession (internal consistency).** Today's new section concedes that Gray's second dissociation "fails at that grain," but the immediately preceding paragraph still asserted synaesthesia as "the closest of the canonical cases to a strict instance of both Gray patterns at once" with no forward signal, and the **Relation to Site Perspective** section still characterised the rejoinder as merely "the standard finer-grain functionalist rejoinder" that the Map "flags" — stale wording, since the body now says in terms that the rejoinder "is no longer promissory." A reader truncating before the new section, or reading the tenet section alone, got the pre-concession article. **Fixed**: added a named-anchor forward reference (`[[#the-predictive-processing-account|…]] (below)`) to the wedge paragraph per the writing-style guide's forward-reference rule, and rewrote the tenet-section clause to state that the Map "does not treat that inference as secure," names the predictive-processing rejoinder as contesting the matching grain, and "lets it stand rather than arguing past it."

2. **Calibration overreach in `description` frontmatter.** The meta description billed the article as "single-species empirical **evidence for irreducible phenomenology**" — a stronger claim than the body supports post-concession, and in tension with the body's own explicit *constrains-not-establishes* discipline. This is the possibility/probability-slippage lens applied to the metadata channel (the description is what search and chat surfaces quote). **Fixed**: now "…and what it does and doesn't settle about functionalism." Side benefit: 166 → 155 chars, back inside the 150–160 spec.

### Medium Issues Found

3. **Style-guide violation — "load-bearing" as bare intensifier.** CLAUDE.md and the writing-style guide's "Overused Words and Constructions" section name this specifically. "A load-bearing concrete-phenomenon case" was pure emphasis, doing no structural work. **Fixed**: now "a concrete-phenomenon case." The surrounding calibration hedges (speculative-integration tier, Ramachandran & Hubbard granted, constrains-vs-establishes) were preserved verbatim.

4. **Duplicate Further Reading gloss.** Two entries carried near-identical "architecturally cleanest exemplar" glosses. **Fixed**: the axis entry now differentiates itself from the apex entry.

### Calibration Check (Possibility/Probability Slippage)

Body clean, and moving in the conservative direction. The new section's residue statement — "No current measurement discriminates the two, which leaves the disagreement at the framework boundary rather than settled against the computational account" — is correctly pitched: it declines to claim the hard-problem residue *refutes* predictive processing. The interface reading remains labelled speculative-integration tier. A tenet-accepting reviewer would not now flag any body claim as overstated; before this pass they would have flagged the `description`.

### Attribution Accuracy Check

All checks pass. Seth's, van Leeuwen's, and Reeder's positions are correctly presented as *physicalist* — the article states outright that "Seth and van Leeuwen build these models within physicalism and would reject the interface reading of them," which is the false-shared-commitment trap avoided explicitly. No qualifier drops, no "explores"→"argues" inflation, no source/Map conflation (Seth's coexistence claim verified as genuinely his, above).

### Reasoning-Mode Classification (Editor-Internal)

Named opponents: functionalism/representationalism (carried over) and now predictive processing.
- Functionalism: **Mixed (Mode One + Mode Three)**, unchanged — Mode One via functionalism's own parsimony commitment (joint-cluster absorption cost); Mode Three residue.
- Predictive processing: **Mode Three (framework-boundary marking)**, correctly executed. The article concedes the in-framework argument rather than manufacturing one, then marks the boundary honestly. No boundary-substitution — the concession is the opposite failure mode from the one the outer reviewers flagged.
- **No label leakage**: grep for the full forbidden-label set returns clean. "Framework boundary" appears as natural prose, which the discipline endorses.

### Internal-Quote / Cross-Reference Channel

The two claims the article makes *about* `[[predictive-processing-and-dualism]]` were grep-verified against that file's current text: "the Map adopts the mechanics without its originators' metaphysics" matches "The Map appropriates the architecture while rejecting its originators' physicalist metaphysics"; "the formalism's metaphysical neutrality… cuts in both directions" matches its "The Metaphysical Neutrality of the Mathematics" section and the Beni (2021) treatment. Both faithful.

## Optimistic Analysis Summary

### Strengths Preserved
Front-loaded lead; the extra-vs-missing pairing with aphantasia; the MacPherson conceptual-vocabulary caveat; the van Leeuwen semantic-mediation hedge woven into Wager's argument rather than bolted on; the joint-package framing that survives the concession intact ("unaffected in form — it never assumed functionalism had no reply"). The new section is genuinely strong work: it concedes without collapsing, and the four-way "reach is considerable" enumeration (consistency, semantic mediation, Bor's fade, projector–associator) is the most economical statement of PP's explanatory coverage of synaesthesia anywhere in the corpus.

### Enhancements Made
Four, all consistency/calibration/style repairs listed above. No content manufactured — the article is otherwise converged at five reviews.

### Cross-links
Full cluster present. One gap identified but deliberately left to a follow-up task: `[[predictive-processing-and-dualism]]` contains **zero** mentions of synaesthesia, so the new link is one-directional. Fixing that is a sibling-file edit, out of scope for single-document deep review.

## Remaining Items

Queued as a follow-up task (see `todo.md`): today's concession has corpus-wide reach that this single-file pass cannot discharge. Four sibling loci assert the "architecturally cleanest exemplar / strict instance of both Gray patterns" claim without the predictive-processing qualification:
- `obsidian/concepts/phenomenology-vs-function-axis.md:85`
- `obsidian/apex/phenomenal-variation-within-a-species.md:104`
- `obsidian/voids/synesthetic-void.md:129`
- `obsidian/apex/taxonomy-of-voids.md:130`

Plus the missing reciprocal link in `obsidian/topics/predictive-processing-and-dualism.md`.

## Stability Notes

Bedrock framework-boundary disagreements carried forward, NOT to be re-flagged as critical: eliminative-materialist/Dennettian deflation of the simultaneous-occupancy puzzle; cross-activation reductionism (explicitly granted as data-only-compatible); MWI objection to tenet alignment. **New**: the predictive-processing challenge is now *absorbed into the article as a concession*, not an open defect — do not re-flag "the article doesn't engage predictive processing" (resolved 2026-07-28) and do not re-flag "the wedge is overstated" (the wedge is now explicitly narrowed in-text).

Citation stability to preserve: Adam Wager (1999) *Philosophical Psychology* 12(3):263–281 (do not reintroduce "Alan / Philosophia / Southwest Philosophy Review"); Gray-2003 first dissociation = visual + auditory pipeline pair. **New, verified 2026-07-28**: Reeder et al. 2024 priors are **"intermediate-level"** — this is the paper's own term; do not "correct" it to "low-level" on the strength of a secondary summary. Seth 2014 is *Cognitive Neuroscience* 5(2):97–118 (not the 2015 *Cognitive Neuroscience* reply pieces), and his coexistence claim ("inducers are not substituted by concurrents") is genuinely his, not a Map interpolation.

Length stability: `analyze_length` will keep reporting soft_warning on this article because of its 24-entry References block. Authored argument prose is ~2380/3000. Do not mint condense tasks off the raw metric.