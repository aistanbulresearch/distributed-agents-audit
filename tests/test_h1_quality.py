"""H1 extraction-quality gate (pre-registration section 5), tested on corrupted inputs."""

from dataclasses import replace

import pytest

from audit.lib.h1_quality import (
    COMPARISON_FIELDS,
    Annotated,
    evaluate,
    extraction_errors,
    gate_intervals,
    passes,
)

ROW = ("Auh", "E001")


def _ann(quantity="logfc", value="-0.571", **kw) -> Annotated:
    base = dict(row=ROW, quantity=quantity, relation="=", value_text=value,
                cell_type="155 MB Glut", gene="Auh", scope="gene", unit=None,
                self_inclusion=None, threshold_quantity=None, threshold_relation=None,
                threshold_text=None)
    base.update(kw)
    return Annotated(**base)


def _count(value="0", **kw) -> Annotated:
    return _ann(quantity="n_sig", value=value, gene=None, scope="cell", unit="genes",
                self_inclusion="exclude", threshold_quantity="padj", threshold_relation="<",
                threshold_text="0.05", **kw)


GOLD = [_ann(), _ann("padj", "0.00544"), _count()]


def test_perfect_agreement():
    report = evaluate(GOLD, list(GOLD))

    assert (report.recall, report.precision, report.binding_accuracy) == (1.0, 1.0, 1.0)


def test_missing_extraction_lowers_recall_only():
    report = evaluate(GOLD, GOLD[:2])

    assert report.recall == pytest.approx(2 / 3)
    assert report.precision == 1.0 and report.binding_accuracy == 1.0


def test_spurious_extraction_lowers_precision_only():
    report = evaluate(GOLD, GOLD + [_ann("pval", "3.12e-7")])

    assert report.precision == pytest.approx(3 / 4)
    assert report.recall == 1.0


@pytest.mark.parametrize("field", ["scope", "unit", "self_inclusion", "threshold_quantity",
                                   "threshold_relation", "threshold_text", "relation",
                                   "cell_type", "gene", "quantity"])
def test_any_corrupted_comparison_field_fails_binding(field):
    corrupted = {"scope": "target", "unit": "rows", "self_inclusion": "include",
                 "threshold_quantity": "pval", "threshold_relation": "<=",
                 "threshold_text": "0.1", "relation": "<", "cell_type": "308 CB GABA",
                 "gene": "Sst", "quantity": "n_rows"}[field]
    extracted = [GOLD[0], GOLD[1], replace(GOLD[2], **{field: corrupted})]

    report = evaluate(GOLD, extracted)

    assert report.recall == 1.0
    assert report.binding_accuracy == pytest.approx(2 / 3)
    assert field in report.disagreements[0]["fields"]


def test_every_comparison_field_is_checked():
    assert set(COMPARISON_FIELDS) == {
        "quantity", "relation", "value_text", "cell_type", "gene", "scope", "unit",
        "self_inclusion", "threshold_quantity", "threshold_relation", "threshold_text"}


def test_correspondence_is_one_to_one_by_value_and_order():
    gold = [_ann("padj", "1.0"), _ann("padj", "1.0", gene="Syp")]
    extracted = [_ann("padj", "1.0")]

    report = evaluate(gold, extracted)

    assert report.n_pairs == 1 and report.recall == 0.5


def test_value_text_is_normalised_before_matching():
    report = evaluate([_ann(value="20,353", quantity="n_ctrl")],
                      [_ann(value="20353", quantity="n_ctrl")])

    assert report.n_pairs == 1


def test_extraction_errors_count_spurious_and_misbound():
    extracted = [GOLD[0], replace(GOLD[1], gene="Sst"), GOLD[2], _ann("pval", "3.12e-7")]

    report = evaluate(GOLD, extracted)

    assert extraction_errors(report) == 2


def test_gate_intervals_are_field_level():
    other = ("Opa1", "E002")
    gold = GOLD + [replace(a, row=other) for a in GOLD]
    extracted = list(GOLD) + [replace(GOLD[0], row=other)]

    report = evaluate(gold, extracted)
    intervals = gate_intervals(report)

    assert report.per_row[other] == {"annotated": 3, "extracted": 1, "pairs": 1, "agree": 1}
    assert intervals["recall"][0] == pytest.approx(4 / 6)
    assert intervals["precision"] == (1.0, 1.0, 1.0)
    assert intervals["binding_accuracy"] == (1.0, 1.0, 1.0)
    assert intervals == gate_intervals(report)


def test_gate_thresholds():
    good = evaluate(GOLD, list(GOLD))
    assert passes(good)

    low_recall = evaluate(GOLD * 10, GOLD * 8)
    assert not passes(low_recall)


def test_per_type_recall_applies_only_with_twenty_instances():
    gold = [_ann(value=str(i)) for i in range(30)] + [_count(value=str(i)) for i in range(5)]
    extracted = [_ann(value=str(i)) for i in range(30)] + [_count(value="0")]

    report = evaluate(gold, extracted)

    assert report.recall_by_type["C"] == pytest.approx(1 / 5)
    assert report.recall >= 0.80
    assert "C" not in report.types_checked
