---
title: "Deep Review - Phenomenal Constitution Thesis (PCT)"
created: 2026-08-04
modified: 2026-08-04
human_modified: null
ai_modified: 2026-08-04T11:15:00+00:00
draft: false
topics: []
concepts:
  - "[[phenomenal-constitution-thesis]]"
  - "[[cognitive-phenomenology]]"
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-04
last_curated: null
---

**Date**: 2026-08-04
**Article**: [[phenomenal-constitution-thesis|Phenomenal Constitution Thesis (PCT)]]
**Previous review**: [[deep-review-2026-06-26-phenomenal-constitution-thesis|2026-06-26]]

**Delta since last review**: frontmatter only — `topics: []` was populated with three bare slugs (commit `e19d4349d`, the agentic-social degenerate-pick fix). The body and References block were byte-identical to the state the 2026-06-26 review left them in. Per §2.4's trigger rule a stable-References no-op pass may skip the web-verify sweep; this review instead re-ran the sweep under a **quote-provenance** lens the prior pass did not apply, on the `[[quote-fidelity-defects-survive-metadata-reviews]]` principle that verbatim provenance is orthogonal to the metadata channel. That lens found one critical defect.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Misattributed verbatim quote (citation-framing-accuracy)**: The article read *"Horgan and Tienson's thesis that phenomenology is 'primary to all other forms of intentionality'"*. The quoted phrase is **not** Horgan and Tienson's wording. It is the Internet Encyclopedia of Philosophy author's own summary of a **programme-wide** commitment, and the IEP credits three parties jointly, not H&T alone. Verified verbatim at the live IEP entry: *"proponents of Phenomenal intentionalism claim that phenomenology or Phenomenal intentionality is primary to all other forms of intentionality (Horgan & Tienson 2002, Kriegel 2011, Mendelovici 2018)."*

  Two errors compounded: a secondary source's gloss presented as the primary authors' formulation, and a joint attribution collapsed onto one pair of names. **Resolution**: re-framed rather than deleted, per `[[citation-framing-accuracy-lens]]`. The IEP gloss is now attributed to the IEP with its joint credit intact, and Horgan and Tienson's *actual* formulation is quoted in its place — *"a kind of intentionality, pervasive in human mental life, that is constitutively determined by phenomenology alone"* (2002, 520, as quoted in the SEP *Phenomenal Intentionality* entry). The substitution strengthens the paragraph: the genuine H&T sentence states the **constitutive** claim directly, which is precisely the horn the Map adopts, where the mis-attributed gloss only asserted primacy.

- **Orphan inline cite (consequence of the above)**: Horgan and Tienson were quoted with no References entry and no year in body text. Added References entries 6 (Horgan & Tienson 2002) and 7 (SEP *Phenomenal Intentionality*), renumbering the internal self-cite to 8.

**Why the prior review missed it.** The 2026-06-26 ledger recorded this cite as `real-correct` with the justification *"their 2002 inseparability/phenomenal-intentionality thesis"* — a **paraphrase-level** ratification. The paraphrase is accurate; the quotation marks around it were not earned. This is the exact shape catalogued in `[[quote-fidelity-defects-survive-metadata-reviews]]`: a cite can pass every metadata check (author real, year right, thesis correctly characterised) while the quoted span belongs to a different text.

**Provenance note for future passes.** The defect entered the article from its own research note (`research/phenomenal-constitution-thesis-2026-06-26.md`), which recorded the phrase in quotes under its IEP section and then, in the Historical Timeline table, re-attributed it to the 2002 H&T row. Per `[[research-note-self-flagged-gaps-propagate-to-the-article]]` **the note has been corrected too** — both loci now carry the true provenance, and the IEP bullet carries an explicit "do not attribute this phrase to them" warning to stop re-propagation.

### §2.4 Publisher-of-Record Citation Web-Verify Ledger (this pass)

Re-verified only the cites whose *provenance* (as opposed to metadata) was unexamined in the 2026-06-26 ledger:

- Horgan & Tienson 2002, "primary to all other forms of intentionality" — state: **real-wrong-attribution** (phrase is IEP's programme-level gloss crediting H&T + Kriegel + Mendelovici; re-framed to IEP, replaced in the H&T slot by their verbatim 2002 formulation via SEP).
- Horgan & Tienson 2002, "constitutively determined by phenomenology alone" (new) — state: **real-correct** (quoted verbatim with page 520 in SEP *Phenomenal Intentionality*; authors and year independently confirmed at OpenAlex: Terence Horgan and John Tienson, 2002, 536 citations). Chapter end-page deliberately **omitted** from the References entry rather than guessed — only p. 520 is verified, and inventing `520–533` would be the very defect class this pass exists to catch.
- IEP "Cognitive Phenomenology", "a non-causal explanatory relation…" — state: **real-correct** (re-verified verbatim; the article's framing as *IEP's rendering* was already correct). Note the live IEP uses acute-accent marks around the inner quotes; the article's normalisation to standard quotes is typographic, not a fidelity defect.
- SEP *Phenomenal Intentionality* — state: **real-correct** (live entry; the phrase "primary to all other" does **not** occur there, confirming IEP as the sole source of that wording).

Carried forward unchanged from the 2026-06-26 ledger (body untouched since): Chudnoff 2015, Johnston 1992 (89–106), Wasserman SEP, Gertler SEP, Bennett 2004 (routed via SEP), Horgan & Kriegel 2007, Southgate & Oquatre-sept.

Empirical-record currency sweep: helper returned **0 superlative claims**. Inline↔References cross-reference: clean after the two additions. Remaining inline-only names (Wiggins, Bennett, Chalmers, Horgan & Kriegel) are correctly routed through the secondary source that cites them; Tye, Dretske, Prinz, Pitt, Strawson, Siewert, Kriegel appear as unquoted position name-drops without years, which needs no entry.

### §2.5 Attribution Accuracy — PASS (after the fix above)
The Chudnoff role-accuracy paragraph — that he supplies the constituting/accompanying distinction but is a **critic** of content-PCT — remains correct and is the article's single strongest defensive move. Qualifier preservation ("partly constitutes", "restricted class", "potentially different persistence conditions") intact. Source/Map separation explicit. Modal register calibrated. No self-contradiction.

### §2 Calibration (possibility/probability slippage) — PASS
No tenet-coherence-as-evidence-upgrade. Tenet 3 link still registered as "supporting Tenet 3's plausibility rather than proving it", with the non-causal character of constitution acknowledged not to establish downward causation. Tenet 1 invocation still correctly restricted to the bare irreducibility reading.

### Medium Issues Found
- Redundant wikilink alias `[[cognitive-phenomenology|cognitive-phenomenology]]` (alias identical to target) — simplified to `[[cognitive-phenomenology]]`.

### Counterarguments Considered
- Deflationism (Tye/Dretske/Prinz) and weak liberalism remain engaged honestly with downstream conclusions marked conditional. Unchanged; no re-litigation.

## §2.6 Reasoning-Mode Classification (editor-internal)
- Engagement with deflationists (Tye, Dretske, Prinz): **Mode Three** — registers the opposition as real and capable, makes downstream conclusions conditional rather than claiming in-framework refutation. Honest; unchanged.
- Engagement with grounding-and-constitution physicalists: clarificatory disambiguation ("share a verb and nothing else"), not a refutation claim. Honest; unchanged.
- Engagement with Chudnoff: **Mode Three** — the Map records that it sides against him on the content-determinacy verdict and does not claim to refute him on his own ground. Honest.
- **Label leakage: none** (grep for the full forbidden-label set returned clean).

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded definition; the opening paragraph states the thesis, its structural role, and the AI-understanding consequence before any truncation point.
- The three-way triangulation (PCT vs phenomenal realism / supervenience / identity) does genuine disambiguating work and was left untouched.
- Exemplary modal discipline and source/Map separation.
- The Chudnoff role-accuracy paragraph — preserved verbatim.

### Enhancements Made
- The replacement quote is a net gain, not merely a repair: Horgan and Tienson's own sentence names *constitutive determination*, so the article's central claim is now anchored to a primary-source formulation of exactly that relation rather than to a secondary gloss about primacy.

### Cross-links Added
None needed — the Further Reading block is comprehensive and all nine wikilink targets resolve to live articles.

## Remaining Items

None. **The prior review's one deferred note is now stale and is retired**: it recorded that `[[intentionality]]` and `[[symbol-grounding-problem]]` resolved only to `archive/` copies. Live articles now exist at `obsidian/concepts/intentionality.md` and `obsidian/concepts/symbol-grounding-problem.md`, and the synced Hugo output confirms both body links render to `/concepts/…` live URLs, not archive-notice pages. No `[[archival_link_rot]]` exposure remains here.

Word count: 1981 → 2076 (+95), 83% of the 2500 concepts soft threshold. No length pressure.

## Stability Notes

- Physicalists, functionalists, and deflationists (Tye/Dretske/Prinz) will reject PCT from outside the Map's tenets — bedrock framework-boundary disagreement, **not** a correctable defect. Already marked honestly. Do not re-flag.
- The article holds PCT explicitly as an abductive bet with conditional downstream conclusions. Future reviews must not push it toward "established"/"demonstrated" framing.
- **New**: the Horgan & Tienson attribution is now settled in three places (article, research note, this ledger). The phrase "primary to all other forms of intentionality" belongs to the **IEP**, describing the phenomenal-intentionality programme as a whole. Do not re-attribute it to Horgan and Tienson. The H&T-specific quote is "…constitutively determined by phenomenology alone" (2002, 520).
- The article body is otherwise converged. Two full passes have now found one citation defect each and nothing structural; a third pass should expect a no-op unless the body changes.
