"""Extract 33 cropped images for Pertemuan 2-7 from TPGS Ch.2/3/4/5/6/8.

Renders at 300 DPI using explicit per-target crop rects measured from
each PDF page's text/image block layout.
"""
from __future__ import annotations
import sys
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[2]
PDF_PATH = ROOT / "Ebook" / (
    "(Business professional collection) John E. Gamble_ Arthur A. Thompson_ "
    "Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest "
    "for Competitive Advantage (2021).pdf"
)

DPI = 300
ZOOM = DPI / 72
MATRIX = fitz.Matrix(ZOOM, ZOOM)

# Each target: (pdf_pg_0idx, subdir_pertN, out_filename, crop_rect, marker)
TARGETS = [
    # ---- Pertemuan 2 (Ch.2) — 2 Figures + 4 C&C = 6 images ----
    (54, "pertemuan-2", "fig_2_1.png", (45.0, 50.0, 530.0, 405.0),  "FIGURE 2.1"),
    (66, "pertemuan-2", "fig_2_2.png", (45.0, 50.0, 530.0, 680.0),  "FIGURE 2.2"),
    (57, "pertemuan-2", "cc_2_1.png",  (45.0, 50.0, 530.0, 685.0),  "CONCEPTS & CONNECTIONS 2.1"),
    (60, "pertemuan-2", "cc_2_2.png",  (45.0, 50.0, 530.0, 685.0),  "CONCEPTS & CONNECTIONS 2.2"),
    (63, "pertemuan-2", "cc_2_3.png",  (45.0, 380.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 2.3"),
    (70, "pertemuan-2", "cc_2_4.png",  (45.0, 50.0, 530.0, 685.0),  "CONCEPTS & CONNECTIONS 2.4"),

    # ---- Pertemuan 3 (Ch.3) — 7 Figures + 1 C&C = 8 images ----
    (77, "pertemuan-3", "fig_3_1.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 3.1"),
    (79, "pertemuan-3", "fig_3_2.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 3.2"),
    (81, "pertemuan-3", "fig_3_3.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 3.3"),
    (83, "pertemuan-3", "fig_3_4.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 3.4"),
    (85, "pertemuan-3", "fig_3_5.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 3.5"),
    (87, "pertemuan-3", "fig_3_6.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 3.6"),
    (88, "pertemuan-3", "fig_3_7.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 3.7"),
    (95, "pertemuan-3", "cc_3_1.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 3.1"),

    # ---- Pertemuan 4 (Ch.4) — 2 Figures + 1 C&C = 3 images ----
    (112, "pertemuan-4", "fig_4_1.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 4.1"),
    (115, "pertemuan-4", "fig_4_2.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 4.2"),
    (113, "pertemuan-4", "cc_4_1.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 4.1"),

    # ---- Pertemuan 5 (Ch.5) — 3 Figures + 4 C&C = 7 images ----
    (128, "pertemuan-5", "fig_5_1.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 5.1"),
    (130, "pertemuan-5", "fig_5_2.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 5.2"),
    (135, "pertemuan-5", "fig_5_3.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 5.3"),
    (132, "pertemuan-5", "cc_5_1.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 5.1"),
    (141, "pertemuan-5", "cc_5_2.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 5.2"),
    (142, "pertemuan-5", "cc_5_3.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 5.3"),
    (144, "pertemuan-5", "cc_5_4.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 5.4"),

    # ---- Pertemuan 6 (Ch.6) — 1 Figure + 3 C&C = 4 images ----
    (149, "pertemuan-6", "fig_6_1.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 6.1"),
    (153, "pertemuan-6", "cc_6_1.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 6.1"),
    (159, "pertemuan-6", "cc_6_2.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 6.2"),
    (163, "pertemuan-6", "cc_6_3.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 6.3"),

    # ---- Pertemuan 7 (Ch.8) — 4 Figures + 1 C&C = 5 images ----
    (194, "pertemuan-7", "fig_8_1.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 8.1"),
    (195, "pertemuan-7", "fig_8_2.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 8.2"),
    (206, "pertemuan-7", "fig_8_3.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 8.3"),
    (210, "pertemuan-7", "fig_8_4.png", (45.0, 50.0, 530.0, 700.0), "FIGURE 8.4"),
    (197, "pertemuan-7", "cc_8_1.png",  (45.0, 50.0, 530.0, 700.0), "CONCEPTS & CONNECTIONS 8.1"),
]


def render(page, rect, out: Path):
    pix = page.get_pixmap(matrix=MATRIX, clip=rect, alpha=False)
    out.parent.mkdir(parents=True, exist_ok=True)
    pix.save(out)
    return pix.width, pix.height


def main() -> int:
    if not PDF_PATH.exists():
        print(f"PDF not found: {PDF_PATH}", file=sys.stderr)
        return 1
    doc = fitz.open(PDF_PATH)
    out_root = ROOT / "images"
    for pno, subdir, fname, crop, marker in TARGETS:
        page = doc[pno]
        rect = fitz.Rect(*crop) & page.rect
        out = out_root / subdir / fname
        w, h = render(page, rect, out)
        print(f"wrote {out.relative_to(ROOT)} ({w}x{h} px)")
    print(f"\nTotal: {len(TARGETS)} images written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
