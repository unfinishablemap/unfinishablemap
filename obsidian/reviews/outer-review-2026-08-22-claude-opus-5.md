---
title: "Outer Review - Claude Opus 5 (2026-08-22)"
created: 2026-08-22
modified: 2026-08-22
human_modified: null
ai_modified: 2026-08-22T04:39:15+00:00
draft: false
description: "Claude Opus 5 audits the anaesthesia article: an inverted IIT reading of the ketamine PCI result, a dying-brain study described as the wrong experiment, and an Orch-OR subsection that recruits the Map's own demoted mechanism as support."
topics:
  - "[[the-interface-problem]]"
  - "[[quantum-biology-and-neural-consciousness]]"
concepts:
  - "[[filter-theory]]"
  - "[[interactionist-dualism]]"
related_articles:
  - "[[project]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "claude-opus-5"
ai_generated_date: 2026-08-22
last_curated: 2026-08-22
outer_review_status: processed
outer_review_conversation_url: https://claude.ai/chat/f0878387-7623-4f73-84a9-88b94d60aa4f
outer_review_extraction_method: js-dom
subject_type: recent
subject_title: "Audit anaesthesia-and-the-consciousness-interface"
subject_articles:
  - topics/anaesthesia-and-the-consciousness-interface.md
subject_source: reuse:pending-reviews:outer-review-2026-08-22-chatgpt-5-6-sol-pro.md
---

**Date**: 2026-08-22
**Reviewer**: Claude Opus 5
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Act as a hostile but fair referee for one article on The Unfinishable Map (https://unfinishablemap.org), a philosophy site defending interactionist dualism with minimal quantum-level interaction. Subject: https://unfinishablemap.org/topics/anaesthesia-and-the-consciousness-interface/ - last substantively modified 2026-08-13. Audit it as it now stands. Verify each citation at its primary source: metadata, and whether the article's paraphrases match what those works actually found. Test for insufficient evidence, missed counterarguments, tenet-protective bracketing, and stale references against the current 2020s anaesthesia and consciousness-science literature. State explicitly whether the inference from anaesthetic pharmacology to an interface reading is warranted, and name the physicalist or deflationary rivals it leaves unengaged. Assess its integration with neighbouring Map articles and consistency with the positions register. Consult the changelog at https://unfinishablemap.org/workflow/changelog/ - the site changes daily and web-search indices lag 24-48 hours, so recent work will not surface in search alone. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Adversarial Audit: "Anaesthesia and the Consciousness Interface" (unfinishablemap.org)

*Audited as live at 2026-08-22. Target last substantively modified 2026-08-13; the changelog window through 2026-08-21 contains no entry touching this article, its tenet anchors, or its registered position, so the text audited is current. Neighbouring pages fetched: /tenets/, /topics/quantum-biology-and-neural-consciousness/, /topics/born-rule-and-the-consciousness-interface/, /concepts/filter-theory/, /concepts/degrees-of-consciousness/, /positions/, plus the apex #33/#34 material via the register and outer-review record.*

## 1. TL;DR VERDICT

**REVISE-HARD**, with two named sections demoted to **COHERENCE-ONLY**. The article's citation metadata is unusually clean — the empirical references overwhelmingly exist, are correctly attributed, and are quoted or paraphrased faithfully. The failure is not fabrication; it is **inferential**. The article commits a systematic **constrain-vs-establish gate failure**: every genuinely discriminating datum it invokes (agent-specific PCI dissociation, disconnection-not-extinction, neural inertia, active reboot, stochastic emergence) is equally predicted by mainstream physicalist neuroscience — and was, in fact, produced by it — yet the prose repeatedly slides from "compatible with filter theory" to "evidence for the interface." The article is aware of this at several points and says so; but it banks those confessions as epistemic credentials without letting them change the verdicts they impugn (**confession-without-correction**, the site's dominant pathology, present here in force). The Minimal Quantum Interaction subsection recruits Orch-OR/microtubule anaesthetic-binding work (Craddock, Wiest) that is (a) empirically contested and single-lab and (b) inconsistent with the Map's own preferred post-decoherence corridor mechanism — a **co-optation firewall failure** pointed inward at the site's own tenet ordering.

