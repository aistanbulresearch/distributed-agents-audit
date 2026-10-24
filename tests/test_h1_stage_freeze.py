"""Receipt check of the staged H1 freeze (pre-registration section 10)."""

import json

from audit.lib import paths
from audit.lib.manifest import sha256_file
from audit.scripts.h1_stage_freeze import check_receipts, git_round_trip


def _tree(tmp_path):
    reg = tmp_path / "registrations"
    (reg / "annotation" / "blank").mkdir(parents=True)
    form = reg / "annotation" / "H1_adjudication_sample1.md"
    form.write_text("filled", encoding="utf-8")
    blank = reg / "annotation" / "blank" / "H1_adjudication_sample1.md"
    blank.write_text("blank", encoding="utf-8")
    key = reg / "H1_annotation_sample1.jsonl"
    key.write_text("{}\n", encoding="utf-8")
    return reg, form, blank, key


def test_matching_receipts_pass(tmp_path):
    reg, form, blank, key = _tree(tmp_path)
    (reg / "annotation" / "tally.json").write_text(json.dumps(
        {"inputs": {form.name: sha256_file(form)},
         "forms": {blank.name: sha256_file(blank)},
         "samples": {"1": {"key": key.name, "sha256": sha256_file(key)}}}), encoding="utf-8")
    assert check_receipts(reg) == []


def test_stale_or_missing_hashes_are_reported(tmp_path):
    reg, form, blank, _ = _tree(tmp_path)
    (reg / "annotation" / "tally.json").write_text(json.dumps(
        {"inputs": {form.name: "0" * 64, "absent.md": "1" * 64},
         "forms": {blank.name: sha256_file(form)}}), encoding="utf-8")
    problems = check_receipts(reg)
    assert len(problems) == 3
    assert any("absent.md is not published" in p for p in problems)


def _crlf_stage(tmp_path, attributes: str):
    stage = tmp_path / "stage"
    (stage / "registrations").mkdir(parents=True)
    (stage / ".gitattributes").write_bytes(attributes.encode())
    form = stage / "registrations" / "H1_owner_check_filled.md"
    form.write_bytes(b"| 1 | n_sig | \xe2\x9c\x93 |\r\nline two\r\n")
    ref = tmp_path / "de.parquet"
    ref.write_bytes(b"reference")
    manifest = {"artifacts": {".gitattributes": sha256_file(stage / ".gitattributes"),
                              "registrations/H1_owner_check_filled.md": sha256_file(form)},
                "reference": {"key": "cache:de.parquet", "sha256": sha256_file(ref)}}
    return stage, manifest, (lambda key: tmp_path / key.partition(":")[2])


def test_repository_attributes_keep_registration_bytes_through_git(tmp_path):
    attributes = (paths.REPO_ROOT / ".gitattributes").read_text(encoding="utf-8")
    stage, manifest, resolve_input = _crlf_stage(tmp_path, attributes)
    assert git_round_trip(stage, manifest, tmp_path / "scratch", resolve_input) == []


def test_line_ending_normalisation_is_caught(tmp_path):
    stage, manifest, resolve_input = _crlf_stage(tmp_path, "* text=auto eol=lf\n")
    problems = git_round_trip(stage, manifest, tmp_path / "scratch", resolve_input)
    assert problems and "H1_owner_check_filled.md" in problems[0]
