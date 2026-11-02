---
title: "Deep Review - The Evolutionary Case for Mental Causation"
created: 2026-11-02
modified: 2026-11-02
human_modified: null
ai_modified: 2026-11-02T23:50:34+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-02
last_curated: null
---

**Date**: 2026-11-02
**Article**: [[evolutionary-case-for-mental-causation|The Evolutionary Case for Mental Causation]]
**Previous review**: [[deep-review-2026-07-19-evolutionary-case-for-mental-causation|2026-07-19]] (8th pass; prior passes 02-05, 03-10, 04-02, 06-02, 06-17, 07-19)

## Why this pass was warranted

Selector rank #2 (rank #1, `affective-tone-divergence-across-meditative-traditions`, was edited today and skipped per the driver brief). The article is not byte-stable since 07-19: commit `980295b917` (09-24) re-cited Heyes→Dunstone & Caldwell, restored the Lacalli quote and rewrote a falsifiability bullet, and `29ed0ec8b6` (10-14) linked the new `inheritance-problem-for-the-psychophysical-law` page. That new page also changed a dependency: it states a selectability trilemma under which "the evolutionary argument therefore inherits the mechanism debt rather than discharging it", and this article's quantum section still implied the opposite.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Fabricated James quotation fragment (attribution error).** L43 read: consciousness "must do something" because "the distribution of consciousness shows it…". The phrase "must do something" occurs nowhere in *Principles* Ch. 5 (psychclassics.yorku.ca prin5.htm, grep of the raw text: 0 hits for "do something"). The 06-02 review certified "The 'must do something' … phrasings also match", and the 07-19 review re-verified only the two long quotes. "He continued:" also implied contiguity, but the steering sentence comes several paragraphs later, in the chapter's summing-up. **Fix:** the fragment is replaced with James's verbatim conclusion, "if it is useful, it must be so through its causal efficaciousness". The steering clause is now quoted from its real subject ("the study a posteriori of the distribution of consciousness shows it…") so that no subject is spliced inside the quotation marks. Corpus sweep: no other live page carries the fragment.
2. **Wrong date and priority claim.** The lede said "first articulated by William James in 1890". James made the argument in "Are We Automata?" (*Mind* 4(13), 1879, 1–22; Crossref doi 10.1093/mind/os-4.13.1). The 1879 text on Wikisource contains the same steering sentence and the pleasure–pain variant. SEP (Robinson 2023, §2.2) cites James 1879 for the argument and "James (1879; 1890)" for the alignment variant. **Fix:** "which William James pressed in 1879 and restated in 1890". The unverifiable "first" is dropped, and the James 1879 reference is added.
3. **Asymbolia presented as an instance of the opposite pattern (internal contradiction).** The text predicted arbitrary valence (injury felt as pleasant while avoidance stays intact), then said "Such cases are rare but not entirely absent: pain asymbolia patients…, yet their avoidance behaviours are impaired." In asymbolia valence and avoidance co-vary, so the case cannot instance the predicted dissociation. **Fix:** the clinical cases now appear as "valence and behaviour failing together rather than any inverted pairing". The rival is named as the co-optimization page names it (a constitutive-physicalist co-optimizer whose felt awfulness *is* the valence prior's computational role), and the "consistent with … also compatible with" calibration is kept. This discharges the P3 task at todo.md "L75 offers pain asymbolia as an instance of arbitrary valence".
4. **One-sided "why this pairing?" argument.** The paragraph ran the classic argument without the replies that its own child page (`co-optimization-reply-to-the-correlation-problem`) weighs. **Fix:** one sentence adds Robinson's reference-fixing reply (cited to Robinson 2023, §2.2, verified verbatim at the SEP), the Map's counter that it "relocates the question rather than dissolving it", and the inbound harmony debt that interactionism shares.
5. **Calibration slippage against the sibling page (possibility/probability).** L99 read "evolution likely built the quantum substrate through which consciousness operates, just as it built the quantum compass in a bird's eye." The page it summarises (`evolutionary-case-for-quantum-neural-effects`) now says avian magnetoreception is on "its leading but unsettled model" and that the argument supplies "plausibility … rather than probability". A tenet-accepting reviewer would flag "likely" together with an established-sounding compass. **Fix:** the sentence now reports the sibling's own calibration. The Further Reading label carrying the same "likely built" claim was fixed as well.
6. **Stale Map-internal characterisation.** L99 said `consciousness-and-causal-powers` flags the four mechanisms "at the speculative-integration evidential tier". That label existed on the page only from 05-18 to 05-19 (`git log -S`: 2d53d51aec added it, 3c30be3a78 removed it). The page now says the mechanisms are "hypothesised, not empirically established" and grades the evidence on a three-rung ladder. **Fix:** "which flags the four mechanisms as hypothesised rather than empirically established".
7. **Dependency moved underneath (selectability constraint).** The MQI tenet paragraph presented quantum indeterminacy as the mechanism the evolutionary argument needs. The 10-14 inheritance page shows that, on the per-context Born-preservation reading, the selector is invisible to selection. The Map therefore cannot hold all three of exact Born preservation, outcome-selection as the only channel, and an evolutionary case that runs through the selector. **Fix:** one sentence in §The Quantum Dimension states the trilemma and links `#the-selectability-constraint`. The MQI paragraph now says the evolutionary argument "inherits that mechanism's open debt rather than discharging it" (the inheritance page's own wording, L129). The trailing clause it replaced, "without violating physical laws…", repeated L97.
8. **Orphan references.** Peper (2020) and Robinson (2023) were in References with no inline citation. Peper is real (Crossref 10.1080/19420889.2020.1713967, 13(1):6–21), but no claim in the article draws on it, and the research note it came from also lists it only as a reference. It has been removed. Robinson 2023 is now cited inline at the reference-fixing reply.

### Medium Issues Found

- **Banned construction.** "This is not a fringe objection. It is the default position…" was rewritten as "Far from a fringe objection, non-reductive physicalism is the default position…". The 06-02 review's boundary-marking reading is kept, and the antecedent of the vague "it" is now named.
- **Heading overclaim.** "Why the Response Fails" became "Difficulties for the Response", because the section itself concedes that the co-optimization rejoinder "remains live". The only inbound anchor is to `#The Correlation Problem`, a subheading that is unchanged.
- **Dropped qualifier.** "preempt the causal contributions" became "preempt the default causal profile" (Saad's term, per `concepts/delegatory-causation`). Saad is now named as the originator, and the second, duplicate wikilink in the same sentence was removed.
- **Cited-author stance (Georgiev).** Georgiev's abstract makes a "reductive identification of conscious experiences with the quantum information comprised in quantum brain states". The clause now records that he is a quantum physicalist, not a dualist, so "quantum-mind partisan" cannot be read as an ally of the Map's dualism.
- **Dunstone & Caldwell.** The hypothesis is "Heyes and colleagues'", per the abstract, so "and colleagues" was added.
- **Unsupported claim removed.** "Without conscious temporal integration, cognition would be limited to moment-by-moment reaction" (2026-02-05 creation text) had no source and is contestable, since non-conscious sequence learning integrates information over time.
- **Weak rebuttal removed.** "But this contradicts intuitions most researchers share" under §What Would Defeat (creation text) appealed to intuition only.
- **Further Reading label.** The pain-consciousness entry changed from "the strongest evidence that phenomenal character tracks adaptive value" to "the paradigm test of whether phenomenal character does causal work", the wording the co-optimization page uses for it.
- **Relation section opener.** "supports multiple Map tenets" became "bears on four Map tenets", because the Dualism and MQI paragraphs now say the support is indirect or carries a debt.

### Publisher-of-record citation ledger (§2.4)

- James 1879 ("Are we automata?", *Mind* 4(13), 1–22): **real-correct** (Crossref doi 10.1093/mind/os-4.13.1). Added. The 1879 text contains the steering sentence and the pleasure–pain argument.
- James 1890 (*Principles*, Henry Holt): **real-correct** (Open Library 1890). Quote 1 ("It is very generally admitted … oyster.") is verbatim. Quote 2 is verbatim and now quoted from its real subject. Quote 3 ("if it is useful, it must be so through its causal efficaciousness") is verbatim and new. The "must do something" fragment was **fabricated** and has been removed (critical 1).
- Georgiev 2024 (*Life* 14(1), 48): **real-correct** (Crossref doi 10.3390/life14010048, issued online 2023-12-27 in the 2024 volume). The quote is verbatim in the abstract, including "however,", and the article truncates before "since epiphenomenal consciousness cannot evolve…". Stance: reductive quantum physicalist (now recorded).
- Lacalli 2024 (*Frontiers in Psychology* 15, 1493423): **real-correct** (Crossref; Thurston Lacalli). The quote is verbatim in the abstract and full text. The source reads "more responsive, though memory, to the past life experiences", and the article's bracketed "[, through memory,]" correctly marks the typo fix. "Proposes" is fair, since Lacalli says "a strong case can be made".
- Dunstone & Caldwell 2018 (*Palgrave Communications* 4, 145): **real-correct** (Crossref doi 10.1057/s41599-018-0200-y). Result direction: the review "examine[s] these arguments", says the theory is not yet directly tested, and proposes methods to test it. The article says "assesses the hypothesis", which matches. Credit is to "Heyes and colleagues" (fixed).
- DeWall, Baumeister & Masicampo 2008 (*Consciousness and Cognition* 17(3), 628–645): **real-correct** (Crossref doi 10.1016/j.concog.2007.12.004; PubMed 18226923). Result direction is confirmed from the abstract: "Substantial decrements in logical reasoning were found when a cognitive load manipulation preoccupied conscious processing, while hampering the nonconscious system with consciously suppressed thoughts failed to impair reasoning". DeWall et al. are dual-process psychologists, and the article already notes that physicalism accommodates the finding.
- Kim 1998 (*Mind in a Physical World*, MIT Press): **real-correct** (Open Library 1998). Cited only for the exclusion argument.
- Robinson 2023 (SEP "Epiphenomenalism"): **real-correct**. The live entry reads "substantive revision Thu Jun 15, 2023". §2.2 "Natural Selection" holds the reference-fixing reply, quoted verbatim on the co-optimization page. It was an orphan and is now cited inline.
- Peper 2020: **real-correct** (Crossref) but orphaned and unused. Removed (critical 8).
- Superlative-claim helper: no hits, so no currency sweep was needed.

### Map-internal quotation and characterisation re-grep

- `co-optimization-reply-to-the-correlation-problem`: the reference-fixing reply ("whatever accompanies its avoidance of injury is displeasure by the meaning of the word"), the Map's "relocates the question without dissolving it", and the shared inbound debt ("One debt is shared whichever reading is taken") are all present. The constitutive-physicalist co-optimizer is defined there. The inbound anchor `#The Correlation Problem` still resolves.
- `evolutionary-case-for-quantum-neural-effects` lede: "leading but unsettled model" and "plausibility … rather than probability" are present (critical 5).
- `consciousness-and-causal-powers` L100: "hypothesised, not empirically established" is present. The tier label the article quoted is gone (critical 6).
- `inheritance-problem-for-the-psychophysical-law` L118 trilemma and L129 "inherits the mechanism debt rather than discharging it": present (critical 7).
- `concepts/delegatory-causation`: "default causal profile" and "preferred causal structure for interactionist dualism" are present, and the latter supports the article's "preferred".
- `concepts/pain-asymbolia`: §"Causal Efficacy of Phenomenal Quality" carries the constrain-vs-establish discipline, and the absent withdrawal and avoidance it describes match the rewritten clinical sentence.

### Counterarguments Considered

- **Co-optimization (property-dualist, Robinson):** now engaged with its reply rather than past it. Mode Mixed: the opening identifies the unexplained pairing (Mode Two), the reference-fixing reply is answered on the Map's realism about felt valence, and the residue is marked honestly as a shared debt (Mode Three).
- **Constitutive-physicalist co-optimizer:** Mode Three. It accommodates the clinical pattern by identity, and the article says the cases "do not on their own discriminate".
- **Epiphenomenalism (Huxley / "selection acts on genes"):** Mixed Mode One and Two, unchanged from 07-19.
- **Illusionism:** Mode One and Two (regress internal to the illusionist's belief-generating mechanism), unchanged.
- **Non-reductive physicalism:** Mode Three (explicit boundary-marking), unchanged.
- No editor-vocabulary labels were leaked into the body (grep clean).

## Optimistic Analysis Summary

### Strengths Preserved
- The three-premise structure, and the lede's admission that the byproduct rejoinder "remains live".
- The §The Physicalist Account of Mental Causation concession that the argument is "equally compatible with non-reductive physicalism and with dualism". The Birch-style restraint this shows is the article's best feature.
- The DeWall hedges ("suggestive (though not decisive)", "the physicalist can accommodate this finding too"), installed by earlier reviews and untouched.
- §What Would Defeat the Argument?, including the 09-24 co-optimization bullet.
- The Lacalli bracket correction and the Dunstone & Caldwell attribution from 09-24.
- The 05-18 constrain-vs-establish parenthetical, kept verbatim.

### Enhancements Made
- The James material is now verbatim and correctly dated. The new "if it is useful, it must be so through its causal efficaciousness" states the argument's own inference in James's words, which is stronger than the fabricated fragment.
- The correlation-problem exchange now mirrors its child page, so the parent no longer contradicts its own spin-off.
- The quantum section now names the Map's own open debt (selectability), so the MQI tenet paragraph is calibrated to the Map's current analysis.

### Cross-links Added
- [[inheritance-problem-for-the-psychophysical-law#the-selectability-constraint|selectability constraint]], the anchored link. The bare-slug body link from 10-14 was already present.

## Length

3255 → 3254 words (analyze_length, topics soft 3000 / hard 4000; soft_warning). Length-neutral mode was applied. The additions (selectability trilemma, Robinson reply, James quotes and date, Georgiev stance, James 1879 reference) were offset by cutting redundancy: the Huxley gloss, the section intro, restated sentences in the definition, correlation, novelty, Lacalli and BI paragraphs, the Peper reference, the unsupported temporal-integration claim, and the intuition rebuttal. No text installed by an earlier review was cut. The two 02-05-review sentences (specific character / "know") were merged with both ideas kept.

## Remaining Items

- The open P3 todo task "`topics/evolutionary-case-for-mental-causation` L75 offers pain asymbolia as an instance of arbitrary valence…" is **discharged by this pass** (critical 3 and 4). The driver should close it so it is not re-offered. Its secondary check, "smile or laugh when pricked", does not apply here, because the article never carried that claim. The claim lives at `concepts/pain-asymbolia` L59 and `co-optimization-reply` L75 ("some smile when pricked"), and remains an open lead for those pages.
- `consciousness-and-causal-powers` is not changed by this review.

## Stability Notes

- Bedrock (do not re-flag): eliminativists reject "consciousness" as a natural kind; MWI defenders resist the collapse framing; hard-line functionalists prefer access to phenomenal consciousness; non-reductive physicalists accept the argument as evidence for physicalism, and the article concedes this explicitly.
- **Lesson for future passes:** prior reviews certified the James quotes as "verified WORD-FOR-WORD" (06-02) and "verbatim confirmed" (07-19), while a short quoted fragment between the two long quotes was fabricated. Grep every quoted span separately, including short ones.
- The selectability-constraint sentence states an open Map debt and is calibration, not a concession to be trimmed. If the Map later resolves the trilemma (for example by adopting the coarser-grain reading), update this sentence rather than deleting it.
- "Strong abductive case" in the lede was a deliberate 06-04 downgrade from "establishes". Do not oscillate it.
