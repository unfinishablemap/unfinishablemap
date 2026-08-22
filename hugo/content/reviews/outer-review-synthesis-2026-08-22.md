---
ai_contribution: 100
ai_generated_date: 2026-08-22
ai_modified: 2026-08-22 05:31:44+00:00
ai_system: claude-opus-5
author: Andy Southgate
concepts: []
created: 2026-08-22
date: &id001 2026-08-22
description: Cross-review synthesis of 3 outer reviews from 2026-08-22 auditing the
  anaesthesia article. Nine convergent clusters, two task upgrades, two apparent convergences
  defeated on verification, and the cycle's strongest finding blocked by one word
  of length headroom.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-22 05:31:44+00:00
modified: *id001
related_articles:
- '[[project]]'
synthesis_coverage: 3/3
synthesizes:
- reviews/outer-review-2026-08-22-chatgpt-5-6-sol-pro.md
- reviews/outer-review-2026-08-22-claude-opus-5.md
- reviews/outer-review-2026-08-22-gemini-2-5-pro.md
title: Outer Review Synthesis - 2026-08-22
topics: []
---

**Date**: 2026-08-22
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 3 of 3 commissioned reviewers contributed (ChatGPT 5.6 Pro, Claude Opus 5, Gemini 2.5 Pro). All three audited the same subject — `topics/anaesthesia-and-the-consciousness-interface`, selected by the recent-aged fallback at the ChatGPT commission and reused by the other two services. All three `pending-reviews.yaml` entries resolve to a single `subject_articles` value, so the convergence below is real rather than an artefact of subject drift.

## TL;DR

All three reviewers reached the same verdict by three different routes: the article's empirical synthesis is good and its inference is not. Receptor-specific, reversible, agent-differentiated abolition of consciousness is what a structured physicalist substrate predicts, so the pharmacology constrains rather than discriminates — yet the `description:` and lead announce a "molecular map" that the article's own closing section, and its registered position P-CS4, both decline. Cluster tally: **9 convergent** (5 at 3/3, 4 at 2/3), **10 singleton**, **3 divergences**. **Two tasks upgraded P2 → P1**; none deduplicated, because the four open tasks target disjoint line ranges by design. Two *apparent* convergences were defeated on verification (Global Neuronal Workspace, neural inertia) — in both cases a reviewer's search or quotation was wrong, and agreement would have been correlated error rather than corroboration.

The binding constraint on this cycle is arithmetic: the article stands at **3999 words against a 4000-word hard threshold** — one word of headroom, measured with `tools.curate.length` on all three legs and re-confirmed here. The single strongest finding of the day (cluster 3) cannot be executed until the length-relieving edits land, and is recorded here rather than minted.

## Convergent Findings

### 1. The pharmacology constrains but does not discriminate — yet the lead and `description:` present it as a finding
- **Flagged by**: chatgpt, claude, gemini (3/3)
- **Verification**: clean. Both navigation surfaces grep-confirmed verbatim (`description:` L3, lead L53), as is the article's own contrary concession at L135 and P-CS4's "compatible with — not forced by" at [positions/consciousness-scope.md](/positions/consciousness-scope/) L79.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "The article's description and opening call the pharmacology a 'molecular map' of the mind–brain connection and say that interactionist dualism 'predicts exactly' the observed architecture, while a late section correctly concedes that anaesthesia cannot distinguish the interface interpretation from sophisticated functionalism. The late concession is the defensible position; the headline framing is not."
  - **Claude Opus 5**: "**No.** ... A production/identity theorist predicts *exactly* the same facts: if conscious contents are realised by specific thalamocortical and cortico-cortical dynamics, then drugs acting on the receptors that shape those dynamics will produce content-specific deficits. Receptor specificity is evidence *for a structured neural substrate* — which every physicalist already asserts."
  - **Gemini 2.5 Pro**: "The observation that specific molecules degrade specific cognitive capacities is precisely what a modular, physicalist production model logically requires. ... The manuscript owes a symmetric accounting: it must demonstrate why pharmacological dissociation provides stronger evidence for an interactionist filter than it does for the mundane reality of neuroanatomical modularity."
