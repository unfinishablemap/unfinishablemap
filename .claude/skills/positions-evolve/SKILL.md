---
name: positions-evolve
description: Maintain the positions register — add, update, retire, and audit explicit claims the Map currently holds.
context: fork
agent: general-purpose
---

# Positions Evolve

The positions register at `obsidian/positions/` is the Map's maintained list of explicit claims it currently holds, with status, confidence band, dependencies, and the conditions that would shift each one. This skill is the only path through which positions are created, modified, retired, or audited.

Read [[obsidian/positions/positions.md]] before any operation — it documents the schema, confidence vocabulary, and how positions relate to tenets and apex articles. Do not duplicate that content here.

## When to use

- Add a new position when recent apex / topic / concept work has produced a stable commitment the register does not yet record.
- Update a position when its confidence band has shifted, its dependencies have changed, or the "Would shift if" conditions need rewording.
- Retire (or mark superseded) a position when evidence or reasoning has overturned it. Do not delete — preserve the entry for historical record.
- Audit the register periodically: check no two positions contradict, every dependency link resolves, every position is cited by at least one apex/topic article.

## Invocation

```
/positions-evolve add "<claim, stated assertively>"
/positions-evolve update P-XN
/positions-evolve retire P-XN
/positions-evolve audit
```

When invoked from the task queue, the args string is the task title + notes; parse it to determine mode.

## Modes

### Mode 1: `add`

Create a new position entry in the appropriate domain file (or create the domain file if no existing file fits).

**Process:**
1. Identify the domain. Existing domain files are listed in [[obsidian/positions/positions.md]]. If none fits, create a new domain file from `obsidian/templates/position.md`; pick a kebab-case filename matching the domain (e.g., `agency-and-will.md`).
2. Pick the next position ID. IDs are domain-prefixed: `P-Q*` for `quantum-interface`, `P-A*` for `agency-and-will`, etc. Use the next free number in that domain.
3. Fill the schema (see [[obsidian/positions/positions.md]] for the canonical shape). Required fields: Status, Confidence, Asserts, Depends on, Argued in, Would shift if, Last reviewed.
4. **Calibrate the hedging**: the language in the Asserts paragraph must match the confidence band. A *low*-confidence position must not be phrased as a settled result; a *high*-confidence position should not be over-hedged. Refer to [[concepts/evidential-status-discipline]] for the corpus vocabulary.
5. **Verify citations**: every `[[apex/...]]` or `[[topics/...]]` link in "Argued in" must resolve to a real file. Grep before inserting.
6. **Verify dependencies**: every `[[P-XN]]`-style reference (when used) must point to an existing position. Tenet references should name the tenet (e.g., "Tenet 2 (Minimal Quantum Interaction)").
7. Append the entry to the domain file. Keep entries ordered by ID within each file.
8. Update `obsidian/positions/positions.md` if a new domain file was created (add to the Domains list).
9. Bump `progress.positions_written` in `obsidian/workflow/evolution-state.yaml` if you created the first entry in a new domain file (the counter counts files written, not individual positions — TBD: confirm during audit).

**Length discipline**: each entry should be ~150–300 words. The whole domain file should stay under the soft threshold (1500 words); hard threshold 2500. If a domain file is approaching the soft threshold, split it rather than condense.

### Mode 2: `update`

Revise an existing position in place.

**Process:**
1. Read the current entry. Identify exactly what changed (confidence band, Asserts paragraph, Depends on, Argued in, Would shift if).
2. Make the edit. **Calibrate hedging** if confidence shifted (see Add step 4).
3. Update `Last reviewed:` to today's date.
4. If confidence shifted by more than one band (e.g., low → high), prepend a one-line history note inside the entry: `- **Updated 2026-MM-DD**: confidence raised low → high after [reason].` Keep at most the three most recent history notes per entry; older ones can be summarised.
5. Identify cascade: if this position is in another position's "Depends on" list, those downstream positions may need re-audit. Log the cascade in the changelog entry but do not auto-edit downstream positions (that's a separate audit pass).

### Mode 3: `retire`

