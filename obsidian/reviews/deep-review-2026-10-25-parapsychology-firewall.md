---
title: "Deep Review - The Parapsychology Firewall"
created: 2026-10-25
modified: 2026-10-25
human_modified: null
ai_modified: 2026-10-25T01:18:24+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-25
last_curated: null
---

**Date**: 2026-10-25
**Article**: [[parapsychology-firewall|The Parapsychology Firewall: Why Spectacular Psi Would Disconfirm the Map]]
**Previous review**: [[deep-review-2026-08-18-parapsychology-firewall|2026-08-18]] (also [[deep-review-2026-07-07-parapsychology-firewall|2026-07-07]] and [[deep-review-2026-06-22-parapsychology-firewall|2026-06-22]])
**Word count**: 2151 → 2658 (+507; topics soft 3000, hard 4000; no length pressure)

## What Was Unchecked Going In

Two edits by other skills had landed since 08-18, and neither was reviewed here:
`cc77b347` (09-08) scoped "indistinguishable from chance" in the lead, and `e3e68951`
(09-27) added to Constraint 1 that the Maier et al. 2018 external-RNG null does not test
the brain-internal corridor. The register had also moved. P-Q2's Asserts was rewritten
on 2026-10-14 to "Born-exact in every publicly conditionable context", and that rewrite
is now the open P1 HUMAN DECISION on P-Q2's quantifier (see Remaining Items).

Both repairs hold where they landed. The lead's indistinguishability is scoped to the
unconditioned aggregate. Constraint 1 states that the Maier null was predicted either way
under brain-locality. Two other places had not caught up with the P-Q3 correction. L73 still
said the external-RNG nulls were "predicted by" a Born-preserving interface. "What Would
Actually Bear" and the cheap-falsifier paragraph still credited the framework with a
mechanism-level exposure that the falsification roadmap says the endorsed path does not have.

## Pessimistic Analysis Summary

### Publisher-of-Record Citation Ledger (§2.4)

Each cite was checked at Crossref, with fields printed. Result direction was checked
against the publisher abstract or full text.

- **Bösch, Steinkamp & Boller 2006**, *Psychol. Bull.* 132(4):497–523, doi
  10.1037/0033-2909.132.4.497. **real-correct.** Authors Holger Bösch, Fiona Steinkamp,
  Emil Boller. Result direction (OpenAlex abstract): 380 studies, "a significant but very
  small overall effect", effect sizes "strongly and inversely related to sample size",
  and possibly an artefact of publication bias. That matches L73. Stance: meta-analysts;
  not enlisted for dualism. Fixed this pass: it was a References-only orphan and is now
  cited inline at L73.
- **Donadi, Piscicchia, Curceanu, Diósi, Laubenstein & Bassi 2021**, *Nature Physics*
  17(1):74–78, doi 10.1038/s41567-020-1008-4. Online 2020-09-07, print 2021-01.
  **real-correct; ADDED.** The "falsified parameter-free Diósi-Penrose model" claim had
  no citation. Publisher abstract: "This rules out the natural parameter-free version of
  the Diósi–Penrose model." The result direction matches. The citation form matches the
  corpus (P-Q6, falsification roadmap).
- **Han & Choi 2016**, *Sci. Rep.* 6:22986, doi 10.1038/srep22986. **real-correct.**
  Authors Yeong Deok Han, Taeseung Choi; issued 2016-03-14. Abstract: "Born rule on
  quantum measurement is derived by requiring relativistic causality condition." That
  matches Constraint 2. Fixed this pass: References-only orphan, now cited inline at L55.
- **Maier, Dechamps & Pflitsch 2018 (A)**, *Front. Psychol.* 9:379, doi
  10.3389/fpsyg.2018.00379, issued 2018-03-21. Three authors: Markus A. Maier, Moritz C.
  Dechamps, Markus Pflitsch. **real-correct metadata; real-wrong characterisation at L73
  (fixed).** In the full text (Europe PMC, PMC5872141) the "regist" string occurs twice.
  One is the Study 2 sentence about Maier & Dechamps, the other a reference title. The
  study itself was not registered. It used a sequential Bayesian design stopping at
  BF > 10, with 12,571 participants and BF01 = 10.07. The 2026-06-22 review's ledger
  ("12,571-subject Bayesian **pre-registered** study") is where the L73 error was
  ratified. Stance: the authors are micro-PK researchers who read their temporal
  pattern through von Lucadou's Model of Pragmatic Information. They are not firewall
  proponents and are not enlisted as such.