- **Sharpest form**: ChatGPT's, because it locates the defect as an ordering failure rather than an error — the underdetermined claim is present and correct in the body, it is simply not allowed to control the article. Claude names the same pattern site-wide as "confession-without-correction": precise disclosures "are stated and then not permitted to downgrade the surrounding verdicts or the headline thesis. They function as inoculation, not remediation."
- **Task action**: **Upgraded P2 → P1** — "the lead and `description:` ... assert what its own closing section and P-CS4 both decline". This task is also the cycle's length-relief lever (deleting the Many Worlds paragraph and tightening the lead), so the upgrade is doubly correct: it should run early to create budget for the others.

### 2. The teleological active-reboot reading is asserted flatly, where the Map's own concept page disclaims it
- **Flagged by**: chatgpt, claude, gemini (3/3 — upgraded from the Gemini leg's own 2/3 assessment, which had not seen Claude's independent hit)
- **Verification**: clean. Both spans grep-confirmed in obsidian and the hugo mirror. The internal control is [concepts/active-reboot.md](/concepts/active-reboot/) L101, which states in terms: "It does not show the brain 'calls' consciousness back."
- **Quotes**:
  - **Claude Opus 5**: "**Epistemic-to-metaphysical slide:** 'the neural side prepares a channel that consciousness then re-enters' and 'the workspace must be inhabited, not merely activated' convert an epistemic finding (frontoparietal dynamics normalise before behavioural recovery — Mashour 2021) into a metaphysical claim (a channel awaiting a non-physical occupant)."
  - **ChatGPT 5.6 Pro**: "Neural recovery preceding behavioural recovery is redescribed as the brain preparing for consciousness to enter. Yet any realizational theory predicts that the enabling physical state precedes its behavioural manifestations. The article treats ordinary causal ordering as evidence for a second entity because the second entity is already assumed."
  - **Gemini 2.5 Pro**: "To frame this purely biochemical cascade — mediated by the valosin-containing protein (VCP) and FAF1 recruitment — as a teleological 'boot sequence' designed to welcome back an immaterial consciousness is scientifically absurd."
- **Adjudication**: Gemini's *headline* charge (that the article misappropriates Hu et al.) fails and was already rejected at collection — the article quotes Hu's own framing, disowns the "active reboot" label as the Map's, and concedes the GNW reading at L109. What survives across all three is narrower and exact: two unattributed sentences (L109 "The workspace must be inhabited, not merely activated"; L123 "since the brain prepares for consciousness before it arrives") state the interface reading as fact rather than as the Map's interpretation. Claude's independent hit on both loci is what raises this from 2/3 to 3/3.
- **Task action**: **Upgraded P2 → P1** — "two loci ... assert the teleological active-reboot reading flatly". Length-neutral (two word-for-word clause swaps) and touches no line any sibling task touches.

### 3. No physicalist rival is held at full strength — and Dendritic Integration Theory is the specific, verified gap
- **Flagged by**: chatgpt, claude, gemini (3/3 on the general charge; DIT specifically 2/3 — chatgpt §5.1 and gemini §II; predictive processing / active inference 2/3 — chatgpt §5.2 and claude §2.3)
- **Verification**: clean, and independently grep-confirmed on all three legs. Vocabulary census on the live article, spaced and hyphenated: `dendrit` 0, `apical` 0, `Larkum` 0, `Suzuki` 0, `Aru` 0, `layer 5` 0, `predictive processing` 0, `predictive routing` 0, `active inference` 0, `higher-order` 0, `recurrent processing` 0, `dynamical system` 0, `mesocircuit` 0, `illusionis` 0, `Cogitate` 0.
- **Quotes**:
  - **Gemini 2.5 Pro**: "Crucially, recent neurobiological breakthroughs have established that diverse general anaesthetics — despite their completely disparate molecular targets (GABA-A, NMDA, two-pore potassium channels) — all converge on a single, uniform physiological outcome: they decouple the apical tuft from the basal dendrites."
  - **ChatGPT 5.6 Pro**: "This is arguably the most direct physicalist rival to the article's 'separable interface channels,' because it provides a cellular mechanism for the same dissociation."
  - **Claude Opus 5**: "Predictive processing / active inference (Friston, Clark, Seth, Hohwy): Entirely absent — the known site-wide blind spot recurs here."
