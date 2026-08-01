---
ai_contribution: 100
ai_generated_date: 2026-07-28
ai_modified: 2026-07-28 22:12:06+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-28
date: &id001 2026-07-28
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-28 22:12:06+00:00
modified: *id001
related_articles: []
title: Deep Review - Objectivity and Consciousness
topics: []
---

**Date**: 2026-07-28
**Article**: [Objectivity and Consciousness](/concepts/objectivity-and-consciousness/)
**Previous review**: [2026-06-25](/reviews/deep-review-2026-06-25-objectivity-and-consciousness/)
**Pass**: 7th deep review. Re-qualified by a body change: a same-day `refine-draft` (commit 209d2b51c) added the missing Levine (1983) References entry and pointed the lead at "Levine's term, discussed below." Completing that citation raised the fidelity bar on the Levine paragraph — and the paragraph did not survive verification at the primary text.

## Verdict: one critical attribution fix, three orphan references resolved, length-neutral

Contrary to the previous review's expectation of a no-op, the primary-text check on the newly-completed Levine citation surfaced a real attribution error that had survived six prior reviews.

## Critical issues found

### 1. Levine's contrast case was not his (fixed)

The article read: *"Joseph Levine (1983) noted that even if 'pain = C-fiber firing' is true, the identity remains explanatorily unsatisfying in a way that 'water = H2O' is not. We can see why water has its properties given H2O's molecular structure…"*

Levine's paper contains **no occurrence of "water" or "H2O"**. Verified by extracting the full text of the paper (informationphilosopher.com and newdualism.org scans of the PPQ original). His numbered statements are:

- (1) Pain is the firing of C-fibers.
- (2) Heat is the motion of molecules.

and his explanatory account of (2) is *"our knowledge of chemistry and physics makes intelligible how it is that something like the motion of molecules could play the causal role we associate with heat."* The water/H₂O pair is the standard **post-Levine** illustration (Kripke-adjacent, popularised via Chalmers and Block–Stalnaker), not Levine's own. Putting it inside a "Levine (1983) noted that…" clause attributes to him an example he never used.

**Fix applied**: the paragraph now quotes Levine's actual statements (1) and (2), names "heat is the motion of molecules" as *his contrast case*, and paraphrases his own chemistry-and-physics-make-intelligible reasoning. The philosophical point — and the Map's stronger ontological reading, explicitly marked as its own position *contra* Levine's epistemic framing — is unchanged.

**Family-resolution note (deferred, corpus-wide)**: the water/H₂O idiom is used across ~14 content articles. In most (`hard-problem-of-consciousness`, `materialism`, `reductionism`, `supervenience`, `philosophical-zombies`, `zombie-master-argument`, `modal-structure-of-phenomenal-properties`, `type-identity-theory`, `arguments-against-materialism`) it is the *Map's own* illustration and is unobjectionable. Two files place it inside a Levine-attribution clause and carry the same defect as the one fixed here:
- `obsidian/concepts/explanatory-gap.md` L62 — "His key insight… Physical identities like 'water = H2O' are explanatorily satisfying"
- `obsidian/topics/leibnizs-mill-argument.md` L69 — "Levine asked why physical-phenomenal identities like 'pain = C-fiber activation' lack the explanatory transparency of 'water = H₂O'"

A P2 task has been queued rather than swept here, since `explanatory-gap.md` is the canonical home for the distinction and warrants its own pass.

### 2. Three orphan References entries (fixed)

Three verified, relevant sources sat in References with no inline citation anywhere in the body — a §2.4 step-5 orphan in the inline↔references direction. The previous review recorded "no inline↔reference orphans," which was too lenient a reading. All three resolved by attaching them to the claims they actually support, rather than by deletion:

- **Tomasello & Carpenter 2007** → now cited at the shared-intentionality claim, which previously asserted the "9-12 months" figure with no support at all.
- **Wolf & Tomasello 2025** → now cited in the Second-Person Phenomenology section for the shared-intentionality account of human social bonding (its actual subject), not for the developmental timing (which it does not address).
- **Cleeremans, Mudrik & Seth 2025** → now cited in the Neurophenomenology section for the field-level call for renewed attention to phenomenology.

## Citation web-verify (§2.4) — per-cite ledger

Triggered: the References block was modified since the last deep review.

