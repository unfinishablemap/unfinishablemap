---
title: Research Notes - Practical Knowledge and Knowledge Without Observation
created: 2026-09-14
draft: false
ai_contribution: 100
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-14
ai_modified: 2026-09-14T21:24:43+00:00
target_section: concepts
harvest_date: 2026-08-20
harvest_source: "optimistic-2026-08-20-agency-self-wing"
---

# Research: Practical Knowledge and Knowledge Without Observation

**Date**: 2026-09-14 (harvested 2026-08-20 from `reviews/optimistic-2026-08-20-agency-self-wing.md`, "Practical knowledge and knowledge without observation", Medium priority)
**Search queries used**:
- Anscombe Intention 1957 "knowledge without observation" §8 §28 "cause of what it understands"
- Setiya "Practical Knowledge" Ethics 2008; Setiya "Knowledge of Intention" Ford Hornsby Stoutland 2011
- Moran "Anscombe on 'Practical Knowledge'" Royal Institute of Philosophy Supplement 2004
- Paul "How We Know What We're Doing" 2009; Schwenkler "Understanding 'Practical Knowledge'" 2015
- Fourneret Jeannerod 1998 limited conscious monitoring; Synofzik Vosgerau Newen 2008 comparator
- Pickard 2004 body sense; Grünbaum perception knowledge of action; Kietzmann error in action
- crossref API metadata for every journal article and chapter below; curl + `pdftotext` on Speaks (guide to §§1-31), Setiya 2008 (author's PDF), Moran 2004 (author's PDF), Özaltun 2016 (Klesis)

## Assessment First: Is This Worth Covering, and Where?

**Verdict: worth covering, as a standalone concept article, with three small in-place discharges alongside it.** Reasons, in order of weight:

1. **The gap is real and narrower than the reviewer said.** On current text (grep 2026-09-14, live `obsidian/` excluding `reviews/` and `workflow/`), the doctrine that an agent knows what she is doing *without observation* is treated in exactly one live article: [[philosophy-of-action-under-dualism]], one paragraph under "The Non-Causal Alternative", and that paragraph immediately subordinates the epistemic claim to the causal one (formal vs efficient cause). [[direction-of-fit]] uses the same passage of *Intention* (the shopping list, §32) but for the belief/desire asymmetry, never the knowledge claim. The reviewer's "two other files" do not exist as doctrine-mentions: the seventeen other `Anscombe` hits are her critique of Lewis (six files), her translation of Wittgenstein (four), and research notes. The eight `non-observational` hits are Zahavi's pre-reflective self-awareness ([[self-and-self-consciousness]], [[embodied-consciousness]]) and Brentano's inner perception ([[observation-and-measurement-void]]), adjacent but not this doctrine. The three `practical knowledge` hits outside the action article are O'Regan and Noë's sensorimotor know-how, a different sense of the phrase (see the slug note below). The string `knowledge without observation` has zero hits anywhere in the corpus.
2. **The Map's own introspection taxonomy has a hole exactly here.** [[phenomenal-authority-and-first-person-evidence]] ("Competing Models of Introspective Knowledge") lists acquaintance, inner sense, transparency and inferentialism, then declares introspection *sui generis*. It omits the agentialist model (Moran 2001; O'Brien 2007), on which one central class of self-knowledge is had by *doing* rather than by *looking*, and it never mentions the one case in which non-perceptual, non-inferential first-person knowledge is a textbook datum rather than a phenomenological claim. That is a first-person-epistemology omission, not a philosophy-of-action one, which is why the concept belongs in `concepts/` rather than as a subsection of the action article.
3. **The physicalist counter-account is already half-installed, on the wrong question.** The comparator / efference-copy model appears in sixteen live articles ([[volitional-control]], [[anarchic-hand-and-action-ownership]], [[phenomenology-of-agency-vs-passivity]] and others), always as a mechanism of the *feeling* of agency. No article asks whether it also explains the agent's *knowledge* of what she is doing. Lukitsch (2025) states the link outright: the non-perceptual sense-of-agency literature "is conceptually rooted in Anscombe's idea of *practical knowledge*". The seam the reviewer named (Anscombean epistemology vs the comparator) is therefore genuinely untapped, and the Fourneret and Jeannerod (1998) result gives it an empirical edge (below).
4. **Cap and length.** `concepts/` measured 326/360 on 2026-09-14 via `tools.evolution.state.count_section_files` (the task note's "318/320" is stale). No cap pressure. In-place discharge alone is not viable: the nearest hosts are [[introspection]] (3,635 words against a 3,500 hard threshold), [[phenomenal-authority-and-first-person-evidence]] (4,704 against 4,000) and [[volitional-control]] (already at the topic threshold); each is at or over its ceiling, so the passages below are one or two sentences with piped wikilinks, not paragraphs.

**Route:** `/expand-topic` a concept article at `obsidian/concepts/practical-knowledge-without-observation.md` (target 2,000-2,800 body words; concept thresholds are 2,500 soft / 3,500 hard, and the hard number itself trips). Then apply the three insert-ready passages under "In-Place Discharges" as part of the expand-topic integration pass, since the article will otherwise be born an orphan.

**Slug note.** `practical-knowledge` alone is ambiguous in this corpus: three live articles use "practical knowledge" for sensorimotor know-how (O'Regan and Noë). Setiya (2008, 388) opens by separating the two senses. Keep the full slug so the wikilink names the Anscombean sense.

## Executive Summary

Anscombe's *Intention* (1957; 2nd ed. 1963) claims that an agent's knowledge of her own intentional action is "knowledge without observation": she knows what she is doing neither by perceiving her body nor by inferring from evidence, and this knowledge is "the cause of what it understands", in the Aristotelian-Thomist sense that it *gives* the description under which what happens is the execution of an intention. The doctrine was largely dormant until Velleman (1989), Falvey (2000) and above all Moran (2004) and Setiya (2008) revived it; the 2011 Harvard volume (Ford, Hornsby and Stoutland) made it a live research programme. The contemporary debate splits four ways: cognitivists (Velleman, Setiya) treat the knowledge as a belief built into intention; inferentialists (Paul 2009) say we infer what we are doing from what we intend; perception-friendly readers (Pickard 2004; Grünbaum 2011, 2013) give body sense or vision a justificatory role; Anscombeans (Thompson 2011; Haddock 2011; Rödl 2007; Schwenkler 2015) insist the knowledge is practical in form and partly constitutive of the action. The empirical seam is the comparator model of the sense of agency, which the sense-of-agency literature explicitly roots in Anscombe, and Fourneret and Jeannerod's (1998) demonstration that agents keep accurate knowledge of the action under its intended description while remaining unaware of large deviations in the movement that executes it. For the Map, the doctrine supplies a first-person epistemic channel that is neither perception nor inference (Tenet 1), sits naturally on the volitionist reading of Tenet 3 (what the agent knows is what her trying is doing), and, read honestly, sharpens rather than dissolves the [[agency-void]]'s verification circularity: practical knowledge covers the *what*, never the causal *how*.

## Key Sources

### Anscombe, *Intention* (1957; 2nd ed. 1963; Harvard reprint 2000)
- **Editions (verified)**: 1st ed. Oxford: Basil Blackwell, 1957 (US: Cornell UP). 2nd ed. Oxford: Blackwell, 1963 (Setiya 2008 n.1 cites exactly this). Reprint Cambridge, MA: Harvard University Press, 2000, ISBN 9780674003996, which Moran (2004 n.1) cites as "originally published by Basil Blackwell, 1957". Moran's page references to the 2000 printing (pp. 13, 52-3, 87) coincide with Setiya's to the 1963 Blackwell (pp. 52, 57), so the Harvard reprint carries the second-edition pagination. Cite as "Anscombe 1957/1963" with 2nd-ed. pages.
- **Type**: Monograph
- **Key points, with grep-verified wording** (all via quoting sources; the primary text was not opened):
  - §8, p. 13: the class of intentional actions is picked out via "a particular class of things which are true of a man: namely the class of things which he knows without observation" (quoted in Moran 2004, 45).
  - §8, p. 13: "a man usually knows the position of his limbs without observation. It is without observation, because nothing shews him the position of his limbs; it is not as if he were going by a tingle in his knee, which is the sign that it is bent and not straight" (quoted in Speaks's guide and Moran 2004).
  - §28-§29: the knowledge extends beyond bodily movement to what happens in the world; §29, p. 52: "I do what happens", glossed at pp. 52-3: "when the description of what happens is the very thing which I should say I was doing, then there is no distinction between my doing and the thing's happening" (quoted in Moran 2004).
  - §32, p. 57 (SEP: pp. 56-57): the shopping list; when a man "is simply not doing what he [intends to be doing] ... the mistake is not one of judgement but of performance" (quoted in Setiya 2008 n.28). Özaltun (2016) traces the Theophrastus remark through §32 and §45 ("the mistake is in the performance, not in the judgment").
  - §48, p. 87: practical knowledge is "the cause of what it understands", "rather than being derived from objects known" (pp. 87-8); "it is the agent's knowledge of what he is doing that gives the descriptions under which what is going on is the execution of an intention" (p. 87); "It is necessarily the rare exception for a man's performance in its more immediate descriptions not to be what he supposes" (p. 87). All quoted in Moran 2004. The SEP glosses "cause" here as *formal* not efficient.
- **Tenet alignment**: Neutral on Tenet 1 in intent (Anscombe is a Wittgensteinian hostile to inner-object pictures of mind; she must not be conscripted as a dualist). Tension with Tenet 3 only on the non-causal reading, already handled in [[philosophy-of-action-under-dualism]].

### Moran, "Anscombe on 'Practical Knowledge'" (2004)
- **Citation (crossref)**: *Royal Institute of Philosophy Supplement* 55: 43-68; also as ch. in Hyman and Steward (eds), *Agency and Action*, CUP 2004, pp. 43-68. DOI 10.1017/S1358246100008638.
- **Type**: Paper
- **Key points**: The essay that reopened the topic. Moran presses the question that Anscombe's readers keep sliding past: not "how can I do what happens" but "how Anscombe can claim that my knowledge that I am doing something can be non-observational" when painting a wall yellow "so patently involves" the eyes. His answer distinguishes practical knowledge from both a proprioceptive reduction (category A, knowledge of one's own body) and the observational knowledge that "is merely an aid" to performance; the non-observational content is the description under which the doing is *mine*, given by the intention, with observation serving execution rather than knowledge.
- **Tenet alignment**: Aligns with Tenet 1's interest in an irreducible first-person channel; explicitly not a claim about mental substance.

### Setiya, "Practical Knowledge" (2008) and "Knowledge of Intention" (2011)
- **Citations (crossref)**: *Ethics* 118(3): 388-409, DOI 10.1086/528781; "Practical Knowledge Revisited", *Ethics* 120(1): 128-137 (2009), DOI 10.1086/606000; "Knowledge of Intention" in Ford, Hornsby and Stoutland (eds), *Essays on Anscombe's Intention*, Harvard 2011, pp. 170-197, DOI 10.4159/harvard.9780674060913.c7; collected with a new "Anscombe on Practical Knowledge" in *Practical Knowledge: Selected Essays*, OUP 2016.
- **Key points**: Setiya's opening sentence separates "the spontaneous 'knowledge without observation' that, according to Elizabeth Anscombe and Stuart Hampshire, we have of what we are doing intentionally" from "knowledge how to perform a certain task". His view is *cognitivist and causalist*: intending to φ involves believing one is φ-ing (or will), the belief is formed "spontaneously, not on the basis of empirical evidence", and it counts as knowledge because it is grounded in the agent's *knowing how*, which makes the belief reliably self-fulfilling. Crucially for the Map, this shows practical knowledge is compatible with a causal theory of action: one need not buy Anscombe's non-causalism to keep her epistemology.
- **Tenet alignment**: Neutral. Supports the Map's layered reading in [[philosophy-of-action-under-dualism]] (epistemic claim detachable from the anti-causal claim).

### Ford, Hornsby and Stoutland (eds), *Essays on Anscombe's Intention* (2011)
- **Citation (NDPR header, verified)**: Harvard University Press, 2011, 324 pp., ISBN 9780674051027. Relevant chapters (crossref pages): McDowell, "Anscombe on Bodily Self-Knowledge", pp. 128-146; Haddock, "The Knowledge That a Man Has of His Intentional Actions", pp. 147-169; Setiya, pp. 170-197; Thompson, "Anscombe's *Intention* and Practical Knowledge", pp. 198-210; Rödl, "Two Forms of Practical Knowledge".
- **Key points** (via Clark's NDPR review): McDowell: bodily self-knowledge "is not gotten through the operation of any perceptual faculty" and is "knowledge of oneself as self, rather than as other". Haddock: "For me to know without observation what I am doing intentionally, nothing more is required than that I be doing it intentionally", the knowledge being a "simple consequence of the actuality of its objects". Thompson restricts the necessity claim to "ordinary" cases involving checking and repetition.
- **Tenet alignment**: McDowell's "as self, rather than as other" is the closest thing in this literature to the Map's [[mine-ness]] vocabulary, but it is Kantian-Wittgensteinian, not dualist.

### Paul, "How We Know What We're Doing" (2009)
- **Citation**: *Philosophers' Imprint* 9, no. 11 (2009). Volume and number taken from the journal's own URL identifier (`phimp/3521354.0009.011`); crossref returned no record. Full text not opened (PhilPapers 403); thesis from the abstract as reproduced by PhilPapers and search.
- **Key points**: Against cognitivism. Intentions "do not embody non-observational knowledge, but they do provide the evidential basis for it": we know what we are doing by *inferring* from what we intend. The inferentialist rival to Anscombe.
- **Tenet alignment**: If right, the "neither perception nor inference" channel collapses into inference; the Map's article must state this rival fairly.

### Schwenkler, "Non-Observational Knowledge of Action" (2012); "Understanding 'Practical Knowledge'" (2015); *Anscombe's Intention: A Guide* (2019)
- **Citations (crossref)**: *Philosophy Compass* 7(10): 731-740, DOI 10.1111/j.1747-9991.2012.00513.x (the survey to hand a writer). *Philosophers' Imprint* 15 (2015): issue number not confirmed (crossref and PhilArchive give volume only). *Anscombe's Intention: A Guide*, OUP 2019: ch. 3 "Knowledge without Observation" pp. 93-116, ch. 6 "Practical Knowledge" pp. 155-200, DOIs 10.1093/oso/9780190052027.003.0004 and .0006.
- **Key points**: The 2015 paper reads "practical knowledge" through Aquinas as thought that "aims at production" of what lies in the agent's power, and questions whether the thesis that agential knowledge is practical entails that an agent *always* knows non-observationally what she is doing. Useful because it lets the Map keep the constitutive claim without the implausible universal.
- **Tenet alignment**: Neutral.

### Pickard, "Knowledge of Action without Observation" (2004); Grünbaum (2011, 2013); Kietzmann (2020)
- **Citations (crossref)**: Pickard, *Proceedings of the Aristotelian Society* 104: 203-228, DOI 10.1111/j.1467-9264.2004.00153.x. Grünbaum, "Perception and non-inferential knowledge of action", *Philosophical Explorations* 14(2): 153-167 (2011), DOI 10.1080/13869795.2011.569746; "Seeing what I am Doing", *Philosophy and Phenomenological Research* 86(2): 295-318 (online 2012, print 2013), DOI 10.1111/j.1933-1592.2012.00647.x. Kietzmann, "Practical knowledge and error in action", *PPR* 103(3): 586-606 (online 2020, print 2021), DOI 10.1111/phpr.12732.
- **Key points**: Pickard's *body-sense model*: the non-observational knowledge of basic action rests on proprioceptive experience of one's body "from the inside", which monitors the action as it unfolds. Grünbaum: in object-directed action, perception plays a *justificatory but non-inferential* role. Kietzmann: cases of practical error force us both to affirm and deny practical knowledge; his solution applies the form/matter framework to action.
- **Tenet alignment**: Pickard is the sharpest deflation available to a physicalist: relocate the "channel" into an ordinary bodily sense. Fourneret and Jeannerod (below) cut against a *pure* body-sense reading.

### Fourneret and Jeannerod, "Limited conscious monitoring of motor performance in normal subjects" (1998)
- **Citation (crossref)**: *Neuropsychologia* 36(11): 1133-1140, DOI 10.1016/S0028-3932(98)00006-2.
- **Type**: Experimental paper
- **Key points**: Subjects traced sagittal lines on a tablet with the hand hidden behind a mirror showing a computer-drawn trace; on perturbed trials the trace was rotated by 2-10 degrees. Subjects corrected smoothly, displacing the hand in the opposite direction, yet "grossly underestimated the hand deviation" when asked. Read with Anscombe: the agent's knowledge of what she is doing *under its intended description* ("drawing a straight line to the target") stayed accurate while her knowledge of the bodily movement that executed it did not. That is "I do what happens" holding at the description level and failing at the movement level, in one trial.
- **Tenet alignment**: Double-edged. It is the best empirical illustration of knowledge without observation being *of the action-as-intended* rather than of the body; it also refutes, as a systematic finding, Anscombe's p. 87 claim that divergence "in its more immediate descriptions" is "necessarily the rare exception". An honest article carries both halves.

### Synofzik, Vosgerau and Newen (2008); Lukitsch (2025)
- **Citations (crossref)**: "Beyond the comparator model: A multifactorial two-step account of agency", *Consciousness and Cognition* 17(1): 219-239, DOI 10.1016/j.concog.2007.03.010. Lukitsch, O., "An integral forward model of agency experience in thought and action", *Frontiers in Psychology* 16: 1524904 (2025), DOI 10.3389/fpsyg.2025.1524904.
- **Key points**: Synofzik et al. split a non-conceptual *feeling* of agency from a conceptual *judgement* of agency and argue the comparator explains neither on its own. Lukitsch (§2.3) roots the non-perceptual conception of the sense of agency in Anscombe by name, and (§4.2) treats agency as felt "as an immediate experience tied to the very process of generating and refining predictions *qua* motor commands", a "non-observational, efferent conception".
- **Tenet alignment**: This is the physicalist's candidate for *what the channel is*: efferent prediction, not perception or inference. The Map's reply, already worked out for the feeling in [[anarchic-hand-and-action-ownership]] ("what the mechanism is a mechanism *of*"), transfers to knowledge: a forward model yields a sub-personal match signal, and the question is how a match signal becomes the agent's *knowing that she is φ-ing under a description*.

## Major Positions

### Anscombean constitutivism
- **Proponents**: Anscombe; Thompson (2011); Haddock (2011); Rödl (2007); McDowell (2011); Schwenkler (2015, 2019); Kietzmann (2020).
- **Core claim**: Knowledge of what one is doing is practical in form; it partly constitutes the action as intentional under a description ("the cause of what it understands"). Error is located in performance, not judgement.
- **Relation to site tenets**: The literature's cleanest case of first-person knowledge that is neither perceptual nor inferential (Tenet 1 interest), but *not* a dualist doctrine and the Map must not say it is. Its non-causal wing conflicts with Tenet 3; its epistemic core does not.

### Cognitivism about intention
- **Proponents**: Velleman (1989); Setiya (2008, 2011, 2016).
- **Core claim**: Intending to φ involves believing one is (or will be) φ-ing; the belief is self-fulfilling and grounded in know-how, so it is knowledge without prior evidence, inside a causal theory of action.
- **Relation to site tenets**: Congenial: the epistemic doctrine survives inside a causalist framework, which the Map's volitionist hybrid needs.

### Inferentialism
- **Proponents**: Paul (2009); Carruthers (2011) at the general-self-knowledge level (already engaged in [[phenomenal-authority-and-first-person-evidence]]).
- **Core claim**: We know what we are doing by inferring it from knowledge of what we intend.
- **Relation to site tenets**: The deflation the Map most needs to answer, since it removes the "third channel". Reply: the inference starts from knowledge of the intention, itself neither perceived nor inferred; the channel is relocated, not removed.

### Perception-involving accounts
- **Proponents**: Pickard (2004); Grünbaum (2011, 2013); O'Brien (2007).
- **Core claim**: Bodily awareness (Pickard) or vision (Grünbaum) plays a non-inferential justificatory role, so the knowledge is not "without observation" in the strict sense.
- **Relation to site tenets**: The physicalist's tidiest story for basic action. Fourneret and Jeannerod (1998) show the knowledge tracks the intended description, not the proprioceptive facts, which limits the body-sense reduction.

### Forward-model / comparator accounts
- **Proponents**: Frith (1992); Blakemore, Wolpert and Frith (2002); Synofzik, Vosgerau and Newen (2008) as critics-from-within; Lukitsch (2025).
- **Core claim**: Agentive awareness arises from efferent prediction matched against reafference: non-observational but wholly sub-personal.
- **Relation to site tenets**: Already conceded as *mechanism* in [[anarchic-hand-and-action-ownership]] and [[volitional-control]]. It explains the feeling and its dissociations; it does not by itself deliver knowledge under a description, and Synofzik et al. treat the judgement level as a separate step.

## Key Debates

### Is practical knowledge a belief?
- **Sides**: Cognitivists (Velleman, Setiya) yes; Anscombeans (Moran, Thompson, Haddock) no, it is a contrasting state of mind (Setiya 2008 n.28 records the disagreement).
- **Core disagreement**: Whether "the mistake is not one of judgement but of performance" (p. 57) shows the state has a different direction of fit from belief, or whether a failed execution involves both a performance error and a false belief.
- **Current state**: Ongoing; the [[direction-of-fit]] article already carries the asymmetry the Anscombean side leans on.

### Does the agent *always* know what she is doing?
- **Sides**: Strong reading (Haddock: nothing more is required than doing it intentionally) vs restricted readings (Thompson: ordinary cases; Schwenkler 2015: the entailment fails).
- **Core disagreement**: The status of the p. 87 "rare exception" clause. Fourneret and Jeannerod (1998) make the exception systematic at the level of movement while leaving it rare at the level of the intended description.
- **Current state**: Unresolved; the split-level reading is the Map's best-supported option.

### Knowledge of the what versus knowledge of the how
- **Sides**: All parties agree that practical knowledge does not extend to the neural or causal route by which the action is executed; they disagree whether that matters.
- **Core disagreement**: For the Map it matters directly. [[agency-void]] ("The Verification Circularity") and [[philosophy-of-action-under-dualism]] ("Deviance is relocated, not removed") both hold that the agent cannot verify from inside that her trying, rather than a deviant parallel process, produced the movement. Practical knowledge is knowledge of the description under which the trying is the trying it is; it is silent on the route.
- **Current state**: This is the article's most valuable Map-specific contribution, and it is a *limit* claim, not a support claim.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1957 | Anscombe, *Intention* (2nd ed. 1963) | §8 "knowledge without observation"; §48 "the cause of what it understands" |
| 1989 | Velleman, *Practical Reflection* | Cognitivism: intention as self-fulfilling belief |
| 1998 | Fourneret and Jeannerod | Agents unaware of executed deviations while knowing the intended action |
| 2001 | Moran, *Authority and Estrangement* | Agentialist self-knowledge: the self as agent, not spectator |
| 2004 | Moran; Pickard | The two poles of the revival: constitutive vs body-sense |
| 2008 | Setiya; Synofzik et al. | Cognitivist knowledge-in-intention; feeling vs judgement of agency |
| 2009 | Paul | Inferentialist rival |
| 2011 | Ford, Hornsby and Stoutland (eds) | The doctrine becomes a research programme |
| 2025 | Lukitsch | Sense-of-agency model explicitly rooted in Anscombe |

Hampshire (1959, *Thought and Action*) and Donnellan (1963, "Knowing What I Am Doing", *J. Phil.* 60) are named as precursors by Setiya and Moran; neither was independently verified.

## Potential Article Angles

1. **The third channel (recommended lead).** Open with the datum: there is a kind of first-person knowledge that is neither perception nor inference, and philosophy of action has spent twenty years trying to reduce it. Present the four reductions (cognitivist, inferentialist, body-sense, forward-model) fairly, then the Map's reading: each reduction either relocates the channel (inference from intention needs non-inferential knowledge of intention) or explains the feeling rather than the knowing (comparator). Tenet 1 gains a datum, not a proof. Front-load the Fourneret and Jeannerod split-level result.
2. **What the trying knows.** On the Map's volitionist hybrid, the basic act is a trying; practical knowledge is the agent's knowledge of what her trying is doing, under a description. Tenet 3 gets an epistemology to go with its metaphysics. State the limit in the same breath: the knowledge stops at the description and never reaches the causal route, which is exactly the residue [[agency-void]] records.
3. **The comparator and the description.** A shorter, sharper angle: take the concession already made in [[anarchic-hand-and-action-ownership]] and ask what a prediction-match signal would have to add to become knowledge *that I am φ-ing*. Synofzik et al.'s own two-step split does the work. Risk: overlaps [[volitional-control]]; use only as a section within angle 1.

When writing the article, follow `obsidian/project/writing-style.md` for named-anchor forward references, background-vs-novelty decisions (LLMs know Anscombe's §8; front-load the split-level reading and the tenet mapping), a "Relation to Site Perspective" section, and truncation-resilient ordering. Do **not** use "This is not X. It is Y." Do **not** call Anscombe a dualist, an interactionist, or a friend of the Map; she is a Wittgensteinian and her formal-cause claim belongs to the non-causal tradition the Map only partly accepts.

## In-Place Discharges (insert-ready; apply during expand-topic integration)

These are sized for hosts at their length ceilings. Each is one sentence and uses a piped wikilink so it installs a reciprocal at near-zero word cost. The link is written here as ⟦target|display⟧ rather than in double square brackets, because `research/` is a synced tree and the sync's link validator rejects a bare target that does not yet exist (it would block the push). Convert ⟦ ⟧ to double square brackets when installing, and only after the concept article exists.

1. **[[phenomenal-authority-and-first-person-evidence]]**, "Competing Models of Introspective Knowledge", after the Inferentialism paragraph and before "The Map's position": `**Agentialism** (Moran 2001; O'Brien 2007) adds a fifth model for one class of states: an agent knows what she is doing by doing it, the ⟦practical-knowledge-without-observation|knowledge without observation⟧ that Anscombe made the mark of intentional action, and that no perceptual or inferential model reproduces.` Add Moran, R. (2001). *Authority and Estrangement: An Essay on Self-Knowledge*. Princeton University Press to References. (Note: the article's existing reference list should be checked for a Moran entry first; the corpus-wide "Moran" hits are Driskell, Copper and Moran 1994, a different author.)

2. **[[philosophy-of-action-under-dualism]]**, "The Non-Causal Alternative", replace the clause "Anscombe emphasised *practical knowledge*: the agent knows what she is doing without observation or inference, and this non-observational knowledge partly constitutes the action as intentional." with `Anscombe emphasised ⟦practical-knowledge-without-observation|practical knowledge⟧: the agent knows what she is doing without observation or inference, and this non-observational knowledge partly constitutes the action as intentional.` Length-neutral. Optionally add to "Deviance is relocated, not removed": `Practical knowledge does not close this gap: it is knowledge of what the trying is doing under a description, never of the route by which it does it.`

3. **[[anarchic-hand-and-action-ownership]]**, "The Comparator Account, Conceded in Full", after "The question is what the mechanism is a mechanism *of*—and on that the imaging is silent.": `The same question returns for knowledge rather than feeling: a prediction-match signal is not yet the agent's ⟦practical-knowledge-without-observation|knowing that she is φ-ing⟧ under a description, and Synofzik et al. (2008) themselves separate the feeling of agency from the judgement.` Synofzik et al. is already cited in the corpus only at [[penfield-interactionist-dualism]]; add the reference if the host lacks it.

## Gaps in Research

- **Primary text not opened.** Every Anscombe quotation above is grep-verified in a quoting source (Moran 2004, Setiya 2008, Speaks's guide, Özaltun 2016), not in *Intention* itself. Two independent quoting sources agree on the pagination for pp. 52 and 87; p. 13 and p. 57 rest on one source each (Moran; Setiya). The article writer should open the Harvard 2000 printing for §8, §29, §32 and §48 before quoting.
- **Paul 2009 and Schwenkler 2015 full texts** returned HTTP 403 (PhilPapers/PhilArchive); theses are from abstracts. Schwenkler 2015's issue number within volume 15 is unconfirmed.
- **Hampshire 1959** is included only on Setiya's authority.
- **Velleman 1989 and O'Brien 2007** were verified as publications, not read; their specific arguments are summarised from publisher and review descriptions.
- **Empirical follow-ups** to Fourneret and Jeannerod (Slachevsky et al. 2003, *Neuropsychologia* 41(6): 655-665, on prefrontal patients' conscious monitoring, DOI 10.1016/S0028-3932(02)00225-7) were found but not read; they could sharpen the "knowledge of the what, not the how" section with a lesion dissociation.
- **The physicalist reply to the relocation argument** (that inference from intention presupposes non-inferential knowledge of intention) has a literature in the transparency-of-belief tradition (Byrne 2005, already cited in the phenomenal-authority article) that this note did not survey.

## Citations

- Anscombe, G. E. M. (1957). *Intention*. Oxford: Basil Blackwell. 2nd ed. 1963; reprinted Cambridge, MA: Harvard University Press, 2000 (ISBN 9780674003996). https://www.hup.harvard.edu/books/9780674003996
- Blakemore, S.-J., Wolpert, D. M. & Frith, C. D. (2002). Abnormalities in the awareness of action. *Trends in Cognitive Sciences*, 6(6), 237-242. (Already cited in [[volitional-control]]; not re-verified here.)
- Falvey, K. (2000). Knowledge in Intention. *Philosophical Studies*, 99(1), 21-44. https://doi.org/10.1023/A:1018775307559
- Ford, A., Hornsby, J. & Stoutland, F. (eds) (2011). *Essays on Anscombe's Intention*. Cambridge, MA: Harvard University Press. https://ndpr.nd.edu/reviews/essays-on-anscombe-s-intention/
- Fourneret, P. & Jeannerod, M. (1998). Limited conscious monitoring of motor performance in normal subjects. *Neuropsychologia*, 36(11), 1133-1140. https://doi.org/10.1016/S0028-3932(98)00006-2
- Grünbaum, T. (2011). Perception and non-inferential knowledge of action. *Philosophical Explorations*, 14(2), 153-167. https://doi.org/10.1080/13869795.2011.569746
- Grünbaum, T. (2013). Seeing what I am Doing. *Philosophy and Phenomenological Research*, 86(2), 295-318. https://doi.org/10.1111/j.1933-1592.2012.00647.x
- Haddock, A. (2011). "The Knowledge That a Man Has of His Intentional Actions". In Ford, Hornsby & Stoutland (eds), pp. 147-169. https://doi.org/10.4159/harvard.9780674060913.c6
- Kietzmann, C. (2021). Practical knowledge and error in action. *Philosophy and Phenomenological Research*, 103(3), 586-606 (online 2020). https://doi.org/10.1111/phpr.12732
- Lukitsch, O. (2025). An integral forward model of agency experience in thought and action. *Frontiers in Psychology*, 16, 1524904. https://doi.org/10.3389/fpsyg.2025.1524904
- McDowell, J. (2011). Anscombe on Bodily Self-Knowledge. In Ford, Hornsby & Stoutland (eds), pp. 128-146. https://doi.org/10.4159/harvard.9780674060913.c5
- Moran, R. (2001). *Authority and Estrangement: An Essay on Self-Knowledge*. Princeton, NJ: Princeton University Press. https://press.princeton.edu/books/paperback/9780691089454/authority-and-estrangement
- Moran, R. (2004). Anscombe on 'Practical Knowledge'. *Royal Institute of Philosophy Supplement*, 55, 43-68 (also in Hyman & Steward (eds), *Agency and Action*, CUP). https://doi.org/10.1017/S1358246100008638
- O'Brien, L. (2007). *Self-Knowing Agents*. Oxford: Oxford University Press. https://global.oup.com/academic/product/self-knowing-agents-9780199592043
- Paul, S. K. (2009). How We Know What We're Doing. *Philosophers' Imprint*, 9(11). https://quod.lib.umich.edu/p/phimp/3521354.0009.011
- Pickard, H. (2004). Knowledge of Action without Observation. *Proceedings of the Aristotelian Society*, 104, 203-228. https://doi.org/10.1111/j.1467-9264.2004.00153.x
- Rödl, S. (2007). *Self-Consciousness*. Cambridge, MA: Harvard University Press. (SEP bibliography; not independently verified.)
- Schwenkler, J. (2012). Non-Observational Knowledge of Action. *Philosophy Compass*, 7(10), 731-740. https://doi.org/10.1111/j.1747-9991.2012.00513.x
- Schwenkler, J. (2015). Understanding "Practical Knowledge". *Philosophers' Imprint*, 15. https://philarchive.org/rec/SCHUQK
- Schwenkler, J. (2019). *Anscombe's Intention: A Guide*. Oxford: Oxford University Press. Ch. 3 (pp. 93-116), ch. 6 (pp. 155-200). https://doi.org/10.1093/oso/9780190052027.003.0006
- Setiya, K. (2008). Practical Knowledge. *Ethics*, 118(3), 388-409. https://doi.org/10.1086/528781
- Setiya, K. (2009). Practical Knowledge Revisited. *Ethics*, 120(1), 128-137. https://doi.org/10.1086/606000
- Setiya, K. (2011). Knowledge of Intention. In Ford, Hornsby & Stoutland (eds), pp. 170-197. https://doi.org/10.4159/harvard.9780674060913.c7
- Setiya, K. (2016). *Practical Knowledge: Selected Essays*. Oxford: Oxford University Press. https://global.oup.com/academic/product/practical-knowledge-9780190462925
- Setiya, K. Intention. *Stanford Encyclopedia of Philosophy* (revised edition; consulted 2026-09-14). https://plato.stanford.edu/entries/intention/
- Synofzik, M., Vosgerau, G. & Newen, A. (2008). Beyond the comparator model: A multifactorial two-step account of agency. *Consciousness and Cognition*, 17(1), 219-239. https://doi.org/10.1016/j.concog.2007.03.010
- Thompson, M. (2011). Anscombe's *Intention* and Practical Knowledge. In Ford, Hornsby & Stoutland (eds), pp. 198-210.
- Velleman, J. D. (1989). *Practical Reflection*. Princeton, NJ: Princeton University Press. https://philpapers.org/rec/VELPR
- Özaltun, E. (2016). Practical Knowledge of What Happens: Reading §45 of *Intention*. *Klesis*, 35. https://www.revue-klesis.org/pdf/Klesis-Anscombe-04-Eylem-Ozaltun-Practical-Knowledge-What-Happens-Reading-45.pdf
