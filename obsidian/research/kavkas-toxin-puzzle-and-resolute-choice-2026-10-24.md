---
title: "Research Notes - Kavka's Toxin Puzzle and Resolute Choice"
created: 2026-10-24
modified: 2026-10-24
human_modified: null
ai_modified: 2026-10-24T19:08:09+00:00
draft: false
description: "Research notes on Kavka's toxin puzzle and resolute choice: a contract that forbids precommitment, McClennen, Gauthier and Bratman's no-regret condition, folded into the precommitment page."
topics:
  - "[[precommitment-and-the-diachronic-agent]]"
  - "[[akrasia-and-weakness-of-will]]"
  - "[[the-divided-will]]"
  - "[[diachronic-agency-and-personal-narrative]]"
concepts:
  - "[[self-control-as-skill-and-scaffolding]]"
related_articles:
  - "[[tenets]]"
  - "[[tenets/background-commitments]]"
  - "[[research/precommitment-and-the-diachronic-agent-2026-10-23]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-24
last_curated: null
recommended_action: fold
target_section: topics
target: precommitment-and-the-diachronic-agent
target_slug: precommitment-and-the-diachronic-agent  # FOLD HOST (existing page), not a new slug
---

# Research: Kavka's Toxin Puzzle and Resolute Choice

