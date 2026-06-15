#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

EXCLUDE_PARTS = {'.quarto', '_site', 'site_libs', 'assets', 'data', 'scripts'}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CITE_RE = re.compile(r"(?<![\w/])@([A-Za-z0-9_:.+-]+)")


def parse_args():
    p = argparse.ArgumentParser(description='Build a small notes link graph payload for Quarto pages.')
    p.add_argument('--root', type=Path, default=Path('.'))
    p.add_argument('--output', type=Path, default=Path('data/notes_link_graph_payload.json'))
    p.add_argument('--include-prefix', action='append', default=[])
    return p.parse_args()


def front_matter(text: str):
    if not text.startswith('---\n'):
        return {}, text
    end = text.find('\n---\n', 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5:]
    meta = {}
    for line in raw.splitlines():
        if ':' in line and not line.startswith(' '):
            key, value = line.split(':', 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta, body


def title_from_path(path: Path):
    if path.name == 'index.qmd':
        return path.parent.name.replace('-', ' ').title() if path.parent.name != '.' else 'Home'
    return path.stem.replace('-', ' ').title()


def allowed(rel: Path, prefixes: list[str]):
    if any(part in EXCLUDE_PARTS for part in rel.parts):
        return False
    if not prefixes:
        return True
    rels = rel.as_posix()
    cleaned = [p.strip().lstrip('./').rstrip('/') for p in prefixes if p.strip()]
    return any(rels == p or rels.startswith(p + '/') for p in cleaned)


def normalize_target(root: Path, source_rel: Path, target: str):
    target = target.strip().strip('<>').split('#', 1)[0].split('?', 1)[0]
    if not target or target.startswith(('http://', 'https://', 'mailto:')):
        return None
    candidate = (root / source_rel.parent / target).resolve()
    try:
        rel = candidate.relative_to(root.resolve())
    except ValueError:
        return None
    if rel.suffix == '.html':
        rel = rel.with_suffix('.qmd')
    return rel.as_posix() if rel.suffix == '.qmd' else None


def main():
    args = parse_args()
    root = args.root.resolve()
    nodes = []
    paths = []
    for path in sorted(root.rglob('*.qmd')):
        rel = path.relative_to(root)
        if allowed(rel, args.include_prefix):
            paths.append(path)
    path_set = {p.relative_to(root).as_posix() for p in paths}
    edges = []
    citations = []
    for path in paths:
        rel = path.relative_to(root)
        text = path.read_text(encoding='utf-8')
        meta, body = front_matter(text)
        node_id = rel.as_posix()
        nodes.append({'id': node_id, 'title': meta.get('title') or title_from_path(rel), 'path': node_id})
        for link in LINK_RE.findall(body):
            target = normalize_target(root, rel, link)
            if target and target in path_set:
                edges.append({'source': node_id, 'target': target, 'type': 'internal-link'})
        for cite in sorted(set(CITE_RE.findall(body))):
            citations.append({'source': node_id, 'citation': cite})
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({'nodes': nodes, 'edges': edges, 'citations': citations}, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
