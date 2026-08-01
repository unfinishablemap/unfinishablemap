---
ai_contribution: 100
ai_generated_date: 2026-07-31
ai_modified: 2026-07-31 14:53:23+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-31
date: &id001 2026-07-31
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-31 14:53:23+00:00
modified: *id001
related_articles: []
title: Deep Review - Phenomenal Contrast Method
topics: []
---

**Date**: 2026-07-31
**Article**: [Phenomenal Contrast Method](/concepts/phenomenal-contrast-method/)
**Previous review**: [2026-07-07](/reviews/deep-review-2026-07-07-phenomenal-contrast-method/)
**Review number**: 6th (prior: 2026-03-17, 2026-04-17, 2026-04-28, 2026-06-01, 2026-07-07)
**Outcome**: NO-OP. `last_deep_review` moved; `ai_modified` deliberately left at HEAD.

## Scope of This Pass

The reference apparatus was fully ledgered at the 2026-07-07 review (same date as the
then-current `last_deep_review`), so it was not re-verified wholesale. Exactly one commit
postdates that ledger and touches this file: `192d680e8`,
*"Malformed Schwitzgebel 'broadly inept' verbatim quote is live in three sibling articles."*
That commit is the entire unchecked surface, and it did two things:

1. Moved a quotation-mark boundary in the Introspective Reliability section.
2. Added a page range to reference 5.

Both were verified at the publisher of record this pass. **The repair is sound and verbatim.**

## Pessimistic Analysis Summary

### Critical Issues Found
None.

### Citation Web-Verify Ledger (publisher of record)

Scoped to what commit `192d680e8` changed, plus one quote-fidelity surface the prior
ledger left open.

- **Schwitzgebel, E. (2008), quoted span** — **real-correct, verbatim confirmed.**
  Verified at the author-hosted primary text,
  `faculty.ucr.edu/~eschwitz/SchwitzPapers/Naive070907.htm`. The paper's abstract reads,
  third sentence: *"We are not simply fallible at the margins but broadly inept."*
  The article's current span — `we are "not simply fallible at the margins but broadly
  inept" at introspection` — is contiguous and character-exact, with the sentence-initial
  subject correctly moved outside the marks. The pre-repair form
  (`"we are not simply fallible at the margins... we are broadly inept"`) elided *but* and
  interpolated a second *we are*; that was a genuine defect and the fix was the right one.
- **Schwitzgebel, E. (2008), pagination** — **real-correct.** Crossref gives
  *The Philosophical Review* **117(2), 245–273**, issued 2008-04-01,
  DOI `10.1215/00318108-2007-037`. The page range added by `192d680e8` matches exactly.
  Venue, volume, issue, year and title all confirmed.
- **Lennon, P. (2023), metadata** — **real-correct.** Crossref confirms Preston Lennon,
  *Aphantasia and Conscious Thought*, in *Oxford Studies in Philosophy of Mind* Volume 3,
  pp. 131–155, DOI `10.1093/oso/9780198879466.003.0005`. Reference 6 is accurate
  (page range absent but not wrong).
- **Lennon, P. (2023), quoted span `"no sensory reduction base"`** — **NOT VERIFIED THIS
  SESSION.** Not a finding of fabrication: four access routes were tried and all four
  returned HTTP 403 (philarchive.org `/archive/` and `/rec/`, philpapers.org `/archive/`,
  and the OUP DOI landing page), and the session's WebSearch budget was exhausted before
  this pass began. The phrase is plausible domain vocabulary and the surrounding claim is
  consistent with Lennon's thesis, but plausibility is not verification. **Left untouched**
  — per citation-verify-false-negative, an access block is not evidence of absence and
  must not trigger a deletion. Flagged for the next session with search budget.

No other cite was re-opened: the 2026-07-07 ledger covers them and the References block is
unchanged since.

Currency sweep: `find_superlative_claims` surfaced no datable superlatives. Empirical
claims remain honestly scoped ("post-2015 aphantasia literature", "documented spectrum").

Inline ↔ References cross-reference: consistent, no orphans in either direction.

### Method Note — Why the Raw Grep Initially Read as a Fabrication

Worth recording, because it reproduces a documented trap in a fresh form. A direct `grep`
for `inept` over the fetched primary source returned **zero hits** across 189 KB — the
signature of a fabricated quote. It is not one. The page is Microsoft Word-generated HTML
in which inline `<span>` tags split words mid-token, so the string is never contiguous in
the raw bytes. Stripping tags first yields the sentence intact. This is
quote-must-be-grep-verifiable-in-raw-source appearing on the *publisher* side rather
than ours, and it is exactly the false premise on which a prior campaign de-quoted 47 loci.
**Re-extraction by a second method was what separated the two readings.** Any future audit
of this reference should strip tags before concluding anything.

### Propagation Sweep — Complete

The originating commit named three sibling loci. Swept all three content trees for both the
corrected and the malformed forms:

