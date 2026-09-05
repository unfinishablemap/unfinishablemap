---
ai_contribution: 100
ai_generated_date: 2026-09-05
ai_modified: 2026-09-05 09:11:37+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-09-05
date: &id001 2026-09-05
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-05 09:11:37+00:00
modified: *id001
related_articles: []
title: Deep Review - Galilean Exclusion
topics: []
---

**Date**: 2026-09-05
**Article**: [Galilean Exclusion](/concepts/galilean-exclusion/)
**Previous review**: [2026-07-06](/reviews/deep-review-2026-07-06-galilean-exclusion/) (6th review; prior passes 2026-02-21, 2026-03-23, 2026-04-29, 2026-06-01, 2026-07-06)

## Summary

Sixth review. The article had converged over five passes; the only body change since 2026-07-06 is a paragraph on [ontic structural realism](/concepts/ontic-structural-realism/) inserted on 2026-09-04 by the `expand-topic` run that wrote that article (commit dad04f04ee). Cross-link paragraphs written into a neighbour by another article's author are never reviewed by anyone, so this pass concentrated on that paragraph. It carried a dropped qualifier (critical) and had been inserted at a point that broke an existing anaphor (medium). Both fixed. Two instances of the style guide's "This is not X. It is Y." construct were also reworded, leaving the sieve metaphor intact. Everything else remains as the 2026-07-06 review left it.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Dropped qualifier in the OSR paragraph (source/Map conflation across the cross-link).** The inserted text read "Galileo *relocates* the residue where structural realism *abolishes* it", as if ontic structural realism as held by its proponents denies that experience is a datum. The source article is explicit that this is not so: OSR "is a thesis about the ontology of physics and is nearly silent on consciousness", abolishes the residue in mind only "on the strongest reading", and the rival that does so "is a composite the Map has assembled, not a position anyone defends in print" (`concepts/ontic-structural-realism` L35–37). The neighbour's summary had flattened all of that. **Resolution**: rewritten to "Structural realism, on its strongest reading, *abolishes* it — but that reading extends a thesis about the ontology of physics to experience itself, and the extension is a separate commitment (phenomenal structuralism) rather than part of structural realism about physics." The paragraph now says the same thing as the article it links to.

### Medium Issues Found

- **Broken anaphor from the insertion point.** The paragraph had been placed between the circularity argument and "This point cuts against both extreme positions", so "this point" now appeared to refer to the OSR paragraph, whose point does not cut against materialist and mysterian. "A third position" also preceded the naming of the two positions it was third to. **Resolution**: moved the paragraph to follow "both extreme positions"; "a third position" now resolves against the materialist and mysterian just named, and "this point" again refers to the decided-not-discovered argument.
- **"On other ground" was a dead end.** The paragraph conceded that the circularity charge does not reach OSR and that the argument "has to be made on other ground" without saying where. **Resolution**: pointed to the grounds the source article actually gives — Newman's problem and the standing of phenomenal structuralism — via an anchored link to `[[ontic-structural-realism#the-choice]]` (the article uses explicit `{#id}` heading anchors; the `[[slug#id|text]]` form is the corpus convention, cf. `[[metacognition#the-metarepresentation-threshold]]`).

### Low Issues Found

- Two instances of the "This is not X. It is Y." construct flagged in the style guide's *Overused Words and Constructions*: "This is not a claim about the limits of scientific effort or intelligence. It is a claim about…" and "The gap is not merely a hard empirical problem awaiting further research. It reflects…". Reworded into single sentences carrying the same contrast. No prior review had touched either sentence, so this is not oscillation; the sieve/sand metaphor that follows the first is untouched.

### Publisher-of-Record Citation Web-Verify (this pass)

The References block is unchanged since the 2026-06-01 full web-verify and the 2026-07-06 spot re-verify (Frank/Gleiser/Thompson 2024 at MIT Press; Whitehead 1920 at CUP). The 2026-09-04 insertion added no bibliographic citation, so those seven entries are carried as **real-correct** without re-fetching: Chalmers 1996 (OUP); Frank, Gleiser & Thompson 2024 (MIT Press); Galilei 1623/1957 trans. Drake (Doubleday); Husserl 1936/1970 trans. Carr (Northwestern); Thompson 2007 (Harvard UP); Whitehead 1920 (CUP); Whitehead 1925 (Macmillan).

The insertion did add one sourced *claim* — that Galileo relocates secondary qualities into the sentient body — which the source article attributes to SEP but says it received "through publisher summaries rather than raw text". Verified this pass at the publisher of record (raw HTML fetched and grepped, not summarised):

