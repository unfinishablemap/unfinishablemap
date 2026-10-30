---
title: "Optimistic Review - 2026-10-30 - Clinical Insight Wing"
created: 2026-10-30
draft: false
ai_contribution: 100
ai_system: claude-opus-5-5
ai_modified: 2026-10-30T09:21:00+00:00
---

# Optimistic Review — Clinical Insight Wing

**Date**: 2026-10-30
**Wing**: five clinical pages on which a patient's report about their own experience goes wrong, or does not. Each page turns on **insight**, the patient's knowledge that an anomaly is subjective: Charles Bonnet syndrome (insight kept, hallucination recognised as unreal), depersonalisation (insight kept, the "as if"), Capgras and Cotard (insight lost, delusion), and Anton syndrome (the deficit itself denied). The question put to the wing: **does the Map use "insight" in one sense across these pages, and do the pages talk to each other where their cases meet?**

**Why this wing**: coverage was measured on review *content*. All 623 `optimistic-*.md` files were grepped for every live slug as a substring.

| article | optimistic reviews naming it (substring) | last optimistic treatment under its own heading |
|---|---|---|
| `concepts/depersonalisation-nosology` | **0** | none (created 2026-10-28) |
| `topics/anton-syndrome-and-the-sincere-report-of-seeing` | 1 | 2026-10-09 (first-person-certification wing) |
| `concepts/charles-bonnet-syndrome` | 2 | 2026-10-14 (three-creations wing); 09-18 only names the research note |
| `concepts/cotard-delusion` | 2 | 2026-10-01 / 09-30 |
| `topics/capgras-delusion-and-the-affective-recognition-channel` | 2 | **2026-08-02** (single-case-dissociation cluster); the 10-22 hit is a one-line classifier note |

No wing review has put these five side by side. The recent wings the brief excludes (luck, retrocausal, interactionist lineage, subject structure, self-knowledge, contemplative evidence) name none of them. All five were read in full on disk between 09:08 and 09:15Z.

**Content reviewed** (body-only `analyze_length`, measured 09:10Z; topics band 3000/4000/6000, concepts 2500/3500/5000, gate `>=`; headroom = hard − 1 − count; inbound = files under topics/concepts/voids/apex/positions/tenets whose *body* carries the slug as a wikilink):

| # | article | words | status | headroom to hard | last deep review | body inbound |
|---|---|---|---|---|---|---|
| 1 | `obsidian/concepts/depersonalisation-nosology.md` | 2514 | soft_warning | 985 | 2026-10-28 | 2 |
| 2 | `obsidian/topics/anton-syndrome-and-the-sincere-report-of-seeing.md` | 3562 | soft_warning | 437 | 2026-10-04 | 11 |
| 3 | `obsidian/concepts/charles-bonnet-syndrome.md` | 2689 | soft_warning | 810 | 2026-10-19 | 7 |
| 4 | `obsidian/concepts/cotard-delusion.md` | 3495 | soft_warning | **4** | 2026-10-01 | 15 |
| 5 | `obsidian/topics/capgras-delusion-and-the-affective-recognition-channel.md` | 2648 | ok | 1351 | 2026-09-10 | 5 |

Section counts from `count_section_files` at 09:10Z: **topics 367/370, concepts 370/370 (AT CAP), voids 113/125, positions 25/90.** Cotard's 4-word headroom means any change there must add no words.

Prior ledgers read before praising: the five deep reviews' Stability Notes (nosology 10-28: the refusal to adjudicate placements is deliberate; CBS 10-19: neutrality verdicts by design, "do not re-expand the compensation reading", "page has converged on structure"; Anton 10-04: "The A-vs-B underdetermination is the article's settled position", do not re-add "only" to the Swartz & Brust periods sentence; Cotard 10-01: do not re-flag under-claiming, Gerrans hedge deliberate; Capgras 09-10: Corlett quotations verified at full text, "must not be 'corrected'"), the nosology cross-review (10-28), and the 09-30 creation-wing ledger, which ruled Cotard's "at most suggestive" a ceiling and not an over-claim. That ruling is honoured below.

## The Wing's Question: One Word, Three Objects, Two Registers

**Verdict: the pages never contradict one another on insight, but "insight" covers three different objects and two different registers, and no page says so. One page (CBS L86) settles the register by assertion where its sources do not.** Here is how each page uses the word:

| page | what the patient has insight *into* | register the page uses | locus |
|---|---|---|---|
| nosology | that the change is subjective: ICD-10 criterion (c), "an acceptance that this is a subjective and spontaneous change ... (i.e. insight)" | **judged**: "acceptance", "reality testing remains intact", "the patient knows the change is subjective" | L35, L39, L45 |
| (hub context) depersonalisation / phenomenal-quality-void | the same. "I know it's real but it doesn't feel real" — "demonstrating that reality-feeling is independent of belief" | **judged**, set against a withdrawn feeling | hub L37; void L96 |
| CBS | that the images are unreal | **presented**: "Insight is a phenomenal fact: the hallucination presents as unreal while remaining vivid" | L32, L38, L62, L86 |
| Cotard | that the condition is "as if". Cotard is "the insight-lost complement" | **left open** between Billon (the pathology is in the experience, taken at face value) and the revised two-factor account (a second factor drops the "as if") | L52, L56 |
| Capgras | that the spouse is not an impostor | **judged**: Factor 2, "a reasoning pathology the Map takes no position on" | L69–71 |
| Anton | that one is blind (the deficit) | the page never uses the word; Levine: the absence "must be discovered by a process of self-observation and inference" | L60 |

The three objects are the *change* (depersonalisation), the *content* (CBS) and the *deficit* (Anton). They can come apart in a single patient, and the Map already holds the case that shows it. In Swartz and Brust's (1984) patient (Anton L70–72), blind from eye injury, the hallucinations' "unreality ... he recognized" (content-insight kept), yet he "believed that his vision had been restored" (deficit-insight lost). The page that would most gain from this case, CBS, has no link to Anton, and Anton has no link to CBS.

The two registers matter because they decide which side of the Capgras **scope rule** insight falls on. The Capgras page puts belief evaluation outside the Map's territory and keeps "only the anomalous experience". Cotard inherits that rule. If insight is *judged*, losing it is a Factor-2 event, and the Map rightly says nothing about it. If insight is *presented*, as CBS L86 says, then whether the "as if" survives is partly a fact about experience, and that is the Map's territory. Cotard L56 sees exactly this fork ("which differ over whether a second factor is needed to lose the 'as if'") and leaves it open. CBS L86 closes it for one syndrome without a source.

