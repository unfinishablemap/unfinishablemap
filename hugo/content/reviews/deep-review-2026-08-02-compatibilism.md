---
ai_contribution: 100
ai_generated_date: 2026-08-02
ai_modified: 2026-08-02 20:45:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-02
date: &id001 2026-08-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-02 20:45:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Compatibilism
topics: []
---

**Date**: 2026-08-02
**Article**: [Compatibilism](/concepts/compatibilism/)
**Previous review**: [2026-07-13](/reviews/deep-review-2026-07-13-compatibilism/) (create-time cross-review + independent publisher-of-record second pass)

## Scope Determination

The only change to the file since the 2026-07-13 review was a frontmatter `topics:` fill
(commit `afaef915c`, the corpus-wide `topics: []` remediation). **Body and References are
byte-identical to the reviewed state.** Under §2.4's trigger rule ("the body or References
block was modified since the last deep-review"), the publisher-of-record web-verify pass is
**correctly skipped** this cycle: the 07-13 review ran it twice, the second pass with
independent primary-publisher WebSearches and URLs for all ten citations, and no citation
text has changed since.

Rather than re-run a converged lens, this pass applied the two lenses **never previously run
on this article** — §2.6 reasoning-mode classification and the full six-persona pessimistic /
seven-persona optimistic sweep. Clean-validated articles carry defects that each *different*
lens catches, so a fresh lens is worth more than a re-run of a converged one. That held here:
one real internal contradiction surfaced.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Internal contradiction on the natural reading (Relation to Site Perspective).** The
  sentence read: *"The Map takes the emergentist route to face a hard question about whether
  higher-level indeterminism can be genuine if the underlying physics is closed."* The
  intended parse is "takes [the emergentist route] to [face]" — i.e. *regards* emergentism as
  facing that question. But the greedy first-pass reading, "The Map takes the emergentist
  route," asserts the Map **adopts** emergentism. That flatly contradicts the immediately
  preceding clause, which places the Map on the quantum-interface side of the locus dispute
  ("emergent agential-level autonomy (List) **versus** physical influence on quantum outcomes
  (the Map)"), and contradicts the whole article's libertarian framing. For an LLM-first
  audience this is a live misparse, not a stylistic quibble. **Resolution applied**: rewritten
  to *"The emergentist route faces a hard question about whether higher-level indeterminism can
  be genuine if the underlying physics is closed — a question the quantum interface is designed
  to answer at the physical level."* Verified fixed in `obsidian/` and re-synced to `hugo/`
  (the defect was live on the published page).

### Medium Issues Found

- **Taxonomy promise not honoured for the sixth variant.** The organizing-axis section declared
  "Three strategies recur" and then "The variants below are grouped by which strategy they
  take" — but five of six variant headings carry a strategy tag *(reinterpret / bypass /
  relocate)* and the Strawsonian section carries none, with no explanation. The 07-13 review
  noted the outlier was handled *honestly* but did not notice that the article **promises** a
  grouping it then breaks. **Resolution applied**: the framing sentence now closes with the
  outlier explicitly — "closing with Strawson's, which declines the axis altogether and grounds
  responsibility in practice rather than in any reading of the phrase."

- **Editor-voice scaffolding in article prose.** Two passages addressed the corpus's editorial
  state rather than the subject: *"so this variant carries new material"* and *"A mature
  compatibilism page situates itself against this challenge rather than repeating it."* This is
  the same category §2.6 prohibits for engagement labels — editorial vocabulary leaking into
  content. The second also has the article referring to itself in the third person as "a mature
  compatibilism page." **Resolution applied**: both removed. The navigational "no dedicated page
  elsewhere in the lattice" notes were **kept** in both the dispositionalism and
  emergentism sections — those tell a reader this is the canonical treatment, and they are now
  parallel in form.

### Low Issues Found

- `description` was 171 chars, over the 150–160 guideline. Trimmed to 159 (dropped the
  redundant "libertarian", which the body establishes anyway).

### Verified Clean (no action)

- **§2.6 label leakage** — grep for all forbidden editor labels (`direct-refutation-feasible`,
  `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification:`,
  `**Evidential status:**`, etc.): **zero hits**.
- **Corpus-meta claims still true** — the article asserts no dedicated page exists for
  dispositionalism or for Dennett/List. Verified: `Vihvelin` appears only in
  `source-versus-leeway-incompatibilism`, `the-consequence-argument-for-incompatibilism` and
  this article; "Why Free Will Is Real" appears only here. Both claims hold.
  (`consciousness-and-the-metaphysics-of-laws-and-dispositions` is laws-metaphysics, not
  free-will ability-dispositionalism — not a collision.)
- **All 13 wikilink targets resolve**; no bare-slug markdown links; EOF clean (no tool-call
  tag artifact).
- **Style guide** — no "load-bearing", no "This is not X. It is Y." construct.
- **Attribution spot-checks** — Fara 2008 as *co-canonical* new dispositionalist alongside
  Vihvelin is correct (Clarke's 2009 *Mind* critique "The New Dispositionalism" targets exactly
  this pair). Frankfurt's "wanton" / "second-order volitions", Fischer–Ravizza's
  guidance-vs-regulative control and "taking responsibility", Dennett's evitability argument,
  and List's agential-level-indeterminism-with-physical-determinism are all faithfully stated.
  Hume is explicitly flagged in-text as paraphrase, not quotation.
