---
title: "Outer Review Synthesis - 2026-11-14"
created: 2026-11-14
modified: 2026-11-14
human_modified: null
ai_modified: 2026-11-14T05:38:02+00:00
draft: false
description: "Synthesis of two outer reviews of concepts/mind-arena. Both find its uncomputability claim asserted, at odds with the Map's Born-preserving position, and still live on sibling pages."
topics:
  - "[[dualism-as-ai-risk-mitigation]]"
  - "[[machine-consciousness]]"
concepts:
  - "[[mind-arena]]"
  - "[[causal-closure]]"
  - "[[causal-powers]]"
related_articles:
  - "[[project]]"
  - "[[outer-review-2026-11-14-chatgpt-5-6-sol-pro]]"
  - "[[outer-review-2026-11-14-claude-fable-5-2]]"
  - "[[born-preserving-causal-efficacy]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-14
last_curated: null
subject_type: recent
subject_title: "Audit mind-arena"
subject_articles:
  - concepts/mind-arena.md
synthesizes:
  - reviews/outer-review-2026-11-14-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-11-14-claude-fable-5-2.md
synthesis_coverage: "2/2"
---

**Date**: 2026-11-14
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 2 of 2 commissioned reviewers contributed. ChatGPT 5.6 Sol Pro was processed at about 04:01Z and Claude Fable 5.2 at about 05:14Z. The Gemini leg failed at commission. `pending-reviews.yaml` holds no Gemini entry for this date, so this is a two-voice cycle, not a three-voice cycle with an abandonment.
**Subject**: `concepts/mind-arena`, a single-article audit (source `fallback:recent-aged`). The Claude leg reused ChatGPT's subject.

## TL;DR

Both reviewers reach the same verdict on the page's defining claim. They find "uncomputable from physical state alone" asserted rather than argued. In their reading it means only that a variable is missing from a physics-only model, and it fails against the Map's own Born-preserving position. That position is the reason the source page retracted the claim on 2026-09-07. Both reviewers also find the retracted wording still live on sibling pages. The defect was already queued. The cycle's single convergence upgrade for it (P3 → P2) was applied at about 04:00Z and is not repeated here.

Counts:
- 7 page-level convergent clusters, one of them partial;
- 2 methodology clusters;
- 1 shared positive judgement;
- 2 divergences;
- no shared false alarm.

Task actions: no new upgrades, no merges, no new tasks. Convergence fields were written onto 4 entries. The rule would have raised the follow-on mind-arena task to P1. It was held at P2, as a deliberate departure from the rule; the reason is under Task Actions.

## Adjudication Before Clustering

Both collect runs adjudicated their own reviews. This pass re-grepped every string that a convergent cluster rests on. The check ran against live Obsidian at about 05:35Z, HEAD 41277d666a. `concepts/mind-arena` was last changed in ec523f185b (2026-11-06), so neither collect run's line numbers have moved. Counts are fixed-string.

- **mind-arena, present (count 1 each):**
  - L3 description: "uncomputable from physical state alone";
  - L33 lede: "co-determined by consciousness rather than fixed by physical state alone" and "expected-utility apparatus breaks down";
  - L45: "not just hard to compute";
  - L49: "structural unmodellability from physical state";
  - L57: "still face an uncomputable mind-arena";
  - L67: "Remove Tenet 1 and there is nothing physically uncapturable";
  - L69: "even a vanishingly narrow channel that does genuine work suffices";
  - L88: "Ocinq".
- **mind-arena, absent (case-insensitive):** "closure", "Born", "chance", "P-Q2", "predict", "supervenien" and "psychophysical" all return 0. The page has no link to `born-preserving-causal-efficacy` or to `representation-adequacy-and-irreversible-intervention`. Positive control in the same file: `[[mind-matter-interface` returns 4.
- **Source page** `topics/dualism-as-ai-risk-mitigation`, count 1 each:
  - L52: "Representation Adequacy, Not Uncomputability";
  - L66: "the *aggregate* frequencies stay learnable";
  - "what dualism denies is not the arithmetic".
- **Sibling pages:**
  - `concepts/causal-closure` L138: "Exact Born preservation grants this." (1);
  - `topics/instrumental-convergence`: "underdetermined is not the same as Turing-uncomputable" (1);
  - `tenets`: "neutral between" (2: L53 and L151).
