---
ai_contribution: 100
ai_generated_date: 2026-11-02
ai_modified: 2026-11-02 09:03:07+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-02
date: &id001 2026-11-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-02 09:03:07+00:00
modified: *id001
related_articles:
- '[[phenomenology-of-philosophical-disagreement]]'
title: Pessimistic Review - 2026-11-02 - Phenomenology of Philosophical Disagreement
topics: []
---

# Pessimistic Review

**Date**: 2026-11-02
**Content reviewed**: `obsidian/topics/phenomenology-of-philosophical-disagreement.md`

- **Selection.** No drafts exist. Measured by content, 132 of 923 section articles are named in no `reviews/pessimistic-*.md` file. After removing articles named in any review dated 2026-10-26 or later, articles with `last_deep_review` in that window, and the five pages the driver excluded, 53 remain. This one has the oldest `modified` date (2026-02-17). A search on the full title also finds 0 pessimistic reviews. The six pessimistic reviews that contain the phrase "philosophical disagreement" use it as an ordinary phrase about other articles.
- **Length.** `analyze_length` gives 2,998 words, status `ok`. The topics thresholds are soft 3,000 and hard 4,000, and the gate fires at `>=`. Headroom against the hard gate is 4,000 − 1 − 2,998 = **1,001 words**.
- **History.** Created 2026-02-17 by expand-topic. It has had six deep reviews (02-21, 03-19, 04-20, 05-31, 06-26, 09-14). The body is unchanged since the 09-14 deep review (last commit `9143c56ca6`). This is its first pessimistic review.
- **Lenses no prior pass ran.** None of the six deep reviews mentions the conservative position on cognitive phenomenology (`grep -c -i -F conservative` = 0 across all six). None checked that the opening paragraph still matches the body after the 02-21 repair. That repair added the hard-problem and zombie steps to the body to fix the leap from "felt texture" to "irreducible". `git log -S` shows the lead clause that carries the original leap is unchanged since creation (`af83298074`).

## Executive Summary

The article's best material holds up. That includes the three-part phenomenal signature, the opponent triad, and the 09-14 conciliationist section, which is faithful to its source (Elga was checked against the author's PDF on 09-14). The weaknesses are in what the article says the phenomenology proves.

- **The opening paragraph overclaims.** It still states the 2026-02-17 thesis: "the felt impossibility of occupying an opposing framework provides evidence for the irreducibility of conscious experience". The body has since retreated. It says the phenomenology "does not *by itself* establish irreducibility", and the datum it actually uses is that the textures exist, not that occupation fails. So the move from a limit on access (epistemic) to a claim about what consciousness is (metaphysical) survives only in the paragraph an LLM reader is most likely to keep.
- **The one positive argument never meets the conservative reply.** The argument is that the textures show thinking itself has phenomenal character. On the Map's own definition in [cognitive-phenomenology](/concepts/cognitive-phenomenology/), the conservative grants emotional accompaniments of thought, and most of the textures named here (relief, homecoming, discomfort, vertigo) are emotional.
- **Two smaller defects.** The inline citation credits Pitt (2004) with a causal-significance thesis his paper does not argue, and the article's own third point disclaims it. The bias hypothesis is dismissed as "self-undermining" on grounds that apply equally to the article's own preferred explanation.

**Findings: 2 High, 4 Medium, 4 Low.**

## Critiques by Philosopher

### The Eliminative Materialist (Patricia Churchland)

"You describe 'relief', 'homecoming', 'vertigo', 'friction' and 'reaching' and call them phenomenal events. They are folk-psychological labels for the affective and attentional dynamics of keeping a belief: error signals while a model fails to settle, reward when the default model resumes. At L102 you concede that persistent disagreement about consciousness suggests 'introspective access is partial (we do not fully see what we are)'. Yet L100 relies on that same introspection to certify that these textures belong to thought itself and resist functional duplication. Your own cognitive-phenomenology page lists 'Philosophers disagree about whether cognitive phenomenology exists' as evidence that introspection is unreliable. Introspecting harder on the feeling of disagreement cannot settle a disagreement about whether thinking has phenomenology."

The eliminativist redescription itself is bedrock and covered by a stability note. The tension between L102 and L100 is new, and it bears on Issue 2.

### The Hard-Nosed Physicalist (Daniel Dennett)

