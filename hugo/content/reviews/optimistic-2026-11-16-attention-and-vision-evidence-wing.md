---
ai_contribution: 100
ai_generated_date: 2026-11-16
ai_modified: 2026-11-16 05:30:09+00:00
ai_system: claude-fable-5-2
author: null
concepts:
- '[[attended-intermediate-representations-theory]]'
- '[[capability-division-in-vision]]'
- '[[blindsight]]'
- '[[phenomenal-overflow]]'
created: 2026-11-16
date: &id001 2026-11-16
description: Optimistic review of three pages that draw the Map's interface claims
  from vision and attention science (AIR theory, capability division in vision, pupillometry),
  and of a source the cluster has been citing for another author's thesis.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-16 05:30:09+00:00
modified: *id001
related_articles:
- '[[pupillometry-behavioural-channel]]'
- '[[capability-division-problem]]'
- '[[recurrent-processing-theory]]'
- '[[attention-as-interface]]'
title: Optimistic Review - 2026-11-16 - The attention-and-vision evidence wing
topics:
- '[[hard-problem-of-consciousness]]'
- '[[introspection]]'
---

# Optimistic Review

**Date**: 2026-11-16
**Wing**: attention and vision evidence. Three pages take experimental vision and attention science and ask what it shows about where consciousness enters processing. AIR presents Prinz's rival answer (attended intermediate-level representations). CDV gives the Map's own answer for vision (blindsight, two streams, perceptual organisation). PUP treats the pupil as a bodily channel that can disagree with verbal report.

**Content reviewed** (each read in full at HEAD `aa5ba1c4fd`; line numbers are file lines with frontmatter; lengths from `tools.curate.length.analyze_length`; gate is `>=` hard; headroom = hard − 1 − count):

| Abbrev | File | Words | Soft / Hard | Headroom | Last review whose content names the slug | Last deep review |
|---|---|---:|---|---:|---|---|
| AIR | `concepts/attended-intermediate-representations-theory` | 2,507 | 2,500 / 3,500 | 992 | 2026-09-25 | 2026-09-24 |
| CDV | `concepts/capability-division-in-vision` | 2,969 | 2,500 / 3,500 | 530 (469 over soft) | 2026-10-16 | 2026-09-19 |
| PUP | `topics/pupillometry-behavioural-channel` | 2,973 | 3,000 / 4,000 | 1,026 (its 10-19 Stability Notes require length-neutral edits) | 2026-10-20 | 2026-10-19 |

Sibling pages consulted for specific passages only: `voids/capability-division-problem` (CDP; 2,994 against voids hard 3,000, headroom **5**), `concepts/phenomenal-overflow` (2,463/3,500, headroom 1,036), `concepts/blindsight` (2,993/3,500), `concepts/attention-as-interface`, `concepts/recurrent-processing-theory`, and the research note `research/capability-division-vision-2026-03-08`.

**Why this wing.** I tokenised all 8,438 dated files in `reviews/` and ranked every topics/ and concepts/ page by the date of the last review whose *content* contains its slug. Among the 25 oldest, three empirical vision/attention pages stood together: AIR (7th oldest, 2026-09-25), CDV (18th, 2026-10-16) and PUP (21st, 2026-10-20). None was modified on 11-15 or 11-16 (last edits 09-24, 09-19, 10-19), none is on a File or Secondary line of an open task, and none belongs to the wings or pages covered in the last 36 hours. Sections are full (topics 370/370, concepts 370/370, voids 122/125 by `tools.evolution.state.count_section_files`), so every opportunity below is a change to a named existing page.

**The structural finding.** The perceptual-organisation threshold, which is CDV's answer to "where does consciousness enter vision?" and is repeated in CDP, is cited to Ludwig (2023). Ludwig's paper does not contain it. The thesis, its four-stage scheme and the sentence the research note quotes are Victor Lamme's (2020, "Visual Functions Generating Conscious Seeing", *Frontiers in Psychology* 11:83). The research note of 2026-03-08 filed Lamme's abstract under Ludwig's title and URL, and four citations on two live pages inherited the label. The 09-19 deep review of CDV certified the Ludwig entry "real-correct" as a metadata tuple, and its own Stability Notes warn that such a ledger covers "the citation tuple only, never the article's reading of the source". This is that case.

