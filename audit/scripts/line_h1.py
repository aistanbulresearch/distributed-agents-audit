"""Line H1: data consistency of quantitative evidence (pre-registration registrations/H1.md).

Run: uv run python -m audit.scripts.line_h1 <stage>

Stages, in the order the pre-registration fixes:
- ``equivalence``: section 2, the reference file against the 18-target upstream file;
- ``gate``: section 5, the frozen extractor against the frozen sample-1 key;
- ``compare``: section 6, every extracted assertion against the reference (only after the
  gate passed).
Every stage first runs the freeze guard (section 10: local artifacts, reference bytes and
the live Software Heritage archive) and aborts if it fails. Only the frozen extractor and
matcher are used; every choice beyond the pre-registration is listed in
``registrations/H1_deviations.md``. Results go to ``audit/results/h1/line_h1_<stage>.json``.
"""

import json
import logging
import sys
from pathlib import Path

import httpx
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

from audit.lib import corpus, paths
from audit.lib.freeze_check import FreezeClaim, verify_freeze
from audit.lib.h1_extract import Vocabulary, extract
from audit.lib.h1_quality import (
    Annotated,
    evaluate,
    extraction_errors,
    from_assertion,
    gate_intervals,
    passes,
)

logger = logging.getLogger(__name__)

REG = paths.REPO_ROOT / "registrations"
OUT = paths.REPO_ROOT / "audit" / "results" / "h1"
RECON = paths.REPO_ROOT / "audit" / "results" / "recon" / "inventory.json"
UPSTREAM_DE = (paths.UPSTREAM_ROOT / "data" / "inputs" / "biology"
               / "differential_expression.parquet")
CLAIM = FreezeClaim(
    origin="https://github.com/aistanbulresearch/distributed-agents-audit",
    tag="prereg-H1-v1", commit="7e04da3507c9fa915881d65eb52b2e547f750303",
    manifest_path="registrations/H1_freeze.json",
    manifest_sha256="f348e305c44727fb9d1d1395ede8c32771a6c5e68b1c1b76c5ea01a105859356")
SWH_API = "https://archive.softwareheritage.org/api/1/"
VALUE_COLUMNS = ("logfoldchanges", "pvals", "pvals_adj", "scores")
KEY_COLUMNS = ("gene_target", "group_name", "names")
REL_TOL, ABS_TOL, AGREE_MIN = 1e-6, 1e-12, 0.999


def reference_path() -> Path:
    manifest = json.loads((REG / "H1_freeze.json").read_text(encoding="utf-8"))
    return paths.resolve_input(manifest["reference"]["key"])


def guard() -> dict[str, str]:
    def get(path: str) -> dict:
        r = httpx.get(SWH_API + path, timeout=60, follow_redirects=True)
        r.raise_for_status()
        return r.json()
    paths.check_upstream_pin()
    receipt = verify_freeze(CLAIM, REG / "H1_freeze.json", paths.REPO_ROOT.joinpath, get,
                            paths.resolve_input)
    logger.info("guard passed: %s", receipt)
    return receipt


def write(stage: str, result: dict) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"line_h1_{stage}.json"
    out.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n", encoding="utf-8",
                   newline="\n")
    logger.info("wrote %s", out)
    return out


# --- section 2: equivalence --------------------------------------------------------------

def _distinct_keys(table: pa.Table) -> int:
    return table.group_by(list(KEY_COLUMNS)).aggregate([]).num_rows


def _close(u: pa.ChunkedArray, r: pa.ChunkedArray) -> pa.ChunkedArray:
    """Relative tolerance 1e-6, absolute 1e-12 near zero; both missing counts as agreeing."""
    u, r = pc.cast(u, pa.float64()), pc.cast(r, pa.float64())
    diff = pc.abs(pc.subtract(u, r))
    scale = pc.max_element_wise(pc.abs(u), pc.abs(r))
    ok = pc.or_(pc.less_equal(diff, ABS_TOL), pc.less_equal(diff, pc.multiply(scale, REL_TOL)))
    return pc.fill_null(pc.or_kleene(ok, pc.and_(pc.is_null(u), pc.is_null(r))), False)


