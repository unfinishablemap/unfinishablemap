---
name: compose-paper
description: Compose an academic preprint for SSRN and PhilArchive. Drafts locally in markdown, then writes to Google Docs via Chrome for final formatting and PDF export.
---

# Compose Paper

Draft and produce an academic preprint suitable for submission to SSRN and PhilArchive.

## When to Use

- When `/compose-paper [topic]` is invoked
- When the user wants to write a paper about the Map's methodology, architecture, or findings

## Directory Structure

Each paper lives in `papers/<slug>/`:

```
papers/<slug>/
├── outline.md          # Section outline with word count targets per section
├── draft.md            # Full markdown draft (primary working file)
├── figures/            # Diagrams and images (PNG/SVG, 300+ dpi)
├── references.md       # Categorised bibliography with relevance notes
└── notes.md            # Planning notes, core thesis, target audience, decisions log
```

Paper-related downloads (PDFs of referenced papers) go in `papers/downloads/` (gitignored). Committable metadata about each downloaded paper goes in `papers/manifests/`:

```
papers/downloads/           # Gitignored — actual PDFs
├── arxiv-2302.01339.pdf
└── ...
papers/manifests/           # Committed — metadata about each PDF
├── arxiv-2302.01339.md     # SHA-256, summary, relevance assessment
└── ...
```

This directory is outside `obsidian/` and `hugo/` — papers are not part of the site content pipeline.

## Writing Style

### Academic Register

Papers use a different voice from Map articles:

- **"We" is standard** in clearly authored working papers with named authors
- **Hedged claims.** "The results suggest..." not "This proves..."
- **No tenet advocacy.** Papers describe the Map's tenets as methodological choices, not truth claims
- **Define all jargon.** Assume the reader knows neither philosophy of mind nor Hugo/Obsidian
- **Avoid LLM clichés.** Same rules as Map content — no "This is not X. It is Y." constructs. Also avoid the "not merely X, but Y" escalation pattern, "This capability shift made a new kind of X possible," and similar formulaic phrasings that read as AI-generated
- **Avoid grandiosity and overclaiming.** Do not use phrasing like "fills this gap," "novel contribution," or "we introduce the concept of X" when a simpler statement works. Coined terms should appear sparingly (once or twice), not be repeated for emphasis. Let the work speak for itself rather than announcing its significance
- **No pretentious framing.** Prefer plain descriptions over dramatic ones. "The system reviews its output" not "the system attacks its own output indefinitely." Academic readers are put off by language that oversells
- **Use lists and bullet points.** Break up dense prose with structured lists where appropriate — enumerating components, steps, contributions, or design choices. This aids readability and scanning

### Formatting

- Single column, 11-12pt serif font (Times New Roman or similar)
- 1-inch margins, 1.5 line spacing
- Numbered sections (1, 1.1, 1.2, 2, ...)
- Figures/tables inline with numbered captions (Figure 1, Table 1)
- References at end, APA or similar consistent style

### Length

- Typical SSRN working paper: 4,000-7,000 words
- Strategy: draft ~20% long, then compact ruthlessly with hard caps per section
- Set explicit word count targets for each section in the outline

## Instructions

### 1. Plan the Paper

Create `papers/<slug>/notes.md` with:
- Working title (and alternatives in reserve)
- Core thesis in 2-3 sentences
- Key claims (numbered, testable)
- Target audience (primary and secondary)
- Target venue (SSRN networks, potential journals for later)
- What the paper is NOT (scope boundaries)
- Open questions for the writing process

Create `papers/<slug>/outline.md` with:
- Working title, authors, keywords
- Terminology definitions for any coined terms (with necessary-and-sufficient conditions, not just description)
- Draft abstract (~200 words)
- Section-by-section outline with word count targets (draft and final columns)
- Each section: bullet points describing key content, key citations, any user-provided data needed
- Figures table (number, description, type, notes)
- Key references list (most-cited in text)
- Explicit statement of what the paper claims (existence proof? methodological proposal? empirical study?)

