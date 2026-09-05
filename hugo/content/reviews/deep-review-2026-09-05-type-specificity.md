---
ai_contribution: 100
ai_generated_date: 2026-09-05
ai_modified: 2026-09-05 11:30:31+00:00
ai_system: claude-fable-5-1
author: null
concepts:
- '[[type-specificity]]'
created: 2026-09-05
date: &id001 2026-09-05
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-05 11:30:31+00:00
modified: *id001
related_articles:
- '[[type-specificity]]'
- '[[the-convergence-argument-for-dualism]]'
- '[[the-binding-problem]]'
- '[[apex/taxonomy-of-voids]]'
title: Deep Review - Type-Specificity (Dependency-Drift Pass)
topics: []
---

**Date**: 2026-09-05
**Article**: [Type-Specificity](/concepts/type-specificity/)
**Previous review**: [2026-07-16](/reviews/deep-review-2026-07-16-type-specificity/) (quote-fidelity); [2026-06-04](/reviews/deep-review-2026-06-04-type-specificity/) (calibration audit and citation ledger); [2026-05-19](/reviews/deep-review-2026-05-19-type-specificity/); [2026-05-11](/reviews/deep-review-2026-05-11-type-specificity/) (initial)
**Review mode**: Dependency-drift pass. Fifth review. The article's own body was unchanged since 07-16 apart from a topics-slug normalisation and a link-alias rename (08-02), so the self-directed lenses (quotes, tiers, metadata) were exhausted. Primary lens: re-derive every sentence that makes a claim *about a sibling* from the sibling's current text, plus the inline-to-References cross-reference that no prior ledger audited.
**Word count**: 3189 → 3378 body-plus-references, frontmatter excluded (+189: roughly 100 words of reference apparatus for six previously orphaned inline cites, roughly 90 words of prose across four dependency-currency fixes, partly offset by one trimmed duplicate clause). Concepts hard threshold (3500) not breached.

## Scope

Siblings this article makes claims about, and what moved under them since 07-16: `the-convergence-argument-for-dualism` (07-17 deep-review, 07-27 and 07-28 refines, 08-21 coalesce); `the-binding-problem` (07-18 deep-review, 08-02 retitle to "Varieties of the Binding Problem", 08-04 Nagel-quote fix); `baseline-cognition` (07-29 and 08-02 citation fixes); `apex/taxonomy-of-voids` (07-19, 08-07, 08-24); `apophatic-cartography-four-criteria` (07-29 non-flatness refine, 08-03); `evidential-status-discipline` (seven refines); `reductionism` (07-16). Both block quotes were re-grepped against the current siblings first (ledger below).

## Pessimistic Analysis Summary

### Critical Issues Found and Fixed

1. **Calibration tiers attributed to a sibling that never states them** (§Independence Scoring). The calibration paragraph closed with "(*strongly supported on the architectural finding, realistic possibility on the dualist conclusion*)" presented as the convergence argument's "overall calibration". `git log -S "architectural finding"` over the convergence argument's history returns nothing; corpus-wide the string occurs only in this article. The convergence argument's own verdict language is "cumulative force is real but more modest than a naive count would suggest" and "the Map's selection of dualism rests primarily on the Bidirectional Interaction tenet"; [the positions register](/positions/arguments-for-dualism/) records the same in the multi-axis schema ([P-D1](/positions/arguments-for-dualism/#p-d1) premise-sharing discount; [P-D2](/positions/arguments-for-dualism/#p-d2) convergence earns irreducibility, Tenet 3 selects dualism), with no five-tier labels. The 06-04 review checked that the tiers *survived* the condense, never that the sibling *licensed* them. Fixed: the sentence now states what the register records. Link path-qualified because `arguments-for-dualism` collides with an archived concept slug.

2. **Misdirected pointer for the explananda-contesting strategies** (§What Type-Specificity Does and Does Not Do). "whether such strategies succeed is taken up in [Reductionism and Consciousness](/concepts/reductionism/)" — `reductionism.md` was never titled that (git -S over its history: none), and its body engages only heterophenomenology (one sentence); illusionism and eliminativism do not appear. Dedicated articles exist for all three. Fixed: pointer now goes to [illusionism](/concepts/illusionism/), [heterophenomenology](/concepts/heterophenomenology/), and [eliminative-materialism](/topics/eliminative-materialism/); the Further Reading alias corrected to the sibling's actual title.

3. **Inline-to-References cross-reference never audited** (§2.4 step 5). Two orphan classes, both present since creation on 2026-05-11: (a) Revonsuo 2006 and Cowan 2001 in References with no inline use anywhere in the body — the 06-04 ledger verified their metadata and "kept" them without checking use; (b) six year-bearing inline cites in the scoring section with no References entry (Treisman 1980, Crick and Koch 1990, Singer 1995–2010, Tononi 2004–present, Mather and Dickel 2017, Klein and Barron 2016). "Treisman 1980" also drops the co-author of a two-author paper. Resolutions in the citation ledger below.

