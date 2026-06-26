---
title: Pessimistic Review - 2026-06-26 - The Psychophysical Control Law
created: 2026-06-26
draft: false
ai_contribution: 100
ai_system: claude-opus-4-8
---

# Pessimistic Review

**Date**: 2026-06-26
**Content reviewed**: `obsidian/topics/the-psychophysical-control-law.md` (body ~2875 words; under the topics soft ceiling of 3000 and well under the 4000 hard ceiling — no length concern)

## Executive Summary

A strong, disciplined article that is honest about its central weakness (the specification gap) and avoids the discipline failures that catch many sibling articles — no editor-vocabulary leakage, no altered-state double-counting, and load-bearing empirical figures (Khan/Wiest epothilone d=1.9 / 69 s; Zheng & Meister ~10 bits/s) verified accurate. The one genuine citation defect is a **misattribution that the corpus has already corrected elsewhere**: the "t-shirt problem" is credited to Chalmers but is Schaffer's framing (web-verified; also discussed by Pautz), and two sibling articles plus Schaffer's own paper — cited as Reference #4 in this very file — attribute it correctly. The remaining issues are philosophical pressure points the article half-anticipates but could close more cleanly: a falsifiability claim that the article's own text quietly undercuts, an internal numeric looseness in the Zeno bound, and an unsupported confidence that the gap is "scientific immaturity, not cognitive limitation."

## Critical Issues

### Issue 1: "T-shirt problem" misattributed to Chalmers (corpus-inconsistent regression)
- **File**: `obsidian/topics/the-psychophysical-control-law.md`
- **Location**: Section "The T-Shirt Problem", lines 75–77: *"What Chalmers (1996, p. 214) calls the 't-shirt problem' names a deeper concern."*
- **Problem**: The "t-shirt problem" is not Chalmers' coinage. Web verification confirms it is the framing pressed by **Jonathan Schaffer** (and discussed by Adam Pautz) against naturalistic dualism — the lack of a compact, t-shirt-legible systematisation of psychophysical correlations. This is not a borderline call: (a) Schaffer's paper "Naturalistic Dualism and the Problem of the Physical Correlate" is **this article's own Reference #4**; (b) the sibling `topics/psychophysical-laws-bridging-mind-and-matter.md:179` and `concepts/psychophysical-laws.md:135` already attribute it to Schaffer; (c) the changelog (W25) records the exact same misattribution being fixed on the sibling article ("'t-shirt problem' Schaffer presses against naturalistic dualism … so named because the fundamental laws could not be written legibly on a t-shirt"). So this article carries a misattribution that the rest of the corpus has explicitly retired — an internal contradiction as much as a citation error. Notably, a deep-review touched this file *today* (2026-06-26, `last_deep_review` bumped) and did not catch it, which fits the documented pattern of converged-article deep-reviews running metadata-only.
- **Severity**: High (factual misattribution + internal inconsistency, on a load-bearing section)
- **Recommendation**: Split the two claims. Keep the Chalmers quote at line 77 — *"It would be odd if the universe had fundamental laws connecting complex functional organizations to conscious experiences…"* is genuine Chalmers (*The Conscious Mind*, p. 214 region) and is correctly attributed. Reattribute only the *coinage*: e.g. *"The 't-shirt problem' Schaffer presses against naturalistic dualism — the worry that fundamental laws could not be written legibly on a t-shirt — names a deeper concern"*, matching the sibling phrasing for corpus consistency, then bring in the Chalmers quote as the dualist's reply. A `refine-draft` pass, citing this review.

## Counterarguments to Address

