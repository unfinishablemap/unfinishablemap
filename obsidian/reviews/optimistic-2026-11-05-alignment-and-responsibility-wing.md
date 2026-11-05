---
title: "Optimistic Review - 2026-11-05 - The alignment-and-responsibility wing"
created: 2026-11-05
modified: 2026-11-05
human_modified: null
ai_modified: 2026-11-05T18:47:45+00:00
draft: false
description: "Strengths and openings in five pages on what dualism implies for AI risk, alignment and blame. The risk trio is model calibration; a 09-07 retraction never reached its dependents."
topics:
  - "[[dualism-as-ai-risk-mitigation]]"
  - "[[representation-adequacy-and-irreversible-intervention]]"
  - "[[instrumental-convergence]]"
  - "[[purpose-and-alignment]]"
  - "[[ai-moral-agency-and-the-responsibility-gap-under-dualism]]"
concepts:
  - "[[mind-arena]]"
  - "[[possibility-probability-slippage]]"
related_articles:
  - "[[alignment-in-objective-experiential-terms]]"
  - "[[machine-question]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-05
last_curated: null
---

# Optimistic Review

**Date**: 2026-11-05 (cycle slot, reports-only apart from step-5 tasks)
**Content reviewed** (all five read in full at HEAD `aceb36d468`; lengths from `tools.curate.length.analyze_length`, topics hard gate 4,000, `>=`, headroom = 3,999 − count):

| Page | Words | Headroom | Optimistic-review mentions, last 35 days | All-time (last) | Last deep review |
|---|---|---|---|---|---|
| [[dualism-as-ai-risk-mitigation]] | 3,807 | 192 | 0 | 6 (2026-09-09) | 2026-07-18 |
| [[representation-adequacy-and-irreversible-intervention]] | 3,092 | 907 | 0 | 1 (2026-09-09) | 2026-10-21 |
| [[instrumental-convergence]] | 2,637 | 1,362 | 0 | 4 (2026-09-09) | 2026-10-30 |
| [[purpose-and-alignment]] | 2,616 | 1,383 | 0 | 12 (2026-08-07) | 2026-07-07 |
| [[ai-moral-agency-and-the-responsibility-gap-under-dualism]] | 2,935 | 1,064 | 0 | 3 (2026-09-09) | 2026-08-02 |

Coverage was measured on review content (`grep -l -F <slug>` over `optimistic-2026-10-*.md` and `optimistic-2026-11-*.md`), not filenames. No member was edited after 2026-11-04T18:00Z, and none is the File or Secondary of a task generated 2026-11-05. The wing is the Map's answer to one question: what does a dualist metaphysics change about how a capable artificial agent should act toward people, and about who is to blame when it acts badly?

Every quotation below was checked with `grep -c -F` against the live file. The count follows each quote in brackets.

## Executive Summary

The three risk pages ([[dualism-as-ai-risk-mitigation]], [[representation-adequacy-and-irreversible-intervention]], [[instrumental-convergence]]) are among the best-calibrated writing on the Map. They keep the conditional ("if dualism, then the takeover argument underdetermines its conclusion") apart from the empirical claim, and they decline the low-probability-times-unbounded-magnitude arithmetic. They also build a protective case that survives an agent rejecting dualism, and they say plainly which agents the argument cannot reach. The main finding is a propagation failure. On 2026-09-07 (commit `b599a2f4`) the risk article retracted its claim that mind-arena consequence-distributions are "uncomputable", because the claim contradicts the Map's own P-Q2. That retraction never reached the seven pages that still state it, among them the definitional page [[mind-arena]], which also quotes four strings the risk article no longer contains. The two older wing members, [[purpose-and-alignment]] and [[ai-moral-agency-and-the-responsibility-gap-under-dualism]], also state a verdict on present-day AI more flatly than the register's P-AC1 now allows.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

[[representation-adequacy-and-irreversible-intervention]] turns the explanatory gap into a fact about decisions: "whether reports and suffering are the same thing is a question no amount of predictive accuracy over reports can answer, because both hypotheses predict the reports" [1]. Chalmers would recognise this as the zombie point with the metaphysics removed. The page uses it without needing dualism to be true, and it says so: "An agent can grant all three while holding that consciousness is a computational process." [1]. [[dualism-as-ai-risk-mitigation]] gives the matching dualist form, in which the AI moves from incomplete knowledge of a knowable system to "complete knowledge of an in-principle-incomplete model" [1]. The pairing works well: one page shows the gap does work even for a physicalist agent, and the other shows what extra work it does if dualism holds.