- **Maier & Dechamps 2018 (B)**, *J. Sci. Explor.* 32(2):265–297, doi 10.31275/2018.1250,
  issued 2018-06-30. Two authors: Markus A. Maier, Moritz C. Dechamps. Title "Observer
  Effects on Quantum Randomness: Testing Micro-Psychokinetic Effects of Smokers on
  Addiction-Related Stimuli". **real-correct; ADDED.** Checked by grep of the publisher PDF
  (journalofscientificexploration.org, article 1250). "The study was pre-registered at the
  Open Science Framework (OSF) (https://osf.io/4fzq8)" applies to Study 2. That study had
  175 smokers (one-tailed BF01 = 11.07) and 220 non-smokers (BF01 = 3.74). Study 1 had
  reported strong evidence *for* micro-PK (BF10 = 66.06), so the article calls Study 2 "a
  pre-registered replication of an earlier positive result". It does not call (B) a null
  paper. Both studies used an external tRNG. Stance: same authors and the same MPI
  reading as (A).
- **Stapp 2006**, *Zygon* 41(3), doi 10.1111/j.1467-9744.2005.00762.x. Crossref: Henry
  P. Stapp, issued 2006-09-02, no pages deposited. The 08-18 note still applies: do not
  restore a page range. **real-correct metadata. It had been a References-only orphan since
  creation (`git log -S Stapp` hits only the creation commit d590202f).** Now cited
  inline at L65. The quote "nature returns answers, subject to specified statistical
  requirements" was grep-verified in the LBL preprint linked in the entry
  (www-physics.lbl.gov/~stapp/QID.pdf). Its context: "the agent freely chooses the
  questions … and nature returns answers". Stance: Stapp is an interactive dualist, but
  NOT a firewall ally. He modelled a "purported empirical violation of the predictions of
  quantum theory" (Stapp 1994, *Phys. Rev. A* 50(1):18–22, doi 10.1103/PhysRevA.50.18,
  confirmed at Crossref). The article cites him only for where his mechanism sits
  (question, not outcome), which matches `tenets.md` L107.
- **Torres Alegre 2025**, arXiv:2512.12636. Not in Crossref; checked at the arXiv API.
  Author Enso O. Torres Alegre, submitted 2025-12-14, no journal-ref and no DOI.
  **real-correct; ADDED as a named cite.** Constraint 2 had described this result, said
  it was unrefereed and named no author. Abstract: in "any GPT satisfying purification
  … the only such relationship consistent with no-signaling is the identity", within
  finite-dimensional GPTs. "finite-dimensional" was added to L55. The "not yet refereed"
  claim is still current: there is still no journal-ref. The citation form matches the
  corpus (`apex/post-decoherence-selection-programme`).
- **Southgate & Oquatre-sept 2026**: internal self-citation, linked six times in the
  body. The "Oquatre-sept" form is kept per the 06-22 stability note.

**Cross-reference, both directions, keyed on (surname, year).** Before this pass, three
of the five References entries had no inline cite: Bösch 2006, Han & Choi 2016 and Stapp
2006. All three prior reviews recorded "no orphans in either direction", and none of them
was right. Torres Alegre 2025 and the Diósi-Penrose result were cited in the body with no
entry. All eight entries now have inline cites, and every inline cite has an entry.
`find_superlative_claims`: empty.

### Critical Issues Found

1. **Internal contradiction at L87.** "the same self-concealment that *immunises the Map
   against falsification-by-spectacular-psi*" said the opposite of the thesis in the
   article's own title and lead. It was the unfalsifiability-shield phrasing the brief
   warned about. Fixed to "keeps the Map consistent with the null record, and exposed to
   any spectacular result".