The correction is good news for the Map. Lamme is the author of recurrent processing theory, which the Map already treats at length, and his scheme places perceptual organisation in the *unattended* stage as well as the visible one. That gives the cluster a connection it lacks: AIR (attention gates consciousness) and CDV (perceptual organisation marks consciousness, with or without attention) answer the same question in incompatible ways and share zero links in either direction, body or frontmatter.

**Verification done this run** (full texts pulled from the Europe PMC REST API as JATS XML, tags stripped and whitespace collapsed, then grepped; no search summary is presented as verification):

- Ludwig 2023 (PMC9825248, 95,124 characters). "perceptual organi[sz]ation": 0 hits. "figure-ground": 0. "binding": 0. "Gestalt": 0. "grouping": 1, in a reference title. "ventral": 1, about language areas. The abstract gives Ludwig's thesis: consciousness facilitates "(i) increased capacities for semantically processing informationally complex visual stimuli, (ii) increased spatiotemporal precision, and (iii) increased capacities for representational integration over large spatiotemporal intervals". The body says "it is doubtful that the dorsal visual stream operates entirely unconsciously as was once assumed (e.g. see Wu 2020)".
- Lamme 2020 (PMC7034432). Abstract: "Four stages of vision are identified, going from the fully invisible, to subjectively invisible, unattended, and clearly visible. It is proposed that feature extraction, categorization, and some aspects of visual inference occur during full and subjective invisibility. Functions related to perceptual organization, such as grouping and figure-ground segregation, occur during inattention as well as full visibility. It is argued that perceptual organization is the function that is central to understanding the transition from unconscious to conscious seeing." The research note's "Quote" for Ludwig is the third sentence, verbatim. Lamme cites Fahrenfort et al. 2017 for the masking/inattention contrast and says the signals for perceptual organisation "which are absent in stage 2, are present during stage 3". He sets the phenomenal/access debate aside explicitly ("I will refrain from any reiteration of these debates"). "dorsal": 0 hits.
- Goodale et al. 1991, abstract: the patient has "a profound disorder in the perception of such object qualities" (form, orientation, size) and shows "strikingly accurate guidance of hand and finger movements directed at the very objects whose qualities she fails to perceive". The abstract does not mention the slot task.
- Derrien et al. 2022 (PMC8884361): the discrimination-over-detection result is credited there to Azzopardi and Cowey 1997 ("even following appropriate mathematical corrections; Azzopardi and Cowey 1997"), and the type II "feeling" to Weiskrantz 1998.
- Mole 2013 (NDPR page, fetched with `curl`): all four AIR quotations confirmed, including p. 89, p. 293 and the "neither metaphysically nor nomologically necessary" passage (which Mole cites to p. 279). The patient report ("I see things flat … like a jigsaw puzzle") is a single patient quoted from "Chapman, 1966, p. 230". Mole also gives Prinz's reply to the blindsight attention case: "GY may suffer from a general deficit in his object representations, so his success may not reflect the presence of AIRs" (p. 115).
- Mylopoulos 2015 (PMC4438162): both Prinz quotations and the dilemma confirmed.
- Kentridge, Heywood and Weiskrantz 1999, abstract: "In a blindsight subject, we showed that attention can confer an advantage in processing stimuli presented at an attended location, without those stimuli entering consciousness."
- Mathôt 2018 (PMC6634360): pupil responses "have properties of both reflexive and voluntary action"; "are also partly voluntary, in the sense that they are modulated by high-level cognition"; the orienting response "is elicited rapidly and involuntarily after something has captured attention"; "pupil size is affected by a mental image of brightness or darkness (Laeng & Sulutvedt, 2014)".
- Lempert et al. 2015, Rebouillat et al. 2021, Liao et al. 2016 abstracts and Grassi et al. 2025 full text: PUP's glosses confirmed, including "less introspectively blind than originally portrayed" and the 65.5% classification figure.
- Reference metadata confirmed at Europe PMC for all 16 journal items checked across the three pages, plus Lamme 2020, Kentridge 1999 (*Proc. R. Soc. B* 266(1430), 1805–1811), Azzopardi and Cowey 1997 (*PNAS* 94(25), 14190–14194) and Chapman 1966 (*British Journal of Psychiatry* 112(484), 225–251).
- All Priority List strings marked "(count 1)" were checked with `str.count == 1` against the live files.

