"""Extract 3 cropped images from TPGS Ch.1 for Pertemuan 1 RMK.

Renders at 300 DPI and crops to the bounding box of the figure/sidebar
plus a 12pt padding margin.
"""
from __future__ import annotations
import sys
from pathlib import Path
import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parents[2]
PDF_PATH = ROOT / "Ebook" / (
    "(Business professional collection) John E. Gamble_ Arthur A. Thompson_ "
    "Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest "
    "for Competitive Advantage (2021).pdf"
)
OUT_DIR = ROOT / "images" / "pertemuan-1"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DPI = 300
ZOOM = DPI / 72
MATRIX = fitz.Matrix(ZOOM, ZOOM)
PAD = 12  # PDF points of padding around the discovered bounding box

# (pdf_page_index_0based, text_marker_prefix, output_filename, explicit_crop)
# explicit_crop = (x0, y0, x1, y1) in PDF points; None falls back to heuristic.
# Crops were measured directly from each page's text/image block bboxes after
# the heuristic mis-clipped narrow-seed cases (FIGURE 1.1) and 3-column
# layouts (CONCEPTS & CONNECTIONS 1.1).
TARGETS = [
    (44, "CONCEPTS & CONNECTIONS 1.1", "cc_1_1.png",
     (45.0, 58.0, 530.0, 626.0)),
    (46, "CONCEPTS & CONNECTIONS 1.2", "cc_1_2.png",
     (45.0, 58.0, 502.0, 462.0)),
    (47, "FIGURE 1.1",                 "fig_1_1.png",
     (60.0, 440.0, 535.0, 672.0)),
]


def find_marker_block(page: fitz.Page, marker: str) -> fitz.Rect | None:
    """Return the bbox of the text block whose first line starts with `marker`."""
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        text = "".join(
            span["text"]
            for line in block.get("lines", [])
            for span in line.get("spans", [])
        )
        if text.strip().upper().startswith(marker.upper()):
            return fitz.Rect(block["bbox"])
    return None


def union_nearby_blocks(page: fitz.Page, seed: fitz.Rect) -> fitz.Rect:
    """Expand the seed bbox to include text/image blocks within the same column
    that are visually contiguous (within 20 pts vertically)."""
    page_rect = page.rect
    column_left  = seed.x0 - 8
    column_right = seed.x1 + 8
    rect = fitz.Rect(seed)
    changed = True
    while changed:
        changed = False
        for block in page.get_text("dict")["blocks"]:
            bbox = fitz.Rect(block["bbox"])
            if bbox.x0 < column_left or bbox.x1 > column_right + 220:
                continue
            if rect.intersects(bbox):
                continue
            vgap_top = bbox.y0 - rect.y1
            vgap_bot = rect.y0 - bbox.y1
            if -20 < vgap_top < 20 or -20 < vgap_bot < 20:
                rect |= bbox
                changed = True
    # also pull in image blocks on the page that fall inside the union
    for img_block in page.get_text("dict")["blocks"]:
        if img_block.get("type") == 1:
            ibox = fitz.Rect(img_block["bbox"])
            if rect.intersects(ibox):
                rect |= ibox
    # apply padding, clip to page
    rect.x0 -= PAD; rect.y0 -= PAD
    rect.x1 += PAD; rect.y1 += PAD
    rect &= page_rect
    return rect


def render(page: fitz.Page, rect: fitz.Rect, out: Path) -> None:
    pix = page.get_pixmap(matrix=MATRIX, clip=rect, alpha=False)
    pix.save(out)
    print(f"wrote {out}  ({pix.width}x{pix.height} px)")


def main() -> int:
    if not PDF_PATH.exists():
        print(f"PDF not found: {PDF_PATH}", file=sys.stderr)
        return 1
    doc = fitz.open(PDF_PATH)
    for pno, marker, fname, explicit_crop in TARGETS:
        page = doc[pno]
        if explicit_crop is not None:
            rect = fitz.Rect(*explicit_crop) & page.rect
        else:
            seed = find_marker_block(page, marker)
            if seed is None:
                print(f"marker not found on page {pno+1}: {marker}",
                      file=sys.stderr)
                return 2
            rect = union_nearby_blocks(page, seed)
        render(page, rect, OUT_DIR / fname)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
