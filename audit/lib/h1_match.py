"""H1 matching rule: is a recomputed value consistent with a reported number?

A reported decimal matches when the recomputed value rounds to it, or truncates (toward
zero) to it, at the precision the report wrote. Counts must be equal. Inequalities are
evaluated as written. See section 4 of the H1 pre-registration.
"""

from decimal import Decimal
from typing import Literal

Kind = Literal["probability", "signed", "count"]

_EQUALITY = {"=", ":"}
_RELATIONS = {"<", "<=", ">", ">=", "≤", "≥"} | _EQUALITY


def normalise_number(text: str) -> str:
    """Strip thousands separators and a leading plus; map the Unicode minus to ASCII."""
    return text.strip().replace("−", "-").replace(",", "").removeprefix("+")


def quantum(text: str) -> Decimal:
    """One unit of the last written digit (mantissa digit for scientific notation)."""
    number = normalise_number(text).lower()
    mantissa, _, exponent = number.partition("e")
    decimals = len(mantissa.partition(".")[2])
    return Decimal(1).scaleb(-decimals + (int(exponent) if exponent else 0))


def _as_decimal(value: float | int) -> Decimal:
    return Decimal(value) if isinstance(value, int) else Decimal(repr(float(value)))


def _equal(text: str, recomputed: Decimal, kind: Kind) -> bool:
    reported = Decimal(normalise_number(text))
    if kind == "count":
        return recomputed == reported
    unit = quantum(text)
    is_bare_integer = not any(ch in normalise_number(text).lower() for ch in ".e")
    if kind == "probability" and is_bare_integer:
        unit = Decimal("0.1")  # "FDR=1" is read as "FDR=1.0"
    rounds = abs(recomputed - reported) <= unit / 2
    if reported >= 0 and not normalise_number(text).startswith("-"):
        truncates = reported <= recomputed < reported + unit
    else:
        truncates = reported - unit < recomputed <= reported
    return rounds or truncates


def consistent(text: str, relation: str, recomputed: float | int, kind: Kind) -> bool:
    """Whether ``recomputed`` is consistent with the reported ``text`` under ``relation``."""
    if relation not in _RELATIONS:
        raise ValueError(f"unknown relation {relation!r}")
    value = _as_decimal(recomputed)
    if relation in _EQUALITY:
        return _equal(text, value, kind)
    reported = Decimal(normalise_number(text))
    if relation == "<":
        return value < reported
    if relation in ("<=", "≤"):
        return value <= reported
    if relation == ">":
        return value > reported
    return value >= reported
