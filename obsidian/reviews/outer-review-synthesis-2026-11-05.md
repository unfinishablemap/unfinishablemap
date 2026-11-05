---
title: "Outer Review Synthesis - 2026-11-05"
created: 2026-11-05
modified: 2026-11-05
human_modified: null
ai_modified: 2026-11-05T05:35:11+00:00
draft: false
description: "Synthesis of 3 outer reviews from the 2026-11-05 full-site audit: four two-reviewer content clusters (one upgraded P2→P1, three on human decisions), three methodology recurrences, seven rejected convergences, no duplicates."
topics:
  - "[[perceptual-failure-and-the-interface]]"
  - "[[multi-agent-born-preservation-problem]]"
concepts:
  - "[[substrate-independence]]"
  - "[[working-memory]]"
  - "[[selection-only-channel]]"
related_articles:
  - "[[project]]"
  - "[[outer-review-2026-11-05-chatgpt-5-6-sol-pro]]"
  - "[[outer-review-2026-11-05-claude-fable-5-1]]"
  - "[[outer-review-2026-11-05-gemini-3-1-pro]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-05
last_curated: null
synthesizes:
  - reviews/outer-review-2026-11-05-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-11-05-claude-fable-5-1.md
  - reviews/outer-review-2026-11-05-gemini-3-1-pro.md
synthesis_coverage: "3/3"
---

**Date**: 2026-11-05
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 3 of 3 commissioned reviewers contributed, and none was abandoned. The legs were ChatGPT 5.6 Sol Pro (processed 04:38Z; 7 tasks plus 1 NEEDS-HUMAN), Claude Fable 5.1 with Research (processed 05:04Z; 5 tasks plus 1 NEEDS-HUMAN, plus one convergence note on a ChatGPT task) and Gemini 3.1 Pro with Deep Research (processed 05:19Z; 4 tasks). The subject was the site-stale-7d fallback `Full-site audit`. Claude and Gemini reused ChatGPT's subject, but each service ran its own prompt. Gemini's prompt asked a hostile journal referee for five weaknesses, each with a 2020–2025 source, and barred methodology commentary. Every live locus below was re-checked with `grep -c -F` against `obsidian/` between 05:21Z and 05:35Z.

## TL;DR

The only two-reviewer finding that lands on one live sentence with an open task is the production strawman in `topics/perceptual-failure-and-the-interface`. L114 says that if the brain generates consciousness, «less brain activity should always mean less consciousness», and L108 says emergence predicts the anaesthetic components «should grade together». ChatGPT reached it from the source side (Sarasso 2015 and Siegel 2024 are "non-discriminating"). Claude reached it from an archived predecessor whose sentence is L108's direct ancestor. The same L114 fix was asked for on 2026-06-11 and did not land. That task goes P2 → P1. The other three content clusters converge on standing human decisions: the P-Q2 Born-preservation quantifier, the Tenet 3 quantifier as it bears on AI verdicts, and P-Q1's credence band. The loop cannot act on any of the three, so they get notes, not upgrades.

Cluster count: 0 three-reviewer clusters, 4 two-reviewer content clusters (C1–C4), 3 two-reviewer methodology recurrences (M1–M3), 7 rejected convergences (R1–R7), 14 singleton tasks (counting the R1 working-memory task) plus 2 singleton NEEDS-HUMAN entries, and 2 divergences. Task actions: 1 upgrade (P2 → P1), 0 deduplications, 0 deletions, 2 combine notes on open tasks with no priority change, 3 convergence notes on human-decision entries. `parse_tasks` active count: 353 before, 353 after.

## Adjudication Before Clustering

Each leg was tested before it was allowed to count. A leg counts only if it points at a real defect that grep confirms on the live page. A leg that rests on an archived page, a stale index read or a misattributed URL counts only if the same defect is independently live.

