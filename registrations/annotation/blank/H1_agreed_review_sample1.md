# H1 annotation, sample 1: full review of the remaining agreed fields (DC-33)

The agreement audit of this sample found an error, so every other field where both
annotators produced identical annotations is now reviewed, as fixed in advance (decision
DC-33). 73 fields. Check each against section 3 (`H1_section3_rev10.md`): mark every row
`✓` or `✗` (`✗ → field=value` for a correction), and add any in-scope assertion both missed
under **Missed by both**.

Türkçe özet: Uzlaşma denetiminde bir hata bulunduğu için, bu örneklemde iki notlayıcının tamamen
anlaştığı diğer tüm metinler inceleniyor. Her satırı ✓ veya ✗ ile işaretleyin, ikisinin de
atladığı ölçümleri ekleyin.

## 1. Add3 / E008

Row cell_type field: `empty`

Raw statistics text:

> Among 1,511-2,046 non-Add3 perturbations per Add3-tested cell type, the largest absolute Pearson correlation to the Add3 score vector was 0.1497; in 053 Sst Gaba the best positive neighbor was Cd3g at r=0.0657 and the best negative neighbor was Ikzf3 at r=-0.0451.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 2. Aimp1 / E001

Row cell_type field: `empty`

Raw statistics text:

> 371,818 Aimp1-target DE rows across 22 cell classes; 34-199 perturbed cells per class, median 66.5; 15/22 classes had fewer than 70 Aimp1-perturbed cells.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 3. Alk / E012

Row cell_type field: `empty`

Raw statistics text:

> A scan of 44,133 group-target pairs across the parquet found 0 gene_target entries for Ltk, Alkal1, Alkal2, Ptn, or Mdk; downstream/pathway comparators were present, including Kras in 20 Alk-overlapping cell types, Pik3ca in 21, Pik3r1 in 19, Mapk1 in 21, Ptpn11 in 21, and Sos1 in 21.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 4. Arhgef9 / E009

Row cell_type field: `empty`

Raw statistics text:

> Among all non-Arhgef9 perturbations using the Arhgef9 top-200 non-target genes, strongest positive/negative correlations were 110: Bmpr2 r=0.337 and Il6ra r=-0.295; 151: Tbce r=0.354 and Ngfr r=-0.264; 155: Pou3f4 r=0.295 and Safe_target_46 r=-0.232.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 5. Atp2c1 / E001

Row cell_type field: `empty`

Raw statistics text:

> 371818 Atp2c1 DE rows across 22 cell types; Atp2c1 transcript measured in all 22; Atp2c1 score negative in 21/22; nominal target P<0.05 in 13/22; target FDR<0.05 in 2/22; n_pert_matched range 39-211 and n_ctrl_matched range 3465-23679.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 371818 | — | — | target | rows | unstated | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 6. Atp9a / E008

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> Using the top 200 non-Atp9a genes by absolute Wilcoxon score, the largest positive Pearson correlations across 2045 comparator perturbations were Kif21a r=0.407 and Kctd16 r=0.395; Safe_target_4 was in the top 10 at r=0.354; the most negative was Atp6v0c r=-0.356.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 7. Bcl11a / E002

Row cell_type field: `empty`

Raw statistics text:

> Bcl11a transcript logFC was negative in 17/22 measured cell types; mean logFC -0.188; only 027 NP-CT-L6b-OB Glut reached nominal p=0.00228, logFC -0.390, score -3.05, FDR=1.0, and 008 L2-3 IT ENT PPP RSP Glut reached nominal p=0.0234, logFC -0.218, score -2.27, FDR=1.0; all 22 on-target FDR values were 1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | pval | = | 0.00228 | 027 NP-CT-L6b-OB Glut | Bcl11a | gene | — | — | — |  |
| 2 | logfc | = | -0.390 | 027 NP-CT-L6b-OB Glut | Bcl11a | gene | — | — | — |  |
| 3 | score | = | -3.05 | 027 NP-CT-L6b-OB Glut | Bcl11a | gene | — | — | — |  |
| 4 | padj | = | 1.0 | 027 NP-CT-L6b-OB Glut | Bcl11a | gene | — | — | — |  |
| 5 | pval | = | 0.0234 | 008 L2-3 IT ENT PPP RSP Glut | Bcl11a | gene | — | — | — |  |
| 6 | logfc | = | -0.218 | 008 L2-3 IT ENT PPP RSP Glut | Bcl11a | gene | — | — | — |  |
| 7 | score | = | -2.27 | 008 L2-3 IT ENT PPP RSP Glut | Bcl11a | gene | — | — | — |  |
| 8 | padj | = | 1.0 | 008 L2-3 IT ENT PPP RSP Glut | Bcl11a | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 8. Chrm2 / E003

Row cell_type field: `empty`

Raw statistics text:

> Chrm2 was represented in 22 of 23 dataset cell classes and absent from 215 MB Dopa; n_pert_matched min=23, median=63, max=155; 7/22 assayed classes had fewer than 50 perturbed cells; n_ctrl_matched ranged from 3,465 to 23,679.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 9. Cox6a1 / E001

Row cell_type field: `empty`

Raw statistics text:

> Cox6a1 transcript was measured in 23 perturbation cell types; 23/23 logFC values were negative; median logFC -0.488, range -1.252 to -0.119; nominal p<0.05 in 10/23; FDR<0.10 in 1/23 and FDR<0.05 in 0/23.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 10. Ctnnb1 / E002

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> 171 perturbed cells versus 23679 controls; 383 genes at FDR<0.05, including 283 down and 100 up. Ctnnb1 logFC -0.593 FDR 1.83e-10; Plekhg1 logFC -1.157 FDR 3.55e-25; Gabra4 logFC -0.758 FDR 7.85e-22; Ramp3 logFC -1.367 FDR 3.00e-21; Chgb logFC 0.696 FDR 1.76e-13.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 171 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 23679 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 3 | n_sig | = | 383 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  |
| 4 | logfc | = | -0.593 | 151 TH Prkcd Grin2c Glut | Ctnnb1 | gene | — | — | — |  |
| 5 | padj | = | 1.83e-10 | 151 TH Prkcd Grin2c Glut | Ctnnb1 | gene | — | — | — |  |
| 6 | logfc | = | -1.157 | 151 TH Prkcd Grin2c Glut | Plekhg1 | gene | — | — | — |  |
| 7 | padj | = | 3.55e-25 | 151 TH Prkcd Grin2c Glut | Plekhg1 | gene | — | — | — |  |
| 8 | logfc | = | -0.758 | 151 TH Prkcd Grin2c Glut | Gabra4 | gene | — | — | — |  |
| 9 | padj | = | 7.85e-22 | 151 TH Prkcd Grin2c Glut | Gabra4 | gene | — | — | — |  |
| 10 | logfc | = | -1.367 | 151 TH Prkcd Grin2c Glut | Ramp3 | gene | — | — | — |  |
| 11 | padj | = | 3.00e-21 | 151 TH Prkcd Grin2c Glut | Ramp3 | gene | — | — | — |  |
| 12 | logfc | = | 0.696 | 151 TH Prkcd Grin2c Glut | Chgb | gene | — | — | — |  |
| 13 | padj | = | 1.76e-13 | 151 TH Prkcd Grin2c Glut | Chgb | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 11. Ddhd1 / E002

Row cell_type field: `empty`

Raw statistics text:

> 371,818 gene-level rows across 22 Ddhd1 contrasts; 0 rows at FDR<0.05; 1 row at FDR<0.10, Mcl1 in 046 CTX-CGE GABA with FDR=0.0630.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  |
| 2 | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  |
| 3 | n_sig | = | 1 | 046 CTX-CGE GABA | — | cell | rows | unstated | padj < 0.10 |  |
| 4 | padj | = | 0.0630 | 046 CTX-CGE GABA | Mcl1 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 12. Dnajc5 / E001

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 143 perturbed cells versus 20353 controls; Dnajc5 score -5.324778; logFC -0.627294; p=1.010767e-07; FDR=0.001763; rank 1/17443 by absolute score and p value.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 143 | 155 MB Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 20353 | 155 MB Glut | — | cell | — | — | — |  |
| 3 | score | = | -5.324778 | 155 MB Glut | Dnajc5 | gene | — | — | — |  |
| 4 | logfc | = | -0.627294 | 155 MB Glut | Dnajc5 | gene | — | — | — |  |
| 5 | pval | = | 1.010767e-07 | 155 MB Glut | Dnajc5 | gene | — | — | — |  |
| 6 | padj | = | 0.001763 | 155 MB Glut | Dnajc5 | gene | — | — | — |  |
| 7 | n_rows | = | 17443 | 155 MB Glut | — | cell | genes | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 13. Esrrb / E002