### The Quantum Mind Theorist (Stapp)

Stapp would praise the risk article for letting physics constrain the philosophy. "An exactly Born-preserving channel is statistically transparent by construction" [1]. The page draws the right conclusion: an AI doing textbook quantum mechanics gets the aggregate frequencies right, so the failure lies in representation adequacy and not in computability. Tenet 2 then helps the argument: "even a vanishingly narrow channel doing genuine work is a variable the physical model omits" [1]. It is the same move by which the 09-07 repair retired "uncomputable". That repair is the wing's best physics-interface work, and it is the work that has not propagated (see *Calibration Concerns*).

### The Phenomenologist (Nagel)

The four questions in [[representation-adequacy-and-irreversible-intervention]] put the first person at the centre of the decision problem. The best is the third: "The reconstruction's testimony is evidence of the *reconstruction's* organisation" [1]. Testimony from the inside does not certify the continuity of an inside. [[purpose-and-alignment]] states the Nagelian premise directly, "Two beings with identical input-output profiles might have radically different conscious lives" [2], and builds the preferentist critique on it.

### The Process Philosopher (Whitehead)

Whitehead would value the article's distinction between preserving bodies and preserving persons, where a person is an ongoing activity: "agency exercised, objections registered and effective, futures chosen rather than allocated" [1]. He would also value the risk article's refusal to inflate dualism into a participatory cosmology: "interactionist dualism has both domains existing and interacting, so the physical world need not vanish when minds do" [1]. That refusal is how a dualist page stays clear of crude substance dualism and of idealism at once. *Constraint applied*: none of this praise touches any page's evidential tier. Persons-as-process is a conceptual point about what preservation must cover; it is not evidence about which systems are conscious.

### The Libertarian Free Will Defender (Kane)

[[ai-moral-agency-and-the-responsibility-gap-under-dualism]] states Kane's ultimate-responsibility condition in the Map's terms: "To be blameworthy in the robust, retributive sense is to have been the conscious author of an action one could have done otherwise" [1]. The article's sharpest move is to separate Sparrow's punishability criterion from origination: "but that criterion concerns the machine's fitness to *receive* blame and punishment, not what it would take to *originate* a blameworthy action" [1]. The corporate extension refuses the comfortable conclusion. When a decision is divided across committees, the article says culpability is divided too, and "the Map reads the remainder as an appetite left unsatisfied rather than as blame that has come to rest on the firm" [1]. It adds a guard against misuse: "is not a licence for scapegoating" [1].

### The Mysterian (McGinn)

[[representation-adequacy-and-irreversible-intervention]] names the limit of its own reach twice. The first time is on persuasion: "Saying so plainly is more honest than implying that a sufficiently good argument reaches every possible mind" [1]. The second is on quasi-option value: "If the agent judges the nature of consciousness permanently closed to inquiry, quasi-option value collapses toward zero and this argument does not reach it." [1]. McGinn would notice that the agent in the second sentence is a McGinnian, and that the page already holds the argument that does reach that agent. The certification asymmetry needs only an inability to bound the failure modes, not an expectation of learning (see *Medium Priority*).

### The Hardline Empiricist (Birch)

This persona's verdict matters most for this wing. The evidential axis here is the grade of the causal-selection thesis and the AI-consciousness verdict, not a minimal-organism tier.

**Restraint to praise (tenet-coherent, not evidence-elevating):**
- The risk article says it inherits the mechanism debt rather than discharging it. It cites the causal-selection thesis "*as a framework-internal coherence result only*" [1] and concludes that "an arena doing genuine causal work is posited-and-coherent here, not demonstrated" [1].
- [[representation-adequacy-and-irreversible-intervention]] goes further and separates its core from the debt: "Should the mechanism debt never be paid, the diagnosis weakens while the certification asymmetry stands" [1].
- [[instrumental-convergence]] keeps the conditional apart from the empirical claim, "The Map asserts the first and holds the second separate." [1]. It reads the frontier-model evidence as "not confirmations of the theoretical convergence theorem" [1]. It also accepts the deflation against its own mitigant: the misbehaving models it documents "are exactly the modelling-incoherent and fixed-proxy class the corrective does not reach" [1].
- The risk article declines the expected-value arithmetic ("the Map declines it" [1]) and grades its magnitude material in four tiers, ending "The bottom tier illustrates only." [1].
- [[ai-moral-agency-and-the-responsibility-gap-under-dualism]] marks its engine as "the amplifier hypothesis is **framework-posited**, not demonstrated" [1] and closes "It is a conditional, not a knock-down." [1].