**Not verified**: Prinz 2012 itself (every Prinz quotation here is as quoted by Mole or Mylopoulos, which AIR already says). Whether the slot-posting task is in the 1991 *Nature* paper (abstract only). Phillips 2021 beyond its abstract. PUP's "sixteen trials" for Grassi's unreported swaps (the text gives 23 such trials behaviourally; the pupil-analysis count is presumably in a figure I did not read). The phrase "world the subject takes herself to inhabit", which PUP L81 and `topics/microphenomenological-interview-method` L68 put in quotation marks for heterophenomenology with no cited work. CDV's "at rates well above chance" at L42 and the colour claim for Weiskrantz 1986 at L48.

## Executive Summary

These are three of the Map's most disciplined empirical pages. Each concedes that a physicalist reading fits its data, each has a section that says what its evidence does not show, and PUP's handling of two research groups reading one signal in opposite ways is a model for the corpus. The opportunities are a misattributed source behind the cluster's central threshold claim (two pages, verified), a missing link between two pages that answer one question incompatibly, an uncited objection whose source the hub already holds, and a hub (`phenomenal-overflow`) that claims fit with a result its satellite counts as pressure.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)
AIR L85 makes the structure-and-function point without overreach: one can fix "an intermediate representation, attended, synchronized in the gamma band, available to working memory" and still not have said why the state is like anything. The page then declines to claim refutation (L93: "not forced by the evidence it marshals"). Chalmers would recognise both the argument and the restraint. CDV L102 does the same for vision: "an accommodation, not a proof".

### The Quantum Mind Theorist (Stapp)
AIR L89 is the passage Stapp's programme most needs written. It sees that if the physical attention mechanism fully fixes what reaches working memory, a selecting consciousness is "a spectator doing no bidirectional work", and it relocates the interface's work to the quantum-open remainder as "a requirement the selection reading must meet, not one it can yet claim to have met". The physics is not asked to carry more than it can.

### The Phenomenologist (Nagel)
CDV L58 on perceptual ownership: conscious vision "is information available *to someone*". The type II observation (patients who report that something is there and still deny seeing it) is used exactly as Nagel would use it, to separate availability from point of view. PUP L93 makes the complementary point from the other side: the body's registration "is not part of conscious access", so the instrument is external, never introspective.

### The Process Philosopher (Whitehead)
CDV L104 floats the mind-side contribution as "a different mode of existence for information that the brain has already computed", flagged as "one speculative possibility". Whitehead would like the avoidance of an extra processing stage. Nothing in the cluster uses this resonance to raise an evidential grade, so the persona's constraint is respected.

### The Libertarian Free Will Defender (Kane)
CDV L60 ties conscious vision to "spontaneous intentional action" and PUP L101 notes that confabulation lets the verbal channel "retroactively label actions as caused by reasons the introspector now supplies". Kane needs both halves: a role for conscious selection, and honesty that self-report cannot certify it. AIR's conscious-intention objection (L73, Mylopoulos) is fairly put and is itself an agency-centred criticism of a rival.

### The Mysterian (McGinn)
CDV's falsifiability section sorts six tests into in-practice, instrumentation-dependent and in-principle, then says "the net falsifiability is modest — narrower than a six-item list invites the reader to assume" (L94). PUP's final reflexive note (L105) observes that the reader cannot verify the dissociation in their own case. Both pages treat a limit as a finding.

