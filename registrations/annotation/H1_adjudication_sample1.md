# H1 annotation, sample 1: whole-field adjudication

Two independent annotators disagreed somewhere in each field below. Each field shows the raw
text and both versions, labelled X and Y (the label of each annotator is drawn at random per
field, so X is not always the same annotator). Rule on the **whole field** against section 3
of the pre-registration (`H1_section3_rev10.md`), including the rows both versions share.

In the **Ruling** column: `✓` keeps the row as shown; `✗` drops it (out of scope or wrong);
`✗ → <correction>` replaces it. Where X and Y give different versions of the same value
(source `X≠` / `Y≠`, differing columns named under *differs*), mark the right one ✓ and the
other ✗. Rows with source `X+Y` are identical in both versions. Add any in-scope assertion
that both versions missed in the **Missed by both** table. An explicitly identified
restricted population is out of scope as a subset count.

Self-inclusion labels (pre-registration §5, revision 13): `exclude` when the count's text or
lead-in has an exclusion qualifier (non-target, excluding/other than the target); `include`
only when it says "including the target/<Target>"; `unstated` when there is no qualifier.
Both versions are shown with this rule already applied, so some fields may show no visible
difference in the `self` column although the raw files differed there; review every field
in full regardless.

Türkçe özet: Her metinde iki notlayıcı en az bir yerde ayrışıyor. Metnin tamamını bölüm 3'e
göre değerlendirin: doğru satıra ✓, yanlış veya kapsam dışı satıra ✗ (gerekirse
`✗ → düzeltme`), ikisinin de atladığı ölçümleri en alttaki tabloya ekleyin. X/Y etiketi her
metinde rastgele; hangisinin hangi notlayıcı olduğunu bilmiyorsunuz. `self` sütunu: hedefi
dışlayan bir niteleme varsa `exclude`, açıkça "including the target" yazıyorsa `include`, hiçbir
niteleme yoksa `unstated`. İki versiyon bu kural uygulanmış olarak gösteriliyor; bu yüzden
bazı metinlerde görünür bir fark olmayabilir. Yine de her metni bütünüyle inceleyin.

27 fields.

## 1. Ap2m1 / E007

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> Ap2s1 perturbation used 310 perturbed cells versus 23679 controls; Ap2s1 logFC -0.536 FDR 6.33e-05; 1152 genes were FDR<0.05. Across the 139 Ap2m1 FDR genes, the Ap2m1-Ap2s1 Pearson score correlation was 0.920; 121/139 were also FDR<0.05 after Ap2s1 perturbation and all 121 had the same sign. Ap2s1 Tfrc logFC 0.984 FDR 3.06e-24; Mical2 logFC -1.227 FDR 2.95e-52; Prkcb logFC -1.015 FDR 2.13e-48.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | logfc | = | -0.536 | 151 TH Prkcd Grin2c Glut | Ap2s1 | gene | — | — | — |  | ✗ Other perturbation: Ap2s1. |
| 2 | X | padj | = | 6.33e-05 | 151 TH Prkcd Grin2c Glut | Ap2s1 | gene | — | — | — |  | ✗ Other perturbation: Ap2s1. |
| 3 | X | n_sig | = | 1152 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  | ✗ Other perturbation: Ap2s1. |
| 4 | X | logfc | = | 0.984 | 151 TH Prkcd Grin2c Glut | Tfrc | gene | — | — | — |  | ✗ Other perturbation: Ap2s1. |
| 5 | X | padj | = | 3.06e-24 | 151 TH Prkcd Grin2c Glut | Tfrc | gene | — | — | — |  | ✗ Other perturbation: Ap2s1. |
| 6 | X | logfc | = | -1.227 | 151 TH Prkcd Grin2c Glut | Mical2 | gene | — | — | — |  | ✗ Other perturbation: Ap2s1. |
| 7 | X | padj | = | 2.95e-52 | 151 TH Prkcd Grin2c Glut | Mical2 | gene | — | — | — |  | ✗ Other perturbation: Ap2s1. |
| 8 | X | logfc | = | -1.015 | 151 TH Prkcd Grin2c Glut | Prkcb | gene | — | — | — |  | ✗ Other perturbation: Ap2s1. |
| 9 | X | padj | = | 2.13e-48 | 151 TH Prkcd Grin2c Glut | Prkcb | gene | — | — | — |  | ✗ Other perturbation: Ap2s1. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 2. Armc9 / E004

Row cell_type field: `empty`

Raw statistics text:

