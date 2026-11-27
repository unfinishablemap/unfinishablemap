---
title: "Deep Review - The Modality Void"
created: 2026-11-27
modified: 2026-11-27
human_modified: null
ai_modified: 2026-11-27T14:54:06+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[modality-void]]"
  - "[[research/voids-modality-void-2026-09-05]]"
  - "[[pessimistic-2026-10-26-modality-void]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-27
last_curated: null
---

**Date**: 2026-11-27
**Article**: [[modality-void|The Modality Void]]
**Previous review**: Never deep-reviewed. Prior passes were two pessimistic reviews, [[pessimistic-2026-09-07-modality-void|2026-09-07]] and [[pessimistic-2026-10-26-modality-void|2026-10-26]], each discharged by a refine-draft (`7e737f67ad`, `6be34cefec`).
**Selection**: chosen by the driver, because voids are outside the `deep_review.py` pool. The page was created on 2026-09-06 from `research/voids-modality-void-2026-09-05`.
**Word count** (`analyze_length`, body-only): 2,566 → 2,723 (+157). Status is `soft_warning` before and after. Voids thresholds are 2,000 soft, 3,000 hard and 4,000 critical, and the hard gate fires at `>=`. Headroom fell from 433 to 276.

## Pessimistic Analysis Summary

The 10-26 pessimistic review said every quoted span reproduces, and that is still true: every string inside quotation marks is verbatim (see the ledger below). The defects sit in paraphrases, glosses and inferences, which no earlier pass checked against the source. Four were seeded by the research note (L144, L150, L175 and L203). One was installed by the 10-26 repair (`6be34cefec`, the Tenet 5 paragraph). Two are Map-internal summaries that went stale or were incomplete from the start.

### Critical Issues Found