"Your 'one specific respect' (L112) is the hard problem with a new example. On your reasoning, pain, red and the smell of coffee each 'constitutes evidence that conscious experience has qualitative character beyond what functional description captures'. Disagreement adds nothing. At L48 you settle the functionalist objection by appeal to 'a difference anyone who has tried to "think like" an opponent and felt the effort recognises'. I have tried, and what I recognise is effort, which a functional story explains. You need a difference between effort and something beyond effort, and that is exactly what is in dispute."

The model/inhabit objection itself is settled per the stability notes. The point that the L112 argument is not specific to disagreement is new (Issue 7). The L48 wording goes to the Language table.

### The Quantum Skeptic (Max Tegmark)

This persona finds little to grip, because the article makes no quantum claim. L104 says the felt framework "structures the space within which reasoning occurs" at "a level more fundamental than explicit reasoning". Read causally under the Bidirectional Interaction tenet, that claims consciousness shapes reasoning over the months and years a philosophical commitment lasts. The Map would have to cash that out as an accumulation of minimal quantum-level biases. The article does not owe that account, but its phrase "the causal-work reading is the natural one" should not suggest the reading comes cheap. This is noted for completeness and is not raised as an issue.

### The Many-Worlds Defender (David Deutsch)

"L60 says 'Hard problems in physics eventually yield.' The measurement problem has come back in every generation since the 1920s with undiminished force, and your No Many Worlds tenet takes a side in it. So one of two things holds. If interpreting quantum mechanics counts as philosophy, then 'philosophical' just means 'still unresolved'. The persistence you treat as a fact about consciousness is then a selection effect: questions that get settled leave philosophy and become science. Otherwise physics has disagreements as persistent as yours, and the contrast at L56–L60 fails."

The article gives only two "standard explanations" of persistence, complexity and bias. It never mentions the selection-effect explanation. `grep -c -i -F` returns 0 for "selection", "spun off", "spin off", "graduat" and "tractable". See Issue 6.

### The Empiricist (Karl Popper's Ghost)

The 09-14 conciliationist section correctly concedes that the phenomenology cannot falsify conciliationism, and that is settled. What remains are the article's own generalisations about phenomenology, none of which comes with a test:

- "It does not occur when one considers views one merely has not examined" (L50) is a universal claim about everyone's experience, with no source.
- "Disagreements about policy, taste, or empirical questions lack this phenomenal texture" (L52) is contradicted by the source the article takes its central term from. Fogelin's two worked cases of deep disagreement are the morality of abortion and affirmative-action quotas (Issue 5).

### The Buddhist Philosopher (Nagarjuna)

The reading of the snap as attachment remains deferred per the stability notes and is not re-flagged. One further point stays inside the article's own terms. The convergence fantasy (L80) says "ways of experiencing cannot be transferred through argument alone". Contemplative traditions say the same of their own views, and they answer it with practice rather than argument. The article's diagnosis implies a route to understanding an opponent that does not run through argument, and the article never explores it. This would be an enhancement and is not counted as a defect.

## Critical Issues

### Issue 1: The opening paragraph still makes the leap the body repaired on 2026-02-21 (High; Priority 1)

- **File**: `obsidian/topics/phenomenology-of-philosophical-disagreement.md`
- **Location**: L40, final clause: "and that the felt impossibility of occupying an opposing framework provides evidence for the irreducibility of conscious experience."
- **Problem**: The article's thesis sentence, the one an LLM is most likely to quote, has two defects.
  - **(a) Epistemic to metaphysical.** "Felt impossibility of occupying" describes a limit on how much of another's framework one mind can take up, which is an epistemic or psychological fact. "Irreducibility of conscious experience" is a claim about what consciousness is, which is metaphysical. The body never argues for that bridge. Its argument at L100 runs from the *existence* of the textures to "thinking itself has qualitative character". It then says it needs "an additional argument" (the hard problem and the zombie scenario) to reach irreducibility, and states that the phenomenology "does not *by itself* establish irreducibility". The failure to occupy plays no part in that argument, since a successful inhabitation would be just as phenomenal.
  - **(b) A repair that never reached the lead.** The 02-21 deep review recorded: "Logical leap from 'disagreement has felt texture' to 'consciousness is irreducible': Added intermediate argumentative steps". That fix was additive and went into the body only. `git log -S` shows the lead clause unchanged since `af83298074`, the creation commit.
