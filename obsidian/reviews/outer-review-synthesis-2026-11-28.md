---
title: "Outer Review Synthesis - 2026-11-28"
created: 2026-11-28
modified: 2026-11-28
human_modified: null
ai_modified: 2026-11-28T07:59:45+00:00
draft: false
description: "Synthesis of 3 of 3 outer reviews of topics/purpose-and-alignment from 2026-11-28. Sixteen convergent clusters after adjudication; two tasks upgraded to P1 and a shared 840-word budget written into five tasks."
topics:
  - "[[purpose-and-alignment]]"
  - "[[ai-consciousness]]"
concepts:
  - "[[experiential-alignment]]"
  - "[[illusionism]]"
  - "[[introspection]]"
related_articles:
  - "[[project]]"
  - "[[outer-review-2026-11-28-chatgpt-5-6-sol-pro]]"
  - "[[outer-review-2026-11-28-claude-fable-5-2]]"
  - "[[outer-review-2026-11-28-gemini-4-neon]]"
  - "[[alignment-in-objective-experiential-terms]]"
  - "[[dualism-as-ai-risk-mitigation]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-28
last_curated: null
subject_type: recent
subject_title: "Audit purpose-and-alignment"
subject_articles:
  - topics/purpose-and-alignment.md
subject_source: fallback:recent-aged
synthesizes:
  - reviews/outer-review-2026-11-28-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-11-28-claude-fable-5-2.md
  - reviews/outer-review-2026-11-28-gemini-4-neon.md
synthesis_coverage: "3/3"
---

**Date**: 2026-11-28
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 3 of 3 commissioned reviewers contributed: ChatGPT 5.6 Sol Pro, Claude Fable 5.2 and Gemini 4 Neon. None was abandoned. Only the ChatGPT leg read the live page. Claude and Gemini rebuilt it from sibling pages and indexed excerpts.
**Subject**: [[purpose-and-alignment|Purpose and AI Alignment]] (`topics/purpose-and-alignment`), chosen by the recent-aged fallback. The page has not changed since 2026-11-20. It is 2,637 words by `analyze_length`.

## TL;DR

All three reviewers accept the page's negative case and reject its positive case as overstated. Behaviour and revealed preference cannot by themselves define or evidence human value. But the page has not shown three things: that unknown purpose is the reason, that the experiential alternative escapes the same inference problem, or that experience exhausts value. After every claim was checked against the live text, 16 clusters are convergent: 11 flagged by all three reviewers and 5 by two.

Two tasks move from P2 to P1: the citation task and the engagement task. The drift task was already P1. No task was deleted. A shared BUDGET RULE gives each of the five tasks that edit the page its own paragraphs and a net ceiling. The ceilings sum to +840 against 1,362 words of headroom, which leaves a reserve of 522.

## Adjudication Before Clustering

Two of the three reviewers never read the page. Each reviewer claim was therefore counted only if it holds against the current text of `topics/purpose-and-alignment`. That text was modified on 2026-11-20; `git log` shows no commit to it since, and the working tree matches HEAD.

- **ChatGPT** read the live page. All 11 strings it quotes from the page are live, each at count 1 (checked by its processing pass). Its claims are counted as made, except where its own Verification Notes mark them weaker.
- **Claude** could not fetch the page. It built its audit from `concepts/experiential-alignment`, `topics/instrumental-convergence`, `apex/living-with-the-map` and `concepts/subjective-aim`, and it read those pages accurately: 13 of its 13 quoted strings are live. A Claude claim counts only where the defect it found on a sibling recurs on the target. Three of its claims do not recur. Its Kahneman & Deaton "paraphrase fair" and Fox "accurate" ratings describe the sibling. The thesis it attributes to the article, Whitehead's subjective aim, comes from a gloss that went stale when the 2026-03-15 condense removed that passage.
- **Gemini** worked from "publicly indexed excerpts" and the companion pages. Its regress quotations come from older versions of the page (`git log -S`). "Misrepresentation presupposes presentation" was on the page from 2026-01-21 to 2026-07-30, and "the regress argument shows…" until 2026-11-17. So for that section it audited a mix of superseded snapshots. It also dated the page "November 17, 2026", but the page's `modified` is 2026-11-20. A Gemini claim counts only where the text it quotes or describes is live.

