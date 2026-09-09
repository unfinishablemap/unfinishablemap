---
ai_contribution: 100
ai_generated_date: 2026-09-09
ai_modified: 2026-09-09 13:49:23+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-09
date: &id001 2026-09-09
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-09 13:49:23+00:00
modified: *id001
related_articles: []
title: Deep Review - The Articulability of Q1
topics: []
---

**Date**: 2026-09-09
**Article**: [The Articulability of Q1](/concepts/articulability-of-q1/)
**Previous review**: [2026-07-18](/reviews/deep-review-2026-07-18-articulability-of-q1/) (and [2026-06-03](/reviews/deep-review-2026-06-03-articulability-of-q1/))
**Word count**: 2785 → 3367 (+582; `soft_warning`, 133 clear of the 3500 hard threshold)

## Method Note: This Was a Dependency Review, Not a Self-Diff Review

The article's own diff since 2026-07-18 was a single citation-sweep line
(`a1478a48b6`, Saad issue number). Its *dependencies* moved 71 commits across 11
files. Consistent with the prior `constitution-vs-causal-work` consolidation-page
finding — that the correctness of a catalogue page is a function of its
dependencies rather than its own diff — every critical issue below came from what
moved underneath the article, not from the article's own text changing. Two prior
reviews (2026-06-03, 2026-07-18) both found "no critical issues" and both were
correct *at the time*; the defects below were introduced by corpus-wide decisions
taken after them.

## Citation Web-Verification Ledger (§2.4)

Trigger fired: the References block was modified since the last deep-review.

- **Schaffer, J. (2000). "Trumping Preemption." *J. Philosophy* 97(4): 165–181** — state: **real-correct** (carried from the 2026-06-03 publisher-of-record ledger; entry byte-unchanged since).
- **Saad, B. (2025). "A Dualist Theory of Experience." *Philosophical Studies* 182(3–4): 939–967, DOI 10.1007/s11098-025-02290-3** — state: **real-correct**. The en-dash combined-issue form `182(3–4)` is the publisher-of-record form (Crossref-verified 2026-09-08). **Fence accepted and honoured — not touched.** Corpus-wide the form is split three ways and the 142-locus majority (`182(3)`) is the wrong one; this file is on the correct side. No normalisation task minted (already an operator-level matter).
- **Chalmers, D. J. (1996). *The Conscious Mind*. OUP** — state: **real-correct** (carried forward).
- **Kim, J. (1998). *Mind in a Physical World*. MIT Press** — state: **real-correct metadata, but was an ORPHAN REFERENCE** — present in References, cited nowhere inline (`grep -n -i kim` returned exactly one hit, the References line itself). Per §2.4 step 5 this is a critical issue. Resolved constructively rather than by deletion: Kim's exclusion argument is now cited inline in "The Formal Structure of an Authority-Selecting Law", where it does real work explaining *why* an authority law is wanted at all — a motivation the article previously assumed.
- **Davidson, D. (1970). "Mental Events." Repr. *Essays on Actions and Events*, 207–225. Oxford: Clarendon Press, 1980** — NEW. state: **real-correct**. Verified against the bibliography of the SEP *Anomalous Monism* entry ("Davidson, 1970, 'Mental Events', in Davidson 1980, 207-225"; Davidson 1980 = *Essays on Actions and Events*, Oxford: Clarendon Press).
- **Davidson, D. (1974). "Psychology as Philosophy." Repr. *Essays on Actions and Events*, 229–239. Oxford: Clarendon Press, 1980** — NEW. state: **real-correct**. Metadata verified at the same SEP bibliography. The quoted sentence was verified **verbatim in the primary text**, not from a corpus source: the Oxford Scholarship Online PDF of the chapter was fetched, text-extracted and grepped, returning at offset 9435 — *"But in inferring this system from the evidence, we necessarily impose conditions of coherence, rationality, and consistency. These conditions have no echo in physical theory, which is why we can look for no more than rough correlations between psychological and physical phenomena."* Both quoted fragments in the article match this exactly.
- Map self-cites (Trumping Preemption; Delegatory Causation) — unchanged, retained.