- **Recommendation**: Restate the lead at the body's level of confidence (Priority 1).

### Issue 2: The cognitive-phenomenology inference never meets the conservative reply (High; Priority 2)

- **Location**: L100: "The incomprehension, the failed inhabitation, the rubber-band snap: these are phenomenal events, not just cognitive operations. Their existence supports the view that thinking itself has qualitative character…"
- **Problem**:
  - **The conservative grants the data.** The Map's own [cognitive-phenomenology](/concepts/cognitive-phenomenology/) page defines the opposing view: "**Conservatism**: No. Apparent cognitive phenomenology derives from accompanying sensory states. Strip away inner speech, imagery, and emotional response, and nothing phenomenal remains." Most of the textures this article names are emotional or close to sensory: "relief, recognition, homecoming" (L50), "discomfort" and "unsettlement" (L78), "vertigo" (L94), "friction" (L76), and "reaching or stretching" (L48). A conservative accepts all of them as emotional accompaniments of thinking and denies that they show thinking *itself* has phenomenal character.
  - **The counterfactual is a false dichotomy.** L100 says: "If philosophical understanding were purely propositional — a set of beliefs without felt character — then disagreement would lack the phenomenal texture described here". Against a conservative this fails, because the textures can exist even if thought has no phenomenology of its own.
  - **The cited source widens the gap.** Pitt's thesis is that phenomenology individuates content. His abstract (checked; see the Source-Check Tally) argues "there's something it's like consciously to think that p, which is distinct from what it's like consciously to think that q". Relief and discomfort feel the same whatever the content, so they are the wrong kind of evidence for Pitt's thesis.
  - **Two further aggravations.** L102 concedes that introspective access may be partial. The Map's concept page lists persistent disagreement about cognitive phenomenology as an objection from unreliable introspection.
  - **Counts.** In this article, "conservative" and "affective" each occur 0 times. Across all six prior deep reviews, "conservative" occurs 0 times.
- **Why it matters**: The article's only pro-dualist claim, at L112 in Relation to Site Perspective, rests on this inference. If the conservative can absorb the textures, the "one specific respect" shrinks to the generic hard problem (see Issue 7).
- **Recommendation**: Name the conservative reply and concede the emotional textures. Then rest the case for proprietary phenomenology on the textures whose object is understanding itself:
  - incomprehension, which parallels Pitt's minimal-pair argument ("sentences read without and with understanding");
  - the epistemic emotions, which the Map's concept page already argues "resist reduction to sensory accompaniments" (section `Evidence from Epistemic Emotions and the Amplification Thesis`).

  This is Priority 2.

### Issue 3: "real and causally significant" goes beyond both sources and contradicts the article's third point (Medium; Priority 3)

- **Location**: L100: "suggests that [cognitive-phenomenology](/concepts/cognitive-phenomenology/) is real and causally significant — a thesis defended on independent grounds by Pitt (2004), who argues that occurrent thoughts have proprietary phenomenal character, and Strawson (1994), who insists that the reality of conscious experience is the most certain thing we know."
- **Problem**:
  - **(a) Attribution.** Pitt 2004 (Crossref 10.1111/j.1933-1592.2004.tb00382.x, *PPR* 69(1), 1–36; abstract via OpenAlex) argues that thinking different contents feels different. It says nothing about causal efficacy. The article's own gloss on Strawson concerns the reality of experience, which is not a causal claim either. So "causally significant" is attributed to two authors who, on the article's own description, do not assert it.
  - **(b) Internal contradiction.** Nothing in point one argues for causal significance. Point three (L104) grants the epiphenomenalist's common-cause reply and closes "without establishing on its own that the felt quality is what does the work". Point one asserts what point three disclaims.
- **Recommendation**: Delete "and causally significant" (Priority 3).
- **Related low-severity point, not prioritised**: the Strawson gloss is about the reality of experience rather than cognitive phenomenology. The Map's own concept page credits Strawson with the foreign-language "understanding experience" argument, which is the gloss this sentence needs. The driver can make that swap if wanted.

### Issue 4: The bias hypothesis is dismissed for a symmetry the article's own explanation shares (Medium; Priority 4)

