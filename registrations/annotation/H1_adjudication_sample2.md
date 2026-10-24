# H1 annotation, sample 2: whole-field adjudication

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

53 fields.

## 1. Acox1 / E005

Row cell_type field: `308 CB GABA`

Raw statistics text:

> 32 Acox1-perturbed cells versus 8277 controls; Gtf2i logFC 0.446, score 4.303, p=1.69e-5, FDR=0.286; Orai2 logFC 0.875, p=7.38e-5, FDR=0.485; Acbd5 logFC -1.959, score -3.928, p=8.58e-5, FDR=0.485; Acox1 logFC -0.359, p=0.172, FDR=1; 11 genes had p<0.001 and none had FDR<0.05.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 32 | 308 CB GABA | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 8277 | 308 CB GABA | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | logfc | = | 0.446 | 308 CB GABA | Gtf2i | gene | — | — | — |  | ✓ |
| 4 | X+Y | score | = | 4.303 | 308 CB GABA | Gtf2i | gene | — | — | — |  | ✓ |
| 5 | X+Y | pval | = | 1.69e-5 | 308 CB GABA | Gtf2i | gene | — | — | — |  | ✓ |
| 6 | X+Y | padj | = | 0.286 | 308 CB GABA | Gtf2i | gene | — | — | — |  | ✓ |
| 7 | X+Y | logfc | = | 0.875 | 308 CB GABA | Orai2 | gene | — | — | — |  | ✓ |
| 8 | X+Y | pval | = | 7.38e-5 | 308 CB GABA | Orai2 | gene | — | — | — |  | ✓ |
| 9 | X+Y | padj | = | 0.485 | 308 CB GABA | Orai2 | gene | — | — | — |  | ✓ |
| 10 | X+Y | logfc | = | -1.959 | 308 CB GABA | Acbd5 | gene | — | — | — |  | ✓ |
| 11 | X+Y | score | = | -3.928 | 308 CB GABA | Acbd5 | gene | — | — | — |  | ✓ |
| 12 | X+Y | pval | = | 8.58e-5 | 308 CB GABA | Acbd5 | gene | — | — | — |  | ✓ |
| 13 | X+Y | padj | = | 0.485 | 308 CB GABA | Acbd5 | gene | — | — | — |  | ✓ |
| 14 | X+Y | logfc | = | -0.359 | 308 CB GABA | Acox1 | gene | — | — | — |  | ✓ |
| 15 | X+Y | pval | = | 0.172 | 308 CB GABA | Acox1 | gene | — | — | — |  | ✓ |
| 16 | X+Y | padj | = | 1 | 308 CB GABA | Acox1 | gene | — | — | — |  | ✓ |
| 17 | X+Y | n_sig | = | 11 | 308 CB GABA | — | cell | genes | unstated | pval < 0.001 |  | ✓ |
| 18 | X+Y | n_sig | = | 0 | 308 CB GABA | — | cell | genes | unstated | padj < 0.05 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 2. Ahrr / E002

Row cell_type field: `empty`

Raw statistics text:

> Ahrr transcript measured in 22 Ahrr-targeted cell classes; score range -0.380445 to 0.976431; absolute maximum score 0.976431 in 022 L5 ET CTX Glut; nominal p range 0.328851-0.987434; FDR=1.0 in all 22 rows.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | padj | = | 1.0 | 022 L5 ET CTX Glut | Ahrr | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 3. Atp6v1a / E002

Row cell_type field: `052 Pvalb Gaba`

Raw statistics text:

> 113 perturbed cells versus 13710 controls; Atp6v1a logFC -0.663, score -6.269, nominal p=3.64e-10, FDR=6.10e-6; 1/16762 genes FDR<0.05.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 113 | 052 Pvalb Gaba | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 13710 | 052 Pvalb Gaba | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | logfc | = | -0.663 | 052 Pvalb Gaba | Atp6v1a | gene | — | — | — |  | ✓ |
| 4 | X+Y | score | = | -6.269 | 052 Pvalb Gaba | Atp6v1a | gene | — | — | — |  | ✓ |
| 5 | X+Y | pval | = | 3.64e-10 | 052 Pvalb Gaba | Atp6v1a | gene | — | — | — |  | ✓ |
| 6 | X+Y | padj | = | 6.10e-6 | 052 Pvalb Gaba | Atp6v1a | gene | — | — | — |  | ✓ |
| 7 | X+Y | n_sig | = | 1 | 052 Pvalb Gaba | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 8 | X+Y | n_rows | = | 16762 | 052 Pvalb Gaba | — | cell | genes | unstated | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 4. Bmpr1b / E005

Row cell_type field: `052 Pvalb Gaba`

Raw statistics text:

> 78 perturbed cells versus 13710 controls; no gene reached FDR<0.05; the top row was Armcx1 with score -4.432, logFC -0.719, p=9.32e-6, FDR=0.156; the Bmpr1b transcript score was 0.038 with p=0.970 and FDR=1.000.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 78 | 052 Pvalb Gaba | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 13710 | 052 Pvalb Gaba | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | 052 Pvalb Gaba | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 4 | X+Y | score | = | -4.432 | 052 Pvalb Gaba | Armcx1 | gene | — | — | — |  | ✓ |
| 5 | X+Y | logfc | = | -0.719 | 052 Pvalb Gaba | Armcx1 | gene | — | — | — |  | ✓ |
| 6 | X+Y | pval | = | 9.32e-6 | 052 Pvalb Gaba | Armcx1 | gene | — | — | — |  | ✓ |
| 7 | X+Y | padj | = | 0.156 | 052 Pvalb Gaba | Armcx1 | gene | — | — | — |  | ✓ |
| 8 | X+Y | score | = | 0.038 | 052 Pvalb Gaba | Bmpr1b | gene | — | — | — |  | ✓ |
| 9 | X+Y | pval | = | 0.970 | 052 Pvalb Gaba | Bmpr1b | gene | — | — | — |  | ✓ |
| 10 | X+Y | padj | = | 1.000 | 052 Pvalb Gaba | Bmpr1b | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 5. Brd4 / E002

Row cell_type field: `empty`

Raw statistics text:

> FDR<0.05 genes by cell type: 151 TH Prkcd Grin2c Glut 311, 155 MB Glut 43, 191 MB P MY GABA 21, 052 Pvalb Gaba 3, 046 CTX-CGE GABA 1, 066 CNU-HYa HY GABA 1, and 0 in the other 15 Brd4-assayed cell types.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_sig | = | 311 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 2 | X+Y | n_sig | = | 43 | 155 MB Glut | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | n_sig | = | 21 | 191 MB P MY GABA | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 4 | X+Y | n_sig | = | 3 | 052 Pvalb Gaba | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 5 | X+Y | n_sig | = | 1 | 046 CTX-CGE GABA | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 6 | X+Y | n_sig | = | 1 | 066 CNU-HYa HY GABA | — | cell | genes | unstated | padj < 0.05 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 6. Cacng8 / E001

Row cell_type field: `empty`

Raw statistics text:

> 388046 Cacng8 DE rows across 23 group_name values and 17994 measured genes; 0 rows at FDR < 0.05, < 0.10, or < 0.20; minimum FDR 0.325; 131 rows had nominal p < 0.001.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_rows | = | 17994 | — | — | target | genes | unstated | — |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 4 | X+Y | min_padj | = | 0.325 | — | — | target | — | — | — |  | ✓ |
| 5 | X+Y | n_sig | = | 131 | — | — | target | rows | unstated | pval < 0.001 |  | ✓ |
| 6 | Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.10 |  | ✗ Single zero already used for the first threshold; no second count occurrence. |
| 7 | Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.20 |  | ✗ Single zero already used for the first threshold; no third count occurrence. |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 7. Cd80 / E004

