"""H1 extraction-quality gate: compare extracted assertions with an independent annotation.

Correspondence is one-to-one within an evidence row, by normalised value text in order of
appearance. A corresponding pair counts as correctly bound only if every comparison-relevant
field agrees. Thresholds are those of the H1 pre-registration, section 5.
"""

from collections import defaultdict
from dataclasses import dataclass, field, fields

from audit.lib.h1_extract import Assertion
from audit.lib.h1_match import normalise_number
from audit.lib.h1_stats import cluster_bootstrap_ratio

COMPARISON_FIELDS = (
    "quantity", "relation", "value_text", "cell_type", "gene", "scope", "unit",
    "self_inclusion", "threshold_quantity", "threshold_relation", "threshold_text",
)
RECALL_MIN = 0.90
RECALL_PER_TYPE_MIN = 0.80
PER_TYPE_MIN_INSTANCES = 20
PRECISION_MIN = 0.95
BINDING_MIN = 0.95


@dataclass(frozen=True)
class Annotated:
    row: tuple[str, str]  # (target_gene, evidence_id)
    quantity: str
    relation: str
    value_text: str
    cell_type: str | None
    gene: str | None
    scope: str
    unit: str | None
    self_inclusion: str | None
    threshold_quantity: str | None
    threshold_relation: str | None
    threshold_text: str | None


@dataclass
class QualityReport:
    recall: float
    precision: float
    binding_accuracy: float
    n_annotated: int
    n_extracted: int
    n_pairs: int
    recall_by_type: dict[str, float]
    types_checked: set[str]
    disagreements: list[dict] = field(default_factory=list)
    # Per annotated field (evidence row): annotated, extracted, pairs, agree counts.
    per_row: dict[tuple[str, str], dict[str, int]] = field(default_factory=dict)


def from_assertion(row: tuple[str, str], a: Assertion) -> Annotated:
    """Project an extracted assertion onto the annotation schema."""
    names = {f.name for f in fields(Annotated)} - {"row"}
    return Annotated(row=row, **{name: getattr(a, name) for name in names})


def assertion_type(a: Annotated) -> str:
    if a.quantity in ("logfc", "score", "pval", "padj"):
        return "A" if a.relation in ("=", ":") else "A'"
    return {"n_pert": "B", "n_ctrl": "B", "n_sig": "C", "n_rows": "D",
            "min_pval": "E", "min_padj": "E"}.get(a.quantity, "other")


def correspondence_key(a: Annotated) -> str:
    return normalise_number(a.value_text).lower()


def differing_fields(gold: Annotated, got: Annotated) -> list[str]:
    def norm(name: str, value: object) -> object:
        if name.endswith("text") and isinstance(value, str) and value:
            return normalise_number(value).lower()
        return value
    return [n for n in COMPARISON_FIELDS if norm(n, getattr(gold, n)) != norm(n, getattr(got, n))]


def evaluate(annotated: list[Annotated], extracted: list[Annotated]) -> QualityReport:
    pool: dict[tuple[tuple[str, str], str], list[Annotated]] = defaultdict(list)
    for got in extracted:
        pool[(got.row, correspondence_key(got))].append(got)
    pairs: list[tuple[Annotated, Annotated]] = []
    found_by_type: dict[str, int] = defaultdict(int)
    total_by_type: dict[str, int] = defaultdict(int)
    for gold in annotated:
        total_by_type[assertion_type(gold)] += 1
        candidates = pool[(gold.row, correspondence_key(gold))]
        if candidates:
            pairs.append((gold, candidates.pop(0)))
            found_by_type[assertion_type(gold)] += 1
    disagreements = []
    per_row: dict[tuple[str, str], dict[str, int]] = defaultdict(
        lambda: {"annotated": 0, "extracted": 0, "pairs": 0, "agree": 0})
    for gold in annotated:
        per_row[gold.row]["annotated"] += 1
    for got in extracted:
        per_row[got.row]["extracted"] += 1
    for gold, got in pairs:
        per_row[gold.row]["pairs"] += 1
        diff = differing_fields(gold, got)
        if diff:
            disagreements.append({"row": gold.row, "value_text": gold.value_text, "fields": diff})
        else:
            per_row[gold.row]["agree"] += 1
    n_pairs = len(pairs)
    return QualityReport(
        recall=n_pairs / len(annotated) if annotated else 1.0,
        precision=n_pairs / len(extracted) if extracted else (1.0 if not annotated else 0.0),
        binding_accuracy=(n_pairs - len(disagreements)) / n_pairs if n_pairs else 0.0,
        n_annotated=len(annotated),
        n_extracted=len(extracted),
        n_pairs=n_pairs,
        recall_by_type={t: found_by_type[t] / n for t, n in total_by_type.items()},
        types_checked={t for t, n in total_by_type.items() if n >= PER_TYPE_MIN_INSTANCES},
        disagreements=disagreements,
        per_row=dict(per_row),
    )


def gate_intervals(report: QualityReport) -> dict[str, tuple[float, float, float]]:
    """Recall, precision and binding accuracy as (estimate, lower, upper), with intervals from
    the frozen cluster bootstrap over annotated fields (errors cluster within a field)."""
    rows = report.per_row.values()
    return {
        "recall": cluster_bootstrap_ratio([(r["pairs"], r["annotated"]) for r in rows]),
        "precision": cluster_bootstrap_ratio([(r["pairs"], r["extracted"]) for r in rows]),
        "binding_accuracy": cluster_bootstrap_ratio([(r["agree"], r["pairs"]) for r in rows]),
    }


def extraction_errors(report: QualityReport) -> int:
    """Extracted assertions that are spurious (no annotated counterpart) or misbound."""
    return (report.n_extracted - report.n_pairs) + len(report.disagreements)


def passes(report: QualityReport) -> bool:
    """Whether the report meets every acceptance criterion of the pre-registration."""
    return (report.recall >= RECALL_MIN
            and all(report.recall_by_type[t] >= RECALL_PER_TYPE_MIN for t in report.types_checked)
            and report.precision >= PRECISION_MIN
            and report.binding_accuracy >= BINDING_MIN)
