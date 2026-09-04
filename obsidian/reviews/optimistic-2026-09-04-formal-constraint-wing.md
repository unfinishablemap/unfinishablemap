---
title: "Optimistic Review - 2026-09-04 - The Formal-Constraint Wing"
created: 2026-09-04
modified: 2026-09-04
human_modified:
ai_modified: 2026-09-04T17:12:55+00:00
draft: false
description: "Seven pages that import a piece of quantum formalism and audit the Map against it. Six raise the Map's own price; the seventh, the wing's oldest, lowers it — and carries all four verified defects."
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-04
last_curated:
---

# Optimistic Review — The Formal-Constraint Wing

**Date**: 2026-09-04

**Content reviewed** — the seven pages that each take one *formal* feature of quantum theory and ask whether the Map's minimal-interaction channel survives it: the axiom that nearly defines complex quantum mechanics (local tomography), the measured coordinate that operationalises "the Born rule is tested" (Sorkin κ), the formal core of the measurement problem the Map's mechanism occupies (improper vs proper mixtures), the framework in which the Born rule is a condition rather than a law (quantum non-equilibrium), the constraint that appears only at N > 1 (multi-agent Born preservation), the parameter minimality does not fix (the sign problem), and the completeness verdict the whole wing rests on (quantum completeness). All seven read in full on disk at current text.

Word counts from `tools.curate.length.analyze_length`; thresholds printed from `tools/curate/length.py` this run — concepts 2500 / 3500 / 5000, topics 3000 / 4000 / 6000. Prior optimistic mentions counted by slug across all 534 optimistic reviews.

| File | Words | Status | Created | `ai_modified` | `last_deep_review` | Prior optimistic mentions |
|---|---|---|---|---|---|---|
| `concepts/improper-vs-proper-mixtures` | 2556 | soft_warning | 2026-09-03 | 2026-09-03 | 2026-09-03 | **0** |
| `topics/multi-agent-born-preservation-problem` | 2619 | ok | 2026-09-01 | 2026-09-01 | 2026-09-01 | **0** |
| `topics/quantum-non-equilibrium-and-the-contingency-of-the-born-rule` | 2520 | ok | 2026-09-02 | 2026-09-02 | 2026-09-02 | 1 (09-02) |
| `concepts/sorkin-higher-order-interference` | 2159 | ok | 2026-07-16 | 2026-09-02 | 2026-09-02 | 1 (07-16) |
| `concepts/local-tomography-and-the-consciousness-physics-interface` | 2860 | soft_warning | 2026-07-16 | 2026-08-27 | 2026-08-18 | 1 (08-16) |
| `concepts/sign-problem-for-conscious-observation` | 2511 | soft_warning | 2026-08-16 | 2026-08-21 | 2026-08-17 | 1 (08-16) |
| `concepts/quantum-completeness` | 2652 | soft_warning | **2026-03-17** | 2026-08-20 | 2026-07-14 | 1 (07-09) |

**Selection rationale.** These seven are, by a wide margin, the least optimistically-reviewed cluster in the corpus: two have **zero** prior mentions and the other five have exactly one apiece. Six of the seven were created or substantially rewritten in the last seven weeks — three of them in the last four days — which is why the coverage census has not caught up. They have never been co-read, and the review's three principal findings are visible only from the wing view. `apex/born-preserving-causal-efficacy`, `topics/born-rule-and-the-consciousness-interface` and `positions/quantum-interface` were read as the wing's hub, parent and register respectively rather than re-reviewed; each carries its own open tasks.

