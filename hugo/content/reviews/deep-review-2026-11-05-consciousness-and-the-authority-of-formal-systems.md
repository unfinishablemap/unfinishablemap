---
ai_contribution: 100
ai_generated_date: 2026-11-05
ai_modified: 2026-11-05 09:49:12+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-05
date: &id001 2026-11-05
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-05 09:49:12+00:00
modified: *id001
related_articles: []
title: Deep Review - Consciousness and the Authority of Formal Systems
topics: []
---

**Date**: 2026-11-05
**Article**: [Consciousness and the Authority of Formal Systems](/topics/consciousness-and-the-authority-of-formal-systems/)
**Previous review**: [2026-07-12](/reviews/deep-review-2026-07-12-consciousness-and-the-authority-of-formal-systems/) (citation walk). The one before it is [2026-07-11](/reviews/deep-review-2026-07-11-consciousness-and-the-authority-of-formal-systems/) (convergence-discount and normative-gap recalibration).

## Why this pass

This is the ninth deep review. It was chosen by the selector (score 74, 115 days since the last review). Two edits landed after 2026-07-12 and neither had been reviewed:

- 2026-09-14 (apex-evolve) added one Further Reading line.
- 2026-10-09 (refine-draft, from optimistic-2026-10-06 item 4) rewrote the Szangolies sentence at L115.

The 10-09 sentence was the main target. This pass verified it against Szangolies' full text, which no earlier pass had done (07-12 checked metadata only). The other lenses were a sibling-fix sweep across the formal-authority wing and the Galilean cluster, and a both-directions orphan check of the References block.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

**1. L115: the 10-09 fence denied Szangolies a claim he makes, and the "rigorous mathematics" label covered his own hedges.**

- **Before**: "On Szangolies' account the same formal mechanism that prevents a system from proving its own consistency also generates quantum theory's epistemic horizons — value indeterminacy, complementarity, the uncertainty relations. That much is rigorous mathematics, not analogy; reading the horizon as a limit on outcome determination is the Map's extension, which Szangolies, a naturalist, does not draw."
- **What the paper says** (arXiv:1805.10668v2 full text, extracted and grepped):
  - Szangolies draws the outcome reading himself. He identifies "the undecidability of certain measurement outcomes due to self-reference" as his common thread.
  - He concludes: "We have shown that, in general, there are always measurement outcomes that cannot be predicted".
  - He ties the horizon to the measurement problem through a "hypercomputational interpretation", with "the randomness taking over whenever knowledge about the system's state reaches the epistemic horizon".
  - What he does not draw is any role for consciousness. The word "conscious" occurs 0 times in the paper.
  - He hedges the quantum side throughout. His abstract investigates self-reference "as a possible origin of such epistemic horizons". He calls what emerges "phenomena closely paralleling the quantum phenomena". He writes: "I do not claim to have achieved a reconstruction of the full quantum formalism. While the above results appear very suggestive, it remains to be seen whether the entirety of quantum phenomena can be derived".
  - "Value indeterminacy" is not his term. His closest is property indefiniteness "mirroring the phenomenon of superposition".
- **Why it is critical**: the 10-09 fence was in the wrong place. It treated a claim Szangolies makes as the Map's extension, and its "That much is rigorous mathematics" covered a quantum fit that he himself calls open. Those are an attribution error and a dropped qualifier.
- **After**: "…underlying Gödelian incompleteness, and proposes it as a possible origin of quantum theory's epistemic horizons: measurement sequences whose outcomes no program can predict from the system's state, complementarity, the uncertainty relations. The fixed-point theorem is rigorous mathematics, not analogy; how much of quantum theory it yields Szangolies leaves open, disclaiming "a reconstruction of the full quantum formalism." Reading consciousness into the horizon is the Map's extension, which Szangolies, a naturalist, does not draw."
- The fence now sits where the self-reference sibling (L76) puts it: on the extension to consciousness. The three-tier structure is preserved, and so is the "naturalist" stance, which was verified (see the ledger). The phrase "prevents a system from proving its own consistency" was dropped. It names the second incompleteness theorem, while the Lawvere unification covers diagonal incompleteness, and L113 already states the first theorem.

**2. L93: the Galilean origin was used to support category error (a method/history calibration error).**

