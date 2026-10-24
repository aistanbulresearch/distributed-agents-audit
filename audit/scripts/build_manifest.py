"""Record SHA-256 digests of every input file the audit reads.

Run: uv run python -m audit.scripts.build_manifest
"""

import logging

from audit.lib import manifest, paths

logger = logging.getLogger(__name__)

_RELEASE = "src/distributed_agents/corpus/releases/shi/artifacts"

UPSTREAM_INPUTS = (
    f"{_RELEASE}/ledgers/findings.csv",
    f"{_RELEASE}/ledgers/references.csv",
    f"{_RELEASE}/ledgers/evidence.csv",
    f"{_RELEASE}/reports/reports.jsonl",
    f"{_RELEASE}/audits/claim_reconciliation.jsonl",
    f"{_RELEASE}/audits/claim_reconciliation.summary.json",
    f"{_RELEASE}/audits/claim_reconciliation_unassigned.jsonl",
    f"{_RELEASE}/audits/ledger_extraction.json",
    f"{_RELEASE}/audits/sourceguard_reconciliation.json",
    "data/inputs/biology/differential_expression.parquet",
    "data/inputs/literature/final_classified_findings.csv",
    "data/tables/scaling/single_agent_classifications.csv",
    "data/runs/shuffles/within_screen_reports_audits_150.jsonl",
    "data/runs/shuffles/out_of_screen_reports_audits_150.jsonl",
    "data/runs/reports/june/reports.jsonl",
    "data/runs/reports/july/reports.jsonl",
)

PREPRINT_INPUTS = tuple(f"media-{i}.{'pdf' if i == 1 else 'xlsx'}" for i in range(1, 7))

# perturbai/wholebrain_crispr_atlas at a pinned revision; the agents' DE input (H1 reference).
CACHE_INPUTS = (
    "hf/perturbai__wholebrain_crispr_atlas/a7c65dc0a64da4bd47cf6ef5f4dec6c7ef745e87/"
    "analysis/2603_shi_manuscript/diff_expr_genes/"
    "wilcoxon_de_results_group_name_final_data_no_multi_guide_cells.parquet",
)


def manifest_keys() -> list[str]:
    return (
        [f"upstream:{rel}" for rel in UPSTREAM_INPUTS]
        + [f"preprint:{name}" for name in PREPRINT_INPUTS]
        + [f"cache:{rel}" for rel in CACHE_INPUTS]
    )


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    paths.check_upstream_pin()
    files = {key: paths.resolve_input(key) for key in manifest_keys()}
    missing = [key for key, path in files.items() if not path.is_file()]
    if missing:
        raise FileNotFoundError("missing inputs: " + ", ".join(missing))
    paths.MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_manifest(paths.MANIFEST_PATH, manifest.digest_files(files))
    manifest.verify_manifest(paths.MANIFEST_PATH, paths.resolve_input)
    logger.info("wrote %d entries to %s", len(files), paths.MANIFEST_PATH)


if __name__ == "__main__":
    main()
