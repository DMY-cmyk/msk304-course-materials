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
