"""H1 extraction grammar: atomic quantitative assertions from evidence ``statistics`` text.

Works on text and vocabularies only (cell-type labels, measured gene names); it never reads
DE values. The grammar is defined by ``tests/test_h1_extract.py`` and by section 3 of the
H1 pre-registration.

Pipeline per text: normalise numbers -> mask cell-type labels -> split sentences and
clauses -> mask out-of-scope numbers (correlations, ranges, summaries, approximations) ->
match in-scope patterns in a fixed order, masking each match -> bind cell type and gene.
"""

import re
from dataclasses import dataclass

NUM = r"[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?"
_LABEL_MASK = "§"
_SPAN_MASK = "¤"
_ABBREVIATIONS = {"vs", "e.g", "i.e", "ca", "approx", "fig", "al", "cf"}
_PADJ = r"FDR|q|padj|p_adj|adjusted\s+p"
_PVAL = r"nominal\s+p|p"


@dataclass(frozen=True)
class Vocabulary:
    cell_types: tuple[str, ...]
    genes: frozenset[str]


@dataclass(frozen=True)
class Assertion:
    target: str
    quantity: str  # logfc score pval padj n_pert n_ctrl n_sig n_rows min_pval min_padj other
    relation: str
    value_text: str
    cell_type: str | None
    cell_source: str | None  # "sentence", "row" or None
    gene: str | None
    scope: str  # "gene", "cell" or "target"
    status: str  # "extracted", "unresolved_context" or "out_of_scope"
    reason: str | None = None
    threshold_quantity: str | None = None
    threshold_relation: str | None = None
    threshold_text: str | None = None
    unit: str | None = None
    self_inclusion: str | None = None  # counts: "include", "exclude" or "unstated"
    start: int = 0


def normalise(text: str) -> str:
    """Unicode minus to ASCII; ``3.1 x 10^-5`` to ``3.1e-5``."""
    text = text.replace("−", "-").replace("≤", "<=").replace("≥", ">=")
    return re.sub(r"(\d(?:\.\d+)?)\s*[x×]\s*10\^?\s*([+-]?\d+)", r"\1e\2", text)


def _label_spans(text: str, labels: tuple[str, ...]) -> list[tuple[int, int, str]]:
    spans: list[tuple[int, int, str]] = []
    for label in sorted(labels, key=len, reverse=True):
        for m in re.finditer(rf"(?<![\w-]){re.escape(label)}(?![\w-])", text):
            if all(m.end() <= s or m.start() >= e for s, e, _ in spans):
                spans.append((m.start(), m.end(), label))
    return sorted(spans)


def _mask(text: str, start: int, end: int, char: str) -> str:
    return text[:start] + char * (end - start) + text[end:]


def _sentences(masked: str) -> list[tuple[int, int]]:
    cuts = [0]
    for m in re.finditer(r"\.\s+(?=[A-Z0-9§(])|\n+", masked):
        word = re.search(r"([A-Za-z.]+)$", masked[cuts[-1]:m.start()])
        if m.group().startswith(".") and word and word.group(1).lower() in _ABBREVIATIONS:
            continue
        cuts.append(m.end())
    cuts.append(len(masked))
    return [(a, b) for a, b in zip(cuts, cuts[1:], strict=False) if b > a]


def _clause_bounds(masked: str, start: int, end: int, pos: int) -> tuple[int, int]:
    left = masked.rfind(";", start, pos)
    right = masked.find(";", pos, end)
    return (left + 1 if left >= 0 else start), (right if right >= 0 else end)


_RECURRENCE = (
    re.compile(r"(?i)(?<![\w.])\d+\s*(?:/|of)\s*\d+\s+(?:[\w-]+\s+){0,2}"
               r"(?:cell[\s-]types?|cell\s+classes|classes|signatures|contrasts|tests|groups)\b"),
    re.compile(r"(?i)(?<![\w.])\d+\s*/\s*\d+\s+(?:had|were|showed|reached|passed)\b"),
    re.compile(r"(?i)\b(?:in|across)\s+\d+\s*/\s*\d+\b"),
)
_OTHER_PERTURBATION = re.compile(
    r"\b(?P<g>[A-Za-z][A-Za-z0-9]*)(?:[\s-]perturb(?:ation|ed)\b|\s+knockout\b|[\s-]KO\b)")

