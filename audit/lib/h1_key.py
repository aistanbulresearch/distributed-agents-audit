"""Assemble the resolved H1 annotation keys (pre-registration section 5).

Each sampled field gets its assertions from exactly one source: the owner's 30-field check
(sample 1), the whole-field adjudication, the agreement audit, the DC-33 review of remaining
agreed fields, or, for agreed fields that no review covered, the annotators' identical
annotation. A field covered twice or not at all is an error.
"""

import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import asdict

from audit.lib.h1_quality import Annotated
from audit.lib.h1_rulings import RuledField, parse_form

RowId = tuple[str, str]

_RULED_ROW = re.compile(r"^(\| \d+ \|.*\| )(✓\*?)[^|]*(\|)$")


def normalise_owner_check(text: str) -> str:
    """Rewrite the owner-check sheet into the ruled-form layout: its "Missed" heading becomes
    "Missed by both", and every ✓ or ✓* verdict (✓* = conditionally correct, accepted by
    decision DC-27) becomes ✓. ✗ verdicts are left as they are."""
    lines = []
    for line in text.replace("**Missed:**", "**Missed by both**").splitlines():
        m = _RULED_ROW.match(line)
        lines.append(f"{m.group(1)}✓ {m.group(3)}" if m else line)
    return "\n".join(lines) + "\n"


def resolve_owner_check(ruled: Mapping[RowId, RuledField], *, add_missed: set[RowId],
                        remove: Mapping[RowId, Iterable[tuple[str, str]]],
                        extra: Mapping[RowId, list[Annotated]]) -> dict[RowId, list[Annotated]]:
    """The owner's resolution of the checked fields: kept rows minus ``remove`` (quantity,
    value_text), plus the owner's missed rows only for fields in ``add_missed``, plus
    ``extra`` rows the decisions add."""
    out: dict[RowId, list[Annotated]] = {}
    for row, f in ruled.items():
        drop = set(remove.get(row, ()))
        kept = [a for a in f.kept if (a.quantity, a.value_text) not in drop]
        if len(f.kept) - len(kept) != len(drop):
            raise ValueError(f"{row}: rows to remove not found exactly once")
        if f.corrected:
            raise ValueError(f"{row}: corrections are not used in the owner check")
        out[row] = kept + (f.added if row in add_missed else []) + extra.get(row, [])
    return out


def merge_sources(expected: list[RowId], sources: Mapping[str, Mapping[RowId, list[Annotated]]]
                  ) -> tuple[dict[RowId, list[Annotated]], dict[RowId, str]]:
    """One assertion list per expected field, in sample order, and the source of each."""
    key: dict[RowId, list[Annotated]] = {}
    origin: dict[RowId, str] = {}
    for name, part in sources.items():
        for row, assertions in part.items():
            if row in origin:
                raise ValueError(f"{row}: covered by {origin[row]} and {name}")
            if row not in expected:
                raise ValueError(f"{row}: not in the sample ({name})")
            key[row], origin[row] = assertions, name
    missing = [row for row in expected if row not in key]
    if missing:
        raise ValueError(f"fields without a source: {missing[:5]}")
    return {row: key[row] for row in expected}, {row: origin[row] for row in expected}


def key_lines(key: Mapping[RowId, list[Annotated]]) -> list[str]:
    """JSON lines in the annotators' format (one field per line, key order)."""
    return [json.dumps({"target_gene": row[0], "evidence_id": row[1],
                        "assertions": [{k: v for k, v in asdict(a).items() if k != "row"}
                                       for a in assertions]}, ensure_ascii=False)
            for row, assertions in key.items()]


def resolved(fields: Mapping[RowId, RuledField]) -> dict[RowId, list[Annotated]]:
    return {row: f.resolved for row, f in fields.items()}


def parse_owner_check(text: str) -> dict[RowId, RuledField]:
    return parse_form(normalise_owner_check(text), sourced=False)


def target_minimum(row: RowId, quantity: str, value: str) -> Annotated:
    """A minimum without gene or cell type (type E at target scope)."""
    return Annotated(row=row, quantity=quantity, relation="=", value_text=value,
                     cell_type=None, gene=None, scope="target", unit=None,
                     self_inclusion=None, threshold_quantity=None, threshold_relation=None,
                     threshold_text=None)
