# H1 annotation, sample 2: agreement audit

Both annotators produced identical annotations for each field below; these 20 fields
were drawn at random among such fields (`agreement_audit_sample`, seed 20261029). Check each
against section 3 (`H1_section3_rev10.md`): mark every row `✓` or `✗` (with the correction),
and add any in-scope assertion both missed under **Missed by both**. A single error in this
sample triggers the review of all its remaining agreed fields (decision DC-33).

Türkçe özet: Bu metinlerde iki notlayıcı tamamen aynı sonucu verdi. Her satırı ✓ veya ✗ ile
işaretleyin, ikisinin de atladığı ölçümleri ekleyin. Tek bir hata bile bulunursa o örneklemin
anlaşılan tüm metinleri gözden geçirilir.

## 1. Bmpr2 / E008

Row cell_type field: `empty`

Raw statistics text:

> In 15 related BMP/TGF receptor or SMAD perturbations, 0 target self-transcript rows had FDR<0.05; Bmpr2 had 2 self-transcript FDR<0.05 rows and 11 self-transcript nominal p<0.001 rows.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 2. Cic / E011

Row cell_type field: `empty`

Raw statistics text:

> Atxn1 was FDR-up after Cic perturbation in 151 TH Prkcd Grin2c Glut with logFC 0.496, p 1.91e-11, FDR 7.67e-09, and in 005 L4-5 IT CTX Glut with logFC 0.578, p 1.16e-06, FDR 0.00330; Atxn1 was nominally positive in five Cic-assayed cell types.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | logfc | = | 0.496 | 151 TH Prkcd Grin2c Glut | Atxn1 | gene | — | — | — | ✓ |
| 2 | pval | = | 1.91e-11 | 151 TH Prkcd Grin2c Glut | Atxn1 | gene | — | — | — | ✓ |
| 3 | padj | = | 7.67e-09 | 151 TH Prkcd Grin2c Glut | Atxn1 | gene | — | — | — | ✓ |
| 4 | logfc | = | 0.578 | 005 L4-5 IT CTX Glut | Atxn1 | gene | — | — | — | ✓ |
| 5 | pval | = | 1.16e-06 | 005 L4-5 IT CTX Glut | Atxn1 | gene | — | — | — | ✓ |
| 6 | padj | = | 0.00330 | 005 L4-5 IT CTX Glut | Atxn1 | gene | — | — | — | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 3. Cux1 / E006

Row cell_type field: `empty`

Raw statistics text:

> Cux2 target had 371818 rows across the same 22 Cux1-assayed cell groups; 2 total rows were FDR < 0.05: Cux2 in 151 TH Prkcd Grin2c Glut, logFC -0.428, p=8.54e-7, FDR 0.0147, and Sun1 in 053 Sst GABA, logFC 0.916, p=2.43e-6, FDR 0.0400.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 4. Epm2a / E004

Row cell_type field: `empty`

Raw statistics text:

> Among the top 20 absolute-score genes from each of 22 Epm2a cell types, only 13 genes recurred twice and none recurred more than twice; several recurrent genes flipped sign, including Bscl2, Faf2, Mob4, Pum2, Rnmt, and Sumo3.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 5. Fam120a / E010

Row cell_type field: `empty`

Raw statistics text:

> Across all same-cell-type target signatures, the largest positive Fam120a Pearson neighbor was Wdr26 in 308 CB GABA at r=0.235; the largest negative neighbor was B9d1 in 308 CB GABA at r=-0.202; all other cell-type maxima had |r|<=0.200.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 6. Gfpt1 / E011

Row cell_type field: `empty`

Raw statistics text:

> Pearson score correlations between Gfpt1 and Ogt perturbations were low: r=0.146 in 151 TH Prkcd Grin2c Glut, r=0.090 in 155 MB Glut, and r=0.064 in 052 Pvalb Gaba. In 151, Ogt knockdown had 4 FDR<0.05 genes versus 311 for Gfpt1; in 155, Ogt knockdown had 536 FDR<0.05 genes led by Xpo1/Rsrp1 rather than Hspa5/Sdf2l1; in Pvalb, Ogt knockdown had 109 FDR<0.05 genes whereas Gfpt1 had zero.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 7. Gfra1 / E009

Row cell_type field: `empty`

Raw statistics text:

> gene_target filters returned zero rows for Gdnf, Gfra2, Gfra3, Gfra4, Nrtn, Artn, and Pspn; Ret was profiled in 23 cell types with 0 total genes at FDR<0.1, and its best own-transcript row was 215 MB Dopa with 23 perturbed cells, score -4.44, p=9.20e-6, FDR=0.149.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 8. Gpr158 / E008

