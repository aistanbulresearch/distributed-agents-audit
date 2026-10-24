"""H1 extraction grammar, version 2 (the single pre-registered retry; see
``registrations/H1_deviations.md``): atomic quantitative assertions from evidence
``statistics`` text. Version 1 (``h1_extract.py``) is frozen and unchanged.

Works on text and vocabularies only (cell-type labels, measured gene names); it never reads
DE values. The grammar is defined by ``tests/test_h1_extract.py`` and by section 3 of the
H1 pre-registration.

Pipeline per text: normalise numbers -> mask cell-type labels -> split sentences and
clauses -> mask out-of-scope numbers (correlations, ranges, summaries, approximations) ->
match in-scope patterns in a fixed order, masking each match -> bind cell type and gene.
"""

import re
from dataclasses import dataclass, replace

NUM = r"[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?"
_LABEL_MASK = "§"
_SPAN_MASK = "¤"
_ABBREVIATIONS = {"vs", "e.g", "i.e", "ca", "approx", "fig", "al", "cf"}
_PADJ = r"FDR|q|pvals_adj|pval_adj|padj|p_adj|adj_p|adjusted\s+p"
_PVAL = r"nominal\s+p|raw\s+p|pvals|p"


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
    r"\b(?P<g>[A-Za-z][A-Za-z0-9]*)(?:[\s-]perturb(?:ations?|ed)\b|\s+knockout\b|[\s-]KO\b"
    r"|[\s-]self\b|\s+self-\w+|\s+(?:target\s+(?:transcript|FDR|row|rows|p)\b)"
    r"|\s+itself\b|\s+in\s+§+\s+had\s+(?:its\s+own|[A-Z][a-z0-9]+\s+(?:log|score|p\b|FDR)))")
_GENE = r"[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*"
# A gene (or a list of genes) that "had/produced/yielded" counts of genes or rows is a
# perturbation: "Cul3 had 1 FDR<0.05 gene", "Purb and Purg produced 0 FDR<0.05 genes",
# "B9d1 in 308 CB GABA had 9 FDR<0.05 genes", "Arhgef9 338323 rows".
_PERTURBATION_SUBJECT = re.compile(
    rf"(?P<gs>{_GENE}(?:\s*,\s*{_GENE})*(?:,?\s+and\s+{_GENE})?)(?:\s+itself)?"
    rf"(?:\s+in\s+§+)?(?:\s+n\s*=\s*\d[\d,]*)?\s+(?:had|has|produced|yielded|returned|showed|"
    rf"each\s+with)\b"
    rf"(?=[^;]*?(?<![\w.])(?:\d[\d,]*|no|zero|one|two|three)\s+(?:[^\s;]+\s+){{0,3}}?"
    rf"(?:genes?|rows?|DEGs?)\b)")
_GENE_ROWS = re.compile(rf"(?P<gs>{_GENE})\s+\d[\d,]*\s+(?:[\w-]+\s+)?rows\b"
                        rf"|(?P<gs2>{_GENE})\s+n\s*=\s*\d[\d,]*\s+had\s+\d")
# Sentence openings that put the whole sentence under another perturbation.
_SENTENCE_LEAD = re.compile(
    rf"\s*(?:(?:For|In|After)\s+)?(?:the\s+)?(?:"
    rf"(?P<g1>{_GENE})[\s-]perturb\w*"
    rf"|\d[\d,]*\s+(?P<g2>{_GENE})[\s-](?:perturbed\s+|targeted\s+)?cells\b"
    rf"|(?P<g3>{_GENE}):\s*\d[\d,]*\s+perturbed"
    rf"|(?:two|three|\d+)\s+(?P<g4>{_GENE})\s+(?:FDR|q|p)\b"
    rf"|(?P<cmp>Comparator\b))")

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
_WORD_COUNT = r"no|zero|none|one|two|three|four|five|six|seven|eight|nine|ten"
_UNIT = r"genes?|rows?|DEGs?|transcripts?|tests?"
_INT = r"(?:\d{1,3}(?:,\d{3})+|\d+)(?!\d|\.\d)"
_P_SIG_THRESHOLD_FIRST = re.compile(
    rf"(?i)(?<![\w.,<>=])(?P<k>{_INT}|{_WORD_COUNT})\s+(?P<q>{_PADJ}|{_PVAL})\s*"
    rf"(?P<rel><=|<)\s*(?P<thr>{NUM})\s+(?:[A-Za-z][\w-]*\s+){{0,2}}?(?P<unit>{_UNIT})\b")
