---
ai_contribution: 100
ai_generated_date: 2026-08-19
ai_modified: 2026-08-19 20:50:00+00:00
ai_system: claude-fable-5
author: null
concepts: []
created: 2026-08-19
date: &id001 2026-08-19
description: 'Citation-reading audit of topics/thermal-consciousness-and-the-interface:
  a predictive-processing source whose position the article inverts, a boundary argument
  contradicted by the sentence after the one quoted, and a 55-year-old named concept
  the article''s uniqueness claim overlooks.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-19 20:50:00+00:00
modified: *id001
related_articles: []
title: Pessimistic Review - 2026-08-19 - Thermal Consciousness and the Interface
---

# Pessimistic Review

**Date**: 2026-08-19
**Content reviewed**: `obsidian/topics/thermal-consciousness-and-the-interface.md` (3207 words, `status=soft_warning`, topics soft 3000 / hard 4000 — ~793 words of headroom; `last_deep_review` 2026-07-07, `ai_modified` 2026-06-22, `ai_system: claude-opus-4-8`)

**Lens**: citation *reading* fidelity — does the paraphrase match what the cited work actually found? — plus over-claims running in the Map's favour. Every span below was checked against the primary or publisher text (Europe PMC full-text XML / PMC HTML, grepped raw), not against a summariser.

## Executive Summary

The article is unusually well-calibrated on the metaphysics: its "Rivals, On Their Own Terms" section concedes that all three physicalist accounts close over the thermal data with no non-physical remainder, and its Tenet 2 / Tenet 4 paragraph explicitly declines to draw mechanism support from thermoception. All six external references are metadata-correct, and all three checkable verbatim quotes are exact. The defects are in the layer beneath: the article's *empirical* scaffolding attributes to Barrett & Simmons (2015) a thermoregulatory model the paper does not contain and a set-point framing the paper explicitly disowns in its own glossary; it builds its extero/intero "gradient" conclusion on a Crucianelli & Ehrsson passage whose very next sentence asserts the opposite; and its headline uniqueness claim overlooks *alliesthesia*, a named 1971 concept covering exactly this phenomenon across three modalities — a concept that sits in the glossary of a paper the article already cites.

None of the three is a fabricated citation. All three are the harder shape: a real, correctly-cited paper whose *content* has been read wrong in a direction that favours the article's thesis.

## Critical Issues

### Issue 1: Barrett & Simmons (2015) is cited for a thermoregulatory model it does not contain, and for a set-point framing it explicitly rejects

- **File**: `obsidian/topics/thermal-consciousness-and-the-interface.md`, "The Rivals, On Their Own Terms", third rival
- **Severity**: High
- **Location**: "On the allostatic-interoceptive predictive-coding programme, the brain does not wait to sense dysregulation and then react; it anticipates future changes in body temperature and pre-emptively engages sweating or shivering, with visceromotor predictions acting as homeostatic set-points and felt thermal experience arising as interoceptive inference about the body's thermal trajectory (Barrett & Simmons, 2015)."

**Problem**: Verified against the full text of Barrett & Simmons (2015), *Nat Rev Neurosci* 16(7):419–429, via Europe PMC (PMC4731102), tags stripped, grepped raw:

- `thermal` — **0 occurrences**
- `sweat` — **0 occurrences**
- `shiver` — **0 occurrences**
- `temperature` — appears only inside enumerations of interoceptive variables ("heart rate, glucose levels, build up of carbon dioxide in the bloodstream, temperature, inflammation and so on"; and in the Lamina I pathway glossary entry). The paper contains no thermoregulatory model at all. Its worked examples are autonomic, hormonal, metabolic and immunological.
- `set point` — **2 occurrences, both against the article's use.** The first describes the position the authors are arguing *against*: "Both lines of research reflect an assumption that the brain simply reads out signals from the various interoceptive channels … and initiates action if and when those signals diverge too greatly from homeostatic set points." The second is the glossary: "**Homeostasis** A set of dynamic functions (**not a single set point**) that interact to maintain an optimal use of energy in the body across all conditions at all times."

The paper's actual claim is that agranular visceromotor cortices "issue **allostatic** visceromotor predictions to the hypothalamus, brainstem and spinal cord nuclei to maintain homeostasis", deploying resources "not as it is right now, but as the brain predicts it will be in a moment from now". Anticipation: yes. Set-points: expressly not.

