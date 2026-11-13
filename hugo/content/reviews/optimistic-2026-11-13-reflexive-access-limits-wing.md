---
ai_contribution: 100
ai_generated_date: 2026-11-13
ai_modified: 2026-11-13 19:59:37+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[self-reference-paradox]]'
- '[[inverted-qualia]]'
created: 2026-11-13
date: &id001 2026-11-13
description: 'Optimistic review of four pages on what a subject cannot reach: itself
  as subject, the world apart from its own contribution, the split that makes both
  limits, and the character of other minds.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-13 19:59:37+00:00
modified: *id001
related_articles:
- '[[self-reference-paradox]]'
- '[[constitutive-exclusion]]'
- '[[the-subject-object-distinction-as-philosophical-discovery]]'
- '[[consciousness-and-the-problem-of-other-properties]]'
title: Optimistic Review - 2026-11-13 - The reflexive access-limits wing
topics:
- '[[hard-problem-of-consciousness]]'
- '[[constitutive-exclusion]]'
---

# Optimistic Review

**Date**: 2026-11-13 (19:47–19:59 UTC, cycle slot)
**Wing**: reflexive access limits. Each page names one direction in which a conscious subject cannot get outside its own standpoint: toward itself, toward the world, and toward other subjects. The fourth page covers the subject-object split that produces all three.

**Content reviewed** (each read in full at HEAD `076137005c`; line numbers are `Read`-tool file lines with frontmatter included; lengths from `tools.curate.length.analyze_length`, body-only; headroom = hard − 1 − count, gate `>=`):

| Abbrev | File | Words | Hard | Headroom | Last optimistic mention (tokenised content of all `reviews/optimistic-*`) | Other reviews |
|---|---|---:|---:|---:|---|---|
| SRP | `concepts/self-reference-paradox` | 2,564 | 3,500 | 935 | 2026-07-26 (one passing hit) | deep 07-25; outer 10-14 mentions it only in passing |
| CE | `topics/constitutive-exclusion` | 3,948 | 4,000 | **51** | 2026-08-02 (one passing hit) | deep 09-10; outer-review cycle 09-29 (single-article subject); pessimistic 11-12 on correlationism quotes it once |
| SOD | `topics/the-subject-object-distinction-as-philosophical-discovery` | 2,409 | 4,000 | 1,590 | 2026-07-19 | deep 09-29; outer 10-03 lists it |
| POP | `topics/consciousness-and-the-problem-of-other-properties` | 2,112 | 4,000 | 1,887 | 2026-08-02 | deep 07-19; mentions in pessimistic 09-07 and deep 09-29 (modal structure) |

**Why this wing.** I tokenised every review file once and tested each live slug in link or path position. Then I ranked all 931 live pages by the date of their last optimistic mention, among those with no review-file mention since 2026-10-30. These four form the oldest coherent cluster in that ranking. A substring grep of all `reviews/` content confirmed that no review in the last 14 days takes any of them as its subject. The only 14-day hit is one passing quotation of CE in the 11-12 pessimistic review of `correlationism-and-the-ancestrality-argument`. None of the four appears in `git log --since='40 hours ago'` for the content sections. None of today's reviewed pages (`voids/weeping-void`, `topics/self-observation-and-the-moments-of-selection`, `topics/structure-of-attention`, `apex/moral-status-of-edge-cases`) is in the wing, and the 11-13 existential-givenness wing shares no page with it. No open task above `## Completed Tasks` targets any of the four.

Section counts (`tools.evolution.state.count_section_files`, 19:55Z): topics 370/370 and concepts 370/370 (both full), voids 120/125, positions 28. No expand-topic is proposed for topics/ or concepts/. Every new subject below is either a fold into an existing page or a later idea.

