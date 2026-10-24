"""Check both annotators' files for one H1 sample, pair them and build the owner's forms.

Run: uv run python -m audit.scripts.h1_pair_annotations <sample: 1|2> <annotator_A.jsonl>
         <annotator_B.jsonl> <out_dir>

Writes to ``out_dir``: ``H1_pairing_sample<n>.json`` (format check, file hashes, A-B
agreement, per-field status), ``H1_adjudication_sample<n>.md`` (every partially disagreeing
field, both versions as blind X/Y) and ``H1_agreement_audit_sample<n>.md`` (the drawn fully
agreed fields). For sample 1 the owner-checked fields are excluded (their resolution is
final). Reads evidence text only, never DE values or extractor output. Exits 1 on any
format problem, before pairing.
"""

import hashlib
import json
import logging
import sys
from pathlib import Path

from audit.lib import corpus, paths
from audit.lib.h1_annotation import (
    agreement_summary,
    check_format,
    compare_field,
    include_as_unstated,
    parse,
)
from audit.lib.h1_quality import Annotated
from audit.lib.h1_sampling import agreement_audit_sample, xy_assignment

logger = logging.getLogger(__name__)

SAMPLES = paths.REPO_ROOT / "audit" / "results" / "h1" / "annotation_samples.json"
RECON = paths.REPO_ROOT / "audit" / "results" / "recon" / "inventory.json"
SAMPLE_KEYS = {1: "sample1", 2: "sample2_reserved"}
COLUMNS = "| # | source | quantity | rel | value | cell type | gene | scope | unit | self | " \
          "threshold | differs | Ruling |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|"
AUDIT_COLUMNS = "| # | quantity | rel | value | cell type | gene | scope | unit | self | " \
                "threshold | Verdict |\n|---|---|---|---|---|---|---|---|---|---|---|"
MISSED = ("**Missed by both** (add one row per in-scope assertion neither version lists):\n\n"
          "| quantity | rel | value | cell type | gene | scope | unit | self | threshold |\n"
          "|---|---|---|---|---|---|---|---|---|\n")

ADJUDICATION_HEAD = """# H1 annotation, sample {n}: whole-field adjudication

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

{count} fields.

"""

AUDIT_HEAD = """# H1 annotation, sample {n}: agreement audit

Both annotators produced identical annotations for each field below; these {count} fields
were drawn at random among such fields (`agreement_audit_sample`, seed {seed}). Check each
against section 3 (`H1_section3_rev10.md`): mark every row `✓` or `✗` (with the correction),
and add any in-scope assertion both missed under **Missed by both**. A single error in this
sample triggers the review of all its remaining agreed fields (decision DC-33).

Türkçe özet: Bu metinlerde iki notlayıcı tamamen aynı sonucu verdi. Her satırı ✓ veya ✗ ile
işaretleyin, ikisinin de atladığı ölçümleri ekleyin. Tek bir hata bile bulunursa o örneklemin
anlaşılan tüm metinleri gözden geçirilir.

"""


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _cells(a: Annotated) -> list[str]:
    threshold = " ".join(x for x in (a.threshold_quantity, a.threshold_relation,
                                     a.threshold_text) if x) or "—"
    return [a.quantity, a.relation, a.value_text, a.cell_type or "—", a.gene or "—", a.scope,
            a.unit or "—", a.self_inclusion or "—", threshold]


def _field_head(i: int, row: tuple[str, str], ledger_row: dict) -> str:
    return (f"## {i}. {row[0]} / {row[1]}\n\nRow cell_type field: "
            f"`{ledger_row['cell_type'] or 'empty'}`\n\nRaw statistics text:\n\n"
            f"> {ledger_row['statistics']}\n\n")