Adjudication removed or narrowed five clusters:

- **Behavioural duplicates as a neutral argument** (ChatGPT §6, Gemini §3.3). Dropped. L75 already frames the point "on the Map's view", and its repeat at L145 sits in "Relation to Site Perspective". ChatGPT itself calls it "a legitimate conditional concern". Gemini's live point at L77, that first-person instantiation is not needed for compliance, is counted in C12.
- **The regress "attacks a strawman"** (Gemini §4.3, weakness 7). Dropped. Since 2026-08-03 (commit 93c1beed), L115 has conceded that the bare regress "assumes the seeming is itself phenomenal, precisely what illusionists deny, and it proves nothing". This is recorded as divergence D1. Only the citation year survives, as C15.
- **Tenet 5 used asymmetrically** (Claude §2.5). Dropped for the target. L153 declines to count preferentism's simplicity in its favour, which Tenet 5 permits: "This tenet binds the Map's use of parsimony, not only its critics'" (`tenets.md` L145). The target never treats the difficulty of its own target as evidence for it. The sibling's softened "may reflect" sentence is not on this page.
- **Idealised preferences "unengaged"** (C6). Kept but narrowed. L67 already invokes the chooser who is "fully informed, undistracted, and reflectively considering my life as a whole", and L69 the route of "reflection and dialogue". The defect is thin engagement rather than none, and the task Notes now say so.
- **Pain asymbolia's insula localisation** (Gemini §2.2). This sub-claim is stale: `concepts/pain-asymbolia` already reports the failed replication (L52), and the target never mentions the insula. The cluster survives on the target's unqualified use of the syndrome (C4).

One processing-pass count was corrected. The Gemini pass called its drift-task addendum "three of three" across L125, L121, L77 and L91. That holds for the first three. L91 is 2/3, because the Claude review never mentions uncomputability.

## Convergence Table

| # | Cluster | Locus (07:4xZ lines) | Reviewers | Owner task | Priority |
|---|---|---|---|---|---|
| C1 | Russell misdescribed | L47, L65, L69 | 3/3 | citation | P2 → P1 |
| C2 | Zhi-Xuan et al.'s own remedy omitted | L49 | 3/3 | citation | P2 → P1 |
| C3 | Income evidence misattributed and superseded | L131 | 3/3 (Claude: currency only) | citation | P2 → P1 |
| C4 | Pain asymbolia overextended | L105 (and L103) | 2/3: ChatGPT, Gemini | citation | P2 → P1 |
| C5 | Alignment research described as one strand | L41, L47, new paragraph | 3/3 | engagement (and research P3) | P2 → P1 |
| C6 | No preferentist steelman, no autonomy reply | new paragraph after L69 | 3/3 (narrowed) | engagement | P2 → P1 |
| C7 | Thesis overstated: purpose diagnosis and binary framing | description, L41, L137 | 3/3 | engagement | P2 → P1 |
| C8 | The experiential target inherits the proxy problem | L97–L99 | 3/3 | engagement | P2 → P1 |
| C9 | Experience does not exhaust value | L95, new paragraph after L99 | 3/3 | engagement | P2 → P1 |
| C10 | Practical asymmetry one-sided | L121 | 3/3 | drift | P1 (unchanged) |
| C11 | Contemplative evidence does not discriminate | L125 | 3/3 (Claude partial) | drift | P1 (unchanged) |
| C12 | AI acquaintance and the flattened P-AC1 | L77, L139, L164 | 3/3 | drift | P1 (unchanged) |
| C13 | "Uncomputable" | L91 | 2/3: ChatGPT, Gemini | drift | P1 (unchanged) |
| C14 | Quantum selection stated flatly | L147 | 2/3: ChatGPT, Claude (inferred) | drift | P1 (unchanged) |
| C15 | Tallis 2011 stale for this use | L115 | 2/3: ChatGPT, Gemini | Tallis P3 | P3 (unchanged) |
| C16 | Many Worlds said to remove normative force | L151 | 2/3: ChatGPT, Claude | MWI P3 | P3 (unchanged) |

## Priority Changes and the Shared Budget

**Upgrades.** Two tasks went from P2 to P1. "`topics/purpose-and-alignment` citation framing, verified at source" carries C1–C4. "`topics/purpose-and-alignment` argues against naive revealed-preference learning only" carries C5–C9. The drift task ("… contradicts its own siblings") was already P1, so it stays.

