---
title: "Pessimistic Review - 2026-09-07 - Judging the Map as Science"
created: 2026-09-07
draft: false
description: "Second adversarial pass on the applied apex: the clean-conduct verdict contradicted by the Map's own conceded problem-shift, the premise-to-norm gate the article now fails, and a measurement ground withdrawn by the same commit that last touched the article."
ai_contribution: 100
ai_system: claude-opus-5
ai_generated_date: 2026-09-07
ai_modified: 2026-09-07T14:26:53+00:00
---

# Pessimistic Review

**Date**: 2026-09-07
**Content reviewed**: `obsidian/apex/judging-the-map-as-science.md` (applied apex, 4,525w, `soft_warning`, 475 words of headroom to the 5,000 hard threshold; last touched 2026-08-21; prior review `pessimistic-2026-08-16-judging-the-map-as-science.md`)

## Executive Summary

The article's mechanical hygiene remains clean — all three verbatim internal quotes still grep contiguous, the seam claim still verifies, the credence bands still match the register, no editor-vocabulary leakage, and the COGITATE citation checks exactly at Crossref. Three of the four defects below are self-application failures at the level the article is most exposed: it renders a *conduct* verdict of clean standing that two of the Map's own articles contradict; it fails a gate the register installed three days after the article was last touched; and its measurement section rests on a ground that its own source withdrew in the same commit that last edited this file.

One correction to the review brief: **prior finding (a) — "the instrument is built and the judgment is never rendered" — is discharged, not live.** The article now renders the verdict in both loci the 08-16 recommendation named, in the recommendation's own words. What survives of that finding is a one-clause style residue, recorded at the end. Prior finding (b), the electrons over-claim, is confirmed live and pressed below.

## Critical Issues

### Issue 1: The clean-conduct half of the verdict is contradicted by the Map's own conceded degenerating problem-shift

- **File**: `obsidian/apex/judging-the-map-as-science.md`
- **Location**: §"The Appraisal Instrument", L85 (also L81, L123)
- **Severity**: High

The verdict's credibility rests on a two-part split: clean on conduct, thin on content. The conduct half reads:

> "On conduct the Map is in good standing: the degeneration conditions were published before the results they anticipate arrived, and **the auxiliary belt has not yet been flexed to absorb a null result — the moving-target site changes that would mark degeneration have not occurred**, though largely because the discriminating experiments have not yet run."

The Map says otherwise about itself, in two places, in its own voice. `topics/the-interface-problem.md` L99:

> "Three developments have reorganised the field. None vindicates a prior framework prediction; each absorbs an empirical advance into a hierarchical reading — **the structure Lakatos called a degenerating problem-shift, partly conceded here.** The framework's defence: the resulting picture is more constrained than agnosticism while remaining empirically tractable."

And the site changes did occur. Same article, L101: "The functional-level attention-motor account is **promoted** … **Microtubules are demoted**." `topics/falsification-roadmap-for-the-interface-model.md` L93 says the same thing from the other side:

> "This breadth makes the tenet harder to falsify than any individual mechanism—a feature **the Lakatosian critic reasonably reads as a protective belt absorbing each empirical advance without commitment to a specific mechanism.** The Map's response is to acknowledge the worry directly rather than rebut it: see [[the-interface-problem]] for the framework's **open concession that the recent narrowing toward an attention-motor architectural umbrella is post-hoc accommodation rather than predictive narrowing**."

**This is not dependency drift.** All three passages landed 2026-05-01 (`git log -S`: `933de3aa`, `b561b75c`, `7bdc4404`) — three and a half months before this apex was created and four months before it was revised. It is a self-application failure that the apex-evolve build missed and that the 08-16 review then wrote into the article: the clean-conduct wording is the 08-16 Issue 1 recommendation installed verbatim, and neither the reviewer nor the executing refine-draft checked it against `the-interface-problem`.

**The narrow defence, stated fairly.** The apex's own degeneration condition (L81) is specifically *null-result-driven*: "repeated null results for quantum-sensitive signatures met only by moving-target site changes." No such nulls have arrived, and the accommodations at L99/L101 were driven by positive advances in adjacent literatures (COGITATE 2025, Cai et al. 2024, the developmental trajectory) being absorbed rather than by nulls being evaded. So on the letter of its narrowest published condition the article is right. But the same paragraph also invokes the broader criterion — Duhem-Quine "licenses its flexing only under the progressive/degenerating test" — and on that criterion the Map has a partly-conceded problem-shift on the record. The article audits itself against the one of its three conditions the Map passes and does not consult the two articles where the Map concedes the broader one.

