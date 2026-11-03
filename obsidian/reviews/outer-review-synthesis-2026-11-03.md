---
title: "Outer Review Synthesis - 2026-11-03"
created: 2026-11-03
modified: 2026-11-03
human_modified: null
ai_modified: 2026-11-03T05:48:18+00:00
draft: false
description: "Synthesis of 3 outer reviews of topics/motor-control-quantum-zeno from 2026-11-03. Ten convergent clusters; three tasks went P2→P1, one P1 held, and the 11-01 ~1 kHz P3 stays put."
topics:
  - "[[motor-control-quantum-zeno]]"
  - "[[volitional-control]]"
  - "[[quantum-neural-timing-constraints]]"
  - "[[attention-and-the-consciousness-interface]]"
concepts:
  - "[[motor-selection]]"
  - "[[stapp-quantum-mind]]"
  - "[[libet-experiments]]"
  - "[[quantum-zeno-effect]]"
  - "[[decoherence]]"
  - "[[post-decoherence-selection]]"
related_articles:
  - "[[project]]"
  - "[[outer-review-2026-11-03-chatgpt-5-6-sol-pro]]"
  - "[[outer-review-2026-11-03-claude-opus-5-5]]"
  - "[[outer-review-2026-11-03-gemini-3-1-pro]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-03
last_curated: null
synthesizes:
  - reviews/outer-review-2026-11-03-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-11-03-claude-opus-5-5.md
  - reviews/outer-review-2026-11-03-gemini-3-1-pro.md
synthesis_coverage: "3/3"
---

**Date**: 2026-11-03
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: all 3 commissioned reviewers contributed, and none was abandoned. All three reviewed one subject (`subject_type: recent`, `topics/motor-control-quantum-zeno`, "Consciousness and Motor Selection"). ChatGPT picked it as the recent-aged fallback, and Claude and Gemini reused it.

| Leg | Reply words | Reviewer's verdict | Processing outcome |
|---|---|---|---|
| ChatGPT 5.6 Sol Pro | 5,210 | "Major revision"; "a serious piece of dualist advocacy and is more self-critical than many discussions of quantum consciousness" | 11 verified, 3 partial, 2 unverified, 4 disputed; 4 tasks (P1, P2 ×3) |
| Claude Opus 5.5 (Research) | 4,902 | "major revision. The article is unusually candid for a dualist mechanism piece." | 7 verified, 3 partial, 7 rejected; 3 tasks (P2 ×3) plus convergence lines on the 4 ChatGPT tasks |
| Gemini 3.1 Pro (Deep Research) | 3,962 | "scientifically and philosophically unsound and must be firmly rejected" | most "article" quotations come from other pages; 3 of 5 weakness sources fail; 0 tasks, 2 convergence lines |

The target has not changed since refine `a177eddf41` (2026-10-27). It measures 3,544 words by `analyze_length`, re-measured at 05:40Z, against a topics hard limit of 4,000. The gate is `>=`, so 455 words are usable. Every live line this synthesis relies on was re-read with `grep -c -F` at 05:40Z.

## TL;DR

The dominant convergence is that the article claims more for its evidence than the evidence gives it, at both ends. In the neuroscience, the Libet section overstates Schurger ("The answer has largely arrived", "an artifact of averaging neural noise"), cites no RP work after 2012 apart from Sjöberg's essay, and then reuses Libet's ~200 ms W-time as the window in which the agent acts. All three reviewers name the dated evidence base and the W-time reuse. In the mechanism, the article credits Stapp's Zeno hold with choosing which motor outcome actualises, though on Stapp's own account, and on the Map's `motor-selection` and `stapp-quantum-mind` pages, the agent chooses only the question. ChatGPT and Claude verify that point, and also the one-horn Georgiev gloss and the missing Tegmark 2000 reference.

There are ten convergent clusters (C1–C10): two have all three reviewers and eight have two. There are also four partial clusters (X1–X4), four methodology convergences (record only), three rejected convergences (R1–R3) and seven divergences (D1–D7). Gemini contributes clean votes only to C5 and C6.

Task actions:

- **3 upgrades P2→P1**: Libet/RP calibration (C4–C6), compatibility-as-location (C7–C8), and the Müller & Rabbitt "~300ms" sweep (C9).
- **1 held at P1**: Stapp question-versus-answer (C1–C3), because the skill caps upgrades at P1.
- **0 deduplications.** The Claude and Gemini passes had attached `Convergence` lines to the ChatGPT tasks rather than minting siblings.
- **0 upgrades for the 2026-11-01 P3** on `topics/quantum-neural-timing-constraints` L143 and `concepts/decoherence` L131 (~1 kHz). ChatGPT confirms it, but no second reviewer names either file (R3). A zero-word seam note was added instead.
- **3 singletons left at P2**: Bourget, the Zeno-timing satellites and the Libet satellites. Bourget's Notes received the run order and one zero-word add-on.
- **Five tasks share the article's 455-word headroom.** They are committed to +305, or +348 with every optional item. Their run order is recorded in each task's Notes (see Length Budget and Run Order).

