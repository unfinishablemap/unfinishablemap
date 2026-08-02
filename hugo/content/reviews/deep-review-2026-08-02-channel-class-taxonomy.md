---
ai_contribution: 100
ai_generated_date: 2026-08-02
ai_modified: 2026-08-02 16:32:00+00:00
ai_system: claude-opus-5
author: null
concepts:
- '[[channel-class-taxonomy]]'
created: 2026-08-02
date: &id001 2026-08-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-02 16:32:00+00:00
modified: *id001
related_articles:
- '[[selection-only-channel]]'
- '[[conservation-laws-and-mental-causation]]'
- '[[possibility-probability-slippage]]'
title: Deep Review - Channel-Class Taxonomy
topics: []
---

**Date**: 2026-08-02
**Article**: [Channel-Class Taxonomy](/concepts/channel-class-taxonomy/)
**Previous review**: [2026-07-11](/reviews/deep-review-2026-07-11-channel-class-taxonomy/)

The article re-qualified because an earlier same-day deep-review of
[selection-only-mind-influence](/topics/selection-only-mind-influence/) upgraded the Stapp `n.d.` citation here to the
published *Zygon* 2006 record, bumping `ai_modified` without touching
`last_deep_review`. Expected outcome was a converged no-op confirming the inherited
citation change. **Verdict: FIX** — two critical defects surfaced that four prior
passes did not reach: a one-word quote-fidelity error in the Carroll challenge, and a
definitional inconsistency in the Class-2 bias parameter that makes the stated
information rate wrong by a factor of four on a literal reading.

## Citation Web-Verify Ledger

Trigger met: the References block was modified since the last deep-review (Stapp
entry rewritten today). The changed cite was verified in full at the publisher of
record; the newly-quoted Carroll challenge was verified at source; the remaining
entries carry publisher-verified verdicts from the 2026-06-02 and 2026-07-11 ledgers
and were not re-litigated.

