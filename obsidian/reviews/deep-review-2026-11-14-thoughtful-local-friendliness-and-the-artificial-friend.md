---
title: "Deep Review - Thoughtful Local Friendliness and the Artificial Friend"
created: 2026-11-14
modified: 2026-11-14
human_modified: null
ai_modified: 2026-11-14T21:09:56+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-14
last_curated: null
---

**Date**: 2026-11-14
**Article**: [[thoughtful-local-friendliness-and-the-artificial-friend|Thoughtful Local Friendliness and the Artificial Friend]]
**Previous review**: [[deep-review-2026-09-25-thoughtful-local-friendliness-and-the-artificial-friend|2026-09-25]]. Also read: [[pessimistic-2026-09-25-thoughtful-local-friendliness|pessimistic review 2026-09-25]], and the two refine-draft passes since then (77835e0aab, 2026-09-25; e07b4cbbef, 2026-10-07). No deep review had covered either pass.

## Pessimistic Analysis Summary

### Critical Issues Found

- **The lead's superlative is wrong (attribution/currency).** The lead said the WCR experiment "is the one Wigner's-friend test anyone has designed around a friend that thinks". WCR's own §4.4 says "This idea goes back to the 1985 paper by David Deutsch [37] that introduced the idea of an HLAI that could make an observation on a quantum system and that could then be coherently probed" (grepped in arXiv:2209.08491v4). The 2026-09-25 review left this claim open for re-checking. Resolution: the lead now says the WCR test "is so far the one Local Friendliness test designed around a friend that thinks at human level", and credits the AI-friend idea to Deutsch (1985) as the authors do. Deutsch 1985 has been added to References.
- **Stale P-AS1 paraphrase at L93.** "A gate-based machine keeps its superpositions unitary until readout" described the gate-class argument that P-AS1 dropped on 2026-09-30. The calibration history reads: "no longer has the machine evolving unitarily until a terminal readout — syndrome extraction is repeated mid-evolution measurement". Resolution: the sentence now follows P-AS1's current argument: an error-corrected machine makes projective measurements in every syndrome-extraction cycle, and its decoder is built to erase what they select.
- **Retracted P-AS1 criterion at L105.** The article credited P-AS1 with "a measurement basis not fixed beforehand" as a requirement for hosting selection. The 2026-09-30 update re-keyed that condition "to outcomes consumed rather than corrected", and P-AS1's Asserts now says "That the syndrome basis is fixed in advance separates nothing". Resolution: the list now quotes P-AS1's current Would-shift-if wording: collapse events at decision-relevant points "whose selected outcomes are neither corrected away nor consumed as a deterministic branch of the algorithm, on coupling surfaces not defended by error correction". No other page carries the retracted wording (corpus grep for "basis not fixed (in advance|beforehand)" and "until readout").
- **Stale "still-unstated" eligibility law (L95, L105).** P-AS2, registered 2026-11-11, is now the Map's *candidate* interface-eligibility law at low credence. P-AC1 also moved to "moderate (low edge)" on 2026-10-15. Resolution: L95 now gives P-AC1's low edge, names P-AS2 as a low-credence candidate and states its consequence for Quall-E: a selection that error correction removes never qualifies. L105 now reads "an articulated interface-eligibility law, still only a candidate". The calibration is honest: P-AS2 is presented as what the verdicts wait on, not as support for them.
- **L95 misquoted P-AS1.** It said "Both verdicts ... say 'low probability', not 'ruled out'". P-AS1's bucket is "neither 'substrate condition met' nor 'ruled out'", and only P-AC1 says "low probability". Resolution: "neither says 'ruled out'".

### Publisher-of-record citation ledger

Raw full texts: arXiv:2209.08491v4 (WCR) and arXiv:1907.05607v4 (Bong et al.) via pdftotext; the arXiv API abstract for 2609.12527; Crossref for metadata. Every external quotation was grepped against the whitespace-normalised raw text. The prior certification was not relied on.