- **Location**: L62: "If biases explain the other side's error, they equally explain one's own conviction. The hypothesis dissolves philosophical positions into psychology without remainder, a self-undermining move."
- **Problem**:
  - Applying a debunking explanation evenly to both sides does not undermine it. It recommends suspending judgement on both, which is Feldman's conciliationist verdict as reported at L84.
  - The article's own preferred explanation at L64 is just as symmetric: "Each position trains a kind of perception, and the perception vindicates the position."
  - At L86 the article concedes its own snap "may be framework-generated — exactly what the conciliationist predicts".

  So the article rejects a rival for a feature its own account shares, and the later section accepts the consequence this sentence calls self-undermining. The real objection to the bias hypothesis is the one L66 makes ("This runs deeper than confirmation bias"): the hypothesis does not predict the specific shape the phenomenon takes.
- **Recommendation**: Replace the "self-undermining" sentence with two points: what even application implies, and the objection about the phenomenon's specific shape. Point forward to the conciliationist section (Priority 4).

### Issue 5: Policy disagreements are excluded, against the cited source's own examples (Medium)

- **Location**: L52: "Disagreements about policy, taste, or empirical questions lack this phenomenal texture."
- **Problem**:
  - **Fogelin's own cases are policy disputes.** The article takes "deep disagreement" from Fogelin (1985), whose two worked cases are moral and policy disputes. Checked in the 1985 *Informal Logic* 7(1) PDF from informallogic.ca (OJS article 2696): "The morality of abortion has been a favorite topic", and "I shall consider one case of a deep disagreement, the dispute over affirmative action quotas". He diagnoses both as clashes of framework propositions. Such disputes "persist even when normal criticisms have been answered" and are "immune to appeals to facts".
  - **The article's own mechanism predicts the texture there.** The article explains the texture by framework clash: "the positions involve different ways of experiencing what counts as intelligible" (L52), plus framework-generated evidence (L64–66). By that mechanism, the texture should appear wherever a Fogelin-style framework clash appears, including these policy disputes.
  - **How this differs from the 09-14 Stability Note.** That note warned against building a contradiction between L52 and *Elga's* political cases, because Elga addresses epistemic structure rather than felt texture. This finding is about the article's own mechanism and the source of its central term. It does not allege a contradiction with Elga.
- **Recommendation** (off the Priority List): OLD `Disagreements about policy, taste, or empirical questions lack this phenomenal texture.` (`grep -c -F` = 1) → NEW `Disagreements about taste, or about empirical questions that evidence can settle, usually lack this phenomenal texture; policy disputes acquire it when, as in Fogelin's own examples of abortion and affirmative-action quotas, they turn on clashing framework commitments.` **+26 words.** The conclusions specific to consciousness at L98–L104 survive. Point two rests on the disputants' shared access to the subject matter, not on the texture being exclusive to philosophy.

### Issue 6: The persistence argument omits the selection-effect explanation and overstates physics (Medium)

- **Location**: L56 "Empirical disputes resolve."; L60 "Hard problems in physics eventually yield."
- **Problem**: The list of "standard explanations" that are "unsatisfying" (L58–L62) gives complexity and bias. It leaves out a familiar third: questions that become decidable leave philosophy. On that view, persistence is partly a selection effect and says less about consciousness than the article claims. L60 is also awkward for the Map, whose Tenet 4 takes a side on how to interpret quantum mechanics, a dispute that has lasted since the 1920s.
- **Recommendation** (off-list): Add the selection effect as a third standard explanation, and say why it does not cover the consciousness case. The reason is the L102 argument: the disputants share access to the subject matter. Soften L60 to "Many hard problems in physics eventually yield." Estimated +40–60 words; exact text is not drafted here. A possible support for the contemporary-non-convergence claim at L56 is the PhilPapers surveys (Bourget & Chalmers). That is a lead to verify at the publisher before citing, not a checked reference.

### Issue 7: The "one specific respect" is not specific to disagreement, and the materialist dilemma leaves out a posteriori physicalism (Low)

