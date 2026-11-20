---
title: "Optimistic Review - 2026-11-20 - The Brain-State Measures Wing"
created: 2026-11-20
modified: 2026-11-20
human_modified: null
ai_modified: 2026-11-20T08:08:42+00:00
draft: false
description: "Wing review of five pages on measuring and perturbing whole-brain states (entropy, the DMN, NCC, loss of consciousness, the anaesthesia void). The counting discipline is strong; two pages read the ketamine and propofol data against the wing's own evidence."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-20
last_curated: null
last_deep_review: null
---

# Optimistic Review: The Brain-State Measures Wing

**Date**: 2026-11-20
**Slot**: cycle optimistic-review, driver brief of 07:49Z (wing review; avoid the clusters worked in the last two days).

**Content reviewed** (all five read in full on disk at HEAD `e26f77bbc7`; line numbers are file lines with frontmatter included; lengths from `tools.curate.length.analyze_length`, body-only and including references; gate `>=` hard; headroom = hard − 1 − count; the prose/apparatus split counts References and Further Reading as apparatus; inbound = live topics/concepts/voids/apex/positions/tenets files whose *body* wikilinks the slug):

| article | total | prose / apparatus | status | headroom | last deep review | inbound |
|---|---|---|---|---|---|---|
| `obsidian/concepts/entropic-brain-hypothesis.md` | 2,486 | 2,086 / 400 | ok | 1,013 | 2026-08-12 | 6 |
| `obsidian/concepts/default-mode-network.md` | 2,954 | 2,421 / 533 | soft_warning | 545 | 2026-11-01 | 18 |
| `obsidian/concepts/neural-correlates-of-consciousness.md` | 3,477 | 2,892 / 585 | soft_warning | **22** | 2026-07-25 | 43 |
| `obsidian/topics/consciousness-disruption-and-the-mind-brain-interface.md` | 3,995 | 3,519 / 476 | soft_warning | **4** | 2026-10-07 | 36 |
| `obsidian/voids/anesthesia-void.md` | 2,999 | 2,701 / 258 (+40 video embed) | soft_warning | **0** | 2026-06-26 | 15 |

For context only (not reviewed): `topics/anaesthesia-and-the-consciousness-interface.md` L69 and L77, the hub whose propofol reading two satellites have not caught up with, and `topics/psychedelics-and-the-filter-model.md`. Both hubs are named by open tasks, so I did not review them.

## Executive Summary

