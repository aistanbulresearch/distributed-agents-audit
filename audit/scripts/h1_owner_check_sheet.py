"""Build the owner's 30-field check sheet of H1 annotation sample 1 (revision-8 annotation).

Run: uv run python -m audit.scripts.h1_owner_check_sheet <annotation_rev8.jsonl> <sheet_out.md>

The sheet was first produced by this exact code on 2026-10-23 (before any extractor output
existed); the script reproduces it byte for byte. Reads evidence text only.
"""

import json
import logging
import sys
from pathlib import Path

from audit.lib import corpus, paths
from audit.lib.manifest import sha256_file

logger = logging.getLogger(__name__)

SAMPLES = paths.REPO_ROOT / "audit" / "results" / "h1" / "annotation_samples.json"
HEADER = [
    "# H1 annotation — owner's check of 30 fields", "",
    "Fields drawn before the annotation existed (`random.Random(20261025)`, sample 1).",
    "For each field: read the raw text, then mark every annotated assertion in the **Verdict**",
    "column as ✓ (correct in every column) or ✗ with the correction, and list under",
    "**Missed** any in-scope assertion the annotator left out. Section 3 of the",
    "pre-registration is the rule book; the annotator's codebook is in `H1_annotator_prompt.md`.",
    "Your verdicts become the resolved annotation for these 30 fields.", "",
]
COLUMNS = ["| # | quantity | rel | value | cell type | gene | scope | unit | self | threshold "
           "| Verdict |", "|---|---|---|---|---|---|---|---|---|---|---|"]


def _cell(v: object) -> str:
    return "—" if v is None else str(v).replace("|", "\\|")


def build_sheet(check: list[tuple[str, str]], ann: dict, rows: dict) -> str:
    out = list(HEADER)
    for i, key in enumerate(check, 1):
        r, a = rows[key], ann[key]
        out += [f"## {i}. {key[0]} / {key[1]}", "",
                f"Row cell_type field: `{r['cell_type'] or 'empty'}`", "",
                "Raw statistics text:", "", "> " + r["statistics"].replace("\n", " "), ""]
        if a:
            out += COLUMNS
            for j, x in enumerate(a, 1):
                thr = ("—" if x["threshold_quantity"] is None else
                       f"{x['threshold_quantity']} {x['threshold_relation']} "
                       f"{x['threshold_text']}")
                out.append(f"| {j} | {x['quantity']} | {_cell(x['relation'])} | "
                           f"{_cell(x['value_text'])} | {_cell(x['cell_type'])} | "
                           f"{_cell(x['gene'])} | {x['scope']} | {_cell(x['unit'])} | "
                           f"{_cell(x['self_inclusion'])} | {_cell(thr)} | |")
        else:
            out.append("*The annotator found no in-scope assertion in this field.*")
        out += ["", "**Missed:**", "", "---", ""]
    return "\n".join(out)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    ann_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
    paths.check_upstream_pin()
    samples = json.loads(SAMPLES.read_text(encoding="utf-8"))
    check = [tuple(r) for r in samples["owner_check"]]
    ann = {}
    for line in ann_path.read_text(encoding="utf-8").splitlines():
        o = json.loads(line)
        ann[(o["target_gene"], o["evidence_id"])] = o["assertions"]
    rows = {(r["target_gene"], r["evidence_id"]): r
            for r in corpus.read_csv_checked(paths.release_dir() / "ledgers" / "evidence.csv")}
    out_path.write_text(build_sheet(check, ann, rows), encoding="utf-8", newline="\n")
    logger.info("wrote %s, sha256 %s", out_path, sha256_file(out_path))


if __name__ == "__main__":
    main()