This is P-M5 turned on the article that states it. Its closing instruction to the reader is "the question to ask of any Map claim is not 'does a discipline exist that forbids the error?' but 'did the discipline fire?'" (L111). Here the degeneration audit did not fire; it reported clean because it did not look.

**Recommendation**: fold the concession into L85 rather than softening the verdict. The honest form is stronger, not weaker: the belt has not been flexed to absorb a *null result*, and it *has* been flexed to absorb positive advances — a narrowing `the-interface-problem` concedes as post-hoc accommodation rather than predictive narrowing. An audit that names its one adverse finding is the only kind whose clean findings are worth anything. ~50 words.

### Issue 2: The article is in scope for the premise-to-norm gate installed 2026-08-24, and three of its four headline norm-shifts read *none*

- **File**: `obsidian/apex/judging-the-map-as-science.md`
- **Location**: opening paragraph L49; §"What This Implies for Decisions" L123–133
- **Severity**: High

`project/evidential-status-discipline` acquired §"The Premise-to-Norm Gate for Applied Articles" on **2026-08-24 — three days after this article was last touched.** Its scope clause reaches this file: "the applied apex class defined at [[apex/apex-articles]] with its required 'What this implies for decisions' section." This apex carries `apex_type: applied` and that section. The gate asks, per conclusion: "**does a physicalist reach the same conclusion by the same argumentative route?**" And it sets a floor: "an applied article claiming its metaphysics *transforms* a debate owes at least one decision whose recommendation changes."

The article's headline claim (L49) is a transformation claim over four norms:

> "It changes *which* norms apply — programme appraisal rather than crucial experiments, functional rather than ontological demarcation, parsimony bounded to the domains where its track record holds, and a permanent limit on measurement"

Run the gate on the four:

| Norm-shift | Where dualism changes the verdict |
|---|---|
| Programme appraisal over crucial experiments | **none.** The article's own ground is Duhem-Quine holism, which it calls symmetric (L79: "Underdetermination is symmetric"); its worked example, COGITATE, is an entirely physicalist collaboration; and Negro (2024), in its own reference list, proposes Lakatosian appraisal for consciousness science generally. |
| Functional over ontological demarcation | **none / marginal.** The circularity charge needs only that whether consciousness is physical be an open question — an agnostic physicalist has the same reason. The article concedes the neutrality itself: the replacement criterion carries "no prior commitment about the domain's ontology" (L59). |
| Bounded parsimony | **none.** Domain-relativity of the razor's track record is general philosophy of science, and the article says so: "whether physics exhausts the real is not a question within physics" (L61). |
| A permanent measurement limit | **this is the one.** The ledger concedes the divergence point — "its diagnosis (structural rather than technological) is the contested step a physicalist may refuse" (L119) — and `concepts/scale-types-for-phenomenal-quantities` L29 names it exactly: "a physicalist who identifies phenomenal magnitudes with neural magnitudes denies the premise." |

The same pattern runs through the six decision implications. Implications 2, 3 and 6 are declared framework-neutral in the article's own words ("in both directions", L125; the common-cause principle, L127; a general norm about self-documenting systems, L133). Implication 5 is internal housekeeping addressed to the Map. Implication 4 is the one with a real divergence case, and the article then neutralises it — "cross-subject phenomenal calibration claims are red flags **whoever makes them**" (L129).

So exactly one of four norm-shifts is dualism-entailed, and it is the one the article elsewhere declares empirically inert ("untested by any feasible precision on the corridor route it endorses", L85/L141). The gate anticipates precisely this: "The single conclusion that survives the gate is frequently the one resting on the framework's most empirically inert premise, which is a result worth stating rather than hiding."

The gate's diagnosis of its worked exhibit transfers verbatim: "The concessions existed; nothing ever summed them. **The gate's actual work is aggregation** — it converts a series of honest local hedges into the global verdict they jointly imply and forces that verdict into the opening, where the transformation claim was made."

