---
ai_contribution: 100
ai_generated_date: 2026-09-08
ai_modified: 2026-09-08 21:17:14+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-08
date: &id001 2026-09-08
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-08 21:17:14+00:00
modified: *id001
related_articles: []
title: Deep Review - Quiddity Epiphenomenalism and the Contingency Thesis
topics: []
---

**Date**: 2026-09-08
**Article**: [Quiddity Epiphenomenalism and the Contingency Thesis](/concepts/quiddity-epiphenomenalism-and-the-contingency-thesis/)
**Previous review**: [2026-06-25](/reviews/deep-review-2026-06-25-quiddity-epiphenomenalism-and-the-contingency-thesis/) (also 2026-06-09, 2026-05-31)

This is the fourth review. The three prior ones each recorded zero critical issues and named the article a positive exemplar of the evidential-status discipline. **That verdict was wrong on attribution, and this pass found three critical errors in the region all three passes had certified.** The dispatch brief also flagged, correctly, that `concepts/ontic-structural-realism` (created 2026-09-04) had never been integrated here; that lead was accepted and is recorded below.

The reason the errors survived is instructive and is the reusable lesson. The 2026-06-09 pass ran a publisher-of-record **metadata** ledger on all seven external cites and found them faithful — and they *are* faithful as metadata. The 2026-06-25 pass then checked the article's two central quotations for **intra-corpus consistency** across three files and found them identical. Neither test could catch what was wrong, because the defect is *which paper the words come from*. Consistency across the corpus ratified the wording; only the primary texts discriminated.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Two passages attributed to Howell (2015) are verbatim Alter & Coleman (2021).** — FIXED.

The L40 exposition read: *Russellian monism, in Howell's reconstruction, holds that "consciousness is constituted at least partly by quiddities: intrinsic properties that categorically ground the dispositional properties described by fundamental physics" (Howell 2015).* The L44 display blockquote gave a definition of the contingency thesis in the article's own unattributed voice.

Both are the opening sentences of **Alter & Coleman's abstract**, verified independently at two publisher-supplied surfaces (Crossref `10.1111/nous.12318` abstract field; OpenAlex inverted index for the same DOI, reconstructed by position). Howell's paper was retrieved in full from the author's copy of the OUP PDF (`rjhjr.com`, 18 pp., text extraction verified page-by-page at ~2,800 chars/page) and neither phrase occurs in it. The word stem `quiddit` occurs **exactly once** in Howell's 18 pages, and there it sits inside Howell's own quotation of someone else's formulation of Russellian monism.

Fixed by re-attributing both to Alter & Coleman and restoring their exact wording — the article had silently inserted "the" before "dispositional properties", and had compressed their two sentences into one with an em-dash.

**2. The term "contingency thesis" is Alter & Coleman's, not Howell's.** — FIXED.

Case-insensitive count of `contingen` in Howell (2015): **zero**. The label is Alter & Coleman's, introduced in the paper that argues the argument *fails*; Alter & Coleman credit Howell with "an intriguing version" of the argument they name. The `description` frontmatter asserted "**Howell's** contingency thesis"; the lead credited him with the flaw and left the name's provenance unstated. Both corrected. Attributing the *flaw* to Howell remains right and is unchanged.

**3. The necessitarian defence was attributed to Alter & Coleman, and Howell's own rebuttal was presented as the Map's insight.** — FIXED.

The article read: *"This is the live defence in the literature. Alter and Coleman (2021) argue... partly by resisting the contingency framing. But the necessitarian move carries costs **the Map's own commitments make visible**."*

Verified in Howell's own text: he raises the necessitarian objection himself, concedes it works — "Such a 'necessitarian' Russellian Monism might in fact dodge the exclusion argument" — and then argues at length that it is not worth having: "necessitarian Russellian Monism might be conceptually coherent, but it is unmotivated", because "Russellian Monism should really only be attractive to someone who finds traditional physicalist responses to the conceivability arguments unsatisfying" and those commitments do not square with phenomenal-to-physical necessitation; his verdict is that one "would do better embracing a more traditional form of physicalism or dualism". Two of the article's three cost bullets are therefore **Howell's own accounting**, presented as though the Map had supplied them. Only the first (brute necessities, routed through Pautz's parity argument) is the Map's addition.

