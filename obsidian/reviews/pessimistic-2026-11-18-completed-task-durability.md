---
title: "Pessimistic Review - 2026-11-18 - Completed Task Durability"
created: 2026-11-18
modified: 2026-11-18
human_modified: null
ai_modified: 2026-11-18T12:21:32+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-2
ai_generated_date: 2026-11-18
last_curated: null
---

# Pessimistic Review

**Date**: 2026-11-18
**Content reviewed**: the completed-task record (`obsidian/workflow/todo.md` and `obsidian/workflow/archive/completed-tasks-2026-W*.md`) checked against the live pages, for one question set by the driver: do completed repair tasks hold on the page?

## Executive Summary

Mostly yes. In a stratified sample of 83 completed repair tasks from 2026-06-01 to 2026-11-10, 69 quoted a defective string that could be tested; 68 held and 1 did not, and the one failure is the known control (`voids/minimal-consciousness-void`, fixed this morning). Three wider sweeps found two more live failures and one mechanism that explains most of the risk: a task closed "by consolidation" because a sibling task's commit was said to cover it. Two of the 12 testable tasks closed that way kept their flagged sentence (17%), against 1 of 223 for tasks with an explicit old-to-new string that ran under their own commit. No fix was found to have been reverted by a later condense, coalesce or deep review, and no queue-line mismark was found.

Three repairs are listed at the end. None is a fabricated quotation or a tenet-support claim.

## Where completed tasks live, and the population

| Location | Completed blocks (`### ✓`) |
|---|---|
| `obsidian/workflow/todo.md`, between `## Completed Tasks` (L5911) and `## Blocked Tasks` | 181 (71 dated 2026-11; the rest are June to October blocks closed with a status prefix) |
| `obsidian/workflow/todo.md`, above `## Completed Tasks` | 18 |
| `obsidian/workflow/todo.md`, below `## Blocked Tasks` (Vetoed section) | 478 (almost all February to May, outside the window) |
| `obsidian/workflow/archive/completed-tasks-2026-W04.md` to `-W46.md` (42 weekly files) | 10,025 |

Parsed total (archives plus the Completed section): 10,206 blocks. In the window 2026-06-01 to 2026-11-10: 5,206 blocks, of which 4,336 are repair-type (refine-draft 3,009; deep-review 1,130; cross-review 197).

Of the 4,336, a pattern match found 2,208 that quote at least one candidate string and name a file in topics, concepts, voids, apex, tenets or positions. That figure is an upper bound on "tasks that quote a defective string": the match also catches generic deep-review tasks that quote strings to preserve, and link-install tasks. In the sample, 11 of 36 non-outer tasks drawn from this frame turned out to quote no defect at all. A stricter count (a quoted string followed by an arrow, or preceded by the word OLD, and actually found on the page) gives 223 tasks.

## Sampling rule

Frame: the 2,208 tasks above (446 outer-review-sourced, 1,762 not). The 446 outer-sourced tasks were too many to take whole, so the rule was:

- **Stratum A (36)**: outer-review-sourced, 6 per month June to November, drawn at random (seed 20261118) from tasks whose notes mention a tenet-support claim, a quotation or attribution fault, a figure or citation fault, or an over-strong modal.
- **Stratum B (11)**: every frame task closed with a status prefix instead of a plain date (RESOLVED-BY-CONSOLIDATION, DONE-BY-COORDINATED-PASS, DUPLICATE, DONE-OUT-OF-BAND). Taken with certainty because the control case is of this kind.
- **Stratum C (36)**: not outer-sourced, 6 per month, spread 2 concepts, 2 topics, 1 voids, 1 apex, same priority filter, same seed.

Sample size 83. By month: June 16, July 19, August 12, September 12, October 12, November 12. By section of the first file: concepts 30, topics 28, voids 11, apex 11, tenets 2, positions 1.

## Method

For each quoted string and each file the task names, the string was tested (whitespace collapsed, case folded, emphasis marks and wikilink syntax stripped, split on ellipses and slashes) against four versions of the file: three days before the task date, the start of the task date, the end of the following day, and HEAD. A string present before and gone after is counted as fixed in the task window. A string present before, after and now was read in context, in the task notes and on the page, to decide whether it was the defect, a string the task said to keep, or text the fix extended. Every survivor candidate was then read in its full current paragraph.

The first version of the test was case-sensitive and missed the control, because the task quoted "the void exists…" and the page had "The void exists…". The figures below are from the corrected test, which classifies the control as present on 2026-11-17.

## Classified table (sample, 83 tasks)

Stratum A = outer-sourced, B = closed with a status prefix, C = other. "Named commit" = a commit on the task date whose subject contains the task title.

