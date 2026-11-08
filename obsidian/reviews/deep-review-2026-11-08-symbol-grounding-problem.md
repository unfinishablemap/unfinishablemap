---
title: "Deep Review - Symbol Grounding Problem"
created: 2026-11-08
modified: 2026-11-08
human_modified: null
ai_modified: 2026-11-08T18:08:31+00:00
draft: false
topics:
  - "[[ai-consciousness]]"
  - "[[machine-consciousness]]"
concepts:
  - "[[symbol-grounding-problem]]"
  - "[[continual-learning-argument]]"
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-11-08
last_curated: null
---

**Date**: 2026-11-08
**Article**: [[symbol-grounding-problem|Symbol Grounding Problem]]
**Previous review**: [[deep-review-2026-07-13-symbol-grounding-problem|2026-07-13]]

Eighth review. Scoped to the three body/References changes since 2026-07-13 (the only ones):
the 2026-10-24 re-attribution of "The Vector Grounding Problem" to the published Coelho Mollo
& Millière (2026) *Philosophy and the Mind Sciences* entry (L49, L167) and the softened L125
closing paragraph; the 2026-10-25 P-AC1 calibration of L105 ("Current LLMs probably achieve…");
the 2026-08-02 Searle BBS page-range fix (References only). Plus a Map-internal quotation
recheck. **Two small body edits; no structural change.** 2,663 → 2,668 words (concepts hard
3,500).

## Pessimistic Analysis Summary

### Critical Issues Found
None.

