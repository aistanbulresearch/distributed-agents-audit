"""Helpers for reading agent reports (Markdown with fenced JSONL appendix blocks)."""

import json
import re
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

_FENCE = re.compile(r"^```")


@dataclass
class JsonlBlock:
    rows: list[dict] = field(default_factory=list)
    n_invalid: int = 0


def iter_jsonl(path: Path) -> Iterator[dict]:
    """Yield one JSON object per non-empty line."""
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def extract_jsonl_block(report: str, heading: str) -> JsonlBlock | None:
    """Parse the first fenced block after a heading line containing ``heading``.

    Returns None if the heading or its fenced block is absent. Lines that are not
    JSON objects are counted in ``n_invalid`` rather than raised.
    """
    lines = report.splitlines()
    start = next(
        (i for i, line in enumerate(lines) if line.lstrip().startswith("#") and heading in line),
        None,
    )
    if start is None:
        return None
    open_at = next((i for i in range(start + 1, len(lines)) if _FENCE.match(lines[i])), None)
    if open_at is None:
        return None
    block = JsonlBlock()
    for line in lines[open_at + 1:]:
        if _FENCE.match(line):
            break
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            block.n_invalid += 1
            continue
        if isinstance(value, dict):
            block.rows.append(value)
        else:
            block.n_invalid += 1
    return block


def url_host(url: str) -> str:
    """Lower-cased host without a leading ``www.``; empty string if not an HTTP(S) URL."""
    parsed = urlparse(url.strip())
    if parsed.scheme.lower() not in ("http", "https") or not parsed.netloc:
        return ""
    host = parsed.netloc.lower().split("@")[-1].split(":")[0]
    return host.removeprefix("www.")
