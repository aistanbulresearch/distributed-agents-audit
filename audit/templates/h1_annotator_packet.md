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

**Output.** Write exactly one file: `{OUTPUT_PATH}`, UTF-8, exactly 150 lines, one JSON
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

