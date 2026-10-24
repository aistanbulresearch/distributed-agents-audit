# Independent annotation task (H1, sample 1)

You are an independent annotator for a pre-registered measurement. Work only from this
message.

**Rules.** Do not open, read, list or search any file or directory; do not run commands; do
not search the web. The only tool use allowed is writing your single output file (below).

**Task.** For each of the 150 evidence fields at the end of this message, list every
quantitative assertion that the extraction grammar in Section 3 (quoted verbatim below)
puts in scope (types A, A′, B, C, D, E) **and** for which Section 3's rules determine every
required context (a cell type for gene values, cell counts and anything Section 3 binds to a
cell type; a gene for gene values). Omit assertions that Section 3 classes as out of scope
(ranges, correlations, medians, means, maxima, approximations, recurrence, other
perturbations, restricted subsets) and assertions whose required context cannot be
determined. Each field's own `cell_type` value is given; Section 3 says when it applies.
Treat mouse gene symbols as genes.

**Output.** Write exactly one file: `C:/Dev/Corpus Audit/_internal/records/prereg/H1_annotation_sample2_B.jsonl`, UTF-8, exactly 150 lines, one JSON
object per field, in the order given below:
`{"target_gene": ..., "evidence_id": ..., "assertions": [ ... ]}` (an empty list if none).
Each assertion object has exactly these keys:
- `quantity`: one of `logfc`, `score`, `pval`, `padj`, `n_pert`, `n_ctrl`, `n_sig`, `n_rows`,
  `min_pval`, `min_padj`. Mapping: logFC variants → `logfc`; "score", "z" → `score`;
  "p", "nominal p" → `pval`; "FDR", "q", "padj", "adjusted p" → `padj`.
- `relation`: `=`, `<`, `<=`, `>` or `>=`, as written (`=` when a value is just stated).
- `value_text`: the number exactly as written, sign and thousands separators included; `0`
  for "No …"/"none" counts; "3.1 × 10^-5" written as `3.1e-5`.
- `cell_type`: the exact label from the list below, or `null`.
- `gene`: the gene symbol exactly as written, or `null` (counts, totals, minima without a
  gene).
- `scope`: `gene` for gene values (A, A′) and for minima restricted to a gene; `cell` for
  cell counts (B) and for C/D/E bound to a cell type; `target` for C/D/E without one.
- `unit`: for C and D, `rows` if the text counts rows, otherwise `genes` (also for DEGs,
  transcripts, and the N of "rank r of N"); `null` for other types.
- `self_inclusion`: for C and for D totals of rows, of "k/N", or of "among N tested":
  `exclude`, `include` or `unstated` per Section 3; `null` for "rank r of N" totals and for
  all other types.
- `threshold_quantity`, `threshold_relation`, `threshold_text`: for C only — `padj` or
  `pval`, `<` or `<=`, and the threshold number as written; `null` otherwise.

When finished, reply with one line giving the number of fields written and the total
number of assertions. Do not include the annotations in your reply.

## Cell-type labels (the only valid `cell_type` values)

- `001 L5-6 IT Glut`
- `005 L4-5 IT CTX Glut`
- `007 L2-3 IT CTX Glut`
- `008 L2-3 IT ENT PPP RSP Glut`
- `009 L2-3 IT PIR AON ENT Glut`
- `012 MEA LA CA1 DG Glut`
- `017 CA3 CA2-FC DG Glut`
- `022 L5 ET CTX Glut`
- `027 NP-CT-L6b-OB Glut`
- `046 CTX-CGE GABA`
- `052 Pvalb Gaba`
- `053 Sst Gaba`
- `054 CNU-MGE GABA`
- `059 CNU-LGE LSX GABA`
- `066 CNU-HYa HY GABA`
- `110 CNU-HYa HY MM Glut`
- `145 MH-LH TH Glut`
- `151 TH Prkcd Grin2c Glut`
- `155 MB Glut`
- `191 MB P MY GABA`
- `215 MB Dopa`
- `217 P MY Pineal Glut`
- `308 CB GABA`

## 3. Unit of analysis and extraction grammar

The unit is one **atomic assertion**: one reported number, bound to a target, a cell-type
context and, for gene-level values, a gene.

Extraction is done by `audit/lib/h1_extract.py`; `tests/test_h1_extract.py` defines the
grammar by example, using verbatim ledger phrasings (including every case raised in review).
They use the `statistics` text and two vocabularies only: the 23 cell-type labels and the
distinct gene names (`names`) of the reference file. No DE value column is read.

**Processing order.** Normalise numbers (Unicode minus; `3.1 × 10^-5` → `3.1e-5`) → mask every
cell-type label → split sentences (not after `vs.`, `e.g.`, `i.e.`, `ca.`, `approx.`, `Fig.`,
`al.`, `cf.`) and clauses (`;`) → mask out-of-scope spans, numeric ranges first → match
in-scope patterns in a fixed order, masking each match so no number is used twice.

**Cell-type resolution, in this order:**
1. the nearest label earlier in the same clause (a colon does not stop this search, so
   `151 TH Prkcd Grin2c Glut: 135 perturbed …` binds the label);
2. the first label later in the same clause, **without crossing a colon** (so in
   `Only 6 Ap3b1 rows had FDR<1.0: Fam169a … in 005 L4-5 IT CTX Glut` the count is not
   bound to 005, while Fam169a's values are);
3. for gene-level values only: the nearest label earlier in the same sentence;
4. the row's `cell_type` field;
5. otherwise none.
The source (`clause`, `sentence`, `row`) is recorded. Regression: Ap3b1/E004.

**Gene resolution.** Cell-type labels are masked first, so gene symbols inside labels
(`053 Sst Gaba`, `052 Pvalb Gaba`, `151 TH Prkcd Grin2c Glut`) are never bound (regression:
Grm6/E004). Equalities bind to the nearest preceding measured-gene token in the sentence.
**Inequalities bind only to a gene token directly before the statistic** (optionally followed
by "self" or "target"); otherwise they are `unresolved_context`, so aggregate thresholds
(`overall FDR<0.05`) never become gene assertions.

**Assertion types in scope:**

| Type | Examples | Recomputed as |
|---|---|---|
| A. Gene value | `Auh score -5.116, logFC -0.571, p=3.12e-7, FDR=0.00544`; `q 0.0318` | the value for (target, cell type, gene) |
| A′. Gene inequality | `Ahdc1 FDR<0.05` | whether the inequality holds |
| B. Cell counts | `145 perturbed cells versus 20,353 controls`; `164 Clec16a cells versus 23,679 controls`; `135 perturbed versus 23,679 controls`; `149 Rara cells`; `8,277 controls`; `n_pert_matched 64` | `n_pert_matched`, `n_ctrl_matched` |
| C. Significant-gene count | `37 genes at FDR<0.05`; `0 FDR<0.05 genes`; `No FDR <0.05 genes`; `112 rows had p < 0.001`; `6 Ap3b1 rows had FDR<1.0` | rows below the stated threshold |
| D. Totals | `371818 Wilcoxon rows`; `rank 1 of 17,443`; the N in `1/17443 genes` | row count for the bound scope |
| E. Minima | `min FDR=0.602440`; `minimum nominal p = 1.13e-05` | minimum over the bound scope |

Regressions: Bcas3/E005 (threshold-first zero counts; "perturbed versus" without "cells"),
Clec16a/E004 (paired count naming the target), Fezf1/E003 (ranges).

**One primary interpretation per assertion.** Counts (C, D) and minima (E) are recomputed
under a single primary interpretation, fixed by the text:
- *Unit:* `rows` → gene × cell-type rows; `genes`/`DEGs`/`transcripts` at cell scope → rows
  of that cell type; at target scope → distinct genes.
- *Self inclusion:* resolved once per count from the count's own text plus its lead-in (from
  the previous extracted span in the same clause, or the clause start), so a qualifier of an
  earlier count never carries over. `non-target`, `non-self`, `non-<Target>` (e.g.
  `non-Ap3b2`), `excluding the target / <Target>`, `other than the target / <Target>` → the
  target's own transcript excluded; `including the target / <Target>` → included; otherwise
  included (literal reading). The same resolution applies to the count's denominator (the N
  in `k/N` and in `among N tested`). Recorded as `self_inclusion`. Regressions: Dnajc5/E006,
  Ap3b2/E002.
- *Restricted populations:* a count, total or minimum whose lead-in names a restricted subset
  (`selected`, `listed`, `prespecified`, `candidate`, `chosen`, `curated`, `panel`, `module`,
  `these`, `those`) is `out_of_scope` (reason `subset_scope`): the subset cannot be
  reconstructed from the DE data, so it is neither bound to a nearby cell type nor compared.
  Regression: Ndufv1/E008. The word list is how the extractor detects subsets; it does not
  limit the rule. For the annotation key, a count whose text explicitly identifies a
  restricted population (e.g. "88 rows covering Mcf2l, Rhoa, Rock1, and Rock2") is out of
  scope as a subset count even without one of these words; an extractor that keeps such a
  count in scope makes an extraction error, counted by the quality gate (section 5).
- *Scope:* the bound cell type if any; otherwise the whole target. A gene token directly
  before "minimum" restricts E to that gene.

