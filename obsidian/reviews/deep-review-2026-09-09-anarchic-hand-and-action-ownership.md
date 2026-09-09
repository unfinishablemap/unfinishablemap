---
title: "Deep Review - Anarchic Hand and the Fragmentation of Action-Ownership"
created: 2026-09-09
modified: 2026-09-09
human_modified: null
ai_modified: 2026-09-09T07:39:52+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-09
last_curated: null
---

**Date**: 2026-09-09
**Article**: [[anarchic-hand-and-action-ownership|Anarchic Hand and the Fragmentation of Action-Ownership]]
**Previous review**: [[deep-review-2026-08-04-anarchic-hand-and-action-ownership|2026-08-04]] (and [[deep-review-2026-07-16-anarchic-hand-and-action-ownership|2026-07-16]])

## Scope of This Pass

Targeted, not a fresh sweep. `last_deep_review` was 2026-08-04; the only content
change since is commit `4650f1ac25` (2026-08-21), whose diff against this file is
exactly **one inserted paragraph** (closing "The Interface Reading") plus
**reference 10** (Steinert et al. 2019). `git show` confirms references 1–9 are
byte-untouched since the 2026-08-04 per-cite ledger, so that ledger still stands
and was not re-litigated.

The 08-21 commit's *primary* target was
[[brain-computer-interfaces-and-the-interface-boundary]] ("fold it into the BCI
boundary article, which has 1381 words of headroom"); this article was a
**secondary host**. That matters: the inserted paragraph had never been read by
any review, and it turns out to have been rendered more strongly here than in the
primary host, which quoted the same source correctly.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Dropped modal — a prospective research direction asserted as accomplished fact.**
The paragraph read "predictive decoders initiate movement from anticipated rather
than commanded activity" — flat present indicative. The source is thoroughly
modalised and prospective. Verbatim from the publisher PDF (*Philos. Technol.*
(2019) 32:457–482, retrieved via `rd.springer.com`, SHA-256
`c6058d81…e9d4a351`):

> "One line of current research focuses on BCIs that read out brain states to
> predict users' movement intentions (Wang and Jung 2011). Through machine
> learning, BCIs **may** adapt to plans or intentions of the users… Engineers
> **hope** that this will lead to a much smoother user experience… However, **if**
> BCI systems initiate movements without any user command… users do not have
> executory control. This leads to the sixth peculiarity of BCIs, that **it may
> initiate movements by predictive interpretation of brain signals**."

Nothing in the source says predictive decoders *do* initiate movement; it says a
line of research aims at systems that *may*. **Resolution**: rewritten to name it
"prospective rather than accomplished — a line of research on decoders that read
brain states to predict a user's movement intentions," with the source's own
modal preserved inside a verbatim quote ("may initiate movements by predictive
interpretation of brain signals").

Note the **family-resolution** dimension: the primary host
[[brain-computer-interfaces-and-the-interface-boundary]] (L133) already quotes
this correctly *with* the modal. The two articles disagreed about the same source
sentence; this pass brings the secondary host into line with the primary, not the
reverse.

**2. Dropped framework qualifier on the load-bearing attribution.**
The paragraph read "Steinert et al. (2019) **argue** that events mediated by
passive BCIs are not actions at all" — an unconditioned thesis. The source
delivers the verdict explicitly *relative to a framework*:

> "By contrast, **according to the standard theory**, events mediated by passive
> BCIs do not constitute actions, because the events in question are not caused
> by the right mental states. This is the fourth peculiarity we wish to highlight:
> **events mediated by passive BCIs are no actions**."

And the very next section opens "However, some authors consider causal accounts of
agency of the kind just presented as too coarse-grained" — the paper then moves to
control-based accounts (executory / guidance / veto). So the attribution was not
*false* (the authors do assert the peculiarity in their own voice), but it dropped
the qualifier that makes it a standard-causal-theory verdict rather than a
free-standing conclusion. Per §2.5 this is a dropped qualifier that changes
meaning, and the irony is sharp: the paragraph sits two lines below the article's
own careful "the framework-relative reading is…" move. **Resolution**: attribution
now reads "on the standard causal theory of action, 'events mediated by passive
BCIs are no actions'", with the mechanism ("not caused by the right mental
states") quoted and the "peculiarities" framing named.

Also corrected in passing: "not actions at all" → the source's actual "are no
actions". The paper does use "do not qualify as actions at all," but of *some
BCI-mediated events* generally in its roadmap, not of passive BCIs.

### Medium Issues Found

**3. Analogy flattened the passive/predictive distinction it depends on.**
"Anarchic hand is the biological instance of that shape" identified anarchic hand
with a "shape" the sentence had just built out of *two different* BCI cases. They
are not interchangeable for this argument:

- **Passive** BCI: brain activity "not modulated intentionally to achieve a
  certain goal" (source, offset 14988) — no intention in any register.
- **Predictive** decoder: reads out "users' movement intentions… preferences or
  more distal intentions" — an intention *is* present; only the executory command
  is bypassed.

Anarchic hand aligns with the **passive** case. The article's own comparator
section (§"The Comparator Account, Conceded in Full") says the movements are
"triggered exogenously by the affordances of objects… rather than by the patient's
plan" — no plan of the patient's at all. Yet the original sentence led with
predictive decoders, the weaker analogue. **Resolution**: analogy explicitly
scoped ("the biological analogue of the passive case specifically"), with the
disanalogy stated rather than glossed. This strengthened the paragraph — the
contrast now does argumentative work instead of being a latent objection.

### Counterarguments Considered

- *"The load-bearing closing claim is unsupported"* — checked and **rejected**.
  "In neither does the missing ingredient show up in the movement's competence. It
  shows up only in the absence of the agency signal" is consistent with the
  article's own §"The Comparator Account, Conceded in Full": Assal et al. 2007
  found involuntary movements with isolated M1 activation and no premotor
  preparatory activity — competence preserved, authorship precursor absent. The
  claim is exactly what the conceded comparator account predicts. No change.

### Citation Ledger (§2.4)

Only the new cite was in scope. Verified at the **publisher of record** — the
Springer PDF's own running header, not an aggregator.

- Steinert, S., Bublitz, C., Jox, R., & Friedrich, O. (2019). *Doing Things with
  Thoughts: Brain-Computer Interfaces and Disembodied Agency*. *Philosophy &
  Technology*, 32(3), 457–482. `10.1007/s13347-018-0308-4` — **state:
  real-correct on every metadata field; reading corrected (see criticals 1 and 2)**.

⚠️ **The year 2019 is correct — do not "fix" it to 2018.** The PDF header reads
"Philos. Technol. (2019) 32:457–482" with "Published online: 10 March 2018". This
is an online-first/print split: Crossref `issued`, Unpaywall `published_date`, and
OpenAlex `publication_year` all report **2018-03-10** (the online-first date),
while the print issue carrying pages 457–482 is **2019**. A citing paper's
reference list independently renders it "Philos Technol. 2019;32(3):457–82".
Reading `issued` as the print year is exactly the error this note exists to
prevent. **Left alone this pass; DOI left alone.**

OpenAlex `W2789829182` carries `mag` id 2789829182, proving the record predates
2022 — LLM contamination of the metadata is ruled out for free.

Retrieval note for future passes: `link.springer.com` serves a "Client Challenge"
bot block (3038-byte HTML) for both the article and `/content/pdf/` paths, and
`d-nb.info` 403s. **`rd.springer.com/content/pdf/10.1007/s13347-018-0308-4.pdf`
serves the real 613KB PDF.** Every OA index (Unpaywall, Semantic Scholar) points
only at the blocked host, so the paper looks unretrievable when it is not.

All four quotes now in the article were grep-verified against the extracted raw
text at positive offsets (39109, 47439, 38990, 14988) — not against the research
note, which is *upstream* of the original wording and therefore ratifies rather
than tests it. That upstream check is in fact what first flagged the defect: the
note quotes "are no actions" and "may initiate", so the article had strengthened
both claims relative to its own source note.

### Reasoning-Mode Classification (§2.6)

Engagement with the comparator/forward-model account (Frith, Blakemore & Wolpert;
Goldberg; Assal): **Mode Three — framework-boundary marking**, unchanged from the
2026-07-16 and 2026-08-04 classifications. Steinert et al. are used as a
*source*, not an opponent — no engagement mode applies. Grep for all forbidden
editor-vocabulary labels returned offset −1 on every one.

## Optimistic Analysis Summary

### Strengths Preserved

- The dual-reading discipline in the lead ("compatible with two readings that
  predict the same picture") and the titled full-strength concession section —
  untouched, and the reason this article has twice been called a model of the
  Map's calibration discipline.
- The act / limb / person series (anarchic hand → alien hand → Capgras) with its
  explicit no-shared-pathway disclaimer.
- The withheld/fabricated bracketing against the left-hemisphere interpreter.
- The framework-relative caution at the end of §"The Interface Reading", which is
  what made critical 2 visible by contrast.

### Enhancements Made

- The BCI paragraph now carries the passive/predictive distinction as an explicit
  contrast, which sharpens rather than dilutes the interface reading: the
  engineered case that *most* resembles anarchic hand is the one with no
  intention at all, and saying so makes the "execution pathway without the
  volitional hand-off" structure precise.

### Cross-links Added

None. The one wikilink in the paragraph
(`[[brain-computer-interfaces-and-the-interface-boundary#whose-action-is-a-decoded-movement]]`)
already existed and already resolves — the anchor matches the live heading
"## Whose Action Is a Decoded Movement?". No new link was introduced, so no
resolution risk was taken.

## Pre-08-21 Body

**Nothing found.** As expected and as the brief predicted: the pre-08-21 body has
a dedicated 2026-08-04 deep review with a complete citation ledger, plus
[[optimistic-2026-08-02-single-case-dissociation-cluster]] which treats this
article as a primary subject (16 mentions). No superlative claims detected
(`find_superlative_claims` → 0), so the currency sweep was a no-op. No findings
were manufactured here.

## Remaining Items

None. The two criticals and the one medium were all fixed in this pass; length
had 502 words of headroom so nothing had to be traded (2498 → 2605, `ok`).

## Stability Notes

- **The comparator account will always reach the same clinical facts on
  physicalist premises.** The article concedes this in a titled section and
  locates the disagreement at "what the mechanism is a mechanism *of*." This is
  bedrock, not a defect. Third review to record it. Do not re-flag.
- **Assal et al. 2007 is a right-parietal ("alien") case cited for a general
  involuntary-movement neural correlate.** Deliberate and faithful — the finding
  cited is the missing premotor precursor, not the lesion taxonomy. Fourth review
  to reach this conclusion. Do not re-flag as a taxonomy mismatch.
- **`anchoring_audit_exempt: true` is correct.** Calibration here is phrasal, so
  the modal-hedge counter reads ~0/kw despite exemplary calibration. Do not pad.
- **The Steinert 2019/2018 year split is settled** — see the ledger warning above.
  Any future flag proposing 2018 should be closed by reading the PDF header, not
  Crossref `issued`.
- **Lesson worth generalising**: this defect existed because the paragraph was
  inserted into a *secondary* host by a fold aimed at a different article. The
  primary host got the modal right; the drive-by paragraph did not, and nothing
  reviewed it for 19 days. Secondary-host insertions from a fold deserve the same
  source-fidelity pass as the primary target.