Row cell_type field: `empty`

Raw statistics text:

> Gpr179 perturbations contributed 371818 rows across 22 cell types; no row for any gene had FDR<0.1, the minimum row FDR was 0.2816, and every exact Gpr179 target-transcript row had FDR=1.0.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 9. Kcnc2 / E001

Row cell_type field: `052 Pvalb Gaba`

Raw statistics text:

> 72 perturbed cells versus 13710 controls; Kcnc2 score -5.657, logFC -0.752, p=1.54e-08, FDR=2.59e-04.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 72 | 052 Pvalb Gaba | — | cell | — | — | — | ✓ |
| 2 | n_ctrl | = | 13710 | 052 Pvalb Gaba | — | cell | — | — | — | ✓ |
| 3 | score | = | -5.657 | 052 Pvalb Gaba | Kcnc2 | gene | — | — | — | ✓ |
| 4 | logfc | = | -0.752 | 052 Pvalb Gaba | Kcnc2 | gene | — | — | — | ✓ |
| 5 | pval | = | 1.54e-08 | 052 Pvalb Gaba | Kcnc2 | gene | — | — | — | ✓ |
| 6 | padj | = | 2.59e-04 | 052 Pvalb Gaba | Kcnc2 | gene | — | — | — | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 10. Minar2 / E007

Row cell_type field: `empty`

Raw statistics text:

> Across their assayed rows, Tsc1 had 1,162 FDR<0.05 genes and Tsc2 had 423; Mtor had 2, Rptor had 0, Akt3 had 0, Notch1 had 1, Notch2 had 0, Notch3 had 0, and Notch4 had 1.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 11. Nefl / E009

Row cell_type field: `empty`

Raw statistics text:

> For each listed NMDA/PSD/MAPK transcript, the minimum FDR across all Nefl cell types was 1.0. Best nominal p values included Grin1 p=0.00172, Grin2c p=0.0225, Dlg4 p=0.0223, Camk2a p=0.0393, Mapk1 p=0.0495, Raf1 p=0.248, and Mapk3 p=0.190.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 12. Ogfrl1 / E006

Row cell_type field: `empty`

Raw statistics text:

> The top five nominal genes from each of 22 cell types yielded 110 gene entries with no repeated gene name; among top-10 lists only Odf2 recurred, twice; among top-20 lists the maximum recurrence for any gene was 2 cell types.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 13. Peg3 / E003

Row cell_type field: `empty`

Raw statistics text:

> Five Peg3 target rows were not nominally significant: 017 CA3 CA2-FC DG Glut score -1.697, logFC -0.214, p=0.0898; 059 CNU-LGE LSX GABA score -1.214, logFC -0.266, p=0.225; 008 L2-3 IT ENT PPP RSP Glut score -1.166, logFC -0.156, p=0.244; 009 L2-3 IT PIR AON ENT Glut score -1.074, logFC -0.135, p=0.283; 001 L5-6 IT Glut score -0.929, logFC -0.132, p=0.353.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | score | = | -1.697 | 017 CA3 CA2-FC DG Glut | Peg3 | gene | — | — | — | ✓ |
| 2 | logfc | = | -0.214 | 017 CA3 CA2-FC DG Glut | Peg3 | gene | — | — | — | ✓ |
| 3 | pval | = | 0.0898 | 017 CA3 CA2-FC DG Glut | Peg3 | gene | — | — | — | ✓ |
| 4 | score | = | -1.214 | 059 CNU-LGE LSX GABA | Peg3 | gene | — | — | — | ✓ |
| 5 | logfc | = | -0.266 | 059 CNU-LGE LSX GABA | Peg3 | gene | — | — | — | ✓ |
| 6 | pval | = | 0.225 | 059 CNU-LGE LSX GABA | Peg3 | gene | — | — | — | ✓ |
| 7 | score | = | -1.166 | 008 L2-3 IT ENT PPP RSP Glut | Peg3 | gene | — | — | — | ✓ |
| 8 | logfc | = | -0.156 | 008 L2-3 IT ENT PPP RSP Glut | Peg3 | gene | — | — | — | ✓ |
| 9 | pval | = | 0.244 | 008 L2-3 IT ENT PPP RSP Glut | Peg3 | gene | — | — | — | ✓ |
| 10 | score | = | -1.074 | 009 L2-3 IT PIR AON ENT Glut | Peg3 | gene | — | — | — | ✓ |
| 11 | logfc | = | -0.135 | 009 L2-3 IT PIR AON ENT Glut | Peg3 | gene | — | — | — | ✓ |
| 12 | pval | = | 0.283 | 009 L2-3 IT PIR AON ENT Glut | Peg3 | gene | — | — | — | ✓ |
| 13 | score | = | -0.929 | 001 L5-6 IT Glut | Peg3 | gene | — | — | — | ✓ |
| 14 | logfc | = | -0.132 | 001 L5-6 IT Glut | Peg3 | gene | — | — | — | ✓ |
| 15 | pval | = | 0.353 | 001 L5-6 IT Glut | Peg3 | gene | — | — | — | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 14. Ptch2 / E003

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 182 Ptch2-guide cells versus 20,353 controls; Ptpn5 score 4.430 logFC 0.454 nominal p=9.4e-06 FDR=0.164; Cep70 score 3.889 logFC 0.329 nominal p=1.01e-04 FDR=0.879; Fzd3 score 3.293 logFC 0.429 nominal p=9.92e-04 FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 182 | 155 MB Glut | — | cell | — | — | — | ✓ |
| 2 | n_ctrl | = | 20,353 | 155 MB Glut | — | cell | — | — | — | ✓ |
| 3 | score | = | 4.430 | 155 MB Glut | Ptpn5 | gene | — | — | — | ✓ |
| 4 | logfc | = | 0.454 | 155 MB Glut | Ptpn5 | gene | — | — | — | ✓ |
| 5 | pval | = | 9.4e-06 | 155 MB Glut | Ptpn5 | gene | — | — | — | ✓ |
| 6 | padj | = | 0.164 | 155 MB Glut | Ptpn5 | gene | — | — | — | ✓ |
| 7 | score | = | 3.889 | 155 MB Glut | Cep70 | gene | — | — | — | ✓ |
| 8 | logfc | = | 0.329 | 155 MB Glut | Cep70 | gene | — | — | — | ✓ |
| 9 | pval | = | 1.01e-04 | 155 MB Glut | Cep70 | gene | — | — | — | ✓ |
| 10 | padj | = | 0.879 | 155 MB Glut | Cep70 | gene | — | — | — | ✓ |
| 11 | score | = | 3.293 | 155 MB Glut | Fzd3 | gene | — | — | — | ✓ |
| 12 | logfc | = | 0.429 | 155 MB Glut | Fzd3 | gene | — | — | — | ✓ |
| 13 | pval | = | 9.92e-04 | 155 MB Glut | Fzd3 | gene | — | — | — | ✓ |
| 14 | padj | = | 1.0 | 155 MB Glut | Fzd3 | gene | — | — | — | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 15. Sptb / E003

Row cell_type field: `066 CNU-HYa HY GABA`

Raw statistics text:

> 59 perturbed cells versus 10110 controls; Raf1 logFC 0.588105 score 4.276751 P=1.89e-5 FDR=0.163071; Gabra2 logFC -1.144329 score -4.275661 P=1.91e-5 FDR=0.163071; Ypel4 logFC 0.492260 P=5.15e-5 FDR=0.293529; Sptb logFC -0.116286 P=0.707295 FDR=1.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 59 | 066 CNU-HYa HY GABA | — | cell | — | — | — | ✓ |
| 2 | n_ctrl | = | 10110 | 066 CNU-HYa HY GABA | — | cell | — | — | — | ✓ |
| 3 | logfc | = | 0.588105 | 066 CNU-HYa HY GABA | Raf1 | gene | — | — | — | ✓ |
| 4 | score | = | 4.276751 | 066 CNU-HYa HY GABA | Raf1 | gene | — | — | — | ✓ |
| 5 | pval | = | 1.89e-5 | 066 CNU-HYa HY GABA | Raf1 | gene | — | — | — | ✓ |
| 6 | padj | = | 0.163071 | 066 CNU-HYa HY GABA | Raf1 | gene | — | — | — | ✓ |
| 7 | logfc | = | -1.144329 | 066 CNU-HYa HY GABA | Gabra2 | gene | — | — | — | ✓ |
| 8 | score | = | -4.275661 | 066 CNU-HYa HY GABA | Gabra2 | gene | — | — | — | ✓ |
| 9 | pval | = | 1.91e-5 | 066 CNU-HYa HY GABA | Gabra2 | gene | — | — | — | ✓ |
| 10 | padj | = | 0.163071 | 066 CNU-HYa HY GABA | Gabra2 | gene | — | — | — | ✓ |
| 11 | logfc | = | 0.492260 | 066 CNU-HYa HY GABA | Ypel4 | gene | — | — | — | ✓ |
| 12 | pval | = | 5.15e-5 | 066 CNU-HYa HY GABA | Ypel4 | gene | — | — | — | ✓ |
| 13 | padj | = | 0.293529 | 066 CNU-HYa HY GABA | Ypel4 | gene | — | — | — | ✓ |
| 14 | logfc | = | -0.116286 | 066 CNU-HYa HY GABA | Sptb | gene | — | — | — | ✓ |
| 15 | pval | = | 0.707295 | 066 CNU-HYa HY GABA | Sptb | gene | — | — | — | ✓ |
| 16 | padj | = | 1 | 066 CNU-HYa HY GABA | Sptb | gene | — | — | — | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 16. Suco / E010

