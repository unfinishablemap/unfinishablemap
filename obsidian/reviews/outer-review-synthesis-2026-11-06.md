---
title: "Outer Review Synthesis - 2026-11-06"
created: 2026-11-06
modified: 2026-11-06
human_modified: null
ai_modified: 2026-11-06T06:28:39+00:00
draft: false
description: "Synthesis of 2 outer reviews of substance-property-dualism (Gemini abandoned): nine verified two-reviewer clusters, five tasks upgraded P2→P1, Pautz splice settled for Claude, no merges."
topics:
  - "[[history-of-the-interaction-problem]]"
concepts:
  - "[[substance-property-dualism]]"
  - "[[where-the-substance-commitment-enters]]"
  - "[[illusionism]]"
  - "[[pairing-problem]]"
  - "[[causal-exclusion-argument]]"
  - "[[russellian-monism]]"
related_articles:
  - "[[project]]"
  - "[[outer-review-2026-11-06-chatgpt-5-6-sol-pro]]"
  - "[[outer-review-2026-11-06-claude-fable-5-1]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-06
last_curated: null
synthesizes:
  - reviews/outer-review-2026-11-06-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-11-06-claude-fable-5-1.md
synthesis_coverage: "2/3"
---

**Date**: 2026-11-06
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 2 of 3 commissioned reviewers contributed. The ChatGPT 5.6 Sol Pro leg was processed at 04:49Z and minted 5 tasks (1 P1, 4 P2). The Claude Fable 5.1 leg, with Research, was processed at 05:32Z. It added Claude-corroborated addenda to all five ChatGPT-leg tasks and minted 1 new P2. The **Gemini 3.1 Pro Deep Research leg was abandoned** at 06:09Z, because the research stalled at "Starting research..." for more than 100 minutes with no source count. That is a pipeline failure, not a reviewer verdict, and Gemini contributes nothing to any cluster below. The subject was `concepts/substance-property-dualism` (fallback `recent-aged`). Claude and Gemini reused ChatGPT's subject, and each ran its own prompt.

## TL;DR

Both reviewers audited the same 3,002-word article and converged on nine verified defect clusters. The strongest are four. Zimmerman (2010) is misattributed a panpsychism-or-epiphenomenalism dilemma that his abstract does not contain. The article's bare-regress reply to illusionism is one that Frankish 2016 §1.1 explicitly answers and the Map's own `concepts/illusionism` L91 concedes. Descartes's reply to Elisabeth is credited to the pineal gland. And the lead calls the Posit One dependency a mere "preference", although the article's own L161 heading says otherwise. The one known false agreement was adjudicated before clustering. ChatGPT called the Pautz quotation "real". Claude found it spliced, and this synthesis re-fetched the raw draft independently and confirmed Claude.

Cluster count: 0 three-reviewer clusters (one leg abandoned), 9 two-reviewer content clusters (C1–C9), 3 two-reviewer methodology recurrences (M1–M3), 7 non-counting agreements (R1–R7), 3 divergences (D1–D3). Task actions: 5 upgrades (P2 → P1) and 1 P1 rewritten without a priority change. There were 0 deduplications and 0 deletions, because the Claude leg had already added addenda instead of minting duplicates. `parse_tasks` active count: 386 before, 386 after. P1 went from 3 to 8, P2 from 21 to 16, and P3 stayed at 362.

## Adjudication Before Clustering

Each leg was tested before it was allowed to count. A cluster counts only if both reviewers make the same claim and the claim holds against the live file (grep count printed) or the raw source.

