---
title: "Outer Review Synthesis - 2026-10-01"
created: 2026-10-01
modified: 2026-10-02
human_modified: null
ai_modified: 2026-10-02T01:54:16+00:00
draft: false
description: "Cross-review synthesis of 2 outer reviews from 2026-10-01 on Neural Correlates of Consciousness. Identifies findings flagged by multiple reviewers and upgrades their task priority."
topics: []
concepts: []
related_articles:
  - "[[project]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-01
last_curated: null
synthesizes:
  - reviews/outer-review-2026-10-01-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-10-01-claude-opus-5-5.md
synthesis_coverage: "2/3"
---

**Date**: 2026-10-01
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 2 of 3 commissioned reviewers contributed: ChatGPT 5.6.sol Pro and Claude Opus 5.5. The Gemini 2.5 Pro Deep Research leg was abandoned at 2026-10-02T01:23Z. It had been stuck for about 21 hours on "Researching 23 websites…", with its last thinking step "Extracting Document Content for Technical Review", and it never produced a report. No Gemini position is recorded or inferred anywhere below.
**Subject**: `concepts/neural-correlates-of-consciousness`, chosen by the recent-aged fallback. The page was last substantively revised on 2026-09-24. Its only change since the reviews is commit d63adb3824 (2026-10-01 08:05Z), which piped "compatible with all three" at L77 to the new [[inference-to-the-best-explanation-against-dualism]] page. It now has 3,419 words by `analyze_length`, against the concepts hard gate of 3,500 (`>=`).

## TL;DR

Both reviewers recommend major revision, and they reach almost the same diagnosis independently. The article's one secure thesis, that correlation does not entail identity, is correct. Around it, though, the page credits a real IEP sentence to the SEP, misattributes and reverses the covert-consciousness figures, conflates Koch et al.'s background conditions with the full NCC, and treats compatibility as prediction and as "support". It also offers four falsifiers that cannot discriminate between the rival views. **Eight convergent clusters were verified against the live page and primary records; none was rejected outright.** Two parts of clusters were trimmed in adjudication: the reviewers' shared wish to delete the No Many Worlds section, and their shared addition of "bilateral" to the V4 correction. The eight open NCC tasks were merged into six, each now P1 (five upgraded from P2, one already P1), with a combined length plan that fits the page's 80 words of headroom. One cluster, the structural separation of survey from interpretation, was recorded but not tasked.

## Adjudication before clustering

Every cluster below was checked against the live `obsidian/concepts/neural-correlates-of-consciousness.md` at 2026-10-02 01:36Z. Where a claim concerned a source, it was checked against the primary record. Raw-HTML or API retrievals made for this synthesis:

- **IEP vs SEP.** `iep.utm.edu/dualism-and-mind/` contains "As for correlation, interactionism actually predicts that mental events are caused by brain events and vice versa, so the fact that perceptions are correlated with activity in the visual cortex does not support materialism over this form of dualism." This is Scott Calef's entry, §7.d "The Correlation and Dependence Arguments". The live SEP *Dualism* entry has 0 hits for "actually predicts", "visual cortex" and "vice versa". It does contain "Hence interactionism violates physical closure after all", but as an argument it reports and then answers through Mills. Claude presented the sentence as the SEP's own statement, which is slightly too strong.
- **Koch et al. 2016.** The publisher page for doi:10.1038/nrn.2016.22 has Key Points reading "The neuronal correlates of consciousness (NCC) are the minimum neuronal mechanisms jointly sufficient for any one specific conscious experience." It then distinguishes full NCC, content-specific NCC and "background conditions (factors that enable consciousness, but do not contribute directly to the content of experience — for example, arousal systems …)". The abstract has "the minimum neural mechanisms sufficient for any one specific conscious percept" and the posterior-hot-zone localisation. This **corrects the Claude collecting pass**, which said "jointly sufficient" was Koch's 2004 wording only. ChatGPT was right that the 2016 review uses it. It also shows that the article's L55 quotation splices the two 2016 wordings.
- **Chalmers 2000** (consc.net/papers/ncc2.html). The first-pass formulation is the ASSC "correlates directly". §4 "Overall definition" gives the minimal-sufficiency-under-conditions-C definition. The paper separates question (2), what an NCC is, from question (5), whether consciousness is reducible to its NCC. Each reviewer described one half (see Divergences).
- **Bouvier & Engel 2006** (Europe PMC abstract): 92 cases; "The severity of color vision deficits of the cases varied greatly"; deficits "often incomplete and never restricted to color vision". The abstract does **not** say "bilateral". Both reviewers add that word (ChatGPT's suggested replacement text; Claude's "usually needs bilateral damage for full loss"). It is a correlated, unverified addition and the task does not carry it.
- **Covert consciousness.** The figures were checked against the canonical page `topics/covert-consciousness-and-cognitive-motor-dissociation#the-numbers-and-their-denominators`, not against either reviewer. ChatGPT's Bodien figure (60 of 241, 25%) is right, but ChatGPT did not notice the Kondziella misattribution. Claude's Kondziella correction (14% of VS, 32% of MCS, "roughly 15%") is right, but its "covert-awareness rates are already established at 14–25%" overclaims. The canonical page treats these as detection rates whose true value "is unknown", and says Aubinet 2025's "up to 25%" is "not a CMD rate". That overclaim had been copied into the falsifier task's note and has been corrected there.
- **Koch's reading of COGITATE.** Both reviewers say it has no source, and that is true. The reading itself is real: Reuters (Will Dunham; the syndicated copy is dated 1 May 2025) quotes Koch: "Here, the evidence is decidedly in favor of the posterior cortex." The fix is to cite it, not delete it.
- **Bajwa et al. 2025** (Europe PMC abstract): of 52 attempted awakenings from deep propofol sedation, 24 gave reports of experience and 5 gave reports of none. PCIst and LZc did not differ between dreaming and non-dreaming periods. This confirms ChatGPT §4.7 and qualifies Claude's Sarasso-based claim (see Divergences).
- **Tallis.** The PDCnet record is "Tallis in Wonderland: The Illusion of Illusionism", *Philosophy Now* 161, 58–59.
- **Sibling pages, checked live**: `illusionism` L91 (the bare regress "assumes 'seeming' is itself phenomenal"); `conscious-vs-unconscious-processing` ("Where the Physicalist Reading Stops"; "Why the Physicalist Reading Fails" has 0 hits; L193); `palette-extension-void` L50 (Fong et al. 2025); `observation-and-measurement-void` L122 ("The void is self-sealing.") and L96 (Michel 2021 calibration); `terminal-lucidity-and-filter-transmission-theory` L140; `positions/quantum-interface` P-Q2 (L64) and P-Q9 (L141); `filter-theory` ("metabolically expensive", "discriminates no better than the imaging"); `global-workspace-theory` (6 hits for Naccache).

**Disputed claims excluded from clustering.** ChatGPT §7.6's "July internal deep review" does not exist: the NCC deep reviews are dated 03-26 and 03-27, and "honest falsifiability conditions" appears in none of them. ChatGPT §4.8 and §9.5 place the Map's out-of-gamut coverage in `observation-and-measurement-void`; it is in `palette-extension-void`, so the substance stands and the location does not. Claude's fix 18 quotes "explains how dualism accommodates…" from filter-theory, which has 0 hits for it. Claude's fix 24 says the IIT page lacks the pseudoscience dispute, which is false. Claude's fix 20 needs no change. None of these affected a cluster count.

**Independence.** Both legs read the live article and the changelog. ChatGPT ran first. The Claude prompt reused the subject but not ChatGPT's findings. The source work was separate: Claude found the IEP origin and the Kondziella figures, while ChatGPT found Bouvier & Engel, Bajwa, Naccache and the Tallis title. Both cited Koch et al.'s background-conditions taxonomy, but each did so independently from the publisher page. So the overlap in diagnosis is not an artefact of shared retrieval.

## Convergent Findings