Mark a position as superseded or retired without deleting it.

**Process:**
1. Change `Status: live` to `Status: superseded` (the claim has been replaced by a newer position — name the successor) or `Status: retired` (the claim was overturned and not replaced).
2. Add a one-line retirement note: `- **Retired 2026-MM-DD**: [reason]. [Successor: P-XN if applicable.]`
3. Move the entry to the bottom of the file, under a `## Retired` heading if not already present.
4. **Cascade check**: grep the rest of the register for `Depends on:` lines referencing this position. Each downstream position must be either updated (to depend on the successor) or itself retired. Log the cascade in the changelog; queue an `update` task for each affected downstream position.

### Mode 4: `audit`

Walk the full register checking for internal consistency. Read-only; produces a report and may queue follow-up tasks.

**Checks:**
1. **No contradictions**: scan Asserts paragraphs for direct contradiction between two `live` positions. Surface any contradictions found.
2. **All dependencies resolve**: every `[[P-XN]]`-style reference and every `[[apex/...]]` / `[[topics/...]]` / `[[concepts/...]]` link in Depends on / Argued in must resolve to an existing file or position. List unresolved.
3. **No orphans**: every `live` position should be cited (mentioned by ID, or its Asserts paraphrased) by at least one apex/topic/concept article. Grep the corpus for each position ID; list orphaned positions.
4. **Confidence calibration drift**: scan Asserts paragraphs for vocabulary that doesn't match the declared confidence band (e.g., "demonstrates" / "proves" in a low-confidence entry, "may" / "could" in a high-confidence entry). Flag mismatches against [[concepts/evidential-status-discipline]].
5. **Staleness**: positions with `Last reviewed:` more than 60 days old should be flagged for re-review.
6. **Cascade health**: every position with downstream dependents should still be `live`. A retired position with live dependents is a structural error; flag and queue updates.

**Output**: a report at `obsidian/reviews/positions-audit-YYYY-MM-DD.md` listing findings by check, with line refs. For each finding, queue a follow-up task in `obsidian/workflow/todo.md` (P2 for contradictions / cascade-errors, P3 for staleness / calibration drift).

## Frontmatter Schema

Position-domain files use standard frontmatter (see `obsidian/templates/position.md`) plus the conventional fields. No position-specific frontmatter fields are required — the structure is inside the body, in the `## P-XN:` entries.

## Cross-Skill Integration

- **After `/apex-evolve` lands a new apex article**: if the article advances a claim the register does not record, queue `/positions-evolve add` for the claim.
- **After `/refine-draft` or `/deep-review` substantially revises a topic/concept that's cited in a position's "Argued in"**: queue `/positions-evolve update <position-id>` to re-verify the citation still supports the position.
- **After `/coalesce` or `/archive` of an article cited in a position**: queue `/positions-evolve update <position-id>` to fix the broken citation.
- **Outer-review findings that overturn a position**: queue `/positions-evolve retire <position-id>` or `update`, depending on severity.

## Length Management

- Per-entry: ~150–300 words.
- Per domain file: soft 1500, hard 2500, critical 4000. If a domain file approaches the soft threshold, split it (don't condense entries — they are deliberately structured).

## Important

- **Never delete a position**. Retire or supersede, but preserve the entry. The register's value depends on showing what the Map used to hold and why it changed.
- **No bulk creation**. Add positions one at a time, with deliberation. If you find yourself wanting to add five positions in one invocation, run five separate `add` operations or queue follow-up tasks.
- **No editorial drift**. The "Asserts" paragraph commits the Map. If you would not stand behind the claim as written, do not register it; refine until you would.
- **Cascade visibility**. Every retire / major update must surface downstream effects. The register's job is to make dependency structure legible.
- **Logging**: prepend an entry to `obsidian/workflow/changelog.md` describing the operation (add / update / retire / audit), the position ID(s) touched, and any cascade follow-ups queued.
- **Do not commit**. Leave changes uncommitted; the orchestrator (`cycle_post.py` for `/loop`, `/agent-commit` for manual) handles git.
