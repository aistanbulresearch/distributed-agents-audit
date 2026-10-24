"""Read the owner's filled H1 adjudication and agreement-audit forms (pre-registration §5).

Every assertion row ends in a ruling: ``✓`` keeps the row as shown, ``✗ <reason>`` drops it,
``✗ → field=value; ...`` replaces the named fields. Rows under **Missed by both** are added.
The resolved field is the kept and corrected rows, in form order, followed by the added rows.
"""

import re
from dataclasses import dataclass, field, replace
from typing import Any

from audit.lib.h1_quality import Annotated

RowId = tuple[str, str]

_FIELD = re.compile(r"^## (\d+)\. (\S+) / (\S+)$", re.M)
_MISSED = "**Missed by both**"
# Form column names → Annotated attributes (correction keys use the column names).
_ALIASES = {"quantity": "quantity", "rel": "relation", "relation": "relation",
            "value": "value_text", "value_text": "value_text", "cell type": "cell_type",
            "cell_type": "cell_type", "gene": "gene", "scope": "scope", "unit": "unit",
            "self": "self_inclusion", "self_inclusion": "self_inclusion",
            "threshold_quantity": "threshold_quantity",
            "threshold_relation": "threshold_relation", "threshold_text": "threshold_text"}
_THRESHOLD = re.compile(r"^(padj|pval) (<=|<) (\S+)$")


class RulingError(ValueError):
    """A ruling or added row that cannot be read unambiguously."""


@dataclass
class RuledField:
    row: RowId
    kept: list[Annotated] = field(default_factory=list)
    dropped: list[tuple[Annotated, str]] = field(default_factory=list)
    corrected: list[tuple[Annotated, Annotated]] = field(default_factory=list)
    added: list[Annotated] = field(default_factory=list)
    resolved: list[Annotated] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return bool(self.dropped or self.corrected or self.added)


def _none(cell: str) -> str | None:
    return None if cell in ("—", "-", "") else cell


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _annotated(row: RowId, c: list[str]) -> Annotated:
    """``c`` = quantity, rel, value, cell type, gene, scope, unit, self, threshold."""
    threshold = _none(c[8])
    tq = tr = tt = None
    if threshold is not None:
        m = _THRESHOLD.match(threshold)
        if not m:
            raise RulingError(f"{row}: unreadable threshold {threshold!r}")
        tq, tr, tt = m.groups()
    return Annotated(row=row, quantity=c[0], relation=c[1], value_text=c[2],
                     cell_type=_none(c[3]), gene=_none(c[4]), scope=c[5], unit=_none(c[6]),
                     self_inclusion=_none(c[7]), threshold_quantity=tq,
                     threshold_relation=tr, threshold_text=tt)


def _correct(a: Annotated, text: str) -> Annotated:
    body = text.split("→", 1)[1]
    body = re.sub(r"(?i)[;.]?\s*all other fields unchanged\.?\s*$", "", body.strip())
    changes: dict[str, Any] = {}
    for part in filter(None, (p.strip() for p in body.split(";"))):
        key, sep, value = part.partition("=")
        name = _ALIASES.get(key.strip().lower())
        if not sep or name is None:
            raise RulingError(f"{a.row}: unreadable correction {part!r}")
        changes[name] = _none(value.strip())
    if not changes:
        raise RulingError(f"{a.row}: empty correction {text!r}")
    return replace(a, **changes)


def parse_form(text: str, *, sourced: bool) -> dict[RowId, RuledField]:
    """Parse a filled form. ``sourced`` is True for adjudication forms (a source and a
    *differs* column before the ruling), False for agreement-audit forms."""
    heads = list(_FIELD.finditer(text))
    out: dict[RowId, RuledField] = {}
    for i, m in enumerate(heads):
        row = (m.group(2), m.group(3))
        block = text[m.end():heads[i + 1].start() if i + 1 < len(heads) else len(text)]
        rows_part, _, missed_part = block.partition(_MISSED)
        ruled = RuledField(row=row)
        for line in rows_part.splitlines():
            if not re.match(r"^\| \d+ \|", line):
                continue
            c = _cells(line)
            values = c[2:11] if sourced else c[1:10]
            ruling = c[-1]
            a = _annotated(row, values)
            if ruling == "✓":
                ruled.kept.append(a)
                ruled.resolved.append(a)
            elif ruling.startswith("✗") and "→" in ruling:
                fixed = _correct(a, ruling)
                ruled.corrected.append((a, fixed))
                ruled.resolved.append(fixed)
            elif ruling.startswith("✗"):
                ruled.dropped.append((a, ruling[1:].strip()))
            else:
                raise RulingError(f"{row}: row without a ruling: {line}")
        for line in missed_part.splitlines():
            c = _cells(line) if line.startswith("|") else []
            if len(c) == 9 and c[0] not in ("quantity",) and not c[0].startswith("---"):
                added = _annotated(row, c)
                ruled.added.append(added)
                ruled.resolved.append(added)
        out[row] = ruled
    return out
