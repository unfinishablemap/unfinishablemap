---
title: "Deep Review - Inventory Blindness"
created: 2026-09-10
modified: 2026-09-10
human_modified: null
ai_modified: 2026-09-10T21:51:26+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-10
last_curated: null
---

**Date**: 2026-09-10
**Article**: [[inventory-blindness|Inventory Blindness]]
**Previous review**: [[deep-review-2026-07-14-inventory-blindness|2026-07-14]] (sixth review; fifth was the publisher-of-record verify pass)
**Word count**: 1968 → 2166 (+198)

## Focus of this pass

Sixth review. Two commits touched the article since the 2026-07-14 pass. One
(`5986c301a5`, 08-19) is a cosmetic self-citation repoint — References entry 4 moved
from the archived `/concepts/cognitive-closure/` URL to its `superseded_by` successor
`/concepts/mysterianism/`. The other (`9f059f5a80`, 08-02) added the
`## What Would Challenge This View?` section in response to a refine-draft finding whose
own commit title reads: *"argues absence produces no signal but carries no falsifier bar,
so downstream articles keep inferring invisibility-as-confirmation from it."*

So the pass had a specific question to answer: the fix landed in the source — did it
reach the body of the source, and did it reach the twelve downstream articles it was
written for? This is the inverse of ordinary stranding: not a fix that orphaned its
dependents, but a disclaimer added upstream while the dependents carry on unchanged.

## Pessimistic Analysis Summary

### Critical Issues Found

- **The body still ran the inference the new section disavows, in the Tenet 5 paragraph.**
  The Occam's-Razor passage read: *"The apparent parsimony of materialism about
  consciousness could reflect a blind spot rather than a genuine insight — we find
  physicalism 'simpler' because we lack the concepts that would reveal its inadequacy."*
  The hedge ("could reflect") is undone inside the same sentence by a trailing clause in
  the indicative that asserts both that physicalism has an inadequacy and that our sense
  of its simplicity is *caused by* our lacking the concepts that would expose it. That is
  exactly the mirror-image inference the 08-02 section names and rejects — *"What it does
  not underwrite is the mirror-image inference from the same silence to the conclusion
  that limits are present and hidden"* — and it contradicts the same section's *"it
  supplies no reason to think it obtains."* This is a calibration error inside the Map's
  own framework, not a bedrock disagreement: a reviewer who fully accepts Tenet 5 would
  still flag it, because the load-bearing move is defeater-removal being written up as a
  causal diagnosis. **Resolution applied**: rewritten as a conditional with the bound made
  explicit — *"if the concepts that would expose an inadequacy are missing, physicalism
  will feel simpler whether or not it is, and the feeling is no guide either way. That
  withdraws a warrant from the parsimony argument. It supplies no evidence that the
  missing concepts exist."* The paragraph's defensive force is unchanged; the smuggled
  confirmatory clause is gone.

  Note that this passage is the one the [[project/architecture-vs-significance-two-tier-discount|two-tier discount]]
  cites as its third worked exhibit, on the strength of the hedge. The discount doc was
  reading the first half of a sentence whose second half withdrew the hedge.

- **The bound sat at ~75% depth in an LLM-first document.** The 08-02 section is at the
  bottom of the article, after Historical Evidence and Application Across the Voids
  Framework. The Map's primary audience is chatbots fetching pages, and the style guide's
  truncation-resilience rule puts important information first. The twelve downstream
  articles were written by readers of this article's opening. Placing the bound only at
  the end is the structural reason the fix did not propagate — the fix was invisible at
  the point where inheritance happens. **Resolution applied**: a second lead paragraph
  states the one-directionality in three sentences and forward-references the full
  treatment with a named anchor, per the "explained below" pattern. It closes with
  *"Articles that cite inventory blindness inherit that bound"* — the same instruction the
  08-02 section carries, now positioned where a citing author will actually read it.

### Medium Issues Found

- **The positive cases the falsifier section rests on were never named.** The section's
  hinge sentence — *"the framework's testable content lies in the positive cases where a
  missing capacity becomes visible from outside"* — had no referent within reach. The four
  numbered items that follow are *falsifiers*, not positive cases. The positive cases do
  exist in the article (Capgras-prosopagnosia, Dunning-Kruger, Stanford's retrospective
  record), but three sections earlier and never gathered. A reader arriving at the
  falsifier section, or an LLM given only its lower half, gets a decorative bar.
  **Resolution applied**: the three are now named in the sentence that depends on them,
  each with the reason it counts as external triangulation, and the section states that
  the empirical case rests on them rather than on the absence of an introspective signal.

