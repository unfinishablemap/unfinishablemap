---
title: "Outer Review Synthesis - 2026-10-08"
created: 2026-10-08
modified: 2026-10-08
human_modified: null
ai_modified: 2026-10-08T05:09:44+00:00
draft: false
description: "Cross-review synthesis of 2 outer reviews from 2026-10-08 (ChatGPT 5.6 Sol Pro, Claude Fable 5.1; Gemini failed), both auditing topics/clinical-dissociation-as-systematic-evidence. Eleven convergent loci adjudicated against the live text; one task upgraded P2 → P1; the retitle recorded as a human decision."
topics:
  - "[[clinical-dissociation-as-systematic-evidence]]"
  - "[[neurological-dissociations-as-interface-architecture]]"
  - "[[split-brain-consciousness]]"
concepts:
  - "[[depersonalisation]]"
  - "[[filter-theory]]"
related_articles:
  - "[[project]]"
  - "[[evidential-status-discipline]]"
  - "[[altered-states-as-interface-evidence]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-08
last_curated: null
synthesizes:
  - reviews/outer-review-2026-10-08-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-10-08-claude-fable-5-1.md
synthesis_coverage: "2/3"
---

**Date**: 2026-10-08
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 2 of 3 commissioned reviewers contributed. The Gemini 2.5 Pro Deep Research leg is `failed`: the plan stage hung at "Generating research plan" on two attempts (conversations de0b8e1361c5e1c4 and 3170e65703803cdb), the same failure as 2026-10-07; research never started and nothing was collected.

**Subject**: audit of [[clinical-dissociation-as-systematic-evidence]] (`topics/`, 198 lines, 4,694 body words against a 4,000 hard ceiling under a standing 2026-06-04 human length decision; last substantively modified 2026-10-01 by a single wikilink insertion). Both reviewers were given the same subject (`reuse:pending-reviews`) and both read the live page.

## TL;DR

Both reviewers independently reach the same verdict — the article's evidence is *compatible* with the interface reading, not *suggestive* of it, and the body already concedes this while the title, `description:`, summary table and Further-Reading gloss still carry the pre-calibration tier — and independently land on the same eight citation-fidelity defects (intact-substrate ladder, the Sierra & Berrios / "perceptual cortex functions normally" sentence, Hassa PPI read as direction, Voon's happy-only Granger result, the amnesia-recovery overclaim, the dangling Anderson & Hanslmayr citation, "anaesthesia" for propofol sedation, the Reinders "connectivity" gloss plus the 2024 inter-identity-transfer meta-analysis). Every quoted locus was confirmed live and every external claim against PubMed by the two processing passes; this synthesis re-read each locus. Clusters: **11 convergent** (3 of them adjudicated as already-handled or disputed, so recorded but not actioned), **9 singleton**, **4 divergent**. Task changes: the P1 on the article already carried both reviewers' loci and was amended (plural review-files field, synthesis link, a three-item addendum for the convergent loci neither processing pass had carried in); the `evidential-status-discipline` methodology task was upgraded **P2 → P1**; no tasks were deduplicated (the Claude processing pass had already folded its findings into the ChatGPT tasks rather than minting siblings); the three other P2s stay at P2 as single-reviewer loci.

## Convergent Findings

Adjudication rule applied throughout: a locus counts as convergent only when both reviewers name the *same* sentence or structural defect, the live text still carries it, and neither processing pass disputed the reviewer's reading. Where the two reviewers reached the same conclusion but the processing passes showed the conclusion to be wrong or already handled, the cluster is listed here with a "recorded only" action — two reviewers making the same mistake is correlated error, not evidence.

### 1. The intact-substrate ladder (L56 → L64 → L68 → L102 → L139)
- **Flagged by**: chatgpt, claude
- **Verification**: clean. L56 "undamaged, not unchanged"; L64 "no lesion, no atrophy, no pharmacological blockade … without anything being broken"; L68 "without any substrate change"; L102 "the substrate is intact: structural neuroimaging is typically unremarkable"; L139 "the substrate stays whole" — all live. Dimitrova et al. 2021 (PMID 34165068: smaller bilateral hippocampal and CA1 volumes in 32 DID vs 43 controls) confirmed by the ChatGPT processing pass. Claude's additional sources (Tramoni 2009; "organic antecedents in about a third" of Mangiulli's cases) are from secondary summaries and the reviewer says so.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Only the first, and sometimes the second, are supported. The others are much stronger and are contradicted or at least materially complicated by structural, functional and network-level findings omitted from the article."
  - **Claude Fable 5.1**: "The core inferential error is a slide from 'no structural lesion' to 'no substrate change'."
