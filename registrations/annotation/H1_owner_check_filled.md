

---

## 1. Akap9 / E010

Row cell_type field: `empty`

Raw statistics text:

> In related contrasts, Ppp2r1a yielded 3,147 FDR<0.05 rows across cell types, including 1,292 in 151 TH Prkcd Grin2c Glut and 476 in 155 MB Glut; Ppp2r1a target FDR was 2.28e-44 in 151 TH and 5.34e-32 in 155 MB Glut; Prkaca target FDR was 7.34e-24 in 191 MB P MY GABA and 1.25e-22 in 155 MB Glut.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓ Boş anotasyon doğru: tüm sayılar açıkça Ppp2r1a ve Prkaca perturbasyonlarına ait.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 2. Amfr / E003

Row cell_type field: `191 MB P MY GABA`

Raw statistics text:

> 49 perturbed cells versus 10309 controls; Amfr score -4.509, logFC -1.215, p=6.50e-06, FDR=0.111.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 49 | 191 MB P MY GABA | — | cell | — | — | — | ✓ |
| 2 | n_ctrl | = | 10309 | 191 MB P MY GABA | — | cell | — | — | — | ✓ |
| 3 | score | = | -4.509 | 191 MB P MY GABA | Amfr | gene | — | — | — | ✓ |
| 4 | logfc | = | -1.215 | 191 MB P MY GABA | Amfr | gene | — | — | — | ✓ |
| 5 | pval | = | 6.50e-06 | 191 MB P MY GABA | Amfr | gene | — | — | — | ✓ |
| 6 | padj | = | 0.111 | 191 MB P MY GABA | Amfr | gene | — | — | — | ✓ |

**Kontrol:** ✓ Altı satırın tüm alanları doğru; hücre tipi satır alanından alınır.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 3. Arih1 / E008

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> In 151 TH Prkcd Grin2c Glut, Arih1 and Cul3 perturbations shared 3 of their top 50 absolute-score genes, 11 of their top 100, and 27 of their top 200; 26/27 of the top-200 overlaps had the same score sign. Cul3 had 1 FDR<0.05 gene in this cell type; the Cul3 self-transcript had logFC -0.408, p=0.00133, FDR 0.656.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓* Cul3 perturbasyonu kapsam dışı. Top-k örtüşme ve işaret uyumunun dışlanması kod kitabına bağlı.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 4. Atf6 / E006

Row cell_type field: `empty`

Raw statistics text:

> Manf perturbation produced FDR<0.05 Hspa5 up-regulation in 8 cell types. Examples: 155 MB Glut, 192 perturbed cells: Hspa5 logFC +0.879/FDR=2.43e-14, Dnajb9 +0.779/FDR=9.41e-5, Hyou1 +0.506/FDR=1.95e-4, Pdia6 +0.533/FDR=2.48e-4, Sdf2l1 +1.379/FDR=3.73e-5; 054 CNU-MGE GABA, 81 perturbed cells: Hspa5 +0.818/FDR=1.77e-6, Hyou1 +0.724/FDR=0.00234, Ppib +0.470/FDR=0.0166, Rpn1 +0.506/FDR=0.0373.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 192 | 155 MB Glut | — | cell | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 2 | logfc | = | +0.879 | 155 MB Glut | Hspa5 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 3 | padj | = | 2.43e-14 | 155 MB Glut | Hspa5 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 4 | logfc | = | +0.779 | 155 MB Glut | Dnajb9 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 5 | padj | = | 9.41e-5 | 155 MB Glut | Dnajb9 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 6 | logfc | = | +0.506 | 155 MB Glut | Hyou1 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 7 | padj | = | 1.95e-4 | 155 MB Glut | Hyou1 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 8 | logfc | = | +0.533 | 155 MB Glut | Pdia6 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 9 | padj | = | 2.48e-4 | 155 MB Glut | Pdia6 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 10 | logfc | = | +1.379 | 155 MB Glut | Sdf2l1 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 11 | padj | = | 3.73e-5 | 155 MB Glut | Sdf2l1 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 12 | n_pert | = | 81 | 054 CNU-MGE GABA | — | cell | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 13 | logfc | = | +0.818 | 054 CNU-MGE GABA | Hspa5 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 14 | padj | = | 1.77e-6 | 054 CNU-MGE GABA | Hspa5 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 15 | logfc | = | +0.724 | 054 CNU-MGE GABA | Hyou1 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 16 | padj | = | 0.00234 | 054 CNU-MGE GABA | Hyou1 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 17 | logfc | = | +0.470 | 054 CNU-MGE GABA | Ppib | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 18 | padj | = | 0.0166 | 054 CNU-MGE GABA | Ppib | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 19 | logfc | = | +0.506 | 054 CNU-MGE GABA | Rpn1 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |
| 20 | padj | = | 0.0373 | 054 CNU-MGE GABA | Rpn1 | gene | — | — | — | ✗ Kapsam dışı: Manf perturbasyonu; satırı kaldır. |

