# RMK Pert. 8 + CR Artikel 13/14 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce three submission-ready Word documents for MST304 Temu 8 — a figure-rich RMK of TPGS (C&E 21e) Ch. 7 plus graduate critical reviews of Artikel 13 and Artikel 14 — passing the locked format/figure/concept gates.

**Architecture:** PyMuPDF crops the 10 source exhibits to PNG; three Markdown content files (single source of truth) are authored per the approved spec blueprints; Pandoc + `reference.docx` assembles each into a final .docx in the repo-convention folders; a verifier script asserts the Phase-5 gates and emits a validation report.

**Tech Stack:** Python 3.12, PyMuPDF 1.27, Pandoc 3.9 (`C:\Program Files\Pandoc\pandoc.exe`), python-docx (verification), reference template `Dev Assistant/scripts/reference.docx`.

**Authoritative content sources (already ingested, Phase 0):**
- `analysis/ch7-concept-inventory.md` + `analysis/ch7-text.txt` (chapter text, book p. = PDF p. − 43)
- `analysis/artikel13-brief.md` + `analysis/artikel13-text.txt`
- `analysis/artikel14-brief.md` + `analysis/artikel14-text.txt`
- Spec: `docs/superpowers/specs/2026-06-05-rmk-cr-pertemuan8-design.md`

**File structure:**

```
Dev Assistant/
├── scripts/
│   ├── extract_pert8_figures.py    # Task 1 — crops 10 exhibits → temp/pert8_figures/*.png
│   ├── build_pert8.py              # Task 5 — markdown → pandoc → 3 docx
│   └── verify_pert8.py             # Task 6 — format/figure/concept gates
├── content/pert8/
│   ├── rmk.md                      # Task 2 — RMK Pert. 8 (Bahasa Indonesia)
│   ├── cr13.md                     # Task 3 — Critical Review Artikel 13
│   └── cr14.md                     # Task 4 — Critical Review Artikel 14
└── temp/pert8_figures/             # cropped PNGs (gitignored ok; regenerated)
RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx                       # output
Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 13.docx
Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 14.docx
analysis/pert8-validation.md        # Task 6 output
```

---

### Task 1: Extract and visually verify the 10 source exhibits

**Files:**
- Create: `Dev Assistant/scripts/extract_pert8_figures.py`
- Output: `Dev Assistant/temp/pert8_figures/*.png` (10 files)

- [ ] **Step 1: Write the extraction script**

```python
"""Extract Pert. 8 exhibits: TPGS C&E 21e Ch.7 figures + Artikel 13/14 figures.

Two-pass workflow:
  pass 1 (--render-pages): render each target page full-size for visual bbox check
  pass 2 (default): crop per FIG_SPECS clip boxes -> PNG
Clip boxes are anchor-relative with manual overrides (validated Pert. 2-7 practice).
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

# (name, pdf_path, page_index_0based, anchor_text, mode, manual_clip_or_None)
# mode: 'below' = clip from anchor top to bottom margin (caption above figure)
#       'above' = clip from top margin to anchor bottom (caption below figure)
#       'manual' = use the supplied fitz.Rect verbatim
FIG_SPECS = [
    ("ch7_figure_7_1", TPGS, 224, "FIGURE 7.1", "below", None),
    ("ch7_figure_7_2", TPGS, 236, "FIGURE 7.2", "below", None),
    ("ch7_table_7_1",  TPGS, 239, "TABLE 7.1",  "above", None),
    ("art13_figure_2", ART13, 10, "Figure 2: Interconnection", "above", None),
    ("art13_figure_3", ART13, 11, "Figure 3: Relationship", "below", None),
    ("art13_table_3",  ART13, 14, "Table 3: Characteristics", "below", None),
    ("art14_figure_1", ART14, 2,  "Figure 1. Strategic Imperatives", "above", None),
    ("art14_figure_2", ART14, 4,  "Figure 2. Cisco", "above", None),
    ("art14_figure_3", ART14, 5,  "Figure 3. Case Study", "above", None),
    ("art14_table_2",  ART14, 6,  "Table 2. Research Questions", "below", None),
]

def clip_for(pg, anchor, mode, manual):
    if mode == "manual":
        return manual
    hits = pg.search_for(anchor)
    if not hits:
        return None
    r = hits[0]
    W, H = pg.rect.width, pg.rect.height
    if mode == "below":
        return fitz.Rect(28, r.y0 - 4, W - 28, H - 34)
    return fitz.Rect(28, 30, W - 28, r.y1 + 6)

def main(render_pages=False):
    OUT.mkdir(parents=True, exist_ok=True)
    docs = {}
    for name, pdf, idx, anchor, mode, manual in FIG_SPECS:
        if pdf not in docs:
            docs[pdf] = fitz.open(str(pdf))
        pg = docs[pdf][idx]
        if render_pages:
            pg.get_pixmap(matrix=MAT).save(str(OUT / f"PAGE_{name}.png"))
            print(f"rendered page for {name}")
            continue
        clip = clip_for(pg, anchor, mode, manual)
        if clip is None:
            print(f"!! anchor not found: {name}"); continue
        pg.get_pixmap(matrix=MAT, clip=clip).save(str(OUT / f"{name}.png"))
        print(f"cropped {name}: {clip}")

if __name__ == "__main__":
    main(render_pages="--render-pages" in sys.argv)
```

