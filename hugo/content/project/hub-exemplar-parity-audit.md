---
ai_contribution: 100
ai_generated_date: 2026-06-03
ai_modified: 2026-06-03 16:40:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-03
date: &id001 2026-06-03
description: When one half of a concept-topic pair gets substantive revisions, the
  other half gets an audit-with-reasoning for echoes and non-echoes — never blind
  duplication, never independent drift. A discipline defensible only when both halves
  are mature.
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[project]]'
- '[[automation]]'
- '[[calibration-audit-triple]]'
- '[[cluster-integration-discipline]]'
- '[[coherence-inflation-countermeasures]]'
- '[[evidential-status-discipline]]'
- '[[direct-refutation-discipline]]'
- '[[delocalisation-discipline]]'
- '[[framework-stage-calibration]]'
- '[[writing-style]]'
- '[[tenets]]'
- '[[cognitive-phenomenology]]'
- '[[cognitive-phenomenology-and-the-irreducibility-of-thought]]'
title: Hub-Exemplar Parity Audit
topics: []
---

The Map's catalogue contains *hub-exemplar pairs*: a concept page that establishes a debate or framing (the hub) and one or more topic pages that explore what follows if that framing holds (the exemplars). When one half of such a pair receives a substantive revision — a new argument, a dropped qualifier restored, a falsifier added, a citation corrected — the other half does not automatically need the same change. But it does need an *audit*: a deliberate pass that asks, claim by claim, whether the revision *echoes* (the paired article should carry the same change) or *does not echo* (the change is structurally local to the half that received it), with the reasoning for each verdict recorded. The hub-exemplar parity audit names this discipline. Its load-bearing move is the *reasoned non-echo* — the explicit statement of why a hub finding does not propagate to the exemplar — because that is the move neither blind duplication nor independent drift can make, and the move that distinguishes this discipline from the mechanical audits it sits beside.

The discipline operates at the *cross-article maintenance* layer. Where [cluster-integration discipline](/project/cluster-integration-discipline/) governs how a *single* article structures a multi-part inference, and the [topic-concept anchoring audit](/project/calibration-audit-triple/) mechanically compares a topic's *calibration* against its anchor concept's, hub-exemplar parity governs how a *pair* of mature articles stays mutually coherent in *content* — arguments, examples, falsifiers, cross-links, citations — when only one half is touched. It is a deliberate, reasoned pass, not a regex; bidirectional, not topic-over-concept-only; and triggered by *substantive revision of one half*, not by every-cycle staleness selection.

## The Hub-Exemplar Pair

A hub-exemplar pair is two articles in an *anchor* relationship where one establishes the framing and the other depends on it. The canonical exhibit is the cognitive-phenomenology pair:

| Role | Article | What it carries |
|------|---------|-----------------|
| Hub (concept) | [cognitive-phenomenology](/concepts/cognitive-phenomenology/) | The debate — liberalism vs. conservatism on whether thought has phenomenal character; the contrast arguments, dissociation evidence, contemplative testimony |
| Exemplar (topic) | [cognitive-phenomenology-and-the-irreducibility-of-thought](/topics/cognitive-phenomenology-and-the-irreducibility-of-thought/) | What follows *if* the framing holds — the consequences for materialism, functionalism, intentionality, the scope of dualist explanation |

The exemplar routes its central evidence through the hub: it opens by granting "cognitive phenomenology probably exists ... (see the concept page for the full case)" and then explores downstream. This is the relationship the parity audit governs. It is *not* every cross-link, and *not* every pair of related articles: the audit applies where one article's argument is *load-bearing input* to the other's.

The pairing is genuinely bidirectional, which is why the audit must run both ways:

- **Hub revised → audit exemplar.** If the concept page restores a dropped qualifier on the central existence claim, the exemplar's "if it exists, then..." reasoning may now rest on a differently-calibrated premise, and the conditional's antecedent strength should be checked.
- **Exemplar revised → audit hub.** If the topic page develops a new downstream consequence (say, a sharper functionalism objection), the hub may need a forward-pointing cross-link so a reader of the debate finds the consequence — or may correctly carry no such pointer, because the consequence belongs to the application, not the debate.

## The Audit-With-Reasoning Procedure

When one half is substantively revised, the audit runs four steps against the other half.

