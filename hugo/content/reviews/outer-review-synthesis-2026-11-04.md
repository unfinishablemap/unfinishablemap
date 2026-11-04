---
ai_contribution: 100
ai_generated_date: 2026-11-04
ai_modified: 2026-11-04 07:05:51+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts:
- '[[thought-insertion]]'
- '[[depersonalisation]]'
- '[[illusionism]]'
- '[[witness-consciousness]]'
- '[[mine-ness]]'
- '[[meditation-and-consciousness-modes]]'
created: 2026-11-04
date: &id001 2026-11-04
description: Synthesis of 3 outer reviews of topics/phenomenology-of-agency-vs-passivity
  from 2026-11-04. 17 convergent clusters; five tasks went P2→P1; a false zero and
  a false two-leg claim from the collect passes corrected.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-04 07:05:51+00:00
modified: *id001
related_articles:
- '[[project]]'
- '[[outer-review-2026-11-04-chatgpt-5-6-sol-pro]]'
- '[[outer-review-2026-11-04-claude-fable-5-1]]'
- '[[outer-review-2026-11-04-gemini-3-1-pro]]'
synthesis_coverage: 3/3
synthesizes:
- reviews/outer-review-2026-11-04-chatgpt-5-6-sol-pro.md
- reviews/outer-review-2026-11-04-claude-fable-5-1.md
- reviews/outer-review-2026-11-04-gemini-3-1-pro.md
title: Outer Review Synthesis - 2026-11-04
topics:
- '[[phenomenology-of-agency-vs-passivity]]'
- '[[volitional-control]]'
- '[[predictive-processing-and-dualism]]'
- '[[free-will]]'
---

**Date**: 2026-11-04
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: all 3 commissioned reviewers contributed, and none was abandoned. All three reviewed one subject (`subject_type: recent`, `topics/phenomenology-of-agency-vs-passivity`). ChatGPT picked it as the recent-aged fallback, and Claude and Gemini reused it.

| Leg | Reply words | Reviewer's verdict | Processing outcome |
|---|---|---|---|
| ChatGPT 5.6 Sol Pro | 5,448 | "substantially better calibrated than its title and opening suggest", but "stronger as a descriptive inventory than as evidence for interactionist dualism" | read the page; every quoted span verifies; 3 tasks minted (P2) and convergence lines on Gemini's 2 |
| Claude Fable 5.1 (Research) | 6,522 | "DEMOTE-TO-COHERENCE-ONLY", with DELETE for "Against Illusionism" | read the page; about 45 quoted spans verify; sibling-page claims partly stale; 2 tasks minted (P2) and convergence lines on the other 5 |
| Gemini 3.1 Pro (Deep Research) | 3,698 | "entirely unready for academic submission and warrants outright rejection" | the subject page is absent from its used sources; W4 and W5 false; framing spine misattributed; 2 tasks minted (P2) |

The target has not changed since `c21b76f433` (2026-10-27). It measures 3,697 words by `analyze_length` (re-measured at 06:51Z) against a topics hard limit of 4,000. The gate is `>=`, so the ceiling is 3,999 and 302 words are usable. Every live line this synthesis relies on was re-checked with `grep -c -F`, against the positive controls "comparator" = 2 and "hinge" = 1.

## TL;DR

The dominant finding, on all three legs, is that the page's two arguments against deflation outrun its own concessions. The binding paragraph (L135) still calls intentional binding a "non-introspective measure of agency" that involuntary movements lack. The "must derive" demand (L133) never names the predictive-processing derivation that the page's own link target, `topics/volitional-control`, already concedes. And "Against Illusionism" (L143) answers the illusionist with meditative sharpening the illusionist already predicts, citing Lutz et al. 2008 for a result the paper does not report. That last citation finding is the cycle's most independent convergence: no prompt named it, and the full text confirms it.

There are 17 convergent clusters (C1–C17): four with all three reviewers and thirteen with two. There are also two partial clusters (X1–X2), six methodology convergences (M1–M6), six synthesis-pass observations (M7–M12), six rejected convergences (R1–R6) and seven divergences (D1–D7).

Task actions:

- **5 upgrades P2→P1**: binding and predictive processing (C1–C5, C17), "Against Illusionism" (C6–C7), thought insertion (C8–C9), clinical overreach (C10–C12), and the framework-only moves (C13–C16).
- **0 deduplications.** The ChatGPT and Claude passes had attached `Convergence` lines to existing tasks rather than minting siblings.
- **2 singleton tasks left at P2**: the L157 depersonalisation bullet, and the description / L79 / Rebouillat task.
- **The 2026-10-28 P3** (the Ciaunica 2024 null at L125) stays at P3, because only one leg cites it today.
- **Four collect-pass errors corrected in task Notes.** These are a false zero on "the most contested" (the sibling does say it); a false two-leg claim on L79; second legs missed on L89, L101 and the L133 Rajan clause; and a two-leg finding at L73 that no task covered.
- **Eight tasks share the page's 302 usable words.** Their worst-case total is +287, not the +277 the collect notes record. The run order is written into each task's Notes (see Length Budget and Run Order).

## Adjudication Before Clustering

A vote counts only if the reviewer's claim survived its processing pass against the live text and, where reachable, the primary source. Two reviewers making the same false claim is correlated error, not convergence. A claim that a collect pass marked false was re-checked before it was discarded.

**Gemini 3.1 Pro: claims excluded from every count.**