### 1. The "Interactionism actually predicts…" quotation is not the SEP's
- **Flagged by**: chatgpt, claude
- **Verification**: Clean (raw-HTML grep of both encyclopedias, above). The quotation is real and verbatim in the IEP; the only change is a capital I. ChatGPT's "untraceable or fabricated quotation" verdict is superseded by Claude's location of the source. Both reviewers agree it cannot stand as an SEP quotation.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "I could not recover that sentence from the current *Dualism* entry, from the archived version checked, or through an exact-phrase search."
  - **Claude Opus 5.5**: "appears in the **Internet Encyclopedia of Philosophy**, "Dualism and Mind"."
- **Task action**: Already P1, so no upgrade was available. The task was retitled and rewritten as "Re-attribute the 'Interactionism actually predicts…' quotation … to the IEP (Calef, §7.d), qualify 'predicts', and name the closure objection the SEP actually discusses". It also corrects the research note at L90 and L170.

### 2. Compatibility is reported as prediction, and the physicalist's real arguments are missing (likelihood, IBE, causal closure)
- **Flagged by**: chatgpt, claude
- **Verification**: Clean. L81 and L154 ("both physicalism and interactionism predict exactly the correlations NCC research discovers") are present. The page has 0 hits for "exclusion", "Papineau" and "Kim", and "closure" appears only in falsifier 4 as gap closure. The IBE half was **already acted on**: the research and expand-topic chain harvested from ChatGPT §5.1 finished on 2026-10-01, creating [[inference-to-the-best-explanation-against-dualism]] (piped at NCC L77), and its cross-review is ✓. Those completed tasks were not resurrected.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "**Generic interactionism does not predict “exactly the correlations” found by NCC research.**" and "The article attacks a conspicuously weak inference while neglecting the cumulative causal and abductive case."
  - **Claude Opus 5.5**: ""Both physicalism and interactionism predict exactly the correlations NCC research discovers" is false on any likelihood-sensitive reading." and it names "the causal-closure argument (Papineau) and the SEP's statement that interactionism "violates physical closure after all"".
- **Task action**: Folded into existing tasks, so no new task was created. The L81 "predicts" clause and the closure clause went into the cluster-1 P1. The L154 "predict exactly" wording went into the Illusionism/Dualism task (P2→P1, cluster 6).

### 3. Definition, lead, V4 and COGITATE are imprecise or unsourced
- **Flagged by**: chatgpt, claude
- **Verification**: Clean on every sub-point, using the publisher Key Points, consc.net, the Bouvier & Engel abstract, the COGITATE abstract (checked by the Claude collecting pass) and the Reuters copy. Sub-findings:
  - L55 folds arousal systems into the full NCC.
  - Chalmers 2000 is never used.
  - The L51 lead presents the IIT-aligned posterior-hot-zone localisation as an established finding.
  - The L59 V4 claim is categorical.
  - L63 reports neither the preregistered outcomes nor the substance of the GNWT reply, and gives Koch's reading no source.
  - The L109 hippocampal-binding claim has no source (ChatGPT §4.9; Claude §2.1, unreferenced-claims row).

  "Bilateral" was trimmed as unverified.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The opening is substantially Koch’s operational formulation wearing a Chalmers citation in the reference list." It also says the hot zone is "an influential hypothesis, not an established general finding", and that Koch's "particular post-result interpretation cannot simply be placed in his mouth without a source".
  - **Claude Opus 5.5**: "The article folds brainstem/thalamic arousal into "full NCC", which is the very conflation the review was written to remove." It also says "Present it as an IIT-aligned, contested hypothesis." and "Source the Koch reading or delete it."
- **Task action**: Upgraded P2→P1: "Definition, lead, V4 and COGITATE precision in neural-correlates-of-consciousness …". Three tasks were combined into one: the Claude definition/lead/COGITATE task absorbed the ChatGPT empirical-precision items (a) V4 and (c) Koch reading, and the ChatGPT cross-review item (a) Naccache, which edited the same paragraphs (L59 and L63).

