"""Extract Pert. 8 exhibits: TPGS C&E 21e Ch.7 figures + Artikel 13/14 figures.

Two-pass workflow:
  pass 1 (--render-pages): render each target page full-size for visual bbox check
  pass 2 (default): crop per FIG_SPECS clip boxes -> PNG
Clip strategies verified against the page renders (2026-06-05):
  - 'between': top anchor (caption/figure start) -> bottom anchor (Source line /
    axis label / next-body-text start)
  - 'below':   anchor top -> bottom page margin (caption above, table fills rest)
  - 'above':   top page margin -> anchor bottom (figure on top, caption below)
"""
from __future__ import annotations

import sys
from pathlib import Path

import fitz

ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
TPGS = ROOT / "TPGS-21Ed-2018-Crafting and Executing Strategy Concepts (Temu 8 - 14).pdf"
ART13 = ROOT / "Article" / "Artikel 13.pdf"
ART14 = ROOT / "Article" / "Artikel 14.pdf"
OUT = ROOT / "Dev Assistant" / "temp" / "pert8_figures"
MAT = fitz.Matrix(3, 3)  # ~216-300 DPI effective

# (name, pdf, page_idx0, mode, anchor_top, anchor_bottom_or_None)
FIG_SPECS = [
    ("ch7_figure_7_1", TPGS, 224, "between", "FIGURE 7.1",
     "Source: Adapted from Michael E. Porter"),
    ("ch7_figure_7_2", TPGS, 236, "between", "FIGURE 7.2",
     "Need for Local Responsiveness"),
    # NB: anchor avoids the body-text mention "Table 7.1 provides a summary"
    # (search_for is case-insensitive) by matching the caption title text.
    ("ch7_table_7_1",  TPGS, 239, "below",
     "Advantages and Disadvantages of Multidomestic", None),
    ("art13_figure_2", ART13, 10, "between", "Figure 2: Interconnection",
     "Source: Author"),
    ("art13_figure_3", ART13, 11, "between", "Figure 3: Relationship",
     "Source: Author"),
    ("art13_table_3",  ART13, 14, "between", "Table 3: Characteristics",
     "Source: Based on Orlovska"),
    ("art14_figure_1", ART14, 2,  "above",   "Figure 1. Strategic Imperatives", None),
    ("art14_figure_2", ART14, 4,  "above",   "Figure 2. Cisco", None),
    ("art14_figure_3", ART14, 5,  "above",   "Figure 3. Case Study", None),
    ("art14_table_2",  ART14, 6,  "between", "Table 2. Research Questions",
     "to make approvals independently"),
]


def clip_for(pg: fitz.Page, mode: str, a_top: str, a_bot: str | None):
    hits = pg.search_for(a_top)
    if not hits:
        return None
    r = hits[0]
    W, H = pg.rect.width, pg.rect.height
    if mode == "below":
        return fitz.Rect(28, r.y0 - 4, W - 28, H - 34)
    if mode == "above":
        # top=52 clears the JIM running header (verified on page renders)
        return fitz.Rect(28, 52, W - 28, r.y1 + 5)
    # between
    assert a_bot is not None
    hits_b = pg.search_for(a_bot)
    if not hits_b:
        return None
    rb = hits_b[0]
    bottom = rb.y1 + 6 if a_bot.startswith(("Source", "Need")) else rb.y0 - 6
    return fitz.Rect(28, r.y0 - 4, W - 28, bottom)


def main(render_pages: bool = False) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    docs: dict[Path, fitz.Document] = {}
    for name, pdf, idx, mode, a_top, a_bot in FIG_SPECS:
        if pdf not in docs:
            docs[pdf] = fitz.open(str(pdf))
        pg = docs[pdf][idx]
        if render_pages:
            pg.get_pixmap(matrix=MAT).save(str(OUT / f"PAGE_{name}.png"))
            print(f"rendered page for {name}")
            continue
        clip = clip_for(pg, mode, a_top, a_bot)
        if clip is None:
            print(f"!! anchor not found: {name}")
            continue
        pg.get_pixmap(matrix=MAT, clip=clip).save(str(OUT / f"{name}.png"))
        print(f"cropped {name}: {clip}")


if __name__ == "__main__":
    main(render_pages="--render-pages" in sys.argv)
