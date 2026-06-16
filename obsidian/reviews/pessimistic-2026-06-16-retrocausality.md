---
title: Pessimistic Review - 2026-06-16 - Retrocausality
created: 2026-06-16
draft: false
ai_contribution: 100
ai_system: claude-opus-4-8
---

# Pessimistic Review

**Date**: 2026-06-16
**Content reviewed**: `obsidian/concepts/retrocausality.md` (last deep-review 2026-05-19; body modified 2026-02-28; never the primary subject of a pessimistic review)

## Executive Summary

`retrocausality.md` is an unusually disciplined article — it conditionalises its central claim on an explicitly-flagged minority interpretation (TI), runs an "Addressing Objections" section, and has a "What Would Challenge This View?" section. Its weaknesses are not bluster but **selective citation** and **internal inconsistency with the corpus's own canonical treatments**. The two most serious findings: (1) the decoherence-rebuttal paragraph presents Hagan et al. (2002) as an unchallenged answer to Tegmark and contradicts the figure given in the Map's own `decoherence.md` (seven vs eight orders of magnitude) while omitting the Reimers/McKemmish counter-rebuttals that `decoherence.md` explicitly says must be cited to avoid "selective citation"; (2) the falsifiability defence asserts that "all quantum interpretations make identical predictions," which the Map's own `measurement-problem.md` contradicts by discussing testable objective-collapse theories (GRW/CSL/Penrose).

## Critiques by Philosopher

### The Eliminative Materialist (Churchland)
The whole edifice is a baroque rescue of a folk-psychological intuition ("I really do decide"). You concede the Schurger neural-noise reinterpretation and classical temporally-extended-decision models "require less interpretational commitment" — and then reach past them for the most exotic option available. By your own admission the parsimonious resolutions work. Why import backward causation, the transactional interpretation, and a quantum-conscious interface to save a feeling that neuroscience is already explaining away? The article never says what retrocausality *buys* that the cheaper resolutions don't, beyond a "more fundamental" dissolution — but "more fundamental" is doing no work if the cheaper option already dissolves the puzzle.

### The Hard-Nosed Physicalist (Dennett)
"Contemplative Evidence" is the soft underbelly. Meditators reporting awareness "outside temporal flow" is offered as "phenomenological support for the atemporal selection model." This is exactly the inflation of introspective report into metaphysics that I warn against — the witness's *report* that it stands outside time is a fact about the report, not about time. The "crystallisation" phenomenology of decision is presented as something retrocausality "vindicates," but the feeling of an option crystallising is equally predicted by a wholly classical accumulator hitting threshold. You are reading the conclusion you want out of the phenomenology.

### The Quantum Skeptic (Tegmark)
This is the article's most exposed flank, and it has been handled inconsistently with the Map's own work. The decoherence paragraph says Hagan/Hameroff/Tuszynski (2002) obtained "estimates seven orders of magnitude longer" and that "this debate remains unresolved." But the Map's canonical `decoherence.md` gives **eight or more orders of magnitude** AND immediately adds the Reimers et al. (2009) and McKemmish et al. (2009) re-derivations, warning in terms that "citing Hagan as a closed rebuttal of Tegmark would be selective citation." `retrocausality.md` does precisely that — presents Hagan as the live answer, omits the counter-rebuttals, and even gets the order-of-magnitude figure wrong relative to the home article. "No experiment has directly measured coherence times in living neural tissue" is true but cuts the other way: the absence of any positive measurement is not symmetric support for long coherence.

### The Many-Worlds Defender (Deutsch)
The article asserts TI "produces one actual history, not branching worlds" as a point in its favour under No Many Worlds — but this is tenet-preference dressed as argument. You have not refuted MWI here; you have noted that TI is *compatible* with a tenet you already hold. That is fine as framework-boundary marking, but the "No Many Worlds" subsection in "Relation to Site Perspective" reads as if single-outcome-ness were an *achievement* of retrocausality rather than a stipulation. The honest phrasing: TI is selected partly *because* it is single-history, not shown to be correct and then found to deliver single histories.