**Kontrol:** ✗ 20 satırın sayıları doğru kopyalanmış olsa da tümü açıkça Manf perturbasyonuna ait. Atf6 anotasyonundan bu 20 satır kaldırılmalı.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 5. Atp2b2 / E007

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> Atp2a2 perturbation: n=98, Atp2a2 logFC -1.256338 FDR 1.780900e-19 and 186 non-target FDR genes in this cell type, including Hspa5 +0.749096 FDR 1.953462e-06, Ddit3 +1.603674 FDR 2.058184e-08, Xbp1 +0.785159 FDR 3.004919e-07, Chac1 +3.013680 FDR 6.612620e-08, Asns +0.866488 FDR 3.080109e-06, Slc7a5 +1.975921 FDR 0.001754, Sesn2 +2.390634 FDR 0.000326, and Trib3 +3.684104 FDR 0.037283. All listed genes had pvals_adj = 1.0 after Atp2b2 knockdown in the same cell type.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✗ Son cümle Atp2b2 knockdown bağlamına dönüyor ve listelenen genler için pvals_adj=1.0 veriyor. Atp2a2 perturbasyonunun önceki sayıları kapsam dışı.

**Missed:** 

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Hspa5 | gene | — | — | — |
| padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Ddit3 | gene | — | — | — |
| padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Xbp1 | gene | — | — | — |
| padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Chac1 | gene | — | — | — |
| padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Asns | gene | — | — | — |
| padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Slc7a5 | gene | — | — | — |
| padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Sesn2 | gene | — | — | — |
| padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Trib3 | gene | — | — | — |

**Belirsiz ek aday:** Aynı hücre tipinde Atp2a2 padj=1.0; yalnızca All listed genes ifadesi ilk adı geçen Atp2a2 genini de kapsıyorsa. Sekiz açık listedeki genin sayısına dahil edilmedi.

---


## 6. Atp6v1b2 / E002

Row cell_type field: `052 Pvalb Gaba`

Raw statistics text:

> 64 perturbed versus 13,710 control cells; 9 genes at FDR<0.05. Atp6v1b2 logFC -0.694, score -5.885, p=3.98e-09, FDR=6.67e-05; Hcn3 logFC 0.994, FDR=0.00273; Dusp1 logFC 1.139, FDR=0.0114; Serpini1 logFC -0.727, FDR=0.0323; Scg2 logFC 0.861, FDR=0.0340; Gadd45g logFC 1.871, FDR=0.0402; Slc6a17 logFC 0.473, FDR=0.0490; Ptprn logFC 0.545, FDR=0.0490; Lpcat1 logFC 1.007, FDR=0.0490.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 64 | 052 Pvalb Gaba | — | cell | — | — | — | ✓ |
| 2 | n_ctrl | = | 13,710 | 052 Pvalb Gaba | — | cell | — | — | — | ✓ |
| 3 | n_sig | = | 9 | 052 Pvalb Gaba | — | cell | genes | unstated | padj < 0.05 | ✓ |
| 4 | logfc | = | -0.694 | 052 Pvalb Gaba | Atp6v1b2 | gene | — | — | — | ✓ |
| 5 | score | = | -5.885 | 052 Pvalb Gaba | Atp6v1b2 | gene | — | — | — | ✓ |
| 6 | pval | = | 3.98e-09 | 052 Pvalb Gaba | Atp6v1b2 | gene | — | — | — | ✓ |
| 7 | padj | = | 6.67e-05 | 052 Pvalb Gaba | Atp6v1b2 | gene | — | — | — | ✓ |
| 8 | logfc | = | 0.994 | 052 Pvalb Gaba | Hcn3 | gene | — | — | — | ✓ |
| 9 | padj | = | 0.00273 | 052 Pvalb Gaba | Hcn3 | gene | — | — | — | ✓ |
| 10 | logfc | = | 1.139 | 052 Pvalb Gaba | Dusp1 | gene | — | — | — | ✓ |
| 11 | padj | = | 0.0114 | 052 Pvalb Gaba | Dusp1 | gene | — | — | — | ✓ |
| 12 | logfc | = | -0.727 | 052 Pvalb Gaba | Serpini1 | gene | — | — | — | ✓ |
| 13 | padj | = | 0.0323 | 052 Pvalb Gaba | Serpini1 | gene | — | — | — | ✓ |
| 14 | logfc | = | 0.861 | 052 Pvalb Gaba | Scg2 | gene | — | — | — | ✓ |
| 15 | padj | = | 0.0340 | 052 Pvalb Gaba | Scg2 | gene | — | — | — | ✓ |
| 16 | logfc | = | 1.871 | 052 Pvalb Gaba | Gadd45g | gene | — | — | — | ✓ |
| 17 | padj | = | 0.0402 | 052 Pvalb Gaba | Gadd45g | gene | — | — | — | ✓ |
| 18 | logfc | = | 0.473 | 052 Pvalb Gaba | Slc6a17 | gene | — | — | — | ✓ |
| 19 | padj | = | 0.0490 | 052 Pvalb Gaba | Slc6a17 | gene | — | — | — | ✓ |
| 20 | logfc | = | 0.545 | 052 Pvalb Gaba | Ptprn | gene | — | — | — | ✓ |
| 21 | padj | = | 0.0490 | 052 Pvalb Gaba | Ptprn | gene | — | — | — | ✓ |
| 22 | logfc | = | 1.007 | 052 Pvalb Gaba | Lpcat1 | gene | — | — | — | ✓ |
| 23 | padj | = | 0.0490 | 052 Pvalb Gaba | Lpcat1 | gene | — | — | — | ✓ |

