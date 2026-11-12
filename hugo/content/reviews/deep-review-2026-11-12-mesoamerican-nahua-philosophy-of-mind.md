---
ai_contribution: 100
ai_generated_date: 2026-11-12
ai_modified: 2026-11-12 00:51:30+00:00
ai_system: claude-fable-5-2
author: null
concepts: []
created: 2026-11-12
date: &id001 2026-11-12
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-12 00:51:30+00:00
modified: *id001
related_articles: []
title: Deep Review - Mesoamerican Nahua Philosophy of Mind
topics: []
---

**Date**: 2026-11-12
**Article**: [Mesoamerican Nahua Philosophy of Mind](/topics/mesoamerican-nahua-philosophy-of-mind/)
**Previous review**: [2026-09-11](/reviews/deep-review-2026-09-11-mesoamerican-nahua-philosophy-of-mind/)
**Word count**: 2335 → 2464 (+129), `ok`, 536 below topics soft 3000
**Mode**: post-modification review. The only body change since 2026-09-11 is the 2026-10-14 refine-draft rewrite of one sentence in §Relation to Site Perspective ("qualifies its core inference as well…"). That sentence was checked and holds. The yield of this pass came from somewhere else: the 2026-09-11 review *carried forward* the 2026-07-10 citation ledger without re-fetching, so this pass re-ran §2.4 against raw publisher text.

## Method

Raw sources fetched with curl and grepped as text (no summariser in the loop):

- IEP "Aztec Philosophy" (Maffie), https://iep.utm.edu/aztec-philosophy/ — 11,147 words extracted
- University Press of Colorado catalogue page for Maffie 2014
- Notre Dame Philosophical Reviews review of Maffie 2014 (Robert Eli Sanchez Jr., 2014.10.11)
- Getty Digital Florentine Codex landing page

Not obtained: the full text of Maffie 2014, León-Portilla 1963 and López Austin 1988 (archive.org search returned no full-text item for Maffie; the other two were not attempted beyond that). Claims resting only on those books are marked below.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Florentine Codex dated "compiled c. 1545–1590" — wrong for the Codex. FIXED.**
The cited source itself (Getty) says the manuscript was completed in 1577 and then sent to Europe. 1545–1590 is the span of Sahagún's working life on the wider *Historia general* project, ending at his death; the Codex left New Spain a decade before 1590. The figure sat in the body (§Reconstruction Across a Colonial Filter), in the References entry, and three times in the source research note. Body now reads "compiled over decades … completed as a manuscript in 1577"; References entry now "(completed 1577)"; the three research-note occurrences corrected in `research/nahua-philosophy-of-mind-teotl-tripartite-soul-2026-07-10`. Corpus sweep for `1545` and `Florentine Codex`: no other article carries the date. Also dropped "single" from "the single most reliable source" — Getty's wording is "the most reliable source".

**2. "A refined metaphysics comparable to the ancient Greeks", attributed jointly to León-Portilla and Maffie — unsupported for Maffie. FIXED.**
`Greek` returns zero hits in the IEP entry and zero on the publisher page, whose own claim is "a highly sophisticated and internally coherent systematic philosophy worthy of consideration alongside other philosophies from around the world". León-Portilla does draw Greek comparisons, but the sentence credited the comparison to both. Replaced with "a sophisticated, coherent metaphysics", which both sources support.

**3. "More cautious reviewers warn against imposing a single coherent 'system' on fragmentary, mediated evidence" — no reviewer named, no reference. FIXED.**
An unattributed plural. The NDPR review supplies a real instance, and it says something narrower than the article's gloss: Sanchez grants the worldview "can be found in the Náhuatl language and other products of Aztec culture" but finds it "difficult to tell whether it is a 'reconstruction' of Aztec philosophy, as it was meant to be, or a construction". Both strings verbatim in the fetched review. Sentence rewritten around the named reviewer; Sanchez 2014 added to References.

**4. León-Portilla's reading labelled "arguably idealist" — mischaracterised. FIXED.**
The IEP entry states the disagreement precisely: the tlamatinime "conceived the dreamlikeness or illusoriness of earthly existence in epistemological — not ontological — terms (pace Leon-Portilla 1963). Illusion was not an ontological category as it was, say, for Plato." The NDPR review describes León-Portilla as arguing that "like Plato, the Aztecs worried that reality is not what it appears to be, leading them to endorse a strand of dualism". So the León-Portilla reading is a Platonic two-grade appearance/reality picture, and the Maffie/León-Portilla split is ontological versus epistemological illusion. Rewritten accordingly. Because the word "dualism" appears in the secondary literature here, a closing sentence fences it: the two-level picture divides appearance from reality, not mind from body, so it gives no licence to conscript the Nahua as mind-body dualists. This matters for a dualist site — the temptation runs toward the Map's own conclusion.

### Medium Issues Found

**5. Mind-versus-matter presented as the Map's extension ("and, by extension, mind versus matter") when Maffie says it outright. FIXED.**
The IEP passage lists only "personal vs. impersonal, animate vs. inanimate, etc.", so the article's hedge was honest relative to the IEP. But the book states the mind-matter point directly: teotl is "a tertium quid, a third kind of stuff that is neither mind nor matter (as customarily conceived by dualists)" (p. 48). The whole article's basin-edge reading rests on this, and it was the one step not sourced. Added, cited as "Maffie 2014, p. 48, quoted in Sanchez 2014" because the string was verified in the NDPR review's quotation, not in the book itself.

### Checked and Holding

