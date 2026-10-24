"""Development diagnostics for the H1 extractor (text and vocabularies only).

Run: uv run python -m audit.scripts.h1_extraction_diagnostics

Counts extraction outcomes over the evidence ledger. Reads no DE value column: the gene
vocabulary is the distinct ``names`` of the released 18-target DE file and the cell-type
labels come from the recon inventory. These are diagnostics of the parser during
development, not H1 results.
"""

import json
import logging
from collections import Counter

import pyarrow.parquet as pq

from audit.lib import corpus, paths
from audit.lib.h1_extract import Vocabulary, extract

logger = logging.getLogger(__name__)

OUT = paths.REPO_ROOT / "audit" / "results" / "h1" / "extraction_diagnostics.json"
RECON = paths.REPO_ROOT / "audit" / "results" / "recon" / "inventory.json"
RELEASED_DE = (
    paths.UPSTREAM_ROOT / "data" / "inputs" / "biology" / "differential_expression.parquet"
)


def build_vocabulary() -> Vocabulary:
    groups = json.loads(RECON.read_text(encoding="utf-8"))["differential_expression"]["groups"]
    names = pq.read_table(RELEASED_DE, columns=["names"])["names"].unique().to_pylist()
    return Vocabulary(cell_types=tuple(groups), genes=frozenset(names))


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    paths.check_upstream_pin()
    vocab = build_vocabulary()
    status: Counter[str] = Counter()
    quantity: Counter[str] = Counter()
    reason: Counter[str] = Counter()
    source: Counter[str] = Counter()
    rows = rows_with_extracted = 0
    for row in corpus.read_csv_checked(paths.release_dir() / "ledgers" / "evidence.csv"):
        if corpus.is_control(row["target_gene"]):
            continue
        rows += 1
        found = extract(row["statistics"], row["target_gene"], row["cell_type"], vocab)
        rows_with_extracted += any(a.status == "extracted" for a in found)
        for a in found:
            status[a.status] += 1
            reason[a.reason or "none"] += 1
            if a.status == "extracted":
                quantity[a.quantity] += 1
                source[a.cell_source or "none"] += 1
    result = {
        "gene_vocabulary_size": len(vocab.genes),
        "non_control_evidence_rows": rows,
        "rows_with_extracted_assertion": rows_with_extracted,
        "assertions_by_status": dict(status),
        "extracted_by_quantity": dict(quantity),
        "assertions_by_reason": dict(reason),
        "extracted_by_cell_source": dict(source),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    logger.info("wrote %s", OUT)


if __name__ == "__main__":
    main()
