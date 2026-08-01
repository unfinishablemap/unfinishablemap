---
ai_contribution: 100
ai_modified: 2026-07-30 12:36:02+00:00
ai_system: claude-opus-5
concepts: []
created: 2026-07-30
date: '2026-07-30'
draft: false
lastmod: 2026-07-30 12:36:02+00:00
related_articles: []
title: Pessimistic Review - 2026-07-30 - Fox et al. 2012 Neural-Prediction Over-Enrollment
---

# Pessimistic Review — Fox et al. (2012) and the Neurophenomenology Citation Surface

**Date**: 2026-07-30
**Primary content reviewed**: `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md` (37 references, `ai_modified: 2026-07-13`, 17 days converged, no open task)
**Secondary loci examined**: `obsidian/concepts/phenomenological-evidence.md`, `obsidian/apex/testing-the-map-from-inside.md`, `obsidian/apex/contemplative-path.md`, `obsidian/topics/contemplative-practice-as-philosophical-evidence.md`, `obsidian/concepts/default-mode-network.md`

## Executive Summary

The lens applied was not "find a logical gap" but "find a claim that rests on something that will not bear it." Six citations in the target article were verified at their publishers. Two are exactly correct. Four are enrolled for propositions their sources do not contain, and one of those four has propagated to **six loci across four files**, two of them apex flagships, one of them a wikilink alias.

The headline finding: **Fox et al. (2012) collected no neuroimaging from its participants at all** — its "objective measures" were two-point-discrimination thresholds and primary-somatosensory-cortex representation areas *taken from previously published literature as group-average norms*. The corpus cites it, at six places, for the proposition that trained observers' reports "predict neural signatures" that untrained reports do not. That proposition carries the Map's rebuttal to Dennett's heterophenomenology in three separate articles, and it is not a finding of the study.

The second finding is a propagation failure rather than a citation failure: the Kral et al. (2022) null result on structural brain change was installed in the target article's empirical paragraph and its lead, but never reached the `description:` frontmatter, the section topic sentence, or the tenet-relation claim — so the article's *nav surface* and its *statement of what the evidence establishes for Bidirectional Interaction* both still assert structural neuroplasticity that the same article retracts 120 lines earlier.

## Critical Issues

### Issue 1: Fox et al. (2012) enrolled for a neural-prediction finding it does not contain

