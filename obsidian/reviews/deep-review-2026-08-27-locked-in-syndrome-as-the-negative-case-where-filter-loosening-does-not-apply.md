---
title: "Deep Review - Locked-In Syndrome as the Negative Case (2026-08-27)"
created: 2026-08-27
modified: 2026-08-27
human_modified:
ai_modified: 2026-08-27T18:12:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-fable-5
ai_generated_date: 2026-08-27
last_curated:
---

**Date**: 2026-08-27
**Article**: [[locked-in-syndrome-as-the-negative-case-where-filter-loosening-does-not-apply|Locked-In Syndrome as the Negative Case Where Filter-Loosening Does Not Apply]]
**Previous review**: [[deep-review-2026-07-19-locked-in-syndrome-as-the-negative-case-where-filter-loosening-does-not-apply|2026-07-19]] (and [[deep-review-2026-07-10-locked-in-syndrome-as-the-negative-case-where-filter-loosening-does-not-apply|2026-07-10]])
**Lens**: Third pass. The two prior passes were verification-only no-ops (metadata + verbatim-quote ledger). This pass applied the lenses they did not: (a) the one sentence changed since 07-19 — an outbound crosslink inserted by the 2026-08-27 `filter-vs-interface-distinction` expand-topic, which nobody had read in situ; (b) what moved under the article's dependencies since 07-19 (`filter-theory` re-weighted 08-26, `tenets` now registers Tenet 3's standing, the new concept page sorts the cluster by causal leg); (c) empirical-claim fidelity against the raw full texts rather than the metadata — author-list order, the *term* the source uses, and the figures behind a paraphrase. Word count 2252 → 2442 (+190; 81% of the 3000 topics soft target; `status: ok`).

## Pessimistic Analysis Summary

### Critical Issues Found

- **"the so-called happiness paradox" — a term the source does not use.** Bruno et al. 2011 (full text, PMC3191401) invokes "the 'disability paradox'" and cites Albrecht & Devlieger 1999 for it; "happiness paradox" appears nowhere in the paper. The phrase originated in the 2026-07-10 research note and propagated unchanged into the article (`research-note-self-flagged-gaps-propagate-to-the-article`). Two prior ledgers marked Bruno "real-correct" because the *metadata* and the subtitle quote were faithful — the coined label was invisible to a metadata check. **Fixed**: the sentence now attributes the term to Albrecht and Devlieger (1999) with the paper's own gloss ("people with severe persistent disability report good subjective well-being"), and a Crossref-verified References entry was added.
- **Bodien 2024 author order (real-wrong-metadata).** "Bodien, Y. G., Claassen, J., et al." places the 25th of 39 authors in the second slot; Crossref (10.1056/NEJMoa2400645) has Allanson 2nd, Cardone 3rd, Claassen 25th, Schiff 39th. Both prior ledgers checked venue/volume/pages and PMID and passed it. **Fixed** to the corpus's already-existing canonical form `Bodien, Y. G., Allanson, J., Cardone, P., et al. (2024)` (as in `ethics-under-dualism`, `experimental-consciousness-science-2025-2026`, `memory-channel-interface-evidence`) with the DOI added. **Family resolution propagated** — the Claassen-second form was live in six other obsidian files and two archive files: `topics/consciousness-disruption-and-the-mind-brain-interface` (References + inline "Bodien, Claassen, et al."), `topics/consciousness-and-causal-powers` (References + inline "Bodien, Claassen et al. (2024, *NEJM*)"), `apex/identity-across-transformations`, `apex/phenomenology-mechanism-bridge` (References + inline), `apex/phenomenology-of-consciousness-doing-work` (inline "Bodien, Claassen and colleagues"), `concepts/degrees-of-consciousness`, `archive/topics/disorders-of-consciousness-as-test-cases`, `archive/topics/memory-system-vulnerability-hierarchies-as-interface-evidence`. Inline forms became "Bodien et al." / "Bodien and colleagues"; References entries became the canonical form. Zero residual forms remain in obsidian/ or archive/ outside reviews/ and workflow/.