> Nominal Armc9 p<0.05 target rows occurred in 052 Pvalb Gaba: logFC -0.392, p=0.00489; 005 L4-5 IT CTX Glut: logFC -0.266, p=0.0199; 054 CNU-MGE GABA: logFC -0.410, p=0.0305; 022 L5 ET CTX Glut: logFC -0.407, p=0.0314; 059 CNU-LGE LSX GABA: logFC -0.386, p=0.0362; all five had 0 FDR<0.10 genes.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | pval | < | 0.05 | 052 Pvalb Gaba | Armc9 | gene | — | — | — |  | ✓ |
| 2 | X+Y | logfc | = | -0.392 | 052 Pvalb Gaba | Armc9 | gene | — | — | — |  | ✓ |
| 3 | X+Y | pval | = | 0.00489 | 052 Pvalb Gaba | Armc9 | gene | — | — | — |  | ✓ |
| 4 | X+Y | logfc | = | -0.266 | 005 L4-5 IT CTX Glut | Armc9 | gene | — | — | — |  | ✓ |
| 5 | X+Y | pval | = | 0.0199 | 005 L4-5 IT CTX Glut | Armc9 | gene | — | — | — |  | ✓ |
| 6 | X+Y | logfc | = | -0.410 | 054 CNU-MGE GABA | Armc9 | gene | — | — | — |  | ✓ |
| 7 | X+Y | pval | = | 0.0305 | 054 CNU-MGE GABA | Armc9 | gene | — | — | — |  | ✓ |
| 8 | X+Y | logfc | = | -0.407 | 022 L5 ET CTX Glut | Armc9 | gene | — | — | — |  | ✓ |
| 9 | X+Y | pval | = | 0.0314 | 022 L5 ET CTX Glut | Armc9 | gene | — | — | — |  | ✓ |
| 10 | X+Y | logfc | = | -0.386 | 059 CNU-LGE LSX GABA | Armc9 | gene | — | — | — |  | ✓ |
| 11 | X+Y | pval | = | 0.0362 | 059 CNU-LGE LSX GABA | Armc9 | gene | — | — | — |  | ✓ |
| 12 | Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.10 |  | ✗ Restricted five-cell-type population; not target scope. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 3. Brsk2 / E007

Row cell_type field: `empty`

Raw statistics text:

> Brsk1 and Stk11 had 0 rows in the dataset. In 052 Pvalb Gaba, full-score Pearson r values to Brsk2 were Strada 0.0147, Mark3 0.0340, Prkaa2 0.00385, Mapt 0.0445 across 16,762 genes; the largest non-self positive correlation was 0.102. In 005 L4-5 IT CTX Glut, r values were Strada 0.0179, Mark3 -0.0135, Prkaa2 -0.0257, Mapt 0.0687 across 17,122 genes; the largest non-self positive correlation was 0.159.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | n_rows | = | 16,762 | 052 Pvalb Gaba | — | cell | genes | unstated | — |  | ✗ Correlation population; out of scope. |
| 2 | X | n_rows | = | 17,122 | 005 L4-5 IT CTX Glut | — | cell | genes | unstated | — |  | ✗ Correlation population; out of scope. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 4. Cdk8 / E004

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> 154 Med13 cells versus 23,679 controls; 11 genes at FDR<0.05, including Prkcd logFC -0.427 FDR=2.46e-04, Grin2b -0.249 FDR=0.00110, Plekhg1 -0.317 FDR=0.00195, Pcp4 -0.324 FDR=0.00276, Lrrtm1 -0.382 FDR=0.00276, Atp2a2 -0.236 FDR=0.00276, Grm1 -0.229 FDR=0.00702, Ramp3 -0.304 FDR=0.00814, and Scnm1 +0.634 FDR=0.0434.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | n_sig | = | 11 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  | ✗ Other perturbation: Med13. |
| 2 | Y | logfc | = | -0.427 | 151 TH Prkcd Grin2c Glut | Prkcd | gene | — | — | — |  | ✗ Other perturbation: Med13. |
| 3 | Y | padj | = | 2.46e-04 | 151 TH Prkcd Grin2c Glut | Prkcd | gene | — | — | — |  | ✗ Other perturbation: Med13. |
| 4 | Y | padj | = | 0.00110 | 151 TH Prkcd Grin2c Glut | Grin2b | gene | — | — | — |  | ✗ Other perturbation: Med13. |
| 5 | Y | padj | = | 0.00195 | 151 TH Prkcd Grin2c Glut | Plekhg1 | gene | — | — | — |  | ✗ Other perturbation: Med13. |
| 6 | Y | padj | = | 0.00276 | 151 TH Prkcd Grin2c Glut | Pcp4 | gene | — | — | — |  | ✗ Other perturbation: Med13. |
| 7 | Y | padj | = | 0.00276 | 151 TH Prkcd Grin2c Glut | Lrrtm1 | gene | — | — | — |  | ✗ Other perturbation: Med13. |
| 8 | Y | padj | = | 0.00276 | 151 TH Prkcd Grin2c Glut | Atp2a2 | gene | — | — | — |  | ✗ Other perturbation: Med13. |
| 9 | Y | padj | = | 0.00702 | 151 TH Prkcd Grin2c Glut | Grm1 | gene | — | — | — |  | ✗ Other perturbation: Med13. |
| 10 | Y | padj | = | 0.00814 | 151 TH Prkcd Grin2c Glut | Ramp3 | gene | — | — | — |  | ✗ Other perturbation: Med13. |
| 11 | Y | padj | = | 0.0434 | 151 TH Prkcd Grin2c Glut | Scnm1 | gene | — | — | — |  | ✗ Other perturbation: Med13. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 5. Cebpe / E005