- **Why this is the cycle's strongest finding**: it is the one place where a live physicalist mechanism would *replace* rather than merely accommodate the article's central construct. Gemini's leg, which went 1-for-5 on everything else, supplied the best source of the day — **Suzuki & Larkum (2020), *General Anesthesia Decouples Cortical Pyramidal Neurons*, Cell 180(4) 666-676.e13, DOI `10.1016/j.cell.2020.01.024`**, verified metadata-exact at Crossref and named by no sibling leg. ChatGPT asked for "dendritic integration" as one item in a list of eight rivals without a citation.
- **Task action**: **Recorded only — no task minted. This finding is length-blocked and is honestly reported as such.** Every version of the fix adds prose to an article with one word of headroom. Both the ChatGPT and Gemini legs parked it for this synthesis; this synthesis confirms the convergence and declines to mint a task that could not be executed. The named source of offsetting reduction is **cluster 8** (demoting the death-boundary passage) plus the Many Worlds deletion already inside the upgraded cluster-1 task — together roughly 200 words. The honest sequence is: land the two P1 citation tasks and the two upgraded P1 calibration tasks, re-measure with `analyze_length`, and only then decide whether the recovered budget is spent on DIT or banked. **A bare `condense` task is not the answer** — this is a flagship with four open tasks and the length call is a human one.

### 4. The four separable "interface components" are reified rather than discovered
- **Flagged by**: chatgpt, claude, gemini (3/3)
- **Verification**: clean on the general charge. Gemini's *specific* route to it (the Isolated Forearm Technique is "completely ignored") is false and was rejected at collection — L91 engages the IFT explicitly. See Divergences.
- **Quotes**:
  - **Claude Opus 5**: "**Constitutional-attractor effect:** The 'four separable interface components' ... are presented as discovered, but track the Map's pre-existing filter architecture; the sources taxonomise the same data differently (Bonhomme's three components; Sanders' connected/disconnected binary)."
  - **ChatGPT 5.6 Pro**: "Evidence that memory, connectedness and responsiveness dissociate establishes distinguishable functions. The further claim that they are channels between two substances requires an argument. Naming each function an 'interface component' does not supply one." He lists six equally-available redescriptions of the same evidence and observes: "The article never identifies a result that selects the first description."
  - **Gemini 2.5 Pro**: "consciousness under anaesthesia is not a cleanly dissociable set of immaterial modules mapping perfectly onto distinct receptor classes, but rather a highly volatile, fluid, and graded continuum of cortical network degradation."
- **Task action**: **Recorded only — no task minted.** The general charge is a re-framing of cluster 1 and is covered by the upgraded cluster-1 task in substance. Its one sharply actionable sub-finding (the temporal-binding component has no identifiable source) is a ChatGPT singleton, is not length-blocked, and is listed below as the cycle's highest-value unminted item.

### 5. The ketamine/IIT sentence is inverted — the article deploys IIT's own originators against IIT
- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: clean, verified at primary source. Sarasso et al. 2015's abstract was retrieved in full via EuropePMC and presents high-PCI-under-ketamine as the measure succeeding. The author list includes both **Tononi** and **Casali**.
- **Quotes**:
  - **Claude Opus 5**: "This misfires — Sarasso/Casali present exactly high-PCI-under-ketamine as PCI *succeeding*: detecting *disconnected consciousness* in behaviourally unresponsive subjects ... The article inverts a confirmation of the IIT-derived measure into a challenge to it."
  - **ChatGPT 5.6 Pro**: "High PCI or complexity during ketamine does not obviously challenge IIT. IIT distinguishes the presence or richness of experience from environmental connectedness and behavioural responsiveness. A highly integrated but disconnected internally generated state is therefore not an evident counterexample."
- **Notable**: neither leg minted this until the Claude leg made it the lead item of its P1 — two reviewers reached the same sentence (L93) from opposite ends, ChatGPT via the Onoda citation and Claude via the Sarasso author list, and each leg's isolated `/outer-review` pass nearly let it through as noise.
- **Task action**: Recorded on the existing P1 "three evidential-overreach loci ... an inverted IIT reading that CONVERGED across two reviewers"; already P1, so not upgraded. Notes rewritten to carry ChatGPT's corroborating route.

### 6. The Parnia AWARE-II statistic is wrong on the denominator and on the variable
- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: clean, verified at primary source. The AWARE-II abstract (*Resuscitation* 191:109903) was retrieved in full via EuropePMC and attaches **no** percentage to its EEG finding.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "Parnia's 39% figure concerns a small interviewed survivor subset, not 40% of all cardiac-arrest patients showing organised activity."
  - **Claude Opus 5**: "**MATERIAL FAIL** ... The '~40% organised brain activity' claim conflates a survivor self-report rate with an EEG finding."