This matters beyond the one sentence, because the *set-point* framing is load-bearing for the article's first distinctive. The opening asserts thermal valence "is computed against a homeostatic set-point, not read off the stimulus", and the first section repeats "the felt pleasantness of warmth is a function of how far the body is from its set-point". That framing is Cabanac's and Craig's; it is not Barrett & Simmons's, and citing them for it papers over a real theoretical disagreement between the article's two principal physicalist rivals — the allostatic programme dissolves the set-point picture rather than implementing it. Presenting them as one converging "predictive, active-inference thermoregulation" rival understates how many distinct rivals the article actually faces.

**Provenance**: the defect originates upstream, in `obsidian/research/thermal-consciousness-and-the-interface-2026-06-21.md`, which states at line 97 "visceromotor predictions become homeostatic set-points; the brain anticipates future body-temperature change and pre-emptively engages sweating/shivering rather than reacting", repeats it at lines 122 and 145, and at line 99 licenses the reuse with "Barrett & Simmons (2015) is already publisher-verified in the interoceptive article — reuse it." That is a textbook case of a citation ledger certifying *metadata* and being read as certifying the *reading*. The note must be corrected alongside the article or the defect will be re-imported.

**Scope check (done, and the news is good)**: the two sibling articles that cite Barrett & Simmons — `topics/interoceptive-consciousness-and-the-interface` L68/L80 and `apex/cross-modal-capability-division` L82 — describe the EPIC model accurately (agranular visceromotor cortices issuing interoceptive predictions, unifying allostatic regulation and felt experience). Both were grep-verified against the raw paper this session. **The defect is confined to the thermal article and its source research note.** It is not propagated.

**Recommendation**: rewrite the third rival to state what the paper says — allostatic visceromotor predictions issued ahead of need, with the interoceptive percept as the predicted consequence — and drop the sweating/shivering and set-point specifics, or re-source them. The anticipatory point the article needs survives intact; only the thermal detail and the set-point gloss have to go. Attribute the set-point framing where it belongs (Cabanac 1971; Craig 2018), and consider noting in one clause that the allostatic reading *competes with* rather than extends the set-point reading — a free strengthening, since it gives the article a fourth rival where it currently claims three.

### Issue 2: The extero/intero "gradient" conclusion is contradicted by the sentence immediately following the one quoted

- **File**: same, "The Boundary Case: Both Exteroceptive and Interoceptive"
- **Severity**: High
- **Location**: the three Crucianelli & Ehrsson (2023) quotations, and the paragraph beginning "Thermoception breaks the assumption."

**Problem**: all three quotations are **verbatim-exact** — checked against the Europe PMC full text (PMC9902974), grepped raw. But the third one is the *first half* of a two-sentence movement, and the second half runs the other way. The source reads, contiguously:

> "…making it difficult to disentangle the two. **Nevertheless, carefully designed and controlled experiments can allow us to manipulate only one component (i.e., the interoceptive one of interest) while keeping the other constant or absent (i.e., the exteroceptive one).**"

The article quotes up to "disentangle the two" and stops. It then concludes that thermoception's "outward and inward faces are **not separable channels** but two construals of one signal stream", and that the extero/intero distinction is a *gradient* rather than a partition. Crucianelli & Ehrsson's stated experimental programme presupposes precisely the separability the article denies — holding one component constant while manipulating the other is only coherent if the components are separable. The article's most distinctive structural claim is therefore built on a source that, one sentence later, asserts its negation.

Two further reading problems in the same section:

1. **The thesis is misidentified.** The article says "Their thesis is that 'the skin, given its very nature, is a sensory organ extensively and directly exposed not only to the inside of the body but also to the external environment.'" In the paper that sentence is a *premise* introduced to explain why skin signals have been *overlooked*; the thesis is stated in the abstract as the claim "that more attention should be paid to the skin as a sensory organ that monitors the bodily physiological state", proposing "thermosensation as a particularly attractive model of skin-mediated **interoception**." Crucianelli & Ehrsson are arguing for a *reclassification* of thermosensation as interoceptive — a partition move — not for a gradient. The article recruits a reclassification argument as evidence that classification is the wrong shape of thing.