Row cell_type field: `empty`

Raw statistics text:

> 371818 gene-by-cell-type tests for Esrrb; 0 genes with FDR<0.05 in any of 22 cell types; smallest FDR=0.522 for Fech in 217 P MY Pineal Glut.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 371818 | — | — | target | rows | unstated | — |  |
| 2 | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  |
| 3 | min_padj | = | 0.522 | 217 P MY Pineal Glut | — | cell | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 14. Fas / E003

Row cell_type field: `empty`

Raw statistics text:

> 0/371,818 rows with FDR < 0.05; 1/371,818 with FDR < 0.10; global minimum FDR = 0.091179.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  |
| 2 | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  |
| 3 | n_sig | = | 1 | — | — | target | rows | unstated | padj < 0.10 |  |
| 4 | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  |
| 5 | min_padj | = | 0.091179 | — | — | target | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 15. Fcgr4 / E009

Row cell_type field: `empty`

Raw statistics text:

> For Cd14, Csf1r, Fcgr2b, Itgb2, Tlr2, Tlr4, and Trem2 self-transcript rows, all adjusted p values were 1.0; the best nominal self p over these perturbations was 0.4323 for Csf1r.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 16. Fmn1 / E003

Row cell_type field: `empty`

Raw statistics text:

> Top rows by nominal p: Ccdc107 in 007 L2-3 IT CTX Glut score 4.378920 logFC 0.839417 p=0.0000118 FDR=0.199811; Rgs7 in 110 CNU-HYa HY MM Glut score -4.231404 logFC -1.232078 p=0.0000232 FDR=0.398682; Asah1 in 009 L2-3 IT PIR AON ENT Glut p=0.000037 FDR=0.632470; Csnk1a1 in 191 MB P MY GABA p=0.000048 FDR=0.826762; Ranbp6 in 027 NP-CT-L6b-OB Glut p=0.000053 FDR=0.878324.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | score | = | 4.378920 | 007 L2-3 IT CTX Glut | Ccdc107 | gene | — | — | — |  |
| 2 | logfc | = | 0.839417 | 007 L2-3 IT CTX Glut | Ccdc107 | gene | — | — | — |  |
| 3 | pval | = | 0.0000118 | 007 L2-3 IT CTX Glut | Ccdc107 | gene | — | — | — |  |
| 4 | padj | = | 0.199811 | 007 L2-3 IT CTX Glut | Ccdc107 | gene | — | — | — |  |
| 5 | score | = | -4.231404 | 110 CNU-HYa HY MM Glut | Rgs7 | gene | — | — | — |  |
| 6 | logfc | = | -1.232078 | 110 CNU-HYa HY MM Glut | Rgs7 | gene | — | — | — |  |
| 7 | pval | = | 0.0000232 | 110 CNU-HYa HY MM Glut | Rgs7 | gene | — | — | — |  |
| 8 | padj | = | 0.398682 | 110 CNU-HYa HY MM Glut | Rgs7 | gene | — | — | — |  |
| 9 | pval | = | 0.000037 | 009 L2-3 IT PIR AON ENT Glut | Asah1 | gene | — | — | — |  |
| 10 | padj | = | 0.632470 | 009 L2-3 IT PIR AON ENT Glut | Asah1 | gene | — | — | — |  |
| 11 | pval | = | 0.000048 | 191 MB P MY GABA | Csnk1a1 | gene | — | — | — |  |
| 12 | padj | = | 0.826762 | 191 MB P MY GABA | Csnk1a1 | gene | — | — | — |  |
| 13 | pval | = | 0.000053 | 027 NP-CT-L6b-OB Glut | Ranbp6 | gene | — | — | — |  |
| 14 | padj | = | 0.878324 | 027 NP-CT-L6b-OB Glut | Ranbp6 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 17. Fth1 / E003

Row cell_type field: `empty`

Raw statistics text:

> Weakest Fth1 entries were 017 CA3 CA2-FC DG Glut n=73 logFC -0.388 nominal p=0.0447 FDR 1.0, 059 CNU-LGE LSX GABA n=63 logFC -0.558 p=0.0207 FDR 1.0, and 012 MEA LA CA1 DG Glut n=68 logFC -0.415 p=0.0140 FDR 1.0; 217 P MY Pineal Glut had only 33 cells but a large logFC -1.360 and FDR 0.0351.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 73 | 017 CA3 CA2-FC DG Glut | — | cell | — | — | — |  |
| 2 | logfc | = | -0.388 | 017 CA3 CA2-FC DG Glut | Fth1 | gene | — | — | — |  |
| 3 | pval | = | 0.0447 | 017 CA3 CA2-FC DG Glut | Fth1 | gene | — | — | — |  |
| 4 | padj | = | 1.0 | 017 CA3 CA2-FC DG Glut | Fth1 | gene | — | — | — |  |
| 5 | n_pert | = | 63 | 059 CNU-LGE LSX GABA | — | cell | — | — | — |  |
| 6 | logfc | = | -0.558 | 059 CNU-LGE LSX GABA | Fth1 | gene | — | — | — |  |
| 7 | pval | = | 0.0207 | 059 CNU-LGE LSX GABA | Fth1 | gene | — | — | — |  |
| 8 | padj | = | 1.0 | 059 CNU-LGE LSX GABA | Fth1 | gene | — | — | — |  |
| 9 | n_pert | = | 68 | 012 MEA LA CA1 DG Glut | — | cell | — | — | — |  |
| 10 | logfc | = | -0.415 | 012 MEA LA CA1 DG Glut | Fth1 | gene | — | — | — |  |
| 11 | pval | = | 0.0140 | 012 MEA LA CA1 DG Glut | Fth1 | gene | — | — | — |  |
| 12 | padj | = | 1.0 | 012 MEA LA CA1 DG Glut | Fth1 | gene | — | — | — |  |
| 13 | n_pert | = | 33 | 217 P MY Pineal Glut | — | cell | — | — | — |  |
| 14 | logfc | = | -1.360 | 217 P MY Pineal Glut | Fth1 | gene | — | — | — |  |
| 15 | padj | = | 0.0351 | 217 P MY Pineal Glut | Fth1 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 18. Ghr / E004

Row cell_type field: `007 L2-3 IT CTX Glut`

Raw statistics text:

> 23 Ghr-targeted cells versus 7553 controls; Sugp2 score=-4.1372, logFC=-1.0530, p=3.52e-5, FDR=0.588973; Pomgnt1 score=3.8468, logFC=1.5857, p=1.20e-4, FDR=1.0; 40/16753 genes had p<0.01.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 23 | 007 L2-3 IT CTX Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 7553 | 007 L2-3 IT CTX Glut | — | cell | — | — | — |  |
| 3 | score | = | -4.1372 | 007 L2-3 IT CTX Glut | Sugp2 | gene | — | — | — |  |
| 4 | logfc | = | -1.0530 | 007 L2-3 IT CTX Glut | Sugp2 | gene | — | — | — |  |
| 5 | pval | = | 3.52e-5 | 007 L2-3 IT CTX Glut | Sugp2 | gene | — | — | — |  |
| 6 | padj | = | 0.588973 | 007 L2-3 IT CTX Glut | Sugp2 | gene | — | — | — |  |
| 7 | score | = | 3.8468 | 007 L2-3 IT CTX Glut | Pomgnt1 | gene | — | — | — |  |
| 8 | logfc | = | 1.5857 | 007 L2-3 IT CTX Glut | Pomgnt1 | gene | — | — | — |  |
| 9 | pval | = | 1.20e-4 | 007 L2-3 IT CTX Glut | Pomgnt1 | gene | — | — | — |  |
| 10 | padj | = | 1.0 | 007 L2-3 IT CTX Glut | Pomgnt1 | gene | — | — | — |  |
| 11 | n_sig | = | 40 | 007 L2-3 IT CTX Glut | — | cell | genes | unstated | pval < 0.01 |  |
| 12 | n_rows | = | 16753 | 007 L2-3 IT CTX Glut | — | cell | genes | unstated | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 19. Gnal / E005

Row cell_type field: `059 CNU-LGE LSX GABA`

Raw statistics text:

