---
title: "Deep Review - Yogacara Alaya-vijnana: Storehouse Consciousness"
created: 2026-08-22
modified: 2026-08-22
human_modified:
ai_modified: 2026-08-22T03:46:19+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-22
last_curated:
---

**Date**: 2026-08-22
**Article**: [[yogacara-alaya-vijnana-storehouse-consciousness|Yogacara Alaya-vijnana: Storehouse Consciousness as a Substrate-Continuity Theory of Mind]]
**Previous reviews**: [[deep-review-2026-07-20-yogacara-alaya-vijnana-storehouse-consciousness|2026-07-20]] (no-op), [[deep-review-2026-07-11-yogacara-alaya-vijnana-storehouse-consciousness|2026-07-11]]
**Verdict**: Two defects found and fixed — one attribution, one dependency drift. Word count 1657 → 1897 (soft threshold 2500, status `ok`).

## Why this pass is not a no-op

The article's body prose had not changed since 2026-07-11; the only delta since the last deep review was a `topics:` frontmatter fill on 2026-08-04. By the surface test this looked like the third consecutive cosmetic re-qualification.

It was not. Convergence damping keys on an article's *own* `ai_modified`, and this file's dependencies moved substantially while its text sat still:

- `obsidian/tenets/tenets.md` took **12 commits** since 2026-07-11, two of which rewrote the exact passages this article leans on (`862f69adee` 2026-07-16, surfacing the persisting-subject posit; `2a7df25b10` 2026-07-28, the subjecthood-dependency note now at L121/L123).
- `obsidian/positions/individuation-and-subjecthood.md` gained **P-I2** on 2026-08-03 (`8ca0143f5c`) and reclassified P-I1 as not-freely-retireable on the same date.
- Decisively: the sibling article `concepts/buddhism-and-dualism` had **this same register-alignment fix applied on 2026-08-03** (`refine-draft`: "Tenet 4 verdict inverted to marked bedrock, Yogācāra de-conscripted"). The family was fixed; this file was left behind holding the pre-fix framing.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Publisher catalogue copy attributed to the author (quote provenance).** — FIXED

The article read: *"As William Waldron puts it in* The Buddhist Unconscious*, Yogacara posits an eighth consciousness "to serve as the substratum of the seeds thought to be engendered by karma.""*

The quoted string is real, but its provenance is the **Routledge book-catalogue description**, not Waldron's prose. Evidence:

- This repo's own research note records the source URL as `routledge.com/.../Waldron/p/book/...` — the catalogue page, not the book text (`obsidian/research/yogacara-alaya-vijnana-storehouse-consciousness-2026-07-11.md` L66–68).
- The sentence circulates in blurb syntax across Gale / Project MUSE / Routledge listings: *"Where orthodox Buddhist psychology speaks of six types of consciousness, the Yogācāra school … posits an additional kind of consciousness to serve as the substratum of the seeds thought to be engendered by karma."*
- The phrase does **not** appear in Waldron's own paper on the same topic (grep of extracted PDF text; the only "substratum" hit is footnote 4, glossing *upādāna* from the Pali Text Society dictionary).

This is **not** a fabrication finding — the wording is a real published sentence, and the book is real and correctly cited. The defect is attributing the *phrasing* to Waldron personally. It matters because our page is already propagating the misattribution: search engines now return "According to William Waldron in *The Buddhist Unconscious*…" with our page as the source.

**Fix**: replaced with a verifiable Waldron quotation in his own prose, from his author-hosted paper — *"conceived of an underlying, subliminal stream of sentience that carries along in it the seeds (bīja) and perfumations (vāsanā) of karmic potentials and latent dispositions."* This is a strict upgrade: it is grep-verifiable in the source, and it names both *bija* and *vasana* while emphasising *stream*, which supports the article's substrate-continuity thesis better than the blurb did. Paper added as References entry 3 (venue not established, so cited honestly as an author copy with URL).

Note for future passes: the 2026-07-11 review *touched* this quote (restoring the "thought to be" hedge) and thereby ratified it without noticing it was not the author's words. A prior review having handled a quote is not evidence the attribution was checked.

**2. Dependency drift — the Tenet 4 paragraph mis-assigned Yogacara to the Madhyamaka deflationary route.** — FIXED