# Unit before threshold: "37 genes at FDR<0.05", "6 Ap3b1 rows had FDR<1.0", "1/17443 genes",
# optionally followed by a denominator: "... at FDR<0.05 among 17442 tested".
_P_SIG = re.compile(
    rf"(?i)(?<![\w.,<>=])(?P<k>{_INT}|{_WORD_COUNT})(?:\s*(?:/|of)\s*(?P<N>{_INT}))?\s+"
    rf"(?:[A-Za-z][\w-]*\s+){{0,3}}?(?P<unit>{_UNIT})\b[^;.,]{{0,60}}?"
    rf"(?:(?P<q>{_PADJ}|{_PVAL})\s*(?P<rel><=|<)|(?P<below>below|under)\s+"
    rf"(?P<q2>{_PADJ}|{_PVAL}))\s*(?P<thr>{NUM})"
    rf"(?:\s+among\s+(?P<M>{NUM})(?:\s+(?:genes|rows|transcripts))?(?:\s+tested)?)?")
# Counts over a restricted population ("41 selected genes", "these markers") are not
# representable as a whole cell type or target, so they are out of scope.
_SUBSET = re.compile(
    r"(?i)\b(?:selected|listed|prespecified|pre-specified|candidate|chosen|curated|panel|"
    r"module|these|those|covering|direct)\b|\bnone\s+of\b"
    r"|\ball\s+(?:two|three|four|five|six|\d+)\s+had\b|\beach\s+\w+\s+had\b"
    r"|(?:self-transcript|self|target-transcript|transcript)\s+rows?\b"
    r"|(?<![\w-])target\s+rows?\b|[A-Za-z0-9]-row\b")
_ROW_WORDS = (r"Wilcoxon|DE|parquet|result|non-?target|non-?self|non-[A-Za-z][\w]*|"
              r"gene-level|gene|"
              r"gene-by-cell-type|gene-by-cell|differential-expression|[A-Za-z][\w]*-target|"
              r"[A-Za-z][\w]*-perturbation|target-comparison|[A-Za-z][\w]*-versus-Non_target")
_P_ROWS = re.compile(
    rf"(?i)(?<![\w.,<>=])(?P<N>{_INT})\s+(?:(?:{_ROW_WORDS}|[A-Z][a-z0-9]+)\s+){{0,3}}"
    rf"(?:rows|tests)\b")
_P_TESTED = re.compile(rf"(?i)(?<![\w.,<>=])(?P<N>{_INT})\s+(?:genes\s+tested|tested\s+genes)\b")
# "count=": "FDR<0.05 count=0 and FDR<0.10 count=1".
_P_COUNT_EQ = re.compile(
    rf"(?i)(?P<q>{_PADJ}|{_PVAL})\s*(?P<rel><=|<)\s*(?P<thr>{NUM})\s+count\s*(?:=|:|of)\s*"
    rf"(?P<k>{_INT})")
_P_SIG_ELIDED = re.compile(
    rf"(?i)(?<![\w.,<>=])(?P<k>{_INT}|{_WORD_COUNT})(?:\s*/\s*(?P<N>{_INT}))?\s+"
    rf"(?:had|with|at|reached|passed)\s+(?:nominal\s+)?(?P<q>{_PADJ}|{_PVAL})\s*"
    rf"(?P<rel><=|<)\s*(?P<thr>{NUM})")
_P_N_EQ = re.compile(rf"(?<![\w-])n\s*=\s*(?P<n>{_INT})(?!\s*(?:genes|rows))")
_P_RANK = re.compile(rf"(?i)\brank\s+{NUM}\s*(?:of|/)\s*(?P<N>{NUM})")
_P_MIN = re.compile(
    rf"(?i)(?<![\w-])(?<!second\s)(?<!next\s)(?:global\s+)?(?:minimum|min\.?|lowest|smallest|"
    rf"best)\s+(?:nominal\s+)?"
    rf"(?P<q>{_PADJ}|p(?:-value|\s+value)?)\s*(?:was|of|is|=|:)?\s*"
    rf"(?P<rel><=|>=|<|>|=)?\s*(?P<num>{NUM})")