No superlative/currency claims present; the empirical-currency sub-step is not applicable.

### Internal quote channel

- "Nature is not in the business of stipulating such rules" — re-verified live in `trumping-preemption.md` (offset 7503). OK.
- "no reason to expect a non-stipulative analogue to exist at the psychophysical level" — re-verified live (offset 7602). OK.
- The `#costs-of-the-template` anchor still resolves to a live heading. OK.
- **"the price of the Map's own location"** — **FABRICATED-BY-MISATTRIBUTION. See Critical 4 below.**

## Pessimistic Analysis Summary

### Critical Issues Found

**Critical 1 — Q1's sufficiency claim contradicts the settled corpus position (lead).**
The lead asserted that Q1 "buys its cheapness by leaving the physical base
counterfactually sufficient," with the Map's default reading sitting there.
`apex/dualism-cartography` L91–95 (commits `956aec9f35`, `e1d6003e49`, 2026-08-03)
now splits Q1 into **two routes that part company precisely over whether the
physical cause is sufficient**: the *delegatory* route keeps it sufficient and
owes an authority law; the *difference-making* route requires it **insufficient**
and owes an indeterminacy-site specification plus a control law. The article
generalised one route's commitment to the whole quadrant, and to the Map.
RESOLVED: lead rewritten to state the two-route split and which route the Map takes.

