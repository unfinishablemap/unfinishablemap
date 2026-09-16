---
title: "Deep Review - Direction of Fit"
created: 2026-09-16
modified: 2026-09-16
human_modified: null
ai_modified: 2026-09-16T19:56:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-16
last_curated: null
---

**Date**: 2026-09-16
**Article**: [[direction-of-fit|Direction of Fit]]
**Previous review**: [[deep-review-2026-07-16-direction-of-fit|2026-07-16]] (5th; earlier 2026-06-03, 2026-05-09, 2026-03-22, 2026-02-23)

## Verdict: One attribution error corrected (Searle "double direction of fit")

Sixth deep review. The article was nominated because three cross-link insertions
(2026-07-18) bumped `ai_modified`. Those insertions are clean. But the pass ran a
lens no prior review had run — claim-match of the *Searle section bullets* against
Searle's raw text rather than the canonical citation metadata — and it surfaced a
substantive misattribution that had survived five "converged" passes.

## Pessimistic Analysis Summary

### Critical Issues Found
1. **Misattribution — "double direction of fit" for intentions-in-action
   (corrected).** The article stated: "Searle argued that intentions-in-action
   have both [directions]: they represent the action being performed
   (mind-to-world) while causing that very action (world-to-mind)." Searle's
   *Intentionality* (1983, ch. 3) table and his 1980 *Cognitive Science* paper
   both give the intention in action **world-to-mind direction of fit** and
   **mind-to-world direction of *causation***: "the Intentional component has the
   world-to-mind direction of fit… And the direction of causation is from the
   experience of acting to the event." The article had (a) collapsed Searle's
   fit/causation distinction into a "double direction of fit", and (b) swapped
   the labels (calling the representing "mind-to-world" and the causing
   "world-to-mind", the reverse of Searle's assignment). Searle's genuine
   double-direction category is *declarations* in the speech-act taxonomy
   (Searle 1979; Searle & Vanderveken 1985), not intentions. Corrected: the
   bullet now presents direction of causation as Searle's paired notion, gives
   declarations as the double-fit case, and says explicitly that Searle does
   not extend double fit to intentions.
2. **Downstream Map paragraph built on the error (corrected).** The
   "Direction of Fit and Agent Causation" section opened a paragraph with "The
   double direction of fit in intentions-in-action is particularly telling" and
   mapped that non-Searlean claim onto Bidirectional Interaction. Rewritten on
   Searle's actual fit/causation pairing (perception: mind-to-world fit,
   world-to-mind causation; intention: the reverse), which supports the Map's
   two-way picture *better* and without misattribution. Added a
   cited-author-stance clause: Searle, a biological naturalist, would locate the
   mind-to-world causation in the neural realiser; the Map's step beyond him is
   marked as the Map's.

### Medium Issues Found (corrected)
- **"Null direction" bullet misfiled undirected anxiety.** The article listed
  "emotions like undirected anxiety, moods" as Searle's null-direction states.
  Searle's raw text: "there are forms of nervousness, elation, and undirected
  anxiety that are not Intentional" — i.e. the question of fit does not arise
  for them. His no-direction *Intentional* states are cases like "I am sorry
  that you left the room, my sorrow has no direction of fit" (1980, p. 49);
  they presuppose their content. Bullet rewritten to give the sorry/glad
  examples and to separate the non-Intentional case. The later "emotion
  problem" sentence ("Undirected anxiety may lack propositional content
  entirely") was already consistent with Searle and is unchanged.

### Low Issues
None.

### Counterarguments Considered
All six personas re-engaged. Bedrock disagreements (eliminative materialism on
Bayesian normativity; functionalism via the thermostat; Buddhist non-self)
remain properly handled at the framework boundary and are not re-flagged.
Quantum-skeptic and Many-Worlds personas remain not-applicable (no quantum
mechanism invoked). The Hard-Nosed Physicalist persona is the one that caught
the Searle error: a naturalist reader of Searle knows the fit/causation table.

## Citation Web-Verify (per-cite ledger)
Sources this pass: raw text of Searle *Intentionality* (yanko.lib.ru mirror,
abridged; grep-verified for the fit/causation table and the undirected-anxiety
passage), raw PDF of Searle (1980) "The Intentionality of Intention and Action",
*Cognitive Science* 4 (pdftotext + NFKC grep), raw PDF of Humberstone (1992),
Wikipedia "Direction of fit" raw HTML (for the Searle 1979 declarations /
null taxonomy). WebSearch summaries were treated as leads only — one of them
quoted the Map's own sentence back (self-contamination) and was discarded.
- Anscombe, G.E.M. (1957). *Intention*. Basil Blackwell — real-correct
  (metadata re-verified 2026-07-16; not re-verified this pass; coinage hedge
  left as-is per stability note).
