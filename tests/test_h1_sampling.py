"""Frozen sampling procedures for H1 (pre-registration, sections 5 and 6)."""

import random

import pytest

from audit.lib.h1_sampling import (
    AGREEMENT_AUDIT_SEEDS,
    ANNOTATION_SEEDS,
    AUDIT_SEED,
    OWNER_CHECK_SEED,
    XY_SEEDS,
    agreement_audit_sample,
    annotation_population,
    audit_sample,
    draw_annotation_samples,
    owner_check_sample,
    xy_assignment,
)


def _rows(n, controls=0, empty=0):
    rows = [{"target_gene": f"G{i:04d}", "evidence_id": "E001", "statistics": "x"}
            for i in range(n)]
    rows += [{"target_gene": f"Safe_target_{i}", "evidence_id": "E001", "statistics": "x"}
             for i in range(controls)]
    rows += [{"target_gene": f"H{i:04d}", "evidence_id": "E001", "statistics": "  "}
             for i in range(empty)]
    return rows


def test_frozen_seeds():
    assert ANNOTATION_SEEDS == (20261023, 20261024)
    assert AUDIT_SEED == 20261023


def test_population_is_canonical_and_excludes_controls_and_empty_fields():
    rows = _rows(5, controls=2, empty=3)
    shuffled = rows[::-1]

    assert annotation_population(rows) == annotation_population(shuffled)
    assert annotation_population(rows) == [(f"G{i:04d}", "E001") for i in range(5)]


def test_duplicate_row_ids_are_rejected():
    rows = _rows(3) + _rows(1)
    with pytest.raises(ValueError, match="duplicate"):
        annotation_population(rows)


def test_samples_use_random_sample_on_the_canonical_order():
    population = annotation_population(_rows(1000))
    first, second = draw_annotation_samples(population, size=150)

    assert first == sorted(random.Random(20261023).sample(population, 150))
    remaining = [row for row in population if row not in set(first)]
    assert second == sorted(random.Random(20261024).sample(remaining, 150))


def test_samples_are_disjoint_without_replacement_and_deterministic():
    population = annotation_population(_rows(1000))
    first, second = draw_annotation_samples(population, size=150)

    assert len(set(first)) == len(first) == 150
    assert len(set(second)) == len(second) == 150
    assert not set(first) & set(second)
    assert (first, second) == draw_annotation_samples(list(reversed(population)), size=150)


def test_population_too_small_raises():
    with pytest.raises(ValueError, match="population"):
        draw_annotation_samples(annotation_population(_rows(250)), size=150)


def test_owner_check_sample_is_frozen_subset_of_sample1():
    population = annotation_population(_rows(1000))
    first, _ = draw_annotation_samples(population, size=150)

    check = owner_check_sample(first)

    assert OWNER_CHECK_SEED == 20261025 and len(check) == 30
    assert set(check) <= set(first)
    assert check == sorted(random.Random(20261025).sample(sorted(first), 30))
    assert check == owner_check_sample(list(reversed(first)))


def test_adjudication_seeds_are_frozen_per_sample():
    assert XY_SEEDS == {1: 20261026, 2: 20261028}
    assert AGREEMENT_AUDIT_SEEDS == {1: 20261027, 2: 20261029}


def test_xy_assignment_is_canonical_and_deterministic():
    fields = annotation_population(_rows(40))
    rng = random.Random(20261026)
    expected = {field: rng.random() < 0.5 for field in sorted(fields)}

    assert xy_assignment(fields, sample=1) == expected
    assert xy_assignment(list(reversed(fields)), sample=1) == expected
    assert 0 < sum(expected.values()) < len(fields)


def test_agreement_audit_sample():
    fields = annotation_population(_rows(100))

    drawn = agreement_audit_sample(fields, sample=2)

    assert drawn == sorted(random.Random(20261029).sample(sorted(fields), 20))
    assert agreement_audit_sample(fields[:7], sample=2) == sorted(fields[:7])


def test_audit_sample_takes_all_when_fewer_than_size():
    mismatches = [("G0001", "E001", 12, "logfc"), ("G0002", "E003", 0, "padj")]

    assert audit_sample(mismatches, size=100) == sorted(mismatches)


def test_audit_sample_is_canonical_and_deterministic():
    mismatches = [(f"G{i % 40:04d}", f"E{i % 7:03d}", i, "padj") for i in range(500)]
    expected = sorted(random.Random(20261023).sample(sorted(mismatches), 100))

    assert audit_sample(mismatches, size=100) == expected
    assert audit_sample(list(reversed(mismatches)), size=100) == expected


def test_audit_sample_rejects_duplicate_ids():
    with pytest.raises(ValueError, match="duplicate"):
        audit_sample([("G1", "E1", 0, "padj")] * 2, size=100)