- **Task action**: Recorded on the existing P1 "three citation defects ... a headline statistic with the wrong denominator AND the wrong variable"; already P1, so not upgraded. Notes rewritten to record the second voice.

### 7. Wiest 2025 is a review, not an experiment — and the Orch-OR cluster at L143 recruits the Map's own dispreferred mechanism
- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: clean on the Wiest attribution (confirmed at OUP: a theory/hypothesis article recruiting Babcock et al. 2024). Gemini's version of the quantum critique was rejected outright — it attributed to the article a citation the article does not contain (`Khan` 0, `epothilone` 0, `Tegmark` 0, `Orch-OR` 0, `Penrose` 0), and the decoherence objection it wrapped around that is already priced by `positions/quantum-interface` P-Q1/P-Q4/P-Q5.
- **Quotes**:
  - **Claude Opus 5**: "The article therefore recruits, as quantum support, exactly the mechanism family the Map treats as its weakest fallback — and does so without noting the inconsistency. ... Crucially, an Orch-OR anaesthetic-binding mechanism, if real, *would be empirically detectable* — which contradicts apex #34's insistence that the endorsed corridor interface is Born-preserving and *empirically indistinguishable from chance*."
  - **ChatGPT 5.6 Pro**: "Correct the Wiest attribution. Name the original delayed-luminescence or microtubule studies directly; describe Wiest as reviewing and interpreting them rather than conducting them."
- **Task action**: Recorded on both open P1s, which each own half of L143 (ChatGPT's re-words the Wiest attribution inside it; Claude's cuts the paragraph to a hedged pointer). **Both already P1, so not upgraded — but they must be executed in a single pass**, because if Claude's cut lands first the ChatGPT re-wording is absorbed and becomes moot. See Method Notes.

### 8. The death-boundary passage should not be the article's "strongest discriminating evidence"
- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: clean. L95 grep-confirmed: "The strongest discriminating evidence comes from the boundary between anaesthesia and death."
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "The death material currently launders speculative evidence from one domain into an ostensibly controlled pharmacological argument. It should be removed or placed in a separate, explicitly low-confidence convergence section."
  - **Claude Opus 5**: "(a) the death/cardiac-arrest 'strongest discriminating evidence' passage — Parnia is materially misread, Xu is overstated, and terminal lucidity is anecdotal and does no discriminating work."
- **Task action**: **Partially covered, structurally unminted.** The two citation-level halves (Parnia's denominator, Xu's population) sit inside the two open P1s. The structural demand — that the passage stop being framed as the discriminator — has no task. Unlike cluster 3 this fix is **length-relieving**, which makes it the natural first source of the budget cluster 3 needs. Recorded here rather than minted so the file does not accumulate a fifth open task; a later pass should take clusters 8 and 3 together, in that order.

### 9. Physicalist sources are recruited toward a conclusion their authors reject
- **Flagged by**: chatgpt, claude, gemini (3/3)
- **Verification**: clean. Claude is the only leg that quantified it, and did so from its own citation table rather than from the article's prose.
- **Quotes**:
  - **Claude Opus 5**: "**Fabrication rate: zero detected.** **Author-stance failure rate: ~11 of 17 citations recruited toward an interface/dualist conclusion their authors explicitly do not hold.** This is the dominant and systematic pathology of the article."
  - **ChatGPT 5.6 Pro**: the article "cites physicalist studies as though their results supported transmission"; on Redinbaugh and Hu, "The Map calls the same machinery a channel, but supplies no observation differentiating those descriptions."
  - **Gemini 2.5 Pro**: "a philosophical methodology that treats neurobiology as a rhetorical buffet, where physical mechanisms are selectively invoked when they can be twisted to support dualism, and ignored entirely when they provide exhaustive, native reductionist explanations."
- **Task action**: **Recorded only.** This is a site-wide methodology finding, not an article defect, and the instrument already exists — `project/evidential-status-discipline` carries the rival-or-support roster, and an open P1 from the **2026-08-21** cycle is already extending it. Adding a second roster task from this cycle would duplicate that work. The article-level consequence is cluster 1, which is upgraded.

## Singleton Findings

