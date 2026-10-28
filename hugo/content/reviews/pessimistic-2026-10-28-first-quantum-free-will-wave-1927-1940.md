---
ai_contribution: 100
ai_generated_date: 2026-10-28
ai_modified: 2026-10-28 17:48:10+00:00
ai_system: claude-fable-5-1
author: null
concepts:
- '[[quantum-indeterminacy-free-will]]'
- '[[popper-three-worlds-interactionism]]'
- '[[trilemma-of-selection]]'
- '[[ensemble-level-epiphenomenalism]]'
created: 2026-10-28
date: &id001 2026-10-28
description: First review of any kind for topics/first-quantum-free-will-wave-1927-1940
  (created 2026-10-28). All 41 sampled quotations hit the raw scans; two source-fidelity
  defects (the Russell gloss, Schrödinger's second horn), one reasoning-mode defect
  (Tenet 5 turned on Schlick), and three upgrades of non-replies into replies.
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-10-28 17:48:10+00:00
modified: *id001
related_articles:
- '[[topics/first-quantum-free-will-wave-1927-1940]]'
- '[[research/first-quantum-free-will-wave-1927-1940-2026-10-27]]'
- '[[positions/quantum-interface]]'
title: Pessimistic Review - 2026-10-28 - The First Quantum Free-Will Wave, 1927–1940
topics:
- '[[free-will]]'
- '[[history-of-the-interaction-problem]]'
---

# Pessimistic Review

**Date**: 2026-10-28
**Content reviewed**: `obsidian/topics/first-quantum-free-will-wave-1927-1940.md` (3,421 words by `analyze_length`: prose ~2,774 + Further Reading 64 + References 595; topics band 3000/4000/6000, hard gate at >= 4000, headroom 579). Created 2026-10-28 ~09:52Z from [first-quantum-free-will-wave-1927-1940-2026-10-27](/research/first-quantum-free-will-wave-1927-1940-2026-10-27/); no prior review of any kind.

## Executive Summary

The page's quotation discipline holds: every one of 41 quoted spans sampled across Eddington 1928, Eddington 1935, Planck 1932, Jeans 1933, Schlick 1939 (both scans), Popper's OCR and Davidson 1942 was found in the raw text once the OCR noise was normalised, and no quotation marks sit on a carrier-only source (Schrödinger, Hobart, Stebbing, Bohr, Jordan, Lillie, Compton are all paraphrased with the carrier named). The defects are in the glosses around the quotations, not in the quotations. Two are source-fidelity errors verifiable on disk: L59 makes Russell contrast Eddington's free-will argument with "the determinist's", when Russell's p. 121 sentence (quoted at Eddington 1935 pp. 306–307) contrasts it with the entropy argument for a Creator that Eddington declined; and L53 gives Schrödinger's second horn the antecedent "if it does not [ride on a quantum event]", when the 1936 note's second horn is "if that is denied", that is, if the agent cannot alter the odds. The page also upgrades three figures who did not reply to the wave into repliers (Schrödinger "answered" Eddington in 1936 at L83; Bohr sits in the "Jordan drew his own critics" paragraph at L63; "more than ten contemporaries answered it" at L27 counts Hobart and Schlick 1930, whom the page itself says never addressed physics). In the Relation section the reply to the randomness objection deploys Tenet 5 against Schlick and leans on Popper's label "clearly absurd" where an in-framework reply on Schlick's own definitions is available and stronger. Banned constructions: none. Altered-state symmetry audit: not applicable (no supportive-cluster items cited).

## Quotation Sample (hits/misses, with the pattern used)

Method: both the quotation and the whole scan were reduced to lowercase alphanumerics only (`re.sub(r"[^a-z0-9]","",NFKC(text))`), so double-spaced words, line-end hyphenation, curly apostrophes and running heads cannot produce a false zero; the match is a substring search on that reduced text, with the raw context printed for every hit. Script: scratchpad `pr/qcheck.py`, `pr/chase.py`, `pr/chase2.py`, `pr/chase3.py` (session aa88bc03).

| Source (scan) | Spans sampled | First-pass hits | After chasing with li/th-free anchors | Notes |
|---|---|---|---|---|
| Eddington 1928, `edd_natureofphysical00eddi.txt` | 13 (L35 x3, L41 x5, L43 x5) | 12 | 13 | The one miss was the running head "MIND AND STATISTICAL LAWS 313" inserted between "physically" and "improbable", which confirms the pp. 312–313 locator |
| Eddington 1935, `eddington1935_dli.txt` | 9 (L35 x2, L45 x5, L59 x2) | 4 | 9 | DLI OCR renders *li* as *h/H/U* and *th* as *di/tli* ("dayHght", "Aldiough", "biUions", "vohtion", "hmited", "modem"); all nine present at the stated pages (p. 87 head "88" follows the chink sentence; p. 89 head precedes "single volition") |
| Planck 1932, `planck1932.txt` | 4 (L59) | 4 | 4 | |
| Jeans 1933, `jeans1933.txt` | 3 (L37, L61 x2) | 3 | 3 | Full keyhole span hit as one piece |
| Schlick 1939, `schlick1939_dli.txt` + `_mbp.txt` | 4 (L49) | 2 | 4 | p. 150 span broke on "lyifree" (OCR of "unfree") in the following clause; both scans carry "Freedom means the opposite of compulsion; a man is free if he does not act under compulsion" at p. 150, and the p. 156 chance passage verbatim |
| Popper OCR, `raw/popper.txt` | 6 (L51 x4, L89, L33) | 6 | 6 | "where chance begins" straddles the p. 227 head; "clearly absurd" at p. 228; "by influencing or selecting some quantum jumps" at p. 233; Lillie carrier confirmed at Popper's note ("begins, it appears, with a paper by Ralph Lillie, Science, 46 [OCR], 1927, pp. 139 ff.") |
| Davidson 1942, `davidson1942.txt` | 2 (L55) | 2 | 2 | "misleading theologians, preachers, and even philosophers 'who should have known better'" at p. 89 |
| **Total** | **41** | **33** | **41** | Zero misses after flexible matching; zero quotation marks on carrier-only sources |

Carrier re-checks: Davis 2009 n. 68 reads "he, too, stressed the role of consciousness in amplifying uncertainties at the microscopic level" (`davis2b.txt` L1016–1017), so L45's report of Davis is accurate. The Information Philosopher's Schrödinger page (fetched 17:4xZ) confirms "I consider this hope an illusion, for the following general reasons", "First, that the laws of Nature are after all at 'my' mercy", "Or, secondly, if that is denied, why on earth do I feel responsible", "There is no ψ-function in life", the Donnan prompt, and that Schrödinger's text names neither Eddington nor Compton (the site's headline does). Compton's 1931 caveat ("Of course this does not necessarily mean that the living organism is free") is in the 1931 *Science* note per the sibling research note, so L33's "in 1931" is right.

