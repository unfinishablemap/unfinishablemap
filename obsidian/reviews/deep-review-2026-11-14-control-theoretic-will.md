---
title: "Deep Review - Control-Theoretic Will"
created: 2026-11-14
modified: 2026-11-14
human_modified:
ai_modified: 2026-11-14T19:42:09+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-14
last_curated:
---

**Date**: 2026-11-14
**Article**: [[control-theoretic-will|Control-Theoretic Will]]
**Previous review**: [[deep-review-2026-07-18-control-theoretic-will|2026-07-18]]

## Change Since Last Review

This is the eighth deep review. The 2026-07-18 pass was a no-op on a converged article. Since then, five content commits have landed (`82bd975d51..HEAD`). They are substantive, so this pass is a real review and not a cross-link bump:

- 2026-10-04 (4974ed8e17): the Dualism paragraph now concedes that no current prediction separates a physical from a non-physical controller. The akrasia open question became "Akratic signal mapping".
- 2026-10-04: Further Reading lines added for `the-divided-will` and `self-control-as-skill-and-scaffolding`, plus an Adaptive-control sentence on self-control.
- 2026-10-06 (71806a6b96): new veto-cautions paragraph, citing Schultze-Kraft et al. 2016 and quoting it.
- 2026-10-09 (8a7fc1db20): Tenet 2 gloss at the veto paragraph and in the Minimal Quantum Interaction paragraph.
- 2026-11-09 / 11-10: zero-word pipe to `alief-and-acting-against-belief`, and the Sheppes & Gross 2011 sentence with two quotations.

Two new references (Schultze-Kraft 2016, Sheppes & Gross 2011) and three quotations entered the page with no deep review since. The §2.4 web-verify was therefore mandatory.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Brass & Haggard (2007) attribution (L78).** The page said Brass and Haggard's (2007) "'whether' model identified distinct neural circuitry for this operation". Three earlier reviews (03-21, 04-27, 05-31) certified this as correct. That certification was wrong in two ways, both checked against the PMC6672190 full text:
  - The 2007 paper contains no "whether" model. It studies "the decision whether to act or not", and its abstract claims "a candidate brain area" (dFMC). The named What/When/Whether model is Brass & Haggard's later 2008 paper.
  - **Cited-author stance.** The paper says: "Our data identify a clear neural basis for inhibiting intentions and thus identify the neural correlate of the veto process. The hypothesis of a special, non-neural veto process could therefore become unnecessary." The page had enlisted the authors as support for the controller's veto and left out that they read their result against a non-neural veto.
  - **Resolution**: the sentence now reads "Brass and Haggard (2007) located a candidate fronto-median area for the decision whether to act, a correlate they suggest could make a non-neural veto unnecessary, though an interactionist expects one too". This is a paraphrase with no quotation marks, and it keeps their hedge "could".
- **Veto deadline: internal tension and over-scope (L82).** The paragraph quotes Schultze-Kraft that "even after the onset of the movement, it is possible to alter and **cancel** the movement as it unfolds". It then concluded that veto is "the most time-limited in practice" and that "the operation that stays available longest is attractor steering". There were three problems:
  - The quotation itself shows that cancellation stays available after onset.
  - The study used cued (BCI-emitted) stop signals. The page's own linked sibling `topics/quantum-neural-timing-constraints` L102 scopes the boundary "at least for cued stops" and says a self-initiated veto's boundary "is untested".
  - Nothing supports reading altering or aborting a single foot movement as attractor switching.
  - **Resolution**: "Veto is the most plausible operation in bits, and its onset-withholding form the most time-limited, at least for cued stops; aborting or altering a movement already under way stays available longer." This keeps the 10-06 fix's two points (bit-cost is not Tenet 2's minimality, and the cheapest operation has the earliest deadline). It removes only the unsupported attractor-steering identification.

### Medium Issues Found

