"""Replay every H1 annotation generator in a fresh checkout and compare with the freeze.

Run from the root of a clone of the frozen branch, with the upstream submodule initialised
(LFS files fetched): uv run python -m audit.scripts.h1_replay_freeze

Checks the freeze manifest (every artifact and the reference DE file, byte for byte), then
regenerates into a scratch directory and compares byte for byte with the frozen files: the
samples, the five packets, the owner-check sheet, the blank forms, the pairing and tally
records and both resolved keys with their assembly record. Prints one line per check and
exits 1 on any difference. Reads evidence text only; never compares DE values with report
statistics and produces no extractor output.
"""

import json
import logging
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from audit.lib import paths
from audit.lib.freeze_check import verify_local
from audit.lib.manifest import sha256_file

logger = logging.getLogger(__name__)

REG = paths.REPO_ROOT / "registrations"
ANN = REG / "annotation"
SAMPLES = paths.REPO_ROOT / "audit" / "results" / "h1" / "annotation_samples.json"
_OUTPUT_LINE = re.compile(r"Write exactly one file: `([^`]+)`")


def _run(module: str, *args: object) -> None:
    subprocess.run([sys.executable, "-m", module, *map(str, args)], check=True,
                   capture_output=True, cwd=paths.REPO_ROOT)


def _same(label: str, made: Path, frozen: Path, failures: list[str]) -> None:
    ok = made.is_file() and sha256_file(made) == sha256_file(frozen)
    logger.info("%s %s", "ok  " if ok else "DIFF", label)
    if not ok:
        failures.append(label)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    paths.check_upstream_pin()
    manifest = json.loads((REG / "H1_freeze.json").read_text(encoding="utf-8"))
    verify_local(manifest, paths.REPO_ROOT.joinpath, paths.resolve_input)
    logger.info("ok   manifest: %d artifacts and the reference file", len(manifest["artifacts"]))
    failures: list[str] = []
    frozen_samples = SAMPLES.read_bytes()
    _run("audit.scripts.h1_draw_samples")
    ok = SAMPLES.read_bytes() == frozen_samples == (REG / "H1_samples.json").read_bytes()
    logger.info("%s samples", "ok  " if ok else "DIFF")
    if not ok:
        failures.append("samples")
        SAMPLES.write_bytes(frozen_samples)
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        packets = [(s, w, "H1_section3_rev10.md", f"H1_packet_sample{s}_{w}.md")
                   for s in (1, 2) for w in ("A", "B")]
        packets.append((1, "A", "H1_section3_rev8.md", "H1_packet_sample1_A_rev8.md"))
        for s, _, section3, name in packets:
            target = _OUTPUT_LINE.search((ANN / name).read_text(encoding="utf-8"))
            if target is None:
                failures.append(f"{name}: no output path")
                continue
            _run("audit.scripts.h1_build_packet", s, ANN / section3, target.group(1),
                 out / name)
            _same(name, out / name, ANN / name, failures)
        _run("audit.scripts.h1_owner_check_sheet", ANN / "H1_annotation_sample1_A_rev8.jsonl",
             out / "H1_owner_check.md")
        _same("H1_owner_check.md", out / "H1_owner_check.md", ANN / "H1_owner_check.md",
              failures)
        _run("audit.scripts.h1_owner_check_tally", ANN / "H1_owner_check_filled.md",
             out / "H1_owner_check_tally.json")
        _same("H1_owner_check_tally.json", out / "H1_owner_check_tally.json",
              ANN / "H1_owner_check_tally.json", failures)
        for s in (1, 2):
            pair = out / f"pair{s}"
            pair.mkdir()
            a = ANN / f"H1_annotation_sample{s}_A.jsonl"
            b = ANN / f"H1_annotation_sample{s}_B.jsonl"
            _run("audit.scripts.h1_pair_annotations", s, a, b, pair)
            name = f"H1_pairing_sample{s}.json"
            _same(name, pair / name, ANN / name, failures)
            for name in (f"H1_adjudication_sample{s}.md", f"H1_agreement_audit_sample{s}.md"):
                _same(f"blank/{name}", pair / name, ANN / "blank" / name, failures)
            name = f"H1_rulings_tally_sample{s}.json"
            _run("audit.scripts.h1_tally_rulings", s, a, b, ANN / f"H1_adjudication_sample{s}.md",
                 ANN / f"H1_agreement_audit_sample{s}.md", out / name)
            _same(name, out / name, ANN / name, failures)
        a1, b1 = ANN / "H1_annotation_sample1_A.jsonl", ANN / "H1_annotation_sample1_B.jsonl"
        _run("audit.scripts.h1_agreed_review_form", 1, a1, b1, out / "H1_agreed_review_sample1.md")
        _same("blank/H1_agreed_review_sample1.md", out / "H1_agreed_review_sample1.md",
              ANN / "blank" / "H1_agreed_review_sample1.md", failures)
        review = "H1_agreed_review_tally_sample1.json"
        _run("audit.scripts.h1_tally_agreed_review", 1, a1, b1,
             ANN / "H1_agreed_review_sample1_filled.md", out / review)
        _same(review, out / review, ANN / review, failures)
        keys = out / "keys"
        keys.mkdir()
        _run("audit.scripts.h1_assemble_keys", ANN, keys)
        for s in (1, 2):
            name = f"H1_annotation_sample{s}.jsonl"
            _same(name, keys / name, REG / name, failures)
        _same("H1_key_assembly.json", keys / "H1_key_assembly.json",
              ANN / "H1_key_assembly.json", failures)
    if failures:
        logger.info("replay FAILED: %s", ", ".join(failures))
        sys.exit(1)
    logger.info("replay clean: every regenerated file equals the frozen file")


if __name__ == "__main__":
    main()
