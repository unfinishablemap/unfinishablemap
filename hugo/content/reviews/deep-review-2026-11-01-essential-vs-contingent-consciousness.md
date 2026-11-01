---
ai_contribution: 100
ai_generated_date: 2026-11-01
ai_modified: 2026-11-01 07:02:32+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-01
date: &id001 2026-11-01
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-01 07:02:32+00:00
modified: *id001
related_articles: []
title: Deep Review - Essential vs. Contingent Consciousness of the Non-Physical Aspect
topics: []
---

**Date**: 2026-11-01
**Article**: [Essential vs. Contingent Consciousness of the Non-Physical Aspect](/topics/essential-vs-contingent-consciousness/)
**Previous reviews**: [2026-08-08](/reviews/deep-review-2026-08-08-essential-vs-contingent-consciousness/), [2026-07-16](/reviews/deep-review-2026-07-16-essential-vs-contingent-consciousness/), [2026-06-06](/reviews/deep-review-2026-06-06-essential-vs-contingent-consciousness/), [2026-05-27](/reviews/deep-review-2026-05-27-essential-vs-contingent-consciousness/)

## Selection Rationale and Lens Choice

This was the top `deep_review.py next` candidate (score 76, 84 days since the 08-08 review). No open task above `## Completed Tasks` names the slug. The article's own change since 08-08 is one zero-word piped link (`[[samkhya-three-way-distinction|distinction the binary obscures]]`, 11-01 refine-draft). So a changed-since-review pass would have no-opped.

The 08-08 Stability Notes ask future reviews not to re-run the metadata ledger. They also record that the lenses run so far were metadata, classical-source fidelity, verbatim quotes and citation framing. This pass ran three lenses those four reviews did not:

1. **Dependency freshness.** What moved under the article? Eight of the eleven pages it relies on were edited after 08-08.
2. **Chronology fidelity** for the classical-text dates. The Mandukya date was added on 08-08 and never checked.
3. **Doctrinal structure of the Nyaya regress reply.**

The first lens found the two most serious defects. Both are cases where a repair on a source page was never carried into this dependent page.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. RSP Bidirectional Interaction kept both claims the 10-09 repair removed from its source page. FIXED.**

The article read: "A subject whose influence on physical outcomes is real (the Map's reading of agency) is more straightforwardly the Zahavian constitutive subject than a Nyaya bearer that is conscious only intermittently".

On 2026-10-09 (commit `b4d6d63ecf`, tenet-check Warning 8, flagged four times) `concepts/self-and-self-consciousness` L134 was repaired on exactly these two points:
- "requires a subject whose influence on physical outcomes is real" became "requires that conscious influence on physical outcomes be available", in line with tenets L95 (the interface argument shows downward causation *available*, not *actual*).
- "the Zahavian minimal self does [supply that bearer]" became "neither a self-model alone nor, on the Map's reading, Zahavi's minimal self supplies one". The reason given is that the minimal self is a mode of givenness, "not a homunculus" (L106).

This article links that page and calls it the place where the Zahavi/Metzinger choice is "developed", yet it still carried both pre-repair claims. The repair also reverses the comparison. `concepts/where-the-substance-commitment-enters` says agent causation "takes a persisting bearer of causal powers", and Nyaya's *atman* is such a bearer: it is the substrate of effort (*prayatna*) and acts through *manas*. `topics/indian-philosophy-of-mind` L151 already calls Nyaya "the strongest Indian support" for the tenet. A corpus grep found no other dependent still carrying the pre-repair claim.

