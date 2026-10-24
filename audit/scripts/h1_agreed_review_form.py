"""Build the full review form of a sample's remaining agreed fields (decision DC-33).

Run: uv run python -m audit.scripts.h1_agreed_review_form <sample: 1|2> <annotator_A.jsonl>
         <annotator_B.jsonl> <form_out.md>

Triggered when the owner finds an error among a sample's 20 audited agreed fields: every
other fully agreed field of that sample (outside sample 1's owner-checked fields) is reviewed
the same way. Same layout as the agreement-audit form. Reads evidence text only.
"""

import json
import logging
import sys
from pathlib import Path

from audit.lib import corpus, paths
from audit.lib.h1_annotation import compare_field, parse
from audit.lib.h1_sampling import agreement_audit_sample
from audit.scripts.h1_pair_annotations import (
    AUDIT_COLUMNS,
    MISSED,
    SAMPLE_KEYS,
    SAMPLES,
    _cells,
    _field_head,
    _sha256,
)

logger = logging.getLogger(__name__)

HEAD = """# H1 annotation, sample {n}: full review of the remaining agreed fields (DC-33)

The agreement audit of this sample found an error, so every other field where both
annotators produced identical annotations is now reviewed, as fixed in advance (decision
DC-33). {count} fields. Check each against section 3 (`H1_section3_rev10.md`): mark every row
`✓` or `✗` (`✗ → field=value` for a correction), and add any in-scope assertion both missed
under **Missed by both**.

Türkçe özet: Uzlaşma denetiminde bir hata bulunduğu için, bu örneklemde iki notlayıcının tamamen
anlaştığı diğer tüm metinler inceleniyor. Her satırı ✓ veya ✗ ile işaretleyin, ikisinin de
atladığı ölçümleri ekleyin.

"""


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    sample = int(sys.argv[1])
    a_path, b_path, out_path = Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
    paths.check_upstream_pin()
    samples = json.loads(SAMPLES.read_text(encoding="utf-8"))
    expected = [tuple(r) for r in samples[SAMPLE_KEYS[sample]]]
    owner_checked = {tuple(r) for r in samples["owner_check"]} if sample == 1 else set()
    ann_a = parse(a_path.read_text(encoding="utf-8").splitlines())
    ann_b = parse(b_path.read_text(encoding="utf-8").splitlines())
    agreed = [row for row in expected if row not in owner_checked
              and compare_field(row, ann_a[row], ann_b[row]).fully_agreed]
    audited = set(agreement_audit_sample(agreed, sample))
    remaining = [row for row in agreed if row not in audited]
    ledger = {(r["target_gene"], r["evidence_id"]): r for r in
              corpus.read_csv_checked(paths.release_dir() / "ledgers" / "evidence.csv")}
    parts = [HEAD.format(n=sample, count=len(remaining))]
    for i, row in enumerate(remaining, start=1):
        rows = [f"| {n} | " + " | ".join(_cells(a)) + " |  |"
                for n, a in enumerate(ann_a[row], start=1)]
        body = (AUDIT_COLUMNS + "\n" + "\n".join(rows) + "\n\n" if rows else
                "*Both annotators found no in-scope assertion in this field.*\n\n")
        parts.append(_field_head(i, row, ledger[row]) + body + MISSED + "\n---\n\n")
    out_path.write_text("".join(parts), encoding="utf-8", newline="\n")
    logger.info("%d remaining agreed fields; wrote %s, sha256 %s", len(remaining), out_path,
                _sha256(out_path))


if __name__ == "__main__":
    main()
