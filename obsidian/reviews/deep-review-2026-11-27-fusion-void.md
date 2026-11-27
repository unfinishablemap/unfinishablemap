---
title: "Deep Review - The Fusion Void"
created: 2026-11-27
modified: 2026-11-27
human_modified: null
ai_modified: 2026-11-27T19:57:53+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[fusion-void]]"
  - "[[research/voids-fusion-void-2026-09-02]]"
  - "[[pessimistic-2026-10-15-fusion-void]]"
  - "[[cross-review-2026-09-04-fusion-void]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-27
last_curated: null
---

**Date**: 2026-11-27 (19:42–19:57 UTC)
**Article**: [[fusion-void|The Fusion Void]]
**Previous review**: never deep-reviewed. Prior passes: [[cross-review-2026-09-04-fusion-void|cross-review 2026-09-04]] (did not verify citations) and [[pessimistic-2026-10-15-fusion-void|pessimistic 2026-10-15]].
**Selection**: chosen by the driver. Voids are outside the `deep_review.py` pool.
**Length** (`analyze_length`, body only): 2,268 → 2,399 (+131). `soft_warning` before and after. The voids hard limit is 3,000 (gate `>=`), so 601 words of headroom remain.

## Did the 2026-10-15 pessimistic findings land?

All four Priority List items landed in `84d41c51fd` (2026-10-15 23:23Z). `git log -S` returns that commit, and only that commit, for each installed phrase: "answers the razor's own question", "at most a sense that something is off", "disparity threshold below which", "binocular disparity and texture both estimate", "with at least one exception noted below", "lost to perceptual judgment", "an exceptional case of mandatory fusion", "what perceptual judgment no longer has", the Prsa reference, and "The same authors go one step further".

The six off-list items had never been touched (`git log -S` returns only the creation commit `1e002516b9` for each). This pass fixed five of them: "a decade on", "most sensitive probe", "proven … by the definition of the measurement", "propagates into a different perceived world" and "reported nowhere", and it added the falsifier sentence. It kept "unaided" (see Stability Notes). It did not carry out the pessimistic review's `binding-void` and `three-kinds-of-void` cross-page notes. Both are listed under Follow-ups.

## Verification Ledger

Each source was pulled raw and grep-tested with whitespace collapsed. No summariser was used. All eleven quotations in the body were re-grepped against the fetched texts after editing. Each was found at count ≥ 1: count 1 in the full text or abstract, and count 2 where both the abstract and the full text carry it.

