---
title: "Outer Review Synthesis - 2026-09-16"
created: 2026-09-16
modified: 2026-09-16
human_modified: null
ai_modified: 2026-09-16T06:20:32+00:00
draft: false
description: "Cross-review synthesis of the three 2026-09-16 audits of topics/lucid-dreaming-and-dualist-rendering. Thirteen convergent clusters, seven at 3/3; three tasks upgraded P2 to P1, one leg added to the target P1; Gemini's retraction charge and two of its five sources were false."
topics: []
concepts: []
related_articles:
  - "[[project]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-16
last_curated: null
synthesizes:
  - reviews/outer-review-2026-09-16-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-09-16-claude-opus-5.md
  - reviews/outer-review-2026-09-16-gemini-2-5-pro.md
synthesis_coverage: "3/3"
---

**Date**: 2026-09-16
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Subject**: Single-article audit of `topics/lucid-dreaming-and-dualist-rendering` (`subject_type: recent`, `subject_source: fallback:recent-aged`; last substantively modified 2026-09-09, 3,328 body words). ChatGPT commissioned it at 04:07; Claude (04:20) and Gemini (04:38) reused the subject through the reuse anchor, so all three read the same live text. Gemini was briefed as a hostile journal referee; the other two as external referees checking every citation against the primary lucid-dreaming literature.
**Coverage**: 3 of 3 commissioned reviewers contributed. No abandonments. Every leg carries a `## Verification Notes` section from `/outer-review`, and those verdicts were applied *before* clustering: a claim two reviewers share counts as convergence only if neither half was disputed on disk. Gemini's five mandated sources were checked at Crossref by its collection pass — two exact, one real but off-topic, one a fabricated author/year on a 2013 paper, one a title/author/journal conflation across two papers — and its retraction charge against a review the article cites is false; those parts are excluded from every cluster below.

## TL;DR

The cycle converged on one article harder than any single-article cycle so far: **thirteen convergent clusters, seven of them 3/3**. The dominant finding is that the article's evidential frame — four "capability signatures" plus a degradation asymmetry presented as pressure on physicalism — is compatible-only by the article's own hedges, and that its strongest physicalist rivals (precision weighting and generative-model release for the asymmetry; the global workspace reading of Konkoly; a lucid-dream-specific predictive-processing model) are absent from the text. Beneath the frame sit verified citation failures: Baird 2018's "reshapes neural structure" is contradicted by the paper (2/3, full text), Konkoly 2026 is deployed for a causal claim its own cueing-null and lucidity-null results undercut (3/3), and Hobson–Hong–Friston 2014 is cited in the reversed argumentative direction (2/3). Two quotations absent from their cited sources are a Claude singleton that ChatGPT's descriptive-level pass got wrong. Counts: **13 convergent clusters** (3 tasks upgraded P2 → P1, 3 already at P1 recorded, 1 NEEDS-HUMAN entry annotated, 1 leg added to the target P1, 1 convergence on a declined remedy, 1 carried without a task), **16 singletons** (7 carried as legs of the target P1, 1 as an item of an upgraded task, the rest recorded or refuted), **5 divergences**, **0 task-level deduplications** — the per-review passes had already folded sibling findings into one task per file at collection.

## Convergent Findings

### 1. Baird 2018 "practice reshapes neural structure" is contradicted by the paper

- **Flagged by**: claude, chatgpt (2/3)
- **Verification**: Clean, at full text by both passes (PMC6290891): "In contrast, no significant differences in brain structure were observed"; n = 14 vs 14, cross-sectional; the finding is increased resting-state *functional* connectivity between left aPFC and bilateral angular gyrus. The article's L116 fails on both legs (no structural result; no design that licenses temporal precedence). Gemini cited Baird 2018 correctly as "frontopolar functional connectivity" and did not notice the article's structural claim — a miss, not a dissent. ChatGPT's addition that the error "has propagated to neighbouring articles" was verified wider than stated: seven loci (3 live articles, 2 research notes, 2 served archive pages).
- **Quotes**:
  - **Claude Opus 5** (§2.5): "Baird, Castelnovo, Gosseries & Tononi 2018 found the opposite: … '**In contrast, no significant differences in brain structure were observed.**' … The article's inference fails on both legs: there is no structural change, and a cross-sectional design licenses no claim about practice causing anything or about temporal precedence."
  - **ChatGPT 5.6 Pro** (§Correct source, materially misrepresented finding): "This is the clearest citation failure. Functional connectivity becomes 'neural structure'; cross-sectional association becomes practice-induced plasticity; and no temporal data become a claim of capability preceding accommodation."
- **Task action**: **Recorded — two tasks already P1, no upgrade available.** Leg (d) of the target P1 (the article's own L116) and the P1 sweep "Baird 2018 'larger aPFC volume / practice reshapes structure' is a hard factual error propagated to 3 live articles, 2 research notes and 2 archive pages" (seven loci, ChatGPT's extension). `Review files:` lines updated on both.

