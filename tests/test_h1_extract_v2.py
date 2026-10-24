"""H1 extraction grammar v2 (retry), defined by example. The v1 cases must still hold; the
v2 cases at the end use verbatim sample-1 or ledger phrasings, never sample-2 fields."""

import pytest

from audit.lib.h1_extract_v2 import Vocabulary, extract

CELL_TYPES = (
    "001 L5-6 IT Glut", "005 L4-5 IT CTX Glut", "008 L2-3 IT ENT PPP RSP Glut",
    "017 CA3 CA2-FC DG Glut", "052 Pvalb Gaba", "053 Sst Gaba", "066 CNU-HYa HY GABA",
    "151 TH Prkcd Grin2c Glut", "155 MB Glut", "191 MB P MY GABA", "308 CB GABA",
    "059 CNU-LGE LSX GABA", "046 CTX-CGE GABA", "009 L2-3 IT PIR AON ENT Glut",
)
GENES = frozenset({
    "Sst", "Pvalb", "Prkcd", "Grin2c", "Prkci", "Sik3", "Creb3l2", "Mbd2", "Supt16", "Gale",
    "Auh", "Ahdc1", "Rara", "Vegfa", "Tiparp", "Atp5b", "Rusc2", "Ggps1", "Tsc1", "Tsc2",
    "Opa1", "Asns", "Mars1", "Chac1", "Ddit3", "mt-Co2", "Erf", "Spred1", "Kif1a", "Stxbp1",
    "Kremen1", "Nbea", "Syp", "Gria2",
})
VOCAB = Vocabulary(cell_types=CELL_TYPES, genes=GENES)


def _in_scope(assertions):
    return [a for a in assertions if a.status == "extracted"]


def _find(assertions, quantity):
    return [a for a in _in_scope(assertions) if a.quantity == quantity]


def test_gene_names_inside_cell_labels_are_not_bound():
    # Codex review round 1, finding 1 (Grm6/E004).
    text = ("Mbd2 in 066 CNU-HYa HY GABA: score 4.4957, logFC 0.6280, p 6.79e-6, FDR 0.1187; "
            "Prkci in 053 Sst Gaba: score 4.1005, logFC 0.8685, p 4.09e-5, FDR 0.3567; "
            "Sik3 in 053 Sst Gaba: score 4.0884, logFC 0.9100, p 4.34e-5, FDR 0.3567; "
            "Creb3l2 in 053 Sst Gaba: score 3.7511, logFC 1.1235, p 1.76e-4, FDR 0.9643.")
    out = extract(text, target="Grm6", row_cell_type=None, vocab=VOCAB)

    assert not [a for a in out if a.gene in {"Sst", "Pvalb", "Prkcd", "Grin2c"}]
    prkci = {a.quantity: (a.value_text, a.cell_type) for a in _in_scope(out)
             if a.gene == "Prkci"}
    assert prkci == {"score": ("4.1005", "053 Sst Gaba"), "logfc": ("0.8685", "053 Sst Gaba"),
                     "pval": ("4.09e-5", "053 Sst Gaba"), "padj": ("0.3567", "053 Sst Gaba")}
    assert {a.cell_type for a in _in_scope(out) if a.gene == "Mbd2"} == {"066 CNU-HYa HY GABA"}
    assert len(_in_scope(out)) == 16


def test_row_cell_type_and_counts():
    text = ("145 perturbed cells versus 20,353 controls; Auh score -5.116, logFC -0.571, "
            "p=3.12e-7, FDR=0.00544; rank 1 of 17,443 by p value.")
    out = extract(text, target="Auh", row_cell_type="155 MB Glut", vocab=VOCAB)

    by_q = {a.quantity: a for a in _in_scope(out)}
    assert by_q["n_pert"].value_text == "145" and by_q["n_ctrl"].value_text == "20,353"
    assert by_q["n_pert"].cell_type == "155 MB Glut"
    assert (by_q["logfc"].gene, by_q["logfc"].value_text) == ("Auh", "-0.571")
    assert by_q["padj"].value_text == "0.00544" and by_q["padj"].relation == "="
    assert (by_q["n_rows"].value_text, by_q["n_rows"].scope) == ("17,443", "cell")