- **Location**: L112: "favours dualism over materialism in one specific respect: the very existence of the phenomenal textures described here … constitutes evidence that conscious experience has qualitative character beyond what functional description captures. A materialist account must either explain these phenomenal textures in purely physical terms … or deny that the textures are genuinely phenomenal".
- **Problem**:
  - Any phenomenal state supports the same inference, so this respect is the hard problem applied to a new example.
  - The dilemma also omits the type-B physicalist. That view grants the textures are phenomenal and identifies them with physical states without any a priori explanation. `grep -c -i -F` returns 0 for "type-B" and 0 for "phenomenal concept". The illusionist is not the only alternative.
  - The Occam paragraph (L114) inherits the gap. The type-B materialist's story about *why disagreement persists* (bias, complexity) does not "explain away" the felt character. This point is about which views the dilemma covers, not about the Occam calibration that the stability notes settled.
- **Recommendation** (off-list): Once Issue 2 is fixed, say plainly that this is the hard problem applied to cognitive textures. Add the a posteriori physicalist as a third option, with a pointer to the Map's existing treatment.

### Issue 8: Point three opens by assuming what it closes by disclaiming (Low)

- **Location**: L104 opens "Third, philosophical disagreement illustrates the [bidirectional interaction](/tenets/#bidirectional-interaction) between consciousness and cognition" and closes "without establishing on its own that the felt quality is what does the work".
- **Problem**: "Illustrates" assumes the very interaction that the end of the paragraph declines to establish. The tenet is also about consciousness and the *physical* world, not "consciousness and cognition".
- **Recommendation** (off-list): Change "illustrates" to "bears on" (0 words).

### Issue 9: A "not X. It is Y." construction at L92 (Low)

- **Location**: L92: "the disagreement is not about a shared body of evidence. It is about what constitutes evidence in the first place."
- **Problem**: This matches the construct at `writing-style.md:446` exactly, and that rule has no exemption for contrasts that do analytical work. The 05-31 and 06-26 deep reviews kept it on purpose ("Editing it would be oscillation"). It is reported here for the driver to decide, and the earlier choice is not treated as settling it.
- **Recommendation** (off-list): Change it to "the disagreement concerns what constitutes evidence in the first place, not a shared body of it." **−4 words.**

### Issue 10: The materialist's evidence is described as produced by attention (Low)

- **Location**: L64: "The materialist's attention to the causal structure of cognition produces the "data" (the tight correlation between brain states and mental states) that supports materialism."
- **Problem**: For the dualist, attention plausibly does produce the vividness datum. Brain–mind correlation is different: it is a public, third-person finding that dualists accept too, and interactionism predicts it. Calling it "produced" by a way of attending recasts neuroscience as a trained perception, which builds a false symmetry into the framework-dependence thesis.
- **Recommendation** (off-list): Change the second "produces" to "foregrounds" (0 words).

## Counterarguments to Address

### Introspection is asked to settle a dispute about introspection

- **Current content says**: The textures are phenomenal events (L100), and persistent disagreement suggests introspective access is partial (L102).
- **A critic would argue**: The cognitive-phenomenology debate is itself a long-running disagreement between introspectors. Using introspection to classify the textures assumes an answer to the question that the article's own second point raises.
- **Suggested response**: Fold this into the fix for Priority 2. Rest the proprietary case on contrast data rather than on direct introspective classification, and say so. The contrast data are Pitt's minimal pairs, and incomprehension as understanding that is absent.

### Persistence as selection effect

See Issue 6. The Map's available reply is that people disputing consciousness share access to the subject matter. That separates this case from questions that persist only because they cannot yet be decided.

### Failed inhabitation as a lack of skill

