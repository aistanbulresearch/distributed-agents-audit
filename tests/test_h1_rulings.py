"""Reading the owner's filled H1 forms (pre-registration §5)."""
# ruff: noqa: E501  (form rows are reproduced verbatim)

import pytest

from audit.lib.h1_rulings import RulingError, parse_form

ADJUDICATION = """# header

## 1. Armc9 / E004

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | pval | = | 0.00489 | 052 Pvalb Gaba | Armc9 | gene | — | — | — |  | ✓ |
| 2 | X≠ | logfc | = | -0.392 | 052 Pvalb Gaba | Armc9 | gene | — | — | — | cell_type | ✓ |
| 3 | Y≠ | logfc | = | -0.392 | — | Armc9 | gene | — | — | — | cell_type | ✗ Wrong cell. |
| 4 | Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.10 |  | ✗ → unit=rows; all other fields unchanged. |

**Review:** text.

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| n_rows | = | 0 | 215 MB Dopa | — | cell | rows | unstated | — |

---

## 2. Bcas3 / E005

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | padj | = | 0.1 | — | Bcas3 | gene | — | — | — |  | ✗ Other perturbation. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
"""

AUDIT = """## 1. Mark3 / E002

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 39 | 145 MH-LH TH Glut | — | cell | — | — | — | ✓ |

**Missed by both** (add):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| n_sig | = | one | 145 MH-LH TH Glut | — | cell | genes | unstated | padj < 0.05 |
"""


def test_adjudication_rulings_resolve_in_order():
    f = parse_form(ADJUDICATION, sourced=True)
    armc9 = f[("Armc9", "E004")]
    assert [a.value_text for a in armc9.resolved] == ["0.00489", "-0.392", "0", "0"]
    assert armc9.resolved[1].cell_type == "052 Pvalb Gaba"
    assert armc9.resolved[2].unit == "rows" and armc9.resolved[2].threshold_text == "0.10"
    assert armc9.resolved[3].quantity == "n_rows" and armc9.resolved[3].threshold_text is None
    assert len(armc9.dropped) == 1 and len(armc9.corrected) == 1 and len(armc9.added) == 1
    bcas3 = f[("Bcas3", "E005")]
    assert bcas3.resolved == [] and bcas3.changed


def test_audit_form_with_added_row():
    f = parse_form(AUDIT, sourced=False)[("Mark3", "E002")]
    assert [a.quantity for a in f.resolved] == ["n_pert", "n_sig"]
    assert f.added[0].value_text == "one" and f.added[0].threshold_quantity == "padj"
    assert f.changed


def test_unruled_or_unreadable_rows_raise():
    with pytest.raises(RulingError):
        parse_form(AUDIT.replace("| — | ✓ |", "| — |  |"), sourced=False)
    with pytest.raises(RulingError):
        parse_form(ADJUDICATION.replace("unit=rows", "colour=red"), sourced=True)
