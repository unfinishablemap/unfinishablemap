---
title: "Research: The Ignorance Hypothesis"
created: 2026-10-03
modified: 2026-10-03
human_modified: null
ai_modified: 2026-10-03T10:28:38+00:00
draft: false
description: "Research notes on Stoljar's ignorance hypothesis: the verified formulation, how Chalmers and Stoljar each file it (type-F for the 2001 view, type-C for the 2006 one), the Papineau and Kind objections, the Q2 misfiling, and what Tenet 5 commits the Map to."
topics:
  - "[[hard-problem-of-consciousness]]"
  - "[[arguments-against-materialism]]"
  - "[[four-quadrant-dualism-taxonomy]]"
  - "[[epistemic-advantages-of-dualism]]"
concepts:
  - "[[type-a-type-b-and-type-c-physicalism]]"
  - "[[russellian-monism]]"
  - "[[mysterianism]]"
  - "[[physical-completeness]]"
  - "[[intrinsic-nature]]"
  - "[[zombie-master-argument]]"
  - "[[philosophical-zombies]]"
  - "[[conceivability-possibility-inference]]"
  - "[[knowledge-argument]]"
  - "[[explanatory-gap]]"
  - "[[vitalism]]"
  - "[[primitive-identities-and-strong-necessities]]"
  - "[[revelation-thesis]]"
  - "[[meta-problem-of-consciousness]]"
related_articles:
  - "[[tenets]]"
  - "[[positions/methodology-and-calibration]]"
  - "[[positions/arguments-for-dualism]]"
  - "[[type-a-type-b-and-type-c-physicalism-2026-10-02]]"
  - "[[primitive-identities-and-strong-necessities-2026-10-03]]"
  - "[[mysterianism-cognitive-closure-2026-01-14]]"
  - "[[knowledge-argument-marys-room-2026-01-14]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-03
last_curated: null
last_deep_review: null
---

# Research: The Ignorance Hypothesis

**Date**: 2026-10-03
**Origin**: harvested P2 research-topic; source review `obsidian/reviews/optimistic-2026-10-02-physicalist-typing-wing.md` (§New Article Subjects, item 2). The task notes named the output `-2026-10-02.md`, the harvest date; research notes are named by run date, hence `-2026-10-03`.
**Search queries used**: none. The session's web-search budget was exhausted before this run, so every source was reached by direct fetch: Crossref and OpenAlex (metadata, publisher abstracts, OpenAlex abstract indexes, Stoljar's works list by author id A5040625146); OUP chapter abstracts for *Ignorance and Imagination* via Crossref; Taylor & Francis chapter pages for the Kind–Stoljar debate (abstracts embedded in the page JSON); consc.net author texts (Chalmers 2003, 2013, 2018); the SEP "Physicalism" raw HTML (revision of 16 September 2026); the NDPR review page (Papineau 2007); the ANU Open Research repository (author's preprint of Stoljar's "Four Kinds of Russellian Monism"); the Cambridge Apollo repository (submitted version of McClelland 2020). PhilPapers, academic.oup.com, onlinelibrary.wiley.com and oecs.mit.edu returned Cloudflare 403s; ANU bitstreams for Stoljar's 2020 Handbook chapter, his Bloomsbury chapter and his 2019 panpsychism chapter returned 401 (restricted); the Google Books API quota was zero.
**Verification**: every quotation below was re-checked by script against the fetched text it is attributed to, after normalising whitespace, curly quotes and dash/hyphen variants. Quotations from publisher abstracts are labelled as abstracts; they are the publisher-of-record wording, not the author's body text. Quotations from author's preprints and submitted versions are labelled, and their page numbers are the preprint's own. Works whose existence and metadata were confirmed but whose content was not read are listed under §Supporting sources and §Gaps, and none of their arguments is reported here.

## Verdict (assess-first)

**A new concept page is warranted, at roughly 2,000–2,500 words of prose (total under 3,000 by `analyze_length`).** The licence to decline was considered and rejected for four reasons.

1. **It is the main undercutter of the Map's core cluster, and the Map has no account of it.** The explanatory-gap, zombie and knowledge arguments are, by [[positions/arguments-for-dualism#^p-d1|P-D1]], one premise-sharing cluster. P-D1 names the [[phenomenal-concepts-strategy]] as "the mainstream physicalist statement of exactly this shared premise". The ignorance hypothesis is a second, independent diagnosis of the same premise, and it survives the failure of every phenomenal-concept variant. It locates the fault on the physical side, where the Map's standard reply (acquaintance with consciousness) does not reach it (see §Corpus Seams). "Ignorance hypothesis" has one live hit (routing L75), and Stoljar's own vocabulary ("epistemic view", "o-physicalism", "non-standard physicalism", "object-based conception") has zero live hits. Those zeros were measured with the same command that returned three files for "epistemic physicalism", as a positive control.
2. **The filings conflict, and the conflict is partly a factual error.** The harvesting review says Chalmers files Stoljar under type-F. That holds for Stoljar's 2001 view only. Chalmers's 2003 text predates the 2006 book, and by Stoljar's own account Chalmers would classify the 2006 view as type-C ([[#Reconciling the Filings|§Reconciling the Filings]]). The Map's Q2 filing ([[four-quadrant-dualism-taxonomy]] L102) then attaches cell-level debts to Stoljar (an exclusion debt and a Tenet-3 exclusion) that do not apply to a physicalist view.
3. **Tenet 5 makes the hypothesis the Map's own problem.** The tenet's rationale asserts that "The apparent simplicity of physicalism could reflect ignorance rather than insight". Stoljar's premise is the same epistemic humility pointed the other way. The Map deploys that clause, or its equivalent, against physicalism on at least five pages and never turns it on its own arguments. An article is the place to say what the Map grants (that we are ignorant of something relevant) and what it denies (that the missing truths are non-experiential and would close the gap).
4. **The literature is substantial and current.** It runs from the 2006 book through the 2009 *PPR* symposium (Stoljar, Alter, Bennett), critical notices (Papineau 2007, Levine 2008, Gertler 2009), Stoljar's 2013 and 2020 restatements, McClelland 2020 on the meta-problem, Chalmers 2018's dismissal, and a 2023 book-length dualist–epistemicist debate (Kind and Stoljar).

**Why not fold it into an existing page.** The four natural hosts are full or off-scope. [[mysterianism]] has 65 words of headroom, and McGinn's view differs from Stoljar's on exactly the points that matter: permanence, and whether the missing property is special. [[russellian-monism]] is the species, not the genus: Stoljar treats Russellian monism "as a specific version of RM4, rather than the other way around". [[type-a-type-b-and-type-c-physicalism]] owns the taxonomy and the routing table, and should point to a host rather than become one. [[four-quadrant-dualism-taxonomy]] is over its hard gate (4,003).

