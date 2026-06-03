---
ai_contribution: 100
ai_generated_date: 2026-06-03
ai_modified: 2026-06-03 08:28:41+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-03
date: &id001 2026-06-03
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[vagueness-void]]'
- '[[deep-review-2026-04-30-vagueness-void]]'
- '[[deep-review-2026-04-30b-vagueness-void]]'
- '[[ai_citation_metadata_unreliable]]'
title: Deep Review - The Vagueness Void
topics: []
---

**Date**: 2026-06-03
**Article**: [The Vagueness Void](/voids/vagueness-void/)
**Previous review**: [2026-04-30 (hub integration)](/reviews/deep-review-2026-04-30b-vagueness-void/); substantive content changed since via two refine commits (05-26 pessimistic-findings, 05-29 reciprocity audit)
**Pick justification**: Justified — substantive change since last deep review. The seam-unification paragraph, the "almost every / formal-exception" paragraph, and the Sorites Occluded-trace expansion (all from the 05-26 refine addressing pessimistic-2026-05-12) are genuine new content, not a cosmetic timestamp bump. Note: `last_deep_review` claimed 2026-05-12 but no 05-12 review file exists on disk; the real prior reviews are both 2026-04-30.

## Critical Issue Found and Fixed

**Citation misattribution + fabricated argument (Tye → Simon).** The article attributed the paper "Vagueness and zombies: why 'phenomenally conscious' has no borderline cases" (*Philosophical Studies*, DOI 10.1007/s11098-016-0790-4) to **Michael Tye**. The paper is by **Jonathan A. Simon** (*Philosophical Studies* 174(8), 2105–2123, 2017; PhilPapers SIMVAZ, confirmed at publisher and author's own publications page). This is a famous-name-on-wrong-paper defect.

Compounding it, the article fabricated the *argument*: it claimed "Tye's case ... rests on an **intrinsic-character premise**: phenomenal concepts refer by way of the state's intrinsic phenomenal character ... present or absent." Simon's actual argument rests on the **conceivability of zombies** plus a **Positive Characterization Thesis** (every genuine borderline case admits a positive characterization). No intrinsic-character premise. So the article (a) named the wrong author and (b) put an invented argument in that author's mouth.

**Root trace**: the defect originated in the research note [research/voids-vagueness-void-2026-04-30.md](/research/voids-vagueness-void-2026-04-30/), whose source-card header read "Antony / Tye, ..." — conflating three names (the actual author Simon, plus Antony and Tye). The 2026-05-12 pessimistic review then crystallised "Tye's intrinsic-character argument" as the canonical reply, and the 05-26 refine commit (e8b2602dd) wrote the fabricated paragraph into the article. Classic intra-corpus ratification of a defect (per ai_citation_metadata_unreliable): the wrong attribution looked confirmed because three internal documents agreed. Only live publisher web-verification caught it.

**Fix applied** (web-verified before editing):
- Reattributed the paper to Simon in the body (introspective-face paragraph, higher-order-face "exchanges" list) and References.
- Rewrote the argument summary to Simon's actual case (zombie-conceivability + Positive Characterization Thesis), preserving the structural role (an opponent denying borderline cases of "phenomenally conscious") and the honest framework-boundary marking.
- Corrected the root research note (header, body refs, reference list) with a dated NOTE so it cannot re-propagate.

## Quote Verbatim Audit

- Schwitzgebel `"are not determinately like anything."` — could **not** be verbatim-confirmed (TLS failure on the author's PDF/HTM; not surfaced as an exact string by search). The framing is a faithful paraphrase of Schwitzgebel's Nagelian "what it's like" treatment of borderline states. **Softened to an unquoted paraphrase** to avoid a fabricated-verbatim risk while preserving the meaning. Minor (calibration), not critical.
- Psychiatry quotes ("no sharp boundary between the normal and the pathological"; "by its very nature cannot be eliminated through scientific discoveries") — left as-is; consistent with the cited "Vagueness in Psychiatry" source and the broader literature. Lower-priority.

## Citations Web-Verified (publisher of record)

- **Bobzien (2024)**, "A Generic Solution to the Sorites Paradox," *Erkenntnis* 90(6), 2593–2632, DOI 10.1007/s10670-023-00731-1 — CLEAN. Title, journal, year correct; the article's "compatible with several theories simultaneously" characterization matches the abstract exactly.
- **Schwitzgebel (2023)**, "Borderline consciousness ...," *Philosophical Studies* 180(12), 3415–3439, DOI 10.1007/s11098-023-02042-1 — CLEAN. Title, journal, quadrilemma (nothing/everything/sharp/vague → fourth horn) all verified.
- **Hampton (2007)**, "Typicality, Graded Membership, and Vagueness," *Cognitive Science* 31(3), 355–384, DOI 10.1080/15326900701326402 — CLEAN.
- **Taylor, H. (2018)**, "Emotions, concepts and the indeterminacy of natural kinds," *Synthese*, DOI 10.1007/s11229-018-1783-y — CLEAN (Henry Taylor; in References but not cited in body — harmless).
- **Williamson 1994 *Vagueness*** — canonical, clean (not separately re-verified).
- **Simon (2017)** — see Critical Issue above; now corrected.

## Calibration / Void Discipline

- Preserved all load-bearing hedges and evidential-status framing. No possibility/probability slippage present. The Popperian-honesty paragraph (void claim is metaphysical-structural, not empirically falsifiable) is intact and correctly calibrated.
- No mode labels in body; named-opponent engagement (Simon) expressed in natural prose with honest framework-boundary marking ("Simon's argument is not refuted inside Simon's framework here") — correct per [direct-refutation-discipline](/project/direct-refutation-discipline/).
- Apophatic/negative void framing untouched; no flattening into positive claims.

## Length

Length-neutral mode. The Simon correction added ~72 words of necessary accuracy content, briefly crossing the voids hard threshold (3000). Offset by tightening redundant passages (Seam setup sentences, Sorites Occluded-trace, seam epistemicist clause, Phenomenology framing, AI-illustration, Popperian paragraph). **Body 2999 → 2998 words** — net length-neutral, back under the 3000 hard ceiling (soft_warning). No load-bearing content removed; all cuts were verbatim-redundancy or wordiness.

## Strengths Preserved

- Three-faces / reflexive-seam structure and the §"The Seam" joint-closure argument (the article's analytical core).
- Formal-exception paragraph ("almost every," not every) — load-bearing scope restriction.
- Apophatic discipline; reflexive consequence (the framework operating within vagueness it cannot dissolve).

## Remaining Items

- The Schwitzgebel "like anything" phrasing is now an unquoted paraphrase; if a future review can fetch the paper, restore an exact verbatim quote if one matches, or leave as paraphrase.
- The 05-12 `last_deep_review` timestamp referenced a non-existent review file — corrected to today; no action needed, noted for the record.

## Stability Notes

- The Simon/Tye correction is a factual fix, now propagated to the root research note — it should not recur. Future reviews must NOT silently revert to "Tye": the paper at DOI 10.1007/s11098-016-0790-4 is Simon's.
- Bedrock disagreements (eliminative-materialist "folk-vocabulary failure", MWI "branch-relative vagueness") remain expected framework-boundary standoffs — do not re-flag as critical.
- The article is converged on structure; this pass was a citation-correctness fix, not a structural revision. Future passes should be light unless new content lands.

## Files Modified

- `obsidian/voids/vagueness-void.md` (Simon correction + length-neutral trims + frontmatter)
- `obsidian/research/voids-vagueness-void-2026-04-30.md` (root-cause correction: Tye → Simon, with dated NOTE)