- **Gemini misattributes sibling text to the page it names.** Three of its five URLs do not hold the text it quotes. The bandwidth quotes live at `concepts/working-memory` L127, not on `topics/bandwidth-of-consciousness`. The Cogitate material belongs to `topics/experimental-consciousness-science-2025-2026` L50 and `concepts/global-workspace-theory` L84, not to the unfolding-argument page. Each Gemini leg below is therefore placed at its true locus.
- **Two Gemini weaknesses fail against the live text or the source.** Weakness 1 says the DP page suppresses Donadi et al. 2021. In fact the page's lead says the parameter-free version "was falsified in 2021", and that sentence has been live since commit 099eb9b457 (2026-07-31). The section "The Diósi-Penrose Model and Its Partial Falsification" has been there since the page was created on 2026-03-15. So the charge is a misreading, not a stale index. Weakness 5 says Zheng & Meister measured only motor output. That is false: in the blindfolded-speedcubing passage of arXiv 2408.10234v2, the perception phase runs near 11.8 bits/s with no motor readout.
- **Claude quoted search-index renderings.** By its own statement, only the changelog and homepage were fetched live. The processor found seven of its claims already fixed and three of its quoted pages archived: `topics/perceptual-degradation-and-the-interface`, `topics/quantum-measurement-consciousness-interface` and `concepts/protention`. Three of its absence claims are false. The Tenet 4 apex exists as `apex/one-world-wager`, Laukkonen, Friston & Chandaria 2025 is cited on `concepts/predictive-processing` and `topics/predictive-processing-and-dualism`, and Georgiev is cited on 10+ pages. Claude's legs below count only where the defect is live on today's text.
- **ChatGPT rarely gives line-level loci.** It read the live site, and its Map-side descriptions mostly verify. But it names pages, not sentences, and the perceptual-failure locus was found by the processing driver's corpus grep. Its legs count where its stated verdict, applied to the live sentence, identifies the defect.

## Convergence Table

| ID | Finding | ChatGPT | Claude | Gemini | Verified live | Task action |
|---|---|---|---|---|---|---|
| C1 | Production strawman, perceptual-failure L108/L114 | §7.8–7.9 | Part 2 §4, §5 row 4, Part 4 item 12 (archived predecessor) | — | Yes, both strings count 1 | P2 → P1 |
| C2 | P-Q2 quantifier versus public-conditioned tests | §5 Tenet 2, §6 row 3, items 3, 11 | Part 2 §2 item 1, §3, Part 4 item 5 | — | Yes ("publicly conditionable" live in P-Q2 and selection-only-channel) | Note on P1 HUMAN DECISION (already P1, blocked) |
| C3 | Tenet 3 quantifier: AI verdicts read universal efficacy inconsistently | §3.5, §5 Tenet 3, §6 row 5, item 4 | Part 4 item 2 (substrate-independence L126) | — | Yes (L126 versus L128/L130) | Note on NEEDS-HUMAN; combine note on the substrate-independence P2, no upgrade |
| C4 | P-Q1 credence held moderate on specifiability | §4.4 | Part 2 §6, Part 3, Part 4 item 5 | — | Yes (P-Q1 L54/L60 band rationale) | No task owns it; recorded on the P-Q2 entry |
| M1 | Corrections and grades do not propagate to satellites | §4.3, §4.5, items 19, 20, 26 | Part 2 §4, Part 5 | — | Four live instances this cycle | Addendum on methodology NEEDS-HUMAN |
| M2 | Same-family review is not independent | item 25 | Part 5 bullets 1 and 4 | — | n/a (process) | Recorded for tune-system |
| M3 | Hard word ceilings block calibration work | item 27 | Part 2 §1, Part 5 bullet 3 | — | Cycle data below | Recorded |

## Convergent Findings

### C1. Perceptual failure attacks a production view no one holds