- **Alais & Burr 2004** (*Curr Biol* 14(3) 257–262). State: **real-correct**. Checked against the Crossref record and the PubMed abstract (PMID 14761661). The quotation is verbatim. Direction of result: vision captures sound when visual localisation is good, and "the reverse holds" for severely blurred stimuli, as the article says. The authors take no metaphysical stance.
- **Deroy, Faivre, Lunghi, Spence, Aller & Noppeney 2016** (*Multisens Res* 29(6–7) 585–606). State: **real-correct metadata, with a paraphrase defect and a date defect** (Critical 2 and 4). Checked against Crossref and the PMC5082728 full text (efetch). All three quotations are verbatim. In the source, the "privileged access" sentence opens with "Accordingly". It follows from "Many theories of perceptual consciousness postulate strong interdependencies between consciousness and the capacity to integrate information" (Mudrik et al. 2014), and it carries "may". The next sentences report Hillis's cross-modal evidence that "participants had at least to some extent access to the sensory component signals". Author stance: this is an empirical review, and the authors take no dualist commitment.
- **Ernst & Banks 2002** (*Nature* 415(6870) 429–433). State: **real-correct**. Checked against Crossref, the PubMed abstract (PMID 11807554) and the full text (course-copy PDF). The quotation is verbatim in the abstract. The page says the weights "track momentary stimulus quality". The full text supports this: "Because the noise level varied randomly from trial to trial, the weights must have been set within the 1-s stimulus presentation."
- **Hillis, Ernst, Banks & Landy 2002** (*Science* 298(5598) 1627–1630). State: **real-correct metadata, with an empirical-scope defect** (Critical 1). Checked against Crossref, the PubMed abstract (PMID 12446912) and the full text (NYU lab PDF, 4 pp.). Both quoted fragments are verbatim. The lead example (disparity and texture to slant, weighted by reliability) is supported by the paper itself: "texture and disparity weights are set dynamically, trial-by-trial". Metamers appeared only where "Some thresholds actually fell outside the rectangle defined by single-cue thresholds … the participant failed to discriminate, on any basis, stimuli whose constituents were themselves discriminable". Losses were otherwise consistent: "only the within-modal data consistently indicated losses … sometimes rather large ones". Note 19 says participants sometimes detected the odd stimulus by a different calculation, shape constancy. The paper also explains the asymmetry: haptic and visual signals "do not always come from the same object", so mandatory combination "would be misleading". That sentence is now installed.
- **Körding, Beierholm, Ma, Quartz, Tenenbaum & Shams 2007** (*PLoS ONE* 2(9) e943). State: **real-correct**. Checked against Crossref, the PubMed abstract and the PMC1978520 full text. The quotation is verbatim. The value p_common = 0.28±0.05 comes from Experiment 1 (nineteen subjects). The authors' own wording is "The average probability of perceiving a common cause", so the page's "averaged 0.28" matches the source. The paper adds that p_common "will not be constant" outside the experiment. The page says the gate "performs near-optimally" within the conditions it was tuned on. The paper says behaviour emerges "as close to Bayes-optimal" and also that "there is no reason why the nervous system should be optimal under all circumstances", so the page's scope matches.
- **Mallick, Magnotti & Beauchamp 2015** (*Psychon Bull Rev* 22(5) 1299–1307). State: **real-correct metadata, with sample and hedge defects** (Critical 3). Checked against Crossref, the PubMed abstract and the PMC4580505 full text. Both quoted spans are verbatim in the abstract. The abstract gives 165 adults, "40 of whom were retested following a one-year interval". The NED model is Magnotti & Beauchamp's (2014), and Mallick et al. write only that "one solution would be to apply" it. Their description of the threshold supports the page's gate reading: below threshold "the individual infers that the auditory and visual speech cues arise from the same talker and integrate them". There is a name-form variant. PubMed and PMC index the first author as "Mallick DB", while Crossref deposits the family name as "Basu Mallick". The page keeps the PubMed form; recorded here, not changed. The abstract gives r = 0.91 and the results section gives r = 0.92. The page quotes the abstract.
- **McGurk & MacDonald 1976** (*Nature* 264(5588) 746–748). State: **metadata real-correct** (Crossref, PubMed PMID 1012311). **Content not reached.** PubMed has no abstract, and no full text was obtained. The page already says "the 1976 report was not consulted". Its one-line description of the effect is corroborated by the Mallick abstract: "pairing incongruent auditory and visual syllables produces a percept different from the component syllables".
- **Prsa, Gale & Blanke 2012** (*J Neurophysiol* 108(8) 2282–2291). State: **real-correct**. Checked against Crossref and the PubMed abstract (PMID 22832567). The quotation is verbatim. The page's "also fuse into metamers" matches "quasi-identical in terms of the integrated bimodal estimate became perceptual metamers", with thresholds larger "in pertinent cases".
- **Map self-references.** "The Binding Void" was created 2026-02-24 and "The Parsimony Void" (`epistemological-limits-occams-razor`, title confirmed) 2026-02-22. Both are correct.
- **Inline ↔ References.** No orphans in either direction.
- **Superlatives.** `find_superlative_claims` returned nothing. A manual pass found three, all fixed: "psychophysics' most sensitive probe", "The most-discussed exhibit", and "The rare void" in the description.
- **Sibling summaries**, each checked against its target's current text:
  - `binding-void` lead L45 ("whether phenomenal unity resists explanation in principle"): agrees.
  - `predictive-construction-void` L70 (subtraction barrier): agrees.
  - `plenitude-void` L74 (format): agrees.
  - `capability-division-problem` L56 ("Every candidate … disputable, the fusion void's well-modelled cue combination included"): agrees.
  - `modality-void` L83 ("mandatory within a sense and, with at least one exception, negotiable between senses"; this void "hides a percept's components and their weights"): **agrees** with this page's L47 and L73, and with its Further Reading gloss.
  - `epistemological-limits-occams-razor` ("cognitive parsimony … an architectural feature of minds"): this page's gloss "treats the razor as a cognitive bias in theory choice" agrees. That page's own gloss of *this* page is stale (Follow-up 1).
  - The operation-void sentence is stale against `three-kinds-of-void` L97 and `categorical-perception-void` L77 (Medium 2).

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Hillis's metamers stated as universal** (§Component Destruction L69). OLD: "Physically different cue-combinations that fuse to the same within-modality estimate become indiscriminable — perceptual metamers. The pre-fusion components are unavailable not only to report but to discrimination, psychophysics' most sensitive probe." In the paper, metamers appear in *some* conditions. The consistent finding is threshold loss in the cues-inconsistent direction. NEW: "Within vision, discrimination consistently fell short of what the single cues allowed when disparity and texture changed in opposite directions, and in some conditions physically different combinations that fused to the same estimate could not be told apart on any basis — perceptual metamers. The pre-fusion components are unavailable not only to report but to discrimination." The same overreach sat in §Approaches. OLD: "the ceiling is proven rather than merely encountered: metamers are indiscriminable by the definition of the measurement." That sentence was also circular. NEW: "the ceiling is measured rather than merely encountered: constituents discriminable on their own stop being discriminable once fused into a metamer." This follows Hillis's note 7 definition. Seeded at research note L62 and L151.
2. **Deroy's "may" hardened, and an inference from theories presented as the authors' own proposal** (§Relation, Dualism). OLD: "The same authors go one step further, suggesting that privileged access to the integrated product is why one experiences phenomenal unity; that is an account in terms of access". NEW: "The same authors go one step further, drawing on theories that tie consciousness to integration: privileged access to the integrated product may be why one experiences phenomenal unity. That is an account in terms of access". Pronoun check: "That" refers to the suggestion in the preceding sentence.
3. **Mallick: the stability sample was dropped and a suggestion hardened** (§A Trait). OLD: "observed "dramatic differences … (from 0 % to 100 %)," stable across a year (test-retest correlation, r = 0.91). … the authors propose modelling". The stability figure covers 40 of 165 participants, and the model is one the authors suggest applying. NEW: "observed, among 165 adults, "dramatic differences … (from 0 % to 100 %)," and in the 40 retested a year later the rates held (test-retest correlation, r = 0.91). … the authors suggest modelling". Seeded at research note L100–102.
4. **Wrong interval** (§Component Destruction L71). OLD: "They restate the cross-modal exception a decade on". The gap from 2002 to 2016 is fourteen years. NEW: "fourteen years on". Seeded at research note L110.
5. **The weighting model was misdescribed** (§Relation, Tenets 2/3). OLD: "precision weights are the kind of small, high-leverage parameter the minimality requirement points toward, since a slight shift in weighting propagates into a different perceived world." Under the maximum-likelihood combination the page cites, the estimate is linear in the weights, so a slight shift moves it only slightly. The flip-like point is the common-cause decision near threshold, as in Körding's report rule and Mallick's "rapid transition" near an individual's threshold. NEW: "precision weights look like the small, high-leverage parameter the minimality requirement points toward, but under reliability weighting a slight shift moves the estimate only slightly; the leverage sits at the common-cause gate, where near threshold a slight shift decides whether one event or two is perceived." The paragraph stays labelled speculation and keeps its no-evidence clause. Seeded at research note L176.