| Date | Stratum | Outer | Named commit | Task (title fragment) | First file | Class | Evidence |
|---|---|---|---|---|---|---|---|
| 2026-06-02 | C | - | Y | Web-verify + cite "seven orders of magnitude" decoherence figure in topics/int | topics/interaction-problem-across-traditions | HELD | 2 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-06-02 | C | - | Y | Deep review apex/contemplative-path.md (~32d since review, ai_contribution=100 | apex/contemplative-path | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-06-02 | C | - | Y | Deep review topics/falsification-roadmap-for-the-interface-model.md (gap ~24d  | topics/falsification-roadmap-for-the-interface-model | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-06-02 | B | Y | - | Mark cessation evidence as n=1 + annotate misapplied Hume passage + currency u | voids/minimal-consciousness-void | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-06-02 | B | Y | - | Narrow modal overreach + soften tenet-bracketing in voids/minimal-consciousnes | voids/minimal-consciousness-void | SURVIVED | CONTROL. "would have a discoverable minimum" removed 2026-06-02 (d81d406843); "The void exists precisely because consciousness is causally efficacious … bidirectional tenet in miniature" on the page until b70b450537, 2026-11-18 |
| 2026-06-03 | C | - | Y | Complete reciprocal back-links into concepts/direction-of-fit.md (asymmetric c | concepts/direction-of-fit | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-06-07 | B | Y | - | Confront the Lakatosian-progressivity incoherence in the duhem-quine article's | topics/duhem-quine-underdetermination-consciousness | HELD | closed by consolidation; concession on the page ("A hard core whose central mechanism remains empirically silent cannot claim the Lakatosian honour…", L118) |
| 2026-06-08 | A | Y | Y | Correct the false TSVF originality claim in the post-decoherence-selection ape | apex/post-decoherence-selection-programme | HELD | 2 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-06-09 | B | Y | - | Fix four web-verified citation defects in concepts/illusionism.md (outer revie | concepts/illusionism | HELD | 3 string(s) removed in window; "Kammerer (2022)" now cites the Moorean paper for the Moorean point (correct use); not a regression |
| 2026-06-10 | A | Y | Y | Fix Husserl "all three" misattribution in apex/conjunction-coalesce.md | apex/conjunction-coalesce | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-06-20 | C | - | Y | Deep review concepts/mind-brain-separation.md (30d since last review, ai_contr | concepts/mind-brain-separation | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-06-20 | A | Y | - | RESOLVED-BY-CONSOLIDATION (commit 04d04bcb): Sharpen accommodation-vs-evidence | topics/consciousness-interface-development | HELD | 1 string(s) removed in window; closed by consolidation (04d04bcbb1); evidential sentence removed, framing paragraph at L45 |
| 2026-06-20 | A | Y | - | RESOLVED-BY-CONSOLIDATION (commit 04d04bcb): Add co-optation footnote + falsif | topics/consciousness-interface-development | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-06-25 | A | Y | Y | Engage Butlin et al. 2023 by name + propagate P-Q3 mechanism-debt + AI-unfalsi | apex/assessing-ai-consciousness-under-the-map | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-06-26 | C | - | Y | Deep review voids/disappearance-voids.md (26d since review — 2026-05-31 placeh | voids/disappearance-voids | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-06-26 | A | Y | Y | Propagate the access/phenomenal calibration to the mental-causation sibling cl | concepts/content-specificity-of-mental-causation | HELD | 2 quoted string(s) gone from 2 file(s) within the task-day window |
| 2026-07-07 | B | - | - | Cross-review topics/graduated-middle-path-valence-modulated-attention.md (fres | topics/graduated-middle-path-valence-modulated-attention | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-07-11 | C | - | Y | Deep review topics/neural-implementation-specifics.md (owed-web-verify seam —  | topics/neural-implementation-specifics | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-07-14 | B | - | - | Sweep residual Denton-2024 "demonstrated" over-claims | topics/neural-implementation-specifics | HELD | 2 string(s) removed in window; closed out-of-band; three files fixed 2026-07-14 (ed3d2494df and siblings) |
| 2026-07-15 | B | Y | - | Correct flagship exposition + citation defects and thin rival field in concept | concepts/trumping-preemption | HELD | 2 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-07-15 | B | Y | - | Note trumping-vs-quantum-selection mechanism tension across concepts/trumping- | concepts/trumping-preemption | HELD | closed by consolidation; the MQI bullet now says the two realisations "are not interchangeable" and the page carries the epiphenomenalist-invisibility passage (L79–L89) |
| 2026-07-16 | C | - | Y | Deep review concepts/causal-powers.md (settled-converged 38d review gap, oldes | concepts/causal-powers | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-07-16 | A | Y | Y | Agency articles — replace the exhaustive trilemma and the near-perfect-predict | positions/agency-and-will | HELD | no exact string; P-A register now calls the trilemma "a non-exhaustive heuristic" and lists the omitted positions (L48) |
| 2026-07-18 | C | - | Y | Deep review topics/eastern-philosophy-consciousness.md — stale cross-cultural  | topics/eastern-philosophy-consciousness | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-07-19 | C | - | Y | Deep review voids/minimal-consciousness-void.md — stale quote-dense void floor | voids/minimal-consciousness-void | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-07-19 | B | - | - | Fix Hofstadter over-attribution in concepts/chinese-room-argument.md — SUBSUME | concepts/chinese-room-argument | HELD | closed as DUPLICATE; the Hofstadter "co-originator" phrase was removed the same day by the sibling task commit 30a6b87255 |
| 2026-07-22 | A | Y | Y | Sync stale flat "AI systems lack consciousness" theses to the scoped bidirecti | apex/apex-articles | HELD | 4 quoted string(s) gone from 3 file(s) within the task-day window |
| 2026-07-22 | A | Y | Y | Resolve the Tenet 3 context-vs-outcome selection tension in tenets/tenets.md ( | tenets/tenets | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-07-25 | B | Y | - | panpsychism.md — correct the Goff/Kastrup dissociation conflation (applied in  | concepts/panpsychism | HELD | 3 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-07-25 | B | Y | - | panpsychism.md — update IIT to 4.0, qualify the C. elegans phi claim, and make | concepts/panpsychism | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-07-27 | A | Y | Y | voids/what-voids-reveal.md — separate epistemic limitation from modal impossib | voids/what-voids-reveal | HELD | no exact string; convergence demoted to coherence, independence-weighted count installed (L102–L110) |
| 2026-07-29 | C | - | - | moral-architecture-of-consciousness.md — the apex inherits none of its cluster | apex/moral-architecture-of-consciousness | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-07-29 | A | Y | Y | parsimony-epistemology.md — an undergraduate thesis carries a load-bearing cla | concepts/parsimony-epistemology | HELD | Hubbard sentence reframed at L63 ("raises exactly that criticism…") |
| 2026-07-29 | A | Y | Y | epistemology.md — the hub infers ontological nonidentity from epistemic asymme | concepts/epistemology | HELD | 3 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-07-31 | C | - | Y | coupling-modes settles as Born-rule-preserving the Stapp-Zeno question the reg | concepts/coupling-modes | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-01 | C | - | Y | the SETTLED SOURCE file in the Hu et al. family is itself unfixed — active-reb | concepts/active-reboot | HELD | 4 quoted string(s) gone from 3 file(s) within the task-day window |
| 2026-08-01 | C | - | Y | WRONG FIRST AUTHOR on a live citation at three loci — the corpus says "Sanford | concepts/bidirectional-interaction | HELD | 3 quoted string(s) gone from 3 file(s) within the task-day window |
| 2026-08-04 | A | Y | Y | the falsification criteria in phenomenology-of-memory-and-the-self cancel them | topics/phenomenology-of-memory-and-the-self | HELD | 9 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-08 | C | - | Y | phenomenology-of-musical-understanding's blurb strips the attribution its own  | topics/phenomenology-of-musical-understanding | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-13 | A | Y | Y | the dissociation pair claims causal-direction evidence it disclaims — neurolog | topics/neurological-dissociations-as-interface-architecture | HELD | 2 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-17 | C | - | Y | research-programme-decisions-under-the-map quotes a P-Q9 sentence deleted on 2 | apex/research-programme-decisions-under-the-map | HELD | 5 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-18 | A | Y | Y | eastern-philosophy-consciousness calls process haecceitism "The Resolution" wh | topics/eastern-philosophy-consciousness | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-19 | A | Y | Y | concepts/knowledge-argument misdescribes Jackson's 2003 reversal and carries t | concepts/knowledge-argument | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-20 | A | Y | Y | apex/apex-articles index: convergent stale-thesis and registry-drift defects — | apex/apex-articles | HELD | 5 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-22 | A | Y | Y | concepts/coupling-modes and the hypnagogia article cite each other as evidence | concepts/coupling-modes | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-22 | C | - | Y | three citation defects in topics/anaesthesia-and-the-consciousness-interface v | topics/anaesthesia-and-the-consciousness-interface | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-08-26 | C | - | Y | voids/creative-aesthetic-void L95 quotes Kant with two words that are not in t | voids/creative-aesthetic-void | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-09-02 | C | - | Y | tenet-check 2026-09-02 Warning 1 — the remaining surface loci (descriptions, a | apex/phenomenology-of-consciousness-doing-work | HELD | 9 string(s) removed in window; named surface loci fixed 2026-09-02; a body echo of "cross-cultural evidence confirms" on the same apex survived until a follow-up task on 2026-09-10 (702c3aaa67) |
| 2026-09-02 | A | Y | Y | tenets/tenets.md L105 Schrödinger analogy says "The brain presents options; th | tenets/tenets | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-09-05 | A | Y | Y | topics/ethics-of-consciousness-invertebrate-question L91 answers aggregation w | topics/ethics-of-consciousness-invertebrate-question | HELD | 3 quoted string(s) gone from 2 file(s) within the task-day window |
| 2026-09-05 | A | Y | Y | concepts/pain-asymbolia — consolidated pass: the article grants the dissociati | concepts/pain-asymbolia | HELD | 5 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-09-07 | C | - | Y | voids/modality-void — the lead premise is denied by its own cited source, the  | voids/modality-void | HELD | 9 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-09-07 | C | - | Y | topics/dualism-as-ai-risk-mitigation — the uncomputability claim contradicts P | topics/dualism-as-ai-risk-mitigation | HELD | 5 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-09-09 | C | - | Y | concepts/penfield-interactionist-dualism holds the wing's outbound-leg clinica | concepts/penfield-interactionist-dualism | UNTESTABLE | no defective string quoted (generic review, link install or additive task) |
| 2026-09-10 | C | - | Y | concepts/categorical-surprise L55/L59 — the Gödel and Tarski appeal establishe | concepts/categorical-surprise | HELD | 4 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-09-16 | A | Y | Y | topics/lucid-dreaming-and-dualist-rendering — the Degradation Asymmetry and Ep | topics/lucid-dreaming-and-dualist-rendering | HELD | 16 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-09-25 | C | - | Y | topics/animal-consciousness L192 imports Tenet 3 into the Occam row the depend | topics/animal-consciousness | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-09-27 | A | Y | Y | concepts/libet-experiments infers "room for consciousness" from 60% classifier | concepts/libet-experiments | HELD | 4 string(s) removed in window; heading now "A Retrocausal Proposal" |
| 2026-09-29 | A | Y | Y | Cross-review — three inbound pages still assert the flat, pre-2026-09-21 const | topics/the-subject-object-distinction-as-philosophical-discovery | HELD | 6 string(s) removed in window; "carry more evidential weight" now conditioned on the routes' independence, as asked |
| 2026-10-01 | C | - | Y | Covert-consciousness ledger batch D: qbism, substrate-independence and degrees | concepts/substrate-independence | HELD | 2 quoted string(s) gone from 2 file(s) within the task-day window |
| 2026-10-03 | A | Y | Y | Give Bidirectional Interaction one quantifier on the epiphenomenalism and AI-e | concepts/epiphenomenalism | HELD | 4 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-10-03 | A | Y | Y | Bring post-decoherence-selection into line with prebiotic-collapse on who actu | concepts/post-decoherence-selection | HELD | 6 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-10-06 | A | Y | Y | topics/vertiginous-question — two sentence-level fixes, LENGTH-NEUTRAL: L125 " | topics/vertiginous-question | HELD | 4 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-10-07 | A | Y | Y | assent-void — four calibration errors verified at source: Williams's status, t | voids/assent-void | HELD | 16 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-10-08 | C | - | Y | concepts/rival-explanations-of-the-explanatory-gap — fresh-create defect tail: | concepts/rival-explanations-of-the-explanatory-gap | HELD | 3 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-10-10 | C | - | Y | apex/attention-as-causal-bridge L187 still calls Schwartz's OCD work "suggesti | apex/attention-as-causal-bridge | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-10-12 | C | - | Y | topics/q3-q4-sliding-boundary-and-transparency-problem L92 says its stabiliser | topics/q3-q4-sliding-boundary-and-transparency-problem | HELD | 6 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-10-20 | C | - | Y | Lower "Every attention void is evidence of mental causation" in voids/attentio | voids/attention-and-consciousness | HELD | 1 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-10-20 | A | Y | Y | concepts/binding-problem L169, L167, L172 — compass and photosynthesis called  | concepts/binding-problem | HELD | L169 now: compass "leading but unsettled… the one surviving precedent"; "photosynthesis no longer serves (P-Q8)" |
| 2026-10-22 | A | Y | Y | concepts/miswanting misses the emotions-as-outcome countermodel (Davis, Love & | concepts/miswanting | HELD | 4 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-10-26 | C | - | Y | "bidirectional (fronto)parietal coherence" (Rajan et al. 2019's directional re | topics/the-interface-problem | HELD | 4 quoted string(s) gone from 3 file(s) within the task-day window |
| 2026-11-01 | C | - | Y | voids/self-transcendence-void L84 quotes Wittgenstein's 1930 ladder remark wit | voids/self-transcendence-void | HELD | 2 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-11-01 | A | Y | Y | topics/quantum-randomness-channel-llm-consciousness verdict is still categoric | topics/quantum-randomness-channel-llm-consciousness | HELD | 13 quoted string(s) gone from 2 file(s) within the task-day window |
| 2026-11-02 | A | Y | Y | voids/cross-state-void — the lede's "what crosses is a *description*" (L37) is | voids/cross-state-void | HELD | 10 string(s) removed in window; "survives disclosure" narrowed to "in one study" as asked |
| 2026-11-03 | A | Y | Y | topics/motor-control-quantum-zeno never engages Bourget's (2004) weakness-of-w | topics/motor-control-quantum-zeno | HELD | 3 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-11-04 | A | Y | Y | topics/phenomenology-of-agency-vs-passivity protects the selection reading wit | topics/phenomenology-of-agency-vs-passivity | HELD | 10 string(s) removed in window; "choosing not to choose" kept but labelled "the Map's gloss" as asked |
| 2026-11-04 | A | Y | Y | topics/phenomenology-of-agency-vs-passivity L143 "Against Illusionism" conclud | topics/phenomenology-of-agency-vs-passivity | HELD | 5 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-11-05 | C | - | Y | apex/process-and-consciousness calls anti-emergentism "the Map's insight" (L79 | apex/process-and-consciousness | HELD | 4 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-11-08 | A | Y | Y | concepts/substance-property-dualism is stale on Chalmers and Jackson, never na | concepts/substance-property-dualism | HELD | 3 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-11-10 | C | - | Y | concepts/causal-closure L98–100 "### Kim's Formulation Dilemma" / "Kim himself | concepts/causal-closure | HELD | 4 quoted string(s) gone from 2 file(s) within the task-day window |
| 2026-11-10 | C | - | Y | Sibling haecceity defects: topics/vertiginous-question L183 "but the indexical | topics/vertiginous-question | HELD | 3 quoted string(s) gone from 2 file(s) within the task-day window |
| 2026-11-10 | C | - | Y | Fold the surgical/pharmacological record into concepts/pain-asymbolia ## What  | concepts/pain-asymbolia | HELD | 2 quoted string(s) gone from 1 file(s) within the task-day window |
| 2026-11-10 | C | - | Y | topics/consciousness-and-social-understanding L77 says the limits of understan | topics/consciousness-and-social-understanding | HELD | L77 now scopes the felt limit ("in some encounters… But felt opacity is only one mode of misfit") |
## The cases that did not hold

### 1. SURVIVED (control) — `voids/minimal-consciousness-void`, task of 2026-06-02

- **Task**: "Narrow modal overreach + soften tenet-bracketing in voids/minimal-consciousness-void.md", from outer reviews 2026-06-02, 3 of 3 reviewers. Instruction: "downgrade 'the void exists precisely because consciousness is causally efficacious / the bidirectional tenet in miniature' to an analogy, since intra-mental attentional modulation is not the mind→matter bidirectional interaction the tenet asserts".
- **How it was closed**: header `### ✓ RESOLVED-BY-CONSOLIDATION (2026-06-02)`. The task never ran. Commit `88526999a8` (2026-06-02 05:43Z, "chore(todo): mark 4 minimal-consciousness-void prose siblings RESOLVED-BY-CONSOLIDATION") closed it two minutes after commit `d81d406843` (05:41Z), whose subject is a different task ("Add overlooked probing strategies + downgrade 'unexplorable'…").
- **What the covering commit did**: it removed the companion sentence ("a purely physical phenomenon would have a discoverable minimum") and it edited the Bidirectional paragraph, changing "it actively participates in and transforms what it examines" to "it transforms what it examines". The next two sentences, the ones the task quoted, were left as they were.
- **The record said so**: the block's own Status line lists what the pass did ("softened the lead and the Dualism site-perspective bullet…") and does not mention the Bidirectional bullet. It ends "Verify in the article before re-queueing." Nothing did.
- **Duration**: on the page from 2026-06-02 to 2026-11-18 (169 days), through two deep reviews of the page (2026-06-05 and 2026-07-19; the second is in this sample, classed UNTESTABLE because it quotes no defect). Removed by `b70b450537` (2026-11-18 06:52Z).
- **Why it did not hold**: closed on a sibling's commit that touched the paragraph and kept the sentence.

### 2. SURVIVED (live) — `topics/consciousness-interface-development`, task of 2026-06-20

Found in the sweep of consolidation-closed tasks, not in the random sample.

- **Task**: "Resolve the infant 'wide-aperture' internal contradiction in consciousness-interface-development.md", from outer reviews 2026-06-20, 3 of 3 reviewers. The notes quote three strings ("This gives infant consciousness broad perceptual access," "more access, less agency," "The infant has access the adult lacks") and instruct: "state unambiguously that it is the interface (not consciousness) that has 'broader/less-filtered access' in infancy, and rewrite every 'infant consciousness has more access' phrasing accordingly".
- **Current sentence** (`obsidian/topics/consciousness-interface-development.md:135`): "No phase represents the "correct" state of the interface; each is a configuration with characteristic capacities and costs. The infant has access the adult lacks, the adult has control the infant lacks, and the elderly person may have a form of integrative breadth that neither possessed."
- **How it was closed**: header `### ✓ 2026-06-20 RESOLVED-BY-CONSOLIDATION (commit 04d04bcb)`, closed by `d7abf2a8d4` (2026-06-20 05:02Z, "auto(queue): close 4 sibling outer-review tasks RESOLVED-BY-CONSOLIDATION"). The covering commit `04d04bcbb1` (05:01Z) carries another task's title ("Update stale developmental-neuroscience claims… (implicit-ToM + age-25 maturity)").
- **What the covering commit did**: it fixed the first two strings (L51 now reads "The infant *interface* offers broad, weakly filtered access… broader discrimination at the interface is not a richer phenomenal field"). At the third it joined three sentences into one with commas and kept the words.
- **Why it did not hold**: the same as case 1. Two of three quoted strings were rewritten; the third was edited for punctuation and left making the claim. L51's stipulation softens the reading, but the subject of L135 is still "the infant", and the task named this sentence.
- **Open task covering it**: none (0 hits for the string above `## Completed Tasks`).

### 3. SURVIVED, one of two asks (live) — `concepts/zombie-master-argument`, task of 2026-09-10

Found in the sweep of tasks with an explicit old-to-new string, not in the random sample.

- **Task**: "`concepts/zombie-master-argument` L44 asserts the physicalist cost tally as fact…". Instruction: "attribute the cost claim to the Map, and soften the universal ('every available block has been attempted' → the blocks the literature has attempted)".
- **Current sentence** (`obsidian/concepts/zombie-master-argument.md:46`): "…to resist the conclusion, the physicalist must block at least one step, and every available block has been attempted, each, on the Map's assessment, at significant theoretical cost."
- **Completing commit**: `ded0e88f7c` (2026-09-10 02:36Z). Its subject names this task. It inserted "on the Map's assessment," and left "every available block has been attempted".
- **Why it did not hold**: a two-part instruction; the part named in the task title was done and the second part was not. The task's lesser locus ("Fürst's reversal showing" → now "arguing", L112) was done.
- **Open task covering it**: none.

### 4. Skipped and recorded (not a failure) — `topics/clinical-dissociation-as-systematic-evidence`, task of 2026-10-08

"isolate a recurrent factor" and "distinct from any failure of content retrieval" (L92) are still on the page verbatim. The task marked them "as budget allows", the page was over its hard gate (4,687 now), and the completing pass wrote the five skipped items into an open block: `### NEEDS-HUMAN (length budget) 2026-10-08` in `todo.md`, which names item (11) and the Simeon et al. 2008 reference. This is the pattern working as intended, and it is listed here only because a string test alone would call it a survivor.

### 5. PROPAGATED — fixed on the named page, verbatim on a sibling

391 distinctive strings (six words or more) that a sampled or old-to-new task removed were searched for across topics, concepts, voids, apex, tenets and positions. Four were found verbatim on a page the task did not name. Two are defects:

- **`topics/free-will:153`** still has "Meditation reveals that consciousness can *refrain from selecting*.", which the 2026-11-01 task on `concepts/attentional-economics` changed to "Meditation suggests, on the Map's reading, that…". An open P3 task minted the same day already covers it (`todo.md` L2624). Not listed below.
- **The Cai et al. (2024) reference.** The 2026-11-03 task on `topics/motor-control-quantum-zeno` (commit `8061e31d22`) replaced "Cai, X., Liu, C. & Kaeser, P.S. (2024)." with "Cai, X., Liu, C., Tsutsui-Kimura, I., et al. (2024).", recording that Crossref lists 14 authors with Kaeser last. The three-author form is still at `concepts/motor-selection:245` and `apex/phenomenology-mechanism-bridge:198`. A worse variant, with the last author printed as first author, is at `concepts/attention-as-interface:268` ("Kaeser, P.S. et al. (2024)."), and five archived pages have "Kaeser, P.A., et al. (2024)." No open task covers any of these (0 hits for "Kaeser" above `## Completed Tasks`). Listed below.

The other two (`apex/one-world-wager:54`, `apex/assessing-ai-consciousness-under-the-map:116`) carry the string in a context where it is correct.

No REGRESSED case was found. One string looked like one ("Kammerer (2022)" on `concepts/illusionism`, removed 2026-06-09, present now); the current use cites the Moorean paper for the Moorean point, which is what the task asked for.

## Rates

**Sample (83 tasks; 14 UNTESTABLE excluded; 69 testable)**

| Group | Testable | HELD | HELD-INCIDENTALLY | SURVIVED | SURVIVED-VARIANT | REGRESSED |
|---|---|---|---|---|---|---|
| All | 69 | 68 (98.6%) | 0 | 1 (1.4%) | 0 | 0 |
| (i) Outer-review-sourced (44 sampled, 2 untestable) | 42 | 41 (97.6%) | 0 | 1 (2.4%) | 0 | 0 |
| (ii) Multi-file (strings removed from two or more files) | 13 | 13 (100%) | 0 | 0 | 0 | 0 |
| (iii) No commit on the task date naming the task (14 sampled, 4 untestable) | 10 | 9 (90%) | 0 | 1 (10%) | 0 | 0 |
| Plain-dated closure, own commit | 59 | 59 (100%) | 0 | 0 | 0 | 0 |

The single SURVIVED is the control, which entered through stratum B, taken with certainty. In the 72 randomly drawn tasks (strata A and C, 60 testable) nothing survived.

**Sweep 1: tasks with an explicit old-to-new string (whole window, not a sample).** 223 tasks, 491 string-and-file pairs. 403 pairs (82%) were removed in the task window; 11 were already gone at the start of the task date; 8 were new text; 69 were still present after the task. All 69 were read against the task notes: 66 are cases where the new text contains the old (a clause appended, a wikilink piped over existing words) or the string was quoted as something to keep; the other 3 are one string in case 3 above and two in case 4 (one skipped and recorded, one marked optional). At task level: 1 untracked survivor in 223 (0.4%).

**Sweep 2: tasks closed without running (whole window).** 61 repair tasks carry a closure prefix or a status line saying a sibling pass covered them. All 61 are dated June or July; the practice of closing a block this way appears to stop after July. 34 are refine-drafts with a resolvable file; 12 of those quote a defective string that was on the page. 10 held and 2 survived (cases 1 and 2): 17%.

**Sweep 3: commit naming.** 129 of 4,336 repair tasks (3.0%) have no commit within a day of the task date whose subject contains the first 45 characters of the title. 48 further plain-dated refine-drafts from that group were probed; the six title-quoted defects checked on the page had all been fixed. No case was found where a commit named one task and completed another.

**What these numbers support.** A task that ran under its own commit and quoted its defect almost always removed it: 59 of 59 sampled, and 222 of 223 in sweep 1. A task closed on the strength of a sibling's commit is much less safe, on small numbers (2 of 12). The sample cannot support a claim about UNTESTABLE tasks (generic deep reviews, additive tasks, link installs), which are 14 of 83 here and roughly a quarter of the 2,208-task frame; a deep review that "verified" a page is not tested by this method at all, and two such reviews passed over the control sentence. The test is at string level. A reworded sentence that still makes the withdrawn claim would be classed HELD unless it was one of the roughly 40 current sentences read in full; none of those was a variant survivor.

## Mechanisms

| Mechanism | Count | Cases |
|---|---|---|
| Closed by consolidation: a sibling task's commit is recorded as covering the task; that commit edited the paragraph and kept the flagged sentence | 2 | `voids/minimal-consciousness-void` (2026-06-02, fixed 2026-11-18); `topics/consciousness-interface-development` (2026-06-20, live) |
| Two-part instruction, one part applied, task marked complete | 1 | `concepts/zombie-master-argument` (2026-09-10, live) |
| Fix applied to the named page, same string left on pages the task did not name | 2 found | `topics/free-will` (tracked by an open P3); Cai et al. reference on three live pages and five archived ones (untracked) |
| Later condense, coalesce or deep review reintroducing a fixed string | 0 | — |
| Completion marked by a cycle that ran a different task | 0 | — |

Both consolidation failures share three features: the task came from an outer review with all three reviewers agreeing; it quoted several strings; and the covering commit fixed some and edited around the rest.

## Priority List

Three repairs. Each sentence was re-read at HEAD today and checked for an open task.

### 1. `topics/consciousness-interface-development` L135 still attributes the wider access to the infant, not to the infant's interface

- **File**: `obsidian/topics/consciousness-interface-development.md` (one file).
- **OLD** (count 1): "The infant has access the adult lacks, the adult has control the infant lacks, and the elderly person may have a form of integrative breadth that neither possessed."
- **What the original task asked** (2026-06-20, 3 of 3 outer reviewers): state that the interface, not consciousness, has the broader or less-filtered access in infancy, and rewrite every phrasing that says otherwise. This is the third of the three strings it quoted; the other two were fixed.
- **NEW**: "The infant's interface filters less than the adult's, the adult has control the infant lacks, and the elderly may have a form of integrative breadth that neither possessed."
- **Length**: 3,988 by `analyze_length` against the topics hard gate of 4,000 (fires at >=), so 11 words of headroom. The NEW above is net-zero (+1 for the first clause, −1 for "person"). Check that "neither possessed" still reads correctly after the change of subject.
- **Open task**: none.

### 2. The Cai et al. (2024) reference has the wrong author list on three live pages

- **Files**: `obsidian/concepts/motor-selection.md` (L245), `obsidian/apex/phenomenology-mechanism-bridge.md` (L198), `obsidian/concepts/attention-as-interface.md` (L268). Then the archive tree: `archive/concepts/attention-motor-quantum-interface.md`, `archive/topics/attention-disorders-and-quantum-interface.md`, `archive/topics/attention-motor-quantum-selection.md`, `archive/topics/the-interface-location-problem-revisited.md`, `archive/concepts/dopamine-selection-interface.md`, and reference 1 of `obsidian/research/dopamine-attention-motor-quantum-interface-2026-01-24.md` (L220; its 2026-08-08 correction note at L25 may already say enough).
- **OLD**: on the first two pages, "Cai, X., Liu, C. & Kaeser, P.S. (2024)." (count 1 each). On `attention-as-interface`, "Kaeser, P.S. et al. (2024)." (count 1), which prints the last author as first author. In the archive, "Kaeser, P.A., et al. (2024)." (wrong initial as well).
- **What the original task asked** (2026-11-03, on `topics/motor-control-quantum-zeno` only): replace the three-author form with the form below, on a Crossref record of 14 authors, first Cai, Liu, Tsutsui-Kimura, last Kaeser (doi 10.1038/s41586-024-08038-z).
- **NEW**: "Cai, X., Liu, C., Tsutsui-Kimura, I., et al. (2024)." everywhere, matching `topics/motor-control-quantum-zeno` L156. This review used no outside source, so the author list rests on the 2026-11-03 task's recorded check; re-read the Crossref record before editing. Check each page's body for an in-text citation that follows the old first author.
- **Length**: `concepts/motor-selection` 3,497 against 3,500, so the +1 lands on 3,498 with one word to spare; if the count comes out higher, "Cai, X., Liu, C., et al. (2024)." is −1. `apex/phenomenology-mechanism-bridge` 4,935 against 5,000 (+1). `concepts/attention-as-interface` 3,467 against 3,500 (+4). Not net-zero, but inside every gate. Archive pages have no gate.
- **Open task**: none.

### 3. `concepts/zombie-master-argument` L46 still says every available block has been attempted

- **File**: `obsidian/concepts/zombie-master-argument.md` (one file).
- **OLD** (count 1): "and every available block has been attempted, each, on the Map's assessment, at significant theoretical cost."
- **What the original task asked** (2026-09-10): attribute the cost claim to the Map (done) and soften the universal to the blocks the literature has attempted (not done).
- **NEW**: "and each block the literature has attempted carries, on the Map's assessment, significant theoretical cost."
- **Length**: 3,217 against the concepts hard gate of 3,500. The NEW is one word shorter.
- **Open task**: none.

Not listed, because an open task already covers the sentence: `topics/free-will` L153 (P3, 2026-11-01) and `topics/clinical-dissociation-as-systematic-evidence` L92 (NEEDS-HUMAN length block, 2026-10-08).

## For the operator

Observations, not tasks.

- **The risk sits in one closure type.** Every failure of the control's kind found here was a block closed "by consolidation" on a sibling's commit. There are 61 such closures in the window, all in June and July. The 12 that quote a defect have now been checked; the other 22 refine-drafts with a file quote none and were not checked beyond a grep for some of the additions they asked for.
- **The closing record already knew.** The control's Status line listed what the covering pass had done, left out the Bidirectional bullet, and ended "Verify in the article before re-queueing." A closure that copies the task's quoted strings and greps each one at close would have caught both consolidation failures.
- **Quoted strings make completion checkable.** For 223 tasks the notes carry an explicit old string, and a mechanical test of "is the old string gone, or does the new text contain it" settled 422 of 491 pairs without reading; the other 69 needed the task notes read. Tasks written that way are the ones that can be audited after the fact.
- **A string test needs three normalisations to be trusted.** Case (the control was missed by a case-sensitive test), emphasis marks inside the quoted string (the task wrote `*precisely because*`), and two strings joined by a slash in one pair of quotation marks. Without all three the control reads as fixed.
- **Skips for length were handled well where a block was written.** The clinical-dissociation pass wrote its five skipped items into a NEEDS-HUMAN block with the reasons. The zombie-master pass skipped one clause and wrote nothing.
- **Deep reviews do not re-test old findings.** Two deep reviews of the control page ran while the sentence stood. Neither task quoted it, and a review working from the current page has no reason to know a past task claimed to have removed it.
- **Published completed-task files overstate.** The weekly archives are synced to the site. Yesterday's synthesis noted that an outside reviewer built its picture of a page from them; a block headed RESOLVED is read as a fix.

## What was not tested

- Tasks that quote no defective string: generic deep reviews, additive tasks (add a caveat, add a rival), link installs. 14 of the 83 sampled.
- Research notes, `project/` pages and `arguments/` pages as targets (the frame was topics, concepts, voids, apex, tenets, positions).
- The other 2,125 frame tasks beyond the sample, except through the three sweeps.
- Variant survival at scale: about 40 current sentences were read in full; the rest of the HELD class rests on the string being gone.
- Whether each removal was made by the task's own commit or by a same-day sibling: the window test does not separate them. About 20 were checked by diff.
- Sibling propagation for strings shorter than six words, and for paraphrases.
- The `hugo/content` copies, except for the three live survivors (each matches its obsidian source).
- Whether the fixes are philosophically right. This review asked only whether what a task said it removed is gone.
- The Cai author list against Crossref (no outside source was used).

## Critiques by Philosopher

Not applicable to this lens. The review audits the task record against the pages and takes no position on any argument.

## Strengths

- Tasks that ran under their own commit and quoted their defect held in 59 of 59 sampled cases, including all 13 multi-file tasks.
- No fix was found to have been undone by a later condense, coalesce or deep review.
- Later tasks (from about August) carry exact old strings with grep counts, which is what made this audit possible.