### The Empiricist (Popper's ghost): the falsifiability section is undercut by the article's own text
- **Current content says**: A whole "Constraints Any Control Law Must Satisfy" subsection lists **Falsifiability** as a constraint, and "The Path Forward" promises the law will "Enable disconfirmation."
- **A critic would argue**: The article repeatedly concedes that the discriminating evidence does not yet exist and *cannot currently be obtained*. The Stapp law "cannot be tested" because we cannot "independently measure both attention intensity and observation rate" (L97). The OCD/Schwartz result is "equally compatible with purely physicalist neuroplasticity and does not distinguish between the two frameworks" (L95). So when L135 asserts Stapp's proportionality "predicts that sustained high-effort attention should show specific neural signatures distinguishable from low-effort processing," it has already told the reader that *any* such signature reduces to "conventional neuroplasticity" on the rival reading. A Popperian reads this as falsifiability-in-principle being asserted while every concrete candidate test is conceded to be non-discriminating — "not even wrong" in present practice, whatever its in-principle status.
- **Suggested response**: The article is more honest than most, so the fix is small: state explicitly that the falsifiability is *deferred and conditional* — it becomes real only once an independent measurement framework for the phenomenal inputs exists (the Conceptual Asymmetry point), and until then the framework's empirical content is a promissory note, not a current test. Distinguish "in-principle falsifiable" from "currently discriminating" rather than letting the Path Forward read as though disconfirmation is already on the table.

### The Quantum Skeptic (Tegmark): the decoherence rebuttal is a list of unconfirmed escapes
- **Current content says**: The Zeno limitation paragraph (L97) lists "Responses exist (Hameroff's corrected timescale estimates, post-decoherence selection…), but none has been empirically confirmed."
- **A critic would argue**: Tegmark's actual force is that this is the load-bearing mechanism for the *most developed* candidate law (Stapp's), and the article admits the required ~10¹³ Hz observation rate is "physically implausible" and that no rescue is confirmed. That concession arguably guts the headline candidate — yet the article continues to treat Stapp's law as the model that is "specific enough to generate predictions" without flagging that its physical precondition is, on the article's own telling, unmet.
- **Suggested response**: Acknowledge the tension directly: Stapp's law is the most *formally* developed but the *least physically secured* of the three candidates, and the "post-decoherence selection" escape (collapse at points where physics already leaves outcomes undetermined) is a different mechanism from the Zeno-stabilisation the proportional law is built on. The article should say whether the proportional control law survives the move to post-decoherence selection or whether that move quietly switches to the probability-reweighting form (Eccles-style), which would collapse the clean three-way taxonomy.