1. **Macpherson misread as yielding a count (Indirect methods, and the second deflation).** OLD: "Macpherson's multidimensional space lets a count fall out of a sense's coordinates rather than out of intuition." OLD (second deflation): "multidimensional taxonomies already narrowing it". The source (Glasgow eprints author version, pp. 34–35) says plotting individuates senses "in a nonsparse, fine-grained manner". It says the plotting can be done for token or idealised senses, that clusters "Perhaps … would correspond to the Aristotelian senses", and that for neighbouring senses "we should not concern ourselves with the question of whether they are the same sense. Once we have plotted their location in the space and noted their similarities and differences, we have said everything we need to say about the senses." So no count falls out: the count depends on grain, and the same-sense question is retired. NEW: "Macpherson's multidimensional space locates each sense by its coordinates rather than by intuition; any count then depends on the grain at which the space is read (token senses or idealised ones, points or clusters), and once senses are plotted, she holds, "we have said everything we need to say about the senses"." Also "narrowing it" → "recasting it as a matter of coordinates and grain". Seeded at note L203 ("let the count fall out of clustering rather than intuition").
2. **O'Callaghan's tentative suggestion presented as a commitment.** OLD: "O'Callaghan goes further, restricting "the senses" to low-level systems that need not correspond to categories of experience." The source (author's pre-publication PDF, §6) says "perhaps we should restrict talk of the senses to low-level systems such as the eye and very early visual processes, which can be individuated as Heil and Keeley suggest. But these senses are not perceptual modalities, and they do not correspond neatly to categories of experience." The article dropped "perhaps" and turned "do not correspond neatly" into "need not correspond". NEW: "O'Callaghan goes further, tentatively: perhaps "the senses" should name only low-level systems individuated Keeley's way, which do not correspond neatly to categories of experience." Seeded at note L150 ("Proposes restricting").
3. **Hurley and Noë: "answers" where the source says "address".** OLD: "Their question … is answered by charting relations between brain, body and world". Published PDF, abstract: "We use the dominance/deference distinction to address the comparative gaps … We do so not by inward scrutiny but rather by expanding our gaze". NEW: "they address by charting relations between brain, body and world rather than by inward scrutiny". Seeded at note L52 ("cannot be closed 'by inward scrutiny'") and L175 ("is answered 'not by inward scrutiny'").
4. **von Melchner et al.: motive credited to scare quotes that are not about evidence.** OLD: "The scare quotes are deliberate: behaviour, not report, is the evidence." The only scare quotes inside the quoted span are on 'rewired', a term for the surgery. The quotes the note had in mind are on 'seen', which the article does not quote. NEW: "The hedge is the authors' own: the ferrets *respond as though* they perceive, and the abstract puts 'seen' in scare quotes. Behaviour, not report, is the evidence." The authors' hedge is now located in their own words, and no motive is credited to them. Seeded at note L144.
5. **The Tenet 5 paragraph contradicts itself (installed by `6be34cefec`, 10-26).** OLD: "gains a narrower instance than the palette extension void supplies … it is the count the evidence leaves least settled … parsimony proper is not what selected the five." It claims an instance of a parsimony tenet while saying parsimony was not involved. That is also a P-V3 over-claim, since a void supports no tenet. "Least settled" is a comparative that Macpherson does not support: she says the count is open, not that five is the least settled candidate. NEW: "is touched only at a tangent; the palette extension void remains the clean case. … it is a count the evidence has repeatedly unsettled … Parsimony did not select the five, so the case is no instance of the tenet; what it shares with the tenet is the lesson that felt obviousness, like felt simplicity, is no measure of a carving's warrant while knowledge is incomplete." Both Macpherson quotations are kept verbatim. The paragraph now turns Tenet 5 on no one, which is consistent with `tenets.md` L145/L147, where the tenet binds parsimony on either side.
6. **The Bidirectional remark reintroduces the "no tags" premise.** OLD: "arrive tagged with a channel the selecting consciousness cannot read — so the interface would be modality-blind on the mind side." The article grants Fréchette that the tag is "present, evident and irresistible", so the mind side is handed the tag and cannot audit it. The 10-26 review removed the same premise from the Dualism paragraph and missed this one. NEW: "arrive with a channel tag the selecting consciousness is handed but cannot audit — so on the mind side the interface would work from modality labels it has no means to check." Seeded at note L221.
7. **The apex summary dropped the apex's own scope (Dualism paragraph).** The apex's description and L78 have marked the asymmetry as "an exteroceptive regularity rather than a universal law" since 2026-06-20 (`73ff7ed2d0`), because interoception inverts it. The article (created 09-06) gave the finding without that qualifier. NEW appends: "— an asymmetry the apex marks as exteroceptive rather than universal, since interoception inverts it." Both apex quotations still match verbatim: "across five senses one modality at a time" is at L48, and "common supramodal signature" is at L48 and L126.
8. **The fusion-void qualifier went stale (Distinguishing Sibling Voids).** OLD: "mandatory within a sense and negotiable between senses". On 2026-10-15 (`84d41c51fd`) `voids/fusion-void` L45 became "mandatory within a single sense and, with at least one exception noted below, negotiable between senses" (Prsa, Gale & Blanke 2012, visual–vestibular self-motion). NEW: "mandatory within a sense and, with at least one exception, negotiable between senses".

### Medium Issues Found

- **Target of Macpherson's reply.** OLD: "Macpherson's reply leaves even the count open rather than conventional". Her "simply silent" verdict answers Nudds's claim that the folk conception fixes five ("obvious", Nudds 2004 p. 35 as she quotes it), not his conventionality. NEW: "Macpherson's reply to Nudds's folk five leaves even the count open and empirical rather than conventional". Her text supports "empirical": the folk "embrace the idea that the number of actual senses is a matter to be determined by empirical findings". Seeded at note L187.
- **A condition was dropped from oral referral.** OLD: "Retronasal olfaction is experienced as taste, in the mouth." Spence 2016's abstract (OpenAlex) says that for retronasal odours "it is the congruency between the odour-taste(s) pairing that is key". NEW: "typically experienced", plus "modulated for retronasal odours by how congruent odour and taste are". The same unqualified sentence is live elsewhere (see Remaining Items).
- **The originator of the TVSS finding.** OLD: "Hurley and Noë report that sensory-substitution users describe quasi-visual experience only while actively controlling the camera". Hurley and Noë relay Bach-y-Rita (1984: 149). NEW: "Hurley and Noë relay Bach-y-Rita's finding that tactile-vision substitution users reach quasi-visual experience …". The 10-26 review declined this change; it is applied here following the named-idea-originator discipline. Bach-y-Rita is named without a year, so no References entry is owed.
- **Two dropped qualifiers on Macpherson.** "independent axes" became "relatively independent axes" (source: "relatively independent dimensions"). "may collapse into another" became "may come to look like another" (source: "could turn out to look very much like", which she follows with the remark that the identity is "a point much disputed").
- **Reference metadata.** Fréchette gains 31(2), 413–430 (Crossref and PMC XML; epub 2021-10-26, issue 2023-06). O'Callaghan gains pp. 92–118 (Crossref and OpenAlex) and a provenance note ("Read in the author's pre-publication version"). The author PDF is headed "Oxford Handbook to Philosophy and Cognitive Science", which is the origin of the old wrong title that 10-26 fixed.

### Verification Ledger (§2.4, this run)

Every quoted string was grepped after collapsing whitespace and normalising quote marks. Counts are hits in that source.

- **Auvray & Spence 2008** (*Consc. Cogn.* 17(3) 1016–1031). State: real-correct. Europe PMC abstract: "the taxonomy currently used to define our senses is simply not appropriate" [1]. "propose it may indicate" renders "We propose that … may be indicative of the fact that" faithfully.
- **Craig & Bushnell 1994** (*Science* 265(5169) 252–255). State: real-correct. Europe PMC abstract: the long quotation [1], verbatim with "first demonstrated in 1896". The gloss "two classes of ascending spinothalamic tract neurons that are sensitive to innocuous or noxious cold" plus "central disinhibition, or unmasking" supports "two cold-responsive spinothalamic classes differing in innocuous versus noxious tuning". Result direction: grill-evoked pain matched cold-evoked pain psychophysically, as the article implies. "Correct channel tag" is the Map's reading and is labelled as a near-case.
- **Fréchette 2023** (*EJP* 31(2) 413–430). State: real-wrong-metadata (incomplete; volume and pages added). PMC10946872 full-text XML via efetch:
  - "my experiencing "da da" as a case of hearing appears to me as evident as my experiencing "ba ba"" [1]. The source continues "as a case of hearing does in a normal situation", so the truncation is fair. The article's single quotes inside double quotes are a typographic nesting only.
  - "[e]ven when we are told about the mechanisms underlying the illusion, we simply cannot be rid of our classification" [1].
  - Gloss "subsume tokens of our experiences under experience-kinds": source "subsume tokens of our experiences under different experience kinds, or senses" [1].
  - "evidently given": "it appears to us as evident" [1].
  - "argues, against Nudds": "In contrast to Nudds … it does matter to Alice" [1].
  - "irresistible" (10-26) is still faithful. Fréchette leaves the correctness of the classification open ("we could assess this classification in terms of correctness"), so calling McGurk a *mis*classification is the Map's reading. The article marks it as such ("The Map grants that thesis").
- **Hurley & Noë 2003** (*Biol. Phil.* 18(1) 131–168). State: real-correct. Read in the published Kluwer typeset PDF, author-hosted at alvanoe.squarespace.com/s/neural-plasticity-and-consciousness.pdf; the 2002 consc.net draft was compared and lacks the illusory/veridical sentence.
  - "Notice that cortical dominance thus schematized involves illusory experience, while cortical deference involves veridical experience" [1] supports the article's gloss.
  - "We suggest that an inward focus in response to explanatory gap worries can be misleading" [1].
  - "not by inward scrutiny but rather by expanding our gaze" [1].
  - "active control of the camera (1984: 149)" [1] and "subjects report only tactile sensation" [1].
- **Keeley 2002** (*J Phil* 99(1) 5–28; OpenAlex pages 5–28, Crossref first page 5). State: real-correct, and disclosed as second-hand. O'Callaghan's preprint: "Keeley (2002) suggests we individuate the senses in terms of organs evolutionarily dedicated to picking up information of a certain kind" [1]. The article's gloss is verbatim apart from the verb.
- **Liang et al. 2022** (arXiv 2203.02053, NeurIPS 2022). State: real-correct. arXiv API abstract: "embedded at arm's length in their shared representation" [1]. The five authors match.
- **Macpherson 2011** (*Phil. Stud.* 153(1) 123–142; online 2010-10-30). State: real-correct. Glasgow eprints 43551 author version:
  - "what it was an experience as of" [1].
  - "phenomenal character criterion could turn out to look [p.16] very much like the representational criterion" [1].
  - "I believe that the folk concept is simply silent with regard to the question of how many senses there are" [1].
  - "progress in science, together with philosophical investigation" [1].
  - "creating a brand new sense" [1] (source: "or are we creating a brand new sense?"; the article's "we [are] creating" is a bracketed reordering).
  - "the folk" [1 in this sense].
  - "the number of senses that they recognize has frequently been altered" [1].
  - "disputed throughout history by both philosophers and scientists" [1].
  - "we have said everything we need to say about the senses" [1] (new this run).
  - List fidelity: the four criteria (representation, phenomenal character, proximal stimulus, sense organ) match her list and order. She credits the four approaches to Grice (1962) in fn. 17.
- **Nudds 2004** (*PAS* 104(1) 31–51; Crossref title "II—The Significance of the Senses"). State: real-correct, secondary. The quotation is nested in Fréchette [1], cited "(Nudds, 2004, p. 46)", and p. 46 falls within 31–51. The primary was not reached (Semantic Scholar closed; scholar.archive.org returns a challenge page). The reference entry already discloses that it was not consulted directly.
- **O'Callaghan 2012** (*Oxford Handbook of Philosophy of Cognitive Science*, pp. 92–118). State: real-wrong-metadata (pages and provenance added). The published chapter was not reached. All checks are against the author's "forthcoming" PDF, so any later wording change is unverified.
- **Spence 2016** (*FQP* 50 117–128). State: real-correct. OpenAlex abstract: "mislocalization of food-related olfactory stimuli to the oral cavity" [1], and "Many researchers believe that it contributes to the widespread confusion" supports "held partly responsible". ORA author PDF: "rather the receptor surface (or sensory system) that has been used to detect those chemosensory signals" [1] supports the receptor-surface clause. Congruency condition: see Medium.
- **von Melchner, Pallas & Sur 2000** (*Nature* 404(6780) 871–876). State: real-correct. Europe PMC abstract: "'rewired' ferrets respond as though they perceive the stimuli to be visual rather than auditory" [1], and "the perceptual modality of a neocortical region is instructed to a significant extent by its extrinsic inputs" [1]. Result direction: visual behaviour through the rerouted pathway, as stated. Scope: the light was presented in the field "'seen' only by this projection". The article does not overstate this.
- **Map-internal.** The P-A4 quotation is verbatim at `positions/agency-and-will.md` L91. P-M2 credence *high* is at L89. The apex quotations are verbatim (L48, L126). The fusion-void qualifier is stale (Critical 8).
- **Empirical-currency helper** (`find_superlative_claims`): no hits.
- **Inline ↔ References**: no orphans in either direction. The two Map self-references (fusion-void, source-attribution-void) are linked in the body.

### Reasoning-mode classification (editor-internal)

- **Nudds (conventionality).** Mode One: the attribution errors hold on any carving, so conventionality reaches only the counting face.
- **Empirical-count deflation.** Conceded and scoped per face, with no tenet invoked.
- **Neurobiological individuation (Keeley, third deflation).** Mixed: non-authoritativeness on the count is conceded, and a boundary mark is placed where the stake is the unauditable verdict.
- **Physicalist reading of the supramodal signature.** Mode Three, stated in its strongest form ("late convergence … nothing here separates the readings").
- **Labels:** `grep` found 0 forbidden labels in the body.

### Counterarguments Considered

- *Macpherson's own view dissolves the counting face.* Partly true. Once senses are plotted, the same-sense question is retired. The article now says so in Indirect methods, and that agrees with its classification of the counting face as unexplored and third-personally tractable. The attribution and boundary faces do not depend on the count.
- *Eliminativist and Buddhist pressure on "a subject handed a verdict"* (10-26 personas). This is bedrock and is not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The lead's P-A4 bridge, which makes the void an unauditable-verdict structure and not ignorance of anatomy.
- The near-case demotion of the thermal grill.
- The per-face three-kinds classification.
- The common-cause paragraph, which names the shared upstream, the missing distinguishing test and the thin face-level independence "claimed as no more". The Hardline Empiricist persona would single this out as the model of evidential restraint.
- The AI section's two cautions.
- Every verified quotation, kept as it was.

### Enhancements Made

- The Indirect methods section now carries Macpherson's actual view (count relative to grain; the same-sense question retired). This sharpens the void's asymmetry: third-person instruments do not merely answer the count better, they reshape the question.
- The Tenet 5 paragraph now models the either-side discipline instead of manufacturing an instance.

### Cross-links Added

None. No new wikilinks were added. The two open P3 cross-review tasks (Molyneux void, todo ~L1925; vitality-form void, ~L4121) keep their anchors: the "Distinguishing Sibling Voids" section and its paragraph structure are unchanged apart from the in-sentence fusion qualifier.

## Remaining Items (follow-ups, none edited)

1. **`voids/voids.md` L219.** The catalogue gloss still runs on the abandoned "modality arrives as the *format* of an experience rather than as a checkable datum" premise, and it lists "the thermal grill" among channel tags that are "wrong". The article demotes the grill to a near-case with a *correct* tag. The index is CRITICAL-length, so any fix must be net-zero.
2. **`voids/voids.md` L308** (research ledger). "the phenomenal-character criterion collapses into the representational one" overstates Macpherson's "could turn out to look very much like". "interlaced innocuous warm and cool bars delivered as burning pain" is listed under "which sense delivered a content", which contradicts the demotion.
3. **`topics/chemosensory-consciousness-and-the-interface` L78.** "Retronasal smell is experienced as taste, in the mouth" is unqualified. It needs "typically" or the congruency condition (Spence 2016).
4. **`research/voids-prevalence-void-2026-09-10` L134.** It glosses the modality void as "modality arrives as the *format* of an experience", a stale premise. It is a research note, so annotate it only.
5. **Seeding research note `research/voids-modality-void-2026-09-05`.** Do not edit it in a review pass. It needs dated correction lines for:
   - L52/L169/L222: the "format, not datum" premise, which Fréchette denies.
   - L52/L175: "cannot be closed 'by inward scrutiny'" / "is answered 'not by inward scrutiny'". The source says "address … not by inward scrutiny".
   - L65/L215: "the five-sense count is the simplest carving"; and the "parsimony selects" instance.
   - L122/L173/L187: the thermal grill as an attribution "class error".
   - L144: a motive credited to the 'seen' scare quotes.
   - L150: "Proposes restricting" drops O'Callaghan's "perhaps".
   - L149/L255: the handbook title "Philosophy and Cognitive Science", which should be "of Cognitive Science".
   - L171: "Introspection delivers a folk five".
   - L187: Macpherson's reply aimed at conventionality instead of the folk-five claim.
   - L199: "Spence reports oral referral in the trained as in the untrained". The ORA PDF has 0 hits for "trained" or "expert", so the claim is unsupported.
   - L203: "let the count fall out of clustering".
   - L220: the fusion boundary without the Prsa exception.
   - L221: "modality-blind on the mind side".
6. **Not reached this run:** the Nudds 2004 primary text and the published O'Callaghan chapter (pre-publication version only). There is no archived predecessor page; the article was created fresh, so no `archive/` sweep is owed.

## Stability Notes

- **Checked this run, at raw source:** every quotation, paraphrase and gloss in the body against the sources named in the ledger. That covers the published Hurley–Noë PDF, the Macpherson and O'Callaghan author PDFs, the Fréchette PMC full text, the Spence ORA PDF and OpenAlex abstract, the Europe PMC abstracts and the arXiv abstract. All DOIs were checked against Crossref. Future reviews need not re-verify these strings unless the body changes. Re-check Nudds 2004 and O'Callaghan if either primary becomes reachable.
- The Map's reading that the McGurk tag is a *mis*classification and the thermal grill's tag is *correct* is a labelled Map interpretation, not a source claim. Do not re-flag it as source/Map conflation.
- Bedrock: the eliminativist and Madhyamaka objections to "a subject handed an unauditable verdict" are framework-boundary disagreements (10-26) and are not defects.
- The Tenet 5 relation is now graded as "touched only at a tangent". Do not restore an "instance" claim unless parsimony is shown to have selected the five.
- The Dualism relation is graded "compatible … predicts nothing … consonant, not probative", which is P-V3-compliant. Do not upgrade it.
