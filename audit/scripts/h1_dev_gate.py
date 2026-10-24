"""Development harness for the H1 parser retry (pre-registration section 5): sample 1 only.

Run: uv run python -m audit.scripts.h1_dev_gate [--fields] [--extractor v1|v2]

Scores an extractor against the frozen sample-1 key with the frozen gate code and, with
``--fields``, prints every field where the key and the extractor differ. It never loads the
sample-2 key and refuses to extract any sample-2 field, so no sample-2 extractor output exists
before the single pre-registered evaluation. Reads evidence text and gene names only.
"""

import importlib
import json
import logging
import sys
from collections import defaultdict

import pyarrow.parquet as pq

from audit.lib.h1_extract import Vocabulary
from audit.lib.h1_quality import correspondence_key, evaluate, from_assertion, passes
from audit.scripts.line_h1 import RECON, REG, UPSTREAM_DE, ledger, load_key

logger = logging.getLogger(__name__)


def sample2_rows() -> set[tuple[str, str]]:
    samples = json.loads((REG / "H1_samples.json").read_text(encoding="utf-8"))
    return {tuple(r) for r in samples["sample2_reserved"]}


def dev_vocabulary() -> Vocabulary:
    """Identical to the reference file's names (17,994; checked by the gate run)."""
    groups = json.loads(RECON.read_text(encoding="utf-8"))["differential_expression"]["groups"]
    names = pq.read_table(UPSTREAM_DE, columns=["names"])["names"].unique().to_pylist()
    return Vocabulary(cell_types=tuple(groups), genes=frozenset(names))


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    version = sys.argv[sys.argv.index("--extractor") + 1] if "--extractor" in sys.argv else "v2"
    module = importlib.import_module("audit.lib.h1_extract" + ("_v2" if version == "v2" else ""))
    vocab = dev_vocabulary()
    rows = ledger()
    key = load_key(REG / "H1_annotation_sample1.jsonl")
    forbidden = sample2_rows()
    if forbidden & set(key):
        sys.exit("sample-1 key overlaps sample 2")
    extracted, by_row = [], defaultdict(list)
    for row in key:
        r = rows[row]
        found = module.extract(r["statistics"], row[0], r["cell_type"] or None, vocab)
        got = [from_assertion(row, a) for a in found if a.status == "extracted"]
        extracted += got
        by_row[row] = got
    annotated = [a for v in key.values() for a in v]
    rep = evaluate(annotated, extracted)
    logger.info("%s recall %.3f precision %.3f binding %.3f by type %s pass %s", version,
                rep.recall, rep.precision, rep.binding_accuracy,
                {t: round(v, 3) for t, v in sorted(rep.recall_by_type.items())}, passes(rep))
    if "--fields" not in sys.argv:
        return
    for row, gold in key.items():
        got = by_row[row]
        pool = defaultdict(list)
        for g in got:
            pool[correspondence_key(g)].append(g)
        missed = []
        for a in gold:
            if pool[correspondence_key(a)]:
                pool[correspondence_key(a)].pop(0)
            else:
                missed.append(a)
        extra = [g for v in pool.values() for g in v]
        if missed or extra:
            print(f"\n=== {row[0]}/{row[1]} cell={rows[row]['cell_type']!r}")
            print("TEXT:", rows[row]["statistics"])
            for a in missed:
                print("  MISSED ", a.quantity, a.relation, a.value_text, a.cell_type, a.gene,
                      a.scope, a.unit, a.self_inclusion)
            for g in extra:
                print("  EXTRA  ", g.quantity, g.relation, g.value_text, g.cell_type, g.gene,
                      g.scope, g.unit, g.self_inclusion)


if __name__ == "__main__":
    main()