### Medium Issues Found
- **L105 calibration seam with P-AC1.** The paragraph opens "Current LLMs *probably* achieve
  linguistic competence without linguistic understanding" and closes "low-probability side, not
  ruled out ([[positions/ai-consciousness-scope#^p-ac1|P-AC1]])", but the sentence between them,
  "They are Chinese Rooms at scale.", was an unhedged identity claim. A tenet-accepting reviewer
  would still read it as outrunning the two sentences that bracket it. Fixed by scoping, keeping
  the phrase the 2026-07-13 review listed as a strength: OLD "They are Chinese Rooms at scale."
  → NEW "On this reading they are Chinese Rooms at scale."
- **L123 "is not X; it is Y" construct** (the CLAUDE.md-flagged pattern in semicolon form):
  OLD "The symbol grounding problem is not a technical challenge awaiting better engineering;
  it is a conceptual limitation revealing that meaning requires experience." → NEW "On that
  explanation the symbol grounding problem is a conceptual limitation revealing that meaning
  requires experience, rather than a technical challenge awaiting better engineering." The
  rephrase also makes the framework-conditional scope explicit (the previous sentence is the
  Map's explanation, so the limitation claim is a Map reconstruction, not a documented textual
  claim). Post-edit grep for "This is not", "is not …; it is", and "load-bearing": 0 hits.

### Citation ledger (scoped re-verification)

- **Coelho Mollo, D. & Millière, R. (2026). The Vector Grounding Problem. *Philosophy and the
  Mind Sciences* 7(1). doi:10.33735/phimisci.2026.12307** — state: **real-correct**. Crossref
  record for the DOI: title, authors (family "Coelho Mollo", given "Dimitri"; "Millière",
  "Raphaël"), container *Philosophy and the Mind Sciences*, volume 7, issue 1, type
  journal-article, published-online 2026-02-27, CC-BY 4.0. OpenAlex agrees (publication_year
  2026, publication_date 2026-02-27, biblio volume 7 issue 1, no page range — the journal uses
  article numbers, so the References entry's lack of pages is correct). The published version
  therefore exists with that volume/year; the 2023 arXiv:2304.01481 is its preprint.
  - *Quoted word "merry-go-round" (L49)*: the publisher's PDF galleys (download/12307/12354 and
    /12445, the Crossref `link` and OpenAlex `oa_url` targets) are behind a bot-check wall
    (`Making sure you're not a bot!`), so the version of record could not be grepped directly.
    The current arXiv PDF (OpenAlex-listed location, 8 pp.) is the **accepted manuscript**,
    headed "Forthcoming in Philosophy and the Mind Sciences", and contains the sentence the
    article paraphrases verbatim: "Their use of continuous vectors rather than discrete symbols
    does not help them escape the 'merry-go-round' of representations or connect to the external
    world". The article's gloss ("the move to continuous vectors rather than discrete symbols,
    the authors note, does not help escape the 'merry-go-round' of representations or connect to
    the world") is a faithful close paraphrase with only the one word quoted. 5 occurrences of
    "merry-go-round" in the manuscript. Result-direction leg: the article correctly reports that
    the authors go on to *argue LLMs can be referentially grounded* via teleosemantic conditions
    (matches the published abstract: "We argue that they can… two conditions derived from
    teleosemantic theories"), and correctly marks the Map's dissent as the Map's own.
    Cited-author-stance leg: anti-sceptical about LLM grounding; the article presents them as
    opponents on the final verdict, not endorsers. **Residual**: verbatim presence of the word in
    the typeset version of record **confirmed** via the OpenAlex-listed Oxford Research Archive
    copy (ora.ox.ac.uk …/files/r2514nn76j, 10 pp., running head "Philosophy and the Mind
    Sciences | Vol. 7 | 2026", self-citation "Coelho Mollo, D., & Millière, R. (2026) … 7.
    https://doi.org/10.33735/phimisci.2026.12307"): 5 occurrences, the paraphrased sentence
    verbatim. No residual.
- **Pavlick, E. (2023)** (L93, L166) and **Coelho Mollo & Millière** attribution lines (L49,
  L167) — grep-confirmed the live article attributes both correctly; the swapped attributions
  live only in the research note `research/symbol-grounding-problem-2026-01-30`, which has its
  own open P3 task (not touched here).
- **Searle (1980) BBS 3(3), 417-424** — References-only page-range fix of 2026-08-02; the 07-13
  ledger carried 417-457. 417-424 is the target-article span (the full BBS treatment with
  commentaries runs to 457); both forms circulate, 417-424 is the common citation. Not changed.

### Not re-litigated (carried from the 2026-07-13 web-verified-complete apparatus; body and
References unchanged at these loci)
Harnad (1990) *Physica D*; both Harnad Scholarpedia quotes (verbatim-verified 07-13); Steels
(2008) framing; Li & Mao (2022) framing and metadata; Barsalou (2008); Dove (2016).
`find_superlative_claims`: 0 hits — currency sweep skipped.

### Map-internal quotation recheck
24 lines carry both a quoted phrase and a wikilink: 17 are frontmatter list entries, 7 are body
lines (L49, L81, L85, L99, L105, L137, L139). Of the quoted phrases on those body lines, one
quotes another Map page: "substitution space" (L105), which resolves against
`concepts/continual-learning-argument` L58/L62 (the page's own wording of Hoel's term); the
same page carries "lookup tables" and the "no non-trivial theory" claim (L59). "quoted
environment" (L99) is this article's own coinage ("what might be called"), not a quotation
(`whether-language-model-words-refer` does not use it); the link text "inherit statistical
traces of human grounding" matches that page's "inherit reference… derived reference" (L69) and
"refer derivatively" (L3/L71). The remaining quoted phrases are quoted-source quotes (Harnad,
Steels, Pavlick, Coelho Mollo & Millière, Li & Mao's "hard"/"easy", Dove's title, the "Robot
Reply"/"systems reply"/"Talking Heads"/"language games" labels) or the article's own
scare-quotes ("thin"/"thick", "aboutness", "cat", "simpler"). **Stranded: 0 / 1.**

### Anchor and link check
`cognitive-phenomenology#The Phenomenal Constitution Thesis` → heading present (L113);
`intentionality#Phenomenal Intentionality Theory` → L85; all five `tenets#^…` block anchors
present; every bare-slug wikilink target in the body exists (0 missing). Inline ↔ References
reciprocity intact (8/8).

### Reasoning-mode check (editor-internal)
Engagement with Coelho Mollo & Millière: Mode Three — the teleosemantic route is reported as
their argument and the Map's dissent is marked as the Map's, with the substantive engagement
delegated to `concepts/teleosemantics`. Engagement with Steels: Mode One (functional ≠ intrinsic
grounding on his own terms). Engagement with Pavlick/deflationary line: Mode Three. Hoel: Mode
Two/Three mixed, honestly marked "defeasible". No label leakage; no boundary-substitution.

### Counterarguments Considered
The four bedrock items from 07-13 were not re-flagged (see Stability Notes).

## Optimistic Analysis Summary

### Strengths Preserved
Everything the 07-13 review listed, including "Chinese Rooms at scale" (kept, scoped). The
2026-10-24 L125 softening ("they lack original intentionality and speaker meaning, though their
symbols can still refer derivatively") now coheres with `whether-language-model-words-refer`
and with the P-AC1 "not ruled out" register — a genuine calibration improvement since 07-13.

### Enhancements Made
Two sentence-level edits (above). No additions, no new sections; length-neutral in spirit
(+5 words).

### Cross-links Added
None.

## Word Count
- Before: 2,663 (soft_warning; concepts soft 2,500 / hard 3,500)
- After: 2,668

## Remaining Items
None.

## Stability Notes

Converged page; eighth review. The citation-and-quote apparatus remains web-verified-complete,
now including the 2026 PhiMiSci entry (Crossref + OpenAlex + version-of-record text via ORA). Future
reviews should treat it as such unless the body or References block is modified.

**Bedrock disagreements (unchanged, do NOT re-flag):**
1. Eliminativist objection to meaning/intentionality as real explananda
2. Functionalist / deflationary-semantics challenge (anchored to Pavlick; bedrock)
3. MWI objection to indexical identity
4. Empiricist falsifiability concerns
5. Coelho Mollo & Millière's teleosemantic grounding route — a framework-boundary disagreement
   argued out in `concepts/teleosemantics`, not a defect of this page

Calibration: the L105 paragraph now reads at a single register from "probably" through "On
this reading" to "not ruled out (P-AC1)". The L123 limitation claim is explicitly scoped to
the Map's explanation. No possibility/probability slippage.