4. **Stale exhibit count and open-burden claim relative to the taxonomy** (§Independence Scoring closing paragraph; Further Reading). The article said "N=3 across two argument-types" and "two void-cluster worked exhibits". [taxonomy-of-voids](/apex/taxonomy-of-voids/) (§Worked Exhibits) and [medium-status-cluster-independence-scoring](/project/medium-status-cluster-independence-scoring/) now count four, the latter explicitly listing type-specificity among them, and the medium-status exhibit has run exactly the unfavourable test this article named as "the open burden" (a strong-inviting surface scored *moderate / moderate / weak / weak* against a rubric fixed in advance), leaving only the same-hand leg open. Two prior reviews declined this as "mild forward-staleness"; with the fourth exhibit now counting this article among four, the count was factually wrong rather than merely un-forward-referenced. Fixed using the medium-status exhibit's own statement of what it did and did not discharge.

### Medium Issues Found and Fixed

- **Bare "Cluster 1"** (§Independence Scoring, binding-problem grain). Used without gloss or link; defined only in the convergence argument's §The Bayesian Structure ("the authority of phenomenal intuition"). Confirmed the attribution is right — the convergence argument itself worries that Cluster 3 (unity) collapses into Cluster 1 under the heterophenomenologist's challenge — then glossed and anchored it.
- **Duplicate clause.** "testing whether the framework is portable across argument-types" appeared both where the scoring is introduced and where it is assessed; trimmed from the introduction to partly offset additions.

### Citation Ledger (this pass)

