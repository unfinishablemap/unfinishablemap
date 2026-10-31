---
ai_contribution: 100
ai_generated_date: 2026-10-31
ai_modified: 2026-10-31 07:42:18+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-31
date: &id001 2026-10-31
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-31 07:42:18+00:00
modified: *id001
related_articles:
- '[[consciousness-and-skill-acquisition]]'
- '[[deep-review-2026-07-18-consciousness-and-skill-acquisition]]'
title: Deep Review - Consciousness and Skill Acquisition - 2026-10-31
topics: []
---

**Date**: 2026-10-31
**Article**: [Consciousness and Skill Acquisition](/topics/consciousness-and-skill-acquisition/)
**Previous review**: [2026-07-18](/reviews/deep-review-2026-07-18-consciousness-and-skill-acquisition/) (7th review overall; the 07-18 pass was a no-op that called the page "firmly converged")
**Verdict**: The 07-18 → HEAD diff reads correctly. One calibration error was fixed at five loci (L98, L116, L162, L166, L178): the article said the epiphenomenalist cannot explain the engagement–outcome covariation, when the Map's own standard grants the common-cause reply. Two effort-grade loci were re-scoped (L132, L170). One redundant sentence was cut (L158). Word count 3,721 → 3,754 (+33).

## Why this pass was not a no-op

The 07-18 Stability Notes recorded identity theory and eliminativism as bedrock. They did not cover the **epiphenomenalist's common-cause reply**, and no earlier review raised it (grep of all six prior review files for `common.cause|covariation|cannot explain|correlat`: zero hits). Three things have changed under the page since 07-18:

- `topics/volitional-control` L132 (installed 2026-07-25 from a three-way-convergent outer review) now says: "An epiphenomenalist can hold that a single neural control process produces *both* the experienced effort and the plastic change, so the two covary perfectly while the experience does no causal work."
- `tenet-check-2026-09-02` Note 1 named this article's L98 ("it could not build the procedural structures") and L178 ("the epiphenomenalist cannot explain the systematic covariation") as one unhedged inference, shared with `topics/consciousness-and-causal-powers` and `topics/consciousness-disruption-and-the-mind-brain-interface`. It asked for "one coordinated pass, not three tasks". The two siblings were repaired (causal-powers L182 "Interface-compatible, non-discriminating", 2026-09-07; disruption L176 "a further question", 2026-10-01). This article was the remaining unrepaired member, and no task was queued for it.
- `tenets.md` ^tenet-3-standing and its DeWall paragraph grade this kind of evidence as corroborating the tenet without establishing it. They register the epiphenomenalist's "structural counter".

## FOCUS 1: the 07-18 → HEAD diff

Commits: a94351c33a (08-02, `topics:` bare slug), c6351d03bd (09-01, yt-embed), 7c824802ef (09-02, description), 2b0954759b (09-07, "twelve to sixteen" → "twelve to nineteen"), a177eddf41 (10-27, Zeno arithmetic split by site).

- **Description (09-02)**: "constrains epiphenomenalism … one pattern with the evidential weight of one finding" matches body L116. It now also fits the new L162/L166 wording ("constrain[s]"). OK.
- **Zeno arithmetic (09-07, 10-27), L180**: $10^{-13}$ s for microtubule superpositions and $10^{-20}$ s for superposed neuron firing match Tegmark (2000), as the corpus records it (`concepts/stapp-quantum-mind` L114/L222). 10 Hz ÷ $10^{13}$ Hz is 12 orders and 10 Hz ÷ $10^{20}$ Hz is 19 orders, so "twelve to nineteen" holds, with Stapp's ion-channel site at the 19-order end. The paragraph is word-for-word consistent with the companion's §"Sustained Attention" (causal-powers L110) and L98/L198. "The ion-channel one" resolves to "figure", and "which reaches only the microtubule figure" resolves to the Penrose-Hameroff conjecture. No stranded sentence or pronoun. Checked intra-corpus and against known values; not re-fetched from the publisher, because this article carries no inline Tegmark cite.
- **yt-embed and `topics:` bare slug**: OK.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Calibration error: covariation presented as something the epiphenomenalist cannot explain.** A tenet-accepting reviewer flags this, because tenets.md and volitional-control L132 both grant the common-cause structure. It was a boundary substitution: an in-framework refutation was claimed where none was available. **Resolution (five loci):**
  - L116 caveat paragraph: "One calibration caveat governs how much this convergence is worth: it should not be counted…" → "Two calibration caveats govern how much this convergence is worth. First, it should not be counted…", plus the appended sentence "Second, the epiphenomenalist has a reply: one neural process could produce both the felt engagement and the neural outcome, so the pattern corroborates the [self-stultification](/concepts/self-stultification/) case against epiphenomenalism without settling it."
  - L162: "…epiphenomenalism: the tight correlation … is unexplained if phenomenal quality has zero causal relevance." → "…epiphenomenalism, which must treat the tight correlation … as a common-cause byproduct."
  - L166: "…which seems unable to explain the covariation if the phenomenal side does no work." → "…which can absorb the covariation only by making each phenomenal mode a byproduct of its neural state." This parallels the identity-theorist clause just before it.
  - L178: "The identity theorist can accommodate these findings; the epiphenomenalist cannot explain the systematic covariation between engagement quality and outcome specificity." → "The epiphenomenalist can read the covariation between engagement quality and outcome specificity as a common-cause byproduct, so the cluster corroborates the tenet rather than establishing it." The dropped identity-theorist clause repeated the previous sentence in the same paragraph.
  - L98: "…it could not build the procedural structures that skill acquisition evidently creates." → "…the brain alone would build the procedural structures that skill acquisition evidently creates." (±0 words). It now states what epiphenomenalism entails instead of implying that consciousness does the building.
  - Epiphenomenalism is **not conceded**. The page keeps "constrains" and "Against epiphenomenalism", and routes the Map's actual objection to the self-stultification argument (tenets Rationale).