- **Pautz (the known false agreement).** ChatGPT §4: "The Pautz quotation is real." Claude §2.3: "The Pautz quote is unverified … the opening 'Though called' is not found." This synthesis fetched Wayback snapshot `20260424035143` of `philpapers.org/archive/PAUCRM.pdf` (8 pages, header "First Draft of December 15th, 2015") and ran `pdftotext` on it. 'Though called' has **0** hits. 'calling it a physicalist view' has **1**, in the sentence "Still, primitivist Russellian monism is an unattractively complicated view. I am calling it a physicalist view, but it seems to have many of the vices of dualism." The live article L73 carries «"Though called a physicalist view, it seems to have many of the vices of dualism."» (count 1). The predicate is verbatim and the subject is not. **Verdict: Claude is right on fidelity, and ChatGPT's "real" is wrong on the subject clause.** ChatGPT's separate scope claim is right: the target is *primitivist* Russellian monism, and the draft sets it apart from the reductive form ("the distinction between reductive and primitivist forms of Russellian monism"). The scope also covers L73's grounding-laws clause: "this view requires exactly parallel special, brute 'grounding laws'", where "this view" is the primitivist form. This is a divergence settled in Claude's favour (D1), so it is not counted as convergence on "the quote is fine".
- **Zimmerman.** Crossref carries no abstract for DOI 10.1111/j.1467-8349.2010.00189.x, so the abstract was rebuilt from OpenAlex's inverted index (864 characters). 'panpsych' has 0 hits and 'epiphenomen' 0. 'bearers of the qualia' has 1, 'adverbial' 1 and 'speculative forms of materialism' 1. Both reviewers' claims hold. This check is at abstract level only, because the full text is paywalled.
- **Frankish 2016.** In the raw eprint (keithfrankish.github.io), 'not themselves phenomenally conscious ones' has 1 hit and 'self-defeating to explain illusory phenomenal properties' has 1. The footnote cites "Pereboom, 2011, pp. 27–8" for an argument "that it does not generate an infinite regress". Both reviewers' claims hold.
- **Descartes–Elisabeth 1643.** In the raw earlymoderntexts PDF, 'pineal' has 0 hits. The 'gland' matches (2) are both inside 'England'. 'notion of their union' has 2 hits ("only the notion of their union, on which depends the notion of the soul's power to move the body"). Both reviewers' claims hold.
- **Live article greps** (`obsidian/concepts/substance-property-dualism.md`, 3,002 words by `analyze_length`, concepts hard 3,500, gate `>=`). Every quoted anchor below printed count 1. The absence claims printed 0: 'exclusion' 0, 'causal-exclusion' 0, 'Papineau' 0, 'phenomenal concept' 0, 'Schwarze' 0, 'McKemmish' 0, 'Jackson' 0, 'bi-aspectual' 0, 'Elisabeth' 0 (but 'Elizabeth' 1), 'Mackie' 0. Hasker is named twice (L75, L95) and Kim twice, and Bailey once (L95). None of the three has a References entry.
- **Claude's search-copy reads.** Claude fetched the target article live but read most sibling pages from search-index copies. Three of its sibling-page claims fail against the live corpus: 'dualism without substances' has 0 hits in `concepts/bi-aspectual-ontology`; the "vices" quote is absent from `concepts/russellian-monism`; and the Jackson recantation is already on `concepts/knowledge-argument` (the "Jackson's Self-Rejection" section, L108). None of those claims enters a cluster.

## Convergence Table

