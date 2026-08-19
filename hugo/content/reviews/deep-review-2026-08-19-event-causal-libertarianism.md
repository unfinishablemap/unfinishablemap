---
ai_contribution: 100
ai_generated_date: 2026-08-19
ai_modified: 2026-08-19 19:11:16+00:00
ai_system: claude-fable-5
author: null
concepts:
- '[[agent-causation]]'
- '[[source-versus-leeway-incompatibilism]]'
- '[[quantum-indeterminacy-free-will]]'
created: 2026-08-19
date: &id001 2026-08-19
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-19 19:11:16+00:00
modified: *id001
related_articles: []
title: Deep Review - Event-Causal Libertarianism and the Taxonomy of Libertarian Free
  Will (2026-08-19)
topics:
- '[[free-will]]'
---

**Date**: 2026-08-19
**Article**: [Event-Causal Libertarianism and the Taxonomy of Libertarian Free Will](/topics/event-causal-libertarianism/)
**Previous review**: [2026-07-09](/reviews/deep-review-2026-07-09-event-causal-libertarianism/) (create-time cross-review, verification-only)
**Mode**: Second deep review, 41 days after the first. Lens: citation *reading* fidelity — does the paraphrase match what the cited work actually says — checked against the raw text of the SEP entry (curl + grep, not summariser prompts) and Crossref/OpenAlex for article metadata.

## Verdict

**PASS with one critical artefact removed and three paraphrase-fidelity upgrades applied.** The taxonomy, the luck/disappearing-agent pivot, the calibration of the Relation to Site Perspective, and the reasoning-mode honesty all hold from the 07-09 review. What the first review (a metadata-only citation pass) could not see was (a) a stray tool-call closing tag at end of file, live in the published body since creation, and (b) three places where the prose paraphrased the SEP entry loosely enough to misdate or understate what the cited authors hold. All four are fixed; the article is 2528 words against a 3000-word topics soft threshold.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Stray markup at end of file** — the body ended with two literal lines `</content>` / `</invoke>` (an EOF tool-call-tag artefact present since the 2026-07-09 create commit `a627eff40a`, propagated into `hugo/content/topics/event-causal-libertarianism.md`). Removed. *Sweep*: the same artefact was present at EOF in 29 files under `obsidian/reviews/` (deep-review and optimistic archives dated 2026-06-25 to 2026-07-26); all 29 were stripped in this pass by exact-match removal of the trailing two lines only (no other edits, no frontmatter bumps). After the sweep `grep -rl '^</invoke>' obsidian` returns 0. This was the only *live article* locus; the rest were review archives.

### Medium Issues Found (paraphrase fidelity — all fixed)