def test_in_sentence_cell_label_overrides_row_and_recurrence_is_out_of_scope():
    text = ("Ahdc1 RNA was measured in all 22 Ahdc1 cell-type tests; 0/22 had Ahdc1 FDR<0.05. "
            "In 151 TH Prkcd Grin2c Glut, Ahdc1 logFC was +0.404, nominal p=2.47e-04, FDR=0.193.")
    out = extract(text, target="Ahdc1", row_cell_type=None, vocab=VOCAB)

    assert {(a.quantity, a.value_text) for a in _in_scope(out)} == {
        ("logfc", "+0.404"), ("pval", "2.47e-04"), ("padj", "0.193")}
    assert all(a.cell_type == "151 TH Prkcd Grin2c Glut" and a.gene == "Ahdc1"
               for a in _in_scope(out))
    assert any(a.status == "out_of_scope" and a.reason == "recurrence" for a in out)


def test_clause_level_cells_counts_and_minima():
    text = ("No FDR <0.05 genes in 151 TH Prkcd Grin2c Glut despite 149 Rara cells, "
            "min FDR=0.602440; 155 MB Glut, 136 cells, min FDR=0.225020.")
    out = extract(text, target="Rara", row_cell_type=None, vocab=VOCAB)

    pert = {(a.cell_type, a.value_text) for a in _find(out, "n_pert")}
    assert pert == {("151 TH Prkcd Grin2c Glut", "149"), ("155 MB Glut", "136")}
    mins = {(a.cell_type, a.value_text) for a in _find(out, "min_padj")}
    assert mins == {("151 TH Prkcd Grin2c Glut", "0.602440"), ("155 MB Glut", "0.225020")}
    zero = _find(out, "n_sig")
    assert [(a.value_text, a.threshold_text, a.cell_type) for a in zero] == [
        ("0", "0.05", "151 TH Prkcd Grin2c Glut")]


def test_target_wide_counts_without_cell_context():
    text = ("371818 Wilcoxon rows across 22 cell types; 0 genes at FDR < 0.05; minimum nominal "
            "p = 1.13e-05; minimum FDR = 0.193; 112 rows had p < 0.001.")
    out = extract(text, target="Erf", row_cell_type=None, vocab=VOCAB)

    got = {(a.quantity, a.value_text, a.scope) for a in _in_scope(out)}
    assert ("n_rows", "371818", "target") in got
    assert ("min_pval", "1.13e-05", "target") in got
    assert ("min_padj", "0.193", "target") in got
    sig = {(a.value_text, a.threshold_quantity, a.threshold_text, a.unit)
           for a in _find(out, "n_sig")}
    assert sig == {("0", "padj", "0.05", "genes"), ("112", "pval", "0.001", "rows")}


def test_k_of_n_genes_gives_count_and_total():
    text = ("1/17443 genes in the 155 MB Glut contrast had FDR<0.05 and that gene was Rusc2; "
            "the top non-target by FDR was Atp5b, logFC 0.3246, p=7.86e-6, FDR=0.0686.")
    out = extract(text, target="Fosl2", row_cell_type=None, vocab=VOCAB)

    assert [(a.value_text, a.cell_type) for a in _find(out, "n_sig")] == [("1", "155 MB Glut")]
    assert [(a.value_text, a.scope) for a in _find(out, "n_rows")] == [("17443", "cell")]
    assert {(a.quantity, a.value_text) for a in _in_scope(out) if a.gene == "Atp5b"} == {
        ("logfc", "0.3246"), ("pval", "7.86e-6"), ("padj", "0.0686")}


def test_correlations_are_out_of_scope_and_not_bound():
    text = ("In 155 MB Glut, among 2,040 non-self perturbations the top positive neighbor was "
            "Stxbp1 r=0.121 and the top negative neighbor was Kremen1 r=-0.065.")
    out = extract(text, target="Kif1a", row_cell_type=None, vocab=VOCAB)

    assert _in_scope(out) == []
    assert sum(a.reason == "correlation" for a in out) == 2