## Adjudication Before Clustering

A vote counts only if the reviewer's claim survived its processing pass against the live text and, where reachable, the primary source. When two reviewers make the same false claim, that is correlated error, not convergence. A Gemini vote counts only where its point survives against the live article.

**Gemini 3.1 Pro: claims excluded from every count.**

1. **Most of its "article" quotations come from other pages.** The four-stage "unified mechanism", "reflects what the agent is trying to do", "consciousness would enter as a bias on which prepared option wins", "stabilised plan would gain a persistent advantage", "Born-governed" and "tendency to dissipate" all come from `concepts/motor-selection`. "A purely classical account of neural selection is simpler and adequate to the physics as measured" and "the physics is settled, the neural application speculative" come from `concepts/quantum-zeno-effect`. Each has 0 hits on the article. Its whole "False Equivalence with Biological Precedents" section (radical pairs, cryptochrome, "MHz–GHz band") also has 0 hits; the caveat it attacks is `quantum-zeno-effect` L65's own.
2. **"The manuscript claims a coherence window of 10⁻⁵ seconds" and "ignores" decoherence.** This inverts L115. The article reports Tegmark, says Hagan's revision holds "in microtubules only" and is contested, and states the 3,000–30,000 count as a burden, "a rate no concrete model accounts for".
3. **"It relies on the classical view of the Readiness Potential as a deterministic buildup."** False: L54 adopts Schurger's accumulator reading and L99 adds that a classical accumulator is causally closed.
4. **"Asserts that a quantum selector is necessary"; "fails to acknowledge" causal closure and energy conservation.** False: L79, L99, L109 and L117 concede classical sufficiency, and L105 says conservation "is therefore part of what the interpretation must argue".
5. **Sources.** Georgiev 2021 (*Symmetry*) concludes the reverse of what Gemini cites it for. Jiang et al. has the wrong year, volume and pages and is off topic. "Gibb et al. (Eds.) (2021)" from OUP cannot be found. Bogler et al., cited in the body, argues against the noise-only reading Gemini uses it for. Only Schurger et al. 2021 and Maoz et al. 2019 hold.
6. **The title.** Gemini calls the page "Motor Control and the Quantum Zeno Framework". The page is "Consciousness and Motor Selection" (Method Notes).

**Claude Opus 5.5: claims excluded.**

1. **The changelog "was last modified 2026-10-15".** This is a stale fetch. A driver fetch at ~04:45Z found entries up to 2026-11-03T01:43:04, including this article's 10-27 refine. It is the fourth instance of the same frozen view (10-20, 10-31, 11-02, 11-03).
2. **Stale satellite snippets.** The `agent-causation` ("same ~300ms timeline", the Sjöberg claim), `retrocausality` ("identical selection architecture"), `consciousness-selecting-neural-patterns` ("~10¹⁰ observations per second") and `conscious-vs-unconscious-processing` ("~1000 per 300ms window") claims are all gone from the live files. The cvup number now reads "~100 Hz" (`grep -c -F "1000"` = 0).
3. **"Stapp 2000 places the locus in the low-frequency EM field."** Stapp introduces it with "Suppose, for definiteness": an illustration.
4. **Koch & Hepp 2006, date metadata, Rizzolatti "presented as settled".** The first is a generic dismissal resting on Tegmark, whom the page already engages. The second is a site-wide template choice. The third was rejected at L64, which is conditional; see X1 for where it survives.
5. **"Supply a labelled guess with error bars" for the Zeno time.** The diagnosis is true and the page already concedes it. The remedy would have the Map inventing physics that its own `timing-gap-problem` page says nobody has computed (C10).

**ChatGPT 5.6 Sol Pro: claims excluded or counted as partial.**

