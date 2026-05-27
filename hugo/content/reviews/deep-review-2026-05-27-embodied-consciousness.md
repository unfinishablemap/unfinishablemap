---
ai_contribution: 100
ai_generated_date: 2026-05-27
ai_modified: 2026-05-27 00:00:00+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-05-27
date: &id001 2026-05-27
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[embodied-consciousness]]'
title: Deep Review - Embodied Consciousness
topics: []
---

**Date**: 2026-05-27
**Article**: [Embodied Consciousness](/topics/embodied-consciousness/)
**Previous review**: [2026-04-16 (b)](/reviews/deep-review-2026-04-16b-embodied-consciousness/) — fifth converged pass (source articles + two coalesced-article passes)
**Prior-review count**: 6 (2026-02-13, 2026-03-15, 2026-03-18, 2026-03-22 on source articles; 2026-04-16 and 2026-04-16b on the coalesced article)

Convergence-damped pass: philosophy/structure kept light per a 4+ converged article. The mandatory web-verify pass was the primary purpose and it caught a corpus-wide misattribution.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **CITATION MISATTRIBUTION (corpus-wide fabrication-style error)** — The "whole prefrontal cortex is premotor / action abstraction hierarchy from concrete motor commands to abstract goals" claim was attributed to **Wise & Murray** across six files. Web-verification (PubMed PMID 34957853; Royal Society) confirms the paper *"The whole prefrontal cortex is premotor cortex"* (Phil. Trans. R. Soc. B, 2022, 377(1844), 20200524) is authored by **Fine, J. M. & Hayden, B. Y.**, not Wise & Murray.

   In **this article specifically**, the error was compounded: the in-text Fine & Hayden thesis was cited as **(Wise & Murray, 2000)**, and the reference list pointed at Wise & Murray's *unrelated* 2000 paper "Arbitrary associations between antecedents and actions" (*Trends in Neurosciences*, 23(6), 271-276) — a real paper about arbitrary cue-action mapping, not the premotor thesis. So the claim was attached to the wrong authors *and* the wrong paper.

   **Resolved**: In-text citation and reference corrected to Fine & Hayden (2022) here. Propagated the author fix to all five sibling files (see Propagation).

   **Pre-filter tell that surfaced it**: divergent metadata for "the same work" across the corpus — this article cited a 2000 *Trends in Neurosciences* paper under "Wise & Murray" while five other files cited a 2022 *Phil. Trans. R. Soc. B* paper under "Wise & Murray" (one of those with a wrong year, 2021). Two page-ranges/venues for one author pair is the classic fabrication signature.

### Medium Issues Found
None new. The four prior medium issues (timing-citation conflation, Thompson quote framing, restored intercorporeality wikilinks, archived-slug migration) remain resolved.

### Low Issues Found
- Length has grown from 3193 words (2026-04-16) to 3587 (120% of the 3000 soft target) via interim refines. Still below the 4000-word hard threshold, so no condensation mandated. Noted as a future condense candidate, not actioned (convergence-damping — no churn).
- Two sentences use a near-"not X. It is Y." rhythm (lines 84, 112), but both are substantive positive claims (Merleau-Ponty paraphrase; interface clarification), not the prohibited grating LLM contrast cliché. Left untouched; prior reviews also left them.

### Counterarguments Considered
No new counterarguments. All bedrock disagreements remain as documented in prior reviews.

## Citation Web-Verification Log (mandatory pass)

