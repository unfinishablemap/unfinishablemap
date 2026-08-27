---
ai_contribution: 100
ai_generated_date: 2026-08-27
ai_modified: 2026-08-27 03:22:41+00:00
ai_system: claude-fable-5
author: null
concepts: []
created: 2026-08-27
date: &id001 2026-08-27
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-27 03:22:41+00:00
modified: *id001
related_articles: []
title: Deep Review - The Simulation Theory of Memory
topics: []
---

**Date**: 2026-08-27
**Article**: [The Simulation Theory of Memory](/concepts/simulation-theory-of-memory/)
**Previous review**: [2026-07-27](/reviews/deep-review-2026-07-27-simulation-theory-of-memory/)

Third deep review. The unreviewed surface since 2026-07-27 is exactly the 2026-08-04 refine-draft that added the "self-model reply" subsection (Metzinger 2003; Apps & Tsakiris 2014) as a sibling extension of the convergent 3/3 outer-review finding on `phenomenology-of-memory-and-the-self`. This pass web-verified the two new cites at the publisher, re-checked the whole References block against the prior ledgers rather than inheriting them, and read the new subsection against the article's own lead. Two defects found and fixed: one real-wrong-metadata cite that both prior ledgers had ratified, and one internal calibration tension the new subsection introduced.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Real-wrong-metadata cite — SEP "Memory" entry authorship.** The References block read `Michaelian, K., Robins, S. K., & Sant'Anna, A. (Eds.). Memory. *Stanford Encyclopedia of Philosophy*`. The live SEP citation-info page (`archinfo.cgi?entry=memory`, fetched raw) gives the author field as `Michaelian, Kourken and Sutton, John and Sant'Anna, André`; the entry was rewritten in 2017 by Michaelian & Sutton and Sant'Anna joined in a later revision. Sarah Robins is not an author of the entry, and SEP entries have authors, not editors — the "(Eds.)" form looks like a conflation with one of the Routledge memory collections. Both the 2026-06-24 and 2026-07-27 ledgers marked this cite "real-correct"; neither fetched the citation-info page. **Resolution**: corrected to `Michaelian, K., Sutton, J., & Sant'Anna, A. Memory. *Stanford Encyclopedia of Philosophy* (first published 2017; current revision).` Corpus grep: this form appears only in this article; no family propagation needed.

**2. Internal calibration tension introduced by the 08-04 addition (new content reintroducing a problem — issue-tracking rule 2).** The lead asserted that STM "cannot ground the feeling of remembering … nor explain how a subject tells a memory apart from a free imagining," and the Dualism tenet paragraph called the discrimination problem "the signature of that missing contribution." The new self-model subsection then conceded that a transparent self-model of oneself-as-past-subject is a candidate mechanism for exactly that discrimination, and the Map's reply retreated to "why is running it experienced at all." A tenet-accepting reviewer would flag the lead as overstated relative to the body: the residue the article can actually defend is the *felt character* of the discrimination, not the discrimination itself. This is calibration inside the framework, not bedrock disagreement. **Resolution**: (a) lead re-scoped — the feeling of remembering is that "by which a subject tells a memory apart," the self-model repair "offers a candidate mechanism for the discrimination but no account of why its verdicts are felt," and "that narrower gap" is where the Map locates the contribution; (b) the self-model subsection now states explicitly that the Map's reply "concedes the discrimination *mechanism* while contesting only its felt character — so the residue STM leaves is narrower than the section above first states"; (c) the Dualism paragraph's "signature" sentence is narrowed "to the question of why the discrimination is felt rather than merely computed." The sibling `phenomenology-of-memory-and-the-self` already carries this concession (its reply is labelled "the relocation move again" with a confidence downgrade), so the fix imports the cluster's existing calibration rather than deriving a new one.

### Medium Issues Found
- **Source/Map seam in the self-model subsection.** Neither Metzinger (2003) nor Apps & Tsakiris (2014) discusses remembering; the subsection's "On this reading the feeling of remembering is …" let the application read as if it were the sources' own claim. **Fixed**: now opens "Neither source addresses remembering directly; extended to memory, the account makes the feeling of remembering …".
- **Missing cross-link**: the sibling's parallel paragraph links [predictive-processing-and-dualism](/topics/predictive-processing-and-dualism/) as the wider programme; this article did not. **Added** in prose and in `related_articles`.