- Bolton, M. (2022). "Primary and Secondary Qualities in Early Modern Philosophy", *Stanford Encyclopedia of Philosophy*, first published 1 June 2022, §2.2 — **real-correct**. Verbatim: the hypothesis "entails that SQs are not in bodies that cause them but internal to sentient bodies—effects of the mechanical affections of insensient bodies on the sensory organs of living bodies"; and, quoting the Assayer in Finocchiaro's translation (2008: 185), the qualities "inhere only in the sensitive body … [I]f one removes the animal, then all these qualities are … annihilated." The relocation reading is Galileo's own text, and it matches this article's existing Assayer exposition ("exists only in the person being touched"), so the paragraph was reworded to lean on that rather than on an unnamed "reading". No new References entry needed.

Currency sweep: `find_superlative_claims` returned nothing.

### Counterarguments Considered

- Eliminative materialist / hard-nosed physicalist: the decided-not-discovered argument is a genetic fallacy — how physics came to omit experience says nothing about whether experience is physical. The article already concedes exactly this ("It does not tell us that consciousness is nothing beyond physical structure" is the *only* claim it makes from the history) and now, with the OSR paragraph relocated, explicitly names the position on which the circularity charge fails. Bedrock beyond that; not re-flagged.
- Quantum skeptic / MWI defender: nothing in this article turns on quantum mechanics or on indexicality. No engagement required.
- Empiricist: the article's thesis is historical-methodological, not empirical, and it says so; its one empirical-adjacent claim (that cognitive science incorporates reports as third-person data) is uncontroversial. No unsupported factual claims found.
- Buddhist philosopher: would deny the primary/secondary distinction is anything but conventional; the article's own point that the boundary is unstable (via [primary-secondary-quality-boundary](/topics/primary-secondary-quality-boundary/)) partially absorbs this. Bedrock, per earlier reviews.

### Reasoning-Mode Check (named opponents; editor-internal)

- Materialist ("everything real is physical" resting on the exclusion): Mode Two — the materialist helps himself to a methodological omission as if it were an empirical finding. Unchanged from prior reviews; natural prose, no label leakage.
- Mysterian: Mode Three, symmetric honest boundary-marking. Unchanged.
- Ontic structural realist (new this cycle): Mode Three, now honestly marked — the paragraph says the Map's standard reply does not reach this position and hands off to where the Map's actual grounds are stated, rather than implying the circularity charge covers it. Before this pass the paragraph was honest about the limit but silent about where the argument lived.

### Calibration Audit

No evidential-status claims on the five-tier scale; the article's claims are about method and history. The Relation to Site Perspective still frames Dualism as gaining *historical context*, not evidence. No possibility/probability slippage.

## Optimistic Analysis Summary

### Strengths Preserved

- "Not a Discovery but a Decision" — the methodological-exclusion vs metaphysical-absence distinction, the article's thesis.
- The sieve/sand metaphor (lead sentences reworded; the metaphor itself verbatim).
- The conclusion cutting against both materialism and mysterianism — now sharpened by the OSR paragraph sitting directly after it as the one position the argument does not reach.
- The Galileo → Descartes → Husserl → Whitehead arc.

### Enhancements Made

- The OSR paragraph now carries its own source article's qualifications, so a reader who follows the link finds the same position described on both sides.
- The paragraph's concession ("has to be made on other ground") now names the ground and links to it, converting a dangling admission into a navigable one.

### Cross-links Added

- [ontic-structural-realism](/concepts/ontic-structural-realism/#the-choice) (anchored; the bare `[[ontic-structural-realism]]` link was already present from the 2026-09-04 insertion).

## Length Check

1903 → 1948 words by `tools.curate.length` (concepts soft 2500 / hard 3500). Below soft threshold; normal mode. The +45 is the qualifier and the pointer; the two style rewordings were net-negative.

## Remaining Items

None.

## Stability Notes

Durable convergence across six reviews. The one live source of drift for this article is now identified: neighbouring `expand-topic` runs writing cross-link paragraphs into it. Future reviews should diff against the last review commit first and read any inserted paragraph against the article it links to — that is where this cycle's only critical issue came from. Adversarial-persona disagreements (eliminative materialist, MWI defender, Buddhist on conventional distinctions) remain bedrock framework-boundary disagreements; do not re-flag. The OSR engagement is deliberately Mode Three with a hand-off; do not try to refute OSR inside this article — that argument belongs in `concepts/ontic-structural-realism`, which owns Newman's problem and phenomenal structuralism.