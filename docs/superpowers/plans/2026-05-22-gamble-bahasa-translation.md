# Gamble Bahasa Indonesia Translation — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce `Temu 1-7 Buku Gamble (Bahasa Indonesia).docx` — a 150-page Indonesian study aid translated from the original PDF, with strategic-management jargon left in English italic and figures embedded inline.

**Architecture:** Three isolated Python stages (extract → translate → render) under `Dev Assistant/scripts/translate_gamble/`. A glossary module handles mask/unmask of protected terms so Google Translate never touches them. SQLite caches per-block translations for cheap re-runs. A thin `run.py` CLI orchestrates the three stages.

**Tech Stack:** Python 3.12, PyMuPDF (PDF extraction), deep-translator (Google Translate wrapper), python-docx (DOCX rendering), SQLite (cache), pytest (tests).

**Spec:** `docs/superpowers/specs/2026-05-22-gamble-bahasa-translation-design.md`

---

## Task 1: Project scaffolding, dependencies, and .gitignore

**Files:**
- Create: `Dev Assistant/scripts/translate_gamble/__init__.py`
- Create: `Dev Assistant/scripts/translate_gamble/tests/__init__.py`
- Create: `Dev Assistant/scripts/translate_gamble/requirements.txt`
- Create: `.gitignore`

- [ ] **Step 1: Verify Python and existing libraries**

Run: `python --version && python -m pip show PyMuPDF python-docx`
Expected: Python 3.12.x; PyMuPDF 1.27.1; python-docx 1.2.0. If missing, install: `python -m pip install PyMuPDF python-docx`.

- [ ] **Step 2: Install deep-translator and pytest**

Run: `python -m pip install "deep-translator>=1.11" "pytest>=8"`
Expected: successful install with no errors.

- [ ] **Step 3: Create package directories and empty init files**

Create `Dev Assistant/scripts/translate_gamble/__init__.py` with a single line:
```python
"""Bahasa Indonesia translation pipeline for Gamble Strategic Management ch. 1-7."""
```

Create `Dev Assistant/scripts/translate_gamble/tests/__init__.py` as an empty file.

- [ ] **Step 4: Write requirements.txt**

Create `Dev Assistant/scripts/translate_gamble/requirements.txt`:
```
PyMuPDF>=1.27.1
python-docx>=1.2.0
deep-translator>=1.11
pytest>=8
```

- [ ] **Step 5: Write .gitignore**

Create `.gitignore` at the repo root:
```
# Python
__pycache__/
*.pyc
.pytest_cache/

# Translate-gamble pipeline build artifacts
Dev Assistant/scripts/translate_gamble/build/

# Word lock files
~$*.docx
~$*.doc

# OS
Thumbs.db
.DS_Store
```

- [ ] **Step 6: Commit**

```bash
git add ".gitignore" "Dev Assistant/scripts/translate_gamble/__init__.py" "Dev Assistant/scripts/translate_gamble/tests/__init__.py" "Dev Assistant/scripts/translate_gamble/requirements.txt"
git commit -m "chore(translate_gamble): scaffold package + deps + gitignore"
```

---

## Task 2: Glossary — protected-term data + mask round-trip test

**Files:**
- Create: `Dev Assistant/scripts/translate_gamble/glossary.py`
- Create: `Dev Assistant/scripts/translate_gamble/tests/test_glossary.py`

- [ ] **Step 1: Write failing test for `mask` and `unmask` round-trip**

Create `Dev Assistant/scripts/translate_gamble/tests/test_glossary.py`:
```python
from translate_gamble.glossary import mask, unmask, GLOSSARY_VERSION


def test_glossary_version_is_string():
    assert isinstance(GLOSSARY_VERSION, str)
    assert len(GLOSSARY_VERSION) > 0


def test_mask_replaces_known_term_with_sentinel():
    masked, mapping = mask("A firm needs a competitive advantage.")
    assert "competitive advantage" not in masked.lower()
    assert "§T" in masked
    assert len(mapping) == 1


def test_mask_handles_longest_match_first():
    # "competitive advantage" must be masked as one unit, not "competitive" first
    masked, mapping = mask("competitive advantage is core")
    assert len(mapping) == 1
    only_value = next(iter(mapping.values()))
    assert only_value.lower() == "competitive advantage"


def test_mask_is_case_insensitive_but_preserves_original():
    masked, mapping = mask("Competitive Advantage matters.")
    assert len(mapping) == 1
    assert next(iter(mapping.values())) == "Competitive Advantage"


def test_unmask_restores_terms_and_reports_italic_spans():
    masked, mapping = mask("Use SWOT and value chain analysis.")
    # Simulate translator output: same sentinels, Indonesian words around
    translated = masked.replace("Use", "Gunakan").replace("and", "dan").replace("analysis", "analisis")
    text, spans = unmask(translated, mapping)
    assert "SWOT" in text
    assert "value chain" in text
    assert "§T" not in text
    # Two italic spans, one per term, both within text bounds
    assert len(spans) == 2
    for start, end in spans:
        assert 0 <= start < end <= len(text)


def test_unmask_handles_unused_sentinels_gracefully():
    # If translator drops a sentinel, unmask must not crash
    masked, mapping = mask("strategy and SWOT")
    text, spans = unmask("strategi dan", mapping)
    assert "§T" not in text
    # At most one span (the surviving one); zero is also acceptable
    assert len(spans) <= 1


def test_mask_does_not_break_word_boundaries():
    # "strategist" must NOT match "strategy"
    masked, mapping = mask("The strategist studies strategy.")
    assert "strategist" in masked
    assert len(mapping) == 1
    assert next(iter(mapping.values())).lower() == "strategy"
```

