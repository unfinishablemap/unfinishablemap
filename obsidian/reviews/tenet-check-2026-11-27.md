---
title: Tenet Alignment Check - 2026-11-27
created: 2026-11-27
modified: 2026-11-27
human_modified:
ai_modified: 2026-11-27T12:31:48+00:00
draft: false
description: "Tenet check 171: a delta check of the 83 pages edited since 2026-11-25T00:00Z plus four corpus-wide sweeps. No Errors. 18 Warnings: eight Tenet 5 scope misstatements, four void support claims, six over-reach."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-27
last_curated:
last_deep_review:
---

# Tenet Alignment Check

**Date**: 2026-11-27
**Files checked**: 83 in the window, plus four corpus-wide sweeps. The window is every page under apex, concepts, positions, tenets, topics and voids with a commit since 2026-11-25T00:00:00Z: apex 7, concepts 26, positions 4, tenets 1, topics 18, voids 27. That includes the two section index files `apex/apex-articles` and `voids/voids`. Of the 83, 61 were committed after the 2026-11-25 report (15:32Z); the other 22 were covered there and are re-read here. The sweeps covered 950 pages (topics 371, concepts 371, voids 125, apex 45, positions 30, arguments 6, tenets 2), with research notes for the Tenet 5 pattern.
**Errors**: 0
**Warnings**: 18 (eight Tenet 5 scope misstatements, four void support claims against P-V3, six over-reach or posit-as-result)
**Notes**: 13

## Summary

Nothing in the window or the corpus contradicts a tenet. No page concedes epiphenomenalism in the Map's own voice, endorses many-worlds, or uses parsimony as a decisive argument against dualism.

The window's edits to tenet sections hold the grade. Thirty-two pages had tenet-section body changes, and every changed sentence reads at the rung it earns. Examples:

- `voids/valence-void` L115–L119 and `voids/compound-failure-signatures` L143 now carry P-V3. "finds particularly strong support" and "gains support from two directions" have 0 hits in the corpus.
- `concepts/metacognition` L180–L188 now says "fits irreducibility without evidencing it", and its L184 has the correct Tenet 5 form: "binds the Map's own preference for a conscious threshold equally".
- `concepts/mine-ness` L136–L148 names Laukkonen, Friston and Chandaria as "the Map's strongest physicalist rival, unrefuted (P-RR2)".
- `voids/interested-party-void` L100 states Nagel's stance and names active inference as the rival that predicts the tilt.
- The four pages fixed at d0d296c2 (11:16Z today) now give the correct reason, e.g. `concepts/basic-argument-and-constitutive-luck` L135: "The tenet limits appeals to simplicity on both sides, and the compatibilist and event-causal replies rest on none".

The corpus sweeps found three things the window did not:

1. **The Tenet 5 scope misreading is wider than four pages.** Eight more live pages say or imply that the tenet binds only the Map (A1–A8). Four of them carry an explicit "only", as the fixed four did. The misreading also has upstream seeds that will keep producing it. Six open todo tasks prescribe "Tenet 5 constrains only the Map's own reasoning" as a calibration rule in their Notes (Note 1). And four October tenet checks used "Tenet 5 binds only the Map's reasoning" as a pass standard and listed several of today's eight pages as models of it.
2. **Four voids still read the void as support for a tenet** (B1–B4), against P-V3. All four were raised by earlier checks (between 10-20 and 11-25), and none was minted.
3. **One page argues for the Map from parsimony.** `topics/the-strong-emergence-of-consciousness` L167 says the parsimony advantage "tilts back toward strong emergence with mechanism" (C6), against `tenets.md` L147.

As on 2026-11-20 and 2026-11-25, the commonest window failure is a sentence left at the old grade beside a re-graded sibling. `concepts/nihilism-and-existentialism` L48 was re-graded on 2026-11-26 ("Neither Sartre nor Heidegger argued for dualism"), but its tenet section L114 and L122 were not (C4).

**Method.** I extracted the window's body diff for all 83 files against `aba2c6ed65` (the last commit before 2026-11-25T00:00Z): 835 changed lines, frontmatter excluded. I read the whole tenet section of all 81 pages that have one, about 25,200 words. The four positions pages have no tenet section; for them I read the diff, which contains only calibration notes. I read `tenets.md` in full. For the 170 changed lines outside tenet sections that use tenet vocabulary, I filtered for unnegated strong-claim sentences (19) and read them; none is a tenet issue. Every quoted string below has `str.count == 1` in the live file. Before calling a sentence over-reach, I read the page's own concession to its end. A sentence already marked "on the Map's reading" or "the Map holds" was treated as the Map's voice.

### Sweep counts and positive controls

