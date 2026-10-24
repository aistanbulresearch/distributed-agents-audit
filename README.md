# Distributed Agents Corpus Audit

An independent audit of the literature corpus released with:

> Sun A, Park JJ, DeTomaso D, et al. *Distributed AI agents enable comprehensive
> discovery of biological insights at scale.* bioRxiv 2026.10.15.759436.
> DOI: [10.64898/2026.10.15.759436](https://doi.org/10.64898/2026.10.15.759436)

The paper validates its agent output against the source study's findings, held-out
perturbations, and measured cell depletion. It does not measure whether the 16,580
references in the released corpus exist or support the findings they are attached to.
This repository measures that. It audits the released output, not the generation process.

## Upstream input (read-only)

The authors' repository is included as a git submodule, pinned to one commit:

| | |
|---|---|
| Repository | https://github.com/jinlabneurogenomics/distributed_agent |
| Path | `upstream/distributed_agent` |
| Commit | `c20445d929f5aedce1d539ef6fbd8843b8c06e25` (2026-10-21) |
| License | MIT |

Nothing under `upstream/` is modified by this audit. Audit scripts read from it and write
only under `audit/`. Moving the pin is a deliberate, separately committed change.

## Setup

```bash
git clone --recurse-submodules https://github.com/aistanbulresearch/distributed-agents-audit
cd distributed-agents-audit/upstream/distributed_agent
git lfs install
git lfs pull
```

On Windows, clone with `git -c core.longpaths=true clone --recurse-submodules ...` and run
`git config core.longpaths true` inside the submodule. Two upstream files under
`shi_holdout/skills/` exceed the 260-character path limit when the clone sits in a deep
directory, and the submodule checkout aborts without it.

`git lfs pull` is required: key files under `data/` (for example
`data/tables/literature/final_classified_findings.csv`) arrive as LFS pointers otherwise.
To skip the LFS download during the initial clone, set `GIT_LFS_SKIP_SMUDGE=1`.

## Reference data

Line H1 compares reported statistics with the differential-expression results released on
Hugging Face (`perturbai/wholebrain_crispr_atlas`, revision
`a7c65dc0a64da4bd47cf6ef5f4dec6c7ef745e87`,
`analysis/2603_shi_manuscript/diff_expr_genes/wilcoxon_de_results_group_name_final_data_no_multi_guide_cells.parquet`,
10.8 GB). Place it under a data cache at
`hf/perturbai__wholebrain_crispr_atlas/<revision>/<path>`; the cache defaults to
`../data-cache` next to the clone and can be set with `CORPUS_AUDIT_DATA_CACHE`. Its SHA-256
is in `inputs/MANIFEST.sha256` and in the freeze manifest.

## Layout

```
upstream/distributed_agent/   pinned authors' repository (read-only)
registrations/                frozen pre-registrations, annotation keys and freeze manifests
audit/lib/                    extraction, matching, sampling, statistics and freeze checks
audit/scripts/                one script per step; every published number comes from one
audit/templates/              annotator packet template
audit/results/                tables produced by the scripts
inputs/MANIFEST.sha256        SHA-256 of every external input
tests/                        unit tests
```

## Rules

1. The pre-registration is committed before the data it governs is analysed.
2. Every number in a results table or in the write-up comes from a script in this repository.
3. Each claim is marked as an observation or an inference.
4. Negative results are reported as they are.

## Status

Line H1 (data consistency of quantitative evidence) is pre-registered and frozen under the
tag `prereg-H1-v1`: `registrations/H1.md` is the protocol, `registrations/H1_freeze.json`
lists the SHA-256 of every frozen file and of the reference data. To check the freeze from a
fresh clone (submodule initialised, LFS files pulled, reference data in the data cache):

```bash
uv run python -m audit.scripts.h1_replay_freeze
```

No outcome has been computed before this freeze.
