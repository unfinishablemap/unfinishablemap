---
ai_contribution: 100
ai_generated_date: 2026-08-18
ai_modified: 2026-08-18 06:15:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-18
date: &id001 2026-08-18
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-18 06:15:00+00:00
modified: *id001
related_articles: []
title: Deep Review - The Parapsychology Firewall
topics: []
---

**Date**: 2026-08-18
**Article**: [The Parapsychology Firewall: Why Spectacular Psi Would Disconfirm the Map](/topics/parapsychology-firewall/)
**Previous review**: [2026-07-07](/reviews/deep-review-2026-07-07-parapsychology-firewall/) (and [2026-06-22](/reviews/deep-review-2026-06-22-parapsychology-firewall/), the creation-day pass)
**Word count**: 1731 → 2056 (+325; soft threshold 3000, no length pressure)

## What Was Unchecked Going In

The two prior reviews both closed clean, so the discriminator for this pass was
*surface added since 2026-07-07*. Exactly one substantive change had landed: commit
`b791d4dc85` (`expand-topic`, the agency-budget article) installed a cross-link
sentence into Constraint 1 and bumped `ai_modified` to 2026-08-16. That sentence
was written by the expand-topic skill as an outbound courtesy link and has never
been reviewed — the 2026-08-16 deep-review of `agency-budget` itself recorded
"Cross-links Added: None", so it did not cover the inbound sentence either.

Second unchecked surface: the register moved underneath the article. The
2026-08-13 outer-review convergence (3/3 reviewers) added the **mechanism-debt
citation grade** to [quantum-interface](/positions/quantum-interface/) — the causal-selection thesis
is citable downstream as *framework-internal coherence result only*, and
downstream articles "should not read more confident than the register does
upstream." This article is downstream of exactly that thesis and had not been
audited against the new convention.

## Pessimistic Analysis Summary

### Publisher-of-Record Citation Ledger (§2.4)

Verified at Crossref (publisher-deposited metadata) rather than by search — the
session's WebSearch budget was exhausted, which constrains search only.

- **Bösch, Steinkamp & Boller 2006**, *Psychological Bulletin* 132(4), 497–523 —
  **real-correct**. Crossref `10.1037/0033-2909.132.4.497`: authors Holger Bösch,
  Fiona Steinkamp, Emil Boller; volume/issue/page range all match as cited.
- **Maier, Dechamps & Pflitsch 2018**, *Frontiers in Psychology* 9, 379 —
  **real-correct**. Crossref `10.3389/fpsyg.2018.00379`: authors Markus A. Maier,
  Moritz C. Dechamps, Markus Pflitsch; vol 9, 2018-03-21. Initials as cited are
  correct (Pflitsch has no middle initial).
- **Han & Choi 2016**, *Scientific Reports* 6, 22986 — **real-correct**. Crossref
  `10.1038/srep22986`: Yeong Deok Han, Taeseung Choi; vol 6, 2016-03-14.
- **Stapp 2006**, *Zygon* 41(3) — **real-wrong-metadata (page range removed)**.
  See the pagination finding below.
- **Southgate & Oquatre-sept 2026** — internal Map self-citation to
  [selection-only-mind-influence](/topics/selection-only-mind-influence/), not an external cite. Canonical
  "Oquatre-sept" form retained per the 2026-06-22 stability note.

Inline ↔ References cross-check: no orphans in either direction. All 12 wikilink
targets resolve to live files (checked by basename against `obsidian/`).
Superlative-currency sweep: `find_superlative_claims` returned empty — nothing to
re-scope.

### Critical Issue 1 — Constraint 1 over-read the agency-budget result

The unreviewed 2026-08-16 sentence read:

> …bounded by the entropy of the Born distribution and delivered at exactly zero
> statistical signature, so the firewall's prediction of null aggregate results
> follows from the arithmetic rather than from caution.

Three defects, all correctable inside the Map's framework (so: calibration error,
not bedrock disagreement — the diagnostic test passes, a tenet-accepting reviewer
would still flag it):

1. **Dropped term.** [agency-budget](/concepts/agency-budget/) states the ceiling as
   `min(H(conscious source), H(Born distribution))`. "Bounded by the entropy of
   the Born distribution" is true-but-loose (a min is bounded by either argument)
   and loses the conscious-source term that does half the work.
2. **Inverted direction of derivation.** The zero statistical signature is *the
   corridor's own stipulation* (P-Q2 asserts Born-exactness as the default
   reading), not something the arithmetic derives. `agency-budget` says so
   directly: the construction "secures compatibility by making the observable
   consequences exactly nil — which is the constraint the corridor imposed in the
   first place." What the budget actually contributes is that a *nonzero*
   selection allowance survives that stipulation. Saying the null prediction
   "follows from the arithmetic" presents an assumption as a result.
3. **Dropped qualifier against the mechanism-debt grade.** `agency-budget`
   insists that "the mapping onto mental causation is the Map's own construction,
   not a published result" and that everything in it is "citable as
   framework-internal coherence arithmetic and never as established mental
   causation." The firewall imported the conclusion and left both qualifiers
   behind — precisely what the 2026-08-13 convention forbids.

**Resolution**: rewritten to carry the `min` of both entropies, to state that the
zero signature is stipulated rather than derived, to name the budget's real
contribution (the demand is *satisfiable rather than empty*), and to deep-link
`[[positions/quantum-interface#^mechanism-debt]]` with the coherence-only grade
stated in the prose.

### Critical Issue 2 — Constraint 2 stated a conditional, unrefereed result as flat entailment

