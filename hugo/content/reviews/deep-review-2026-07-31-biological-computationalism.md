---
ai_contribution: 100
ai_generated_date: 2026-07-31
ai_modified: 2026-07-31 12:02:17+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-31
date: &id001 2026-07-31
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Biological Computationalism (Unledgered-Citation Pass)
topics: []
---

**Date**: 2026-07-31
**Article**: [Biological Computationalism](/concepts/biological-computationalism/)
**Previous review**: [2026-06-25](/reviews/deep-review-2026-06-25-biological-computationalism/) (citation ledger: [2026-05-29](/reviews/deep-review-2026-05-29-biological-computationalism/))
**Mode**: Targeted publisher-of-record pass on the one citation added *after* the only ledger, plus a full six/seven-persona sweep. 8th review; body argument converged.

## Scope

The 2026-05-29 pass ledgered the whole reference apparatus. Commit `3a1f03cad` (2026-07-30, "photosynthesis-coherence over-claim") then added **reference #10 — Duan et al. (2017), PNAS** and reworded the Minimal Quantum Interaction paragraph that cites it. That citation postdated the ledger and had never been verified. This pass verified it; the pre-existing, unchanged references were not re-verified (ledgered 05-29, low-risk profile).

WebSearch budget was exhausted for the session, so verification ran through direct registrar/index APIs rather than search: **Crossref** (`api.crossref.org`, registrar of record for the DOI), **Europe PMC** core record, and the **PMC** full text. No result was sourced from an aggregator or from unfinishablemap.org.

## Citation Ledger (this pass)

- **Duan, H.-G., Prokhorenko, V. I., Cogdell, R. J., Ashraf, K., Stevens, A. L., Thorwart, M., & Miller, R. J. D. (2017), "Nature does not rely on long-lived electronic quantum coherence for photosynthetic energy transfer", *PNAS* 114(32), 8493–8498, doi:10.1073/pnas.1702261114** — state: **real-correct**. Crossref returns the title, the seven-author list *in the cited order*, PNAS, vol 114, issue 32, pages 8493–8498, DOI exact. Europe PMC corroborates (PMID 28743751, PMCID PMC5559008). Every element of the article's tuple matches; no metadata defect.

Source-conclusion check on the three claims the article attaches to it, against the verbatim abstract and the Significance statement:

- *"dephasing within roughly 60 femtoseconds"* — supported. Abstract: "confirm the orthodox view of rapidly decaying electronic quantum coherence on a timescale of 60 fs." Significance statement: "the electronic decoherence occurs within 60 fs."
- *"no hint of a biofunctional role"* — supported, but the article had **dropped the paper's own qualifier**. Abstract: "give no hint that **electronic** quantum coherence plays any biofunctional role in real photoactive biomolecular complexes." Fixed (below).
- *"the long-lived oscillations once read as electronic are now attributed to vibrational coherence"* — supported. Full text: the oscillations "are related to vibrational coherence"; their "frequencies … lifetimes, and amplitudes all match those expected for molecular modes, and not long-lived electronic coherences."

No currency-superseded superlative: the article makes no "first/largest/current-record" claim about this result.

Inline ↔ References cross-check: all inline cites (Milinkovic & Aru 2026, Thagard 2022, Putnam 1967, Searle 1980/1992, Piccinini 2015, Duch 2005/2019, Duan 2017) have entries; no orphans in either direction.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Dropped qualifier in the Duan paraphrase (attribution fidelity).** The article read "found no hint of a biofunctional role" where the paper says no hint that *electronic* quantum coherence plays such a role. The paper deliberately leaves vibrational/vibronic coherence open — it is what they attribute the oscillations to. Read standalone (or truncated, which is the LLM-first failure mode this style guide is built around), the unqualified clause asserts a broader negative than the source supports, and it is an over-correction running *against* the Map's Minimal Quantum Interaction tenet — the direction that collects ratification rather than challenge. The following sentence partially repaired it; the qualifier is now restored explicitly. **Fixed.**

**2. Over-generalised measurement scope.** "measured electronic coherence in light-harvesting complexes" (plural) described a study that measured one complex — the Fenna–Matthews–Olson protein of *Chlorobium tepidum*. The generality is the *authors'* inference ("we anticipate that this finding is general"), not their measurement. The passage now names FMO, names the technique and the conditions (two-dimensional photon echo, **ambient temperature in aqueous solution** — the detail that makes the result decisive against the earlier cryogenic long-coherence claims), and attributes the generalisation to the authors rather than asserting it. **Fixed.**

