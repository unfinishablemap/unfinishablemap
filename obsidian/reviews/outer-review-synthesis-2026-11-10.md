---
title: "Outer Review Synthesis - 2026-11-10"
created: 2026-11-10
modified: 2026-11-11
human_modified: null
ai_modified: 2026-11-11T01:18:36+00:00
draft: false
description: "Synthesis of 2 outer reviews of pain-consciousness-and-causal-power (Gemini abandoned): 17 convergent clusters adjudicated against the live page, 4 tasks upgraded P2→P1, 1 minted, 2 clusters already landed."
topics:
  - "[[pain-consciousness-and-causal-power]]"
  - "[[empirical-phenomena-mental-causation]]"
  - "[[co-optimization-reply-to-the-correlation-problem]]"
  - "[[emotion-and-dualism]]"
concepts:
  - "[[pain-asymbolia]]"
  - "[[valence]]"
  - "[[integrated-information-theory]]"
  - "[[phenomenal-concepts-strategy]]"
related_articles:
  - "[[project]]"
  - "[[outer-review-2026-11-10-chatgpt-5-6-sol-pro]]"
  - "[[outer-review-2026-11-10-claude-fable-5-2]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-11
last_curated: null
subject_type: recent
subject_articles:
  - topics/pain-consciousness-and-causal-power.md
synthesizes:
  - reviews/outer-review-2026-11-10-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-11-10-claude-fable-5-2.md
synthesis_coverage: "2/3"
---

**Date**: 2026-11-10 (cycle); synthesised 2026-11-11 01:16Z
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 2 of 3 commissioned reviewers contributed. The ChatGPT 5.6 Sol Pro leg was processed at 04:01Z and minted 5 tasks (2 P1, 3 P2), and it upgraded the 2026-11-03 tenet-check P3 on L170/L174 to P1. The Claude Fable 5.2 leg (Research, 251 sources) was processed at 04:44Z. It added dated addenda to four of the ChatGPT-leg tasks and minted 3 P2s. The Gemini 3.1 Pro Deep Research leg was **abandoned** at 00:51Z on 2026-11-11: the report hung at "Creating your report…" for about 20.5 h, and `pending-reviews.yaml` records the failure_reason. The subject was "Audit pain-consciousness-and-causal-power" (`topics/pain-consciousness-and-causal-power.md`, fallback `recent-aged`; the Claude leg reused it), set as a hostile-referee premise attack plus a source check.

## TL;DR