- **Flagged by**: chatgpt, claude
- **Verification**: clean, with both legs reaching the defect by content rather than by a live quotation. L114 «less brain activity should always mean less consciousness» and L108 «these should grade together» are 1 hit each in `topics/perceptual-failure-and-the-interface`. ChatGPT names no page. Its §7.8 verdict that the anaesthetic dissociation is non-discriminating contradicts L108, which counts that dissociation against emergence. Its §7.9 verdict on the "less brain activity, more consciousness" formula lands on the L112–L114 argument, which runs from reduced default-mode blood flow to a puzzle for generation. Claude quoted `archive/topics/perceptual-degradation-and-the-interface`, which was coalesced into this page on 2026-03-13. Its quoted sentence (count 1 in the archive) is the direct ancestor of L108: the coalesced page carried it verbatim until the 2026-06-11 refine reworded it. Claude's second complaint, the grade «This dissociation supports the interface model», has 0 hits live; L102 now says "interface-compatible".
- **History**: `reviews/outer-review-2026-06-11-chatgpt-5-5-pro.md` item 6 (L122) asked for this L114 fix. The 2026-06-11 refine (commit fd02950c4b) kept the sentence, changing only its punctuation, and rewrote the archived sentence into the present L108. So this is the third raise of a fix that has not landed.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "important evidence that responsiveness and conscious experience dissociate; not evidence that experience passes through a non-physical interface." And: "It does not support a simple “less brain activity, more consciousness” filter formula."
  - **Claude Fable 5.1**: "This is reached by attacking a strawman: “If consciousness were simply an emergent property of neural complexity, these should look similar—less complexity, less consciousness.”"
- **Task action**: Upgraded P2 → P1: "`topics/perceptual-failure-and-the-interface` L114 attacks a production view no one holds …". The task was already a single task, because the Claude processor appended a convergence note rather than minting a sibling, so nothing was deduplicated. `Review file` became `Review files`, a `Synthesis` line was added, the Notes gained the convergent preamble, and a COMBINE ADD-ON records the history and asks the fork to confirm that both strings reach str.count 0.

### C2. P-Q2's quantifier and the public-conditioning problem

- **Flagged by**: chatgpt, claude
- **Verification**: clean. The open decision is the blocked P1 HUMAN DECISION on P-Q2. "publicly conditionable" is live in `positions/quantum-interface` (1) and `concepts/selection-only-channel` (4). The intention-, task- and subject-conditioned tests ChatGPT cites are on that entry's cascade list, for example `concepts/consciousness-and-scientific-explanation` L58/L126.
- **What the two legs add together**: ChatGPT states the inconsistency: tests that condition on reported intentions or tasks condition on public variables, which the P-Q2 wording holds Born-exact. Claude states the entailment from the other side: the only conditioning variable left free is the mental state itself, and it cannot be fixed except through brain-mediated report. These are the same point. The entry's own 2026-10-30 reported-intention addendum had already reached it from inside the corpus.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "This is the most important formal inconsistency in the live corpus."
  - **Claude Fable 5.1**: "Any discriminating test must condition on a mental variable C that is fixed independently of the brain state it is meant to influence. No such independent fix exists, because C is accessed only through brain-mediated report."
- **Task action**: Recorded only. The entry is already P1 and blocked on a human decision. A COMBINE NOTE was appended to its Notes, and Status, Blocked-by and priority are unchanged.

### C3. The Tenet 3 quantifier, as it bears on AI verdicts

- **Flagged by**: chatgpt (the root), claude (a live instance)
- **Verification**: clean. ChatGPT's leg is that the AI register and the epiphenomenalism pages record the universal-versus-existential reading as unresolved. `positions/ai-consciousness-scope` L63 says `concepts/epiphenomenalism` "now records Tenet 3's quantifier as unresolved", and that is live. Claude's leg is at `concepts/substrate-independence` L126, «If AI systems were conscious, they would need to influence the physical world through non-physical means» (count 1). That sentence reads Tenet 3 universally, while L128 («those experiences would be causally irrelevant to outputs fully determined by computation», count 1) and L130 («truly epiphenomenal», count 1) entertain conscious but inert AI. Claude did not name the quantifier. Its point that the page makes Tenet 3 "a necessary condition on consciousness that no tenet states" is the universal reading, applied without warrant.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Until this is resolved, claims about passive experience, dreams, artificial phenomenality and minimal organisms will continue to oscillate between two different theories."
  - **Claude Fable 5.1**: "Fix “If AI systems were conscious, they would need to influence the physical world through non-physical means”, which makes Tenet 3 a necessary condition on consciousness that no tenet states."