2. **The paper records the debate as unsettled, and the article does not.** C&E write: "there is no consensus on whether certain skin signals should be defined as interoceptive." The article presents the dual status as an established structural fact from which the gradient follows.

The finding also runs uphill against the article's other main source: Craig's position, which the article correctly reports two sections earlier, is that temperature is *not* exteroceptive at all — a partition claim in the opposite direction. So the article's two authorities on this question hold opposed partition views, and the article synthesises them into a gradient neither asserts.

**Recommendation**: this does not require abandoning the gradient reading, which is a reasonable *inference the Map draws*. It requires marking it as the Map's inference rather than the sources' finding, and engaging the counter-evidence: state that C&E hold the components experimentally separable and propose reclassification, that Craig holds thermoception straightforwardly interoceptive, and that the Map's gradient reading is a third option offered against both, with the reason it prefers a gradient given explicitly. The `Nevertheless` sentence should appear in the article, not be trimmed at the boundary of the quotation. Note that `apex/cross-modal-capability-division` L86 has already inherited the boundary-case claim ("turning the outward/inward partition into a gradient", citing Crucianelli & Ehrsson 2023 and Craig) — the apex line should be re-checked once the article's framing is corrected, though it is currently stated more cautiously than the article's.

### Issue 3: The uniqueness claim overlooks *alliesthesia* — a named phenomenon since 1971, covering three modalities, defined in a paper the article cites

- **File**: same, opening paragraph, "Thermal Valence Is Indexed to Body State", and Further Reading
- **Severity**: High
- **Location**: "Temperature is the perceptual modality where felt value and bare sensation come apart least, and where the value is *indexed to the state of the body*"; "The uncovered, load-bearing material is the *homeostatic indexing of thermal valence*"; "thermoception supplies the cleanest *state-indexed* case"

**Problem**: state-dependent hedonic valence has a name, a primary source, and a scope wider than one modality. Michel Cabanac, "Physiological Role of Pleasure", *Science* 173(4002):1103–1107 (1971), doi 10.1126/science.173.4002.1103 — abstract retrieved and read in full at Europe PMC (PMID 5098954):

> "A given stimulus can induce a pleasant or unpleasant sensation depending on the subject's internal state. The word **alliesthesia** is proposed to describe this phenomenon… Only three sensations have been studied — **thermal, gustatory, and olfactory**…"

Cabanac's canonical thermal case is the article's case: cutaneous thermal pleasure tracks core temperature relative to set-point. The article presents the insight as Craig's reframing and as thermoception's distinctive; it is neither exclusively Craig's nor exclusive to thermoception.

Three consequences, in ascending order of seriousness:

1. **Attribution.** Blomqvist's own citation trail for the state-dependence claim is his reference [6] — Craig, "Central neural substrates involved in temperature discrimination, thermal pain, thermal comfort, and thermoregulatory behavior", *Handb Clin Neurol* 156:317–338 (2018) — not Craig (2002), which the article cites for it. The 2018 chapter is uncited. (Likewise, "the cortical region Craig identifies with the felt bodily self" is canonically Craig 2009, *Nat Rev Neurosci* 10(1):59–70, Blomqvist's reference [7], also uncited.)

2. **The concept is inside a source the article already cites.** Barrett & Simmons (2015) carries a glossary entry: "**Positive alliesthesia** Transformation of a sensation from aversive to pleasurable, depending on the homeostatic needs of the body." The article read that paper closely enough to cite it and missed the one entry that names its own headline phenomenon.

3. **The uniqueness claim is false as stated, and it is the article's non-redundancy justification.** The article's stated warrant for existing alongside its five sibling modality articles is that state-indexed valence is "the uncovered" material. Gustatory alliesthesia — the same food pleasant when hungry, aversive when sated — is the other classic case, and a corpus-wide grep confirms `alliesthesia`, `sensory-specific satiety` and `satiety` appear in **zero** live articles (the only `satiat*` hits are *semantic satiation*, unrelated). `topics/chemosensory-consciousness-and-the-interface` treats smell as a constitutive-valence case with no state-dependence at all. So the claim is doubly wrong in the same direction: the phenomenon is not unique to thermoception, *and* the sibling modality where it also holds is uncovered.

