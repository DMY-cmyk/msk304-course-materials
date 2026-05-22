"""Shared insertion helpers for Pertemuan 2-7 visual insertion.

Conventions:
- Every image is followed by a Caption-styled paragraph beginning "Gambar ".
- Every table is preceded by a Caption-styled paragraph beginning "Tabel ".
- An IMAGES entry is: (anchor_text_prefix, image_filename, caption_text)
- A TABLES entry is: (anchor_text_prefix, caption_text, rows_list_of_tuples)
  where rows_list_of_tuples[0] is the header row.
"""
from __future__ import annotations
from pathlib import Path
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


def find_anchor_paragraph(doc, prefix: str):
    """Return the first paragraph whose stripped text starts with `prefix`."""
    for p in doc.paragraphs:
        if p.text.strip().startswith(prefix):
            return p
    return None


def find_insertion_point(doc, anchor_prefix: str):
    """Walk forward from the anchor paragraph until the next H2 or H3 heading.

    Returns the paragraph immediately BEFORE that next heading. That's the
    paragraph at the end of the anchor's sub-section content. Visuals are
    inserted AFTER it (i.e., addnext on that paragraph's XML element).

    If no terminator heading found, returns the last paragraph in the doc.
    """
    anchor = find_anchor_paragraph(doc, anchor_prefix)
    if anchor is None:
        return None
    paras = doc.paragraphs
    idx = paras.index(anchor)
    last_in_section = anchor
    for p in paras[idx + 1:]:
        if p.style.name in ("Heading 1", "Heading 2", "Heading 3"):
            return last_in_section
        last_in_section = p
    return last_in_section


def caption_already_present(doc, caption_text: str) -> bool:
    """Return True if a Caption-styled paragraph with this exact text exists."""
    target = caption_text.strip()
    for p in doc.paragraphs:
        if p.style.name == "Caption" and p.text.strip() == target:
            return True
    return False


def insert_image_after(anchor_para, img_path: Path, caption: str, doc):
    """Insert centered image + caption paragraph immediately after anchor."""
    tmp_p = doc.add_paragraph()
    tmp_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    tmp_p.add_run().add_picture(str(img_path), width=Inches(6.0))
    tmp_p_el = tmp_p._element
    tmp_p_el.getparent().remove(tmp_p_el)
    anchor_para._element.addnext(tmp_p_el)

    cap_p = doc.add_paragraph(caption, style="Caption")
    cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap_p_el = cap_p._element
    cap_p_el.getparent().remove(cap_p_el)
    tmp_p_el.addnext(cap_p_el)
    return cap_p


def insert_table_after(anchor_para, caption: str, rows_data, doc):
    """Insert Caption paragraph then a Table Grid table immediately after anchor.

    rows_data[0] is the header row (bolded).
    Returns the Caption paragraph element.
    """
    cap_p = doc.add_paragraph(caption, style="Caption")
    cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap_p_el = cap_p._element
    cap_p_el.getparent().remove(cap_p_el)
    anchor_para._element.addnext(cap_p_el)

    n_cols = len(rows_data[0])
    n_rows = len(rows_data)
    tbl = doc.add_table(rows=n_rows, cols=n_cols)
    tbl.style = "Table Grid"
    for r_idx, row in enumerate(rows_data):
        for c_idx, cell_text in enumerate(row):
            cell = tbl.rows[r_idx].cells[c_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(str(cell_text))
            if r_idx == 0:
                run.bold = True
    tbl_el = tbl._element
    tbl_el.getparent().remove(tbl_el)
    cap_p_el.addnext(tbl_el)
    return cap_p


def apply_pertemuan(doc, images, tables, img_dir: Path):
    """Apply IMAGES and TABLES specs to a Pertemuan's sub-sections.

    For each entry:
    - Resolve insertion point (last paragraph of anchor's sub-section).
    - Idempotency: if caption text already present anywhere, skip.
    - Insert image+caption (or caption+table) after that insertion point.

    Returns (inserted_images, inserted_tables, skipped) tuple of counts.
    """
    n_img = n_tbl = n_skip = 0

    for anchor_prefix, img_filename, caption in images:
        if caption_already_present(doc, caption):
            n_skip += 1
            continue
        anchor = find_insertion_point(doc, anchor_prefix)
        if anchor is None:
            raise RuntimeError(
                f"anchor not found for image {img_filename!r}: {anchor_prefix!r}"
            )
        img_path = img_dir / img_filename
        if not img_path.exists():
            raise RuntimeError(f"image not found: {img_path}")
        insert_image_after(anchor, img_path, caption, doc)
        n_img += 1

    for anchor_prefix, caption, rows in tables:
        if caption_already_present(doc, caption):
            n_skip += 1
            continue
        anchor = find_insertion_point(doc, anchor_prefix)
        if anchor is None:
            raise RuntimeError(
                f"anchor not found for table caption {caption!r}: {anchor_prefix!r}"
            )
        insert_table_after(anchor, caption, rows, doc)
        n_tbl += 1

    return n_img, n_tbl, n_skip