- **Before**: "The Galilean precedent (discussed in the next section) supports category error — consciousness was excluded from mathematical description not by accident but by design."
- **Labels**: Galileo relocating secondary qualities into the perceiver is a *documented textual claim*. The exclusion being "by design" is *contested historiography*. Category error is a *Map reconstruction*.
- **Transition check**: the sentence fails "initial method ⇒ permanent limit". A method built to leave quality out would fail to capture quality whether or not quality is structural, so the design origin cannot pick category error over temporary difficulty. The galilean-exclusion sibling has stated exactly this since its 09-05 cycle: "the method's failure to capture qualities is no evidence *for* their non-physicality, since a method built to leave quality out would fail whether or not quality is physical" (`concepts/galilean-exclusion` L70). Its closing revisability paragraph (L96) adds that "a science's primitives are not fixed by its founding".
- **After**: "The Galilean precedent (discussed in the next section) bears on this only indirectly: a method built to leave quality out would fail whether or not quality is structural, so what favours category error is what structural recapture has since left out."
- The argument now rests on a separate, named premise: the recapture argument at L103, where what was recaptured was "the *structural correlate*, not the phenomenal quality". The Map's preference for category error stands.

**3. L67: the inferentialist-reading qualifier on Carroll's regress was dropped.**

- The source pages present the regress as the canonical entry point only "on the inferentialist reading", and both call that reading contested. `concepts/carrolls-regress` L31 acknowledges "a deflationary reading on which it is no such thing", and L53 says "The inferentialist reading is contested". `voids/inference-void` L49–51 gives both readings.
- The target cited the regress for "executing the rule never amounts to being moved by it" with no qualifier. A computer running modus ponens as a transition rule is the deflationary resolution itself, so the bare citation overstated what the regress shows.
- **After**: "the gap that [Carroll's regress](/concepts/carrolls-regress/), on its contested inferentialist reading, and the [inference void](/voids/inference-void/) treat as canonical…". The apex says the same at L122: "the regress step needs the inferentialist reading to be defensible".

**4. Four orphan References. The 07-12 certification of "no orphans … and vice versa" was false.**

Four entries had no inline attribution: Jackson 1982, Chalmers 1996, Reppert 2003, and Alter & Nagasawa 2015. This was checked by counting each surname in the body prose with the References block excluded. Each count was 0; the one "Alter" hit is the heading "Alternative Frameworks". Each entry supports a passage, so all four were attributed inline rather than deleted:

- Reppert 2003 at the L85 explanatory-idleness argument (the argument from reason).
- Chalmers 1996 at the zombie parenthetical.
- Jackson at the knowledge argument, with a one-clause stance note (see 6 below).
- Alter & Nagasawa 2015 at the naming of Russellian monism.

**5. L89: McDowell's contrast was given in terms that are not his.**

- **Before**: "(later sharpened by McDowell into the contrast between "reasons" and "causes")". The scare-quoted pair presents "reasons" and "causes" as McDowell's terms.
- McDowell's own contrast in *Mind and World* is the "space of reasons" against the "realm of law".
- **After**: "(later developed by McDowell as the contrast between the "space of reasons" and the "realm of law")".
- **Verification is secondary, not primary.** Crispin Wright's 1996 review of *Mind and World* (raw PDF grepped) quotes McDowell verbatim: "concepts whose fundamental point is to place things in the realm of law". It also quotes "the structure of the space of reasons" several times. Wright never uses "reasons and causes" (0 hits). Google Books search-within on both *Mind and World* volume ids (O4m7VtNHjY0C, JQI3AwAAQBAJ) was blocked by a captcha redirect this run, so no page number was taken from the primary text.

### Medium Issues Found (fixed)

**6. Stance note on Jackson.** Naming Jackson for the knowledge argument requires recording his current view. The article now says "(1982; he has since rejected its conclusion)". This was verified in the raw SEP "Qualia: The Knowledge Argument" text: "But Jackson changed his mind. Jackson (1995) argues that knowledge about qualia is impossible if qualia are epiphenomenal and he concludes that something must be wrong with the knowledge argument."

**7. L101: "deciding" became "asserting".**

- **Before**: "— deciding that mathematics would describe nature while qualities excluded from mathematical description would be treated as subjective projections".
- The galilean-exclusion sibling (L66) now rejects the decision framing: "he did not merely *decide* to leave them out of physics either. He asserted … that they are mere names on the side of the object and real only in the sentient body", and the assertion was warranted by "a mathematical programme that had no use for them". The sibling's 09-05 review verified this against SEP (Bolton 2022 §2.2, quoting Finocchiaro's Assayer: the qualities "inhere only in the sensitive body").
- **After**: "— letting mathematics describe nature while asserting that the qualities it had no use for were subjective, residing only in the perceiver." This is an unquoted paraphrase.

**8. L139: an internal tension with L87 was resolved.**

- **Before**: "But a theory that reduces logical compulsion to neural habit cannot itself be logically justified." "Logical compulsion" is the felt bindingness that L87 (since 07-11) concedes is underdetermined between the Map and the physicalist's self-monitoring reply. Read that way, the line re-inflated the defect 07-11 removed.
- **After**: "But a theory that reduces logic's authority to neural habit must rely on that authority to justify itself."
- The target is now logic's *authority*, which is the L89 transcendental (Nagel) point. The 07-11 stability notes say not to soften that point, and it is not softened here: the self-stultification structure is stated directly. The felt-compulsion standoff at L87 is untouched.

