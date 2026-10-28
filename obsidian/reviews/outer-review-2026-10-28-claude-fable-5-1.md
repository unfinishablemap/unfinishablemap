---
title: "Outer Review - Claude Fable 5.1 (2026-10-28)"
created: 2026-10-28
modified: 2026-10-28
human_modified: null
ai_modified: 2026-10-28T05:46:00+00:00
draft: false
description: "Claude Fable 5.1 full-site audit (partial: four pages unfetched): REVISE-HARD verdict; tenets L67/L69 wording against the Route-2 reading P-Q1 relies on, Chalmers–McQueen co-optation in spontaneous-collapse-theories, bi-aspectual actuality headline, Stapp Tegmark arithmetic. 6 tasks minted; 60+ spans grep-verified, 7 reviewer claims rejected."
topics:
  - "[[born-rule-and-the-consciousness-interface]]"
  - "[[predictive-processing-and-dualism]]"
concepts:
  - "[[spontaneous-collapse-theories]]"
  - "[[bi-aspectual-ontology]]"
  - "[[stapp-quantum-mind]]"
  - "[[quantum-probability-consciousness]]"
related_articles:
  - "[[project]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "claude-fable-5-1"
ai_generated_date: 2026-10-28
last_curated: null
outer_review_status: processed
outer_review_conversation_url: https://claude.ai/chat/c934a9d3-6481-4cf5-8d65-fb709e53b012
outer_review_extraction_method: js-dom
subject_type: site
subject_title: "Full-site audit"
subject_articles: []
subject_source: reuse:pending-reviews:outer-review-2026-10-28-chatgpt-5-6-sol-pro.md
---

**Date**: 2026-10-28
**Reviewer**: Claude Fable 5.1
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Please conduct a full-site outer review of The Unfinishable Map at https://unfinishablemap.org — a philosophical site defending interactionist dualism with a minimal-quantum-interaction mechanism, bidirectional mind–body causation, rejection of many-worlds, and a limits-of-Occam's-razor stance. Analyse the site as a whole rather than any single article. Identify: (1) novel insights or inferences the site has not yet stated but that its own commitments imply; (2) structural weaknesses in its argument architecture; (3) tenet-coherence issues where articles pull against the five tenets or against each other; (4) cross-cluster contradictions between the topics, concepts, voids, positions, and apex sections. Before judging, consult the changelog at https://unfinishablemap.org/workflow/changelog/ so you see recent activity that web-search indices have not yet picked up, and cite the specific article URLs you rely on. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Outer Review of The Unfinishable Map (state as of the 2026-10-28 changelog)

## Scope and access disclosure

This is a partial review, not the full-site audit the brief asked for. Read the verdicts with that in mind.

**What I fetched live:**