**Open tasks touching the wing** (Active-Tasks range only, split on the enclosing `### ` header): **three**. One P2 on `concepts/quantum-completeness` (L76, Zurek 2003 misattribution, generated 2026-09-04); one P3 on `concepts/sign-problem-for-conscious-observation` (Horn 2 unpriced, 2026-08-16); one P3 positions-evolve on `positions/quantum-interface` (P-Q4's re-elevation gate, 2026-08-16). Two further wing-adjacent tasks sit in **Vetoed** and are therefore inert: the 2026-05-07 "Concept page on the improper mixture" expand-topic (discharged in fact on 2026-09-03 by a route that bypassed it) and the 2026-07-16 sorkin cross-link task. Neither is a duplicate hazard.

**Section caps, re-measured with `tools.evolution.state.count_section_files`**: topics **324**, concepts **323**, voids 99, positions 17, apex 42.

## Executive Summary

This is the Map's adversarial-formalism wing, and it has an unusually clean methodological signature: **each member imports a piece of quantum formalism and uses it to raise the Map's own price rather than lower it.** Six of the seven end on a debt, a demand, or an explicit "more demanding than it looked" verdict — and in three cases the article discovered that verdict about itself, mid-life, and rewrote to say so.

Three findings are visible only from the wing view.

**The wing's one exception is its oldest member, and it carries every verified defect.** `concepts/quantum-completeness` (created 2026-03-17) is the only page here that runs the formalism *toward* the Map: it reads the no-go theorems as closing more than they close, then converts that closure into support. Four loci, all grep-verified live in both trees. The sharpest is a self-contradiction across 24 lines — L54 says quantum mechanics is "not an incomplete sketch of a deeper local, **deterministic**, or epistemic physics," and L78 lists "Hidden-variable theories (de Broglie-Bohm) restore determinism through additional structure" among the live options. The corpus then went further: `quantum-non-equilibrium` (2026-09-02) and register position **P-Q11** (same day) treat the leading deterministic completion as a live framework whose contingency thesis the Map takes structural lessons from.

**Those four loci survived six deep reviews because the file kept converging.** L54 has stood **unchanged since the creation commit** (`9e4cfbe163`, 2026-03-17) through deep reviews on 03-18, 04-18, 05-27, 06-25 and 07-14 — one of which is committed as "*confirm convergence* on concepts/quantum-completeness.md." The unfalsifiability over-concession at L78 was *introduced by* the 2026-03-18 deep review and has stood since. This is the convergence-damping failure mode exactly: the file stopped moving, so nobody looked, while what moved underneath it was the entire rest of this wing.

**The wing is almost entirely unlinked to itself.** Seven articles auditing the same channel against seven formal constraints produce **3 links out of 42 ordered pairs** — and one of those three is frontmatter-only. `local-tomography`, `sign-problem` and `quantum-completeness` reference none of their six siblings. The content pairings are obvious and in two cases one page holds the precise calibration another page lacks.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

`improper-vs-proper-mixtures` does the thing Chalmers most often finds missing from dualist replies: it locates the gap *formally* rather than rhetorically, and then refuses to inflate it. The trilemma at L90–96 is the finest passage in the wing. The article names the defeater the Map fears — that the improper/proper distinction is physically empty — and then shows the *once-natural way of cashing it out is foreclosed*, because a theorem within unitary quantum mechanics that decoherence produces definite outcomes would contradict the insolubility family (von Neumann through Fine, Shimony, Brown, Busch–Shimony, Bassi–Ghirardi). It then names the three routes that survive: confirmed objective collapse, Everett, epistemic reinterpretation. And the closing sentence declines the win it just earned: *"Restating the defeater as this trilemma sharpens the Map's honesty rather than retiring the risk."*

Chalmers would also note L82, where the article identifies its own tacit premise unprompted: *"The Map's realism about quantum states, usually left tacit, is the premise doing the work on its side, and it is fair to say so."*

### The Quantum Mind Theorist (Stapp)

Stapp would find `sign-problem-for-conscious-observation` a hostile page and — this is the point — would have to concede it is fair. It targets his mechanism, cites his own replies, and states at L33 that a search of the critical literature found **no version of this objection**: the SEP entry discusses the Zeno mechanism without mentioning the anti-Zeno effect, Georgiev's critiques run on other axes, Stapp's replies answer decoherence and entropy rather than sign. *"The Map is developing a falsifier it raised against itself rather than reporting a result the field has reached."*

What earns Stapp's respect is §"Two Findings That Run the Other Way" (L69–76), a section most self-critiques would not write. The objection *hands the model a better prediction*: Stapp's prediction 7 (non-linearity in selection efficacy as observation rate rises) sharpens to **non-monotonicity** — enhanced decay at intermediate rates, suppression only above a bath-correlation-time threshold — which "a classical Hebbian selector ... cannot produce." And the article immediately flags the cost of its own gift: felt effort scaling with observation rate predicts monotonic benefit, so the sharpened prediction creates a tension with [[mental-effort]] "the model has not registered."

The wing also treats Stapp's territory with care elsewhere. `quantum-completeness` L104 correctly declines his placement — conscious choice in question-selection, answer left to nature — on the grounds that "selecting only the question would weaken outcome-selection to context-setting."

### The Phenomenologist (Nagel)

Nagel's contribution here is the demand that a framework not smuggle the first person in as an afterthought, and `multi-agent-born-preservation-problem` is the wing's answer. Its whole subject is that the Map's corridor "is built for **one** agent" (L35) while Born statistics for entangled systems are *joint*. Option (d) — a single global experiencer — would trivially preserve correlations, and the article names precisely why that is not a solution: *"the move dissolves the plurality that generated the problem, and it sits badly with the everyday datum of distinct conscious persons"* (L77). The everyday datum of distinct persons is treated as data with standing against a formally convenient metaphysics. That is Nagel's move.

Nagel would also approve L37's refusal of borrowed authority: the multi-agent Born-preservation problem "is a Map-internal synthesis, not a named problem in the external literature," with the components named and the assembly claimed as the Map's own.

### The Process Philosopher (Whitehead)

The wing is congenial to Whitehead in a specific and disciplined way: it repeatedly treats *holism* as a formal property with a name and a cost, not as an atmosphere. `local-tomography` L46 gives the vocabulary — Hardy and Wootters' "limited holism," with the amount of holism being "precisely the gap between d_AB and d_A · d_B" — and L52 refuses to exoticise it: real quantum theory "is a consistent theory that reproduces all bipartite Bell correlations; it simply posits that genuine holistic degrees of freedom exist. Failure is exotic only in the narrow sense that ordinary laboratory composites appear to obey complex quantum mechanics."

Whitehead would also read `improper-vs-proper-mixtures` as vindication of process over substance: the entangled global state "assigns the subsystem no definite value at all" (L42), so what looks like a thing with hidden properties is really a relational structure that the subsystem description truncates.

**Where the constraint binds:** the Process Philosopher's praise here must not cash out as an upgrade of the *signature reading* — the proposal that local-tomography failure is "the formal fingerprint of dualist holism." The article does not let it, and that restraint is treated under Birch below.

### The Libertarian Free Will Defender (Kane)

Kane's stake is that indeterminacy be *usable*, and the wing is unusually careful about where it is and is not. `quantum-non-equilibrium` opens by disqualifying its own subject from Kane's service: pilot-wave determinism "removes the very indeterminacy the Map's tenets require" (L29), and the interpretations survey "rates pilot-wave theory the interpretation most hostile to its framework" (L71). The article then explains exactly what it *is* for — structure, not evidence: a worked demonstration that "Born statistics hold" can name an emergent, in-principle-violable regularity, plus a price list (L31).

Kane would find `sign-problem` the wing's most important page for his concerns, because it isolates the failure mode that would make libertarian agency hollow. Horn 1 (L55): if the sign is set by neural spectral properties, "the agent's contribution would carry no information about what the agent wanted" — minimal, causal, and idle. The article's demand at L83 is the right general lesson: *"an interface proposal owes a magnitude argument **and** a direction argument, and should not treat the first as discharging the second."*

### The Mysterian (McGinn)

McGinn's praise goes to the wing's habit of naming exactly which quantity is unknown, rather than gesturing at unknowability. `sign-problem` L79: *"One measurement would convert this from a dilemma into a decidable question: characterisation of the neural coupling spectrum G(ω) ... Nobody has computed or measured it."* That is a bounded ignorance with an address.

`local-tomography` L88 does the same for its own subject: the article's contribution "is to *name the exact axiom* whose interface-status is unknown — which sharpens Tenet 2 by locating its open question precisely, rather than supplying any evidence for the interface."

And `multi-agent-born` L95 names the single missing artefact rather than the general mystery: a two-agent, one-Bell-pair toy model, "the single highest-value piece of missing work." The register picked that up the same day — P-Q10 now carries an *N≥2 extension (2026-09-02)* clause naming this article.

### The Hardline Empiricist (Birch)

**This persona's verdict is load-bearing for this review, and it splits the wing cleanly in two.**

Six of the seven pages perform the discipline, several of them at moments where the opposite was available and cheaper:

- **`local-tomography` is the wing's best case of tenet-as-evidence-upgrade being praise-worthily *not* done — and the article rewrote itself to make its own claim harder.** The 2026-08-27 revision found that Galley and Masanes prove a *conjunction*: any Born modification violates purification **and** local tomography, so contraposed, *either* axiom forces the Born rule. The article states the consequence against itself at L86: a fingerprint "made of one failed axiom would be comparatively cheap; the theorem asks for two ... **The signature reading is therefore a more demanding proposal than a single-axiom version of it would be.**" It closes at L88: "speculation the Map finds attractive, not a result ... a coherence move within the framework, not framework-independent support." An article that discovers its own signature costs double and says so is doing exactly what this persona exists to praise.
- **`quantum-non-equilibrium` L31 and L75 keep the registers separate by construction.** "*nothing in this literature is about consciousness: none of the sources this article draws on connects quantum non-equilibrium to mind or free will, and every tenet-relevant inference drawn later is the Map's own, argued as such.*" The Tenet-3 inference at L75 is labelled inline — "this is the Map's own inference, found nowhere in the non-equilibrium literature" — and bounded twice: Valentini locates non-equilibrium in the early universe, never in brains; and the Map's default reading "does not use this door."
- **`quantum-non-equilibrium` L81 states the symmetric constraint explicitly**: "the Map must not quietly convert 'coherently violable' into 'probably violated.'" That is possibility/probability slippage named as a rule the article binds itself by.
- **`improper-vs-proper-mixtures` L50 refuses to promote an argument to a theorem**: "the argument is not a formal theorem, and presenting it as one overstates it — d'Espagnat himself did not." L66 then gives the detectability verdict at exactly its true size: "neither 'empty' nor 'detectable': detectable in principle and in reversible small-scale regimes, undetectable for all practical purposes at macroscopic scales."
- **`sorkin` converts a slogan into a number and a regime** (L66): replace "the Born rule is well-tested" with "κ ≲ 10⁻² (Sinha) to ~10⁻⁴ (Kauten) *in the optical regime*." Then it protects the number from misuse in both directions — L80 (a measured κ ≠ 0 can be finite-slit looped trajectories, entirely within standard QM) and L82 (Valentini & Varma test a *different observable*, Born-rule linearity in expectation values, not I₃, and the author "is a pilot-wave theorist whose programme actively seeks Born-rule violations"). Naming your own supporting citation's motivated stance is rare.
- **`multi-agent-born` L81 refuses corroboration from a null it predicts**: the micro-PK meta-analyses are "*consistency*, not corroboration, since every no-influence view predicts them identically; and on the joint demands specifically, nothing has come in ... which is weaker than the demands having survived a test."
- **`sign-problem` L65 flags its own arithmetic**: the ~25 fs thermal correlation time is "**arithmetic performed for the Map, not a measured or published neural parameter**, and no such parameter exists in the literature."

**`concepts/quantum-completeness` is the exception, and the failure is precisely the one this persona is built to catch.** It runs a structural/formal result up the evidential ladder into support for the Map. Four loci, all live in both trees:

1. **L102 — the tier-upgrade itself.** "Quantum completeness supports this: if physics is genuinely exhaustive within its domain and yet the selection of actual outcomes exceeds that domain, **then something non-physical is required**." The article's own L78 lists GRW/CSL and de Broglie-Bohm as remaining *physical* options, so "required" is not what the argument delivers. The honest form is the one its six siblings use: the formalism *leaves the gap open*; it does not *require* the Map's occupant.
2. **L44 / L54 — the no-go summary over-closes, and self-contradicts.** L44: the theorems "establish that QM is not an approximation awaiting deeper physics. Any deeper physics would face the same problems." L54: QM "is not an incomplete sketch of a deeper local, **deterministic**, or epistemic physics." Bohmian mechanics is nonlocal (Bell-compatible), contextual (Kochen–Specker-compatible) and ψ-ontic (PBR-compatible) — a standing counterexample the *same file* names 24 lines later at L78. The corpus has since built an article and a register position (**P-Q11**, 2026-09-02) on that very framework's contingency thesis.
3. **L78 — over-concession, "no unconditioned-aggregate qualifier" family.** "This proposal is empirically unfalsifiable ... The Map treats this as a philosophical framework compatible with physics, not a competing physical hypothesis." Unqualified. **P-Q9** in the register says the opposite in terms: self-concealment "is local to the *aggregate-statistics channel* ... and is **not** a global unfalsifiability shield," and names positive residue on two channels. This locus is *not* among the five in the open P2 over-concession family task (which explicitly says "work THIS list") — it is a sixth, in a file that task does not name.
4. **L58 — attribution.** "**Von Neumann's** three-process decomposition." Von Neumann distinguished *two* processes; the third is Stapp's refinement following Dirac. [[topics/completeness-in-physics-under-dualism]] L68 states it correctly — "Von Neumann (1932) originally distinguished two processes ... Stapp sharpened this into three" — so the corpus already holds the right form. (Grep-verified string sibling at `topics/psychophysical-laws-bridging-mind-and-matter` L131, out of this review's scope.)