- **Levine, J. (1983), "Materialism and Qualia: The Explanatory Gap," *Pacific Philosophical Quarterly* 64, 354-361** — real-correct. DOI 10.1111/j.1468-0114.1983.tb00207.x; the page footer of the original reads "Pacific Philosophical Quarterly 64 (1983) 354-361," so the entry's locator form matches the publisher's own. **Body claim corrected** — see critical issue 1.
- **Cleeremans, A., Mudrik, L., & Seth, A. K. (2025)** — real-wrong-metadata (incomplete). Verified at publisher (frontiersin.org): *Frontiers in Science* **3, 1546279**, DOI 10.3389/fsci.2025.1546279. Volume and article number added; author order and title confirmed correct.
- **Tomasello, M., & Carpenter, M. (2007), "Shared intentionality," *Developmental Science* 10(1), 121-125** — real-correct (PubMed 17181709). *Empirical-claim fidelity caveat*: the abstract frames its subjects as "human 1- and 2-year-olds," not 9-12 months. The 9-12 month onset is Tomasello's own well-established claim (the "9-month revolution" for joint intentionality) but is not the 2007 paper's stated age range. The inline cite is therefore attached to the *term* "shared intentionality" rather than to the age figure, which keeps the attribution faithful.
- **Wolf, W., & Tomasello, M. (2025), *Perspectives on Psychological Science* 20(2), 264-275** — real-correct (locator completed by the previous review; re-confirmed at SAGE).
- **Sandved-Smith, L., et al. (2025), *Neuroscience of Consciousness* 2025(1), niaf016** — real-correct (verified in the 2026-05-26 pass, which corrected a Ramstead→Sandved-Smith misattribution; unchanged since).
- **Nagel 1974** (*Phil. Review* 83(4), 435-450), **Nagel 1986**, **Dennett 1991**, **Varela 1996** (*JCS* 3(4), 330-349) — real-correct, canonical, unchanged.

Prose-only thinker mentions without year-cites (Husserl, McGinn, Stapp, von Neumann–Wigner, Berkeley) carry no `Author YYYY` inline form and so require no References entry under §2.4 step 5; each links to a concept page that carries the citation. Not treated as orphans.

## Currency

`find_superlative_claims` returns zero. No datable empirical-record claims.

## Reasoning-mode classification (§2.6, editor-internal)

- **Dennett / heterophenomenology** — Mode Three. States the phenomenal-realist objection, gives Dennett his own rebuttal in his own terms ("there is no gap between reports and experience"), and locates the disagreement at the bedrock qualia-realism question. No boundary-substitution.
- **Berkeley / idealism** — Mode Three with a Mode One component. The pragmatic and modest-realism arguments mark the boundary honestly; the evolutionary argument is question-begging against a committed idealist and is offered as the Map's reason for its own position, not as a refutation. Unchanged from prior reviews.
- **Label leakage**: grep clean — no editor-vocabulary in prose.

## Calibration check

The quantum section remains the site's highest calibration-risk zone and remains clean: collapse-by-consciousness is flagged "a minority position," "remains contested," and the tenet move stays conditional. No evidential-status upgrade on tenet-coherence alone. A tenet-accepting reviewer would flag nothing as overstated.

## Optimistic pass — strengths preserved

- The three-perspective (first/second/third-person) taxonomy with its "none alone suffices" closer is the article's structural spine. Untouched.
- The Husserl inversion (objectivity *grounded in* intersubjectivity rather than opposed to it) is the piece's most distinctive move. Untouched.
- The honest marking of the Map's ontological reading as stronger than Levine's epistemic one. Untouched.
- The measurement-standards cross-link paragraph (units, instruments, calibration). Untouched.

## Length

2551 → 2553 words (+2). Length-neutral mode observed: ~33 words of citation attachment paid for by ~31 words of genuine duplication removed —
- the third restatement of "objectivity is intersubjective agreement, not elimination of the observer" (the formulation survives twice more, in its proper homes);
- "We don't infer minds; we directly encounter them in social interaction," a verbatim-in-substance repeat of the same claim two sections earlier;
- "Phenomenal consciousness resists the view from nowhere—but multiple conscious perspectives can converge on its features," restated in full by the very next paragraph;
- the third statement of what heterophenomenology brackets, already given at first mention.

Style note: the article contains several instances of the discouraged "This isn't X; it's Y" construct. Per `writing-style.md` these are explicitly **not** to be swept from existing prose ("a guide for *future* writing"), so they were left alone. Future reviews should not re-flag them.

## Remaining items

- Corpus-wide Levine/water-H₂O attribution alignment in `explanatory-gap.md` and `leibnizs-mill-argument.md` — P2 task queued.

## Stability notes

Settled bedrock standoffs — do NOT re-flag: eliminativism vs phenomenal realism; the idealism section's evolutionary rejoinder; MWI indexical brevity; epistemic-vs-ontological gap.

The convergence lesson from this pass: five consecutive reviews recorded "citations verified" for the Levine paragraph on the strength of the *attribution* being right (Levine did coin "explanatory gap," did use C-fibers, did frame it epistemically). The defect was in an *illustrative example* silently swapped for the corpus's house idiom — a defect class that intra-corpus consistency actively conceals, because thirteen sibling articles use water/H₂O and thereby ratify it. Only the primary text catches this. Future passes on citation-bearing articles should check not just *who* and *what year* but *which example the source actually used*.