"""Assemble and check the resolved H1 annotation keys of both samples.

Run: uv run python -m audit.scripts.h1_assemble_keys <records_dir> <out_dir>

``records_dir`` holds the annotators' raw files, sample 1's revision-8 annotation and the
owner's filled check, and the owner's filled adjudication, agreement-audit and DC-33 review
forms (file names below). Writes ``H1_annotation_sample{1,2}.jsonl`` and
``H1_key_assembly.json`` (source of every field, counts, input and output hashes) to
``out_dir``. Every form is re-checked against the raw files before use. Reads evidence text
only; never DE values or extractor output.
"""

import hashlib
import json
import logging
import sys
from collections import Counter
from pathlib import Path

from audit.lib import corpus, paths
from audit.lib.h1_annotation import check_format, compare_field, include_as_unstated, parse
from audit.lib.h1_key import (
    key_lines,
    merge_sources,
    parse_owner_check,
    resolve_owner_check,
    resolved,
    target_minimum,
)
from audit.lib.h1_rulings import parse_form
from audit.lib.h1_sampling import agreement_audit_sample
from audit.scripts.h1_tally_rulings import RECON, SAMPLE_KEYS, SAMPLES, _form_rows, _shown

logger = logging.getLogger(__name__)

# The owner's decisions DC-27 and DC-29 on the 30-field check (pre-registration §5).
OWNER_CHECK_ADD_MISSED = {("Eif4h", "E010"), ("Htr1a", "E005"), ("Pde1c", "E004")}
OWNER_CHECK_REMOVE = {("Il1rapl1", "E014"): [("n_sig", "0")]}
OWNER_CHECK_EXTRA = {("Htr1a", "E005"): [target_minimum(("Htr1a", "E005"), "min_padj", "0.693")]}


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    rec, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    paths.check_upstream_pin()
    samples = json.loads(SAMPLES.read_text(encoding="utf-8"))
    labels = set(json.loads(RECON.read_text(encoding="utf-8"))
                 ["differential_expression"]["groups"])
    ledger = {(r["target_gene"], r["evidence_id"]): r for r in
              corpus.read_csv_checked(paths.release_dir() / "ledgers" / "evidence.csv")}
    owner_checked = [tuple(r) for r in samples["owner_check"]]
    inputs: dict[str, str] = {}
    report: dict = {"samples": {}}
    for sample in (1, 2):
        expected = [tuple(r) for r in samples[SAMPLE_KEYS[sample]]]
        files = {"A": rec / f"H1_annotation_sample{sample}_A.jsonl",
                 "B": rec / f"H1_annotation_sample{sample}_B.jsonl",
                 "adjudication": rec / f"H1_adjudication_sample{sample}.md",
                 "audit": rec / f"H1_agreement_audit_sample{sample}.md"}
        if sample == 1:
            files |= {"rev8": rec / "H1_annotation_sample1_A_rev8.jsonl",
                      "owner_check": rec / "H1_owner_check_filled.md",
                      "dc33_review": rec / "H1_agreed_review_sample1_filled.md"}
        inputs |= {p.name: _sha(p) for p in files.values()}
        ann_a = parse(files["A"].read_text(encoding="utf-8").splitlines())
        ann_b = parse(files["B"].read_text(encoding="utf-8").splitlines())
        checked = set(owner_checked) if sample == 1 else set()
        comps = {row: compare_field(row, ann_a[row], ann_b[row])
                 for row in expected if row not in checked}
        agreed = [row for row, c in comps.items() if c.fully_agreed]
        audited = agreement_audit_sample(agreed, sample)
        unaudited = [row for row in agreed if row not in set(audited)]

        adj = parse_form(files["adjudication"].read_text(encoding="utf-8"), sourced=True)
        audit = parse_form(files["audit"].read_text(encoding="utf-8"), sourced=False)
        problems = []
        for row, f in adj.items():
            text = ledger[row]["statistics"]
            if _form_rows(f) != _shown(include_as_unstated(ann_a[row], text, row[0]),
                                       include_as_unstated(ann_b[row], text, row[0]), row):
                problems.append(f"{row}: adjudication rows altered")
        for row, f in audit.items():
            if _form_rows(f) != Counter(ann_a[row]):
                problems.append(f"{row}: audit rows altered")
        sources = {"adjudication": resolved(adj), "agreement_audit": resolved(audit)}
        if sample == 1:
            rev8 = parse(files["rev8"].read_text(encoding="utf-8").splitlines())
            check = parse_owner_check(files["owner_check"].read_text(encoding="utf-8"))
            for row, f in check.items():
                if _form_rows(f) != Counter(rev8[row]):
                    problems.append(f"{row}: owner-check rows differ from revision-8 file")
            sources["owner_check"] = resolve_owner_check(
                check, add_missed=OWNER_CHECK_ADD_MISSED, remove=OWNER_CHECK_REMOVE,
                extra=OWNER_CHECK_EXTRA)
            review = parse_form(files["dc33_review"].read_text(encoding="utf-8"),
                                sourced=False)
            for row, f in review.items():
                if _form_rows(f) != Counter(ann_a[row]):
                    problems.append(f"{row}: DC-33 review rows altered")
            sources["dc33_review"] = resolved(review)
        else:
            sources["agreed_unreviewed"] = {
                row: include_as_unstated(ann_a[row], ledger[row]["statistics"], row[0])
                for row in unaudited}
        key, origin = merge_sources(expected, sources)
        lines = key_lines(key)
        problems += check_format(lines, expected, labels)
        if problems:
            for p in problems:
                logger.info("sample %d: %s", sample, p)
            sys.exit(1)
        out = out_dir / f"H1_annotation_sample{sample}.jsonl"
        out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        by_source = Counter(origin.values())
        assertions: Counter[str] = Counter()
        for row, name in origin.items():
            assertions[name] += len(key[row])
        report["samples"][str(sample)] = {
            "key": out.name, "sha256": _sha(out), "fields": len(key),
            "assertions": sum(len(v) for v in key.values()),
            "fields_by_source": dict(by_source), "assertions_by_source": dict(assertions),
            "source_of_field": {f"{r[0]}/{r[1]}": origin[r] for r in expected}}
        logger.info("sample %d: %d fields, %d assertions, %s; sha256 %s", sample, len(key),
                    report["samples"][str(sample)]["assertions"], dict(by_source), _sha(out))
    report["inputs"] = inputs
    (out_dir / "H1_key_assembly.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
