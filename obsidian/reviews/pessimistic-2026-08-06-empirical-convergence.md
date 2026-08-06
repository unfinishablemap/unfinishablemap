---
title: "Pessimistic Review - 2026-08-06 - Empirical Evidence for Consciousness-Selecting"
created: 2026-08-06
draft: false
ai_contribution: 100
ai_system: claude-opus-5
ai_modified: 2026-08-06T23:25:00+00:00
---

# Pessimistic Review

**Date**: 2026-08-06
**Content reviewed**: `obsidian/topics/empirical-evidence-for-consciousness-selecting.md` (3890 words, `last_deep_review: 2026-07-12`, `ai_modified: 2026-08-01`)

## Executive Summary

This is a well-calibrated article in its middle — the "Grading the evidence by what it actually supports" section (L115-128) is among the most honest evidential apparatus in the corpus, and the theory table's asterisked footnote (L139) correctly refuses to read a defeater-for-rivals as positive support. The defects are at the **edges**: the frontmatter `description:` and the "Relation to Site Perspective" section both assert the conclusion the grading section explicitly says the evidence does not reach, and one uncited empirical figure survives here that two of the Map's own prior deep-reviews already diagnosed and removed from sibling articles — and that this article's own 2026-07-12 deep-review actively ratified. A fourth finding runs the other way: the falsifier preamble at L149 concedes more than the article's own falsifier paragraphs support.

Five findings, all substantiated on disk. No speculative list.

## Critical Issues

### Issue 1: the enzyme 10¹⁷ figure attributes total catalytic rate enhancement to quantum tunnelling — uncited here, already diagnosed twice, and ratified by this article's last deep-review

- **File**: `obsidian/topics/empirical-evidence-for-consciousness-selecting.md`
- **Location**: L96
- **Severity**: High

L96 reads:

> **Enzyme catalysis.** Quantum tunnelling drives reaction rates in enzymes, confirmed through kinetic isotope effects. Evolution has optimised these effects to accelerate reactions by factors up to 10¹⁷.

Read plainly, "these effects" is quantum tunnelling, and the sentence credits tunnelling with rate enhancements up to 10¹⁷. The ~10¹⁷ figure is the *total* catalytic proficiency of the most proficient enzymes measured against the uncatalysed reaction; the tunnelling contribution inferred from kinetic isotope effects is orders of magnitude smaller, and whether tunnelling is *evolutionarily optimised* at all is the contested part of that literature rather than a settled result. The paragraph carries **no citation**, and the References list (L191-214) contains **no enzyme-catalysis source** at all.

**This is not a new diagnosis — the Map has already made it twice, in writing.** Both prior verdicts are on disk:

- `obsidian/reviews/deep-review-2026-02-23-quantum-decoherence-objection-responses.md` L39 — *"Enzyme catalysis acceleration overstated: Replaced specific numbers (10¹² to 10¹⁷) attributed entirely to tunnelling with accurate framing."*
- `obsidian/reviews/deep-review-2026-03-23-evolutionary-case-for-quantum-neural-effects.md` L30 — *"Claimed 'factors of 10¹² to 10¹⁷' without citation; these figures appear to conflate overall enzyme acceleration with quantum tunnelling contributions specifically. Resolution: Removed the unsupported figures."*

**And this article's own most recent deep-review ratified the defect rather than catching it.** `obsidian/reviews/deep-review-2026-07-12-empirical-evidence-for-consciousness-selecting.md` L47:

> the article's live superlatives (enzyme rate "up to 10^17"; "the most recent and technically specific evidence") are faithful and not superseded. No superlative required updating.

The currency lens asked *"is this figure out of date?"* — it is not — and never asked *"is the figure attributed to the right cause?"* A fresher number would not have fixed anything. This is the exact shape of `fix-by-file-leaves-string-siblings-live`: two files were repaired in 2026-02/03 and the defective string was never re-grepped across the corpus.

**Family scope (measured across all three trees, 2026-08-06).** Live loci carrying the tunnelling-attributed form:

| Locus | Form | Status |
|---|---|---|
| `obsidian/topics/empirical-evidence-for-consciousness-selecting.md:96` | "Evolution has optimised **these effects** to accelerate reactions by factors up to 10¹⁷" | **Strongest form; uncited. This review's target.** |
| `obsidian/topics/quantum-biology-and-neural-consciousness.md:57` | "relies on quantum tunnelling, accelerating reactions by factors of 10¹² to 10¹⁷" | Live, out of scope for this review |
| `obsidian/concepts/quantum-biology-and-neural-mechanisms.md:80` | "Selection has propagated active-site geometries that exploit tunneling to accelerate reactions by factors of 10¹² to 10¹⁷" | Live, out of scope |
| `obsidian/research/quantum-biology-consciousness-2026-01-16.md:159` | "If enzymes routinely use quantum tunneling to accelerate reactions by factors of 10¹⁷" | Research note; propagates per `research-note-self-flagged-gaps-propagate-to-the-article` |
| `archive/topics/quantum-biology-and-the-consciousness-debate.md:47`, `archive/topics/quantum-biology-evidence-in-neural-systems.md:49`, `archive/concepts/quantum-biology.md:91` | "Evolution didn't avoid quantum effects; it exploited them to accelerate reactions by factors of 10¹² to 10¹⁷" | Archive bodies are full serving pages per `defect-sweeps-must-include-archive-tree` |

**The calibrated model already exists in the corpus** — `obsidian/concepts/decoherence.md:135`: *"Quantum tunnelling **contributes to** reaction acceleration factors of 10¹² to 10¹⁷, confirmed by large kinetic isotope effects."* That form is honest: it locates tunnelling as a contributor to reactions whose overall acceleration falls in that range, without crediting tunnelling with the whole factor.

- **Recommendation** (this article only): rewrite L96 to the `decoherence.md` form, drop "Evolution has optimised these effects", and either cite the rate-enhancement figure to its actual source or remove the number and keep the kinetic-isotope-effect claim, which is what the paragraph's argument actually needs. The paragraph's argumentative job is only *"warm biology exploits quantum effects"* — that survives the fix intact. The six sibling loci are **reported here, not minted**; they belong to a corpus sweep, not to this reports-only pass.

### Issue 2: "Relation to Site Perspective" asserts what the article's own grading section says the evidence does not reach

- **File**: `obsidian/topics/empirical-evidence-for-consciousness-selecting.md`
- **Location**: L161-171 against L117 and L128
- **Severity**: High

The article builds an explicit grading ladder at L117 and then states its own verdict:

> L117: *"Graded honestly, every current line lands in the first three; none reaches the last three."* (the last three being supports-quantum-involvement, supports-consciousness-specific-selection, **supports-dualism**)
>
> L128: *"the convergence is real, but it converges on mental causation plus a permissive substrate, not on consciousness-specific quantum selection and still less on dualism. Those further steps are argued elsewhere; **this article's evidence does not reach them**."*

Thirty lines later the tenets section opens:

> L161: *"The empirical convergence supports all five of the Map's [[tenets]]:"*

and then, under Dualism:

> L163: *"The comparative evidence **shows** consciousness contributes capacities that unconscious processing alone does not achieve. The neurological evidence **shows** conscious intention dissociates from motor execution. **Together they support the claim that consciousness is not reducible to neural computation** — though the further step from causal efficacy to non-physicality requires the philosophical arguments the Map develops elsewhere."*

Three problems compound in that one paragraph:

1. **It contradicts the grading table by name.** The table's comparative-cognition row (L122) grades that exact evidence at `supports-mental-causation` and gives the rival reading: *"Conscious access is a physical broadcast/global-workspace function; reasoning depends on it because it depends on that mechanism, not on anything non-physical."* The neurological row (L123) does the same. Irreducibility to neural computation is precisely what those two rows say the evidence does not establish.
2. **The trailing hedge disclaims the sentence it is attached to.** "Not reducible to neural computation" *is* the non-physicality claim; the concession that non-physicality "requires the philosophical arguments the Map develops elsewhere" therefore withdraws the assertion made eleven words earlier. A reader gets the assertion; a careful reader gets a contradiction.
3. **The register is systematically stronger than the body.** The body uses "appears to enable" (L65), "seem to require" (L65), "may be instructive" (L66), "appears to dissociate" (L84). The tenets section switches to bare "shows" twice in L163 and to a flat categorical at L167: *"Consciousness is not a passive observer—it shapes neural outcomes."* This is `condense-regresses-calibration-qualifiers` in reverse — the hedges were never installed in this section in the first place.