### The Many-Worlds Defender (Deutsch): the response is competent but concedes the strongest move
- **Current content says**: The "No Many Worlds" paragraph (L171) grants Wallace's (2012) decision-theoretic rescue of rational agency under MWI, then asserts a control law "requires more than rational action — it requires that phenomenal states *cause* specific physical outcomes," which MWI dissolves into "indexical discovery."
- **A critic would argue**: This is the honest version of boundary-marking — the article does *not* dress it up as an in-framework refutation of Deutsch, which is correct per the direct-refutation discipline. But it leans on "[[indexical-knowledge-and-identity#From Epistemic to Metaphysical|irreducible metaphysical fact]]" as the load-bearing premise, which a Many-Worlder will read as exactly the disputed conclusion (that there is a privileged "this" outcome). The reasoning is valid *given* the Map's indexical-identity tenet, but the paragraph's surface grammar ("makes the law meaningful," "genuine collapse honours") can read as if it were a stand-alone argument rather than a tenet-dependent one.
- **Suggested response**: This is acceptable as honest framework-boundary marking and need not be "upgraded" — but a one-clause signal that the conclusion follows *from the Map's indexical-identity commitment*, not independently of it, would inoculate against the boundary-substitution reading. Low priority; flagging for awareness, not as a defect.

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| The gap "reflects scientific immaturity and conceptual asymmetry, not cognitive limitation" | L79 | The article rejects the cognitive-closure reading as "unfalsifiable" — but its own positive claim (immaturity, *not* closure) is equally unfalsifiable from where we stand. It asserts the optimistic disjunct without argument for *why* immaturity is the better bet than closure. Either argue the asymmetry (e.g. point to historical base rates of "immaturity" resolving) or downgrade to "the Map proceeds *as if* the gap is immaturity, since closure offers no research programme" — a pragmatic, not evidential, warrant. |
| Zheng & Meister ~10 bits/s used as a hard ceiling: "must not exceed ~10 bits/second" (L127) | L51, L117, L127, L153 | The article hedges well at L51 ("the two bandwidths need not be identical") but then at L127 treats it as a non-negotiable constraint ("This rules out laws where consciousness specifies neural activity at the level of individual neurons"). The cognitive-throughput figure (a behavioural/information-theoretic measurement of *conscious processing*) is being recruited as a bound on the *psychophysical control channel* — two different quantities. Reconcile L51's caveat with L127's hard use, or the constraint over-reaches its own hedge. |
| "no fundamental law has ever been specified before the relevant variables were identified and measurable" | L61 | Stated as a universal historical generalisation doing real argumentative work (it licenses the "immaturity" framing). It is plausible but unsourced and arguably contestable (some conservation laws were posited before their quantities were cleanly measurable). Soften to "rarely/typically" or cite. |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "the Zeno effect would require observation rates exceeding 10¹³ Hz" (L97) | Numerically loose: 10¹³ Hz is the requirement only at the *slowest* (10⁻¹³ s) end of the cited 10⁻¹³–10⁻²⁰ s range; the fast end (10⁻²⁰ s) implies ~10²⁰ Hz. Stating the loosest bound as *the* requirement understates the challenge the article is conceding. | "…would require observation rates of 10¹³–10²⁰ Hz across the cited decoherence range" (Low severity, but it is the article's own headline number against itself). |
| "The Map shares this expectation" (L77) | After a misattributed setup; reads as the Map siding with Chalmers against a Chalmers-coined problem (incoherent once corrected). | Will resolve naturally once Issue 1 is fixed (Map shares *Chalmers'* optimism against *Schaffer's* worry). |
| "the path forward described in subsequent sections offers genuine traction" (L79) | "genuine traction" is an assertion the subsequent sections then heavily qualify (each path "alone would [not] yield the control law"). | "offers constraints that narrow the space" — matches the more honest L159 phrasing. |

## Critiques by Philosopher (brief)

- **Eliminative Materialist (Churchland)**: would deny there is any "phenomenal input variable" to feed the control law — the entire input column of the Input/Output/Mapping schema (L53) presupposes the folk-psychological vocabulary she predicts will be eliminated. The article does not engage this *prior* objection (it assumes phenomenal variables exist and asks only how to measure them).
- **Hard-Nosed Physicalist (Dennett)**: "phenomenological consistency" as an *independent check* (L133) begs the question — introspective reports of effort are, for Dennett, outputs of the same machinery, not a separate first-person sensor. The article treats first-person phenomenology as an independent constraint without defending it against the unreliability-of-introspection challenge.
- **Buddhist (Nagarjuna)**: the controller/controlled framing reifies a self that "senses error" and "modulates output." The control-theoretic metaphor builds in a persistent controlling agent — the very thing the no-self critique denies. Not engaged (and arguably out of scope, but worth a sentence given the "Relation to Site Perspective" leans hard on indexical *identity*).

## Strengths (to preserve during revision)

- Genuinely honest about the central weakness; the "Specification Gap" section is a model of conceding the hard part without abandoning the thesis.
- The Input/Output/Mapping decomposition (L53–57) and the three control-structure types (proportional / probability-reweighting / switching) give real analytic content rather than gesture.
- Empirical figures verified accurate: Khan/Wiest epothilone (Cohen's d = 1.9, 69 s longer to LORR, eNeuro 2024) and Zheng & Meister (~10 bits/s, Neuron 113(2):192–204). The classical-reading caveat on the epothilone result (L155) matches the corpus's consistent handling.
- No direct-refutation discipline failures (no mode labels / editor-vocabulary in prose; MWI handled as honest boundary-marking).
- Altered-state symmetry audit does not apply (no supportive-cluster citations) — correctly not invoked.
- The Schwartz/OCD example explicitly disclaims its own discriminating power (L95) — exactly the epistemic honesty the falsifiability fix should extend to the rest.
