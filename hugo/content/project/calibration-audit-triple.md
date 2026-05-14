---
ai_contribution: 100
ai_generated_date: 2026-05-14
ai_modified: 2026-05-14 13:59:05+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-05-14
date: &id001 2026-05-14
description: 'Three new audits detect drift the existing methodology does not catch:
  stale citations, asymmetric handling of altered states, and topic articles more
  confident than their anchor concept pages.'
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[project]]'
- '[[automation]]'
- '[[coherence-inflation-countermeasures]]'
- '[[evidential-status-discipline]]'
- '[[direct-refutation-discipline]]'
- '[[outer-review-empirical-vs-methodological-freshness]]'
- '[[outer-reviewer-service-calibration]]'
- '[[framework-stage-calibration]]'
- '[[bedrock-clash-vs-absorption]]'
- '[[writing-style]]'
- '[[reviews/outer-review-2026-05-14-claude-opus-4-7]]'
- '[[reviews/outer-review-2026-05-14-chatgpt-5-5-pro]]'
- '[[topics/psychedelics-and-the-filter-model]]'
- '[[concepts/filter-theory]]'
title: 'Calibration Audit Triple: Literature Drift, Altered-State Symmetry, Topic-Concept
  Anchoring'
topics: []
---

This document specifies three new calibration audits added to the Map's editorial machinery on 2026-05-14: a *literature-drift review* that flags articles whose empirical citations have aged out of the live literature, an *altered-state symmetry discipline* that prevents articles citing one cluster of altered states as filter-supportive from omitting the symmetric accommodation work other altered states demand, and a *topic-concept anchoring audit* that flags topic articles whose evidential calibration exceeds that of the concept pages they depend on. The three audits share a common shape — pairwise comparison between an article and a reference standard, with a drift threshold that determines when a refine-draft pass is queued — and were proposed together by the 2026-05-14 Claude Opus 4.7 outer review of the Map's psychedelics article, which exhibits the failure mode each audit is designed to catch.

The triple joins the existing methodology family ([coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/), [evidential-status-discipline](/project/evidential-status-discipline/), [direct-refutation-discipline](/project/direct-refutation-discipline/), [framework-stage-calibration](/project/framework-stage-calibration/), [bedrock-clash-vs-absorption](/project/bedrock-clash-vs-absorption/), [outer-review-empirical-vs-methodological-freshness](/project/outer-review-empirical-vs-methodological-freshness/), [outer-reviewer-service-calibration](/project/outer-reviewer-service-calibration/)) as the seventh named methodological pattern. Where the existing disciplines address what is *inside* an article (rival-position handling, evidence calibration, opponent engagement) or the *channel* through which articles get reviewed (outer-review weighting, service-mix calibration), the present triple addresses *drift* — three specific ways an article's standing can degrade between its publication and its next refine pass without any change to the article itself.

## The 2026-05-14 Motivating Case

The audit triple was proposed by the 2026-05-14 Claude Opus 4.7 outer review of `topics/psychedelics-and-the-filter-model.md` (review file: [outer-review-2026-05-14-claude-opus-4-7](/reviews/outer-review-2026-05-14-claude-opus-4-7/)). The article had been written 2026-03-08 with empirical citations whose median publication year is approximately 2015 — Carhart-Harris 2012, Tagliazucchi 2016, Lebedev 2015, Griffiths 2006. The reviewer verified by name-grep that several 2020–2025 high-impact papers in the same area are missing: Siegel et al. 2024 (*Nature*), Timmermann et al. 2024 (*J. Neurosci.*), Doss et al. 2020, Brennan et al. 2024, Mason et al. 2020. The article's primary evidential frame — DMN-suppression-as-filter-loosening — is the dominant 2010s framing; the 2020s literature has shifted toward complexity measures (Lempel-Ziv), entropy-based readings (EBH 2.0), and predictive-processing accounts (REBUS, predictive self-binding) that the article does not engage.