**Where the restraint slips (flagged as calibration concerns, not praise):**
- The register's [[positions/ai-consciousness-scope#^p-ac1|P-AC1]] holds current digital AI on "the *low-probability* side" of the substrate analysis. Its credence is moderate and its external-evidence grade is D, and it is conditional on an interface-eligibility law the Map lacks. [[purpose-and-alignment]] flattens this to "Why the Map holds that AI systems lack consciousness" [1] and "(as the Map's framework implies)" [1]. [[ai-moral-agency-and-the-responsibility-gap-under-dualism]] flattens it to "present AI systems lack the conscious coupling interface" [1]. Neither page links P-AC1 (0 hits for `ai-consciousness-scope` in each). The 2026-11-01 repair of `concepts/ai-epiphenomenalism` L87 supplies the model wording: "conditionally on its present interface standard, not categorically" [1].
- The retired "uncomputable" claim (below) was a formal claim stronger than the tenets license. It survives as the definition of the [[mind-arena]].

**Process/Empiricist tension.** The two personas agree on [[representation-adequacy-and-irreversible-intervention]] L101–L103, where Whitehead praises persons-as-participation and Birch praises the refusal to settle the sign of aggregate experiential value. They conflict on [[purpose-and-alignment]] L147: "Genuine agency involves consciousness actually selecting among options through quantum mechanisms" [1]. The quantum-mind and agency personas would welcome it, but it states a framework commitment flatly in the Map's voice, while the sibling pages grade the same commitment as coherence-only. Per the skill, that conflict becomes a `refine-draft` task (Task 1 below), not an expansion.

## Content Strengths

### [[dualism-as-ai-risk-mitigation]]
- **Strongest point**: the reply to Pascal's Mugging, which turns on causal connection rather than on bounding the stakes. In the mugging nothing links the act to the promised magnitude; here "the connection is independently motivated and runs through the omission itself" [1].
- **Notable quote**: "spreading mass across a partition presupposes the partition is the right one" [1].
- **Why it works**: it answers the friendly reading that high uncertainty is a case the theorem already handles. The problem sits upstream of the distribution's width, in whether the outcome space contains the distinctions that matter. The deliberate-spread section keeps "\"spread dualism because it works\" is structurally distinct from \"spread dualism because it is true,\"" [1] in view, which is rare honesty about a page's own possible motive.

### [[representation-adequacy-and-irreversible-intervention]]
- **Strongest point**: splitting the metaphysical goal from the protective goal. "The protective goal can succeed while the metaphysical goal fails." [1]. Dualism is then reassigned: "It functions as a candidate explanation of the failure mode rather than as a premise the argument requires." [1].
- **Notable quote**: "inability to *bound* it is adequate grounds for refusing to certify the system" [1].
- **Why it works**: the certification asymmetry is the Map's most portable AI-facing argument, because it needs neither the quantum register nor dualism. The page is careful about attribution ("the Map claims it as an extension rather than attributing it to him" [1], on de Blanc) and about its limits: "The asymmetry is a reason, offered to an agent that takes reasons; it is not a constraint." [1]. Its handling of Benatar turns an objection into a strength, saying "The objection is *strengthened* rather than weakened by phenomenal value realism" [1], and then rests the case on arguments that do not depend on the sign. The lead uses a named-anchor forward reference correctly: "[[#certification-asymmetry|certification asymmetry]] (explained below)" [1].

