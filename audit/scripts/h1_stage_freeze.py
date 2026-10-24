"""Stage the H1 freeze tree and its manifest (pre-registration section 10).

Run: uv run python -m audit.scripts.h1_stage_freeze <records_dir> <stage_dir>

Copies the committed repository tree (``git ls-files`` at HEAD, the upstream submodule
excluded; the working tree must be clean) and the annotation material from ``records_dir``
into ``registrations/`` under ``stage_dir``; rebuilds the blank forms from the raw files into
``registrations/annotation/blank/`` (the rebuilt pairing records must equal the stored ones);
checks that every file hash stated in a published receipt matches the published file; then
writes ``registrations/H1_freeze.json``: the SHA-256 of every staged file, the reference DE
file's input key and hash from the input manifest, and the upstream pin. The guard's local
check (artifacts and reference bytes) is run on the result, and again on a fresh clone of a
throwaway repository holding the staged tree. ``code_commit`` stays null here;
it is set when the clean branch is committed. ``stage_dir`` must not exist.
"""

import json
import logging
import re
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path

from audit.lib import paths
from audit.lib.freeze_check import FreezeVerificationError, verify_local
from audit.lib.manifest import read_manifest, sha256_file

logger = logging.getLogger(__name__)

DE_KEY_SUFFIX = "wilcoxon_de_results_group_name_final_data_no_multi_guide_cells.parquet"
# records_dir file → registrations/ path
REGISTRATIONS = {
    "H1.md": "H1.md",
    "keys/H1_annotation_sample1.jsonl": "H1_annotation_sample1.jsonl",
    "keys/H1_annotation_sample2.jsonl": "H1_annotation_sample2.jsonl",
    "keys/H1_key_assembly.json": "annotation/H1_key_assembly.json",
    "H1_section3_rev8.md": "annotation/H1_section3_rev8.md",
    "H1_section3_rev10.md": "annotation/H1_section3_rev10.md",
    "H1_annotator_prompt.md": "annotation/H1_packet_sample1_A_rev8.md",
    "H1_annotation_sample1_A_rev8.jsonl": "annotation/H1_annotation_sample1_A_rev8.jsonl",
    "H1_owner_check.md": "annotation/H1_owner_check.md",
    "H1_owner_check_filled.md": "annotation/H1_owner_check_filled.md",
    "H1_owner_check_tally.json": "annotation/H1_owner_check_tally.json",
    "H1_agreed_review_sample1_filled.md": "annotation/H1_agreed_review_sample1_filled.md",
    "H1_agreed_review_tally_sample1.json": "annotation/H1_agreed_review_tally_sample1.json",
}
for _s in (1, 2):
    for _who in ("A", "B"):
        REGISTRATIONS[f"H1_packet_sample{_s}_{_who}.md"] = (
            f"annotation/H1_packet_sample{_s}_{_who}.md")
        REGISTRATIONS[f"H1_annotation_sample{_s}_{_who}.jsonl"] = (
            f"annotation/H1_annotation_sample{_s}_{_who}.jsonl")
    for _name in (f"H1_adjudication_sample{_s}.md", f"H1_agreement_audit_sample{_s}.md",
                  f"H1_pairing_sample{_s}.json", f"H1_rulings_tally_sample{_s}.json"):
        REGISTRATIONS[_name] = f"annotation/{_name}"


def _git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(paths.REPO_ROOT), *args], check=True,
                          capture_output=True, text=True).stdout


def _run(module: str, *args: str) -> None:
    subprocess.run([sys.executable, "-m", module, *args], check=True, capture_output=True,
                   cwd=paths.REPO_ROOT)


def regenerate_blank_forms(records: Path, blank: Path, scratch: Path) -> None:
    """Rebuild the blank forms from the raw files into ``blank`` and require the rebuilt
    pairing records to equal the stored ones byte for byte."""
    blank.mkdir(parents=True)
    for s in ("1", "2"):
        out = scratch / f"sample{s}"
        out.mkdir(parents=True)
        _run("audit.scripts.h1_pair_annotations", s,
             str(records / f"H1_annotation_sample{s}_A.jsonl"),
             str(records / f"H1_annotation_sample{s}_B.jsonl"), str(out))
        pairing = f"H1_pairing_sample{s}.json"
        if sha256_file(out / pairing) != sha256_file(records / pairing):
            sys.exit(f"{pairing} does not reproduce from the raw files")
        for form in (f"H1_adjudication_sample{s}.md", f"H1_agreement_audit_sample{s}.md"):
            shutil.copy2(out / form, blank / form)
    _run("audit.scripts.h1_agreed_review_form", "1",
         str(records / "H1_annotation_sample1_A.jsonl"),
         str(records / "H1_annotation_sample1_B.jsonl"),
         str(blank / "H1_agreed_review_sample1.md"))