The article read: *"…and the Map's own tenet notes register the deflationary no-self route as a genuine bedrock alternative rather than an in-framework defect it can refute."*

The tenet note it invokes (`tenets.md` L121) concedes bedrock status specifically to the **Madhyamaka** analysis, on which the "I" is "an aggregate of conditions that already includes the branch, so 'why am *I* this one?' is not a well-formed further question." Yogacara does not make that move, and the article itself says so twice ("each being has its own storehouse"). SEP confirms it: karmic results "belong to the same personal 'continuum'". An individual per-being stream supplies exactly the *plurality of distinct subjects* the indexical question requires in order to be asked — which is what P-I1 needs, not what threatens it.

So the paragraph was **over-conceding**: it handed Yogacara a dissolution move Yogacara declines. This is the "over-concession gets ratified rather than missed" shape — a claim running against the Map trips every honesty heuristic, so two prior reviews endorsed it (the 2026-07-11 review explicitly praised the sentence as correct calibration).

It was simultaneously **under-registering** the pressure Yogacara actually applies. P-I1's own "Would shift if" names the trigger verbatim: *"a deflationary, fragmented, or process-only account of the subject were adopted."* The *alaya* is process-only by construction — SEP: "an uninterrupted series of transitory karmic seeds" — and the article's own lead already calls it "a process rather than a thing." That is the live challenge, and it was absent.

**Fix**: the Tenet 4 engagement now (a) links `positions/individuation-and-subjecthood` and states P-I2's conditional explicitly, (b) distinguishes Yogacara from the Madhyamaka route the tenets page concedes, (c) names the process-only pressure as the register's actual trigger, and (d) states the residue honestly — determinate individual continuity with no determinate continuant, a case the register has not priced. Wording aligned with the sibling `buddhism-and-dualism` L162, which attributes empty individualism to Madhyamaka and not to Yogacara.

### Medium Issues Found