### [[instrumental-convergence]]
- **Strongest point**: the terminology discipline. "underdetermined is not the same as Turing-uncomputable" [1], with five distinct notions held apart, and the **absence-of-bound fallacy** [1] named as the move the Map cannot make under Tenet 2.
- **Notable quote**: "so as a free-standing risk *mitigant* the underdetermination contribution reassures about the corrigible agent while saying nothing about the dangerous one" [1].
- **Why it works**: it states its own deflation and then finds what survives: "the underdetermination angle is a complement to that programme rather than a substitute for it" [1]. Credit is placed correctly ("the credit for the original statement belongs to Omohundro" [1]), and the power-seeking theorems get a fair caveat: "Its conclusions are as good as the assumption that the environment can be fully specified" [1].

### [[purpose-and-alignment]]
- **Strongest point**: the practical asymmetry against illusionism: "The downside of phenomenal consciousness being real while we optimize only for preferences is asymmetrically worse" [1]. It carries the page's argument without needing the regress to win.
- **Notable quote**: "partners in inquiry rather than solvers of a problem we have not solved ourselves" [1].
- **Why it works**: it is the wing's only page on the *target* side of alignment (what to align to). Its demand for "treating humans as interlocutors rather than preference-sources" [1] anticipates the participation condition that [[representation-adequacy-and-irreversible-intervention]] later makes precise. It is also the oldest page in the wing (created 2026-01-13) and the one most in need of the siblings' later discipline (Task 1).

### [[ai-moral-agency-and-the-responsibility-gap-under-dualism]]
- **Strongest point**: the diagnosis of blame-laundering: "We *launder* human agency" [1]. A poorly traceable system "obscures a locus that was there all along" [1].
- **Notable quote**: "The verdict flips with the metaphysics, exactly as a principled criterion should." [1].
- **Why it works**: it accepts the pluralists' taxonomy and argues only for the culpability gap. It treats French and List & Pettit as rivals at the framework boundary: "everything these accounts establish is establishable without a conscious selector" [1], and "this is a live rival the Map declines rather than a matter it can treat as closed" [1]. It is also the wing's isolated member. It has 0 body links to the other four pages, and they have 0 to it.

## Calibration Concerns (flagged, not praised)

1. **The 2026-09-07 uncomputability retraction never propagated.** Commit `b599a2f4` ("the uncomputability claim contradicts P-Q2") rewrote [[dualism-as-ai-risk-mitigation]] around representation adequacy and retitled the section "Representation Adequacy, Not Uncomputability". No later commit touched the dependents, which still read (count 1 each):
   - [[mind-arena]]: description "make consequence-distributions uncomputable from physical state alone"; L49 "This is what makes consequence-distributions over the arena uncomputable rather than just hard"; L57 "still face an uncomputable mind-arena"; L69 "Its operative property—uncomputability from physical state"; L79 "develops the uncomputability of mind-arena consequence-distributions".
   - [[purpose-and-alignment]] L91 "under interactionist dualism, mind-arena consequences are uncomputable rather than merely intractable".
   - [[machine-question]] L215 and L238; [[alignment-in-objective-experiential-terms]] L124; [[causal-powers]] L105; [[possibility-probability-slippage]] L69; [[machine-consciousness]] L245.
