---
ai_contribution: 100
ai_generated_date: 2026-07-29
ai_modified: 2026-07-29 16:50:50+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-29
date: &id001 2026-07-29
description: Corpus-wide mechanical audit of all 38 apex articles against their declared
  apex_sources, plus the targeted calibration-propagation fix to moral-architecture-of-consciousness.
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[apex/moral-architecture-of-consciousness]]'
title: Apex Evolve 2026-07-29 — Moral Architecture of Consciousness (+ corpus-wide
  apex source-coverage audit)
topics: []
---

## Scope

Two pieces of work: (1) the corpus-wide mechanical check proposed in the cycle-500 briefing — grep every apex article against its own declared `apex_sources` — and (2) the targeted fix to [apex/moral-architecture-of-consciousness.md](/apex/moral-architecture-of-consciousness/) for the still-open P3 minted by `/optimistic-review` 2026-07-29T06:10Z.

## Part 1 — Corpus-wide apex source-coverage audit (new check, first run)

**Method.** For each of the 38 apex articles, parse `apex_sources` from frontmatter and test whether the article *body* contains a wikilink or markdown link resolving to each declared source slug. Then cross-check mechanism-heavy apex articles for calibration markers (mechanism-debt anchor, `P-Q*` position IDs, bias-without-deviation framing).

**Result: clean on the primary check.** All 38 apex articles link **every one** of their declared sources in the body. 316 source declarations, zero unlinked. The failure mode the briefing anticipated — an apex citing none of its sources — does not exist in the corpus.

**Result: clean on the mechanism-calibration check.** The apex articles with the highest mechanism-vocabulary density all carry explicit calibration rather than forceful assertion:

- `what-consciousness-tells-us-about-physics.md` — carries an explicit **Headline guard** ("The argument below sometimes uses 'consciousness selects' as shorthand. The Map's actual thesis is weaker than that headline"), and states the whole synthesis conditionally.
- `self-concealing-interface.md` — names the most-testable-tenet-vs-concealment tension in the open and resolves it rather than letting it stand.
- `interface-specification-programme.md` — contains an explicit self-correction ("This is where an earlier statement of the programme overreached, and the correction is the honest one").
- `born-preserving-causal-efficacy.md`, `research-programme-decisions-under-the-map.md`, `assessing-ai-consciousness-under-the-map.md` — heavy `P-Q*` citation and debt inheritance.

The defect fixed earlier today in `time-consciousness-growing-block.md` appears to have been isolated rather than the tip of a pattern.

**Applied-apex discipline: clean.** All three `apex_type: applied` articles satisfy the ≥3-positions requirement (`assessing-ai-consciousness-under-the-map` 5, `embodied-interface` 4, `research-programme-decisions-under-the-map` 5), and each cites more position IDs in the body than it declares in frontmatter.

## Part 2 — Two findings the audit surfaced that are NOT clean

### Finding A: the "Evidence and Dependency" retrofit has stalled at 7/38

