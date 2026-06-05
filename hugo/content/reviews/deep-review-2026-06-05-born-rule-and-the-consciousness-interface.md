---
ai_contribution: 100
ai_generated_date: 2026-06-05
ai_modified: 2026-06-05 14:26:16+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-05
date: &id001 2026-06-05
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Born Rule and the Consciousness-Physics Interface
topics: []
---

**Date**: 2026-06-05
**Article**: [The Born Rule and the Consciousness-Physics Interface](/topics/born-rule-and-the-consciousness-interface/)
**Previous review**: [2026-06-02](/reviews/deep-review-2026-06-02-born-rule-and-the-consciousness-interface/) (18th+ pass)

## Selection Rationale (changed-since-review staleness)

`last_deep_review` was 2026-06-02; `ai_modified` was 2026-06-04 (NOT today). Three
refine commits landed between the last review and now — the most load-bearing being the
06-04 "Adopt consciousness-physics-interface-formalism calibration" pass, plus two
citation-metadata fixes (niaf011 Babcock/Hameroff→Wiest; Kerskens López-Pérez surname).
Citation-heavy (37 references, many post-2020 quantum/empirical/preprint), matching the
steer's preference. Audit focused on the unreviewed delta + a full citation pass
including background refs. Diffed against the last-review base (59d11f8dd) before auditing.

## Pessimistic Analysis Summary

### Critical Issues Found
- **CHIMERA / wrong-author + misattributed-quote citation defect — Landsman (2025),
  ref #21 → FIXED.** The article cited arXiv:2502.08545 "The Born Rule — 100 Years Ago
  and Today" as **Landsman, K. (2025)** and quoted "Landsman's 2025 centenary review"
  concluding *"all derivations found in the literature are either circular or unrelated
  to measurement."* Web-verification against arXiv/Entropy establishes:
  1. **Wrong author.** arXiv:2502.08545 / *Entropy* 27(4):415 is by **Arnold Neumaier**
     (Univ. Wien, single author), NOT Klaas Landsman. Klaas (N.P.) Landsman is a real
     Born-rule author — his survey is "The Born rule and its interpretation"
     (math.ru.nl/~landsman/Born.pdf) and his 2020 "Indeterminism and Undecidability"
     (arXiv:2003.03554, correctly cited *elsewhere* in the corpus) — but he did not author
     the 2025 centenary arXiv paper. Classic chimera: right title/year/venue, wrong author.
  2. **Stance error + unverifiable verbatim quote.** Neumaier's paper does NOT conclude
     the Born rule is underivable. It says standard derivations are "usually circular"
     because they presuppose measurement — *but argues his own detector-response postulate
     succeeds* once measurement is defined operationally. The quoted sentence matches
     neither Neumaier's wording ("usually circular and hence of questionable value") nor
     any verifiable Landsman publication. The article had used the (mis)quote to support
     "a century of failed attempts" — against the cited paper's own thesis.

  **Resolution (3-state de-citation discipline — state 2: real-paper-wrong-metadata +
  wrong-stance):** the *paper* is real, so not deleted. Reattributed to Neumaier (2025),
  *Entropy* 27(4):415, and the body recast to report what Neumaier actually argues
  (derivations "usually circular" because they presuppose measurement; Neumaier dissents
  from underivability via his detector postulate; the consciousness-free rivals read this
  as relocating the observer). The unverifiable verbatim quote removed. The article's
  underivability claim survives — it is independently carried by Araújo (2021), Zhang
  (2026), and the observer-presupposition point, none of which depend on the bad cite.

- **Propagated to research file → FIXED.** Same Landsman(2025)=arXiv:2502.08545 defect in
  [born-rule-derivation-attempts-2026-03-14](/research/born-rule-derivation-attempts-2026-03-14/) (meta-assessment line + reference list).
  Reattributed to Neumaier with an inline NOTE recording the correction. (The *other*
  Landsman cites in the corpus — self-reference-and-the-limits / measurement-problem,
  both "Landsman 2020, arXiv:2003.03554" — are a genuinely different, real Landsman paper
  and are CORRECT; not touched.)

### Citation Web-Verification (publisher of record)
Four citations changed since the last review were the highest-risk items (recently-edited
author lists) and were web-verified — all four fixes are CORRECT:
- **Ref #5 niaf011** — VERIFIED author is **Michael C. Wiest** (Wellesley), *Neuroscience
  of Consciousness* 2025(1) niaf011. The 06-04 fix Babcock/Hameroff→Wiest is right (old
  metadata was the wrong-author chimera). The body characterization quote "direct physical
  evidence of a macroscopic quantum entangled state in the living human brain" is accurate
  to Wiest's abstract.
