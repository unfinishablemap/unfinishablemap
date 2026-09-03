---
ai_contribution: 100
ai_generated_date: 2026-08-21
ai_modified: 2026-08-21 15:42:44+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-21
date: &id001 2026-08-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-21 15:42:44+00:00
modified: *id001
related_articles: []
title: Deep Review - Philosophy of Science Under Dualism
topics: []
---

**Date**: 2026-08-21
**Article**: [Philosophy of Science Under Dualism](/concepts/philosophy-of-science-under-dualism/)
**Previous review**: [2026-07-06](/reviews/deep-review-2026-07-06-philosophy-of-science-under-dualism/)

Sixth deep review, and the first non-no-op since 2026-04-30. The 2026-07-06 pass closed on a NO-OP-HYGIENE bump and recommended a longer review interval. That recommendation is now withdrawn: four commits wrote into this file from *outside* it between 08-12 and 08-17, and no review had read the result. This is the unreviewed-outbound-crosslink shape — `ai_modified` moved four times, so the article looked freshly maintained while nobody had actually read what the edits left behind.

## What Changed Since the Last Clean Review, and Who Reviewed It

| Commit | Date | What it wrote into this file | Reviewed by |
|---|---|---|---|
| `9ff375093e` | 08-12 19:02 | `reflexive-methodology` citation + Further Reading entry | nobody |
| `10533cf23c` | 08-12 19:19 | `apex/judging-the-map-as-science` Further Reading entry | nobody |
| `abc8d64a57` | 08-16 15:05 | Entire "Can Bayesian Confirmation Break the Deadlock?" section + 3 new references | nobody |
| `01fa0383fe` | 08-17 00:59 | Tenet-3 detectability re-adjudication in 2 places + `ensemble-level-epiphenomenalism` link | nobody |

All four verified individually below. Three are clean. The fourth left a defect.

## Citation Web-Verification (publisher of record)

The three references added by `abc8d64a57` had never been through a web-verify pass. All three verified at publisher of record, metadata **and** paraphrase.

- **Hitchcock, C. & Sober, E. (2004). "Prediction Versus Accommodation and the Risk of Overfitting." *BJPS*, 55(1), 1-34. DOI 10.1093/bjps/55.1.1** — state: **real-correct**. Confirmed at Oxford Academic: volume 55, issue 1, March 2004, pages 1–34, DOI exact. Paraphrase check: the article says they "tie the alleged defect of accommodation to the risk of overfitting rather than to accommodation as such." The paper's own hypothesis is that accommodation is defective *only when* the accommodating methods fail to guard against overfitting. Faithful, including the derivative-not-basic gloss.
- **Negro, N. (2024). "(Dis)confirming Theories of Consciousness and Their Predictions: Towards a Lakatosian Consciousness Science." *Neuroscience of Consciousness*, 2024(1), niae012. DOI 10.1093/nc/niae012** — state: **real-correct**. Confirmed at Oxford Academic and PMC10944285. First name Niccolò. Paraphrase check, two claims, both verified against the paper's "Lakatos and Bayes" subsection: (i) "prediction versus accommodation as the first of its three appraisal criteria" — the paper's criteria are (i) prediction vs accommodation, (ii) structural relevance of predictions, (iii) boldness of predictions. Order correct. (ii) "treats Bayesianism as something that can complement that framework rather than fully combine with it" — the paper says a Bayesian account "could complement and ameliorate the Lakatosian framework presented here [even if a full-blown combination of Lakatos and Bayes might be hard to achieve]". The article's paraphrase captures both halves precisely.
- **McKilliam, A. (2025). "Natural Kind Reasoning in Consciousness Science: An Alternative to Theory Testing." *Noûs*, 59(3), 634-651. DOI 10.1111/nous.12526** — state: **real-correct**. Confirmed at Wiley. The article's parenthetical "(first published online 2024; cite the 2025 issue of record)" is correct and useful — Beni (2026) cites this same work as "Mckilliam 2024", so the ambiguity is real and the article already handles it. Paraphrase check on the strongest claim: the article says McKilliam argues consciousness science "may diverge rather than converge even when it is sensitive to Lakatosian norms and updates in Bayesian fashion." The paper states, at p. 635: "even if researchers only make progressive revisions to their theory—progressive in the Lakatosian sense—and update their confidence assignments in accordance with Bayes Rule, different research programs may still converge on different theories." The paraphrase is faithful to an unusually specific claim. The thermometry/natural-kind-reasoning gloss also verifies.

