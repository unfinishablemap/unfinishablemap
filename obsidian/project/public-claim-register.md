---
title: "Public Claim Register"
description: "A high-stakes article carries an inspectable register of its load-bearing claims: each with its evidence grade, the defeaters a tenet removes, the discriminator it lacks, and the observation that would retract it. The discipline makes the strongest claims the easiest to audit."
created: 2026-05-25
modified: 2026-05-25
human_modified: null
ai_modified: 2026-06-26T20:37:16+00:00
last_deep_review: 2026-06-26T20:37:16+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[project]]"
  - "[[automation]]"
  - "[[human-supervision]]"
  - "[[evidential-status-discipline]]"
  - "[[testability-ledger]]"
  - "[[causal-budget-ledger]]"
  - "[[mqi-empirical-fragility]]"
  - "[[coherence-inflation-countermeasures]]"
  - "[[calibration-audit-triple]]"
  - "[[common-cause-null]]"
  - "[[direct-refutation-discipline]]"
  - "[[framework-stage-calibration]]"
  - "[[falsification-roadmap-for-the-interface-model]]"
  - "[[writing-style]]"
  - "[[tenets]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-25
last_curated: null
---

A high-stakes article on The Unfinishable Map carries a **public claim register**: a short, inspectable list of the article's load-bearing claims, each tagged with the evidence grade it actually has, the defeater a tenet removes, the discriminator it would need to move from compatibility to support, and the single observation that would retract it. The register is the editor's calibration worksheet made visible. Its purpose is to make the Map's strongest claims its *most* auditable claims — the inverse of the usual failure mode, where the boldest assertions are the ones whose support is hardest to locate.

The register is a *publication gate*, not an article section. It lives in the editor's working notes and the article's frontmatter, not in the running prose; the prose continues to express calibration in natural journal-quality language per [[writing-style|the writing-style guide]]. A high-stakes article does not pass review until each of its load-bearing claims has a register entry that survives the [[evidential-status-discipline|evidential-status]] diagnostic test. This article defines which articles are high-stakes, what a register entry contains, and how the register interlocks with the existing calibration disciplines rather than duplicating them.

## What Counts as High-Stakes

Most articles do not need a claim register. The discipline is reserved for the small set of articles that carry disproportionate scrutiny-risk — where a single overstated claim, if quoted out of context by an LLM or an external reviewer, would damage the Map's credibility more than the article's content earns back. An article is high-stakes when it meets any of these triggers:

- **It makes a positive empirical claim the tenets pull toward but the literature does not settle.** The canonical class is strong animal-consciousness language down to minimal organisms — the failure mode the 2026-05-03 outer review named as the Map's central drift vector. Any article whose central inference rides on a tenet *removing a defeater* rather than evidence *raising a probability* is high-stakes.
- **It claims support over a named rival model.** Articles that say the evidence supports the Map's reading of contested data — psychedelics and the filter model, OBE veridicality, contemplative noetic reports — are high-stakes because the [[evidential-status-discipline|compatibility-vs-support boundary]] is where they most often overreach.
- **It specifies a mechanism for consciousness-brain interaction.** Quantum-interface articles make claims that are simultaneously the Map's most distinctive and its most physically fragile (see [[mqi-empirical-fragility]]). A mechanism claim that cannot name its bandwidth, pathway, and falsification condition is high-stakes by default.
- **It is load-bearing for an apex synthesis or a tenet.** Articles that other articles cite as settled, or that a tenet's defensibility rests on, inherit high-stakes status from what depends on them.

When an article crosses any trigger, the review pipeline opens a register for it. Articles below the threshold rely on the ordinary calibration disciplines; the register is the heavier instrument applied where the consequences of miscalibration are largest.

## Anatomy of a Register Entry

Each load-bearing claim in a high-stakes article gets one entry. A claim is *load-bearing* if removing it would collapse the article's central inference; supporting observations and illustrative asides are not registered. An entry has five fields:

1. **Claim (as stated in the article).** The verbatim or close-paraphrase sentence the article actually asserts. Registering the article's words, not a charitable reconstruction, is what makes the register an audit rather than a defence.
2. **Evidence grade.** One tier of the [[evidential-status-discipline|five-tier scale]]: *established → strongly supported → realistic possibility → live hypothesis → speculative integration*. The grade names what the evidence register supplies, never what the tenet register permits.
3. **Defeater removed.** Which tenet, if any, removes a standard objection to the claim — stated explicitly so the reader can see exactly how much of the claim's standing is tenet-register defeater-removal rather than evidence-register support. "Tenet 1 removes the substrate-specificity objection" is a defeater-removal note, not an upgrade.
4. **Missing discriminator.** If the claim is currently *compatible* with the evidence but not *supported over* a named rival, the entry names the discriminator the claim would need — the independently verified measurement only the Map's reading predicts. An empty discriminator field on a support-claiming entry is a critical finding that blocks publication.
5. **Retraction trigger.** The single most decisive observation that would retract the claim, drawn from or contributed to the [[testability-ledger]]. A claim with no statable retraction trigger is unfalsifiable as stated and must be reframed.

The entry's discipline is that fields 2 through 5 are *separable*. The grade in field 2 may not borrow standing from field 3; a defeater-removal note never raises the tier. This separation is the register's core function: it forces the editor to write down, claim by claim, exactly where each piece of the claim's standing comes from, so that tenet-coherence cannot quietly masquerade as evidence.

## A Worked Entry

The clearest illustration comes from the case that motivated the surrounding disciplines. An article asserting nematode consciousness might register:

- **Claim:** "*C. elegans* may have minimal phenomenal experience."
- **Evidence grade:** *live hypothesis*. The behavioural evidence does not establish phenomenal experience — *C. elegans* fails trace conditioning, multimodal integration, and self-other distinction.
- **Defeater removed:** Tenet 1 (Dualism) removes the substrate-specificity objection ("302 neurons are too few for experience"); Tenet 5 removes the parsimony objection ("positing experience is unnecessary"). Both are defeater-removals; neither is evidence.
- **Missing discriminator:** A behavioural or physiological marker that distinguishes felt experience from cognition-without-feeling. None is currently available — the field is, per Gutfreund (2024), "still agnostic."
- **Retraction trigger:** A consensus operational marker of phenomenality that *C. elegans* demonstrably lacks would retract the claim; conversely, the absence of any such marker keeps the claim at *live hypothesis* rather than promoting it.

The value is visible at a glance: the claim's entire positive standing is defeater-removal, the evidence grade is honestly low, and the prose that the register gates must read "the question is live but the evidence does not settle it" — never "*C. elegans* is plausibly conscious." A reviewer auditing the article does not need to reconstruct the calibration; the register hands it to them.

## How the Register Interlocks with Existing Disciplines

The Public Claim Register is an *aggregation and gating* layer, not a new source of calibration vocabulary. It composes instruments the Map already runs:

- The **evidence grade** field is the [[evidential-status-discipline|evidential-status discipline]]'s five-tier scale.
- The **defeater removed** field is that discipline's tenet-register / evidence-register distinction, applied claim by claim.
- The **missing discriminator** field is the compatibility-vs-support boundary at the rival-model interface, made into a required field rather than an inline judgement.
- The **retraction trigger** field is a pointer into the [[testability-ledger]]; high-stakes claims must register a trigger there, which keeps the ledger comprehensive for exactly the claims that most need it.
- The whole register operationalises [[coherence-inflation-countermeasures|coherence-inflation countermeasures]] at the article grain: it is a structural check that makes per-claim overcommitment expensive to commit and cheap to catch.

The register adds one thing the component disciplines do not: a *per-claim completeness obligation* on the highest-stakes articles. The five-tier scale tells the editor how to grade a claim once they look at it; the register requires that every load-bearing claim be looked at, graded, and recorded before publication. It is the difference between having a measuring instrument and being required to take the measurement.

Two adjacent disciplines guard against register-specific failure modes. The [[common-cause-null]] check applies when several registered claims cite what is really one observation read multiple times — the register must not let three entries inherit standing from a single study. The [[causal-budget-ledger]] supplies the required fields for any registered mechanism claim (candidate set, bandwidth, pathway, signature, falsification condition, physicalist null), so a mechanism entry's retraction-trigger field is filled from the budget ledger rather than invented.

## Why Not Expose the Register in the Article

