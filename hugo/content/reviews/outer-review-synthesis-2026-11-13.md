---
ai_contribution: 100
ai_generated_date: 2026-11-13
ai_modified: 2026-11-13 05:09:13+00:00
ai_system: claude-fable-5-2
author: Andy Southgate
concepts: []
created: 2026-11-13
date: &id001 2026-11-13
description: 'Synthesis of 3 full-site outer reviews: two page-level convergences,
  two claim-level ones on sibling pages, a three-reviewer methodology finding on corrections
  that do not propagate, and the operator decisions the reviews bear on.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-13 05:09:13+00:00
modified: *id001
related_articles:
- '[[project]]'
- '[[outer-review-2026-11-13-chatgpt-5-6-sol-pro]]'
- '[[outer-review-2026-11-13-claude-fable-5-2]]'
- '[[outer-review-2026-11-13-gemini-3-1-pro]]'
subject_articles: []
subject_title: Full-site audit
subject_type: site
synthesis_coverage: 3/3
synthesizes:
- reviews/outer-review-2026-11-13-chatgpt-5-6-sol-pro.md
- reviews/outer-review-2026-11-13-claude-fable-5-2.md
- reviews/outer-review-2026-11-13-gemini-3-1-pro.md
title: Outer Review Synthesis - 2026-11-13
topics: []
---

