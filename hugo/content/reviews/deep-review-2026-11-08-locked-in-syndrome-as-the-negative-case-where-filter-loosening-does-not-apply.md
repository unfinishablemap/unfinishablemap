---
ai_contribution: 100
ai_generated_date: 2026-11-08
ai_modified: 2026-11-08 21:08:47+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-11-08
date: &id001 2026-11-08
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-08 21:08:47+00:00
modified: *id001
related_articles: []
title: Deep Review - Locked-In Syndrome as the Negative Case (2026-11-08)
topics:
- '[[consciousness-disruption-and-the-mind-brain-interface]]'
- '[[neurological-dissociations-as-interface-architecture]]'
---

**Date**: 2026-11-08
**Article**: [Locked-In Syndrome as the Negative Case Where Filter-Loosening Does Not Apply](/topics/locked-in-syndrome-as-the-negative-case-where-filter-loosening-does-not-apply/)
**Previous review**: [2026-08-27](/reviews/deep-review-2026-08-27-locked-in-syndrome-as-the-negative-case-where-filter-loosening-does-not-apply/) (and 2026-07-19, 2026-07-10)
**Lens**: Fourth pass, scoped to what moved since 08-27. The 08-27 review declared the page converged unless a dependency changed; three body commits have landed since, and one of them (3da824a5, 2026-09-08) added a whole section — "What the Pure-Output Idealisation Omits" — with seven new citations that no deep review had reached. This pass web-verified that section at the publisher of record (Crossref metadata; Europe PMC abstracts; the Laukkonen accepted manuscript in full), checked the section's coherence with the lead and the two-arms section, re-checked the two cross-link commits (29a13992, 44a7014c), re-ran the Map-internal quotation check in both directions, and re-tested the 08-27 spillover. Word count 3842 → 3849 (+7; topics hard threshold 4000, gate `>=`; headroom 150). Length-neutral mode: the seven words are a published-version References correction (+5) and one scoping qualifier (+2), offset by nothing because no trimmable passage was found that did not carry a prior review's fix.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Silva et al. 2025 cited as a medRxiv preprint after journal publication (real-wrong-metadata, currency).** Crossref records the preprint 10.1101/2025.04.24.25326368 as `is-preprint-of` 10.1088/1741-2552/adf50e: *Journal of Neural Engineering* 22(4), 046039, published 2025-08-07 (PMID 40720979, PMC12337102). The published abstract carries the quoted fragment verbatim ("leveraged different neural representations with differentiable spectrotemporal responses") and the published author list gives Brosler as "Samantha C." **Fixed**: References entry now cites the journal version with its DOI and "Brosler, S. C."; the inline cite and the quotation are unchanged. Family check: the preprint DOI appeared nowhere else in obsidian/, archive/ or hugo/content outside this page and its twin, so nothing to propagate.
- **An unscoped superlative in the never-reviewed section.** "And in the largest series, 100 patients followed for a year" (Kumral et al. 2022) reads as a claim about the literature; the Map has not verified that 100 is the largest locked-in cohort ever reported (Patterson & Grabois 1986 pooled 139 literature cases, for one). `find_superlative_claims` returned empty — "largest series" is outside its lexicon — so this would have sailed through the mechanical sweep. **Fixed** to "the largest of these series", which is true of the five findings the paragraph lists (9, 6, 10, 100 patients) and claims nothing about the field.

### Medium Issues Found

- **A residual categorical "clean pure-output case" after the new section had qualified it.** The 09-08 refine softened the lead and §"Why Filter-Loosening Does Not Apply" to "predominantly output" / "substantially undisturbed" and added the omissions section ("purity is approximate"), but left §"A Taxonomy Graded by Output" L58 asserting that the Bauer classification "is what makes locked-in syndrome a clean pure-output case rather than a mixed one". Read after the omissions section this is a small internal friction: a clinical claim where only a classificatory one is earned. **Fixed** to "is what classes locked-in syndrome as a pure-output case rather than a mixed one" — the taxonomy classes the case; the clinical qualification stands. Zero net words.
- The honest ledger's "only the motor output is destroyed; so consciousness is expected to persist" (L80) is the production theory's account of the *idealised* case, and the omissions section explicitly says the argument below "is built on the idealisation with that qualification carried along". Left as is; noted so the next pass does not re-litigate it.