- **The pharmacology→interface inference is NOT warranted.** Reversible, receptor-specific, agent-specific abolition of consciousness is exactly what a production/identity model predicts; none of the cited dissociations discriminate between production and interface readings.
- **The article's single strongest move — mainstream anaesthesiology's convergence on "disconnection, not extinction" — is real and correctly cited, but the sources (Bonhomme, Montupil, Sanders, Laureys/Gosseries, Tononi) are explicitly physicalist and the framing carries no dualist entailment.**
- **The quantum section is the weakest and most detachable; cut it to a single hedged pointer, and flag its Orch-OR citations as inconsistent with the Map's own corridor reading and as no-new-data/single-lab.**

## 2. DIMENSIONAL ANALYSIS

### 2.1 Citation Verification Table (three layers: metadata / verbatim fidelity / author-stance)

| Citation | (a) Metadata | (b) Fidelity | (c) Author-stance |
| --- | --- | --- | --- |
| Sarasso et al. 2015, *Curr Biol* 25(23):3099–3105 | PASS — exact | PASS — propofol/xenon low PCI + no report; ketamine high PCI + vivid dreams; faithful | **FAIL** — Sarasso/Boly/Massimini/Tononi/Laureys [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0960982215012427) are IIT/physicalist; the paper reads PCI as a *neural* marker of (disconnected) consciousness, not interface evidence |
| Montupil et al. 2023, *BJA Open* 8:100224 | PASS | PASS — "disconnection sufficient" faithful | **FAIL** — explicitly physicalist: "it is agreed that consciousness is generated by brain activity… there must be neuroanatomical and neurophysiological substrates of consciousness, or neural correlates" |
| Bonhomme et al. 2019, *Front Syst Neurosci* 13:36 | PASS | PASS — three-component decomposition (wakefulness/internal/external awareness) faithful | **FAIL** — title "a probe to explore consciousness"; naturalist NCC framing |
| Kallionpää et al. 2018, *Br J Anaesth* 121(1):270–280 | PASS | PASS — N400/semantic-congruity abolished, words still processed under dexmedetomidine; faithful | **FAIL** — physicalist EEG/ERP study |
| Mashour 2024, *Neuron* 112(10):1553–1567 | PASS | PASS — emergence as active process on distinct circuitry; "core elements" framing faithful | **FAIL** — Mashour is a GNW/physicalist; review frames anaesthesia within GNW+IIT ("global neuronal workspace; integrated information" are its keywords) |
| Mashour et al. 2021, *eLife* 10:e59525 | PASS | PASS — frontoparietal restoration; executive function returns first; faithful | **FAIL** — physicalist |
| Sepúlveda et al. 2019, *Anaesthesia* 74(6):801–809 | PASS | PASS — neural inertia/hysteresis, flip-flop bistability; faithful | Physicalist pharmacological review |
| Friedman et al. 2010, *PLoS ONE* 5(7):e11903 | PASS | PASS — conserved behavioural-state barrier | Physicalist |
| Redinbaugh et al. 2020, *Neuron* 106(1):66–75 | PASS | PASS — central-lateral thalamus + deep cortical layers most sensitive; CL stimulation restores wake dynamics; faithful | **FAIL** — an explicit thalamocortical-NCC paper; its causal, anatomically-specific reading is a *generator/substrate* claim, the opposite of the article's "diffuse generator" strawman |
| Hu et al. 2023, *Nat Neurosci* 26(5):751–764 | PASS | PASS — KCC2 ubiquitin degradation in VPM; active, anaesthetic-independent; quotes faithful; article correctly flags mouse study + honestly downgrades to a 3-mechanism-class-plus-one-within-class span | **FAIL** — physicalist molecular neuroscience; "active process" is theirs, the "active reboot"/channel-reopening interface gloss is the Map's (article discloses this) |
| Stone et al. 2025, *Br J Anaesth* 135(1):121–133 | PASS | PASS — genetically identical mice, [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0007091225001667) ≥2 orders of magnitude emergence variability, stochastic model [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC12226763/) beats PK-PD; faithful; article correctly says it does not adjudicate classical vs quantum | Physicalist |
| Lewis et al. 2018, *eLife* 7:e33250 | PASS | PASS — transient sleep-like cortical state with K-complex-like responses pre-emergence; faithful | Physicalist |
| Xu et al. 2023, *PNAS* 120(19):e2216268120 | PASS | **PARTIAL FAIL** — real, but "cardiac arrest gamma surges" is imprecise. The human study analysed "four comatose dying patients before and after the withdrawal of ventilatory support. Two of the four patients exhibited a rapid and marked surge of gamma power" — global-hypoxia dying, not cardiac-arrest-with-recovery | **FAIL** — Borjigin/Mashour read it as brain-based; no survival or veridical-perception claim |
| Parnia et al. 2023 (AWARE-II), *Resuscitation* 191:109903 | PASS | **MATERIAL FAIL** — article says "~40% of cardiac arrest patients showing organised brain activity during CPR." Actual: of 567 in-hospital arrests only 53 (9.3%) survived, 28 were interviewed, 85 total had EEG; "∼40% of survivors reported a perception of consciousness without explicit recall, while ∼20% reported features consistent with a recalled experience of death… and ∼3% overt visual and auditory awareness." The "~40% organised brain activity" claim conflates a survivor self-report rate with an EEG finding | **FAIL** — Parnia's interpretation is contested but not dualist-interactionist |
| Craddock et al. 2015, *Curr Top Med Chem* 15(6):523–533 | PASS | PARTIAL — "dampen quantum oscillations in tryptophan… π-resonance energy transfer" faithful to the paper's *computational model* | **FAIL + internal inconsistency** — Craddock/Hameroff/Tuszynski Orch-OR; a *pre-decoherence-coherence* mechanism the Map's tenet page ranks *below* post-decoherence selection |
| Wiest 2025, *Neurosci Conscious* 2025(1):niaf011 | PASS | **PARTIAL FAIL** — "delayed luminescence experiments showing anaesthetics measurably alter quantum properties" overstates: niaf011 is a review whose author states "There are no new data associated with this article"; the empirical work (delayed luminescence; epothilone-B) is elsewhere and single-lab. Article's "contested but suggestive" is calibration-generous | **FAIL + internal inconsistency** — explicit Orch-OR advocacy, inconsistent with the corridor reading |
| Liem et al. 2004, *Anesthesiology* 101(2):279–283 | PASS | PASS — but note precise figure: desflurane requirement 6.2 vol% in redheads vs 5.2 vol% in dark-haired women (P=0.0004), a ~19% increase; 9/10 redheads carried MC1R mutations. Article's "approximately 20% more" is a fair round | Physicalist |
| Franks 2008, *Nat Rev Neurosci* 9(5):370–386 | PASS | PASS (background) | Physicalist — Franks' whole programme is *specific-receptor production* |