def test_statistics_about_another_perturbation_are_out_of_scope():
    text = "In 308 CB GABA, Tsc1 perturbation gave Gria2 logFC -0.21, FDR=0.4."
    out = extract(text, target="Tsc2", row_cell_type=None, vocab=VOCAB)

    assert _in_scope(out) == []
    assert {a.reason for a in out} == {"other_perturbation"}


def test_medians_ranges_and_approximations_are_out_of_scope():
    text = ("Across the 22 Syngap1 cell classes, n_perturbed ranged from 27 to 183 with median "
            "64.5; Syp median logFC -0.294; approximately 300 cells.")
    out = extract(text, target="Syngap1", row_cell_type="155 MB Glut", vocab=VOCAB)

    assert _in_scope(out) == []
    assert {a.reason for a in out} >= {"range", "summary_statistic", "approximation"}


def test_unresolved_when_no_gene_or_cell():
    out = extract("logFC -0.511 and FDR 6.63e-4 overall.", target="Opa1",
                  row_cell_type=None, vocab=VOCAB)

    assert {a.status for a in out} == {"unresolved_context"}


def test_vs_abbreviation_does_not_split_sentences():
    text = ("37 perturbed cells vs. 7,679 controls; Nbea logFC -0.00277, nominal P=0.924, "
            "FDR=1.0; Syp logFC -0.294, nominal P=0.00447, FDR=1.0.")
    out = extract(text, target="Nbea", row_cell_type="005 L4-5 IT CTX Glut", vocab=VOCAB)

    assert {(a.quantity, a.value_text) for a in _in_scope(out) if a.gene is None} == {
        ("n_pert", "37"), ("n_ctrl", "7,679")}
    assert {(a.quantity, a.value_text) for a in _in_scope(out) if a.gene == "Syp"} == {
        ("logfc", "-0.294"), ("pval", "0.00447"), ("padj", "1.0")}


def test_unicode_minus_and_times_ten_notation():
    text = "In 308 CB GABA, Tsc2 logFC −0.42, p = 3.1 × 10^-5."
    out = extract(text, target="Tsc2", row_cell_type=None, vocab=VOCAB)

    assert {(a.quantity, a.value_text) for a in _in_scope(out)} == {
        ("logfc", "-0.42"), ("pval", "3.1e-5")}


# Codex review round 2 regressions (verbatim ledger rows).

AP3B1_E004 = (
    "Only 6 Ap3b1 rows had FDR<1.0: Fam169a score -4.215 logFC -1.006 FDR 0.428 in 005 L4-5 IT "
    "CTX Glut; Epha4 score 4.198 logFC 0.727 FDR 0.458 in 022 L5 ET CTX Glut; Abhd2 score -4.175 "
    "logFC -1.097 FDR 0.512 in 009 L2-3 IT PIR AON ENT Glut; Cpsf7, Nrip3 and Rims2 in 022 L5 ET "
    "CTX Glut had FDR 0.865-0.893; 67 rows had p<0.001 and no gene recurred in at least two cell "
    "types at that cutoff.")
VOCAB2 = Vocabulary(
    cell_types=CELL_TYPES + ("022 L5 ET CTX Glut",),
    genes=GENES | {"Fam169a", "Epha4", "Abhd2", "Cpsf7", "Nrip3", "Rims2", "Ap3b1", "Bcas3",
                   "Dtx3", "Pde2a", "Prr36", "Tppp", "Brd9", "Clec16a", "Sod2", "Lrrtm1"})


def test_clause_label_beats_label_from_earlier_clause():
    out = extract(AP3B1_E004, target="Ap3b1", row_cell_type=None, vocab=VOCAB2)

    cells = {a.gene: a.cell_type for a in _in_scope(out) if a.gene}
    assert cells == {"Fam169a": "005 L4-5 IT CTX Glut", "Epha4": "022 L5 ET CTX Glut",
                     "Abhd2": "009 L2-3 IT PIR AON ENT Glut"}
    counts = {(a.value_text, a.threshold_quantity, a.scope) for a in _find(out, "n_sig")}
    assert counts == {("6", "padj", "target"), ("67", "pval", "target")}
    assert not [a for a in _in_scope(out) if a.value_text in {"0.865", "0.893", "-0.893"}]


