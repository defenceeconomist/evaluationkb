# Book Extraction Plan

Target PDF:

`Purposeful Program Theory Effective Use of Theories of Change and Logic Models. by Funnell, Sue C. Rogers, Patricia J..pdf`

Output:

`book_extracted.json`, a reconstruction-oriented JSON document containing ordered text, headings, figures, boxes, headers, and footers.

## Extraction Strategy

1. Read the PDF with PyMuPDF.
   - Extract document metadata.
   - Extract the embedded table of contents with `doc.get_toc()`.
   - Use TOC entries as the primary source for heading levels.

2. Extract page elements in reading order.
   - Text blocks are extracted from `page.get_text("dict")`.
   - Raw PDF lines are reconstructed into visual lines, then grouped into paragraph elements using geometry, indentation, line gaps, and style continuity.
   - Wrapped paragraph lines are joined with spaces, with simple line-break hyphenation repair. List-like/index-like groups preserve line breaks and are marked with `paragraph_preserves_line_breaks`.
   - Image blocks are embedded in JSON as base64 `data:image/...` strings.
   - Drawing rectangles are inspected as candidate boxes.
   - Box regions are rendered to PNG and embedded as base64 text so the box can be reconstructed visually even when its internals are complex.

3. Tag headings.
   - Normalize text and TOC titles.
   - Match extracted text blocks against TOC entries on the same page or nearby pages, including compact matching for letter-spaced headings.
   - Assign `heading_level` from the TOC level.
   - Add a secondary font-size and top-of-page heuristic for unlisted headings, but keep these marked as heuristic.
   - Treat large one-letter chapter openers as `drop_cap` paragraph elements, not headings.

4. Tag headers and footers.
   - First identify text in the top and bottom page bands.
   - Then detect repeated normalized text across pages.
   - Mark matching elements with `type: "header"` or `type: "footer"` and `filterable: true`.

5. Tag figures and boxes.
   - Image blocks become `type: "figure"` with embedded base64 text.
   - Vector-drawn visual regions linked to `Figure`/`Fig.` captions become `type: "figure"` image crops. Nested vector rectangles inside those figures are removed as separate visual elements.
   - Callout regions without figure captions become `type: "box"` after duplicate/near-duplicate filtering, such as the “Origins of Black Box” callout.
   - Box JSON includes enclosed child text ids, an embedded rendered crop, and `render_layer`.
   - Caption text beginning with `Figure`, `Table`, or `Exhibit` is tagged as `figure_caption`; only `Figure`/`Fig.` captions convert nearby visual crops into figures.
   - Text inside figures is tagged `figure_text` for inspection/search but is hidden from default combined and readable viewer modes because the figure crop is authoritative.

## Viewer QA Features

- Layout QA mode renders the extracted page geometry and supports layer controls for images, text, and combined display.
- Readable Text mode renders:
  - figures as inline image crops with captions;
  - boxes as bordered callout blocks using their child text;
  - tables as geometry-preserving panels using extracted table captions and cell text positions.
- The sidebar Review panel lists all figures, boxes, and tables, with filters for each kind and direct page navigation for QA.

6. Preserve reconstruction data.
   - Every element has a stable id, page number, original `bbox`, padded `render_bbox`, reading order, type, role, `block_role`, text or embedded image text, source line boxes, line count, and style hints.
   - Page dimensions and source metadata are stored at top level.

7. QA extraction output.
   - Run `scripts/qa_book_extraction.py` to check TOC heading coverage, drop-cap classification, render geometry, duplicate boxes, relationship ids, and caption/visual links.
   - Use the viewer's Layout QA mode for bbox/layer review and Readable Text mode for extracted-content review.

## JSON Shape

```json
{
  "schema_version": "1.0",
  "source": {"path": "book.pdf", "page_count": 1},
  "toc": [{"level": 1, "title": "Chapter", "page": 12}],
  "pages": [
    {
      "page_number": 1,
      "width": 612,
      "height": 792,
      "elements": [
        {
          "id": "p0001_e0001",
          "type": "heading",
          "heading_level": 1,
          "filterable": false,
          "bbox": [72, 80, 540, 108],
          "render_bbox": [68, 76, 544, 112],
          "block_role": "chapter_title",
          "lines": [{"bbox": [72, 80, 540, 108], "text": "Chapter title"}],
          "text": "Chapter title"
        }
      ]
    }
  ]
}
```

## Runtime Dependency

Install PyMuPDF before running:

```sh
python3 -m pip install pymupdf
```