Row cell_type field: `empty`

Raw statistics text:

> In the 21 Suco classes, exact all-gene score correlations with available related perturbations were near zero: max |r| = 0.130 for Col11a1, 0.076 for Col2a1, 0.054 for Fam120a, and 0.054 for Hif1a; Col2a1 had one FDR < 0.05 gene in 017 CA3 CA2-FC DG Glut, and Fam120a and Hif1a had no FDR < 0.05 rows in this related subset.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 17. Tsc1 / E011

Row cell_type field: `empty`

Raw statistics text:

> In full within-cell-type score-vector correlations, Rab7 was the highest non-Tsc2 positive neighbor in 155 MB Glut (r=0.358), 151 TH Prkcd Grin2c Glut (r=0.358), and 191 MB P MY GABA (r=0.296); Rab7 was also positive in 066 CNU-HYa HY GABA (r=0.218) and 110 CNU-HYa HY MM Glut (r=0.205). Mtor was the strongest negative neighbor in 155 MB Glut (r=-0.268), 151 TH Prkcd Grin2c Glut (r=-0.222), and 191 MB P MY GABA (r=-0.162); Rptor was also negative in those classes (r=-0.134, -0.124, and -0.093).

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 18. Ufc1 / E007

Row cell_type field: `empty`

Raw statistics text:

> Across all measured genes, Ufc1-Uba5 Pearson correlations were 0.751 in 151 TH Prkcd Grin2c Glut, 0.515 in 155 MB Glut, and 0.383 in 191 MB P MY GABA. In 151, Uba5 was the top non-self positive neighbor of Ufc1 among 2046 perturbations; Uba5 had 2677 FDR<0.05 genes, and 495 of the 572 Ufc1 FDR genes also passed FDR under Uba5 with the same sign. In 155, 21 of 24 Ufc1 FDR genes overlapped Uba5 with the same sign; in 191, 6 of 18 overlapped with the same sign.

*Both annotators found no in-scope assertion in this field.*

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 19. Vps13a / E004

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 81 perturbed cells versus 20353 controls; Vps13a logFC -0.653920, score -3.489654, p=0.000484, FDR=1.0 and was the most negative gene; Idh3a score 3.878631, p=0.000105, FDR=1.0; Drosha score -3.436270, p=0.000590, FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 81 | 155 MB Glut | — | cell | — | — | — | ✓ |
| 2 | n_ctrl | = | 20353 | 155 MB Glut | — | cell | — | — | — | ✓ |
| 3 | logfc | = | -0.653920 | 155 MB Glut | Vps13a | gene | — | — | — | ✓ |
| 4 | score | = | -3.489654 | 155 MB Glut | Vps13a | gene | — | — | — | ✓ |
| 5 | pval | = | 0.000484 | 155 MB Glut | Vps13a | gene | — | — | — | ✓ |
| 6 | padj | = | 1.0 | 155 MB Glut | Vps13a | gene | — | — | — | ✓ |
| 7 | score | = | 3.878631 | 155 MB Glut | Idh3a | gene | — | — | — | ✓ |
| 8 | pval | = | 0.000105 | 155 MB Glut | Idh3a | gene | — | — | — | ✓ |
| 9 | padj | = | 1.0 | 155 MB Glut | Idh3a | gene | — | — | — | ✓ |
| 10 | score | = | -3.436270 | 155 MB Glut | Drosha | gene | — | — | — | ✓ |
| 11 | pval | = | 0.000590 | 155 MB Glut | Drosha | gene | — | — | — | ✓ |
| 12 | padj | = | 1.0 | 155 MB Glut | Drosha | gene | — | — | — | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 20. Ywhae / E010

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> Braf perturbation, 137 perturbed cells: Vgf FDR=1.39e-4 logFC=-0.795, Ptpn5 FDR=1.39e-4 logFC=-0.635, Atp2a2 FDR=1.39e-4 logFC=-0.263, Unc13a FDR=0.00393 logFC=-0.315. Ywhae perturbation, 157 perturbed cells: the same genes all FDR=1.0 with p=0.783, 0.257, 0.0446, and 0.149, respectively.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 157 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