**Why this is a calibration finding and not a praise.** The Process Philosopher and the Hardline Empiricist converge on six of these seven pages: the holism is real, and it is priced. They conflict on `quantum-completeness`, and per this skill's rule that conflict is the diagnostic — the file contains possibility/probability slippage, and the appropriate output is a `refine-draft`, minted below, not an expansion opportunity.

## Content Strengths

### `concepts/local-tomography-and-the-consciousness-physics-interface`
- **Strongest point**: the "single door with two locks" correction (L68), which *tightened a constraint against the Map's own preferred reading* and then propagated the consequence to the signature reading at L86 rather than leaving it in the technical section.
- **Notable quote**: "The theorem describes a single door with two locks, rather than two independent doors either of which would serve."
- **Why it works**: the boxworld case at L38 is doing real scope work — locally tomographic, no-signalling, and *not* Born-ruled — which is what stops the article from over-reading Galley–Masanes as a general result about probabilistic theories. Most articles would have used the theorem at its most flattering size.

### `concepts/improper-vs-proper-mixtures`
- **Strongest point**: §"The Emptiness Attack Runs in Two Directions" (L70–74). Kirkpatrick deflates the distinction to *all-improper*; Castellani, in a paper titled "All quantum mixtures are proper," deflates to *all-proper*. The article's inference is the good one: "the deflationary conclusion is thus underdetermined even among deflationists."
- **Notable quote**: "That the two flagship deflationists deflate in opposite directions is evidence that 'the simpler reading' is not even uniquely defined here." (L104)
- **Why it works**: it converts a Tenet-5 claim from assertion into a worked instance, using the opposition's own disagreement rather than the Map's assertion.
- **Second strength**: §"Whose FAPP Is It?" (L54–56) recovers Bell's coinage as an *accusation* and then declines to recruit him — "Bell is an ally on the diagnosis, not the cure: his preferred exits were Bohmian mechanics and objective collapse, both of which the Map declines."