**Kontrol:** ✓ 23 satır doğru. Farklı isimli genler aynı perturbasyonda ölçülen sonuçlar; farklı perturbasyonlar değil.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 7. Bin1 / E001

Row cell_type field: `empty`

Raw statistics text:

> 388046 Bin1-target rows across 23 group_name strata; 2262 total perturbed cells versus 213511 matched controls when summed across strata; Bin1 transcript measured in all 23 strata; target row p<0.05 in 13/23, p<0.01 in 10/23, p<0.001 in 7/23, and FDR<0.05 in 3/23.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 388046 | — | — | target | rows | unstated | — | ✓ |

**Kontrol:** ✓ n_rows doğru. Toplam hücre sayıları tek hücre tipine yazılamaz; özetlerin kapsamı ayrıca doğrulanmalı.

**Missed:** **Kapsamı doğrulanacak:** n_pert=2262 ve n_ctrl=213511 (23 strata üzerinden toplam); 23 strata; p<0.05: 13/23, p<0.01: 10/23, p<0.001: 7/23, padj<0.05: 3/23. Bunlar tek hücre tipine yazılmadı.

---


## 8. Bmpr2 / E001

Row cell_type field: `empty`

Raw statistics text:

> 371,818 Bmpr2-perturbation rows across 22 cell classes; the Bmpr2 transcript had negative logFC in 22/22 classes, nominal p<0.05 in 17/22, FDR<0.05 in 2/22, and median self logFC -0.671.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 371,818 | — | — | target | rows | unstated | — | ✓ |

**Kontrol:** ✓ n_rows doğru. Medyan ve oranlar için kapsam belgesi gerekli.

**Missed:** **Kapsamı doğrulanacak:** 22 sınıf; negatif logFC 22/22; p<0.05: 17/22; padj<0.05: 2/22; median self logFC=-0.671.

---


## 9. Casr / E007

Row cell_type field: `empty`

Raw statistics text:

> Top-100 Casr-restricted screen placed Grm1 among the inverse neighbors in 054 CNU-MGE GABA and 155 MB Glut with r=-0.399193 and r=-0.372081 over selected genes; corresponding all-gene Casr:Grm1 correlations were -0.046000 and -0.016567.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓* Korelasyonlar ve Top-100 bilgisi kapsam dışıysa boş anotasyon doğru.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 10. Cep85l / E005

Row cell_type field: `empty`

Raw statistics text:

> Cdk5r1 was nominally up in 017 CA3 CA2-FC DG Glut (score 2.131, logFC 0.342, p=0.0331, FDR=1.0), 022 L5 ET CTX Glut (score 2.498, logFC 0.233, p=0.0125, FDR=1.0), 054 CNU-MGE GABA (score 2.303, logFC 0.348, p=0.0213, FDR=1.0), and 308 CB GABA (score 2.967, logFC 0.433, p=0.00301, FDR=1.0).

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | score | = | 2.131 | 017 CA3 CA2-FC DG Glut | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 2 | logfc | = | 0.342 | 017 CA3 CA2-FC DG Glut | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 3 | pval | = | 0.0331 | 017 CA3 CA2-FC DG Glut | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 4 | padj | = | 1.0 | 017 CA3 CA2-FC DG Glut | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 5 | score | = | 2.498 | 022 L5 ET CTX Glut | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 6 | logfc | = | 0.233 | 022 L5 ET CTX Glut | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 7 | pval | = | 0.0125 | 022 L5 ET CTX Glut | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 8 | padj | = | 1.0 | 022 L5 ET CTX Glut | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 9 | score | = | 2.303 | 054 CNU-MGE GABA | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 10 | logfc | = | 0.348 | 054 CNU-MGE GABA | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 11 | pval | = | 0.0213 | 054 CNU-MGE GABA | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 12 | padj | = | 1.0 | 054 CNU-MGE GABA | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 13 | score | = | 2.967 | 308 CB GABA | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 14 | logfc | = | 0.433 | 308 CB GABA | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 15 | pval | = | 0.00301 | 308 CB GABA | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 16 | padj | = | 1.0 | 308 CB GABA | Cdk5r1 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |

**Kontrol:** ✓* 16 satırın sayı/gen/hücre tipi doğru. Cdk5r1 adı bir ölçülen gen olarak okunmuştur; metin Cdk5r1 perturbasyonu demiyor. Cep85l bağlamının sürdüğü varsayımıyla korunur.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 11. Chrna2 / E005

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> Chrna2 perturbation: Chrna2 score 0.319, p=0.750, FDR=1.0 with 231 cells. Comparator on-target rows in the same cell type were Chrnb2 score -6.594, p=4.27e-11, FDR=7.37e-7 with 222 cells; Chrna4 score -5.128, p=2.92e-7, FDR=0.00373 with 293 cells; Ache score -5.165, p=2.40e-7, FDR=0.00415 with 117 cells.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | score | = | 0.319 | 151 TH Prkcd Grin2c Glut | Chrna2 | gene | — | — | — | ✓ |
| 2 | pval | = | 0.750 | 151 TH Prkcd Grin2c Glut | Chrna2 | gene | — | — | — | ✓ |
| 3 | padj | = | 1.0 | 151 TH Prkcd Grin2c Glut | Chrna2 | gene | — | — | — | ✓ |
| 4 | n_pert | = | 231 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — | ✓ |

**Kontrol:** ✓ Dört Chrna2 satırı doğru; açıkça comparator olan diğer perturbasyonlar dışlanır.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 12. Dlx5 / E006

Row cell_type field: `empty`

Raw statistics text:

> Dlx6 had 23 tested cell-type contrasts and 0 rows with FDR<0.05. Spearman correlations between matched Dlx5 and Dlx6 score vectors ranged from -0.039274 in 308 CB GABA to 0.087554 in 009 L2-3 IT PIR AON ENT Glut across the 23 shared Dlx5 cell types.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓* Dlx6 perturbasyonu kapsam dışı; korelasyonlar da kapsam dışıysa boş anotasyon doğru.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 13. Eif4h / E010

Row cell_type field: `empty`

Raw statistics text:

> Total q<0.05 rows across matched eIF4-related perturbations: Eif4h=1, Eif4a2=6, Eif4g1=1, Eif4e=184; in 151 TH Prkcd Grin2c Glut specifically, Eif4h=1, Eif4a2=2, Eif4g1=1, Eif4e=160.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✗ Eif4h için iki ayrı bağlamda 1 anlamlı satır atlanmış. q, padj olarak normalleştirildi.

**Missed:** 

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| n_sig | = | 1 | — | — | target | rows | unstated | padj < 0.05 |
| n_sig | = | 1 | 151 TH Prkcd Grin2c Glut | — | cell | rows | unstated | padj < 0.05 |

---


## 14. Glrb / E006

Row cell_type field: `empty`

Raw statistics text:

> Exact target filtering recovered Arhgef9 338323 rows across 20 groups and Glra1, Glra2, Glra3, Gphn, and Slc6a5 each with 371818 rows across 22 groups; exact gene_target values Glra4 and Slc6a9 returned 0 rows.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓ Tüm sayılar açıkça başka gene_target değerlerine ait; Glrb için sayı yok.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 15. Gpr162 / E007

Row cell_type field: `007 L2-3 IT CTX Glut`

Raw statistics text:

