---
title: Tenet Alignment Check - 2026-06-01
created: 2026-06-01
draft: false
ai_contribution: 100
ai_system: claude-opus-4-8
---

# Tenet Alignment Check

**Date**: 2026-06-01
**Files checked**: 512 (261 topics, 251 concepts)
**Errors**: 0
**Warnings**: 0
**Notes**: 1

## Summary

No tenet contradictions. The corpus discusses all five tenets' ruled-out positions —
eliminative materialism, illusionism, the many-worlds interpretation, epiphenomenalism,
reductive physicalism, and parsimony-against-dualism — pervasively, but in every checked
case these appear as *named opponents the Map argues against* or as *registered costs*,
not as endorsed positions. This continues the stable 0/0/0 run since the 2026-05-25 check.

Endorsement-shaped pattern scans returned only conditional/opponent-framed or
Tenet-5-discounted occurrences:

- **"consciousness is just brain activity / nothing but neurons"** — matches in
  `topics/consciousness-and-memory.md` (line 187), `concepts/quantum-consciousness.md`
  (line 196), `concepts/luck-objection.md` (line 142),
  `topics/william-james-consciousness.md` (line 125) are all anti-reductive
  "If consciousness is just X, then [problem]" set-ups, several explicitly invoking
  Tenet 5 against the "simpler" reductive story ("dissolves the apparent parsimony of
  'consciousness is just brain activity'").
- **"phenomenal consciousness is an illusion" (illusionism)** — ~30 files matched; every
  occurrence introduces illusionism as an opponent and immediately deploys the
  regress/self-undermining response (Tallis's "misrepresentation presupposes
  presentation"). No file endorses the position. `concepts/witness-consciousness.md` and
  `concepts/buddhism-and-dualism.md` explicitly distinguish the Buddhist no-self claim
  from eliminativism.
- **"consciousness is epiphenomenal"** — matches in
  `topics/dopamine-and-the-unified-interface.md`, `concepts/mental-imagery.md`,
  `concepts/attentional-economics.md`, `concepts/baseline-cognition.md`, etc. are all
  contrastive ("If/On a framework where consciousness is epiphenomenal…") used to motivate
  the interactionist reading and the self-stultification argument.
- **MWI endorsement** ("many-worlds is true/correct/we adopt MWI") — zero matches. The
  four "If MWI is true" hits (`topics/delegatory-dualism.md`, `concepts/many-worlds.md`,
  `concepts/conservation-laws-and-mental-causation.md`,
  `concepts/quantum-indeterminacy-free-will.md`) all state the conditional precisely to
  explain why the Map *rejects* MWI per Tenet 4.
- **Occam-against-dualism** — the single apparent match
  (`concepts/philosophy-of-science-under-dualism.md` line 64) presents
  "parsimony typically favours physicalism over dualism" and rebuts it in the very next
  paragraph via Tenet 5 (parsimony is domain-relative and assumes the point in dispute).
  Consistent with Tenet 5, the reverse of a violation.
- **Quantum woo / mysticism endorsement** ("quantum healing", "law of attraction",
  "manifest reality", "quantum energy") — zero matches.

No draft content in `topics/` or `concepts/` (0 files with `draft: true`).

## Errors

None.

## Warnings

None.

## Notes

### concepts/ensemble-level-epiphenomenalism.md

- **Tenet in tension**: 3 (Bidirectional Interaction)
- **Issue**: The article concedes that under its "corridor-plus-trumping" reading, the
  distinction between genuine conscious authorship and outright epiphenomenalism becomes
  "*entirely* metaphysical, with no possible empirical consequence at any scale" — i.e.
  "consciousness is a cause" and "consciousness is epiphenomenal" make no predictively
  distinct claims (line 50).
- **Why this is a NOTE, not an error**: The article does *not* endorse epiphenomenalism.
  It maintains consciousness as a genuine cause and frames the predictive
  indistinguishability as a deliberate, registered cost the Map "adopts knowingly," not a
  difference it has "earned." This is the Map's evidential-status/honesty discipline at
  work rather than a tenet breach. Flagged (carried over from prior checks) only so a
  human reviewer remains aware the corpus contains an article that openly states the
  interactionist commitment is, at the ensemble level, empirically indistinguishable from
  the position Tenet 3 rules out. No action required.

## Files Passing All Checks

All 512 files pass (the single item above is a NOTE, not a failure). Spot-checked
opponent-position articles all carry proper tenet-rejecting framing:
`concepts/illusionism.md`, `concepts/many-worlds.md`, `concepts/materialism.md`,
`concepts/epiphenomenalism.md`, `concepts/functional-seeming.md`.