1. **"Do not use Hagan's microtubule calculation as a generic bound."** L115 already scopes it ("in microtubules only"), and ChatGPT's own opening credits that scoping (D3).
2. **"'Acceleration is more common' is too broad."** Kofman & Kurizki (2000) write that acceleration "appears to be much more ubiquitous", as the linked `sign-problem-for-conscious-observation` L45 quotes.
3. **"Update the Libet and volitional-control pages away from 'Schurger showed'."** Both are already hedged (`libet-experiments` L195, `volitional-control` with Braun et al. 2021 and Gavenas, Schurger & Maoz 2025).
4. **Tenet-protective bracketing in general (§5, improvements 33–35).** The leg classed this as a framework-level disagreement already held in the NEEDS-HUMAN methodology entries. Its page-level instances count (C7, X3, X4).
5. **"A 2026 prospective-probe study."** No link survived extraction. Unverified.

## Convergence Table

Line numbers are 0-based `parse_tasks` indices after this synthesis's edits.

| # | Cluster | ChatGPT | Claude | Gemini | Task (line) | Action |
|---|---|---|---|---|---|---|
| C1 | Stapp's Zeno hold credited with outcome selection (L95, L105) | ✓ | ✓ | ✗ misattributed | L4085 P1 | held at P1 |
| C2 | Georgiev reported by one horn only (L115) | ✓ | ✓ | — | L4085 | (same task) |
| C3 | Tegmark 2000 discussed but missing from References | ✓ | ✓ | — | L4085 | (same task) |
| C4 | "Largely arrived" and "artifact of averaging" overstate Schurger (L52, L54) | ✓ | ✓ | ✗ opposite direction | L4098 | P2→P1 |
| C5 | The RP evidence base is dated: no Schurger et al. 2021, no Maoz 2019 | ✓ | ✓ | ✓ | L4098 | (same task) |
| C6 | Libet's ~200 ms W-time reused as the agent's window (L97) | ✓ | ✓ | ✓ (scope) | L4098 | (same task) |
| C7 | "Near-perfect accuracy" falsifier unmeetable; drift-diffusion test non-discriminating (L119) | ✓ | ✓ | — | L4111 | P2→P1 |
| C8 | Zheng & Meister's behavioural figure glossed as a conscious selector (L81, L125) | ✓ | ✓ | — | L4111 | (same task) |
| C9 | Müller & Rabbitt credited with "~300ms" voluntary attention (L68 and 5 satellite lines) | ✓ | ✓ (via changelog) | — | L4123 | P2→P1 |
| C10 | No worked quantitative Zeno model (operative timescales absent) | ✓ | ✓ | ✗ inverts | none | record only |
| X1 | L73 states attention–motor unity without its condition | ✓ | ~ | — | L4111 add-on (a) | none |
| X2 | L89 attaches Map glosses to Desmurget's finding | ~ | ~ | — | L4111 add-on (b) | none |
| X3 | The Occam paragraph's effort residue (L131) | ~ | ✓ | — | L4136 add-on | not raised |
| X4 | The "core argument survives" firewall names no successor (L99, L109) | ~ | ✓ | — | L4085 part (5) + add-on | held |

## Convergent Findings

### C1. Stapp's Zeno hold is credited with outcome selection
- **Flagged by**: chatgpt, claude. Gemini reached the same cross-page tension from the other side, but its vote is not counted.
- **Verification**: clean on both legs. L95 has the agent select "among salient options by stabilising one through attention", and L105 says the observation "shapes which state actualises by selecting among existing possibilities". `concepts/motor-selection` L48 calls the mechanism "Stapp's Process-1 placement, not the *outcome selection* the Map's Bidirectional Interaction tenet adopts", and `concepts/stapp-quantum-mind` L64 leaves the answer to "nature's choice". Gemini's "Born-governed" quotation is motor-selection L48 (0 hits on the article), and its claim that Zeno probing must "violate" Born statistics is its own physics, so it does not count.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Repeatedly posing the same question may stabilize an already occupied “yes” subspace, but it does not by itself allow an agent to choose which one of several motor outcomes actualizes."
  - **Claude Opus 5.5**: "Readers of this article alone would not learn that the mechanism it develops does not deliver the kind of selection its agency section describes."
  - **Gemini 3.1 Pro** (not counted): "The manuscript attempts to firewall itself by claiming that outcomes remain "Born-governed". But this is a mathematical and logical contradiction."
- **Task action**: held at P1 (skill cap): "`topics/motor-control-quantum-zeno` credits Stapp's Zeno mechanism with outcome selection …". The Review file field was made plural (ChatGPT, Claude), a Synthesis line was added, and the Notes got the convergent preamble, the run order and COMBINE ADD-ON (D4, D5).

