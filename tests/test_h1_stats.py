"""Frozen interval methods for H1 (pre-registration, section 6)."""

import pytest

from audit.lib.h1_stats import (
    RESAMPLES,
    SEED,
    cluster_bootstrap_ratio,
    confirmed_error_removal,
    extrapolated_share,
    quantile_type7,
    wilson_interval,
)

# Supplemental audit-adjusted shares (Codex review round 7).

def test_confirmed_error_removal_codex_example():
    assert confirmed_error_removal(mismatches=1000, evaluable=10000, errors=20) == \
        pytest.approx(980 / 9980)


def test_extrapolated_share_codex_example():
    estimate, low, high = extrapolated_share(mismatches=1000, evaluable=10000, errors=20,
                                             audited=100)
    r_low, r_high = wilson_interval(20, 100)

    assert estimate == pytest.approx(800 / 9800)
    assert low == pytest.approx((1000 - 1000 * r_high) / (10000 - 1000 * r_high))
    assert high == pytest.approx((1000 - 1000 * r_low) / (10000 - 1000 * r_low))
    assert low <= estimate <= high


def test_both_formulas_agree_when_every_mismatch_is_audited():
    estimate, _, _ = extrapolated_share(mismatches=40, evaluable=5000, errors=7, audited=40)

    assert estimate == pytest.approx(confirmed_error_removal(mismatches=40, evaluable=5000,
                                                             errors=7))


def test_zero_denominators_are_undefined():
    assert confirmed_error_removal(mismatches=5, evaluable=5, errors=5) is None
    assert extrapolated_share(mismatches=5, evaluable=5, errors=5, audited=5) is None
    assert extrapolated_share(mismatches=0, evaluable=100, errors=0, audited=0) is None


@pytest.mark.parametrize(("kwargs"), [
    {"mismatches": 10, "evaluable": 100, "errors": 11},
    {"mismatches": 200, "evaluable": 100, "errors": 0},
])
def test_confirmed_error_removal_rejects_impossible_counts(kwargs):
    with pytest.raises(ValueError):
        confirmed_error_removal(**kwargs)


@pytest.mark.parametrize(("kwargs"), [
    {"mismatches": 1000, "evaluable": 10000, "errors": 101, "audited": 100},
    {"mismatches": 50, "evaluable": 10000, "errors": 1, "audited": 100},
])
def test_extrapolated_share_rejects_impossible_counts(kwargs):
    with pytest.raises(ValueError):
        extrapolated_share(**kwargs)


def test_frozen_constants():
    assert (RESAMPLES, SEED) == (10_000, 20261023)


@pytest.mark.parametrize(("p", "expected"), [(0.0, 1.0), (0.25, 1.75), (0.5, 2.5),
                                             (0.975, 3.925), (1.0, 4.0)])
def test_quantile_type7_linear_interpolation(p, expected):
    assert quantile_type7([1.0, 2.0, 3.0, 4.0], p) == pytest.approx(expected)


def test_wilson_interval():
    low, high = wilson_interval(0, 150)
    assert low == 0.0 and high == pytest.approx(0.0249, abs=1e-3)
    assert wilson_interval(10, 10)[1] == 1.0
    low, high = wilson_interval(2, 100)
    assert low == pytest.approx(0.0055, abs=1e-3) and high == pytest.approx(0.0700, abs=1e-3)


def test_ratio_estimator_pools_counts_not_per_group_shares():
    estimate, _, _ = cluster_bootstrap_ratio([(1, 1), (0, 99)], resamples=100, seed=1)

    assert estimate == pytest.approx(0.01)


def test_bootstrap_is_deterministic_for_a_seed():
    groups = [(i % 3, 10) for i in range(50)]

    assert cluster_bootstrap_ratio(groups) == cluster_bootstrap_ratio(groups)


def test_codex_round5_example_is_pinned():
    # 100 equally sized targets, one with 30/100 mismatches: the frozen method gives one
    # fixed interval, so no post-hoc choice of CI construction is possible.
    groups = [(30, 100)] + [(0, 100)] * 99

    estimate, low, high = cluster_bootstrap_ratio(groups)

    assert estimate == pytest.approx(0.003)
    assert low == 0.0
    assert high == pytest.approx(0.009, abs=1e-12)


def test_groups_without_denominator_are_excluded():
    with_empty = cluster_bootstrap_ratio([(1, 10), (0, 0), (2, 10)])
    without = cluster_bootstrap_ratio([(1, 10), (2, 10)])

    assert with_empty == without


def test_no_evaluable_groups_raises():
    with pytest.raises(ValueError):
        cluster_bootstrap_ratio([(0, 0)])
