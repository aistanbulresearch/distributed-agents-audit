"""H1 dual annotation: annotator-file format check and A-B pairing (pre-registration §5)."""

import json
from dataclasses import asdict, replace

from audit.lib.h1_annotation import (
    agreement_summary,
    check_format,
    compare_field,
    include_as_unstated,
    parse,
)
from audit.lib.h1_quality import Annotated

ROW = ("Auh", "E001")
ROW2 = ("Bcas3", "E005")
LABELS = {"155 MB Glut"}


def _ann(quantity="logfc", value="-0.571", row=ROW, **kw) -> Annotated:
    base = dict(row=row, quantity=quantity, relation="=", value_text=value,
                cell_type="155 MB Glut", gene="Auh", scope="gene", unit=None,
                self_inclusion=None, threshold_quantity=None, threshold_relation=None,
                threshold_text=None)
    base.update(kw)
    return Annotated(**base)


def _line(row, assertions) -> str:
    body = [{k: v for k, v in asdict(a).items() if k != "row"} for a in assertions]
    return json.dumps({"target_gene": row[0], "evidence_id": row[1], "assertions": body})


def test_valid_file_has_no_problems_and_round_trips():
    lines = [_line(ROW, [_ann(), _ann("padj", "0.00544")]), _line(ROW2, [])]

    assert check_format(lines, [ROW, ROW2], LABELS) == []
    assert parse(lines) == {ROW: [_ann(), _ann("padj", "0.00544")], ROW2: []}


def test_format_problems_are_reported():
    bad_vocab = _line(ROW, [_ann(quantity="mean"), _ann(cell_type="Astro")])
    assert len(check_format([bad_vocab], [ROW], LABELS)) == 2
    assert check_format([_line(ROW2, [])], [ROW], LABELS)  # wrong field order
    assert check_format([_line(ROW, [])], [ROW, ROW2], LABELS)  # missing line
    missing_key = json.dumps({"target_gene": "Auh", "evidence_id": "E001",
                              "assertions": [{"quantity": "logfc"}]})
    assert check_format([missing_key], [ROW], LABELS)


def test_identical_and_empty_fields_are_fully_agreed():
    assert compare_field(ROW, [_ann()], [_ann()]).fully_agreed
    assert compare_field(ROW, [], []).fully_agreed


def test_value_normalisation_pairs_but_any_field_difference_disagrees():
    same = compare_field(ROW, [_ann(value="-0.571")], [_ann(value="−0.571")])
    assert same.fully_agreed
    diff = compare_field(ROW, [_ann()], [replace(_ann(), cell_type=None)])
    assert not diff.fully_agreed and diff.differing[0][2] == ["cell_type"]


def test_unpaired_assertions_on_either_side():
    c = compare_field(ROW, [_ann(), _ann("padj", "0.1")], [_ann(), _ann("pval", "0.2")])
    assert [a.value_text for a in c.only_a] == ["0.1"]
    assert [b.value_text for b in c.only_b] == ["0.2"]
    assert len(c.agreed) == 1 and not c.fully_agreed


def test_repeated_values_pair_in_order():
    a = [_ann(value="0"), _ann(value="0", gene="Cul3")]
    b = [_ann(value="0"), _ann(value="0", gene="Cul3")]
    assert compare_field(ROW, a, b).fully_agreed


def test_agreement_summary_counts():
    comps = [compare_field(ROW, [_ann()], [_ann()]),
             compare_field(ROW2, [_ann(row=ROW2)], [_ann(row=ROW2, gene=None)]),
             compare_field(("C", "E1"), [], [_ann(row=("C", "E1"))])]
    s = agreement_summary(comps)
    assert (s["fields_fully_agreed"], s["pairs_agreed"], s["pairs_differing"], s["only_b"]) \
        == (1, 1, 1, 1)
    assert s["assertion_agreement"] == 1 / 3
    assert (s["assertions_a"], s["assertions_b"]) == (2, 3)


def test_include_read_as_unstated_only_without_explicit_phrase():
    count = _ann("n_sig", "11", gene=None, scope="cell", unit="genes", self_inclusion="include",
                 threshold_quantity="padj", threshold_relation="<", threshold_text="0.05")
    plain = include_as_unstated([count], "11 genes had FDR<0.05.", "Auh")
    assert plain[0].self_inclusion == "unstated"
    explicit = include_as_unstated([count], "11 genes including Auh had FDR<0.05.", "Auh")
    assert explicit[0].self_inclusion == "include"
    kept = include_as_unstated([replace(count, self_inclusion="exclude")], "11 genes", "Auh")
    assert kept[0].self_inclusion == "exclude"