### 4. Covert consciousness: misattributed figure, reversed direction, inference against no one
- **Flagged by**: chatgpt, claude
- **Verification**: Clean against the canonical page. Kondziella 2016 reports 14% of VS and 32% of MCS ("roughly 15%"). Claassen 2019 reports 15%. Bodien 2024 reports 60 of 241 (25%) without observable command-following. "Up to 25%" is Aubinet 2025's broader figure. Each reviewer's own additions were trimmed: ChatGPT's proposed fix would have kept the misattribution in place, and Claude's "established at 14–25%" was dropped. The canonical page itself is completed work harvested from ChatGPT §4.4 (✓ 2026-10-01).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The claim that “subsequent work” gives estimates around 15% is out of date." and "The article therefore argues against a position few serious physicalists hold: that consciousness is identical to behavioural output."
  - **Claude Opus 5.5**: "The article has the direction of the controversy backwards." and "This attacks a target nobody holds."
- **Task action**: Upgraded P2→P1 as part of the filter-section task (clusters 4 and 5 share the L113–122 bullets). The ChatGPT empirical-precision item (b) was merged in, and its driver-added **Ledger** field was moved with it unchanged apart from a provenance note.

### 5. The filter section's "support" heading survives its own concession; Santander and the DMN bullet are co-opted
- **Flagged by**: chatgpt, claude
- **Verification**: Clean. The L115 heading, L118 (Santander) and L119 (DMN) were checked against L122's own concession ("callosal integration as a generator needing only a thin posterior channel"; "cannot honestly be cited as independent confirmation") and against filter-theory's metabolic concessions. Both reviewers also attack the Borrowed Tooling subsection at L91–95 on different grounds: ChatGPT says "“Our tenet rejects it” is not evidence against it." while Claude says "**DEMOTE**: off-topic for this concept page." The merged task condenses that subsection as the page's funding source.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "But it leaves the heading “Several findings support this reading” and then restores broader pro-filter rhetoric elsewhere." It also says "“Dissolves the Default Mode Network” is a journalistic metaphor, not an adequate description of the measured result."
  - **Claude Opus 5.5**: "Listing it under "Several findings support this [filter] reading" turns a channel-dependence result, where unity tracks surviving fibres, into transmission support." It also says "No production theory identifies the DMN as the generator of consciousness."
- **Task action**: Upgraded P2→P1: "Filter-theory section of neural-correlates-of-consciousness: demote 'support' to compatibility, replace the covert-consciousness figures with the canonical anchor, fix the covert, Santander, DMN and anaesthesia readings". This was two tasks (the Claude filter task plus the ChatGPT empirical-precision item (b)), now one.

### 6. The illusionist regress ignores Frankish's reply, and the opacity inference ignores Type-B physicalism
- **Flagged by**: chatgpt, claude
- **Verification**: Clean. L126 runs the bare regress, while `illusionism` L91 already rejects it. Grep finds 0 hits for "Type-B" and "phenomenal concept". Frankish, Levine and Dennett are orphan references. Tallis is the only voice against illusionism, and his reference lacks the column title and issue (PDCnet confirms both).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "But the article cannot refute it simply by reinstating phenomenal seeming as a premise." and "It begs the question against the phenomenal-concept strategy and other Type-B physicalist positions."
  - **Claude Opus 5.5**: "Frankish's quasi-phenomenal-property reply to the "seeming must be phenomenal" regress is not addressed." and "Only Type-A physicalism is mentioned."
- **Task action**: Upgraded P2→P1: "Illusionism and Dualism sections of neural-correlates-of-consciousness: replace the bare seeming-regress with Frankish's reply, add the Type-B reply to the opacity inference, fix the Tallis reference". It absorbed the ChatGPT empirical-precision item (d) (Tallis) and the tenet-verb task's item (d) (the L156 verb), so the L154–156 Dualism paragraph now has a single owner.

### 7. None of the four falsifiers discriminates, and the honest statement is that generic interactionism is not NCC-falsifiable
- **Flagged by**: chatgpt, claude
- **Verification**: Clean. L143–148 were read in full, along with `palette-extension-void` L50 (Fong 2025, against falsifier 2), `terminal-lucidity…` L140 (against falsifier 3), and P-Q2 and P-Q9 (against the L148 "genuine empirical risk"). Both reviewers say Type-B physicalism predicts the persistent opacity that falsifier 4 relies on.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "None of the article’s four conditions meets that standard." and "The article should admit that **bare dualism is probably not directly falsifiable by ordinary NCC data**."
  - **Claude Opus 5.5**: "Unreachable threshold." (falsifier 1) and "The honest statement is: *on the Map's current commitments, no NCC result can disconfirm interactionism.*"