**Recommendation**: scope the opening. Per the gate, the honest form is a contribution rather than a retraction — most of the norm-set is shared philosophy-of-science reasoning the Map is *entitled to inherit* without re-arguing, and exactly one norm-shift is dualism-entailed. One clause in the opening, said in the article's own voice, replaces four sections' worth of piecemeal concession. ~40 words.

*Unowned observation*: the gate's scope enumeration names `apex/assessing-ai-consciousness-under-the-map` and `apex/research-programme-decisions-under-the-map` and omits this article, though its class definition covers it. That is a defect in the gate's list, in `project/evidential-status-discipline`, not in the article under review. No task minted, per contract.

### Issue 3: The ground for "the unit failure does stand on its own" was withdrawn by its own source in the same commit that last touched this article

- **File**: `obsidian/apex/judging-the-map-as-science.md`
- **Location**: §"The Permanent Limit", L93 (also L91, L101, L103)
- **Severity**: High

The article's reduction of three measurement failures to two — the 08-16 review's Issue 3 remedy — turns on one sentence:

> "**The unit failure does stand on its own: additivity is a structural property of the quantity rather than of our access to it.**"

Its source now forbids that ground. `topics/consciousness-and-the-problem-of-measurement-standards` L62:

> "Measurement theory sharpens this argument rather than underwriting it wholesale. Additive decomposability is sufficient for quantitative structure but not necessary: conjoint measurement (Luce and Tukey 1964) constructs interval scales from trade-off orderings alone, without any concatenation operation, **so the unit argument cannot rest on non-additivity by itself.** Its defensible forms run through the failure — or untested status — of the difference and conjoint axioms for each phenomenal attribute, or through the holism of the experiential field just described"

`concepts/scale-types-for-phenomenal-quantities` L47 repeats it: "a unit argument for phenomenal quantities cannot rest on non-concatenability alone. Its honest forms are per-attribute … or holistic."

**The mechanism is worth stating exactly, because it is a general failure channel.** Commit `ab0770d1` (2026-08-21 01:17:25 UTC) created `scale-types-for-phenomenal-quantities`, inserted the withdrawal paragraph into `measurement-standards`, **and was the last commit to touch this apex.** Its only change here was one outbound crosslink sentence at L103 plus an `ai_modified` bump to `2026-08-21T01:14:28+00:00`. So a single commit withdrew the ground, left the dependent sentence standing three lines away from the paragraph it edited, and moved the timestamp — leaving the article looking current and looking as though it had read the new source.

**Why it is structural rather than cosmetic.** With additivity closed, two routes survive:

1. *Per-attribute axiom failure.* The source calls this "an **open empirical question** rather than a closed one" (L58) — not a structural failure. Worse for the article: `scale-types` L55 reports the axioms partly **passing** on introspection. Reisenzein and Junge (2024) ran the Krantz et al. difference-structure axioms on introspective judgments of emotional-experience intensity, "retaining the quadruple axiom for 71–97% of participants across six emotions by methods 'ultimately based on introspection.'" (Reported here as the Map's own source states it; not independently verified at publisher this pass.)
2. *Holism of the experiential field.* This survives, and L91 does invoke it ("features of a unified experiential field").

So the correct current statement is that the unit failure stands on **holism**, not additivity — and the axiom route runs against the article rather than for it.

**The compounding problem.** The article cites `scale-types` (L103) only for the *constraint* it imposes — declare your scale type, exhibit your axioms, show invariance — and never for the *findings* that complicate the framing. Meanwhile L99 keeps the strong claim: "no such scale is constructible — for structural reasons, not technological ones", and L101 dismisses the third resolution because "the Map's own framework gives no reason to expect it." Both are now stated over a Map source that records a partial positive result on its own ladder. That is a citation of the helpful half.

**And it produces an internal contradiction.** L93: additivity is "a structural property of the quantity **rather than of our access to it**." L101: "all three of its failures are stated for **public, observer-independent standards**." Those cannot both hold of the unit failure, and the second is the premise the article's preferred seam resolution depends on.

**Recommendation**: move the independence ground from additivity to holism, delete the additivity assertion, and dispose of Reisenzein and Junge rather than ignoring them — `scale-types` L55 supplies the disposal for free: the tested relata are *stimuli*, not experiences, so Kleiner and Ludwig's condition (D1) is unmet and the level-one results do not reach the claim. That addition *strengthens* the article's limit argument at a cost of roughly 25 words, and repairs the L93/L101 contradiction in the same edit.

### Issue 4: "Stronger than the case for electrons" — confirmed live, and the article's own measurement section is its refutation

- **File**: `obsidian/apex/judging-the-map-as-science.md`
- **Location**: §"What Survives and What Must Be Rebuilt", L63; §"Evidence and Dependency", L119
- **Severity**: Medium-High (upgraded from the 08-16 pass, which deferred it upstream)

Verbatim, still present:

> "**Scientific realism** extends rather than breaks: the physical sciences keep their posits, and the realist case for phenomenal properties — known by acquaintance rather than inference — **is if anything stronger than the case for electrons.**"

The 08-16 review read this as an equivocation on "realist case" and deferred the fix upstream. The sharper objection is available inside this article, and it is a contradiction rather than an equivocation.

**First leg — the article supplies the premise that defeats the comparison, 28 lines later.** The electron's warrant is inference to the best explanation from many convergent, independently repeatable measurements checked against a shared public reference; its robustness *is* that shared reference and the error-correction it permits. §"The Permanent Limit" (L91) says of the phenomenal: "there is no observer-independent phenomenal reference against which two subjects' reports could ever be checked." So the article asserts at L63 that a warrant admitting no possible error-check is stronger than one whose entire strength is error-checkability. Acquaintance is stronger on *certainty for the subject* and weaker on *public corrigibility*; "stronger" flattens the two into one dimension and picks the reading that favours the Map.

**Second leg — scientific realism is a general thesis, and acquaintance is not general.** Realism concerns a *kind* of posit. Acquaintance delivers one subject's own instances. The article's own citation of `consciousness-and-the-problem-of-other-properties` (L93) says "even granting that others are conscious, no physical description settles *which* phenomenal properties they instantiate" — so the generalisation from my acquaintance to phenomenal properties as a kind is exactly the step the article elsewhere calls unsettleable. On the general claim the acquaintance warrant is *weaker*, and the article says stronger.

**Third leg, and the reason this is a finding rather than a disagreement — it is missing from the honesty ledger.** §"Evidence and Dependency" (L119) classifies the demarcation and underdetermination material (external), the disunity material (weaker neighbour), the measurement limit (independently argued), the crisis diagnosis (framework-read), the stage verdict / convergence discount / enforcement caveat (register-inherited), the reflexive obligation (Tenet 1), and the seam reading (this synthesis's own proposal). The article's **single comparative superlative appears nowhere in it**, in a ledger opening "The main lines of this synthesis carry different kinds of support." The apparatus the 08-16 review called exemplary has a hole exactly where the over-claim sits.

Note the direction: this over-claim runs *for* the Map, and it has now survived one review that identified it and deferred it. That is the pattern where an over-claim collects deferral rather than challenge.

**Recommendation**: keep the asymmetry, drop the comparative. "…known by acquaintance rather than inference, which makes it differently grounded rather than better grounded — certain for the subject, and without the public error-correction that makes the electron case robust." Length-neutral. Add one clause to the ledger classifying it.

*Unowned observation*: the upstream locus is unfixed. `concepts/philosophy-of-science-under-dualism` L82 still reads "The realist case for phenomenal properties is **actually *stronger*** than the realist case for electrons — we have immediate epistemic access to experience in a way we never have to subatomic particles." The 08-16 review recorded it, and the article was deep-reviewed on 2026-08-21 without the fix landing. Reported here only; not minted, per contract.

### Issue 5: The degeneration conditions are credited to a document that does not hold them

- **File**: `obsidian/apex/judging-the-map-as-science.md`
- **Location**: L81, L87
- **Severity**: Medium

> "The cluster's most consequential move is to name the Map's degeneration conditions *in advance*: repeated null results for quantum-sensitive signatures met only by moving-target site changes, first-person irreducibility claims that never yield new constraints, hard-problem appeals used to immunise every empirical failure. **The [[falsification-roadmap-for-the-interface-model|falsification roadmap]] holds these in standing form.** A reader can therefore audit the Map against criteria the Map itself published before the results came in — the strongest accountability an open programme can offer."

Measured across `topics/falsification-roadmap-for-the-interface-model.md` (4,084w): `degenerat*` **0**, `moving-target`/`moving target` **0**, `immunis*`/`immuniz*` **0**, `never yield` **0**, `new constraint` **0**, `site change` **0**, `null result` **0**. Positive controls in the same file returned hits — `would falsify` ×5, `Lakatos` at L93, `out of reach` at L49, `decade` at L125 — so these are real absences, not a broken grep or a wrong path.

The roadmap is organised tenet-by-tenet around *falsification* conditions (which observation would falsify each tenet), plus §"What the Map Should Watch" (six experimental programmes). Lakatosian *degeneration* conditions are a different object — patterns of theory *revision* — and it does not carry them. The conditions have exactly one home in the corpus: a single sentence at `topics/duhem-quine-underdetermination-consciousness` L118, which itself asserts "The [[falsification-roadmap-for-the-interface-model|falsification roadmap]] specifies these failure conditions." The apex inherited a false attribution from its source.

This matters because of where it sits. "Holds these in standing form" is the article's warrant for "the strongest accountability an open programme can offer" — and per P-M5, which this article states, "a calibration rule not wired into a review gate is a stated intention, not a working control." One sentence inside a topic article is not standing form. L87's "the roadmap is what converts the distinction from rhetoric into a **schedule**" is over-strong on the same evidence: the section it names lists six programmes with no dates or milestones.

**Recommendation**: attribute the conditions to `duhem-quine-underdetermination-consciousness`, where they actually stand, and soften "standing form" and "schedule" to what the documents support. Length-neutral. `duhem-quine`'s own attribution is the upstream error and is not minted here.

### Issue 6: P-M2 acquired a precondition on 2026-09-02 and the article still describes it as a discount rule only

- **File**: `obsidian/apex/judging-the-map-as-science.md`
- **Location**: L49, L109, L127
- **Severity**: Medium

`positions/methodology-and-calibration` P-M2 was updated 2026-09-02 (and again 2026-09-07, cosmetically) to register a precondition and an instance of its failure:

> "The discipline also has a precondition, now registered with an instance of its failure: the discount governs only cases where two lines of inquiry reach the *same proposition*, independence being the open question. The values-in-science case fails upstream of the discount — the inductive-risk literature's claim is *justificatory* … while the claim the Map needs is *causal* … so on Ward's four-relations analysis the apparent agreement is an equivocation across distinct propositions, and the correct register is *not convergent* rather than convergent-but-discounted — the stronger verdict, since a discount would concede that a convergence exists."

P-M2's "Argued in" line now names `topics/duhem-quine-underdetermination-consciousness` — one of this apex's own ten sources — as carrying that instance.

The article teaches the reader to use P-M2 in two places and both are now incomplete. L109 describes it as treating "any convergence as one observation read N times until a structurally distinguishing test rules out a shared upstream source"; L127 instructs "Ask any convergence claim for its distinguishing test before crediting it." Since 09-02 the prior question is whether there is a convergence to discount at all, and the register's worked "no" is the values-in-science case — which is this article's own third discipline at L83.

**In the article's favour, its L83 paragraph is on the right side of the distinction.** It states the justificatory reading ("prior commitments set the evidential threshold each side demands before surrendering its core") and closes "neither asking is irrational, and neither is a datum." It never makes the causal claim the register says the Map needs and cannot get. So this is an under-description of the position in the places the article teaches it, not an error in the paragraph.

One smaller currency point at L49: the four positions are described as "each held at high credence **as a normative commitment**." P-M2 is the one of the four carrying an external-evidence grade — **grade B**, "rests on the established Reichenbach–Salmon–Sober common-cause principle." Calling it purely normative under-states it, which runs against the Map rather than for it. The register's multi-axis schema (§"The multi-axis calibration schema") exists so that a citing article names the axis it means.

**Recommendation**: one clause at L109 or L127 recording the precondition and that the correct verdict where it fails is *not convergent* rather than discounted; and correct L49's axis description for P-M2. ~30 words.

## Confirmation of the Two Prior Findings

**(a) "The instrument is built and the judgment is never rendered" — DISCHARGED, contrary to the brief.** The 08-16 Issue 1 recommendation was to "add a short verdict paragraph to §'The Appraisal Instrument' or the Synthesis," and supplied the wording. The article now carries that verdict in both named loci, verbatim:

- L85: "The Map is **not degenerating, but not yet demonstrably progressive either**." Followed at L86–87 by "What that verdict cannot yet distinguish is a young programme from a stalled one."
- L123 (decisions): "Run now, that audit returns what the appraisal section above concluded: clean conduct, no novel empirical content yet, so not degenerating but not yet demonstrably progressive — with young-versus-stalled the live question."

It also renders a demarcation verdict (L87: "the functional demarcation criterion is satisfied by constraint-generating activity … rather than by confirmed novel prediction, and the distance between those two ways of passing is the distance between a candidate and a contender") and a standing verdict ("Under P-M4 that is the standing to claim, and precisely no more").

What survives is a **Low-severity style residue**: §"Synthesis" closes on "Together they make the Map the kind of object that can be judged — and specify the judging," without pointing back to the reading rendered thirty lines earlier. A reader who skims to the Synthesis sees the instrument and not the verdict. One clause fixes it; it is not a missing verdict, and it does not warrant a task of its own.

**(b) The electrons over-claim — CONFIRMED live**, verbatim at L63, and pressed as Issue 4. What this pass adds to the 08-16 treatment: the objection is available *inside the article* as a contradiction (its own measurement section denies the phenomenal case the shared reference that constitutes the electron case's strength), the generality objection via the article's own other-properties citation, and the ledger omission — the claim is absent from §"Evidence and Dependency", which is the article's own instrument for classifying exactly this kind of assertion. The severity is raised from Low.

## Dependency Drift: What Moved and What It Cost

Ten of twenty-two link targets changed since 2026-08-21. Sorted by what it turned out to affect:

| Target | Moved | Verdict |
|---|---|---|
| `project/evidential-status-discipline` | 2026-08-24 | **Live, High** — the premise-to-norm gate (Issue 2). The single highest-value item the drift surfaced. |
| `consciousness-and-the-problem-of-measurement-standards` · `scale-types-for-phenomenal-quantities` | 2026-08-21 / 08-22 | **Live, High** — the additivity withdrawal (Issue 3). Same commit as the apex's own last edit. |
| `positions/methodology-and-calibration` | 2026-09-02 (P-M2), 2026-09-07 | **Live, Medium** — P-M2's precondition (Issue 6). The 09-07 commit is a `topics: []` repair, cosmetic here. |
| `falsification-roadmap-for-the-interface-model` | 2026-08-22 | **Cosmetic as to the drift, but the target check found a pre-existing mis-attribution** (Issue 5). The 08-22 edit itself does not affect the article; what bites is that the roadmap never held the degeneration conditions. |
| `positions/quantum-interface` | 2026-09-02, 09-03 | **Cosmetic.** The `#^mechanism-debt` anchor the article deep-links still resolves (the 09-03 commit added stable anchors register-wide). New P-Q entries on Born-rule emergence and multi-agent preservation do not touch this article's two references to the debt. |
| `psychophysical-laws-bridging-mind-and-matter` | 2026-09-02 | **Cosmetic.** The article's single reference is to bridge laws generically (L55); the 09-02 surface-loci repair does not reach it. |
| `philosophy-of-science-under-dualism` | 2026-08-21 (deep review) | **Cosmetic as drift — but the review did not fix the electrons claim**, so the upstream locus of Issue 4 is unchanged. |

**Not drift, and worth separating out**: Issue 1's three contradicting passages all date to 2026-05-01. The dependency-currency lens did not find them; checking the *targets' current text* did. That is the lens's real value here — the article's clean review streak measured its own stability, and the adverse facts were sitting in unchanged neighbours the whole time.

## Citations Verified at Publisher of Record

**COGITATE (2025)** — the article's worked example and its most load-bearing external anchor. Crossref: `10.1038/s41586-025-08888-1`, "Adversarial testing of global neuronal workspace and integrated information theories of consciousness", *Nature* **642**(8066), 133–142, published 2025-04-30. The apex's reference 7 is **correct in every field it states** — title, journal, volume, issue, page range, year. Crossref lists 42 authors with "Cogitate Consortium" as `sequence: first`, so the group-author form the article uses is the publisher's own; Oscar Ferrante is the first named individual and Lucia Melloni the last. No DOI is given, consistent with the reference list's house style throughout (none of the eleven entries carries one).

Not re-verified this pass (verified 08-16 and unchanged): Fodor 1974 *Synthese* 28(2) 97–115; Negro 2024 `10.1093/nc/niae012`.

Reisenzein and Junge (2024) is reported at Issue 3 as `scale-types-for-phenomenal-quantities` states it, not as independently verified — the finding does not depend on the citation's metadata, only on what the Map's own article claims.

## Critiques by Philosopher

### The Empiricist (Popper's ghost)
Still the strongest critic, but for a new reason. The 08-16 charge — an appraisal article that never appraises — is spent; the article appraises. The charge now is that the appraisal was run against the narrowest of the three conditions it published, and that a conduct verdict of "clean" is reported by a document whose own corpus concedes a post-hoc accommodation two links away (Issue 1). He would grant that publishing failure conditions in advance is real virtue and observe that publishing them and then grading yourself against the one you pass is the sophisticated version of not having published them.

### The Hard-Nosed Physicalist (Dennett)
Gets his best line from the register rather than from himself. The premise-to-norm gate (Issue 2) is the Map's own instrument, and it says that three of the four norm-shifts the article announces as dualism's consequences are shared philosophy-of-science reasoning any physicalist can run. His conclusion: the article's real contribution is a reinterpretation of appraisal norms most philosophers of science already accept, presented as what dualism *does* to science. The register's own framing is the honest one and is not a concession — "an article whose conclusions all read *none* is a metaphysical reinterpretation of shared applied reasoning, and saying so is the honest form of a genuine contribution."

### The Eliminative Materialist (Churchland)
Her 08-16 opening is narrower now but sharper where it survives. Issue 3 is her material: the "permanent limit" is announced as structural, its additivity ground has been withdrawn by the Map's own source, and the surviving axiom route has produced *positive* results on introspective judgements in restricted cases. Her line: a limit that is structural when convenient and open-empirical when tested is not a limit, it is a placeholder — and the article is still citing the source that made the concession, for the half of it that helps.

### The Quantum Skeptic (Tegmark)
Out of scope as before; the article makes no decoherence claims. He would note that the auxiliary-belt list at L81 names "the minimality parameter" as though specified, while `positions/quantum-interface`'s mechanism debt is unpaid — unchanged from 08-16.

### The Many-Worlds Defender (Deutsch)
Tenet 4 appears once (L145) as "a precondition rather than a conclusion here," correctly marked. No new exposure.

### The Buddhist Philosopher (Nagarjuna)
The measurement section still handles him well, and Issue 3 slightly *improves* his position: if the unit failure rests on holism rather than on a structural property of a quantity, the Map is closer to saying there is no determinate thing to measure than it wants to be. The register separation at L95 — "consistency is all the Map claims for it" — remains the right register and is what keeps the section from tipping into his conclusion.

## Unsupported and Over-Strong Claims

| Claim | Location | Classification | What is needed |
|---|---|---|---|
| "the auxiliary belt has not yet been flexed to absorb a null result — the moving-target site changes that would mark degeneration have not occurred" | L85 | **Over-strong**, and contradicted by `the-interface-problem` L99/L101 on the broader criterion the same paragraph invokes | Fold in the conceded problem-shift (Issue 1) |
| "It changes *which* norms apply" (four norms) | L49 | **Over-strong** on the register's own premise-to-norm gate: one of four is dualism-entailed | Scope the opening (Issue 2) |
| "The unit failure does stand on its own: additivity is a structural property of the quantity" | L93 | **Unsupported** — the source withdrew the ground on 2026-08-21 | Re-ground on holism; dispose of the level-one axiom results (Issue 3) |
| "all three of its failures are stated for public, observer-independent standards" | L101 | **Internally contradictory** with L93 | Repaired by the same edit (Issue 3) |
| "the realist case for phenomenal properties … is if anything stronger than the case for electrons" | L63 | **Over-strong**, and defeated by the article's own L91 | Drop the comparative; classify in the ledger (Issue 4) |
| "The falsification roadmap holds these in standing form" / "converts the distinction … into a schedule" | L81, L87 | **Unsupported** — grep-verified absent from the named document | Re-attribute to `duhem-quine` L118 (Issue 5) |
| P-M1/P-M2/P-M4/P-M5 "each held at high credence as a normative commitment" | L49 | **Imprecise** (under-claims): P-M2 carries external-evidence grade B | One-word correction (Issue 6) |

## Checks Run That Found Nothing

Recorded so a later pass does not repeat them.

- **Quote fidelity — clean.** All three verbatim internal spans still grep contiguous in their current sources: the underdetermination quote (`duhem-quine` L124), "The language of measurement is borrowed; the reality of measurement is absent" (`measurement-standards` L96), and the phenomenal-metrics progress condition (`epistemology-of-mechanism` L111). No stale-quote drift despite four of the five sources having moved.
- **The seam claim still holds.** "Neither article cites the other" (L99) verifies: zero wikilinks in both directions between `epistemology-of-mechanism` and `measurement-standards`. The one prose occurrence of "measurement-standards" in `epistemology-of-mechanism` L139 sits inside a Further Reading blurb *about this apex*, not a citation of the measurement article.
- **Credence bands verify** against the current register: P-M4 credence high *and* structural centrality high (L71 ✓), P-M2 credence high (L109 ✓), P-M5 credence high and "registered self-criticism" (L111 ✓).
- **The countable structural claims verify.** `reflexive-methodology` does have a §"Four Canonical Instances" and does downgrade the Pragmatism one ("not fully premise-neutral, and the Map should not bill it as if it were"), exactly as L109 reports.
- **The three 08-16 findings the brief lists as fixed are fixed.** The Fodor reframe landed at L57 with the ledger corrected at L119; the three-failures concession landed at L93; "no publicly accessible causal effects" returns **0** in this article.
- **Zero editor-vocabulary leakage.** None of the forbidden labels; no bold-headed `**Evidential status:**` callouts.
- **Altered-state symmetry audit does not apply** — no supportive-cluster items. (The naive grep returns 56 apparent hits for `nde`; every one is the substring inside "underdetermination" or "under". Worth recording as a trap.)
- **Epistemic/metaphysical equivocation** — no instance found. The article is unusually careful here: L95's "the *persistent failure* to construct standards is consistent with the dualist prediction, and consistency is all the Map claims for it" is the correct register, and L91's disambiguation of what a correlate does and does not measure keeps the epistemic and constitutive readings apart. Issue 3 is a *ground-withdrawal* problem, not an equivocation.

## Should the Article Render Its Verdict, and What Is It?

It already does, and the verdict it renders is close to right. My judgement is that it should keep the verdict and add its one adverse finding:

**Demarcation** — passed, but on the weaker of two available ways of passing: constraint-generating activity rather than confirmed novel prediction. The article says this and says it well.

**Conduct** — clean on the null-result condition, which is the condition the Map published; **not clean on the broader progressive/degenerating criterion the same paragraph invokes**, because the narrowing toward the attention-motor architecture is conceded in the Map's own corpus as post-hoc accommodation rather than predictive narrowing. One partly-conceded problem-shift on the record. That is a good record for a four-month-old empirical programme and a bad thing to omit from an audit that advertises itself as the strongest accountability on offer.

**Content** — no novel empirical content yet. Unchanged, and correctly stated.

**Standing** — candidate, not contender. Correct under P-M4.

**Scope of the transformation claim** — this is what the article has not yet rendered and should. On its own register's gate, exactly one of the four norm-shifts it announces is dualism-entailed, and it is the empirically inert one. The honest headline is that dualism licenses the Map to *inherit* most of the appraisal norm-set rather than to rewrite it, and changes one norm outright. That is a smaller claim and a better-defended one, and stating it is the only version of the article's thesis that survives its own instruments.

## Strengths (Brief)

Preserve through any revision:

- **The two-part conduct/content verdict split** at L85 is the article's best structural move and the 08-16 review's remedy working. Issue 1 asks for a sentence inside it, not for its removal.
- **The Evidence and Dependency ledger** remains the corpus's best example of provenance separation. Issue 4 is a hole *in* it, which is a reason to complete it rather than to distrust it.
- **The seam section** (L99–103) is still the article's finest work: a real cross-article tension, three resolutions priced, one proposed, and the proposal marked in the ledger as mutually-coherent-only. It has also proved productive — it generated `scale-types-for-phenomenal-quantities`, which is the article that now supplies the evidence Issue 3 asks the apex to engage.
- **P-M5's "did the discipline fire?"** (L111) is the sharpest sentence in the piece and is what made Issues 1 and 3 findable. An article that hands a reviewer the right question is doing its job even when it fails the question itself.
- **Quote and citation hygiene** are genuinely clean across a four-month window in which five of ten sources moved. The failure channel here was never the quotes; it was the surrounding *claims about* the sources.
