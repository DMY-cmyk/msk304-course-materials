# Pertemuan 2-7 Visuals Addition Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 33 cropped TPGS-ebook images (19 Figures + 14 Concepts & Connections sidebars) and 11 native Word tables across Pertemuan 2 through 7 in `RMK Pra UTS.docx`, distributed at the natural §X.N sub-section where each visual belongs.

**Architecture:** A 3-layer Python script package. (1) A single PDF extractor renders all 33 PNGs at 300 DPI into per-Pertemuan subdirectories. (2) A shared helpers module exports anchor-resolution and insertion utilities. (3) Six per-Pertemuan content modules each declare their `IMAGES` and `TABLES` placement specs; a master driver imports a Pertemuan module by `--pertemuan N` and inserts everything for that one Pertemuan, idempotently. Per-Pertemuan tasks are independent — a bug in Pertemuan 5 does not block Pertemuan 2-4 commits.

**Tech Stack:** Python 3.12, `python-docx`, `PyMuPDF` (`fitz`), Pillow.

**Spec:** `docs/superpowers/specs/2026-05-22-msk304-pertemuan-2-7-visuals-design.md`

---

## File Structure

| Path | Role |
|---|---|
| `Dev Assistant/scripts/pert_2_7/__init__.py` | Marks the package. Empty. |
| `Dev Assistant/scripts/pert_2_7/helpers.py` | Shared `insert_image_after_anchor`, `insert_table_after_anchor`, `find_anchor_paragraph`, idempotency check. |
| `Dev Assistant/scripts/pert_2_7/pert2.py` | Pertemuan 2 `IMAGES` and `TABLES` content specs (Task 4). |
| `Dev Assistant/scripts/pert_2_7/pert3.py` | Pertemuan 3 content (Task 5). |
| `Dev Assistant/scripts/pert_2_7/pert4.py` | Pertemuan 4 content (Task 6). |
| `Dev Assistant/scripts/pert_2_7/pert5.py` | Pertemuan 5 content (Task 7). |
| `Dev Assistant/scripts/pert_2_7/pert6.py` | Pertemuan 6 content (Task 8). |
| `Dev Assistant/scripts/pert_2_7/pert7.py` | Pertemuan 7 content (Task 9). |
| `Dev Assistant/scripts/extract_pert_2_7_images.py` | Renders all 33 PNGs in one pass (Task 3). |
| `Dev Assistant/scripts/insert_pert_2_7_visuals.py` | Driver: takes `--pertemuan N`, imports `pert_2_7.pertN`, applies its IMAGES + TABLES (Task 2). |
| `Dev Assistant/scripts/verify_pert_2_7.py` | Final acceptance verification (Task 10). |
| `images/pertemuan-2/…` through `pertemuan-7/…` | 33 PNG outputs total. |
| `RMK Pra UTS.PRE-PERT-2-7.docx` | Pre-task-1 backup. |
| `RMK Pra UTS.docx` | Target — modified six times, once per Pertemuan task. |

---

## Task 1: Setup, Backup, and Scaffold

**Files:**
- Create: `Dev Assistant/scripts/pert_2_7/__init__.py` (empty)
- Create: 8 placeholder script files (one-line comments each)
- Create: 6 image directories
- Create: `RMK Pra UTS.PRE-PERT-2-7.docx` (binary copy)

- [ ] **Step 1: Create the backup**

Run:
```powershell
Copy-Item "RMK Pra UTS.docx" "RMK Pra UTS.PRE-PERT-2-7.docx"
```

Verify hashes match:
```powershell
(Get-FileHash "RMK Pra UTS.docx").Hash -eq (Get-FileHash "RMK Pra UTS.PRE-PERT-2-7.docx").Hash
```
Expected: `True`.

- [ ] **Step 2: Create the 6 image output directories**

```powershell
2..7 | ForEach-Object { New-Item -ItemType Directory -Force "images/pertemuan-$_" }
```

- [ ] **Step 3: Create the package directory and 8 placeholder files**

```powershell
New-Item -ItemType Directory -Force "Dev Assistant/scripts/pert_2_7"
```

Create these files, each with the single comment line shown:

`Dev Assistant/scripts/pert_2_7/__init__.py`:
```python
```
(empty file)

`Dev Assistant/scripts/pert_2_7/helpers.py`:
```python
# Shared helpers for Pertemuan 2-7 visual insertion (Task 2)
```

`Dev Assistant/scripts/pert_2_7/pert2.py`:
```python
# Pertemuan 2 content (Task 4)
```

`Dev Assistant/scripts/pert_2_7/pert3.py`:
```python
# Pertemuan 3 content (Task 5)
```

`Dev Assistant/scripts/pert_2_7/pert4.py`:
```python
# Pertemuan 4 content (Task 6)
```

`Dev Assistant/scripts/pert_2_7/pert5.py`:
```python
# Pertemuan 5 content (Task 7)
```

`Dev Assistant/scripts/pert_2_7/pert6.py`:
```python
# Pertemuan 6 content (Task 8)
```

`Dev Assistant/scripts/pert_2_7/pert7.py`:
```python
# Pertemuan 7 content (Task 9)
```

`Dev Assistant/scripts/extract_pert_2_7_images.py`:
```python
# 33-image extractor for Pertemuan 2-7 (Task 3)
```

`Dev Assistant/scripts/insert_pert_2_7_visuals.py`:
```python
# Per-Pertemuan visuals inserter driver (Task 2)
```

`Dev Assistant/scripts/verify_pert_2_7.py`:
```python
# Acceptance verifier (Task 10)
```

- [ ] **Step 4: Commit**

```bash
git add "Dev Assistant/scripts/pert_2_7/" "Dev Assistant/scripts/extract_pert_2_7_images.py" "Dev Assistant/scripts/insert_pert_2_7_visuals.py" "Dev Assistant/scripts/verify_pert_2_7.py" "RMK Pra UTS.PRE-PERT-2-7.docx" "images/pertemuan-2/" "images/pertemuan-3/" "images/pertemuan-4/" "images/pertemuan-5/" "images/pertemuan-6/" "images/pertemuan-7/"
git commit -m "chore(pert2-7): scaffold scripts, image dirs, and backup"
```