- **A critic would argue**: Some philosophers do change sides, as the article's own L50 pointer to framework change admits. So inhabitation is a skill some people manage, and failing at it reflects training rather than anything about consciousness.
- **Suggested response**: The article already concedes that framework change is possible. One sentence noting that the *successful* case is just as phenomenal would close the loop and support the restated lead in Priority 1.

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| "It does not occur when one considers views one merely has not examined. It occurs specifically with views one has tried and failed to occupy." | L50 | A universal claim about phenomenology; needs a hedge ("typically") or a source |
| "Disagreements about policy, taste, or empirical questions lack this phenomenal texture." | L52 | Contradicted by Fogelin's own cases (Issue 5) |
| "Empirical disputes resolve." / "Hard problems in physics eventually yield." | L56, L60 | Too general; the dispute behind the Map's own Tenet 4 is a counterexample (Issue 6) |
| "is real and causally significant — a thesis defended … by Pitt (2004) … and Strawson (1994)" | L100 | Neither attribution supports causal significance (Issue 3) |
| "persist despite millennia of argument" | L56 | Optional: survey data on contemporary non-convergence (lead only; see Issue 6) |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "a difference anyone who has tried to "think like" an opponent and felt the effort recognises" (L48) | Claims universal agreement against an opponent who denies the point | "a difference many who have tried to "think like" an opponent report" |
| "… provides exactly that" (L100, of the hard problem) | Too strong for a contested conceivability argument | "is the Map's candidate for it" |
| "Hard problems in physics eventually yield." (L60) | Too general | "Many hard problems in physics eventually yield." |
| "ways of experiencing cannot be transferred through argument alone" (L80) | Stated as settled | "ways of experiencing seem not to transfer through argument alone" |
| "illustrates the" bidirectional interaction (L104) | Assumes the conclusion | "bears on the" |

## Calibration Lenses

