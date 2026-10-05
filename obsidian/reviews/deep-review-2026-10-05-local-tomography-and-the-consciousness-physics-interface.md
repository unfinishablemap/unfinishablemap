---
title: "Deep Review - Local Tomography and the Consciousness-Physics Interface"
created: 2026-10-05
modified: 2026-10-05
human_modified:
ai_modified: 2026-10-05T14:07:14+00:00
draft: false
description: "Third deep review: grep-verifies every quotation added since 2026-08-18 in the raw source PDFs and corrects a reversed claim about quaternionic quantum theory that two prior reviews passed."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-05
last_curated:
---

**Date**: 2026-10-05
**Article**: [[concepts/local-tomography-and-the-consciousness-physics-interface|Local Tomography and the Consciousness-Physics Interface]]
**Previous review**: [[reviews/deep-review-2026-08-18-local-tomography-and-the-consciousness-physics-interface|2026-08-18]]

## Scope

Three refine-draft commits landed since the 2026-08-18 review (`de68d9bf50` class premise and boxworld; `a66b293718` Further Reading link; `567c8ac7bd` the Hoffreumon-Woods dispute rewrite). They added five quotations and three references. This pass verified all of those against the raw full texts (arXiv PDFs converted with `pdftotext` and grepped), and re-read the older sections against the full texts where the earlier reviews had only checked abstracts.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Reversed claim about quaternionic quantum theory (factual error; present since creation, passed by both prior reviews).** `## What Failure Looks Like` said that for quaternionic theory "Global degrees of freedom are then unavoidable by construction." The sources say the reverse. Barnum and Wilce (footnote 2): the candidate quaternionic composite "suffers from difficulties in even identifying the product effects necessary to a locally tomographic composite—indeed, its dimension is smaller than the product". Hardy (2001, quant-ph/0101012): quaternionic composites "would have to have less degrees of freedom than the product of the number of degrees of freedom associated with the subsystems", against real composites which "have more". A composite with too few parameters has no surplus global degrees of freedom. **Resolution**: sentence replaced with "Its composite has *fewer* parameters than the product of its parts', so what fails there is the product structure itself, with no surplus of global degrees of freedom." The section's opening generalisation ("When local tomography fails, a composite has a global degree of freedom") was scoped to failure "by excess" so the section no longer contradicts itself.
- **Misdescribed Barnum-Wilce (attribution).** The parenthetical said quaternionic failure "follows as a consequence of the uniqueness result rather than as a separate Barnum-Wilce assertion." Barnum and Wilce do remark on it separately, in footnote 2, crediting earlier work. **Resolution**: now "the quaternionic difficulty appears only in a footnote crediting earlier work."
- **"Limited holism" mis-scoped (attribution, minor).** The article said Hardy and Wootters "name this residual 'limited holism'", the residual being real quantum theory's surplus over complex. In the paper the phrase names holism that is *bounded* by an n-local tomography principle, and they apply it to complex quantum theory first ("In this respect the holism of quantum theory is limited"; "other principles, not as limiting as local tomography, that also give rise to a kind of limited holism"). **Resolution**: "Hardy and Wootters call holism bounded in this way 'limited holism'". The signature reading's later use of the vocabulary is unaffected.

### Publisher-of-Record Citation Ledger

Metadata from the arXiv API and Crossref REST; quotations grepped in the raw PDF text.