**Date**: 2026-10-24
**Origin**: P3 queue task harvested from `reviews/optimistic-2026-10-24-fresh-article-wing.md`, New-Territory candidate 1 (L426, "Can an intention do a device's work?"; fold recommendation at L475).
**Verdict**: **FOLD**, not article. The host is `topics/precommitment-and-the-diachronic-agent`. The fold is one new section, "The Toxin: Binding Ruled Out" (`#toxin`), placed between "The Override Removed" and "Identity and Authority" (before host L70). It is **539 words** (469 prose + 70 references) and ends the host at **3,311** by `analyze_length`, measured on a scratch copy with the draft inserted. The draft is [below](#angles).

**Searches and fetches**:
- **WebSearch, 4 calls**: a Kavka 1983 PDF; the SEP on sequential choice; a Holton "Rational Resolve" PDF (none found); O'Donoghue & Rabin's terminology.
- **Raw fetches, grepped by script** (whitespace-, quote- and line-break-hyphen-normalised):
  - **Kavka 1983, original journal**: archive.org item `dli.calcutta.02556` (*Analysis* vol. 43, Digital Library of India scan), file `H02969_hocr_searchtext.txt.gz`. The running heads "34 ANALYSIS", "THE TOXIN PUZZLE 35" and "36 ANALYSIS" survive in the OCR, so **page numbers are verified**.
  - SEP "Decision Theory" (Steele & Stefánsson; first published 16 Dec 2015, substantive revision 20 Aug 2025), raw HTML.
  - Liberman 2016 (JESP, open access), PDF via `pdftotext`.
  - Kroon, "Just Imagine" (Advanced Reasoning Forum PDF), a secondary reproduction of Kavka's setup.
- **archive.org full-text-search snippets** (phrase queries scoped to one item; about 100 characters of context each; full OCR is lending-restricted):
  - `rationalcommitme0000unse`: Coleman & Morris (eds.), *Rational Commitment and Social Justice: Essays for Gregory Kavka* (CUP 1998). This holds Bratman 1998, Gauthier 1998 and Harman 1998.
  - `rationalitydynam0000mccl`: McClennen, *Rationality and Dynamic Choice* (CUP 1990).
  - `paradoxesofratio0000unse`: Campbell & Sowden (eds.), *Paradoxes of Rationality and Cooperation* (1985).
  - `breakdownofwill0000ains`: Ainslie, *Breakdown of Will* (CUP 2001).
  - `intentionplanspr0000brat`: Bratman, *Intention, Plans, and Practical Reason* (1987).
- **Crossref**: Kavka 1983; the 1998 volume's chapter list; McClennen 1985 and 1988; Gauthier 1994 and 1997; Holton 2004; Liberman 2016; Hammond 1976; Pollak 1968; Mele 1992 and 1996; Bratman 1992; DeHelian & McClennen 1993.
- **Local**: the Strotz 1955–56 PDF text from the 10-23 precommitment research, re-grepped for "naive" and "sophisticat".
- **Read first, not re-derived**:
  - the host;
  - [[research/precommitment-and-the-diachronic-agent-2026-10-23]] (§D L236ff, Guards L383ff, Gaps L538ff);
  - `topics/akrasia-and-weakness-of-will` L76–82;
  - `topics/diachronic-agency-and-personal-narrative` L81;
  - `topics/emotion-regulation-and-the-timing-of-control` (no Holton/Bratman hits);
  - `concepts/self-control-as-skill-and-scaffolding`.

**Verification tags**:
- **[V-scan]**: grep-verified in OCR of a scan of the original printed pages, with page numbers taken from the running heads.
- **[V-raw]**: grep-verified in raw HTML or a PDF text layer.
- **[V-ocr]**: an archive.org full-text-search snippet of the named book. The wording is verified, but **pages are not**, unless a running head appears inside the snippet. **Chapter attribution in an edited volume is inferred from context**, since the index does not report chapter boundaries.
- **[V-xref]**: Crossref metadata only.
- **[V-sec]**: read only through the named secondary source.
- **[Lead]**: not verified.

**Quote tally**:
- **The 13 quotations in the draft passage: 13 of 13 pass.**
  - Kavka, 5: [V-scan], normalised substring check.
  - SEP, 2: [V-raw], normalised substring check.
  - Bratman, 4, and McClennen, 2: [V-ocr], exact-phrase queries returning a hit.
- **Every other quotation in Sources A (Kavka), E (SEP), F (Liberman) and side-finding 3 (Strotz) passes** the same check against the local raw text: 56 checks in all, with running heads stripped and the OCR repairs listed under Source A applied.
- **The [V-ocr] quotations in Sources B, D and G** were each confirmed as an exact-phrase hit in the archive.org index, or rebuilt from overlapping hits.
- **Expected misses (OCR word-merges), not used in the draft**:
  - Kavka's "As a cognitive scientist, materialist" reads "Asa" in the OCR.
  - Bratman's clause (b), "would regret not sticking with her intention", returns 0 because the OCR splits "in¬ tention". The draft paraphrases clause (b) for that reason.
- **Negative control**: the secondary paraphrase "make no bets" (Kroon) is **absent** from Kavka's text, as expected.

## Executive Summary

Kavka's toxin puzzle is precommitment with the external route closed by contract. A billionaire pays for an intention at midnight to drink a day-sickening toxin the next afternoon, and the money arrives before the drinking.

Kavka's own text raises binding yourself "by today making irreversible arrangements that will give you sufficient independent incentive to drink it", and then rules it out: "arrangement of such external incentives is ruled out". It also sets aside a self-promise by stipulating the agent's character (pp. 34–35). The case therefore isolates the question the host leaves implicit: **can an internal intention do what Elster's condition (iii) says only an external device does?**

Kavka's answer is **hedged**: you cannot "(or have extreme difficulty doing so)", because intentions are "dispositions to act which are based on reasons to act" (p. 35).

The replies divide on whether a plan's rationality transfers to its steps:
- **McClennen's resolute choice** (in print by 1985) says it can, for a perfectly rational agent. But McClennen himself assigns Ulysses, "an imperfectly rational being", to sophisticated choice, which means precommitment.
- **Gauthier**, on Bratman's report, holds "moderate resolution": one may rationally drink.
- **Bratman** rejects both forms of resolution for such cases, as not doing justice to "the significance of temporal and causal location to our agency". He proposes a no-regret condition that some temptation cases meet and the toxin case fails.
- **Holton's resolutions** (second-order intentions) are built for temptation's judgement shift. The akrasia page already covers them.

**For the Map.** Resolute choice is a policy rule that any persisting planning system can run, so it needs nothing further. The SEP's dilemma shows that it either keeps the later override, and then looks like choosing against one's preferences, or removes it internally, and then posits a binding that condition (iii) excludes and that Kavka doubts can be formed. The persisting subject the Map posits answers *whose plan* the earlier plan is. It does not answer *why it should govern now*, which is Bratman's objection and the host's authority question turned inward. This is fit, not evidence.

## Verdict: fold, not article {#verdict}

**`recommended_action: fold`**, host `topics/precommitment-and-the-diachronic-agent`. This mints no task.

**Why not an article.**
1. **Cap.** `tools.evolution.state.count_section_files("topics")` = **366** of 370 (driver's figure confirmed at 18:4xZ). CLAUDE.md records one over-count sidecar.
2. **The host's spine is exactly what the puzzle manipulates.** The host defines precommitment by Elster's condition (iii) (L44) and turns on retained versus removed override (L62–68). Kavka's contract forbids the condition-(iii) route. A standalone page would have to restate both.
3. **The literature the Map needs is small.** It is Kavka's two theses, three replies (McClennen, Gauthier, Bratman) and one decision-theory framing. The wider literature (Mele, Harman, Farrell's deterrence variants, game-theoretic resolute choice, Independence violations) has no tenet bearing beyond what the fold says.
4. **The reviewer recommended a fold** (review L475) and the host has room.

**Host lengths** (`tools.curate.length.analyze_length`, body only, measured about 18:40Z and re-measured about 19:05Z). Headroom = hard − 1 − count.

| Host | Count now | Hard | Headroom | Role |
|---|---|---|---|---|
| `topics/precommitment-and-the-diachronic-agent` | **2,772** (prose 2,337 / Further Reading 63 / References 372) | 4,000 | 1,227 | **Primary.** After the fold: **3,311** (prose 2,799 / FR 63 / refs 447). This crosses soft (3,000) into `soft_warning`, which carries no consequence; hard headroom after the fold is 688 |
| `topics/akrasia-and-weakness-of-will` | **3,651** | 4,000 | 348 | Secondary, **optional only**. L80 already links precommitment. At most a ~20-word clause (see [optional add-ons](#optional)). Not a host for the fold |
| `topics/diachronic-agency-and-personal-narrative` | **3,451** | 4,000 | 548 | No change needed. L81's Bratman sentence is about plans coordinating the agent, not the toxin |
| `topics/the-divided-will` | **3,074** | 4,000 | 925 | Possible later home for the **Ainslie toxin lead** (Source G), not for this fold |
| `concepts/self-control-as-skill-and-scaffolding` | **3,038** | 3,500 | 461 | No change. Its L90 luck-objection sentence ("moving selection to the moment a resolution is formed") already covers the relocation point |

## Coverage on the Map (scoped) {#coverage}

Method: case-insensitive fixed-string file counts. "Live" is `topics/ concepts/ apex/ voids/ positions/` with `-refinement-log` sidecars excluded; "research" is `research/`. Run about 18:40Z.

| String | Live / research | Notes |
|---|---|---|
| "toxin puzzle" | **0 / 1** | Research: the 10-23 precommitment note (§D lead) |
| "toxin" | 0 / 2 | The second research hit is botulinum toxin (`intact-substrate-reversibility`). Different subject |
| "Kavka" | **0 / 3** | Research: precommitment note; `partitioned-and-distributed-minds…` L77 (Kavka 1994, a *review* of Ainslie's *Picoeconomics*); `voids-numbing-void` (Kavka 1979, "The numbers should count"). **Two different Kavka works, neither the toxin** |
| "resolute choice" | **0 / 2** | Research: precommitment note; `partitioned-and-distributed-minds…` L80 (Ainslie's ch. 8 lists "resolute choice" among five theories of will) |
| "McClennen" | **0 / 1** | |
| "Gauthier" | 1 / 2 | Live hit is **Isabel Gauthier** (Greebles, `consciousness-as-perceptual-architect` L107). Different person |
| "sophisticated choice", "no-regret", "dynamic choice", "Hammond", "Rabinowicz" | 0 / 0, 0 / 0, 0 / 1, 0 / 1, 0 / 1 | The research hits are unrelated (self-prediction void; a different Hammond) |
| **Positive controls** "Holton" / "akrasia" / "Bratman" | **4 / 9**, **20 / 18**, **5 / 7** | Holton and akrasia match the driver. **Bratman is 5 live**, one more than the precommitment note's 4 of 10-23; the host itself, created 10-24, is the new hit |

What the neighbours already hold, so the fold does not restate it:
- **Holton's resolutions**: `akrasia` L80 ("an intention formed precisely to insulate the agent against contrary inclinations…"), and L80's precommitment contrast (added by the host's expand-topic commit `9343b54876`, 2026-10-24).
- **Bratman's plans** "settle matters in advance, resist casual reconsideration": `diachronic-agency` L81.
- **The host**:
  - L50 places resolutions, plans and personal rules inside the agent, outside (iii);
  - L64 says "A resolution can be abandoned";
  - L98 has Steward's settler.

## What Is New Relative to the Host and Its Research Note {#new}

**Already on the Map, not re-derived**: Elster's conditions (i), (iii) and (v); the internal/external line; Holton's resolutions; Bratman's plans; Ainslie's interests; Steward's settler; the identity/authority split.

**Genuinely new**:
1. **Kavka's text builds the puzzle by closing both of the host's routes.**
   - The external route: "Why not bind yourself… by today making irreversible arrangements", then "arrangement of such external incentives is ruled out, as are such alternative gimmicks as hiring a hypnotist to implant the intention, forgetting the main relevant facts of the situation, and so forth" (p. 34).
   - The internal self-promise, by stipulated character: "Promising yourself that you will drink the toxin could help if you were one of those strange people who take pride in never releasing oneself from a promise to oneself, no matter what the circumstances. Alas, you are not." (pp. 34–35).
   - So the puzzle *is* the question of whether an intention can do a device's work. The precommitment note's §D had it as a lead only.
2. **Kavka's conclusion is hedged and has a stated rationale.** "Yet you cannot do so (or have extreme difficulty doing so) without resorting to exotic tricks involving hypnosis, hired killers, etc." He adds: "you cannot intend to act as you have no reason to act, at least when you have substantial reasons not to act" (p. 35). The thesis is that "intentions are only partly volitional" (p. 36). **The brief's gloss "Kavka: one cannot" must carry the hedge.**
3. **McClennen does not offer resolute choice as a replacement for Ulysses' ropes.** He holds that perfect rationality "points toward what I have characterized as being resolute, while an imperfectly rational being (such as Ulysses) must settle for some version or other of sophisticated choice" (1990, [V-ocr]). He also writes "Sophisticated Ulysses precommits". The SEP agrees: "Resolute choice deviates from sophisticated choice only under certain conditions that are not fulfilled by Ulysses, given his change in attitudes." **So resolute choice and precommitment are complements, not rivals.** This sharpens the host's L50 line.
4. **Bratman's 1998 taxonomy:**
   - the "linking principle" and the "standard view", whose joint operation yields Kavka's result;
   - **strong resolution**, "a version of 'resolute choice'" after McClennen;
   - **moderate resolution**, Gauthier's view, which adds "a further, counterfactual test";
   - **sophistication**;
   - Bratman's own **no-regret condition**.
   His objection to both resolutions is that they do not do justice to "the significance of temporal and causal location to our agency". On the Map's reading, that is the host's later override, defended as the agent's standpoint.
5. **The SEP's dilemma** for resolute choice: "What would it mean for an agent to choose against her preferences in order to fulfill a previously-selected plan? That would seem to defy the very notion of preference." Defenders "may have in mind a different interpretation… whereby future 'choice points' are not really points at which an agent is free to choose according to her preferences at the time." **This maps one-to-one onto the host's retained/removed override.**
6. **Coiner corrections** ([below](#coiners)):
   - "resolute choice" is McClennen's and in print by **1985**, not first in 1990;
   - Strotz uses neither "naive" nor "sophisticated" as terms.
7. **The Map's question** gets an answer of the host's own shape: resolute choice needs nothing beyond a planning system; the posit settles whose plan it is, not its authority ([below](#maps-question)).

## Key Sources {#key-sources}

### A. Kavka, G. S. (1983). "The toxin puzzle." *Analysis* 43(1), 33–36. doi:10.1093/analys/43.1.33 [V-xref; V-scan]

- **Source**: archive.org `dli.calcutta.02556`, OCR search text. Page breaks: "34 ANALYSIS" falls after the opening paragraph's "…the money will"; "THE TOXIN PUZZLE 35" falls inside the self-promise parenthesis; "36 ANALYSIS" falls after "Now when reasons for intending and reasons".
- **OCR repairs**: "OU" for "YOU" (drop cap); "receiv- ing", "con- tract", "incen- tives" (hyphenation); "stuf" for "stuff"; "hav2" for "have"; "tò" for "to"; "Ncw" for "Now"; "willicg" for "willing"; "Asa" for "As a". **Quote the repaired forms and do not quote around the damaged ones.**
- **p. 33**: "You are feeling extremely lucky. You have just been approached by an eccentric billionaire who has offered you the following deal. He places before you a vial of toxin that, if you drink it, will make you painfully ill for a day, but will not threaten your life or have any lasting effects." Also: "The billionaire will pay you one million dollars tomorrow morning if, at midnight tonight, you intend to drink the toxin tomorrow afternoon."
- **p. 34**:
  - "You are perfectly free to change your mind after receiving the money and not drink the toxin."
  - The scanner: "As a cognitive scientist, materialist, and faithful former student of Doctor X, you have no doubt that the machine will correctly detect the presence or absence of the relevant intention." **This is a stipulation of the story.** See [guards](#guards).
  - "So instead of planning to drink the toxin, you decide to intend today to drink it and then change your mind after midnight. But if that is your plan, then it is obvious that you do not intend to drink the toxin. (At most you intend to intend to drink it.)"
  - The precommitment route: "Why not bind yourself to drink the stuff tomorrow, by today making irreversible arrangements that will give you sufficient independent incentive to drink it?" Promising another person, a forfeit to "your least favourite political party", and "hire a hitman" are the examples.
  - "arrangement of such external incentives is ruled out, as are such alternative gimmicks as hiring a hypnotist to implant the intention, forgetting the main relevant facts of the situation, and so forth."
- **pp. 34–35**: "(Promising yourself that you will drink the toxin could help if you were one of those strange people who take pride in never releasing oneself from a promise to oneself, no matter what the circumstances. Alas, you are not.)"
- **p. 35**:
  - Newcomb is invoked and set aside: "you are the first one to receive the offer".
  - "Yet you cannot do so (or have extreme difficulty doing so) without resorting to exotic tricks involving hypnosis, hired killers, etc."
  - "If intentions were inner performances or self-directed commands, you would have no trouble earning your million… But intentions are better viewed as dispositions to act which are based on reasons to act".
  - "you cannot intend to act as you have no reason to act, at least when you have substantial reasons not to act."
  - "While you have no reasons to drink the toxin, you have every reason (or at least a million reasons) to intend to drink it."
- **p. 36**:
  - "when we have good reasons to intend but not to act, conflicting standards of evaluation come into play and something has to give way: either rational action, rational intention, or aspects of the agent's own rationality".
  - "It also reveals that intentions are only partly volitional. One cannot intend whatever one wants to intend any more than one can believe whatever one wants to believe. As our beliefs are constrained by our evidence, so our intentions are constrained by our reasons for action."
- **Origin note (p. 36, n. 1)**: "The puzzle discussed here emerged from a conversation, some years ago, with Tyler Burge about 'Some Paradoxes of Deterrence'" (Kavka 1978, *J. Phil.*).
- **Stance**: moral and political philosopher (Hobbes; deterrence). No engagement with dualism. The "materialist" scanner operator is the reader's fictional persona.

### B. Bratman, M. E. (1998). "Toxin, Temptation, and the Stability of Intention." In Coleman & Morris (eds.), *Rational Commitment and Social Justice*, CUP, pp. 59–83. doi:10.1017/cbo9780511527364.006 [V-xref; V-ocr]

- **Chapter list** [V-xref]: Gauthier, "Rethinking the Toxin Puzzle" pp. 47–58; Bratman pp. 59–83; Harman, "The Toxin Puzzle" pp. 84–89; Farrell, "A New Paradox of Deterrence" pp. 22–46.
- **Section heads** [V-ocr]: "III. Autonomous Benefits: Toxin"; "IV. Autonomous Benefits: Reciprocation"; "V. Sophistication and Resolution"; a later section begins "Temporary Reversals in Rankings".
- **The standard view**: "depends on the agent's evaluative ranking at the time of the action of options available then. Call this the standard view." Also "On Wednesday my evaluative ranking will favor nondrinking over drinking."
- **The linking principle**: "The linking principle tells us that rationally to settle on such a plan I cannot suppose…". Kavka's result is "the combination of the linking principle and the standard view."
- **Strong resolution**: "…McClennen, we may call this a version of 'resolute choice.'20 In anticipation of a later distinction I will call it, more specifically, strong resolution." Also "Sophistication accepts the standard view; strong resolution says, instead, that a prior plan settling on which was…" (snippet ends).
- **Moderate resolution**: "Gauthier adds a further, counterfactual test on rational follow-through". Then "…would have done if one had initially not settled on the plan to drink or to reciprocate. So one may rationally drink the toxin, and one may rationally reciprocate. Let us call Gauthier's view moderate resolution." The OCR breaks "moder¬ ate".
- **The objection**: "This seems to me not to do justice to the significance of temporal and causal location to our agency. Strong and moderate resolution, in seeking a strong role for planning…". Also "I am skeptical, then, about strong and moderate resolution.27 But I also think that sophistication is too simple."
- **Scope**: "I have rejected strong and moderate resolution as applied to our autonomous-[benefit cases]" (the snippet ends at the line break before a running head "70").
- **No-regret**:
  - "Statement (a) says, roughly, that the agent would not regret sticking with her prior intention; (b) says, roughly, that she would regret not sticking with her in[]tention."
  - Temptation cases pass: Ann's "one-beer policy she would satisfy the no-regret condition"; Quinn's self-torturer, "his intention to stop at 15 satisfies the no-regret condition".
  - The toxin fails: "…fixed the past prior to my Wednesday decision, I would regret following through and drinking the toxin. Granted, if I did follow through I might later be glad that I am that kind of guy - the kind of guy who wins the money…". A second fragment adds "…but that seems a different matter".
- **Pages within 59–83 are unverified.**
- **Bratman (1987)**, *Intention, Plans, and Practical Reason* (Harvard UP), discusses the toxin with a Monday/Tuesday/Wednesday version [V-ocr: "discussed by Gregory Kavka in his article 'The Toxin Puzzle.' Suppose that on Monday you are offered…"]. McClennen 1990 n. 22 locates it at "Bratman (1987, pp. 101–6)" [V-ocr].
- **Stance**: planning theorist; naturalist frame; no dualism.

### C. Gauthier [via Bratman; metadata]

- **Gauthier's view as Bratman reports it** is moderate resolution (Source B). Bratman's n. 21 points to Gauthier's "Assure and Threaten", "Commitment and Choice" and "Intention and Deliberation" [V-ocr].
- **Gauthier, D. (1994).** "Assure and Threaten." *Ethics* 104(4), 690–721. doi:10.1086/293651 [V-xref].
- **Gauthier, D. (1997).** "Resolute Choice and Rational Deliberation: A Critique and a Defense." *Noûs* 31(1), 1–25. doi:10.1111/0029-4624.00033 [V-xref]. Liberman (2016, n. 1) says McClennen's notion "is elaborated upon and modified by Gauthier (1997)" [V-raw in Liberman].
- **Gauthier, D. (1998).** "Rethinking the Toxin Puzzle," pp. 47–58 [V-xref]. Fragments [V-ocr; **chapter attribution inferred, not confirmed**]:
  - "Can I give myself a reason to drink the toxin? It may seem that I can do so by forming the intention to drink it."
  - "…that drinking it is part of the best course of action that I could embrace as a whole - best not only prospectively, but still best at the time of drinking."
  - **Do not quote these as Gauthier's.** Paraphrase his view through Bratman.

### D. McClennen [V-xref; V-ocr]

- **McClennen, E. F. (1985).** "Prisoner's Dilemma and Resolute Choice." In R. Campbell & L. Sowden (eds.), *Paradoxes of Rationality and Cooperation* (UBC Press), ch. 5, pp. 94–104. doi:10.59962/9780774857154-006 [V-xref]. The editors' introduction [V-ocr]: "There McClennen defends a conception of rationality as 'resolute choice.'" The scare quotes mark it as new. **The term is in print by 1985.**
- **McClennen, E. F. (1988).** "Constrained Maximization and Resolute Choice." *Social Philosophy and Policy* 5(2), 95–118. doi:10.1017/s026505250000008x [V-xref].
- **McClennen, E. F. (1990).** *Rationality and Dynamic Choice: Foundational Explorations*. CUP. doi:10.1017/cbo9780511983979 [V-xref; V-ocr].
  - Contents [V-ocr]: 9.4 "Sophisticated choice" 153; 9.6 "Resolute choice" 156; 9.7 "Resolute choice and separability" 158; 11.3 "The problem with sophisticated choice" 190; ch. 12 "The feasibility of resolute choice" 200 (12.1 "An argument against resolute choice" 200); 15.1 "Resolute choice and game theory" 256.
  - "…rationality points toward what I have characterized as being resolute, while an imperfectly rational being (such as Ulysses) must settle for some version or other of sophisticated choice."
  - "Sophisticated Ulysses precommits".
  - Ch. 12 is previewed: "Ulysses and the potential drug addict are perhaps best treated as agents for whom a resolute approach is not possible, or at least…".
  - McClennen quotes Elster: Ulysses "reveals himself to be less than perfectly rational since 'a rational creature would not have to resort to this device'".
  - The idiom: "The resolute self is capable of recognizing ties to its own former selves." Also "the time-defined selves to maximize preferences against what previous selves have chosen".
  - He quotes Kavka's setup (n. 22: "Kavka (1983, pp. 33–4)") and Kavka's dispositional view of intention (n. 23: "Kavka (1983, p. 35)").
  - **Pages for the quotations are unverified**, apart from the contents entries.
- **Secondary gloss** [V-raw, Liberman 2016, n. 1]: "McClennen (1990) outlines a notion of resolute choice in which the chooser commits herself to a plan that seems best at the time of initial choice, and then sticks with this plan regardless of whether it continues to seem best to her".
- **Stance**: decision theorist; motivated by Independence-violating preferences and intrapersonal/interpersonal coordination. No metaphysics of persons. "Selves" is a modelling idiom.

### E. Steele, K., & Stefánsson, H. O. (2025). "Decision Theory." *SEP*, first published 16 Dec 2015, substantive revision 20 Aug 2025. https://plato.stanford.edu/entries/decision-theory/ [V-raw]

- "Three major approaches to negotiating sequential decision trees have appeared in the literature. These are the naïve or myopic approach, the sophisticated approach and the resolute approach."
- "The hallmark of the sophisticated approach, by contrast, is its emphasis on backwards planning". "Sophisticated Ulysses would take note of the fact that, if he reaches the island of the sirens unrestrained, he will want to stop there indefinitely".
- "Resolute choice deviates from sophisticated choice only under certain conditions that are not fulfilled by Ulysses, given his change in attitudes."
- "Defenders of resolute choice typically defend decision theories and associated preferences that violate the Independence axiom/Sure-Thing Principle (notably McClennen 1990 and Machina 1989…)".
- "According to resolute choice, in appropriate contexts, the agent should at all choice points stick to the strategy that was initially deemed best."
- "What would it mean for an agent to choose against her preferences in order to fulfill a previously-selected plan? That would seem to defy the very notion of preference."
- "Defenders of resolute choice may have in mind a different interpretation of sequential decision models, whereby future 'choice points' are not really points at which an agent is free to choose according to her preferences at the time."
- The entry's own stance: "it will be assumed that rational agents pursue the sophisticated approach to choice (as per Levi 1991, Maher 1992, Seidenfeld 1994, amongst others)". **So the SEP is not neutral.** It sides with sophistication.
- **No coiner is credited** for the three approaches.

### F. Holton, via Liberman 2016 [V-raw in Liberman; V-sec for Holton]

- **Liberman, A. (2016).** "Reconsidering Resolutions." *Journal of Ethics and Social Philosophy* 10(2), 1–27. doi:10.26556/jesp.v10i2.98 [V-xref; V-raw]. This is the "Liberman (2016)" lead in the precommitment note, now confirmed.
- **Holton 2009 as Liberman quotes it**:
  - resolutions consist in "both an intention to engage in a certain action, and a further intention not to let that intention be deflected" (Holton 2009, p. 11);
  - "as a matter of empirical fact, temptation normally induces judgment shift" (97);
  - judgement becomes "either corrupted or powerless" and so "cannot be the motor of resistance" (98).
- **Liberman's objection** (abstract) [V-raw]: "the second-order intention is as equally susceptible to temptation as the first-order intention alone would be". She proposes "a first-order intention paired with a second-order desire".
- **Holton 2004**, "Rational Resolve", *Phil. Rev.* 113(4), 507–535, doi:10.1215/00318108-113-4-507 [V-xref]: **the body was not read.** Whether Holton treats the toxin case directly is **unverified** ([gaps](#gaps)).

### G. Ainslie (2001), *Breakdown of Will*, on the toxin [V-ocr; lead for `the-divided-will`]

- Ch. 8's theory-scoring table lists "Rational to drink toxin" among its tested properties (the partitioned note L80 counts eight properties).
- "…drinking the toxin is irrational under the null theory and the resolute choice theory. The organ and pattern-seeking theories seem to make no prediction about…"
- On philosophers: "Philosophers have sometimes balked at this conclusion, but have been able to come up with little rational incentive to drink the toxin: only 'savings with respect to decision-making costs' and the promising but vague 'need to coordinate' successive decisions." His notes cite "McClennen (1990, pp. 230-231) on decision costs".
- He attributes "resolute choice" to McClennen as "a sense of commitment to a plan initiated by a prior self". Then: "Using a more complex model, philosopher Michael Bratman argues that it is 'rational to follow through with a prior plan in those circumstances…'".
- "Kavka and Newcomb express opposite ends of the spectrum of how the will can be experienced: Kavka expresses how a significant precedent…". The running head near this reads 138.
- **Lead only.** Ainslie's own claim that intertemporal bargaining makes drinking rational, via precedent, is **not reconstructed** here. If used, it would show the toxin answered by a population of interests with no ego. That belongs in `the-divided-will`, not this fold.

### H. Early replies and secondary reproductions

- **Thomas, J. (1983).** "The toxin, the blood donor and the bomb." *Analysis* 43 (a later issue of the same volume), running head p. 209 [V-scan; issue and pages otherwise unverified]. It refers to the contract's prohibition on "'arrangement of external incentives' and 'alternative gimmicks'". **The earliest reply found here. Lead.**
- **Mele, A. R. (1992).** "Intentions, reasons, and beliefs: Morals of the toxin puzzle." *Philosophical Studies* 68, 171–194. doi:10.1007/bf00354475 [V-xref]. Mele (1996), "Rational Intentions and the Toxin Puzzle", *ProtoSociology* 8, 39–52 [V-xref]. Not read.
- **Bratman (1992)**, "Planning and the stability of intention", *Minds and Machines* 2, doi:10.1007/bf00261286. **DeHelian & McClennen (1993)**, "…: A comment", *Minds and Machines* 3, 319–333, doi:10.1007/bf00976285 [V-xref]. Not read.
- **Kroon**, "Just Imagine" (Advanced Reasoning Forum PDF) [V-raw]. It reproduces Kavka's setup as a block quote, **lightly altered** (it omits "who has offered you the following deal" and the parentheticals). It **paraphrases** the side conditions ("you are to make no bets, do anything that will cause you to become irrational…"). **Quote Kavka from the scan, never from Kroon.**

## Major Positions {#positions}

- **Kavka (1983): intention is constrained by reasons for action.**
  - Claim: you cannot intend, or can do so only with extreme difficulty, what you have no reason to do when you have substantial reason not to.
  - For the Map: neutral. The dispositional account of intention is substrate-neutral.
- **Strong resolution / resolute choice (McClennen 1985, 1990).**
  - Claim: a rational agent sticks with the plan judged best at the outset, even against her ranking at a later node. This holds "in appropriate contexts" (SEP), not for Ulysses-type preference change.
  - For the Map: a normative rule that any planner can implement. It neither supports nor threatens the tenets.
- **Moderate resolution (Gauthier, per Bratman 1998).**
  - Claim: follow-through is rational if the plan's course beats never having settled on it. One "may rationally drink".
  - For the Map: as above.
- **Bratman (1998): sophistication is too simple, resolution goes too far.**
  - Claim: the standard view holds except where the no-regret condition licenses follow-through (some temptation cases), and the toxin fails it. Agency has a temporal and causal location.
  - For the Map: closest to the host's retained override and to Steward's settler (host L98). Still physical-or-agnostic.
- **Sophistication (SEP's default; Levi, Maher, Seidenfeld).**
  - Claim: rational agents plan backwards from predicted later choices, and Ulysses precommits.
  - For the Map: this is the host's subject, precommitment as the sophisticated agent's tool.
- **Holton: resolutions as second-order intentions** (via the akrasia page and Liberman).
  - Claim: built for judgement shift under temptation. Liberman: the second-order intention is equally exposed.
  - For the Map: already covered. Internal, so outside (iii).

## Key Debates {#debates}

1. **Can one intend what one will have no reason to do?**
   - Kavka says no, with the hedge.
   - Gauthier says yes, via plan rationality (as reported).
   - Bratman says not in the toxin case.
   - Current state: open.
2. **Does a plan's rationality transfer to its steps?**
   - Resolute choice says yes.
   - The SEP's standard interpretation says no: "defy the very notion of preference".
   - Bratman: only under no-regret.
3. **Is resolute choice feasible for humans?** McClennen devotes ch. 12 to "The feasibility of resolute choice" and exempts Ulysses and "the potential drug addict". Not read beyond the contents and previews.

## Historical Timeline

| Year | Event | Significance |
|---|---|---|
| 1955–56 | Strotz | "Precommit", "consistent planning"; the unaware agent is a "spendthrift" (p. 165) |
| 1968 | Pollak, "Consistent Planning" (*RES* 35(2): 201–208) [V-xref] | Lead for "naive / sophisticated" |
| 1976 | Hammond, "Changing Tastes and Coherent Dynamic Choice" (*RES* 43(1): 159–173) [V-xref] | Dynamic-consistency framework; body not read |
| 1978 | Kavka, "Some Paradoxes of Deterrence" | Conditional deterrent intentions |
| 1983 | **Kavka, "The toxin puzzle"**; Thomas's reply | Unconditional case; contract excludes external incentives |
| 1985 | **McClennen, "Prisoner's Dilemma and Resolute Choice"** | "Resolute choice" in print |
| 1987 | Bratman, *Intention, Plans, and Practical Reason* | The toxin in planning theory (pp. 101–6 per McClennen) |
| 1990 | McClennen, *Rationality and Dynamic Choice* | Resolute choice developed; Ulysses assigned to sophistication |
| 1994 / 1997 | Gauthier, "Assure and Threaten"; "Resolute Choice and Rational Deliberation" | Plan rationality; modified resolute choice |
| 1998 | Coleman & Morris (eds.), essays for Kavka: Gauthier, Bratman, Harman | Strong vs moderate resolution; the no-regret condition |
| 2001 | Ainslie, *Breakdown of Will* | "Rational to drink toxin" as a test property |
| 2004 / 2009 | Holton, "Rational Resolve"; *Willing, Wanting, Waiting* | Resolutions as second-order intentions |
| 2016 | Liberman, "Reconsidering Resolutions" | The second-order intention is equally exposed |
| 2025 | SEP "Decision Theory" revision | Naive / sophisticated / resolute; sides with sophistication |

## The Map's Question {#maps-question}

This section is the Map's interpretation. No source above argues for it.

1. **Can one intend now what one will have no reason to do later?**
   - Kavka's answer is "no, or only with extreme difficulty", on a dispositional account of intention that suits any planner.
   - The Map need not take sides. What matters for the host is that the case is constructed by forbidding the condition-(iii) route.
2. **What the replies imply about the diachronic agent.**
   - McClennen's resolute agent and the precommitting Ulysses are **complements**. Resolution is what a perfectly rational planner would do; precommitment is the sophisticated fallback for "an imperfectly rational being".
   - Bratman's objection, "temporal and causal location", is a defence of the **retained later override** as the agent's own standpoint. So the host's internal/external line reappears inside the theory of rational intention.
3. **Does resolute choice need anything beyond a persisting planning system?**
   - **Formally, no.** It is a policy rule ("stick to the strategy that was initially deemed best"). Any system that stores and executes a plan can run it. McClennen's own idiom is time-defined "selves", and Ainslie scores it with a population of interests and no ego.
   - **Conceptually it faces the SEP's dilemma**:
     - if later choice points are free, keeping the plan looks like choosing against one's preferences;
     - if they are not, resolute choice posits an *internal* binding, which (iii) keeps outside precommitment and whose formation Kavka doubts.
   - **The persisting subject** ([[tenets/background-commitments|Posit One]]) is held as a commitment. It makes the earlier plan the same agent's plan, so resolute choice would be self-government, not one self legislating for another. It does not say **why the earlier plan should govern now**. That is Bratman's objection, and the host's authority question (#identity-authority) turned inward. **A scope finding, not a weakness.**
4. **Where a selector would sit.** Exactly where the host puts it for precommitment: at the earlier settling, if anywhere. Kavka's case adds only that the earlier settling may be unable to reach the later act without a device. **Fit, not evidence. Resolve phenomenology fits without evidencing, and Tenet 3's quantifier stays unresolved.**

## Draft Fold Passage {#angles}

**Placement**: a new section between "The Override Removed" (ends host L68) and "## Identity and Authority {#identity-authority}" (host L70). Insert it before L70, with one blank line on each side.

**Budget**: 469 words of prose (the heading included) + 70 words for 4 references = **539**. Host 2,772 → **3,311** (measured).

**New references** (insert alphabetically; the host numbers its list explicitly, so renumber):
- Bratman 1998 before Bratman 2007 (current #3);
- Kavka after John (current #14);
- McClennen after Kavka;
- Steele & Stefánsson after Spellecy (current #17), before Steward.

**Wikilinks used**: `[[akrasia-and-weakness-of-will|…]]` (live, bare) and `[[#identity-authority|…]]` (host anchor, L70). No new bare slugs.

```markdown
## The Toxin: Binding Ruled Out {#toxin}

Gregory Kavka's toxin puzzle (1983) closes the external route by stipulation. A billionaire pays a million dollars if at midnight you intend to drink, next afternoon, a toxin that will make you ill for a day; the money comes first, and you are "perfectly free to change your mind" (p. 34). Binding yourself "by today making irreversible arrangements that will give you sufficient independent incentive to drink it" is ruled out by the contract, and a promise to yourself "could help if you were one of those strange people who take pride in never releasing oneself from a promise to oneself", which you are not (pp. 34–35). With binding in Elster's sense forbidden, the case asks whether an intention alone can bind. Kavka's answer is hedged: you cannot "(or have extreme difficulty doing so)", because intentions are "dispositions to act which are based on reasons to act", and you have every reason to intend but none to drink (p. 35).

The replies turn on whether a plan's rationality passes to its steps. Edward McClennen's resolute chooser keeps to the plan judged best at the outset, but he counts Ulysses "an imperfectly rational being" who "must settle for some version or other of sophisticated choice", the backward planning that precommits (1990). On the view Bratman attributes to David Gauthier, "moderate resolution", one may rationally drink, since the course that includes drinking beats never having settled on the plan. Bratman rejects both forms of resolution here as not doing justice to "the significance of temporal and causal location to our agency". His no-regret condition asks, roughly, whether the agent "would not regret sticking with her prior intention" and would regret abandoning it; some temptation cases pass, but in the toxin case "I would regret following through and drinking the toxin" (1998).

On the Map's reading, which none of these authors argues for, resolute choice needs nothing beyond a planning system that stores and executes a plan. Its rule, where it applies, is to "stick to the strategy that was initially deemed best" at every choice point, and its defenders may treat later points as not "really points at which an agent is free to choose" (Steele & Stefánsson 2025). If they are free, keeping the plan looks like choosing against one's preferences; if not, it posits an internal binding, outside condition (iii), of the kind Kavka doubts we can form. A Holtonian resolution, an intention guarded by a second-order one ([[akrasia-and-weakness-of-will|the akrasia article]]), meets Kavka's question one level up wherever no judgement shift is expected. The posited persisting subject makes the earlier plan the same agent's but does not say why it should govern now, which is Bratman's objection and the [[#identity-authority|authority question]] turned inward. Resolve fits a selector and a physical planner equally.
```

```markdown
1. Bratman, M. E. (1998). Toxin, temptation, and the stability of intention. In J. L. Coleman & C. W. Morris (Eds.), *Rational Commitment and Social Justice* (pp. 59–83). Cambridge University Press. https://doi.org/10.1017/cbo9780511527364.006
1. Kavka, G. S. (1983). The toxin puzzle. *Analysis*, 43(1), 33–36. https://doi.org/10.1093/analys/43.1.33
1. McClennen, E. F. (1990). *Rationality and Dynamic Choice: Foundational Explorations*. Cambridge University Press. https://doi.org/10.1017/cbo9780511983979
1. Steele, K., & Stefánsson, H. O. (2025). Decision theory. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/decision-theory/
```

**Why each claim in the draft is safe**:
- "both forms of resolution": strong resolution is Bratman's name for "a version of 'resolute choice'" after McClennen, and moderate is Gauthier's. "here" scopes Bratman's rejection to autonomous-benefit cases ("as applied to our autonomous-[benefit cases]").
- "would regret abandoning it" paraphrases clause (b), because its OCR is split.
- "the backward planning that precommits" glosses sophisticated choice (SEP: "backwards planning"; McClennen: "Sophisticated Ulysses precommits").
- "of the kind Kavka doubts we can form" keeps the host's lead claim intact. Without it, the dilemma's second horn would read as a second, internal override-removing strategy, contradicting the host's scoped "the one self-control strategy" claim (L36, L66). With it, internal binding stays a contested posit, not a strategy the Map lists.
- "one level up" (Holton) is the Map's inference and sits under the Map's-reading label. It parallels Liberman's objection without attributing it to her.

### Optional add-ons {#optional}

Each pushes the host above 3,311.
1. **Lead pointer** (+~22, host L38, after `…sit at the act of binding ([[#placement|explained below]]).`): `Kavka's toxin puzzle, whose terms forbid external binding, tests whether an intention alone can do a device's work ([[#toxin|explained below]]).`
2. **McClennen idiom guard** (+~16, after the Holton sentence): "McClennen's 'resolute self' with 'ties to its own former selves' is a modelling idiom like Strotz's." It was cut for length. Add it back if a reviewer reads the persisting-subject sentence as enlisting McClennen.
3. **Secondary host, `topics/akrasia-and-weakness-of-will` L80** (headroom 348; +~20): after the precommitment sentence, `Kavka's toxin puzzle, which rules out the external route, asks whether a resolution can bind where no temptation shifts the judgement ([[precommitment-and-the-diachronic-agent#toxin|explained there]]).` Only after the host fold lands, since the anchor must exist.

## Guards for the Fold Writer (Binding) {#guards}

### Calibration and tenets
- **Tenet 3.**
  - No "precommitment / resolve / resolute choice shows (reveals, requires) a selector".
  - Resolution phenomenology (Kavka's teeth-gritting "'I will drink that toxin' over and over again", p. 35) fits without evidencing.
  - Tenet 3's quantifier stays unresolved.
  - Keep the closing "Resolve fits a selector and a physical planner equally."
- **Elster's (iii).** Resolutions, resolute choice and self-promises are internal and stay outside (iii), as host L50 frames them. Do not call resolute choice "internal precommitment" as if it met Elster's definition.
- **Tenet 4.**
  - The persisting subject is a **commitment** ([[tenets/background-commitments|Posit One]]), not a result of this literature.
  - No author here argues for a further-fact self. McClennen's "selves" and Ainslie's "prior self" are modelling idioms.
  - Do not enlist Kavka, Gauthier, Bratman, McClennen, Holton or Ainslie for dualism or for persistence.
- **No temporal framework.** No link to `time-collapse-and-agency` (precommitment note, guard 6).
- **Never concede epiphenomenalism.** That the toxin agent cannot will the intention into being does not show that intention is idle. Kavka's point is that intention answers to reasons.
- **Tenet 5 constrains only the Map's own reasoning.** No parsimony charge against sophistication or resolute choice.
- **Kavka's materialist scanner** ("As a cognitive scientist, materialist…", p. 34) is a fictional stipulation that the detector works. **Do not argue that the puzzle presupposes physicalism or that intentions are brain states,** and do not argue the converse.

### Author stances
- **Kavka**: Hobbes scholar and deterrence theorist. His thesis is about intention and reasons. No metaphysics of mind.
- **McClennen**: decision theorist. Resolute choice serves Independence-violating preferences and coordination. **He does not say resolute choice frees Ulysses from the ropes.**
- **Gauthier**: contractarian (constrained maximisation). Report his toxin view **through Bratman** unless his own chapter is read.
- **Bratman**: planning theorist. Do not attribute to him a defence of the persisting subject. "Temporal and causal location" concerns the agent's standpoint at the time of action.
- **Steele & Stefánsson (SEP)**: they **side with sophistication**. Do not present their dilemma as neutral reportage.
- **Holton**: see the akrasia page. **No new Holton quotations** in the host (precommitment note guard stands). The Liberman-quoted p. 11 sentence is [V-sec] and is not needed.
- **Ainslie**: naturalist; interests, not selves. Not used in the fold.

### Coiner and term traps {#coiners}
- **The toxin puzzle**: Kavka 1983. It "emerged from a conversation… with Tyler Burge" (n. 1). Kavka is the author, and Burge is not a co-coiner.
- **"Resolute choice"**:
  - McClennen's term, **in print by 1985** ("Prisoner's Dilemma and Resolute Choice"; the editors put it in scare quotes). This is the earliest found here, not established as the first.
  - **The brief's "(1990)" understates it.**
  - Hammond 1976's body was not read. Nothing found here credits Hammond with "resolute".
  - The SEP credits no coiner for the three approaches.
- **"Sophisticated" / "naive"**:
  - **Strotz 1955–56 uses neither term.** The local PDF text has 0 hits for "sophisticat". "Naive" occurs only adverbially: individuals "who naively resolve now what they 'will do' in the future", p. 177 [V-raw]. His terms are "spendthrift", "precommit", "consistent planning" and the "strategical" man.
  - Pollak 1968 is the lead for the terms.
  - McClennen 1990 writes "myopic (or naive)".
  - **Do not credit Strotz with "sophisticated choice".**
- **"Strong" / "moderate resolution"**: Bratman's labels (1998), not McClennen's or Gauthier's.
- **"No-regret condition"**: Bratman's (1998).
- **"Resolutions"** in the second-order-intention sense: Holton's. **"Resolve"** is Ainslie 2021's. **"Resolute"** is McClennen's. Three words, three authors.
- **"Sophisticated"** here means the dynamic-choice approach. It is **not** the O'Donoghue–Rabin "sophisticates" of the host's L86 (beliefs about one's own bias), though the two are related. Gloss on first use, as the draft does ("the backward planning that precommits").

### Quote status {#quote-status}
- **Cleared, page verified [V-scan]**: Kavka 1983, every sentence quoted in Source A, at the pages shown.
- **Cleared [V-raw]**: SEP Decision Theory (Source E); Liberman 2016's own sentences; Strotz p. 177 "naively resolve".
- **Cleared wording, page unverified [V-ocr]**: Bratman 1998 (Source B); McClennen 1990 (Source D); cite chapter or year, not page.
- **"As quoted in" only**: Holton 2009 p. 11 (via Liberman).
- **Do not quote**:
  - the Gauthier 1998 fragments (chapter attribution unconfirmed);
  - Ainslie's toxin fragments (lead);
  - Harman 1998 (one unattributed fragment only);
  - Kroon's version of Kavka;
  - Holton 2004 (body unread);
  - Mele 1992 and 1996;
  - McClennen 1985 body (title and editors' sentence only).

### Evidence not to lean on
- **No empirical claim** about whether people can form toxin-type intentions was searched. The fold makes none.
- **Newcomb**: Kavka invokes and dismisses it (p. 35). Do not import Newcomb or decision-theoretic evidentialism.
- **The precommitment note's retraction warning** (Ariely & Wertenbroch 2002) stands. No deadline examples.

## Absence and Exclusivity Claims (Scoped) {#absence}

1. **On the Map**: "toxin puzzle" 0, "Kavka" 0, "resolute choice" 0, "McClennen" 0, "sophisticated choice" 0, "no-regret" 0. Positive controls: "Holton" 4, "akrasia" 20, "Bratman" 5. Scope: live `topics/ concepts/ apex/ voids/ positions/`, 2026-10-24 about 18:40Z.
2. **The single live "Gauthier" is Isabel Gauthier**, a different person.
3. **"Resolute choice in print by 1985"** is the earliest *found here*, via the archive.org index and Crossref. It is not a bibliographic census.
4. **"Strotz uses neither term"** is scoped to the one PDF text layer (JSTOR-stamped, 8,371 words).
5. **"The SEP credits no coiner"** is scoped to the "Decision Theory" entry's §6.1 text.
6. **"Holton's toxin stance unverified"** means only that it was not read here. It does not mean he has none.

## Gaps in Research {#gaps}

- **Holton 2004 and 2009** bodies are closed. Whether Holton discusses the toxin case, and how, is unverified. A search summary suggested he holds it "a rational disposition not to rethink" in the toxin case. **[Lead; the subject of that sentence is ambiguous between Holton and Bratman.]**
- **Gauthier's own text** (1994, 1997, 1998) was not read beyond index fragments. His view is reported through Bratman.
- **Harman 1998** (pp. 84–89): one fragment, unattributed ("you can adopt the concern by forming the intention to drink the toxin").
- **McClennen 1990 ch. 12** (feasibility) and **1985** body: not read.
- **Bratman 1987 IPPR** pp. 101–6 and Bratman's later "Temptation Revisited" (2007) and *Planning, Time, and Self-Governance* (2018): not read.
- **Pages** for every [V-ocr] quotation.
- **Hammond 1976**: whether it uses "resolute" or "sophisticated". **Pollak 1968**: whether it coins "naive / sophisticated".
- **Ainslie 2001 ch. 8**: his own bargaining answer to the toxin (Source G).
- **No 2020s literature** on the toxin puzzle was searched (Rudolf and Melis appear in search results as titles only).

## Side-Findings (leads only) {#side-findings}

1. **Precommitment note §D, a coiner risk.** It calls O'Donoghue & Rabin 1999 the "Origin of the sophisticate/naif terminology".
   - The naive/sophisticated distinction predates them: McClennen 1990 uses "myopic (or naive)" and "sophisticated choice", and Pollak 1968 is a lead.
   - They may have introduced the *nouns* "sophisticates" and "naifs" in behavioural economics (unverified).
   - **The host does not carry the claim.** Host L86 quotes John 2020's "partial sophisticates" without attributing the term. Low priority; research note only.
2. **Ainslie's toxin scoring** (Source G) is a ready-made addition to `the-divided-will` (headroom 925). It shows the toxin answered without an ego. **Lead.** Reconstruct his bargaining claim from the book before tasking.
3. **Strotz p. 177**: "individuals who precommit their future actions or who naively resolve now what they 'will do' in the future", and "How familiar the sentence that begins, 'I resolve, starting next . . .'!" [V-raw]. Strotz himself separates precommitting from resolving. This could support host L50 at zero cost if a later edit wants a primary source for the internal/external line. Not needed now.
4. **Thomas 1983** (*Analysis* 43, p. 209 running head) is an early reply that reads the contract's exclusions as "'arrangement of external incentives' and 'alternative gimmicks'". It is the first published reading of the puzzle as a binding problem found here.

## Citations

1. Ainslie, G. (2001). *Breakdown of Will*. Cambridge University Press. https://doi.org/10.1017/CBO9781139164191
2. Bratman, M. E. (1987). *Intention, Plans, and Practical Reason*. Harvard University Press.
3. Bratman, M. E. (1992). Planning and the stability of intention. *Minds and Machines*, 2. https://doi.org/10.1007/bf00261286
4. Bratman, M. E. (1998). Toxin, temptation, and the stability of intention. In J. L. Coleman & C. W. Morris (Eds.), *Rational Commitment and Social Justice: Essays for Gregory Kavka* (pp. 59–83). Cambridge University Press. https://doi.org/10.1017/cbo9780511527364.006
5. DeHelian, L., & McClennen, E. F. (1993). Planning and the stability of intention: A comment. *Minds and Machines*, 3, 319–333. https://doi.org/10.1007/bf00976285
6. Gauthier, D. (1994). Assure and threaten. *Ethics*, 104(4), 690–721. https://doi.org/10.1086/293651
7. Gauthier, D. (1997). Resolute choice and rational deliberation: A critique and a defense. *Noûs*, 31(1), 1–25. https://doi.org/10.1111/0029-4624.00033
8. Gauthier, D. (1998). Rethinking the toxin puzzle. In J. L. Coleman & C. W. Morris (Eds.), *Rational Commitment and Social Justice* (pp. 47–58). Cambridge University Press. https://doi.org/10.1017/cbo9780511527364.005
9. Hammond, P. J. (1976). Changing tastes and coherent dynamic choice. *Review of Economic Studies*, 43(1), 159–173. https://doi.org/10.2307/2296609
10. Harman, G. (1998). The toxin puzzle. In J. L. Coleman & C. W. Morris (Eds.), *Rational Commitment and Social Justice* (pp. 84–89). Cambridge University Press. https://doi.org/10.1017/cbo9780511527364.007
11. Holton, R. (2004). Rational resolve. *Philosophical Review*, 113(4), 507–535. https://doi.org/10.1215/00318108-113-4-507
12. Holton, R. (2009). *Willing, Wanting, Waiting*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199214570.001.0001
13. Kavka, G. S. (1978). Some paradoxes of deterrence. *Journal of Philosophy*, 75, 285–302. [V-ocr, as cited in Bratman 1987]
14. Kavka, G. S. (1983). The toxin puzzle. *Analysis*, 43(1), 33–36. https://doi.org/10.1093/analys/43.1.33
15. Liberman, A. (2016). Reconsidering resolutions. *Journal of Ethics and Social Philosophy*, 10(2), 1–27. https://doi.org/10.26556/jesp.v10i2.98
16. McClennen, E. F. (1985). Prisoner's dilemma and resolute choice. In R. Campbell & L. Sowden (Eds.), *Paradoxes of Rationality and Cooperation* (pp. 94–104). University of British Columbia Press. https://doi.org/10.59962/9780774857154-006
17. McClennen, E. F. (1988). Constrained maximization and resolute choice. *Social Philosophy and Policy*, 5(2), 95–118. https://doi.org/10.1017/s026505250000008x
18. McClennen, E. F. (1990). *Rationality and Dynamic Choice: Foundational Explorations*. Cambridge University Press. https://doi.org/10.1017/cbo9780511983979
19. Mele, A. R. (1992). Intentions, reasons, and beliefs: Morals of the toxin puzzle. *Philosophical Studies*, 68, 171–194. https://doi.org/10.1007/bf00354475
20. Pollak, R. A. (1968). Consistent planning. *Review of Economic Studies*, 35(2), 201–208. https://doi.org/10.2307/2296548
21. Steele, K., & Stefánsson, H. O. (2025). Decision theory. *Stanford Encyclopedia of Philosophy* (substantive revision 20 August 2025). https://plato.stanford.edu/entries/decision-theory/
22. Strotz, R. H. (1955–56). Myopia and inconsistency in dynamic utility maximization. *Review of Economic Studies*, 23(3), 165–180. https://doi.org/10.2307/2295722
23. Thomas, J. (1983). The toxin, the blood donor and the bomb. *Analysis*, 43. [V-scan of running head p. 209; issue and full pages unverified]