| ID | Finding | ChatGPT | Claude | Verified live / at source | Task | Action |
|---|---|---|---|---|---|---|
| C1 | Zimmerman misattributed (L159) | §3, ref row 14, item 7 | §2.3, row 14, fix 11 | Yes: L159 count 1; abstract has no panpsych/epiphenomen | A | Already P1 |
| C2 | Pairing: location reply overclaimed, Bailey/Kim uncited (L95) | §3, item 8 | §2.4 row 1, row "—", fix 13 | Yes: "supports the first" 1; no Bailey/Kim/Hasker entries | A | Already P1 |
| C3 | Illusionism replies beg the question (L109 regress, L111 debunking) | §5, ref row 4, item 12 | §2.4, row 4, fix 14 | Yes: both strings 1; Frankish §1.1 raw; `illusionism` L91 | A | Already P1 |
| C4 | Contemplative reports treated as independent evidence (L113) | §5, item 13 | §2.4, fix 15 | Yes: L113 1; `witness-consciousness` L148, `illusionism` L133 | A | Already P1 |
| C5 | Lead calls the Posit One dependency a "preference" (L41; L3, L169) | §7, items 1, 18 | §2.5, fix 18 | Yes: L41 1, L161 heading 1; background-commitments L58 | B | P2 → P1 |
| C6 | Primitive subject unity treated as cost-free (L159, L97, L61; item 5) | §3 Hasker, §4, §10, items 9, 17 | §2.2, §2.4, fixes 7, 17 | Yes: three strings 1 each; SEP §5.2; P-SC2 | C | P2 → P1 |
| C7 | Cartesian history and attribution apparatus (L51; Hasker entry; RM filing) | §2, §3, §4, items 3–6, 10 | §2.1, §2.3, fixes 1, 4, 7, 13 | Yes: L51 strings 1; 'pineal' 0 in the 1643 letters | D | P2 → P1 |
| C8 | Post-decoherence clause offered as mitigation; non-replication unsourced (L129) | §6, ref row 5, items 14–15 | §2.4 decoherence row, row 5, fixes 16, 20 | Yes: strings 1; 'Schwarze' 0; background-commitments L42 | E | P2 → P1 |
| C9 | Exclusion argument absent; closure rejection treated as free (L175) | §10 ("Causal exclusion for interactionist properties") | §2.3, §2.4 table, fix 12 | Yes: 'exclusion' 0; `concepts/causal-exclusion-argument` exists, unlinked | F | P2 → P1 |
| M1 | Specialist-page corrections do not reach the hub | items 20, 25, §8 | methodology 4 | Three live instances (`illusionism` L91, `pairing-problem` L81/L89/L93, scoping L44/L50) | NEEDS-HUMAN | Addenda already present |
| M2 | Claim–source ledgers ratify readings nobody grepped in the source | item 21 | methodology 1, 7 | Pautz and Zimmerman, both ratified by the 2026-07-30 ledger | NEEDS-HUMAN | Addenda already present |
| M3 | Currency refresh for live debates | item 24 | methodology 6 | Jackson recantation and Chalmers's later preference missing from the hub | Weekly literature-drift and F | No change |

## Convergent Findings

### C1. Zimmerman (2010) misattributed
- **Flagged by**: chatgpt, claude
- **Verification**: clean. Both legs checked the claim against the abstract, and this synthesis re-checked it through OpenAlex. The full text is paywalled, so the check stays at abstract grain.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Zimmerman is attributed an argument from property dualism to 'panpsychism or epiphenomenalism' that his paper does not make."
  - **Claude Fable 5.1**: "'Persistent pressure toward either panpsychism or epiphenomenalism' is not in his abstract or in secondary summaries."
- **Task action**: P1 left at P1. "`concepts/substance-property-dualism` misattributes Zimmerman (2010) at L159 …" got its fields rewritten (`Review files`, `Synthesis`, convergent preamble). There were no siblings to merge.
- **Note**: Claude's attribution of the epiphenomenalism-or-overdetermination dilemma to Searle 2002 is unverified. The task's addendum already forbids asserting it without the text.

### C2. Pairing: the location reply is overclaimed and the sources are uncited
- **Flagged by**: chatgpt, claude
- **Verification**: clean on the shared claim. ChatGPT alone made the haecceity misattribution ("invoking haecceities … (Bailey, Rasmussen, Van Horn)"); it is verified against `concepts/pairing-problem` L81/L89/L93 and counts as a singleton inside the same task.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "interface locality may address where interaction occurs, but it does not non-circularly ground why this subject is coupled to this brain."
  - **Claude Fable 5.1**: "Reply (1), 'consciousness is located where it interfaces', grounds location in the causal interface whose pairing was in question. That is circular."
- **Task action**: P1 left at P1. Same task as C1, locus (b).

### C3. The illusionism replies beg the question
- **Flagged by**: chatgpt, claude
- **Verification**: clean. Frankish §1.1 was raw-verified by the Claude leg and re-verified here. `concepts/illusionism` L91 concedes that the bare regress fails. Both reviewers also independently said that the L111 "Introspection survives debunking" reply misdescribes the illusionist inference (ChatGPT §5: "Illusionists do not infer nonexistence from fallibility alone"; Claude §2.4: "The argument is not 'introspection is fallible, therefore its object is illusory'"). That makes L111 part of this cluster, not a Claude-only addendum.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Frankish's position is precisely that 'seeming' here means a nonphenomenal self-representation."
  - **Claude Fable 5.1**: "The article's reply begs the question against the view it names and engages none of these moves."