## Critiques by Philosopher

### The Eliminative Materialist
Churchland would read the page as an unintended confession. The Map's selection posit is a 1928 hypothesis that its own author called "one of the most dubious points in the theory of the interaction of mind and matter", and the page shows that in ninety-eight years the posit has acquired no mechanism, only a renamed debt. A research programme whose central move was stated, costed and declined by Eddington before neuroscience existed is folk psychology awaiting elimination, and the page's own table has two critics (Planck, Russell) marked "Unused" and unanswered.

### The Hard-Nosed Physicalist
Dennett would fasten on Eddington's "conscious unit" whose "behaviour symbolises a single volition of the spirit" and on the Map's "indexical character of which outcome a subject actualises": both are homunculi placed where the explanation should be. He would note that the page's reply to Schlick (L89) rejects the chance/causation partition instead of saying what the selecting mind is, which is the Cartesian theatre's standard move. He would also point out that Schrödinger's own conclusion, omitted at L53, was that "the plurality of possible events" in a free action is a self-deception, a deflationary line the page does not engage.

### The Quantum Skeptic
Tegmark would observe that the page omits the one sentence of Schrödinger 1936 that anticipates him: "The material units which determine the processes of life seem to be large enough" to be shielded from quantum uncertainty (carrier text, in the research note at L129). The decoherence objection was on the table in 1936 from the physicist whose dilemma the page borrows, and the page uses only the dilemma. Eddington's "many billions of atoms" unit (L45) is, on Tegmark's reading, a concession that no single-event amplifier is credible.