### Medium Issues Found

1. **Internal tension in the ventriloquist paragraph** (L65). OLD: "the auditory estimate that disagreed is gone". That asserts component loss across senses, where §Component Destruction says components are partially available between senses. NEW: "appears nowhere in it", which is a claim about the felt sense only.
2. **Stale sibling summary** (§Distinguishing Sibling Voids). OLD: "fusion is perception's". `categorical-perception-void` (created 2026-09-28) places itself in the operation-void family (L77), and `three-kinds-of-void` L97 lists it there. It is perceptual too. NEW: "fusion is one of perception's, beside [[categorical-perception-void|categorical perception]]". The link is piped, and the page was added to `related_articles`.
3. **"reported nowhere" is false of the Map's own practice** (closing paragraph). The positions register reports credence and evidence grade, and independence scoring exists. OLD: "and reported nowhere. … whose weights the concluder cannot read". NEW: "and seldom reported in full. … cannot fully read".
4. **Falsifiers absent.** This was deferred twice against the soft line, which carries no consequence. Added one sentence after the within-sense ceiling: "Two findings would challenge the void as drawn: within-sense metamers that became discriminable with training, or introspective reports of single-cue estimates under conflict that predicted discrimination performance."

### Low Issues Found

- Description "The rare void" → "A rare void". The cross-review allowed "rare" but not uniqueness.
- "The most-discussed exhibit" → "A much-discussed exhibit". The superlative was unsupported.
- "psychophysics' most sensitive probe" was deleted inside Critical 1.