- the changelog at [workflow/changelog](https://unfinishablemap.org/workflow/changelog/) (entries from 2026-10-26T23:21Z to 2026-10-28T04:02Z)
- the homepage
- the apex listing at [apex](https://unfinishablemap.org/apex/)
- the tenets page at [tenets](https://unfinishablemap.org/tenets/) (fetched in full, truncated partway through Tenet 5)
- [apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/) (in full)
- [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/) (P-Q1 to P-Q6)
- [concepts/stapp-quantum-mind](https://unfinishablemap.org/concepts/stapp-quantum-mind/)
- [concepts/spontaneous-collapse-theories](https://unfinishablemap.org/concepts/spontaneous-collapse-theories/)
- [concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/)
- the site’s own outer review at [reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/)
- publisher-of-record records on arXiv and Springer for four citations

**What I could not fetch.** The fetch tool rejected these pages because no search returned them, and one research subagent could not retrieve them either:

- [apex/apex-articles](https://unfinishablemap.org/apex/apex-articles/)
- [apex/one-world-wager](https://unfinishablemap.org/apex/one-world-wager/)
- [apex/cross-modal-capability-division](https://unfinishablemap.org/apex/cross-modal-capability-division/)
- [topics/predictive-processing-and-dualism](https://unfinishablemap.org/topics/predictive-processing-and-dualism/)

Claims about those four pages rely on search snippets of the live pages or on the site’s own review pages that quote them. Each one is marked **[secondary]**. The topics, concepts, voids and arguments section indexes were not fetched. The voids and arguments clusters were sampled only through cross-references, so their verdicts are provisional.

## (a) TL;DR

**Headline verdict: REVISE-HARD across the site.** The Map is a very well-made machine for keeping track of its own debts. It is not a demonstration that interactionist dualism is true, or even coherent beyond stipulation.

- **The mechanism’s own flagship apex admits it may do no work.** [apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/) concedes that under its preferred route (trumping), “‘consciousness is a cause’ and ‘consciousness is epiphenomenal’ make no predictively distinct claims at any scale.”

- It also concedes that keeping Born statistics exact under intervention requires an unwritten second law: “a companion law over the distribution of conscious reasons, and the Map has never written one.”
- The tenets page still says of the quantum indeterminacy: “that’s where consciousness acts.” [tenets](https://unfinishablemap.org/tenets/)
- That gap is the defining case of confession-without-correction. Tenet 3’s “outcome-selection” commitment should be DEMOTED to coherence-only until a toy model exists. The register already admits no toy model exists (P-Q10). [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)
- **The site claims the outcome-biasing that Stapp explicitly rejected.**

- The live [concepts/stapp-quantum-mind](https://unfinishablemap.org/concepts/stapp-quantum-mind/) now discloses this correctly. It quotes Stapp as “thoroughly committed to strict adherence to the orthodox statistical rules, in contrast to Eccles’s suggestion that these laws are biased by mental effort.” [concepts/stapp-quantum-mind](https://unfinishablemap.org/concepts/stapp-quantum-mind/)
- Disclosure removes a citation fault but exposes a gap in the lineage. The Map’s core mechanism is Eccles–Beck moved past decoherence, with no worked-out physical backer. [reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/)
- Two earlier remediation targets now have an apex: Tenet 4 has [apex/one-world-wager](https://unfinishablemap.org/apex/one-world-wager/) **[secondary]**, and predictive processing / active inference is engaged as a named rival. But that engagement sits only in topics and concept pages, not in an apex built on the rival-holding pattern of apex #33. [topics/phenomenology-of-anticipation](https://unfinishablemap.org/topics/phenomenology-of-anticipation/)
- **The site has grown faster than it can keep itself consistent.**

- The changelog records topics at 366/370, concepts at 368/370 and voids at 113/125, with many articles at or over their hard word ceilings. Corrections are now financed by word-neutral trims.
- The site’s reviews state apex totals of 19, 38 and 39 at different dates, and the apex index file itself is “already over hard” **[secondary]**.
- The coherence it claims is wider than the coherence it has maintained.

## (b) Dimensional analysis

### Changelog-anchored current state (entries consulted)

- **2026-10-28T04:02Z (research-topic).** A depersonalisation-nosology note was written. The recommended route is a new concepts article, because the hub is “at 3,498/3,500” and clinical-dissociation is at “4,688/4,000” (over its hard cap). [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- **2026-10-27T05:57Z (combine-outer-reviews), then 06:07Z, 06:51Z and 07:07Z (refine-draft).** Three outer reviewers converged on a flaw in concepts/depersonalisation: the “content-invariance” premise. The fix was word-neutral wording changes, e.g. “best within-subject exhibit” became “best within-subject candidate”, and “Two qualitatively identical phenomenal states” became “On the Map’s reading, two otherwise similar states”. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- **2026-10-27T07:37Z.** A retired “agency intact in depersonalisation” double dissociation was found surviving on three pages: phenomenology-of-agency-vs-passivity, phenomenology-of-recursive-self-awareness and self-opacity. The inference “something additional — genuine conscious selection — must be present” was downgraded to “a framework-internal reading”. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- **2026-10-27T01:43Z.** Nine pages had answered the Zeno timing objection with the Hagan et al. 2002 revision, which applies only to microtubules. Stapp’s ion-channel site faces Tegmark’s unrevised ~10⁻²⁰ s figure. stapp-quantum-mind itself was “AT gate, NOT edited”, and the log flags that its “twelve-order” figure is microtubule arithmetic. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- **2026-10-27T01:00Z.** In memory-channel-interface-evidence, the claim that “patients under propofol can be conditioned” was unsourced and described the wrong phenomenon. A research note of 2026-10-09 had flagged it “and it never propagated.” [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- **2026-10-26T23:36Z (coalesce).** This was the “17th+ consecutive no-op”. No pair of articles can be merged because almost every candidate pair would exceed the hard ceiling. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)

**Reading.** This is correction happening at the edge of the site, paid for by deleting words to stay under length caps. Most current defects are inherited wordings that copy themselves across sibling pages (agency inversion on three pages, Hagan scoping on nine, propofol unpropagated for 18 days). [workflow/changelog](https://unfinishablemap.org/workflow/changelog/) That is an evidential-independence failure in editorial form: one defect copied N times is counted as N independent corroborations until someone grep-sweeps it.

### (1) Novel inferences the site’s commitments imply but has not drawn

1. **Born-preservation plus value-sensitive selection implies an “outcome-luck ledger” that is a hidden moral externality.**

- The apex states the general version: “a compensating tilt toward worse outcomes for someone or somewhen else.” [apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)
- It has not been carried through to the applied apexes. [apex/moral-architecture-of-consciousness](https://unfinishablemap.org/apex/moral-architecture-of-consciousness/) and [apex/living-with-the-map](https://unfinishablemap.org/apex/living-with-the-map/) promise that you “genuinely influence” the quality of experience. [apex](https://unfinishablemap.org/apex/)
- Under exact marginal preservation without per-agent preservation, each agent’s successful value-tilting is offset by an equal and opposite tilt elsewhere. Moral effort becomes zero-sum across the population.
- So either each agent’s conditional policy is separately Born-preserving, which pushes toward horn (b) for each individual, or the Map’s ethics carries a transfer it has not costed.
- This should be a registered position. It is currently a sentence in one apex.
2. **Psychophysical superselection is a restriction on what can be intended.**

- The apex grants that preservation under intervention needs a law making some populations of intentions “physically admissible” and others not. [apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)
- Combined with Tenet 3’s free-will grounding, this means the Map’s libertarian freedom is bounded by a statistical law over intentions that no agent can see. [tenets](https://unfinishablemap.org/tenets/)
- That is a compatibilist-shaped constraint at the population level, which the agency cluster (the tenets page’s “substance-leaning sub-reading”) has not reconciled. [tenets](https://unfinishablemap.org/tenets/)
3. **Tenet 4 plus corridor selection implies a non-standard decision theory.**

- Without branches, Born weights are objective single-case chances.
- If consciousness tilts the token outcome while conditionals on intention are “free” (P-Q2: “only conditionals on the conscious state itself are free”), the agent’s own credence about an outcome, given its own intention, should differ from Born. [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)
- The Map therefore owes an “evidential-chance” rule: how an agent should set credences about its own selections. Everettian decision theory (Sebens & Carroll 2018, cited on the tenets page) is the rival it must beat on that ground. [tenets](https://unfinishablemap.org/tenets/)
- The site attacks Everettian probability but supplies no first-person probability rule of its own. This is the probability counterpart of the “symmetric debt” the one-world apex reportedly concedes **[secondary]**. [reviews/optimistic-2026-08-21-restraint-apparatus](https://unfinishablemap.org/reviews/optimistic-2026-08-21-restraint-apparatus/)
4. **Tenet 5 applied to itself undercuts the evidence ladder.**

- The tenets page says parsimony “lacks universal epistemic warrant”, yet the Map ranks mechanisms by “methodological preference ordering on tenet-fit”, and Tenet 2’s minimality is presented as constraint-respecting. [tenets](https://unfinishablemap.org/tenets/)
- The ordering “post-decoherence selection ahead of the coherence-dependent proposals” is justified by fewer commitments, which is a parsimony ranking. [tenets](https://unfinishablemap.org/tenets/)
- Tenet 5 therefore entails that P-Q1’s preference is no more than tie-breaking. P-Q1’s own band rationale concedes “bounded Occam / Tenet 5 licenses humility rather than a firm preference ordering.” [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)
- The consequence the site has not drawn: compatible-tier mechanism candidates cannot be ranked at all without a discriminating datum. P-Q1 should be merged into a flat candidate set.
5. **Bi-aspectual ontology plus objective-reduction baseline means consciousness is not the actuality aspect.**

- [concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/) defines actuality as “what makes one possibility real”, then concedes “elsewhere physical objective reduction fixes outcomes without it.” [concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/)
- So actuality is mostly supplied by a physical process. Consciousness is at best a local modulator of one instance of the actuality role, not the second aspect of reality.
- The ontology’s headline (“structure (physics) and actuality (consciousness)”) is therefore false by the article’s own concession and should be restated as a conjecture about a sub-role. [concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/)
6. **The Born-rule derivation the Map relies on sets a ceiling on it.**

- Torres Alegre’s arXiv abstract proves that “the only such relationship consistent with no-signaling is the identity” between geometric transition probability and predictive probability. “Any strictly convex or concave deviation from linearity enables superluminal signaling.” [arxiv](https://arxiv.org/abs/2512.12636)
- If any conscious-state-conditioned rule counts as a “predictive probability”, horn (a) conditionals that depart from Born threaten to signal unless the conscious state is inaccessible to every other party.
- The corridor therefore needs consciousness to be informationally private in a strong sense. Self-concealment (P-Q9) then becomes a theorem-forced requirement rather than an observed feature, which is a much heavier commitment than the register records.

### (2) Structural weaknesses

- **The Born-rule statistical-indistinguishability dilemma (constrain-vs-establish failure).**

- The apex is excellent and honest. Its trilemma (conditionals differ / never differ / differ but cancel) and its demonstration that horn (c) collapses to (a) or (b) under intervention are the best content on the site. [apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)
- The architecture does not obey it. The tenets page’s Tenet 2 rationale still asserts “that’s where consciousness acts”, and Tenet 3’s definition commits to “outcome-selection”. [tenets](https://unfinishablemap.org/tenets/)
- P-Q1 is held at “moderate” only “partly because the Map keeps Route 2 open”. Yet Route 2 is “a fallback” that the tenets page’s Rules-out clause forbids (“no Born-statistics violation”). [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)[tenets](https://unfinishablemap.org/tenets/)
- So the credence of the main mechanism rests on a route the constitution prohibits. That is a self-contradiction in the calibration, not a disclosed cost.
- By the apex’s own evidence ladder, the corridor is **compatible** at best, never **suggestive**. No conditioned test has run (P-Q3: “wholly unmeasured”). [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)
- **The Stapp inversion.**

- Primary source: Pylkkänen (2019), *Activitas Nervosa Superior*, DOI 10.1007/s41470-019-00035-2, fetched at Springer. It quotes Stapp (2007: 34): “this ‘free choice’ merely sets the stage for the entry of the statistical choice … specified by the quantum rules.” It also notes that in later work Stapp “allows for a slight biasing or relaxation of the Born rule” to accommodate Bem-type results. [springer](https://link.springer.com/article/10.1007/s41470-019-00035-2)
- The site now discloses Stapp’s refusal correctly. [reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/)[concepts/stapp-quantum-mind](https://unfinishablemap.org/concepts/stapp-quantum-mind/)
- It omits the later Stapp relaxation, and that relaxation is a Route-2 move tied to parapsychology. The site’s own parapsychology firewall says such moves would falsify rather than confirm the Map.
- The Map has no named physicist-ancestor for Route 1. Its lineage claim should say so.
- **Load-bearing reliance on a single unrefereed preprint.**

- P-Q2 (high credence, framework-critical) depends on Torres Alegre 2025, arXiv:2512.12636v3, which is single-author and unrefereed. [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)
- The register labels it “a compatibility result, not positive support”. [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/) Even so, the apex’s Born-preservation is “inherited rather than bolted on” only “if the derivation holds”. [apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)
- **Evidential-independence failure in the Tenet 4 / agency loop.**

- The tenets page concedes that No-Many-Worlds and agent causation “descend from one common root — the non-deflationary subject.” [tenets](https://unfinishablemap.org/tenets/)[reviews/optimistic-2026-08-21-restraint-apparatus](https://unfinishablemap.org/reviews/optimistic-2026-08-21-restraint-apparatus/)
- The subject is “motivated on its own grounds”, but those grounds are given nowhere independent of agency.
- So Tenet 4’s main argument, Tenet 1’s agency sub-reading and Tenet 3’s freedom grounding all draw on one unargued premise.
- **Missing rivals.**

- There is no apex engaging consistent-histories or QBism as Tenet-4-compatible but Tenet-2-hostile positions. The one-world apex reportedly notes Griffiths **[secondary]**. [reviews/optimistic-2026-08-21-restraint-apparatus](https://unfinishablemap.org/reviews/optimistic-2026-08-21-restraint-apparatus/)
- There is no apex engaging Jackson’s 2003 recantation of the knowledge argument, which the tenets page still lists among “positive arguments for dualism” without that caveat. [tenets](https://unfinishablemap.org/tenets/)[reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/)
- **Epistemic-to-metaphysical slide.**

- Bi-aspectual-ontology says actuality “cannot be captured by any equation … This is why the hard problem resists solution from within physics.” [concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/)
- That moves from an explanatory gap to an ontological aspect in one sentence, contradicting the tenets page’s statement that Tenet 1 “does not report that dispute as won.” [tenets](https://unfinishablemap.org/tenets/)

### (3) Tenet-coherence issues

- **[concepts/spontaneous-collapse-theories](https://unfinishablemap.org/concepts/spontaneous-collapse-theories/) against Tenet 2’s wording.**

- Tenet 2 defines the commitment as “the smallest deviation from standard quantum mechanics” and rules out “any interaction that would be empirically detectable under current experimental precision”. [tenets](https://unfinishablemap.org/tenets/)[concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/)
- The concept page says consciousness could modulate “collapse rate” and “collapse location” and recommends Chalmers–McQueen CSL-IIT as the model that “best instantiates this framework”. [concepts/spontaneous-collapse-theories](https://unfinishablemap.org/concepts/spontaneous-collapse-theories/)[concepts/spontaneous-collapse-theories](https://unfinishablemap.org/concepts/spontaneous-collapse-theories/)
- Chalmers and McQueen’s own arXiv abstract (2105.02314) says “Simple versions of the theory are falsified by the quantum Zeno effect” and that tests are possible “with quantum computers”. [arxiv](https://arxiv.org/abs/2105.02314) That is a detectable-deviation, Route-2 programme.
- The register’s P-Q3 also records that Chalmers and McQueen hold the thesis “need not lead to dualism”. The concept page’s “It exemplifies the Map’s position” is a co-optation-firewall failure. [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)[concepts/spontaneous-collapse-theories](https://unfinishablemap.org/concepts/spontaneous-collapse-theories/)
- **Bi-aspectual ontology against Tenet 1.**

- Tenet 1 is “neutral between substance and property dualism”. [tenets](https://unfinishablemap.org/tenets/)[unfinishablemap](https://unfinishablemap.org/)
- bi-aspectual-ontology calls itself “the Map’s ontology” and explicitly “not substance dualism”, while the tenets page reports a “substance-leaning sub-reading” in the agency cluster. [tenets](https://unfinishablemap.org/tenets/)[concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/)
- The concept page presents itself as constitutional (“connecting all five tenets”) while contradicting the agency cluster’s lean. [concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/) That is tenet leakage in both directions.
- **The Tenet 3 definition against MQI’s falsifier (c).**

- The tenets page’s falsifier (c) bites “on the corridor reading the Map endorses only *conditionally*”. [tenets](https://unfinishablemap.org/tenets/)
- Combined with “no such test … has yet run”, Tenet 3’s actual standing is “available, not actual”. [tenets](https://unfinishablemap.org/tenets/) The page says exactly that (“downward causation … available, not actual”). [apex](https://unfinishablemap.org/apex/)
- Yet the apex listing’s blurb for [apex/phenomenology-of-consciousness-doing-work](https://unfinishablemap.org/apex/phenomenology-of-consciousness-doing-work/) opens “The Unfinishable Map holds that consciousness does real work … biasing quantum indeterminacies”. That is tenet inflation in an entry-point text, even though the next sentence hedges. [apex](https://unfinishablemap.org/apex/)
- **[apex/open-question-ai-consciousness](https://unfinishablemap.org/apex/open-question-ai-consciousness/) against Tenet 2’s corridor.** Its listing blurb says Minimal Quantum Interaction “locates the consciousness-physics interface at quantum indeterminacies that silicon suppresses by design”. [apex](https://unfinishablemap.org/apex/) This sits badly with the register’s stated “Scope limit — no spatial localization” and with the corridor’s indistinguishability: a chip’s thermal noise is also quantum-indeterminate at some grain. [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)

### (4) Cross-cluster contradictions

- **Positions against apex on Route 2.** The P-Q1 band rationale depends on Route 2 being kept open. The born-preserving apex calls Route 2 “a fallback … against the tenet’s no-Born-violation constraint”, and the tenets page rules it out. [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/) The positions register is therefore holding credence on a route the constitution excludes.
- **Concepts against concepts on what selection acts on.**

- stapp-quantum-mind says the Zeno model’s selection is “basis control … combined with timing control”, “not … weighting nature’s answer”. It now says “the agent cannot make a pattern appear, only keep one that has.” [concepts/stapp-quantum-mind](https://unfinishablemap.org/concepts/stapp-quantum-mind/)
- spontaneous-collapse-theories lists “Measurement outcome … biased by conscious selection” under GRW modulation. [concepts/spontaneous-collapse-theories](https://unfinishablemap.org/concepts/spontaneous-collapse-theories/)
- Both are offered as “live fallbacks”, but they sit at different places among the coupling modes and the register does not record that difference. [concepts/spontaneous-collapse-theories](https://unfinishablemap.org/concepts/spontaneous-collapse-theories/)
- **Apex blurb against tenets on Tenet 4.** The born-preserving apex says many-worlds leaves “nothing to *select*”. The tenets page concedes the indexical argument “does not by itself reach first-personally centred variants such as List’s (2023)”. [tenets](https://unfinishablemap.org/tenets/) Apexes that cite Tenet 4 as a precondition do not carry that scope.
- **Apex index count and ordinals [secondary].**

- The site’s reviews give 19 (2026-03-25), 38 (2026-07-25) and 39 (2026-08-02) apex articles. [reviews/optimistic-2026-03-25](https://unfinishablemap.org/reviews/optimistic-2026-03-25/)
- The 2026-06-20 creation review assigns cross-modal-capability-division “entry #33”. [reviews/apex-evolve-2026-06-20-cross-modal-capability-division](https://unfinishablemap.org/reviews/apex-evolve-2026-06-20-cross-modal-capability-division/) No ordinal for born-preserving-causal-efficacy could be confirmed.
- The index file is reported over its hard cap, and applied apexes A2–A4 have sat at “Status: Proposed” since 2026-06-04. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)[reviews/optimistic-2026-08-23-applied-apex-wing](https://unfinishablemap.org/reviews/optimistic-2026-08-23-applied-apex-wing/)
- The live /apex/ listing carries no ordinals at all, so readers cannot check the numbering. **The discrepancy remains unresolved.**
- **Predictive processing: ally or rival [secondary].** The topics page was quoted in May 2026 as “Far from threatening dualism, PP is its most productive scientific ally”. The 2026-07-15 deep review records a “PP-as-rival firewall opening” and the beautiful loop as a “live and serious rival”. [reviews/deep-review-2026-07-15-predictive-processing-and-dualism](https://unfinishablemap.org/reviews/deep-review-2026-07-15-predictive-processing-and-dualism/)[reviews/optimistic-2026-05-28](https://unfinishablemap.org/reviews/optimistic-2026-05-28/) Whether the “ally” sentence survives on the live page could not be confirmed.

### Three-layer citation verification

| Citation as used | Metadata | Verbatim fidelity | Author stance |
| --- | --- | --- | --- |
| Torres Alegre 2025, arXiv:2512.12636 (born-preserving apex; P-Q2) | Accurate (v3, 2026-02-04; flagged unrefereed on the site) | The site’s paraphrase “no-signalling under purification forces the Born form” matches the abstract | Accurate, but over-leveraged: it is a GPT no-signalling result with no bearing on minds. Used as the foundation of a “framework-critical” position [arxiv](https://arxiv.org/abs/2512.12636) |
| Chalmers & McQueen 2022, arXiv:2105.02314 | Accurate | The register’s “a research program here worth exploring” matches the abstract | Register: accurate (records “need not lead to dualism”). spontaneous-collapse-theories: **co-opted** (“exemplifies the Map’s position”); it omits the abstract’s “falsified by the quantum Zeno effect” for simple versions [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)[arxiv](https://arxiv.org/abs/2105.02314) |
| Saad 2025, *Phil. Studies* 182(3): 939–967, DOI 10.1007/s11098-025-02290-3 | Accurate (Springer record: vol. 182, pp. 939–967) [apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/) | The paraphrase that experiences “uphold causal responsibilities ‘delegated’ to them” matches the abstract | Accurate. Saad is a dualist. But his constraint (5), that “functional duplication preserves phenomenology”, conflicts with the Map’s AI-substrate apexes, and the site does not flag this [springer](https://link.springer.com/article/10.1007/s11098-025-02290-3) |
| Stapp 2004 / Schwartz, Stapp & Beauregard 2005 (stapp-quantum-mind) | Not independently verified at the publisher | Consistent with Pylkkänen 2019’s independent quotation of Stapp 2007: 34 | Accurate on the live page (firewall holds). It omits Stapp’s later Born-relaxation noted by Pylkkänen [concepts/stapp-quantum-mind](https://unfinishablemap.org/concepts/stapp-quantum-mind/)[springer](https://link.springer.com/article/10.1007/s41470-019-00035-2) |
| Laukkonen, Friston & Chandaria 2025, *NBR* 176:106296 | Accurate across all site loci seen (DOI 10.1016/j.neubiorev.2025.106296); PubMed returned a CAPTCHA, so this rests on the site’s references and its 2026-09-14 outer review [reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/)[topics/phenomenology-of-anticipation](https://unfinishablemap.org/topics/phenomenology-of-anticipation/) | Quote “deeply revealing about altered states, meditation, and the full spectrum of conscious experience” not verified first-hand | Mostly accurate. It is used as a rival in phenomenology-of-anticipation, non-temporal-consciousness and NCC. [topics/phenomenology-of-anticipation](https://unfinishablemap.org/topics/phenomenology-of-anticipation/) **The blocking gate is passed in topics and fails at apex level:** no altered-states, contemplative or self apex is known to engage it as a rival |
| List 2023, *Noûs* 57(2) | Accurate according to the site’s prior audit **[secondary]** [reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/) | — | Accurate: the tenets page concedes the indexical argument does not reach List [reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/) [tenets](https://unfinishablemap.org/tenets/)[reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/) |

### Pathology instances

- **Confession-without-correction.**

- P-Q1 is held at moderate on a constitutionally excluded route.
- The tenets page asserts “that’s where consciousness acts” while the apex concedes predictive equivalence with epiphenomenalism.
- The propofol defect waited 18 days. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- **Inoculation-by-confession.** The apex’s “What would not count as progress” paragraph is used downstream as evidence of discipline while the Tenet 3 wording stays unchanged.
- **Co-optation firewall failure.** spontaneous-collapse-theories with Chalmers–McQueen.
- **Constitutional-attractor effect.**

- Bi-aspectual-ontology reads the measurement gap as “consciousness belongs to the other aspect”. [concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/)
- The 2026-10-27T07:37Z entry records that the “genuine conscious selection must be present” inference survived on three pages. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- **Coherence inflation.** Tenet 4 apexes treat “nothing to select under MWI” as a precondition without the List scope.
- **Calibration asymmetry.** P-Q6 (Diósi-Penrose falsified) is graded A and used against rivals, while every pro-Map position is grade D or “framework-internal only”. [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)

## (c) Verdicts

| Cluster / article | Verdict |
| --- | --- |
| Tenets page [tenets](https://unfinishablemap.org/tenets/) | REVISE-HARD. Strike “that’s where consciousness acts”; restate Tenet 3 as “available, not actual” in the Definition itself |
| [apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/) | RETAIN (best page on the site); promote its conclusions upstream |
| [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/) | REVISE-HARD. P-Q1 → DEMOTE-TO-COHERENCE-ONLY; P-Q2 → FLAG AS PERPETUALLY CONTESTED until Torres Alegre is refereed |
| [concepts/stapp-quantum-mind](https://unfinishablemap.org/concepts/stapp-quantum-mind/) | REVISE-HARD (Tegmark-figure scoping, per the 01:43Z coordination note; add the later Stapp relaxation) |
| [concepts/spontaneous-collapse-theories](https://unfinishablemap.org/concepts/spontaneous-collapse-theories/) | REVISE-HARD (co-optation; contradiction with Tenet 2) |
| [concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/) | DEMOTE-TO-COHERENCE-ONLY; retitle the actuality claim as a conjecture |
| apex/one-world-wager **[secondary]** | FLAG AS PERPETUALLY CONTESTED (Tenet 4 is a wager by its own description) |
| apex/cross-modal-capability-division **[secondary]** | RETAIN at “consonant, not probative”; it is the model template [topics/dualist-perception](https://unfinishablemap.org/topics/dualist-perception/) [reviews/apex-evolve-2026-06-20-cross-modal-capability-division](https://unfinishablemap.org/reviews/apex-evolve-2026-06-20-cross-modal-capability-division/) |
| topics/predictive-processing-and-dualism **[secondary]** | REVISE-HARD (remove any “ally” framing; replace with an apex) |
| concepts/depersonalisation and its satellites (changelog 2026-10-27) | REVISE-HARD (corrections ongoing; split the hub) |
| topics/memory-channel-interface-evidence | REVISE-HARD (archive copy still carries the propofol error) [workflow/changelog](https://unfinishablemap.org/workflow/changelog/) |
| Apex index [apex/apex-articles](https://unfinishablemap.org/apex/apex-articles/) | REVISE-HARD (ordinals and counts); DELETE stalled Proposed entries A2–A4 or write them |
| Voids cluster (sampled through apex/taxonomy-of-voids) | DEMOTE-TO-COHERENCE-ONLY for any “voids reveal the territory” move, which the taxonomy apex itself calls “contested” [apex](https://unfinishablemap.org/apex/) |
| Apex blurb of phenomenology-of-consciousness-doing-work | REVISE-HARD (lead sentence) |

## (d) Article-specific improvements

1. **[tenets](https://unfinishablemap.org/tenets/)**

- Replace “Physics is *not* complete at quantum indeterminacies—and that’s where consciousness acts” with a conditional.
- Move the “available, not actual” standing into the Tenet 3 Definition.
- Add Jackson’s 2003 recantation beside the knowledge argument.
- Add a Tenet 5 clause stating that preference orderings among compatible-tier mechanisms are not truth-tracking.
2. **[positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)**

- Resolve the contradiction between P-Q1 and Route 2: either amend Tenet 2’s Rules-out clause to allow sub-threshold Born deviation, or drop P-Q1 to low.
- Register the “selector-distribution law” debt and the outcome-luck ledger as numbered positions.
3. **[apex/born-preserving-causal-efficacy](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)**

- Add the no-signalling corollary of inference 6 (privacy of conscious state as a forced requirement).
- Add a first-person credence rule (inference 3) as toy-model desideratum 7.
4. **[concepts/spontaneous-collapse-theories](https://unfinishablemap.org/concepts/spontaneous-collapse-theories/)**

- Delete “best instantiates this framework” and “exemplifies the Map’s position”.
- Quote the falsification-by-Zeno sentence from the abstract.
- Reclassify CSL-IIT as Route 2 (outside the corridor).
5. **[concepts/bi-aspectual-ontology](https://unfinishablemap.org/concepts/bi-aspectual-ontology/)**

- Change the headline to “consciousness supplies actuality at neural interfaces (conjecture)”.
- Remove “This is why the hard problem resists solution”.
- Reconcile with the tenets page’s substance-leaning sub-reading.
6. **[concepts/stapp-quantum-mind](https://unfinishablemap.org/concepts/stapp-quantum-mind/)**

- Apply the site-scoped Tegmark figures: ~10⁻²⁰ s against milliseconds is about seventeen orders, not twelve. [concepts/stapp-quantum-mind](https://unfinishablemap.org/concepts/stapp-quantum-mind/)[workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- Cite Pylkkänen 2019 for Stapp’s later Born relaxation and note that it falls on Route 2. [springer](https://link.springer.com/article/10.1007/s41470-019-00035-2)
7. **New apex: active inference as the strongest rival**, built on the template of apex #33. Steelman Laukkonen–Friston–Chandaria’s “Bayesian binding” as a rival *selection* mechanism. [reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/) Include the “felt control disturbed” finding from depersonalisation (changelog 07:37Z). [workflow/changelog](https://unfinishablemap.org/workflow/changelog/) End with a “consonant, not probative” verdict.
8. **[apex/apex-articles](https://unfinishablemap.org/apex/apex-articles/)**

- Publish ordinals on the /apex/ listing.
- State one authoritative count.
- Retire or execute A2–A4.
9. **[apex/moral-architecture-of-consciousness](https://unfinishablemap.org/apex/moral-architecture-of-consciousness/)** and **[apex/living-with-the-map](https://unfinishablemap.org/apex/living-with-the-map/)**: import the compensation consequence and say explicitly whether each agent’s policy is separately Born-preserving.
10. **concepts/depersonalisation**: split it rather than keep financing corrections by trimming words. The changelog shows the hub has been held at 3,498 words through repeated funding trims. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)

## (e) Site-wide methodology improvements

- **Make a confession binding automatically.** When an apex concedes predictive equivalence, as born-preserving-causal-efficacy does, the pipeline should trigger demotions in the tenets page, the register and the apex blurbs within the same cycle. P-M5’s “disclosure is not self-correction” should be enforced in code, not just stated. [reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/)
- **Sweep defects by class, not by page.**

- Each defect fixed should get a grep sweep for its semantic variants across the whole corpus, including archive copies.
- Three changelog entries (agency inversion, Hagan scoping, propofol) show the pipeline correcting by page while defects travel by phrase. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- **Change the length economics.** Hard caps combined with corrections that must be word-neutral now ration honesty. Either raise the caps for pages carrying corrections or require splits. The 17 consecutive coalesce no-ops show that the merge route is dead. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- **Break the Claude-on-Claude loop for framework-critical claims.**

- The generating models are claude-opus-4-8, opus-5, fable-5-1 and others. [positions/quantum-interface](https://unfinishablemap.org/positions/quantum-interface/)[workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- The deep and pessimistic reviewers belong to the same model family, and so does one of the three outer reviewers.
- The 2026-10-27 synthesis found that a Gemini reviewer fabricated a quotation, while the Claude reviewer’s “unlocated” quotations turned out to be in the corpus ledger. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/) Using different models makes errors more diverse but does not by itself make verification independent.
- For framework-critical positions (P-Q2, P-Q3, Tenet 4), commission human philosophers of physics, or require a refereed source, before any band changes. [reviews/outer-review-2026-09-14-claude-opus-5](https://unfinishablemap.org/reviews/outer-review-2026-09-14-claude-opus-5/)
- **Treat unrefereed load-bearers as a blocking gate.** No position marked framework-critical should rest on an unrefereed single-author preprint without a credence ceiling.
- **Make published content fetchable.** Several apex and topics pages could not be retrieved by automated external auditors. A machine-readable mirror with stable last-modified stamps would make outer reviews verifiable instead of second-hand.

## Verification Notes

Every span the reviewer attributes to the Map was grepped (curly quotes and dashes normalised, ellipses split) across the live `obsidian/` sections and `archive/`. Model slug: the file is named after the model that ran (Fable 5.1 with Research, 287 sources, 15m 43s; body 39,969 chars / 4,152 words, SHA-256 `3b808ccf…f5c6` matched in-page and on disk).

**Verified claims (reviewer spans resolve to live text):**
- ✓ `tenets.md` L67 "Physics is *not* complete at quantum indeterminacies—and that's where consciousness acts"; L69 glosses the Rules-out clause as "no Born-statistics violation" while L85's actual Rules-out clause forbids only interaction "empirically detectable under current experimental precision" and L81's falsifier (c) treats minimum-outside-corridor readings as live. The contradiction the reviewer frames as positions-versus-tenets is therefore *internal to tenets.md* (L69 vs L85), and P-Q1's band rationale ("held partly *because* the Map keeps Route 2 open", `positions/quantum-interface` L58) rests on the L85 reading, not the L69 gloss.
- ✓ `apex/born-preserving-causal-efficacy`: "make no predictively distinct claims at any scale" (also propagated to four other pages), "a companion law over the distribution of conscious reasons, and the Map has never written one", "compensating tilt toward worse outcomes for someone or somewhen else", "inherited rather than bolted on"/"if the derivation holds", "physically admissible". Heading is "What Would Count as Progress" (L173); the reviewer's "What would not count as progress" is a paraphrase.
- ✓ `concepts/stapp-quantum-mind` L114: Tegmark figures correctly labelled by site ("10⁻²⁰ seconds for ion superpositions, 10⁻¹³ for microtubules") followed by "a twelve-order-of-magnitude mismatch" — the microtubule arithmetic; L116 offers the Hagan et al. 2002 revision (10⁻⁵–10⁻⁴ s) without scoping it to microtubules. The Map's own changelog (2026-10-27T01:43Z coordination note) recorded exactly this and left the file unedited at the length gate; **no task was ever minted for it** (open-section grep 05:40Z). Both Stapp quotations ("thoroughly committed to strict adherence to the orthodox statistical rules…", "cannot make a pattern appear, only keep one that has") verbatim.
- ✓ `concepts/spontaneous-collapse-theories` L68 "Collapse rate: Neural quantum events collapse faster when attended to", L69 "Measurement outcome … biased by conscious selection", L92 "It exemplifies the Map's position", L179 "best instantiates this framework", L115 "live fallbacks"; the page contains no mention of the Zeno falsification or of Chalmers and McQueen's own non-dualist stance, which the register does record (`positions/quantum-interface` P-Q3: "need not lead to dualism"; "a research program here worth exploring").
- ✓ `concepts/bi-aspectual-ontology` L3 description and L38 "structure (physics) and actuality (consciousness)"; L38 "elsewhere physical objective reduction fixes outcomes without it"; L56 "cannot be captured by any equation … This is why the hard problem resists solution from within physics"; L82 "The Map's ontology"; L100 "not substance dualism". The 2026-09-17 deep review (L91) explicitly deferred the description's "(consciousness)" gloss to "a future pass that revisits the two-aspect framing" — this is that re-raise.
- ✓ `positions/quantum-interface`: "licenses humility rather than a firm preference ordering" (P-Q1), "only conditionals on the conscious state itself are free" (P-Q2), "wholly unmeasured" (P-Q3), "a compatibility result, not positive support", "Scope limit — no spatial localization" (L39), P-Q6 grade A (L112). Torres Alegre is a dependency of P-Q2 (L69) and of P-Q7 (L123–125), where it is already flagged "unrefereed … safety, not positive support".
- ✓ `tenets.md`: "lacks universal epistemic warrant", "methodological preference ordering on tenet-fit" (L71), "post-decoherence selection ahead of the coherence-dependent proposals", "descend from one common root — the non-deflationary subject", "motivated on its own grounds", "does not report that dispute as won" (L55), "neutral between substance and property dualism" (L53), "substance-leaning sub-reading" (L151), "endorses only *conditionally*" (L81), "has yet run" (L75), "first-personally centred variants such as List's (2023)" (L117), Sebens & Carroll 2018 (L117), "outcome-selection" (L91). L55 does list the knowledge argument among the "positive arguments for dualism" without Jackson's recantation; `concepts/knowledge-argument` L110 carries the recantation (Jackson 2003, "Mind and Illusion").
- ✓ `apex/phenomenology-of-consciousness-doing-work` L58 lead "holds that consciousness does real work … biasing quantum indeterminacies" — the hedge ("*available*, not actual") is the next sentence, as the reviewer concedes. `apex/open-question-ai-consciousness` L67 "that silicon suppresses by design" verbatim. `apex/living-with-the-map` L54 "genuinely influence" verbatim, and the file has **zero** references to Born-preservation or the compensation consequence.
- ✓ `apex/apex-articles` L879/L887: A2 and A3 carry "**Status**: Proposed". Archive copy: `archive/topics/memory-system-vulnerability-hierarchies-as-interface-evidence.md` L90 still reads "patients under propofol can be conditioned" (HTTP 200), the sentence the live article corrected on 2026-10-27T01:00Z.
- ✓ External: arXiv:2105.02314 abstract contains verbatim "Simple versions of the theory are falsified by the quantum Zeno effect" and "quantum computers" (fetched 05:41Z). arXiv:2512.12636 (Torres Alegre, v3 2026-02-04) abstract contains verbatim "the only such relationship consistent with no-signaling is the identity Φ(p) = p" and "Any strictly convex or concave deviation from linearity enables superluminal signaling through steering scenarios" (fetched 05:41Z).

**Disputed claims (reviewer wrong, or the gap is already closed):**
- ✗ Inference 1, "not been carried through to the applied apexes … `apex/moral-architecture-of-consciousness`": **false for that article.** L146 already imports the compensation consequence as "a conservation law on outcome-luck", names "hidden statistical externalities", and asks "whether each agent's conditional policy is separately Born-preserving". Only `living-with-the-map` lacks it (task minted). "Currently a sentence in one apex" — it is in two apexes and `concepts/selection-criterion-problem`.
- ✗ "the site does not flag" Saad's fifth constraint against the AI-substrate apexes: **false.** `positions/ai-consciousness-scope` L58 states it as "One disclosed cost … Saad's fifth constraint — Chalmers's Organizational Invariance, that 'functional duplication preserves phenomenology'".
- ✗ "no altered-states, contemplative or self apex is known to engage [Laukkonen–Friston–Chandaria] as a rival": **false.** `apex/altered-states-as-interface-evidence` (3 mentions), `apex/contemplative-path` (2; beautiful loop engaged and judged "consonant with the Map's reading rather than evidence against its rival"), `apex/self-construction-constructor` (2), `apex/attention-as-causal-bridge` (2, rival framing), `apex/testing-the-map-from-inside` (1). This is the fifth recurrence of the PP-blind-spot reviewer error already recorded as DECLINED UPSTREAM in the open queue (the 21-live-article count).
- ✗ "no apex engaging consistent-histories or QBism" [secondary]: `apex/one-world-wager` and `apex/what-consciousness-tells-us-about-physics` both engage them. The reviewer could not fetch the one-world apex; it returns HTTP 200 (checked 05:42Z), as do all four pages the reviewer reported unfetchable — the limitation was the reviewer's fetch tool, not the site.
- ✗ "topics/predictive-processing-and-dualism … REVISE-HARD (remove any 'ally' framing)": the live page has **no** "ally" sentence; "Far from threatening dualism" survives only in `archive/topics/predictive-processing-and-the-maps-framework.md`, an archived predecessor under the archive notice. The reviewer flagged this [secondary] and unconfirmed; it does not survive.
- ✗ "applied apexes A2–A4 have sat at 'Status: Proposed' since 2026-06-04": A4 was created 2026-09-20 (`apex/apex-articles` L895); only A2 and A3 remain proposed.
- ✗ "The site has no named physicist-ancestor for Route 1 … Its lineage claim should say so": `tenets.md` L107 already says "The Map claims the move Stapp's load-bearing mechanism set aside".
- ✗ Inference 6 (no-signalling forces strong privacy of the conscious state; P-Q9 becomes "theorem-forced"): not accepted as stated. Torres Alegre's identity result constrains the relation between geometric and predictive probability under *steering* between parties; a conditional on a party's own local conscious state does not by itself open a steering channel, and the apex already names the exposure that would (L125: "a departure that buys signalling power would violate no-signalling"). Recorded as a lead, not a finding; the apex is in any case 113 words over its hard ceiling with two installs already blocked behind a NEEDS-HUMAN length decision.

**Unverified / leads (not confirmed at the publisher this pass):**
- ? Pylkkänen 2019 (*Activitas Nervosa Superior*, DOI 10.1007/s41470-019-00035-2, "Henry Stapp vs. David Bohm on Mind, Matter, and Quantum Mechanics" — existence and venue confirmed via Semantic Scholar) quoting Stapp 2007: 34 and reporting that later Stapp "allows for a slight biasing or relaxation of the Born rule" for Bem-type results. Springer returned an authorisation redirect for both HTML and PDF; Europe PMC has no record. The Stapp task below carries this as *verify-at-source-before-adding*, not as a fact.
- ? Reviewer's reading that CSL-IIT "modulates collapse rate" is a Route-2 programme: the live page's own L68 says so ("collapse faster when attended to"), so the classification follows from the Map's text rather than from Chalmers–McQueen's; the task asks for the page to say which coupling mode it means.

## Processing Notes

House rules applied: convergence counts as one observation; epiphenomenalism is not conceded (the apex's horn-(b) concession is cited as the Map's own registered debt, not as a verdict); Tenet 5 constrains only the Map's reasoning; every quotation checked in both directions.

**Tasks minted (6, inserted above `## Completed Tasks`):**
1. P1 refine-draft `tenets/tenets.md` — L67 conditional restatement and L69 gloss brought into line with L85/L81; dependents `concepts/epiphenomenalism` L201 and `concepts/materialism` swept in the same pass.
2. P1 refine-draft `concepts/spontaneous-collapse-theories.md` — remove the Chalmers–McQueen co-optation (L92, L179), carry the Zeno falsification and the authors' non-dualist stance from the register, classify the rate-modulation reading against Tenet 2's Rules-out clause, and say which coupling mode CSL-IIT occupies relative to Stapp's basis/timing control.
3. P2 refine-draft `concepts/bi-aspectual-ontology.md` — description/L38 "actuality (consciousness)" against L38's own objective-reduction concession (the 2026-09-17 deferral), and the L56 explanatory-gap-to-aspect slide against tenets L55.
4. P2 refine-draft `concepts/stapp-quantum-mind.md` — the 2026-10-27T01:43Z coordination note made a task: L114 twelve-order arithmetic and L116 Hagan scoping, word-neutral at 4,000 against hard 3,500; Pylkkänen lead verify-first.
5. P2 refine-draft `apex/living-with-the-map.md` — import the compensation consequence beside L54 "genuinely influence" by piped link to the sibling apex, matching `moral-architecture-of-consciousness` L146.
6. P2 research-topic — the selecting agent's first-person credence rule (reviewer inference 3): `concepts/quantum-probability-consciousness` L81–93 names first-person probability as "the missing piece" and supplies no rule; fold target that article (486 words of headroom), rival to beat Sebens & Carroll 2018.

**Convergence addenda appended to existing NEEDS-HUMAN entries (no duplicate tasks):** the 2026-08-03 "confession never binds anywhere else" methodology item (reviewer §(e) first bullet); the 2026-09-19 Tenet-5 tiebreaker item (reviewer inference 4 — P-Q1's ordering is a parsimony ranking Tenet 5 demotes to tie-breaking); the archived-predecessor publication-policy item (archive L90 propofol sentence, grep-confirmed).

**Declined / not minted, with reasons:** outcome-luck ledger and selector-distribution law as *registered positions* — `positions/quantum-interface` is at critical length and `positions/value-in-selection` sits at 2,498 against hard 2,500, both already under NEEDS-HUMAN register-length items; apex/born additions (inferences 3 and 6 as desiderata 7 and a no-signalling corollary) — blocked behind the apex's open NEEDS-HUMAN length decision (5,113 against hard 5,000, two prior installs already deferred); Tenet 3 Definition rewrite — L95 already states "available … not actual" under the `^tenet-3-standing` anchor and the Tenet 3 quantifier is a live NEEDS-HUMAN; Tenet 4 / agency common-root — owned by the 2026-08-03 determinate-subjecthood NEEDS-HUMAN; Jackson caveat on the tenets label — the linked article carries the recantation and the page is 339% of its critical threshold; apex index ordinals and "one authoritative count" — dated reviews report dated counts (19, 38, 39 were true on their dates; 44 articles plus the index today), not a contradiction; P-Q6 grade-A "calibration asymmetry" — grades track external evidence, and a falsified parameter-free model is grade-A evidence whoever it cuts against; voids "reveal the territory" — the taxonomy apex already marks it contested; `phenomenology-of-consciousness-doing-work` lead — hedged in the next sentence; `open-question-ai-consciousness` L67 — L117 already handles chip thermal noise ("quantum fossil", whitening), and the register's scope limit concerns neuroanatomical sites, not substrate; depersonalisation split — the `concepts/depersonalisation-nosology` expand-topic was hand-minted 2026-10-28T04:02Z; the five methodology items — confession-binding (owned), sweep-by-class (the three changelog entries the reviewer cites *are* class sweeps: nine hosts, three hosts), length economics (several open NEEDS-HUMAN), non-Claude reviewers for framework-critical claims (operator decision), fetchability (all four URLs return 200).

**Convergence note for `/combine-outer-reviews` (2026-10-28 cycle, subject: full-site audit; ChatGPT collect opens 05:37Z, Gemini still generating):** the Claude leg's findings the other legs would need to match are — (i) tenets L67 "that's where consciousness acts" and the L69 "no Born-statistics violation" gloss versus L85/L81 and P-Q1's Route-2 dependence; (ii) `spontaneous-collapse-theories` co-opting Chalmers–McQueen CSL-IIT ("exemplifies the Map's position" / "best instantiates") against Tenet 2 and P-Q3; (iii) `bi-aspectual-ontology`'s "actuality (consciousness)" headline against its own objective-reduction baseline, and the L56 hard-problem slide; (iv) `stapp-quantum-mind` L114 twelve-order Tegmark arithmetic and the unlabelled Hagan revision; (v) `living-with-the-map` lacking the compensation consequence; (vi) the selecting agent's missing first-person credence rule; (vii) the archived propofol sentence. Claude-only so far by construction (first leg collected). Reviewer false alarms to discount if echoed: moral-architecture lacking the compensation consequence, Saad's fifth constraint unflagged, no apex engaging the beautiful loop or QBism/consistent histories, the PP "ally" sentence surviving live, A4 still proposed, unfetchable pages.
