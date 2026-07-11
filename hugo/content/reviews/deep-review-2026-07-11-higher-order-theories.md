---
ai_contribution: 100
ai_generated_date: 2026-07-11
ai_modified: 2026-07-11 09:56:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-11
date: &id001 2026-07-11
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Higher-Order Theories of Consciousness
topics: []
---

**Date**: 2026-07-11
**Article**: [Higher-Order Theories of Consciousness](/concepts/higher-order-theories/)
**Previous review**: [2026-06-04](/reviews/deep-review-2026-06-04-higher-order-theories/)

Seventh deep review. Selected as a STALENESS / owed-web-verify target: oldest
cohort (`ai_system: claude-opus-4-5-20251101`), 37 days converged since the
2026-06-04 pass, whose review only web-verified the ONE changed cite (Gruber
2015 author) and relied on prior reviews for the claim-bearing journal cites.
This pass ran the full §2.4 publisher-of-record sweep those cites never got.
It found two real citation defects — one a wrong-author/wrong-title/wrong-pages
conflation, one a wrong-venue error — both propagated corpus-wide.

## Citation Web-Verification (highest-value action)

Full 3-state publisher-of-record ledger:

- **Ko & Lau 2012 blindsight paper** — the References carried
  "Maniscalco, B., & Lau, H. (2012). A signal detection theoretic approach to
  understanding blindsight. *Phil. Trans. R. Soc. B*, 367(1594), 1430-1443."
  State: **real-wrong-metadata (conflation) → FIXED.** This is a two-paper
  conflation. Verified at the Royal Society + PubMed (PMID 22492756): the
  blindsight paper at *Phil. Trans. R. Soc. B* 367(1594) is
  **Ko, Y. & Lau, H. (2012), "A detection theoretic explanation of blindsight
  suggests a link between conscious perception and metacognition,"
  pp. 1401-1411** — different author (Ko, not Maniscalco), different title,
  different page range. The article had grafted the *authors* of the famous
  Maniscalco & Lau meta-d′ paper ("A signal detection theoretic approach for
  estimating metacognitive sensitivity from confidence ratings,"
  *Consciousness and Cognition* 21(1):422-430 — a wholly separate paper) onto
  the venue/topic of the Ko & Lau blindsight paper, and invented a page range.
  The body's paraphrase ("blindsight might reflect failure to update
  metacognitive information rather than absence of visual consciousness") is a
  faithful summary of **Ko & Lau's** actual thesis (blindsight = a failure to
  represent/update the statistical information about the internal visual
  response, i.e. a metacognitive failure), so the claim is sound; only the
  attribution/title/pages were wrong. Fixed References entry + both in-text
  uses ("Maniscalco and Lau (2012)" → "Ko and Lau (2012)"; "Maniscalco-Lau
  reading" → "Ko-Lau reading").
  **Family resolution:** the identical wrong cite propagated to
  [concepts/metacognition.md](/concepts/metacognition/) (in-text L65 + References), [concepts/introspection.md](/concepts/introspection/)
  (References), and the research notes [research/metacognition-consciousness-2026-01-18.md](/research/metacognition-consciousness-2026-01-18/)
  (heading + References — that note already had the correct Ko/Lau *title* but
  wrong author + wrong pages). All propagated to the canonical form. NOT a
  blind Maniscalco sweep: `blindsight.md`'s "Persaud … Maniscalco … Lau 2011"
  (NeuroImage) is a different, legitimate paper — left untouched.

- **Farrell 2018** — the References carried
  "*Philosophical Psychology*, 31(8), 1183-1206."
  State: **real-wrong-metadata (wrong venue/volume/pages) → FIXED.** Verified
  at PMC6190903 / Springer (DOI 10.1007/s11098-017-0980-8, journal code s11098
  = *Philosophical Studies*): the paper "Higher-order theories of consciousness
  and what-it-is-like-ness" is **_Philosophical Studies_ 175(11), 2743-2761**
  (online 2017, print 2018). *Philosophical Psychology* 31(8) is a real issue
  but this title is not in it (its 1183-1206 slot is not this paper). The
  research note [research/higher-order-theories-consciousness-2026-01-14.md](/research/higher-order-theories-consciousness-2026-01-14/)
  carried the same wrong venue while linking the *Philosophical Studies* PMC
  URL — internally self-contradicting; corrected there too.

- **Block 2011** — "The higher order approach to consciousness is defunct,"
  *Analysis* 71(3):419-431. State: **real-correct.** Vol/issue/pages verified.
  In-body quote "the higher-order approach to consciousness is defunct" is
  verbatim-faithful to the paper title.

- **Brown 2025** — *Consciousness as Representing One's Mind: The Higher-Order
  Approach to Consciousness Explained*, Oxford University Press (April 2025).
  State: **real-correct** (re-confirmed at OUP/publisher; ISBN 9780197784006;
  introduces the HOROR theory). The article's "as qualitative" HOROR
  characterization is faithful.

- **Lau 2022** — *In Consciousness We Trust: The Cognitive Neuroscience of
  Subjective Experience*, OUP 2022. State: **real-correct** (canonical
  flagship; title/publisher/year accurate; PRM characterization faithful).

- **Farrell "ambitious" quote** — the body quotes only the word "ambitious";
  Farrell's paper does distinguish "ambitious" vs modest HOT and argues the
  ambitious variety fails for what-it-is-like-ness. Faithful.

- Canonical books (Armstrong 1968 Routledge, Lycan 1996 MIT, Rosenthal 2005
  OUP, Gennaro 2012 MIT) and Gruber et al. 2015 (*Front. Psychol.* 6:91):
  spot-confirmed, no defects.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Ko/Lau conflation** (wrong author + title + pages) — FIXED, propagated.
- **Farrell wrong venue** (Phil. Psychology → Phil. Studies) — FIXED, propagated.

### Medium / Low Issues Found
- Minor: References L191 renders "higher order" (no hyphen) while the body
  hyphenates the same quoted title. Pre-existing, trivial, quote is faithful;
  left as-is to avoid churn.
- References use repeated "1." markers (auto-numbering idiom). Renders fine;
  left as convention.

### Possibility/Probability Slippage Check
- No slippage. The lead ("HOT describes cognitive architecture rather than
  phenomenal consciousness") is explicitly framework-relative ("From The
  Unfinishable Map's perspective"). The PRM and quantum sections declare the
  Dualism-boundary disagreement honestly ("noted as such, not as something
  PRM's own resources refute"; quantum prediction hedged as "challenging" to
  detect). No tenet-as-evidence upgrade.

### Reasoning-Mode Classification (editor-internal)
- Rosenthal (HOT): Mode Mixed — regress + empirical-dissociation internal
  arguments; tenet-boundary marked honestly.
- Brown (HOROR): Mode Two — unsupported-foundational-move on HOT's own terms.
- Lau (PRM): Mode Two → Mode Three — "by Lau's own standard of mechanistic
  adequacy" then declared bedrock Dualism residue.
- Frankish/Dennett (illusionism): Mode Two — "the representing is itself a
  seeming" works inside illusionism's framework.
- No label leakage: forbidden editor-vocabulary terms absent from prose.

## Attribution Accuracy Check
- All source expositions (Rosenthal's three conditions, Armstrong/Lycan HOP,
  Lycan's retreat, Block's defunct claim, Farrell on ambitious HOT, HOROR "as",
  Lau's PRM) correctly attributed and qualifier-preserving. The Ko-vs-Maniscalco
  fix corrects the one attribution error. No source/Map conflation.

## Optimistic Analysis Summary

### Strengths Preserved (do not change)
- Front-loaded access/phenomenal summary.
- Three-level metarepresentational distinction (Gruber/Jourdain evidence).
- Clean empirical-dissociation table (blindsight / blind insight / aPFC).
- PRM section engaging the strongest HOT variant on its own terms.
- Unity-of-consciousness convergence/divergence section.
- HOROR and illusionism critiques that steelman before objecting.

### Enhancements Made
- None beyond the citation corrections (article is converged; length-safe,
  do-not-grow band).

## Length
- `analyze_length`: 2802 words, 112% of 2500 soft target, `soft_warning`
  (well under 3500 hard). +6 words from corrected (longer) canonical titles —
  unavoidable for accuracy; length-neutral otherwise.

## Cross-links
- Wikilink targets resolve (live/archived). No new links added.

## Remaining Items
None.

## Stability Notes

Seventh deep review. The prose has been stable across five consecutive reviews
with zero prose-level critical issues; the value of this pass — as with the
2026-06-04 pass — was the citation web-verify, which caught two metadata
defects (a two-paper conflation + a wrong venue) that five prior "verified"
reviews missed. Intra-corpus consistency had *ratified* the wrong cites: the
same conflation was replicated verbatim across four sibling files, so
cross-checking against the corpus would only have confirmed the error. Only the
live publisher caught it.

Bedrock disagreements carried forward (do NOT re-flag):
1. Eliminativists/physicalists find the dualist framing question-begging —
   framework-boundary; not correctable inside the tenets.
2. The quantum prediction is speculative — appropriately hedged.
3. Contemplative/Buddhist evidence has inherent limitations — acknowledged.
4. PRM's mechanistic adequacy cannot, by the Map's lights, discharge the
   felt-character question — Dualism-boundary residue, declared honestly.

`ai_modified` + `last_deep_review` bumped to 2026-07-11T09:56:00+00:00 (real
citation fixes). `ai_system` HELD at claude-opus-4-5-20251101.