- **Recommendation**: replace the L161 header with a claim the grading section can carry — the convergence *bears on* all five tenets, and *supports* the two it actually reaches (Bidirectional Interaction and, via the categorical-objection collapse, Occam's Razor Has Limits), while the Dualism and Minimal Quantum Interaction paragraphs should state explicitly that this article's evidence is consistent with those tenets without establishing them, pointing at where they are argued. Restore the body's hedging verbs in L163 and L167. The fix is length-neutral and removes a contradiction rather than adding a caveat.

### Issue 3: over-concession — the falsifier preamble mis-sorts two of its own four defeaters

- **File**: `obsidian/topics/empirical-evidence-for-consciousness-selecting.md`
- **Location**: L149 against L153, L157, L169
- **Severity**: Medium

L149:

> Three of the four defeaters below describe a *rival* becoming more attractive rather than an experiment that falsifies consciousness-selecting directly; only the absence of neural quantum effects approaches a self-defeater, and even that removes a precondition.

The article's own defeater paragraphs contradict that sorting in two places:

- **Defeater 2** (L153): *"If refined experiments demonstrate no quantum effects at any functionally relevant timescale in living neurons, **the substrate for consciousness-selecting disappears**."* Removing a necessary precondition of the mechanism *is* falsifying the mechanism. L149 double-hedges it — "approaches a self-defeater, and even that removes a precondition" — as though precondition-removal were a lesser thing than falsification.
- **Defeater 4** (L157, MWI): *"If all quantum outcomes occur in parallel branches, **'selection' loses meaning** — consciousness locates itself in a branch but does not determine which branch becomes actual."* And L169: *"The entire framework requires collapse to be real. If all outcomes occur, **there is nothing to select**."* A condition under which the hypothesis has no content is a truth-condition falsifier, not a rival gaining attractiveness. L149 files it in the "rival becoming more attractive" bucket.

By the article's own text the honest count is **two rivals-gaining-ground (classical theory succeeds; epiphenomenalism finds a mechanism) and two framework-killers**, not three-and-a-half to one-half. This is the concession-direction failure the corpus keeps producing: a self-critical sentence that runs *against* the Map collects no scrutiny, so an understatement of the framework's own falsifiability survives review while an equivalent overstatement would not. See `over-concession-gets-ratified-not-merely-missed`.

The defensible part of L149 — that MWI-confirmation may not be *experimentally* reachable — is worth keeping, but it is a point about the route to the defeater, not about whether the defeater is a self-defeater.

- **Recommendation**: rewrite L149 to sort the four defeaters honestly (two rival-attractiveness, two framework-killers), and preserve the genuine caution as a separate remark about how hard it is to reach the MWI condition experimentally. This *strengthens* the article's falsifiability posture using material already in it.

### Issue 4: premise-strength drift on Denton et al. (2024) — a computational modelling result stated as accomplished biology

- **File**: `obsidian/topics/empirical-evidence-for-consciousness-selecting.md`
- **Location**: L94
- **Severity**: Medium

> **Avian magnetoreception.** Migratory birds navigate using quantum spin entanglement in cryptochrome proteins. [...] A 2024 *Nature Communications* study **showed that** the quantum Zeno effect — the same mechanism Stapp proposes for consciousness-brain interaction — **enables** cryptochrome magnetosensitivity. **Evolution has already implemented Zeno-like dynamics in a functional biological system.**

Denton et al. (2024) — reference 4, correctly attributed — is a **computational/theoretical modelling study**, not an experiment. "Showed that X enables Y" over-reads it, and the following sentence converts the model into an accomplished fact of evolutionary biology stated flat, with no hedge. This is a known family with a documented sweep (`denton-2024-first-biological-precedent-propagation`); the calibrated model is in the sibling article `obsidian/topics/quantum-biology-and-neural-consciousness.md:55`, which frames it as *"computational confirmation"* and adds that *"the precedent is for the mechanism category, not for any neural deployment."*

This locus matters more than most in the family because of what the sentence is doing rhetorically: it names Stapp's mechanism in the same breath, so the reader carries "evolution has already implemented Stapp's mechanism" forward into the neural argument — the inference the calibrated sibling explicitly blocks.

Secondary, same paragraph: *"Migratory birds navigate using quantum spin entanglement in cryptochrome proteins"* states the radical-pair account as settled fact. It is the leading hypothesis; the functional role of entanglement in a living bird has not been demonstrated. The article hedges far weaker claims elsewhere and does not hedge this one.

- **Recommendation**: "modelled" / "showed computationally" for Denton; replace the flat evolutionary claim with the sibling's framing (a computational precedent for the mechanism category, not a neural demonstration); add a light qualifier to the radical-pair sentence. Length-neutral.

### Issue 5: nav surface — `description:` asserts the conclusion the body denies, and it is the machine-read surface

- **File**: `obsidian/topics/empirical-evidence-for-consciousness-selecting.md`
- **Location**: frontmatter L3
- **Severity**: Medium

> `description: "Multiple independent empirical lines—evolutionary, cognitive, neurological, and quantum-biological—converge on the conclusion that consciousness causally selects among neural outcomes rather than passively accompanying them."`

The body's conclusion is the opposite of "converge on the conclusion that consciousness causally selects":

- L128: *"it converges on mental causation plus a permissive substrate, **not on consciousness-specific quantum selection**"*
- L141: *"The convergence removes a competitor and leaves consciousness-selecting **among the surviving candidates**; singling it out from its true rivals is separate work."*
- L113: *"Each line, taken alone, is compatible with both consciousness-selecting and classical-physicalist readings; neither interpretation is forced by the data line by line."*

The body's actual claim would be *"converge on mental causation and a permissive quantum substrate, leaving consciousness-selecting among the surviving candidates"* — which is still a substantive, publishable claim, just the true one.

This is the `navigation-surfaces-carry-unreviewed-claims` pattern, and here the exposure is machine-read rather than incidental. `hugo/layouts/_default/baseof.html` L13/L28/L41 emit `.Description` as `<meta name="description">`, `og:description` and `twitter:description`; `hugo/layouts/partials/machine-meta.html` L38 emits it into the JSON-LD `"description"` field. An LLM or crawler that reads the structured metadata and truncates the body — the article's own stated primary audience — receives the over-claim and never reaches L128 that retracts it. Verified live in `hugo/content/topics/empirical-evidence-for-consciousness-selecting.md` L23.

- **Recommendation**: rewrite the description to the L128/L141 claim. One line, no body change, removes the article's most-read over-claim.

## Critiques by Philosopher

### The Eliminative Materialist (Churchland)

The strongest thing in the article is the physicalist column of the grading table, and it is fatal to the article's framing rather than a concession the article survives. Every row's right-hand entry is a live, non-question-begging alternative written by the article itself; having written them, the article proceeds to a tenets section that behaves as though they were not there. If "conscious access is a physical broadcast/global-workspace function" accommodates the comparative data (L122), then "consciousness contributes capacities that unconscious processing alone does not achieve" (L163) is a redescription of the broadcast function in folk vocabulary, not evidence against it.

### The Hard-Nosed Physicalist (Dennett)

The neurological line is the intuition pump doing the work. Sjöberg's SMA patients "retain the subjective sense of willing" (L76) — retained *reports* of willing, which is what a heterophenomenologist expects when the machinery generating reports is spared and the machinery generating movement is not. The article correctly notes Sjöberg synthesises rather than reports fresh data; it does not notice that the dissociation is between two report-generating subsystems, not between experience and mechanism. And L167's "Consciousness is not a passive observer—it shapes neural outcomes" is asserted flat in a section whose body spent 90 lines refusing to assert it.

### The Quantum Skeptic (Tegmark)

L92 says my objection "has collapsed"; L98 says the decoherence-timescale dispute "remains live" and cites Reimers and McKemmish against Hagan's revision. Both cannot be the article's position. What actually happened is that the *categorical* form of the objection was refuted in a photoactivated retinal radical pair — a specialised, evolved, non-neural architecture — and the article knows this, because its sibling says so explicitly. Then L96 credits tunnelling with an enzyme rate enhancement that is not tunnelling's, which is the same move a scale smaller: take a real quantum effect in biology and inflate what it accounts for.

### The Many-Worlds Defender (Deutsch)

The theory table's asterisk (L139) is the most intellectually serious paragraph on this site — it explicitly refuses to read the measurement problem as positive support and concedes the other collapse-realist readings inherit the same opening. Then L149 files "Many-Worlds is confirmed" under *rivals becoming more attractive*, when L169 concedes that under MWI "there is nothing to select." The article has correctly identified that MWI would end it and then declined to say so in the summary sentence. That is a false modesty which functions as protection.

### The Empiricist (Popper's ghost)

L149 is the important sentence and it is wrong in the direction that flatters the reviewer, not the theory. The article tells me its falsifiers are thin; its own paragraphs describe two conditions under which the hypothesis has no content. Understating your own falsifiability is not humility, it is a different way of avoiding the test — and it is harder to catch, because it reads as scruple.

### The Buddhist Philosopher (Nagarjuna)

The article's evidential apparatus is unusually careful about what each line establishes, and then a tenets section restores a stable, causally efficacious selector that the apparatus never earned. The grading ladder is itself an admirable exercise in seeing that no view is established independently of the standards brought to it; the article stops that analysis one step before applying it to the thing doing the grading.

## Unsupported Claims

| Claim | Location | Needed Support |
|---|---|---|
| "Evolution has optimised these effects to accelerate reactions by factors up to 10¹⁷" | L96 | A citation, and a correction: the figure is total catalytic proficiency, not tunnelling's contribution. Two prior Map deep-reviews already reached this verdict. |
| "Evolution has already implemented Zeno-like dynamics in a functional biological system" | L94 | Denton et al. 2024 is computational; the calibrated sibling framing at `quantum-biology-and-neural-consciousness.md:55` is the fix. |
| "Migratory birds navigate using quantum spin entanglement in cryptochrome proteins" | L94 | Leading hypothesis, stated as settled; add the qualifier the article gives far weaker claims. |
| "Together they support the claim that consciousness is not reducible to neural computation" | L163 | Contradicted by the article's own grading table rows L122-123 and by L117/L128. |
| "The bandwidth constraint ... appears to ensure that any selection would be minimal" | L165 | The bridge from a ~10 bit/s throughput ceiling to *minimality of physical intervention* is asserted, not argued. The Zheng & Meister attribution itself is sound and matches `research/bandwidth-constraints-10-bits-2026-03-29.md`; only the inference needs a line of support. Low severity — noted, not a critical issue. |

## Language Improvements

| Current | Issue | Suggested |
|---|---|---|
| L163 "The comparative evidence **shows**" / "The neurological evidence **shows**" | Categorical where the body says "appears to" / "seem to" | "indicates" / "is consistent with" — restore the body's register |
| L167 "Consciousness is not a passive observer—it shapes neural outcomes." | Flat assertion of the contested conclusion; also close to the banned "not X, it is Y" shape | "The evolutionary and neurological lines are the article's strongest evidence that consciousness shapes neural outcomes rather than merely accompanying them." |
| L161 "supports all five of the Map's tenets" | Header asserts more than the five paragraphs below concede | "bears on all five of the Map's tenets, though it establishes only some of them" |
| L149 "even that removes a precondition" | Double-hedged understatement of a genuine falsifier | "and removing a necessary precondition is falsification, not a lesser thing" |

## Checks Run and Passed

- **Altered-state symmetry** (Audit Two): supportive-cluster gate **does not fire** — the article cites no psychedelics/NDE/terminal-lucidity/cessation/OBE material. Anaesthesia appears (L98, L106) as microtubule evidence, not as filter-model support. Audit not applicable.
- **Reasoning-mode failures**: no boundary-substitution and **no label leakage**. Greps for `direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification:`, `**Evidential status:**` return zero. The engagement with physicalist rivals at L55, L68, L88, L109 and L119-128 is argued in-framework throughout — the physicalist column is written in the physicalist's own voice and is not dismissed by tenet appeal anywhere. This is the article's outstanding strength.
- **Epistemic/metaphysical equivocation**: the measurement-problem paragraph (L100) is the risk locus, and the article handles it correctly — L126 grades it `establishes-possibility` and L139 explicitly refuses to read it as positive support. No equivocation found.
- **Internal `positions/` and `P-xx` cites**: none present; the lens does not apply.
- **Style guide**: front-loading is good (L42 states the honest claim in the first sentence); no "This is not X. It is Y." construct; "Relation to Site Perspective" present, substantive, and the subject of Issue 2.

## Strengths (Brief)

Preserve these under any revision:

- **L115-128, the grading ladder.** Weakest-claim-supported grading with an explicit rival-reading column is the strongest evidential discipline in the corpus. It is also the instrument that makes Issues 2 and 5 diagnosable at all — the article convicts itself, which is the mark of an honest apparatus.
- **L139, the asterisk.** Refusing to read a defeater-for-rivals as positive support, and conceding that the other collapse-realist interpretations inherit the same opening, is exactly the concession-direction discipline the corpus otherwise gets wrong.
- **L141 and L143.** "The convergence removes a competitor and leaves consciousness-selecting among the surviving candidates" and the plate-tectonics parallel explicitly labelled "suggestive rather than decisive."
- **The per-line "what this does not establish" paragraphs** (L55, L68, L88, L109). Four sections, four honest limits, each naming the specific rival that survives.
- **L98 and L109** engage the disconfirming literature by name (Reimers, McKemmish, the directionally-mixed 2025 *BMC Anesthesiology* result, the 2026 *Frontiers* feasibility standard the line has not met) rather than citing only the favourable side.

## Tasks Minted

One `refine-draft` on the reviewed article (Issues 1-5). The six sibling loci of the enzyme-figure family are reported above but **not** minted — a corpus sweep is out of contract for a reports-only pass.