Row cell_type field: `empty`

Raw statistics text:

> At nominal p < 0.001, 104 Cd80 rows represented 104 unique genes; among each cell type's top 50 positive genes, the most recurrent gene appeared in 3 of 21 cell types, and the same maximum recurrence of 3 of 21 was seen for top-50 absolute genes.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_sig | = | 104 | — | — | target | rows | unstated | pval < 0.001 |  | ✓ |
| 2 | X+Y | n_sig | = | 104 | — | — | target | genes | unstated | pval < 0.001 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 8. Cdin1 / E004

Row cell_type field: `009 L2-3 IT PIR AON ENT Glut`

Raw statistics text:

> 46 perturbed cells versus 9,240 controls; 22 genes had p<0.001 and 56 had |score|>3. Zfp638 logFC 0.645, score 4.390, p=1.13e-5, FDR=0.1089; Slit1 logFC -1.376, score -4.366, p=1.27e-5, FDR=0.1089; Vps9d1 logFC -1.021, FDR=0.693.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 46 | 009 L2-3 IT PIR AON ENT Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 9,240 | 009 L2-3 IT PIR AON ENT Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_sig | = | 22 | 009 L2-3 IT PIR AON ENT Glut | — | cell | genes | unstated | pval < 0.001 |  | ✓ |
| 4 | X+Y | logfc | = | 0.645 | 009 L2-3 IT PIR AON ENT Glut | Zfp638 | gene | — | — | — |  | ✓ |
| 5 | X+Y | score | = | 4.390 | 009 L2-3 IT PIR AON ENT Glut | Zfp638 | gene | — | — | — |  | ✓ |
| 6 | X+Y | pval | = | 1.13e-5 | 009 L2-3 IT PIR AON ENT Glut | Zfp638 | gene | — | — | — |  | ✓ |
| 7 | X+Y | padj | = | 0.1089 | 009 L2-3 IT PIR AON ENT Glut | Zfp638 | gene | — | — | — |  | ✓ |
| 8 | X+Y | logfc | = | -1.376 | 009 L2-3 IT PIR AON ENT Glut | Slit1 | gene | — | — | — |  | ✓ |
| 9 | X+Y | score | = | -4.366 | 009 L2-3 IT PIR AON ENT Glut | Slit1 | gene | — | — | — |  | ✓ |
| 10 | X+Y | pval | = | 1.27e-5 | 009 L2-3 IT PIR AON ENT Glut | Slit1 | gene | — | — | — |  | ✓ |
| 11 | X+Y | padj | = | 0.1089 | 009 L2-3 IT PIR AON ENT Glut | Slit1 | gene | — | — | — |  | ✓ |
| 12 | X+Y | logfc | = | -1.021 | 009 L2-3 IT PIR AON ENT Glut | Vps9d1 | gene | — | — | — |  | ✓ |
| 13 | X+Y | padj | = | 0.693 | 009 L2-3 IT PIR AON ENT Glut | Vps9d1 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 9. Celsr2 / E003

Row cell_type field: `empty`

Raw statistics text:

> Across 388,046 Celsr2 rows, exactly one non-Celsr2 row had FDR<0.05; in each of the 10 cell types with Celsr2 FDR<0.05, Celsr2 was the only FDR<0.05 gene.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388,046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X | n_sig | = | one | — | — | target | rows | exclude | padj < 0.05 |  | ✓ |
| 3 | Y | n_sig | = | 1 | — | — | target | rows | exclude | padj < 0.05 |  | ✗ Alternative of row 2; preserve the source value_text one. |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 10. Crlf1 / E002

Row cell_type field: `empty`

Raw statistics text:

> 0/371,818 Crlf1 rows at FDR < 0.05 and 0/371,818 at FDR < 0.10; 107/371,818 rows at nominal P < 0.001; the lowest adjusted P was 0.335.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 2 | X+Y | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.10 |  | ✓ |
| 4 | X+Y | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  | ✓ |
| 5 | X+Y | n_sig | = | 107 | — | — | target | rows | unstated | pval < 0.001 |  | ✓ |
| 6 | X+Y | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  | ✓ |
| 7 | X+Y | min_padj | = | 0.335 | — | — | target | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 11. Cyfip1 / E006

Row cell_type field: `empty`

Raw statistics text:

> Cyfip2 had six FDR-significant rows, all Cyfip2 self-rows, in 005 L4-5 IT CTX Glut, 066 CNU-HYa HY GABA, 145 MH-LH TH Glut, 151 TH Prkcd Grin2c Glut, 155 MB Glut, and 191 MB P MY GABA; self FDR range 4.39e-11 to 0.00453; 0 non-self FDR < 0.05 rows.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | n_sig | = | 0 | — | — | target | rows | exclude | padj < 0.05 |  | ✗ Other perturbation: Cyfip2 context. |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 12. Ehmt1 / E011

Row cell_type field: `308 CB GABA`

Raw statistics text:

> In 308 CB GABA, Pearson score correlations across 16,945 shared genes ranked Wdr26 as the strongest positive Ehmt1 signature neighbor among 2,022 comparators, r=0.358, and Eef2 as the strongest negative neighbor, r=-0.329. The same Ehmt1 308 CB GABA comparison had 69 perturbed cells, 8,277 controls, and 0 FDR<0.05 genes.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 69 | 308 CB GABA | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 8,277 | 308 CB GABA | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | 308 CB GABA | — | cell | genes | unstated | padj < 0.05 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 13. Etv6 / E004

Row cell_type field: `empty`

Raw statistics text:

> Across 388046 Etv6 differential-expression rows, 2 rows were FDR<0.05 and 3 rows were FDR<0.20; 21/23 cell types had zero FDR<0.05 genes.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 2 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | n_sig | = | 3 | — | — | target | rows | unstated | padj < 0.20 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 14. Gfap / E001

Row cell_type field: `empty`

Raw statistics text:

> 371,818 Gfap-target DE rows across 22 cell types; 16,428-17,443 measured genes per cell type; 22-133 perturbed cells per block, median 49.5; 3,465-23,679 Non_target controls.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 15. Glis2 / E003

Row cell_type field: `empty`

Raw statistics text:

> 388046 gene-by-cell-class tests for Glis2; FDR<0.05: 0; FDR<0.10: 0; minimum FDR=0.279; 119 tests had nominal p<0.001.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  | ✗ → unit=rows; all other fields unchanged. |
| 3 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.10 |  | ✗ → unit=rows; all other fields unchanged. |
| 4 | X+Y | min_padj | = | 0.279 | — | — | target | — | — | — |  | ✓ |
| 5 | X+Y | n_sig | = | 119 | — | — | target | rows | unstated | pval < 0.001 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 16. Gria3 / E005

Row cell_type field: `308 CB GABA`

Raw statistics text:

> 42 perturbed cells versus 8,277 controls; Gria3 logFC +0.033, p = 0.963, FDR = 1.0; 0/16,945 genes had FDR < 0.1. The top nominal genes were Grik4 logFC +0.876, FDR = 0.833; Cadm3 logFC -0.890, FDR = 0.833; and Tbx1 logFC +1.519, FDR = 0.833.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 42 | 308 CB GABA | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 8,277 | 308 CB GABA | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | logfc | = | +0.033 | 308 CB GABA | Gria3 | gene | — | — | — |  | ✓ |
| 4 | X+Y | pval | = | 0.963 | 308 CB GABA | Gria3 | gene | — | — | — |  | ✓ |
| 5 | X+Y | padj | = | 1.0 | 308 CB GABA | Gria3 | gene | — | — | — |  | ✓ |
| 6 | X+Y | n_sig | = | 0 | 308 CB GABA | — | cell | genes | unstated | padj < 0.1 |  | ✓ |
| 7 | X+Y | n_rows | = | 16,945 | 308 CB GABA | — | cell | genes | unstated | — |  | ✓ |
| 8 | X+Y | logfc | = | +0.876 | 308 CB GABA | Grik4 | gene | — | — | — |  | ✓ |
| 9 | X+Y | padj | = | 0.833 | 308 CB GABA | Grik4 | gene | — | — | — |  | ✓ |
| 10 | X+Y | logfc | = | -0.890 | 308 CB GABA | Cadm3 | gene | — | — | — |  | ✓ |
| 11 | X+Y | padj | = | 0.833 | 308 CB GABA | Cadm3 | gene | — | — | — |  | ✓ |
| 12 | X+Y | logfc | = | +1.519 | 308 CB GABA | Tbx1 | gene | — | — | — |  | ✓ |
| 13 | X+Y | padj | = | 0.833 | 308 CB GABA | Tbx1 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 17. Grik5 / E009

Row cell_type field: `001 L5-6 IT Glut`

Raw statistics text:

> Across 88 Grik1-Grik4 measured rows inside the 22 Grik5 contrasts, all had FDR=1.0. Strongest same-family nominal response was Grik4 in 001 L5-6 IT Glut: 47 perturbed cells, logFC 0.901642, score 3.952532, p=7.73e-05, FDR=1.0; the same contrast had Grik5 logFC -0.190989, p=0.194532, FDR=1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X≠ | padj | = | 1.0 | 001 L5-6 IT Glut | Grik5 | gene | — | — | — | gene | ✗ Aggregate multi-gene FDR; unresolved measured gene. |
| 2 | Y≠ | padj | = | 1.0 | 001 L5-6 IT Glut | Grik4 | gene | — | — | — | gene | ✗ Aggregate multi-gene FDR; unresolved measured gene. |
| 3 | X+Y | n_pert | = | 47 | 001 L5-6 IT Glut | — | cell | — | — | — |  | ✓ |
| 4 | X+Y | logfc | = | 0.901642 | 001 L5-6 IT Glut | Grik4 | gene | — | — | — |  | ✓ |
| 5 | X+Y | score | = | 3.952532 | 001 L5-6 IT Glut | Grik4 | gene | — | — | — |  | ✓ |
| 6 | X+Y | pval | = | 7.73e-05 | 001 L5-6 IT Glut | Grik4 | gene | — | — | — |  | ✓ |
| 7 | X≠ | padj | = | 1.0 | 001 L5-6 IT Glut | Grik4 | gene | — | — | — | gene | ✓ |
| 8 | Y≠ | padj | = | 1.0 | 001 L5-6 IT Glut | Grik5 | gene | — | — | — | gene | ✗ Shifted alternative; explicit Grik4 FDR is row 7 and Grik5 FDR is row 11. |
| 9 | X+Y | logfc | = | -0.190989 | 001 L5-6 IT Glut | Grik5 | gene | — | — | — |  | ✓ |
| 10 | X+Y | pval | = | 0.194532 | 001 L5-6 IT Glut | Grik5 | gene | — | — | — |  | ✓ |
| 11 | X | padj | = | 1.0 | 001 L5-6 IT Glut | Grik5 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 18. Htr6 / E002

Row cell_type field: `empty`

Raw statistics text:

> 388046 Htr6 DE rows across 23 classes; 0 rows with q<0.05; 1 row with q<0.1; 103 rows with nominal p<0.001 spanning 102 genes; only Sh3gl2 recurred at p<0.001 and flipped sign.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | n_sig | = | 1 | — | — | target | rows | unstated | padj < 0.1 |  | ✓ |
| 4 | X+Y | n_sig | = | 103 | — | — | target | rows | unstated | pval < 0.001 |  | ✓ |
| 5 | X+Y | n_sig | = | 102 | — | — | target | genes | unstated | pval < 0.001 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 19. Kcnj6 / E001

Row cell_type field: `empty`

Raw statistics text:

> 23 cell types; 388,046 Kcnj6 DE rows; n_pert_matched 20-226, median 78; 0 rows at FDR<0.05 and 0 rows at FDR<0.10; best transcriptome-wide FDR=0.254 in 005 L4-5 IT CTX Glut.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388,046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.10 |  | ✓ |
| 4 | X+Y | min_padj | = | 0.254 | 005 L4-5 IT CTX Glut | — | cell | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 20. Kdm4b / E004

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 258 perturbed cells versus 20,353 controls; 2 non-target genes had nominal p<0.001; 0 genes had pvals_adj <0.10; Kdm4b logFC -0.645 score -3.270 p=0.00108 q=1.0; Urgcp logFC 0.330 p=0.000535 q=1.0; Oprl1 logFC -0.347 p=0.000709 q=1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 258 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 20,353 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_sig | = | 2 | 155 MB Glut | — | cell | genes | exclude | pval < 0.001 |  | ✓ |
| 4 | X+Y | n_sig | = | 0 | 155 MB Glut | — | cell | genes | unstated | padj < 0.10 |  | ✓ |
| 5 | X+Y | logfc | = | -0.645 | 155 MB Glut | Kdm4b | gene | — | — | — |  | ✓ |
| 6 | X+Y | score | = | -3.270 | 155 MB Glut | Kdm4b | gene | — | — | — |  | ✓ |
| 7 | X+Y | pval | = | 0.00108 | 155 MB Glut | Kdm4b | gene | — | — | — |  | ✓ |
| 8 | X+Y | padj | = | 1.0 | 155 MB Glut | Kdm4b | gene | — | — | — |  | ✓ |
| 9 | X+Y | logfc | = | 0.330 | 155 MB Glut | Urgcp | gene | — | — | — |  | ✓ |
| 10 | X+Y | pval | = | 0.000535 | 155 MB Glut | Urgcp | gene | — | — | — |  | ✓ |
| 11 | X+Y | padj | = | 1.0 | 155 MB Glut | Urgcp | gene | — | — | — |  | ✓ |
| 12 | X+Y | logfc | = | -0.347 | 155 MB Glut | Oprl1 | gene | — | — | — |  | ✓ |
| 13 | X+Y | pval | = | 0.000709 | 155 MB Glut | Oprl1 | gene | — | — | — |  | ✓ |
| 14 | X+Y | padj | = | 1.0 | 155 MB Glut | Oprl1 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 21. Kdm5b / E002

Row cell_type field: `empty`

Raw statistics text:

> Strongest own-transcript rows: 022 L5 ET CTX Glut, 72 perturbed vs 8,644 controls, logFC -0.369, score -3.726, p=1.95e-4, rank 1/17,009 by p; 155 MB Glut, 164 vs 20,353, logFC -0.363, p=5.88e-4, rank 2/17,443; 052 Pvalb Gaba, 125 vs 13,710, logFC -0.392, p=8.89e-4, rank 4/16,762; 145 MH-LH TH Glut, 65 vs 6,961, logFC -0.597, p=0.00152, rank 8/16,707. All four had pvals_adj=1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 72 | 022 L5 ET CTX Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 8,644 | 022 L5 ET CTX Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_rows | = | 17,009 | 022 L5 ET CTX Glut | — | cell | genes | — | — |  | ✓ |
| 4 | X | n_pert | = | 164 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 5 | X | n_ctrl | = | 20,353 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 6 | X+Y | n_rows | = | 17,443 | 155 MB Glut | — | cell | genes | — | — |  | ✓ |
| 7 | X | n_pert | = | 125 | 052 Pvalb Gaba | — | cell | — | — | — |  | ✓ |
| 8 | X | n_ctrl | = | 13,710 | 052 Pvalb Gaba | — | cell | — | — | — |  | ✓ |
| 9 | X+Y | n_rows | = | 16,762 | 052 Pvalb Gaba | — | cell | genes | — | — |  | ✓ |
| 10 | X | n_pert | = | 65 | 145 MH-LH TH Glut | — | cell | — | — | — |  | ✓ |
| 11 | X | n_ctrl | = | 6,961 | 145 MH-LH TH Glut | — | cell | — | — | — |  | ✓ |
| 12 | X+Y | n_rows | = | 16,707 | 145 MH-LH TH Glut | — | cell | genes | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 22. Kdm6a / E002

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> 176 perturbed cells versus 23679 controls across 17259 genes; 1 gene FDR<0.05 and 17 genes p<0.001. Ntng1 logFC 0.1596, score 4.772, p=1.83e-6, FDR 0.0315; Nell1 logFC 0.2157, FDR 0.1218; Ptpn5 logFC -0.3177, FDR 0.1218; Cyp46a1 logFC -0.1606, FDR 0.1296.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 176 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 23679 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_rows | = | 17259 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | — |  | ✓ |
| 4 | X+Y | n_sig | = | 1 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 5 | X+Y | n_sig | = | 17 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | pval < 0.001 |  | ✓ |
| 6 | X+Y | logfc | = | 0.1596 | 151 TH Prkcd Grin2c Glut | Ntng1 | gene | — | — | — |  | ✓ |
| 7 | X+Y | score | = | 4.772 | 151 TH Prkcd Grin2c Glut | Ntng1 | gene | — | — | — |  | ✓ |
| 8 | X+Y | pval | = | 1.83e-6 | 151 TH Prkcd Grin2c Glut | Ntng1 | gene | — | — | — |  | ✓ |
| 9 | X+Y | padj | = | 0.0315 | 151 TH Prkcd Grin2c Glut | Ntng1 | gene | — | — | — |  | ✓ |
| 10 | X+Y | logfc | = | 0.2157 | 151 TH Prkcd Grin2c Glut | Nell1 | gene | — | — | — |  | ✓ |
| 11 | X+Y | padj | = | 0.1218 | 151 TH Prkcd Grin2c Glut | Nell1 | gene | — | — | — |  | ✓ |
| 12 | X+Y | logfc | = | -0.3177 | 151 TH Prkcd Grin2c Glut | Ptpn5 | gene | — | — | — |  | ✓ |
| 13 | X+Y | padj | = | 0.1218 | 151 TH Prkcd Grin2c Glut | Ptpn5 | gene | — | — | — |  | ✓ |
| 14 | X+Y | logfc | = | -0.1606 | 151 TH Prkcd Grin2c Glut | Cyp46a1 | gene | — | — | — |  | ✓ |
| 15 | X+Y | padj | = | 0.1296 | 151 TH Prkcd Grin2c Glut | Cyp46a1 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 23. Lpar6 / E002

Row cell_type field: `empty`

Raw statistics text:

> 355,046 Lpar6 gene-level tests across 21 cell groups; 0 genes at FDR<0.10 and 0 at FDR<0.05. The global minimum adjusted p value was 0.210 and the maximum absolute Wilcoxon score was 4.364; each cell type had only 1-9 genes with nominal p<0.001.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 355,046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.10 |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  | ✓ |
| 4 | X+Y | min_padj | = | 0.210 | — | — | target | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 24. Mecr / E005

Row cell_type field: `empty`

Raw statistics text:

> Across all 388046 Mecr rows, 1 row passed FDR <0.05; 89 rows passed p<0.001, representing 89 unique genes with no gene recurring at p<0.001 in more than one cell type.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 1 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | n_sig | = | 89 | — | — | target | rows | unstated | pval < 0.001 |  | ✓ |
| 4 | X+Y | n_sig | = | 89 | — | — | target | genes | unstated | pval < 0.001 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 25. Mest / E007

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> Mest: 164 perturbed/23,679 control cells, 0 FDR < 0.05 genes, best FDR 0.215. Ctnnb1: 171 perturbed/23,679 control cells, 383 FDR < 0.05 genes, minimum FDR 3.55e-25. The Mest-Ctnnb1 score correlation in this cell type was r = -0.003.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 164 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 23,679 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 4 | X+Y | min_padj | = | 0.215 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 26. Nefh / E005

Row cell_type field: `empty`

Raw statistics text:

> 371796 non-Nefh rows across 22 cell types; 0 rows had FDR < 0.05 or FDR < 0.10. Best non-target rows: Ap4e1 in 005 L4-5 IT CTX Glut logFC 0.697801 score 4.321463 p 1.549979e-05 FDR 0.265387; Lmbrd1 in 022 L5 ET CTX Glut logFC -0.389738 score -4.179902 p 2.916350e-05 FDR 0.496042; Actr3b in 052 Pvalb Gaba logFC -0.868764 score -4.005685 p 6.183804e-05 FDR 0.518265.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 371796 | — | — | target | rows | exclude | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | logfc | = | 0.697801 | 005 L4-5 IT CTX Glut | Ap4e1 | gene | — | — | — |  | ✓ |
| 4 | X+Y | score | = | 4.321463 | 005 L4-5 IT CTX Glut | Ap4e1 | gene | — | — | — |  | ✓ |
| 5 | X+Y | pval | = | 1.549979e-05 | 005 L4-5 IT CTX Glut | Ap4e1 | gene | — | — | — |  | ✓ |
| 6 | X+Y | padj | = | 0.265387 | 005 L4-5 IT CTX Glut | Ap4e1 | gene | — | — | — |  | ✓ |
| 7 | X+Y | logfc | = | -0.389738 | 022 L5 ET CTX Glut | Lmbrd1 | gene | — | — | — |  | ✓ |
| 8 | X+Y | score | = | -4.179902 | 022 L5 ET CTX Glut | Lmbrd1 | gene | — | — | — |  | ✓ |
| 9 | X+Y | pval | = | 2.916350e-05 | 022 L5 ET CTX Glut | Lmbrd1 | gene | — | — | — |  | ✓ |
| 10 | X+Y | padj | = | 0.496042 | 022 L5 ET CTX Glut | Lmbrd1 | gene | — | — | — |  | ✓ |
| 11 | X+Y | logfc | = | -0.868764 | 052 Pvalb Gaba | Actr3b | gene | — | — | — |  | ✓ |
| 12 | X+Y | score | = | -4.005685 | 052 Pvalb Gaba | Actr3b | gene | — | — | — |  | ✓ |
| 13 | X+Y | pval | = | 6.183804e-05 | 052 Pvalb Gaba | Actr3b | gene | — | — | — |  | ✓ |
| 14 | X+Y | padj | = | 0.518265 | 052 Pvalb Gaba | Actr3b | gene | — | — | — |  | ✓ |
| 15 | Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.10 |  | ✗ Single zero already used at the first threshold; do not reuse. |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 27. Nf1 / E002

Row cell_type field: `empty`

Raw statistics text:

> Nf1 transcript logFC was negative in 21 of 22 measured classes; six classes had nominal Nf1 p < 0.01, led by 052 Pvalb Gaba logFC -0.562 p=0.000255, 151 TH Prkcd Grin2c Glut logFC -0.352 p=0.001541, 054 CNU-MGE GABA logFC -0.530 p=0.004939, 110 CNU-HYa HY MM Glut logFC -0.507 p=0.006087, 155 MB Glut logFC -0.339 p=0.008285, and 053 Sst Gaba logFC -0.534 p=0.009938; no Nf1 target-transcript row had FDR < 0.05.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | pval | < | 0.01 | 052 Pvalb Gaba | Nf1 | gene | — | — | — |  | ✓ |
| 2 | X+Y | logfc | = | -0.562 | 052 Pvalb Gaba | Nf1 | gene | — | — | — |  | ✓ |
| 3 | X+Y | pval | = | 0.000255 | 052 Pvalb Gaba | Nf1 | gene | — | — | — |  | ✓ |
| 4 | X+Y | logfc | = | -0.352 | 151 TH Prkcd Grin2c Glut | Nf1 | gene | — | — | — |  | ✓ |
| 5 | X+Y | pval | = | 0.001541 | 151 TH Prkcd Grin2c Glut | Nf1 | gene | — | — | — |  | ✓ |
| 6 | X+Y | logfc | = | -0.530 | 054 CNU-MGE GABA | Nf1 | gene | — | — | — |  | ✓ |
| 7 | X+Y | pval | = | 0.004939 | 054 CNU-MGE GABA | Nf1 | gene | — | — | — |  | ✓ |
| 8 | X+Y | logfc | = | -0.507 | 110 CNU-HYa HY MM Glut | Nf1 | gene | — | — | — |  | ✓ |
| 9 | X+Y | pval | = | 0.006087 | 110 CNU-HYa HY MM Glut | Nf1 | gene | — | — | — |  | ✓ |
| 10 | X+Y | logfc | = | -0.339 | 155 MB Glut | Nf1 | gene | — | — | — |  | ✓ |
| 11 | X+Y | pval | = | 0.008285 | 155 MB Glut | Nf1 | gene | — | — | — |  | ✓ |
| 12 | X+Y | logfc | = | -0.534 | 053 Sst Gaba | Nf1 | gene | — | — | — |  | ✓ |
| 13 | X+Y | pval | = | 0.009938 | 053 Sst Gaba | Nf1 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 28. Nkx6-2 / E001

Row cell_type field: `empty`

Raw statistics text:

> Nkx6-2 had 371,818 DE rows across 22 group_name values; all 22 Nkx6-2 groups were annotated Glut or GABA; 215 MB Dopa was present in the parquet but had no Nkx6-2 rows.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| n_rows | = | 0 | 215 MB Dopa | — | cell | rows | unstated | — |

---

## 29. Nr1h2 / E001

Row cell_type field: `empty`

Raw statistics text:

> Nr1h2 transcript was present in 23/23 cell-type result tables; target-row logFC range -1.269 to +0.812; all target-row pvals_adj = 1.0; smallest nominal target p was 0.0493 in 053 Sst Gaba with logFC +0.812, and the largest negative target row was 017 CA3 CA2-FC DG Glut with logFC -1.269, p=0.0821, FDR=1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | logfc | = | +0.812 | 053 Sst Gaba | Nr1h2 | gene | — | — | — |  | ✓ |
| 2 | X+Y | pval | = | 0.0821 | 017 CA3 CA2-FC DG Glut | Nr1h2 | gene | — | — | — |  | ✓ |
| 3 | X+Y | padj | = | 1.0 | 017 CA3 CA2-FC DG Glut | Nr1h2 | gene | — | — | — |  | ✓ |
| 4 | Y | logfc | = | -1.269 | 017 CA3 CA2-FC DG Glut | Nr1h2 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 30. Pcsk2 / E008

Row cell_type field: `empty`

Raw statistics text:

> 151 TH Prkcd Grin2c Glut, 155 MB Glut, and 007 L2-3 IT CTX Glut each had Pcsk2 as the sole FDR<0.1 gene despite Pcsk2 FDR values of 1.19e-28, 2.49e-16, and 1.38e-6, respectively.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | padj | = | 1.38e-6 | 007 L2-3 IT CTX Glut | Pcsk2 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| padj | = | 1.19e-28 | 007 L2-3 IT CTX Glut | Pcsk2 | gene | — | — | — |
| padj | = | 2.49e-16 | 007 L2-3 IT CTX Glut | Pcsk2 | gene | — | — | — |

---

## 31. Peg3 / E004

Row cell_type field: `empty`

Raw statistics text:

> Among 371,796 non-Peg3 rows from Peg3 perturbation contrasts, exactly one row had pvals_adj<0.05: Gpx3 in 110 CNU-HYa HY MM Glut with score 4.614, logFC 1.228, p=3.95e-6, FDR 0.0339.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 371,796 | — | — | target | rows | exclude | — |  | ✓ |
| 2 | X | n_sig | = | 1 | — | — | target | rows | exclude | padj < 0.05 |  | ✗ Alternative of corrected row 7; preserve source value_text one. |
| 3 | X+Y | score | = | 4.614 | 110 CNU-HYa HY MM Glut | Gpx3 | gene | — | — | — |  | ✓ |
| 4 | X+Y | logfc | = | 1.228 | 110 CNU-HYa HY MM Glut | Gpx3 | gene | — | — | — |  | ✓ |
| 5 | X+Y | pval | = | 3.95e-6 | 110 CNU-HYa HY MM Glut | Gpx3 | gene | — | — | — |  | ✓ |
| 6 | X+Y | padj | = | 0.0339 | 110 CNU-HYa HY MM Glut | Gpx3 | gene | — | — | — |  | ✓ |
| 7 | Y | n_sig | = | one | — | — | target | rows | exclude | padj < 0.05 |  | ✗ → self=unstated; all other fields unchanged. |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 32. Pkd1 / E002

Row cell_type field: `empty`

Raw statistics text:

> 355,046 Pkd1 differential-expression rows across 21 cell types; 0 genes with FDR < 0.05; global minimum FDR 0.4746 for Slc25a23 in 046 CTX-CGE GABA; maximum absolute Wilcoxon score 4.182.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 355,046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | min_padj | = | 0.4746 | 046 CTX-CGE GABA | — | cell | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 33. Plxnd1 / E001

Row cell_type field: `empty`

Raw statistics text:

> 371,818 Plxnd1-perturbation rows across 22 cell types; 57-279 perturbed cells and 3,465-23,679 matched controls per cell type; 0 genes at FDR<=0.05 or FDR<=0.10, and 1/371,818 genes at FDR<=0.25.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj <= 0.05 |  | ✓ |
| 3 | X | n_sig | = | 0 | — | — | target | genes | unstated | padj <= 0.10 |  | ✗ Single zero already used at the first threshold; do not reuse. |
| 4 | X+Y | n_sig | = | 1 | — | — | target | genes | unstated | padj <= 0.25 |  | ✓ |
| 5 | X+Y | n_rows | = | 371,818 | — | — | target | genes | unstated | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 34. Pou6f1 / E004

Row cell_type field: `empty`

Raw statistics text:

> 151 TH Prkcd Grin2c Glut had 226 perturbed cells and no FDR < 0.05 rows; Pou6f1 logFC 0.037, p 0.986, FDR 1.0. 155 MB Glut had 209 perturbed cells and no FDR < 0.05 rows; Pou6f1 logFC 0.241, p 0.171, FDR 1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 226 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | 151 TH Prkcd Grin2c Glut | — | cell | rows | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | logfc | = | 0.037 | 151 TH Prkcd Grin2c Glut | Pou6f1 | gene | — | — | — |  | ✓ |
| 4 | X+Y | pval | = | 0.986 | 151 TH Prkcd Grin2c Glut | Pou6f1 | gene | — | — | — |  | ✓ |
| 5 | X+Y | padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Pou6f1 | gene | — | — | — |  | ✓ |
| 6 | X+Y | n_pert | = | 209 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 7 | X+Y | n_sig | = | 0 | 155 MB Glut | — | cell | rows | unstated | padj < 0.05 |  | ✓ |
| 8 | X+Y | logfc | = | 0.241 | 155 MB Glut | Pou6f1 | gene | — | — | — |  | ✓ |
| 9 | X+Y | pval | = | 0.171 | 155 MB Glut | Pou6f1 | gene | — | — | — |  | ✓ |
| 10 | X+Y | padj | = | 1.0 | 155 MB Glut | Pou6f1 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 35. Prdm5 / E002

