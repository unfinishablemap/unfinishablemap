---
title: "Deep Review - Interface Friction"
created: 2026-11-19
modified: 2026-11-19
human_modified: null
ai_modified: 2026-11-19T18:44:24+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-19
last_curated: null
---

**Date**: 2026-11-19
**Article**: [[interface-friction|Interface Friction]]
**Previous review**: [[deep-review-2026-07-17-interface-friction|2026-07-17]] (8th deep review overall; prior passes 2026-02-20, 2026-03-19, 2026-04-16, 2026-04-17, 2026-05-28, 2026-06-25, 2026-07-17)

## Context

Driver-selected (score 80; 124 days since the last review). Since 07-17 the page has had four edits from other tasks that no deep review has seen:

- `6b4ab9fbc8` (2026-09-10): bandwidth paragraph re-sourced. 10⁹ bits/s moved to Zheng & Meister, and the ~11 million bits/s figure given to Zimmermann/Nørretranders.
- `70d6362ca3` (2026-09-18): `[[evidential-status-discipline]]` link added in the choking paragraph.
- `cf46c33c69` (2026-10-14): Tegmark scope added ("10⁻²⁰ seconds for ion superpositions").
- `d532895034` (2026-11-03): Zeno timing recast, adding Hagan scoping, the Stapp/Georgiev crux and the 3,000-event figure.

Two lines were fenced for open tasks and were not edited: L78 (todo P3 on Gröpel & Mesagno) and L114 (the `topics/dualism-channel-width-axis` rider). Findings on them are under "Fenced lines" below.

All prior fixes are still in place: the twelve-order gap with its "(~10⁻¹ s)" anchor, Zheng & Meister (2025), the six-domain list, and the interpretive-not-predictive framing in the lead, Pathological Friction and choking paragraphs.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Stale propagation from the resistance page (L44).**
   - **Defect.** The page said each of the six resistance domains "exhibits the same structure—directedness-against-constraint, graded yielding, sustained temporality". That sentence was written 2026-04-16 21:44 (`ed7a3a06c4`) from the source page's wording at the time. `topics/phenomenology-of-resistance-across-domains` withdrew it seven hours later (`bebc7db41e`, 2026-04-17 04:13). Its L87–93 now read: "One feature recurs across all six; two further features recur robustly across a narrower group but do not generalise cleanly". Graded yielding and temporality hold "in four domains—physical, material, moral, epistemic".
   - **Why four reviews missed it.** The 04-17, 05-28, 06-25 and 07-17 passes checked the domain *list* against the source, which was correct. None checked the shared-*structure* clause.
   - **Fix.** OLD "Each exhibits the same structure—directedness-against-constraint, graded yielding, sustained temporality—with different objects." → NEW "All six share directedness meeting constraint; graded yielding and sustained temporal structure recur in four of them but not in logical or imaginative resistance."

2. **Carhart-Harris et al. 2012: misread result, author stance missing, and a "distinctive" prediction that the cited result does not separate from rival models (L108).**
   - **The gloss is not in the source.** The page said "default-mode network suppression correlates with reports of enriched phenomenology". "Enriched" and "expanded" have 0 hits in the raw PubMed/PMC abstract (nonsense control 0). The paper reports that the size of the decrease in ACC/mPFC activity "predicted the intensity of the subjective effects". That is intensity, not enrichment. The gloss came in with the 02-20 pass, which attached the citation to a sentence that had no source until then; no review had checked the paraphrase against the paper.
   - **The authors' own stance (§2.4 step 8).** They explain the result neurally: the subjective effects "are caused by decreased activity and connectivity in the brain's key connector hubs, enabling a state of unconstrained cognition" (grep count 1 in the PMC record). A production account therefore accommodates the same result, so calling the filter model's prediction "distinctive" was a calibration error. It also sat badly with the lead's statement that the framework "does not generate empirically distinguishable predictions beyond standard models".
   - **Fix.** OLD "The filter model also generates a distinctive prediction: … Psychedelic research is suggestive here—default-mode network suppression correlates with reports of enriched phenomenology (Carhart-Harris et al. 2012)—but the evidence is mixed: psychedelics also impair task performance" → NEW "The filter model also makes a prediction: … Psychedelic research is consistent with it but does not discriminate between the models: in Carhart-Harris et al. (2012) the size of psilocybin's reduction in anterior cingulate/medial prefrontal activity, a default-mode hub, predicted the intensity of the subjective effects, yet the authors explain those effects neurally, as "caused by decreased activity and connectivity in the brain's key connector hubs". The evidence is also mixed: psychedelics impair task performance".
   - **Scope.** The "mixed evidence" and aperture/precision structure that earlier reviews told future passes not to oscillate on is kept. This fix concerns source fidelity and the author's stance, not the balance of the evidence.

