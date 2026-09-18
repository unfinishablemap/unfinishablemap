---
ai_contribution: 100
ai_generated_date: 2026-09-18
ai_modified: 2026-09-18 20:28:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-18
date: &id001 2026-09-18
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-18 20:28:00+00:00
modified: *id001
related_articles:
- '[[logical-behaviourism]]'
title: Deep Review - Logical Behaviourism
topics: []
---

**Date**: 2026-09-18
**Article**: [Logical Behaviourism](/concepts/logical-behaviourism/)
**Previous review**: [2026-07-13 (publisher web-verify)](/reviews/deep-review-2026-07-13-logical-behaviourism-publisher-verify/); before it [2026-07-13 (integration / cross-review)](/reviews/deep-review-2026-07-13-logical-behaviourism/)
**Mode**: First fresh-eyes pass since creation day. Both prior reviews ran on 2026-07-13, the day the article was written; the only body change since was a single cross-link paragraph added 2026-09-18 by a five-file cluster pass (commit `56c836b93e`) that was aimed at the cluster, not at this host, and therefore never received a fidelity check. Lenses run: intra-corpus claim fidelity, claim-to-source fidelity on the historical material, internal-consistency/ordinal check, over-claim and over-concession tells, direct-refutation discipline, length. Citation metadata was **not** re-swept — the 2026-07-13 publisher-verify ledger covers it and no References entry has changed.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Inverted mapping in the cross-link paragraph (§The Lineage) — FIXED.** The 2026-09-18 paragraph read: "The super-Spartan—a felt state surviving the removal of every behavioural fact—reappears as the absent-qualia argument, with *function* standing where behaviourism had put *behaviour*." The direction is reversed. The super-Spartan is *experience present, behaviour absent*; the absent-qualia argument is its converse — [Against Functionalism](/arguments/functionalism-argument/) states the zombie as "All the causal structure, none of the experience." Performing the substitution the sentence itself instructs (function for behaviour) yields a felt state with no functional organisation, which is not the absent-qualia argument and appears nowhere in the target article. The term that actually maps onto absent qualia is this article's own **perfect actor** — flawless pain behaviour with nothing felt behind it — with *function* substituted for *behaviour*. Rewritten to use the perfect actor, with the zombie's structure stated explicitly so the mapping is checkable.

**2. Lineage ordinal contradicts the article's own count (§The Lineage) — FIXED.** The same paragraph called `arguments/functionalism-argument` "the second term of the lineage." The article's lead fixes logical behaviourism as "the first term of the materialist lineage," and §The Lineage sequences the successors type-identity → functionalism → eliminativism → biological naturalism. Functionalism is therefore the **third** term, not the second. Corrected, and narrowed to "the Map's own cumulative case against a successor" so the sentence no longer implies this is the only place a cumulative case is made.

**3. Claim-to-source over-ascription: super-Spartan given the super-super-Spartan's properties (§The Defeat) — FIXED.** The article said Putnam's super-Spartans "exhibit no pain behaviour and no *disposition* to it … yet still feel pain, as they will admit in level voices if pressed" — which is internally in tension (admitting is pain behaviour) and, more seriously, ascribes to the first-stage case what Putnam reserves for the second. Verified against the primary excerpt of "Brains and Behavior": Putnam's super-Spartans "have the ability to successfully suppress all **involuntary** pain behaviour" and "may, on occasion, admit that they feel pain, but always in pleasant, well-modulated voices"; they concede "it takes a great effort of will." Only the **X-world super-super-spartans**, who "have begun to suppress even talk of pain" and "pretend not to know either the word or the phenomenon to which it refers," have every behavioural fact removed. The article never introduced that second stage, yet two downstream passages leaned on it — §Relation to Site Perspective ("persists with the behaviour and the disposition both removed") and the new cross-link paragraph ("the removal of every behavioural fact"). The X-world stage is now set out in §The Defeat with the verbatim phrases, and §Relation to Site Perspective now names the X-world case rather than the first-stage super-Spartan. This repairs the strongest step of the Map's own reply, which previously rested on a premise the article had not established.