- [ ] **Step 2: Run the tests to confirm they fail**

Run (from the repo root): `python -m pytest "Dev Assistant/scripts/translate_gamble/tests/test_glossary.py" -v`
Expected: `ModuleNotFoundError: No module named 'translate_gamble'` OR collection error. Either is acceptable — confirms tests run but module is missing.

- [ ] **Step 3: Make `translate_gamble` importable from pytest**

Create `Dev Assistant/scripts/translate_gamble/conftest.py`:
```python
import sys
from pathlib import Path

# Make the parent dir importable so `from translate_gamble import ...` works
_PARENT = Path(__file__).resolve().parent.parent
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))
```

- [ ] **Step 4: Implement `glossary.py`**

Create `Dev Assistant/scripts/translate_gamble/glossary.py`:
```python
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
```

- [ ] **Step 5: Run the tests to confirm they pass**

Run: `python -m pytest "Dev Assistant/scripts/translate_gamble/tests/test_glossary.py" -v`
Expected: 7 passed.

- [ ] **Step 6: Commit**

```bash
git add "Dev Assistant/scripts/translate_gamble/glossary.py" "Dev Assistant/scripts/translate_gamble/conftest.py" "Dev Assistant/scripts/translate_gamble/tests/test_glossary.py"
git commit -m "feat(translate_gamble): glossary mask/unmask with longest-match-first"
```

---

## Task 3: Extract stage — PDF → structured JSON + images

**Files:**
- Create: `Dev Assistant/scripts/translate_gamble/extract.py`
- Create: `Dev Assistant/scripts/translate_gamble/tests/test_extract.py`

- [ ] **Step 1: Write failing test for classify_block heuristic**

Create `Dev Assistant/scripts/translate_gamble/tests/test_extract.py`:
```python
from translate_gamble.extract import classify_block, detect_chapter_start


def test_classify_block_large_font_is_heading_1():
    assert classify_block(text="STRATEGY", font_size=18.0, is_bold=True) == ("heading", 1)


def test_classify_block_medium_bold_is_heading_2():
    assert classify_block(text="Crafting the Strategy", font_size=14.0, is_bold=True) == ("heading", 2)


def test_classify_block_small_bold_caps_is_heading_3():
    assert classify_block(text="LEARNING OBJECTIVES", font_size=11.5, is_bold=True) == ("heading", 3)


def test_classify_block_bullet_is_list_item():
    assert classify_block(text="• rivalry among competitors", font_size=11.0, is_bold=False) == ("list_item", 0)


def test_classify_block_default_is_body():
    assert classify_block(text="A company's strategy is its game plan.", font_size=11.0, is_bold=False) == ("body", 0)


def test_classify_block_figure_caption():
    assert classify_block(text="FIGURE 1.2 The Five-Forces Model", font_size=10.0, is_bold=True) == ("caption", 0)


def test_detect_chapter_start_matches_chapter_header():
    assert detect_chapter_start("CHAPTER 1") == 1
    assert detect_chapter_start("3 EVALUATING A COMPANY'S EXTERNAL ENVIRONMENT") == 3
    assert detect_chapter_start("A company's strategy is its game plan.") is None
```

- [ ] **Step 2: Run the tests to confirm they fail**

Run: `python -m pytest "Dev Assistant/scripts/translate_gamble/tests/test_extract.py" -v`
Expected: `ModuleNotFoundError` or `ImportError` on `extract`.

- [ ] **Step 3: Implement `extract.py`**