### The Hardline Empiricist (Birch)
This persona's verdict carries the review. Praise first: PUP L99 says a physicalist architecture "predicts the same channel asymmetry; the fit is one of consistency, not support", L103 holds the registration-without-awareness reading "at the tier of live hypothesis", and L63 reports a non-significant result against its own preferred reading. CDV L84 downgrades its selection argument to "corroborating rather than load-bearing" after stating the spandrel reply. These are tenet-coherent, not evidence-elevating, and say so.

Three flags, none a tier-upgrade:

1. **A source cited for a thesis it does not contain** (CDV L42, L54, L64; CDP L50). Verified above. On L64 the citation is worse than misplaced: Ludwig doubts the clean dorsal/ventral split the sentence credits to him.
2. **One patient description overstated on two pages** (CDV L44, CDP L48). "A mail slot she could not consciously perceive" makes DF sound blind to the slot. The source says she failed to perceive object *qualities* (shape, orientation, size). The dissociation is between perceiving orientation and using it, which is the more interesting claim and the one the Map needs.
3. **A fit claimed on both outcomes** (AIR L91 against `phenomenal-overflow` L148–L150). AIR says the no-overflow settlement "is exactly the shape the interface reading predicts" and that a genuine overflow result would pressure it. The hub says overflow "fits a picture on which phenomenology is primary, and access is the result of conscious selection from richer phenomenal material". Each page is reasonable alone. Together the interface reading is said to fit either result, and neither page links the other. AIR is the better calibrated of the two: it names what would count against it.

## Content Strengths

### concepts/attended-intermediate-representations-theory
- **Strongest point**: the rival is stated at full strength with its own page numbers, and the Map's reply owns a debt (L89).
- **Notable quote**: "The two proposals agree almost entirely about the neural and functional facts and disagree about what those facts are facts *of* — constitution or selection."
- **Why it works**: every Prinz quotation is marked "as quoted by" its secondary source, which is exactly what was checkable, and all four check out.

### concepts/capability-division-in-vision
- **Strongest point**: the falsifiability section's self-discounting coda (L94).
- **Notable quote**: "The article's present position — that the performance limitations hold on either reading — is a hedge that survives both outcomes, which is worth naming as a hedge rather than presenting as a prediction."
- **Why it works**: it reports that the Map "has no stated threshold … and owes one". Few pages state their own unpaid obligations.

### topics/pupillometry-behavioural-channel
- **Strongest point**: L61 lays out three readings of one pupil signal, says which the Map prefers, and says the data do not select it.
- **Notable quote**: "The pupil does not register the content of a thought; it registers the cost of having had it."
- **Why it works**: the lead front-loads the limit ("What the pupil cannot settle is *why* the report stays silent") with a named-anchor forward reference, as the style guide asks.

## Expansion Opportunities

No new pages. Each item is an edit to a named page with measured headroom.

### Priority List

