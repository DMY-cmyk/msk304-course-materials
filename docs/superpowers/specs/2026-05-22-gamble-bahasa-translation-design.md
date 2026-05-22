# Bahasa Indonesia Translation of *Temu 1–7 Buku Gamble*

**Date:** 2026-05-22
**Status:** Draft — awaiting user review
**Owner:** Dzaki

## 1. Goal

Produce a faithful Bahasa Indonesia reading-aid translation of `Temu 1-7 Buku Gamble.pdf`
(150 pages, Chapters 1–7 of Gamble's *Strategic Management*) as a single DOCX file,
preserving the original figures and tables as embedded images, with core
strategic-management jargon left in English and rendered in italic.

## 2. Non-goals

- Publication-grade Indonesian translation. Output is a study aid, not a textbook to be sold.
- Pixel-perfect layout parity with the original (no two-column reproduction).
- Translation of text *inside* figure images (image content stays English).
- Editing the original PDF or producing a side-by-side bilingual document.
- Re-running translation on every minor glossary tweak (caching is required, see §6).

## 3. Inputs and Outputs

**Input:**
- `Temu 1-7 Buku Gamble.pdf` (150 pages, 12.7 MB) in the project root.

**Outputs (final artifact):**
- `Temu 1-7 Buku Gamble (Bahasa Indonesia).docx` in the project root.

**Intermediate artifacts** (under `Dev Assistant/scripts/translate_gamble/build/`,
gitignored):
- `extracted/page_{NNN}.json` — structured per-page blocks.
- `extracted/images/page_{NNN}_img{K}.png` — extracted figures.
- `translated/page_{NNN}.json` — translated blocks with italic-span markers.
- `cache/translations.sqlite` — block-hash → translation cache.

## 4. Architecture — Three Isolated Stages

Each stage reads from the previous stage's on-disk artifacts and writes its own.
Any stage can be re-run independently.

```
PDF ──extract.py──► extracted/  ──translate.py──► translated/  ──render.py──► DOCX
                                       │
                                       └── glossary.py (mask/unmask)
                                       └── cache (SQLite)
```

### 4.1 Stage 1 — `extract.py`

**Input:** PDF path.
**Output:** `extracted/page_{NNN}.json` + image PNGs.

For each page, emit a JSON document:

```json
{
  "page": 12,
  "chapter": 1,
  "blocks": [
    {"type": "heading", "level": 1, "text": "...", "bbox": [x0,y0,x1,y1]},
    {"type": "body",    "text": "...", "bbox": [...]},
    {"type": "caption", "ref": "page_012_img0.png", "text": "FIGURE 1.2 ..."},
    {"type": "list_item", "text": "..."},
    {"type": "image",   "ref": "page_012_img0.png", "bbox": [...]}
  ]
}
```

**Block classification rules:**
- Font size ≥ 16pt → `heading` level 1
- Font size 13–15pt + bold → `heading` level 2
- Font size 11–12pt + bold + UPPERCASE → `heading` level 3
- Text starting with bullet marker (`•`, `–`, `■`) → `list_item`
- Text immediately below a detected image, ≤ 60 chars or matching `^(FIGURE|TABLE)\s\d` → `caption`
- Everything else → `body`

**Chapter detection:** match `^CHAPTER \d+\b` or `^\d+\s+[A-Z]{3,}` at top of page → record as chapter start, propagate `chapter` field forward until next start.

**Images:** PyMuPDF `page.get_images()` extracts every embedded image. Save as PNG only if width ≥ 100px and area ≥ 10000px² (filters out decorative rules and bullets).

**Tables:** Out of scope for v1 — table regions flow as ordinary `body` blocks.
Re-formatting tables is deferred; see §9 Risks.

### 4.2 Stage 2 — `translate.py`

**Input:** `extracted/page_{NNN}.json`.
**Output:** `translated/page_{NNN}.json` with the same shape, but every text field replaced
by its Indonesian translation and a parallel `italic_spans` field listing
`(start, end)` character offsets of protected terms.

**Per-block algorithm:**
1. Hash the original text. If present in `cache/translations.sqlite`, reuse.
2. Call `glossary.mask(text) → (masked, mapping)`. Sentinels are short tokens
   `§T###§` that Google Translate leaves intact across language boundaries
   (verified in §10).
3. Call `deep_translator.GoogleTranslator(source='en', target='id').translate(masked)`.
4. Call `glossary.unmask(translated, mapping) → (text_id, italic_spans)`.
5. Write `(hash, text_id, italic_spans)` to cache and to the output JSON.

**Rate limiting:** 1 request per 200ms (Google's free endpoint tolerates ~5 RPS;
we stay well under). On HTTP 429, exponential backoff up to 30s, then fail loud.

**Chunking:** Google's free endpoint accepts ~5000 chars per request. Split body
blocks longer than 4500 chars at sentence boundaries before sending.

### 4.3 Stage 3 — `render.py`

**Input:** `translated/page_{NNN}.json`.
**Output:** `Temu 1-7 Buku Gamble (Bahasa Indonesia).docx`.

Walk pages in order. For each block:
- `heading level=N` → `document.add_heading(text, level=N)`. Insert a page break
  before any chapter-start heading (detected via `chapter` field change).
- `body` → `add_paragraph` with `Body Text` style, justified, 11pt. Use the
  `italic_spans` to split into runs and italicize the protected spans.
- `list_item` → `add_paragraph(style='List Bullet')`, same italic-run logic.
- `caption` → italic single-run paragraph centred under the image.
- `image` → `add_picture(ref, width=Inches(5.5))` with `CENTER` alignment.

Apply project-standard styles (matches existing RMK/Pertemuan formatting per
recent commits `5b6c58b`, `82c7d29`):
- Body text justified (`jc=both`)
- Tables (when added) get grid borders
- Font: Times New Roman 11pt for body, 14/13/12pt for H1/H2/H3

### 4.4 `glossary.py` — protected-terms data + mask/unmask

A flat list of ~80 strategic-management terms plus regex hooks for proper nouns.

**Categories:**
- **Core jargon** (≈60 entries, hard-coded): *strategy*, *business model*,
  *competitive advantage*, *value proposition*, *profit formula*, *SWOT*,
  *PESTEL*, *value chain*, *core competencies*, *first-mover advantage*,
  *Porter's Five Forces*, *blue ocean*, *VRIN*, *balanced scorecard*,
  *strategic group map*, *driving forces*, *generic strategy*,
  *broad differentiation*, *focused low-cost*, *best-cost provider*, etc.
  (Full list maintained in `glossary.py`; reviewable and editable.)
- **Auto-detected** at extraction time:
  - Sequences of ≥2 capitalized words (proper nouns / company names)
  - All-caps acronyms ≥ 3 letters
  - Inline italics in the source PDF (font-flag check)

**API:**
```python
def mask(text: str) -> tuple[str, dict[str, str]]:
    """Replace each protected term with §T###§. Return masked text + mapping."""

def unmask(translated: str, mapping: dict[str, str]) -> tuple[str, list[tuple[int,int]]]:
    """Restore originals. Return final text and (start,end) spans to italicize."""
```

Matching is **case-insensitive whole-word** with longest-match-first to avoid
*"competitive"* eating *"competitive advantage"*. Restored text preserves the
original capitalization from the glossary.

## 5. Directory Layout

```
Dev Assistant/scripts/translate_gamble/
├── __init__.py
├── glossary.py
├── extract.py
├── translate.py
├── render.py
├── run.py              # CLI: orchestrates all 3 stages, supports --only-stage N
└── build/              # gitignored
    ├── extracted/
    ├── translated/
    └── cache/translations.sqlite
```

Add `Dev Assistant/scripts/translate_gamble/build/` to `.gitignore`.

## 6. Caching and Re-runs

- `translations.sqlite` keyed by `sha256(source_text + glossary_version)`.
- Bumping `GLOSSARY_VERSION` constant in `glossary.py` invalidates all cache entries
  on next run (forces re-translation against the new term list).
- `run.py --only-stage extract|translate|render` skips earlier stages if their
  outputs exist. `--force` re-runs ignoring caches.

## 7. Dependencies

Already installed:
- `PyMuPDF` 1.27.1 (PDF extraction)
- `python-docx` 1.2.0 (DOCX rendering)

To install:
- `deep-translator` (Google Translate wrapper, no API key)

Add to `requirements.txt` if one exists, else document in this spec.

## 8. Validation / Acceptance

A run is acceptable when **all** of these hold:

1. `run.py` completes end-to-end with exit code 0.
2. Output DOCX exists, opens cleanly in Word, and is 100–250 pages.
3. **Spot-check on 5 random pages**: every glossary term that appears in the source
   page appears italicized in the output, in its original English form.
4. Every figure/table image from the source PDF that survived the size filter
   (§4.1) appears in the DOCX in the right chapter.
5. No raw `§T###§` sentinels visible in the output (grep the DOCX text).
6. Chapter 1, Chapter 4, and Chapter 7 headings all appear styled as Heading 1
   and start on a new page.

A validation script `verify.py` automates checks 4, 5, 6 by reading the rendered
DOCX with python-docx and asserting. Checks 1, 2, 3 are manual.

## 9. Risks and Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Google Translate rate-limits / blocks IP | Medium | Per-block caching means a partial run is never lost; resume from cache. Backoff on 429. |
| Sentinels `§T###§` corrupted by translator | Low | Pre-flight test on 10 sample blocks; if corruption detected, switch sentinel format. |
| Tables render as messy flowing text | High | Documented as known v1 limitation. Manual fix-up in Word acceptable for a study aid. |
| Headings misclassified (font-size heuristic fails) | Medium | Manual override list in `extract.py` for known-bad pages. Heading style still applied so user can fix visually. |
| Translation quality below user's bar | Medium | If unacceptable on spot-check, swap Stage 2 to Claude API (Haiku) — same JSON contract, drop-in replacement. |
| Foreign-language quotations inside body (e.g., French, Latin) get translated | Low | Auto-detect via `langdetect` and add to protected spans. Deferred unless spotted in spot-check. |

## 10. Open Questions / Pre-flight Tests

Before Stage 2 runs against all 150 pages, run a **pre-flight script** that:
- Translates 10 representative blocks (varied: heading, body, list, caption).
- Verifies sentinels round-trip intact.
- Prints diff for human eyeball check.

If pre-flight fails, fix sentinel format or glossary before bulk run.

## 11. Out of Scope (for this spec)

- Translating the front matter / table of contents of the original book (not present in this PDF excerpt anyway).
- Generating an index or Indonesian glossary appendix.
- Audio narration / e-book conversion.
- Re-translating into other languages.

These can be follow-up specs if wanted.
