"""Assembling the resolved H1 keys (pre-registration section 5)."""
# ruff: noqa: E501  (sheet rows are reproduced verbatim)

import json

import pytest

from audit.lib.h1_key import (
    key_lines,
    merge_sources,
    normalise_owner_check,
    parse_owner_check,
    resolve_owner_check,
    target_minimum,
)
from tests.test_h1_annotation import _ann

CHECK = """## 1. Il1rapl1 / E014

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 | ✓* Subset only. |
| 2 | pval | = | 0.0266 | 017 CA3 CA2-FC DG Glut | Mcf2l | gene | — | — | — | ✓ |

**Missed:** **Scope note:** prose only.

---

## 2. Atf6 / E006

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | logfc | = | 0.5 | 155 MB Glut | Manf | gene | — | — | — | ✗ Other perturbation. |

**Missed:** Yok.

---

## 3. Htr1a / E005

*The annotator found no in-scope assertion in this field.*

**Missed:**

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |

---

## 4. Atp2b2 / E007

*The annotator found no in-scope assertion in this field.*

**Missed:**

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Hspa5 | gene | — | — | — |
"""


def test_conditional_verdicts_become_kept():
    assert "✓* Subset" not in normalise_owner_check(CHECK)
    check = parse_owner_check(CHECK)
    assert len(check[("Il1rapl1", "E014")].kept) == 2
    assert len(check[("Atf6", "E006")].dropped) == 1


def test_owner_check_resolution_applies_the_decisions():
    htr1a = ("Htr1a", "E005")
    out = resolve_owner_check(
        parse_owner_check(CHECK), add_missed={htr1a},
        remove={("Il1rapl1", "E014"): [("n_sig", "0")]},
        extra={htr1a: [target_minimum(htr1a, "min_padj", "0.693")]})
    assert [a.value_text for a in out[("Il1rapl1", "E014")]] == ["0.0266"]
    assert out[("Atf6", "E006")] == []
    assert [(a.quantity, a.value_text) for a in out[htr1a]] == [("n_sig", "0"),
                                                               ("min_padj", "0.693")]
    assert out[("Atp2b2", "E007")] == []  # missed rows not added: not in add_missed


def test_removal_must_match_exactly():
    with pytest.raises(ValueError):
        resolve_owner_check(parse_owner_check(CHECK), add_missed=set(),
                            remove={("Il1rapl1", "E014"): [("n_sig", "9")]}, extra={})


def test_merge_requires_each_field_exactly_once():
    a, b = ("A", "E1"), ("B", "E1")
    key, origin = merge_sources([a, b], {"x": {b: []}, "y": {a: [_ann(row=a)]}})
    assert list(key) == [a, b] and origin == {a: "y", b: "x"}
    with pytest.raises(ValueError):
        merge_sources([a, b], {"x": {a: []}, "y": {a: []}})
    with pytest.raises(ValueError):
        merge_sources([a, b], {"x": {a: []}})


def test_key_lines_round_trip_format():
    line = key_lines({("Auh", "E001"): [_ann()]})[0]
    obj = json.loads(line)
    assert obj["target_gene"] == "Auh" and obj["assertions"][0]["value_text"] == "-0.571"
    assert "row" not in obj["assertions"][0]