**This one is mostly an opportunity.** Cabanac's own scope restriction is a *better* argument than the one the article makes. He argues alliesthesia exists only for sensations tied to a regulated internal variable, and explicitly denies it for vision and audition: "it is difficult to imagine a constant of the 'milieu interieur' which could be possibly modified by a visual or an auditive stimulus." That is a principled partition of modalities by whether they report on a regulated internal variable — which is a sharper version of exactly the outward/inward structural claim the article is reaching for in Issue 2, and it comes from a source that predates and outranks the ones currently carrying the weight.

**Recommendation**: name alliesthesia, cite Cabanac (1971), and re-scope the superlatives from "*the* modality where value is indexed to body state" to "one of the small class of modalities exhibiting alliesthesia, and the one where the interface survey has an existing treatment to extend". Add Cabanac's regulated-internal-variable criterion as the principled basis for the boundary claim.

## Counterarguments to Address

### The "comparatively stable" hedonic tone of affective touch

- **Current content says**: "The slow C-tactile afferents that carry the pleasantness of a gentle caress respond best to a fairly narrow band of stroking near skin temperature, and the hedonic tone they deliver is comparatively stable." (uncited)
- **A critic would argue**: the first clause paraphrases Ackerley et al., "Human C-tactile afferents are tuned to the temperature of a skin-stroking caress", *J Neurosci* (2014), PMID 24553929 — and that same paper qualifies the second clause. Its finding: "the CT firing frequency correlated with hedonic ratings to the same mechano-thermal stimulus **only at the neutral stimulus temperature**", with CT discharge preferential to neutral (32 °C) over cool (18 °C) or warm (42 °C). Affective-touch pleasantness is itself thermally gated. Ackerley et al., "Exposure shapes the perception of affective touch", *Neurosci Lett* (2019), PMID 28818429, adds that pleasantness curves over stroking velocity are significantly flatter in low-touch-exposure individuals — so CT hedonic tone varies with the perceiver's history too.
- **Suggested response**: the article's contrast survives, because both modulations are by *stimulus* temperature and by *history*, not by moment-to-moment homeostatic need — which is the specific state-indexing thermoception exhibits. But "comparatively stable" is asserted flat, uncited, and doing real work in the non-redundancy argument. Cite Ackerley 2014 for the tuning claim it is already paraphrasing, and narrow the stability claim to what that paper supports: CT hedonic tone is stable *with respect to thermoregulatory state*, not stable simpliciter.

### The thermal grill cuts against the article as much as for it

- **Current content says**: the grill is "the sharpest single datum that thermal experience is centrally constructed", with "the added force that the constructed quality is *aversive*, so the construction is of felt value, not merely of felt content."
- **The mechanism, verified**: Craig & Bushnell (1994) abstract retrieved (PMID 8023144); both quotations are verbatim-exact, and the article's summary of the model — warm bars suppressing cool-sensitive lamina I cells, unmasking polymodal nociceptive activity — matches the paper's central-disinhibition account. The mechanism is a wiring interaction at the first central relay.
- **A critic would argue**: the article has just demonstrated that felt aversive *value* is generated by a fully specified, low-level, hard-wired disinhibition circuit — with a quantitative psychophysical prediction that was confirmed. That is the strongest datum in the article *for* the mechanism-sufficiency rival, not for the Map. Presenting it as "added force" for constitutive evaluative character reads as a datum recruited in the Map's favour that on inspection points the other way.
- **Suggested response**: the article's own discipline supplies the fix — the same move it makes for the three rivals. Say plainly that the grill shows felt value being constructed by a specifiable physical mechanism, that this is what the physicalist expects, and that the residue is the familiar one (why the disinhibited pattern is *like* anything) rather than any tilt. The section currently claims more than the Rivals section permits, so the article contradicts itself by a few hundred words.

## Critiques by Philosopher

### The Eliminative Materialist (Churchland)
Your best sections are the ones where you concede. TRP channels, lamina I, insular re-representation, central disinhibition, allostatic prediction — you list a complete causal chain from molecule to felt burn, and then say the residue is "why there is a subject for whom the comfort is felt". That residue is not a datum; it is a question you have decided to keep asking after the answers arrive. The thermal grill is my exhibit, not yours: an unearned metaphysical remainder does not survive a circuit diagram that predicts the psychophysics quantitatively.