### Tenet Readings

- **Occam's Razor Has Limits.** The page uses no parsimony appeal on either side. The gate is explicitly "not a standing preference for the simpler model", and the tenet is applied to the edge of the gate's calibration, not used to settle a framework. That is symmetric with `tenets.md` L145 and L147. The page claims only that the void "bears on" the tenet and claims no support for it, which complies with P-V3.
- **Dualism.** The bearing is graded compatible at most: "this locates the explanatory residue rather than evidencing any account of it, and a physicalist reading of that residue is untouched". This complies with P-V3, and it does not concede epiphenomenalism.
- **Minimal Quantum Interaction and Bidirectional Interaction.** Labelled speculation, with "the void supplies no evidence that one does". Only the modelling claim inside the remark was corrected (Critical 5).
- **No Many Worlds** is correctly absent.

### Counterarguments Considered (reasoning modes; editor-internal)

- **The deflationist** ("nothing is lost; the components were never mental contents"). Mode One. The reply uses the deflationist's own evidential standard: single-cue stimuli are discriminable alone and stop being discriminable once combined.
- **The physicalist reading of the residue.** Mode Three. The boundary is marked honestly ("untouched by anything argued here").
- **Deroy's access account of unity.** Mixed. Mode Two identifies the move (an access account is offered for experienced oneness), then Mode Three leaves the residue to `binding-void`.

## Optimistic Analysis Summary

### Strengths Preserved

- The measured edge, now sharper. Hillis's own reason for the asymmetry turns the edge into a common-cause fact. Fusion is mandatory where signals reliably share a source, and negotiable where "haptic and visual signals … do not always come from the same object". This ties §Component Destruction back to §The Common-Cause Gate.
- "The machinery is third-person open and first-person closed."
- The McGurk hedging (L79) was left exactly as the cross-review fixed it.
- The pessimistic review's Tenet 5 relocation ("as compelling as ever and wrong") and its Deroy access/phenomenal reply.

### Enhancements Made

1. The Hillis rationale sentence (+24 words).
2. The falsifier sentence (Medium 4).
3. The categorical-perception sibling link (Medium 2).

### Persona notes (brief)

- **Hardline Empiricist.** Praises the scoped metamer claim and the stated falsifiers. The page now says what would move its own edge.
- **Process Philosopher.** Would want the self-motion metamer read as the felt self assembled by fusion. That is declined here: it would upgrade a Map reading on tenet load. It is recorded under Follow-ups as a subject idea, as the pessimistic review recorded it.
- **Chalmers, Nagel, McGinn.** The access/phenomenal seam is the page's strongest philosophical move, and it is preserved.
- **Stapp, Kane.** Relocating the leverage to the common-cause gate fits the selection-site material better than precision weights did. Probability matching (Wozny et al. 2010) is the natural next citation if a future pass has the budget. It is not added here.

## Remaining Items

None on this page. All fixes are applied.

## Stability Notes

- **What was checked, and how.** Raw sources were fetched and grep-verified: Hillis 2002 full text; Ernst & Banks 2002 full text; Körding 2007, Deroy 2016 and Mallick 2015 full texts from PMC; the Alais & Burr and Prsa abstracts. All eight DOIs were checked at Crossref. McGurk & MacDonald 1976 content was not reached, and the page discloses this.
- **Within-sense metamers are partial.** Losses are consistent, but full metamers occur "in some conditions". A future pass must not re-generalise this to "become indiscriminable" without a qualifier, and must not drop "in some conditions".
- **Deroy's access account** is an inference "Accordingly" from many theories, and it carries "may". Do not harden it to "is why", and do not present it as the authors' settled view.
- **Körding's p_common 0.28** is Experiment 1. "averaged" follows the authors' own "average probability". Do not re-litigate it.
- **"unaided"** (L83) is kept deliberately. The self-test the pessimistic review raised (alternating eyes open and closed over a dubbed clip) requires a constructed stimulus, which is an aid. The sentence is true as written. Re-flag only if the page drops "unaided".
- **The three-kinds classification mismatch** is a cross-page matter, not a defect here. `three-kinds-of-void` L97 calls the family "occluded at the readout", while this page says "unexplorable core, unexplored margin".
- **The cross-review's notes still bind:** the brain-side assignment is held open; there is no "first or only" superlative; the physicalist reading is bedrock; "no computational remainder" is the cross-review's own scoping and should not be tightened or loosened.