- [ ] **Step 2: Run pass 1 and inspect each page render**

Run: `python "Dev Assistant/scripts/extract_pert8_figures.py" --render-pages`
Then Read each `PAGE_*.png` to determine whether each caption sits above or below its figure and whether the default margins clip correctly.

- [ ] **Step 3: Adjust modes / set manual clips where needed; run pass 2**

Run: `python "Dev Assistant/scripts/extract_pert8_figures.py"`
Expected: 10 `*.png` crops written.

- [ ] **Step 4: Visually verify every crop**

Read all 10 PNGs; each must be legible, undistorted, fully bounded, with no neighboring body text. Iterate overrides until clean.

- [ ] **Step 5: Commit**

```bash
git add "Dev Assistant/scripts/extract_pert8_figures.py"
git commit -m "feat(pert8): exhibit extraction script (10 crops, two-pass verified)"
```

---

### Task 2: Author RMK content (`rmk.md`)

**Files:**
- Create: `Dev Assistant/content/pert8/rmk.md`

- [ ] **Step 1: Write the full RMK in academic Bahasa Indonesia** following spec blueprint §"RMK Pert. 8" exactly: 11 sections in chapter order; every concept from `analysis/ch7-concept-inventory.md` §1–§9 placed; ### sub-headings (2–5 per section); bold pivots; italic foreign terms; page citations *(TPGS 21e, 2018, hlm. X)*.

Document head (exact):

```markdown
# RESUME MATERI KULIAH (RMK) PERTEMUAN 8

**Strategi Bersaing di Pasar Internasional**
*(Strategies for Competing in International Markets — TPGS Chapter 7)*

**Nama: Dzaki Muhammad Yusfian**
**NIM: 01079**
**Mata Kuliah: Manajemen Strategik Kontemporer (MST304)**
**Program: Magister Akuntansi STIE YKPN Yogyakarta**
```

Figure embeds (exact syntax; Pandoc implicit_figures renders alt-text as caption):

```markdown
![Gambar 7.1. The Diamond of National Competitive Advantage (Sumber: TPGS 21e, 2018, hlm. 182)](../temp/pert8_figures/ch7_figure_7_1.png){width=5.8in}

![Gambar 7.2. Tiga Pendekatan Bersaing secara Internasional (Sumber: TPGS 21e, 2018, hlm. 194)](../temp/pert8_figures/ch7_figure_7_2.png){width=5.8in}

![Tabel 7.1. Keunggulan dan Kelemahan Strategi Multidomestik, Global, dan Transnasional (Sumber: TPGS 21e, 2018, hlm. 197)](../temp/pert8_figures/ch7_table_7_1.png){width=5.8in}
```

