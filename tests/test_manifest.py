from pathlib import Path

import pytest

from audit.lib import manifest


def _files(tmp_path: Path) -> dict[str, Path]:
    a = tmp_path / "a.csv"
    b = tmp_path / "b.bin"
    a.write_text("x,y\n1,2\n", encoding="utf-8")
    b.write_bytes(b"\x00\x01\x02")
    return {"upstream:a.csv": a, "preprint:b.bin": b}


def test_roundtrip_verifies(tmp_path):
    files = _files(tmp_path)
    out = tmp_path / "MANIFEST.sha256"
    manifest.write_manifest(out, manifest.digest_files(files))

    manifest.verify_manifest(out, files.__getitem__)


def test_verify_manifest_detects_change(tmp_path):
    files = _files(tmp_path)
    out = tmp_path / "MANIFEST.sha256"
    manifest.write_manifest(out, manifest.digest_files(files))

    files["preprint:b.bin"].write_bytes(b"\x00\x01\x03")

    with pytest.raises(manifest.ManifestMismatch, match="preprint:b.bin"):
        manifest.verify_manifest(out, files.__getitem__)


def test_manifest_is_sorted_and_stable(tmp_path):
    files = _files(tmp_path)
    out = tmp_path / "MANIFEST.sha256"
    manifest.write_manifest(out, manifest.digest_files(files))

    keys = [line.split("  ", 1)[1] for line in out.read_text(encoding="utf-8").splitlines()]
    assert keys == sorted(keys)