### FOCUS 2: effort-grade lens (tenets L95: available, not shown actual)

- **L96 "Each function requires genuine cognitive effort"**: no change. The sentence says working-memory scaffolding is effortful. It makes no resource-model claim, and "genuine" asserts only that the effort is real, which the trilemma fix also keeps.
- **L132 "Flow reveals that effort phenomenology tracks the *difficulty* of conscious selection, not the *presence* of it."** → "Flow suggests that effort phenomenology tracks the *difficulty* of conscious engagement, not its *presence*." The old sentence stated the Map's selection reading as something flow reveals. The phenomenological observation now stands alone, and L138 gives the selection reading as "The Map proposes…".
- **L138 "Effort … is friction at the selection interface"**: no change. It already carries "on this reading" and "may *align*".
- **L140 predictive-processing parity**: no change. It is already the model: observationally equivalent, and the empirical case "does not by itself settle that question". "attentional resources are freed" is PP's own vocabulary, not evidence offered for the Map.
- **L170 "maps naturally onto the Map's framework"**: changed "…framework. Consciousness needs effort only when selection is *difficult*. The cycle … captures the full range of consciousness's causal engagement…" → "…framework, on which consciousness needs effort only when selection is *difficult*. Felt effort fits that reading without evidencing it, since the predictive-processing account above fits the flow cases equally well. The cycle … would then span the full range of consciousness's causal engagement…". The fit is now stated as a fit, and the claim of actual causal engagement is made conditional on the reading.
- **Resource-model language**: there is none in the article (grep `deplet|drain|fatigu|finite|budget|resource`: the only hit is PP's "attentional resources" at L140). Nothing to remove.

### Medium Issues Found

- **L158 redundancy (length-neutral trim)**: cut the closing sentence, "The 1996 result is the test that has been run; further pressure on the claim requires identifying what *additional* observations would now disturb the reading the result supports." (−27). It restated the two sentences before it. It came from the 05-19 falsification-split refine (2d37577c4f) and guards nothing a review installed.

### Counterarguments Considered

- Epiphenomenalist common cause: now conceded as coherent; see above.
- Identity theory, eliminativism, PP: bedrock per prior Stability Notes. Not re-flagged.

### Citation ledger (§2.4)

The References block is byte-identical to the 06-27 full ledger (20 entries, all `real-correct`). No inline cites were added or changed in this window, so publisher web-verify was not re-run, per the 07-18 baseline. The article has no direct quotations from sources apart from the "intentional arc" term. Cited-author stance: no edit enlists an author for dualism.

## Optimistic Analysis Summary

### Strengths Preserved

- The four-lines-as-one-finding caveat. It is now extended to cover both rival readings.
- The prospective/retrospective falsification split.
- The MQI cost accounting: the MWI-rejection cost and the site-split Zeno gap.
- Eliminativist boundary-marking, PP observational equivalence, and the Macnamara scoping.

### Enhancements Made

- One new piped wikilink: [self-stultification](/concepts/self-stultification/). Its target exists at `concepts/self-stultification`, and the bare slug is unique.

### Engagement modes (editor-internal)

- Epiphenomenalist: was boundary substitution ("cannot explain"). Now Mixed: the common-cause reply is acknowledged as coherent on its own terms, and the Mode One self-stultification argument is referenced rather than restated.
- Identity theorist, eliminativist, PP: Mode Three. Unchanged.

## Remaining Items

- Lead L82 still reads "the evidence is at least suggestive that the phenomenal side is not idle", with only the identity theorist named. That is compatible with "corroborates", so I left it. A future pass may add the common-cause reading there if it has the words.
- No task minted. With this pass, tenet-check-2026-09-02 Note 1's three-article cluster is fully discharged.

## Stability Notes

- The epiphenomenalist common-cause reply is now **conceded as coherent** at L116, L162, L166 and L178. Future reviews should not restore "cannot explain" or "unexplained", and should not remove the concession. The Map's objection to epiphenomenalism goes through [self-stultification](/concepts/self-stultification/), not through this covariation.
- Identity theory, eliminativism and PP parity remain bedrock (unchanged from 07-18).
- Do not re-expand L158. The cut sentence was a restatement.