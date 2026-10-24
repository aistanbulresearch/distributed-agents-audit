import pytest

from audit.lib.h1_match import consistent, quantum

# Codex review round 1, finding 2: tenfold differences must not match.


@pytest.mark.parametrize(
    ("text", "expected"),
    [("0.00544", "0.00001"), ("3.12e-7", "1E-9"), ("-0.571", "0.001"), ("1.0", "0.1"),
     ("20,353", "1"), ("2.47e-04", "1E-6"), ("1", "1")],
)
def test_quantum_from_written_precision(text, expected):
    from decimal import Decimal
    assert quantum(text) == Decimal(expected)


def test_tenfold_difference_is_a_mismatch():
    assert not consistent("0.001", "=", 0.0001, kind="probability")


def test_rounding_interval_accepts_nearby_value():
    assert consistent("0.001", "=", 0.00104, kind="probability")
    assert consistent("0.001", "=", 0.00096, kind="probability")


def test_truncation_interval_accepts_value_up_to_next_unit():
    # 0.0019 does not round to 0.001 but truncates to it; 0.002 does neither.
    assert consistent("0.001", "=", 0.0019, kind="probability")
    assert not consistent("0.001", "=", 0.002, kind="probability")
    assert not consistent("0.001", "=", 0.0021, kind="probability")


def test_fdr_one_point_zero_requires_value_near_one():
    assert not consistent("1.0", "=", 0.91, kind="probability")
    assert consistent("1.0", "=", 0.96, kind="probability")
    assert consistent("1.0", "=", 1.0, kind="probability")


def test_bare_integer_probability_treated_as_one_decimal():
    assert consistent("1", "=", 0.97, kind="probability")
    assert not consistent("1", "=", 0.9, kind="probability")


def test_scientific_notation_uses_mantissa_precision():
    assert consistent("3.12e-7", "=", 3.124e-7, kind="probability")
    assert consistent("3.12e-7", "=", 3.1249e-7, kind="probability")
    assert not consistent("3.12e-7", "=", 3.13e-7, kind="probability")
    assert not consistent("3.12e-7", "=", 3.12e-6, kind="probability")


def test_negative_values_truncate_toward_zero_and_keep_sign():
    assert consistent("-0.571", "=", -0.5714, kind="signed")
    assert consistent("-0.571", "=", -0.5719, kind="signed")
    assert not consistent("-0.571", "=", 0.571, kind="signed")
    assert consistent("+0.404", "=", 0.4041, kind="signed")


def test_unicode_minus_is_parsed():
    assert consistent("−0.25", "=", -0.25, kind="signed")


def test_integer_counts_require_exact_equality():
    assert consistent("20,353", "=", 20353, kind="count")
    assert not consistent("20,353", "=", 20354, kind="count")


def test_inequalities_are_strict_as_written():
    assert consistent("0.05", "<", 0.049, kind="probability")
    assert not consistent("0.05", "<", 0.05, kind="probability")
    assert consistent("0.05", "<=", 0.05, kind="probability")
    assert consistent("0.001", ">", 0.002, kind="probability")


def test_unknown_relation_raises():
    with pytest.raises(ValueError):
        consistent("0.1", "~", 0.1, kind="probability")