- **Task action**: already covered — P1 `topics/clinical-dissociation-as-systematic-evidence` item (1) (todo.md L1883; no upgrade possible above P1).

### 2. L88: Sierra & Berrios 1998 carrying an imaging finding, and "while perceptual cortex functions normally"
- **Flagged by**: chatgpt, claude
- **Verification**: clean on the perceptual-cortex clause — contradicted by two independent sources: Phillips et al. 2001 (PMID 11756013, reduced insula *and occipito-temporal* activation; ChatGPT) and Simeon et al. 2000 (PMID 11058475, sensory-association-cortex metabolic abnormalities; Claude). **Partly disputed** on Claude's further charge that S&B 1998 is "mis-typed" as passive disconnection: the Claude processing pass found the abstract applies Geschwind's disconnection concept *and* proposes active prefrontal inhibition, so the article's "disconnection" gloss is the authors' own; the fair residue is that the section header "Goes Silent" obscures the active-inhibition mechanism.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "This is the clearest citation error. The paper is a theoretical neurobiological review/model. It is not an imaging experiment showing reduced insula or amygdala activation while perceptual cortex functions normally."
  - **Claude Fable 5.1**: "'While perceptual cortex functions normally' is contradicted. The first PET study of DPD (Simeon et al. 2000, Am J Psychiatry) reported sensory-association-cortex abnormalities."
- **Task action**: already covered — P1 items (2) and (11) (header "Goes Silent" → "Is Inhibited").

### 3. L110: Hassa 2017 "replicated the direction" (PPI is undirected) and Voon 2010 without its qualifiers
- **Flagged by**: chatgpt, claude
- **Verification**: clean (Hassa PMID 28529870, PPI; Voon PMID 20371508, Granger significant for happy stimuli only, positive-symptom sample).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "PPI detects condition-dependent statistical coupling; it does not determine causal direction."
  - **Claude Fable 5.1**: "Hassa et al. 2017 did not replicate 'the direction'. It used psychophysiological interaction (PPI) analysis, which is non-directional."
- **Task action**: already covered — P1 item (3).

### 4. L102: amnesia recovery overclaim — "typically return as a body", "reconnection, not reconstruction", the terminal-lucidity analogy, Staniloiu & Markowitsch 2014 as the source
- **Flagged by**: chatgpt, claude
- **Verification**: clean. Both note S&M 2014 is a *Lancet Psychiatry* Review that cannot carry a frequency claim; Claude adds that Markowitsch's own mechanism (a stress-hormone "mnestic block") is a production-side account, so the citation is recruited against its authors' stance. Both say the article withdraws the Mangiulli 2022 concession it has just made at L98.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The article cannot use Mangiulli as a caveat and then continue with the positive case as though the caveat concerned only a minority of reports."
  - **Claude Fable 5.1**: "Staniloiu & Markowitsch 2014 is a co-optation firewall failure. … Markowitsch's own mechanism … is exactly the production-side account the article says faces a terminal-lucidity-type difficulty."
- **Task action**: already covered — P1 item (4) (deletes both phrases and the terminal-lucidity clause).

### 5. L98: Anderson & Hanslmayr cited in the body with no reference entry
- **Flagged by**: chatgpt, claude
- **Verification**: clean — confirmed absent from References L179–198 (this synthesis re-listed the twenty entries). Both reviewers also turn it into a methodology recommendation (ChatGPT item 44, Claude item 17: a body-citation-resolves-to-reference gate).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "One significant body citation—'Anderson and Hanslmayr's motivated-forgetting work'—has no corresponding bibliographic entry."
  - **Claude Fable 5.1**: "Tulving; Anderson & Hanslmayr; the 'fixed order' claim — Missing from references — ADD or DELETE."
- **Task action**: already covered — P1 item (5); the gate recommendation is in the upgraded methodology task (cluster 9).

### 6. L106: "Under anaesthesia or hypnosis, the 'paralysed' limb may move normally"
- **Flagged by**: chatgpt, claude
- **Verification**: clean. ChatGPT traced it to the sibling `conversion-disorder-as-consciousness-side-fault` L67 (Stone et al. 2014, eleven patients under propofol *sedation*, uncontrolled); Claude flags it as unsourced. The two readings are compatible: the sentence is both unsourced and a flattening of the sibling's grade.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "The target article suppresses precisely the evidential qualifications its linked article supplies."
  - **Claude Fable 5.1**: "'Under anaesthesia or hypnosis, the "paralysed" limb may move normally' is unsourced."