1. **The framing spine.** "causal interface void", "causal interface" and "interface void" each have 0 hits on the page, and `git log -S` finds none in its history. That void is the title of `voids/causal-interface`. Gemini's W1 framing (binding as a proxy for that interface) and W5's "inexplicable 'causal interface void'" are void.
2. **Quoted phrases from other pages.** "well-oiled hinge" has 0 hits (it lives on `concepts/skill-delegation` and in the 2026-07-17 deep review's strengths list). "luminous", "infallib…", "efferent", "corollary" and "forward model" also have 0 hits.
3. **The depersonalisation table row is invented.** "A failure of the conscious 'hinge' or a disturbance in primitive *ipseity*" matches no line. The page's "hinge" (L77) concerns the directedness of agentic time, and "ipseity" (L155) is Sass & Parnas on schizophrenia.
4. **W4 (neuroplasticity) attacks an inference the page disclaims.** L73: "it is equally predicted by therapy-induced plasticity on a physicalist account, so it fits effort as causal engagement without establishing it." "Norman et al., 2024" has no Crossref record, and "van den Heuvel, 2026" falls outside the prompt's window.
5. **W5 (comparator erasure) is false.** L119: "a comparator or higher-order model locates the sense of agency in circuitry distinct from the motor pathway and so predicts the same double dissociation." Ciaunica et al. 2022 is misapplied there.
6. **What survives.** W1's empirical core (binding is not selective to voluntary action; Hoerl et al. 2020, plus Suzuki et al. 2019 and Kong et al. 2024 from its source list), W3's core (the meditative argument begs the question), and W2 in part. W2's "total absence" is false, since L125 carries one active-inference anchor, but L133 does omit the predictive-processing derivation.

**Claude Fable 5.1: claims excluded.**

1. **Stale sibling-page claims.** The flat "depersonalisation shows the other (agency intact, ownership fading)" is gone from `topics/phenomenology-of-recursive-self-awareness`. Its L117 now reads "only on the Gallagher-style reading (ownership fading while felt initiation can persist …)", repaired in `c21b76f433`. The highlights claim "dissociates cleanly from motor output" has 0 hits in both trees, because the entry rolled off. The fetch tool blocked slug URLs, so Claude read indexed extracts.
2. **L139 "regime-stable" called false.** `concepts/depersonalisation` L79 says the separability of a felt dimension from "insight and much perception and cognition" holds on every reading. Only the agency limb depends on the reading, and L125 already says so.
3. **"Single-group" called inaccurate (L73).** It was one treated cohort with no control arm, so the phrase is defensible. Claude's other L73 point (the effort gloss) survives as C12.
4. **Two quotations from Laukkonen, Friston & Chandaria (2025)** ("computational theory of consciousness grounded in active inference", "altered states like meditation, psychedelics, and minimal states") have 0 hits in the abstract.
5. **Overreaches that survive in narrower form.** Lutz "says close to the opposite" (the verified verdict is that it does not report the claim; C7). Binding is not "non-introspective" because it is read from clock reports (the literature's word is "implicit"; C1). And L115's "real and not merely conceptual" conflates phenomenal with causal reality (rejected, R3).
6. **The structural verdicts** (DELETE "Against Illusionism"; rewrite "Disorders" from scratch; evidential-ladder tags on every item) are over budget, and the defects are already tasked in place (D7).

**ChatGPT 5.6 Sol Pro: claims excluded or counted as partial.**

1. **"A 2026 review concludes that binding reflects a mixture of perceptual and cognitive processes"**. It was not found at Crossref or PubMed, so it is unverified and uncounted.
2. **§7.3 (quantum degrees mapped without a bridge).** L169 already reads "may correspond" inside the Relation section (R2).
3. **One collect-pass rejection reversed.** The ChatGPT leg marked ✗ ChatGPT's statement that the sibling calls the agency reading "the most contested", recording 0 hits. That was a false zero. `concepts/thought-insertion` L36 ends: "The Unfinishable Map's other articles use the reading *ownership preserved, agency lost*, which is one of the five and the most contested." (`grep -c -F "most contested"` = 1). The sentence has been there since the page's creation commit, `2e296e55af` (2026-10-01), at character 731 of a 746-character line. ChatGPT's vote on C8 is therefore clean. An erratum was added to the ChatGPT review file, and the thought-insertion task's Notes were corrected (its old instruction said "do not quote it").

## Convergence Table

Line numbers in the Task column are 0-based `parse_tasks` indices after this synthesis's edits. Page lines (Lnn) are 1-based lines of the live article.

| # | Issue (page line) | ChatGPT | Claude | Gemini | Verdict | Task (line) | Action |
|---|---|---|---|---|---|---|---|
| C1 | Binding presented as a selective, validated agency measure (L135) | ✓ | ✓ | ✓ core only | verified | 4230 | P2→P1 |
| C2 | "would have no reason to distort" attacks a view nobody holds (L135) | ✓ | ✓ | — | verified | 4230 | (same task) |
| C3 | "must derive" omits the predictive-processing derivation (L133) | ✓ | ✓ | ~ partial | verified | 4230 | (same task) |
| C4 | "multiple independent lines" share one common cause (L137) | ✓ | ✓ | — | verified | 4230 | (same task) |
| C5 | Rajan 2019 measured no subjective agency (L133) | ✓ | ✓ | — | verified | 4230 | (same task); was recorded as ChatGPT-only |
| C6 | Meditative sharpening does not answer the illusionist (L143) | ✓ | ✓ | ✓ core only | verified | 4263 | P2→P1 |
| C7 | Lutz 2008 does not report sharpening (L143) | ✓ | ✓ overreach | — | verified (full text) | 4263 | (same task) |
| C8 | Thought insertion is not a "secure direction" (L125) | ✓ | ✓ | — | verified | 4293 | P2→P1 |
| C9 | The cited Sass & Parnas ipseity model cuts against a clean agency subtraction (L155) | ✓ | ✓ | ✗ misattributed | verified | 4293 | zero-word add-on |
| C10 | Utilisation behaviour is behavioural capture, not reported passivity (L159) | ✓ | ✓ | — | verified (abstract) | 4317 | P2→P1 |
| C11 | An involuntary memory is owned but unauthored (L89) | ✓ | ✓ | — | verified | 4317 | (same task); was recorded as Claude-only |
| C12 | Schwartz's effort gloss is reported as if measured (L73) | ✓ | ✓ | ✗ void (W4) | verified | 4317 | new optional (h); was untasked |
| C13 | Flow "still selects" is an unmeasured rescue (L109) | ✓ | ✓ | — | verified | 4342 | P2→P1 |
| C14 | "choosing not to choose" leaves no negative case (L149) | ✓ | ✓ | — | verified | 4342 | (same task) |
| C15 | L161 recasts the general hard problem as an agency anomaly | ✓ | ✓ | — | verified | 4342 | (same task) |
| C16 | L101 "must treat as primitive": rival accounts derive the regularity | ✓ | ✓ | — | verified (Beilock & Carr 2001) | 4342 | (same task); ChatGPT §9 was not counted before |
| C17 | No reference after 2019 in the empirical sections | ✓ | ✓ | ✓ | verified | 4230, 4263 | carried by the binding and illusionism P1s |
| X1 | Hypnosis "sense of agency is absent", uncited and with no rival named (L119) | ✓ | ~ | — | partial | 4317 (b) | rides with the P1 |
| X2 | "should be an active process" presumes agentive thinking (L155) | ~ | ✓ | — | partial | 4293 (c) | rides with the P1 |

## Convergent Findings

### C1. Binding is presented as a selective, validated agency measure
- **Flagged by**: chatgpt, claude, gemini (empirical core only)
- **Verification**: clean. L135 reads "provides a non-introspective measure of agency" and "involuntary movements do not" (1 hit each). The page's own link target, `topics/volitional-control` L128, holds binding "suggestive and contested" (1 hit). Suzuki et al. 2019 reports "identical magnitude-binding effects in both the presence and complete absence of intentional action" (abstract, OpenAlex). Hoerl et al. 2020 offers a unitary causal-belief account. The counterweight is Zhao, Dang, Gu, Fu & Haggard (2025, *Psychological Bulletin*, 75 studies), which finds action binding "increased for more volitional actions" and still calls binding "a reliable, quantitative measure of sense of agency" (D3). On the label: Claude's clock-report objection makes "non-introspective" inaccurate, and the literature's term is "implicit", which is the title of the page's own anchor.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "But the current wording—calling binding a non-introspective measure of agency and saying involuntary movements do not bind—is no longer adequate."
  - **Claude Fable 5.1**: "Suzuki, Lush, Seth & Roseboom (2019) found binding of identical magnitude with and without intentional action."
  - **Gemini 3.1 Pro**: "Crucially, the binding effect is reliably observed in contexts entirely devoid of intentional action."
- **Task action**: upgraded P2→P1: "`topics/phenomenology-of-agency-vs-passivity` L133–L137 still presents intentional binding as selective …". The `Review files` line now lists all three legs, a `Synthesis` line was added, and the Notes received the convergent preamble, COMBINE ADD-ON (h)–(j) and the run order.

### C2. "No reason to distort" attacks a view nobody holds
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L135 ends "An epiphenomenal consciousness would have no reason to distort temporal perception selectively for voluntary actions." L133, one paragraph earlier, grants the common-cause reply: "one neural process producing both the demand and the feeling". On epiphenomenalism the brain does the distorting.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The statement that an epiphenomenal consciousness would have “no reason” to distort temporal perception is also invalid as stated."
  - **Claude Fable 5.1**: "On epiphenomenalism, the *brain* produces the distortion, so the closing sentence attacks a straw man."
- **Task action**: the same P1, item (a). Deleting the sentence saves words.

### C3. "Must derive" omits the predictive-processing derivation
- **Flagged by**: chatgpt, claude; gemini partial (W2)
- **Verification**: clean. On the page, "predictive", "precision" and "sensory attenuation" each have 0 hits, and "active-inference" has 1, as the L125 depersonalisation anchor. `topics/volitional-control` concedes "Active inference predicts the dissociation table" (1 hit). `project/evidential-status-discipline` L165–L167 names predictive processing as the default rival for this cluster and names Laukkonen, Friston & Chandaria (2025) for phenomenology and meditation pages, so the page fails a standing Map gate. For effort specifically, Claude adds Shenhav, Botvinick & Cohen 2013 and Kurzban et al. 2013 (both real at Crossref).
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "This rival also directly answers one of the article’s central rhetorical questions: why effort and authorship attach to some demanding operations but not others."
  - **Claude Fable 5.1**: "Physicalist accounts already do derive it."
  - **Gemini 3.1 Pro** (partial): "The total absence of these models from a manuscript claiming to exhaustively map the phenomenology of agency constitutes an academic evasion that immediately disqualifies the text from serious peer review."
- **Task action**: the same P1, items (b), (f) and (g).

### C4. "Multiple independent lines" share one common cause
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L137: "The convergence of multiple independent lines of evidence (introspective, implicit, neuroplastic) makes a wholesale dissociation progressively less plausible". The paragraph never applies the common-cause reply that L133 grants.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Counting them as separate lines of support risks evidential double-counting unless the article shows that they depend on different assumptions and different causal pathways."
  - **Claude Fable 5.1**: "These lines are not independent."
- **Task action**: the same P1, item (c). The Wegner sentence in the same paragraph is protected by the 2026-07-17 stability note and is not touched.

### C5. Rajan 2019 measured no subjective agency
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L133 relates frontal theta in Rajan et al. 2019 to "subjective agency" (1 hit). The abstract (PubMed 29931088) contrasts choice cues with instruction cues and reads frontal theta as "indexing decision-making".
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Consequently, the article’s reference to a relation between the frontal-theta signature “and subjective agency” is not supported by Rajan et al."
  - **Claude Fable 5.1**: "It contains no measure of “subjective agency” or felt effort."
- **Task action**: the same P1, item (d). The collect passes recorded this as ChatGPT-only, but Claude §2.8 and §2.11 table row 12 agree. COMBINE ADD-ON (j) makes it required.

### C6. Meditative sharpening does not answer the illusionist
- **Flagged by**: chatgpt, claude, gemini (core only)
- **Verification**: clean on the page's own text. L143 grants the illusionist that the contrast is "'real' as a representation", then concludes that its deepening "is better explained by its tracking a real distinction than by its being an adaptive misrepresentation." Both siblings already concede the point. `concepts/witness-consciousness` L148: "the testimony is consonant with the Map's reading rather than evidence against its rivals". `concepts/meditation-and-consciousness-modes` L151: "Sharpening is in any case no evidence against illusionism". Gemini's "infallibility intuition" and its Kammerer characterisation are unverified and do not count.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Improved discrimination under training can indicate a more refined functional self-model. It does not show that the model’s apparent reference to conscious causal efficacy is veridical."
  - **Claude Fable 5.1**: "Trained discrimination of a modelled variable is not evidence that the variable is non-physical."
  - **Gemini 3.1 Pro**: "The manuscript attempts to defeat illusionism by pointing to the overwhelming subjective force of the illusion, entirely missing the fact that contemporary physicalist frameworks explicitly predict and functionally explain this exact subjective force."
- **Task action**: upgraded P2→P1: "… L143 "Against Illusionism" concludes the illusionist is answered by meditative sharpening …". The `Review files` line now lists all three legs, a `Synthesis` line was added, and the Notes received the convergent preamble, a COMBINE ADD-ON and the run order.

### C7. Lutz 2008 does not report sharpening
- **Flagged by**: chatgpt, claude. Gemini names Lutz only as dated literature.
- **Verification**: confirmed in the full text by the ChatGPT leg (PMC2693206). Against the positive controls "FA" = 32 and "OM" = 38, "agency", "agent", "passiv", "sharpen", "sharper" and "intention" each have 0 hits. Claude's "says close to the opposite" overreaches. The open-monitoring sentence ("the “effortful” selection or “grasping” of an object as primary focus is gradually replaced by the “effortless” sustaining of an awareness without explicit selection") describes what the practice aims at, not a finding about discrimination. None of the three prompts named Lutz or meditation, so this is the cycle's least prompt-seeded convergence (M7).
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The cited paper does not report that result."
  - **Claude Fable 5.1**: "Lutz, Slagter, Dunne & Davidson (2008) report no agency data."
- **Task action**: the same P1. The COMBINE ADD-ON says to rescope the citation without citing Lutz as counter-evidence.

### C8. Thought insertion is not a "secure direction"
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L125 reads "dissociates from agency in one secure direction" (1 hit). `concepts/thought-insertion` L36 calls the page's reading "one of the five and the most contested". L78 says the double dissociation "holds only on the agency reading", and L108 cautions this page by name ("reasons from the double dissociation", 1 hit). Martin & Pacherie 2013 (PubMed 23262256): "thought insertion primarily involves a disruption of the sense of ownership".
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The problem is that the article still calls thought insertion “one secure direction.”"
  - **Claude Fable 5.1**: "“Secure” is false."
- **Task action**: upgraded P2→P1: "… L125 says mine-ness "dissociates from agency in one secure direction" …". The `Review files` line now lists ChatGPT and Claude, a `Synthesis` line was added, and the Notes received the preamble, the "most contested" CORRECTION and the run order.

### C9. The cited ipseity model cuts against a clean agency subtraction
- **Flagged by**: chatgpt, claude. Gemini's "ipseity" row is misattributed to depersonalisation.
- **Verification**: clean. L155 already says that "Sass and Parnas's (2003) ipseity disturbance model situates this within a broader disruption of the minimal self." That is a rival to the agency reading, and it sits in the same bullet.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "accurate, but insufficiently integrated into the subsequent inference."
  - **Claude Fable 5.1**: "The target therefore contradicts a sibling page and the cited Sass & Parnas ipseity framework, which locates thought insertion in a disturbance of minimal self-presence, not a clean agency subtraction."
- **Task action**: zero-word add-on (e) on the thought-insertion P1: when hedging L155, use the existing Sass & Parnas sentence as the rival reading.

### C10. Utilisation behaviour is behavioural capture, not reported passivity
- **Flagged by**: chatgpt, claude
- **Verification**: clean at the abstract (PubMed 6850269): objects "compels the patients to grasp and use them", and "the presentation of objects implies the order to grasp and use them". There is no first-person passivity report. L159 reads "Passivity in the face of affordances replaces active selection." (1 hit).
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The article moves from observed behaviour and lesion anatomy to an unmeasured first-person state."
  - **Claude Fable 5.1**: "Listing it on an “axis” of agency *phenomenology* conflates a control deficit with a phenomenal one."
- **Task action**: upgraded P2→P1: "… states clinical and altered-state phenomenology more strongly than its sources …". The `Review files` line now lists ChatGPT and Claude, a `Synthesis` line was added, and the Notes received the preamble, a COMBINE ADD-ON and the run order.

### C11. An involuntary memory is owned but unauthored
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L89, under the heading "No authorship", reads "the sense of ownership is diminished or absent" (1 hit). L123 separates ownership from agency, so the page commits the conflation it warns against.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "An involuntary memory can lack authorship while retaining full ownership."
  - **Claude Fable 5.1**: "Involuntary memories are paradigmatically *owned* but unauthored."
- **Task action**: the same P1, item (g), one word. The collect pass recorded it as Claude-only.

### C12. Schwartz's effort gloss is reported as if measured
- **Flagged by**: chatgpt, claude. Gemini W4 attacks the same paragraph, but its vote is void.
- **Verification**: clean on the page. L73 reads "OCD patients who exert sustained mental effort to reframe intrusive thoughts show measurable decreases in caudate nucleus activity" (1 hit). The study measured caudate metabolism in behaviour-therapy responders and did not measure effort. Both processing passes missed this half. The ChatGPT pass judged the paragraph fair overall, and the Claude pass dealt only with "single-group".
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The article’s description of patients “exert[ing] sustained mental effort to reframe intrusive thoughts” is a plausible therapeutic gloss, but it is not how the experiment operationalised or measured the intervention."
  - **Claude Fable 5.1**: "The article’s gloss, “OCD patients who exert sustained mental effort to reframe intrusive thoughts,” is Schwartz’s later interpretive gloss, not the measured variable."
- **Task action**: new optional item (h) on the clinical P1. It is length-neutral, sits last in the work order, and asks the fork to read the abstract first. No other task owns L73.

### C13. Flow "still selects" is an unmeasured rescue
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L109: "Consciousness in flow still selects, only without resistance." (1 hit). L107 already draws the better conclusion, that the axis "involves at least two" dimensions.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "It is a protective framework stipulation."
  - **Claude Fable 5.1**: "The article’s flow passage (“Consciousness in flow still selects, only without resistance”) is an unfalsifiable rescue."
- **Task action**: upgraded P2→P1: "… protects the selection reading with framework-only moves …". The `Review files` line now lists ChatGPT and Claude, a `Synthesis` line was added, and the Notes received the preamble, a COMBINE ADD-ON and the run order. These are page-local labels, not the framework-wide falsifiability standoff that the 2026-07-17 stability notes protect.

### C14. "Choosing not to choose" leaves no negative case
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L149: "The practitioner's report is of consciousness choosing not to choose rather than of unconsciousness." (1 hit).
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "A framework in which every state is reinterpret-able as some level of selection has no clear negative case."
  - **Claude Fable 5.1**: "LFC and Ciaunica et al. (2022) model voluntary relaxation versus involuntary collapse of self-model precision (meditation versus depersonalisation) without positing a chooser outside the model."
- **Task action**: the same P1, item (b).

### C15. L161 recasts the general hard problem as an agency anomaly
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L161: "Why does the loss of authorship *feel* different from the loss of control, if both are just changes in information processing?" The question applies equally to red and green.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The unresolved issue is why any such state is phenomenal, which is the general consciousness problem."
  - **Claude Fable 5.1**: "This is the generic hard problem renamed."
- **Task action**: the same P1, item (c). Claude's DELETE route is allowed there, because it is net-negative.

### C16. "Must treat as primitive": rival accounts derive the regularity
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L101: "What the case supplies is a regularity such an account must treat as primitive" (1 hit). Beilock & Carr 2001 (abstract): choking was "eliminated by self-consciousness training. These findings support explicit monitoring theories of choking". `topics/free-will` says physicalism accommodates the same phenomenology "without a non-physical selector" (1 hit).
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The target still repeatedly implies that the physicalist must treat the patterns as primitive or merely accommodating."
  - **Claude Fable 5.1**: "False: Beilock & Carr (2001) found choking eliminated by self-consciousness training, supporting explicit-monitoring theories that derive it"
- **Task action**: the same P1, item (e), already recommended. The add-on records ChatGPT §9 as the second leg.

### C17. No reference after 2019 in the empirical sections
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean. The 17 references run to Rajan 2019, and Rebouillat 2021 is cited in the body but has no entry. The page was revised on 2026-10-27, and the binding and meditation literatures moved in 2019–2025.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The references are therefore **foundationally respectable but empirically stale**."
  - **Claude Fable 5.1**: "There is nothing from 2020–2026 on sense of agency, thought insertion, depersonalisation or utilisation behaviour."
  - **Gemini 3.1 Pro**: "The text operates in an artificially constructed intellectual vacuum, hermetically sealed against the neurocognitive and philosophical consensus of the 2020–2025 literature."
- **Task action**: carried by the binding P1, which adds 2019–2025 sources within ≤ +90, and by the illusionism P1's optional sources. Not a separate task (see M6).

### X1. Hypnosis: "absent", uncited, and with no rival named (partial)
- **Flagged by**: chatgpt (clean); claude (a different defect in the same sentence pair)
- **Verification**: L119 reads "the sense of agency is absent" (1 hit), with no citation. ChatGPT objects to the absolute; Claude objects to the missing citation and the missing cold-control account. Both say a physicalist generative account of hypnotic passivity goes unengaged: Martin & Pacherie 2019 (real at Crossref) and Dienes & Perner 2007 (unverified).
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The phenomenology of hypnotically suggested movement is relevant, but “the sense of agency is absent” is too absolute."
  - **Claude Fable 5.1**: "“Subjects report that their arm rises ‘by itself’” has no citation."
- **Task action**: the clinical P1, item (b). It does not carry the upgrade on its own.

### X2. "Should be an active process" presumes agentive thinking (partial)
- **Flagged by**: claude (clean); chatgpt (the same observation, aimed at the agency reading as a whole)
- **Verification**: L155 reads "has been stripped from what should be an active process" (1 hit). `concepts/doxastic-voluntarism` quotes Strawson (2003) that thought and judgement "neither are nor can be a matter of action".
- **Quotes**:
  - **Claude Fable 5.1**: "“Should be an active process” presupposes contested doctrine."
  - **ChatGPT 5.6 Sol Pro**: "Many thoughts arise without any felt production or selection but are not experienced as inserted."
- **Task action**: the thought-insertion P1, item (c), now recommended.

## Rejected Convergences

### R1. L79: "two legs flag it"
- The description task's Notes said "Two legs flag it". They flag different sentences. ChatGPT §4 targets the third sentence, "This sense of open alternatives disappears once the decision is made", writing "Likewise, counterfactual alternatives do not necessarily disappear once a decision is made." Claude §2.2 targets the second: "The “Counterfactual awareness” bullet (“You could have done otherwise”) builds libertarian content into the phenomenal description."
- **Rejected as a convergence.** These are two single-leg defects. A COMBINE CORRECTION in that task's Notes keeps item (b) as scoped (+2), leaves the declined third-sentence point alone, and keeps the task at P2.

### R2. L169: quantum degrees mapped onto phenomenal degrees
- ChatGPT §7.3: "The proposed progression from intensive selection through fluent selection to minimal or absent quantum influence is not derived from either the phenomenology or physics." Claude §2.7: "Under the Born-preserving corridor (apex #34) “degree of influence” is empirically invisible, so phenomenology cannot index it".
- **Rejected.** L169 already reads "may correspond to degrees of consciousness's influence on quantum outcomes" (1 hit), and it sits in the Relation to Site Perspective section, where tenet mappings belong. Claude's version treats empirical invisibility as if it ruled out correspondence. The framework P1 is told not to edit L169.

### R3. L115: lucid dreams
- ChatGPT: "Thus “lucid dreams restore the agency pole” should become:" (the first sentence). Claude's verdict row: "Phenomenal reality is conflated with causal reality" (the last clause, "demonstrating that the contrast is real and not merely conceptual").
- **Rejected as a convergence.** The two target different clauses. Claude's half misreads "real", which here means phenomenally real, as L59 says ("The contrast itself is a real datum"). ChatGPT's half stays a single-leg item, (c) in the clinical P1, and the add-on tells that task to leave the last clause alone.

### R4. The Schwartz paragraph as a whole
- Gemini W4 ("The manuscript isolates 1996 OCD neuroimaging data to claim that CBT efficacy proves dualist "downward causation,"") and Claude §2.8 ("“Single-group” is inaccurate: it is an uncontrolled responder/poor-responder comparison.").
- **Rejected.** Gemini attacks an inference L73 disclaims, and "single-group" is defensible. Only the effort-gloss half survives, as C12.

### R5. Depersonalisation mishandled across the page
- Gemini's table row ("A failure of the conscious "hinge" or a disturbance in primitive *ipseity*") and Claude §2.0 ("This is confession-without-correction in its pure form.").
- **Rejected as a convergence.** Gemini's row is invented. Of Claude's five sites, two are stale (recursive-self-awareness, highlights), and L139 is disputed (see Adjudication). The two that survive are L157 on this page and `apex/identity-across-transformations` L125 ("while perception continues unchanged", 1 hit). Both sit in the single-leg L157 P2, which stays at P2. Nobody edits L139.

### R6. Desmurget
- Gemini W5 ("deliberately suppressing the standard forward/comparator models"), Claude §2.1 ("The Desmurget result cuts against the article more than it admits.") and ChatGPT ("Its modest conclusion is also right").
- **Rejected.** These are three different claims with no shared defect. W5 is false (L119), and ChatGPT endorses L119's conclusion while asking for two caveats. Claude's "stimulation manufactures felt intention" is already conceded by L137's Wegner sentence ("the feeling can be present where the control is not"). ChatGPT's caveats remain optional item (e) of the clinical P1.

## Singleton Findings

Not upgraded; left at their original priority. Listed for the record.

- **Claude Fable 5.1**: the L157 depersonalisation bullet ("The entire experiential field shifts toward passivity", 1 hit), plus the apex L125 clause → P2 at line 4367. The frontmatter description overclaim ("struggle to explain", 1 hit), L79 "You could have done otherwise.", and Rebouillat 2021, which has 0 hits under `## References` → P2 at line 4394. L159 "every object they encounter" (Shallice et al. 1989) → clinical P1 (f). L165 "equally irreducible" → framework P1 (f), optional. Four reference-only entries → not tasked: a stable corpus convention, per the 2026-07-17 deep review L50. Not tasked as out of scope or over budget: L147 quantum biasing, first-rank-symptom nosology, utilisation localisation, cold-control theory.
- **ChatGPT 5.6 Sol Pro**: the L182 Further Reading label → framework P1 (d). L115 "restore the agency pole" → clinical P1 (c). L123 "theirs (agency)" wording → clinical P1 (d). The Desmurget caveats → clinical P1 (e), optional. Not tasked: L59's single axis, which is optional and length-neutral in the framework P1 (see D5); habit and choking mechanisms; the L79 third sentence and the L91 present-orientation claim; the multidimensional-profile and strongest-rival rewrites (over budget); sibling-page sync and apex labels (out of scope).
- **Gemini 3.1 Pro**: none beyond its votes on C1, C3 (partial), C6 and C17.

## Divergences

- **D1. Gemini vs ChatGPT and Claude, on comparator coverage.** Gemini says the page suppresses the comparator model. ChatGPT lists "Desmurget’s stimulation findings fit physicalist comparator models" among the page's concessions, and Claude says "The article concedes the last point". L119 supports ChatGPT and Claude.
- **D2. Gemini vs ChatGPT, on Schwartz.** Gemini says the page treats the PET result as proof of downward causation. ChatGPT: "The article commendably concedes the small, uncontrolled design and that ordinary therapy-induced plasticity predicts the result equally well." L73 supports ChatGPT.
- **D3. ChatGPT vs Gemini and Claude, on how far to downgrade binding.** ChatGPT: "Volition is one moderator of temporal binding, but binding is neither unique to voluntary action nor a validated direct measure of phenomenal authorship." Gemini: "The 2020–2025 literature has systematically dismantled the exclusive link between intentionality, volition, and temporal binding." Claude: "Add Suzuki et al. 2019 and Schwarz et al. 2019 as defeaters of binding-as-agency." The 75-study meta-analysis (Zhao et al. 2025) supports ChatGPT. The binding P1 adopts ChatGPT's calibration (add-on (i)), and Schwarz et al. 2019 stays uncited because no abstract was available.
- **D4. ChatGPT vs Claude, on bibliographic integrity.** ChatGPT: "Generally good; no obvious fabricated reference". Claude: "Citation integrity fails at the load-bearing points." Both are partly right. All 17 entries are real, but Rebouillat is missing and Lutz is not entailed. The four reference-only entries are a convention, not orphans.
- **D5. ChatGPT vs Claude, on the opening.** ChatGPT: "The article has identified a **family of related contrasts**, not a demonstrated scalar dimension." Claude retains the lede: "Uncontested; correctly stated in the lede". They address different claims (the scalar axis versus the reality of the datum), so the disagreement dissolves. L59 stays optional and length-neutral in the framework P1.
- **D6. ChatGPT vs Claude, on the 2026-10-27 depersonalisation repair.** ChatGPT: "The 27 October depersonalisation correction is well integrated." Claude calls it confession without correction. ChatGPT is right about L125. Claude is right about L157 and the apex clause, and wrong about L139 and two stale sibling sites (R5).
- **D7. Claude vs ChatGPT and Gemini, on the remedy for "Against Illusionism".** Claude: "**Delete “Against Illusionism”** in its entirety." ChatGPT: "That concession should replace the present claim that phenomenological deepening is better explained by a real causal distinction." The illusionism P1 rescopes in place within ≤ +20 and explicitly declines the DELETE route.

## Per-Reviewer Reliability

- **ChatGPT 5.6 Sol Pro: the most reliable leg.** It read the subject page, and every quoted span verifies, with one paraphrase-in-quotes ("Conscious re-engagement" for "consciousness re-engages"). All 21 PubMed IDs resolve. Once the "most contested" reversal is applied, none of its Map-internal quotations fails. It was also the only leg to calibrate against its own finding: it surfaced the 2025 binding meta-analysis and Hodson et al. 2024's "modest support" for predictive coding, and it resisted treating predictive processing as an all-purpose victor. One unverified source (the "2026 review" on binding). Weight: full.
- **Claude Fable 5.1: reliable on the page, unreliable on siblings.** About 45 quoted spans from the page verify, 14 of 14 added citations are real at Crossref, and its clinical coverage is the widest of the three. But it read sibling pages from indexed extracts, so two of its four propagation claims are stale. Two of its LFC quotations are not in the abstract. Its verdicts overreach in five places (Lutz "opposite", "non-introspective", L139, L115, the DELETE remedies). Weight: full on page-level findings, after stripping the overreach; none on sibling-page claims without a fresh grep.
- **Gemini 3.1 Pro: the least reliable leg; read the subject page through neighbours.** The subject article is absent from its 38 used sources, which include four sibling pages and five Map review pages, among them the 2026-07-17 deep review. That explains the misattributed spine, the "well-oiled hinge" quotation and the invented table row. Two of its five weaknesses are false. One citation cannot be found (Norman 2024), one falls outside the window (van den Heuvel 2026), and one is misapplied (Ciaunica 2022 in W5). Its surviving votes are the empirical cores of W1 and W3, and part of W2. This is the second consecutive cycle with the same pattern (see [reviews/outer-review-synthesis-2026-11-03.md](/reviews/outer-review-synthesis-2026-11-03/)). Weight: count a Gemini vote only where its point survives against the live page.

## Methodology Observations

### Reviewer methodology proposals that converge (record only; operator-reserved)

- **M1. Claim-entailment verification, not metadata verification.** ChatGPT item 13 and Claude items 3 and 6. The verified instance is Lutz 2008, which the 2026-07-17 deep review classed "real-correct" because it supported the framing. Both legs already added evidence to the NEEDS-HUMAN citation-entailment entry (todo line 1237), which now records 3 of 3 legs on one page.
- **M2. Propagate corrections by proposition, from a canonical page.** ChatGPT items 11 and 15 and Claude item 1. This page lagged three of its own link targets: `topics/volitional-control` L128 on binding, `concepts/witness-consciousness` L148 and `concepts/meditation-and-consciousness-modes` L151 on illusionism, and `concepts/thought-insertion` L36/L78/L108 on the agency reading. The 2026-11-03 synthesis recorded the same pattern (its M1).
- **M3. Standing gates must block publication.** Claude items 5 and 7 and ChatGPT item 18. The instance is the strongest-physicalist-rival gate (`project/evidential-status-discipline` L165–L167). It names Laukkonen, Friston & Chandaria 2025 for phenomenology and meditation pages, yet this page went through nine reviews with 0 hits for "predictive" and "precision".
- **M4. Check for a common cause before counting lines of evidence as independent.** ChatGPT item 16 and Claude §2.1(2). The page instance is C4.
- **M5. Clinical phenomenology needs patient testimony and current nosology.** ChatGPT item 19 (no redescribing behaviour as phenomenology without testimony) and Claude item 6 (check clinical sections against DSM-5-TR, ICD-11 and a named recent review, not against Map concept pages). The page instances are C10, X1 and the L157 bullet.
- **M6. Currency checks for fast-moving literatures.** ChatGPT item 20, Claude §2.9 and Gemini's whole report (C17). The weekly `literature-drift-review` exists but had not reached this page, whose newest reference is 2019.

Single-leg proposals, recorded only: ChatGPT item 14 (invalidate "durable convergence" after substantive edits; the July review's "durable convergence" verdict is the instance). Claude item 2 (reconcile body citations against References; Rebouillat today, Tegmark in the 2026-11-03 cycle, two consecutive days). Claude item 4 (meta-descriptions are claims; instantiated by the description P2).

### Observations from this synthesis pass

- **M7. Part of the convergence was planted by the prompts.** All three prompts named comparator, predictive-processing and binding accounts, and all three asked about bracketing to protect the tenets. Claude's prompt also named thought insertion, depersonalisation and utilisation behaviour. So C1–C4 and C13–C16 were prompt-seeded on every leg, and C8 and C10 on Claude's leg only (ChatGPT reached them unprompted). C6, C7 and C11 were named in no prompt. The upgrades here rest on the live-text greps and on the page's own link targets, not on vote counts. A future rule could discount a convergence on a rival framework the prompt itself named.
- **M8. A false zero in a collect pass discarded a correct reviewer claim.** "the most contested" sits at character 731 of a 746-character line on `concepts/thought-insertion`. The ChatGPT pass recorded 0 hits, marked the reviewer ✗, and wrote "do not quote it" into a task. A `grep -c -F` over the whole file finds it. Any ✗ that discards a reviewer quotation should come with its positive control.
- **M9. Convergence keyed on a line, not a sentence, manufactured agreement.** L79 (R1) and L115 (R3) each had two legs on one line but on different sentences with different defects. Key a convergence on the quoted sentence.
- **M10. Collect passes missed convergences with earlier legs' untasked sections.** L89 (ChatGPT §4), the L133 Rajan clause (Claude §2.8), L101 (ChatGPT §9), L155's Sass & Parnas sentence (both legs) and L73's effort gloss (both legs) were all recorded as one leg or not at all. Each pass compared its new leg against the earlier legs' tasks, not against their full replies.
- **M11. The shared-budget arithmetic drifted.** The collect notes carry "+277 of 302". Summing every task's stated cap gives +287 (90 + 20 + 10 + 30 + 10 + 5 + 30 + 92), because the ChatGPT pass counted its three caps of 10, 30 and 10 as 40. The slack is 15 words, not 25.
- **M12. Two reviewers did not read what they cited.** Gemini's used-source list omits the subject page for the second cycle running. Claude's fetch tool blocked slug URLs, so its sibling claims came from index extracts. Both failures show up as quotations that grep to 0 on the live page, and both legs' processing passes caught them.

## Length Budget and Run Order

Eight open tasks edit the article, which stands at 3,697 of 4,000 (gate `>=`, ceiling 3,999, 302 usable). Each task's Notes now ends with the same RUN ORDER AND SHARED BUDGET paragraph, which names its step. The queue sorts by priority and then by line (`select_queue_task`), which yields this order. The two other P1s in the queue are both blocked on human decisions.

| Step | Task | Line | Lines owned on the page | Cap | Worst-case total |
|---|---|---|---|---|---|
| 1 | P1 binding and predictive processing | 4230 | L133–L137 | +90 | 3,787 |
| 2 | P1 "Against Illusionism" | 4263 | L143, Lutz entry | +20 | 3,807 |
| 3 | P1 thought insertion (+ `concepts/thought-insertion` L108) | 4293 | L125 (existing sentences), L155 | +10 | 3,817 |
| 4 | P1 clinical overreach | 4317 | L73, L89, L115, L119, L123, L159 | +30 | 3,847 |
| 5 | P1 framework-only moves | 4342 | L59, L101, L109, L149, L161, L165, L182 | +10 | 3,857 |
| 6 | P2 depersonalisation bullet (+ apex L125) | 4367 | L157 | +5 | 3,862 |
| 7 | P2 description, L79, Rebouillat | 4394 | frontmatter description, L79, Rebouillat entry | +30 | 3,892 |
| 8 | P3 Ciaunica 2024 null (+ `concepts/thought-insertion` L58) | 2960 | an insert after L125's sentences | +92 | 3,984 |

That leaves 15 spare words at the worst case. The core edits are much smaller, because most items are length-neutral and several are net-negative (deleting the "no reason" sentence saves about 17 words). If an earlier task overruns, later tasks cut in this order:

1. Optional new reference entries in steps 1, 2 and 4. Link the existing Map page instead; step 1 keeps at most two new entries.
2. Step 4's optional (e) Desmurget clause.
3. Step 8's passage A, trimmed to the bare null plus its reference.

Step 7's Rebouillat entry fixes a defect and is not optional. No edit may bring the page to 4,000.

Where tasks meet on one line, the owner is named in every task:

- **L125.** Step 3 owns the existing sentences, and step 8 only inserts after them. Step 6 keeps "Actions feel automatic" so L125's pointer to the clinical sketch stays true.
- **L135.** Step 1 owns it. Step 8 drops its optional L135 clause.
- **L123.** Step 4 owns it. Step 3 re-anchors L125 on anarchic hand without editing L123.
- **L155 and L157.** Steps 3 and 6, kept parallel.
- **L139 and L169.** Nobody (R5, R2).
- **References.** Every step adds its own entries alphabetically and removes none.

## Method Notes

- **Rule applied.** A cluster was upgraded only if at least two legs flagged it and their findings verified against the live text. The rule excluded every Gemini vote except C1, C3 (partial), C6 and C17. Each of the five upgraded tasks has at least one two-leg finding that is required, not optional.
- **No upgrade went past P1.** Five tasks on one page now sit at P1, and they will run consecutively, because the queue's only other P1s are blocked. That is why the run order and line ownership were written into every task rather than left to each fork's re-measurement.
- **Todo edits.** Five headings were changed P2→P1 in place. Five `Review file` lines became `Review files`, and five `Synthesis` lines were inserted above `Notes`, so the blocks after line 4226 moved down by one to five lines. Each convergent task's Notes received the convergent preamble and a COMBINE ADD-ON. The two singleton P2s received a COMBINE NOTE or CORRECTION, and all eight tasks received the RUN ORDER paragraph at the end of their Notes, which `task_to_skill` passes to the fork. `parse_tasks` still returns 322 active tasks, and P0–P2 stays at 24 (P1 7, P2 17). No article was edited. The ChatGPT review file received a dated erratum for the "most contested" reversal.