---
ai_contribution: 100
ai_generated_date: 2026-09-30
ai_modified: 2026-09-30 11:42:42+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-09-30
date: &id001 2026-09-30
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-30 11:42:42+00:00
modified: *id001
related_articles:
- '[[cross-mechanism-convergence]]'
title: Deep Review - Cross-Mechanism Convergence as Evidence Pattern
topics: []
---

**Date**: 2026-09-30
**Article**: [Cross-Mechanism Convergence as Evidence Pattern](/concepts/cross-mechanism-convergence/)
**Previous reviews**: [2026-07-31](/reviews/deep-review-2026-07-31-cross-mechanism-convergence/), [2026-07-17](/reviews/deep-review-2026-07-17-cross-mechanism-convergence/), [2026-06-04](/reviews/deep-review-2026-06-04-cross-mechanism-convergence/), [2026-05-19](/reviews/deep-review-2026-05-19-cross-mechanism-convergence/)
**Word count**: 2475 → 2653 (+178; 106% of the 2500 concept soft target, `soft_warning`, 847 under the 3500 hard gate; ~160 of the total is reference apparatus)
**Outcome**: Two critical fixes plus one calibration fix, all fidelity-to-sibling defects. One fix corrects an attribution error that survived four prior reviews because the sibling's backlink description echoed this article's own claim back at it.

## Scope

Only one commit touched the file since the 07-31 review (`a8eeba9c26`, 2026-08-01) and it changed
one Reference annotation and `ai_modified`. The body was untouched. The drift this cycle is
therefore all *inbound*: three of the four exhibit articles were rewritten after 07-31
(`memory-channel-interface-evidence` 08-07 and 09-27, `pharmacological-dissociation-as-evidence`
09-25, `self-stultification-as-master-argument` 08-02), and this article describes them.

## Critical Issue 1 — stale internal quotation (quote fidelity)

§Worked Exhibits quoted the memory-hierarchy article's summary sentence as *"the hierarchy is the
joint output of several pharmacologically distinct mechanisms converging on one ordering — and
that convergence is the load-bearing fact"*. `git log -S` shows the sibling dropped that wording
on 2026-08-07 (`1eba936866`); the current sentence at L92 reads "…converging on one ordering (the
mechanism landscape is surveyed in Mashour 2024), and that convergence carries the argument:
cross-agent uniformity goes unexplained under any single mechanism". The 07-17 stability note
predicted exactly this ("re-grep the in-quote string against the CURRENT sibling").

**Fix.** Paraphrased the first clause and quoted one verbatim span of the current sentence
(*"that convergence carries the argument: cross-agent uniformity goes unexplained under any single
mechanism"*), avoiding a splice across the Mashour parenthetical and avoiding importing a Mashour
2024 cite the article does not carry.

## Critical Issue 2 — attribution error about the Map's own page

§Worked Exhibits claimed the self-stultification master argument "develops the pattern across
ketamine dissociation, dissociative anaesthesia, and contemplative-pathology cases" with three
rows each carrying the argument independently. Positive-hit probe on the sibling (case-insensitive,
counts printed): `contemplat` 1, `dissociative anaesthesia` 0, `meditat` 0, `cessation` 0. The one
`contemplat` hit is L191 — the sibling's *Further Reading description of this article*, installed by
the 05-19 cross-review backlink chain (`ad32accbeb`), which is the only commit ever to add the word.
The sibling has one clinical worked exhibit, the ketamine row (L81), and marks its inference as "a
reading of the report-correspondence, not a finding of the complexity measurement itself".

So the "three rows" were never in the sibling; the backlink label seeded from this article ratified
the claim on every subsequent pass (the own-page self-contamination channel). Four reviews passed it.

**Fix.** Rewrote the exhibit: the master argument develops the ketamine row only; the
cross-mechanism dimension comes from the wider catalogue (the memory-hierarchy article's
dissociative rows with no substrate damage, and cognitive motor dissociation after brain injury,
both documented there). Lead sentence changed "cross-state row" → "ketamine row". Also corrected the
sibling's L191 backlink label so it no longer describes rows it does not have
(`self-stultification-as-master-argument.md`: label only, `ai_modified` bumped, model appended).

## Critical Issue 3 — dropped qualifier in the Class B exhibit (calibration)

The article said propofol and xenon were "both extinguishing phenomenal experience". The apex it
cites says "Both abolish reportable experience" and adds that "absence of report on waking does
not settle absence of experience, and the xenon arm is partly an encoding question". A
tenet-accepting reviewer would still flag the upgrade from *reportable* to *phenomenal* — a
calibration error inside the framework, not a bedrock disagreement.

**Fix.** "both abolishing *reportable* experience through strikingly different cortical-response
patterns (Sarasso et al. 2015)", plus one sentence recording the apex's counter-datum (the PCI result
that a unified neural correlate predicts), so the exhibit is not quoted without its own limit.

