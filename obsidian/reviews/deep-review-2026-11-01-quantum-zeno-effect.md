---
title: "Deep Review - The Quantum Zeno Effect"
created: 2026-11-01
modified: 2026-11-01
human_modified:
ai_modified: 2026-11-01T11:48:29+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-01
last_curated:
---

**Date**: 2026-11-01
**Article**: [[quantum-zeno-effect|The Quantum Zeno Effect]]
**Previous review**: [[deep-review-2026-08-21-quantum-zeno-effect|2026-08-21]] (fourth review; earlier passes 2026-07-14 and 2026-07-20)

## Why this article

It ranked second in the candidate list (score 75) after `topics/forward-in-time-vs-time-symmetric-selection`, which the driver excluded. No open task above `## Completed Tasks` names it as File or Secondary. Its three todo mentions are prose inside other tasks: the agentic-social NEEDS-HUMAN note, a stapp-quantum-mind P3 that cites L78 as a model for its own fix, and a research-gap list. Seven commits had landed on the file since 2026-08-21 (10-05 ×4, 10-12 ×2, 10-27), and none had been read by a deep review. Following the 08-21 stability note, this pass aimed at the new material rather than the argument.

**Length**: 3,240 → 3,231 words (−9) against concepts soft 2,500 / hard 3,500. The page sits in the soft-to-hard band, so the pass was length-negative.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Misattributed figure: "~1,000 observations per window that Stapp's own modelling assumes (Stapp 2007)".** Stapp's book says something different. In *Mindful Universe* (Springer 2007, Google Books id `pArDC3K3O2UC`, search-within endpoint; control query "Zeno" returned 10 hits) p. 127 reads: "…and that uses 10 milliseconds for the time between probing actions. In the model the pertinent quantum states all have the same frequency and are almost stable. These conditions allow the probing frequencies to be ~ 100 hertz." Over a ~300 ms window that is about thirty probing actions, not ~1,000. Searches of the same volume for "1000" and "thousand" return 0, and "per second" and "kilohertz" return 0. Stapp 2000 (arXiv quant-ph/0010029) gives no count and ties process (3) to the "low frequency (< 40Hz)" field scale, and Georgiev 2015 gives none either. The corpus traces the figure to `topics/comparing-quantum-consciousness-mechanisms` (created 2026-02-09). That page's own 2026-05-19 review recorded it as "carried forward from nine prior reviews; requires physical text access". The source research note `research/quantum-zeno-effect-2026-07-14` L108 cites it "per `comparing-quantum-consciousness-mechanisms.md`", so it was never checked against Stapp. **Fixed.** Old: "The lower figure is the same order as the ~1,000 observations per window that Stapp's own modelling assumes (Stapp 2007), but that number is a modelling assumption rather than an independent prediction, and no concrete model supplies events at either rate." New: "The model Stapp describes runs two orders below even the lower figure: 10 milliseconds between probing actions, about 100 per second (Stapp 2007, p. 127), or some thirty per window; no concrete model supplies events at either rate." The correction makes the next sentence easier to read: Stapp (2000) rejects the outpacing premise, and his own rate shows why he has to.
- **Internal contradiction with the positions register: "the leading candidate for the physical channel" / "the mechanism most closely fitted to what this tenet asks for".** P-Q1 holds post-decoherence selection to be "the strongest current mechanism candidate". P-Q4 (in the register since 2026-06-04) holds that Stapp-Zeno "is currently demoted relative to post-decoherence selection", behind the decoherence timescale and the regime criterion. `concepts/stapp-quantum-mind` L128 and L146 already follow the register. This page's Minimal Quantum Interaction paragraph has called Zeno "the leading candidate" since it was created on 2026-07-14, and three reviews passed it. A tenet-accepting reviewer would flag this too, so it counts as a calibration error and not a bedrock disagreement. **Fixed.** Old: "The Zeno effect is the leading candidate for the physical channel through which a minimal, energy-frugal conscious influence could act—selection among existing potentialities rather than injection of force. It is the mechanism most closely fitted to what this tenet asks for, which is why the Map tracks it closely." New: "The Zeno effect offers a candidate physical channel for a minimal, energy-frugal conscious influence—selection among existing potentialities rather than injection of force—which is why the Map tracks it closely. The Map nonetheless ranks it below [[post-decoherence-selection|post-decoherence selection]], behind the decoherence timescale and the Zeno/anti-Zeno regime criterion (P-Q4)." Bare P-Q4 autolinks during sync.
- **Wrong origin story that contradicts the page's own citation: "the Zeno mechanism as the Map uses it traces to the 2007 book".** The same section cites Stapp (2000) for the Zeno-on-a-mixture claim. Stapp 2000 L358 applies the effect explicitly ("putting the same question repeatedly to Nature in rapid succession"; L386 "the Quantum Zeno Effect described above"). The QID paper (www-physics.lbl.gov/~stapp/QID.pdf) has a section headed "The Quantum Zeno Effect" and contains 12 occurrences of "Zeno". Schwartz, Stapp & Beauregard 2005 has a section "(g) The quantum Zeno effect". The sentence was there from creation as a disambiguation note, and the separate claim about where the idea came from was never checked. Label: *documented textual claim*, and it was false. **Fixed.** Old: "This is distinct from his earlier "Quantum Interactive Dualism" writings (LBNL 2005 / *Zygon* 2006); the Zeno mechanism as the Map uses it traces to the 2007 book." New: "The book is distinct from his "Quantum Interactive Dualism" paper (LBNL 2005 / *Zygon* 2006), but the Zeno proposal is older than either: Stapp (2000) already states it." The title-and-year disambiguation is kept. The new text does not say who stated the idea first.
- **Internal contradiction: "could destabilise as easily as stabilise".** The page's own Anti-Zeno section says that on Kofman and Kurizki's result "the caveat is asymmetric rather than even-handed: acceleration is the generic case and suppression the special one." The Bidirectional Interaction paragraph turned that back into an even split. **Fixed.** New: "The anti-Zeno mirror is a live risk here: on [Kofman and Kurizki's result](#the-anti-zeno-effect), destabilisation is the generic case and stabilisation the special one."