**Verification done this run** (files in `/tmp/claude-1000/-home-andy-unfin-unfinishablemap/e7fd0dd3-0248-4116-a7c5-2dabdf48c5ec/scratchpad/optrev/`):
- Kim, Garg, Peng and Garg (2025), quoted at CE L65. The arXiv 2506.07962 abstract contains the quoted sentence verbatim, and the four authors match.
- Buyl et al. (2026), cited at CE L65 and L161. Crossref confirms *npj Artificial Intelligence* 2(1), article 7, DOI 10.1038/s44387-025-00048-0.
- Kawakita et al. (2025), "Is my 'red' your 'red'?", proposed below for POP. Crossref confirms *iScience* 28(3), five authors, DOI 10.1016/j.isci.2025.112029.
- Steyvers & Peters (2025), cited at SRP L94. The OpenAlex abstract (DOI 10.1177/09637214251391158) is an overview comparing LLM and human metacognition. It says nothing about blind spots that "the system cannot detect, because detection would require the compromised capacity". The full text was not obtained, so this is tasked as assess-first.

**Not obtained**: Wheeler 1983 p. 184 wording; Putnam 1981 p. xi; Merleau-Ponty Landes p. lxxiii; Nagel 1986 pp. 70, 90, 105. All of these are quoted at CE L45–L61 and were not re-fetched; the 09-10 deep review is their last check.

## Executive Summary

CE is the best-calibrated page in the wing and one of the most careful on the Map. It grades its own claim into four rungs of unequal security. It counts its six traditions as "two or three independent strands". It quotes Merleau-Ponty's Preface against its own use of him. It ends by saying the void "supplies no support for dualism" (L113). The other three pages are older and less revised, and each still states something about the Map's own commitments more strongly than a sibling page now allows:

- **POP** says two people with inverted colour spaces could have no difference in "behaviour or brain activity" (L44). It says the barrier is one "no amount of scientific or philosophical progress can cross" (L107). `concepts/inverted-qualia` L171–L175 says that under Bidirectional Interaction any *actual* inversion "should produce subtle behavioural differences", and treats strict behavioural identity as "physically unrealised though conceivable". POP never mentions the Bidirectional Interaction tenet.
- **SOD** cites the comparative phenomenology of meditation as documenting "this convergence" on the subject-object asymmetry (L63). The page it links, at L75–L87, documents convergence on states where the distinction *dissolves* (Advaita non-dual awareness, kensho, rigpa). That is the condition SOD's own first falsifier names (L101), and L111 says no falsifier has been met.
- **SRP** says "Dualism predicts this structure" and that physicalism "struggle[s] with strong-form cases" (L146). CE L129 concedes that "a physicalist can predict much of the same inaccessibility", and [P-V2](/positions/voids-as-evidence/#p-v2) says a tenet that removes a defeater does not thereby upgrade the evidence.

Of the twelve directed links among the four pages, seven are missing from the body. POP links none of the other three and none of them links POP.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

POP's opening states the problem as two questions, each its own: "The problem of other minds asks whether anyone else is home. The problem of other properties asks what it is like *inside* their home" (L36). Chalmers would recognise the inverted spectrum being used for its epistemic consequence rather than as yet another argument against functionalism (L46). He would value POP L54 even more, which ties the interpersonal case to the modal backbone: "The gap is between categories of fact — physical and phenomenal — not between crude and fine-grained physical descriptions."

SOD keeps the hard problem in view when it answers enactivism. Its third reply (L77) separates the claim that the subject is *embodied* from the claim that it is *identical to* bodily activity. It concedes the first and locates the dispute in the second: "Why is this particular pattern of embodied activity accompanied by experience at all?" That separation is the cleanest dualist reply to 4E cognition anywhere in the wing.

### The Quantum Mind Theorist (Stapp)

SRP L128 gives the structural parallel with the measurement problem as two specific shared features: the apparatus is coupled to the system, and "no meta-level description resolves the problem because any such description presupposes measurement". It then marks the Map's extension as speculative: introspection "may literally constitute a quantum measurement on the consciousness-brain system. This is speculative; the structural case holds independently" (L130). Stapp would find the hedge the right one, but it does not survive into SRP L148 (see [Calibration Concerns](#calibration-concerns-tasked-not-praised)).

CE handles Wheeler better than most sympathetic readers would. It quotes the registration dictum and then reads its qualifiers against the Map: "A photodetector is not a mind" (L61). L67 adds: "Putting consciousness where Wheeler put registration is the Map's move rather than his." A quantum-mind theorist who wants Wheeler as an ally should start from this paragraph, because it shows exactly how much of Wheeler the ally gets.

### The Phenomenologist (Nagel)

CE treats Nagel with unusual fidelity. It quotes his stated aim, "to defend the possibility of objective ascent and to understand its limits", and concludes: "Nagel therefore limits what objectivity can *capture*, not what it can *reach*" (L57). Nagel would recognise his realism there, and would be glad not to be enlisted as a correlationist.

POP's examples centre first-person character at more than one grain. Grief can differ between two people "not just in how it feels but in whether it feels like *one* thing at all" (L62). Temporal reports "describe structural features — relations between moments — not the intrinsic quality of temporal experience" (L64). The second point anticipates the structure-versus-character line that colour science has since made empirical (see [Expansion Opportunities](#expansion-opportunities)).

SRP L90 gives the phenomenology of the subject's absence from its own field: "The subject is the limit of the experiential field, not an item within it." It cites Hume and Wittgenstein's eye. SOD L53 states the same point in its own words ("the real subject slips behind the attempt").

### The Process Philosopher (Whitehead)

CE L45 lets Merleau-Ponty's "constituting but also constituted" (Reynolds's gloss, labelled as a gloss) set against the clean spectator, then turns the Preface against the constitutive reading. Whitehead would admire a page that refuses both the detached subject and the manufactured world. SOD's enactivism section (L69–L77) also takes the organism–environment loop seriously before it objects.