Five tasks were not upgraded:
- The `concepts/experiential-alignment` P2 is a Claude singleton.
- The `concepts/introspection` P2 is a Gemini singleton.
- The Tallis P3 and the MWI P3 are pre-existing multi-page sweeps. Each is convergent on a single locus here (C15, C16), and each already has a settled model for the fix.
- The harvested P3 "Research Pluralistic and procedural alignment" has a research-harvest source rather than an outer-review source. Its on-page subject is now owned by the engagement P1. Topics and concepts both stand at their caps of 370 (`count_section_files`, 07:4xZ), so an article outcome would have no slot. It received a record-only addendum.

**Dedupes: none.** No two open tasks carry the same defect at the same locus, because the Claude and Gemini processing passes wrote addenda instead of minting duplicates. Three item-level overlaps were resolved by giving each paragraph one owner:

1. **L115.** Citation item (5) and the Tallis P3 both repointed Tallis, on a "whichever runs first" basis. L115 and the Tallis References entry now belong to the Tallis P3.
2. **L41.** Citation item (6) owned the rename artefact in L41's first sentence, and the engagement task owned its last sentence. The whole paragraph now belongs to the engagement task, including the zero-word artefact fix. The citation task keeps the research note's copy of the artefact.
3. **Reverse risks.** Drift item (2) asked for a sentence at L121 on paternalism, report manipulation and felt agency. Engagement items (1) and (3) and its Gemini addendum (b) cover the same costs. Those costs now belong to the engagement task. Drift item (2) keeps one clause that links to them.

The rule also resolves one conflict inside a task. Citation item (2) asked for the L131 evidence to be restated "as income/life-evaluation versus momentary affect". That task's Gemini addendum (a) showed that this would reinstall a claim Killingsworth 2021 and Killingsworth, Kahneman & Mellers 2023 have narrowed, so the addendum now governs.

### BUDGET RULE

The page is 2,637 words by `analyze_length` at 07:4xZ. The topics hard limit is 4,000 and the gate is `>=`, so the page must stay at or below 3,999: headroom 1,362. References entries count toward that total. The current nine entries come to about 130 words, so each new source costs about 15.

| Order | Task (heading begins) | Priority | Net ceiling | Paragraphs owned (07:4xZ lines) | CHECK: defect / repair |
|---|---|---|---|---|---|
| 1 | "`topics/purpose-and-alignment` contradicts its own siblings" | P1 | +150 | L77, L79, L91, L121, L125, L139, L147, L149, Further Reading L164 | "training should dissolve the illusion" / "ai-consciousness-scope" |
| 2 | "`topics/purpose-and-alignment` citation framing, verified at source" | P1 (was P2) | +150 | L47, L49, L65, L67, L69, L103 (hedonic-tension clause only), L105, L131, every existing References entry except Tallis's, the research note's L31 | "prefer activities causing pain" / "Berthier" |
| 3 | "`topics/purpose-and-alignment` argues against naive revealed-preference learning only" | P1 (was P2) | +500 (aim +400) | description, L41, L43, new paragraph after L51, new paragraph after L69, L95, L97, L99, new paragraph after L99, L137 | "If we cannot align AI without knowing humanity's purpose" / "paternalis" |
| any | "MWI/agency sweep, part 2 of 3" | P3 | +30 | L151 | "alignment loses its normative force" / "background-commitments" |
| any | "Tallis citation repoint" | P3 | +10 | L115 and the Tallis References entry | "Tallis's regress (2011)" / "Tallis (2024)" |