- **Task action**: Upgraded P2→P1: "Rewrite all four falsifiers in neural-correlates-of-consciousness …". It absorbed the ChatGPT cross-review item (b) (falsifier 2) and now takes falsifier 4. The old note claimed the Type-B task covered falsifier 4, but that task never named L146.

### 8. The tenet-relation section overclaims: the retracted "genuinely causal" sentence, MQI inflation, the No Many Worlds verb, the Occam non sequitur, and the imported measurement-void conclusion
- **Flagged by**: chatgpt, claude
- **Verification**: Clean on all five loci (L160, L164, L168, L172 and L178). The L160 retraction on the sibling was checked live. The void's "self-sealing" and its Michel calibration reply were checked live. The theory count at L172 has no source; both reviewers note this, and Kuhn 2024 is already cited on `duhem-quine-underdetermination-consciousness`. **Trimmed in adjudication**: both reviewers would delete the No Many Worlds section (and Claude the Occam section). `pessimistic-2026-06-01-neural-correlates-of-consciousness` L30 judged the MWI paragraph to be honest framework-boundary marking that "the reader should not mistake … for an in-framework argument". What survives is the closing "This supports No Many Worlds", which reads as an in-framework argument. The paragraph stays and the verb is downgraded.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The NCC article therefore upgrades evidence that its own neighbour correctly treats as non-discriminating." It also says "The posterior cortical hot zone does not become a plausible quantum interface merely because the Map needs an anatomical location.", calls the Occam move "That is a theory-family fallacy", and says "the NCC article imports only the conclusion."
  - **Claude Opus 5.5**: "The NCC article, last modified 2026-09-24, still carries the retracted inference and a Further Reading gloss that predates the retraction." It also says "NCC has no bearing on MWI, and the indexical question is world-count-neutral.", "Preregistered falsification of two theories *is* progress." and "Imported void claim."
- **Task action**: Upgraded P2→P1: "Recalibrate the tenet-relation verbs in neural-correlates-of-consciousness: functional-dissociation sentence, MQI coherence inflation, No Many Worlds verb, Occam non sequitur, imported measurement-void claim". It absorbed the ChatGPT cross-review item (c) (L160). L178, which both reviewers flagged but neither collecting pass turned into a task, was added here instead of minting a new task.

### 9. Separate the neutral survey from the Map's interpretation (structural)
- **Flagged by**: chatgpt, claude
- **Verification**: The diagnosis is clean; it is the sum of clusters 2, 5, 7 and 8.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Separate neutral survey from site interpretation visually."
  - **Claude Opus 5.5**: "Restructure as a neutral concept page plus one clearly fenced "Map's reading" section"
- **Task action**: Recorded only; no task. A restructure cannot fit in 80 words of headroom. The six P1 tasks apply the same recalibration where the problems are, which delivers the effect without reorganising the page. If the page still reads as tenet-led after they land, a condense task is the route.

## Length plan (the six tasks against 80 words of headroom)

The page has 3,419 words; the hard gate is 3,500 `>=`, so the ceiling is 3,499 and the headroom is 80. Each task carries its own net budget and its own named funding in its Notes, so the plan holds in any execution order.

| Task (all P1) | Net budget | Named funding |
|---|---|---|
| IEP quotation, "predicts", closure (L79–81) | ≤ +15 | L81 lead-in sentence (20 words), which restates the quotation |
| Definition, lead, V4, COGITATE (L51–63) | ≤ +20 | L109 hippocampal-binding sentence (30; unsourced and flagged by both) with its Further Reading gloss; the orphan Dennett reference (9); the L51 rhetorical question (13); Naccache carried by link with no reference entry |
| Illusionism and Dualism (L124–128, L154–156) | ≤ +10 | condense the regress fork and the Tallis sentence; delete "we would expect … intelligible" (16); no new references |
| Falsifiers (L139–148) | ≤ +5 | trade words within the 268-word section; deleting falsifier 3 frees about 45 |
| Filter section (L91–95, L113–122) | ≤ −20 (target −30) | **the page's funding source**: Borrowed Tooling subsection 152 words → a pointer of one or two sentences; covert bullet about −35 |
| Tenet-relation verbs (L158–172, L178) | ≤ −20 | MQI fold (about −24); Occam reduction (about −30); L160 shrinks |

