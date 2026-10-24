"""H1 dual annotation: check annotator files and pair annotator A with annotator B.

The format check covers only the codebook's form (pre-registration section 5): line count,
field order, keys and value vocabularies. It never judges content. Pairing uses the gate's
correspondence rule (one-to-one within a field, by normalised value text, in order of
appearance) and agreement on every comparison field.
"""

import json
import re
from collections import defaultdict
from dataclasses import dataclass, field, replace

from audit.lib.h1_quality import (
    COMPARISON_FIELDS,
    Annotated,
    correspondence_key,
    differing_fields,
)

RowId = tuple[str, str]  # (target_gene, evidence_id)

QUANTITIES: set[str | None] = {"logfc", "score", "pval", "padj", "n_pert", "n_ctrl", "n_sig",
                               "n_rows", "min_pval", "min_padj"}
RELATIONS: set[str | None] = {"=", "<", "<=", ">", ">="}
SCOPES: set[str | None] = {"gene", "cell", "target"}
UNITS = {None, "rows", "genes"}
SELF_INCLUSION = {None, "exclude", "include", "unstated"}
THRESHOLD_QUANTITIES = {None, "padj", "pval"}
THRESHOLD_RELATIONS = {None, "<", "<="}
LINE_KEYS = {"target_gene", "evidence_id", "assertions"}


def _check_assertion(a: object, cell_types: set[str], where: str) -> list[str]:
    if not isinstance(a, dict):
        return [f"{where}: assertion is not an object"]
    if set(a) != set(COMPARISON_FIELDS):
        return [f"{where}: keys {sorted(set(a) ^ set(COMPARISON_FIELDS))} wrong"]
    problems = []
    vocab: dict[str, set[str | None]] = {
        "quantity": QUANTITIES, "relation": RELATIONS, "scope": SCOPES, "unit": UNITS,
        "self_inclusion": SELF_INCLUSION, "threshold_quantity": THRESHOLD_QUANTITIES,
        "threshold_relation": THRESHOLD_RELATIONS}
    for name, allowed in vocab.items():
        if a[name] not in allowed:
            problems.append(f"{where}: {name}={a[name]!r} not allowed")
    if a["cell_type"] is not None and a["cell_type"] not in cell_types:
        problems.append(f"{where}: cell_type={a['cell_type']!r} not a listed label")
    if not isinstance(a["value_text"], str) or not a["value_text"].strip():
        problems.append(f"{where}: value_text must be a non-empty string")
    for name in ("gene", "threshold_text"):
        if a[name] is not None and not isinstance(a[name], str):
            problems.append(f"{where}: {name} must be a string or null")
    return problems


def check_format(lines: list[str], expected: list[RowId], cell_types: set[str]) -> list[str]:
    """Return every format problem of an annotator file (empty list if none)."""
    problems = []
    if len(lines) != len(expected):
        problems.append(f"{len(lines)} lines, expected {len(expected)}")
    for i, (line, row) in enumerate(zip(lines, expected, strict=False), start=1):
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as e:
            problems.append(f"line {i}: not JSON ({e.msg})")
            continue
        if not isinstance(obj, dict) or set(obj) != LINE_KEYS:
            problems.append(f"line {i}: keys must be {sorted(LINE_KEYS)}")
            continue
        if (obj["target_gene"], obj["evidence_id"]) != row:
            problems.append(f"line {i}: field {obj['target_gene']}/{obj['evidence_id']}, "
                            f"expected {row[0]}/{row[1]}")
        if not isinstance(obj["assertions"], list):
            problems.append(f"line {i}: assertions is not a list")
            continue
        for j, a in enumerate(obj["assertions"], start=1):
            problems.extend(_check_assertion(a, cell_types, f"line {i} assertion {j}"))
    return problems


def parse(lines: list[str]) -> dict[RowId, list[Annotated]]:
    """Annotations per field, in file order. Call only on a file that passed ``check_format``."""
    out: dict[RowId, list[Annotated]] = {}
    for line in lines:
        obj = json.loads(line)
        row = (obj["target_gene"], obj["evidence_id"])
        out[row] = [Annotated(row=row, **a) for a in obj["assertions"]]
    return out


@dataclass(frozen=True)
class FieldComparison:
    row: RowId
    agreed: list[tuple[Annotated, Annotated]] = field(default_factory=list)
    differing: list[tuple[Annotated, Annotated, list[str]]] = field(default_factory=list)
    only_a: list[Annotated] = field(default_factory=list)
    only_b: list[Annotated] = field(default_factory=list)

    @property
    def fully_agreed(self) -> bool:
        return not (self.differing or self.only_a or self.only_b)


def compare_field(row: RowId, a: list[Annotated], b: list[Annotated]) -> FieldComparison:
    """Pair A's and B's assertions of one field by the correspondence rule."""
    pool: dict[str, list[Annotated]] = defaultdict(list)
    for got in b:
        pool[correspondence_key(got)].append(got)
    result = FieldComparison(row=row)
    paired_b: set[int] = set()
    for gold in a:
        candidates = pool[correspondence_key(gold)]
        if not candidates:
            result.only_a.append(gold)
            continue
        other = candidates.pop(0)
        paired_b.add(id(other))
        diff = differing_fields(gold, other)
        if diff:
            result.differing.append((gold, other, diff))
        else:
            result.agreed.append((gold, other))
    result.only_b.extend(x for x in b if id(x) not in paired_b)
    return result


def agreement_summary(comparisons: list[FieldComparison]) -> dict[str, float | int]:
    """Counts for the pre-registered A-B agreement report. ``assertion_agreement`` is agreed
    pairs over the union of assertions (agreed + differing pairs + unpaired of either side)."""
    agreed = sum(len(c.agreed) for c in comparisons)
    differing = sum(len(c.differing) for c in comparisons)
    only_a = sum(len(c.only_a) for c in comparisons)
    only_b = sum(len(c.only_b) for c in comparisons)
    union = agreed + differing + only_a + only_b
    fully = sum(c.fully_agreed for c in comparisons)
    return {
        "fields": len(comparisons),
        "fields_fully_agreed": fully,
        "field_agreement": fully / len(comparisons) if comparisons else 0.0,
        "assertions_a": agreed + differing + only_a,
        "assertions_b": agreed + differing + only_b,
        "pairs_agreed": agreed,
        "pairs_differing": differing,
        "only_a": only_a,
        "only_b": only_b,
        "assertion_agreement": agreed / union if union else 1.0,
    }


def include_as_unstated(annotations: list[Annotated], statistics: str, target: str
                        ) -> list[Annotated]:
    """Reporting view of the self-inclusion label convention (pre-registration section 5,
    revision 13): ``include`` is read as ``unstated`` unless the field's text says "including
    the target/<Target>". Used only for the second A-B agreement figure."""
    explicit = rf"(?i)\bincluding\s+(?:the\s+)?(?:target|{re.escape(target)})\b"
    if re.search(explicit, statistics):
        return list(annotations)
    return [replace(a, self_inclusion="unstated") if a.self_inclusion == "include" else a
            for a in annotations]