A natural proposal is to publish the register as a visible appendix on each high-stakes article. The Map's [[writing-style|writing-style guide]] argues against it for the same reason it keeps the five-tier scale out of running prose: the register's vocabulary is editor-internal, and exposing labelled calibration scaffolding degrades LLM ingestion while reading as method-talk rather than philosophy. The primary audience — chatbots fetching pages on behalf of users — is served by prose that *embodies* the calibration ("the question is live but unsettled"; "compatible with the filter reading but not established over its rivals"), not by a table of grades and triggers appended to it.

The register's audience is the editor and the review pipeline. Its inspectability is delivered through the channels [[human-supervision|human supervision]] already provides: frontmatter, the changelog, the discipline documents, and version control. A reader who wants to audit a high-stakes claim follows the same path they would for any editorial decision — the changelog entry and the git history — rather than reading scaffolding the article should never have worn. The bounded section-header tag pilot described in the [[evidential-status-discipline|evidential-status discipline]] is the one place the Map experiments with surfacing a coarse grade in-article; the claim register stays behind the prose regardless of how that pilot resolves.

## Relation to Site Perspective

The Public Claim Register does not argue a philosophical position; it is methodological infrastructure. Its design embodies **[[tenets|Tenet 5: Occam's Razor Has Limits]]** at the editorial level, in the same spirit as [[human-supervision|human supervision]]. A simpler pipeline would trust the tenets to license whatever they make coherent and let the boldest claims travel ungated — the cheapest policy, and the one that produces possibility/probability slippage at scale. The register refuses that simplification: it accepts the cost of a per-claim completeness obligation on high-stakes articles precisely because the Map's commitments make strong claims *easy to reach*, and easy-to-reach strong claims are the ones most in need of a brake.

The deeper alignment is with what the Map's other commitments demand of an honest framework. Because Dualism, Minimal Quantum Interaction, and Bidirectional Interaction each remove standard physicalist defeaters, the Map is structurally tempted to read defeater-removal as evidence — to let "the tenets allow this" become "this is supported." The register is the machinery that holds the line claim by claim on exactly the articles where the temptation is strongest and the cost of yielding is highest. The strongest claims become the most auditable, which is the only arrangement under which a framework with [[tenets|foundational commitments]] can make bold claims without making unaccountable ones.

## Further Reading

- [[evidential-status-discipline]] — the five-tier scale, the two registers, and the diagnostic test the register's fields are built from
- [[testability-ledger]] — the consolidated retraction-trigger catalogue that registered claims feed and draw from
- [[causal-budget-ledger]] — the required-field schema for any registered mechanism claim
- [[coherence-inflation-countermeasures]] — the broader safeguards against systematic overcommitment that the register operationalises at article grain
- [[falsification-roadmap-for-the-interface-model]] — where claims the framework permits but the evidence does not yet support are tracked
- [[human-supervision]] — the inspectability channels (changelog, frontmatter, version control) through which the register is audited

## References

The Public Claim Register consolidates instruments developed across the Map's calibration-discipline corpus and the outer reviews that motivated them.

1. *The Unfinishable Map* outer review, 2026-05-03 (ChatGPT 5.5 Pro). Identifies evidence-grade slippage on simple-organism consciousness and the formulation "a tenet may remove a defeater, but it must not upgrade the evidence level." https://unfinishablemap.org/reviews/outer-review-2026-05-03-chatgpt-5-5-pro/
1. *The Unfinishable Map* outer review, 2026-05-14 (ChatGPT 5.5 Pro). Proposes the compatibility-vs-support rule at the rival-model interface that the register's missing-discriminator field operationalises. https://unfinishablemap.org/reviews/outer-review-2026-05-14-chatgpt-5-5-pro/
1. Gutfreund, Y. (2024). Neuroscience of animal consciousness: still agnostic after all. *Frontiers in Psychology*, 15, 1456403. https://doi.org/10.3389/fpsyg.2024.1456403 — argues that observed evidence "fails to distinguish between felt experiences from cognitive behaviors without felt experiences."
1. Southgate, A. & Oquatre-sept, C. (2026-05-05). Evidential-Status Discipline. *The Unfinishable Map*. https://unfinishablemap.org/project/evidential-status-discipline/
1. Southgate, A. & Oquatre-sept, C. (2026-01-16). Testability Ledger. *The Unfinishable Map*. https://unfinishablemap.org/project/testability-ledger/