> 40 perturbed cells versus 8,270 controls; 0 FDR<0.05 genes; top row Dhdds logFC 0.981, score 4.261, p 2.03e-5, FDR 0.336.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 40 | 059 CNU-LGE LSX GABA | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 8,270 | 059 CNU-LGE LSX GABA | — | cell | — | — | — |  |
| 3 | n_sig | = | 0 | 059 CNU-LGE LSX GABA | — | cell | genes | unstated | padj < 0.05 |  |
| 4 | logfc | = | 0.981 | 059 CNU-LGE LSX GABA | Dhdds | gene | — | — | — |  |
| 5 | score | = | 4.261 | 059 CNU-LGE LSX GABA | Dhdds | gene | — | — | — |  |
| 6 | pval | = | 2.03e-5 | 059 CNU-LGE LSX GABA | Dhdds | gene | — | — | — |  |
| 7 | padj | = | 0.336 | 059 CNU-LGE LSX GABA | Dhdds | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 20. Gria3 / E006

Row cell_type field: `empty`

Raw statistics text:

> Across 12 AMPAR-complex or AMPAR-adjacent genes measured in all 21 Gria3 cell-type comparisons, 0/252 gene-by-cell rows had FDR < 0.1. Gria1, Gria2, Gria4, Cacng2, Cacng3, Cnih2, Cnih3, Dlg4, Dlgap4, Grip1, Pick1, and Shisa9 all had adjusted p = 1.0 in every Gria3 comparison; the smallest nominal AMPAR-subunit p was Gria2 in 008 L2-3 IT ENT PPP RSP Glut, p = 0.00101, FDR = 1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | pval | = | 0.00101 | 008 L2-3 IT ENT PPP RSP Glut | Gria2 | gene | — | — | — |  |
| 2 | padj | = | 1.0 | 008 L2-3 IT ENT PPP RSP Glut | Gria2 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 21. Guk1 / E003

Row cell_type field: `066 CNU-HYa HY GABA`

Raw statistics text:

> 121 perturbed cells versus 10110 controls; Guk1 logFC -0.774181 score -4.245932 p=0.000022 q=0.309490; Tjp1 logFC 0.627963 score 4.130688 p=0.000036 q=0.309490; Pdzd8 logFC 0.496576 score 3.898388 p=0.000097 q=0.552412.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 121 | 066 CNU-HYa HY GABA | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 10110 | 066 CNU-HYa HY GABA | — | cell | — | — | — |  |
| 3 | logfc | = | -0.774181 | 066 CNU-HYa HY GABA | Guk1 | gene | — | — | — |  |
| 4 | score | = | -4.245932 | 066 CNU-HYa HY GABA | Guk1 | gene | — | — | — |  |
| 5 | pval | = | 0.000022 | 066 CNU-HYa HY GABA | Guk1 | gene | — | — | — |  |
| 6 | padj | = | 0.309490 | 066 CNU-HYa HY GABA | Guk1 | gene | — | — | — |  |
| 7 | logfc | = | 0.627963 | 066 CNU-HYa HY GABA | Tjp1 | gene | — | — | — |  |
| 8 | score | = | 4.130688 | 066 CNU-HYa HY GABA | Tjp1 | gene | — | — | — |  |
| 9 | pval | = | 0.000036 | 066 CNU-HYa HY GABA | Tjp1 | gene | — | — | — |  |
| 10 | padj | = | 0.309490 | 066 CNU-HYa HY GABA | Tjp1 | gene | — | — | — |  |
| 11 | logfc | = | 0.496576 | 066 CNU-HYa HY GABA | Pdzd8 | gene | — | — | — |  |
| 12 | score | = | 3.898388 | 066 CNU-HYa HY GABA | Pdzd8 | gene | — | — | — |  |
| 13 | pval | = | 0.000097 | 066 CNU-HYa HY GABA | Pdzd8 | gene | — | — | — |  |
| 14 | padj | = | 0.552412 | 066 CNU-HYa HY GABA | Pdzd8 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 22. Hspd1 / E002

Row cell_type field: `empty`

Raw statistics text:

> Hspd1 target transcript was measured in 22 cell types. Nominal negative rows: 151 TH Prkcd Grin2c Glut score -3.393, logFC -0.564, p=0.000691, p_adj=1.0, rank 3/17,259, n=137; 145 MH-LH TH Glut score -2.566, logFC -0.899, p=0.0103, n=43; 054 CNU-MGE GABA score -2.512, logFC -0.897, p=0.0120, n=37; 155 MB Glut score -2.468, logFC -0.567, p=0.0136, n=117.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 17,259 | 151 TH Prkcd Grin2c Glut | — | cell | genes | — | — |  |
| 2 | n_pert | = | 137 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 3 | n_pert | = | 43 | 145 MH-LH TH Glut | — | cell | — | — | — |  |
| 4 | n_pert | = | 37 | 054 CNU-MGE GABA | — | cell | — | — | — |  |
| 5 | n_pert | = | 117 | 155 MB Glut | — | cell | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 23. Ifngr2 / E004

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> 201 perturbed cells versus 23679 controls; Ifngr2 logFC -0.574, score -3.695, P=2.20e-4, FDR=1.0; Stat1 logFC -0.888, score -3.437, P=5.88e-4; Nlrc5 logFC -2.372, score -2.874, P=0.00406; B2m logFC -0.846, score -2.304, P=0.0212; all module FDR values were 1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 201 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 23679 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 3 | logfc | = | -0.574 | 151 TH Prkcd Grin2c Glut | Ifngr2 | gene | — | — | — |  |
| 4 | score | = | -3.695 | 151 TH Prkcd Grin2c Glut | Ifngr2 | gene | — | — | — |  |
| 5 | pval | = | 2.20e-4 | 151 TH Prkcd Grin2c Glut | Ifngr2 | gene | — | — | — |  |
| 6 | padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Ifngr2 | gene | — | — | — |  |
| 7 | logfc | = | -0.888 | 151 TH Prkcd Grin2c Glut | Stat1 | gene | — | — | — |  |
| 8 | score | = | -3.437 | 151 TH Prkcd Grin2c Glut | Stat1 | gene | — | — | — |  |
| 9 | pval | = | 5.88e-4 | 151 TH Prkcd Grin2c Glut | Stat1 | gene | — | — | — |  |
| 10 | logfc | = | -2.372 | 151 TH Prkcd Grin2c Glut | Nlrc5 | gene | — | — | — |  |
| 11 | score | = | -2.874 | 151 TH Prkcd Grin2c Glut | Nlrc5 | gene | — | — | — |  |
| 12 | pval | = | 0.00406 | 151 TH Prkcd Grin2c Glut | Nlrc5 | gene | — | — | — |  |
| 13 | logfc | = | -0.846 | 151 TH Prkcd Grin2c Glut | B2m | gene | — | — | — |  |
| 14 | score | = | -2.304 | 151 TH Prkcd Grin2c Glut | B2m | gene | — | — | — |  |
| 15 | pval | = | 0.0212 | 151 TH Prkcd Grin2c Glut | B2m | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 24. Igsf8 / E005

Row cell_type field: `empty`

Raw statistics text:

> At p<0.01, no non-Igsf8 gene recurred in more than 3/23 cell classes; Colgalt1, Fam135b, Ric8b, Pbx1, and Elp1 each appeared in exactly three classes.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 25. Kcnab1 / E008

Row cell_type field: `empty`

Raw statistics text:

> Pearson correlations between Kcnab1 and Kcnab2 scores on the top 100 positive plus top 100 negative Kcnab1 genes were 0.128 in 052 Pvalb Gaba, 0.037 in 066 CNU-HYa HY GABA, 0.053 in 151 TH Prkcd Grin2c Glut, 0.133 in 155 MB Glut, and 0.120 in 191 MB P MY GABA.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 26. Kcnab2 / E011

Row cell_type field: `empty`

Raw statistics text:

> The strongest non-self absolute Pearson correlations to the Kcnab2 score vector in the five FDR-significant cell types were |r|=0.109 in 052 Pvalb Gaba, 0.073 in 066 CNU-HYa HY GABA, 0.083 in 151 TH Prkcd Grin2c Glut, 0.106 in 155 MB Glut, and 0.125 in 191 MB P MY GABA.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 27. Kcnc1 / E009

Row cell_type field: `empty`

Raw statistics text:

> Kcnc1 correlations with Kcnc3 score vectors were r=0.0212 in 191 MB P MY GABA, r=-0.0064 in 151 TH Prkcd Grin2c Glut, and r=0.0710 in 155 MB Glut; Kcnc3 target FDR values in those classes were 1.22e-11, 6.16e-07, and 2.64e-17. Kcnc1 correlations with Kcnc2 were r=0.0388, 0.0831, and 0.0089 in the same classes; Kcnc2 target FDR was 1.0, 4.65e-05, and 2.48e-05, respectively.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 28. Kctd16 / E006

Row cell_type field: `empty`

Raw statistics text:

> Across 20 overlapping Kctd16 cell types, Pearson correlations of same-gene Wilcoxon score vectors were Kctd16 versus Kctd8 range -0.029 to 0.070, Kctd16 versus Gabbr1 range -0.053 to 0.038, and Kctd16 versus Gabbr2 range -0.028 to 0.072. Kctd8 itself had 0 FDR<0.05 genes across 22 tested cell types.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 29. Kiz / E010

Row cell_type field: `empty`

Raw statistics text:

> In the four Kiz cell classes with FDR<0.5 rows, absolute top positive/negative whole-signature correlations were small: 054 Tspoap1 r=0.154 and Safe_target_40 r=-0.122; 053 Mycn r=0.121 and Gp6 r=-0.101; 059 Npy1r r=0.0757 and Calm3 r=-0.0593; 110 Snf8 r=0.121 and Prnp r=-0.108.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 30. Klf13 / E005

Row cell_type field: `053 Sst Gaba`

Raw statistics text:

> 60 perturbed cells versus 5622 controls; 16428 genes tested; 0 genes with FDR < 0.05; 7 genes with p < 0.001. Ctnna2 was the top row with score -4.023, logFC -0.584, p 5.75e-5, FDR 0.9444.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 60 | 053 Sst Gaba | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 5622 | 053 Sst Gaba | — | cell | — | — | — |  |
| 3 | n_rows | = | 16428 | 053 Sst Gaba | — | cell | genes | unstated | — |  |
| 4 | n_sig | = | 0 | 053 Sst Gaba | — | cell | genes | unstated | padj < 0.05 |  |
| 5 | n_sig | = | 7 | 053 Sst Gaba | — | cell | genes | unstated | pval < 0.001 |  |
| 6 | score | = | -4.023 | 053 Sst Gaba | Ctnna2 | gene | — | — | — |  |
| 7 | logfc | = | -0.584 | 053 Sst Gaba | Ctnna2 | gene | — | — | — |  |
| 8 | pval | = | 5.75e-5 | 053 Sst Gaba | Ctnna2 | gene | — | — | — |  |
| 9 | padj | = | 0.9444 | 053 Sst Gaba | Ctnna2 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 31. Klrk1 / E006

Row cell_type field: `empty`

Raw statistics text:

> A targeted scan for 41 NKG2D-adaptor, NK-receptor, ligand, and broad signaling labels found rows for Klrk1, Fyn, Cd247, Mapk1, Pik3r1, and Rac1; it returned no rows for the core adaptors Hcst or Tyrobp, Klrc1-4, Klrd1, Ncr1, Zap70, Syk, Lat, Lck, Vav1, Plcg1, Plcg2, mouse Raet1/H60 ligand names, or Ulbp1-3.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 32. Kmt2e / E005

Row cell_type field: `empty`

Raw statistics text:

> At FDR<0.25, the intersection between the 151 TH Prkcd Grin2c Glut and 155 MB Glut signatures contained exactly three genes. Snhg11 logFC +0.107 FDR 0.0219 in 151 and +0.162 FDR 0.0533 in 155; Atp6v0b +0.182 FDR 0.110 in 151 and +0.287 FDR 0.0644 in 155; Eno2 +0.201 FDR 0.0310 in 151 and +0.261 FDR 0.193 in 155.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 33. Lepr / E008

Row cell_type field: `145 MH-LH TH Glut`

Raw statistics text:

> Mc4r perturbation: 71 perturbed cells, Smox score 4.953 logFC 1.179 p=7.31e-7 FDR=0.0122, 1 gene at FDR<0.1. Lepr perturbation: 55 perturbed cells, best gene Shank3 score -3.535 p=4.08e-4 FDR=1.0, 0 genes at FDR<0.1; Lepr target row p=0.793 FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 55 | 145 MH-LH TH Glut | — | cell | — | — | — |  |
| 2 | score | = | -3.535 | 145 MH-LH TH Glut | Shank3 | gene | — | — | — |  |
| 3 | pval | = | 4.08e-4 | 145 MH-LH TH Glut | Shank3 | gene | — | — | — |  |
| 4 | padj | = | 1.0 | 145 MH-LH TH Glut | Shank3 | gene | — | — | — |  |
| 5 | n_sig | = | 0 | 145 MH-LH TH Glut | — | cell | genes | unstated | padj < 0.1 |  |
| 6 | pval | = | 0.793 | 145 MH-LH TH Glut | Lepr | gene | — | — | — |  |
| 7 | padj | = | 1.0 | 145 MH-LH TH Glut | Lepr | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 34. Lgals3 / E008

Row cell_type field: `empty`

Raw statistics text:

> St3gal5 had significant on-target depletion in 10 cell types: target-row FDR 1.96e-14 to 0.0209 and scores -8.821 to -4.847; in each of those cell types exactly one gene reached FDR<0.05, and 155 MB Glut was the only one with a second gene at FDR<0.10.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 35. Lhcgr / E002

Row cell_type field: `empty`

Raw statistics text:

> 0 of 371,818 Lhcgr-versus-Non_target gene tests had pvals_adj < 0.05 across 22 subclasses.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  |
| 2 | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 36. Lmbrd1 / E007

Row cell_type field: `empty`

Raw statistics text:

> In 046 CTX-CGE GABA, Lmbrd1 score 0.155, logFC 0.107, p=0.877, FDR=1; in 308 CB GABA, Lmbrd1 score 0.800, logFC 0.101, p=0.424, FDR=1.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | score | = | 0.155 | 046 CTX-CGE GABA | Lmbrd1 | gene | — | — | — |  |
| 2 | logfc | = | 0.107 | 046 CTX-CGE GABA | Lmbrd1 | gene | — | — | — |  |
| 3 | pval | = | 0.877 | 046 CTX-CGE GABA | Lmbrd1 | gene | — | — | — |  |
| 4 | padj | = | 1 | 046 CTX-CGE GABA | Lmbrd1 | gene | — | — | — |  |
| 5 | score | = | 0.800 | 308 CB GABA | Lmbrd1 | gene | — | — | — |  |
| 6 | logfc | = | 0.101 | 308 CB GABA | Lmbrd1 | gene | — | — | — |  |
| 7 | pval | = | 0.424 | 308 CB GABA | Lmbrd1 | gene | — | — | — |  |
| 8 | padj | = | 1 | 308 CB GABA | Lmbrd1 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 37. Lrch1 / E002

Row cell_type field: `empty`

Raw statistics text:

> Lrch1 transcript was measured in 21 cell classes; 17 of 21 scores were negative and 4 of 21 were positive; all Lrch1 self-transcript rows had FDR=1.0. Strongest nominal self-transcript rows: 151 TH Prkcd Grin2c Glut score -2.320 logFC -0.150 p=0.0203; 191 MB P MY GABA score -2.199 logFC -0.458 p=0.0279; 052 Pvalb Gaba score -1.985 logFC -0.377 p=0.0472; 145 MH-LH TH Glut score -1.961 logFC -0.398 p=0.0499; 066 CNU-HYa HY GABA score -1.909 logFC -0.413 p=0.0563.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 38. Lztfl1 / E003

Row cell_type field: `empty`

Raw statistics text:

> Across all Lztfl1 rows, FDR<0.05 count=0 and FDR<0.10 count=1; the only 10% row was Cyld in 059 CNU-LGE LSX GABA, score 4.526, logFC 0.527, p=6.01e-6, FDR=0.099, while Lztfl1 in the same cell class had logFC -0.442, p=0.086, FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  |
| 2 | n_sig | = | 1 | — | — | target | rows | unstated | padj < 0.10 |  |
| 3 | score | = | 4.526 | 059 CNU-LGE LSX GABA | Cyld | gene | — | — | — |  |
| 4 | logfc | = | 0.527 | 059 CNU-LGE LSX GABA | Cyld | gene | — | — | — |  |
| 5 | pval | = | 6.01e-6 | 059 CNU-LGE LSX GABA | Cyld | gene | — | — | — |  |
| 6 | padj | = | 0.099 | 059 CNU-LGE LSX GABA | Cyld | gene | — | — | — |  |
| 7 | logfc | = | -0.442 | 059 CNU-LGE LSX GABA | Lztfl1 | gene | — | — | — |  |
| 8 | pval | = | 0.086 | 059 CNU-LGE LSX GABA | Lztfl1 | gene | — | — | — |  |
| 9 | padj | = | 1.0 | 059 CNU-LGE LSX GABA | Lztfl1 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 39. Mafb / E003