### Low Issues Found

- Schnakers et al. 2008, fifth author: the article writes "Eeckhout, P."; PubMed indexes "Van Eeckhout P" while the publisher of record (Springer, via Crossref) gives family "Eeckhout", given "Philippe". The entry matches the publisher of record; left unchanged and recorded here so it is not flagged as an error later.
- Kumral et al. 2022: Crossref `issued` is 2021 (online-first) while the issue (122(1)) and Europe PMC's `pubYear` are 2022. The article's 2022 is the issue year; left as is.

### Publisher-of-record citation ledger (this pass)

Scoped to the 09-08 section and its new References entries, plus the one cite that gained a dependency. Verification sources: Crossref API for every DOI; Europe PMC REST abstracts (PubMed-walled pages were not used); the Laukkonen accepted manuscript PDF from the Southern Cross University research portal.

- **Smith & Delargy 2005** (Locked-in syndrome) — state: **real-correct; new quote raw-grep VERBATIM** at PMC549115: "Although patients are conscious, attention, executive function, intellectual ability, perception, and visual and verbal memory can be affected." Oxford comma present in the source. The article's framing ("although patients are conscious") matches the source clause. (Prior ledgers covered the cardinal-presentation quote; not re-litigated.)
- **Rousseaux et al. 2009** (Evidence of persisting cognitive impairment in a case series of patients with locked-in syndrome) — state: **real-correct; both quotes VERBATIM.** Crossref: *J Neurol Neurosurg Psychiatry* 80(2), 166-170, DOI 10.1136/jnnp.2007.128686. Abstract: "Nine patients with LIS resulting from brainstem stroke"; "LIS patients showed significant difficulties in auditory recognition (associative level), oral comprehension of complex sentences, delayed visuospatial memory, mental calculation and problem solving"; "These disorders were not related to a specific localisation of lesions." Result direction: impairment present, as the article says. Fifth author appears as "Danze" (Crossref) / "Danzé" (PubMed); article follows Crossref.
- **Bassetti, Mathis & Hess 1994** (Multimodal electrophysiological studies … report of six patients) — state: **real-correct; quote VERBATIM; numbers VERBATIM.** Crossref: *JNNP* 57(11), 1403-1406, DOI 10.1136/jnnp.57.11.1403; PMC1073195. Abstract: "Somatosensory evoked potentials were altered in four of the patients, and brainstem auditory evoked potentials were altered in two of four patients examined, showing a clinically unsuspected tegmental involvement. The EEG showed a predominance of reactive alpha activity in all patients, documenting a preserved consciousness." Article's "four of six" is the abstract's "four of the patients" with n = 6 supplied from the title.
- **Conson et al. 2008** (Selective motor imagery defect in patients with locked-in syndrome) — state: **real-correct; quote VERBATIM; direction correct.** Crossref: *Neuropsychologia* 46(11), 2622-2628, DOI 10.1016/j.neuropsychologia.2008.04.015. Abstract: "a profound impairment on a modified version of the hand-laterality task and a normal performance on mental rotation of abstract items"; "the pontine lesion, both determined a complete de-efferentation, and affected a component of the motor system, which is crucial for mental representation of body parts". The article's attribution of the deficit to the pontine lesion is the authors' own suggestion.
- **Schnakers et al. 2008** (Cognitive function in the locked-in syndrome) — state: **real-correct; quote VERBATIM.** Crossref: *Journal of Neurology* 255(3), 323-330, DOI 10.1007/s00415-008-0544-0. Abstract conclusion: "Results indicate that LIS patients can recover intact cognitive levels in cases of pure brainstem lesions, and that additional brain injuries are most likely responsible for associated cognitive deficits in the LIS." The article's gloss "scope the qualification rather than extend it" is fair to the conclusion. Author-form note under Low.
- **Kumral et al. 2022** (The clinical and cognitive spectrum of locked-in syndrome: 1-year follow-up of 100 patients) — state: **real-correct; figure VERBATIM; superlative scoped.** Crossref: *Acta Neurologica Belgica* 122(1), 113-121, DOI 10.1007/s13760-021-01675-5. Abstract: "One hundred patients with locked-in syndrome (LIS) were recruited"; "At the onset of stroke, orientation to time and place was normal in 43% of patients with a single infarct compared with 18% of those with PMIL". "Improving over the following year" is the paper's "many patients can show significant improvement in LIS"; acceptable paraphrase. "Largest series" → "largest of these series" (see Critical).
- **Laukkonen, Friston & Chandaria 2025** (A beautiful loop: An active inference theory of consciousness) — state: **real-correct; quotes VERBATIM; absence claim VERIFIED.** Crossref: *Neuroscience & Biobehavioral Reviews* 176, 106296, DOI 10.1016/j.neubiorev.2025.106296. Abstract: "namely an epistemic field"; "inferential competition to enter the world model"; "a selection for consciousness that we call Bayesian binding"; "epistemic depth, which is the recurrent sharing of the Bayesian beliefs throughout the system". The article's "The authors do not discuss locked-in syndrome" was tested against the 21,685-word accepted manuscript: zero hits for "locked", "de-efferent", "deafferent". The derivation is correctly labelled as the Map's.
- **Silva et al. 2025** (Implications of shared motor and perceptual activations …) — state: **real-wrong-metadata (preprint superseded; corrected to *Journal of Neural Engineering* 22(4), 046039, DOI 10.1088/1741-2552/adf50e; "Brosler, S." → "Brosler, S. C."). Quote VERBATIM in the published abstract.** Stance leg: the article uses the finding *against* a clean output-arm reading ("the cortical channel is not an anatomically segregated output arm"), so no endorsement is imputed.
- **Not re-litigated** (verified at the raw-text grain by the 07-10, 07-19 and 08-27 ledgers; no dependency moved): Bauer, Gerstenbrand & Rumpl 1979; Bruno et al. 2011; Albrecht & Devlieger 1999; Silva et al. 2024; Bodien et al. 2024; Plum & Posner 1966; the two Map self-citations.