### The Many-Worlds Defender
Deutsch has little purchase on a historical page, and the page says Tenet 4 is not engaged (L89). His one remark: Eddington's "decision between the possible behaviours is what we call volition" (L35) is exactly the branch-relative description Everett makes literal; the page treats "possible behaviours" as alternatives that one agent selects among without noting that the selection posit's single-outcome assumption is doing silent work (see the Tenet 4 note on "objective single-outcome actualization" in the tenets matrix).

### The Empiricist
Popper's ghost would approve of the page's honesty about carriers and would press one point: Planck's self-reference argument ("no eye can see itself", L59, L77) is an argument that the felt openness of volition is unfalsifiable from inside, and the page registers it as "Unused" without saying whether the Map's indexical reply is any better placed. He would also notice that L83's "The Map escapes his first horn" is asserted as a result where only the empirical half (no detectable odds-alteration) is secured.

### The Buddhist Philosopher
Nagarjuna would say the whole 1927–1940 argument, and the Map's reading of it, turns on a selector who is one thing: Eddington's "Ego" and "unitary nature of that which in reality it represents" (L45), the Map's "which outcome a subject actualises" (L83). The page records Schlick's partition as definitional and rejects it; it does not notice that the self which is to fall "between chance and determinism" is being posited by the same stroke. Planck's "the observing subject would also be the object of research" is closer to the Madhyamaka point than the page allows, and it is "Unused".

## Critical Issues (ranked)

### Issue 1: L59 misreads Russell's "based on knowledge" contrast
- **File**: obsidian/topics/first-quantum-free-will-wave-1927-1940.md
- **Location**: L59: "called Eddington's free-will argument one based on ignorance where the determinist's was based on knowledge."
- **Problem**: Raw (`eddington1935_dli.txt`, pp. 306–307, quoting Russell p. 121): "It will be seen that Eddington, in this passage, does not infer a definite act of creation by a Creator. His only reason for not doing so is that he does not like the idea. The scientific argument leading to the conclusion which he rejects is much stronger than the argument in favour of free will, since that is based on ignorance, whereas the one we are now considering is based upon knowledge." The knowledge-based argument is the entropy argument for a Creator, which Eddington declined; Russell's point is that Eddington accepts weak arguments for conclusions he likes and rejects strong ones for conclusions he dislikes. "The determinist's" argument is not in the passage. The research note (L74) carried the sentence correctly; the gloss was added at article-writing time.
- **Severity**: High (source fidelity; the raw text is on disk and says otherwise)
- **Recommendation**: Length-neutral rewrite: "called Eddington's free-will argument one based on ignorance, weaker than the entropy argument for a Creator, based on knowledge, which Eddington declined" (−1 word). Table row L74 ("Epistemic: indeterminacy is ignorance") can stand.

