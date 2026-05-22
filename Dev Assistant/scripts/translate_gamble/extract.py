"""Stage 1: PDF -> per-page structured JSON + extracted figure PNGs."""
from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF

_CHAPTER_HEADER_RE = re.compile(
    r"^(?:"
    r"CHAPTER\s+(\d{1,2})"  # "CHAPTER 3" with optional title after
    r"|(\d{1,2})\s+[A-Z][A-Z'\s,]{4,}"  # "3 EVALUATING A COMPANY'S..." (number + all-caps title)
    r")$"
)
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
        # Group 1: CHAPTER N form; Group 2: N TITLE form
        return int(match.group(1) or match.group(2))
    return None


def detect_chapter_from_blocks(raw_blocks: list[dict]) -> int | None:
    """Scan all blocks on a page for the giant-digit + all-caps-title pair.

    A chapter-start page contains BOTH:
    1. A span with font size >= 30pt whose stripped text is exactly one or two
       digits (the giant chapter number).
    2. A span with font size >= 14pt whose stripped text is uppercase
       letters/punctuation with length >= 15 (the chapter title banner).
       OR a block whose aggregated text (via _block_text_and_style) satisfies
       the same criterion.

    Detection operates at the *span* level so it handles the common layout
    where the title and chapter digit share the same block (merged by MuPDF).

    Returns the chapter number (int) if both signals are found, else None.
    """
    giant_digit: int | None = None
    has_uppercase_title = False

    for blk in raw_blocks:
        if blk.get("type", 0) != 0:
            continue
        for line in blk.get("lines", []):
            for span in line.get("spans", []):
                txt = span.get("text", "").strip()
                size = float(span.get("size", 0.0))
                if not txt:
                    continue

                # Signal 1: giant digit span (1–2 digits, font >= 30pt)
                if size >= 30.0 and re.fullmatch(r"\d{1,2}", txt):
                    giant_digit = int(txt)

                # Signal 2: all-caps title span (font >= 14pt, len >= 15,
                # only uppercase letters + common punctuation)
                if (
                    size >= 14.0
                    and len(txt) >= 15
                    and re.fullmatch(r"[A-Z0-9\s,\.\-\'\"&/’‘]+", txt)
                ):
                    has_uppercase_title = True

        # Also check the aggregated block text for Signal 2 (covers multi-line
        # uppercase titles that individually may be short per span)
        if not has_uppercase_title:
            block_text, block_size, _ = _block_text_and_style(blk)
            stripped = block_text.strip()
            if (
                block_size >= 14.0
                and len(stripped) >= 15
                and re.fullmatch(r"[A-Z0-9\s,\.\-\'\"&/’‘â]+", stripped)
            ):
                has_uppercase_title = True

    if giant_digit is not None and has_uppercase_title:
        return giant_digit
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


_PNG_OK_CS_NAMES = {"DeviceGray", "DeviceRGB"}


def _to_png_compatible(pix: fitz.Pixmap) -> fitz.Pixmap:
    """Return a pixmap that MuPDF's PNG writer can handle (grayscale or RGB, no alpha)."""
    cs = pix.colorspace
    # Convert any non-Gray/RGB colorspace (CMYK, DeviceN, separation…) to RGB
    if cs is None or cs.name not in _PNG_OK_CS_NAMES:
        pix = fitz.Pixmap(fitz.csRGB, pix)
    if pix.alpha:
        pix = fitz.Pixmap(pix, 0)
    return pix


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
        try:
            pix = _to_png_compatible(pix)
            fname = f"page_{page_num:03d}_img{img_index}.png"
            out_path = img_dir / fname
            out_path.write_bytes(pix.tobytes("png"))
            records.append({"type": "image", "ref": fname})
        except Exception:
            pass  # skip unrenderable images
        finally:
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

            # Chapter detection: scan all blocks for giant-digit + all-caps-title pair
            ch = detect_chapter_from_blocks(raw.get("blocks", []))
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
