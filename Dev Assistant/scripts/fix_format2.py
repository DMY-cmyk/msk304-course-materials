"""More aggressive justify fix.

(1) Inject <w:jc val="both"/> into the Body Text and First Paragraph
    STYLE definitions so even paragraphs without explicit jc inherit it.
(2) Set <w:jc val="both"/> on every paragraph that is not a heading or
    caption (regardless of style name).
(3) Re-apply grid borders on all tables for safety.
"""
from __future__ import annotations
import sys
from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[2]
DOCX = ROOT / "RMK Pra UTS.docx"


def ensure_pPr(element):
    pPr = element.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr")
        element.insert(0, pPr)
    return pPr


def set_pPr_justify(element) -> None:
    """Set w:jc val='both' inside the element's w:pPr (creating pPr if needed)."""
    pPr = ensure_pPr(element)
    jc = pPr.find(qn("w:jc"))
    if jc is None:
        jc = OxmlElement("w:jc")
        pPr.append(jc)
    jc.set(qn("w:val"), "both")


def set_style_default_justify(style) -> None:
    """Embed w:jc='both' into a paragraph style's pPr default."""
    el = style.element
    pPr = el.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr")
        # pPr must come before rPr if present
        rPr = el.find(qn("w:rPr"))
        if rPr is not None:
            rPr.addprevious(pPr)
        else:
            el.append(pPr)
    jc = pPr.find(qn("w:jc"))
    if jc is None:
        jc = OxmlElement("w:jc")
        pPr.append(jc)
    jc.set(qn("w:val"), "both")


BORDER_KINDS = ("top", "left", "bottom", "right", "insideH", "insideV")


def set_table_borders(table) -> None:
    tbl = table._element
    tblPr = tbl.find(qn("w:tblPr"))
    if tblPr is None:
        tblPr = OxmlElement("w:tblPr")
        tbl.insert(0, tblPr)
    existing = tblPr.find(qn("w:tblBorders"))
    if existing is not None:
        tblPr.remove(existing)
    borders = OxmlElement("w:tblBorders")
    for kind in BORDER_KINDS:
        b = OxmlElement(f"w:{kind}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "6")
        b.set(qn("w:space"), "0")
        b.set(qn("w:color"), "000000")
        borders.append(b)
    tblPr.append(borders)


def set_cell_borders(cell) -> None:
    tcPr = cell._tc.find(qn("w:tcPr"))
    if tcPr is None:
        tcPr = OxmlElement("w:tcPr")
        cell._tc.insert(0, tcPr)
    existing = tcPr.find(qn("w:tcBorders"))
    if existing is not None:
        tcPr.remove(existing)
    tcBorders = OxmlElement("w:tcBorders")
    for kind in ("top", "left", "bottom", "right"):
        b = OxmlElement(f"w:{kind}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "6")
        b.set(qn("w:space"), "0")
        b.set(qn("w:color"), "000000")
        tcBorders.append(b)
    tcPr.append(tcBorders)


def main() -> int:
    if not DOCX.exists():
        print(f"docx not found: {DOCX}", file=sys.stderr)
        return 1
    doc = Document(DOCX)

    # 1. Style-level justify defaults for body styles
    for sname in ("Normal", "Body Text", "First Paragraph"):
        try:
            set_style_default_justify(doc.styles[sname])
            print(f"style default justify set: {sname}")
        except KeyError:
            print(f"style not found: {sname}")

    # 2. Direct paragraph-level justify on every non-heading, non-caption paragraph
    n = 0
    for p in doc.paragraphs:
        sn = p.style.name
        if sn.startswith("Heading"):
            continue
        if sn == "Caption":
            continue
        set_pPr_justify(p._element)
        n += 1

    # Also in table cells
    n_cells = 0
    for tbl in doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    sn = p.style.name
                    if sn.startswith("Heading") or sn == "Caption":
                        continue
                    set_pPr_justify(p._element)
                    n_cells += 1

    # 3. Borders on every table again
    n_tables = 0
    for tbl in doc.tables:
        try:
            tbl.style = "Table Grid"
        except KeyError:
            pass
        set_table_borders(tbl)
        for row in tbl.rows:
            for cell in row.cells:
                set_cell_borders(cell)
        n_tables += 1

    doc.save(DOCX)
    print(f"forced justify on {n} body paragraphs, {n_cells} cell paragraphs")
    print(f"re-applied borders on {n_tables} tables")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
