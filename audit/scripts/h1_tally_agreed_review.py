"""Tally the owner's filled full review of a sample's remaining agreed fields (DC-33).

Run: uv run python -m audit.scripts.h1_tally_agreed_review <sample: 1|2> <annotator_A.jsonl>
         <annotator_B.jsonl> <filled_review.md> <out.json>

Checks that the form covers exactly the agreed fields outside the agreement-audit draw (and
outside sample 1's owner-checked fields), that no displayed row was altered and that every
resolved assertion fits the codebook; reports the rulings. Reads evidence text only.
"""

import hashlib
import json
import logging
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from audit.lib import paths
from audit.lib.h1_annotation import check_format, compare_field, parse
from audit.lib.h1_rulings import parse_form
from audit.lib.h1_sampling import agreement_audit_sample
from audit.scripts.h1_tally_rulings import (
    RECON,
    SAMPLE_KEYS,
    SAMPLES,
    _changes,
    _form_rows,
    _summary,
)

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    sample = int(sys.argv[1])
    a_path, b_path, form_path, out_path = map(Path, sys.argv[2:6])
    paths.check_upstream_pin()
    samples = json.loads(SAMPLES.read_text(encoding="utf-8"))
    expected = [tuple(r) for r in samples[SAMPLE_KEYS[sample]]]
    owner_checked = {tuple(r) for r in samples["owner_check"]} if sample == 1 else set()
    labels = set(json.loads(RECON.read_text(encoding="utf-8"))
                 ["differential_expression"]["groups"])
    ann_a = parse(a_path.read_text(encoding="utf-8").splitlines())
    ann_b = parse(b_path.read_text(encoding="utf-8").splitlines())
    agreed = [row for row in expected if row not in owner_checked
              and compare_field(row, ann_a[row], ann_b[row]).fully_agreed]
    audited = set(agreement_audit_sample(agreed, sample))
    remaining = [row for row in agreed if row not in audited]

    review = parse_form(form_path.read_text(encoding="utf-8"), sourced=False)
    problems = []
    if list(review) != remaining:
        problems.append("review form fields differ from the remaining agreed fields")
    for row, f in review.items():
        if _form_rows(f) != Counter(ann_a[row]):
            problems.append(f"{row}: rows altered")
    lines = [json.dumps({"target_gene": r[0], "evidence_id": r[1],
                         "assertions": [{k: v for k, v in asdict(a).items() if k != "row"}
                                        for a in f.resolved]}) for r, f in review.items()]
    problems += check_format(lines, list(review), labels)
    report = {
        "sample": sample,
        "inputs": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in (a_path, b_path, form_path)},
        "problems": problems,
        "review": {**_summary(review),
                   "fields_with_error": sum(f.changed for f in review.values())},
        "review_changes": _changes(review),
    }
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
    logger.info("problems %d; review %s", len(problems), json.dumps(report["review"]))
    for p in problems:
        logger.info("  %s", p)


if __name__ == "__main__":
    main()