> 66 perturbed cells versus 7,553 controls; Ppp2r5d was the top positive row with score 4.436, logFC +0.800, p=9.17e-6, FDR=0.154; Gpr162 in the same signature had score -3.381, logFC -0.377, p=7.23e-4, FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 66 | 007 L2-3 IT CTX Glut | — | cell | — | — | — | ✓ |
| 2 | n_ctrl | = | 7,553 | 007 L2-3 IT CTX Glut | — | cell | — | — | — | ✓ |
| 3 | score | = | 4.436 | 007 L2-3 IT CTX Glut | Ppp2r5d | gene | — | — | — | ✓ |
| 4 | logfc | = | +0.800 | 007 L2-3 IT CTX Glut | Ppp2r5d | gene | — | — | — | ✓ |
| 5 | pval | = | 9.17e-6 | 007 L2-3 IT CTX Glut | Ppp2r5d | gene | — | — | — | ✓ |
| 6 | padj | = | 0.154 | 007 L2-3 IT CTX Glut | Ppp2r5d | gene | — | — | — | ✓ |
| 7 | score | = | -3.381 | 007 L2-3 IT CTX Glut | Gpr162 | gene | — | — | — | ✓ |
| 8 | logfc | = | -0.377 | 007 L2-3 IT CTX Glut | Gpr162 | gene | — | — | — | ✓ |
| 9 | pval | = | 7.23e-4 | 007 L2-3 IT CTX Glut | Gpr162 | gene | — | — | — | ✓ |
| 10 | padj | = | 1.0 | 007 L2-3 IT CTX Glut | Gpr162 | gene | — | — | — | ✓ |

**Kontrol:** ✓ On satır doğru. Ppp2r5d aynı Gpr162 imzasında ölçülen gendir.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 16. Hdac5 / E009

Row cell_type field: `empty`

Raw statistics text:

> In 151 TH Prkcd Grin2c Glut, score correlations with the Hdac5 signature were Ppp2r1a r=0.0305, Ppp3ca r=-0.0317, Camk2b r=-0.0181, Hdac4 r=0.0269, Mef2c r=0.0076, Mef2d r=0.0058. In 155 MB Glut, the matching r values were 0.0288, 0.0179, 0.0179, 0.0039, 0.0161, and 0.0019.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓* Korelasyonlar kapsam dışıysa boş anotasyon doğru.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 17. Htr1a / E005

Row cell_type field: `empty`

Raw statistics text:

> FDR<0.05 row counts among assayed serotonin receptors were Htr2a=1 and Htr3b=1, with Htr1a, Htr1b, Htr1f, Htr2b, Htr2c, Htr3a, Htr4, Htr6, and Htr7 all 0; minimum adjusted p values were Htr3b 0.0195, Htr2a 0.0330, Htr1f 0.0654, Htr1b 0.308, Htr2c 0.361, Htr7 0.575, and Htr1a 0.693; none of the 11 receptor perturbations significantly reduced its own transcript.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✗ Htr1a için FDR<0.05 satır sayısı 0 atlanmış. Minimum adjusted p=0.693 de verilmiş; min_padj türünün izinli olması ayrıca doğrulanmalı.

**Missed:** 

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 |

**Kod kitabına bağlı ek aday:** Minimum adjusted p=0.693, Htr1a perturbasyonunun özetidir; ölçülen gen belirtilmemiştir (gene=—). İzin veriliyorsa target düzeyinde minimum olarak kodlanmalı; quantity=min_padj ve scope=target birleşiminin geçerliliği kod kitabından doğrulanmalıdır. Htr1a transkriptine ait tekil padj olarak yazılmamalı.

---


## 18. Il1rapl1 / E014

Row cell_type field: `empty`

Raw statistics text:

> 88 rows covering Mcf2l, Rhoa, Rock1, and Rock2 across 22 cell types; 0 rows with FDR<0.05; Mcf2l was nominally down only in 017 CA3 CA2-FC DG Glut with p=0.0266 and 046 CTX-CGE GABA with p=0.0357; Rhoa had minimum nominal p=0.176.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 | ✓* Yalnızca dört genlik alt küme; tüm target sonucu değil. |
| 2 | pval | = | 0.0266 | 017 CA3 CA2-FC DG Glut | Mcf2l | gene | — | — | — | ✓ |
| 3 | pval | = | 0.0357 | 046 CTX-CGE GABA | Mcf2l | gene | — | — | — | ✓ |
| 4 | min_pval | = | 0.176 | — | Rhoa | gene | — | — | — | ✓ |

**Kontrol:** ✓* İlk sayı yalnızca Mcf2l/Rhoa/Rock1/Rock2 için seçilen 88 satırı kapsar. scope=target tüm Il1rapl1 sonuçları demekse bu alan düzeltilmeli, dört genlik alt kümeyle sınırlandırılmalı. Diğer üç satırın sayı/gen/hücre tipi doğru. Metin başka bir perturbasyon belirtmediğinden Il1rapl1 bağlamı korunmuştur.

**Missed:** **Kapsamı doğrulanacak:** n_rows=88, yalnızca Mcf2l/Rhoa/Rock1/Rock2 genlerinin 22 hücre tipindeki satırları. Tüm Il1rapl1 perturbasyonu sayısı olarak eklenmemeli. Alt küme kapsamı destekleniyorsa 88 ve n_sig=0 aynı alt kümeye bağlanmalı.

