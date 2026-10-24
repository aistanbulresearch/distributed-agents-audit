import pytest

from audit.lib import paths


def test_resolve_input_maps_sources():
    assert paths.resolve_input("upstream:data/x.csv") == paths.UPSTREAM_ROOT / "data/x.csv"
    assert paths.resolve_input("preprint:media-2.xlsx") == paths.PREPRINT_SUPP_DIR / "media-2.xlsx"


def test_resolve_input_maps_cache():
    key = "cache:hf/perturbai__wholebrain_crispr_atlas/rev/file.parquet"
    expected = paths.DATA_CACHE_DIR / "hf/perturbai__wholebrain_crispr_atlas/rev/file.parquet"
    assert paths.resolve_input(key) == expected
    assert not paths.DATA_CACHE_DIR.is_relative_to(paths.REPO_ROOT)


def test_resolve_input_rejects_unknown_source():
    with pytest.raises(ValueError, match="unknown manifest source"):
        paths.resolve_input("elsewhere:file.csv")


def test_release_dir_points_into_upstream():
    assert paths.release_dir("shi").is_relative_to(paths.UPSTREAM_ROOT)
    assert paths.release_dir("shi_holdout").name == "artifacts"