**What the page must not do.** It must not restate the A/B/C taxonomy or the collapse argument (the routing page owns both; link `[[type-a-type-b-and-type-c-physicalism#Why Type-C Collapses]]`). It must not re-run the zombie or knowledge arguments. It must not say Chalmers files the ignorance hypothesis under type-F. It must not answer Stoljar with the acquaintance reply, which concerns phenomenal-side ignorance; Stoljar's ignorance is physical-side. It must not cite the "it is hard to see how" intuition as evidence against the hypothesis without noting that the hypothesis predicts that intuition. And it must not lift the Map's tier on the strength of any reply here, since each is defeater-removal or dialectical ([[positions/methodology-and-calibration#^p-m1|P-M1]]).

## Executive Summary

Daniel Stoljar's *Ignorance and Imagination* (OUP 2006) defends "the epistemic view". It is built on a hypothesis about our epistemic situation that the OUP chapter abstract states as "the ignorance hypothesis", "which says that we are ignorant of a type of non-experiential truth relevant to the nature of experience". The view has two theses. E1: if the hypothesis is true, the "logical problem of experience" is solved, because the conceivability and knowledge arguments then commit a standard error. E2: the hypothesis is true. The logical problem is an inconsistent triad: there are experiential truths; every truth is entailed by some non-experiential truth; not every truth is. The book argues E2 from general plausibility, from a Russellian version, and from historical precedent (Broad on chemistry, Descartes on language), and contrasts the view with McGinn's mysterianism. It then argues that the a posteriori and a priori entailment views (roughly Type-B and Type-A) either have "no answer to the arguments" or collapse into the epistemic view. That is a collapse argument running the opposite way to Chalmers's. Stoljar's later statements call it "non-standard physicalism" (2023) and, against Chalmers, recommend "type-C Materialism" by name (2020).

The main objections are verified in published form. Papineau (NDPR 2007) argues that non-experiential facts are third-personal while experiential facts are first-personal, so it is "hard to see" how knowing more of the former could make zombies inconceivable. He adds that a posteriori physicalists never needed zombies to be inconceivable. Chalmers's structure-and-dynamics argument (2003) answers the generic type-C version: unknown structural truths leave the gap, and unknown intrinsic truths make the view type-F. Stoljar's 2013 reply disambiguates "structure" three ways and rejects the argument on each. Chalmers (2018) answers the meta-problem version: the central problem intuitions "concern the phenomenal rather than the physical". McClelland (2020) replies that problem intuitions are hybrid, with a physical-side component that ignorance undermines. Kind (2023), defending "dualism 2.0", objects (as Stoljar's reply abstract summarises her) that ignorance "would not have the advertised effect" on the arguments, that the view leaves the hard problem undone ("you're not done"), and that it treats physicalism as a default to be defended "at all costs".

For the Map, three results. (a) Chalmers's type-F filing is correct for Stoljar 2001 and wrong if transferred to 2006. The Q2 filing is compatible in principle with both, but it misdescribes what a physicalist view owes. (b) Tenet 5 commits the Map to treating E2 as live. The real disagreement is E1 and the content of the ignorance. The Map also holds that current physics is incomplete in a way relevant to consciousness ([[physical-completeness]] L86–L90), but on its view what is missing is consciousness-involving: actuality-selection, Chalmers's route 4, type-D. Stoljar holds that the missing truths are non-experiential. (c) Against the ignorance hypothesis the Map's tier is *compatible*, not the *suggestive* the routing page gives Type-C in general. The hypothesis predicts both the gap's persistence and the "hard to see how" intuition, and the Map's stock acquaintance reply misses it.

## Terminology

- **Ignorance hypothesis (IH)**: "we are ignorant of a type of non-experiential truth relevant to the nature of experience" (OUP intro abstract). The wording is *non-experiential*, not *physical*. The book abstract nevertheless glosses the view as tracing the problem to "our ignorance of the relevant physical facts". The neutral wording lets the hypothesis be stated without first settling what "physical" means.
- **Epistemic view**: E1 (if IH, the logical problem is solved) plus E2 (IH is true). The Map's taxonomy page calls it "Stoljar's epistemic physicalism". That label is the Map's coinage and has no hit in the sources checked.
- **Logical problem of experience**: the inconsistent triad given in the chapter-2 abstract (quoted under Key Sources). Stoljar distinguishes it from "the empirical problem and the traditional mind-body problem".
- **t-physical / o-physical** (Stoljar 2001): properties invoked by physical theory, versus properties of paradigmatically physical objects, including whatever grounds their dispositions. Chalmers (2013) adopts the terms. The 2001 view, physicalism stated over o-physical properties, is the one Chalmers files under type-F.
- **RM4 / "non-standard physicalism"**: the 2013 preprint's name for the Nagel-inspired, non-Russellian version that Stoljar endorses. "Nagelian monism" is the title of a 2015 Stoljar paper, unread here ([[#Gaps in Research|§Gaps]]).
- **Type-C** (Chalmers 2003): "there is a deep epistemic gap between the physical and phenomenal domains, but it is closable in principle". The CPN text explicitly includes an ignorance clause (quoted below).

## Key Sources

### Stoljar, *Ignorance and Imagination: The Epistemic Origin of the Problem of Consciousness* (OUP 2006)
- **DOI**: 10.1093/0195306589.001.0001. Published 2006-07-01 (Crossref); xi + 249 pp. (Levine's *Mind* review header). Chapter DOIs `10.1093/0195306589.003.intro` and `.0001`–`.0011`, with pages from Crossref.
- **Type**: monograph. **Read**: the publisher's book abstract and all twelve chapter abstracts (Crossref). Body text not read; one body quotation is relayed secondarily (McClelland, below).
- **Key points** (all from OUP abstracts):
  - Book: "Instead, we should view the problem itself as having its origin in our ignorance of the relevant physical facts."
  - Introduction (pp. 3–14): "a hypothesis about our epistemic situation that the author calls “the ignorance hypothesis”, which says that we are ignorant of a type of non-experiential truth relevant to the nature of experience". The introduction also presents "the example of the slugs and tiles — the main aid to thought in the book".
  - Ch. 2, "Three Problems of Experience" (pp. 25–47): the logical problem "focuses on three inconsistent theses: there are experiential truths; if there are experiential truths, every truth is entailed by, or supervenes on, some non-experiential truth; and if there are experiential truths, not every truth is entailed by, or supervenes on, some non-experiential truth."
  - Ch. 3, "The Skeptical Challenge" (pp. 48–64): against those who reject conceivability-to-possibility reasoning, "this reasoning is ubiquitous in philosophy, and thus to the extent that there is a problem here it is everyone’s rather than the author’s."
  - Ch. 4, "Error from Ignorance" (pp. 67–86): "This suggests in turn that E1 is true: if the ignorance hypothesis is true, the logical problem is solved."
  - Ch. 5, "General Plausibility" (pp. 87–105), on E2: "The epistemic view is also compared and contrasted with McGinn’s mysterianism."
  - Ch. 6, "Russellian Speculations" (pp. 106–122): "Russell’s idea is that empirical inquiry acquaints only with relational or dispositional features of physical objects, rather than their categorical or intrinsic features. A version of the epistemic view based on this idea is explicated."
  - Ch. 7, "Historical Precedent" (pp. 123–141): "the epistemic view is known to be correct for older philosophical problems that are structurally analogous to the logical problem".
  - Ch. 8, "Objections and Replies" (pp. 142–172): two objections, that "we are in possession of the relevant truths", and that the view has "a range of alarming side effects".
  - Ch. 9, "A Posteriori Entailment" (pp. 175–197): the view "either ... has no answer to the arguments, or else collapses into the epistemic view". Ch. 10 makes the analogous claim for a priori entailment (pp. 198–217).
  - Ch. 11 (pp. 218–234): rejects eliminativism and "primitivism", and criticises the argument from "revelation".
- **Tenet alignment**: conflicts with Tenet 1 as a defence of physicalism. It is neutral on Tenets 2–4, and shares Tenet 5's premise while reversing its target.

### Stoljar, "Two Conceptions of the Physical" (*PPR* 62(2), 2001, 253–281) and the SEP "Physicalism" entry
- **DOI**: 10.1111/j.1933-1592.2001.tb00056.x. **Read**: abstract (OpenAlex).
- **Key point**: an inconsistent tetrad: "(1) if physicalism is true, a priori physicalism is true; (2) a priori physicalism is false; (3) if physicalism is false, epiphenomenalism is true; (4) epiphenomenalism is false." It is resolved by distinguishing a theory-based from an object-based conception of the physical. This is the view Chalmers files under type-F.
- **SEP "Physicalism"** (Stoljar, revision of 16 September 2026; raw HTML grepped). The "third response" to the knowledge argument "leaves open the possibility that one might appeal to the object-conception of the physical to define a version of physicalism which evades the knowledge argument." The entry has 0 hits for "ignoran" and does not list the 2006 book in its bibliography (the 2006 year token appears under other authors only). The SEP therefore carries the 2001 precursor, not the ignorance hypothesis.

### Stoljar, "Four Kinds of Russellian Monism" (in U. Kriegel, ed., *Current Controversies in Philosophy of Mind*, Routledge, pp. 17–39)
- **Metadata**: Crossref gives DOI 10.4324/9780203116623-1, "issued 2013-10-01". The Taylor & Francis page attaches that DOI to Kriegel's introduction (pp. 1–13), a publisher metadata conflict (see §Gaps). Chalmers (2013) cites it as "Stoljar, D. 2013".
- **Read**: the author's preprint (ANU Open Research, handle 1885/23387; 25 pp.). Quotations and page numbers are the preprint's.
- **Key points**:
  - "My own feeling, as will emerge in the final section of the paper, is that only the fourth of these represents a viable version of the view." (p. 1)
  - Footnote 1 lists among similar names "“the Russellian version of the epistemic view” (Stoljar 2006)". In the book, Russellian monism is one version of the epistemic view.
  - RM4 starts from Nagel's *The View from Nowhere* (1986, pp. 52–3). It holds that current theory is incomplete and that "in the limit of inquiry (a limit which we will perhaps never reach)" a complete theory may be reached, so that "we are currently ignorant about theoretically important aspects of matter" (p. 18).
  - RM4.a: "CT-materialism is false, and false for reasons quite distinct from those involved in the conceivability argument." The substitute thesis (CT-materialism+) counts final-theory properties as physical and "does not face" the conceivability argument (p. 19).
  - **On structure and dynamics** (pp. 20–22). Stoljar takes three readings of "structure". On mathematical structure, premise 1 is false, because physics is empirical. On metaphysical (relational) structure, all three premises fail; "some truths about consciousness are themselves relational". On Chalmers's nomic-spatiotemporal reading he poses a dilemma. If the reading lets physics name the causes of experience, the proponent denies premise 3: "we don’t know currently what those properties are", "so we are in no position to assert that no truth about consciousness is a truth about them". If not, the proponent denies premise 1. "In sum, if by ‘structure’ one means either mathematical, metaphysical, or nomic and spatiotemporal structure, SDO is unpersuasive, and RM4 emerges as the most promising version of Russellian Monism."
  - On genus and species: "in other places I have treated Russellian Monism as a specific version of RM4, rather than the other way around (see Stoljar 2006)". And: "RM4 might not (might not) be a version of Russellian Monism, but it remains the closest thing that is plausible." (p. 23)
  - **Footnote 29**: "Chalmers would, I think, classify RM4 as a version of materialism—type-C materialism, in particular—and would set it aside from genuine Russellian Monism which would be classified as type-F monism."
  - Footnote 30: Pereboom's case for requiring that the unknown properties be absolutely intrinsic "apparently relies on the idea sometimes called ‘revelation’—and this is an idea I have been critical of elsewhere". This links to [[revelation-thesis]].
- **Tenet alignment**: conflicts with Tenet 1. Its anti-SDO argument bears directly on the "method-claim" that [[physical-completeness]] L90 calls a bet.

### Stoljar, "Chalmers v Chalmers" (*Noûs* 54(2), 2020, 469–487) and "The Epistemic Approach to the Problem of Consciousness" (*Oxford Handbook of the Philosophy of Consciousness*, 2020, 481–496)
- **DOIs**: 10.1111/nous.12334; 10.1093/oxfordhb/9780198749677.013.22. **Read**: abstracts (Crossref).
- *Noûs* abstract: Chalmers's dualism is inconsistent with his structuralism, and "the best response to the inconsistency, I argue, is to adopt what Chalmers calls ‘type‐C Materialism’, a version of materialism that has been much discussed in recent times because of its promise to move us beyond the stand‐off between standard versions of materialism and dualism." This is Stoljar's own type-C filing.
- Handbook abstract: on the epistemic view "we are ignorant at least for the time being of something important and relevant when it comes to the hard problem, and this fact has a significant implication for its solution." It takes two objections. First, "while we may be ignorant of various features of the world, we are not ignorant of any feature that is relevant to the hard problem". Second, "even if the epistemic approach is true, properly understood it is not an answer to the hard problem; indeed, it is no contribution to that problem at all." It closes by asking why "the epistemic approach, despite its attractiveness, remains a minority view in contemporary philosophy of mind."

### Kind & Stoljar, *What is Consciousness? A Debate* (Routledge, Little Debates about Big Questions, 2023; foreword by Frank Jackson)
- **DOI**: 10.4324/9780429324017 (Crossref lists Kind, Stoljar, Jackson; the publisher TOC reads "Foreword by Frank Jackson"). **Read**: the publisher description and all six chapter abstracts (Taylor & Francis page JSON). Body text not read.
- Book description: the two authors are "united in their rejection of this kind of “standard” physicalism". "Amy Kind defends dualism 2.0, a thoroughly modern version of dualism", while "Daniel Stoljar defends non-standard physicalism, a kind of physicalism different from both the standard version and dualism 2.0."
- Kind, "The Mind-Body Problem: Dualism Rebooted" (pp. 3–62): "it develops Dualism 2.0, a contemporary version of the dualist view, one that avoids many of the problems traditionally associated with dualism. It also provides reasons to think that dualism is our best bet for accounting for consciousness."
- Stoljar, "Non-standard Physicalism: The Epistemic Approach to the Problem of Consciousness" (pp. 63–131). Part II covers "(b) how the epistemic view undermines those arguments". Part III examines the idea that "(a) there are laws connecting every conscious state with some physical state, and (b) that consciousness science aims at providing systematic information about those laws", and "argues that this assumption should be replaced with a more modest and defensible conception of the science of consciousness."
- Kind, "Ignorance Is No Defense: Reply to Daniel Stoljar" (pp. 135–154): "It offers reasons to think that the view is unsatisfactory."
- Stoljar, "Taking Non-Standard Options Seriously: Reply to Amy Kind" (pp. 155–173): "It argues that Kind does not take non-standard options on the problem of consciousness seriously enough."
- Kind, "The Consciousness Slugathon: Reply to Daniel Stoljar's Reply" (pp. 177–192): "(a) to show that non-standard versions of physicalism do not fare any better than standard versions and (b) to defend against his assertion that dualism is impossible to believe."
- Stoljar, "Even More Seriously: Reply to Amy Kind's Reply" (pp. 193–200) summarises Kind's three objections. First, "while people are indeed ignorant in some sense or other, just as the view says, this would not have the advertised effect on such key arguments as the conceivability argument and the knowledge argument." Second: "The second objection is what Kind calls the “you’re not done” objection". It "concedes for the sake of argument that the epistemic view undermines arguments like the conceivability argument, but points out that there are further issues about consciousness that the view does not address." Third, a burden-of-proof objection: "This objection says that the epistemic view assumes that physicalism is a default hypothesis, and defends it at all costs."
- **Tenet alignment**: Kind is a published dualist interlocutor for the Map. Her own arguments are known only through these abstracts.

### Chalmers, "Consciousness and its Place in Nature" (2003)
- **Read**: full text, author's version (consc.net/papers/nature.html).
- Type-C, described with an ignorance clause: "it is accessible in principle (perhaps accessible a priori), but is not accessible to us now, perhaps because the reasoning required is currently beyond us, or perhaps because we do not currently grasp all the required physical truths."
- On incomplete physics: "Some type-C materialists hold we do not yet have a complete physics, so we cannot know what such a physics might explain. But here we do not need to have a complete physics: we simply need the claim that physical descriptions are in terms of structure and dynamics."
- The one complete-physics appeal "that should be taken seriously" is intrinsic natures: "The relevant intrinsic properties are unknown to us, but they are knowable in principle. This is an important position, but it is precisely the position discussed under type F".
- **The filing** (type-A section, footnote): "(ii) Some views (e.g., Stoljar 2001 and Strawson 2000) deny an epistemic gap not by functionally analyzing consciousness but by expanding our view of the physical base to include underlying intrinsic properties. These views are discussed under type F." And in the type-F footnote: "Versions of type-F monism have been put forward by Russell 1926, Feigl 1958/1967, Maxwell 1979, Lockwood 1989, Chalmers 1996, Griffin 1998, Strawson 2000, and Stoljar 2001."
- On type-F: "From one perspective, it can be seen as a sort of materialism." And: "One might suggest that while the view arguably fits the letter of materialism, it shares the spirit of antimaterialism."
- The type-C sympathisers footnote: "I think McGinn is ultimately a type-F monist".
- **The hook argument**: "epistemic implication from A to B requires some sort of conceptual hook by virtue of which the condition described in A can satisfy the conceptual requirements for the truth of B."

### Chalmers, "The Meta-Problem of Consciousness" (*JCS* 25(9–10), 2018, 6–61), §"Underestimating the physical"
- **Read**: full text (consc.net PDF in the journal layout; the passage is on pp. 32–33, after page headers; McClelland 2020 cites p. 31 for its opening sentence).
- "we are only impressed by the mind–body problem because we underestimate the body" (the PDF hyphenates "under-estimate" across a line). "One version of this view (e.g. Stoljar, 2001; Strawson, 2006) holds that we conceive of the physical in structural terms (perhaps in terms of the equations of physics), ignoring its intrinsic nature, which may have a close tie to consciousness. This path often leads to panpsychism and Russellian monism."
- Chalmers's reply: "the key intuition in setting up the hard problem is that explaining functions does not explain consciousness." Such intuitions "concern the phenomenal" and, on the next page, "rather than the physical and are not removed by enriching our conception of the physical." The sentence spans a page break with footnotes 24–25 between its halves, so the two halves were verified separately.
- He again cites Stoljar **2001**, not 2006.

### Chalmers, "Panpsychism and Panprotopsychism" (2013 Amherst Lecture; author's PDF)
- **Read**: author's PDF (consc.net/papers/panpsychism.pdf, marked "Forthcoming as the 2013 Amherst Lecture in Philosophy"). The quotes are from its pp. 17–18.
- Footnote 11: "Stoljar and Strawson are naturally counted as expansionary Russellian physicalists." Footnote 12 concludes that "Russellian monism is not best characterized (following Stoljar) as o-physicalism about consciousness without t-physicalism."

### Papineau, review of *Ignorance and Imagination* (*Notre Dame Philosophical Reviews* 2007.04.15)
- **URL**: https://ndpr.nd.edu/reviews/ignorance-and-imagination-the-epistemic-origin-of-the-problem-of-consciousness/ (full text read).
- Summary: "The central thesis of Daniel Stoljar's book is that we are puzzled about consciousness only because we don't know enough about the non-conscious facts."
- On McGinn and Russell: "As McGinn tells it, not only are we ignorant of the non-experiential facts that determine experiential facts, but this ignorance is chronic." Stoljar's moderate view drops both extras: "It only adds extra hostages to argumentative fortune to claim that this ignorance is irremediable, or that it is of categorical matters."
- On the precedents: "Hindsight shows that Descartes' and Broad's ignorance was certainly not irremediable; nor was it of categorical facts, given that both computation and quantum bonding are most naturally thought of in terms of causal roles."
- **Objection 1** (the "how could ignorance close the gap" objection): "By their nature, non-experiential facts would seem to be third-personal, objective, and non-perspectival, while experiential facts are first-personal, subjective, and perspectival. It is hard to see how knowledge of the former could automatically render the absence of the latter inconceivable." In reply, Stoljar uses Nagel's point of view and the pair *John is a number* / *John is not in pain*. Papineau finds this insufficient for positive experiential claims, and adds: "But it is then very hard to avoid wondering how knowledge of mundane scientific facts could possibly render zombies inconceivable."
- **Objection 2** (from the Type-B side): "Since a posteriori physicalists deny that any claims linking the physical and the conscious realms are a priori, won't they automatically hold that zombies are conceivable?" Papineau reports that Stoljar's late reading of conceivability is that "we should simply read it as saying that 'it appears possible that not-p'." He then argues that physicalists can explain the appearance instead.
- Verdict: "I think that Stoljar is looking in the wrong place for a solution to the problem of consciousness."
- **Tenet alignment**: Papineau is a Type-B physicalist. His objection 1 is the one the Map would want, but he states it as an intuition ("hard to see how"), and IH predicts that intuition.

### McClelland, "Ignorance and the Meta-Problem of Consciousness" (*JCS* 27, 2020)
- **Read**: submitted version (Cambridge Apollo, DOI 10.17863/cam.120115). The JCS venue and volume come from OpenAlex; issue and pages were not confirmed.
- Abstract: "Although Chalmers quickly dismisses this view, I argue that it has much greater promise than he recognises." Problem intuitions are "hybrid intuitions that encompass one’s intuitive take on the phenomenal and one’s intuitive take on the physical. The ignorance hypothesis undermines the second half of these hybrid intuitions."
- IH, unlike other views, "holds that the shortcomings lie on the physical side of these hybrid judgements (Montero 1999)".
- On Stoljar's development: "Stoljar started out arguing for the Russellian version of IH (2001) but then went on to adopt a general formulation of IH without such a commitment."
- A secondary relay of Stoljar 2006, p. 10: "…a hypothesis about our current epistemic situation is the best explanation for the distinctively philosophical predicament we are confronted with when we think about experience". This is relayed by McClelland, not checked against the book.

### Supporting sources (metadata verified; content not read)
- Stoljar, D. (2009). Précis of *Ignorance and Imagination*. *PPR* 79(3), 748–755. 10.1111/j.1933-1592.2009.00302.x
- Alter, T. (2009). Does the Ignorance Hypothesis Undermine the Conceivability and Knowledge Arguments? *PPR* 79(3), 756–765. 10.1111/j.1933-1592.2009.00303.x
- Bennett, K. (2009). What You Don't Know Can Hurt You. *PPR* 79(3), 766–774. 10.1111/j.1933-1592.2009.00304.x
- Stoljar, D. (2009). Response to Alter and Bennett. *PPR* 79(3), 775–784. 10.1111/j.1933-1592.2009.00305.x
- Gertler, B. (2009). The Role of Ignorance in the Problem of Consciousness (critical notice). *Noûs* 43(2), 378–393. 10.1111/j.1468-0068.2009.00711.x
- Levine, J. (2008). Review of *Ignorance and Imagination*. *Mind* 117(465), 228–231. 10.1093/mind/fzn022
- Doggett, T. & Stoljar, D. (2010). Does Nagel's Footnote Eleven Solve the Mind-Body Problem? *Philosophical Issues* 20, 125–143. 10.1111/j.1533-6077.2010.00184.x. Co-authored; do not cite as Stoljar alone.
- Stoljar, D. (2010). *Physicalism*. Routledge. 10.4324/9780203856307 (publisher description only; no IH-specific content read).
- Stoljar, D. (2019). Panpsychism and Non-standard Materialism. In *The Routledge Handbook of Panpsychism*, 218–229. 10.4324/9781315717708-19. Abstract (OpenAlex): "I will argue that non-standard materialism is preferable in several ways to panpsychism."
- Cutter, B. (2023). The Inconceivability Argument. *Ergo* 9. 10.3998/ergo.2268. Abstract: "First, it is not (ideally, positively) conceivable that phenomenal truths are grounded in physical truths." It is an unread but obvious target for IH, since the premise is about ideal conceivability.
- Botin, M. (2023). Russellian Physicalists get our phenomenal concepts wrong. *Philosophical Studies* 180(7), 1829–1848. 10.1007/s11098-023-01955-1. Abstract: a "revelation challenge" to Russellian physicalism. It bears on the Russellian species only.

## Major Positions

### The epistemic view (Stoljar 2006 →)
- **Core claim**: IH is true and, if true, dissolves the logical problem. It is neutral on what the unknown truths are: they need be neither categorical nor permanently unknowable.
- **Arguments**: general plausibility, the slugs-and-tiles model, historical precedent, and the claim that the rival entailment views either fail or collapse into it.
- **Relation to tenets**: denies Tenet 1's ground (irreducibility), not the reality of experience. It is compatible with consciousness being causally efficacious, since consciousness is physical, so Tenet 3's selector does nothing against it ([[positions/arguments-for-dualism#^p-d2|P-D2]]: Bidirectional Interaction selects *among irreducibility-respecting alternatives*, and IH-physicalism is not one).

### Russellian version (Stoljar 2001; ch. 6 of the 2006 book)
- **Core claim**: the unknown truths concern the categorical or intrinsic bases of physical dispositions. This is type-F in Chalmers's scheme. Stoljar later treats it as one species of the epistemic view, and Chalmers counts Stoljar among the "expansionary Russellian physicalists".
- **Relation to tenets**: answered by [[russellian-monism]] (combination problem, instability, epiphenomenalism return).

### Mysterianism (McGinn 1989)
- **Core claim**: the ignorance is permanent for minds like ours (cognitive closure). Chalmers files McGinn as type-F. Papineau: McGinn's ignorance "is chronic". Stoljar's ch. 5 compares the two views.
- **Relation to tenets**: [[mysterianism]] gives it the strongest Tenet-5 alignment. The differences from IH (permanence; a special missing property P) are what make IH the harder opponent: it asks for less.

### Type-C materialism (Chalmers's category)
- **Core claim**: the gap is deep but closable in principle. Chalmers argues it is "inherently unstable" and collapses into A, B, D or F. Stoljar accepts the label in 2020 and contests the collapse premise (structure and dynamics).

### A posteriori (Type-B) physicalism as a rival diagnosis (Papineau)
- **Core claim**: zombies are conceivable and the appearance of distinctness is explained without positing ignorance. Stoljar's ch. 9 argues this view needs "further material" and collapses into the epistemic view, while Papineau argues Stoljar never gives a principled rationale for his conceivability assumptions. This is the IH-versus-Type-B front, which the Map watches from outside.

### Dualism 2.0 (Kind 2023)
- **Core claim**: a modern dualism, "our best bet". Against IH, the ignorance would not defeat the arguments, the view is not done, and it presumes physicalism.
- **Relation to tenets**: the closest published ally for the Map in this exchange. Its content is abstract-level only.

## Key Debates

### 1. Could ignorance of non-experiential truths close the gap? (the central objection)
- **Sides**: Papineau 2007 (third-personal facts cannot make the absence of first-personal facts inconceivable), Chalmers 2003 (no "conceptual hook"), Kind 2023 (no "advertised effect"), and the first objection in Stoljar's 2020 Handbook chapter, against Stoljar (the *John is a number* point; Nagelian points of view; the 2013 dilemma about premise 3).
- **Core disagreement**: whether any non-experiential truth could a priori necessitate a *positive* experiential truth. Stoljar's example shows a non-experiential truth necessitating a *negative* one. Papineau says that does not carry over.
- **State**: open. For the Map, note an asymmetry. The objection is strongest when it rests on the concept of consciousness (Chalmers's hook, which needs only that consciousness is not a functional concept, as Stoljar grants). It is weakest when it rests on what physical truths could be like, because that is exactly where IH says we are ignorant.

### 2. Is the structure-and-dynamics argument sound?
- **Sides**: Chalmers 2003/2010 against Stoljar 2006, 2009 and 2013 (three readings of "structure", each failing). Pereboom's absolutely intrinsic properties and Alter–Nagasawa are cited by Stoljar but were not read here.
- **State**: open. The Map's own position is already modest: [[physical-completeness]] L90 says the Map's position "is a bet on the method-claim, not a proof of it" and that the gap is "robust across the physics we can presently envisage". [[intrinsic-nature]] L43 states the method-claim more firmly ("that silence is a feature of the method, not a deficit of current theory"). The two pages should agree. An article on IH has to cite the weaker form.

### 3. Is the view empty, unfalsifiable, or no answer at all?
- **Sides**: Kind's "you're not done" and burden-of-proof objections. The second objection in Stoljar's Handbook chapter ("no contribution to that problem at all") is one Stoljar raises against himself. The Map's own Hempel analysis bears on it too: [[intrinsic-nature]] L59 says physicalism over completed physics is "unfalsifiable", citing Montero 2003.
- **Core disagreement**: IH is physicalism over a not-yet-known physics, the second horn of Hempel's dilemma. Its defenders reply that it targets the *logical* problem (the anti-physicalist arguments), not the hard problem.
- **For the Map, a symmetry caution**: Tenet 2 is described on [[tenets]] as a "consistency claim" rather than a novel-prediction claim. Charging IH with unfalsifiability while defending the interface as consistency-only would breach Tenet 5's symmetric discipline. The fair charge is narrower: IH, as stated, makes no prediction that dualism does not also make.

### 4. Historical precedent
- **Sides**: Stoljar ch. 7 (Broad's chemistry, Descartes's language: modal arguments that looked compelling and failed through ignorance) against the Map's disanalogy ([[vitalism]] §"The Disanalogy Reply"; [[conceivability-possibility-inference]] L104–L106).
- **Observation**: Papineau's description of the precedents, that the missing facts were "most naturally thought of in terms of causal roles", is the structural fact the Map's disanalogy needs. In those cases the explanandum was functional, so a conceptual hook existed. Papineau makes the point to separate Stoljar from Russell, not to defend dualism. Attribute the use to the Map.

### 5. Whose collapse?
- Chalmers: Type-C collapses into A, B, D or F. Stoljar: the a posteriori and a priori entailment views (B and A) need "further material" and either fail or collapse into the epistemic view. Each side's collapse argument assumes its own verdict on the structure premise. Neither collapse is settled, and the routing page already reports Chalmers's as "Chalmers's argument, not a settled result".

## Reconciling the Filings

**Chalmers's filing is of the 2001 view, and it is accurate for that view.** "Consciousness and its Place in Nature" (2002/2003) predates *Ignorance and Imagination*, and both its Stoljar footnotes cite Stoljar 2001, the object-based or intrinsic-property expansion. Chalmers's later texts that were checked (2013, 2018) also cite 2001 and place Stoljar with Russellian or expansionary physicalism. None of the texts read files the 2006 ignorance hypothesis. The routing page L75 reports this correctly: Stoljar's 2001-type views are filed "under type F", and "Stoljar's later ignorance hypothesis (2006) ... keeps the type-C hope alive in physicalist terms". The harvesting review's compressed phrasing, that Chalmers files Stoljar under type-F, should not travel into the article.

**The 2006 view is type-C on every account checked.** Chalmers's own type-C definition includes the clause "perhaps because we do not currently grasp all the required physical truths". Stoljar (2013 preprint, n. 29) expects Chalmers to "classify RM4 as a version of materialism—type-C materialism, in particular". Stoljar (2020) recommends "type‐C Materialism" by name. McClelland (2020) confirms the move from the Russellian 2001 view to the general 2006 formulation. Whether IH *collapses* into type-F is a separate matter. That is Chalmers's argument (if the unknown truths are not structural, they are intrinsic, hence F), and it depends on the structure premise Stoljar disputes. Collapse into F is an argument, not a filing.

**The Q2 filing answers a different question, and that is compatible in principle.** [[four-quadrant-dualism-taxonomy]] L75 says the thickness axes are "orthogonal" to Chalmers's D/E/F, so a view can be type-C (or F) and Q2 without contradiction. The Q2 entry is nonetheless defective in three respects.

1. **Scope.** The taxonomy "ranges over non-reductive positions on mind–matter" and flags its monist limit cases (L83). Stoljar's view is a physicalism and is not flagged.
2. **Category.** The physical axis measures ontological weight: "'Max-physical' expands the physical side *ontologically*" (L73). IH's thickness is epistemic. It says our *theory* omits truths, not that the world contains more physical ontology than a lean physicalist allows. The L73 coinage "ignorance-facts" turns an epistemic gap into an ontological item, and the min/max contrast is itself indexed to "what physics says", which inherits Hempel's dilemma.
3. **Inherited debts.** The Q2 cell's debts do not apply. [[mechanism-costs-dualism-thickness-quadrants]] L87 assigns Q2 an exclusion debt ("the mind seems to owe *no* causation account at all, because it does no causal work on this reading") and says "this cell is ruled out by Tenet 3". [[four-quadrant-dualism-taxonomy]] L149–L151 has Bidirectional Interaction ruling out pure Q2. On IH, however, consciousness is (o-)physical and does whatever causal work its physical realiser does. The tenet that excludes Stoljar is Tenet 1, not Tenet 3, and his "min-mind" rating holds only vacuously, because the view has no non-physical mind-side.

**Reconciliation.** Neither filing is simply wrong. Chalmers's F is right for 2001, and Q2 is a defensible thickness reading if flagged. The correct composite statement is that Stoljar 2001 is type-F (Chalmers 2003), while the 2006 hypothesis is type-C by Chalmers's definition, Stoljar's self-filing and McClelland's reading, and is argued by Chalmers to collapse toward F. On the thickness grid it belongs as a *flagged physicalist limit case* of Q2, whose physical-side thickness is epistemic and whose mind-side is null, so the Q2 exclusion and Tenet-3 debts do not attach. All three Q2 hosts are over or near their gates (four-quadrant 4,003, over hard; cartography 5,185, over hard; mechanism-costs 3,303, headroom 696), so the fix there is a pointer, not a rewrite.

## Map Relevance

### Tenet 1 (Dualism) and the P-D1/P-D2 structure
IH attacks the stage that earns irreducibility, not the stage that selects dualism. P-D2 sends Bidirectional Interaction to select "among the irreducibility-respecting alternatives", and IH-physicalism is not one, so the Map's case against IH must be carried entirely by the irreducibility cluster that IH undercuts. P-D1 names the phenomenal-concept strategy as the mainstream statement of the cluster's shared premise. Its shift condition ("the phenomenal concept strategy were shown to fail in all its variants, removing the mainstream account of *why* the arguments share a premise") overstates what such a failure would remove, because IH supplies a second account that survives it. That is a positions seam ([[#Corpus Seams|below]]). The register cannot take it length-neutrally (positions/arguments-for-dualism 2,495 words, headroom 4; a dated *Updated* note is mandatory), so it belongs to positions-evolve, not to the article.

### Tenet 5 (Occam's Razor Has Limits): is the Map committed to taking IH seriously?
**Yes, to E2; no, to E1.** The tenet states that "Simplicity is not a reliable guide to truth when knowledge is incomplete", that "our conceptual tools may be fundamentally inadequate", and that "The apparent simplicity of physicalism could reflect ignorance rather than insight". The symmetric-discipline clause ("parsimony cannot decide for or against a framework when the relevant knowledge is incomplete") formally governs parsimony only. Its premise, though, is incompleteness of knowledge relevant to the mind–body problem, and that is E2 in substance. A Map that asserts that premise against physicalism's simplicity cannot then treat the same premise as ad hoc when it is pointed against the conceivability arguments. The apparent distinctness of consciousness could, by parity, reflect ignorance rather than insight. What Tenet 5 does not commit the Map to is E1, the claim that the relevant unknowns are *non-experiential* truths whose discovery would close the gap.

**The disagreement is over the content of the ignorance.** The Map also holds that current physics is incomplete in a way relevant to consciousness. [[physical-completeness]] L86–L88 holds that "Actuality-selection is not a structural determination" and that the structural completeness of current physics "does not entail ontological completeness". On the Map's view, what is missing involves consciousness itself: selection at quantum indeterminacy. That is Chalmers's fourth route ("physics might end up appealing to consciousness itself"), which "leads to a view on which consciousness is itself irreducible" (type-D), and the routing page L77 already places the Map there by commitment. Stoljar's missing truths are non-experiential. Both views predict that the gap persists and that current physics is incomplete. In principle they come apart over whether the completing theory's laws must contain experiential variables. An outcome deviation conditioned on intention, the discriminating channel the routing page L124 names, would push any completion toward route 4. None has been observed. This analysis is the Map's, not Stoljar's or Chalmers's, and the article must label it so.

### Tier calibration (P-M1)
- Against IH-physicalism the Map's tier is **compatible**. The routing page gives Type-C generally a *suggestive* tier, but IH breaks each of the supports for that verdict.
  - Persistence: the routing page L123 says "Persistence is mildly unexpected on Type-C". IH makes no timescale prediction. Stoljar's ignorance holds "at least for the time being", and the limit of inquiry is one "which we will perhaps never reach". Persistence is therefore expected on IH, as on dualism.
  - The "hard to see how" intuition is predicted by IH, so citing it is not evidence against IH.
  - The acquaintance reply misses (see seams).
- Replies that do reach IH, each defeater-removing or dialectical and none tier-raising:
  - Chalmers's conceptual-hook argument, in its consciousness-side form.
  - The structure-and-dynamics argument, a contested bet.
  - The precedent disanalogy, which reaches E2's historical support only.
  - Kind's "you're not done", which is dialectical: IH answers the logical problem, not the hard one.
- Removing IH as a defeater would restore the conceivability cluster's standing. It would not raise any tier, by P-M1.

### Tenets 2–4
Tenet 2: IH is closure-compatible. A Stoljarian can absorb a future physics with novel structure, but not one whose laws mention consciousness without becoming route 4. Tenet 3: no purchase, as above. Tenet 4: orthogonal.

## Corpus Seams

Line numbers measured 2026-10-03 at 10:15–10:20Z.

1. **The acquaintance reply misses physical-side ignorance.** [[zombie-master-argument]] L76: "The conceivability of zombies doesn't reflect ignorance of what consciousness is". [[philosophical-zombies]] L85, same move; [[conceivability-possibility-inference]] L108: "we have first-person acquaintance with what consciousness *is*". Each answers ignorance of the *phenomenal* relatum (the water/H₂O model). IH concedes acquaintance and places the ignorance on the physical relatum (McClelland: "the shortcomings lie on the physical side"). Nothing in these passages is false, but none reaches IH, and the routing table files the acquaintance row under B only, which is consistent with that.
2. **"All the physics" begs the question against IH.** [[philosophical-zombies]] L67: "We are positively grasping a coherent scenario: all the physics, none of the experience." On IH we positively conceive only the physics we know. This sentence is exactly what IH denies, and the page has no reply. That page has an open P3 (todo "Replies aimed at the wrong type under a Type-B heading") and 24 words of headroom (3,475), so it is a coordination target, not an article edit.
3. **The ignorance clause is used in one direction only.** [[tenets]] L141: "The apparent simplicity of physicalism could reflect ignorance rather than insight". Parallel uses appear at [[philosophical-zombies]] L209, [[explanatory-gap]] L193, [[conceivability-possibility-inference]] L142 and [[epistemic-advantages-of-dualism]] L48, where the last says the materialist "assumes we know what a complete physics looks like—an assumption mysterians like Colin McGinn reasonably doubt". The same doubt is IH's premise. The article should host the parity point, and these pages should not each be patched.
4. **The routing page's Type-C persistence clause** (L123). See Tier calibration. The verdict is defensible for closure-soon Type-C (Churchland's posture) but not for IH. This is a candidate one-clause scoping for a later refine-draft; the routing page has 681 words of headroom and open P3s naming it as a secondary file.
5. **The Q2 entries** ([[four-quadrant-dualism-taxonomy]] L71, L73, L102, L163; [[dualism-cartography]] L64, L69; [[mechanism-costs-dualism-thickness-quadrants]] L85–L89). See §Reconciling. The first two hosts are over their hard gates, so only zero-word pipes are possible there (a zero-word pipe from "Stoljar's epistemic physicalism" to the new page). The mechanism-costs L85 entry could take a one-clause flag (headroom 696).
6. **Method-claim strength differs between two pages.** [[intrinsic-nature]] L43 ("that silence is a feature of the method, not a deficit of current theory") is firmer than [[physical-completeness]] L90 ("a bet on the method-claim, not a proof of it"). Stoljar's 2013 three-readings argument is aimed exactly at this claim. Flag it for the article's author, but do not fix it in the article.
7. **P-D1's shift condition** ([[positions/arguments-for-dualism]] L50) names only the phenomenal-concept strategy as the account of the shared premise. IH is a second account. This is for positions-evolve.
8. **Coined label.** "Stoljar's epistemic physicalism" (three files) is the Map's phrase. Stoljar's terms are "the epistemic view" (2006), "non-standard materialism" (2019) and "non-standard physicalism" (2023). A new article should use his terms and may note the Map's label once.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1927 | Russell, *The Analysis of Matter* | Physics knows only structure; the source of the Russellian species |
| 1974 | Nagel, "What Is It Like to Be a Bat?" (footnote 11) | Conceptual-revolution hope; subject of Doggett & Stoljar 2010 |
| 1986 | Nagel, *The View from Nowhere*, pp. 52–3 | The passage RM4 starts from |
| 1989 | McGinn, "Can We Solve the Mind–Body Problem?" (*Mind* 98: 349–366) | Permanent-ignorance (cognitive closure) version |
| 2001 | Stoljar, "Two Conceptions of the Physical" (*PPR*); "The Conceivability Argument and Two Conceptions of the Physical" (*Phil. Perspectives* 15) | t-/o-physical; the view Chalmers files as type-F |
| 2002/03 | Chalmers, "Consciousness and its Place in Nature" | A–F taxonomy; type-C collapse; Stoljar 2001 under F |
| 2006 | Stoljar, *Ignorance and Imagination* | The ignorance hypothesis and the epistemic view |
| 2007 | Papineau, NDPR review | The perspectival objection; the Type-B objection |
| 2008–09 | Levine (*Mind*); *PPR* symposium (Précis; Alter; Bennett; Response); Gertler (*Noûs*) | The critical reception (content unread here) |
| 2010 | Stoljar, *Physicalism*; Doggett & Stoljar, "Nagel's Footnote Eleven" | Book-length physicalism; the Nagelian line |
| 2013 | Stoljar, "Four Kinds of Russellian Monism" | RM4 endorsed; SDO rejected on three readings; n. 29 on type-C |
| 2013 | Chalmers, "Panpsychism and Panprotopsychism" | Stoljar as "expansionary Russellian physicalist" |
| 2018 | Chalmers, "The Meta-Problem of Consciousness" §11 | "Underestimating the physical" dismissed |
| 2020 | McClelland (*JCS*); Stoljar, "Chalmers v Chalmers" (*Noûs*); Stoljar, Oxford Handbook chapter | Hybrid intuitions; Stoljar's explicit type-C; two objections stated |
| 2023 | Kind & Stoljar, *What is Consciousness? A Debate* | Dualism 2.0 against non-standard physicalism |

## Potential Article Angles

**Recommended: concepts/`ignorance-hypothesis`, "The Ignorance Hypothesis".** Lead with Stoljar's formulation and the E1/E2 structure, in his terms. Then cover:

1. **Where it sits**: type-C, not type-F. Give the 2001/2006 distinction in two sentences, link the routing page for the collapse argument, and state the Q2 flag (§Reconciling).
2. **Why it is the hardest opponent for the Map's core cluster**: it undercuts the shared premise from the physical side, survives the failure of phenomenal-concept accounts, and is untouched by Tenet 3's selector.
3. **What does not answer it**: the acquaintance reply, the "all the physics" conceivability claim, persistence, and the "hard to see how" intuition.
4. **What does reach it**: the conceptual-hook argument (its strongest form rests on the concept of consciousness, as Kind and Papineau press it); the structure-and-dynamics argument, with Stoljar's three-readings reply and [[physical-completeness]]'s "bet" posture; the precedent disanalogy ([[vitalism]]); and "you're not done".
5. **Tenet 5 parity**: the Map grants E2 and contests E1, and the disagreement is over the *content* of the ignorance (non-experiential truths versus consciousness-involving selection, route 4).
6. **Tier**: *compatible*, with the replies filed as defeater-removal under P-M1.

Alternative (not recommended): a comparative page, "Two ignorance hypotheses: Stoljar and the Map". It would over-weight the Map's own speculative content.

When writing the article, follow `obsidian/project/writing-style.md` for the named-anchor summary technique for forward references, background-versus-novelty decisions (what to include and omit), tenet alignment, and LLM optimisation (front-load the important information).

### Articles that should later cite it (lengths by `analyze_length`, 2026-10-03; concepts hard 3,500, topics 4,000, apex 5,000, positions 2,500; gate `>=`; headroom = hard − 1 − count)

| Page | Words | Headroom | Locus | Edit |
|------|-------|----------|-------|------|
| concepts/type-a-type-b-and-type-c-physicalism | 2,818 | 681 | L75 "Stoljar's later ignorance hypothesis (2006)" | zero-word pipe; optional Further Reading line |
| concepts/physical-completeness | 2,703 | 796 | L90 (method-claim bet) | one-sentence pointer |
| concepts/russellian-monism | 2,949 | 550 | §"The Mysterian Angle" L107–L109 or Further Reading | one line |
| topics/mechanism-costs-dualism-thickness-quadrants | 3,303 | 696 | L85 Q2 list | pipe plus one-clause flag (exclusion debt does not attach) |
| concepts/vitalism | 2,426 | 1,073 | §"The Disanalogy Reply" | optional one line (Stoljar's precedents) |
| topics/four-quadrant-dualism-taxonomy | 4,003 | −4 (over hard) | L102 | zero-word pipe only |
| apex/dualism-cartography | 5,185 | −186 (over hard) | L69 | zero-word pipe only |
| concepts/mysterianism | 3,434 | 65 | §"Temporary Versus Permanent" L138 | zero-word pipe only |
| concepts/zombie-master-argument | 3,042 | 457 | L76 | leave for a later task (seam 1) |
| concepts/knowledge-argument | 3,491 | 8 | — | none |
| concepts/explanatory-gap | 3,495 | 4 | L193 | none |
| positions/arguments-for-dualism | 2,495 | 4 | P-D1 L50 | positions-evolve only |

## Gaps in Research

- **The book's body text was not read.** Every claim about *Ignorance and Imagination* rests on OUP's abstracts plus Papineau's and McClelland's reports. The *John is a number* example, the slugs and tiles, and the late reading of conceivability as appearance of possibility are relayed by Papineau. The p. 10 quotation is relayed by McClelland.
- **The 2009 *PPR* symposium content** (Alter, Bennett, Stoljar's response) and **Gertler's 2009 critical notice** were not read; their metadata only is verified. These are probably the most sustained academic critiques of E1, and Alter's title asks the exact question. Their arguments are leads, not citations.
- **Levine 2008** (*Mind*): metadata only.
- **Stoljar 2015, "Russellian Monism or Nagelian Monism?"**: confirmed only as an OpenAlex index record (PhilPapers source). The venue (presumably Alter & Nagasawa, eds., *Consciousness in the Physical World*, OUP 2015) and pages are unverified. Treat as a lead.
- **Doggett & Stoljar 2010** and **Stoljar's 2020 Handbook chapter**: abstracts or metadata only (Wiley and ANU blocked).
- **Kind 2023**: abstract-level only. Whether her "you're not done" objection is the hard problem restated, or something sharper, needs the chapter.
- **Chalmers on the 2006 book**: no text found in which Chalmers files the 2006 ignorance hypothesis by letter. Stoljar's n. 29 is a forecast, not a report. The Map should say "on Stoljar's reading" when it states the type-C filing in Chalmers's name.
- **Metadata conflict**: DOI 10.4324/9780203116623-1 resolves to Stoljar's chapter in Crossref (pp. 17–39) but to Kriegel's introduction on the Taylor & Francis page. Cite the volume and pages and note the DOI as Crossref's.
- **McClelland 2020**: the venue (*JCS* 27) comes from OpenAlex; issue and pages are unconfirmed. McClelland 2013, "The Neo-Russellian Ignorance Hypothesis" (*JCS*), was not read.
- **Cutter 2023**: whether the inconceivability argument is immune to IH (it relies on *ideal* positive conceivability) is an open and unrun question.
- **Search**: no WebSearch was available. Philosophers' replies published after 2023 may have been missed.

## Citations

1. Chalmers, D. J. (2003). Consciousness and its place in nature. In S. P. Stich & T. A. Warfield (Eds.), *The Blackwell Guide to Philosophy of Mind* (pp. 102–142). Blackwell. https://consc.net/papers/nature.html (full text, author's version)
2. Chalmers, D. J. (2013). Panpsychism and panprotopsychism. The Amherst Lecture in Philosophy. https://consc.net/papers/panpsychism.pdf (full text, author's PDF; quoted pages are that PDF's)
3. Chalmers, D. J. (2018). The meta-problem of consciousness. *Journal of Consciousness Studies*, 25(9–10), 6–61. https://consc.net/papers/metaproblem.pdf (full text)
4. Kind, A., & Stoljar, D. (2023). *What is Consciousness? A Debate*. Routledge (Little Debates about Big Questions; foreword by F. Jackson). https://doi.org/10.4324/9780429324017 (publisher description and chapter abstracts). Chapters: Kind, The Mind-Body Problem: Dualism Rebooted (3–62); Stoljar, Non-standard Physicalism: The Epistemic Approach to the Problem of Consciousness (63–131); Kind, Ignorance Is No Defense (135–154); Stoljar, Taking Non-Standard Options Seriously (155–173); Kind, The Consciousness Slugathon (177–192); Stoljar, Even More Seriously (193–200).
5. McClelland, T. (2020). Ignorance and the meta-problem of consciousness. *Journal of Consciousness Studies*, 27. https://doi.org/10.17863/cam.120115 (full text, submitted version)
6. Papineau, D. (2007). Review of D. Stoljar, *Ignorance and Imagination*. *Notre Dame Philosophical Reviews*, 2007.04.15. https://ndpr.nd.edu/reviews/ignorance-and-imagination-the-epistemic-origin-of-the-problem-of-consciousness/ (full text)
7. Stoljar, D. (2001). Two conceptions of the physical. *Philosophy and Phenomenological Research*, 62(2), 253–281. https://doi.org/10.1111/j.1933-1592.2001.tb00056.x (abstract)
8. Stoljar, D. (2006). *Ignorance and Imagination: The Epistemic Origin of the Problem of Consciousness*. Oxford University Press. https://doi.org/10.1093/0195306589.001.0001 (book and chapter abstracts)
9. Stoljar, D. (2013). Four kinds of Russellian monism. In U. Kriegel (Ed.), *Current Controversies in Philosophy of Mind* (pp. 17–39). Routledge. Crossref DOI https://doi.org/10.4324/9780203116623-1 (full text, author's preprint, ANU Open Research http://hdl.handle.net/1885/23387)
10. Stoljar, D. (2020). Chalmers v Chalmers. *Noûs*, 54(2), 469–487. https://doi.org/10.1111/nous.12334 (abstract)
11. Stoljar, D. (2020). The epistemic approach to the problem of consciousness. In U. Kriegel (Ed.), *The Oxford Handbook of the Philosophy of Consciousness* (pp. 481–496). Oxford University Press. https://doi.org/10.1093/oxfordhb/9780198749677.013.22 (abstract)
12. Stoljar, D. (2026 revision). Physicalism. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/physicalism/ (full text)
13. Metadata-only (content not read; see §Gaps): Alter 2009; Bennett 2009; Stoljar 2009a, 2009b (*PPR* 79(3)); Gertler 2009 (*Noûs* 43(2)); Levine 2008 (*Mind* 117(465)); Doggett & Stoljar 2010 (*Phil. Issues* 20); Stoljar 2010 (*Physicalism*, Routledge); Stoljar 2019 (Routledge Handbook of Panpsychism); Stoljar 2015 (OpenAlex record only); Cutter 2023 (*Ergo* 9, abstract); Botin 2023 (*Phil. Studies* 180, abstract); McGinn 1989 (*Mind* 98(391), 349–366, https://doi.org/10.1093/mind/xcviii.391.349).
