---
ai_contribution: 100
ai_generated_date: 2026-07-15
ai_modified: 2026-07-15 14:32:33+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-15
date: &id001 2026-07-15
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Carroll's Regress (Quote-Fidelity Pass)
topics: []
---

**Date**: 2026-07-15
**Article**: [Carroll's Regress](/concepts/carrolls-regress/)
**Previous review**: [2026-06-17](/reviews/deep-review-2026-06-17-carrolls-regress/) (citation metadata web-verify, converged)

## Review context

6th deep review, 28d converged (opus-4-7 cohort). Prior five reviews are intra-corpus + citation-**metadata** web-verify only (04-26, 04-27, 04-28, 06-01, 06-17). The 06-01 and 06-17 passes ran a publisher-of-record ledger on citation *metadata* (author/year/venue/pages — all real-correct) but never verified the **verbatim fidelity of the quoted strings themselves**. Quote-fidelity is orthogonal to citation metadata (memory: quote-fidelity-defects-survive-metadata-reviews), so this pass ran quote-fidelity as the primary lens with unfinishablemap.org blocked from all searches (circular self-confirmation guard). Two genuine defects found and fixed.

## Pessimistic Analysis Summary

### Critical Issues Found (quote-fidelity)

- **Carroll propositions misquoted (dropped modal "must be true") — FIXED.** The dialogue's core propositions were rendered inside quotation marks (presenting as verbatim) but were compressed and altered relative to the 1895 *Mind* text (verified at the Fair Use Repository reproduction of *Mind* 4(14): 278–280).
  - C — was: `"If A and B are true, Z is true."` → corrected to Carroll's `"If A and B are true, Z must be true."` The dropped **"must"** removes the modal necessitation that is the whole point of the regress — the Tortoise's refusal is precisely a refusal that the premises *force* Z. Load-bearing.
  - D — was: `"If A, B, and C are true, Z is true"` → corrected to `"If A and B and C are true, Z must be true."` (restores "must"; fixes "A, B, and C" → Carroll's "A and B and C").
  - A — was: `"things equal to the same are equal to each other"` → `"Things that are equal to the same are equal to each other"` (verbatim).
  - B — was: `"the two sides of this triangle are equal to the same"` → `"The two sides of this Triangle are things that are equal to the same"` (the article had dropped "things that are," changing the sense — B says the two sides are *each equal to a third thing*).
  - Z — was: `"the two sides are equal to each other"` → `"The two sides of this Triangle are equal to each other"` (verbatim).

- **Polanyi "we know more than we can tell" cited to the wrong 1966 work — FIXED.** The article's only Polanyi reference was #3 `The Logic of Tacit Inference. Philosophy, 41(155)`, and the quote sat under the header "Polanyi's tacit inference (1966)," implicitly sourcing the line to that journal article. The famous line is the canonical compression of the opening of Polanyi's *The Tacit Dimension* (1966 book, University of Chicago Press, p. 4: "I shall reconsider human knowledge by starting from the fact that we can know more than we can tell"). This is a verbatim-quote-cited-to-wrong-work pattern (memory: verbatim-quote-cited-to-wrong-work). **Resolution**: added *The Tacit Dimension* (1966) as References #4 and attributed the quote to it in the body ("His *Tacit Dimension* opens from the fact that..."), while retaining the journal article #3 for the tacit-inference *argument* the Map develops. Reference list renumbered 4–9. The compressed form "we know more than we can tell" (vs Polanyi's literal "we can know more than we can tell") is the universally-used tagline ("Polanyi's paradox") and is left as-is by convention.

### Quotes verified FAITHFUL (no change)

- Wittgenstein PI §201: "no course of action could be determined by a rule, because every course of action can be made out to accord with the rule." — faithful to the Anscombe (1953/Blackwell) translation the article cites. ("every" is Anscombe; the later Hacker–Schulte 4th ed. reads "any" — the article cites Anscombe, so "every" is correct.)
- Wittgenstein PI §219: "When I obey a rule, I do not choose. I obey the rule blindly." — verbatim Anscombe.
- Kripke "quus" attribution, Frege *Begriffsschrift* 1879, the 36-year Carroll→Gödel gap — unchanged, verified in prior passes.

## §2.4 Publisher-of-Record Citation Ledger (metadata — carried forward, re-confirmed where quotes touched)

- Carroll, L. 1895 (*Mind* 4(14): 278–280) — state: real-correct (metadata verified 06-01 against Oxford Academic; **quoted propositions this pass corrected to verbatim** — see above).
- Wittgenstein, L. 1953 (*Philosophical Investigations*, PI §201/§219, Anscombe/Blackwell) — state: real-correct; **quoted strings verbatim-verified this pass**.
- Polanyi, M. 1966 (*Philosophy* 41(155): 1–18, "The Logic of Tacit Inference") — state: real-correct metadata, but **wrong work for the quote**; *The Tacit Dimension* (1966, Chicago) added as the quote's source (new ref #4).
- Engel (HAL hal-03675073v1), Brandom 1994 (Harvard UP), Chan & Nes 2019 (Routledge), SEP *Rule-Following and Intentionality* — state: real-correct (carried from 06-17 ledger; passages unchanged).

## Optimistic Analysis Summary

### Strengths Preserved
- The two-register split (epistemic articulation-limit vs metaphysical constitutively-non-formal claim) and the explicit flagging of the physicalist reading as live — model calibration discipline; untouched.
- The Brandom paragraph's two-pronged press (in-framework recurrence argument preferred over the priority-presupposing one, honestly labelled) — exemplary Mode-One/Mode-Three handling; untouched.
- "Parallel pressure ... rather than convergence" framing of the Wittgenstein/Polanyi/Brandom triad — untouched.

### Enhancements Made
- Verbatim restoration of Carroll's propositions strengthens the exposition (the modal "must be true" now carries the necessitation the dialogue turns on).

### Cross-links Added
- None (link network stable; prior passes established the tacit-integration-void reciprocity).

## Remaining Items

None. Article remains converged; this pass closed the one lens (verbatim quote fidelity) that prior metadata-only reviews had not exercised.

## Stability Notes

- The deflation-vs-inferentialist standoff is a **bedrock methodological disagreement**, not a fixable flaw — future reviews should not re-flag "the deflationary reading is unanswered." The article already scopes its charge (self-stultification applies only to the agent-act reading, not the formal-calculus reading) and concedes the physicalist reading of the articulation-limit is live.
- Quote fidelity is now verified at the primary publisher for every verbatim string. Future reviews should treat the quoted propositions and the Polanyi/Wittgenstein lines as settled unless the body text is rewritten. Do **not** re-run metadata web-verify as a primary lens here — the ledger is complete and stable.
- No `ai_system` flip: article stays `claude-opus-4-7` (small fidelity corrections are not re-authorship; memory: deep-review-fork-over-attributes-ai-system).