| Pattern | Scope | Hits | Positive control (expected hit, found) |
|---|---|---|---|
| 1a. Tenet 5 scope: 16 phrase variants ("only the Map's", "binds only", "constrains only", "governs only the Map", "the Map's own reasoning", "lesson is for the Map", …) | all of `obsidian/` except workflow and reviews | 84 lines (apex 3, concepts 17, positions 2, tenets 3, topics 15, voids 2, project 14, research 28) | The four pages fixed at d0d296c2, read from the base tree `aba2c6ed65`: 1 hit each, 4/4 |
| 1b. Tenet 5 scope: a line naming Occam, Tenet 5 or parsimony that also says "Map's own", "binds/governs/constrains the Map", "no charge against", "not its critics" | same | 162 lines (research 53) | `tenets.md` L145 "binds the Map's use of parsimony, not only its critics'" |
| 1 combined, non-research | content and project | 148 loci, each read in sentence context | — |
| 2a. P-V3: support vocabulary in a void's tenet section (support, strengthen, evidence, confirm, reinforce, corroborate, vindicate, lends weight, …) | all 125 voids (each has a tenet section) | 283 sentences; 60 with no negation in the sentence, all read | `voids/capability-division-problem` L120, the 2026-11-25 Note 4 sentence |
| 2b. P-V3: positive support verbs ("finds … support", "is supported by", "strengthens the", "provides … evidence", …) | same | 44 matches; 8 with no negation nearby, all read; the other 36 checked as genuinely negated | `voids/creative-aesthetic-void` L180 "None of the Map's … commitments is supported by this void" (negated form) |
| 2c. P-V3: "what dualism/the tenet predicts", "one would expect", "would be expected" | same | 9 | `voids/necessary-opacity` L156, a window page read in full |
| 3. Epiphenomenalism concession ("epiphenomenalism is/may be true or correct", "causally idle/inert", "makes no difference", "along for the ride", "the Map concedes … epiphenomenal", …) | 950 content pages | 301 hits in 173 files; 42 with no hedge, attribution or negation marker, all read; hedged hits with "Map"/"we" also read (21) | `tenets.md` L109 "along for the ride" (Rules-out) and L93; `apex/embodied-interface` L125 "causally idle" (the open NEEDS-HUMAN reading) |
| 4a. Many-worlds in the Map's voice ("MWI/many-worlds/Everett is true or correct", "all branches are equally real", "the Map accepts MWI", …) | 950 content pages | 20 hits in 19 files; 4 unhedged, all definitions | `tenets.md` L115 (the tenet's own Definition: "All branches are equally real.") |
| 4b. Parsimony as decisive ("parsimony favours/settles/tilts", "decisively favours", "parsimony advantage", "simpler and therefore", …) | 950 content pages | 49 hits in 40 files; 9 unhedged, all read, plus every hit on a Map-favouring line | `topics/interventionist-and-counterfactual-dualism` L108 "simpler and therefore truer" (in a correct self-binding sentence) |
| Co-optation roster, tenet sections of the 81 window pages | — | 14 name hits (McGinn 3, Metzinger 2, Dennett 2, Damasio 2, Nagel, Zahavi, Friston, Sartre, Heidegger) | `voids/interested-party-void` L100 (Nagel, stance stated) |

## Errors

None.

Pattern 3 found no concession. The 42 unhedged hits are rivals described ("Epiphenomenalism holds that …"), Kim's dilemma stated as his conclusion, Further Reading glosses ("The view that consciousness is causally inert"), a hypothetical AI scenario (`concepts/ai-epiphenomenalism` L43), or the Map's rejection. `topics/self-stultification-as-master-argument` L149 says "Epiphenomenalism might be correct despite being impossible to rationally believe". That matches `tenets.md` L101, which holds that the self-stultification argument does not refute epiphenomenalism, so it is not a concession; its next sentence over-claims the other way (Note 10).

Pattern 4 found no many-worlds endorsement. The four unhedged hits are definitions: `tenets.md` L115, `topics/indexical-identity-quantum-measurement` L97, `concepts/indexical-knowledge-and-identity` L142, and `topics/the-reverse-inference` L92 "are excluded". No page uses parsimony as a decisive argument against dualism. The reverse direction, parsimony used for the Map, has one live case (C6) and one queued case (see Still present).

## Warnings

### A. Tenet 5 scope: the tenet said or implied to bind only the Map (pattern 1)

`tenets.md` L145: "This tenet binds the Map's use of parsimony, not only its critics'." L147: the tenet rules out "Using parsimony as a decisive argument against dualism" and also any Map argument that leans on parsimony. L69: "Tenet 5's symmetric self-binding therefore applies to parsimony arguments *for or against* the framework". A page may say the tenet has nothing to answer in a case where the rival's argument makes no appeal to simplicity, but it must give that reason. It may not say the tenet's scope stops at the Map. The fix pattern is the one d0d296c2 used: "The tenet limits appeals to simplicity on either side; [the rival] rests on none here."

All eight are older text. Two of the pages (A1, A8) were edited in the window, at other lines. Six of the eight were listed as passing the misread standard by the 2026-10-23, 10-24, 10-26 or 10-29 tenet checks (Note 1).

#### A1. `topics/trilemma-of-selection.md` L117 (explicit "only")
- **Quote**: "Tenet 5 binds only the Map's reasoning: it bars both preferring Horn 3 for its richness and dismissing Planck as deflationary."
- **Issue**: The colon clause is symmetric and correct; the label before it is the misreading. The sentence entered on 2026-10-30 (923cc4406f, the Planck–MacKay fold), four days after the 10-26 check had flagged this page's Occam paragraph (then L133) as "Tenet 5 turned outward" under the misread standard. The window's 379229627a edited L72, L78, L97 and L144 on this page and did not reach L117.
- **Fix**: "binds only the Map's reasoning" → "discounts simplicity on either side". Net 0. Headroom 426 (3573 of 4000).

#### A2. `concepts/access-consciousness.md` L133 (explicit "only")
- **Quote**: "The tenet governs only the Map's own reasoning: it lets the Map doubt that economy settles the question, and gives no licence to discount the physicalist account of access for being simple."
- **Issue**: Same shape as A1. The colon clause even applies the tenet to the physicalist's economy, which contradicts the label. The 10-24 check listed "access-consciousness RSP" as passing.
- **Fix**: "governs only the Map's own reasoning" → "discounts economy on either side". Net −1. Headroom 922.

#### A3. `topics/visual-indexes-and-demonstrative-reference.md` L111 (explicit "only")
- **Quote**: "The tenet governs only the Map's own reasoning: it lets the Map doubt that simplicity settles the personal-level question, and gives no licence to discount a well-evidenced sub-personal capacity for being simple."
- **Issue**: A2's sentence nearly word for word. The 10-23 check listed it as passing.
- **Fix**: "governs only the Map's own reasoning" → "discounts simplicity on either side". Net −1. Headroom 1018.

