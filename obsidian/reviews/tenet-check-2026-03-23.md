---
title: Tenet Alignment Check - 2026-03-23
created: 2026-03-23
draft: false
ai_contribution: 100
ai_system: claude-opus-4-6
---

# Tenet Alignment Check

**Date**: 2026-03-23
**Files checked**: 452
**Errors**: 0
**Warnings**: 3
**Notes**: 15

## Summary

Comprehensive scan of all 229 topic files and 223 concept files against the five foundational tenets. The corpus remains well-aligned overall. Every article includes explicit "Relation to Site Perspective" sections. Opposing views (materialism, epiphenomenalism, MWI, functionalism, illusionism, Russellian monism) are consistently discussed critically, not endorsed.

Three warning-level issues were found where rival frameworks are presented with insufficient re-anchoring to the Map's position. Fifteen note-level items identify minor tensions, broken tenet anchors, and places where framing could be tightened. No errors (direct contradictions) were found.

The recurring machine-consciousness.md warning from prior checks persists. Two new warnings were identified in concepts (integrated-information-theory.md, predictive-processing.md).

## Warnings

### machine-consciousness.md
- **Tenet potentially violated**: Bidirectional Interaction (Tenet 3)
- **Issue**: The "Open Possibilities" section presents "One-Way Consciousness" (epiphenomenal upload consciousness) as a live possibility without sufficiently ruling it out under Tenet 3.
- **Quote**: "The upload would be conscious but causally impotent... This would undermine the Bidirectional Interaction tenet's relevance to uploading."
- **Recommendation**: Reframe to note that if upload consciousness exists, Tenet 3 predicts it is causally efficacious. Present "one-way consciousness" as a rival prediction, not an open possibility the Map entertains.
- **Status**: Persists from prior check (2026-03-22).

### integrated-information-theory.md
- **Tenet potentially violated**: Bidirectional Interaction (Tenet 3)
- **Issue**: Sustained technical exposition of IIT's identity claim (phi = consciousness) without periodic re-anchoring to the Map's position. The article does contain correct disclaimers about conflict with Tenet 3, but the extended sympathetic treatment could leave an LLM reader uncertain whether IIT's identity claim is endorsed.
- **Recommendation**: Add brief re-anchoring statements within the technical exposition sections to clarify the Map treats IIT as a rival framework, not a compatible one.

### predictive-processing.md
- **Tenet potentially violated**: Bidirectional Interaction (Tenet 3)
- **Issue**: The "Deep Self-Models" section uses phrases like "phenomenal consciousness might emerge from subjective valuation" and describes Solms' claim that "free energy minimization might explain why uncertainty feels like something" without framing these as PP's claims under critique. Given the Map's stance that consciousness does not emerge from physical processes, this language needs clearer attribution.
- **Recommendation**: Reframe the "might emerge" and "might explain" formulations to explicitly attribute them to PP/Solms as claims being examined, not as positions the Map holds open.

## Notes

### Broken Tenet Anchors (4 files)

| File | Anchor used | Correct anchor |
|------|-------------|----------------|
| `consciousness-and-the-philosophy-of-biology.md` | `[[tenets#^minimal-interaction]]` | `[[tenets#^minimal-quantum-interaction]]` |
| `consciousness-and-the-problem-of-measurement-standards.md` | `[[tenets#^bidirectional]]` | `[[tenets#^bidirectional-interaction]]` |
| `animal-consciousness.md` | `[[tenets#^occams-razor]]` | `[[tenets#^occams-limits]]` |
| `phenomenal-normativity-environmental-ethics.md` | `[[tenets#^minimal-interaction]]` | `[[tenets#^minimal-quantum-interaction]]` |

These are link-precision issues only — prose content correctly describes the relevant tenets.

### william-james-consciousness.md
- **Tenet**: Dualism (Tenet 1)
- **Issue**: Presents James's "radical empiricism" and "pure experience" neutral monism framework sympathetically without clearly distinguishing the Map's interactionist dualism from James's neutral monism. The statement that James "refused both crude materialism and crude dualism" could suggest a middle path the Map might endorse.
- **Recommendation**: Add a sentence in the body clarifying where the Map departs from James's metaphysics, noting that while the Map draws on filter theory and attention-as-interface concepts, it does not adopt neutral monism.