Row cell_type field: `empty`

Raw statistics text:

> Within Cebpe perturbation, adjusted p was 1.0 for every tested row of Csf3r, Spi1, Gfi1, Gfi1b, Rara, Rxra, Gata1 and Sp1. Minimum nominal p by gene was Sp1 0.0848, Rara 0.1568, Rxra 0.2574, Csf3r 0.7095, Spi1 0.8042, Gfi1 0.8162, Gata1 0.8499 and Gfi1b 0.8715.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | min_pval | = | 0.0848 | — | Sp1 | gene | — | — | — |  | ✗ Gene-restricted minimum binding is not supplied by the required pattern. |
| 2 | Y | min_pval | = | 0.1568 | — | Rara | gene | — | — | — |  | ✗ Gene-restricted minimum binding is not supplied by the required pattern. |
| 3 | Y | min_pval | = | 0.2574 | — | Rxra | gene | — | — | — |  | ✗ Gene-restricted minimum binding is not supplied by the required pattern. |
| 4 | Y | min_pval | = | 0.7095 | — | Csf3r | gene | — | — | — |  | ✗ Gene-restricted minimum binding is not supplied by the required pattern. |
| 5 | Y | min_pval | = | 0.8042 | — | Spi1 | gene | — | — | — |  | ✗ Gene-restricted minimum binding is not supplied by the required pattern. |
| 6 | Y | min_pval | = | 0.8162 | — | Gfi1 | gene | — | — | — |  | ✗ Gene-restricted minimum binding is not supplied by the required pattern. |
| 7 | Y | min_pval | = | 0.8499 | — | Gata1 | gene | — | — | — |  | ✗ Gene-restricted minimum binding is not supplied by the required pattern. |
| 8 | Y | min_pval | = | 0.8715 | — | Gfi1b | gene | — | — | — |  | ✗ Gene-restricted minimum binding is not supplied by the required pattern. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 6. Cox11 / E002

Row cell_type field: `empty`

Raw statistics text:

> Cox11 transcript measured in 23/23 Cox11 cell-type tests; 16/23 logFC values were negative and 17/23 Wilcoxon scores were negative; nominal p<0.05 in 191 MB P MY GABA logFC -0.734 p=0.001138, 155 MB Glut logFC -0.502 p=0.010220, 053 Sst Gaba logFC -0.996 p=0.016610, and 110 CNU-HYa HY MM Glut logFC -0.759 p=0.018701; Cox11 p_adj=1.0 in every cell type.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | logfc | = | -0.734 | 191 MB P MY GABA | Cox11 | gene | — | — | — |  | ✓ |
| 2 | X+Y | pval | = | 0.001138 | 191 MB P MY GABA | Cox11 | gene | — | — | — |  | ✓ |
| 3 | X+Y | logfc | = | -0.502 | 155 MB Glut | Cox11 | gene | — | — | — |  | ✓ |
| 4 | X+Y | pval | = | 0.010220 | 155 MB Glut | Cox11 | gene | — | — | — |  | ✓ |
| 5 | X+Y | logfc | = | -0.996 | 053 Sst Gaba | Cox11 | gene | — | — | — |  | ✓ |
| 6 | X+Y | pval | = | 0.016610 | 053 Sst Gaba | Cox11 | gene | — | — | — |  | ✓ |
| 7 | X+Y | logfc | = | -0.759 | 110 CNU-HYa HY MM Glut | Cox11 | gene | — | — | — |  | ✓ |
| 8 | X+Y | pval | = | 0.018701 | 110 CNU-HYa HY MM Glut | Cox11 | gene | — | — | — |  | ✓ |
| 9 | Y | padj | = | 1.0 | 110 CNU-HYa HY MM Glut | Cox11 | gene | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 7. Foxl2 / E001