#### A4. `topics/blocks-harder-problem.md` L135 (explicit "not Block's")
- **Quote**: "The tenet binds the Map's own reasoning, not Block's or McLaughlin's."
- **Issue**: The next sentence gives the real reason: "Block's own objections to them are explanatory, not appeals to simplicity". So the conclusion holds for this case, but the stated scope is wrong. Its research note, `blocks-harder-problem-2026-10-24`, is one of the twelve known notes. The 10-24 check listed L135 as passing.
- **Fix**: → "Here the appeals to simplicity at issue would be the Map's own." (the chain-of-thought form). +1. Headroom 1229.

#### A5. `topics/reactive-attitudes-and-strawsonian-responsibility.md` L85 (implied)
- **Quote**: "That constrains the Map's own reasoning and brings no charge against the Strawsonian."
- **Issue**: The sentence before it says the tenet "bears only on a further inference, from "the practices need no metaphysical foundation" to "there is none", which it lets the Map decline to treat as decisive". Declining someone's simplicity-driven inference *is* the tenet binding that party, so "constrains the Map's own reasoning" misdescribes what was just done. This is the shape d0d296c2 fixed on four pages ("constrains only the Map's own reasoning, so it brings no charge against …"), minus the "only". The 10-26 check listed L85 as passing.
- **Fix**: → "The tenet limits that inference whoever draws it, and brings no charge against the dissolution's two limbs." +4. Headroom 1030.

#### A6. `concepts/the-ownerless-suffering-argument.md` L127 (implied)
- **Quote**: "binds the Map's own reasoning here and supplies no charge against its opponents."
- **Issue**: The next sentence applies the tenet to the opponents' advantage: "The ownerless reading is the more parsimonious one … and the Map declines to count that parsimony against itself". That is the tenet discounting a rival's parsimony, the first clause of its Rules-out. The 10-24 check listed L127 as passing.
- **Fix**: → "cuts both ways here: it denies the opponents' parsimony decisive force and supplies the Map no charge against them." +6. Headroom 181.

#### A7. `voids/molyneux-void.md` L93 (implied)
- **Quote**: "The caution binds the Map's own reasoning and is no charge against Berkeley or Leibniz."
- **Issue**: The same paragraph says "Both historical camps claimed economy" and that "Neither economy picked out a question an experiment could answer". Two parsimony appeals that settled nothing are exactly what the tenet discounts. The clause exempts them.
- **Fix**: → "The caution applies to both camps' economies and binds the Map's own reasoning as much." Net 0. Headroom 231.

#### A8. `concepts/psychophysical-indexing-law.md` L116 (implied)
- **Quotes**: "the lesson is for the Map's own reasoning." and "The tenet constrains how the Map reasons and says nothing against the physicalist exclusion rule, which remains the only worked answer."
- **Issue**: The page gives no reason why the tenet "says nothing" against IIT's exclusion postulate (L51, L89), and the construction implies the scope limit. Its research note, `psychophysical-indexing-law-2026-10-28`, is one of the twelve known notes. The 10-29 check listed it (then L114) as passing. Lead to check, unverified: IIT 3.0 (Oizumi, Albantakis & Tononi 2014) is sometimes read as motivating exclusion by Occam's razor. Verify that at source before relying on it. If true, the tenet does bear on that justification.
- **Fix**: "the lesson is for the Map's own reasoning" → "the lesson here falls on the Map's own reasoning" (+1). The second sentence → "The tenet discounts simplicity on either side, so it neither credits nor faults the physicalist exclusion rule for its economy; that rule remains the only worked answer." (+6). Keep the verdict that the rule is the only worked answer. Headroom 262.

### B. A void read as support for a tenet (pattern 2, P-V3)

`positions/voids-as-evidence` P-V3 suspends the cumulative step, and `apex/taxonomy-of-voids` L231 says void convergence "lends dualism no evidential weight while P-V3's cumulative step stays suspended". Of the 125 voids, these four state support or a dualism-only prediction without naming the rival that predicts the same thing. None of the four links P-V3.

#### B1. `voids/acquaintance-void.md` L157 (window page; older text)
- **Tenet**: Bidirectional Interaction.
- **Quote**: "The void would be merely academic if acquaintance were epiphenomenal; that it shapes behaviour suggests a genuine causal relation, making its limits genuine constraints on what minds can do."
- **Issue**: "that it shapes behaviour" assumes what is in dispute. A physicalist on whom acquaintance is a neural state predicts the same reports, and the epiphenomenalist explains the tracking by correlation (`tenets.md` L101). The page's own Dualism paragraph, L153, carries P-V3, so the Bidirectional paragraph is out of step with its sibling. Raised by the 10-20, 10-21 and 11-16 checks; not queued.
- **Rung earned**: compatible.
- **Fix**: → "The void would be merely academic if acquaintance were epiphenomenal. That reports track acquaintance fits the tenet without evidencing it: a physicalist who identifies acquaintance with a neural state predicts the same tracking." +4 (the clause "making its limits genuine constraints on what minds can do" goes with the old reading). Headroom 529.

#### B2. `voids/capability-division-problem.md` L120 (window page; older text; was 2026-11-25 Note 4)
- **Tenet**: Dualism.
- **Quotes**: "The Map interprets the capability division problem as evidence that dualism requires a different kind of explanatory framework than physicalism provides." and "Physicalism explains vision entirely in neural terms and treats consciousness as something to be explained away."
- **Issue**: The void is read as evidence. The second sentence describes eliminativism, not non-eliminative physicalism. The section has no P-V3 or P-V2 line, which the 10-24 check (W11) asked for. Raised on 10-24 and 11-25; not queued.
- **Rung earned**: compatible.
- **Fix**: **Headroom 0** (2999 of 3000), so the net change must be ≤ 0. Replace both sentences (36 words) with: "The Map reads the problem as calling for an explanatory framework physicalism lacks; the void lends that reading no evidential weight ([[positions/voids-as-evidence#^p-v3|P-V3]]), and physicalism, which explains vision in neural terms, need not explain consciousness away." (35 words for 37, −2). Re-measure after the edit: the wikilink may count differently.