Review outline with the user before proceeding to literature search.

### 2. Literature Search

Build `papers/<slug>/references.md`:
- Organise references by category (e.g., AI-Assisted Knowledge Production, Constitutional AI, etc.)
- Each entry: full citation, 2-3 sentence relevance note, download status
- Include a gap analysis at the end: what exists vs what doesn't (the paper's contribution)
- Number entries for easy cross-referencing (numbers need not be sequential across categories)

**Evaluating external reference suggestions:** When the user provides references from other AI systems (ChatGPT, Gemini, etc.), evaluate for relevance to the paper's specific angle — don't adopt conclusions, extract references. Apply consistent criteria: only add references directly relevant to the paper's contribution claim.

### 3. Download and Catalogue Papers

Download referenced papers to `papers/downloads/` (gitignored). For each downloaded paper, create a manifest in `papers/manifests/<filename>.md`:

```markdown
# [Paper Title]

## Bibliographic
- **Title:** [Full title]
- **Authors:** [All authors]
- **Date:** [Publication date]
- **Venue:** [Journal/conference/preprint server]
- **URL:** [Source URL]

## File
- **Local path:** papers/downloads/[filename].pdf
- **SHA-256:** [hash]
- **Size:** [bytes]
- **Downloaded:** [ISO date]

## Summary
[2-3 sentence summary from reading the paper]

## Relevance to Our Paper
[How this paper relates to our contribution. High/Medium/Low relevance rating.]

## Notes
[Any issues, wrong-paper downloads, missing sections, etc.]
```

Verify each downloaded paper is actually the correct paper by reading its first pages. Wrong-paper downloads from arXiv are not uncommon — check title and authors match.

### 4. Review the Outline

Before drafting, stress-test the outline by considering:
- **Normative claim clarity:** Is it explicit what the paper claims? (existence proof, methodological proposal, empirical study, etc.)
- **Domain-agnostic argument:** If the system is instantiated in a specific domain, is there a structural invariance argument showing the architecture doesn't depend on domain content?
- **Evaluation honesty:** Are metrics formalised? Is the gap between what can and cannot be measured stated explicitly?
- **Likely reviewer objections:** List 5-7 anticipated objections and where the paper addresses each
- **Compaction plan:** Which sections can absorb others if space is tight?

If the user provides external reviews (from other AI systems or human reviewers), weigh the feedback — don't just accept it. Accept what strengthens the paper, set aside what would cause scope creep or change the paper's identity.

### 5. Draft in Markdown

Write the full draft in `papers/<slug>/draft.md`.

Structure:
```markdown
# [Title]

**Author:** [Name and affiliation]    ← use "Authors:" if multiple

**Abstract:** [150-250 words]

**Keywords:** [3-6 keywords for SSRN discovery]

## 1. Introduction
...

## 2. [Section]
...

## N. Conclusion
...

## References
[Numbered or author-date format, consistent throughout]
```

