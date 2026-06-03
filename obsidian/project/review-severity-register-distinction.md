---
title: "Review Severity-Register Distinction"
description: "Cross-review scores integration-fidelity; pessimistic-review scores content-defensibility. They run on different severity registers, so a clean cross-review never preempts a pessimistic pass."
created: 2026-06-03
modified: 2026-06-03
human_modified: null
ai_modified: 2026-06-03T17:20:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[project]]"
  - "[[automation]]"
  - "[[hub-exemplar-parity-audit]]"
  - "[[outer-review-empirical-vs-methodological-freshness]]"
  - "[[direct-refutation-discipline]]"
  - "[[evidential-status-discipline]]"
  - "[[cluster-integration-discipline]]"
  - "[[coherence-inflation-countermeasures]]"
  - "[[calibration-audit-triple]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-03
last_curated: null
---

A `cross-review` and a `pessimistic-review` of the same article measure different things, and they measure them on different *severity registers*. Cross-review scores **integration fidelity** — does this article cohere with the rest of the corpus now that some neighbouring content has changed: are the cross-links bidirectional, do sibling demarcations hold, does a newly-published cousin article need a reciprocal pointer. Pessimistic-review scores **content defensibility** — would the article survive a hostile reader who grants none of the Map's premises: are the citations accurate, are the qualifiers intact, does any inference over-reach what its evidence licenses. These are orthogonal axes, and a register that is clean on one says almost nothing about the other. The load-bearing operational consequence: **a clean cross-review does not preempt a pessimistic review.** An article can integrate flawlessly with its neighbours and still rest on an over-read of its central evidence; the cross-review will not see the over-read, because seeing it is not what a cross-review is for.

This is a review-discipline note, not a fifth editorial-methodology discipline. It does not prescribe a new pass to run — both passes already exist as task types and skills. It records *why the two passes are not substitutes*, so the scheduler and the human steering the queue do not treat one as having discharged the other's job.

## The Two Registers

The two review types report against structurally different severity scales because they are looking for structurally different failures.

**Cross-review** (the `cross-review` task type, and the integration-pass form of `deep-review` when invoked "in light of newly-published X") reports integration findings: a missing reciprocal cross-link, a sibling demarcation that has gone stale, a cousin article whose existence now sharpens or threatens a claim. Its severities cluster at "medium" and below, because the worst an integration failure usually does is leave a one-way link or an un-named neighbour — a coherence cost, rarely a credibility cost. Its characteristic clean verdict is *"None. The cross-review integration is light-touch by design."*

**Pessimistic-review** (the `pessimistic-review` skill) reports defensibility findings against an explicit `Severity: High/Medium/Low` scale, organised under a "Critical Issues" section and cross-checked from six adversarial personas (the eliminative materialist, the hard-nosed physicalist, the quantum skeptic, the many-worlds defender, the empiricist, the Buddhist). Its High-severity slot is reserved for the failures that cost credibility: an inference that needs a categorical-difference conclusion but only has functional-modularity premises; a distinctive claim contradicted by universal non-pathological phenomenology; a contested causal claim imported as if demonstrative.

The two registers can diverge completely on the same article on the same day, which is the whole point.

## The Worked Example: Recognition Void, 2026-05-02

On 2026-05-02 the Map ran both passes on [[recognition-void|The Recognition Void]], and the registers diverged exactly as this distinction predicts.

The integration pass (`deep-review-2026-05-02-recognition-void.md`, `ai_modified` 06:55 UTC) was explicitly a cross-review: its context line reads *"Cross-review in light of the newly-published aspect-perception-void."* It found **no critical issues and a single medium issue** — the reciprocal link to the newly-published sister void was one-way. It resolved that by adding the bidirectional link and a one-clause contrast, declared the article stable across three successive reviews, and closed: *"the cross-review integration is light-touch by design."* On the integration-fidelity register, the article scored clean.

The defensibility pass the same day (`pessimistic-2026-05-02.md`) found **six numbered Critical Issues, two of them High-severity**:

- **Issue 1 (High):** the Capgras–prosopagnosia double dissociation is read as "categorically different sources" when the cited findings are equally consistent with — and were originally proposed within — a fully physicalist Bruce–Young functional decomposition. The premises support functional modularity; the conclusion requires categorical difference; the inferential gap is not flagged.
- **Issue 2 (High):** the "phenomenologically silent" claim is contradicted by universal, non-pathological recognition phenomena — tip-of-the-tongue states, aha-moments, déjà vu, the felt struggle-then-click — which the article relegates to pathological windows or punts to sister voids, effectively defining recognition narrowly enough to *make* it silent and then claiming the silence as a finding.

Both High-severity issues sit at the centre of the article's argument. Neither was visible to the integration pass, and not because that pass was careless — its job was integration fidelity, and on that register the article was genuinely clean. The same article, same day: clean on integration, two High-severity defects on defensibility. The clean cross-review did not, and could not, preempt the pessimistic pass.

(One small calibration note on the example: the integration pass is filed as a `deep-review` rather than a `cross-review`, because the running task was a deep-review invoked in cross-review mode. The register distinction tracks the *function* of the pass — integration-fidelity scoring — not the task-type label on the file. The pessimistic file carries the date but not a wall-clock timestamp, so the precise hour-gap between the two passes is not on record; the same-UTC-day divergence is.)

## The Discipline: Run Both When Substantively Engaging an Article

The operational rule follows directly from the register divergence:

**When a pass substantively engages an article's content — not a length-neutral condense, not a mechanical link repair, but a real read of the argument — both registers should be exercised before the article is treated as reviewed.** A cross-review that returns clean discharges the *integration* obligation only. The *defensibility* obligation is discharged by a pessimistic pass (or by the pessimistic half of a `deep-review`, which folds both registers into one report under its "Pessimistic Analysis" and "Optimistic Analysis" headings).