Each embed preceded by a 1-line transition and followed by 2–3 sentences of interpretation. Anchors: Gambar 7.1 in §2 (Diamond), Gambar 7.2 + Tabel 7.1 in §6 (three approaches). IC 7.1/7.2/7.3 narrated in prose in §5/§6/§10.

- [ ] **Step 2: Self-check against concept inventory** — walk §1–§9 of `analysis/ch7-concept-inventory.md`; confirm each bullet has a home; confirm the section ordering mirrors the chapter; confirm Key Points (hlm. 209–210) all covered.

- [ ] **Step 3: Commit**

```bash
git add "Dev Assistant/content/pert8/rmk.md"
git commit -m "feat(pert8): RMK content - 11 sections, 3 exhibits anchored, full Ch.7 coverage"
```

---

### Task 3: Author CR Artikel 13 content (`cr13.md`)

**Files:**
- Create: `Dev Assistant/content/pert8/cr13.md`

- [ ] **Step 1: Write the review** per spec blueprint §"CR Artikel 13": identity head (same block style as Task 2, title "CRITICAL REVIEW ARTIKEL 13"); sections: (1) Identitas Bibliografis & Tujuan; (2) Kerangka Teoretis & Metode; (3) Temuan Utama; (4) Penilaian Kritis; (5) Keterkaitan dengan TPGS Bab 7; (6) Implikasi & Penilaian Akhir. Embeds:

```markdown
![Gambar 1. Interkoneksi pasar — identitas F∩N=G (Sumber: Kostruba & Kostruba, 2025, hlm. 163)](../temp/pert8_figures/art13_figure_2.png){width=4.5in}

![Gambar 2. Komponen lingkungan pemasaran internasional (Sumber: Kostruba & Kostruba, 2025, hlm. 164)](../temp/pert8_figures/art13_figure_3.png){width=5.8in}

![Tabel 1. Tiga kelompok strategi internasionalisasi (Sumber: Kostruba & Kostruba, 2025, hlm. 167)](../temp/pert8_figures/art13_table_3.png){width=5.8in}
```

§4 must execute the spec's critique hooks (method opacity; F∩N=G incoherence; labeling slip; dated CPI; untested model; counterbalanced strengths). §5 must map: motives↔TPGS §1; Tables 3–4 ↔ five entry options; environment/Hofstede ↔ §2c/2e; inverted emerging-market perspective ↔ §7–8; Diamond as missing lens.

- [ ] **Step 2: Self-check against rubric** — all 6 sections present; appraisal genuinely evaluative; Ch.7 linkage explicit with TPGS page references.

- [ ] **Step 3: Commit**

```bash
git add "Dev Assistant/content/pert8/cr13.md"
git commit -m "feat(pert8): CR Artikel 13 - full rubric, 3 exhibits, Ch.7 linkage"
```

---

### Task 4: Author CR Artikel 14 content (`cr14.md`)

**Files:**
- Create: `Dev Assistant/content/pert8/cr14.md`

- [ ] **Step 1: Write the review** per spec blueprint §"CR Artikel 14"; same skeleton as Task 3 (title "CRITICAL REVIEW ARTIKEL 14"). **Own-words discipline:** no extended verbatim passages (≤1 short attributed quote); summarize panel insights analytically. Embeds:

```markdown
![Gambar 1. Imperatif Strategis dalam Kepemimpinan Pemasaran Global (Sumber: Gregory, Li & Solanki, 2026, hlm. 36)](../temp/pert8_figures/art14_figure_1.png){width=5.8in}

![Gambar 2. Alur Kerja Dukungan Pelanggan Berbasis AI Cisco (Sumber: Gregory, Li & Solanki, 2026, hlm. 38)](../temp/pert8_figures/art14_figure_2.png){width=5.5in}

![Gambar 3. Studi Kasus Kampanye IKEA Asia Tenggara (Sumber: Gregory, Li & Solanki, 2026, hlm. 39)](../temp/pert8_figures/art14_figure_3.png){width=5.5in}

![Tabel 1. Pertanyaan Riset dan Hipotesis (Sumber: Gregory, Li & Solanki, 2026, hlm. 40)](../temp/pert8_figures/art14_table_2.png){width=5.8in}
```

§4 critique hooks: n=3 single public panel; curated-narrative risk; unverified practitioner numbers; method-label stacking; Insight-Paper genre (H1–H16 generated not tested); counterbalanced strengths (currency, mechanism-level cases, triangulation, agenda value). §5 linkage: AI shifts the transnational frontier (Gambar 7.2/Tabel 7.1); mini-hatcheries ↔ concentrate-vs-disperse + coordination; capability transfer ↔ §5b; regulatory fragmentation ↔ §2c; platform localization ↔ §7; IKEA SEA ↔ Four Seasons parallel.

- [ ] **Step 2: Self-check** — rubric complete; verbatim-quote audit (≤1 short quote); Ch.7 linkage explicit.

- [ ] **Step 3: Commit**

```bash
git add "Dev Assistant/content/pert8/cr14.md"
git commit -m "feat(pert8): CR Artikel 14 - full rubric, 4 exhibits, AI-notice-compliant"
```

---

### Task 5: Build the three .docx

**Files:**
- Create: `Dev Assistant/scripts/build_pert8.py`
- Output: the 3 final .docx (paths in header)

- [ ] **Step 1: Write the build script**

```python
"""Build Pert. 8 deliverables: markdown -> pandoc (reference.docx) -> final docx."""
from __future__ import annotations
import subprocess
from pathlib import Path

ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
CONTENT = ROOT / "Dev Assistant" / "content" / "pert8"
REFERENCE = ROOT / "Dev Assistant" / "scripts" / "reference.docx"
PANDOC = r"C:\Program Files\Pandoc\pandoc.exe"

JOBS = [
    (CONTENT / "rmk.md",  ROOT / "RMK" / "01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx"),
    (CONTENT / "cr13.md", ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 13.docx"),
    (CONTENT / "cr14.md", ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 14.docx"),
]

def build(src: Path, dst: Path) -> None:
    cmd = [PANDOC, str(src), "-o", str(dst),
           "--reference-doc", str(REFERENCE),
           "--from", "markdown+implicit_figures",
           "--resource-path", str(CONTENT)]
    subprocess.run(cmd, check=True)
    print(f"built {dst.name} ({dst.stat().st_size:,} bytes)")

if __name__ == "__main__":
    for src, dst in JOBS:
        build(src, dst)
```

- [ ] **Step 2: Run the build**

Run: `python "Dev Assistant/scripts/build_pert8.py"`
Expected: three "built …" lines, no pandoc errors, sizes > 200 KB each (images embedded).

- [ ] **Step 3: Commit**

```bash
git add "Dev Assistant/scripts/build_pert8.py" "RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx" "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 13.docx" "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 14.docx"
git commit -m "feat(pert8): build three submission docx via pandoc + reference template"
```

---

### Task 6: Verify gates and emit validation report

**Files:**
- Create: `Dev Assistant/scripts/verify_pert8.py`
- Output: `analysis/pert8-validation.md`

- [ ] **Step 1: Write the verifier**

