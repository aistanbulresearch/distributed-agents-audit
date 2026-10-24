"""Verify a pre-registration freeze before any comparison runs.

Two checks, both required (H1 pre-registration, section 10):
- local: every frozen artifact and the reference DE file still have the SHA-256 recorded in
  the freeze manifest, and the manifest itself is the one named in the freeze claim;
- archive: the latest complete Software Heritage visit of the public repository contains the
  annotated tag, the tag points to the claimed commit, the manifest archived at that commit has
  the claimed SHA-256, and the visit is not earlier than the tag.
The archive is queried live for the claimed tag, so a recorded but stale snapshot identifier
proves nothing on its own.
"""

import json
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from audit.lib.manifest import sha256_file

ApiGet = Callable[[str], dict]


class FreezeVerificationError(RuntimeError):
    """Raised when the freeze cannot be verified; the comparison must not run."""


@dataclass(frozen=True)
class FreezeClaim:
    origin: str  # public repository URL as archived by Software Heritage
    tag: str  # annotated tag, e.g. prereg-H1-v1
    commit: str  # git commit the tag must point to
    manifest_path: str  # repository path of the freeze manifest
    manifest_sha256: str


def verify_reference(manifest: dict, resolve_input: Callable[[str], Path]) -> None:
    """The reference DE file bound in ``manifest["reference"]`` (input key and SHA-256) must
    exist and match byte for byte."""
    ref = manifest.get("reference") or {}
    if not ref.get("key") or not ref.get("sha256"):
        raise FreezeVerificationError("freeze manifest does not bind a reference file")
    path = resolve_input(ref["key"])
    if not path.is_file():
        raise FreezeVerificationError(f"reference file missing: {ref['key']}")
    if sha256_file(path) != ref["sha256"]:
        raise FreezeVerificationError(f"reference file changed: {ref['key']}")


def verify_local(manifest: dict, resolve: Callable[[str], Path],
                 resolve_input: Callable[[str], Path]) -> None:
    """Every artifact listed in ``manifest["artifacts"]`` must match its recorded SHA-256, and
    so must the reference file."""
    changed = [path for path, digest in manifest["artifacts"].items()
               if sha256_file(resolve(path)) != digest]
    if changed:
        raise FreezeVerificationError("frozen artifacts changed: " + ", ".join(changed))
    verify_reference(manifest, resolve_input)


def verify_archive(claim: FreezeClaim, get: ApiGet) -> dict[str, str]:
    """Check the claim against Software Heritage; return a receipt for the run log."""
    visit = get(f"origin/{claim.origin}/visit/latest/?require_snapshot=true")
    if visit.get("status") != "full":
        raise FreezeVerificationError(
            f"latest archive visit is not complete: {visit.get('status')}")
    snapshot = visit["snapshot"]
    branches = get(f"snapshot/{snapshot}/?branches_from=refs/tags/{claim.tag}"
                   f"&branches_count=1")["branches"]
    branch = branches.get(f"refs/tags/{claim.tag}")
    if branch is None:
        raise FreezeVerificationError(f"tag {claim.tag} is not in the archived snapshot {snapshot}")
    if branch["target_type"] != "release":
        raise FreezeVerificationError(f"tag {claim.tag} is not an annotated tag")
    release = get(f"release/{branch['target']}/")
    if release["target"] != claim.commit:
        raise FreezeVerificationError(
            f"tag {claim.tag} points to {release['target']}, not {claim.commit}")
    archived = get(f"revision/{claim.commit}/directory/{claim.manifest_path}/")
    if archived["content"]["checksums"]["sha256"] != claim.manifest_sha256:
        raise FreezeVerificationError("archived manifest differs from the claimed manifest")
    if datetime.fromisoformat(visit["date"]) < datetime.fromisoformat(release["date"]):
        raise FreezeVerificationError("archive visit is dated before the tag")
    return {"snapshot": snapshot, "visit_date": visit["date"], "release": branch["target"],
            "commit": claim.commit, "tag_date": release["date"]}


def verify_freeze(claim: FreezeClaim, manifest_file: Path, resolve: Callable[[str], Path],
                  get: ApiGet, resolve_input: Callable[[str], Path]) -> dict[str, str]:
    """Full guard: the local manifest is the claimed one, its artifacts and the reference
    file match, and the archive holds the same manifest at the tagged commit."""
    if sha256_file(manifest_file) != claim.manifest_sha256:
        raise FreezeVerificationError("local manifest differs from the claimed manifest")
    verify_local(json.loads(manifest_file.read_text(encoding="utf-8")), resolve, resolve_input)
    return verify_archive(claim, get)
