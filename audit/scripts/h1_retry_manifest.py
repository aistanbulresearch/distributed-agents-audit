"""Write the H1 retry manifest (deviation D-1): ``registrations/H1_retry.json``.

Run: uv run python -m audit.scripts.h1_retry_manifest

Binds the corrected parser, its tests, the development harness, the evaluation code, the
deviation record and the results that led to the retry, by SHA-256, to the commit that holds
them (HEAD, which must be clean), together with the reference file binding of the freeze
manifest. The tag ``prereg-H1-retry1`` is then put on the commit adding this manifest, and
``line_h1.py`` verifies it (locally and in the Software Heritage archive) before sample 2 is
touched.
"""

import json
import logging
import subprocess
import sys

from audit.lib import paths
from audit.lib.manifest import sha256_file

logger = logging.getLogger(__name__)

RETRY_FILES = (
    "audit/lib/h1_extract_v2.py",
    "tests/test_h1_extract_v2.py",
    "audit/scripts/h1_dev_gate.py",
    "audit/scripts/line_h1.py",
    "tests/test_line_h1.py",
    "audit/scripts/h1_retry_manifest.py",
    "registrations/H1_deviations.md",
    "audit/results/h1/line_h1_equivalence.json",
    "audit/results/h1/line_h1_gate_sample1_v1.json",
)
OUT = paths.REPO_ROOT / "registrations" / "H1_retry.json"


def _git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(paths.REPO_ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    if _git("status", "--porcelain", "--untracked-files=no"):
        sys.exit("working tree has uncommitted changes")
    freeze = json.loads((paths.REPO_ROOT / "registrations" / "H1_freeze.json")
                        .read_text(encoding="utf-8"))
    manifest = {
        "line": "H1", "deviation": "D-1", "tag": "prereg-H1-retry1",
        "freeze_tag": freeze["tag"], "freeze_code_commit": freeze["code_commit"],
        "code_commit": _git("rev-parse", "HEAD"),
        "reference": freeze["reference"],
        "artifacts": {f: sha256_file(paths.REPO_ROOT / f) for f in RETRY_FILES},
    }
    OUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    logger.info("wrote %s, sha256 %s", OUT, sha256_file(OUT))


if __name__ == "__main__":
    main()