### Issue 2: L53 misstates the antecedent of Schrödinger's second horn
- **File**: obsidian/topics/first-quantum-free-will-wave-1927-1940.md
- **Location**: L53: "if a decision rides on an indeterminate quantum event, the laws of nature are at the agent's mercy; if it does not, there is no reason to feel responsible for it."
- **Problem**: The carrier text runs "First, that the laws of Nature are after all at 'my' mercy. ... Or, secondly, if that is denied, why on earth do I feel responsible". "That" is the agent's ability to alter the odds (Schrödinger's 30:70 smoking example); the second horn is the case where the decision is quantum-statistical and *uncontrolled*, so "the frequency of my sinning is determined by Heisenberg's principle". It is not the case where the decision does not ride on a quantum event. The page's own L83 mapping ("a selection that leaves the statistics untouched must say what distinguishes it from chance") is faithful to the real second horn, so L53 and L83 currently disagree about what the dilemma is.
- **Severity**: High (source fidelity on the page's central historical hinge; the carrier is the only text the page has for Schrödinger, and the page departs from it)
- **Recommendation**: Length-neutral: "if a decision rides on a quantum event whose odds the agent can alter, the laws of nature are at the agent's mercy; if the agent cannot alter them, the frequency of his acts is fixed by Heisenberg's principle and there is no reason to feel responsible" (+8 words, recoverable from the sentence that follows, "named by a physicist of the first rank", see Issue 4).

### Issue 3: L89 turns Tenet 5 on Schlick and substitutes Popper's verdict for an argument
- **File**: obsidian/topics/first-quantum-free-will-wave-1927-1940.md
- **Location**: L89: "Schlick's 'there is no other opposite of causality' is a definitional partition, and the Map rejects it with Popper, who called the thesis that nothing can lie between perfect chance and perfect determinism 'clearly absurd' (p. 228). A dichotomy adopted for its tidiness, under incomplete knowledge of what a selecting mind would be, is no evidence that the middle is empty".
- **Problem**: Two house-rule failures in one paragraph. (a) Tenet 5 constrains the Map's own parsimony reasoning; here it is deployed outward ("adopted for its tidiness ... no evidence that the middle is empty") against an opponent's definition. (b) The "rejection" rests on Popper's label "clearly absurd" without Popper's argument (plastic control, p. 232), which the page's Popper host presents and this page does not. Reasoning-mode classification: a missed in-framework reply rather than boundary-substitution, since the page does not claim to refute Schlick inside his framework; but the in-framework reply is available and better. On Schlick's own definitions (p. 156: chance = absence of a cause; p. 150: freedom = non-compulsion), the Map's posit is not a decision "utterly without any cause": the selected outcome has a cause, the agent's selection, so it falls on the causal side of Schlick's partition, and what Schlick can then demand is the mechanism, which is exactly the debt the page already books at L83. Rejecting the partition instead concedes that selection sits "between chance and determinism", imports Popper's undefined middle, and leaves the page open to Schlick's reply that an undefined middle is just chance under another name (the "Schlick complaint up a level" the Popper host already records at its L80).
- **Severity**: Medium (reasoning mode; house rule on Tenet 5)
- **Recommendation**: Length-neutral replacement of the two sentences: keep Popper's verdict as Popper's; state the in-framework point (on Schlick's definitions the posit is causal, not causeless, so his p. 156 case does not describe it; what remains owed is the mechanism); drop the "adopted for its tidiness" clause; retain "rejecting it does not fill the middle, which is the debt above" or its equivalent. Tenet 5's paragraph can then say what Tenet 5 actually licenses here: the Map does not take the tidiness of Schlick's dichotomy as a reason to believe it, and equally does not take the tidiness of its own selection story as a reason to believe that.

### Issue 4: Three non-replies upgraded into replies (L83, L63, L27; also L53)
- **File**: obsidian/topics/first-quantum-free-will-wave-1927-1940.md
- **Location**: L83: "The dilemma was stated and chosen on in 1928 and answered in 1936". L53: "The first horn is the cost of Eddington's choice, named by a physicist of the first rank". L63: Bohr's "Light and Life" closes the paragraph that opens "Jordan drew his own critics". L27: "more than ten contemporaries answered it".
- **Problem**: (a) L53 states that Schrödinger names neither Eddington nor Compton and was prompted by Donnan; L83 then has him "answer" Eddington's 1928 choice. (b) The research note (L114, L260) records that whether Bohr ever criticised Jordan's amplifier "was not established", and Joaquim et al. 2015 call Jordan a follower of Bohr; the page's evidence for Bohr's position is three hocr fragments, while the one verified Bohr text on volition (1930, via Eddington 1935 p. 72) goes unused. Placing Bohr in the critics' paragraph is an upgrade by position. (c) The "more than ten" who "answered" includes Hobart ("contains no physics", L49), Schlick 1930 ("never mentions quantum physics", L49) and Bohr; the count of those who addressed the wave is at most ten (Eddington against Lillie, Russell, Planck, Schlick 1935, Schrödinger, Stebbing, Jeans, Zilsel, Neurath, Frank, Bünning, with Schrödinger addressing Donnan's hope rather than any named builder).
- **Severity**: Medium (attribution; the convergence rule says several critics on the randomness objection count as one observation, and padding the count works against that rule)
- **Recommendation**: L83 "answered in 1936" → "its cost named independently in 1936"; L53 drop "named by a physicist of the first rank" (the words pay for Issue 2); L63 either move Bohr to the Jeans/Planck paragraph with "not established as a critic of Jordan" or cut the sentence (−27 words); L27 "more than ten contemporaries answered it" → "a dozen contemporaries wrote against or around it".

### Issue 5: L83 "The Map escapes his first horn, since no law is at the agent's mercy" (epistemic/metaphysical check)
- **File**: obsidian/topics/first-quantum-free-will-wave-1927-1940.md
- **Location**: L83
- **Problem**: On Schrödinger's first horn as he stated it (the agent alters the odds), Born-preservation does escape, and the sentence is defensible. But "no law is at the agent's mercy" claims more than the evidence supports: what is secured is that no *statistical* regularity is detectably violated (the epistemic/empirical reading); under per-trial selection the individual outcome is at the agent's mercy, and whether the Born rule is a law about ensembles only or also a law about what fixes single events is the open question [P-Q3](/positions/quantum-interface/#mechanism-debt) books. The page states the debt in the next clause, so this is a wording-level equivocation, not a structural one.
- **Severity**: Low–Medium
- **Recommendation**: "escapes his first horn as he stated it, since no odds are altered, at the price of making each outcome depend on the agent, which is what his second horn then asks about" (+10 words; recoverable from Issue 4's cuts).

### Issue 6: L37 "his content is given by title only" is not quite true
- **File**: obsidian/topics/first-quantum-free-will-wave-1927-1940.md
- **Location**: L37: "held that organisms amplify single quantum events in control centres into macroscopic behaviour; his 1934 *Erkenntnis* paper extended it to psychology and the will and offered it, in Mach's name, as positivism. None of Jordan's physiology was read for this article, so his content is given by title only."
- **Problem**: "single quantum events in control centres" and "in Mach's name" are not in any title; they come from Howard's MPRL chapter and the psiquadrat seminar page (research note L101, L108–109). The disclosure understates the carriers rather than the content; the content is within what the note licenses.
- **Severity**: Low
- **Recommendation**: "so his content is given from titles and Howard's summary only" (+3 words).

## Counterarguments to Address

### "The historical finding cuts against the Map, not for it"
- **Current content says**: the Map's position is "the road not taken rather than a discovery" (L83), and Eddington stated the Tenet 2 line "a century early".
- **A critic would argue**: Eddington stated it and declined it because confining influence to outcomes "neither of which would be improbable" leaves "its opportunity of interference ... too circumscribed to bring about the results which are observed to follow from mental decisions" (p. 313, quoted at L43). The Map's reply is neural amplification (L85), but amplification of a Born-preserving per-trial selection reproduces Schrödinger's second horn at the level of the agent's lifetime statistics: if every amplified selection tracks the agent's reasons, the ensemble over that agent's decisions is biased, and the Born-preservation claim is about which ensemble. The page does not say which ensemble.
- **Suggested response**: one clause pointing to where [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/) or [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/) states the reference-class question, rather than a new argument here.

### "Schlick's partition is satisfiable, so stop rejecting it"
- **Current content says**: the Map rejects "there is no other opposite of causality" as a definitional partition (L89).
- **A critic would argue**: a Schlickian would welcome the Map's posit as a *causal* story (the agent's selection causes the outcome) and ask only for the causal mechanism; by rejecting the partition the page volunteers for the harder, Popperian position of defending an undefined middle.
- **Suggested response**: Issue 3's rewrite.

### "Planck and Russell are unanswered and you say so"
- **Current content says**: both "remain available to an opponent and neither has been answered on its pages" (L77).
- **A critic would argue**: Planck's self-reference argument is an alternative explanation of the felt openness the Map's agency cluster treats as evidence (the introspective datum the agency route to Tenet 3 leans on), and leaving it "Unused" leaves that cluster exposed.
- **Suggested response**: out of scope for this page; the open cross-review task should hand the Planck lead to the agency cluster rather than this page absorbing it.

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| "the determinist's was based on knowledge" | L59 | None available; the raw passage contrasts with the Creator argument (Issue 1) |
| Schrödinger's second horn is the non-quantum case | L53 | Carrier text says "if that is denied" = cannot alter the odds (Issue 2) |
| Bohr belongs among Jordan's critics | L63 (by paragraph placement) | Research note: not established; Joaquim et al. make Jordan a follower of Bohr (Issue 4b) |
| "more than ten contemporaries answered it" | L27 | Count excluding Hobart, Schlick 1930 and Bohr is at most ten (Issue 4c) |
| "the strongest objection to it" is older than the Map | L29 | Which objection is meant is never named; the Relation section treats the randomness/indistinguishability dilemma as the debt and the magnitude objection as answered by amplification |
| Jordan "in control centres" | L37 | Licensed by Howard's chapter, not by a title; adjust the disclosure (Issue 6) |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "answered in 1936" (L83) | Upgrades a Donnan-prompted note into a reply to Eddington | "its cost named independently in 1936" |
| "named by a physicist of the first rank" (L53) | Prestige doing argumentative work; 8 words | delete |
| "a century early" (L83) | 1928 → 2026 is 98 years; rhetorical rounding on a page whose point is dating | "ninety-eight years early" or "in 1928" |
| "more than ten contemporaries answered it" (L27) | Count includes non-repliers | "a dozen contemporaries wrote against or around it" |
| "The Map escapes his first horn" (L83) | Result-register for a conditional | "escapes his first horn as he stated it" |
| "his content is given by title only" (L37) | Understates the carriers used | "from titles and Howard's summary only" |

Banned constructions: `load-bearing` 0 hits; "This is not X. It is Y." 0 hits by regex (`(is|are|was) not [^.]*\. (It|This|They) (is|are|was)`) and by a manual read of every "not ... rather than" and "not ..., but" sentence (L29, L43, L45, L83, L87, L89 all keep the contrast inside one clause). Forbidden editor-vocabulary labels (`direct-refutation-feasible`, `bedrock-perimeter`, `Evidential status:` callouts, etc.): 0.

## House-Rule Audit

- **Epiphenomenalism never conceded**: holds. L83 books the mechanism debt against [quantum-interface](/positions/quantum-interface/#mechanism-debt) and says "rather than conceding epiphenomenalism".
- **No builder enlisted for dualism**: holds. L87 firewalls Eddington (mind-stuff), Compton (evolutionary efficacy, inner awareness), Jordan (Machian positivism), Lillie (unread). Outside the Relation section, L29 ("None of the four builders is a witness for the Map's dualism") and L33–37 keep to structure. One soft spot: L83 "states the tenet's distinction a century early" reads as lineage; it is a structural parallel and the paragraph says so two sentences later.
- **Tenet 5 only inward**: fails at L89 (Issue 3).
- **Convergence counts as one observation**: holds in the Relation section; L27's head-count works against it (Issue 4c).
- **Altered-state symmetry (Audit Two)**: gate 1 fails (no supportive-cluster items cited); audit does not apply.
- **Style guide**: front-loaded lead (L27–29) with named anchors; Relation section present and substantive; background is selective. The table at L67–75 is the page's best LLM-facing asset.

## Host-Sentence Fidelity (four inbound links)

| Host | What the host says the page establishes | Page | Verdict |
|---|---|---|---|
| `topics/sherrington-dualist-lineage` L95 | "the amplifier vocabulary Ralph Lillie had introduced in *Science* in 1927, which Compton built his decision model on and Popper would later dispute" | L33: Lillie 1927 originates the image; Compton cites him; Popper's penny-toss via the Popper page | Matches |
| `concepts/popper-three-worlds-interactionism` L64 | "as Ralph Lillie had argued in 1927, [the nervous system] is itself such an amplifier" | L27, L33 | Matches (both pages rest on carriers; Popper's note and Compton 1931 name Lillie) |
| `topics/trilemma-of-selection` L58 (Horn 2) | "openness alone is not freedom" piped to the page | L47–55 randomness section | Matches; the pipe lands on a page whose Randomness section is the generic form, which is what Horn 2 wants |
| `concepts/quantum-indeterminacy-free-will` L33 | `related_articles` membership only | — | Nothing asserted; nothing to check |

`concepts/popper-three-worlds-interactionism` L70 still reads "the doctrine that chance is the only alternative to determinism" with no date and no Jordan; the cross-review task at todo L3570 says a refine at "L3602" owns this clause, but no open task mentions it (grep for `Schlick 1935`, `dating clause`, `popper-three-worlds`, `only alternative` in the open section: only L3577 itself). The owner has been completed, moved or never minted. Not minted here (integration is the cross-review's remit); recorded for the driver.

## Strengths (Brief)

- Quotation discipline is the best of any page reviewed this month: 41/41 verified, carriers named in prose and in the References provenance note, Stebbing deliberately unquoted.
- The dating work is genuinely new to the corpus: Schlick dated twice, Schrödinger's Donnan prompt, Eddington's magnitude objection placed before Compton, Davis n. 68 corrected against the raw chapters.
- The "Who Established What" table with "Unused" rows is an honest map of the Map's own gaps.
- The Dualism paragraph (L87) is a model firewall and should be preserved verbatim through the refine passes.