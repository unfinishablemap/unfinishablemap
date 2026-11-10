---
title: "Research Notes - Imperativism and Evaluativism About Pain"
created: 2026-11-10
modified: 2026-11-10
human_modified: null
ai_modified: 2026-11-10T12:20:29+00:00
draft: false
description: "The representational theories of pain's unpleasantness predict asymbolia instead of suffering it, so the corpus's claim that asymbolia settles the hedonic-evaluativist dispute fails. Fold into concepts/valence and concepts/pain-asymbolia."
topics:
  - "[[pain-consciousness-and-causal-power]]"
concepts:
  - "[[pain-asymbolia]]"
  - "[[valence]]"
related_articles:
  - "[[emotion-and-dualism]]"
  - "[[minds-without-words]]"
  - "[[valence-as-a-natural-kind]]"
  - "[[constructed-emotion-and-valence-as-a-natural-kind-2026-09-05]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-10
last_curated: null
last_deep_review: null
recommended_action: fold
target_section: concepts
target_slug: valence
---

# Research: Imperativism and Evaluativism About Pain

**Date**: 2026-11-10
**Originating task**: P3 `research-topic` (todo L40), minted 2026-11-10 04:53Z by `/harvest-research-subjects` from the two 2026-11-10 outer reviews of [[pain-consciousness-and-causal-power]] (`reviews/outer-review-2026-11-10-claude-fable-5-2.md` §2.3 "Theory by Theory" and §4 item 8; `reviews/outer-review-2026-11-10-chatgpt-5-6-sol-pro.md` §2 "Klein's imperative theory" and §4 "Representationalism").
**Measured at write time** (2026-11-10 ~12:05Z, by `tools.evolution.state.count_section_files`): topics 369 against the 370 cap, the last slot already claimed by two open P3 expand tasks; concepts 370/370 (full). Host lengths by `tools.curate.length.analyze_length` (gate `>=`): `concepts/valence` 1,932 (hard 3,500); `concepts/pain-asymbolia` 2,968 (hard 3,500); `topics/pain-consciousness-and-causal-power` 3,982 (hard 4,000); `topics/emotion-and-dualism` 3,404 (hard 4,000); `apex/minds-without-words` 4,141 (hard 5,000); `concepts/evaluative-phenomenal-character` 3,490 (hard 3,500).
**Builds on**: [[constructed-emotion-and-valence-as-a-natural-kind-2026-09-05]], which covers imperativism about *valence in general* (Barlassina & Hayward 2019; Kauppinen 2021), Carruthers's unity thesis, and Corns (2014) on "motivational oomph". Nothing there is re-run. This note covers the *pain-specific* debate and what each theory predicts for asymbolia.
**Search and retrieval**: Crossref DOI and bibliographic lookups; OpenAlex abstracts (inverted index) and title search; Semantic Scholar (no abstracts returned); Glasgow Enlighten (Bain 2013 abstract). Full texts saved and read with `python -I`/`pdftotext`: SEP "Pain" (Aydede, substantive revision 4 March 2019, HTML); Martínez (2023), Klein & Duval (2023), Aydede (2023) from the open-access *Belgrade Philosophical Annual* 36(2) Grahek issue; Noordhof (2021) from White Rose (CC BY); Barlassina & Hayward (2019) author preprint from White Rose; Duval & Klein (2025) from the Cambridge Core open-access HTML; Fulkerson's NDPR review (2016.03.05) of *What the Body Commands*. Bot-walled (Cloudflare or 403): PhilArchive, PhilPapers, Springer, Wiley, Philosophy of Brains. WebSearch (standard) ×4.
**Sources consulted**: 33 (listed under [Citations](#citations); 8 read in full, 17 at abstract level, the rest at metadata level).

**Evidence grades** (the convention of the 2026-09-05 note):
- **[raw]**: full text saved this session and the quoted string grep-verified in it. SEP "Pain"; Martínez 2023; Klein & Duval 2023; Aydede 2023; Noordhof 2021; Barlassina & Hayward 2019 (preprint, so page numbers are not the *Mind* pagination); Duval & Klein 2025; Fulkerson 2016 (NDPR).
- **[raw, quoted]**: a string verified in a raw source that is itself *quoting* the work named. Grahek 2007 pp. 76 and 80 (quoted by Martínez 2023); Klein 2015 *Mind* p. 498 (quoted by Klein & Duval 2023, Klein's own later paper); Klein 2015 book pp. 46–7, 48, 56 (quoted by Fulkerson 2016); Bain 2013 p. S82 and Hall 2008 p. 534 (quoted by the SEP). Do not put these in an article as direct quotations of the original without checking the original first.
- **[abstract]**: publisher or OpenAlex abstract, verbatim. Klein 2015 *Mind*; Bain 2011, 2013, 2014, 2019; Jacobson 2013; Cutter & Tye 2014; Hall 2008; Grahek 2007 (MIT Press blurb); Corns 2014; Gray 2018; Mitchell 2025; Kinakin 2026; Klein 2010; Coninx 2020; Barlassina 2020; Klein 2015 book (MIT Press description via Crossref).
- **[metadata]**: the record was confirmed at Crossref, OpenAlex or the SEP bibliography, but nothing beyond it was read. Klein 2007; Martínez 2011; Cutter & Tye 2011; Martínez & Klein 2016; Carruthers 2023; Tye 2005; Helm 2002; Nelkin 1994; the Klein 2015 book's chapter list.

## Executive Summary

The outer reviewers are right that the pain page's red-square argument misses its targets, and the gap is wider than they said. **Three live pages, at five loci, claim that pain asymbolia decides the hedonic-versus-evaluativist dispute** in the hedonic account's favour: [[valence]] L53 ("provides the strongest evidence"), [[emotion-and-dualism]] L79 ("reveal which account is correct") and L83 ("does more than settle the hedonic-evaluativist debate"), and [[minds-without-words]] L111 ("**Pain asymbolia settles this specific dispute**") and L137. That argument is Grahek's. He argued that asymbolic pain "does not represent for them any damage or potential damage to their bodies", as the smiling and laughing in testing shows (Grahek 2007, p. 80, [raw, quoted] by Martínez 2023). The field's answer is on record: **both representational families predict the dissociation.** Evaluativism (the label is David Bain's) says an unpleasant pain represents a bodily disturbance *and represents it as bad for the subject*. Bain (2014) argues that asymbolia "reveals not only that unpleasant pain is composite, but that its ‘hedomotive component’ is evaluative" [abstract]: asymbolics represent the damage but not as bad for them, because, on Klein's reading, they have "lost a general capacity to care about their bodily integrity" (Klein 2015 *Mind* [abstract]). Hybrid imperativism (Martínez 2011) gives pain a descriptive component and an imperative one, so "we should expect the familiar asymbolic pattern of sensory pain without painfulness" (Martínez 2023 [raw]). The corpus premise that asymbolics "retain the capacity to represent tissue damage as harmful" (emotion-and-dualism L79) is exactly what both rivals deny. Klein's own gloss is that asymbolics "can no longer conceive of why such events are bad" (Klein 2015 *Mind* p. 498 [raw, quoted]).

**Three findings matter for the fold.** (1) **"Differing in whether it hurts *is* differing in content" holds for Martínez, Bain, Cutter & Tye, Barlassina & Hayward and Noordhof, but not for Klein's book.** In *What the Body Commands* Klein holds that "suffering is not a feature of pain: it is a response to pain", so that "pains only contingently hurt and feel bad" (pp. 46–7), and he admits "I have no theory of suffering, no story about what sort of state is present when pains feel bad" (p. 56) (both [raw, quoted] by Fulkerson 2016). The SEP summarises his unpleasantness as "second-order agential level commands directed at the pain's imperative content" [raw]. The Fable review's sentence pairs "imperativism (Klein; Martínez 2011)" with "differing in whether it hurts IS differing in content". For Klein that is wrong. The open P1 on the pain page (todo L5139 (d)) must cite Martínez (2011), Bain (2013) or Cutter & Tye (2011) for hurt-as-content, and Klein only for motivational force. (2) **The hedonic account's best argument is the one the corpus never uses.** It is the rationality of painkillers, the "messenger-shooting" objection (Jacobson 2013 [abstract]): if unpleasantness were only a representation of damage, killing the pain while the damage remains would be "shooting the messenger". The objection is contested (Cutter & Tye 2014; Bain 2019) and still live (Kinakin 2026, *Phil Studies* 183(6) [abstract]: "intentionalism about painfulness is incompatible with the sort of painkiller-taking behaviour characteristic of being in painful pain"). `messenger` has no live hit in this sense, and `painkiller` appears only in the analogous argument against illusionism (`topics/phenomenal-value-realism` L193, "Illusionists take painkillers"). (3) **Representationalism is not physicalism.** Aydede (2023 [raw]) divides strong representationalism into reductive-realist and non-reductive-irrealist versions, and the latter hold that phenomenal content "cannot be explained in purely non-representational, non-mental, or more broadly, naturalistic/physicalistic terms". The hedonic-versus-representational question is therefore orthogonal to Tenet 1. The Map can lose it without losing dualism, and winning it would not evidence dualism.

**For the inseparability claim** (pain page L134–142): imperativism and Noordhof's response-dependence build motivational force into pain's content or its painfulness. Inseparability is a *shared* commitment with these physicalist-compatible rivals, so it cannot discriminate dualism from them. Grahek, whom the page recruits, held the opposite of inseparability for the sensory component: its "pure juice or essence … [turns] out to be a blunt, fleshless, inert sensation … powerless to move the body and mind in any way" (Grahek 2007, p. 76 [raw, quoted]). Corns (2014 [abstract]) argues that "Unpleasantness and motivational oomph doubly dissociate". **None of these views concedes epiphenomenalism.** Every one of them assigns pain's (un)pleasantness a motivating or reason-giving role. What they dispute is what the felt badness *is*, not whether it does any work.

**Verdict: fold, not article.** The yield for the Map is one correction (asymbolia does not settle the dispute) and one missing comparator (imperativism), and `concepts/valence` has 1,568 words of headroom to carry both. A standalone topics article would be mostly background on physicalist theories, which the style guide says to skip. The topics cap is also exhausted. See [Recommended Fold](#fold).

## Corpus Baseline

- `imperativis`: 0 live articles. The 2 research hits are the 2026-09-05 note and one other. `motivationalis`: 0 live. `What the Body Commands`: 1 live (the pain page's References L217, body-uncited). `Klein (2015)`: 1 live, the *Mind* paper on [[pain-asymbolia]] L73.
- **Evaluativism** appears only as Carruthers's (2018) account of *valence*: [[valence]] L49; [[emotion-and-dualism]] L73–79 (anchor `{#hedonic-vs-evaluativist}`); [[minds-without-words]] L111; [[valence-as-a-natural-kind]] L98 (Further-Reading gloss "the hedonic and evaluativist accounts"). `Bain (20`, `Bain, D`, `Cutter` (in the pain sense), `Martínez` (in the pain sense), `Jacobson`, `Aydede`, `Barlassina`, `Hall (2008` have 0 live hits. (`Cutter` has 16 live hits, all Brian Cutter on Russellian monism, AI ensoulment or psychophysical harmony.)
- [[pain-asymbolia]] already carries Klein (2015 *Mind*), Gerrans (2020, 2024), Griffith & Kind (2024) and Duval & Klein (2025). So its "What Asymbolia Dissociates" section needs only the content-side reading, not the lost-care reading.
- The pain page cites Noordhof (2021) once (L142), accurately. The Fable review's Verification Notes confirm p. 178. This session confirms the p. 177 response-dependence sentence [raw].

## Per-View Prediction Table {#prediction-table}

| View (proponents) | Content of pain / of its unpleasantness | Reading of asymbolia | Is "whether it hurts" a content difference? | Bearing on the Map's inseparability claim |
|---|---|---|---|---|
| **Grahek** (2007). Not a content theory; declares neither "subjectivist" nor "objectivist" | Pain is composite: a sensory-discriminative component plus affective, cognitive and behavioural components. "Painfulness" is the affective component | "Pain without painfulness". The sensory component survives and is inert. Asymbolic pain "does not represent for them any damage" (p. 80) | No. Painfulness is a separable component, not content | **Against** inseparability for the sensory quale ("powerless to move the body and mind in any way", p. 76). Consistent with it only if "awfulness" means the affective component. The page recruits Grahek for the opposite of his use: asymbolia was his counterexample to *motivationalism* (Klein 2015 *Mind* abstract) |
| **Pure imperativism** (Klein 2007, 2015) | Pain is exhausted by imperative content: in 2007 a proscription against acting with the part, in 2015 "protect that body part" (SEP). Hurt is "a response to pain", contingently connected; unpleasantness is tentatively a higher-order command (SEP; Barlassina & Hayward call it "higher-order imperativism") | Asymbolics keep their pains (the commands) but "have lost a general capacity to care about their bodily integrity". This predicts broad threat-indifference and a link to depersonalisation (Klein & Duval 2023 [raw]: "predicts that pain asymbolia ought to come with more general deficiencies in reacting to immediate threats to one's body") | **No** for pain itself (pains "only contingently hurt"). Tentatively yes for suffering, via a higher-order command; Klein offers "no theory of suffering" | Motivational force is constitutive of *pain*. Hurt is separable from pain, so Klein does not build inseparability of *hurt* and causal power into the view. Non-discriminating either way |
| **Hybrid (first-order) imperativism** (Martínez 2011; the SEP also files Hall 2008, on itch, here) | Indicative content ("there's something going on in my leg") plus imperative content, e.g. <See to it that this bodily damage is no more!> (SEP). Painfulness *is* the imperative content | The indicative content survives and the command is lost: "sensory pain without painfulness" (Martínez 2023). The command is computed at the limbic integration stage, where lesions cut it off | **Yes** | Inseparability is built in, since painfulness just is a command, and so cannot discriminate dualism. Barlassina & Hayward's objection: first-order imperative content is neither sufficient (neutral itches) nor necessary (objectless misery) for affective character |
| **Reflexive imperativism** (Barlassina & Hayward 2019) | Unpleasantness = "Less of U!" / "Get less of me!", a command about the experience itself | Asymbolic pain "does not feel unpleasant" and so is no affective experience; whether it is still pain is left open (preprint fn. 3) | **Yes** | Built in, as for hybrid imperativism. Its reflexive content is designed to make painkillers rational |
| **Evaluativism** (Bain 2013, 2014, 2019; label Bain's per SEP; precursors Nelkin 1994, Helm 2002, Tye 2005) | The pain represents a bodily disturbance and additionally represents it as bad for the subject "in the bodily sense" (Bain 2013 p. S82, [raw, quoted] by SEP). Reasons and motivation flow from evaluative content (Bain 2013 abstract) | The missing component "consists in evaluative content". It is missing *because* asymbolics cannot care (Bain 2014 combines Grahek and Klein) | **Yes** | Motivation and reasons follow from the evaluative content in a subject who cares. When caring goes, they come apart. No inseparability at the level of pain-the-sensation |
| **Tracking representationalism** (Tye 2005; Cutter & Tye 2011, 2014) | The badness of bodily damage *for us*, an objective, evolutionarily significant property of the disturbance (SEP; Gray 2018 abstract) | Not read this session. By the view's structure, the evaluative tracking component is lost. a Martínez post on Philosophy of Brains reportedly argues the tracking theory struggles here (search snippet only, unverified) | **Yes** | Reductive, and explicitly physicalist. Motivation runs through the represented badness |
| **Response-dependence** (Noordhof 2021) | Pain represents a sensory quality (PQ) at a location. Painfulness is a response-dependent property, represented *by* the disposition to respond aversively, M(Rp), which is "part of its representational properties" | The reversal: "their failure to have the disposition is the explanation of why they don't experience the pain as painful" (p. 178) | **Yes**. Noordhof presents this as the answer to the objection that representing damage "would not imply that the experience itself was unpleasant" (p. 177) | Inseparability is close to analytic, since painfulness is partly the aversive disposition. A rival that *accepts* the page's thesis gladly, as the Fable review said |
| **Self-model / active inference** (Gerrans 2020, 2024) | Not a content theory of unpleasantness. Affect is marked "mine" by anterior-insular self-modelling | "Depersonalization for pain" | n/a | Already engaged on [[pain-asymbolia]] L73. No change needed |
| **Anti-unitarism** (Corns 2014, 2020) | No single property. Unpleasantness and motivational oomph doubly dissociate and together are insufficient for painfulness | — | — | **The direct counter** to a strict biconditional between felt badness and motivation. Already in the corpus at [[valence-as-a-natural-kind]] L74 |

**Reading the table.** On every content view, asymbolia is a prediction, not an anomaly. What it presses is *motivationalism*, the thesis that pain is intrinsically motivating (Grahek's target), and among imperativists it presses hardest on Klein's *pure* view. Klein's answer relocates the deficit from the pain to the subject. Bain (2011 [abstract]) "use[s] dissociation cases to argue that possession of ‘imperative content’ cannot wholly constitute pain". The SEP's verdict is that "there is evidence that pain asymbolia may be the only form of genuine dissociation (Grahek 2007)" [raw]. So the case is strong evidence that pain is composite, and weak evidence about what the affective component is.

## Recommended Fold {#fold}

Two hosts. The primary host carries the correction and the comparator; the secondary host gets one paragraph. Both passages were applied to scratch copies and measured with `analyze_length`.

### Host 1 (primary): `concepts/valence`

- **Replace** everything from the heading `## Two Competing Accounts` (`grep -c -F` = 1, currently L43) up to but not including `## Valence and the Hard Problem` (`grep -c -F` = 1, currently L57). That is the two-accounts list and the `### Why the Hedonic Account Is Stronger` subsection, L43–55, 277 words. Other anchors in the replaced span, each `grep -c -F` = 1: "Two main philosophical accounts compete to explain what valence is."; "[[pain-asymbolia|Pain asymbolia]] provides the strongest evidence."; "If valence were merely a representation of value, these patients should still feel motivated to avoid damage. They don't."; "What survives the exchange is the asymmetry itself".
- **No inbound anchors break.** No live page links to `valence#two-competing-accounts` or `#why-the-hedonic-account-is-stronger` (grepped 2026-11-10). The heading rename is safe.
- **Measured**: 1,932 → **2,409** (+477, ten References entries included). That is under the 2,500 soft guideline and leaves 1,090 under the hard gate. The open P2 on this page (todo L5206, L85/L69 calibration, ≤ +15) does not touch L43–55. The two can land in either order.
- **Passage** (use as drafted; every quoted fragment is in the [ledger](#ledger)):

> ## Three Competing Accounts
>
> Three philosophical accounts compete to explain what valence is.
>
> **The hedonic account** treats valence as an intrinsic qualitative property of experience. The badness of pain is not *about* anything—it is a feature the pain has in virtue of being the experience it is. Just as redness is an intrinsic quality of visual experience, badness is an intrinsic quality of painful experience.
>
> **The evaluativist account** treats valence as a nonconceptual representation of value. David Bain, who gave the view its name, states it for pain: an unpleasant pain represents a bodily disturbance and also represents that disturbance as bad for its subject (Bain 2013). Cutter and Tye (2011) give a tracking version on which the represented badness is an objective property of the damage, and Carruthers (2018) extends the view to valence generally: when afraid, attention is directed outward—the bear's claws seem dangerous.
>
> **The imperativist account** treats valence as a command rather than a description. Klein (2007) gave the first explicit imperative theory of pain, on which a pain's content is a command against using the injured part; Martínez (2011) extended imperative content to pain's unpleasantness, pairing a description of the disturbance with a command to see that it ends; Barlassina and Hayward (2019) generalise the view to all affect, on which an unpleasant experience commands "Get less of me!" On both representational accounts of unpleasantness, whether an experience hurts is a difference in what it represents or commands, so they deny that two experiences could share their content and differ only in felt badness.
>
> ### Where the Hedonic Account's Case Lies
>
> [[pain-asymbolia|Pain asymbolia]] can look like decisive evidence: patients represent tissue damage—they know their hand is burned—without feeling any badness. That rules out identifying felt badness with the detection of damage. It does not favour the hedonic account over its representational rivals, because both predict the dissociation. Evaluativists deny that asymbolics represent the damage as bad for them, and Bain (2014) argues that the missing component of their pain "consists in evaluative content"; hybrid imperativism keeps the description and loses the command, which yields what Martínez (2023) calls "the familiar asymbolic pattern of sensory pain without painfulness."
>
> The hedonic account's advantage lies with reasons. A pain gives its subject a reason to be rid of the experience itself, which is why taking a painkiller that leaves the injury untouched is rational. If the unpleasantness were only a representation of the damage, removing the experience while the damage remains would be "shooting the messenger" (Jacobson 2013). Representationalists have replies (Cutter and Tye 2014), and the dispute is open, but on the hedonic account the reason needs no further machinery: the badness is in the experience, so ending the experience ends it. Objectless moods offer a second consideration. Free-floating anxiety and undirected elation feel bad or good without representing any particular thing as dangerous or fine. An evaluativist can answer that such moods represent the world at large under an evaluative aspect, which keeps that case contested rather than settling it.
>
> Two limits bound the result. Representationalism and physicalism come apart: tracking versions are explicitly reductive, but the non-reductive versions Aydede (2023) distinguishes hold that the represented content resists naturalistic explanation, so the choice among these three accounts is orthogonal to the [[tenets#^dualism|Dualism]] tenet, and the Map's dualism would survive the hedonic account's defeat. Nor does any of the three make valence idle: the representational accounts build motivational force into the content itself, so the question is what the felt badness is, not whether it does any work.

- **References to add** (the host's format; the list is unsorted with repeated `1.`, so append at the end):

> 1. Aydede, M. (2023). Is pain representational? *Belgrade Philosophical Annual*, 36(2), 25–39. https://doi.org/10.5937/bpa2302025a
> 1. Bain, D. (2013). What makes pains unpleasant? *Philosophical Studies*, 166(S1), 69–89. https://doi.org/10.1007/s11098-012-0049-7
> 1. Bain, D. (2014). Pains that don't hurt. *Australasian Journal of Philosophy*, 92(2), 305–320. https://doi.org/10.1080/00048402.2013.822399
> 1. Barlassina, L., & Hayward, M. K. (2019). More of me! Less of me!: Reflexive imperativism about affective phenomenal character. *Mind*, 128(512), 1013–1044. https://doi.org/10.1093/mind/fzz035
> 1. Cutter, B., & Tye, M. (2011). Tracking representationalism and the painfulness of pain. *Philosophical Issues*, 21(1), 90–109. https://doi.org/10.1111/j.1533-6077.2011.00199.x
> 1. Cutter, B., & Tye, M. (2014). Pains and reasons: Why it is rational to kill the messenger. *The Philosophical Quarterly*, 64(256), 423–433. https://doi.org/10.1093/pq/pqu025
> 1. Jacobson, H. (2013). Killing the messenger: Representationalism and the painfulness of pain. *The Philosophical Quarterly*, 63(252), 509–519. https://doi.org/10.1111/1467-9213.12029
> 1. Klein, C. (2007). An imperative theory of pain. *The Journal of Philosophy*, 104(10), 517–532. https://doi.org/10.5840/jphil2007104104
> 1. Martínez, M. (2011). Imperative content and the painfulness of pain. *Phenomenology and the Cognitive Sciences*, 10(1), 67–90. https://doi.org/10.1007/s11097-010-9172-0
> 1. Martínez, M. (2023). Grahek-style imperativism. *Belgrade Philosophical Annual*, 36(2), 59–70. https://doi.org/10.5937/bpa2302059m

- **Optional, about +2 words**: [[valence-as-a-natural-kind]] L98's Further-Reading gloss "the hedonic and evaluativist accounts" can become "the hedonic, evaluativist and imperativist accounts".

### Host 2 (secondary): `concepts/pain-asymbolia`

- **Insert** a new paragraph in `## What Asymbolia Dissociates`, after the paragraph that begins "A second line of dissent targets the subtraction picture itself rather than the classification." and ends "…routes to [[constitution-vs-causal-work]]." (both `grep -c -F` = 1; currently L73). It goes immediately before the paragraph beginning "Nociception is one interoceptive channel" (`grep -c -F` = 1, currently L75).
- **Measured**: 2,968 → **3,112** (+144, two References entries included). **Coordination**: three open tasks also add to this page. They are the P2 Hagiwara 2020 inverse dissociation (todo L5163, ≤ +90), the P2 Schilder & Stengel priority plus L85–87 calibration (todo L5196, ≤ +40), and the P3 C-tactile case (todo L4272, +60 to +90). Together they could reach about +220 → ~3,332. That leaves ~168 under the `>=` 3,500 gate. None of them edits L73–75, so order is free. Re-measure before each.
- **Passage**:

> The representational theories of pain's unpleasantness predict the case from the content side. On Martínez's (2011) hybrid imperativism a pain pairs a description of a bodily disturbance with a command to end it, and asymbolia keeps the description while losing the command. On evaluativism the asymbolic still represents the disturbance but no longer as bad for themselves, and Bain (2014) joins this to Klein's reading: the lost capacity to care explains why the pain lacks a component that "consists in evaluative content". What asymbolia presses is the motivationalist claim Grahek targeted—that pain is intrinsically motivating—rather than representationalism as a family; [[valence]] takes up how the Map's hedonic reading fares against these rivals.

- **References to add** (the host's format; Bain goes before Berthier, Martínez after Klein):

> 1. Bain, D. (2014). "Pains That Don't Hurt." *Australasian Journal of Philosophy*, 92(2), 305–320. https://doi.org/10.1080/00048402.2013.822399
> 1. Martínez, M. (2011). "Imperative Content and the Painfulness of Pain." *Phenomenology and the Cognitive Sciences*, 10(1), 67–90. https://doi.org/10.1007/s11097-010-9172-0

  (The host's list is not strictly sorted: Geschwind sits last. Insert by surname and leave the rest alone. The scratch measurement put Bain after Berthier; the word count is unaffected.)

### Quotation ledger {#ledger}

| # | Fragment as used in the fold | Source, locus | Verified from | Grammatical subject in source |
|---|---|---|---|---|
| 1 | "Get less of me!" | Barlassina & Hayward 2019, opening of the paper | raw preprint (White Rose 144897): "commanding us Get more of me!, Get less of me!"; the same pair is in the *Mind* abstract quoted in the 2026-09-05 note | the slogan for unpleasant experience; the fold's subject is "an unpleasant experience" (same) |
| 2 | "consists in evaluative content" | Bain 2014, abstract | OpenAlex abstract: "(ii) claim that the missing component consists in evaluative content" | "the missing component" (of asymbolics' pains); the fold keeps that subject in both hosts |
| 3 | "the familiar asymbolic pattern of sensory pain without painfulness" | Martínez 2023, §5, p. 68 | raw PDF text: "If the structures in charge of issuing the painful imperative are not there, or are cut off from sensory cortices, we should expect the familiar asymbolic pattern of sensory pain without painfulness." | what "we should expect" on Martínez's model; the fold says Martínez "calls" it that, which fits |
| 4 | "shooting the messenger" | Jacobson 2013, abstract | OpenAlex abstract: "a subject who knowingly acts so as to get rid of her pain without thereby getting rid of the bodily condition it represents always behaves irrationally – in so acting she is shooting the messenger" | the subject who removes the pain but not the condition; the fold paraphrases that condition faithfully |

Every other quotation in this note is grep-verified in the raw source its grade names. The script is `imp-scripts/verify_quotes.py` in this session's scratchpad: 39 strings, all present.

## Guards for the Fold Writer {#guards}

- **Quote only the four ledger fragments.** If a sentence must change, change the paraphrase, not the quotation. Bain 2013's "bad for him in the bodily sense" is [raw, quoted] via the SEP only. The fold paraphrases it ("bad for its subject"); keep it paraphrased.
- **Coiners.** Klein (2007) gave the first explicit imperative theory of *pain* (Martínez 2023: "the first explicit imperativist treatment of pain … was Klein (2007)"; Barlassina & Hayward: imperative content "was first used to explain … itches (Hall 2008) and pains (Klein 2007)"). Martínez (2011) first applied it to pain's *unpleasantness*. Do not credit Klein's 2015 book with originating imperativism; it is the full development. For evaluativism, the SEP says "Bain labels the position evaluativism". The idea predates the label (Nelkin 1994; Helm 2002; Tye 2005/2006; Cutter & Tye 2011), so the fold says Bain "gave the view its name", not that he originated it. Carruthers (2018) is a later proponent about valence generally. Keep him as the valence-wide citation, not the pain-evaluativism source.
- **Klein 2015 is not a hurt-as-content theorist.** For the book, pains "only contingently hurt and feel bad". Do not attach "whether it hurts is a difference in content" to Klein. The fold attaches it to "representational accounts of unpleasantness" and cites Klein only for 2007 priority. Keep it so.
- **Klein 2007's content is a proscription** ("a command against using the injured part"). The SEP gives "a proscription against acting with bodily parts where pain is felt", and Klein (2010 [abstract]): "pains proscribe against taking action with the painful body part". The 2015 "protect that body part" formulation is the book's. Do not swap them.
- **Calibration that must survive edits.** The fold says asymbolia "rules out identifying felt badness with the detection of damage". That much it does. It must not say asymbolia refutes, defeats or disfavours evaluativism or imperativism. "The dispute is open" and "keeps that case contested" stay. The final paragraph's two limits stay intact: representationalism ≠ physicalism, and none of the accounts makes valence idle. They are what stops the fold from reading as either a concession of dualism or an argument for it.
- **Never concede epiphenomenalism.** The last sentence ("the question is what the felt badness is, not whether it does any work") is the guard. Do not cut it for length.
- **Do not touch** `concepts/valence` L65–69 or L85 (owned by the open P2, todo L5206), or the lede at L33. In `concepts/pain-asymbolia`, do not touch L50 or L85–87 (todo L5196), the Complementary Dissociations section (todo L4272, L5163), or the Klein/Gerrans paragraph L73 itself.
- **Pronouns.** In the asymbolia passage, "Klein's reading" points back to the L73 paragraph, which must stay immediately above. "themselves" (singular, for "the asymbolic") is deliberate; "for them" would be ambiguous. In the valence passage, "both" in "because both predict the dissociation" = the two representational rivals named in the previous section.
- **Prose discipline**: no "This is not X. It is Y."; no "load-bearing"; no mode labels. After insertion, check that `## Valence and the Hard Problem` reads on from "…not whether it does any work."
- **Frontmatter**: `ai_modified` from `date -u`. `ai_system`: `concepts/valence` is `claude-opus-4-6+claude-opus-5+claude-fable-5+claude-fable-5-1` and `concepts/pain-asymbolia` is `claude-opus-4-6+claude-opus-5+claude-fable-5-1`. Append the writer's model only if that exact component is absent anywhere in the string. `claude-opus-5-5` is absent from both today.
- **(Surname, year) orphan check both ways** after the edit. The valence fold adds ten body citations and ten references; Carruthers 2018 is already listed.

## Downstream Corrections Outside the Fold {#downstream}

These loci repeat the claim the fold withdraws. They are `refine-draft` material for the driver to mint, not part of the fold. Each OLD string is `grep -c -F` = 1 on 2026-11-10.

1. **`topics/emotion-and-dualism`** (3,404/4,000; open P3 todo L1793 touches L107/L212 only).
   - L79 OLD paragraph begins "Pain asymbolia cases reveal which account is correct." and contains "they retain the capacity to represent tissue damage as harmful". It also answers the evaluativist with "this concedes the point: whatever is disrupted is the felt badness, not the informational content about harm". An evaluativist concedes nothing there, because for them the felt badness *is* the evaluative content and not the informational content about damage. The sentence presupposes the conclusion.
   - Suggested NEW (length-neutral): "Pain asymbolia narrows the dispute without settling it. Patients represent tissue damage (they know their hand is burned) without feeling the badness, which rules out identifying the badness with damage detection. Evaluativists predict the same case: on their view asymbolics no longer represent the damage as bad for them, and Bain (2014) locates the missing component of their pain in evaluative content. The hedonic account's case rests on other ground, set out in [[valence]]." Add Bain 2014 to References, or drop the citation and keep the [[valence]] pointer.
   - L83 OLD "Pain asymbolia does more than settle the hedonic-evaluativist debate." NEW "Pain asymbolia matters beyond the hedonic-evaluativist debate."
   - L85 ("The representation exists—patients accurately represent tissue damage … despite intact representation …") is aimed at functionalism and can stand. Check it does not re-assert intact *evaluative* representation.
2. **`apex/minds-without-words`** (4,141/5,000).
   - L111 OLD "**Pain asymbolia settles this specific dispute**" and "which is why asymbolia is decisive against the evaluativist reduction". NEW: "**Pain asymbolia narrows this specific dispute**" … and replace the "decisive" clause with "which rules out identifying valence with damage detection, though evaluativists predict the same dissociation ([[valence]])". The next sentence ("It does *not* settle the separate Panksepp-LeDoux question…") still reads with "It" = asymbolia; keep "separate".
   - L137 OLD "Pain asymbolia constrains identity readings of valence by settling the hedonic-evaluativist dispute." NEW "Pain asymbolia constrains identity readings of valence by ruling out valence's identity with damage detection."
3. **Addendum for the open P1 on the pain page** (todo L5139, item (d), the red-square paragraph L128). Material for its NEW paragraph:
   - (i) Cite hurt-as-content to Martínez (2011) and Bain (2013), or Cutter & Tye (2011), not to Klein (2015). Klein's book makes hurt "a response to pain" (pp. 46–7, [raw, quoted] by Fulkerson). Klein (2015) can carry *motivational force by representational mode*, which is what the P1's Notes say.
   - (ii) The page's own phrase "tissue-damage-as-threat" already builds evaluative content into the comparison, as the Fable review notes.
   - (iii) Noordhof (2021, p. 177 [raw]), whom the page already cites at L142, presents response-dependence as the representationalist answer to exactly the red-square worry: "Recognition that the disposition to respond aversively can itself be a representational property avoids this problem."
   - (iv) The Map's residual is the general explanatory gap the page already states at L132, which applies to redness as much as to pain. Nothing pain-specific survives.
   - Length: net ≤ 0, per that task. A pipe link `[[valence|…]]` on existing words costs nothing.
4. **Addendum for the open P2 on the pain page** (todo L5184, item (c), inseparability L134–142).
   - (i) Grahek's own view of the sensory component is the opposite of inseparability: "powerless to move the body and mind in any way" (p. 76, [raw, quoted] by Martínez 2023). This strengthens the Fable review's point that the page recruits Grahek against his use.
   - (ii) Imperativism and Noordhof make motivational force or the aversive disposition constitutive of pain or painfulness. Inseparability is therefore a thesis these physicalist-compatible rivals *share*, and it can be stated as coherence-only without loss.
   - (iii) Corns (2014) is the counter-evidence to a strict biconditional and is already in the corpus ([[valence-as-a-natural-kind]] L74).

## Pages Considered and Not Recommended {#not-recommended}

- **A topics article** (`topics/imperativism-and-evaluativism-about-pain`, free per `scripts/check_slug.py`). **Declined.** The cap is exhausted, and the yield is a correction plus a comparator, which `concepts/valence` can carry with 1,090 words to spare after the fold. An article would be mainly an exposition of physicalist theories of pain affect, background the style guide says to skip unless framed for the Map's perspective, and the framing is two paragraphs long. If a human later wants an article, the [prediction table](#prediction-table) and [Key Debates](#debates) are its outline. Keep the slug.
- **`topics/pain-consciousness-and-causal-power`** (3,982/4,000; four open tasks). No fold. Its red-square and inseparability passages are owned by the open P1 (L5139) and P2 (L5184), and [§Downstream](#downstream) items 3–4 give those tasks their material.
- **`concepts/evaluative-phenomenal-character`** (3,490/3,500). No room; not needed.
- **`topics/emotion-and-dualism` as a fold host.** Its "Hedonic vs. Evaluativist Accounts" subsection (L73–79) duplicates the valence page. The right fix is the length-neutral correction in [§Downstream](#downstream) item 1 plus a pointer to [[valence]], not a second copy of the comparator.

## Key Sources

### SEP "Pain" (Aydede; first published 30 Sep 2005, substantive revision 4 Mar 2019) [raw]
- **URL**: https://plato.stanford.edu/entries/pain/
- **Key points**: §5 "Evaluative and motivational theories". "Perhaps the two most prominent proponents of a mixed evaluative view of pain, in recent years, are Michael Tye (2006a,b, Cutter & Tye 2011) and David Bain (2003, 2013, 2017). Both defend strong representationalism for both the sensory and affective components of pains. Bain labels the position evaluativism." "Tye (2006a,b) and Cutter & Tye (2011) take the badness of physical disorder to be an evolutionarily significant objective property of the disturbance (such as aptness to harm)." "Hall (2008), Martinez (2011), and Klein (2007) offer accounts of pain that belong to the class of motivational theories. They call their views ‘imperative’ theories (or, imperativism as the views have come to be known)". Hall and Martínez give mixed descriptive-plus-imperative contents ("Stop! Stop doing what you're doing with this bodily part" (Hall 2008: 534); <See to it that this bodily damage is no more!> (Martinez 2011)). Klein's are purely imperative, and for Klein "The affective, unpleasantness, aspect is only contingently related to pains … and consists of second-order agential level commands directed at the pain's imperative content." On asymbolia: "there is evidence that pain asymbolia may be the only form of genuine dissociation (Grahek 2007)". Lobotomy and morphine patients "Probably … still feel the negative affect but don't mind it". That last point is relevant to the sibling harvest task on surgical and pharmacological dissociation (todo L46), not here.
- **Tenet alignment**: Neutral survey. Its observation that "functionalist or psychofunctionalist reductions of the affective/evaluative dimension of pain might turn out to be the most natural option" for these theorists is the physicalist end-state the Map declines.

### Klein (2015), "What Pain Asymbolia Really Shows", *Mind* 124(494):493–516 [abstract; p. 498 raw, quoted]
- **URL**: https://doi.org/10.1093/mind/fzu185
- **Key points**: "Nikola Grahek argues that such patients present a clear counterexample to motivationalism about pain. I argue that Grahek has mischaracterized pain asymbolia. Properly understood, asymbolics have lost a general capacity to care about their bodily integrity. Asymbolics’ indifference to pain thus does not show something about the intrinsic nature of pain; it shows something about the relationship between pains and subjects". p. 498 (quoted by Klein & Duval 2023): "They do not care about cuts and burns and scrapes, because they can no longer conceive of why such events are bad."
- **Tenet alignment**: Physicalist imperativist; already engaged on [[pain-asymbolia]]. The p. 498 sentence is the textual refutation of the corpus premise that asymbolics "retain the capacity to represent tissue damage as harmful".

### Klein (2015), *What the Body Commands: The Imperative Theory of Pain*, MIT Press [abstract (MIT description); chapter list metadata; pp. 46–7, 48, 56 raw, quoted by Fulkerson 2016]
- **URL**: https://doi.org/10.7551/mitpress/10480.001.0001
- **Key points**: "Klein argues that pains are imperative; they are sensations with a content, and that content is a command to protect the injured part of the body. He terms this view ‘imperativism about pain,’ and argues that imperativism can account for two puzzling features of pain: its strong motivating power and its uninformative nature." "Klein's intent is to defend the imperativist view in a pure form—without requiring pain to represent facts about the world." Chapters 11 "Pain Asymbolia and Lost Capacities" (pp. 141–152) and 12 "Asymbolia, Motivation, and the Self" (pp. 153–166). Via Fulkerson: "suffering is not a feature of pain: it is a response to pain. This means that suffering is only contingently connected to pain, and hence that pains only contingently hurt and feel bad" (46–7); "Commands from the body do not intrinsically, essentially, or necessarily feel bad" (48); "I have no theory of suffering, no story about what sort of state is present when pains feel bad" (56).
- **Tenet alignment**: The pure imperativist separates pain from hurt, which is closer to Grahek's separation than the reviewers' summaries suggest. For the Map, Klein's book is a rival about pain's *motivation* and is silent about its *hurt*.

### Fulkerson (2016), NDPR review of *What the Body Commands* (2016.03.05) [raw]
- **URL**: https://ndpr.nd.edu/news/what-the-body-commands-the-imperative-theory-of-pain/
- **Key points**: The source of the book quotations above. Fulkerson's own objection: "Pains perform their primary motivating function very often by hurting", and severe pains "are impossible to ignore, even when we think they are issued in error". He prefers a view on which pains "compel action directly, by (among other things) biasing motor responses, capturing attention, and rewarding compliance".
- **Tenet alignment**: A psychofunctionalist (co-author of Aydede & Fulkerson). He is an ally only on the narrow point that hurting does motivational work, which is the Map's inseparability intuition stated by a physicalist.

### Martínez (2011), "Imperative content and the painfulness of pain", *Phenomenology and the Cognitive Sciences* 10(1):67–90 [metadata; content via SEP, Martínez 2023 and Barlassina & Hayward, all raw]
- **URL**: https://doi.org/10.1007/s11097-010-9172-0 (online 6 Aug 2010; issue 2011)
- **Key points**: First-order hybrid imperativism. Pain pairs indicative content (B&H's reconstruction: "There is a burning disturbance in your right hand") with imperative content ("See to it that the disturbance in your right hand does not exist!"). The painfulness is the imperative component (Barlassina & Hayward: imperative content "was deployed to deal with pain experiences' affective phenomenal character (Martínez 2011)").
- **Tenet alignment**: Physicalist-compatible (naturalistic metasemantics: Millikan, Shea). It predicts asymbolia directly.

### Martínez (2023), "Grahek-style imperativism", *Belgrade Philosophical Annual* 36(2):59–70 [raw]
- **URL**: https://doi.org/10.5937/bpa2302059m (open access)
- **Key points**: The priority claim: "the first explicit imperativist treatment of pain (i.e., one along the lines sketched above) was Klein (2007)". The debate map: evaluative content "along the lines of ‘What is currently happening to your right arm is bad news’ (Tye 2006; Bain 2013)" versus imperative content "along the lines of ‘Do something about your right arm!’ (Klein 2007, 2015a; Martínez 2011; Barlassina and Hayward 2019)". On Grahek: he "presents this claim as supported by asymbolia" and argues "that painful phenomenology cannot represent tissue damage (the way evaluativists such as Tye or Bain, cited above, would want) because, if it did, asymbolics would be motivated to do something about it". Grahek's own words as Martínez quotes them: "[T]he pain that these patients feel does not represent for them any damage or potential damage to their bodies. That this is so is best proved by the fact that they consistently smile or laugh during pain testing procedures" (p. 80); the sensory essence is "a blunt, fleshless, inert sensation pointing to nothing beyond itself, leaving no traces in the memory and powerless to move the body and mind in any way" (p. 76). Against Klein's lost-care model: pain *vehicles* can disrupt regardless of caring (the "stolen-bicycle spam" and earworm cases), and the care model "does not seem to speak to how the asymbolic is able to effortlessly ignore the spammy repetition of pain vehicles". The positive model: indicative content near the sensory periphery, imperative content after limbic integration (citing Price 2000), so a limbic lesion yields "the familiar asymbolic pattern of sensory pain without painfulness". fn. 1: "the intentionalist thesis is compatible with the bearers of content not being the experiences themselves".
- **Tenet alignment**: The single most useful source. It shows the corpus's asymbolia-against-evaluativism argument is Grahek's, and it records the content-theoretic reply.

### Bain (2014), "Pains that Don't Hurt", *Australasian Journal of Philosophy* 92(2):305–320 [abstract]
- **URL**: https://doi.org/10.1080/00048402.2013.822399 (online Aug 2013)
- **Key points**: "Nikola Grahek thinks asymbolics’ pains are abnormal, lacking a component that make normal pains unpleasant and motivating. Colin Klein thinks that what is abnormal is not asymbolics’ pains, but asymbolics … I agree with Klein that asymbolics are incapable of caring about their bodily integrity; but I argue against him that, if this is to explain not only their indifference to visual and verbal threat, but also their indifference to pain, we must … (i) take asymbolics’ lack of bodily care not as an alternative to, but as an explanation of their pains’ missing a component, and (ii) claim that the missing component consists in evaluative content. Asymbolia, I conclude, reveals not only that unpleasant pain is composite, but that its ‘hedomotive component’ is evaluative."
- **Tenet alignment**: The direct counter to [[valence]] L53 and its siblings. The evaluativist claims asymbolia as *support*.

### Bain (2013), "What makes pains unpleasant?", *Philosophical Studies* 166(S1):69–89 [abstract; p. S82 raw, quoted by SEP]
- **URL**: https://doi.org/10.1007/s11098-012-0049-7 (Glasgow Enlighten 70384)
- **Key points**: "The unpleasantness of pain motivates action. Hence many philosophers have doubted that it can be accounted for purely in terms of pain’s possession of indicative representational content. Instead, they have explained it in terms of subjects’ inclinations to stop their pains, or in terms of pain’s imperative content. I claim that such ‘noncognitivist’ accounts fail to accommodate unpleasant pain’s reason-giving force. What is needed, I argue, is a view on which pains are unpleasant, motivate, and provide reasons in virtue of possessing content that is indeed indicative, but also, crucially, evaluative." The canonical statement (quoted by the SEP): "A subject’s being in unpleasant pain consists in his (i) undergoing an experience (the pain) that represents a disturbance of a certain sort, and (ii) that same experience additionally representing the disturbance as bad for him in the bodily sense."
- **Companions**: Bain (2011), "The imperative view of pain", *JCS* 18:164–185 [abstract]: "Against Klein, I use dissociation cases to argue that possession of ‘imperative content’ cannot wholly constitute pain … the idea of a command cannot bear the explanatory weight Klein and Hall place on it." Bain (2019; online 2017), "Why take painkillers?", *Noûs* 53(2):462–490 [abstract]: "pain’s unpleasantness does indeed have noninstrumental disvalue", and his "evaluativist view can [accommodate it]—either by appealing to ‘anti-unpleasantness’ desires or by exploiting pain’s perceptuality".

### Cutter & Tye (2011), "Tracking representationalism and the painfulness of pain", *Philosophical Issues* 21(1):90–109 [metadata; content via SEP and Gray 2018]
- **URL**: https://doi.org/10.1111/j.1533-6077.2011.00199.x
- **Key points**: Gray (2018 [abstract]) summarises the view: "Tracking representationalism explains the negative affective character of pain, and its capacity to motivate action, by reference to the representation of the badness for us of bodily damage." Reply to Jacobson: Cutter & Tye (2014), *Phil Q* 64(256):423–433 [abstract], aim "to show that these charges are mistaken".
- **Tenet alignment**: Reductive physicalist. The paper's text on asymbolia was not read (see Gaps).

### Jacobson (2013), "Killing the Messenger: Representationalism and the Painfulness of Pain", *Philosophical Quarterly* 63(252):509–519 [abstract]
- **URL**: https://doi.org/10.1111/1467-9213.12029
- **Key points**: "representationalism does not have the resources to explain the most salient aspect of the phenomenal character of pain – it is bound to leave out the painfulness of pain or its negative affect … representationalism is committed to a false picture on which a subject who knowingly acts so as to get rid of her pain without thereby getting rid of the bodily condition it represents always behaves irrationally – in so acting she is shooting the messenger."
- **Tenet alignment**: The best available argument for the hedonic reading over representationalism, and absent from the corpus. Jacobson's positive view (an attitudinal anti-damage desire account, per the SEP) is not the Map's. Cite her for the objection only.

### Barlassina & Hayward (2019), "More of me! Less of me!", *Mind* 128(512):1013–1044 [raw preprint]
- **URL**: https://doi.org/10.1093/mind/fzz035 (preprint: eprints.whiterose.ac.uk/144897)
- **Key points (pain-specific)**: the two-variety taxonomy, "first-order imperativism (Martínez 2011, 2015a, 2015b) and higher-order imperativism (Klein 2015)". The history: "Imperative content was first used to explain the sensory phenomenal character of bodily sensations like itches (Hall 2008) and pains (Klein 2007). Subsequently, it was deployed to deal with pain experiences’ affective phenomenal character (Martínez 2011)." fn. 3 on asymbolia: "Lacking affective phenomenal character, asymbolic pain does not count as an affective experience. Does it count as pain at all? This question is beyond the remit of this article."
- The valence-general content is in the 2026-09-05 note and is not repeated.

### Noordhof (2021), "Explaining Impossible and Possible Imaginings of Pain", *RIFP* 12(2):173–182 [raw]
- **URL**: https://doi.org/10.4453/rifp.2021.0015 (White Rose 178347, CC BY). Crossref has no record of this DOI (404). OpenAlex and White Rose confirm it.
- **Key points**: A comment in the *RIFP* forum on Radden's "Imagined and delusional pain". p. 177: "The painfulness of pain is plausibly a response dependent property"; "A subject’s experience represents the painfulness of pain when the experience includes, as a part of its representational properties, M(Rp)"; "The painfulness of pain has been thought to be an objection to representationalist accounts of pain because it was assumed that even, if our pain experiences represented damage to the body, or indeed, that there was something painful going on, this would not imply that the experience itself was unpleasant. Recognition that the disposition to respond aversively can itself be a representational property avoids this problem." p. 178: "my proposal is that their failure to have the disposition is the explanation of why they don’t experience the pain as painful." He predicts that asymbolics "would take pain to be no less basically imaginable than other bodily sensations".
- **Tenet alignment**: A representationalist answer to the red-square worry that the pain page already cites for something else. It accepts the inseparability thesis, so it shows the thesis does not discriminate.

### Aydede (2023), "Is pain representational?", *Belgrade Philosophical Annual* 36(2):25–39 [raw]
- **URL**: https://doi.org/10.5937/bpa2302025a (open access)
- **Key points**: Strong representationalism "has reductive and non-reductive versions, which are usually paired with realist and irrealist versions respectively". "Defenders of irrealist strong representationalism tend to be nonreductivist about both experience and representation: sensory experiences have their phenomenal character solely due to their representational content (sometimes called phenomenal content), which cannot be explained in purely non-representational, non-mental, or more broadly, naturalistic/physicalistic terms." Conclusion: "making pain experiences (along with the experiences of other similar bodily sensations) strongly representational is a mistake." He sets imperativism aside (fn. 1).
- **Tenet alignment**: An anti-representationalist about pain, but a psychofunctionalist, not a dualist. Cite him for the taxonomy (representationalism ≠ physicalism) and not as an ally of Tenet 1.

### Klein & Duval (2023), "Is pain asymbolia a deficit or a syndrome?", *Belgrade Philosophical Annual* 36(2):41–57 [raw]; Duval & Klein (2025), *Phil Sci* 93(1):221–229 [raw]
- **URLs**: https://doi.org/10.5937/bpa2302041d · https://doi.org/10.1017/psa.2025.10098
- **Key points**: Klein's view "predicts that pain asymbolia ought to come with more general deficiencies in reacting to immediate threats to one’s body". The Grahek–Klein dispute is cast as deficit versus syndrome, mirroring a German versus French split in early neurology. "The term was first introduced in a case study by Schilder and Stengel (1928)", which corroborates the open priority task (todo L5196). Duval & Klein conclude "for all we know, pain asymbolia might still be pain."

### Grahek (2007), *Feeling Pain and Being in Pain*, 2nd ed., MIT Press [abstract; pp. 76, 80 raw, quoted]
- **URL**: https://doi.org/10.7551/mitpress/2978.001.0001 (1st ed. 2001, BIS-Verlag, Oldenburg, per the Fable review; not checked)
- **Key points**: "pain without painfulness and painfulness without pain". The book "does not offer another philosophical theory of pain that conclusively supports or definitively refutes either subjectivist or objectivist assumptions". Grahek died in 2003 (Martínez 2023), before any of the imperativist papers.

### Corns (2014); Hall (2008); Gray (2018); Mitchell (2025); Kinakin (2026); Barlassina (2020); Coninx (2020) [abstracts]
- Corns: "Unpleasantness and motivational oomph doubly dissociate and, even taken together, are insufficient for painfulness."
- Hall: "The theory ascribes intentional content to bodily sensations but not, strictly speaking, representational content. Rather, the content of these sensations is an imperative: in the case of itches, ‘Scratch!’"
- Mitchell, "Towards Affective-Evaluativism", *Phil Q* 75(2):693–717: unpleasant pains "essentially involve a proprietary intentional mode—what I call affective-interoception—and a distinctive kind of evaluatively qualified sensory content". This is the current form of evaluativism.
- Kinakin, "Why intentionalists can’t take painkillers", *Phil Studies* 183(6):1905–1929 (2026): see the Executive Summary.
- Barlassina, "Beyond good and bad", *Thought* 9(4):274–284: "Evaluativism by Carruthers and reflexive imperativism by Barlassina and Hayward agree that valence … is a natural kind shared across all affective states".
- Coninx, "Pain experiences and their link to action", *JCS* 27: imperative theories "cannot provide an imperative content that meets their own criteria of sufficiency and necessity".

## Major Positions

### Evaluativism (Bain; Tye; Cutter & Tye; Mitchell; Carruthers for valence generally)
- **Core claim**: Pain's unpleasantness is the experience's representing a bodily disturbance as bad for the subject.
- **Key arguments**: It explains unpleasant pain's reason-giving force better than desire or imperative views (Bain 2013). It explains asymbolia as lost evaluative content (Bain 2014).
- **Relation to site tenets**: Compatible with physicalism in its tracking form. Non-reductive versions are compatible with dualism. Its live difficulty is the messenger-shooting and normative condition, which Bain (2019) accepts as a constraint. Its success would not refute Tenet 1, and its failure would not evidence it.

### Imperativism (Klein; Hall; Martínez; Barlassina & Hayward)
- **Core claim**: Pain, or its unpleasantness, has imperative content (satisfaction conditions, not truth conditions).
- **Key arguments**: It explains motivational force and pain's "uninformative" character (Klein). Homeostatic analogy (hunger, thirst, itch). Painkiller rationality on the reflexive version.
- **Relation to site tenets**: Physicalist-compatible (Millikan and Shea metasemantics). It shares the Map's conviction that pain's character is action-guiding, so it is a rival on *what* the character is, not on whether it acts.

### Response-dependence (Noordhof)
- **Core claim**: Painfulness is a response-dependent property, represented via the subject's aversive disposition.
- **Relation to site tenets**: It reverses the Map's explanatory order (disposition explains painfulness), which is why the pain page cites it as a constraint. It is compatible with physicalism.

### Anti-representationalism about pain (Aydede; Aydede & Fulkerson; Jacobson; Corns)
- **Core claim**: Pain affect is not (strongly) representational. Psychofunctionalist, desire-theoretic or pluralist accounts replace it.
- **Relation to site tenets**: On the Map's side against representationalism but not on Tenet 1. These are physicalist alternatives, so the Map should cite them for their objections, not their conclusions.

## Key Debates {#debates}

### Is asymbolia evidence about pain or about the subject?
- **Sides**: Grahek (pain's affective component is missing; deficit) vs Klein (the subject's capacity to care is missing; syndrome, depersonalisation) vs Bain (both: lost care explains the missing evaluative component) vs Martínez (processing-stage model; vehicles still disrupt) vs Griffith & Kind (not pain at all) vs Duval & Klein (probably still pain; taxonomy first). De Vignemont (2015) and Klein (2017, *AJP* 95(3):588–593, "Pain, care, and the body: A response to de Vignemont") dispute what "care for the body" means [metadata via Klein & Duval 2023].
- **Current state**: Open (Klein & Duval 2023: the debate "does not resolve"). For the Map the point is that no side reads asymbolia as evidence for a non-representational felt badness.

### Can representationalism explain painkillers? (the messenger-shooting objection)
- **Sides**: Jacobson 2013 and Kinakin 2026 (no) vs Cutter & Tye 2014 and Bain 2019 (yes) vs Barlassina & Hayward 2019 (reflexive content solves it).
- **Current state**: Live in 2026. This is where the hedonic account's case is strongest. Neither the corpus nor either outer review uses it.

### Is imperative content sufficient and necessary for unpleasantness?
- **Sides**: Martínez 2011 (first-order: yes) vs Barlassina & Hayward 2019 (neutral itches and objectless misery are counterexamples) vs Coninx 2020 (no imperative content meets the criteria) vs Bain 2011 (commands cannot carry the explanatory weight).

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1928 | Schilder & Stengel name "asymbolia" for pain | Priority (corroborates todo L5196) |
| 1994 | Nelkin, "Reconsidering Pain" | An "evaluative theory of pain" (judgmental, two-component) |
| 2001/2007 | Grahek, *Feeling Pain and Being in Pain* (1st/2nd ed.) | Asymbolia enters philosophy as "pain without painfulness"; used against motivationalism and against representing damage |
| 2002 | Helm, "Felt Evaluations" | Pains and pleasures as felt evaluations |
| 2005/2006 | Tye, "Another Look at Representationalism about Pain" | Evaluative content for pain's affect within tracking representationalism |
| 2007 | Klein, "An Imperative Theory of Pain" (*J Phil*) | First explicit imperativism about pain |
| 2008 | Hall, "If it itches, scratch!" | Imperative content for bodily sensations (itch) |
| 2011 | Martínez, "Imperative content and the painfulness of pain"; Cutter & Tye, "Tracking representationalism and the painfulness of pain"; Bain, "The imperative view of pain" | Imperativism extended to unpleasantness; tracking evaluativism; first critique of imperativism |
| 2013 | Bain, "What makes pains unpleasant?"; Jacobson, "Killing the messenger" | Evaluativism named and defended; the messenger-shooting objection |
| 2014 | Bain, "Pains that don't hurt"; Cutter & Tye, "Pains and reasons"; Corns, "Unpleasantness, motivational oomph, and painfulness" | Asymbolia claimed for evaluativism; reply to Jacobson; double dissociation of unpleasantness and motivation |
| 2015 | Klein, *What the Body Commands* and "What Pain Asymbolia Really Shows" (*Mind*) | Pure imperativism; asymbolia as lost care; hurt separated from pain |
| 2017/2019 | Bain, "Why take painkillers?" | Evaluativism accepts the non-instrumental-disvalue constraint |
| 2019 | Barlassina & Hayward, reflexive imperativism | "Get less of me!"; first-order and higher-order imperativism both rejected |
| 2020/2024 | Gerrans, depersonalisation for pain; allostatic extension | Self-model reading (already on [[pain-asymbolia]]) |
| 2021 | Noordhof, response-dependence of painfulness | Disposition explains painfulness |
| 2023 | *Belgrade Philosophical Annual* Grahek issue (Martínez; Klein & Duval; Aydede) | Grahek-style imperativism; deficit vs syndrome; representationalism's reductive/non-reductive split |
| 2024–2026 | Griffith & Kind; Duval & Klein; Mitchell; Kinakin | Is asymbolia pain? Affective-evaluativism; painkillers against intentionalism |

## Potential Article Angles

1. **The fold above** (recommended). It turns the valence page's two-account contrast into three, withdraws the asymbolia-settles claim, and relocates the hedonic account's case to reasons and objectless moods. Tenet alignment: Tenet 1 is explicitly left untouched by the outcome; Tenet 3 is protected by the no-idle-valence sentence; Tenet 5 by refusing to let a parsimony-flavoured "both predict it" become "therefore representationalism".
2. **A topics article** on representational theories of pain affect. Deferred (cap) and not recommended (yield). Use the prediction table as its outline if ever wanted.
3. **A narrower positions-register note.** If `positions/arguments-for-mental-causation` P-MC1 leans on asymbolia, its "would shift if" list could add that asymbolia is predicted by every content theory of pain affect. Not checked this session; flag only.

When writing, follow `obsidian/project/writing-style.md`: the named-anchor technique, background only where framed for the Map, the "Relation to Site Perspective" requirement, and front-loading.

## Gaps in Research

- **Cutter & Tye (2011) on asymbolia.** Full text bot-walled (Wiley). The table's tracking-representationalist row is inferred from the view's structure plus the SEP and Gray summaries. Martínez's Philosophy of Brains post reportedly argues the tracking theory struggles with asymbolia (search snippet only; the page is Cloudflare-walled). Do not cite Cutter & Tye *on asymbolia* until read.
- **Klein 2007 and Martínez 2011 abstracts and texts.** Not retrieved (PDCnet page without abstract, Springer walled). Their content is attested by three independent raw sources (SEP, Martínez 2023, Barlassina & Hayward). That is adequate for the fold's paraphrases, not for quotation.
- **Klein 2015 book, chapters 11–12.** Not read. The book quotations are via Fulkerson's review. The lost-care thesis is verified from the *Mind* abstract and the Klein & Duval quotation.
- **Grahek pp. 76 and 80.** Quoted by Martínez. Verify against the book before any article quotes them. The 2001 first edition was not checked.
- **Bain 2013 p. S82 wording.** Quoted by the SEP only; the fold paraphrases it.
- **Carruthers 2023** ("On valence: imperative or representation of value?", *BJPS* 74(3):533–553). Metadata only (abstract absent from OpenAlex; publisher 403 in the 09-05 session). It is the direct valence-level comparison of the two representational families and should be read before [[valence]] is next deep-reviewed.
- **Milojević & Subotić (2023)**, "Embodied pain, chronic pain, and Grahek's legacy" (*BPA* 36(2):71–?). Downloaded, not read.
- **Positions register**: whether P-MC1 or P-VS2 cite asymbolia against representationalism was not checked.

## Relation to Site Perspective (for the fold)

- **Dualism.** Unaffected in either direction. The representational theories are physicalist in their usual forms, but representationalism as such is not (Aydede 2023). The Map's dualism does not depend on the hedonic account defeating them, and their success would not refute it. The explanatory gap the Map relies on, why any content or command should feel like anything, is general: it applies to the red square as much as to pain. Asymbolia adds nothing distinctively anti-representational to it.
- **Bidirectional Interaction.** Every theory in the table gives pain's (un)pleasantness a motivating or reason-giving role. None supports epiphenomenalism, and the fold must say so (its final sentence). The inseparability claim on the pain page is shared with imperativism and response-dependence, so it is a coherence point and not a discriminator.
- **Occam's Razor Has Limits.** "Both rivals predict asymbolia" is not "therefore representationalism". It leaves the hedonic account where its own arguments put it (reasons, objectless moods), with the dispute open.
- **Minimal Quantum Interaction / No Many Worlds.** Not engaged.

## Citations

1. Aydede, M. (2019). Pain. *Stanford Encyclopedia of Philosophy* (first published 30 Sep 2005; substantive revision 4 Mar 2019). https://plato.stanford.edu/entries/pain/
2. Aydede, M. (2023). Is pain representational? *Belgrade Philosophical Annual*, 36(2), 25–39. https://doi.org/10.5937/bpa2302025a
3. Bain, D. (2011). The imperative view of pain. *Journal of Consciousness Studies*, 18, 164–185. (Volume and pages per the SEP bibliography; issue number not verified.)
4. Bain, D. (2013). What makes pains unpleasant? *Philosophical Studies*, 166(S1), 69–89. https://doi.org/10.1007/s11098-012-0049-7
5. Bain, D. (2014). Pains that don't hurt. *Australasian Journal of Philosophy*, 92(2), 305–320. https://doi.org/10.1080/00048402.2013.822399
6. Bain, D. (2019). Why take painkillers? *Noûs*, 53(2), 462–490. https://doi.org/10.1111/nous.12228
7. Barlassina, L. (2020). Beyond good and bad: Reflexive imperativism, not evaluativism, explains valence. *Thought*, 9(4), 274–284. https://doi.org/10.1002/tht3.471 (subtitle per Crossref)
8. Barlassina, L., & Hayward, M. K. (2019). More of me! Less of me!: Reflexive imperativism about affective phenomenal character. *Mind*, 128(512), 1013–1044. https://doi.org/10.1093/mind/fzz035
9. Carruthers, P. (2023). On valence: Imperative or representation of value? *British Journal for the Philosophy of Science*, 74(3), 533–553. https://doi.org/10.1086/714985
10. Coninx, S. (2020). Pain experiences and their link to action: Challenging imperative theories. *Journal of Consciousness Studies*, 27. (PhilPapers record CONPEA-4; pages unverified.)
11. Corns, J. (2014). Unpleasantness, motivational oomph, and painfulness. *Mind & Language*, 29(2), 238–254. https://doi.org/10.1111/mila.12048
12. Cutter, B., & Tye, M. (2011). Tracking representationalism and the painfulness of pain. *Philosophical Issues*, 21(1), 90–109. https://doi.org/10.1111/j.1533-6077.2011.00199.x
13. Cutter, B., & Tye, M. (2014). Pains and reasons: Why it is rational to kill the messenger. *The Philosophical Quarterly*, 64(256), 423–433. https://doi.org/10.1093/pq/pqu025
14. Duval, A., & Klein, C. (2025 online; 2026 issue). Pain asymbolia is probably still pain. *Philosophy of Science*, 93(1), 221–229. https://doi.org/10.1017/psa.2025.10098
15. Fulkerson, M. (2016). Review of Colin Klein, *What the Body Commands*. *Notre Dame Philosophical Reviews*, 2016.03.05. https://ndpr.nd.edu/news/what-the-body-commands-the-imperative-theory-of-pain/
16. Grahek, N. (2007). *Feeling Pain and Being in Pain* (2nd ed.). MIT Press. https://doi.org/10.7551/mitpress/2978.001.0001
17. Gray, R. (2019; online 2018). On the content and character of pain experience. *Pacific Philosophical Quarterly*, 100(1), 47–68. https://doi.org/10.1111/papq.12261
18. Hall, R. J. (2008). If it itches, scratch! *Australasian Journal of Philosophy*, 86(4), 525–535. https://doi.org/10.1080/00048400802346813
19. Helm, B. W. (2002). Felt evaluations: A theory of pleasure and pain. *American Philosophical Quarterly*, 39(1), 13–30.
20. Jacobson, H. (2013). Killing the messenger: Representationalism and the painfulness of pain. *The Philosophical Quarterly*, 63(252), 509–519. https://doi.org/10.1111/1467-9213.12029
21. Kinakin, M. (2026). Why intentionalists can't take painkillers. *Philosophical Studies*, 183(6), 1905–1929. https://doi.org/10.1007/s11098-026-02523-z
22. Klein, C. (2007). An imperative theory of pain. *The Journal of Philosophy*, 104(10), 517–532. https://doi.org/10.5840/jphil2007104104
23. Klein, C. (2010). Response to Tumulty on pain and imperatives. *The Journal of Philosophy*, 107(10), 554–557. https://doi.org/10.5840/jphil20101071038
24. Klein, C. (2015a). *What the Body Commands: The Imperative Theory of Pain*. MIT Press. https://doi.org/10.7551/mitpress/10480.001.0001
25. Klein, C. (2015b). What pain asymbolia really shows. *Mind*, 124(494), 493–516. https://doi.org/10.1093/mind/fzu185
26. Klein, C., & Duval, A. (2023). Is pain asymbolia a deficit or a syndrome? Historical reflections on an ongoing debate. *Belgrade Philosophical Annual*, 36(2), 41–57. https://doi.org/10.5937/bpa2302041d
27. Martínez, M. (2011). Imperative content and the painfulness of pain. *Phenomenology and the Cognitive Sciences*, 10(1), 67–90. https://doi.org/10.1007/s11097-010-9172-0
28. Martínez, M. (2023). Grahek-style imperativism. *Belgrade Philosophical Annual*, 36(2), 59–70. https://doi.org/10.5937/bpa2302059m
29. Martínez, M., & Klein, C. (2016; online 2015). Pain signals are predominantly imperative. *Biology & Philosophy*, 31(2), 283–298. https://doi.org/10.1007/s10539-015-9514-y
30. Mitchell, J. (2025; online 2024). Towards affective-evaluativism: The intentional structure of unpleasant pain experience. *The Philosophical Quarterly*, 75(2), 693–717. https://doi.org/10.1093/pq/pqae002
31. Noordhof, P. (2021). Explaining impossible and possible imaginings of pain. *Rivista internazionale di Filosofia e Psicologia*, 12(2), 173–182. https://doi.org/10.4453/rifp.2021.0015
32. Nelkin, N. (1994). Reconsidering pain. *Philosophical Psychology*, 7(3), 325–343.
33. Tye, M. (2005). Another look at representationalism about pain. In M. Aydede (Ed.), *Pain: New Essays on Its Nature and the Methodology of Its Study* (pp. 99–120). MIT Press. https://doi.org/10.7551/mitpress/5211.003.0005