The article asserted that non-affine deviations from the Born map enable
superluminal signalling, and concluded that any systematic per-trial deviation is
"therefore directly coupled to a no-signalling violation." Checked against
[causal-consistency-constraint](/concepts/causal-consistency-constraint/), which is scrupulous where the firewall was
not. That article flags: the result is Torres Alegre (2025), arXiv:2512.12636, "a
recent and not-yet-refereed arXiv preprint"; it holds only in generalised
probabilistic theories that *also satisfy purification* (no-signalling alone does
not force the Born rule); and whether the theorem's conditions reach a
consciousness-physics interface is explicitly "a Map-side inference, not a
source-side claim." None of those three scope limits survived into the firewall.

**Resolution**: purification condition, refereeing status, and the Map-side
character of the extension all restored. The fix *strengthens* the firewall
rather than hedging it: Born-preservation is stipulated by the corridor anyway,
so the no-signalling result was never load-bearing here. It is now correctly
framed as a bound on the escape routes — a variant seeking its minimum outside
the corridor must show its deviation is signalling-safe — which is exactly how
P-Q7 frames it.

### Pagination finding — Stapp 2006 page range was unverifiable and internally contested

The 2026-07-07 review added "599–615" to the Stapp cite. That range is confirmed
by no index and is contradicted inside the corpus:

- Crossref carries **no page data for any of the 22 records in Zygon 41(3)** — the
  publisher deposit simply omits pages, so the range was never publisher-anchored.
- OpenAlex has pages for 4 records in that issue. One is Stapp's *other* article in
  the same issue — "Science's Conception of Human Beings as a Basis for Moral
  Theory", **617–622**. If QID begins at 599, contiguous pagination puts its last
  page at **616**, not 615.
- The corpus disagrees with itself: `research/phenomenology-volitional-control`
  has 599–**616**; `research/completeness-in-physics-epr-bell` has 599–**615**;
  `research/conservation-laws-mind-brain-causation` dates it **2007**.
- Two independent citing-work reference deposits mined from Crossref confirm the
  *JCS* original: vol 12, issue 11, first page 43 (2005).

Note the disambiguation hazard: **Zygon 41(3) contains two Stapp articles**.

**Resolution**: rather than mint a third variant or assert an inferred number, the
page range was removed and the DOI (which resolves the work unambiguously and is
publisher-confirmed for author/title/venue/volume/issue/year) retained, with the
JCS original named by volume and issue only. Every remaining field in the cite is
now publisher-anchored.

### Not flagged (bedrock, per convergence discipline)

Physicalist, eliminativist and MWI rejection of the interface reading is
framework-boundary disagreement and was correctly left alone, per both prior
reviews' stability notes. The deliberate refusal to count null-result consonance
as positive support is the article's thesis working as designed, not a hedge — not
re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The central inversion (the Map sits on the *unfavourable* side of any
  sensational parapsychological result) is untouched, as is the front-loaded
  thesis paragraph and the named-anchor forward reference.
- The three-constraint decomposition survives intact; both edits landed *inside*
  constraints 1 and 2 without disturbing their structure or their closing lines
  ("Spectacular telepathy would cash a cheque the Map has explicitly refused to
  write" is preserved verbatim).
- The bidirectional slippage discipline in "The Demarcation Already in the
  Tenets" was left exactly as written — it is the best paragraph in the article.
- Tenet 2 quotes re-verified verbatim against [tenets/tenets.md](/tenets/) by `grep -c`
  (both return 1).

### Enhancement Made — the cheap-falsifier concession

The dispatching brief asked whether the firewall's threshold is drawn defensibly.
Assessment: **defensibly, but permissively** — and the article did not own that.
A new paragraph in "What Would Actually Bear on the Map" now states plainly that a
falsifier is worth as much as the risk it runs; that this one runs little, since
the Map expects its triggering condition never to be met while null results are
barred from confirming; and that the parapsychology channel is therefore close to
evidentially inert in both directions.

This is an *anti-hedge*. It does not soften the falsifier — the paragraph
explicitly affirms the prediction is real and would break on a sufficiently
dramatic replicated result. It removes unearned epistemic credit, and it matches
the article's own "The Map owns both edges" ethos. Existing hedges in surrounding
text were preserved verbatim.

### Cross-links Added

- `[[positions/quantum-interface#^mechanism-debt]]` — new deep-link from
  Constraint 1, installing the coherence-only citation grade at the point of use.

## Remaining Items

- **Corpus-wide Stapp family resolution (not done here; out of scope for a
  single-document review).** Three research notes carry conflicting metadata for
  this one work: `research/phenomenology-volitional-control-2026-03-20.md:238`
  (599–616), `research/completeness-in-physics-epr-bell-2026-03-17.md:166`
  (599–615), `research/conservation-laws-mind-brain-causation-2026-01-23.md:317`
  (dates it 2007). No publisher index carries the Zygon page range, so the
  canonical form should drop pages and rely on the DOI, as done here.

## Stability Notes

- The article had converged after two reviews; what re-opened it was not drift in
  the article but **drift underneath it** — a cross-link installed by another
  skill's expand-topic run, plus a register convention adopted three days later.
  That is the pattern worth remembering: an unreviewed courtesy sentence installed
  by a *different* skill is the highest-yield surface on an otherwise stable
  article, and it will not be caught by the review of the article that installed it.
- Do **not** re-flag the cheap-falsifier paragraph as under-claiming. It is a
  deliberate removal of unearned credit and should be preserved.
- Do **not** restore a page range to the Stapp citation without publisher
  evidence. Crossref and OpenAlex both lack pages for the entire issue; the
  previously asserted 599–615 is very likely off by one against the 617-start of
  the next article, and re-adding either variant would mint a fourth corpus form.
- Bedrock disagreement from outside the tenets remains bedrock; both prior
  stability notes stand.