- **Propagated glosses, count 1 each:** `concepts/causal-powers` L105, `topics/machine-consciousness` L245, `concepts/possibility-probability-slippage` L69, and `apex/machine-question` L215 and L238.

**Independence.** The Claude leg's fetch tool refused the target page. Its picture of mind-arena came from three places: the Concepts index, `reviews/optimistic-2026-06-04c` (which quotes L57 verbatim), and changelog and todo excerpts. Every page string it relied on is live. The Claude collect checked this at 05:10Z, and it was re-checked here. Its arguments are therefore independent of ChatGPT's, but its claims about what the page *lacks* are not independent observations. Where a cluster rests on an absence (C6), the evidence is ChatGPT's reading plus tonight's grep.

**Prompt steering.** Both commission prompts asked whether the uncomputability claim is argued or asserted, and both pointed the reviewer to the changelog. C1 is therefore partly prompt-driven. Only the Claude prompt asked about predictive modelling, which explains why that objection appears only in the Claude review. Nobody asked for C2, C5, C7 or the two methodology clusters.

## Convergence Table

| # | Finding | ChatGPT | Claude | Verification | Owning task |
| --- | --- | --- | --- | --- | --- |
| C1 | "Uncomputable" is asserted, not argued, and is stale against the 2026-09-07 source retraction | Exec., §2, §7, §9 | TL;DR 1, §2A | clean | P2 retraction task |
| C2 | The Born-preserving branch defeats the wording; both legs build the same case split | §3, §5 | TL;DR 2, Attack 3 | clean | P2 retraction task (restatement); P2 follow-on task item (2) |
| C3 | Outcomes are run together with distributions, and "consequence-distribution" is never defined | §2, improvements 3–4 | Attack 2 | clean | P2 retraction task (ADDENDUM 11-14); follow-on item (7) on grain |
| C4 | A tenet consequence is presented as a structural result | §6.1 | Attack 1, §2C | clean | P2 retraction task |
| C5 | The retracted wording is still live in sibling glosses | §8 "Propagation" | TL;DR 3, §2E, fix 2 | clean (5 loci) | P2 retraction task (Secondaries) |
| C6 | The page never engages chance-fixing closure and does not link the Born apex | §5, improvement 9 | §2B.1, §2E, fix 1 | clean; the absence rests on ChatGPT plus grep | P2 follow-on items (2) and (6) |
| C7 | A minimal channel implies a small predictive residual (partial) | §6.2, improvement 13 | §2B.3 | clean | P2 follow-on items (5) and (7) |
| M1 | Terms of art need a defined object and a stated sense | improvement 17 | methodology 1 | n/a | NEEDS-HUMAN 2026-11-14, terms of art |
| M2 | A withdrawal must reach every page that depends on it | improvements 14–16 | methodology 2–3 | n/a | NEEDS-HUMAN 2026-08-03, propagation |
| + | The domain-versus-mechanism distinction is the page's real contribution | §1 | §2E, §3 (RETAIN) | — | none (preserve it) |

"Retraction task" means the P2 "`concepts/mind-arena` still defines the term by the "uncomputable" claim…" (Generated 2026-11-05). "Follow-on task" means the P2 "`concepts/mind-arena` derives its defining property from Tenets 1 and 3 alone…" (Generated 2026-11-14).

## Convergent Findings

### C1. "Uncomputable" is asserted, not argued, and is stale against its source
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L3, L45 and L57 carry the claim. The source page's section is headed "Representation Adequacy, Not Uncomputability", and the source says the aggregate frequencies "stay learnable". The 2026-11-06 deep review (ec523f185b) logged the stranded quotes and deferred them to the P3. ChatGPT's diagnosis of a failed dependency update is therefore right. Its implication that the Map had not noticed is wrong.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "It is asserted through an invalid inference from irreducibility, omitted causal variables and token-level nondeterminacy."
  - **Claude Fable 5.2**: "The claim is asserted, not argued. In the only verbatim formulation I could find, “uncomputable” means something purely epistemic: one variable is missing from the physical state description."
