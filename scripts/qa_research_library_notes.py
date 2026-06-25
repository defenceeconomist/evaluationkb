#!/usr/bin/env python3
"""QA checks for generated MCP research-library notes."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "research_library_notes_manifest.json"
REFERENCES = ROOT / "references.bib"
REQUIRED_HEADINGS = {"## Source", "## References"}


def front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta


def add(issues: dict[str, list[str]], category: str, message: str) -> None:
    issues[category].append(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    issues: dict[str, list[str]] = defaultdict(list)
    if not MANIFEST.exists():
        add(issues, "manifest", f"Missing {MANIFEST.relative_to(ROOT)}")
        return report(issues)

    manifest = load_json(MANIFEST)
    references = REFERENCES.read_text(encoding="utf-8") if REFERENCES.exists() else ""
    seen_slugs: set[str] = set()
    seen_targets: set[str] = set()

    for book in manifest.get("books", []):
        slug = book.get("slug", "")
        generated = book.get("generation_mode") != "existing-hand-authored"
        if slug in seen_slugs:
            add(issues, "manifest", f"Duplicate slug {slug}")
        seen_slugs.add(slug)

        citation = book.get("citation", "")
        if citation and f"{{{citation}," not in references:
            add(issues, "references", f"Missing BibTeX entry for {citation}")

        evidence_path = ROOT / "data" / "research-library" / "evidence" / slug / "evidence-summary.json"
        if not evidence_path.exists():
            add(issues, "evidence", f"Missing evidence summary for {slug}")
            evidence_ids: set[str] = set()
        else:
            evidence = load_json(evidence_path)
            evidence_ids = {
                evidence_id
                for record in evidence.get("records", [])
                for evidence_id in record.get("evidence_ids", [])
            }

        target_paths = [book.get("target_path", "")]
        target_paths.extend(section.get("target_path", "") for section in book.get("sections", []))
        for target in filter(None, target_paths):
            if target in seen_targets:
                add(issues, "manifest", f"Duplicate target {target}")
            seen_targets.add(target)
            path = ROOT / target
            if not path.exists():
                add(issues, "files", f"Missing target {target}")
                continue
            text = path.read_text(encoding="utf-8")
            meta = front_matter(text)
            if not meta:
                add(issues, "front_matter", f"Missing or invalid front matter in {target}")
            elif generated and meta.get("citation_key") != citation:
                add(issues, "front_matter", f"Unexpected citation_key in {target}: {meta.get('citation_key')}")
            required_headings = REQUIRED_HEADINGS if generated else {"## References"}
            for heading in required_headings:
                if heading not in text:
                    add(issues, "content", f"{target} missing {heading}")
            if re.search(r"\bTODO\b|FIXME|TBD", text):
                add(issues, "content", f"{target} contains placeholder text")

        for section in book.get("sections", []):
            for evidence_id in section.get("evidence_ids", []):
                if evidence_ids and evidence_id not in evidence_ids:
                    add(issues, "evidence", f"{slug} manifest evidence id not in summary: {evidence_id}")

    return report(issues)


def report(issues: dict[str, list[str]]) -> int:
    total = sum(len(values) for values in issues.values())
    print(f"Research-library notes QA: {total} issue(s)")
    for category in sorted(issues):
        print(f"\n[{category}] {len(issues[category])}")
        for message in issues[category]:
            print(f"- {message}")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