2. **The endorsed path was credited with exposure it lacks (L77, L81).** "The
   framework's genuine empirical exposure appears to live at the mechanism level
   (coherence-time …, microtubule …, the falsified … Diósi-Penrose model)" and "a
   coherence-time or collapse-model result could go against the framework next year".
   Both contradict `topics/falsification-roadmap-for-the-interface-model` L79 (coherence
   impossibility "forecloses Orch-OR … but not the selection-only readings"), L87 (strict
   corridor "not Popper-refutable by unconditioned Born-rule tests … vulnerable instead to
   motivation-loss / theoretical supersession") and P-Q6 (DP "does not reach Orch-OR").
   A reader who accepts the tenets would still flag this. Rescoped: those results bear on
   the coherence-dependent candidates. The endorsed path is exposed to a conditioned
   brain-internal test (not yet run in the work reviewed) and to supersession. The
   cheap-falsifier paragraph now says the corridor's own exposure "is not near-term"
   ("well beyond current reach at the neural grain", following `tenets.md` L81). This
   strengthens the 08-18 anti-hedge rather than reversing it.
3. **Locus (1) of the Maier P3: "large pre-registered micro-PK studies" (L73).**
   Reattributed. "a 12,571-participant sequential study (Maier, Dechamps & Pflitsch 2018)
   and … a pre-registered replication of an earlier positive result (Maier & Dechamps
   2018, Study 2)". "Pre-registered" now attaches only to (B) Study 2. **DONE.**
4. **The P-Q3 correction had not reached L73.** "consistent with—indeed predicted by—a
   Born-preserving, self-concealing interface" gave Born preservation credit for nulls
   that brain-locality predicts on its own. Fixed. "Indeed predicted by" was dropped,
   with a new sentence: "The micro-PK studies all target an external random-number
   generator, so brain-locality predicts no genuine effect in any of them whether or not
   the interface exists." The sentence is limited to micro-PK because the decline effect
   spans ganzfeld and card-guessing paradigms (`selection-only-mind-influence` L115).
5. **P-Q3's cost was stated more weakly than the register states it (L79).** The page
   made ensemble-level epiphenomenalism a future risk that a demonstration "might" bring
   about. Rewritten to quote P-Q3 at full strength ("sits genuinely close to
   epiphenomenalism"). The Map neither concedes the worry nor treats it as dissolved, and
   the page names the candidate answer (the per-trial/ensemble distinction plus the
   indexical fact) as open.
6. **Reference orphans.** Covered in the ledger above.

### Medium Issues Found

- **P-Q7 strength (L55).** "The Map buys compatibility with relativistic causality" is
  stronger than P-Q7, which secures single-system marginals and leaves joint and
  Lorentz-covariant safety open. Fixed: "buys single-system no-signalling safety (joint
  and Lorentz-covariant safety stay open under P-Q7)".
- **Tenet 2 means empirical-constraint minimality (L87, L81).** "consciousness makes
  the smallest possible difference, which is precisely why…" became "the smallest
  difference the empirical record leaves room for". The cheap-falsifier paragraph now
  states that the firewall's height "was set partly by the very record it is now said to
  predict". `concepts/brain-interface-boundary` L118 already concedes "The framework was
  constructed knowing this".
- **Wager read as a conjunction (L89).** "reliable, lawlike, content-importing psi" became
  "replicated psi that is large, lawlike or content-importing", which matches L61's
  disjunction. The disconfirmer is now as easy to trigger as the page says.
- **Firewall scope (L37, L43).** The bound is now on psi defined as mind acting outside
  its own brain or importing content. A pointer explains that a conditioned brain-internal
  deviation is a different observable. Without the pointer, L37's "any effect crossing it
  would falsify" collided with the lead's "would test the corridor".
- **Lead token clause (L31).** "a property of the unconditioned aggregate and not of the
  token" could be read as saying the token is distinguishable, which contradicts P-Q2's
  "per-trial indistinguishable". It now reads "holds for the unconditioned aggregate,
  while each token outcome is still selected rather than left to chance".
- **Description (L3).** "falsify … the Map's dualism" pinned on Tenet 1 something the
  firewall gets from Tenet 2. It now reads "disconfirm … the Map's minimal-interface
  dualism", and the self-concealment is scoped to "unconditioned aggregate tests".
- **Tenet 2 quote fidelity (L71).** `tenets.md` L83 says the tenet is not quantum woo
  that is used "to justify … parapsychology". The page had listed parapsychology itself
  as the thing contrasted. It now reads "quantum mysticism, including its use to justify
  parapsychology or magical thinking". The two tenet quotes (L65, L71) were re-checked
  against `tenets.md` L83/L85.
- **Absence scoping (L51, L77).** "none has yet run" became "none has yet run in the work
  the Map has reviewed".

### Reasoning-Mode Classification (§2.6)

- Folk dualism, an unnamed opponent: Mode Two (the force picture assumes "more mind =
  more push" without arguing for it), then Mode Three at the tenet boundary. No change.
- Stapp: cited for where his mechanism sits. He is not a reply target, so no mode
  applies.
- No label leakage. A grep for every forbidden editor label returns 0.

### Counterarguments Considered

- Physicalist, eliminativist and MWI rejection of the interface: bedrock, not re-flagged
  (per all three prior stability notes).
- The empiricist charge that the firewall is accommodation dressed as prediction is now
  conceded explicitly in the cheap-falsifier paragraph, through empirical-constraint
  minimality. That concession is correct inside the framework.

## Optimistic Analysis Summary

### Strengths Preserved

- The central inversion and the front-loaded bold thesis are untouched.
- The three-constraint structure is untouched, and "Spectacular telepathy would cash a
  cheque the Map has explicitly refused to write" is kept word for word.
- The bidirectional slippage discipline in "The Demarcation Already in the Tenets" is
  kept word for word after the citation sentence.
- The 08-18 cheap-falsifier paragraph is kept and extended in the same direction, removing
  more unearned credit.
- The Constraint 1 agency-budget calibration from 08-18 is kept word for word, apart from
  the absence-scoping clause.

### Enhancements Made

- Stapp is placed against the Map: question-selection versus outcome-selection. This shows
  why the corridor is what keeps the stronger claim inside the firewall.
- The page now names the endorsed path's real exposure: conditioned brain-internal tests
  and supersession.

### Cross-links Added

- `[[tenets#^minimal-quantum-interaction|empirical-constraint minimality]]` (L81)
- `[[positions/quantum-interface#^mechanism-debt|P-Q3]]` (L79)
- `[[brain-interface-boundary|brain-locality]]` (L73; second inbound use)
- In-page anchor `#what-would-actually-bear-on-the-map` (L43)

## Remaining Items

- **This page is a downstream locus of the open P1 HUMAN DECISION on P-Q2's quantifier.**
  That decision is not settled here. L31 ("a deviation *conditioned* on intention, task or
  subject would test the corridor itself") and L51 ("it binds that unconditioned marginal
  only") carry the `tenets.md` L75 / pooled-marginal reading. If option (a) is chosen
  ("Born-exact in every publicly conditionable context"), both lines need rescoping, along
  with L77's "a deviation conditioned on intention, task or subject". Under option (a) a
  task- or subject-conditioned deviation is the fallback outside the corridor, not a test
  of the corridor. The wording added this pass ("exposed to", "would test") was kept
  neutral between (a) and (b). It does not propagate the 10-14 reading.
- The Maier P3's other loci (2)–(5) were NOT touched, per the brief. A further
  out-of-scope lead: `research/quantum-randomness-llm-token-sampling-2026-02-10.md` L109
  cites (A) as two-author "Maier, M. A., & Dechamps, M. C. (2018)" with the *Front.
  Psychol.* title. That research note is not in the P3's optional list.

## Stability Notes

- **"No orphans" was certified falsely three times (06-22, 07-07, 08-18).** Stapp has
  never appeared in the body. Bösch and Han & Choi were only alluded to. Next time, run
  the both-directions check by printing surname hit counts in the body, separately from
  References.
- Do not restore "pre-registered" to (A). Only (B) Study 2 was registered.
- Do not re-credit the endorsed corridor with coherence-time or collapse-model exposure.
  The falsification roadmap and P-Q6 rule it out. Those results bear on the
  coherence-dependent candidates only.
- Do not re-flag the empirical-constraint-minimality concession (L81) as over-conceding.
  It restates `tenets.md` and `brain-interface-boundary` L118. Like the 08-18 paragraph it
  extends, it removes unearned credit.
- Earlier stability notes still hold: the cheap-falsifier paragraph stays; no Stapp page
  range without publisher evidence; bedrock is bedrock.