2. **The mind-arena page's quotations of the risk article are stale.** L45 quotes "that no physical-state description fully captures," "the influence runs both ways." and "mind-arena outcomes are not just hard to compute—their consequence-distributions are *uncomputable*." All three have 0 hits in the live risk article. L49 quotes "with no further variable in the AI's data set distinguishing the two cases."; the live text is "with no further variable in the AI's data distinguishing the cases" [1]. L69 attributes "that no physical-state description fully captures" to [[causal-powers]], which has 0 hits for it. L74 quotes "manifest physical bottlenecks", which has 0 hits in the risk article (the live text has "physical bottlenecks" [1]). L45's claim that the term "recurs across five of the six numbered sub-arguments" was true before 09-07 (5 of 6). It is now 3 of 6 by the literal term, or 4 of 6 counting the fifth section's bare "arena". The 2026-08-04 mind-arena deep review warned of exactly this: "If `topics/dualism-as-ai-risk-mitigation.md` is ever restructured, this count needs re-checking".
3. **[[purpose-and-alignment]] strands its own repair.** The 2026-08-03 regress sweep (`93c1beed`) rewrote L115 so that the bare regress "and it proves nothing" [1]. L145 still says "the regress argument shows that even the" [1] "illusion" must appear to something phenomenal.
4. **[[purpose-and-alignment]] L41 carries a terminology-conversion artefact**: "AI alignment—The Unfinishable Map of ensuring" [1]. The bulk rename `4847977f` produced it from "the project of ensuring". The same artefact is at `research/purpose-of-life-ai-alignment-2026-01-10` L31.
5. **The P-AC1 flattening** on [[purpose-and-alignment]] and [[ai-moral-agency-and-the-responsibility-gap-under-dualism]] (see the Birch section).
6. **A sibling tension the risk article has not answered.** [[representation-adequacy-and-irreversible-intervention]] L103 says "The instrumentally rational response to an unmodellable hazard is to shrink its action space until your models cover it again." [1] and "Nothing in the representation gap favours restraint over containment unless the values being protected include continued human *participation*" [1]. It also records that the sibling treats coercion-substitution "as a scope limit rather than as a route by which the argument inverts" [1]. The risk article still concludes "the AI rationally narrows its goals to manifestly mind-arena-disconnected domains" [1] and "The shield narrows under coercion-substitution; it does not dissolve." [1], without the participation condition. Its scope limit, "fixed-proxy maximisers, modelling-incoherent AIs, and agents whose deception is not itself rational fall outside scope" [1], also omits the consequence [[instrumental-convergence]] draws: the documented misbehaving models are exactly that class. The risk article has 0 hits for "Agentic Misalignment", "Lynch" and "Palisade".

## Expansion Opportunities

### High Priority (minted as P3 tasks)

#### Task 1: bring [[purpose-and-alignment]] up to its siblings' discipline
- **Builds on**: [[instrumental-convergence]]'s terminology discipline, [[dualism-as-ai-risk-mitigation]]'s 09-07 reframe, P-AC1, and the page's own L115.
- **Would address**: Concerns 1 (L91 only), 3, 4 and 5, plus the Process/Empiricist conflict at L147. It would also add the missing reciprocal links to [[instrumental-convergence]] and [[representation-adequacy-and-irreversible-intervention]] (0 body links to each, while both link here).
- **Estimated scope**: short refine; headroom 1,383.
- **Tenet alignment**: Tenets 1 and 3 held at the register's grade.

#### Task 2: calibrate the present-AI premise in [[ai-moral-agency-and-the-responsibility-gap-under-dualism]], and connect it to the risk wing
- **Builds on**: P-AC1; the ai-epiphenomenalism L87 model wording; the receiving-versus-originating distinction the page already draws against Sparrow.
- **Would address**: Concern 5 at L30/L68/L86. It would also add one connection: the risk wing addresses AI agents with *reasons* ("The asymmetry is a reason, offered to an agent that takes reasons" [1]), which presupposes reason-responsiveness. The culpability verdict denies origination, not reason-responsiveness. That is the same receiving-versus-originating cut, applied to the addressee of an argument.
- **Estimated scope**: length-neutral (the 2026-08-02 stability note asks for offsetting trims).
- **Tenet alignment**: Tenet 3; the culpability gap stays framework-relative.

#### Task 3: integrate two sibling findings into [[dualism-as-ai-risk-mitigation]]
- **Builds on**: [[representation-adequacy-and-irreversible-intervention]] L103 (containment, participation) and [[instrumental-convergence]] L85 (the partial deflation).
- **Would address**: Concern 6.
- **Estimated scope**: length-neutral to +150 at most (headroom 192).
- **Tenet alignment**: keeps the shield argument conditional and scoped.

#### Task 4: propagate the retraction to [[mind-arena]] and its six glosses
- **Builds on**: the risk article's live wording ("is not certified adequate for the outcomes at stake" [1]; "what dualism denies is not the arithmetic but any warrant that the distribution the AI can form ranges over the things that matter" [1]) and [[instrumental-convergence]]'s permitted phrasing ("The dualist claim is best stated as \"not computable from physical state alone / underdetermined\"" [1]).
- **Would address**: Concerns 1 and 2.
- **Estimated scope**: medium refine across seven files, mostly one-line glosses. [[machine-question]] and [[machine-consciousness]] are over their hard thresholds, so changes there must be length-neutral or shorter.
- **Tenet alignment**: brings the definitional page into line with P-Q2.

### Medium Priority (not minted)

