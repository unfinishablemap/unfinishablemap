---
name: compose-paper
description: Compose an academic working paper for SSRN. Drafts locally in markdown, then writes to Google Docs via Chrome for final formatting and PDF export.
---

# Compose Paper

Draft and produce an academic working paper suitable for submission to SSRN as a preprint.

## When to Use

- When `/compose-paper [topic]` is invoked
- When the user wants to write a paper about the Map's methodology, architecture, or findings

## Directory Structure

Each paper lives in `papers/<slug>/`:

```
papers/<slug>/
├── outline.md          # Section outline with key points per section
├── draft.md            # Full markdown draft (primary working file)
├── figures/            # Diagrams and images (PNG/SVG, 300+ dpi)
├── references.md       # Bibliography in development
└── notes.md            # Scratch space, research notes, decisions log
```

This directory is outside `obsidian/` and `hugo/` — papers are not part of the site content pipeline.

## Writing Style

### Academic Register

Papers use a different voice from Map articles:

- **Third person, passive acceptable.** "The system was designed to..." not "We built..."
  - Exception: "we" is acceptable in a clearly authored working paper with named authors
- **Hedged claims.** "The results suggest..." not "This proves..."
- **No tenet advocacy.** Papers describe the Map's tenets as methodological choices, not truth claims
- **Define all jargon.** Assume the reader knows neither philosophy of mind nor Hugo/Obsidian

### Formatting

- Single column, 11-12pt serif font (Times New Roman or similar)
- 1-inch margins, 1.5 line spacing
- Numbered sections (1, 1.1, 1.2, 2, ...)
- Figures/tables inline with numbered captions (Figure 1, Table 1)
- References at end, APA or similar consistent style

### Length

- Typical SSRN working paper: 4,000-10,000 words
- Target for Map methodology papers: 5,000-7,000 words

## Instructions

### 1. Plan the Paper

Create `papers/<slug>/outline.md` with:
- Working title and abstract (150-250 words)
- Section headings with 2-3 bullet points each describing key content
- Identify which figures/diagrams are needed
- List key references

Review outline with the user before proceeding.

### 2. Draft in Markdown

Write the full draft in `papers/<slug>/draft.md`.

Structure:
```markdown
# [Title]

**Authors:** [Names and affiliations]

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

### 3. Prepare Figures

- Export diagrams to `papers/<slug>/figures/` as PNG (300+ dpi) or SVG
- Mermaid diagrams from the site can be rendered via CLI or screenshot
- Each figure needs a caption and must be referenced in the text

### 4. Write to Google Docs

Using Chrome browser automation:
1. Create a new blank Google Doc
2. Set up formatting (font, margins, spacing)
3. Transfer content section by section from draft.md
4. Insert figures at appropriate locations
5. Apply heading styles (Heading 1, Heading 2, etc.)
6. Name the document: "[Paper Title] — SSRN Draft"

<!-- TODO: Refine the Google Docs workflow as we learn what works -->

### 5. Export and Submit

1. Export Google Doc as PDF (File > Download > PDF)
2. Verify formatting in the PDF
3. Submit to SSRN:
   - Title matching the PDF title page
   - Abstract matching the paper
   - Keywords
   - Author name and affiliation
   - Select appropriate research network(s)

## SSRN Submission Notes

- SSRN is a preprint server — no peer review, basic editorial screening only
- No cost to submit or read
- Paper must be uploaded as PDF
- Title in PDF must match title in submission form
- Author affiliations must appear in the PDF
- English abstract required
- Relevant networks: Philosophy Research Network, Computer Science Research Network

## Important

- Papers are NOT Map content — they are about the Map, written for an academic audience
- Keep the Map's philosophical positions as context, not argument — the paper's contribution is methodological
- All claims about the system should be verifiable from the public repo
- Include the repo URL and site URL for reproducibility
- Diagrams should be self-contained (readable without visiting the site)