_P_VALUE = re.compile(
    rf"(?<![\w-])(?P<key>(?i:log2?\s*FC|log2?\s*fold[\s-]change|logfoldchanges?|score|z|"
    rf"{_PADJ}|{_PVAL})(?:[\s-]?value)?)(?![\w-])\s*(?:(?i:was|of|is)\s*)?"
    rf"(?P<rel><=|>=|<|>|=|:)?\s*(?P<num>{NUM})")
_P_BARE = re.compile(
    r"(?<![\w.-])(?P<g>[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*)\s+(?P<num>[+-]?\d+\.\d+)"
    r"(?![\w.%]|\s*(?:cells|genes|rows|perturbed|controls))")
_P_LIST_HEAD = re.compile(
    r"(?<![\w.-])(?P<g>[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*)\s+"
    r"(?P<key>(?i:log2?\s*FC|logfoldchanges?|score))\s*(?:=|:)?\s*[+-]?\d")
_GENE_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-.][A-Za-z0-9]+)*")


def _key_quantity(key: str) -> str:
    key = re.sub(r"\s+", " ", key.lower())
    if key.startswith("log"):
        return "logfc"
    if key in ("score", "z"):
        return "score"
    if re.fullmatch(r"(?:fdr|q|pvals_adj|pval_adj|padj|p_adj|adj_p|adjusted p)(?:[ -]?value)?",
                    key):
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
        self.sentence_bounds = _sentences(masked)
        self.other_text = self._other_text(text)
        self.other_sentences = self._other_sentences()

    def _is_other(self, gene: str | None) -> bool:
        if not gene:
            return False
        return gene.lower() != self.target.lower() and gene in self.vocab.genes

    def _other_text(self, text: str) -> bool:
        """The whole text concerns another perturbation: the target is never named and some
        other gene is named as a perturbation."""
        if re.search(rf"(?i)(?<![A-Za-z0-9]){re.escape(self.target)}(?![a-z0-9])", text):
            return False
        for a, b in self.sentence_bounds:
            m = _SENTENCE_LEAD.match(self.masked, a, b)
            if m and (m.group("cmp") or self._is_other(
                    next(g for g in (m.group("g1"), m.group("g2"), m.group("g3"),
                                     m.group("g4")) if g))):
                return True
        return any(self._is_other(m.group("g")) for m in _OTHER_PERTURBATION.finditer(self.masked))

    def _other_sentences(self) -> set[tuple[int, int]]:
        """Sentences led by another perturbation, and later sentences naming that gene."""
        flagged: set[tuple[int, int]] = set()
        leads: set[str] = set()
        for a, b in self.sentence_bounds:
            m = _SENTENCE_LEAD.match(self.masked, a, b)
            gene = next((g for g in (m.group("g1"), m.group("g2"), m.group("g3"),
                                     m.group("g4")) if g), None) if m else None
            if m and (m.group("cmp") or self._is_other(gene)):
                flagged.add((a, b))
                if gene:
                    leads.add(gene)
            elif self.names_target_context(self.masked[a:b]):
                continue  # the text switches back to the target's own perturbation
            elif any(re.search(rf"(?<![A-Za-z0-9]){re.escape(g)}(?![a-z0-9])",
                               self.masked[a:b]) for g in leads):
                flagged.add((a, b))
        return flagged

    def names_target_context(self, text: str) -> bool:
        """``<Target> perturbation/perturbed/knockout/KO`` or a ``<Target>:`` heading."""
        t = re.escape(self.target)
        return bool(re.search(
            rf"(?i)(?<![A-Za-z0-9]){t}(?:[\s-]perturb\w*|\s+knockout\b|[\s-]KO\b|\s*:)", text))

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
        names_target = self.names_target_context(clause)
        if (self.other_text or sent in self.other_sentences) and not names_target:
            return "other_perturbation"
        for m in _OTHER_PERTURBATION.finditer(clause):
            if self._is_other(m.group("g")):
                return "other_perturbation"
        for pattern in (_PERTURBATION_SUBJECT, _GENE_ROWS):
            for m in pattern.finditer(clause):
                genes = re.findall(_GENE, m.group("gs") or m.groupdict().get("gs2") or "")
                if any(self._is_other(g) for g in genes):
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
        rf"(?i)(?<![\w.,-])(?P<n>{NUM})\s+(?:{target}[-\s])?(?:matched\s+)?"
        rf"(?:(?:perturbed|targeted)(?:\s+(?:cells|nuclei))?|cells|nuclei)\s+"
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
    cells = re.compile(rf"(?i)(?<![\w.,-])(?P<n>{NUM})\s+(?:{target}[-\s])?"
                       rf"(?:(?:perturbed|targeted)[-\s])?(?:cells|nuclei)\b")
    for m in take(cells):
        if _COUNT_BOUND.search(ctx.masked[:m.start()]):
            out.append(_assertion(ctx, sent, m.start(), "other", "=", m.group("n"),
                                  status="out_of_scope", reason="bound"))
            continue
        out.append(_assertion(ctx, sent, m.start(), "n_pert", "=", m.group("n")))
    for m in take(_P_N_EQ):
        out.append(_assertion(ctx, sent, m.start(), "n_pert", "=", m.group("n")))
    for m in take(_P_SIG_THRESHOLD_FIRST):
        out.append(_count(ctx, sent, m, _count_value(m.group("k")),
                          _lead_in(ctx, sent, work, m)))
    for m in take(_P_SIG):
        if not m.group("k")[0].isdigit() and len(
                ctx.masked[m.end("k"):m.start("unit")].split()) > 1:
            continue
        if re.search(r"(?i)\brecurr", ctx.masked[m.end("unit"):m.end()]):
            out.append(_assertion(ctx, sent, m.start(), "other", "=", m.group("k"),
                                  status="out_of_scope", reason="recurrence"))
            continue
        lead = _lead_in(ctx, sent, work, m)
        out.append(_count(ctx, sent, m, _count_value(m.group("k")), lead))
        total = m.group("N") or m.group("M")
        if total:
            status, reason = _subset_status(lead)
            out.append(_assertion(ctx, sent, m.start(), "n_rows", "=", total, needs_cell=False,
                                  unit=_unit(m.group("unit")),
                                  self_inclusion=_self_inclusion(lead, ctx.target),
                                  status=status, reason=reason))
    for m in take(_P_SIG_ELIDED):
        # "... and 16 had FDR<=0.5": the unit is the earlier count's in the same sentence.
        earlier = sorted((a for a in out if a.quantity == "n_sig"
                          and sent[0] <= a.start < m.start()), key=lambda a: a.start)
        if not earlier:
            continue
        lead = _lead_in(ctx, sent, work, m)
        count = _count(ctx, sent, m, _count_value(m.group("k")), lead, unit=earlier[-1].unit)
        if earlier[-1].status == "out_of_scope":
            # The elided count concerns the same population as its antecedent: "Across 41
            # selected genes, 9 genes had P<0.001 and 16 had P<0.01" restricts both.
            count = replace(count, status="out_of_scope", reason=earlier[-1].reason)
        out.append(count)
        if m.group("N"):
            status, reason = _subset_status(lead)
            if earlier[-1].status == "out_of_scope":
                status, reason = "out_of_scope", earlier[-1].reason
            out.append(_assertion(ctx, sent, m.start(), "n_rows", "=", m.group("N"),
                                  needs_cell=False, unit=earlier[-1].unit,
                                  self_inclusion=_self_inclusion(lead, ctx.target),
                                  status=status, reason=reason))
    for m in take(_P_COUNT_EQ):
        out.append(_count(ctx, sent, m, m.group("k"), _lead_in(ctx, sent, work, m),
                          unit="rows"))
    for m in take(_P_TESTED):
        lead = _lead_in(ctx, sent, work, m)
        status, reason = _subset_status(lead)
        out.append(_assertion(ctx, sent, m.start(), "n_rows", "=", m.group("N"),
                              needs_cell=False, unit="genes",
                              self_inclusion=_self_inclusion(lead, ctx.target),
                              status=status, reason=reason))
    for m in take(_P_RANK):
        paren = ctx.masked[ctx.masked.rfind("(", sent[0], m.start()) + 1:m.start()]
        if "(" in ctx.masked[sent[0]:m.start()] and ")" not in paren and re.search(
                r"(?i)\br\s*=|correlation|\brho\b", paren):
            out.append(_assertion(ctx, sent, m.start(), "other", "=", m.group("N"),
                                  status="out_of_scope", reason="correlation"))
            continue
        out.append(_assertion(ctx, sent, m.start(), "n_rows", "=", m.group("N"), unit="genes"))
    for m in take(_P_ROWS):
        lead = _lead_in(ctx, sent, work, m)
        status, reason = _subset_status(lead)
        # "88 rows covering Mcf2l, Rhoa, ..." (named genes) and "in all 19 rows" are not
        # whole-scope totals; "rows covering 22 cell types" is.
        if (re.match(r"\s+covering\s+(?!\d)", ctx.masked[m.end():])
                or re.search(r"(?i)\ball\s+$", ctx.masked[sent[0]:m.start()])):
            status, reason = "out_of_scope", "subset_scope"
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
        if re.search(r"(?i)\ball\s+(?:\w+\s+)?(?:had\s+)?$", ctx.masked[sent[0]:m.start()]):
            out.append(_assertion(ctx, sent, m.start(), _key_quantity(m.group("key")), relation,
                                  m.group("num"), status="out_of_scope", reason="distributive"))
            continue
        # Equalities bind to the nearest preceding gene; inequalities only to an adjacent one,
        # so aggregate thresholds ("overall FDR<0.05") never become gene assertions.
        if relation in ("=", ":"):
            gene = ctx.gene(sent, m.start())
        else:
            gene = ctx.adjacent_gene(m.start())
        out.append(_assertion(ctx, sent, m.start(), _key_quantity(m.group("key")),
                              relation, m.group("num"), gene=gene, needs_gene=True,
                              scope="gene", inherit=True))
    # A list "Adgrb1 logFC -0.513 FDR ...; Dync1i2 -0.467 FDR ..." writes the first item's
    # leading statistic once; later bare values after a gene take that statistic.
    first = next((m for m in _P_LIST_HEAD.finditer(ctx.masked, *sent)
                  if m.group("g") in ctx.vocab.genes), None)
    lead_q = _key_quantity(first.group("key")) if first else None
    if first is not None and lead_q in ("logfc", "score"):
        for m in take(_P_BARE):
            after = ctx.masked[m.end():m.end() + 12]
            if (m.group("g") not in ctx.vocab.genes or m.start() < first.end()
                    or (re.match(r"\s*(?i:log2?\s*FC|logfoldchange)", after)
                        and lead_q == "logfc")
                    or (re.match(r"\s*(?i:score|z\b)", after) and lead_q == "score")):
                continue
            out.append(_assertion(ctx, sent, m.start("num"), lead_q, "=", m.group("num"),
                                  gene=m.group("g"), needs_gene=True, scope="gene",
                                  inherit=True))
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
    return "rows" if unit.lower().rstrip("s") in ("row", "test") else "genes"


_ZERO_WORDS = {"no", "zero", "none"}
_COUNT_BOUND = re.compile(
    r"(?i)(?:\bover|\bmore\s+than|\bfewer\s+than|\bless\s+than|\bat\s+least|\bup\s+to)\s*$")


def _count_value(k: str) -> str:
    """Counts as written; "no", "zero" and "none" are written as 0 (codebook)."""
    return "0" if k.lower() in _ZERO_WORDS else k


def _count(ctx: _Context, sent: tuple[int, int], m: re.Match[str], k: str,
           lead: str, unit: str | None = None) -> Assertion:
    status, reason = _subset_status(lead)
    groups = m.groupdict()
    below = groups.get("below")
    q = groups.get("q") or groups.get("q2") or ""
    return _assertion(ctx, sent, m.start(), "n_sig", "=", k, needs_cell=False,
                      threshold_quantity=_threshold_quantity(q),
                      threshold_relation="<" if below else m.group("rel"),
                      threshold_text=m.group("thr"),
                      unit=unit or _unit(m.group("unit")),
                      self_inclusion=_self_inclusion(lead, ctx.target),
                      status=status, reason=reason)
