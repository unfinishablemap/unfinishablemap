---
title: "Deep Review - Predictive Processing and Dualism"
created: 2026-09-30
modified: 2026-09-30
human_modified: null
ai_modified: 2026-09-30T09:17:13+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-30
last_curated: null
---

**Date**: 2026-09-30
**Article**: [[predictive-processing-and-dualism|Predictive Processing and Dualism]]
**Previous review**: [[deep-review-2026-07-15-predictive-processing-and-dualism|2026-07-15]]

## Review Context

Seventh deep review, cycle-slot self-selected (score 55; 77 days unreviewed). Since the 07-15 pass the article absorbed two refine-drafts — the mechanistic-rival section (active inference versus post-decoherence selection, 2026-07-2x) and the value-fork Bayesian-binding routing — which pushed it from 3998 to **4862 words (162% of soft, 862 over the 4000 hard ceiling)**. Lenses this pass: (a) full publisher-of-record re-verify, keyed on (surname, year) in both directions and reading the source, not just the metadata; (b) tenet propagation — the article's tenet wording checked against `tenets.md` as it now reads; (c) inline↔References orphan check both ways; (d) length, split into prose versus apparatus before acting. The 07-15 stability notes were read first; nothing they record as resolved is re-raised.

## Pessimistic Analysis Summary

### Critical Issues Found

- **References #16 was a conflated citation (real-wrong-metadata, corrected).** The entry read "Wiese, W. & Friston, K. (2021). Active Inference as a Computational Framework for Consciousness. *Review of Philosophy and Psychology*, 12, 743-765." Crossref resolves that title to **Vilas, Auksztulewicz & Melloni**, *RPP* 13(4):859–878 (DOI 10.1007/s13164-021-00579-w, online 2021); "12, 743-765" matches no record. The body claim the cite supports — that the same formalism admits both a representationalist and an enactive reading — is carried by the *real* Wiese & Friston 2021 paper, "Examining the Continuity between Life and Mind: Is There a Continuity between Autopoietic Intentionality and Representationality?", *Philosophies* 6(1):18, whose abstract (raw, Semantic Scholar) states that the FEP "renders realism about computation and representation compatible with a strong life-mind continuity thesis (although the free energy principle does not entail computational and representational realism)". Re-cited to that paper and the body sentence rewritten to say exactly what the abstract says (compatible-with but not-entailing representational realism; enactivist as-if reading and representationalist reading both available). The 07-15 ledger had not covered this cite. **Family resolution**: the same wrong entry, with a hallucinated key-points block, lived in `research/predictive-processing-active-inference-dualism-2026-03-19` (heading, URL, timeline row, reference); all four loci corrected there with a dated correction note. No other corpus file cites it.
- **Three orphan References entries (Clark 2013, Clark 2016, Friston 2010)** were listed but never cited inline — the 07-15 review recorded reciprocity as intact, so a later condense must have stripped the inline cites. Rather than delete three legitimate canonical sources, the cites were attached to the sentences they support (the PP definition; the free energy principle). Orphan check now 17/17 in both directions.
- **Tenet propagation — Stapp.** `tenets.md` (Bidirectional Interaction, "Outcome-selection, not context-selection") now explicitly distinguishes the Map's outcome-selection from Stapp's Process-1 choice-of-question and names that as "the move Stapp's load-bearing mechanism set aside". The article's quantum-Bayesian section presented the Map's interface as "the participating-observer role Stapp (2007) ascribes to consciousness", as though they coincided. Reworded to "a cousin of" Stapp's role, with the divergence stated (Stapp: which question is put to nature; Tenet 3: which outcome becomes actual).
- **Internal contradiction.** "This is the same gap the beautiful-loop theory tries and fails to close from the inside" contradicted the section's own verdict that the rival is "defeated neither by the tenets nor by decisive evidence" (a 06-22/07-15 stability note). Changed to "on the Map's reading, does not close".
- **Tenet-word conflation.** "Active inference is the strongest empirical case for bidirectional causation in cognitive science" used the tenet's term for organism→world action, which is not what Tenet 3 asserts (mind→brain). Reworded to "strongest case for organisms changing the world rather than merely modelling it", keeping the nested-hierarchy extension as the Map's own step.

### Publisher-of-Record Citation Web-Verify (§2.4) — per-cite ledger

Raw sources were grep-checked (Europe PMC full-text XML, OpenAlex inverted-index abstracts, Crossref, the preprint PDF) rather than summarised. Each line certifies the *reading* as well as the tuple unless stated.