### Medium Issues Found

- **Flat assertions of the Map's model as fact (brief focus 2).** Four sentences stated the friction reading as if it were established:
  - L72, Attentional Cost, which has no section-level interpretive frame: "reflects genuine work at the interface" → "would, on this model, reflect genuine work at the interface".
  - L76: "Attention is a scarce resource because the interface channel is narrow" → "On that framing, attention is scarce because the interface channel is narrow".
  - L86: "These low-friction pathways suggest well-worn interface channels" → "These low-friction pathways would correspond to well-worn interface channels".
  - L90: "Learning a new motor skill is effortful precisely because the interface channel for that particular pattern has not been established." → "On the friction reading, learning a new motor skill is effortful because the interface channel for that particular pattern has not yet been established."

  None of these is a possibility/probability upgrade. They are unlabelled Map inferences of the kind the lead disclaims.
- **Tegmark scope (L58).** "10⁻²⁰ seconds for ion superpositions" → "10⁻²⁰ seconds for a neuron poised between firing and not firing (some 10⁶ sodium ions in superposition)". In the arXiv full text the figure is for "a superposition of firing and not firing" in which "N ∼ 10⁶ Na+ ions are in a superposition of being inside and outside the cell" (1 hit). Eq. 10 scales as 1/N, so the bare "ion superpositions" (introduced by the 10-14 sweep `cf46c33c69`) invites a single-ion reading the source does not support.
- **Named-author attribution with no trace on the page (L60).** "Stapp argues … which Georgiev disputes" had no years and no References entries; the only Stapp entry is the 2007 book, which is not the source of the claim. Changed to "Stapp (2000) argues … which Georgiev (2015) disputes" and added both References entries (verified below).

### §2.4 Publisher-of-Record Ledger

All sources were fetched by curl. Text was whitespace-collapsed before grep, and each grep was paired with the nonsense control `qzxv-nonsense` (0 hits in every source).

- **Zheng & Meister 2025** (*Neuron* 113(2):192–204) — **real-correct**.
  - Crossref: Neuron 113(2) 192–204, issued 2025-01.
  - arXiv 2408.10234 full text: "The population of 6 million cones in one eye has a capacity of about 1.6 gigabits/s" (1 hit); "our sensory systems gather data at ∼ 10⁹ bits/s" (abstract); "10 bits/s" (22 hits).
  - The 10⁹ and 1.6 Gb/s claims on L52 are faithful.
  - "Seven orders of magnitude" was left alone deliberately: the 09-10 sweep recorded it as the conservative end of the page's 10–50 bit/s range (10⁹ ÷ 50 ≈ 10⁷·³). Not re-litigated.
- **Zimmermann 1986** — **real-correct**. Crossref: "Neurophysiology of Sensory Systems", *Fundamentals of Sensory Physiology*, pp. 68–116, 1986, DOI 10.1007/978-3-642-82598-9_3. The ~11 million bits/s figure follows the 09-10 sweep's upstream verification. The chapter's full text is not online.
- **Nørretranders 1998** (*The User Illusion*, Viking) — **real-correct**. Open Library lists the 1998 English edition.
- **Tegmark 2000** (*Phys. Rev. E* 61, 4194–4206) — **real-correct**.
  - Crossref: PRE 61(4) 4194–4206.
  - arXiv quant-ph/9907009 full text: "decoherence timescales (∼ 10−13 − 10−20 seconds) … dynamical timescales (∼ 10−3 − 10−1 seconds)".
  - The 10⁻²⁰ s figure is for "a superposition of a firing and non-firing neuron" with N ∼ 10⁶ Na⁺ ions displaced (Eq. 10, ion–ion collisions, τ ∝ 1/N). L58 was rescoped to match (Medium issue).