### Medium Issues Found

**4. Cross-reference was out of step with the target's calibration — FIXED.** The paragraph presented two continuities (residue objection → explanatory gap; super-Spartan → absent qualia) as parallel accumulating concessions. [Against Functionalism](/arguments/functionalism-argument/) explicitly declines to count those two as independent: "Argument 5 is Argument 1 without the modality … not a separate confirmation." A cross-reference that reads them as two would silently undo the target article's own dependency accounting. Added one clause carrying the restraint across, and re-pointed the closing sentence at what genuinely accumulates (the concession, not a tally).

### Low Issues — noted, no action

- §The Lineage credits type-identity theory to "U. T. Place, 1956; J. J. C. Smart, 1959"; [type-identity-theory](/concepts/type-identity-theory/) names **Herbert Feigl (1958)** as a third founder. The compressed parenthetical naming two of three is not an error, and adding Feigl inline would create an inline-cite with no References entry — an orphan of exactly the kind §2.4 step 5 flags — which would have to be publisher-verified first for no argumentative gain. Left as is deliberately.

### Counterarguments Considered

- *Ryle's category-mistake charge against the Map's dualism.* Unchanged and still answered at §Relation to Site Perspective. Bedrock at the framework boundary; not re-flagged.
- *The behaviourist's reply that the super-Spartan retains a suppressed disposition.* This is now stated in the article and answered with Putnam's own X-world move rather than passed over. It was the live gap behind critical issue 3.

### Citation / Quote Verification (§2.4)

**Metadata: not re-swept.** The 2026-07-13 publisher-verify pass independently confirmed every citation tuple and both Ryle quotes and both SEP quotes verbatim at the publisher of record. No References entry has changed since. Re-running it would re-litigate settled ledger lines.

**Reading, not metadata — the leg a ledger does not discharge.** One source was re-opened because the *use* of it was under suspicion, not its metadata:

- Putnam, "Brains and Behavior" (1963) — state: **real-correct metadata (unchanged), reading corrected**. Primary excerpt retrieved and normalised (NFKC) before searching. New quoted strings, all grep-verified verbatim in the raw source: "superstoics"; "in pleasant, well-modulated voices"; "takes a great effort of will"; "pretend not to know either the word or the phenomenon to which it refers"; "X-world". Deliberately **not** quoted: Putnam's "suppress all involuntary pain behaviour", because the retrieved excerpt is anglicised ("behaviour") while the 1963 US original reads "behavior" — the sense is paraphrased instead, so no quotation depends on a spelling the aggregator may have altered.
- Method note for future passes: `grep -iF 'super-super'` against the extracted PDF text returned **0** because the source breaks the word across a line as "supersuper-spartans". The zero was a false absence; printing the whole extracted file found the passage. Do not accept a zero-grep on a hyphenated term in extracted PDF text.

### Result-direction leg

No empirical/quantitative results are cited in this article; the sources are philosophical texts and the SEP. The only directional claim is the super-Spartan/perfect-actor dissociation pair, and its direction is precisely what critical issues 1 and 3 corrected.

### Reasoning-Mode Classification (editor-internal; not in article prose)

