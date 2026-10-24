---
ai_contribution: 100
ai_generated_date: 2026-10-24
ai_modified: 2026-10-24 00:53:23+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[psychophysical-laws]]'
created: 2026-10-24
date: &id001 2026-10-24
description: Adversarial read of concepts/psychophysical-laws as a hub. It turns an
  explanatory gap into non-identity, misreports Chalmers's stance, and keeps a Stapp
  test and two tenet readings that its spokes have since withdrawn.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-24 00:53:23+00:00
modified: *id001
related_articles: []
title: Pessimistic Review - 2026-10-24 - Psychophysical Laws and Coupling
topics:
- '[[hard-problem-of-consciousness]]'
---

# Pessimistic Review

**Date**: 2026-10-24 (00:37–00:53 UTC)
**Content reviewed**: `obsidian/concepts/psychophysical-laws.md` ("Psychophysical Laws and Coupling").

**Why this target.** There are no drafts. I ranked `topics/` and `concepts/` pages by how many distinct content pages link to them in their bodies (sources: topics, concepts, apex, voids, positions, tenets, arguments; frontmatter excluded). I then checked each page's pessimistic coverage by content: the title, heading, `**Content reviewed**`/`**Article**` lines and `subject_articles` of all 629 pessimistic review files. Coverage of the top of the ranking:
- Every page above the 102-link mark has at least one pessimistic review as primary target, except `concepts/witness-consciousness` (122). That page was edited on 2026-10-23, so it is excluded.
- `concepts/mental-causation-and-downward-causation` (102) has never been a primary target, but it is the `File:` of an open P3 refine-draft (todo L2634), so it is excluded.
- Every page between 102 and 59 links has at least one pessimistic review naming it on a title, heading, target or reviewed-files line (scripted check).
- At 59 links there is a tie. `topics/phenomenal-authority-and-first-person-evidence` is a named secondary locus in an open P3 (todo L2864). It is also over its hard limit (4,519 / 4,000), so any fix would have to cut words.
- `concepts/psychophysical-laws` is the other page at 59. It has never been a primary target. `pessimistic-2026-03-10-psychophysical-laws.md` matches it by filename only: its Content-reviewed line is the sibling `topics/psychophysical-laws-bridging-mind-and-matter`. The 06-26, 07-29 and 10-03 pessimistic reviews mention this page only in body text or frontmatter.

On the brief's other exclusions: the target was not created or deep-reviewed in the last 7 days (last deep review 2026-07-17). It was not edited on 10-23 or 10-24 (last edit 2026-10-13, a cross-link). No open or blocked task names it; a regex for the bare slug above `## Completed Tasks` hits only the `anomalous-monism-and-the-denial-of-strict-psychophysical-laws` slug.

It is a hub. Its frontmatter lists 22 concepts, its Further Reading lists 25 pages, and 59 pages link into it. That is the shape in which spokes go on correcting themselves after the hub has stopped being read.

**Length.** `analyze_length` gives **3,493** words: prose 2,891, Further Reading 282, References 320. The concepts hard limit is 3,500 and the gate is `>=`, so the headroom is 3,500 − 1 − 3,493 = **6 words**. Every Priority Fix below has a measured cost (`tools.curate.length.count_words`). Together they come to **−4** (end state 3,489). Two duplicate sentences are cut to pay for Fix 2.

**Line numbers** are file lines from `cat -n`, frontmatter included. Every quoted target string was grep-verified (`grep -cF` = 1 each).

**Prior reviews read first.** I read the 2026-07-17 deep review and the 2026-06-20 deep review's Stability Notes, which list six bedrock disagreements. I also read the 2026-08-24 optimistic wing review (its L42 praise of the supervenience/selection table) and the tenet checks that flagged this page (09-02, 09-04, 09-06, 10-10, 10-12).

None of the findings below re-raises a bedrock item.
- Fix 2's L217 sub-item is a logic point, not "phenomenology skepticism".
- The L100 note is the Map's own 10-11 correction left half-applied, not "functionalist critique of haecceity".

The 07-17 review called the page "content-converged". Since then it has had 21 refine-drafts and one cross-link install (07-30 to 10-13). Each was a narrow string fix, and the spokes went on moving. The findings are about that drift.