### `concepts/sign-problem-for-conscious-observation`
- **Strongest point**: L39's diagnosis, which survives the mechanism it critiques — "**minimality of magnitude has been carrying an implicit assumption of simplicity of specification**, and those two come apart under pressure." Horn 2 then cashes it: "A sign-selecting agent is small in magnitude and complex in specification."
- **Notable quote**: "The corpus has never had to distinguish these, because it has been reading 'minimal' as 'small' while relying on it to license 'does what the agent intends.'" (L59)
- **Why it works**: it is a critique of the Map's own vocabulary, not of a rival's, and it is stated as a standing obligation rather than a one-off.

### `topics/multi-agent-born-preservation-problem`
- **Strongest point**: L57 states the *coverage* before the *residue* — "Interface locality converts the multi-agent problem from ubiquitous to boundary-case" — and only then names the three survivors. Stating what your existing answer does cover, before claiming a gap, is the discipline that keeps a self-raised problem from being theatre.
- **Notable quote**: "'the case never arises' is an empirical bet about neural physics, not a theorem." (L61)
- **Why it works**: option (a) is priced against superdeterminism's measurement-dependence and the Map's *own* psychophysical-laws defence is offered and then left open ("whether a law that makes N independent selectors jointly Born-consistent is explanatory or merely stipulated is open").

