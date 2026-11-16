---
ai_contribution: 100
ai_generated_date: 2026-11-16
ai_modified: 2026-11-16 16:18:03+00:00
ai_system: claude-fable-5-2
author: null
concepts: []
created: 2026-11-16
date: &id001 2026-11-16
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-16 16:18:03+00:00
modified: *id001
related_articles: []
title: Deep Review - The Transit Void (quotation and source-fidelity audit)
topics: []
---

**Date**: 2026-11-16
**Article**: [The Transit Void](/voids/transit-void/)
**Previous review**: [2026-07-20](/reviews/deep-review-2026-07-20-transit-void/)
**Trigger**: driver-chosen. A refine pass at 14:35Z found one quotation on this page ("micro-acts", Petitmengin 2006) that is absent from its source and traced it to a research note. This pass checks every other quoted string and every attributed paraphrase against the source itself. The five earlier reviews certified metadata only; none grepped a quotation.

## Length

| Measure | Before | After |
|---|---|---|
| `analyze_length` total (voids: soft 2000 / hard 3000 / critical 4000, fires at >=) | 3514 | 3505 |
| Prose | 2799 | 2779 |
| References list | 575 | 586 |
| Further Reading | 100 | 100 |
| Video embed boilerplate | 40 | 40 |

Net change is -9 words. The prose alone (2779) is under the hard gate; the total fires because of 726 words of apparatus (30 references, the Further Reading list and the embed block). The prose is still 39% over the soft threshold. A condense task is not warranted by the hard gate; a prose-only condense toward the soft threshold is optional and should not touch the reference list, which is now cited entry by entry.

## Quotation Table

Every string in quotation marks on the page, with the route used and the count returned by a grep of the fetched text.

| String as it stood | Source route | Count | Verbatim | Subject / work right | Seeded by a note | Action |
|---|---|---|---|---|---|---|
| "tension of consciousness" (Maeda) | phenomenologyonline.com page text | 1 | yes | No. Maeda puts the phrase in quotation marks and cites Schutz (1962); she writes "polarities", never "paradox"; the clause "the loosening cannot itself be conscious" is not hers. Her sentence is "This unawareness of being able to forget everything makes it possible to fall asleep." | voids-transition-void-2026-03-05 L123 | Rewritten: term credited to Schutz via Maeda; the unsupported clause replaced by what she says |
| "the focal anterior P3a can occur nonconsciously" (Escera and Corral 2007) | author-hosted PDF (ub.edu/brainlab), pdftotext | 0; "focal anterior" 0; "conscious" 0; "aware" 0 (also 0 with whitespace stripped) | no | The paper never uses the word "conscious". Europe PMC full-text phrase search returns 0 for the string anywhere. | voids-distraction-void-2026-04-23 L78 | Quotation removed. Escera and Corral re-cited for what they do say: P3a/novelty-P3 as the signature of involuntary orienting |
| "only when consequences seem detrimental, either in retrospect or from the vantagepoint of a third-party observer" (Anderson 2024) | PMC12270342 full text via NCBI efetch | "only when consequences seem detrimental" 0; "vantagepoint" 1 | spliced | Source: "We just call it distraction when the consequences of attention allocation seem detrimental, either in retrospect or from the vantagepoint of a third-party observer". The opening four words were not Anderson's. | voids-distraction-void-2026-04-23 L68 | Quotation marks moved to start at "seem detrimental"; the introspection inference marked as the Map's |
| "largely determined by spontaneous subthreshold fluctuations in neuronal activity" (Schurger et al. 2012) | Europe PMC abstract (PMID 22869750) | 1 | yes | Subject right ("the precise moment at which the decision threshold is crossed"), but the source conditions it on "when the imperative to produce a movement is weak", which the page dropped | voids-initiation-void-2026-03-30 L57 kept the condition; the page lost it | Condition restored |
| "intend[ing] the phase of the object about to occur" (Husserl 1991) | IEP phe-time page: 0. SEP self-consciousness-phenomenological (current and three archived editions): 0. Europe PMC phrase search: found in Martin, Gergel and Owen 2019, who quote it from Zahavi 2003 p. 83 | n/a | not Husserl's words | The wording is Zahavi's gloss of Husserl ("a more or less indefinite intention of the phase of the object about to occur"), cited on the page to the Brough translation | voids-initiation-void-2026-03-30 L89 and voids-readiness-void-2026-03-04 L65 | Quotation marks removed; paraphrased; "below conscious access" dropped (protention is a moment of consciousness, implicit rather than unconscious) |
| "multiple contributories, some reflectively conscious, some pre-reflectively conscious, and some non-conscious" (Gallagher 2012) | Full text not obtained (CORE 403, figshare 202, UoW copy is a different paper). Two secondary routes agree: the ScienceDirect abstract snippet and a Taylor and Francis article quoting p. 28 | not grepped in a raw source | compressed | Both secondary routes give "some of which are" three times; the page had silently dropped the words inside the quotation marks | voids-initiation-void-2026-03-30 L99 | Quotation marks narrowed to "multiple contributories"; the rest paraphrased. **Still unverified against the paper itself** |
| "an illusory phenomenology of self-causation" (Metzinger 2013) | Europe PMC full text of the 2013 Frontiers paper (PMC3868016): "self-causation" 0, "illusory" 0 outside the reference list. Metzinger 2015, "M-Autonomy", JCS 22(11-12) 270-302, author PDF: 1 (p. 291) | 0 in the cited work, 1 in the other | yes | Wrong work, and the source is conditional: "If this is true, an illusory phenomenology of self-causation will be a necessary neurocomputational fiction in the construction of any new EAM". The page had "consciousness constructs". | voids-initiation-void-2026-03-30 L68-71 (heading "Metzinger (2013, 2015)", URL of the 2013 paper only) | Re-cited to 2015; "may require"; Metzinger 2015 added to References |
| "always been there" (mood shifts) | unattributed scare quotes | n/a | n/a | n/a | n/a | Left |
| "I gradually drifted off around eleven" | the page's own example | n/a | n/a | n/a | n/a | Left |
| "Random neural firing produces random thoughts" | a position quoted without an owner | n/a | n/a | No one is cited as holding it | n/a | Removed with its sentence |
| "insight emerges suddenly, its operations largely eluding consciousness (Petitmengin, 2006)" | corrected at 14:35Z | n/a | n/a | n/a | n/a | Not touched |