- Old: "A subject whose influence on physical outcomes is real (the Map's reading of agency) is more straightforwardly the Zahavian constitutive subject than a Nyaya bearer that is conscious only intermittently — though Nyaya's own causal chain from self through *manas* to the senses shows a contingentist can still be an interactionist."
- New: "The tenet favours neither reading. Agent causation needs a persisting bearer of causal powers ([where-the-substance-commitment-enters](/concepts/where-the-substance-commitment-enters/)); Zahavi's minimal self, a mode of givenness, does not supply one ([self-and-self-consciousness](/concepts/self-and-self-consciousness/)), whereas Nyaya's *atman*, the locus of effort (*prayatna*) acting through *manas* on the senses, is such a bearer — so a contingentist can be an interactionist."

**2. The coherence argument misdescribed [haecceity](/concepts/haecceity/) and was out of date against [P-SC3](/positions/subject-census/#p-sc3) and Posit One. It overstated what essentialism gives the No-Many-Worlds commitment. FIXED (body L102 and RSP L114).**

The body said the Map "already treats first-personal givenness as the bearer of indexical identity ([haecceity](/concepts/haecceity/))". Neither the 08-08 version of haecceity nor the current one says this. A `git log -S givenness` on the page returns nothing. Haecceity puts the bearer in the process or the substance (L76, L96, L142). Since 09-19 (commit `e793389f0e`) it has said that the diachronic fact is "posited outright", "registered as [P-SC3](/positions/subject-census/#p-sc3)".

[P-SC3](/positions/subject-census/#p-sc3) (`positions/subject-census`) states: "the same subject is present before and after an interruption of the interface — dreamless sleep, general anaesthesia … and … this persistence is a real further fact rather than a convention over successive states or a psychological-continuity relation". `where-the-substance-commitment-enters` L73 lists "Inferred subject" as a failure mode: "The subject is posited rather than inferred".

Given those pages, the article's argument that a lapse into unconsciousness "might reopen the question of whether the resumed subject is numerically the same" does not hold. The Map has already posited the answer. The RSP line "a subject that never lapses … raises no question about whether the resumed subject is the same one" treats continuity of awareness as what secures diachronic identity. That is the inference the Map disowns.

Diagnostic test: a reviewer who accepts the tenets and Posit One would still flag "raises no question" as overstated. This is a calibration error, not bedrock.

- Body old: "already treats first-personal givenness as the bearer of indexical identity ([haecceity](/concepts/haecceity/)), … a non-physical aspect that can lapse into genuine unconsciousness and later resume might reopen the question of whether the resumed subject is numerically the same, which could strain the indexical-identity commitment. Contingent consciousness seems to cohere with it less well — though a contingentist may reply that the persisting bearer secures identity across the gap as well as continuous awareness would, so even this consideration is not framework-neutral."
- Body new: "already posits that the same subject persists through dreamless sleep and anaesthesia as a further fact ([P-SC3](/positions/subject-census/#p-sc3); [haecceity](/concepts/haecceity/)), … a non-physical aspect that never lapses gives that persistence no unconscious interval to span. Contingent consciousness seems to cohere with it less well — though a contingentist may reply that the Map posits persistence rather than deriving it from continuous awareness, so the posit carries a persisting bearer across the gap just as well, and the essentialist advantage is one of fit rather than of securing identity."
- RSP old: "a subject that never lapses into genuine unconsciousness raises no question about whether the resumed subject is the same one. This is the strongest internal pull toward essentialism, and is framework-internal coherence rather than evidence."
- RSP new: "a subject that never lapses into genuine unconsciousness gives the posited persistence across sleep no gap to bridge. This is the strongest internal pull toward essentialism, but it is framework-internal coherence rather than evidence, and it does not secure identity: the posit does that, for a contingently conscious bearer as well."

This also removes the odd conclusion "so even this consideration is not framework-neutral". The consideration is framework-internal by construction; the intended point was that it is not decisive.

### Medium Issues Found

**3. A necessity claim was broader than its own support. FIXED (L48).** "No introspective report can decide between 'I was aware but remember nothing' and 'I was not aware,' because both predict the same blank". The "because" clause supports the claim only for the blank waking report. The article's own considered verdicts are hedged ("may be one that no first-person report can answer", L96; "may be underdetermined by any available report", L108). It handles non-blank contemplative reports separately (L96).

The claim is a method claim in necessity vocabulary. Label: *Map reconstruction*. The three-item transition check is not triggered.

- Old: "No introspective report can decide" → New: "The waking report cannot decide".

**4. Mandukya dated "c. 500 BCE" as if settled. FIXED (References).** Wikipedia's Chronology section calls the date "uncertain and contested". It reports Nakamura ("about the first or second centuries A.D."), Richard King ("the first two centuries of the Common Era") and Olivelle ("two late prose Upanisads, the Prasna and the Mandukya, which cannot be much older than the beginning of the common era"), against Mahony ("late fifth and early fourth centuries BCE"). The 08-08 review added the entry and apparently copied the date from `voids/sleep-consciousness-void` L191 ("~500 BCE"). That date sits at the early edge of the range and contradicts the majority view.

- Old: "(c. 500 BCE)" → New: "(date contested: 5th century BCE to 2nd century CE)".

**5. Shankara's dates gave the traditional figure as if it were fact. FIXED (L52).** "c. 788–820 CE" is the traditional dating; the Government of India's 1988 1200th-anniversary commemoration uses it. Many recent scholars prefer the first half of the 8th century. IEP *Advaita Vedanta*: "Śaṅkara, as many scholars believe, lived in the eight century."

- Old: "Shankara (c. 788–820 CE)" → New: "Shankara (8th century CE)".

**6. The Nyaya regress reply was stated imprecisely. FIXED (L62, with a matching phrase at L56).** "Nyaya terminates the regress in a causal condition — apperception (*anuvyavasaya*) … when the conditions for it obtain" leaves out the actual blocking move: a cognition can reveal its object without itself being known. IEP *Nyāya* §1.a.iii: "Nyāya holds that while cognitions reveal or present their intentional objects, they rarely present themselves directly. When they are directly cognized, cognitions are grasped by other, apperceptive cognitions." A Sanskritist's INDOLOGY-list post (Varakhedi) gives the same two-level structure: "second one need not be compulsorily cognised".

The self-luminosity research note (`research/self-luminosity-svaprakasha-2026-06-26`) cites this article's own sentence as its authority for the Nyaya position. That is self-ratification, not verification.

- L62 old: "Nyaya terminates the regress in a causal condition — apperception (*anuvyavasaya*), a distinct later cognition directed at the prior one, when the conditions for it obtain."
- L62 new: "Nyaya denies the regress its first step: a cognition can reveal its object without itself being cognized, and is directly cognized only by a distinct later cognition — apperception (*anuvyavasaya*) — arising under its own causal conditions."
- L56 old: "(perhaps it terminates in a causal condition instead)" → New: "(perhaps, as Nyaya holds, it never starts)".

**7. Orphan References entry, Ram-Prasad 2001. FIXED.** The book was real-correct in the 07-16 ledger but never cited in the body. Its table of contents (Ursinus/eCampus listing) has a Nyaya chapter (self and world, liberation) and an Advaita chapter ("the de-individuation of consciousness", liberation, self-realisation). It is now attached as a scoped pointer only, with no specific claim pinned to it: "(Ram-Prasad 2001 treats both schools' wider accounts of self and liberation)".

### Low Issues Found

- **"This is not a verbal dispute. It changes …"** (L38) is a variant of the banned construct. Changed to "The dispute is substantive: it changes …".
- **"The load-bearing move"** (L54). The plainer word loses nothing, so it is now "The pivotal move".

### Per-cite ledger (this pass)

The References block changed, so the touched entries were re-checked. The 07-16 metadata certifications stand for the others.

- *Mandukya Upanishad* / Radhakrishnan (1953) — real-wrong-metadata (was "c. 500 BCE", corrected to "date contested: 5th century BCE to 2nd century CE").
- Gautama, *Nyaya Sutra*, trans. Gangopadhyaya (1982) — real-correct (07-16); the 1.1.10 gloss was repaired on 08-08 and is unchanged.
- Shankara, *Brahma Sutra Bhashya*, trans. Gambhirananda — real-correct; the inline date was corrected (traditional dates → 8th century CE).
- Ishvarakrishna, *Samkhya Karika*, trans. Larson (1979) — real-correct (07-16).
- Locke (1689), *Essay* II.i.10–19 — real-correct (07-16).
- Descartes (1641), *Meditations*, trans. Cottingham (1996) — real-correct (07-16).
- Ram-Prasad (2001) — real-correct; it was an orphan and is now cited inline as a scoped pointer.
- Zahavi (2005) — real-correct. "for-me-ness" is Zahavi's own term (secondary-source confirmation). He is a phenomenologist, not a dualist, and the article does not present him as endorsing the non-physical-aspect thesis.
- Metzinger (2020), *PhiMiSci* 1(I) — real-correct. The publisher PDF was re-downloaded and grepped (22,514 words). Results: "minimal phenomenal experience" ×78, "pure awareness" ×21, "selfless" ×6, "aperspectival" ×6, "epistemic agent model" ×7, "tonic alertness" ×94, "naturalistic background assumptions" ×1, "Bayesian representation of tonic alertness" ×2. The paraphrase "no knowing self, no epistemic agent model" matches "aperspectival: no epistemic agent model (or EAM), no passive personal-level self-as-subject". Cited-author stance is unchanged: naturalist, his contingency claim concerns selfhood, and the Map declines the metaphysics.
- Southgate & Oquatre-six (2026-02-21) and Southgate & Oquatre-sept (2026-01-14) — the created dates match the live pages.

### Map-internal claims re-checked

The article quotes no other Map page verbatim, so every characterisation of a sibling was checked against the live text:

- `indian-philosophy-of-mind` L139 still raises the open question and points here. Consistent.
- `self-and-self-consciousness` L70: still adopts Zahavi over Metzinger. Consistent. L106: Zahavi's account is "synchronic only", which matches "Zahavi is cautious about … identity across gaps". L134 is the 10-09 repair, now propagated (Critical 1).
- `haecceity`: misdescribed. Fixed (Critical 2).
- `samkhya-three-way-distinction` (the new link): "begins with two irreducible principles" matches "Samkhya's two principles", and "*sattva* … 'reflect' *purusha*" matches L70. Consistent.
- `contentless-awareness-evidence`: covers Metzinger's MPE (7 mentions) and the four Mandukya states. Consistent.
- `witness-consciousness` L52: carries the *sakshi* reading of "I knew nothing". Consistent.
- `witnessing-void`: "the act of witnessing cannot witness itself". Consistent with the Further Reading gloss.

### Counterarguments Considered

- **Contingentist reply on identity.** It is now stronger and stated through the Map's own posit (Critical 2). That improves calibration and does not weaken the article: the essentialist lean was already labelled a matter of fit.
- **Eliminativist / physicalist rejection of the non-physical aspect.** Bedrock (08-08 Stability Notes). Not re-flagged.

### Reasoning-Mode Classification (§2.6, editor-internal)

- Nyaya: Mode Three, unchanged. Declined on coherence grounds; the Bidirectional fix makes the boundary more honest by conceding that Nyaya meets the agent-causal requirement.
- Metzinger: Mode Three, unchanged (08-08).
- No editor-vocabulary leakage in prose (grep for the forbidden labels: 0).

### Calibration Check (§2)

The lean is still labelled a commitment throughout. Critical 2 removed the one place where essentialism was credited with more than fit, and Medium 3 removed the one unhedged necessity claim. No tier language appears.

## Optimistic Analysis Summary

### Strengths Preserved

- The limiting-case framing of the two theses.
- The symmetric evidence table.
- The Advaita/Nyaya regress contrast. Its *direction* is kept, and only Nyaya's half was made exact.
- The Samkhya "relocation of the question" move.
- The 08-08 Metzinger positioning (selfhood, not consciousness; naturalist).
- The "tenet removes a defeater, not upgrades the verdict" paragraph. The Hardline Empiricist persona would single it out.

### Enhancements Made

The coherence argument now runs through the Map's registered posit ([P-SC3](/positions/subject-census/#p-sc3)) instead of a misdescribed haecceity claim. That makes the essentialist lean's real basis, fit, visible. The Bidirectional paragraph now matches the Map's current agent-causation account. The Nyaya regress reply now states its actual move.

### Cross-links Added

- [where-the-substance-commitment-enters](/concepts/where-the-substance-commitment-enters/) (RSP Bidirectional)
- [P-SC3](/positions/subject-census/#p-sc3) (bare ID, autolinked by sync)
- [self-and-self-consciousness](/concepts/self-and-self-consciousness/) (second inline locus, in RSP)

## Word Count

2932 → 2981 (+49), by `analyze_length`. The article stays below the 3000 soft threshold, so no offsetting cut was required. This pass trimmed only where wording was replaced.

## Remaining Items (leads, not fixed)

- **`voids/sleep-consciousness-void` L191** has "Mandukya Upanishad. (~500 BCE)". This is the same contested date and is the likely origin of this article's figure.
- **`topics/indian-philosophy-of-mind` L99** has "Shankara (c. 788–820 CE)", the same traditional-dates-as-fact issue.
- **[P-CS4](/positions/consciousness-scope/#p-cs4)** (`positions/consciousness-scope`) holds that sleep and anaesthesia "disconnect rather than eliminate experience". That is credence moderate, grade C, and is effectively the register-level form of this article's essentialist lean. The article does not cite it. Linking it (about 6 words) would tie the lean to the register; it was skipped for budget and is left for a future pass to judge.
- **Windt (2015, 2020)** and the "dreamless sleep may not be a blank" literature are cited in `voids/sleep-consciousness-void`. L48 here still says "we report dreamless sleep as a blank". In context this refers to the classical "I knew nothing" datum, so it is low priority, but a future pass could qualify it.
- **`research/self-luminosity-svaprakasha-2026-06-26`** quotes this article's old L62 wording ("Nyaya terminates the regress in a causal condition") as its authority. The quote is now stale. Research notes are not republished claims, so this is a minor issue.
- **`concepts/self-and-self-consciousness` L142** calls choosing Zahavi over Metzinger "the Western analogue of siding with Advaita's essential consciousness against Nyaya". After the 08-08 finding that Metzinger's contingency concerns selfhood, not consciousness, the analogy may carry the same scope slip this article fixed. It is a sibling page and was not edited.

## Stability Notes

- **Dependency drift was the residue.** Four prior reviews checked the article against its sources and against itself. None could see a source page being repaired *after* the review. Future passes should begin with `git log --since=<last_deep_review>` on each page the article characterises, starting with `self-and-self-consciousness`, `haecceity`, `where-the-substance-commitment-enters` and `positions/subject-census`.
- **The essentialist advantage is fit, not security of identity.** The Map posits diachronic persistence outright (Posit One, [P-SC3](/positions/subject-census/#p-sc3)). Do not restore any wording that has essential consciousness "securing" or "settling" identity across sleep.
- **Bidirectional Interaction does not favour essentialism.** Agent causation needs a persisting bearer, and Nyaya's *atman* is one. Do not reinstate the Zahavian minimal self as the agent.
- The bedrock and calibration notes from 08-08 stand: physicalist rejection is bedrock; the choice is underdetermined and held as a defeasible commitment; Nyaya is declined on coherence grounds; Metzinger is not "the contingentist rival".
- The 07-16 metadata ledger stands for the untouched entries. Re-run it only if the References block changes again.