Row cell_type field: `empty`

Raw statistics text:

> 388,046 Prdm5 differential-expression rows across 23 cell types; 16,228-17,443 ranked genes per cell type; 0 rows at FDR<0.1 and 0 rows at FDR<0.05; minimum FDR=0.466; 95 rows had nominal p<0.001.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388,046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.1 |  | ✓ |
| 3 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 4 | X+Y | min_padj | = | 0.466 | — | — | target | — | — | — |  | ✓ |
| 5 | X+Y | n_sig | = | 95 | — | — | target | rows | unstated | pval < 0.001 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 36. Rp9 / E003

Row cell_type field: `022 L5 ET CTX Glut`

Raw statistics text:

> 56 perturbed cells versus 8644 controls; Rp9 logFC -1.425, nominal p=8.50e-08, FDR=0.00145. Only 1 gene reached FDR<0.10; Bscl2 logFC -0.705, FDR=0.179; Uba5 logFC -0.815, FDR=0.621.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 56 | 022 L5 ET CTX Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 8644 | 022 L5 ET CTX Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | logfc | = | -1.425 | 022 L5 ET CTX Glut | Rp9 | gene | — | — | — |  | ✓ |
| 4 | X+Y | pval | = | 8.50e-08 | 022 L5 ET CTX Glut | Rp9 | gene | — | — | — |  | ✓ |
| 5 | X+Y | padj | = | 0.00145 | 022 L5 ET CTX Glut | Rp9 | gene | — | — | — |  | ✓ |
| 6 | X+Y | n_sig | = | 1 | 022 L5 ET CTX Glut | — | cell | genes | unstated | padj < 0.10 |  | ✓ |
| 7 | X+Y | logfc | = | -0.705 | 022 L5 ET CTX Glut | Bscl2 | gene | — | — | — |  | ✓ |
| 8 | X+Y | padj | = | 0.179 | 022 L5 ET CTX Glut | Bscl2 | gene | — | — | — |  | ✓ |
| 9 | X+Y | logfc | = | -0.815 | 022 L5 ET CTX Glut | Uba5 | gene | — | — | — |  | ✓ |
| 10 | X+Y | padj | = | 0.621 | 022 L5 ET CTX Glut | Uba5 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 37. Rpgr / E006

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 88 perturbed cells versus 20353 controls; Clasrp score -3.823156, logFC -0.289556, p = 0.000132, FDR = 1.0; Rpgr logFC 0.043665, p = 0.954430, FDR = 1.0; 11 rows had p < 0.001 and 0 had FDR < 0.10.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 88 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 20353 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | score | = | -3.823156 | 155 MB Glut | Clasrp | gene | — | — | — |  | ✓ |
| 4 | X+Y | logfc | = | -0.289556 | 155 MB Glut | Clasrp | gene | — | — | — |  | ✓ |
| 5 | X+Y | pval | = | 0.000132 | 155 MB Glut | Clasrp | gene | — | — | — |  | ✓ |
| 6 | X+Y | padj | = | 1.0 | 155 MB Glut | Clasrp | gene | — | — | — |  | ✓ |
| 7 | X+Y | logfc | = | 0.043665 | 155 MB Glut | Rpgr | gene | — | — | — |  | ✓ |
| 8 | X+Y | pval | = | 0.954430 | 155 MB Glut | Rpgr | gene | — | — | — |  | ✓ |
| 9 | X+Y | padj | = | 1.0 | 155 MB Glut | Rpgr | gene | — | — | — |  | ✓ |
| 10 | X+Y | n_sig | = | 11 | 155 MB Glut | — | cell | rows | unstated | pval < 0.001 |  | ✓ |
| 11 | X+Y | n_sig | = | 0 | 155 MB Glut | — | cell | rows | unstated | padj < 0.10 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 38. Satb2 / E002

Row cell_type field: `all 23 assayed cell types`

Raw statistics text:

> 388,046 Satb2 rows across 23 groups; 0 genes with P_adj<0.05. The smallest raw P values were Aatf in 145 MH-LH TH Glut, logFC 1.114, score 4.394, P=1.12e-5, P_adj=0.186; Ermp1 in 052 Pvalb Gaba, P=1.99e-5, P_adj=0.334; Itch in 027 NP-CT-L6b-OB Glut, P=2.24e-5, P_adj=0.374; Scrt1 in 001 L5-6 IT Glut, P=2.76e-5, P_adj=0.474.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388,046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | logfc | = | 1.114 | 145 MH-LH TH Glut | Aatf | gene | — | — | — |  | ✓ |
| 4 | X+Y | score | = | 4.394 | 145 MH-LH TH Glut | Aatf | gene | — | — | — |  | ✓ |
| 5 | X+Y | pval | = | 1.12e-5 | 145 MH-LH TH Glut | Aatf | gene | — | — | — |  | ✓ |
| 6 | X+Y | padj | = | 0.186 | 145 MH-LH TH Glut | Aatf | gene | — | — | — |  | ✓ |
| 7 | X+Y | pval | = | 1.99e-5 | 052 Pvalb Gaba | Ermp1 | gene | — | — | — |  | ✓ |
| 8 | X+Y | padj | = | 0.334 | 052 Pvalb Gaba | Ermp1 | gene | — | — | — |  | ✓ |
| 9 | X+Y | pval | = | 2.24e-5 | 027 NP-CT-L6b-OB Glut | Itch | gene | — | — | — |  | ✓ |
| 10 | X+Y | padj | = | 0.374 | 027 NP-CT-L6b-OB Glut | Itch | gene | — | — | — |  | ✓ |
| 11 | X+Y | pval | = | 2.76e-5 | 001 L5-6 IT Glut | Scrt1 | gene | — | — | — |  | ✓ |
| 12 | X+Y | padj | = | 0.474 | 001 L5-6 IT Glut | Scrt1 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 39. Six1 / E003

Row cell_type field: `empty`

Raw statistics text:

> 388,046 Six1 differential-expression rows; 0 rows with FDR<0.05; 12 rows with FDR<1.0; minimum FDR=0.304859; minimum nominal p=1.853e-5.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388,046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | n_sig | = | 12 | — | — | target | rows | unstated | padj < 1.0 |  | ✓ |
| 4 | X+Y | min_padj | = | 0.304859 | — | — | target | — | — | — |  | ✓ |
| 5 | X+Y | min_pval | = | 1.853e-5 | — | — | target | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 40. Smad4 / E002

Row cell_type field: `empty`

Raw statistics text:

> Smad4 transcript row present in 22/22 signatures; 18/22 logFC values were negative; median logFC -0.204; minimum logFC -0.804 in 008 L2-3 IT ENT PPP RSP Glut; minimum nominal p=0.00366 in 052 Pvalb Gaba; all Smad4 transcript FDR values were 1.0.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | padj | = | 1.0 | 052 Pvalb Gaba | Smad4 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| min_pval | = | 0.00366 | 052 Pvalb Gaba | — | cell | — | — | — |

---

## 41. Snx10 / E002

Row cell_type field: `empty`

Raw statistics text:

> 371,818 Snx10 differential-expression rows across 22 cell types; 0 genes at FDR<0.05 or FDR<0.10; minimum FDR=0.300872 and minimum nominal p=1.829e-5.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 371,818 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  | ✓ |
| 3 | X | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.10 |  | ✗ Single zero already used at the first threshold; do not reuse. |
| 4 | X+Y | min_padj | = | 0.300872 | — | — | target | — | — | — |  | ✓ |
| 5 | X+Y | min_pval | = | 1.829e-5 | — | — | target | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 42. Tbx2 / E002

Row cell_type field: `empty`

Raw statistics text:

> 388046 Tbx2 differential-expression rows across 23 cell types; 0 genes at FDR<0.05; best adjusted p=0.2176 for Gapvd1 in 007 L2-3 IT CTX Glut with score=-4.360, logFC=-0.584, nominal p=1.30e-5.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |  | ✓ |
| 3 | X+Y | min_padj | = | 0.2176 | 007 L2-3 IT CTX Glut | — | cell | — | — | — |  | ✓ |
| 4 | X+Y | score | = | -4.360 | 007 L2-3 IT CTX Glut | Gapvd1 | gene | — | — | — |  | ✓ |
| 5 | X+Y | logfc | = | -0.584 | 007 L2-3 IT CTX Glut | Gapvd1 | gene | — | — | — |  | ✓ |
| 6 | X+Y | pval | = | 1.30e-5 | 007 L2-3 IT CTX Glut | Gapvd1 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 43. Tef / E006

Row cell_type field: `012 MEA LA CA1 DG Glut`

Raw statistics text:

> 59 perturbed cells versus 7030 controls; Tef logFC -0.236 p=0.097 FDR=1.0; top row Rnpepl1 logFC -1.218 p=5.99e-6 FDR=0.101; zero genes with FDR<0.05.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 59 | 012 MEA LA CA1 DG Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 7030 | 012 MEA LA CA1 DG Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | logfc | = | -0.236 | 012 MEA LA CA1 DG Glut | Tef | gene | — | — | — |  | ✓ |
| 4 | X+Y | pval | = | 0.097 | 012 MEA LA CA1 DG Glut | Tef | gene | — | — | — |  | ✓ |
| 5 | X+Y | padj | = | 1.0 | 012 MEA LA CA1 DG Glut | Tef | gene | — | — | — |  | ✓ |
| 6 | X+Y | logfc | = | -1.218 | 012 MEA LA CA1 DG Glut | Rnpepl1 | gene | — | — | — |  | ✓ |
| 7 | X+Y | pval | = | 5.99e-6 | 012 MEA LA CA1 DG Glut | Rnpepl1 | gene | — | — | — |  | ✓ |
| 8 | X+Y | padj | = | 0.101 | 012 MEA LA CA1 DG Glut | Rnpepl1 | gene | — | — | — |  | ✓ |
| 9 | X | n_sig | = | zero | 012 MEA LA CA1 DG Glut | — | cell | genes | unstated | padj < 0.05 |  | ✗ Alternative of row 10; normalize a zero count to 0. |
| 10 | Y | n_sig | = | 0 | 012 MEA LA CA1 DG Glut | — | cell | genes | unstated | padj < 0.05 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 44. Tpi1 / E008

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> 260 Pgk1-perturbed cells versus 23679 controls; Pgk1 logFC -1.441, FDR=4.43e-32; Pnisr logFC -0.227, FDR=7.00e-11; Rsrp1 logFC -0.217, FDR=5.73e-10; Ogt logFC -0.146, FDR=5.00e-04; 22 genes total had FDR<0.05.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X | logfc | = | -1.441 | 151 TH Prkcd Grin2c Glut | Pgk1 | gene | — | — | — |  | ✗ Other perturbation: Pgk1 context. |
| 2 | X | padj | = | 4.43e-32 | 151 TH Prkcd Grin2c Glut | Pgk1 | gene | — | — | — |  | ✗ Other perturbation: Pgk1 context. |
| 3 | X | logfc | = | -0.227 | 151 TH Prkcd Grin2c Glut | Pnisr | gene | — | — | — |  | ✗ Other perturbation: Pgk1 context. |
| 4 | X | padj | = | 7.00e-11 | 151 TH Prkcd Grin2c Glut | Pnisr | gene | — | — | — |  | ✗ Other perturbation: Pgk1 context. |
| 5 | X | logfc | = | -0.217 | 151 TH Prkcd Grin2c Glut | Rsrp1 | gene | — | — | — |  | ✗ Other perturbation: Pgk1 context. |
| 6 | X | padj | = | 5.73e-10 | 151 TH Prkcd Grin2c Glut | Rsrp1 | gene | — | — | — |  | ✗ Other perturbation: Pgk1 context. |
| 7 | X | logfc | = | -0.146 | 151 TH Prkcd Grin2c Glut | Ogt | gene | — | — | — |  | ✗ Other perturbation: Pgk1 context. |
| 8 | X | padj | = | 5.00e-04 | 151 TH Prkcd Grin2c Glut | Ogt | gene | — | — | — |  | ✗ Other perturbation: Pgk1 context. |
| 9 | X | n_sig | = | 22 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  | ✗ Other perturbation: Pgk1 context. |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 45. Trpm3 / E006

Row cell_type field: `308 CB GABA`

Raw statistics text:

> 57 perturbed cells versus 8,277 controls; 16,945 genes tested; 0 genes with FDR < 0.05; min FDR 1.0; top nominal up Fam118a score 3.7896, logFC 0.9074, p 1.51e-4; top nominal down Pogz score -3.7858, logFC -0.9430, p 1.53e-4.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 57 | 308 CB GABA | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 8,277 | 308 CB GABA | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_rows | = | 16,945 | 308 CB GABA | — | cell | genes | unstated | — |  | ✓ |
| 4 | X+Y | n_sig | = | 0 | 308 CB GABA | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 5 | X+Y | min_padj | = | 1.0 | 308 CB GABA | — | cell | — | — | — |  | ✓ |
| 6 | X+Y | score | = | 3.7896 | 308 CB GABA | Fam118a | gene | — | — | — |  | ✓ |
| 7 | X+Y | logfc | = | 0.9074 | 308 CB GABA | Fam118a | gene | — | — | — |  | ✓ |
| 8 | X+Y | pval | = | 1.51e-4 | 308 CB GABA | Fam118a | gene | — | — | — |  | ✓ |
| 9 | X+Y | score | = | -3.7858 | 308 CB GABA | Pogz | gene | — | — | — |  | ✓ |
| 10 | X+Y | logfc | = | -0.9430 | 308 CB GABA | Pogz | gene | — | — | — |  | ✓ |
| 11 | X+Y | pval | = | 1.53e-4 | 308 CB GABA | Pogz | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 46. Tspan12 / E002

Row cell_type field: `empty`

Raw statistics text:

> 388,046 Wilcoxon tests across 23 cell types; 1 gene at FDR<=0.05, 2 at FDR<=0.10, 3 at FDR<=0.20; 110 rows at nominal p<=0.001 and all 110 were distinct genes.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 388,046 | — | — | target | rows | unstated | — |  | ✓ |
| 2 | X+Y | n_sig | = | 1 | — | — | target | genes | unstated | padj <= 0.05 |  | ✓ |
| 3 | X+Y | n_sig | = | 2 | — | — | target | genes | unstated | padj <= 0.10 |  | ✓ |
| 4 | X+Y | n_sig | = | 3 | — | — | target | genes | unstated | padj <= 0.20 |  | ✓ |
| 5 | X+Y | n_sig | = | 110 | — | — | target | rows | unstated | pval <= 0.001 |  | ✓ |
| 6 | X+Y | n_sig | = | 110 | — | — | target | genes | unstated | pval <= 0.001 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 47. Tuba1a / E007

Row cell_type field: `empty`

Raw statistics text:

> Across all 21 Tuba1a contrasts, 16 rows reached FDR<0.05 and all 16 were Tuba1a or Tuba/Tubb genes; at FDR<0.10, the only added non-tubulin row was Copb1 in 151 TH Prkcd Grin2c Glut, logFC 0.478, FDR 0.0961.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_sig | = | 16 | — | — | target | rows | unstated | padj < 0.05 |  | ✓ |
| 2 | X+Y | logfc | = | 0.478 | 151 TH Prkcd Grin2c Glut | Copb1 | gene | — | — | — |  | ✓ |
| 3 | X+Y | padj | = | 0.0961 | 151 TH Prkcd Grin2c Glut | Copb1 | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 48. Ubr1 / E001