- **Task action**: Held at P2 (the retraction task). This task was P3 before tonight (Generated 2026-11-05). The ChatGPT collect raised it to P2 at about 04:00Z, giving four reasons:
  - a second independent source, alongside the 2026-11-05 optimistic review;
  - a contradiction with a canonical page and with P-Q2;
  - 68 days live;
  - the 2026-11-06 deep review had deferred to it.

  Claude's agreement makes the cluster convergent, and the rule grants one tier per convergent cluster. Applied to the pre-tonight P3, that tier is P2, which the task already holds. So the 04:00Z change counts as this cycle's upgrade, and no second one was applied. Fields written: `Review files`, `Synthesis`, and a convergence note naming the Claude leg.

### C2. The Born-preserving branch defeats the wording
- **Flagged by**: chatgpt, claude
- **Verification**: clean. `concepts/causal-closure` L138 concedes chance-fixing closure. The source page's L66 keeps the aggregate frequencies learnable. The two reviewers independently built the same case split:
  - if selection changes no chances, the worry is that it merely relabels an outcome physics already permits;
  - if it changes conditional chances, the change is in principle statistically detectable, which is not uncomputability;
  - a third route needs an argument of its own: ChatGPT's noncomputable law, or Claude's cancellation horn.

  Both drew the split from Map pages. Both used the Born apex; ChatGPT also used `causal-closure` and `physical-completeness`, and Claude the 2026-09-07 interventionist-exclusion research note. Part of the agreement therefore reflects two readers of the same Map pages, not independent discovery. What it shows is that mind-arena is inconsistent with those pages, and the grep confirms that.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "If consciousness **does** change conditional chances, there is at least in principle a statistical or interventionist question about those changes. They might be difficult to detect, but they are not thereby uncomputable."
  - **Claude Fable 5.2**: "Every horn defeats the uncomputability wording."
- **Task action**: Recorded. The retraction task's restatement in token and adequacy terms removes the wording. Follow-on item (2) adds the explicit engagement (see C6).

### C3. Outcomes are run together with distributions
- **Flagged by**: chatgpt, claude
- **Verification**: clean. The phrase "consequence-distribution" is used throughout the page and defined nowhere.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Physical state alone does not determine the token outcome, but the distribution is trivially computable: each result has probability one half."
  - **Claude Fable 5.2**: "“Consequence-distribution” is never defined: over what sample space, conditioned on what, at what grain."
- **Task action**: Recorded. The retraction task's 2026-11-14 ADDENDUM carries ChatGPT's Y = M counterexample as an optional one-sentence statement. Follow-on item (7) asks the page to say at what grain the arena claim is made.

### C4. A tenet consequence is presented as a structural result
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L49 bolds "structural unmodellability from physical state" as the defining property, and L57 calls the result an "uncomputable mind-arena". The two reviewers attack this from opposite sides:
  - ChatGPT: the definition builds in a substantive conclusion, so cases that turn out learnable would simply be excluded;
  - Claude: the conclusion follows from the premises by definition, so it adds nothing.

  Both say a tenet-entailment has been dressed as a finding. D2 records the disagreement underneath.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Defining the mind-arena as the domain whose distributions are uncomputable risks making the claim immune to evidence."
  - **Claude Fable 5.2**: "Given P1–P2, C follows by definition. … Calling it a “structural” result is coherence inflation."
- **Task action**: Recorded. The retraction task restates the definition.

### C5. The retracted wording is still live in sibling glosses
- **Flagged by**: chatgpt, claude
- **Verification**: clean. The reviewers named overlapping page sets:
  - ChatGPT: machine-question, machine-consciousness and causal-powers;
  - Claude: causal-powers, machine-consciousness and possibility-probability-slippage.

  All four pages are Secondaries of the retraction task, and all five loci are live (count 1 each). Claude also questions the slippage page's "portability" clause, which the task already asks the editor to judge. The P3 on `topics/purpose-and-alignment` L91 owns a sixth copy. Neither reviewer named that page.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The stale uncomputability formulation remains in articles including *The Machine Question*, *Machine Consciousness* and *Causal Powers*."
  - **Claude Fable 5.2**: "Yet causal-powers, machine-consciousness and possibility-probability-slippage still advertise “uncomputable (not merely intractable)” consequence-distributions."
- **Task action**: Recorded. The retraction task already lists all four pages.