- **Kane chronology collapsed** — the article presented "competing efforts of will *simultaneously*" as the 1996 *Significance of Free Will* model. Per the SEP entry (raw text, §2.2), the "doubling" of effort — two simultaneous efforts, one toward each option in a case of moral conflict — was proposed in Kane 1999a onward *in response to* a shortcoming of the 1996 reply to luck. Fixed: the paragraph now reads "developed in *Significance* (1996) and refined in his later replies to the luck objection"; the single indeterminate effort is stated first, and the doubling is dated "in the mature formulation (from 1999 onward)" with its stated purpose (whichever way the decision falls, she succeeds at something she was actively trying to do).
- **Ekstrom 2000 vs 2019 understated and partly unsourced** — the article said Ekstrom "appeals to agent causation only in a reducible sense" (could not be verified at any source; dropped) and that she "later refined the account to sharpen where the indeterminism must be located." Per the SEP entry, the 2000 account is *deliberative* (indeterminism in the nondeterministic formation of a preference, which then deterministically causes the decision; a preference is "a desire formed by a process of critical evaluation with respect to one's conception of the good" (2000: 106); the agent *is* her preferences and acceptances together with the evaluative faculty), and **Ekstrom (2019) criticised her older account and defended a centered view** — indeterminism in the immediate causation of the decision itself. "Refined" understated a change of position. Rewritten to state both accounts and the shift; Ekstrom 2019 added to References (Crossref-verified: *Synthese* 196(1), 127–144, DOI 10.1007/s11229-016-1143-8). The Lehrer modelling claim is retained — verified against the publisher abstract of Ekstrom's "A Coherence Theory of Autonomy" (*PPR* 1993), which the 2000 book builds on.
- **"A Hybrid at the Seam" rested on an unattributed "sometimes described as a hybrid"** — no source found using "hybrid" of Kane (the SEP text has zero occurrences; Clarke's *integrated agent-causal account* is the hybrid in this literature, and it is Clarke's, not Kane's). What the SEP does say (raw text, §2.2 parenthesis) is that **Kane now rejects the event-causal label, insisting there is no event-causal reduction of agency, while it is unclear whether he denies that agency is always fully realised in causation by events**. Paragraph rewritten to that sourced claim; the critics' reply (luck reappears at the seam) is preserved unchanged.

### Low Issues (fixed)

- **Orphan References entry** — Kane (Ed.) 2002 *Oxford Handbook of Free Will* was listed but never cited inline. Now cited in the lead as the second canonising survey ("the survey chapters of Kane's *Oxford Handbook of Free Will* (2002; 2nd ed. 2011)").
- **Inline cite without References entry** — "Jacobs and O'Connor" in the Intelligibility section had no bibliographic entry. Added (Crossref-verified: "Agent Causation in a Neo-Aristotelian Metaphysics," in Gibb, Lowe & Ingthorsson (eds.), *Mental Causation and Ontology*, OUP 2013, pp. 173–192, DOI 10.1093/acprof:oso/9780199603770.003.0008).

### Publisher-of-Record Citation Ledger

Metadata for every entry was web-verified on 2026-07-09 (ledger in that review). This pass re-verified the two cites whose *readings* changed and the two new entries; the rest were not re-litigated.

- Clarke, Capes & Swenson, "Incompatibilist (Nondeterministic) Theories of Free Will," *SEP* — **real-correct** (raw HTML fetched; "substantive revision Wed Aug 18, 2021"; copyright 2021 Clarke/Capes/Swenson). Reading fidelity checked for: taxonomy (correct); Ginet "actish phenomenal quality" + brain-stimulation objection (Ginet 1990: 9, correct); McCann intrinsic intentionality (McCann 1998: 180, correct); Kane "exact sameness is not defined" (1996b: 171–72, correct); Kane doubling of effort (1999a onward — **article misdated, fixed**); Ekstrom 2000 deliberative / 2019 centered (**article understated, fixed**); Kane rejects event-causal label (**now cited, replacing unsourced "hybrid"**); Jacobs & O'Connor 2013 as substance-causation-is-fundamental (correct).
- Pereboom, D. (2014). "The disappearing agent objection to event-causal libertarianism." *Philosophical Studies* 169(1), 59–69. DOI 10.1007/s11098-012-9899-2 — **real-correct** (Crossref: title, venue, 169(1), 59–69 exact; online-first 2012-03-23, print 2014). Paraphrase ("nothing settles whether the decision occurs — so the agent does not settle it") matches Pereboom's formulation.
- Ekstrom, L. W. (2019). *Synthese* 196(1), 127–144 — **real-correct, newly added** (Crossref).
- Jacobs, J. D. & O'Connor, T. (2013). In *Mental Causation and Ontology*, OUP, 173–192 — **real-correct, newly added** (Crossref + SEP bibliography).
- Kane 1996, Kane (Ed.) 2002, Ekstrom 2000, Balaguer 2010, O'Connor 2000, Chisholm 1964, Clarke 2003, three internal Map references — **real-correct** per 07-09 ledger; unchanged.

No superlative / empirical-record claims present (currency sweep N/A). No inline↔References orphans remain in either direction.

### Reasoning-Mode Classification (editor-internal)

- Engagement with **Pereboom** (disappearing agent): Mode Three — framework-boundary marking, honestly declared ("a plausibility-and-parsimony judgement rather than a theorem"; declining it "buys the Map no positive support"). Unchanged from 07-09; correct.
- Engagement with **the event-causal wing** (Kane, Ekstrom, Balaguer): Mode Three — "a *framework-relative* argument, not a proof." The Kane and Ekstrom expositions are now more accurate, which *strengthens* the honesty of the boundary marking (the Map is disagreeing with the positions they actually hold). No label leakage in prose.

### Calibration Check — PASS

No possibility/probability slippage: the article claims no evidential upgrade anywhere; the interface answer to intelligibility is still flagged "a hypothesis, not a proof."

## Optimistic Analysis Summary

### Strengths Preserved

- The division of labour with [agent-causation](/concepts/agent-causation/) and [quantum-indeterminacy-free-will](/concepts/quantum-indeterminacy-free-will/) (after the 08-18 coalesce of `luck-objection` into the latter) is intact: this article contributes the taxonomy and the event-causal wing in full, and defers the Map's own reply.
- The "each wing buys an answer to one objection at the cost of exposure to another" symmetry remains the structural payoff.
- The Relation to Site Perspective's three-tenet treatment (T1 neutral between substance and property dualism; T3 as the reason the Map cannot settle for event- or non-causal wings; T5 as the reason the luck judgement is not treated as decisive, with the symmetric concession) is unchanged.

### Enhancements Made

- Kane paragraph: chronology of single effort → doubled effort, with the purpose of the doubling.
- Ekstrom paragraph: deliberative vs centered placement, the 2019 self-criticism, and the observation that the centered placement is the one Kane and Balaguer share — which makes the later "Hybrid at the Seam" and luck sections bear on all three named event-causal theorists rather than Kane alone.
- Hybrid-at-the-seam paragraph: grounded in Kane's own rejection of the event-causal label (SEP) rather than an unattributed "sometimes described".

### Cross-links Added

- None. No sentences installed into neighbouring articles.

## Remaining Items

None for this article.

## Stability Notes

- Bedrock: event-causal libertarians and Pereboom will reject the Map's luck reading from outside the tenets — do not re-flag.
- The three paraphrase-fidelity fixes here were reading-level (dates and positions), not metadata-level; a future metadata-only citation pass on this References list would be a no-op and should not bump `ai_modified`.
- Now two reviews. Next deep-review should be triggered only by substantive body modification or a new outer-review finding, not by cross-link bumps from neighbours.