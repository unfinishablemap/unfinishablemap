---
ai_contribution: 100
ai_generated_date: 2026-07-11
ai_modified: 2026-07-11 17:23:45+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-11
date: &id001 2026-07-11
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Binding Problem (concept)
topics: []
---

**Date**: 2026-07-11
**Article**: [The Binding Problem](/concepts/binding-problem/) (concepts/binding-problem.md — the general binding problem; NOT the topics/the-binding-problem five-varieties article)
**Previous review**: [2026-05-16](/reviews/deep-review-2026-05-16-binding-problem/)

## Context

CYCLE-SLOT owed-web-verify pass. This is the concepts/binding-problem article. Its prior
reviews (through 2026-05-16) ran **intra-corpus attribution checks only** — no
publisher-of-record web-verify ledger existed. The reference list has also churned since the
last review of this article (the 2026-06-05 refine swapped the split-brain cite Pinto→Santander
and the microtubule cite Wiest→Khan), so the §2.4 web-verify trigger fires cleanly. All inline
`Author YYYY` cites and every References entry were verified at the publisher of record.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Wimmer et al. 2015 (Cell Reports) — CITATION CONFLATION → FIXED.** The reference
  *"Wimmer, R. D., Schmitt, L. I., … Halassa, M. M. (2015). Consciousness depends on integration
  between parietal cortex, striatum and thalamus. Cell Reports, 10(8), 1-12"* is a Frankenstein:
  the **title and the body's supported claim** belong to a *different* paper —
  **Afrasiabi, M., Redinbaugh, M. J., Phillips, J. M., Kambi, N. A., Mohanta, S., Raz, A.,
  Haun, A. M., & Saalmann, Y. B. (2021). Consciousness depends on integration between parietal
  cortex, striatum, and thalamus. *Cell Systems*, 12(4), 363-373, doi:10.1016/j.cels.2021.02.003.**
  The real Wimmer et al. 2015 is *"Thalamic control of sensory selection in divided attention"*,
  **Nature** 526:705-709 (PubMed 26503050) — a mouse optogenetic attention study that says
  nothing about consciousness or parietal/striatal contribution. The article grafted Wimmer's
  author list + a placeholder "Cell Reports 10(8), 1-12" locator onto Afrasiabi's title and
  finding. Classic real-paper-wrong-metadata (NOT fabrication — the claim and a real source
  exist). **Fixed**: reference corrected to Afrasiabi et al. 2021 Cell Systems.
  - **Body knock-on (line 160) — FIXED.** Old prose read *"Optogenetic studies (Wimmer et al.,
    2015) confirm that thalamic disruption prevents information from reaching the global
    workspace, and that parietal cortex, striatum, and thalamus contribute more than frontal
    cortex to consciousness states."* Afrasiabi 2021 is **not optogenetic** — it is electrode/LFP
    recording plus **electrical thalamic microstimulation in macaques** — and did not frame its
    result in global-workspace terms. Rewrote to: *"Recording and microstimulation studies in
    macaques (Afrasiabi et al., 2021) found that parietal cortex, striatum, and thalamus
    contribute more than frontal cortex to conscious states, and that stimulating the thalamus
    can rouse an animal from anaesthesia—consistent with the thalamus serving as a hub whose
    disruption withdraws consciousness."* Method, species, and framing now match the source.

- **Santander et al. 2025 — mis-attributed sub-clause → FIXED (medium/attribution).** Line 113
  bundled *"and perceptual binding divides while response unity persists"* under the Santander
  citation. Santander et al. 2025 (PNAS) found the *opposite* for partial-callosotomy patients —
  preserved interhemispheric integration and **no** disconnection syndrome; the "split
  perception / unified response" datum is the classic Pinto-type finding (the cite Santander
  *replaced*). Removed the grafted clause; line now reads *"…can sustain full interhemispheric
  integration, with no behavioural signs of a disconnection syndrome"*, which is faithful to
  Santander and coheres with the following sentence's "unity is more resilient than classical
  theories predict."

### Publisher-of-Record Citation Ledger (§2.4)

Every inline cite and References entry verified at the publisher of record this pass:

- Afrasiabi et al. 2021 (Consciousness depends on integration…) — **real-wrong-metadata**
  (was "Wimmer et al. 2015, Cell Reports, 10(8) 1-12"; corrected to Afrasiabi et al. 2021,
  Cell Systems 12(4):363-373, doi:10.1016/j.cels.2021.02.003). Verified PubMed 33730543.
- Santander, T., et al. 2025 (Full interhemispheric integration…) — **real-correct** (PNAS
  122(43) e2520190122, doi:10.1073/pnas.2520190122; first author Tyler Santander; body "1 cm of
  intact posterior callosal fibres" matches "only 1 cm of the splenium intact"). Grafted
  sub-clause removed (see above).
- Khan, S., … Wiest, M. C. et al. 2024 (Epothilone B delays anesthetic unconsciousness) —
  **real-correct** (eNeuro 11(8) ENEURO.0291-24.2024, doi:10.1523/ENEURO.0291-24.2024).
  **Cohen's d = 1.9 verified verbatim** at PMC11363512 ("standardized mean difference (Cohen's
  d) of 1.9… 'large'"; n = 8 male Long-Evans rats). Body stat is faithful.
