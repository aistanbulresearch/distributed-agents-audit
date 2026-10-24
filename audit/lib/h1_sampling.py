"""Frozen sampling procedures for H1 (pre-registration, sections 5 and 6).

Population order is canonical (ascending tuple order of identifiers), so the input order
cannot matter. Draws use ``random.Random(seed).sample`` on that order: without replacement.
The validation annotation sample is drawn from the population minus the first sample, so
the two never overlap.
"""

import random
from collections.abc import Iterable, Mapping

from audit.lib.corpus import is_control

RowId = tuple[str, str]  # (target_gene, evidence_id)
MismatchId = tuple[str, str, int, str]  # (target_gene, evidence_id, start offset, quantity)

ANNOTATION_SEEDS = (20261023, 20261024)
ANNOTATION_SIZE = 150
AUDIT_SEED = 20261023
AUDIT_SIZE = 100
OWNER_CHECK_SEED = 20261025
OWNER_CHECK_SIZE = 30
# Dual annotation (section 5): blind X/Y labels and the owner's audit of agreed fields.
XY_SEEDS = {1: 20261026, 2: 20261028}
AGREEMENT_AUDIT_SEEDS = {1: 20261027, 2: 20261029}
AGREEMENT_AUDIT_SIZE = 20


def _unique_sorted(items: Iterable, what: str) -> list:
    items = list(items)
    if len(set(items)) != len(items):
        raise ValueError(f"duplicate {what} identifiers")
    return sorted(items)


def annotation_population(rows: Iterable[Mapping[str, str]]) -> list[RowId]:
    """Non-control evidence rows with a non-empty ``statistics`` field, in canonical order."""
    ids = ((r["target_gene"], r["evidence_id"]) for r in rows
           if not is_control(r["target_gene"]) and r["statistics"].strip())
    return _unique_sorted(ids, "row")


def draw_annotation_samples(population: list[RowId], size: int = ANNOTATION_SIZE
                            ) -> tuple[list[RowId], list[RowId]]:
    """(first sample, reserved validation sample), each sorted, disjoint, of ``size`` rows."""
    canonical = _unique_sorted(population, "row")
    if len(canonical) < 2 * size:
        raise ValueError(f"population of {len(canonical)} too small for two samples of {size}")
    first = random.Random(ANNOTATION_SEEDS[0]).sample(canonical, size)
    taken = set(first)
    remaining = [row for row in canonical if row not in taken]
    second = random.Random(ANNOTATION_SEEDS[1]).sample(remaining, size)
    return sorted(first), sorted(second)


def owner_check_sample(sample1: list[RowId], size: int = OWNER_CHECK_SIZE) -> list[RowId]:
    """The fields of annotation sample 1 that the owner checks by hand (frozen draw)."""
    canonical = _unique_sorted(sample1, "row")
    return sorted(random.Random(OWNER_CHECK_SEED).sample(canonical, size))


def xy_assignment(fields: list[RowId], sample: int) -> dict[RowId, bool]:
    """Per field, whether annotator A is shown as X (else Y) to the blind adjudicator.
    One ``random()`` draw per field in canonical order."""
    rng = random.Random(XY_SEEDS[sample])
    return {field: rng.random() < 0.5 for field in _unique_sorted(fields, "row")}


def agreement_audit_sample(agreed_fields: list[RowId], sample: int,
                           size: int = AGREEMENT_AUDIT_SIZE) -> list[RowId]:
    """Fields where A and B fully agree that the owner checks anyway (all if at most size)."""
    canonical = _unique_sorted(agreed_fields, "row")
    if len(canonical) <= size:
        return canonical
    return sorted(random.Random(AGREEMENT_AUDIT_SEEDS[sample]).sample(canonical, size))


def audit_sample(mismatches: Iterable[MismatchId], size: int = AUDIT_SIZE) -> list[MismatchId]:
    """Mismatches to check by hand: all if at most ``size``, else a frozen random sample."""
    canonical = _unique_sorted(mismatches, "mismatch")
    if len(canonical) <= size:
        return canonical
    return sorted(random.Random(AUDIT_SEED).sample(canonical, size))