The Map's own pages also disagree on what a hallucination carries. `voids/perceptual-reality-monitoring-void` L64: "In hallucination, the signal is present without external cause; in derealization, external cause is present without the signal." On that general description, a CBS image carries the felt-real signal, and insight is a judgement *overriding* it, the mirror image of depersonalisation's belief standing against a withdrawn feeling. CBS L86 says the reverse for CBS. Both can be true only if CBS is the exception, a hallucination that comes without the signal. That may well be so, but no page argues it. (The 10-14 three-creations review proposed linking the void's L94 "Hallucination" to CBS as "the cleanest insight-preserved hallucination: felt-real signal absent". That pipe was never installed, and the claim inside it is the one at issue here.)

**The case that counts as Factor 1 alone is misreported.** Cotard L52 gives the two-factor prediction: "A patient with the first factor alone should report the *as-if* form ... with insight preserved, which is the clinical picture of depersonalisation." The only Factor-1-alone population the wing cites is Capgras's four non-delusional ventromedial-prefrontal (vmPFC) cases. Capgras L69 says these patients "report the felt strangeness of familiar faces without forming any delusion". Corlett 2019, the page's own source for those four cases (L79), describes them only by skin conductance: "their familiarity response is operationalized as their lack of a skin conductance response (SCR) to famous faces like Marilyn Monroe or Margaret Thatcher". The verbatim text of PMC6686846, fetched at about 09:16Z today, attributes no report or experience of strangeness to any of them. The "feel" wording appears only in Corlett's glosses of the *theory* ("so 'That doesn't feel like my wife'"). The page's own L79 already describes them correctly: "patients who lack the autonomic response to familiar faces but form no delusion". L69's wording traces to an uncited "e.g." in the research note (`research/capgras-delusion-and-the-affective-recognition-channel-2026-07-10` L91, "some with ventromedial damage who feel the strangeness but don't form the delusion"). Caveat: about 62% of the paper came back verbatim. The rest, including the reference list, was summarised, so the fork must check the PDF and Coltheart & Davies 2022 before rewriting. The defect carries forward into L63: the autonomic trace "is selectively absent in exactly the patients whose reports describe its felt absence". The vmPFC cases are absent-trace patients who, on the record the page cites, describe nothing. This is the wing's one verified source-fidelity defect, and Top-Priority item 1 below repairs it.

**Verdict vocabulary (observation only, nothing minted).** For the same tier, the five pages use five phrasings: CBS "neutral"; Anton "compatible with Tenet 1 and does not support it"; nosology "compatible with, not evidenced by"; Cotard "compatible with, at most suggestive for" (ruled a ceiling by the 09-30 ledger, honoured); Capgras "consistent with, not proof of" (L87). Capgras's version is the only one that measures against *proof*, a bar the evidential-status discipline does not use. Its body is fully neutral ("accounts for every datum here just as well"). Three deep reviews have passed the phrasing, the `anchoring_audit_exempt` comment at L9 quotes it, and changing it would churn more than it fixes, so it is recorded here and not minted.

## Top-Priority List (tasks are minted from this list only)

1. **Capgras L69 / L63 source fidelity, plus the L35 "mineness" collision.** Verified above. L35's scare-quoted "mineness" names the felt familiarity of *another person*. The Map's `[[mine-ness]]` is the for-me-ness of one's *own* experience, with depersonalisation as its central evidence (`mine-ness` itself never mentions Capgras or familiarity). The lead sentence is the page's most-read text, and it borrows a Map technical term for a different property. A length-neutral swap fixes it. → task (P2).
2. **CBS L86: rescope "Insight is a phenomenal fact" and connect CBS to the wing.** State that the sources record insight being *reported* and leave open whether unreality is *presented* or *inferred*. Name both Map framings (`perceptual-reality-monitoring-void` L64: felt-real signal present in hallucination; `phenomenal-quality-void` L96: reality-feeling independent of belief). Add the Swartz & Brust separation of content-insight from deficit-insight to "Why insight survives" (L62), and add Anton to Further Reading. Page evidence for the open question: L38 records criteria that "demanded only partial insight", and graded insight is what a judgement looks like. A lead from one standard web search this run: a review summary states that insight "may be delayed when the hallucination is context-appropriate". That is unpinned to a source, so the fork must locate and raw-verify it before citing. → task (P3).
3. **Anton: install CBS as the accurate-report control and the release contrast.** Zero-word pipe at L74 ("positive visual phenomena went with awareness of loss, not denial" is CBS's profile). Name CBS as a third neighbouring case at L101, as the true modal positive, a hallucination reported as a hallucination. Add one sentence after L72 saying the Swartz & Brust patient separates two insights that the CBS patient holds together. Add a Further Reading entry. → task (P3).
4. **Give `depersonalisation-nosology` reciprocal links at three zero-word spans.** It has 2 live inbound hosts. Cotard calls depersonalisation "the better-studied and non-delusional condition" (L56) without linking the page that documents the criterion that makes it non-delusional. `voids/necessary-opacity` L82 ("while retaining the insight that they are nonetheless themselves") and `topics/clinical-phenomenology-and-altered-experience` L107 ("Patients maintain insight") likewise. The 10-28 cross-review checked only the hub, `clinical-dissociation` and `mine-ness`. → task (P3).

## Executive Summary

These five pages are the Map's most consistently calibrated clinical set. Each states its Tenet-1 verdict at compatibility or below, names its physicalist rival and concedes the datum to it, and two of them correct the Map's own earlier readings: CBS retires "compensation", and the nosology page shows the affective rival to be "one party to this dispute rather than its settled outcome". The wing's unifying idea, insight, is used for three different objects and in two registers without being named as such, and CBS L86 asserts one register as fact. The wing also holds one verified source-fidelity defect (Capgras L69, the non-delusional vmPFC cases described as "report[ing] the felt strangeness"). CBS is an island: no link runs from it to the other four or from them to it.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)
Anton engages Chalmers on his own premise. It quotes his concession, "in cases of blindness denial, subjects believe that they are having visual experiences when they likely have none", and then tests whether his restriction holds up: "The restriction is principled only if impairment can be identified independently of the error itself, and mostly it can" (L84). Chalmers would welcome the global/modal typology (L94–101), which keeps his strongest claim, that experience exists at all, out of clinical reach: "the global-positive cell, where Layer 1 actually makes its claim, has no clinical instance". He would also welcome the page's refusal to let that warrant spread to artificial reporters: "Layer 1 ... lends those reports nothing" (L101).

### The Quantum Mind Theorist (Stapp)
Stapp's praise here is for restraint. Every page that addresses Tenet 2 says "nothing" (nosology L77, Cotard L74, Anton L123), and CBS withdraws the Map's earlier use of the syndrome for Tenet 3: "Release phenomena are, on their face, one-way: cortex to experience" (L82). A quantum-interface theorist does better when clinical cases are not asked to carry the physics. The wing leaves the interface question to the pages that can price it.

### The Phenomenologist (Nagel)
Capgras puts the felt side first and keeps it there: "They experience a person who looks exactly right and feels categorically wrong" (L49). Cotard's "reported from somewhere" (L64) is Nagel's point in clinical form: even the report that denies the reporter is made from a point of view. Nagel would praise CBS L86 most of all ("it does not derive what it is like for the same cortex's output to arrive once labelled and once unlabelled"). **That praise is held back here** (Calibration Concerns, below): it rests on a descriptive premise the page has not sourced.

### The Process Philosopher (Whitehead)
CBS's "Filter accounts are themselves release-shaped" (L80) avoids crude dualism by handing the *content* of experience to the brain on any metaphysics: "the brain supplies it on either metaphysics". Cotard's interface prediction that for-me-ness is "attenuated but never eliminated" (L66) is gradualist without collapsing into identity. **Tier check**: no page uses process-philosophical or tenet coherence to raise a case above compatibility. Cotard's "framework-internal weight" (L72) says outright that coherence is not evidence. Nothing to flag on this axis.

### The Libertarian Free Will Defender (Kane)
The wing treats the patient as a reasoner whose appraisals matter, without enlisting that for libertarian agency. The nosology page's Hunter model has the patient's own catastrophic appraisal keeping the condition going ("a vicious cycle", "safety behaviours"), and 29% remission under cognitive-behavioural therapy (L49–51). The Capgras page keeps belief evaluation as a distinct capacity (Factor 2) rather than folding it into the anomaly. Kane would note, and approve, that neither page draws a freedom conclusion from this.

### The Mysterian (McGinn)
Anton L78: "The decisive limit is methodological. Every measure in these studies is a report or a behaviour." CBS L66: "None of these gaps is a gap for dualism to fill." Cotard L68 offers its one asymmetry "as a prediction rather than evidence" and adds "Nothing on this page rests on the prediction." The humility runs both ways. The pages decline to fill clinical gaps with the soul, and equally decline to say that clinical science has closed the hard problem.

### The Hardline Empiricist (Birch)
This is the wing's strongest axis.
- **Self-correction against the Map's interest**: CBS retires the compensation reading by name and withdraws an argument for Tenet 3 (L68–74). The nosology page reports that ICD-10's "loss of emotions is the most frequent" "presses on the Map's reading rather than on the rival" (L69).
- **Counting convergence honestly**: nosology L55, "one research group occupies two of its corners", treats overlapping authors as non-independent evidence. Cotard's arithmetic (L42: immortality and existence-denial "must co-occur in at least 24 of the 100") turns base rates into a structural observation without overreaching.
- **Declining a tier upgrade when the structure invited one**: Cotard's "Nothing in Cotard discriminates; what it earns is framework-internal weight" (L72) is the named pattern, tenet-coherent and not evidence-elevating. Capgras's "Only Factor 1 is the Map's territory" (L71) stops the channel claim from spreading into belief.
- **Where Birch withholds praise**: Capgras L63's "exactly the patients" and L69's "report the felt strangeness" overstate the record (Top-Priority 1). CBS L86's premise is unsourced (below).

## Content Strengths

### concepts/depersonalisation-nosology
- **Strongest point**: it finds the one criterion that survives every placement and makes it the bridge to the hub: "One criterion survives every placement — retained insight" (L29). The page then turns that criterion against the dissociative placement, through Medford: "the hallmark of true dissociation is a lack of subjective awareness of change" (L51).
- **Notable quote**: "a chapter heading says where a syndrome is filed, not whether experience does causal work" (L75).
- **Why it works**: a nosology page is the easiest place to slip a classification into an ontology. L71 blocks that move in one sentence by separating "dissociative" as a filing kinship from "comes apart" as a within-experience claim.

### topics/anton-syndrome-and-the-sincere-report-of-seeing
- **Strongest point**: the case "fixes where authority attaches: to *seemings*, not to *reports*" (L44; restated at L111). This repair costs the Map something real ("a sincere first-person report does not certify that a seeming stands behind it") and keeps what matters.
- **Notable quote**: "Three things come apart in this one patient" (L72). This is the wing's most informative single case, and its significance reaches beyond the page.
- **Why it works**: the 2×2 global/modal × negative/positive table (L96–99) is a tool the rest of the corpus can reuse. Cotard already cites it ("what fails is the report, not the position").

### concepts/charles-bonnet-syndrome
- **Strongest point**: it names the equivocation between neuronal and phenomenal compensation (L72), "Neuronal compensation ... is affirmed by the literature ... Phenomenal compensation ... is denied by it", and retires only the second.
- **Notable quote**: "The content tracks cortical architecture rather than the missing scene; this is the single strongest datum against any gap-filling reading" (L40).
- **Why it works**: the page withdraws an argument the Map had been making and says so on the page, which is rare and worth more than another supporting case would be.

### concepts/cotard-delusion
- **Strongest point**: "That settles less than it appears to" (L66) follows the page's own best datum at once and gives it to the rival: "a running model that reports non-existence is still a running model".
- **Notable quote**: "Cotard is the case where the somewhere is what the report denies" (L34).
- **Why it works**: it runs the hardest test of a Map commitment, passes it, and then explains why passing earns nothing at the significance tier.

### topics/capgras-delusion-and-the-affective-recognition-channel
- **Strongest point**: the telephone datum. DS "called his parents impostors when looking at them but not when speaking to them on the telephone" (L59). "The modality-specificity is what makes the disconnection reading a finding rather than a story fitted after the fact."
- **Notable quote**: "His contrast runs between psychological and merely physical salience rather than between vision and hearing" (L81). This is the 09-10 repair, which made the page's engagement with Corlett faithful to Corlett's text.
- **Why it works**: it engages its sharpest critic on that critic's own terms and lets the verdict stay underdetermined.

## Calibration Concerns (not praise; refine-shaped, minted)

1. **Nagel against Birch on CBS L86.** The Phenomenologist praises "Insight is a phenomenal fact: the hallucination presents as unreal while remaining vivid". The Empiricist asks for the source and finds none. The page's own citations record that insight is *reported* (Teunisse: "all patients had full insight into the unreal nature of their hallucinations"). Its L38 records criteria that "demanded only partial insight". The Map's general description of hallucination (`perceptual-reality-monitoring-void` L64) gives hallucination the felt-real signal. The 10-19 deep review passed L86 because it "explicitly disclaims evidential weight". That disclaimer covers the tenets, not the descriptive premise. When the two personas conflict over the same sentence, the house rule says flag it, not praise it. This is Top-Priority 2. It is a register change in one paragraph and leaves the page's structure alone, so the 10-19 "converged on structure" note stands.
2. **Capgras L63 "exactly the patients"** overreaches its own L79 (Top-Priority 1).

No Process-Philosopher tier-upgrade was found anywhere in the wing.

## Uncovered Subjects (not covered by any live article)

Hit counts: `live` = files in `obsidian/topics concepts voids apex positions` matching the pattern (case-insensitive); `research` = files in `obsidian/research/`. Patterns were run with variants; controls `capgras` (live 14 / research 5) and `anosognos` (23 / 14) returned positive hits first, so the zeros below are not artefacts of a broken key. Authors marked *(lead)* were not verified this run.

1. **Presented versus inferred unreality: what clinical insight is made of.** Is a hallucination's or depersonalised scene's unreality given in the experience, or judged? This covers CBS, depersonalisation's "as if", phantom limb (the release-phenomena note's C4: "phantom limbs are felt as real limbs", so insight there is plainly judged), lucid dreaming, and Anton reading B. It decides where the Capgras/Cotard scope rule falls. Grep: `clinical insight|insight into (the|their) (illness|condition|disorder)` → live 0 / research 0; `reality[- ]stamp` → live 1 (`phenomenal-quality-void`) / research 2; insight-phrase variants (`retained insight|insight-lost|partial insight|...`) → live 9 / research 5, all passing uses; `reality[- ]testing` → live 6 / research 7. Natural home: a topics article (3 slots), or a fold into `voids/perceptual-reality-monitoring-void` (2624/3000, headroom 375).
2. **Is Factor 1 experienced? Unconscious-anomaly and endorsement/explanationist accounts of monothematic delusion.** The leads are Coltheart, Menzies & Sutton 2010, "Abductive inference and delusional belief" *(lead)*, on which the anomalous datum need not be conscious, and Bayne & Pacherie 2004 *(lead)* on endorsement versus explanation. The question bears directly on the Capgras/Cotard claim that "only the anomalous experience is the Map's territory": if Factor 1 can be unconscious, that territory shrinks. The vmPFC record above (absent SCR, nothing reported) is its first datum. Grep: `abductive inference and delusional` → 0 / 0; `Menzies` → live 4 / research 4, all Peter Menzies on causation; `endorsement account|explanationist` → live 1 (`phenomenal-conservatism`, unrelated) / research 1 (`thought-insertion-2026-10-01` §"Also present: endorsement accounts", about thought insertion); `Pacherie` → live 7, all agency phenomenology. Home: a fold into Capgras after Top-Priority 1 (headroom 1351), or topics.
3. **Delusional misidentification beyond Capgras**: Fregoli, intermetamorphosis, subjective doubles, reduplicative paramnesia, and mirrored-self misidentification, the last of which bears on self-recognition and Cotard. Grep: each of `fregoli`, `intermetamorphos`, `reduplicative paramnesia`, `mirrored[- ]self`, `subjective doubles?` → 0 / 0; `delusional misidentification|misidentification syndrome` → live 2 (capgras, recognition-void) / research 4. Home: a fold into `voids/recognition-void` (2478/3000, headroom 521; note its open P3 at todo ~L2019) or a topics article.
4. **Double bookkeeping: delusions held but not acted on.** Bleuler's term, used by Sass *(lead)*. The wing's own instance is Anton L52: "Although she would deny visual deficit, she would accept such assistance". The subject bears on whether a delusion is a belief, and so on what the Capgras page's Factor 2 is a deficit *in*. Grep: `double[- ]bookkeeping|bleuler` → 0 / 0; `delusions? (are|as) (beliefs|imaginings)|doxastic account of delusion` → 0 / 0; `bortolotti` → live 2 (both cite her 2018 confabulation paper) / research 3; `currie` → live 1 (`alief-and-acting-against-belief`, Currie & Ichino on alief, not delusion). Home: topics, or a fold into `alief-and-acting-against-belief` (3351/4000).
5. **Musical hallucinosis in acquired deafness, CBS's auditory twin.** Grep: `musical hallucin|musical hallucinosis|musical ear` → live 1 (`resolution-void`, a passing mention) / research 2 (`release-phenomena-2026-10-14`, which says outright "the Map has zero live coverage"; `voids-recurrence-void-2026-05-05`). Home: the release-phenomena page (item 6).
6. **Release phenomena as a family (banked, unconsumed).** `research/release-phenomena-2026-10-14` recommends a `concepts/release-phenomena` page covering CBS, tinnitus, musical hallucinosis, phantom limb and deprivation hallucination, with Anton as the contrast case. It sits in `pending_articles` with `target_section: concepts`, which is at cap. No live page links it and no todo task owns it. Grep: `release[- ]phenomen` slug → no live file. **Carry-forward defect for whoever writes it**: the note's Anton row says "Release needs an intact generator and a lost input; Anton has a lost generator", but Anton L54 records denial after *ocular* and optic-nerve blindness (Swartz & Brust 1984; McDaniel & McDaniel 1991), where the generator is intact. The contrast holds only for cortical Anton. Home: topics (the only section with room), or leave banked.
7. **Measuring insight in psychiatry**: the Scale to Assess Unawareness of Mental Disorder (Amador, *lead*) and the Beck Cognitive Insight Scale *(lead)*, and whether clinical insight is metacognition. Grep: `beck cognitive insight|cognitive insight scale|SUMD|unawareness of mental disorder|amador` → 0 / 0. Lower priority.
8. **Peduncular hallucinosis and ffytche's second (brainstem/neuromodulatory) hallucination syndrome**, which CBS L36 names and sets aside, and in which insight reportedly varies *(lead)*. Grep: `peduncular` → live 0 / research 1 (`logic-of-dissociation-inference-2026-10-19`, lesion-network mapping). Lower priority.

## Expansion Opportunities

### High Priority
- **The insight register (Uncovered 1)**: medium topics article or void fold. Builds on all five pages plus `phenomenal-quality-void` and `perceptual-reality-monitoring-void`. Tenet alignment: Tenet 5 (do not settle the register for tidiness); Dualism is unaffected either way, and the article should say so up front.
- **Is Factor 1 experienced? (Uncovered 2)**: fold into Capgras once Top-Priority 1 lands. It fixes the scope of the Map's "anomalous experience" claim.

### Medium Priority
- **Delusional misidentification family (Uncovered 3)**: fold into recognition-void.
- **Release phenomena (Uncovered 6)**: the banked note, which needs the Anton-row correction first.

### Ideas for Later
- Double bookkeeping (Uncovered 4); musical hallucinosis (5); insight scales (7); peduncular hallucinosis (8).

## Cross-Linking Suggestions

| From | To | Reason | Words |
|---|---|---|---|
| `topics/anton-syndrome-...` L74 "positive visual phenomena went with awareness of loss" | `concepts/charles-bonnet-syndrome` | that phrase describes CBS exactly | 0 (minted) |
| `topics/anton-syndrome-...` L101 neighbouring-cases sentence | `concepts/charles-bonnet-syndrome` | the true modal positive, the control for reading B | ~+15 (minted) |
| `concepts/charles-bonnet-syndrome` L62 / Further Reading | `topics/anton-syndrome-...` | Swartz & Brust separate content-insight from deficit-insight | ~+40 (minted) |
| `concepts/charles-bonnet-syndrome` L86 | `voids/perceptual-reality-monitoring-void`, `voids/phenomenal-quality-void` | the two Map framings of the felt-real signal | in the rescope (minted) |
| `concepts/cotard-delusion` L56 "non-delusional condition" | `concepts/depersonalisation-nosology` | the page that documents the insight criterion | 0 (minted) |
| `voids/necessary-opacity` L82 "retaining the insight" | `concepts/depersonalisation-nosology` | same | 0 (minted) |
| `topics/clinical-phenomenology-and-altered-experience` L107 "maintain insight" | `concepts/depersonalisation-nosology` | same; the page already lists nosology's topic in its frontmatter but has no body link | 0 (minted) |
| `voids/perceptual-reality-monitoring-void` L94 "Hallucination" | `concepts/charles-bonnet-syndrome` | the 10-14 suggestion, still uninstalled; **install only after Top-Priority 2 settles the register**, because the 10-14 label "felt-real signal absent" is the disputed claim | 0 (not minted) |
| `topics/capgras-...` L69 (after repair) | `concepts/cotard-delusion#Two Factors, One Factor, and the Depersonalisation Continuum` | the Factor-1-alone prediction lives there | 0 (not minted; the Capgras fork may take it) |

## New Concept Pages Needed

None proposed: concepts is at cap (370/370). The one concept-shaped candidate, `release-phenomena`, is banked research targeted at concepts. Its realistic homes are the topics section or staying banked.

## Tasks Added to todo.md

Four tasks, inserted immediately above `## Completed Tasks`:

1. **P2** — `topics/capgras-delusion-and-the-affective-recognition-channel` L69/L63 vmPFC "felt strangeness" fidelity + L35 "mineness" collision. File: `obsidian/topics/capgras-delusion-and-the-affective-recognition-channel.md`.
2. **P3** — `concepts/charles-bonnet-syndrome` L86 insight-register rescope + Anton link. File: `obsidian/concepts/charles-bonnet-syndrome.md`.
3. **P3** — `topics/anton-syndrome-and-the-sincere-report-of-seeing` CBS as the accurate-report control (L74 pipe, L101, after L72, Further Reading). File: `obsidian/topics/anton-syndrome-and-the-sincere-report-of-seeing.md`.
4. **P3** — three zero-word reciprocal pipes to `concepts/depersonalisation-nosology`. File: `obsidian/concepts/cotard-delusion.md` (plus two secondary hosts named in Notes).