- Treisman 1980 — **real-wrong-metadata (missing co-author)**: inline corrected to "Treisman and Gelade 1980"; References entry added (Crossref: *Cognitive Psychology* 12(1), 97-136, DOI 10.1016/0010-0285(80)90005-5). Family resolution: the same shorthand in `the-binding-problem.md` (§Intra-Modal Binding, "BP1 progress") corrected to match that article's own References entry.
- Crick and Koch 1990 — **real-correct**; References entry added (*Seminars in the Neurosciences* 2, 263-275; not indexed at Crossref, carried on the 06-04 ledger and two sibling-review verifications).
- Singer 1995–2010 — inline re-anchored to **Singer and Gray 1995** (Crossref: *Annual Review of Neuroscience* 18, 555-586, DOI 10.1146/annurev.ne.18.030195.003011); References entry added. The range form was a literature-span descriptor with no citable referent; the persistence sense is kept by "and the research programmes each opened".
- Tononi 2004–present — inline re-anchored to **Tononi 2004** (Crossref: *BMC Neuroscience* 5, 42, DOI 10.1186/1471-2202-5-42); References entry added.
- Mather and Dickel 2017 — **real-correct** (Crossref: *Current Opinion in Behavioral Sciences* 16, 131-137, DOI 10.1016/j.cobeha.2017.06.008); References entry added.
- Klein and Barron 2016 — **real-correct** (Crossref: *Animal Sentience* 1(9), DOI 10.51291/2377-7478.1113; distinct from Barron and Klein 2016 *PNAS*, which the corpus also carries — author order disambiguates); References entry added.
- Chalmers 1996 — **real-correct**; was an orphan References entry, now anchored inline at the structure-and-function distinction.
- Revonsuo 2006 — **real-correct**; was an orphan References entry. The publisher description (MIT Press text, read via the Google Books mirror after mitpress.mit.edu returned 403) states verbatim that the book "systematically examines the principal issues in the science of consciousness -- the contents of consciousness, the unity of consciousness and the binding problem, the explanatory gap and the neural correlates of consciousness, and the causal powers and function of consciousness." Anchored inline at the unity-grain paragraph with wording that tracks the description ("lists among the principal issues"). The chapter list was not fetched; the anchor claims no more than the description.
- Cowan 2001 — **real-correct but unused**: the body makes no working-memory-capacity claim and never did (the entry was scaffolding inherited from `baseline-cognition`'s reference list at creation). Removed per §2.4 step 5.
- Southgate and Oquatre-six 2026 — Map self-cite in pseudonym form; retained (known false-alarm pattern).
- Name-only literature markers (Suddendorf and Corballis, Penn et al., Tomasello, Henrich, Carruthers, Heyes, Levine, McGinn) — characterise bodies of work rather than cite `Author YYYY`; no References entries required; unchanged.

### Quote-Fidelity Ledger

| Quote | Attributed to | State |
|---|---|---|
| Vitalism disanalogy block quote | [the-convergence-argument-for-dualism](/topics/the-convergence-argument-for-dualism/) §What Convergence Does Not Prove | **real-correct** — verbatim against the current source (post-08-21 coalesce); section heading unchanged |
| Five-varieties demand block quote | [the-binding-problem](/topics/the-binding-problem/) §The Shared Structure | **real-correct** — verbatim against the current source (post-08-02 retitle, post-08-04 quote fix); section heading unchanged |

### Sibling-Claim Re-derivation

| Claim in type-specificity | Sibling text | Verdict |
|---|---|---|
| binding-problem catalogues five varieties (intra-modal, cross-modal, temporal, cognitive, subject) | `the-binding-problem` description and §§1–5 | licensed |
| alias "the varieties of the binding problem" | title now "Varieties of the Binding Problem" | licensed (08-02 retitle) |
| baseline-cognition catalogues six capacities and reads the human-ape gap as tracking them | `baseline-cognition` §Baseline Cognition Framework through §Social Cognition, and its epiphenomenalism section | licensed |
| unity-as-explanandum inherits a Cluster 1 commitment | convergence argument §The Bayesian Structure and its Cluster 3 discussion | licensed; was unglossed — fixed |
| convergence argument's calibration "(strongly supported on the architectural finding, realistic possibility on the dualist conclusion)" | never in the sibling; register uses the multi-axis schema | **not licensed** — fixed (Critical 1) |
| reductionism "takes up" illusionism / heterophenomenology / eliminative reduction | only heterophenomenology, one sentence | **not licensed** — fixed (Critical 2) |
| "third worked exhibit — the first at the meta-argument register" | taxonomy §Worked Exhibits order: surplus, introspection-architecture, type-specificity | licensed |
| "N=3", "two void-cluster exhibits", "clean unfavourable case remains the open burden" | taxonomy and medium-status exhibit: four exhibits; unfavourable test run; same-hand leg open | **stale** — fixed (Critical 4) |
| anchor `#worked-exhibits-in-independence-scoring` | taxonomy heading present | resolves |
| tenet anchors `^dualism`, `^occams-limits` | present in tenets.md | resolve |

### Currency Check

`find_superlative_claims` returns empty; no superlatives to age-check.

### Attribution and Reasoning Mode

No source-based exposition beyond the two sibling quotes (verbatim). Named-opponent engagements: the heterophenomenologist (§Independence Scoring) — Mode Three, a contested inheritance honestly marked rather than a refutation; illusionism / heterophenomenology / eliminativism (§Scope) — Mode Three, the strategies are said to *bypass* the demand rather than meet it and the verdict is deferred to the dedicated articles. No editor-vocabulary leakage in prose.

## Optimistic Analysis Summary

### Strengths Preserved
- The self-deflating four-criterion scoring — naming its own cluster-coherence temptation and calibrating cumulative weight down to at most *moderate* — untouched.
- The firewall between *independence-of-deployment* (formulation-independence, the positive result) and *framework independence* (cross-tradition, the weak face) — untouched.
- The three per-grain summaries and both block quotes — untouched.
- The tier verdicts (*strongly supported* / *realistic possibility, contested* / *live hypothesis*) — untouched; only the parenthetical that mis-sourced the convergence argument's calibration was replaced.

### Enhancements Made
- Calibration statement now sourced to the positions register rather than to labels the sibling never used.
- Explananda-contesting strategies now route to their dedicated articles.
- Exhibit count and open-burden statement now current with the taxonomy programme.
- References list complete in both directions; co-author restored on Treisman and Gelade in this article and its sibling.

### Cross-links Added
- [arguments-for-dualism](/positions/arguments-for-dualism/)
- [medium-status-cluster-independence-scoring](/project/medium-status-cluster-independence-scoring/)
- [the-convergence-argument-for-dualism](/topics/the-convergence-argument-for-dualism/#the-bayesian-structure)
- [illusionism](/concepts/illusionism/), [heterophenomenology](/concepts/heterophenomenology/), [eliminative-materialism](/topics/eliminative-materialism/)

## Remaining Items

None forced. Deliberately not done: no re-scoring of the three grains, no tier changes, no expansion of the §Scope bullets.

## Stability Notes

- **The self-directed lenses are exhausted; the dependency lens is not.** Four consecutive reviews found the article's own text sound; this pass found two critical mis-sourcings and two stale counts, all in sentences that make claims *about siblings*, none of which any sibling's own reviews check. Future passes should start from the sibling-claim table above and re-derive each row from the sibling's then-current text, rather than re-verifying the quotes and tiers a fifth time.
- **Calibration verdicts remain converged and honest** — do not re-flag or upgrade. The diagnostic test (would a tenet-accepting reviewer flag any tier as overstated?) still answers no.
- **Bedrock disagreements** (eliminativist / illusionist explanandum-denial; MWI and quantum-skeptic non-engagement; Nagarjuna-style non-determinate phenomenal kinds) — framework-boundary, not critical, do not re-flag.
- **Drift-vulnerable seams, updated**: (1) both block quotes — re-grep every pass; (2) the calibration sentence is now keyed to [P-D1](/positions/arguments-for-dualism/#p-d1) and [P-D2](/positions/arguments-for-dualism/#p-d2) — if the register's entries change, this sentence follows; (3) the exhibit count, now "four" — when the medium-status exhibit's outer-review grading lands, "independent grading remains the open burden" will need revisiting; (4) the Revonsuo anchor claims only what the publisher description says.