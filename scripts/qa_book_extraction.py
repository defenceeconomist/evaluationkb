#!/usr/bin/env python3
"""Quality checks for the extracted book JSON."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


CAPTION_RE = re.compile(r"^(figure|fig\.|table|exhibit)\s+\d+(?:\.\d+)?\b", re.I)


def normalize(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "").strip().lower()
    return re.sub(r"^[\W_]+|[\W_]+$", "", value)


def normalize_compact(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def bbox_area(bbox: Iterable[float]) -> float:
    x0, y0, x1, y1 = bbox
    return max(0.0, x1 - x0) * max(0.0, y1 - y0)


def bbox_intersection_area(first: Iterable[float], second: Iterable[float]) -> float:
    ax0, ay0, ax1, ay1 = first
    bx0, by0, bx1, by1 = second
    return max(0.0, min(ax1, bx1) - max(ax0, bx0)) * max(0.0, min(ay1, by1) - max(ay0, by0))


def bbox_similarity(first: Iterable[float], second: Iterable[float]) -> float:
    intersection = bbox_intersection_area(first, second)
    union = bbox_area(first) + bbox_area(second) - intersection
    return intersection / union if union else 0.0


def contains(outer: Iterable[float], inner: Iterable[float], tolerance: float = 1.0) -> bool:
    ox0, oy0, ox1, oy1 = outer
    ix0, iy0, ix1, iy1 = inner
    return (
        ox0 - tolerance <= ix0
        and oy0 - tolerance <= iy0
        and ox1 + tolerance >= ix1
        and oy1 + tolerance >= iy1
    )


def element_label(element: dict[str, Any]) -> str:
    text = (element.get("text") or "").replace("\n", " ")
    return f"p{element['page_number']} {element['id']} {element['type']} {element.get('block_role', '')}: {text[:90]}"


def horizontally_near(first: Iterable[float], second: Iterable[float]) -> bool:
    ax0, _, ax1, _ = first
    bx0, _, bx1, _ = second
    return max(0.0, min(ax1, bx1) - max(ax0, bx0)) > 0


def vertical_distance(first: Iterable[float], second: Iterable[float]) -> float:
    return min(abs(second[1] - first[3]), abs(first[1] - second[3]))


def nearby_visuals(caption: dict[str, Any], visuals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        visual
        for visual in visuals
        if contains(visual["bbox"], caption["bbox"], tolerance=4.0)
        or (horizontally_near(caption["bbox"], visual["bbox"]) and vertical_distance(caption["bbox"], visual["bbox"]) <= 65)
    ]


def add(issue_map: dict[str, list[str]], category: str, message: str) -> None:
    issue_map[category].append(message)


def check_document(data: dict[str, Any]) -> dict[str, list[str]]:
    issues: dict[str, list[str]] = defaultdict(list)
    all_ids: set[str] = set()
    duplicate_ids: set[str] = set()
    headings_by_page: dict[int, list[dict[str, Any]]] = defaultdict(list)
    elements_by_page: dict[int, list[dict[str, Any]]] = {}

    for page in data.get("pages", []):
        elements = page.get("elements", [])
        elements_by_page[page["page_number"]] = elements
        page_ids = {element.get("id") for element in elements if element.get("id")}
        for element in elements:
            element_id = element.get("id")
            if not element_id:
                add(issues, "schema", f"p{page['page_number']} element missing id")
            elif element_id in all_ids:
                duplicate_ids.add(element_id)
            else:
                all_ids.add(element_id)

            for field in ("bbox", "render_bbox", "type", "role", "reading_order", "block_role"):
                if field not in element:
                    add(issues, "schema", f"{element_label(element)} missing {field}")

            if element.get("type") == "heading":
                headings_by_page[page["page_number"]].append(element)

            heading_size = float((element.get("style") or {}).get("font_size") or 0)
            heading_height = element.get("bbox", [0, 0, 0, 0])[3] - element.get("bbox", [0, 0, 0, 0])[1]
            if (
                element.get("type") == "heading"
                and re.fullmatch(r"[A-Za-z]", (element.get("text") or "").strip())
                and (heading_size >= 20 or heading_height >= 28)
            ):
                add(issues, "drop_caps", f"one-letter heading likely drop cap: {element_label(element)}")

            if element.get("block_role") == "drop_cap" and element.get("type") == "heading":
                add(issues, "drop_caps", f"drop cap still typed as heading: {element_label(element)}")

            if element.get("text") and re.search(r"[A-Za-z0-9]", element.get("text", "")) and element.get("line_count", 1) > 1:
                bbox = element.get("bbox", [0, 0, 0, 0])
                style = element.get("style") or {}
                font_size = float(style.get("font_size") or 10)
                expected_height = element.get("line_count", 1) * font_size * 1.12
                actual_height = bbox[3] - bbox[1]
                if actual_height < expected_height * 0.75:
                    add(issues, "text_geometry", f"tight text bbox may crop in viewer: {element_label(element)}")

            if element.get("type") == "box" and not element.get("child_text_element_ids"):
                add(issues, "boxes", f"box has no child text: {element_label(element)}")

            for relation_field in ("child_text_element_ids", "caption_element_ids", "parent_box_element_ids"):
                for related_id in element.get(relation_field, []):
                    if related_id not in page_ids:
                        add(issues, "relationships", f"{element_label(element)} has unresolved {relation_field}: {related_id}")

        boxes = [element for element in elements if element.get("type") == "box"]
        for index, first in enumerate(boxes):
            for second in boxes[index + 1 :]:
                if bbox_similarity(first["bbox"], second["bbox"]) >= 0.97:
                    add(issues, "boxes", f"duplicate boxes: {element_label(first)} overlaps {second['id']}")
                elif contains(first["bbox"], second["bbox"]) and bbox_area(second["bbox"]) / max(1.0, bbox_area(first["bbox"])) > 0.92:
                    add(issues, "boxes", f"near-duplicate nested boxes: {element_label(first)} contains {second['id']}")

        id_map = {element["id"]: element for element in elements if element.get("id")}
        for box in boxes:
            for child_id in box.get("child_text_element_ids", []):
                child = id_map.get(child_id)
                if child and not contains(box["bbox"], child["bbox"], tolerance=4.0):
                    add(issues, "boxes", f"box child outside parent: {box['id']} child {child_id}")

        captions = [element for element in elements if element.get("block_role") == "figure_caption" or CAPTION_RE.match(element.get("text") or "")]
        visuals = [element for element in elements if element.get("type") in {"box", "figure"}]
        for caption in captions:
            candidates = nearby_visuals(caption, visuals)
            if candidates and not any(caption["id"] in visual.get("caption_element_ids", []) for visual in candidates):
                add(issues, "captions", f"nearby caption not linked to visual: {element_label(caption)}")
        for visual in visuals:
            if visual.get("type") == "figure" and visual["page_number"] > 1 and bbox_area(visual["bbox"]) > 5000 and not visual.get("caption_element_ids"):
                add(issues, "captions", f"figure has no linked caption: {element_label(visual)}")

    if duplicate_ids:
        for element_id in sorted(duplicate_ids):
            add(issues, "schema", f"duplicate id: {element_id}")

    for toc_entry in data.get("toc", []):
        page_number = toc_entry.get("page")
        title = normalize(toc_entry.get("title", ""))
        if not title:
            continue
        candidates = headings_by_page.get(page_number, []) + headings_by_page.get(page_number - 1, []) + headings_by_page.get(page_number + 1, [])
        compact_title = normalize_compact(title)
        if not any(
            title in normalize(candidate.get("text", ""))
            or normalize(candidate.get("text", "")) in title
            or normalize_compact(candidate.get("text", "")) == compact_title
            for candidate in candidates
        ):
            add(issues, "headings", f"TOC heading not found near p{page_number}: {toc_entry.get('title')}")

    return dict(issues)


def print_report(issues: dict[str, list[str]], max_per_category: int) -> int:
    total = sum(len(values) for values in issues.values())
    print(f"Extraction QA report: {total} issue(s)")
    for category in sorted(issues):
        values = issues[category]
        print(f"\n[{category}] {len(values)}")
        for message in values[:max_per_category]:
            print(f"- {message}")
        if len(values) > max_per_category:
            print(f"- ... {len(values) - max_per_category} more")
    return 1 if issues else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_path", nargs="?", default="book_extracted.json", help="Path to extracted JSON.")
    parser.add_argument("--max-per-category", type=int, default=25, help="Maximum issue lines printed per category.")
    parser.add_argument("--fail-on-issues", action="store_true", help="Exit non-zero if any QA issue is found.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    issues = check_document(data)
    exit_code = print_report(issues, args.max_per_category)
    if args.fail_on_issues and exit_code:
        raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