#### B3. `voids/imagery-void.md` L133 (corpus sweep; last edited 2026-11-20)
- **Tenet**: Dualism.
- **Quote**: "The Map reads this as evidence that phenomenology has independent structure from the functional roles it accompanies—which is what [[tenets#^dualism|Dualism]] predicts."
- **Issue**: The paragraph concedes that "the function may differ in fine-grained ways the experiments miss". A physicalist who places the difference in strategy or fine-grained function predicts the same aphantasia dissociation, so "evidence … which is what Dualism predicts" claims a discriminator the paragraph does not have. Raised on 11-18; not queued.
- **Rung earned**: compatible.
- **Fix**: → "The Map reads this as phenomenology having structure independent of its functional roles, as [[tenets#^dualism|Dualism]] allows; a physicalist who finds the difference in fine-grained function predicts the same, so the void adds no weight ([[positions/voids-as-evidence#^p-v3|P-V3]])." +14. **Headroom 24** (2975 of 3000).

#### B4. `voids/perceptual-reality-monitoring-void.md` L110 and L112 (corpus sweep; last edited 2026-10-30)
- **Tenets**: Bidirectional Interaction (L110) and Dualism (L112).
- **Quotes**: "Whatever the metaphysics, the empirical purchase of reality-monitoring strengthens the broader claim that interface-sites are systematically opaque to the consciousness they constitute." and "The discriminator's structural opacity is the kind of result the Map expects on **dualism**:"
- **Issue**: On any account a sub-personal discriminator is opaque to the person whose experience it shapes. "Whatever the metaphysics" concedes the result is framework-neutral, and yet the sentence says it "strengthens" a Map claim. Raised on 10-24 and 11-18; not queued.
- **Rung earned**: compatible.
- **Fix**: L110: "strengthens" → "fits", and add "; a sub-personal discriminator is opaque on physicalism too, so the fit adds no weight ([[positions/voids-as-evidence#^p-v3|P-V3]])" (+15). L112: "is the kind of result the Map expects on **dualism**:" → "fits **dualism** without favouring it:" (−6). Net +9. Headroom 375.

### C. Over-reach and posits stated as results on window pages

#### C1. `concepts/epistemology-of-limit-knowledge.md` L129 (window page; older text)
- **Tenet**: Dualism (over-reach; P-V3 at concept level).
- **Quote**: "The convergence of failure signatures around the consciousness-physics interface is limit-knowledge that supports dualism abductively—if consciousness were reducible to physics, the structured, categorical nature of the failure would be unexpected. This support is genuine but bounded,"
- **Issue**: `apex/taxonomy-of-voids` L231 grades the same convergence as "framework-internal coherence" that "lends dualism no evidential weight". The paragraph names the rival itself, cognitive closure, which expects structured failure, but only to bound the "support", not to withdraw it. Open task todo L3779 covers this page's "demonstrates" sentence, not this one. Raised on 11-18.
- **Rung earned**: compatible.
- **Fix**: replace from "The convergence of failure signatures" through "and the bound matters:" with "The convergence of failure signatures around the consciousness-physics interface is limit-knowledge the Map reads as fitting dualism. The fit is framework-internal coherence, not abductive support ([[positions/voids-as-evidence#^p-v3|P-V3]]): a naturalist who accepts [[mysterianism|cognitive closure]] also expects structured, categorical failure. Even read as fit, the bound matters:" (44 words for 40, +4). Headroom 1260. Keep the paragraph's remainder ("cognitive closure is double-edged …") as it is. Best run in the same pass as todo L3779.

#### C2. `concepts/mental-imagery.md` L159 and L145 (window page; older text; L145 is 2026-11-25 W7)
- **Tenet**: Bidirectional Interaction (over-reach).
- **Quotes**: "Mental imagery supports [[bidirectional-interaction]] through multiple channels:" (L159, the tenet-section opener) and "The evidence provides confirmatory support for the Map's position rather than knockdown proof." (L145)
- **Issue**: L161 says "That reading is the conclusion under dispute, not a datum" and "The Map acknowledges that identity theory also predicts this". L163 says "consistent with". The opener and L145 claim more than the paragraphs they introduce. L159 was raised on 11-02. Neither is queued.
- **Rung earned**: compatible against physicalism; suggestive against epiphenomenalism only.
- **Fix**: L159: "supports" → "bears on" (+1). L145: "provides confirmatory support for" → "is consistent with" (−1). Net 0. Headroom 72.

#### C3. `apex/identity-across-transformations.md` L193 (window page; older text)
- **Tenet**: Bidirectional Interaction (a posit stated as a result; `tenets#^tenet-3-standing`).
- **Quote**: "Your consciousness has made choices that shaped physical outcomes. These choices constitute *your* history in a way that psychological patterns cannot capture."
- **Issue**: The tenets page says articles asserting such causal work "should read no more confidently than this paragraph does". Raised on 10-12, 11-05 and 11-15. Open task todo L5593 covers L173, L175 and L189 on this page, not L193; add L193 to it.
- **Rung earned**: the Map's posit.
- **Fix**: → "On the Map's posit, your consciousness has made choices that shaped physical outcomes, at the tenet's registered standing." (+9 over the first sentence). Headroom 431.