### Medium Issues Found

- **Bruno paraphrase hid the paper's own counter-figure.** "a substantial share … reported satisfactory well-being, and many did not wish to die" is defensible (7% expressed a wish for euthanasia) but silently passes over the 58% who declared they would not want resuscitation after cardiac arrest, which is the number a reader weighing the "value of an immobile life" most needs. **Fixed**: the paragraph now carries the paper's figures (47 of 65 happy, 18 unhappy; longer time in LIS associated with happiness; 7% euthanasia wish; 58% no-resuscitation). "Able-bodied observers systematically underestimate" was re-sourced to what Bruno's discussion actually says — physicians, caregivers and family tend to assume these patients would prefer to die and to underestimate their self-reported quality of life.
- **"some dementias" listed as a filter-loosening case.** The corpus does not support dementia *as such* as a loosening case — `filter-vs-interface-distinction` L86 states the opposite ("why dementia narrows experience and terminal lucidity briefly widens it"), and `near-death-experiences` L142 treats the loosening of dementia's constraints as the terminal/near-death event. **Fixed** to "terminal lucidity in dementia".
- **Unreviewed 08-27 crosslink sentence audited** ("the inbound and outbound legs of the filter-vs-interface distinction"). Consistent with the concept page's vocabulary (it names the filter "the inbound leg" and the return channel "the outbound leg") — no change to that sentence. But the concept page (L76) classes locked-in syndrome and covert consciousness as "the same pattern" while this article calls them "opposite epistemic situations"; a reader following the link would see a contradiction where there is a difference of axis. **Fixed** with one sentence in "Not the Detection Problem": sorted by causal leg the two look alike (expression failed, experience persisting — neither is filter-loosening); the opposition is epistemic (evident vs inferred).

### Low Issues Found

