---
title: "Optimistic Review - 2026-11-26 - The Other-Minds Wing"
created: 2026-11-26
modified: 2026-11-26
human_modified: null
ai_modified: 2026-11-26T14:05:41+00:00
draft: false
description: "Wing review of three pages on other minds: the metaphysical problem, the second-person channel and logical behaviourism. All three are well calibrated, but no page in the wing links to another, and two hubs overstate."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-26
last_curated: null
last_deep_review: null
---

# Optimistic Review: The Other-Minds Wing

**Date**: 2026-11-26
**Slot**: cycle optimistic-review, driver brief. Reports only: no article and no `todo.md` edit. The driver mints the tasks.

## Why This Wing

The three pages each take a different side of one question: how one mind stands to another. One page treats the metaphysics, one the evidence, and one the historical attempt to dissolve the question by semantics. All three are cut off from each other, and two of them are cut off from the hub they presuppose.

**Selection method.**

1. **Excluded pages edited today.** I took every page in `topics/`, `concepts/`, `voids/`, `apex/`, `positions/` and `tenets/` touched since `2026-11-26T00:00:00+00:00`. That is 20 pages, among them `tenets/tenets.md`, `positions/quantum-interface`, `positions/thought-and-understanding`, `concepts/mine-ness`, `topics/consciousness-and-the-ownership-problem` and `voids/tenet-generated-voids`.
   - **Note for the driver**: the brief's `git log --since=2026-11-26` returns **nothing**. Git reads a bare date as that date at the *current time of day*, so at 13:47Z it meant 13:47Z. The command needs the explicit `T00:00:00+00:00`.
2. **Excluded pages with open tasks.** I excluded any page named in an open task, using `parse_tasks` (558 active tasks) and a grep of the open part of `todo.md` above `## Completed Tasks` (L7508).
3. **Ranked the rest.** I ranked the remaining pages by their total review-file mentions and their last optimistic-review mention.

The lowest-covered page left was `topics/subjective-facts-and-the-metaphysical-problem-of-other-minds`. It has 7 review-file mentions in all, the lowest of any page with no open task. Its last optimistic mention was 10-16, and that was a one-line pointer. Its two natural siblings also have no open tasks, and neither has been an optimistic review's subject since September or October.

| abbrev | page | analyze_length | hard | headroom (hard−1−count) | review files mentioning | last optimistic mention | last deep review | open tasks naming it |
|---|---|---|---|---|---|---|---|---|
| SF | `obsidian/topics/subjective-facts-and-the-metaphysical-problem-of-other-minds.md` | **3,387** | 4,000 | **612** | 7 | 10-16 (pointer only) | 2026-10-16 | 0 |
| SP | `obsidian/topics/the-second-person-evidential-channel.md` | **2,736** | 4,000 | **1,263** | 9 | 09-23 (`intersubjective-wing`) | 2026-09-14 | 0 |
| LB | `obsidian/concepts/logical-behaviourism.md` | **2,607** | 3,500 | **892** | 13 | 10-22 (`two-senses-wing`, L52 only) | 2026-09-18 | 0 (3 grep hits, all inside the agentic-social NEEDS-HUMAN notes at todo L578–582) |

These lengths come from `tools.curate.length.analyze_length`. That count is body only, and the gate is `>=`. I measured at 14:00Z at HEAD `fbe8c231a8`.

**Content reviewed**: all three pages, read in full on disk. For context I also read:

- the latest deep review of each page, including its Remaining Items and Stability Notes;
- `voids/voids-between-minds` L97–106;
- `concepts/problem-of-other-minds` L76–80;
- `topics/philosophy-of-action-under-dualism` L63–69.