- The 2026-10-14 sentence ("qualifies its core inference as well: the traditions that *do* pose the problem differ on substance, self and causation, yet all start from the mind-matter partition") is consistent with §common-cause paragraph, which claims only that convergence is "conceptually conditional rather than architecturally forced" and does not claim to discharge the common-cause objection.
- "would *strengthen rather than confirm*" — certified 2026-07-10, used as the model for the Kyoto fix in `pessimistic-2026-10-12-non-western-traditions-wing` and `deep-review-2026-11-11-japanese-philosophy-of-mind-kyoto-school`. Left alone.
- `[[common-cause-null|despite-commitments]]` — the term is still present in the target (4 occurrences).
- No editor-vocabulary label leakage. No named-opponent reply in the §2.6 sense; teotl-monism is marked as a rival held unadjudicated (boundary-marking, honestly stated).
- Calibration: no five-tier upgrade anywhere; the article lowers the convergence argument's reach. A tenet-accepting reviewer would not flag any claim as overstated.

### Citation Ledger (§2.4)

- Maffie 2014, *Aztec Philosophy* (UPC) — **real-correct**. Publisher page: paperback ISBN 978-1-60732-461-4, March 2014. "Ontological monism" / "constitutional monism" confirmed as Maffie's labels via NDPR ("He dubs these two beliefs ontological and constitutional monism"). "A thing is what it does" confirmed as NDPR paraphrase ("Something is what it does"). Gods as "aspects" or "guises" confirmed (NDPR quoting p. 87 context). Olin / malinalli / nepantla glosses and "agonistic inamic unity" confirmed via NDPR; weaving as root metaphor confirmed. Thunderstorm/river comparison: seen only in a search-result excerpt of the book, not in fetched raw text — paraphrase, not quoted; **not independently certified**. Louisville place-of-publication left alone per the 2026-07-10 stability note.
- Maffie, "Aztec Philosophy", *IEP* — **real-correct**. All five quoted strings grep-verbatim in raw text: "a single, dynamic, vivifying, eternally self-generating and self-regenerating sacred power, energy or force"; "both metaphysically immanent and transcendent"; "seamless totality"; "know teotl through teotl"; "without mediation by language, concepts, or categories". Note the IEP term for the paired-opposites doctrine is "dialectical polar monism"; "agonistic inamic unity" is the 2014 book's term, and the article attributes it to "Maffie" without the IEP tag, correctly.
- Sanchez 2014, NDPR review — **newly added, real-correct**. Three quoted strings grep-verbatim.
- León-Portilla 1963 — **real-correct (metadata)**; characterisation corrected (item 4). "The only earthly truth" for flower-and-song not verified in raw text of the book.
- López Austin 1988 — **real-correct (metadata)**. Seats (head / heart / liver) and functions cross-checked against the IEP's summary, which cites him. Two details rest on López Austin alone and were not raw-verified: tonalli leaving "in sexual excitement", and susto as tonalli loss. The IEP gives "dreams and shamanic journeys".
- Sahagún et al., Florentine Codex — **real-wrong-metadata** (was "c. 1545–1590", corrected to "completed 1577"). "Created by … Sahagún and a group of Nahua elders, authors, and artists" and "widely regarded as the most reliable source" confirmed at Getty.
- Two Map self-cites — unchanged.

Superlative sweep: `find_superlative_claims` n=0.
Inline ↔ References: every inline cite has an entry; every entry is cited (Sanchez now cited twice).

**Cited-author-stance leg**: Maffie is a pantheist-monist interpreter who defines teotl against dualism in so many words; the article presents him as the source of a *rival* to Tenet 1 and never as support. Sanchez expresses reservations, not rejection ("not quite criticisms") — the article's "grants … yet finds" preserves that.

## Optimistic Analysis Summary

### Strengths Preserved

- Exposition fenced from interpretation, with the §Relation opening sentence forbidding read-back.
- The opposite-direction contamination argument (teyolia had a Franciscan template; teotl-monism had none) and its admission that the asymmetry costs the Map.
- Tenet 5 applied in both directions.
- Birch-style restraint: the tripartite soul is "thematic … not evidential about mechanism".

### Enhancements Made

- Maffie's own "neither mind nor matter" statement now anchors the article's central step.
- The systematisation dispute has a named reviewer and verbatim words.
- The León-Portilla/Maffie split is stated as ontological versus epistemological illusion, which is how Maffie himself frames it.

### Cross-links Added

None.

## Remaining Items

- Teyolia is described as "the force that survived death and travelled to the afterlife". The IEP adds "After death, each goes its own way" — all three forces have a post-mortem fate, though only teyolia goes to the world of the dead. The article's wording is defensible; a future pass with López Austin in hand could sharpen it.
- Tonalli-in-sexual-excitement and susto-as-tonalli-loss need López Austin 1988 raw text.
- `topics/japanese-philosophy-of-mind-kyoto-school` Further Reading still calls this article "a third basin-edge case" (noted 2026-09-11; out of scope here).

## Stability Notes

- Physicalist, eliminativist and process-monist rejection of the Map's dualism remains bedrock; not re-flagged.
- The IEP (2005-era) says teotl is "both metaphysically immanent and transcendent"; the NDPR review reports the 2014 book as denying the Aztecs an immanent/transcendent dichotomy. The article quotes the IEP accurately with an IEP tag, and "both" is compatible with rejecting the dichotomy. Do not churn.
- The 2026-07-10 note that the IEP quote fragments "need not be re-litigated" is now backed by a raw-text grep rather than a carried-forward ledger. The exemption covers those five strings only; it never covered the Florentine date, the Greek comparison or the León-Portilla characterisation, which is how they survived two reviews.