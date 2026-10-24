from pathlib import Path

import pytest

from audit.lib import corpus

FIXTURES = Path(__file__).parent / "fixtures"
MINI = FIXTURES / "mini_corpus"


def test_ref_join_is_per_target():
    refs = corpus.load_references(MINI)
    findings = {(f.target_gene, f.finding_id): f for f in corpus.load_findings(MINI)}

    arx_refs = corpus.refs_for_finding(findings[("Arx", "F001")], refs)
    psmb4_refs = corpus.refs_for_finding(findings[("Psmb4", "F001")], refs)

    assert [r.url for r in arx_refs] == [
        "https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=O35085",
        "https://pubmed.ncbi.nlm.nih.gov/11111111/",
    ]
    assert [r.url for r in psmb4_refs] == ["https://pubmed.ncbi.nlm.nih.gov/22222222/"]


def test_ref_ids_pipe_split():
    findings = {(f.target_gene, f.finding_id): f for f in corpus.load_findings(MINI)}

    assert findings[("Arx", "F001")].ref_ids == ("R001", "R003")
    assert findings[("Arx", "F001")].evidence_ids == ("E002", "E003")
    assert findings[("Psmb4", "F002")].ref_ids == ()


def test_lfs_pointer_raises():
    with pytest.raises(corpus.LfsPointerError):
        list(corpus.read_csv_checked(FIXTURES / "lfs_pointer.csv"))


def test_controls_excluded_by_default():
    default = {f.target_gene for f in corpus.load_findings(MINI)}
    with_controls = {f.target_gene for f in corpus.load_findings(MINI, include_controls=True)}

    assert "Safe_target_17" not in default
    assert "Safe_target_17" in with_controls
    assert corpus.is_control("Non_target") and not corpus.is_control("Arx")


def test_missing_ref_raises_keyerror():
    refs = corpus.load_references(MINI)
    finding = corpus.Finding(
        target_gene="Arx", finding_id="F009", finding_type="other", direction="",
        confidence="low", literature_status="", summary="", why_it_matters="",
        genes=(), n_genes=0, comparators=(), cell_types=(), n_cell_types=0,
        evidence_ids=(), ref_ids=("R404",), main_caveats="",
    )
    with pytest.raises(KeyError):
        corpus.refs_for_finding(finding, refs)