```python
"""Phase-5 gates for Pert. 8: format, figures, identity, concept coverage."""
from __future__ import annotations
from pathlib import Path
from docx import Document
from docx.shared import Mm

ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
DOCS = {
    "rmk":  ROOT / "RMK" / "01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx",
    "cr13": ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 13.docx",
    "cr14": ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 14.docx",
}
EXPECTED_IMAGES = {"rmk": 3, "cr13": 3, "cr14": 4}
# concept keyword gates per doc (lower-cased substring match on full text)
KEYWORDS = {
    "rmk": ["diamond", "multidomestik", "transnasional", "greenfield", "lisensi",
            "waralaba", "profit sanctuar", "subsidisasi", "dumping", "ctrip",
            "four seasons", "walgreens", "kurs", "brIC".lower(), "ekspor",
            "akuisisi", "joint venture", "wheel", "honeywell", "suzuki", "home depot"],
    "cr13": ["kostruba", "ukraina", "kopi", "jerman", "polandia", "hofstede",
             "f∩n", "internasionalisasi", "diaspora", "bab 7", "tpgs"],
    "cr14": ["gregory", "cmo", "generatif", "cisco", "ikea", "agilitas",
             "tata kelola", "transnasional", "bab 7", "tpgs", "panel"],
}
checks = []
def ok(label, cond):
    checks.append((label, bool(cond)))
    print(("PASS " if cond else "FAIL ") + label)

for key, path in DOCS.items():
    d = Document(str(path))
    sec = d.sections[0]
    ok(f"{key}: file exists", path.exists())
    ok(f"{key}: A4 width 210mm", abs(sec.page_width - Mm(210)) < Mm(2))
    ok(f"{key}: A4 height 297mm", abs(sec.page_height - Mm(297)) < Mm(2))
    full = "\n".join(p.text for p in d.paragraphs).lower()
    ok(f"{key}: identity NIM 01079", "01079" in full)
    ok(f"{key}: identity name", "dzaki muhammad yusfian" in full)
    n_img = len(d.inline_shapes)
    ok(f"{key}: embedded images == {EXPECTED_IMAGES[key]}", n_img == EXPECTED_IMAGES[key])
    missing = [k for k in KEYWORDS[key] if k not in full]
    ok(f"{key}: concept keywords (missing: {missing})", not missing)

n_fail = sum(1 for _, c in checks if not c)
report = ROOT / "analysis" / "pert8-validation.md"
lines = ["# Pert. 8 Validation Report\n"]
lines += [f"- {'✅' if c else '❌'} {label}" for label, c in checks]
lines.append(f"\n**Result: {len(checks)-n_fail}/{len(checks)} passed**")
report.write_text("\n".join(lines), encoding="utf-8")
print(f"\n{len(checks)-n_fail}/{len(checks)} passed -> {report}")
raise SystemExit(1 if n_fail else 0)
```

- [ ] **Step 2: Run verifier; fix failures; re-run until clean**

Run: `python "Dev Assistant/scripts/verify_pert8.py"`
Expected: all PASS, exit 0. (Note: font/spacing come from reference.docx styles — spot-check one doc manually in Word/LibreOffice for 12 pt TNR + 1.5 spacing.)

- [ ] **Step 3: Augment `analysis/pert8-validation.md`** with the concept→section table, figure checklist, and per-review rubric checklist (manual additions per spec §"Pipeline & verification").

- [ ] **Step 4: Commit**

```bash
git add "Dev Assistant/scripts/verify_pert8.py" analysis/pert8-validation.md
git commit -m "feat(pert8): gate verifier + validation report - all gates green"
```

---

## Self-review notes
- Spec coverage: Task 1 ↔ spec §Figure extraction; Tasks 2–4 ↔ §Document blueprints (content authority = Phase-0 analysis files, cited in header); Task 5 ↔ §Pipeline; Task 6 ↔ §Hard gates. Capsule narration covered in Task 2 anchors. AI-notice discipline in Task 4 Step 1.
- Image-count gate counts only embedded exhibits (3/3/4) — matches blueprints.
- Caption numbering: in CR docs the article's own figure numbers are renumbered sequentially per document (Gambar 1–3 / Tabel 1) with the source's identity stated in the caption — consistent with Pert. 2–7 practice.
```