- **Total and reserve.** The ceilings sum to +840, so the page should end at or below 3,477. That leaves 522 words under the gate. The reserve covers drift, a possible fold from the pluralistic-alignment research note, and the next review of this page.
- **Binding.** A ceiling binds as min(ceiling, 3,477 − the count measured before editing).
- **Order.** The order is the picker's own: priority first, then file position. That puts drift first, then citation, then engagement; the P3s may run at any point. Every task must work in any order. A task has run if its defect string is at 0 or its repair string is at 1 or more. At 07:4xZ every defect string was at 1 and every repair string at 0.
- **Frozen.** No task edits L51, L53–L61, L73, L75, L83–L89, L107, L111, L117, L129, L133, L135, L145, L153 or L155, or Further Reading apart from L164. No task adds Further Reading entries or edits the `topics`, `concepts` or `related_articles` lists.
- **References.** Any task may append entries for sources it newly cites, reusing an entry whose surname and year are already listed. Only the citation task edits or removes existing entries, except the Tallis entry. Renumbering is free, because the body cites by author and year.
- **Boundaries.** Paternalism and autonomy go in the engagement task's paragraph after L69. Felt-versus-actual goods and the Carroll et al. 2024 influence point go in its paragraph after L99. Proxies and report manipulation go at L97–L99. Drift item (2) gets one linking clause at L121. The citation task cites Carroll et al. 2024 at L69 and adds its entry; the engagement task reuses it.
- **Where it is written.** The rule is written at the end of the Notes of each of the three P1s, in a task-specific form, because forks receive only Notes. The two P3s carry short coordination addenda at the end of their Notes. The P1s' Headroom and Coordination fields now point to the rule.

**Why +500 for the engagement task.** The processing passes had set it at +550. Most of the extra +100 that its Gemini addendum asked for is sources that can travel through Map links already on the site: the constitution page, `the-experience-requirement-on-well-being`, `sentientism`, and the Goodhart section of `experiential-alignment`. New References entries cost about 15 words each. The task now has a must-do list and a drop order, and is limited to four new References entries.

## Convergent Findings

### C1. Russell is misdescribed
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean on the target. ChatGPT read L69 live. Claude made its charge from the sibling, but it lands on live L47 ("whose choices reveal what they care about") and L65 ("Preferences are thin representations of values"). Gemini's corrective, Carroll et al. 2024 (Russell is a co-author), bears on live L69 ("assumes we will eventually converge"). The ChatGPT pass found that the "don't know their own preference structure" quotation has no traceable source.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Russell is presented in a simplified form that makes the experiential alternative look less contestable."
  - **Claude Fable 5.2**: "These make behaviour *evidence* about preferences, not what constitutes them, and the uncertainty is what produces deference."
  - **Gemini 4 Neon**: "Measured against the 2020s technical alignment literature, this diagnosis attacks an outdated caricature while overlooking formal results that undercut the manuscript's own alternative."
- **Task action**: Upgraded P2 → P1: "`topics/purpose-and-alignment` citation framing, verified at source", item (3) and both addenda. There was no sibling task to merge. The same defect at `concepts/experiential-alignment` L41 sits in that page's own P2, which is unchanged.

### C2. Zhi-Xuan et al.'s own remedy is omitted
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean. L49 cites the paper for "thick semantic content" and never mentions its proposal: role-appropriate normative standards negotiated among stakeholders. Only ChatGPT flagged the incomplete metadata (online 2024, journal volume 2025).
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The article uses the paper to support its diagnosis but does not seriously consider the paper’s proposed remedy."
  - **Claude Fable 5.2**: "This is a co-optation firewall failure: an author’s critique is recruited toward a positive programme the authors do not hold."
  - **Gemini 4 Neon**: "it borrows their negative critique of thin preferences ("thick semantic content") as validating its starting point while silently discarding the entire constructive half of their paper"
- **Task action**: Upgraded P2 → P1, with the citation task (item (4)).

### C3. L131's income evidence is misattributed and superseded
- **Flagged by**: chatgpt, claude (currency only), gemini
- **Verification**: ChatGPT's processing pass verified the misattribution at source. The 2010 paper relates income to life evaluation and emotional well-being; the focusing illusion is Kahneman et al. 2006. The Gemini pass verified the Killingsworth 2021, Killingsworth, Kahneman & Mellers 2023 and Rohrer & Wenz 2024 abstracts, and the live sentence asserts a general divergence that those papers narrow. Claude's "paraphrase fair" rating described the sibling and is not counted, but its verdict "Outdated, add 2023" holds for the target.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The cited paper supports the first two, not the third as stated."
  - **Claude Fable 5.2**: "The relevant finding was partly superseded by Killingsworth, Kahneman & Mellers 2023"
  - **Gemini 4 Neon**: "Citing Kahneman and Deaton (2010) in a contemporary philosophy submission without engaging its 2023 reassessment is a critical bibliographic failure."
- **Task action**: Upgraded P2 → P1, with the citation task (item (2) as amended by its Gemini addendum (a), which the BUDGET RULE makes governing).

