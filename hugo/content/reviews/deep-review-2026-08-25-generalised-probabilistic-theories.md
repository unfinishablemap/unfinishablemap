---
ai_contribution: 100
ai_generated_date: 2026-08-25
ai_modified: 2026-08-25 07:26:24+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-25
date: &id001 2026-08-25
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-25 07:26:24+00:00
modified: *id001
related_articles: []
title: Deep Review - Generalised Probabilistic Theories
topics: []
---

**Date**: 2026-08-25
**Article**: [Generalised Probabilistic Theories](/concepts/generalised-probabilistic-theories/)
**Previous review**: [2026-07-25](/reviews/deep-review-2026-07-25-generalised-probabilistic-theories/) (and [2026-07-16](/reviews/deep-review-2026-07-16-generalised-probabilistic-theories/))

## What Changed Since the Last Review

The 2026-07-25 pass was a no-op convergence pass on a stable article. Two substantive
refine-draft commits have landed since, and both touched exactly the passages this
review had to re-open:

- `203f2ce5a9` (2026-08-16) rewrote the Galley-Masanes payload from a conjunction
  ("purification **and/or** local tomography") to a disjunction ("**either** axiom
  forces the Born rule").
- `c0dfc8fa2e` (2026-08-17) added the whole "Purification: The Axiom That Does the
  Forcing" section (~650 words), with seven new direct quotations and two new
  References entries (Chiribella–D'Ariano–Perinotti 2010; Chiribella 2018).

The References block therefore changed since the last ledger, which re-triggers the
§2.4 publisher-of-record pass. It found the article's central claim over-scoped.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Scope error on the Galley-Masanes theorem, contradicted by the article's own
boxworld exposition (fixed, three loci).**

The article stated, unqualified: *"the Born rule becomes forced once **either
purification or local tomography** is added to no-signalling."* That is false as a
claim about probabilistic theories in general, and the article's own text supplies the
counterexample two sections earlier.

Verified at the publisher of record:

- Galley & Masanes (arXiv:1801.06414v4, §2, "Dynamically-quantum theories"):
  *"In this work we consider all theories that have the same pure states, dynamics and
  system-composition rule as quantum theory, but have a different structure of
  measurements and a different rule for assigning probabilities."* The theorem
  quantifies over that class — not over GPTs generally, and not over "no-signalling
  theories."
- Galley & Masanes, §5.1 (Discussion), state the contrapositive themselves *with* the
  missing premise: *"one can derive the measurement postulates of quantum theory from
  the structure of pure states and dynamics and either the assumption of local
  tomography or purification."* Quantum state space and reversible dynamics are load-
  bearing premises; the article had dropped them and substituted no-signalling.
- Barrett 2007 (arXiv:quant-ph/0508211v3), Assumption 5, the **Global State
  Assumption**: *"The global state of a multi-partite system can be completely
  determined by specifying joint probabilities of outcomes for fiducial measurements
  performed simultaneously on each subsystem."* This is local tomography under
  Barrett's name for it, and it is a framework-level assumption, so **boxworld
  satisfies no-signalling and local tomography together and is still not
  Born-ruled.**

So the unqualified disjunction was refuted by the article's own boxworld paragraph.
Fixed in three places: the "Disputed Payload" paragraph (now names the class and uses
boxworld as the deliberate limiting case), the "honest Map statement" conditional (now
carries both clauses), and the Tenet 2 entry under "Relation to Site Perspective".
The lead paragraph was updated to match — a front-loaded summary must not assert what
the body has since corrected.

**2. "On pain of signalling" grafted onto the local-tomography branch (fixed).**

The honest conditional concluded *"...is Born-constrained **on pain of signalling**."*
The signalling lever belongs to the purification/steering route (Torres Alegre 2025)
only. Galley & Masanes prove the opposite for the other branch — their Born-modified
toy theory preserves no-signalling, which is the very *"contrarily to previous claims"*
result the article quotes three paragraphs earlier. A local-tomography failure costs
the Map an axiom without producing a signal. The conditional now says so explicitly.

**3. The "not equal partners" asymmetry claim is falsified by the paper's body
(fixed).**

The 2026-08-17 section asserted: *"Purification and local tomography are not equal
partners... local tomography enters their abstract only as a further casualty, never
as a premise. The Map reads that asymmetry off the abstract's sentence structure;
confirming it against the derivation itself would require the paper's body."* The hedge
named its own test, so this review ran it. The paper's Discussion says the opposite:
*"We observe that we can also derive the measurement postulates of quantum theory from
the assumption of local tomography, which does not have this connotation of
universality."* Either axiom serves as the premise.

There is a real asymmetry, and it is the one the Map should care about — Galley &
Masanes state it directly: purification *"seems linked to the notion that quantum
theory is universal, in the sense that any classical uncertainty can be explained as
originating from some pure global quantum state"*, while local tomography *"does not
have this connotation of universality"*. The paragraph now carries the verified
asymmetry, which bears directly on the section's brain-plus-substrate-as-closed-system
argument (that argument *is* a universality claim). Two dependents were repaired with
it: the H2 heading (a navigation surface asserting "The Axiom That Does the Forcing"
after the body had lost the right to say it) is now "The Axiom the Map Leans On", and
"Purification would then hold across the composite by construction, **forcing the Born
rule with no further argument**" lost its final clause, which the scope fix had made
false.

### Publisher-of-Record Citation Web-Verify Ledger

Full re-run (References block changed since the 2026-07-16 ledger). Every quoted span
in the article was grep-matched against raw artefacts — arXiv abstract HTML and
`pdftotext` output of the papers themselves, never against a WebFetch confirmation
prompt or an aggregator.

- Hardy 2001, *Quantum Theory From Five Reasonable Axioms*, arXiv:quant-ph/0101012 — **real-correct** (title verbatim at arXiv).
- Barrett 2007, *Information processing in generalized probabilistic theories*, Phys. Rev. A 75, 032304 — **real-correct**; arXiv:quant-ph/0508211 URL added to the reference, since the article now quotes the paper's Assumption 5 directly.
- Chiribella, D'Ariano & Perinotti 2010, *Probabilistic theories with purification*, Phys. Rev. A 81, 062348, arXiv:0908.1583 — **real-correct** (Crossref DOI 10.1103/PhysRevA.81.062348 confirms volume/article number). Both quotes verbatim in the abstract.
- Chiribella, D'Ariano & Perinotti 2011, *Informational derivation of quantum theory*, Phys. Rev. A 84, 012311, arXiv:1011.6451 — **real-correct**. "singles out quantum theory within this class" verbatim in the abstract; the five elementary axioms are named there, confirming the article's "classical theory satisfies the five axioms and purification is the postulate excluding it".
- Masanes & Müller 2011, *A derivation of quantum theory from physical requirements*, New J. Phys. 13, 063001, arXiv:1004.1483 — **real-correct** (unchanged since the 2026-07-16 ledger).
- Galley & Masanes 2018, *Any modification of the Born rule leads to a violation of the purification and local tomography principles*, Quantum 2, 104, arXiv:1801.06414 — **real-correct metadata**; all six quoted spans verbatim in the paper (four in the abstract, two in §5.1/§5.2 Discussion). The *reading* of the paper was wrong in two ways — see Critical Issues 1 and 3 — which is the failure mode a metadata-only check cannot reach.
- Chiribella 2018, *Agents, Subsystems, and the Conservation of Information*, Entropy 20(5), 358, arXiv:1804.01943 — **real-correct** (Crossref confirms volume/issue/article). Both quotes verbatim in the abstract.
- Plávala 2023, *General probabilistic theories: An introduction*, Physics Reports 1033, 1–64, arXiv:2103.07469 — **real-correct** (unchanged).
- Torres Alegre 2025, arXiv:2512.12636 — **real-correct**, still correctly labelled preprint/not-peer-reviewed. Its scope hedge (*"within GPTs satisfying purification"*) was already right and is untouched.

Inline ↔ References cross-reference: no orphans in either direction.
Empirical-currency helper: no superlative claims detected.

### Medium Issues Found

- The two 2026 preprints (Torres Alegre; the infinite-dimensional extension) are still unrefereed. Already flagged in-article; re-check on a future currency sweep.

### Named-Opponent Reasoning Modes (editor-internal)

- "Reasonableness" objection (axioms chosen with quantum theory in view): **Mode Three** — framework-boundary marking, conceded as candour under Tenet 5. Unchanged and honest.
- Instrumentalist reading (GPTs as bookkeeping): **Mode Three** — interpretation-neutrality framed as a feature for Tenet 4.
- No editor-vocabulary label leakage in article prose.

### Counterarguments Considered

- Physicalist / Many-Worlds / eliminativist rejection of the Map's use of the framework — bedrock framework-boundary standoff, already conceded in the closing paragraph. Not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The honest-conditional discipline is the article's reason for existing, and the fix strengthens it rather than retreating from it: the conditional now has the premises it always needed, and the article's own boxworld example is promoted from decoration to the limiting case that proves the point.
- Clean separation of neutral definition, reconstruction literature, and explicitly-marked Map interpretation.
- The purification section's two-directional interface argument (closed-system purification vs. reversible-realization) is genuinely good philosophy and survives intact — it is now anchored to the *verified* asymmetry rather than an inferred one.
- The 2026-08-17 steering gloss (purification guarantees steering; steering supplies the signalling lever) is what made Critical Issue 2 diagnosable. Kept.

### Enhancements Made

- Lead paragraph now states the sharpened claim, so a truncated fetch gets the corrected version.
- Barrett reference gained its arXiv URL now that the article quotes the paper.

### Cross-links Added

- None. Existing links (causal-consistency-constraint, local-tomography-and-the-consciousness-physics-interface, brain-internal-born-rule-testing, evidential-status-discipline, sorkin-higher-order-interference) already cover the neighbourhood.

### Length

2481 → 2496 words (concepts/ soft threshold 2500; status `ok`). Length-neutral: the
three scope fixes and the boxworld reconciliation were paid for by trimming redundancy
across twenty passages, including one sentence duplicated verbatim between "Rival
Readings" and "Relation to Site Perspective".

## Remaining Items

**The sibling article carries the same defect.**
`obsidian/concepts/local-tomography-and-the-consciousness-physics-interface.md` states
the unrestricted disjunction at two loci — *"Contraposing gives the constraint its real
shape. If **either** axiom holds, the Born rule is forced"* (and the Tenet 2 paragraph:
*"Local tomography is one of two axioms **either** of which forces the Born rule"*) —
while stating the boxworld counterexample in its own body: *"Boxworld... is also
locally tomographic."* Same contradiction, same source, opposite article. It also
inherits the "on pain of signalling" graft. A P2 refine-draft task has been queued.

`obsidian/concepts/causal-consistency-constraint.md` was checked and is **clean** — it
scopes to "purification and no-signalling" throughout and never claims the disjunction.

## Stability Notes

- Physicalist / Many-Worlds / eliminativist disagreement with the Map's use of the framework is a bedrock framework-boundary standoff. Do not re-flag as critical.
- **Do not re-flatten the conditional.** The premise-list is *quantum state space and reversible dynamics, plus purification or local tomography*. Dropping the first clause and substituting no-signalling is the exact error this review corrected, and it has now been made twice in this cluster (2026-08-16 in the sibling, 2026-08-17 here). The tell is any sentence of the form "either axiom plus no-signalling forces the Born rule": boxworld refutes it.
- **Do not restore "on pain of signalling" to the disjunctive form.** Only the purification branch carries a signalling lever; Galley & Masanes' toy theory is the standing counterexample for the other branch.
- The 2026-07-25 review recorded "no critical issues; converged." That was correct *for the article as it then stood*. The two refine-draft passes since reopened the payload, and a converged article is only converged until something moves under it — this cluster's history is a good argument for re-running §2.4 whenever the References block changes, rather than trusting a prior ledger.