- **Task action**: P1 left at P1. Same task, loci (c) and (e).

### C4. Contemplative reports treated as independent evidence
- **Flagged by**: chatgpt, claude
- **Verification**: clean against the Map's own standard. `concepts/witness-consciousness` L148 reads "consonant with the Map's reading rather than evidence against its rivals", and L119 engages Laukkonen, Friston and Chandaria 2025 (Crossref-verified by the Claude leg).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "A report after meditation still involves memory, metacognition, attention and retrospective conceptualisation."
  - **Claude Fable 5.1**: "Citing reports as independent evidence against a theory of reports is an evidential-independence failure."
- **Task action**: P1 left at P1. Same task, locus (d).

### C5. The lead understates the operational substance dependency
- **Flagged by**: chatgpt, claude
- **Verification**: clean on the shared claim. L41 («treats the choice as a philosophical preference rather than a doctrinal requirement», count 1) sits under the article's own L161 heading "Where the Substance-Leaning Becomes Load-Bearing". `tenets/background-commitments` L58 says the operational framework "runs substance-dualist". Claude's stronger "DELETE the 'accepts either' headline" was **disputed** at processing, because the same L58 continues "the neutrality is honest *at the tenet level*". That recommendation does not count. See D2 and D3.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The main article now says those dependencies are 'load-bearing,' but still describes the choice globally as merely preferential."
  - **Claude Fable 5.1**: "The article calls the substance lean 'a philosophical preference, not a doctrinal requirement'. Its own next section is headed 'Where the Substance-Leaning Becomes Load-Bearing'."
- **Task action**: Upgraded P2 → P1: "`concepts/substance-property-dualism` lead L41, L163, L177 and the L67 definition say less than the canonical scoping page …" (1 task, no siblings). The preamble records D3, so the fork writes both halves of the reconciliation.

### C6. Primitive subject unity is treated as cost-free
- **Flagged by**: chatgpt, claude
- **Verification**: clean. «it avoids the combination problem entirely» (L159), «Substance dualism avoids this by positing unified mental substances from the start.» (L97) and «By positing unified mental substances from the start» (L61) each count 1. SEP Dualism §5.2 ("Whether one believes that the mind is a substance or just a bundle of properties, the same challenge arises") was raw-verified by the Claude leg. The Map books the debt itself at P-SC2. Both reviewers also judge challenge item 5 ("Contemplative consensus on substancehood") non-discriminating, which supports the task's item-5 offset.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "A primitive unified substance avoids constitutive subject-combination by stipulation, but inherits questions about subject emergence, individuation, neural distribution, pairing and fission."
  - **Claude Fable 5.1**: "Emergent substance dualism (Hasker) must explain how a unified simple subject arises from a composite brain, which is a combination problem in reverse."
- **Task action**: Upgraded P2 → P1: "`concepts/substance-property-dualism` treats primitive subject unity as cost-free …" (1 task, no siblings).

### C7. Cartesian history and attribution apparatus
- **Flagged by**: chatgpt, claude
- **Verification**: clean. In the 1643 letters 'pineal' has 0 hits. The sibling `topics/history-of-the-interaction-problem` keeps the pineal locus (L51) apart from the primitive-notions reply (L63), and it gives Leibniz momentum, not energy (L91). The live article spells the name 'Elizabeth' (1 hit) where the sibling has 'Elisabeth' (17). Hasker is named at L75 and L95 with no References entry. Both reviewers also object to filing Russellian monism inside property dualism (ChatGPT §4, "not simply a property-dualist variety"; Claude §2.3, "miscategorised"), and the Pautz draft's own phrase "non-standard form of physicalism" (2 hits) supports them.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "'Descartes answered … by pointing to the pineal gland' conflates two different parts of Descartes's position."
  - **Claude Fable 5.1**: "The pineal gland belongs to the *Treatise on Man* and *Passions of the Soul*, not to the answer Elisabeth received."
