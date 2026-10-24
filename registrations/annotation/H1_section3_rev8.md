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
  Regression: Ndufv1/E008.
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