- **Zheng & Meister (2025): source/Map conflation (L33, L134).**
  - Their figure is "the information throughput of a human being", that is, behaviour. They place the bottleneck in a neural "inner brain".
  - The page said consciousness selects "through a channel limited to roughly 10 bits per second (Zheng & Meister, 2025)", and at L134 that the figure "is a measured fact about conscious processing".
  - The sibling `concepts/attentional-economics` L48 already scopes it correctly: "That figure is behavioural … it measures what conscious agents *do*".
  - **Resolution**: L33 adds ", the measured throughput of human behaviour". L134 "conscious processing" becomes "behavioural throughput". The Map's claim (the channel) and the source's measurement (behaviour) are now separate.
- **Cisek (2007) gloss (L33).** "runs simulations" is not part of the affordance-competition hypothesis. The paper's "Simulations" are the author's computer simulations of the model. **Resolution**: removed. Cited-author stance: in Cisek's model a single response is selected by neural competition, biased by prefrontal cortex and basal ganglia. The page assigns selection to consciousness only as the Map's own claim, which the lead's "The Unfinishable Map's framework implies" frames.
- **Schwartz & Begley (2002) (L150).** "document how directed mental effort produces measurable neuroplastic changes" presented the authors' causal interpretation as documentation. What is documented is caudate change after therapy. **Resolution**: "document how" became "argue that" (0 words). The source is dualist-sympathetic ("mental force"), so enlisting it is fair, but its interpretation is now marked as an argument.
- **Interface locality (L100).** "a standard control-theoretic requirement, not an ad hoc restriction" claimed more than control theory gives, and more than the linked target says. `consciousness-selecting-neural-patterns` "The Brain Boundary" says locality "follows largely from the selection mechanism rather than as an ad hoc restriction" and adds a caveat about designed external substrates. **Resolution**: "then follows largely from the loop rather than from an ad hoc restriction" (+3).
- **Terminology (L104).** "Disorders of consciousness" is a clinical term (coma, VS/UWS, MCS) and does not cover ADHD, OCD or psychosis. **Resolution**: "Psychiatric conditions—ADHD, OCD, psychosis—" (−3).

### Citation Ledger (§2.4: publisher-of-record, Crossref + PMC full text, 2026-11-14)

- Brass & Haggard 2007 ("To Do or Not to Do: The Neural Signature of Self-Control"), *J. Neurosci.* 27(34):9141–9145, doi 10.1523/jneurosci.0924-07.2007. Metadata real-correct. **Body characterisation was wrong** ("whether" model, "distinct neural circuitry"; stance omitted) and is now corrected, as described above. Result direction: dFMC is more active for intentional inhibition than for action. The page now says this.
- Cisek 2007 ("Cortical mechanisms of action selection: the affordance competition hypothesis"), *Phil. Trans. R. Soc. B* 362(1485):1585–1599, doi 10.1098/rstb.2007.2054. Real-correct. Gloss trimmed ("runs simulations").
- Libet 1985 ("Unconscious cerebral initiative and the role of conscious will in voluntary action"), *BBS* 8(4):529–539, doi 10.1017/S0140525X00044903. Real-correct. The ~550 ms RP and ~200 ms W figures originate in Libet et al. 1983 and are restated in 1985. The page attributes them to "Libet's experiments", not to the 1985 paper, which is acceptable.
- Schultze-Kraft et al. 2016 ("The point of no return in vetoing self-initiated movements"), *PNAS* 113(4):1080–1085, doi 10.1073/pnas.1513569112. Published online 2015-12-14 in the January 2016 issue, so citing it as 2016 is correct. Real-correct. **The quotation was grep-verified** in the PMC4743787 full text, in the Discussion: "However, even after the onset of the movement, it is possible to alter and cancel the movement as it unfolds." The "about 200 ms before EMG onset" figure matches the abstract ("earlier than 200 ms before movement onset") and the Results ("starting around 200 ms before EMG"). Stance: "the original interpretation of the veto was dualistic, whereas in our case veto is meant akin to 'cancellation'". The page cites them for timing only and does not enlist them for dualism.
- Schwartz & Begley 2002, *The Mind and the Brain*, ReganBooks. Real-correct (stable book). The characterisation is now marked "argue".
- Sheppes & Gross 2011 ("Is Timing Everything? Temporal Considerations in Emotion Regulation"), *PSPR* 15(4):319–331, doi 10.1177/1088868310395778. Real-correct. **Both quotations were grep-verified** in the abstract (Europe PMC): "Regulation strategies that target early processing stages require minimal effort" and "regulation strategies that target later processing stages require effort that is proportional to the intensity of the emotional response". The page presents them as a hypothesis ("hypothesise"), and the abstract frames them as "an alternative process-specific timing hypothesis". Faithful.
- Stapp 2007, *Mindful Universe*, Springer. Real-correct. The quantum Zeno effect is called "one candidate", which is consistent with `tenets` registering Stapp's Process-1 route without adopting it.
- Wiener 1948, *Cybernetics*. Real-correct. The first edition was Technology Press (MIT) with Wiley and Hermann, and "MIT Press" is the conventional citation.
- Zheng & Meister 2025 ("The unbearable slowness of being: Why do we live at 10 bits/s?"), *Neuron* 113(2):192–204, doi 10.1016/j.neuron.2024.11.008. Metadata real-correct. **Result scope corrected**: the figure is behavioural throughput, not a measured consciousness channel.
- `find_superlative_claims`: 0 candidates.
- Orphan check, keyed on (surname, year), both directions: 9 inline cites and 9 References entries map one-to-one: Brass & Haggard 2007, Cisek 2007, Libet 1985, Schultze-Kraft 2016, Schwartz & Begley 2002, Sheppes & Gross 2011, Stapp 2007, Wiener 1948, Zheng & Meister 2025. No orphans.

