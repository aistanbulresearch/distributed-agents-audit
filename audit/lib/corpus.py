"""Read-only loaders for the released corpus ledgers.

``ref_id`` and ``evidence_id`` are local to a target gene: ``R001`` exists in almost every
report. Every join therefore goes through ``(target_gene, id)``.
"""

import csv
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

# Report fields can be long; 2**31 - 1 is the largest limit a 32-bit C long (Windows) accepts.
csv.field_size_limit(2**31 - 1)

_LFS_HEADER = "version https://git-lfs"
_CONTROL_PREFIXES = ("Safe_target", "Non_target")


class LfsPointerError(RuntimeError):
    """Raised when a data file is an unresolved Git LFS pointer."""


@dataclass(frozen=True)
class Reference:
    target_gene: str
    ref_id: str
    ref_slug: str
    source: str
    source_type: str
    citation: str
    url: str
    description: str


@dataclass(frozen=True)
class Finding:
    target_gene: str
    finding_id: str
    finding_type: str
    direction: str
    confidence: str
    literature_status: str
    summary: str
    why_it_matters: str
    genes: tuple[str, ...]
    n_genes: int
    comparators: tuple[str, ...]
    cell_types: tuple[str, ...]
    n_cell_types: int
    evidence_ids: tuple[str, ...]
    ref_ids: tuple[str, ...]
    main_caveats: str


def is_control(target_gene: str) -> bool:
    """True for safe-target and non-targeting control labels."""
    return target_gene.startswith(_CONTROL_PREFIXES)


def read_csv_checked(path: Path) -> Iterator[dict[str, str]]:
    """Yield CSV rows, refusing files that are Git LFS pointers."""
    with open(path, encoding="utf-8", newline="") as handle:
        first = handle.readline()
        if first.startswith(_LFS_HEADER):
            raise LfsPointerError(f"{path} is a Git LFS pointer; run `git lfs pull` upstream")
        handle.seek(0)
        yield from csv.DictReader(handle)


def _split(value: str) -> tuple[str, ...]:
    return tuple(part.strip() for part in value.split("|") if part.strip())


def _int(value: str) -> int:
    return int(value) if value.strip() else 0


def load_references(release_dir: Path) -> dict[tuple[str, str], Reference]:
    """Load references keyed by ``(target_gene, ref_id)``."""
    refs: dict[tuple[str, str], Reference] = {}
    for row in read_csv_checked(release_dir / "ledgers" / "references.csv"):
        ref = Reference(**{field: row[field] for field in Reference.__dataclass_fields__})
        key = (ref.target_gene, ref.ref_id)
        if key in refs:
            raise ValueError(f"duplicate reference key {key}")
        refs[key] = ref
    return refs


def load_findings(release_dir: Path, include_controls: bool = False) -> list[Finding]:
    """Load findings; safe-target and non-targeting controls are excluded by default."""
    findings = []
    for row in read_csv_checked(release_dir / "ledgers" / "findings.csv"):
        if not include_controls and is_control(row["target_gene"]):
            continue
        findings.append(
            Finding(
                target_gene=row["target_gene"],
                finding_id=row["finding_id"],
                finding_type=row["finding_type"],
                direction=row["direction"],
                confidence=row["confidence"],
                literature_status=row["literature_status"],
                summary=row["summary"],
                why_it_matters=row["why_it_matters"],
                genes=_split(row["genes"]),
                n_genes=_int(row["n_genes"]),
                comparators=_split(row["comparators"]),
                cell_types=_split(row["cell_types"]),
                n_cell_types=_int(row["n_cell_types"]),
                evidence_ids=_split(row["evidence_ids"]),
                ref_ids=_split(row["ref_ids"]),
                main_caveats=row["main_caveats"],
            )
        )
    return findings


def refs_for_finding(
    finding: Finding, refs: dict[tuple[str, str], Reference]
) -> list[Reference]:
    """Resolve a finding's ``ref_ids`` within its own target. Raises KeyError if missing."""
    return [refs[(finding.target_gene, ref_id)] for ref_id in finding.ref_ids]
