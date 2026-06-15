#!/usr/bin/env python3
"""Extract a PDF book into reconstruction-oriented JSON.

The extractor preserves page order, text blocks, TOC-derived heading levels,
filterable headers/footers, image figures, and visually rendered boxes.

Runtime dependency:
    python3 -m pip install pymupdf
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    import fitz  # PyMuPDF
except ImportError as exc:  # pragma: no cover - exercised only without dependency
    raise SystemExit(
        "Missing dependency: PyMuPDF. Install it with:\n"
        "  python3 -m pip install pymupdf"
    ) from exc


DEFAULT_PDF = (
    "Purposeful Program Theory Effective Use of Theories of Change and Logic Models. "
    "by Funnell, Sue C. Rogers, Patricia J..pdf"
)

CAPTION_RE = re.compile(r"^(figure|fig\.|table|exhibit)\s+\d+(?:\.\d+)?\b", re.I)
FIGURE_CAPTION_RE = re.compile(r"^(figure|fig\.)\s+\d+(?:\.\d+)?\b", re.I)
TABLE_CAPTION_RE = re.compile(r"^(?i:table)\s+\d+(?:\.\d+)+(?:\s+\([^)]+\)|\s+[A-Z0-9])")
LIST_MARKER_RE = re.compile(r"^(?:[•▪◦·]|[-–]|\d+[.)]|[a-zA-Z][.)])$")
LIST_ITEM_RE = re.compile(r"^(?P<marker>[•▪◦·]|[-–]|\d+[.)]|[a-zA-Z][.)])\s+")
LIGATURE_REPLACEMENTS = str.maketrans(
    {
        "ﬁ": "fi",
        "ﬂ": "fl",
        "ﬀ": "ff",
        "ﬃ": "ffi",
        "ﬄ": "ffl",
    }
)
SPACED_HEADING_REPLACEMENTS = {
    "c o n t e n t s": "Contents",
    "co n ten ts": "Contents",
    "pa r t o n e": "PART ONE",
    "pa r t t w o": "PART TWO",
    "pa r t t h r e e": "PART THREE",
    "pa r t f o u r": "PART FOUR",
    "pa r t f i v e": "PART FIVE",
    "pa r t 1": "PART 1",
    "pa r t 2": "PART 2",
    "pa r t 3": "PART 3",
    "pa r t 4": "PART 4",
    "pa r t 5": "PART 5",
}


@dataclass(frozen=True)
class TocEntry:
    level: int
    title: str
    page: int
    norm_title: str


def normalize_text(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "").strip().lower()
    value = re.sub(r"^[\W_]+|[\W_]+$", "", value)
    return value


def clean_extracted_text(value: str) -> str:
    value = (value or "").translate(LIGATURE_REPLACEMENTS)
    value = re.sub(r"\b([A-Za-z]*(?:ffi|ffl|fi|fl))\s+([a-z]+)\b", r"\1\2", value)

    stripped = re.sub(r"\s+", " ", value).strip()
    heading_key = stripped.lower()
    if heading_key in SPACED_HEADING_REPLACEMENTS:
        return SPACED_HEADING_REPLACEMENTS[heading_key]

    tokens = stripped.split()
    if len(tokens) >= 2 and all(re.fullmatch(r"[ivxlcdm]", token, re.I) for token in tokens):
        return "".join(tokens)

    return value


def normalize_compact(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def text_hash(value: str) -> str:
    return hashlib.sha1(normalize_text(value).encode("utf-8")).hexdigest()[:12]


def list_marker(value: str) -> str | None:
    text = (value or "").strip()
    if LIST_MARKER_RE.fullmatch(text):
        return text
    match = LIST_ITEM_RE.match(text)
    return match.group("marker") if match else None


def list_kind(marker: str | None) -> str | None:
    if not marker:
        return None
    return "ordered" if re.fullmatch(r"(?:\d+|[a-zA-Z])[.)]", marker) else "unordered"


def is_list_marker_line(line: dict[str, Any]) -> bool:
    return bool(list_marker(line.get("text", "")))


def bbox_area(bbox: Iterable[float]) -> float:
    x0, y0, x1, y1 = bbox
    return max(0.0, x1 - x0) * max(0.0, y1 - y0)


def expand_bbox(bbox: Iterable[float], page_size: tuple[float, float], padding: float = 3.0) -> list[float]:
    x0, y0, x1, y1 = bbox
    width, height = page_size
    return [
        round(max(0.0, x0 - padding), 3),
        round(max(0.0, y0 - padding), 3),
        round(min(width, x1 + padding), 3),
        round(min(height, y1 + padding), 3),
    ]


def bbox_intersection_area(first: Iterable[float], second: Iterable[float]) -> float:
    ax0, ay0, ax1, ay1 = first
    bx0, by0, bx1, by1 = second
    return max(0.0, min(ax1, bx1) - max(ax0, bx0)) * max(0.0, min(ay1, by1) - max(ay0, by0))


def bbox_similarity(first: Iterable[float], second: Iterable[float]) -> float:
    first_area = bbox_area(first)
    second_area = bbox_area(second)
    if not first_area or not second_area:
        return 0.0
    intersection = bbox_intersection_area(first, second)
    union = first_area + second_area - intersection
    return intersection / union if union else 0.0


def vertical_gap(first: Iterable[float], second: Iterable[float]) -> float:
    return second[1] - first[3]


def contains(outer: Iterable[float], inner: Iterable[float], tolerance: float = 2.0) -> bool:
    ox0, oy0, ox1, oy1 = outer
    ix0, iy0, ix1, iy1 = inner
    return (
        ox0 - tolerance <= ix0
        and oy0 - tolerance <= iy0
        and ox1 + tolerance >= ix1
        and oy1 + tolerance >= iy1
    )


def rect_to_list(rect: Any) -> list[float]:
    return [round(float(rect[0]), 3), round(float(rect[1]), 3), round(float(rect[2]), 3), round(float(rect[3]), 3)]


def pixmap_to_data_uri(pix: Any, image_format: str = "png") -> str:
    data = pix.tobytes(image_format)
    encoded = base64.b64encode(data).decode("ascii")
    return f"data:image/{image_format};base64,{encoded}"


def image_bytes_to_data_uri(image_bytes: bytes, extension: str | None) -> str:
    ext = (extension or "png").lower().lstrip(".")
    mime_ext = "jpeg" if ext in {"jpg", "jpeg"} else ext
    encoded = base64.b64encode(image_bytes).decode("ascii")
    return f"data:image/{mime_ext};base64,{encoded}"


def render_clip_to_data_uri(page: Any, bbox: Iterable[float], zoom: float) -> str:
    matrix = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=matrix, clip=fitz.Rect(*bbox), alpha=False)
    return pixmap_to_data_uri(pix, "png")


def extract_toc(doc: Any) -> list[TocEntry]:
    entries: list[TocEntry] = []
    for level, title, page in doc.get_toc(simple=True):
        clean_title = clean_extracted_text(title).strip()
        entries.append(TocEntry(level=int(level), title=clean_title, page=int(page), norm_title=normalize_text(clean_title)))
    return entries


def toc_by_page(toc: list[TocEntry], page_tolerance: int) -> dict[int, list[TocEntry]]:
    by_page: dict[int, list[TocEntry]] = defaultdict(list)
    for entry in toc:
        for page in range(max(1, entry.page - page_tolerance), entry.page + page_tolerance + 1):
            by_page[page].append(entry)
    return by_page


def merge_bbox(bboxes: Iterable[Iterable[float]]) -> list[float]:
    values = [list(bbox) for bbox in bboxes]
    if not values:
        return [0.0, 0.0, 0.0, 0.0]
    return [
        round(min(bbox[0] for bbox in values), 3),
        round(min(bbox[1] for bbox in values), 3),
        round(max(bbox[2] for bbox in values), 3),
        round(max(bbox[3] for bbox in values), 3),
    ]


def line_overlap_ratio(first: Iterable[float], second: Iterable[float]) -> float:
    _, ay0, _, ay1 = first
    _, by0, _, by1 = second
    overlap = max(0.0, min(ay1, by1) - max(ay0, by0))
    height = max(0.001, min(ay1 - ay0, by1 - by0))
    return overlap / height


def lines_are_adjacent_on_same_visual_line(first: Iterable[float], second: Iterable[float]) -> bool:
    ax0, _, ax1, _ = first
    bx0, _, bx1, _ = second
    horizontal_gap = max(0.0, max(ax0, bx0) - min(ax1, bx1))
    return line_overlap_ratio(first, second) >= 0.6 and horizontal_gap <= 8.0


def visual_lines_from_block(block: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    raw_lines: list[dict[str, Any]] = []
    all_spans: list[dict[str, Any]] = []
    for line in block.get("lines", []):
        parts = []
        spans: list[dict[str, Any]] = []
        for span in line.get("spans", []):
            text = span.get("text", "")
            if text:
                parts.append(text)
                spans.append(span)
                all_spans.append(span)
        if parts:
            raw_lines.append(
                {
                    "bbox": rect_to_list(line.get("bbox", [0, 0, 0, 0])),
                    "text": clean_extracted_text("".join(parts)),
                    "spans": spans,
                }
            )

    visual_lines: list[dict[str, Any]] = []
    for raw_line in sorted(raw_lines, key=lambda item: (item["bbox"][1], item["bbox"][0])):
        if visual_lines and lines_are_adjacent_on_same_visual_line(visual_lines[-1]["bbox"], raw_line["bbox"]):
            previous = visual_lines[-1]
            pieces = previous.pop("_pieces")
            pieces.append(raw_line)
            pieces.sort(key=lambda item: item["bbox"][0])
            previous["_pieces"] = pieces
            previous["bbox"] = merge_bbox(piece["bbox"] for piece in pieces)
            previous["text"] = clean_extracted_text("".join(piece["text"] for piece in pieces).strip())
            previous["spans"] = [span for piece in pieces for span in piece["spans"]]
        else:
            visual_lines.append({**raw_line, "_pieces": [raw_line]})

    for line in visual_lines:
        line.pop("_pieces", None)
        line["style"] = style_from_spans(line["spans"])
    return visual_lines, all_spans


def text_from_lines(lines: list[dict[str, Any]], preserve_line_breaks: bool = False) -> str:
    if preserve_line_breaks:
        return "\n".join(line["text"].strip() for line in lines if line["text"].strip()).strip()

    text = ""
    for line in lines:
        value = line["text"].strip()
        if not value:
            continue
        if not text:
            text = value
        elif text.endswith("-") and value[:1].islower():
            text = text[:-1] + value
        else:
            text += " " + value
    return re.sub(r"[ \t]+", " ", text).strip()


def lines_from_block(block: dict[str, Any]) -> tuple[str, list[dict[str, Any]], list[dict[str, Any]]]:
    lines, spans = visual_lines_from_block(block)
    return text_from_lines(lines, preserve_line_breaks=True), spans, lines


def style_from_spans(spans: list[dict[str, Any]]) -> dict[str, Any]:
    if not spans:
        return {}
    sizes = [float(span.get("size", 0.0)) for span in spans if span.get("size")]
    fonts = [span.get("font") for span in spans if span.get("font")]
    flags = [int(span.get("flags", 0)) for span in spans if span.get("flags") is not None]
    return {
        "font_size": round(statistics.median(sizes), 3) if sizes else None,
        "font": Counter(fonts).most_common(1)[0][0] if fonts else None,
        "flags": Counter(flags).most_common(1)[0][0] if flags else None,
    }


def font_size(style: dict[str, Any]) -> float | None:
    size = style.get("font_size")
    return float(size) if size else None


def styles_compatible(first: dict[str, Any], second: dict[str, Any]) -> bool:
    first_size = font_size(first)
    second_size = font_size(second)
    if first_size and second_size and abs(first_size - second_size) > 1.0:
        return False

    first_font = first.get("font")
    second_font = second.get("font")
    if first_font and second_font and first_font != second_font:
        first_base = re.sub(r"[-,]?(Regular|Roman|Italic|Bold|Lite|Light|Semibold).*$", "", first_font)
        second_base = re.sub(r"[-,]?(Regular|Roman|Italic|Bold|Lite|Light|Semibold).*$", "", second_font)
        if first_base and second_base and first_base != second_base:
            return False
    return True


def should_preserve_line_breaks(lines: list[dict[str, Any]]) -> bool:
    if len(lines) <= 1:
        return False

    texts = [line["text"].strip() for line in lines if line["text"].strip()]
    if not texts:
        return False

    short_lines = sum(1 for text in texts if len(text) <= 42)
    numeric_index_lines = sum(1 for text in texts if re.search(r"\b[ivxlcdm\d]+(?:[-–,]\s*[ivxlcdm\d]+)*$", text, re.I))
    return len(texts) >= 4 and (short_lines / len(texts) >= 0.65 or numeric_index_lines / len(texts) >= 0.45)


def serialise_lines(lines: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "bbox": line["bbox"],
            "text": line["text"].strip(),
            "style": line.get("style", {}),
        }
        for line in lines
        if line.get("text", "").strip()
    ]


def visual_row_count(lines: list[dict[str, Any]]) -> int:
    rows: list[dict[str, Any]] = []
    for line in sorted(lines, key=lambda value: (value["bbox"][1], value["bbox"][0])):
        if rows and line_overlap_ratio(rows[-1]["bbox"], line["bbox"]) >= 0.35:
            rows[-1]["bbox"] = merge_bbox([rows[-1]["bbox"], line["bbox"]])
        else:
            rows.append(line)
    return len(rows)


def paragraph_break(previous: dict[str, Any], current: dict[str, Any], paragraph: list[dict[str, Any]]) -> bool:
    px0, py0, px1, py1 = previous["bbox"]
    cx0, cy0, cx1, cy1 = current["bbox"]
    del py0

    if is_list_marker_line(current) and any(not is_list_marker_line(line) for line in paragraph):
        return True

    if is_list_marker_line(previous):
        return False

    prev_height = max(1.0, py1 - previous["bbox"][1])
    current_height = max(1.0, cy1 - cy0)
    vertical_gap = cy0 - py1
    if vertical_gap < -min(prev_height, current_height) * 0.35:
        return True
    if vertical_gap > max(prev_height, current_height) * 1.25:
        return True

    horizontal_overlap = max(0.0, min(px1, cx1) - max(px0, cx0))
    narrow_width = max(1.0, min(px1 - px0, cx1 - cx0))
    if horizontal_overlap / narrow_width < 0.35 and abs(cx0 - px0) > 24:
        return True

    if not styles_compatible(previous.get("style", {}), current.get("style", {})):
        return True

    paragraph_left = min(line["bbox"][0] for line in paragraph)
    previous_left = previous["bbox"][0]
    indent = cx0 - paragraph_left
    previous_is_body_left = abs(previous_left - paragraph_left) <= 4.0
    if previous_is_body_left and indent >= 10.0:
        return True

    outdent = paragraph_left - cx0
    if len(paragraph) > 1 and outdent >= 10.0:
        return True

    return False


def paragraphize_text_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_page: dict[int, list[dict[str, Any]]] = defaultdict(list)
    non_text: list[dict[str, Any]] = []
    for item in items:
        if item.get("kind") == "text":
            by_page[item["page_number"]].append(item)
        else:
            non_text.append(item)

    paragraph_items: list[dict[str, Any]] = []
    for page_number, page_items in by_page.items():
        lines: list[dict[str, Any]] = []
        for item in sorted(page_items, key=lambda value: (value["bbox"][1], value["bbox"][0], value["block_index"])):
            for line_index, line in enumerate(item.get("lines", [])):
                lines.append(
                    {
                        **line,
                        "page_number": page_number,
                        "block_index": item["block_index"],
                        "line_index": line_index,
                    }
                )

        current: list[dict[str, Any]] = []
        paragraph_index = 0
        for line in sorted(lines, key=lambda value: (value["bbox"][1], value["bbox"][0], value["block_index"], value["line_index"])):
            if current and paragraph_break(current[-1], line, current):
                paragraph_items.append(make_paragraph_item(page_number, paragraph_index, current))
                paragraph_index += 1
                current = []
            current.append(line)
        if current:
            paragraph_items.append(make_paragraph_item(page_number, paragraph_index, current))

    return non_text + paragraph_items


def make_paragraph_item(page_number: int, paragraph_index: int, lines: list[dict[str, Any]]) -> dict[str, Any]:
    spans = [span for line in lines for span in line.get("spans", [])]
    preserve_line_breaks = should_preserve_line_breaks(lines)
    text = text_from_lines(lines, preserve_line_breaks=preserve_line_breaks)
    marker = list_marker(lines[0]["text"] if lines else "") or list_marker(text)
    item = {
        "kind": "text",
        "page_number": page_number,
        "block_index": 200000 + paragraph_index,
        "bbox": merge_bbox(line["bbox"] for line in lines),
        "text": text,
        "norm_text": normalize_text(text),
        "style": style_from_spans(spans),
        "line_count": visual_row_count(lines),
        "lines": serialise_lines(lines),
        "paragraph_preserves_line_breaks": preserve_line_breaks,
    }
    if marker:
        item["list_marker"] = marker
        item["list_kind"] = list_kind(marker)
    return item


def collect_raw_elements(doc: Any, zoom: float) -> list[dict[str, Any]]:
    raw: list[dict[str, Any]] = []
    for page_index, page in enumerate(doc, start=1):
        page_dict = page.get_text("dict")
        for block_index, block in enumerate(page_dict.get("blocks", [])):
            block_type = block.get("type")
            bbox = rect_to_list(block.get("bbox", [0, 0, 0, 0]))
            if block_type == 0:
                text, spans, lines = lines_from_block(block)
                if not text:
                    continue
                raw.append(
                    {
                        "kind": "text",
                        "page_number": page_index,
                        "block_index": block_index,
                        "bbox": bbox,
                        "text": text,
                        "norm_text": normalize_text(text),
                        "style": style_from_spans(spans),
                        "lines": lines,
                    }
                )
            elif block_type == 1:
                image_bytes = block.get("image")
                if not image_bytes:
                    continue
                ext = block.get("ext") or block.get("extension") or "png"
                raw.append(
                    {
                        "kind": "figure",
                        "page_number": page_index,
                        "block_index": block_index,
                        "bbox": bbox,
                        "embedded_text": image_bytes_to_data_uri(image_bytes, ext),
                        "alt_text": "",
                        "source_format": ext,
                    }
                )

        for draw_index, drawing in enumerate(page.get_drawings()):
            rect = drawing.get("rect")
            if not rect:
                continue
            bbox = rect_to_list(rect)
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            if width < 48 or height < 24:
                continue
            if bbox_area(bbox) < 1600:
                continue
            raw.append(
                {
                    "kind": "drawn_region",
                    "page_number": page_index,
                    "block_index": 100000 + draw_index,
                    "bbox": bbox,
                    "embedded_text": render_clip_to_data_uri(page, bbox, zoom),
                }
            )
    return raw


def repeated_margin_text(raw: list[dict[str, Any]], page_sizes: dict[int, tuple[float, float]], band_ratio: float) -> set[str]:
    occurrences: dict[str, set[int]] = defaultdict(set)
    page_count = len(page_sizes)
    for item in raw:
        if item.get("kind") != "text":
            continue
        _, height = page_sizes[item["page_number"]]
        y0, y1 = item["bbox"][1], item["bbox"][3]
        in_margin = y1 <= height * band_ratio or y0 >= height * (1.0 - band_ratio)
        if in_margin and item["norm_text"]:
            occurrences[item["norm_text"]].add(item["page_number"])
    threshold = max(3, int(page_count * 0.08))
    return {text for text, pages in occurrences.items() if len(pages) >= threshold}


def classify_text(
    item: dict[str, Any],
    page_size: tuple[float, float],
    repeated_margin: set[str],
    toc_candidates: list[TocEntry],
    large_font_cutoff: float | None,
    band_ratio: float,
) -> dict[str, Any]:
    width, height = page_size
    del width
    y0, y1 = item["bbox"][1], item["bbox"][3]
    norm = item["norm_text"]

    if y1 <= height * band_ratio:
        role = "running_header" if norm in repeated_margin else "page_margin_header"
        return {"type": "header", "filterable": True, "role": role}
    if y0 >= height * (1.0 - band_ratio):
        role = "running_footer" if norm in repeated_margin else "page_margin_footer"
        return {"type": "footer", "filterable": True, "role": role}

    for entry in toc_candidates:
        compact_norm = normalize_compact(norm)
        compact_title = normalize_compact(entry.norm_title)
        if (
            norm == entry.norm_title
            or norm.startswith(entry.norm_title)
            or entry.norm_title.startswith(norm)
            or (compact_norm and compact_norm == compact_title)
            or (compact_norm and (compact_norm.startswith(compact_title) or compact_title.startswith(compact_norm)))
        ):
            return {
                "type": "heading",
                "filterable": False,
                "role": "toc_heading",
                "heading_level": entry.level,
                "heading_source": "toc",
                "toc_title": entry.title,
            }

    font_size = item.get("style", {}).get("font_size")
    if large_font_cutoff and font_size and font_size >= large_font_cutoff and len(norm) <= 140:
        return {
            "type": "heading",
            "filterable": False,
            "role": "inferred_heading",
            "heading_level": None,
            "heading_source": "font_size",
        }

    return {"type": "paragraph", "filterable": False, "role": "body_text"}


def infer_large_font_cutoff(raw: list[dict[str, Any]]) -> float | None:
    sizes = [
        float(item.get("style", {}).get("font_size"))
        for item in raw
        if item.get("kind") == "text" and item.get("style", {}).get("font_size")
    ]
    if len(sizes) < 20:
        return None
    body = statistics.median(sizes)
    high = statistics.quantiles(sizes, n=10)[-1]
    return round(max(body * 1.25, high), 3)


def dedupe_drawn_regions(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    kept: list[dict[str, Any]] = []
    for item in sorted(items, key=lambda value: bbox_area(value["bbox"]), reverse=True):
        if item.get("kind") != "drawn_region":
            kept.append(item)
            continue
        duplicate = False
        for existing in kept:
            if existing.get("kind") != "drawn_region" or existing["page_number"] != item["page_number"]:
                continue
            same_box = bbox_similarity(existing["bbox"], item["bbox"]) >= 0.97
            nested_without_distinct_shape = contains(existing["bbox"], item["bbox"], tolerance=1.0) and bbox_area(item["bbox"]) / max(
                1.0, bbox_area(existing["bbox"])
            ) > 0.92
            if same_box or nested_without_distinct_shape:
                duplicate = True
                break
        if not duplicate:
            kept.append(item)
    return kept


def is_drop_cap(element: dict[str, Any], large_font_cutoff: float | None) -> bool:
    text = (element.get("text") or "").strip()
    if not re.fullmatch(r"[A-Za-z]", text):
        return False
    font_size_value = font_size(element.get("style", {})) or 0.0
    bbox_height = element["bbox"][3] - element["bbox"][1]
    return bool(
        (large_font_cutoff and font_size_value >= large_font_cutoff)
        or font_size_value >= 22.0
        or bbox_height >= 28.0
    )


def is_chapter_number(element: dict[str, Any], toc_pages: dict[int, list[TocEntry]]) -> bool:
    text = (element.get("text") or "").strip()
    if not re.fullmatch(r"\d{1,2}", text):
        return False
    if not toc_pages.get(element["page_number"]):
        return False
    return element["bbox"][1] < 130 and (element["bbox"][3] - element["bbox"][1]) >= 24


def is_uppercase_heading_candidate(text: str) -> bool:
    letters = [char for char in text if char.isalpha()]
    return bool(letters) and sum(1 for char in letters if char.isupper()) / len(letters) >= 0.75


def is_figure_caption(element: dict[str, Any]) -> bool:
    return bool(FIGURE_CAPTION_RE.match((element.get("text") or "").strip()))


def caption_block_role(text: str) -> str | None:
    value = (text or "").strip()
    if FIGURE_CAPTION_RE.match(value):
        return "figure_caption"
    if TABLE_CAPTION_RE.match(value):
        return "table_caption"
    if re.match(r"^exhibit\s+\d+(?:\.\d+)?\b", value, re.I):
        return "exhibit_caption"
    return None


def classify_block_role(
    element: dict[str, Any],
    toc_pages: dict[int, list[TocEntry]],
    large_font_cutoff: float | None,
) -> str:
    text = (element.get("text") or "").strip()
    role = element.get("role", "")
    element_type = element.get("type")

    if element_type == "header":
        return "header"
    if element_type == "footer":
        return "footer"
    if element_type == "box":
        return "box"
    if element_type == "figure":
        return "figure"
    if element.get("list_marker"):
        return "list_item"
    if is_drop_cap(element, large_font_cutoff):
        return "drop_cap"
    if is_chapter_number(element, toc_pages):
        return "chapter_number"
    if role == "toc_heading" or (element_type == "heading" and element["bbox"][1] < 230):
        return "chapter_title" if toc_pages.get(element["page_number"]) and element["bbox"][1] < 240 else "heading"
    caption_role = caption_block_role(text)
    if caption_role:
        return caption_role
    if element_type == "heading":
        return "heading"
    if element.get("parent_box_element_ids"):
        return "box_text"
    if is_uppercase_heading_candidate(text) and len(text) <= 90 and element.get("line_count", 1) <= 2:
        return "heading"
    return "body_text"


def apply_text_relationship_roles(
    elements_by_page: dict[int, list[dict[str, Any]]],
    toc: list[TocEntry],
    large_font_cutoff: float | None,
) -> None:
    toc_pages = toc_by_page(toc, 1)

    for page_number, elements in elements_by_page.items():
        text_elements = [element for element in elements if element.get("text")]
        box_like = [element for element in elements if element.get("type") in {"box", "figure"}]

        for element in elements:
            if element.get("text"):
                block_role = classify_block_role(element, toc_pages, large_font_cutoff)
                element["block_role"] = block_role
                if block_role == "drop_cap":
                    element["type"] = "paragraph"
                    element["role"] = "drop_cap"
                    element["heading_source"] = None
                    element["heading_level"] = None
                elif block_role.endswith("_caption"):
                    element["role"] = block_role
                elif block_role == "chapter_number":
                    element["role"] = "chapter_number"
                elif block_role == "chapter_title":
                    element["role"] = "chapter_title"
                elif block_role == "box_text":
                    element["role"] = "box_text"
                elif block_role == "heading" and element.get("type") != "heading":
                    text_size = font_size(element.get("style", {})) or 0.0
                    if element["bbox"][1] < 125 or (large_font_cutoff and text_size >= large_font_cutoff):
                        element["type"] = "heading"
                        element["role"] = "inferred_heading"
                        element["heading_source"] = element.get("heading_source") or "postprocess"
                        element["heading_level"] = element.get("heading_level")
            elif element.get("type") == "box":
                element["block_role"] = "box"
                element["render_layer"] = "box_image"
            elif element.get("type") == "figure":
                element["block_role"] = "figure"
                element["render_layer"] = "figure_image"

        captions = [element for element in text_elements if str(element.get("block_role", "")).endswith("_caption")]
        for visual in box_like:
            caption_ids: list[str] = []
            for caption in captions:
                same_column = bbox_intersection_area(
                    [visual["bbox"][0], 0, visual["bbox"][2], 10],
                    [caption["bbox"][0], 0, caption["bbox"][2], 10],
                ) > 0
                gap_after = vertical_gap(visual["bbox"], caption["bbox"])
                gap_before = vertical_gap(caption["bbox"], visual["bbox"])
                if contains(visual["bbox"], caption["bbox"], tolerance=4.0) or (
                    same_column and (-12 <= gap_after <= 65 or -12 <= gap_before <= 65)
                ):
                    caption_ids.append(caption["_raw_id"])
            if caption_ids:
                visual["caption_element_ids"] = caption_ids
                if any(is_figure_caption(caption) for caption in captions if caption["_raw_id"] in caption_ids):
                    visual["type"] = "figure"
                    visual["role"] = "image"
                    visual["block_role"] = "figure"
                    visual["render_layer"] = "figure_image"
                    visual["source_format"] = visual.get("source_format", "png")
                    visual["alt_text"] = visual.get("alt_text", "")

        figure_visuals = [element for element in elements if element.get("type") == "figure"]
        for visual in elements:
            if visual.get("type") not in {"box", "figure"}:
                continue
            for figure in figure_visuals:
                if visual is figure:
                    continue
                if visual["page_number"] == figure["page_number"] and contains(figure["bbox"], visual["bbox"], tolerance=2.0):
                    visual["_drop_visual_region"] = True
                    break

        elements_by_page[page_number] = [element for element in elements if not element.get("_drop_visual_region")]
        elements = elements_by_page[page_number]
        text_elements = [element for element in elements if element.get("text")]
        box_like = [element for element in elements if element.get("type") in {"box", "figure"}]

        for text in text_elements:
            box_parents = [box["_raw_id"] for box in box_like if box.get("type") == "box" and contains(box["bbox"], text["bbox"], tolerance=3.0)]
            figure_parents = [
                figure["_raw_id"] for figure in box_like if figure.get("type") == "figure" and contains(figure["bbox"], text["bbox"], tolerance=3.0)
            ]
            if box_parents:
                text["parent_box_element_ids"] = box_parents
                if text.get("block_role") != "figure_caption":
                    text["block_role"] = "box_text"
                    text["role"] = "box_text"
            if figure_parents:
                text["parent_figure_element_ids"] = figure_parents
                if text.get("block_role") != "figure_caption":
                    text["block_role"] = "figure_text"
                    text["role"] = "figure_text"


def assign_elements(
    raw: list[dict[str, Any]],
    toc: list[TocEntry],
    page_sizes: dict[int, tuple[float, float]],
    band_ratio: float,
    toc_page_tolerance: int,
) -> dict[int, list[dict[str, Any]]]:
    raw = paragraphize_text_items(dedupe_drawn_regions(raw))
    repeated_margin = repeated_margin_text(raw, page_sizes, band_ratio)
    large_font_cutoff = infer_large_font_cutoff(raw)
    toc_pages = toc_by_page(toc, toc_page_tolerance)
    elements_by_page: dict[int, list[dict[str, Any]]] = defaultdict(list)

    text_items_by_page: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for item in raw:
        if item.get("kind") == "text":
            text_items_by_page[item["page_number"]].append(item)

    for item in sorted(raw, key=lambda x: (x["page_number"], x["bbox"][1], x["bbox"][0], x["block_index"])):
        page_number = item["page_number"]
        page_size = page_sizes[page_number]
        base = {
            "page_number": page_number,
            "bbox": item["bbox"],
            "render_bbox": expand_bbox(item["bbox"], page_size, padding=4.0 if item["kind"] == "text" else 0.0),
            "reading_order": len(elements_by_page[page_number]) + 1,
        }

        if item["kind"] == "text":
            classification = classify_text(
                item,
                page_size,
                repeated_margin,
                toc_pages.get(page_number, []),
                large_font_cutoff,
                band_ratio,
            )
            element = {
                **base,
                **classification,
                "_raw_id": pending_id(page_number, item),
                "text": item["text"],
                "text_hash": text_hash(item["text"]),
                "style": item.get("style", {}),
                "line_count": item.get("line_count", 1),
                "lines": item.get("lines", []),
                "block_role": classification["role"],
                "render_layer": "text",
            }
            if item.get("list_marker"):
                element["list_marker"] = item["list_marker"]
                element["list_kind"] = item.get("list_kind")
            if item.get("paragraph_preserves_line_breaks"):
                element["paragraph_preserves_line_breaks"] = True
        elif item["kind"] == "figure":
            element = {
                **base,
                "type": "figure",
                "filterable": False,
                "role": "image",
                "_raw_id": pending_id(page_number, item),
                "embedded_text": item["embedded_text"],
                "alt_text": item.get("alt_text", ""),
                "source_format": item.get("source_format", "png"),
                "block_role": "figure",
                "render_layer": "figure_image",
            }
        else:
            enclosed = [
                pending_id(page_number, text_item)
                for text_item in text_items_by_page[page_number]
                if contains(item["bbox"], text_item["bbox"])
            ]
            if not enclosed:
                continue
            element = {
                **base,
                "type": "box",
                "filterable": False,
                "role": "drawn_box",
                "_raw_id": pending_id(page_number, item),
                "embedded_text": item["embedded_text"],
                "child_text_element_ids": enclosed,
                "block_role": "box",
                "render_layer": "box_image",
            }
        elements_by_page[page_number].append(element)

    apply_text_relationship_roles(elements_by_page, toc, large_font_cutoff)

    for page_number, elements in elements_by_page.items():
        raw_to_element_id: dict[str, str] = {}
        for index, element in enumerate(elements, start=1):
            element["id"] = f"p{page_number:04d}_e{index:04d}"
            if element.get("_raw_id"):
                raw_to_element_id[element["_raw_id"]] = element["id"]
        for element in elements:
            if element.get("child_text_element_ids"):
                element["child_text_element_ids"] = [
                    raw_to_element_id.get(child_id, child_id) for child_id in element["child_text_element_ids"]
                ]
            if element.get("caption_element_ids"):
                element["caption_element_ids"] = [
                    raw_to_element_id.get(caption_id, caption_id) for caption_id in element["caption_element_ids"]
                ]
            if element.get("parent_box_element_ids"):
                element["parent_box_element_ids"] = [
                    raw_to_element_id.get(parent_id, parent_id) for parent_id in element["parent_box_element_ids"]
                ]
            if element.get("parent_figure_element_ids"):
                element["parent_figure_element_ids"] = [
                    raw_to_element_id.get(parent_id, parent_id) for parent_id in element["parent_figure_element_ids"]
                ]
            element.pop("_drop_visual_region", None)
            element.pop("_raw_id", None)

    return elements_by_page


def table_region_bbox(
    caption: dict[str, Any],
    elements: list[dict[str, Any]],
    page_size: tuple[float, float],
) -> tuple[list[float], list[str]]:
    width, height = page_size
    caption_y = caption["bbox"][1]
    content_top = caption["bbox"][3]
    page_bottom_limit = height * 0.92
    breaker_y = page_bottom_limit
    saw_content = False
    last_content_bottom = content_top

    for element in sorted(elements, key=lambda item: (item["bbox"][1], item["bbox"][0])):
        if element["id"] == caption["id"] or element.get("filterable"):
            continue
        if element["bbox"][1] <= content_top + 2:
            continue

        block_role = element.get("block_role", "")
        is_breaker = (
            block_role in {"table_caption", "figure_caption", "exhibit_caption", "chapter_title"}
            or element.get("type") == "heading"
        )
        if saw_content and is_breaker:
            breaker_y = min(breaker_y, max(caption["bbox"][3] + 2, element["bbox"][1] - 12))
            break

        if not saw_content and is_breaker:
            continue

        element_width = element["bbox"][2] - element["bbox"][0]
        prose_after_table = (
            saw_content
            and element.get("text")
            and element.get("block_role") == "body_text"
            and element["bbox"][0] >= 80
            and element_width >= width * 0.45
            and element["bbox"][1] - last_content_bottom >= 14
        )
        if prose_after_table:
            breaker_y = min(breaker_y, max(caption["bbox"][3] + 2, element["bbox"][1] - 8))
            break

        if element.get("text") or element.get("type") in {"box", "figure"}:
            saw_content = True
            last_content_bottom = max(last_content_bottom, element["bbox"][3])

    children = [
        element
        for element in elements
        if element["id"] != caption["id"]
        and not element.get("filterable")
        and element["bbox"][1] >= content_top - 2
        and element["bbox"][3] <= breaker_y + 2
        and element.get("block_role") not in {"figure_caption", "exhibit_caption", "chapter_title"}
    ]
    if not children:
        children = [
            element
            for element in elements
            if element["id"] != caption["id"]
            and not element.get("filterable")
            and element["bbox"][1] >= content_top - 2
            and element["bbox"][1] <= min(page_bottom_limit, content_top + height * 0.35)
        ]

    content_bbox = merge_bbox([caption["bbox"], *(child["bbox"] for child in children)])
    x0 = max(0.0, min(content_bbox[0], 54.0) - 4.0)
    x1 = min(width, max(content_bbox[2], width - 54.0) + 4.0)
    y0 = max(0.0, caption_y - 5.0)
    y1 = min(height, max(content_bbox[3] + 6.0, caption["bbox"][3] + 20.0))
    return [round(x0, 3), round(y0, 3), round(x1, 3), round(y1, 3)], [child["id"] for child in children if child.get("text")]


def add_table_screenshots(
    doc: Any,
    elements_by_page: dict[int, list[dict[str, Any]]],
    page_sizes: dict[int, tuple[float, float]],
    zoom: float,
) -> None:
    for page_number, elements in elements_by_page.items():
        captions = [
            element
            for element in elements
            if element.get("block_role") == "table_caption" and TABLE_CAPTION_RE.match((element.get("text") or "").strip())
        ]
        if not captions:
            continue

        additions: list[dict[str, Any]] = []
        page = doc[page_number - 1]
        for index, caption in enumerate(captions, start=1):
            bbox, child_ids = table_region_bbox(caption, elements, page_sizes[page_number])
            table_id = f"p{page_number:04d}_table_{index:04d}"
            additions.append(
                {
                    "page_number": page_number,
                    "bbox": bbox,
                    "render_bbox": bbox,
                    "reading_order": caption["reading_order"] + 0.1,
                    "type": "table",
                    "filterable": False,
                    "role": "table_screenshot",
                    "block_role": "table",
                    "render_layer": "figure_image",
                    "id": table_id,
                    "embedded_text": render_clip_to_data_uri(page, bbox, zoom),
                    "alt_text": caption.get("text", "Table"),
                    "caption_element_ids": [caption["id"]],
                    "child_text_element_ids": child_ids,
                    "source_format": "png",
                }
            )
            caption["parent_table_element_ids"] = [table_id]

        if additions:
            merged = sorted([*elements, *additions], key=lambda item: (item["reading_order"], item["bbox"][1], item["bbox"][0]))
            for order, element in enumerate(merged, start=1):
                element["reading_order"] = order
            elements_by_page[page_number] = merged


def pending_id(page_number: int, item: dict[str, Any]) -> str:
    return f"pending_p{page_number:04d}_b{item['block_index']:06d}"


def build_document(pdf_path: Path, zoom: float, band_ratio: float, toc_page_tolerance: int) -> dict[str, Any]:
    doc = fitz.open(pdf_path)
    toc = extract_toc(doc)
    page_sizes = {
        index: (float(page.rect.width), float(page.rect.height))
        for index, page in enumerate(doc, start=1)
    }
    raw = collect_raw_elements(doc, zoom)
    elements_by_page = assign_elements(raw, toc, page_sizes, band_ratio, toc_page_tolerance)
    add_table_screenshots(doc, elements_by_page, page_sizes, zoom)

    pages = []
    for page_number, page in enumerate(doc, start=1):
        pages.append(
            {
                "page_number": page_number,
                "width": round(float(page.rect.width), 3),
                "height": round(float(page.rect.height), 3),
                "elements": elements_by_page.get(page_number, []),
            }
        )

    return {
        "schema_version": "1.0",
        "source": {
            "path": str(pdf_path),
            "file_name": pdf_path.name,
            "page_count": doc.page_count,
            "metadata": doc.metadata,
        },
        "extraction": {
            "engine": "PyMuPDF",
            "figure_embedding": "data_uri_base64",
            "box_embedding": "rendered_clip_data_uri_base64",
            "header_footer_strategy": "repeated_margin_text",
            "heading_strategy": "toc_match_then_font_size_heuristic",
            "paragraph_strategy": "line_geometry_indent_gap_and_style",
            "header_footer_band_ratio": band_ratio,
            "toc_page_tolerance": toc_page_tolerance,
        },
        "toc": [
            {"level": entry.level, "title": entry.title, "page": entry.page}
            for entry in toc
        ],
        "pages": pages,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", nargs="?", default=DEFAULT_PDF, help="Path to the source PDF.")
    parser.add_argument("-o", "--output", default="book_extracted.json", help="Output JSON path.")
    parser.add_argument("--zoom", type=float, default=2.0, help="Render zoom for embedded box crops.")
    parser.add_argument(
        "--header-footer-band-ratio",
        type=float,
        default=0.09,
        help="Top/bottom page band used for header/footer detection.",
    )
    parser.add_argument(
        "--toc-page-tolerance",
        type=int,
        default=1,
        help="Pages around a TOC entry where its heading may be matched.",
    )
    parser.add_argument("--indent", type=int, default=2, help="JSON indentation. Use 0 for compact JSON.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdf_path = Path(args.pdf).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    document = build_document(
        pdf_path,
        zoom=args.zoom,
        band_ratio=args.header_footer_band_ratio,
        toc_page_tolerance=args.toc_page_tolerance,
    )

    output_path.write_text(
        json.dumps(document, ensure_ascii=False, indent=None if args.indent == 0 else args.indent),
        encoding="utf-8",
    )
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