def equivalence() -> dict:
    upstream = pq.read_table(UPSTREAM_DE)
    targets = sorted(pc.unique(upstream["gene_target"]).to_pylist())
    ref = pq.read_table(reference_path(), filters=[("gene_target", "in", targets)],
                        columns=upstream.column_names)
    up_keys, ref_keys = _distinct_keys(upstream), _distinct_keys(ref)
    joined = upstream.join(ref, keys=list(KEY_COLUMNS), join_type="inner",
                           left_suffix="_u", right_suffix="_r")
    result: dict = {"targets": len(targets), "rows_upstream": upstream.num_rows,
                    "rows_reference": ref.num_rows,
                    "duplicate_keys_upstream": upstream.num_rows - up_keys,
                    "duplicate_keys_reference": ref.num_rows - ref_keys,
                    "rows_joined": joined.num_rows,
                    "keys_only_upstream": up_keys - joined.num_rows,
                    "keys_only_reference": ref_keys - joined.num_rows}
    for col in ("n_pert_matched", "n_ctrl_matched"):
        unequal = pc.not_equal(joined[f"{col}_u"], joined[f"{col}_r"])
        result[f"{col}_unequal_rows"] = int(pc.sum(pc.fill_null(unequal, True)).as_py() or 0)
    agree_all = None
    for col in VALUE_COLUMNS:
        ok = _close(joined[f"{col}_u"], joined[f"{col}_r"])
        result[f"{col}_agreement"] = pc.mean(pc.cast(ok, pa.int8())).as_py()
        agree_all = ok if agree_all is None else pc.and_(agree_all, ok)
    result["all_value_columns_agreement"] = (
        pc.mean(pc.cast(agree_all, pa.int8())).as_py() if agree_all is not None else 0.0)
    result["passes"] = bool(
        result["keys_only_upstream"] == 0 and result["keys_only_reference"] == 0
        and result["duplicate_keys_upstream"] == 0 and result["duplicate_keys_reference"] == 0
        and result["n_pert_matched_unequal_rows"] == 0
        and result["n_ctrl_matched_unequal_rows"] == 0
        and all(result[f"{c}_agreement"] >= AGREE_MIN for c in VALUE_COLUMNS))
    return result


# --- section 3 vocabulary and section 5 gate ---------------------------------------------

def vocabulary() -> tuple[Vocabulary, dict]:
    """Cell-type labels and the distinct ``names`` of the reference file (section 3). The
    18-target file's names, used during development, are compared for the record."""
    groups = json.loads(RECON.read_text(encoding="utf-8"))["differential_expression"]["groups"]
    names: set[str] = set()
    for batch in pq.ParquetFile(reference_path()).iter_batches(columns=["names"],
                                                              batch_size=4_000_000):
        names.update(pc.unique(batch.column(0)).to_pylist())
    dev = set(pq.read_table(UPSTREAM_DE, columns=["names"])["names"].unique().to_pylist())
    info = {"reference_names": len(names), "development_names": len(dev),
            "only_reference": len(names - dev), "only_development": len(dev - names)}
    return Vocabulary(cell_types=tuple(groups), genes=frozenset(names)), info


def ledger() -> dict[tuple[str, str], dict]:
    return {(r["target_gene"], r["evidence_id"]): r for r in
            corpus.read_csv_checked(paths.release_dir() / "ledgers" / "evidence.csv")}


def load_key(path: Path) -> dict[tuple[str, str], list[Annotated]]:
    key = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        o = json.loads(line)
        row = (o["target_gene"], o["evidence_id"])
        key[row] = [Annotated(row=row, **a) for a in o["assertions"]]
    return key


def gate(sample: int = 1) -> dict:
    vocab, vocab_info = vocabulary()
    rows = ledger()
    key = load_key(REG / f"H1_annotation_sample{sample}.jsonl")
    annotated = [a for assertions in key.values() for a in assertions]
    extracted = []
    for row in key:
        r = rows[row]
        found = extract(r["statistics"], row[0], r["cell_type"] or None, vocab)
        extracted += [from_assertion(row, a) for a in found if a.status == "extracted"]
    report = evaluate(annotated, extracted)
    intervals = gate_intervals(report)
    return {
        "sample": sample, "vocabulary": vocab_info,
        "n_annotated": report.n_annotated, "n_extracted": report.n_extracted,
        "n_pairs": report.n_pairs,
        "recall": intervals["recall"], "precision": intervals["precision"],
        "binding_accuracy": intervals["binding_accuracy"],
        "recall_by_type": report.recall_by_type,
        "types_checked": sorted(report.types_checked),
        "extraction_errors": extraction_errors(report),
        "misbound_pairs": len(report.disagreements),
        "disagreements": [{"row": list(d["row"]), "value_text": d["value_text"],
                           "fields": d["fields"]} for d in report.disagreements],
        "passes": passes(report),
    }


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    stage = sys.argv[1]
    receipt = guard()
    if stage == "equivalence":
        result = equivalence()
    elif stage == "gate":
        result = gate(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    else:
        sys.exit(f"unknown stage {stage!r}")
    result["guard_receipt"] = receipt
    write(stage if stage != "gate" else f"gate_sample{result['sample']}", result)
    logger.info("%s", json.dumps({k: v for k, v in result.items()
                                  if k not in ("disagreements", "guard_receipt")}))


if __name__ == "__main__":
    main()