- **Ref #11 DeBrota** — VERIFIED authors **DeBrota, Fuchs, Pienaar, Stacey** (PRA 104,
  022207, 2021). 06-04 fix from "…& Schack" → "…Pienaar & Stacey" is right (Schack was the
  wrong fourth author).
- **Ref #20 Kerskens** — VERIFIED authors **C.M. Kerskens & D. López Pérez** (J. Phys.
  Commun. 2022). Surname fix "Pérez, D.L."→"López Pérez, D." is right (compound surname).
- **Ref #22 Maier-Dechamps-Pflitsch** — VERIFIED **Maier, Dechamps & Pflitsch**, Front.
  Psychol. 9:379, doi:10.3389/fpsyg.2018.00379. Expanded cite matches exactly.
- Load-bearing arXiv cites (Torres Alegre 2512.12636, Zhang 2603.06211, Agrawal-Wilson
  2511.21355) were web-verified clean on 2026-06-02 — not re-verified this pass per the
  prior review's instruction; no new edition/retraction.

### Inline ↔ References consistency (both directions)
- Every References surname resolves in-body; every body author-year cite resolves to a
  References entry. The two apparent orphans are non-issues confirmed in the prior review:
  Ghirardi (#13) cited via "GRW" acronym; SEP (#29) cited as "(SEP 2024)".
- Low-confidence PhilArchive cites (Tonetto, Arana) lack arXiv/DOI but are framed as
  preprints, are tangential not load-bearing, and were retained by prior reviews — no
  positive fabrication evidence, left as-is.

### Reasoning-Mode Classification (editor-internal)
- **QBism (DeBrota-Fuchs-Pienaar-Stacey)**: Mode Three (framework-boundary) — "not an
  in-framework refutation; the disagreement is framework-boundary." Honest.
- **MWI (Deutsch/Wallace/Carroll-Sebens)**: Mode Three — "its preference for indexical
  identity over branching is tenet-load-bearing." Honest bedrock-marking.
- **Neumaier / Hilbert-space primitivist (Urgleichung)**: Mode Three with partial Mode-Two
  flavour; article concedes "the realist could dispute both" and absorption is "heuristic
  rather than derivational." Honest. No boundary-substitution, no label leakage.

## Optimistic Analysis Summary

### Strengths Preserved (do not change)
- The Compatibility-vs-Support section + three-tier interface-compatible/-suggestive/
  -discriminating gradient remains the corpus-canonical evidential-status treatment.
- Honest ownership of the corridor's structural unfalsifiability as "the honest cost, not
  a strength."
- "Relation to Site Perspective" inherits the discipline tenet-by-tenet.

### Enhancements Made
- Citation-accuracy repair only (Landsman→Neumaier, article + research file). No
  expansion: article is over the topics hard threshold.

### Cross-links Added
- None (article at 170% of soft threshold; length-neutral mode).

## Length
- Before: ~5064 words. After: ~5107 words (+~43; the Neumaier correction is marginally
  longer than the dropped misquote — a critical-fix exception, not discretionary expansion).
- **Over the topics hard threshold (4000); 170% of the 3000 soft target.** Under critical
  (6000). Per steer: did NOT condense — the over-length is the protected own-calibration
  content. Human length-decision task already queued (DEFERRED-TO-HUMAN 2026-06-02); not
  re-queued.

## Remaining Items
- **Human length decision** — already queued from the prior review; still open. No action.
- The Landsman(2025) chimera was caught only by live web-verification of a background-class
  meta-assessment cite — exactly the "AI citation metadata unreliable / converged ≠
  verified" pattern. Recommend a corpus-wide grep for any other "Landsman (2025)" /
  arXiv:2502.08545 attribution if new born-rule articles appear (this pass fixed the two
  found: the article + the 03-14 research note).

## Stability Notes
- **Converged on thesis, structure, framing** — unchanged from the 2026-06-02 baseline.
  This pass was a citation-accuracy correction, not a content event.
- **All framework-boundary disagreements (QBist, objective-collapse, hidden-variable, MWI,
  Popperian-unfalsifiability) are bedrock** — honestly marked in-article; do NOT re-flag.
- **The corridor's structural unfalsifiability is owned, not hidden** — do not "fix" it.
- **Do NOT condense without a human length decision** — over-length is protected
  calibration content (the condense-regresses-calibration danger zone).
- **The four changed citations + three load-bearing arXiv cites are now web-verified clean**
  — do not re-verify absent a new edition/retraction.