### 2. The Degradation Asymmetry omits precision weighting and reads Charles Bonnet syndrome as compensation rather than generative release

- **Flagged by**: gemini, claude, chatgpt (3/3)
- **Verification**: Clean on the gap (`predictive`, `precision`, `active inference`, `Bayesian` all 0 hits in the article). Claude's mechanism is verbatim in the article's own cited source (Hobson, Hong & Friston 2014, PMC4191565): "This model is continually updated and entrained by sensory prediction errors in wakefulness to ensure veridical perception, but not in dreaming." ChatGPT's Ffytche 1998 point is verified at the abstract (CBS hallucinations "reflect the functional specializations of the region" — nothing about compensation). Gemini's two citations for this cluster were excluded: Wiese 2024 is real but about digital simulation, not precision weighting; "Blom, R. E., et al. (2024)" does not exist — the paper with that title is Reichert, Seriès & Storkey 2013, *PLoS Comput. Biol.* 9(7): e1003134. The convergence is scored on the mechanism, which all three describe identically.
- **Quotes**:
  - **Gemini 2.5 Pro** (§The Failure to Engage with Bayesian Brain Frameworks): "Because the brain attempts to minimize variational free energy against a degraded but highly precision-weighted sensory stream, the resulting conscious percept is blurry or distorted. The brain does not maliciously 'withhold' a rendering capability, nor does a dualist filter simply narrow."
  - **Claude Opus 5** (§2.1): "A degraded-but-present retinal signal still entrains the waking model; in dreaming, input is gated and the model runs free. The asymmetry is precisely what the production account predicts. The article presents as an anomaly a fact its own citation explains."
  - **ChatGPT 5.6 Pro** (Finding 11): "Charles Bonnet syndrome shows internally generated visual contents correlated with content-specific ventral extrastriate activity. It does not show the visual system generating reliable *compensatory* imagery that restores the lost scene."
- **Task action**: **Recorded — already P1, leg (a) of the target P1** (Reichert 2013 install, Hobson entrainment sentence, "compensatory" removed, L124 "explanatory economy" concession retained). See Divergence 3 for the delete-versus-reframe split.

### 3. Konkoly 2026 and the two-way-communication studies are over-read as Tenet 3 "laboratory verification"

- **Flagged by**: gemini, claude, chatgpt (3/3)
- **Verification**: Clean. Konkoly 2026 (PMC12875123) at full text: "no significant main effect of cueing or interactions (ps > .6)"; the 20→40% figure is "a post-hoc analysis" in 12 targeted dreamers; Table 1 lucid incorporation 1/9 solved (11%) vs non-lucid 6/13 (46%); the authors' own limitation that dream benefits "cannot be disentangled from processing occurring in the interim". The article's 42%/17% is accurate. Claude's quoted strings "even without lucidity" and "post-waking cognition" are paraphrases (0 hits) but the substance holds. Gemini's GNW reading rests on Mashour, Roelfsema, Changeux & Dehaene 2020, *Neuron* 105(5): 776–798 (Crossref-exact); `global workspace` is 0 hits in the article. L138 "provide laboratory verification" is verbatim on disk.
- **Quotes**:
  - **Gemini 2.5 Pro** (§The GNW Explanation of Conscious Broadcasting): "GNW is an explicitly anti-epiphenomenal framework; the non-linear broadcasting of information across the workspace *is* the physical causal mechanism that enables flexible, cross-modular problem solving, delayed response, and metacognitive report."
  - **Claude Opus 5** (§2.6): "Since the article deploys the study for **Bidirectional Interaction** (conscious/volitional control), the study's own finding that lucidity and control did *not* drive the effect undercuts the use."
  - **ChatGPT 5.6 Pro** (Finding 3): "To challenge epiphenomenalism, one would need evidence that variation in phenomenal content itself changes the outcome while relevant physical processing is held fixed. This study does not approximate that intervention."