- **Task action**: Upgraded P2 → P1: "`concepts/substance-property-dualism` history and attribution apparatus …" (1 task, no siblings). The preamble records the D1 verdict and widens the primitivist scope to L73's grounding-laws clause. Lowe at locus (c) carries two distinct claims, both verified, one from each reviewer (R4).

### C8. The decoherence paragraph counts an open measurement problem as mitigation
- **Flagged by**: chatgpt, claude
- **Verification**: clean against the Map's own constraint. `tenets/background-commitments` L42 holds that the measurement problem "cannot be evidence for conscious selection". Both reviewers also flag the unsourced non-replication clause («depends on a single-frequency result that has not replicated», count 1; 'Schwarze' 0 in the article, while `concepts/radical-pair-magnetoreception` L48/L103 carries Schwarze et al. 2016).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "An unresolved interpretation problem is not positive evidence for a consciousness-sensitive selection law."
  - **Claude Fable 5.1**: "'Decoherence doesn't solve collapse' shows only that selection is not excluded."
- **Task action**: Upgraded P2 → P1: "`concepts/substance-property-dualism` L129 decoherence paragraph …" (1 task, no siblings). The Luo clause in the same paragraph stays with the open P3 Luo sweep.

### C9. The exclusion argument is missing
- **Flagged by**: chatgpt, claude
- **Verification**: clean on absence. 'exclusion' has 0 hits and 'causal-exclusion' 0, and the Map's `concepts/causal-exclusion-argument` exists but is unlinked. ChatGPT raised this in its list of absent counterarguments, not as a numbered improvement, and its processing pass neither confirmed nor disputed it. Both reviewers also name the phenomenal-concepts strategy as a missing reply at L87 ('phenomenal concept' 0). But the ChatGPT leg declined its own L87 framing request, so that locus is recorded as Claude-led (R3) and does not drive the upgrade.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Causal exclusion for interactionist properties: rejecting closure is only the start; the article must say which physical transitions are not physically sufficient and how mental properties alter them."
  - **Claude Fable 5.1**: "The article says closure is 'an additional commitment ... that the Map rejects'. That reframes a widely held inductive premise (Papineau) as an optional extra and never engages the argument for it."
- **Task action**: Upgraded P2 → P1: "`concepts/substance-property-dualism` is stale on Chalmers and Jackson, never names Kim's exclusion argument …" (1 task, minted by the Claude leg). Only locus (c) is two-reviewer. Loci (a), (d), (e) and (f) are Claude singletons that ride along at the task's tier.

### Methodology recurrences (M1–M3)

- **M1, propagation.** ChatGPT items 20 and 25 match Claude methodology item 4. The collect legs already attached dated addenda to the 2026-08-03 propagation NEEDS-HUMAN entry, so no further action was taken.
- **M2, ledgers ratify readings.** ChatGPT item 21 matches Claude methodology items 1 and 7. This cycle shows it twice. The 2026-07-30 deep-review ledger graded Zimmerman "faithful on the main enrollment", and it recorded the Pautz quotation as "grep-contiguous in the raw file", meaning the Map's own research note, not the source. The ChatGPT leg then called the same quotation "real". The addenda are already on the 2026-07-30 per-claim-ledger NEEDS-HUMAN entry.
- **M3, currency.** ChatGPT item 24 matches Claude methodology item 6. The weekly `/literature-drift-review` covers the mechanism, and task F covers this page's instance.

## Rejected and Non-Counting Agreements