Row cell_type field: `empty`

Raw statistics text:

> 388,046 Foxl2-perturbation DE rows across 23 cell types; 0 genes at FDR<0.05 in every cell type; best cell-type minimum FDR=0.1249 and best nominal p=7.49e-06.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388,046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | min_padj | = | 0.1249 | — | — | target | — | — | — |  | ✓ |
| 4 | Y | min_pval | = | 7.49e-06 | — | — | target | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 8. Frrs1l / E005

Row cell_type field: `empty`

Raw statistics text:

> Within Frrs1l perturbations, none of Cpt1c, Gria1, Gria2, Gria3, Gria4, Cacng2, Cacng3, Cacng8, or Dlg4 was FDR<0.05 in any measured cell type; the smallest adjusted p value in this set was Gria2 in 308 CB GABA, logFC -0.536, p=0.00171, FDR=0.649; Cpt1c min p=0.0302, FDR=1.0; Dlg4 min p=0.0237, FDR=1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | logfc | = | -0.536 | 308 CB GABA | Gria2 | gene | — | — | — |  | ✓ |
| 2 | X+Y | pval | = | 0.00171 | 308 CB GABA | Gria2 | gene | — | — | — |  | ✓ |
| 3 | X+Y | padj | = | 0.649 | 308 CB GABA | Gria2 | gene | — | — | — |  | ✓ |
| 4 | X+Y | min_pval | = | 0.0302 | — | Cpt1c | gene | — | — | — |  | ✓ |
| 5 | X | padj | = | 1.0 | 308 CB GABA | Cpt1c | gene | — | — | — |  | ✓ |
| 6 | X+Y | min_pval | = | 0.0237 | — | Dlg4 | gene | — | — | — |  | ✓ |
| 7 | X | padj | = | 1.0 | 308 CB GABA | Dlg4 | gene | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 9. Glra2 / E008

Row cell_type field: `empty`

Raw statistics text:

> Glrb perturbation strongly depleted the Glrb row in 151 TH Prkcd Grin2c Glut, n=132, logFC=-0.782, p=1.01e-11, FDR=1.74e-7; 155 MB Glut, n=89, logFC=-0.810, p=1.92e-8, FDR=3.34e-4; and 191 MB P MY GABA, n=49, logFC=-1.139, p=8.30e-8, FDR=0.00142. In each of these three cell classes Glrb itself was the only FDR<0.05 gene.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | n_pert | = | 89 | 155 MB Glut | — | cell | — | — | — |  | ✗ Other perturbation: Glrb. |
| 2 | Y | logfc | = | -0.810 | 155 MB Glut | Glrb | gene | — | — | — |  | ✗ Other perturbation: Glrb. |
| 3 | Y | pval | = | 1.92e-8 | 155 MB Glut | Glrb | gene | — | — | — |  | ✗ Other perturbation: Glrb. |
| 4 | Y | padj | = | 3.34e-4 | 155 MB Glut | Glrb | gene | — | — | — |  | ✗ Other perturbation: Glrb. |
| 5 | Y | n_pert | = | 49 | 191 MB P MY GABA | — | cell | — | — | — |  | ✗ Other perturbation: Glrb. |
| 6 | Y | logfc | = | -1.139 | 191 MB P MY GABA | Glrb | gene | — | — | — |  | ✗ Other perturbation: Glrb. |
| 7 | Y | pval | = | 8.30e-8 | 191 MB P MY GABA | Glrb | gene | — | — | — |  | ✗ Other perturbation: Glrb. |
| 8 | Y | padj | = | 0.00142 | 191 MB P MY GABA | Glrb | gene | — | — | — |  | ✗ Other perturbation: Glrb. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 10. Grin2b / E008

Row cell_type field: `007 L2-3 IT CTX Glut`

Raw statistics text:

> In 007 L2-3 IT CTX Glut, Grin2b and Grin2a score vectors had Pearson r=-0.147 across 16753 genes, no overlapping FDR<0.05 genes, and Grin2a was the 3rd-most anticorrelated perturbation among 2011 Grin2b comparators; Grin2a yielded 20 FDR genes including Nptx2 logFC 1.777 FDR 6.09e-04, Scg2 logFC 1.292 FDR 0.00732, and Bdnf logFC 1.249 FDR 0.0272, whereas these genes trended negative after Grin2b perturbation. In 005 L4-5 IT CTX Glut, Grin2b versus Grin2a Pearson r=-0.081 across 17122 genes.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | n_rows | = | 17122 | 005 L4-5 IT CTX Glut | — | cell | genes | unstated | — |  | ✗ Correlation population; out of scope. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 11. Il4ra / E005