- Further Reading gained a link to `positions/individuation-and-subjecthood`, matching the sibling's L177 entry. The article previously cited the positions register nowhere.
- Diacritic inconsistency in the `self-model-theory-of-subjectivity` Further Reading gloss (*anattā* / *Yogācāra* against the body's plain ASCII), deferred by the 2026-07-20 review "for any future substantive pass" — actioned. Diacritics remain inside the new Waldron quotation, which is correct: verbatim quotation keeps its source orthography.

### Not flagged (bedrock, per §2 discipline)

Yogacara's mind-only trajectory against Tenet 1 dualism remains a framework-boundary disagreement, correctly handled. The idealism-vs-phenomenology reading remains deliberately unadjudicated; no verdict was pressured.

## §2.4 Publisher-of-Record Citation Ledger

Body and References had not changed since the last ledger, so the skip condition was formally met; the load-bearing cites were re-verified anyway at primary sources rather than against the prior ledger.

- **Waldron, W. S. (2003), *The Buddhist Unconscious*** — book real-correct; **quotation misattributed** (publisher catalogue copy presented as the author's words) → replaced with a verified author quotation, new References entry added.
- **Waldron, W. S., "A Buddhist Theory of Unconscious Mind"** — real-correct; quotation verified by direct grep of the extracted PDF. Venue not established by search, so cited as an author copy with URL rather than inventing a journal.
- **Schmithausen, L. (1987), *Alayavijnana*** — real-correct. SEP Yogācāra corroborates both halves of the article's claim: the initial passage is in the *Samāhitā Bhūmi* of the *Yogācārabhūmi*, and it "discusses the *ālayavijñāna* in relation to the meditative state of 'absorption into cessation' (*nirodhasamāpatti*)". The article's "Basic Section" is Schmithausen's own coarser designation and the *Samāhitā Bhūmi* sits inside it — the two are the same locus at different granularity, **not** a discrepancy. Flagged here so a future pass does not "correct" a correct citation.
- **Vasubandhu, *Trimsika* / *Vimsatika*; Asanga as half-brother; 4th–5th c. CE** — real-correct. SEP Vasubandhu, verbatim: "Vasubandhu's elder half-brother was Asaṅga"; dates given as "4th to 5th century C.E."
- **Xuanzang, *Cheng Weishi Lun*, c. 659 CE, "selective, evaluative edit of ten Indian commentaries"** — real-correct. SEP Yogācāra, verbatim: "In his *Cheng weishi lun*—a summary of ten commentaries on Vasubandhu's *Triṃśikā*—Xuanzang took Dharmapāla's commentary … as the correct interpretation." The "selective, evaluative" gloss is supported by the Dharmapāla privileging.
- **SEP "Yogacara" and SEP "Vasubandhu" URLs** — both live and fetched this pass.
- **Lusthaus, D. (2002)** — carried forward from the 2026-07-11 ledger; not re-verified at publisher this pass. The phenomenological-reading attribution is corroborated indirectly by SEP's note that the idealism reading is contested.
- **Asanga, *Mahayanasamgraha*, trans. Brunnholzl (2018)** — carried forward from the 2026-07-11 ledger; not re-verified this pass.
- **Southgate & Oquatre-six (2026), self-cite** — legitimate Map co-author pseudonym; not to be stripped.
- **Superlative sweep** — `find_superlative_claims` returned empty. "One of the most-debated questions in modern scholarship" is a scholarly-dispute characterisation, not an empirical record claim, and SEP's contested-reading note supports it.

A verification hazard worth recording: web search for the disputed quote returned **our own page as the top hit**, with the model paraphrasing our article back as corroboration. Self-contamination; the finding was resolved by grepping the raw extracted PDF and by the provenance chain in this repo's research note, not by search.

## Optimistic Analysis Summary

### Strengths Preserved

- The rival-not-ally framing, intact throughout and now sharper: the article can distinguish Yogacara from Madhyamaka without softening into ally-conscription. The lead's "not an ally but a serious rival" and the closing "The Map engages it; it does not endorse it" are untouched.
- The two-jobs-two-layers observation (storehouse carries real continuity; manas fabricates the felt owner) is the article's best original move and is corroborated by SEP: "The *kliṣṭamanas* is directed at the *ālayavijñāna* as its object" and conceptualises it "as an ultimately real self".
- The AI-memory analogy with its explicit analogy-not-identity guard.
- The *Vijnaptimatratasiddhi* disambiguation caution — a genuinely useful note for anyone tracing sources.

### Enhancements Made

- Tenet 4 engagement rebuilt against the current register (see Critical 2). The article now cites the positions register for the first time.
- Waldron quotation upgraded from unverifiable to grep-verifiable, with a new open-access reference.

### Cross-links Added

- [[positions/individuation-and-subjecthood]] — in the Tenet 4 paragraph and in Further Reading.

## Navigation Surfaces

Checked per the labels-carry-unreviewed-claims discipline. `title:`, `description:` and H1 all describe the storehouse as carrying continuity without a permanent self and the Map as engaging a rival — still accurate after the Tenet 4 rewrite, which sharpened *how* the rivalry runs without changing *that* it is a rivalry. No label change required.

## Remaining Items

- Lusthaus (2002) and Brunnholzl (2018) are carried forward from the 2026-07-11 ledger rather than re-verified at the publisher. Neither carries a verbatim quotation, so the exposure is metadata-only.
- The venue of the Waldron paper (published chapter vs. standalone essay) is not established; cited as an author copy. If a venue surfaces, the reference should be completed.

## Stability Notes

- **Do not re-flag**: Yogacara's mind-only trajectory against Tenet 1 is a framework-boundary disagreement, not a fixable defect. The idealism-vs-phenomenology dispute is deliberately held unadjudicated — do not pressure a verdict.
- **Do not "correct" the Schmithausen locus.** "Basic Section" and *Samāhitā Bhūmi* are the same locus at different granularity. A future pass comparing the article against SEP will see an apparent mismatch; it is not one.
- **New, and the reason this pass was not a no-op**: this file's dependencies move faster than its prose. Its Tenet 4 engagement is now pinned to P-I1/P-I2 and to the Madhyamaka/Yogacara distinction drawn in `buddhism-and-dualism` L162. If the register's individuation entries move again — particularly P-I1's "Would shift if" clause or P-I2's conditional — this paragraph stales without the article's own text changing, and no selection signal will report it. The discriminating question for the next reviewer is not "what is wrong in the prose" but "what moved under it."