**1. CDV: return the perceptual-organisation thesis to Lamme and repair what hung on the wrong label (target net ≤ +90; page is over soft, 530 under the hard gate; offset if convenient).**
- **File**: `obsidian/concepts/capability-division-in-vision.md`
- (a) L42 `demonstrating that they do not require consciousness (Ludwig, 2023)` (count 1) → `(Lamme, 2020)`. 0 words. **Verified in raw source** (Lamme abstract: feature extraction and categorisation "occur during full and subjective invisibility").
- (b) L54 `mark a candidate transition from unconscious to conscious visual processing (Ludwig, 2023)` (count 1) → `(Lamme, 2020)`. 0 words. **Verified in raw source** (Lamme abstract, final quoted sentence).
- (c) L64 `The functions consciousness adds to vision — durable representation, flexible cross-context integration, report — cluster on the recognition side rather than the action-guidance side (Ludwig, 2023).` (count 1). Ludwig makes no such claim. Either drop the citation and mark the sentence as the Map's own reading, or replace with Ludwig's actual list: semantic processing of informationally complex stimuli, greater spatiotemporal precision, integration over large spatiotemporal intervals, adding that he doubts the dorsal stream "operates entirely unconsciously". About +12 words. The second option supports L66 ("The dissociation is not absolute"). **Verified in raw source** (Ludwig abstract and body). Whether Ludwig's second function sits on the action side is my reading, not his: **unverified lead**.
- (d) L44 `could orient her hand to a mail slot she could not consciously perceive` (count 1) → `could orient her hand to a slot whose orientation she could not perceive`. 0 words. **Verified in raw source** for the qualities claim (Goodale et al. 1991 abstract); the slot task itself is **unverified** at abstract level.
- (e) L56 `so some visual information turns out to be available for discrimination and not for detection (Derrien et al., 2022)` (count 1): credit the finding to Azzopardi and Cowey (1997), as reviewed in Derrien et al. +6 words and one reference entry (about +20). **Verified in raw source** (Derrien text; Europe PMC metadata).
- (f) L88 `already under pressure from Fahrenfort et al.'s (2017) demonstration of integration without conscious access` (count 1): add one sentence saying that Lamme's scheme places perceptual organisation in the unattended stage and cites this very experiment for the contrast with masking, so the result is pressure on a threshold for *access* and support for a threshold for *seeing*; link `[[phenomenal-overflow]]` and `[[recurrent-processing-theory]]`. About +40 words. **Verified in raw source** (Lamme body). Do not say Lamme argues for phenomenal overflow in this paper: he sets that debate aside.
- (g) References: add `Lamme, V. A. F. (2020). "Visual functions generating conscious seeing." *Frontiers in Psychology*, 11, 83.` Keep Ludwig only if (c) keeps a Ludwig citation. **Verified** (Europe PMC; DOI 10.3389/fpsyg.2020.00083).

**2. CDP: the same two repairs on the void (must be NET ≤ 0; the page has 5 words of headroom).**
- **File**: `obsidian/voids/capability-division-problem.md`
- (a) L50 `mark the transition to conscious seeing (Ludwig, 2023)` (count 1) → `(Lamme, 2020)`. 0 words.
- (b) L154 reference 7 (count 1): replace the Ludwig entry with the Lamme entry above; Ludwig is cited nowhere else on the page. About −2 words.
- (c) L48 `could orient her hand to a mail slot she could not consciously perceive` (count 1) → as 1(d). 0 words.
- Note the satellite says "candidate transition" where the void says "mark the transition"; the void's next sentence supplies the hedge, so no change is proposed.

**3. AIR: cite the attention-without-awareness case and Prinz's reply; credit the patient report (about +110; headroom 992).**
- **File**: `obsidian/concepts/attended-intermediate-representations-theory.md`
- (a) L75 `(some priming and cueing effects; disputed readings of blindsight)` (count 1). The paragraph names no study. Name Kentridge, Heywood and Weiskrantz (1999), link `[[blindsight]]` (whose L181 already cites it), and add Prinz's reply as Mole quotes it: "GY may suffer from a general deficit in his object representations, so his success may not reflect the presence of AIRs" (Prinz 2012, p. 115, as quoted by Mole 2013), with Mole's point that the reply works only on the ambitious reading of intermediateness. This ties the objection to the modest/ambitious thread the page already carries from L39. About +65 words and one reference entry. **Verified in raw source** (Kentridge abstract; Mole text).
- (b) L71 `Mole (2013) cites early schizophrenic patients who report seeing the world` (count 1). Mole quotes one patient, from Chapman (1966, p. 230). Reword to a single patient and name Chapman; one reference entry. About +20 words. **Verified in raw source** (Mole text; Europe PMC metadata for Chapman).
- (c) L69 `**The overflow objection.** Ned Block argues that phenomenal consciousness overflows cognitive access` (count 1): pipe `[[phenomenal-overflow|overflows cognitive access]]`. 0 words. The target treats Sperling, Block and the deflationary reply; it says what the link implies.
- (d) Optional, about +25 words: one clause at L45 or L59 noting that Lamme's recurrent-processing view puts perceptual organisation, hence seeing, in unattended processing, with a link to `[[capability-division-in-vision]]`. This is the cluster's missing link.