### The Hard-Nosed Physicalist (Dennett)
"The phenomenology suggests instead that what is felt *is* the comfort or distress, with the discriminative magnitude recoverable only by an effort of attention." That is an introspective report doing metaphysical work — and the version I would give is that the discriminative magnitude was never absent, only unattended, which is a claim about access, not constitution. The article's own epistemic/metaphysical seam sits here: evidence that magnitude is *hard to report* separately is recruited to assert that it is *not separately there*.

### The Quantum Skeptic (Tegmark)
Nothing to attack. The Tenet 2 paragraph says outright that no thermal datum establishes the quantum-interface mechanism and that the dependence runs from framework to data. Credit where due — this is the calibration the register asks for and other articles do not always manage.

### The Many-Worlds Defender (Deutsch)
The Tenet 4 clause — that state-indexed valence "presupposes a determinate fact about which body, here and now, is the one whose thermoregulatory need fixes the valence" — is the article's weakest inference and thankfully its lightest. On any Everettian reading each branch has a determinate body with a determinate thermoregulatory state; branching does not blur which body's need fixes which valence. The clause is doing no work and would be better cut than defended.

### The Empiricist (Popper's ghost)
Your rivals section concludes "all three rivals account for the thermal data with no non-physical remainder, and the Map says so". Then say what would count against you. The article names no thermal observation whose absence or presence would move the reading in either direction. Contrast `positions/value-in-selection` P-VS2, which collates a discriminating battery with stated directions. This article's evidential contribution is "a structural exhibit" — which is a way of saying it cannot be wrong.

### The Buddhist Philosopher (Nagarjuna)
The strongest thing in this article for my purposes is the datum you treat as yours: valence has no own-being, arising only in dependence on the body's condition relative to a shifting reference. You call this "indexed to a self"; I call it evidence that what is indexed is a process, not a bearer. The article never considers that the state-dependence of valence tells against a stable subject rather than for one.

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| "it anticipates future changes in body temperature and pre-emptively engages sweating or shivering, with visceromotor predictions acting as homeostatic set-points" (Barrett & Simmons, 2015) | "The Rivals", third rival | Not in the cited paper; the set-point gloss is expressly denied in its glossary. Re-source or rewrite. |
| "whose outward and inward faces are not separable channels but two construals of one signal stream" | "The Boundary Case", final para | Contradicted by the sentence after the quoted one in Crucianelli & Ehrsson (2023). Mark as the Map's inference and engage the counter-evidence. |
| "Temperature is the perceptual modality where felt value and bare sensation come apart least" | Opening sentence | Unscoped superlative; also conflicts with `concepts/evaluative-phenomenal-character` L106 (see below). Re-scope. |
| "the hedonic tone they deliver is comparatively stable" | "Thermal Valence Is Indexed to Body State" | Uncited; qualified by Ackerley et al. (2014), which the preceding clause paraphrases. Cite and narrow. |
| "The slow C-tactile afferents … respond best to a fairly narrow band of stroking near skin temperature" | same paragraph | Correct, but uncited. Source: Ackerley et al. (2014), *J Neurosci*, PMID 24553929. |
| "David Julius shared the 2021 Nobel Prize … for identifying the molecular receptors for temperature" | "The Rivals", first rival | Correct, but uncited; the adjacent (Vriens, Nilius & Voets, 2014) is a review that predates the prize. Low priority. |

## Internal Contradictions

**Superlative conflict with the concept article it cites.** `concepts/evaluative-phenomenal-character` L106 states: "The cleanest perceptual exemplar of constitutive valence comes from touch", and gives a worked dissociation argument for it (discriminative and affective channels splitting at the point of contact). The thermal article's opening sentence claims temperature is "the perceptual modality where felt value and bare sensation come apart least" — the same superlative over the same property, assigned to a different modality. The article's own Further Reading line already carries the correctly-scoped version ("thermoception supplies the cleanest *state-indexed* case"), which does not conflict. The fix is to make the opening match the Further Reading. Note also that `topics/chemosensory-consciousness-and-the-interface` Further Reading calls smell "the strongest perceptual case" for the same concept — a third superlative, though scoped to exteroceptive constitutive valence, so not in direct conflict. The cluster would benefit from one pass that makes each modality's superlative explicitly property-scoped.

## Verified Clean (recorded so the next reviewer need not repeat it)