**Fabrication rate: zero detected.** **Author-stance failure rate: ~11 of 17 citations recruited toward an interface/dualist conclusion their authors explicitly do not hold.** This is the dominant and systematic pathology of the article.

### 2.2 THE CENTRAL QUESTION — Is the inference from anaesthetic pharmacology to an "interface" reading warranted?

**No.** The article's core structure is: distinct molecular agents (GABA-A positive allosteric modulators, NMDA antagonists, α2 agonists, halogenated ethers, xenon) disrupt distinct components of experience via distinct receptor targets → therefore consciousness has a "structured, multi-layered interface." This is a non-sequitur with respect to the dualism/physicalism contrast. A production/identity theorist predicts *exactly* the same facts: if conscious contents are realised by specific thalamocortical and cortico-cortical dynamics, then drugs acting on the receptors that shape those dynamics will produce content-specific deficits. Receptor specificity is evidence *for a structured neural substrate* — which every physicalist already asserts — not for a non-physical relatum connected via an interface.

The article's own **constrain-vs-establish gate** is the correct diagnostic, and the article fails it. The sentence "Specific receptor targets suggest consciousness depends on particular molecular systems — the kind of structured interface the Map's framework requires" conflates *the framework being consistent with* the data with *the data favouring* the framework over rivals. The verb "requires" does illegitimate work: production models require the identical structure.