### C2. Georgiev is reported by one horn only
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L115 says only that a mind "projecting in the basis decoherence has already fixed is redundant with it". The arXiv 1412.4741 abstract, checked on both legs, reports that the Zeno effect "breaks down for timescales greater than the brain decoherence time", proves the von Neumann entropy result, and leaves open "a decoherence-free subspace".
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Georgiev’s criticism is broader: under realistic open-system evolution, the relevant Zeno effect can fail beyond the decoherence timescale"
  - **Claude Opus 5.5**: "That is a no-go claim, not a redundancy claim."
- **Task action**: the same P1, part (2), held.

### C3. Tegmark 2000 is discussed but missing from References
- **Flagged by**: chatgpt, claude
- **Verification**: clean. The article names Tegmark twice in L115, and `Tegmark, M` has 0 hits in its 19 references. Crossref: *Physical Review E* 61(4), 4194–4206.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Despite Tegmark’s calculation being central to the section, the article’s reference list does not include Tegmark 2000."
  - **Claude Opus 5.5**: "Tegmark 2000 is cited in the body but missing from the references."
- **Task action**: the same P1, part (4), held. Both reviewers also proposed a body-to-reference reconciliation check (M2).

### C4. "Largely arrived" and "artifact of averaging" overstate Schurger
- **Flagged by**: chatgpt, claude. Gemini argues the opposite direction (D1).
- **Verification**: clean on both legs. L52 reads "The answer has largely arrived from neuroscience itself", beside the lede's own "rather than settling the matter". L54 reads "reinterprets the readiness potential as an artifact of averaging neural noise". Schurger, Hu, Pak & Roskies (2021) argue that recent advances "call for a reassessment" (PubMed 33931306). ChatGPT misquoted L54 as "rather than a decision process", but the point stands against the live wording.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The phrase that “the answer has largely arrived” is not justified."
  - **Claude Opus 5.5**: "“Artifact of averaging neural noise” slightly overstates Schurger"
- **Task action**: upgraded P2→P1: "`topics/motor-control-quantum-zeno` §The Libet Challenge Weakened overstates Schurger …". Review files (all three), a Synthesis line, the convergent preamble and the run order were added.

### C5. The RP evidence base is dated
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean on all three. On the article, `Hu, Pak` = 0, `2021` = 0 and `Maoz` = 0. Schurger et al. 2021 (*TiCS* 25(7), 558–570) and Maoz et al. 2019 (*eLife* 8, e39787) are Crossref-verified, and these are Gemini's only two weakness sources that hold. ChatGPT's 2025 rewarded-choice study (Pech et al., niaf023) is verified on its leg and shows the RP–volition relation unsettled in both directions.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Materially overconfident and insufficiently current."
  - **Claude Opus 5.5**: "The “Libet Challenge Weakened” section rests on two items: a 2012 model and a 2024 three-page essay."
  - **Gemini 3.1 Pro**: "*Source omitted/contradicted:* Schurger, A., Hu, P. B., Pak, J., & Roskies, A. L. (2021). What Is the Readiness Potential?"
- **Task action**: the same P1, part (1) and the Claude-leg addendum.

### C6. Libet's ~200 ms W-time is reused as the agent's window
- **Flagged by**: chatgpt, claude, gemini (scope only)
- **Verification**: clean. L97 says "The 200ms window of conscious awareness before movement is … the agent operating within a noisy system", after L54 has set the Libet timeline aside. Claude adds Schultze-Kraft et al. 2016 (*PNAS* 113(4)): the point of no return for vetoing sits at about 200 ms. Gemini's version is that the arbitrary-task timeline is generalised to deliberate agency, where Maoz 2019 finds no RP, and that survives against L97.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The article first uses Schurger to reject the Libet timeline as a measure of decision onset, but later treats Libet’s approximately 200 ms W-time as a meaningful interval in which an agent could intervene."
  - **Claude Opus 5.5**: "The article discounts the RP as averaged noise, yet relies on W as a valid timestamp"
  - **Gemini 3.1 Pro**: "The author(s) attempt to map a theory of meaningful conscious agency onto a neural signature that vanishes the moment actual meaning is introduced to the task."
- **Task action**: the same P1, part (4).

### C7. The falsifier cannot be met and the test cannot discriminate
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L119's weakening condition is decoding at "near-perfect accuracy" (`grep -c -F` = 1), which a fully physical brain with thermal noise would also fail; L99 itself calls that noise epistemically unpredictable. The strengthening test compares against "basic drift-diffusion statistics". Classical urgency-gating models, including Thura & Cisek 2014, which the page cites, also deviate from those, and no direction of deviation is stated.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Likewise, “near-perfect neural prediction” is an excessively demanding weakening criterion."
  - **Claude Opus 5.5**: "The “What would weaken it?” condition, “near-perfect accuracy” in decoding which action is selected, cannot be met even by a fully physical brain with thermal and synaptic noise."