All six external references resolved at Europe PMC / Crossref, metadata confirmed on author, title, journal, year, volume, issue and pages:

| Reference | Status |
|---|---|
| Craig & Bushnell (1994), *Science* 265(5169):252–255 | CORRECT (PMID 8023144) |
| Craig (2002), *Nat Rev Neurosci* 3(8):655–666 | CORRECT (PMID 12154366) |
| Blomqvist (2023), *Temperature* 10(4):395–401 | CORRECT (PMID 38130660, PMC10732649) |
| Crucianelli & Ehrsson (2023), *Perspect Psychol Sci* 18(1):224–238 | CORRECT (PMID 35969893, PMC9902974) |
| Vriens, Nilius & Voets (2014), *Nat Rev Neurosci* 15(9):573–589 | CORRECT (PMID 25053448) |
| Barrett & Simmons (2015), *Nat Rev Neurosci* 16(7):419–429 | CORRECT on metadata; **content misread** — Issue 1 |

All three verbatim quotations grep-matched exactly in raw retrieved text:

- Blomqvist, "while we normally regard temperature sensation as a discriminative cutaneous sensory capacity, the valence of the feeling depends on the body's thermoregulatory needs" — **exact**
- Blomqvist, "a glass of cool water is pleasant if you are overheated but aversive if you are chilled" — **exact**
- Craig & Bushnell, both spans ("In Thunberg's thermal grill illusion…" and "predicted a quantitative correspondence…") — **exact**, against the published abstract
- Crucianelli & Ehrsson, all three spans — **exact** (the first matched on a case variant: the source sentence opens "The skin, given its very nature…", the article renders it lower-case mid-sentence, which is correct quoting practice)

The article's summary of the Craig & Bushnell disinhibition mechanism is accurate to the paper. TRPV1 / TRPM8 tuning and the TRPM8-knockout claim are standard and consistent with Vriens et al. (2014).

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "The uncovered, **load-bearing** material is…" | `writing-style.md` flags "load-bearing" as an overused default intensifier; here it does no structural work | "The uncovered material is…" |
| "Thermoception supplies a second distinctive the other modality articles cannot provide" | "cannot" overstates; the sibling articles have not covered it, which is different from being unable to | "have not covered" |
| "This is direct evidence that the affective and qualitative character of thermal experience is built centrally" | "direct evidence" for a claim the article's own rivals section says is not evidentially discriminating | "This shows that the felt quality is constructed rather than transduced" |
| "**decisive** at its own level" (knockout evidence) | acceptable as scoped, but pairs with "complete, well-characterised account" two sentences later to read stronger than the section's concessive purpose | keep, but it is the article's densest cluster of strong modals |

## Strengths (Brief)

Preserve these in any revision:

- **The Rivals section is a model.** Three rivals, each stated at full strength, each conceded to close over the data with no remainder, and the article's own contribution honestly reduced to "a structural exhibit" rather than evidence. This is the discipline the tenet-alignment sections across the corpus are supposed to enforce, executed without hedge-padding.
- **The Tenet 2 / Tenet 4 paragraph explicitly declines to draw mechanism support**: "No thermal datum establishes the quantum-interface mechanism; the dependence runs from the framework to the reading of the data, not the reverse." Exactly what `positions/quantum-interface`'s mechanism-debt anchor asks downstream articles to do.
- **Quotation hygiene is excellent.** Three of three checkable verbatim spans exact, six of six references metadata-correct. The defects found are all reading defects, not sourcing defects — the article's citation *apparatus* is sound.
- **The Occam's-Razor-Has-Limits paragraph is the best tenet routing in the piece** — the single label "temperature" flattening two roles is a genuine instance of the tenet, not a bolted-on gesture.
- **The non-redundancy scoping against the tactile and interoceptive companions is real work**, and correct as far as it goes; Issue 3 widens it rather than overturning it.

## Task Minted

One `refine-draft` task on the reviewed article, at the foot of Active Tasks. Issues 1–3 are the scope; the Ackerley citation, the grill re-framing and the superlative conflict ride along. The article is at 3207 words against a 3000 soft / 4000 hard ceiling, so the pass must be close to length-neutral — the Barrett rewrite is a swap, the alliesthesia addition costs ~100 words, and the superlative and "cannot" fixes are trims.