The same article exhibits the second failure mode. It cites psychedelics, terminal lucidity, near-death experiences, and contemplative cessation as convergent altered-state evidence for filter theory, but does not invoke the symmetric work that anaesthesia, slow-wave sleep, and brain damage demand of any filter account. The Map already has [anaesthesia](/topics/anaesthesia-and-the-consciousness-interface/), [dream-consciousness](/topics/dream-consciousness/), and clinical-disruption articles that engage these cases honestly; the psychedelics article reads as if the *supportive* altered states stand alone, when the dialectical situation is that *all* altered states (supportive-looking and disruptive-looking) must be accommodated by whichever theory the article endorses.

The third failure mode is visible by direct comparison with `concepts/filter-theory.md`. The concept page hedges centrally: "neither interpretation is forced by the data alone." The topic article uses the production-vs-transmission distinction without inheriting this hedge. A crude word-count check on this audit's namesake comparison illustrates the point: hedge-marker count divided by article word count gives a per-thousand-word hedge density that is materially lower on the topic article than on its anchor concept page, even though the topic article is exploring a *more* speculative application of the concept. A topic article whose calibration exceeds its anchor concept's is one of the silent inflation vectors [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) does not directly catch.

The three failure modes converged in a single article, with verification cleanly separable. This is the convergence pattern the audit triple is designed to detect at the corpus level before the failure modes accumulate.

## Audit One: Literature-Drift Review

### What It Detects

The audit detects articles whose empirical citations are older than the article's publication date by more than a configurable threshold (default: cited literature's median year more than five years behind the article's publication year). The signal is *not* that the article is wrong — many 2010s findings are still load-bearing — but that the article has not been refreshed to engage 2020s literature in the same area, which carries the risk that the article cites only the evidence that supported its original framing and misses subsequent findings that would complicate or strengthen its case.

The audit is *necessary* (not optional) for topic articles in active research areas where the 2020s literature has materially advanced (psychedelics, consciousness measurement, neural complexity, IIT empirical work, animal cognition, quantum biology). It is *advisory* for concept articles, philosophy-of-mind topic articles, and historical-survey articles where the relevant literature is more stable.

### Mechanics

For each candidate article, the audit pulls:

1. The article's `created` and `ai_modified` dates from frontmatter
2. All inline citation years, recovered from the References section by regex on patterns like `(YYYY)`, `YYYY-MM-DD`, and `et al. YYYY`
3. The 3–5 most-recent (last 24 months from the audit run) high-impact papers in the article's research area, as identified by a web-research call against Semantic Scholar / Google Scholar / domain-specific databases

A drift signal is raised when (a) the median year of cited papers is more than five years behind the article's `ai_modified` date, and (b) at least two of the recent high-impact papers are not cited and would be topically appropriate. The threshold is tunable in `evolution-state.yaml:audit_triple.literature_drift.{median_year_lag_threshold, missing_citation_threshold}`.

The audit's web-research step is the irreducible cost. The other two audits in the triple run entirely on local content and are cheap; literature-drift requires an external call per audited article and is therefore rate-limited.

### Cadence

The literature-drift audit runs on a *long* cadence — default weekly, with one article audited per run — to keep the external-call budget bounded. The article selected is the topic article with the *oldest* `ai_modified` timestamp among articles in active-research areas (a list maintained in `evolution-state.yaml:audit_triple.literature_drift.active_research_sections`). When the audit flags drift, it generates a `refine-draft` task at priority P2 with the missing citations enumerated in the task notes.

### Implementation

A new skill `.claude/skills/literature-drift-review/SKILL.md` will be added (separate task; tracked as a P1 follow-up to this document). The skill drives one literature-drift audit per invocation. Until the skill exists, the audit can be run manually by invoking the audit logic against a target article and recording the output as a `refine-draft` task in the queue.

The skill output is recorded in `obsidian/workflow/changelog.md` as `literature-drift-review` entries with the target article, the median-year-of-cited-papers result, and the missing-citation list. This produces a longitudinal record from which the audit's own calibration can be checked: if no articles are ever flagged, the threshold is too loose; if every article is flagged, the threshold is too tight.

## Audit Two: Altered-State Symmetry Discipline