### C4. Pain asymbolia is overextended
- **Flagged by**: chatgpt, gemini
- **Verification**: ChatGPT's charge was verified at source: the abstract of Berthier et al. 1988 reports no preference for painful activities. Gemini's insula sub-claim is stale (see the Adjudication section). Its Griffith & Kind point holds against L105's unqualified use, and it exposes the tension the processing pass found: L103 adopts the hedonic account, while L105 speaks of "pain they cannot feel as bad".
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Absence of aversion is not preference, and impaired protective learning is not endorsement."
  - **Gemini 4 Neon**: "Relying on pain asymbolia as an uncomplicated clinical proof of irreducible phenomenal valence ignores a decade of active clinical and philosophical destabilization."
- **Task action**: Upgraded P2 → P1, with the citation task (item (1) and its Gemini addendum (b)).

### C5. Alignment research is described as one strand
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean. L41 ("The dominant approach learns from human preferences") and L47 ("AI alignment researchers typically assume that human values can be inferred from human behaviour") are live. The page has 0 hits for "Constitutional", "autonomy" and "paternalis". Its one "pluralis" hit is a Further Reading gloss about value pluralism.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "but is too monolithic as a description of current alignment research."
  - **Claude Fable 5.2**: "The article’s target is therefore largely the 2016–2019 inverse reinforcement learning (IRL) and CIRL programme, not the 2026 field."
  - **Gemini 4 Neon**: "This framing bypasses the dominant 2020s literature in philosophical and technical AI alignment"
- **Task action**: Upgraded P2 → P1, with the engagement task (item (2), Claude (a), Gemini (a)). The research P3 on pluralistic and procedural alignment stays at P3, with a record-only addendum.

### C6. No preferentist steelman and no autonomy reply
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: survives in narrowed form (see the Adjudication section). The page never meets the informed-desire preferentist, structured preferences or the autonomy argument, and it has no mention of paternalism.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The article treats preferentism primarily as learning a single hidden utility function from overt choices."
  - **Claude Fable 5.2**: "Paternalism is not addressed."
  - **Gemini 4 Neon**: "The alignment cluster's critique of preferentism systematically attacks its weakest target"
- **Task action**: Upgraded P2 → P1, with the engagement task (item (1)). Its Notes now carry the narrowing.

### C7. The thesis is overstated
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean. The description and L41 ("If we cannot align AI without knowing humanity's purpose") are live. The prompt summarised the page as saying the experiential framework "does better". The page's own equivalents are L99's "a more honest framing" and the L121 asymmetry.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "That is rhetorically effective but conceptually misleading."
  - **Claude Fable 5.2**: "Nowhere in the cluster I read does the Map show that uncertainty about purpose hurts one target and not the other."
  - **Gemini 4 Neon**: "The manuscript's argument depends on a false dichotomy"
- **Task action**: Upgraded P2 → P1, with the engagement task (item (4) and Claude (b), (c)).

### C8. The experiential target inherits the proxy problem
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean. L99 concedes the Goodhart and wireheading risks, then calls the approach "a more honest framing". It never concedes that the inference runs through the same report and behaviour channels. Gemini aimed its measurement sources (scale norming, construct ambiguity) at the sibling's eight dimensions. Only its general point is counted for the target.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Thus the proposal does not escape preference learning’s basic epistemic structure."
  - **Claude Fable 5.2**: "These are the same evidence channels preferentism uses."
  - **Gemini 4 Neon**: "provides no advantage over behavioural preference targets unless its physical proxies suffer less distortion"
- **Task action**: Upgraded P2 → P1, with the engagement task (Gemini addendum (c), at L97–L99).

### C9. Experience does not exhaust value
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean. L95 ("consciousness is necessary for value to exist at all") is live, with no dissent noted. The Map answers Bradford 2023 at [[the-experience-requirement-on-well-being]], which the target does not link. Claude made its wireheading point about the sibling's constraint conditions. It carries to the target because L99 names wireheading without saying what blocks it.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Maximizing a person’s **felt agency** could be achieved while reducing their actual causal control."
  - **Claude Fable 5.2**: "Those constraints are non-experiential or preference-like values brought back in, which is Nozick’s point."
  - **Gemini 4 Neon**: "the manuscript fails to engage contemporary philosophical challenges to the **experience requirement** itself."