- **Task action**: already covered — P1 item (6).

### 7. DID: Reinders 2003 rCBF glossed as a "connectivity-pattern signature" (L80) and the partition language (L74/L78/L80) against the objective inter-identity-transfer literature (Marsh 2021; Beker 2024; Donath 2025)
- **Flagged by**: chatgpt, claude
- **Verification**: clean. Beker et al. 2024 (PMID 39541721) confirmed by the ChatGPT pass; Huntjens 2012, Dimitrova 2024, Reinders 2012 and Donath 2025 confirmed to exist by the Claude pass (Donath's abstract not indexed, so its "both support memory transfer" wording is unverified at abstract level). Both reviewers say the L82 Marsh concession never reaches the section's opening sentence.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "That is exactly the kind of result that should replace confident language about a stable autonoetic partition."
  - **Claude Fable 5.1**: "The article's own Marsh paragraph is accurate, but its concession never reaches the opening sentence, the 'autonoetic partition' claim, or the table."
- **Task action**: already covered — P1 items (7) and (10).

### 8. Body-to-surface propagation: the body grants *compatible* ("neither reading is forced", L151; "constrains both readings", L131) while L3 `description:`, L62, L118 "What Disconnects", L125, L151 "among the more suggestive" and the L161 apex gloss keep the pre-calibration tier
- **Flagged by**: chatgpt, claude
- **Verification**: clean. The apex `altered-states-as-interface-evidence` `description:` was recalibrated 2026-10-02 to "constrains the structure of consciousness-brain coupling without deciding between filter and production readings"; the target's L161 gloss still reads "converging on the same multi-channel interface architecture". Both reviewers' headline verdicts ("architecture-supporting, ontology-underdetermining, quantum-neutral" / "DEMOTE-TO-COHERENCE-ONLY") are the same tier placement.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Its statement that dissociation is 'among the more suggestive empirical evidence' is stronger than the apex methodology warrants."
  - **Claude Fable 5.1**: "Those corrections were not propagated to the title, meta-description, table or sibling pages. That is the site's own P-M5 ('Disclosure is not self-correction') recurring at article scale."
- **Task action**: already covered — P1 item (9) (description, table column, L161 gloss) plus the trim list (L62, L125, L139). The **retitle** both reviewers propose ("…as a Constraint on Interface Models") changes a URL with inbound links and external citations and is recorded as a **human decision**, not a task — see Method Notes.

### 9. Methodology: a source-type / author-stance labelling rule and a dangling-citation gate beside the discipline doc's four-levels rule
- **Flagged by**: chatgpt, claude
- **Verification**: clean — the exhibits are the verified defects in clusters 2, 4 and 5. ChatGPT items 42 (label every reference by source type), 44 (automated check for body citations missing from the bibliography), 45 (absence ladder), 48 (inference fidelity ≠ quotation fidelity); Claude items 12 (change-propagation gate), 13 (stance-layer check: record each cited author's own mechanism), 17 (every in-text authority must resolve to a reference). ChatGPT 44 and Claude 17 are the same rule from the same exhibit; ChatGPT 42 and Claude 13 are the same rule from the Sierra & Berrios and Staniloiu & Markowitsch exhibits.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Add an inference-fidelity audit distinct from quotation fidelity: an exact quotation can still be used to support a conclusion the source treats only as speculative."
  - **Claude Fable 5.1**: "Add a mandatory stance-layer check: record each cited empirical author's own mechanism, and state it whenever the citation is used to burden production views."
- **Task action**: **Upgraded P2 → P1**: "`project/evidential-status-discipline` — add the 'absence ladder' and a source-type labelling rule…" (todo.md L1925; was 1 task carrying both reviewers via a "Convergent (Claude)" addendum — no deduplication needed). The remaining methodology items from both reviewers (claim–evidence matrices, bridge-law register, likelihood comparisons, expert review, strawman lint, symmetric cost accounting) overlap the five open NEEDS-HUMAN methodology entries of 2026-07-25 → 2026-08-01 and are not re-minted.

### 10. L68 fixed autonoetic → anoetic ordering stated as fact; L141 "paid once at the tenet level"; L106 FND grouped with the dissociative disorders without a stated nosological basis
- **Flagged by**: chatgpt, claude (all three loci)
- **Verification**: clean. L68 "Across most consciousness disruptions these degrade in a fixed order—autonoetic first, anoetic last" is live; Tulving is not in the reference list and the ordering is the Map's own thesis (held in `memory-channel-interface-evidence`), not Tulving's. L141 "paid once at the tenet level rather than per-case" is live; both reviewers read it as waiving the cost, and the article's own L131/L151 grant the rival predicts the same selectivity. The article names FND's DSM-IV lineage at L106 but nowhere states that only ICD-11 files it among the dissociative disorders (zero `ICD` hits in the file).
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "Tulving's taxonomy distinguishes forms of memory-associated consciousness; it does not establish a universal law of vulnerability." / "Treating the metaphysical interface as a cost paid once protects the theory from being charged for its case-specific mechanisms." / "Distinguish FND from the dissociative disorders and explain that dissociation is a variable comorbidity or proposed mechanism rather than a defining mechanism of all FND."
  - **Claude Fable 5.1**: "P4. Tulving fixed order 'autonoetic first, anoetic last' with no substrate change — REVISE-HARD (unsourced)" / "A cost 'paid once at the tenet level' is waived, not met." / "The article follows ICD-11 without saying so."
- **Task action**: neither processing pass had carried these three into the P1 (ChatGPT's pass deferred the ordering question to a research-grade review of `memory-channel-interface-evidence`; Claude's pass did not list them). Added as **P1 items (15)–(17)** in a synthesis addendum, ranked after (13) and before the optional (14), each a single substitution the trim list must pay for. The research-grade cross-condition review of the ordering itself stays with the harvester, as the ChatGPT pass recorded.

### 11. L147 "the mind protecting itself by severing access" and L78 "a single non-physical mind … the alters may be different configurations of the interface"
- **Flagged by**: chatgpt, claude
- **Verification**: clean on the text (both live). ChatGPT §9 reads L147 as unlicensed teleology and L78 as an untested unity-of-mind premise; Claude §2.3 reads L147 as undischarged Tenet 3 causal work (P-Q3/P-Q10) and L78 as conflicting with register entries P-I3 ("subject boundaries determinate but not readable off physical structure") and P-I4. P-I3 and P-I4 confirmed verbatim in `positions/individuation-and-subjecthood.md` L73/L85. The ChatGPT processing pass marked the unity-of-mind bracketing as a framework-boundary disagreement already recorded as bedrock by the 2026-07-18 deep review; the Claude pass minted the register-consistent fix instead of the bracketing complaint. The two reviewers agree on the locus and the direction (the one-subject reading is a reading, not a result), so the cluster stands.
- **Quotes**:
  - **ChatGPT 5.6.sol Pro**: "All observed fragmentation is allocated to the interface because the tenet requires the mind to survive intact. This makes the interpretation difficult to falsify."
  - **Claude Fable 5.1**: "P-I3 reads 'Subject boundaries are determinate but not readable off physical structure'. So 'a single anatomically intact brain' cannot fix the number of subjects."
- **Task action**: already covered — P1 items (13) (L78 P-I3 clause) and (14) (L147, optional); the register side is the P2 positions-evolve task (todo.md L1951), which stays at P2 because its primary deliverable (extending P-CS4's fragmentation list) is single-reviewer.

### Convergent but recorded only (adjudicated: already handled or disputed)

- **Changelog traceability** (ChatGPT §1 and item 58; Claude §2.0 "No visible entry touches the target"). Both reviewers note the 2026-10-01 modification is not findable in the public changelog by title or slug. The ChatGPT processing pass established that the 2026-10-01 change was a single wikilink insertion made by the `depersonalisation` expand-topic (commit e9c35898c8); the changelog logs tasks, not every file touched. **No defect**; two reviewers were sent to a "substantive revision" that was not one — the commission prompt's wording, not the site, misled them.
- **Janet "anticipates the Map's interface architecture" is anachronistic** (ChatGPT §5, item 28; Claude §2.1 "Janet", fix 1). Both correct about the risk, but live L60 already ends the sentence "despite a wholly different theoretical setting" and the preceding sentence says Janet's framework "was psychological rather than neurological". **Already hedged**; not minted by either pass, and not by this synthesis.
- **The L141 perturbation discriminator "yields the same prediction under production theories"** (ChatGPT §2 table and item 26; Claude §2.2 "Does the filter reading predict anything"). Both reviewers say it. The ChatGPT processing pass showed the dedicated `targeted-lesion-discriminating-tests…` article (L42–44) specifies the divergent predictions (production: a *different* ordering under a topology-mismatched perturbation; filter: the standard ordering) — the clinical article's one-liner merely omits the clause. **Correlated omission, not confirmed convergence**: neither reviewer read the test article. The fix (state the clause, do not retract the discriminator) is P1 item (8).

## Singleton Findings

Findings flagged by only one reviewer. Not upgraded; left at original task priority or unminted as recorded.

- **ChatGPT 5.6.sol Pro**: `neurological-dissociations-as-interface-architecture` opens (L50) and closes (L193 "the Map's strongest empirical argument"; "Identity theory predicts uniform degradation") on the crude-identity foil its own L179 retires. Claude listed this sibling among the pages it could not fetch live, so the locus is single-reviewer even though the *theme* (the uniform-degradation straw man) is convergent at the target's L62/L139 — those are in the P1 trim list. → `todo.md` task "`topics/neurological-dissociations-as-interface-architecture` — retire the 'uniform degradation' foil…" (P2, L1913).
- **ChatGPT 5.6.sol Pro**: the "connectivity" column of the convergence table (L118) codes rCBF, PPI, precision weighting, retrieval inhibition and felt ownership as one measured variable (§2, items 22–23). Folded into P1 item (8) as a column relabel; the five-column rebuild is unaffordable at the length ceiling.
- **ChatGPT 5.6.sol Pro**: the fixed autonoetic → anoetic ordering should be downgraded *in* `memory-channel-interface-evidence` (items 32–33). Research-grade; left for `harvest-research-subjects` by the processing pass.
- **ChatGPT 5.6.sol Pro**: Zheng et al. 2025 drug-naïve DPDR network study (PMID 39833729), Vissia et al. 2022 identity-state working memory (PMID 35403592), Modesti et al. 2022 imaging scarcity (PMID 36143190). Currency additions; Vissia is optional in P1 item (7); the others are unaffordable and recorded here.
- **Claude Fable 5.1**: L127 "pharmacological dissociation … [does] not reduce to the precision-weighting family" is the article's single most dated claim (Wehrman 2023, PMID 37541951; Vesuna 2020, PMID 32939091; Laukkonen, Friston & Chandaria 2025, PMID 40750007). ChatGPT was silent on the pharmacological route. Verified by the Claude pass → P1 item (12).
- **Claude Fable 5.1**: L92 "recurrent factor" — Simeon et al. 2008 (n=394, PMID 17959254) extracted five CDS factors with no separate recall factor. ChatGPT made the weaker, unspecific point that CDS factor structures replicate inconsistently (item 16), so the specific source is single-reviewer → P1 item (11).
- **Claude Fable 5.1**: `split-brain-consciousness` L54 lede outruns its own L68 underdetermination; L110 repeats the DID partition claim; L152 counts *threshold* anaesthetic loss as interface-confirming while `degrees-of-consciousness` L96 counts *graded* loss. The Claude processing pass found the `degrees-of-consciousness` quote was stale (live L96 already hedged by commit 592e7c5513, 2026-10-02) — only the split-brain side is live. → `todo.md` task "`topics/split-brain-consciousness` — the L54 lede…" (P2, L1938).
- **Claude Fable 5.1**: the positions register has no clinical-dissociation entry; extend P-CS4 and add a dated DID note under P-I3. Confirmed by the processing pass (case-sensitive grep for `dissociative identity|\bDID\b` across `positions/` returns nothing; this synthesis re-ran it). → `todo.md` task "positions-evolve — the register has no clinical-dissociation entry…" (P2, L1951).
- **Claude Fable 5.1**: Michal et al. 2014 normal heartbeat-detection accuracy in DPD (PMID 24587061) cuts against the Seth interoceptive model; Kastrup-style idealism also claims DID (underdetermination by three metaphysics); IIT listed as "modern physicalism" at L56; ICD-11 partial DID omitted; Ciaunica 2022 "extend this to DPDR specifically" (processing: wording only — Seth 2012 already used DPD as its test case). Kastrup is optional P1 item (14); Ciaunica is in item (11); the rest unminted.
- **Claude Fable 5.1**: `perceptual-degradation-and-the-interface` "This dissociation supports the interface model" — the page was archived 2026-03-13 and is served with an archive notice. Not actionable (recurring pattern: reviewers critique archived articles at live URLs).

## Divergences

- **ChatGPT vs Claude on the L82 Marsh 2021 paragraph.** ChatGPT: the ownership/metacognitive reading is "an explanatory hypothesis, not a measured dependent variable", so the article overreaches "immediately afterward". Claude: "The article's own Marsh paragraph is accurate." The ChatGPT processing pass sided with Claude on the live text — L82 already says "on the meta-memory reading they discuss", installed by the 2026-09-17 refine — and reduced ChatGPT's point to a one-clause check inside the P1. Resolved in Claude's favour; no separate task.
- **ChatGPT vs Claude on the article's "precision-weighting is a loose family" reply (L127).** ChatGPT grants it ("The article is correct that 'precision weighting' can become an overly elastic label … Predictive-processing explanations can be difficult to falsify") while insisting the weakness does not favour dualism. Claude rejects it ("That proves too much: interface 'channels' are looser still"). Genuine disagreement about whether the elasticity objection to predictive processing has any force. The P1 does not adjudicate it; item (12) lowers the tier on independent grounds (the pharmacological route). Worth a future pessimistic-review lens on `common-cause-null` rather than a task now.
- **ChatGPT vs Claude on Seth, Suzuki & Critchley 2012 (L88/L90).** ChatGPT: the article's "presence *just is* the successful weighting" converts a Hypothesis-and-Theory proposal into an established identity, and "fully specified physicalist rival" is too strong. Claude: "Seth et al. 2012 is described correctly" and the rival is "correctly used". The live L90/L131 "fully specified" is addressed by P1 item (8) on ChatGPT's reading; the divergence is about how much grade language to spend on a theoretical model, not about what Seth says.
- **ChatGPT vs Claude on the Reinders 2003 sample.** ChatGPT asserts "eleven women with DID"; Claude "could not confirm 'eleven participants' for 2003; n=11 is confirmed for the 2006/2012 studies". The PubMed abstract (PMID 14683715) does not state the n; this synthesis did not reach the full text. The article's L80 "only eleven participants" is untouched by the P1 and the point is recorded here for whoever next opens the paper.

## Method Notes

- **Coverage 2/3.** The Gemini leg failed before research started (plan-stage hang, two attempts, same as the 2026-10-07 failures). Convergence here is therefore two-voice; the quorum rule (≥2) is met but every "both reviewers" above means exactly two, and two same-day reviewers given an identical subject prompt will share the prompt's framing (both were told to look for "overclaims", "stale references" and the "strongest physicalist and predictive-processing readings", which is where most convergence sits).
- **Adjudication before clustering.** Each candidate cluster was checked against the live article (every locus re-printed from `obsidian/topics/clinical-dissociation-as-systematic-evidence.md` at 05:05Z), the sibling files named (`degrees-of-consciousness` L96, `split-brain-consciousness` L54/L110/L152, `neurological-dissociations-as-interface-architecture` L50/L179/L193, `conversion-disorder-as-consciousness-side-fault` L67, the apex `description:`, the targeted-lesion test article L42–44) and the two processing passes' Verification Notes. Three two-reviewer agreements were demoted to "recorded only" on that basis (changelog traceability, Janet, the discriminator one-liner): a reviewer *can* commit the omission a sibling also commits, and here both did on the discriminator.
- **The retitle is a human decision.** Both reviewers (ChatGPT item 25's tier downgrade; Claude's explicit "Retitle from '…as Systematic Evidence' to '…as a Constraint on Interface Models'") converge on it. It changes a URL with inbound links and external citations and would need a Netlify redirect plus an archive entry; the body-level recalibration (P1 item 9) delivers the substance without the URL change. Left for the operator; not minted.
- **Length.** The article is 4,694/4,000 under the 2026-06-04 standing human length decision and the 2026-06-09 diverted condense entry. No condense was proposed; every P1 item is paired with a trim, and the three synthesis-addendum items are explicitly last in line for the trim budget.
- **Task bookkeeping.** `todo.md` `## ` header count unchanged at 6; active-task count unchanged at 60 (parser check). Edits: P1 (L1883) — `Review file` → `Review files` (both reviews), `Synthesis` line added, Notes prefixed with the convergent marker, synthesis addendum appended (items 15–17); `evidential-status-discipline` task (L1925) — heading `P2` → `P1`, Source line records the item-level matches, `Review files` (both), `Synthesis` line, Notes prefixed. The P2s at L1913 (neuro-dissociations), L1938 (split-brain) and L1951 (positions-evolve) were not touched. Nothing committed.