The **radio/transmitter analogy** is implicitly load-bearing (filter theory = transmission model). Its classic weakness is untouched: a damaged radio producing distorted output is fully explained by its circuitry without positing a broadcast station; the inference to an external signal requires *independent* evidence of the station. The article's version does not escape this. It explicitly concedes, in §"What Anaesthesia Cannot Tell Us," that "anaesthetic evidence alone cannot distinguish the Map's interactionist interpretation from a sophisticated functionalist one," and defers the discriminating work to "convergence." That concession is correct and it guts the article's headline claim that anaesthetic pharmacology "maps the consciousness-brain interface with unexpected precision."

The three claimed filter-discriminating predictions — (i) graded not binary, (ii) consciousness persisting under disruption, (iii) enhanced experience when filtering loosens — are all accommodated by physicalist accounts without post-hoc strain: (i) graded PCI *is* the mainstream finding (Casali 2013, Sarasso 2015); (ii) "disconnected consciousness" is itself a physicalist construct (Sanders, Tononi, Laureys, Sleigh 2012, *Unresponsiveness ≠ unconsciousness*); (iii) the psychedelic entropy increase is a physicalist result (Carhart-Harris entropic-brain), and the article's own psychedelics cross-link concedes "production accounts accommodate it equally." No differential support survives.

### 2.3 Missed / under-engaged rivals

