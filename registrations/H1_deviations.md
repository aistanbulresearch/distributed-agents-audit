# H1 deviations from the frozen pre-registration (`prereg-H1-v1`)

Every choice made after the freeze that the pre-registration does not fix is listed here,
with its reason, before the step it affects is run.

## D-1 — Extraction-quality gate failed on sample 1; single retry with a corrected parser

**What happened.** Section 5's gate was run on sample 1 with the frozen extractor
(`audit/lib/h1_extract.py`, SHA-256 `a95c4220209104aa32271cdd2474383dabed4b540017c3b8063288d03e49f42c`)
against the frozen sample-1 key (644 assertions). Result
(`audit/results/h1/line_h1_gate_sample1_v1.json`): recall 0.806 [0.722, 0.876], precision
0.777 [0.682, 0.859], binding accuracy 0.983 [0.965, 0.995]; recall by type A 0.873, B 0.791,
C 0.542, D 0.286. Recall, precision and the B, C and D type floors fail. Before this run the
freeze guard passed and the reference-equivalence check (section 2) passed
(`audit/results/h1/line_h1_equivalence.json`). No report statistic had been compared with DE
values, and none has been since.

**What section 5 prescribes, and what is done.** The parser is corrected; the corrected code
is committed and its commit hash and file hashes are published here with the reason; only then
is it evaluated, once, on sample 2 against sample 2's key frozen at the freeze. If it fails
again, H1's primary measure is reported as inconclusive. There is no further retry.

**How the correction was made.**
- The frozen extractor is not modified. The correction is a new module,
  `audit/lib/h1_extract_v2.py`, which starts as a copy of `h1_extract.py`. All 25 grammar
  cases of `tests/test_h1_extract.py` still hold for v2 (`tests/test_h1_extract_v2.py`).
- Development data: sample 1 (the gate sample) and ledger rows outside sample 2. The harness
  `audit/scripts/h1_dev_gate.py` loads only the sample-1 key and refuses sample-2 fields. The
  extractor (v1 or v2) has never been run on any sample-2 field; the sample-2 key has not been
  read by any development code.
- Changes (each covered by a test with a verbatim sample-1 or ledger phrasing):
  1. Column-name spellings: `pvals_adj`, `pval_adj`, `adj_p` (adjusted p), `pvals`, `raw p`.
  2. Counts: singular units (`1 row`, `1 gene`), `tests` as rows, counts written as words
     (`zero`/`no`/`none` → `0`; other words kept as written, per the codebook, and only when
     the unit follows directly), `below|under <threshold>`, `<threshold> count=k`, and an
     elided unit after an earlier count in the same sentence (`9 genes had P<0.001 and 61 had
     P<0.01`), which also inherits that count's restriction when it is out of scope; a count
     whose text says the genes "recurred" is out of scope (recurrence).
  3. Row totals (type D): integers only, never a number preceded by a comparison operator;
     descriptive words between the number and `rows/tests` (`Aimp1-target DE`, `gene-level`,
     `gene-by-cell-type`, `non-Ncam1`, `differential-expression`, `target-comparison`); `N genes
     tested`; `rank r/N` as well as `rank r of N`; a rank inside a parenthesis with a
     correlation is out of scope.
  4. Cell counts (type B): `N <Target>-perturbed/-targeted cells`; `n=N` is the number of
     perturbed cells; `over/more than/fewer than/at least N cells` is out of scope.
  5. Minima: `best nominal p` is a minimum; `second-/next-smallest` is not.
  6. Other perturbations (section 3 puts them out of scope), recognised beyond the v1 clause
     pattern: a sentence opened by another gene's perturbation (`X perturbation`, `N X cells
     versus`, `X: N perturbed cells`, `two X FDR<0.05 rows`, `Comparator ...`) and later
     sentences naming that gene; a whole text that never names the target but names another
     perturbation; a clause in which another gene "had/produced/yielded" counts of genes or
     rows, another gene's `self`, `self-…`, `target transcript/FDR/row`, `itself`, or `X N
     rows`. A clause naming the target's own perturbation is exempt from the sentence- and
     text-level rules.
  7. Restricted populations (section 3): additionally `covering <genes>`, `direct`, `none of`,
     `all five had`, `each <noun> had`, self-/target-transcript rows, `target rows`, `<X>-row`,
     and `in all N rows`.
  8. Gene binding stays sentence-local, as section 3 fixes it (an equality with no preceding
     gene token in its sentence remains `unresolved_context`); a bare signed decimal right
     after a gene in a list takes the statistic the list's first item writes first (`Cadm3 logFC -1.227 FDR …, Ptov1 -1.668 FDR …` → logFC; `Nbas score -3.740 logFC …,
     Creb3 +3.436 logFC …` → score); values introduced by `all` are distributive and out of
     scope.
- Development score on sample 1 (not a test; sample 1 was used to build v2): recall 0.921,
  precision 0.988, binding accuracy 0.983; by type A 0.906, B 0.977, C 0.915, D 1.0.
- Adversarial review round 17 led to four changes before publication: a target-transcript
  binding across sentences was removed (it went beyond section 3), elided counts inherit
  their antecedent's restriction, the single attempt is enforced, and the evaluation is bound
  to the published retry code (below).

**Frozen for the evaluation.** The retry is bound like the freeze. The manifest
`registrations/H1_retry.json` (written by `audit/scripts/h1_retry_manifest.py`) lists the
SHA-256 of the corrected parser, its tests, the development harness, the evaluation code and
its tests, this record and the two results that led to the retry, and the commit holding
them; the reference file is bound as in the freeze manifest. The annotated tag
`prereg-H1-retry1` is put on the commit adding the manifest, which is pushed to the public
repository and archived by Software Heritage; the claim (commit and manifest SHA-256) is then
recorded in `registrations/H1_retry_claim.json`.

The evaluation is `line_h1.py gate 2 v2`. It runs the freeze guard; then the retry guard
(the local retry files match the manifest, and the live archive holds the tag, the commit and
the manifest); then reserves the single attempt by creating
`audit/results/h1/line_h1_gate_sample2_v2.attempt.json` atomically (it is never removed, so
an interrupted attempt still counts); only then reads the sample-2 key and runs the frozen
gate code (`audit/lib/h1_quality.py`) with the frozen criteria. Only the pairs (sample 1, v1)
and (sample 2, v2) run. If v2 passes, the comparison (section 6) uses v2; if it fails, H1 is
reported as inconclusive, the mismatch share shown only descriptively next to the failed
criteria.

## D-2 — Counts written as words in the comparison

v2 keeps a count written as a word (`one`, `two`) as written, as the codebook requires. The
frozen matcher reads digits only, so the comparison maps the words one to ten to their numbers
before calling `h1_match.consistent`. The matching rule itself is unchanged.
