---
title: "Outer Review Synthesis - 2026-11-25"
created: 2026-11-25
modified: 2026-11-25
human_modified: null
ai_modified: 2026-11-25T06:08:33+00:00
draft: false
description: "Synthesis of 3 of 3 outer reviews of concepts/valence from 2026-11-25. Seven convergent clusters on one page, five flagged by all three reviewers; six tasks upgraded P2 to P1, none merged."
topics:
  - "[[emotion-and-dualism]]"
  - "[[valence-as-a-natural-kind]]"
  - "[[predictive-processing-and-dualism]]"
concepts:
  - "[[valence]]"
  - "[[pain-asymbolia]]"
  - "[[philosophical-zombies]]"
  - "[[sentientism]]"
related_articles:
  - "[[project]]"
  - "[[outer-review-2026-11-25-chatgpt-5-6-sol-pro]]"
  - "[[outer-review-2026-11-25-claude-fable-5-2]]"
  - "[[outer-review-2026-11-25-gemini-4-neon]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-fable-5-2
ai_generated_date: 2026-11-25
last_curated: null
subject_type: recent
subject_title: "Audit valence"
subject_articles:
  - concepts/valence.md
subject_source: fallback:recent-aged
synthesizes:
  - reviews/outer-review-2026-11-25-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-11-25-claude-fable-5-2.md
  - reviews/outer-review-2026-11-25-gemini-4-neon.md
synthesis_coverage: "3/3"
---