_OUT_OF_SCOPE = (
    # Any numeric range (0.895-0.917, 23-191, -0.21 to -0.4) before anything else, so that
    # neither endpoint can be read as a scalar or a signed value.
    ("range", re.compile(
        rf"(?<![\w.,]){NUM}(?:\s*[-–—]\s*|\s+to\s+){NUM}(?!\w|\.\d)")),
    ("correlation", re.compile(
        rf"(?i)\b(?:pearson\s+|spearman\s+)?(?:r|rho|ρ|cosine(?:\s+similarity)?|"
        rf"correlation)\s*(?:=|:|of|was)?\s*{NUM}")),
    ("range", re.compile(rf"(?i)\b(?:ranged?|ranging)\s+from\s+{NUM}\s+(?:to|-)\s+{NUM}")),
    ("range", re.compile(rf"(?i)\bbetween\s+{NUM}\s+and\s+{NUM}")),
    ("summary_statistic", re.compile(
        rf"(?i)\b(?:median|mean|average|maximum|max)\b(?:\s+[A-Za-z_-]+){{0,2}}"
        rf"\s*(?:=|:|of|was)?\s*{NUM}")),
    ("approximation", re.compile(
        rf"(?i)(?:~|≈|\bapproximately\b|\babout\b|\broughly\b|\bnearly\b)\s*{NUM}")),
)

_P_NMATCH = re.compile(rf"(?i)\bn_(?P<w>pert|ctrl)(?:_matched)?\s*(?:=|:|was|of)?\s*(?P<n>{NUM})")
_P_CTRL = re.compile(
    rf"(?i)(?<![\w.,-])(?P<m>{NUM})\s+(?:matched\s+)?(?:non-targeting\s+|NTC\s+)?"
    rf"(?:controls?|NTC)(?:\s+(?:cells|nuclei))?\b")
# Threshold before unit: "0 FDR<0.05 genes", "No FDR <0.05 genes".
_P_SIG_THRESHOLD_FIRST = re.compile(
    rf"(?i)(?<![\w.,])(?P<k>{NUM}|no)\s+(?P<q>{_PADJ}|{_PVAL})\s*(?P<rel><=|<)\s*"
    rf"(?P<thr>{NUM})\s+(?:[A-Za-z][\w-]*\s+){{0,2}}?(?P<unit>genes|rows|DEGs?|transcripts)\b")
# Unit before threshold: "37 genes at FDR<0.05", "6 Ap3b1 rows had FDR<1.0", "1/17443 genes",
# optionally followed by a denominator: "... at FDR<0.05 among 17442 tested".
_P_SIG = re.compile(
    rf"(?i)(?<![\w.,])(?P<k>{NUM})(?:\s*(?:/|of)\s*(?P<N>{NUM}))?\s+"
    rf"(?:[A-Za-z][\w-]*\s+){{0,2}}?(?P<unit>genes|rows|DEGs?|transcripts)\b[^;.]{{0,60}}?"
    rf"(?P<q>{_PADJ}|{_PVAL})\s*(?P<rel><=|<)\s*(?P<thr>{NUM})"
    rf"(?:\s+among\s+(?P<M>{NUM})(?:\s+(?:genes|rows|transcripts))?(?:\s+tested)?)?")
# Counts over a restricted population ("41 selected genes", "these markers") are not
# representable as a whole cell type or target, so they are out of scope.
_SUBSET = re.compile(
    r"(?i)\b(?:selected|listed|prespecified|pre-specified|candidate|chosen|curated|panel|"
    r"module|these|those)\b")
_P_ROWS = re.compile(
    rf"(?i)(?<![\w.])(?P<N>{NUM})\s+(?:(?:Wilcoxon|DE|parquet|result|non-?target|non-?self)\s+)?"
    rf"rows\b")