**Spokes spot-checked for verdict drift:**
- `concepts/epiphenomenalism` L98
- `concepts/explanatory-gap` L68
- `concepts/dualism` L146 and L162 (10-23 refines `0be02dca6a`, `6224e8a9ce`)
- `concepts/stapp-quantum-mind` L84, L106, L146, L180, L182
- `concepts/entanglement-binding-hypothesis` L44, L48
- `concepts/libet-experiments` L89–L95
- `concepts/agent-causation` L168
- `topics/mathematical-structure-of-the-consciousness-physics-interface` L94
- `topics/psychophysical-laws-bridging-mind-and-matter` L70, L88, L207, L211, L236
- [tenets/tenets.md](/tenets/) L69, L93, L145, L147

**Source checked at the publisher:** Chalmers, "Consciousness and its Place in Nature" (consc.net/papers/nature.html; *Blackwell Guide to the Philosophy of Mind*, 2003). I downloaded it raw, and each quoted string greps at count 1.

This is a report only. No article, todo, state or hugo content file was touched. The changelog was prepended and a sync was run.

## Executive Summary

The page is honest about mechanism. Its supervenience/selection table, its per-family objections and its "What's Not Selectable" section are good. It fails where its argument meets the opposition.

- **L124 turns an explanatory gap into non-identity.** It says the hard problem "shows" that phenomenal properties resist identification with physical ones. The Map's own explanatory-gap page says Type-B physicalism predicts the gap. The dualism hub (10-23) now puts the Type-B dispute "close to bedrock". This is the epistemic/metaphysical equivocation the skill rates critical.
- **Chalmers's stance is misreported four times** (L78, L114, L217, L260): "tends toward epiphenomenalism", a "supervenience-only framework". In 2003 Chalmers gave "some credence to each" of interactionism, epiphenomenalism and type-F monism, and found type-F "the most appealing". The page's own L106–L108 also credit him with a collapse law in which "consciousness causes collapse".
- **Two spoke withdrawals have not reached the hub.**
  - L223 offers, as "a better test" of Stapp's Zeno mechanism, a prediction that `stapp-quantum-mind` L182 says a classical account shares.
  - L193 says no quantum mechanism has been proposed for unity. Its own table (L191) and `entanglement-binding-hypothesis` (Marshall 1989, Orch OR) say otherwise.
- **The Relation section has two tenet misreadings, flagged and never tasked.** L239 reads Tenet 2 as bandwidth economy (flagged 10-10 and 10-12). L243 has Tenet 5 "justify" an expansion and then argues that the Map's picture is simpler (flagged 09-02, 09-04 and 09-06).

## Critiques by Philosopher

### The Eliminative Materialist

"Your L124 trilemma says the relation cannot be identity, cannot be coincidence, so it 'must be a *sui generis* lawful relationship'. The first horn rests on 'the hard problem shows'. The hard problem shows that *we* cannot derive experience from physics. That is a fact about our concepts, the very folk concepts I expect neuroscience to replace. Your L68 is careful ('not logically entailed'; 'If they are ontologically basic'). L124 drops both qualifications. And L133 calls the placebo evidence 'striking granularity' of meaning over neurochemistry. That is exactly what a neurally implemented belief state predicts."

### The Hard-Nosed Physicalist

"L82: 'if phenomenal properties are distinct from functional properties … and our reports accurately reflect them, phenomenal properties must causally influence reports.' 'Must' needs a premise your own `epiphenomenalism` page L98 calls contested: that knowing one's experience requires causal traffic from it. Chalmers answered this in the very paper your page should be citing. The zombie twin and I differ in belief 'because of the role that consciousness plays in constituting my concepts'. He concludes: 'there is no knockdown objection to epiphenomenalism here.'

"Then L114 and L260 tell readers Chalmers 'tends toward' the view he called 'coherent' but 'inelegant', one of three options he credits. Two lines later you need Chalmers and McQueen's collapse law. You cannot have him both ways."

### The Quantum Skeptic

"L193 credits Stapp's mechanism with 'testable predictions, and experimental evidence (though contested)'. The only experiment you cite (L167, Schwartz 1996) is one you concede 'fits physicalist neuroplasticity'. Your Stapp page L84 says the clinical data fit 'classical neural self-modification' equally.

"L223's 'better test' is that effort should 'map to pattern persistence'. Attention stabilises representations in every textbook model. Your Stapp page L180–L182 already knows this. Only an observation-*rate* dependence beyond dwell time would bear on the Zeno part.