- Searle, J. (1983). *Intentionality*. Cambridge University Press — metadata
  real-correct; **claim-match: two bullets were wrong (double direction; null
  direction examples) — corrected as above.** Result-direction leg: the
  fit/causation table is now reported in Searle's direction. Cited-author-stance
  leg: Searle's biological naturalism now stated where the Map goes beyond him.
- Humberstone, I.L. (1992). Direction of fit. *Mind* 101(401), 59-84 —
  real-correct (raw PDF fetched; reference-only by design).
- Smith, M. (1994). *The Moral Problem*. Blackwell — real-correct
  (canonical; not re-verified; reference-only by design).
- No superlative/currency claims detected (`find_superlative_claims` empty).
- Inline ↔ References: Anscombe and Searle cited inline; Humberstone and Smith
  intentionally bibliography-only (prior stability note). No orphans introduced.

## Attribution Accuracy Check
- Anscombe shopping-list analogy: correct ✓
- Searle systematisation: mind-to-world / world-to-mind bullets correct ✓;
  double-direction bullet was a misattribution — FIXED ✓; null-direction
  examples were misfiled — FIXED ✓
- Source/Map separation: the agent-causation paragraph now marks the Map's
  step beyond Searle explicitly ✓
- No dropped qualifiers, overstated positions, false shared commitments ✓

## Possibility/Probability Calibration Check
- Placebo: "suggestive" / "contested" — unchanged, correct tier ✓
- No evidential-status upgrade introduced by the rewrite; the new paragraph is
  interpretive mapping, conditional on the tenets ✓

## Reasoning-Mode Classification
Article engages positions generically (eliminative materialism, functionalism,
biological reduction), not named opponents; strict classification does not
apply. The one named source (Searle) is now engaged as: Mode Three for the
phenomenal-vs-neural-realiser question — the disagreement with his biological
naturalism is noted as a framework-boundary matter, not dressed as refutation.
No editor-vocabulary leakage into prose.

## Cross-link Review (the three 2026-07-18 insertions)
- `[[emotion-and-dualism|Emotions]]` inline in the emotion-problem paragraph —
  target exists (topics/), label accurate ✓
- `[[subjective-aim]]` Further Reading — target exists (concepts/), "satisfaction"
  appears 7x in the target; description accurate ✓
- `[[epistemic-emotions]]` Further Reading — target exists (concepts/),
  curiosity 16x / doubt 15x in the target; description accurate ✓

## Optimistic Analysis Summary

### Strengths Preserved
Front-loaded opening; Anscombe exposition; normative-dimension argument;
thermostat analogy; falsifiable "What Would Challenge This View?"; painter
phenomenal-template example; placebo restraint. All untouched.

### Enhancements Made
The rewrite of the agent-causation paragraph is a strengthening as well as a
fix: Searle's own fit/causation pairing gives the Map's Bidirectional
Interaction reading a real textual anchor in a naturalist source, with the
Map's additional step (phenomenal content as the mind-to-world cause) cleanly
separated.

### Cross-links Added
None. All 16 wikilink targets verified live.

## Length
1828 → 2001 words (+173), 80% of the 2500 soft threshold. Below soft; no
length-neutral obligation. No trimming applied.

## Remaining Items
None.

## Stability Notes
- The Searle section now reflects Searle's actual apparatus: fit runs one way,
  causation the other; double fit belongs to declarations; no-direction
  Intentional states are sorry/glad-that-*p* cases; undirected anxiety is
  non-Intentional. Do NOT re-introduce "double direction of fit" for
  intentions — five prior reviews ratified it because they checked citation
  metadata, not the bullets' claim-match against the raw text.
- Prior stability notes stand: coinage hedge ("usually credited to Searle")
  deliberate; bedrock disagreements not critical; placebo tier fixed;
  Humberstone and Smith reference-only.
- Lens coverage as of this pass: citation metadata (5 passes), coinage (1),
  Searle-section claim-match against raw text (this pass), cross-link
  insertion accuracy (this pass). Unrun: none identified for this article.