Row cell_type field: `empty`

Raw statistics text:

> Il2rg perturbation was present in 22 cell groups with 20-157 perturbed cells per group; each group had 0 genes at FDR<0.05; minimum genome-wide FDR=0.103637; the Il2rg target transcript had FDR=1.0 in all 22 measured on-target rows.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  | ✗ Other perturbation: Il2rg. |
| 2 | X | min_padj | = | 0.103637 | — | — | target | — | — | — |  | ✗ Other perturbation: Il2rg. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 12. Itpr1 / E007

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> Atp2a2 perturbation: 98 perturbed cells versus 23679 controls; Atp2a2 logFC -1.256, p=1.03e-23, FDR=1.78e-19; 187/17259 genes had FDR < 0.05, including Ddit3 logFC 1.604, FDR=2.06e-8; Xbp1 logFC 0.785, FDR=3.00e-7; Hspa5 logFC 0.749, FDR=1.95e-6; and Chac1 logFC 3.014, FDR=6.61e-8. The Itpr1-versus-Atp2a2 Wilcoxon-score correlation in this cell type was r=0.0165.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | logfc | = | -1.256 | 151 TH Prkcd Grin2c Glut | Atp2a2 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 2 | Y | pval | = | 1.03e-23 | 151 TH Prkcd Grin2c Glut | Atp2a2 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 3 | Y | padj | = | 1.78e-19 | 151 TH Prkcd Grin2c Glut | Atp2a2 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 4 | Y | n_sig | = | 187 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  | ✗ Other perturbation: Atp2a2. |
| 5 | Y | n_rows | = | 17259 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | — |  | ✗ Other perturbation: Atp2a2. |
| 6 | Y | logfc | = | 1.604 | 151 TH Prkcd Grin2c Glut | Ddit3 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 7 | Y | padj | = | 2.06e-8 | 151 TH Prkcd Grin2c Glut | Ddit3 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 8 | Y | logfc | = | 0.785 | 151 TH Prkcd Grin2c Glut | Xbp1 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 9 | Y | padj | = | 3.00e-7 | 151 TH Prkcd Grin2c Glut | Xbp1 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 10 | Y | logfc | = | 0.749 | 151 TH Prkcd Grin2c Glut | Hspa5 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 11 | Y | padj | = | 1.95e-6 | 151 TH Prkcd Grin2c Glut | Hspa5 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 12 | Y | logfc | = | 3.014 | 151 TH Prkcd Grin2c Glut | Chac1 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |
| 13 | Y | padj | = | 6.61e-8 | 151 TH Prkcd Grin2c Glut | Chac1 | gene | — | — | — |  | ✗ Other perturbation: Atp2a2. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 13. Mkx / E001

Row cell_type field: `empty`

Raw statistics text:

> 21 Mkx target-transcript rows; 24-111 perturbed cells per subclass versus 4,807-23,679 Non_target controls; Mkx logFC range -0.590 to +0.443, median -0.113; 14/21 logFC values were negative; minimum nominal p=0.010595 in 052 Pvalb Gaba; 0/21 target rows had FDR<0.05 and all had FDR=1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | min_pval | = | 0.010595 | 052 Pvalb Gaba | — | cell | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 14. Ncam1 / E003

Row cell_type field: `empty`

Raw statistics text:

> Across 371796 non-Ncam1 rows in the 22 Ncam1-perturbation strata, 0 rows reached FDR<0.05 and 0 reached FDR<0.10. The smallest non-target FDRs were Lancl1 in 191 MB P MY GABA at 0.289 and Micu3 in 005 L4-5 IT CTX Glut at 0.382.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 371796 | — | — | target | rows | exclude | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.10 |  | ✓ |
| 4 | Y | padj | = | 0.289 | 191 MB P MY GABA | Lancl1 | gene | — | — | — |  | ✓ |
| 5 | Y | padj | = | 0.382 | 005 L4-5 IT CTX Glut | Micu3 | gene | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 15. Neurod2 / E001

Row cell_type field: `empty`

Raw statistics text:

> Neurod2 was measured in all 23 Neurod2-perturbed cell classes; 21-260 perturbed cells versus 2019-23679 matched controls; no Neurod2 row had p<0.05; minimum target-row p=0.135, maximum |Wilcoxon score|=1.49, and every target-row FDR was 1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X≠ | min_pval | = | 0.135 | — | Neurod2 | gene | — | — | — | gene, scope | ✗ Restricted self-transcript minimum; neither displayed scope is valid. |
| 2 | Y≠ | min_pval | = | 0.135 | — | — | target | — | — | — | gene, scope | ✗ Restricted self-transcript minimum; neither displayed scope is valid. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 16. Pak3 / E002