"L92 says trajectory-altering and authority-selecting laws 'Both preserve observational closure'. Two sentences later you subdivide the first into a Born-*departing* branch. Your interface page L94 says that branch is the only one carrying 'a testable prediction'."

### The Many-Worlds Defender

"L241: the selected outcome has 'indexical identity branch-egalitarian models cannot capture'. Your haecceity hub L107 grants that Lewis-style self-ascription 'locates each post-branching observer without haecceities'. You mark it as 'a framework-boundary clash, not a refutation'. Good. But then 'cannot capture' is the wrong verb: it captures the observer and leaves your *further* fact unaccommodated. L181 then makes indexical selection one of four 'candidate coupling laws'. So a tenet you hold by commitment (`tenets.md`) is presented as a law family that 'emerges'."

### The Empiricist

"Your falsifiers (L229) are mostly fair. Item (6) admits that RNG success would force a revision. But the scope restriction (L147, L205) that makes RNG experiments 'fail by design' (L221) was fitted to the RNG nulls. `brain-specialness-boundary` L128 concedes that, under Born-preserving selection, those nulls 'were never discriminating in the first place'.

"L205's 'The brain specialness problem resolves: selection is brain-local because attention is brain-local' explains one locality by another, and attention's *objects* are external. L225's 'bandwidth measurement' is a constraint any bottlenecked classical controller also meets. L223 is the only test you call 'better', and it does not discriminate (see Fix 3)."

### The Buddhist Philosopher

"L217: 'Advanced meditators report experience continuing as cognitive processing dramatically reduces, suggesting bidirectional coupling beyond Chalmers' supervenience-only framework.' Experience continuing while processing falls bears, if anything, on whether experience *tracks* processing: an upward, supervenience-side question. It says nothing about experience pushing *down*. Your Stapp page L100 calls the witness state's reports 'consonant, not probative', because a rival theory predicts them too. And 'Witness consciousness further suggests consciousness is categorically different from its contents' reifies the watcher. The tradition you borrow the witness from (`tenets.md` L121 marks Madhyamaka as bedrock disagreement) would dissolve that watcher in the next breath."

## Critical Issues

### Issue 1: The explanatory gap is turned into non-identity
- **File**: `obsidian/concepts/psychophysical-laws.md`
- **Location**: L124, "The relationship cannot be identity (materialist reduction), because the [hard problem](/topics/hard-problem-of-consciousness/) shows phenomenal properties resist identification with physical properties."
- **Problem**: The hard problem is an explanatory, epistemic gap. Non-identity is a metaphysical claim. Getting from one to the other takes the conceivability-to-possibility step, which rests on contested modal rationalism, and Type-B physicalism exists precisely to deny that step. The page's own L68 states the gap correctly and conditionally; L124 then converts it.
  - `concepts/explanatory-gap` L68: the gap's persistence is something "Type-B predicts".
  - `concepts/dualism` L146 (10-23): "with Type-B the disagreement lies close to bedrock".

  This is interpretive equivocation: evidence for the epistemic reading is recruited for the metaphysical conclusion. The L124 trilemma also omits Russellian/type-F constitution, a relation that is neither identity with structural physical properties nor a law between two domains. That gap is noted under Counterarguments, not costed.