---


## 19. Itm2b / E006

Row cell_type field: `empty`

Raw statistics text:

> P4htm reached FDR < 0.05 only in 027 NP-CT-L6b-OB Glut; its next smallest nominal p was 0.0214 in 052 Pvalb Gaba with FDR=1.0. Lrrc24 reached FDR < 0.05 only in 052 Pvalb Gaba; its next smallest nominal p was 0.0529 in 191 MB P MY GABA with FDR=1.0.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | pval | = | 0.0214 | 052 Pvalb Gaba | P4htm | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 2 | padj | = | 1.0 | 052 Pvalb Gaba | P4htm | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 3 | pval | = | 0.0529 | 191 MB P MY GABA | Lrrc24 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |
| 4 | padj | = | 1.0 | 191 MB P MY GABA | Lrrc24 | gene | — | — | — | ✓* Ölçülen gen yorumu; kontrol notuna bak. |

**Kontrol:** ✓* Dört satırın sayı/gen/hücre tipi doğru. P4htm ve Lrrc24, Itm2b altında ölçülen genler kabul edildi; metinde başka perturbasyon oldukları belirtilmiyor. Bu yorumla iki FDR<0.05 iddiası atlanmış.

**Missed:** 

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| padj | < | 0.05 | 027 NP-CT-L6b-OB Glut | P4htm | gene | — | — | — |
| padj | < | 0.05 | 052 Pvalb Gaba | Lrrc24 | gene | — | — | — |

*Bu iki ek satır mevcut dört satırla aynı bağlam varsayımına bağlıdır. Bu genler comparator perturbasyonlarıysa altı satır da dışlanmalıdır.*

---


## 20. Mboat7 / E003

Row cell_type field: `empty`

Raw statistics text:

> Mboat7 target transcript logFC was negative in 21/22 measured cell types; median logFC -0.430682; p<0.05 in 17/22, p<0.01 in 14/22, p<0.001 in 10/22; Mboat7 was the largest absolute-score gene in 7/22 cell types.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓* Yalnızca oranlar ve medyan var; bu özetler kapsam dışıysa boş anotasyon doğru.

**Missed:** **Kapsamı doğrulanacak:** negatif logFC 21/22; median logFC=-0.430682; p<0.05: 17/22; p<0.01: 14/22; p<0.001: 10/22; en büyük absolute-score 7/22.

---


## 21. Mttp / E004

Row cell_type field: `145 MH-LH TH Glut`

Raw statistics text:

> 55 Mttp-targeted cells versus 6,961 controls; Pcsk2 logFC 0.7089, score 4.1818, nominal P=2.89e-05, FDR=0.3545; Tsc22d2 logFC -0.9627, score -4.0938, nominal P=4.19e-05, FDR=0.3545; Kpna3 FDR=0.7328; Gramd1a FDR=0.7374; Mapk8ip2 FDR=0.8451.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 55 | 145 MH-LH TH Glut | — | cell | — | — | — | ✓ |
| 2 | n_ctrl | = | 6,961 | 145 MH-LH TH Glut | — | cell | — | — | — | ✓ |
| 3 | logfc | = | 0.7089 | 145 MH-LH TH Glut | Pcsk2 | gene | — | — | — | ✓ |
| 4 | score | = | 4.1818 | 145 MH-LH TH Glut | Pcsk2 | gene | — | — | — | ✓ |
| 5 | pval | = | 2.89e-05 | 145 MH-LH TH Glut | Pcsk2 | gene | — | — | — | ✓ |
| 6 | padj | = | 0.3545 | 145 MH-LH TH Glut | Pcsk2 | gene | — | — | — | ✓ |
| 7 | logfc | = | -0.9627 | 145 MH-LH TH Glut | Tsc22d2 | gene | — | — | — | ✓ |
| 8 | score | = | -4.0938 | 145 MH-LH TH Glut | Tsc22d2 | gene | — | — | — | ✓ |
| 9 | pval | = | 4.19e-05 | 145 MH-LH TH Glut | Tsc22d2 | gene | — | — | — | ✓ |
| 10 | padj | = | 0.3545 | 145 MH-LH TH Glut | Tsc22d2 | gene | — | — | — | ✓ |
| 11 | padj | = | 0.7328 | 145 MH-LH TH Glut | Kpna3 | gene | — | — | — | ✓ |
| 12 | padj | = | 0.7374 | 145 MH-LH TH Glut | Gramd1a | gene | — | — | — | ✓ |
| 13 | padj | = | 0.8451 | 145 MH-LH TH Glut | Mapk8ip2 | gene | — | — | — | ✓ |