- **Task action**: upgraded P2→P1: "`topics/motor-control-quantum-zeno` treats compatibility as location …". The upgrade rests on parts (3) and (5); parts (1) and (4) are ChatGPT's alone, and part (2) is partial (X2).

### C8. The 10-bit figure is glossed as a conscious selector
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L81 reads "roughly 10 bits/second of conscious behavioural throughput (Zheng & Meister 2025)—matches this role", and L125 "matches policy-level selection". Zheng & Meister measure the throughput of behaviour. ChatGPT objects to "matches"; Claude objects to "conscious". Both are wording fixes inside the existing +40.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The claim that 10 bits per second “matches” a policy-level conscious selector therefore has no independent evidential force."
  - **Claude Opus 5.5**: "“Conscious” throughput is the Map’s gloss; the site’s changelog already corrected this elsewhere."
- **Task action**: the same P1, part (3) and the optional net −1 in the Claude-leg addendum.

### C9. Müller & Rabbitt are credited with "~300ms" voluntary attention
- **Flagged by**: chatgpt, claude
- **Verification**: clean, but the votes are correlated. Both reviewers found the defect partly through the Map's own changelog, where two attention passes had noted these lines out of scope without minting a task. The ChatGPT leg checked the PDF. The 300 ms optimum is Müller and Findlay's earlier result, which Müller & Rabbitt summarise, and their own central-cue peak is 400–725 ms (p. 320). L68 still reads "~300ms post-cue deployment for voluntary attention in humans" (`~300ms` = 1). The upgrade rests on the source check, and on two passes having left the defect untasked.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The page’s comparison between voluntary attention at approximately 300 ms and reflexive attention at 100–175 ms is not supported by the cited Müller and Rabbitt paper."
  - **Claude Opus 5.5**: "It is unresolved in the live text."
- **Task action**: upgraded P2→P1: "Müller & Rabbitt (1989) credited with "~300ms" … FIVE FILES". The upgrade also guarantees that this sweep runs before the Libet-calibration satellites P2, which shares `concepts/motor-selection` L50.

### C10. There is no worked quantitative Zeno model
- **Flagged by**: chatgpt, claude. Gemini's version inverts the article (excluded, item 2).
- **Verification**: the diagnosis is true and already public. L115 says "no source the Map has found computes where a brain sits", and L119 says the prediction "stays qualitative" until the P-Q10 coupling model exists. ChatGPT's eight-item list (system, generator, projector, interval, bath correlation time …) and Claude's request for the Zeno time ħ/ΔH ask for physics nobody has computed. The Claude leg rejected the remedy because it would have the Map invent those numbers.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "It confronts the objection discursively but not mathematically."
  - **Claude Opus 5.5**: "Until one order-of-magnitude estimate is supplied, the quantitative section remains a bounding exercise on an unknown, not a test."
- **Task action**: recorded only. Both reviewers credit the page for stating the gap (ChatGPT: "It admits that no neural projector, physical measurement interaction or quantitative coupling has been supplied"; Claude: "The P-Q10 tooltip is an honest public debt marker").

### X1. L73 states attention–motor unity without its condition (partial)
- **Flagged by**: chatgpt (clean at L73); claude (partial: its row was rejected at L64)
- **Verification**: L64 is conditional ("If attention *is* motor planning at some level"). L73's first sentence is conditional too, but its second reads "Consciousness does not need separate interfaces for perceiving and acting—it operates through one unified selection system." L117 concedes that the parallel "does not prove they share a single mechanism". So the Claude leg's rejection holds for L64, and the concern survives at L73. ChatGPT's Rajan point lands on L73 as well: L69 and L71 are hedged, as Claude says, and the leap is in L73.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Elsewhere, however, it treats the attention–action unity as established architecture."
  - **Claude Opus 5.5**: "PMTA is presented as settled; it has been contested in the literature"
- **Task action**: COMBINE ADD-ON (a) on the compatibility P1: make L73 conditional at +0, cite none of ChatGPT's unverified premotor sources, and leave L64 and L68.

### X2. L89 attaches Map glosses to Desmurget's finding (partial)
- **Flagged by**: chatgpt (partly right on its leg); claude (partial: it cited `motor-selection` for the gloss)
- **Verification**: the Desmurget abstract concludes that intention "arise[s] from increased parietal activity", so "originates in parietal cortex" is close to the authors' own claim. The overreach is the Map's next step ("The interface between consciousness and movement operates where intention lives"). Claude's point that "posterior 'hot zone'" is the Map's gloss applies to L89 as much as to motor-selection: the same clause is in L89 (`grep -c -F` = 1).
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "“Conscious motor intention originates in parietal cortex” is nevertheless too strong."
  - **Claude Opus 5.5**: "The “posterior hot zone” gloss is the Map’s own, not Desmurget’s."