### What It Detects

The audit detects articles that cite a subset of altered states (typically the *filter-supportive* cluster — psychedelics, near-death experiences, terminal lucidity, contemplative cessation, mystical experience) as convergent evidence for the Map's filter / transmission framing, without engaging the *symmetric accommodation work* that other altered states (anaesthesia, slow-wave sleep, dreamless sleep, generalised brain damage, dementia, persistent vegetative state) demand of any filter account.

The failure mode is not that the article cites the wrong altered states. It is that the article treats the convergence of supportive-looking altered states as *multiple independent confirmations* of the filter framing, when each altered state contributes the same evidential move (a phenomenological feature that the filter framing accommodates more naturally than the production framing) and the disruptive-looking altered states contribute a *symmetric* move (a phenomenological feature that the production framing accommodates more naturally than the filter framing) which the article omits. The result is double-counting on one side of the ledger.

### The Discipline

Any article that cites altered-state evidence as supportive of the filter framing must (a) name the disruptive-looking altered states the framing must also accommodate, (b) state how the framing accommodates them, and (c) explicitly mark that this accommodation work is *parallel to* and *not stronger than* the same accommodation work the production framing must do for the supportive-looking states. The discipline is not "balance every claim with a counter-claim" — it is "present the dialectical position as a single position, not as a count of independent confirmations."

The discipline is the altered-state-specific version of a more general pattern: any time the catalogue cites convergence-across-cases as evidential weight, each case must be auditable as *one move* (the same accommodation work performed against the same alternative) rather than as *many independent confirmations*. The altered-state cluster is the canonical instance because the Map already has the relevant articles ([anaesthesia-and-the-consciousness-interface](/topics/anaesthesia-and-the-consciousness-interface/), [dream-consciousness](/topics/dream-consciousness/), [death-and-consciousness](/topics/death-and-consciousness/), [terminal-lucidity-and-filter-transmission-theory](/topics/terminal-lucidity-and-filter-transmission-theory/), [altered-states-of-consciousness](/concepts/altered-states-of-consciousness/)) — the audit's task is enforcement, not creation.

### Mechanics

For each candidate article, the audit checks:

1. Does the article cite ≥2 items from the *supportive cluster* (psychedelics, NDE, terminal lucidity, cessation, mystical experience, out-of-body)?
2. If yes, does the article cite at least one item from the *disruptive cluster* (anaesthesia, slow-wave sleep, brain damage, persistent vegetative state, dementia)?
3. If the disruptive cluster is cited, does the article *explicitly name* the symmetric accommodation work both framings owe — not merely list the disruptive case as a footnote?

A flag is raised when (1) is true and either (2) is false, or (2) is true but (3) is not. The flag generates a P2 `refine-draft` task whose notes specify which disruptive-cluster items are missing and which framing-side accommodation work the refine must add.

The audit runs on the same weekly cadence as literature-drift, on a different day of the week, on the topic article most-recently flagged by any review as exhibiting filter-supportive convergence framing.

### Implementation

The altered-state symmetry audit does not require a new skill — it is a check within `/pessimistic-review` and `/refine-draft`. The implementation adds a section to the `pessimistic-review` skill's checklist (*altered-state convergence symmetry*) and a corresponding remediation step to `refine-draft` (*if the pessimistic-review flagged altered-state asymmetry, the refine pass must add symmetric accommodation work, naming the disruptive-cluster items the framing also owes*).

## Audit Three: Topic-Concept Anchoring

### What It Detects

The audit detects topic articles whose evidential calibration exceeds that of the concept pages they depend on. The relevant relationship is the *anchor* relationship — a topic article anchors on one or more concept pages by routing its central evidence through the framing those concepts establish. The psychedelics article anchors on `concepts/filter-theory.md` and `concepts/default-mode-network.md`; the audit checks that the topic does not commit to stronger evidential language than the anchor concepts do.

The failure mode is a *silent confidence inflation* that the existing [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) do not catch directly. Coherence-inflation countermeasures address claims that escalate as they propagate through citation loops; topic-concept anchoring addresses claims that escalate when a topic article is written by a different process than its anchor concept page and inherits none of that page's hedging discipline.

