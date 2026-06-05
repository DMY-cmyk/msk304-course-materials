"""Build Pert. 8 deliverables: markdown -> pandoc (reference.docx) -> final docx.

Post-processing (validated Pert. 2-7 practice; reference.docx alone is not enough):
  1. page geometry: A4 + 30/25/30/25 mm margins (reference ships degenerate pgSz)
  2. typography: Normal = Times New Roman 12pt, 1.5 line spacing, 1.25cm first-line
     indent; headings forced to Times New Roman (H1 14pt)
  3. image extents: pandoc emits NEGATIVE wp:extent values for PyMuPDF PNGs
     (DPI-metadata quirk) -> recompute from real pixel aspect at the spec width
"""
from __future__ import annotations

import io
import subprocess
from pathlib import Path

from docx import Document
from docx.shared import Cm, Inches, Mm, Pt
from PIL import Image

ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
CONTENT = ROOT / "Dev Assistant" / "content" / "pert8"
REFERENCE = ROOT / "Dev Assistant" / "scripts" / "reference.docx"
PANDOC = r"C:\Program Files\Pandoc\pandoc.exe"

JOBS = [
    (CONTENT / "rmk.md",
     ROOT / "RMK" / "01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx"),
    (CONTENT / "cr13.md",
     ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 13.docx"),
    (CONTENT / "cr14.md",
     ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 14.docx"),
]


def build(src: Path, dst: Path) -> None:
    cmd = [
        PANDOC, str(src), "-o", str(dst),
        "--reference-doc", str(REFERENCE),
        "--from", "markdown+implicit_figures",
        # image refs are written relative to content/ (e.g. ../temp/...), so the
        # search path must include content/ itself for `..` to land on Dev Assistant/
        "--resource-path", f"{CONTENT};{CONTENT.parent}",
    ]
    subprocess.run(cmd, check=True)
    fix_geometry(dst)
    print(f"built {dst.name} ({dst.stat().st_size:,} bytes)")


# desired render width (inches) per source image basename (spec, Phase 3.5)
IMG_WIDTHS = {
    "ch7_figure_7_1": 5.8, "ch7_figure_7_2": 5.8, "ch7_table_7_1": 5.8,
    "art13_figure_2": 4.5, "art13_figure_3": 5.8, "art13_table_3": 5.8,
    "art14_figure_1": 5.8, "art14_figure_2": 5.5, "art14_figure_3": 5.5,
    "art14_table_2": 5.8,
}
# map cropped-PNG pixel sizes -> widths, since pandoc renames media parts
_PX_TO_WIDTH: dict[tuple[int, int], float] = {}
_FIGDIR = Path(__file__).parent.parent / "temp" / "pert8_figures"
for _name, _w in IMG_WIDTHS.items():
    _p = _FIGDIR / f"{_name}.png"
    if _p.exists():
        _PX_TO_WIDTH[Image.open(_p).size] = _w


def fix_geometry(path: Path) -> None:
    d = Document(str(path))
    # 1. page geometry
    for sec in d.sections:
        sec.page_width = Mm(210)
        sec.page_height = Mm(297)
        sec.left_margin = Mm(30)
        sec.right_margin = Mm(25)
        sec.top_margin = Mm(30)
        sec.bottom_margin = Mm(25)
    # 2. typography (match accepted Pert. 7 standard)
    normal = d.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    normal.paragraph_format.line_spacing = 1.5
    normal.paragraph_format.first_line_indent = Cm(1.25)
    for sname, size in [("Heading 1", 14), ("Heading 2", 12), ("Heading 3", 12)]:
        try:
            st = d.styles[sname]
        except KeyError:
            continue
        st.font.name = "Times New Roman"
        st.font.size = Pt(size)
        if st.paragraph_format is not None:
            st.paragraph_format.first_line_indent = Cm(0)
    for sname in ("Image Caption", "Caption", "Captioned Figure", "CaptionedFigure"):
        try:
            st = d.styles[sname]
        except KeyError:
            continue
        st.font.name = "Times New Roman"
        st.font.size = Pt(11)
        if st.paragraph_format is not None:
            st.paragraph_format.first_line_indent = Cm(0)
    # 3. image extents (pandoc negative-extent bug)
    for sh in d.inline_shapes:
        rid = sh._inline.graphic.graphicData.pic.blipFill.blip.embed
        blob = d.part.related_parts[rid].blob
        px_w, px_h = Image.open(io.BytesIO(blob)).size
        width_in = _PX_TO_WIDTH.get((px_w, px_h), 5.8)
        sh.width = Inches(width_in)
        sh.height = Inches(width_in * px_h / px_w)
    d.save(str(path))


if __name__ == "__main__":
    for src, dst in JOBS:
        build(src, dst)