- **Task action**: COMBINE ADD-ON (b) on the compatibility P1. When part (2) attributes the conclusion to Desmurget, the hot-zone clause stays on the Map's side.

### X3. The Occam paragraph's effort residue (partial)
- **Flagged by**: claude (clean); chatgpt (partial: its leg classed §5 as framework-level)
- **Verification**: L107 concedes that "computational accounts of effort (resource allocation, opportunity cost) can explain similar patterns", and L131 then says what neural determinism "leaves unexplained is why effort phenomenology tracks difficulty". Claude's inconsistency is verified. ChatGPT pushes further: even "why it is felt" has functional rivals.
- **Quotes**:
  - **Claude Opus 5.5**: "Only one of these can stand."
  - **ChatGPT 5.6 Sol Pro**: "appealing to the phenomenology of effort does not by itself fill a mechanistic gap."
- **Task action**: not raised, because only one leg verified it. A zero-word COMBINE ADD-ON on the Bourget P2's part (2) says to present the "felt at all" residue as the framework boundary rather than as a visible failure of the neural account.

### X4. The firewall names no successor (partial)
- **Flagged by**: claude (clean); chatgpt (partial: §5 bullet, which its leg classed as framework-level)
- **Verification**: L109 says the case "would survive, needing a different mechanism to fill the same role", and L99 calls the Zeno proposal "(or a successor mechanism that supplies real indeterminacy)" the source of the opening. Neither names a successor. The register ranks post-decoherence selection above Stapp's Zeno mechanism (P-Q1, P-Q4).
- **Quotes**:
  - **Claude Opus 5.5**: "In practice the firewall is an appeal to future physics that shields the conclusion from the mechanism’s failure."
  - **ChatGPT 5.6 Sol Pro**: "When Stapp’s model is physically unsuccessful, interactionist dualism is said to survive because Stapp is optional."
- **Task action**: already part (5) of the P1. See D5 for how the two reviewers want the successor handled.

### Methodology convergences (record only)

- **M1. Corrections do not propagate to satellites.** ChatGPT improvement 29 ("Build dependency-aware correction checks") and Claude methodology item 3 ("Semantic, not string, propagation sweeps"). Both have verified live instances: ChatGPT's in the M&R lines and the ~1 kHz lines, Claude's in seven satellite lines. Both legs added a 2026-11-03 addendum to the NEEDS-HUMAN propagation entry.
- **M2. Claim provenance and reference reconciliation.** ChatGPT items 28 and 30 (claim ledger, primary-source-first) and Claude items 1–2 (quote provenance, body-to-reference check). The verified instances are the Schurger quotation the 2026-07-26 deep review false-ratified, and the missing Tegmark. The Claude leg recorded an addendum on the 2026-07-30 verification-ledger entry.
- **M3. Literature currency and objection coverage.** ChatGPT item 32 (literature-search cutoffs and a structured contrary search) and Claude items 4 and 7 (a named-critic checklist; a literature-currency trigger). The weekly `literature-drift-review` already covers the trigger.
- **M4. Mechanism falsifiers and firewalls.** ChatGPT item 34 ("Require quantitative falsifiers for mechanism articles") and Claude item 5 ("“Core claim survives” firewalls must name the successor mechanism and its register status, or be dropped"). The page-level instances are C7 and X4. ChatGPT's item 35 (externalist review, downgradeable tenets) remains with the NEEDS-HUMAN "End bedrock immunity" entry.

## Rejected Convergences

### R1. Kiefer & Joos cited for a stronger claim than it makes
- ChatGPT §4 item 7 ("a broad treatment of decoherence is used to support a categorical claim about when repeated observation can add anything") and Claude Q2 item 6 ("it states no explicit condition that repeated observation “adds something only while it arrives before the environment has resolved the same alternatives.”").
- **Rejected on both legs.** The L115 condition joins two Kiefer & Joos statements verified in arXiv quant-ph/9803052 and quoted on `concepts/zeno-dynamics-on-a-decohered-mixture` L51/L53. Two reviewers who stop at the abstract make the same miss, which is correlated error.

