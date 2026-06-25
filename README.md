# Evaluation Knowledge Base

This repository contains a Quarto website for source-grounded study notes on evaluation books and guidance. The first book section covers Sue C. Funnell and Patricia J. Rogers' *Purposeful Program Theory: Effective Use of Theories of Change and Logic Models*.
The site also includes generated major-section study notes for the ready `evaluation-texts` books in the MCP research library.

## Site Structure

```text
.
├── _quarto.yml
├── index.qmd
├── references.bib
├── notes/
│   ├── index.qmd
│   └── purposeful-programme-theory/
│       ├── index.qmd
│       ├── chapter-*.qmd
│       └── synthesis pages
├── assets/
│   ├── css/
│   └── js/
├── data/
│   ├── notes_link_graph_payload.json
│   ├── research_library_notes_manifest.json
│   └── research-library/
├── scripts/
│   ├── extract_book_to_json.py
│   ├── generate_research_library_notes.py
│   ├── qa_book_extraction.py
│   ├── qa_research_library_notes.py
│   └── extract_link_graph.py
└── viewer/
```

## Render

Render the website from the repository root:

```bash
quarto render
```

The pre-render step scans notes and writes `data/notes_link_graph_payload.json`, which supports the notes map.

## MCP Research-Library Notes

Regenerate the MCP-derived notes from the curated manifest in `scripts/generate_research_library_notes.py`:

```bash
python3 scripts/generate_research_library_notes.py
python3 scripts/qa_research_library_notes.py
```

Refresh the curated evidence IDs with the `mcp__researchlibrary` tools before changing the generator's book or section records. The checked-in evidence summaries store retrieval IDs and source locations, not copied source text.

## Extraction QA

The current book extraction can be checked with:

```bash
python3 scripts/qa_book_extraction.py book_extracted.json --max-per-category 25
```

## Adding More Books

1. Add the source PDF and extracted JSON, preferably under a future `sources/<book-slug>/` folder once multiple books are present.
2. Add a BibTeX entry to `references.bib`.
3. Create `notes/<book-slug>/index.qmd` and chapter files under the same folder.
4. Add the new book section and chapter pages to `_quarto.yml`.
5. Keep notes paraphrased, source-grounded, and cross-linked to related concepts and chapters.
6. Run `quarto render` and check navigation, citations, and the generated link graph.

## Note Conventions

Chapter notes should include source metadata, a study summary, key concepts, practical implications, connections to other notes, study prompts, and references. Use source page ranges from the extracted table of contents and avoid long verbatim passages from copyrighted texts.
