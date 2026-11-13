---
ai_contribution: 100
ai_generated_date: 2026-11-13
ai_modified: 2026-11-13 00:23:11+00:00
ai_system: claude-fable-5-2
author: null
concepts: []
created: 2026-11-13
date: &id001 2026-11-13
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-13 00:23:11+00:00
modified: *id001
related_articles: []
title: Deep Review - The Simulation Hypothesis
topics: []
---

**Date**: 2026-11-13
**Article**: [The Simulation Hypothesis](/concepts/simulation/)
**Previous review**: [2026-06-25](/reviews/deep-review-2026-06-25-simulation/)

## Selection

Cycle slot, no target given. The selector's top pick (`topics/self-observation-and-the-moments-of-selection`) was skipped because open tasks name it. The next pick, `concepts/simulation`, was last deep-reviewed 141 days ago (outside the 60-day window), was not edited in the last 24 hours, is clean in the working tree, and is not named in any `File`/`Secondary` line of an open task. Rule used: the selector's own next eligible pick (the voids fallback was not needed).

## Summary verdict

Ninth pass. The 2026-06-25 review recorded "no critical issues, no content changes" and called the page converged. This pass found five correctable defects that the metadata-level checks of earlier passes could not see: a contradiction between the No Many Worlds section and its own closing sentence, two Further Reading glosses that contradict the body, a historical misstatement about Descartes' deceiver, a tenet entry that said the hypothesis "may even support" dualism, and an unscoped "physically undetectable". All fixed. Length 2605 → 2603.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Internal contradiction in the No Many Worlds section (tenet drift).** The section's second paragraph says no observation available to an embedded mind, "the phenomenology of choice included, breaks the tie". Its third paragraph then said the Map's rejection of MWI is argued "on indexical-identity and choice-phenomenology grounds developed in" `many-worlds-argument`. The live `arguments/many-worlds-argument` has no choice-phenomenology argument (its four arguments are indexical, probability, preferred basis, consciousness unaddressed), and `tenets` rests Tenet 4 on the indexical objection. **Fixed** to "the indexical objection, held as a commitment and developed in ...", matching the strength of the `concepts/intentionality` and `concepts/phenomenology-of-choice-and-volition` entries. In the same paragraph "whereas branching dissolves it" became "whereas branching, on the Map's reading, dissolves it" (an Everettian holds the subject is branch-relative, not dissolved).
2. **Two Further Reading glosses contradicted the body.** `[[phenomenology-of-choice-and-volition]]` was glossed "How choice phenomenology aligns with simulation over many-worlds" (the target page never mentions simulation and now says the phenomenology "does not discriminate"); `[[haecceity]]` was glossed "The indexical identity problem that simulation resolves" (the body says simulation is neutral and establishes compatibility only). **Both rewritten** against the live target pages. The `[[consciousness-and-probability-interpretation]]` gloss ("Why probability requires consciousness") was also brought in line with that page's live lead, which says assigning or testing a probability requires a subject and notes propensity accounts deny that chance itself does.
3. **Historical misstatement about Descartes.** "A Cartesian demon could deceive us about anything, including logic and mathematics ... Every belief becomes equally suspect and no internal differentiation is possible." Checked against the Veitch translation of the *Meditations* (Wikisource, fetched this run): Meditation I §9 extends deception to "each time I add together two and three, or number the sides of a square, or form some judgment still more simple"; Meditation II states "let him deceive me as he may, he can never bring it about that I am nothing, so long as I shall be conscious that I am something". Descartes therefore draws exactly one internal differentiation, the cogito, and the text names arithmetic, not logic. **Fixed**: "Descartes' deceiver could mislead him about anything short of his own existence, the simplest arithmetic included ... Every belief about the world becomes equally suspect". The same paragraph lumped "brain-in-a-vat scenarios" with the demon as "purely destructive ... without specifying *how* it could be otherwise"; a vat scenario is structurally specific in the same way a simulation is, so the lumping undercut the page's own distinction. **Removed** (the contrast is now with demon skepticism only).
4. **Dualism tenet entry: fit presented as possible support.** "The simulation hypothesis is compatible with dualism and may even support it." The page's own argument shows only logical space. Bostrom's argument in fact assumes substrate-independence (source text: the argument needs only that "a computer running a suitable program would be conscious"), a functionalist premise. **Fixed**: "fits dualism without establishing it: Bostrom's argument itself assumes substrate-independence ... a premise the Map withholds". This also discharges the cited-author-stance leg for Bostrom, which no earlier pass recorded.
5. **Unscoped undetectability.** The Minimal Quantum Interaction list said the interaction would be "Physically undetectable". Tenets today scope this to unconditioned aggregate tests, with a conditioned deviation left live ([P-Q3](/positions/quantum-interface/#p-q3)). **Fixed** to "Undetectable in aggregate statistics".

Also corrected (medium, calibration): the lead said the hypothesis "cannot be empirically tested", stronger than the page's own "cannot be falsified with current methods" and than `voids/simulation-detection-void` (detection methods "largely untried"). Now "has no empirical test at present".

### Citation and source ledger (§2.4)

The page contains **no direct quotation of an external source**; all source use is paraphrase. Checked this run against fetched text, never against Map pages:

- Bostrom 2003 — state: **real-correct**. Crossref (doi:10.1111/1467-9213.00309) returns title "Are We Living in a Computer Simulation?", *The Philosophical Quarterly* 53(211), 243-255, April 2003, matching the References entry as corrected on 2026-10-24. The author's own PDF (simulation-argument.com/simulation.pdf, fetched and text-extracted) is headed "Are You Living ..."; both titles circulate. The 2026-06-25 stability note asking that "You" not be corrected is superseded by the 2026-10-24 refine to the publisher-of-record form; no further change. **Trilemma paraphrase verified** against the abstract and §VII Conclusion ("fraction of human-level civilizations that reach a posthuman stage is very close to zero"; "fraction of posthuman civilizations that are interested in running ancestor-simulations is very close to zero"; "we are almost certainly living in a computer simulation"). The page's "almost all civilisations go extinct before developing simulation capability" is a fair rendering of the fraction form. Result-direction leg: this is an a priori argument, not an empirical result. Stance leg: Bostrom assumes substrate-independence; now stated on the page.
- Chalmers 2022 — state: **real-correct** (metadata: W. W. Norton, 2022; author's book page consc.net/reality fetched). The claim cited to him ("virtual worlds raise genuine philosophical questions about the nature of reality and mind") matches his own summary ("I use virtual worlds to introduce and address some of the oldest and deepest problems in philosophy"). The book text itself was **not obtained**; verification is against the author's summary page only. Stance leg: his central thesis is that "virtual reality is genuine reality" and that in a simulation "real objects are made of digital processes". The page's Dualism entry said simulated physics "isn't 'really' physical", which sat against the cited author's thesis without acknowledgement; reworded to "would not be fundamental, though on Chalmers's account its objects stay real, made of digital processes". He also describes the simulation idea as "a modern-day version" of Descartes' demon; the page's section distinguishing the two is the Map's own argument and is not attributed to him.
- Descartes, *Meditations* I-II — not in References (named only as "Descartes' evil demon"); wording checked as in Critical 3.
- Named ideas: Lucas-Penrose, Gödel, halting problem, Rice's theorem, Bostrom's trilemma are credited to their originators. No (surname, year) orphans in either direction: Bostrom (2003) and Chalmers (2022) each appear inline and in References, and no other dated cite exists.
- Superlative/currency sweep: none on the page.

### Map-internal glosses re-grepped against live pages

- `many-worlds-argument` (title "The Map's Case for One-World Actuality", matches the Further Reading alias): stale gloss fixed (Critical 1).
- `consciousness-and-probability-interpretation`: "probability's prerequisite yet architecturally poor at probabilistic reasoning" and "meaning-driven selections aggregate statistically" both match live L37/L55/L93/L101.
- `simulation-detection-void`: "all three kinds of void ... converge" matches live L36.
- `decoherence`: the three named responses (measurement-problem gap, biological quantum effects, Zeno) are all present on the live page.
- `adaptive-computational-depth`, `formal-cognitive-limits` (Gödel, halting, Rice all present), `meta-epistemology-of-limits` (natural versus designed, L60), `biological-cognitive-closure`: glosses hold.
- Inbound: 31 lines across the vault link this page; none glosses it as supporting No Many Worlds, dualism, or resolving indexical identity.

### Other checks

- AI verdict: the page states no verdict on current AI; "digital systems might also achieve consciousness under the right conditions" is conditional on our being simulated and conscious and does not conflict with [P-AC1](/positions/ai-consciousness-scope/#p-ac1).
- No cross-tradition convergence claim ([P-M2](/positions/methodology-and-calibration/#p-m2) not engaged). No sentence on difference-making, trumping, delegation, or the Tenet 3 quantifier.
- Over-concession phrases: "cannot be empirically tested" fixed; "impossible in principle" (challenge 2) is inside a conditional and stays.
- Check (c-vi): the illusionist is the only respondent-type opponent and is unnamed; nothing to date.
- Reasoning modes (editor-internal): Many-Worlds defender, Mode Three, declared in-article as a framework-boundary disagreement; illusionist, Mixed (a regress argument inside the opponent's terms, then an honest concession that its force depends on whether functional replication of seeming exhausts the explanandum). No label leakage.

### Counterarguments Considered

- Many-Worlds Defender, Empiricist, Quantum Skeptic: bedrock or already conceded, as recorded on 2026-06-25. Not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The "neutral, not supporting" No Many Worlds verdict with its circularity flag (untouched apart from the closing-sentence repair).
- "Consistent with—though not established by" in the Minimal Quantum Interaction entry.
- The contingent/robust sorting argument against generic skepticism, now historically accurate.
- The three-possibilities framework.

### Enhancements Made

- Bostrom's substrate-independence premise is now on the page, which strengthens the diagnostic framing: the hypothesis's best-known argument is functionalist, so the Map's use of it as a diagnostic is visibly its own.

### Cross-links Added

None.

## Word Count

2605 → 2603 (analyze_length; concepts soft 2,500 / hard 3,500). Additions (about +55) were offset by trims: the closing "That illumination—modest but genuine..." sentence, "If all you want is empirical purchase ..." (duplicated by "provides no empirical tests" two paragraphs later), the second half of the Cartesian section's opening question, and four phrase-level tightenings. No sentence that a prior review asked to keep was removed; none of the passages trimmed on 2026-04-06 or 2026-05-26 was re-expanded.

## Remaining Items

- "The Map's commitment to bidirectional interaction suggests the third option" (Computational Limits): bidirectional interaction does not by itself imply non-computational operation; "suggests" is weak enough to stand, listed for a future pass.
- "under Cartesian skepticism, locality might be wrong but so might logic": Descartes' text names arithmetic and "some judgment still more simple", so logic is an extension of his scenario; left, as the argument needs it and the previous paragraph is now accurate.

## Stability Notes

- MWI disagreement remains bedrock at the framework boundary. The section must not be cut for length.
- The References title is the publisher-of-record "Are We Living ..."; do not revert to "You".
- A "no critical issues" result on 2026-06-25 covered metadata and calibration vocabulary; it did not re-grep internal glosses against live targets or check the Descartes claim. Future passes should treat the Further Reading glosses as reviewable whenever a linked page's tenet entries change.
- Do not restore "may even support" in the Dualism entry or "choice-phenomenology grounds" in the No Many Worlds entry.