Both reviewers reach the same verdict on the same page. The body of "Pain, Consciousness, and Causal Power" already grades asymbolia as *compatible with* rather than *discriminating for* phenomenal causation (L132, L142). Its lede (L64, "the single most discriminating empirical test case in philosophy of mind"), its theory-by-theory section (functionalism, IIT and representationalism answered in weak forms) and its inseparability section (L136–148) still claim more than that. Each candidate cluster was adjudicated against the live file before it counted. Of 17 convergent clusters, 15 are TRUE and 2 are PARTLY. One half of a third cluster (ChatGPT's L176 charge) is FALSE. Two clusters landed on the page after processing: the anticipation and placebo overclaim, and the Many-Worlds physics error (commit a76853e1f4, 11:54Z 11-10). Two more landed in part on sibling pages.

Task actions: 4 upgrades P2 → P1 (the calibration pass, the inseparability/Site-Perspective pass, Hagiwara, and `empirical-phenomena-mental-causation` L155). 2 P1s were rewritten without a priority change. 1 task was minted (P2, orphan References, a convergent TRUE cluster no task owned). There were 0 deduplications: the Fable leg appended addenda rather than minting twins. One convergent TRUE item that fell through that leg's dedupe (L120 functionalism) was added to the calibration task, and one task's type was corrected (cross-review → refine-draft) so its Notes reach the fork. `parse_tasks` active count went from 389 to 390: P1 4 → 8, P2 21 → 18, P3 364 → 364.

## Adjudication Before Clustering

- **Live page.** `obsidian/topics/pain-consciousness-and-causal-power.md` measured 3,982/4,000 by `analyze_length` at 01:05Z on 11-11 (gate `>=`, 17 usable words). Every convergent anchor still open printed `grep -c -F` = 1: "single most discriminating", "Patients report nociceptive stimuli accurately", "selective loss of affective-bodily concern", "As Nikola Grahek frames it", "being precisely the one carrying", "phi is a single scalar measure", "But perceiving a red square", "which is the dualist's central point", "equally distinctive neural signatures", "is a non-causal rival", "Consciousness determines what happens next", "These extended responses track the *felt severity* of the pain", "more transparently", "none can explain why the informational deficit produces a phenomenal one", "declining to explain the central datum", "isolating the hard problem's target". Absence claims printed 0 in the body: `Gerrans`, `active inference`, `predictive`, `imperativ`, `Feinstein`, and the surnames of 11 References entries (listed under C15). Positive controls: Berthier 1, Griffith 2, Noordhof 1, Jensen 1, `valence-prior` 1.
- **Landed since processing.** L152, L154, L170 and L174 were rewritten at 11:54Z on 11-10 (a76853e1f4). L152 now reads "The imagined awfulness is a candidate driver, not a demonstrated one, since masked cues can trigger conditioned nocebo responses (Jensen et al., 2012)". L170 now reads "which neural simulation explains as readily", and L174 is one sentence: "Everettian branches share one dynamics and one supervenience mapping". The clusters these lines carried (C13, C14) are recorded as landed and were not re-minted.
- **Disputed at processing, not counted.** ChatGPT's Duval & Klein overstatement (D1). Fable's stale-changelog charge (the cached copy read 10-15; the live page read 11-09). Fable's claim that the concept page's valence-prior account "explains exactly that deficit" (an over-read of `concepts/pain-asymbolia` L97). Fable's "category error" charge against the bare-correlation / phenomenal-concept split, which is half right; see the singletons.
- **Sibling pages checked.** `topics/co-optimization-reply-to-the-correlation-problem` L49 ("Two positions go under this name") and L95 (the constitutive-physicalist co-optimizer "grants felt awfulness causal efficacy as the computational role"). `concepts/pain-asymbolia`: `Hagiwara` 0, `Ploner` 0, `seizure` 0, `Gerrans` 4, Klein/Gerrans paragraph at L75. `topics/empirical-phenomena-mental-causation` L155, count 1, 3,999/4,000. `concepts/valence` L33/L73/L89. `topics/emotion-and-dualism` L3/L57/L89.

## Convergence Table

| # | Cluster | ChatGPT | Fable | Verdict | Task (line after edit) | Action |
|---|---|---|---|---|---|---|
| C1 | L64 lede "single most discriminating" | §2, §11, imp 5 | §1, §2.3 r1, §4.1 | TRUE | P1 L5036 (a) | P1 kept, rewritten |
| C2 | L114 Berthier base: "selective", "report accurately", non-replication | §2, imp 6 | §2.4 r1/r9, §3 B, §4.5 | TRUE | P1 L5036 (b) | P1 kept; concept-page part landed |
| C3 | L116 Grahek taxonomy as clinical fact / against his own use | §2 Grahek, imp 7 | §2.4 r7, §4.7 | PARTLY | P1 L5036 (c) + P1 L5094 (c) | recorded |
| C4 | L128 red-square representationalism; Klein uncited | §2 Klein, §4, imp 10 | §2.4 r12, §2.5, §4.8 | TRUE | P1 L5036 (d) | P1 kept; sibling pages landed |
| C5 | Physicalist comparators (Klein lost-care, Gerrans, active inference) absent from topic page | §2, §3, imp 31 | §1, §2.7.2–3, §4.6 | TRUE, length-blocked | P1 L5036 note + P1 L5094 (g) | zero-cost pipe added |
| C6 | L126 IIT single scalar vs IIT 4.0 | §4 IIT, imp 14 | §2.5, §4.8 | TRUE | P1 L5022 (b) | P1 kept, rewritten |
| C7 | L76 phenomenal-concepts epistemic→ontological slide | §8, §11, imp 21 | §2.5, §3, §4.4 | TRUE | L5052 (1) | **P2 → P1** |
| C8 | L120 functionalism dilemma | §4, imp 11 | §2.3 r2, §2.7.1, §4.8 | TRUE | L5052 new (6) | **P2 → P1**, scope added |
| C9 | L92 "equally distinctive neural signatures" | §1 | §2.4 r13, §4.13 | TRUE | L5052 (2) | **P2 → P1** |
| C10 | Inseparability L136–148 (L140 "determines", felt severity, quality-action, "more transparently") | §5, imp 15 | §2.5, §3 C, §4.9–10 | TRUE | L5094 (c) | **P2 → P1**, L140 added |
| C11 | Evolutionary reach; L160 "non-causal rival" | §7, §11, imp 20 | §2.6.1, §3 evol. row, §4.3 | TRUE | L5052 (5) + L5094 (e) | **P2 → P1** (with C7) |
| C12 | Site-Perspective re-assertion (L168, L170, L176) | §11, imp 32 | §2.3 r3–4, §4.12 | PARTLY (L176 half FALSE) | L5094 (a) | **P2 → P1** (with C10) |
| C13 | Anticipation/placebo as phenomenal causation | §6, imp 16–19 | §1, §3 D, §4.11 | TRUE | ✓ L5450 | landed a76853e1f4 |
| C14 | Many-Worlds "every supervenience mapping … somewhere" | §9, imp 22 | §2.5, §4.12 | TRUE | ✓ L5450 | landed a76853e1f4 |
| C15 | Orphan References (bibliography padding) | §10, imp 34 | §2.4 summary, §5.4 | TRUE | new P2 L5131 | **minted** |
| C16 | Converse dissociation absent (Hagiwara; Ploner) | §2, imp 23 | §2.7.1 | TRUE | L5067 | **P2 → P1** |
| C17 | `empirical-phenomena-mental-causation` L155 | §12, imp 25 | §4 EPMC | TRUE | L5080 | **P2 → P1**, type fixed |

## Convergent Findings

### C1. The lede calls asymbolia the decisive test the body withdraws
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE. L64 is count 1, and L132 reads "it is all the case discriminates … asymbolia constrains these theories without establishing the Map's causal reading". The 2026-11-03 tenet check (Priority 7) caught the same locus and left it untasked for want of headroom.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Asymbolia only constrains causal interpretations, but the opening calls it the most discriminating empirical test."
  - **Claude Fable 5.2**: "The topic page still opens by calling it 'the single most discriminating empirical test case in philosophy of mind.'"
- **Task action**: P1 left at P1: "`topics/pain-consciousness-and-causal-power` grades Berthier's six cases as 'the single most discriminating empirical test case' (L64) …" (L5036). The task gains an optional (a2), a net-zero softening of L112 "isolating the hard problem's target", which ChatGPT §3 also undercuts: "The lesion does not independently vary phenomenal awfulness while holding its physical and functional realiser fixed."

### C2. The Berthier base is thin, and L114 states it as a selective clinical result
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE. Both halves of L114 are count 1. The ChatGPT leg verified the Berthier 1988 abstract and Feinstein et al. 2016 ("No studies have replicated the original finding"); the Fable leg verified Griffith & Kind 2024 ("For three (out of six) of their patients, Berthier et al. tested pain threshold"). `Feinstein` is 0 on the topic page.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Calling the loss 'selective' converts an interpretive hypothesis into a clinical result."
  - **Claude Fable 5.2**: "Body: patients 'report nociceptive stimuli accurately — localisation, modality, intensity' is **overstated**. Thresholds were tested in only 3 of 6."
- **Task action**: P1 left at P1 (L5036 (b)). The scope note now covers both halves of L114. The concept-page part landed: the surgical/pharmacological research note (d07226be6c, 16:03Z) and its fold into `concepts/pain-asymbolia` (1b8c99778d, 16:07Z) answer the "tiny base" objection there, securing the sensory-affective split without enlarging asymbolia's six-patient base. Both were harvested from these two reviews (✓ L5417, L5412).

### C3. Grahek's taxonomy is used as the clinical finding, and against his own use of the case
- **Flagged by**: chatgpt, claude
- **Verification**: PARTLY. Both legs agree the L116 description of Grahek's distinction is accurate: ChatGPT calls it "broadly faithful to his project", and Fable's column (b) reads "accurate". They differ on what is wrong with it. ChatGPT's charge, that the taxonomy reads as the clinical result rather than one interpretation, is TRUE at L116. Fable's charge, that the page recruits Grahek *for* inseparability when he offered asymbolia against motivationalism (Klein 2015 *Mind* abstract, verified), holds against L136's broad claim that pain collapses phenomenal character into causal role. It does not hold against the page's narrower awfulness–power link, because Grahek's *being in pain* is the component that drives behaviour.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Grahek's classification is a philosophical interpretation of sparse and heterogeneous clinical reports, not a neutral clinical conclusion established by Berthier's data."
  - **Claude Fable 5.2**: "Grahek is recruited for the opposite of his thesis."
- **Task action**: Recorded with the verdict. L5036 (c) keeps the L116 fix and must say what Grahek offered the case *as*. L5094 (c) owns L136–142, where the dilemma Fable states belongs.

### C4. Representationalism is answered with a red square; Klein sits unused in the References
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE. L128 is count 1, and Klein (2015) has no body citation (the only "Klein" in the body is Duval and Klein).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The red-square comparison attacks only a thin descriptive representationalism."
  - **Claude Fable 5.2**: "This ignores evaluativism (Bain; Cutter & Tye 2011) and imperativism (Klein; Martínez 2011), on which the *content* of pain is evaluative or imperative, so differing in whether it hurts *is* differing in content."
- **Task action**: P1 left at P1 (L5036 (d)). The 12:28Z addendum, now inside the Notes, governs the citation choice: Martínez 2011, Bain 2013 or Cutter & Tye 2011, not the Klein book. The sibling-page part landed: `research/imperativism-and-evaluativism-about-pain-2026-11-10` (f0a460146c, 12:28Z; ✓ L5446); the three-account fold on `concepts/valence` (0aee4be0b3, 12:38Z; ✓ L5441), which the task may now link at zero cost via `[[valence#Three Competing Accounts|…]]`; and the "asymbolia settles the hedonic-evaluativist dispute" withdrawal on `topics/emotion-and-dualism` and `apex/minds-without-words` (9e391235f7, 14:39Z; ✓ L5431).

### C5. The strongest physicalist readings of asymbolia are on the concept page, not the topic page
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE, but length-blocked. `Gerrans` 0, `active inference` 0, `predictive` 0 in the topic body; `concepts/pain-asymbolia` carries the Klein lost-care and Gerrans allostatic-inference paragraph at L75. At 17 usable words no paragraph fits.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Whether ultimately successful or not, it is exactly the kind of contemporary comparator the article needs to confront at full strength."
  - **Claude Fable 5.2**: "**Page reply:** none on the topic page. The concept page engages the reading properly."
- **Task action**: L5094 gains item (g), a zero-cost pipe of L142's "a valence-prior account" to `pain-asymbolia#Causal Efficacy of Phenomenal Quality`. L5036 is told to keep L114's existing link into the concept page's `What Asymbolia Dissociates` section. A full engagement is the remainder, owed when the page has budget.

### C6. IIT is described as a scalar-only theory
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE. L126 is count 1, and Albantakis et al. 2023 (IIT 4.0) was verified at PLOS.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "IIT 4.0 expressly distinguishes the **quantity** of consciousness from its structured **quality**."
  - **Claude Fable 5.2**: "In IIT 3.0/4.0, Φ gives the *quantity* of consciousness, while the *quality* is given by the cause–effect structure, so a local lesion can remove a specific quality."
- **Task action**: P1 left at P1 (L5022 (b)). Fields rewritten. Its (a), the IASP definition, is a ChatGPT singleton.

### C7. The phenomenal-concepts strategy's epistemic gap is counted as the dualist's point
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE (L76, count 1).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "It cannot simply count the acknowledged epistemic difference as the dualist conclusion."
  - **Claude Fable 5.2**: "Loar, Papineau and Balog concede a *conceptual* gap precisely in order to deny an *ontological* one."
- **Task action**: Upgraded P2 → P1: "`topics/pain-consciousness-and-causal-power` calibration pass on five sentence-level over-claims …" (L5052, item (1)).

### C8. The functionalism dilemma attacks a functionalism of information alone
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE. L120 "being precisely the one carrying phenomenal character" (count 1) contradicts L84, which gives sensory pain its own phenomenology ("sharp, burning, throbbing"). Its conclusion targets a view functionalists do not hold. No task owned this line: the Fable leg's dedupe counted its fix 8 as owned when only the IIT and representationalism clauses were.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "functionalism does not have to claim that **sensory information alone** does so."
  - **Claude Fable 5.2**: "The page's dilemma for functionalism … is a dilemma functionalists embrace: on the second horn the affective component just *is* the motivational role."
- **Task action**: Added as item (6) to L5052, the same task upgraded P2 → P1 under C7, with a coordination note to the concept-page P2 (L5110 (b)), which makes the same correction at `concepts/pain-asymbolia` L85–87.

### C9. "Equally distinctive neural signatures" fails from both sides
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE (L92, count 1). The two legs argue in complementary directions. ChatGPT: physicalism does not require a compact signature per folk category. Fable: the page's own References entry, Kragel & LaBar 2015, reports categorically distinct signatures. Either way the "sharp challenge" does not stand.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Physical realization does not require a one-to-one anatomical signature for every folk-psychological category."
  - **Claude Fable 5.2**: "Kragel & LaBar's title reports that multivariate neural biomarkers of emotional states *are* categorically distinct."
- **Task action**: Upgraded with L5052 (item (2), which already says cite-or-drop Kragel & LaBar).

### C10. The inseparability thesis rests on introspective unity and uncited mappings
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE. L138 concedes that the epiphenomenalist may read the felt unity as physical; L140 then asserts "Consciousness determines what happens next" (count 1). L140's "felt severity" and L146–148's sharp/burning/aching taxonomy carry no citation, and "more transparently" is count 1.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The article briefly concedes this epiphenomenalist interpretation and then immediately asserts that consciousness determines the subsequent response."
  - **Claude Fable 5.2**: "Transparency to introspection is an epistemic property. Inferring causal priority from it is a slide from the epistemic to the metaphysical."
- **Task action**: Upgraded P2 → P1: "`topics/pain-consciousness-and-causal-power` Site-Perspective and Claim-C calibration …" (L5094). Item (c) is widened to L140, and it still runs last on the file by FIFO.

### C11. The evolutionary argument binds less than its section title says
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE. The co-optimization page the label links names two positions under that name (L49) and grants the constitutive-physicalist co-optimizer felt awfulness "causal efficacy as the computational role" (L95). L160's "non-causal rival" therefore fits only one of them. Fable's Robinson point is reachable one click away, so its remedy is a pipe link, not prose.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The article calls co-optimization a 'non-causal rival,' but this conflates two different opponents."
  - **Claude Fable 5.2**: "The concession is accurate, but it empties the section's title ('Hardest Case') of content."
- **Task action**: Upgraded with L5052 (item (5)); L5094 (e) holds the Robinson pipe. The section rename is not tasked (PARTLY: L160 already scopes it, and a heading change moves an anchor).

### C12. The Site-Perspective section re-asserts what the body withdraws
- **Flagged by**: chatgpt, claude
- **Verification**: PARTLY. L170 "phenomenal content alone" was TRUE and has landed (a76853e1f4). L168 "none can explain" is PARTLY: L132 itself says "None explains the core phenomenon" and calls it the explanatory gap, so the defect is the modal *can* and its use as tenet support, not a contradiction of a shared-explanandum verdict. ChatGPT's L176 half is FALSE (see D3).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Access-level accounts predict anticipation equally well, but the tenet section says phenomenal content acts alone."
  - **Claude Fable 5.2**: "The hedges that were added later sit in the body. The unhedged assertions survive in the lede and the Site Perspective section."
- **Task action**: Upgraded with L5094 (item (a)). The note sets "none yet explains" as the minimal acceptable form and tells the fork not to edit L176.

### C13. Anticipated and placebo pain are read as phenomenal causation
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE at review time. Both legs cite masked-cue conditioning: ChatGPT Jensen et al. 2015, Fable Jensen et al. 2012.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The experiments intervene on instructions, cues or expectations—not on phenomenal character while holding those other variables constant."
  - **Claude Fable 5.2**: "It confuses absence of peripheral input with absence of physical cause."
- **Task action**: Recorded only. The matching task is complete: "`topics/pain-consciousness-and-causal-power` L170/L174 …" (✓ L5450, a76853e1f4, 11:54Z on 11-10) rewrote L152, L154 and L170.

### C14. The Many-Worlds paragraph contains a physics error
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE at review time; now fixed. L174 now states that branches share one dynamics.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "This paragraph should be removed rather than hedged."
  - **Claude Fable 5.2**: "Everettian branches share one set of dynamical laws, and MWI does not vary psychophysical laws across branches."
- **Task action**: Recorded only. Landed in the same commit as C13 (✓ L5450).

### C15. A third of the References list is padding
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE. Eleven entries have 0 surname hits in the body: Cassell, Chalmers, Cleeremans, Jackson, Klein 2015, Kragel, Levine, Panksepp, Ramachandran, Rubins, Scarry. Fable counted 10 because it passed Levine as "generic use". The 2026-11-03 changelog left them "unchanged and out of scope".
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "A reference list should not function as a background reading dump."
  - **Claude Fable 5.2**: "Ten references … are bibliography padding."
- **Task action**: Minted as a new P2 (L5131), cite-or-delete per entry, with the Klein, Kragel & LaBar and Chalmers entries reserved for the sibling tasks that decide them. Because `analyze_length` counts the reference apparatus, the deletions also return words to the page.

### C16. No converse dissociation appears beside asymbolia
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE. `concepts/pain-asymbolia` has `Hagiwara` 0, `Ploner` 0 and `seizure` 0; its only "inverse" is phantom pain. Hagiwara et al. 2020 was verified via E-utilities, and the Ploner 1999 entry was Crossref-checked in the surgical research note.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Such cases support a distributed, multidirectional decomposition of pain processing."
  - **Claude Fable 5.2**: "Asymbolia shows that 'pain' is a cluster of separable functional components, which is exactly what … Ploner et al. (1999, the converse case: 'pain affect without pain sensation') predicted."
- **Task action**: Upgraded P2 → P1: "`concepts/pain-asymbolia` lacks the inverse dissociation — Hagiwara et al. (2020) …" (L5067). Its budget note records that the two P3s on that page cannot both fit under 3,499 afterwards.

### C17. `empirical-phenomena-mental-causation` L155 states phenomenal causation outright
- **Flagged by**: chatgpt, claude
- **Verification**: TRUE (L155, count 1; page 3,999/4,000).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "that article itself still contains one overstrong asymbolia sentence immediately before its better-calibrated section."
  - **Claude Fable 5.2**: "Audit it for the same 'placebo shows phenomenal causation' overreach."
- **Task action**: Upgraded P2 → P1 (L5080). The type was changed from cross-review to refine-draft. A cross-review task dispatches deep-review with the file path and title only, so its OLD/NEW strings and zero headroom would never have reached the fork.

### Methodology recurrences
Both legs restate site-level disciplines already logged as 11-10 addenda on the standing NEEDS-HUMAN (methodology ratification) entry (todo L743): caveat-regression and hedge propagation (ChatGPT imp 32–33; Fable §5 items 2 and 7); entailment and stance verification beyond metadata (ChatGPT imp 28–29; Fable §5 item 5); rival-theory gates (ChatGPT imp 31; Fable §5 item 6); and the orphan-reference purge (ChatGPT imp 34; Fable §5 item 4), whose content instance here is C15. The two legs also each say, in different words, that the review history ratified a defective page: ChatGPT points to the "seven times converged" deep review, Fable to Claude-on-Claude circularity. These were left for human ratification and nothing was minted.

## Singleton Findings

Left at their original priority.

- **ChatGPT 5.6.sol Pro**: L80 defines pain as nociceptive signalling against IASP (verified; L5022 (a), P1). L92 "No analgesic touches any of these" (L5052 (2)). L98 meditation, where Grant & Rainville report unpleasantness paralleling intensity (verified; L5052 (3)). L122 "two separate monitoring streams" (L5052 (4)). Untasked: L124 GNW (low value, since L132 already names the gap), the 2024 suffering review (unverified), and imp 24 on `emotion-and-dualism`'s "strongest empirical case" thesis (a human position call, declined at processing).
- **Claude Fable 5.2**: the description's scope clause has no body counterpart (`bare-correlation` 0 in the body; L5094 (d)). L172 Minimal Quantum Interaction inherits the Born-preservation debt (L5094 (b)). The Robinson and Chalmers-2003 replies are missing, though both are argued elsewhere on the Map (L5094 (e)). The L183 embodied-interface blurb (L5094 (f)). The concept page credits Rubins & Friedman with priority over Schilder & Stengel, and its L85–87 functionalism overreach (verified; "`concepts/pain-asymbolia` L50 credits …", L5110, P2). `concepts/valence` L89 "binds the bare-correlation epiphenomenalist" (L5120, P2; see D4). Untasked: the uncited opioid claim at L154 (TRUE, but a citation costs about 25 words at 17 usable); Noordhof's imagining thesis (anticipation already hedged); the missing literature (illusionism, Mørch, Carruthers, congenital insensitivity, Hardcastle/Corns, the meta-problem, Jackson's recantation; length-blocked); and the claim that the bare-correlation / phenomenal-concept split misfiles a physicalist strategy (half right at processing, tasked only as zero-cost pieces in L5120 (b) and L5094 (e)).
- **Disputed singleton**: Fable's stale-changelog charge (§2.1, §5 item 8). The live changelog read 11-09 at processing, so Fable read a cached copy. FALSE; not tasked.

## Divergences

- **D1. ChatGPT vs Fable on Duval & Klein.** ChatGPT: "'Duval and Klein reply that it probably still is [pain]' overstates what their discussion establishes." Fable: "'reply that it probably still is': accurate." Page evidence: the L114 wording mirrors the reference title at L209, "Pain Asymbolia Is Probably Still Pain", and the paper concludes "for all we know, pain asymbolia might still be pain" (ChatGPT-leg verification). **Fable is right.** The wording stays, and a guard was added to L5036 so the (b) and (c) rewrites cannot soften it.
- **D2. Grant & Rainville.** Fable passes the meditation citations "unverified beyond metadata"; ChatGPT read the abstract ("Changes in pain unpleasantness generally paralleled those found in pain intensity"). This is not a true contradiction, since Fable did not check. The verified reading governs L5052 (3).
- **D3. A FALSE convergence: ChatGPT's L176 charge.** ChatGPT §11 lists "Noordhof and valence-prior accounts remain live, but physicalism is later described as declining to explain the central datum", which pairs with Fable's L168 row in C12. Page evidence: L176's "central datum" is "why anything *suffers at all*", the gap that L132 keeps in the body ("None explains the core phenomenon … That shortfall is the [[explanatory-gap]] in clinical focus"). The Noordhof and valence-prior accounts predict the dissociation (L142, "a shared explanandum"); they do not close that gap. L176 restates the body, so it is excluded from C12, and L5094 is told not to edit it.
- **D4. An apparent divergence on "binds the bare-correlation".** ChatGPT §12 says `emotion-and-dualism` "correctly says asymbolia binds the bare-correlation version", while Fable §4 asks `concepts/valence` to downgrade "binds" to "presses on". Page evidence: `emotion-and-dualism` L57 and L89 attribute the binding to the P-MC1-scoped anti-epiphenomenalism argument ("the Map's strongest anti-epiphenomenalism argument binds bare correlation"), whereas `concepts/valence` L89 attributes it to the lesion ("When the phenomenal property is absent, behavior changes, which binds …"). ChatGPT's own §3 says the lesion alters experience and behaviour jointly "whether the experience is causally efficacious, physically constituted by that system, or epiphenomenally correlated with it", which supports Fable on the valence line. No contradiction remains, and L5120 stays a Fable singleton at P2.

## Length Budget (run order)

The topic page is 3,982/4,000 (17 usable). Its P1s now run FIFO by line: L5022 (IASP/IIT), L5036 (Berthier/Grahek/representationalism), L5052 (calibration pass plus L120), then L5094 (Site-Perspective/inseparability, last, as its Coordination note requires). The new orphan-References P2 (L5131) follows. Each P1 is net ≤ 0 on its own budget. The P2's deletions free roughly 150 words of reference apparatus but must not turn into new prose in the same pass. `concepts/pain-asymbolia` is 3,098/3,500 with two open P1/P2 additions (about +133 and ≤ +40) and two P3s (about +75, +144) that will not both fit. `empirical-phenomena-mental-causation` has 0 usable words.

## Method Notes

- Coverage was 2/3: Gemini 3.1 Pro was abandoned at 00:51Z on 11-11, after about 20.5 h at "Creating your report…" (`pending-reviews.yaml` failure_reason). With two legs, a cluster can count at most 2/3, and every cluster here is a 2/3 cluster.
- Every cluster was adjudicated against the live file at 01:05Z, not against the review text. Four of the ChatGPT leg's line-level targets (L152, L154, L170, L174) had moved since processing, and those clusters were recorded as landed.
- Two pipeline defects were found and fixed in the task text. First, the Fable leg's convergent addenda sat in `- **Addendum …**:` fields above `Notes:`, which `task_to_skill` never passes to the fork (only File, Notes with continuation lines, and Review file are passed). They were moved into the Notes verbatim, along with L5094's Coordination field. Second, L5080 was typed cross-review, which dispatches deep-review with only the file and title. It was retyped as refine-draft.
- Orphan check method: frontmatter stripped, `## References` onward excluded, `grep -oiF` per surname, with Berthier, Griffith, Noordhof and Jensen as positive controls.