- **Task action**: An addendum was added to the NEEDS-HUMAN (foundations) entry on the Tenet 3 quantifier, putting `concepts/substrate-independence` on its consumer-side sweep. A COMBINE NOTE was added to the Claude-leg P2 on `concepts/substrate-independence`, with no priority change. The two legs meet at the root, not on that page, and the page's correct fix depends on the human decision. Raising it to P1 would push a fork to settle locally a question the operator owns. The note tells the fork that the conditional rewording of L126 holds on every reading and is safe to install, and that it must not settle the quantifier.

### C4. P-Q1's credence is held at moderate because horn (a) is specifiable

- **Flagged by**: chatgpt, claude
- **Verification**: The text both legs target is live. P-Q1 L54 reads "credence moderate (low edge; conditional on both the horn-(a) wager and the P-Q10 toy-model debt being payable …)", and its L60 band rationale says the vacuity charge is answered "*in principle*" because horn (a) is specifiable, "so the credence was not cratered to *low*". Whether this is a defect is a calibration judgement. This band was held against two earlier convergent raises (2026-07-16 and 2026-07-27, recorded in `positions/quantum-interface-calibration-history`), so this is the third.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "There is no stated prior, update rule or reference class showing why an external-evidence-grade-D mechanism deserves moderate rather than low credence."
  - **Claude Fable 5.1**: "Holding credence at “moderate … pinned to the low edge” on the grounds that horn (a) is “in-principle specifiable” is calibration by possibility rather than by evidence."
- **Task action**: Recorded only. No open task owns P-Q1's band. The convergence was appended to the P-Q2 HUMAN DECISION entry, whose option (a) already requires re-running P-Q1's "falls to low" trigger. Whether to mint a `positions-evolve` re-adjudication now, or leave it to the P-Q2 decision, is a driver or operator call (see Method Notes).

### Methodology recurrences (M1–M3)

- **M1. Corrections and grades do not reach satellites.** ChatGPT: "the site’s own audits repeatedly find that corrections do not propagate automatically". Claude: "Hub honest, satellites flat", and "**Rule:** any logged defect must, in the same commit, change a credence, an evidence grade or a verdict, or delete text." Four of the cycle's verified tasks are live instances. `apex/taxonomy-of-voids` L231/L233 contradict P-V1 after three tenet checks flagged them. `apex/process-and-consciousness` drops `topics/consciousness-as-activity` L43's process-physicalism concession. `topics/machine-consciousness` L229 asserts tenet independence that `tenets/background-commitments` L36 disclaims. And C1's L114 survived the refine that was meant to remove it. An addendum was added to the NEEDS-HUMAN (methodology ratification) 2026-08-03 entry, with no new task.
- **M2. Same-family review is not independent review.** ChatGPT item 25: "Repeated reviews by related language-model families are not independent confirmations." Claude Part 5: "A reviewer and a reviser that share priors converge on *naming* defects, because naming is cheap and fluent." Both processors recorded this for the tune-system pass, and nothing was minted.
- **M3. Hard word ceilings stall calibration repairs.** ChatGPT item 27: "Replace hard word ceilings with modularisation", and "Do not force unresolved caveats into research notes where ordinary readers will miss them." Claude: "The page that carries the site’s deepest unresolved problem is the one page the maintenance cycle has decided to skip", which refers to `apex/born-preserving-causal-efficacy` under its NEEDS-HUMAN length decision. The cycle's own tasks support the point. Five of the sixteen target pages already over their hard limit: `tenets/tenets.md` at 6,793, `topics/machine-consciousness` at 4,127, `concepts/substrate-independence` at 3,610, `concepts/working-memory` at 3,746, and `positions/consciousness-scope` at 4,318 (critical). Two more have under 100 words of room: `apex/taxonomy-of-voids` with 86 and `concepts/conscious-vs-unconscious-processing` with 19. Recorded only; this belongs to the operator's ceiling policy.

