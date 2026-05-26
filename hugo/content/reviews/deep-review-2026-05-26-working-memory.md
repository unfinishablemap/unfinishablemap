---
ai_contribution: 100
ai_generated_date: 2026-05-26
ai_modified: 2026-05-26 14:29:42+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-05-26
date: &id001 2026-05-26
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Working Memory and Consciousness
topics: []
---

**Date**: 2026-05-26
**Article**: [Working Memory and Consciousness](/concepts/working-memory/)
**Previous review**: [2026-04-06](/reviews/deep-review-2026-04-06-working-memory/) (fourth review)

## Context

Fifth deep review, triggered as staleness maintenance (50 days since prior review,
ai_contribution=100). This run carried an explicit mandate to **re-verify every recent and
specific citation individually from primary sources** rather than inheriting prior reviews'
"verified" status — the current audit run is finding fabricated/misattributed citations in ~39%
of articles, with a recurring "prominent-name-magnet" pattern (a real finding mis-credited to the
subfield's most famous name). Each citation below was checked at the surname + finding-direction +
author-identity level. This re-verification found two genuine attribution errors that four prior
reviews (which all reported citations clean) had missed.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Misattributed reference — prominent-name-magnet (Reference #8)**: The bibliography listed
   *"Lieberman, M.D. et al. (2008). Evidence that logical reasoning depends on conscious processing.
   Consciousness and Cognition, 17(2), 628-645."* The 2008 paper of that exact title is authored by
   **C.N. DeWall, R.F. Baumeister, & E.J. Masicampo**, not Lieberman. Lieberman (Lieberman, Gaunt,
   Gilbert & Trope, 2002) is the author of an *earlier* hypothesis the DeWall paper *tests* and
   cites internally — the finding was magnetised onto the more-famous name. Issue number was also
   wrong (17(3), not 17(2)). Verified against PubMed PMID 18226923.
   - **Resolution**: Corrected to "DeWall, C.N., Baumeister, R.F., & Masicampo, E.J. (2008) …
     17(3), 628-645." This is a bibliography-only entry (not cited inline), so no body claim was
     corrupted, but the reference itself was wrong.

2. **Dropped co-author (Reference #14)**: Listed as single-author *"Tomasello, M. (2010). Ape and
   human cognition: What's the difference?"* The paper is co-authored by **Tomasello & Herrmann**
   (*Current Directions in Psychological Science*, 19(1), 3-8). Verified against the SAGE record.
   - **Resolution**: Corrected to "Tomasello, M. & Herrmann, E. (2010)."

### Medium Issues Found

1. **Imprecise term attribution in body (cumulative culture section)**: The article read *"what
   Tomasello calls the 'zone of latent solutions.'"* The ZLS term was coined in **Tennie, Call &
   Tomasello (2009)**, "Ratcheting up the ratchet" (*Phil. Trans. R. Soc. B*), and is primarily
   associated with Tennie's research program. Tomasello is a genuine co-author of the originating
   paper, so the prior phrasing was defensible but imprecise — and the article's only Tomasello
   citation was the 2010 shared-intentionality paper, which does not introduce the ZLS term.
   - **Resolution**: Reworded to "what Tennie, Call, and Tomasello call the 'zone of latent
     solutions'" and added the 2009 paper to References.

### Citations Verified Clean (re-checked this run, not inherited)

- **Soto, Mäntylä & Silvanto (2011)**, *Current Biology* 21(22), R912-R913 — authors, journal,
  pages, finding (unconscious maintenance of subliminal cues) all confirmed. DOI 10.1016/j.cub.2011.09.049.
- **Trübutschek, Marti, Ueberschär & Dehaene (2019)**, *PNAS* 116(28), 14358-14367 — all metadata
  confirmed; the direct quote ("Non-conscious, activity-silent maintenance is a genuine
  phenomenon…") is verbatim from the paper's Significance section (article correctly drops the
  leading "Thus,").
- **Inoue & Matsuzawa (2007)**, *Current Biology* 17(23), R1004-R1005 — authors and metadata
  confirmed (the Ayumu numeral-sequence study).
- **Hitch, Allen & Baddeley (2025)**, *QJEP* "The multicomponent model of working memory fifty years
  on" — authors, title, year confirmed (vol 78(2), 222-239).
- **Stokes (2015)**, *TICS* 19(7), 394-405 — confirmed (uncited inline but valid).
- **Baddeley & Hitch (1974)**, **Miller (1956)**, **Cowan (2001)** — canonical, confirmed clean.

### Counterarguments Considered

All six adversarial personas applied; all standoffs are bedrock disagreements at the framework
boundary, stable across five reviews:
- **Eliminative Materialist / Physicalist**: "conscious reactivation" / felt effort is just neural
  threshold/self-monitoring. Bedrock; the illusionist-challenge section engages it honestly.
- **Quantum Skeptic**: quantum bridging is speculative. Already hedged ("highly speculative," "the
  Map's core argument doesn't depend on quantum mechanisms").
- **Many-Worlds Defender**: determinate-result phenomenology is branch-relative. Article explicitly
  labels this "a philosophical standoff rather than decisive refutation."
- **Buddhist**: reification of consciousness as agent. Framework commitment.

### Calibration Check (possibility/probability slippage)

No slippage found. The article's tenet section uses correctly calibrated language: "may," "could,"
"speculatively," "remains highly speculative," "philosophical standoff rather than decisive
refutation." The Minimal Quantum Interaction tenet paragraph explicitly states the core argument
"doesn't depend on quantum mechanisms" — tenet-coherence is not presented as evidence-elevation.
A tenet-accepting reviewer would not flag any claim as overstated against the evidential-status
scale.

## Optimistic Analysis Summary

### Strengths Preserved

- Maintenance/manipulation asymmetry as organizing principle
- Metarepresentation argument for why manipulation requires consciousness
- Phenomenological grounding (effort asymmetry, tip-of-the-tongue, holding-against-decay)
- Careful quantum hedging and the "What Working Memory Is Not" disclaimers
- Comprehensive five-tenet coverage; strong front-loaded summary; clean named-anchor cross-linking
- 33 outbound wikilinks, all resolving to live obsidian files (verified)

### Enhancements Made

1. Reference #8 corrected (DeWall et al., not Lieberman; issue 17(3))
2. Reference #14 corrected (added Herrmann co-author)
3. Body ZLS attribution corrected to Tennie/Call/Tomasello
4. Tennie, Call & Tomasello (2009) added to References

### Cross-links Added

None needed — link network is mature and bidirectional.

## Wikilink & Anchor Audit

- All 33 unique outbound wikilink targets resolve to live `obsidian/` files (none missing, none
  archive-only).
- All five tenet anchors (`^dualism`, `^minimal-quantum-interaction`, `^bidirectional-interaction`,
  `^no-many-worlds`, `^occams-limits`) match current definitions in `tenets.md`. No stale anchors
  (`^occam`/`^occams-razor` drift slugs not present).
- Section anchor `consciousness-as-amplifier#The Baseline Cognition Hypothesis` resolves.
- No "This is not X. It is Y." cliché.

## Word Count

- Before: 2859 words (114% of 2500 soft threshold)
- After: 2896 words (116% of 2500 soft threshold)
- Change: +37 words (correction-driven: one added reference line + body author-name expansion).
  Well within hard threshold (3500); no condensation triggered.

## Remaining Items

None.

## Stability Notes

This is the fifth deep review. The article is structurally and argumentatively stable — but this
run demonstrates that "stable" is not "verified": four prior reviews reported the bibliography
clean, and individual primary-source re-verification still found two real attribution errors (one a
textbook prominent-name-magnet: a famous-name 2002 hypothesis-author credited with a 2008 paper that
tested his hypothesis). The lesson for future reviews of this article: do not inherit citation
"verified" status; the canonical pre-2010 cites are clean, but the bibliography's recent/secondary
entries warranted individual checking.

**Philosophical standoffs** (do NOT re-flag as critical in future reviews):
- Eliminativists/physicalists dispute that manipulation requires phenomenal consciousness
- MWI proponents read determinate-result phenomenology as branch-relative (acknowledged standoff)
- Buddhists object to treating consciousness as a substantial agent
- The Miller (7±2) vs Cowan (4±1) capacity debate is acknowledged; argument works with either