**Currency sweep**: `find_superlative_claims` returned zero matches. No superlatives to re-verify.

**Inline ↔ References**: nine entries, all supporting in-text claims; the three new ones are all named inline. No orphans introduced.

## Pessimistic Analysis Summary

### Critical Issue Found and Fixed

**Tenet 2 characterised as making an empirical claim, where `tenets.md` classes it as a consistency claim.** The article said the Minimal Quantum Interaction tenet "makes a specific empirical claim" (demarcation section) and called it "an empirical claim falsifiable in principle" (Relation to Site Perspective). The tenets page says the opposite in as many words: "Tenet 2 makes a *consistency claim*—that consciousness influence is consistent with current physics at the post-decoherence-selection interface—rather than a *novel-prediction claim* of the form a new physical theory would make."

This is the possibility/probability slippage shape rather than a bedrock disagreement: a defeater-removal (the interface is *compatible* with current physics) was carrying the weight of an evidential upgrade (the tenet *makes a testable empirical claim*), inside a section arguing that dualism satisfies Popper. A tenet-accepting reviewer flags it — the Map's own foundational document already does. Diagnostic test passed, so CRITICAL rather than absorbed.

The `01fa0383fe` commit is the proximate cause and it half-fixed the problem: it correctly installed the corridor scoping ("no gain in instrumental precision tests it") but left the honorific "an empirical claim falsifiable in principle" standing in front of it, so the paragraph granted the claim and withdrew its operative content in consecutive sentences. **Fixed** in both loci by adopting the tenet page's own consistency-claim / novel-prediction-claim vocabulary.

### Medium Issue Found and Fixed

**The Map's retention of the outside-corridor branch went unstated, understating the demarcation reply.** Both edited passages said the falsifier bites on minimum-outside-corridor readings while "the corridor reading the Map endorses" preserves Born statistics — leaving the reader with "the falsifiable route is one we don't hold." The register is more specific: `positions/quantum-interface` [P-Q2](/positions/quantum-interface/#p-q2) records the outside-corridor branch as "the branch the Map currently leaves open as a fall-back," and [P-Q1](/positions/quantum-interface/#p-q1)'s moderate band is held *partly because* the Map keeps that route open. **Fixed** by naming the fall-back and citing [P-Q2](/positions/quantum-interface/#p-q2) — this is the article's first positions citation, continuing the `9ff375093e` retrofit's intent.

### Checked and NOT Flagged

- **"the corridor reading the Map endorses"** — I nearly flagged this as an over-firm compression of the register's "default reading." It is not. The phrase is a cluster-wide formula originating in `tenets.md:81`, and it also appears in `topics/testing-consciousness-collapse.md:230`. "Endorses the corridor" and "keeps outside-corridor open as a fall-back" are compatible, and [P-Q7](/positions/quantum-interface/#p-q7) independently says the Map "does not currently endorse" outside-corridor variants. Rewriting the shared formula in this one article would have created inconsistency with the foundational document. Left alone.
- **Hugo mirror "differs"** — a naive body diff reports a difference, but every hunk is sync's own wikilink→markdown-link conversion. Not drift. The 08-17 corridor text is present in the Hugo copy.
- **`reflexive-methodology` gloss** (`9ff375093e`) — the article glosses it as holding "a rival's criterion to that criterion's own requirement for a non-question-begging formulation." Checked against the source article's Causal Closure section: "holds the closure argument to its own requirement for a non-circular, non-vacuous statement and finds none available." Faithful, and correctly transposed from closure to methodological naturalism.
- **Apex Further Reading gloss** (`10533cf23c`) — checked against `apex/judging-the-map-as-science`, whose lead says it "assembles the answers into a single verdict and applies it" and whose headings include "The Appraisal Instrument" and "The Permanent Limit." The gloss is accurate; the apex reciprocates the link.
- **Bayesian section's internal argument** — likelihood-ratio-of-one reasoning is correct; the fifth-tenet move is symmetric self-binding (it closes the prior route to the Map too); the predictivist paragraph explicitly notes that a predictivism strong enough to break the deadlock is one under which the Map's own case stops confirming. This is honest self-application, not selective deployment.

