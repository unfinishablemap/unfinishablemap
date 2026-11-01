---
ai_contribution: 100
ai_generated_date: 2026-11-01
ai_modified: 2026-11-01 01:17:34+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-01
date: &id001 2026-11-01
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-01 01:17:34+00:00
modified: *id001
related_articles: []
title: Deep Review - Experiential Alignment
topics: []
---

**Date**: 2026-11-01
**Article**: [Experiential Alignment](/concepts/experiential-alignment/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-experiential-alignment/) (sixth deep review; also [pessimistic 2026-07-18](/reviews/pessimistic-2026-07-18-experiential-alignment/))

Seventh deep review. Three refine passes landed after the 07-19 review without a deep review: 07-27 (`78f9e36480`, patienthood/agency collapse, one Further Reading gloss), 07-30 (`b1adfdf1a6`, corpus-wide Tallis de-quote, one body sentence), and 09-21 (`60ca7f5447`, the Measurement Protocol's representational-error paragraph). This pass checked each in context, ran the calibration lenses the driver named, and ran the result-direction and subject legs of §2.4, which no prior review of this page had run. The prior Stability Notes were honoured. The three 07-18 findings stay resolved, and every bedrock disagreement is left as it was.

## Pessimistic Analysis Summary

### Diff check (since `1889f90d78`)

- **07-27 Further Reading gloss** (`ethics-under-dualism`). The agency half reads correctly: the target says "Moral agency requires causal efficacy" (L202). The patienthood half still collapses a distinction the target draws: "Moral patienthood extends to every being capable of valenced experience… Consciousness is the wider bar" (L109, [P-MS1](/positions/moral-status/#p-ms1)). This is the same collapse class the 07-27 pass was fixing. **Fixed**: "How consciousness grounds moral patienthood" → "How valenced experience grounds moral patienthood".
- **07-30 Tallis de-quote**. The page carries no quotation marks around any Tallis wording, so no residual verbatim survives. The unquoted paraphrase "illusions presuppose experience" is faithful: it is the verbatim *Philosophy Now* 161 sentence "all illusions presuppose experience" minus "all". But the sweep **did not repoint the work** here, although it did so at `arguments/functionalism-argument`. References still pinned the claim to *Aping Mankind* (2011), and that book does not contain the article's wording. **Fixed** (see ledger).
- **09-21 representational-error paragraph**. It is faithful to its source (`topics/representation-adequacy-and-irreversible-intervention` L61, "proxy and target then agree on everything observable"). Two defects appear on transplant. (i) "a learned construct" has no antecedent on this page. (ii) "proxy" here means a measurement method, while in the source it means the learned construct, so "proxy and target agree" muddles the sentence. Also, "agree on every observable… nothing diverges" is an unscoped claim of absence: triangulation can only see divergence among what is *measured*. **Fixed**: "the system's learned construct… construct and target agree on everything measured and nothing diverges". The argument is unchanged and the scope is now accurate.

### Critical Issues Found

1. **Result-direction contradiction, K&D 2010** (What Would Challenge point 2). The page said "preference satisfaction correlates with life satisfaction but **not** moment-to-moment experience (the 'focusing illusion')". The cited paper says "Emotional well-being also rises with log income, but there is no further progress beyond an annual income of ~$75,000". The paper is also about *income*, not preference satisfaction. Killingsworth, Kahneman & Mellers 2023 (*PNAS* 120(10) e2208661120) has since confined the plateau to the least-happy group. What does survive is the abstract's "emotional well-being… and life evaluation… have different correlates". The 05-25 review checked only the *attribution* of "focusing illusion" ("loose but legitimately Kahneman's"), never the direction of the claim. **Fixed**: "how people evaluate their lives and how their days feel have different correlates (Kahneman & Deaton 2010)". The uncited "focusing illusion" label was dropped. That phenomenon is real (Schkade & Kahneman 1998), but it was attached to the wrong finding, and re-attaching it correctly would cost about 14 words the budget did not have.
2. **Training Argument: phenomenology offered as evidence against illusionism** (lenses b/e, calibration). The premise "If phenomenal states were illusory, training… should not improve access to them" misdescribes illusionism. Fox et al. measured agreement between subjective tactile-sensitivity ratings for 20 body regions and *population-averaged* objective norms (S1 representation size, two-point threshold). Illusionism accommodates that equally well: introspective representations can track bodily states better with nothing phenomenal presented. "Consistent with phenomenal content being genuinely accessible" is evidentially empty when the finding is equally consistent with the denial. A tenet-accepting reviewer would still flag this, so it is a calibration error. **Fixed**: the subsection now states what was measured, keeps the logarithmic and cross-sectional qualifiers, says explicitly that the result does not count against illusionism, and says what it does bear on (the trustworthiness of reports).
3. **Measurement Protocol treats meditators' reports as calibrators** (lens a). "Meditators appear to distinguish hedonic valence, attention quality, and agency with greater precision than untrained subjects (see Contemplative Evidence below), potentially providing calibration data." The linked section contains only practitioners' self-reports, so introspection was certifying introspection. The one study the page cites tests tactile sensitivity, not valence, attention or agency. **Fixed**: the bullet now states the tactile finding, links to the Training Argument, and says that on valence, attention quality and agency "their reports still need calibrating".

### Medium Issues Found

- **"These are direct phenomenological observations"** (Witness Consciousness, lens a). It treated practitioner reports as transparent access, against the Map's grading that introspective judgement is fallible and theory-shaped. **Fixed**: "fallible, tradition-shaped first-person reports rather than inferences from behaviour".
- **Frankish's term attached to the wrong subject** (Regress Response). "*quasi-phenomenal* introspective representations" was wrong: Frankish's quasi-phenomenal properties are physical properties of the states that introspection misrepresents, not the representations themselves. This matches the Map's own `concepts/illusionism` L105. **Fixed**: "replaces phenomenal properties with *quasi-phenomenal* ones—physical properties of brain states that introspection *misrepresents*…". The next sentence's misrepresentation-as-relation argument is unaffected.
- **Falsifier 5 self-sealing** ("The Map's haecceitism rules this out"). This is the same Medium defect class the 07-18 pessimistic review fixed in points 1 and 4; point 5 was missed. **Fixed**: "The Map's haecceitism denies this; an argument that a subject's thisness carries no weight against aggregation would remove the floor's stated ground." This does not reopen the bedrock haecceity/MWI dispute. It only makes the defeat condition statable.
- **Tenet 5 used as a positive licence** (lens f). "experiential alignment's difficulty reflects the genuine difficulty of the target, not a defect" asserted what Tenet 5 can only leave open. **Fixed**: "may reflect… rather than", which matches the clause before it ("consciousness may be exactly such a boundary").
- **Unscoped claim of absence, jhana** (lens d). "a phenomenological precision preferentist frameworks cannot capture" overreached: a preferentist could rank the jhanas among themselves. **Fixed**: "such a survey does not record", scoped to the survey just described.

### Low Issues

- **Whitehead gloss** "irreducible to comparative rankings" put the Map's contrast inside Whitehead's mouth. **Cut** (−4 words). The next sentence already does the Map's work.

### Publisher-of-Record Citation Ledger (this pass)

The full metadata ledger from 2026-06-24 stands for entries not listed here (Kahneman 1999, Rawlette 2016, Varela 1996, Zhi-Xuan et al. 2024, Garrabrant 2017, Whitehead 1929, Russell 2019: all real-correct, metadata unchanged).

- Tallis 2011 (*Aping Mankind*) — **real-correct metadata, wrong work for the inline wording; replaced**. Google Books search-within on live id `Lk37CwAAQBAJ` (control queries "Neuromania"/"Darwinitis" hit; the p.9 snippet mentions *The Explicit Animal* "twenty years ago") finds a *cognate* argument, "presupposes prior presentation. For example, my face in a mirror…", aimed at representationalism. It finds 0 hits for "misrepresentation presupposes" and no "illusions presuppose experience". The book also predates Frankish 2016, the target of the article's sentence. It is not fabricated, and a future pass must not call it so.
- Tallis 2024, "The Illusion of Illusionism", *Philosophy Now* 161 (April/May 2024), "Tallis in Wonderland" column — **real-correct, installed as ref 9**. I fetched the raw publisher HTML with `curl` and stripped tags two ways. Tag-to-nothing: "all illusions presuppose experience" ×1 and "misrepresentation presupposes presentation" ×1. Tag-to-space: the second phrase returns **0**, reproducing the split-word artifact recorded in memory. Issue date is from the issue TOC ("Issue 161: April/May 2024") and the page's JSON-LD (datePublished 2024-04-08). The corpus's "58-59" page range is **not shown on the publisher's web page**, so it was omitted rather than propagated.
- Fox, Zakarauskas, Dixon, Ellamil, Thompson & Christoff 2012, *PLOS ONE* 7(9) e45370 — **real-correct** (publisher XML). Result-direction: experts more accurate than novices, experience predicts accuracy, logarithmic relation. Faithful in direction. The **subject** was misdescribed: accuracy means agreement with population-averaged tactile norms, not access to phenomenal states. Fixed above.
- Kahneman & Deaton 2010, *PNAS* 107(38) 16489-93 — **real-correct metadata; result-direction CONTRADICTED by the old body sentence; currency-superseded on the plateau** (Killingsworth, Kahneman & Mellers 2023). The new sentence carries only the "different correlates" finding, which the 2023 paper does not touch. Now cited inline, which closes the inline↔References orphan.
- Frankish 2016, *JCS* 23(11-12) 11-39 — metadata real-correct (06-24). Term-subject check: **primary UNREACHABLE** (PhilArchive 403, author eprint 404). The fix rests on independent secondary sources that agree and on the Map's own `concepts/illusionism` L105.

**Cited-author stance**: Tallis is an anti-physicalist critic of illusionism and is not presented as endorsing dualism. Frankish is the named opponent. Fox et al. take no metaphysical stance, and the page now says explicitly that their result is neutral. Whitehead is a process philosopher used only for the satisfaction/intensity contrast. Russell's preferentist framework is the opponent. No author is enlisted for dualism (lens c passes).

### Quote / term-of-art check

| Item | Source | State |
|---|---|---|
| Tallis "illusions presuppose experience" (unquoted paraphrase) | *Philosophy Now* 161 raw HTML | VERIFIED (verbatim "all illusions presuppose experience"); subject fits: Tallis's next sentence, "Presentation is a relationship between an entity… and a subject conscious of that entity", is the article's relatum worry |
| Tallis "misrepresentation presupposes presentation" (absent from page) | same | VERIFIED verbatim at publisher; re-quoting was available but **not done**, because restoring quotes across the 47 de-quoted loci is the open operator call recorded in memory |
| Frankish *quasi-phenomenal* | Frankish 2016 | primary UNREACHABLE; subject CONTRADICTED by secondary consensus → fixed |
| Whitehead "actual occasions", "satisfaction" | *Process and Reality* | VERIFIED as technical terms (standard); gloss trimmed |
| "focusing illusion" | Kahneman | term real; attachment to the K&D income finding CONTRADICTED → removed |
| Garrabrant's four Goodhart types | AI Alignment Forum 2017 | VERIFIED (06-24 ledger; table unchanged) |

### Reasoning-Mode Classification (editor-internal)

- Engagement with illusionism (Frankish): **Mode Two → Mode Three**, unchanged. The Training Argument no longer does Mode-One work it could not earn: it now marks the evidence as neutral.
- Engagement with heterophenomenology (Dennett): **Mode Three**, unchanged.
- No label leakage (grep clean). No "This is not X. It is Y.", no "load-bearing".

### Lens results

(a) Introspection fallibility: three loci fixed (Measurement Protocol bullet, Training Argument, Witness Consciousness). L102 "not because they are infallible" was already hedged. (b) No phenomenology as evidence for a tenet: the Training Argument is fixed; the jhana and witness passages now claim phenomenological discrimination only. (c) No author enlisted for dualism: pass. (d) Claims of absence scoped: L114 and the jhana line fixed; L96 "cannot be directly measured from outside" is accepted framework-level. (e) No concession to epiphenomenalism: none found; the L114 "every observable" scoping also removes any reading on which the missed aspect is physically idle. (f) Tenet 5 constrains only the Map's own reasoning: L204 fixed.

## Optimistic Analysis Summary

### Strengths Preserved
- The constraints-not-optimisation design and the Goodhart failure-mode table, both untouched
- The phenomenal/causal agency distinction, consistent with [P-A4](/positions/agency-and-will/#p-a4) (introspection cannot certify efficacy)
- The 07-18/07-19 calibration repairs (the illusionism hedge, the conditional practical asymmetry, the conditional quantum agency, Buddhist *anattā* boundary-marking), all intact
- The governance requirements, intact

### Enhancements Made
The Hardline Empiricist's preferred move is now on the page: the Training Argument openly declines to treat a neutral result as evidence. The Measurement Protocol now carries a real, scoped citation instead of a self-certifying forward reference.

### Cross-links Added
- [introspection](/concepts/introspection/) (body link moved into the Measurement Protocol; it was previously doubled in the Training Argument)

## Remaining Items

None for this article. Length: 3350 → 3380 (+30, at the brief's ceiling). Still `soft_warning`, with headroom 119 under the 3500 gate.

## Stability Notes

Seventh review. Do NOT re-flag:
- the 07-18 trio (resolved);
- the bedrock disagreements (eliminativism, heterophenomenology, the MWI indexical dispute, *anattā* vs haecceity);
- the decision to leave Tallis unquoted. That is a deliberate deferral to the corpus-wide operator call, not an oversight; the verbatim is verified above if anyone wants to restore it.

*Aping Mankind* carries a cognate argument and is **not** fabricated. The *Philosophy Now* page range (58-59) is unverified at the publisher's web page. The Training Argument now says the evidence is neutral between the views. A future pass should not "strengthen" it back into an anti-illusionist argument without a study that measures something an illusionist cannot accommodate.