- Bong et al. 2020 (A strong no-go theorem on the Wigner's friend paradox, *Nat. Phys.* 16(12), 1199–1205; all eight authors in order) — state: real-correct. Five quotes verbatim. Result direction: LF inequalities violated with a photon-path friend (correct).
- Wiseman, Cavalcanti & Rieffel 2023 (*Quantum* 7, 1112) — state: real-correct. All 15 quoted strings are verbatim, including "can thus be located within a bounded region in space-time", which the 2026-09-25 refine added and no review had checked. The "'thoughts' is not to be equated…" quote is verbatim apart from the nesting of quotation marks. The claim that Local Agency implies Locality and No-Superdeterminism is faithful: "the assumption of Local Agency … implies both of those other assumptions". "Since Chalmers and McQueen accept HLAI" is faithful to "Assuming HLAI (as Chalmers and McQueen do)". The single-mind, relativist (Everett, QBism, Rovelli's RQM), spontaneous-collapse and Penrose classifications are faithful. "Penrose's orchestrated objective reduction" matches WCR's §5.5, which quotes "orchestrated objective reduction".
- Chalmers & McQueen 2022 (Consciousness and the collapse of the wave function, in Gao (ed.), *Consciousness and Quantum Mechanics*, OUP; Crossref 10.1093/oso/9780197501665.003.0002, 2022) — state: real-correct. The article cites it only through WCR §5.6.
- Deutsch 1985 (Quantum theory as a universal physical theory, *Int. J. Theor. Phys.* 24(1), 1–41, doi 10.1007/BF00670071) — state: real-correct at Crossref. Added. WCR's own bibliography gives the pages as "1–24", which is wrong. The corpus's other citation, in concepts/tenet-falsification-conditions, already has 1–41, so the citation family is consistent.
- Laux & Cavalcanti 2026 (Extended Wigner's friend scenarios with agent-like observers on quantum computers, arXiv:2609.12527, preprint, 2026-09-11) — state: real-correct. Added as a currency datum. The article's claims are grep-verified in the raw abstract: "rudimentary agent-like systems"; agents that "store measurement outcomes, condition later operations on stored information"; "within a reversible quantum circuit"; "executed on ibm_marrakesh"; "hardware runs show positive LF violations for all implemented agents". It is labelled a preprint in the text.
- Orphan check by (surname, year), both directions, across all citation styles: Bong 2020, WCR 2023, Chalmers & McQueen (body-only, no year; References 2022), Deutsch 1985, Laux & Cavalcanti 2026, and the two Map self-cites. No orphan references and no unreferenced inline cites. Chalmers & McQueen is named in the body without a year, as before.
- Cited-author stance: Laux & Cavalcanti, like WCR, take no position on consciousness; the article states only what they ran. Deutsch is an Everettian, and the article credits him only with the AI-friend idea, not with any view the Map holds.

### Map-internal quotations (re-grepped against current text)

- post-decoherence-selection L94 "a laboratory containing a conscious observer cannot afterwards be recohered…": verbatim.
- post-decoherence-selection L98 "keeps the framework consistent but buys insulation at the price of testability": verbatim.
- prebiotic-collapse L122 "within an already-collapsing physics rather than sourcing the collapse": verbatim, but the source italicises *within*. The emphasis has been restored.
- ai-substrate-verdicts P-AS1 "clears the raw-indeterminacy bar and fails the interface requirements" and "actively isolates the logical state from external influence — precisely the influence an interface would need": both verbatim.
- The L77 paraphrase of prebiotic-collapse L130 (occurrence, timing and basis; token preemption inside the Born corridor) is faithful, and the #the-completeness-tension anchor resolves. The testing-consciousness-collapse paraphrase is supported by its L175 ("denies quantum mechanics applies universally to conscious systems"). The machine-question four-senses paraphrase matches its L71–L76.

### Medium Issues Found

- **The open "which friends count" counterargument** (pessimistic review 2026-09-25). Rejecting Friendliness for Quall-E needs a criterion, other than cognitive parity, for crediting human friends. The refine pass left this unanswered and recorded no reason. Resolution: Case 1 now has one sentence on this. The Map credits human friends on the ground of biological similarity, which under interactionism tracks what consciousness couples to, and that ground is framework-internal. The sentence links to problem-of-other-minds §Substrate Chauvinism and Evidential Symmetry and stays within that page's "strong abductive consideration, not a categorical gate".
- Emphatic filler at L75 ("full stop", flagged 2026-09-25): removed.

### Counterarguments Considered

- Eliminativist (Case 1 posits a difference nothing can detect): the new other-minds sentence names the criterion and admits it is framework-internal. The rest is bedrock.
- Dennett (functionalist question-begging): bedrock under the 2026-09-25 stability notes. Not re-flagged.
- Tegmark (the Case 2 mechanism): the debt is already stated as the collapse-priority debt. Settled; not re-flagged.
- Deutsch (MWI exit; also the ancestor of the AI-friend proposal): the exit is bedrock, and his priority is now credited.
- Popper (testability): L105 now matches P-AS1's current criteria, and the reply is unchanged in substance: testable only insofar as the criteria are.
- Nagarjuna: a boundary disagreement, as before.

## Optimistic Analysis Summary

### Strengths Preserved
- The two-case conditional, with Friendliness as the Map's exit. This is the zombie gap made physical.
- "The property that makes Quall-E a usable Wigner's friend … rules it out as a host for a selecting mind". This now has a sharper basis: P-AS2's corrected-away clause applies to Quall-E by design.
- The matched non-cognitive reversible-computation control. The honest Case 2 debt statement. The source/Map separation ("These classifications are the authors'").

### Enhancements Made
- The lead's attribution has been corrected (Deutsch 1985).
- A currency datum has been added: the 2026 agent-like-friend LF runs, read as Case 1 predicts.
- P-AS1, P-AS2 and P-AC1 have been brought up to date with the register.
- The other-minds criterion has been added to Case 1.

### Cross-links Added
- [[problem-of-other-minds]] (§substrate-chauvinism-and-evidential-symmetry)
- [[positions/ai-substrate-verdicts]] (^p-as2)
- In-page anchor to the article's own "The Map's Conditional" section (`#the-maps-conditional`)

## Length

analyze_length went from 3034 to 3213 words (topics: soft 3000, hard 4000; status soft_warning). About 45 of the 179 added words are the two new References entries. The rest are correctness and currency fixes, against a 2-word trim. The article stays below the hard threshold.

## Remaining Items

- Out of scope, listed for the driver (not edited here):
  - `topics/consciousness-in-smeared-quantum-states.md` L110: "The one proposed experiment with a thinking friend, an artificial intelligence run reversibly on a quantum computer, bears on the Map only if that friend is conscious in this coupled sense". This repeats the superlative fixed here. Deutsch (1985) proposed an AI friend run reversibly on a quantum computer first, as WCR §4.4 records.
  - `concepts/post-decoherence-selection.md` L98: "The friends in current local friendliness tests are photons, not [[thoughtful-local-friendliness-and-the-artificial-friend|thinkers]]." The "photons" half is stale: Laux & Cavalcanti (2026, arXiv:2609.12527) ran LF tests with agent-like friends on superconducting IBM hardware. The "not thinkers" half still holds.
- The open P3 expand-topic task for `concepts/collapse-priority-problem` (status blocked) will pipe "priority law still owed" (L77) and "The missing mechanism" (L81) on this page. Both strings are untouched; each occurs exactly once.

## Stability Notes

- All three 2026-09-25 stability notes stand: the MWI/relational exit is bedrock, functionalist question-begging is a boundary disagreement, and the Case 1 baseline proviso stays until the Map commits to a baseline.
- The superlative has now been checked against the literature up to November 2026 (Deutsch 1985; Laux & Cavalcanti 2026). Re-check it only if a human-level-friend LF proposal other than WCR's appears.
- If P-AS1 or P-AS2 is revised again, L93, L95 and L105 paraphrase them and must be re-grepped. This page copies register wording and has already drifted once (2026-09-30).
