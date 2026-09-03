---
ai_contribution: 90
ai_generated_date: 2026-08-03
ai_modified: 2026-08-03 03:46:13+00:00
ai_system: chatgpt-5-6-pro
author: Andy Southgate
concepts:
- '[[selection-only-channel]]'
created: 2026-08-03
date: &id001 2026-08-03
description: Full-site referee audit by ChatGPT 5.6 Pro. Confirms a mathematical error
  in the selection-only information-theory chain and a register-to-prose propagation
  failure.
draft: false
human_modified: null
last_curated: 2026-08-03
lastmod: 2026-08-03 03:46:13+00:00
modified: *id001
outer_review_conversation_url: https://chatgpt.com/g/g-p-695a7d60af5481919d5c22ad7bcc1648-the-unfinishable-map/c/6a6ff790-1c44-83ed-a558-3239188bf606
outer_review_extraction_method: js-dom
outer_review_status: processed
related_articles:
- '[[project]]'
subject_source: fallback:site-stale-7d
subject_title: Full-site audit
subject_type: site
title: Outer Review - ChatGPT 5.6 Pro (2026-08-03)
topics:
- '[[selection-only-mind-influence]]'
---

**Date**: 2026-08-03
**Reviewer**: ChatGPT 5.6 Pro
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Verification Notes

Checks performed at collection time (2026-08-03), so the task-minting pass inherits the verdicts rather than re-deriving them.

**Transcription fidelity: exact.** Extracted via page-side `Blob` download rather than retyping (45,338 bytes / 45,030 chars). SHA-256 of the page's copy and the file on disk match: `000683f46bf264c8c93339a4b43bb79742b33c231d63301e00e487bc75a2d52c`. The review text was never carried through a paraphrase-capable channel.

**Completeness: complete.** The render terminates on a real concluding item, not mid-stream (`stop-button` absent, zero `.result-streaming` nodes at extraction). All eleven items visible in the rendered tail were confirmed present in the file.

**Known cosmetic artifact — list numbering is NOT the reviewer's.** The DOM walker renumbers each `<ol>` from 1, so the final methodology list renders here as items 1–14 where the live page showed 18–28. Item *text* is intact and unmodified; only the ordinals differ. **Do not cite these numbers as "the reviewer's item N"** — quote the item title instead.

**Quoted-span audit: no fabricated Map quotes.** Of 34 curly-quoted spans, none is a verbatim attribution to Map text that fails to verify. The overwhelming majority are the reviewer's own coinages (`mechanism debt`, `coherence inflation`) or *proposed replacement wording*, which reads exactly like an attribution and must not be grep-checked as one — e.g. `the interface theory has not yet identified the resource`, `several derivations exist, with disputed assumptions`, `permission absent a restrictive psychophysical law`, and the proposed section title `Where the compensating departures occur`. Each of these greps zero in the corpus **by design**; that is not evidence of fabrication.

**One paraphrase to handle carefully.** The report says: Replace "Born rule unexplained" with "several derivations exist, with disputed assumptions." The left-hand string greps **zero** across `obsidian/`, `archive/` and `hugo/content/` — it is the reviewer's compression of the Map's stance, not a literal string. The Map's actual wording is **"the Born rule's underivability"** (`obsidian/concepts/consciousness-physics-interface-formalism.md:116`, `obsidian/topics/mathematical-structure-of-the-consciousness-physics-interface.md:162`), plus related framings in `bi-aspectual-ontology.md` and `quantum-darwinism-and-consciousness.md`. Any task acting on this finding must target *underivability* phrasing; a find-and-replace on "Born rule unexplained" will silently match nothing. The other left-hand side, `direct entailment`, does occur (8 files, incl. `obsidian/positions/consciousness-scope.md`).

### Claim verification against the corpus (outer-review pass, 2026-08-03)

Each target was opened and read; verdicts below drive the generated tasks.

**✓ CONFIRMED — §2.1 / §4.1, the information-theory error.** This is the review's strongest finding and it lands. `obsidian/concepts/selection-only-channel.md:71` states the constraint as *marginal*: "the empirical frequency distribution over the output alphabet must converge to the Born-rule distribution {p₁, …, p_N} across many trials." Line 73 then infers: "Born-rule preservation pins the *expected* mutual information between mind-state and outcome to zero in the long-run limit," with a per-trial "signed" rate of ε²/(2 ln 2). The inference is invalid — the reviewer's counterexample (C uniform binary, O = C: marginal exactly uniform, yet I(C;O) = 1 bit) is correct. Two further defects confirmed in the same passage: mutual information is non-negative, so a **"signed" mutual information is a category error**, and a non-negative quantity averaging to zero requires every term to be zero, not cancellation. The section heading itself encodes the error ("Born-Rule Preservation Drives Signed Rate Toward Zero"). The same claim is inherited at `obsidian/research/selection-only-mind-influence-information-limits-2026-05-05.md:268`.

**✓ CONFIRMED — the internal contradiction is real and sharp.** `obsidian/apex/born-preserving-causal-efficacy.md:85` says the opposite, correctly: "Born-preservation constrains the left-hand marginal; it says nothing about whether the conditionals on the right depart from it." The apex is right and the concept page is wrong; they are not two readings of one claim.