### `topics/quantum-non-equilibrium-and-the-contingency-of-the-born-rule`
- **Strongest point**: the adversarial reading at L57 — "It reads the theorem adversarially, as pricing: within this class of theories there is nothing innocent between exact equilibrium, where the statistical-level budget for any influence is zero, and signalling." This is why the Map claims Born *exactness* rather than smallness (P-Q2), and the article supplies the structural reason instead of asserting the position.
- **Notable quote**: "the Map must not quietly convert 'coherently violable' into 'probably violated.'" (L81)
- **Why it works**: §"typicality tension" (L77) is owned rather than smoothed — the rival "may be correct" — and the residual seam (Landsman on contingent initial sampling) is flagged as "an open question the Map flags rather than answers."

### `concepts/sorkin-higher-order-interference`
- **Strongest point**: the quadratic-form derivation at L49–53 — squaring a sum yields self-terms and pairwise cross-terms only, "so nothing beyond pairwise ever appears. That quadratic-form fact is the entire content of 'the Born rule forbids higher-order interference.'" One line of algebra replaces a paragraph of appeal.
- **Notable quote**: "The bound is real, tightening, and silent about the brain: exactly the shape [[tenets#^occams-limits|Tenet 5]] predicts." (L26)
- **Why it works**: it front-loads both the number and its limit in the lead, so a truncated read still gets the qualifier — a genuine LLM-first win.