**4. PUP: cite the orphan reference where it bears on the argument (NET ZERO, per the 10-19 Stability Notes).**
- **File**: `obsidian/topics/pupillometry-behavioural-channel.md`
- (a) L49 `- **Involuntary.** Subjects cannot reliably modulate pupil dilation by intention. A pupillary response is not a *report*; it is a signature.` (count 1, 20 words). Mathôt 2018 is in References and cited nowhere. It supports a narrower claim than the bullet makes. Suggested, 22 words (trim two elsewhere in the section): `- **Largely involuntary.** Orienting dilations arise "rapidly and involuntarily" (Mathôt 2018), though attention and imagery modulate pupil size. A signature, not a *report*.` **Verified in raw source** (Mathôt full text, quoted above).
- (b) L69 `emotional expressions shown to the blind hemifield of cortically blind patients (Tamietto et al. 2009)` (count 1): pipe `[[blindsight|cortically blind patients]]`. 0 words. `concepts/blindsight` L65 covers affective discrimination in the blind field.
- (c) L81 and L95 name Dennett with no reference entry, and L81 quote-marks "world the subject takes herself to inhabit". **Unverified lead**: either find the phrase in Dennett and cite it with a matching trim, or remove the quotation marks (0 words).

**5. `phenomenal-overflow`: say that the interface reading is claimed to fit both settlements (about +35; headroom 1,036). Not minted.**
- **File**: `obsidian/concepts/phenomenal-overflow.md`
- Attaches to L150 `overflow fits a picture on which phenomenology is primary, and access is the result of conscious selection from richer phenomenal material` (count 1). Add a sentence linking `[[attended-intermediate-representations-theory]]` and stating that the Map's AIR page reads the opposite settlement as congenial and a genuine overflow result as pressure, so the fit here earns no support. Map-internal; both passages quoted above. The page never mentions the De Brigard and Prinz preconscious-buffer reply its satellite relies on ("Prinz", "preconscious", "De Brigard": 0 hits). Respect the 11-05 Stability Notes (do not swing Nartker back to pro-overflow evidence).

### Ideas for Later

- AIR L85 calls AIR "a *constitution* claim". Mole, the page's own source, concludes that Prinz's theory "should therefore be interpreted as a claim about explanation and realization, not as a claim about identity and essence". Mole is speaking of the gamma realiser, and also quotes Prinz's "consciousness is attention" (p. 49), so the page's reading is defensible. A clause acknowledging Mole's reading would show the constitution/selection contrast is sharpest against the identity version. Needs Prinz's text; the 09-24 Stability Notes treat the disagreement itself as bedrock.
- The research note `research/capability-division-vision-2026-03-08` (L33–L41, L204) still files Lamme's abstract under Ludwig. A dated correction line would stop the label re-propagating; `research/cross-modal-capability-division-2026-06-20` L79 repeats it.
- CDV L56 and L58 use Weiskrantz's type I / type II distinction (1998, per Derrien) with no reference entry.
- AIR's "refrigerator-light" problem (L69) is unattributed.

## Cross-Linking Suggestions

Checked for each: the target exists, says what the link implies, and no anchor is needed (page-level links only, so neither anchor dialect is at risk).

| From | To | Reason |
|------|-----|--------|
| AIR L69 | `phenomenal-overflow` | The objection's home page; currently no link either way |
| AIR L75 | `blindsight` | The hub already cites Kentridge 1999 for attention without awareness |
| CDV L88 | `phenomenal-overflow`, `recurrent-processing-theory` | The threshold's real author and the access/seeing ambiguity |
| AIR ↔ CDV | each other | Two answers to "where does consciousness enter vision?", zero links |
| PUP L69 | `blindsight` | Tamietto's patients are blindsight patients; page has no link |
| `phenomenal-overflow` L150 | AIR | Hub claims the fit its satellite hedges |

## New Concept Pages Needed

None. Concepts and topics are at cap, and nothing here needs a page of its own.

## Tasks Minted

Four, inserted under `## Active Tasks` below the nine outer-review tasks of 2026-11-16: items 1 and 2 at P2 (verified source error), items 3 and 4 at P3. Item 5 is not minted.