Five of seven attributed quotations were defective in words, subject or cited work. All five trace to research-note lines that the page copied.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Escera and Corral quotation absent from the paper**: removed (above).
- **Metzinger quotation cited to the wrong work and stripped of its conditional**: fixed (above). "Epistemic agent model collapse" as an italicised term reworded to "a collapse of the epistemic agent model"; the 2013 text has "collapse of the EAM".
- **Husserl quotation is a commentator's gloss**: fixed (above).
- **Anderson and Gallagher quotations altered inside the marks**: fixed (above).
- **Maeda credited with Schutz's term and with a claim she does not make**: fixed (above).
- **Analayo (2003) "reports the convergent finding" that the highest training "does not dissolve the void but locates it more precisely"**: no research note carries this; it entered at the transit merge (`252ca10e40`) from initiation-void. The archive.org full text of the book returns 0 for every probe of the idea ("retrospective", "in retrospect", "cannot be caught", "after onset", "moment of arising", "already arisen"), and the Satipatthana Sutta as Analayo translates it says the reverse of the page's thrust: the practitioner acts "clearly knowing" when "falling asleep, waking up" and contemplates "the nature of arising". The sentence now says the question is unsettled and cites Analayo for the sutta's instruction.
- **"EEG studies of yoga nidra show high gamma"**: uncited in the original article and absent from the notes. Thompson (2014), searched through archive.org full-text search, reports higher gamma activity in experienced meditators during NREM sleep, when gamma normally decreases (the Ferrarelli et al. study of mindfulness meditators), and mentions yoga nidra only in a note on Satyananda. Sentence re-scoped to the finding Thompson reports and the citation moved onto it. The "(Thompson, 2014)" previously attached to the "fundamental tension" sentence had no basis in the note, which calls the tension its own; the citation was moved off.
- **Dream forgetting stated as a human fact**: the NIH release (Wayback copy, 2026-08-01) describes a mouse study of memory tasks; the dream link is Kilduff's "may prevent the content of a dream from being stored". Rewritten with "In mice" and "may".
- **Brown and McNeill (1966) cited for staged lexical access and a blocking word**: the paper reports knowledge of syllable count, stress and letters in the tip-of-the-tongue state ("generic recall"); the blocking hypothesis is later. Rewritten.
- **Internal contradiction with the conjunction-coalesce apex**: the page asserted it is a conjunction-coalesce whose "joint claim is stronger than any single face" and that "dissolving the seam into one mechanism would lose analytical purchase", while the apex (L116) holds that the page "is best held as a single-mechanism article wearing a conjunction's vocabulary, not a confirmed conjunction-coalesce" and the page itself says the faces "share one architecture". Rewritten to state the classification as offered and unconfirmed. The apex quotes the string "the in-flight-access instance of the conjunction-coalesce"; that string is preserved.
- **Calibration, Schurger**: "it is inherently indeterminate, and no observer, internal or external, could predict the precise moment" went beyond a stochastic-accumulator model; now "unpredictable in practice". In the tenet section "indeterminate zone" became "noise-dominated zone". "The materialist narrative" became "the Libet-era narrative" and "the materialist reading of Libet" became "the epiphenomenalist reading", since Schurger's model is itself physicalist.
- **Calibration, tenet section**: "The structured, personally meaningful stream suggests active selection over passive reception" contradicted the body, which attributes that structure to the default network. Now "fits active selection but equally fits associative dynamics". "We choose the destination but cannot watch the journey" removed.
- **Over-concession**: "without ... leaving a detectable signature" read as untestable in principle and sat beside "distinguishing tests arrive". Now "a currently detectable signature".
- **Voids register**: the Dualism paragraph argued from "a physical system's transitions are in principle observable from any vantage point", which is about third-person observation and does not bear on self-opacity. Replaced with the register's grade, following the 2026-11-15 rewrites of plurality-void and acquaintance-void: the opacity does not discriminate, the object-among-objects reading is the Map's, and the cumulative step is suspended ([P-V3](/positions/voids-as-evidence/#p-v3)).

### Medium Issues Found

- Lead: "the structural impossibility common to these cases" now "the structural limit the Map finds common to these cases". The body carries a section on what would undermine the claim and now records the sutta's contrary instruction.
- "Spontaneous thoughts appear fully formed ... as if delivered from elsewhere": universal removed ("typically appear with no phenomenology of generation").
- "prove to be one void seen from two sides": removed (unsupported, and at odds with the unconfirmed classification).
- Frankish (2016) "argue that" dissolving 3am insights are artifacts: Frankish does not discuss them; now "would treat".
- "Current evidence: training extends edge-territory" had no citation; now "On present reports".

### Citation Ledger

- Libet et al. 1983 — metadata real-correct (carried; Crossref returns the 1993 reprint first). Figures not re-read this pass.
- Schurger, Sitt and Dehaene 2012 — real-correct (Europe PMC: 109(42) E2904-13). Result leg: abstract read; quote verbatim; condition restored.
- Neafsey 2021 — real-correct (Europe PMC: 94, 103171). Abstract supports the paraphrase (RP possibly an "artifact of averaging"; Libet's results "no longer valid reasons").
- Killingsworth and Gilbert 2010 — metadata carried; Crossref lookup returned a dataset record, not re-verified. 46.9% not re-read.
- Christoff et al. 2016 — real-correct (OpenAlex).
- Irving 2016 — real-correct (OpenAlex; online 2015, print 2016). "Not monitored as it unfolds" not checked against the text.
- Buckner et al. 2008 — real-correct (Crossref).
- Metzinger 2013 — real-correct; quotation moved off it.
- Metzinger 2015 — added; real-correct (PDF header: JCS 22, No. 11-12, 2015, pp. 270-302).
- Gallagher 2012 — real-correct (Crossref: 30(1) 15-31, print April 2012). Quote unverified against the paper.
- Merleau-Ponty 1945/2012; Husserl 1991; Dennett 1991; James 1902 — books, not fetched.
- Eldridge 2020 — real-correct (OpenAlex). "Double concealment" seen only in an aggregator summary; unverified.
- Petitmengin 2006 — real-correct (Crossref).
- Thompson 2014 — book; gamma passage found by full-text search.
- Nisbett and Wilson 1977; Wegner 1994; McGinn 1989 — real-correct (Crossref).
- Maeda — web text confirmed at Phenomenology Online.
- Analayo 2003 — full text read; claim replaced.
- Schooler et al. 2011 — authors and title confirmed (Crossref); volume and pages carried. Paraphrase not re-read.
- Anderson 2024 — real-correct (Europe PMC: 32(9-10) 959-978).
- Escera and Corral 2007 — real-correct (PDF header: 21(3-4) 251-264).
- Pitts et al. 2014; Aru et al. 2012 — real-correct (Crossref).
- Brown and McNeill 1966 — real-correct (OpenAlex).
- NIH 2019 — real-correct; primary is Izawa et al. 2019, Science 365(6459) 1308-1313.
- Frankish 2016 — carried; Crossref lookup did not return it.

(Surname, year) both directions: every reference is cited in the body and every body citation has an entry (30 entries).

Cited-author stance: Metzinger, Schurger, Anderson, Dennett, Frankish and McGinn are not presented as endorsing dualism; McGinn's and Dennett's disclaimers stand, and the Dualism paragraph now says the physicalist models predict the opacity.

### Reasoning-Mode Classification (editor-internal)

Unchanged from 2026-07-20: illusionism mixed (Mode One/Two); Dennett Mode Three. No editor vocabulary in the article.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-face frame and the watching/crossing formulation.
- The ERP caveat (Pitts, Aru) and the "interpretive stance ... not interface evidence" sentence.
- The Minimal Quantum Interaction paragraph's "framework-internal coherence, not interface evidence".
- The McGinn and Dennett source/Map separations.
- The "What Would Challenge This View" list.

### Enhancements Made

- Metzinger 2015 added as the source of the self-causation passage.
- The Dualism paragraph links the voids register.

### Cross-links Added

- positions/voids-as-evidence ([P-V3](/positions/voids-as-evidence/#p-v3) anchor)

## Remaining Items

Not minted as tasks (driver instruction). For the driver:

- `obsidian/research/voids-distraction-void-2026-04-23.md` L78: the "Quote" `"MMN is a pre-attentive index of novel detection and P3a is the involuntary capture of attention... the focal anterior P3a can occur nonconsciously."` is absent from Escera and Corral 2007. L68: `"only when consequences seem detrimental, either in retrospect or from the vantagepoint of a third-party observer."` has an invented opening.
- `obsidian/research/voids-initiation-void-2026-03-30.md` L68, L71: both Metzinger quotations are from the 2015 JCS paper, under the 2013 URL. L89: `"intends the phase of the object about to occur"` is Zahavi's wording and is not on the IEP page given as the URL. L99: Gallagher quote drops "of which are".
- `obsidian/research/voids-readiness-void-2026-03-04.md` L65: `"Protention intends the phase of the object about to occur thereby providing a future-oriented temporal context for the primal impression."` is not on the SEP Husserl page route tried; grep any page that quotes it.
- `obsidian/research/voids-transition-void-2026-03-05.md` L123: Maeda credited with the claim that "this loosening cannot itself be conscious".
- `obsidian/research/voids-thoughts-that-slip-away-2026-01-13.md` L72: "MCH neurons actively prevent dream content from being stored in hippocampus" drops "mice" and "may".
- Other pages: grep the corpus for `focal anterior P3a`, `illusory phenomenology of self-causation`, `about to occur`, `multiple contributories`, `only when consequences seem detrimental`, `yoga nidra` with `gamma`, and `Analayo` with "cannot be caught" or "locates it more precisely". Archived parents (`archive/voids/initiation-void`, `distraction-void`, `transition-void`) carry the originals.
- Unverified on this page: Gallagher 2012 wording at source; Eldridge's "double concealment"; Schooler's "long stretches"; Irving's "not monitored"; the ERP latency figures; Libet's 550/200 ms; Killingsworth's 46.9%.

## Stability Notes

Prior notes carry forward (MWI indexical disagreement; Buddhist stance difference; Dennett; three-face frame; the 2026-06-10 tenet softening). Two are amended:

- The 2026-07-20 note that the page is a coherent conjunction-coalesce is superseded by the apex's own verdict that the classification is unconfirmed. Do not restore "the joint claim is stronger than any single face".
- "Citations verified" in the five earlier reviews covered metadata. Quotations and paraphrases were first checked on 2026-11-16. Do not restore the Escera quotation, the yoga nidra gamma claim, the Analayo "convergent finding", or quotation marks around the protention wording.
- The Dualism paragraph's register sentence is calibration, matching plurality-void and acquaintance-void. Do not restore the "observable from any vantage point" argument.