**Kontrol:** ✓ 13 satır doğru; ölçülen genler Mttp perturbasyonu altında.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 22. Nefl / E001

Row cell_type field: `empty`

Raw statistics text:

> 22 cell-type tests; Nefl logFC was negative in 21/22; nominal p<0.05 in 19/22; FDR<0.05 in 11/22 and FDR<0.10 in 12/22; median logFC -0.915.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓* Hücre tipi sayıları, oranlar ve medyan kapsam dışıysa boş anotasyon doğru.

**Missed:** **Kapsamı doğrulanacak:** 22 test; negatif logFC 21/22; p<0.05: 19/22; padj<0.05: 11/22; padj<0.10: 12/22; median logFC=-0.915.

---


## 23. Nfic / E011

Row cell_type field: `empty`

Raw statistics text:

> The Nfic subset contained 388,046 Wilcoxon rows across 23 cell types. Exactly two rows had FDR<0.05: Bambi in 151 TH Prkcd Grin2c Glut at FDR=0.00382 and Nfic in 155 MB Glut at FDR=0.0175; 4 rows had FDR<=0.1 and 16 had FDR<=0.5.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 388,046 | — | — | target | rows | unstated | — | ✓ |
| 2 | n_sig | = | 2 | — | — | target | rows | unstated | padj < 0.05 | ✓ |
| 3 | padj | = | 0.00382 | 151 TH Prkcd Grin2c Glut | Bambi | gene | — | — | — | ✓ |
| 4 | padj | = | 0.0175 | 155 MB Glut | Nfic | gene | — | — | — | ✓ |
| 5 | n_sig | = | 4 | — | — | target | rows | unstated | padj <= 0.1 | ✓ |
| 6 | n_sig | = | 16 | — | — | target | rows | unstated | padj <= 0.5 | ✓ |

**Kontrol:** ✓ Altı satır doğru; < ve <= ilişkileri korunmuş.

**Missed:** Kesin ek atlama yok. **Kapsamı doğrulanacak:** 23 hücre tipi sayısı.

---


## 24. Nobox / E002

Row cell_type field: `22 Nobox-tested cell classes`

Raw statistics text:

> 371818 gene-by-cell-type rows; 0 rows with FDR<0.05; 1 row with FDR<0.1; 134 rows with nominal p<0.001 across all rows.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_rows | = | 371818 | — | — | target | rows | unstated | — | ✓ |
| 2 | n_sig | = | 0 | — | — | target | rows | unstated | padj < 0.05 | ✓ |
| 3 | n_sig | = | 1 | — | — | target | rows | unstated | padj < 0.1 | ✓ |
| 4 | n_sig | = | 134 | — | — | target | rows | unstated | pval < 0.001 | ✓ |

**Kontrol:** ✓ Dört satır doğru. Satır alanındaki 22 Nobox-tested cell classes tek hücre tipi değildir; target toplamlarında cell type boş kalmalı.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 25. Paqr8 / E003

Row cell_type field: `empty`

Raw statistics text:

> Paqr8 was measured in 22 signatures with 40-215 perturbed cells per signature; 17/22 estimated Paqr8 logFC values were negative, 3/22 Paqr8 rows had nominal p<0.05, and 1/22 had FDR<0.05.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓* İmza sayısı, aralık ve oranlar kapsam dışıysa boş anotasyon doğru.

**Missed:** **Kapsamı doğrulanacak:** 22 imza; imza başına n_pert aralığı 40–215; negatif logFC 17/22; p<0.05: 3/22; padj<0.05: 1/22.

---


## 26. Pde1c / E004

Row cell_type field: `empty`

Raw statistics text:

> Total FDR < 0.05 genes across matched PDE perturbations and cell types: Pde1c 0, Pde3a 0, Pde4d 0, Pde4b 2, Pde10a 3. Pde10a self-depletion was significant only in 059 CNU-LGE LSX GABA with logFC -0.942, FDR 0.00478.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✗ Pde1c için toplam FDR<0.05 gen sayısı 0 atlanmış. Kaynak genes dediği için unit=genes korunmuştur. Diğer perturbasyonlar kapsam dışı.

**Missed:** 

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| n_sig | = | 0 | — | — | target | genes | unstated | padj < 0.05 |

---


## 27. Plxnc1 / E002

Row cell_type field: `151 TH Prkcd Grin2c Glut`

Raw statistics text:

> 258 perturbed cells versus 23,679 controls; Plxnc1 score -4.458, logFC -0.575, p=8.26e-6, FDR=0.1426; rank 1/17,259 by negative score, absolute score, and nominal p.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_pert | = | 258 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — | ✓ |
| 2 | n_ctrl | = | 23,679 | 151 TH Prkcd Grin2c Glut | — | cell | — | — | — | ✓ |
| 3 | score | = | -4.458 | 151 TH Prkcd Grin2c Glut | Plxnc1 | gene | — | — | — | ✓ |
| 4 | logfc | = | -0.575 | 151 TH Prkcd Grin2c Glut | Plxnc1 | gene | — | — | — | ✓ |
| 5 | pval | = | 8.26e-6 | 151 TH Prkcd Grin2c Glut | Plxnc1 | gene | — | — | — | ✓ |
| 6 | padj | = | 0.1426 | 151 TH Prkcd Grin2c Glut | Plxnc1 | gene | — | — | — | ✓ |
| 7 | n_rows | = | 17,259 | 151 TH Prkcd Grin2c Glut | — | cell | genes | — | — | ✓* Rank paydası; n_rows kodlama kuralı doğrulanmalı. |

**Kontrol:** ✓ İlk altı satır doğru. ✓* 17,259 sıralamanın gen paydası; n_rows olarak kodlanması kurala bağlı. Rank=1, n_rows değildir.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---


## 28. Plxnc1 / E006

Row cell_type field: `empty`

Raw statistics text:

> Outside the five cell types with Plxnc1 p<0.005, the target row had p>=0.0325 and FDR=1.0; in 017 CA3 CA2-FC DG Glut Plxnc1 logFC was -0.052 with p=0.732, and in 217 P MY Pineal Glut logFC was -0.150 with p=0.978.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | logfc | = | -0.052 | 017 CA3 CA2-FC DG Glut | Plxnc1 | gene | — | — | — | ✓ |
| 2 | pval | = | 0.732 | 017 CA3 CA2-FC DG Glut | Plxnc1 | gene | — | — | — | ✓ |
| 3 | logfc | = | -0.150 | 217 P MY Pineal Glut | Plxnc1 | gene | — | — | — | ✓ |
| 4 | pval | = | 0.978 | 217 P MY Pineal Glut | Plxnc1 | gene | — | — | — | ✓ |

**Kontrol:** ✓ Dört satır doğru. İsmi tek tek verilmeyen hücre tipi grubuna ait p>=0.0325 ve FDR=1.0 iddialarının nasıl kodlanacağı kurala bağlı.

**Missed:** **Kapsamı doğrulanacak:** Plxnc1 p>=0.0325 ve padj=1.0, p<0.005 olan beş hücre tipi dışındaki gruba ait. İki adı verilen hücre için padj=1.0 grup ifadesinden çıkarılabilir; doğrudan belirtilmeyen değerleri gruptan yayma kuralı sağlanmadığından kesin ek satır olarak yazılmadı.

---


## 29. Rpgrip1l / E006

Row cell_type field: `empty`

Raw statistics text:

> B9d1 in 308 CB GABA had 9 FDR<0.05 genes among 62 perturbed cells, led by Bend6 FDR=0.0343 and Phc2/Homer3/Gas8 FDR=0.0452; Ahi1 in 155 MB Glut had its own target transcript decreased, logFC=-0.695, p=4.26e-11, FDR=7.44e-7; Ift88 in 155 MB Glut had Pcsk1n logFC=0.427, p=5.30e-7, FDR=0.00924. Rpgrip1l had 0 FDR<0.05 genes in 308 CB GABA and 155 MB Glut.

| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | n_sig | = | 0 | 308 CB GABA | — | cell | genes | unstated | padj < 0.05 | ✓ |

**Kontrol:** ✓ Mevcut 308 CB GABA satırı doğru; 155 MB Glut için aynı 0 sayısı atlanmış. Açıkça başka perturbasyonlara ait değerler dışlanır.

**Missed:** 

| quantity | rel | value | cell type | gene | scope | unit | self | threshold |
|---|---|---|---|---|---|---|---|---|
| n_sig | = | 0 | 155 MB Glut | — | cell | genes | unstated | padj < 0.05 |

---


## 30. Stard7 / E008

Row cell_type field: `empty`

Raw statistics text:

> Across 22 cell types, mean Pearson correlations with Stard7 scores ranged from -0.002 for Selenoi to 0.024 for Chchd10. Only |r| > 0.10 values were in 308 CB GABA: Micos13 0.238, Chchd10 0.231, Mboat7 0.210, Pitpnm3 -0.183; these comparator CB GABA tables had minimum FDR 1.000.

*The annotator found no in-scope assertion in this field.*

**Kontrol:** ✓* Korelasyonlar kapsam dışıysa ve minimum FDR açıkça comparator tablolarına ait olduğundan boş anotasyon doğru.

**Missed:** Yok; yukarıdaki kapsam notu geçerlidir.

---