- **R1. Whitehead (L139).** ChatGPT (reference row 13; §10) says process monism "does not automatically satisfy the Map's dualism tenet", and Claude (row 13) flags "co-optation". The Claude-leg processor **disputed** the charge: L139 claims compatibility, not a dualist label. This synthesis agrees with the dispute. L139's stated grounds ("experiential reality is fundamental, and no physical description entails or explains experience") are the irreducibility content that background-commitments L58 says "is all Tenet 1 asserts". Not counted, and no task.
- **R2. Challenge item 4 (L151).** Both reviewers call it non-discriminating, but for different reasons. Claude's reason ("Physicalism also predicts that this will not occur") was disputed at processing, because property dualism needs a physical bearer, so the condition does separate the two dualisms. ChatGPT's reason (it could reflect "an incomplete neural measurement") is an evidential caveat that applies to any discovery claim. Not counted, and task C keeps item 4.
- **R3. L87 physicalist replies.** Both name the phenomenal-concepts strategy. The ChatGPT leg declined the L87 attribution request as framework-perspective, and the Claude leg tasked a zero-argument link. The absence is verified (0 hits), but because one leg declined, this agreement does not drive F's upgrade.
- **R4. Lowe (L61).** Same locus, different claims. ChatGPT says NCSD is flattened (the self is "not necessarily separable" and bears physical properties, `concepts/four-category-ontology` L72). Claude says Lowe's model is non-quantum (verbatim SEP Mental Causation). Both are verified and both sit in task D(c).
- **R5. Hagan (L129).** Different claims. ChatGPT says the result is model-specific and that McKemmish is omitted. Claude says recruiting Orch OR proponents is co-optation. Both sit in E(d) as an option.
- **R6. Quantum "opening" (L57–59).** Different claims. ChatGPT says that indeterminacy alone does not establish causal room; that point was declined at processing as framework-level, since it is owned by P-Q2. Claude says the quantum route is presented as a generic substance-dualist resource. That point is partly supported, and it is folded into D(c).
- **R7. No Many Worlds paragraph (L177).** Both flag it, for different reasons. ChatGPT says the advantage is overstated against scoping L50 ("declares that presupposition rather than securing it"). Claude says it is inconsistent with `concepts/haecceity` L187 ("not a soul-substance"). Both are verified and both sit in task B(c).

## Singleton Findings

Findings from only one reviewer are not upgraded. Where they share a task with a convergent cluster they ride at that task's tier, which is a property of how the tasks were bundled, not extra weight on the singleton.

- **ChatGPT 5.6.sol Pro**: the Bailey–Rasmussen–Van Horn haecceity misattribution (verified; task A(b), P1). L163's slide from a persisting agent to a non-physical one (scoping L44; task B(b), P1). The L67 definition excludes substance-bearing property dualism (task B(d), P1). The unsourced «faster microtubule dynamics may relax the requirement further» (task E(a), P1). McKemmish et al. 2009 omitted (task E(d), optional). Declined at processing: Chalmers "causally miscontextualised", the L79 neural-dependence charge, the multidimensional taxonomy matrix, and a dependency table on the scoping page.
- **Claude Fable 5.1**: the Pautz splice (raw-verified twice; task D(e), P1; see D1). Pautz's own complexity premise and his "no strong argument" aim (task D(e), optional). Chalmers's SEP-reported later preference for substance dualism (task F(a)). The Jackson recantation (task F(b)). "Chalmersan" misspelt and unscoped at L133 (task F(d)). "Substance" never defined (task F(e)). The missing `bi-aspectual-ontology` link (task F(f)). L3's "The Map accepts either", which is false given that L175 excludes epiphenomenalist property dualism (task B(f)). Kim's two-souls rejoinder and the "live unpaid debt" concession (task A(b), optional). Claude methodology items 2 and 3 (bedrock lists; confession-without-correction) are on NEEDS-HUMAN addenda. Disputed or unverified at processing: the "three incompatible self-descriptions", the survival contradiction, sibling fixes that have already landed, the Searle 2002 dilemma, Pitts 2019, Weir 2024, and "Chalmers 2016, 24" as a primary source.

## Divergences