Inline↔References: every `Author YYYY` has an entry and every entry is cited inline; no orphans in either direction. `find_superlative_claims` empty (but see the "largest series" miss above).

### Cross-link commits since 08-27, audited in situ

- 29a13992 (2026-10-01): the detection-problem paragraph now sends the reader to [covert-consciousness-and-cognitive-motor-dissociation](/topics/covert-consciousness-and-cognitive-motor-dissociation/). Target exists; the `#the-numbers-and-their-denominators` anchor resolves (its H2 is at that page's L37); the sentence still fits ("developed at length in … and will not be re-told here" is true of that page).
- 44a7014c (2026-10-23): the two-arms paragraph gained "[Tonic immobility](/topics/tonic-immobility-and-awareness/) also closes output with input reported partly open, but reflexively and briefly in an intact brain, a disanalogy that makes it a weaker test of the arms." Target exists; the disanalogy is stated, not merely asserted; consistent with the paragraph's "cutting predominantly one of them".

### Map-internal quotations (both directions)

- Inbound (this page quoting another Map page verbatim): **0**. Every double-quoted phrase in the body is an external-source quotation or the page's own term ("filter-loosening", "output-only", "pseudocoma"). The one piped link into the tenets page (`available rather than actual`) matches the tenets page's L95 wording.
- Outbound (other pages quoting this page): `concepts/filter-vs-interface-distinction` L76 quotes six phrases — "two dissociable arms", "an ascending or input arm", "a descending or output arm", "functional rather than anatomical", "the Map does not thereby locate either arm of the interface in the pons", "can only be inferred from EEG rather than read off behaviour, and at the bedside it may be genuinely uncertain". **6 of 6 still present verbatim** after this pass's edits (none of the three edits touched those sentences). The other ten pages linking here carry no quoted phrase on the linking line.

### Reasoning-mode classification (editor-internal)

- Engagement with the production/materialist theory (honest ledger): **Mode Three**, framework-boundary marking, honest — concedes empirical equivalence, claims no refutation. Unchanged.
- Engagement with Laukkonen, Friston & Chandaria 2025 (new since 08-27): **Mode Three** done the right way round — the Map derives the rival's prediction from its stated conditions, shows the rival gets the case right on its own resources, and uses that *against* its own evidential claim. No boundary-substitution; no label leakage (grep for the forbidden editor-vocabulary terms: zero).

### Counterarguments Considered

- *Pathway distinctness is neuroanatomy, not interface evidence* — bedrock, absorbed by the honest ledger across all three prior passes. Not re-flagged (08-27 Stability Notes honoured).
- *If the ascending channels are "not invariably untouched" (Bassetti), the "input arm intact" premise fails* — the 09-08 section already answers this: the departures run toward mild impairment, the argument is built on the idealisation with the qualification carried along, and the lead now says "largely sparing". Coherence check passed: lead → omissions section → two-arms section ("predominantly", "substantially persist") form one consistent gradient; the one residual categorical (L58) is fixed above.

## Optimistic Analysis Summary

### Strengths Preserved

- The omissions section is a model of the "cost it honestly" pattern the Hardline Empiricist persona praises: it names the qualification, quantifies it from five sources, and then says exactly what it does and does not cost ("not release … the categorical form of the intactness claim").
- The Laukkonen paragraph makes the honest ledger sharper against a named, fully worked rival rather than a strawman "production theory", and labels the prediction as the Map's derivation.
- The "read as interpretation" gate; the communication-vs-detection contrast; the twice-stated total-LIS caveat; the Silva 2025 finding used against the page's own clean-output picture.

### Enhancements Made

- References now point at the published, peer-reviewed Silva 2025 rather than a preprint.
- One superlative scoped; one classificatory claim no longer reads as a clinical one.

### Cross-links Added

- None. The page already carries the cluster's reciprocal links; adding any would cost words a converged page should not spend.

## Remaining Items

- **Spillover (different file), still standing — tasked this pass.** `concepts/filter-vs-interface-distinction` L76 still glosses this article as "Speech neuroprostheses decoding an intact intent-to-act signal from cortex give the diagnosis an engineering test", firmer than the hedge it summarises ("*appears to be* … On this reading …", and now also the Silva 2025 caveat that the decoded territory is shared with perception). That page's 2026-10-05 deep review checked the six quoted phrases but did not consider the gloss. Minted a P3 `refine-draft` for that page (3235 words; concepts hard 3500; headroom 264).
- `find_superlative_claims` lexicon miss ("largest series"): noted here; not tasked (tooling, not content).

## Stability Notes

The 08-27 notes stand: the materialist "pathway distinctness is neuroanatomy" point is bedrock, correctly absorbed; the calibration (illustration, not evidence; "available rather than actual") is tied to the tenets page's Tenet-3 standing block and should be revisited only if that block moves. New this pass: the 09-08 omissions section is now publisher-verified at the quotation grain, its seven cites are real-correct (one metadata update), and its qualification is carried consistently through the lead, the taxonomy section and the two-arms section. The honest ledger's "only the motor output is destroyed" is the rival's account of the idealised case and is covered by the omissions section's "carried along" clause — do not re-flag. Four passes in, with every section now reviewed at least once at the raw-text grain, treat the page as converged unless a dependency changes or a cited preprint publishes.