Row cell_type field: `empty`

Raw statistics text:

> Pak3 transcript was measured in all 22 tested cell types; logFC was negative in 20/22; nominal p<0.05 in 4/22, led by 155 MB Glut logFC -0.631 p=3.39e-4 and 145 MH-LH TH Glut logFC -0.864 p=0.00291; every Pak3 self row had pvals_adj=1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | padj | = | 1.0 | 145 MH-LH TH Glut | Pak3 | gene | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 17. Pde1c / E001

Row cell_type field: `empty`

Raw statistics text:

> Pde1c DE row present in 22 cell types; 1,230 total matched Pde1c-perturbed cells, 21-155 per cell type; all Pde1c transcript adjusted p values = 1.0; smallest nominal on-target p = 0.062 in 308 CB GABA, logFC -0.696, score -1.866.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X≠ | min_pval | = | 0.062 | 308 CB GABA | Pde1c | gene | — | — | — | gene, scope | ✗ Restricted self-transcript minimum; neither displayed scope is valid. |
| 2 | Y≠ | min_pval | = | 0.062 | 308 CB GABA | — | cell | — | — | — | gene, scope | ✗ Restricted self-transcript minimum; neither displayed scope is valid. |
| 3 | X+Y | logfc | = | -0.696 | 308 CB GABA | Pde1c | gene | — | — | — |  | ✓ |
| 4 | X+Y | score | = | -1.866 | 308 CB GABA | Pde1c | gene | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 18. Pds5a / E005

Row cell_type field: `empty`

Raw statistics text:

> Among 106 Pds5a rows with nominal p<0.001, Exd2 was the only gene appearing in more than one cell class, in 017 CA3 CA2-FC DG Glut and 054 CNU-MGE GABA; no gene recurred in three or more p<0.001 rows.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X≠ | n_sig | = | 106 | 017 CA3 CA2-FC DG Glut | — | cell | rows | unstated | pval < 0.001 | cell_type, scope | ✓ |
| 2 | Y≠ | n_sig | = | 106 | — | — | target | rows | unstated | pval < 0.001 | cell_type, scope | ✗ First later label in the clause binds the count; keep row 1. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 19. Plcb1 / E004

Row cell_type field: `005 L4-5 IT CTX Glut`

Raw statistics text:

> 136 Itpr1 cells versus 15039 controls; Itpr1 score -5.1634, logFC -0.4351, nominal p=2.43e-7, FDR=0.00415; the Itpr1 self row was the only FDR<0.05 row for that perturbation in this cell type.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | score | = | -5.1634 | 005 L4-5 IT CTX Glut | Itpr1 | gene | — | — | — |  | ✗ Other perturbation: Itpr1. |
| 2 | Y | logfc | = | -0.4351 | 005 L4-5 IT CTX Glut | Itpr1 | gene | — | — | — |  | ✗ Other perturbation: Itpr1. |
| 3 | Y | pval | = | 2.43e-7 | 005 L4-5 IT CTX Glut | Itpr1 | gene | — | — | — |  | ✗ Other perturbation: Itpr1. |
| 4 | Y | padj | = | 0.00415 | 005 L4-5 IT CTX Glut | Itpr1 | gene | — | — | — |  | ✗ Other perturbation: Itpr1. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 20. Prdm10 / E003

Row cell_type field: `191 MB P MY GABA`

Raw statistics text:

> 111 perturbed cells versus 10309 controls; 34 FDR<0.05 genes: 6 up and 28 down; Cadm3 logFC -1.227 FDR 1.12e-20, Ptov1 -1.668 FDR 5.57e-20, Madd -1.326 FDR 3.45e-18, Prdm10 +0.981 FDR 0.00173.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 111 | 191 MB P MY GABA | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 10309 | 191 MB P MY GABA | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_sig | = | 34 | 191 MB P MY GABA | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 4 | X+Y | logfc | = | -1.227 | 191 MB P MY GABA | Cadm3 | gene | — | — | — |  | ✓ |
| 5 | X+Y | padj | = | 1.12e-20 | 191 MB P MY GABA | Cadm3 | gene | — | — | — |  | ✓ |
| 6 | X+Y | padj | = | 5.57e-20 | 191 MB P MY GABA | Ptov1 | gene | — | — | — |  | ✓ |
| 7 | X+Y | padj | = | 3.45e-18 | 191 MB P MY GABA | Madd | gene | — | — | — |  | ✓ |
| 8 | X+Y | padj | = | 0.00173 | 191 MB P MY GABA | Prdm10 | gene | — | — | — |  | ✓ |
| 9 | Y | logfc | = | -1.668 | 191 MB P MY GABA | Ptov1 | gene | — | — | — |  | ✓ |
| 10 | Y | logfc | = | -1.326 | 191 MB P MY GABA | Madd | gene | — | — | — |  | ✓ |
| 11 | Y | logfc | = | +0.981 | 191 MB P MY GABA | Prdm10 | gene | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 21. Ranbp2 / E010