_P_RANK = re.compile(rf"(?i)\brank\s+{NUM}\s+of\s+(?P<N>{NUM})")
_P_MIN = re.compile(
    rf"(?i)\b(?:global\s+)?(?:minimum|min\.?|lowest|smallest)\s+(?:nominal\s+)?"
    rf"(?P<q>{_PADJ}|p(?:-value|\s+value)?)\s*(?:was|of|is|=|:)?\s*"
    rf"(?P<rel><=|>=|<|>|=)?\s*(?P<num>{NUM})")
_P_VALUE = re.compile(
    rf"(?<![\w-])(?P<key>(?i:log2?\s*FC|log2?\s*fold[\s-]change|logfoldchanges?|score|z|"
    rf"{_PADJ}|{_PVAL})(?:[\s-]?value)?)(?![\w-])\s*(?:(?i:was|of|is)\s*)?"
    rf"(?P<rel><=|>=|<|>|=|:)?\s*(?P<num>{NUM})")
_GENE_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-.][A-Za-z0-9]+)*")


def _key_quantity(key: str) -> str:
    key = re.sub(r"\s+", " ", key.lower())
    if key.startswith("log"):
        return "logfc"
    if key in ("score", "z"):
        return "score"
    if re.fullmatch(r"(?:fdr|q|padj|p_adj|adjusted p)(?:[ -]?value)?", key):
        return "padj"
    return "pval"


def _threshold_quantity(q: str) -> str:
    return "padj" if re.fullmatch(rf"(?i){_PADJ}", q.strip()) else "pval"


class _Context:
    """Per-text state: label spans, sentence bounds and binding helpers."""

    def __init__(self, text: str, target: str, row_cell: str | None, vocab: Vocabulary):
        self.target, self.row_cell, self.vocab = target, (row_cell or None), vocab
        self.labels = _label_spans(text, vocab.cell_types)
        masked = text
        for start, end, _ in self.labels:
            masked = _mask(masked, start, end, _LABEL_MASK)
        self.masked = masked

    def cell(self, sent: tuple[int, int], pos: int,
             inherit: bool) -> tuple[str | None, str | None]:
        """Cell type for an assertion at ``pos``.

        Order: nearest label earlier in the same clause; first label later in the same clause
        without crossing a colon; (only if ``inherit``) nearest label earlier in the
        sentence; the row's cell_type field.
        """
        c0, c1 = _clause_bounds(self.masked, *sent, pos)
        before = [lab for s, e, lab in self.labels if c0 <= s and e <= pos]
        if before:
            return before[-1], "clause"
        colon = self.masked.find(":", pos, c1)
        segment_end = colon if colon >= 0 else c1
        after = [lab for s, e, lab in self.labels if pos <= s and e <= segment_end]
        if after:
            return after[0], "clause"
        if inherit:
            earlier = [lab for s, e, lab in self.labels if sent[0] <= s and e <= pos]
            if earlier:
                return earlier[-1], "sentence"
        return (self.row_cell, "row") if self.row_cell else (None, None)

    def gene(self, sent: tuple[int, int], pos: int) -> str | None:
        tokens = [m.group() for m in _GENE_TOKEN.finditer(self.masked, sent[0], pos)]
        return next((t for t in reversed(tokens) if t in self.vocab.genes), None)

    def adjacent_gene(self, pos: int) -> str | None:
        """Gene token directly before ``pos``, optionally followed by "self" or "target"."""
        m = re.search(r"([A-Za-z][\w.-]*)\s+(?:(?:self|target)\s+)?$", self.masked[:pos])
        return m.group(1) if m and m.group(1) in self.vocab.genes else None

    def clause_flag(self, sent: tuple[int, int], pos: int) -> str | None:
        c0, c1 = _clause_bounds(self.masked, *sent, pos)
        clause = self.masked[c0:c1]
        if any(p.search(clause) for p in _RECURRENCE):
            return "recurrence"
        for m in _OTHER_PERTURBATION.finditer(clause):
            g = m.group("g")
            if g.lower() != self.target.lower() and g in self.vocab.genes:
                return "other_perturbation"
        return None