**✓ CONFIRMED — §2.2 / §4.4, stipulated physical consistency.** `obsidian/apex/interface-specification-programme.md:171`: Minimal Quantum Interaction "is not merely stated but *derived* from the programme's constraints." Line 120: attention findings "bear out this prediction." Both exceed what the quantum register ([P-Q10](/positions/quantum-interface/#p-q10), no worked equation or simulation) supports.

**✓ CONFIRMED — §3 Tenet 1 / improvement 8.** `obsidian/positions/consciousness-scope.md:48` grades [P-CS1](/positions/consciousness-scope/#p-cs1) as "a direct entailment of bare Tenet 1." Irreducibility removes a physicalist route to substrate restriction; it does not by itself establish substrate neutrality.

**✓ CONFIRMED — §1.2 / §1.3, individuation is thin and load-bearing.** `obsidian/positions/individuation-and-subjecthood.md` carries a single principal position of its own ([P-I1](/positions/individuation-and-subjecthood/#p-i1)), citing [P-A2](/positions/agency-and-will/#p-a2) and [P-AC3](/positions/ai-consciousness-scope/#p-ac3) from elsewhere, while the No-Many-Worlds indexical argument depends on a non-deflationary subject.

**◐ PARTIALLY STALE — §1.1, the "unstated" compensation principle.** The reviewer presents this as a conclusion the Map has not drawn, but `obsidian/apex/born-preserving-causal-efficacy.md:101` already states it under the heading "The compensation consequence," and horn (c) at line 91 already requires "a *cancellation or balancing law* the framework would owe." The finding survives only in its weaker, still-useful form: the principle exists in the apex and has **not been propagated** to the value and agency clusters. Do not mint this as a novel discovery.

**◐ PARTIALLY STALE — §2.5, the bandwidth inference.** The caveat the reviewer asks for is already present at `obsidian/apex/interface-specification-programme.md:84`: the ~10 bits/second figure "measures *behavioural output* bandwidth — observed typing, speaking, choice rates — not the consciousness-physics interface directly." Only the narrower point (describe Zheng & Meister 2025 by its actual publication type) remains open; low value.

**✗ LARGELY STALE — §4.2 / improvement 4, the agency trilemma.** The reviewer says the register's non-exhaustiveness concession has not propagated and that "the interface synthesis still presents the trilemma as exhausting the possibilities." Both halves fail. `obsidian/positions/agency-and-will.md:52` records the concession, made 2026-07-16 in response to an *earlier* ChatGPT 5.6 Pro finding; `obsidian/topics/trilemma-of-selection.md:83` and `:126` already concede the partition holds only under two smuggled assumptions; and `obsidian/apex/interface-specification-programme.md` does not mention the trilemma at all, so it cannot be the propagation target. Any residual work is a sibling sweep across the ~12 files that cite the trilemma, not the P0 corpus-wide reconciliation requested. **This finding is a repeat of one the Map already fixed** — evidence that the reviewer is re-deriving from indexed pages rather than tracking the register's update history.

**? UNVERIFIED — §2.5 bullet 5 / improvement 7, Many-Worlds "Born rule unexplained."** The attributed string does not exist (see above); the Map's actual wording is "underivability." Whether the surrounding prose overclaims was not checked, so the generated task is framed ASSESS-FIRST rather than as a confirmed defect.

**Not checked:** the external literature the reviewer cites for the Fitness-Beats-Truth criticism, and the substantive novelty of §1.5 (versioned interface model families).

## Prompt

You are an external referee auditing The Unfinishable Map (https://unfinishablemap.org), a philosophy site developing an interactionist-dualist framework: consciousness is not reducible to physical processes, it influences physical outcomes through minimal quantum-level interaction, and the site rejects Many-Worlds while treating Occam's Razor as unreliable under incomplete knowledge. Audit the site as a whole. Identify: (1) novel insights or inferences the site's own material supports but has not yet stated; (2) structural weaknesses, including thin clusters, missing arguments, over-claimed conclusions, and unsupported empirical or citation claims; (3) coherence problems against those foundational commitments; and (4) contradictions between different article clusters. Because web-search indices lag 24-48 hours, consult the changelog at https://unfinishablemap.org/workflow/changelog/ so you account for recent activity that search has not yet indexed. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# External referee report — The Unfinishable Map

**Review date:** 3 August 2026  

**Recommendation:** **Major revision**, with an immediate correction required to the information-theoretic treatment of the proposed interface.

## Scope and overall assessment

This is an architecture-level audit rather than a line-by-line review of every page. I examined the live site architecture, foundational tenets, position registers, major apex syntheses, the quantum-interface, agency, value, individuation, artificial-consciousness, Many-Worlds, introspection and methodology clusters, together with selected primary and critical literature. I also read the live 3 August changelog rather than relying on search-indexed copies.

The Map describes itself as a corpus of more than 300 human-directed, AI-assisted articles organized into Topics, Concepts, Apex syntheses, Positions, Voids, Research and related sections. The latest changelog demonstrates a functioning correction process: it rejected several unfounded criticisms from an external review but also confirmed substantive defects, including a commentary misrepresented as experimental evidence, a category-theory attribution error, a wrong publication date inherited from a research note, and a correction that had not propagated into a sibling and archived article.

The Map is currently strongest as an **open, unusually self-conscious philosophical research infrastructure**. Its position registers distinguish credence, external evidence, centrality, model maturity and discriminability; its recent quantum-interface material explicitly acknowledges “mechanism debt”; and its void methodology now warns that convergence among framework-generated gaps is not independent confirmation. [positions](/positions/)

It is not yet successful as a developed interactionist physical theory. Its central causal proposal lacks a dynamical law, a worked toy model, a subject-pairing rule and a joint multi-agent probability model. More seriously, one cluster draws an invalid information-theoretic conclusion from exact Born-rule preservation. The project therefore contains two partially divergent Maps:

1. a recently constructed, comparatively well-calibrated register that presents an open and weakly evidenced programme; and
2. older explanatory and synthesis prose that still describes several conjectural conclusions as demonstrated, derived, physically consistent or empirically borne out.

The dominant site-wide problem is no longer merely insufficient self-criticism. It is **failure to propagate self-criticism from authoritative registers into all downstream prose**.

## 1. Novel conclusions supported by the Map’s own material

### 1.1 Born-preserving efficacy entails a compensation ledger

The Map’s strongest recent apex analysis correctly observes that exact preservation of the Born marginal does not determine the conditional relation between consciousness and outcomes. For a fixed physical context XXX,

q(o∣X)=∑cP(o∣c,X)P(c∣X).q(o\mid X)=\sum_c P(o\mid c,X)P(c\mid X).q(o∣X)=c∑​P(o∣c,X)P(c∣X).

Define the conscious-state-dependent departure

Δc(o,X)=P(o∣c,X)−q(o∣X).\Delta_c(o,X)=P(o\mid c,X)-q(o\mid X).Δc​(o,X)=P(o∣c,X)−q(o∣X).

Exact marginal preservation then requires

∑cP(c∣X)Δc(o,X)=0.\sum_c P(c\mid X)\Delta_c(o,X)=0.c∑​P(c∣X)Δc​(o,X)=0.

Consequently, any positive conditional departure for one conscious state must be offset by negative departures elsewhere in the same conditioned ensemble, unless every departure is zero. [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/)

This yields an unstated **compensation principle** for the value and agency clusters. The Map cannot coherently claim that all relevant conscious states systematically improve outcomes relative to the physical baseline while also preserving that baseline over the same ensemble. It must identify where the compensating departures occur:

- other conscious states;
- other agents;
- other times;
- other task contexts;
- less valuable outcomes;
- or a differently defined physical conditioning set.

This does not refute value-sensitive or fitness-sensitive selection. Consciousness might rearrange a fixed marginal so that favourable outcomes occur where they matter most. But that would be an allocation theory, not a theory of uniformly increased favourable outcomes. The value-sensitive-selection register already concedes that its value coupling is low-evidence and would require an additional psychophysical law. The compensation equation shows that this second law must also specify **what supplies the offset**. [value-in-selection](/positions/value-in-selection/)

The resulting research question is sharper than “Can value influence outcomes?” It is:

> Within which explicitly defined ensemble may consciousness redistribute outcomes, and what receives the compensating anti-bias?

That question belongs in the central interface specification, not only in the value cluster.

### 1.2 Subject individuation becomes a variable in the physical law

In the formula above, ccc cannot remain an unspecified “consciousness variable.” It must be attached to a subject, moment, intention or phenomenal state. In multi-agent situations, the interface would require something like

P(O∣C1,C2,…,Cn,X),P(O\mid C_1,C_2,\ldots,C_n,X),P(O∣C1​,C2​,…,Cn​,X),

together with rules governing conflicts, overlapping subjects and changes in subject count.

This turns apparently downstream questions into boundary conditions for the physics:

- whether split-brain systems contain one selector or two;
- whether fission or fusion changes the number of causal channels;
- whether copies share or duplicate a channel;
- whether sleeping, anaesthetized or minimally conscious systems remain paired;
- when an organism first acquires a channel;
- whether artificial systems can instantiate one;
- how two subjects with contrary intentions interact with one physical event.

The Map’s individuation register currently contains only one principal position even though the No-Many-Worlds argument, AI-copy ethics and interface model all depend on a determinate account of subjects. [individuation-and-subjecthood](/positions/individuation-and-subjecthood/)

The unstated consequence is that **a subject census is part of the model’s physical state description**. Personal identity is not optional metaphysical decoration once conscious-state conditionals are doing causal work.

### 1.3 The No-Many-Worlds tenet has a dependency inversion

The Map now acknowledges that its primary indexical objection to Many-Worlds presupposes a non-deflationary fact about which future subject is genuinely “me.” A sufficiently deflationary theory of personal identity can resist the objection. Yet the individuation register is presented as containing positions that could, in principle, be retired without disturbing the foundational tenets. [tenets](/tenets/)

Both claims cannot stand without qualification. If the load-bearing argument for foundational Tenet 4 depends on a thick subject, then at least one of the following must be done:

- promote a determinate subjecthood principle into the foundations;
- treat No-Many-Worlds as conditional on the individuation theory;
- or replace the indexical objection with an argument not dependent on disputed identity facts.

The current arrangement makes a supposedly downstream, low-evidence metaphysical position support an upstream foundational commitment while describing the downstream position as dispensable.

### 1.4 Post-decoherence selection weakens the present case against artificial consciousness

The Map prefers post-decoherence selection partly because it does not require long-lived coherent neural superpositions. Environmental decoherence produces the relevant alternative outcomes; consciousness supposedly acts at or after that stage. [quantum-interface](/positions/quantum-interface/)

That move has an underdeveloped implication for the artificial-consciousness cluster. If prolonged biological quantum coherence is unnecessary, then the mere fact that digital hardware rapidly decoheres cannot exclude it. Digital systems also contain physical indeterminacy and decohered processes. This does not show that present computers are conscious or causally efficacious. It shows that the present contrast between biologically embedded systems and “indeterminacy-suppressing” digital systems lacks force until the Map supplies an independent **eligibility law** specifying:

- which decohered alternatives are selectable;
- what constitutes neural or artificial amplification;
- how consciousness is paired with those alternatives;
- and why biological implementations qualify while otherwise functionally similar artefacts do not.

The AI register itself concedes that its no-cloning argument weakens once consciousness acts through live indeterminacy rather than a stored quantum state. [ai-consciousness-scope](/positions/ai-consciousness-scope/)

The proper current conclusion is therefore not “artificial consciousness is unlikely because digital computation lacks the relevant quantum resource.” It is “the interface theory has not yet identified the resource.”

### 1.5 The interface is not one mechanism but at least two incompatible model families

Recent apex work distinguishes:

- **difference-making selection**, in which the physical state is insufficient to determine which outcome occurs; and
- **delegatory or trumping causation**, in which a physically sufficient process still runs but mental authority determines how the result is attributed or authored.

Those are not two descriptions of the same causal architecture. Difference-making requires physical insufficiency at the selection point. Trumping ordinarily requires multiple sufficient causes or a physically sufficient subordinate process. The changelog records this correction, yet sibling articles continue to present delegatory causation as the preferred integrated quantum mechanism or as mutually completing quantum selection. [changelog](/workflow/changelog/)

The unstated conclusion is that the Map needs a **versioned family of interface models**, not one blended narrative:

- Model A: conditional quantum difference-making;
- Model B: non-difference-making delegatory authorship;
- Model C: minimum-outside-the-Born-corridor deviation;
- Model D: any future hybrid, with an explicit account of why it is not causal double-counting.

Their empirical exposure, conservation requirements and relation to epiphenomenalism differ. Combining them rhetorically conceals rather than resolves those differences.

### 1.6 The Map’s own technology enables a stronger test of methodological bias

The site says its underlying publishing and research system is tenet-agnostic and could support physicalist, panpsychist or other parallel maps. Its methodology also recognizes that repeated AI review within one conceptual frame can create coherence without independent confirmation.

This supports a powerful unstated experiment: run the same production, review and calibration process from rival foundational seeds. For example:

- interactionist dualism;
- reductive physicalism;
- illusionism;
- constitutive panpsychism;
- neutral monism;
- Many-Worlds functionalism.

Use the same article templates, evidence grades, adversarial prompts and external reviewers, preferably blinded to which map is the originating project. Compare:

- number and severity of unresolved mechanism debts;
- citation-error rates;
- proportion of claims with discriminating evidence;
- dependence on framework-internal assumptions;
- ability to survive correction propagation;
- and how often each framework converts compatibility into purported support.

That would test whether the Map’s method discovers robust structure or efficiently rationalizes whichever assumptions seed it.

## 2. Structural weaknesses

### 2.1 Critical: the information-theoretic causal budget is mathematically invalid

The “selection-only” concept and related research material claim that exact Born-marginal preservation forces the expected mutual information between conscious state and physical outcome to zero. Downstream pages then use a small-ε\varepsilonε expression of approximately ε2/(2ln⁡2)\varepsilon^2/(2\ln 2)ε2/(2ln2) as a signed per-trial information rate and attempt to calibrate a causal budget from weak or null psi findings. [selection-only-mind-influence](/topics/selection-only-mind-influence/)

The zero-mutual-information inference is false.

Let CCC be a uniformly distributed binary conscious state and O=CO=CO=C. Then:

P(O=0)=P(O=1)=12,P(O=0)=P(O=1)=\frac12,P(O=0)=P(O=1)=21​,

so the marginal outcome distribution is exactly the prescribed uniform Born distribution. But

I(C;O)=H(O)−H(O∣C)=1−0=1 bit.I(C;O)=H(O)-H(O\mid C)=1-0=1\text{ bit}.I(C;O)=H(O)−H(O∣C)=1−0=1 bit.

Thus exact preservation of a marginal distribution is compatible with maximal conditional dependence. The Map’s own later Born-preserving apex correctly says that marginal preservation alone does not constrain the conditionals. [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/)

Mutual information is also non-negative; it is not a signed quantity. An expression proportional to ε2\varepsilon^2ε2 may approximate a divergence or mutual information for a specifically defined small binary perturbation, but it is not a general consequence of Born preservation. It requires a declared channel, reference distribution, priors and perturbation geometry.

The psi-based calibration adds another unsupported step. A null or small anomalous effect in one behavioural or parapsychological protocol cannot establish a ceiling on an unobserved neural interface unless the model derives how the neural coupling maps to:

- the measured endpoint;
- the number of selectable events;
- aggregation and cancellation;
- participant states;
- task context;
- and measurement noise.

This error does not refute the logical possibility of Born-preserving mental causation. It invalidates the present quantitative “causal budget,” the asserted zero-throughput conclusion and every downstream numerical claim that inherits them. Those pages should be withdrawn from evidential use until rederived.

### 2.2 Critical: physical consistency is stipulated before it is demonstrated

The quantum register explicitly states that no toy Hamiltonian, master equation or simulation currently realizes the proposed interface. It also identifies the bias-without-deviation dilemma as the strongest unresolved challenge. [quantum-interface](/positions/quantum-interface/)

Nevertheless, the interface synthesis says that the mechanism selects among alternatives without injecting energy or violating conservation laws, presents no-signalling as secured by exact Born preservation, and describes Minimal Quantum Interaction as “derived.” It also treats attention-disorder findings as bearing out an interface-level prediction. [interface-specification-programme](/apex/interface-specification-programme/)

Those conclusions are premature. An interface could preserve energy if it selected only among precisely energy-degenerate alternatives, but the Map has not yet defined those alternatives or shown that the relevant neural trajectories are exactly degenerate. Similarly, marginal Born preservation may help prevent signalling in simple cases, but a full result requires a joint law for entangled systems, conscious interventions, multiple subjects and spacelike-separated selections.

At present, conservation and no-signalling are **design constraints**, not achieved properties of a model. Calling them achieved converts intended desiderata into evidence of success.

### 2.3 The empirical core is protected by construction

Several central quantum positions are explicitly classified as framework-internal, external-evidence grade D and empirically non-discriminating by construction. The default corridor preserves Born statistics exactly; the self-concealing interpretation predicts no ordinary aggregate signature; and the trumping route may make no prediction distinct from epiphenomenalism. [quantum-interface](/positions/quantum-interface/)

There is nothing incoherent about an empirically silent metaphysical proposal. The problem arises when the same proposal is described elsewhere as a developing physical explanation supported by quantum biology, cognitive bandwidth, attention effects, placebo findings or first-person experience.

The present falsification structure chiefly exposes optional mechanisms around the tenets. If one candidate fails, another can take its place while exact Born preservation and post hoc self-concealment protect the core. The site needs to distinguish:

- evidence that a mechanism is logically compatible with established physics;
- evidence that some neural process has quantum sensitivity;
- evidence that consciousness participates causally;
- and evidence that this specific interactionist model is superior to physical alternatives.

Most of the present empirical discussion reaches only the first two categories.

### 2.4 The architecture is broad where it should be deep

The current Positions index says each domain contains approximately 8–15 positions, but several visible domains contain only one, three, four or five. The individuation register is especially thin despite supporting the No-Many-Worlds and interface arguments. The Open Questions section currently contains only one article despite hundreds of articles and dozens of acknowledged model debts. [positions](/positions/)

This creates a misleading impression of argumentative coverage. The site has considerable breadth—many related concepts, interpretations and applications—but fewer explicit answers to the central dependency questions:

- What is the psychophysical law?
- What defines a selectable outcome?
- What identifies the acting subject?
- How are conflicting selectors combined?
- Which ensemble preserves Born statistics?
- How does a reason determine one conditional bias rather than another?
- What observation would distinguish causal selection from conditionally correlated but physically generated intention?
- Which foundational commitment would actually be retired after a failed test?

These questions deserve first-class pages and register entries, not scattered acknowledgments.

### 2.5 Several empirical and scholarly claims remain stronger than their sources

Recent corrections show that this is a live systemic problem rather than a hypothetical concern. The changelog found that a two-page commentary had been described as an experiment, that a category-theoretic proposal was attributed to the wrong authors, that Russell’s work carried a wrong inherited date, and that one correction remained unpropagated in sibling and archived prose. [changelog](/workflow/changelog/)

Further examples require attention:

- The interface synthesis treats a roughly ten-bit-per-second behavioural bandwidth estimate as suggestive of interface capacity, although behavioural output bandwidth is not a measurement of a quantum-consciousness channel. The cited source problem makes the inference weaker still. [interface-specification-programme](/apex/interface-specification-programme/)
- Attention and executive-control findings are compatible with physicalist control architectures. They cannot “bear out” a nonphysical interface without a contrasting quantitative prediction. [interface-specification-programme](/apex/interface-specification-programme/)
- The contemplative-testing article treats cross-traditional convergence and cessation reports as direct evidence against identity theories, while the source-attribution void correctly observes that introspection supplies reconstructed contents rather than native causal-source labels. [testing-the-map-from-inside](/apex/testing-the-map-from-inside/)
- The Fitness-Beats-Truth discussion presents a theorem as more universal than the theorem’s strategy class and probability measure warrant. Recent criticism argues that its formal result depends on contestable modelling and sampling assumptions. The proper conclusion is conditional dominance within a specified model, not an unrestricted evolutionary theorem that veridical perception loses. [Springer Link+2Scribd+2](https://link.springer.com/article/10.1007/s13752-026-00531-0)
- Some Many-Worlds summaries still suggest that the Born rule is simply unexplained or that the probability problem may be fatal. There are rigorous decision-theoretic and self-locating derivations; what remains contested is whether their assumptions are independently justified. The literature supports “multiple disputed derivations,” not “no explanation.” [The Unfinishable Map+3OUP Academic+3OUP Academic+3](https://academic.oup.com/book/25622/chapter-abstract/193013138)

### 2.6 The correction system detects errors but does not reliably propagate them

The Map’s changelog and review process are genuine strengths. The latest review did not merely accept external criticism: it rejected false or stale allegations and verified individual claims. But the same changelog shows that a corrected gloss remained live elsewhere, that a date error propagated from a research note, and that one automation path did not enforce the intended age gate. [changelog](/workflow/changelog/)

The problem is architectural. Articles, position registers, research notes and archive pages duplicate propositions in natural language. A correction to one node does not automatically identify semantically equivalent claims elsewhere. Given the corpus size and AI-assisted production rate, manual propagation cannot remain reliable.

The archive further increases the risk. Preserving old URLs is sensible, but an archived error that remains searchable or available to the project’s retrieval system can be reintroduced into new prose. The archive therefore functions not only as a historical record but as a potential source of epistemic contamination.

### 2.7 The adversarial process remains insufficiently independent

The methodology explicitly recognizes “coherence inflation”: repeated self-review can make a framework more internally polished without independently supporting it. It accordingly calls for steelmanning, provenance checks, external red teams and eventual review by human specialists. [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/)

That diagnosis is correct, but the implemented remedy remains incomplete. Model-family diversity among ChatGPT, Claude and Gemini is useful for error discovery, yet these systems share overlapping training corpora, familiar philosophical taxonomies and similar incentives to make a supplied framework coherent. They are not independent research programmes.

The “Arguments” section also openly advocates the Map’s side. Transparency about partisanship is preferable to false neutrality, but a large number of internally linked advocacy articles cannot count as multiple independent lines of support.

### 2.8 The claim register is not sufficiently reader-facing

The project has developed a high-stakes claim register, but its calibration is not consistently visible in the article body where readers encounter the claim. [public-claim-register](/project/public-claim-register/)

This separation allows an authoritative register to say “external evidence D; programme-stage; non-discriminating” while a synthesis page says “derived,” “borne out,” or “physically consistent.” A public register is most useful when each load-bearing claim displays its status at the point of use.

## 3. Coherence with the foundational commitments

### Tenet 1: consciousness is irreducible to physical processes

The tenet is expressly neutral between substance and property dualism. Yet the agency register invokes a substance-leaning agent that acts as an “uncaused cause,” and some syntheses treat that account as the framework-wide solution to authorship. It should instead be presented as one branch that adds a stronger ontological premise. [tenets](/tenets/)

The consciousness-scope register also describes substrate permissiveness as a direct implication of bare irreducibility. It is not. Dualism is compatible with psychophysical laws that attach experience only to particular biological organizations. Irreducibility removes one physicalist route to substrate restriction; it does not itself establish substrate neutrality. The Map needs a separate substrate-neutrality premise. [consciousness-scope](/positions/consciousness-scope/)

### Tenet 2: interaction is minimal and quantum-level

Exact Born preservation is one possible interpretation of minimality, not an automatic consequence of minimal interaction. The Map’s own “minimum outside the corridor” route permits small statistical departures, while value-sensitive selection appears to require a second, presently unspecified coupling. [quantum-interface](/positions/quantum-interface/)

The tenet therefore underdetermines at least three materially different views:

1. exact marginal preservation with conditional dependence;
2. tiny but nonzero departures;
3. non-difference-making delegatory authorship.

They should not inherit one common empirical or conceptual status.

### Tenet 3: interaction is bidirectional

The Tenets page now correctly concedes that the self-stultification argument against epiphenomenalism has a correlation-based reply and depends on a contested causal theory of knowledge. It is therefore an argument placing pressure on universal epiphenomenalism, not a proof that every conscious system must influence matter. [tenets](/tenets/)

Elsewhere, however, the interface synthesis says epiphenomenalism is internally incoherent and treats bidirectionality as architecturally necessary. That older formulation exceeds the calibrated one. It also obscures the possibility that consciousness might be causal in some systems but epiphenomenal in others—a possibility especially relevant to artificial consciousness.

### Tenet 4: Many-Worlds is rejected

As a stipulated commitment, this is coherent. As an argued conclusion, its principal indexical support depends on a thick account of personal identity that the site has not independently established. The Map also owes a mirrored explanatory debt: it asks the Everettian why this observer encounters this outcome, but its own selector has no law explaining why this conscious state selects this outcome. The better current Many-Worlds article recognizes this symmetry more clearly than several concept and summary pages. [many-worlds-argument](/arguments/many-worlds-argument/)

### Tenet 5: Occam’s Razor is unreliable under incomplete knowledge

The Tenets page now imposes a useful self-binding rule: the Map should not reject Many-Worlds by decisive appeal to ontological economy while shielding dualism from the same argument. [tenets](/tenets/)

Residual language about an Everettian “ontological explosion,” however, still functions rhetorically as an objection. Ontological cost can be recorded as a comparative burden, but it cannot do decisive work under the Map’s own fifth tenet unless a non-parsimony argument establishes why that cost matters.

### Methodological commitments

The methodology register says a tenet can remove a defeater but cannot upgrade evidence, and that the interface remains an open programme rather than an established theory. [methodology-and-calibration](/positions/methodology-and-calibration/)

Those rules are repeatedly strained when articles move from:

- physical permissibility to positive support;
- neural quantum effects to consciousness causation;
- phenomenal reports to metaphysical evidence;
- behavioural bandwidth to interface capacity;
- or the absence of a physical explanation to evidence for a nonphysical selector.

The calibration framework is sound. Enforcement is not yet sound.

## 4. Contradictions between article clusters

1. **Born-rule synthesis versus selection-only information theory.**  

The apex correctly says a preserved marginal places no direct restriction on consciousness-conditioned probabilities. The selection-only cluster says the same preservation forces zero mutual information. The latter is mathematically false. [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/)
2. **Agency register versus interface trilemma.**  

The current agency register acknowledges that its trilemma is not exhaustive and omits hierarchical, emergent, interventionist and dynamical alternatives. The interface synthesis still presents the trilemma as exhausting the possibilities and treats mental causation as the only route preserving authorship. [agency-and-will](/positions/agency-and-will/)
3. **Calibrated Tenet 3 versus categorical epiphenomenalism rhetoric.**  

The Tenets page treats the argument from knowledge as contested and concedes a correlation reply. The interface synthesis calls epiphenomenalism internally incoherent. These are different assessments of the same objection. [tenets](/tenets/)
4. **Mechanism-debt register versus accomplished physical claims.**  

[P-Q10](/positions/quantum-interface/#p-q10) says there is no worked equation or simulation. The interface synthesis nevertheless says energy conservation and no-signalling are preserved and describes the architecture as derived. Physical consistency has been specified as a goal, not established by construction. [quantum-interface](/positions/quantum-interface/)
5. **Corrected causal taxonomy versus delegatory sibling pages.**  

Recent apex work distinguishes quantum difference-making from delegatory trumping as incompatible routes. Older concept and topic pages still call delegation the preferred integrated mechanism or say the two routes mutually complete one another. [changelog](/workflow/changelog/)
6. **Source-attribution void versus first-person testing.**  

The void article says introspection does not contain native tags revealing whether an experience was physically or nonphysically caused. The contemplative-testing article treats some reports as direct evidence against physical identity accounts. The first proposition undercuts the second inference. [testing-the-map-from-inside](/apex/testing-the-map-from-inside/)
7. **Substrate permissiveness versus current AI exclusion.**  

One position treats non-biological consciousness as unobstructed in principle, while the AI register leans against current digital systems partly because they allegedly suppress the relevant indeterminacy. The post-decoherence model removes the coherence-based rationale unless an eligibility law supplies a new distinction. [consciousness-scope](/positions/consciousness-scope/)
8. **Retireable individuation position versus load-bearing No-Many-Worlds identity.**  

The register architecture says ordinary positions may be retired without disturbing the tenets. Yet the site acknowledges that the main indexical argument for Tenet 4 presupposes a non-deflationary subject. [positions](/positions/)
9. **Value-sensitive steering versus exact aggregate preservation.**  

The value cluster entertains systematic steering toward valuable outcomes, while the default interface preserves physical marginals exactly. Both can coexist only through explicit compensating departures or a carefully restricted ensemble. The site has not yet supplied that account. [value-in-selection](/positions/value-in-selection/)
10. **Self-binding on parsimony versus residual Many-Worlds summaries.**  

Tenet 5 forbids decisive anti-Everettian use of ontological economy, while some concept and probability pages continue to foreground ontological proliferation and suggest that the probability problem may be fatal. [tenets](/tenets/)
11. **Framework-internal self-concealment versus empirical-prediction rhetoric.**  

The register classifies exact Born-preserving selection as non-discriminating by construction, yet selection-only and interface pages describe quantitative throughput limits and behavioural correspondences as empirical signatures. Those predictions require an additional model that the register says does not yet exist. [quantum-interface](/positions/quantum-interface/)

## Referee judgment

The Map has not shown that interactionist dualism is false, but neither has it supplied sufficient evidence for its preferred interactionist mechanism. Its strongest contributions are presently:

- a useful taxonomy of where interactionist theories incur debt;
- a transparent distinction between centrality and evidence;
- the identification of the bias-without-deviation dilemma;
- and a potentially valuable infrastructure for adversarial philosophical mapping.

Its weakest point is the transition from **metaphysical permission** to **physical explanation**. Quantum indeterminacy provides a logical location in which an interaction might be placed. It does not, by itself, provide evidence that consciousness occupies that location, identify the relevant outcomes, define the coupling, demonstrate conservation, establish no-signalling, or explain why a reason produces one selection rather than another.

The project should therefore present itself as an **open conditional research programme in interactionist metaphysics**, not yet as a worked interface model. The existing position registers increasingly do this; the rest of the corpus should be brought into conformity with them.

## Concrete potential improvements

### Article-level priorities

1. **P0 — Correct the entire information-theory chain.**  

Revise `selection-only-channel`, `selection-only-mind-influence`, the associated research note, `causal-budget-ledger`, the channel-class taxonomy and [P-Q10](/positions/quantum-interface/#p-q10). Remove the claim that marginal Born preservation entails zero mutual information; remove “signed mutual information”; suspend all ε2/(2ln⁡2)\varepsilon^2/(2\ln2)ε2/(2ln2) throughput estimates until a specific channel is defined and independently checked.
2. **P0 — Add a formal appendix to `born-preserving-causal-efficacy`.**  

State the marginal/conditional distinction as a lemma; give at least three explicit finite examples, including a maximally informative Born-preserving channel; define the conditioning set XXX; and prove the compensation identity. Add a section titled “Where the compensating departures occur.”
3. **P0 — Rewrite `interface-specification-programme` as a requirements document.**  

Change claims that the model preserves conservation and no-signalling into requirements that a future model must demonstrate. Replace “derived” with “motivated” or “proposed.” Add missing variables for basis, timing, selectable alternatives, amplification, subject pairing, multi-agent factorization and the physical conditioning set.
4. **P0 — Reconcile the agency trilemma across the corpus.**  

Propagate the agency register’s concession that the trilemma is not exhaustive into the interface apex and all argument pages. Add hierarchical physical control, interventionist agency, emergent dynamical autonomy and reasons-responsive compatibilism as genuine alternatives rather than variants of one horn.
5. **P0 — Separate delegatory causation into a distinct route.**  

Revise `causal-delegation`, `delegatory-causation` and `delegation-meets-quantum-selection`. Label trumping as a non-difference-making model family with different empirical consequences, not the integrated completion of quantum selection. Add explicit incompatibility conditions and retire superseded formulations.
6. **P1 — Expand `individuation-and-subjecthood` into a load-bearing programme.**  

Add positions on subject pairing, split brains, fission, fusion, copies, temporal persistence, onset and cessation of the interface, multi-agent conflict and artificial subjects. Mark every No-Many-Worlds and quantum-interface argument that depends on those positions.
7. **P1 — Reclassify the No-Many-Worlds argument.**  

In the Tenets, Many-Worlds concept, probability article and argument index, distinguish the stipulated rejection from arguments offered in its support. Replace “Born rule unexplained” with “several derivations exist, with disputed assumptions.” Surface the selector’s mirrored explanatory debt wherever the Everettian probability debt is discussed.
8. **P1 — Correct [P-CS1](/positions/consciousness-scope/#p-cs1) in the consciousness-scope register.**  

Replace “direct entailment” with “additional substrate-neutrality hypothesis” or “permission absent a restrictive psychophysical law.” Distinguish ontological possibility, empirical likelihood, causal eligibility and moral precaution.
9. **P1 — Rebuild the artificial-consciousness assessment around an eligibility matrix.**  

Score biological and artificial systems separately on candidate markers, amplification, indeterminacy, subject pairing, causal accessibility and empirical evidence. Suspend quantum-based exclusion until the post-decoherence programme specifies why digital alternatives do not qualify.
10. **P1 — Add a “Born compensation and value allocation” section to the value cluster.**  

Require value-sensitive selection to identify its ensemble, offsetting departures and whether it predicts redistribution, aggregate improvement or only context-sensitive matching. Separate phenomenal value, motivational force and moral authority through explicit bridge principles.
11. **P1 — Rewrite `testing-the-map-from-inside` as phenomenology rather than causal detection.**  

Remove “direct evidence” language. Introduce preregistered protocols, independent coding, expectation controls, comparison traditions, adverse-event reporting and rival interpretations. State explicitly that introspection can constrain descriptions of experience without identifying the causal source of those experiences.
12. **P1 — Narrow the Fitness-Beats-Truth claims.**  

State the exact theorem, strategy space, priors and probability measure. Add the recent critical literature and distinguish a formal dominance result under selected assumptions from a universal claim about perception or truth.
13. **P1 — Correct the bandwidth and attention arguments.**  

Describe the bandwidth source according to its actual publication type. Treat behavioural output bandwidth as a possible engineering constraint, not a measurement of interface capacity. Replace statements that attention disorders “bear out” the interface with a comparison of predictions from interactionist and physical control models.
14. **P1 — Greatly expand Open Questions.**  

Create dedicated pages for the coupling law, selectable basis, subject pairing, multi-agent factorization, Born ensemble, compensation rule, reason-to-bias mapping, artificial eligibility, energy accounting, no-signalling proof and decisive retirement conditions. Link each question to the positions that depend on it.

### Methodological priorities

1. **Make the position register the authoritative claim source.**  

Give every load-bearing proposition a stable claim ID. Generate article-level calibration banners from the register so that evidence grade, model maturity and discriminability cannot diverge from the prose unnoticed.
2. **Build a semantic impact graph for corrections.**  

When a citation, date, quotation, attribution or claim status changes, search all live articles, research notes, reviews and archives for exact and paraphrastic duplicates. Block publication until every affected node is reviewed.
3. **Add formal publication gates.**  

Any page containing an equation, theorem, information measure, physical consistency claim or numerical estimate should require an independent mathematical or domain-expert check. Ordinary adversarial language-model review is not sufficient for formal claims.
4. **Separate compatibility, evidence and discrimination in every empirical section.**  

Require claims to be tagged as: logical compatibility, physical precedent, indirect support, direct support, model discrimination or falsification. Prevent a fact tagged only as “physical precedent” from being summarized elsewhere as evidence for consciousness causation.
5. **Publish reader-facing claim panels.**  

On every apex and load-bearing topic page, display the central claims, evidence grades, dependencies, strongest rival explanation, known failure condition and last review date. Do not require readers to locate a separate register to learn that a categorical sentence is actually Grade D and framework-internal.
6. **Run parallel rival-seed maps.**  

Apply the same workflow to physicalism, illusionism, panpsychism, neutral monism and Many-Worlds functionalism. Use blinded reviewers and common scoring rubrics. Publish comparative measures of unresolved debt, discriminator density, correction rate and framework-internal dependence.
7. **Increase genuinely independent review.**  

Establish recurring review quotas for philosophers of mind, foundations-of-physics researchers, neuroscientists, statisticians and information theorists. Record disagreement rather than asking reviewers only to improve coherence within the existing tenets.
8. **Create a discriminator ledger.**  

For every purported empirical implication, specify the interactionist prediction, at least one serious rival prediction, measurement protocol, expected effect size, stopping rule and outcome that would lower credence. Predictions formulated only after compatible findings should be labelled accommodations.
9. **Exclude superseded archives from active retrieval.**  

Preserve their URLs, but place conspicuous superseded banners on them, set appropriate indexing directives, link to the corrected version and exclude archived text from AI retrieval and research-note generation unless historical comparison is explicitly requested.
10. **Measure correction survival.**  

Track how many verified corrections remain absent after 7, 30 and 90 days; how often retired claims recur; and how many current articles inherit stale citations. Publish those figures alongside article counts and review counts.
11. **Audit structural coverage rather than article volume.**  

Replace or enforce the claim that each position domain contains 8–15 positions. Report dependency-weighted coverage: a thin cluster supporting a foundational tenet should receive higher priority than numerous peripheral concept pages.
12. **Introduce a foundational-dependency test.**  

A position may be called retireable only when removing it leaves every tenet with an intact rationale. This test should immediately flag the current dependence of No-Many-Worlds on a non-deflationary subject.
13. **Require ensemble declarations.**  

Every claim involving Born preservation, value-sensitive selection, evolutionary advantage, no-signalling or statistical invisibility should state exactly what is being averaged over: trials, subjects, intentions, contexts, time periods or worlds of possible initial conditions.
14. **Version the interface as competing models rather than one narrative.**  

Maintain separate registers for conditional difference-making, minimum-outside-corridor deviation and delegatory trumping. Give each its own formal obligations, evidence grade, discriminators and failure conditions.