**Section caps (driver's figures)**: concepts 370/370 and topics 370/370 are full, and voids is 124/125. No new article can be acted on, so every opportunity below is either a fold into a page with headroom or a research subject.

## Executive Summary

The wing's strength is calibration under pressure. SF shows the Map that its primitive "I" puts it on the inegalitarian side of Merlo's question, and that Tenet 4's indexical argument depends on keeping that fact. It calls this "a verdict about the Map's own dependency structure, not a refutation of either side". SP separates an established method (second-person neuroscience) from a hypothesis (second-person evidence). It names the experiment that would tell them apart, and it does not pretend that experiment has been run. LB turns behaviourism's own defeaters into the dualist's argument, and it concedes what Ryle got right.

The weakness is connection. None of the three pages links to the other two, and LB never links the other-minds hub its second motivation depends on. Two neighbouring pages state as fact what this wing holds open:

- `voids/voids-between-minds` L99 asserts the irreducible second-person knowledge that SP treats as a hypothesis.
- LB L78 ranks Ryle's charge "the most-cited objection to interactionist dualism". The Map's own history page calls Elisabeth's 1643 question "The defining objection", and the Map's objections catalogue never names Ryle.

The best uncovered subject is **Ryle's regress against volitions**. The Map explicitly chose a volitionist theory of action and has never stated the oldest objection to volitions.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

Chalmers would value most that SF does not let the dualist off the hook. L64 records that Hellie's "Against Egalitarianism" names Chalmers's *dualist* system as its target: "The branch is not only the physicalist's" (count 1, L64). The vertiginous question is shown to bite dualists and physicalists alike, which is the honest place to start.

LB gives the cleanest version of the residue argument on the Map. L80 says the X-world super-super-spartan leaves "a state (felt pain) that persists with the behaviour and the disposition both removed". It then credits the sharper residue cases to the successors' critics: "The sharpest versions of this residue objection" (count 1, L66) belong to Nagel 1974 and Block 1978. LB L84 draws the line Chalmers himself draws: "The Map's dualism is a claim about the irreducibility of *phenomenal character*, not a defence of a Cartesian inner mechanism." (count 1, L84).

### The Quantum Mind Theorist (Stapp)

There is little physics in this wing, and Stapp would praise its restraint rather than its reach. SF's Tenet 4 entry says something a single-world quantum ontology needs said: standpoint pluralism "multiplies stacks of facts about one history, not histories" (count 1, L108). Perspectival plurality therefore does not reopen many worlds.

SF's Bidirectional Interaction entry is the wing's most original physics-facing move. Because each subject is paired with one physical channel, "the census of standpoints belongs to the physical state description rather than floating free as a stack of fact-sets" (count 1, L118). Here the Map's interface does metaphysical work that the egalitarian does not need, and SF marks it honestly as "still owed with the law".

SP's Tenet 3 paragraph declines to claim that inter-brain synchrony shows the mind acting on the brain: "nothing in reciprocal timing or inter-brain synchrony discriminates "phenomenal state causes expression" from "correlate causes expression."" (count 1, L69). Stapp would want more, but he would accept that this is the correct ceiling.

### The Phenomenologist (Nagel)

SF opens on Nagel's own ground. Nagel's *View from Nowhere* "objective self" is the ancestor of the "which subject is this one" fact that SF prices. Nagel would praise the lede's three-problem split. The metaphysical problem asks whether reality would "single out one point of view" (count 1 for "or does reality single out one point of view", L36), and it is kept distinct from the epistemological and conceptual problems.

He would also praise the Kinkaid section, which sets one phenomenology against another instead of a theory against a phenomenology: "If the other is given *as* a centre, the exercise that found feltness only in my own case has misdescribed its data." (count 1, L96).

SP's conclusion reads as Nagelian in a good way. Even at its fullest, engagement "is evidence about coupling and responsiveness, and no window into another's interior" (count 1, L77).

### The Process Philosopher (Whitehead)

Whitehead would find a natural ally in SF's treatment of perspective as a feature of *reality* rather than of psychology. In standpoint pluralism "the world itself differs between subjects" (L74), and each subject is a standpoint relative to which it is the centre. That is close to Whitehead's own perspectival ontology.

In SP he would side with the enactivist "constitutive" reading that the Map declines. But he would praise the honesty of how the Map marks the refusal: "The Map treats this as a case of taking method without ontology; the enactivist would deny that the two come apart." (count 1, L71).

No tier-upgrade is at stake anywhere in the wing. No organism or system is placed on the evidential scale.

### The Libertarian Free Will Defender (Kane)

SP gives Kane a concrete picture of agents answerable to one another. Turn-taking gaps far shorter than word-production latency suggest "*predictive coupling* — each partner modelling and anticipating the other" (count 1 for "predictive coupling", L47). And "A spectator watching a recording cannot exhibit it, because there is no one to predict them back." (count 1, L47).

LB's knowing-how concession (L46, L84) is the right shape for an agent-causal view: competence is displayed in conduct, and it is not a silent inner recitation. Kane would ask for more, and the wing does not give it. Ryle's chapter on the will is the sharpest attack ever made on volitions, the mental acts of willing that cause bodily movements. LB, the Map's Ryle page, never states that attack. Neither does the page where the Map chose volitionism (see Uncovered Subject 1).

### The Mysterian (McGinn)

SF refuses to settle what an abstract cannot settle. Of Lipman's chapter 12 it says "an abstract cannot settle it. The debate is open" (count 2: L90 body, plus the L9 frontmatter exemption note that quotes it). SF L102 frames the Map's dependencies as "a dependency the preceding sections create, not an instruction" (count 1, "Each entry below is a dependency the preceding sections create, not an instruction.").

SP ends on the thing McGinn would want ended on: "For the Map, that remaining distance is the point." (count 1, L77).

### The Hardline Empiricist (Birch)

Birch's verdict decides how this review should be read, and it is mostly praise.

**SP is a model of evidential-status discipline.**
- The lede assigns the tiers up front: "established in the first sense, a hypothesis in the second" (count 1, L29).
- It disarms the synchrony artifact with Burgess's pseudo-pairs: "The existence of a dyad-level observable does not certify what it observes." (count 1, L57).
- It names its own missing test: "until a design separates being responded to from taking oneself to be, the irreducibility hypothesis lacks its discriminating test, and this article does not pretend otherwise" (count 1, L61).

This is "tenet-coherent, not evidence-elevating" done in full. Tenet 3 receives consistency only, and the inference to ontological difference is credited to another page rather than restated.

**SF refuses to recruit.** "None of these authors is enlisted for Tenet 1." (count 1, L116). On Tenet 5 it says "Tenet 5 forbids trading them on simplicity alone" (count 1, inside the L120 sentence).

**LB is the weakest of the three on this axis, and the weakness is narrow.** Its argument is sound, but two superlatives are rankings the Map's own pages contradict:
- L78: "Ryle's category-mistake charge remains the most-cited objection to interactionist dualism" (count 1).
- L30: "the source of the single most durable objection to dualism" (count 1).

Against these, `topics/history-of-the-interaction-problem` L47 says "The defining objection arrived in 1643" (count 1), and `concepts/objections-to-interactionism` contains no "Ryle" at all (`grep -ciF ryle` = 0). Both fixes cost one word each (Priority 2).

**Calibration concern (not praise).** `voids/voids-between-minds` L99 is not in the wing, but it is the hub SP's conclusion points toward. It states flatly that in encounter "something passes between them that cannot be captured by introspection alone or by external observation" (count 1). It adds "The encounter grants a form of knowledge available nowhere else" (count 1).

SP holds the first half of that as false for the measurable signal: "Dyadic contingency is third-person-measurable" (count 1, L51). It holds the rest as open: "that claim is worth stating precisely and holding as a hypothesis rather than a result" (count 1, L61).

So the Process-friendly "between" is asserted on the void page and held open on the specialist page. This is the slippage the two personas exist to catch. It goes to the priority list as a `refine-draft` (Priority 4), not as a strength.

**Process/Empiricist verdict**: the two personas converge inside the wing, praising the same passages (SP L71, SF L116) for different reasons. They conflict only at the void hub, and that conflict is flagged.

## Content Strengths

### `obsidian/topics/subjective-facts-and-the-metaphysical-problem-of-other-minds.md`

- **Strongest point**: the five-exit decision tree (L64–68), followed by the terminological correction that rescues it.
- **Notable quote**: "So there are two egalitarianisms: the deflationist's rejects first-person realism, the fragmentalist's is a form of it, and only the first denies subjective facts." (count 1, L70)
- **Why it works**: the word "egalitarian" names two opposed views in this literature, and the page separates them before arguing. The cost to Tenet 4 then becomes exact. The egalitarian's dissolution of "why am I this subject?" "is available word for word to the Everettian for "why am I this branch?"" (count 1, L108).
- **Also strong**: the Occam entry prices both rivals in their own currency: "Fragmentalism is extravagant in one currency (stacks of facts), the Map's primitive "I" in another (a fact simpliciter no description reaches); Tenet 5 forbids trading them on simplicity alone." (count 1, L120).

### `obsidian/topics/the-second-person-evidential-channel.md`

- **Strongest point**: the split between second-person *neuroscience*, which is established and widens the third-person channel, and second-person *evidence*, which is a hypothesis (L43). The split is then carried through to the conclusion without slipping.
- **Notable quote**: "Dyadic contingency is third-person-measurable — hyperscanning and turn-timing corpora record it from outside — but it is produced only under live coupling, so no recording of either party alone contains it and no introspective report can supply it" (fragments counted: "Dyadic contingency is third-person-measurable" 1; "so no recording of either party alone contains it and no introspective report can supply it" 1; L51).
- **Why it works**: it states exactly what is relational about the evidence and exactly what remains open. The Pfeiffer et al. (2014) believed-interactivity result is placed as a concession against the article's own strongest claim. The 09-14 stability notes mark this as deliberate, and it should stay.

### `obsidian/concepts/logical-behaviourism.md`

- **Strongest point**: the inversion in the site-perspective section. The objections that killed behaviourism from inside materialism are available to the dualist *a fortiori*. Then comes the reversal: "Ryle does not so much refute the ghost as decline to look for it." (count 1, L82). And: "Dispositionalism changes the subject." (count 1, L82).
- **Notable quote**: "Logical behaviourism did not fall to dualists." (count 1, L56). It is a five-word sentence that sets up the whole argument.
- **Why it works**: it keeps credit precise. Putnam's two cases are "Putnam's, and should be attributed to him alone" (count 1, L62, full sentence). The Hempel/Carnap calibration paragraph (L52) refuses the textbook simplification. And L74 declines to double-count, saying "What accumulates is that concession, not a tally of arguments" (count 1).

## Expansion Opportunities

Every item here is a fold into an existing page or a research subject. No new page can be created.

### High Priority

#### Ryle's regress against volitions, and the Map's volitionist choice

- **Builds on**: `topics/philosophy-of-action-under-dualism` L63, "## Volitionism: Trying as the Basic Act" (headroom 1,092; no open tasks). That page selects "a volitionist agent-causal hybrid" (description). It also builds on LB, the Map's only page on *The Concept of Mind* (headroom 892).
- **Would address**: Ryle's chapter on the will ("The Will", *The Concept of Mind* ch. 3) argues that volitions are a myth. Its sharpest step is a regress: if a volition is itself voluntary it needs a prior volition, and if it is not, the action it causes is not voluntary either. The Map posits the smallest possible act of trying at the interface, so this regress is aimed squarely at its own choice. Nine content pages discuss volitionism, and none of them names Ryle (see Uncovered Subjects).
- **Estimated scope**: research note, then about 250–400 words folded into philosophy-of-action §Volitionism, with a pointer from LB.
- **Tenet alignment**: Tenets 2 and 3. Hornsby's view that tryings are inseparable from their agent, which that page already uses, is one of the standard answers to the regress. The Map may already hold the reply without ever having stated the objection.

#### Strawson's "Persons" as an objection to Posit One

- **Builds on**: SF's Posit One entry (L106), and LB's lineage section (L70–74), which lists the successors to behaviourism but not Strawson's third way.
- **Would address**: Strawson argues that the concept of a person is primitive and that states of consciousness can be ascribed to oneself only if they can be ascribed to others. If he is right, the Cartesian ego is not a possible bearer of experience. That is a direct challenge to a "numerically determinate, persisting subject" posited prior to any physical criterion (SF L106).
- **Estimated scope**: research note first. The likeliest host is SF, as a short paragraph under "What Moves" (headroom 612).
- **Tenet alignment**: Tenet 1, through Posit One. This is an objection to engage, not a source of support.

### Medium Priority

#### Darwall's second-person standpoint beside the second-person channel

- **Builds on**: SP L73, which says "Being addressed as a "you" is evidence *to* you about another's responsiveness".
- **Would address**: second-personal *address*, in Darwall's sense of reasons that exist only between persons who can hold each other answerable, is the normative counterpart to second-person *evidence*. SP never distinguishes the two, and the distinction would keep the evidential claim from borrowing moral weight.
- **Estimated scope**: about 120 words in SP (headroom 1,263).
- **Note**: first suggested by `optimistic-2026-09-23-intersubjective-wing` L153. It is still at zero hits and was never minted.

#### Intellectualism about knowing-how

- **Builds on**: LB L46 ("This is the part of Ryle's project that survives its collapse, and the Map has no quarrel with it.", count 1) and LB L84 ("his account of *knowing how* as competence-in-conduct survives intact", count 1).
- **Would address**: Stanley & Williamson (2001) argue that knowing-how is a species of knowing-that, so Ryle's distinction is contested in its own right. The Map's reply does not depend on who wins that debate. "Survives intact" claims more than the Map needs (Lower-priority item 5).

### Ideas for Later

- **Valberg's horizonal subject.** It is the third inegalitarian exit beside Hare and Merlo. The Map mentions Valberg only inside a Merlo quotation (SF L60). Its host would be SF's L65 branch, because `concepts/egocentric-presentism` has 14 words of headroom.
- **Fine's external relativism developed.** SF L84 says "The Map's corpus names only the fragmentalist route; it should know the relativist one exists." (count 1). The research note `research/fragmentalism-and-standpoint-pluralism-2026-10-14.md` already covers it, so the gap is a host. A fragmentalism concept page is the natural home if a slot ever opens (see New Concept Pages).
- **The other-minds half of Jackson's 1982 reply**, suggested for SF by `optimistic-2026-10-16-self-stultification-repair-wing` L183. It is still unused (`grep -ciF jackson` SF = 0).
- **Wittgenstein's private-language argument behind logical behaviourism.** First noted by `optimistic-2026-08-03-physicalist-rivals-cluster` L175. LB still has no "Wittgenstein" (count 0). `concepts/problem-of-other-minds` L76–80 covers the dissolution, so a pointer would do (see Cross-Linking).

## Uncovered Subjects

Each count below is the number of **files** matching a case-insensitive fixed-string grep. "Content" means `topics concepts voids apex positions tenets arguments`, and "research" means `research/`. Each subject has a positive control showing that the grep can find neighbouring material.

1. **Ryle's regress against volitions ("The Will", *The Concept of Mind* ch. 3, 1949) and the Map's volitionist theory of action.**
   - Zero hits: "regress of volitions" 0/0; "myth of volitions" 0/0; "volitional regress" 0/0; "volition regress" 0/0.
   - Nine content pages match `volitionis`, and all nine have `grep -ciF ryle` = 0. Of the five content pages that name Ryle, none mentions volition (`grep -ciE volition` = 0 for each).
   - Positive control: "volitionism" 6/4; "Concept of Mind" 2/9; "Hornsby" 2/3.
   - Landing: `topics/philosophy-of-action-under-dualism` §Volitionism (headroom 1,092).
2. **Strawson's "Persons" (1958; *Individuals* ch. 3, 1959) and the conceptual problem of other minds (Avramides, *Other Minds*, 2001).** Strawson's topics are P-predicates, the primitive concept of a person, and the claim that self-ascription requires other-ascription.
   - Zero hits: "P-predicate" 0/0; "M-predicate" 0/0; "primitive concept of a person" 0/0; "Avramides" 0/0; "conceptual problem of other minds" 0/0.
   - Near-miss: `research/problem-of-other-minds-2026-01-14.md` L113 lists "P.F. Strawson" once among proponents of the Wittgensteinian dissolution, with no argument given.
   - Positive control: "Individuals: An Essay" 2/2. The book *is* cited, but for sounds (`topics/auditory-consciousness-and-the-interface` L107) and categorial voids (`voids/conceptual-scheme-void` L162), not for persons. The heading "### Wittgensteinian Dissolution" appears once, in `concepts/problem-of-other-minds` L76.
   - Metadata: from memory, so a lead. Crossref returned only the 2025 Routledge reissue of *Individuals*, and its query for Avramides failed.
3. **Intellectualism about knowing-how (Stanley & Williamson 2001) against Ryle.**
   - Zero hits: "Stanley & Williamson" 0/1 (the one research hit is a "verify if used" bullet in `research/philosophy-of-habit-under-dualism-2026-07-07.md` L206); "Stanley and Williamson" 0/0; "knowledge-how" 0/3 (passing bullets in three void notes).
   - Positive control: "knowing how" 7/13.
   - Metadata **verified at Crossref**: *Journal of Philosophy* 98(8): 411–444, DOI 10.2307/2678403.
4. **Darwall's second-person standpoint (2006): second-personal reasons, address and accountability.**
   - Zero hits: "Darwall" 0/0; "second-person standpoint" 0/0; "second-personal" 0/3 (the research hits use the word in other senses, e.g. "second-personal acquaintance" in `research/voids-intersubjective-void-2026-02-01.md` L147).
   - Positive control: "second-person" 25/16.
   - Repeat submission: listed by `optimistic-2026-09-23-intersubjective-wing` L153 and still absent from `../unfinishablemap_log/research-harvest-state.json`, which contains no "Darwall".
   - Metadata: lead. Crossref holds Harvard UP digital-edition DOIs dated 2009 (10.4159/9780674253636); the print original is 2006.
5. **Valberg's horizonal subject (*Dream, Death, and the Self*, 2007): the third inegalitarian first-person realism.**
   - Near-zero hits: "Valberg" 1/2 (the only content hit is inside the Merlo quotation at SF L60; the research hits are name-drops in `egocentric-presentism-2026-06-17` L58 and the subjective-facts research note L74); "personal horizon" 0/1.
   - Positive control: "Hare 2009" 2/2. Hare is the other inegalitarian, and he has a page (`concepts/egocentric-presentism`).
   - Metadata at Crossref: Princeton UP 2007, DOI 10.1515/9780691190181.

**Checked and excluded** (these looked uncovered, but are covered):
- *Direct social perception*: a case-sensitive grep returned 0, but `concepts/empathy` L75 "### Zahavi: Direct Social Perception, and Beyond Empathy" covers it.
- *Fragmentalism and external relativism*: covered by the research note `fragmentalism-and-standpoint-pluralism-2026-10-14`.
- *Schwitzgebel's phenomenal-dispositional account of belief*: covered by the research note `voids-dormancy-void-2026-09-17` L59.

## Cross-Linking Suggestions

Baseline counts are `grep -cF` of the target slug in the host, taken before any change.

| From | To | Reason | Baseline |
|---|---|---|---|
| SP L77 "remaining distance" | `voids-between-minds#encounter-the-second-person-void` | Both build on Schilbach et al. 2013, and they have zero edges between them. Priority 1. | 0 |
| `voids-between-minds` L99 | SP | The hub states what SP holds as a hypothesis. Priority 4. | 0 |
| LB L38 "other minds" | `problem-of-other-minds` | LB's second motivation is the other-minds problem, and the page never links it. Priority 2. | 0 |
| SF L36 "epistemological one" | `problem-of-other-minds` | The lede names the problem it presupposes, and its only link to it is in Further Reading. Priority 3. | 0 in body (fm L16, Further Reading L126) |
| SF L96 | SP | Kinkaid's counter-datum and Reddy's engaged stance are rival phenomenologies of the other, and SP underwrites only the weaker one. Priority 3. | 0 |
| `problem-of-other-minds` L80 "quasi-behaviorist" | LB | The dissolution section names behaviourism without linking it. Lower-priority 7. | 0 |
| LB | `language-and-consciousness` (Wittgenstein) | Covers the private-language gap noted 08-03. Lower priority, no task. | 0 |

## New Concept Pages Needed

None can be created while concepts is at 370/370. If a slot opens, the strongest candidate is **`concepts/fragmentalism`**. It was named as owed by `deep-review-2026-10-16-subjective-facts…` (Stability Notes, "a future `concepts/fragmentalism` page"), a research note already exists, and three content pages name the view without a home.

## Priority list for the driver

There are four items, and each fits its host's measured headroom. Every OLD string was checked with `grep -cF` on the live file; each returned 1 unless stated. Word costs were computed with `tools.curate.length.count_words` on the old and new strings.

### 1. SP L77: link the channel's remainder to the encounter void (+0)

- **Host**: `obsidian/topics/the-second-person-evidential-channel.md`. analyze_length **2,736**, hard **4,000**, headroom **1,263**.
- **OLD** (L77, count 1): `For the Map, that remaining distance is the point.`
- **NEW**: `For the Map, that [[voids-between-minds#encounter-the-second-person-void|remaining distance]] is the point.`
- **Word cost**: +0.
- **Checks**:
  - The anchor exists in the built page. `hugo/public/voids/voids-between-minds/index.html` (built 02:28Z today) has `<h2 id=encounter-the-second-person-void>`, and `heading_anchor_slug` returns the same slug.
  - The baselines are `grep -cF "[[voids-between-minds"` SP = 0 and `grep -cF the-second-person-evidential-channel` in `voids/voids-between-minds.md` = 0.
- **Why**: the two pages share Schilbach et al. 2013 (SP reference 1; voids-between-minds L105 and reference 8) and have zero edges either way. SP's last sentence names exactly the remainder the void page describes.
- **Stability**: the 09-14 notes ask that the next review be prompted by substantive change, not a cross-link bump. This edit is a link only, and it should not trigger a re-review of SP.
- **Type**: refine-draft.

### 2. LB L78 and L30: drop two superlatives the Map contradicts, and link L38 to the other-minds hub (+2)

- **Host**: `obsidian/concepts/logical-behaviourism.md`. analyze_length **2,607**, hard **3,500**, headroom **892**.
- **(a) OLD** (L78, count 1): `Ryle's category-mistake charge remains the most-cited objection to interactionist dualism`
  **NEW**: `Ryle's category-mistake charge remains among the most-cited objections to interactionist dualism`
  **Cost**: +1.
- **(b) OLD** (L30, count 1): `It is the source of the single most durable objection to dualism`
  **NEW**: `It is the source of one of the most durable objections to dualism`
  **Cost**: +1.
- **(c) OLD** (L38, count 1): `The second was the problem of *other minds and public language*`
  **NEW**: `The second was the problem of *[[problem-of-other-minds|other minds]] and public language*`
  **Cost**: +0. The baseline `grep -cF "[[problem-of-other-minds"` LB = 0. Wikilinks inside italics are normal in the corpus (446 files).
- **Total**: +2.
- **Evidence for (a) and (b)**:
  - This page's own topics-frontmatter host, `topics/history-of-the-interaction-problem`, says at L47 "The defining objection arrived in 1643" (count 1). That is Elisabeth, 306 years before *The Concept of Mind*.
  - `concepts/objections-to-interactionism` never names Ryle (`grep -ciF ryle` = 0).
  - Ranking Ryle first is an empirical claim with no source, and the Map's own catalogue and history disagree with it.
- **Stability (09-18)**: the X-world paragraph, the perfect-actor/absent-qualia mapping, and the knowing-how concession are untouched.
- **Type**: refine-draft.

### 3. SF L96 and L36: tie the counter-datum to the second-person channel, and link the lede to the hub (+26)

- **Host**: `obsidian/topics/subjective-facts-and-the-metaphysical-problem-of-other-minds.md`. analyze_length **3,387**, hard **4,000**, headroom **612**.
- **(a) OLD** (L36, count 1): `distinct from the epistemological one (how do I know you are conscious?)`
  **NEW**: `distinct from the [[problem-of-other-minds|epistemological one]] (how do I know you are conscious?)`
  **Cost**: +0. The body has no link to the hub; it appears only in frontmatter L16 and Further Reading L126.
- **(b) OLD** (L96, count 1): `If the other is given *as* a centre, the exercise that found feltness only in my own case has misdescribed its data.`
  **NEW**: the same sentence, followed by: `The Map's [[the-second-person-evidential-channel|second-person channel]] reaches only a weaker datum of the same family: the other given as a responder, not as a second centre of feltness.`
  **Cost**: +26. The baseline `grep -cF the-second-person-evidential-channel` SF = 0.
- **Grounding**: the new sentence states only what SP itself says. SP L45 has "what engagement discloses is the other as a responder" (count 1). SP L77 has "Even then it is evidence about coupling and responsiveness, and no window into another's interior." (count 1). It quotes no outside source, so the 10-14/10-16 quote ledger is unaffected.
- **Why**: Kinkaid's datum is "another perspective with its own 'mineness'" (L96). SP underwrites only "the other as a responder". Saying which of the two the Map's own evidence reaches stops a reader from taking SP as support for Kinkaid's stronger claim.
- **Stability (10-16)**: this edit neither re-flags the open privileged-fragment fork nor calls Lipman "unrefuted".
- **Type**: refine-draft.

### 4. `voids/voids-between-minds` L99: import the dedicated page's hypothesis status (+2, coordinate)

- **Host**: `obsidian/voids/voids-between-minds.md`. analyze_length **2,995**, hard **3,000**, headroom **4**.
- **(a) OLD** (L99, count 1): `something passes between them that cannot be captured by introspection alone or by external observation`
  **NEW**: `something passes between them that may not be capturable by introspection alone or by external observation`
  **Cost**: +1.
- **(b) OLD** (L99, count 1): `The encounter grants a form of knowledge available nowhere else, yet that knowledge is permanently incomplete.`
  **NEW**: `The encounter may grant a form of [[the-second-person-evidential-channel|knowledge available nowhere else]], yet that knowledge is permanently incomplete.`
  **Cost**: +1.
- **Total**: +2, giving 2,997 after the edit.
- **Why**: SP holds the measurable part of the claim as third-person accessible ("Dyadic contingency is third-person-measurable", count 1, L51). It holds the rest as open ("that claim is worth stating precisely and holding as a hypothesis rather than a result", count 1, L61). The void hub asserts both.
- **Coordination**:
  - The open P3 cross-review of `voids/chroma-void` (todo L4396, parse_tasks index 4395) lists this page as a neighbour host and measured its headroom at 6. It is now 4, and this item leaves 2, so that task's edit here must be a 0-word piped link.
  - If headroom is gone at execution time, keep "grants", install only the link in (b) (+0), and drop (a).
  - Do not touch L105 in this pass (Lower-priority item 8).
- **Type**: refine-draft.

### Lower-priority list (beyond the four)

5. **LB L84 knowing-how calibration (+28 including the reference).**
   - OLD (count 1): `his account of *knowing how* as competence-in-conduct survives intact`
   - NEW: `his account of *knowing how* as competence-in-conduct survives the collapse, though intellectualists (Stanley & Williamson 2001) contest it on independent grounds` (+12).
   - Add the reference: `11. Stanley, Jason, and Timothy Williamson. "Knowing How." *Journal of Philosophy* 98, no. 8 (2001): 411–444. https://doi.org/10.2307/2678403` (+16). Metadata was verified at Crossref.
   - If both this item and Priority 2 are taken, combined LB headroom after both is 862.
6. **SF L92 Madhyamaka clause (+14).** This is the Remaining Item that `deep-review-2026-10-16` deferred.
   - OLD (count 1): `Whether a dissolution is an answer is where the Map and Lipman part.`
   - NEW: `Whether a dissolution is an answer is where the Map and Lipman part, as it parts from the [[buddhism-and-dualism|Madhyamaka]] no-self dissolution, which the tenets record as bedrock.`
   - Grounding: `tenets/tenets.md` L121 still reads "A deflationary route stays open at the framework boundary: the Madhyamaka no-self analysis ([[buddhism-and-dualism]], …)". tenets.md was edited today, but its L71, not L121; re-grep L121 before editing.
   - If Priority 3 is also taken, combined SF headroom after both is 572.
7. **`concepts/problem-of-other-minds` L80: a 0-word link to LB.**
   - OLD (count 1): `a quasi-behaviorist conclusion the Map rejects` → NEW `a [[logical-behaviourism|quasi-behaviorist]] conclusion the Map rejects`.
   - The host has 27 words of headroom (3,472/3,500) and an open task, todo heading L5184 (parse_tasks index 5183), that plans +7 at L198. Fold this link into that task's run rather than minting a separate one.
8. **`voids/voids-between-minds` L105 Schilbach "transformation gap" (LEAD, unverified).**
   - The clause "so I cannot observe what you are like independently of our meeting" (count 1 within the L105 string) reads as the research note's own inference. Its source is `research/voids-second-person-void-2026-03-28.md` L120, which says "This means I cannot observe…".
   - The page attributes the clause to Schilbach et al. 2013. The note's quoted phrase at L85 ("a complex dynamical system that is self-organized and takes on a life of its own") was not checked against the BBS text here.
   - Verify at source before any edit. The host has no headroom after Priority 4.
9. **`arguments/functionalism-argument` → LB reciprocal**, owed since `deep-review-2026-09-18` Remaining Items. It is still absent (count 0). The host is at 3,496/3,500 (headroom 3) and has no behaviourism phrase to pipe (`grep -ciE behavio` hits only role descriptions at L39, L59 and L121). This needs a length decision and should not be minted as a refine.
10. **A positions-register entry for "second-person evidence as a candidate third channel"**, owed since `pessimistic-2026-09-14`. `grep -rliE "second.person" obsidian/positions/` returns 0. This is a positions-evolve item if the driver wants it.
