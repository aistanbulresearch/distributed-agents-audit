"""SHA-256 manifest of every input file the audit reads."""

import hashlib
from collections.abc import Callable, Mapping
from pathlib import Path

_CHUNK = 1 << 20


class ManifestMismatch(RuntimeError):
    """Raised when an input file no longer matches its recorded digest."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while chunk := handle.read(_CHUNK):
            digest.update(chunk)
    return digest.hexdigest()


def digest_files(files: Mapping[str, Path]) -> dict[str, str]:
    """Map each manifest key to the SHA-256 of its file."""
    return {key: sha256_file(path) for key, path in files.items()}


def write_manifest(path: Path, digests: Mapping[str, str]) -> None:
    """Write ``<sha256>  <key>`` lines, sorted by key."""
    lines = [f"{digests[key]}  {key}" for key in sorted(digests)]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def read_manifest(path: Path) -> dict[str, str]:
    entries = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, key = line.split("  ", 1)
            entries[key] = digest
    return entries


def verify_manifest(path: Path, resolve: Callable[[str], Path]) -> None:
    """Raise ManifestMismatch listing every key whose file digest changed."""
    changed = [
        key for key, digest in read_manifest(path).items() if sha256_file(resolve(key)) != digest
    ]
    if changed:
        raise ManifestMismatch("input files changed: " + ", ".join(changed))