- **Hagan, Hameroff & Tuszyński 2002** (*PRE* 65, 061901) — **real-correct**. PubMed 12188753: Tegmark's 10⁻¹³ s lengthens to "10(-5)-10(-4) s", which is 8–9 orders, so "eight or more orders" is faithful and correctly scoped to microtubules. The 3,000-event figure checks: 0.3 s ÷ 10⁻⁴ s = 3,000.
- **Stapp 2000** (arXiv quant-ph/0010029, "The importance of quantum decoherence in brain processes") — **real-correct; new entry**. Full text: "the Quantum Zeno Effect described above is not destroyed by the fact that S(t)b is a mixture: that makes no difference at all" (1 hit). This supports L60's "works on the decohered mixture and need not outpace decoherence".
- **Georgiev 2015** (*IJMPB* 29(7), 1550039) — **real-correct; new entry**. Crossref confirms the metadata. The OpenAlex abstract says Stapp held "the efficacy of such mental efforts would not be undermined by environmental decoherence" and that "the quantum Zeno effect breaks down for timescales greater than the brain decoherence time … Stapp's model is physically implausible". "Georgiev disputes" is faithful.
- **Schwartz, Stapp & Beauregard 2005** (*Phil. Trans. R. Soc. B* 360(1458) 1309–1327) — **real-correct** (PubMed 16147524).
- **Stapp 2007** (*Mindful Universe*, Springer) — **real-correct**. Crossref: 2007, Springer Berlin Heidelberg, DOI 10.1007/978-3-540-72414-8.
- **Carhart-Harris et al. 2012** (*PNAS* 109(6) 2138–2143) — **real-correct metadata; paraphrase corrected** (see Critical 2). PubMed 22308440. The PMC record (3277566) has no body, so the abstract and keywords are the raw source; keywords include "default mode network".
- **Beilock & Carr 2001** (*JEP: General* 130(4) 701–725) — **real-correct**. PubMed 11757876: "These findings support explicit monitoring theories of choking and … that attending to proceduralized skills hurts performance". "Conscious self-monitoring degrades automatised skill" is faithful at the abstract's strength.
- **Gröpel & Mesagno 2019** (*IRSEP* 12(1) 176–201) — **real-correct metadata**. Crossref issued 2019-01; OpenAlex abstract reconstructed. Fenced line: see below.
- **Smoulder et al. 2024** (*Neuron* 112(20) 3424–3433.e8) — **real-correct metadata**. PubMed 39270654; authors Smoulder, Marino, Oby and others. Fenced line: see below.

Cross-references: every inline cite has a References entry and every entry is cited inline. The superlative scan (`find_superlative_claims`) returned nothing.

### Links, anchors, Map-internal quotations

- All 31 outbound wikilink targets resolve, with no ambiguous stems. The five `tenets#^…` block anchors are present. The in-page `{#pathological-friction}` is present.
- There are no Map-internal quotations. The four quoted strings are illustrative or scare quotes: "bits per second", "Reach for the cup", "fire motor neuron N₄₅₆₇₈", "why".
- The page neither links nor quotes `concepts/quantum-consciousness` or `concepts/quantum-biology-and-neural-mechanisms`, both edited today, so nothing was stranded.
- Paraphrase checks:
  - L60 matches `topics/motor-control-quantum-zeno` L115 (Hagan scope, Stapp/Georgiev crux, 3,000 to 30,000 events, "a rate no concrete model accounts for").
  - The `[[decoherence|itself contested]]` link matches decoherence L101/L105/L167.
  - "Quantum biology demonstrates that warm biological systems *can* exploit quantum effects" is a possibility claim. It is consistent with decoherence L141 ("establishes possibility, not actuality") and with the quantum-biology page's lead ("indicates … harness"), since enzyme tunnelling is established. Kept.
  - The causal-interface void gloss matches the void's lead. The skill-acquisition arc and the habit gloss in Further Reading match their pages.

### Fenced lines (findings only, not edited)

- **L78, Gröpel & Mesagno.**
  - "47" is verified (1 hit).
  - "confirm" and "support" have 0 hits. The abstract's grade is "the results indicate that, in general, choking interventions based on both choking models and on acclimatisation provide a benefit to performance under pressure".
  - The review classifies interventions under the two models. It does not test the split, and its third, acclimatisation, group falls outside it. "Confirmed" overstates.
- **L78, Smoulder et al. 2024 (new finding for the same task).**
  - The citation is attached to "where conscious self-monitoring degrades automatised skill". Smoulder's mechanism is reward-driven: rhesus monkeys facing a "jackpot", in which "increases in reward drive neural activity during movement preparation into, and then past, a zone of optimal performance".
  - That is the "incentive-driven over-arousal of preparatory states" model which the same paragraph later names correctly. It is not evidence about self-monitoring, and it comes from monkeys.
  - Suggested scope for the task: something like "and a motor-cortical substrate for reward-driven choking in monkeys reported by Smoulder et al. 2024".