def test_zero_count_with_threshold_before_unit_is_a_count():
    text = ("151 TH Prkcd Grin2c Glut: 135 perturbed versus 23,679 controls, 0 FDR<0.05 genes, "
            "Bcas3 self logFC -0.317 FDR 1.0; 155 MB Glut: 109 perturbed versus 20,353 controls, "
            "0 FDR<0.05 genes, Bcas3 self logFC -0.475 FDR 1.0.")
    out = extract(text, target="Bcas3", row_cell_type=None, vocab=VOCAB2)

    assert {(a.value_text, a.cell_type) for a in _find(out, "n_sig")} == {
        ("0", "151 TH Prkcd Grin2c Glut"), ("0", "155 MB Glut")}
    assert {(a.value_text, a.cell_type) for a in _find(out, "n_pert")} == {
        ("135", "151 TH Prkcd Grin2c Glut"), ("109", "155 MB Glut")}
    assert {a.value_text for a in _find(out, "n_ctrl")} == {"23,679", "20,353"}
    assert not [a for a in out if a.relation == "<" and a.gene == "Bcas3"]
    assert {(a.quantity, a.relation, a.value_text) for a in _in_scope(out)
            if a.gene == "Bcas3"} == {("logfc", "=", "-0.317"), ("padj", "=", "1.0"),
                                      ("logfc", "=", "-0.475")}


def test_numeric_ranges_never_become_scalars():
    text = ("82 perturbed cells versus 8644 controls; Dtx3 logFC 0.314 score 4.670 p=3.01e-06 "
            "FDR=0.0512; Pde2a logFC 0.434 score 4.306 p=1.66e-05 FDR=0.141; Prr36/Tppp/Brd9 "
            "FDR 0.895-0.917.")
    out = extract(text, target="Fezf1", row_cell_type="022 L5 ET CTX Glut", vocab=VOCAB2)

    assert not [a for a in _in_scope(out) if a.gene in {"Prr36", "Tppp", "Brd9"}]
    assert any(a.reason == "range" for a in out)
    assert {a.value_text for a in _find(out, "n_pert")} == {"82"}

    bare = extract("23-191 perturbed cells per class.", target="Fezf1",
                   row_cell_type="022 L5 ET CTX Glut", vocab=VOCAB2)
    assert _in_scope(bare) == []
    assert [a.reason for a in bare] == ["range"]


def test_paired_counts_naming_the_target_keep_the_control_count():
    text = ("164 Clec16a cells versus 23,679 controls; Clec16a logFC -0.371, p=0.00178, FDR=1.0; "
            "Sod2 logFC 0.321, p=3.42e-06, FDR=0.0589.")
    out = extract(text, target="Clec16a", row_cell_type="151 TH Prkcd Grin2c Glut", vocab=VOCAB2)

    assert {a.value_text for a in _find(out, "n_pert")} == {"164"}
    assert {a.value_text for a in _find(out, "n_ctrl")} == {"23,679"}


def test_standalone_control_count():
    out = extract("Matched against 8,277 controls in 308 CB GABA.", target="Tsc2",
                  row_cell_type=None, vocab=VOCAB)

    assert [(a.value_text, a.cell_type) for a in _find(out, "n_ctrl")] == [
        ("8,277", "308 CB GABA")]


def test_self_inclusion_is_recorded_for_counts():
    out = extract("12 non-target genes had FDR<0.05 and 37 genes at FDR<0.1 in 155 MB Glut.",
                  target="Opa1", row_cell_type=None, vocab=VOCAB)

    assert {(a.value_text, a.self_inclusion) for a in _find(out, "n_sig")} == {
        ("12", "exclude"), ("37", "unstated")}