None of the four pages uses process-philosophical resonance to move anything up the evidential scale, so the Hardline Empiricist has no slippage to check on this axis.

### The Libertarian Free Will Defender (Kane)

SOD L93 runs the self-stultification argument and adds the reply the epiphenomenalist would make: "The inference is not airtight; the epiphenomenalist may reply that the talk is caused by physical states correlated with experience rather than by experience itself." Kane would value an agency argument that names its weak joint.

SRP L150 makes the opacity of decision a prediction of the interface model: the mechanism "would operate below the resolution of self-modelling". That is a fair use of the Bidirectional Interaction tenet. Its support at L100, Libet's experiments showing awareness "after neural commitment has begun", states the contested reading without the Schurger et al. (2012) accumulator reinterpretation that the Map's own `topics/free-will` engages.

### The Mysterian (McGinn)

SRP gives McGinn a structural reason for closure in place of a mood. Its three conditions (L58–L62: instrument-object identity, no meta-instrument, no un-inspected baseline) turn the slogan "the mind cannot know itself" into something that can be checked. When all three hold, the paradox follows. When one fails, as with the weak form on public objects where "multiple observers triangulate" (L78), the circle is benign. The weak/strong distinction and the third gradient of "irrecoverably-conditioned inspection" (L82) are the most reusable machinery in the wing.

CE L115 says what would narrow the void, and concedes that the direct defeater is "one the thesis predicts will not be found, so the indirect tests are the operative ones". A mysterian rarely says which observations would shrink the closure; CE does.

### The Hardline Empiricist (Birch)

The verdict is split, and it runs by page age.