Row cell_type field: `052 Pvalb Gaba`

Raw statistics text:

> 88 Mafb-perturbed cells versus 13710 controls; Ccdc88a logFC=-0.503, score=-4.69, p=2.69e-06, FDR=0.0450. The next ranked genes Man2a2 and Psmg1 both had FDR=0.796. Mafb itself had logFC=-0.213, p=0.152, FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 88 | 052 Pvalb Gaba | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 13710 | 052 Pvalb Gaba | — | cell | — | — | — |  |
| 3 | logfc | = | -0.503 | 052 Pvalb Gaba | Ccdc88a | gene | — | — | — |  |
| 4 | score | = | -4.69 | 052 Pvalb Gaba | Ccdc88a | gene | — | — | — |  |
| 5 | pval | = | 2.69e-06 | 052 Pvalb Gaba | Ccdc88a | gene | — | — | — |  |
| 6 | padj | = | 0.0450 | 052 Pvalb Gaba | Ccdc88a | gene | — | — | — |  |
| 7 | padj | = | 0.796 | 052 Pvalb Gaba | Psmg1 | gene | — | — | — |  |
| 8 | logfc | = | -0.213 | 052 Pvalb Gaba | Mafb | gene | — | — | — |  |
| 9 | pval | = | 0.152 | 052 Pvalb Gaba | Mafb | gene | — | — | — |  |
| 10 | padj | = | 1.0 | 052 Pvalb Gaba | Mafb | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 40. Max / E006

Row cell_type field: `empty`

Raw statistics text:

> Mga perturbation produced only 3 FDR<0.05 rows overall but included Stag3 in 151 TH Prkcd Grin2c Glut (logFC 3.606, FDR 4.83e-5) and 155 MB Glut (logFC 3.633, FDR 1.93e-4); Obscn was also up in Mga-perturbed 151 cells (logFC 4.435, FDR 1.73e-8).

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 41. Med23 / E008

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> None of 11 immediate-early or activity-response genes tested in 151 TH Prkcd Grin2c Glut reached FDR<0.05 under Med23 perturbation; Jun was nominally up (logFC 0.376, p=0.0117, FDR=1.0), Fos was near zero (logFC -0.0649, p=0.910, FDR=1.0), and Arc was near zero (logFC -0.0381, p=0.813, FDR=1.0).

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | logfc | = | 0.376 | 151 TH Prkcd Grin2c Glut | Jun | gene | — | — | — |  |
| 2 | pval | = | 0.0117 | 151 TH Prkcd Grin2c Glut | Jun | gene | — | — | — |  |
| 3 | padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Jun | gene | — | — | — |  |
| 4 | logfc | = | -0.0649 | 151 TH Prkcd Grin2c Glut | Fos | gene | — | — | — |  |
| 5 | pval | = | 0.910 | 151 TH Prkcd Grin2c Glut | Fos | gene | — | — | — |  |
| 6 | padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Fos | gene | — | — | — |  |
| 7 | logfc | = | -0.0381 | 151 TH Prkcd Grin2c Glut | Arc | gene | — | — | — |  |
| 8 | pval | = | 0.813 | 151 TH Prkcd Grin2c Glut | Arc | gene | — | — | — |  |
| 9 | padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Arc | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 42. Mtnr1b / E005

Row cell_type field: `empty`

Raw statistics text:

> Per-cell-type Mtnr1b n_pert_matched values were 20-162 with median 56.5; the three largest were 151 TH Prkcd Grin2c Glut n=162, 155 MB Glut n=136, and 005 L4-5 IT CTX Glut n=109; the smallest was 217 P MY Pineal Glut n=20.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 162 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 2 | n_pert | = | 136 | 155 MB Glut | — | cell | — | — | — |  |
| 3 | n_pert | = | 109 | 005 L4-5 IT CTX Glut | — | cell | — | — | — |  |
| 4 | n_pert | = | 20 | 217 P MY Pineal Glut | — | cell | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 43. Neo1 / E001

Row cell_type field: `empty`

Raw statistics text:

> 21 subclasses; 355046 Neo1 target-comparison rows; 29-167 perturbed cells and 4807-23679 controls per subclass; Neo1 transcript row measured in all 21; 20/21 target-row logFC values were negative; 4/21 had nominal target-row p<0.05; best target row was 151 TH Prkcd Grin2c Glut with score -3.911, logFC -0.447, p=9.17e-5, FDR=0.792.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 355046 | — | — | target | rows | unstated | — |  |
| 2 | score | = | -3.911 | 151 TH Prkcd Grin2c Glut | Neo1 | gene | — | — | — |  |
| 3 | logfc | = | -0.447 | 151 TH Prkcd Grin2c Glut | Neo1 | gene | — | — | — |  |
| 4 | pval | = | 9.17e-5 | 151 TH Prkcd Grin2c Glut | Neo1 | gene | — | — | — |  |
| 5 | padj | = | 0.792 | 151 TH Prkcd Grin2c Glut | Neo1 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 44. Nfib / E006

Row cell_type field: `empty`

Raw statistics text:

> The two Nfic FDR < 0.05 rows were Bambi in 151 TH Prkcd Grin2c Glut, logFC 0.721, p = 2.21e-7, FDR = 0.00382, n = 297 perturbed cells; and the Nfic self row in 155 MB Glut, logFC -0.504, p = 1.00e-6, FDR = 0.0175, n = 260 perturbed cells.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 45. Nfkb1 / E007

Row cell_type field: `empty`

Raw statistics text:

> Global Pearson correlations of Wilcoxon score vectors versus Nfkb1 across shared features were Rel -0.0009, Map3k7 0.0011, Traf3 0.0054, Nfkb2 0.0108, Relb 0.0118, and Chuk 0.0129.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 46. Nr2c1 / E002

Row cell_type field: `empty`

Raw statistics text:

> 371818 Nr2c1 gene-level rows across 22 cell classes; 1 row with pvals_adj<0.05; 86 rows with raw p<0.001; 1125 rows with raw p<0.01.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 371818 | — | — | target | rows | unstated | — |  |
| 2 | n_sig | = | 1 | — | — | target | rows | unstated | padj < 0.05 |  |
| 3 | n_sig | = | 86 | — | — | target | rows | unstated | pval < 0.001 |  |
| 4 | n_sig | = | 1125 | — | — | target | rows | unstated | pval < 0.01 |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 47. Nr2f2 / E009

Row cell_type field: `empty`

Raw statistics text:

> Nr2c2 was the second-most negative Nr2f2 neighbor in 017 CA3 CA2-FC DG Glut (r=-0.252, rank 2029/2030) and in 001 L5-6 IT Glut (r=-0.086, rank 1874/1875).

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 48. Pax7 / E002

Row cell_type field: `empty`

Raw statistics text:

> 371,818 Pax7 differential-expression rows across 22 cell classes; 1 row had FDR<0.05, 1 row had FDR<0.20, and the second-smallest FDR was 0.204478.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  |
| 2 | n_sig | = | 1 | — | — | target | rows | unstated | padj < 0.05 |  |
| 3 | n_sig | = | 1 | — | — | target | rows | unstated | padj < 0.20 |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 49. Pdcd10 / E003

Row cell_type field: `052 Pvalb Gaba`

Raw statistics text:

> 91 perturbed cells versus 13710 controls; Pdcd10 logFC -0.475, score -3.168, p=0.00154, FDR=1.0, rank 6 by absolute score and rank 2 among negative scores; Srm logFC 0.650, score 3.965, p=7.33e-5, FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 91 | 052 Pvalb Gaba | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 13710 | 052 Pvalb Gaba | — | cell | — | — | — |  |
| 3 | logfc | = | -0.475 | 052 Pvalb Gaba | Pdcd10 | gene | — | — | — |  |
| 4 | score | = | -3.168 | 052 Pvalb Gaba | Pdcd10 | gene | — | — | — |  |
| 5 | pval | = | 0.00154 | 052 Pvalb Gaba | Pdcd10 | gene | — | — | — |  |
| 6 | padj | = | 1.0 | 052 Pvalb Gaba | Pdcd10 | gene | — | — | — |  |
| 7 | logfc | = | 0.650 | 052 Pvalb Gaba | Srm | gene | — | — | — |  |
| 8 | score | = | 3.965 | 052 Pvalb Gaba | Srm | gene | — | — | — |  |
| 9 | pval | = | 7.33e-5 | 052 Pvalb Gaba | Srm | gene | — | — | — |  |
| 10 | padj | = | 1.0 | 052 Pvalb Gaba | Srm | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 50. Plec / E008

Row cell_type field: `001 L5-6 IT Glut`

Raw statistics text:

> Pearson correlations of 16723-gene score vectors between Plec and 1874 other perturbations in 001 L5-6 IT Glut ranged from Adnp r=-0.064 to Nhs r=0.069; the STRING-linked Dag1 perturbation had r=0.051.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 51. Pou2f2 / E005

Row cell_type field: `217 P MY Pineal Glut`

Raw statistics text:

> 32 Pou2f2 cells versus 3,465 controls; Tbc1d9b score -4.135, logFC -0.740, nominal p=3.56e-5, FDR=0.5964; BC005537 score -3.962, logFC -0.709, nominal p=7.4e-5, FDR=0.6234.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 32 | 217 P MY Pineal Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 3,465 | 217 P MY Pineal Glut | — | cell | — | — | — |  |
| 3 | score | = | -4.135 | 217 P MY Pineal Glut | Tbc1d9b | gene | — | — | — |  |
| 4 | logfc | = | -0.740 | 217 P MY Pineal Glut | Tbc1d9b | gene | — | — | — |  |
| 5 | pval | = | 3.56e-5 | 217 P MY Pineal Glut | Tbc1d9b | gene | — | — | — |  |
| 6 | padj | = | 0.5964 | 217 P MY Pineal Glut | Tbc1d9b | gene | — | — | — |  |
| 7 | score | = | -3.962 | 217 P MY Pineal Glut | BC005537 | gene | — | — | — |  |
| 8 | logfc | = | -0.709 | 217 P MY Pineal Glut | BC005537 | gene | — | — | — |  |
| 9 | pval | = | 7.4e-5 | 217 P MY Pineal Glut | BC005537 | gene | — | — | — |  |
| 10 | padj | = | 0.6234 | 217 P MY Pineal Glut | BC005537 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 52. Ppip5k2 / E007

Row cell_type field: `empty`

Raw statistics text:

> For Pten perturbation, FDR<0.05 genes were detected in 151 TH Prkcd Grin2c Glut (33), 155 MB Glut (11), and 191 MB P MY GABA (1). Mtor had 2 FDR<0.05 genes in 151 TH Prkcd Grin2c Glut, and Plcb1 had 1 in 005 L4-5 IT CTX Glut; Inpp5k had 0 in all 22 overlapping Ppip5k2 cell types.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 53. Prdm2 / E006

Row cell_type field: `empty`

Raw statistics text:

> Across the 22 Prdm2 cell types, mean full-transcriptome Pearson correlations of Wilcoxon scores with Prdm2 were Prdm5 r = -0.0005, Prdm10 r = 0.0094, Prdm12 r = 0.0074, and Prdm16 r = 0.0022; all individual cell-type correlations across these four paralogs were between -0.065 and 0.089.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 54. Rel / E005

Row cell_type field: `empty`

Raw statistics text:

> Relb, Nfkb1, Nfkb2, Chuk, and Traf3 produced 1891546 combined gene rows across their available cell types; 0 rows had FDR < 0.05. Their target-transcript rows also had 0 FDR-significant detections.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 55. Rnf13 / E006

Row cell_type field: `empty`

Raw statistics text:

> In the five classes with nominal Rnf13 target-transcript decrease, the 50 tests covering Atf6, Hspa5, Mapk8, Mapk9, Xbp1, Ern1, Traf2, Ddit3, Bax, and Bcl2l11 had median |score| 0.625 and no FDR < 0.05; the only nominal p<0.05 marker was Bax in 191 MB P MY GABA, logFC 0.377, score 2.209, p=0.0272, FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | logfc | = | 0.377 | 191 MB P MY GABA | Bax | gene | — | — | — |  |
| 2 | score | = | 2.209 | 191 MB P MY GABA | Bax | gene | — | — | — |  |
| 3 | pval | = | 0.0272 | 191 MB P MY GABA | Bax | gene | — | — | — |  |
| 4 | padj | = | 1.0 | 191 MB P MY GABA | Bax | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 56. Ror1 / E004

Row cell_type field: `017 CA3 CA2-FC DG Glut`

Raw statistics text:

> 65 Ror1-perturbed cells; 0 genes with pvals_adj < 0.05; top rows: Bin1 logFC -0.413 p=8.9e-05 pvals_adj 0.458853, Me1 logFC -1.356 p=1.20e-04 pvals_adj 0.458853, Kcnj4 logFC 0.949 p=1.30e-04 pvals_adj 0.458853.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 65 | 017 CA3 CA2-FC DG Glut | — | cell | — | — | — |  |
| 2 | n_sig | = | 0 | 017 CA3 CA2-FC DG Glut | — | cell | genes | unstated | padj < 0.05 |  |
| 3 | logfc | = | -0.413 | 017 CA3 CA2-FC DG Glut | Bin1 | gene | — | — | — |  |
| 4 | pval | = | 8.9e-05 | 017 CA3 CA2-FC DG Glut | Bin1 | gene | — | — | — |  |
| 5 | padj | = | 0.458853 | 017 CA3 CA2-FC DG Glut | Bin1 | gene | — | — | — |  |
| 6 | logfc | = | -1.356 | 017 CA3 CA2-FC DG Glut | Me1 | gene | — | — | — |  |
| 7 | pval | = | 1.20e-04 | 017 CA3 CA2-FC DG Glut | Me1 | gene | — | — | — |  |
| 8 | padj | = | 0.458853 | 017 CA3 CA2-FC DG Glut | Me1 | gene | — | — | — |  |
| 9 | logfc | = | 0.949 | 017 CA3 CA2-FC DG Glut | Kcnj4 | gene | — | — | — |  |
| 10 | pval | = | 1.30e-04 | 017 CA3 CA2-FC DG Glut | Kcnj4 | gene | — | — | — |  |
| 11 | padj | = | 0.458853 | 017 CA3 CA2-FC DG Glut | Kcnj4 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 57. Rsrc1 / E003

Row cell_type field: `empty`

Raw statistics text:

> 151 TH Prkcd Grin2c Glut had 233 perturbed cells and 0 genes at FDR<0.25; 155 MB Glut had 205 perturbed cells and 0 genes at FDR<0.25. In 155 MB Glut the top nominal positive row was Srsf9, score 3.807, p=0.000141, FDR=0.614, and the top negative row was Ndufa10, score -4.071, p=0.000047, FDR=0.614.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 233 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 2 | n_sig | = | 0 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.25 |  |
| 3 | n_pert | = | 205 | 155 MB Glut | — | cell | — | — | — |  |
| 4 | n_sig | = | 0 | 155 MB Glut | — | cell | genes | unstated | padj < 0.25 |  |
| 5 | score | = | 3.807 | 155 MB Glut | Srsf9 | gene | — | — | — |  |
| 6 | pval | = | 0.000141 | 155 MB Glut | Srsf9 | gene | — | — | — |  |
| 7 | padj | = | 0.614 | 155 MB Glut | Srsf9 | gene | — | — | — |  |
| 8 | score | = | -4.071 | 155 MB Glut | Ndufa10 | gene | — | — | — |  |
| 9 | pval | = | 0.000047 | 155 MB Glut | Ndufa10 | gene | — | — | — |  |
| 10 | padj | = | 0.614 | 155 MB Glut | Ndufa10 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 58. Serpini1 / E009

Row cell_type field: `empty`

Raw statistics text:

> Plat, Plau, Plaur, and Plg were absent as gene_target perturbations. App, Lrp1, and Prnp were present, but their maximum absolute Pearson correlations with Serpini1 score vectors across shared cell types were 0.105, 0.097, and 0.078 respectively.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 59. Sp4 / E002

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> 183 perturbed cells versus 23679 matched controls; 14 genes at FDR<0.05. Top effects included Stxbp2 logFC=-1.069, score=-7.400, FDR=2.35e-09; Svip logFC=0.643, score=6.267, FDR=3.17e-06; Tspan17 logFC=-0.695, score=-6.182, FDR=3.64e-06; Strada logFC=0.469, score=5.842, FDR=2.23e-05; Tsga10 logFC=0.772, FDR=7.23e-04.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 183 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 23679 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 3 | n_sig | = | 14 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  |
| 4 | logfc | = | -1.069 | 151 TH Prkcd Grin2c Glut | Stxbp2 | gene | — | — | — |  |
| 5 | score | = | -7.400 | 151 TH Prkcd Grin2c Glut | Stxbp2 | gene | — | — | — |  |
| 6 | padj | = | 2.35e-09 | 151 TH Prkcd Grin2c Glut | Stxbp2 | gene | — | — | — |  |
| 7 | logfc | = | 0.643 | 151 TH Prkcd Grin2c Glut | Svip | gene | — | — | — |  |
| 8 | score | = | 6.267 | 151 TH Prkcd Grin2c Glut | Svip | gene | — | — | — |  |
| 9 | padj | = | 3.17e-06 | 151 TH Prkcd Grin2c Glut | Svip | gene | — | — | — |  |
| 10 | logfc | = | -0.695 | 151 TH Prkcd Grin2c Glut | Tspan17 | gene | — | — | — |  |
| 11 | score | = | -6.182 | 151 TH Prkcd Grin2c Glut | Tspan17 | gene | — | — | — |  |
| 12 | padj | = | 3.64e-06 | 151 TH Prkcd Grin2c Glut | Tspan17 | gene | — | — | — |  |
| 13 | logfc | = | 0.469 | 151 TH Prkcd Grin2c Glut | Strada | gene | — | — | — |  |
| 14 | score | = | 5.842 | 151 TH Prkcd Grin2c Glut | Strada | gene | — | — | — |  |
| 15 | padj | = | 2.23e-05 | 151 TH Prkcd Grin2c Glut | Strada | gene | — | — | — |  |
| 16 | logfc | = | 0.772 | 151 TH Prkcd Grin2c Glut | Tsga10 | gene | — | — | — |  |
| 17 | padj | = | 7.23e-04 | 151 TH Prkcd Grin2c Glut | Tsga10 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 60. Spast / E009

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> 141 perturbed cells versus 23,679 controls; Spast logFC -0.343, P=0.00756, FDR=1.0; 9 genes had P<0.001 and 61 had P<0.01; top nominal genes included Exoc4 logFC 0.274, P=1.92e-4; Kif1a logFC 0.172, P=2.40e-4; Clpp logFC 0.442, P=3.22e-4; Mkrn1 logFC 0.469, P=4.06e-4.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 141 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 23,679 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 3 | logfc | = | -0.343 | 151 TH Prkcd Grin2c Glut | Spast | gene | — | — | — |  |
| 4 | pval | = | 0.00756 | 151 TH Prkcd Grin2c Glut | Spast | gene | — | — | — |  |
| 5 | padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Spast | gene | — | — | — |  |
| 6 | n_sig | = | 9 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | pval < 0.001 |  |
| 7 | n_sig | = | 61 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | pval < 0.01 |  |
| 8 | logfc | = | 0.274 | 151 TH Prkcd Grin2c Glut | Exoc4 | gene | — | — | — |  |
| 9 | pval | = | 1.92e-4 | 151 TH Prkcd Grin2c Glut | Exoc4 | gene | — | — | — |  |
| 10 | logfc | = | 0.172 | 151 TH Prkcd Grin2c Glut | Kif1a | gene | — | — | — |  |
| 11 | pval | = | 2.40e-4 | 151 TH Prkcd Grin2c Glut | Kif1a | gene | — | — | — |  |
| 12 | logfc | = | 0.442 | 151 TH Prkcd Grin2c Glut | Clpp | gene | — | — | — |  |
| 13 | pval | = | 3.22e-4 | 151 TH Prkcd Grin2c Glut | Clpp | gene | — | — | — |  |
| 14 | logfc | = | 0.469 | 151 TH Prkcd Grin2c Glut | Mkrn1 | gene | — | — | — |  |
| 15 | pval | = | 4.06e-4 | 151 TH Prkcd Grin2c Glut | Mkrn1 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 61. Stmn2 / E003

Row cell_type field: `empty`

Raw statistics text:

> 017 CA3 CA2-FC DG Glut: 65 perturbed cells, Stmn2 logFC -0.203, p=0.243, FDR=1.0, no genes below FDR 0.5. 059 CNU-LGE LSX GABA: 67 perturbed cells, Stmn2 logFC -0.322, p=0.220, FDR=1.0, no genes below FDR 0.5.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 65 | 017 CA3 CA2-FC DG Glut | — | cell | — | — | — |  |
| 2 | logfc | = | -0.203 | 017 CA3 CA2-FC DG Glut | Stmn2 | gene | — | — | — |  |
| 3 | pval | = | 0.243 | 017 CA3 CA2-FC DG Glut | Stmn2 | gene | — | — | — |  |
| 4 | padj | = | 1.0 | 017 CA3 CA2-FC DG Glut | Stmn2 | gene | — | — | — |  |
| 5 | n_sig | = | 0 | 017 CA3 CA2-FC DG Glut | — | cell | genes | unstated | padj < 0.5 |  |
| 6 | n_pert | = | 67 | 059 CNU-LGE LSX GABA | — | cell | — | — | — |  |
| 7 | logfc | = | -0.322 | 059 CNU-LGE LSX GABA | Stmn2 | gene | — | — | — |  |
| 8 | pval | = | 0.220 | 059 CNU-LGE LSX GABA | Stmn2 | gene | — | — | — |  |
| 9 | padj | = | 1.0 | 059 CNU-LGE LSX GABA | Stmn2 | gene | — | — | — |  |
| 10 | n_sig | = | 0 | 059 CNU-LGE LSX GABA | — | cell | genes | unstated | padj < 0.5 |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 62. Sv2a / E001

Row cell_type field: `empty`

Raw statistics text:

> 371,818 Sv2a-perturbation rows covering 22 cell types; the Sv2a transcript row was negative in 22/22; 13/22 passed FDR<0.05 with logFC -0.70 to -1.39 and Wilcoxon scores -4.69 to -13.70.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 63. Tas2r118 / E008

Row cell_type field: `empty`

Raw statistics text:

> A scan of 2046 unique gene_target values found Tas2r118 as the only Tas2r entry and found no Tas1r1, Tas1r2, Tas1r3, Gnat3, Plcb2, Itpr3, or Trpm5 perturbation targets.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 64. Tlr7 / E002

Row cell_type field: `empty`

Raw statistics text:

> 19 Tlr7 self-transcript rows; Wilcoxon score range -0.184 to 0.286; nominal p range 0.7749-0.9909; pvals_adj=1.000 in all 19 rows.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 65. Tsga10 / E002

Row cell_type field: `empty`

Raw statistics text:

> Tsga10 mRNA was measured in 22/22 contrasts; all Tsga10 rows had FDR=1.0 and nominal p>=0.0764; logFC was negative in 18/22 contrasts and positive in 4/22; best nominal target row was 308 CB GABA logFC 0.415, score 1.772, p=0.0764, FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | logfc | = | 0.415 | 308 CB GABA | Tsga10 | gene | — | — | — |  |
| 2 | score | = | 1.772 | 308 CB GABA | Tsga10 | gene | — | — | — |  |
| 3 | pval | = | 0.0764 | 308 CB GABA | Tsga10 | gene | — | — | — |  |
| 4 | padj | = | 1.0 | 308 CB GABA | Tsga10 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 66. Tspan12 / E007

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> Fzd4: 188 perturbed cells, 0 genes at FDR<=0.05. Lrp5: 230 perturbed cells, 0 genes at FDR<=0.05. Lrp6: 120 perturbed cells, 4 genes at FDR<=0.05 and Axin2 logFC=-0.8002, p=2.54e-5, FDR=0.0731.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 67. Tuba4a / E011

Row cell_type field: `empty`

Raw statistics text:

> Tuba4a self rows with weak engagement included 053 Sst Gaba: 42 perturbed cells, logFC 0.029, p=0.902, FDR=1.0; 008 L2-3 IT ENT PPP RSP Glut: 47 perturbed cells, logFC -0.133, p=0.651, FDR=1.0; 308 CB GABA: 54 perturbed cells, logFC -0.140, p=0.673, FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 42 | 053 Sst Gaba | — | cell | — | — | — |  |
| 2 | logfc | = | 0.029 | 053 Sst Gaba | Tuba4a | gene | — | — | — |  |
| 3 | pval | = | 0.902 | 053 Sst Gaba | Tuba4a | gene | — | — | — |  |
| 4 | padj | = | 1.0 | 053 Sst Gaba | Tuba4a | gene | — | — | — |  |
| 5 | n_pert | = | 47 | 008 L2-3 IT ENT PPP RSP Glut | — | cell | — | — | — |  |
| 6 | logfc | = | -0.133 | 008 L2-3 IT ENT PPP RSP Glut | Tuba4a | gene | — | — | — |  |
| 7 | pval | = | 0.651 | 008 L2-3 IT ENT PPP RSP Glut | Tuba4a | gene | — | — | — |  |
| 8 | padj | = | 1.0 | 008 L2-3 IT ENT PPP RSP Glut | Tuba4a | gene | — | — | — |  |
| 9 | n_pert | = | 54 | 308 CB GABA | — | cell | — | — | — |  |
| 10 | logfc | = | -0.140 | 308 CB GABA | Tuba4a | gene | — | — | — |  |
| 11 | pval | = | 0.673 | 308 CB GABA | Tuba4a | gene | — | — | — |  |
| 12 | padj | = | 1.0 | 308 CB GABA | Tuba4a | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 68. Tubb2a / E003

Row cell_type field: `empty`

Raw statistics text:

> 11/371818 Tubb2a DE rows passed FDR<0.05; 9/11 were Tubb2a itself; only 2/371796 non-target rows passed FDR<0.05; 12 total rows passed FDR<0.10.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_sig | = | 11 | — | — | target | rows | unstated | padj < 0.05 |  |
| 2 | n_rows | = | 371818 | — | — | target | rows | unstated | — |  |
| 3 | n_sig | = | 2 | — | — | target | rows | exclude | padj < 0.05 |  |
| 4 | n_rows | = | 371796 | — | — | target | rows | exclude | — |  |
| 5 | n_sig | = | 12 | — | — | target | rows | unstated | padj < 0.10 |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 69. Uqcrq / E006

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> 345 perturbed cells versus 23679 controls; Gpr180 logFC -0.466410, score -4.709418, p=2.484e-06, FDR=0.042876; Uqcrq logFC -0.294505, score -2.391641, p=0.016773, FDR=1; only 1 gene in this class had FDR<0.05.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 345 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 23679 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  |
| 3 | logfc | = | -0.466410 | 151 TH Prkcd Grin2c Glut | Gpr180 | gene | — | — | — |  |
| 4 | score | = | -4.709418 | 151 TH Prkcd Grin2c Glut | Gpr180 | gene | — | — | — |  |
| 5 | pval | = | 2.484e-06 | 151 TH Prkcd Grin2c Glut | Gpr180 | gene | — | — | — |  |
| 6 | padj | = | 0.042876 | 151 TH Prkcd Grin2c Glut | Gpr180 | gene | — | — | — |  |
| 7 | logfc | = | -0.294505 | 151 TH Prkcd Grin2c Glut | Uqcrq | gene | — | — | — |  |
| 8 | score | = | -2.391641 | 151 TH Prkcd Grin2c Glut | Uqcrq | gene | — | — | — |  |
| 9 | pval | = | 0.016773 | 151 TH Prkcd Grin2c Glut | Uqcrq | gene | — | — | — |  |
| 10 | padj | = | 1 | 151 TH Prkcd Grin2c Glut | Uqcrq | gene | — | — | — |  |
| 11 | n_sig | = | 1 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 70. Usp48 / E007

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> Usp9x perturbation: 83 perturbed cells, Usp9x logFC -0.560, FDR 0.00354, with only 1 FDR<0.05 gene. Uchl1 perturbation: 250 perturbed cells, Uchl1 logFC -1.143, FDR 8.07e-60, with only 1 FDR<0.05 gene. Neither perturbation FDR-changed the 10 Usp48 downstream genes.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 71. Wac / E008

Row cell_type field: `empty`

Raw statistics text:

> Pearson correlations of Wac scores to all other perturbations: in 151 TH Prkcd Grin2c Glut, Ddx23 r=0.228 rank 1, Psmb4 r=0.227 rank 2, Prpf6 r=0.221 rank 3, Psmc5 r=0.204 rank 4, Psmc1 r=0.200 rank 6; in 155 MB Glut, Prpf6 r=0.220 rank 1, Psmc1 r=0.218 rank 2, Psmb4 r=0.206 rank 3, Pomp r=0.197 rank 5; in 052 Pvalb Gaba, Psmb4 r=0.176 rank 1, Psmc1 r=0.154 rank 2, Pomp r=0.144 rank 3, Prpf6 r=0.131 rank 5; in 066 CNU-HYa HY GABA, Psmc1 r=0.178 rank 1, Ddx23 r=0.168 rank 2, Psmb4 r=0.156 rank 3, Prpf6 r=0.153 rank 4, Pomp r=0.146 rank 5.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 72. Zfp106 / E006

Row cell_type field: `052 Pvalb Gaba`

Raw statistics text:

> 59 perturbed cells versus 13710 controls; Zfp106 logFC 0.207313, p=0.320920, FDR=1.0; Med8 logFC -1.169994, p=0.000018, FDR=0.246102; Ip6k1 logFC -0.602412, p=0.000029, FDR=0.246102; 0 genes at FDR<0.05.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 59 | 052 Pvalb Gaba | — | cell | — | — | — |  |
| 2 | n_ctrl | = | 13710 | 052 Pvalb Gaba | — | cell | — | — | — |  |
| 3 | logfc | = | 0.207313 | 052 Pvalb Gaba | Zfp106 | gene | — | — | — |  |
| 4 | pval | = | 0.320920 | 052 Pvalb Gaba | Zfp106 | gene | — | — | — |  |
| 5 | padj | = | 1.0 | 052 Pvalb Gaba | Zfp106 | gene | — | — | — |  |
| 6 | logfc | = | -1.169994 | 052 Pvalb Gaba | Med8 | gene | — | — | — |  |
| 7 | pval | = | 0.000018 | 052 Pvalb Gaba | Med8 | gene | — | — | — |  |
| 8 | padj | = | 0.246102 | 052 Pvalb Gaba | Med8 | gene | — | — | — |  |
| 9 | logfc | = | -0.602412 | 052 Pvalb Gaba | Ip6k1 | gene | — | — | — |  |
| 10 | pval | = | 0.000029 | 052 Pvalb Gaba | Ip6k1 | gene | — | — | — |  |
| 11 | padj | = | 0.246102 | 052 Pvalb Gaba | Ip6k1 | gene | — | — | — |  |
| 12 | n_sig | = | 0 | 052 Pvalb Gaba | — | cell | genes | unstated | padj < 0.05 |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 73. Zfp397 / E005

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 0/17442 non-Zfp397 genes with FDR < 0.05; best non-target rows: Ap2a1 score 3.576292 logFC 0.299479 p=0.000349 FDR=1, Irf2 score 3.547924 FDR=1, Rbm12b2 score -3.360078 FDR=1.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_sig | = | 0 | 155 MB Glut | — | cell | genes | exclude | padj < 0.05 |  |
| 2 | n_rows | = | 17442 | 155 MB Glut | — | cell | genes | exclude | — |  |
| 3 | score | = | 3.576292 | 155 MB Glut | Ap2a1 | gene | — | — | — |  |
| 4 | logfc | = | 0.299479 | 155 MB Glut | Ap2a1 | gene | — | — | — |  |
| 5 | pval | = | 0.000349 | 155 MB Glut | Ap2a1 | gene | — | — | — |  |
| 6 | padj | = | 1 | 155 MB Glut | Ap2a1 | gene | — | — | — |  |
| 7 | score | = | 3.547924 | 155 MB Glut | Irf2 | gene | — | — | — |  |
| 8 | padj | = | 1 | 155 MB Glut | Irf2 | gene | — | — | — |  |
| 9 | score | = | -3.360078 | 155 MB Glut | Rbm12b2 | gene | — | — | — |  |
| 10 | padj | = | 1 | 155 MB Glut | Rbm12b2 | gene | — | — | — |  |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