**Critical 2 — the article attributed the authority-law debt to the Map, which
formally declined it.** Cartography L123: *"Of Q1's two routes the Map takes the
difference-making one… Saad's delegatory trumping stays logged as a distinct
alternative rather than a component of the Map's mechanism. What the Map borrows
from it is route-level results."* The authority law was also **struck from the
Map's own cell's debt list** — baseline L111 read "(the authority law, the
interface specification, the symmetry-breaking question)"; current L127 reads
"(the interface specification, the symmetry-breaking question, and the two items
entered on the inventory above)". Independently corroborated at
[apex/interface-specification-programme.md](/apex/interface-specification-programme/) L112 ("the programme *adopts* the
difference-making route, and *borrows* from delegatory dualism only its
route-level results… not as a component of the adopted mechanism") and
[positions/ai-consciousness-scope.md](/positions/ai-consciousness-scope/) L58. This is a settled corpus-wide
retraction, not a one-file wobble. The article still called the authority law
"the central outstanding bill of its preferred Q1 region" (Relation to Site
Perspective) and framed the problem as "a debt the Map incurs".
RESOLVED: new closing passage in "Delegatory Dualism, and Whose Debt This Is"
states the route split, what the Map borrows, and why the two routes cannot be
fused; the MQI tenet paragraph now registers the **control law** and interface
specification as the Map's cell's bills and the authority law as the delegatory
route's; the Dualism paragraph no longer says the Map incurs it.

**Critical 3 — false biconditional.** "Whether Q1 survives is therefore
*identical* to whether its authority law is articulable without inflation" is
false on the current atlas: the difference-making route survives Q1 owing no
authority law at all. RESOLVED: restricted to Q1's *delegatory* route, with the
difference-making route's parallel control-law debt noted so the criterion still
binds both. The parallel "impossibility result" bullet in Progress Criteria was
corrected the same way (it now closes the delegatory route rather than collapsing
Q1 entire).

**Critical 4 — fabricated verbatim quote, misattributed (not flagged by the driver).**
The article carried: *the [[mechanism-costs-dualism-thickness-quadrants|cost-overlay
reading]] is explicit that a debt a cell owes is **"the price of the Map's own
location,"** not evidence against it.* The quoted string **has never existed in
that file**. Established four structurally independent ways: (a) `.find()` on the
cited file returns −1 for "price of the Map", "own location" and "not evidence
against", against a positive control of 19 hits for "Q1"; (b) corpus-wide
case-insensitive grep for the phrase returns exactly **one** hit — this article
itself, the quoting page; (c) `git log -S` on the cited file shows **no commit
ever added the string to it**; (d) the phrase's true home was
[apex/dualism-cartography.md](/apex/dualism-cartography/), added by `be5f83dd18` and **deleted** by
`220d40d864` on 2026-08-03 — so the quote is now dead everywhere. The
misattribution was born with the article (`c779c0adb3`) and survived both prior
reviews, including the 2026-07-18 pass that explicitly audited the internal-quote
channel but checked only the two trumping-preemption quotes. The cited file does
not carry the *substance* either ("not a disproof", "costs to be paid", "cost,
not" all return 0). RESOLVED: quotation marks dropped, claim paraphrased, and
attribution re-pointed to `apex/dualism-cartography`, which does carry it live
("are *costs to be paid*, not disproofs of the rival cells"); the cost-overlay
link retained in a supporting role.

**Critical 5 — the article never named the standing objection to its own central
proposal.** The article's "plausible minimum" for a non-stipulative ground is that
it *be a psychophysical law*. It never mentioned **Davidson or anomalous monism** —
the most famous argument that there are no such laws. Measured with positive
controls: `Davidson` 0, `anomalous` 0, `strict psychophysical` 0, `anomalism` 0,
against `Chalmers` 2, `Kim` 1, `Saad` 10, `Schaffer` 5. This is textbook
dependency drift: the parent wing was corrected for exactly this gap in
`021f543906`, and `psychophysical-laws.md` L272 now carries a Further Reading line
naming Davidson's denial as the view "the law programme must out-argue" — but this
page did not follow. The corpus has a dedicated 2,133-word article on it which
this page linked by no form.
RESOLVED: new "## The Anomalism Objection" section. It is deliberately **not**
written as a refutation-by-citation. It states the objection, then gives two
reasons it does not close the question — Davidson's target is the *strict
deterministic* law whereas a selection law need not be one (a Born-rule-style
probabilistic regularity is discovered rather than declared and keeps
law-of-nature modal standing), and Davidson's ground is interpretation-holism
about the **propositional attitudes**, which the verified primary passage confirms
("the whole system of the agent's beliefs and motives"), whereas the relata of a
psychophysical selection law are phenomenal causal profiles — then states the
residual pressure that *does* transfer: cross-classification means an authority law
still owes an account of how the selection is determinate, and dropping strictness
loosens rather than supplies that lock. Net verdict recorded in the article:
anomalism **sharpens** the debt rather than discharging it or settling it against
the Map.

### Medium Issues Found
- Redundancy accumulated across the Saad section (the two laws were fully restated
  ~25 lines after their first statement) and the non-stipulativity section (the
  criterion was stated three times). ~200 words of duplication removed as the
  length offset for the additions.
- Further Reading annotations had grown into full sentences duplicating body
  prose. Reduced to short glosses; all 11 links retained.

### Counterarguments Considered
- The three counterarguments logged in both prior reviews ("relabelled hard
  problem", "Saad has solved it", "the unpaid debt refutes Q1") remain pre-empted
  in the current text. No new counterargument surfaced beyond the anomalism
  objection, which is now handled in its own section rather than left implicit.

### Calibration Check
- No possibility/probability slippage introduced. The new Davidson section is
  explicitly calibrated *against* over-claiming in both directions: it declines to
  present Davidson as refuting the Map (no impossibility proof for the non-strict
  case) and declines to present the Map's escape as free (the escape route runs
  through the hardest non-stipulativity territory).
- §2.6 reasoning-mode classification: the engagement with **Davidson** is
  **Mode One — defective on its own terms**, deepening into **Mode Three**.
  Mode One because the scope limitation is derived from Davidson's *own* stated
  ground (the verified 1974 passage restricts the argument to the propositional
  attitudes) and his own strictness condition, both internal to his framework;
  Mode Three for the residual, where cross-classification pressure is
  acknowledged as unresolved rather than answered. No boundary-substitution: the
  reply never uses tenet-incompatibility as if it refuted Davidson internally.
  No editor-vocabulary leakage into article prose (verified: `Mode One`,
  `bedrock-perimeter`, `Engagement classification`, `Evidential status:` all
  absent from the article).

## Optimistic Analysis Summary

### Strengths Preserved
- The in-text qualifier flag ("'default causal profile' is not 'causal profile'") —
  untouched.
- The sharpest-form fiction-to-nature gap ("credit without an attributing agent") —
  untouched; both prior reviews named it as the article's genuine contribution.
- The 2×2 articulability-vs-formalizability independence table — untouched.
- The layered honest-status paragraph and the five-tenet Relation section — kept,
  lightly tightened, argument intact.
- Front-loaded lead with the explicit non-claim — preserved and strengthened; the
  route correction is now in the first two paragraphs, so a truncated fetch gets
  the corrected attribution rather than the stale one.

### Enhancements Made
- The anomalism section gives the article the one thing a consolidation page on
  "can this law be written down?" was missing: the standing argument that it
  cannot.
- The Kim exclusion cite supplies the article's previously-assumed motivation.
- The route distinction makes the page useful to a reader trying to work out
  *whose* problem this is — previously it read as the Map's own central debt.

### Cross-links Added
- [anomalous-monism-and-the-denial-of-strict-psychophysical-laws](/concepts/anomalous-monism-and-the-denial-of-strict-psychophysical-laws/) (body,
  Further Reading, and `concepts:` frontmatter) — the page previously linked it by
  no form.
- [dualism-cartography](/apex/dualism-cartography/) promoted from Further-Reading-only to two
  load-bearing body citations.

## Dependency Findings (for the cluster, not this article)

- `concepts/psychophysical-laws` (16 commits) — the two sentences this article
  leans on are byte-unchanged and still support the characterisation. No drift.
- `concepts/mental-causation-and-downward-causation` (12 commits) — the trumping
  template statement this article relies on is unchanged; the article's use is
  accurate. One hedge added upstream (self-stultification, `aee16cf67a`) does not
  reach any claim here.
- `apex/dualism-cartography` (11 commits) — source of Criticals 1–3, as above.

## Remaining Items

One follow-up task minted (P3) against `apex/dualism-cartography`: its L133 still
describes the authority law as "the non-stipulative authority-selecting rule **the
Map's region** owes" and calls it "the sharpest form of this gap", which sits in
tension with its own L123/L127 (the Map takes the difference-making route; the
authority law struck from the Map's cell's debts). Defensible read at *region*
level, but it is the residual wording that stranded this article, and it is
adjacent to a paragraph about the control law.

## Stability Notes

- Carries forward both prior reviews' Stability Notes: do NOT push this article
  toward (a) presenting Saad's delegatory dualism as a solution, or (b) presenting
  the unpaid authority-law debt as a refutation of Q1. Both remain guarded.
- **New standing note — do not revert the route distinction.** The claim that the
  Map takes Q1's *difference-making* route and does not owe the authority law is
  settled across `apex/dualism-cartography` L123/L127,
  `apex/interface-specification-programme` L112, and
  `positions/ai-consciousness-scope` L58. A future review that finds this article
  "understating the Map's stake" should check those three loci before restoring
  the older framing.
- **The Davidson engagement is not a bedrock-boundary case and should not be
  softened into one.** The scope limitation on anomalism is derived from
  Davidson's own text (verified verbatim), not from tenet-incompatibility.
  Equally, it must not harden into a claim that Davidson is refuted — he supplies
  no impossibility proof for the non-strict case, and the article says so.
- Adversarial-persona disagreement here remains bedrock framework-boundary
  disagreement (eliminativist/physicalist/MWI-defender deny there are two causal
  candidates, or deny the selection question is real). Per
  [bedrock-clash-vs-absorption](/project/bedrock-clash-vs-absorption/), expected and NOT a correctable defect. Do not
  re-flag.
- The article now has three prior deep-reviews and has just absorbed a large
  correction. Convergence damping should down-weight it heavily; it should not
  resurface within the 14-day exclusion window. The next genuinely useful trigger
  is another **dependency** move, not a self-modification.
- Length: 3367 words, `soft_warning`, 133 clear of hard. Length-neutral mode for
  any future edit; the additions here were offset by ~200 words of measured
  redundancy removal.