def _adjudication_rows(row: tuple[str, str], x: list[Annotated], y: list[Annotated]
                       ) -> list[str]:
    """Rows in X's order, each X row followed by its differing Y counterpart; Y-only last.
    Pairing is symmetric (k-th occurrence of a value with k-th), so X/Y orientation is safe."""
    c = compare_field(row, x, y)
    status: dict[int, tuple[Annotated, list[str]] | None] = {id(a): None for a, _ in c.agreed}
    status.update({id(a): (b, diff) for a, b, diff in c.differing})
    rows: list[tuple[str, Annotated, list[str]]] = []
    for a in x:
        if id(a) not in status:
            rows.append(("X", a, []))
        elif (entry := status[id(a)]) is None:
            rows.append(("X+Y", a, []))
        else:
            rows += [("X≠", a, entry[1]), ("Y≠", entry[0], entry[1])]
    rows += [("Y", b, []) for b in c.only_b]
    return ["| " + " | ".join([str(n), source, *_cells(ann), ", ".join(diff), ""]) + " |"
            for n, (source, ann, diff) in enumerate(rows, start=1)]


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    sample = int(sys.argv[1])
    a_path, b_path, out_dir = Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
    paths.check_upstream_pin()
    samples = json.loads(SAMPLES.read_text(encoding="utf-8"))
    expected = [tuple(r) for r in samples[SAMPLE_KEYS[sample]]]
    owner_checked = {tuple(r) for r in samples["owner_check"]} if sample == 1 else set()
    labels = set(json.loads(RECON.read_text(encoding="utf-8"))
                 ["differential_expression"]["groups"])
    lines = {}
    problems = {}
    for name, path in (("A", a_path), ("B", b_path)):
        lines[name] = path.read_text(encoding="utf-8").splitlines()
        problems[name] = check_format(lines[name], expected, labels)
        logger.info("annotator %s: %s, %d format problems", name, path.name,
                    len(problems[name]))
        for p in problems[name]:
            logger.info("  %s", p)
    if problems["A"] or problems["B"]:
        sys.exit(1)
    ann_a, ann_b = parse(lines["A"]), parse(lines["B"])
    paired_rows = [row for row in expected if row not in owner_checked]
    comps = [compare_field(row, ann_a[row], ann_b[row]) for row in paired_rows]
    summary = agreement_summary(comps)
    agreed_rows = [c.row for c in comps if c.fully_agreed]
    disagreeing = [c for c in comps if not c.fully_agreed]
    a_is_x = xy_assignment(expected, sample)
    audit_rows = agreement_audit_sample(agreed_rows, sample)
    ledger = {(r["target_gene"], r["evidence_id"]): r for r in
              corpus.read_csv_checked(paths.release_dir() / "ledgers" / "evidence.csv")}
    conv = [compare_field(row,
                          include_as_unstated(ann_a[row], ledger[row]["statistics"], row[0]),
                          include_as_unstated(ann_b[row], ledger[row]["statistics"], row[0]))
            for row in paired_rows]

    adjudication = [ADJUDICATION_HEAD.format(n=sample, count=len(disagreeing))]
    for i, c in enumerate(disagreeing, start=1):
        # Shown under the label convention so the raw include/unstated habit cannot reveal
        # which annotator is X (review round 13); classification above stays raw.
        text = ledger[c.row]["statistics"]
        shown_a = include_as_unstated(ann_a[c.row], text, c.row[0])
        shown_b = include_as_unstated(ann_b[c.row], text, c.row[0])
        x, y = (shown_a, shown_b) if a_is_x[c.row] else (shown_b, shown_a)
        adjudication.append(_field_head(i, c.row, ledger[c.row]) + COLUMNS + "\n"
                            + "\n".join(_adjudication_rows(c.row, x, y)) + "\n\n"
                            + MISSED + "\n---\n\n")
    audit = [AUDIT_HEAD.format(n=sample, count=len(audit_rows),
                               seed={1: 20261027, 2: 20261029}[sample])]
    for i, row in enumerate(audit_rows, start=1):
        rows = [f"| {n} | " + " | ".join(_cells(a)) + " |  |"
                for n, a in enumerate(ann_a[row], start=1)]
        body = (AUDIT_COLUMNS + "\n" + "\n".join(rows) + "\n\n" if rows else
                "*Both annotators found no in-scope assertion in this field.*\n\n")
        audit.append(_field_head(i, row, ledger[row]) + body + MISSED + "\n---\n\n")

    out_dir.mkdir(parents=True, exist_ok=True)
    adj_path = out_dir / f"H1_adjudication_sample{sample}.md"
    audit_path = out_dir / f"H1_agreement_audit_sample{sample}.md"
    adj_path.write_text("".join(adjudication), encoding="utf-8", newline="\n")
    audit_path.write_text("".join(audit), encoding="utf-8", newline="\n")
    report = {
        "sample": sample,
        "files": {"A": {"path": a_path.name, "sha256": _sha256(a_path),
                        "assertions": sum(len(v) for v in ann_a.values())},
                  "B": {"path": b_path.name, "sha256": _sha256(b_path),
                        "assertions": sum(len(v) for v in ann_b.values())}},
        "format_problems": 0,
        "owner_checked_excluded": len(owner_checked),
        "agreement": summary,
        "agreement_label_convention": agreement_summary(conv),
        "partially_disagreeing": [list(c.row) for c in disagreeing],
        "agreement_audit": [list(r) for r in audit_rows],
        "forms": {adj_path.name: _sha256(adj_path), audit_path.name: _sha256(audit_path)},
    }
    json_path = out_dir / f"H1_pairing_sample{sample}.json"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8", newline="\n")
    logger.info("%s", json.dumps(summary))
    logger.info("partially disagreeing %d, audit %d; wrote %s", len(disagreeing),
                len(audit_rows), json_path)


if __name__ == "__main__":
    main()