- **Possibility/probability slippage** — none. The article's only empirical claim is the
  PhilPapers figure (date-scoped, twice verified). The dispute is metaphysical throughout.

## §2.6 Reasoning-Mode Classification (first run on this article)

The article replies to five named opponents. No boundary-substitution found — the article
never presents tenet-incompatibility as an in-framework refutation.

- **List** — *Mode One*. The reply raises an internal-to-List problem (whether higher-level
  indeterminism is genuine when the underlying physics is closed), which is the standard
  objection pressed from List's own commitments, not from Tenet 3. Correctly executed; this is
  the sentence whose wording was fixed above.
- **Fischer (semicompatibilism)** — *Mode Three, honestly declared*. The article names it "the
  hardest challenge", concedes it threatens to make the quantum apparatus *unnecessary*, offers
  a partial reply (leeway does work beyond grounding responsibility — it makes deliberation
  about an open future non-illusory), and states the burden is "one the Map carries rather than
  waves away." The available Mode One argument (Pereboom's four-case manipulation argument) is
  correctly **delegated** to [the-manipulation-argument-and-hard-incompatibilism](/topics/the-manipulation-argument-and-hard-incompatibilism/) rather than
  re-derived — legitimate for a hub page.
- **Vihvelin (new dispositionalism)** — *Mode Three*, with the in-framework attack routed to
  [the-consequence-argument-for-incompatibilism](/topics/the-consequence-argument-for-incompatibilism/). See Remaining Items.
- **Frankfurt / Strawson** — descriptive exposition plus cross-reference; no engagement claimed,
  none needed.
- **Dennett** — descriptive only; the article correctly reserves the retain-categorical-
  alternatives claim for List and gives Dennett the deflationary reading.

No classification vocabulary appears in article prose.

## Optimistic Analysis Summary

### Strengths Preserved

- The **reinterpret / bypass / relocate** organizing axis is the article's best asset — it is a
  genuine analytic contribution, not a list, and it makes each variant's relation to Tenet 3
  immediately legible. Untouched except to honour it for the sixth variant.
- The **concede-the-morals, contest-the-metaphysics** framing in Relation to Site Perspective
  ("the Map does not treat compatibilists as covert deniers of responsibility") is unusually
  fair-minded for a rival-position page and is exactly the posture that makes the disagreement
  land. Untouched.
- Naming **semicompatibilism as the hardest challenge to the Map's own apparatus** — an article
  volunteering the objection that most threatens its parent project. Untouched.
- The **PhilPapers caveat** about secondary summaries inflating the figure via subset
  renormalisation. Untouched.

### Enhancements Made

- Taxonomy now complete and self-consistent across all six variants.
- Two editor-voice intrusions removed; prose now speaks to the reader throughout.

### Cross-links Added

None — the article already carries 8 Further Reading links and 5 inline cross-references, all
resolving, and the 07-13 pass installed the reciprocal inbound links.

## Length

2502 → **2499 words** (100% of the 2500-word `concepts/` soft target). Length-neutral: the
Strawson clarification (+) was paid for by the editor-voice and redundancy trims (−). Status
improved from `soft_warning` to `ok`.

## Remaining Items

- **New dispositionalism has no dedicated page and the thinnest reply in the article.** The
  article itself calls it "among the strongest live challenges to the Map's premise that leeway
  must be metaphysically categorical", and the only reply is the Consequence Argument routing.
  The sharper in-framework objection — that a disposition whose manifestation conditions are
  never met in a deterministic world is a bare conditional in dispositional clothing (Clarke,
  *Mind* 2009) — is not made anywhere in the lattice. This is a genuine content gap, but adding
  it here would require a new citation and web-verification against a length-neutral budget, so
  it is **deferred rather than bodged in**. No task minted: this warrants a dedicated page
  (`research-topic` → `expand-topic`), which is out of contract for deep-review to mint, and no
  open task currently targets this file.

## Stability Notes

**Carried forward from 2026-07-13 and reaffirmed** — the Map's disagreement with compatibilism
is a bedrock metaphysical framework-boundary disagreement (Tenet 3: categorical versus
conditional/emergent leeway), **not** a calibration error. Future reviews must NOT re-flag as
critical:

- "Fischer's semicompatibilism makes the quantum interface unnecessary" — the article states
  this as a burden it carries; §2.6 confirms it as honest Mode Three.
- "Compatibilists will find the categorical-leeway premise unmotivated" — framework boundary.
- "List's emergentism is a cheaper route to the same conclusion" — the article names the locus
  dispute explicitly and raises the internal objection to List.

**New this pass** — the citation ledger is closed. Ten citations were verified at the publisher
of record on 2026-07-13 across two independent passes, with URLs. Absent a change to the
References block or the addition of a new cite, §2.4 should be **skipped**, not re-run, on this
article; re-running it is the no-op that convergence damping exists to prevent.

The article is **converged**. Two full review cycles have now found one defect each, both minor
and both of a kind only a fresh lens catches (07-13: majority/plurality inconsistency; 08-02:
the emergentist-route misparse). A third pass should be triggered only by substantive body
edits, not by frontmatter churn.