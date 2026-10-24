# H1 annotation, sample 1: agreement audit

Both annotators produced identical annotations for each field below; these 20 fields
were drawn at random among such fields (`agreement_audit_sample`, seed 20261027). Check each
against section 3 (`H1_section3_rev10.md`): mark every row `✓` or `✗` (with the correction),
and add any in-scope assertion both missed under **Missed by both**. A single error in this
sample triggers the review of all its remaining agreed fields (decision DC-33).

Türkçe özet: Bu metinlerde iki notlayıcı tamamen aynı sonucu verdi. Her satırı ✓ veya ✗ ile
işaretleyin, ikisinin de atladığı ölçümleri ekleyin. Tek bir hata bile bulunursa o örneklemin
anlaşılan tüm metinleri gözden geçirilir.

## 1. Alx1 / E001

Row cell_type field: `empty`

Raw statistics text:

> Alx1 had 321,156 Wilcoxon rows across 19 of 23 cell groups; n_pert_matched ranged from 22 to 86 and matched non-target controls ranged from 5,622 to 23,679.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 2. Arsb / E001

Row cell_type field: `empty`

Raw statistics text:

> Arsb was measured in 23/23 Arsb-perturbed cell types; Arsb logFC was negative in 23/23; 18/23 had nominal p<0.05, 9/23 had p<0.001, and 5/23 had pvals_adj<0.05; median target logFC=-0.866.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 3. Atg5 / E005

Row cell_type field: `308 CB GABA`

Raw statistics text:

> 39 perturbed cells versus 8,277 controls. Ccnk logFC +1.050, p=1.16e-5, FDR=0.197; Atg5 logFC -0.886, p=0.0747, FDR=1.0; zero genes reached FDR<0.10.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 39 | 308 CB GABA | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 8,277 | 308 CB GABA | — | cell | — | — | — |  |
| 3 | logfc | = | +1.050 | 308 CB GABA | Ccnk | gene | — | — | — |  |
| 4 | pval | = | 1.16e-5 | 308 CB GABA | Ccnk | gene | — | — | — |  |
| 5 | padj | = | 0.197 | 308 CB GABA | Ccnk | gene | — | — | — |  |
| 6 | logfc | = | -0.886 | 308 CB GABA | Atg5 | gene | — | — | — |  |
| 7 | pval | = | 0.0747 | 308 CB GABA | Atg5 | gene | — | — | — |  |
| 8 | padj | = | 1.0 | 308 CB GABA | Atg5 | gene | — | — | — |  |
| 9 | n_sig | = | 0 | 308 CB GABA | — | cell | genes | unstated | padj < 0.10 |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 4. Cep112 / E001

Row cell_type field: `21 Cep112-profiled neuronal classes`

Raw statistics text:

> Target row present in 21/21 Cep112 signatures; n_pert_matched 21-106; n_ctrl_matched 4807-23679; Cep112 self logFC range -0.706 to +0.484; all nominal p>=0.115; all FDR=1.0.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 5. Chrne / E006

Row cell_type field: `empty`

Raw statistics text:

> Within 23 cell types, Chrne signatures were correlated with 448-2046 perturbations over 16228-17443 genes; maximum same-cell positive Pearson r=0.187801 with Macf1 in 054 CNU-MGE GABA; maximum negative r=-0.215541 with Manf in 054 CNU-MGE GABA; maximum absolute neighbor r in any cell type=0.215541.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 6. Ddhd1 / E005

Row cell_type field: `308 CB GABA`

Raw statistics text:

> 74 perturbed cells versus 8,277 controls; Ddhd1 logFC -0.481, score -2.707, p=0.00678, FDR=1.0; 0 genes at FDR<0.10; only Epn1 and Paf1 had p<0.001, with FDR=1.0 for both.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 74 | 308 CB GABA | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 8,277 | 308 CB GABA | — | cell | — | — | — |  |
| 3 | logfc | = | -0.481 | 308 CB GABA | Ddhd1 | gene | — | — | — |  |
| 4 | score | = | -2.707 | 308 CB GABA | Ddhd1 | gene | — | — | — |  |
| 5 | pval | = | 0.00678 | 308 CB GABA | Ddhd1 | gene | — | — | — |  |
| 6 | padj | = | 1.0 | 308 CB GABA | Ddhd1 | gene | — | — | — |  |
| 7 | n_sig | = | 0 | 308 CB GABA | — | cell | genes | unstated | padj < 0.10 |  |
| 8 | padj | = | 1.0 | 308 CB GABA | Paf1 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 7. Etfa / E001

Row cell_type field: `empty`

Raw statistics text:

> Etfa rows in 21 cell types; 1,101 total Etfa-perturbed cells and 208,027 matched controls summed across contrasts; n_pert per class 28-127; Etfa logFC was negative in 18/21 classes, median logFC -0.293; all Etfa pvals_adj=1.0.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 8. Figla / E004

Row cell_type field: `217 P MY Pineal Glut`

Raw statistics text:

> 33 Figla cells versus 3,465 controls; Klhl22 logFC 1.0696, score 4.485, nominal p 7.28e-6, pvals_adj 0.122.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 33 | 217 P MY Pineal Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 3,465 | 217 P MY Pineal Glut | — | cell | — | — | — |  |
| 3 | logfc | = | 1.0696 | 217 P MY Pineal Glut | Klhl22 | gene | — | — | — |  |
| 4 | score | = | 4.485 | 217 P MY Pineal Glut | Klhl22 | gene | — | — | — |  |
| 5 | pval | = | 7.28e-6 | 217 P MY Pineal Glut | Klhl22 | gene | — | — | — |  |
| 6 | padj | = | 0.122 | 217 P MY Pineal Glut | Klhl22 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 9. Foxn1 / E003

Row cell_type field: `empty`

Raw statistics text:

> 151 TH Prkcd Grin2c Glut: 140 perturbed cells, top gene Echs1 logFC 0.8406, score 4.0702, nominal p 4.7e-05, FDR 0.8107; 155 MB Glut: 109 perturbed cells, minimum FDR 1.0; 005 L4-5 IT CTX Glut: 74 perturbed cells, minimum FDR 1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 140 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 2 | logfc | = | 0.8406 | 151 TH Prkcd Grin2c Glut | Echs1 | gene | — | — | — |  |
| 3 | score | = | 4.0702 | 151 TH Prkcd Grin2c Glut | Echs1 | gene | — | — | — |  |
| 4 | pval | = | 4.7e-05 | 151 TH Prkcd Grin2c Glut | Echs1 | gene | — | — | — |  |
| 5 | padj | = | 0.8107 | 151 TH Prkcd Grin2c Glut | Echs1 | gene | — | — | — |  |
| 6 | n_pert | = | 109 | 155 MB Glut | — | cell | — | — | — |  |
| 7 | min_padj | = | 1.0 | 155 MB Glut | — | cell | — | — | — |  |
| 8 | n_pert | = | 74 | 005 L4-5 IT CTX Glut | — | cell | — | — | — |  |
| 9 | min_padj | = | 1.0 | 005 L4-5 IT CTX Glut | — | cell | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 10. Fzd9 / E007

Row cell_type field: `empty`

Raw statistics text:

> In 012 MEA LA CA1 DG Glut, there were 83 Fzd9-perturbed cells versus 7030 controls, Fzd9 score 0.014, p=0.989, FDR 1.0, and 0 FDR genes; best row Syf2 FDR 0.6787. In 017 CA3 CA2-FC DG Glut, there were 103 perturbed cells versus 8620 controls, Fzd9 score -0.049, p=0.961, FDR 1.0, and 0 FDR genes; best row Chchd2 FDR 1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 83 | 012 MEA LA CA1 DG Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 7030 | 012 MEA LA CA1 DG Glut | — | cell | — | — | — |  |
| 3 | score | = | 0.014 | 012 MEA LA CA1 DG Glut | Fzd9 | gene | — | — | — |  |
| 4 | pval | = | 0.989 | 012 MEA LA CA1 DG Glut | Fzd9 | gene | — | — | — |  |
| 5 | padj | = | 1.0 | 012 MEA LA CA1 DG Glut | Fzd9 | gene | — | — | — |  |
| 6 | padj | = | 0.6787 | 012 MEA LA CA1 DG Glut | Syf2 | gene | — | — | — |  |
| 7 | n_pert | = | 103 | 017 CA3 CA2-FC DG Glut | — | cell | — | — | — |  |
| 8 | n_ctrl | = | 8620 | 017 CA3 CA2-FC DG Glut | — | cell | — | — | — |  |
| 9 | score | = | -0.049 | 017 CA3 CA2-FC DG Glut | Fzd9 | gene | — | — | — |  |
| 10 | pval | = | 0.961 | 017 CA3 CA2-FC DG Glut | Fzd9 | gene | — | — | — |  |
| 11 | padj | = | 1.0 | 017 CA3 CA2-FC DG Glut | Fzd9 | gene | — | — | — |  |
| 12 | padj | = | 1.0 | 017 CA3 CA2-FC DG Glut | Chchd2 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 11. Gnas / E010

Row cell_type field: `012 MEA LA CA1 DG Glut`

Raw statistics text:

> Pearson correlations computed over the top 100 absolute-score Gnas genes per class; maximum all-target correlation was Foxl2 r=0.5209 in 012 MEA LA CA1 DG Glut; strongest related targets in that class were Gnb5 r=0.4793, Gnal r=0.4183, Creb1 r=0.4073, and Adcy5 r=-0.4262.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 12. Hesx1 / E007

Row cell_type field: `empty`

Raw statistics text:

> All-target score correlations to Hesx1 had maximum absolute r<0.118 in 20/22 strata. The exceptions were 017 CA3 CA2-FC DG Glut, max |r|=0.271, and 308 CB GABA, max |r|=0.345. In 308 CB GABA, top positive neighbors were Ranbp2 r=0.345, Atp6v1e1 r=0.316, B9d1 r=0.311, and Lhx4 r=0.289; top negative neighbors were Gpr68 r=-0.305, Scn9a r=-0.297, and Cckar r=-0.289.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 13. Lrrtm3 / E001

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 153 perturbed cells versus 20353 controls; Lrrtm3 score -4.372723, logFC -0.587722, nominal p=1.22706588e-05, adjusted p=0.214037101.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 153 | 155 MB Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 20353 | 155 MB Glut | — | cell | — | — | — |  |
| 3 | score | = | -4.372723 | 155 MB Glut | Lrrtm3 | gene | — | — | — |  |
| 4 | logfc | = | -0.587722 | 155 MB Glut | Lrrtm3 | gene | — | — | — |  |
| 5 | pval | = | 1.22706588e-05 | 155 MB Glut | Lrrtm3 | gene | — | — | — |  |
| 6 | padj | = | 0.214037101 | 155 MB Glut | Lrrtm3 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 14. Map1b / E006

Row cell_type field: `empty`

Raw statistics text:

> In 151 TH Prkcd Grin2c Glut and 155 MB Glut, both Map1b and Mapt perturbations had exactly one FDR<0.05 row: the targeted transcript itself. Mapt self rows were logFC -0.533, FDR=1.43e-5 in 151 TH Prkcd Grin2c Glut and logFC -0.519, FDR=0.00663 in 155 MB Glut.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 15. Mark3 / E002

Row cell_type field: `145 MH-LH TH Glut`

Raw statistics text:

> Across 355,046 Mark3 rows, only one gene had p_adj<0.05 or p_adj<0.1: Rai1 in 145 MH-LH TH Glut, score -5.304, logFC -1.618, p=1.14e-7, p_adj=0.00190, 39 perturbed cells versus 6,961 controls; the next-best cell-type minimum p_adj values were 0.339 and 0.439.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 355,046 | 145 MH-LH TH Glut | — | cell | rows | unstated | — |  |
| 2 | score | = | -5.304 | 145 MH-LH TH Glut | Rai1 | gene | — | — | — |  |
| 3 | logfc | = | -1.618 | 145 MH-LH TH Glut | Rai1 | gene | — | — | — |  |
| 4 | pval | = | 1.14e-7 | 145 MH-LH TH Glut | Rai1 | gene | — | — | — |  |
| 5 | padj | = | 0.00190 | 145 MH-LH TH Glut | Rai1 | gene | — | — | — |  |
| 6 | n_pert | = | 39 | 145 MH-LH TH Glut | — | cell | — | — | — |  |
| 7 | n_ctrl | = | 6,961 | 145 MH-LH TH Glut | — | cell | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 16. Med13l / E001

Row cell_type field: `empty`

Raw statistics text:

> Med13l transcript was measured in 22 cell-type signatures with n_pert_matched ranging from 31 to 200; 0/22 direct Med13l rows reached FDR<0.05; 3/22 had nominal p<0.05; 13/22 Wilcoxon scores were negative; strongest direct row was 151 TH Prkcd Grin2c Glut with score -3.046, logFC -0.317, p=0.00232, FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | score | = | -3.046 | 151 TH Prkcd Grin2c Glut | Med13l | gene | — | — | — |  |
| 2 | logfc | = | -0.317 | 151 TH Prkcd Grin2c Glut | Med13l | gene | — | — | — |  |
| 3 | pval | = | 0.00232 | 151 TH Prkcd Grin2c Glut | Med13l | gene | — | — | — |  |
| 4 | padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Med13l | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 17. Nr2f6 / E004

Row cell_type field: `empty`

Raw statistics text:

> Across the 22 Nr2f6 cell-class signatures, no up- or down-regulated top-10 gene recurred in more than two classes; the total nominal burden was 294-439 p<0.05 genes per class with every class having zero FDR<0.1 genes.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.1 |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 18. Pura / E008

Row cell_type field: `empty`

Raw statistics text:

> In 151 TH Prkcd Grin2c Glut, Pura-score Pearson correlations were 0.117 versus Purb and 0.013 versus Purg; Purb and Purg produced 0 FDR<0.05 genes with 239 and 146 perturbed cells. In 155 MB Glut, Pura-score Pearson correlations were 0.086 versus Purb and 0.010 versus Purg; Purb and Purg produced 0 FDR<0.05 genes with 225 and 113 perturbed cells. Purb and Purg target transcripts did not pass FDR in these two classes.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 19. Sox11 / E002

Row cell_type field: `empty`

Raw statistics text:

> 388046 Sox11 gene-by-cell-type tests; 0 genes at FDR<0.05; minimum FDR=0.1816; maximum absolute score=4.402; 116 rows at nominal p<0.001 versus 388.0 expected at a uniform 0.001 rate.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 388046 | — | — | target | rows | unstated | — |  |
| 2 | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  |
| 3 | min_padj | = | 0.1816 | — | — | target | — | — | — |  |
| 4 | n_sig | = | 116 | — | — | target | rows | unstated | pval < 0.001 |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 20. Zfhx2 / E006

Row cell_type field: `empty`

Raw statistics text:

> Across 44 same-cell-type Pearson comparisons of Zfhx2 with Zfhx3 or Zfhx4 score vectors, the largest absolute correlation was |r|=0.0847; Zfhx3 perturbation in 151 TH Prkcd Grin2c Glut produced 5 FDR<0.05 genes including Tagln3 FDR=9.78e-8, whereas Zfhx4 perturbation in 110 CNU-HYa HY MM Glut produced 1 FDR<0.05 gene, Sccpdh FDR=0.0492.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