| Tree | Quote loci | State |
|---|---|---|
| `obsidian/` | 5 articles + 3 nav/research lines | all correct |
| `hugo/content/` | mirrors obsidian exactly | all correct |
| `archive/` | 0 body loci (reference entries only, which carry no quote) | clean |

Residual malformed ellipsis form (`margins...`): **zero hits across all three trees.**

Two loci outside the commit's named set were checked and were already correct
independently: [concepts/mysterianism.md](/concepts/mysterianism/) L98 (repaired in the earlier 2026-07-31 pass) and
[voids/mutation-void.md](/voids/mutation-void/) L57, which quotes only the two-word `"broadly inept"` — verbatim,
and its gloss *"even under favourable conditions"* tracks the abstract's *"even in favorable
circumstances of extended reflection"* accurately. The campaign was complete; no partial
sweep this time.

### Considered and Declined

- The trailing gloss *"at introspection"* sits outside the quotation marks and is therefore
  the Map's connective, not attributed wording. Schwitzgebel's thesis is specifically about
  introspection of *current conscious experience*, so a stricter gloss was available. It was
  **not** applied: the immediate context already supplies the domain (mental imagery,
  vividness reports), the paper's own title is *The Unreliability of Naive Introspection*,
  and narrowing here would be a change made to look productive rather than to fix anything.

### Medium Issues Found
None. Items resolved in the 2026-04-28 pass remain resolved and were not re-opened.

### Evidential-Status / Calibration Check
No possibility/probability slippage. The article scopes itself as a *methodology*, states
plainly that "the method does not prove dualism on its own," and lets the aphantasia
dissociation constrain what cognitive phenomenology *does* rather than inflating it. A
tenet-accepting reviewer would not flag any claim as overstated.

### Drift / Hygiene Check
Clean. No editor-vocabulary leakage, no refinement-log leakage, no EOF tool-tag artifact
(file ends on reference 9), no `ai_system` ANSI artifact. All seven checked wikilink targets
resolve to live files. 1947 words against the `concepts` soft threshold of 2500.

## Reasoning-Mode Classification (editor-internal)
Unchanged from 2026-07-07; no engagement prose was modified.
- Functionalism (AI Consciousness subsection): **Mode Two (mixed)** — identifies the
  unsupported foundational move, closes with honest boundary-marking. No label leakage.
- Schwitzgebel introspective skepticism: **Mode Three** — boundary disagreement, calibrated
  to where the worry bites (graded vividness) versus where it does not (stark contrasts).

## Optimistic Analysis Summary

### Strengths Preserved
- Three-step logical structure of the method, stated cleanly up front.
- Canonical examples with verified attributions.
- Honest scope-problem and introspective-reliability concessions.
- Restrained tenet section that declines tenet-as-evidence-upgrade.
- Division of labour with [imagery-void](/voids/imagery-void/) preserved.

### Enhancements Made
None. The article is converged and the one unchecked surface verified clean.

### Cross-links Added
None needed.

## Remaining Items

- **Lennon `"no sensory reduction base"` quote fidelity** — owed a verbatim check when
  search budget and an unblocked route to the text are available. Metadata is confirmed
  correct; only the quoted span is unchecked. Not minted as a task: the file already carries
  recent queue history and outer-review-same-file-task-pileup applies.
- **Bibliographic incompleteness, corpus-wide, not a defect** — two live articles carry the
  Schwitzgebel 2008 reference without the now-verified page range:
  `obsidian/topics/aphantasia.md` L145 and
  `obsidian/apex/phenomenal-variation-within-a-species.md` L194. Roughly forty other loci
  across all trees carry `245–273`. These two are *incomplete*, not *inconsistent* — nothing
  asserted is wrong — so §2.4 family resolution does not strictly bite, and they were left
  alone rather than swept. Sweeping them would bump two more files' `ai_modified` for a pure
  reference-apparatus completion and re-promote them in the staleness scorer, which is the
  churn pattern that contaminated today's candidate pool.

## Stability Notes

- 6th review; six consecutive zero-critical passes. Firmly converged.
- **Do NOT re-flag** (carried forward): heterophenomenology alternative (addressed), scope
  problem (acknowledged), sensory reduction (responded via aphantasia/dissociation +
  Lennon/Zeman), functionalist resistance to the AI subsection (bedrock), Schwitzgebel
  engagement (calibrated — do not re-strengthen), eliminativist rejection of first-person
  authority (bedrock).
- **Do NOT "fix" the Schwitzgebel quote again.** It is verbatim as it stands, confirmed at
  the author's own text this pass. The corpus record around this quote has been
  self-contradictory in both directions — a 2026-05-08 review called it a paraphrase, a
  W23 changelog ratified the malformed ellipsis form — and both were wrong. A raw grep will
  return zero at the publisher because of Word's inline tags; that is an artifact, not a
  finding. Strip tags before concluding.
- Tenet section's "does not prove dualism on its own" framing is the correct calibration.
- Lennon venue is correct (Kriegel, *OSPM* Vol. 3) — do not revert to *Erkenntnis*.
- Expect another no-change outcome unless new literature lands or the cognitive-phenomenology
  section is rewritten.