### Low Issues (fixed)

- The Further Reading list held `[[phenomenology-of-intellectual-life]]` twice (two piped lines). The shorter duplicate was removed.
- L95's "These are long-standing philosophical challenges, not naive assumptions." was removed. The added Chalmers and Jackson attributions now do its work.
- At L113, "This is not a practical limitation but a structural one — an inherent boundary on what formal methods can accomplish on their own terms." became "The limit is structural, not practical." The "internal limits" frame in the previous sentence already carries "on their own terms".

### Publisher-of-Record Citation Ledger

The References block is unchanged since the full 07-12 publisher walk, so 12 entries carry that verification forward. Szangolies was re-verified fresh because the body claim attached to it changed on 10-09.

- Galilei 1623, *The Assayer*: real-correct (carried forward).
- Russell 1927, *The Analysis of Matter*, Kegan Paul: real-correct (carried forward).
- Gödel 1931, *Monatshefte* 38:173–198: real-correct (carried forward).
- Sellars 1956, EPM, *Minnesota Studies* vol. 1: real-correct (carried forward). The quotation "logical space of reasons" was grep-verified this pass in a raw EPM text (ditext transcription, §36): "we are placing it in the logical space of reasons, of justifying and being able to justify what one says". The 07-12 pass had certified it without a grep.
- Wigner 1960, *Comm. on Pure and Applied Mathematics* 13(1):1–14: real-correct (carried forward; the 07-12 "in"→"on" fix is intact).
- Jackson 1982, "Epiphenomenal Qualia", *Phil. Quarterly* 32(127):127–136: real-correct (carried forward). It is now cited inline, and his later stance is verified at SEP.
- McGinn 1989, *Mind* 98(391):349–366: real-correct (carried forward).
- Chalmers 1996, *The Conscious Mind*, OUP: real-correct (carried forward). Now cited inline.
- Nagel 1997, *The Last Word*, OUP: real-correct (carried forward).
- Reppert 2003, *C.S. Lewis's Dangerous Idea*, IVP: real-correct (carried forward). Now cited inline. The subtitle "In Defense of the Argument from Reason" is omitted, which is acceptable.
- McDowell 1994, *Mind and World*, Harvard UP: real-correct metadata. The body's framing of his terms was wrong and is fixed (see 5).
- Szangolies 2018, "Epistemic Horizons and the Foundations of Quantum Mechanics", *Foundations of Physics* 48:1669–1697: real-correct metadata, re-verified this pass (arXiv abs page citation_doi 10.1007/s10701-018-0221-9; full-text PDF v2). The body claim was real-wrong framing and is fixed (see 1).
- Alter & Nagasawa 2015, *Consciousness in the Physical World*, OUP: real-correct (carried forward). Now cited inline.

**Orphan check, both directions, keyed on (surname, year).**
- Inline years (Russell 1927, Gödel 1931, Nagel 1997, Szangolies 2018, plus the new Reppert 2003, Chalmers 1996, Jackson 1982, Alter & Nagasawa 2015) all resolve to References entries.
- Every References entry is now named in the body.
- Lawvere is named inline without a year and has no References entry. He is cited through Szangolies, so this is low priority and left as is.

**Superlative-currency sweep**: `find_superlative_claims` returned nothing.

**Result-direction leg**: the only empirically cited paper is Szangolies. He reports outcome unpredictability and property indefiniteness as derived results within any theory that allows the maps in his proofs to be instantiated. He leaves open whether these amount to the full quantum formalism. The article now reports this in that direction and at that strength.