**Date**: 2026-11-25
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 3 of 3 commissioned reviewers contributed; none abandoned or failed.
- ChatGPT 5.6 Sol Pro (`chatgpt-5-6-sol-pro`), processed 04:51Z, minted 7 tasks. [Conversation](https://chatgpt.com/g/g-p-695a7d60af5481919d5c22ad7bcc1648-the-unfinishable-map/c/6b0641c4-3370-83eb-acb6-093a736cbd9c).
- Claude Fable 5.2 (`claude-fable-5-2`), processed 05:22Z, minted 3 tasks and appended 5 addenda. [Conversation](https://claude.ai/chat/fa88ee17-f587-4e30-b6cc-1e71afc7c1df).
- Gemini 4 Neon, High, Deep Research (`gemini-4-neon`), processed 05:39Z, minted 1 task and appended 7 addenda. [Conversation](https://gemini.google.com/app/546c556d7f5918ff).

**Subject**: one article, `concepts/valence` ("Audit valence", the recent-aged fallback; the Claude and Gemini legs reused the subject ChatGPT drew at 02:00Z). All three reviewed the same page on the same day, so same-page convergence is possible throughout, unlike the full-site cycle of 2026-11-24.

## TL;DR

All three reviewers found that the active-inference paragraph of `concepts/valence` credits a nociceptive valence-prior model of asymbolia to Joffily and Coricelli (2013) and Hesp et al. (2021), neither of which gives it. That is the cycle's dominant finding and it was already P1. Six further issues on the same page are convergent after adjudication (four at 3 of 3, two at 2 of 3) and their tasks move from P2 to P1. Four tasks stay P2 as single-reviewer findings, including the cycle's most distinctive single point, Gemini's on the zombie sentence.

**Cluster count**: 7 convergent (5 three-reviewer, 2 two-reviewer), 4 singleton tasks, 6 divergences, 9 reviewer charges judged false alarms or overstated.

**Task actions**: 6 upgrades (P2 → P1), 0 merges, 0 new tasks. The seven convergent tasks were rewritten in place with a convergence header, a `Review files` line, a `Synthesis` line and a binding word ceiling; every existing field and addendum is kept. `parse_tasks` active count: 508 before, 508 after.

## Adjudication Before Clustering

Each issue was checked against the live Obsidian source before it was counted. `concepts/valence` is unchanged since 2026-11-17 (2,474 words by `analyze_length`), so every passage the three reviewers quote from it is the passage now on the page. The dependency pages are a different matter.

- **The Claude leg read search-index copies of eight dependency pages**, and says so. Two of its cross-page charges fail on the live pages:
  - `apex/minds-without-words` is said to call asymbolia "decisive against the evaluativist reduction" and to say it "settles this specific dispute". Live: "settles this specific dispute" 0, "decisive against" 0, "narrows this specific dispute" 1 (L111). The wording was withdrawn on 2026-11-10.
  - `concepts/reductionism` is said possibly still to carry the "seek treatment" sentence. Live: 0 occurrences.
  - Neither charge was shared by another reviewer, so no false convergence arose from the stale copies. The Claude leg's findings about `concepts/valence` itself rest on the live page.
- **The ChatGPT and Gemini legs read the live page.** Each processing pass found the reviewer's Map quotations on the page.
- **Shared-error check.** The one finding all three share that depends on an external source is the Hesp et al. misattribution. It was checked independently of the reviewers at abstract depth (OpenAlex, DOI 10.1162/neco_a_01341: a T-maze simulation; no occurrence of "pain", "nocicept" or "asymbolia"), and against the Map (`topics/predictive-processing-and-dualism` contains none of Hesp, Joffily or asymbolia). The convergence is real at that depth. The body of the paper was not read, so any statement about what the body says remains a lead.
- **A shared under-reading, not counted.** ChatGPT and Claude both say the Map holds incompatible positions on moral status. Both processing passes judged that an under-reading: `positions/moral-status` (P-MS1) separates who can be wronged from what bears intrinsic value, so P-VS4's pluralism about value does not contradict a necessity claim about moral status. Two reviewers making the same under-reading is correlated error. The moral-status cluster is counted only on the part that survives (see C3).
- **Re-checked live in this run** (fixed-string, Obsidian, about 06:00Z):
  - `concepts/valence`: "illusionis" 0, "higher-order" 0, "Kammerer" 0, "LeDoux" 0, "Berridge" 0, "wanting" 0, "born-preserving" 0, "Gerrans" 0, "Hagiwara" 0, "Klein (2015)" 0, "attitudinal" 0, "Smithies" 1 (the reference entry, "forthcoming"). Positive controls on the same page: "Panksepp" and "Hesp" both present.
  - `concepts/pain-asymbolia` L40: "do not withdraw, guard injured limbs, or show distress" 1.
  - `topics/emotion-and-dualism` L57: "the strongest empirical case for interactionist dualism" 1, "resist every attempt at functional reduction" 1; L229 "forthcoming" 1.
  - `apex/born-preserving-causal-efficacy` L101: "compensation consequence" 1, "conservation law on outcome-luck" 1.
  - `concepts/philosophical-zombies`: heading "The Interactionist Escape" at L159; "standalone" at L165.
- **Lengths** (`analyze_length`, gate `>=`): `concepts/valence` 2,474 of 3,500; `concepts/pain-asymbolia` 3,283 of 3,500; `topics/emotion-and-dualism` 3,465 of 4,000; `concepts/philosophical-zombies` 3,497 of 3,500.

## Convergence Table

"Survives" means the reviewer's version of the issue holds against the live page and the processing pass's source checks. Only surviving versions are counted.

| ID | Issue on `concepts/valence` | ChatGPT | Claude | Gemini | Count | Task action |
|---|---|---|---|---|---|---|
| C1 | Active-inference paragraph credits a nociceptive valence-prior model of asymbolia to sources that do not give it | §2.6, item 1: survives | §2.1 C8, row 7: survives | weakness 4: survives ("partially disconfirmed empirically" is an unread lead) | 3/3 | Already P1; rewritten in place, goes first |
| C2 | Asymbolia stated as a clean subtraction; behaviour "tracks" the felt badness | §2.7, item 6: survives | §2.1 C7: survives (Klein's common cause unnamed) | weakness 3: survives on the shorthand and the inverse dissociation; cohort figures unverified | 3/3 | P2 → P1 |
| C3 | Necessity sentence unmarked; Smithies uncited and still "forthcoming" | §2.8, items 7 and 10: survives on marking and reference; "three positions" does not | §2.1 C9, §2.4 I2–I3: survives on marking and orphan reference; "contradicts P-VS4" does not | weakness 8, row 6: survives on the sentence and Smithies; "falsely claims" about invertebrates does not | 3/3 | P2 → P1 |
| C4 | Panksepp has no rival reading; no illusionist account is named | §2.3, §2.5, items 2 and 5: both survive | §2.1 C4: Panksepp survives; illusionism not raised | weaknesses 2 and 7: both survive | 3/3 on Panksepp, 2/3 on illusionism | P2 → P1 |
| C5 | Own-voice "common evaluative dimension"; "structurally irresolvable"; "supports … at multiple points" | §2.1, items 3–4: survives | §2.1 C2, C6, C11, §2.4 I5: survives | weakness 1: survives for the sentence in "What Valence Is"; the tenet-section instance does not | 3/3 | P2 → P1 |
| C6 | The reasons argument does not separate the hedonic account from reflexive imperativism | not raised | §2.1 C5, fix 5: survives | weakness 6: survives on painkillers; the moods half is unverified | 2/3 | P2 → P1 |
| C7 | "Three Competing Accounts" presented as the field | not raised (calls the taxonomy "improved but incomplete") | §2.3, fix 4: survives (attitudinal theories; no citation) | weakness 6: survives (dispositional hybrid theories; Pallies 2021, metadata only) | 2/3 | P2 → P1 |
| S1 | Zombie sentence unconditional beside the causal-work claim | mentions the zombie in passing only | not raised | weakness 7: survives for the page, not for the Map | 1/3 | Left at P2 |
| S2 | Minimal Quantum Interaction paragraph omits the compensation consequence | calls the paragraph well calibrated; objects only to "currency" | §2.4 I4, fix 8: survives | raises a different point (asymmetric standard) | 1/3 | Left at P2 |
| S3 | Lead of `concepts/pain-asymbolia` categorical | item 13: survives | not raised (its fix 13 asks for a different line) | not raised | 1/3 | Left at P2 |
| S4 | Lead of `topics/emotion-and-dualism` over-states | item 12: survives | not raised | not raised | 1/3 | Left at P2 |

## Priority Ordering

The nine `concepts/valence` tasks share 1,025 words of headroom. The order below and the ceilings are written into the tasks themselves: the full table sits in the Notes of the C1 task, and each convergent task carries its own position and ceiling at the head of its Notes. The ceilings are net words by `analyze_length` and sum to 820, leaving 205 in reserve. The queue picks by priority, so the order is advice and the ceilings are what bind.

| Order | Task | Priority | Ceiling | Why here |
|---|---|---|---|---|
| 1 | C1 active-inference misattribution | P1 | +70 | A source-characterisation error; the rest of "Valence and Causal Work" depends on what the rival is said to be |
| 2 | C2 asymbolia shorthand and "tracks" | P1 | +60 | Same section as C1; follows the re-attribution |
| 3 | C6 reasons argument and reflexive imperativism | P1 | +150 | The page's main positive argument for the hedonic account |
| 4 | C7 "Three Competing Accounts" framing | P1 | +90 | Renames the heading the reasons subsection sits under |
| 5 | S1 zombie conditional | P2 | +45 | Small; settles the hard-problem section before the larger edit |
| 6 | C4 illusionist account and Panksepp companion | P1 | +250 | Largest; same section as S1 |
| 7 | C5 own-voice wording | P1 | +30 | A wording pass over sentences C4 sits beside |
| 8 | C3 necessity sentence and Smithies | P1 | +90 | Moral-status section and reference list; independent of the others |
| 9 | S2 compensation clause | P2 | +35 | One clause and one link in the tenet section |

Five ceilings were raised from the figures set at mint (C1 from +40, C2 from +30, C3 from +60, C7 from +80, C5 from near zero), because the later addenda enlarged those tasks. C4, C6, S1 and S2 are unchanged.

## Convergent Findings

### C1. Active-inference paragraph misattributes the asymbolia model
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean at abstract depth. The reviewers' further statements about the body of Hesp et al. are unverified.
- **Live passage**: "valence is a precision-weighted signal of expected value: a prior over the nociceptive stream that drives avoidance-policy selection, on which asymbolia is disrupted valence-prior assignment with sensory processing intact, predicting exactly this dissociation".
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "At present the paragraph attributes a pain-specific lesion model to two papers that do not present it."
  - **Claude Fable 5.2**: "Neither Joffily & Coricelli nor Hesp et al. models nociception or asymbolia."
  - **Gemini 4 Neon**: "even though Hesp et al. (2021) never mention nociception or pain asymbolia"
- **What each added**: ChatGPT, that "expected value" is loose for the formalism. Claude, that the residual the Map rests on is the general hard problem and gives no valence-specific advantage. Gemini, a real source for an active-inference account of asymbolia already on the Map (Gerrans 2020, abstract verified; a self-modelling account, which differs from a valence prior over the nociceptive stream).
- **Task action**: Already P1, left at P1: "`concepts/valence` active-inference paragraph credits a nociceptive valence-prior model of asymbolia…" (one task from the start; rewritten in place).

### C2. Asymbolia as a clean subtraction
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean on the shorthand. Gemini's figures for the Schilder and Stengel series are unverified and excluded.
- **Live passage**: "patients with intact sensory pain processing but absent felt badness do not avoid painful stimuli with normal urgency"; "what the behavior tracks".
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Replace the pristine “intact processing minus badness” description with the classificatory, lesion and self-model qualifications now present in the specialist page."
  - **Claude Fable 5.2**: "The page mentions “the lesion’s common-cause reading” only in passing and never states the datum that makes it compelling."
  - **Gemini 4 Neon**: "The manuscript treats pain asymbolia as a pristine subtraction of felt badness from intact sensory pain and asserts that avoidance behavior tracks felt badness"
- **Note**: the three bring three different missing qualifications, each already carried by `concepts/pain-asymbolia`: the classification dispute, Klein's common cause, and the inverse dissociation (Hagiwara et al. 2020, abstract verified). The specialist page was corrected and the parent was not.
- **Task action**: Upgraded P2 → P1: "`concepts/valence` still describes asymbolia as "intact sensory pain processing but absent felt badness"…".

### C3. Necessity sentence and the Smithies reference
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean on the surviving part; disputed on the "incompatible positions" charge (ChatGPT and Claude) and on the invertebrate charge (Gemini).
- **Live passage**: "But valence provides the necessary condition: without felt badness, there is nothing for moral concern to be about."
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Say that valence is a strong basis for welfare and moral patienthood, not that nothing valence-free could matter."
  - **Claude Fable 5.2**: "Smithies is in the reference list but never cited at this point."
  - **Gemini 4 Neon**: "ignoring contemporary challenges from non-conscious welfare subjectivity, the Vulcan dilemma, and illusionist ethics"
- **What survives**: the sentence is stated flatly with no pointer to the dispute; it says "felt badness" where P-MS1 says good or bad; Smithies argues the very claim and appears only as a stale reference entry (Crossref: published 2026, pp. 307–336).
- **What does not**: ChatGPT's remedy of softening the claim. The necessity direction is a registered commitment the Map holds and marks as a bullet it bites. The task marks the commitment and does not retire it.
- **Task action**: Upgraded P2 → P1: "`concepts/valence` states "valence provides the necessary condition…"".

### C4. Panksepp without a rival; no illusionist account
- **Flagged by**: chatgpt, claude, gemini on Panksepp; chatgpt, gemini on illusionism
- **Verification**: clean. Every source the reviewers offer for the companion sentences is unread; each is a lead.
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "The complete absence of a named illusionist treatment is the largest philosophical omission."
  - **Claude Fable 5.2**: "One side of a live dispute is reported as a finding."
  - **Gemini 4 Neon**: "The manuscript infers from conserved mammalian subcortical circuits that conscious felt valence is phylogenetically foundational rather than a cortical overlay"; and, on illusionism, "without engaging either illusionist theories of introspection or empirical meta-problem evidence begs the central question of the paper"
- **Note**: ChatGPT's sharpest formulation belongs here. The page treats the existence of a further phenomenal fact as agreed and then faults rivals for not explaining it; the fix is to say that the premise is contested. The Map engages illusionism on `concepts/illusionism` and Kammerer on ten content pages, so the gap is local to this page.
- **Task action**: Upgraded P2 → P1: "`concepts/valence` names no illusionist account of apparent phenomenal valence…".

### C5. Own-voice claims that outrun the page's concessions
- **Flagged by**: chatgpt, claude, gemini
- **Verification**: clean for the sentence in "What Valence Is"; Gemini's second instance disputed.
- **Live passage**: "This generality is what makes valence fundamental: it provides a common evaluative dimension across conscious experience"; "a structurally irresolvable cognitive limit"; "Valence supports the Map's framework at multiple points."
- **Quotes**:
  - **ChatGPT 5.6 Sol Pro**: "Make scalar phenomenal currency a disputed hypothesis rather than part of the introductory definition."
  - **Claude Fable 5.2**: "This is a premise standing in for an argument."
  - **Gemini 4 Neon**: "The manuscript treats negative valence as a simple, modality-general positive–negative property cleanly separable from sensory quality"
- **Note**: the page's own child, `topics/valence-as-a-natural-kind`, already locates the Map's exposure on the single-scalar claim. The parent can take its grade from the child without new citations.
- **Task action**: Upgraded P2 → P1: "`concepts/valence` asserts in its own voice that valence is "a common evaluative dimension"…".

### C6. The reasons argument and reflexive imperativism
- **Flagged by**: claude, gemini
- **Verification**: clean on the painkiller consideration (the Barlassina and Hayward abstract confirms the command is reflexive). The moods half is unverified.
- **Live passage**: "The hedonic account's advantage lies with reasons."; "on the hedonic account the reason needs no further machinery".
- **Quotes**:
  - **Claude Fable 5.2**: "So the “advantage” is not unique to the hedonic account, and the page does not engage this."
  - **Gemini 4 Neon**: the page's two arguments are neutralised by a rival "that the author cites one paragraph earlier and then ignores"
- **Task action**: Upgraded P2 → P1: "`concepts/valence` says the hedonic account's "advantage lies with reasons"…".

### C7. "Three Competing Accounts" as the field
- **Flagged by**: claude, gemini
- **Verification**: clean on the framing. Neither named family has a source read at the publisher.
- **Live passage**: "Three philosophical accounts compete to explain what valence is."
- **Quotes**:
  - **Claude Fable 5.2**: "rename it “Competing accounts” and add attitudinal/desire theories (Heathwood) and Aydede’s adverbialism"
  - **Gemini 4 Neon**: the page omits "dispositional hybrid critiques (Oppositeness, Normativity) of pure felt-quality theories"
- **Note**: the two agree that the three are presented as exhaustive and name different missing families. The oppositeness question (what makes felt goodness and felt badness opposites, as redness and greenness are not) stands without any paper and is in the task as an open demand on the hedonic account.
- **Task action**: Upgraded P2 → P1: "`concepts/valence` presents "Three Competing Accounts" as the field…".

## Singleton Findings

Flagged by one reviewer. Not upgraded; left untouched at their original priority.

- **Gemini 4 Neon**: the zombie sentence ("a zombie's pain-processing would be functionally identical to ours") sits two sections before the argument that felt badness does causal work. In its words: "The manuscript deploys functional-duplicate zombies against physicalism in Section 3 and silently repudiates functional duplication to defend interactionism in Section 4." Right about the page as worded; the Map already concedes the conditional at `concepts/philosophical-zombies` ("The Interactionist Escape"). → `todo.md` task "`concepts/valence` says a zombie's pain-processing "would be functionally identical to ours"…" (P2). This is the strongest single-reviewer finding of the cycle, and neither other reviewer saw it.
- **Claude Fable 5.2**: the Minimal Quantum Interaction paragraph omits the compensation consequence that `apex/born-preserving-causal-efficacy` says value-sensitive articles inherit ("It mentions neither this externality nor the apex."). → task "`concepts/valence` Minimal Quantum Interaction paragraph offers valence as the selection "currency"…" (P2).
- **ChatGPT 5.6 Sol Pro**: the lead of `concepts/pain-asymbolia` is categorical where its body is qualified ("Bring its categorical behavioural summary into line with the qualified body."). → task "Lead of `concepts/pain-asymbolia` says patients "do not withdraw, guard injured limbs, or show distress"…" (P2). An older driver-minted P3 names the same sentence; the task already carries the cross-reference.
- **ChatGPT 5.6 Sol Pro**: the lead of `topics/emotion-and-dualism` over-states ("Replace “strongest empirical case” and “resist every attempt at functional reduction” with language matching the article’s own later concessions"). → task "Lead of `topics/emotion-and-dualism` says emotional consciousness is "the strongest empirical case for interactionist dualism"…" (P2).
- **Smaller single-reviewer points already folded into the convergent tasks as checks** (no separate task): core affect as accessible versus always phenomenally present (Claude C3, a lead); "particularly stark because the property seems so simple" (Claude C6); the unsourced "trillions of invertebrates" (ChatGPT item 9, Claude C10); Bentham quoted without a reference entry (Claude); label checks on "hybrid imperativism … Martínez (2023)" and "who gave the view its name" (Claude); the page says its dualism would survive the hedonic account's defeat and does not say whether its ground for moral status would (Gemini).

## Divergences

- **ChatGPT and Claude vs Gemini, on the low-credence labelling.** ChatGPT: "There is no serious tenet-protective overstatement in its explicit confidence labelling." Claude: "Tenets 1, 3 and 5 are used with unusual discipline." Gemini reads the same labels as insulation, "protected by low-credence disclaimers and an asymmetric "undelivered step" double standard". The processing pass found the page hides neither debt. The residue all three can accept is narrow: the sentence "The Map takes the phenomenal horn on the strength of that undelivered step" faults the rival for an undelivered step without saying the Map's own account leaves one too. That clause is in the C1 task.
- **Claude vs Gemini, on objectless moods.** Claude's verdict table retains the consideration: "| T6 | Objectless moods weigh against representational accounts | compatible | **RETAIN** (already marked contested) |". Gemini says reflexive imperativism answers it as well: "it handles both cases directly without invoking irreducible hedonic qualia". The source Gemini gives was checked at abstract depth and the abstract does not mention moods. Unsettled; the C6 task treats the moods half as a lead to be read at source.
- **Claude vs Gemini, on Cleeremans and Tallon-Baudry (2022).** Claude would lean on the paper further: "Credit Cleeremans & Tallon-Baudry for the comparison and ranking (“mental currency”) idea." Gemini says the existing citation already misuses it: "Citation inversion of Cleeremans and Tallon-Baudry (2022) and bibliographic negligence". Adjudicated: the page cites the paper only for functional significance, which is its claim, so "inversion" is overstated; the abstract does draw a reductive moral the reader is not told about. A few words in the C5 task; no further credit added.
- **ChatGPT vs the processing passes, on the remedy for the necessity sentence.** ChatGPT would replace the claim; Claude offers "Either P-VS4 or the valence page’s moral-status paragraph must give way." Both rest on the under-reading recorded above. The Map's register holds the necessity direction, so the task marks the claim and keeps it. Whether a being with non-hedonic evaluative character only is addressed anywhere is left as a report item in C3.
- **ChatGPT vs Claude and Gemini, on the taxonomy.** ChatGPT: "The distinctions among hedonic, evaluativist and imperativist accounts are basically accurate." Claude and Gemini say the three-way list omits a standing family. These are compatible on accuracy and differ on completeness; C7 is counted at 2 of 3.
- **Claude vs Gemini, on invertebrates.** Claude's table: "| T13 | Value-sensitive coupling makes valence structurally expected in invertebrates | framework commitment (correctly labeled) | **RETAIN**". Gemini says the page "falsely claims that invertebrate valence is merely a framework commitment". The sentence grades one structural expectation and does not deny that evidence exists; Claude's reading is the right one. A wording check sits in C3.

## Reviewer Claims Judged False Alarms or Overstated

1. **Claude**: `apex/minds-without-words` says asymbolia "settles this specific dispute" and is "decisive against the evaluativist reduction". Stale search-index copy; 0 live.
2. **Claude**: `concepts/reductionism` may still carry the "seek treatment" sentence. Stale copy; 0 live.
3. **Claude**: Smithies pp. 307–335. Crossref gives 307–336.
4. **ChatGPT and Claude**: the site holds incompatible positions on moral status. An under-reading of P-MS1 against P-VS4.
5. **Gemini**: the tenet section "quietly reinstates" the single-currency thesis. The sentence reports "the value-sensitive position" and grades it at low credence.
6. **Gemini**: the page "inverts" Cleeremans and Tallon-Baudry. Overstated, as above. The "chronic pain" quotation is not in the abstract.
7. **Gemini**: the page "falsely claims" there is no evidence of invertebrate affect. A misreading of "a framework commitment, not a probability the evidence supplies".
8. **Gemini**: "all twenty bibliographic entries" and its section numbering. Presentational; no entry is claimed retracted and none was found to be.
9. **ChatGPT**: `topics/ethics-of-consciousness-invertebrate-question` needs an anti-vagueness premise beyond dualism. The page's body already supplies it; only the lead is generic.

Unverified and kept as leads, in every task that mentions them: Hesp et al.'s statement that they "do not equate expected precision directly with valence" (ChatGPT); Kammerer's 2026 book (ChatGPT); Kiverstein, Miller and Rietveld (2019) as characterised (Claude); every numerical result in the Gemini report; Voodla et al. (2024) as disconfirming Joffily and Coricelli (Gemini); the "homuncular regress" Gemini alleges in one parenthesis, which is the reviewer's own argument and was not assessed.

## Methodology Proposals

ChatGPT made ten (its items 19–28) and Claude twelve (Part 5). Gemini made none; its prompt excluded the pipeline. They are listed and assessed here on their merits. None is minted as a task: adopting any of them is a methodology decision for the operator.

**Proposed by both reviewers** (the stronger candidates):

| Proposal | ChatGPT | Claude | Assessment |
|---|---|---|---|
| Propagate a correction to every page that repeats the corrected claim | 20 | 2 | Strong, and this cycle is a live instance: `concepts/pain-asymbolia` was corrected on 2026-11-24 and `concepts/valence` still carried the old shorthand (C2). The 2026-11-24 synthesis recorded the same failure as its M1. Claude's "block publication" form is too heavy; a generated list of pages sharing the withdrawn phrase is the workable part. |
| Detect stale "forthcoming" entries and reference entries with no in-text citation | 25 | 4 | Strong and cheap. Both are mechanical checks; the Smithies entry failed both, on two pages. |
| Label a rival that the Map has built as the Map's construction; attribute to sources only what they state | 19, 21 | 6 | Strong. It is the general form of C1. ChatGPT's per-sentence claim ledger is costly as specified; the narrower rule (any model credited to a paper must be found in that paper) would have caught C1. |
| Check summary text (leads, descriptions, tenet-section openers) separately from bodies | 27 | 1 | Good. S3, S4 and the "supports … at multiple points" opener are all cases. Claude's ban on the word "supports" is a blunt instrument; a check that the opener claims no more than the paragraphs under it is the useful part. |
| Engage the newest strong rival in its own vocabulary | 22 | 5, 7 | Good in principle, and the direct-refutation discipline written into the task notes already asks for it; C4 shows a page where it lapsed. Claude's hard pre-publication gate for a named paper list would need upkeep and would block on length-capped pages. |
| Record what each external reviewer actually read (page version; index lag) | 26 | 9 | Good. Claude's two stale-copy false alarms this cycle and the 2026-11-24 cycle's three are the evidence. The commission prompts already ask for the live page and, for two of the three legs, the changelog; a last-modified feed by slug is the missing piece. |
| Keep a cross-page contradiction register; check categorical claims against the positions register | 28 | 8 | Partly sound. A check against the register is useful, but the one conflict both reviewers offer as the example (necessity versus P-VS4) was an under-reading, so an automatic "conflict banner" would have fired falsely here. |

**Proposed by one reviewer:**

- **ChatGPT 23, state what kind of disagreement an "explanatory gap" claim marks and what would count against it.** Good; it is the method-level form of C4's sharpest point.
- **ChatGPT 24, pair any old foundational empirical source with a recent review or adversarial update.** Good; Panksepp (1998) standing alone is the case. The weekly literature-drift audit already works in this direction for topic pages and does not cover concept pages.
- **Claude 3, record each cited author's own conclusion on the point cited.** Good where an author is cited on a contested point (Bain on asymbolia; Cleeremans and Tallon-Baudry). Its example of an "inversion" on the apex was drawn from a stale copy, so the instance is void while the idea stands.
- **Claude 10, same-family review.** The observation is fair: internal reviews share a model family, and, as the reviewer reports (not re-checked here), an optimistic review of 2026-03-22 praised an asymbolia argument since withdrawn. The outer-review programme is the existing answer. Weighting outer reviews above internal optimistic ones when they conflict is reasonable; a required non-same-family pass before any page counts as reviewed would bind every page to the Chrome window's throughput.
- **Claude 11, separate changelog categories (metadata repair, stance repair, propagation sweep, retreat of a thesis).** Modest value; useful mainly if "stabilised" status is ever computed from the changelog.
- **Claude 12, automatically demote long-held low-credence framework-internal positions on every citing page.** Weak. A position already labelled low credence and framework-internal is not improved by a timer; the defect this cycle was a missing cost (S2), not an over-held credence.
- **Claude's fixes 15 and 16** (annotate the 2026-03-22 optimistic review; mark two leads in a February research note as non-peer-reviewed). Small and reasonable; not taken up here because review files and research notes are records of their date.

## Subjects the Map Does Not Cover (for the research harvester)

Counts are files containing the term, by fixed-string search at about 06:00Z. "Content" means `topics/`, `concepts/`, `apex/`, `voids/` and `positions/`; "research" means `research/`. Positive control: "Kammerer" returns 10 content files and 8 research notes. Every paper below is confirmed at metadata depth only unless an abstract check is stated; none has been read.

- **Attitudinal (desire) theories of pleasure and unpleasantness, and dispositional hybrid theories.** "attitudinal theor" 0 content, 0 research; "Heathwood" 0 content, 1 research; "Pallies" 0 content, 1 research; "Oppositeness" 0 and 0; "adverbialis" 0 content, 4 research. Pallies (2021), "An honest look at hybrid theories of pleasure", *Philosophical Studies* 178(3), 887–907, is listed unread in `research/constructed-emotion-and-valence-as-a-natural-kind-2026-09-05`. Flagged by Claude (no citation) and Gemini. The strongest candidate: a fourth family of accounts with no article, bearing directly on C7.
- **The "causal assumption" critique.** Key and Brown (2024), "Making sense of feelings", *Neuroscience of Consciousness* 2024(1), niae034: 0 content, 0 research (abstract verified at OpenAlex: it names and rejects the assumption that feelings such as pain drive behaviour). A direct opponent of Bidirectional Interaction as applied to pain, with no coverage.
- **Common versus stimulus-specific neural coding of negative affect, and mixed-valence states.** Čeko et al. (2022), *Nature Neuroscience* 25(6), 760–770: 0 and 0. Vaccaro et al. (2024), *Cerebral Cortex* 34(4), bhae122: 0 and 0. Cowen and Keltner (2021): 1 content, 2 research. These bear on `topics/valence-as-a-natural-kind` and on the single-scalar claim in C5.
- **Higher-order accounts of emotional consciousness in their 2020s form.** Taschereau-Dumouchel, Michel, Lau, Hofmann and LeDoux (2022), *Molecular Psychiatry* 27(3), 1322–1330: 0 and 0. "LeDoux" itself is on 12 content pages, so this would add depth to existing coverage.
- **Empirical tests of the free-energy-rate account of valence.** Voodla, Uusberg and Desender (2024): 0 and 0.
- **Covered already, so not candidates**: reflexive imperativism ("Barlassina" on 1 content page, `concepts/valence`, and in 2 research notes, so thin but present); the inverse dissociation (Hagiwara on `concepts/pain-asymbolia`); Gerrans (7 content pages); Kiverstein (5); the Beautiful Loop paper ("Laukkonen" on 41 content files); Berridge's wanting and liking (`topics/wanting-liking-and-the-value-in-mechanism-fork`); the evaluative space model ("Cacioppo" on 2 content pages).

## Method Notes

- **Three of three, one page.** All three legs completed, on a single article. Convergence here is same-page and same-passage throughout, which is why six tasks meet the same-page rule (same claim, same page, passage live now) where the 2026-11-24 full-site cycle produced none.
- **The collect passes did most of the clustering.** They ran in sequence, and each later pass appended its evidence to the earlier task instead of minting a duplicate. This run found no two tasks sharing a defect and a locus, so nothing was merged. The nearest contacts are noted in the tasks: C5's Caution covers the word "currency" in the paragraph S2 adds a clause to; C4 and S1 edit the same section.
- **What changed in `todo.md`.** Seven tasks, in place, all above the `## Completed Tasks` line (L6862 after the edits): six headings changed from P2 to P1; on all seven, `Review file` became `Review files`, a `Synthesis` field was added above `Notes`, and a convergence header with quotes, order and ceiling was placed at the start of `Notes`, followed by the original Notes and every addendum unchanged. No Type, Status, File, Headroom or Caution line was altered. The four singleton tasks were not touched.
- **Counts.** `parse_tasks` active 508 before and 508 after (P1 3 → 9, P2 26 → 20, P3 479 → 479; pending 473, blocked 33, superseded 2, unchanged). One `## Completed Tasks` line before and after.
- **Sources.** No external source was fetched in this run. Every source fact comes from the three processing passes (Crossref and OpenAlex). No citation was added to any task that a processing pass had not already recorded, and each keeps the grade it was given there.
- **Convergence is weaker than the count suggests in two places.** C4 is 3 of 3 only on the Panksepp half. C6 is 2 of 2 only on the painkiller half. Both are marked in the tasks.