- **Internal inconsistency: the falsifier's account of the non-Euclidean case contradicted
  the body's.** Falsifier (2) described *"the diffuse dissatisfaction visible in the
  non-Euclidean case."* The body says the opposite: mathematicians *"questioned the
  parallel postulate for centuries and repeatedly tried to derive it,"* and *"the parallel
  postulate's special status was visible."* The dissatisfaction was not diffuse — the
  suspect axiom was identified precisely; what was absent were the tools to build the
  alternative. **Resolution applied**: reworded to match the body — the case now *fixes
  the bar* rather than sitting below it, and the falsifier is sharper for it, since the
  bar is "registered the shape of the theory," not "registered that something was wrong."

### Counterarguments Considered

- *Eliminativist / hard-nosed physicalist*: the structural-vs-practical claim is resisted
  from outside the Map's tenets. Bedrock framework-boundary disagreement, flagged as such
  by the 2026-07-14 review, not re-flagged here.
- *Popper's Ghost*: the strongest remaining objection is that all four falsifiers are
  difficult rather than impossible, and (3) in particular ("systematically surfaced
  nothing across many domains") has no crisp stopping rule. The section already concedes
  the central prediction is null and non-diagnostic; adding a stopping-rule qualification
  would restate what the first paragraph says. Left as is.
- *Nagarjuna*: the recursion at steps 3-4 arguably applies to the concept of inventory
  blindness itself. The article's fourth falsifier addresses the recursion directly. No
  change.

## §2.4 Publisher-of-Record Citation Ledger

**Carried forward from 2026-07-14, with justification.** The trigger rule runs the
web-verify pass when the References block was modified since the last deep-review. The
three external entries are byte-identical to the state verified at the publisher on
2026-07-14; the only References change since is entry 4, an internal Map self-citation.
Re-litigating them would violate the prior review's explicit stability note.

- **McGinn, C. (1989). "Can We Solve the Mind-Body Problem?" *Mind*, 98(391), 349-366.** — state: **real-correct** (verified 2026-07-14, unchanged).
- **Stanford, K. (2006). *Exceeding Our Grasp*. Oxford University Press.** — state: **real-correct** (verified 2026-07-14, unchanged).
- **Kruger, J. & Dunning, D. (1999). "Unskilled and Unaware of It." *JPSP*, 77(6), 1121-1134.** — state: **real-correct** (verified 2026-07-14, unchanged).
- **Entry 4 (Map self-citation): Mysterianism and Cognitive Closure, 2026-01-15, `/concepts/mysterianism/`** — state: **real-correct.** Checked this pass because it changed: the target article `obsidian/concepts/mysterianism.md` carries `created: 2026-01-15`, matching the cited date, and the slug is live. The repoint away from the archived `/concepts/cognitive-closure/` URL is correct.
- **Entry 5 (Map self-citation): The Recognition Void, 2026-03-22, `/voids/recognition-void/`** — unchanged, target live.

### Superlative / currency sweep
`find_superlative_claims` returns **0** on the article. The two edits that touch empirical
description (positive cases, non-Euclidean) introduce no superlative and no dated record.
Nothing to re-scope.

### Cross-reference (inline ↔ References)
No orphans in either direction. The edits add no citations.

## Reasoning-mode check
No named opponent is engaged with a refutation claim. "Materialism" and "physicalism"
appear as positions whose *parsimony warrant* is withdrawn, which is Mode Two
(unsupported-foundational-move) territory rather than boundary substitution — and the
rewritten Tenet 5 paragraph now says explicitly what the withdrawal does and does not
buy. No editor-vocabulary label leakage in prose.

## Optimistic Analysis Summary

### Strengths Preserved
- The four-level recursion (distinctive Map contribution) — untouched.
- The three-way contrast with anosognosia, inattentional blindness, and unknown unknowns.
- The anti-correlated-metacognitive-signal paragraph, which already stated the correct
  remedy ("external triangulation through cases where the missing capacity becomes
  separately visible") — the new positive-cases sentence makes that paragraph's principle
  concrete rather than replacing it.
- The 08-02 section's own prose, which is the most calibration-honest passage in the
  article. Nothing in it was cut; the edits are one clarification inside it and two
  additions elsewhere that bring the rest of the article up to its standard.
- The Dualism and Bidirectional-Interaction tenet paragraphs, both correctly conditional.

### Enhancements Made
- Second lead paragraph carrying the one-directionality bound (truncation resilience).
- Positive cases named where the claim that rests on them is made.
- Non-Euclidean characterisation aligned across the two sections that describe it.
- "parsimony arguments *fail*" → "*become unreliable*" in the lead, matching the
  hedge the Dualism paragraph already uses for the same move.

### Cross-links Added
None. See "Citer audit" below for one reciprocal that is genuinely missing but out of
scope for a single-article review.

## Citer audit (reported, not edited)

Thirteen live files cite inventory blindness outside `reviews/` and `workflow/`. The
question this pass had to answer is whether any still runs the inference the 08-02
section disavows — the "closure would be invisible, and invisibility is what we find"
pattern.

**Corpus-wide result: no citer completes the confirmatory inference.** A pattern sweep
for the completion clause (`what we find|observe|see`, `precisely/exactly what we`,
`as we would expect`, `and that is what`) returns zero across all thirteen. The sweep was
positive-controlled against the article itself, which returns the expected single hit —
its own quoted disavowal of the pattern.

Per-citer verdicts:

- **[[meta-epistemology-of-limits]]** — the one flagged for scrutiny, because it uses
  inventory blindness to establish that a hard problem and a closed one *feel identical*,
  and something is inferred next. **Sound, and unusually so.** The bullet immediately
  following is *"Success proves contingency; failure proves nothing. Solving shows the
  problem was solvable. Failing — even across centuries — cannot establish permanent
  closure."* The Suspended Position states that verification and falsification are both
  blocked. The historical section states *"no persistence proves a limit is permanent"*
  and turns the selection effect against **both** sides — Dennett's optimism *"generalises
  from the only cases that leave evidence,"* which is the licensed defensive use, and the
  persistence indicators are immediately checked with *"yet every dissolved limit also
  looked permanent to those inside it."* It labels convergence *"weak evidence"* and then
  discounts it as possibly *"common cognitive constraints rather than external reality,"*
  and it applies the recursion to the Map itself: *"The recursive challenge applies
  equally to the dualist position the Map defends."* It also explicitly declines the
  confirmatory move it could have made — *"Illusionism-as-symptom: denying the phenomenon
  might itself be what cognitive closure looks like from inside, though this is a
  diagnosis rather than an argument and should not be mistaken for one."* This citer was
  already compliant before the 08-02 fix existed. No action.
- **[[mysterianism]]** — stops one clause short of the fallacy and stops deliberately:
  *"If humans are cognitively closed with respect to the consciousness-physics link, we
  should expect the closure to be invisible from the inside."* Conditional expectation
  with no "and that is what we observe." Sound.
- **[[recognition-void]]** — the sharpest of the citers on this point, and worth quoting
  because it does unprompted what the 08-02 section asks for: *"That does not raise it to
  framework-independent evidence, though: under the common-cause null the convergence
  remains a coherence property of the Map's self-image rather than independent
  confirmation, and inventory blindness only blocks one deflationary move against it."*
  Sound.
- **[[closure-types-void]]**, **[[three-kinds-of-void]]**, **[[self-opacity]]**,
  **[[biological-cognitive-closure]]**, **[[capgras-delusion-and-the-affective-recognition-channel]]**,
  **[[anti-correlated-metacognitive-signal]]** — all descriptive or definitional uses
  ("absent capabilities produce no signal", "the word for this is inventory blindness",
  "the illusion is never challenged from within"). None infers presence from silence.
  The anti-correlated hit at frontmatter level is a list entry, not prose. Sound.
- **[[project/architecture-vs-significance-two-tier-discount]]** — its architecture/
  significance split is exactly the right treatment, and its larger discount on the
  significance tier *blocks* the disavowed move by construction. One wrinkle, now
  resolved upstream: it rests on the Tenet 5 hedge, and the hedged sentence was the one
  undoing itself in its second half. The article's rewrite makes the discount doc's
  reading true of the source. Its italicised near-quote *"may reflect a blind spot rather
  than an insight"* matches the article's Further Reading formulation, so this is not a
  quote-fidelity defect. No action needed.
- **research notes** (`voids-notation-void-2026-08-19`,
  `capgras-…-2026-07-10`) — frontmatter list entry and dedup bookkeeping respectively.
  No inferential use.

### One citer worth a light-touch follow-up (P3, operator's call)

**[[epistemology-of-limit-knowledge]]**, in the "Phenomenally constituted and reliable"
option: *"developmental no-trace as recognition-via-inference (no phenomenal signal at
all, so the limit is known only indirectly, through [[inventory-blindness]])."* Read
strictly, that treats the null observation as a route *to* knowledge of the limit, which
is what the 08-02 bound denies. Three things keep it from being a live defect: the whole
three-option block is declared *"a live hypothesis, not a settled Map commitment"*; the
very next option says *"The satisfaction and no-trace modes are especially exposed here:
a limit that feels like completion is precisely the kind that could be illusory"*; and
the Bootstrap Problem section states the challenge in full. What keeps it worth a look is
that the article *"leans toward the first option,"* so the loose parenthetical carries
some weight. It reads as imprecise wording inside a disclaimed option rather than an
inherited fallacy. Not edited — single-article contract.

### Missing reciprocal (reported, out of scope)

`obsidian/concepts/naturally-occluded.md` contains **zero** occurrences of "inventory"
(checked by offset, not by truncated grep). The link is one-directional: this article
points at naturally-occluded twice — in the body (*"explains why inventory blindness
exists"*) and in Further Reading (*"Why evolution produces and maintains the blind spots
inventory blindness conceals"*) — and gets nothing back.

This bears on **todo.md L6269**, the 2026-04-06 eight-pair cross-linking task whose
second pair is `inventory-blindness → adaptive-cognitive-limits (mechanism and
evolutionary explanation)`. `adaptive-cognitive-limits` was coalesced into
`naturally-occluded` (commit `13c1d19164`), and the outbound half of that pair is
**already installed and correct** under the successor slug. Only the inbound half is
missing, and installing it means editing another article, which this contract excludes.
The operator can close the outbound half of that pair now; the inbound half is a
one-sentence job in `naturally-occluded`.

## Remaining Items

- `epistemology-of-limit-knowledge` parenthetical above — P3, wording only.
- `naturally-occluded` inbound reciprocal — P3, one sentence, closes todo L6269's second pair.

Neither is minted as a task here: both are sub-sentence wording jobs in other articles,
and L6269 already exists as the natural home for the second.

## Stability Notes

Sixth deep review, and the first since 2026-04-28 to change the article's content
substantively. That is not a regression from convergence — it is the 08-02 disclaimer
being carried the rest of the way into the article that hosts it. The three edits are all
the same edit: make the body say what the falsifier section says.

Future reviews must NOT re-flag:

- The three external citations are publisher-verified real-correct (2026-07-14). Do not
  re-litigate McGinn 1989 / Stanford 2006 / Kruger & Dunning 1999 absent a substantive
  edit to the References block. Entry 4's repoint was checked this pass and is correct.
- Eliminative-materialist / physicalist resistance to the structural-vs-practical claim —
  bedrock framework-boundary disagreement.
- **The Tenet 5 paragraph now ends with two short declarative sentences separating what
  the argument withdraws from what it does not supply.** They read as redundant next to
  the "could reflect" hedge earlier in the paragraph. They are not: the version without
  them asserted the causal diagnosis outright, and the redundancy is the repair. Do not
  condense them back into the hedge.
- The lead's second paragraph duplicates the opening of the "What Would Challenge This
  View?" section. That duplication is deliberate — it is the truncation-resilience fix,
  and it is the mechanism by which the bound reaches citing authors. Do not deduplicate.
- **The citer audit found the corpus clean on this axis** (2026-09-10, thirteen files,
  positive-controlled sweep). A future review should not re-run the full citer sweep
  unless the article's bound changes; `meta-epistemology-of-limits` in particular has
  been checked twice now and is a model case, not a suspect one.