#### C4. `concepts/nihilism-and-existentialism.md` L122 and L114 (out of step with L48, re-graded 2026-11-26)
- **Tenets**: Bidirectional Interaction (L122, a posit stated as a result) and Dualism (L114, the co-optation firewall's verdict-direction leg).
- **Quotes**: L122: "The [[tenets#^bidirectional-interaction|Bidirectional Interaction tenet]] provides the mechanism: consciousness biases which neural patterns actualise.", "[[concepts/epiphenomenalism|Epiphenomenalism]] cannot explain why talk of phenomenal states tracks phenomenal states if those states are causally inert." and "The Map provides what existentialism needs: genuine causal efficacy of mind." L114: "Heidegger makes the same point differently".
- **Issue**: d44b952eb9 re-graded the lead, the description and three body lines. L48 now says "Neither Sartre nor Heidegger argued for dualism, and Heidegger rejected the Cartesian subject". The tenet section was not touched. L122 states the mechanism and its efficacy as delivered. `tenets.md` L101 calls the tracking argument "the deepest difficulty for epiphenomenalism rather than its refutation". L114 then enlists Heidegger for "the Map's core claim" two headings below L48's disclaimer.
- **Rung earned**: the Map's posit (L122); a parallel, not an ally (L114).
- **Fix**: L122 → "The [[tenets#^bidirectional-interaction|Bidirectional Interaction tenet]] proposes a mechanism, consciousness biasing which neural patterns actualise, held at [[tenets#^tenet-3-standing|the tenet's registered standing]]. Epiphenomenalism meets its [[tenets#^tenet-3-epiphenomenalism|deepest difficulty]] here: why talk of phenomenal states tracks those states if they are causally inert. On its posit, the Map offers what existentialism assumes: causal efficacy of mind." (51 words for 41, +10). L114: "Heidegger makes the same point differently" → "Heidegger, who rejected the Cartesian subject, makes a related point" (+4). Headroom 910.

#### C5. `concepts/attention-as-interface.md` L236 (window page; older text)
- **Tenets**: Occam's Razor Has Limits and Bidirectional Interaction (over-reach).
- **Quote**: "The interface hypothesis adds complexity but explains what simpler theories cannot: why attention feels effortful and why effortful attention produces neuroplastic results."
- **Issue**: Four lines up, L232 grades the neuroplasticity evidence: "Schwartz's OCD neuroplasticity is suggestive rather than grounding". Here it is treated as an explanandum that only the interface explains. Practice-driven plasticity is explained on every view. Raised on 09-23.
- **Rung earned**: compatible.
- **Fix**: "explains what simpler theories cannot: why attention feels effortful and why effortful attention produces neuroplastic results" → "offers a reading of why attention feels effortful" (−8). **Headroom 21** (3478 of 3500).

#### C6. `topics/the-strong-emergence-of-consciousness.md` L167 and L194 (window page; older text; pattern 4)
- **Tenet**: Occam's Razor Has Limits (parsimony argued *for* the framework; `tenets.md` L147 and L69).
- **Quotes**: "the parsimony advantage tilts back toward strong emergence with mechanism." (L167) and "Why the parsimony advantage may favour strong emergence with mechanism over physicalism" (L194, Further Reading gloss).
- **Issue**: The target page, `topics/parsimony-case-for-interactionist-dualism`, reads its own case "not as positive evidence for dualism but as an internal critique" (L140). This page cashes it as a parsimony tilt toward the Map's view, which the tenet's self-binding forbids. Raised on 11-03; not queued.
- **Rung earned**: defeater-removal (parsimony neutralised, not reversed).
- **Fix**: L167 "tilts back toward strong emergence with mechanism" → "no longer favours physicalism" (−3). L194 gloss → "Why physicalism's parsimony advantage is thinner than it looks" (−3). **Headroom 30** (3969 of 4000).

## Notes

1. **Upstream seeds of the Tenet 5 misreading** (driver action; no content edit).
   - **(a) Open task Notes.** Six open tasks prescribe "Tenet 5 constrains only the Map's own reasoning" as a standing calibration rule. They are at todo L1789 (`concepts/phenomenology-of-choice-and-volition`), L1800 and L1810 (both `apex/consciousness-and-agency`), L1841 (`topics/phenomenology-of-returning-attention`, which also tells the fork to rephrase a correct outward use), L2066 (`topics/philosophy-of-language-under-dualism`) and L4652 (`concepts/standing-agnostic-challenge`). Each will hand the misreading to a fork. Per memory, fork args carry Notes verbatim. Correct them in place before any of the six is picked, e.g. "Tenet 5 discounts parsimony on either side (tenets.md L145)".
   - **(b) Review files.** Twenty-four review files carry the phrase. The four that matter are the 2026-10-23, 10-24, 10-26 and 10-29 tenet checks. Their calibration tables take their families from the driver's brief ("Family (brief)"), so the misreading entered through the briefs. Each table carries a row "Tenet 5 binds only the Map's reasoning" and lists "Compliant instances found (controls)" under it, among them A2, A3, A4, A5, A6 and A8. Future tenet-check briefs should state the family as "Tenet 5 discounts parsimony on either side".
   - **(c) The NEEDS-HUMAN at todo L121.** The 10-29 W7 ("Tenet 5 turned outward", nineteen loci) treated outward uses of the tenet as defects under that standard. Its loci were recorded against this NEEDS-HUMAN (doctrine, the "parsimony tiebreaker" rule), which should be re-read in light of L145 and L147. Turning the tenet against a critic's parsimony argument is the first clause of the Rules-out. Only parsimony treated as decisive, in either direction, is out of contract.
   - **(d) Research notes.** The twelve research notes (14 hits of "constrains only") are the known set owned by todo L7840. The sweep found no others. Two of them seeded live defects listed here: `blocks-harder-problem-2026-10-24` (A4) and `psychophysical-indexing-law-2026-10-28` (A8).
2. **Tenet 5, borderline wording** (no "only"; the content that follows is symmetric): `concepts/discrimination-problem` L124 "governs the Map's own reasoning here." (the next sentence applies the tenet to the rival's simplicity); `topics/measuring-the-witness-attitude` L110 "The tenet constrains the Map's own reasoning."; `topics/immediate-emotions-and-the-affect-heuristic` L111 "The tenet governs the Map's own reasoning, not what the studies show." Reword when the pages are next touched. `concepts/self-blindness` L124, `concepts/modal-epistemology` L125 and `voids/boredom-void` L96 are at grade: each gives the reason, or the case really is the Map's own appeal.
3. `concepts/mysterianism` L186: "Mysterianism provides indirect support." for No Many Worlds, two sentences before "it supplies no reason to think many-worlds false." This contradicts itself on the same page as the carried W9 at L64. "provides indirect support" → "is compatible with the tenet" can go with W9.
4. **Weaker void claims** that are conditional or graded nearby:
   - `voids/mood-void` L127: "the Map's opacity there is what the tenet predicts, not what it would need to explain away." This follows "If mind influences physical cognition somewhere", but names no rival.
   - `voids/causal-interface` L148: "This is coherent: one would expect an interface between consciousness and physics to be at the edge of what either mode of access can reveal." The window edited a later clause of this line and left this sentence. L150, also edited, grades the outside half correctly.
   - `voids/voids` L335 (section index; one window line elsewhere): "The hard problem persists not as a puzzle awaiting solution but as a signpost marking where materialist explanation ends." This is flat, and the index's tenet section has no P-V3 line.
5. `concepts/quantum-biology-and-neural-mechanisms` L164: "they remove the objection that warm brains cannot support quantum consciousness". `tenets.md` L79 claims only that warm environments "do not categorically rule out quantum-functional mechanisms". `concepts/quantum-consciousness` L190, "transforming … mental causation from philosophical puzzle into precise proposal", sits uneasily with P-Q10 (no worked toy model).
6. `topics/pain-consciousness-and-causal-power` L172: "When the felt awfulness is present, it drives protective behaviour;" is flat, and the grade ("compatible with phenomenal causation rather than evidence for it") arrives one clause later. "it drives" → "it accompanies" would match.
7. `voids/transit-void` L196: "the epiphenomenalist reading of Libet was the simpler story, and Schurger reveals its simplicity as illusory." Schurger's model is itself a physicalist noise account; it undercuts the readiness-potential inference, not epiphenomenalism's simplicity.
8. `topics/philosophy-of-action-under-dualism` L101: "The posit must still earn its keep—and here it does, by answering the disappearing agent directly". Its sibling `topics/event-causal-libertarianism` L86 calls the same move "a framework-relative judgement rather than a demonstration". The window's change to this page was the Ryle fold and references, not this line.
9. `topics/ethics-of-consciousness-invertebrate-question` L115 ("permanently underdetermined at the empirical level") is unchanged since the 2026-11-25 Note 9. The window edited L119 on this page, and L119 reads at grade.
10. `topics/self-stultification-as-master-argument` L149 (pattern 3, the reverse direction): after the correct concession, "A position that cannot be rationally held … drops out of rational discourse entirely." `tenets.md` L103 says the strongest version of epiphenomenalism, the phenomenal-concept strategy, survives the objection, so it has not dropped out. Raised only in two spring optimistic reviews.
11. `topics/the-convergence-argument-for-dualism` L177 (pattern 4): "When multiple substantially independent lines of evidence favor dualism, physicalism's parsimony advantage is outweighed by its explanatory disadvantage." The sentence is conditional and treats parsimony as a tiebreaker, which is within contract. Its "substantially independent" sits against P-M2's shared-source discount. Raised on 07-29b and 07-30.
12. `apex/embodied-interface` L125 ("an experience can be genuinely phenomenal, genuinely owned, and causally idle") was the pattern 3 positive control. It follows the dispositional reading of Tenet 3, the open NEEDS-HUMAN quantifier decision, and is not a defect.
13. Co-optation roster: no enlistment in the 81 tenet sections read. McGinn is cited for an epistemic caveat (`concepts/quantum-biology-and-neural-mechanisms` L174, `concepts/quantum-consciousness` L192) or on his own page. Metzinger (`concepts/mine-ness` L136, `concepts/self-and-self-consciousness` L194), Dennett (`voids/narrative-void` L107), Friston (`concepts/mine-ness` L148) and Nagel (`voids/interested-party-void` L100) are each named as a rival or with their stance stated. Damasio is stated as "a neurobiological naturalist" (`voids/narrative-void` L111). The one firewall issue is Heidegger at `concepts/nihilism-and-existentialism` L114, folded into C4.

**P-V3 survey, all 125 voids.**
- **Claim support:** four (B1–B4).
- **Weaker unlinked readings:** three (Note 4: `mood-void`, `causal-interface`, the `voids` index).
- **No unnegated support claim in any sweep:** the other 118. I read every hit but did not read the whole tenet section of the 99 voids outside the window, so for those this is a lexical clearance, not a full read.
- **The 26 window voids, read in full:**
  - 22 state P-V3 or P-V2, or grade each paragraph as a reading, fit or illustration.
  - `causal-interface` grades its Minimal Quantum Interaction paragraph (L150) but keeps the unlinked "one would expect" at L148 (Note 4).
  - `interface-formalization-void` runs the dependency from tenets to void (the tenets "posit an interface that mathematics can surround but not penetrate") and claims no support back.
  - `acquaintance-void` (B1) carries P-V3 in its Dualism paragraph only.
  - `capability-division-problem` (B2) has no disclaimer.
- **New since 2026-11-25:** `valence-void` and `compound-failure-signatures` now carry P-V3.

## Change since the 2026-11-25 report

**Repaired in the window** (tenet-section sentences replaced; each reads at grade):

| Page | Locus | Change |
|---|---|---|
| `voids/valence-void` | L115–L119 | "finds particularly strong support" → P-V3; asymbolia "compatible with the data rather than supported by them" |
| `voids/compound-failure-signatures` | L141–L147 | "gains support from two directions" → "a thematic link only", P-V3 |
| four Tenet 5 pages | rollback L110, basic-argument L135, transparency L105, chain-of-thought L120 | "constrains only the Map's own reasoning" → the symmetric reason (d0d296c2) |
| `concepts/metacognition` | L180–L188 | Tenet 3 "causally indispensable" → "fits the tenet without evidencing it"; Tenet 4 posit marked |
| `concepts/mine-ness` | L136–L148 | "suggestive" against MWI → "equally expected on Many-Worlds … no evidence against MWI" |
| `topics/consciousness-and-the-ownership-problem` | L132, L138 | ownership graded "*compatible* tier, no higher" |
| `topics/first-quantum-free-will-wave-1927-1940` | L89 | Tenet 5 no longer deployed against Schlick |
| `topics/trilemma-of-selection` | L76, L95 (body) | Horn 3 out of the result register |
| `voids/interested-party-void` | L100–L106 | rival named (active inference, P-RR2); progress claim "fits … without supporting it" |
| `voids/tenet-generated-voids` | L141–L151 | "one signature, though, not five"; plurality void "adds nothing to the tenet" |
| `concepts/nihilism-and-existentialism` | L48 (lead) | "strengthens the Dualism tenet" withdrawn (tenet section left: C4) |
| `concepts/generalised-probabilistic-theories` | L96–L102 | "does no work *for* the interface reading over its rivals" |
| twelve more voids | tenet sections | aspect-perception, attention-and-consciousness, causal-interface (L150), commensurability, death, erasure, ineffable-encounter, interface-formalization, meaning, narrative, necessary-opacity, self-transcendence |

**The 2026-11-25 Warnings: all ten still live** (each OLD string at count 1). The Priority List and W5 were minted:

- W1 `concepts/valence` L91 → todo L6795.
- W2 `concepts/reductionism` L109 → todo L6804.
- W3 `topics/emotion-and-dualism` L145, with the L137 clause → todo L6773.
- W4 `apex/interface-specification-programme` L173 and L177 → todo L6231.
- W5 `topics/ai-consciousness` L153 → todo L6813.

W6 (`consciousness-selecting-neural-patterns` L162), W8 (`predictive-processing` L182), W9 (`mysterianism` L64) and W10 (`wheelers-participatory-universe-and-it-from-bit` L148) are not queued. W7 (`mental-imagery` L145) is folded into C2 above.

**Still present, already queued** (not counted again):

- `topics/dual-domain-capabilities-in-proprioception-and-spatial-imagination` L103 "is supported by the persistent explanatory gap" (todo L3427 and siblings).
- `concepts/motor-selection` L198 "The attention-motor unification supports the" Dualism tenet.
- `apex/embodied-interface` L79 "Asymbolia is the demonstration:".
- `concepts/geometric-model-of-mind` L112, "the Map because parsimony favours the smallest non-physical influence consistent with the tenets" (todo L4770, "Four more pages ground Tenet 2's minimality in parsimony"). This line also says the Map rejects Penrose–Hameroff, while `tenets.md` L71 keeps Orch OR as "live fallbacks". Add that to L4770's brief.
- `concepts/mental-causation-and-downward-causation` L198 "we lose epistemic access to our own minds" and L202 "Required for mental causation to be possible" (todo L3226).
- `topics/consciousness-and-cognitive-distinctiveness` L188 "Many-worlds eliminates this distinction" (todo L3820, the MWI/agency sweep).

**Still present, not queued:** `topics/forward-in-time-conscious-selection` L177, "is what an interface doing causal work at a primitive seam predicts" (raised 10-05, 11-02, 11-25).

## Priority List (at most four)

Rules for all four:
- Re-grep each OLD string (`str.count == 1` at this run) and read its whole paragraph before editing.
- Do not weaken a commitment the Map holds, and never concede epiphenomenalism.
- The Tenet 5 standard is `tenets.md` L145: the tenet discounts parsimony on either side. Do not copy any task note that says it "constrains only the Map's own reasoning".
- No "This is not X. It is Y."; no "load-bearing". New wikilinks must be piped.
- Do a pronoun and next-sentence check after each replacement.

Word counts are from `tools.curate.length.analyze_length` at this run. Gates fire at `>=`, and headroom is hard − 1 − count.

### 1. Tenet 5 scope, eight live pages (A1–A8)
One sweep of the same class as today's d0d296c2 P2. Use the drafts in A1–A8; each is a phrase swap of −1 to +7 words. Headroom ranges from 181 (ownerless-suffering) to 1229. For A8, verify the IIT-exclusion lead at source or leave the reason general. Afterwards these two greps should both return 0 on `obsidian/{topics,concepts,voids,apex,positions}`:
- `grep -rnE "governs only the Map|binds only the Map|constrains only the Map"`
- `grep -rnF "not Block's or McLaughlin's"`

**Before minting**, correct the six open task Notes in Note 1(a), so a fork running one of them does not reinstall the misreading this item removes.

### 2. Four voids read as tenet support (B1–B4)
`acquaintance-void` L157 (+4, headroom 529), `capability-division-problem` L120 (−2, **headroom 0**), `imagery-void` L133 (+14, **headroom 24**), `perceptual-reality-monitoring-void` L110 and L112 (+9 net, headroom 375). Model sentence: `voids/commensurability-void` L97, "dualism makes room for the void, while the void, being conjectural, returns no evidential support to dualism or to any other tenet". Measure the two tight files before and after; if the wikilink pushes `capability-division-problem` to 3000, drop the pipe text and keep the bare P-V3 anchor.

### 3. `concepts/epistemology-of-limit-knowledge` L129 (C1)
2239 words of 3500 (headroom 1260). Run it with open todo L3779 on the same page, which owns the "demonstrates … independently motivated entries" sentence. The replacement in C1 is +4. Keep the paragraph's closure caveats.

### 4. `concepts/nihilism-and-existentialism` L122 and L114 (C4)
2589 words of 3500 (headroom 910). Bring the tenet section into line with L48 (re-graded 2026-11-26). L122 +10 and L114 +4, as drafted in C4. Check that the "### Bidirectional Interaction" heading still matches its paragraph, and that L130 (No Many Worlds), which is already at grade, is not touched.

Left off the list: C2 (`mental-imagery` L159 and L145, two verb swaps, net 0 against headroom 72), C3 (`identity-across-transformations` L193, best added to todo L5593), C5 (`attention-as-interface` L236, −8 against headroom 21) and C6 (`the-strong-emergence-of-consciousness` L167 and L194, −6 against headroom 30). C6 is the strongest fifth candidate: it is the corpus's one live parsimony-for-the-Map argument, and its fix shortens the page.

## Files Passing All Checks

No Warning on 73 of the 83 window pages. Marks: † a Note here; ‡ a carried sentence, queued or not.

- **Apex:** apex-articles, conjunction-coalesce, moral-status-of-edge-cases, self-concealing-interface, taxonomy-of-voids, what-it-might-be-like-to-be-an-ai.
- **Concepts:** basic-argument-and-constitutive-luck, brain-interface-boundary, emergence, four-category-ontology, generalised-probabilistic-theories, mental-causation-and-downward-causation ‡, metacognition, mine-ness, motor-selection ‡, mysterianism †‡, pain-asymbolia, phenomenology-of-choice-and-volition, quantum-biology-and-neural-mechanisms †, quantum-consciousness †, quantum-indeterminacy-free-will, quantum-probability-consciousness, retrocausality, rollback-argument-against-agent-causation, self-and-self-consciousness, transparency-method-of-self-knowledge, valence ‡.
- **Positions:** quantum-interface, subject-census, subject-census-calibration-history, thought-and-understanding. All changes are dated calibration notes; P-TU1's new note grades a reported zero on the compatible / suggestive / discriminating ladder, and no band moved.
- **Tenets:** tenets. The window's one change re-labels Stapp-Zeno's pre-decoherence status as disputed.
- **Topics:** animal-consciousness, biological-teleology-and-the-interface-framework, chain-of-thought-as-verbal-protocol, consciousness-and-cognitive-distinctiveness ‡, consciousness-and-the-ownership-problem, dual-domain-capabilities-in-proprioception-and-spatial-imagination ‡, emotion-and-dualism ‡, ethics-of-consciousness-invertebrate-question †, event-causal-libertarianism, first-quantum-free-will-wave-1927-1940, pain-consciousness-and-causal-power †, phenomenology-of-cognitive-limit-types, philosophy-of-action-under-dualism †, responsibility-gradient-from-attentional-capacity, the-epiphenomenalist-threat, valence-as-a-natural-kind.
- **Voids:** agency-void, apophatic-cartography, aspect-perception-void, attention-and-consciousness, causal-interface †, commensurability-void, compound-failure-signatures, death-void, erasure-void, ineffable-encounter-void, interested-party-void, interface-formalization-void, language-thought-boundary, meaning-void, narrative-void, necessary-opacity, self-maintained-cognitive-limits, self-transcendence-void, stereopsis-void, tenet-generated-voids, thrownness-void, transit-void †, valence-void, void-as-ground-of-meaning, voids †.

Window pages with a Warning: `voids/acquaintance-void`, `voids/capability-division-problem`, `concepts/epistemology-of-limit-knowledge`, `concepts/mental-imagery`, `apex/identity-across-transformations`, `concepts/nihilism-and-existentialism`, `concepts/attention-as-interface`, `topics/the-strong-emergence-of-consciousness`, `topics/trilemma-of-selection`, `concepts/psychophysical-indexing-law`. Pages with a Warning found by the corpus sweeps only: `concepts/access-consciousness`, `topics/visual-indexes-and-demonstrative-reference`, `topics/blocks-harder-problem`, `topics/reactive-attitudes-and-strawsonian-responsibility`, `concepts/the-ownerless-suffering-argument`, `voids/molyneux-void`, `voids/imagery-void`, `voids/perceptual-reality-monitoring-void`.

Models of the grade worth copying:
- `concepts/basic-argument-and-constitutive-luck` L135: "The tenet limits appeals to simplicity on both sides, and the compatibilist and event-causal replies rest on none, so it brings no charge against those rivals either."
- `topics/phenomenology-of-memory-and-the-self` L156: "with knowledge this incomplete, parsimony decides nothing in either direction."
- `concepts/mine-ness` L144: the felt singularity of mine-ness "is equally expected on Many-Worlds, whose branch observers never experience one another, so it is compatible with the tenet but no evidence against MWI."
- `voids/stereopsis-void` L85: "Dualist and physicalist predict the same report, and under the Map's calibration rule ([[positions/voids-as-evidence#^p-v2|P-V2]]) nothing flows back to the tenet."

## Not Done

- The sweeps are lexical. A Tenet 5 or P-V3 misstatement in vocabulary outside the listed variants would not be caught. I read every hit in sentence context but did not read whole tenet sections outside the window's 81 pages.
- For pattern 3, hedged hits (259) were read only where the sentence named the Map, "we" or "our" and carried concession vocabulary (21). The other hedged hits were classed by their marker, not read one by one.
- On the 26 window pages whose tenet sections were not edited in the window, any carried sentence older than the 2026-11-25 report is listed only if it is new to this report or still unqueued.
- The A8 lead (IIT 3.0's exclusion postulate and Occam's razor) is unverified.
- No article, position, research note or todo entry was edited. No tasks were minted. No commit.