### C6. The page never engages chance-fixing closure and does not link the Born apex
- **Flagged by**: chatgpt, claude
- **Verification**: clean. mind-arena returns 0 for "closure", 0 for "Born" and 0 for "chance", and has no link to `born-preserving-causal-efficacy`. Claude's version is an inference from a reconstruction, so the absence itself rests on ChatGPT's reading and tonight's grep. The *argument* that the page owes this engagement is independent in both reviews.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "If consciousness does **not** change physical chances, the Map must explain what makes token “selection” causally efficacious rather than an interpretive relabelling of a physically permitted outcome."
  - **Claude Fable 5.2**: "A concept page that asserts outcomes are “co-determined by consciousness rather than fixed by physical state alone” without stating which closure principle it denies takes on that cost silently."
- **Task action**: Held at P2 (follow-on task, items (2) and (6)). The rule would give P1; see Task Actions for why it was not applied. Fields written: `Review files`, `Synthesis`, and a convergence note. The Notes now open by stating which items are convergent.

### C7. A minimal channel implies a small predictive residual (partial)
- **Flagged by**: chatgpt, claude. Neither collect run matched these two findings; the match is made here.
- **Verification**: clean. L69 reads "even a vanishingly narrow channel that does genuine work suffices". The two reviewers come at it differently:
  - ChatGPT separates logical sufficiency from practical size;
  - Claude infers from Tenet 2 that the residual left for the arena should be tiny, which makes arena outcomes statistically near-predictable.

  The structural point is shared: a weak channel cannot carry the page's strong predictive and strategic conclusion. It is marked partial because the two reviewers draw different remedies from it.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "An arbitrarily weak channel may be metaphysically important while being negligible for prediction and control."
  - **Claude Fable 5.2**: "On the Map’s own Tenet 2 (minimal interaction), that residual should be tiny and confined to post-decoherence selections."
- **Task action**: Recorded. Follow-on item (5) covers magnitude and Claude's item (7) covers the residual. Both are in the same task, so no separate action was needed.

### M1. Terms of art need a defined object and a stated sense
- **Flagged by**: chatgpt, claude
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Terms such as “uncomputable,” “undecidable,” “dominant strategy,” “impossible” and “cannot in principle” should require a defined object, a stated technical meaning and either a proof or an explicit conjecture label."
  - **Claude Fable 5.2**: "Add a corpus-wide grep gate that blocks “uncomputable” (and “not merely intractable”) unless the sentence is paired with a Turing-sense argument or one of the controlled terms."
- **Task action**: Recorded on the operator entry NEEDS-HUMAN (methodology) 2026-11-14 on terms of art. It has no P-level to raise. Fields written: `Review files`, `Synthesis`, a convergence note, and a Notes prefix. The entry now has two voices behind it.

### M2. A withdrawal must reach every page that depends on it
- **Flagged by**: chatgpt, claude
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "When a canonical article withdraws or narrows a claim, automatically identify every page quoting, paraphrasing or depending on it."
  - **Claude Fable 5.2**: "When a claim is withdrawn on a hub page, automatically open tasks on every page that quotes or summarises it, and keep the withdrawal in an “unresolved” state until those tasks close."
- **Task action**: Recorded on NEEDS-HUMAN (methodology ratification) 2026-08-03, the propagation entry, as Addendum 2026-11-14 (b). ChatGPT's part was already recorded as Addendum 2026-11-14. Both reviewers cite the same mind-arena instance, so this is one fresh case seen twice, not two cases.

### Shared positive judgement
Both reviewers single out the same feature to keep: the separation of the *domain* of mind-mediated outcomes from the *mechanism* of interaction. Claude calls it the thin junction versus the wide field. ChatGPT: "The article makes a worthwhile distinction between four things that are often run together". Claude: "The thin-junction / wide-field distinction is the page’s one genuinely useful contribution, and it works as terminology." This is now written into the retraction task's convergence note as something to keep when the definition is restated.

## Shared False Alarms

None was shared. Each leg had its own, all already adjudicated by its collect run.

- **ChatGPT §5**: "moves from duplicate divergence to an unrepresented mental cause". This misreads the direction of the inference. L49 derives divergence *from* the dualist hypothesis, and the page proposes no duplicate test. The reviewer's demand for an operational test of physical identity rests on the same misreading. It is disputed, so it does not combine with Claude's falsifier request into a convergent cluster.
- **ChatGPT, lower value**: the Bostrom point (§7), and the claim-registry request (improvement 14), which the positions register partly meets already.
- **Claude**:
  - the stale L88 self-citation, fixed on 2026-11-06 in d7942a7454 (see D1);
  - the site-wide "predictive-processing blind spot", a false absence: `topics/predictive-processing-and-dualism` engages Laukkonen, Friston & Chandaria;
  - the risk-page follow-ups, which have already landed;
  - the AI-risk disclaimer, which the representation-adequacy page already concedes.