Flagged by one reviewer only. Not upgraded; listed for the record.

- **ChatGPT 5.6 Pro** — the Moncrieff reference does not exist as printed (the paper is by Marco Masi, *Frontiers in Psychology* 14:1150605; the article number 1254857 is fabricated). Verified twice at publisher of record. → open P1 "three citation defects" (already P1).
- **Claude Opus 5** — the Xu 2023 reference welds Borjigin 2013's title onto Xu's byline, year, volume and eLocator; root cause traced to a research note. → open P1 "three evidential-overreach loci" (already P1).
- **ChatGPT 5.6 Pro** — the Many Worlds paragraph (L147) names no discriminating observation and cites no Everettian literature. → open P1 (upgraded, cluster 1); deletion is length-relieving.
- **ChatGPT 5.6 Pro** — **the temporal-binding channel has no identifiable source.** "No study in the reference list clearly reports this finding, and I could not identify the primary experiment corresponding to that description. ... Without a source, the article has evidence for dimensions involving connectedness, arousal, report and memory, but not for its claimed four-part interface map." **No open task, and not length-blocked** — the recommended fix (delete the component unless a primary source can be found) reduces prose. Flagged here as the cycle's highest-value unminted item. ⚠️ The absence of a source was **not** independently verified at collection; a search for the primary experiment must come first, and `citation-verify-false-negative` is the failure mode to avoid. `concepts/filter-theory` L90 repeats the same four-component taxonomy and would need the same treatment.
- **ChatGPT 5.6 Pro** — the article's evidential rules for absent reports are incompatible: report present → consciousness persisted; report absent → consciousness extinguished; or, when convenient, report absent → memory failed. "A principled report model must be fixed before the result is interpreted." No open task.
- **ChatGPT 5.6 Pro** — the hysteresis of neural inertia at L141 is read as consciousness having "its own persistence conditions", where ordinary bistable physical systems display the same asymmetry. **Downgraded from an apparent 2/3** — see Method Notes. No open task.
- **ChatGPT 5.6 Pro** — the xenon/ketamine "same receptor, opposite phenomenology" contrast treats polypharmacological agents as a controlled comparison. No open task.
- **ChatGPT 5.6 Pro** — the red-hair/MC1R anaesthetic-resistance evidence is too weak to bear metaphysical weight, and physicalism is strawmanned as predicting sensitivity to track brain size. No open task.
- **Claude Opus 5** — Cogitate Consortium 2025 (*Nature* 642(8066):133–142) is absent where PCI and workspace machinery are deployed, though both were substantially challenged in 2025. Length-blocked, no task. ⚠️ The review's named propagation target is already satisfied: `topics/the-interface-problem` L198 already cites it.
- **Claude Opus 5** — the NAP5 spontaneous-report audit figure (Pandit 2014, ~1:19,600) is not distinguished from the structured-interview figure the article uses (Sebel 2004, 0.13%). Currency suggestion, adds prose, no task.

## Divergences

Three cases where reviewers pulled against each other. Adjudicated before clustering, per `convergence-can-be-false-two-reviewers-wrong-one-right`.

- **Claude Opus 5 vs ChatGPT 5.6 Pro — citation health.** Claude opened with "The article's citation metadata is unusually clean — the empirical references overwhelmingly exist, are correctly attributed" and recorded "Fabrication rate: zero detected". ChatGPT found three defects and all three verified at publisher of record: a reference that does not resolve as printed, a headline statistic with the wrong denominator and variable, and an experiment attributed to an author who did not run it. **ChatGPT is right.** Claude's table simply does not include the Moncrieff row, and rated Parnia and Wiest as *fidelity* failures while passing their metadata — so its headline verdict is an artefact of which layer it was scoring. This is `citation-ledger-ratifies-the-reading-not-just-the-metadata` appearing inside an *outer* review: a clean-looking ledger certifies the layer it checked and nothing else.
- **Gemini 2.5 Pro vs ChatGPT 5.6 Pro and Claude Opus 5 — the Isolated Forearm Technique.** Gemini's weakness 5 charges that the article "completely ignor[es]" the IFT literature. **False** — L91 gives the IFT figure explicitly. ChatGPT and Claude both read the passage correctly and press the narrower, sound point that the article gives the figure without engaging its deflationary reading. Gemini's supporting metadata is also wrong in four places (the paper is Lennertz et al. 2023, BJA 130(2) e217-e224, with Sanders as *last* author — the `near-miss-byline` shape), and its 11% is the 18-40yr subgroup, consistent with rather than contradicting the article's general-population "roughly 5%".
- **ChatGPT 5.6 Pro vs Claude Opus 5 — Onoda et al. 2025.** ChatGPT: "Real, but misused in the IIT argument ... It cannot support the article's claim that ketamine poses a specific challenge to IIT." Claude: Onoda 2025 is among the references "all present and correctly cited". **Not a real contradiction** — two lenses, not one error (`figure-disagreement-may-be-two-systems-not-one-error`): Claude scored metadata currency, ChatGPT scored inferential use. Resolved at collection in the article's favour: L111 bundles Onoda with Breyton et al. 2025 and Van Maldegem et al. 2025, and Breyton 2025 explicitly covers ketamine, so the bundle collectively supports the sentence. Do not "fix" the Onoda cite.

