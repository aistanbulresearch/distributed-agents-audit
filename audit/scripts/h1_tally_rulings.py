"""Tally the owner's filled adjudication and agreement-audit forms for one H1 sample.

Run: uv run python -m audit.scripts.h1_tally_rulings <sample: 1|2> <annotator_A.jsonl>
         <annotator_B.jsonl> <filled_adjudication.md> <filled_audit.md> <out.json>

Checks that each form covers exactly the fields the pairing selected, that the rows shown
were not altered (they must equal what the pairing displays from the raw files) and that
every resolved assertion fits the codebook. Reports rulings and the agreement-audit error
count with its Wilson interval, and whether decision DC-33 (full review of the remaining
agreed fields) is triggered. Reads evidence text only; never DE values or extractor output.
"""

import hashlib
import json
import logging
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from audit.lib import corpus, paths
from audit.lib.h1_annotation import check_format, compare_field, include_as_unstated, parse
from audit.lib.h1_quality import Annotated
from audit.lib.h1_rulings import RuledField, parse_form
from audit.lib.h1_sampling import agreement_audit_sample
from audit.lib.h1_stats import wilson_interval

logger = logging.getLogger(__name__)

SAMPLES = paths.REPO_ROOT / "audit" / "results" / "h1" / "annotation_samples.json"
RECON = paths.REPO_ROOT / "audit" / "results" / "recon" / "inventory.json"
SAMPLE_KEYS = {1: "sample1", 2: "sample2_reserved"}


def _shown(a: list[Annotated], b: list[Annotated], row: tuple[str, str]) -> Counter:
    """The rows the adjudication form displays for a field (identical rows once)."""
    c = compare_field(row, a, b)
    shown = [x for x, _ in c.agreed] + [x for d in c.differing for x in d[:2]]
    return Counter(shown + c.only_a + c.only_b)


def _form_rows(f: RuledField) -> Counter:
    return Counter(f.kept + [a for a, _ in f.dropped] + [a for a, _ in f.corrected])


def _summary(fields: dict[tuple[str, str], RuledField]) -> dict:
    return {"fields": len(fields), "fields_changed": sum(f.changed for f in fields.values()),
            "rows_kept": sum(len(f.kept) for f in fields.values()),
            "rows_dropped": sum(len(f.dropped) for f in fields.values()),
            "rows_corrected": sum(len(f.corrected) for f in fields.values()),
            "rows_added": sum(len(f.added) for f in fields.values()),
            "resolved_assertions": sum(len(f.resolved) for f in fields.values())}


def _changes(fields: dict[tuple[str, str], RuledField]) -> list[dict]:
    out = []
    for row, f in fields.items():
        if f.changed:
            out.append({"field": f"{row[0]}/{row[1]}",
                        "dropped": [[a.quantity, a.value_text, why] for a, why in f.dropped],
                        "corrected": [[a.quantity, a.value_text,
                                       {k: v for k, v in asdict(b).items()
                                        if v != getattr(a, k)}] for a, b in f.corrected],
                        "added": [[a.quantity, a.value_text] for a in f.added]})
    return out


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    sample = int(sys.argv[1])
    a_path, b_path, adj_path, audit_path, out_path = map(Path, sys.argv[2:7])
    paths.check_upstream_pin()
    samples = json.loads(SAMPLES.read_text(encoding="utf-8"))
    expected = [tuple(r) for r in samples[SAMPLE_KEYS[sample]]]
    owner_checked = {tuple(r) for r in samples["owner_check"]} if sample == 1 else set()
    labels = set(json.loads(RECON.read_text(encoding="utf-8"))
                 ["differential_expression"]["groups"])
    ledger = {(r["target_gene"], r["evidence_id"]): r for r in
              corpus.read_csv_checked(paths.release_dir() / "ledgers" / "evidence.csv")}
    ann_a = parse(a_path.read_text(encoding="utf-8").splitlines())
    ann_b = parse(b_path.read_text(encoding="utf-8").splitlines())
    comps = {row: compare_field(row, ann_a[row], ann_b[row])
             for row in expected if row not in owner_checked}
    disagreeing = [row for row, c in comps.items() if not c.fully_agreed]
    agreed = [row for row, c in comps.items() if c.fully_agreed]
    audited = agreement_audit_sample(agreed, sample)

    adj = parse_form(adj_path.read_text(encoding="utf-8"), sourced=True)
    audit = parse_form(audit_path.read_text(encoding="utf-8"), sourced=False)
    problems = []
    if list(adj) != disagreeing:
        problems.append("adjudication form fields differ from the pairing's selection")
    if list(audit) != audited:
        problems.append("audit form fields differ from the agreement-audit draw")
    for row, f in adj.items():
        text = ledger[row]["statistics"]
        shown = _shown(include_as_unstated(ann_a[row], text, row[0]),
                       include_as_unstated(ann_b[row], text, row[0]), row)
        if _form_rows(f) != shown:
            problems.append(f"{row}: adjudication rows altered")
    for row, f in audit.items():
        if _form_rows(f) != Counter(ann_a[row]):
            problems.append(f"{row}: audit rows altered")
    resolved = {**adj, **audit}
    lines = [json.dumps({"target_gene": r[0], "evidence_id": r[1],
                         "assertions": [{k: v for k, v in asdict(a).items() if k != "row"}
                                        for a in f.resolved]}) for r, f in resolved.items()]
    problems += check_format(lines, list(resolved), labels)
    errors = sum(f.changed for f in audit.values())
    lo, hi = wilson_interval(errors, len(audit))
    report = {
        "sample": sample,
        "inputs": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in (a_path, b_path, adj_path, audit_path)},
        "problems": problems,
        "adjudication": _summary(adj),
        "adjudication_changes": _changes(adj),
        "agreement_audit": {**_summary(audit), "fields_with_error": errors,
                            "error_rate": errors / len(audit) if audit else None,
                            "wilson_95": [lo, hi]},
        "agreement_audit_changes": _changes(audit),
        "dc33_full_review_triggered": errors > 0,
        "agreed_fields_not_audited": len(agreed) - len(audited),
    }
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
    logger.info("problems %d; adjudication %s; audit errors %d/%d; DC-33 %s",
                len(problems), json.dumps(report["adjudication"]), errors, len(audit),
                report["dc33_full_review_triggered"])
    for p in problems:
        logger.info("  %s", p)


if __name__ == "__main__":
    main()