- **Worst-case peak.** If all four growth tasks run first, the page reaches at most 3,419 + 50 = **3,469**, which is 31 words under the gate.
- **Final ceiling.** The ceiling is 3,419 + 10 = **3,429**. The expected landing is about 3,400–3,420.
- **Additions left out.** Three proposed additions were judged not worth their words and left out of the tasks: ChatGPT's COGITATE prediction table (about 150 words), ChatGPT's broadened ten-theory taxonomy, and Claude's full reference-completion list.

## Singleton Findings

Findings flagged by only one reviewer. Where a task already contains one, it is noted; otherwise it is not tasked.

- **ChatGPT 5.6.sol Pro**: the "three possibilities" taxonomy omits token identity, functionalism, Russellian monism and idealism (§1). Not tasked; this is cluster 9 territory.
- **ChatGPT 5.6.sol Pro**: L160's "NCC strongly supports physical→mental causation" sits badly beside the article's mere-correlation framing (§1). An optional item in the tenet-verb task.
- **ChatGPT 5.6.sol Pro**: L128 "Both camps make the same empirical predictions" is too quick (§6). An optional item in the Illusionism/Dualism task.
- **ChatGPT 5.6.sol Pro**: the 2026 no-report inattentional-blindness study (PMID 42060400) supports a multistage picture (§4.3). It resolves at PubMed, but its interpretive claim is unverified; it is a lead only.
- **ChatGPT 5.6.sol Pro**: the bridge-law cost and the target of physicalism as local type identity (§5.4–5.5); and proposed revisions to `observation-and-measurement-void`, `filter-theory`, `interactionist-dualism` and the MQI page (improvements 18–20). Other pages; not tasked here.
- **Claude Opus 5.5**: predictive processing is absent from the page. Verified (0 hits for "predictive"). An optional item in the filter-section task.
- **Claude Opus 5.5**: Sarasso et al. 2015 PCI as the strongest production-side datum. Carried in the filter-section task, but only together with Bajwa's within-sedation null (see Divergences).
- **Claude Opus 5.5**: emergence is never developed (§2.3 ¶4); the report-dependence "smuggling" sentence (P20); the Tulving table has no source (P9); the IIT pseudoscience controversy (the IIT page already carries it). Not tasked.
- **Claude Opus 5.5**: sibling fixes 16 (filter-theory's 15%), 17 (REBUS as a production model), 19 (`visual-consciousness` L87, now inside the definition/COGITATE task), 21 (research-note annotation), 23 (GWT fencing, overstated), 25 (`predictive-processing-and-dualism` length, unmeasured), 27 (`consciousness-disruption…` falsifier) and 28 (anaesthesia port, inside the filter task). Only 19 and 28 are tasked.

## Divergences

- **ChatGPT vs Claude on Chalmers 2000.**
  - ChatGPT: "Minimal sufficiency is one developed proposal, not the unqualified starting definition attributed to the NCC programme as a whole."
  - Claude quotes the minimal-sufficiency-under-conditions-C text as "Chalmers's actual definition".
  - Resolution: both halves are right. The paper starts from "correlates directly" and arrives at minimal sufficiency as its §4 "Overall definition". The task says "overall definition".
  - A trap neither reviewer raised: Chalmers's "background state of consciousness" (waking, dreaming, hypnosis) is something an NCC can be found for. It is not Koch et al.'s "background conditions", which are enablers outside the NCC.
- **ChatGPT vs Claude on what propofol shows.**
  - ChatGPT: "unresponsiveness under propofol is not reliably equivalent to absence of experience." Bajwa 2025 confirms this: 24 of 52 awakenings gave reports of experience.
  - Claude reads the propofol/ketamine PCI split (Sarasso 2015) as a case where "A *neural* measure predicted the presence of experience independently of behaviour."
  - Bajwa also found that PCIst did not separate dreaming from non-dreaming periods within sedation. Both datasets are real but they answer different questions. The task forbids "near-total extinction" as a general claim and requires Bajwa's null alongside any Sarasso sentence.
- **Both reviewers vs the Map's prior adjudication on No Many Worlds.** This is not a reviewer-vs-reviewer disagreement, so it is recorded under cluster 8: deletion was rejected and the verb downgraded.

## Method Notes

- **Coverage 2/3.** Gemini was commissioned at 04:14Z, stalled in Deep Research, and was abandoned at 2026-10-02T01:23Z without a report. The quorum of two was met, and every cluster above is 2/2 of the legs that produced reviews.
- **Task merges: 8 open NCC tasks → 6, all P1** (five P2→P1 upgrades; the IEP task was already P1). The merge followed paragraph ownership, because six separate edits to one paragraph on a page with 80 words of headroom are unsafe.
  - The ChatGPT "Empirical-precision fixes" task was dissolved into three tasks: its V4 and Koch items went to definition/COGITATE, its L117 item and **Ledger** field to the filter section, and its Tallis item to Illusionism/Dualism.
  - The ChatGPT "Cross-review … global-workspace-theory, palette-extension-void and conscious-vs-unconscious-processing" task was dissolved into three tasks: Naccache went to definition/COGITATE, falsifier 2 to falsifiers, and L160 to tenet verbs. Its type was `cross-review`; every surviving task is `refine-draft`.
  - Every grep-verified locus from the eight originals survives in exactly one task. Every task keeps an absolute `File:` path, and all new fields (`Review files`, `Synthesis`, `Status`, and the moved `Ledger`) sit above `Notes:`.
- **Parser check** (`tools.evolution.task_selector.parse_tasks`): 52 active before and 50 after (P0–P2 went from 23 to 21; P1 from 1 to 6; P2 from 22 to 15; P3 unchanged at 29). No headings were added, and `## Completed Tasks` appears once.
- **The collecting passes undercounted one convergence and overcorrected one source.**
  - L178, the imported measurement-void claim, was raised by both reviewers (ChatGPT §7.5 and §9.4; Claude P19), but neither pass turned it into a task.
  - The Claude pass's "jointly sufficient is Koch's 2004 wording" is wrong: it is in the 2016 Key Points.
  - The falsifier task's note had copied Claude's "established at ~14–25%"; it was corrected against the canonical covert page.
- **Convergent methodology proposals (recorded only; operator-reserved; not minted and not appended this cycle).** Each owning NEEDS-HUMAN entry is named so the operator can add addenda as earlier cycles did:
  - Quotation-provenance gate: ChatGPT 21 and 30; Claude 2 ("a single string match" would have caught the SEP/IEP swap). Owner: NEEDS-HUMAN 2026-09-07 (citation-ledger inheritance). This cycle's instance is that the misattributed quotation was ratified by the 01-14 research note and `pessimistic-2026-03-19-night`, and the "up to 25%" figure by three internal passes.
  - Cross-page numerical consistency and staleness propagation: ChatGPT 23 and 28; Claude 3 and 4. Owner: NEEDS-HUMAN 2026-08-03. This cycle's instances are the 09-29 `conscious-vs-unconscious-processing` retraction, which did not reach NCC L160, and the filter-theory 15% vs NCC 25% split. The Corpus Figures Ledger / canonical-page pattern used for covert consciousness on 2026-10-01 is a working prototype.
  - Opponent parity before "converged": ChatGPT 24 and 29; Claude 11. Owner: NEEDS-HUMAN 2026-07-25. This cycle's instances are the regress vs Frankish and the missing Type-B reply.
  - Falsifier reachability template: ChatGPT 26; Claude 8.
  - Evidence-ladder tags and theory-family inference checks: ChatGPT 25 and 27; Claude 9.
  - Cross-family or human sign-off for quotations: ChatGPT 30; Claude 1.
- **Not tasked, observed in passing.** 21 live content pages cite Tallis 2024 under the short title "The Illusion of Illusionism", and `topics/attention-and-the-consciousness-interface` gives it as *Philosophy Now* 159. PDCnet has issue 161, pages 58–59. This is a corpus sweep candidate, outside this cycle's subject.