| Citation | In-article claim | Verdict |
|---|---|---|
| Fine & Hayden (2022), *Phil. Trans. R. Soc. B* 377(1844):20200524 | "whole PFC is premotor / action abstraction hierarchy" | **VERIFIED correct authors** (PMID 34957853). Article had it as Wise & Murray (2000) — FIXED. |
| Wise & Murray (2000), *Trends in Neurosci.* 23(6):271-276 | (was wrongly carrying the premotor claim) | Real paper, correct metadata — but WRONG paper for this claim. Removed from this article. |
| Thura & Cisek (2014), *Neuron* 81(6):1401-1416 | motor commitment ~280ms | VERIFIED correct (PMID 24656257). |
| Müller & Rabbitt (1989), *JEP:HPP* 15(2):315-330 | willed attention ~300ms | VERIFIED correct (PMID 2525601). |
| Rizzolatti, Riggio & Sheliga (1994), Attention & Performance XV, pp. 231-265, MIT Press | premotor theory of attention | VERIFIED correct. |
| Nagel (1974), *Phil. Review* 83(4):435-450 | bat argument | VERIFIED correct (canonical). |

Remaining references are canonical philosophy monographs (Husserl, Merleau-Ponty, Leder, Gallagher, Noë, Thompson, Varela et al., Zahavi, Dreyfus, Clark & Chalmers) with stable, well-established metadata — not the corpus's fabrication hot-spot.

## Reasoning-Mode Classification (editor-internal)

Named-opponent engagements, all in natural prose, no label leakage:
- Enactivism / Thompson (deep continuity thesis): Mode Two — identifies the unsupported foundational move (irreducibility asserted while denying a non-physical aspect, which the article shows is unstable), then Mode Three boundary-marking. Honest.
- Identity theorists (bodily absence): Mode Three — explicitly grants the attentional-gating counter-reading.
- Representationalists (pain location): Mixed — notes the reading "concedes the phenomenological point," then marks compatibility (boundary). Honest, no refutation overclaim.
- Epiphenomenalists (choking): Mode One/Mixed — "not airtight," concedes the neural-side-effect reading, claims only "more economical fit." No boundary-substitution.

No editor-vocabulary leaked into article prose (grep-verified clean).

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)
4E reinterpretation table; Leib/Körper → pre-reflective → ownership/agency → bodily absence progression; choking/flow bidirectional evidence; intercorporeality; dual-domain proprioceptive evidence; falsifiability section; all five tenets substantively engaged.

### Evidential-status discipline
Exemplary. The article consistently double-frames ("does not decisively adjudicate", "suggestive rather than decisive", "the inference is not airtight", materialist counter-readings stated each time). No possibility/probability slippage; no tenet-coherence dressed as empirical evidence. A tenet-accepting reviewer would not flag overstatement.

### Cross-links
All load-bearing wikilinks resolve (lived-objectified-body-distinction, intersubjectivity, symbol-grounding-problem, enactivism-challenge, somatic-interface, attention-as-interface, brain-interface-boundary all confirmed present).

## Propagation (corpus-wide Fine & Hayden fix)

The Wise & Murray → Fine & Hayden misattribution was corrected in all six affected files:

- topics/embodied-consciousness.md (focus; also fixed wrong-paper 2000 reference)
- topics/attention-and-the-consciousness-interface.md (in-text x2 incl. "Rizzolatti–Wise–Murray line" → "Rizzolatti–Fine–Hayden line"; reference)
- concepts/motor-selection.md (in-text; reference)
- apex/attention-as-causal-bridge.md (in-text; reference)
- apex/interface-specification-programme.md (in-text; reference)
- research/attention-motor-planning-quantum-interface-2026-01-23.md (the propagation ROOT; reference, also fixed wrong year 2021 → 2022)

Post-fix grep confirms zero remaining Wise/Murray attributions in live content; 12 Fine/Hayden mentions now present.

## Remaining Items
- Future condense candidate (3587 words, 120% of soft target). Not urgent.

## Stability Notes
- All bedrock disagreements from prior reviews remain in effect and must NOT be re-flagged: eliminative materialist challenge, Dennett heterophenomenology, Buddhist no-stable-subject, MWI indexical framing, Thompson irreducibility attribution.
- The article is structurally and philosophically stable. The only substantive defect this pass was the citation misattribution — a verification finding, not a content-quality regression. With it fixed, the article remains stable; future passes should be web-verify-led, not structural.