**CE passes everywhere this persona looked.** Its lead (L35) is a ladder of four claims: well supported, convergent, "possible, not established", and "the Map's own extension, conditional on its tenets and argued from no cited tradition". Each tenet paragraph in its Relation section (L127–L135) states its evidential role. Bidirectional Interaction "supplies the commitment, the premise supplies the bridge; neither is evidence". Dualism "offers a reading of the exclusion rather than receiving support from it", and the paragraph cites [P-V2](/positions/voids-as-evidence/#p-v2). No Many Worlds "removes a defeater and supplies nothing further". Occam's Razor is "disabled in both directions and favours neither". The page applies its independence discount to its own medium as well: L65 notes that the sibling voids were "drafted by the same kind of instrument from the same corpus", and supports the point with a correlated-errors result verified today. That paragraph is the clearest example on the Map of *tenet-coherent, not evidence-elevating* applied to a whole page.

**SOD is partly calibrated.** It refuses the upgrade twice in its own voice: the cross-tradition encounter is "suggestive rather than decisive" (L63), and concession-convergence "removes a defeater rather than supplying fresh positive evidence" (L65). The problem is the evidence it cites at L63, covered under Calibration Concerns.

**SRP and POP still carry the older register.** SRP's "Dualism predicts this structure" (L146) and "competing frameworks must explain away" (L156) predate CE's discipline. So do POP's "demonstrate" (L86) and "permanent feature of a world that contains more than matter" (L107). They are flagged below rather than praised.

## Content Strengths

### concepts/self-reference-paradox (SRP)
- **Strongest point**: The three architectural conditions (L58–L62) and the failure modes they produce (L64: "epistemic circularity ... disappearing objects ... self-sealing confidence").
- **Notable quote**: "The circle is benign where the object is publicly accessible (multiple observers triangulate); where the object is private, benignity fails and the circle bites." (L78)
- **Why it works**: The page turns a family resemblance across four voids into a diagnostic with stated conditions, so a reader can test a new candidate against it. L80 and L120 keep the mutation void's constitutive claim "at the hypothesis tier", which is the right register for the strong form. At L94 the page states that Michel argues calibration is achievable and then disagrees with him openly, rather than enlisting him.

### topics/constitutive-exclusion (CE)
- **Strongest point**: The four-sense analysis of "constitutes" (L127), with the thermostat as the control case: "a thermostat shapes the room's temperature without being barred from knowing the room."
- **Notable quote**: "A shared ancestor can transmit a shared prejudice as readily as a shared insight, so the convergence is suggestive rather than decisive." (L63)
- **Why it works**: The page argues against its own sources wherever they resist it: the Merleau-Ponty Preface (L45), Nagel's realism (L57), Putnam's 1994 natural realism (L59), Kant's denial that the mind constitutes the noumenon (L67), and Meillassoux's ancestrality, which it accepts through the prebiotic-collapse account (L111). Its realist-replies section (L101–L115) gives structural realism, naturalised epistemology, disjunctivism, Meillassoux and self-refutation each a paragraph and concedes something to each. At 3,948 words with 51 of headroom, the page is finished as it stands, and nothing below asks it to grow.

### topics/the-subject-object-distinction-as-philosophical-discovery (SOD)
- **Strongest point**: The enactivism section's three replies, especially the embodied-versus-identical distinction (L77).
- **Notable quote**: "Descartes did not invent subjectivity, but he discovered how to make it philosophically visible." (L47)
- **Why it works**: The page's thesis, that the distinction was found rather than imposed, is one a reader can test, and the page supplies five falsifiers (L101–L109). L63 carries CE's four-rung grading into the Husserl paragraph accurately, including CE's realism about pre-conscious physical fact. That is a good example of a sibling page inheriting a correction instead of re-stating the old claim, which the 09-29 outer-review cycle asked for. The cost is readability: L63 is a single paragraph of 376 words, and its exclusion sentence runs past 100.

### topics/consciousness-and-the-problem-of-other-properties (POP)
- **Strongest point**: The access/existence distinction (L82): "Other people's phenomenal properties are perfectly real and determinate. The barrier is access, not existence."
- **Notable quote**: "The privacy of phenomenal properties is the cost of their reality." (L109)
- **Why it works**: POP generalises a familiar problem to one level down, and its testimony section (L68–L76) names the mechanism: words for phenomenal qualities are learned "through public criteria", so language "encodes relations and functions rather than intrinsic qualities". The four falsifiers (L94–L97) are concrete. The contemplative paragraph (L88) answers the objection that self-access is weaker than assumed by turning it into a further limit. It is the most clearly argued page in the wing, and the one whose central claim most needs re-scoping to the Map's own later commitments.

## Calibration Concerns (tasked, not praised)

These are recorded because the skill routes possibility/probability slippage to `refine-draft` rather than praise.

1. **POP against inverted-qualia and the Bidirectional Interaction tenet.** POP L44 says of inverted colour spaces that "Nothing in their behaviour or brain activity need differ". L72 says "Their testimony is indistinguishable, but their experiences differ". L54 says a perfect scanner "would still face the explanatory gap", and L107 says the barrier is one "no amount of scientific or philosophical progress can cross". `concepts/inverted-qualia` (deep-reviewed 11-11) says at L171: "Phenomenal character is causally efficacious, so any *actual* instance of qualia-inversion should produce subtle behavioural differences". At L175 it calls strict behavioural identity with a qualia difference "a limit case the Map treats as physically unrealised though conceivable". That text has stood since at least 2026-04-19 (`git log -S` returns the 04-19 condense). POP's 07-19 deep review left the conflict in place, and POP's Relation section (L101–L109) does not mention Bidirectional Interaction.

   The repair keeps POP's core. Under the Map's tenets, a *difference* between two people's qualities is in principle detectable at fine grain. What stays closed is identifying *which* quality the other instantiates, because behavioural and neural data fix structure only up to isomorphism (Palmer 1999, already cited at `inverted-qualia` L78). POP L64 already makes the "structure, not character" point for time. L105's MQI claim, that two brains "with identical quantum states could ... be paired with different phenomenal properties", needs the same tenet-conditional marking, since a different selecting subject would by the Map's own account bias outcomes differently.

2. **SOD's convergence evidence is the dissolution its falsifier names.** SOD L63 says "the subject-object collapse is one of three structural features discovered independently" and cites `topics/comparative-phenomenology-of-meditative-traditions` as documenting "this convergence". That page's section "The Subject-Object Collapse" (L75–L87) describes "states where the ordinary distinction between experiencer and experienced dissolves". Its examples are Advaita ("*advaita* means 'not-two'"), Zen kensho, Dōgen's "dropping off body and mind", and Dzogchen rigpa as "neither subject nor object". SOD's first falsifier (L101) is traditions concluding that "the *asymmetry between subject and object* itself disappears", and L111 says "none of these conditions has been met. Cross-cultural convergence continues to support the discovery reading."

   The Map's own `topics/japanese-philosophy-of-mind-kyoto-school` adds Nishida's pure experience, "experience prior to the subject-object division" (L30–L38), and leaves its "dissolve or dodge" question open (L70–L72). SOD links neither the Kyoto page nor any mention of Nishida. A defensible reply exists: the reports are of states, and SOD L63 notes that "even emptiness is discovered *by* a contemplative *of* experience". SOD has to make that reply, though, rather than cite the collapse as confirmation.

3. **SOD L57 states the asymmetry in the phenomenal-concept strategist's terms.** "These are not two ways of looking at the same thing—they are two genuinely different kinds of access, which is why the explanatory gap persists." The phenomenal concepts strategy grants the two kinds of access and uses them to explain the gap physicalistically. SOD never engages it, although `concepts/phenomenal-concepts-strategy` exists. Two kinds of access do not by themselves give two kinds of thing.

4. **SRP's Relation section runs ahead of its body.** At L146, "Dualism predicts this structure". The same paragraph says physicalist frameworks "struggle with strong-form cases, because on the standard account inspection is supposed to be information-preserving". On a physicalist account attention is itself a neural process that modulates what it selects, so inspection-induced change is expected rather than anomalous. CE L129 concedes the parallel point. L148 says MQI "is the tenet most illuminated" and that measurement and introspection "both involve consciousness acting at the indeterminacy boundary". That drops L130's "This is speculative". L156 says competing frameworks "must explain away" the shape. L70, "Both readings confirm that self-reference sits at the centre of any account of consciousness", also overclaims.

5. **SRP L94's Steyvers & Peters gloss** attributes to the paper the Map's own thesis ("blind spots the system cannot detect, because detection would require the compromised capacity"). The abstract fetched today does not support that reading (see Verification). The reference entry also lacks volume and DOI.

## Expansion Opportunities

### High Priority

#### Structure versus character in POP (fold, topics/ at cap)
- **Builds on**: POP L64, L74; `concepts/inverted-qualia` L74–L84 and L169–L175; `concepts/structuralism-about-phenomenal-character` (created 10-13, which calls itself "the Map's most direct rival to dualism" and cites Kawakita et al. 2025 at L76 and L138).
- **Would address**: POP's strongest rival is absent from the page. Structuralism says an experience *is* its place in a quality space, so isomorphic quality spaces share character (Lyre, cited at structuralism L106), and the "which property" question gets an answer from structure. The 2020s cross-subject alignment programme ("Is my 'red' your 'red'?") gives structuralism an empirical arm. POP's falsifier L94 ("functional role fixing phenomenal character") is the nearest entry, and it is not the same view.
- **Estimated scope**: About 250–400 words inside POP, with no new page.
- **Tenet alignment**: Dualism (the page defends irreducibility against its most direct rival); Bidirectional Interaction (difference-detection, per Concern 1).

#### Nondual reports and pure experience in SOD (fold, topics/ at cap)
- **Builds on**: SOD L63, L73, L101, L111; `topics/comparative-phenomenology-of-meditative-traditions` L75–L87, L161; `topics/japanese-philosophy-of-mind-kyoto-school` L30–L38, L70–L72.
- **Would address**: Concern 2. This is also the best philosophical opportunity on SOD. The discovery thesis meets a rival "discovery" thesis, that the split is derivative of a prior unity, and the Map already has a page that treats that rival with care.
- **Estimated scope**: About 200–350 words.
- **Tenet alignment**: Dualism; Occam's Razor Has Limits. The Kyoto page L86 reads the same datum into opposite metaphysics.

### Medium Priority

#### Recalibrate SRP's Relation section to CE's standard (refine)
- **Builds on**: CE L113, L127–L135; `positions/voids-as-evidence` [P-V2](/positions/voids-as-evidence/#p-v2) (L51).
- **Would address**: Concerns 4 and 5, plus the uncited "roughly five orders of intentionality" claim (L110) and the Libet reading (L100).
- **Estimated scope**: Mostly length-neutral rewording.

#### Earlier discoverers in SOD's history
- SOD L47 says "The full articulation required Descartes". `topics/the-hard-problem-in-non-western-philosophy` has a section titled "Avicenna's Flying Man: The Cogito Six Centuries Early" (L67), and Augustine's *si fallor, sum* (*De civitate Dei* XI.26) is a well-known anticipation that no content page quotes (`grep -i 'si fallor'` over topics/concepts/voids/apex = 0). Both strengthen the "discovered" claim. The independence caution in `topics/epistemology-of-convergence-arguments` L92 applies: the diachronic pattern is "at least partly a canon-formation selection artefact", and Avicenna reached the Latin West. Folded into the SOD task as an optional locus.

### Ideas for Later
- **Yogācāra's grasper–grasped thesis.** The doctrine that the duality of *grāhaka* and *grāhya* is imagined (*parikalpita*) is the most explicit philosophical argument, in any tradition the Map covers, that the subject-object split is constructed. `concepts/yogacara-alaya-vijnana-storehouse-consciousness` does not mention it (grep `grahya|grāhya|grahaka|grāhaka` = 0). It would be a fold into that page after the SOD task, if the SOD repair wants a citable Buddhist constructionist. Sources were not checked this run.
- **The private-language reply to POP's testimony bottleneck.** If words for qualities are learned "through public criteria" (POP L72), Wittgenstein's beetle-in-the-box conclusion is that the private object "drops out of consideration as irrelevant". `concepts/problem-of-other-minds` L76–L80 engages the Wittgensteinian dissolution and POP does not. A one-paragraph fold, best done with the structuralism fold because both press the same "idle character" objection.
- **CE at headroom 51.** Nothing should be added to CE. Any future change there should be net-neutral.

## Cross-Linking Suggestions

Directed body-link counts within the wing, frontmatter excluded (`awk` body split + `grep -c "\[\[slug[]|#]"`): SRP→CE 0 (frontmatter only), SRP→SOD 0, SRP→POP 0, CE→SRP 1, CE→SOD 2, CE→POP 0, SOD→SRP 2, SOD→CE 2, SOD→POP 0, POP→SRP 0, POP→CE 0, POP→SOD 0.

| From | To | Reason |
|------|-----|--------|
| POP | `concepts/inverted-qualia#the-detectability-objection` and its Bidirectional section | POP's central example is inverted qualia; the link already exists (L16, L44) but the page ignores the commitment there (Concern 1) |
| POP | `concepts/structuralism-about-phenomenal-character` | The most direct rival to POP's thesis; 0 links either way |
| POP | `topics/the-subject-object-distinction-as-philosophical-discovery` | POP's L80–L82 self/other asymmetry is SOD's L57 "two genuinely different kinds of access" applied between subjects |
| POP | `topics/constitutive-exclusion` (or `voids/intrinsic-nature-void`) | POP L74's "language ... encodes relations and functions rather than intrinsic qualities" is CE L77's structure/intrinsic-nature split applied to testimony |
| POP | `concepts/problem-of-other-minds` (Hogan twins, L182) | POP L95 names the Hogan twins with no link or reference |
| SRP | `topics/the-subject-object-distinction-as-philosophical-discovery` | SRP L90 ("The subject is the limit of the experiential field") is SOD L53's first discovery; SOD links SRP twice, SRP never links back |
| SRP | `topics/constitutive-exclusion` | Frontmatter only. The body host is L122–L124, where SRP lists instantiations; CE L75 already marks the boundary between the two pages (self versus encountered) |
| SOD | `topics/japanese-philosophy-of-mind-kyoto-school` | Nishida's pure experience is the rival discovery thesis (Concern 2) |
| SOD | `concepts/phenomenal-concepts-strategy` | Concern 3 |
| SOD | `topics/the-hard-problem-in-non-western-philosophy` (Avicenna section) | L47's "required Descartes" |

## New Concept Pages Needed

None. concepts/ and topics/ are full, and every gap found here has a host page already: POP for structuralism and the private-language reply, SOD for nondual reports and earlier discoverers, the Yogācāra page for the grasper–grasped thesis.

## Tasks Minted

Three P3 `refine-draft` tasks are inserted immediately above `## Completed Tasks` in `obsidian/workflow/todo.md`. Each carries assess-first licence and its own headroom figure.

1. POP: re-scope the barrier to *which* quality rather than *whether* qualities differ, per inverted-qualia's Bidirectional commitment; engage structuralism and Kawakita et al. 2025; link the wing. File `obsidian/topics/consciousness-and-the-problem-of-other-properties.md`.
2. SOD: answer the nondual-collapse and Nishida evidence against falsifier 1 and L111; engage the phenomenal concepts strategy at L57; optional Avicenna locus at L47. File `obsidian/topics/the-subject-object-distinction-as-philosophical-discovery.md`.
3. SRP: bring the Relation section to CE's [P-V2](/positions/voids-as-evidence/#p-v2) standard; assess the Steyvers & Peters gloss; link SOD and CE in the body. File `obsidian/concepts/self-reference-paradox.md`.

CE gets no task.