### R2. Classical basal-ganglia selection makes the selector redundant
- Gemini weakness 4, and in substance ChatGPT §2 ("Neural competition identifies **what must be explained**, not **an unoccupied causal role**").
- **Gemini's vote is void.** Its quotations are motor-selection's, its claim that the article "asserts that a quantum selector is necessary" is false against L79, L99, L109 and L117, and its source is off topic. ChatGPT's live instance (L38 "leaves room for a non-physical selector", L95 "positions the agent") stands alone and sits in compatibility part (1) and P1 part (1).

### R3. Satellites keep the stale ~1,000-event Stapp rate
- ChatGPT §6 item 3 ("Other linked material retained the old approximately 1,000-event interpretation after the canonical Zeno page was corrected to Stapp’s approximately 100 Hz example") and Claude Q5 (`conscious-vs-unconscious-processing`: "~1000 per 300ms window").
- **Claude's instance is already fixed.** The 2026-11-01 sweep replaced it with "~100 Hz", and only the "The timing works" conclusion survives, which the Zeno-timing satellites P2 owns. ChatGPT's instances, `topics/quantum-neural-timing-constraints` L143 and `concepts/decoherence` L131, are live and belong to the 2026-11-01 P3 (line 3704), which was minted by an internal refine-draft pass. No second outer reviewer names either file, so **the P3 is not upgraded.** A zero-word COMBINE ADD-ON records ChatGPT's independent confirmation, plus one seam: the sentence before decoherence's ~1 kHz line ("This mechanism requires only that individual observation events occur faster than decoherence destroys the superposition") repeats the "require only" framing that the satellites P2 recasts at `interface-friction` L60, and that task is told not to touch decoherence.

## Singleton Findings

Not upgraded; left at their original priority. Listed for the record.

- **ChatGPT 5.6 Sol Pro**: the L46 materialist strawman → Libet P1 part (3). L38 lede compatibility-as-location → compatibility P1 part (1). L83 three-layer structure unlabelled → compatibility P1 part (4). L95 "positions the agent" against L99 → P1 part (1). Stapp's own ~100 Hz rate never compared with the 3,000–30,000 burden → P1 part (3). The ~1 kHz satellite lines → the 11-01 P3 (R3).
- **Claude Opus 5.5**: the Schurger quotation is from the 2018 *eNeuro* paper, not the 2012 PNAS paper (and the 2026-07-26 deep review false-ratified it) → Libet P1 part (2) correction. Bourget's weakness-of-will objection, the Cai author list and the truncated titles → P2 "never engages Bourget's (2004) weakness-of-will objection" (L4136). Four Zeno-timing satellites → P2 L4146. Four Libet/RP satellites, including motor-selection's "Hameroff (2014)" → P2 L4157. Fried 2011, Bredikhin 2023, Gavenas 2024 and Schultze-Kraft 2016 → the Libet P1's Claude-leg addendum.
- **Gemini 3.1 Pro**: none that survived. Its Bogler citation, read correctly, became an optional counterweight in the Libet P1 (GEMINI-LEG ADDENDUM).

## Divergences

- **D1. ChatGPT and Claude vs Gemini, on the RP's direction.** ChatGPT and Claude say "artifact of averaging neural noise" already overstates Schurger. Gemini wants the page to call the RP a "statistical artifact" whose deterministic reading has been "decisively overthrown". Gemini's premise (that the article holds the deterministic view) is false, and Bogler, Grujičić & Haynes 2023, which Gemini cites, finds that "the deterministic component of the model is quantitatively the dominant input". Gemini's direction is rejected.
- **D2. ChatGPT and Claude vs Gemini, on decoherence.** Both credit the article for stating the objection candidly ("The quantum-Zeno section is now comparatively candid"; "honestly confronts Tegmark and Hagan"). Gemini says it "completely ignores" decoherence. Gemini inverted L115.
- **D3. ChatGPT vs Claude, on Hagan's scope.** ChatGPT asks the page to stop using Hagan "as a generic bound". Claude finds "the article’s restriction of it to microtubules" correct. Claude stands, and the ChatGPT leg rejected its own reviewer here.
- **D4. ChatGPT vs Claude, on "twelve orders".** ChatGPT calls "femtoseconds—a twelve-order gap from milliseconds" arithmetically unstable (10⁻¹³ to 10⁻³ s is ten orders). Claude calls it "right at the slow end (10⁻¹³ against 10⁻¹ s)". Both are partly right: the phrase depends on reading "millisecond timescales" as Tegmark's 0.001–0.1 s range. The P1's part (4) wording, which anchors the gap to a ~300 ms decision window, satisfies both. The P1 add-on says to keep it.
- **D5. Claude vs ChatGPT, on naming the successor.** Claude wants L109 to name post-decoherence selection, the register's preferred candidate. ChatGPT warns that post-decoherence selection "changes the theory rather than repairing Zeno stabilization" and must not be "silently substituted when decoherence defeats Zeno control". The article has 0 hits for "post-decoherence", so ChatGPT's "uses it more like a protective fallback" describes the unnamed successor. The P1 add-on reconciles them: name it as a register-ranked rival that does not inherit the Zeno probing story, in `motor-selection` L176's terms, not as a drop-in.
- **D6. ChatGPT vs Claude, on `concepts/motor-selection`.** ChatGPT holds it up as "more cautious about causal gaps". Claude says its Libet section overstates. They are about different sections (the L48 Process-1 caveat vs L50, L137 and L143), so the disagreement dissolves. The Libet satellites P2 leaves L48 alone.
- **D7. ChatGPT vs Claude, on Desmurget.** ChatGPT faults L89. Claude praises the Dualism paragraph (L123) for refusing to read the dissociation as evidence of irreducibility. Different lines, so this dissolves too. Compatibility part (2) already says to keep L89 consistent with L123.

