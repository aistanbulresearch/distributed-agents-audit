"""Freeze verification against local files and the Software Heritage archive.

Response shapes follow the live Software Heritage API (checked 2026-10-23 on a public repo).
"""

import json

import pytest

from audit.lib.freeze_check import (
    FreezeClaim,
    FreezeVerificationError,
    verify_archive,
    verify_freeze,
    verify_local,
)

ORIGIN = "https://github.com/example/distributed-agents-audit"
TAG = "prereg-H1-v1"
COMMIT = "a" * 40
RELEASE = "b" * 40
SNAPSHOT = "c" * 40
MANIFEST_PATH = "registrations/H1_freeze.json"
MANIFEST_SHA = "d" * 64


def _api(**overrides):
    responses = {
        f"origin/{ORIGIN}/visit/latest/?require_snapshot=true":
            {"date": "2026-11-01T10:00:00+00:00", "status": "full", "snapshot": SNAPSHOT},
        f"snapshot/{SNAPSHOT}/?branches_from=refs/tags/{TAG}&branches_count=1":
            {"branches": {f"refs/tags/{TAG}": {"target": RELEASE, "target_type": "release"}}},
        f"release/{RELEASE}/":
            {"target": COMMIT, "target_type": "revision", "date": "2026-11-01T09:00:00+00:00"},
        f"revision/{COMMIT}/directory/{MANIFEST_PATH}/":
            {"type": "file", "content": {"checksums": {"sha256": MANIFEST_SHA}}},
    }
    responses.update(overrides)
    return lambda path: responses[path]


CLAIM = FreezeClaim(origin=ORIGIN, tag=TAG, commit=COMMIT, manifest_path=MANIFEST_PATH,
                    manifest_sha256=MANIFEST_SHA)


def test_archive_linkage_verified():
    receipt = verify_archive(CLAIM, _api())

    assert receipt == {"snapshot": SNAPSHOT, "visit_date": "2026-11-01T10:00:00+00:00",
                       "release": RELEASE, "commit": COMMIT,
                       "tag_date": "2026-11-01T09:00:00+00:00"}


def test_snapshot_without_the_tag_is_rejected():
    stale = {f"snapshot/{SNAPSHOT}/?branches_from=refs/tags/{TAG}&branches_count=1":
             {"branches": {"refs/tags/prereg-H1-v0": {"target": RELEASE,
                                                       "target_type": "release"}}}}
    with pytest.raises(FreezeVerificationError, match="not in the archived snapshot"):
        verify_archive(CLAIM, _api(**stale))


def test_tag_pointing_to_another_commit_is_rejected():
    moved = {f"release/{RELEASE}/": {"target": "e" * 40, "target_type": "revision",
                                    "date": "2026-11-01T09:00:00+00:00"}}
    with pytest.raises(FreezeVerificationError, match="points to"):
        verify_archive(CLAIM, _api(**moved))


def test_replaced_manifest_is_rejected():
    replaced = {f"revision/{COMMIT}/directory/{MANIFEST_PATH}/":
                {"type": "file", "content": {"checksums": {"sha256": "f" * 64}}}}
    with pytest.raises(FreezeVerificationError, match="archived manifest"):
        verify_archive(CLAIM, _api(**replaced))


def test_visit_before_the_tag_is_rejected():
    early = {f"origin/{ORIGIN}/visit/latest/?require_snapshot=true":
             {"date": "2026-11-01T08:00:00+00:00", "status": "full", "snapshot": SNAPSHOT}}
    with pytest.raises(FreezeVerificationError, match="before the tag"):
        verify_archive(CLAIM, _api(**early))


def test_incomplete_visit_is_rejected():
    partial = {f"origin/{ORIGIN}/visit/latest/?require_snapshot=true":
               {"date": "2026-11-01T10:00:00+00:00", "status": "partial", "snapshot": SNAPSHOT}}
    with pytest.raises(FreezeVerificationError, match="not complete"):
        verify_archive(CLAIM, _api(**partial))