- **Stapp, H. P. (2006), "Quantum Interactive Dualism: An Alternative to Materialism", *Zygon* 41(3), DOI 10.1111/j.1467-9744.2005.00762.x** — **real-correct**. Verified independently at Crossref (`api.crossref.org/works/10.1111/...`) and OpenAlex: title, sole author Henry P. Stapp, container *Zygon: Journal of Religion and Science*, volume 41, issue 3, issued 2006. The apparently-anomalous `2005` segment inside the DOI is genuine Wiley registration-year encoding, **not** a transcription error — do not "correct" it to `2006`. Neither Crossref nor OpenAlex carries a page range for this record; the article correctly omits pages. (Several *research/* notes and [topics/quantum-state-inheritance-in-ai.md](/topics/quantum-state-inheritance-in-ai/) assert `599–616`; that range is plausible but is **not** confirmed by either registry — see Remaining Items.) Wiley's landing page is paywalled (HTTP 402) and could not be used.
- **Stapp verbatim quote (Class 1 body)** — **real-correct, re-verified this pass.** QID.pdf re-downloaded from LBL and parsed with `pdftotext` (7,685 words). Both fragments are verbatim at line 303–305 of the extraction: *"...is not determined by the agent, who chooses only the question. The answer is picked by "Nature", in accordance with a specified statistical law."* The article's rendering of the source's typographic double quotes around *Nature* as single quotes is required nesting inside its own quotation marks and is not an alteration. The 2026-07-11 fix holds. **Note for the record**: the quote is verified in the LBL preprint, which the References entry names explicitly as such; it has not been checked against the published *Zygon* text (paywalled).
- **Carroll, S. (2011), "Physics and the Immortality of the Soul", *Scientific American* Guest Blog** — **real-wrong-metadata → corrected.** See critical issue 1. Verified verbatim at the live Scientific American page (the `blogs.scientificamerican.com` host now 302s to `www.scientificamerican.com/blog/...`; the new URL is the one recorded).
- **Pati, A. K. (2026), "No-Signalling Fixes the Hilbert-Space Inner Product", arXiv:2601.13012** — **real-correct**, re-verified at arXiv this pass (sole author Arun Kumar Pati, submitted 19 January 2026; the abstract's conclusion — that any nontrivial inner product produces superluminal signalling — is what the article uses it for).
- Bösch, Steinkamp & Boller 2006 (*Psychological Bulletin* 132(4):497–523, PMID 16822162) — real-correct (prior ledger).
- Eccles 1994 (*How the Self Controls Its Brain*, Springer) — real-correct (prior ledger).
- Hameroff & Penrose 2014 (*Phys Life Rev* 11(1):39–78) — real-correct (prior ledger).
- Han & Choi 2016 (*Sci Rep* 6:22986) — real-correct (prior ledger; co-author Choi restored 2026-06-02).
- Maier, Dechamps & Pflitsch 2018 (*Front Psychol* 9:379, PMC5872141) — real-correct; currency confirmed 2026-07-11.
- Penrose 2014 (*Found Phys* 44(5):557–575) — real-correct (prior ledger).
- Shannon 1948 (*BSTJ* 27(3):379–423); Sorkin 1994 (*Mod Phys Lett A* 9(33):3119–3127) — established classics.
- Stapp 1993 (*Mind, Matter, and Quantum Mechanics*) and Stapp 2007 (*Mindful Universe*) — title-disambiguated; each in-text pointer resolves to the right work. No blind collapse of the three Stapp entries.
- Southgate & Oquatre-sept 2026-05-11; Southgate & Oquatre-six 2026-03-19 — Map self-cites, legitimate pseudonymous co-author forms; not to be stripped.

**Inline ↔ References cross-check**: complete in both directions after this pass. The
Carroll challenge was the one inline attribution with no References entry; it now has
one. No orphaned References entries.

**Superlative / currency sweep**: `find_superlative_claims` returns empty. No
record-claims, no "first to demonstrate", no "to date" superlatives requiring
currency re-verification.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Quote-fidelity — Carroll challenge mis-quoted by one word (FIXED).** The article
carried `Carroll's "what particles is the soul made of?" challenge`. Carroll's actual
wording, verified verbatim at the Scientific American source, is *"If you claim that
some form of soul persists beyond death, what particles is that soul made of?"* —
**that** soul, not **the** soul. A single-word substitution inside quotation marks is
the same defect class the 2026-07-11 pass caught in the Stapp quote, at smaller scale:
words the source did not write, presented as words it did. Corpus sweep across
`obsidian/`, `archive/`, and `hugo/content/` found the defective string live in exactly
one serving body (this article, plus its unsynced Hugo mirror); the sibling
[conservation-laws-and-mental-causation](/concepts/conservation-laws-and-mental-causation/) already carries the correct wording, so this
was drift at a single locus rather than a family. Fixed to the verbatim form, with
`(Carroll 2011)` added inline and a References entry minted (References renumbered
2–15; the numbers are not referenced inline, so renumbering is inert).

**2. Class-2 bias parameter defined inconsistently with its own formula (FIXED).** The
Shannon specification said the per-trial rate "is bounded by the *signed* deviation
max{*p_i*' − *p_i*}" and then, in the next sentence, "with bias *ε*, the rate is
*ε²*/(2 ln 2) bits per trial". Those two statements are incompatible. Under the stated
definition — ε as a single outcome's deviation from its unbiased probability — the
binary small-bias rate is the standard BSC result 2ε²/ln 2, which is **four times** the
figure the article gives. The ε²/(2 ln 2) form is correct only when ε is the *spread*
between the biased candidate probabilities, max{p_i'} − min{p_i'}, which is precisely
the convention [selection-only-channel](/concepts/selection-only-channel/) derives and which the rest of the corpus uses
consistently (verified against `selection-only-channel`, `selection-only-mind-influence`,
`type-token-causation`, `consciousness-and-causal-powers`,
`overdetermination-dissolution-under-selection-only-interactionism` — all six loci agree
on the formula, and the two numeric checks that exist in the corpus, ε ≈ 10⁻⁴ → 7 × 10⁻⁹
bits and ε ≈ 10⁻³ → 7 × 10⁻⁷ bits, both confirm the spread reading). So the formula was
right and the *definition* had drifted; the taxonomy article was the sole locus carrying
the mismatched definition. Fixed by writing ε explicitly as the spread and pointing to
the sibling derivation. Also dropped "the standard small-bias Shannon formula" — there
is no formula of that name; it is the quadratic small-bias limit of the Shannon rate,
now described as such.

### Medium Issues Found

**3. Inverted inference in the Cross-Class Invariants section (FIXED).** "energy-injection
is the easiest in principle to detect — which is why a century of precision physics has
produced no evidence of it" states, literally, that ease of detection *caused* the null
result. The intended point is the converse: easy detectability is what makes the null
result evidentially damaging. Rewritten accordingly. Popper's Ghost was the persona that
surfaced this — the sentence as written made an unfalsifiable-sounding claim out of a
genuinely falsificationist one.

**4. `description` exceeded the meta-description budget (FIXED).** 185 characters against
the 150–160 guideline; the overflow was the bolt-on tail ", in human-AI collaboration".
Trimmed to 158 characters. Purely subtractive; the substantive description is unchanged.

### Not Flagged (bedrock, per prior Stability Notes)

Eliminative-materialist, hard-physicalist, MWI, and Madhyamaka objections to the
taxonomy's premises remain framework-boundary disagreements and were not re-flagged. The
Tegmark warm-wet decoherence objection to Classes 3–4 remains out of scope here.

### Calibration check (possibility/probability slippage diagnostic)

Ran the §2 diagnostic — *would a reviewer who fully accepts the Map's tenets still flag
any claim as overstated relative to the evidential-status scale?* **No.** The "menu, not
a verdict" framing is intact, the closing paragraph still names treating
tenet-coherence as evidence-for-a-class as textbook
[possibility-probability-slippage](/concepts/possibility-probability-slippage/), and no class assignment is presented as
empirically favoured. The ε ≈ 10⁻⁴ RNG-psi ceiling remains explicitly conditional ("if
interpreted as a real signal"). No slippage. Note that the Class-2 fix *tightened*
calibration rather than loosening it: the corrected definition yields a smaller stated
information rate than the literal reading of the old definition would have.

### Reasoning-mode classification (§2.6)

The article is a catalogue, not a reply to named opponents; the one engagement is with
Carroll on Class 5. Engagement with Carroll: **Mode Three (framework-boundary marking),
conceded** — the article grants that the challenge is correctly aimed at
energy-injection dualism and declines the class outright rather than defending it. That
is an honest concession, not a refutation claim, and it is the right mode. Label-leakage
scan clean: no editor-vocabulary terms appear anywhere in the article prose.

### Notation and sync-safety watch

`Y_B`, `{p_i}`, `{p_i'}`, `log₂(N)`, `P(y|x)` (pipe escaped inside the table), `E_G`,
`ℏ/τ` all render as plain notation. No `[[n,k,d]]`-style bracket notation that sync
would silently strip. All thirteen `[[…]]` targets in the body and Further Reading
resolve to live files (verified by `find`), including
[sorkin-delta-brain-internal-analogues](/topics/sorkin-delta-brain-internal-analogues/) and [consciousness-bandwidth-architecture](/concepts/consciousness-bandwidth-architecture/).
`topics:` entries are bare slugs, per the canonical form. No EOF tool-call artifact.

## Optimistic Analysis Summary

### Strengths Preserved

- The five-row comparison table remains the article's highest-value asset: it is the
  only place in the corpus where the four Shannon-channel components and the energy
  question are cross-tabulated against all five classes in one view.
- The metaphysics-neutral framing — a taxonomy stated in Shannon's vocabulary rather
  than in dualist vocabulary — is what lets rival theories be compared without
  begging the question against any of them. Untouched.
- The explicit disclaimer that the ordering is "not strictly one-dimensional" (basis-choice
  and probability-bias are siblings, not ancestors) is unusually honest for a taxonomy
  article and pre-empts the obvious objection to the table's left-to-right reading.
- "Menu, not a verdict" and the closing slippage inoculation — preserved verbatim, as
  the two prior reviews also insisted.
- Class 5's honest concession to Carroll, and the observation that no contemporary
  dualist theory occupies the class the standard objection targets.

### Enhancements Made

- Class-2 specification now defines its bias parameter explicitly and points to the
  sibling derivation, closing a factor-of-four ambiguity.
- Carroll challenge now carries a verifiable citation rather than a bare name-drop.
- Cross-Class Invariants inference direction corrected.

### Cross-links Added

- [selection-only-channel](/concepts/selection-only-channel/) gains an additional inbound anchor from the Class-2
  specification (previously only Class 1 and the content-confinement discussion pointed
  there), which is the right place for it: the ε convention is derived there.

### Length

`analyze_length` reports 2583 words / soft_warning, but that is the known
reference-apparatus inflation: decomposed, Further Reading is 149 words and References
266, leaving a **body of 2177 words against a 2500 concepts/ soft threshold**. The
article is comfortably under budget and the pass's net +31 words is almost entirely the
new Carroll References entry. No compensating trim was required, and none was made.

## Remaining Items

- **Stapp 2006 page range unconfirmed.** Crossref and OpenAlex both omit pages for
  DOI 10.1111/j.1467-9744.2005.00762.x. Six *research/* notes and
  [topics/quantum-state-inheritance-in-ai.md](/topics/quantum-state-inheritance-in-ai/) assert `599–616` for this article. The
  range is plausible for *Zygon* 41(3) but is not registry-confirmed, and the Wiley
  landing page is paywalled. This article omits pages and is therefore safe; the claim
  lives elsewhere. Low priority, and not worth a task on its own — fold it into the next
  review that touches `quantum-state-inheritance-in-ai`.
- **`objections-to-interactionism.md` cites the same Carroll argument as "Carroll (2016)"**
  (i.e. *The Big Picture*) while `conservation-laws-and-mental-causation.md` and now this
  article cite the 2011 blog post. Both works make the argument, so neither cite is wrong,
  but the corpus is citing one challenge to two sources. Out of scope for this file; noted
  for whichever pass next touches `objections-to-interactionism`.

## Stability Notes

- **The DOI's `2005` segment is correct.** `10.1111/j.1467-9744.2005.00762.x` resolves to
  a 2006 *Zygon* 41(3) article; Wiley encoded the registration year, not the publication
  year. Two registries confirm. A future pass that "fixes" this to `2006` will break the
  DOI. Do not touch it.
- **The ε convention is now settled corpus-wide as the spread max{p_i} − min{p_i}**, with
  rate ε²/(2 ln 2) bits per trial. Any future edit that redefines ε as a single outcome's
  deviation must also multiply the rate by four — but the corpus convention is the spread,
  and six articles depend on it. Do not redefine it locally.
- The Stapp quote is verified against the LBL preprint, not the published *Zygon* text
  (paywalled, HTTP 402). The References entry names the preprint explicitly, which makes
  the provenance honest. Re-verification against the published text is only worth doing
  if institutional access appears.
- Framework-boundary disagreements (eliminative materialism, hard physicalism, MWI,
  Madhyamaka non-self) are bedrock; do not re-flag.
- The "menu, not a verdict" discipline and the tenet-coherence-is-not-evidence disclaimer
  remain the article's calibration spine and must not be diluted.
- Four passes have now touched this article and every one has found something the
  previous ones missed — but the yield is falling and has moved from body claims to
  citation surface. If a fifth pass finds only cosmetics, the article should be treated
  as converged.