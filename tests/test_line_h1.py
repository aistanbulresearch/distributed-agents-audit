"""Single-attempt and pairing rules of the H1 gate stage (deviation D-1; review round 17).

These tests never load a key or extract a field: they stop before any sample data is read.
"""

import json

import pytest

from audit.scripts import line_h1


def test_only_the_prescribed_sample_extractor_pairs_run(monkeypatch):
    def fail(*_args, **_kwargs):
        raise AssertionError("must not get this far")
    monkeypatch.setattr(line_h1, "load_key", fail)
    monkeypatch.setattr(line_h1, "retry_guard", fail)
    for sample, version in ((2, "v1"), (1, "v2"), (3, "v2")):
        with pytest.raises(SystemExit, match="not allowed"):
            line_h1.gate(sample, version, {})


def test_attempt_reservation_is_atomic_and_never_repeats(tmp_path):
    path = tmp_path / "attempt.json"
    line_h1.reserve_attempt(path, {"n": 1})
    assert json.loads(path.read_text(encoding="utf-8")) == {"n": 1}
    with pytest.raises(SystemExit, match="already made"):
        line_h1.reserve_attempt(path, {"n": 2})
    assert json.loads(path.read_text(encoding="utf-8")) == {"n": 1}


def test_sample2_needs_the_retry_guard_before_the_reservation_and_the_key(monkeypatch, tmp_path):
    order = []
    monkeypatch.setattr(line_h1, "ATTEMPT", tmp_path / "attempt.json")

    def no_claim():
        order.append("retry_guard")
        raise SystemExit("no published retry claim")
    monkeypatch.setattr(line_h1, "retry_guard", no_claim)
    monkeypatch.setattr(line_h1, "load_key", lambda *_: order.append("load_key"))
    with pytest.raises(SystemExit, match="no published retry claim"):
        line_h1.gate(2, "v2", {})
    assert order == ["retry_guard"]
    assert not (tmp_path / "attempt.json").exists()


def test_reserved_attempt_blocks_before_the_key_is_read(monkeypatch, tmp_path):
    attempt = tmp_path / "attempt.json"
    attempt.write_text("{}", encoding="utf-8")
    monkeypatch.setattr(line_h1, "ATTEMPT", attempt)
    monkeypatch.setattr(line_h1, "retry_guard", lambda: {"commit": "x"})

    def fail(*_args, **_kwargs):
        raise AssertionError("key must not be read")
    monkeypatch.setattr(line_h1, "load_key", fail)
    monkeypatch.setattr(line_h1, "vocabulary", fail)
    with pytest.raises(SystemExit, match="already made"):
        line_h1.gate(2, "v2", {})