**Cited-author-stance leg** (each author's own commitment, and the article does not present any of them as endorsing dualism):
- Szangolies: naturalist. His chapter is "Von Neumann Minds: A Toy Model of Meaning in a Natural World" (2018), and in his own forum comments he describes the model as how intentions arise "in a natural world governed by 'mindless mathematical laws'". The article says "a naturalist".
- Sellars: scientific naturalist.
- McDowell: naturalism of second nature, against "bald naturalism". The article cites both only for the irreducibility of the space of reasons.
- Nagel: anti-reductionist, not a substance dualist. Cited for reason's autonomy.
- Jackson: now a physicalist. Flagged in the text.
- Chalmers: naturalistic property dualist. Cited for zombie conceivability only.
- Russell: led "not to dualism", as the text says.
- McGinn: mysterian naturalist. Cited for closure.
- Reppert: anti-naturalist, endorses the argument from reason. Cited for that argument.

### Map-internal paraphrases re-checked against their source pages

- `phenomenal-authority-and-first-person-evidence` L120 reads "the dispute appears underdetermined by the evidence available from inside either framework". The target's L87 paraphrase is faithful.
- `consciousness-and-mathematics` L70: "every major position on what mathematical objects *are*—Platonism, intuitionism, formalism, structuralism—implies a position on what consciousness *does*". L129 is faithful.
- The `the-quantitative-comprehension-void` heading "## The Abstract Mathematical Ceiling" (L81) exists, so the anchor resolves.
- `carrolls-regress` / `inference-void`: the paraphrase was unfaithful by a dropped qualifier and is fixed (critical 3).

### Brief's sibling-pattern sweep

None of the cluster patterns listed in the brief occurs in this page. The terms checked were Kim, Polanyi, Stapp, Aharonov/TSVF, Lowe, Baddeley, Goyal, Van Dam, emergence, teleology, chance-fixing, and "fits the tenet": 0 body hits each, counted in Python. The applicable sibling repairs came from the galilean-exclusion cycle (items 2 and 7) and the self-reference Szangolies fence (item 1).

### Reasoning-Mode Classification (editor-internal)

- Physicalist evolved-tracking reply (L87): Mode Three, unchanged since 07-11.
- Cultural-constructivism and adaptationism (L89): Mode Two (self-stultification on the opponent's coherence standard), unchanged.
- Occam paragraph (L139): now explicitly the Mode Two transcendental structure. Before this pass it was ambiguous between that and an over-claimed Mode One defeat of the tracking reply.
- Functionalism (L95): Mode Three in substance ("suggests", "indicates"). The arguments are now attributed to their authors.
- Russellian monism (L125): Mode Three (stated reasons for preferring dualism).

A grep for editor-vocabulary leakage in the article prose found nothing.

## Optimistic Analysis Summary

### Strengths Preserved

- The authority/sovereignty distinction and its mapping onto delegatory causation.
- The three-tier (mathematical / interpretive / philosophical) Szangolies structure. It is preserved and is now true to the source at the first tier.
- The 07-11 convergence discount ("one argument shown in two domains") in Relation to Site Perspective, untouched.
- The 07-11 L87 standoff register and the L89 transcendental point. The Occam line now agrees with both.
- The Galilean recapture argument (L103), which now explicitly carries the category-error preference.
- The thermostat and gravitational-mass analogies.

### Enhancements Made

- The bibliography is now attached to the body: four previously unattached sources are cited inline.
- Stance honesty for Jackson.
- Szangolies is reported at his own strength. Birch-persona praise: the pass declines to let a "possible origin" read as a theorem about quantum mechanics. Whitehead-persona caution: nothing was upgraded.

### Cross-links Added

- None. The page is densely linked, and the duplicate Further Reading entry was removed.

## Length

- 3052 → 3075 words (+23; `analyze_length`; topics hard 4000, soft_warning). Headroom is 924 (hard − 1 − count).
- Additions (+66 approx.) were offset by three trims (L95 meta sentence, L113 redundancy, Further Reading duplicate; −43 approx.).

## Remaining Items

- The computational account of mathematical truth (Deutsch) is still deferred to a dedicated article, carried forward from earlier reviews.
- The McDowell terms were verified through Wright's verbatim quotation, not the primary text, because Google Books search-within was captcha-blocked. If a later pass reaches the primary text, record the page for "realm of law".
- The Szangolies over-statement is still live on three neighbouring pages. These are proposed to the driver as follow-ups and were not edited here:
  - `topics/self-reference-and-the-limits-of-physical-description` L48 and L74.
  - `apex/authority-of-form` L90.
  - `concepts/causal-closure` L134.

## Stability Notes

- **The Szangolies fence belongs on consciousness, not on outcomes.** Szangolies himself derives unpredictable measurement outcomes; what he does not draw is any role for consciousness. A future pass must not move the fence back to "outcome determination", and must not drop his "possible origin" and no-full-reconstruction hedges in order to restore "rigorous mathematics" across the quantum fit. The fixed-point theorem is rigorous. Its fit to quantum theory is, by his own account, open.
- **The Galilean precedent does not by itself favour category error.** The case for category error rests on the recapture premise (L103). Re-installing "supports category error … by design" would reintroduce an "initial method ⇒ permanent limit" transition failure.
- **The L139 Occam line targets logic's authority, not felt compulsion.** Do not change it back to "logical compulsion … cannot be logically justified". That would contradict L87's 07-11 standoff concession.
- All 07-11 and 07-12 stability notes carry forward:
  - Persona disagreements are bedrock.
  - The absence of Lucas–Penrose is correct by construction.
  - The convergence discount stays.
  - The transcendental point is not to be softened.
  - The Wigner "on" fix stays.