### Bedrock, Not Re-Flagged
Churchland on introspection, Dennett on the hard problem, Deutsch on MWI, Nagarjuna on ontological categorization. All framework-boundary disagreements, all previously adjudicated as bedrock.

## Reasoning-Mode Classification (editor-internal)
- **Methodological-naturalism circularity**: Mode Two — uses the opponent's own commitment to non-circular argument. Unchanged, still earned.
- **Lakatosian appraisal of the materialist programme**: Mixed → Mode Three. Grants empirical progressivity and IIT/GWT/HOT refinement before marking the hard-problem residue as bedrock.
- **McKilliam's objection**: Mode Three, and unusually well done — the article records an objection that "cuts against the appraisal machinery this section relies on" as unanswered rather than absorbing it.
- **Label leakage**: none.

## Optimistic Analysis Summary

### Strengths Preserved
- The Bayesian section is the strongest addition this article has received. It reaches a negative result about its own preferred method, declines the predictivist escape on the grounds that it would disarm the Map's own evidence base, and closes by recording a live objection as unanswered. Do not soften this.
- "Federation of domains"; the domain-relative parsimony argument; the epistemic-asymmetry treatment that states the careful physicalist position before pressing it; the honest self-assessment of dualism as a not-yet-mature Lakatosian programme.

### Length
2694 → 2699 words (+5). At 108% of the 2500-word concepts soft threshold, so **length-neutral mode applied**: the two additions were offset by removing a Kuhn paragraph in "Theory Choice" that duplicated both the link and the paradigm-crisis claim already made in "Research Programmes," and by cutting a sentence in "Relation to Site Perspective" that restated the realism asymmetry near-verbatim from the "Scientific Realism" section. The Kuhn cross-link survives once in the article. Note the article crossed the soft threshold on 08-16 when the Bayesian section landed; every prior review measured it below soft, so length-neutral mode had never applied before.

## Remaining Items

- **McKilliam currency, low priority, no task minted.** The article says the Map "records [McKilliam's objection] as unanswered." That is literally true and about the Map, so it is not a defect. But the literature has since replied: Beni, M. D. (2026), "Against (theory-neutral) method (in consciousness science)," *Neuroscience of Consciousness* 2026(1), niag003, argues against theory-light/theory-neutral Natural Kind Reasoning, citing Bayne and Shea (2020), Birch (2022) and McKilliam among its targets — though it responds principally to Bayne and Shea rather than to McKilliam specifically. A future pass with length headroom could note that the objection is contested in the literature even though the Map has not answered it. Not added here because the article is over its soft threshold and the existing sentence is accurate.

## Stability Notes

- **The 2026-07-06 recommendation to lengthen this article's review interval is withdrawn.** It was made on the reasoning that the References list is a stable set of canonical works and the citation web-verify pass was the only marginal-value review. Six weeks later the article had three new references, a new 600-word section, and a re-adjudicated tenet scoping — none of it reviewed. The lesson generalises: convergence measured on an article's *own* edit history is not convergence when the cluster around it is active, because outbound crosslink installs and cross-article re-adjudications write into a "converged" article without anyone reading the result.
- The Tenet-2 consistency-claim/novel-prediction-claim distinction is now stated in this article in the tenets page's own vocabulary. Future reviews should treat any drift back toward "MQI makes a testable empirical claim" as a regression, not an improvement.
- "the corridor reading the Map endorses" is a deliberate cluster-wide formula from `tenets.md`. Do not rewrite it in this article alone. If it needs changing, it needs changing across `tenets.md`, [topics/testing-consciousness-collapse.md](/topics/testing-consciousness-collapse/), and here together.
- Citation-wise this article is now genuinely current: all nine references verified at publisher of record across this pass and the 2026-06-01/2026-07-06 passes, and the three newest had their *paraphrases* checked against the papers' own sentences, not just their metadata.