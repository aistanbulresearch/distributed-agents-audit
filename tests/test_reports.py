from audit.lib import reports

REPORT = """# Report

## Key Biological Findings
[F001] something

## Structured Appendix

### Literature Comparisons JSONL
```jsonl
{"comparison_id":"LC001","finding_id":"F001","context_match":"partial: cell type differs"}
not json
{"comparison_id":"LC002","finding_id":"F002","context_match":"matched"}
```

### Pathways JSONL
```jsonl
{"pathway":"x","finding_ids":["F001"]}
```
"""


def test_extract_block_parses_rows_and_counts_invalid():
    block = reports.extract_jsonl_block(REPORT, "Literature Comparisons JSONL")

    assert block is not None
    assert [row["comparison_id"] for row in block.rows] == ["LC001", "LC002"]
    assert block.n_invalid == 1


def test_extract_block_stops_at_next_fence():
    block = reports.extract_jsonl_block(REPORT, "Pathways JSONL")

    assert block is not None
    assert block.rows == [{"pathway": "x", "finding_ids": ["F001"]}]


def test_extract_block_missing_heading_returns_none():
    assert reports.extract_jsonl_block(REPORT, "Evidence JSONL") is None


def test_url_host_normalises():
    assert reports.url_host("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1/") == "ncbi.nlm.nih.gov"
    assert reports.url_host("http://DOI.org/10.1/x") == "doi.org"
    assert reports.url_host("not a url") == ""