def test_lightweight_tag_is_rejected():
    light = {f"snapshot/{SNAPSHOT}/?branches_from=refs/tags/{TAG}&branches_count=1":
             {"branches": {f"refs/tags/{TAG}": {"target": COMMIT, "target_type": "revision"}}}}
    with pytest.raises(FreezeVerificationError, match="annotated"):
        verify_archive(CLAIM, _api(**light))


def _write(tmp_path, name, text):
    path = tmp_path / name
    path.write_text(text, encoding="utf-8", newline="\n")
    return path


REF_KEY = "cache:hf/de.parquet"


def _frozen(tmp_path):
    """A frozen artifact and a reference file, with a manifest binding both."""
    from audit.lib.manifest import sha256_file
    code = _write(tmp_path, "h1_extract.py", "x = 1\n")
    (tmp_path / "cache" / "hf").mkdir(parents=True)
    ref = _write(tmp_path / "cache" / "hf", "de.parquet", "reference bytes")
    manifest = {"artifacts": {"h1_extract.py": sha256_file(code)},
                "reference": {"key": REF_KEY, "sha256": sha256_file(ref)}}
    resolve_input = lambda key: tmp_path / "cache" / key.partition(":")[2]  # noqa: E731
    return code, ref, manifest, resolve_input


def test_local_artifact_change_is_rejected(tmp_path):
    code, _, manifest, resolve_input = _frozen(tmp_path)
    verify_local(manifest, tmp_path.joinpath, resolve_input)

    code.write_text("x = 2\n", encoding="utf-8")
    with pytest.raises(FreezeVerificationError, match="h1_extract.py"):
        verify_local(manifest, tmp_path.joinpath, resolve_input)


def test_changed_reference_is_rejected_while_artifacts_match(tmp_path):
    _, ref, manifest, resolve_input = _frozen(tmp_path)
    ref.write_text("substituted bytes", encoding="utf-8")
    with pytest.raises(FreezeVerificationError, match="reference file changed"):
        verify_local(manifest, tmp_path.joinpath, resolve_input)


def test_missing_reference_is_rejected_while_artifacts_match(tmp_path):
    _, ref, manifest, resolve_input = _frozen(tmp_path)
    ref.unlink()
    with pytest.raises(FreezeVerificationError, match="reference file missing"):
        verify_local(manifest, tmp_path.joinpath, resolve_input)


def test_manifest_without_reference_binding_is_rejected(tmp_path):
    _, _, manifest, resolve_input = _frozen(tmp_path)
    for broken in ({k: v for k, v in manifest.items() if k != "reference"},
                   {**manifest, "reference": {"key": REF_KEY, "sha256": ""}}):
        with pytest.raises(FreezeVerificationError, match="does not bind"):
            verify_local(broken, tmp_path.joinpath, resolve_input)


def test_regenerated_local_manifest_does_not_match_the_claim(tmp_path):
    _, _, manifest, resolve_input = _frozen(tmp_path)
    manifest_file = _write(tmp_path, "H1_freeze.json", json.dumps(manifest))

    with pytest.raises(FreezeVerificationError, match="local manifest"):
        verify_freeze(CLAIM, manifest_file, tmp_path.joinpath, _api(), resolve_input)


def test_full_guard_passes_when_everything_matches(tmp_path):
    from audit.lib.manifest import sha256_file
    _, _, manifest, resolve_input = _frozen(tmp_path)
    manifest_file = _write(tmp_path, "H1_freeze.json", json.dumps(manifest))
    claim = FreezeClaim(origin=ORIGIN, tag=TAG, commit=COMMIT, manifest_path=MANIFEST_PATH,
                        manifest_sha256=sha256_file(manifest_file))
    api = _api(**{f"revision/{COMMIT}/directory/{MANIFEST_PATH}/":
                  {"type": "file",
                   "content": {"checksums": {"sha256": sha256_file(manifest_file)}}}})
    receipt = verify_freeze(claim, manifest_file, tmp_path.joinpath, api, resolve_input)
    assert receipt["commit"] == COMMIT