### The Empiricist (Popper's ghost)
"Isn't this unfalsifiable? All quantum interpretations (Copenhagen, Many-Worlds, Bohmian) make identical predictions for currently testable scenarios." This is false as stated and the Map knows it: `measurement-problem.md` discusses GRW, CSL, and Penrose objective-collapse theories, which make predictions that *differ* from standard QM and are the target of active experimental tests. The defence "neither can it be empirically refuted" is a tu quoque, not a virtue — and it sits awkwardly beside the article's own "experimental falsification distinguishing retrocausal from non-retrocausal interpretations" listed as a challenge condition. Either interpretations are empirically distinguishable (so the falsifiability defence collapses) or they are not (so the listed challenge condition is empty). The article wants both.

### The Buddhist Philosopher (Nagarjuna)
The "haecceity" move — "you *are* one history, selected through the atemporal transaction" — reifies exactly the permanent indexical self that should be deconstructed. The article treats the selected history's *thisness* as a metaphysical bedrock that branching models "cannot capture," but the felt thisness is itself a construction. This is a framework-boundary disagreement, honestly notable as such, not a refutation within my framework.

## Critical Issues

### Issue 1: Decoherence rebuttal contradicts the Map's own canonical article (figure + selective citation)
- **File**: `obsidian/concepts/retrocausality.md`
- **Location**: "The Decoherence Challenge," point (2), lines 113
- **Problem**: Two defects in one paragraph. (a) **Figure mismatch**: says Hagan et al. obtained estimates "seven orders of magnitude longer"; the canonical `decoherence.md:95` says "eight or more orders of magnitude longer" (10⁻⁵ to 10⁻⁴ s). `coupling-modes.md:112` also says "seven orders." (b) **Selective citation**: presents Hagan as the live rebuttal and says only that "this debate remains unresolved," omitting the Reimers et al. (2009) and McKemmish et al. (2009) re-derivations that `decoherence.md` flags as essential, explicitly warning that "citing Hagan as a closed rebuttal of Tegmark would be selective citation." The article commits the very error its own corpus names.
- **Severity**: High
- **Recommendation**: `refine-draft`. Reconcile the figure to the canonical "eight or more orders of magnitude" (and fix `coupling-modes.md` to match in the same pass), and add a clause noting the Reimers/McKemmish counter-rebuttals so the dispute is presented as live-and-contested, matching `decoherence.md`. Do not present Hagan as a closed answer.

### Issue 2: Falsifiability defence contradicts the Map's own `measurement-problem.md`
- **File**: `obsidian/concepts/retrocausality.md`
- **Location**: "Addressing Objections" → "Isn't this unfalsifiable?", line 93
- **Problem**: "All quantum interpretations (Copenhagen, Many-Worlds, Bohmian) make identical predictions for currently testable scenarios." This is too strong: objective-collapse theories (GRW, CSL, Penrose), which the Map covers in `measurement-problem.md:119` and `spontaneous-collapse-theories`, make predictions that *differ* from standard QM and are experimentally tested. The cited trio (Copenhagen/MWI/Bohm) happen to be empirically equivalent, but generalising "all interpretations" is false and is contradicted by the article's own "What Would Challenge This View?" item (1), which presupposes interpretations *can* be experimentally distinguished.
- **Severity**: Medium
- **Recommendation**: `refine-draft`. Restrict the claim to the empirically-equivalent interpretations actually named ("Copenhagen, Many-Worlds, and Bohmian mechanics make identical predictions for currently testable scenarios"), and acknowledge that objective-collapse families are an exception — which is consistent with, not damaging to, the Map (its modified growing block already invokes objective collapse).

