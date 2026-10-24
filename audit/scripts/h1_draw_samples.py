"""Draw H1's two annotation samples with the frozen sampler (row identifiers only).

Run: uv run python -m audit.scripts.h1_draw_samples

Reads only ``target_gene``, ``evidence_id`` and whether ``statistics`` is non-empty; no DE
data. Writes the population size, the SHA-256 of the canonical population list and both
samples' row identifiers. At the freeze this file is published as
``registrations/H1_samples.json``.
"""

import hashlib
import json
import logging

from audit.lib import corpus, paths
from audit.lib.h1_sampling import (
    ANNOTATION_SEEDS,
    ANNOTATION_SIZE,
    OWNER_CHECK_SEED,
    annotation_population,
    draw_annotation_samples,
    owner_check_sample,
)

logger = logging.getLogger(__name__)

OUT = paths.REPO_ROOT / "audit" / "results" / "h1" / "annotation_samples.json"


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    paths.check_upstream_pin()
    rows = corpus.read_csv_checked(paths.release_dir() / "ledgers" / "evidence.csv")
    population = annotation_population(rows)
    canonical = json.dumps(population, separators=(",", ":")).encode("utf-8")
    first, second = draw_annotation_samples(population)
    result = {
        "population": "non-control evidence rows with non-empty statistics, upstream c20445d",
        "population_size": len(population),
        "population_sha256": hashlib.sha256(canonical).hexdigest(),
        "seeds": list(ANNOTATION_SEEDS),
        "size": ANNOTATION_SIZE,
        "sample1": [list(r) for r in first],
        "sample2_reserved": [list(r) for r in second],
        "owner_check_seed": OWNER_CHECK_SEED,
        "owner_check": [list(r) for r in owner_check_sample(first)],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8", newline="\n")
    logger.info("wrote %s (population %d)", OUT, len(population))


if __name__ == "__main__":
    main()