Create `Dev Assistant/scripts/translate_gamble/extract.py`:
```python
"""Stage 1: PDF -> per-page structured JSON + extracted figure PNGs."""
from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF

_CHAPTER_HEADER_RE = re.compile(r"^(?:CHAPTER\s+)?(\d{1,2})(?:\s+[A-Z][A-Z'\s,]{4,})?$")
_CAPTION_RE = re.compile(r"^(FIGURE|TABLE|EXHIBIT|CONCEPTS\s*&\s*CONNECTIONS)\s")
_BULLET_RE = re.compile(r"^\s*[•▪–■◦]\s")

_MIN_IMG_WIDTH = 100
_MIN_IMG_AREA = 10_000


def classify_block(text: str, font_size: float, is_bold: bool) -> tuple[str, int]:
    """Return (block_type, heading_level). heading_level is 0 for non-headings."""
    text_stripped = text.strip()
    if not text_stripped:
        return ("body", 0)
    if _BULLET_RE.match(text_stripped):
        return ("list_item", 0)
    if _CAPTION_RE.match(text_stripped):
        return ("caption", 0)
    if font_size >= 16.0:
        return ("heading", 1)
    if font_size >= 13.0 and is_bold:
        return ("heading", 2)
    if (
        font_size >= 11.0
        and is_bold
        and text_stripped == text_stripped.upper()
        and len(text_stripped) >= 4
    ):
        return ("heading", 3)
    return ("body", 0)


def detect_chapter_start(first_line: str) -> int | None:
    """Return chapter number if line looks like a chapter header, else None."""
    stripped = first_line.strip()
    match = _CHAPTER_HEADER_RE.match(stripped)
    if match:
        return int(match.group(1))
    return None


def _block_text_and_style(block: dict[str, Any]) -> tuple[str, float, bool]:
    """Flatten a PyMuPDF block dict into (text, dominant_font_size, any_bold)."""
    if block.get("type", 0) != 0:  # not a text block
        return ("", 0.0, False)
    lines = []
    sizes: list[float] = []
    bold_any = False
    for line in block.get("lines", []):
        spans = line.get("spans", [])
        for span in spans:
            txt = span.get("text", "")
            if txt:
                lines.append(txt)
                sizes.append(float(span.get("size", 11.0)))
                # PyMuPDF flag bit 4 = bold
                if int(span.get("flags", 0)) & 16:
                    bold_any = True
        lines.append(" ")
    text = "".join(lines).strip()
    dominant_size = max(sizes) if sizes else 11.0
    return text, dominant_size, bold_any


def _extract_images(page: fitz.Page, doc: fitz.Document, page_num: int, img_dir: Path) -> list[dict[str, Any]]:
    """Save eligible images and return list of image block records."""
    records: list[dict[str, Any]] = []
    for img_index, img_info in enumerate(page.get_images(full=True)):
        xref = img_info[0]
        try:
            pix = fitz.Pixmap(doc, xref)
        except Exception:
            continue
        if pix.width < _MIN_IMG_WIDTH or (pix.width * pix.height) < _MIN_IMG_AREA:
            pix = None
            continue
        if pix.n - pix.alpha >= 4:  # CMYK -> RGB
            pix = fitz.Pixmap(fitz.csRGB, pix)
        fname = f"page_{page_num:03d}_img{img_index}.png"
        out_path = img_dir / fname
        pix.save(str(out_path))
        records.append({"type": "image", "ref": fname})
        pix = None
    return records


def extract_pdf(pdf_path: Path, out_dir: Path) -> None:
    """Walk every page of the PDF and write per-page JSON + image PNGs."""
    pages_dir = out_dir / "pages"
    img_dir = out_dir / "images"
    pages_dir.mkdir(parents=True, exist_ok=True)
    img_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    current_chapter = 1
    try:
        for i, page in enumerate(doc, start=1):
            raw = page.get_text("dict")
            blocks_out: list[dict[str, Any]] = []

            # Chapter detection: look at first non-empty text block
            first_text = ""
            for blk in raw.get("blocks", []):
                t, _, _ = _block_text_and_style(blk)
                if t:
                    first_text = t.splitlines()[0] if "\n" in t else t
                    break
            ch = detect_chapter_start(first_text)
            if ch is not None:
                current_chapter = ch

            for blk in raw.get("blocks", []):
                text, size, bold = _block_text_and_style(blk)
                if not text:
                    continue
                btype, level = classify_block(text, size, bold)
                rec: dict[str, Any] = {"type": btype, "text": text}
                if btype == "heading":
                    rec["level"] = level
                blocks_out.append(rec)

            # Append images for this page after text blocks
            blocks_out.extend(_extract_images(page, doc, i, img_dir))

            payload = {
                "page": i,
                "chapter": current_chapter,
                "blocks": blocks_out,
            }
            (pages_dir / f"page_{i:03d}.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
    finally:
        doc.close()


if __name__ == "__main__":
    import sys
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("Temu 1-7 Buku Gamble.pdf")
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("Dev Assistant/scripts/translate_gamble/build/extracted")
    extract_pdf(pdf, out)
    print(f"Extracted to {out}")
```

- [ ] **Step 4: Run the tests to confirm they pass**

Run: `python -m pytest "Dev Assistant/scripts/translate_gamble/tests/test_extract.py" -v`
Expected: 7 passed.

- [ ] **Step 5: Smoke-run extract on the real PDF**