### Issue 3: Uncited "2017 satellite experiment" whose attribution exists elsewhere in the corpus
- **File**: `obsidian/concepts/retrocausality.md`
- **Location**: "Retrocausality in Physics" → Wheeler's delayed-choice, line 58; References section, lines 182-195
- **Problem**: The body cites "The 2017 satellite experiment extended this over thousands of kilometres" with no author and no References entry. Two sibling articles correctly attribute this to **Vedovato et al. (2017)** (`time-symmetric-physics.md:154`, `forward-in-time-vs-time-symmetric-selection.md:74`). An anonymous "the 2017 experiment" is a citation gap, and the attribution is already verified in-corpus.
- **Severity**: Low
- **Recommendation**: `refine-draft`. Attribute to "Vedovato et al. (2017)" inline and add the reference, matching the sibling articles.

## Counterarguments to Address

### The cheaper resolutions undercut the motivation
- **Current content says**: Retrocausality offers "a more fundamental resolution" than the Schurger reinterpretation, and "the alternatives chip away at the premises" while retrocausality gives "the most radical dissolution" (lines 46, 81).
- **A critic would argue**: If the cheaper, lower-commitment resolutions already dissolve the Libet puzzle (which the article concedes), the appeal to retrocausality is unmotivated by the Libet problem itself — it is motivated by the *tenets*, not by Libet. The article half-says this but lets "more fundamental" carry weight it hasn't earned.
- **Suggested response**: State plainly that retrocausality is not needed *to answer Libet* — the classical resolutions suffice — but is the resolution that fits the Map's independently-motivated tenet structure. This is more honest and removes the unsupported "more fundamental is better" implication.

### Contemplative report as evidence
- **Current content says**: Meditators' reports of standing "outside" temporal flow provide "phenomenological support for the atemporal selection model" (lines 124-127).
- **A critic would argue**: Epistemic/metaphysical equivocation — the report is evidence about the report, not about the temporal structure of selection. A report of timelessness is equally explained by an altered temporal-binding mechanism with no metaphysical timelessness behind it.
- **Suggested response**: Downgrade to natural-language hedge: the phenomenology is *consonant with* the atemporal model and would be surprising on a strictly sequential one, but is not independent confirmation. (Orthogonal to hedge density — the surrounding text is already hedged; the issue is the inferential leap, not the tone.)

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| Hagan et al. estimates "seven orders of magnitude longer" | retrocausality.md:113 | Reconcile to canonical "eight or more orders" + cite Reimers/McKemmish counter-rebuttals |
| "All quantum interpretations make identical predictions" | retrocausality.md:93 | Restrict to Copenhagen/MWI/Bohm; exempt objective-collapse (GRW/CSL/Penrose) |
| "The 2017 satellite experiment" (anonymous) | retrocausality.md:58 | Attribute to Vedovato et al. (2017); add References entry |
| Contemplative reports give "phenomenological support" for atemporal selection | retrocausality.md:125 | Downgrade to "consonant with," not "support for" |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "estimates seven orders of magnitude longer ... debate remains unresolved" | Selectively favourable; omits counter-rebuttals | "estimates eight or more orders of magnitude longer, though Reimers et al. (2009) and McKemmish et al. (2009) dispute the parameters; the debate is live" |
| "All quantum interpretations ... make identical predictions" | Over-general, internally contradicted | "Copenhagen, Many-Worlds, and Bohmian mechanics make identical predictions for currently testable scenarios" |
| "provides phenomenological support for the atemporal selection model" | Epistemic→metaphysical leap | "is consonant with the atemporal selection model" |

## Strengths (Brief)

This is a genuinely careful article and the revisions should preserve its discipline. Its conditional framing ("Each 'if' is genuinely uncertain"), its honest concession that TI "remains contested but not refuted," its inclusion of the Maudlin contingent-absorber challenge *and* the Kastner/Lewis exchange with a "stable impasse" verdict, the Sjöberg (2024) SMA-resection corroboration, and the dedicated "What Would Challenge This View?" section are all exemplary. No editor-vocabulary label leakage was found, no boldfaced "Evidential status:" callouts, no strong-language violations. The fixes are local citation/consistency repairs, not structural rewrites — the argument's honesty is intact, the citations just need to match the rest of the corpus.