**Drafting principles learned:**
- State the normative claim early (what kind of contribution this is)
- When coining terms, provide necessary-and-sufficient conditions, not just descriptions
- For domain-specific instantiations, include an architectural invariance argument
- Include a reproducibility subsection (model versions, sampling settings, prompt structure, failure handling)
- Evaluation sections should honestly separate "what we can measure" from "what we cannot"
- Structural analogies to established frameworks (e.g., Lakatos) can elevate a Discussion section from observations to theory
- AI pseudonyms for citation need governance clarification (metadata, not legal authorship)
- Failure modes sections are rare and valuable — be candid
- **Verify all URLs before submission.** URLs in references can become stale or be wrong from the start
- **Attribute claims precisely.** When citing a named person, quote or closely paraphrase what they actually said. Do not synthesise a stronger claim and attribute it to them
- **Scope formal results accurately.** If a paper proves X under conditions Y, state both X and Y. Dropping scope conditions inflates the claim
- **Avoid anthropomorphic framing of AI system behaviour.** Do not describe AI outputs as "conceived," "identified for itself," or "self-aware." Describe what the system produced and why the architecture led to that output. This is especially important when citing Shanahan's anthropomorphism warning — do not violate the principle you invoke
- **Signal preprint/non-peer-reviewed status** of cited works. Do not present PhilArchive preprints alongside published journal articles without indicating the difference
- **Do not list contributions you haven't delivered.** If a section contains placeholder data, do not claim that section's content as a contribution in the introduction
- **Existence proofs need specificity.** "We prove X exists" must specify what X is concretely — not "that a system can run" (trivial) but what measurable property the system demonstrates
- **Ground architectural claims in concrete mechanisms.** When claiming a system converges or improves, explain *why* — what feedback signal drives the convergence? Coding agents converge because tests provide objective pass/fail signals. Philosophy lacks this. If your system approximates testability through review layers, say so explicitly, and be honest about where the approximation falls short
- **Process reviews into the outline, not the draft.** When receiving review feedback, update the outline and maintain a review corrections checklist there. Generate fresh drafts from the corrected outline rather than patching the draft directly. This prevents drift between the outline (source of truth) and the draft
- **Make arithmetic verifiable.** When reporting counts that should add up (e.g., review files by type totalling to a grand total), verify the sum. Unexplained arithmetic gaps in a paper about rigour invite scrutiny
- **Distinguish "detected and corrected" from "fewer than baseline."** Showing that a system finds and fixes errors is not the same as showing comparative superiority over a baseline. Do not use comparative language ("measurably fewer than X") unless you have a direct comparison. "Identifies and resolves" is defensible; "fewer than single-pass" requires a controlled comparison
- **Acknowledge small sample sizes.** If a mechanism has been used only a handful of times (e.g., 5 outer reviews out of 1,370 total), state the count, explain why it is small, and do not draw general conclusions from it
- **Explain hedged counts.** "At least N" without explanation suggests incomplete record-keeping. Either give exact counts or explain what makes borderline cases ambiguous (e.g., "6 confirmed fabricated citations; additional cases where citation details were imprecise rather than wholly invented")
- **Add forward references for unsupported claims.** If a claim in an early section (e.g., "drives measurable improvement") is supported by data in a later section, add a forward reference "(Section N)" so the reader knows evidence is coming
- **Map technical mechanisms to familiar analogues.** Review layers map onto traditional philosophical workflow (pessimistic review ≈ hostile referee, outer review ≈ reviewer from a different subfield). Making these comparisons explicit helps readers from adjacent fields understand the architecture

### 6. Publish to Website

Each paper gets a landing page and per-version pages on unfinishablemap.org. These live in `obsidian/papers/` and sync through the normal pipeline.

**Landing page** — `obsidian/papers/<slug>.md`:
- Title, author, summary, keywords, repository link
- Version table with wikilinks to each version page

**Version page** — `obsidian/papers/<slug>-v<N>.md`:
- Full abstract
- PDF download link pointing to `/papers/<slug>/<slug>-v<N>.pdf`
- Suggested citations (APA + BibTeX) with canonical URL `https://unfinishablemap.org/papers/<slug>-v<N>/`
- Version notes
- Wikilink back to landing page

**PDF storage** — `hugo/static/papers/<slug>/<slug>-v<N>.pdf`:
- Served at `/papers/<slug>/<slug>-v<N>.pdf`
- Copy the exported PDF here after finalising

All files use standard flat frontmatter with `ai_contribution: 0` (human-authored pages about the paper). The papers section has no menu entry but appears in the sitemap.

URL structure:
| URL | Purpose |
|-----|---------|
| `/papers/` | Section listing |
| `/papers/<slug>/` | Paper landing (all versions) |
| `/papers/<slug>-v<N>/` | Version page: abstract, PDF download, citation |
| `/papers/<slug>/<slug>-v<N>.pdf` | PDF file |

### 7. Prepare Figures

- Export diagrams to `papers/<slug>/figures/` as PNG (300+ dpi) or SVG
- Mermaid diagrams from the site can be rendered via CLI or screenshot
- Each figure needs a caption and must be referenced in the text