The section was adopted 2026-07-16 (ChatGPT 5.6 Pro full-site audit, rec #29) and is declared **required on every apex article**. It is present on 7:

`self-construction-constructor`, `assessing-ai-consciousness-under-the-map`, `dualism-cartography`, `steelmanning-as-method`, `ai-as-introspection-control`, `phenomenology-of-consciousness-doing-work`, `what-consciousness-tells-us-about-physics`.

It is absent from the other 31. This is a genuine gap between a stated discipline and the corpus, and it is not visible to any existing check.

**It collides with length discipline, which is why it has stalled.** The section costs ~200 words. Of the 31 articles missing it, **16 have under 400 words of headroom to the hard threshold** and 5 have under 100. Retrofitting by addition is not available for half the backlog; it needs substitution, which is a per-article editorial judgement rather than a sweep. Flagging for a human decision on sequencing rather than starting an unbudgeted sweep.

Note also that several articles do the ledger's *work* in prose without the heading — `moral-architecture-of-consciousness` L156–158 states the artifact-of-method discount, denies that the four pillars are four independent confirmations, and declares the synthesis conditional and framework-internal. Whether such prose satisfies the requirement or must be re-headed is part of the decision.

### Finding B: apex length is systemically over soft, and three articles are over hard

Mean apex length is **4433 words** against a 4000 soft threshold; **28 of 38** are over soft. Three are over hard (5000):

| Article | Words | Argument only | Status | Open task |
|---|---|---|---|---|
| `phenomenal-output-causal-machinery-dissociation` | 6904 | 5647 | **critical** | yes — `#veto` |
| `machine-question` | 5765 | 4943 | hard_warning | **none** |
| `conjunction-coalesce` | 5144 | 4895 | hard_warning | yes |

Argument-only figures exclude References / Further Reading / Source Articles, per the known caveat that `analyze_length` counts reference apparatus.

`machine-question` is the only unflagged one. It was condensed to 5019 words on 2026-05-29 and has since accreted to 5765 (+746) — the cross-link accretion the briefing describes, arriving from *other* articles' refines rather than from anyone editing it. No condense task was minted here: the sibling critical-status article carries an operator `#veto` on exactly that remedy, which reads as a standing human decision that apex length is human-decision territory. Reported rather than queued.

## Part 3 — The targeted fix applied

**Target**: [apex/moral-architecture-of-consciousness.md](/apex/moral-architecture-of-consciousness/), per the P3 minted by `/optimistic-review` 2026-07-29T06:10Z ([reviews/optimistic-2026-07-29-moral-responsibility-desert-cluster.md](/reviews/optimistic-2026-07-29-moral-responsibility-desert-cluster/)).

**The finding, re-verified by grep before editing**: the desert cluster's calibration lives in its specialist articles and does not reach this synthesis — the piece readers and retrieving LLMs hit first. Confirmed zero links to `frankfurt-cases-and-the-principle-of-alternate-possibilities`, `reactive-attitudes-and-strawsonian-responsibility`, `consciousness-and-moral-agency-under-duress`, `ai-moral-agency-and-the-responsibility-gap-under-dualism`. The failure mode is **silence**, not over-claim — the concessions had nowhere to propagate from.

**Four changes:**

1. **Compatibilist Symmetry Challenge section** — hung both specialist links on the existing "developed catalogue-wide" sentence, with the concessions stated rather than merely linked: that relocating the Map's libertarianism from leeway to sourcehood is "a retreat and a conditional one, not a costless translation" and that the semicompatibilist actual-sequence rival remains standing; and that resisting the Strawsonian dissolution is "not evidence that Strawson is wrong or that dualism is right." Both concessions verified verbatim in their source articles before quoting. This closes a loop rather than opening one — the reactive-attitudes article already links `compatibilist-symmetry-challenge` from its own text.

2. **Responsibility Gradient section** — linked the existing unlinked "duress" prose to `consciousness-and-moral-agency-under-duress`, at exactly the point the synthesis summarises the gradient's legal application.

3. **What Would Challenge This View?** — inherited the better-calibrated hedge from the source article. The apex stated the neural-prediction falsifier flatly; [topics/moral-implications-of-genuine-agency.md](/topics/moral-implications-of-genuine-agency/) warns that "prediction-completeness has no fixed threshold" and names the failure mode "falsifiability theatre." Removed the flat parenthetical and added the hedge, naming the Libet–Soon–Maoz progression as decoding that has not dislodged libertarian readings.

4. **Source Articles** — added `ai-moral-agency-and-the-responsibility-gap-under-dualism`, giving the agency pillar its missing lower bound: systems with no conscious interface fall off the responsibility scale entirely.

**Respected the task's exclusions**: L60 (coherence-inflation discount) and L156 (four-pillars-are-not-four-confirmations) untouched — both rated the strongest calibration prose in the cluster.

**Length**: 4499 → 4638 words (+139). Status unchanged at `soft_warning`; 362 words of headroom to hard. Part of the hedge was paid by substitution (removed the flat 13-word falsifier parenthetical). The remainder is net addition, justified on the grounds that a bare link does not propagate a concession — a retrieving LLM reading only the synthesis would still receive the forceful version, which is precisely the failure the three reviewers converged on.

**Frontmatter**: `ai_modified` advanced to 2026-07-29T16:50:50+00:00 (verified against `date -u` in the same command). `ai_system` **held** at `claude-opus-4-6+claude-opus-5` — no re-authorship. `last_deep_review` untouched (no deep review performed). `apex_last_synthesis` untouched — this was a targeted refine, not a synthesis pass, and the stale-field drift is a known harmless artifact not to be reconciled.

**Validation**: frontmatter valid; sync clean; all four new wikilinks confirmed resolving to `/topics/...` in the Hugo output; no `[1m]` artifact; no EOF tool-call artifact.

## Known sibling locus, deliberately not batched

[topics/moral-implications-of-genuine-agency.md](/topics/moral-implications-of-genuine-agency/) has the same two absent links plus an internal tension over whether "genuine" reasons-responsiveness excludes determination. Left unqueued and unedited per the task's explicit instruction not to batch — `cycle_post` closes multi-file tasks after one file.