Row cell_type field: `empty`

Raw statistics text:

> None of the measured canonical antiviral or inflammatory genes tested was FDR<0.05 in any of the 20 Ranbp2 cell types; best adjusted values were Stat2 FDR=0.966 and FDR=1.0 for Ifit3, Stat1, Ifit1, Isg15, Ifit2, Irf7, Ifitm3, Cxcl10, Ccl2, Il6, Tnf, Oas1a, and Ifnb1.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | min_padj | = | 0.966 | — | Stat2 | gene | — | — | — |  | ✗ Restricted-population summary; no standalone cell-bound value. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 22. Sall1 / E002

Row cell_type field: `empty`

Raw statistics text:

> 371,818 Sall1 DE tests across 22 cell types; 1 gene at FDR<0.05, 21/22 cell types with 0 FDR<0.05 genes; second-best FDR=0.102806.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | Y | n_sig | = | 1 | — | — | target | genes | unstated | padj < 0.05 |  | ✗ Same clause contains 21/22 cell-type recurrence. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 23. Six5 / E001

Row cell_type field: `empty`

Raw statistics text:

> Six5 transcript row present in 23/23 assayed cell types; 1,831 total Six5-perturbed cells; per-cell-type n_pert_matched=20-215 and n_ctrl_matched=2,019-23,679; Six5-row median |score|=0.168, maximum |score|=1.043, minimum nominal p=0.297, and pvals_adj=1.0 in every cell type.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X≠ | min_pval | = | 0.297 | — | — | target | — | — | — | gene, scope | ✗ Restricted self-transcript minimum; neither displayed scope is valid. |
| 2 | Y≠ | min_pval | = | 0.297 | — | Six5 | gene | — | — | — | gene, scope | ✗ Restricted self-transcript minimum; neither displayed scope is valid. |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 24. St3gal3 / E009

Row cell_type field: `empty`

Raw statistics text:

> Each listed marker was measured in all 22 St3gal3 tests and every pvals_adj was 1.0. The smallest nominal values were Ncam1 p 0.023 in 217 P MY Pineal Glut, Mbp p 0.0267 in 012 MEA LA CA1 DG Glut, St8sia4 p 0.0282 in 217 P MY Pineal Glut, and Bcan p 0.0475 in 053 Sst Gaba.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | pval | = | 0.023 | 217 P MY Pineal Glut | Ncam1 | gene | — | — | — |  | ✓ |
| 2 | X≠ | pval | = | 0.0267 | 012 MEA LA CA1 DG Glut | Mbp | gene | — | — | — | cell_type | ✗ Earlier clause label takes precedence; keep row 3. |
| 3 | Y≠ | pval | = | 0.0267 | 217 P MY Pineal Glut | Mbp | gene | — | — | — | cell_type | ✓ |
| 4 | X≠ | pval | = | 0.0282 | 217 P MY Pineal Glut | St8sia4 | gene | — | — | — | cell_type | ✗ Earlier clause label takes precedence; keep row 5. |
| 5 | Y≠ | pval | = | 0.0282 | 012 MEA LA CA1 DG Glut | St8sia4 | gene | — | — | — | cell_type | ✓ |
| 6 | X≠ | pval | = | 0.0475 | 053 Sst Gaba | Bcan | gene | — | — | — | cell_type | ✗ Earlier clause label takes precedence; keep row 7. |
| 7 | Y≠ | pval | = | 0.0475 | 217 P MY Pineal Glut | Bcan | gene | — | — | — | cell_type | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 25. Tbr1 / E005

Row cell_type field: `009 L2-3 IT PIR AON ENT Glut`

Raw statistics text:

> 108 perturbed cells versus 9240 controls; 0 genes with pvals_adj < 0.05 and 2 genes with pvals_adj < 0.10: Pnma8b logFC +0.595 q=0.0566; Ehbp1 +0.548 q=0.0959.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 108 | 009 L2-3 IT PIR AON ENT Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 9240 | 009 L2-3 IT PIR AON ENT Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | 009 L2-3 IT PIR AON ENT Glut | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 4 | X+Y | n_sig | = | 2 | 009 L2-3 IT PIR AON ENT Glut | — | cell | genes | unstated | padj < 0.10 |  | ✓ |
| 5 | X+Y | logfc | = | +0.595 | 009 L2-3 IT PIR AON ENT Glut | Pnma8b | gene | — | — | — |  | ✓ |
| 6 | X+Y | padj | = | 0.0566 | 009 L2-3 IT PIR AON ENT Glut | Pnma8b | gene | — | — | — |  | ✓ |
| 7 | X | logfc | = | +0.548 | 009 L2-3 IT PIR AON ENT Glut | Ehbp1 | gene | — | — | — |  | ✓ |
| 8 | X+Y | padj | = | 0.0959 | 009 L2-3 IT PIR AON ENT Glut | Ehbp1 | gene | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 26. Vps41 / E004

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 141 perturbed cells versus 20353 controls; Mcoln1 logFC 0.397 score 4.702 p=2.57e-6 FDR 0.0448; Vps41 logFC -0.562 p=4.08e-5 FDR 0.157; Cds1 0.460 p=3.50e-5; Atp6v0b 0.229 p=6.24e-5; Insig1 0.603 p=6.28e-5; Lamp2 0.410 p=7.26e-5; Msmo1 0.563 p=2.34e-4; Srebf2 0.382 p=8.92e-4.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 141 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 20353 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | logfc | = | 0.397 | 155 MB Glut | Mcoln1 | gene | — | — | — |  | ✓ |
| 4 | X+Y | score | = | 4.702 | 155 MB Glut | Mcoln1 | gene | — | — | — |  | ✓ |
| 5 | X+Y | pval | = | 2.57e-6 | 155 MB Glut | Mcoln1 | gene | — | — | — |  | ✓ |
| 6 | X+Y | padj | = | 0.0448 | 155 MB Glut | Mcoln1 | gene | — | — | — |  | ✓ |
| 7 | X+Y | logfc | = | -0.562 | 155 MB Glut | Vps41 | gene | — | — | — |  | ✓ |
| 8 | X+Y | pval | = | 4.08e-5 | 155 MB Glut | Vps41 | gene | — | — | — |  | ✓ |
| 9 | X+Y | padj | = | 0.157 | 155 MB Glut | Vps41 | gene | — | — | — |  | ✓ |
| 10 | X | logfc | = | 0.460 | 155 MB Glut | Cds1 | gene | — | — | — |  | ✓ |
| 11 | X+Y | pval | = | 3.50e-5 | 155 MB Glut | Cds1 | gene | — | — | — |  | ✓ |
| 12 | X | logfc | = | 0.229 | 155 MB Glut | Atp6v0b | gene | — | — | — |  | ✓ |
| 13 | X+Y | pval | = | 6.24e-5 | 155 MB Glut | Atp6v0b | gene | — | — | — |  | ✓ |
| 14 | X | logfc | = | 0.603 | 155 MB Glut | Insig1 | gene | — | — | — |  | ✓ |
| 15 | X+Y | pval | = | 6.28e-5 | 155 MB Glut | Insig1 | gene | — | — | — |  | ✓ |
| 16 | X | logfc | = | 0.410 | 155 MB Glut | Lamp2 | gene | — | — | — |  | ✓ |
| 17 | X+Y | pval | = | 7.26e-5 | 155 MB Glut | Lamp2 | gene | — | — | — |  | ✓ |
| 18 | X | logfc | = | 0.563 | 155 MB Glut | Msmo1 | gene | — | — | — |  | ✓ |
| 19 | X+Y | pval | = | 2.34e-4 | 155 MB Glut | Msmo1 | gene | — | — | — |  | ✓ |
| 20 | X | logfc | = | 0.382 | 155 MB Glut | Srebf2 | gene | — | — | — |  | ✓ |
| 21 | X+Y | pval | = | 8.92e-4 | 155 MB Glut | Srebf2 | gene | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

## 27. Zmynd8 / E005

Row cell_type field: `empty`

Raw statistics text:

> 18 of 22 Zmynd8-tested cell types had zero genes at FDR<0.05. Examples with over 100 perturbed cells but no FDR<0.05 genes were 052 Pvalb Gaba with 134 perturbed cells, 066 CNU-HYa HY GABA with 106, and 022 L5 ET CTX Glut with 104.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_sig | = | 0 | 052 Pvalb Gaba | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 2 | X+Y | n_pert | = | 134 | 052 Pvalb Gaba | — | cell | — | — | — |  | ✓ |
| 3 | X | n_pert | = | 106 | 066 CNU-HYa HY GABA | — | cell | — | — | — |  | ✓ |
| 4 | X | n_pert | = | 104 | 022 L5 ET CTX Glut | — | cell | — | — | — |  | ✓ |

**Missed by both:** None.

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

---