- **L114, Minimal Quantum Interaction paragraph.** The rider sentence "The interface is narrow precisely because the tenet demands minimal intervention" has two faults:
  - It explains a structural fact by a tenet's demand.
  - It reads minimality as channel width. Tenets L69 defines minimality as empirical-constraint minimality: no *detectable* energy injection or Born deviation, a bound on detectability, not on width.
  - The same conflation runs through the whole paragraph: "The minimality of the interaction *produces* friction", "A larger interaction—more energy, …", where "more energy" presumes the minimal interaction carries some energy, which the rules-out clause forbids at detectable levels; and "Friction is the price of minimality", which earlier reviews praised as a strength. The bandwidth limit on L52 is behavioural throughput (Zheng & Meister) and is not derived from MQI.
  - A one-sentence rider that fixes only L114's third sentence would leave the paragraph's first and last sentences in tension with tenets L69. The rider task should consider recasting the paragraph, for example: "Minimality bounds what the interaction can do undetected; if it is that constrained, friction is part of its price".

### Counterarguments Considered

All six adversarial personas were re-run against the delta. No new framework-boundary objections arose.

- **Quantum Skeptic.** The Zeno timing recast (11-03) is now honest on both horns, so nothing further is owed.
- **Popperian.** The filter-model "distinctive prediction" was the one point where the empiricist's objection was a calibration error inside the framework, not bedrock, and it is fixed (Critical 2).
- **Reasoning modes (§2.6).** No extended reply to a named opponent. The generic physicalist engagement stays Mode Three with a Mode Two seed. Carhart-Harris is now cited with his own stance rather than enlisted. No editor vocabulary leaks into the prose.

## Optimistic Analysis Summary

### Strengths Preserved

- The four-source taxonomy and the lead's explicit "interpretive, not predictive" caveat. The Pathological Friction section stays a model of restraint.
- The 11-03 Zeno passage. It states the Stapp/Georgiev crux and the "if it must" arithmetic compactly and matches its parent page exactly.
- The aperture/precision reading of the mixed psychedelic evidence, kept verbatim.
- The choking paragraph's interpretive-fit framing (fenced; untouched).

### Enhancements Made

- Brought the resistance cross-reference into line with its source (Critical 1).
- Made the psychedelic citation faithful and calibrated (Critical 2).
- Labelled four Map inferences as the Map's, and rescoped Tegmark's 10⁻²⁰ s figure to its source.
- Made the Stapp (2000) and Georgiev (2015) attributions traceable on the page.

### Cross-links Added

None. The existing links all resolve and no gap justified new ones at this length.

## Length

- Before: 2,569 (concepts soft 2,500 / hard 3,500; gate `>=`).
- After: 2,684 (+115; still `soft_warning`, 816 below hard).
- Within the brief's ≤ +150 cap. Two trims to this pass's own additions recovered 17 words.

## Remaining Items (reported to the driver; no tasks minted)

- The L78 findings above go to the open P3 on Gröpel & Mesagno (heading begins "Two siblings carry the citation misreadings"): grade "confirmed" down, and rescope Smoulder.
- The L114 finding goes to the `topics/dualism-channel-width-axis` P3 rider: consider the whole paragraph, not just the one sentence.
- Lead for other pages, not checked here: `topics/motor-control-quantum-zeno` L115 puts Tegmark's 10⁻²⁰ s at "the ion-channel scale at which Schwartz, Stapp and Beauregard (2005) locate the quantum uncertainty", a single-ion site. Tegmark's figure is for ~10⁶ ions and scales as 1/N. Before treating this as a defect, confirm with Eq. 10–13 what a single-ion estimate would be. The same concern applies to the ~20 pages the 10-14 sweep gave the bare "ion superpositions" wording.
- The description field (190 characters) states the channel's constraints without the interpretive caveat. This is low priority and was left alone.

## Stability Notes

- **Settled; do not reopen.**
  - The twelve-order decoherence gap.
  - Zheng & Meister (2025).
  - "Seven orders of magnitude" as the conservative end of 10–50 bit/s (09-10 sweep rationale).
  - The balanced psychedelic structure (mixed evidence plus aperture/precision).
  - The interpretive-not-predictive framing.
  - The quantum-Zeno rate tension and its sub-personal resolution.
  - Physicalist "mere redescription" objections are bedrock.
- **New: resistance-page sync covers features as well as the list.** When checking L44 against `topics/phenomenology-of-resistance-across-domains`, verify the *shared-feature* claim as well as the domain enumeration. Only directedness-meeting-constraint is universal. Graded yielding and temporality hold in four of the six.
- **New: Carhart-Harris 2012 reports intensity, not enrichment, and its authors read the result neurally.** Do not restore "enriched phenomenology", and do not call the filter prediction "distinctive" on the strength of this paper.
- **Reference ledger.** The References block is web-verified through 2026-11-19, including the two new entries (Stapp 2000, Georgiev 2015).