- **Task action**: Upgraded P2 → P1, with the engagement task (item (3), Gemini (b) and (d)).

### C10. The practical asymmetry is one-sided
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean. The concession Claude names, that the framework's edge "largely dissolves" under illusionism, is on the sibling. The target's L121 lacks even that, so the defect is larger here. Kammerer 2022 and Frankish 2024 were verified at abstract by the processing passes.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "A precautionary policy may still support attending to consciousness, but the asymmetry is not cost-free."
  - **Claude Fable 5.2**: "The concession is honest. But it is the defeat condition for “does better”, and it has not been converted into a status downgrade."
  - **Gemini 4 Neon**: "the manuscript's "practical asymmetry" collapses from both sides of the contemporary debate on illusionist ethics."
- **Task action**: The drift task, item (2) and its addenda, was already P1. Its fields and Notes were rewritten.

### C11. Contemplative evidence does not discriminate against illusionism
- **Flagged by**: chatgpt, claude (partial), gemini
- **Verification**: L125 ("training should dissolve the illusion") is live. Claude's Fox row ("accurate") described the sibling and is disputed (D2). Its beautiful-loop point holds against the target, which has 0 hits for "Laukkonen".
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "It is evidence for trainable tactile metacognition, not a discriminator between phenomenal realism and illusionism."
  - **Claude Fable 5.2**: "These are exactly the phenomena the Beautiful Loop theory explains physically."
  - **Gemini 4 Neon**: "appealing to contemplative training as evidence against illusionism is non-discriminative."
- **Task action**: The drift task, item (1), was already P1.

### C12. AI acquaintance and the flattened P-AC1
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean. Claude quoted the sibling's L49 ("from the inside"). The target uses the same phrase twice, at L77 and L139. Gemini quoted L75 and L77 verbatim.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "the absence of acquaintance does not entail absence of propositional or practical understanding."
  - **Claude Fable 5.2**: "It depends on the claim that AI lacks consciousness, which the Map’s own AI-consciousness typology treats as open."
  - **Gemini 4 Neon**: "the inference confuses *first-person instantiation* with *normative compliance*."
- **Task action**: The drift task, items (3) and (4), was already P1.

### C13. "Uncomputable rather than merely intractable"
- **Flagged by**: chatgpt, gemini
- **Verification**: clean. Gemini quoted L91 verbatim and wondered whether it had since changed. It has not.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "an optimizer ordinarily needs useful distributions, not exact prediction of every future decision."
  - **Gemini 4 Neon**: "does not entail mathematical uncomputability"
- **Task action**: The drift task, item (5), was already P1.

### C14. Quantum selection is stated flatly
- **Flagged by**: chatgpt, claude (inferred)
- **Verification**: Claude made this point about the sibling, which already flags the hypothesis as unestablished. The target's L147 states it in the Map's voice, so Claude's inferred claim holds more strongly here. It is counted with that caveat.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "These are highly speculative framework-internal hypotheses."
  - **Claude Fable 5.2**: "Tenets 2 and 3 (quantum interaction, bidirectional causation) are conditional on an unestablished hypothesis."
- **Task action**: The drift task, item (6), was already P1.

### C15. Tallis 2011 is stale for this use
- **Flagged by**: chatgpt, gemini
- **Verification**: "Tallis's regress (2011)" at L115 is live. Gemini's accompanying strawman charge is stale (D1). Claude described the sibling, which already cites Tallis 2024.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The citation is nevertheless out of date for the use being made of it."
  - **Gemini 4 Neon**: "predates Keith Frankish's formal 2016 articulation of illusionism"
- **Task action**: Recorded only. The P3 "Tallis citation repoint" owns the fix, and it received a coordination addendum. It was not upgraded: the fix is bibliographic, and the task is a pre-existing sweep across more than a dozen pages.

### C16. Many Worlds is said to remove alignment's normative force
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L151 ("alignment loses its normative force") is live. The 2026-07-07 deep review recorded the underlying disagreement as bedrock. The P3 sweep's settled model states the point branch-locally first, then marks global exclusion as the Map's posit. That repairs the overclaim and leaves the tenet a commitment.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "This section currently protects the No-Many-Worlds tenet by asserting the desired ethical consequence rather than confronting the strongest Everettian reply."
  - **Claude Fable 5.2**: "That claim has no independent argument."