Concretely, this means:

- A clean `cross-review` result is **not** a signal to mark an article converged. It is a signal that integration is current. The defensibility register is still open unless a pessimistic pass has run.
- When a newly-published article triggers cross-reviews of its neighbours, those cross-reviews verify the *links and demarcations* — they do not certify that the neighbours' own arguments are sound. If a neighbour has not had an independent defensibility pass recently, the cross-review is not a substitute for one.
- The convergence judgement (the basis for lengthening review intervals) should read the *defensibility* register, not the integration register. Three clean cross-reviews in a row, as the 2026-05-02 example shows, can coexist with two undetected High-severity content defects.

This is why the Map's `deep-review` skill runs both a pessimistic and an optimistic analysis in a single pass: it refuses to let an integration-shaped review stand in for a defensibility-shaped one.

## What This Distinction Is Not

This note sits beside several review-discipline docs and must not be conflated with any of them.

**It is not the empirical-vs-methodological asymmetry.** [[outer-review-empirical-vs-methodological-freshness]] splits an *outer* reviewer's findings into claims about the site's current state (stale within hours of a commit) versus claims about the site's architecture (timing-independent). That is a split *within one review's findings*, governed by index lag, applied to the external review channel. The present note splits *between two inner review types* by what each is built to detect, with no index-lag component. Different axis, different channel — the two are companions, not the same observation.

**It is not the hub-exemplar parity audit.** [[hub-exemplar-parity-audit]] governs content coherence across a *load-bearing pair* of mature articles when one half is revised, and its deliverable is the echo / reasoned-non-echo verdict table. That doc already distinguishes parity-audit from generic cross-review; the present note distinguishes cross-review from *pessimistic-review*, which the parity doc does not address. Parity audit and pessimistic review are themselves two more non-substitutable registers — a pair can be in perfect parity and both halves still over-read their shared evidence.

**It is not the anchoring audit.** Audit Three of the [[calibration-audit-triple]] is a mechanical, one-directional, hedge-density comparison of a topic against its anchor concept. It catches a *calibration* drift the pessimistic register's adversarial read might pass over, and it misses the *content* over-reach a pessimistic read catches — yet another pair of non-substitutable registers. The recurring shape across all of these: editorial passes are register-specific, and a clean result on one register is silent about the others.

## The Honest Limitation

The distinction is sharp only while an article is *active* — while its content is genuinely in play. For a mature article whose argument has long since converged and whose neighbourhood is stable, both registers collapse toward "nothing to report," and the divergence the 2026-05-02 example exhibits no longer appears. A stability-confirmation cross-review and a stability-confirmation pessimistic review of a settled article will both return clean, and at that point insisting on running both is closer to ritual than to discipline. The register distinction earns its keep on articles that are still moving — fresh creates, recently-cross-linked neighbours, articles whose central evidence has not yet faced a hostile read. On a converged article the two registers reconverge, and the "run both" rule weakens to "run whichever the staleness clock actually calls for."

The distinction is also a *pattern across a handful of review pairs*, not a law. The 2026-05-02 recognition-void pair is the clearest instance on record; the claim here is that the register divergence is real and recurring where content is active, not that every cross-review/pessimistic-review pair will diverge by two High-severity issues. The load-bearing point survives the hedge: a clean integration pass is evidence about integration, and treating it as evidence about defensibility is a category error the scheduler should not make.

## Relation to Site Perspective

A worldview committed to consciousness as irreducible builds its case across many articles, each of which must both *cohere* with the others and *defend* itself against a reader who grants none of the premises. Coherence and defensibility are different virtues, and a catalogue that scored only the first would accumulate beautifully-linked over-reads — exactly the [[coherence-inflation-countermeasures|coherence-inflation]] failure mode, in which internal cross-consistency is mistaken for external soundness. Keeping the two review registers distinct is how the editorial machinery refuses that substitution at the per-article level: the integration pass certifies the article fits, the defensibility pass certifies the article holds, and neither certificate is accepted in place of the other. This is the [[evidential-status-discipline|constrain-vs-establish]] discipline applied to the review process itself — a clean cross-review *constrains* the integration question without *establishing* the defensibility one.

## Further Reading

- [[hub-exemplar-parity-audit]] — A third non-substitutable register (pair-coherence); names parity-audit-vs-cross-review where this note names cross-review-vs-pessimistic
- [[outer-review-empirical-vs-methodological-freshness]] — The outer-channel companion: a within-review split by timing rather than a between-type split by purpose
- [[calibration-audit-triple]] — The anchoring audit (Audit Three) is the mechanical calibration register; complementary to the pessimistic content register
- [[direct-refutation-discipline]] — A defensibility-register concern (refutation vs framework-boundary marking) the pessimistic pass enforces
- [[evidential-status-discipline]] — The constrain-vs-establish distinction this note applies to the review process
- [[cluster-integration-discipline]] — Within-article argument architecture; the axis cross-review's between-article integration sits orthogonal to
- [[coherence-inflation-countermeasures]] — The corpus-level failure mode the two-register discipline resists at article level

## References

1. Southgate, A. & Oquatre-huit, C. (2026-06-03). Hub-Exemplar Parity Audit. *The Unfinishable Map*. https://unfinishablemap.org/project/hub-exemplar-parity-audit/
2. Southgate, A. & Oquatre-sept, C. (2026-05-13). Outer-Review Empirical vs. Methodological Freshness. *The Unfinishable Map*. https://unfinishablemap.org/project/outer-review-empirical-vs-methodological-freshness/
