"""Locations of the pinned upstream repository and local inputs."""

import os
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
UPSTREAM_ROOT = REPO_ROOT / "upstream" / "distributed_agent"
PINNED_COMMIT = "c20445d929f5aedce1d539ef6fbd8843b8c06e25"

# Supplementary tables of the preprint; read in place until the vendoring decision is made.
PREPRINT_SUPP_DIR = Path(
    os.environ.get("CORPUS_AUDIT_PREPRINT_DIR", REPO_ROOT.parent / "Preprint" / "supp material")
)


def release_dir(name: str = "shi") -> Path:
    """Return the artifacts directory of a corpus release (``shi`` or ``shi_holdout``)."""
    return UPSTREAM_ROOT / "src" / "distributed_agents" / "corpus" / "releases" / name / "artifacts"


# Large downloaded inputs (e.g. the full DE matrix); kept outside the repository.
DATA_CACHE_DIR = Path(
    os.environ.get("CORPUS_AUDIT_DATA_CACHE", REPO_ROOT.parent / "data-cache")
)

MANIFEST_PATH = REPO_ROOT / "inputs" / "MANIFEST.sha256"


def resolve_input(key: str) -> Path:
    """Map a manifest key (``upstream:``, ``preprint:`` or ``cache:`` + path) to a file path."""
    source, _, rel = key.partition(":")
    if source == "upstream":
        return UPSTREAM_ROOT / rel
    if source == "preprint":
        return PREPRINT_SUPP_DIR / rel
    if source == "cache":
        return DATA_CACHE_DIR / rel
    raise ValueError(f"unknown manifest source in key {key!r}")


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", "-c", "core.longpaths=true", "-C", str(UPSTREAM_ROOT), *args],
        capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def check_upstream_pin() -> None:
    """Raise RuntimeError unless upstream is at the pinned commit with no local changes."""
    head = _git("rev-parse", "HEAD")
    if head != PINNED_COMMIT:
        raise RuntimeError(f"upstream HEAD is {head}, expected pinned {PINNED_COMMIT}")
    dirty = _git("status", "--porcelain")
    if dirty:
        raise RuntimeError(f"upstream has local changes:\n{dirty}")