- **IIT + PCI:** The article *uses* PCI (Casali 2013, Sarasso 2015) but never engages IIT as the rival that most naturally owns these data. It asserts "ketamine poses a specific challenge to integrated information theory: PCI remains at waking levels yet consciousness is disconnected." This misfires — Sarasso/Casali present exactly high-PCI-under-ketamine as PCI *succeeding*: detecting *disconnected consciousness* in behaviourally unresponsive subjects (the paper's own bullet: "PCI may index the presence of disconnected consciousness during unresponsiveness"). The article inverts a confirmation of the IIT-derived measure into a challenge to it.
- **Global Neuronal Workspace / cognitive unbinding (Mashour, Hudetz):** Cited for reboot data but engaged only to be "reframed," never confronted as a rival explanation of the same evidence.
- **Predictive processing / active inference (Friston, Clark, Seth, Hohwy):** Entirely absent — the known site-wide blind spot recurs here. Anaesthesia has a substantial active-inference literature (e.g., Wehrman/Sanders 2023 on ketamine reducing but not eliminating predictive-coding responses as a mechanism of sensory disconnection) that would directly contest both the "temporal binding interface component" and the "content without access" readings. Not cited.
- **Cogitate adversarial collaboration (Cogitate Consortium 2025, *Nature* 642(8066):133–142):** Absent. Directly relevant: with n=256 across fMRI/MEG/iEEG it found "a lack of sustained synchronization within the posterior cortex contradicts [IIT]… GNWT is challenged by the general lack of ignition at stimulus offset and limited representation of certain conscious dimensions in the prefrontal cortex." Its omission lets the article deploy PCI (IIT) and workspace (GNW) machinery as if both were settled tools when both were substantially challenged in 2025.
- **Connected/disconnected + isolated-forearm-technique literature (Sanders 2017; Lennertz 2023; Ni Mhuircheartaigh/Warnaby):** The article gives the IFT figure but does not engage its *deflationary* reading — connected consciousness under anaesthesia is the mainstream physicalist interpretation of residual cortical processing, not interface evidence.
- **The deflationary core point** — that reversible abolition is *precisely* what a physicalist expects — is stated once and then not allowed to constrain the Dualism tenet-alignment subsection, which reasserts "a system losing generative capacity should not produce more consciousness."

### 2.4 Orch-OR usage vs the Map's own minimal quantum interface

The Minimal Quantum Interaction subsection leans on Craddock et al. 2015 and Wiest 2025 — both **Orch-OR / pre-decoherence-coherence** proposals. The Map's own tenets page explicitly ranks post-decoherence selection *ahead of* Orch-OR and states the coherence-dependent proposals "stand or fall with that more demanding assumption" of coherence surviving at neural timescales. The article therefore recruits, as quantum support, exactly the mechanism family the Map treats as its weakest fallback — and does so without noting the inconsistency. The empirical standing is weaker still: Wiest 2025 is a no-new-data review; the delayed-luminescence and epothilone-B (microtubule-stabiliser-delays-anaesthesia) results are single-lab and unreplicated; the decoherence-timescale dispute (Tegmark 2000 vs Hagan et al. 2002, spanning ~10⁻¹³–10⁻⁴ s) remains unresolved by the literature's own admission. Presenting this cluster as "measurably alter quantum properties of microtubules — contested but suggestive" is generous. Crucially, an Orch-OR anaesthetic-binding mechanism, if real, *would be empirically detectable* (altered potency via microtubule binding) — which contradicts apex #34's insistence that the endorsed corridor interface is Born-preserving and *empirically indistinguishable from chance*. The article never reconciles the detectable mechanism it cites with the undetectable one it is committed to. [Oxford Academic](https://academic.oup.com/nc/article-pdf/2025/1/niaf011/63128065/niaf011.pdf)

### 2.5 Tenet-protective bracketing pathologies

- **Confession-without-correction (dominant):** Precise disclosures — "the convergence is *suggestive* rather than *vindicating*"; "anaesthetic evidence alone cannot adjudicate against the functionalist reading"; "does not by itself support the quantum reading"; "the bootstrapping problem remains open" — are stated and then not permitted to downgrade the surrounding verdicts or the headline thesis. They function as inoculation, not remediation.
- **Constitutional-attractor effect:** The "four separable interface components" (phenomenal presence / content-without-access / temporal binding / memory encoding) are presented as discovered, but track the Map's pre-existing filter architecture; the sources taxonomise the same data differently (Bonhomme's three components; Sanders' connected/disconnected binary).
- **Epistemic-to-metaphysical slide:** "the neural side prepares a channel that consciousness then re-enters" and "the workspace must be inhabited, not merely activated" convert an epistemic finding (frontoparietal dynamics normalise before behavioural recovery — Mashour 2021) into a metaphysical claim (a channel awaiting a non-physical occupant).
- **Evidential-independence failure:** The closing "convergence" argument counts anaesthesia, contemplative pathology, and clinical phenomenology as distinct evidence streams, though the article's own linked "epistemology of convergence arguments" concedes these form a "compound signature" that "earns the architecture, not its dualist significance." Good self-awareness — again not allowed to bind the verdict.
- **Calibration asymmetry:** Congenial single-lab quantum results (Wiest, Craddock) are "suggestive"; the hostile deflationary reading is granted then walled off in a section titled to sound like a limitation rather than a defeater.

### 2.6 Stale references / literature currency

Metadata is current through 2025 (Stone 2025, Onoda 2025, Breyton 2025, Van Maldegem 2025 all present and correctly cited). Substantive gaps: **Cogitate 2025** (absent, materially relevant to the PCI/workspace deployment); the **NAP5 audit** distinction is not drawn — Pandit et al. 2014 report accidental awareness with explicit recall at "∼1:19 600 anaesthetics (95% CI 1:16 700–23 450)" by spontaneous report, rising to ∼1:8,200 with neuromuscular block, versus the ~0.1–0.2% the article quotes (which is the structured-interview figure, Sebel et al. 2004, 0.13%); the **microtubule/quantum-anaesthesia critiques** (standing decoherence objections; Wiest 2025 being no-new-data) are underweighted.

### 2.7 Quantum-interface load-bearing & Born-rule consistency

The article is *mostly* disciplined: it explicitly quarantines the quantum reading of stochastic emergence ("equally consistent with classical neuronal noise… does not by itself support the quantum reading") and routes it to /topics/stochastic-emergence-as-quantum-interface-evidence/. That is the correct move and matches apex #34's register. The lapse is confined to the Minimal Quantum Interaction subsection, where the Craddock/Wiest claims (a) assert a detectable mechanism at odds with the Born-preserving corridor and (b) inherit no acknowledgement of the **bias-without-deviation dilemma** that apex #34 makes binding on any causal claim about consciousness "re-entering" or "reorganising around" channels. No overt **Stapp inversion** occurs (the article does not attribute outcome-biasing to Stapp), but neither does it inherit the corridor discipline that would forbid its Bidirectional-tenet causal language from reading more confidently than "available, not actual."

### 2.8 Integration & positions-register consistency

Integration is dense and largely accurate (filter-theory, degrees-of-consciousness, anesthesia-void, stochastic-emergence, the memory-hierarchy discriminating-test article all correctly linked, with the compound-signature discount honestly imported). The registered position (Consciousness-scope register: fragmentation cases "read as interface disruption rather than division of consciousness") matches the article's stance; no drift. But there is a **within-article registry-vs-body calibration mismatch**: the Dualism and Bidirectional subsections, and the citation-abstract/title, assert discriminating support that §"What Anaesthesia Cannot Tell Us" concedes the evidence does not provide — **structural over-service of Tenets 1/2/3**.

### 2.9 Calibration against apex benchmarks #33 and #34

Apex #34 (born-preserving-causal-efficacy) and #33 (cross-modal-capability-division) hold rivals at full strength, name the discriminator they owe, and refuse to treat a shared explanandum as confirmation (#33 explicitly "forbids treating a shared explanandum as proof of the interface"). This article reads several calibration-generations behind that standard: it treats shared explananda (PCI gradation, disconnection, active emergence) as interface confirmation, engages no rival at full strength, and specifies no discriminator it does not immediately defer to another article. It should be brought up to the #33/#34 rival-holding discipline before it is treated as settled.

## 3. BOTTOM-LINE VERDICT

**REVISE-HARD**, with two sections **DEMOTED-TO-COHERENCE-ONLY**. The article is not deletable — its empirical scaffolding is sound, its integration is strong, and much of its self-critical apparatus is genuinely good. But as it stands it systematically overclaims: its title/abstract ("maps the consciousness-brain interface with unexpected precision") and its Dualism/MQI subsections assert discriminating support that the body elsewhere concedes it does not have. The two sections that must be demoted to coherence-only:

- (a) the death/cardiac-arrest "strongest discriminating evidence" passage — Parnia is materially misread, Xu is overstated, and terminal lucidity is anecdotal and does no discriminating work;
- (b) the Minimal Quantum Interaction subsection — Orch-OR co-optation plus internal inconsistency with the Map's own corridor ordering.

## 4. ARTICLE-SPECIFIC FIXES (keyed to named slugs)

1. **/topics/anaesthesia-and-the-consciousness-interface/ — retitle and re-scope the thesis.** Replace "maps the consciousness-brain interface with unexpected precision" (abstract, description, lead) with a constrain-level claim: "anaesthetic pharmacology constrains, but does not discriminate between, production and interface readings of the consciousness–brain relation." Move the §"What Anaesthesia Cannot Tell Us" concession into the lead so it binds the article rather than inoculating it.
2. **Fix the Parnia (AWARE-II) misattribution.** "~40% of cardiac arrest patients showing organised brain activity during CPR" → "of 567 in-hospital arrests, 53 (9.3%) survived and 28 were interviewed; ∼40% of survivors reported a perception of consciousness without explicit recall, ∼20% features of a recalled experience of death, ∼3% overt awareness; near-normal EEG emerged in a minority up to 35–60 min into CPR." Cross-check the identical figure at /topics/consciousness-under-extreme-metabolic-constraint/.
3. **Correct the Xu 2023 gloss.** State it analysed four comatose dying patients after withdrawal of ventilatory support (2/4 gamma surge) — global-hypoxia dying, not cardiac-arrest-with-recovery.
4. **Repair the IIT inversion.** Rewrite "ketamine poses a specific challenge to integrated information theory": Sarasso/Casali present high-PCI-under-ketamine as PCI *detecting disconnected consciousness* — an IIT-derived success. Engage IIT as the rival owner of the PCI data rather than a foil.
5. **Cut or quarantine the Minimal Quantum Interaction subsection.** Reduce to one sentence deferring to /topics/quantum-biology-and-neural-consciousness/ and /topics/stochastic-emergence-as-quantum-interface-evidence/; flag that Craddock 2015 and Wiest 2025 are Orch-OR (pre-decoherence-coherence) proposals the Map's own /tenets/ page ranks below its corridor reading, that Wiest 2025 states "no new data," and that an Orch-OR binding mechanism is detectable and thus at odds with the Born-preserving corridor of apex #34.
6. **Add the missing rivals.** Engage predictive processing / active inference (Wehrman/Sanders 2023 on ketamine and predictive coding; Seth; Hohwy) and cite Cogitate 2025 (*Nature* 642:133–142) wherever PCI/workspace machinery is deployed — here and at /topics/the-interface-problem/.
7. **Distinguish the awareness incidences.** Separate the NAP5 spontaneous-report audit figure (Pandit 2014, ∼1:19,600; ∼1:8,200 with neuromuscular block) from the structured-interview figure the article uses (Sebel 2004, 0.13%); and update the IFT figure — currently "roughly 5%" — with Sanders 2017 (4.6% overall) and Lennertz 2023 (11% in young adults; 13% in females, 6% in males).
8. **Bind the Dualism/Bidirectional subsections to apex #34.** State the bias-without-deviation dilemma wherever the article claims consciousness "re-enters," "inhabits," or "reorganises around" channels, so the causal language reads no more confidently than "available, not actual."

## 5. SITE-WIDE METHODOLOGY IMPROVEMENTS

- **The author-stance / co-optation firewall is not working on congenial empirical clusters.** The rival-or-support field check already logged in evidential-status-discipline (for Friston, Tononi, Dehaene, Mashour, Seth, Barrett, Craig, Graziano) should be made **blocking** for any article whose evidential spine is physicalist consciousness-science: no article ships where a majority of empirical citations are authors whose framework the article contradicts, without an explicit shared-explanandum discount recorded at each use. This article, with ~11/17 stance-failures, would not pass such a gate.
- **Confession-without-correction needs a mechanical linter.** When an article contains a hedge of the form "X is suggestive rather than vindicating / cannot adjudicate / does not by itself support," a review pass must verify that no downstream tenet-alignment subsection, abstract, or title reasserts the stronger claim. This is the registry-vs-body calibration diff turned *inward within a single article* — the exact failure mode present here.
- **Deploy the #33/#34 rival-holding standard as a gate, not an aspiration.** Articles citing shared explananda (PCI, disconnection, active emergence) should be required to name the discriminator and either supply it or demote to constrain-level *in the same sentence* — the discipline apex #33 already enforces with "forbids treating a shared explanandum as proof of the interface."
- **The predictive-processing blind spot is now corpus-wide and repeat-flagged.** Active inference is the single most-cited contemporary framework in exactly the domains the Map treats (anaesthesia, psychedelics, attention, binding, the interface problem). Its systematic absence is a structural gap outer reviews keep noting; a standing task to seed a dedicated predictive-processing rival treatment and back-link it from the interface cluster is overdue.
- **Tag quantum-mechanism citations by sub-reading.** Any citation to Orch-OR / Craddock / Hameroff / Wiest / Fisher-Posner should carry an automatic note that it is a pre-decoherence-coherence proposal ranked below post-decoherence selection, preventing the corpus from recruiting its own dispreferred fallback as affirmative support — as this article currently does.