### 8. Write to Google Docs

Using Chrome browser automation:
1. Create a new blank Google Doc (or open existing draft)
2. Transfer content section by section from draft.md
3. Apply heading styles (Heading 1, Heading 2, etc.)
4. Insert figures at appropriate locations
5. Name the document: "[Paper Title] draft N"

### 9. Format for PDF Export

Apply these formatting changes in Google Docs:

1. **Font:** Select All (Ctrl+A), change to Times New Roman (serif)
2. **Page numbers:** Format > Page numbers > Footer, start at 1, show on all pages
3. **Title block metadata** (below author line, in Normal text style):
   - Affiliation line (e.g., "Independent Researcher")
   - Status line: "Preprint — [Month Year] — Not peer-reviewed"
4. **No decorative formatting** — no horizontal rules, drop caps, or ornamental dividers. Clean section headings and consistent typography are sufficient

The title block should read:
```
[Title]
Author: [Name] ([email])       ← use "Authors:" if multiple
[Affiliation]
Preprint — [Month Year] — Not peer-reviewed

Abstract
[...]
```

### 10. Export and Publish

1. Export Google Doc as PDF (File > Download > PDF)
2. Verify formatting in the PDF (page numbers, font, title block)
3. Save locally with version: `papers/<slug>/exports/<slug>-v1.pdf`
4. Copy PDF to `hugo/static/papers/<slug>/<slug>-v1.pdf` for website hosting
5. Update the version page's download link (remove "coming soon" if present)
6. Run `uv run python scripts/sync.py` and verify with `cd hugo && hugo server`
7. Submit to target platforms (see submission notes below)

### 11. Version Management

Neither SSRN nor PhilArchive maintains version history reliably (SSRN overwrites without preserving previous versions). Manage versions locally:

- Keep exported PDFs in `papers/<slug>/exports/` with version numbers: `<slug>-v1.pdf`, `<slug>-v2.pdf`
- Track versions in git
- Optionally note the version on the PDF title page (e.g., "v1.0" after the date)
- Google Docs document title should include draft number: "[Title] draft N"

## Platform Submission Notes

### SSRN

- SSRN is a preprint server — no peer review, basic editorial screening only
- No cost to submit or read
- **No formatting requirements** — SSRN is format-agnostic. Just upload a readable PDF
- **One hard rule:** title and author names in the PDF must match the submission form
- Author affiliations must appear in the PDF
- English abstract required
- **SSRN adds its own footer** ("Electronic copy available at: http://ssrn.com/abstract=XXXX") to the first two pages — can be unchecked during upload
- **SSRN does not preserve previous versions** — revisions permanently overwrite. Manage your own version history
- Submission form requires: title, date written, abstract, author names + affiliations. Keywords and DOI are optional
- Relevant networks: Philosophy Research Network, Computer Science Research Network

### PhilArchive

- PhilArchive is an open-access philosophy e-print archive (sister site of PhilPapers)
- No cost to submit or read
- **No formatting requirements** — no templates, no mandated fonts/margins/page size, no required metadata in the PDF
- Papers must be "of professional quality" — lightly vetted for quality and relevance
- Metadata (title, abstract, keywords, categories) is entered through the web form, not the PDF
- Versioning is handled through their web interface — they support multiple versions with permanent links
- Requires a Phil* account (shared across PhilPapers, PhilArchive, PhilEvents, PhilJobs)
- Content appears on both PhilArchive and PhilPapers automatically
- Categories use the PhilPapers taxonomy — select appropriate philosophy subcategories

## Important

- Papers are NOT Map content — they are about the Map, written for an academic audience
- Keep the Map's philosophical positions as context, not argument — the paper's contribution is methodological
- All claims about the system should be verifiable from the public repo
- Include the repo URL and site URL for reproducibility
- Diagrams should be self-contained (readable without visiting the site)
- When the user provides stats or data to fill placeholders, integrate them and enforce section word caps during compaction