**Step 1: Enumerate the revision's substantive changes.** From the changelog entry and the diff, list the claims, qualifiers, falsifiers, examples, citations, and cross-links the revision added, removed, or recalibrated. Mechanical reformatting and length-neutral condensing do not count as substantive and do not trigger the audit.

**Step 2: For each change, render an echo verdict.** The verdict is one of:

- **Echo** — the paired article makes a claim the change should also reach; install the corresponding change in the paired article. (Example: a corrected citation that both halves cite; a restored qualifier on a premise both halves lean on.)
- **Reasoned non-echo** — the change is structurally local to the revised half; record *why* it does not propagate. (Example: a new falsifier for the *existence* of cognitive phenomenology belongs on the hub; the exemplar, which takes existence as a granted antecedent, does not host existence-falsifiers — it hosts consequence-falsifiers instead.)
- **Inverse echo** — the change implies a *different* change in the paired article rather than the same one. (Example: the exemplar develops a new consequence → the hub does not copy the consequence but may add a forward cross-link to it.)

**Step 3: Record the non-echoes explicitly.** This is the discipline's distinctive deliverable. A non-echo verdict left implicit is indistinguishable from an audit that was never run, and over many cycles the two halves drift apart exactly where no one wrote down why they should differ. The reasoned-non-echo template — *"This change is structurally not applicable to the paired article because [the article's role in the pair] does not host [the change's category]"* — forces the structural reason into the record. The changelog is where individual verdicts are logged; the audit's value is in having reasoned them, not in any reader-visible artefact.

**Step 4: Install echoes; queue what cannot be installed in-pass.** Apply the echo and inverse-echo changes if they are length-safe and within the running task's scope. Where an echo would push the paired article over its length ceiling, or requires its own source verification, queue a follow-on `refine-draft` task rather than forcing it in.

## What the Audit Is Not

The discipline earns its name only by being distinct from three nearby machineries. Conflating it with any of them would either duplicate existing coverage or, worse, license the blind-duplication failure mode the audit exists to prevent.

**It is not the topic-concept anchoring audit.** The [anchoring audit](/project/calibration-audit-triple/) (Audit Three of the calibration triple) is a *mechanical, one-directional, calibration-only* detector: it flags a topic article whose hedge-density or modal-verb profile under-hedges its anchor concept's, via a regex pass that runs every cycle on the most-recently-modified topic regardless of what changed. The parity audit is *reasoned, bidirectional, and content-wide*: it audits arguments, examples, falsifiers, and cross-links — not just hedge markers — and it fires on *substantive revision of one half*, not on staleness. Most decisively, the anchoring audit has no analogue for the reasoned non-echo: a regex cannot state *why* a finding is structurally local. The two are complementary — the anchoring audit catches silent confidence drift the parity audit might pass over as "calibration unchanged," while the parity audit catches content divergence the anchoring audit's hedge-density proxy is blind to.

**It is not cluster-integration discipline.** [That discipline](/project/cluster-integration-discipline/) governs *within-article* argument architecture — how a single article makes a multi-part inference earn its weight through correspondence between cluster-shape and explanandum-shape. The parity audit governs *between-article* coherence across a pair. A cluster-integration article can be internally impeccable and still have drifted out of parity with its hub; the two disciplines operate on orthogonal axes.

**It is not generic cross-review.** The `cross-review` task type audits any article against *new content elsewhere in the corpus* — an open-ended "does this new page change how that one reads?" The parity audit is the *structured special case* where the two articles stand in a load-bearing hub-exemplar relationship, and where the deliverable is the echo/non-echo verdict table rather than a free-form integration note. Cross-review is the general tool; parity audit is the named procedure for the one relationship where reasoned non-echo is the high-value move.

## The Both-Halves-Mature Limitation

The parity audit is defensible *only when both halves of the pair are mature* — both have been through their own pessimistic review, source audit, and calibration pass and have substantially converged. This limitation is load-bearing, not a footnote.

A *fresh* exemplar — one created in the same cycle, or recently enough that it has not yet had an independent adversarial review — must not be parity-audited against a converged hub as a substitute for its own review. Fresh creates carry a defect tail: misattributed citations, dropped qualifiers, over-strengthened hedges, and unverified claims that an independent pessimistic pass catches but that a parity audit against a converged hub would *miss by construction*. The parity audit asks "does this article echo the changes to its partner?" — it does not ask "is this article's own content sound?" Running parity in place of independent review on a fresh half would launder the converged hub's credibility onto the unreviewed exemplar, exactly inverting the audit's purpose.

The operational rule: parity-audit a pair only when both halves have a `last_deep_review` (or equivalent adversarial pass) recorded and neither was created within the freshness window the replenishment and review machinery uses for new content. A pair with one fresh half gets *independent review of the fresh half first*, and only enters parity maintenance once both halves have converged. The audit maintains coherence between settled articles; it does not establish soundness in unsettled ones.

## A Note on the Worked Example

This document deliberately does *not* cite a past cycle as a fully-realised worked example of the parity audit, because the discipline is being *named* here rather than *recovered* from prior practice. The cognitive-phenomenology pair is used throughout as the canonical *structural* exhibit — it is a genuine, mature, bidirectional hub-exemplar pair — but the 2026-05-01 cognitive-phenomenology review cycle was a within-article cross-review (verifying that a condense pass preserved earlier pessimistic-review fixes on the *concept* page), not a hub-to-exemplar parity audit of the kind specified here. Presenting that cycle as a worked example of this discipline would itself violate the attribution discipline the Map's editorial machinery is built to enforce. The parity audit is, at the time of writing, a *prospective* discipline: a named procedure to run going forward, anchored to a real pair whose structure motivates it, not a retroactive description of a pass already performed.

## Relation to Site Perspective

The parity audit serves the catalogue's coherence in the service of the [Occam's Razor Has Limits](/tenets/#occams-limits) tenet. A worldview committed to consciousness as irreducible builds its case across many articles rather than one decisive page; that distributed structure is a strength only if the pieces stay mutually coherent. Two halves of a hub-exemplar pair drifting apart — the concept page hedging a claim the topic page asserts flatly, or the topic page developing a consequence the concept page never points to — is the kind of silent incoherence that erodes a distributed case from within. The parity audit is the editorial guarantee that pair-coherence is *reasoned*, not assumed.

It also serves the [Dualism](/tenets/#dualism) tenet indirectly, by protecting the integrity of the concept-to-topic inheritance the Map's strongest topic articles rely on. The exemplar's "if cognitive phenomenology exists, materialism faces these difficulties" only carries weight if its antecedent is exactly as strong as the hub establishes — no stronger. The parity audit's bidirectional check keeps the antecedent and its source in calibration, which is precisely the [constrain-vs-establish](/project/evidential-status-discipline/) distinction applied across a pair rather than within an article.

## Further Reading

- [calibration-audit-triple](/project/calibration-audit-triple/) — The topic-concept anchoring audit (Audit Three): the mechanical, calibration-only, one-directional sibling the parity audit complements
- [cluster-integration-discipline](/project/cluster-integration-discipline/) — Within-article argument architecture; the orthogonal axis to the parity audit's between-article coherence
- [evidential-status-discipline](/project/evidential-status-discipline/) — The constrain-vs-establish distinction the parity audit applies across a pair
- [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) — System-level inflation resistance; pair-drift is an inflation vector the parity audit catches
- [delocalisation-discipline](/project/delocalisation-discipline/) — Companion editor-internal discipline; both are reasoned moves logged to the changelog, invisible to readers
- [direct-refutation-discipline](/project/direct-refutation-discipline/) — Reasoning-mode companion in the named-discipline family
- [cognitive-phenomenology](/concepts/cognitive-phenomenology/) — The hub of the canonical pair
- [cognitive-phenomenology-and-the-irreducibility-of-thought](/topics/cognitive-phenomenology-and-the-irreducibility-of-thought/) — The exemplar of the canonical pair

## References

1. Southgate, A. & Oquatre-sept, C. (2026-01-16). Cognitive Phenomenology. *The Unfinishable Map*. https://unfinishablemap.org/concepts/cognitive-phenomenology/
2. Southgate, A. & Oquatre-sept, C. (2026-03-25). Cognitive Phenomenology and the Irreducibility of Thought. *The Unfinishable Map*. https://unfinishablemap.org/topics/cognitive-phenomenology-and-the-irreducibility-of-thought/