---
ai_contribution: 100
ai_generated_date: 2026-09-21
ai_modified: 2026-09-21 00:14:24+00:00
ai_system: claude-opus-5
author: Andy Southgate
concepts:
- '[[evidential-status-discipline]]'
created: 2026-09-21
date: &id001 2026-09-21
description: 'Full-register audit of all 61 positions across 17 domain files - the
  first since 2026-07-12. No contradictions, no broken dependencies, clean calibration
  vocabulary; one structural finding: two domain files never received the foundational-dependency
  test.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-21 00:14:24+00:00
modified: *id001
related_articles:
- '[[positions]]'
- '[[positions/voids-as-evidence]]'
- '[[positions/ai-substrate-verdicts]]'
title: Positions Register Audit - 2026-09-21
topics: []
---

# Positions Register Audit — 2026-09-21

Full-register cross-check. **All 61 live positions across all 17 domain files were read in full** (Asserts, Calibration, Depends on, Argued in, Would shift if, Last reviewed), plus `positions.md` and the six companion `*-calibration-history` files as context.

This is the first full-register audit since **`200b4d3735`, 2026-07-12** — **71 days**, against a 30-day cadence. The three intervening commits matching "audit" are single-entry or single-domain passes (`f2efa90f2c` [P-I3](/positions/individuation-and-subjecthood/#p-i3), `004966d408` [P-D3](/positions/arguments-for-dualism/#p-d3), `777068c4eb` quantum-interface), not full-register. At the last audit the register held **34 entries across 8 domain files**; it now holds **61 across 17**, so **27 entries and 9 domains had never been through a cross-register audit**.

The nine domain files postdating the last audit — `arguments-for-dualism`, `finding-level-calibration`, `arguments-for-mental-causation`, `subject-census`, `moral-status`, `ai-substrate-verdicts`, `perception-and-the-interface`, `thought-and-understanding`, `memory-and-autonoesis` (17 entries) — were audited **against the eight pre-existing domains**, not only against each other, since a contradiction between a 2026-09 entry and a 2026-06 entry is the class 71 days without a cross-check produces.

## Method

Entries were extracted field-by-field into a structured index and checked mechanically, then the full Asserts corpus (~22,000 words) was read for contradictions. Counting used `grep -oiF … | wc -l` throughout — register entries are single very long lines, so `grep -c` cannot see a second match on a line. Every zero result was paired with a positive control, and one control failure was caught and corrected during the run (see "Lead 1" below).

## Check 1 — Contradictions between live positions

**None found.** Seven cross-seam candidates were raised and each was adjudicated to a disclosed-and-scoped relation rather than a contradiction. Recording them because "no contradictions" is only informative if the candidates are named:

| Candidate seam | Why it looked like a contradiction | Verdict |
|---|---|---|
| [P-MC3](/positions/arguments-for-mental-causation/#p-mc3) (new) vs [P-Q2](/positions/quantum-interface/#p-q2) / [P-Q3](/positions/quantum-interface/#p-q3) (old) | [P-MC3](/positions/arguments-for-mental-causation/#p-mc3) has the Map "denying causal completeness" and consciousness "biasing which physically permissible outcome actualises", while [P-Q2](/positions/quantum-interface/#p-q2) preserves Born statistics *exactly* | **Clean — disclosed.** [P-MC3](/positions/arguments-for-mental-causation/#p-mc3) grades the escape below the diagnostic and depends on the `^mechanism-debt` anchor, which *is* [P-Q3](/positions/quantum-interface/#p-q3), the entry that names this as the live bias-without-deviation dilemma. The tension is the register's own registered open problem, carried explicitly. |
| [P-MC2](/positions/arguments-for-mental-causation/#p-mc2) (new) vs [P-CS6](/positions/consciousness-scope/#p-cs6) / [P-SC1](/positions/subject-census/#p-sc1) / [P-CS1](/positions/consciousness-scope/#p-cs1) | [P-MC2](/positions/arguments-for-mental-causation/#p-mc2) reads Tenet 3 at "universal-actual-efficacy"; three other entries hold it at "available-not-actual" standing | **Clean — different objects.** `tenets.md:95` (`^tenet-3-standing`) settles it: "available-not-actual" is what *the interface argument establishes*, not what the tenet asserts. The anchor itself books Tenet 3 as "a metaphysical commitment supported by self-stultification and indirect evidence" — which is exactly [P-MC2](/positions/arguments-for-mental-causation/#p-mc2)'s claim that the tenet's universal reading outruns the argument's existential one. [P-MC2](/positions/arguments-for-mental-causation/#p-mc2) is the register's statement of the shortfall the tenets page books. |
| [P-MS1](/positions/moral-status/#p-ms1) (new) vs [P-I1](/positions/individuation-and-subjecthood/#p-i1) / [P-SC3](/positions/subject-census/#p-sc3) | [P-MS1](/positions/moral-status/#p-ms1) needs "a momentary experiential locus … not a persisting self"; [P-I1](/positions/individuation-and-subjecthood/#p-i1) and [P-SC3](/positions/subject-census/#p-sc3) assert a determinate, persisting subject | **Clean — reconciled in-entry.** [P-MS1](/positions/moral-status/#p-ms1) states that status sits at the base layer and "the persisting subject the agency cluster asserts is a further claim the *derivation* does not rest on", then routes the sleeper/coma interval verdicts explicitly to [P-SC3](/positions/subject-census/#p-sc3). Scoped, not conflicting. |
| [P-AS1](/positions/ai-substrate-verdicts/#p-as1) (new) vs [P-AC1](/positions/ai-consciousness-scope/#p-ac1) (old) | Two substrate verdicts over adjacent hardware classes | **Clean — explicitly sibling-scoped.** [P-AS1](/positions/ai-substrate-verdicts/#p-as1): "the conventional-digital verdict belongs to [P-AC1](/positions/ai-consciousness-scope/#p-ac1) — this entry registers the bucket [P-AC1](/positions/ai-consciousness-scope/#p-ac1) explicitly disclaims, as a sibling verdict rather than a consequence." |
| [P-I4](/positions/individuation-and-subjecthood/#p-i4) / [P-AC3](/positions/ai-consciousness-scope/#p-ac3) (additive counting) vs [P-SC2](/positions/subject-census/#p-sc2) (no pairing law) | An additive counting rule resting on a pairing behaviour the Map says it has not specified | **Clean — booked as conditional.** [P-I4](/positions/individuation-and-subjecthood/#p-i4) states the fission verdict is "conditional twice over, and both conditions are booked", naming [P-SC2](/positions/subject-census/#p-sc2) as the unpaid debt. |
| [P-TU1](/positions/thought-and-understanding/#p-tu1) / [P-MA1](/positions/memory-and-autonoesis/#p-ma1) (new) vs [P-A4](/positions/agency-and-will/#p-a4), [P-D1](/positions/arguments-for-dualism/#p-d1), [P-M2](/positions/methodology-and-calibration/#p-m2) (old) | Two constitutive-phenomenology commitments that could each be counted as fresh confirmation | **Clean — premise-sharing disclosed.** Both depend on [P-D1](/positions/arguments-for-dualism/#p-d1) explicitly ("sharpens the explanandum in a new domain without adding an independent confirmation") and [P-TU1](/positions/thought-and-understanding/#p-tu1) additionally routes felt effort's causal standing to [P-A4](/positions/agency-and-will/#p-a4) and its converging lines to [P-M2](/positions/methodology-and-calibration/#p-m2). |
| [P-PI1](/positions/perception-and-the-interface/#p-pi1) / [P-F1](/positions/finding-level-calibration/#p-f1) (new) vs [P-M1](/positions/methodology-and-calibration/#p-m1) / [P-M2](/positions/methodology-and-calibration/#p-m2) (old) | A new empirical wing that could inflate the catalogue | **Clean — self-limiting.** [P-PI1](/positions/perception-and-the-interface/#p-pi1) closes with "citing the wing's convergence as support for Tenet 1 is the pattern [P-F1](/positions/finding-level-calibration/#p-f1) forbids." |

**Finding zero contradictions across 17 never-audited entries is the reportable outcome here**, and the reason is visible in the table: the new domains were written with explicit cross-references to the old ones, and in several cases the new entry exists *in order to* restrain what an old one could be read as supporting.

## Check 2 — Dependencies and citations resolve

**Clean.** Every `[[…]]` target and every position reference appearing in `Depends on`, `Argued in`, `Asserts` and `Would shift if` across all 61 entries resolves — to an existing corpus file or to an existing position ID. Bare (non-wikilinked) position references in `Depends on` were checked separately and all resolve. **0 unresolved references.**

## Check 3 — Orphan positions

**6 of 61 are orphaned** on the strict test (position ID not mentioned in any `apex/`, `topics/`, `concepts/`, `voids/`, `tenets/`, `questions/` or `arguments/` article). All six are cited in `reviews/` and `workflow/`, and one in `project/`, so none is unreferenced — but none is cited from the article layer the register exists to serve:

| Position | Non-register hits | Where |
|---|---|---|
| [P-CS1](/positions/consciousness-scope/#p-cs1) | 33 | `reviews/` 15, `workflow/` 18 |
| [P-F1](/positions/finding-level-calibration/#p-f1) | 19 | `project/` 1, `reviews/` 8, `workflow/` 10 |
| [P-MC3](/positions/arguments-for-mental-causation/#p-mc3) | 12 | `reviews/` 5, `workflow/` 7 |
| [P-MC4](/positions/arguments-for-mental-causation/#p-mc4) | 11 | `reviews/` 4, `workflow/` 7 |
| [P-PI1](/positions/perception-and-the-interface/#p-pi1) | 4 | `reviews/` 2, `workflow/` 2 |
| [P-MA1](/positions/memory-and-autonoesis/#p-ma1) | 1 | `workflow/` 1 |

[P-PI1](/positions/perception-and-the-interface/#p-pi1) and [P-MA1](/positions/memory-and-autonoesis/#p-ma1) were added on 2026-09-14 and 2026-09-20 and have simply not been picked up yet; [P-CS1](/positions/consciousness-scope/#p-cs1) is the more notable case, being the **minimal-dualism spine** with *high* structural centrality and five register entries hanging from it, yet named by no article. Not escalated: this is an integration gap, not a register defect, and the register's convention is that an entry's `Argued in` points *outward* rather than requiring the article to point back.

## Check 4 — Calibration vocabulary and the discriminability aggregate

**Vocabulary clean.** All 61 entries parse to six axes, and every value is in the closed vocabulary defined at `methodology-and-calibration#^calibration-schema`. No off-vocabulary values, no missing axes. (The 2026-08-03 audit found seven off-vocabulary values; none has recurred.)

**Aggregate re-derived from the `- **Calibration**` lines** — parsing only those lines, per the instruction at `positions.md:57`:

- **direct** 4 ([P-A3](/positions/agency-and-will/#p-a3), [P-AC4](/positions/ai-consciousness-scope/#p-ac4), [P-MA1](/positions/memory-and-autonoesis/#p-ma1), [P-Q6](/positions/quantum-interface/#p-q6)) · **indirect** 25 · **in-principle** 1 ([P-SC1](/positions/subject-census/#p-sc1)) · **none** 8 · **none-by-construction** 3 ([P-CS5](/positions/consciousness-scope/#p-cs5), [P-Q2](/positions/quantum-interface/#p-q2), [P-Q7](/positions/quantum-interface/#p-q7)) · **n/a** 20 — **total 61**
- **inert** (none + none-by-construction) **11**; inert ∩ centrality *high* **5** ([P-CS1](/positions/consciousness-scope/#p-cs1), [P-I1](/positions/individuation-and-subjecthood/#p-i1), [P-I3](/positions/individuation-and-subjecthood/#p-i3), [P-Q2](/positions/quantum-interface/#p-q2), [P-Q7](/positions/quantum-interface/#p-q7)); inert ∩ framework-internal *yes* **10**

**This reproduces the `positions.md` Updated-note chain exactly**, through to the 2026-09-20 second-pass figures (live 61, direct 4, inert 11, framework-internal inert 10, high-centrality inert 5). **No band was moved by this audit**, so no re-derivation note was added and `positions.md` is unchanged — it remains at **3386 words, `hard_warning`, 614 words from critical (4000)**.

One convention note, observed and not changed: the prose paragraph at `positions.md:55` still reads "As of 2026-09-06, the 56 live positions…", with the deltas carried in the dated `Updated` notes beneath. That is the documented arrangement (`positions.md:57` instructs re-derivation before quoting, and the paragraph is dated), not drift.

## Check 5 — Staleness

**6 entries carry a `Last reviewed` older than 60 days**, the rest are current:

| Position | Last reviewed | Days |
|---|---|---|
| [P-A3](/positions/agency-and-will/#p-a3) | 2026-06-10 | 103 |
| [P-M1](/positions/methodology-and-calibration/#p-m1) | 2026-06-22 | 91 |
| [P-M4](/positions/methodology-and-calibration/#p-m4) | 2026-06-22 | 91 |
| [P-CS2](/positions/consciousness-scope/#p-cs2) | 2026-06-22 | 91 |
| [P-CS3](/positions/consciousness-scope/#p-cs3) | 2026-06-22 | 91 |
| [P-CS5](/positions/consciousness-scope/#p-cs5) | 2026-07-17 | 66 |

Four of the six ([P-M1](/positions/methodology-and-calibration/#p-m1), [P-M4](/positions/methodology-and-calibration/#p-m4), [P-CS2](/positions/consciousness-scope/#p-cs2), [P-CS3](/positions/consciousness-scope/#p-cs3)) share a single 2026-06-22 date, which is a batch stamp rather than four independent reviews. None shows substantive drift on reading — the staleness is in the field, not visibly in the content.

## Check 6 — Cascade health

**No cascade errors are possible in the current register: all 61 entries are `live`.** There is no `superseded` or `retired` entry anywhere in the 17 domain files, so there is no retired-position-with-live-dependents case to flag.

Recorded as an observation rather than a defect: a register 15 months old that has never retired or superseded a single entry is a fact worth the operator's notice. The corpus does record *reclassifications* ([P-I1](/positions/individuation-and-subjecthood/#p-i1) and [P-MC1](/positions/arguments-for-mental-causation/#p-mc1) on 2026-08-03) and band movements, so positions do change — but the retire/supersede path has never been exercised, and its cascade machinery is therefore untested in practice.

## Check 7 (register-specific) — Foundational-dependency test coverage

**This is the audit's one structural finding.**

`positions.md:108` records the foundational-dependency test — *"a position counts as retireable only if removing it leaves every tenet with an intact rationale"* — and states that a **register-wide sweep on 2026-08-03 "completed the application"**.

The test is applied at **file level**, in each domain file's preamble. Coverage measured this run: **15 of the 17 domain files carry it**, and the coverage is impressively current — every domain created since the sweep carries it, including `memory-and-autonoesis` ([P-MA1](/positions/memory-and-autonoesis/#p-ma1), created 2026-09-20), and every file's count-claim still matches its entry count (`quantum-interface` "all eleven" = 11; `consciousness-scope` "all six" = 6, naming [P-CS6](/positions/consciousness-scope/#p-cs6) added 2026-09-20; `ai-consciousness-scope` "all four" = 4; `arguments-for-dualism` "All three" = 3; `subject-census` "Two of the three" = 3; `methodology-and-calibration` "all five" = 5; `value-in-selection` "all four" = 4).

**Two files carry no foundational-dependency statement at all:**

| File | Entries | Reason it was missed |
|---|---|---|
| [positions/voids-as-evidence.md](/positions/voids-as-evidence/) | 3 — [P-V1](/positions/voids-as-evidence/#p-v1), [P-V2](/positions/voids-as-evidence/#p-v2), [P-V3](/positions/voids-as-evidence/#p-v3) | Never covered. `positions.md:108`'s own enumeration of the 2026-08-03 sweep lists "the quantum-interface, consciousness-scope, AI-scope, dualism-argument, methodology and finding-level domains" — **`voids-as-evidence` is absent from that list**, so the sweep that declared itself complete did not reach it. |
| [positions/ai-substrate-verdicts.md](/positions/ai-substrate-verdicts/) | 1 — [P-AS1](/positions/ai-substrate-verdicts/#p-as1) | Domain file created **2026-08-20**, seventeen days *after* the sweep, and never retrofitted. |

Verified with variant spellings (`foundational-dependency`, `foundational dependency`, `retireable`, `retirable`, `rationale`, `None are tenets`, `not tenets`) — all zero in both files, against a working positive control on `value-in-selection.md`.

**Not repaired here**, because audit mode is read-only by the skill's own contract. The verdicts look derivable from rules the corpus has already stated rather than needing fresh judgement — [P-V1](/positions/voids-as-evidence/#p-v1)/[P-V2](/positions/voids-as-evidence/#p-v2)/[P-V3](/positions/voids-as-evidence/#p-v3) are discount rules *on* the void catalogue's evidential payoff, which is the "inverse direction" pass `positions.md:108` already defines and `finding-level-calibration.md` already states for its own domain; [P-AS1](/positions/ai-substrate-verdicts/#p-as1) is a per-class substrate verdict sibling to [P-AC1](/positions/ai-consciousness-scope/#p-ac1), which passes. But writing it is an edit, and a task has been queued instead.

This is a clean instance of the position it falls under: **[P-M5](/positions/methodology-and-calibration/#p-m5)**, *disclosure is not self-correction — a discipline binds only as far as the pipeline enforces it*. The test is documented, was declared complete, and has two gaps that survived 49 days because nothing re-checks coverage.

## Leads adjudicated

### Lead 1 — Does any register entry breach the [P-CS6](/positions/consciousness-scope/#p-cs6) partition?

**No.** [P-CS6](/positions/consciousness-scope/#p-cs6) (added 2026-09-20) partitions filter evidence: transmission-over-production evidence "bears on Tenet 1 and nothing else", and "Tenet 3's outbound leg is therefore owed a *separate* argument rather than carried over".

The containment is **structural, not entry-by-entry**: every citation of every filter article in the entire 17-file register sits on one line — `consciousness-scope.md:110`, which is [P-CS6](/positions/consciousness-scope/#p-cs6)'s own `Argued in` line. Independently re-verified this run: `filter-theory` 1 hit, `psychedelics-and-the-filter-model` 1 hit, `filter-vs-interface-distinction` 3 hits (frontmatter, `Argued in`, [P-CS6](/positions/consciousness-scope/#p-cs6)'s own Updated note) — all in `consciousness-scope.md`. No other domain file cites filter evidence at all, so no other entry is in a position to breach the partition.

Candidates examined and cleared: **[P-CS4](/positions/consciousness-scope/#p-cs4)** (adjacent-clean — uses the filter inbound only, "what the filter transmits when sensory gating and prefrontal constraint loosen", concluding non-division rather than outbound causation, and its `Depends on` says "explicitly *not* the quantum-interface register"); **[P-Q9](/positions/quantum-interface/#p-q9)** (partition-confirming — "MQI's bandwidth-limited outbound channel" argues the outbound leg on quantum grounds, exactly where [P-CS6](/positions/consciousness-scope/#p-cs6) assigns it); **[P-D3](/positions/arguments-for-dualism/#p-d3)**, **[P-CS1](/positions/consciousness-scope/#p-cs1)**, **[P-AC1](/positions/ai-consciousness-scope/#p-ac1)/[P-AC3](/positions/ai-consciousness-scope/#p-ac3)**, **[P-MC4](/positions/arguments-for-mental-causation/#p-mc4)** (all homonym false hits — "Indo-Greek transmission", "the quantum substrate filter" as a screening criterion, "substrate-permissive", "reducing the aesthetic catalogue").

⚠️ **Method note for the record**: a first pass returned `NDE` = 699 hits across the 17 files. That was substring conflation — matching *u**nde**feated*, *i**nde**pendent*, *u**nde**r*. The word-boundary form returns 0, and the absence was then licensed by positive controls showing the same terms live in 104–234 corpus files each.

**Recorded, not decided**: [P-CS6](/positions/consciousness-scope/#p-cs6)'s `Argued in` cites `concepts/filter-theory` as authority, and today's tenet check #137 found *that article* breaching the partition. That is an article-layer defect with a register-layer citation exposure — **not** a register breach, since [P-CS6](/positions/consciousness-scope/#p-cs6)'s own prose states the partition correctly. The repair belongs in `concepts/filter-theory`, not here.

### Lead 2 — Do other entries with a `grade D` / `discriminability direct` pairing state their standing as plainly as [P-MA1](/positions/memory-and-autonoesis/#p-ma1)?

**The question has no comparison class: [P-MA1](/positions/memory-and-autonoesis/#p-ma1) is the only entry in the register with that pairing.**

- **direct** discriminability: 4 entries — [P-A3](/positions/agency-and-will/#p-a3) (grade B), [P-AC4](/positions/ai-consciousness-scope/#p-ac4) (grade B), [P-MA1](/positions/memory-and-autonoesis/#p-ma1) (grade D), [P-Q6](/positions/quantum-interface/#p-q6) (grade A).
- **grade D**: 21 entries, of which exactly one — [P-MA1](/positions/memory-and-autonoesis/#p-ma1) — is also *direct*.

So the specific worry (that a D/direct pairing might elsewhere read as *survived-when-untested*) cannot arise elsewhere, because nowhere else is a claim with no independent empirical support paired with a runnable decisive test. The other three *direct* entries carry grades A or B, i.e. the test has been run and reported.

Checking the broader shape — whether any entry lets "unrefuted" pass as "survived" — the standing vocabulary is concentrated exactly where it should be: `unrefuted` appears only in `memory-and-autonoesis` (3) and `moral-status` (1); `untested` in `memory-and-autonoesis` (4), `quantum-interface` (4) and `value-in-selection` (1). [P-MA1](/positions/memory-and-autonoesis/#p-ma1) states the distinction explicitly — *"unrefuted and untested, the weakest of the falsifier states … unrefuted is not survived"* — and [P-MS1](/positions/moral-status/#p-ms1) uses the same construction (*"unrefuted and contested, not tested"*). **No entry was found stating a survived-when-untested standing.** [P-MA1](/positions/memory-and-autonoesis/#p-ma1)'s own handling is, on this evidence, the register's model case rather than a risk.

## Recorded, not decided

Three items observed during the pass that belong to the operator, logged here without action:

1. **Length has escalated sharply since it was last measured, and one file is now `critical`.** The open NEEDS-HUMAN entry `todo.md:1148` (2026-08-03) reads *"5 of 13 files already breach"*. Re-measured this run with `analyze_length`: **14 of the 18 register files breach** (excluding the six `*-calibration-history` companions, which add 5 more breaches of their own — 19 of 23 overall). **[positions/quantum-interface.md](/positions/quantum-interface/) is at 5930 words against a 4000 critical threshold — 1930 words over**, and is the only `critical` file. `individuation-and-subjecthood` (3938, 62 from critical) and `methodology-and-calibration` (3922, 78 from critical) are next. Note that `quantum-interface` *already has* a calibration-history companion file and is still critical, so the split convention has not held the line. No new task minted — this is the existing NEEDS-HUMAN item, with a current figure.

2. **The retired single-band vocabulary is live on the published surface.** `hugo/data/positions.yaml` is current as to membership (all 61 IDs present) but renders every entry's band as `bands: 'confidence: moderate · limited or indirect evidence · framework-critical'` — the **retired single Confidence band** — and its `summary` string, which is what the site surfaces, reconstructs the same retired label. Of the six multi-axis axes only three (`credence`, `grade`, `structural_centrality`) are exported; `model maturity`, `empirical discriminability` and `framework-internal only` are not. This is a concrete surface of the logged NEEDS-HUMAN governance defect at `todo.md:671` (the multi-axis schema enforced by no tool, and `/positions-evolve` still keyed to the retired band) and is **explicitly out of scope** for this audit. Recorded; nothing decided.

3. **The retire/supersede path has never been exercised** (Check 6 above).

## Summary

| Check | Result |
|---|---|
| 1. Contradictions | **None.** 7 cross-seam candidates raised, all adjudicated as disclosed-and-scoped |
| 2. Dependencies resolve | **Clean.** 0 unresolved of all references across 61 entries |
| 3. Orphans | 6 of 61 not cited from the article layer |
| 4. Calibration vocabulary | **Clean.** 61/61 in-vocabulary; aggregate re-derived and reproduces exactly; no band moved |
| 5. Staleness | 6 entries >60 days |
| 6. Cascade health | **Clean** — all 61 `live`, no retired-with-dependents case possible |
| 7. Foundational-dependency coverage | **1 finding** — 2 of 17 files never received the test |

One follow-up task queued, for Check 7.