### Map-internal Quotations and Anchors (re-grepped against current text)

- Further Reading quotes "stable preferences that move action" for `wholeheartedness-void`. The phrase is live at that page's L99.
- `emotion-regulation-and-the-timing-of-control#not-uniform`: the `{#not-uniform}` heading is live at L65. The two Sheppes & Gross strings also match that page.
- `valence-and-conscious-selection#the-value-sensitive-horn-valence-as-selection-currency`: the heading is live (L93).
- `consciousness-selecting-neural-patterns#The Bandwidth Constraint` / `#The Brain Boundary`, `attentional-economics` (3 anchors) and `motor-selection#The "Can Move / Won't Move" Distinction` are all live.
- The glosses for `quantum-neural-timing-constraints`, `self-control-as-skill-and-scaffolding` ("The fit discriminates nothing", L88), `the-divided-will` (L87) and `anarchic-hand-and-action-ownership` (L86 "write-access") all match their targets' current text.
- Tenet 2 glosses at L82 and L134 match `tenets` L69 ("empirical-constraint minimality … no detectable energy injection, no detectable Born-statistics deviation, no conservation-law violation") and the scoped "aggregate" Born wording.

### Counterarguments Considered

All six adversarial personas engaged:
- **Churchland and Dennett** are answered by "Analogy, Model, and Ontology" and by the Dualism paragraph's admission that there is no current discriminating test. The new Brass & Haggard clause gives the physicalist reading in the authors' own words and answers it in one clause.
- **Tegmark**: the actuator is kept as a candidate.
- **Deutsch**: the No-Many-Worlds paragraph is bedrock, per earlier reviews.
- **Popper's ghost**: the veto-deadline paragraph is now scoped to what the cued-stop experiment shows.
- **Nagarjuna**: bounded by "What Control-Theoretic Will Is Not".

### Calibration (§2)

- **No tenet-as-evidence upgrade.** L132 and L140 explicitly deny that stability or the operations pay for the non-physical posit.
- **Possibility/probability slippage.** The two calibration items fixed this pass (veto deadline over-scope and the Zheng & Meister scope) were both evidence-scope errors of the kind a reader who accepts the tenets would still flag. Both are corrected.
- **Necessity vocabulary.** L100's "standard … requirement" was the page's one necessity-register claim. It is now scoped to "largely" to match its own linked source.

### Reasoning Mode (§2.6, editor-internal)