(If `git add` complains about empty directories, that's OK — directories will be filled in later tasks. Skip empty-dir args if needed.)

---

## Task 2: Helpers + Driver

**Files:**
- Modify: `Dev Assistant/scripts/pert_2_7/helpers.py`
- Modify: `Dev Assistant/scripts/insert_pert_2_7_visuals.py`

- [ ] **Step 1: Write helpers.py**

Replace contents of `Dev Assistant/scripts/pert_2_7/helpers.py` with:

```python
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
```

- [ ] **Step 2: Write the driver script**

Replace contents of `Dev Assistant/scripts/insert_pert_2_7_visuals.py` with:

```python
"""Per-Pertemuan visuals inserter driver.

Usage:
    python "Dev Assistant/scripts/insert_pert_2_7_visuals.py" --pertemuan N

Imports the corresponding pert_2_7.pertN module, applies its IMAGES and
TABLES to RMK Pra UTS.docx, saves in place. Idempotent — caption text
match skips already-inserted entries.
"""
from __future__ import annotations
import argparse
import importlib
import sys
from pathlib import Path
from docx import Document

# Allow importing from the pert_2_7 package
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from pert_2_7.helpers import apply_pertemuan  # noqa: E402

ROOT = SCRIPT_DIR.parents[1]
DOCX = ROOT / "RMK Pra UTS.docx"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pertemuan", "-p", type=int, required=True,
                    choices=[2, 3, 4, 5, 6, 7])
    args = ap.parse_args()

    if not DOCX.exists():
        print(f"docx not found: {DOCX}", file=sys.stderr)
        return 1

    img_dir = ROOT / "images" / f"pertemuan-{args.pertemuan}"
    if not img_dir.exists():
        print(f"image dir not found: {img_dir}", file=sys.stderr)
        return 2

    module_name = f"pert_2_7.pert{args.pertemuan}"
    try:
        mod = importlib.import_module(module_name)
    except ImportError as e:
        print(f"could not import {module_name}: {e}", file=sys.stderr)
        return 3

    images = getattr(mod, "IMAGES", [])
    tables = getattr(mod, "TABLES", [])

    doc = Document(DOCX)
    n_img, n_tbl, n_skip = apply_pertemuan(doc, images, tables, img_dir)
    doc.save(DOCX)

    print(f"Pertemuan {args.pertemuan}: inserted {n_img} images, "
          f"{n_tbl} tables, skipped {n_skip} already-present entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Smoke test — driver should fail cleanly with no content module yet**

Run:
```powershell
python "Dev Assistant/scripts/insert_pert_2_7_visuals.py" --pertemuan 2
```

Expected:
```
Pertemuan 2: inserted 0 images, 0 tables, skipped 0 already-present entries
```
Return code: 0 (since pert2.py is still a placeholder with no IMAGES or TABLES).

- [ ] **Step 4: Commit**

```bash
git add "Dev Assistant/scripts/pert_2_7/helpers.py" "Dev Assistant/scripts/insert_pert_2_7_visuals.py"
git commit -m "feat(pert2-7): shared helpers and per-Pertemuan driver"
```

---

## Task 3: Image Extractor (all 33 images)

**Files:**
- Modify: `Dev Assistant/scripts/extract_pert_2_7_images.py`
- Output: 33 PNG files across `images/pertemuan-2..7/`

- [ ] **Step 1: Inspect each target page's block layout to determine bbox**

For each of the 33 target labels below, the engineer needs to verify and potentially refine the explicit crop rect by running the following on the source PDF:

```python
python -c "
import sys; sys.stdout.reconfigure(encoding='utf-8')
import fitz
doc = fitz.open('Ebook/(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf')
# replace PNO with the 0-indexed page
PNO = 54  # for page 55
p = doc[PNO]
print('page rect:', p.rect)
for b in p.get_text('dict')['blocks']:
    typ = 'TXT' if b.get('type')==0 else 'IMG'
    bb = b['bbox']
    if typ == 'TXT':
        t = ''.join(s['text'] for ln in b.get('lines',[]) for s in ln.get('spans',[]))[:80]
    else:
        t = '(image)'
    print(f'  {typ} ({bb[0]:.1f},{bb[1]:.1f})-({bb[2]:.1f},{bb[3]:.1f}) | {t}')
"
```

For each target, take the union bounding box of the figure/sidebar's blocks (including its label and any image-type blocks) and add a 12pt margin.

- [ ] **Step 2: Write the extractor**

Replace contents of `Dev Assistant/scripts/extract_pert_2_7_images.py` with:

```python
"""Extract 33 cropped images for Pertemuan 2-7 from TPGS Ch.2/3/4/5/6/8.

Renders at 300 DPI. Each target may specify an explicit crop rect; if
None, the heuristic falls back to a wider-than-default page-width
extraction starting from the label block.
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
PAGE_TEXT_FRAME = (45.0, 540.0)  # nominal (x0, x1) for a typical TPGS body text frame

# Each target: (pdf_pg_0idx, subdir_pertN, out_filename, crop_or_None,
#              fallback_marker_for_heuristic)
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


def render(page, rect, out: Path) -> tuple[int, int]:
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
    ok = 0
    for pno, subdir, fname, crop, marker in TARGETS:
        page = doc[pno]
        rect = fitz.Rect(*crop) & page.rect
        out = out_root / subdir / fname
        w, h = render(page, rect, out)
        print(f"wrote {out.relative_to(ROOT)} ({w}x{h} px)")
        ok += 1
    print(f"\\nTotal: {ok}/{len(TARGETS)} images written")
    return 0 if ok == len(TARGETS) else 4


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Run the extractor**

```powershell
python "Dev Assistant/scripts/extract_pert_2_7_images.py"
```

Expected: 33 `wrote ...` lines, ending with `Total: 33/33 images written`.

- [ ] **Step 4: Sanity-check image dimensions**

```powershell
python -c "from pathlib import Path; from PIL import Image; ps=sorted(Path('images').glob('pertemuan-*/*.png')); [print(p.relative_to('images'), Image.open(p).size, p.stat().st_size) for p in ps]"
```

Expected: 33 lines. Every image width should be > 1500 px. Every file size > 50 KB.

**If any image is suspiciously small (<50 KB or <1500 px wide):**
1. Open the corresponding PDF page using the inspector from Step 1.
2. Look at the actual block layout to identify a better crop rect.
3. Edit the `TARGETS` entry's `crop` tuple with corrected coordinates.
4. Re-run the extractor.

- [ ] **Step 5: Visual spot-check (load 6 images, one per Pertemuan)**

Open the following 6 images one at a time and verify they show complete content with no clipping:
- `images/pertemuan-2/fig_2_1.png`
- `images/pertemuan-3/fig_3_2.png`
- `images/pertemuan-4/fig_4_2.png`
- `images/pertemuan-5/fig_5_1.png`
- `images/pertemuan-6/fig_6_1.png`
- `images/pertemuan-7/fig_8_3.png`

If any look clipped or wrong, refine the crop rect in `TARGETS` and re-render.

- [ ] **Step 6: Commit**

```bash
git add "Dev Assistant/scripts/extract_pert_2_7_images.py" "images/pertemuan-2/" "images/pertemuan-3/" "images/pertemuan-4/" "images/pertemuan-5/" "images/pertemuan-6/" "images/pertemuan-7/"
git commit -m "feat(pert2-7): extract 33 cropped images from TPGS Ch.2-8 at 300 DPI"
```

---

## Task 4: Pertemuan 2 Content + Insertion

**Files:**
- Modify: `Dev Assistant/scripts/pert_2_7/pert2.py`
- Modify (when run): `RMK Pra UTS.docx`

**What this task does:** Define IMAGES and TABLES specs for Pertemuan 2 (6 images + 4 tables), run the driver, verify, commit.

- [ ] **Step 1: Read TPGS Ch.2 source tables from the PDF**

Run the inspector for each of Tables 2.1, 2.2, 2.3, 2.4 to extract their text content:

```python
python -c "
import sys; sys.stdout.reconfigure(encoding='utf-8')
import fitz
doc = fitz.open('Ebook/(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf')
for pno in [54, 56, 56, 63]:  # pp 55, 57, 57, 64 (1-indexed)
    p = doc[pno]
    print(f'=== PG {pno+1} ===')
    for b in p.get_text('dict')['blocks']:
        if b.get('type') != 0: continue
        bb = b['bbox']
        t = ''.join(s['text'] for ln in b.get('lines',[]) for s in ln.get('spans',[]))
        if t.strip(): print(f'  y={bb[1]:.0f} | {t.strip()[:200]}')
"
```

Use the output to transcribe each table's headers and rows. Sub-bullets in TPGS tables become individual cells in the Word table.

- [ ] **Step 2: Write the pert2 content module**

Replace contents of `Dev Assistant/scripts/pert_2_7/pert2.py` with the content specification below. The anchor prefixes match exact text from the existing document. IMAGES list is finalized; TABLES content must be filled in based on the Step 1 inspection.

```python
"""Pertemuan 2 visual-insertion content spec.

IMAGES: each (anchor_text_prefix, img_filename, caption)
TABLES: each (anchor_text_prefix, caption, rows_list_of_tuples)
"""

CIT_FIG = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 2"
CIT_TAB = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 2"

IMAGES = [
    ("§2.2 Lima Tahap Proses Manajemen Strategis",
     "fig_2_1.png",
     f"Gambar 2.1 — Proses Perumusan dan Eksekusi Strategi (Lima Tahap). "
     f"{CIT_FIG}, hlm. 14 (Figure 2.1)."),

    ("Pengembangan Visi Strategis, Misi, dan Nilai Inti",
     "cc_2_1.png",
     f"Gambar 2.2 — Contoh-Contoh Pernyataan Visi Strategis. "
     f"{CIT_FIG}, hlm. 17 (Concepts & Connections 2.1)."),

    ("Pengembangan Visi Strategis, Misi, dan Nilai Inti",
     "cc_2_2.png",
     f"Gambar 2.3 — TOMS Shoes: Model Bisnis Berbasis Misi. "
     f"{CIT_FIG}, hlm. 20 (Concepts & Connections 2.2)."),

    ("Penetapan Tujuan (Setting Objectives)",
     "cc_2_3.png",
     f"Gambar 2.4 — Contoh-Contoh Tujuan Perusahaan. "
     f"{CIT_FIG}, hlm. 23 (Concepts & Connections 2.3)."),

    ("Perumusan Strategi (Crafting Strategy)",
     "fig_2_2.png",
     f"Gambar 2.5 — Hirarki Pembuatan Strategi Perusahaan. "
     f"{CIT_FIG}, hlm. 26 (Figure 2.2)."),

    ("§2.3 Corporate Governance dalam Proses Strategis",
     "cc_2_4.png",
     f"Gambar 2.6 — Kegagalan Tata Kelola Perusahaan di Volkswagen. "
     f"{CIT_FIG}, hlm. 30 (Concepts & Connections 2.4)."),
]

TABLES = [
    # Table 2.1 — Factors Shaping Decisions in Strategy Process
    ("§2.2 Lima Tahap Proses Manajemen Strategis",
     f"Tabel 2.1 — Faktor-Faktor yang Membentuk Keputusan dalam Proses Perumusan "
     f"dan Eksekusi Strategi. {CIT_TAB}, hlm. 14 (Table 2.1).",
     [
         ("External Considerations", "Internal Considerations"),
         ("Does sticking with the company's present strategic course present "
          "attractive opportunities for growth and profitability?",
          "Does the company have an appealing customer value proposition?"),
         ("What kind of competitive forces are industry members facing, and are "
          "they acting to enhance or weaken the company's prospects for growth "
          "and profitability?",
          "What are the company's competitively important resources and "
          "capabilities, and are they potent enough to produce a sustainable "
          "competitive advantage?"),
         ("What factors are driving industry change, and what impact will they "
          "have on the company's competitive position?",
          "Does the company have sufficient business and competitive strength "
          "to seize market opportunities and nullify external threats?"),
         ("How are industry rivals positioned, and what strategic moves are "
          "they likely to make next?",
          "Are the company's costs competitive with those of key rivals?"),
         ("What are the key factors of future competitive success, and does the "
          "industry offer good prospects for attractive profits for companies "
          "possessing those capabilities?",
          "Is the company competitively stronger or weaker than its key rivals?"),
     ]),

    # Table 2.2 — Characteristics of Effectively Worded Vision Statements
    ("Pengembangan Visi Strategis, Misi, dan Nilai Inti",
     f"Tabel 2.2 — Karakteristik Pernyataan Visi yang Efektif. "
     f"{CIT_TAB}, hlm. 16 (Table 2.2).",
     [
         ("Characteristic", "Description"),
         ("Graphic",
          "Paints a picture of the kind of company that management is trying "
          "to create and the market position(s) the company is striving to "
          "stake out."),
         ("Directional",
          "Is forward-looking; describes the strategic course that management "
          "has charted and the kinds of product-market-customer-technology "
          "changes that will help the company prepare for the future."),
         ("Focused",
          "Is specific enough to provide managers with guidance in making "
          "decisions and allocating resources."),
         ("Flexible",
          "Is not so focused that it makes it difficult for management to "
          "adjust to changing circumstances in markets, customer preferences, "
          "or technology."),
         ("Feasible",
          "Is within the realm of what the company can reasonably expect to "
          "achieve."),
         ("Desirable",
          "Indicates why the directional path makes good business sense."),
         ("Easy to communicate",
          "Is explainable in 5 to 10 minutes and, ideally, can be reduced to "
          "a simple, memorable slogan."),
     ]),

    # Table 2.3 — Common Shortcomings in Company Vision Statements
    ("Pengembangan Visi Strategis, Misi, dan Nilai Inti",
     f"Tabel 2.3 — Kekurangan yang Sering Muncul dalam Pernyataan Visi "
     f"Perusahaan. {CIT_TAB}, hlm. 17 (Table 2.3).",
     [
         ("Shortcoming", "Why It Matters"),
         ("Vague or incomplete",
          "Short on specifics about where the company is headed or what kind "
          "of company management is trying to create."),
         ("Not forward-looking",
          "Doesn't indicate whether or how management intends to alter the "
          "company's current product-market-customer-technology focus."),
         ("Too broad",
          "So all-inclusive that the company could head in almost any "
          "direction, pursue almost any opportunity, or enter almost any "
          "business."),
         ("Bland or uninspiring",
          "Lacks the power to motivate company personnel or inspire "
          "shareholder confidence about the company's direction."),
         ("Not distinctive",
          "Provides no unique company identity; could apply to companies in "
          "any of several industries (or at least several rivals operating "
          "in the same industry or market arena)."),
         ("Too reliant on superlatives",
          "Doesn't say anything specific about the company's strategic course "
          "beyond the pursuit of such lofty accolades as best, most "
          "successful, recognized leader, global or worldwide leader, or "
          "first choice of customers."),
     ]),

    # Table 2.4 — Types of Objectives
    ("Penetapan Tujuan (Setting Objectives)",
     f"Tabel 2.4 — Jenis Tujuan: Tujuan Finansial dan Tujuan Strategis. "
     f"{CIT_TAB}, hlm. 22 (Table 2.4).",
     [
         ("Financial Objectives", "Strategic Objectives"),
         ("An x percent increase in annual revenues",
          "Winning an x percent market share"),
         ("Annual increases in after-tax profits of x percent",
          "Achieving lower overall costs than rivals"),
         ("Annual increases in earnings per share of x percent",
          "Overtaking key competitors on product performance or quality or "
          "customer service"),
         ("Annual dividend increases of x percent",
          "Deriving x percent of revenues from the sale of new products "
          "introduced within the past five years"),
         ("Profit margins of x percent",
          "Having broader or deeper technological capabilities than rivals"),
         ("An x percent return on capital employed (ROCE) or return on "
          "shareholders' equity (ROE)",
          "Having a wider product line than rivals"),
         ("Increased shareholder value in the form of an upward-trending "
          "stock price",
          "Having a better-known or more powerful brand name than rivals"),
         ("Bond and credit ratings of x",
          "Having stronger national or global sales and distribution "
          "capabilities than rivals"),
         ("Internal cash flows of x dollars to fund new capital investment",
          "Consistently getting new or improved products to market ahead of "
          "rivals"),
     ]),
]
```

- [ ] **Step 3: Run the driver for Pertemuan 2**

```powershell
python "Dev Assistant/scripts/insert_pert_2_7_visuals.py" --pertemuan 2
```

Expected stdout:
```
Pertemuan 2: inserted 6 images, 4 tables, skipped 0 already-present entries
```
Return code: 0.

- [ ] **Step 4: Idempotency check — re-run**

```powershell
python "Dev Assistant/scripts/insert_pert_2_7_visuals.py" --pertemuan 2
```

Expected:
```
Pertemuan 2: inserted 0 images, 0 tables, skipped 10 already-present entries
```

If anything other than "skipped 10" appears, STOP. Restore from `RMK Pra UTS.PRE-PERT-2-7.docx` and debug the idempotency check.

- [ ] **Step 5: Structural verification**

```powershell
python -c "from docx import Document; d=Document('RMK Pra UTS.docx'); print('inline images:', len(d.inline_shapes)); print('tables:', len(d.tables)); print('captions starting with Gambar 2.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Gambar 2.'))); print('captions starting with Tabel 2.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Tabel 2.')))"
```

Expected:
- `inline images: 9` (was 3, added 6)
- `tables: 8` (was 4, added 4)
- `captions starting with Gambar 2.: 6`
- `captions starting with Tabel 2.: 4`

- [ ] **Step 6: Commit**

```bash
git add "Dev Assistant/scripts/pert_2_7/pert2.py" "RMK Pra UTS.docx"
git commit -m "feat(pert2): insert 6 images + 4 tables in Pertemuan 2"
```

---

## Task 5: Pertemuan 3 Content + Insertion

**Files:**
- Modify: `Dev Assistant/scripts/pert_2_7/pert3.py`
- Modify (when run): `RMK Pra UTS.docx`

**What this task does:** 7 Figures + 1 C&C = 8 images, plus 3 tables, into Pertemuan 3.

- [ ] **Step 1: Inspect Tables 3.1, 3.2, 3.3 in the PDF**

```python
python -c "
import sys; sys.stdout.reconfigure(encoding='utf-8')
import fitz
doc = fitz.open('Ebook/(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf')
for pno in [78, 92, 98]:
    p = doc[pno]
    print(f'=== PG {pno+1} ===')
    for b in p.get_text('dict')['blocks']:
        if b.get('type') != 0: continue
        bb = b['bbox']
        t = ''.join(s['text'] for ln in b.get('lines',[]) for s in ln.get('spans',[]))
        if t.strip(): print(f'  y={bb[1]:.0f} | {t.strip()[:200]}')
"
```

- [ ] **Step 2: Write pert3.py content module**

Replace `Dev Assistant/scripts/pert_2_7/pert3.py` with:

```python
"""Pertemuan 3 visual-insertion content spec."""

CIT_FIG = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 3"
CIT_TAB = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 3"

IMAGES = [
    ("§3.2 Q1 — Analisis Makro-Lingkungan (PESTEL)",
     "fig_3_1.png",
     f"Gambar 3.1 — Lingkungan Makro Perusahaan dalam Kerangka PESTEL. "
     f"{CIT_FIG}, hlm. 38 (Figure 3.1)."),

    ("§3.3 Q2 — Lima Kekuatan Kompetitif Porter",
     "fig_3_2.png",
     f"Gambar 3.2 — Model Lima Kekuatan Persaingan Porter. "
     f"{CIT_FIG}, hlm. 40 (Figure 3.2)."),

    ("§3.3 Q2 — Lima Kekuatan Kompetitif Porter",
     "fig_3_3.png",
     f"Gambar 3.3 — Faktor-Faktor yang Memengaruhi Daya Tawar Pembeli. "
     f"{CIT_FIG}, hlm. 42 (Figure 3.3)."),

    ("§3.3 Q2 — Lima Kekuatan Kompetitif Porter",
     "fig_3_4.png",
     f"Gambar 3.4 — Faktor-Faktor yang Memengaruhi Tekanan Persaingan dari "
     f"Produk Substitusi. {CIT_FIG}, hlm. 44 (Figure 3.4)."),

    ("§3.3 Q2 — Lima Kekuatan Kompetitif Porter",
     "fig_3_5.png",
     f"Gambar 3.5 — Faktor-Faktor yang Memengaruhi Daya Tawar Pemasok. "
     f"{CIT_FIG}, hlm. 46 (Figure 3.5)."),

    ("§3.3 Q2 — Lima Kekuatan Kompetitif Porter",
     "fig_3_6.png",
     f"Gambar 3.6 — Faktor-Faktor yang Memengaruhi Ancaman Pendatang Baru. "
     f"{CIT_FIG}, hlm. 48 (Figure 3.6)."),

    ("§3.3 Q2 — Lima Kekuatan Kompetitif Porter",
     "fig_3_7.png",
     f"Gambar 3.7 — Faktor-Faktor yang Memengaruhi Kekuatan Rivalitas "
     f"Kompetitif. {CIT_FIG}, hlm. 49 (Figure 3.7)."),

    ("§3.8 Q7 — Evaluasi Daya Tarik Industri",
     "cc_3_1.png",
     f"Gambar 3.8 — Contoh Analisis Industri. "
     f"{CIT_FIG}, hlm. 56 (Concepts & Connections 3.1)."),
]

TABLES = [
    # Table 3.1 — Six PESTEL Components
    ("§3.2 Q1 — Analisis Makro-Lingkungan (PESTEL)",
     f"Tabel 3.1 — Enam Komponen Lingkungan Makro dalam Analisis PESTEL. "
     f"{CIT_TAB}, hlm. 39 (Table 3.1).",
     [
         ("Component", "Description"),
         ("Political factors",
          "Political policies and processes, including the extent to which a "
          "government intervenes in the economy. They include such matters as "
          "tax policy, fiscal policy, tariffs, the political climate, and the "
          "strength of institutions such as the federal banking system."),
         ("Economic conditions",
          "The general economic climate and specific factors such as interest "
          "rates, exchange rates, the inflation rate, the unemployment rate, "
          "the rate of economic growth, trade deficits or surpluses, savings "
          "rates, and per-capita domestic product. Economic factors also "
          "include conditions in the markets for stocks and bonds."),
         ("Sociocultural forces",
          "The societal values, attitudes, cultural factors, and lifestyles "
          "that impact business, as well as demographic factors such as the "
          "population size, growth rate, and age distribution. Sociocultural "
          "forces vary by locale and change over time."),
         ("Technological factors",
          "The pace of technological change and technological developments "
          "that have the potential for wide-ranging effects on society, such "
          "as genetic engineering, nanotechnology, and 3D printing."),
         ("Environmental forces",
          "Ecological and environmental forces including weather, climate, "
          "climate change, and associated factors like water shortages. These "
          "factors can directly impact industries such as insurance, "
          "agriculture, energy production, and tourism."),
         ("Legal and regulatory factors",
          "The regulations and laws that companies must comply with such as "
          "consumer laws, labor laws, antitrust laws, and occupational health "
          "and safety regulation."),
     ]),

    # Table 3.2 — Driving Forces
    ("§3.4 Q3 — Driving Forces Perubahan Industri",
     f"Tabel 3.2 — Kekuatan Pendorong yang Paling Umum dalam Perubahan Industri. "
     f"{CIT_TAB}, hlm. 53 (Table 3.2).",
     [
         ("Driving Force", "Examples / Impact"),
         ("Changes in the long-term industry growth rate",
          "Affects supply-demand balance, ease of entry, market saturation."),
         ("Increasing globalization",
          "Players race to build market position in foreign markets; companies "
          "must compete globally to remain viable."),
         ("Emerging new internet capabilities and applications",
          "Internet of Things, cloud computing, mobile commerce reshape "
          "competitive dynamics."),
         ("Shifts in who buys the products and how the products are used",
          "Demographic changes alter end-uses, distribution channels, and "
          "marketing approaches."),
         ("Product innovation",
          "New products attract new buyers, expand market boundaries, alter "
          "rivalry intensity."),
         ("Marketing innovation",
          "New media channels, branding, and pricing models alter cost "
          "structure and customer reach."),
         ("Entry or exit of major firms",
          "Major M&A, divestiture, or new entrants reshape competitive "
          "position and strategic group structure."),
         ("Diffusion of technical know-how across firms and countries",
          "Erodes proprietary advantages; raises competition among "
          "previously specialized firms."),
         ("Changes in cost and efficiency",
          "Reshapes competitive position when learning curves, scale "
          "economies, or input prices change significantly."),
         ("Reductions in uncertainty and business risk",
          "More firms enter the industry once early uncertainty is resolved."),
         ("Regulatory influences and government policy changes",
          "Deregulation, new safety/environmental laws, trade policy shifts."),
         ("Changing societal concerns, attitudes, and lifestyles",
          "Health, sustainability, social-justice concerns drive demand "
          "shifts and force strategic adjustments."),
     ]),

    # Table 3.3 — Key Success Factors
    ("§3.7 Q6 — Faktor Kunci Keberhasilan",
     f"Tabel 3.3 — Jenis-Jenis Faktor Kunci Keberhasilan (Key Success Factors). "
     f"{CIT_TAB}, hlm. 59 (Table 3.3).",
     [
         ("Category", "Examples"),
         ("Technology-related",
          "Expertise in particular technology or scientific research; "
          "proven ability to improve production processes."),
         ("Manufacturing-related",
          "Low-cost production efficiency; high quality of manufacture; high "
          "use of capacity; ability to manufacture or assemble products that "
          "are customized to buyer specifications."),
         ("Distribution-related",
          "Strong network of wholesale distributors/dealers; strong direct "
          "sales capability; low distribution costs; fast delivery."),
         ("Marketing-related",
          "Breadth of product line and product selection; well-known and "
          "well-respected brand name; courteous, personalized customer "
          "service; accurate filling of buyer orders."),
         ("Skills- and capability-related",
          "Talented workforce; clever advertising; proven expertise in a "
          "particular technology; superior information systems."),
         ("Other types",
          "Favorable image/reputation with buyers; overall low costs; "
          "convenient locations; pleasant and courteous employees; access to "
          "financial capital; patent protection."),
     ]),
]
```

- [ ] **Step 3: Run driver**

```powershell
python "Dev Assistant/scripts/insert_pert_2_7_visuals.py" --pertemuan 3
```

Expected: `Pertemuan 3: inserted 8 images, 3 tables, skipped 0 already-present entries`.

- [ ] **Step 4: Verify**

```powershell
python -c "from docx import Document; d=Document('RMK Pra UTS.docx'); print('inline images:', len(d.inline_shapes)); print('tables:', len(d.tables)); print('captions Gambar 3.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Gambar 3.'))); print('captions Tabel 3.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Tabel 3.')))"
```

Expected:
- inline images: 17 (9 + 8 new)
- tables: 11 (8 + 3 new)
- Gambar 3.: 8
- Tabel 3.: 3

- [ ] **Step 5: Commit**

```bash
git add "Dev Assistant/scripts/pert_2_7/pert3.py" "RMK Pra UTS.docx"
git commit -m "feat(pert3): insert 8 images + 3 tables in Pertemuan 3"
```

---

## Task 6: Pertemuan 4 Content + Insertion

**Files:**
- Modify: `Dev Assistant/scripts/pert_2_7/pert4.py`

**Plan:** 2 Figures + 1 C&C = 3 images, plus 2 tables (Table 4.2 SWOT, Table 4.3 competitive strength).

- [ ] **Step 1: Inspect Tables 4.2 and 4.3 in PDF (pages 111 and 120)**

```python
python -c "
import sys; sys.stdout.reconfigure(encoding='utf-8')
import fitz
doc = fitz.open('Ebook/(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf')
for pno in [110, 119]:
    p = doc[pno]
    print(f'=== PG {pno+1} ===')
    for b in p.get_text('dict')['blocks']:
        if b.get('type') != 0: continue
        bb = b['bbox']
        t = ''.join(s['text'] for ln in b.get('lines',[]) for s in ln.get('spans',[]))
        if t.strip(): print(f'  y={bb[1]:.0f} | {t.strip()[:200]}')
"
```

- [ ] **Step 2: Write pert4.py**

Replace `Dev Assistant/scripts/pert_2_7/pert4.py` with:

```python
"""Pertemuan 4 visual-insertion content spec."""

CIT_FIG = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 4"
CIT_TAB = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 4"

IMAGES = [
    ("§4.3 Q2 — Sumber Daya, Kapabilitas, dan Uji VRIN",
     "fig_4_1.png",
     f"Gambar 4.1 — Identifikasi Sumber Daya dan Kapabilitas Perusahaan. "
     f"{CIT_FIG}, hlm. 72 (Figure 4.1)."),

    ("§4.3 Q2 — Sumber Daya, Kapabilitas, dan Uji VRIN",
     "cc_4_1.png",
     f"Gambar 4.2 — Contoh Identifikasi Sumber Daya dan Kapabilitas pada "
     f"Perusahaan. {CIT_FIG}, hlm. 73 (Concepts & Connections 4.1)."),

    ("§4.5 Q3 — Daya Saing Struktur Biaya & Proposisi Nilai Pelanggan",
     "fig_4_2.png",
     f"Gambar 4.3 — Rantai Nilai Representatif untuk Sebuah Industri. "
     f"{CIT_FIG}, hlm. 75 (Figure 4.2)."),
]

TABLES = [
    # Table 4.2 — SWOT Factors
    ("§4.4 Analisis SWOT",
     f"Tabel 4.1 — Faktor-Faktor yang Perlu Dipertimbangkan dalam Mengidentifikasi "
     f"Kekuatan, Kelemahan, Peluang, dan Ancaman Perusahaan. "
     f"{CIT_TAB}, hlm. 70 (Table 4.2).",
     [
         ("Potential Internal Strengths & Competitive Capabilities",
          "Potential Internal Weaknesses & Competitive Deficiencies"),
         ("Core competencies in key areas",
          "No clear strategic direction"),
         ("A strong financial condition; ample financial resources to grow "
          "the business",
          "No well-developed or proven core competencies"),
         ("Strong brand-name image / company reputation",
          "A weak balance sheet; burdened with too much debt"),
         ("Economies of scale and/or learning and experience-curve advantages "
          "over rivals",
          "Higher overall unit costs relative to those of key competitors"),
         ("Other cost advantages over rivals (proprietary technology, "
          "input-cost advantages, capacity utilization)",
          "Missing some key skills or competencies; lack of management "
          "depth"),
         ("Attractive customer base",
          "Subpar profitability"),
         ("Technology / innovation skills; important patents",
          "Plagued with internal operating problems or obsolete facilities"),
         ("Product innovation capabilities",
          "Too narrow a product line relative to rivals"),
         ("Proven capabilities in improving production processes",
          "Weak brand image or reputation"),
         ("Good supply chain management capabilities",
          "Weaker dealer network than key rivals"),
         ("Good customer service capabilities",
          "Behind on product quality, R&D, and/or technological know-how"),
         ("Better product quality relative to rivals",
          "In the wrong strategic group"),
         ("Wide geographic coverage and/or strong global distribution",
          "Losing market share because…"),
         ("Alliances/joint ventures that provide access to valuable "
          "technology / competencies / attractive geographic markets",
          "Lack the financial resources to fund promising strategic "
          "initiatives"),
         ("Potential Market Opportunities",
          "Potential External Threats to Future Profitability"),
         ("Meeting demand of fast-growing market segments",
          "Increasing intensity of competition among industry rivals — may "
          "squeeze profit margins"),
         ("Expanding the company's product line to meet a broader range of "
          "customer needs",
          "Slowdowns in market growth"),
         ("Using existing skills/know-how to enter new product lines or new "
          "businesses",
          "Likely entry of potent new competitors"),
         ("Online sales / e-commerce growth",
          "Loss of sales to substitute products"),
         ("Integrating forward or backward",
          "Growing bargaining power of customers or suppliers"),
         ("Falling trade barriers in attractive foreign markets",
          "A shift in buyer needs / tastes away from industry's product"),
         ("Acquiring rival firms or companies with attractive technological "
          "expertise / capabilities",
          "Adverse demographic changes that threaten to curtail demand"),
         ("Entering into alliances or joint ventures to expand the firm's "
          "market coverage or boost its competitive capability",
          "Adverse economic conditions / recession"),
         ("Openings to exploit emerging new technologies",
          "Costly new regulatory requirements"),
         ("Openings to extend the company's brand name or reputation to new "
          "geographic areas",
          "Tightening credit conditions / rising borrowing costs"),
     ]),

    # Table 4.3 — Competitive Strength Assessment
    ("§4.6 Q4 — Competitive Strength Assessment",
     f"Tabel 4.2 — Penilaian Kekuatan Kompetitif Tertimbang Sederhana. "
     f"{CIT_TAB}, hlm. 80 (Table 4.3).",
     [
         ("Key Success Factor / Strength Measure", "Weight",
          "ABC Co. Rating / Score", "Rival 1 Rating / Score",
          "Rival 2 Rating / Score"),
         ("Quality / product performance", "0.10",
          "8 / 0.80", "5 / 0.50", "1 / 0.10"),
         ("Reputation / image", "0.10",
          "8 / 0.80", "7 / 0.70", "1 / 0.10"),
         ("Manufacturing capability", "0.10",
          "2 / 0.20", "10 / 1.00", "5 / 0.50"),
         ("Technological skills", "0.05",
          "10 / 0.50", "1 / 0.05", "3 / 0.15"),
         ("Dealer network / distribution capability", "0.05",
          "9 / 0.45", "4 / 0.20", "5 / 0.25"),
         ("New-product innovation capability", "0.05",
          "9 / 0.45", "4 / 0.20", "5 / 0.25"),
         ("Financial resources", "0.10",
          "5 / 0.50", "10 / 1.00", "3 / 0.30"),
         ("Relative cost position", "0.30",
          "5 / 1.50", "10 / 3.00", "1 / 0.30"),
         ("Customer service capabilities", "0.15",
          "5 / 0.75", "7 / 1.05", "1 / 0.15"),
         ("Sum of weights", "1.00", "", "", ""),
         ("Overall weighted competitive strength rating", "",
          "5.95", "7.70", "2.10"),
     ]),
]
```

- [ ] **Step 3: Run driver**

```powershell
python "Dev Assistant/scripts/insert_pert_2_7_visuals.py" --pertemuan 4
```

Expected: `Pertemuan 4: inserted 3 images, 2 tables, skipped 0 already-present entries`.

- [ ] **Step 4: Verify**

```powershell
python -c "from docx import Document; d=Document('RMK Pra UTS.docx'); print('inline images:', len(d.inline_shapes)); print('tables:', len(d.tables)); print('captions Gambar 4.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Gambar 4.'))); print('captions Tabel 4.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Tabel 4.')))"
```

Expected:
- inline images: 20 (17 + 3 new)
- tables: 13 (11 + 2 new)
- Gambar 4.: 3
- Tabel 4.: 2

- [ ] **Step 5: Commit**

```bash
git add "Dev Assistant/scripts/pert_2_7/pert4.py" "RMK Pra UTS.docx"
git commit -m "feat(pert4): insert 3 images + 2 tables in Pertemuan 4"
```

---

## Task 7: Pertemuan 5 Content + Insertion

**Files:**
- Modify: `Dev Assistant/scripts/pert_2_7/pert5.py`

**Plan:** 3 Figures + 4 C&C = 7 images. No tables (TPGS Ch.5 has none).

- [ ] **Step 1: Write pert5.py**

Replace `Dev Assistant/scripts/pert_2_7/pert5.py` with:

```python
"""Pertemuan 5 visual-insertion content spec."""

CIT_FIG = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 5"

IMAGES = [
    ("§5.1 Pengantar & Dua Faktor Diferensiator",
     "fig_5_1.png",
     f"Gambar 5.1 — Lima Strategi Kompetitif Generik. "
     f"{CIT_FIG}, hlm. 88 (Figure 5.1)."),

    ("§5.2 Strategi 1 — Low-Cost Provider",
     "fig_5_2.png",
     f"Gambar 5.2 — Driver Biaya Penting dalam Rantai Nilai Perusahaan. "
     f"{CIT_FIG}, hlm. 90 (Figure 5.2)."),

    ("§5.2 Strategi 1 — Low-Cost Provider",
     "cc_5_1.png",
     f"Gambar 5.3 — Vanguard: Strategi Penyedia Berbiaya Rendah dalam "
     f"Industri Reksa Dana. {CIT_FIG}, hlm. 92 (Concepts & Connections 5.1)."),

    ("§5.3 Strategi 2 — Broad Differentiation",
     "fig_5_3.png",
     f"Gambar 5.4 — Driver Nilai Penting yang Menciptakan Keunggulan "
     f"Diferensiasi. {CIT_FIG}, hlm. 95 (Figure 5.3)."),

    ("§5.3 Strategi 2 — Broad Differentiation",
     "cc_5_2.png",
     f"Gambar 5.5 — Contoh Strategi Diferensiasi pada Industri Restoran. "
     f"{CIT_FIG}, hlm. 101 (Concepts & Connections 5.2)."),

    ("§5.3 Strategi 2 — Broad Differentiation",
     "cc_5_3.png",
     f"Gambar 5.6 — Strategi Diferensiasi dan Posisi Kompetitif. "
     f"{CIT_FIG}, hlm. 102 (Concepts & Connections 5.3)."),

    ("§5.5 Strategi 4 — Best-Cost Provider",
     "cc_5_4.png",
     f"Gambar 5.7 — American Giant: Penerapan Prinsip-Prinsip Strategi "
     f"Best-Cost Provider. {CIT_FIG}, hlm. 104 (Concepts & Connections 5.4)."),
]

TABLES = []
```

- [ ] **Step 2: Run driver**

```powershell
python "Dev Assistant/scripts/insert_pert_2_7_visuals.py" --pertemuan 5
```

Expected: `Pertemuan 5: inserted 7 images, 0 tables, skipped 0 already-present entries`.

- [ ] **Step 3: Verify**

```powershell
python -c "from docx import Document; d=Document('RMK Pra UTS.docx'); print('inline images:', len(d.inline_shapes)); print('captions Gambar 5.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Gambar 5.')))"
```

Expected:
- inline images: 27 (20 + 7 new)
- Gambar 5.: 7

- [ ] **Step 4: Commit**

```bash
git add "Dev Assistant/scripts/pert_2_7/pert5.py" "RMK Pra UTS.docx"
git commit -m "feat(pert5): insert 7 images in Pertemuan 5"
```

---

## Task 8: Pertemuan 6 Content + Insertion

**Files:**
- Modify: `Dev Assistant/scripts/pert_2_7/pert6.py`

**Plan:** 1 Figure + 3 C&C = 4 images. No tables.

- [ ] **Step 1: Write pert6.py**

Replace `Dev Assistant/scripts/pert_2_7/pert6.py` with:

```python
"""Pertemuan 6 visual-insertion content spec."""

CIT_FIG = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 6"

IMAGES = [
    ("§6.2 Strategi Ofensif untuk Meningkatkan Posisi Pasar",
     "fig_6_1.png",
     f"Gambar 6.1 — Jenis-Jenis Manuver Strategi Ofensif. "
     f"{CIT_FIG}, hlm. 110 (Figure 6.1)."),

    ("§6.2 Strategi Ofensif untuk Meningkatkan Posisi Pasar",
     "cc_6_1.png",
     f"Gambar 6.2 — Contoh Strategi Blue Ocean. "
     f"{CIT_FIG}, hlm. 114 (Concepts & Connections 6.1)."),

    ("§6.5 Ruang Lingkup Operasi (Scope of the Firm)",
     "cc_6_2.png",
     f"Gambar 6.3 — Walmart: Penerapan Strategi Akuisisi Horizontal. "
     f"{CIT_FIG}, hlm. 120 (Concepts & Connections 6.2)."),

    ("§6.5 Ruang Lingkup Operasi (Scope of the Firm)",
     "cc_6_3.png",
     f"Gambar 6.4 — Contoh Aliansi Strategis dalam Industri Otomotif Global. "
     f"{CIT_FIG}, hlm. 124 (Concepts & Connections 6.3)."),
]

TABLES = []
```

- [ ] **Step 2: Run driver**

```powershell
python "Dev Assistant/scripts/insert_pert_2_7_visuals.py" --pertemuan 6
```

Expected: `Pertemuan 6: inserted 4 images, 0 tables, skipped 0 already-present entries`.

- [ ] **Step 3: Verify**

```powershell
python -c "from docx import Document; d=Document('RMK Pra UTS.docx'); print('inline images:', len(d.inline_shapes)); print('captions Gambar 6.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Gambar 6.')))"
```

Expected:
- inline images: 31 (27 + 4 new)
- Gambar 6.: 4

- [ ] **Step 4: Commit**

```bash
git add "Dev Assistant/scripts/pert_2_7/pert6.py" "RMK Pra UTS.docx"
git commit -m "feat(pert6): insert 4 images in Pertemuan 6"
```

---

## Task 9: Pertemuan 7 Content + Insertion

**Files:**
- Modify: `Dev Assistant/scripts/pert_2_7/pert7.py`

**Plan:** 4 Figures + 1 C&C = 5 images, plus 2 tables (Tables 8.1, 8.2).

- [ ] **Step 1: Inspect Tables 8.1 and 8.2 in PDF (pages 203, 206)**

```python
python -c "
import sys; sys.stdout.reconfigure(encoding='utf-8')
import fitz
doc = fitz.open('Ebook/(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf')
for pno in [202, 205]:
    p = doc[pno]
    print(f'=== PG {pno+1} ===')
    for b in p.get_text('dict')['blocks']:
        if b.get('type') != 0: continue
        bb = b['bbox']
        t = ''.join(s['text'] for ln in b.get('lines',[]) for s in ln.get('spans',[]))
        if t.strip(): print(f'  y={bb[1]:.0f} | {t.strip()[:200]}')
"
```

- [ ] **Step 2: Write pert7.py**

Replace `Dev Assistant/scripts/pert_2_7/pert7.py` with:

```python
"""Pertemuan 7 visual-insertion content spec."""

CIT_FIG = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 8"
CIT_TAB = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 8"

IMAGES = [
    ("§7.1 Pengantar — Dari Single-Business ke Multibusiness",
     "fig_8_1.png",
     f"Gambar 7.1 — Tujuan Membangun Perusahaan Multibisnis Melalui "
     f"Diversifikasi. {CIT_FIG}, hlm. 154 (Figure 8.1)."),

    ("§7.1 Pengantar — Dari Single-Business ke Multibusiness",
     "fig_8_2.png",
     f"Gambar 7.2 — Tiga Tes untuk Menilai Daya Tarik Langkah Diversifikasi. "
     f"{CIT_FIG}, hlm. 155 (Figure 8.2)."),

    ("§7.4 Mode Masuk Diversifikasi",
     "cc_8_1.png",
     f"Gambar 7.3 — Merger Kraft Foods dengan H. J. Heinz: Studi Kasus "
     f"Akuisisi Diversifikasi. {CIT_FIG}, hlm. 158 (Concepts & Connections 8.1)."),

    ("§7.6 Mengevaluasi Strategi Perusahaan Terdiversifikasi (Six-Step Procedure)",
     "fig_8_3.png",
     f"Gambar 7.4 — Matriks Sembilan-Sel: Daya Tarik Industri vs Kekuatan "
     f"Kompetitif. {CIT_FIG}, hlm. 166 (Figure 8.3)."),

    ("§7.7 Empat Pilihan Strategis Pasca-Evaluasi",
     "fig_8_4.png",
     f"Gambar 7.5 — Pilihan Strategis dan Finansial Utama untuk Mengalokasikan "
     f"Sumber Daya Keuangan Perusahaan Terdiversifikasi. "
     f"{CIT_FIG}, hlm. 170 (Figure 8.4)."),
]

TABLES = [
    # Table 8.1 — Industry Attractiveness Weighted Scores
    ("§7.6 Mengevaluasi Strategi Perusahaan Terdiversifikasi (Six-Step Procedure)",
     f"Tabel 7.1 — Perhitungan Skor Daya Tarik Industri yang Tertimbang. "
     f"{CIT_TAB}, hlm. 162 (Table 8.1).",
     [
         ("Industry Attractiveness Measure", "Importance / Weight",
          "Industry A Rating / Score", "Industry B Rating / Score",
          "Industry C Rating / Score", "Industry D Rating / Score"),
         ("Market size and projected growth rate", "0.10",
          "8 / 0.80", "5 / 0.50", "2 / 0.20", "3 / 0.30"),
         ("Intensity of competition", "0.25",
          "8 / 2.00", "7 / 1.75", "3 / 0.75", "2 / 0.50"),
         ("Emerging opportunities and threats", "0.10",
          "2 / 0.20", "9 / 0.90", "4 / 0.40", "5 / 0.50"),
         ("Cross-industry strategic fit", "0.20",
          "8 / 1.60", "4 / 0.80", "8 / 1.60", "2 / 0.40"),
         ("Resource requirements", "0.10",
          "5 / 0.50", "8 / 0.80", "2 / 0.20", "6 / 0.60"),
         ("Seasonal and cyclical influences", "0.05",
          "8 / 0.40", "5 / 0.25", "10 / 0.50", "5 / 0.25"),
         ("Social, political, regulatory, and environmental factors", "0.05",
          "7 / 0.35", "7 / 0.35", "7 / 0.35", "7 / 0.35"),
         ("Industry profitability", "0.10",
          "5 / 0.50", "10 / 1.00", "3 / 0.30", "3 / 0.30"),
         ("Industry uncertainty and business risk", "0.05",
          "5 / 0.25", "7 / 0.35", "10 / 0.50", "1 / 0.05"),
         ("Sum of importance weights", "1.00", "", "", "", ""),
         ("Weighted overall industry attractiveness scores", "",
          "6.60", "6.70", "4.80", "3.25"),
     ]),

    # Table 8.2 — Competitive Strength Assessment for Diversified Businesses
    ("§7.6 Mengevaluasi Strategi Perusahaan Terdiversifikasi (Six-Step Procedure)",
     f"Tabel 7.2 — Penilaian Kekuatan Kompetitif untuk Bisnis-Bisnis dalam "
     f"Perusahaan Terdiversifikasi. {CIT_TAB}, hlm. 164 (Table 8.2).",
     [
         ("Competitive Strength Measure", "Importance / Weight",
          "Business A Rating / Score", "Business B Rating / Score",
          "Business C Rating / Score", "Business D Rating / Score"),
         ("Relative market share", "0.15",
          "10 / 1.50", "1 / 0.15", "6 / 0.90", "2 / 0.30"),
         ("Costs relative to competitors' costs", "0.20",
          "7 / 1.40", "2 / 0.40", "5 / 1.00", "3 / 0.60"),
         ("Ability to match or beat rivals on key product attributes", "0.05",
          "9 / 0.45", "4 / 0.20", "8 / 0.40", "4 / 0.20"),
         ("Brand image and reputation", "0.10",
          "9 / 0.90", "2 / 0.20", "7 / 0.70", "5 / 0.50"),
         ("Other competitively valuable capabilities", "0.15",
          "7 / 1.05", "2 / 0.30", "5 / 0.75", "3 / 0.45"),
         ("Benefits from strategic fit with sister businesses", "0.20",
          "8 / 1.60", "4 / 0.80", "8 / 1.60", "2 / 0.40"),
         ("Bargaining leverage with suppliers/buyers; access to alliances",
          "0.05", "9 / 0.45", "3 / 0.15", "7 / 0.35", "4 / 0.20"),
         ("Profitability relative to competitors", "0.10",
          "5 / 0.50", "1 / 0.10", "4 / 0.40", "4 / 0.40"),
         ("Sum of importance weights", "1.00", "", "", "", ""),
         ("Overall weighted competitive strength scores", "",
          "7.85", "2.30", "6.10", "3.05"),
     ]),
]
```

- [ ] **Step 3: Run driver**

```powershell
python "Dev Assistant/scripts/insert_pert_2_7_visuals.py" --pertemuan 7
```

Expected: `Pertemuan 7: inserted 5 images, 2 tables, skipped 0 already-present entries`.

- [ ] **Step 4: Verify**

```powershell
python -c "from docx import Document; d=Document('RMK Pra UTS.docx'); print('inline images:', len(d.inline_shapes)); print('tables:', len(d.tables)); print('captions Gambar 7.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Gambar 7.'))); print('captions Tabel 7.:', sum(1 for p in d.paragraphs if p.style.name=='Caption' and p.text.startswith('Tabel 7.')))"
```

Expected:
- inline images: 36 (31 + 5 new)
- tables: 15 (13 + 2 new)
- Gambar 7.: 5
- Tabel 7.: 2

- [ ] **Step 5: Commit**

```bash
git add "Dev Assistant/scripts/pert_2_7/pert7.py" "RMK Pra UTS.docx"
git commit -m "feat(pert7): insert 5 images + 2 tables in Pertemuan 7"
```

---

## Task 10: Final Acceptance Verification

**Files:**
- Modify: `Dev Assistant/scripts/verify_pert_2_7.py`

- [ ] **Step 1: Write the verifier**

Replace contents of `Dev Assistant/scripts/verify_pert_2_7.py` with:

```python
"""Final acceptance verification for Pertemuan 2-7 visuals addition.

Exits 0 on PASS. Exits 1 on any failure with descriptive message.
"""
from __future__ import annotations
import sys
from pathlib import Path
from docx import Document

ROOT = Path(__file__).resolve().parents[2]
DOCX = ROOT / "RMK Pra UTS.docx"

EXPECTED_GAMBAR_PER_PERT = {2: 6, 3: 8, 4: 3, 5: 7, 6: 4, 7: 5}
EXPECTED_TABEL_PER_PERT  = {2: 4, 3: 3, 4: 2, 5: 0, 6: 0, 7: 2}


def fail(msg: str) -> int:
    print(f"FAIL: {msg}", file=sys.stderr)
    return 1


def main() -> int:
    if not DOCX.exists():
        return fail(f"docx not found: {DOCX}")
    doc = Document(DOCX)

    n_imgs = len(doc.inline_shapes)
    if n_imgs < 36:
        return fail(f"expected >=36 inline images, got {n_imgs}")

    n_tables = len(doc.tables)
    if n_tables != 15:
        return fail(f"expected 15 tables, got {n_tables}")

    # Per-Pertemuan caption counts
    gambar_counts = {n: 0 for n in EXPECTED_GAMBAR_PER_PERT}
    tabel_counts  = {n: 0 for n in EXPECTED_TABEL_PER_PERT}
    for p in doc.paragraphs:
        if p.style.name != "Caption":
            continue
        t = p.text.strip()
        for n in gambar_counts:
            if t.startswith(f"Gambar {n}."):
                gambar_counts[n] += 1
        for n in tabel_counts:
            if t.startswith(f"Tabel {n}."):
                tabel_counts[n] += 1

    for n, expected in EXPECTED_GAMBAR_PER_PERT.items():
        got = gambar_counts[n]
        if got != expected:
            return fail(f"Pertemuan {n}: expected {expected} 'Gambar {n}.x' "
                        f"captions, got {got}")

    for n, expected in EXPECTED_TABEL_PER_PERT.items():
        got = tabel_counts[n]
        if got != expected:
            return fail(f"Pertemuan {n}: expected {expected} 'Tabel {n}.x' "
                        f"captions, got {got}")

    # Pertemuan 1 must still be intact
    pert1_imgs = sum(1 for p in doc.paragraphs
                     if p.style.name == "Caption" and p.text.startswith("Gambar 1."))
    if pert1_imgs != 3:
        return fail(f"Pertemuan 1 regression: expected 3 'Gambar 1.x' captions, "
                    f"got {pert1_imgs}")

    print(f"PASS — {n_imgs} inline images, {n_tables} tables.")
    print("Per-Pertemuan caption counts:")
    for n in sorted(EXPECTED_GAMBAR_PER_PERT):
        print(f"  Pertemuan {n}: {gambar_counts[n]} Gambar, "
              f"{tabel_counts[n]} Tabel")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Run the verifier**

```powershell
python "Dev Assistant/scripts/verify_pert_2_7.py"
```

Expected stdout:
```
PASS — 36 inline images, 15 tables.
Per-Pertemuan caption counts:
  Pertemuan 2: 6 Gambar, 4 Tabel
  Pertemuan 3: 8 Gambar, 3 Tabel
  Pertemuan 4: 3 Gambar, 2 Tabel
  Pertemuan 5: 7 Gambar, 0 Tabel
  Pertemuan 6: 4 Gambar, 0 Tabel
  Pertemuan 7: 5 Gambar, 2 Tabel
```

Return code: 0.

- [ ] **Step 3: Manual eye-check in Word**

Open `RMK Pra UTS.docx` in Microsoft Word. Spot-check:
- One image per Pertemuan renders at full 6" width without stretching
- One Word table per applicable Pertemuan has bold header row and Table Grid borders
- Captions read in Indonesian with correct citation
- No broken styles, no XML errors, no missing fonts warnings

If anything looks off, restore from `RMK Pra UTS.PRE-PERT-2-7.docx` and iterate on the specific failing Pertemuan.

- [ ] **Step 4: Commit**

```bash
git add "Dev Assistant/scripts/verify_pert_2_7.py"
git commit -m "test(pert2-7): final acceptance verification script"
```

---

## Done Criteria (matches Spec §7)

- [ ] Word opens the document without corruption warnings
- [ ] Inline image count = **36** (3 from Pertemuan 1 + 33 new)
- [ ] Native table count = **15** (4 existing + 11 new)
- [ ] All 6 per-Pertemuan caption counts match Task 10 expected values
- [ ] Pertemuan 1 has not regressed (still 3 `Gambar 1.x` captions, 2 `Tabel` captions)
- [ ] `verify_pert_2_7.py` exits 0 with PASS
- [ ] All commits in place: 1 scaffold + 1 helpers/driver + 1 extractor + 6 per-Pertemuan + 1 verifier = **10 commits** total