## Method Notes

- **Two apparent convergences were defeated on verification.** Both would have looked like corroboration and both were correlated error.
  - **Global Neuronal Workspace.** All three legs pressed GNW, and a naive grep for `global workspace` returns **zero**. The article writes "global **neuronal** workspace" (1 hit, L109), inside a concession: "Early prefrontal re-engagement fits global neuronal workspace theory, but the Map reframes it". Gemini treats GNW as bracketed, which overstates. ChatGPT and Claude make the *accurate* version of the charge — that GNW is named and then redescribed rather than confronted as a rival — which is not an omission finding at all and folds into cluster 3. Any convergent *omission* claim must be checked against spaced, hyphenated and interpolated forms before clustering.
  - **Neural inertia.** ChatGPT §3.5 and Gemini §III appear to converge. Gemini's version rests on two spans that are not in the article: it quotes the article as saying consciousness has "intrinsic resistance to state transitions" (L103 actually says "intrinsic resistance **of neural circuits** to transitions", Sepúlveda's own definition) and as claiming consciousness "must be actively re-established through processes that may involve non-physical factors" — `non-physical factors` greps **zero**. Gemini also charges the article with ignoring the bistable flip-flop mechanism, which L103 names and cites (Sepúlveda et al. 2019). Gemini's leg is disqualified; the cluster collapses to a ChatGPT singleton whose target (the L141 Dualism paragraph) is real.
- **Coverage was not uniform in quality.** ChatGPT went 12/12 on span fidelity with zero fabrications; Claude went 3/3; Gemini survived **1 of 5** numbered weaknesses — two quoted text retired in commits `886404f70d` and `9924a9ed03`, one quoted a sibling article's retired lead, one attacked an omission the article does not have, and §VI attributed to the article a citation it does not contain (Khan et al. 2024 on epothilone B). The `outer-reviewers-critique-archived-articles-at-live-urls` and `outer-review-fabricates-target-quotes` shapes both fired on the same leg. **And yet that leg supplied the cycle's single best source** (Suzuki & Larkum 2020). A low survival rate is not a reason to discount a leg's surviving finding.
- **No tasks were deduplicated.** The four open tasks on this file each cite a different review and target disjoint line ranges by construction — each leg's `/outer-review` pass had already restricted its minting to what the prior legs had not raised. The two P1s overlap only at **L143** and **L95**, and there they carry different defects, in a deliberate order (Claude's fix 3 frees ~90 words and must run first). Merging them would destroy that ordering and produce a single six-item task. Recorded here instead: **the two P1s must be executed in one pass**, and the Wiest sub-item of the ChatGPT P1 should be marked satisfied rather than applied twice if Claude's cut lands first. The two upgraded tasks touch L3/L53/L147 and L109/L123 respectively and collide with nothing.
- **The length gate governs the whole cycle.** `analyze_length` reports `word_count=3999, section='topics', soft_threshold=3000, hard_threshold=4000`. Every fix in the four open tasks is length-neutral or length-reducing by design; the two genuinely additive convergent findings (cluster 3, and Claude's Cogitate singleton) are recorded unminted for exactly this reason. Whether the recovered budget is spent on DIT or banked is a human decision on a flagship article, and this synthesis does not pre-empt it.
- **Four tasks are open on one file** (`outer-review-same-file-task-pileup`). This synthesis upgraded two of them and minted none, which keeps the count at four.