### Counterarguments Considered
- Possibility/probability slippage re-checked across the whole article: every interpretive move remains hedged ("on the Map's reading," "the Map's entry point, not a defect the Map manufactures"), the interface reading is still held separate from the reconsolidation signature, and the one overstatement found (item 2) has been corrected in the direction of *less* confidence. No slippage remains.
- Hard-Nosed Physicalist / Eliminativist: STM's naturalist proponents reject the irreducible-contribution conclusion — bedrock, unchanged from prior reviews, not re-flagged.

### Citation web-verify ledger (publisher of record)
New since the last ledger:
- Metzinger 2003 (*Being No One*, MIT Press) — real-correct (OpenAlex record; MIT Press catalogue URL is carried in [self-model-theory-of-subjectivity](/concepts/self-model-theory-of-subjectivity/)).
- Apps & Tsakiris 2014 (*Neurosci. Biobehav. Rev.* 41:85–97, DOI 10.1016/j.neubiorev.2013.01.029) — real-correct (Europe PMC + Crossref; print 2014, online 2013-02-15). The quoted `"me"` matches the abstract verbatim ("processed in a Bayesian manner as the most likely to be 'me'"); the article's "hypothesis" is a fair gloss, not inside the quote marks.
- SEP "Memory" — **real-wrong-metadata** (was Michaelian, Robins & Sant'Anna (Eds.); corrected to Michaelian, Sutton & Sant'Anna, authors). Still uncited inline; the 06-24 acceptance of it as bibliographic context stands.

Re-confirmed unchanged from the 2026-06-24 metadata ledger and 2026-07-27 quote-fidelity ledger (References block otherwise untouched since): Schacter & Addis 2007; Schacter, Addis & Buckner 2008; Addis et al. 2009; Hassabis et al. 2007 (verbatim "lacked spatial coherence" confirmed present in body); Martin & Deutscher 1966; Michaelian 2016 (MIT Press); Michaelian 2016 (Frontiers); Robins 2016; Rivadulla-Duró 2024; Michaelian 2022.

No superlative/empirical-record claims present (`find_superlative_claims` returned empty).

### Reasoning-mode classification (editor-internal)
- Engagement with STM/Michaelian's eliminative gloss: **Mode Two** — the discrimination problem is one the simulationist literature raises against itself. Unchanged.
- Engagement with the self-model rival (Metzinger / Apps & Tsakiris): **Mixed** — opens Mode Two (the account helps itself to the step from transparent modelling to felt experience), closes Mode Three (the Map's reply is itself the relocation move and does not defeat the account inside its framework; the honest residue is the narrowed gap, now stated as such). The 08-04 pass classified it the same way; this pass makes the Mode-Three concession visible in the article's lead rather than only in the subsection.
- Engagement with the parsimony defence: **Mode Two** — unchanged.
- No label leakage; grep for editor-vocabulary and the "This is not X. It is Y." construct returned nothing.

## Optimistic Analysis Summary

### Strengths Preserved
- "The Map's verdict is split, and the split is the point" — kept verbatim.
- Clean lineage exposition (Schacter/Addis neuroscience vs. Michaelian philosophy) and the causalist/confabulation section — untouched.
- Hardline Empiricist (Birch) counterweight: the article declines tenet-as-evidence-upgrade throughout, and this pass moved it further toward restraint rather than away.
- Strong inbound integration (7 sibling articles link in).

### Enhancements Made
- Lead now names the strongest physicalist repair up front (truncation resilience: an LLM reading only the first two paragraphs gets the rival and the narrowed residue).
- Self-model subsection now states what the Map's reply concedes, not only what it contests.

### Cross-links Added
- [predictive-processing-and-dualism](/topics/predictive-processing-and-dualism/)

## Remaining Items

None. Word count 1732 → 1822 (73% of the 2500 concepts soft target; headroom intact).

## Stability Notes

- STM's naturalist proponents (Michaelian, Schacter, Addis) reject the irreducible-contribution conclusion from outside the tenets — bedrock; do not re-flag.
- The self-model rival is *not* refuted here and the article does not claim it is: the Map's reply is the relocation move, and the residue is now honestly stated as "why the discrimination is felt" rather than "how the discrimination is done." Future passes should not re-widen the lead's claim back to "STM cannot explain how a subject tells memory from imagining" — that would reintroduce the tension fixed here.
- Lesson for future passes (compounding the 07-27 lesson): two prior ledgers marking a reference-work cite "real-correct" is not evidence anyone fetched its citation-info page. Reference works (SEP/IEP) need the archinfo/author page checked, not the entry landing page.