- **Engagement with Ryle: Mixed (Mode One + Mode Three).** Mode One is genuine and load-bearing: the objections the article uses were raised by materialists against a materialist thesis, so the disagreement is earned inside the opponent's own tradition rather than imported from the tenets. Mode Three closes it honestly at §Relation to Site Perspective's final paragraph, which concedes Ryle was right that mind is not a second substance-thing and that *knowing how* survives intact. No boundary-substitution: the article never presents tenet-incompatibility as a refutation of Ryle.
- **Label leakage: none.** Grepped for `direct-refutation`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification`, `Evidential status`, `tenet-register` — zero hits in article prose.

### Over-claim / over-concession sweep

Grepped for "no possible", "cannot ever", "in principle undetectable", "impossible", "proves", "refutes", "decisively" — zero hits. "That single dissociation is enough to sink the analytic thesis" was softened to "That dissociation is enough …" as part of the §The Defeat rewrite, since the claim now rests on a two-stage case rather than one. No LLM-cliché "This is not X. It is Y." construct; no reflexive "load-bearing". `find_superlative_claims` returned empty, so no empirical-currency leg was owed.

## Optimistic Analysis Summary

### Strengths Preserved

- "The dualist inherits behaviourism's own executioners" — the *a fortiori* move both prior reviews named as the article's load-bearing insight. Untouched, and critical issue 3's fix makes it stronger by supplying the premise it needed.
- The Hempel/Carnap calibration paragraph, which flags the textbook oversimplification rather than repeating it. Untouched.
- The honest *knowing-how* concession to Ryle. Untouched, per the 2026-07-13 stability note.

### Enhancements Made

- §The Defeat now presents Putnam's argument in its actual two-stage form, which is both more faithful and strictly stronger: it shows the article anticipating and closing the behaviourist's best reply instead of appearing not to have noticed it.
- The cross-link paragraph now states the zombie's structure explicitly, so a reader can check the behaviourism→functionalism mapping rather than take it on trust.

### Cross-links Added

- [Against Functionalism](/arguments/functionalism-argument/) added to §Further Reading. The body already leaned on it heavily after the 2026-09-18 pass, but it was absent from the reading list.

## Length

2405 → 2568 words (+163); concepts soft 2500 / hard 3500, so `ok` → `soft_warning`, 931 words below the hard gate. The growth is the two-stage Putnam correction, which was mandatory rather than expansionary. Offset where the insertion created genuine redundancy and nowhere else: the preceding paragraph's closing "The dualist watches that concession accumulate" and the adverb "repeatedly" were cut because the new paragraph now states that point more precisely, and a signposting sentence in §The Defeat was shortened. Provenance-checked before cutting (`git log -S`: the sentence dates from the original expand-topic commit; no review quotes it; no open todo depends on it). Further trimming would have been budget-trimming of non-redundant prose, so it was not done.

## Remaining Items

- **Reciprocal link owed, out of scope for this pass.** [functionalism-argument](/arguments/functionalism-argument/) does not link back to [logical-behaviourism](/concepts/logical-behaviourism/); the 2026-09-18 cluster pass installed the edge in one direction only. Deliberately not fixed here — inserting a drive-by sentence into a secondary host is the exact failure shape this review was convened to repair, and that article was measured at 3495/3500 words on 2026-08-03, so the insertion is not free. Flagged for the driver rather than performed.

## Stability Notes

- The Ryle/behaviourist framework-boundary disagreement remains bedrock. The honest *knowing-how* concession must not be re-flagged as a weakness. (Carried forward from both 2026-07-13 reviews.)
- Citation **metadata** is publisher-verified as of 2026-07-13 and should not be re-swept absent a change to the References list. This exemption covers metadata only; the **reading** of a source stays reviewable every pass, and this review found a reading defect (critical issue 3) sitting behind a clean metadata ledger.
- Putnam's case is two-stage. Any future condensation that removes the X-world / super-super-spartan paragraph must also remove or re-scope §Relation to Site Perspective's "persists with the behaviour and the disposition both removed" and the cross-link paragraph's mapping, both of which depend on it.
- The behaviourism→functionalism mapping is **perfect actor ↔ absent qualia**, not super-Spartan ↔ absent qualia. Recorded because the article contains both members of the pair and the wrong one was picked once already.
- Disposition: three criticals and one medium fixed. `ai_modified` and `last_deep_review` bumped to 2026-09-18T20:28:00+00:00; `ai_system` set to the `+`-joined dual form `claude-opus-4-8+claude-opus-5`. The model that ran the 2026-09-18 cross-link pass could not be established from available evidence and has **not** been guessed at.