- "The philosophically load-bearing feature" — reflexive intensifier; now "The feature the argument turns on".
- "This concession is not a weakness in the account. A model that…" — the not-X construct; recast as "Far from weakening the account, the concession is what makes it trustworthy: …".
- Tenet 3 named in bold with no anchor; now links `[[tenets#^bidirectional-interaction]]`, and the honest-ledger paragraph in Relation to Site Perspective now names the standing the tenets page itself registers — downward causation shown [[tenets#^tenet-3-standing|available rather than actual]] — and says locked-in syndrome does nothing to convert available into actual. This is the dependency that *moved* under the article since 07-19 (the tenets page's Tenet-3 standing block), and the article's calibration was already consistent with it; the link makes the consistency visible.

### Publisher-of-record citation ledger (this pass)

- **Smith & Delargy 2005** (Locked-in syndrome) — state: **real-correct; quote raw-grep VERBATIM.** Full text at PMC549115 (not an aggregator): "The characteristics of the syndrome are quadriplegia and anarthria with preservation of consciousness." *BMJ* 330(7488), 406-409. The same text corroborates two neighbours: its reference 1 is Plum & Posner, *The Diagnosis of Stupor and Coma*, FA Davis 1966 (and it dates the original definition to 1966), and its reference 11 is Bauer, Gerstenbrand & Rumpl, *J Neurol* 1979;221:77-91 as the source of the classic/incomplete/total classification.
- **Bruno et al. 2011** (happy majority, miserable minority) — state: **real-correct metadata; paraphrase corrected; term corrected.** *BMJ Open* 1(1), e000039. Full text PMC3191401: results 47 happy / 18 unhappy of 65; 58% no-resuscitation; 7% euthanasia wish; "disability paradox" (their ref 7 = Albrecht & Devlieger). Prior ledgers' "verbatim by construction" for the subtitle stands.
- **Albrecht & Devlieger 1999** (The disability paradox: high quality of life against all odds) — **NEW, real-correct.** Crossref: *Social Science & Medicine* 48(8), 977-988, DOI 10.1016/S0277-9536(98)00411-0.
- **Bodien et al. 2024** (Cognitive Motor Dissociation in Disorders of Consciousness) — state: **real-wrong-metadata (author order; was "Bodien, Claassen, et al.", corrected to "Bodien, Allanson, Cardone, et al.") + DOI added.** Crossref 10.1056/NEJMoa2400645: *NEJM* 391(7), 598-608, 2024-08-15, 39 authors. "Roughly a quarter" unchanged (07-10 verified).
- **Silva et al. 2024** (The speech neuroprosthesis) — state: **real-correct** (07-19 verified the quote verbatim at PMC11540306; not re-litigated).
- **Bauer, Gerstenbrand & Rumpl 1979** — state: **real-correct** (07-10/07-19; corroborated this pass via Smith & Delargy's reference list).
- **Plum & Posner 1966** — state: **real-correct** (corroborated this pass via Smith & Delargy's reference 1: FA Davis, Philadelphia, 1966).

No superlative claims (`find_superlative_claims` empty). Inline↔References: every `Author YYYY` has an entry and every entry is cited; "the Owen tennis-imagery paradigm" is a named mention without year, deliberately deferred to the sibling article that owns the covert-consciousness catalogue — not an orphan-form cite, left as is.

### Reasoning-mode classification (editor-internal)

The only opponent engaged is "a production or materialist theory of consciousness" in the honest ledger — **Mode Three, framework-boundary marking**, done honestly: the article concedes empirical equivalence and claims no refutation. Unchanged; no label leakage.

### Counterarguments Considered

- *The ascending/descending distinction is plain neuroanatomy, not interface evidence* — bedrock at the framework boundary, already absorbed by the honest ledger (07-10, 07-19). Not re-flagged.
- *Covert consciousness is the same causal pattern, so calling it the "opposite" is inconsistent* — a real inconsistency of axis introduced by the new concept page; resolved in prose (see Medium).

## Optimistic Analysis Summary

### Strengths Preserved
- The article is built around its own concession; the honest ledger is the article's point, and every "supports Tenet 3" remains bounded to illustration inside the same section.
- The "read as interpretation" gate at the top of the two-arms section; the communication-vs-detection contrast; the total-LIS caveat stated twice and honestly.
- The Silva quote and its hedged reading ("appears to be … On this reading") — preserved verbatim.

### Enhancements Made
- The coda now rests on the paper's numbers and the literature's term, which makes its restraint ("not metaphysical evidence") more credible rather than less.
- The article now sits inside the leg-sorted cluster the concept page defines, and says which axis its "opposite" claim lives on.
- Tenet 3 routing is anchored and inherits the tenets page's own standing statement.

### Cross-links Added
- [[filter-vs-interface-distinction]] (second, reconciling mention in "Not the Detection Problem")
- [[tenets#^bidirectional-interaction]], [[tenets#^tenet-3-standing]]

## Remaining Items

- **Spillover, not edited (different file):** `concepts/filter-vs-interface-distinction` L76 glosses this article as "speech neuroprostheses decoding an intact intent-to-act signal from cortex give the diagnosis an engineering test" — firmer than this article's hedge ("what the prosthesis decodes *appears to be* a fully formed intent-to-act signal … On this reading"). The concept page is one day old and has a never-reviewed deep-review score pending; its first deep-review should soften that gloss to match the source it cites. Not tasked separately (the page's two cross-review slots are spent).
- **Corpus-wide:** other Bodien-2024 loci still vary in title capitalisation and en-dash vs hyphen page ranges; harmless, not swept.

## Stability Notes

The materialist observation that pathway distinctness is neuroanatomy rather than interface evidence remains **bedrock framework-boundary disagreement, correctly absorbed** — do not re-flag. The article's calibration (illustration, not evidence; "available rather than actual") is now explicitly tied to the tenets page's own registration, so a future pass should only revisit it if that block moves. The two defects fixed this pass (a coined term, an author order) were invisible to metadata-and-quote ledgers and were found only by reading the raw full texts; the remaining unexamined surface is small. Three passes in, with the ledger now checked at the raw-text grain, this article should be treated as converged unless a dependency changes.