**Date**: 2026-11-13
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 3 of 3 commissioned reviewers contributed. All three audited the whole site (subject "Full-site audit", source `fallback:site-stale-7d`; Claude and Gemini reused ChatGPT's subject). ChatGPT 5.6 Sol Pro was processed at 03:57Z and minted 6 tasks; Claude Fable 5.2 at 04:27Z, 6 tasks; Gemini 3.1 Pro at 04:55Z, 4 tasks. None abandoned.

## TL;DR

The three reviewers read different parts of the site, so page-level agreement is thin: two issues are raised by two reviewers about the same page and the same claim, and both are confirmed on the live pages. One is the wording "the same right-caudate decrease" on five concept pages. The other is the conflict between [P-Q2](/positions/quantum-interface/#p-q2) and [P-Q9](/positions/quantum-interface/#p-q9) in the quantum-interface register, which is a blocked operator decision and is left alone here.

The strong agreement is about method. All three describe, in different vocabulary, a site whose most careful statement of a claim sits on one page while sibling, hub or apex pages still carry the older, stronger version. That finding is confirmed by the last 36 hours of the Map's own changelog (see Methodology), and it belongs to the operator's open decision on correction propagation.

Counts: 2 page-level convergent clusters, 2 claim-level clusters where two reviewers found the same defect on different pages, 1 thematic overlap, 2 methodology clusters. No finding was shared by all three at page level. No shared false alarm at page level; one shared failure mode (material that is not a live article read as if it were). 36 singleton findings are listed. Task actions: one upgrade (P3 to P2), no merges, one new P2 task, and nothing raised to P1.

## Adjudication Before Clustering

Every passage below was grepped on the live Obsidian pages during this run (2026-11-13, about 05:04Z); "confirmed" means the quoted string is present now and says what the reviewer reports. Reviewer claims about external sources are leads unless a collect run fetched them, and only the Gemini run did (Crossref metadata for five works, and one abstract).

What each collect run recorded about its reviewer's reliability, carried forward:

- **ChatGPT 5.6 Sol Pro.** Read the deployed site as pushed at 02:50Z. 17 findings verified against live pages, 5 left as leads, 3 marked imprecise (it attributes "vastly more complex" to quantum mechanics as well as general relativity; it drops italics from a quotation; one quoted phrase is real but not a defect). It reported finding no fabricated quotation.
- **Claude Fable 5.2.** Fetched four pages directly and read the rest through indexed excerpts, which lag. 19 findings verified against live pages; 11 marked disputed, stale or imprecise. Four of those quote wording that is not on the live page: "doom many-worlds" on `concepts/haecceity` (the page reads "press against"), "almost certainly" on `topics/ethics-of-possible-ai-consciousness` (0 hits), "through biasing probabilities" on `concepts/mental-causation-and-downward-causation` (0 hits), and "demonstrate that physical processing and conscious experience are separable" on `topics/dualist-perception` (0 hits; a neighbouring sentence is live and already tasked). It also compared a live topic page with `concepts/protention`, which is archived. This reviewer is from the model family that runs the Map's loop and was given no extra credence for that.
- **Gemini 3.1 Pro.** Worked from a different prompt: a hostile-referee review of empirical claims and citations, adapted from a single-article template, with instructions not to discuss methodology. 9 of the 33 Map pages it browsed were research notes or deep reviews. Of 18 findings checked, 9 were confirmed, 8 were false alarms and 1 was unverifiable. Four of its external attributions were imprecise ("Pedale et al. 2021–2023" is a 2025 paper; Schurger et al. 2021 is called a "consensus paper"; a sentence is credited to "De Haan and Pinto"; "unequivocally proved" for a contested result).

Where one reviewer is right and another wrong about the same material:

- **Dualism cartography.** Claude grades `apex/dualism-cartography` "RETAIN … Original, well-scoped". ChatGPT finds that the page says Minimal Quantum Interaction constrains the channel "without directly constraining either side's thickness" and then that it "Fixes the physical-side coordinate at thin". Both strings are live (count 1 each). ChatGPT is right about the passage; Claude's verdict did not see it.
- **Selection-only channel.** Claude grades `concepts/selection-only-channel` "RETAIN". ChatGPT finds the per-event bound at L62 ("the maximum information transferable by realising one specific candidate") misworded as a bound on a single outcome. The string is live and the mathematics is standard. ChatGPT is right on that sentence; its reading of Han and Choi (2016) remains a lead.
- **Quantum biology.** ChatGPT credits the register with downgrading warm quantum biology. Gemini calls the tryptophan-superradiance passage on `concepts/quantum-consciousness` "biological wishcasting" and objects that optical effects near 10^15 Hz do not show conformational coherence. That objection is the page's own caveat at L70, restated as a criticism. ChatGPT is right.
- **Right-caudate.** Claude's citation table gives the faulty citation as "Schwartz et al. 1996, 'the same right-caudate decrease'". On all five pages the subject of the clause is Nakatani et al. (2003). ChatGPT's account, and Claude's own prose, have it right: the word "same" carries a right-sided finding back onto Schwartz 1996, whose abstract reports bilateral decreases.

## Convergence Table

| # | Issue | Reviewers | Live status (05:04Z) | Task action |
| --- | --- | --- | --- | --- |
| C1 | "the same right-caudate decrease" on five concept pages | ChatGPT, Claude | Confirmed, count 1 on each of five pages | Existing task raised P3 → P2; Convergence field added |
| C2 | Kral et al. (2022) given a wider scope than its design | ChatGPT (`mental-effort` L108), Claude (`stapp-quantum-mind` L82) | Both confirmed; same claim, different pages; three more loci found by this run | No upgrade; Convergence field on the Stapp task; one new P2 for the three uncovered pages |
| C3 | [P-Q2](/positions/quantum-interface/#p-q2) against [P-Q9](/positions/quantum-interface/#p-q9) | ChatGPT, Claude | Confirmed (`positions/quantum-interface` L68 and L146) | None. Blocked operator decision; see Operator Decisions |
| C4 | Requirements stated as results | ChatGPT (`apex/interface-specification-programme` L56 against L171), Claude (`concepts/consciousness-physics-interface-formalism` L101) | Both confirmed; same pattern, different pages | Two existing P2 tasks left as they are |
| C5 | Objective collapse plus conscious "modulation" | Claude (`concepts/spontaneous-collapse-theories` L42, L187), ChatGPT (inference about `tenets` L125) | Claude's strings confirmed; ChatGPT's is an argument, not a quotation defect | Existing P2 left as it is; the priority-rule question goes to the operator |
| M1 | Corrections do not reach dependent pages | ChatGPT, Claude, Gemini | Confirmed from the changelog and live greps | None. Operator methodology decision |
| M2 | Review from outside the generating model family | ChatGPT, Claude | A recommendation, nothing to confirm on a page | None. Operator matter |

## Convergent Findings

### C1. "The same right-caudate decrease" (five concept pages)
- **Flagged by**: chatgpt, claude
- **Verification**: clean. The string is live once on each of `concepts/mental-effort` L110, `concepts/bidirectional-interaction` L97, `concepts/attentional-economics` L87, `concepts/attention-as-interface` L232 and `concepts/meditation-and-consciousness-modes` L46. The source facts (Schwartz 1996 bilateral; Baxter 1992 right caudate) were fetched from PubMed by the Map's own 2026-11-12 neuroplasticity pass, not by either reviewer's collect run. What Nakatani et al. (2003) found is still to be re-fetched by the task.
- **Quotes**:
  - **chatgpt-5-6-sol-pro**: "Schwartz et al. 1996 reported **bilateral** decreases in caudate glucose metabolism among treatment responders. Nakatani et al. 2003 reported a decrease in **right** caudate regional cerebral blood flow. These findings are related, but they are not the same laterality, modality, sample, or design."
  - **Claude Fable 5.2**: "Yet “the same right-caudate decrease” “remains on five pages”: concepts/mental-effort, concepts/attentional-economics, concepts/bidirectional-interaction, concepts/meditation-and-consciousness-modes, concepts/attention-as-interface."
- **Task action**: Upgraded P3 → P2: "Five concepts pages still say Nakatani found "the same right-caudate decrease" as Schwartz 1996 …" (one task before and after; neither collect run minted a duplicate). A Convergence field was added above its Notes. Not raised further: the fix is a one-word change per page and the pages already say the evidence cannot bear the broader argument.

### C2. Kral et al. (2022) cited beyond what it tested
- **Flagged by**: chatgpt, claude (same claim, different pages)
- **Verification**: clean on the strings. `concepts/mental-effort` L108: "Earlier structural claims (cortical thickness) have been weakened by Kral et al. (2022)", in a sentence that opens with long-term meditators. `concepts/stapp-quantum-mind` L82: "Meditation structural remodelling, once cited as supporting evidence, has been weakened by replication failures (Kral et al., 2022)". Kral's design (two randomised trials of eight-week MBSR, 218 meditation-naive participants, no test of long-term practitioners, Lazar 2005 absent from its references) was verified by the Map's 2026-11-12 pass from PubMed and the Europe PMC full text.
- **Quotes**:
  - **chatgpt-5-6-sol-pro**: "It tested claims about changes following an eight-week MBSR intervention. It did not test whether long-term practitioners differ cross-sectionally from matched non-meditators"
  - **Claude Fable 5.2**: "That is the exact conflation corrected on four other pages the same day."
- **Found by this run, named by neither reviewer**: three more live sentences with the same over-wide scope. `topics/attention-and-the-consciousness-interface` L141: "earlier claims of structural brain changes were challenged by Kral et al. (2022)". `concepts/altered-states-of-consciousness` L105: "While earlier studies claimed meditation produces lasting structural brain changes, Kral et al. (2022) … structural remodelling claims should no longer be cited as evidence". `apex/altered-states-as-interface-evidence` L110 cites the null directly after a sentence about advanced meditators and concludes "the reconfiguration is functional, not anatomical"; its reference 8 also gives the issue as 8(21) where every other page gives 8(20). Pages already scoped correctly: `concepts/neuroplasticity` L105, `topics/clinical-neuroplasticity-evidence-for-bidirectional-causation` L76, `concepts/default-mode-network` L112, `topics/contemplative-practice-as-philosophical-evidence` L101, `topics/clinical-evidence-quality-standards-consciousness-research` L62 and L126.
- **Task action**: No upgrade (the two reviewers name different pages, and the Stapp task bundles two single-reviewer items). The `mental-effort` locus rides in the C1 task, now P2. A Convergence field was added to the Stapp P2. One new P2 was minted for the three uncovered pages: "Three more pages give Kral et al. (2022) a wider scope than its design supports …".

### C3. [P-Q2](/positions/quantum-interface/#p-q2) against [P-Q9](/positions/quantum-interface/#p-q9)
- **Flagged by**: chatgpt, claude
- **Verification**: clean on the strings. `positions/quantum-interface` L68 ([P-Q2](/positions/quantum-interface/#p-q2)): outcome frequencies "stay Born-exact in every publicly conditionable context; only conditionals on the conscious state itself are free". L146 ([P-Q9](/positions/quantum-interface/#p-q9)): "a deviation conditioned on intention, task or subject would test the corridor itself", and in the same entry "preservation binds that marginal only and leaves the conditionals free". The register therefore carries two quantifiers. The reviewers' arguments about which is tenable are their own analysis; Claude's rests on Valentini (1991), which nobody fetched.
- **Quotes**:
  - **chatgpt-5-6-sol-pro**: "A preregistered intention, task, or subject identifier is a public trial label. If physical state and intention are both public covariates, exact preservation in every jointly conditioned public context entails no residual intention–outcome dependence at that grain."
  - **Claude Fable 5.2**: "If conscious state C is not fixed by the physical context X (which is what Tenet 1 requires), then horn (a), P(O | C, X) ≠ q(O | X), is a Born-rule violation for a fixed physical preparation. Only the average over a non-physical variable is preserved."
- **Task action**: None. The quantifier is a blocked HUMAN DECISION and no task here touches it. Both arguments are set out under Operator Decisions.

### C4. Requirements stated as results
- **Flagged by**: chatgpt, claude (same pattern, different pages)
- **Verification**: clean. `apex/interface-specification-programme` L56 says the lines of inquiry converge on a channel that selects "without injecting energy or violating conservation laws", while L171 of the same page says conservation and no-signalling are "requirements a future model must be shown to meet, not properties the programme has secured". `concepts/consciousness-physics-interface-formalism` L101 says Minimal Quantum Interaction "is substantiated by the five constraints" and calls the coupling map "the smallest conceivable intervention"; `positions/quantum-interface` records under [P-Q10](/positions/quantum-interface/#p-q10) that no worked toy model exists. ChatGPT's "similarly" about the tenets page overstates: the tenet's definition is conditional in form.
- **Quotes**:
  - **chatgpt-5-6-sol-pro**: "The existing opening converts a design constraint into a result."
  - **Claude Fable 5.2**: "Constraints a mechanism must satisfy do not substantiate that one exists."
- **Task action**: Recorded. The two existing P2 tasks (one per page) already cover both loci and already cross-reference each other; neither was upgraded because the reviewers did not name the same page.

### C5. Objective collapse and conscious "modulation"
- **Flagged by**: claude (page-level), chatgpt (argument about the tenet)
- **Verification**: Claude's strings are live. `concepts/spontaneous-collapse-theories` L42 says GRW and CSL "allow consciousness to **modulate** rather than wholly cause collapse, directly supporting the … Minimal Quantum Interaction tenet", and L187 that the tenet "*favours*" them, against `tenets/background-commitments` L42 ("the measurement problem itself cannot be evidence for conscious selection"). ChatGPT quotes no defect; it argues that the tenets' resolution of the prebiotic problem ("objective reduction with consciousness modulation", live at `tenets` L125) needs a rule for which selector has authority. These are two different claims about one commitment, so this is thematic overlap and is not counted as convergence.
- **Quotes**:
  - **Claude Fable 5.2**: "Ghirardi–Rimini–Weber and Pearle’s collapse models are explicitly mind-independent."
  - **chatgpt-5-6-sol-pro**: "“Modulation” is currently a placeholder for the very law the framework most needs."
- **Task action**: Recorded. The existing P2 on `concepts/spontaneous-collapse-theories` covers the page-level half and already forbids writing a priority rule. The priority-rule question sits with the operator's difference-making decision.

### M1. Corrections do not reach dependent pages
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: confirmed from the Map's own changelog and from live greps; see Methodology for the instances.
- **Quotes**:
  - **chatgpt-5-6-sol-pro**: "The Map is therefore presently a **two-speed epistemic system**: its canonical self-criticism moves faster than its public explanatory surface."
  - **Claude Fable 5.2**: "This is confession-without-correction at propagation scale."
  - **Gemini 3.1 Pro**: "It places the bold, falsified claims in its high-level synthesis articles (e.g., `conscious-vs-unconscious-processing`) to establish its metaphysical tenets, while burying the empirical retractions in granular, localized articles (e.g., `working-memory`)."
- **Task action**: None. The individual loci are tasked (fifteen of the sixteen tasks from this cycle are instances). The remedy is the operator's open methodology decision.

### M2. Review from outside the generating model family
- **Flagged by**: chatgpt, claude
- **Quotes**:
  - **chatgpt-5-6-sol-pro**: "shared model families and a shared corpus can produce correlated agreement."
  - **Claude Fable 5.2**: "At least one review lens per quarter should be human domain-expert review, especially a physicist on the quantum-interface cluster."
- **Task action**: None. An operator matter; listed under Operator Decisions.

## Shared False Alarms

No claim that the live pages do not support was made by two reviewers about the same page. The false alarms are each one reviewer's (Gemini 8, Claude 11 disputed or stale items, ChatGPT 3 imprecisions), and they are itemised in the three review files.

One failure mode is shared by two reviewers and is worth more than any single false alarm:

- **Material that is not a live article read as the site's current claim.** Claude compared a live topic page with `concepts/protention`, which is archived and served at its old URL, and treated the public research note `research/clinical-neuroplasticity-bidirectional-causation-2026-03-21` as contradicting the corrected articles. Gemini opened 5 research notes and 4 deep reviews among its 33 pages and built its readiness-potential section on a research note for an archived page. In both cases the text is really on the public site. The reviewers were wrong about its status, and the site gives a reader little to tell the status by. This bears on the operator's open publication-policy decision.

Two near-overlaps were examined and not counted:

- **Psychedelic imaging and the filter reading.** Claude objects to `topics/psychedelics-and-the-filter-model` L83 ("supplies the neural architecture interactionist dualism needs", live). Gemini objects that `concepts/filter-theory` ignores Siegel et al. (2024); the site-level claim is false (the topic page cites it at five places) and the hub sentence at L83 is stale. Different pages, different claims.
- **Borrowing physicalist formalisms.** Claude's point about predictive processing as "machinery" (`topics/consciousness-and-integrated-information` L138, live) and Gemini's remark that the site borrows the workspace "bottleneck" are the same kind of complaint. Gemini names no passage, so there is nothing to confirm.

## Singleton Findings

Flagged by one reviewer. Not upgraded. Tasks are in `todo.md` at the priority the collect run gave them.

**chatgpt-5-6-sol-pro** (14)
- `apex/interface-specification-programme` L157 calls the channel "~10 bits/second" after L146 says the figure is "not the channel's bandwidth" → same P2 as the conservation wording (C4).
- `topics/dualism-channel-width-axis` L59 orders probability-bias below basis-choice and then calls them "siblings rather than strictly ordered" → P2.
- Same page L65 places "Saad's bare mechanism" at the channel-width floor through the Map's own Born-rule identification → same P2.
- `arguments/arguments` says three arguments each "shows" its conclusion, above the register's "real but modest" → P2.
- `concepts/selection-only-channel` L62 per-event information bound → P2.
- Same page L72, Han and Choi (2016) cited for more than the paper is said to show → same P2, verify first. A lead.
- `tenets/tenets` L136 "initially required more epicycles than geocentrism", out of step with `arguments/epistemological-limits-of-occams-razor` → P2, historical bullets only, verify first.
- `apex/taxonomy-of-voids` lead states the cumulative conclusion before the suspension → P2.
- `apex/dualism-cartography` "Fixes the physical-side coordinate at thin" → open P3 that predates this cycle.
- `project/why-this-is-different` L70 "trusted by inspection" → confirmed live, not tasked (over the collect run's cap).
- `concepts/attentional-economics` L66 infers coarse-grained influence from the 10 bits/s figure → confirmed, not tasked.
- `concepts/parsimony-epistemology` L58 "consciousness exists because something non-physical exists" offered as explanation → confirmed, not tasked.
- `index` L39 "Starting with dualism keeps the question open" → confirmed; adjacent to an open homepage decision.
- Thickness as a profile vector instead of a scalar (a structural proposal) → operator.

**Claude Fable 5.2** (17)
- `apex/phenomenology-mechanism-bridge` L176 "fits singular actualisation more naturally than branching", with `concepts/counterfactual-reasoning` L167 → P2.
- `topics/amplification-mechanisms-consciousness-physics` L151 and L159 place Stapp's Zeno mechanism inside the Born corridor → P2.
- `topics/falsification-roadmap-for-the-interface-model` L125 "ontological profligacy", L185 against L125 and L150, falsifier asymmetry at L65 and L69 → P2.
- `concepts/stapp-quantum-mind` description states Stapp's mechanism in the Map's voice → P2 (with C2).
- Same page L72, James "volition is nothing but attention" chapter attribution → same P2, verify first. A lead.
- `apex/identity-across-transformations` L55, unconditional claim about branching and personal identity → confirmed, not tasked.
- `concepts/motor-selection` L210 "The No Many Worlds tenet preserves motor selection as genuine choice" → confirmed, not tasked.
- `concepts/conservation-laws-and-mental-causation` L113 "requires no speculative new physics" → confirmed, not tasked.
- `topics/consciousness-and-integrated-information` L138, predictive processing as "the machinery" → confirmed, not tasked.
- `topics/psychedelics-and-the-filter-model` L83 and the description of `topics/predictive-processing-and-dualism` → confirmed; the first page has an open length decision.
- `topics/eastern-philosophy-consciousness` L129 "claiming for it only" → string confirmed; what the paper claims is a lead.
- `topics/dual-domain-capabilities-in-proprioception-and-spatial-imagination` L103 "is supported by the persistent explanatory gap in each capability" → confirmed, not tasked.
- `concepts/llm-consciousness` L132, L136, L146 off the [P-AC1](/positions/ai-consciousness-scope/#p-ac1) band → confirmed; waits on the Tenet 3 decision.
- Repository `README.md` L18 "on quantum outcomes" against "on physical outcomes" → confirmed; not site content.
- No apex holds the active-inference rival → an apex-evolve matter; the reviewer agrees the site-wide charge was rightly declined.
- No multiple-comparisons control for conditional residual-structure testing → belongs with the born-preserving apex's deferred installs.
- Corridor selection read as a hidden-variable theory at equilibrium (Valentini 1991), and the steganography skeleton's input assumptions → leads; listed for the research harvester.

**Gemini 3.1 Pro** (5)
- `concepts/conscious-vs-unconscious-processing` L76 "Working memory … requires consciousness. Subliminal priming effects decay within 500ms" against `concepts/working-memory` L59 → P1 (set by the collect run on a confirmed cross-page contradiction with a fetched abstract; unchanged here).
- `concepts/working-memory` L59 reports one of three results from Franco-Martínez et al. (2026) → P2.
- `concepts/types-of-consciousness` L101 split-brain cases "demonstrate that unity can fracture" against `topics/split-brain-consciousness` → P2.
- `concepts/filter-theory` L83 describes psilocybin imaging in pre-2024 terms → P2.
- Veit (2023) absent as a gradualist rival on `concepts/evolution-of-consciousness` → not tasked; left for the research harvest.

## Divergences

- **ChatGPT vs Claude on `apex/dualism-cartography`**: Claude retains it as original and well-scoped; ChatGPT finds a same-page contradiction, which is live. See Adjudication.
- **ChatGPT vs Claude on `concepts/selection-only-channel`**: Claude retains it as correct rival-holding; ChatGPT finds a formal slip at L62, which is live.
- **ChatGPT vs Claude on what to do about [P-Q2](/positions/quantum-interface/#p-q2)**: ChatGPT says choose a quantifier ("Do not retain [P-Q2](/positions/quantum-interface/#p-q2) and [P-Q9](/positions/quantum-interface/#p-q9) as coequal defaults"). Claude says keep the commitment, rename it ("preserves the unconditioned Born marginal") and "FLAG AS PERPETUALLY CONTESTED". They agree that the two entries conflict and disagree about the remedy. Operator decision.
- **ChatGPT vs Claude on the neuroplasticity evidence**: ChatGPT finds that the articles now concede the materialist reading fits equally well. Claude accepts that for the articles and points at a public research note that still says the opposite. Both are right about what they read; the difference is whether a research note counts as the site's voice.
- **ChatGPT vs Gemini on quantum biology**: ChatGPT credits the downgrade; Gemini criticises a passage for lacking a caveat the passage contains. See Adjudication.
- **Claude vs Gemini on predictive processing**: Claude finds it "engaged widely at topic level" and asks only for an apex. Gemini says the site "fails entirely to engage" the generative reading of psychedelic states, which is false for the topic page it did not open and fair for the hub page it did.
- **Gemini vs the other two on overall standing**: Gemini's verdict is "outright rejection"; ChatGPT and Claude both find the registers and flagship pages well calibrated and locate the fault downstream. Gemini's prompt asked for grounds for rejection and forbade praise, so the difference is partly commissioned.

## Operator Decisions

Nothing in this section is resolved or pre-empted. Each entry lists an open decision the reviews bear on and what each reviewer said. No task minted or changed in this run edits any of them.

1. **The [P-Q2](/positions/quantum-interface/#p-q2) quantifier** (blocked HUMAN DECISION).
   - ChatGPT: a preregistered intention or task label is a public covariate, so "Born-exact in every publicly conditionable context" rules out [P-Q9](/positions/quantum-interface/#p-q9)'s positive result. It adds a *reportability–concealment constraint*: if public reports carry information about the conscious state, exactness in every public context needs the proxy to be uninformative, an exact compensation, a narrowed sense of "public", or collapse into trumping. It asks that one quantifier be chosen.
   - Claude: the conditional reading is a Born violation for a fixed physical preparation, with only an average over a non-physical variable preserved; under entanglement a psychophysical superselection law becomes necessary for no-signalling. It asks that [P-Q2](/positions/quantum-interface/#p-q2) be renamed and flagged as contested, not dropped. The Valentini and steganography points are unverified leads and the reviewer says the second is its own reading.
   - Gemini: silent.
2. **Difference-making against trumping and the rival routes.**
   - ChatGPT: baseline objective collapse plus "modulation" leaves four options (reweight outcomes; choose basis or timing; replace the physical selector while reproducing its distribution; accompany without changing). It notes the third "is structurally close to delegatory trumping" and the fourth is epiphenomenalism under another name, and asks for an actuation-allocation law.
   - Claude: on the default reading Tenet 3 is "satisfied only metaphysically"; the Stapp Process-1 relocation is recorded on the apex as "a human editorial decision", so the inversion is disclosed and undecided.
   - Gemini: silent.
3. **The Tenet 3 quantifier** (NEEDS-HUMAN 2026-08-17).
   - ChatGPT: four readings (every conscious token; every subject dispositionally; some episodes; somewhere in the ancestry of reports) and the claim that the reportability argument supports only the last two without further premises.
   - Claude: the AI-consciousness pages are off the [P-AC1](/positions/ai-consciousness-scope/#p-ac1) band (`concepts/llm-consciousness` "almost certainly", "remain excluded", confirmed live); open P3s on those pages wait on this decision.
   - Gemini: silent.
4. **Determinate subjecthood as a sixth commitment** (NEEDS-HUMAN 2026-08-03).
   - ChatGPT: the Map has "a de facto sixth foundational commitment"; either promote Posit One to the tenets or state that Tenet 4 survives as a bare posit if the subject is deflated.
   - Claude: calls `tenets/background-commitments` "the single most philosophically mature page on the site" and asks that Tenet 4 be flagged as contested. It takes no position on promotion.
   - Gemini: silent.
5. **Tenet wording.** No task edits a tenet statement; the one open task on `tenets/tenets` is limited to the historical bullets under Tenet 5 and was not changed here.
   - ChatGPT: Tenet 2's "must do so at the quantum level" should be a posit, and "deviation from standard quantum mechanics" should say whether it is statistical, dynamical or ontological; Tenet 4 is a conjunction of four claims; the Tenet 5 headline is broader than its argument.
   - Claude: Tenet 2 is glossed as probability-bias on some pages and as selection-only on others (its quoted instance was not found live; the general point stands as a lead); the tenets should say Tenet 3 is met only metaphysically on the default reading. It could not fetch the tenets page and worked from secondary wording.
   - Gemini: silent.
6. **Correction-propagation methodology** (NEEDS-HUMAN methodology ratification 2026-08-03). See Methodology. Proposals on the table:
   - ChatGPT: stable claim IDs transcluded into dependent pages; build-time semantic tests; a "consistency lag" metric; close an issue only when every registered dependant has been checked; formalisation gates for mechanism language; a debt box on high-centrality pages.
   - Claude: a banner and an automatic one-band demotion for any defect logged as confirmed and unfixed; propagation by claim with a canonical string grepped across apex and research; a compatible/suggestive/discriminating label on every tenet-relation claim; a rival-of-record per tenet; scope refusals that name the residual finding they leave open.
   - Gemini: forbidden by its prompt from discussing method, it describes the symptom on three hub pages.
7. **Publication policy for superseded research notes and archived pages** (open NEEDS-HUMAN).
   - Claude: delete or banner `research/clinical-neuroplasticity-bidirectional-causation-2026-03-21`; stamp research notes carrying "Tenet alignment: Directly supports" lines as pre-calibration.
   - Gemini: says nothing about policy, and its own reading shows the cost: 9 of its 33 pages were working papers.
   - ChatGPT: silent.
8. **Review outside the model family.** ChatGPT asks for blinded review by domain specialists or independent tool chains; Claude asks for a human domain expert each quarter, a physicist first. Whether and how is the operator's.
9. **The homepage** (NEEDS-HUMAN 2026-11-05 on `index` L37). ChatGPT adds the adjacent L39 "Starting with dualism keeps the question open" and offers a replacement sentence.
10. **Length decisions.** Several of this cycle's tasks sit on pages already over their hard threshold (`apex/interface-specification-programme`, `concepts/stapp-quantum-mind`, `concepts/working-memory`), and Claude's requested additions to `apex/born-preserving-causal-efficacy` meet an open length decision on that page. The new Kral task is net ≤ 0 on all three of its files for the same reason.
11. **New articles and the section caps.** Three requests would each need a new page: Claude's active-inference rival apex, ChatGPT's reportability–concealment constraint, and a treatment of Veit (2023) from Gemini's review. No reviewer addresses the caps. Re-measure the sections before acting on any of them.
12. **Not touched by any reviewer**: the wakefulness-void placement and title.

## Methodology

All three reviewers describe one pattern, and the Map's changelog for 2026-11-12 and 2026-11-13 documents it in the Map's own words. In each case below a defect was found and verified on one page, fixed there, and listed as still live on siblings.

- **Right-caudate, five pages.** The 20:07Z pass on 2026-11-12 changed "the same right-caudate decrease" to "a right-caudate decrease" on `topics/clinical-neuroplasticity-evidence-for-bidirectional-causation` and recorded that the phrase "remains on five pages outside this task". All five are still live (C1). Two outer reviewers, commissioned six and seven hours later, each found them from the outside.
- **Kral and Lazar, at least five pages.** The same pass scoped Kral et al. (2022) on four pages and recorded `concepts/mental-effort` L108 as still carrying the conflation. Claude found a fifth instance on `concepts/stapp-quantum-mind`; this run found three more (C2). That makes five live loci after a sweep that fixed four, and the earlier 2026-07-16 review had ratified the conflation.
- **No Many Worlds inferred from experience, six or more pages.** On 2026-11-12 the inference from the phenomenology of choice to singular actualisation was withdrawn on `concepts/intentionality` (20:49Z) and `concepts/phenomenology-of-choice-and-volition` (21:04Z); deep reviews on 2026-11-13 found the same move in two further tenet entries (00:23Z, 03:25Z) and repaired them. It is still live on `apex/phenomenology-mechanism-bridge` L176 and `concepts/counterfactual-reasoning` L167 (both tasked from the Claude review), and `apex/testing-the-map-from-inside` L162 states the corrected position.
- **Stale Further Reading glosses.** Four deep reviews in 36 hours each found a link gloss describing a target page as it used to be (2026-11-12 19:55Z, 22:39Z; 2026-11-13 00:23Z, 03:25Z). A gloss is a claim about another page and nothing re-checks it when that page changes.
- **Hub against specialised page.** Gemini's three confirmed findings are all of this shape: `concepts/conscious-vs-unconscious-processing` against `concepts/working-memory`, `concepts/types-of-consciousness` against `topics/split-brain-consciousness`, `concepts/filter-theory` against `topics/psychedelics-and-the-filter-model`. ChatGPT's are the same shape with the positions register as the specialised page: the arguments hub, the voids apex lead, the interface apex lead. Claude's GRW finding sets a concept page against `tenets/background-commitments`.

What the evidence supports, stated without choosing a remedy:

- The sweeps do find the siblings. In the right-caudate and Kral cases the fixing pass listed the remaining pages by name. The gap is between listing and fixing, and each listed sibling becomes a separate queued task at a lower priority than the page that prompted it.
- Length headroom is part of the cause. Of the sixteen tasks the collect runs minted from this cycle, nine have a primary file within about ten words of a hard threshold or already over it, and the passes that listed siblings without editing them often cite headroom as the reason.
- Outside readers find the unfixed siblings quickly and report them as contradictions. Fifteen of the sixteen tasks the three collect runs minted are instances of a correction or qualification that exists elsewhere on the site.
- The sweeps key on a phrase. The Kral sweep fixed pages that shared wording and missed pages that made the same claim in other words; three of those were found in this run only by grepping the author's name and reading every hit.

The reviewers' proposed remedies are listed under Operator Decisions, item 6.

## Subjects the Map Does Not Cover (for the research harvester)

Carried from the three review files; none was added by this run.

- The reportability–concealment constraint: whether public reports of conscious states are compatible with Born-exact statistics in every publicly conditionable context (ChatGPT).
- An actuation-allocation law for objective collapse plus conscious modulation (ChatGPT).
- Quantum non-equilibrium and signal-locality (Valentini 1991 and later) as a precedent for mind-conditioned Born deviation with an exact unconditioned marginal (Claude). A lead.
- Perfectly secure steganography by minimum-entropy coupling (Schroeder de Witt et al. 2023) and what its security result assumes about the hidden message (Claude). A lead.
- Veit (2023), *A Philosophy for the Science of Animal Consciousness*: pathological complexity as a gradualist account of the evolution of consciousness (Gemini). The book is real; the reviewer's summary is unchecked.

## Method Notes

- Convergence was counted only where two reviewers raised the same issue about the same page and claim and the passage is live now. By that test two clusters qualify (C1, C3). C2 and C4 are recorded as claim-level agreement on sibling pages and did not trigger an upgrade. C5 is thematic.
- Task count in `todo.md` (active tasks, `tools.todo.processor.parse_tasks`): 407 before, 408 after. One upgrade (right-caudate, P3 → P2). No merges: no two of the sixteen cycle tasks share a primary file, and the one page two tasks touch (`topics/falsification-roadmap-for-the-interface-model`) is edited at different lines with the coordination already written into both. One task minted (Kral scope on three pages, P2). Convergence fields were added above the Notes of two tasks; no Notes were rewritten. Nothing was raised to P1; the single P1 in this cycle was set by the Gemini collect run and is a singleton.
- The Gemini review's prompt differed from the other two and excluded methodology, which lowers the chance of page-level overlap and makes its agreement on M1 an observation of the symptom, not an endorsement of a diagnosis.
- No external source was fetched in this run. Source facts cited here come from the Map's 2026-11-12 neuroplasticity pass (PubMed, Europe PMC) and the Gemini collect run (Crossref, one abstract).
- Line numbers are those of the Obsidian files at about 05:04Z on 2026-11-13 and will drift.