- **Task action**: **Recorded — already P1, legs (b) and (e) of the target P1** (Mashour 2020 install with the direct-refutation remit; L138 rewording to P-CS4's register; the three Konkoly caveats). The ChatGPT singleton on `concepts/mind-brain-separation` L90 ("the case for mental causation rests on the laboratory two-way communication studies") is the same over-read in a neighbour and rides as item (2) of the upgraded filter-theory task (cluster 10).

### 4. The strongest predictive-processing rival is unengaged — three reviewers, three different papers

- **Flagged by**: gemini, claude, chatgpt (3/3 at the article level)
- **Verification**: Clean at the article level; **Gemini's site-level form is false and excluded** (`predictive processing|predictive coding` in 93 live files; dedicated pages `concepts/predictive-processing`, `topics/predictive-processing-and-dualism`) — the recurring article-level-real / site-level-false split. Laukkonen, Friston & Chandaria 2025 is 0 hits in the article and is engaged at `topics/predictive-processing-and-dualism` L82 as "the strongest physicalist alternative the Map currently faces". Simor, Bogdány & Peigneux 2022 (*PNAS*, PMID 36279459) is 0 hits corpus-wide; its abstract matches ChatGPT's steelman table.
- **Quotes**:
  - **Claude Opus 5** (Part 1): "The standing blocking gate — Laukkonen, Friston & Chandaria 2025 … is neither cited nor engaged, though the article squarely triggers it. The paper offers a fully physicalist mechanism for exactly the article's flagship signatures."
  - **ChatGPT 5.6 Pro** (Finding 10): "The article mentions disinhibition, metabolic cost and avoidance of waking hallucination. These are not the strongest contemporary physicalist responses. Simor, Bogdány and Peigneux offer a lucid-dream-specific framework…"
  - **Gemini 2.5 Pro** (§The Rendering Dilemma and the Predictive Processing Blind Spot): "The manuscript's omission of this framework is a staggering dialectical failure, as PP provides an exact, mathematically formalized explanation for the very asymmetry the author claims is a mystery."
- **Task action**: **Upgraded P2 → P1**: "`concepts/predictive-processing` L155 engages no lucid-dream-specific predictive-processing model — install Simor, Bogdány & Peigneux 2022 … and link reciprocally" (refine-draft) — the corpus-side half of the cluster. The target-side half is legs (h) (Laukkonen paragraph, reply imported by piped link) and (o) (Simor clause) of the target P1, already P1.

### 5. Cited physicalist authors are enlisted as dualist witnesses; Hobson 2014 is cited in the reversed argumentative direction

- **Flagged by**: claude, chatgpt (2/3)
- **Verification**: Clean on Hobson: "evidence that grounds consciousness in biophysical computations" is verbatim in the paper, and L136 "describe exactly what dualism predicts" banks the generative-model observation as confirmation. **Claude's blanket "FAIL" for Hobson, Metzinger and Revonsuo is overstated** — L48 already labels the trio "Leading physicalist dream researchers" and says the Map "draws a different conclusion"; the verified residue is that Baird, Tononi and Friston carry no such label. ChatGPT's Revonsuo point (threat simulation is "expressly evolutionary", so "adaptive pressure is minimal" confuses immediate output with evolutionary value) was judged fair in sense and not separately minted.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (Finding 4): "The source accepts the first and rejects or seeks to dissolve the need for the second. It is evidence for the strength of the rival model, not a reluctant step toward the Map's model."
  - **Claude Opus 5** (§2.7, row 5): "**FAIL (flagship co-optation)** — authors 'ground consciousness in biophysical computations'; the article's chief rival, enlisted as its support."
- **Task action**: **Recorded — already P1, legs (i) (one co-optation clause extending the L48 label to Baird, Tononi and Friston) and (n) (L136 compatibility wording) of the target P1.** Feeds cluster 6's cited-author-stance leg.

### 6. Internal citation review certifies that a source exists, not what it reports or which way it argues — and an exemption let this article stop being audited

- **Flagged by**: claude, chatgpt (2/3)
- **Verification**: Clean as descriptions of the failure. The article passed deep reviews on 2026-06-01, 06-21 and 07-26 — the last an explicit quote-and-citation-fidelity pass — with the Baird error intact and two absent quotations certified "real-correct" / "canonical" without a grep. ChatGPT's §5 firewall wording is verbatim in two deep-review files: "bedrock framework-boundary disagreements, not fixable defects — do not re-flag as critical", listing "the physicalist-concession framing". The two reviewers name different mechanisms for the same outcome (ChatGPT: the stability-note exemption; Claude: convergence damping on a "stable" file), and one defect: the review asks whether a citation exists, not what it found.
- **Quotes**:
  - **Claude Opus 5** (Part 5 item 2): "The citation ledger verifies that a paper exists, not what it found. Add a mandatory 'does this paper report this result/direction/null?' leg to deep-review."
  - **ChatGPT 5.6 Pro** (§Methodological evidence of a tenet firewall): "A claim does not cease to be evidentially assessable because it follows from a tenet. … The present review process appears better at checking whether a statistic or quotation exists than at checking whether the source plays the argumentative role assigned to it."
- **Task action**: **Upgraded P2 → P1**: "`deep-review` citation-fidelity lens certifies that a cited paper exists, not what it found — add a result-direction / null-result leg and a cited-author-stance (co-optation) leg" (refine-draft on the skill file; the ChatGPT pass had already added a third leg narrowing stability-note exemptions to framework commitments). Claude's gate-paper literature-drift trigger (Part 5 item 5) is policy and sits in the NEEDS-HUMAN entry.

### 7. The title and frame outrun what the body concedes

- **Flagged by**: claude, chatgpt, gemini (3/3)
- **Verification**: Clean. The description line was already recalibrated to compatible-not-forced on 2026-09-09 (commit 0644dcdf1d) and P-CS4 grades the reading the same way; the H1/title is the residue. ChatGPT's quoted hedge strings "not forced" and "arguably cleaner" are reconstructions (0 hits), but its hedge-and-bank pattern stands on two verbatim strings, L106 "structurally simpler" and L136 "exactly what dualism predicts". Gemini's version is the same charge in hostile register and carries no specific locus.
- **Quotes**:
  - **Claude Opus 5** (Part 1): "An article whose central evidential claim is falsified by its own hedges cannot be retained at topic strength; it must be relabelled and demoted to a coherence-only exposition."
  - **ChatGPT 5.6 Pro** (§The "hedge-and-bank" pattern): "The difficulty is that uncertainty is conceded locally and then the desired conclusion is banked globally. … This creates the appearance of calibration while leaving the argumentative architecture nearly unchanged."
  - **Gemini 2.5 Pro** (§Introduction): "The text consistently erects straw-man representations of physicalist theories, brackets its own dualist commitments as axiomatic rather than securing them through argumentation."
- **Task action**: **Recorded — NEEDS-HUMAN 2026-09-16 (retitle / demote-to-coherence-only) annotated with the 3/3 convergence; status unchanged (no tier to upgrade).** The body-wording residue is leg (n) of the target P1. See Divergence 4 for the three verdict severities.

### 8. The Minimal Quantum Interaction paragraph carries no lucid-dream evidential content

- **Flagged by**: claude, chatgpt (2/3)
- **Verification**: Both are accurate descriptions of the paragraph. **Both remedies were declined at collection** for the same reason: the Relation to Site Perspective section is convention-mandated, the paragraph opens "The Map speculates", and neither reviewer disputes that imperfect dream control has a mundane explanation the article itself gives. ChatGPT's Many-Worlds point is the same shape and was declined alongside.
- **Quotes**:
  - **Claude Opus 5** (§2.3): "Pure tenet leakage — imperfect dream control already has a mundane explanation the article gives two sections earlier … The quantum gloss adds zero evidential content."
  - **ChatGPT 5.6 Pro** (§Minimal quantum interaction is tenet-protective speculation): "Unless the Map specifies what distribution of success, temporal profile or neural signature would differ under quantum selection, this is accommodation rather than explanation."
- **Task action**: **Recorded only — convergence on a declined remedy.** Noted in the NEEDS-HUMAN entry so the operator sees that two reviewers independently reached a remedy the pipeline declines by convention. No article task.

### 9. The blindsight "double dissociation" is contested on the blindsight side, and L112 is the one unhedged sentence

- **Flagged by**: gemini, claude, chatgpt (3/3)
- **Verification**: Clean on the substance. Derrien, Garric, Sergent & Chokron 2022 (*Neurosci. Conscious.* niab043) is real and correctly described by Gemini. **Gemini's "clinical myth" / "anchors" framing is overstated**: L110 already hedges ("*appears* to show", "if it holds up") and `concepts/blindsight` §2 carries Phillips 2021's degraded-conscious-vision reading. **ChatGPT's quoted "perceptual organisation fails in blindsight" is 0 hits** in the target and in `concepts/capability-division-in-vision`. What converges is the narrow point: the contrast is external-input processing with deficient report versus endogenous processing with report, not processing-without-consciousness versus consciousness-without-processing.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (Finding 8): "It is not: neural processing without consciousness; consciousness without neural processing."
  - **Gemini 2.5 Pro** (§The Mischaracterization of Blindsight): "If blindsight involves qualitatively degraded conscious experience rather than true unconscious processing, the manuscript's 'Capability Division Problem' loses its primary empirical anchor."
  - **Claude Opus 5** (Part 3): "**Phenomenal completeness / blindsight double dissociation: FLAG AS PERPETUALLY CONTESTED.**"
- **Task action**: **Recorded — already P1, leg (c) of the target P1 plus the ChatGPT refinement** (soften L112 "generated entirely from mind-side resources"; piped `[[blindsight|degraded-vision reading]]` clause; state the contrast accurately). The vision article's L108 label ("with the same dorsal/ventral division shaping dream imagery") is an overstatement recorded for that file's next review; no task this cycle.

### 10. The "Four Capability Signatures" are counted as independent evidence against `concepts/filter-theory`'s own common-cause discipline

- **Flagged by**: claude, chatgpt (2/3)
- **Verification**: Clean. `concepts/filter-theory` L198 carries the note ("should not be counted as seven independent confirmations") and its seven-case list omits dreams, which L121 introduces. The target counts intention-responsiveness, vividness, completeness and metacognitive sovereignty as four signatures of one regime (internally dominated processing during REM).
- **Quotes**:
  - **Claude Opus 5** (§2.1): "The lucid-dreaming article stacks its signatures ('Four Capability Signatures') without ever performing that deflation."
  - **ChatGPT 5.6 Pro** (§6 *Filter Theory*): "The target article currently violates that discipline by counting intention-responsiveness, vividness, phenomenal integration, metacognition, sensory degradation and cue incorporation as multiple 'signatures,' although most arise from the same fact: internally dominated conscious processing during REM."
- **Task action**: **Upgraded P2 → P1**: "`concepts/filter-theory` L198 common-cause note omits lucid dreaming from its seven-case list, and `concepts/mind-brain-separation` L90…" (refine-draft). The upgrade is earned by item (1); item (2) is a ChatGPT singleton in the same pass. Claude's remedy points the other way — make the target inherit the deflation — and that inheriting sentence is the target P1's closing-sentence leg.

### 11. The vividness surplus (Bilzer & Monzel 2025) is over-read

- **Flagged by**: claude, chatgpt (2/3)
- **Verification**: Clean. Bilzer & Monzel (*Vision* 9(2): 37, Crossref abstract): n = 226; dream imagery versus *voluntary mental imagery*, not waking perception; questionnaire, no neural measures; selective modality profile. The article's L102 second sentence reports this correctly; its first sentence ("more emotionally vivid and perceptually immersive than waking experience, despite operating with reduced neural resources") extrapolates and imports the resource premise Baird 2022 contradicts (a ChatGPT singleton, below).
- **Quotes**:
  - **Claude Opus 5** (§2.1): "Disinhibition explains it; the article concedes disinhibition is 'neurologically plausible,' then rejects it as 'phenomenologically unsatisfying' — an aesthetic preference, not a discriminating test."
  - **ChatGPT 5.6 Pro** (Finding 6): "Their result supports a difference between two forms of offline imagery. It does not establish that a sleeping brain produces richer output with fewer resources, nor that visual/emotional channels are supplied by an independent mind."
- **Task action**: **Recorded — already P1, legs (l) and (m) of the target P1.**

### 12. The neural-correlate claims are stated with more confidence than the literature bears

- **Flagged by**: chatgpt, claude, gemini (3/3)
- **Verification**: Clean on the ChatGPT half (n's exact: Voss 2009 six subjects, frontal 40 Hz artefact-corrected by Baird 2022's Bayesian null; Dresler 2012 four participants, one analysable; Demirel 2025 "sensor-level differences … were minimal"). Claude's Dresler n's were not re-fetched (advisory). **Gemini's version is entangled with a false retraction charge** (see Divergence 2) and was marked "not actionable" at collection because the article never cites gamma, 40 Hz, Voss or tACS; what survives from Gemini is the fragility point itself. L46 "the prefrontal cortex partially reactivates, and neurochemistry is fundamentally altered" is an uncited lead gloss — no collection pass minted a leg for it.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (Finding 14): "The article should not present 'the prefrontal cortex partially reactivates' as a settled unitary finding. It should distinguish state activation, trait connectivity and scalp-EEG artefacts."
  - **Claude Opus 5** (§2.7): "**Dresler et al. 2012** (*Sleep* 35(7):1017-1020) is effectively a single-subject case study (four lucid dreamers enrolled; usable lucid-REM fMRI from **one** subject, two epochs)."
  - **Gemini 2.5 Pro** (§The Instability of Lucid Dreaming Neurobiology): "The manuscript treats exploratory neuroimaging of a notoriously elusive, unstable state as established physical law."
- **Task action**: **Leg (p) added to the target P1 by this synthesis** (L46 reworded at net ≈ 0 words, leaning on the Baird 2022 reference leg (l) already installs; Gemini's retraction language fenced out). Budget unchanged.

### 13. Foundational primary literature is missing from the reference list

- **Flagged by**: claude, chatgpt (2/3)
- **Verification**: Clean — the article cites neither LaBerge et al. 1981 nor Dresler 2011/2012 (ChatGPT lists nine missing papers; Claude names LaBerge and Dresler as "citations that the argument requires"). Both collection passes treated this as advisory.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (§Major missing primary literature): "This is not simply a currency problem. Omitting these papers systematically makes the neural account appear less empirically specified than it is."
  - **Claude Opus 5** (§2.7): "The article's core 'brain provides architecture / consciousness provides content' claim leans on neuroimaging it never cites."
- **Task action**: **Recorded — carried without a task.** The target P1 already adds six references (Reichert, Mashour, Laukkonen, Koroma, Baird 2022, Simor) inside a ≤ +480-word budget against 671 words of headroom to the hard ceiling; a LaBerge/Dresler/Siclari/Demirel install has nowhere to land until the file is condensed. The next deep review of the file should carry this list.

## Singleton Findings

Flagged by one reviewer only. Not upgraded. Verification verdicts are carried so a later cycle does not rediscover a refuted claim and score it as fresh.

**ChatGPT 5.6 Pro** (12 claims verified at abstract or full text; 3 unverified; 6 disputed or lower-value):

- **"The sensory channel closes" / "without any corresponding sensory transduction" is false as stated** (Finding 2) → leg (j) of the target P1. Verified: Koroma 2020 "flexible amplification and suppression of sensory information during REM sleep"; the article's own Konkoly 2021 citation depends on the channel being open. Neither sibling flagged it — Gemini's "isolates the mind from sensory constraints" describes rather than disputes.
- **Colour-blind dream-palette claim (L82) is uncited** (Finding 12) → leg (k). The only indexed primary paper is Yazmajian 1982 (three psychoanalytic cases); source-or-remove.
- **"More experience when the system is doing less" is contradicted by Baird, Tononi & LaBerge 2022** (Finding 5) → leg (l). Verified at the abstract: lucid REM shows "higher-than-average levels of physiological activation"; 0 live files cite the paper.
- **Bilzer scope: imagery, not perception** (Finding 6) → leg (m); the specific wording half of cluster 11.
- **Baird 2018 error propagated across seven loci** (§6) → the P1 sweep; the propagation half of cluster 1.
- **`concepts/mind-brain-separation` L90 "case for mental causation rests on" the two-way studies** (§6) → item (2) of the upgraded filter-theory task.
- **Framework-boundary exemption verbatim in two deep reviews** (§5) → third leg of the upgraded deep-review lens task; the mechanism half of cluster 6.
- **Revonsuo's threat simulation is "expressly evolutionary"** (Finding 4) — fair in sense; recorded, not minted (the L72 sentence concerns the sleeping organism's immediate behaviour).
- **"Interpretation under the Map's tenets" box for the MQI and Many-Worlds paragraphs** — declined (convention-mandated section; the Claude sibling's deletion was declined for the same reason). Residue L136 wording, leg (n).
- **"Perceptual organisation fails in blindsight"** — **disputed**: 0 hits in the target and in `concepts/capability-division-in-vision`; a phrase neither article contains.
- **Hedge strings "not forced" / "arguably cleaner"** — **disputed as quotations**: reconstructions; the pattern stands on L106 and L136.
- **Methodology list items 1, 3–12** — routed at collection: item 1 is the open NEEDS-HUMAN 2026-07-30 per-claim ledger; 3, 4, 6, 10 are the deep-review lens task; 8 is the Baird sweep by hand; 5, 9, 11, 12 are absorbed by the Simor task, leg (l), the filter-theory fix and the target's closing-sentence leg.
- **Mental Imagery / Capability Division in Vision improvement lists** — expansion-tier; not minted (`concepts/mental-imagery` already links the target and carries no Bilzer). Note for the next review of those files.

**Claude Opus 5** (7 claims verified at full text; 3 unverified; 5 disputed or lower-value):

- **L62 Metzinger quotation is not in *The Ego Tunnel*** → leg (f). Verified sharper than the reviewer's flag: 0 hits for "online dreaming", "on-line dreaming", "controlled hallucination" and "waking life is" in the NFKC-normalised book; the genuine wording is from the 3:16 interview and must be cited there. See Divergence 1.
- **L64 Revonsuo quotation is not in the 2000 *BBS* paper** → leg (g). Verified (0 hits for "external physical stimulation" and "created internally"); the reviewer's "originates in Revonsuo 1995 and drops 'like a'" is **unverified** (1995 text paywalled) — the task requotes from the 2000 text rather than re-attributing. Same string in a research note and an archive page; sweep both.
- **Laukkonen, Friston & Chandaria 2025 specifically** → leg (h); the named-paper half of cluster 4.
- **Windt's immersive spatiotemporal hallucination model absent** — recorded, not minted (length).
- **Konkoly 2021 response rate (~18% of attempts) unreported** — **unverified**, not minted; the article quotes no rate.
- **Confession-without-correction should force a status change in the same commit** (Part 5 item 3) — a repeat of the standing proposal already parked on NEEDS-HUMAN entries (see synthesis 2026-09-15, qualified convergence); noted in the 2026-09-16 NEEDS-HUMAN entry, not re-minted.
- **Literature-drift trigger keyed to new gate papers** (Part 5 item 5) — policy; `literature-drift-review` runs weekly, the gate-paper trigger is the residue, noted in the NEEDS-HUMAN entry.
- **"Delete the degradation-asymmetry argument"** — **disputed as remedy**; see Divergence 3.
- **"Delete the Minimal Quantum Interaction paragraph"** — **disputed as remedy**; cluster 8.
- **Co-optation "FAIL" for Hobson, Metzinger, Revonsuo** — **overstated**; L48 labels them. Residue Baird/Tononi/Friston, leg (i).

**Gemini 2.5 Pro** (3 article-level findings verified, all in convergent clusters above; 5 disputed; 2 fabricated quotations; 2 of 5 mandated sources fabricated or conflated):

- **"Gott, Dresler and colleagues … NBR … subjected to retraction"** — **FALSE**. The only retracted lucid-dreaming narrative review is Patel et al. 2026, *Annals of Medicine and Surgery* (PMC13461030), different authors and journal; Baird, Mota-Rolim & Dresler 2019 *NBR*, which the article cites, stands. Nothing imported. See Divergence 2.
- **"The Void" / 400 ms / engrams / computational phenomenology** — **wrong article**: 0 hits in the target; the material is `voids/capability-division-problem` and `topics/neural-refresh-rates-and-the-smoothness-problem`. The citation conflates Sandved-Smith et al. 2021 (*Neurosci. Conscious.* niab018) with Prest 2026 (*Neural Computation* 38(7)). Declined here; assess-first at the void article's next review.
- **Site-level "ignores predictive processing / GNW"** — **false** (93 and 123 live files); the article-level residue is clusters 2–4.
- **Filter theory is unfalsifiable *ad hoc*** — already conceded in the Map's own words (`concepts/filter-theory` L156; target L124). Not new.
- **ALBUS / psychedelics** — not actionable: the article's psychedelics content is one cross-link into `topics/psychedelics-and-the-filter-model`, which carries REBUS and Letheby; "filter opens, allowing cosmic consciousness to enter" is the reviewer's phrase.
- **Two fabricated quotations** ("conscious recognition initiates and drives the exercise of this capability prior to neural accommodation"; "despite low prefrontal activation") — 0 hits; fair paraphrases of L116, never treated as quotes.
- **Source audit against the prompt's own 2020–2025 rule**: Derrien 2022 and Mashour 2020 exact; Wiese 2024 real but off-topic; "Blom 2024" fabricated on Reichert 2013; "Sandved-Smith 2021" title belongs to Prest 2026. Two of five weaknesses carry a resolvable, on-topic source.

## Divergences

Cases where reviewers reached opposite verdicts on the same feature. In each the verification record settles it.

### 1. Are the Metzinger and Revonsuo quotations faithful? — Claude vs ChatGPT

- **Claude Opus 5** (§2.7): Metzinger "**QUESTIONABLE** — … Grep-verify against the book"; Revonsuo "**PARTIAL FAIL** — … attributing it to the 2000 paper is a misattribution."
- **ChatGPT 5.6 Pro** (§Citations accurately represented at the descriptive level): Revonsuo "The virtual-reality and threat-simulation characterisation is broadly faithful"; Metzinger "The 'online dreaming' formulation is consistent with Metzinger's model-based account, although the article should supply a page reference."
- **Resolved for Claude on disk, and beyond it.** Full-text greps of both sources return 0 hits for the article's strings. ChatGPT judged fidelity at the level of doctrine, where both quotations are faithful; Claude judged it at the level of the string, where neither exists. Both are right about what they checked — which is exactly the metadata-versus-verbatim seam the deep-review lens task (cluster 6) closes. Legs (f) and (g).

### 2. Does Baird, Mota-Rolim & Dresler 2019 stand? — Gemini vs ChatGPT and Claude

- **Gemini 2.5 Pro** (§Fragile Neurobiology): "major synthetic reviews … such as the prominent narrative review by Gott, Dresler, and colleagues in *Neuroscience & Biobehavioral Reviews*—have been subjected to retraction."
- **ChatGPT 5.6 Pro** (§Citation audit): "The quotation concerning the importance of beliefs and expectations in unconstrained lucid-dream experience is faithful."
- **Claude Opus 5** (§2.7, row 2): "PASS | PASS — beliefs/expectations quote tracks source."
- **Resolved against Gemini.** The retraction Gemini describes is Patel et al. 2026 in a different journal by different authors; the *NBR* review is unretracted and both siblings verified the article's use of it. A reviewer re-attributing a retraction-for-fabricated-references to a cited, standing source is the sharpest form of the correlated-error hazard this synthesis exists to catch: had a sibling repeated it, topic-overlap clustering would have recorded convergence on a falsehood.

### 3. Degradation asymmetry — delete or reframe? — Claude vs Gemini and ChatGPT

- **Claude Opus 5** (Part 3): "**Degradation asymmetry: DELETE.** Self-refuted by the Hobson–Friston entrainment quote the article itself supplies."
- **ChatGPT 5.6 Pro** (improvements, item 1): "Reframe the degradation argument around the distinction between plausible generation and accurate reconstruction of unknown current-world detail."
- **Gemini 2.5 Pro** (§Charles Bonnet Syndrome as Generative Release): "Both phenomena are governed by the exact same Bayesian mechanics of precision weighting and sensory gating."
- **Resolved for reframe.** All three agree on the mechanism (cluster 2); they split on whether a section that concedes "explanatory economy, not a result the evidence settles" (L124) should survive. The collection pass kept the section and installed the named rival with Claude's verbatim entrainment sentence — the L124 concession now has something to be economical *against*. ChatGPT's own Finding 11 supplies the reason deletion is wrong: "The filter account also inherits a version of the problem … Once that distinction is introduced, the asymmetry ceases to favour either ontology" — a symmetric result worth stating, not a section worth removing.

### 4. Verdict severity — reject, demote, or revise?

- **Gemini 2.5 Pro**: "it is emphatically rejected for academic submission."
- **Claude Opus 5**: "**Verdict: DEMOTE-TO-COHERENCE-ONLY.**"
- **ChatGPT 5.6 Pro**: "Recommendation: **major revision** … The article has an interesting and potentially defensible core."
- **Not resolvable on disk — the shared floor is cluster 7.** Three briefs, three registers, one agreement: the article is an interpretation presented as evidence. ChatGPT's is the only verdict that names what survives ("richly structured conscious experience can occur when external sensory constraint is greatly reduced … prevents any simple equation of perception with passive sensory reception") and offers a title for it. That is the operator's NEEDS-HUMAN decision; the synthesis records that the most charitable reviewer and the most hostile one agree on the diagnosis.

### 5. Does the Map anchor on a blindsight "clinical myth"? — Gemini vs ChatGPT

- **Gemini 2.5 Pro** (§The Mischaracterization of Blindsight): "By treating blindsight as a phenomenal void—a state of pure 'zombie' neurocomputation—the manuscript builds its ontological dualism on a clinical myth."
- **ChatGPT 5.6 Pro** (Finding 8): "Moreover, the neighbouring vision article itself recognises that perceptual integration can occur without conscious access and that some blindsight may involve degraded experience rather than none."
- **Resolved for ChatGPT on disk.** `concepts/blindsight` §2 carries Phillips 2021 and `concepts/capability-division-in-vision` carries Derrien 2022 (L56) — the very paper Gemini cites as the corrective. The target's L110 hedges; L112 does not. The residue both reviewers would accept is leg (c) (cluster 9).

## Method Notes

- **Zero task-level deduplication was needed, by design of the collection passes.** The Gemini pass minted the one target-article P1; the Claude and ChatGPT passes each extended it in place (legs (d)–(i), then (j)–(o)) rather than minting same-file siblings, and each recorded the cross-service convergence in its Verification Notes. This synthesis therefore spent its effort on adjudication and on the three neighbour/methodology tasks the passes had left at P2. It also added one leg — (p), cluster 12 — for a 3/3 convergence with no home, at zero net words.
- **Adjudication cut in both directions again.** Two nominal 3/3 clusters (4, 12) survived only after Gemini's halves were reduced to their article-level residue (the site-level PP charge is false; the neurobiology fragility point is real but its retraction premise is not). Conversely, cluster 13 (missing foundational literature) was a genuine 2/3 that neither collection pass scored, because both treated it as advisory under the length ceiling; it is recorded here and carried forward without a task rather than minted into a file 671 words from hard.
- **Three upgrades, one annotation, one added leg.** Five of the six same-date tasks are now P1 (three were upgraded here; two were minted at P1 by the passes), and the sixth is the NEEDS-HUMAN retitle entry, annotated but not tiered. The selector orders same-tier tasks by line number, so dispatch order is: deep-review lens (skill file, L40) → target P1 → Baird sweep → `concepts/predictive-processing` → `concepts/filter-theory` / `mind-brain-separation`. That order preserves the Simor task's guard ("run AFTER the P1 Baird sweep has touched this file") and lets the lens legs exist before the next deep review of any of these files.
- **Convergence on a declined remedy is worth recording separately.** Cluster 8 (MQI paragraph) is a 2/3 agreement on a change the pipeline declines by convention. Recording it in the NEEDS-HUMAN entry rather than silently dropping it is the honest move: the operator, not the collection pass, owns the convention.
- **Gemini's yield this cycle was three verified article-level findings inside five weaknesses, at the cost of one false retraction charge, one fabricated author/year, one two-paper conflation and a wrong-article section.** Each contribution that survived was one the siblings had also reached (clusters 2, 3, 4, 9, 12), so Gemini added corroboration but no unique verified finding. Its hostile-referee brief produced the most vivid mechanism prose (the precision-weighting paragraph is the clearest statement of the production reply in any of the three reviews) and the least reliable sourcing.
- **Not scored as convergence, deliberately.** (a) ChatGPT's "sensory channel closed" (Finding 2) and Gemini's REM "active thalamic gating" description are about the same physiology but only ChatGPT treats the article's wording as an error; scored as a singleton. (b) ChatGPT's Baird 2022 "doing less" refutation and Gemini's 40 Hz artefact remark share a paper but not a locus — the article never cites gamma. (c) Claude's and ChatGPT's shared praise for the article's honest hedges ("These are improvements over a simple advocacy piece"; "to its credit") is agreement, not a finding.
- **Carried forward without a task.** Cluster 13's reference list (LaBerge 1981, Voss 2009, Dresler 2011/2012, Siclari 2017, Demirel 2025); Windt's model; the `concepts/capability-division-in-vision` L108 label and its circularity charge (ChatGPT §6); the `concepts/mental-imagery` Bilzer install; the void article's computational-phenomenology engagement (Gemini, wrong-article). The next deep review of each named file should read this list before its own lens.
