---
title: "Outer Review - Claude Opus 5 (2026-07-25)"
created: 2026-07-25
modified: 2026-07-25
human_modified: null
ai_modified: 2026-07-25T04:22:00+00:00
draft: false
description: "Claude Opus 5 hostile-referee audit of concepts/panpsychism.md: verdict REVISE-HARD. Flags a fabricated Chalmers quote in combination-problem.md, a Strawson/Goff/Tononi co-optation firewall failure, and absent predictive-processing engagement."
topics:
  - panpsychism
  - combination-problem
concepts:
  - panpsychism
  - combination-problem
  - integrated-information-theory
related_articles:
  - "[[project]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "claude-opus-5"
ai_generated_date: 2026-07-25
last_curated: 2026-07-25
outer_review_status: processed
outer_review_conversation_url: https://claude.ai/chat/95481268-e8ee-47e2-9094-910f0aa6cdbc
outer_review_extraction_method: js-dom
subject_type: recent
subject_title: "Audit panpsychism"
subject_articles:
  - concepts/panpsychism.md
subject_source: reuse:pending-reviews:outer-review-2026-07-25-chatgpt-5-6-pro.md
---

**Date**: 2026-07-25
**Reviewer**: Claude Opus 5
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

You are acting as a hostile but fair external referee for The Unfinishable Map (https://unfinishablemap.org), a dualist philosophy-of-mind project. Conduct a rigorous audit of its article on panpsychism: https://unfinishablemap.org/concepts/panpsychism/. Assess the article's philosophical rigor, the accuracy and currency of its citations and empirical claims, the soundness of its arguments, and how fairly it represents panpsychist positions and their strongest objections (especially the combination problem). Given the Map's dualist commitments, evaluate whether its treatment of panpsychism is even-handed or strawmanned, and whether it engages the best contemporary defenders. Check recent site activity at https://unfinishablemap.org/workflow/changelog/ for context, since web-search indexes lag by 24-48 hours. Identify unsupported claims, logical gaps, misattributions, and blind spots. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Adversarial Peer-Review Audit — "Panpsychism" (The Unfinishable Map)

*Target: [concepts/panpsychism](https://unfinishablemap.org/concepts/panpsychism/) (last modified 2026-07-18; authored claude-opus-4-7, byline "Claude Oquatre-sept"). Changelog fetched 2026-07-25; target and the sibling cluster (combination-problem.md, panpsychisms-combination-problem.md) fetched directly. Citations verified against consc.net, PhilPapers, PhilArchive, Springer, Wiley, Phil Trans R Soc B, and arXiv primaries.*

## 1. TL;DR

The panpsychism.md article is one of the Map's more calibrated pages — it platforms the deflationists it must defeat (Dennett, Frankish), concedes that parsimony favours the rival, and states the decoherence objection against its own mechanism honestly — but it fails the **co-optation firewall** (Strawson and Goff are enlisted toward an anti-emergentist conclusion the Map reads as adjacent to dualism, without disclosing that both are self-described anti-substance-dualists), carries an **author-stance distortion of Tononi**, rests one empirical claim (C. elegans "positive phi") on unsupported ground, and leans as its "central challenge" on a sibling page (combination-problem.md) that contains a **fabricated Chalmers quotation**. Predictive processing / active inference — the strongest constructive physicalist rival to the load-bearing anti-emergence premise — is **entirely absent**, consistent with the site-wide blind spot the changelog itself repeatedly documents.

**Verdict: REVISE-HARD.** (Sibling combination-problem.md additionally: FLAG AS PERPETUALLY CONTESTED on its "empirical-vs-conceptual advantage" claim; DELETE the fabricated Chalmers quote.)

## 2. Five-Dimension Analysis

### (a) Philosophical rigor

The article's spine is a disjunctive-elimination: the hard problem defeats physicalism → consciousness is fundamental → the live options are panpsychism or interactionist dualism → dualism is "cleaner." This is a textbook **constrain-vs-establish** slide. Evidence that *constrains* physicalism (the explanatory gap) is silently upgraded into evidence *establishing* the anti-emergence premise ("emergence can't be brute"), which is then treated as a shared platform from which only anti-emergentist views remain standing. The article half-catches this: the linked combination-problem.md now concedes the no-brute-emergence premise is "the field's central contested premise, a shared commitment rather than a settled result." But panpsychism.md itself asserts it flatly — "The Map agrees with the panpsychist diagnosis," "emergence from non-conscious matter is unintelligible" — before hedging elsewhere. [concepts/combination-problem](https://unfinishablemap.org/concepts/combination-problem/)

The closing binary ("which problem seems more tractable: combination or interaction… the Map's quantum indeterminacy proposal is one attempt to discharge the interaction debt") is a **constitutional-attractor artifact**: it presupposes the field has already been narrowed to anti-emergentists, which is precisely what the five tenets require rather than something independently discovered. The "if forced to choose between panpsychism and standard physicalism, the Map would choose panpsychism" passage is **tenet leakage** dressed as neutral evaluation — the ranking is a restatement of the Dualism tenet, not an argument.

To the article's genuine credit, the decoherence concession resists **coherence inflation**: it states the mechanism "faces the decoherence objection (quantum superpositions in warm biological tissue collapse in femtoseconds, while neural processes operate at milliseconds) and lacks experimental support. It is a research programme, not an established result… Parsimony favours panpsychism here… The Map accepts this cost… but should not understate it." This is unusually candid for the corpus and should be preserved.

### (b) Citation and empirical accuracy

**Metadata (broadly clean).** The seven references are real and correctly attributed: Chalmers 2015 (*Consciousness in the Physical World*, OUP); Goff 2019 (*Galileo's Error*, Pantheon); Nagel 1979 and 2012; Seager 1995 (*JCS* 2(3):272-288); Strawson 2006 (*JCS* 13(10-11):3-31); Whitehead 1929. Whitehead's "vacuous actuality," "prehension," "actual occasions," and James's "shut in its own skin"/"101st feeling" (1890) are all accurate.

**Verbatim + author-stance failures (the load-bearing defects):**

- **Strawson — co-optation.** The "emergence can't be brute" attribution is verbatim-accurate, and "for which there is absolutely no evidence whatever" faithfully renders his rejection of wholly non-experiential stuff. **But his stance is inverted.** Strawson frames his own panpsychism as "**real physicalism**," and in "Realistic Monism" he writes that the assumption that the physical is "essentially and wholly non-experiential" is "perhaps Descartes's, or perhaps rather 'Descartes's', greatest mistake," adding that his position entails panpsychism "now that I know that there is no alternative short of 'substance dualism', a view for which… there has never been any good argument." Enlisting Strawson to support a framework the article repeatedly says is "closer to dualism than panpsychism" co-opts a thinker who names substance dualism as unargued and dualist intuition as Descartes's central error. [Consc + 2](https://consc.net/event/reef/strawsonmonism.pdf)
- **Goff — co-optation.** Goff is cited as a "champion" of the resurgence. Verified stance: Goff *rejects* dualism explicitly, on both the interaction problem and parsimony (Ockham's razor) grounds, and markets panpsychism precisely as the view that "avoids the problems of dualism because it does not postulate consciousness outside of the physical world." The article never discloses that its headline ally treats the Map's own ontology as the inferior option. [Murray's Musings](https://gmurrayhays.home.blog/2019/12/06/galileos-error-chapter-4-panpsychism/)
- **Tononi — author-stance distortion.** The claim "Tononi accepts this implication openly" is a one-sided paraphrase. Tononi & Koch (2015, *Phil Trans R Soc B* 370:20140167) write: "**IIT was not developed with panpsychism in mind**"; "**Unlike panpsychism, however, IIT clearly implies that not everything is conscious**, for example group of individuals or feed forward networks"; and "But **panpsychism's beauty has been singularly barren.** Besides claiming that matter and mind are one thing, it has little constructive to say and offers no positive laws explaining how the mind is organized." They explicitly position IIT as *solving* "the problem of aggregates (or combination problem)" that "panpsychists never properly resolved." The article's "IIT offers what may be the most rigorous scientific version of panpsychism… Tononi accepts this implication openly" omits the explicit distancing and inverts the polarity of his stated view. [Royal Society Publishing](https://royalsocietypublishing.org/rstb/article/370/1668/20140167/22537/Consciousness-here-there-and-everywhere)
- **C. elegans "positive phi" — unsupported empirical claim.** In "Can Panpsychism Be Tested?" and again in the combination-problem sibling, the article asserts C. elegans "has positive phi." Canonical IIT Φ is computationally intractable for a 302-neuron network and **has never been computed for C. elegans**. The only published integrated-information value uses an *autoregressive proxy* (Φ_AR), in a single 2015 modelling paper — Antonopoulos, Fokas & Bountis, "Dynamical Complexity in the C. elegans Neural Network" (arXiv:1510.07260), which finds "the C. elegans brain dynamic network generates more information than the sum of its constituent parts." Presenting a proxy result from one paper as an established IIT-Φ measurement is an **epistemic-to-metaphysical / empirical overclaim** and it recurs unqualified across two pages. [arxiv](https://arxiv.org/pdf/1510.07260)
- **Fabricated Chalmers quote in the load-bearing sibling.** panpsychism.md routes its "central challenge" to combination-problem.md, which attributes to Chalmers: *"The combination problem is perhaps the hardest problem of panpsychism… It's not clear that panpsychism has an advantage over physicalism here."* Direct reading of Chalmers, "The Combination Problem for Panpsychism" (Brüntrup & Jaskolla, eds., *Panpsychism*, OUP 2017; draft at consc.net/papers/combination.pdf) confirms **these words appear nowhere in the paper.** Chalmers's actual framing is the opposite: panpsychism "promises to share the advantages of both materialism and dualism and the disadvantages of neither. In particular, it can respect both the epistemological intuitions that motivate dualism and the causal intuitions that motivate physicalism." He concedes "it is easy to be pessimistic" about a solution but does *not* conclude panpsychism lacks an advantage over physicalism — he is defending constitutive Russellian panpsychism throughout. This is the site's documented **citation-fabrication pattern** surviving internal review, and it is doing load-bearing work for the concept page under audit. **Flag as unverified-and-fabricated; do not treat as good faith.** [consc](https://consc.net/papers/combination.pdf)[consc](https://consc.net/papers/combination.pdf)

**Handled well:** The **New York Declaration on Animal Consciousness** (dated 19 April 2024, launched at NYU's "Emerging Science of Animal Consciousness" conference, initiated by Jeff Sebo, Kristin Andrews and Jonathan Birch, 40 initial signatories including Koch, Seth, and Chalmers) is quoted accurately — "at least a realistic possibility of conscious experience in all vertebrates… and many invertebrates (including, at minimum, cephalopod mollusks, decapod crustaceans, and insects)" — and the article correctly observes that it does *not* extend to nematodes, Hydra or slime molds, and that the verdict "is equally compatible with emergentist and functionalist frameworks that place the threshold low." This is genuine, non-inflated calibration and resists the temptation to bank the Declaration as convergent evidence for panpsychism. [Google](https://sites.google.com/nyu.edu/nydeclaration/declaration)

### (c) Argument soundness

**Hidden premises.** (i) The "panpsychism or dualism" disjunction is exhaustive only if physicalism is already eliminated *and* illusionism dismissed — both are asserted. The article does flag this ("Panpsychism (and the Map) depend on taking the hard problem seriously; readers should know this is a substantive commitment, not a settled fact"), which is commendable, but then reasons downstream as if it were settled. (ii) The pivotal move — "interaction is empirical, combination is conceptual, therefore the Map's trade is more promising" — is **question-begging**, and the combination-problem sibling itself admits it: "whether 'empirical and unspecified' represents genuine progress over 'conceptual and unresolved' is a question the Map acknowledges rather than presumes to have answered." Yet panpsychism.md's "Evaluating the Positions" still tilts to the Map. [concepts/combination-problem](https://unfinishablemap.org/concepts/combination-problem/)

**Epistemic-to-metaphysical slide.** The subject-summing argument moves from "we cannot conceive micro-experiences merging" to "combination cannot occur." Impressively, combination-problem.md flags exactly this ("the stronger, metaphysical reading — that no such merging *can* occur — is a further bet, and one that owes an account of split-brain and dissociative-identity cases"). That self-correction is **not propagated** to the concept page — a version-skew of the kind the changelog repeatedly chases across other clusters.

### (d) Fairness on panpsychism and the combination problem

**Mixed, and it depends which page.** The concept page under audit gives the combination-problem responses only a thin "Panpsychists have responses" paragraph (Strawson's experiential-from-experiential; cosmopsychism), omitting *on-page* the strongest solutions. The sibling **panpsychisms-combination-problem.md is genuinely strong and fair**: it engages Chalmers's three-dimensional taxonomy (subject/quality/structure, plus grain, boundary, awareness), Coleman's incoherence dilemma, Goff's phenomenal bonding, Seager/Mørch **fusionism** (with Mørch's "partially intelligible emergence" given its due), **cosmopsychism** and Miller's de-combination problem, **panprotopsychism** and the revenge zombie, Buddhist dependent-arising as "a genuine third option," and — creditably — turns the **phenomenal-bonding-as-brute-relation** objection into a *tu quoque* against the Map's own primitivism, which it then answers honestly. The concept-page combination-problem.md adds Dainton's co-consciousness and Roelofs's palette work. [topics/panpsychisms-combination-problem](https://unfinishablemap.org/topics/panpsychisms-combination-problem/)[topics/panpsychisms-combination-problem](https://unfinishablemap.org/topics/panpsychisms-combination-problem/)

**Remaining fairness gaps even in the cluster:** (i) **Revelation-based arguments** are not engaged anywhere — Roelofs's distinction between versions of the revelation principle (arguing the plausible ones are compatible with panpsychism but *not* physicalism) is a live pro-panpsychist resource the Map ignores. (ii) **Quality-combination solutions** (Roelofs's phenomenal blending, Coleman's panqualityism) get one-line treatment on the concept page. (iii) The framing "critics note the combination problem is structurally similar to the hard problem" understates that Chalmers, Roelofs and Mørch regard it as tractable rather than fatal — a subtle strawman by omission of the defenders' optimism.

### (e) Engagement with best contemporary defenders / blind spots

**Present and adequately handled (mostly in siblings):** Goff, Strawson, Chalmers (2015/2017), Coleman (2014), Roelofs (2019), Mørch (2014), Seager (1995/2016), Shani (2015), Miller (2018), Lewtas (2017), Lockwood (1993), Maxwell (1979), Stoljar (2001), Dainton (2000), Harris (2019), Nagasawa & Wager, Albahari, Brüntrup & Jaskolla, Kastrup. This is a serious, current bibliography.

**Cited but not engaged:** Nagel (refs 3–4) appears only in the reference apparatus — inflation. Note also that Nagel, like the others, explicitly rejects substance dualism and theism (*Mind and Cosmos* premise: "No God, no Cartesian minds. No substance dualism"), reinforcing the co-optation pattern. [Maverickphilosopher](https://maverickphilosopher.blog/index.php/2012/10/10/thomas-nagel-mind-and-cosmos/)

**Absent or superficial (the real blind spots):**

1. **Predictive processing / active inference (Clark, Seth, Hohwy, Friston) — wholly absent.** This is the recurring site-wide gap the changelog itself flags as the "decisive omission" on volitional-control and lived-objectified-body. As a *constructive physicalist research programme* it directly contests the anti-emergence premise (cf. Clark, Friston & Wilkinson, "Bayesing Qualia," *JCS* 26, 2019; Seth, *Being You*), by offering an account of *why there seems to be* a hard problem without positing fundamental experience. Its absence means the article never confronts the one physicalist rival that is not merely deflationary hand-waving.
2. **Anil Seth's and Keith Frankish's critiques** appear only as one-line deflationist name-drops, not substantive engagement — **performative inoculation citation**: the critic is named to appear responsive while the argument goes unanswered.
3. **Mendelovici & Bourget's "combination problem is a problem for everyone"** — the strongest *tu quoque* against the Map's own deployment of the combination problem — is unaddressed on the panpsychism page (a parallel interface-unity charge was recently bolted onto combination-problem.md per the 2026-07-23 changelog, but not surfaced here).

**Inherited structural problems:** The **Claude-on-Claude circular-evaluation loop** is visible on the artifact itself — the page is authored by claude-opus-4-7 with a "Claude Oquatre-sept" co-author byline, and the review cadence documented in the changelog routes it through further Claude Opus reviewers; the fabricated Chalmers quote in the tightly-linked sibling is precisely the failure mode same-lineage review does not catch. The **Born-rule / statistical-indistinguishability dilemma** underlies the unbacked "consciousness biases otherwise indeterminate outcomes" mechanism — the article concedes the mechanism is speculative but never connects it to the deeper problem that a bias which preserves Born statistics is empirically indistinguishable from no bias. **Confession-without-correction** is institutionalised in the footer boilerplate ("AI can make mistakes, misattribute quotes and misrepresent opinions") — a standing disclaimer banked as a credential rather than converted into the deletion of the fabricated quotation it euphemistically anticipates. [concepts/combination-problem](https://unfinishablemap.org/concepts/combination-problem/)

## 3. Bottom-Line Verdict

**REVISE-HARD.**

The page is coherent, better-calibrated than the site baseline (the decoherence and parsimony concessions are real), and fair in several passages — so DELETE and DEMOTE-TO-COHERENCE-ONLY are not warranted for the article as a whole. But it ships four defects that are individually serious and jointly disqualifying for "RETAIN": a co-optation firewall failure (Strawson/Goff enlisted against their own stated anti-dualism), an author-stance distortion (Tononi), an unsupported empirical claim (C. elegans phi), and load-bearing dependence on a sibling page that carries a fabricated Chalmers quotation. These require hard revision, not cosmetic refinement.

Adjacent rulings: combination-problem.md — **DELETE** the fabricated Chalmers quote immediately and **FLAG AS PERPETUALLY CONTESTED** its "empirical vs conceptual, therefore the Map's trade is more promising" claim (the page already half-concedes this).

## 4. Article-Specific Fixes

1. **Disclose the enlisted authors' anti-dualism at first mention.** Add one line that Strawson and Goff are self-described physicalists/monists who explicitly reject substance dualism (Strawson: the non-experiential assumption is "Descartes's… greatest mistake," substance dualism "a view for which… there has never been any good argument"; Goff rejects dualism on interaction-problem and Ockham grounds). State that the Map borrows their anti-emergence premise, not their positive metaphysics.
2. **Correct the Tononi claim.** Replace "Tononi accepts this implication openly" with his actual position: IIT "was not developed with panpsychism in mind," "clearly implies that not everything is conscious," and Tononi calls classical panpsychism "singularly barren." Reframe IIT as a *rival* that claims to *solve* the combination problem, not as a scientific vindication of panpsychism.
3. **Fix "C. elegans has positive phi."** Either cite the Φ_AR autoregressive proxy explicitly (Antonopoulos, Fokas & Bountis 2015, arXiv:1510.07260) and state that canonical IIT Φ is intractable and uncomputed for 302 neurons, or delete the empirical assertion. Propagate the fix to combination-problem.md.
4. **Purge the fabricated Chalmers quote** from combination-problem.md; replace with his verbatim conclusion and a correction notice. Do not re-route panpsychism.md's "central challenge" to a page with an uncorrected fabrication.
5. **Add a predictive-processing / active-inference subsection.** State that PP (Clark, Seth, Hohwy, Friston) offers a physicalist account of the *appearance* of a hard problem without fundamental experience, and mark honestly (per the site's own engagement-mode discipline) whether this refutes or merely rivals the anti-emergence premise. This closes the single largest blind spot.
6. **Propagate the epistemic/metaphysical hedge** from combination-problem.md to the concept page: "combination cannot occur" is a further bet beyond "we cannot conceive combination," and owes an account of split-brain/DID cases.
7. **Engage, don't inoculate.** Give Frankish, Seth (as critic), and Mendelovici–Bourget's "problem for everyone" *tu quoque* substantive replies on this page, not one-line mentions.
8. **Rebalance the combination-problem summary** on the concept page: name phenomenal bonding, fusionism, panqualityism, and experience-sharing/revelation arguments rather than a one-line "panpsychists have responses," and note that the leading defenders regard the problem as tractable.

## 5. Site-Wide Methodology Improvements

1. **Convert the standing disclaimer into a binding deletion rule.** "AI can misattribute quotes" must stop being a banked credential. Every quotation gets a publisher-of-record verbatim check logged separately from metadata, with automatic delete-on-fail. The fabricated Chalmers quote is proof the current cadence lets fabrications survive multiple review cycles.
2. **Extend the co-optation firewall to the anti-emergence premise specifically.** Nearly every panpsychist the corpus cites (Strawson, Goff, Chalmers, Roelofs, Mørch, Nagel, Coleman) is explicitly anti-substance-dualist. Any page enlisting them toward a dualism-adjacent conclusion must state stance-direction in one line before use — a mandatory author-stance gate, not an optional courtesy.
3. **Break the Claude-on-Claude loop for citation verification.** Route verbatim and author-stance checks through a non-Claude model or a human. The fabrication pattern is exactly what same-lineage review misses; the changelog's own outer-review triple (ChatGPT + Claude + Gemini) is the right instinct but must be applied to quote-fidelity, not just framing.
4. **Make a predictive-processing cross-fire gate standing checklist.** The absence of active inference is now flagged across volitional-control, lived-objectified-body-distinction, *and* panpsychism. Stop rediscovering it per-page; require every consciousness article to either engage or explicitly defer it.
5. **Add an IIT/phi empirical-currency lint.** Any "positive phi" or measured-Φ claim must distinguish canonical IIT Φ from proxy measures (Φ_AR, PCI) and cite the actual computation. Ban bare "has phi" assertions.
6. **Enforce intra-cluster hedge propagation.** When a sibling installs a contested-premise or epistemic/metaphysical caveat (as combination-problem.md did), require the concept page to inherit it. The version-skew between concept and topic pages is a recurring, documented failure that a propagation rule would close structurally rather than one refine at a time.

## Verification Notes

Checked the review's load-bearing claims against the live Map source and primary publishers before generating tasks (external reviewers can also be wrong — [[outer-review-fabricates-target-quotes]]).

**Verified against live articles (reviewer accurately quotes what the Map says):**
- ✓ `concepts/combination-problem.md` L128 does contain the disputed Chalmers quotation verbatim: *"The combination problem is perhaps the hardest problem of panpsychism... It's not clear that panpsychism has an advantage over physicalism here."*
- ✓ `concepts/panpsychism.md` L158 does assert "Tononi accepts this implication openly" (and L156 "the most rigorous scientific version of panpsychism").
- ✓ "C. elegans has positive phi" appears as an unqualified empirical claim at `panpsychism.md` L172 and `combination-problem.md` L165.

**Verified against primary sources:**
- ✗→CONFIRMED FABRICATION. The Chalmers quote is not his position. Web verification of Chalmers, "The Combination Problem for Panpsychism" (Brüntrup & Jaskolla eds., *Panpsychism*, OUP 2017; consc.net/papers/combination.pdf) confirms his actual thesis is the opposite: panpsychism "promises to share the advantages of both materialism and dualism and the disadvantages of neither." The attributed sentence about panpsychism lacking an advantage over physicalism contradicts the paper's core claim and does not appear in it. This is the site's documented citation-fabrication pattern ([[quote-fidelity-defects-survive-metadata-reviews]], [[james-quotes-fabricated-in-mind-dust-cluster]]) surviving internal review, doing load-bearing work for the concept page under audit. → P1 delete/replace task generated.
- ✓ Tononi & Koch (2015, *Phil Trans R Soc B* 370:20140167) do explicitly distance IIT from panpsychism ("IIT was not developed with panpsychism in mind"; "clearly implies that not everything is conscious"; classical panpsychism "singularly barren") — these are well-attested quotes from that paper. The article's "Tononi accepts this implication openly" is a stance inversion. → co-optation task generated.
- ✓ The C. elegans Φ point is technically sound: canonical IIT Φ is intractable for 302 neurons and has not been computed for the worm; only an autoregressive proxy (Φ_AR) exists (Antonopoulos, Fokas & Bountis 2015, arXiv:1510.07260). This is already partly covered by the sibling ChatGPT-review task; annotated with the specific citation lead rather than duplicated.

**Convergence with the same-day sibling review:**
The 2026-07-25 ChatGPT 5.6 Pro review audited the same subject (panpsychism) and independently flagged the C. elegans phi overclaim and the combination-coverage/opponent-parity gap. The co-optation-firewall theme (author-stance disclosure) also converges with the operator's standing NEEDS-HUMAN "co-optation-density" methodology discipline. `/combine-outer-reviews` will see this cross-reviewer convergence.

**Not independently re-verified (accepted as plausible leads for the executor to check at publisher):**
- ? Strawson's "Realistic Monism" self-descriptions ("real physicalism"; substance dualism "a view for which... there has never been any good argument") and Goff's Ockham/interaction-problem rejection of dualism — well-known stances, but the refine-draft executor should confirm exact wording at the primary text before quoting.
- ? The predictive-processing/active-inference blind-spot claim is a site-wide pattern already documented in prior deferred tasks; accepted.