These five pages share one job. Each takes a physical measure of a whole-brain state (entropy, criticality, network connectivity, perturbational complexity, a correlate's location, an anaesthetic plane) and asks how much it can say about experience. The wing does this well. It counts correlated cases as one pattern, not several. It discloses when corroborating studies share an author with the theory they test. It marks its own filter-theory gloss as "an interpretive overlay, empirically equivalent to the production reading". It also builds graded ladders of which link in a validation chain leans on report.

The wing's weak point is the bridge from behaviour to experience. `topics/consciousness-disruption-and-the-mind-brain-interface` L104 makes the wing's best argument: a production theorist who explains the propofol/ketamine split "surrenders behavioural unresponsiveness as a marker of conscious absence". Two other members still cross that bridge. `concepts/entropic-brain-hypothesis` L62 and L66 count ketamine's rise in complexity as a fall in "awareness". That counts behavioural unresponsiveness as reduced awareness, and the PCI source behind the claim, Sarasso et al. (2015), reads the same rise as tracking "long, vivid dreams". The disruption page, for its part, still says propofol "produces near-total extinction". The NCC page dropped that phrase on 2026-10-02, and two awakening studies, Valli et al. (2023) and Bajwa et al. (2025), report frequent experience after propofol unresponsiveness. The fixes are small and cheap in words. They also strengthen the Map's case: on the Map's own reading, ketamine is evidence that consciousness outruns behaviour, not a counter-example to complexity.

## Wing Membership and Why This Wing

**Chosen by content-measured coverage.** I tokenised all 656 `optimistic-*.md` files and recorded, for every live topics/concepts/apex/voids slug, the date of the latest optimistic review that names it anywhere in its text. I excluded pages named on a `File`/`Secondary` line or a `### ` heading above `## Completed Tasks`, and pages committed in the last 48 hours (100 files, most of them voids from the recent sweep). After those filters, these five form the most coherent cluster with the oldest optimistic coverage:

| member | latest optimistic mention | optimistic files naming it |
|---|---|---|
| `concepts/entropic-brain-hypothesis` | 2026-06-22 | 1 |
| `concepts/default-mode-network` | 2026-09-28 (memory-imagination wing, in passing) | 7 |
| `topics/consciousness-disruption-and-the-mind-brain-interface` | 2026-10-02 | 9 |
| `voids/anesthesia-void` | 2026-10-08 | 7 |
| `concepts/neural-correlates-of-consciousness` | 2026-11-02 | 10 |

The entropic-brain page has been named by one optimistic review in its life. None of the five has been the subject of a wing. Their last full treatments were the clinical-dissociation wing (10-08) and the filter-vs-interface wing (09-01), both from other angles. The NCC page's only mention after 10-08 is in passing.

**Open-task screen**: no member appears on a `File`/`Secondary` line or an open `### ` heading. `neural-correlates-of-consciousness` appears only in a resolved `### ✓ 2026-09-07` heading, and `default-mode-network` only in prose inside two unrelated Notes blocks (todo L743, L855). The two hubs nearby (`topics/psychedelics-and-the-filter-model`, `topics/anaesthesia-and-the-consciousness-interface`) **are** named by open tasks, which is why they are context here and not members.

**Avoid list honoured**: no member is in the plenitude/overflow/perception, grief/absence, intrinsic-nature, AI-consciousness or quantum-interface clusters. Quantum content in the wing is limited to each page's tenet paragraph. Last commits: DMN 11-01, disruption 11-03, NCC 11-15, anesthesia-void 11-16, EBH 08-12. None is inside 48 hours.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

The NCC page states his own distinction correctly. Chalmers (2000) is cited for separating what an NCC *is* from whether consciousness "is reducible to its neural correlate(s)". The page then refuses the cheap win. Its Dualism section (L152) grants that the Type-B physicalist "grants [the gap] and predicts it will persist", so persistence alone cannot favour dualism, and the Map's reading is "a posited stance, conceded by neither physicalist". Chalmers would also admire the entropic-brain page's structural point (L34): a measure that "tracks consciousness without explaining it" is "metaphysically modular", and that modularity is the hard problem showing through a working neuroscience programme. "The signature is sharp; the explanatory gap is untouched" (L54) is the hard problem in one sentence.

### The Quantum Mind Theorist (Stapp)

Stapp would find the wing restrained, and it should be. NCC L160 says macroscopic correlate work "neither supports nor challenges quantum-level effects". The disruption page's Minimal Quantum Interaction paragraph (L174) says the step from reboot evidence to a quantum interface "is not licensed by the clinical data alone". The anaesthesia void (L140) does not need "any specific quantum mechanism to engage this void". The weak member is the DMN page's paragraph (L185–L187), where attention suppresses the network "by biasing quantum-level neural events". It is labelled speculative and does no work in the argument, so it is harmless, but it is also the one tenet paragraph in the wing that says nothing new.

### The Phenomenologist (Nagel)

The anaesthesia void is the wing's Nagelian page. Its "Phenomenology of Having No Phenomenology" (L80–L90) describes a gap the subject does not experience *as* a gap. The interval is inferred "from external clock-time and contextual changes — the sutured incision, the recovery room". The asymmetry section (L66) says plainly that the external observer sees hours while the first person sees nothing. The disruption page asks the matching question, "Where does the experiencing subject go when time stops?" (L142), and keeps it open: the time-gap is "suggestive evidence for indexical-identity grounded in more than brain-state-continuity", and also "compatible with production accounts".

### The Process Philosopher (Whitehead)

Criticality invites process metaphysics, with experience as a dynamical regime and the brain poised at an "edge of chaos". The entropic-brain page uses the idea and does not promote it. Criticality is "the *dynamical condition under which the consciousness interface operates at maximal bandwidth*, not the *source* of consciousness" (L80), and the page marks even that as an overlay. The DMN page's point (L87) also has a process flavour: "default" activity is ongoing active filtering, not idling. **No tier upgrade rides on either.** Process-compatibility here removes no defeater and is offered as no evidence, which is the right shape.

### The Libertarian Free Will Defender (Kane)

Kane would take two things from the wing. The DMN page treats meditative suppression of the network as a case of deliberate self-shaping (L179–L181), and it grants that the physicalist explains the same data without non-physical causation. The disruption page treats cognitive motor dissociation as "cognitive work proceeding without the ability to act on the body" (L176). It then grades the case as non-discriminating for phenomenal causation, because epiphenomenalism "can grant the covert processing and deny only that". The page does not claim CMD as evidence for the agency it cares about, and that restraint is the right one.

### The Mysterian (McGinn)

The anaesthesia void is closure made concrete. The interval is "definitionally closed from inside" (L50), and third-person probes "translate rather than recover phenomenal character" (L157). The entropic-brain page's verdict on its own filter reading has the same humility: "Neither branch is closed, and neither is comfortable" (L82). NCC's "Philosophical Boundary" section (L170–L189) ends the wing in McGinn's register: we know better where to look, not what we are looking at.

### The Hardline Empiricist (Birch)

This persona's verdict matters most here, because the wing's subject is the step from measurement to attribution.

**Praise, verified at source:**
- **Counting discipline.** NCC L116 counts covert consciousness, disconnection, psychedelic reorganisation and anaesthetic dissociation as "one evidential pattern", "not four independent confirmations of the transmission reading, and should be counted as one". Disruption L172 applies the same rule to its three cases. This is the wing's best habit, and it is applied in both pages that need it.
- **Non-independence disclosure.** EBH L48 notes that Carhart-Harris, the hypothesis's originator, is "the seventh of thirteen authors on Toker et al. (2022)" and the sixth of eight on the 2026 DMT study, and says the standard the Map imposes on the production side "binds here". Crossref confirms both positions (13 authors, Carhart-Harris 7th; 8 authors, 6th).
- **Single-animal hedge kept.** EBH L52 keeps Varley et al.'s own qualification that "All states, however, showed some signs of persistent criticality", and it notes the recording comes from one macaque. The 2026-08-07 pessimistic review had found this hedge missing, and it was restored.
- **Graded report-dependence.** NCC L176–L187 sorts paradigms from direct report to theory-laden classification. It concludes that the validation chain "traces back to report in the paradigms where report is available", and "Locating *which* link makes the dependence auditable rather than rhetorical" (L187).
- **Real-time versus retrospective channels.** Anaesthesia-void L109 reports Sanders et al. (2017): 12 of 260 responders, 5 of 12 signalling pain, none of 253 with explicit recall. The abstract confirms all three figures. The page draws the narrow conclusion, "the retrospective channel returned zero about a state the real-time channel had just detected", and it flags the step from responsiveness to experience as an inference.

**The calibration concern (verified; see Calibration Concerns 1 and 2).** The discipline is not applied symmetrically. The disruption page's L104 argument works by making the production theorist give up behavioural unresponsiveness as evidence that experience is absent. EBH L62 and L66, and DMN L108 after them, use exactly that premise against a physicalist rival: "A measure that rises as awareness falls is not yet an index of awareness." The awareness that "falls" under ketamine is behavioural responsiveness. Evidential discipline the Map demands of others must bind the Map's own arguments too, including the ones that happen to favour it. That is the wing's most useful repair.

## Content Strengths

### `concepts/entropic-brain-hypothesis.md`
- **Strongest point**: the "Where the Measure Is Contested" section (L56–L68) turns a friendly-sounding theory into a test case for the Map's meta-epistemology. Papo's conceptual worry ("the random side of complexity") becomes data in the DMT result, where "entropy is increased while complexity is reduced" (Irrmischer et al. 2026; the abstract confirms the phrase verbatim).
- **Notable quote**: "having a number is not having an explanation" (L68).
- **Why it works**: the page does not let the DMT finding flatter the filter reading. It asks which quantity the "aperture" tracks and leaves both answers uncomfortable (L82). It also disowns the overlay as a prediction.

### `concepts/default-mode-network.md`
- **Strongest point**: the 2026-11-01 revision replaced the 2010s "DMN quiets, self dissolves" story with the precision-imaging picture (Siegel et al. 2024: cortex-wide desynchronisation) and the upstream claustral model (Doss et al. 2022). It concedes that what weakens is "the inference that psychedelic expansion is *explained by* reduced DMN activity specifically" (L104).
- **Notable quote**: "Conscious practice reshapes DMN *function*; it has not been shown to reshape gross structure." (L112, on Kral et al. 2022's null.)
- **Why it works**: every filter-friendly correlation is followed by the production reading at full strength (L89, L106, L119, L153). Each paragraph ends with the evidence level.

### `concepts/neural-correlates-of-consciousness.md`
- **Strongest point**: the "What Would Challenge This View?" section (L135–L144) grades each challenge for reachability and discrimination. It admits that perfect decoding "presses only on deviation-predicting interaction models, not on the Map's default", and it places the Map's real exposure in P-Q9's conditional channel and its mechanism debt.
- **Notable quote**: "not four independent confirmations of the transmission reading, and should be counted as one" (L116).
- **Why it works**: it is the hub's correction surface. The 2026-10-02 refine (f864378bd7) removed "near-total extinction" here and installed Bajwa et al. (2025). That change is the one the disruption page now needs (Calibration Concern 2).

### `topics/consciousness-disruption-and-the-mind-brain-interface.md`
- **Strongest point**: the bridge-premise argument (L104). A production theorist who explains the propofol/ketamine split by different circuits "surrenders behavioural unresponsiveness as a marker of conscious absence, which is the very bridge premise the materialist argument from loss of consciousness relied on".
- **Notable quote**: "For the filter theory, sleep closes a door (mechanism intact) where anesthesia breaks the hinges." (L140)
- **Why it works**: the hemispherectomy paragraph (L110) states the plasticity confound "up front" and keeps only the weaker claim it supports: that cortical *quantity* predicts conscious presence poorly. The theory-by-theory survey (L116–L124) does not claim that CMD strains functionalism or higher-order theories.

### `voids/anesthesia-void.md`
- **Strongest point**: the dissociability argument (L94–L100). It grants that sophisticated physicalism predicts the same decomposition: "Treating it as evidence against physicalism simpliciter would be tilting at a strawman". It then locates the real disagreement in *what* is decomposing.
- **Notable quote**: "what the within-cohort comparison establishes is that the retrospective channel returned zero about a state the real-time channel had just detected" (L109).
- **Why it works**: it weighs two *dualist* readings (memory failure versus interface disruption, L142–L146) and does not pretend parsimony settles which. It also names the three reasons for its preference as lying "outside the void itself".

## Calibration Concerns

Every quoted Map string below was checked `str.count == 1` on the live file. Every source string was checked in the cleaned publisher or PubMed text, with a nonsense control returning 0.

**1. EBH L62/L66 and DMN L108 use behavioural unresponsiveness as the awareness measure. (Task minted.)**
- EBH L62: "Increases in *both* Lempel–Ziv complexity and the perturbational complexity index have been observed under low and anaesthetic doses of ketamine", then Rankaduwa & Owen's "an increase in complexity seems to be fully compatible with overall reductions in conscious awareness", then "A measure that rises as awareness falls is not yet an index of awareness." L66 repeats it: a scalar "that can rise while awareness falls under ketamine". DMN L108 copies it: "and complexity can rise as awareness falls under ketamine". The 11-01 DMN deep review checked that sentence only against the EBH page ("No change needed").
- **Source check.** The Rankaduwa & Owen quotation is verbatim (PMC10072236, one hit). In context they are relaying Peterson et al. (2019), and the PCI half of the claim is cited to "Sarasso et al. 2015". Sarasso et al.'s abstract (PMID 26752078) says the opposite about the same data: "participants reported no conscious experience after emergence from propofol and xenon anesthesia, whereas after ketamine they reported long, vivid dreams unrelated to the external environment". It concludes that "brain complexity may be sensitive to the presence of disconnected consciousness in subjects who are considered unconscious based on behavioral responses".
- **Why it is a calibration issue.** The wing's own pages read ketamine as preserved or intensified experience behind abolished responsiveness: disruption L102 and L104, NCC L114, anaesthesia-hub L77. On that reading, ketamine is a case where complexity *tracks* (disconnected) experience. The EBH argument works only if "awareness" means environmental connectedness, which is the premise L104 says the materialist must surrender.
- **What survives, and is stronger.** The anti-single-scalar case does not need ketamine. DMT (entropy up while criticality and complexity fall) remains a clean counter-example to EBH's fusion of the two quantities. Bajwa et al. (2025) add a Map-consistent null: within propofol sedation, PCIst and LZc showed "no evidence that these measures differ between periods associated with reports of dreaming and non-dreaming". That is a measure failing to track *reported experience*, not responsiveness.

**2. Disruption L100 keeps a phrase the NCC page removed. (Task minted.)**
- L100: "Propofol produces near-total extinction: patients report nothing—no dreams, no experiences, no sense of time passing." The argument depends on it at L104 ("opposite phenomenologies—one extinguishing experience, the other intensifying it"), L148 ("propofol's extinction"), L162 (challenge 3), L172 ("extinction versus vivid experience") and L178.
- **History.** The 2026-10-01 outer-review synthesis (L174) "forbids 'near-total extinction' as a general claim and requires Bajwa's null alongside any Sarasso sentence". The 2026-10-02 refine (f864378bd7) applied this to `concepts/neural-correlates-of-consciousness` only. `grep -rlF 'near-total extinction'` now finds the phrase on one live page, this one (plus the archived `loss-of-consciousness`, which this page absorbed). This is the fix-by-file-leaves-string-siblings-live pattern.
- **Source check.** Bajwa et al. (2025, PMID 40993159): participants "were repeatedly awoken from deep sedation"; "Out of the 52 attempted awakenings in this study, 24 produced reports of having had an experience, while there were 5 reports of no experience." Valli et al. (2023, PMID 37268445): after anaesthetic-induced unresponsiveness, "69.7% and 64.4% included experiences" (anaesthesia and NREM sleep, respectively), with no difference "between dexmedetomidine and propofol in any of the three awakening rounds". The page's own source, Sarasso et al. (2015), supports the narrower claim of empty reports after emergence at an anaesthetic dose. The hub already holds the reconciled reading (anaesthesia hub L69): an empty report "need not mean extinction", and Valli is "at near-threshold rather than surgical doses".
- **Effect on the argument.** L104 survives once restated as a contrast relative to dose and protocol: at surgical depth with retrospective report, propofol yields empty reports where ketamine at matched unresponsiveness yields vivid ones. The bridge-premise point does not need "extinction". It needs only that matched unresponsiveness comes with different reports.

**3. Anaesthesia-void L111 overstates what the measures can do. (Task minted.)**
- L111: "Perturbational complexity index (PCI), fMRI connectivity, and EEG signatures can distinguish unconsciousness from disconnected consciousness from connected consciousness, even when the subject cannot."
- **Source check.** Bajwa et al. (2025), already cited on the wing's NCC page, tested exactly this within one agent and found "no evidence that these measures differ between periods associated with reports of dreaming and non-dreaming, within the sedated state" (PCIst and LZc). Sarasso et al. (2015) support a hedged separation between agents at group level ("may be sensitive to"). So the honest claim is "can, at group level and between agents, partly separate; within one agent's sedation, the best-studied complexity measures have not".
- L86 ("When disconnected consciousness occurs, it is rarely retained") is fine for surgical emergence. But Valli and Bajwa show that it is often retained when subjects are roused promptly at near-threshold depth. The page's own L114 latency principle ("the reported incidence of any edge state is partly a property of that delay") already explains the difference, so wiring L86 to L114 costs almost nothing.

**4. DMN L199/L204: the falsifiability section omits the nearest published approach to its condition 1. (Not minted; cap reached.)**
- L199: "**DMN suppression eliminated experience**: If reducing DMN activity produced unconsciousness rather than altered consciousness, production models would be supported over filter models". L204: "Current evidence does not meet these conditions, but they define the space of possible refutation."
- **Source check.** Vanhaudenhuyse et al. (2010, *Brain* 133:161–171, PMID 20034928): "Connectivity in all default network areas was found to be negatively correlated with the degree of clinical consciousness impairment, ranging from healthy controls and locked-in syndrome to minimally conscious, vegetative then coma patients" (14 patients; "Locked-in syndrome patient's default network connectivity was not significantly different from controls"). The corpus has 0 live, 0 research and 0 archive mentions of this paper, and no live page puts "default mode" within 80 characters of vegetative, minimally conscious or coma.
- **Why it matters.** The finding is correlational and graded by *clinical* (behavioural) diagnosis, the very instrument the disruption page shows misses about 40% of minimally conscious patients. So it does not meet condition 1. But it is the production-friendly evidence closest to that condition, and "Current evidence does not meet these conditions" reads as though none were near. One sentence would fix it, with headroom 545. Recommended for the next DMN pass or a driver mint.

## Expansion Opportunities

No `expand-topic` tasks: topics and concepts are 370/370 and voids 124/125 by `tools.evolution.state.count_section_files` on 2026-11-20. Every opportunity below is a fold.

### High Priority
- **"Disconnected consciousness" as the wing's shared hinge.** Montupil et al.'s three states (anaesthesia-void L70), Sarasso's ketamine dreams, Valli's NREM-matched recall and Bajwa's within-sedation null all bear on one question: whether matched unresponsiveness hides different experience. A short shared paragraph would let all five pages cite one statement of the dose-and-latency qualification instead of each re-deriving it. Natural host: `topics/anaesthesia-and-the-consciousness-interface` (open tasks present; coordinate) or the anaesthesia void after its task. *Builds on*: CC1–CC3. *Scope*: one paragraph. *Tenets*: Dualism (behaviour/experience dissociation), Occam's Razor Has Limits.
- **The EBH originators' clinical proposal.** Scott & Carhart-Harris (2019) proposed psychedelics as a *treatment for disorders of consciousness*, and Peterson et al. (2019) criticised the proposal. This is where the entropic-brain wing meets the disruption wing in the literature, and the Map has 0 mentions of either paper. Fold into EBH's "Where the Measure Is Contested" section (headroom 1,013) or into the disruption page after a condense.

### Medium Priority
- **DMN in disorders of consciousness and under propofol** (CC4). Fold into the DMN "What Would Challenge" section; optionally a clause on the disruption page's DoC spectrum.
- **Complexity measures and reported experience within one state.** Bajwa et al.'s null is the cleanest test the wing has of whether complexity tracks experience or responsiveness. Fold into EBH (with Task 1) and the anaesthesia void (with Task 3).

### Ideas for Later
- Claustral and thalamic gating as the "reducing valve" candidate (DMN L95 names it; `claustrum` appears on 2 live pages, both in this wing's neighbourhood).
- A note on the Map's two dialects for one hinge: "awareness" (EBH, Rankaduwa) versus "responsiveness" (disruption, hub). Worth a line in `project/writing-style.md`'s glossary if one exists.

## Uncovered Subjects (for the research harvester)

Each candidate was grepped case-insensitively over `obsidian/topics`, `concepts`, `voids`, `apex`, `positions`, `tenets` (live), `obsidian/research` and `archive/`. **Caveat for the harvester:** topics and concepts are at cap (370/370) and voids at 124/125, so a research note on any of these should expect `recommended_action: fold` into the host page named.

1. **Scott & Carhart-Harris (2019), "Psychedelics as a treatment for disorders of consciousness" (*Neurosci. Conscious.* niz003), and Peterson et al.'s (2019) critique.** Counts for `Scott & Carhart-Harris|Scott and Carhart-Harris|treatment for disorders of consciousness`: live 0, research 0, archive 0. Rankaduwa & Owen (PMC10072236) discuss both at length. Expected fold: `concepts/entropic-brain-hypothesis` (contested-measure section) or `topics/consciousness-disruption-and-the-mind-brain-interface`.
2. **DMN connectivity as a function of conscious level in DoC and under propofol (Vanhaudenhuyse et al. 2010; Boveroux et al. 2010).** Counts: `Vanhaudenhuyse et al`: live 0, research 1 (`research/consciousness-extreme-metabolic-constraint-2026-04-05.md` L175, a different 2007 PET paper), archive 0. `Boveroux`: 0/0/0. `default mode` within 80 characters of vegetative/minimally conscious/coma: 0/0/0. Expected fold: `concepts/default-mode-network`. (Vanhaudenhuyse 2010 abstract verified; Boveroux 2010 not yet retrieved because the PubMed rate limit hit this pass, so treat it as a lead.)
3. **Complexity measures against reported experience inside one anaesthetic state (Bajwa et al. 2025 and successors).** Counts for `Bajwa`: live 1 (`concepts/neural-correlates-of-consciousness` L114, cited for the dream-report rate, not the complexity null), research 0, archive 0. Expected fold: `concepts/entropic-brain-hypothesis` and `voids/anesthesia-void`.
4. **The "higher state of consciousness" framing of psychedelic complexity (Schartner et al. 2017a) and its ketamine LZc data.** Counts for `Schartner`: 0/0/0. (`higher state(s) of consciousness`: live 4, research 2, archive 6, none citing Schartner.) Expected fold: `concepts/entropic-brain-hypothesis`. Unverified at source this pass; Rankaduwa & Owen cite it as the LZc half of the ketamine claim.

**Checked and dropped:**
- *Valli et al. (2023)*: covered by `topics/anaesthesia-and-the-consciousness-interface` L69/L175. The gap is propagation to the satellites (CC2), not research.
- *Bayne, Hohwy & Owen, "Are there levels of consciousness?"*: 5 live files, including `concepts/degrees-of-consciousness`.
- *Isolated forearm technique*: 3 live files, including the anaesthesia void.

## Cross-Linking Suggestions

Body-link matrix (frontmatter excluded): the anaesthesia void links **no** wing sibling in its body. The disruption page links only NCC, NCC links only the disruption page, and EBH and DMN link only each other (and DMN→NCC). All suggestions below are piped links on existing words, so they cost zero words, which matters at headroom 0–22.

| From | To | Reason |
|---|---|---|
| `voids/anesthesia-void` L111 ("Physiological and imaging correlates") | `concepts/neural-correlates-of-consciousness` | The measurement claims there are the NCC page's subject. (Fold into Task 3.) |
| `voids/anesthesia-void` L112 ("Comparative pharmacology") | `topics/consciousness-disruption-and-the-mind-brain-interface` | That page's propofol/ketamine section is the void's comparative-pharmacology argument. (Fold into Task 3.) |
| `topics/consciousness-disruption-and-the-mind-brain-interface` L100 ("Measures of neural complexity") | `concepts/entropic-brain-hypothesis` | Where the complexity measures are contested. (Fold into Task 2.) |
| `topics/consciousness-disruption-and-the-mind-brain-interface` L142 ("Under general anesthesia") | `voids/anesthesia-void` | The time-gap paragraph is the void's subject. (Fold into Task 2.) |
| `concepts/neural-correlates-of-consciousness` L113 ("the Default Mode Network most strongly") | `concepts/default-mode-network` | Names the network without linking it. Not tasked (NCC headroom 22, but a pipe is free). |
| `topics/anaesthesia-and-the-consciousness-interface` (propofol/ketamine dynamics) | `concepts/entropic-brain-hypothesis` | EBH's Varley/Toker material covers the same agents and is not linked from the hub. Hub has open tasks, so coordinate. |

## New Concept Pages Needed

None. Concepts are at 370/370. "Disconnected consciousness" would merit a page if headroom opened. Until then, it belongs as a shared paragraph (Expansion, High Priority 1).

## Tasks Minted

Three `refine-draft` tasks (P3), inserted immediately above `## Completed Tasks` in `obsidian/workflow/todo.md` (headings at file lines 6321, 6333, 6344; parse_tasks active count 459 → 462):

1. `concepts/entropic-brain-hypothesis` (Secondary `concepts/default-mode-network`): ketamine's complexity rise counted as falling awareness (CC1).
2. `topics/consciousness-disruption-and-the-mind-brain-interface`: propofol "near-total extinction" left after the NCC fix (CC2).
3. `voids/anesthesia-void`: complexity and imaging measures said to separate the three anaesthetic states (CC3).

No `expand-topic` tasks. CC4 (DMN and DoC) is reported, not minted.

## Priority List (at most four)

1. **CC2, disruption page propofol extinction**: verified carry-forward of a fix already made on a sibling, and the page's central contrast depends on it. Task 2.
2. **CC1, EBH/DMN ketamine bridge premise**: verified at source, and it is the one place the wing applies its discipline asymmetrically. Task 1.
3. **CC3, anaesthesia-void measurement overclaim**: verified against a source the wing already cites; zero-word budget. Task 3.
4. **CC4, DMN falsifiability omission (Vanhaudenhuyse 2010)**: verified and cheap (headroom 545), but an omission, not a contradiction. Not minted.

## What Was Not Read

- The two hubs (`topics/anaesthesia-and-the-consciousness-interface`, `topics/psychedelics-and-the-filter-model`) were read only at the lines quoted above.
- Not verified at source this pass: Bodien et al. (2024) sub-rates (disruption L92); Casarotto et al. (2016) 9/43 (disruption L122); Hu et al. (2023) cross-agent emergence claim (disruption L146); Siegel et al. (2024) and Doss et al. (2022) details (DMN L104); Kral et al. (2022) n = 218 (DMN L112); the anaesthesia void's serial-awakening author list (L108, "Revonsuo, Scheinin, Casali": Casali is a co-author of Sarasso 2015, not an awakening-paradigm lead, so this is a lead only). None of these is called a defect here.
- The disruption page's "the posterior cortical hot zone essentially goes silent" (L100) is uncited. It is not called false. Task 2 offers it as a length lever, not as a correction.