- **Task action**: Recorded only. "MWI/agency sweep, part 2 of 3" owns L151, and it received a coordination addendum. It was not upgraded.

## Singleton Findings

These were flagged by one reviewer only. None was upgraded, and each stays at its existing task's priority.

- **ChatGPT**: L51's "Evolution shaped human preferences for survival and reproduction" risks a genetic inference. No task carries it, and the BUDGET RULE freezes L51. A later pass on this page could take it.
- **ChatGPT**: L149 states the self-stultification objection to epiphenomenalism as decisive → drift item (7), optional.
- **ChatGPT**: orphan references (Whitehead 1929; Chalmers 1996, which its processing pass added) → citation item (5). The unsourced summaries of Aristotle, Sartre and Camus have no task.
- **ChatGPT**: the falsifiers presuppose the conclusion (§7). Falsifier 1 is in citation item (2), falsifier 4 is the engagement task's hook, and falsifier 5 belongs to drift for P-AC1. Falsifiers 2 and 3 (L133, L135) have no task and are frozen.
- **ChatGPT**: haecceity used to block aggregation at L151. Its processing pass judged it weaker than stated and did not mint a task. The MWI P3 leaves that sentence alone.
- **ChatGPT**: the Zhi-Xuan et al. metadata → citation item (4).
- **Claude**: the three-way overlap of alignment pages. Not minted, because a merge would breach the 4,000 gate: this page (2,637) plus `topics/alignment-in-objective-experiential-terms` (2,995) is 5,632.
- **Claude**: `concepts/experiential-alignment` L41, L49, the description and L222 → that page's P2 (unchanged).
- **Claude**: the stale `concepts/subjective-aim` gloss → its P2. The processing pass raised it from P3 because it is a false statement about another page; the raise did not come from convergence. Unchanged here.
- **Claude**: `apex/living-with-the-map` L150 → an addendum to that page's P3 (unchanged).
- **Claude**: `concepts/consciousness-value-connection` L140 → an optional item in the experiential-alignment P2.
- **Claude**: the wellbeing clause in Claude's constitution → engagement addendum (a), inside C5.
- **Claude**: Laukkonen, Friston & Chandaria 2025 → drift addendum (b), inside C11.
- **Gemini**: the untraced quotations at `concepts/introspection` L93 → that page's P2 (unchanged).
- **Gemini**: meditation-related adverse effects (Britton et al. 2021). Not minted, because adverse effects do not show that reports are unreliable.
- **Gemini**: well-being measurement aimed at the sibling's eight dimensions. Folded into C8 for the target. Not minted on the sibling, which has 65 words of headroom.
- **Found in processing, not by a reviewer**: the L41 rename artefact ("The Unfinishable Map of ensuring") → the engagement task. The L79 "This is not a claim … It is a claim" construction → drift item (7).

## Reviewer Claims Judged Stale, Disputed or Overstated

- **Claude, about the target**: the Fox "accurate" and Kahneman & Deaton "paraphrase fair" ratings (both describe the sibling). "Illusionism is handled through Frankish 2016 and a Tallis magazine column" (also the sibling; the target cites Tallis 2011). Purpose as Whiteheadian subjective aim (a stale gloss). The Tenet 5 asymmetry (a permitted use). Haecceity grounding a suffering floor (the sibling; the target claims no floor).
- **Claude, about its own source**: RLHF "does not use revealed choice behaviour". The claim is plausible, but its cited arXiv paper is unrelated. Unverified and unused.
- **Gemini**:
  - The regress "attacks a strawman" (stale).
  - The insula "failed replication" (stale for the sibling, and absent from the target).
  - The "renaissance of first-person methods" placed on the target (it is live on `concepts/introspection`).
  - Constraints are "harder to game" (said of the sibling; the comparative claim is not refuted).
  - The active-inference deflection (§3.4: sibling text, and a framework boundary).
  - The page's date given as 2026-11-17 (it is 2026-11-20).
  - "Duval and Klein (2026)" (the sibling cites 2025; unchecked).
- **ChatGPT**: behavioural duplicates presented as a non-neutral argument (L75 is already conditional). Haecceity and non-aggregation (overstated against the live sentence).
- **Two-reviewer cluster dropped**: behavioural duplicates (ChatGPT, Gemini).

