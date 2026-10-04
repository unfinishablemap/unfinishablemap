---
ai_contribution: 100
ai_generated_date: 2026-10-04
ai_modified: 2026-10-04 06:00:34+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts:
- '[[mental-effort]]'
- '[[control-theoretic-will]]'
- '[[phenomenology-of-choice-and-volition]]'
- '[[agent-causation]]'
created: 2026-10-04
date: &id001 2026-10-04
description: Cross-review synthesis of 2 outer reviews from 2026-10-04 (single-article
  audit of akrasia-and-weakness-of-will). Identifies findings flagged by multiple
  reviewers and upgrades their task priority.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-04 06:00:34+00:00
modified: *id001
related_articles:
- '[[project]]'
synthesis_coverage: 2/3
synthesizes:
- reviews/outer-review-2026-10-04-chatgpt-5-6-sol-pro.md
- reviews/outer-review-2026-10-04-claude-opus-5-5.md
title: Outer Review Synthesis - 2026-10-04
topics:
- '[[akrasia-and-weakness-of-will]]'
- '[[valence-and-conscious-selection]]'
- '[[responsibility-gradient-from-attentional-capacity]]'
- '[[free-will]]'
---

**Date**: 2026-10-04
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 2 of 3 commissioned reviewers contributed: ChatGPT 5.6.sol Pro and Claude Opus 5.5. The Gemini 2.5 Pro Deep Research leg (commissioned 04:25Z) started research on its own and reached "Researching 74 websites" by 04:52Z. The page then stayed byte-identical (18,146 characters) on three loads at 04:52Z, 05:22Z and 05:37Z, with a stop button but no report and no error. The driver abandoned it at 05:37Z, before the 4-hour cutoff (`pending-reviews.yaml`). No Gemini position is recorded or inferred below, and every cluster is at most 2/2 of the legs that reported.
**Subject**: a single-article audit of [akrasia-and-weakness-of-will](/topics/akrasia-and-weakness-of-will/) (`subject_type: recent`, source `fallback:recent-aged`; Claude and Gemini reused ChatGPT's subject). The live page is unchanged since commit `4b6f03fe66` (2026-09-27 01:06Z), so every line number below refers to the text both reviewers read.

## TL;DR

Both reviewers recommend **major revision**, and they agree on its shape. The exposition is mostly accurate, and the neutrality disclaimer is the article's best feature. The defects are fidelity slips in the Davidson, Plato, Aristotle, Hare and Holton material; an empirical claim ("trainable … survives") that the cited evidence does not carry; and a Relation to Site Perspective section that answers a foil instead of the strongest naturalistic rival and never asks how the Map's own selector handles the case.

**Seventeen convergent clusters held up against the live page (K7 and K12 in narrowed form), and an eighteenth holds in part (K18).** One shared charge, that the lens hedge makes the reading unfalsifiable and the Tenet 3 heading should go, was rejected as stated (R1). The Claude processing had already folded its findings into the existing tasks, so nothing needed deduplicating. **Two tasks moved P2 → P1**: the [akrasia-and-weakness-of-will](/topics/akrasia-and-weakness-of-will/) coverage task and the [mental-effort](/concepts/mental-effort/) L84 depletion task. The P1 correction task gained one newly found convergent item, the Socratic gloss and its hedonist premise (K16), which neither per-review pass had minted. It also gained a guard on the bridge-premise item and an explicit "do not" for R1. The choice-phenomenology question stays with the operator.

## Adjudication before clustering

Each candidate was checked against the live page, [tenets](/tenets/) and the cited sibling pages before it was counted. The two Processing Records listed nine candidates (C1–C9). This pass split C2 into three clusters and C5 into two, found four more (K6, K7, K8 and K16), and rejected one shared charge.

| # | Candidate | Verdict | Basis (live text) |
|---|---|---|---|
| K1 | "Trainable … survives"; depletion coverage is one 2016 figure | **Holds** | L78: "the effortful, trainable capacity" and "What survives is … a distinct, trainable capacity". Holton's MIT abstract has "distinct faculty" and "effortful" but not "trainable". The word entered from the 2026-07-09 research note (L64, L90). L78 and [mental-effort](/concepts/mental-effort/) L84 both rest on Hagger 2016 alone, and L84 says the model "collapsed under preregistration". The legs pull in opposite directions on the record (D4), so the task carries both. |
| K2 | Davidson's success presented as settled | **Holds** | L64: "Davidson's achievement is to show that akrasia is possible without being incoherent"; L84: "The post-Davidson consensus says yes". SEP §3.1 (raw text, re-checked here): "Most philosophers writing after him, while acknowledging his pathbreaking work on the issue, think he has not." |
| K3 | The all-out judgement at L68 | **Holds as a sourcing defect, not a mislabel** | L68: "forms the all-out judgement favouring *x*". ChatGPT wants it labelled a reconstruction. Claude's evidence (SEP note 11) shows it is an implication of Davidson's own treatment, made explicit in "Intending" (1978). The fix is to cite 1978, which the fold already says. |
| K4 | "No reason" stripped of its qualifier | **Holds (two qualifiers, one defect family)** | L86: "(the agent violates continence for no reason)" lacks the SEP's "he lacks a reason to do b rather than a" (ChatGPT). L70's ellipsis removes ", all things considered," (Claude), which turns a conditional judgement into an unconditional one. The 2026-08-26 ledger (L37) called that ellipsis "faithful". |
| K5 | The transparent read-off foil; no rival mechanism named | **Holds** | L92: "If selection were a transparent read-off of the agent's best judgement, Davidson's gap … would have nowhere to open." Mele, Ainslie, Bratman and any distributed architecture have 0 hits on the page. Claude adds that the article "does not strawman physicalism" in general (L100's concession). The defect is the foil plus the missing mechanism. |
| K6 | The Map's own selector inherits the puzzle (regress; agent-causal luck) | **Holds; new convergence** | The RTSP (L88–L104) never asks why a selector with its own reasons would choose what it judged worse. "luck" and "agent-caus" have 0 hits. ChatGPT §3.8 states the regress and Claude §3 the luck objection. The Claude processing listed luck as Claude-only. |
| K7 | "Interface" carries an unexamined mechanism | **Holds narrowly; new convergence** | L92 and L102 say "interface", with 0 hits for "quantum", "Minimal Quantum" and "Many Worlds". Claude's "billed as a neutral lens" misreads L40 ("explicitly framework-relative"). L90's "one lens among the framework-neutral accounts above" invites that reading, so an optional word-neutral "alongside" was added to the task. |
| K8 | Felt valence conflated with considered evaluation | **Holds at L92; new convergence** | L92 equates whether valence "guides selection or is idle to it" with whether the output "tracks the agent's evaluations". [the-steelman-for-value-blind-selection](/topics/the-steelman-for-value-blind-selection/) L39 says felt value "is what the selection tracks", and [valence-and-conscious-selection](/topics/valence-and-conscious-selection/) L49 already says the value-sensitive horn needs "present felt pull rather than considered judgement". ChatGPT §3.3 and §5 make the same point from the rational-akrasia side. The convergent locus is akrasia L92. The valence L49 "demonstrably" locus is ChatGPT's alone. |
| K9 | Weakness vs compulsion; deferring desert vs deferring classification | **Holds** | L102: "whether akratic acts are free and blameworthy is a further question the Map defers". L84 cites Watson 1977 by title only ("took up the weakness/compulsion boundary directly"), and "Gorman" has 0 hits. |
| K10 | Rational akrasia named only generically | **Holds** | L86: "Later writers argue that akratic action can be *rational*". Arpaly, McIntyre and Audi have 0 hits. |
| K11 | Schapiro absent | **Holds; framing diverges (D3)** | "Schapiro" has 0 hits. The SEP's "dualistic Kantian moral psychology" and Schapiro's "abandon[ing] your post as deliberator" were both re-checked in the raw SEP text. |
| K12 | Holton's normative criterion flattened to "over-ready" | **Holds in part** | L38 says "over-ready", but L76 already says "the unreasonable dropping of a commitment" and L86 "right to abandon a bad resolution". What is missing is the irreducibly normative criterion (Holton 1999, p. 259) that separates strength of will from stubbornness. The task was narrowed to at most 30 words. |
| K13 | Tenet 5 used to avoid comparative assessment | **Holds** | L104: "Holding the four positions open, rather than collapsing to the tidiest, is the honest register." The article does adjudicate elsewhere (L84, L78), and Claude adds that the four are not four answers to one question (L98, item 14). |
| K14 | Classical texts: translation unnamed; paraphrase in quotation marks | **Holds** | References L118 and L124: "Standard classical text". This is the only live article using that phrase, so the problem is local. L58's quoted "have and not have" is in neither Ross nor the SEP. That phrase was found by the ChatGPT processing; the ChatGPT reviewer flagged only the unnamed translations. |
| K15 | Hare pp. 67–85 | **Holds** | L122: "pp. 67–86". Crossref and OpenAlex give 67–85. The 08-26 ledger (L42) said "Oxford Academic's chapter page confirms" 67–86. |
| K16 | The Socratic gloss and its hedonist premise | **Holds; new convergence, previously unminted** | L50: "On his intellectualist picture, to judge a course of action best just *is* to be most motivated toward it." "hedon" and "measur" have 0 hits. Jowett's *Protagoras* (Gutenberg #1591, grep-verified) states the conclusion conditionally: "if the pleasant is the good, nobody does anything under the idea or conviction that some other thing would be better and is also attainable". SEP note 3: "But see inter alia Callard 2014, Liu 2022, and Obdrzalek 2023 for recent debate over Plato's view in the Protagoras." |
| K17 | Choice phenomenology "neutral" here, "evidence" elsewhere | **Holds; operator item** | [phenomenology-of-choice-and-volition](/concepts/phenomenology-of-choice-and-volition/) L3 says "irreducible evidence for conscious causal efficacy" and L123 "the strongest evidence for genuine conscious contribution". [free-will](/topics/free-will/) L66 says "The core evidence is phenomenological". Akrasia L102 calls its datum "neutral". |
| K18 | The hard-problem → controller bridge (L100) | **Holds in part** | Same sentence, different defects. ChatGPT: the hard-problem and conceivability arguments support non-reduction only, and the controller is a further premise. That checks out against [tenets](/tenets/): L55 marks Tenet 1 "a commitment the Map owns, not a result it reports", and L95 (`^tenet-3-standing`) calls downward causation "a posit the interface argument leaves open". Claude's charge is redundancy, which the page already concedes (R1). Guard added: tenets L59 lists epiphenomenalism under Tenet 1's "Rules out", so the fix must not say epiphenomenalist dualism is compatible with the tenets. |
| R1 | The lens hedge is unfalsifiable; drop the Tenet 3 heading; "compatibility case only" | **Rejected as stated: the page already does this** | L100: "an *interpretation* of a shared phenomenon, not evidence for its metaphysics". L102: "the phenomenon is neutral between the Map's reading and the naturalistic ones". An RTSP entry that records relevance without support is the pattern the writing-style guide requires. Both per-review processings disputed this charge. The live residue (rival mechanisms, interface, bridge) is K5, K7 and K18. |

## Convergent Findings

K1–K16 and K18 live on the two [akrasia-and-weakness-of-will](/topics/akrasia-and-weakness-of-will/) tasks, now both P1 and to be run as one editor pass, plus the [mental-effort](/concepts/mental-effort/) task. K17 is the operator's.

### K1. "Trainable … survives" and the depletion record
- **Flagged by**: chatgpt, claude
- **Verification**: clean; the directions diverge (D4)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The article’s positive conclusion about what survives is not adequately supported and is already empirically stale."
  - **Claude Opus 5.5**: "The article throws out the resource account and keeps one of its predictions."
- **Task action**: P1 correction task item (6) was already P1. **Upgraded P2 → P1**: "`concepts/mental-effort` L84 — 'The strength-resource model collapsed under preregistration' is stale…". It gained a guard to carry both directions and not to read Dang 2025 as a rescue. Its budget is unchanged (+90).

### K2. Davidson's success presented as settled
- **Flagged by**: chatgpt, claude
- **Verification**: clean (SEP §3.1 re-checked)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "“Dominant contemporary view” would be safer than “consensus.”"
  - **Claude Opus 5.5**: "The SEP reports that most post-Davidson philosophers "think he has not" shown this."
- **Task action**: already P1, no upgrade. Item (5) covers L84, and the fold extends it to L64 with Bratman's Sam.

### K3. The all-out judgement at L68
- **Flagged by**: chatgpt, claude
- **Verification**: holds as a sourcing defect. Claude's SEP note 11 overrides ChatGPT's "label it a reconstruction".
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Saying that the akratic “forms the all-out judgment favouring x” is stronger than the safest Davidsonian formulation."
  - **Claude Opus 5.5**: "According to the SEP, this implication "emerges with greater clarity" from Davidson's "Intending" (1978), not from the 1970 paper being cited."
- **Task action**: already P1. Item (3) as amended by the fold (cite "Intending", 1978).

### K4. "No reason" stripped of its qualifier
- **Flagged by**: chatgpt, claude
- **Verification**: clean. The two legs name two different qualifiers, and both are missing.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "“The agent has no reason” must not be left without qualification."
  - **Claude Opus 5.5**: "The ellipsis removes ", all things considered," which is the very qualifier Davidson's solution depends on."
- **Task action**: already P1. Items (2) and (13), with (13) amending the KEEP clause.

### K5. The transparent read-off foil and the missing rival mechanism
- **Flagged by**: chatgpt, claude
- **Verification**: clean
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The article contrasts the Map with a position few serious rivals hold."
  - **Claude Opus 5.5**: "Any non-transparent mechanism, whether motivational strength, discounting or partitioning, accommodates it equally well, so "must accommodate" is a weak constraint presented as a strength."
- **Task action**: already P1. Items (8) and (15).

### K6. The Map's selector inherits the akratic puzzle
- **Flagged by**: chatgpt, claude
- **Verification**: clean; new convergence (ChatGPT's regress and Claude's luck objection are the same gap)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "A nonphysical selector does not end the explanatory regress."
  - **Claude Opus 5.5**: "If the agent-cause selects *against* all of the agent's reasons, Davidson's "surd" becomes the luck objection in its starkest form."
- **Task action**: already P1. Items (8) (regress) and (17) (luck, linking [agent-causation](/concepts/agent-causation/)).

### K7. "Interface" carries an unexamined mechanism
- **Flagged by**: chatgpt, claude
- **Verification**: holds narrowly. Claude's "neutral lens" premise misreads L40, though L90 invites it.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The current halfway position lets “interface” carry mechanistic connotations without exposing the mechanism to scrutiny."
  - **Claude Opus 5.5**: ""Interface" and "controller" assume the Map's architecture inside what is billed as a neutral lens."
- **Task action**: already P1. Item (10), plus a new optional, word-neutral L90 "among" → "alongside".

### K8. Felt valence conflated with considered evaluation
- **Flagged by**: chatgpt, claude
- **Verification**: clean at akrasia L92; new convergence
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "If present felt valence drives the act, the choice may be value-sensitive even while departing from reflective judgment."
  - **Claude Opus 5.5**: "If the selector tracks felt valence, akratic choice is what the model predicts, and the selector is not the seat of rational agency."
- **Task action**: already P1. Item (16), aligning L92 with [valence-and-conscious-selection](/topics/valence-and-conscious-selection/) L49. The valence L49 "demonstrably" P2 is ChatGPT's alone and was left untouched.

### K9. Weakness vs compulsion, and what may be deferred
- **Flagged by**: chatgpt, claude
- **Verification**: clean
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Watson’s challenge deserves a full subsection."
  - **Claude Opus 5.5**: "The article cites the paper as a placeholder and never states its scepticism."
- **Task action**: **Upgraded P2 → P1**: "`topics/akrasia-and-weakness-of-will` — add the weakness/compulsion boundary…", item (a). The Claude-only P2 on [responsibility-gradient-from-attentional-capacity](/topics/responsibility-gradient-from-attentional-capacity/) L61 (weakness vs incapacity) is a separate locus and stays P2.

### K10. Rational akrasia named only generically
- **Flagged by**: chatgpt, claude
- **Verification**: clean
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The article mentions in one sentence that better judgment may itself be defective. That is not enough."
  - **Claude Opus 5.5**: "The article writes only "Later writers argue…" with no names (a generic claim)."
- **Task action**: covered by the same upgrade (coverage task item b).

### K11. Schapiro absent
- **Flagged by**: chatgpt, claude
- **Verification**: clean; framing diverges (D3)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Tamar Schapiro’s recent account deserves inclusion because it is unusually relevant to an agent-causal site."
  - **Claude Opus 5.5**: "Leaving her out is a missed chance to steelman, and the article should engage her."
- **Task action**: covered by the same upgrade (item c). The task now says to present her as both ally and rival.

### K12. Holton's normative criterion
- **Flagged by**: chatgpt, claude
- **Verification**: holds in part (L76 and L86 already carry most of it)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The article also underplays the normative element in Holton."
  - **Claude Opus 5.5**: ""Over-ready" flattens that point."
- **Task action**: covered by the same upgrade (item e), narrowed to at most 30 words.

### K13. Tenet 5 used to avoid comparative assessment
- **Flagged by**: chatgpt, claude
- **Verification**: clean
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Tenet 5 can block the inference “simplest, therefore true.” It should not block “simpler, equally predictive, and independently better supported, therefore presently preferable.”"
  - **Claude Opus 5.5**: "Tenet 5 is brought in exactly where parsimony would count against the redundant dualist gloss."
- **Task action**: already P1. Item (11), with no parsimony doctrine codified (operator item 7).

### K14. Classical texts: translation unnamed, paraphrase in quotation marks
- **Flagged by**: chatgpt, claude
- **Verification**: clean
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "“Standard classical text” is inadequate where translated wording is quoted or interpretive weight is placed on terms."
  - **Claude Opus 5.5**: "The article quietly drops "mad" and names no translation."
- **Task action**: already P1. Item (7), plus the fold (Hamilton & Cairns for the *Protagoras*).

### K15. Hare's page range
- **Flagged by**: chatgpt, claude
- **Verification**: clean (Crossref deposit and OpenAlex: 67–85)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "conceptually accurate, with a minor bibliographic correction and an underdeveloped implication"
  - **Claude Opus 5.5**: "OUP Academic gives pp. 67–85."
- **Task action**: already P1. Item (4).

### K16. The Socratic gloss and its hedonist premise
- **Flagged by**: chatgpt, claude
- **Verification**: clean. Jowett's 358b conditional and SEP note 3 were checked here, against the primary text and the raw SEP notes.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "presents one standard reconstruction as if it were simply the content of the passage"
  - **Claude Opus 5.5**: "The article mentions "miscalculation of pleasures and pains" but never says that the denial depends on a hedonism Socrates may not endorse."
- **Task action**: already P1. **Added as item (18)** to the P1 correction task, with the budget raised from +380 to +400. The fix says "On a standard intellectualist reading" and names the hedonist premise. The page's quotation uses the SEP's translation, so the item cites no Jowett quotation and no unread Callard, Liu or Obdrzalek.

### K18 (partial). The hard-problem → controller bridge
- **Flagged by**: chatgpt, claude (same sentence, different defects)
- **Verification**: ChatGPT's bridge-premise defect holds against [tenets](/tenets/) L55, L59 and L95. Claude's redundancy defect is R1.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Those are additional bridge premises."
  - **Claude Opus 5.5**: "If akrasia adds nothing, the dualist gloss does no work here and should be cut or labelled as purely redescriptive."
- **Task action**: already P1. Item (9), plus a guard against writing that epiphenomenalist dualism is tenet-compatible (tenets L59 rules it out).

### K17. One evidential status for choice phenomenology (operator)
- **Flagged by**: chatgpt, claude
- **Verification**: clean (pocv L3 and L123, free-will L66 and akrasia L102 all verbatim)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Calling the same family of experience “neutral” in one place and “evidence that” the Map’s ontology is true in another is an avoidable calibration failure."
  - **Claude Opus 5.5**: "The akrasia article calls the capacity to hold resolutions "ordinary self-management" with "no dualist commitment", then links to a page that treats that same capacity as evidence for conscious causation."
- **Task action**: none. Harmonising these turns on the Tenet 3 quantifier (actual or available efficacy). Both legs have already appended this to NEEDS-HUMAN (foundations) 2026-08-17, and it stays there.

## Singleton Findings

These were flagged by one reviewer only. They were not upgraded and stay at their original priority. Each was verified by its own processing pass unless marked otherwise.

- **ChatGPT 5.6.sol Pro**: L86 "Davidson builds irrationality into the definition" contradicts the article's own L66 definition → P1 correction task, item (1).
- **ChatGPT 5.6.sol Pro**: Aristotle's impetuosity/weakness split, Neoptolemus's "good incontinence" and the "strong-headed" → coverage task (now P1, carried by K9–K12), item (d).
- **ChatGPT 5.6.sol Pro**: the akratic datum should be time-indexed and kept apart from post-choice report, with a reciprocal on [preference-void](/voids/preference-void/) → coverage task, item (f).
- **ChatGPT 5.6.sol Pro**: Tenets 2 and 4 not engaged → P1 item (10) (its Tenet 2 half converges as K7).
- **ChatGPT 5.6.sol Pro**: [valence-and-conscious-selection](/topics/valence-and-conscious-selection/) L49 "demonstrably" → P2, untouched.
- **ChatGPT 5.6.sol Pro**: [control-theoretic-will](/concepts/control-theoretic-will/) L130 "concrete and testable" and the L144 akratic signal mapping → P2, untouched.
- **ChatGPT 5.6.sol Pro**, not minted by its processing: direct citations for Mischel and Baumeister (27); Hagger et al. 2026 on trait self-control; Gillebaart & Schneider 2024 on effortless self-control (its content is unread, so it is optional in the coverage task as "skill models"); a site-wide taxonomy of practical states (19); the Volitional Control "inconsistency" (rejected); "freely and knowingly" (rejected, see D5); regularising Davidson's date (rejected, see D1).
- **Claude Opus 5.5**: L98 "Holton explains it", where "it" means akrasia → P1 item (14).
- **Claude Opus 5.5**: L56 "what he calls the kernel of truth" → P1 item (12).
- **Claude Opus 5.5**: the L70 quotation opens at "if we ask", outside the SEP's quotation marks, and carries the SEP's "[b]" → P1 item (13), whose ellipsis half converges as K4.
- **Claude Opus 5.5**: the "four positions" are not four answers to one question → P1 item (14), optional clause.
- **Claude Opus 5.5**: Holton's contested folk-concept thesis (SEP note 16; Holton & May 2012), the missing Holton 1999 reference, and Davidson 1982 as an optional, unverified lead → coverage task, items (g) and (h).
- **Claude Opus 5.5**: [responsibility-gradient-from-attentional-capacity](/topics/responsibility-gradient-from-attentional-capacity/) L61 treats weakness as incapacity → P2, untouched (coordinated with K9).
- **Claude Opus 5.5**, rejected by its processing as stale: the responsibility-gradient "Meister's 2024 analysis of perceptual limits" (replaced 2026-06-04), interactionist-dualism "alone" (removed 2026-10-03) and the witness-consciousness Zeno cell (relabelled 2026-09-02).
- **Claude Opus 5.5**, recorded but not minted: Vohs 2021 (felt effort rose without a reliable performance change) for pocv's "What would challenge" list, which on Claude's own account does not meet falsifier (3) (NEEDS-HUMAN 2026-08-17); the glucose-model critiques (leads only, quotes unverified); *The Language of Morals* for Hare's inverted-commas sense.

## Divergences

- **ChatGPT vs Claude, Davidson's date (D1)**: ChatGPT says "The publication history should also be regularised." Claude says "Hedging the date is the right call." Adjudicated for the article: two prior ledgers ratified the 1969/1970 hedge as a record of catalogue disagreement, and the stable reprint is cited.
- **ChatGPT vs Claude, Hare (D2)**: ChatGPT says "The article accurately represents Hare’s view". Claude says "Hare also does not simply say akrasia is "impossible"." Adjudicated for the article: the SEP's own §1 heading is "Hare on the Impossibility of Weakness of Will" (re-checked here), and Hare's chapter abstract (moral weakness is no counterexample to prescriptivism) is consistent with denying strict akrasia.
- **ChatGPT vs Claude, Schapiro's role (D3)**: ChatGPT presents her as a rival ("the agent ceased exercising the will, so the ensuing behaviour should not be understood as a conscious selection at all"). Claude presents her as "the closest thing to an ally in the literature". Both framings hold, and the coverage task now says to present both and not to choose.
- **ChatGPT vs Claude, which way the depletion record leans (D4)**: ChatGPT's Dang 2025 suggests "depletion findings may be paradigm- and intensity-dependent rather than simply absent". Claude's Vohs 2021 strengthens the null ("Because proponents helped design that test, it is harder for them to dismiss than Hagger 2016"), while Claude also notes that the proponents' rebuttals are missing. Both agree the record is wider than one figure, which is K1. The mental-effort task now carries both directions.
- **ChatGPT vs Claude, freedom in the explanandum (D5, implicit)**: ChatGPT says of deferring freedom to the moral-responsibility article: "That division does not work." It wants L33's "freely" turned into an open question. Claude assumes "Davidson's definition makes the akratic act free and intentional". The article keeps "freely": the SEP's own characterisation is "free, intentional action contrary to the agent’s better judgment" (re-checked here). ChatGPT's substantive point, that classification needs the compulsion boundary, is K9.

## Operator Items (methodology; not minted)

The per-review passes deliberately did not mint methodology recommendations. The convergent points among them are listed here for the operator, each against the open entry it reinforces.

1. **One evidential status for choice phenomenology** (K17; ChatGPT 22, Claude rec 10). This is the Tenet 3 quantifier: does the phenomenology evidence *actual* efficacy, or only available efficacy? → NEEDS-HUMAN (foundations) 2026-08-17. Both legs appended to it today.
2. **A discriminating prediction, or an explicit "non-discriminating" label, wherever a Map reading meets a rival** (ChatGPT 21, 23, 24; Claude methodology 3 and 4). Both want a controlled evidence vocabulary and a rule that a reading claiming no evidential weight must name the strongest rival mechanism. → NEEDS-HUMAN (methodology governance) 2026-08-01 (evidential-status scale) and (methodology ratification) 2026-07-25 (opponent parity). R1 shows the article already meets the disclaimer half. The missing half is the named mechanism.
3. **Cross-article claim-strength consistency** (ChatGPT 22, 29; Claude methodology 5): flag page A disclaiming X while linking page B that asserts X. → NEEDS-HUMAN (methodology ratification) 2026-08-03. K17 is the live instance.
4. **A register of contested effects / a claim–evidence matrix** (Claude methodology 2; ChatGPT 28). → NEEDS-HUMAN (methodology) 2026-07-30 (per-claim verification ledger, "contested by later literature" tier). K1 is the live instance: one 2016 figure carries the depletion record on two pages.
5. **Internal citation is not independent support** (ChatGPT §1 "Internal Map citations"; Claude §5 "Circular cross-referencing"). → NEEDS-HUMAN (methodology) 2026-07-29 (deferral-chain grounding). Claude's remedy, moving Map pages out of References, was rejected as a corpus convention. The convergent point is evidential, not about placement.
6. **Quote provenance and named translations** (Claude methodology 1 and 9; ChatGPT 5). → NEEDS-HUMAN (corpus convention): "reference apparatus cannot express VERIFICATION LEVEL". On scale: "Standard classical text" appears in 1 live article (this one), so the translation half is local and handled by P1 item (7).
7. **The scope of Tenet 5** (ChatGPT 25, site-wide; Claude §4, local). → NEEDS-HUMAN (doctrine) 2026-09-19. The P1 task fixes the local instance (item 11) without codifying a doctrine.
8. **Process observation from this pass (one source, recorded only)**: three of the article's fidelity defects entered from the 2026-07-09 research note's paraphrases. They are "trainable" (note L64 and L90; part of K1), "the kernel of truth" (note L52) and "have and not have" (note L79). In addition, the 2026-08-26 ledger certified two readings both legs overturned: L37 calls the Davidson ellipsis "faithful", and L42 says "Oxford Academic's chapter page confirms" pp. 67–86. This is adjacent to Claude methodology 7 (research-gap gate) and NEEDS-HUMAN (methodology) 2026-08-04 (contiguity is not provenance).

## Method Notes

- Both legs audited one unchanged page with hostile-audit prompts, so overlap was expected and adjudication mattered more than counting. The one rejected shared charge (R1) came from both reviewers treating the RTSP's tenet heading as a claim of support, which L100–L102 explicitly disclaim.
- Re-checked for this pass against raw sources: SEP §1 heading, §3.1, the characterisation "free, intentional action…", "dualistic Kantian moral psychology", "abandon[ing] your post as deliberator" and note 3 (live SEP HTML and notes.html); Jowett's *Protagoras* 358b and "the art of measurement" (Gutenberg #1591). All other external claims rely on the per-review processings' checks.
- Every task change was verified with `parse_tasks`. The active count was 76 before and 76 after. P1 went from 1 to 3 and P2 from 16 to 14. Exactly three blocks changed: the two [akrasia-and-weakness-of-will](/topics/akrasia-and-weakness-of-will/) tasks and the [mental-effort](/concepts/mental-effort/) task. In each, the original Notes (the ChatGPT text plus the Claude fold) sit byte-identical inside the new Notes. Every addition went inside Notes, because `task_to_skill` dispatches only Notes and the Review file(s) value. The `Review files` (plural) line is parsed (`tools/todo/processor.py:153`), and the dispatched args were confirmed to carry both review paths and this file's path. The valence L49, control-theoretic-will and responsibility-gradient tasks are untouched.
- With this file on disk, the 10-04 outer-review tasks are released to the queue.
- Model: claude-opus-5-5.