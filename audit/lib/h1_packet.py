"""Build the H1 annotator packet (pre-registration, section 5).

The packet is: the instruction template (``audit/templates/h1_annotator_packet.md``) with
the annotation output path filled in, the cell-type labels as a bullet list, the frozen
section-3 text, and one JSON line per sampled field. The same function builds every
annotator's packet for both samples, so annotators of a sample receive identical bytes.
"""

import json
from collections.abc import Iterable, Mapping

OUTPUT_PLACEHOLDER = "{OUTPUT_PATH}"


def build_packet(template: str, output_path: str, cell_types: Iterable[str], section3: str,
                 rows: Iterable[Mapping[str, str]]) -> str:
    """Return the packet text. ``rows`` are evidence rows in sample order."""
    if template.count(OUTPUT_PLACEHOLDER) != 1:
        raise ValueError(f"template must contain {OUTPUT_PLACEHOLDER} exactly once")
    labels = "\n".join(f"- `{label}`" for label in cell_types)
    fields = "\n".join(
        json.dumps({"target_gene": r["target_gene"], "evidence_id": r["evidence_id"],
                    "cell_type": r["cell_type"] or None, "statistics": r["statistics"]},
                   ensure_ascii=False)
        for r in rows)
    return (template.replace(OUTPUT_PLACEHOLDER, output_path) + labels + "\n\n" + section3
            + "\n\n## The 150 fields\n\n" + fields + "\n")