def extract(statistics: str, target: str, row_cell_type: str | None,
            vocab: Vocabulary) -> list[Assertion]:
    """Extract assertions from one evidence ``statistics`` field."""
    if not statistics.strip():
        return []
    ctx = _Context(normalise(statistics), target, row_cell_type, vocab)
    out: list[Assertion] = []
    for sent in _sentences(ctx.masked):
        work = ctx.masked
        for reason, pattern in _OUT_OF_SCOPE:
            for m in pattern.finditer(work, *sent):
                out.append(_assertion(ctx, sent, m.start(), "other", "=", m.group(),
                                      status="out_of_scope", reason=reason))
                work = _mask(work, m.start(), m.end(), _SPAN_MASK)
        work = _match_in_scope(ctx, sent, work, out)
    return sorted(out, key=lambda a: a.start)


def _assertion(ctx: _Context, sent: tuple[int, int], pos: int, quantity: str, relation: str,
               value_text: str, *, scope: str = "cell", gene: str | None = None,
               needs_gene: bool = False, needs_cell: bool = True, inherit: bool = False,
               status: str | None = None, reason: str | None = None, **extra) -> Assertion:
    cell, source = ctx.cell(sent, pos, inherit=inherit)
    if status is None:
        reason = ctx.clause_flag(sent, pos)
        if reason:
            status = "out_of_scope"
        elif (needs_gene and gene is None) or (needs_cell and cell is None):
            status = "unresolved_context"
        else:
            status = "extracted"
    if scope == "cell" and cell is None and not needs_cell:
        scope = "target"
    return Assertion(target=ctx.target, quantity=quantity, relation=relation,
                     value_text=value_text, cell_type=cell, cell_source=source, gene=gene,
                     scope=scope, status=status, reason=reason, start=pos, **extra)


def _match_in_scope(ctx: _Context, sent: tuple[int, int], work: str,
                    out: list[Assertion]) -> str:
    def take(pattern: re.Pattern[str]) -> list[re.Match[str]]:
        nonlocal work
        found = list(pattern.finditer(work, *sent))
        for m in found:
            work = _mask(work, m.start(), m.end(), _SPAN_MASK)
        return found

    target = re.escape(ctx.target)
    versus = re.compile(
        rf"(?i)(?<![\w.,-])(?P<n>{NUM})\s+(?:{target}\s+)?(?:matched\s+)?"
        rf"(?:perturbed(?:\s+(?:cells|nuclei))?|cells|nuclei)\s+"
        rf"(?:versus|vs\.?|against|compared\s+with)\s+(?P<m>{NUM})\s+(?:matched\s+)?"
        rf"(?:non-targeting\s+)?(?:control|NTC)")
    for m in take(versus):
        out.append(_assertion(ctx, sent, m.start(), "n_pert", "=", m.group("n")))
        out.append(_assertion(ctx, sent, m.start(), "n_ctrl", "=", m.group("m")))
    for m in take(_P_NMATCH):
        out.append(_assertion(ctx, sent, m.start(), f"n_{m.group('w').lower()}", "=",
                              m.group("n")))
    for m in take(_P_CTRL):
        out.append(_assertion(ctx, sent, m.start(), "n_ctrl", "=", m.group("m")))
    cells = re.compile(rf"(?<![\w.,-])(?P<n>{NUM})\s+(?:{target}\s+)?(?:perturbed\s+)?"
                       rf"(?:cells|nuclei)\b")
    for m in take(cells):
        out.append(_assertion(ctx, sent, m.start(), "n_pert", "=", m.group("n")))
    for m in take(_P_SIG_THRESHOLD_FIRST):
        k = "0" if m.group("k").lower() == "no" else m.group("k")
        out.append(_count(ctx, sent, m, k, _lead_in(ctx, sent, work, m)))
    for m in take(_P_SIG):
        lead = _lead_in(ctx, sent, work, m)
        out.append(_count(ctx, sent, m, m.group("k"), lead))
        total = m.group("N") or m.group("M")
        if total:
            status, reason = _subset_status(lead)
            out.append(_assertion(ctx, sent, m.start(), "n_rows", "=", total, needs_cell=False,
                                  unit=_unit(m.group("unit")),
                                  self_inclusion=_self_inclusion(lead, ctx.target),
                                  status=status, reason=reason))
    for m in take(_P_RANK):
        out.append(_assertion(ctx, sent, m.start(), "n_rows", "=", m.group("N"), unit="genes"))
    for m in take(_P_ROWS):
        lead = _lead_in(ctx, sent, work, m)
        status, reason = _subset_status(lead)
        out.append(_assertion(ctx, sent, m.start(), "n_rows", "=", m.group("N"),
                              needs_cell=False, unit="rows",
                              self_inclusion=_self_inclusion(lead, ctx.target),
                              status=status, reason=reason))
    for m in take(_P_MIN):
        gene = ctx.adjacent_gene(m.start())
        quantity = "min_padj" if _threshold_quantity(m.group("q")) == "padj" else "min_pval"
        status, reason = _subset_status(_lead_in(ctx, sent, work, m))
        out.append(_assertion(ctx, sent, m.start(), quantity, m.group("rel") or "=",
                              m.group("num"), gene=gene, needs_cell=False,
                              scope="gene" if gene else "cell", status=status, reason=reason))
    for m in take(_P_VALUE):
        relation = m.group("rel") or "="
        # Equalities bind to the nearest preceding gene; inequalities only to an adjacent one,
        # so aggregate thresholds ("overall FDR<0.05") never become gene assertions.
        if relation in ("=", ":"):
            gene = ctx.gene(sent, m.start())
        else:
            gene = ctx.adjacent_gene(m.start())
        out.append(_assertion(ctx, sent, m.start(), _key_quantity(m.group("key")),
                              relation, m.group("num"), gene=gene, needs_gene=True,
                              scope="gene", inherit=True))
    return work