- **Files**: `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md`; `obsidian/concepts/phenomenological-evidence.md`; `obsidian/apex/testing-the-map-from-inside.md`; `obsidian/apex/contemplative-path.md`; `obsidian/topics/contemplative-practice-as-philosophical-evidence.md`
- **Severity**: High
- **Verified at**: [PMC3458044](https://pmc.ncbi.nlm.nih.gov/articles/PMC3458044/) (Fox, Zakarauskas, Dixon, Ellamil, Thompson & Christoff, 2012, *PLoS ONE* 7(9): e45370)

What the study actually did, quoted from its Methods:

> "Average values for two-point discrimination (2PD) thresholds for each of 20 body regions, as reported in previous research, were used"

> "Average values for total area in primary somatosensory cortex (S1) for 20 body regions were likewise gleaned from prior published research."

So the design is: participants rated their own tactile sensitivity at 20 body regions during a body-scanning meditation; those subjective rankings were correlated against **published normative constants** for 2PD threshold and S1 representation area. No fMRI, EEG or MEG was recorded from any participant. The comparison is cross-sectional (expert vs novice), not longitudinal. What the paper reports about novices is:

> "though not all expert meditators demonstrated high introspective accuracy, *no* novice meditators did"

**The over-enrolled loci** (all strings grep-verified on disk at the line numbers given):

| File | Line | Text |
|---|---|---|
| [concepts/neurophenomenology-and-contemplative-neuroscience.md](/concepts/neurophenomenology-and-contemplative-neuroscience/) | 153 | "But Fox et al. found trained observers predict neural signatures far better than untrained ones." |
| [concepts/neurophenomenology-and-contemplative-neuroscience.md](/concepts/neurophenomenology-and-contemplative-neuroscience/) | 132 | "**Predictive power**: First-person reports from trained observers predict neural signatures that untrained reports do not." |
| [concepts/neurophenomenology-and-contemplative-neuroscience.md](/concepts/neurophenomenology-and-contemplative-neuroscience/) | 51 | "these phenomenological categories predict neural signatures" |
| [concepts/phenomenological-evidence.md](/concepts/phenomenological-evidence/) | 115 | "Trained meditators' reports of **specific attentional states** predict neural signatures that untrained reports do not (Fox et al., 2012)." |
| [apex/testing-the-map-from-inside.md](/apex/testing-the-map-from-inside/) | 182 | "The empirical case is strong: first-person reports from trained observers predict neural signatures that untrained reports do not" |
| [apex/testing-the-map-from-inside.md](/apex/testing-the-map-from-inside/) | 201 | wikilink **alias**: `[[neurophenomenology-and-contemplative-neuroscience\|trained contemplatives predict neural signatures]]` |
| [apex/contemplative-path.md](/apex/contemplative-path/) | 137 | "Trained meditators provide more reliable, precise reports that predict neural signatures untrained reports miss." |
| [topics/contemplative-practice-as-philosophical-evidence.md](/topics/contemplative-practice-as-philosophical-evidence/) | 139 | "If training merely deepened bias, trained reports should diverge from neural data; that convergence tightens instead" |

Three observations that make this worse than a loose paraphrase:

1. **`phenomenological-evidence.md:115` is the furthest from the source.** Fox et al. had nothing to do with attentional states; it measured tactile acuity across body regions. The sentence adds a specificity the study cannot supply, then draws an evidential conclusion from it ("The phenomenology earns evidential status by enabling successful predictions").
2. **`testing-the-map-from-inside.md` states the calibrated version and the over-claim four lines apart.** Line 178 is exemplary — "This is one study, not definitive proof" — and line 182 then asserts "The empirical case is strong" for a claim the study does not make. A reader who stops at 182 gets the opposite of what 178 conceded.
3. **Line 201's over-claim lives in a wikilink alias**, i.e. in the link text that search and LLM retrieval surface first. No prose lens reads aliases.

The claim is also load-bearing in a fourth place that no prose lens would connect to Fox: `neurophenomenology-and-contemplative-neuroscience.md:193` reasons that "if phenomenal consciousness reduced to neural processes, first-person training would not improve correlation with third-person measurements." That inference needs a *longitudinal training* design. Fox et al. is cross-sectional, so self-selection is not excluded — a point the corpus already makes correctly elsewhere (see below).

- **Recommendation**: Re-calibrate, do not delete. Fox et al. is a real, relevant, correctly-dated study, and the corpus **already contains two exemplary formulations of it** that can simply be copied. No invention required:

  - `obsidian/concepts/buddhism-and-dualism.md:54` — "experienced meditators give more accurate introspective reports of tactile sensitivity during body-scanning meditation, measured against objective thresholds, than novices (Fox et al. 2012). This is narrower than a claim that meditators introspect consciousness as such more accurately, but it counts against the view that introspective skill is untrainable."
  - `obsidian/concepts/contemplative-epistemology.md:60` — "…their ability to match subjective reports of tactile sensitivity to objective psychophysical measures… This result is promising but indirect: introspective accuracy on a sensory-discriminative task is not identical to reporting on the structure of phenomenal consciousness. The inferential gap must be acknowledged."

  Both are already right. The defect is confined to the "predict neural signatures" formulation. Note that where the corpus *does* want a genuine reports-track-measured-neural-signatures claim, `topics/phenomenal-authority-and-first-person-evidence.md:104` sources it to **Lutz et al. 2004**, which did record EEG — that is the correct citation for that proposition, and the anti-heterophenomenology passages should be repointed there (with Lutz's own caveats, see Issue 7) rather than to Fox.

### Issue 2: the Kral (2022) correction never reached the nav surface or the tenet-relation claim

- **File**: `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md`
- **Severity**: High
- **Verified at**: [Science Advances 8(20) eabk3316](https://www.science.org/doi/10.1126/sciadv.abk3316) — Kral et al. (2022), "Absence of structural brain changes from mindfulness-based stress reduction: Two combined randomized controlled trials." n = 218 meditation-naïve participants (waitlist 70 / 8-week MBSR 75 / validated active control 73); no evidence of neuroplastic change against either control, whole-brain or ROI. **The article's rendering of Kral at line 75 is accurate.** The defect is that the correction stopped there.

Three uncorrected assertions survive:

- **`description:` frontmatter (line 3)** — "Meditation training produces neuroplastic changes **demonstrating** bidirectional interaction between consciousness and brain." The body says "suggestive evidence" (line 49) and "The findings do not settle the metaphysical debate alone" (line 145). The nav surface asserts what the body concedes it cannot.
- **Line 73** — "Long-term meditators show altered brain **structure** and function:" — the section's topic sentence, two lines above "**Structural changes (under scrutiny)**… Kral et al. (2022)… found no structural brain changes."
- **Line 195, Relation to Site Perspective → Bidirectional Interaction** — "Contemplative neuroscience provides paradigm empirical evidence. Conscious practice causally reshapes brain **structure** and function." This is the worst of the three: it is the article's formal statement of what the evidence establishes for a foundational commitment, and it asserts structural reshaping as *paradigm* evidence after the empirical section retracted it. Line 75 even concedes the fallback: "Cross-sectional differences in long-term practitioners may reflect pre-existing traits rather than practice-induced changes."

For contrast, the corpus has otherwise absorbed Kral well — it is cited in eleven live content files including [concepts/neuroplasticity.md](/concepts/neuroplasticity/), [concepts/mental-effort.md](/concepts/mental-effort/), [concepts/stapp-quantum-mind.md](/concepts/stapp-quantum-mind/) and [topics/clinical-neuroplasticity-evidence-for-bidirectional-causation.md](/topics/clinical-neuroplasticity-evidence-for-bidirectional-causation/). This article is the laggard, and it is the one that *introduces* the topic.

- **Recommendation**: rewrite the `description:` to the body's own register (functional changes; suggestive rather than demonstrative); narrow line 73 to "altered brain function, and — more contestably — structure"; and restate line 195 in terms of **functional** reorganisation, which is what survives Kral and is sufficient for the tenet.

- **Secondary locus, not minted**: `obsidian/concepts/default-mode-network.md:110` — "long-term practitioners show structural changes in brain regions overlapping the DMN (Fox et al., 2014)." That citation is a real morphometric meta-analysis (Fox, Nijeboer, Dixon et al., 2014, *Neuroscience & Biobehavioral Reviews* 43, 48-73) so it is not a misattribution, but the sentence asserts structural change flatly and that file never mentions Kral. Left for the operator.

### Issue 3: `[^dhond]` misattributes a real paper to a non-author and names a repository as the journal

- **File**: `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md` (reference 5, footnote `[^dhond]`, used at line 99)
- **Severity**: Medium-High
- **On disk**: "Dhond, R.P. et al. (2023). Functional Connectivity of Prefrontal Cortex in Various Meditation Techniques. *PMC*."
- **Verified at** [PMC10026337](https://pmc.ncbi.nlm.nih.gov/articles/PMC10026337/), which is the URL the footnote itself points to. The actual article is:

  > Rathore, M., Verma, M., Nirwan, M., Trivedi, S., & Pai, V. "Functional Connectivity of Prefrontal Cortex in Various Meditation Techniques – A Mini-Review." *International Journal of Yoga*, 15(3), 187–194.

  **Dhond is not an author.** "*PMC*" is PubMed Central, a repository, not a journal. And the piece is a **mini-review**, cited at line 99 for a primary empirical claim: "Focused attention meditation implicates default-mode, control (dlPFC, lateral parietal), and salience (ACC, insula) networks.[^dhond]"

- **Recommendation**: correct authors, journal, volume and pages; drop the subtitle-free title; and either re-frame line 99 as a review's summary or repoint it to one of the primary studies the review covers. Matches the known "wrong first author grafted onto a real paper" pattern.

### Issue 4: `[^pernet]` cited for a duration claim the meta-analysis does not make

- **File**: `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md`, line 79
- **Severity**: Medium
- **On disk**: "However, 8-week MBSR may produce only functional changes; structural changes require sustained practice over months to years.[^pernet]"
- **Verified at** [PubMed 33624219](https://pubmed.ncbi.nlm.nih.gov/33624219/) — Pernet, Belov, Delorme & Zammit (2021), *Brain Imaging and Behavior* 15(5), 2720–2730. The abstract reports 25 MRI studies; an ALE analysis (n = 16) finding the right anterior ventral insula as the only region with a consistent effect, at "Cohen's d ~ 0.8"; and the conclusion that "mindfulness meditation practice does induce grey matter changes but also that improvements in methodology are needed," naming "selection, information, attrition and confirmation biases, in addition to weak statistical power."

  There is **no dose-response or duration claim anywhere in it**. Note that the *first* enrollment of this same source, at line 75 ("meta-analysis of 25 MRI studies, Cohen's d ~ 0.8", right anterior ventral insula), is verbatim accurate. Only the second enrollment fails — and it is the sentence doing the most work, because it is the article's residual defence against Kral. It also sits in tension with line 75's own concession that long-term-practitioner differences may be pre-existing traits.

- **Recommendation**: either source the "functional-before-structural" timeline to something that actually argues it, or drop the claim and let Kral stand unhedged. An unsourced hedge is preferable to a misattributed one.

### Issue 5: `[^davidson]` is a university press release standing in for the peer-reviewed paper, with the wrong first author

- **File**: `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md` (reference 2, footnote `[^davidson]`, used at line 109)
- **Severity**: Medium
- **On disk**: "Davidson, R.J. et al. (2008). Study shows compassion meditation changes the brain. *University of Wisconsin-Madison News*." — footnote URL `news.wisc.edu`.
- **Verified**: the study that release reports is Lutz, A., Brefczynski-Lewis, J., Johnstone, T., & Davidson, R.J. (2008), "Regulation of the Neural Circuitry of Emotion by Compassion Meditation: Effects of Meditative Expertise," [*PLoS ONE* 3(3): e1897](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0001897). First author **Lutz**, not Davidson. The paper is an fMRI expert-vs-novice study of response to emotional sounds.

  Line 109 reads: "Compassion meditation appears to modulate emotional response networks—functional activation changes that correlate with prosocial behaviour.[^davidson]" The prosocial-behaviour half of that is Weng et al. (2013), which the article cites separately and correctly at line 79. So a press release is carrying a compound claim, half of which belongs to a different paper.

- **Recommendation**: replace the news item with the *PLoS ONE* citation and split the compound claim across its two actual sources.

### Issue 6: a single-subject case study cited for plural meditators, per-state signatures, and a result not in it

- **File**: `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md`, line 115
- **Severity**: Medium
- **On disk**: "Research on advanced meditators (23,000+ hours) accessing jhana states reveals distinct neural signatures for each of the eight traditional states—increased global connectivity, altered hierarchical organisation, and increased brain entropy.[^demir]" followed by "The phenomenological categories carve neural reality at its joints."
- **Verified at** [PubMed 40215476](https://pubmed.ncbi.nlm.nih.gov/40215476/). The full title is "Advanced concentrative absorption meditation reorganizes functional connectivity gradients of the brain: **7T MRI and phenomenology case study** of jhana meditation" — and the Map's reference list truncates the title precisely at the words that bound the claim. The abstract describes "an intensive case study." It reports a shift of gradients "toward a more globally integrated rather than segregated state" and "a separation between sensory-related and attention modulation-related regions." It does **not** report increased brain entropy, and does not report distinct signatures for each of the eight jhanas individually.

  So: "Research on advanced meditators" (plural) is n = 1; "distinct neural signatures for each of the eight traditional states" overstates the resolution; "increased brain entropy" is not in the paper; and "carve neural reality at its joints" is a strong generalisation from a single practitioner.

  The same plural-from-n=1 pattern recurs at line 119, "Advanced meditators can voluntarily enter cessation states." Laukkonen et al. (2023) is a single-practitioner EEG case study. Its *substance* as the article uses it is sound — the practitioner's brain "didn't turn off" and overall synchronisation was reduced, so line 121's "reorganised but not silent" is properly supported — but the generic plural implies a literature that does not yet exist. The Map's reference also drops the title's "of nirodha samāpatti".

- **Recommendation**: say "a 7T case study of one practitioner with ~23,000 hours" and restore the case-study wording to the reference; drop "increased brain entropy" unless it can be sourced to a different Sacchet-lab paper; soften "carve neural reality at its joints" to match n = 1.

### Issue 7: gamma figures are internally inconsistent and do not match the cited band

- **Files**: `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md` lines 85, 87, 197; `obsidian/apex/testing-the-map-from-inside.md` line 182
- **Severity**: Low-Medium
- **Verified at** [PMC526201](https://pmc.ncbi.nlm.nih.gov/articles/PMC526201/) — Lutz, Greischar, Rawlings, Ricard & Davidson (2004), *PNAS* 101(46). The authors define gamma as **25–42 Hz**: "the ratio of gamma-band activity (25-42 Hz) to slow oscillatory activity (4-13 Hz) is initially higher in the resting baseline before meditation for the practitioners than the controls over medial frontoparietal electrodes."

  On disk, line 85 attributes "gamma-band (30–70 Hz)" to `[^lutz]`. Line 87 then derives "Gamma cycles span 15–35 milliseconds" from that band. But line 197 — the sentence carrying the quantum-Zeno temporal-grain argument — says "(~25–35ms gamma cycles)". Two different figures for the same quantity, and neither follows from Lutz's actual 25–42 Hz (which gives ~24–40 ms). The 15–35 ms figure has also propagated to `apex/testing-the-map-from-inside.md:182`.

  Also worth noting for calibration: Lutz et al. 2004 is **eight** practitioners (mean age 49 ± 15) against **ten** student controls (mean age 21 ± 1.5). Line 85 says meditators show "dramatically increased" gamma with no note of the sample size or the 28-year age gap. The article's own line 75 applies exactly these caveats — small samples, absent active controls — to the structural literature. Applying them where they undercut a claim the Map does not need, and omitting them where they would undercut one it does, is a calibration asymmetry a hostile reviewer will find immediately.

  The article's "even at baseline rest" claim (line 85) *is* supported by Lutz — that part is correct.

- **Recommendation**: pick one band, state it as the article's own convention rather than Lutz's, make the cycle figures agree at both loci and in the apex file, and add the sample-size/age-confound note at line 85.

### Issue 8: cessation is credited to filter theory without the parallel accommodation move

- **File**: `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md`, line 95
- **Severity**: Medium (Altered-State Symmetry, Audit Two)
- Supportive-cluster gate passes: jhana states (line 115), contemplative cessation / *nirodha samapatti* (line 119), mystical/unitive framing via `[[witness-consciousness]]`. Disruptive-cluster engagement passes minimally — line 119 names "sleep or anaesthesia", but only as a phenomenological contrast for cessation, not as evidence the framing must accommodate.
- Symmetry-acknowledgment **fails**. Line 95 reads: "The cessation finding (discussed in the advanced practice section) favours filter theory—consciousness continues during neural reorganisation in ways that don't map straightforwardly to production models." No marker names the accommodation available to the production theorist, who can read cessation as the neural substrate of report-generation going offline while other activity persists — structurally the same move the filter reading makes. The article states the production/filter alternatives fairly at line 95's opening, then awards the case to filter without earning it.
- **Recommendation**: install the parallel-accommodation sentence, inheriting the framing from `obsidian/concepts/altered-states-of-consciousness.md` and `obsidian/topics/anaesthesia-and-the-consciousness-interface.md`, which perform this accommodation for the corpus.

## Critiques by Philosopher

### The Hard-Nosed Physicalist (Dennett)

The most damaging critique available, and it is nearly self-inflicted. The article's designated refutation of heterophenomenology (line 153) is a claim about Fox et al. that Fox et al. does not make. Dennett's reply writes itself: *you told your readers my position "fails empirically," and the empirical failure you cited was eight body-scanning meditators matching published two-point-discrimination norms better than novices did.* Heterophenomenology has no difficulty with that result — expertise at reporting tactile gradients is exactly the kind of report-generating competence heterophenomenology models. The argument does not need the over-claim: the regress point at line 151 is independent and survives intact. Removing the over-claim strengthens the section by removing the part a hostile reader would target first.

### The Eliminative Materialist (Churchland)

"Structural convergence across Buddhist, Hindu, Christian, Sufi, and Daoist practices" (line 131) is offered as evidence of shared phenomenal structure. Churchland's reply: convergence on *vocabulary* — self-dissolution, contentless awareness — across traditions that have been in contact for centuries is what you would expect from a shared folk-psychological framework being taught, not from independent detection. The article's own falsifier list (line 178) makes convergence-failure a test, but never says what independence condition the traditions must satisfy for convergence to count. `topics/contemplative-practice-as-philosophical-evidence.md:181` acknowledges the transmission worry; this article does not.

### The Quantum Skeptic (Tegmark)

Line 197 argues that "the temporal microstructure (~25–35ms gamma cycles) operates at scales where Zeno dynamics could accumulate effects." Tegmark's objection is that the relevant comparison is not gamma cycles against millisecond-scale anything — it is the decoherence time of the candidate quantum degree of freedom, which is orders of magnitude shorter than either figure. Matching a *neural* timescale to a *neural* timescale establishes nothing about whether Zeno dynamics are available. The argument as written compares the wrong two numbers, and the fact that the article states the gamma figure two different ways (Issue 7) suggests the numbers are decorative rather than doing work.

### The Empiricist (Popper's Ghost)

The falsifier list at lines 175–188 is the article's strongest structural feature and deserves saying so. But item 3, "**Neural prediction fails**: trained observers no better than untrained," is not currently a live test, because the confirming result the article claims for it (Issue 1) was never run. The list also closes with "None demonstrated" (line 189) — a claim that item 3 has been *tested and passed*. It has not been tested. That is the sharpest single sentence a Popperian could aim at this article: you listed a falsifier, then reported it survived a test that does not exist.

### The Buddhist Philosopher (Nagarjuna)

Line 167 handles the *anatman* tension unusually honestly — conceding that the phenomenological data are "equally compatible with process philosophy, neutral monism, or Buddhist anti-substantialism." Nagarjuna would press one step further: the article's whole evidential structure assumes a trained observer whose reports become *more accurate* with practice, i.e. a stable knower converging on a stable known. The Madhyamaka reading of *śamatha* is not improved detection but the progressive dismantling of the detector. If that is right, "introspective accuracy" is the wrong metric and its improvement is evidence about training, not about consciousness. The article never considers that its central instrument is framework-dependent.

### The Many-Worlds Defender (Deutsch)

Little purchase here; line 199 is a single sentence and does not overreach.

## Unsupported Claims

| Claim | Location | Needed support |
|---|---|---|
| "trained observers predict neural signatures far better than untrained ones" attributed to Fox et al. | `concepts/neurophenomenology-and-contemplative-neuroscience.md:153` | A study that measured neural signatures in the participants. Fox et al. did not. Repoint to Lutz et al. 2004 or re-calibrate. |
| "reports of specific attentional states predict neural signatures … (Fox et al., 2012)" | `concepts/phenomenological-evidence.md:115` | Same, plus Fox et al. did not study attentional states. |
| "first-person training would not improve correlation with third-person measurements" | `concepts/neurophenomenology-and-contemplative-neuroscience.md:193` | A longitudinal training design. Fox et al. is cross-sectional. |
| "Conscious practice causally reshapes brain structure and function" | `concepts/neurophenomenology-and-contemplative-neuroscience.md:195` | Contradicted by Kral et al. 2022 as cited at line 75 of the same article. |
| "structural changes require sustained practice over months to years" | `concepts/neurophenomenology-and-contemplative-neuroscience.md:79` | Pernet et al. 2021 makes no duration claim. |
| "increased brain entropy" in jhana states | `concepts/neurophenomenology-and-contemplative-neuroscience.md:115` | Not in Demir et al. 2025's abstract. |
| "distinct neural signatures for each of the eight traditional states" | `concepts/neurophenomenology-and-contemplative-neuroscience.md:115` | n = 1 case study; not per-state resolution. |

## Language Improvements

| Current | Issue | Suggested |
|---|---|---|
| "meditation research has empirically vindicated it" (line 49) | "vindicated" is stronger than the article's own hedges support | "meditation research has given it an empirical programme" |
| "produces neuroplastic changes demonstrating bidirectional interaction" (`description:`) | Nav surface over-claims against its own body | "produces measurable functional changes that bear on bidirectional interaction" |
| "The phenomenological categories carve neural reality at its joints" (line 115) | Metaphor asserting per-state resolution from n = 1 | "The phenomenological categories track measurable differences in this practitioner" |
| "dramatically increased gamma-band power" (line 85) | Intensifier with no sample-size or confound note | "markedly higher gamma-band power in eight long-term practitioners relative to ten younger controls" |
| "Heterophenomenology fails empirically" (line 153) | Header asserts a result the cited study cannot deliver | "Heterophenomenology and the training data" |
| "None demonstrated." (line 189) | Reports a passed test that was never run (falsifier 3) | Split: say which falsifiers have been tested and which remain open |

## Strengths (Brief)

Worth preserving through any revision:

- **The falsifier list (lines 175–188) is genuinely good** — eight specific, discriminating conditions including "zombie meditation" and externally-inducing meditation brain states. Most articles in this corpus do not reach this standard. Only its closing verdict needs work, not its content.
- **The Kral et al. (2022) paragraph at line 75 is model practice**: it names the better-powered null result, quantifies it, and diagnoses why the earlier positives may have been artefacts, including the trait-vs-training confound. The problem is that the article stops propagating it, not that it lacks the correction.
- **The *anatman* passage (line 167) concedes underdetermination explicitly** — the data are "equally compatible with process philosophy, neutral monism, or Buddhist anti-substantialism" — which is the register `evidential-status-discipline` asks for.
- **The process/content distinction against Nisbett and Wilson (line 125) is the right move**, correctly drawn, and independent of the Fox over-claim.
- **Two citations verified exactly correct**: Sandved-Smith et al. (2025), *Neuroscience of Consciousness* 2025(1), niaf016 — all five authors, journal, volume and article ID right; and Kral et al. (2022) as described above. The article's citation hygiene is not uniformly poor, which makes the four defective enrollments look like accretion from separate passes rather than a systemic problem.

## Considered and Rejected

- **Length.** `analyze_length` returns 3031 words, `soft_warning`, excess 531 (121% of the 2500 soft threshold). But `## Further Reading` + `## References` run **777 words**, leaving the authored argument at roughly **2254 words — comfortably under the soft threshold**. No length finding. This is exactly the false-over-length trap that citation-dense articles produce.
- **Sandved-Smith et al. (2025)** — verified in full; correct in every field. A prior pass flagged it as a dangling reference and the fix was clean.
- **Kral et al. (2022) as rendered at line 75** — verified accurate down to the participant count and the design. The correction itself is sound; only its propagation is incomplete.
- **Pernet et al. (2021) as rendered at line 75** — "meta-analysis of 25 MRI studies", "right anterior ventral insula", "Cohen's d ~ 0.8" all verbatim from the abstract. Only the *second* use of the citation (line 79) fails.
- **Laukkonen et al. (2023) on cessation** — the substantive claim ("Brain activity continues during cessation, reorganised but not silent", line 121) is supported: the practitioner's brain did not switch off and overall synchronisation dropped. Only the generic plural at line 119 is loose.
- **Weng et al. (2013), "~7 hours of compassion training (two weeks, 30 min daily)"** — arithmetic and description check out; left alone.
- **Lutz et al. 2004's "even at baseline rest"** — supported verbatim by the abstract. Only the band range and cycle figures are wrong.
- **`expand-topic` / `research-topic` ideas.** The Churchland objection above points at a real gap — the corpus has no article stating an *independence criterion* for cross-traditional convergence, which is what would make the convergence argument testable rather than suggestive. Out of contract to mint, and section caps leave three slots corpus-wide; recorded here for the operator. The existing [topics/epistemology-of-convergence-arguments.md](/topics/epistemology-of-convergence-arguments/) may already be the right home for it, in which case this is a refine, not an expand.
- **`obsidian/concepts/default-mode-network.md:110`** — real defect (flat structural claim post-Kral, file never mentions Kral) but I did not review that article, so no task minted. Noted in Issue 2.
- **`obsidian/apex/contemplative-path.md:137`** and **`obsidian/topics/contemplative-practice-as-philosophical-evidence.md:139`** — two further Fox over-enrollment loci. Not minted, to avoid a four-task defect-family cascade on one finding. Both are listed in the minted tasks' notes so whichever pass runs first can sweep them.

## Tasks Minted

Pileup checked for all five candidate paths against the `- **File**:` lines above `## Completed` in `obsidian/workflow/todo.md`: zero open tasks target *or mention* any of them.

1. **P1 refine-draft** — `obsidian/concepts/neurophenomenology-and-contemplative-neuroscience.md` (Issues 1–8, all loci local to this file)
2. **P2 refine-draft** — `obsidian/concepts/phenomenological-evidence.md` (Issue 1, line 115)
3. **P2 refine-draft** — `obsidian/apex/testing-the-map-from-inside.md` (Issue 1, lines 182 and 201 including the wikilink alias; line 178 is the in-file exemplar)