Run from the repo root:
```
python "Dev Assistant/scripts/translate_gamble/extract.py" "Temu 1-7 Buku Gamble.pdf" "Dev Assistant/scripts/translate_gamble/build/extracted"
```
Expected: prints `Extracted to ...`. Verify:
```
ls "Dev Assistant/scripts/translate_gamble/build/extracted/pages" | wc -l
```
Expected: 150 JSON files. Also spot-check one: open `page_001.json` — should contain `chapter: 1`, several blocks including at least one `heading` and several `body` blocks. Image dir should have at least a handful of PNGs (Chapter 1 has figures).

- [ ] **Step 6: Commit**

```bash
git add "Dev Assistant/scripts/translate_gamble/extract.py" "Dev Assistant/scripts/translate_gamble/tests/test_extract.py"
git commit -m "feat(translate_gamble): extract stage — PDF to per-page JSON + images"
```

---

## Task 4: Translate stage — cached, masked, rate-limited

**Files:**
- Create: `Dev Assistant/scripts/translate_gamble/translate.py`
- Create: `Dev Assistant/scripts/translate_gamble/tests/test_translate.py`

- [ ] **Step 1: Write failing test for the cache + the chunk_text helper**

Create `Dev Assistant/scripts/translate_gamble/tests/test_translate.py`:
```python
from pathlib import Path
from translate_gamble.translate import TranslationCache, chunk_text, translate_block


def test_chunk_text_short_returns_single_chunk():
    assert chunk_text("Hello world.") == ["Hello world."]


def test_chunk_text_splits_at_sentence_boundaries():
    long_sentence = "This is one. " * 500  # ~6500 chars
    chunks = chunk_text(long_sentence, max_len=4500)
    assert len(chunks) >= 2
    assert all(len(c) <= 4500 for c in chunks)
    assert "".join(chunks).replace(" ", "") == long_sentence.replace(" ", "")


def test_translation_cache_stores_and_retrieves(tmp_path: Path):
    cache = TranslationCache(tmp_path / "c.sqlite", glossary_version="1.0.0")
    assert cache.get("hello") is None
    cache.put("hello", "halo", [(0, 4)])
    got = cache.get("hello")
    assert got is not None
    text, spans = got
    assert text == "halo"
    assert spans == [(0, 4)]


def test_translation_cache_invalidates_on_version_change(tmp_path: Path):
    db = tmp_path / "c.sqlite"
    c1 = TranslationCache(db, glossary_version="1.0.0")
    c1.put("hello", "halo", [])
    c2 = TranslationCache(db, glossary_version="2.0.0")
    assert c2.get("hello") is None


class FakeTranslator:
    def __init__(self, mapping: dict[str, str]) -> None:
        self.mapping = mapping
        self.calls = 0

    def translate(self, text: str) -> str:
        self.calls += 1
        return self.mapping.get(text, text)


def test_translate_block_masks_and_unmasks_using_glossary(tmp_path: Path):
    cache = TranslationCache(tmp_path / "c.sqlite", glossary_version="1.0.0")
    fake = FakeTranslator({})  # passthrough
    # Source contains a glossary term. Fake translator returns input unchanged,
    # so after unmask we should get the term back with one italic span.
    out_text, spans = translate_block(
        "A firm needs a strategy.", cache=cache, translator=fake
    )
    assert "strategy" in out_text
    assert len(spans) == 1


def test_translate_block_hits_cache_on_second_call(tmp_path: Path):
    cache = TranslationCache(tmp_path / "c.sqlite", glossary_version="1.0.0")
    fake = FakeTranslator({})
    translate_block("hello", cache=cache, translator=fake)
    translate_block("hello", cache=cache, translator=fake)
    assert fake.calls == 1  # second call served from cache
```

- [ ] **Step 2: Run the tests to confirm they fail**

Run: `python -m pytest "Dev Assistant/scripts/translate_gamble/tests/test_translate.py" -v`
Expected: `ModuleNotFoundError` or `ImportError` on `translate`.

- [ ] **Step 3: Implement `translate.py`**

