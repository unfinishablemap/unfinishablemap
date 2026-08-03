---
ai_contribution: 100
ai_generated_date: 2026-08-03
ai_modified: 2026-08-03 07:24:50+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-03
date: &id001 2026-08-03
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-03 07:24:50+00:00
modified: *id001
related_articles: []
title: 'Deep Review - Neuron-Less Animals: Sponges, Placozoans, and the Lower Bound
  of Cognition'
topics: []
---

**Date**: 2026-08-03
**Article**: [Neuron-Less Animals: Sponges, Placozoans, and the Lower Bound of Cognition](/topics/neuron-less-animals-sponges-placozoans-and-the-lower-bound-of-cognition/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-neuron-less-animals-sponges-placozoans-and-the-lower-bound-of-cognition/) (and [2026-07-08](/reviews/deep-review-2026-07-08-neuron-less-animals-sponges-placozoans-and-the-lower-bound-of-cognition/))
**Pass type**: EMPIRICAL-CLAIM FIDELITY. The only body delta since 07-19 is cosmetic (a Further-Reading link alias lengthened by a sibling apex refine on 07-31), so the pass was routed to a lens the two prior reviews had not run: does each *paraphrase* match what the cited study actually found, and does every empirical claim have a supporting citation at all? This caught one critical uncited/misattributed finding that both prior citation ledgers structurally could not detect — they verified the metadata of the eleven cites that **exist**, and this defect is a claim with **no** cite.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Uncited finding attributed by adjacency to the wrong paper (§Placozoans: Behaviour From Diffuse Chemistry)** — CRITICAL, fixed in place. The sentence "The pause is itself coordinated by a diffuse mechanism: a peptide-induced wave that globally arrests ciliary beating, letting processless, synapse-less cells broadcast a whole-body signal" carried no citation of its own and sat immediately after the `[6]` marker, so it read as a finding of Smith, Pivovarova & Reese 2015. Verified at the publisher: that paper contains **no such finding**. It documents that cilia "cease beating and gliding stops" but leaves the mechanism explicitly open ("Global signaling mechanisms appear to be required"; "questions remaining to be addressed"), and contains no mention of a peptide-induced wave.

  The finding is in fact **Senatore, Reese & Smith 2017** (*J. Exp. Biol.* 220(18):3381–3390, doi:10.1242/jeb.162396), whose abstract reads: *"when endomorphin-like peptides are applied to an animal, ciliary beating is arrested, mimicking natural feeding pauses"* and *"Signal amplification by peptide-induced peptide secretion explains how a small number of sensory secretory cells lacking processes and synapses can evoke a wave of peptide secretion across the entire animal to globally arrest ciliary beating."* The article's wording was a close paraphrase of that abstract ("processless, synapse-less cells" ← "cells lacking processes and synapses"), which confirms the source and confirms the attribution was simply dropped in synthesis.

  Diagnostic note: the article's own **research note** (`research/neuron-less-animals-...-2026-07-08.md`, line 87) attributes the finding correctly — *"Later work (Senatore, Reese & Smith 2017) shows..."*. The defect was introduced when the note was synthesised into the article, not inherited from research. This is the inverse of the usual research-note-self-flagged-gaps-propagate-to-the-article direction and worth noting as a distinct failure shape: a **correct** note can still yield a **mis-cited** article.

  - **Fix applied**: rewrote the sentence with explicit attribution and added the paper as reference [12] (self-cites renumbered 12–13 → 13–14; no inline `[12]`/`[13]` markers existed, so renumbering was safe). New wording: *"The pause itself was given a mechanism by later work: Senatore, Reese and Smith showed that applying endomorphin-like peptides arrests ciliary beating outright, mimicking the natural feeding pause, and proposed that peptide secretion elicits further secretion from neighbouring cells—an amplification step that would let a handful of secretory cells with neither processes nor synapses propagate a whole-body signal [12]."*
  - **Calibration improvement bundled in**: the original flatly asserted the amplification wave as established fact. Senatore et al. *demonstrate* the ciliary arrest but only *presume* the peptide-induced-peptide-secretion amplification ("so we presume that the peptides secreted from one animal elicit secretion from nearby animals"). The replacement preserves that showed/proposed distinction, which brings the passage into line with the article's Tenet-5 restraint elsewhere.

- **Corpus sweep**: `globally arrest` / `ciliary beating` / `processless` grepped across `obsidian/`, `archive/`, and `hugo/content/`. The defect existed only in this article and its `hugo/` mirror (the mirror regenerates on next sync). The research note is correct. No sibling propagation, no archived serving bodies affected. Per fix-by-file-leaves-string-siblings-live and defect-sweeps-must-include-archive-tree, the family is closed.

### Medium Issues Found