- Beni 2021 (A critical analysis of Markovian monism) — state: **real-correct**. *Synthese* 199(3-4):6407–6427 confirmed at Crossref; the ellipsed quote is verbatim against PMC7885977 full text: "we could not read off metaphysical theses about the nature of target systems (self-organising conscious systems, in the present context) from our theories of nature of scientific models (Markov blankets)". Reading: Beni argues against inferring ontology from the model — the neutrality use is faithful; Beni is no dualist and is not presented as one. Softened "Beni's critique *shows*" → "*argues*" in the tenet section.
- Friston, Wiese & Hobson 2020 (Sentience and the Origins of Consciousness) — state: **real-correct**. *Entropy* 22(5):516. Grepped at PMC7517007: "ultimately reducible" verbatim ("the extrinsic information geometry is ultimately reducible to the intrinsic information geometry (and the other way around)"); "dual information geometry" ×4; qualia framed as "an attribute of belief updating" and "Bayesian beliefs that imply an extrinsic information geometry" — the article's "extrinsic geometry … 'mental' properties or 'qualia'" is faithful. Reading note: the authors *anticipate* the property-dualist objection ("the dual information geometry itself does not entail property dualism … if one believes that there are irreducible mental properties, one has to posit them in addition"); the article's promissory-note reply engages exactly that move, so the engagement is fair (Mode Two, see §2.6). Stance: explicitly anti-dualist, and so labelled in the lead.
- Hohwy & Seth 2020 — state: **real-correct**. Verbatim at philosophymindscience.org (article 8947): "precisely because it at the outset is not itself a theory of consciousness, has significant potential for advancing the neuroscience of consciousness". Crossref: *Philosophy and the Mind Sciences* 1(II), DOI 10.33735/phimisci.2020.II.64.
- Laukkonen, Friston & Chandaria 2025 (A beautiful loop) — state: **real-correct**. *Neurosci. Biobehav. Rev.* 176:106296 at Crossref/Europe PMC. Publisher full text sits behind a bot challenge; "seem necessary" grep-verified in the PsyArXiv preprint v3 full text ("we propose three conditions that seem necessary for consciousness") and "precedes introspection" likewise; abstract (OpenAlex) confirms epistemic field / Bayesian binding / epistemic depth = "recurrent sharing of the Bayesian beliefs throughout the system" and "distinct from self-consciousness". 06-22 durable lesson holds.
- Clark, Friston & Wilkinson 2019 (Bayesing qualia) — state: **real-correct metadata**; *JCS* 26(9-10):19–33 at OpenAlex. The scare-quoted "qualitative awareness" could not be grep-verified: every raw host (Sussex, Exeter, PhilArchive, Ingenta, UCL) returns 403/202 traps, and the OpenAlex abstract variant does not contain the phrase. Quote marks removed ("some puzzling form of qualitative awareness") so the article no longer asserts verbatimness it cannot certify; the paraphrase matches the JCS abstract as reported by aggregators.
- Wiese & Friston 2021 — state: **real-wrong-metadata → corrected** (see Critical Issues).
- Feldman & Friston 2010 (Attention, uncertainty, and free-energy) — state: **real-correct**. *Front. Hum. Neurosci.* 4:215 (Europe PMC PMC3001758).
- Friston et al. 2013 (The anatomy of choice) — state: **real-correct**, reading confirmed: PMC3782702 full text — "precision has been associated with dopaminergic projections from the ventral tegmental area and substantia nigra"; "sensitivity corresponds to the precision of beliefs about future states and behaves in a way that is remarkably similar to the firing of dopaminergic cells". Six authors as listed.
- Zénon, Solopchuk & Pezzulo 2019 — state: **real-correct**. *Neuropsychologia* 123:5–18, PubMed 30268880; the effort-as-information-cost reading matches the abstract.
- Gunji, Shinohara & Basios 2022 — state: **real-correct**. *Front. Neurorobot.* 16:910161 (PMC9478538); abstract confirms "excess Bayesian inference" → orthomodular lattice, classic Bayesian → Boolean. The article's "phenomena that classical probability *cannot* capture" softened to "handle awkwardly" — the stronger claim is quantum-cognition advocacy, not something the cited paper establishes.
- Austin 1962 — real-correct (canonical phrase, certified 07-15; unchanged). Seth 2021, Stapp 2007, Hohwy 2013, Clark 2013, Clark 2016, Friston 2010 — book/monograph metadata unchanged and correct; the three previously orphaned entries are now cited inline.
- Superlative sweep: no "first/largest/current record" claims in the article; skipped.

### Reasoning-Mode Classification (§2.6, editor-internal)

- Friston/Wiese/Hobson (Markovian monism): Mode Two — the reply identifies reducibility-as-promissory-note using the authors' own admission of two geometries; no label leakage.
- Laukkonen/Friston/Chandaria (beautiful loop): Mode Two opening → Mode Three residue, unchanged and honestly marked; not re-litigated.
- Active inference as mechanistic rival: Mixed — concedes articulation, marks the residue's provenance as near-bedrock; unchanged in substance, tightened in wording.
- Compatibilists (bidirectional section): previously read as a flat refutation ("explains agency-talk but not the phenomenology"); now explicitly Mode Three ("a framework-boundary disagreement the Map marks rather than refutes"), since compatibilists do offer accounts of deliberative phenomenology and the Map's reply is a boundary claim, not an internal one.