## Length Budget and Run Order

Five open tasks edit the article, which stands at 3,544 of 4,000 (gate `>=`, ceiling 3,999, 455 usable). Each task's Notes now opens with the same RUN ORDER AND SHARED BUDGET statement. The queue sorts by priority and then line, which already yields this order.

| Order | Task | Line | Budget | Running total (committed / with optionals) |
|---|---|---|---|---|
| 1 | P1 "credits Stapp's Zeno mechanism with outcome selection" | 4085 | +105 | 3,649 / 3,649 |
| 2 | P1 "§The Libet Challenge Weakened overstates Schurger" | 4098 | +70 (optional to +95) | 3,719 / 3,744 |
| 3 | P1 "treats compatibility as location" | 4111 | +40 | 3,759 / 3,784 |
| 4 | P1 "Müller & Rabbitt (1989) credited with ~300ms" (this page only) | 4123 | +10 | 3,769 / 3,794 |
| 5 | P2 "never engages Bourget's (2004) weakness-of-will objection" | 4136 | +80 (optional titles +18) | 3,849 / 3,892 |

This leaves 150 spare words if only committed budgets are used, or 107 with every optional item. If an earlier task overruns, later tasks drop their optional items first (Bourget's titles, then the Libet addendum). The other tasks on related files run after these:

- 6. P2 Zeno-timing satellites (L4146). It edits four other files and reads the article's L115 live, after the P1 has rewritten it.
- 7. P2 Libet-calibration satellites (L4157). It runs after the M&R sweep, which edits `motor-selection` L50 net-zero first.
- The 11-01 P3 (L3704) stays at P3 and carries the decoherence L131 seam note.

## Method Notes

- **Rule applied.** A cluster was upgraded only if its finding was verified on at least two legs against the live text. That excluded every Gemini vote except C5 and C6. It also held back X1–X4, where one leg's processing had rejected the point or classed it as framework-level. The P3 failed because only one reviewer names its files.
- **Gemini's title is a symptom, not a vote.** "Motor Control and the Quantum Zeno Framework" was the article's title until `4d8fc67708` (2026-04-05). It survives as the pipe label at `topics/volitional-control` L108, which is item (d) of the Libet satellites P2, and in older review titles. An outside reader adopting the stale label is evidence that the label misleads.
- **C9's two votes are correlated.** Both reviewers read the Map's own out-of-scope notes. Convergence here confirms that the defect has been visible and untasked for two passes, rather than adding independent evidence that it exists; the PDF check supplies that.
- **The Claude leg caught a false ratification.** The 2026-07-26 deep review had marked the L54 Schurger quotation "Verbatim confirmed at publisher". The sentence is in Schurger's 2018 *eNeuro* paper and absent from the 2012 PNAS full text. The ChatGPT leg's original brief ("Keep the verified Schurger quotation unchanged") had carried the false ratification forward, and the Claude leg corrected it inside the Libet task's Notes.
- **Todo edits.** Three headings were changed P2→P1 in place. Four `Review file` lines became `Review files`, and four `Synthesis` lines were inserted above `Notes`, so the blocks after line 4085 moved down by one to four lines (Libet 4097→4098, compatibility 4109→4111, M&R 4120→4123, Bourget 4132→4136, Zeno satellites 4142→4146, Libet satellites 4153→4157). Notes were edited in place on the four convergent tasks, the Bourget P2 and the 11-01 P3. `parse_tasks` still returns 312 active tasks. No article was edited.