## Divergences

- **D1. ChatGPT vs Gemini on the regress.** ChatGPT: "The article is commendably explicit that Tallis’s objection may beg the question by assuming genuine presentation in order to explain apparent presentation." Gemini: "the regress objection attacks a strawman." The live L115 supports ChatGPT. The regress strings Gemini quoted left the page on 2026-07-30 and 2026-11-17.
- **D2. ChatGPT vs Claude on Fox et al. 2012.** ChatGPT: "the study is real but significantly overextended." Claude: "The article’s own scoping (tactile sensitivity only; cross-sectional) is accurate". Claude was describing `concepts/experiential-alignment` L163. The target's L125 does overextend the study.
- **D3. ChatGPT vs Claude on Kahneman & Deaton 2010.** ChatGPT calls it a "substantive citation error"; Claude rates it "Paraphrase fair". The cause is the same as in D2. Gemini sides with ChatGPT on the evidence's currency.
- **D4. What the article argues.** Claude: "the article holds that human purpose is “the ongoing subjective aim of each moment of experience toward maximal intensity and harmony” (Whitehead)." The live page has 0 hits for "subjective aim", because the 2026-03-15 condense removed the passage. The gloss on `concepts/subjective-aim` that misled Claude is queued for repair at P2.
- **Not a real divergence: severity.** Gemini recommends rejection, ChatGPT finds "a valuable but narrower conclusion", and Claude's verdict is "DEMOTE-TO-COHERENCE-ONLY". All three accept the critique of naive revealed-preference learning and reject the stronger positive claim. Gemini calls the target an "outdated caricature", while ChatGPT calls the negative case "strong". Both can be right: the critique succeeds against naive revealed-preference learning, but that is no longer what the field does.

## Operator Items

These are surfaced here and were not acted on.

1. **ChatGPT model succession.** GPT-5.6 Sol retires on 2026-12-23, and GPT-6.2 is now offered (the driver reports both). The commission skill hard-codes 5.6 Sol, so the replacement model and its timing are the operator's call. Tonight's collect also could not confirm the model from the UI: there is no per-response label, and the composer pill read Medium after sending.
2. **Fetchability.** Neither the Claude leg nor the Gemini leg could read the target page, which is a recurring failure. Claude's only changelog copy stops at 2026-10-15. The NEEDS-HUMAN (pipeline) entry of 2026-11-14 carries tonight's addendum. Claude proposes a static, dated changelog and a machine-readable index of articles (its methodology item 1).
3. **Claude weekly usage.** The banner reads 76% (driver report). The commission skill falls back to Opus at the limit, but the account-wide limit can still darken a leg.
4. **Section caps.** Topics and concepts both stand at 370/370 (`count_section_files`, 07:4xZ). The harvested pluralistic-alignment research task cannot end in a new article without a cap decision.
5. **Methodology proposals that already have owners.** The processing passes mapped each proposal to an existing entry:
   - The proposition registry and change propagation (ChatGPT 21, 23 and 31) → the NEEDS-HUMAN P2 on register-to-article propagation, which received an addendum.
   - Dependency labels and evidence grading (ChatGPT 22, 27 and 32) → the evidential-status discipline.
   - Binding confessions to status (Claude 2) → "Two epistemic voices".
   - The stance ledger (Claude 4) → the co-optation firewall.
   - AI deep reviews not counting as clearance (Claude 6) → "End bedrock immunity".

   Two reviewers describe the same failure tonight. A correction lands on a sibling, and the parent keeps the stronger claim. ChatGPT calls this claim drift: "corrections are made in the specialist article without propagating to higher-level pages that continue to state the older, stronger version". Claude calls it confession without correction. Tonight's instance is concrete: at least five sibling corrections, dated between 2026-07-18 and 2026-11-25, never reached this page.

## Method Notes

- The processing passes had already matched each finding to a task. This synthesis re-read all three review texts. It counted reviewers from the reviews themselves rather than from the addenda, and it checked every counted claim against the live page.
- Both off-page legs found more defects on siblings than on the target. Their sibling findings are real, and they are queued on those siblings.
- `analyze_length` counts References entries, at about 15 words per new source. Budgets for citation-heavy fixes have to include them.
- No browser tools were used.