Create `Dev Assistant/scripts/translate_gamble/translate.py`:
```python
"""Stage 2: extracted JSON -> translated JSON with italic spans."""
from __future__ import annotations
import hashlib
import json
import re
import sqlite3
import time
from pathlib import Path
from typing import Any, Protocol

from translate_gamble.glossary import GLOSSARY_VERSION, mask, unmask

_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+")


class Translator(Protocol):
    def translate(self, text: str) -> str: ...


def chunk_text(text: str, max_len: int = 4500) -> list[str]:
    """Split text at sentence boundaries so no chunk exceeds max_len chars."""
    if len(text) <= max_len:
        return [text]
    sentences = _SENTENCE_END_RE.split(text)
    chunks: list[str] = []
    buf = ""
    for s in sentences:
        sep = " " if buf else ""
        if len(buf) + len(sep) + len(s) <= max_len:
            buf = buf + sep + s
        else:
            if buf:
                chunks.append(buf)
            # Hard-cut sentences that are themselves too long
            while len(s) > max_len:
                chunks.append(s[:max_len])
                s = s[max_len:]
            buf = s
    if buf:
        chunks.append(buf)
    return chunks


class TranslationCache:
    """SQLite cache keyed by sha256(text + glossary_version)."""

    def __init__(self, db_path: Path, glossary_version: str) -> None:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.glossary_version = glossary_version
        self.conn = sqlite3.connect(str(db_path))
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS translations(
                   key TEXT PRIMARY KEY,
                   text TEXT NOT NULL,
                   spans TEXT NOT NULL
               )"""
        )
        self.conn.commit()

    def _key(self, source_text: str) -> str:
        h = hashlib.sha256()
        h.update(self.glossary_version.encode("utf-8"))
        h.update(b"\x00")
        h.update(source_text.encode("utf-8"))
        return h.hexdigest()

    def get(self, source_text: str) -> tuple[str, list[tuple[int, int]]] | None:
        row = self.conn.execute(
            "SELECT text, spans FROM translations WHERE key=?",
            (self._key(source_text),),
        ).fetchone()
        if row is None:
            return None
        spans = [tuple(p) for p in json.loads(row[1])]
        return row[0], spans

    def put(self, source_text: str, translated_text: str, spans: list[tuple[int, int]]) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO translations(key, text, spans) VALUES(?,?,?)",
            (self._key(source_text), translated_text, json.dumps(spans)),
        )
        self.conn.commit()


def translate_block(
    text: str,
    *,
    cache: TranslationCache,
    translator: Translator,
    sleep_seconds: float = 0.0,
) -> tuple[str, list[tuple[int, int]]]:
    """Translate one block of text. Cached. Masks glossary terms first."""
    cached = cache.get(text)
    if cached is not None:
        return cached

    parts: list[str] = []
    span_accum: list[tuple[int, int]] = []
    offset = 0
    for chunk in chunk_text(text):
        masked, mapping = mask(chunk)
        translated = translator.translate(masked)
        if sleep_seconds:
            time.sleep(sleep_seconds)
        restored, spans = unmask(translated, mapping)
        for s, e in spans:
            span_accum.append((s + offset, e + offset))
        parts.append(restored)
        offset += len(restored) + 1  # +1 for the joining space below
    out_text = " ".join(parts)
    cache.put(text, out_text, span_accum)
    return out_text, span_accum


def _make_google_translator():
    """Return a configured deep_translator.GoogleTranslator instance."""
    from deep_translator import GoogleTranslator
    return GoogleTranslator(source="en", target="id")


def translate_pages(extracted_dir: Path, out_dir: Path, cache_dir: Path) -> None:
    """Translate every page_*.json in extracted_dir into out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    cache = TranslationCache(cache_dir / "translations.sqlite", GLOSSARY_VERSION)
    translator = _make_google_translator()

    page_files = sorted((extracted_dir / "pages").glob("page_*.json"))
    total = len(page_files)
    for idx, src in enumerate(page_files, start=1):
        payload = json.loads(src.read_text(encoding="utf-8"))
        for block in payload["blocks"]:
            if block["type"] == "image":
                continue
            original = block["text"]
            translated, spans = translate_block(
                original,
                cache=cache,
                translator=translator,
                sleep_seconds=0.2,  # ~5 RPS ceiling
            )
            block["text"] = translated
            block["italic_spans"] = spans
        (out_dir / src.name).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"[{idx}/{total}] {src.name}")


if __name__ == "__main__":
    import sys
    base = Path("Dev Assistant/scripts/translate_gamble/build")
    extracted = Path(sys.argv[1]) if len(sys.argv) > 1 else base / "extracted"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else base / "translated"
    cache = base / "cache"
    translate_pages(extracted, out, cache)
    print(f"Translated to {out}")
```

- [ ] **Step 4: Run the tests to confirm they pass**

Run: `python -m pytest "Dev Assistant/scripts/translate_gamble/tests/test_translate.py" -v`
Expected: 6 passed.

- [ ] **Step 5: Pre-flight — translate 3 pages against the real Google endpoint**

Pre-flight script (run interactively, do not commit):
```bash
python -c "
import json
from pathlib import Path
from translate_gamble.translate import translate_pages
import sys
sys.path.insert(0, 'Dev Assistant/scripts/translate_gamble')

# Copy 3 pages to a temp extracted dir to limit scope
base = Path('Dev Assistant/scripts/translate_gamble/build')
src = base / 'extracted' / 'pages'
tmp_ext = base / 'preflight' / 'extracted' / 'pages'
tmp_ext.mkdir(parents=True, exist_ok=True)
# Reuse images
import shutil
img_src = base / 'extracted' / 'images'
img_dst = base / 'preflight' / 'extracted' / 'images'
if not img_dst.exists():
    shutil.copytree(img_src, img_dst)
for name in ['page_001.json', 'page_005.json', 'page_010.json']:
    shutil.copy(src / name, tmp_ext / name)

translate_pages(
    base / 'preflight' / 'extracted',
    base / 'preflight' / 'translated',
    base / 'preflight' / 'cache',
)
out = json.loads((base / 'preflight' / 'translated' / 'page_001.json').read_text(encoding='utf-8'))
for b in out['blocks'][:5]:
    print(b)
"
```
Expected: 3 page files emerge in `preflight/translated/`. Spot-check: page_001 should contain Indonesian text mixed with the original *strategy*, *business model*, *competitive advantage* visible verbatim. No `§T###§` sentinels in output. If sentinels survive, **STOP** and change `§T###§` in `glossary.py` to a different sentinel format (e.g. `XQ###QX`) before continuing.