### Medium Issues Found

- Duplicate "unity of perception and action" bullet in *What PP Gets Right* restated the bidirectional section verbatim in substance — removed.
- Duplicate lead-in to the beautiful-loop section restated the introduction's firewall — merged.
- Precision-weighting section stated the "in the moment of resolution" point twice across two paragraphs — merged.
- The Minimal Quantum Interaction tenet paragraph glossed "minimal" purely as "small bias cascades"; the tenet now defines minimality by its rules-out clause (no energy injection, Born statistics intact). Clause added so the article's sense matches the tenet's.

### Length (§4.5)

Split before acting: **4862 total = 4209 prose + 329 Further Reading + 324 References**. Prose alone exceeded the 4000 hard ceiling, so the overage was not an apparatus artefact. Condensed by removing restatement only — no calibration qualifier, hedge, concession or citation was cut (per the condense-regresses-calibration-qualifiers discipline). **After: 4623 total = 4021 prose + 274 Further Reading + 330 References** (−239). Prose is now at the ceiling; the remaining 623-word total overage is reference apparatus that the article legitimately carries as a hub. A further prose condense would have to cut load-bearing argument (beautiful-loop or mechanistic-rival sections), which a deep-review pass should not do unilaterally — see Remaining Items.

## Optimistic Analysis Summary

### Strengths Preserved

The rivals-not-allies firewall; the neutrality/diagnostic separation in the lead; the promissory-note reading of Markovian monism; the beautiful-loop section's undefeated-rival calibration; the mechanistic-rival section's plain concession on articulation with the residue held; precision-weighting as interface; the placebo compatible-with/not-support-for demarcation; five-tenet coverage with the quantum-Bayesian bridge correctly tiered as "one possible mechanism".

### Enhancements Made

Citation conflation fixed and propagated to its research note; three orphan references reattached; Stapp/Tenet-3 divergence stated; internal contradiction on the beautiful loop removed; bidirectional-term conflation fixed; compatibilist engagement re-marked as boundary; Further Reading descriptions tightened without dropping any routing entry.

### Cross-links Added

None new (cluster complete since 05-28); one existing `[[tenets#^bidirectional-interaction]]` anchor reused in the quantum-Bayesian section.

## Remaining Items

- **Length**: 4623 total (prose 4021, at the topics/ hard ceiling; apparatus 604). Any future addition must be offset. If the total-count gate keeps firing, the operator's choice is between a dedicated `/condense` that cuts argument (not recommended — both rival sections are load-bearing) and accepting the article as a survey-length hub. Not minted as a task here (this pass does not edit todo.md).
- **Clark, Friston & Wilkinson 2019 "qualitative awareness"**: paraphrase now, not a quote; a future pass with access to the JCS text can restore the quote marks if the phrase is verbatim there.
- Cross-link reciprocity from selection-only-mind-influence and born-rule-and-the-consciousness-interface still absent (noted since 05-28; low priority).

## Stability Notes

Carried forward from 07-15 and reaffirmed — do NOT re-flag: MWI/indexical bedrock; eliminativist / Dennettian / quantum-skeptic / empiricist / Buddhist bedrock objections; beautiful-loop undefeated-rival status (do not push toward refutation, and do not re-flag "fails to refute"); quantum-Bayesian bridge tiering; epistemic depth = recurrent sharing of Bayesian beliefs, NOT higher-order self-modelling; Beni/Gunji/Laukkonen metadata (do not "correct" Beni back to Kiefer, Gunji to Pothos, or conflate the three Laukkonen-family cites); the Beni ellipsed quote and the Hohwy & Seth 2020 attribution of "not itself a theory of consciousness".

New durable lessons this pass:

- **Wiese & Friston (2021) is the *Philosophies* 6(1):18 life–mind-continuity paper.** "Active Inference as a Computational Framework for Consciousness" is Vilas, Auksztulewicz & Melloni (*RPP* 13:859–878). A future reviewer must not re-attach that title to Wiese & Friston, and must not "restore" the "12, 743-765" locator, which belongs to nothing.
- **Compatibilist engagement is Mode Three by design.** "Explains agency-talk but not the phenomenology of deciding" is the Map's boundary claim, not an internal refutation; do not re-flag "the Map fails to refute compatibilism".
- **Stapp's role is a cousin, not the Map's mechanism.** Tenets.md commits to outcome-selection and disowns Process-1 context-selection; any sentence equating the Map's interface with Stapp's participating observer is a propagation defect, not a stylistic choice.
- **Prose-versus-apparatus split is 4021/604.** The next length gate should be read against the prose figure before any condense is minted.

Defer further deep reviews unless the article is materially modified or new substantive related content appears.