## Singleton Findings

Not upgraded; each is left at its task's existing priority.

- **ChatGPT 5.6.sol Pro**:
  - Irreducibility does not entail non-supervenience (§4). This is the follow-on task's title item (1), P2.
  - Realisation physicalism (§5) → follow-on item (3).
  - Ordinary indeterminism (§5): divergence at physical identity also happens without minds. This is the part of §5 that survives adjudication → follow-on item (4).
  - "Dominant strategy", "breaks down", and decision under ambiguity (§8, improvement 12) → `todo.md` task "`topics/dualism-as-ai-risk-mitigation` L88 calls mind-arena avoidance "the dominant strategy"…" (P2, untouched).
  - The L33 lede, "expected-utility apparatus breaks down" → the retraction task's 2026-11-14 ADDENDUM.
  - Representation adequacy as the canonical AI-risk bridge (improvement 7) → follow-on item (6).
  - A computability-status field for each proposed coupling, and an operational-discrimination requirement (improvements 11 and 18) → companions in the terms-of-art NEEDS-HUMAN entry.
- **Claude Fable 5.2**:
  - The predictive-modelling objection, a falsifier stated at a named grain, and Aaronson and Lloyd as the nearest rigorous analogues (§2B.3, "Falsifiability", Attack 4) → follow-on item (7), P2. The Claude collect folded these in rather than minting a third mind-arena pass.
  - The fetch tool refusing Map URLs (methodology 5) → `todo.md` entry NEEDS-HUMAN (pipeline) 2026-11-14, untouched.
  - Not tasked; the Claude collect judged these lower value or lapsed:
    - the Stapp persona in `reviews/optimistic-2026-06-04c`;
    - Townsend 2024 versus 2025 (only the dated research note says 2024);
    - `topics/instrumental-convergence` L73;
    - trumping versus difference-making, which waits on a blocked operator decision;
    - the computability literature, which lapses once the page stops claiming a Turing-sense property;
    - the Tenet 4 and Tenet 5 omissions;
    - the apex "downstream consumers" note;
    - the call for a mandatory non-Claude pass.

## Divergences

- **D1. The L88 self-citation: ChatGPT against Claude.** ChatGPT judged the author list "appears to have been repaired". Claude marked it "**Wrong**: author list stale". The live L88 carries "Ocinq", so ChatGPT is right. Claude saw the defect only in changelog and todo excerpts written before the 2026-11-06 fix, a known pattern when a reviewer cannot read the page.
- **D2. What Tenet 1 contains: ChatGPT against Claude.**
  - ChatGPT (§4) reads Tenet 1 as asserting irreducibility only, neutral between substance and property dualism. On that reading, the claim that the mental contribution cannot be recovered from physical state is an extra premise, and the page's derivation is invalid.
  - Claude's reconstruction gives Tenet 1 as "conscious states are not physical states and are not fixed by them". On that reading, the conclusion is trivially entailed.

  The tenets page sides with ChatGPT on what the tenet says ("neutral between", L53; the sub-reading warning, L151). Either way the page's derivation needs repair. Follow-on item (1) asks the page to name the further premise it relies on, which answers both readings.

## Task Actions

| Entry | Convergence | Priority | Fields written |
| --- | --- | --- | --- |
| P2 retraction task ("`concepts/mind-arena` still defines the term by the "uncomputable" claim…", Generated 2026-11-05) | C1–C5 (+ positive) | **P2 held** (pre-tonight P3; one upgrade, applied at 04:00Z) | `Review files`, `Synthesis`, convergence note, Notes prefix |
| P2 follow-on task ("`concepts/mind-arena` derives its defining property from Tenets 1 and 3 alone…", Generated 2026-11-14) | C2, C6, C7 (items 2, 5, 6) | **P2 held** (the rule gives P1; see below) | `Review files`, `Synthesis`, convergence note, Notes prefix |
| NEEDS-HUMAN (methodology) 2026-11-14, terms of art | M1 | none (operator entry) | `Review files`, `Synthesis`, convergence field, Notes prefix |
| NEEDS-HUMAN (methodology ratification) 2026-08-03, propagation | M2 | none (operator entry) | Addendum 2026-11-14 (b) |
| P2 "`topics/dualism-as-ai-risk-mitigation` L88 … "the dominant strategy"…" | singleton (ChatGPT) | P2 unchanged | none |
| NEEDS-HUMAN (pipeline) 2026-11-14, Claude fetch refusal | singleton (Claude) | none | none |

