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

**Output.** Write exactly one file: `C:/Dev/Corpus Audit/_internal/records/prereg/H1_annotation_sample1_A.jsonl`, UTF-8, exactly 150 lines, one JSON
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

{"target_gene": "Add3", "evidence_id": "E008", "cell_type": null, "statistics": "Among 1,511-2,046 non-Add3 perturbations per Add3-tested cell type, the largest absolute Pearson correlation to the Add3 score vector was 0.1497; in 053 Sst Gaba the best positive neighbor was Cd3g at r=0.0657 and the best negative neighbor was Ikzf3 at r=-0.0451."}
{"target_gene": "Aimp1", "evidence_id": "E001", "cell_type": null, "statistics": "371,818 Aimp1-target DE rows across 22 cell classes; 34-199 perturbed cells per class, median 66.5; 15/22 classes had fewer than 70 Aimp1-perturbed cells."}
{"target_gene": "Akap9", "evidence_id": "E010", "cell_type": null, "statistics": "In related contrasts, Ppp2r1a yielded 3,147 FDR<0.05 rows across cell types, including 1,292 in 151 TH Prkcd Grin2c Glut and 476 in 155 MB Glut; Ppp2r1a target FDR was 2.28e-44 in 151 TH and 5.34e-32 in 155 MB Glut; Prkaca target FDR was 7.34e-24 in 191 MB P MY GABA and 1.25e-22 in 155 MB Glut."}
{"target_gene": "Alk", "evidence_id": "E012", "cell_type": null, "statistics": "A scan of 44,133 group-target pairs across the parquet found 0 gene_target entries for Ltk, Alkal1, Alkal2, Ptn, or Mdk; downstream/pathway comparators were present, including Kras in 20 Alk-overlapping cell types, Pik3ca in 21, Pik3r1 in 19, Mapk1 in 21, Ptpn11 in 21, and Sos1 in 21."}
{"target_gene": "Alx1", "evidence_id": "E001", "cell_type": null, "statistics": "Alx1 had 321,156 Wilcoxon rows across 19 of 23 cell groups; n_pert_matched ranged from 22 to 86 and matched non-target controls ranged from 5,622 to 23,679."}
{"target_gene": "Amfr", "evidence_id": "E003", "cell_type": "191 MB P MY GABA", "statistics": "49 perturbed cells versus 10309 controls; Amfr score -4.509, logFC -1.215, p=6.50e-06, FDR=0.111."}
{"target_gene": "Ap2m1", "evidence_id": "E007", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Ap2s1 perturbation used 310 perturbed cells versus 23679 controls; Ap2s1 logFC -0.536 FDR 6.33e-05; 1152 genes were FDR<0.05. Across the 139 Ap2m1 FDR genes, the Ap2m1-Ap2s1 Pearson score correlation was 0.920; 121/139 were also FDR<0.05 after Ap2s1 perturbation and all 121 had the same sign. Ap2s1 Tfrc logFC 0.984 FDR 3.06e-24; Mical2 logFC -1.227 FDR 2.95e-52; Prkcb logFC -1.015 FDR 2.13e-48."}
{"target_gene": "Arhgef9", "evidence_id": "E009", "cell_type": null, "statistics": "Among all non-Arhgef9 perturbations using the Arhgef9 top-200 non-target genes, strongest positive/negative correlations were 110: Bmpr2 r=0.337 and Il6ra r=-0.295; 151: Tbce r=0.354 and Ngfr r=-0.264; 155: Pou3f4 r=0.295 and Safe_target_46 r=-0.232."}
{"target_gene": "Arih1", "evidence_id": "E008", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "In 151 TH Prkcd Grin2c Glut, Arih1 and Cul3 perturbations shared 3 of their top 50 absolute-score genes, 11 of their top 100, and 27 of their top 200; 26/27 of the top-200 overlaps had the same score sign. Cul3 had 1 FDR<0.05 gene in this cell type; the Cul3 self-transcript had logFC -0.408, p=0.00133, FDR 0.656."}
{"target_gene": "Armc9", "evidence_id": "E004", "cell_type": null, "statistics": "Nominal Armc9 p<0.05 target rows occurred in 052 Pvalb Gaba: logFC -0.392, p=0.00489; 005 L4-5 IT CTX Glut: logFC -0.266, p=0.0199; 054 CNU-MGE GABA: logFC -0.410, p=0.0305; 022 L5 ET CTX Glut: logFC -0.407, p=0.0314; 059 CNU-LGE LSX GABA: logFC -0.386, p=0.0362; all five had 0 FDR<0.10 genes."}
{"target_gene": "Arsb", "evidence_id": "E001", "cell_type": null, "statistics": "Arsb was measured in 23/23 Arsb-perturbed cell types; Arsb logFC was negative in 23/23; 18/23 had nominal p<0.05, 9/23 had p<0.001, and 5/23 had pvals_adj<0.05; median target logFC=-0.866."}
{"target_gene": "Atf6", "evidence_id": "E006", "cell_type": null, "statistics": "Manf perturbation produced FDR<0.05 Hspa5 up-regulation in 8 cell types. Examples: 155 MB Glut, 192 perturbed cells: Hspa5 logFC +0.879/FDR=2.43e-14, Dnajb9 +0.779/FDR=9.41e-5, Hyou1 +0.506/FDR=1.95e-4, Pdia6 +0.533/FDR=2.48e-4, Sdf2l1 +1.379/FDR=3.73e-5; 054 CNU-MGE GABA, 81 perturbed cells: Hspa5 +0.818/FDR=1.77e-6, Hyou1 +0.724/FDR=0.00234, Ppib +0.470/FDR=0.0166, Rpn1 +0.506/FDR=0.0373."}
{"target_gene": "Atg5", "evidence_id": "E005", "cell_type": "308 CB GABA", "statistics": "39 perturbed cells versus 8,277 controls. Ccnk logFC +1.050, p=1.16e-5, FDR=0.197; Atg5 logFC -0.886, p=0.0747, FDR=1.0; zero genes reached FDR<0.10."}
{"target_gene": "Atp2b2", "evidence_id": "E007", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Atp2a2 perturbation: n=98, Atp2a2 logFC -1.256338 FDR 1.780900e-19 and 186 non-target FDR genes in this cell type, including Hspa5 +0.749096 FDR 1.953462e-06, Ddit3 +1.603674 FDR 2.058184e-08, Xbp1 +0.785159 FDR 3.004919e-07, Chac1 +3.013680 FDR 6.612620e-08, Asns +0.866488 FDR 3.080109e-06, Slc7a5 +1.975921 FDR 0.001754, Sesn2 +2.390634 FDR 0.000326, and Trib3 +3.684104 FDR 0.037283. All listed genes had pvals_adj = 1.0 after Atp2b2 knockdown in the same cell type."}
{"target_gene": "Atp2c1", "evidence_id": "E001", "cell_type": null, "statistics": "371818 Atp2c1 DE rows across 22 cell types; Atp2c1 transcript measured in all 22; Atp2c1 score negative in 21/22; nominal target P<0.05 in 13/22; target FDR<0.05 in 2/22; n_pert_matched range 39-211 and n_ctrl_matched range 3465-23679."}
{"target_gene": "Atp6v1b2", "evidence_id": "E002", "cell_type": "052 Pvalb Gaba", "statistics": "64 perturbed versus 13,710 control cells; 9 genes at FDR<0.05. Atp6v1b2 logFC -0.694, score -5.885, p=3.98e-09, FDR=6.67e-05; Hcn3 logFC 0.994, FDR=0.00273; Dusp1 logFC 1.139, FDR=0.0114; Serpini1 logFC -0.727, FDR=0.0323; Scg2 logFC 0.861, FDR=0.0340; Gadd45g logFC 1.871, FDR=0.0402; Slc6a17 logFC 0.473, FDR=0.0490; Ptprn logFC 0.545, FDR=0.0490; Lpcat1 logFC 1.007, FDR=0.0490."}
{"target_gene": "Atp9a", "evidence_id": "E008", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Using the top 200 non-Atp9a genes by absolute Wilcoxon score, the largest positive Pearson correlations across 2045 comparator perturbations were Kif21a r=0.407 and Kctd16 r=0.395; Safe_target_4 was in the top 10 at r=0.354; the most negative was Atp6v0c r=-0.356."}
{"target_gene": "Bcl11a", "evidence_id": "E002", "cell_type": null, "statistics": "Bcl11a transcript logFC was negative in 17/22 measured cell types; mean logFC -0.188; only 027 NP-CT-L6b-OB Glut reached nominal p=0.00228, logFC -0.390, score -3.05, FDR=1.0, and 008 L2-3 IT ENT PPP RSP Glut reached nominal p=0.0234, logFC -0.218, score -2.27, FDR=1.0; all 22 on-target FDR values were 1.0."}
{"target_gene": "Bin1", "evidence_id": "E001", "cell_type": null, "statistics": "388046 Bin1-target rows across 23 group_name strata; 2262 total perturbed cells versus 213511 matched controls when summed across strata; Bin1 transcript measured in all 23 strata; target row p<0.05 in 13/23, p<0.01 in 10/23, p<0.001 in 7/23, and FDR<0.05 in 3/23."}
{"target_gene": "Bmpr2", "evidence_id": "E001", "cell_type": null, "statistics": "371,818 Bmpr2-perturbation rows across 22 cell classes; the Bmpr2 transcript had negative logFC in 22/22 classes, nominal p<0.05 in 17/22, FDR<0.05 in 2/22, and median self logFC -0.671."}
{"target_gene": "Brsk2", "evidence_id": "E007", "cell_type": null, "statistics": "Brsk1 and Stk11 had 0 rows in the dataset. In 052 Pvalb Gaba, full-score Pearson r values to Brsk2 were Strada 0.0147, Mark3 0.0340, Prkaa2 0.00385, Mapt 0.0445 across 16,762 genes; the largest non-self positive correlation was 0.102. In 005 L4-5 IT CTX Glut, r values were Strada 0.0179, Mark3 -0.0135, Prkaa2 -0.0257, Mapt 0.0687 across 17,122 genes; the largest non-self positive correlation was 0.159."}
{"target_gene": "Casr", "evidence_id": "E007", "cell_type": null, "statistics": "Top-100 Casr-restricted screen placed Grm1 among the inverse neighbors in 054 CNU-MGE GABA and 155 MB Glut with r=-0.399193 and r=-0.372081 over selected genes; corresponding all-gene Casr:Grm1 correlations were -0.046000 and -0.016567."}
{"target_gene": "Cdk8", "evidence_id": "E004", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "154 Med13 cells versus 23,679 controls; 11 genes at FDR<0.05, including Prkcd logFC -0.427 FDR=2.46e-04, Grin2b -0.249 FDR=0.00110, Plekhg1 -0.317 FDR=0.00195, Pcp4 -0.324 FDR=0.00276, Lrrtm1 -0.382 FDR=0.00276, Atp2a2 -0.236 FDR=0.00276, Grm1 -0.229 FDR=0.00702, Ramp3 -0.304 FDR=0.00814, and Scnm1 +0.634 FDR=0.0434."}
{"target_gene": "Cebpe", "evidence_id": "E005", "cell_type": null, "statistics": "Within Cebpe perturbation, adjusted p was 1.0 for every tested row of Csf3r, Spi1, Gfi1, Gfi1b, Rara, Rxra, Gata1 and Sp1. Minimum nominal p by gene was Sp1 0.0848, Rara 0.1568, Rxra 0.2574, Csf3r 0.7095, Spi1 0.8042, Gfi1 0.8162, Gata1 0.8499 and Gfi1b 0.8715."}
{"target_gene": "Cep112", "evidence_id": "E001", "cell_type": "21 Cep112-profiled neuronal classes", "statistics": "Target row present in 21/21 Cep112 signatures; n_pert_matched 21-106; n_ctrl_matched 4807-23679; Cep112 self logFC range -0.706 to +0.484; all nominal p>=0.115; all FDR=1.0."}
{"target_gene": "Cep85l", "evidence_id": "E005", "cell_type": null, "statistics": "Cdk5r1 was nominally up in 017 CA3 CA2-FC DG Glut (score 2.131, logFC 0.342, p=0.0331, FDR=1.0), 022 L5 ET CTX Glut (score 2.498, logFC 0.233, p=0.0125, FDR=1.0), 054 CNU-MGE GABA (score 2.303, logFC 0.348, p=0.0213, FDR=1.0), and 308 CB GABA (score 2.967, logFC 0.433, p=0.00301, FDR=1.0)."}
{"target_gene": "Chrm2", "evidence_id": "E003", "cell_type": null, "statistics": "Chrm2 was represented in 22 of 23 dataset cell classes and absent from 215 MB Dopa; n_pert_matched min=23, median=63, max=155; 7/22 assayed classes had fewer than 50 perturbed cells; n_ctrl_matched ranged from 3,465 to 23,679."}
{"target_gene": "Chrna2", "evidence_id": "E005", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Chrna2 perturbation: Chrna2 score 0.319, p=0.750, FDR=1.0 with 231 cells. Comparator on-target rows in the same cell type were Chrnb2 score -6.594, p=4.27e-11, FDR=7.37e-7 with 222 cells; Chrna4 score -5.128, p=2.92e-7, FDR=0.00373 with 293 cells; Ache score -5.165, p=2.40e-7, FDR=0.00415 with 117 cells."}
{"target_gene": "Chrne", "evidence_id": "E006", "cell_type": null, "statistics": "Within 23 cell types, Chrne signatures were correlated with 448-2046 perturbations over 16228-17443 genes; maximum same-cell positive Pearson r=0.187801 with Macf1 in 054 CNU-MGE GABA; maximum negative r=-0.215541 with Manf in 054 CNU-MGE GABA; maximum absolute neighbor r in any cell type=0.215541."}
{"target_gene": "Cox11", "evidence_id": "E002", "cell_type": null, "statistics": "Cox11 transcript measured in 23/23 Cox11 cell-type tests; 16/23 logFC values were negative and 17/23 Wilcoxon scores were negative; nominal p<0.05 in 191 MB P MY GABA logFC -0.734 p=0.001138, 155 MB Glut logFC -0.502 p=0.010220, 053 Sst Gaba logFC -0.996 p=0.016610, and 110 CNU-HYa HY MM Glut logFC -0.759 p=0.018701; Cox11 p_adj=1.0 in every cell type."}
{"target_gene": "Cox6a1", "evidence_id": "E001", "cell_type": null, "statistics": "Cox6a1 transcript was measured in 23 perturbation cell types; 23/23 logFC values were negative; median logFC -0.488, range -1.252 to -0.119; nominal p<0.05 in 10/23; FDR<0.10 in 1/23 and FDR<0.05 in 0/23."}
{"target_gene": "Ctnnb1", "evidence_id": "E002", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "171 perturbed cells versus 23679 controls; 383 genes at FDR<0.05, including 283 down and 100 up. Ctnnb1 logFC -0.593 FDR 1.83e-10; Plekhg1 logFC -1.157 FDR 3.55e-25; Gabra4 logFC -0.758 FDR 7.85e-22; Ramp3 logFC -1.367 FDR 3.00e-21; Chgb logFC 0.696 FDR 1.76e-13."}
{"target_gene": "Ddhd1", "evidence_id": "E002", "cell_type": null, "statistics": "371,818 gene-level rows across 22 Ddhd1 contrasts; 0 rows at FDR<0.05; 1 row at FDR<0.10, Mcl1 in 046 CTX-CGE GABA with FDR=0.0630."}
{"target_gene": "Ddhd1", "evidence_id": "E005", "cell_type": "308 CB GABA", "statistics": "74 perturbed cells versus 8,277 controls; Ddhd1 logFC -0.481, score -2.707, p=0.00678, FDR=1.0; 0 genes at FDR<0.10; only Epn1 and Paf1 had p<0.001, with FDR=1.0 for both."}
{"target_gene": "Dlx5", "evidence_id": "E006", "cell_type": null, "statistics": "Dlx6 had 23 tested cell-type contrasts and 0 rows with FDR<0.05. Spearman correlations between matched Dlx5 and Dlx6 score vectors ranged from -0.039274 in 308 CB GABA to 0.087554 in 009 L2-3 IT PIR AON ENT Glut across the 23 shared Dlx5 cell types."}
{"target_gene": "Dnajc5", "evidence_id": "E001", "cell_type": "155 MB Glut", "statistics": "143 perturbed cells versus 20353 controls; Dnajc5 score -5.324778; logFC -0.627294; p=1.010767e-07; FDR=0.001763; rank 1/17443 by absolute score and p value."}
{"target_gene": "Eif4h", "evidence_id": "E010", "cell_type": null, "statistics": "Total q<0.05 rows across matched eIF4-related perturbations: Eif4h=1, Eif4a2=6, Eif4g1=1, Eif4e=184; in 151 TH Prkcd Grin2c Glut specifically, Eif4h=1, Eif4a2=2, Eif4g1=1, Eif4e=160."}
{"target_gene": "Esrrb", "evidence_id": "E002", "cell_type": null, "statistics": "371818 gene-by-cell-type tests for Esrrb; 0 genes with FDR<0.05 in any of 22 cell types; smallest FDR=0.522 for Fech in 217 P MY Pineal Glut."}
{"target_gene": "Etfa", "evidence_id": "E001", "cell_type": null, "statistics": "Etfa rows in 21 cell types; 1,101 total Etfa-perturbed cells and 208,027 matched controls summed across contrasts; n_pert per class 28-127; Etfa logFC was negative in 18/21 classes, median logFC -0.293; all Etfa pvals_adj=1.0."}
{"target_gene": "Fas", "evidence_id": "E003", "cell_type": null, "statistics": "0/371,818 rows with FDR < 0.05; 1/371,818 with FDR < 0.10; global minimum FDR = 0.091179."}
{"target_gene": "Fcgr4", "evidence_id": "E009", "cell_type": null, "statistics": "For Cd14, Csf1r, Fcgr2b, Itgb2, Tlr2, Tlr4, and Trem2 self-transcript rows, all adjusted p values were 1.0; the best nominal self p over these perturbations was 0.4323 for Csf1r."}
{"target_gene": "Figla", "evidence_id": "E004", "cell_type": "217 P MY Pineal Glut", "statistics": "33 Figla cells versus 3,465 controls; Klhl22 logFC 1.0696, score 4.485, nominal p 7.28e-6, pvals_adj 0.122."}
{"target_gene": "Fmn1", "evidence_id": "E003", "cell_type": null, "statistics": "Top rows by nominal p: Ccdc107 in 007 L2-3 IT CTX Glut score 4.378920 logFC 0.839417 p=0.0000118 FDR=0.199811; Rgs7 in 110 CNU-HYa HY MM Glut score -4.231404 logFC -1.232078 p=0.0000232 FDR=0.398682; Asah1 in 009 L2-3 IT PIR AON ENT Glut p=0.000037 FDR=0.632470; Csnk1a1 in 191 MB P MY GABA p=0.000048 FDR=0.826762; Ranbp6 in 027 NP-CT-L6b-OB Glut p=0.000053 FDR=0.878324."}
{"target_gene": "Foxl2", "evidence_id": "E001", "cell_type": null, "statistics": "388,046 Foxl2-perturbation DE rows across 23 cell types; 0 genes at FDR<0.05 in every cell type; best cell-type minimum FDR=0.1249 and best nominal p=7.49e-06."}
{"target_gene": "Foxn1", "evidence_id": "E003", "cell_type": null, "statistics": "151 TH Prkcd Grin2c Glut: 140 perturbed cells, top gene Echs1 logFC 0.8406, score 4.0702, nominal p 4.7e-05, FDR 0.8107; 155 MB Glut: 109 perturbed cells, minimum FDR 1.0; 005 L4-5 IT CTX Glut: 74 perturbed cells, minimum FDR 1.0."}
{"target_gene": "Frrs1l", "evidence_id": "E005", "cell_type": null, "statistics": "Within Frrs1l perturbations, none of Cpt1c, Gria1, Gria2, Gria3, Gria4, Cacng2, Cacng3, Cacng8, or Dlg4 was FDR<0.05 in any measured cell type; the smallest adjusted p value in this set was Gria2 in 308 CB GABA, logFC -0.536, p=0.00171, FDR=0.649; Cpt1c min p=0.0302, FDR=1.0; Dlg4 min p=0.0237, FDR=1.0."}
{"target_gene": "Fth1", "evidence_id": "E003", "cell_type": null, "statistics": "Weakest Fth1 entries were 017 CA3 CA2-FC DG Glut n=73 logFC -0.388 nominal p=0.0447 FDR 1.0, 059 CNU-LGE LSX GABA n=63 logFC -0.558 p=0.0207 FDR 1.0, and 012 MEA LA CA1 DG Glut n=68 logFC -0.415 p=0.0140 FDR 1.0; 217 P MY Pineal Glut had only 33 cells but a large logFC -1.360 and FDR 0.0351."}
{"target_gene": "Fzd9", "evidence_id": "E007", "cell_type": null, "statistics": "In 012 MEA LA CA1 DG Glut, there were 83 Fzd9-perturbed cells versus 7030 controls, Fzd9 score 0.014, p=0.989, FDR 1.0, and 0 FDR genes; best row Syf2 FDR 0.6787. In 017 CA3 CA2-FC DG Glut, there were 103 perturbed cells versus 8620 controls, Fzd9 score -0.049, p=0.961, FDR 1.0, and 0 FDR genes; best row Chchd2 FDR 1.0."}
{"target_gene": "Ghr", "evidence_id": "E004", "cell_type": "007 L2-3 IT CTX Glut", "statistics": "23 Ghr-targeted cells versus 7553 controls; Sugp2 score=-4.1372, logFC=-1.0530, p=3.52e-5, FDR=0.588973; Pomgnt1 score=3.8468, logFC=1.5857, p=1.20e-4, FDR=1.0; 40/16753 genes had p<0.01."}
{"target_gene": "Glra2", "evidence_id": "E008", "cell_type": null, "statistics": "Glrb perturbation strongly depleted the Glrb row in 151 TH Prkcd Grin2c Glut, n=132, logFC=-0.782, p=1.01e-11, FDR=1.74e-7; 155 MB Glut, n=89, logFC=-0.810, p=1.92e-8, FDR=3.34e-4; and 191 MB P MY GABA, n=49, logFC=-1.139, p=8.30e-8, FDR=0.00142. In each of these three cell classes Glrb itself was the only FDR<0.05 gene."}
{"target_gene": "Glrb", "evidence_id": "E006", "cell_type": null, "statistics": "Exact target filtering recovered Arhgef9 338323 rows across 20 groups and Glra1, Glra2, Glra3, Gphn, and Slc6a5 each with 371818 rows across 22 groups; exact gene_target values Glra4 and Slc6a9 returned 0 rows."}
{"target_gene": "Gnal", "evidence_id": "E005", "cell_type": "059 CNU-LGE LSX GABA", "statistics": "40 perturbed cells versus 8,270 controls; 0 FDR<0.05 genes; top row Dhdds logFC 0.981, score 4.261, p 2.03e-5, FDR 0.336."}
{"target_gene": "Gnas", "evidence_id": "E010", "cell_type": "012 MEA LA CA1 DG Glut", "statistics": "Pearson correlations computed over the top 100 absolute-score Gnas genes per class; maximum all-target correlation was Foxl2 r=0.5209 in 012 MEA LA CA1 DG Glut; strongest related targets in that class were Gnb5 r=0.4793, Gnal r=0.4183, Creb1 r=0.4073, and Adcy5 r=-0.4262."}
{"target_gene": "Gpr162", "evidence_id": "E007", "cell_type": "007 L2-3 IT CTX Glut", "statistics": "66 perturbed cells versus 7,553 controls; Ppp2r5d was the top positive row with score 4.436, logFC +0.800, p=9.17e-6, FDR=0.154; Gpr162 in the same signature had score -3.381, logFC -0.377, p=7.23e-4, FDR=1.0."}
{"target_gene": "Gria3", "evidence_id": "E006", "cell_type": null, "statistics": "Across 12 AMPAR-complex or AMPAR-adjacent genes measured in all 21 Gria3 cell-type comparisons, 0/252 gene-by-cell rows had FDR < 0.1. Gria1, Gria2, Gria4, Cacng2, Cacng3, Cnih2, Cnih3, Dlg4, Dlgap4, Grip1, Pick1, and Shisa9 all had adjusted p = 1.0 in every Gria3 comparison; the smallest nominal AMPAR-subunit p was Gria2 in 008 L2-3 IT ENT PPP RSP Glut, p = 0.00101, FDR = 1.0."}
{"target_gene": "Grin2b", "evidence_id": "E008", "cell_type": "007 L2-3 IT CTX Glut", "statistics": "In 007 L2-3 IT CTX Glut, Grin2b and Grin2a score vectors had Pearson r=-0.147 across 16753 genes, no overlapping FDR<0.05 genes, and Grin2a was the 3rd-most anticorrelated perturbation among 2011 Grin2b comparators; Grin2a yielded 20 FDR genes including Nptx2 logFC 1.777 FDR 6.09e-04, Scg2 logFC 1.292 FDR 0.00732, and Bdnf logFC 1.249 FDR 0.0272, whereas these genes trended negative after Grin2b perturbation. In 005 L4-5 IT CTX Glut, Grin2b versus Grin2a Pearson r=-0.081 across 17122 genes."}
{"target_gene": "Guk1", "evidence_id": "E003", "cell_type": "066 CNU-HYa HY GABA", "statistics": "121 perturbed cells versus 10110 controls; Guk1 logFC -0.774181 score -4.245932 p=0.000022 q=0.309490; Tjp1 logFC 0.627963 score 4.130688 p=0.000036 q=0.309490; Pdzd8 logFC 0.496576 score 3.898388 p=0.000097 q=0.552412."}
{"target_gene": "Hdac5", "evidence_id": "E009", "cell_type": null, "statistics": "In 151 TH Prkcd Grin2c Glut, score correlations with the Hdac5 signature were Ppp2r1a r=0.0305, Ppp3ca r=-0.0317, Camk2b r=-0.0181, Hdac4 r=0.0269, Mef2c r=0.0076, Mef2d r=0.0058. In 155 MB Glut, the matching r values were 0.0288, 0.0179, 0.0179, 0.0039, 0.0161, and 0.0019."}
{"target_gene": "Hesx1", "evidence_id": "E007", "cell_type": null, "statistics": "All-target score correlations to Hesx1 had maximum absolute r<0.118 in 20/22 strata. The exceptions were 017 CA3 CA2-FC DG Glut, max |r|=0.271, and 308 CB GABA, max |r|=0.345. In 308 CB GABA, top positive neighbors were Ranbp2 r=0.345, Atp6v1e1 r=0.316, B9d1 r=0.311, and Lhx4 r=0.289; top negative neighbors were Gpr68 r=-0.305, Scn9a r=-0.297, and Cckar r=-0.289."}
{"target_gene": "Hspd1", "evidence_id": "E002", "cell_type": null, "statistics": "Hspd1 target transcript was measured in 22 cell types. Nominal negative rows: 151 TH Prkcd Grin2c Glut score -3.393, logFC -0.564, p=0.000691, p_adj=1.0, rank 3/17,259, n=137; 145 MH-LH TH Glut score -2.566, logFC -0.899, p=0.0103, n=43; 054 CNU-MGE GABA score -2.512, logFC -0.897, p=0.0120, n=37; 155 MB Glut score -2.468, logFC -0.567, p=0.0136, n=117."}
{"target_gene": "Htr1a", "evidence_id": "E005", "cell_type": null, "statistics": "FDR<0.05 row counts among assayed serotonin receptors were Htr2a=1 and Htr3b=1, with Htr1a, Htr1b, Htr1f, Htr2b, Htr2c, Htr3a, Htr4, Htr6, and Htr7 all 0; minimum adjusted p values were Htr3b 0.0195, Htr2a 0.0330, Htr1f 0.0654, Htr1b 0.308, Htr2c 0.361, Htr7 0.575, and Htr1a 0.693; none of the 11 receptor perturbations significantly reduced its own transcript."}
{"target_gene": "Ifngr2", "evidence_id": "E004", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "201 perturbed cells versus 23679 controls; Ifngr2 logFC -0.574, score -3.695, P=2.20e-4, FDR=1.0; Stat1 logFC -0.888, score -3.437, P=5.88e-4; Nlrc5 logFC -2.372, score -2.874, P=0.00406; B2m logFC -0.846, score -2.304, P=0.0212; all module FDR values were 1.0."}
{"target_gene": "Igsf8", "evidence_id": "E005", "cell_type": null, "statistics": "At p<0.01, no non-Igsf8 gene recurred in more than 3/23 cell classes; Colgalt1, Fam135b, Ric8b, Pbx1, and Elp1 each appeared in exactly three classes."}
{"target_gene": "Il1rapl1", "evidence_id": "E014", "cell_type": null, "statistics": "88 rows covering Mcf2l, Rhoa, Rock1, and Rock2 across 22 cell types; 0 rows with FDR<0.05; Mcf2l was nominally down only in 017 CA3 CA2-FC DG Glut with p=0.0266 and 046 CTX-CGE GABA with p=0.0357; Rhoa had minimum nominal p=0.176."}
{"target_gene": "Il4ra", "evidence_id": "E005", "cell_type": null, "statistics": "Il2rg perturbation was present in 22 cell groups with 20-157 perturbed cells per group; each group had 0 genes at FDR<0.05; minimum genome-wide FDR=0.103637; the Il2rg target transcript had FDR=1.0 in all 22 measured on-target rows."}
{"target_gene": "Itm2b", "evidence_id": "E006", "cell_type": null, "statistics": "P4htm reached FDR < 0.05 only in 027 NP-CT-L6b-OB Glut; its next smallest nominal p was 0.0214 in 052 Pvalb Gaba with FDR=1.0. Lrrc24 reached FDR < 0.05 only in 052 Pvalb Gaba; its next smallest nominal p was 0.0529 in 191 MB P MY GABA with FDR=1.0."}
{"target_gene": "Itpr1", "evidence_id": "E007", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Atp2a2 perturbation: 98 perturbed cells versus 23679 controls; Atp2a2 logFC -1.256, p=1.03e-23, FDR=1.78e-19; 187/17259 genes had FDR < 0.05, including Ddit3 logFC 1.604, FDR=2.06e-8; Xbp1 logFC 0.785, FDR=3.00e-7; Hspa5 logFC 0.749, FDR=1.95e-6; and Chac1 logFC 3.014, FDR=6.61e-8. The Itpr1-versus-Atp2a2 Wilcoxon-score correlation in this cell type was r=0.0165."}
{"target_gene": "Kcnab1", "evidence_id": "E008", "cell_type": null, "statistics": "Pearson correlations between Kcnab1 and Kcnab2 scores on the top 100 positive plus top 100 negative Kcnab1 genes were 0.128 in 052 Pvalb Gaba, 0.037 in 066 CNU-HYa HY GABA, 0.053 in 151 TH Prkcd Grin2c Glut, 0.133 in 155 MB Glut, and 0.120 in 191 MB P MY GABA."}
{"target_gene": "Kcnab2", "evidence_id": "E011", "cell_type": null, "statistics": "The strongest non-self absolute Pearson correlations to the Kcnab2 score vector in the five FDR-significant cell types were |r|=0.109 in 052 Pvalb Gaba, 0.073 in 066 CNU-HYa HY GABA, 0.083 in 151 TH Prkcd Grin2c Glut, 0.106 in 155 MB Glut, and 0.125 in 191 MB P MY GABA."}
{"target_gene": "Kcnc1", "evidence_id": "E009", "cell_type": null, "statistics": "Kcnc1 correlations with Kcnc3 score vectors were r=0.0212 in 191 MB P MY GABA, r=-0.0064 in 151 TH Prkcd Grin2c Glut, and r=0.0710 in 155 MB Glut; Kcnc3 target FDR values in those classes were 1.22e-11, 6.16e-07, and 2.64e-17. Kcnc1 correlations with Kcnc2 were r=0.0388, 0.0831, and 0.0089 in the same classes; Kcnc2 target FDR was 1.0, 4.65e-05, and 2.48e-05, respectively."}
{"target_gene": "Kctd16", "evidence_id": "E006", "cell_type": null, "statistics": "Across 20 overlapping Kctd16 cell types, Pearson correlations of same-gene Wilcoxon score vectors were Kctd16 versus Kctd8 range -0.029 to 0.070, Kctd16 versus Gabbr1 range -0.053 to 0.038, and Kctd16 versus Gabbr2 range -0.028 to 0.072. Kctd8 itself had 0 FDR<0.05 genes across 22 tested cell types."}
{"target_gene": "Kiz", "evidence_id": "E010", "cell_type": null, "statistics": "In the four Kiz cell classes with FDR<0.5 rows, absolute top positive/negative whole-signature correlations were small: 054 Tspoap1 r=0.154 and Safe_target_40 r=-0.122; 053 Mycn r=0.121 and Gp6 r=-0.101; 059 Npy1r r=0.0757 and Calm3 r=-0.0593; 110 Snf8 r=0.121 and Prnp r=-0.108."}
{"target_gene": "Klf13", "evidence_id": "E005", "cell_type": "053 Sst Gaba", "statistics": "60 perturbed cells versus 5622 controls; 16428 genes tested; 0 genes with FDR < 0.05; 7 genes with p < 0.001. Ctnna2 was the top row with score -4.023, logFC -0.584, p 5.75e-5, FDR 0.9444."}
{"target_gene": "Klrk1", "evidence_id": "E006", "cell_type": null, "statistics": "A targeted scan for 41 NKG2D-adaptor, NK-receptor, ligand, and broad signaling labels found rows for Klrk1, Fyn, Cd247, Mapk1, Pik3r1, and Rac1; it returned no rows for the core adaptors Hcst or Tyrobp, Klrc1-4, Klrd1, Ncr1, Zap70, Syk, Lat, Lck, Vav1, Plcg1, Plcg2, mouse Raet1/H60 ligand names, or Ulbp1-3."}
{"target_gene": "Kmt2e", "evidence_id": "E005", "cell_type": null, "statistics": "At FDR<0.25, the intersection between the 151 TH Prkcd Grin2c Glut and 155 MB Glut signatures contained exactly three genes. Snhg11 logFC +0.107 FDR 0.0219 in 151 and +0.162 FDR 0.0533 in 155; Atp6v0b +0.182 FDR 0.110 in 151 and +0.287 FDR 0.0644 in 155; Eno2 +0.201 FDR 0.0310 in 151 and +0.261 FDR 0.193 in 155."}
{"target_gene": "Lepr", "evidence_id": "E008", "cell_type": "145 MH-LH TH Glut", "statistics": "Mc4r perturbation: 71 perturbed cells, Smox score 4.953 logFC 1.179 p=7.31e-7 FDR=0.0122, 1 gene at FDR<0.1. Lepr perturbation: 55 perturbed cells, best gene Shank3 score -3.535 p=4.08e-4 FDR=1.0, 0 genes at FDR<0.1; Lepr target row p=0.793 FDR=1.0."}
{"target_gene": "Lgals3", "evidence_id": "E008", "cell_type": null, "statistics": "St3gal5 had significant on-target depletion in 10 cell types: target-row FDR 1.96e-14 to 0.0209 and scores -8.821 to -4.847; in each of those cell types exactly one gene reached FDR<0.05, and 155 MB Glut was the only one with a second gene at FDR<0.10."}
{"target_gene": "Lhcgr", "evidence_id": "E002", "cell_type": null, "statistics": "0 of 371,818 Lhcgr-versus-Non_target gene tests had pvals_adj < 0.05 across 22 subclasses."}
{"target_gene": "Lmbrd1", "evidence_id": "E007", "cell_type": null, "statistics": "In 046 CTX-CGE GABA, Lmbrd1 score 0.155, logFC 0.107, p=0.877, FDR=1; in 308 CB GABA, Lmbrd1 score 0.800, logFC 0.101, p=0.424, FDR=1."}
{"target_gene": "Lrch1", "evidence_id": "E002", "cell_type": null, "statistics": "Lrch1 transcript was measured in 21 cell classes; 17 of 21 scores were negative and 4 of 21 were positive; all Lrch1 self-transcript rows had FDR=1.0. Strongest nominal self-transcript rows: 151 TH Prkcd Grin2c Glut score -2.320 logFC -0.150 p=0.0203; 191 MB P MY GABA score -2.199 logFC -0.458 p=0.0279; 052 Pvalb Gaba score -1.985 logFC -0.377 p=0.0472; 145 MH-LH TH Glut score -1.961 logFC -0.398 p=0.0499; 066 CNU-HYa HY GABA score -1.909 logFC -0.413 p=0.0563."}
{"target_gene": "Lrrtm3", "evidence_id": "E001", "cell_type": "155 MB Glut", "statistics": "153 perturbed cells versus 20353 controls; Lrrtm3 score -4.372723, logFC -0.587722, nominal p=1.22706588e-05, adjusted p=0.214037101."}
{"target_gene": "Lztfl1", "evidence_id": "E003", "cell_type": null, "statistics": "Across all Lztfl1 rows, FDR<0.05 count=0 and FDR<0.10 count=1; the only 10% row was Cyld in 059 CNU-LGE LSX GABA, score 4.526, logFC 0.527, p=6.01e-6, FDR=0.099, while Lztfl1 in the same cell class had logFC -0.442, p=0.086, FDR=1.0."}
{"target_gene": "Mafb", "evidence_id": "E003", "cell_type": "052 Pvalb Gaba", "statistics": "88 Mafb-perturbed cells versus 13710 controls; Ccdc88a logFC=-0.503, score=-4.69, p=2.69e-06, FDR=0.0450. The next ranked genes Man2a2 and Psmg1 both had FDR=0.796. Mafb itself had logFC=-0.213, p=0.152, FDR=1.0."}
{"target_gene": "Map1b", "evidence_id": "E006", "cell_type": null, "statistics": "In 151 TH Prkcd Grin2c Glut and 155 MB Glut, both Map1b and Mapt perturbations had exactly one FDR<0.05 row: the targeted transcript itself. Mapt self rows were logFC -0.533, FDR=1.43e-5 in 151 TH Prkcd Grin2c Glut and logFC -0.519, FDR=0.00663 in 155 MB Glut."}
{"target_gene": "Mark3", "evidence_id": "E002", "cell_type": "145 MH-LH TH Glut", "statistics": "Across 355,046 Mark3 rows, only one gene had p_adj<0.05 or p_adj<0.1: Rai1 in 145 MH-LH TH Glut, score -5.304, logFC -1.618, p=1.14e-7, p_adj=0.00190, 39 perturbed cells versus 6,961 controls; the next-best cell-type minimum p_adj values were 0.339 and 0.439."}
{"target_gene": "Max", "evidence_id": "E006", "cell_type": null, "statistics": "Mga perturbation produced only 3 FDR<0.05 rows overall but included Stag3 in 151 TH Prkcd Grin2c Glut (logFC 3.606, FDR 4.83e-5) and 155 MB Glut (logFC 3.633, FDR 1.93e-4); Obscn was also up in Mga-perturbed 151 cells (logFC 4.435, FDR 1.73e-8)."}
{"target_gene": "Mboat7", "evidence_id": "E003", "cell_type": null, "statistics": "Mboat7 target transcript logFC was negative in 21/22 measured cell types; median logFC -0.430682; p<0.05 in 17/22, p<0.01 in 14/22, p<0.001 in 10/22; Mboat7 was the largest absolute-score gene in 7/22 cell types."}
{"target_gene": "Med13l", "evidence_id": "E001", "cell_type": null, "statistics": "Med13l transcript was measured in 22 cell-type signatures with n_pert_matched ranging from 31 to 200; 0/22 direct Med13l rows reached FDR<0.05; 3/22 had nominal p<0.05; 13/22 Wilcoxon scores were negative; strongest direct row was 151 TH Prkcd Grin2c Glut with score -3.046, logFC -0.317, p=0.00232, FDR=1.0."}
{"target_gene": "Med23", "evidence_id": "E008", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "None of 11 immediate-early or activity-response genes tested in 151 TH Prkcd Grin2c Glut reached FDR<0.05 under Med23 perturbation; Jun was nominally up (logFC 0.376, p=0.0117, FDR=1.0), Fos was near zero (logFC -0.0649, p=0.910, FDR=1.0), and Arc was near zero (logFC -0.0381, p=0.813, FDR=1.0)."}
{"target_gene": "Mkx", "evidence_id": "E001", "cell_type": null, "statistics": "21 Mkx target-transcript rows; 24-111 perturbed cells per subclass versus 4,807-23,679 Non_target controls; Mkx logFC range -0.590 to +0.443, median -0.113; 14/21 logFC values were negative; minimum nominal p=0.010595 in 052 Pvalb Gaba; 0/21 target rows had FDR<0.05 and all had FDR=1.0."}
{"target_gene": "Mtnr1b", "evidence_id": "E005", "cell_type": null, "statistics": "Per-cell-type Mtnr1b n_pert_matched values were 20-162 with median 56.5; the three largest were 151 TH Prkcd Grin2c Glut n=162, 155 MB Glut n=136, and 005 L4-5 IT CTX Glut n=109; the smallest was 217 P MY Pineal Glut n=20."}
{"target_gene": "Mttp", "evidence_id": "E004", "cell_type": "145 MH-LH TH Glut", "statistics": "55 Mttp-targeted cells versus 6,961 controls; Pcsk2 logFC 0.7089, score 4.1818, nominal P=2.89e-05, FDR=0.3545; Tsc22d2 logFC -0.9627, score -4.0938, nominal P=4.19e-05, FDR=0.3545; Kpna3 FDR=0.7328; Gramd1a FDR=0.7374; Mapk8ip2 FDR=0.8451."}
{"target_gene": "Ncam1", "evidence_id": "E003", "cell_type": null, "statistics": "Across 371796 non-Ncam1 rows in the 22 Ncam1-perturbation strata, 0 rows reached FDR<0.05 and 0 reached FDR<0.10. The smallest non-target FDRs were Lancl1 in 191 MB P MY GABA at 0.289 and Micu3 in 005 L4-5 IT CTX Glut at 0.382."}
{"target_gene": "Nefl", "evidence_id": "E001", "cell_type": null, "statistics": "22 cell-type tests; Nefl logFC was negative in 21/22; nominal p<0.05 in 19/22; FDR<0.05 in 11/22 and FDR<0.10 in 12/22; median logFC -0.915."}
{"target_gene": "Neo1", "evidence_id": "E001", "cell_type": null, "statistics": "21 subclasses; 355046 Neo1 target-comparison rows; 29-167 perturbed cells and 4807-23679 controls per subclass; Neo1 transcript row measured in all 21; 20/21 target-row logFC values were negative; 4/21 had nominal target-row p<0.05; best target row was 151 TH Prkcd Grin2c Glut with score -3.911, logFC -0.447, p=9.17e-5, FDR=0.792."}
{"target_gene": "Neurod2", "evidence_id": "E001", "cell_type": null, "statistics": "Neurod2 was measured in all 23 Neurod2-perturbed cell classes; 21-260 perturbed cells versus 2019-23679 matched controls; no Neurod2 row had p<0.05; minimum target-row p=0.135, maximum |Wilcoxon score|=1.49, and every target-row FDR was 1.0."}
{"target_gene": "Nfib", "evidence_id": "E006", "cell_type": null, "statistics": "The two Nfic FDR < 0.05 rows were Bambi in 151 TH Prkcd Grin2c Glut, logFC 0.721, p = 2.21e-7, FDR = 0.00382, n = 297 perturbed cells; and the Nfic self row in 155 MB Glut, logFC -0.504, p = 1.00e-6, FDR = 0.0175, n = 260 perturbed cells."}
{"target_gene": "Nfic", "evidence_id": "E011", "cell_type": null, "statistics": "The Nfic subset contained 388,046 Wilcoxon rows across 23 cell types. Exactly two rows had FDR<0.05: Bambi in 151 TH Prkcd Grin2c Glut at FDR=0.00382 and Nfic in 155 MB Glut at FDR=0.0175; 4 rows had FDR<=0.1 and 16 had FDR<=0.5."}
{"target_gene": "Nfkb1", "evidence_id": "E007", "cell_type": null, "statistics": "Global Pearson correlations of Wilcoxon score vectors versus Nfkb1 across shared features were Rel -0.0009, Map3k7 0.0011, Traf3 0.0054, Nfkb2 0.0108, Relb 0.0118, and Chuk 0.0129."}
{"target_gene": "Nobox", "evidence_id": "E002", "cell_type": "22 Nobox-tested cell classes", "statistics": "371818 gene-by-cell-type rows; 0 rows with FDR<0.05; 1 row with FDR<0.1; 134 rows with nominal p<0.001 across all rows."}
{"target_gene": "Nr2c1", "evidence_id": "E002", "cell_type": null, "statistics": "371818 Nr2c1 gene-level rows across 22 cell classes; 1 row with pvals_adj<0.05; 86 rows with raw p<0.001; 1125 rows with raw p<0.01."}
{"target_gene": "Nr2f2", "evidence_id": "E009", "cell_type": null, "statistics": "Nr2c2 was the second-most negative Nr2f2 neighbor in 017 CA3 CA2-FC DG Glut (r=-0.252, rank 2029/2030) and in 001 L5-6 IT Glut (r=-0.086, rank 1874/1875)."}
{"target_gene": "Nr2f6", "evidence_id": "E004", "cell_type": null, "statistics": "Across the 22 Nr2f6 cell-class signatures, no up- or down-regulated top-10 gene recurred in more than two classes; the total nominal burden was 294-439 p<0.05 genes per class with every class having zero FDR<0.1 genes."}
{"target_gene": "Pak3", "evidence_id": "E002", "cell_type": null, "statistics": "Pak3 transcript was measured in all 22 tested cell types; logFC was negative in 20/22; nominal p<0.05 in 4/22, led by 155 MB Glut logFC -0.631 p=3.39e-4 and 145 MH-LH TH Glut logFC -0.864 p=0.00291; every Pak3 self row had pvals_adj=1.0."}
{"target_gene": "Paqr8", "evidence_id": "E003", "cell_type": null, "statistics": "Paqr8 was measured in 22 signatures with 40-215 perturbed cells per signature; 17/22 estimated Paqr8 logFC values were negative, 3/22 Paqr8 rows had nominal p<0.05, and 1/22 had FDR<0.05."}
{"target_gene": "Pax7", "evidence_id": "E002", "cell_type": null, "statistics": "371,818 Pax7 differential-expression rows across 22 cell classes; 1 row had FDR<0.05, 1 row had FDR<0.20, and the second-smallest FDR was 0.204478."}
{"target_gene": "Pdcd10", "evidence_id": "E003", "cell_type": "052 Pvalb Gaba", "statistics": "91 perturbed cells versus 13710 controls; Pdcd10 logFC -0.475, score -3.168, p=0.00154, FDR=1.0, rank 6 by absolute score and rank 2 among negative scores; Srm logFC 0.650, score 3.965, p=7.33e-5, FDR=1.0."}
{"target_gene": "Pde1c", "evidence_id": "E001", "cell_type": null, "statistics": "Pde1c DE row present in 22 cell types; 1,230 total matched Pde1c-perturbed cells, 21-155 per cell type; all Pde1c transcript adjusted p values = 1.0; smallest nominal on-target p = 0.062 in 308 CB GABA, logFC -0.696, score -1.866."}
{"target_gene": "Pde1c", "evidence_id": "E004", "cell_type": null, "statistics": "Total FDR < 0.05 genes across matched PDE perturbations and cell types: Pde1c 0, Pde3a 0, Pde4d 0, Pde4b 2, Pde10a 3. Pde10a self-depletion was significant only in 059 CNU-LGE LSX GABA with logFC -0.942, FDR 0.00478."}
{"target_gene": "Pds5a", "evidence_id": "E005", "cell_type": null, "statistics": "Among 106 Pds5a rows with nominal p<0.001, Exd2 was the only gene appearing in more than one cell class, in 017 CA3 CA2-FC DG Glut and 054 CNU-MGE GABA; no gene recurred in three or more p<0.001 rows."}
{"target_gene": "Plcb1", "evidence_id": "E004", "cell_type": "005 L4-5 IT CTX Glut", "statistics": "136 Itpr1 cells versus 15039 controls; Itpr1 score -5.1634, logFC -0.4351, nominal p=2.43e-7, FDR=0.00415; the Itpr1 self row was the only FDR<0.05 row for that perturbation in this cell type."}
{"target_gene": "Plec", "evidence_id": "E008", "cell_type": "001 L5-6 IT Glut", "statistics": "Pearson correlations of 16723-gene score vectors between Plec and 1874 other perturbations in 001 L5-6 IT Glut ranged from Adnp r=-0.064 to Nhs r=0.069; the STRING-linked Dag1 perturbation had r=0.051."}
{"target_gene": "Plxnc1", "evidence_id": "E002", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "258 perturbed cells versus 23,679 controls; Plxnc1 score -4.458, logFC -0.575, p=8.26e-6, FDR=0.1426; rank 1/17,259 by negative score, absolute score, and nominal p."}
{"target_gene": "Plxnc1", "evidence_id": "E006", "cell_type": null, "statistics": "Outside the five cell types with Plxnc1 p<0.005, the target row had p>=0.0325 and FDR=1.0; in 017 CA3 CA2-FC DG Glut Plxnc1 logFC was -0.052 with p=0.732, and in 217 P MY Pineal Glut logFC was -0.150 with p=0.978."}
{"target_gene": "Pou2f2", "evidence_id": "E005", "cell_type": "217 P MY Pineal Glut", "statistics": "32 Pou2f2 cells versus 3,465 controls; Tbc1d9b score -4.135, logFC -0.740, nominal p=3.56e-5, FDR=0.5964; BC005537 score -3.962, logFC -0.709, nominal p=7.4e-5, FDR=0.6234."}
{"target_gene": "Ppip5k2", "evidence_id": "E007", "cell_type": null, "statistics": "For Pten perturbation, FDR<0.05 genes were detected in 151 TH Prkcd Grin2c Glut (33), 155 MB Glut (11), and 191 MB P MY GABA (1). Mtor had 2 FDR<0.05 genes in 151 TH Prkcd Grin2c Glut, and Plcb1 had 1 in 005 L4-5 IT CTX Glut; Inpp5k had 0 in all 22 overlapping Ppip5k2 cell types."}
{"target_gene": "Prdm10", "evidence_id": "E003", "cell_type": "191 MB P MY GABA", "statistics": "111 perturbed cells versus 10309 controls; 34 FDR<0.05 genes: 6 up and 28 down; Cadm3 logFC -1.227 FDR 1.12e-20, Ptov1 -1.668 FDR 5.57e-20, Madd -1.326 FDR 3.45e-18, Prdm10 +0.981 FDR 0.00173."}
{"target_gene": "Prdm2", "evidence_id": "E006", "cell_type": null, "statistics": "Across the 22 Prdm2 cell types, mean full-transcriptome Pearson correlations of Wilcoxon scores with Prdm2 were Prdm5 r = -0.0005, Prdm10 r = 0.0094, Prdm12 r = 0.0074, and Prdm16 r = 0.0022; all individual cell-type correlations across these four paralogs were between -0.065 and 0.089."}
{"target_gene": "Pura", "evidence_id": "E008", "cell_type": null, "statistics": "In 151 TH Prkcd Grin2c Glut, Pura-score Pearson correlations were 0.117 versus Purb and 0.013 versus Purg; Purb and Purg produced 0 FDR<0.05 genes with 239 and 146 perturbed cells. In 155 MB Glut, Pura-score Pearson correlations were 0.086 versus Purb and 0.010 versus Purg; Purb and Purg produced 0 FDR<0.05 genes with 225 and 113 perturbed cells. Purb and Purg target transcripts did not pass FDR in these two classes."}
{"target_gene": "Ranbp2", "evidence_id": "E010", "cell_type": null, "statistics": "None of the measured canonical antiviral or inflammatory genes tested was FDR<0.05 in any of the 20 Ranbp2 cell types; best adjusted values were Stat2 FDR=0.966 and FDR=1.0 for Ifit3, Stat1, Ifit1, Isg15, Ifit2, Irf7, Ifitm3, Cxcl10, Ccl2, Il6, Tnf, Oas1a, and Ifnb1."}
{"target_gene": "Rel", "evidence_id": "E005", "cell_type": null, "statistics": "Relb, Nfkb1, Nfkb2, Chuk, and Traf3 produced 1891546 combined gene rows across their available cell types; 0 rows had FDR < 0.05. Their target-transcript rows also had 0 FDR-significant detections."}
{"target_gene": "Rnf13", "evidence_id": "E006", "cell_type": null, "statistics": "In the five classes with nominal Rnf13 target-transcript decrease, the 50 tests covering Atf6, Hspa5, Mapk8, Mapk9, Xbp1, Ern1, Traf2, Ddit3, Bax, and Bcl2l11 had median |score| 0.625 and no FDR < 0.05; the only nominal p<0.05 marker was Bax in 191 MB P MY GABA, logFC 0.377, score 2.209, p=0.0272, FDR=1.0."}
{"target_gene": "Ror1", "evidence_id": "E004", "cell_type": "017 CA3 CA2-FC DG Glut", "statistics": "65 Ror1-perturbed cells; 0 genes with pvals_adj < 0.05; top rows: Bin1 logFC -0.413 p=8.9e-05 pvals_adj 0.458853, Me1 logFC -1.356 p=1.20e-04 pvals_adj 0.458853, Kcnj4 logFC 0.949 p=1.30e-04 pvals_adj 0.458853."}
{"target_gene": "Rpgrip1l", "evidence_id": "E006", "cell_type": null, "statistics": "B9d1 in 308 CB GABA had 9 FDR<0.05 genes among 62 perturbed cells, led by Bend6 FDR=0.0343 and Phc2/Homer3/Gas8 FDR=0.0452; Ahi1 in 155 MB Glut had its own target transcript decreased, logFC=-0.695, p=4.26e-11, FDR=7.44e-7; Ift88 in 155 MB Glut had Pcsk1n logFC=0.427, p=5.30e-7, FDR=0.00924. Rpgrip1l had 0 FDR<0.05 genes in 308 CB GABA and 155 MB Glut."}
{"target_gene": "Rsrc1", "evidence_id": "E003", "cell_type": null, "statistics": "151 TH Prkcd Grin2c Glut had 233 perturbed cells and 0 genes at FDR<0.25; 155 MB Glut had 205 perturbed cells and 0 genes at FDR<0.25. In 155 MB Glut the top nominal positive row was Srsf9, score 3.807, p=0.000141, FDR=0.614, and the top negative row was Ndufa10, score -4.071, p=0.000047, FDR=0.614."}
{"target_gene": "Sall1", "evidence_id": "E002", "cell_type": null, "statistics": "371,818 Sall1 DE tests across 22 cell types; 1 gene at FDR<0.05, 21/22 cell types with 0 FDR<0.05 genes; second-best FDR=0.102806."}
{"target_gene": "Serpini1", "evidence_id": "E009", "cell_type": null, "statistics": "Plat, Plau, Plaur, and Plg were absent as gene_target perturbations. App, Lrp1, and Prnp were present, but their maximum absolute Pearson correlations with Serpini1 score vectors across shared cell types were 0.105, 0.097, and 0.078 respectively."}
{"target_gene": "Six5", "evidence_id": "E001", "cell_type": null, "statistics": "Six5 transcript row present in 23/23 assayed cell types; 1,831 total Six5-perturbed cells; per-cell-type n_pert_matched=20-215 and n_ctrl_matched=2,019-23,679; Six5-row median |score|=0.168, maximum |score|=1.043, minimum nominal p=0.297, and pvals_adj=1.0 in every cell type."}
{"target_gene": "Sox11", "evidence_id": "E002", "cell_type": null, "statistics": "388046 Sox11 gene-by-cell-type tests; 0 genes at FDR<0.05; minimum FDR=0.1816; maximum absolute score=4.402; 116 rows at nominal p<0.001 versus 388.0 expected at a uniform 0.001 rate."}
{"target_gene": "Sp4", "evidence_id": "E002", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "183 perturbed cells versus 23679 matched controls; 14 genes at FDR<0.05. Top effects included Stxbp2 logFC=-1.069, score=-7.400, FDR=2.35e-09; Svip logFC=0.643, score=6.267, FDR=3.17e-06; Tspan17 logFC=-0.695, score=-6.182, FDR=3.64e-06; Strada logFC=0.469, score=5.842, FDR=2.23e-05; Tsga10 logFC=0.772, FDR=7.23e-04."}
{"target_gene": "Spast", "evidence_id": "E009", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "141 perturbed cells versus 23,679 controls; Spast logFC -0.343, P=0.00756, FDR=1.0; 9 genes had P<0.001 and 61 had P<0.01; top nominal genes included Exoc4 logFC 0.274, P=1.92e-4; Kif1a logFC 0.172, P=2.40e-4; Clpp logFC 0.442, P=3.22e-4; Mkrn1 logFC 0.469, P=4.06e-4."}
{"target_gene": "St3gal3", "evidence_id": "E009", "cell_type": null, "statistics": "Each listed marker was measured in all 22 St3gal3 tests and every pvals_adj was 1.0. The smallest nominal values were Ncam1 p 0.023 in 217 P MY Pineal Glut, Mbp p 0.0267 in 012 MEA LA CA1 DG Glut, St8sia4 p 0.0282 in 217 P MY Pineal Glut, and Bcan p 0.0475 in 053 Sst Gaba."}
{"target_gene": "Stard7", "evidence_id": "E008", "cell_type": null, "statistics": "Across 22 cell types, mean Pearson correlations with Stard7 scores ranged from -0.002 for Selenoi to 0.024 for Chchd10. Only |r| > 0.10 values were in 308 CB GABA: Micos13 0.238, Chchd10 0.231, Mboat7 0.210, Pitpnm3 -0.183; these comparator CB GABA tables had minimum FDR 1.000."}
{"target_gene": "Stmn2", "evidence_id": "E003", "cell_type": null, "statistics": "017 CA3 CA2-FC DG Glut: 65 perturbed cells, Stmn2 logFC -0.203, p=0.243, FDR=1.0, no genes below FDR 0.5. 059 CNU-LGE LSX GABA: 67 perturbed cells, Stmn2 logFC -0.322, p=0.220, FDR=1.0, no genes below FDR 0.5."}
{"target_gene": "Sv2a", "evidence_id": "E001", "cell_type": null, "statistics": "371,818 Sv2a-perturbation rows covering 22 cell types; the Sv2a transcript row was negative in 22/22; 13/22 passed FDR<0.05 with logFC -0.70 to -1.39 and Wilcoxon scores -4.69 to -13.70."}
{"target_gene": "Tas2r118", "evidence_id": "E008", "cell_type": null, "statistics": "A scan of 2046 unique gene_target values found Tas2r118 as the only Tas2r entry and found no Tas1r1, Tas1r2, Tas1r3, Gnat3, Plcb2, Itpr3, or Trpm5 perturbation targets."}
{"target_gene": "Tbr1", "evidence_id": "E005", "cell_type": "009 L2-3 IT PIR AON ENT Glut", "statistics": "108 perturbed cells versus 9240 controls; 0 genes with pvals_adj < 0.05 and 2 genes with pvals_adj < 0.10: Pnma8b logFC +0.595 q=0.0566; Ehbp1 +0.548 q=0.0959."}
{"target_gene": "Tlr7", "evidence_id": "E002", "cell_type": null, "statistics": "19 Tlr7 self-transcript rows; Wilcoxon score range -0.184 to 0.286; nominal p range 0.7749-0.9909; pvals_adj=1.000 in all 19 rows."}
{"target_gene": "Tsga10", "evidence_id": "E002", "cell_type": null, "statistics": "Tsga10 mRNA was measured in 22/22 contrasts; all Tsga10 rows had FDR=1.0 and nominal p>=0.0764; logFC was negative in 18/22 contrasts and positive in 4/22; best nominal target row was 308 CB GABA logFC 0.415, score 1.772, p=0.0764, FDR=1.0."}
{"target_gene": "Tspan12", "evidence_id": "E007", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Fzd4: 188 perturbed cells, 0 genes at FDR<=0.05. Lrp5: 230 perturbed cells, 0 genes at FDR<=0.05. Lrp6: 120 perturbed cells, 4 genes at FDR<=0.05 and Axin2 logFC=-0.8002, p=2.54e-5, FDR=0.0731."}
{"target_gene": "Tuba4a", "evidence_id": "E011", "cell_type": null, "statistics": "Tuba4a self rows with weak engagement included 053 Sst Gaba: 42 perturbed cells, logFC 0.029, p=0.902, FDR=1.0; 008 L2-3 IT ENT PPP RSP Glut: 47 perturbed cells, logFC -0.133, p=0.651, FDR=1.0; 308 CB GABA: 54 perturbed cells, logFC -0.140, p=0.673, FDR=1.0."}
{"target_gene": "Tubb2a", "evidence_id": "E003", "cell_type": null, "statistics": "11/371818 Tubb2a DE rows passed FDR<0.05; 9/11 were Tubb2a itself; only 2/371796 non-target rows passed FDR<0.05; 12 total rows passed FDR<0.10."}
{"target_gene": "Uqcrq", "evidence_id": "E006", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "345 perturbed cells versus 23679 controls; Gpr180 logFC -0.466410, score -4.709418, p=2.484e-06, FDR=0.042876; Uqcrq logFC -0.294505, score -2.391641, p=0.016773, FDR=1; only 1 gene in this class had FDR<0.05."}
{"target_gene": "Usp48", "evidence_id": "E007", "cell_type": "151 TH Prkcd Grin2c Glut", "statistics": "Usp9x perturbation: 83 perturbed cells, Usp9x logFC -0.560, FDR 0.00354, with only 1 FDR<0.05 gene. Uchl1 perturbation: 250 perturbed cells, Uchl1 logFC -1.143, FDR 8.07e-60, with only 1 FDR<0.05 gene. Neither perturbation FDR-changed the 10 Usp48 downstream genes."}
{"target_gene": "Vps41", "evidence_id": "E004", "cell_type": "155 MB Glut", "statistics": "141 perturbed cells versus 20353 controls; Mcoln1 logFC 0.397 score 4.702 p=2.57e-6 FDR 0.0448; Vps41 logFC -0.562 p=4.08e-5 FDR 0.157; Cds1 0.460 p=3.50e-5; Atp6v0b 0.229 p=6.24e-5; Insig1 0.603 p=6.28e-5; Lamp2 0.410 p=7.26e-5; Msmo1 0.563 p=2.34e-4; Srebf2 0.382 p=8.92e-4."}
{"target_gene": "Wac", "evidence_id": "E008", "cell_type": null, "statistics": "Pearson correlations of Wac scores to all other perturbations: in 151 TH Prkcd Grin2c Glut, Ddx23 r=0.228 rank 1, Psmb4 r=0.227 rank 2, Prpf6 r=0.221 rank 3, Psmc5 r=0.204 rank 4, Psmc1 r=0.200 rank 6; in 155 MB Glut, Prpf6 r=0.220 rank 1, Psmc1 r=0.218 rank 2, Psmb4 r=0.206 rank 3, Pomp r=0.197 rank 5; in 052 Pvalb Gaba, Psmb4 r=0.176 rank 1, Psmc1 r=0.154 rank 2, Pomp r=0.144 rank 3, Prpf6 r=0.131 rank 5; in 066 CNU-HYa HY GABA, Psmc1 r=0.178 rank 1, Ddx23 r=0.168 rank 2, Psmb4 r=0.156 rank 3, Prpf6 r=0.153 rank 4, Pomp r=0.146 rank 5."}
{"target_gene": "Zfhx2", "evidence_id": "E006", "cell_type": null, "statistics": "Across 44 same-cell-type Pearson comparisons of Zfhx2 with Zfhx3 or Zfhx4 score vectors, the largest absolute correlation was |r|=0.0847; Zfhx3 perturbation in 151 TH Prkcd Grin2c Glut produced 5 FDR<0.05 genes including Tagln3 FDR=9.78e-8, whereas Zfhx4 perturbation in 110 CNU-HYa HY MM Glut produced 1 FDR<0.05 gene, Sccpdh FDR=0.0492."}
{"target_gene": "Zfp106", "evidence_id": "E006", "cell_type": "052 Pvalb Gaba", "statistics": "59 perturbed cells versus 13710 controls; Zfp106 logFC 0.207313, p=0.320920, FDR=1.0; Med8 logFC -1.169994, p=0.000018, FDR=0.246102; Ip6k1 logFC -0.602412, p=0.000029, FDR=0.246102; 0 genes at FDR<0.05."}
{"target_gene": "Zfp397", "evidence_id": "E005", "cell_type": "155 MB Glut", "statistics": "0/17442 non-Zfp397 genes with FDR < 0.05; best non-target rows: Ap2a1 score 3.576292 logFC 0.299479 p=0.000349 FDR=1, Irf2 score 3.547924 FDR=1, Rbm12b2 score -3.360078 FDR=1."}
{"target_gene": "Zmynd8", "evidence_id": "E005", "cell_type": null, "statistics": "18 of 22 Zmynd8-tested cell types had zero genes at FDR<0.05. Examples with over 100 perturbed cells but no FDR<0.05 genes were 052 Pvalb Gaba with 134 perturbed cells, 066 CNU-HYa HY GABA with 106, and 022 L5 ET CTX Glut with 104."}
