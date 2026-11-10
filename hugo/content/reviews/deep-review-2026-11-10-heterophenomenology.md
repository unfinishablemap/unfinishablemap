---
ai_contribution: 100
ai_generated_date: 2026-11-10
ai_modified: 2026-11-10 20:41:12+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-10
date: &id001 2026-11-10
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-10 20:41:12+00:00
modified: *id001
related_articles:
- '[[heterophenomenology]]'
title: Deep Review - Heterophenomenology
topics: []
---

**Date**: 2026-11-10
**Article**: [Heterophenomenology](/concepts/heterophenomenology/)
**Previous review**: [2026-07-14](/reviews/deep-review-2026-07-14-heterophenomenology/)
**Word count**: 2,957 → 2,983 (+26; concepts soft 2,500 / hard 3,500; length-neutral budget of +30 respected)

**Trigger / lens**: Cycle-slot pick from `scripts/deep_review.py next` (score 77; 119 days since the last pass). This is the ninth review. The philosophical core has been stable since 2026-03-06 and was not re-litigated. The 07-14 Stability Notes were honoured: the Nagel, Dennett neutral-path, Varela and Holmes passages were not re-checked. This pass covered what had changed since 07-14: (1) the 10-21 protocol-analysis insertion (commit `07bc128b76`); (2) the 07-30 and 08-18 link and anchor fixes; (3) the dependency targets the article glosses, re-read as they stand now; (4) spot-checks of non-quote factual claims at source.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Origin date of the method (factual error, L46). FIXED.** The article said "Dennett introduced heterophenomenology in *Consciousness Explained* (1991)". The method predates that book. In the opening paragraph of "Who's on First?" (JCS 10(9–10), 2003, p. 19, read in the paper's own text from the Tufts Dennett archive scan), Dennett refers to "my apologia for heterophenomenology (Dennett, 1982; 1991)". His bibliography there lists the 1982 item as "How to study consciousness empirically, or Nothing comes to mind". Crossref gives it as *Synthese* 53(2), 159–180 (November 1982). Changed to "Dennett set out heterophenomenology in a 1982 *Synthese* paper and in *Consciousness Explained* (1991), and developed it further in …", and added the 1982 References entry. Wording was kept to "set out" deliberately. An earlier first use of the *term* (for example in *Brainstorms*, 1978) could not be confirmed or ruled out across two searches, so the article makes no coinage claim.
- **Stale host gloss on a dependency that moved (calibration, L88). FIXED.** The sentence "[Neurophenomenology](/concepts/neurophenomenology-and-contemplative-neuroscience/#advanced-practice) studies meditators' first-person reports of jhana states, finding they correlate with distinct neural signatures" was written on 01-23 against the target's old wording ("distinct neural signatures for each of the eight traditional states"). Commit `98c8f3b6bc` (2026-07-30), a citation-defect fix, rewrote that target section. It now says the strongest evidence is a single-adept 7T case study (Demir, Yang & Sacchet 2025), that the later jhanas are "not individually resolved", and that the evidence is "promising rather than established". The 07-30 fix never reached this host sentence. A reviewer who accepts every tenet would still flag "finding they correlate with distinct neural signatures" as overstated against the n = 1 record. Changed to "with single-adept evidence that deeper states reorganise brain connectivity" (+2). The next sentence opens with its own subject ("Heterophenomenology would study…"), so no pronoun was stranded.

### The 10-21 Protocol-Analysis Insertion (verdict: ACCURATE, no change)

Sentence (L134): "[Protocol analysis](/topics/protocol-analysis/) takes a parallel stance from information-processing psychology: Ericsson and Simon (1980) propose "that verbal reports are data" whose generating mechanism must be modelled, and specify the conditions under which reports of attended information are valid traces of thought."

- **Quote**: verbatim. The OpenAlex abstract of the paper opens "The central proposal of this article is that verbal reports are data."
- **"whose generating mechanism must be modelled"**: faithful to the abstract's "requires explication of the mechanisms by which the reports are generated".
- **Scope**: correctly limited. The sentence says "reports of attended information", not introspective reports in general. This matches the abstract's model of subjects verbalising "information that they are attending to in short-term memory" and its claim that the model "predicts what can reliably be reported". "Attended information" also covers the immediate-retrospective reports the 1980 paper treats, so it is no narrower than the source. "valid traces of thought" is unquoted Map wording. It matches the [protocol-analysis](/topics/protocol-analysis/) lead as it stands now ("a verbal report is a valid trace of thought when subjects voice information they are already attending to").
- **Gloss vs `topics/protocol-analysis` as it stands now**: true. That page presents the same thesis, the same mechanism requirement and the same heeded-information validity conditions. Its insistence that "content" means attended information rather than phenomenal character fits the host sentence, which makes no phenomenal claim.
- **"parallel stance"**: fair. The parallel claimed is the shared one (reports as data whose production must be modelled). The divergence (E&S credit valid reports as veridical traces of short-term-memory contents; Dennett brackets the subject's claims as a heterophenomenological world) is not asserted away. The paragraph's next sentence turns at once to what the Map rejects.
- **Citation ↔ reference**: matched in both directions (in-text "Ericsson and Simon (1980)" ↔ References entry).

### §2.4 Citation Ledger (publisher of record)

- Dennett 1982 ("How to Study Human Consciousness Empirically or Nothing Comes to Mind") — state: real-correct (NEW entry; Crossref 10.1007/BF00484895: *Synthese* 53(2), 159–180, 1982; Dennett cites it as his first apologia for the method in the 2003 paper).
- Dennett 1991 (*Consciousness Explained*, Little, Brown) — state: real-correct (Dennett 2003's own bibliography: "Boston, MA: Little Brown").
- Dennett 2003 ("Who's on First? Heterophenomenology Explained") — state: real-correct (the paper's own running footer: *Journal of Consciousness Studies*, 10, No. 9–10, 2003, pp. 19–30).
- Ericsson & Simon 1980 ("Verbal Reports as Data") — state: real-correct (Crossref 10.1037/0033-295X.87.3.215: *Psychological Review* 87(3), 215–251, May 1980; authors K. Anders Ericsson, Herbert A. Simon). The page's References carry no DOIs anywhere, so none was added, to keep house style.
- Nagel 1974 — state: real-correct (Crossref 10.2307/2183914: *Philosophical Review* 83(4), 1974, first page 435). The quote was verified 07-14 and not re-litigated.
- Rebouillat, Leonetti & Kouider 2021 — state: real-correct (Crossref 10.1093/nc/niab004: *Neuroscience of Consciousness* 2021(1), niab004; three authors as listed).
- Varela 1996 — state: real-correct (verified 07-14). Added check: the scare-quoted "mutual constraint" (L82) is Varela's own term. The 1996 paper's summary text seeks "articulations by mutual constraints between phenomena present in experience and the correlative field of phenomena established by the cognitive sciences". No change.
- Inline ↔ References: every inline cite has an entry and every entry is cited (Dennett 1982 is cited as "a 1982 *Synthese* paper"). No orphans.
- Superlatives: none bearing on cited empirical records.

### Anchor / Fragment Check (both dialects)

All 10 fragment links (8 distinct targets) resolve. Each was checked against the target's source heading (heading-text slug, or explicit `{#id}`) AND against the `id=` attribute in the built `hugo/public` HTML:
- `phenomenology#the-phenomenological-method` (heading text) — OK
- `neurophenomenology-and-contemplative-neuroscience#advanced-practice` (explicit `{#advanced-practice}` on "Jhana States and Cessation") — OK
- `phenomenal-authority-and-first-person-evidence#methodological-implications` (heading text) — OK
- `phenomenal-authority-and-first-person-evidence#constitutive-vs-referring-observation` ×2 (heading text; the 08-18 repair of the dead `#Honest limitation` fragment holds) — OK
- `microphenomenological-interview-method#confabulation-resistance-discipline` (heading text) — OK
- `tenets#dualism` ×2, `tenets#bidirectional-interaction`, `tenets#occams-razor-has-limits` (heading text) — OK

The 07-30 fix (link label "the Map's engagement with AST" replacing "Why Attention Schema Theory Fails") holds.

### Map-Internal Gloss Re-check

- L88 phenomenal-authority "Methodological Implications" gloss and Further Reading L166 ("references back to this article's fuller Varela/Dennett treatment"): true. The target links back to `heterophenomenology#Heterophenomenology vs. Neurophenomenology` for "the meditator/jhāna case".
- L102 / L108 constitutive-vs-referring glosses: true. The target's "Honest limitation" paragraph "identifies the location of bedrock disagreement rather than resolving it from outside".
- L140 microphenomenology gloss: true in substance. The target says "the case against full purchase is conceded by the method's own principals". The *interviewer-prompts-novelty* objection is the deepest part of that case, and the target says the restriction "approximates the boundary without claiming to cross it".
- L88 jhana gloss: stale. Fixed (above).

### Medium Issues Found

- None new. (A sibling-page tension was noted and left alone. `phenomenal-authority-and-first-person-evidence` reads heterophenomenology "at its strongest" as a rival *policy*, not a denial, while this article calls the neutrality "illusory". This is the article's settled thesis since 03-06, and the two readings are compatible: one is a charitable reading of the policy, the other a claim about the policy's consequences. Not a contradiction inside this article.)

### Counterarguments Considered

- Unchanged from 07-14. Bedrock framework-boundary standoffs with eliminativist, illusionist and functionalist readers were not re-flagged.

## §2.5 Attribution Accuracy

Pass. The origin-date fix improves attribution: it now follows Dennett's own self-citation. The E&S sentence attributes nothing beyond the abstract. No source/Map conflation, and no dropped qualifiers.

## §2.6 Reasoning-Mode Classification (editor-internal)

Unchanged from 07-14; no label leakage in prose.

## Calibration Check

The one slippage found was the L88 jhana gloss, an inherited overstatement rather than a tenet-driven upgrade. It is now fixed. The Rebouillat and pupillometry paragraphs remain correctly hedged ("partial purchase", "narrow the easiest reading", phenomenality bracketed).

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded opening; the phenomenology-vs-heterophenomenology table; the narrower self-stultification formulation; the three channel-disagreement paragraphs.
- The 10-21 protocol-analysis sentence works well as a concession. It gives heterophenomenology's report-as-data practice a scientific pedigree without granting the exhaustiveness claim the next paragraph rejects.

### Enhancements Made
- Origin date corrected (1982 *Synthese* paper + 1991 book), with a References entry.
- Jhana gloss recalibrated to the n = 1 record.

### Cross-links Added
None.

## Remaining Items

Out of scope for this file. Reported to the driver, not written to todo:
- `concepts/methodological-pluralism` L69 says jhana reports "correlate with distinct neural signatures". This is the same pre-07-30 overstatement the target page has since withdrawn.
- `concepts/contemplative-epistemology` L91 says "jhana states (with documented neural signatures; Hagerty et al. 2013)". Hagerty et al. 2013 is also a single-practitioner study; worth a calibration look.

## Stability Notes

Ninth review. The core remains converged (stable since 2026-03-06). Both of this pass's fixes were factual or calibration items found by checking what had moved underneath the article. No philosophical defects were found.

- Everything the 07-14 Stability Notes settled still holds (Nagel and Dennett neutral-path verbatim; Varela corrected; the Holmes passage a deliberate paraphrase).
- **Origin date**: the article now says Dennett "set out" the method in 1982 and 1991, citing his own "(Dennett, 1982; 1991)" self-citation (JCS 2003, p. 19). Do NOT upgrade this to a coinage claim ("coined in 1982") unless the term's first printed use is found at the primary text. A *Brainstorms* (1978) first use remains unconfirmed either way.
- **Protocol-analysis sentence (L134)**: verified against the 1980 abstract and against `topics/protocol-analysis` as it stands on 2026-11-10. Re-check only if the protocol-analysis lead changes its "valid trace" or "attended information" framing.
- **Jhana gloss (L88)**: now tied to the target's n = 1 wording. If `neurophenomenology-and-contemplative-neuroscience#advanced-practice` gains a multi-subject study, the gloss may be strengthened. Until then, do not restore "distinct neural signatures".
- Bedrock disagreements (eliminativist, illusionist, functionalist) remain expected framework-boundary standoffs. Do NOT re-flag.