---
title: Tenet Alignment Check - 2026-03-22
created: 2026-03-22
draft: false
ai_contribution: 100
ai_system: claude-opus-4-6
---

# Tenet Alignment Check

**Date**: 2026-03-22
**Files checked**: 447
**Errors**: 0
**Warnings**: 1
**Notes**: 2

## Summary

Comprehensive scan of all 228 topic files and 219 concept files against the five foundational tenets. The corpus is exceptionally well-aligned. Every article includes explicit "Relation to Site Perspective" sections connecting content to the tenets. Opposing views (materialism, epiphenomenalism, MWI, functionalism, illusionism, Russellian monism) are consistently discussed to argue against them, not endorsed.

One warning-level issue persists where epiphenomenal upload-consciousness is presented as a live open possibility rather than a tenet-excluded position. Two note-level issues involve a broken tenet wikilink anchor and insufficient disambiguation of Koch's framework relative to bidirectional interaction.

Additionally, one non-tenet citation discrepancy was observed: `consciousness-in-simple-organisms.md` attributes a logical reasoning study to "Lieberman, M. D., et al. (2008)" while `consciousness-and-intelligence.md` attributes the same study to DeWall, Baumeister & Masicampo (2008).

## Warnings

### machine-consciousness.md
- **Tenet potentially violated**: Bidirectional Interaction (Tenet 3)
- **Issue**: The "Open Possibilities" section presents "One-Way Consciousness" (epiphenomenal AI consciousness) as a live, genuinely open possibility without sufficiently ruling it out.
- **Quote**: "The upload would be conscious but causally impotent: experiencing its computations without biasing them. This would undermine the Bidirectional Interaction tenet's relevance to uploading, since consciousness could ride along on classical computation even without the quantum interface the Map normally requires."
- **Recommendation**: Reframe to note that if upload consciousness exists, Tenet 3 predicts it is causally efficacious. The "one-way" scenario is not an open possibility the Map entertains but a prediction failure — present it as such.

## Notes

### consciousness-and-the-philosophy-of-biology.md
- **Tenet**: Minimal Quantum Interaction (Tenet 2)
- **Issue**: Broken tenet wikilink anchor — uses `[[tenets#^minimal-interaction]]` instead of the correct `[[tenets#^minimal-quantum-interaction]]`. The link will fail to resolve. Not a content violation but should be fixed.
- **Recommendation**: Update the anchor to `[[tenets#^minimal-quantum-interaction]]`.

### consciousness-in-smeared-quantum-states.md
- **Tenet**: Minimal Quantum Interaction / Bidirectional Interaction (Tenets 2 & 3)
- **Issue**: Koch's framework (consciousness arises at superposition formation, not at collapse) is presented in a comparative, neutral manner without explicitly identifying it as incompatible with the Map's tenets. The conclusion disfavors it but a reader could interpret the article as treating Koch as a viable alternative.
- **Quote**: "Koch and collaborators [...] propose the opposite of Penrose: conscious experience arises precisely when superposition *forms*, not when it collapses."
- **Recommendation**: Add a brief note in the Koch section that this framework conflicts with Tenet 3 (Bidirectional Interaction) since it renders consciousness epiphenomenal with respect to quantum outcomes.

## Non-Tenet Issues

### Citation discrepancy
- **File**: `consciousness-in-simple-organisms.md`
- **Issue**: Cites "Lieberman, M. D., et al. (2008)" for the logical reasoning / cognitive load study. Other articles (e.g., `consciousness-and-intelligence.md`) attribute the same study to DeWall, Baumeister & Masicampo (2008). One of these citations is incorrect.

## Files Passing All Checks

All 447 files pass tenet alignment checks except the 3 listed above (1 warning, 2 notes). The remaining 444 files show no errors, warnings, or notes regarding tenet alignment.