- [ ] **Step 6: Commit**

```bash
git add "Dev Assistant/scripts/translate_gamble/translate.py" "Dev Assistant/scripts/translate_gamble/tests/test_translate.py"
git commit -m "feat(translate_gamble): translate stage — cached, masked, chunked"
```

---

## Task 5: Render stage — translated JSON → DOCX

**Files:**
- Create: `Dev Assistant/scripts/translate_gamble/render.py`
- Create: `Dev Assistant/scripts/translate_gamble/tests/test_render.py`

- [ ] **Step 1: Write failing test for paragraph italic-run splitting**

Create `Dev Assistant/scripts/translate_gamble/tests/test_render.py`:
```python
from pathlib import Path
from translate_gamble.render import italic_runs, render_to_docx


def test_italic_runs_no_spans_returns_single_plain_run():
    assert italic_runs("hello world", []) == [("hello world", False)]


def test_italic_runs_single_span_splits_into_three():
    runs = italic_runs("A is strategy here.", [(5, 13)])
    assert runs == [("A is ", False), ("strategy", True), (" here.", False)]


def test_italic_runs_two_spans():
    runs = italic_runs("Use SWOT and value chain.", [(4, 8), (13, 24)])
    assert runs == [
        ("Use ", False),
        ("SWOT", True),
        (" and ", False),
        ("value chain", True),
        (".", False),
    ]


def test_italic_runs_span_at_start():
    runs = italic_runs("strategy matters.", [(0, 8)])
    assert runs == [("strategy", True), (" matters.", False)]


def test_render_to_docx_smoke(tmp_path: Path):
    pages_dir = tmp_path / "translated"
    images_dir = tmp_path / "extracted" / "images"
    pages_dir.mkdir(parents=True)
    images_dir.mkdir(parents=True)
    # Minimal one-page payload
    import json
    (pages_dir / "page_001.json").write_text(json.dumps({
        "page": 1, "chapter": 1,
        "blocks": [
            {"type": "heading", "level": 1, "text": "BAB 1", "italic_spans": []},
            {"type": "body", "text": "Sebuah strategi adalah rencana.", "italic_spans": [(7, 15)]},
        ],
    }), encoding="utf-8")
    out = tmp_path / "out.docx"
    render_to_docx(pages_dir, images_dir, out)
    assert out.exists()
    # Verify with python-docx
    from docx import Document
    doc = Document(str(out))
    texts = [p.text for p in doc.paragraphs]
    assert any("BAB 1" in t for t in texts)
    assert any("strategi" in t for t in texts)
```

- [ ] **Step 2: Run the tests to confirm they fail**

Run: `python -m pytest "Dev Assistant/scripts/translate_gamble/tests/test_render.py" -v`
Expected: `ImportError` on `render`.

- [ ] **Step 3: Implement `render.py`**