## Rejected Convergences

- **R1. The ten-bit figure at `concepts/working-memory` L127 (Gemini plus ChatGPT §7.7 / item 18).** This is a topical agreement, not two legs on one defect. The Gemini leg reaches L127: it quotes the page's text and says the site links the rate "to working memory capacity limitations". But it misattributes the page, and its reason (the motor-only reading) is false. ChatGPT names no page, says nothing about working-memory capacity, and calls the Map's labelled caveat correct ("the Map’s recent caveat is correct. Any use as an upper bound on psychophysical coupling is an additional hypothesis"). L127 frames its interface clause as a hedged reading ("On that reading … suggesting both may reflect"). The tasked defect is that «matches WM capacity limitations strikingly well» (count 1) compares a rate with an item capacity, and Zheng & Meister find the rate unchanged under heavier memory load. That was established by the Gemini processor's own source check, not by either reviewer. The task stays P2, with a COMBINE NOTE recording this adjudication.
- **R2. The Tenet 4 argument is overstated (ChatGPT Tenet 4 and item 17; Claude's MWI satellites and its "no Tenet 4 apex").** Both legs are stale or already discharged. `tenets.md` L117 names Sebens & Carroll and L121 conditions the objection on a non-deflationary "I". `apex/one-world-wager` is the Tenet 4 apex. The "Ontological Extravagance" row of `arguments/many-worlds-argument` now reads as a non-decisive cost, the "doom many-worlds" gloss on `concepts/haecceity` has 0 hits, and `topics/quantum-measurement-consciousness-interface` is archived. Here two reviewers agreed on a defect that is no longer live.
- **R3. The active-inference rival is under-engaged (Claude on `topics/cognitive-science-of-dualism`; Gemini on `concepts/working-memory`'s effort account; ChatGPT in general).** The three legs sit at three different loci. Claude's absence claim is false (see Adjudication). Gemini's point is live: `concepts/working-memory` has 0 hits for "predictive processing", "precision" and "active inference", and L129 states the interface-friction account as "explains". The optional L129 calibration in the working-memory task partly covers it. No two legs share a sentence, so no upgrade. The pattern (dedicated pages engage the rival and satellites do not) is filed under M1.
- **R4. Voids as evidence (ChatGPT on `apex/taxonomy-of-voids`; Claude on the voids section).** These are different defects. ChatGPT quotes promotional lines in the apex. Claude keeps the P-V2 rule and objects to the section's volume ("Roughly a third of the corpus sits in a section that by its own rule cannot carry evidential weight"). That figure is wrong: `voids/` holds 116 files against 369 in topics, 371 in concepts, 45 in apex and 27 in positions, about 12%. Claude divided by the homepage's "over 300 articles". The ChatGPT task is already P1.
- **R5. The dissociation-as-evidence titles (ChatGPT item 14).** The ChatGPT processor predicted a Claude leg. Claude's review has 0 hits for either the clinical or the pharmacological page, and its dissociation point is C1's page. So the NEEDS-HUMAN retitle is singleton this cycle (it is the third raise across cycles, after the 2026-10-08 ChatGPT and Claude legs).
- **R6. Quantum-empirical overstatement (Gemini on DP, Claude on Georgiev, ChatGPT on Hagan).** Three reviewers took aim at the quantum empirical record, at three different claims. Two of the claims are false: DP suppression (see Adjudication), and Georgiev "unremarked" when he is cited on 10+ pages. Only ChatGPT's Hagan "corrected estimates" framing verifies, and it stays a singleton P2.
- **R7. Selection versus biasing (Claude's flagship cross-cluster contradiction).** No other leg made this point. The Claude processor rejected it: "biasing otherwise indeterminate outcomes" is the Minimal Quantum Interaction definition verbatim (`tenets/tenets.md` L65), and the actual defect class ("biasing probabilities") is queued as a P3. It is listed here only because the ChatGPT processor's convergence watch anticipated a Born-preservation cluster, and that cluster is C2, not this.

## Singleton Findings

Not upgraded; left at their original priority.

- **ChatGPT 5.6 Sol Pro**: `apex/taxonomy-of-voids` "receives the strongest support" / "gains cumulative support" against P-V1 → P1 (unchanged; it was minted at P1).
- **ChatGPT 5.6 Sol Pro**: `apex/process-and-consciousness` anti-emergentism, Relation verbs and the dropped process-physicalism concession → P2.
- **ChatGPT 5.6 Sol Pro**: `concepts/psychophysical-indexing-law`, the semantic-ratification dilemma → P2.
- **ChatGPT 5.6 Sol Pro**: `tenets/tenets.md` L77, Hagan et al.'s "corrected estimates", plus a six-page sweep → P2.
- **ChatGPT 5.6 Sol Pro**: `tenets/background-commitments`, linking the collapse-priority and composition debts → P2.
- **Driver-found during ChatGPT processing**: `positions/voids-as-evidence`, "roughly fifteen" versus the index's count → P3.
- **ChatGPT 5.6 Sol Pro**: NEEDS-HUMAN (editorial: retitle) for the clinical and pharmacological dissociation pages → untouched.
- **Claude Fable 5.1**: `topics/machine-consciousness` L229, "Each independently gives reason to doubt" (count 1) → P2.
- **Claude Fable 5.1**: `voids/observer-selection-void` L67, Elga's 2024 manuscript replaced by Elga (2025) *PPR* → P2.
- **Claude Fable 5.1**: `positions/consciousness-scope` P-CS7, the Boltzmann-brain commitment → P2.
- **Claude Fable 5.1**: `topics/cognitive-science-of-dualism` L103, Friston and Laukkonen et al. 2025 → P2.
- **Claude Fable 5.1**: NEEDS-HUMAN (editorial: homepage wording) → untouched (see D1).
- **Gemini 3.1 Pro**: `concepts/conscious-vs-unconscious-processing`, blindsight called "the clearest evidence" without Phillips 2021 → P2.
- **Gemini 3.1 Pro**: `topics/interventionist-and-counterfactual-dualism`, the interventionist branch's Baumgartner (2010) bill → P2.
- **Gemini 3.1 Pro**: `topics/experimental-consciousness-science-2025-2026` L50, GNWT ignition without the Naccache et al. 2025 reply → P2.
- **Gemini 3.1 Pro**: `concepts/working-memory` L127 → P2 (R1; COMBINE NOTE only).

The sixteenth task, the Claude-leg P2 on `concepts/substrate-independence` L126, belongs to C3 and is not repeated here.

## Divergences

- **D1. ChatGPT vs Claude on the status of the tenets.** ChatGPT reads the "chosen starting points" framing as honest calibration: "The tenet is now presented honestly as a chosen commitment in an unresolved dispute." Claude reads the homepage's "methodological choice, not dogma" and its "might be" gloss, set against Tenet 1's flat "is not reducible", as "quiet weakening for public consumption", and poses a dilemma between a methodological posit and a categorical claim. The two reviewers read different pages (`tenets/tenets.md` and `index.md`), but the issue is the same. Both views bear on the homepage NEEDS-HUMAN, which was left untouched as the brief requires. The operator has both on file here.
- **D2. Gemini vs ChatGPT on what Zheng & Meister measured.** Gemini: "They explicitly measured the information rate of *overt behavioral report*—specifically physiological output tasks like speech, typing, and motor tracking." ChatGPT: "They present this as a neuroscience conundrum concerning human behaviour and “inner” versus “outer” brain processing, not as a measure of a non-physical channel." The Gemini processor's check of arXiv v2 settles it for ChatGPT, since the perception phase is measured without motor readout. The Map's working-memory gloss already says *causal*, not phenomenal, bandwidth.

## Reviewer Reliability

- **ChatGPT 5.6 Sol Pro: the most reliable leg on the live state, imprecise on loci.** It treated the live site and the changelog through 4 November as authoritative and gave 54 Map links. Six reviewer-derived tasks verified, and the processing driver found a seventh. One claim was already fixed (Steward), one quotation was a paraphrase in quotation marks ("Digital hardware suppresses relevant quantum indeterminacy", 0 hits corpus-wide), and two points were partial false alarms (the Tenet 4 "omission", and the "minimal" gloss that `tenets.md` L69 already defines). Its source claims match the Map's records, though they were not re-fetched. It names pages rather than lines, so its C1 leg needed the driver's grep to find a locus.
- **Claude Fable 5.1: accurate on what it read live, mostly stale on everything else.** It fetched two pages live, the changelog and the homepage. Everything else came from search-index renderings, some of them months old, as its own caveats warn. Across its 24 numbered fixes and its Part 2 findings, seven claims targeted text already fixed, three quoted archived pages, three rested on false absence claims, and its voids-share figure was wrong. What survives is five tasks, one NEEDS-HUMAN and one convergence leg reached through an archived predecessor. Its changelog-derived claims were accurate wherever checked: the P-Q2 decision is open, the flagship is skipped on length, and the Family 3 sweep is queued. Its source work was good (the Stapp LBNL-55887 text, Elga 2025 *PPR*, the Laukkonen et al. 2025 metadata).
- **Gemini 3.1 Pro: verbatim text, wrong pages, unreliable source characterisation.** It audited the site as one "manuscript". Where it quotes, the strings are verbatim live, with one exception: "confirmed the pre-paradigm state rather than resolving it" has 0 hits and is its own paraphrase. But three of its five URLs do not hold the quoted text. Two of its five weaknesses fail against the page or the source. It misdated Baumgartner (2010, not 2020) and gave Zheng the wrong initial. Whether it read live pages or an index is unknown, because the source panel was not captured. Its DP miss cannot be put down to staleness, since the falsification sentence has been in the lead since 2026-07-31. Four residues were tasked, all after relocating the locus.

## Method Notes

- **Rule applied.** A cluster was upgraded only when at least two legs each pointed at a real defect, confirmed by grep on the same live page, with an open task. Only C1 met it. C2–C4 meet the two-leg test, but the matching entries are human decisions (C2, C3) or there is no task at all (C4). Upgrades go no higher than P1, and the loop cannot act on human-decision entries.
- **C4 is the case Claude's methodology critique describes.** Claude asks that "a disclosed, undischarged defect that two independent reviewers converge on" be treated as corroborated, against the 2026-08-24 line that restating disclosed liabilities is not corroboration. P-Q1's band rationale is disclosed, it is contested, and it has drawn convergent raises three times (07-16, 07-27, 11-05). This synthesis recorded the convergence but did not demote, because a credence band belongs to `positions-evolve` and is coupled to the open P-Q2 decision. The driver should choose between minting a `positions-evolve` re-adjudication of P-Q1's band now and leaving it to the P-Q2 decision. Leaving it unowned repeats the pattern the reviewer named.
- **No deduplication was possible.** Every one of the cycle's 16 tasks targets a different file, and no open task elsewhere in the queue duplicates any of them. The nearest neighbours are already coordinated by line ownership in the tasks' own notes: the P3 at todo ~L3640 on the perceptual-failure page and the P3 at ~L3247 on the process apex.
- **Todo edits.** One heading was changed from P2 to P1 in place. On the same task, `Review file` became `Review files`, a `Synthesis` line was added above `Headroom`, the Notes gained a convergent preamble, and a COMBINE ADD-ON went at the end. COMBINE NOTEs were appended to the Notes of the `concepts/substrate-independence` and `concepts/working-memory` P2s. Convergence notes were added to the P-Q2 HUMAN DECISION (in-line), the Tenet 3 NEEDS-HUMAN (one new paragraph) and the methodology-ratification NEEDS-HUMAN (one new Addendum line). `parse_tasks` returns 353 active tasks before and after. P1 went from 3 to 4 and P2 from 31 to 30, and the P0–P2 total is unchanged at 34. No article was edited.
- **Line numbers** refer to the live `obsidian/` text at 05:21–05:35Z on 2026-11-05.