Row cell_type field: `empty`

Raw statistics text:

> 19 Ubr1 perturbation/cell-type signatures; 321225 gene-level Wilcoxon rows; 20-65 matched Ubr1-perturbed cells per cell type, median 23 and IQR 22-29, versus 5622-23679 matched non-targeting controls.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_rows | = | 321225 | — | — | target | rows | unstated | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 49. Uchl1 / E001

Row cell_type field: `empty`

Raw statistics text:

> 371818 Uchl1 rows across 22 of 23 group_name classes; Uchl1 target logFC was negative in 22/22 classes, nominal target p<0.005 in 22/22, and target FDR<0.05 in 13/22.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | n_rows | = | 371818 | — | — | target | rows | unstated | — |  | ✗ Total occurs inside an excluded recurrence clause. |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 50. Vps37a / E003

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 58 perturbed cells versus 20353 controls; 138 FDR<0.05 genes. Top examples: Rhoq logFC 1.678 FDR 8.59e-06; Ly6h logFC -1.283 FDR 2.36e-04; Atp6v0b logFC 0.541 FDR 3.84e-04; Ddit3 logFC 1.759 FDR 6.43e-04; Tnfrsf12a logFC 2.451 FDR 0.00107; Kifc2 logFC -0.777 FDR 0.00107; Jun logFC 1.705 FDR 0.00373; Atp6v1h logFC 0.848 FDR 0.00918.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 58 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 20353 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_sig | = | 138 | 155 MB Glut | — | cell | genes | unstated | padj < 0.05 |  | ✓ |
| 4 | X+Y | logfc | = | 1.678 | 155 MB Glut | Rhoq | gene | — | — | — |  | ✓ |
| 5 | X+Y | padj | = | 8.59e-06 | 155 MB Glut | Rhoq | gene | — | — | — |  | ✓ |
| 6 | X+Y | logfc | = | -1.283 | 155 MB Glut | Ly6h | gene | — | — | — |  | ✓ |
| 7 | X+Y | padj | = | 2.36e-04 | 155 MB Glut | Ly6h | gene | — | — | — |  | ✓ |
| 8 | X+Y | logfc | = | 0.541 | 155 MB Glut | Atp6v0b | gene | — | — | — |  | ✓ |
| 9 | X+Y | padj | = | 3.84e-04 | 155 MB Glut | Atp6v0b | gene | — | — | — |  | ✓ |
| 10 | X+Y | logfc | = | 1.759 | 155 MB Glut | Ddit3 | gene | — | — | — |  | ✓ |
| 11 | X+Y | padj | = | 6.43e-04 | 155 MB Glut | Ddit3 | gene | — | — | — |  | ✓ |
| 12 | X+Y | logfc | = | 2.451 | 155 MB Glut | Tnfrsf12a | gene | — | — | — |  | ✓ |
| 13 | X+Y | padj | = | 0.00107 | 155 MB Glut | Tnfrsf12a | gene | — | — | — |  | ✓ |
| 14 | X+Y | logfc | = | -0.777 | 155 MB Glut | Kifc2 | gene | — | — | — |  | ✓ |
| 15 | X+Y | padj | = | 0.00107 | 155 MB Glut | Kifc2 | gene | — | — | — |  | ✓ |
| 16 | X+Y | logfc | = | 1.705 | 155 MB Glut | Jun | gene | — | — | — |  | ✓ |
| 17 | X+Y | padj | = | 0.00373 | 155 MB Glut | Jun | gene | — | — | — |  | ✓ |
| 18 | X+Y | logfc | = | 0.848 | 155 MB Glut | Atp6v1h | gene | — | — | — |  | ✓ |
| 19 | X+Y | padj | = | 0.00918 | 155 MB Glut | Atp6v1h | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 51. Zfat / E003

Row cell_type field: `155 MB Glut`

Raw statistics text:

> 174 perturbed cells versus 20353 controls; 17443 genes tested; only 2 genes with FDR<0.1: Zfat logFC 0.971 score 4.933 p=8.08e-07 FDR=0.0141; D6Wsu163e logFC -0.931 score -4.595 p=4.33e-06 FDR=0.0378.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 174 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 2 | X+Y | n_ctrl | = | 20353 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 3 | X+Y | n_rows | = | 17443 | 155 MB Glut | — | cell | genes | unstated | — |  | ✓ |
| 4 | X+Y | n_sig | = | 2 | 155 MB Glut | — | cell | genes | unstated | padj < 0.1 |  | ✓ |
| 5 | X+Y | logfc | = | 0.971 | 155 MB Glut | Zfat | gene | — | — | — |  | ✓ |
| 6 | X+Y | score | = | 4.933 | 155 MB Glut | Zfat | gene | — | — | — |  | ✓ |
| 7 | X+Y | pval | = | 8.08e-07 | 155 MB Glut | Zfat | gene | — | — | — |  | ✓ |
| 8 | X+Y | padj | = | 0.0141 | 155 MB Glut | Zfat | gene | — | — | — |  | ✓ |
| 9 | X+Y | logfc | = | -0.931 | 155 MB Glut | D6Wsu163e | gene | — | — | — |  | ✓ |
| 10 | X+Y | score | = | -4.595 | 155 MB Glut | D6Wsu163e | gene | — | — | — |  | ✓ |
| 11 | X+Y | pval | = | 4.33e-06 | 155 MB Glut | D6Wsu163e | gene | — | — | — |  | ✓ |
| 12 | X+Y | padj | = | 0.0378 | 155 MB Glut | D6Wsu163e | gene | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 52. Zfp322a / E003

Row cell_type field: `empty`

Raw statistics text:

> High-count examples all had 0 FDR-significant genes: 151 TH Prkcd Grin2c Glut, 215 perturbed cells; 155 MB Glut, 183; 005 L4-5 IT CTX Glut, 141; 052 Pvalb Gaba, 121; 009 L2-3 IT PIR AON ENT Glut, 99. The best rows were Mib2 in 005 with score 4.245, logFC 0.388, p = 2.2e-5, FDR = 0.373635 and Senp2 in 052 with score 4.221, logFC 0.556, p = 2.4e-5, FDR = 0.407478.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_pert | = | 215 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — |  | ✓ |
| 2 | Y | n_pert | = | 183 | 155 MB Glut | — | cell | — | — | — |  | ✓ |
| 3 | Y | n_pert | = | 141 | 005 L4-5 IT CTX Glut | — | cell | — | — | — |  | ✓ |
| 4 | Y | n_pert | = | 121 | 052 Pvalb Gaba | — | cell | — | — | — |  | ✓ |
| 5 | Y | n_pert | = | 99 | 009 L2-3 IT PIR AON ENT Glut | — | cell | — | — | — |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

## 53. Zic1 / E005

Row cell_type field: `empty`

Raw statistics text:

> Across 23 Zic1 contrasts, FDR<0.05 occurred for 2 genes total, both in 151 TH Prkcd Grin2c Glut; 151 had 29 genes with p<0.001, while every other cell group had 0 FDR<0.05 genes and 1 to 9 genes with p<0.001; the minimum non-151 FDR was 0.494.

| # | source | quantity | rel | value | cell type | gene | scope | unit | self | threshold | differs | Ruling |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | X+Y | n_sig | = | 2 | 151 TH Prkcd Grin2c Glut | — | cell | genes | unstated | padj < 0.05 |  | ✓ |

**Missed by both** (add one row per in-scope assertion neither version lists):

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|

None.

---

