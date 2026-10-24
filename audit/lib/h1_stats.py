"""Frozen interval methods for H1 (pre-registration, section 6).

Ratio estimator: pooled numerator over pooled denominator across clusters. Interval:
percentile cluster bootstrap. Clusters with a zero denominator are excluded before
resampling, so no resample can have a zero denominator. Resampling uses
``random.Random(SEED).choices`` over cluster indices, ``RESAMPLES`` times, and quantiles use
linear interpolation between order statistics (Hyndman-Fan type 7). Binomial shares from
simple random samples use the 95% Wilson score interval.
"""

import math
import random

RESAMPLES = 10_000
SEED = 20261023
Z95 = 1.959963984540054
ALPHA = 0.05


def quantile_type7(sorted_values: list[float], p: float) -> float:
    """Quantile with linear interpolation; ``sorted_values`` must be sorted ascending."""
    if not sorted_values or not 0 <= p <= 1:
        raise ValueError("need a non-empty sample and 0 <= p <= 1")
    h = (len(sorted_values) - 1) * p
    lower = math.floor(h)
    upper = min(lower + 1, len(sorted_values) - 1)
    return sorted_values[lower] + (h - lower) * (sorted_values[upper] - sorted_values[lower])


def wilson_interval(k: int, n: int, z: float = Z95) -> tuple[float, float]:
    """Two-sided 95% Wilson score interval for k successes in n trials."""
    if n <= 0 or not 0 <= k <= n:
        raise ValueError(f"invalid counts k={k}, n={n}")
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    low = 0.0 if k == 0 else max(0.0, centre - half)
    high = 1.0 if k == n else min(1.0, centre + half)
    return low, high


def confirmed_error_removal(*, mismatches: int, evaluable: int, errors: int) -> float | None:
    """Supplemental share with only the hand-confirmed extraction errors removed:
    (M - e) / (N - e). No extrapolation to unaudited mismatches. ``None`` if N - e = 0."""
    if not 0 <= errors <= mismatches <= evaluable:
        raise ValueError(f"need 0 <= errors <= mismatches <= evaluable, got "
                         f"{errors}, {mismatches}, {evaluable}")
    denominator = evaluable - errors
    return None if denominator == 0 else (mismatches - errors) / denominator


def extrapolated_share(*, mismatches: int, evaluable: int, errors: int, audited: int
                       ) -> tuple[float, float, float] | None:
    """Supplemental share with the audited error rate r = e / audited applied to all
    mismatches: (M - M r) / (N - M r), with bounds from r's 95% Wilson interval.

    The share decreases as r rises, so the lower bound uses r's upper limit. ``None`` if no
    mismatch was audited or any denominator is zero."""
    if not 0 <= errors <= audited <= mismatches <= evaluable:
        raise ValueError(f"need 0 <= errors <= audited <= mismatches <= evaluable, got "
                         f"{errors}, {audited}, {mismatches}, {evaluable}")
    if audited == 0:
        return None
    r_low, r_high = wilson_interval(errors, audited)

    def share(rate: float) -> float | None:
        denominator = evaluable - mismatches * rate
        return None if denominator == 0 else (mismatches - mismatches * rate) / denominator

    estimate, low, high = share(errors / audited), share(r_high), share(r_low)
    if estimate is None or low is None or high is None:
        return None
    return estimate, low, high


def cluster_bootstrap_ratio(groups: list[tuple[int, int]], resamples: int = RESAMPLES,
                            seed: int = SEED) -> tuple[float, float, float]:
    """(estimate, lower, upper) for sum(numerators) / sum(denominators) over clusters.

    ``groups``: one ``(numerator, denominator)`` per cluster (target, or annotated field).
    """
    kept = [(k, n) for k, n in groups if n > 0]
    if not kept:
        raise ValueError("no cluster with a positive denominator")
    estimate = sum(k for k, _ in kept) / sum(n for _, n in kept)
    rng = random.Random(seed)
    indices = range(len(kept))
    stats = []
    for _ in range(resamples):
        draw = rng.choices(indices, k=len(kept))
        stats.append(sum(kept[i][0] for i in draw) / sum(kept[i][1] for i in draw))
    stats.sort()
    return (estimate, quantile_type7(stats, ALPHA / 2), quantile_type7(stats, 1 - ALPHA / 2))
