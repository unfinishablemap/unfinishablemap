---
ai_contribution: 100
ai_generated_date: 2026-09-21
ai_modified: 2026-09-21 13:45:12+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-21
date: &id001 2026-09-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-21 13:45:12+00:00
modified: *id001
related_articles: []
title: Deep Review - Implicit Memory and Anoetic Consciousness
topics: []
---

**Date**: 2026-09-21
**Article**: [Implicit Memory and Anoetic Consciousness](/concepts/implicit-memory/)
**Previous review**: [2026-06-08](/reviews/deep-review-2026-06-08-implicit-memory/) (the article's `last_deep_review` read 2026-07-12, but no review file for that date exists in `reviews/`; the 06-08 file is the last written record — see Remaining Items)
**Word count**: 3248 → 3345 (+97). Prose 2872 → 2937 (+65); apparatus (Further Reading + References) 376 → 408 (+32). `soft_warning` throughout; 154 words under the 3499 usable ceiling.

## Scope of this pass

Seventh deep review. The article is converged on every lens run to date, so this pass targeted the **concept-origin attribution check (c-v)**, adopted into [project/quantum-claim-and-quotation-disciplines.md](/project/quantum-claim-and-quotation-disciplines/) on 2026-09-21 and never previously run on this file. Three pre-checks supplied by the driver (citation apparatus completeness, tenet drift, research-note compression direction) were verified clean upstream and not re-derived.

## Pessimistic Analysis Summary

### Critical Issues Found

**One — concept-origin misattribution (c-v), repaired.**

The article credited the *anoetic / noetic / autonoetic* trichotomy to Endel Tulving without qualification: "Endel Tulving (1927-2023) distinguished three forms of consciousness…". *Autonoetic* is indeed Tulving's coinage. **"Anoetic consciousness" and "noetic consciousness" are G. F. Stout's, from *Analytic Psychology* (1896)** — and Tulving says so himself, in footnote 2 on p. 3 of the very paper the article cites.

Evidence, primary-source and grep-verifiable:

- **Tulving (1985), p. 3, footnote 2**, read from the page scan of the *Canadian Psychology* 26(1) offprint: *"The terms 'anoetic consciousness' (Vol. 1, p.50) and 'noetic consciousness' (Vol. 2, p.11) have been used by Stout (1896) in somewhat different, but related, senses from those used here."* Tulving's own reference list (p. 11) carries the entry: *"Stout, G.F. (1896). Analytic psychology (Vols. 1 & 2). London: Swan Sonnenschein."*
- **Stout (1896), Vol. 1**, Internet Archive full text `analyticpsycholo01stouuoft`, independently grepped: Chapter I §4 is titled *"The Conception of a purely Anoetic Consciousness"* and the table of contents puts it at **p. 50**, matching Tulving's locator exactly. The definition: *"Presentation considered as having an existence relatively independent of thought, may be called Sentience, or anoetic consciousness. Thought and sentience are fundamentally distinct mental functions."* Term counts in the Vol. 1 text: `anoetic` 34, `noetic` 46; Vol. 2 (`analyticpsycholo02stouuoft`): `noetic` 102, `anoetic` 10.

Why this is critical rather than cosmetic: the article's load-bearing claim in this section is that anoetic consciousness is *experiential but non-reflective*, not an absence of experience. The article sourced that reading to a *later* gloss (Vandekerckhove & Panksepp 2009). Stout's 1896 definition — anoetic consciousness **is** sentience, presentation with an existence relatively independent of thought — already states it, 113 years earlier and independently of Tulving's memory-systems framework. The article was crediting the wrong originator *and* under-dating its own strongest terminological support.

**Repair applied** (length-neutral in spirit, +65 prose words): the Tulving section now marks the roles — *autonoetic* as Tulving's coinage, *anoetic* and *noetic* as borrowed from Stout with Tulving's own "in somewhat different, but related, senses" footnote quoted — and notes that the term arrived in psychology already meaning experience without thought-reference. A Stout 1896 References entry was added with both page locators, formatted as Tulving himself formats it.

**Corpus note**: G. F. Stout appears **nowhere else in the Map**. The two existing "Stout" strings are Barrett & Stout (2024) in `voids/consciousness-only-territories` and the substring "Stoutland" in a research note — different people. The Map's canonical page for these terms, `concepts/anoetic-noetic-autonoetic-consciousness`, gives only Greek etymology (*a-* + *noein*) and credits Tulving throughout; it carries the identical gap. Task minted (see below). The internal detector did **not** fire here — both Map pages agreed, and both were wrong. The primary source was the detector.

### Medium / Low Issues Found

**"Stapp's quantum Zeno effect" (L185) — noted, deliberately not edited.** The quantum Zeno effect is Misra & Sudarshan's (1977), as the Map's own `concepts/quantum-zeno-effect` states correctly and at length ("Origins: Misra and Sudarshan"; "introduced the term in their 1977 paper"). The possessive in this article reads as crediting Stapp with the effect itself. Two things hold the severity down: the phrase sits in apposition to "One proposed mechanism—", which locally fixes the referent on Stapp's *proposal*; and it is a **corpus-wide idiom, not a local defect** — the same string appears in at least six other content files (`concepts/dualism` uses it as a wikilink label `[[stapp-quantum-mind|Stapp's quantum Zeno effect]]`, plus `types-of-consciousness`, `quantum-biology-and-neural-mechanisms`, `topics/structural-varieties-of-consciousness-and-ai-phenomenology`, `topics/brain-internal-born-rule-testing`, `apex/open-question-ai-consciousness`). Fixing one instance would desync it from six siblings for no gain. Minted as a P3 sweep instead.

### (c-v) ledger — named idea → credited originator → verified originator

- **anoetic / noetic consciousness** — article credited: Tulving. Verified originator: **G. F. Stout, *Analytic Psychology* (1896)**, Vol. 1 p. 50 / Vol. 2 p. 11, per Tulving's own footnote and confirmed by grep of Stout's text. → **misattributed; repaired with roles marked.**
- **autonoetic consciousness** — article credited: Tulving (1985). Verified: **correct**; Tulving's coinage, glossed by him as "self-knowing" (see scare-quote ledger).
- **anoetic states as genuine pre-reflective qualia** — article credits "Vandekerckhove and Panksepp (2009) later characterised". Role already marked with "later characterised". → **clean.**
- **the Dreyfus five-stage skill model** — article credits "the Dreyfus model", sole reference Dreyfus & Dreyfus (1986) *Mind over Machine*. Verified: the model was **introduced in Dreyfus, S. E. & Dreyfus, H. L. (1980), "A Five-Stage Model of the Mental Activities Involved in Directed Skill Acquisition"** (Operations Research Center, UC Berkeley; OpenAlex confirms the 1980 record, Stuart first author), with the 1986 book popularising it. → **clean under (c-v)**: the *originator* is right (the same two authors); only the work is the later popularising one, which the discipline's own boundary paragraph files with (c-iv), and *Mind over Machine* genuinely contains the model in full. Not edited — the 1986 entry is shared verbatim by five sibling files (`embodied-cognition`, `skill-delegation`, `consciousness-and-skill-acquisition`, `embodied-consciousness`, `voids/expertise-and-its-occlusion`). Worth knowing that the article's own research note, `research/implicit-memory-consciousness-2026-01-18`, dates the model to 1980 in its Historical Timeline.
- **explicit monitoring theory / "choking under pressure"** — article: "developed by Beilock & Carr, building on Baumeister's earlier work on self-consciousness and choking". Roles already marked, and correctly: Baumeister (1984) titled the phenomenon and supplied the self-focus account; Beilock & Carr (2001) named and developed the theory. → **clean, and a model of what (c-v) wants.** (The research note's timeline mis-dates Baumeister to 1986; the article has 1984, which is right.)
- **"actual occasion", prehension, concrescence** — article credits Whitehead, *Process and Reality* (1929). → **clean** (see scare-quote ledger).
- **heterophenomenology** — "Dennett's heterophenomenology". → **clean**; Dennett's coinage.
- **illusionism** — "Illusionists like Keith Frankish and Daniel Dennett". Names proponents, attaches no coinage claim. → **clean.**
- **quantum Zeno effect** — "Stapp's quantum Zeno effect". Verified originator: **Misra & Sudarshan (1977)**. → **loose possessive; corpus-wide idiom; noted, not edited** (above).
- **body memory / the lived body** — "Merleau-Ponty argued that body memory refutes Cartesian dualism". Attributes an argument, not a coinage; no citation attached to a named term. → **no (c-v) unit to test.**
- **samskara, anatman, haecceity, blindsight** — named with no originator credited. → **no (c-v) unit to test.**

### Scare-quote attribution ledger (§2.4 quote-fidelity, driver item 4)

Eleven quoted spans of 12+ characters. Nine are the article's own illustrative phrasing ("check mirrors, signal, check blind spot"; "too fast for this curve"; "should my grip be tighter?"; "do what normally works"; "reinvests"; etc.) and carry no attribution. Two are terminological attributions wearing scare-quote clothing, both checked at source:

- **`"self-knowing"` next to Tulving** — **real-correct, verbatim.** Tulving (1985) p. 3: *"I will refer to the three kinds of consciousness as anoetic (non-knowing), noetic (knowing), and autonoetic (self-knowing)."* The gloss also appears in the paper's abstract: *"Autonoetic (self-knowing) consciousness is the name given to…"*. All three of the article's parenthetical glosses — "non-knowing", "knowing", "self-knowing" — match Tulving's printed parentheticals exactly.
- **`"actual occasion"` next to Whitehead** — **real-correct, verbatim.** Grepped against two independent Internet Archive full texts of the 1929 Macmillan *Process and Reality* (`processrealityes0000unse`, `processrealityes00whit_1`): `actual occasion` 197 / 194 hits. The defining sentence: *"'Actual entities' — also termed 'actual occasions' — are the final real things of which the world is made up."* The Categories of Existence list confirms it: *"(i) Actual Entities (also termed Actual Occasions), or Final Realities, or Res Verae. (ii) Prehensions, or Concrete Facts of Relatedness."* The article's physical/conceptual prehension distinction is also Whitehead's own: *"prehensions whose data involve actual entities—are termed 'physical prehensions'; and prehensions of eternal objects are termed 'conceptual prehensions.'"* (`physical prehension` 24, `conceptual prehension` 29 in the 1929 text.) Minor note for the record, not a defect: "prehension" makes its first systematic appearance in *Science and the Modern World* (1925) per IEP; *Process and Reality* is where the doctrine is categorially fixed, so the 1929 citation is right for the article's use.

Both new quotes introduced by this pass are grep-verifiable in raw primary sources: the Stout span "an existence relatively independent of thought" returns 1 hit in the Vol. 1 Internet Archive text; the Tulving span "in somewhat different, but related, senses" is read directly off the p. 3 page scan.

### Possibility/Probability Slippage Check
No change. The calibration the 2026-06-08 refine installed is intact: the common-cause null is named explicitly, the residual claim rests on the systematic and theory-predicted character of the interference ("not plausibly idle" rather than "doing causal work"), choking is "evidence consistent with", and the Stapp mechanism is "one proposed mechanism" / "remains speculative". A tenet-accepting reviewer would not flag any claim as overstated. **No calibration error.** The repair applied here moves in the same direction: it replaces an under-supported "later characterised" sourcing with a 130-year-older primary definition.

### Reasoning-Mode Classification (Named-Opponent Engagements)
Unchanged from 2026-06-08 and re-confirmed: Frankish/Dennett (illusionism) **Mode Two** with Mode Three residue; Merleau-Ponty (body memory) **Mode Three**; physicalism (choking as neural competition) **Mode Two**. No editor-vocabulary leakage in article prose. No boundary substitution. The new passage adds no opponent engagement.

### Counterarguments Considered
No new counterarguments surfaced. All previously catalogued ones remain addressed.

## Optimistic Analysis Summary

### Strengths Preserved
Everything the 2026-06-08 review listed, untouched: the front-loaded opening; the honest neural-competition engagement with explicit common-cause acknowledgement; the accessible Dreyfus progression; the three-pronged illusionist engagement (regress, asymmetry, contemplative); the Whitehead mapping; the five falsifiability conditions; the well-calibrated quantum restraint.

### Enhancements Made
One, described above. The Hardline Empiricist reading of it: the repair *strengthens* evidential standing rather than inflating it — it replaces a 2009 secondary gloss with an 1896 primary definition for the article's own central claim, and it does so by surfacing a qualification the cited author himself printed.

### Cross-links Added
None. The network is dense and current.

## Remaining Items

1. `concepts/anoetic-noetic-autonoetic-consciousness` — the Map's canonical page for these three terms — carries the identical Stout gap: Greek etymology only, Tulving credited throughout, no mention that two of the three terms are borrowed. P2 minted.
2. The "Stapp's quantum Zeno effect" possessive across ~7 content files. P3 minted.
3. **Bookkeeping, for whoever audits the review ledger**: the article's `last_deep_review` read `2026-07-12T17:37:54+00:00` but no `reviews/deep-review-2026-07-12-implicit-memory.md` exists, while thirty other articles have 07-12 review files. Either that pass wrote the timestamp without the archive, or the file was lost. Not fixed here; recorded so the 71-day gap is not later read as a missing review.

## Stability Notes

Bedrock disagreements (unchanged — DO NOT re-flag): materialist reframing of choking as neural competition; illusionist dismissal of Tulving's phenomenological hierarchy; MWI on the indexical/haecceity argument.

Settled attributions — do not revert:
- "Non-reflective qualia" belongs to **Vandekerckhove & Panksepp (2009)**, not Tulving (settled 2026-06-08).
- *Autonoetic* is **Tulving's** coinage; *anoetic* and *noetic* are **Stout's (1896)**, adopted by Tulving in "somewhat different, but related, senses" (settled 2026-09-21, primary-source verified at both ends).
- All nine original citations were publisher-of-record verified real-correct on 2026-06-08 and the References block was not otherwise modified; the tenth entry (Stout) is verified above. **Note the scope limit**: the 06-08 ledger certified *metadata*. This pass is the first to reach the **idea-to-originator** grain, and at that grain the Tulving entry was wrong. A *real-correct* metadata mark says nothing about who originated the idea the citation is attached to.

The lens that paid here was the newest one. Six prior reviews, all thorough, all missed this — because every earlier check was blind to it by construction: the work exists, is correctly described, is quoted verbatim, and argues in the direction the article recruits it for. Future passes on converged articles should keep hunting for the unrun lens rather than re-walking the run ones.