Create `Dev Assistant/scripts/translate_gamble/render.py`:
```python
"""Stage 3: translated JSON -> single DOCX with italic terms + embedded images."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.shared import Inches, Pt


def italic_runs(text: str, spans: list[tuple[int, int]]) -> list[tuple[str, bool]]:
    """Split text into (substring, is_italic) runs at the given char spans."""
    if not spans:
        return [(text, False)]
    spans_sorted = sorted(spans)
    runs: list[tuple[str, bool]] = []
    cursor = 0
    for start, end in spans_sorted:
        if start < cursor:
            continue  # skip overlaps
        if start > cursor:
            runs.append((text[cursor:start], False))
        runs.append((text[start:end], True))
        cursor = end
    if cursor < len(text):
        runs.append((text[cursor:], False))
    return runs


def _add_paragraph_with_runs(
    doc: Document,
    text: str,
    spans: list[tuple[int, int]],
    *,
    style: str | None = None,
    align: int | None = None,
    italic_all: bool = False,
) -> None:
    para = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    if align is not None:
        para.alignment = align
    for substring, is_italic in italic_runs(text, spans):
        run = para.add_run(substring)
        run.italic = is_italic or italic_all
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)


def _add_heading(doc: Document, text: str, level: int, page_break: bool) -> None:
    if page_break:
        # Add a page break paragraph before the heading
        br = doc.add_paragraph()
        br.add_run().add_break(WD_BREAK.PAGE)
    h = doc.add_heading(text, level=max(1, min(level, 3)))
    for run in h.runs:
        run.font.name = "Times New Roman"


def render_to_docx(translated_pages_dir: Path, images_dir: Path, out_path: Path) -> None:
    doc = Document()

    # Set default body justification on the Normal style
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(11)

    page_files = sorted(translated_pages_dir.glob("page_*.json"))
    last_chapter: int | None = None

    for src in page_files:
        payload: dict[str, Any] = json.loads(src.read_text(encoding="utf-8"))
        chapter = payload.get("chapter")
        for block in payload["blocks"]:
            btype = block["type"]
            spans = [tuple(p) for p in block.get("italic_spans", [])]
            text = block.get("text", "")

            if btype == "heading":
                level = int(block.get("level", 2))
                new_chapter = (
                    level == 1
                    and chapter is not None
                    and chapter != last_chapter
                )
                _add_heading(doc, text, level, page_break=new_chapter and last_chapter is not None)
                if new_chapter:
                    last_chapter = chapter
            elif btype == "body":
                _add_paragraph_with_runs(
                    doc, text, spans, align=WD_ALIGN_PARAGRAPH.JUSTIFY
                )
            elif btype == "list_item":
                _add_paragraph_with_runs(
                    doc, text, spans, style="List Bullet", align=WD_ALIGN_PARAGRAPH.JUSTIFY
                )
            elif btype == "caption":
                _add_paragraph_with_runs(
                    doc, text, spans, align=WD_ALIGN_PARAGRAPH.CENTER, italic_all=True
                )
            elif btype == "image":
                ref = block.get("ref")
                if not ref:
                    continue
                img_path = images_dir / ref
                if not img_path.exists():
                    continue
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.add_run().add_picture(str(img_path), width=Inches(5.5))

    doc.save(str(out_path))


if __name__ == "__main__":
    import sys
    base = Path("Dev Assistant/scripts/translate_gamble/build")
    pages = Path(sys.argv[1]) if len(sys.argv) > 1 else base / "translated"
    imgs = Path(sys.argv[2]) if len(sys.argv) > 2 else base / "extracted" / "images"
    out = Path(sys.argv[3]) if len(sys.argv) > 3 else Path("Temu 1-7 Buku Gamble (Bahasa Indonesia).docx")
    render_to_docx(pages, imgs, out)
    print(f"Wrote {out}")
```

Note: `add_picture` on a run is not directly supported by python-docx — fix this in Step 3a below.

- [ ] **Step 3a: Fix the image insertion (python-docx API quirk)**

In `render.py`, replace the `elif btype == "image":` branch with:
```python
            elif btype == "image":
                ref = block.get("ref")
                if not ref:
                    continue
                img_path = images_dir / ref
                if not img_path.exists():
                    continue
                doc.add_picture(str(img_path), width=Inches(5.5))
                # Centre the picture's paragraph
                doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
```

- [ ] **Step 4: Run the tests to confirm they pass**

Run: `python -m pytest "Dev Assistant/scripts/translate_gamble/tests/test_render.py" -v`
Expected: 5 passed.

- [ ] **Step 5: Commit**

```bash
git add "Dev Assistant/scripts/translate_gamble/render.py" "Dev Assistant/scripts/translate_gamble/tests/test_render.py"
git commit -m "feat(translate_gamble): render stage — DOCX with italic runs and inline images"
```

---

## Task 6: Orchestrator CLI (`run.py`)

**Files:**
- Create: `Dev Assistant/scripts/translate_gamble/run.py`

- [ ] **Step 1: Implement `run.py`**

Create `Dev Assistant/scripts/translate_gamble/run.py`:
```python
"""End-to-end orchestrator. Runs extract -> translate -> render with optional stage skipping."""
from __future__ import annotations
import argparse
from pathlib import Path

from translate_gamble.extract import extract_pdf
from translate_gamble.render import render_to_docx
from translate_gamble.translate import translate_pages


def main() -> None:
    parser = argparse.ArgumentParser(description="Gamble Ch1-7 EN -> ID pipeline")
    parser.add_argument(
        "--pdf", type=Path, default=Path("Temu 1-7 Buku Gamble.pdf"),
        help="Source PDF",
    )
    parser.add_argument(
        "--build-dir", type=Path,
        default=Path("Dev Assistant/scripts/translate_gamble/build"),
        help="Where to store intermediate artifacts",
    )
    parser.add_argument(
        "--out", type=Path,
        default=Path("Temu 1-7 Buku Gamble (Bahasa Indonesia).docx"),
        help="Final DOCX output path",
    )
    parser.add_argument(
        "--only-stage", choices=["extract", "translate", "render"],
        help="Run only this stage (assumes prior stages already produced their outputs)",
    )
    args = parser.parse_args()

    extracted = args.build_dir / "extracted"
    translated = args.build_dir / "translated"
    cache = args.build_dir / "cache"
    images = extracted / "images"

    run_extract = args.only_stage in (None, "extract")
    run_translate = args.only_stage in (None, "translate")
    run_render = args.only_stage in (None, "render")

    if run_extract:
        print(f"[1/3] Extracting {args.pdf} -> {extracted}")
        extract_pdf(args.pdf, extracted)
    if run_translate:
        print(f"[2/3] Translating -> {translated}")
        translate_pages(extracted, translated, cache)
    if run_render:
        print(f"[3/3] Rendering -> {args.out}")
        render_to_docx(translated, images, args.out)

    print("Done.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Smoke-run --only-stage render against the pre-flight 3-page data**

Run:
```
python "Dev Assistant/scripts/translate_gamble/run.py" --only-stage render --build-dir "Dev Assistant/scripts/translate_gamble/build/preflight" --out "preflight_out.docx"
```
Expected: produces `preflight_out.docx`. Open it in Word; should contain Indonesian text with a couple of italicized English terms and at least one embedded image. Delete `preflight_out.docx` after inspection.

- [ ] **Step 3: Commit**

```bash
git add "Dev Assistant/scripts/translate_gamble/run.py"
git commit -m "feat(translate_gamble): orchestrator CLI with --only-stage"
```

---

## Task 7: Verification script

**Files:**
- Create: `Dev Assistant/scripts/translate_gamble/verify.py`

- [ ] **Step 1: Implement verifier**

Create `Dev Assistant/scripts/translate_gamble/verify.py`:
```python
"""Post-build sanity checks on the final DOCX."""
from __future__ import annotations
import sys
from pathlib import Path