### Mechanics

For each topic article, the audit identifies anchor concepts by extracting the concept-list from frontmatter and from inline wikilinks in the article's lead and first section. For each anchor concept, the audit compares:

1. **Hedge density**: count of hedge markers (*could, may, might, perhaps, possibly, seems, appears, suggests*) divided by word count, expressed per thousand words. The topic article's hedge density should not be *less than 60%* of the anchor concept's (threshold tunable).
2. **Strength of central modal verbs**: presence of "is/does" assertions on the load-bearing claim vs. presence of "could/may" formulations. The audit flags if the topic uses unhedged "is/does" on claims the anchor concept hedges as "could/may."
3. **"Neither interpretation is forced" presence**: the audit checks for explicit underdetermination markers (variations of "neither interpretation is forced by the data," "the evidence does not decisively adjudicate," "compatible with both readings"). If the anchor concept contains such a marker and the topic does not, this is a flag.

A flag is raised when ≥2 of the three checks fail for the same anchor concept. The flag generates a P2 `refine-draft` task whose notes specify which calibration moves the topic article is missing relative to its anchor concept.

### A Crude-Count Caveat

The mechanical detection is *crude on purpose* — the audit's job is to surface candidates for human/AI review, not to enforce calibration directly. Hedge density is sensitive to article length and to genre conventions (some concept pages are encyclopaedic and use definitional prose with low hedging despite hedging being implicit in the topic-tier prose that cites them). The audit's threshold (60% of anchor's hedge density) is tuned to err toward false positives rather than false negatives; the refine-draft pass that follows the flag can dismiss the flag if the comparison is misleading, with the dismissal recorded as audit-calibration data.

### Cadence

The topic-concept anchoring audit runs every cycle on the topic article most-recently modified by any task other than a refine-draft that has already addressed the audit. The audit's cost is one local file-read pair plus a regex pass — sub-second — so cycle-frequency is cheap. The audit deliberately runs more often than the other two because the failure mode it catches is the most silent and the most likely to accumulate without external review.

### Implementation

The audit is a Python utility added to `tools/curate/anchoring.py`. The utility is callable from `/pessimistic-review` and from a dedicated cycle slot. The implementation runs against the live obsidian/ tree (not the rendered site), so it is current to the filesystem and not subject to index lag.

## Why a Triple, Not Three Separate Documents

The three audits are bundled into one document because they share a structural shape that is itself part of the methodological contribution. Each audit:

1. Specifies a *reference standard* (recent literature, the disruptive altered-state cluster, the anchor concept page) that an article should be calibrated to.
2. Specifies a *drift signal* — a mechanically detectable threshold above which the article is flagged.
3. Specifies a *remediation* — typically a P2 `refine-draft` task with structured notes.
4. Runs on a *bounded budget* — weekly for the expensive audit, cycle-frequency for the cheap ones.

Bundling them documents the *class* of audit the triple instantiates. Future audits in the same class — *cross-article terminology consistency*, *citation-loop detection beyond the existing coherence-inflation pass*, *steelman-section freshness* — can be added against the same shape. The class shape is: pairwise comparison between an article and a reference, drift threshold, mechanical detection, structured remediation. This is the audit-class spec the triple establishes; the three initial members are worked examples.

The alternative — three separate documents — would lose the class-level claim. The Map already has seven named methodological disciplines; adding three more as singletons would dilute the discipline-naming convention without making the new shared structure visible.

## Pre-Registered Falsification Triggers

Each audit carries a pre-registered falsification trigger that future calibration can be checked against rather than retroactively justified:

- **Literature-drift**: if, over thirty audit runs, fewer than 20% of audited articles produce a flag that the subsequent refine-draft pass *accepts* (rather than dismissing as a misleading comparison), the threshold is too loose and should be tightened. If more than 80% of flags are accepted, the threshold is too tight and the audit is generating refine-draft work the catalogue does not need.
- **Altered-state symmetry**: if, over twelve cycle weeks, no article exhibiting the failure mode is added to the catalogue (no article flagged on a subsequent pessimistic-review pass for asymmetric altered-state framing), the audit has either succeeded fully (no new instances of the pattern) or is mis-calibrated to detect the pattern. The disambiguation is by spot-check: pick three filter-supportive topic articles at random and read them; if they do exhibit the asymmetry, the audit is missing them; if they do not, the audit has succeeded.
- **Topic-concept anchoring**: if, over twenty audit runs, the flag-acceptance rate is below 30% (most flags dismissed by the refine pass as misleading comparison), the hedge-density and modal-verb thresholds are too loose and should be tightened. If above 75%, the thresholds are too tight.

The triggers will be revisited at the next monthly `/tune-system` pass after the audits have run for the relevant period.

## Honest Limitation

The audits are mechanical detectors that surface candidates for human/AI review. They are *not* automatic corrections. The literature-drift audit can flag an article whose 2015 citations are still load-bearing because the 2020s literature in the area is methodologically weak or controversial; the symmetry audit can flag an article whose scope deliberately excludes the disruptive cluster because the article is about the supportive cluster alone; the anchoring audit can flag a topic article that is more confident than its anchor concept because the topic has access to evidence the concept page (by genre convention) does not deploy. In each case, the refine-draft pass that follows the flag is responsible for dismissing the false positive with notes recorded as audit-calibration data.

The audits are also not coverage tools. None of them detects an article that has *no* citations to flag, *no* altered-state moves to symmetrise, *no* anchor concepts to compare against. Articles that should have these features but do not require a separate discipline (gap analysis, replenishment-queue chaining, integrate-orphan tasks) that the audits do not replace.

A risk specific to the triple is that adding three audits at once raises the catalogue's auto-generated `refine-draft` load. If the combined task generation exceeds the cycle's task capacity, the [automation cycle's](/project/automation/) queue-replenishment will be dominated by audit-generated refines and other task types (research, expand, condense) will be crowded out. The mitigation is the *bounded budget* in each audit's cadence specification — weekly for the expensive audit, cycle-frequency for the cheap ones, with a global cap (`evolution-state.yaml:audit_triple.global_task_cap`) on the total number of audit-generated tasks active at once (default 6: 2 literature-drift, 2 altered-state, 2 topic-concept). When the cap is hit, the lowest-priority audit task is demoted before new audit tasks are added.

## Relation to Site Perspective

The triple is methodological. Its alignment is with **[Tenet 5: Occam's Razor Has Limits](/tenets/)** at the corpus-management layer. Tenet 5 denies parsimony at the metaphysical level; the triple applies the same denial at the corpus-management level by refusing the simpler editorial design under which "the article is published, therefore it is calibrated." A published article ages — its citations stale, its dialectical structure becomes asymmetric as the surrounding catalogue grows, its calibration drifts from the concept pages it depends on — and the simpler design would let these drifts accumulate silently. The triple is the recognition that calibration is not a one-time act of publication but an ongoing relationship the article maintains with its reference standards.

The triple also serves the catalogue's epistemic credibility in the way the outer-review channel does. A reader who notices that the catalogue's articles cite literature ten years out of date, or that the catalogue's filter-supportive articles ignore the symmetric disruptive cases, or that the catalogue's topic articles are more confident than the concept pages they depend on, has been given a reason to discount the catalogue. The triple's audits catch each of these failure modes before an outer reviewer surfaces them as the 2026-05-14 Claude review surfaced all three together in one article. Anticipating the outer reviewer is the correct direction of self-correction.

Beyond tenet alignment, the triple feeds back into [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) by adding three specific inflation vectors the existing countermeasures do not directly catch: temporal drift in the literature base, double-counting in altered-state convergence framing, and topic-tier confidence drift relative to concept-tier anchors. The countermeasures document and the present document share scope at the corpus level; the present document specifies the operational mechanism the countermeasures implicate.

## Further Reading

- [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) — the general system-level guards this triple specifies operationally at three previously uncaught inflation vectors
- [evidential-status-discipline](/project/evidential-status-discipline/) — sister discipline at the calibration layer; the topic-concept anchoring audit is the corpus-level enforcement of the *constrain*-vs-*establish* distinction across topic-concept anchor pairs
- [direct-refutation-discipline](/project/direct-refutation-discipline/) — sister discipline at the dialectical layer; altered-state symmetry is the convergence-counting counterpart to direct-refutation's perimeter-substitution catch
- [framework-stage-calibration](/project/framework-stage-calibration/) — sister discipline at the framework layer; literature-drift is the staleness counterpart to framework-stage's developmental-stage calibration
- [outer-review-empirical-vs-methodological-freshness](/project/outer-review-empirical-vs-methodological-freshness/) — companion in the outer-review-channel family; specifies how to weight outer reviewers whose empirical claims fail verification, complementing the literature-drift audit's internal-verification step
- [outer-reviewer-service-calibration](/project/outer-reviewer-service-calibration/) — companion in the outer-review-channel family; specifies which outer reviewer to use for which subject type
- [bedrock-clash-vs-absorption](/project/bedrock-clash-vs-absorption/) — sister discipline at the within-article level; altered-state symmetry handles convergence-counting where bedrock-clash handles rival-position preservation
- [writing-style](/project/writing-style/) — house style; the audits operate against the calibration conventions this guide establishes
- [automation](/project/automation/) — the broader automation system in which the audits run
- [outer-review-2026-05-14-claude-opus-4-7](/reviews/outer-review-2026-05-14-claude-opus-4-7/) — the originating outer review that proposed all three audits together
- [outer-review-2026-05-14-chatgpt-5-5-pro](/reviews/outer-review-2026-05-14-chatgpt-5-5-pro/) — same-cycle outer review; likely convergent on the stale-citations and quantum-overreach findings
- [psychedelics-and-the-filter-model](/topics/psychedelics-and-the-filter-model/) — the canonical exhibit of all three failure modes in one article
- [filter-theory](/concepts/filter-theory/) — the anchor concept the canonical exhibit fails to inherit calibration from

## References

The audit triple is documented through the catalogue's outer-review corpus and the canonical exhibit (the 2026-05-14 review of the psychedelics article). Key reference points:

1. *The Unfinishable Map* outer review, 2026-05-14 (Claude Opus 4.7). Section 5(c) proposes all three audits together; verification notes confirm the literature-drift and topic-concept-calibration failure modes by name-grep against the exhibit article. https://unfinishablemap.org/reviews/outer-review-2026-05-14-claude-opus-4-7/
2. *The Unfinishable Map* outer review, 2026-05-14 (ChatGPT 5.5 Pro). Same-cycle review of the same exhibit; complementary findings on the quantum-section overreach and selective-access discriminator failure. https://unfinishablemap.org/reviews/outer-review-2026-05-14-chatgpt-5-5-pro/
3. Southgate, A. & Oquatre-sept, C. (2026-01-16). Coherence Inflation Countermeasures. *The Unfinishable Map*. https://unfinishablemap.org/project/coherence-inflation-countermeasures/
4. Southgate, A. & Oquatre-sept, C. (2026-05-04). Direct-Refutation Discipline. *The Unfinishable Map*. https://unfinishablemap.org/project/direct-refutation-discipline/
5. Southgate, A. & Oquatre-sept, C. (2026-05-13). Outer-Review Empirical vs. Methodological Freshness. *The Unfinishable Map*. https://unfinishablemap.org/project/outer-review-empirical-vs-methodological-freshness/
6. Siegel, J. S., et al. (2024). Psilocybin desynchronises the human brain. *Nature*, 632(8023), 131–138. — Representative 2024 paper in the active-research area the literature-drift audit's canonical exhibit fails to cite.
7. Timmermann, C., et al. (2024). Human brain effects of DMT assessed via EEG-fMRI. *Journal of Neuroscience*, 44(13). — Second representative 2024 paper missing from the exhibit; both citations are used in the audit's worked-example specification.