def _hash_claims(obj: object) -> list[tuple[str, str]]:
    """(file name, SHA-256) pairs a receipt states: name→hash maps and {path|key, sha256}."""
    found: list[tuple[str, str]] = []
    if isinstance(obj, dict):
        name = obj.get("path") or obj.get("key")
        if isinstance(name, str) and isinstance(obj.get("sha256"), str):
            found.append((name, obj["sha256"]))
        for k, v in obj.items():
            if isinstance(v, str) and re.fullmatch(r"[0-9a-f]{64}", v) and "." in k:
                found.append((k, v))
            else:
                found += _hash_claims(v)
    elif isinstance(obj, list):
        for v in obj:
            found += _hash_claims(v)
    return found


def check_receipts(registrations: Path) -> list[str]:
    """Every file hash stated in a published JSON receipt must match the published file of
    that name (blank forms for the pairing records' ``forms``)."""
    problems = []
    for receipt in sorted(registrations.rglob("*.json")):
        if receipt.name == "H1_freeze.json":  # the manifest; checked by verify_local
            continue
        data = json.loads(receipt.read_text(encoding="utf-8"))
        claims = _hash_claims({k: v for k, v in data.items() if k != "forms"})
        claims += [(f"blank/{n}", h) for n, h in data.get("forms", {}).items()]
        for name, digest in claims:
            candidates = [registrations / name, registrations / "annotation" / name]
            match = [c for c in candidates if c.is_file()]
            if not match:
                problems.append(f"{receipt.name}: {name} is not published")
            elif sha256_file(match[0]) != digest:
                problems.append(f"{receipt.name}: {name} hash differs")
    return problems


def git_round_trip(stage: Path, manifest: dict, scratch: Path,
                   resolve_input: Callable[[str], Path]) -> list[str]:
    """Commit the staged tree to a throwaway repository and clone it with line-ending
    conversion on (the worst case on Windows); the checkout must still match the manifest
    and every receipt."""
    src, out = scratch / "src", scratch / "checkout"
    shutil.copytree(stage, src)
    git = ["git", "-c", "core.autocrlf=true", "-c", "user.name=freeze-check",
           "-c", "user.email=freeze-check@localhost"]
    for args in (["init", "-q", str(src)], ["-C", str(src), "add", "-A"],
                 ["-C", str(src), "commit", "-q", "-m", "round trip"],
                 ["clone", "-q", str(src), str(out)]):
        subprocess.run(git + args, check=True, capture_output=True)
    problems = []
    try:
        verify_local(manifest, out.joinpath, resolve_input)
    except FreezeVerificationError as e:
        problems.append(str(e))
    return problems + check_receipts(out / "registrations")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    records, stage = Path(sys.argv[1]), Path(sys.argv[2])
    paths.check_upstream_pin()
    if _git("status", "--porcelain", "--untracked-files=no").strip():
        sys.exit("working tree has uncommitted changes")
    stage.mkdir(parents=True)
    with tempfile.TemporaryDirectory() as scratch:
        regenerate_blank_forms(records, stage / "registrations" / "annotation" / "blank",
                               Path(scratch))
    tracked = [f for f in _git("ls-files").splitlines()
               if f and not f.startswith("upstream/distributed_agent")]
    for rel in tracked:
        (stage / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(paths.REPO_ROOT / rel, stage / rel)
    for src, dest in REGISTRATIONS.items():
        target = stage / "registrations" / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(records / src, target)
    shutil.copy2(paths.REPO_ROOT / "audit" / "results" / "h1" / "annotation_samples.json",
                 stage / "registrations" / "H1_samples.json")
    problems = check_receipts(stage / "registrations")
    if problems:
        sys.exit("receipt check failed:\n" + "\n".join(problems))
    inputs = read_manifest(paths.MANIFEST_PATH)
    de = [(k, v) for k, v in inputs.items() if k.endswith(DE_KEY_SUFFIX)]
    if len(de) != 1:
        sys.exit("reference DE file not found exactly once in the input manifest")
    files = sorted(p.relative_to(stage).as_posix() for p in stage.rglob("*") if p.is_file())
    manifest = {
        "line": "H1", "tag": "prereg-H1-v1", "code_commit": None,
        "source_commit": _git("rev-parse", "HEAD").strip(),
        "upstream_pin": paths.PINNED_COMMIT,
        "reference": {"key": de[0][0], "sha256": de[0][1]},
        "artifacts": {f: sha256_file(stage / f) for f in files},
    }
    verify_local(manifest, stage.joinpath, paths.resolve_input)
    out = stage / "registrations" / "H1_freeze.json"
    out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    with tempfile.TemporaryDirectory() as scratch:
        problems = git_round_trip(stage, manifest, Path(scratch), paths.resolve_input)
    if problems:
        sys.exit("git round trip failed:\n" + "\n".join(problems))
    logger.info("staged %d files in %s; git round trip clean; manifest sha256 %s",
                len(files), stage, sha256_file(out))


if __name__ == "__main__":
    main()