### `concepts/quantum-completeness`
- **Strongest point**: §"Senses of Completeness" (L38–40). Disentangling Krizek and Mairhofer's five senses plus the Map's *predictive completeness*, and then diagnosing Einstein and Bohr as targeting different ones, is a real service and the reason the page has eleven inbound links.
- **Why it works — and where it stops**: the six-senses apparatus is exactly what should have prevented L54's slip, since "not an incomplete sketch of a deeper deterministic physics" is a claim about *bijective* completeness that the no-go theorems do not deliver. The article built the instrument and did not turn it on its own summary.

## Expansion Opportunities

### High Priority

#### Recalibrate `quantum-completeness` against the wing it anchors
- **Builds on**: the four verified loci above; the file's six-deep-review convergence streak.
- **Would address**: the wing's only tenet-as-evidence-upgrade, plus a sixth locus of the open over-concession family.
- **Estimated scope**: four localised edits, length-neutral (file at 2652w, soft_warning).
- **Tenet alignment**: strengthens Tenet 5 by removing an over-closure and Tenet 2 by scoping the unfalsifiability concession to the unconditioned-aggregate channel the register actually claims.
- **Minted as a P3 below**, with an explicit instruction to batch with the open P2 on the same file.

### Medium Priority

#### The sign/direction obligation has no N > 1 form
`sign-problem` L83 establishes that "an interface proposal owes a magnitude argument *and* a direction argument." `multi-agent-born` generalises the *magnitude* constraint to N agents — marginals, joint correlations, no-signalling — and never asks the direction question at N > 1. Yet the joint case is where direction bites hardest: option (a)'s global harmonisation is precisely a *directional* cross-agent constraint, and option (b)'s joint idleness is Horn 1 at the joint level. Neither page cites the other. Recorded here as an argumentative gap rather than minted: it needs prose, and both files are near ceilings (`sign-problem` at soft_warning, 2511/2500).