- Kerskens, C. M. & López Pérez, D. 2022 (Experimental indications of non-classical brain
  functions) — **real-correct** (J. Phys. Commun. 6, 105001, doi:10.1088/2399-6528/ac94be).
- Warren, W. S. 2023 (Comment on…) — **real-correct** (J. Phys. Commun. 7(3), 038001;
  Kerskens' reply is the adjacent 038002). Locator faithful.
- Baum, E. 2024 (The Quantum Binding Argument: How 40Hz Gamma Synchrony Requires Quantum
  Non-Locality) — **real-correct**, PhilArchive preprint (Erik Baum); correctly flagged in body
  as a non-peer-reviewed preprint. Title/author match.
- Tegmark 2000 (Phys Rev E 61:4194), Hagan et al. 2002 (Phys Rev E 65:061901), Reimers et al.
  2009 (PNAS 106(11):4219-4224), McKemmish et al. 2009 (Phys Rev E 80(2):021912) — decoherence-
  debate canon, stable across the corpus and internally consistent; **real-correct** (carried,
  no metadata edits needed).
- Revonsuo 2006 (Conscious. Cogn. 15:489-508), Bayne & Chalmers 2003 (The Unity of
  Consciousness, OUP), Nagel 1971 (Synthese 22:396-413), Hameroff & Penrose 2014 (Phys Life Rev
  11:39-78), Stapp 2009 (Mind, Matter, and Quantum Mechanics, 3rd ed., Springer), Saxena et al.
  2020 (ACS Nano 14(2):1403-1411) — canonical/background, stable; **real-correct**.

No fabricated cites detected (Wimmer entry was a real-paper-wrong-metadata case, not a phantom —
handled per the citation-verify-false-negative discipline: metadata corrected, claim and its
real source retained).

### Empirical-Currency Sweep

`find_superlative_claims` returned **no** matches. Manual eyeball of the binding-by-synchrony
treatment (§Classical Mechanisms, §Zero-Lag Synchrony Problem): the article does **not** present
gamma-synchrony binding as the settled/leading solution — it presents it critically as a BP1
mechanism that fails to deliver BP2 ("correlation is not identity", "coordination is not
identity") and flags Baum's zero-lag argument as an unresolved preprint. No superlative
("leading theory", "current record") requiring a currency qualifier. No drift to correct.

### Reference-List Integrity

Numbering is clean: every entry uses markdown lazy `1.` and renders as a sequential list (1-17).
The tail "1." entries the task flagged are the ordinary auto-numbering plus the internal
Southgate self-cite — not a numbering restart defect. Inline `(Author, Year)` pointers all
resolve to a References entry after the Afrasiabi correction. No orphan direction-mismatches of
concern (Hameroff-Penrose, Stapp, Saxena are bibliography/background refs supporting the Orch OR
/ Stapp-Zeno / microtubule-resonance prose; retained).

### Reasoning-Mode Classification (editor-internal; changelog only)

Named-opponent engagements unchanged this pass and carried as previously classified:
- Illusionist (§Illusionist Challenge) — Mixed Mode One (regress) + Mode Two (argument from
  reason). Honest.
- Identity theorist (synchrony = unity) — Mode One / Mode Two (coordination ≠ identity from the
  opponent's own causal framework).
- Eliminativist / MWI defender / Buddhist no-self — Mode Three framework-boundary; bedrock, not
  re-flagged.
No label leakage; no editor vocabulary in prose.

## Optimistic Analysis Summary

### Strengths Preserved

- BP1/BP2 scaffold and the "coordination is not identity" structural-failure argument — the
  article's signature contribution, untouched.
- The quantum/classical comparison table and the "Testable Commitments" falsifiability section
  (both supporting and undermining predictions) remain intact.
- Calibration is honest throughout: "None of this proves quantum unity generates phenomenal
  unity"; quantum proposal hedged as "may / if / proposes". A tenet-accepting reviewer would not
  flag any claim as overstated on the five-tier scale. No possibility/probability slippage.

### Enhancements Made

None beyond the corrections. Length-neutral: the Afrasiabi body rewrite is ~same length as the
Wimmer sentence it replaces; the Santander edit is marginally shorter. No expansion/trim
oscillation on a converged article.

## Length

~2930 words — soft_warning (concepts soft 2500 / hard 3500). Net change ≈ 0. No condense
needed.

## Remaining Items

- Santander co-authors beyond the first (the entry's "Bekir, S., Paul, T.") were not
  individually re-verified (first author + title + venue + DOI confirmed; "et al." covers the
  rest). Low risk; carried.
- "Unity as Primitive" remains the thinnest of the three theoretical positions — expansion
  deferred under length constraints (carried across all prior reviews).

## Stability Notes

The article is otherwise converged; this pass's value was entirely in the **owed
publisher-of-record web-verify**, which caught a citation conflation (Wimmer→Afrasiabi) that six
prior intra-corpus reviews *ratified* rather than caught — exactly the pattern the §2.4 discipline
predicts. Bedrock disagreements remain bedrock and must NOT be re-flagged: eliminativists denying
phenomenal unity, MWI proponents finding the indexical argument unsatisfying, Buddhist no-self,
functionalists equating unity with integration (properly engaged Mode Two). The quantum proposal
is speculative by design; decoherence is the acknowledged empirical challenge. Future reviews:
focus on new content/source issues and wikilink integrity — the philosophical structure and
calibration are settled.