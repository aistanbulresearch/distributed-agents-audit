"""Tally the owner's hand check of the H1 annotation (sample 1, 30 fields).

Run: uv run python -m audit.scripts.h1_owner_check_tally <filled_check.md> <out.json>

Parses the filled check sheet: for each field, the verdict cell of every annotated
assertion (✓, ✓* conditional, ✗) and the rows of any "Missed" table. Reads no DE data.
"""

import json
import logging
import re
import sys
from collections import Counter
from pathlib import Path

logger = logging.getLogger(__name__)

_FIELD = re.compile(r"^## (\d+)\. (\S+) / (\S+)", re.M)


def _rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        if line.startswith("|") and not line.startswith("|---"):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


def tally(text: str) -> dict:
    fields = list(_FIELD.finditer(text))
    per_field = []
    totals: Counter[str] = Counter()
    for i, m in enumerate(fields):
        block = text[m.end():fields[i + 1].start() if i + 1 < len(fields) else len(text)]
        annotated, _, missed_part = block.partition("**Missed:**")
        verdicts: Counter[str] = Counter()
        for row in _rows(annotated):
            if row[0] == "#":
                continue
            verdict = row[-1]
            key = ("conditional" if verdict.startswith("✓*") else
                   "correct" if verdict.startswith("✓") else
                   "wrong" if verdict.startswith("✗") else "blank")
            verdicts[key] += 1
        missed = [r for r in _rows(missed_part) if r[0] != "quantity"]
        totals.update(verdicts)
        totals["missed_rows"] += len(missed)
        per_field.append({"field": int(m.group(1)), "target_gene": m.group(2),
                          "evidence_id": m.group(3), **verdicts, "missed_rows": len(missed),
                          "has_scope_note": "Kapsamı doğrulanacak" in block
                          or "Belirsiz" in block or "Kod kitabına bağlı" in block})
    return {"fields": len(fields), "totals": dict(totals), "per_field": per_field}


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    source, out = Path(sys.argv[1]), Path(sys.argv[2])
    result = tally(source.read_text(encoding="utf-8"))
    out.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n", encoding="utf-8",
                   newline="\n")
    logger.info("wrote %s: %s", out, result["totals"])


if __name__ == "__main__":
    main()