## Follow-ups (corpus sweep; not edited)

1. `voids/epistemological-limits-occams-razor.md` L68 says the fusion void finds "the same economy below theory … where the nervous system continually chooses between one-cause and two-cause models … There parsimony arrives as a finished percept". L116 says "The same economy running sub-personally inside perception". Both carry the pre-2026-10-15 reading that this page retracted (Körding's model averages both structures, and its fitted p_common of 0.28 is no simplicity preference). **Medium-High**: a sibling summary contradicting its target.
2. `voids/phenomenal-quality-void.md` L167: "The charted combination machinery that manufactures the felt singleness of a scene". The fusion page now leaves open whether access explains experienced oneness. **Medium.**
3. `voids/voids.md` L217: "component access preserved between senses" is missing the Prsa exception. L306: "Within-modality fusion is mandatory and discards the components" overstates a partial metamer finding. **Medium** (navigation surfaces).
4. `voids/three-kinds-of-void.md` L97: "fusion delivers the fused percept and never the component estimates" ignores partial cross-modal access. L99: "the McGurk syllable is still heard after the explanation" asserts the impenetrability this page rests nothing on. **Low.**
5. `voids/binding-void.md` L87: "and themselves suggest an access-based account of it". To match the source and this page, it could be "drawing on theories that tie consciousness to integration". **Low.**
6. `archive/concepts/phenomenal-binding.md` L77: "Researchers acknowledge this gap explicitly" frames Deroy's proposed account as an admitted gap, and the capitalised "When" drops "Accordingly,". **Low** (archive).
7. `research/voids-serial-order-void-2026-09-17.md` L45 and L175 quote this page's operation-void sentence ("where transit, … fusion is perception's"), which changed today. It is a Map-internal quotation that has now gone stale. **Low.**
8. `research/voids-modality-void-2026-09-05.md` L220 and `research/phenomenal-binding-multimodal-integration-2026-01-23.md` L51 carry the pre-Prsa boundary and the capitalised "When" respectively. **Low.**
9. **Seeding note `research/voids-fusion-void-2026-09-02.md` (not edited).** Its defects:
   - L41: "the eyes and the hand" is the non-destructive case.
   - L42: "destroyed"; "the catalogue's clearest case" (a superlative); "negotiable between senses" without the Prsa exception; "the McGurk illusion persists however well one knows the stimulus" (unverified); "different minds run visibly different weightings" (Mallick places the difference in a disparity threshold).
   - L62: "become indiscriminable"; "the most sensitive probe psychophysics has".
   - L82–83 and L170: "model-selection", "chosen model", "parsimony *implemented*", "simplicity preference", "felt singleness … manufactures". Körding's model averages, and p_common is 0.28.
   - L100–102 and L127: stability is not scoped to the 40 retested participants.
   - L109: Deroy's sentence is given as their claim; in the source it opens "Accordingly", drawing on many theories.
   - L110: "a decade on".
   - L129: "information the system no longer carries".
   - L141: "There is no experience of *almost* fusing", which its own L143 contradicts.
   - L151: "proven ceiling … by definition".
   - L174: "no remainder", "firmly"; "does not touch why … experienced as one".
   - L176: "a small shift in weighting propagates to a different perceived world".
   - L190: "a feature no standalone article in the catalogue currently owns". This is the refuted first-or-only superlative, still live in the Disposition section. The 2026-09-04 cross-review corrected it only in Potential Article Angles.
10. Subject ideas carried from the pessimistic review, unharvested because harvest does not mine pessimistic files:
    - probability matching in perceptual causal inference (Wozny, Beierholm & Shams 2010);
    - the self-motion metamer as a bodily-self case (Prsa et al. 2012).
