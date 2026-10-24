"""Build an H1 annotator packet for sample 1 or sample 2.

Run: uv run python -m audit.scripts.h1_build_packet <sample: 1|2> <section3.md>
         <annotation_output_path> <packet_out.md>

Inputs: the frozen samples file, the evidence ledger (text only), the recon cell-type labels,
the packet template and the frozen section-3 text. Prints the packet's SHA-256.
"""

import hashlib
import json
import logging
import sys
from pathlib import Path

from audit.lib import corpus, paths
from audit.lib.h1_packet import build_packet

logger = logging.getLogger(__name__)

SAMPLES = paths.REPO_ROOT / "audit" / "results" / "h1" / "annotation_samples.json"
RECON = paths.REPO_ROOT / "audit" / "results" / "recon" / "inventory.json"
TEMPLATE = paths.REPO_ROOT / "audit" / "templates" / "h1_annotator_packet.md"
SAMPLE_KEYS = {"1": "sample1", "2": "sample2_reserved"}


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    sample, section3_path, output_path, packet_out = sys.argv[1:5]
    paths.check_upstream_pin()
    samples = json.loads(SAMPLES.read_text(encoding="utf-8"))
    wanted = [tuple(r) for r in samples[SAMPLE_KEYS[sample]]]
    ledger = {(r["target_gene"], r["evidence_id"]): r for r in
              corpus.read_csv_checked(paths.release_dir() / "ledgers" / "evidence.csv")}
    groups = json.loads(RECON.read_text(encoding="utf-8"))["differential_expression"]["groups"]
    packet = build_packet(TEMPLATE.read_text(encoding="utf-8"), output_path, groups,
                          Path(section3_path).read_text(encoding="utf-8"),
                          [ledger[key] for key in wanted])
    Path(packet_out).write_text(packet, encoding="utf-8", newline="\n")
    logger.info("wrote %s (%d chars), sha256 %s", packet_out, len(packet),
                hashlib.sha256(packet.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
