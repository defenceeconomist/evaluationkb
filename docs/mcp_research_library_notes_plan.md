# MCP Evaluation Text Study Notes

## Summary

- Add study notes for the missing ready books in the MCP `evaluation-texts` collection, keeping the existing Purposeful Program Theory pages as the template and baseline.
- Generate book-level overview, concepts, chapter map, practice implications, and chapter/major-section notes for each added book.
- Use `mcp__researchlibrary` evidence packs as the source of truth; do not depend on local PDFs or the unavailable lower-level MCP chunk fetch endpoint.

## Key Changes

- Add a checked-in manifest at `data/research_library_notes_manifest.json` with `book_id`, slug, title, authors, year, citation key, source status, target paths, and selected section/page ranges.
- Add `notes/<book-slug>/` folders for the missing books, each following the current note structure: Source, Core Argument, Study Summary, Key Concepts, Structure, Practical Implications, Connections, Study Prompts, References.
- Update `references.bib` with citation keys for all added books.
- Refactor `_quarto.yml` sidebar for multi-book navigation: global sidebar lists book-level pages; each book index/chapter map carries detailed chapter links.
- Update `notes/index.qmd`, `index.qmd`, `assets/js/notes_filter.js`, and CSS as needed so note cards can filter by book and note type.

## Extraction Workflow

- Start with `library_list_collections`; select ready books in `evaluation-texts`, excluding `purposeful-program-theory` unless refreshing is explicitly requested.
- Discover candidate chapters/major sections per book using broad `rag_search` queries, then build the manifest from unique `section_id`, `section_path`, and page ranges.
- For each manifest section, call `rag_evidence_pack` with `include_neighbors: true`; use `include_media: true` only when figures/tables are needed for understanding.
- Hydrate important or ambiguous records with `rag_get_record`; scan examples/cases/exhibits with `library_scan_labels`.
- Save compact evidence summaries under `data/research-library/evidence/<book-slug>/` for auditability.
- Write only paraphrased notes, with page ranges and evidence IDs in front matter; avoid long verbatim source passages.

## Interfaces

- QMD front matter adds: `book_id`, `collection_id`, `note_type`, `source_pages`, `citation`, `evidence_ids`, and `source_status`.
- Note cards add `data-book` and keep `data-type`; existing `data-section` can remain for legacy/current pages.
- The link graph pre-render remains `scripts/extract_link_graph.py --include-prefix notes/`; generated pages must use normal relative `.qmd` links.

## Test Plan

- Run manifest QA: no duplicate slugs/paths, all citation keys exist in `references.bib`, all evidence IDs point to saved summaries.
- Run notes QA: every generated page has required sections, source metadata, at least one citation, and no TODO markers.
- Run link graph generation and check internal links resolve.
- Run `quarto render --quiet`.
- Spot-check at least one chapter/major-section note per book against its saved evidence summary for claim support and paraphrase quality.

## Assumptions

- Defaults chosen because no clarification answer was received: add missing books first; generate chapter plus book-synthesis pages; do not create cross-book thematic synthesis pages in v1.
- MCP book records are `rag_status: ready` but `status: needs_review`, so generated pages should remain labelled as source-grounded study notes rather than definitive editions.
- Figures/tables are used as supporting evidence for synthesis, not republished as site assets unless separately approved.