def test_inequalities_bind_only_to_an_adjacent_gene():
    out = extract("In 155 MB Glut, Syp logFC -0.3; overall FDR<0.05 was not reached by Ahdc1 "
                  "but Auh FDR<0.05.", target="Auh", row_cell_type=None, vocab=VOCAB)

    ineq = [(a.gene, a.status) for a in out if a.relation == "<"]
    assert ("Auh", "extracted") in ineq
    assert all(status != "extracted" for gene, status in ineq if gene != "Auh")


# Codex review round 3 regressions (verbatim ledger rows).

VOCAB3 = Vocabulary(
    cell_types=CELL_TYPES + ("022 L5 ET CTX Glut",),
    genes=VOCAB2.genes | {"Dnajc5", "Fndc3a", "Map4", "Ap3b2", "Brms1", "Pik3cb", "Ndufv1",
                          "Ndufv2", "Ndufc2"})


def test_exclusion_propagates_to_the_denominator():
    text = ("0/388023 non-target rows had FDR<0.05. The smallest non-target FDR was Fndc3a in 008 "
            "L2-3 IT ENT PPP RSP Glut, FDR=0.076423, p=4.582792e-06; the next was Map4 in 066 "
            "CNU-HYa HY GABA, FDR=0.239432, p=1.399039e-05.")
    out = extract(text, target="Dnajc5", row_cell_type=None, vocab=VOCAB3)

    counts = {(a.quantity, a.value_text, a.self_inclusion, a.scope) for a in _in_scope(out)
              if a.quantity in {"n_sig", "n_rows"}}
    assert counts == {("n_sig", "0", "exclude", "target"),
                      ("n_rows", "388023", "exclude", "target")}


def test_target_specific_exclusion_and_among_n_tested():
    text = ("150 perturbed cells versus 20353 controls; Ap3b2 logFC -0.670, Wilcoxon score -5.797, "
            "p=6.74e-09, FDR=1.18e-04; 0 non-Ap3b2 genes at FDR<0.05 among 17442 tested, with top "
            "nominal non-targets Brms1 p=1.91e-04 FDR=1.0, Pik3cb p=3.55e-04 FDR=1.0, and Sik3 "
            "p=3.98e-04 FDR=1.0.")
    out = extract(text, target="Ap3b2", row_cell_type="155 MB Glut", vocab=VOCAB3)

    counts = {(a.quantity, a.value_text, a.self_inclusion) for a in _in_scope(out)
              if a.quantity in {"n_sig", "n_rows"}}
    assert counts == {("n_sig", "0", "exclude"), ("n_rows", "17442", "exclude")}


def test_subset_counts_are_out_of_scope_not_bound_to_a_later_label():
    text = ("Across 41 selected NDUF/COX/UQCR/SDH genes measured in the 22 Ndufv1 signatures, 39 "
            "rows were nominal p<0.05 and none were FDR<0.05 except Ndufv1 in 191 MB P MY GABA; "
            "in 191 MB P MY GABA, Ndufv2 logFC -0.244, p=0.0293, FDR=1.0 and Ndufc2 logFC "
            "-0.275, p=0.0499, FDR=1.0.")
    out = extract(text, target="Ndufv1", row_cell_type=None, vocab=VOCAB3)

    assert not _find(out, "n_sig")
    assert any(a.reason == "subset_scope" for a in out)
    assert {(a.gene, a.cell_type) for a in _in_scope(out)} == {
        ("Ndufv2", "191 MB P MY GABA"), ("Ndufc2", "191 MB P MY GABA")}


def test_qualifier_of_an_earlier_count_does_not_leak_to_the_next():
    out = extract("12 non-target genes had FDR<0.05 and 37 genes at FDR<0.1 in 155 MB Glut; "
                  "among non-target genes, 5 rows had p<0.001.", target="Opa1",
                  row_cell_type=None, vocab=VOCAB)

    assert {(a.value_text, a.self_inclusion) for a in _find(out, "n_sig")} == {
        ("12", "exclude"), ("37", "unstated"), ("5", "exclude")}