- **D1. ChatGPT vs Claude on the Pautz quotation.** ChatGPT said the quotation is real and only its scope is too narrow; Claude said it is spliced. The raw 2015 draft supports Claude on fidelity ('Though called' 0 hits) and ChatGPT on scope (primitivist Russellian monism). Task D(e) now carries both corrections.
- **D2. ChatGPT vs Claude on "the Map accepts either view".** ChatGPT says the claim is defensible at tenet level and needs recalibration. Claude says it should be deleted as a headline and calls it a "fudge". The Map's `tenets/background-commitments` L58 ("the neutrality is honest *at the tenet level*") supports ChatGPT, so task B recalibrates rather than deletes.
- **D3. ChatGPT vs Claude on which way the substance dependency runs.** ChatGPT says a persisting agent need not be non-physical and that haecceity could attach to a physical subject, which would make the substance lean weaker than the article implies. Claude says property dualism cannot carry Tenet 4 or the free-will commitments, which would make it stronger than the article admits. The scoping page supports ChatGPT on the inference (L44, Steward's animal and O'Connor's organism; L50). Background-commitments L58 supports Claude only on the operational lean. The two corrections are compatible: the lead should state the operational dependency, and the body should not slide from "persisting" to "non-physical". Task B's preamble carries both.

## Length Budget (run order)

The article is 3,002 words by `analyze_length`. The concepts hard threshold is 3,500 with gate `>=`, so the last safe count is 3,499 and the headroom is 497. The six tasks' caps are A +90, B +70, C +70, D +75, E +95 (or +45 without the optional McKemmish clause) and F +75, which sum to **+475 → 3,477**, or 3,427 with E at +45. That leaves 22 words of slack if every task spends its full cap. Two P3 sweeps also draw on this page: the Born-wording sweep (+2 at L173) and the Luo sweep (the L129 Luo clause; it should take its zero-word link option here if headroom is short). After the upgrades all six tasks are P1, and the picker takes P1s in file order: **A → B → C → D → E → F**. Each fork must re-measure before editing and stop at 3,499. F runs last, and its own fallback ("if fewer than 75 words remain below 3,499, do (c) and (a) only") governs. Every task's preamble carries this run order, because a fork receives a task's Notes but not its `Synthesis` field.

## Reviewer Reliability

- **ChatGPT 5.6.sol Pro** read the live article and siblings and gave line-checkable Map-side claims. Its processing pass verified almost all of them, with five declined as false alarms, already present, or framework-level. Its one material error was source-side. It vouched for the Pautz quotation from search snippets after PhilPapers returned 403, and its own processing note had already marked the scope claim as snippet-only.
- **Claude Fable 5.1** fetched the target article live and the key primary sources raw: the 1643 letters, Frankish 2016, the Pautz draft via Wayback, and SEP Dualism and Mental Causation. It was the more reliable leg on sources. Its sibling-page claims came from search copies, and three of them failed against the live corpus. It also over-recommended (DELETE the headline; "falsifies" L133).
- **Gemini 3.1 Pro**: abandoned (pipeline stall). No reliability signal.

## Method Notes

- **Rule applied.** A task was upgraded only when its headline defect was a two-reviewer claim that held against the live file and, where a source was involved, the raw text. All five P2s met this rule. F met it on locus (c) alone, which is also its first-priority locus. A was already P1, and no task went above P1.
- **No deduplication.** The Claude leg corroborated the five ChatGPT-leg tasks through indented `**ADDENDUM**` paragraphs instead of minting duplicates, and its one new task covers loci that no ChatGPT task owned. All six tasks were kept, so the active count is unchanged (386 → 386).
- **Todo edits.** Per task: the heading tier changed in place (B–F only), `Review file` became `Review files` listing both reviews, a `Synthesis` line was inserted directly below it (above `Notes`), and the opening "From outer review 2026-11-06" label of the Notes was replaced with the convergent preamble. Every other field, the Notes body and all addenda are untouched. `git diff --stat` shows 23 insertions and 17 deletions: 5 headings, 6 review lines, 6 Notes openings and 6 new Synthesis lines.
- **Independent re-fetches** for this synthesis were the Pautz Wayback PDF, the Frankish eprint, the earlymoderntexts 1643 PDF, and the Crossref and OpenAlex records for Zimmerman 2010. The OUP abstract page returned 403.
- **Line numbers** refer to the live `obsidian/` text at 06:20–06:28Z on 2026-11-06, before any of the six tasks has run.