**3. Possibility/probability slippage in the Occam's Razor tenet section.** The paragraph closed by saying the qualification-cascade demonstrates "that parsimony pointed away from **the truth** about what consciousness requires." That presupposes biological computationalism is true — which the article explicitly declines to endorse three paragraphs earlier ("These are opposite positive claims"; the Map's interest is in the shared *negative* conclusion only). A reviewer who fully accepts all five tenets would still flag this: the tenet is about the unreliability of simplicity under incomplete knowledge, and it does not need — and the Map has not earned — the claim that BC's positive picture is the truth. A second, smaller error sat alongside it: the listed qualifications are a *rival* framework's commitments, not amendments functionalism itself adopted, so "the functionalist account has required ever more qualifications" mis-describes what happened. Rewritten to make the trajectory claim about the computational research programme, to state plainly that it does not settle whether BC is correct, and to land the tenet's actual point. **Fixed.**

### Medium / Low
- Reference #10 used a hyphen in the page range and a bare `doi:` prefix where the rest of the list uses en-dashes and `https://doi.org/` URLs. Normalised. Missing trailing newline at EOF restored.
- Mixed spaced/unspaced em-dash style across the article predates the 07-30 edit and is corpus-wide; **not** touched — churning it would be oscillation, not improvement.

### Counterarguments Considered
All six adversarial personas engaged. Their objections are the bedrock framework-boundary disagreements already logged across seven prior reviews (eliminative materialist: substrate dependence is "just more physics"; quantum skeptic: decoherence; whether BC genuinely differs from Searle's biological naturalism). Not re-flagged. The "just physics" section already concedes the objection's force explicitly, supplies the dualist reply, and names the crux — balanced, not an over-concession.

### Reasoning-mode classification (editor-internal)
- **Duch** — Mode Three. The passage marks an honest disagreement *between two physicalist branches* over which cost to pay, without claiming the Map refutes Duch inside his own framework. Correct as written.
- **The "just physics" functionalist** — Mode Three, with the concession stated plainly and the crux named. Correct as written.
- **Searle** — Mode One, in-framework: BC disagrees with Searle on computation's observer-relativity using computationalism's own commitments. Correct as written.
- No boundary-substitution found. No label leakage: grep for the full forbidden-vocabulary list returns zero.

## Optimistic Analysis Summary

### Strengths Preserved
Front-loaded opening; the clean three-commitment structure; the honest "just physics" treatment; the Duch foil paragraph (the sharpest thing in the article — it makes the substrate-dependence bet legible as a *bet*, with costs on both sides); the default-causal-profile bridge to Bidirectional Interaction; the clean division of labour with the companion topic article.

### Enhancements Made
The MQI passage is now more precise *and* more forceful than before: naming FMO and the ambient/aqueous conditions is what makes Duan decisive, and the article previously threw that away in favour of a vaguer plural. The Hardline Empiricist and the Process Philosopher are not in tension here — the paragraph still ends on "remains an open empirical question" and claims only compatibility, never using tenet-coherence to upgrade evidential status.

### Cross-links
No changes; 26 distinct wikilinks, all resolving.

## Remaining Items

**Sibling sweep — the dropped qualifier generalises.** The unqualified "biofunctional role" phrasing propagated from the same 07-30 sweep to four other files (plus their hugo mirrors; **zero in `archive/`**):

- `obsidian/positions/quantum-interface.md`
- `obsidian/topics/evolutionary-case-for-quantum-neural-effects.md`
- `obsidian/concepts/entanglement-binding-hypothesis.md`
- `obsidian/concepts/prospective-memory.md` — variant wording ("with no hint of a biofunctional role"), same defect

Counts per tree: obsidian 5 (incl. this article), archive 0, hugo/content 5. Not re-scoped into this task; a follow-up task is queued.

## Stability Notes

Body argument is convergent (8th review). Bedrock disagreements carried forward unchanged from prior reviews — future passes should not re-flag them:
- Eliminative materialists will always object that substrate dependence is "just more physics."
- The No-Many-Worlds connection (substrate specificity → indexical identity) is a clearly-labelled Map inference, contestable but not a defect.
- Whether biological computationalism genuinely differs from Searle's biological naturalism remains contested in the literature.

Process note. The 05-29 ledger was complete *as of 05-29*, and every later review inherited "citations verified" from it — but a citation added on 07-30 sat unchecked underneath that inherited verdict for a day, and it carried two fidelity defects. **A ledger is only a ledger for the citations that existed when it was written.** The cheap discriminator for future passes is to diff the reference block against the date of the most recent ledger rather than trusting the ledger's existence.