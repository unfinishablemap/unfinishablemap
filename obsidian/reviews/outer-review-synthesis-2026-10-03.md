---
title: "Outer Review Synthesis - 2026-10-03"
created: 2026-10-03
modified: 2026-10-03
human_modified: null
ai_modified: 2026-10-03T07:01:32+00:00
draft: false
description: "Cross-review synthesis of 2 outer reviews from 2026-10-03 (single-article audit of consciousness-as-activity). Identifies findings flagged by multiple reviewers and upgrades their task priority."
topics:
  - "[[consciousness-as-activity]]"
  - "[[hard-problem-of-consciousness]]"
  - "[[enactivism-challenge-to-interactionist-dualism]]"
  - "[[bergson-and-duration]]"
concepts:
  - "[[process-philosophy]]"
  - "[[agent-causation]]"
  - "[[where-the-substance-commitment-enters]]"
  - "[[bi-aspectual-ontology]]"
  - "[[temporal-consciousness]]"
  - "[[embodied-cognition]]"
  - "[[the-agent-shaped-hole]]"
related_articles:
  - "[[project]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-03
last_curated: null
synthesizes:
  - reviews/outer-review-2026-10-03-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-10-03-claude-opus-5-5.md
synthesis_coverage: "2/3"
---

**Date**: 2026-10-03
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 2 of 3 commissioned reviewers contributed: ChatGPT 5.6.sol Pro and Claude Opus 5.5. The Gemini 2.5 Pro Deep Research leg (commissioned 04:10Z) was abandoned by the driver at 06:22Z. Deep Research ran for about two hours: it reached "Researching 91 websites" by 04:37Z, and its panel was static from 05:07Z. Gemini then replaced it with "Something went wrong. Please try again later." No report was produced, and the leg was not resubmitted because of dead-turn risk (`pending-reviews.yaml`). No Gemini position is recorded or inferred below. Every cluster is at most 2/2 of the legs that reported.
**Subject**: a single-article audit of [[consciousness-as-activity]] (`subject_type: recent`, source `fallback:recent-aged`; Claude reused ChatGPT's subject). The live page is unchanged since commit `a5791c646a` (2026-09-26 01:48Z), so every line number below refers to the text both reviewers read.

## TL;DR

Both reviewers return **major revision**, and both lead with the same diagnosis. The article's concessions have not reached its claims. The concessions are that the framing is "neutral ground", that process-identity physicalism "can accept the verb framing", and that "the verb shift leaves the hard problem standing". The claims that outrun them are the lead ("aligns naturally", "wrong category"), the closure wording ("is answered"), the MWI paragraph ("reinforces indexical identity") and the Further Reading gloss ("ultimately reinforces"). Both also hold that the verb shift restates Chalmers's problem instead of reframing it, because Chalmers already posed it about processing and function.

**Sixteen convergent clusters held up when checked against the live page, and one more holds in part.** Four candidate convergences were rejected or not counted: one shared false premise (Whitehead), one non-defect (L89), one wrong locus (the enactivism page) and one that rested on a quote the per-review processing had rejected. The tasks were already shaped by the Claude processing's fold, which put the convergent material onto the two existing [[consciousness-as-activity]] tasks, so nothing needed deduplicating. **One task was upgraded, P2 → P1**: the source-fidelity task. Both tasks were rewritten and extended with five verified loci. A plumbing defect was also found and fixed for these two tasks: the Claude fold sat in a field the dispatcher never passes to the executing fork.

## Adjudication before clustering

Each candidate was checked against the live page, the tenets page and the cited sibling pages before it was counted. The two per-review Processing Records listed nine candidates between them (C1–C9 in the Claude record, C1–C7 in the ChatGPT record). This pass found eight more and rejected four.

| # | Candidate | Verdict | Basis (live text) |
|---|---|---|---|
| C1 | Closure "answered" vs available-not-actual | **Holds, narrowed** | L87 and L130 say "answered". tenets L95 (`^tenet-3-standing`, since 2026-08-03) says "available … without showing it to be *actual*" and adds that articles "should read no more confidently than this paragraph does". L130's last sentence ("this answer is available on the activity framing") is already in the right register, so the defect is the two uses of "answered" and the missing P-Q10 no-model debt. It is a calibration shortfall, not a flat contradiction. |
| C2 | The hard problem is already posed of processes | **Holds (Chalmers); weaker for Nagel** | L49: the classic formulation "presupposes the property framework". Chalmers 1995 asks "Why is the performance of these functions accompanied by experience?" (verified by the ChatGPT processing). The Map's own [[hard-problem-of-consciousness]] L94 and L119 pose the problem about neural activity and processing. Nagel's canonical sentence does use possession grammar ("an organism has conscious mental states if and only if there is something…", checked in the 1974 PDF text), so the correction should rest on Chalmers. L93–L95 repeat the reframing claim and were added as loci. |
| C3 | The lead outruns the "neutral ground" concession | **Holds, except "removes obstacles"** | L43 says "aligns naturally" and "aiming its reduction at the wrong category", and L126 opens "dualism becomes more natural". All three are undercut by L126's own "neutral ground … not an independent refutation". Claude's request to replace "removes obstacles" (in the description) does **not** hold: that phrase matches the RSP opener at L124 and was a deliberate 09-26 downgrade from "strengthens". |
| C4 | MWI copy argument vs the branch-relative/fission reply | **Holds** | L132: "activities cannot be copied without becoming different activities". Both reviewers make the type/token point. tenets L123 says that if the subject were "treated as a mere process, the indexical objection would weaken correspondingly". The fix makes the dependency explicit and does not reopen the bedrock dispute with MWI (tenets L121). |
| C5 | Clark slogan; James on effort | **Holds, with a James nuance** | L110: "brains don't *have* models". Clark 2013 says prediction is "achieved using a hierarchical generative model" (verified via OpenAlex by the ChatGPT processing). L77: "Properties don't strain." In *Principles* ch. XI (raw Gutenberg text, re-checked here), James concedes "The feeling of effort certainly _may_ be an inert accompaniment and not the active element", which defeats the inexplicability inference. He then counts himself among the believers in a spiritual force, "as my reasons are ethical". James therefore leans the Map's way on ethical grounds, and the fix must not recast him as an opponent. |
| C6 | GNW ignition without COGITATE 2025 | **Holds (currency, not refutation)** | L120 rests on Dehaene & Changeux 2011 alone. Both reviewers quote the same PubMed 40307561 sentence, which the ChatGPT processing verified. COGITATE challenges ignition at stimulus *offset*. ChatGPT itself says "This does not falsify GNWT". |
| C7 | The "ultimately reinforces" gloss vs the body | **Holds on this page; the shared fix locus is wrong** | L147 says "challenges and ultimately reinforces". L116 says "a framework-boundary difference … do not settle in the Map's favour" and ends "ultimately cannot close". Both reviewers also recommend editing [[enactivism-challenge-to-interactionist-dualism]] (ChatGPT item 32, Claude rec 13), but that page has 0 "reinforce" hits and its L78 keeps the hedge "though the judgement is not forced by the data alone". ChatGPT dropped that hedge, and Claude could not fetch the page. |
| C8 | Time-slice extensionalism asserted flatly | **Holds** | L83: a time-slice "cannot contain consciousness". [[temporal-consciousness]] L102 says the choice "may be structurally underdetermined", and temporal-consciousness-structure-and-agency L88–L90 present retentionalism as live. Claude's sub-point that quasi-instantaneous selection "sits awkwardly" is already answered at L83 ("an event *within* this thick activity, as a footfall is a moment inside the dance"). |
| C9 | Agent-causal choice built into the explanandum | **Holds** | Two loci, one per reviewer. L53 lists "agent-causal selection" beside subjective character and intentionality (ChatGPT §11.1), and L100 has "constituting its own content through agent-causal choice" (Claude §3.5, §5). L85 itself says the tenet "commits only to outcome-selection", and tenets L151 says the same. |
| X1 | Bergson extrapolated to the property framing | **Holds (narrow); new convergence** | L71: "targets exactly the property framing … placing it alongside other properties like position and charge". ChatGPT calls that "the article's extrapolation", and Claude calls it "the article's modern gloss presented as Bergson's critique". The Claude processing did not mark this item convergent. |
| X2 | Candidate features not shown to be necessary or testable | **Holds; new convergence** | L99: recursive self-awareness "distinguishes experience from mere processing". Claude cites minimal phenomenal experience and ChatGPT cites basic pain and colour experience. L102 says "genuinely novel": Claude says it "cannot be tested as stated", and ChatGPT says it needs to be "operationalized". |
| X3 | The skilled-performance claim is uncited | **Holds; new convergence** | L118 cites only a Map page (ChatGPT §6.6; Claude §2, "No external source"). The task item was optional and is now required. |
| X4 | Process philosophy is borrowed without disclosing its verdict on interactionism | **Holds; new convergence** | L65 says "The Map borrows the priority of becoming" and discloses the panexperientialism departure, but not Whitehead's bifurcation verdict ([[process-philosophy]] L124: "interactionist dualism included"). Claude §4 and §6 and ChatGPT §10.3 and §12 make this point. |
| X5 | The sciences are enlisted though their own metaphysics is neutral or physicalist | **Holds narrowly; new convergence** | L108: developments "that the property framing struggles to accommodate". By the article's own L47 taxonomy, functionalism is a property family, and GNW is functionalist (Claude §2; ChatGPT §7). The 09-26 Stability Notes make *PP/enactivism* co-optation bedrock, and L110 and L116 already disclose Clark and Thompson, so only L108 and GNW are in scope. |
| X6 | The activity view's own debts go unbooked | **Holds; new convergence** | L55 says the activity reading "earns its place by the puzzles it avoids", and L134 books only the Whiteheadian form's combination problem. The Map's own form, with the performing subject posited at L85, carries the pairing and persistence questions (ChatGPT §11.4; Claude §5, "Asymmetric Occam", and §4). |
| X7 | Activity and property are not exclusive; properties can be dynamic | **Holds; the per-review fold already marked it convergent** | L104 ("None of these features can be understood as static properties"), L126 ("Properties invite reduction") and the opening generalisation at L43. Both reviewers cite dynamic and dispositional properties and non-reductive property views. "Exactly two families" (L47) is ChatGPT's alone. |
| X8 | The performing subject is posited for framework reasons; unity is under-argued | **Holds in part** | L85 already marks the posit ("The Map posits a performing subject … that the Map's agency cluster adopts"), which largely meets ChatGPT §11.2's demand. What remains is unity ("reads more naturally"), which both reviewers call an intuition. Unity is not one of the two homes on [[where-the-substance-commitment-enters]], which has 0 "unity" hits. That locus was already folded into P1 item (2). |
| R1 | Whitehead: experience blurred into consciousness ("misattribution") | **Rejected: shared false premise** | L63 calls consciousness "the more complex and integrated form of what all occasions do", and L65 says "*experience* is what actuality does, all the way down". The distinction is drawn. Claude's TL;DR clips the quote to "what all occasions do". Both per-review processings had already disputed this. What survives is narrow: L63's "Consciousness is not something occasions have" (optional, task item 8). |
| R2 | L89 "outsources" the ontological argument | **Rejected: not a defect** | L89 makes exactly the concession both reviewers ask for ("Dancing is itself physical … illustrates but does not establish"). Deferring to the explanatory-gap pages is the Map's normal division of labour. |
| R3 | Edit the enactivism-challenge page | **Rejected: wrong locus** | See C7. |
| R4 | L128's attention analogy does not make selection intelligible | **Not counted** | Claude's support (interactionist-dualism L125, "Attention is neurally implemented") was rejected by its own processing as out of context. Disputed support does not count toward convergence, which leaves ChatGPT §8 as a singleton. |

## Convergent Findings

The first group of clusters lives on the P1 calibration task, the second on the P1 source-fidelity task (formerly P2). Both tasks are on [[consciousness-as-activity]] and are to be run as one editor pass.

### C1. "Answered" outruns "available"
- **Flagged by**: chatgpt, claude
- **Verification**: clean; narrowed (see the table)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "the activity article's statement that the exclusion problem is 'answered' at the quantum interface is too strong"
  - **Claude Opus 5.5**: "Its answer to the exclusion problem ('it is answered by the selection mechanism') also claims more than the Map's own Tenets page allows."
- **Task action**: already P1, so no upgrade. P1 calibration item (1) was narrowed to the two uses of "answered" plus the P-Q10 debt.

### C2. The hard problem was already posed about processes
- **Flagged by**: chatgpt, claude
- **Verification**: clean for Chalmers; the Nagel half is weaker
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The reformulation is therefore not a new version of the hard problem. It is close to a restatement of it."
  - **Claude Opus 5.5**: "Chalmers states the hard problem as a question about *processes and functions* being accompanied by experience."
- **Task action**: already P1, so no upgrade. Item (4) was extended with L93–L95 and the Nagel nuance.

### C3. The lead and the "more natural" claims outrun "neutral ground"
- **Flagged by**: chatgpt, claude
- **Verification**: clean, except Claude's "removes obstacles" request (rejected; see Divergences)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "the article is commendably candid that the evidence underdetermines the noun and verb framings. That admission should become the controlling thesis of the page rather than a local disclaimer surrounded by stronger claims."
  - **Claude Opus 5.5**: "Yet its abstract still says the framing 'removes obstacles to interactionist dualism', and its opening says it 'aligns naturally' with that view."
- **Task action**: already P1, so no upgrade. Item (6).

### C4. The MWI copy argument
- **Flagged by**: chatgpt, claude
- **Verification**: clean
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "An Everettian can readily accept that post-branch activities are numerically distinct tokens."
  - **Claude Opus 5.5**: "This confuses types with tokens. Under branching, each branch contains a continuous token activity with the same pre-split history".
- **Task action**: already P1, so no upgrade. Item (2).

### C7. The Further Reading gloss contradicts the body
- **Flagged by**: chatgpt, claude
- **Verification**: holds at L147/L116; both reviewers' proposed edit to the enactivism page rests on a misreading (R3)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "the activity page describes that challenge as 'ultimately' reinforcing dualism. … The stronger conclusion is not earned."
  - **Claude Opus 5.5**: "The article contradicts itself about enactivism."
- **Task action**: already P1, so no upgrade. Item (8).

### C9. Agent-causal choice is built into what is to be explained
- **Flagged by**: chatgpt, claude
- **Verification**: clean (L53 and L100)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Putting it inside the initial characterization of conscious activity loads the conclusion into the premise."
  - **Claude Opus 5.5**: "Building 'agent-causal choice' into the list of candidate features that make an activity experiential means the outcome is fixed by definition."
- **Task action**: already P1, so no upgrade. Item (3).

### X6. The activity view's own debts go unbooked
- **Flagged by**: chatgpt, claude
- **Verification**: clean (L55, L134 against L85)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The article counts the property view's debts without giving an equivalent account of its own."
  - **Claude Opus 5.5**: "conceptual richness is just as unable to decide in the other direction."
- **Task action**: NEW item (10) on the P1 calibration task: one clause at L134 or L55 naming the posited subject's pairing and persistence questions.

### X7. Property and activity are not exclusive categories
- **Flagged by**: chatgpt, claude
- **Verification**: clean; the "exactly two families" taxonomy half is ChatGPT's alone
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "There are dispositional properties, relational properties, temporally extended properties and dynamically realized properties."
  - **Claude Opus 5.5**: "Dynamic, dispositional and relational properties are still properties".
- **Task action**: already P1, so no upgrade. Item (5).

### X8 (partial). The performer is posited; unity is under-argued
- **Flagged by**: chatgpt, claude
- **Verification**: the framework-requirement half is already met at L85; the unity half holds
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Saying unity 'reads more naturally' as one subject acting records an intuition."
  - **Claude Opus 5.5**: "Unity is not one of the canonical page's two named entry points."
- **Task action**: already P1, so no upgrade. This is covered by the Claude-fold locus on item (2), and the task note now says no new defence is to be added.

### C5. The Clark slogan and James on effort
- **Flagged by**: chatgpt, claude
- **Verification**: clean; James re-checked in the raw text (his lean is toward the cause-theory)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "the slogan 'brains don't have models, they do modelling' is not faithful to Clark's terminology"
  - **Claude Opus 5.5**: "'Properties don't strain' is the article's own slogan, not a Jamesian argument."
- **Task action**: **Upgraded P2 → P1**: "`topics/consciousness-as-activity` — four source-fidelity slips, a stale GNW paragraph and two missing counterexample classes". This was the single task for the cluster; there were no siblings to deduplicate. Items (1) and (2), with the James nuance added.

### C6. The GNW paragraph lacks COGITATE 2025
- **Flagged by**: chatgpt, claude
- **Verification**: clean; present it as a challenge, not a refutation
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "a 2026 article should not present the 2011 ignition picture without the update."
  - **Claude Opus 5.5**: "The ignition claim the article leans on is exactly what was tested, and the article does not mention it."
- **Task action**: covered by the upgrade above. Item (5).

### C8. Extensionalism is asserted flatly
- **Flagged by**: chatgpt, claude
- **Verification**: clean; Claude's instantaneous-selection sub-point is already answered at L83
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The page can defend extensionalism, but it cannot simply build it into the definition of activity."
  - **Claude Opus 5.5**: "This takes a side in an open debate on temporal experience (cinematic, retentional and extensional models)".
- **Task action**: covered by the upgrade above. Item (4).

### X1. Bergson is extrapolated to the property framing
- **Flagged by**: chatgpt, claude
- **Verification**: clean (narrow: "bears on", not "targets exactly")
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Saying his critique targets 'exactly the property framing' is the article's extrapolation."
  - **Claude Opus 5.5**: "'placing it alongside other properties like position and charge' is the article's modern gloss presented as Bergson's critique."
- **Task action**: covered by the upgrade above. Item (3), now marked convergent.

### X2. Candidate features are not shown to be necessary or testable
- **Flagged by**: chatgpt, claude
- **Verification**: clean (L99, L102)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Basic pain, colour experience or sudden noise awareness may not require recursive self-awareness."
  - **Claude Opus 5.5**: "'Creative synthesis … genuinely novel' cannot be tested as stated."
- **Task action**: covered by the upgrade above. Item (6) was extended with L99 and L102.

### X3. The skilled-performance claim is uncited
- **Flagged by**: chatgpt, claude
- **Verification**: clean (L118 links only [[consciousness-and-skill-acquisition]], whose own reference list has the literature)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "the target article cites only another Map page."
  - **Claude Opus 5.5**: "No external source."
- **Task action**: covered by the upgrade above. The item was optional and is now required: cite the sibling's sources, or soften the claim at no word cost.

### X4. Process philosophy's verdict on interactionism is not disclosed
- **Flagged by**: chatgpt, claude
- **Verification**: clean (L65 against [[process-philosophy]] L124)
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "why should an ontology built to replace substance/property dualism support a substance-leaning, mind–body interaction theory? Selective borrowing is permissible, but the compatibility cannot be assumed."
  - **Claude Opus 5.5**: "The article 'borrows the priority of becoming' without telling readers that its source tradition rejects interactionism outright."
- **Task action**: covered by the upgrade above. Item (8), the bifurcation disclosure, now marked convergent. The experience-versus-consciousness charge is excluded (R1).

### X5. L108 and GNW: the sciences' own metaphysics
- **Flagged by**: chatgpt, claude
- **Verification**: clean, scoped to L108 and GNW because of the 09-26 bedrock note on PP and enactivism
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Scientific alignment is real but nondiscriminating"
  - **Claude Opus 5.5**: "global workspace theory is a functionalist account of *access* consciousness. Enlisting it as 'aligning' with a dualist-friendly activity view without saying so is co-optation."
- **Task action**: NEW item (11) on the upgraded task.

## Singleton Findings

These were flagged by one reviewer only. They were not upgraded and stay at their original priority.

- **ChatGPT 5.6.sol Pro**: the "exactly two families" taxonomy (L47) omits substance dualism, neutral monism, idealism and others → P1 calibration task, item (5).
- **ChatGPT 5.6.sol Pro**: Whitehead and quantum measurement, "closing on precisely this point" (L65), where the linked page says only "resonates" → P1 calibration task, item (7).
- **ChatGPT 5.6.sol Pro**: passive and unconscious controls for "selective engagement" (Hung, Wu & Shimojo 2020) → P1 source-fidelity task, item (6).
- **ChatGPT 5.6.sol Pro**: the phenomenology-to-ontology slide and "independent philosophical support" on [[bergson-and-duration]] → `todo.md` task "`topics/bergson-and-duration` moves from phenomenological non-spatiality…" (P2, untouched).
- **ChatGPT 5.6.sol Pro**, not minted by its processing: self-application of [[the-agent-shaped-hole]] (item 33); a compatibility bridge on the process-and-consciousness apex (28); the cinematic model on temporal-consciousness-structure-and-agency (31; 3,897/4,000 words); inheritance of the consciousness-and-agency caveats (34); randomness versus reasons (§10.8); and the L128 relabelling point (§8; see R4).
- **Claude Opus 5.5**: who performs the activity (organism or subject, L43 against L85/L116), and whether the body is a constituent (L112) or an interface ([[embodied-cognition]] L142) → P1 calibration task, item (9).
- **Claude Opus 5.5**: Noë, *Out of Our Heads* (2009), as the uncited closest precedent; the Kim (1998) reference; `ai_system` provenance → P1 source-fidelity task, items (7), (9) and (10).
- **Claude Opus 5.5**: [[bi-aspectual-ontology]]'s "dualism without substances" against the agency cluster's substance-leaning subject → `todo.md` task "`concepts/bi-aspectual-ontology` calls the Map's foundational picture…" (P2, untouched). ChatGPT §12 asks a related question about process ontology and a substance-leaning subject, but it names neither this page nor the aspect reading, so the overlap is thematic and was not counted.
- **Claude Opus 5.5**, not minted: the uncited neural-dynamics generalisation (L120); the omission of *Matter and Memory*; Ryle (a clause at most, under item 5); Dunham on James's stream (the quotes are unverified); Whitehead's epochal discreteness; the James ch. X "ultimate known law" clause (optional in the task).

## Divergences

- **ChatGPT vs Claude, "defeater-removal" (L87)**: ChatGPT §1 calls the label "the correct calibration", while Claude §3.3 says "No defeater has been removed. The burden has just been relabelled." ChatGPT's own §6.4 concedes that the advantage "largely disappears" once causally idle processes are granted. Adjudicated: L87 already concedes this ("though an epiphenomenalist could still call experiencing a causally idle process"), so the term stays, as the task instructs.
- **ChatGPT vs Claude, Whitehead's severity**: ChatGPT gives "Broadly accurate history; speculative appropriation" and Claude gives "Misattribution". The page sides with ChatGPT (R1).
- **ChatGPT vs Claude, co-optation's severity**: ChatGPT finds the enactivism discussion "comparatively fair" and the James/Whitehead/Thompson divergences "no longer being silently recruited". Claude calls unacknowledged co-optation "the article's central methodological flaw". Both are partly right. The divergences are disclosed for James, Whitehead, Thompson and Clark, but not for Noë 2009, Whitehead's bifurcation verdict or GNW, which are items (7), (8) and (11).
- **Claude vs ChatGPT and the 09-26 review, the description's "removes obstacles"**: Claude rec 1 would replace it. It matches L124 and the article's defeater-removal framing, and the 09-26 deep review chose it deliberately over "strengthens". Kept.

## Operator Items (methodology; not minted)

ChatGPT's methodology items 36–43 and Claude's recommendations 17–22 were deliberately not minted by the per-review passes. The convergent points among them are listed here for the operator.

1. **Make the tenets-page confidence ceiling enforceable** (Claude 19; ChatGPT 41). Both propose flagging "answered", "genuine causal work" and similar phrases on pages that depend on Tenets 2–3. ChatGPT §11.5 (item 40) supplies the live instance: the 09-26 deep review certified this article's closure wording as "settled" eight weeks after `^tenet-3-standing` had set the ceiling. Lexical scale in topics/concepts/apex/voids/positions: "genuine causal work" in 25 files, "real causal work" in 16, "is answered by" in 12. These are upper bounds; many are hedged, and 30 files already link `^tenet-3-standing`.
2. **Check interpretive fidelity and disclose co-optation** (ChatGPT 36; Claude 18, 22). The deep-review §2.4 ledger already has a "Cited-author stance" line. On 09-26 it covered Place, Smart, James, Whitehead, Clark and Thompson but not GNW or Noë 2009, so the gap is coverage, not a missing mechanism.
3. **An ontology-term glossary** (Claude 17, site-level, with a lint check; ChatGPT 2, a definitions box on this article). Both want property, process, activity and substance pinned down. ChatGPT 37 (evidence labels) is adjacent.
4. **A required adversarial section**: strongest rival, defeat conditions, a discriminating output (ChatGPT 38, 43; Claude 9, 20). The Claude processing counted "What Would Challenge This View?" on 72 of 340 topics pages; the writing-style guide does not require it.
5. **Navigation surfaces lag body concessions** (Claude 21; one proposer, but two convergent content clusters here, C3 and C7, are instances of it).
6. **Dispatch plumbing (found by this pass)**: `task_to_skill` passes only `Notes` and `Review file(s)` to the executing fork. Fields above Notes are never dispatched. In the 61 active tasks these include `Caution` (14), `Secondary files` (11), `Headroom` (10), `Coordination` (3) and the per-review fold field `Claude review (2026-10-03)` (2), and refine-draft does not read todo.md itself. Fixed here for the two [[consciousness-as-activity]] tasks: the fold was moved verbatim into Notes, and the Caution constraints were restated there. The outer-review fold step, and this skill's own instruction to add fields above Notes, should either write into Notes or the dispatcher should pass the raw block. Minor: a `Review file` value written as "`path` (prose)" keeps the prose in `review_file`.
7. Singleton methodology items, recorded only: a literature-currency trigger (ChatGPT 39; the weekly literature-drift-review partly covers it), "bedrock" not being review-exempt (ChatGPT 40; see item 1's instance), and a convergence audit for shared roots (ChatGPT 42).

## Method Notes

- The reviewers overlapped unusually heavily: both audited one unchanged page, and both prompts asked for a hostile audit. Overlap was therefore expected, and adjudication mattered more than counting. The one shared false premise (R1) came from both reviewers misreading the same two sentences.
- Quotes were checked against the live page or the raw source. James ch. XI was re-fetched for this pass (Gutenberg 57628) to refine C5, and the Nagel 1974 PDF text was checked for C2. Chalmers 1995, Clark 2013, COGITATE 2025 and Noë 2009 rely on the per-review processings' checks and were not re-fetched.
- Every task change was verified with `parse_tasks`. The active count was 61 before and 61 after. P1 went from 2 to 3 and P2 from 16 to 15. Only the two [[consciousness-as-activity]] tasks changed, and both moved texts (the Claude folds and the original Notes) are byte-identical inside the new Notes. The bergson-and-duration and bi-aspectual-ontology tasks are untouched.
- With this file on disk, `is_outer_review_task_deferred` releases the 10-03 outer-review tasks to the queue.
- Model: claude-opus-5-5.