### mysterianism.md
- **Tenet**: Dualism (Tenet 1)
- **Issue**: Strongly endorses McGinn's cognitive closure thesis without clarifying that McGinn himself is a physicalist who thinks the unknown property P is physical. The article's heavy reliance on McGinn without distinguishing the Map's selective adoption could imply the Map is agnostic about dualism itself.
- **Recommendation**: Add a note that the Map adopts mysterianism's limits thesis while rejecting McGinn's physicalist assumption about property P.

### philosophy-of-time.md
- **Tenet**: No Many Worlds (Tenet 4)
- **Issue**: Discusses MWI and various QM interpretations as live options when analyzing temporal implications without noting that Tenet 4 rules out MWI.
- **Recommendation**: Include a brief note that the Map's No Many Worlds tenet constrains which QM interpretations are acceptable.

### panpsychism.md
- **Tenet**: Minimal Quantum Interaction (Tenet 2)
- **Issue**: Notes panpsychism solves the prebiotic collapse problem because proto-conscious properties were present from the beginning, without cross-referencing the Map's own resolution (objective reduction with consciousness modulation).
- **Recommendation**: Add cross-reference to `prebiotic-collapse.md` for the Map's preferred solution.

### process-philosophy.md / prehension.md
- **Tenet**: Dualism (Tenet 1)
- **Issue**: Whitehead's panpsychist framework treated sympathetically as a resource without always clearly maintaining the distinction between selective borrowing and full endorsement.
- **Recommendation**: Clarify that the Map uses process philosophy's anti-emergence insight and temporal concepts but rejects pan-experiential ontology.

### functionalism.md
- **Tenet**: Dualism (Tenet 1)
- **Issue**: Treatment of Map/IIT agreement on rejecting functionalism could blur the Map's dualist distinctiveness, since IIT rejects functionalism because substrate matters physically while the Map rejects it because consciousness is non-physical.
- **Recommendation**: Add a sentence distinguishing the two different reasons for rejecting functionalism.

### global-workspace-theory.md
- **Tenet**: Bidirectional Interaction (Tenet 3)
- **Issue**: The question "whether functional implementation suffices for experience" is presented as open without the Map's clear answer.
- **Recommendation**: Add a brief affirmative statement that functional implementation does not suffice for experience under the Map's framework.

### near-death-experiences.md
- **Tenet**: Minimal Quantum Interaction (Tenet 2)
- **Issue**: Discusses consciousness persisting through brain compromise without connecting to the Minimal Quantum Interaction constraint.
- **Recommendation**: Note that any post-death consciousness would need to remain consistent with the minimal interaction framework.

### idealism.md
- **Tenet**: Bidirectional Interaction (Tenet 3)
- **Issue**: Phrases like "this is a wager, not a proof" could undermine the commitment status of Tenet 3.
- **Recommendation**: Strengthen language to distinguish between acknowledging philosophical difficulty and questioning the tenet itself.

### parfit-reductionism.md
- **Tenet**: No Many Worlds (Tenet 4)
- **Issue**: Parfit's branching scenarios reconstructed positively as thought experiments without always clearly marking these as positions being critiqued.
- **Recommendation**: Foreground the Map's stake more strongly — identity matters non-reducibly under Tenet 4.

### llm-consciousness.md
- **Tenet**: Minimal Quantum Interaction (Tenet 2)
- **Issue**: Suggestion that quantum hardware might produce conscious AI could be read as endorsing empirically detectable mind-matter interactions.
- **Recommendation**: Clarify that such a system would still operate within the minimal interaction constraint.

## Non-Tenet Observations

### Stale AI refinement logs
Approximately 17 files across topics and concepts contain embedded `<!-- AI REFINEMENT LOG -->` HTML comments marked "should be removed after human review." These do not affect site rendering or tenet alignment but represent housekeeping debt.

### Inline human comment
`language-recursion-and-consciousness.md` contains an inline comment from the author: `[Andy: I've no idea how it came up with this]`. May want to be resolved before publication.

### Citation discrepancy (persists from prior check)
`consciousness-in-simple-organisms.md` attributes a logical reasoning / cognitive load study to "Lieberman, M. D., et al. (2008)" while other articles attribute the same study to DeWall, Baumeister & Masicampo (2008). One citation is incorrect.

## Files Passing All Checks

All 452 files pass tenet alignment checks except the 18 listed above (3 warnings, 15 notes). The remaining 434 files show no errors, warnings, or notes regarding tenet alignment.