from docx import Document


def verify(docx_path: Path) -> list[str]:
    failures: list[str] = []
    if not docx_path.exists():
        return [f"DOCX not found: {docx_path}"]

    doc = Document(str(docx_path))

    # Check 5: no surviving sentinels
    all_text = "\n".join(p.text for p in doc.paragraphs)
    if "§T" in all_text:
        failures.append("Found surviving §T sentinels in output")

    # Check 4: at least one image present
    image_count = sum(1 for p in doc.paragraphs for r in p.runs if r.element.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}inline"))
    # Above XPath is unreliable; do a simpler check via relationships
    rels = doc.part.rels
    img_rel_count = sum(1 for r in rels.values() if "image" in r.target_ref)
    if img_rel_count < 10:
        failures.append(f"Only {img_rel_count} images embedded (expected >=10 for 7 chapters)")

    # Check 6: at least one Heading 1 per chapter (rough proxy)
    h1_count = sum(1 for p in doc.paragraphs if p.style and p.style.name == "Heading 1")
    if h1_count < 7:
        failures.append(f"Only {h1_count} Heading 1 paragraphs (expected >=7, one per chapter)")

    return failures


if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("Temu 1-7 Buku Gamble (Bahasa Indonesia).docx")
    fails = verify(path)
    if fails:
        for f in fails:
            print(f"FAIL: {f}")
        sys.exit(1)
    print("OK")
```

- [ ] **Step 2: Commit**

```bash
git add "Dev Assistant/scripts/translate_gamble/verify.py"
git commit -m "test(translate_gamble): post-build verifier for final DOCX"
```

---

## Task 8: Full end-to-end run

**Files:**
- Modify: none (produces `Temu 1-7 Buku Gamble (Bahasa Indonesia).docx` at repo root)

- [ ] **Step 1: Run the full pipeline**

Run (will take ~15–30 minutes due to Google Translate rate limiting):
```
python "Dev Assistant/scripts/translate_gamble/run.py"
```
Expected: prints `[1/3]`, `[2/3]`, `[3/3]` and final `Done.` Translation stage prints `[N/150]` progress per page. The cache means a partial run that crashes is resumable — re-running picks up where it left off.

- [ ] **Step 2: Run the verifier**

Run:
```
python "Dev Assistant/scripts/translate_gamble/verify.py"
```
Expected: prints `OK`. If FAIL lines appear, inspect them, fix the relevant stage, then re-run `run.py --only-stage <stage>` and verify again.

- [ ] **Step 3: Manual spot-check (5 random pages)**

Open `Temu 1-7 Buku Gamble (Bahasa Indonesia).docx` in Word. Pick 5 random pages spanning all 7 chapters. For each, confirm:
- The text reads as Indonesian.
- Glossary terms (e.g. *strategy*, *value chain*, *SWOT*) appear in italic and in English.
- Figures/tables from the original PDF appear in the right vicinity.

If a page is badly broken (e.g. all sentinels survived), STOP and debug Stage 2.

- [ ] **Step 4: Commit the final DOCX**

```bash
git add "Temu 1-7 Buku Gamble (Bahasa Indonesia).docx"
git commit -m "feat: final Bahasa Indonesia translation of Gamble Ch1-7"
```

---

## Summary

8 tasks, ~3–4 hours of engineering plus ~30 minutes of unattended translation runtime. Every stage is independently rerunnable. Cache means glossary edits don't force a full re-translation — only the affected blocks change because the SQLite key includes `GLOSSARY_VERSION`. Bump that constant to invalidate cache when the glossary changes.