def _lead_in(ctx: _Context, sent: tuple[int, int], work: str, m: re.Match[str]) -> str:
    """The count's own text plus its lead-in: from the end of the previous masked match in
    the same clause (or the clause start) to the end of this match. Qualifiers of an earlier
    count therefore do not carry over."""
    c0, _ = _clause_bounds(ctx.masked, *sent, m.start())
    previous = work.rfind(_SPAN_MASK, c0, m.start())
    return ctx.masked[(previous + 1 if previous >= 0 else c0):m.end()]


def _self_inclusion(text: str, target: str) -> str:
    t = re.escape(target)
    excluded = (rf"(?i)\bnon-?target\b|\bnon-?self\b|\bnon-{t}\b|"
                rf"\bexcluding\s+(?:the\s+)?(?:target|{t})\b|"
                rf"\bother\s+than\s+(?:the\s+)?(?:target|{t})\b")
    if re.search(excluded, text):
        return "exclude"
    if re.search(rf"(?i)\bincluding\s+(?:the\s+)?(?:target|{t})\b", text):
        return "include"
    return "unstated"


def _subset_status(text: str) -> tuple[str | None, str | None]:
    """(status, reason) for a count whose lead-in restricts it to a subset; else (None, None)."""
    return ("out_of_scope", "subset_scope") if _SUBSET.search(text) else (None, None)


def _unit(unit: str) -> str:
    return "rows" if unit.lower() == "rows" else "genes"


def _count(ctx: _Context, sent: tuple[int, int], m: re.Match[str], k: str,
           lead: str) -> Assertion:
    status, reason = _subset_status(lead)
    return _assertion(ctx, sent, m.start(), "n_sig", "=", k, needs_cell=False,
                      threshold_quantity=_threshold_quantity(m.group("q")),
                      threshold_relation=m.group("rel"), threshold_text=m.group("thr"),
                      unit=_unit(m.group("unit")),
                      self_inclusion=_self_inclusion(lead, ctx.target),
                      status=status, reason=reason)
