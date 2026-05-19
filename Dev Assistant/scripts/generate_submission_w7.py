"""Generate RMK Pertemuan 7 (Corporate Strategy: Diversification, Essentials
Ch.8, with embedded TPGS Ch.8 figures) plus Critical Review Artikel 11 and
Artikel 12.

Pipeline:
  1. Extract 4 figures (FIGURE 8.1-8.4) from TPGS Ch.8 via PyMuPDF.
  2. Build three Markdown content strings (RMK + CR11 + CR12).
  3. Run Pandoc per file with reference.docx -> DOCX outputs.

Source spec: docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import fitz  # PyMuPDF

# ============================================================================
# PATHS
# ============================================================================
SCRIPT_DIR   = Path(__file__).parent
PROJECT_ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
EBOOK        = PROJECT_ROOT / "Ebook" / (
    "(Business professional collection) John E. Gamble_ Arthur A. Thompson_ "
    "Margaret Ann Peteraf - Essentials of Strategic Management _ "
    "The Quest for Competitive Advantage (2021).pdf"
)
OUT_RMK      = PROJECT_ROOT / "RMK"
OUT_CR       = PROJECT_ROOT / "Critical Thinking of the Article"
TEMP         = PROJECT_ROOT / "Dev Assistant" / "temp"
FIGURES_DIR  = TEMP / "ch8_figures"
REFERENCE    = SCRIPT_DIR / "reference.docx"
PANDOC       = r"C:\Program Files\Pandoc\pandoc.exe"


# ============================================================================
# PHASE 1 - FIGURE EXTRACTION
# ============================================================================
def extract_figures(ebook_path: Path, figures_dir: Path) -> dict:
    """Extract TPGS Ch.8 figures 8.1-8.4."""
    figures_dir.mkdir(parents=True, exist_ok=True)
    mat = fitz.Matrix(2, 2)
    results: dict[str, Path] = {}

    fig_specs = [
        # name, anchor text, candidate page indices (confirmed in Task 1)
        ("figure_8_1", "FIGURE 8.1", [194]),
        ("figure_8_2", "FIGURE 8.2", [195]),
        ("figure_8_3", "FIGURE 8.3", [206]),
        ("figure_8_4", "FIGURE 8.4", [210]),
    ]

    with fitz.open(str(ebook_path)) as doc:
        for name, anchor, pg_indices in fig_specs:
            clipped = False
            for pg_idx in pg_indices:
                pg = doc[pg_idx]
                hits = pg.search_for(anchor)
                if hits:
                    r = hits[0]
                    clip = fitz.Rect(30, r.y0 - 5, pg.rect.width - 30, pg.rect.height - 30)
                    pix = pg.get_pixmap(matrix=mat, clip=clip)
                    out = figures_dir / f"{name}.png"
                    pix.save(str(out))
                    results[name] = out
                    clipped = True
                    print(f"  {name}: anchor on page index {pg_idx}")
                    break
            if not clipped:
                pg = doc[pg_indices[0]]
                pix = pg.get_pixmap(matrix=mat)
                out = figures_dir / f"{name}.png"
                pix.save(str(out))
                results[name] = out
                print(f"  {name}: WARNING anchor not found, fallback full page index {pg_indices[0]}")
    return results


def validate_figures(results: dict) -> None:
    """Confirm every PNG exists and is at least 10 KB."""
    for key in ("figure_8_1", "figure_8_2", "figure_8_3", "figure_8_4"):
        path = results.get(key)
        if not path or not path.exists():
            raise FileNotFoundError(f"Missing figure: {key}")
        size = path.stat().st_size
        if size < 10_000:
            raise ValueError(f"{key} too small: {size} bytes")
        print(f"  OK {key}: {size:,} bytes")


# ============================================================================
# PHASE 2 - MARKDOWN BUILDERS (stubs; replaced in Tasks 3-5)
# ============================================================================
def build_rmk(figures: dict) -> str:
    return "# RMK Pert. 7 placeholder\n\nPlaceholder body.\n"


def build_cr11() -> str:
    return "# CR Artikel 11 placeholder\n\nPlaceholder body.\n"


def build_cr12() -> str:
    return "# CR Artikel 12 placeholder\n\nPlaceholder body.\n"


# ============================================================================
# PHASE 3 - PANDOC
# ============================================================================
def pandoc(md: Path, out: Path) -> None:
    result = subprocess.run(
        [PANDOC, str(md), f"--reference-doc={REFERENCE}", "-o", str(out)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    print(f"Generated: {out.name}")


# ============================================================================
# MAIN
# ============================================================================
if __name__ == "__main__":
    TEMP.mkdir(parents=True, exist_ok=True)
    OUT_RMK.mkdir(parents=True, exist_ok=True)
    OUT_CR.mkdir(parents=True, exist_ok=True)
    if not REFERENCE.exists():
        raise FileNotFoundError(f"reference.docx not found at {REFERENCE}")

    print("Phase 1: Extracting TPGS Ch.8 figures...")
    figures = extract_figures(EBOOK, FIGURES_DIR)
    validate_figures(figures)

    print("Phase 2: Building markdown and running pandoc...")
    rmk_md  = build_rmk(figures)
    cr11_md = build_cr11()
    cr12_md = build_cr12()

    for name, content, out in [
        ("rmk_w7.md",  rmk_md,  OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 7.docx"),
        ("cr11.md",    cr11_md, OUT_CR  / "01079_Dzaki Muhammad Yusfian_Artikel 11.docx"),
        ("cr12.md",    cr12_md, OUT_CR  / "01079_Dzaki Muhammad Yusfian_Artikel 12.docx"),
    ]:
        md = TEMP / name
        md.write_text(content, encoding="utf-8")
        pandoc(md, out)
    print("All three documents generated successfully.")
    print(f"RMK : {OUT_RMK}")
    print(f"CR  : {OUT_CR}")