#### The improper/proper commitment is missing from P-Q1's dependency graph
`improper-vs-proper-mixtures` L96 states that "the Map's position still depends on the improper/proper distinction carrying ontological weight — a contested interpretive commitment." **P-Q1** uses that distinction as a load-bearing clause ("decoherence yields an improper mixture rather than realised outcomes with one already picked out") but its *Depends on* line lists Tenets 2 and 3, `post-decoherence-selection`, the decoherence-timescale argument, P-Q3, and the trilemma — **not** the ontological-weight commitment, and not the page that now prices it. The register cites `improper-vs-proper-mixtures`, `sorkin`, `local-tomography`, `sign-problem` and `quantum-completeness` **zero** times each (it does cite `multi-agent-born` three times and `quantum-non-equilibrium` once, both added 2026-09-02 — the wing's newest pages got same-day register entries while its older ones never did).

*Not minted*, per the reports-only contract and to avoid same-file task pile-up: an open P3 positions-evolve on `positions/quantum-interface` already exists (P-Q4's re-elevation gate, 2026-08-16). This dependency addition should ride along with it.

### Ideas for Later

- **`local-tomography`'s purification branch has no home page.** The article establishes that purification is the *other* lock and that "only the purification branch produces a signal," then says "the Map has no account of what would make purification fail across the cut." Purification is named across the wing (it is the conditional in Torres Alegre's result too) but has no dedicated treatment. Concepts is at 323 — headroom exists but this is a genuinely narrow subject; flagged, not proposed.
- **`quantum-completeness`'s "Newtonian Precedent" section** (L86–90) sits oddly beside [[framework-stage-calibration]]'s pre-Keplerian framing, which is the corpus's more calibrated analogue. Worth a look whenever the file next opens.

## Cross-Linking Suggestions

The wing's intra-link density is **3 of 42 ordered pairs**, and one of those (improper → quantum-completeness) is frontmatter-only. The highest-value additions are Further Reading entries only — five of the seven files are at `soft_warning`, so **link-only, no prose**.

| From | To | Reason |
|------|-----|--------|
| `concepts/quantum-completeness` | `concepts/improper-vs-proper-mixtures` | The one-way link becomes two-way. improper's §detectability supplies exactly the calibration quantum-completeness L78 flattens to "empirically unfalsifiable" — undetectable FAPP at macroscopic scales, detectable in principle and in reversible regimes. |
| `concepts/quantum-completeness` | `concepts/sorkin-higher-order-interference` | κ ≲ 10⁻² to ~10⁻⁴ *in the optical regime* is the numerical form of the claim quantum-completeness makes qualitatively; sorkin also marks the untested brain-internal edge. |
| `concepts/quantum-completeness` | `topics/quantum-non-equilibrium-and-the-contingency-of-the-born-rule` | The live deterministic completion whose existence L54's no-go summary excludes. |
| `concepts/local-tomography-...` | `topics/multi-agent-born-preservation-problem` | Both route the no-signalling question through `causal-consistency-constraint` and never through each other; local-tomography's "only the purification branch produces a signal" is directly relevant to multi-agent's demand 3. |
| `concepts/sign-problem-...` | `topics/multi-agent-born-preservation-problem` | The two-parameter obligation (magnitude *and* direction) has no N > 1 form; see Medium Priority above. |
| `concepts/sorkin-higher-order-interference` | `concepts/local-tomography-...` | Sorkin's §"What a Nonzero I₃ Would Mean" and local-tomography both live in the GPT framework and both cite `generalised-probabilistic-theories`; neither names the other. |
| `topics/multi-agent-born-preservation-problem` | `concepts/improper-vs-proper-mixtures` | multi-agent's composition question rests on "baseline objective collapse fixing everything outside brains" — improper's trilemma prices exactly that route (route 1). |

## New Concept Pages Needed

None. Concepts sits at 323 and this wing's gaps are wiring and calibration gaps, not missing-page gaps. The one genuine subject candidate — a dedicated **purification** page — is recorded above as an idea rather than a proposal.

---

*Reports-only review. Two `refine-draft` tasks minted below against reviewed articles; no content modified.*