def test_subset_and_exclusion_rules_also_cover_totals_and_minima():
    out = extract("Across the 21 prespecified markers, minimum p = 0.0444; 371,818 non-target rows "
                  "were tested.", target="Atl1", row_cell_type=None, vocab=VOCAB)

    assert [a.reason for a in out if a.quantity == "min_pval"] == ["subset_scope"]
    assert [(a.value_text, a.self_inclusion) for a in _find(out, "n_rows")] == [
        ("371,818", "exclude")]


@pytest.mark.parametrize("text", ["", "No statistics were computed for this target."])
def test_texts_without_numbers_yield_nothing(text):
    assert extract(text, target="Auh", row_cell_type=None, vocab=VOCAB) == []


# --- v2 (retry) cases ---------------------------------------------------------------------

V2_CELLS = ("151 TH Prkcd Grin2c Glut", "155 MB Glut", "191 MB P MY GABA", "308 CB GABA",
            "017 CA3 CA2-FC DG Glut", "052 Pvalb Gaba", "046 CTX-CGE GABA",
            "009 L2-3 IT PIR AON ENT Glut", "145 MH-LH TH Glut", "054 CNU-MGE GABA",
            "007 L2-3 IT CTX Glut")
V2 = Vocabulary(cell_types=V2_CELLS, genes=frozenset({
    "Aimp1", "Ap2m1", "Ap2s1", "Tfrc", "Mical2", "Atg5", "Ccnk", "Arih1", "Cul3", "Mafb",
    "Ccdc88a", "Ror1", "Bin1", "Me1", "Hspd1", "Lrch1", "Prdm10", "Cadm3", "Ptov1", "Tbr1",
    "Pnma8b", "Ehbp1", "Lztfl1", "Cyld", "Ncam1", "Nfic", "Bambi", "Nfib", "Cdk8", "Med13",
    "Prkcd", "Grin2b", "Rpgrip1l", "B9d1", "Bend6", "Ahi1", "Spast", "Nbas", "Shank2",
    "Creb3", "Lman2l", "Tlr7", "Il1rapl1", "Mcf2l", "Rhoa", "Pax7", "Ghr", "Klf13"}))


def _v2(text, target, cell=None):
    return {(a.quantity, a.value_text, a.cell_type, a.gene, a.unit, a.self_inclusion)
            for a in extract(text, target, cell, V2) if a.status == "extracted"}


def test_v2_row_totals_with_descriptive_words():
    got = _v2("371,818 Aimp1-target DE rows across 22 cell classes; 34-199 perturbed cells per "
              "class, median 66.5.", "Aimp1")
    assert ("n_rows", "371,818", None, None, "rows", "unstated") in got


def test_v2_sentence_led_by_another_perturbation_is_out_of_scope():
    text = ("Ap2s1 perturbation used 310 perturbed cells versus 23679 controls; Ap2s1 logFC "
            "-0.536 FDR 6.33e-05; 1152 genes were FDR<0.05. Ap2s1 Tfrc logFC 0.984 FDR 3.06e-24; "
            "Mical2 logFC -1.227 FDR 2.95e-52.")
    assert _v2(text, "Ap2m1", "151 TH Prkcd Grin2c Glut") == set()


def test_v2_count_words_and_singular_units():
    got = _v2("39 perturbed cells versus 8,277 controls. Ccnk logFC +1.050, p=1.16e-5, FDR=0.197; "
              "zero genes reached FDR<0.10.", "Atg5", "308 CB GABA")
    assert ("n_sig", "0", "308 CB GABA", None, "genes", "unstated") in got
    got = _v2("Nfic subset; 1 row with FDR<0.1.", "Nfic")
    assert ("n_sig", "1", None, None, "rows", "unstated") in got


def test_v2_gene_that_had_counts_is_another_perturbation():
    text = ("Cul3 had 1 FDR<0.05 gene in this cell type; the Cul3 self-transcript had logFC "
            "-0.408, p=0.00133, FDR 0.656.")
    assert _v2(text, "Arih1", "151 TH Prkcd Grin2c Glut") == set()