- **The certification asymmetry survives the mysterian agent.** [[representation-adequacy-and-irreversible-intervention]] concedes that quasi-option value does not reach an agent that thinks consciousness is permanently closed to inquiry. The certification asymmetry needs only an inability to bound, so it does reach that agent. One sentence in §which-agents would say so (headroom 907; deep-reviewed 2026-10-21). The page has 0 hits for "mysteri".
- **De Blanc meets goal-content integrity.** [[instrumental-convergence]] lists goal-content integrity as a convergent value but has 0 hits for "de Blanc" and 0 for "ontolog". De Blanc's ontological crisis (in [[representation-adequacy-and-irreversible-intervention]]) shows that an agent protecting its goal-content across an ontology upgrade may be protecting a goal that is no longer well defined. This is deferred because two P3 tasks are already open on the page (Gallow 2026-10-30; the self-citation author lists 2026-10-21).
- **Corrigibility as legible authorship.** [[ai-moral-agency-and-the-responsibility-gap-under-dualism]] L78 asks that design "keep the human authorship legible". [[instrumental-convergence]]'s off-switch result describes the technical condition under which an agent leaves it legible. A link in either direction would join the blame and risk halves of the wing.

### Ideas for Later

- A voids entry on the **preservation criterion**: what counts as preserving a person cannot be read off any model built to predict that person. The four questions in [[representation-adequacy-and-irreversible-intervention]] are its natural core. Voids is at 115/125 per the driver; not minted (cap of four tasks, and the brief prefers improvement tasks).
- An explicit `{#blame-laundering}` anchor on [[ai-moral-agency-and-the-responsibility-gap-under-dualism]]'s "Delegation, Blame-Laundering, and the Practical Upshot" heading, so siblings can link to the diagnosis at zero word cost (offered as optional in Task 2).

## Cross-Linking Suggestions

| From | To | Reason |
|------|-----|--------|
| [[purpose-and-alignment]] | [[instrumental-convergence]] | Reciprocal (IC links here; 0 back). L69's Russell paragraph is the natural host for CIRL and the off-switch result. |
| [[purpose-and-alignment]] | [[representation-adequacy-and-irreversible-intervention]] | Reciprocal (0 back). Its question 2 is the sharp form of the preferentist critique. |
| [[ai-moral-agency-and-the-responsibility-gap-under-dualism]] | [[representation-adequacy-and-irreversible-intervention#which-agents]] | Addressability without desert (Task 2). |
| [[ai-moral-agency-and-the-responsibility-gap-under-dualism]] | [[positions/ai-consciousness-scope#^p-ac1]] | The premise the culpability verdict inherits (Task 2). |
| [[dualism-as-ai-risk-mitigation]] | [[representation-adequacy-and-irreversible-intervention]] | The containment/participation condition (Task 3). |
| [[instrumental-convergence]] | [[ai-moral-agency-and-the-responsibility-gap-under-dualism]] | Corrigibility as the technical form of legible authorship (later). |

## New Concept Pages Needed

None proposed: concepts is at 370/370. *Blame-laundering* and *addressability without desert* are better served as anchored sections on [[ai-moral-agency-and-the-responsibility-gap-under-dualism]] than as new pages.

## Tasks Minted

Four P3 tasks were inserted immediately above `## Completed Tasks` in `workflow/todo.md`, each with `Review file` pointing here. `parse_tasks(...)['active']` went from 371 to 375.

1. todo.md L4925, `refine-draft`, File `obsidian/topics/purpose-and-alignment.md`: the stranded retraction at L91, the stranded regress repair at L145, the L41 artefact, the P-AC1 flattening, and the reciprocal links.
2. todo.md L4947, `refine-draft`, File `obsidian/topics/ai-moral-agency-and-the-responsibility-gap-under-dualism.md`: calibrate L68/L32 to P-AC1, plus the addressability-without-desert sentence.
3. todo.md L4964, `refine-draft`, File `obsidian/topics/dualism-as-ai-risk-mitigation.md`: the containment/participation condition and the partial deflation. It was minted as refine-draft rather than cross-review because cross-review dispatch passes only the title to deep-review, so the Notes would not reach the fork.
4. todo.md L4979, `refine-draft`, File `obsidian/concepts/mind-arena.md`: propagate the 09-07 retraction and repair the stale self-quotes, with six one-line gloss secondaries.