Where the text is genuinely ambiguous — `genes` at target scope, unstated self inclusion, or a
cell type that came only from the row field — the alternative interpretation (rows instead
of distinct genes; self excluded; target scope instead of the row's cell type) is computed
as a **sensitivity analysis** and reported separately with its own counts. It never changes
the primary outcome.

**Out of scope** (counted, not evaluated): counts over restricted subsets (above); every
numeric range (`0.895-0.917`, `23-191`,
`-0.21 to -0.4`, "ranged from", "between … and"), correlations and similarities (r, rho,
cosine), medians, means, maxima, approximations (`~`, "approximately"), recurrence across
cell types or signatures (a clause containing `k/N had`, `k of N cell types`, `in k/N`), and
any clause naming another perturbation (`Tsc1 perturbation` in a Tsc2 row).

**Outcome categories.** `match`; `mismatch`; `context_not_in_data` (target × cell type or gene
absent from the reference); `unresolved_context` (no cell type or gene could be bound);
`out_of_scope`.

## The 150 fields

{"target_gene": "Abca7", "evidence_id": "E010", "cell_type": "308 CB GABA", "statistics": "83 perturbed cells versus 8,277 controls; Sh3glb1 score -3.913 logFC -0.747 p=9.10e-5; Clcn7 score 3.235 p=0.00122; Npc1 score -2.651 p=0.00801; Ap3b2 score 2.662 p=0.00777; all FDR=1.0."}
{"target_gene": "Acat1", "evidence_id": "E007", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Genome-wide Pearson correlations to the Acat1 score vector in 151 were near zero: Srebf2 r=-0.0057, Hmgcr r=-0.0096, Auh r=0.0078, Ivd r=-0.0161, Acsl4 r=0.0092, Acox1 r=0.0008, Abca1 r=0.0152, Abca7 r=0.0020, Aco2 r=-0.0076, Ogdh r=0.0044, and Pdha1 r=-0.0079 over 17259 shared genes."}
{"target_gene": "Acbd5", "evidence_id": "E006", "cell_type": null, "statistics": "Pearson correlations of Wilcoxon scores between Acbd5 and all 44,111 non-Acbd5 target-by-cell-type signatures had a maximum of +0.1638 and a minimum of -0.1495; Safe_target_72 was the second-closest positive neighbor at r=0.1548. Among Abcd3, Acox1, Acsl4, Agps, Hsd17b4, Pex1, Pex13, Pex14, and Vapb matched by cell type, the largest absolute Acbd5 correlation was |r|=0.1075 and per-target mean r ranged from -0.0048 to +0.0229."}
{"target_gene": "Acox1", "evidence_id": "E005", "cell_type": "308 CB GABA", "statistics": "32 Acox1-perturbed cells versus 8277 controls; Gtf2i logFC 0.446, score 4.303, p=1.69e-5, FDR=0.286; Orai2 logFC 0.875, p=7.38e-5, FDR=0.485; Acbd5 logFC -1.959, score -3.928, p=8.58e-5, FDR=0.485; Acox1 logFC -0.359, p=0.172, FDR=1; 11 genes had p<0.001 and none had FDR<0.05."}
{"target_gene": "Adnp", "evidence_id": "E009", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Among 2046 perturbations in 151 TH Prkcd Grin2c Glut, Arid2 had the lowest score correlation to Adnp, r=-0.111954; Arid2 had 56 FDR<0.05 genes, 7 of the 25 Adnp FDR genes had the same sign under Arid2, and 0 of the 7 Arid2-nominal genes among the Adnp FDR set were same-direction."}
{"target_gene": "Ahdc1", "evidence_id": "E009", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Top positive all-gene Pearson correlations to Ahdc1 scores, excluding Ahdc1 itself: Camta1 r=0.0956, Arid2 0.0786, Pura 0.0770, Tnrc6b 0.0768, Safe_target_23 0.0737. Top negative: Kmt2d r=-0.1296, Crebbp -0.1139, Nipbl -0.0920, Apc -0.0860."}
{"target_gene": "Ahrr", "evidence_id": "E002", "cell_type": null, "statistics": "Ahrr transcript measured in 22 Ahrr-targeted cell classes; score range -0.380445 to 0.976431; absolute maximum score 0.976431 in 022 L5 ET CTX Glut; nominal p range 0.328851-0.987434; FDR=1.0 in all 22 rows."}
{"target_gene": "Arid1b", "evidence_id": "E008", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Across all measured genes, the Arid1b Wilcoxon-score vector was most positively correlated with Smarcb1 after self, rank 2/2046 with r=0.1499; Smarcc2 ranked 3/2046 with r=0.1232; Arid1a ranked 8/2046 with r=0.1002. Ptpn3 was nominally down after Arid1b perturbation, logFC=-0.228, p=2.96e-04, FDR=0.778, and was FDR significant after Arid1a, Smarcb1, Smarcc2, and Smarce1 perturbation; Reep2 was nominally down after Arid1b, logFC=-0.145, p=2.49e-04, FDR=0.778, and was FDR significant after Smarcb1, Smarcc2, and Smarce1."}
{"target_gene": "Arsb", "evidence_id": "E009", "cell_type": null, "statistics": "Within the five Arsb FDR-engaged cell types, the maximum absolute Pearson correlation to any other perturbation was 0.126 in 005 L4-5 IT CTX Glut; the remaining maxima were 0.052 in 007 L2-3 IT CTX Glut, 0.079 in 008 L2-3 IT ENT PPP RSP Glut, 0.118 in 009 L2-3 IT PIR AON ENT Glut, and 0.114 in 151 TH Prkcd Grin2c Glut."}
{"target_gene": "Arx", "evidence_id": "E004", "cell_type": null, "statistics": "14 of 14 Arx-assayed glutamatergic classes had 0 genes at FDR<0.05; the best adjusted p value among these glutamatergic classes was 0.346 in 151 TH Prkcd Grin2c Glut."}
{"target_gene": "Atl1", "evidence_id": "E010", "cell_type": "022 L5 ET CTX Glut", "statistics": "57 perturbed cells versus 8644 controls; Atl1 logFC -0.387, p=0.00527, FDR=1.0; Atl3 logFC 0.491, score 3.238, p=0.00120, FDR=1.0; Atl3 ranked 8th among positive genes."}
{"target_gene": "Atp6v1a", "evidence_id": "E002", "cell_type": "052 Pvalb Gaba", "statistics": "113 perturbed cells versus 13710 controls; Atp6v1a logFC -0.663, score -6.269, nominal p=3.64e-10, FDR=6.10e-6; 1/16762 genes FDR<0.05."}
{"target_gene": "Atrn", "evidence_id": "E007", "cell_type": null, "statistics": "From 2046 unique gene_target values, Mgrn1, Atrnl1, and Agouti were absent. Agrp, Mc1r, Mc3r, and Mc4r were present in Atrn-shared cell types but their target rows all had FDR = 1.0; max absolute target score was 0.826 for Agrp, 0.351 for Mc1r, 0.443 for Mc3r, and 1.275 for Mc4r; all score-vector correlations with Atrn were |r| <= 0.232."}
{"target_gene": "Bbip1", "evidence_id": "E002", "cell_type": "155 MB Glut", "statistics": "145 perturbed cells versus 20353 controls; Bbip1 score -3.004, logFC -0.459, p=0.00267, p_adj=1.0."}
{"target_gene": "Bmpr1b", "evidence_id": "E005", "cell_type": "052 Pvalb Gaba", "statistics": "78 perturbed cells versus 13710 controls; no gene reached FDR<0.05; the top row was Armcx1 with score -4.432, logFC -0.719, p=9.32e-6, FDR=0.156; the Bmpr1b transcript score was 0.038 with p=0.970 and FDR=1.000."}
{"target_gene": "Bmpr2", "evidence_id": "E008", "cell_type": null, "statistics": "In 15 related BMP/TGF receptor or SMAD perturbations, 0 target self-transcript rows had FDR<0.05; Bmpr2 had 2 self-transcript FDR<0.05 rows and 11 self-transcript nominal p<0.001 rows."}
{"target_gene": "Brd4", "evidence_id": "E002", "cell_type": null, "statistics": "FDR<0.05 genes by cell type: 151 TH Prkcd Grin2c Glut 311, 155 MB Glut 43, 191 MB P MY GABA 21, 052 Pvalb Gaba 3, 046 CTX-CGE GABA 1, 066 CNU-HYa HY GABA 1, and 0 in the other 15 Brd4-assayed cell types."}
{"target_gene": "Bscl2", "evidence_id": "E007", "cell_type": null, "statistics": "Using the top 50 absolute-score non-Bscl2 genes per Bscl2 cell type, concatenated over 22 cell types, the strongest non-safe-target cosine similarities were weak: Cfl2 +0.153, Thoc1 +0.142, Pnkd +0.131; strongest negative neighbors were Ror1 -0.097 and Slc52a2 -0.093."}
{"target_gene": "Bsn", "evidence_id": "E006", "cell_type": null, "statistics": "Pclo was assayed in the same 22 Bsn cell types and had 0 FDR<0.05 genes; Bsn-Pclo score correlations had mean Pearson r=0.010 across all shared genes, range -0.080 to 0.095; using the top 200 absolute Bsn-scored genes per cell type, mean r=0.009, range -0.233 to 0.246."}
{"target_gene": "Cacng8", "evidence_id": "E001", "cell_type": null, "statistics": "388046 Cacng8 DE rows across 23 group_name values and 17994 measured genes; 0 rows at FDR < 0.05, < 0.10, or < 0.20; minimum FDR 0.325; 131 rows had nominal p < 0.001."}
{"target_gene": "Calm1", "evidence_id": "E005", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "In 151 TH Prkcd Grin2c Glut, Calm3 perturbation had 175 perturbed cells and depleted Calm3 with logFC -0.969, p 3.12e-29, FDR 5.38e-25, but had zero non-Calm3 genes at FDR <= 0.05; among the Calm1-induced genes, Eno2 was logFC 0.183, FDR 0.203, Rasgrp2 was logFC 0.392, FDR 1.0, and Peg3 was logFC 0.029, FDR 1.0. Pearson r between Calm1 and Calm3 logFC over the 500 most significant Calm1 genes in this class was 0.084."}
{"target_gene": "Cd247", "evidence_id": "E004", "cell_type": "022 L5 ET CTX Glut", "statistics": "54 perturbed cells versus 8644 controls; Zc3h14 score 4.411 logFC 0.538 p=1.03e-5 FDR=0.174972; Eno2 score -3.573 logFC -0.231 p=3.53e-4 FDR=1.0; Keap1 score -3.514 logFC -0.806 p=4.41e-4 FDR=1.0; Plxnb2 score -3.462 logFC -1.491 p=5.36e-4 FDR=1.0."}
{"target_gene": "Cd80", "evidence_id": "E004", "cell_type": null, "statistics": "At nominal p < 0.001, 104 Cd80 rows represented 104 unique genes; among each cell type's top 50 positive genes, the most recurrent gene appeared in 3 of 21 cell types, and the same maximum recurrence of 3 of 21 was seen for top-50 absolute genes."}
{"target_gene": "Cdin1", "evidence_id": "E004", "cell_type": "009 L2-3 IT PIR AON ENT Glut", "statistics": "46 perturbed cells versus 9,240 controls; 22 genes had p<0.001 and 56 had |score|>3. Zfp638 logFC 0.645, score 4.390, p=1.13e-5, FDR=0.1089; Slit1 logFC -1.376, score -4.366, p=1.27e-5, FDR=0.1089; Vps9d1 logFC -1.021, FDR=0.693."}
{"target_gene": "Celsr2", "evidence_id": "E003", "cell_type": null, "statistics": "Across 388,046 Celsr2 rows, exactly one non-Celsr2 row had FDR<0.05; in each of the 10 cell types with Celsr2 FDR<0.05, Celsr2 was the only FDR<0.05 gene."}
{"target_gene": "Cep112", "evidence_id": "E005", "cell_type": "145 MH-LH TH Glut", "statistics": "34 perturbed cells versus 6961 controls; Cep131 score 4.194, logFC 1.115, p=2.75e-5, FDR=0.458."}
{"target_gene": "Chd8", "evidence_id": "E006", "cell_type": null, "statistics": "066 CNU-HYa HY GABA had 4 FDR genes including Pnisr FDR 8.95e-14 and Usp11 FDR 2.87e-8; 110 CNU-HYa HY MM Glut and 145 MH-LH TH Glut each had only Pnisr at FDR<0.05; 217 P MY Pineal Glut had Pnisr, Csf2ra, and Akt2 at FDR<0.05 with 39 perturbed cells."}
{"target_gene": "Cic", "evidence_id": "E011", "cell_type": null, "statistics": "Atxn1 was FDR-up after Cic perturbation in 151 TH Prkcd Grin2c Glut with logFC 0.496, p 1.91e-11, FDR 7.67e-09, and in 005 L4-5 IT CTX Glut with logFC 0.578, p 1.16e-06, FDR 0.00330; Atxn1 was nominally positive in five Cic-assayed cell types."}
{"target_gene": "Cit", "evidence_id": "E003", "cell_type": null, "statistics": "151 TH Prkcd Grin2c Glut n_pert=268, Cit logFC -0.118 p=0.040 FDR=1, min transcriptome FDR=1; 155 MB Glut n_pert=199, min FDR=0.183; 005 L4-5 IT CTX Glut n_pert=160, min FDR=1; 052 Pvalb Gaba n_pert=134, Cit logFC -0.300 p=0.00675 FDR=1 and min transcriptome FDR=1."}
{"target_gene": "Cntnap2", "evidence_id": "E007", "cell_type": null, "statistics": "Across 052 Pvalb Gaba, 145 MH-LH TH Glut, 151 TH Prkcd Grin2c Glut, 155 MB Glut, and 191 MB P MY GABA, each class had 0 non-Cntnap2 genes at FDR<0.05; their non-target nominal p<0.001 counts were 4, 4, 5, 2, and 4, respectively."}
{"target_gene": "Crebbp", "evidence_id": "E008", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Bottom Pearson correlations versus Crebbp among 2046 perturbations were Prdm2 r=-0.129 rank 2046 with min FDR 0.264, Arid2 r=-0.119 rank 2044 with min FDR 3.76e-12, Kansl1 r=-0.115 rank 2043 with min FDR 1.91e-04, and Ctbp1 r=-0.085 rank 2039 with min FDR 4.87e-19."}
{"target_gene": "Crhr1", "evidence_id": "E002", "cell_type": null, "statistics": "Crhr1 itself was measured in all 22 cell types; all Crhr1 rows had FDR=1.0. Four cell types had nominal p<0.05: 066 CNU-HYa HY GABA score -3.191 logFC -0.737 p=0.00142; 191 MB P MY GABA score -2.412 logFC -0.828 p=0.0159; 001 L5-6 IT Glut score -2.027 logFC -0.576 p=0.0427; 155 MB Glut score -1.971 logFC -0.351 p=0.0487."}
{"target_gene": "Crlf1", "evidence_id": "E002", "cell_type": null, "statistics": "0/371,818 Crlf1 rows at FDR < 0.05 and 0/371,818 at FDR < 0.10; 107/371,818 rows at nominal P < 0.001; the lowest adjusted P was 0.335."}
{"target_gene": "Cux1", "evidence_id": "E006", "cell_type": null, "statistics": "Cux2 target had 371818 rows across the same 22 Cux1-assayed cell groups; 2 total rows were FDR < 0.05: Cux2 in 151 TH Prkcd Grin2c Glut, logFC -0.428, p=8.54e-7, FDR 0.0147, and Sun1 in 053 Sst GABA, logFC 0.916, p=2.43e-6, FDR 0.0400."}
{"target_gene": "Cyfip1", "evidence_id": "E006", "cell_type": null, "statistics": "Cyfip2 had six FDR-significant rows, all Cyfip2 self-rows, in 005 L4-5 IT CTX Glut, 066 CNU-HYa HY GABA, 145 MH-LH TH Glut, 151 TH Prkcd Grin2c Glut, 155 MB Glut, and 191 MB P MY GABA; self FDR range 4.39e-11 to 0.00453; 0 non-self FDR < 0.05 rows."}
{"target_gene": "Dlat", "evidence_id": "E007", "cell_type": null, "statistics": "009 L2-3 IT PIR AON ENT Glut: logFC -0.024, p=0.964; 017 CA3 CA2-FC DG Glut: logFC -0.060, p=0.584; 054 CNU-MGE GABA: logFC -0.132, p=0.415; 007 L2-3 IT CTX Glut: logFC -0.113, p=0.750."}
{"target_gene": "Drd2", "evidence_id": "E003", "cell_type": null, "statistics": "Across the other 22 Drd2 cell-type tests, all on-target Drd2 rows had nominal p>=0.142 and FDR=1.0; n_pert_matched ranged from 33 to 213."}
{"target_gene": "Egr2", "evidence_id": "E006", "cell_type": null, "statistics": "Across the 21 Egr2 signatures each listed transcript was measured 21 times and had minimum FDR=1.0; minimum nominal p-values were 0.1387 for Egr1, 0.0236 for Egr3, 0.3758 for Egr4, 0.0515 for Nab1, 0.1765 for Nab2, 0.0621 for Fos, 0.0373 for Jun, 0.1155 for Junb, 0.1224 for Jund, 0.0614 for Bdnf, 0.0321 for Mef2c, and 0.0210 for Mef2d."}
{"target_gene": "Ehmt1", "evidence_id": "E011", "cell_type": "308 CB GABA", "statistics": "In 308 CB GABA, Pearson score correlations across 16,945 shared genes ranked Wdr26 as the strongest positive Ehmt1 signature neighbor among 2,022 comparators, r=0.358, and Eef2 as the strongest negative neighbor, r=-0.329. The same Ehmt1 308 CB GABA comparison had 69 perturbed cells, 8,277 controls, and 0 FDR<0.05 genes."}
{"target_gene": "Epha3", "evidence_id": "E007", "cell_type": null, "statistics": "In upper-layer cortical glutamatergic groups, Epha3 target rows were not FDR-significant: 005 L4-5 IT CTX Glut logFC=0.193, p=0.684, FDR=1.0; 007 L2-3 IT CTX Glut logFC=-0.565, p=0.0985, FDR=1.0; 008 L2-3 IT ENT PPP RSP Glut logFC=-0.692, p=0.00821, FDR=1.0; 022 L5 ET CTX Glut logFC=-0.340, p=0.544, FDR=1.0. Epha4 showed stronger target decreases in the same broad classes, including FDR hits in 005, 007, and 022 and a nominal/FDR=0.119 decrease in 008 (logFC=-0.660, p=7.16e-6)."}
{"target_gene": "Epm2a", "evidence_id": "E004", "cell_type": null, "statistics": "Among the top 20 absolute-score genes from each of 22 Epm2a cell types, only 13 genes recurred twice and none recurred more than twice; several recurrent genes flipped sign, including Bscl2, Faf2, Mob4, Pum2, Rnmt, and Sumo3."}
{"target_gene": "Etv6", "evidence_id": "E004", "cell_type": null, "statistics": "Across 388046 Etv6 differential-expression rows, 2 rows were FDR<0.05 and 3 rows were FDR<0.20; 21/23 cell types had zero FDR<0.05 genes."}
{"target_gene": "Fam120a", "evidence_id": "E010", "cell_type": null, "statistics": "Across all same-cell-type target signatures, the largest positive Fam120a Pearson neighbor was Wdr26 in 308 CB GABA at r=0.235; the largest negative neighbor was B9d1 in 308 CB GABA at r=-0.202; all other cell-type maxima had |r|<=0.200."}
{"target_gene": "Fras1", "evidence_id": "E002", "cell_type": null, "statistics": "The Fras1 row was present in all 21 groups; all target-transcript FDR values were 1.0, scores ranged from -1.853 to +2.088, and logFC ranged from -1.369 to +1.528. The only nominal p<0.05 target row was positive in 217 P MY Pineal Glut: score +2.088, logFC +0.917, p=0.0368, FDR=1.0."}
{"target_gene": "Fxr1", "evidence_id": "E009", "cell_type": null, "statistics": "Full-rank Pearson correlations between Fxr1 scores and the listed comparator perturbations were small in all 13 Fxr1 cell types; the largest absolute values were Cyfip1 r = 0.207, Eif4e r = -0.185, and Tsc2 r = 0.184, all in 308 CB GABA."}
{"target_gene": "Gata3", "evidence_id": "E001", "cell_type": null, "statistics": "Gata3 rows were present in 23 cell types; n_pert_matched 23-220 and n_ctrl_matched 2019-23679; all Gata3 transcript tests had FDR=1.000, nominal p=0.102-0.976, Wilcoxon score=-1.635 to 0.260."}
{"target_gene": "Gfap", "evidence_id": "E001", "cell_type": null, "statistics": "371,818 Gfap-target DE rows across 22 cell types; 16,428-17,443 measured genes per cell type; 22-133 perturbed cells per block, median 49.5; 3,465-23,679 Non_target controls."}
{"target_gene": "Gfpt1", "evidence_id": "E011", "cell_type": null, "statistics": "Pearson score correlations between Gfpt1 and Ogt perturbations were low: r=0.146 in 151 TH Prkcd Grin2c Glut, r=0.090 in 155 MB Glut, and r=0.064 in 052 Pvalb Gaba. In 151, Ogt knockdown had 4 FDR<0.05 genes versus 311 for Gfpt1; in 155, Ogt knockdown had 536 FDR<0.05 genes led by Xpo1/Rsrp1 rather than Hspa5/Sdf2l1; in Pvalb, Ogt knockdown had 109 FDR<0.05 genes whereas Gfpt1 had zero."}
{"target_gene": "Gfra1", "evidence_id": "E009", "cell_type": null, "statistics": "gene_target filters returned zero rows for Gdnf, Gfra2, Gfra3, Gfra4, Nrtn, Artn, and Pspn; Ret was profiled in 23 cell types with 0 total genes at FDR<0.1, and its best own-transcript row was 215 MB Dopa with 23 perturbed cells, score -4.44, p=9.20e-6, FDR=0.149."}
{"target_gene": "Gli1", "evidence_id": "E007", "cell_type": null, "statistics": "154 all-gene Pearson correlations between Gli1 and related perturbations across matched cell types; mean absolute r=0.0227; maximum absolute r=0.1277 for Gli1 versus Ptch1 in 217 P MY Pineal Glut."}
{"target_gene": "Glis2", "evidence_id": "E003", "cell_type": null, "statistics": "388046 gene-by-cell-class tests for Glis2; FDR<0.05: 0; FDR<0.10: 0; minimum FDR=0.279; 119 tests had nominal p<0.001."}
{"target_gene": "Gpr158", "evidence_id": "E008", "cell_type": null, "statistics": "Gpr179 perturbations contributed 371818 rows across 22 cell types; no row for any gene had FDR<0.1, the minimum row FDR was 0.2816, and every exact Gpr179 target-transcript row had FDR=1.0."}
{"target_gene": "Gpr161", "evidence_id": "E007", "cell_type": null, "statistics": "In 001 L5-6 IT Glut, the strongest non-self positive and negative full-vector correlations to Gpr161 were Tbr1 r=0.202 and Atp13a3 r=-0.171; in 217 P MY Pineal Glut they were Rubcn r=0.138 and Ndufb9 r=-0.126; in 027 NP-CT-L6b-OB Glut the top positive was Grik4 r=0.062."}
{"target_gene": "Gria3", "evidence_id": "E005", "cell_type": "308 CB GABA", "statistics": "42 perturbed cells versus 8,277 controls; Gria3 logFC +0.033, p = 0.963, FDR = 1.0; 0/16,945 genes had FDR < 0.1. The top nominal genes were Grik4 logFC +0.876, FDR = 0.833; Cadm3 logFC -0.890, FDR = 0.833; and Tbx1 logFC +1.519, FDR = 0.833."}
{"target_gene": "Grik5", "evidence_id": "E009", "cell_type": "001 L5-6 IT Glut", "statistics": "Across 88 Grik1-Grik4 measured rows inside the 22 Grik5 contrasts, all had FDR=1.0. Strongest same-family nominal response was Grik4 in 001 L5-6 IT Glut: 47 perturbed cells, logFC 0.901642, score 3.952532, p=7.73e-05, FDR=1.0; the same contrast had Grik5 logFC -0.190989, p=0.194532, FDR=1.0."}
{"target_gene": "Grm7", "evidence_id": "E007", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "After Grm7 perturbation, Elfn1 logFC 0.513, score 0.198, p=0.843, FDR=1.0; Elfn2 logFC -0.316, score -2.077, p=0.0378, FDR=1.0; Pick1 logFC -0.031, score -0.153, p=0.879, FDR=1.0; Gprasp1 logFC -0.125, score -1.809, p=0.0705, FDR=1.0."}
{"target_gene": "Hdx", "evidence_id": "E001", "cell_type": null, "statistics": "Hdx transcript rows were present in 22 Hdx-tested cell types; n_perturbed=22-139 and n_control=3465-23679. Hdx logFC median -0.159, range -1.585 to 0.264; 16/22 logFC values were negative; every on-target Hdx row had pvals_adj=1.0, with the smallest nominal p=0.0707 in 007 L2-3 IT CTX Glut."}
{"target_gene": "Htr6", "evidence_id": "E002", "cell_type": null, "statistics": "388046 Htr6 DE rows across 23 classes; 0 rows with q<0.05; 1 row with q<0.1; 103 rows with nominal p<0.001 spanning 102 genes; only Sh3gl2 recurred at p<0.001 and flipped sign."}
{"target_gene": "Il31ra", "evidence_id": "E002", "cell_type": null, "statistics": "Il31ra target row present in 22/22 Il31ra contrasts; pvals_adj=1.0 in all; Wilcoxon score range -0.0959 to 0.9412; nominal p-value range 0.3466 to 0.9985."}
{"target_gene": "Jarid2", "evidence_id": "E006", "cell_type": null, "statistics": "217 P MY Pineal Glut had 35 perturbed cells and Amfr logFC 0.8431, p=1.4e-05, pvals_adj=0.233908; 215 MB Dopa had 21 perturbed cells and Trps1 logFC 1.1762, p=1.5e-05, pvals_adj=0.245798; the remaining top rows in these two cell types had pvals_adj=1.0."}
{"target_gene": "Kat6a", "evidence_id": "E011", "cell_type": "017 CA3 CA2-FC DG Glut", "statistics": "58 Kat6a cells versus 8620 controls; Rspo2 score -0.278 logFC -0.269 p=0.781 FDR=1.0; Ctnnb1 score -0.690 FDR=1.0; Axin2 score -0.215 FDR=1.0; Trp53 score -0.631 FDR=1.0; Mdm2 score -0.184 FDR=1.0; Cdkn1a score -0.247 FDR=1.0."}
{"target_gene": "Kcnab2", "evidence_id": "E010", "cell_type": null, "statistics": "In the five FDR-significant Kcnab2 cell types, Pearson score correlations versus Kcnab2 were near zero: Kcnab1 r=0.005 to 0.050, Kcna1 r=-0.001 to 0.052, and Kcna2 r=-0.026 to 0.042."}
{"target_gene": "Kcnc2", "evidence_id": "E001", "cell_type": "052 Pvalb Gaba", "statistics": "72 perturbed cells versus 13710 controls; Kcnc2 score -5.657, logFC -0.752, p=1.54e-08, FDR=2.59e-04."}
{"target_gene": "Kcnj6", "evidence_id": "E001", "cell_type": null, "statistics": "23 cell types; 388,046 Kcnj6 DE rows; n_pert_matched 20-226, median 78; 0 rows at FDR<0.05 and 0 rows at FDR<0.10; best transcriptome-wide FDR=0.254 in 005 L4-5 IT CTX Glut."}
{"target_gene": "Kdm4b", "evidence_id": "E004", "cell_type": "155 MB Glut", "statistics": "258 perturbed cells versus 20,353 controls; 2 non-target genes had nominal p<0.001; 0 genes had pvals_adj <0.10; Kdm4b logFC -0.645 score -3.270 p=0.00108 q=1.0; Urgcp logFC 0.330 p=0.000535 q=1.0; Oprl1 logFC -0.347 p=0.000709 q=1.0."}
{"target_gene": "Kdm5b", "evidence_id": "E002", "cell_type": null, "statistics": "Strongest own-transcript rows: 022 L5 ET CTX Glut, 72 perturbed vs 8,644 controls, logFC -0.369, score -3.726, p=1.95e-4, rank 1/17,009 by p; 155 MB Glut, 164 vs 20,353, logFC -0.363, p=5.88e-4, rank 2/17,443; 052 Pvalb Gaba, 125 vs 13,710, logFC -0.392, p=8.89e-4, rank 4/16,762; 145 MH-LH TH Glut, 65 vs 6,961, logFC -0.597, p=0.00152, rank 8/16,707. All four had pvals_adj=1.0."}
{"target_gene": "Kdm6a", "evidence_id": "E002", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "176 perturbed cells versus 23679 controls across 17259 genes; 1 gene FDR<0.05 and 17 genes p<0.001. Ntng1 logFC 0.1596, score 4.772, p=1.83e-6, FDR 0.0315; Nell1 logFC 0.2157, FDR 0.1218; Ptpn5 logFC -0.3177, FDR 0.1218; Cyp46a1 logFC -0.1606, FDR 0.1296."}
{"target_gene": "Klc2", "evidence_id": "E009", "cell_type": null, "statistics": "12 of 22 Klc2-profiled cell types had Klc2 self-row FDR=1.0; n_pert_matched ranged from 35 to 78 and Klc2 scores ranged from -3.492 to +1.032."}
{"target_gene": "Kpna3", "evidence_id": "E004", "cell_type": "054 CNU-MGE GABA", "statistics": "26 perturbed cells versus 7679 controls; Txnl4a logFC 1.193, score 4.759, p=1.94e-6, FDR=0.033; Kpna3 logFC -0.756, p=0.0181, FDR=1.0; this was the only Kpna3 row with FDR<0.05."}
{"target_gene": "Lgals3", "evidence_id": "E006", "cell_type": null, "statistics": "Cosine similarity of Lgals3 score vectors to related perturbations was near zero by target: mean cosines 0.002-0.018 for listed targets; the largest absolute related cosine was Cd36 in 308 CB GABA at 0.233, followed by Itgb2 in 308 CB GABA at 0.155 and Cx3cr1 in 308 CB GABA at 0.111."}
{"target_gene": "Lmbr1", "evidence_id": "E009", "cell_type": null, "statistics": "Lmbr1l/Lmbrd1/Lmbrd2 rows under Lmbr1 perturbation: 57 rows, minimum p=0.0132 for Lmbrd2 in 145 MH-LH TH Glut, FDR=1.0; Rnf32/Bhlha9/Nom1/Mnx1/En2/Wnt8b rows: 104 rows, no p<0.05 and all FDR=1.0."}
{"target_gene": "Lpar6", "evidence_id": "E002", "cell_type": null, "statistics": "355,046 Lpar6 gene-level tests across 21 cell groups; 0 genes at FDR<0.10 and 0 at FDR<0.05. The global minimum adjusted p value was 0.210 and the maximum absolute Wilcoxon score was 4.364; each cell type had only 1-9 genes with nominal p<0.001."}
{"target_gene": "Lrp4", "evidence_id": "E004", "cell_type": null, "statistics": "Strong non-significant nominal peaks were Wdfy3 in 009 L2-3 IT PIR AON ENT Glut, score -4.378820, logFC -0.586909, p=1.19324e-05, FDR=0.205070; Vps35 in 053 Sst Gaba, score 4.169475, logFC 0.814343, p=3.05302e-05, FDR=0.501550; and Ell in 059 CNU-LGE LSX GABA, score -4.017924, logFC -1.582550, p=5.87131e-05, FDR=0.971056."}
{"target_gene": "Lrrtm1", "evidence_id": "E006", "cell_type": null, "statistics": "Among measured partner or compensation-candidate genes in Lrrtm1-guide cells, none had FDR<0.05 in any of 22 cell classes. Minimum p/FDR values included Cadm1 p=0.0423/FDR=1.0, Lrrtm2 p=0.654/FDR=1.0, Lrrtm3 p=0.0634/FDR=1.0, Lrrtm4 p=0.0352/FDR=1.0, Nrxn1 p=0.0189/FDR=1.0, and Nlgn3 p=0.0416/FDR=1.0."}
{"target_gene": "Mafb", "evidence_id": "E001", "cell_type": null, "statistics": "22 Mafb-assayed cell classes; 25-197 perturbed cells per class (median 65) versus 3465-23679 matched controls. Mafb target row was present in all 22 classes; on-target FDR=1.0 in every class; smallest on-target nominal p=0.0584; Wilcoxon scores ranged from -1.43 to 1.89."}
{"target_gene": "Mchr1", "evidence_id": "E008", "cell_type": null, "statistics": "Among 2038 non-Mchr1 perturbations with >100000 shared features, target-wide Wilcoxon-score correlations ranged from -0.013 to 0.030; the top positive neighbor was Ndufb9 r=0.0297 and Adora2a was r=0.0282. The strongest within-cell positive neighbor was Adora2a in 012 MEA LA CA1 DG Glut with r=0.218 and 0 FDR < 0.05 rows for that Adora2a context."}
{"target_gene": "Mecr", "evidence_id": "E005", "cell_type": null, "statistics": "Across all 388046 Mecr rows, 1 row passed FDR <0.05; 89 rows passed p<0.001, representing 89 unique genes with no gene recurring at p<0.001 in more than one cell type."}
{"target_gene": "Med15", "evidence_id": "E001", "cell_type": null, "statistics": "Med15 transcript was measured in 22 Med15 contrasts; 16/22 logFC estimates were negative; 5/22 were nominal p<0.05, comprising 4 negative and 1 positive; 0/22 were FDR<0.05. In 151 TH Prkcd Grin2c Glut, Med15 itself had logFC -0.0839, score -0.697, p=0.486, FDR=1.0."}
{"target_gene": "Mest", "evidence_id": "E007", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Mest: 164 perturbed/23,679 control cells, 0 FDR < 0.05 genes, best FDR 0.215. Ctnnb1: 171 perturbed/23,679 control cells, 383 FDR < 0.05 genes, minimum FDR 3.55e-25. The Mest-Ctnnb1 score correlation in this cell type was r = -0.003."}
{"target_gene": "Minar2", "evidence_id": "E007", "cell_type": null, "statistics": "Across their assayed rows, Tsc1 had 1,162 FDR<0.05 genes and Tsc2 had 423; Mtor had 2, Rptor had 0, Akt3 had 0, Notch1 had 1, Notch2 had 0, Notch3 had 0, and Notch4 had 1."}
{"target_gene": "Ncapd3", "evidence_id": "E003", "cell_type": null, "statistics": "The Ncapd3 transcript was measured in all 22 tested classes; 20/22 logFC values were negative; median logFC -0.172; range -0.798 to +0.561; 9/22 self rows had nominal p<0.05; all self rows had FDR=1.0."}
{"target_gene": "Nefh", "evidence_id": "E005", "cell_type": null, "statistics": "371796 non-Nefh rows across 22 cell types; 0 rows had FDR < 0.05 or FDR < 0.10. Best non-target rows: Ap4e1 in 005 L4-5 IT CTX Glut logFC 0.697801 score 4.321463 p 1.549979e-05 FDR 0.265387; Lmbrd1 in 022 L5 ET CTX Glut logFC -0.389738 score -4.179902 p 2.916350e-05 FDR 0.496042; Actr3b in 052 Pvalb Gaba logFC -0.868764 score -4.005685 p 6.183804e-05 FDR 0.518265."}
{"target_gene": "Nefl", "evidence_id": "E009", "cell_type": null, "statistics": "For each listed NMDA/PSD/MAPK transcript, the minimum FDR across all Nefl cell types was 1.0. Best nominal p values included Grin1 p=0.00172, Grin2c p=0.0225, Dlg4 p=0.0223, Camk2a p=0.0393, Mapk1 p=0.0495, Raf1 p=0.248, and Mapk3 p=0.190."}
{"target_gene": "Nf1", "evidence_id": "E002", "cell_type": null, "statistics": "Nf1 transcript logFC was negative in 21 of 22 measured classes; six classes had nominal Nf1 p < 0.01, led by 052 Pvalb Gaba logFC -0.562 p=0.000255, 151 TH Prkcd Grin2c Glut logFC -0.352 p=0.001541, 054 CNU-MGE GABA logFC -0.530 p=0.004939, 110 CNU-HYa HY MM Glut logFC -0.507 p=0.006087, 155 MB Glut logFC -0.339 p=0.008285, and 053 Sst Gaba logFC -0.534 p=0.009938; no Nf1 target-transcript row had FDR < 0.05."}
{"target_gene": "Nfat5", "evidence_id": "E010", "cell_type": null, "statistics": "Within the 20 cell types with both perturbations, Pearson correlations between the Nfat5 score vector and the Nfatc3 score vector ranged from -0.0408 to +0.0794, with the maximum in 308 CB GABA; all absolute correlations were <0.08."}
{"target_gene": "Nkx6-2", "evidence_id": "E001", "cell_type": null, "statistics": "Nkx6-2 had 371,818 DE rows across 22 group_name values; all 22 Nkx6-2 groups were annotated Glut or GABA; 215 MB Dopa was present in the parquet but had no Nkx6-2 rows."}
{"target_gene": "Nr1h2", "evidence_id": "E001", "cell_type": null, "statistics": "Nr1h2 transcript was present in 23/23 cell-type result tables; target-row logFC range -1.269 to +0.812; all target-row pvals_adj = 1.0; smallest nominal target p was 0.0493 in 053 Sst Gaba with logFC +0.812, and the largest negative target row was 017 CA3 CA2-FC DG Glut with logFC -1.269, p=0.0821, FDR=1.0."}
{"target_gene": "Ogfrl1", "evidence_id": "E006", "cell_type": null, "statistics": "The top five nominal genes from each of 22 cell types yielded 110 gene entries with no repeated gene name; among top-10 lists only Odf2 recurred, twice; among top-20 lists the maximum recurrence for any gene was 2 cell types."}
{"target_gene": "Or51e2", "evidence_id": "E003", "cell_type": null, "statistics": "Or51e2 was observed in 18 of 23 cell classes, with 704 perturbed cells total; n_pert_matched ranged from 20 to 84 cells per class, median 35.5. The five classes without an Or51e2 contrast were 001 L5-6 IT Glut, 110 CNU-HYa HY MM Glut, 145 MH-LH TH Glut, 215 MB Dopa, and 217 P MY Pineal Glut."}
{"target_gene": "Orc4", "evidence_id": "E007", "cell_type": null, "statistics": "Filtering gene_target for ORC1-6, CDC6, CDT1, MCM2-7, MCM8-10, CDC45, GINS1-4, CDC7, DBF4, and DBF4B returned only Orc4 and Orc6. Orc6 contributed 371,818 rows across 22 cell types, had 0 rows at FDR<0.05, min pvals_adj 0.397, and only 2/22 nominal Orc6 self rows at p<0.05."}
{"target_gene": "Pax7", "evidence_id": "E004", "cell_type": "022 L5 ET CTX Glut", "statistics": "In 102 Pax7-perturbed cells, the strongest non-Ruvbl1 nominal positive rows were Wnk2 logFC 0.269661, p=6.04e-5, FDR=0.513356; Atp8a2 logFC 0.305094, p=1.43e-4, FDR=0.633309; P4ha2 logFC 0.475649, p=2.19e-4, FDR=0.633309. The strongest negative rows were Ahcyl1 logFC -0.257088, p=1.70e-4, FDR=0.633309; Itfg1 logFC -0.424515, p=2.23e-4, FDR=0.633309; Ncan logFC -0.314008, p=3.85e-4, FDR=0.697379; Fth1 logFC -0.428630, p=3.98e-4, FDR=0.697379."}
{"target_gene": "Pbx3", "evidence_id": "E008", "cell_type": null, "statistics": "017 CA3 CA2-FC DG Glut: Grin1 score 4.333, logFC 0.337, p=1.46e-5, p_adj=0.251, rank 1 in that cell type and lowest nominal p across all Pbx3 rows. 155 MB Glut: Grin1 score -3.270, logFC -0.153, p=0.00108, p_adj=1.0."}
{"target_gene": "Pcsk2", "evidence_id": "E008", "cell_type": null, "statistics": "151 TH Prkcd Grin2c Glut, 155 MB Glut, and 007 L2-3 IT CTX Glut each had Pcsk2 as the sole FDR<0.1 gene despite Pcsk2 FDR values of 1.19e-28, 2.49e-16, and 1.38e-6, respectively."}
{"target_gene": "Peg3", "evidence_id": "E001", "cell_type": null, "statistics": "Peg3 perturbation was detected in 22 cell types; Peg3 rows were negative in 22/22, nominal p<0.05 in 17/22, and dataset FDR<0.05 in 8/22; median Peg3 logFC -0.488, strongest logFC -1.059 in 110 CNU-HYa HY MM Glut."}
{"target_gene": "Peg3", "evidence_id": "E003", "cell_type": null, "statistics": "Five Peg3 target rows were not nominally significant: 017 CA3 CA2-FC DG Glut score -1.697, logFC -0.214, p=0.0898; 059 CNU-LGE LSX GABA score -1.214, logFC -0.266, p=0.225; 008 L2-3 IT ENT PPP RSP Glut score -1.166, logFC -0.156, p=0.244; 009 L2-3 IT PIR AON ENT Glut score -1.074, logFC -0.135, p=0.283; 001 L5-6 IT Glut score -0.929, logFC -0.132, p=0.353."}
{"target_gene": "Peg3", "evidence_id": "E004", "cell_type": null, "statistics": "Among 371,796 non-Peg3 rows from Peg3 perturbation contrasts, exactly one row had pvals_adj<0.05: Gpx3 in 110 CNU-HYa HY MM Glut with score 4.614, logFC 1.228, p=3.95e-6, FDR 0.0339."}
{"target_gene": "Pkd1", "evidence_id": "E002", "cell_type": null, "statistics": "355,046 Pkd1 differential-expression rows across 21 cell types; 0 genes with FDR < 0.05; global minimum FDR 0.4746 for Slc25a23 in 046 CTX-CGE GABA; maximum absolute Wilcoxon score 4.182."}
{"target_gene": "Plxnd1", "evidence_id": "E001", "cell_type": null, "statistics": "371,818 Plxnd1-perturbation rows across 22 cell types; 57-279 perturbed cells and 3,465-23,679 matched controls per cell type; 0 genes at FDR<=0.05 or FDR<=0.10, and 1/371,818 genes at FDR<=0.25."}
{"target_gene": "Pou6f1", "evidence_id": "E004", "cell_type": null, "statistics": "151 TH Prkcd Grin2c Glut had 226 perturbed cells and no FDR < 0.05 rows; Pou6f1 logFC 0.037, p 0.986, FDR 1.0. 155 MB Glut had 209 perturbed cells and no FDR < 0.05 rows; Pou6f1 logFC 0.241, p 0.171, FDR 1.0."}
{"target_gene": "Pparg", "evidence_id": "E006", "cell_type": null, "statistics": "Across assayed classes, Ppara had 0 FDR<0.05 groups, Ppard 0, Rxra 0, Rxrb 0, and Rxrg 0; each target was present in 22-23 cell classes."}
{"target_gene": "Ppp2r2b", "evidence_id": "E008", "cell_type": null, "statistics": "Across matched genes within each cell type, Ppp2r2b:Ppp2r1a score correlations averaged r = 0.001 across 22 cell types with range -0.072 to 0.067; Ppp2r2b:Ppp2r5d averaged r = 0.010 with range -0.058 to 0.078."}
{"target_gene": "Prdm5", "evidence_id": "E002", "cell_type": null, "statistics": "388,046 Prdm5 differential-expression rows across 23 cell types; 16,228-17,443 ranked genes per cell type; 0 rows at FDR<0.1 and 0 rows at FDR<0.05; minimum FDR=0.466; 95 rows had nominal p<0.001."}
{"target_gene": "Ptch1", "evidence_id": "E004", "cell_type": null, "statistics": "Within Ptch1 signatures these nine Hedgehog-neighborhood transcripts all had FDR=1.0 in every assayed cell type. Minimum nominal p values by gene were Gli1=0.8567, Gli2=0.7699, Gli3=0.7565, Ptch2=0.4585, Smo=0.5788, Gpr161=0.00754, Cdon=0.0244, Adcy3=0.0634, and Sufu=0.2897."}
{"target_gene": "Ptch2", "evidence_id": "E003", "cell_type": "155 MB Glut", "statistics": "182 Ptch2-guide cells versus 20,353 controls; Ptpn5 score 4.430 logFC 0.454 nominal p=9.4e-06 FDR=0.164; Cep70 score 3.889 logFC 0.329 nominal p=1.01e-04 FDR=0.879; Fzd3 score 3.293 logFC 0.429 nominal p=9.92e-04 FDR=1.0."}
{"target_gene": "Ptpn1", "evidence_id": "E005", "cell_type": null, "statistics": "In the same DE file, Lepr, Insr, Stat3, and Ptpn11 perturbations each produced 0 FDR<0.05 genes across all assayed cell types for that target; their own target-transcript rows were also FDR=1.0 in every measured cell type."}
{"target_gene": "Rgma", "evidence_id": "E007", "cell_type": "217 P MY Pineal Glut", "statistics": "22 perturbed cells versus 3,465 controls; all genes FDR=1.0 despite large nominal effects including Sde2 logFC 1.247 p=1.34e-04, Gopc logFC 1.171 p=1.57e-04, Spred2 logFC -2.660 p=3.06e-04, and Jarid2 logFC -1.167 p=3.81e-04."}
{"target_gene": "Ripor2", "evidence_id": "E006", "cell_type": null, "statistics": "Score-vector correlations were computed within matched cell types over 16428-17443 measured transcripts. Across Rac1, Cdc42, Pak1, Pak2, Pak3, Arhgap18, Arhgap32, and Arhgef9 the largest |r| was 0.095 for Pak3 in 005 L4-5 IT CTX Glut. Across available STRING-neighbor perturbations Rdx, Epb41l1, and Ywhae the largest |r| was 0.096 for Rdx in 017 CA3 CA2-FC DG Glut. Rhoa, Rhoc, Rock1, Rock2, Ripor1, and Ripor3 were absent as gene_target perturbations."}
{"target_gene": "Robo1", "evidence_id": "E002", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "312 perturbed cells versus 23679 controls; Robo1 logFC -0.538, score -6.398, p=1.57e-10, FDR=2.72e-6, rank 1 by absolute score; the strongest non-target genes were P3h3 p=1.03e-4, FDR=0.890 and Hpf1 p=1.67e-4, FDR=0.963."}
{"target_gene": "Rp9", "evidence_id": "E003", "cell_type": "022 L5 ET CTX Glut", "statistics": "56 perturbed cells versus 8644 controls; Rp9 logFC -1.425, nominal p=8.50e-08, FDR=0.00145. Only 1 gene reached FDR<0.10; Bscl2 logFC -0.705, FDR=0.179; Uba5 logFC -0.815, FDR=0.621."}
{"target_gene": "Rpgr", "evidence_id": "E006", "cell_type": "155 MB Glut", "statistics": "88 perturbed cells versus 20353 controls; Clasrp score -3.823156, logFC -0.289556, p = 0.000132, FDR = 1.0; Rpgr logFC 0.043665, p = 0.954430, FDR = 1.0; 11 rows had p < 0.001 and 0 had FDR < 0.10."}
{"target_gene": "S1pr2", "evidence_id": "E008", "cell_type": null, "statistics": "Whole-target score-vector correlations to S1pr2 were Rtn4r r=0.0230, Lingo1 r=0.0033, and Ngfr r=0.0020 across 371,818 shared rows each; Rtn4r had 1 and Lingo1 had 4 FDR<0.05 rows overall, whereas S1pr2 and Ngfr had 0."}
{"target_gene": "Satb2", "evidence_id": "E002", "cell_type": "all 23 assayed cell types", "statistics": "388,046 Satb2 rows across 23 groups; 0 genes with P_adj<0.05. The smallest raw P values were Aatf in 145 MH-LH TH Glut, logFC 1.114, score 4.394, P=1.12e-5, P_adj=0.186; Ermp1 in 052 Pvalb Gaba, P=1.99e-5, P_adj=0.334; Itch in 027 NP-CT-L6b-OB Glut, P=2.24e-5, P_adj=0.374; Scrt1 in 001 L5-6 IT Glut, P=2.76e-5, P_adj=0.474."}
{"target_gene": "Scarb2", "evidence_id": "E010", "cell_type": null, "statistics": "The parquet contained 2,046 unique perturbation targets. Present related targets included Scarb2, Psap, Grn, Cd36, Lamp2, Atp13a2, Ctsb, Rab7 and Vps35; Gba1 and Scarb1 were not present as gene_target values."}
{"target_gene": "Sdccag8", "evidence_id": "E002", "cell_type": "053 Sst Gaba", "statistics": "37 perturbed cells versus 5622 controls; Spast score 4.747, logFC 1.055, p=2.06e-6, FDR=0.0339; in the same signature Sdccag8 score -0.558, logFC -0.141, p=0.577, FDR=1.0."}
{"target_gene": "Shank2", "evidence_id": "E004", "cell_type": null, "statistics": "The Shank2 row had nominal p<0.05 in 13/22 tested cell types. Cells where Shank2 was rank 1 by p value but FDR=1 included 155 MB Glut, 205 cells, logFC -0.491, p=1.63e-4; 191 MB P MY GABA, 134 cells, logFC -0.513, p=3.26e-4; 217 P MY Pineal Glut, 31 cells, logFC -1.163, p=5.03e-4; and 066 CNU-HYa HY GABA, 108 cells, logFC -0.490, p=9.60e-4, down-score rank 2."}
{"target_gene": "Six1", "evidence_id": "E003", "cell_type": null, "statistics": "388,046 Six1 differential-expression rows; 0 rows with FDR<0.05; 12 rows with FDR<1.0; minimum FDR=0.304859; minimum nominal p=1.853e-5."}
{"target_gene": "Smad4", "evidence_id": "E002", "cell_type": null, "statistics": "Smad4 transcript row present in 22/22 signatures; 18/22 logFC values were negative; median logFC -0.204; minimum logFC -0.804 in 008 L2-3 IT ENT PPP RSP Glut; minimum nominal p=0.00366 in 052 Pvalb Gaba; all Smad4 transcript FDR values were 1.0."}
{"target_gene": "Smad4", "evidence_id": "E010", "cell_type": null, "statistics": "Across 17 TGF/BMP/SMAD/SKI targets assayed in the same cell classes, 9 target-cell pairs had at least one gene at FDR<0.05; Bmpr2, Ski, Smad2, Tgfbr2, and Bmpr1b crossed this threshold in at least one cell class, whereas Smad4 crossed it in 0 cell classes."}
{"target_gene": "Smc1a", "evidence_id": "E003", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Ptprm logFC -0.783 FDR 6.39e-07; Spon1 -0.888 FDR 2.01e-05; Sema5a -0.842 FDR 5.83e-04; Slit3 -0.766 FDR 0.00882; Grin2c -0.448 FDR 0.00329; Atp2a2 -0.351 FDR 2.01e-05; Atp2b1 -0.230 FDR 0.00329."}
{"target_gene": "Snx10", "evidence_id": "E002", "cell_type": null, "statistics": "371,818 Snx10 differential-expression rows across 22 cell types; 0 genes at FDR<0.05 or FDR<0.10; minimum FDR=0.300872 and minimum nominal p=1.829e-5."}
{"target_gene": "Sox9", "evidence_id": "E001", "cell_type": null, "statistics": "Twenty-three of 23 tested cell types contained a measured Sox9 row; 0/23 had nominal p<0.05 or FDR<0.05; every Sox9 row had pvals_adj=1.0; nominal p range 0.217-0.985; Wilcoxon score range -0.860 to 1.234; n_pert_matched range 21-252."}
{"target_gene": "Sp110", "evidence_id": "E005", "cell_type": null, "statistics": "054 CNU-MGE GABA had Zscan18 FDR=0.348 and Rtcb FDR=0.441; 001 L5-6 IT Glut had Fchsd2 and Gpatch1 both FDR=0.404; all remaining cell-type minima were FDR>=0.538."}
{"target_gene": "Sptb", "evidence_id": "E003", "cell_type": "066 CNU-HYa HY GABA", "statistics": "59 perturbed cells versus 10110 controls; Raf1 logFC 0.588105 score 4.276751 P=1.89e-5 FDR=0.163071; Gabra2 logFC -1.144329 score -4.275661 P=1.91e-5 FDR=0.163071; Ypel4 logFC 0.492260 P=5.15e-5 FDR=0.293529; Sptb logFC -0.116286 P=0.707295 FDR=1."}
{"target_gene": "Srrm2", "evidence_id": "E012", "cell_type": "217 P MY Pineal Glut", "statistics": "20 perturbed cells versus 3465 controls; Srrm2 logFC -1.623 FDR 4.82e-4; 5 off-target genes at FDR<0.05, including Atxn2l -1.030 FDR 0.00134 and Leng8 -0.809 FDR 0.00304."}
{"target_gene": "Srsf1", "evidence_id": "E009", "cell_type": null, "statistics": "Across full score vectors after excluding Srsf1 self-correlations, Tnpo3 was the top positive Srsf1 signature neighbor in 13 of 21 matched cell types and within the top five in 15 of 21. Pearson correlations included 0.414 in 151 TH Prkcd Grin2c Glut, 0.369 in 191 MB P MY GABA, 0.363 in 155 MB Glut, and 0.257 in 066 CNU-HYa HY GABA; 017 CA3 CA2-FC DG Glut and 059 CNU-LGE LSX GABA had weak correlations of -0.016 and 0.024."}
{"target_gene": "Suco", "evidence_id": "E010", "cell_type": null, "statistics": "In the 21 Suco classes, exact all-gene score correlations with available related perturbations were near zero: max |r| = 0.130 for Col11a1, 0.076 for Col2a1, 0.054 for Fam120a, and 0.054 for Hif1a; Col2a1 had one FDR < 0.05 gene in 017 CA3 CA2-FC DG Glut, and Fam120a and Hif1a had no FDR < 0.05 rows in this related subset."}
{"target_gene": "Tbx2", "evidence_id": "E002", "cell_type": null, "statistics": "388046 Tbx2 differential-expression rows across 23 cell types; 0 genes at FDR<0.05; best adjusted p=0.2176 for Gapvd1 in 007 L2-3 IT CTX Glut with score=-4.360, logFC=-0.584, nominal p=1.30e-5."}
{"target_gene": "Tef", "evidence_id": "E006", "cell_type": "012 MEA LA CA1 DG Glut", "statistics": "59 perturbed cells versus 7030 controls; Tef logFC -0.236 p=0.097 FDR=1.0; top row Rnpepl1 logFC -1.218 p=5.99e-6 FDR=0.101; zero genes with FDR<0.05."}
{"target_gene": "Tfap4", "evidence_id": "E007", "cell_type": null, "statistics": "Among related HLH/E-box perturbations, Max had 167 FDR<0.05 rows with minimum FDR=1.25e-18, Mga had 3 with minimum FDR=1.73e-8, Mnt had 2 with minimum FDR=0.0223, Tcf4 had 2 with minimum FDR=0.00884, and Usf1 had 1 with minimum FDR=0.0255; Myc, Mycn, Tcf3, Tcf12, Mlxip, and Tfap4 had 0 FDR<0.05 rows."}
{"target_gene": "Tpi1", "evidence_id": "E008", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "260 Pgk1-perturbed cells versus 23679 controls; Pgk1 logFC -1.441, FDR=4.43e-32; Pnisr logFC -0.227, FDR=7.00e-11; Rsrp1 logFC -0.217, FDR=5.73e-10; Ogt logFC -0.146, FDR=5.00e-04; 22 genes total had FDR<0.05."}
{"target_gene": "Trmt1", "evidence_id": "E005", "cell_type": null, "statistics": "151 TH Prkcd Grin2c Glut: 232 perturbed cells, Trmt1 logFC -0.220, p=0.010, min FDR=0.460 with Cars as top positive logFC 0.328, FDR=0.460. 155 MB Glut: 181 perturbed cells, Trmt1 logFC -0.254, p=0.020, min FDR=1.0. 191 MB P MY GABA: 117 perturbed cells, Trmt1 logFC -0.309, p=0.0156, min FDR=0.234 with Drg2 FDR=0.234."}
{"target_gene": "Trpm3", "evidence_id": "E006", "cell_type": "308 CB GABA", "statistics": "57 perturbed cells versus 8,277 controls; 16,945 genes tested; 0 genes with FDR < 0.05; min FDR 1.0; top nominal up Fam118a score 3.7896, logFC 0.9074, p 1.51e-4; top nominal down Pogz score -3.7858, logFC -0.9430, p 1.53e-4."}
{"target_gene": "Tsc1", "evidence_id": "E011", "cell_type": null, "statistics": "In full within-cell-type score-vector correlations, Rab7 was the highest non-Tsc2 positive neighbor in 155 MB Glut (r=0.358), 151 TH Prkcd Grin2c Glut (r=0.358), and 191 MB P MY GABA (r=0.296); Rab7 was also positive in 066 CNU-HYa HY GABA (r=0.218) and 110 CNU-HYa HY MM Glut (r=0.205). Mtor was the strongest negative neighbor in 155 MB Glut (r=-0.268), 151 TH Prkcd Grin2c Glut (r=-0.222), and 191 MB P MY GABA (r=-0.162); Rptor was also negative in those classes (r=-0.134, -0.124, and -0.093)."}
{"target_gene": "Tspan12", "evidence_id": "E002", "cell_type": null, "statistics": "388,046 Wilcoxon tests across 23 cell types; 1 gene at FDR<=0.05, 2 at FDR<=0.10, 3 at FDR<=0.20; 110 rows at nominal p<=0.001 and all 110 were distinct genes."}
{"target_gene": "Tuba1a", "evidence_id": "E007", "cell_type": null, "statistics": "Across all 21 Tuba1a contrasts, 16 rows reached FDR<0.05 and all 16 were Tuba1a or Tuba/Tubb genes; at FDR<0.10, the only added non-tubulin row was Copb1 in 151 TH Prkcd Grin2c Glut, logFC 0.478, FDR 0.0961."}
{"target_gene": "Ubr1", "evidence_id": "E001", "cell_type": null, "statistics": "19 Ubr1 perturbation/cell-type signatures; 321225 gene-level Wilcoxon rows; 20-65 matched Ubr1-perturbed cells per cell type, median 23 and IQR 22-29, versus 5622-23679 matched non-targeting controls."}
{"target_gene": "Uchl1", "evidence_id": "E001", "cell_type": null, "statistics": "371818 Uchl1 rows across 22 of 23 group_name classes; Uchl1 target logFC was negative in 22/22 classes, nominal target p<0.005 in 22/22, and target FDR<0.05 in 13/22."}
{"target_gene": "Ufc1", "evidence_id": "E007", "cell_type": null, "statistics": "Across all measured genes, Ufc1-Uba5 Pearson correlations were 0.751 in 151 TH Prkcd Grin2c Glut, 0.515 in 155 MB Glut, and 0.383 in 191 MB P MY GABA. In 151, Uba5 was the top non-self positive neighbor of Ufc1 among 2046 perturbations; Uba5 had 2677 FDR<0.05 genes, and 495 of the 572 Ufc1 FDR genes also passed FDR under Uba5 with the same sign. In 155, 21 of 24 Ufc1 FDR genes overlapped Uba5 with the same sign; in 191, 6 of 18 overlapped with the same sign."}
{"target_gene": "Vps13a", "evidence_id": "E004", "cell_type": "155 MB Glut", "statistics": "81 perturbed cells versus 20353 controls; Vps13a logFC -0.653920, score -3.489654, p=0.000484, FDR=1.0 and was the most negative gene; Idh3a score 3.878631, p=0.000105, FDR=1.0; Drosha score -3.436270, p=0.000590, FDR=1.0."}
{"target_gene": "Vps37a", "evidence_id": "E003", "cell_type": "155 MB Glut", "statistics": "58 perturbed cells versus 20353 controls; 138 FDR<0.05 genes. Top examples: Rhoq logFC 1.678 FDR 8.59e-06; Ly6h logFC -1.283 FDR 2.36e-04; Atp6v0b logFC 0.541 FDR 3.84e-04; Ddit3 logFC 1.759 FDR 6.43e-04; Tnfrsf12a logFC 2.451 FDR 0.00107; Kifc2 logFC -0.777 FDR 0.00107; Jun logFC 1.705 FDR 0.00373; Atp6v1h logFC 0.848 FDR 0.00918."}
{"target_gene": "Vps41", "evidence_id": "E005", "cell_type": "191 MB P MY GABA", "statistics": "84 perturbed cells versus 10309 controls; Dpp7 logFC 0.792 score 5.091 p=3.56e-7 FDR 0.00609; Vps41 logFC -0.723 p=5.45e-5 FDR 0.253; Insig1 0.657 p=3.77e-5; Atp6v1b2 0.260 p=2.83e-4; Gm2a 0.733 p=3.61e-4; Fdps 0.715 p=6.62e-4; Atp6v0b 0.222 p=7.53e-4; Srebf2 0.382 p=3.43e-3; Mcoln1 0.297 p=6.55e-3."}
{"target_gene": "Wdr26", "evidence_id": "E009", "cell_type": null, "statistics": "At FDR<0.05, Kcna2 and Hnrnpu recurred in 5/5 responsive groups; Srrm2, Nat8l, Kpna1, Luc7l2, Eif4g3, Dync1h1, Lrp1 and Zfp57 recurred in 4/5. Among the recurrent genes, 30 were always down and 60 were always up across the cell types in which they were significant."}
{"target_gene": "Ywhae", "evidence_id": "E010", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Braf perturbation, 137 perturbed cells: Vgf FDR=1.39e-4 logFC=-0.795, Ptpn5 FDR=1.39e-4 logFC=-0.635, Atp2a2 FDR=1.39e-4 logFC=-0.263, Unc13a FDR=0.00393 logFC=-0.315. Ywhae perturbation, 157 perturbed cells: the same genes all FDR=1.0 with p=0.783, 0.257, 0.0446, and 0.149, respectively."}
{"target_gene": "Zbtb24", "evidence_id": "E009", "cell_type": null, "statistics": "Exact gene_target filters returned 0 rows for Cdca7, Hells, Dnmt3b, Dnmt1, Tet1, Tet2, and Tet3; Dnmt3a and Mecp2 were present comparator perturbations in the Zbtb24-tested cell classes."}
{"target_gene": "Zbtb38", "evidence_id": "E006", "cell_type": null, "statistics": "Outside 151 TH Prkcd Grin2c Glut, Msra was measured in 21 signatures with pvals_adj=1.0 for every test; the smallest outside nominal p was 0.00744 in 007 L2-3 IT CTX Glut, and outside scores ranged from -1.795 to 2.677."}
{"target_gene": "Zfat", "evidence_id": "E003", "cell_type": "155 MB Glut", "statistics": "174 perturbed cells versus 20353 controls; 17443 genes tested; only 2 genes with FDR<0.1: Zfat logFC 0.971 score 4.933 p=8.08e-07 FDR=0.0141; D6Wsu163e logFC -0.931 score -4.595 p=4.33e-06 FDR=0.0378."}
{"target_gene": "Zfat", "evidence_id": "E010", "cell_type": null, "statistics": "Zfat versus Setd1a perturbation score-vector correlations were r=-0.019 in 151 TH Prkcd Grin2c Glut and r=-0.0017 in 155 MB Glut. D6Wsu163e was also down after Setd1a perturbation: logFC -0.538 FDR 0.0746 in 151 and logFC -1.500 FDR 2.39e-06 in 155."}
{"target_gene": "Zfp106", "evidence_id": "E004", "cell_type": "217 P MY Pineal Glut", "statistics": "24 perturbed cells versus 3465 controls; Zfp106 logFC -0.809368, p=0.029766, FDR=1.0; Palm logFC 1.021891, p=0.000005, FDR=0.092034; Mat2b logFC 1.184185, p=0.000133, FDR=0.633731; Auts2 logFC -1.222486, p=0.000134, FDR=0.633731; Zfc3h1 logFC -0.930941, p=0.000223, FDR=0.633731."}
{"target_gene": "Zfp322a", "evidence_id": "E003", "cell_type": null, "statistics": "High-count examples all had 0 FDR-significant genes: 151 TH Prkcd Grin2c Glut, 215 perturbed cells; 155 MB Glut, 183; 005 L4-5 IT CTX Glut, 141; 052 Pvalb Gaba, 121; 009 L2-3 IT PIR AON ENT Glut, 99. The best rows were Mib2 in 005 with score 4.245, logFC 0.388, p = 2.2e-5, FDR = 0.373635 and Senp2 in 052 with score 4.221, logFC 0.556, p = 2.4e-5, FDR = 0.407478."}
{"target_gene": "Zic1", "evidence_id": "E005", "cell_type": null, "statistics": "Across 23 Zic1 contrasts, FDR<0.05 occurred for 2 genes total, both in 151 TH Prkcd Grin2c Glut; 151 had 29 genes with p<0.001, while every other cell group had 0 FDR<0.05 genes and 1 to 9 genes with p<0.001; the minimum non-151 FDR was 0.494."}