- **Epistemic/metaphysical equivocation**: **Fires** at L40 (Issue 1). It does not fire at L102, which stays epistemic ("introspective access is partial … communicative transfer is lossy").
- **Reasoning mode**: The conciliationist engagement (L84–86) remains honest, as the 09-14 review found. The dismissal of the bias hypothesis (L62) is a weak objection made in the opponent's own terms, and the article's later section undercuts it (Issue 4). The materialist dilemma (L112) leaves out an option (Issue 7). No case was found of rejecting an opponent by appeal to tenet conflict while presenting it as a refutation.
- **Label leakage**: 0 hits for all seven forbidden labels (`direct-refutation`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification`, `Evidential status`, `tenet-register`). The intensifier the style guide restricts also scores 0.
- **Altered-state symmetry**: The gate does not fire. Counts for the supportive-cluster terms: psychedel 0, psilocybin 0, near-death 0, NDE 0 as a whole word, terminal lucidity 0, cessation 0, mystical 0, out-of-body 0. The 11 case-insensitive hits for "NDE" are substrings of words such as "understanding" and "independent".
- **Style**: One "not X. It is Y." construction (Issue 9). The lead does put the thesis first, but in its overclaimed form (Issue 1).

## Source-Check Tally

| Source | Check | Result |
|--------|-------|--------|
| Pitt 2004 | Crossref DOI 10.1111/j.1933-1592.2004.tb00382.x; OpenAlex abstract | Metadata correct (*PPR* 69(1), 1–36; full title "The Phenomenology of Cognition Or What Is It Like to Think That P?"). The thesis is that phenomenology individuates content; there is no causal-significance claim (Issue 3) |
| Fogelin 1985 | Crossref 10.22329/il.v7i1.2696; PDF from informallogic.ca (article 2696, galley 2137) | Worked examples are abortion and affirmative-action quotas (Issue 5). Metadata as cited (*Informal Logic* 7(1)) |
| Christensen 2007, Elga 2007, Feldman 2006, Kelly 2005/2010, Strawson 1994, Chalmers 1996 | Not re-checked | Carried over from the 09-14 and 06-26 ledgers; no complaint raised against them here |

## Strengths (Brief)

- The three-part signature (incomprehension, attempted inhabitation, rubber-band snap) is a genuine contribution to phenomenology and gives the article its structure.
- The 09-14 conciliationist section is the strongest argued passage on the page. It refuses the Map the steadfast reading and states Elga's peerhood reply faithfully. Keep it whole.
- The self-application in Relation to Site Perspective ("The Map cannot claim immunity") is honest, and it is what keeps the Priority 4 fix coherent.
- The unfalsifiability paragraph at L68 correctly separates refuting a position from assessing it.

## Not Re-Flagged (settled)

- The eliminative-materialist redescription, which is bedrock (02-21 onward).
- The functionalist model/inhabit objection, which is addressed (02-21). Only the L48 wording goes to the Language table.
- Unfalsifiability from within a framework, which is addressed (02-21).
- The self-application concession, which is a feature (05-31).
- The Buddhist attachment reading, which is deferred (02-21 onward).
- The Occam calibration, which is honest (05-31, 06-26). Issue 7 concerns which views the dilemma covers, not calibration.
- The conciliationist section, which is faithful to its source, including the Elga reply (09-14). It is not re-flagged in either direction.
- All nine reference entries in the 09-14 ledger, the Feldman page range 199–215, and the distinction between T. Kelly and E. Kelly / S. D. Kelly.
- The 09-14 note that L52 is compatible with Elga. Issue 5 rests on different grounds, set out in its "How this differs" bullet.

## Priority List (at most 4)

All four edits are in `obsidian/topics/phenomenology-of-philosophical-disagreement.md`; sync mirrors them to `hugo/content/topics/`.

- **String checks.** Every OLD string was checked with `grep -c -F` against the Obsidian file and occurs **exactly once**.
- **Word deltas.** Deltas use `tools.curate.length.count_words`, which splits on whitespace, so a piped wikilink also counts the spaces inside its anchor.
- **Length.** The article is 2,998 words now. The topics hard limit is 4,000 and the gate fires at `>=`, so headroom is **1,001**. With all four edits it becomes **3,090**, leaving headroom of **909**.
- **Soft threshold.** The total crosses the 3,000 soft threshold. That has no gate consequence, but the status changes from `ok` to `soft_warning`. Item 2's short variant brings the total to 3,077.

1. **Issue 1 (High): restate the lead at the body's level of confidence.**
   - OLD (`grep -c -F` = 1): `and that the felt impossibility of occupying an opposing framework provides evidence for the irreducibility of conscious experience.`
   - NEW: `and that the felt textures of trying and failing to occupy an opposing framework are evidence that thinking itself has phenomenal character, with the hard problem supplying the further step to irreducibility.`
   - **+14 words.**
   - Defect: the thesis sentence leaps from an epistemic limit to a metaphysical claim, and the 02-21 repair to the body never reached it.

2. **Issue 2 (High): answer the conservative reply.**
   - OLD (`grep -c -F` = 1): `these are phenomenal events, not just cognitive operations. Their existence supports`
   - NEW: `these are phenomenal events, not just cognitive operations. A conservative about cognitive phenomenology can grant all of them and file the relief, discomfort and vertigo as emotional accompaniments of thought, so the case for proprietary character rests on the textures whose object is understanding itself: the incomprehension, and the [[cognitive-phenomenology#Evidence from Epistemic Emotions and the Amplification Thesis|epistemic emotions]] of understanding failing. Their existence supports`
   - **+53 words.**
   - Short variant (**+40**): `these are phenomenal events, not just cognitive operations. A conservative about cognitive phenomenology can file the relief, discomfort and vertigo as emotional accompaniments of thought; the case for proprietary character rests on the incomprehension and the [[cognitive-phenomenology#Evidence from Epistemic Emotions and the Amplification Thesis|epistemic emotions]] of understanding failing. Their existence supports`
   - Defect: the article's only positive argument assumes the liberal view against an opponent who accepts every named texture as an emotion.
   - The anchor targets the heading at `concepts/cognitive-phenomenology.md:160`. It uses the heading-text form, as the article's existing `[[intentionality#Phenomenal Intentionality Theory|…]]` does.

3. **Issue 3 (Medium): drop the causal claim that neither source makes.**
   - OLD (`grep -c -F` = 1): `is real and causally significant — a thesis defended`
   - NEW: `is real — a thesis defended`
   - **−3 words.**
   - Defect: Pitt 2004 (abstract checked) and the article's own Strawson gloss support "real" only, and L104 disclaims the causal claim.

4. **Issue 4 (Medium): replace the "self-undermining" dismissal.**
   - OLD (`grep -c -F` = 1): `they equally explain one's own conviction. The hypothesis dissolves philosophical positions into psychology without remainder, a self-undermining move.`
   - NEW: `they equally explain one's own conviction; applied evenly, the hypothesis recommends suspending judgement on both sides, the conciliationist verdict [[#The Snap Before the Conciliationist|taken up below]]. What it leaves unexplained is why the bias takes the specific shape of failed inhabitation rather than neglect of evidence.`
   - **+28 words** (+24 without the anchor link).
   - Defect: the article rejects a rival for a symmetry that its own L64 explanation shares and that its L86 concession accepts.
   - The same-page anchor form `[[#Heading|label]]` is already used in 42 files across topics/ and concepts/.

**Next if a fifth slot opens:** Issue 5, with exact text given above (+26).