"""Annotator packet builder (H1 pre-registration, section 5)."""

import json

from audit.lib.h1_packet import OUTPUT_PLACEHOLDER, build_packet

TEMPLATE = f"Write to `{OUTPUT_PLACEHOLDER}`.\n\n## Cell-type labels\n\n"
SECTION3 = "## 3. Grammar\n\nRules."


def _rows():
    return [
        {"target_gene": "Auh", "evidence_id": "E001", "cell_type": "155 MB Glut",
         "statistics": "145 perturbed cells versus 20,353 controls."},
        {"target_gene": "Erf", "evidence_id": "E002", "cell_type": "",
         "statistics": "0 genes at FDR < 0.05; Ålpha \u2212 test."},
    ]


def test_packet_layout_is_exact():
    packet = build_packet(TEMPLATE, "C:/out/a.jsonl", ["001 X", "002 Y"], SECTION3, _rows())

    expected_fields = "\n".join(
        json.dumps({"target_gene": r["target_gene"], "evidence_id": r["evidence_id"],
                    "cell_type": r["cell_type"] or None, "statistics": r["statistics"]},
                   ensure_ascii=False) for r in _rows())
    assert packet == ("Write to `C:/out/a.jsonl`.\n\n## Cell-type labels\n\n"
                      "- `001 X`\n- `002 Y`\n\n## 3. Grammar\n\nRules.\n\n"
                      "## The 150 fields\n\n" + expected_fields + "\n")


def test_empty_cell_type_becomes_null_and_unicode_is_kept():
    packet = build_packet(TEMPLATE, "o", ["001 X"], SECTION3, _rows())

    assert '"cell_type": null' in packet
    assert "Ålpha \u2212 test" in packet


def test_template_must_contain_the_placeholder_once():
    import pytest
    with pytest.raises(ValueError):
        build_packet("no placeholder", "o", ["001 X"], SECTION3, _rows())