### Medium Issues Found

- **Truncated title: Schwartz, Stapp & Beauregard 2005.** Crossref gives "Quantum physics in neuroscience and psychology: a neurophysical model of mind–brain interaction". The reference stopped at "psychology". **Fixed.**
- **Hagan et al. 2002 had no DOI.** Added https://doi.org/10.1103/PhysRevE.65.061901, confirmed at Crossref.
- **Meta-commentary trimmed** to pay for the above: "and the mechanism page should state them plainly rather than smuggle them past the reader" (−14). The two burdens are still stated plainly.

### Publisher-of-Record Web-Verify Ledger (§2.4)

Citations new since the 08-21 ledger:

- **Stapp 2007** (*Mindful Universe*, Springer). Metadata real-correct. **The attached figure was wrong** and has been corrected to p. 127 (above).
- **Stapp 2000** (The importance of quantum decoherence in brain processes), arXiv:quant-ph/0010029, LBNL-46871, 6 Oct 2000. Real-correct. The gloss "rejects the premise that the hold must outpace decoherence, saying the effect survives when the brain state is a mixture" matches the raw PDF L386–387: "the Quantum Zeno Effect described above is not destroyed by the fact that S(t)b is a mixture: that makes no difference at all."
- **Georgiev 2015**, *IJMPB* 29(07), 1550039, DOI 10.1142/S0217979215500393 (Crossref; arXiv:1412.4741). Real-correct. The gloss "a mind projecting in the decoherence basis is redundant with it" matches the raw text: "the action of the mind becomes redundant with the action of the environment", and "If the decoherence pointer basis happens to be the one in which the mind action is intended, then the decoherence alone can achieve the quantum Zeno effect and the mind action will be irrelevant or redundant."
- **Tegmark 2000**, *PRE* 61(4), 4194–4206. Real-correct. The by-site figures added on 10-27 match the paper's table: "Neuron … 10⁻²⁰ s" (colliding ion and colliding H₂O) and "Microtubule … 10⁻¹³ s". The abstract range is "∼10⁻¹³–10⁻²⁰ seconds".
- **Hagan, Hameroff & Tuszyński 2002**, *PRE* 65(6), 061901. Real-correct. The microtubule-only revision "lengthens the decoherence time to 10⁻⁵–10⁻⁴ s" is verified in arXiv quant-ph/0005025. DOI added.
- **Schwartz, Stapp & Beauregard 2005**, *Phil. Trans. R. Soc. B* 360(1458), 1309–1327. Metadata was wrong (subtitle missing) and is fixed. The ion-channel locus is verified in the PMC full text: "At their narrowest points, calcium ion channels are less than a nanometre in diameter … This extreme smallness of the opening in the calcium ion channels has profound quantum mechanical implications." *Considered and kept*: SSB add that the calcium-ion focus "is not meant to suggest that this particular effect is the only place where quantum effects enter into the brain process, or that the quantum process 1 acts locally at these sites." The page claims only that Stapp "locates the quantum uncertainty" at that scale. It does not claim that Process 1 acts locally there, so no qualifier has been dropped.
- **Kobylkov et al. 2019**, *J. R. Soc. Interface* 16(161), 20190716. Real-correct; all eight authors match Crossref. The abstract says the lifetime "is in the range 2–10 µs".
- **Gauger et al. 2011**, *PRL* 106(4), 040503. Real-correct. "at least tens of microseconds" is verbatim in the arXiv:0906.3725 abstract. The dependence on a single-frequency result is verified: the model applies "a 150 nT field oscillating at 1.316 MHz" taken from Ritz et al. 2009.

Quotations carried forward, re-grepped at the raw source this pass:

- Kofman & Kurizki 2000. All four spans are verbatim on the nature.com article page.
- Naskar & Joarder 2023. "Finding the proper value of C0 is our future proposed work" is verbatim across a line break (arXiv:2304.06518 L150–151).
- Ishizaki & Fleming 2009. "was not measured directly", λ = 35 cm⁻¹ and τ_c = 50 fs are verbatim in the PMC2762676 full text.

Other carried-forward citations (Misra & Sudarshan, Itano 1990/1991, Ballentine, Kaulakys & Gontis, Fischer et al., Kominis, Denton, Huh, Reimers) are unchanged since the 08-21 ledger and were not re-litigated.

**Inline ↔ References**: complete in both directions. The new inline "(Stapp 2007, p. 127)" and the second "Stapp (2000)" both resolve to existing entries.

**Empirical-record currency**: no superlative claims were added. "Kominis first framed" is carried and was checked on 08-21.

### Dependency pages changed since 08-21 (all of them had)

- `radical-pair-magnetoreception` (3 commits). The Denton bullet's compass sentence is a **byte-identical** copy of that page's reusable sentence at L62. No drift.
- `process-1-specification-problem` (5). The basis/grain/map wording and both Stapp-2000 and Georgiev glosses agree with it.
- `zeno-dynamics-on-a-decohered-mixture` (2). The "regime" sentence agrees with its lead: confinement holds inside the quadratic window and not once the environment has resolved the alternatives.
- `sign-problem-for-conscious-observation` (5). The magnitude-versus-direction sentence and the regime criterion still match L31–33.
- `stapp-quantum-mind` (18) already defers to P-Q4. This page now agrees with it.
- `post-decoherence-selection` (edited today) is linked, not quoted.
- No Map-internal quotation marks on this page point at another page, so there was nothing to re-quote.

### Reasoning-mode classification (§2.6, editor-internal)

- Ballentine / Itano interpretation dispute: Mode Three. Unchanged.
- Tegmark / Hagan / Reimers decoherence objection: Mode Three. The timing gap "relocates rather than closes". The rate correction strengthens the honesty of this line.
- Stapp 2000 / Georgiev 2015 exchange: reported exposition, with the regime sentence handing each claim its domain. Mixed Two/Three.
- No editor-vocabulary label leakage (grepped).

### Counterarguments Considered

- Physicalist and MWI objections remain at the framework boundary (see Stability Notes). Not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-layer separation between physics and speculation: effect versus interpretation, experiment versus model, precedent for a category versus licence for neurons.
- The Kofman & Kurizki asymmetry, which now also carries the Bidirectional paragraph.
- The Denton/Kominis four-bullet calibration block and its "cite this calibrated statement rather than restate it" instruction. Both kept verbatim.
- The 10-27 site-scoping of the decoherence arithmetic (microtubule best case versus ion-channel site).

### Enhancements Made

- The Relation to Site Perspective now matches the positions register (Birch persona: the "tenet-coherent, not evidence-elevating" pattern now holds in the tenet section too).
- The page now carries a verified, page-cited Stapp rate where it had an unverified figure.

### Cross-links Added

- [[post-decoherence-selection]] (inline, Tenet 2 paragraph). P-Q4 autolinks.

## Remaining Items

None on this page.

**Out-of-scope family (not fixed, for the driver).** The same unverified "~1000 per 300 ms (Stapp 2007)" appears at these live lines:
- `topics/comparing-quantum-consciousness-mechanisms` L82 (the corpus origin)
- `concepts/timing-gap-problem` L71
- `concepts/quantum-consciousness` L124
- `concepts/bidirectional-interaction` L85
- `topics/the-interface-problem` L83
- `concepts/conscious-vs-unconscious-processing` L247 (unattributed "~1000 per 300ms window")
- `research/quantum-zeno-effect-2026-07-14` L108

Separately, `concepts/decoherence` L131 and `topics/quantum-neural-timing-constraints` L113 run their own "~1 kHz / ~1000 per decision" arithmetic. It is not attributed to Stapp, but it is worth a look in the same pass. The canonical replacement is: Stapp's model uses 10 ms between probing actions, ~100 Hz, about thirty per 300 ms window (Stapp 2007, p. 127). Each host must keep its own "same order as the lower figure" logic consistent with the corrected number, because the corrected figure is two orders below 3,000, not the same order. `project/calibration-audit-triple` L378 describes the bidirectional-interaction locus and may need a note.

## Stability Notes

- Bedrock (carried forward; do NOT re-flag): physicalist and eliminativist rejection of quantum-interactionist dualism, and MWI rejection of the collapse presupposition. The page marks both as framework-boundary positions.
- **Correction to the 08-21 note.** That note said "the article's own calibration is not the failure surface". That was true of the expository sections. It was not true of the Relation to Site Perspective, which had carried "leading candidate" against P-Q4 since creation. Future reviews should check this page's ranking language against `positions/quantum-interface` P-Q1/P-Q4 whenever either changes.
- Figures that cite only a Map page and are inherited from another Map page ("per `comparing-…`") need checking at the original source. The ~1,000 figure survived at least eleven reviews across two pages because each review read the previous Map page instead of Stapp.