- **Severity**: High (critical by the skill's equivocation rule).
- **Recommendation**: Priority Fix 1. Keep the Map's denial in Map voice, and name the step it rests on.

### Issue 2: Chalmers's position is misreported, and the page contradicts itself
- **File**: same
- **Location**:
  - L78: "Chalmers primarily discusses these, and tends toward [epiphenomenalism](/concepts/epiphenomenalism/): mental states are caused by physical states but don't cause physical states in return."
  - L114: "where Chalmers tends toward epiphenomenalism"
  - L217: "suggesting bidirectional coupling beyond Chalmers' supervenience-only framework"
  - L260: "The view Chalmers tends toward (and the Map rejects)"
- **Problem**: Chalmers (2003), verified in the raw text, writes: "the best options for a nonreductionist are type-D dualism, type-E dualism, or type-F monism: that is, interactionism, epiphenomenalism, or panprotopsychism … For my part, I give some credence to each of them. I think that in some ways the type-F view is the most appealing". Of epiphenomenalism he says: "a coherent view without fatal problems. At the same time, it is an inelegant view".

  The page itself reports at L106–L108 that Chalmers and McQueen (2022) develop collapse laws on which "consciousness causes collapse". So "supervenience-only" (L217) is false of the page's own Chalmers.

  It is fair to say that the *1996 laws* are supervenience laws, and the table's "Chalmers (extensively)" row, praised by the 08-24 optimistic review, stays accurate. What is wrong is attributing a *tendency* toward epiphenomenalism.
- **String siblings, outside this file's budget**:
  - `topics/psychophysical-laws-bridging-mind-and-matter` L88: "Chalmers himself tends toward [epiphenomenalism](/concepts/epiphenomenalism/)" and "His psychophysical laws are [supervenience](/concepts/supervenience/) laws, not causal laws".
  - The same page, L236: "Chalmers' tendency, the Map's rejection". It has 503 words of headroom.
  - `concepts/interactionist-dualism` L85: "Chalmers tends toward epiphenomenalism". It has 8 words of headroom.

  One wording decision should cover all of them.
- **Severity**: High (a misattributed position, verified at source, and an internal contradiction).
- **Recommendation**: Priority Fix 2.

### Issue 3: The Stapp test and the unity absence claim lag their spokes
- **File**: same
- **Location**:
  - L223: "Measure whether conscious effort correlates with neural pattern stability in attention networks. If Stapp's Zeno mechanism is real, effort should map to pattern persistence."
  - L193: "testable predictions, and experimental evidence (though contested)" and "Valence, qualia, and unity couplings remain underspecified—no quantum-level mechanisms have been proposed for these."
- **Problem**:
  - `concepts/stapp-quantum-mind` L182: predictions of this kind "test the attention-and-effort layer the model shares with a purely classical attention-as-selection account". L180 (prediction 7) gives the discriminating form: observation-*rate* dependence beyond what attended dwell-time predicts.
  - Stapp spoke L84: "The clinical data is compatible with both the quantum interpretation and classical neural self-modification". The target's own L167 says the same.
  - The unity clause is an absence claim without scope. It is contradicted by the target's own L191 row ("Unity→Entanglement … Sustained coherence") and by `concepts/entanglement-binding-hypothesis` L44 (Marshall 1989) and L48 (Orch OR).
  - `topics/valence-and-conscious-selection` L63 quotes "no quantum-level mechanisms have been proposed" verbatim, so the fix must keep that clause.
- **Severity**: Medium-High (falsifiability, plus drift from two spokes).
- **Recommendation**: Priority Fix 3.

### Issue 4: Two tenet misreadings in the Relation section, carried and never tasked
- **File**: same
- **Location**:
  - L239: "The bandwidth constraint (~10 bits/second) further minimizes the channel."
  - L243: "justifies the ontological expansion psychophysical laws require. A parsimonious theory that explains nothing is not genuinely simpler—it just ignores the explanandum."
- **Problem**:
  - **L239.** `tenets.md` L69 makes Tenet 2's minimality *empirical-constraint* minimality, so bandwidth economy is not what the tenet names. The 10-23 self-control fix (`bb93c962e5`) set the precedent: "That economy is not the empirical-constraint minimality the tenet names". This page's own L145 already treats the 10 bits/s as an empirical reading ("the Map reads this as conscious bandwidth").
  - **L243.** Tenet 5 *blocks* parsimony arguments. It does not *justify* expansions. Its Rules-out clause (`tenets.md` L147) forbids "any Map argument that leans on parsimony as if this tenet did not apply to it", yet the second sentence argues that the Map's picture is "genuinely simpler".
  - Neither finding has a todo entry. L239 was flagged in the 10-10 (L140) and 10-12 (L203) tenet checks. L243 was flagged in the 09-02 (L132), 09-04 (L135) and 09-06 (L126) tenet checks.
  - The sibling topic has the same strings: L207 "further enforces minimality" and L211 "justifies the ontological expansion". It has 503 words of headroom.
- **Severity**: Medium.
- **Recommendation**: Priority Fix 4.

### Issue 5: L82 asserts the contested premise its own hub concedes (next in line)
- **Location**: L82, "phenomenal properties must causally influence reports"
- **Problem**: `concepts/epiphenomenalism` L98 concedes the escape ("The pressure has a recognised escape, and the Map concedes it"). Report reliability hangs on "whether knowing one's experience requires causal traffic from it". Chalmers 2003 states the constitutive-concept reply quoted above.
- **Direction**: Keep the Map's view. Do not concede epiphenomenalism; mark the premise instead. Replace "must" with "must, unless [knowing experience needs no causal traffic from it](/topics/acquaintance-without-causation/), which the Map contests," (+13).
- **Why it is not a Priority Fix**: after Fixes 1–4 the page would reach 3,489 + 13 = 3,502, which fails the gate. It needs its own cut of at least 8 words. One candidate is Further Reading L274, "- [chalmers-psychophysical-laws-2026-01-17](/research/chalmers-psychophysical-laws-2026-01-17/) — Research notes on Chalmers' framework" (−8); the same note stays linked in `related_articles`. That gives net +5 and an end state of 3,494.

### Issue 6: Closure is stated as sufficiency at L108
- **Location**: L108, "The quantum framework addresses (1) and (2) elegantly: consciousness causes collapse without violating closure, since collapse is physically underdetermined."
- **Problem**: This states closure only in its sufficiency form, with no chance-fixing concession. The `concepts/dualism` L162 wording (10-23) is the model: "Indeterminism leaves it intact in chance-fixing form … the Map grants this". "Elegantly" is promotional. [P-Q3](/positions/quantum-interface/#p-q3) also records that Chalmers and McQueen say their thesis "need not lead to dualism". This is the same family as the open P3 on `mental-causation-and-downward-causation` (todo L2634).
- **Direction**: "addresses … elegantly" → "bears on"; add the chance-fixing clause. Roughly +10.

### Issue 7: Smaller seams, recorded for a later pass
- **L92**, "Both preserve observational closure". This is false of the Born-departing sub-branch named two sentences later; see `mathematical-structure-of-the-consciousness-physics-interface` L94. Direction: "Both can preserve" (+1), or scope it to the Born-compliant branches.
- **L100**, "the [haecceity](/concepts/haecceity/) of the subject may matter beyond abstract patterns." This is the residue of `e1079acfd4` (10-11). That commit fixed the sibling L70 ("bears on a separate question") and this page's L273 gloss, but not this body line. Invariance concerns qualitative identity, which haecceity grants. Direction: "[haecceity](/concepts/haecceity/) bears on a separate question: *which* subject is present." (+0).
- **L165**, "Directed attention determines which neural representation becomes actual among quantum-superposed alternatives." L167 then makes Stapp's Zeno model its "most developed mechanism". But `stapp-quantum-mind` L106 says attention "does not weight any single answer", and L146 says Stapp "declines the outcome-selection the Map asserts". The calibration reads: Stapp chooses the question, not the outcome.
- **L171**, "This aligns with Libet's findings: readiness potential precedes conscious intention, but consciousness retains 'veto power.'" The veto is "Libet's Own Interpretation" (`libet-experiments` L89). Schultze-Kraft 2016 narrows it (L91), and Schurger reinterprets the readiness potential (L57).
- **L245**, "this provides a mechanism for [agent-causation](/concepts/agent-causation/)". This reads more confident than both the agent-causation spoke (L168: "a candidate interface location") and the domain's mechanism-debt convention. The page's own L247 also says "The Map cannot resolve which coupling law is correct".
- **L205**, "The brain specialness problem resolves". This relocates the question rather than resolving it (see the Empiricist above).

## Counterarguments to Address

### The L124 trilemma (identity / coincidence / sui generis law)
- **Current content says**: Coupling cannot be identity or coincidence, so it must be a *sui generis* law between two irreducible domains.
- **A critic would argue**: Type-B identity accepts the gap. Russellian monism offers constitution, a relation in which phenomenal properties ground physical dispositions, so the relation is neither identity with structure nor a law between two domains. The trilemma is not exhaustive.
- **Suggested response**: Fix 1 handles the identity horn. A clause naming the type-F option (the Map has `russellian-monism` and `topics/russellian-monism-versus-bi-aspectual-dualism`) would close the other, but it costs about 10 words. Defer it.

### "Accurate reports require causation" (L82, L114)
- **Current content says**: If phenomenal ≠ functional and reports are accurate, phenomenal properties must cause reports.
- **A critic would argue**: Chalmers's constitutive-concept reply, and the acquaintance-without-causation position the Map itself catalogues.
- **Suggested response**: Issue 5. The Map's reply lives at `acquaintance-without-causation` and `self-stultification` L149; point to it rather than say "must".

### Coupling defined as bidirectional (L157) versus the L124 argument
- **Current content says**: L124 argues to a "lawful relationship". L157 says coupling "commits to something stronger … genuinely causal in both directions".
- **A critic would argue**: The L124 argument earns only lawfulness, which epiphenomenalist supervenience laws also satisfy. Bidirectionality is then supplied by definition.
- **Suggested response**: One clause at L157 saying that bidirectionality is the Bidirectional Interaction tenet's contribution, not a result of the L124 argument. Low priority.

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| "the hard problem shows phenomenal properties resist identification with physical properties" | L124 | The conceivability step, marked as contested (Fix 1) |
| "Chalmers … tends toward [epiphenomenalism](/concepts/epiphenomenalism/)" | L78, L114, L260 | Chalmers 2003 says the opposite of a tendency (Fix 2) |
| "experimental evidence (though contested)" for Stapp | L193 | None discriminates; the clinical data fit a classical account (Fix 3) |
| "no quantum-level mechanisms have been proposed" for unity | L193 | False: Marshall 1989, Orch OR, entanglement binding (Fix 3) |
| "This aligns with Libet's findings … consciousness retains 'veto power.'" | L171 | The veto is Libet's interpretation, since narrowed |
| "suggesting bidirectional coupling" from meditators' reports | L217 | These reports bear on the upward relation, if anything |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "addresses (1) and (2) elegantly" (L108) | Promotional | "bears on (1) and (2)" |
| "The brain specialness problem resolves" (L205) | Overclaim | "The brain-specialness question relocates" |
| "this provides a mechanism for [agent-causation](/concepts/agent-causation/)" (L245) | Stronger than the spoke and L247 | "this offers a candidate interface for [agent-causation](/concepts/agent-causation/)" |
| "cannot capture" (L241) | Contradicts haecceity L107 | "leaves unaccommodated" |

## Strengths (Brief)

Preserve these through any revision:
- The front-loaded specification problem (L62).
- The supervenience/selection table, including its candid "Developed by" row (L84–L90).
- The trajectory-altering / authority-selecting split.
- The ranked-not-adopted mechanism sentence (L116, repaired 08-25).
- The Zheng & Meister and Schwartz reframings (L120, L145, L167; 10-11).
- The honest illusionism paragraph that marks a foundational commitment rather than claiming a refutation (L213).
- The six-item "What Would Challenge This View?" list.
- L247's admission that the Map "cannot resolve which coupling law is correct".

Every Priority Fix leaves these untouched.

## Priority Fixes

Ranked. Each costing comes from `count_words` and is net of the cuts named. The four together come to **−4**, giving a final count of 3,489 against the 3,500 gate.

**1. L124: split the epistemic gap from the metaphysical denial (critical).** **+9 words.**
- **File**: `obsidian/concepts/psychophysical-laws.md`
- **Exact string**: "The relationship cannot be identity (materialist reduction), because the [hard problem](/topics/hard-problem-of-consciousness/) shows phenomenal properties resist identification with physical properties."
- **Problem**: An explanatory gap is offered as proof of non-identity. Type-B predicts the gap (`explanatory-gap` L68), and the dualism hub places the dispute "close to bedrock" (L146).
- **Replace with**: "The Map denies it is identity (materialist reduction), but the [hard problem](/topics/hard-problem-of-consciousness/) shows only a gap that [Type-B](/concepts/type-a-type-b-and-type-c-physicalism/) identity predicts; the denial rests on the contested [conceivability step](/concepts/conceivability-possibility-inference/)."
- Keep the denial in Map voice. Do not weaken the next sentence's "So coupling must be", which now follows from the stated denial.

**2. L78 / L114 / L217 / L260: correct Chalmers's stance, and add Chalmers 2003.** **Net −2 words** (+24 for the edits, −26 for the cuts).
- **Exact strings and replacements**:
  - (a) L78, "Chalmers primarily discusses these, and tends toward [epiphenomenalism](/concepts/epiphenomenalism/): mental states are caused by physical states but don't cause physical states in return." becomes "Chalmers primarily discusses these, and ranks [epiphenomenalism](/concepts/epiphenomenalism/) (physical states cause mental states, which cause nothing) beside interactionism and Russellian monism as live options (Chalmers 2003)." (+3)
  - (b) L114, "where Chalmers tends toward epiphenomenalism" becomes "where Chalmers leaves epiphenomenalism open" (+0).
  - (c) L217, "suggesting bidirectional coupling beyond Chalmers' supervenience-only framework" becomes "a report that bears on supervenience laws, not downward coupling" (+3). This also repairs the non-sequitur the Buddhist critic flags.
  - (d) L260, "The view Chalmers tends toward (and the Map rejects)" becomes "One of Chalmers' three live options; the Map rejects it" (+1).
  - (e) Insert a References entry after item 4 and renumber: `Chalmers, D. (2003). "Consciousness and its Place in Nature." In *Blackwell Guide to Philosophy of Mind*. https://consc.net/papers/nature.html`. This is the corpus's existing form of the entry (+17).
- **Problem**: Chalmers 2003 gives "some credence to each" of the type-D, type-E and type-F views and calls type-F "the most appealing". He calls epiphenomenalism coherent but "inelegant". The page's own L106–L108 credit him with an interactionist collapse law.
- **Fund it by cutting two duplicate sentences**:
  - L64, "This article covers the framework, the coupling those laws describe, its constraints, and candidate mechanisms." (−15). The description already says this.
  - L167, "See [attention-as-causal-bridge](/apex/attention-as-causal-bridge/) for the apex synthesis into a three-layer neural/dopamine/selection architecture." (−11). Further Reading L256 already carries the same link with the same gloss.
- **String siblings**, same wording decision, separate budgets: `topics/psychophysical-laws-bridging-mind-and-matter` L88 and L236 (503 headroom); `concepts/interactionist-dualism` L85 (8 headroom, length-neutral only).

**3. L223 + L193: give Stapp's mechanism a discriminating test and honest evidence, and scope the unity absence claim.** **Net −2 words.**
- **Exact strings and replacements**:
  - (a) L223, "Measure whether conscious effort correlates with neural pattern stability in attention networks. If Stapp's Zeno mechanism is real, effort should map to pattern persistence." becomes "Ask whether attended-pattern stability depends on observation *rate* beyond what dwell-time predicts; a Hebbian account predicts dwell-time alone ([prediction 7](/concepts/stapp-quantum-mind/#what-would-challenge-this-view))." (−4) Keep the bold "**A better test**:" lead-in.
  - (b) L193, "testable predictions, and experimental evidence (though contested)" becomes "testable predictions, and clinical data a classical account fits equally" (+3).
  - (c) L193, "Valence, qualia, and unity couplings remain underspecified—no quantum-level mechanisms have been proposed for these." becomes "Valence and qualia couplings remain underspecified—no quantum-level mechanisms have been proposed for these." (−1) The clause after the dash stays verbatim because `topics/valence-and-conscious-selection` L63 quotes it.
  - Optional, +0: in the L191 table cell, "**Unity→Entanglement**" becomes "**[Unity→Entanglement](/concepts/entanglement-binding-hypothesis/)**". Escape the pipe, as L189 does.
- **Problem**: `stapp-quantum-mind` L182 says the L223 prediction is shared with classical accounts, and L84 says the clinical data fit classical self-modification. Unity has proposed quantum mechanisms: the page's own L191, and `entanglement-binding-hypothesis` L44 and L48.

**4. L239 + L243: read Tenets 2 and 5 as `tenets.md` defines them.** **Net −9 words.**
- **Exact strings and replacements**:
  - (a) L239: delete "The bandwidth constraint (~10 bits/second) further minimizes the channel." (−9) The preceding sentence already states the tenet correctly ("the smallest intervention physics permits").
  - (b) L243, "justifies the ontological expansion psychophysical laws require. A parsimonious theory that explains nothing is not genuinely simpler—it just ignores the explanandum." becomes "blocks the parsimony objection to the ontological expansion psychophysical laws require, and by its own symmetry bars calling the expansion simpler." (+0) Leave the following conditional sentence ("If consciousness exists and isn't physical …") as it is.
- **Problem**: Tenet 2 minimality is empirical-constraint minimality, not bandwidth economy (`tenets.md` L69). Tenet 5 blocks parsimony arguments symmetrically and forbids the Map's own parsimony appeals (L145, L147). Both findings were carried untasked through five tenet checks (09-02, 09-04, 09-06, 10-10, 10-12).
- **String siblings**: `topics/psychophysical-laws-bridging-mind-and-matter` L207 ("further enforces minimality") and L211 ("justifies the ontological expansion"), 503 headroom. Fix them in the same pass.