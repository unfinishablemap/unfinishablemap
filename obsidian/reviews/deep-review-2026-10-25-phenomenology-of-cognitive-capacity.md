---
title: "Deep Review - The Phenomenology of Cognitive Capacity"
created: 2026-10-25
modified: 2026-10-25
human_modified: null
ai_modified: 2026-10-25T20:20:38+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-25
last_curated: null
---

**Date**: 2026-10-25
**Article**: [[phenomenology-of-cognitive-capacity|The Phenomenology of Cognitive Capacity]]
**Previous review**: [[deep-review-2026-07-18-phenomenology-of-cognitive-capacity|2026-07-18]]

## Summary

This is the seventh review. Selected by `deep_review.py next` (score 71, 99 days unreviewed). The article was *not* converged: two refine-drafts moved it after the 2026-07-18 no-op pass. `3a292b3511` (09-11) rewrote the Bidirectional Interaction paragraph under P-A4 and added Macnamara 2014. `5a829490b4` (09-14) rewrote No Many Worlds to an indexical framing. Both fixes touched only their own paragraph. Four sibling passages in the same file still made the move the 09-11 fix had retracted: the lead, the maintenance paragraph, the reversal paragraph and the Occam paragraph. The article therefore contradicted its own Tenet 3 paragraph. This pass carries the 09-11 repair through the whole file. It also fixes a Dreyfus misreading and replaces an uncited empirical claim with two verified studies, one of which partly disconfirms the article's access claim.

