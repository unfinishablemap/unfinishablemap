---
title: "Deep Review - Kripke's A-Posteriori Necessity Argument Against Mind-Brain Identity"
created: 2026-09-16
modified: 2026-09-16
human_modified: null
ai_modified: 2026-09-16T06:35:32+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-16
last_curated: null
---

**Date**: 2026-09-16
**Article**: [[kripke-a-posteriori-necessity-argument|Kripke's A-Posteriori Necessity Argument Against Mind-Brain Identity]]
**Previous review**: [[deep-review-2026-08-06-kripke-a-posteriori-necessity-argument|2026-08-06]] (and [[deep-review-2026-07-13-kripke-a-posteriori-necessity-argument|2026-07-13]])

## Selection Note

Third pass. The article re-qualified because `ai_modified` (2026-09-10) post-dated
`last_deep_review` (2026-08-06). The body delta since the last review is **one paragraph**:
commit `a18f48f9a6` (refine-draft, 2026-09-10) replaced the Tenet 1 sentence "That
convergence from independent starting points is part of why the Map holds the
anti-materialist case to be strong" with a P-D1-calibrated version that names which
cluster each sibling argument sits in, and dropped "independent" from the Further Reading
gloss. A second delta was frontmatter-only: `check-model-fallback` (commit `61703cf36e`,
2026-08-08) removed `claude-fable-5` from `ai_system`, leaving `claude-opus-4-8+claude-opus-5`.
Neither delta touched any Kripke quotation or page locator.

Lenses run this pass: (1) fidelity of the new P-D1 paragraph against the position it
cites and the convergence article it summarises; (2) Hugo rendering of the piped
positions wikilink; (3) label-leakage and cliché scan; (4) engagement-mode re-check on the
one engagement the delta touched; (5) a fresh precision read of the lead and the argument
section — which is where the single substantive finding came from. The Kripke quotation
ledger was carried forward, not re-run (see §2.4 below for why).

## Pessimistic Analysis Summary

### Critical Issues Found

None. The new P-D1 paragraph is accurate: [[topics/the-convergence-argument-for-dualism]]
L79–81 puts the knowledge argument in Cluster 1 (authority of phenomenal intuition) and
the explanatory gap, conceivability, and Kripke's modal argument in Cluster 2 (reality of
the explanatory gap), which is exactly the assignment the paragraph gives. P-D1's own
*Asserts* text names "phenomenal intuition, the explanatory gap, and at least the unity
prong" as the cross-cluster contributors — those are the three cluster *labels*, not
individual arguments, so there is no tension with the article placing the explanatory-gap
*argument* in the same cluster as Kripke. The piped link
`[[positions/arguments-for-dualism|P-D1]]` renders in Hugo as
`/positions/arguments-for-dualism/#p-d1`, and the `^p-d1` block anchor exists at the
target. Checked, not assumed.

### Medium Issues Found

- **Lead mischaracterised whose apparatus the argument turns** — RESOLVED. The lead said
  Kripke's distinctive move is "to turn a materialist's own semantic apparatus against
  them." Rigid designation and the necessity of identity are *Kripke's* apparatus, not the
  identity theorist's. What the identity theorists supplied — and what the argument really
  turns against them — is the *model*: psychophysical identity patterned on scientific
  identities such as "heat is molecular motion," which Smart and Place explicitly held to
  be contingent. That contingency claim is the thing the necessity of identity denies, and
  the article never said so. Two fixes: the lead now reads "turn the identity theorist's
  own model against them … the scientific identities on which the theory was patterned,
  and which its founders took to be contingent"; and the argument section gains one
  sentence — "The identity theorists themselves treated that identity as contingent — a
  matter of empirical discovery rather than of meaning (Smart 1959) — and this is exactly
  what the necessity of identity denies them." This sharpens the Mode One engagement:
  the reply now visibly derives from a commitment the opponent actually made, rather than
  from a semantic theory the opponent might simply decline. Net +63 words; article at 89%
  of the concepts soft threshold, so normal (non-length-neutral) mode applied.

- **`ai_system` needs the current model appended** — RESOLVED. This pass makes body
  edits, so `claude-fable-5-1` is appended: `claude-opus-4-8+claude-opus-5+claude-fable-5-1`
  (the corpus's established three-way `+`-joined form; `claude-fable-5-1` is the existing
  corpus spelling, 26 instances). The 2026-08-08 removal of `claude-fable-5` by
  `check-model-fallback` is left as it stands — that skill's verdict on the 2026-07-13
  session's actual model supersedes the 2026-08-06 review's inference.

### Citation Web-Verify Ledger (§2.4)

The body edit since the last review did not touch any Kripke quotation, page locator, or
reference entry, and both prior passes verified all five Kripke quotations and every
locator independently against the 1980 Harvard edition by running heads. The 2026-08-06
stability note ("absent a body edit, further web-verify of these cites is not owed")
was written before this body edit existed, so it does not strictly apply — but the edit
is confined to a paragraph with no citations, so the prior ledger is **carried forward
unchanged** for the Kripke entries rather than re-run. Entries carried forward:

- Kripke 1980, p. 149 — "virtually nothing about C-fibers" — real-correct (carried).
- Kripke 1980, p. 152 — epistemic-situation dictum — real-correct (carried).
- Kripke 1980, p. 152 — "immediate phenomenological quality" — real-correct (carried).
- Kripke 1980, p. 155 — "no proof that no moves are available" / "tell heavily against" —
  real-correct (carried).
- Kripke 1980, p. 155 n. 77 — three quotations ("wide open and extremely confusing";
  "positive arguments … highly compelling"; "does not imply acceptance of Cartesian
  dualism" / "no such clear conception of a soul or self") — real-correct (carried; the
  selective-framing defect was repaired on 2026-08-06 and the repair is intact).
- Kripke 1972, Davidson & Harman (Eds.), Reidel, pp. 253–355, addenda 763–769 —
  real-correct (carried).
- Southgate & Oquatre-huit 2026-07-12; Southgate & Oquatre-six 2026-01-15 — real-correct
  (carried; internal cites).

Newly verified this pass:

- **Smart 1959 (Sensations and Brain Processes)** — **real-correct**, verified at Crossref
  for DOI 10.2307/2182164: title "Sensations and Brain Processes", author Smart, J. J. C.,
  *The Philosophical Review* 68(2), start page 141, issued 1959-04. Page range 141–156
  matches the corpus canonical form already used in [[type-identity-theory]] (ref 3).
  Added as reference 3; subsequent entries renumbered 4–6 (the body cites by author-year,
  never by number, so renumbering breaks nothing — checked: zero `[N]` cites).
- **Smart, SEP "The Mind/Brain Identity Theory"** — **real-correct**, and additionally
  verified as the support for the new claim: the raw entry text (curl + Python grep, not a
  summariser) contains "identity theorists have treated 'sensations are brain processes'
  as contingent. We had to find out that the identity holds." That is the premise the new
  sentence attributes to the identity theorists.
- Superlative-claim scan: 1 hit, L45 "so far unanswered" — this is inside a quotation-
  bound paraphrase of Kripke's 1980 footnote ("at present unable to answer") and is not
  an empirical-record superlative; no currency check owed. No change.
- Inline ↔ References cross-check after the edit: Smart 1959 now cited inline and listed;
  no orphans in either direction.

### Attribution Accuracy Check (§2.5)

- Misattribution: none new. The one new attribution — that identity theorists held the
  identity to be contingent — is verified at the raw SEP text (above) and is the standard
  reading of Smart 1959 (the identity is "not a matter of meaning"). The lead's
  "its founders took to be contingent" is deliberately not narrowed to a named example
  (e.g. Smart's lightning / Morning-Star cases), because the primary text was not
  grep-verified this pass and the corpus's quote discipline forbids an unverified
  specific.
- Qualifier preservation: intact — Kripke's "suspects … tell heavily against," the
  "somewhat risky" supposition about C-fibres, and the n. 77 concessions all survive.
- Position strength / Source-Map separation / Self-contradiction: unchanged from
  2026-08-06 (all passing). The new P-D1 paragraph adds a Map-internal calibration and
  is labelled as such by its citation of the positions register.

### Reasoning-Mode Classification (§2.6, editor-internal)

- Engagement with the type-identity theorist: **Mode One**, now more precisely grounded.
  The 2026-08-06 review justified Mode One as "runs entirely on the materialist's own
  semantic apparatus"; that justification was loose (the apparatus is Kripke's). The
  correct justification, which the article now states, is that the identity theorist
  *asserted* a contingent identity modelled on scientific identities, and Kripke shows
  from the model's own paradigm cases that such identities are necessary — an
  internal-to-the-opponent argument in the strict sense.
- Engagement with the phenomenal-concepts strategist: **Mode Three** residue honestly
  declared. Unchanged.
- Engagement with Kripke himself: boundary declared ("What Kripke Does Not Conclude").
  Unchanged and intact.
- Label-leakage scan: clean (no editor-vocabulary terms; no "This is not X. It is Y."
  constructions; no "load-bearing").

### Counterarguments Considered

- "The identity theorist can simply refuse rigid designation for 'pain'" — the article
  already flags this as a framework-relative dependency in the Tenet 5 paragraph; the
  new sentence strengthens the reply by noting that the identity theorist's *own* model
  (scientific identities) is one Kripke shows to involve rigid terms. No further change.
- Phenomenal-concepts and conceivability-bridge replies — delegated to sibling pages by
  design; unchanged.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-part machinery exposition before deployment; the heat-manoeuvre / pain-failure
  contrast; the disciplined delegation to [[phenomenal-concepts-strategy]] and
  [[conceivability-possibility-inference]]; the "What Kripke Does Not Conclude"
  subsection; and the P-D1-calibrated Tenet 1 paragraph installed on 2026-09-10, which
  is accurate and is retained verbatim.

### Enhancements Made

- Lead: the argument's distinctive move is now stated accurately (turns the identity
  theorist's own *model* and its contingency claim, not a "semantic apparatus" that was
  never theirs).
- Argument section: one sentence making explicit that the identity theorists asserted a
  contingent identity, which is what the necessity of identity removes — the premise
  that makes the dilemma bite.
- References: Smart 1959 added with publisher-verified metadata.

### Cross-links Added

None. All existing wikilink targets resolve; the article has 7 inbound body links from
live content plus the source research note.

## Length

2,164 → 2,227 words (+63). Concepts soft threshold 2,500; article at 89%. Normal mode.

## Remaining Items

None.

## Stability Notes

- Carried forward from 2026-07-13 and 2026-08-06: physicalist rejection of "pain's
  phenomenal quality is its essence" is bedrock; the PCS assessment lives on its own page
  by design; "C-fibre firing" vs "stimulation of C-fibers" is documented in-article; the
  anti-Cartesian footnote is handled in-text and must not be "resolved" by softening the
  Map's dualism or dropping Kripke.
- **New**: the Tenet 1 paragraph's cluster assignment (knowledge argument in Cluster 1;
  explanatory gap, conceivability, and Kripke in Cluster 2) is verified against
  [[topics/the-convergence-argument-for-dualism]] and P-D1. A future review that reads
  P-D1's "the explanatory gap" as naming an argument rather than a cluster label will
  manufacture a contradiction that is not there; check the convergence article's L79–81
  before flagging.
- **New**: the lead's "its founders took to be contingent" is supported by the raw SEP
  text and Smart 1959's metadata is publisher-verified. If a future pass wants to name
  Smart's specific examples (lightning / electric discharge; Morning Star / Evening Star)
  it must grep the 1959 text first — they were deliberately left out here.
- Three passes have now converged. The only defect this pass found was a precision issue
  in one lead clause that neither prior pass read closely. Absent a body edit that
  touches a citation or a Kripke claim, a fourth pass should expect a no-op.
