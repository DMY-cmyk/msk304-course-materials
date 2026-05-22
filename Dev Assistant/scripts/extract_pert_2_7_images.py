"""Extract 33 cropped images for Pertemuan 2-7 from TPGS Ch.2/3/4/5/6/8.

Renders at 300 DPI using explicit per-target crop rects auto-tuned to each
figure/sidebar's content extent (label + body + Sources line), trimmed to
avoid bleeding into adjacent body text.
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
    (54, "pertemuan-2", "fig_2_1.png", (45.0, 52.0, 510.0, 295.0), "FIGURE 2.1"),
    (66, "pertemuan-2", "fig_2_2.png", (34.0, 52.0, 515.0, 440.0), "FIGURE 2.2"),
    (57, "pertemuan-2", "cc_2_1.png", (68.0, 53.4, 511.2, 589.3), "CONCEPTS & CONNECTIONS 2.1"),
    (60, "pertemuan-2", "cc_2_2.png", (39.5, 218.4, 502.5, 541.1), "CONCEPTS & CONNECTIONS 2.2"),
    (63, "pertemuan-2", "cc_2_3.png", (68.0, 53.4, 534.0, 399.8), "CONCEPTS & CONNECTIONS 2.3"),
    (70, "pertemuan-2", "cc_2_4.png", (39.5, 53.4, 505.5, 609.2), "CONCEPTS & CONNECTIONS 2.4"),
    (77, "pertemuan-3", "fig_3_1.png", (67.4, 393.8, 500.2, 677.3), "FIGURE 3.1"),
    (79, "pertemuan-3", "fig_3_2.png", (62.0, 254.1, 538.0, 677.5), "FIGURE 3.2"),
    (81, "pertemuan-3", "fig_3_3.png", (62.0, 271.5, 534.8, 675.0), "FIGURE 3.3"),
    (83, "pertemuan-3", "fig_3_4.png", (62.0, 52.4, 526.7, 687.0), "FIGURE 3.4"),
    (85, "pertemuan-3", "fig_3_5.png", (62.0, 52.6, 530.6, 687.8), "FIGURE 3.5"),
    (87, "pertemuan-3", "fig_3_6.png", (62.0, 52.4, 490.0, 590.8), "FIGURE 3.6"),
    (88, "pertemuan-3", "fig_3_7.png", (33.6, 52.4, 509.8, 687.9), "FIGURE 3.7"),
    (95, "pertemuan-3", "cc_3_1.png", (62.3, 53.4, 533.1, 687.9), "CONCEPTS & CONNECTIONS 3.1"),
    (112, "pertemuan-4", "fig_4_1.png", (33.5, 52.4, 499.5, 647.8), "FIGURE 4.1"),
    (115, "pertemuan-4", "fig_4_2.png", (62.6, 465.7, 435.2, 687.3), "FIGURE 4.2"),
    (113, "pertemuan-4", "cc_4_1.png", (68.0, 53.4, 508.2, 414.4), "CONCEPTS & CONNECTIONS 4.1"),
    (128, "pertemuan-5", "fig_5_1.png", (129.6, 52.4, 506.4, 343.5), "FIGURE 5.1"),
    (130, "pertemuan-5", "fig_5_2.png", (129.5, 52.4, 497.0, 400.3), "FIGURE 5.2"),
    (135, "pertemuan-5", "fig_5_3.png", (62.0, 52.4, 429.5, 409.6), "FIGURE 5.3"),
    (132, "pertemuan-5", "cc_5_1.png", (39.5, 53.5, 505.5, 527.2), "CONCEPTS & CONNECTIONS 5.1"),
    (141, "pertemuan-5", "cc_5_2.png", (67.8, 53.4, 534.1, 506.6), "CONCEPTS & CONNECTIONS 5.2"),
    (142, "pertemuan-5", "cc_5_3.png", (39.5, 53.5, 505.5, 491.2), "CONCEPTS & CONNECTIONS 5.3"),
    (144, "pertemuan-5", "cc_5_4.png", (39.5, 53.4, 505.5, 523.5), "CONCEPTS & CONNECTIONS 5.4"),
    (149, "pertemuan-6", "fig_6_1.png", (67.4, 244.9, 432.3, 683.0), "FIGURE 6.1"),
    (153, "pertemuan-6", "cc_6_1.png", (68.0, 53.4, 534.0, 337.4), "CONCEPTS & CONNECTIONS 6.1"),
    (159, "pertemuan-6", "cc_6_2.png", (68.0, 53.1, 534.0, 567.7), "CONCEPTS & CONNECTIONS 6.2"),
    (163, "pertemuan-6", "cc_6_3.png", (68.0, 53.4, 534.0, 554.9), "CONCEPTS & CONNECTIONS 6.3"),
    (194, "pertemuan-7", "fig_8_1.png", (33.5, 316.7, 427.2, 688.5), "FIGURE 8.1"),
    (195, "pertemuan-7", "fig_8_2.png", (62.0, 330.7, 511.6, 687.8), "FIGURE 8.2"),
    (206, "pertemuan-7", "fig_8_3.png", (33.5, 52.4, 501.0, 558.6), "FIGURE 8.3"),
    (210, "pertemuan-7", "fig_8_4.png", (129.5, 425.6, 484.1, 685.0), "FIGURE 8.4"),
    (197, "pertemuan-7", "cc_8_1.png", (62.0, 113.5, 534.0, 656.1), "CONCEPTS & CONNECTIONS 8.1"),
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