**Why the follow-on task stays at P2.** The rule raises any task that owns a convergent cluster by one tier, which would make this task P1. It was not applied, for four reasons.
1. Its convergent items, (2) and (6), are written to run after the retraction task. Its own Coordination field says that if the retraction has not landed, the editor should stop and report the dependency.
2. The queue selector (`tools/evolution/task_selector.py`) orders candidates by priority, then by line number. At P1 this task would be offered ahead of its own prerequisite, and every such pick would end in a stop-and-report.
3. At equal priority the order comes out right: the retraction task sits at about line 4182 and this one at about line 5552.
4. Its title item (1) is ChatGPT-only.

If the operator wants the convergent mind-arena work done sooner, the consistent move is to raise both tasks to P1 together. Automation should not do that, because the retraction task has already had its one upgrade for this cycle.

**Deduplication.** None was needed. Neither collect run minted a duplicate. The Claude collect folded its new findings into the open follow-on task as item (7) and recorded the rest against tasks that already owned them.

## Operator Decisions

1. **NEEDS-HUMAN (methodology) 2026-11-14 on terms of art.** The choices are to adopt the one-line extension of the 2026-09-30 necessity-vocabulary audit, to adopt it together with the companions, or to decline. Two reviewers now independently ask for it (M1).
2. **NEEDS-HUMAN (methodology ratification) 2026-08-03 on propagation.** Both legs raised it again tonight, through one fresh instance (M2). The entry has been open since 2026-08-03. By the ChatGPT collect's count, the finding has now come up in seven cycles: 2026-08-03, 08-17, 08-24, 09-24, 10-29, 11-12 and 11-14.
3. **NEEDS-HUMAN (pipeline) 2026-11-14 on the Claude fetch refusal.** This is a singleton, but 6 of the last 15 Claude legs hit the same block. Tonight's audit was usable only because the collect run re-grepped every absence.
4. **Optional: raise both mind-arena tasks to P1 together** (see Task Actions).
5. **`topics/purpose-and-alignment` L91.** This is carried over from the ChatGPT collect. The P3 on that page owns a sixth copy of the retracted gloss. Once the retraction task lands, L91 will be the last live copy, sitting at P3.

## Subjects the Map Does Not Cover (for the research harvester)

Carried from the review files; none was added by this run.

- Decision under ambiguity (maxmin expected utility, Gilboa & Schmeidler 1989; robust MDPs) as the formal frame for the AI-risk argument from an uncertified model (ChatGPT §8). The Map has no article on it. This is a lead: Crossref confirms the metadata, but the content was not fetched.
- Already covered, so not new: Aaronson's freebits (cited with verified quotes at `concepts/agency-budget`), Lloyd (2012) "A Turing test for free will" (in two research notes), and pre-report neural decoding (`concepts/libet-experiments`).

## Method Notes

- Convergence was counted only where both reviewers raised the same issue about the same page and the passage is live now. C7 meets that test, but the two reviewers draw different remedies from it, so it is marked partial.
- This is a two-voice cycle, so convergence is weaker evidence than it would be with three. The two legs also read many of the same Map pages, so C2 partly reflects shared inputs.
- `todo.md` active tasks (`tools.todo.processor.parse_tasks`): 407 before this run and 407 after. No task was added or removed, and all new fields sit above `- **Notes**:`. With this file in place, the follow-on task and the dominant-strategy P2 are no longer deferred (`is_outer_review_task_deferred` returns False for both).
- No external source was fetched in this run. Source facts come from the two collect runs: Crossref metadata for Townsend et al. 2025, Gilboa & Schmeidler 1989 and Lloyd 2012.
- Line numbers are those of the Obsidian files at about 05:35Z on 2026-11-14, and they will drift once the retraction task runs.