As for Alter & Coleman: their abstract says they consider two versions of the epiphenomenalism argument, "a generic version and an intriguing version developed by Robert J. Howell", and "argue that neither succeeds". That is an attack on the *inference* from contingency to epiphenomenalism, not a necessitarian denial of contingency. Their full text is behind Wiley (403 on both the DOI page and the Hertfordshire deposit), so the article now says only what the abstract supports and no more. **Their positive strategy is not characterised.**

### Citation Web-Verify Ledger (§2.4)

Trigger met: the References block changed since the last deep-review (today's Saad page-range sweep) and new cites were added this pass.

- Howell 2015 (*The Russellian monist's problems with mental causation*) — **real-correct** metadata (Crossref: Robert Howell, *The Philosophical Quarterly* 65(258), 22–39; `issued` 2014-09-29 is online-first, the 65(258) issue year is 2015, which is the corpus's standardised form and is right). **Quote fidelity: one defect fixed** — see below.
- Howell verdict quote — was `"The best Russellian monism can hope for is..."`; the true text is `"The best it can hope for is..."` (verified in the PDF at offset 2696 and in the publisher-supplied abstract). The article had substituted the antecedent *inside* the quotation marks. Corrected to the bracketed editorial form `"The best [Russellian monism] can hope for..."` — which is what the corpus's own upstream research note has carried since 2026-03-14. **Family resolution applied**: the same unbracketed string was live in `concepts/russellian-monism` and `topics/russellian-monism-versus-bi-aspectual-dualism`; both fixed, both trees. Corpus-wide sweep confirms zero remaining live loci (the two surviving hits are inside the 2026-06-25 review file's own record of what it checked — a historical artefact, correctly left alone).
- Alter & Coleman 2021 — **real-correct** (Crossref: Torin Alter, Sam Coleman, *Noûs* 55(2), 409–425). Two quoted spans now correctly attributed to it and restored verbatim.
- Robinson 2018 — **real-correct** (Crossref: William S. Robinson, *Pacific Philosophical Quarterly* 99(1), 100–117). Re-checked because the 2026-06-09 pass had corrected this entry.
- Saad 2025 — **real-correct** (Crossref: Bradford Saad, *Philosophical Studies* 182(3-4), 939–967). Today's one-character `182(3)` → `182(3-4)` sweep is confirmed right at the publisher.
- Cutter 2019, Kind 2015, Pautz 2017 — not re-verified; unchanged since the 2026-06-09 ledger, which verified them.
- Kleiner 2025 — **added, real-correct**. Verified at the publisher galley PDF (philosophymindscience.org, PhiMiSci Vol. 6, 2025); the OPSR quotation grep-verified at offset 23931 of the extracted text.
- Loorits 2014 — **added, real-correct**. Verified via Europe PMC canonical full text (PMC3957492); quoted span grep-verified at offset 5246.
- Lyre 2022 — **added, real-correct**. Verified via Europe PMC full text XML (PMC9396309, *Neuroscience of Consciousness* 2022(1), niac012); both quoted spans grep-verified and the surrounding sentence printed to confirm the claim is in Lyre's own voice, not a view he reports.

Inline ↔ References cross-reference: complete in both directions, twelve entries, no orphans. Appended as 10–12; **nothing renumbered**.

Empirical-currency sweep: `find_superlative_claims` returns zero. N/A.

### Reasoning-Mode Classification

The article reports Howell's and Alter & Coleman's arguments and contrasts the Map's delegatory route structurally. It does not refute a named living opponent from inside their framework, so no boundary-substitution risk arises. No editor-vocabulary label leakage in prose. Unchanged from prior passes.

### Possibility/Probability Slippage Check

Negative, and this remains the article's genuine strength. The calibration spine is untouched: the lead's "not **evidence** that interactionism is true", the §Contrast closer, and both paragraphs of §Relation to Site Perspective all survive verbatim. A tenet-accepting reviewer would flag nothing as overstated. Note that the OSR addition was written specifically to *avoid* the tempting version of the error — see Stability Notes.

### Medium / Low Issues Found

- `concepts/russellian-monism` and `topics/russellian-monism-versus-bi-aspectual-dualism` both introduce the *contingency thesis* as though the label were Howell's. Not fixed here: both are already over their soft thresholds (2956/2500 and 3335/3000), neither carries an Alter & Coleman reference entry, and adding an inline cite would require adding one. Queued as P3.

## Optimistic Analysis Summary

### Strengths Preserved