- Hardy & Wootters (2012), *Limited Holism and Real-Vector-Space Quantum Theory*, Found. Phys. 42, 454-473 — real-correct. Both quotations verbatim in the abstract. Result-direction: real theory is not locally but is bilocally tomographic, as stated. "Limited holism" scope corrected (above).
- Barnum & Wilce (2014), *Local Tomography and the Jordan Structure of Quantum Theory*, Found. Phys. 44, 192-212 — real-correct. Quotation verbatim in the abstract; conditions (Jordan-algebraic systems, locally tomographic composites, one qubit) match. Description of the quaternionic remark corrected (above).
- Renou et al. (2021), Nature 600, 625-629 — real-correct (eight authors in order, journal-ref and DOI on the arXiv record). "real and complex quantum theory make different predictions in network scenarios comprising independent states and measurements" verbatim in the abstract. New since last review: "plausible, yet unverifiable, assumptions about the form of the quantum states" verbatim in the body ("we are thus compelled to accept some plausible, yet unverifiable, assumptions about the form of the quantum states distributed to the three parties"). The article's "had themselves conceded" is a fair report.
- Chen et al. (2022), PRL 128, 040403; Li et al. (2022), PRL 128, 040402 — real-correct per the 2026-08-18 Crossref check; unchanged, not re-fetched.
- Hoffreumon & Woods (2026), arXiv:2603.19208 — real-correct; still v1 with no journal-ref, so "preprint, not peer-reviewed" stands. "the absence of observable cross-source correlations" verbatim. "indistinguishable for all finite network experiments" matches "every finite network correlation achievable in QT is also achievable in RQT".
- Moradi Kalarde, Xu & Renou (2026), arXiv:2604.07425 — real-correct (three authors, title exact, no journal-ref). The article's two claims are both in the paper: Appendix C is headed "Postulate 1 is equivalent to local tomography" and proves it within GPTs (Props. 1 and 2); the abstract states the postulate "fails in FIT".
- Barrios Hita, Trushechkin, Kampermann, Epping & Bruß (2026), PRL 136, 240202, doi:10.1103/4k13-sdjh — real-correct (Crossref: title, five authors, volume, article number, issued 2026-06-18). "Reproduces every complex prediction" matches "reproduces predictions for all multipartite quantum experiments"; "what stands falsified is real quantum theory with the tensor-product composition rule" matches the body ("the models ... which use the tensor product postulate for composite systems").
- Galley & Masanes (2018), Quantum 2, 104 — real-correct. New since last review, both verbatim in the body: "all theories that have the same pure states, dynamics and system-composition rule as quantum theory, but have a different structure of measurements and a different rule for assigning probabilities" (§2, Dynamically-quantum theories) and "from the structure of pure states and dynamics and either the assumption of local tomography or purification". The second confirms at source the disjunctive antecedent the 2026-08-18 review derived by contraposition. Stance: the authors are not presented as endorsing anything about a consciousness interface; the section opens by marking everything after it as the Map's reading.
- Barrett (2007), Phys. Rev. A 75, 032304 — real-correct (Crossref: single author, issued 2007-03-05). Global State Assumption quotation verbatim (Assumption 5). Barrett adds that the assumption "need not be satisfied" over a real Hilbert space, consistent with the article.
- Refs 8 and 9 are Map self-citations; left as they are.

Inline ↔ References: no orphan in either direction, keyed on (surname, year). The superlative helper returned nothing.

### Medium Issues Found

- The article glosses the Galley-Masanes class as "quantum state space and reversible dynamics" in several places, while the definition it quotes also fixes the system-composition rule. The full quotation is in the text, so nothing is misstated; left alone under length pressure.

### Counterarguments Considered

- Quantum sceptic: a "non-physical substrate" with a state space is undefined, so asking whether (B + S) is locally tomographic is empty. The article already says there is "no theory of what S's state space is" and claims only to locate the open question. Framework-boundary disagreement.
- Empiricist: nothing here is testable. The article says so in its lead and its closing paragraph.

### Reasoning modes (editor record)

No named-opponent reply in this article; the real-versus-complex dispute is reported at source with no side taken.

## Optimistic Analysis Summary

### Strengths Preserved

- The single-door-two-locks figure and the passage where the same arithmetic "softens the problem reading [and] sharpens this one".
- The boxworld limiting case doing double duty in the axiom section and the interface section.
- The dispute paragraph, which now reports Renou's own concession, the Hoffreumon-Woods construction, the fermionic reply and the peer-reviewed reformulation without calling a winner.
- Evidential restraint: "The axiom does no work *for* the interface reading over its rivals."

### Enhancements Made

- None beyond the corrections. The article is over its soft threshold and its argument is complete.

### Cross-links Added

- None.

## Length

3001 → 3006 words (concepts soft 2500, hard 3500; `soft_warning`). Length-neutral: the three corrections were offset by tightening the "lesson" paragraph. No qualifier removed.

## Remaining Items

- The `d` overload noted on 2026-08-18 is still there; still a clarity matter only.
- The source research note (`research/local-tomography-and-the-consciousness-physics-interface-2026-07-16`) attributes quaternionic failure to "Barnum-Wilce 2014" and applies "limited holism" to real theory specifically. Both are loose and neither is false in the way the article sentence was; not edited.

## Stability Notes

- The 2026-08-18 notes stand: no mechanism-debt citation on this file; do not strengthen the signature reading; do not call the real-versus-complex dispute.
- A physicalist will say a physical/non-physical composite is not a well-posed object. That is the tenet boundary, and the article does not pretend otherwise.
- Prior ledgers certified the quoted abstracts and missed an unquoted, uncited sentence two paragraphs away. Unquoted technical claims between the quotations are where the next defect in this cluster is most likely to be.