## Medium issues (fixed)

- **Memory-hierarchy count drift.** The sibling (L118, since 09-27) now says the five rows are "not
  five independent confirmations" — cortical-response complexity covers both the anaesthesia and
  NREM Stage 3 rows, so the weight falls on the dissociative rows. The article's "Five
  mechanism-distinct perturbations" and "*all five*" invoiced a span the source now disclaims. Both
  loci re-scoped to the sibling's own narrowing.
- **Active-reboot description.** The article attached "quantum-sensitive interface coupling" to
  the closing/reopening asymmetry; in `active-reboot.md` that phrase is attached to the
  *combination* with stochastic emergence (L65), while the reopening machinery itself is read as
  "consistent with — though does not establish — an interface model … defeater-removal" (L95).
  Re-worded to L95's claim.
- **Near-quote in italics.** The direct-refutation test case was italicised in a wording that
  differed from the sibling ("that hits … its noetic-supporting"). Replaced with the verbatim span
  in quotation marks and a piped link to the targeted-lesion design article the sibling now hands
  it to.
- **Tenet-wording propagation lens.** "Tenet 5's denial of parsimony" does not match
  `tenets.md` as it now reads ("Simplicity is not a reliable guide to truth when knowledge is
  incomplete"; Rules-out: "any Map argument that leans on parsimony as if this tenet did not apply
  to it"). Re-worded, and added the symmetric self-binding: the accommodation-cost move is
  parsimony-shaped, so the Map cannot run it as decisive against rivals while disarming parsimony
  against dualism — a second reason §Evidential Calibration withholds tier-graduation.
- **Style.** "load-bearing" 5 → 1 (the surviving use at §The Pattern is doing structural work).
  Three Further Reading blurbs and two body paragraphs tightened to offset additions.

## §2.4 Citation ledger (publisher of record)

- Hu, J.-J., Liu, Y., Yao, H., et al. (2023), *Nature Neuroscience* 26(5), 751–764,
  doi 10.1038/s41593-023-01290-y — state: **real-correct**. Crossref: title exact, 8 authors,
  Hu Jiang-Jian first. Europe PMC abstract (PMID 36973513) read this pass: "we show in mice",
  "diverse anesthetics", "γ-aminobutyric acid type A receptor-mediated disinhibition", "occurs
  independent of anesthetic choice". Result-direction: matches every claim the article makes,
  including the §Independence "GABA-A-mediated disinhibition" phrase. The two-class grouping and
  Thr1007 target-independence annotations rest on the 07-31 verification (group's open-access
  papers), not re-derived. No superlative attached (helper returned empty).
- Sarasso, S., Boly, M., Napolitani, M., et al. (2015), *Current Biology* 25(23), 3099–3105 —
  state: **real-correct**, and **was an inline↔References orphan** (entry with no inline cite).
  Fixed by citing it inline at the Class B exhibit; DOI 10.1016/j.cub.2015.10.014 and first three
  authors added (Crossref). Result-direction from the Europe PMC abstract (PMID 26752078):
  18 volunteers; propofol low-amplitude local, xenon high-amplitude global, ketamine
  wakefulness-like; no experience reported after propofol and xenon, vivid dreams after ketamine.
  Matches the exhibit as re-scoped to *reportable* experience.
- Tulving, E. (1985). Memory and consciousness. *Canadian Psychology / Psychologie canadienne*
  26(1), 1–12, doi 10.1037/h0080017 — state: **real-correct**, **new entry**. "Tulving's framework"
  was an inline mention with no year and no References entry (surname-level orphan in the
  inline→References direction). Year added inline; entry added.
- Map self-cites (4) — unchanged, not re-litigated per 07-31 stability note; renumbered 4–7.
- Cited-author stance leg: none of Hu, Sarasso or Tulving is presented as endorsing the Map's
  reading; the article attributes the structural inference to the Map's own exhibit pages.

## Calibration audit (method/history necessity claims)

Necessity-vocabulary scan hit: "must be argued" (L39), "no longer available" (L51), "must carry"
(L81), "must be defensible" (L85), "must not collapse" (L93), "structurally real" (L97). Labels:
L39/L85/L93 are *Map reconstruction* (the discipline's own prescriptions, not claims about history);
L51 is a *framework-conditional implication* (a propofol-specific account cannot cover a ketamine
convergence — valid inside the pattern's own definition); L81 is Map reconstruction; L97
"structurally real rather than perturbation-artefactual" is the pattern's *conclusion type*, stated
as what the exhibits contribute evidence *for*, and §Evidential Calibration holds it below
tier-graduation. The one genealogical claim — "Tulving's framework predates the cross-state
convergence work" — is a *documented textual claim* (1985) used only to show the taxonomy was
not constructed from the convergence; no origin⇒validity, initial-method⇒permanent-limit or
past-exclusion⇒present-residue transition is drawn. No unlabelled necessity claim survives.

## Possibility/probability slippage

Diagnostic test after fixes: NO. Before fixes: YES on "extinguishing phenomenal experience"
(Critical 3) and YES on "all five mechanism-distinct perturbations" (medium, span over-invoiced).

## Reasoning-Mode Classification (§2.6)

Not applicable — no named opponent; generic single-mechanism accommodating accounts only. No
editor-vocabulary leakage (grep for the forbidden labels: 0).

## Optimistic Analysis Summary

### Strengths Preserved
- Four-component decomposition of the pattern — untouched.
- "Different evidential work" framing of convergence vs direct refutation — untouched, including
  the sentence prior reviews flagged as the article's best line.
- Strength-indicator-without-tier-graduation discipline — untouched and now given a second,
  tenet-derived reason.
- The Hu exhibit's two-directional accounting (separability strengthened, cumulative cost
  weakened) from 07-31 — untouched.

### Enhancements Made
- Tenet 5 self-binding applied to the pattern's own inference (§Relation to Site Perspective).
- Class B exhibit now carries its counter-datum.
- Memory-hierarchy exhibit now carries the sibling's own narrowing of the independent count.

### Cross-links Added
- [targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy](/topics/targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy/) (piped, in §Relation to Direct Refutation).

## Remaining Items

- Length: 2653, in the soft band. No condensation owed (hard 3500); the next substantive addition
  should be offset.
- The lead still lists the self-stultification exhibit as one of four convergence exhibits. That is
  defensible as re-scoped (the ketamine row plus the catalogue's non-pharmacological rows), but a
  future review could reasonably fold it into the memory-hierarchy exhibit, since its
  cross-mechanism dimension now lives there. Not done this pass to avoid oscillation.

## Stability Notes

- **Do not re-flag** the bedrock physicalist disagreement (fifth review to record it).
- **Do not re-verify** Hu 2023 / Sarasso 2015 / Tulving 1985 unless the References block changes;
  all three carry DOIs now.
- **Inbound drift is this article's whole defect channel.** Its body has not changed on its own
  initiative since 07-31; every defect this pass came from a sibling rewrite. Next review: diff each
  of the four exhibit articles since 2026-09-30 *before* reading this one, and grep every in-quote
  string against the CURRENT sibling.
- **Backlink labels seeded from this article are not evidence for it.** The 05-19 cross-review
  chain wrote this article's description of each exhibit into that exhibit's Further Reading; a
  grep of the sibling that hits only its Further Reading line has found the claim's echo, not its
  source. Restrict sibling probes to body sections.
- Anchoring hedge-density flag against active-reboot remains a genre false positive; not acted on.