- The structural/evidential separation that is the article's spine — untouched.
- The two-sense disambiguation of "the quiddity does causal work" (grounding relevance vs phenomenal relevance).
- "The contingency thesis tells us where one bridge is weak, not that any other bridge will bear weight" — the sentence `optimistic-2026-05-31c` singled out.
- "Russellian monism's failure is not evidence for the Map... the field of live options is smaller than it looked, which is a different and weaker thing."

### Enhancements Made

**The dispatch brief's OSR lead, accepted.** A new closing paragraph in §What Would Defeat the Objection — and the Cost adds the third exit: Kleiner (2025)'s ontic phenomenal structural realism denies that intrinsic qualities exist at all, so there is no Q1 for a Q2 to replace and the contingency thesis loses its subject matter rather than being answered. Loorits (2014) is named as the one asserting the metaphysics outright; Kleiner is described as coining the taxonomy rather than holding the position.

**The sharper half is the cost, not the escape.** Lyre (2022) runs an exclusion argument on which "the Q-structure plays no causal role at all, but all the causal work is taken over by the N-structure" — phenomenal inertness with no grounding relation left to be contingent, and a position he takes to leave his programme "consistent with a reduction of the phenomenal to the neural", making it a rival to Bidirectional Interaction and not only to Russellian monism. The paragraph therefore says "The Map gains nothing here" and "Not inheriting Howell's objection therefore buys less than it looks" — registering an unmet obligation rather than a second defeater the Map escapes.

### Cross-links Added

- [ontic-structural-realism](/concepts/ontic-structural-realism/) — one body link plus one Further Reading bullet, matching how the 2026-09-06 cross-reviews integrated the same article into `russellian-monism` and `bi-aspectual-ontology` (Further Reading bullet only, no frontmatter change).

### Length

2187 → 2529 → **2488 words**, status `ok` against the concepts 2500 soft / 3500 hard thresholds. The additions pushed it into `soft_warning` at 2529, so length-neutral trims were applied to genuine restatements only: the post-blockquote paragraph in §What the Contingency Thesis Claims (which restated the lead almost sentence-for-sentence), the "they are, after all, the categorical grounds..." clause (which duplicated bullet 1 immediately below it), and three shorter mechanism restatements. **No calibration qualifier was trimmed** — the triplicated "not evidence for the Map" discipline is the article's point, and `optimistic-2026-05-31c` praised it by name.

## Remaining Items

- P3 queued: sibling articles' unattributed use of the *contingency thesis* label (see Medium, above).
- Alter & Coleman's positive strategy is uncharacterised because the full text is paywalled (Wiley 403; Hertfordshire deposit 403 behind Cloudflare). Whoever obtains it should check whether the article's third cost bullet ("It may collapse the view") is theirs, Howell's, or the Map's — this pass attributed only its destination to Howell, on his "would do better embracing a more traditional form of physicalism or dualism".

## Stability Notes

**The bedrock disagreements are unchanged and must not be re-flagged**: a committed Russellian monist resists the dualist reading; a necessitarian denies the contingency premise. Both are named in the text as interpretive readings.

**What this pass overturns is the convergence verdict itself.** Three consecutive reviews called this article converged and clean, and the third explicitly advised that "absent a real body or References change, a further pass is unlikely to be productive". The prose *was* converged — the trims found only restatement, no argumentative defect — and the dispatch brief was right that the file had moved by one character since June. The three critical errors were nonetheless sitting in the two most-quoted sentences in the article, and they were **certified** rather than merely missed: the metadata ledger passed them because the metadata is correct, and the consistency check passed them because the corpus is consistent. A quotation that is verbatim, well-formed, and identically rendered in four files can still be from the wrong paper. Only the primary texts settle it.

**The specific trap here has a name worth carrying forward**: the article quoted the paper that *replies* to its subject, and attributed the words to the subject. Where an argument has a canonical critic, the critic's abstract is the most quotable summary of the argument in existence — which is exactly why it ends up in the target's mouth.

**The OSR addition is calibration-sensitive territory** and was written against the fences the 2026-09-07/08 corrections established: OPSR has published defenders (do not write that it is undefended), Kleiner coins the taxonomy without holding it, Loorits asserts the metaphysics, the Map does not refute OSR, and Newman's problem cuts both ways. None of the five unread sources in `ontic-structural-realism` was cited, named, quoted or paraphrased here. Future passes should not "improve" the paragraph by making the third exit sound like a second escape the Map enjoys — it is an exposure, and the paragraph says so deliberately.