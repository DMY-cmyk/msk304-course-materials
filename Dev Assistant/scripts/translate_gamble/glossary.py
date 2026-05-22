"""Protected strategic-management terms — masked before translation, restored after."""
from __future__ import annotations
import re

GLOSSARY_VERSION = "1.0.0"

# Order does not matter — we sort by length descending in _compile()
PROTECTED_TERMS: tuple[str, ...] = (
    # Core jargon (kept English, italic in output)
    "strategy", "business model", "competitive advantage", "value proposition",
    "profit formula", "customer value proposition", "value chain",
    "core competencies", "core competence", "distinctive competence",
    "first-mover advantage", "first mover advantage", "late-mover advantage",
    "blue ocean", "red ocean", "value innovation",
    "broad differentiation", "focused differentiation", "focused low-cost",
    "best-cost provider", "low-cost provider", "generic strategy",
    "balanced scorecard", "strategic vision", "mission statement",
    "strategic objective", "financial objective", "strategic intent",
    "strategic group map", "driving forces", "key success factors",
    "five forces", "five-forces model", "Porter's Five Forces",
    "rivalry", "bargaining power", "threat of substitutes", "threat of entry",
    "barriers to entry", "switching costs", "economies of scale",
    "learning curve", "experience curve", "network effects",
    "SWOT", "PESTEL", "VRIN", "VRIO", "KSF",
    "resource-based view", "dynamic capabilities", "isolating mechanism",
    "competitive asset", "competitive liability", "competitively important resource",
    "value-creating activity", "primary activity", "support activity",
    "benchmark", "benchmarking", "best practice",
    "strategic group", "market segment", "buyer power", "supplier power",
    "complementor", "industry life cycle", "fragmented industry",
    "concentrated industry", "consolidation", "vertical integration",
    "horizontal integration", "diversification", "related diversification",
    "unrelated diversification", "outsourcing", "offshoring",
    "stakeholder", "shareholder value", "corporate governance",
    "strategy formulation", "strategy execution", "strategic plan",
    "strategic leadership", "strategic management process",
)


def _compile() -> re.Pattern[str]:
    # Longest-first prevents "competitive" from eating "competitive advantage"
    terms_sorted = sorted(set(PROTECTED_TERMS), key=len, reverse=True)
    # Escape and join. \b ensures whole-word matching so "strategist" != "strategy".
    escaped = [re.escape(t) for t in terms_sorted]
    return re.compile(r"\b(" + "|".join(escaped) + r")\b", re.IGNORECASE)


_PATTERN = _compile()
_SENTINEL_RE = re.compile(r"§T(\d{3,})§")


def mask(text: str) -> tuple[str, dict[str, str]]:
    """Replace each protected term with a sentinel.

    Returns (masked_text, mapping) where mapping[sentinel] = original_term
    with original capitalization preserved.
    """
    mapping: dict[str, str] = {}
    counter = [0]

    def _replace(match: re.Match[str]) -> str:
        original = match.group(0)
        sentinel = f"§T{counter[0]:03d}§"
        mapping[sentinel] = original
        counter[0] += 1
        return sentinel

    masked = _PATTERN.sub(_replace, text)
    return masked, mapping


def unmask(translated: str, mapping: dict[str, str]) -> tuple[str, list[tuple[int, int]]]:
    """Restore originals into translated text. Returns (text, italic_spans).

    italic_spans is a list of (start, end) char offsets in the final text
    where each restored term begins/ends. Surviving sentinels (the translator
    dropped one) are simply removed without adding a span.
    """
    out_parts: list[str] = []
    spans: list[tuple[int, int]] = []
    cursor = 0
    pos = 0  # running offset in the final string

    for match in _SENTINEL_RE.finditer(translated):
        out_parts.append(translated[cursor:match.start()])
        pos += match.start() - cursor
        sentinel = match.group(0)
        if sentinel in mapping:
            term = mapping[sentinel]
            spans.append((pos, pos + len(term)))
            out_parts.append(term)
            pos += len(term)
        # else: drop the sentinel silently
        cursor = match.end()

    out_parts.append(translated[cursor:])
    return "".join(out_parts), spans