Length: 2803 → 3074 words (prose 2399 → 2607; references 221 → 284; Further Reading unchanged at 183). That is above the topics soft threshold of 3000 and well under the hard threshold of 4000. Eight redundancy trims (about 80 words) offset part of the growth.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Internal contradiction / P-A4 (L99).** The old text read: "If consciousness were epiphenomenal, there would be no phenomenology of effort in maintenance … Behavioural evidence supports this". This contradicts L139, which says the felt gradient "is neither proof of efficacy nor evidence against it". Epiphenomenalism permits felt effort, so the conditional is false. **Fix:** the paragraph now says the felt doing does not by itself defeat epiphenomenalism, and that the Map's case against it rests on the self-stultification problem in [[epiphenomenalism]]. This avoids conceding epiphenomenalism while not pretending the phenomenology decides the question.
2. **Citation framing (L99, Rouder).** The old text was "…a discrete capacity limit of roughly four items (Rouder et al., 2008), and the felt sense of approaching that threshold precedes measurable performance decline", all under "Behavioural evidence supports this". Review 1 (02-23) removed the metacognitive claim from Rouder but left the clause inside the evidence sentence, so that fix was incomplete. **Fix:** the uncited clause is removed. Rouder is now quoted from the PubMed abstract with the paper's own scope qualifier: "highly consistent with a discrete fixed-capacity model of working memory for this task". The "roughly four" figure stays with Cowan 2001 at L91. Rouder's own fitted estimate could not be grep-verified because the PMC full text is captcha-walled, so no number is attributed to Rouder.
3. **Calibration: data fit without evidencing (L47 lead, L101 heading, L119, L137, L145).**
   - *Lead.* Old: "provides evidence that … these boundaries are irreducible to functional descriptions". New: functional descriptions "do not supply" the felt character (matching L139's own wording), and the phenomenology "fits the Map's interactionist reading without establishing it".
   - *Heading.* "Evidence for the Interface Model" became "Fit with the Interface Model", with a sentence noting that any capacity-limited architecture predicts the same three patterns. The heading had no inbound anchors, so renaming it was safe.
   - *L119.* Old: "The Map interprets this as evidence for bidirectional interaction". New: "reads this through", with practice-driven neural restructuring named as the physicalist account of the same clumsiness.
   - *L137, Dualism.* Old: "point to consciousness as … rather than being identical to them". New: "fit that picture … though a physicalist redescription of both remains available". This applies P-TU1's "constrains without establishing" ruling.
   - *L145, Occam.* Old: "records the dynamics of a causal agent". That was a P-A4 violation, and it also used Tenet 5 as a weapon against reductions. It is rewritten so that Tenet 5 binds the Map's own reasoning symmetrically. The Map's complaint about the reductions now rests on the Dualism argument, not on this tenet.
4. **Attribution: Dreyfus misread by contrast (L81).** Old: "Dreyfus (2002) argued that expert performance proceeds without mental representations … The residual phenomenology the Map identifies suggests something more nuanced: not the absence of experience but its transformation". That implies Dreyfus held that experience is absent. He holds the opposite. **Fix:** two grep-verified quotes from the raw PDF (mit.edu/~shaslang/mprg/DreyfusIWR.pdf) showing absorbed coping as experienced and inarticulable. A stance clause adds that Dreyfus found the same structure in simulated neural networks and in Freeman's brain dynamics (abstract), so the agreement is phenomenological only and Dreyfus is not enlisted for dualism. The old "bypasses deliberation entirely" overstated his "almost entirely on intuition" and was dropped.
5. **Unsupported claim plus a partial disconfirmation (L129, with L59/L63/L91/L93).** Old: "Current evidence supports the correlation" was uncited. Old L93 claimed "privileged access". Adam & Vogel 2017 show participants identified only about 28% of their working-memory failure trials. **Fix:** the falsifier now reports both directions: Rademaker et al. 2012 (confidence predicts successful maintenance) and Adam & Vogel 2017 (quoted verbatim from the PubMed abstract). L93 now reads "first-person access … partial and fallible". Hedges were added at L59 ("Often"), L63 ("When the drop is noticed") and L91 ("Often … the strain is felt first") so the phenomenological descriptions no longer contradict the new evidence.

### Medium Issues Found
- **"Not X — Y" constructions.** L85 "Consciousness is not retreating — it is being released" and L123 "These sensations are not mere accompaniments — they are". Both rephrased. L85 had also contradicted the article's own "withdrawal" framing.
- **Computational straw man in the Dualism paragraph.** Old: "A computational system that exceeds buffer capacity simply fails". Review 1 fixed this in L65 but not here. New: "can register that it is near capacity; a conscious subject also *experiences* the approaching limit."
- **Minimal Quantum Interaction.** Added that delegation makes the same sense for any capacity-limited system, so the fit is coherence, not support. Tenet 2 is not redefined.
- **Tenet 3 paragraph.** "The systems consciousness participates in building…" now opens "On that reading," so it matches the paragraph's own P-A4 sentence.
- **Precision fixes.** Sweller 1988 concerns *learning* (title: "Effects on Learning"), so "performance consequences" became "what exceeding these limits costs learning". Cowan's unit is chunks, so "four items without rehearsal" became "four chunks when rehearsal and chunking are blocked" (PubMed abstract: "about four chunks"). Baddeley's model list now includes the episodic buffer (in the 2012 paper's keywords). Tulving: "called this anoetic" became "assigned procedural skill to what he called anoetic ('non-knowing')". This ties anoetic to procedural skill, not to "meaning arriving", which in Tulving's scheme is semantic and noetic. The gloss is verbatim per the 2026-09-21 implicit-memory review's page-scan reading.

### Citation Ledger (publisher of record)
- Adam & Vogel 2017 (Confident failures, *APP* 79(5):1506-1523) — **real-correct**. Crossref and PubMed 28470554. The 28% figure and the quote were grepped verbatim in the raw abstract. Result direction: metacognition tracks performance but severely underestimates failures, as the article states.
- Baddeley 2012 (*Annu Rev Psychol* 63:1-29) — **real-correct** (Crossref).
- Cowan 2001 (*BBS* 24(1):87-114) — **real-correct** (Crossref). The unit was corrected to chunks per the PubMed abstract.
- Dreyfus 2002 (*PCS* 1(4):367-383) — **real-wrong-metadata**. The subtitle was missing. Corrected to "Intelligence without representation – Merleau-Ponty's critique of mental representation" (Crossref and PDF header). Content misreading fixed (Critical 4). Stance: anti-representationalist existential phenomenologist who models skill with neural networks; not a dualist.
- Ericsson, Krampe & Tesch-Römer 1993 (*Psych Rev* 100(3):363-406) — **real-correct** (Crossref).
- Fitts & Posner 1967 (*Human Performance*, Brooks/Cole) — **real-correct** (2026-05-31 ledger). Stage names are standard.
- Kahneman 1973 (*Attention and Effort*, Prentice-Hall) — **real-correct** (prior ledger). Body text unchanged.
- Macnamara, Hambrick & Oswald 2014 (*Psych Sci* 25(8):1608-1618) — **real-correct**. Crossref and PubMed 24986855. The five percentages and "important, but not as important as has been argued" were grepped verbatim in the raw abstract. **Note:** PubMed lists a 2018 corrigendum (*Psych Sci* 29(7):1202-1204, PMID 29733772) whose text is paywalled and was not retrieved. A Hambrick & Macnamara 2019 commentary gives the original overall r as .38, while other sources cite .35. Whether the corrigendum changes the domain percentages is unverified (see Remaining Items).
- Miller 1956 (*Psych Rev* 63(2):81-97) — **real-correct** (Crossref).
- Rademaker, Tredway & Tong 2012 (*J Vis* 12(13):21) — **real-correct**. Crossref and PubMed 23262153. The paraphrase matches "Confidence ratings strongly predicted the likelihood that the cued grating was successfully maintained".
- Rouder et al. 2008 (*PNAS* 105(16):5975-5979) — **real-correct**. PubMed 18420818. The quote was grepped verbatim in the raw abstract. Framing fixed (Critical 2).
- Sweller 1988 (*Cognitive Science* 12(2):257-285) — **real-correct** (Crossref). Framing corrected to learning.
- Tulving 1985 (*Canadian Psychology* 26(1):1-12) — **real-correct** (Crossref). **Coiner check:** *anoetic* is Stout's (1896) term, which Tulving adopted (footnote 2, p. 3, per the 2026-09-21 implicit-memory review). The article says "what he called", which makes no coinage claim, and the linked concept page carries the Stout credit. No change needed.
- Inline ↔ References: 13 inline, 13 entries, no orphans in either direction.
- Superlative sweep: `find_superlative_claims` flagged only "so far" in the new falsifier sentence, which was then rephrased to "Published studies show". No other hits.

### Reasoning-mode classification (editor-internal)
- Epiphenomenalism (L99): Mode Three on the phenomenology, because the felt doing does not discriminate. The reply then points to the Mode One self-stultification argument on the concept page. No label leakage.
- Functionalism/computationalism (L65, L137): Mode Three. The phenomenal remainder is marked at the framework boundary, and the straw man was removed.
- MWI (L143): unchanged since 09-14. Indexical bedrock; the tenet is a commitment, not read off experience.
- Dreyfus: an ally on phenomenology, not an opponent. The stance clause prevents enlisting him.

### Counterarguments Considered
- Churchland: the article now concedes introspective tracking is fallible, using Adam & Vogel. This strengthens the honest version of the access claim and is a correction, not a concession of eliminativism.
- Dennett: a metacognitive monitor captures access functionally. Granted in the Dualism paragraph ("can register that it is near capacity"). The phenomenal remainder is bedrock.
- Tegmark: the Tenet 2 paragraph is conditional and now marked as coherence only.
- Deutsch: unchanged indexical framing.
- Popper: the falsifier section now reports real data in both directions.
- Nagarjuna: the container reification is bedrock (stability note retained).

## Optimistic Analysis Summary

### Strengths Preserved
- The graded saturation sequence (competence, vigilance, density, overflow, fog) and the "shaped gap".
- The mirror-image structure of overload and withdrawal, and the hovering middle phase of automatisation.
- The 09-11 Bidirectional Interaction paragraph (P-A4 symmetry; Macnamara's domain spread) and the 09-14 indexical No Many Worlds paragraph, both kept verbatim apart from "On that reading,".
- The three concrete falsifiers. The first now has data behind it.

### Enhancements Made
- The falsifier section now carries real evidence (Rademaker 2012; Adam & Vogel 2017). The Hardline Empiricist persona would want exactly this, and it turns "privileged access" into a calibrated claim.
- Dreyfus is repositioned from foil to phenomenological ally, with verified quotes.
- The lead is now front-loaded with the article's calibrated thesis.

### Cross-links Added
- [[epiphenomenalism]] (body, L99).
- Same-page anchors in the article to its "Relation to Site Perspective" and "What Would Challenge This View" sections.

## Remaining Items
- **Macnamara 2014 corrigendum (2018)**: its contents are unverified because the text is paywalled. If it revised the domain percentages, the L139 figures need updating. Low priority. The article already says the proportion is "not settled".

## Out-of-scope findings (for the driver)
- `topics/phenomenology-of-intellectual-life` L214: "Bidirectional Interaction gains support from the causal efficacy of intellectual effort … If consciousness were epiphenomenal, the consistent motivational power of understanding experience would be inexplicable". This is the same P-A4 / fit-not-evidence defect fixed here. The hub's only open task (todo L1638) covers L192, not L214.
- `concepts/epistemic-emotions` L135: same pattern, but an open P3 already exists (todo L2446). No new mint needed.
- Archive (not edited): `archive/topics/phenomenology-of-intellectual-effort.md` L170 ("gains support from the causal efficacy of intellectual effort") and `archive/topics/phenomenology-of-cognitive-automatisation.md` L89 ("The Map interprets this as evidence for bidirectional interaction").

## Stability Notes

Earlier notes remain valid: eliminativist distrust of self-report and the Buddhist container objection are bedrock, and No Many Worlds is the weakest tenet link with indexical bedrock. New notes from this pass:
- **The access claim is now calibrated as "real but partial".** Future reviews should not restore "privileged access" or remove the Adam & Vogel counter-datum. That would reintroduce a claim the evidence partly disconfirms.
- **Dreyfus is a phenomenological ally, not a foil.** Do not reinstate a contrast implying he denied the experience of skilled coping.
- **"Fit, not evidence"** now governs the lead, the interface section, the reversal section and all five tenet paragraphs. A future pass that wants to say the phenomenology "supports" or "points to" a tenet is reopening a settled calibration.
- No number is attributed to Rouder 2008 because the full text was unverifiable. Keep "roughly four" with Cowan.