- Engagement with Brass & Haggard's anti-non-neural-veto reading is Mode Two: they infer from "a neural correlate exists" to "no non-neural veto is needed" without the further premise that a correlate rules out a non-physical initiator. An interactionist predicts the correlate too.
- Functionalism, computationalism and eliminativism are Mode Three (boundary-marking).
- No label leakage.

## Optimistic Analysis Summary

### Strengths Preserved

- "Analogy, Model, and Ontology", the article's standout honesty section. Only one redundant sentence was removed, and its referent was carried into the next sentence.
- The taxonomy of five control operations, the mapping table, and the bandwidth-as-design reframing (thermostat, pilot).
- Two points from the 10-06 fix: "the cheapest operation has the earliest deadline", and bit-cost is not Tenet 2's minimality.
- The Dualism paragraph's admission "the Map owes that test and does not yet have it".
- The Occam paragraph's narrowing ("blocks dismissing the posit on grounds of simplicity alone").
- The akratic signal mapping, with the divided-will contrast between predicting and accommodating.

The sympathetic personas found no expansion that would earn its words at 2,964 against the 2,500 soft limit. The Hardline Empiricist praises the scoping this pass added: the cued-stop qualifier, and the behavioural framing of the 10 bits/s figure.

### Enhancements Made

- Brass & Haggard stance clause, with a one-clause interactionist reply.
- Veto-deadline sentence aligned with the timing page and the quoted source.
- 10 bits/s figure attributed to behaviour (two loci).
- Removed for length: "This distinction matters and deserves explicit treatment." (filler), "Engineers apply it to thermostats, aircraft, and chemical plants." (repeats L102's examples) and the L128 sentence that repeated L124.

### Cross-links Added

None needed. All reciprocals already exist.

## Length

2,966 → 2,964 words by `analyze_length` (concepts: soft 2,500, hard 3,500). The pass was length-neutral: additions of +18, +6, +6 and +3 were offset by −2, −3, −6, −9 and −15.

## Remaining Items

Out of scope. These are listed and not edited:

- `concepts/consciousness-selecting-neural-patterns` L78: "recent research (Zheng & Meister, 2025) found conscious thought operates at approximately 10 bits per second". It conflates source and Map in the same way as fixed here. Z&M measure "the information throughput of a human being" (behaviour). `concepts/attentional-economics` L48 is the correct model.
- `topics/anarchic-hand-and-action-ownership` L123: "[[control-theoretic-will]] — the comparator/forward-model treatment of will this article engages." This page never mentions comparators or forward models (0 hits for `comparator|forward.model`), so the gloss is wrong.
- `voids/wholeheartedness-void` L120: "[[control-theoretic-will]] — The decision-theoretic frame the void exceeds". This is already covered by open P3 task item (D) on that page, so no new task is needed.
- Possible family defect, not swept this pass. Twelve live pages mention Brass. The two that name the "whether" model (`apex/phenomenology-mechanism-bridge` L106 and `topics/consciousness-and-causal-powers` L128) correctly cite it as 2007, 2008. Whether any page enlists Brass & Haggard as neutral support for conscious veto, omitting their "non-neural veto process could therefore become unnecessary", was not checked.

## Stability Notes

- **Bedrock, do not re-flag**: the MWI standoff, physicalist adoptability of the framing, and quantum-mechanism speculation. All are framework-boundary disagreements.
- **Do not re-certify Brass & Haggard 2007 as a "whether" model or as neutral support.** The paper argues that its correlate could make a non-neural veto unnecessary. The page now says so and answers it in one clause. Do not delete the stance clause to save words.
- **Veto deadline**: the scoping "at least for cued stops" and "aborting or altering … stays available longer" follow the Schultze-Kraft Discussion and the timing page. Do not restore "the operation that stays available longest is attractor steering". No source supports it.
- **10 bits/s** is behavioural throughput (Zheng & Meister). The channel reading is the Map's. Keep the two separate.
- **Length**: 119% of soft. Future reviews must stay length-neutral.
- **Expect no action items** on the next pass unless new citations are added or a linked anchor moves.