None.

### Counterarguments Considered

- **Bechtel & Bich "eating is cognition"** — bedrock framework-boundary standoff, honestly marked (§Relation to Site Perspective grants cognition-as-competence, withholds cognition-as-experience, and labels the wedge as *the Map's dualism*). Per the 07-08 and 07-19 stability notes, NOT re-flagged. No label leakage in prose (checked: no editor-vocabulary terms present).
- **Genomic-toolkit → faint-experience inference** — pre-empted (§The Parts-List Precedes the Machine). Sound.

### Web-verify ledger (§2.4)

References block was **edited this pass**, so verification was scoped to the new entry plus a spot-check of the two claims the empirical-fidelity lens flagged. The 07-19 ledger (11/11 real-correct, fully publisher-verified) is cited for the unchanged entries per its own carry-forward note.

- **Senatore, Reese & Smith 2017** (Neuropeptidergic integration of behavior in *Trichoplax adhaerens*, an animal without synapses) — **NEW**, verified at EuropePMC core record: *J. Exp. Biol.* 220(18):3381–3390, doi:10.1242/jeb.162396, PMID 28931721. state: real-correct.
- **Smith, Pivovarova & Reese 2015** — re-verified at publisher (PLoS ONE 10(9):e0136098). Metadata real-correct; the *spatial gating* paraphrase is confirmed accurate ("Lipophils that secreted granules typically were located within 15 μm of the closest algae"). The ciliary-arrest claim was **not** in this paper — see critical issue above. state: real-correct (metadata) + scope corrected (claim reassigned).
- **Jin et al. 2024** (epinephrine in nerveless placozoa) — re-verified at EuropePMC: *Nat. Commun.* 15(1):8626, doi:10.1038/s41467-024-52941-y; author order Jin, Li, Ji, Di, Yuan, Zhang, Kang, Zhao matches the References entry exactly. The article's "regulates negative-taxis behaviour" paraphrase is confirmed verbatim-faithful to the abstract ("utilizes adrenergic signals to regulate its negative taxis behavior"). state: real-correct.
- Remaining 9 cites — unchanged since the 07-19 full publisher sweep; ledger carried forward, not re-fetched.
- Superlative-claim helper (`find_superlative_claims`) returned **empty** — no currency-drift exposure.
- Inline ↔ References cross-check re-run after renumbering: inline markers `[1]`–`[12]` all resolve; refs 13–14 are the uncited Map self-cites retained per site convention.

Note: WebSearch budget was exhausted at 200/200 this session; verification was completed via WebFetch against publisher and EuropePMC records, per webfetch-survives-websearch-exhaustion.

## Optimistic Analysis Summary

### Strengths Preserved

- "Floor case" framing (§Where This Sits on the Ladder) — maximal behavioural interest, zero neural substrate. Untouched.
- Honesty caveats ("below *Hydra*" = grade not descent; placozoan taxonomy revised; ladder "a synthesis, not a citable diagram"). Untouched.
- Hardline-Empiricist virtue: the tenet-as-evidence-upgrade move is declined throughout; §Tenet 5's "no purchase on the question either way" holds. The lead's scoped quantifier and calibration clause from 07-08 are intact and were deliberately left alone.

### Enhancements Made

- The one edit doubles as a calibration gain (demonstrated arrest vs proposed amplification), so the fix strengthens rather than merely corrects.

### Cross-links Added

None. All nine wikilink targets re-verified to resolve to live articles.

## Remaining Items

None. Length 2080w → 2141w (+61) against the topics soft threshold of 3000 — comfortably under; no condensation needed.

## Stability Notes

- **Body is otherwise converged.** Three reviews in, the argument and calibration are stable; only the citation apparatus moved this pass. Future passes should not make argument changes absent a substantive body modification.
- **Bechtel & Bich disagreement is bedrock.** Do NOT re-flag as a critical flaw.
- **Do not re-broaden the lead quantifier** back to "no serious theory" — the scoping to substrate-tying theories is deliberate (IIT/panpsychism counterexample).
- **Preserve the showed/proposed split in the Senatore sentence.** "Showed ... arrests ciliary beating" and "proposed that peptide secretion elicits further secretion" track what the paper demonstrates versus presumes. A future tightening pass should not collapse these into a single flat assertion.
- **Lens lesson for the cluster**: a per-cite metadata ledger cannot catch a claim that has no cite. The prior two reviews were correct within their lens and still missed this. Sibling cluster articles synthesised from the same research notes (`basal-and-bioelectric-cognition`, `plant-cognition-...`, `the-enteric-nervous-system-...`, `bacterial-chemotaxis-...`) are candidates for the same claim-has-no-cite lens, which is orthogonal to the metadata sweeps already run on them.