def test_v2_hyphenated_cell_counts_and_column_spellings():
    got = _v2("88 Mafb-perturbed cells versus 13710 controls; Ccdc88a logFC=-0.503, FDR=0.0450.",
              "Mafb", "052 Pvalb Gaba")
    assert ("n_pert", "88", "052 Pvalb Gaba", None, None, None) in got
    got = _v2("65 Ror1-perturbed cells; 0 genes with pvals_adj < 0.05; top rows: Bin1 logFC "
              "-0.413 p=8.9e-05 pvals_adj 0.458853.", "Ror1", "017 CA3 CA2-FC DG Glut")
    assert {("n_pert", "65"), ("n_sig", "0"), ("padj", "0.458853")} <= {g[:2] for g in got}


def test_v2_target_transcript_rows_bind_the_target_and_n_equals_is_perturbed_cells():
    text = ("Hspd1 target transcript was measured in 22 cell types. Nominal negative rows: 151 TH "
            "Prkcd Grin2c Glut score -3.393, logFC -0.564, p=0.000691, rank 3/17,259, n=137.")
    got = _v2(text, "Hspd1")
    assert ("logfc", "-0.564", "151 TH Prkcd Grin2c Glut", "Hspd1", None, None) in got
    assert ("n_pert", "137", "151 TH Prkcd Grin2c Glut", None, None, None) in got
    assert ("n_rows", "17,259", "151 TH Prkcd Grin2c Glut", None, "genes", None) in got


def test_v2_bare_values_take_the_list_lead_statistic():
    got = _v2("Cadm3 logFC -1.227 FDR 1.12e-20, Ptov1 -1.668 FDR 5.57e-20.", "Prdm10",
              "191 MB P MY GABA")
    assert ("logfc", "-1.668", "191 MB P MY GABA", "Ptov1", None, None) in got
    got = _v2("Top rows were Nbas score -3.740 logFC -0.448 p=1.84e-04, Creb3 +3.436 logFC "
              "+0.588 p=5.90e-04.", "Lman2l", "155 MB Glut")
    assert ("score", "+3.436", "155 MB Glut", "Creb3", None, None) in got


def test_v2_elided_and_count_equals_forms():
    got = _v2("141 perturbed cells versus 23,679 controls; 9 genes had P<0.001 and 61 had P<0.01.",
              "Spast", "151 TH Prkcd Grin2c Glut")
    assert ("n_sig", "61", "151 TH Prkcd Grin2c Glut", None, "genes", "unstated") in got
    got = _v2("Across all Lztfl1 rows, FDR<0.05 count=0 and FDR<0.10 count=1.", "Lztfl1")
    assert {("n_sig", "0"), ("n_sig", "1")} <= {g[:2] for g in got}


def test_v2_restricted_and_distributive_statements_are_out_of_scope():
    assert not [g for g in _v2("19 Tlr7 self-transcript rows; pvals_adj=1.000 in all 19 rows.",
                               "Tlr7") if g[0] == "n_rows"]
    got = _v2("88 rows covering Mcf2l, Rhoa, Rock1, and Rock2 across 22 cell types; Rhoa had "
              "minimum nominal p=0.176.", "Il1rapl1")
    assert not [g for g in got if g[0] == "n_rows"]
    # "Rhoa had minimum": the gene is not directly before "minimum" (section 3), so unbound.
    assert ("min_pval", "0.176", None, None, None, None) in got


def test_v2_second_smallest_is_not_a_minimum():
    got = _v2("1 row had FDR<0.05, 1 row had FDR<0.20, and the second-smallest FDR was 0.204478.",
              "Pax7")
    assert not [g for g in got if g[0].startswith("min_")]


def test_v2_thresholds_and_counts_are_never_row_totals():
    got = _v2("The two Nfic FDR < 0.05 rows were Bambi in 151 TH Prkcd Grin2c Glut.", "Nfib")
    assert not [g for g in got if g[0] == "n_rows"]
