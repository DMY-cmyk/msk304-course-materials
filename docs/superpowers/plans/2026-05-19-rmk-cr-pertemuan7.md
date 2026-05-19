# RMK + CR Pertemuan 7 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate three Word documents (RMK Pert. 7 with embedded TPGS Ch.8 figures, CR Artikel 11 Hsieh & Chen 2011, CR Artikel 12 Okebaram & Onuoha 2018) with graduate-level analytical depth, Pert. 6 standard formatting, and an explicit *Strategic Fit / Contingency Theory* paradigmatic synthesis threading through all three.

**Architecture:** Python orchestrator (`generate_submission_w7.py`) extends the W6-enhanced pattern: PyMuPDF figure extraction from TPGS Ch.8, three Markdown content constants, pandoc invocation per file with `reference.docx`. Single-script run produces all three DOCX outputs.

**Tech Stack:** Python 3.12, PyMuPDF (`fitz`), python-docx (already installed), Pandoc (`C:\Program Files\Pandoc\pandoc.exe`).

**Reference documents:**
- Spec: `docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md`
- Prior pipeline (text-only): `Dev Assistant/scripts/generate_submission_w6.py`
- Prior pipeline (figure-enabled): `Dev Assistant/scripts/generate_rmk6_enhanced.py`
- Pandoc reference: `Dev Assistant/scripts/reference.docx`

---

### Task 1: Read primary sources and locate TPGS Ch.8

**Files (read-only):**
- `Article/Artikel 11.pdf` — Hsieh & Chen (2011)
- `Article/Artikel 12.pdf` — Okebaram & Onuoha (2018)
- `Ebook/(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf` — TPGS Ch.8

- [ ] **Step 1: Read Artikel 11.pdf in full**

Capture:
- Three components of the Strategic Fit triad (business strategy, HR strategy, reward system)
- Configurations proposed for each Porter generic strategy (cost leadership / differentiation / focus)
- Theoretical lineage citations (Porter 1985; Schuler & Jackson 1987; Gomez-Mejia & Balkin 1992; Miller 1986; Doty Glick & Huber 1993)
- Direct page references for at least 3 short quotations

- [ ] **Step 2: Read Artikel 12.pdf in full**

Capture:
- How sustainability is defined (triple bottom line — Elkington 1997)
- How organizational effectiveness is operationalized
- Proposed causal mechanism (fit → legitimacy → resources → effectiveness)
- Citations to Venkatraman 1989, Lawrence & Lorsch 1967, Hart 1995, Porter & Kramer 2006
- Page references for at least 3 short quotations
- Methodological disclosures (or lack thereof)

- [ ] **Step 3: Locate TPGS Ch.8 page indices in the PDF**

Run:
```python
import fitz
PDF = r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Ebook\(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf"
doc = fitz.open(PDF)
for i, page in enumerate(doc):
    text = page.get_text()
    if "CHAPTER 8" in text.upper() or "TAILORING STRATEGY" in text.upper():
        print(i, text[:200].replace("\n", " "))
doc.close()
```

Expected: a chapter-opening page index range (likely around index 200–230). Record:
- Chapter start page index (where "CHAPTER 8" title appears)
- Chapter end page index (where Ch.9 starts)
- Page indices for FIGURE 8.1, 8.2, 8.3, 8.4 (search via `page.search_for("FIGURE 8.")`)

Save the indices into a note for use in Task 3.

- [ ] **Step 4: Identify candidate figures**

For each FIGURE 8.X hit, capture:
- Reader page number printed in the PDF
- The figure title text
- Approximate vertical region (top of figure title, bottom of figure body)

Target 3–5 figures from this candidate pool:
- Industry life-cycle stages diagram
- Strategic options matrix for fragmented industries
- Turnaround / retrenchment decision flow
- Strategy-situation fit summary chart

---

### Task 2: Create `generate_submission_w7.py` — boilerplate + figure extraction

**Files:**
- Create: `Dev Assistant/scripts/generate_submission_w7.py`
- Reference (structure only): `Dev Assistant/scripts/generate_rmk6_enhanced.py`

- [ ] **Step 1: Write the file header, imports, and path constants**

```python
"""Generate RMK Pertemuan 7 (with embedded TPGS Ch.8 figures) plus
Critical Review Artikel 11 and Artikel 12.

Pipeline:
  1. Extract 3-5 figures from TPGS Ch.8 via PyMuPDF.
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
```

- [ ] **Step 2: Write the figure extraction function**

Use the page indices recorded in Task 1 Step 3. Update the `cc_specs` list with the actual figure anchors found.

```python
def extract_figures(ebook_path: Path, figures_dir: Path) -> dict:
    """Extract TPGS Ch.8 figures."""
    figures_dir.mkdir(parents=True, exist_ok=True)
    mat = fitz.Matrix(2, 2)
    results: dict[str, Path] = {}

    fig_specs = [
        # name, anchor text, candidate page indices (from Task 1 Step 3)
        ("figure_8_1", "FIGURE 8.1", [INDEX_FROM_TASK_1]),
        ("figure_8_2", "FIGURE 8.2", [INDEX_FROM_TASK_1]),
        ("figure_8_3", "FIGURE 8.3", [INDEX_FROM_TASK_1]),
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


def validate_figures(results: dict, expected_keys: list[str]) -> None:
    """Confirm every PNG exists and is at least 10 KB."""
    for key in expected_keys:
        path = results.get(key)
        if not path or not path.exists():
            raise FileNotFoundError(f"Missing figure: {key}")
        size = path.stat().st_size
        if size < 10_000:
            raise ValueError(f"{key} too small: {size} bytes")
        print(f"  OK {key}: {size:,} bytes")
```

Note: `INDEX_FROM_TASK_1` placeholders MUST be replaced with the actual integer page indices found in Task 1 Step 3 before the script can run.

- [ ] **Step 3: Write the pandoc helper and main entry stub**

```python
def pandoc(md: Path, out: Path) -> None:
    result = subprocess.run(
        [PANDOC, str(md), f"--reference-doc={REFERENCE}", "-o", str(out)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    print(f"Generated: {out.name}")


if __name__ == "__main__":
    TEMP.mkdir(parents=True, exist_ok=True)
    OUT_RMK.mkdir(parents=True, exist_ok=True)
    OUT_CR.mkdir(parents=True, exist_ok=True)
    if not REFERENCE.exists():
        raise FileNotFoundError(f"reference.docx not found at {REFERENCE}")

    print("Phase 1: Extracting TPGS Ch.8 figures...")
    figures = extract_figures(EBOOK, FIGURES_DIR)
    validate_figures(figures, list(figures.keys()))

    print("Phase 2: Building markdown and running pandoc...")
    for name, content, out in [
        ("rmk_w7.md",  RMK,  OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 7.docx"),
        ("cr11.md",    CR11, OUT_CR  / "01079_Dzaki Muhammad Yusfian_Artikel 11.docx"),
        ("cr12.md",    CR12, OUT_CR  / "01079_Dzaki Muhammad Yusfian_Artikel 12.docx"),
    ]:
        md = TEMP / name
        md.write_text(content, encoding="utf-8")
        pandoc(md, out)
    print("All three documents generated successfully.")
    print(f"RMK : {OUT_RMK}")
    print(f"CR  : {OUT_CR}")
```

- [ ] **Step 4: Smoke-test the boilerplate (with dummy content constants)**

Temporarily insert at top, just to verify the script runs:
```python
RMK = "# RMK Pert. 7 placeholder\n\nPlaceholder body.\n"
CR11 = "# CR Artikel 11 placeholder\n\nPlaceholder body.\n"
CR12 = "# CR Artikel 12 placeholder\n\nPlaceholder body.\n"
```

Run:
```powershell
python "Dev Assistant/scripts/generate_submission_w7.py"
```

Expected: Three DOCX files appear with placeholder content; figures extracted to `Dev Assistant/temp/ch8_figures/`. Once verified, REMOVE the placeholder constants — they will be replaced by the real content in Tasks 3–5.

- [ ] **Step 5: Commit the boilerplate**

```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py"
git commit -m "feat(w7): scaffold generator script with TPGS Ch.8 figure extraction"
```

---

### Task 3: Author the RMK content constant

**Files:**
- Modify: `Dev Assistant/scripts/generate_submission_w7.py` — insert `RMK = """..."""` constant
- Reference: `docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md` §4

- [ ] **Step 1: Write the RMK header block**

Replace the placeholder `RMK = "..."` with a triple-quoted f-string. Top of the string:

```python
def _img(name: str) -> str:
    return str(FIGURES_DIR / name).replace("\\", "/")

# Bind figure paths once the constant is built, OR build RMK inside main() after
# extract_figures runs. The latter is simpler — restructure so RMK is built
# inside main() and pass it as an argument.
```

Restructure: define `build_rmk(figures: dict) -> str`, `build_cr11() -> str`, `build_cr12() -> str` as functions. Call them in `main` after figure extraction.

Header content:
```markdown
# RINGKASAN MATERI KULIAH — PERTEMUAN 7

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Topik:** *Tailoring Strategy to Fit Specific Industry and Company Situations* (TPGS Ch.8)

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---
```

- [ ] **Step 2: Write §1 Pendahuluan (3 sub-headings, 600–800 words total)**

Sub-headings (each 200–300 words):
- **Dari Pemilihan Strategi ke Penyesuaian Situasional** — bridge Pert. 6 → Pert. 7
- **Mengapa Satu Strategi Generik Tidak Universal** — bold pivot on context-dependence of strategy
- **Pertanyaan Pengarah Pertemuan 7** — introduce *strategic fit* as the master concept; preview §9

Cite TPGS 2021, Ch.8 page references; cite Porter (1980) for generic strategies bridge.

- [ ] **Step 3: Write §2 Strategi pada *Emerging Industries***

Sub-headings:
- **Karakteristik Industri Baru** — technology uncertainty, no dominant design, customer segments unstable
- **Risiko Dominant-Design Race** — Anderson & Tushman (1990) cycle; bold reasoning on when pioneer rational vs late mover rational
- **Pilihan Strategis: Pioneer vs. Fast Follower** — conditions favoring each
- **Indonesian Examples** — Gojek on-demand transport pioneer; Tokopedia e-commerce early; eFishery aquatech

After Sub-heading 2, insert figure if relevant:
```markdown
![*Gambar 1 — Karakteristik Tahapan Industri (Industry Life Cycle)*]({fig_industry_lifecycle})

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.8, hlm. X*
```
Followed by 2–3 sentence interpretation.

- [ ] **Step 4: Write §3 Strategi pada *Rapidly Growing Industries***

Sub-headings:
- **Logika Share-Grab** — share captured during growth phase = permanent in maturity
- **Capacity Pre-emption** — Ghemawat (1991) commitment theory
- **Brand-Building dalam Jendela Pertumbuhan**
- **Bahaya Over-Expansion** — bold critique: capacity that outruns demand becomes balance-sheet anchor
- **Indonesian Examples** — Shopee growth-phase share grab; BCA mobile banking capacity pre-emption; Mixue rapid F&B expansion

- [ ] **Step 5: Write §4 Strategi pada *Maturing Industries***

Sub-headings:
- **Tanda-Tanda Maturitas** — demand growth slows, capacity > demand, price competition rises
- **Konsolidasi dan Shake-Out**
- **Cost Discipline sebagai Default**
- **Differentiation Refresh sebagai Counter-Strategy** — Apple smartphone refresh; Coca-Cola
- **Indonesian Examples** — Indomie premium variant; Aqua diferensiasi vs private label; Telkomsel cost discipline

- [ ] **Step 6: Write §5 Strategi pada *Stagnant or Declining Industries***

Sub-headings:
- **Tiga Pilihan Utama** (harvest, niche, end-game)
- **Harvest vs. Niche vs. End-Game** — decision criteria
- **Porter's Declining Industry Framework** — Porter (1980), Hambrick (1985)
- **Indonesian Examples** — rokok kretek (Sampoerna niche premium); media cetak (Kompas quality niche, Tempo digital pivot); taksi konvensional (Blue Bird hybrid digital)

- [ ] **Step 7: Write §6 Strategi pada *Turbulent / High-Velocity Industries***

Sub-headings:
- **Definisi Hypercompetition** — D'Aveni (1994)
- **Dynamic Capabilities Framework** — Teece, Pisano & Shuen (1997); sense-seize-transform
- **Real-Options Reasoning** — McGrath & MacMillan (2000)
- **Indonesian Examples** — fintech P2P (OVO/Dana/GoPay); ride-hailing post-pandemic; e-commerce flash-sale wars

- [ ] **Step 8: Write §7 Strategi pada *Fragmented Industries***

Sub-headings:
- **Penyebab Fragmentasi** — low entry barriers, diseconomies of scale, taste heterogeneity, local regulation
- **Pilihan: Konsolidasi vs. Spesialisasi**
- **Geographic Specialization**
- **Indonesian Examples** — Alfamart/Indomaret consolidation; Kopi Kenangan/Janji Jiwa geographic-then-national; Mitra Bukalapak warung digitalization

- [ ] **Step 9: Write §8 Strategi untuk Runner-Up, Weak-Position, Crisis-Ridden Companies**

Sub-headings:
- **Strategi untuk Runner-Up** — vacant-niche, specialist, growth-via-acquisition, distinctive-image
- **Strategi untuk Weak-Position** — abandon, harvest, retrench, turnaround
- **Turnaround Sequencing untuk Crisis-Ridden** — Hofer (1980), Pearce & Robbins (1993); stabilisasi → restrukturisasi → revitalisasi
- **Indonesian Examples** — Garuda Indonesia restrukturisasi 2022 PKPU; Telkomsel runner-up shift; Bank Mandiri post-1998 turnaround

Insert turnaround decision-flow figure here if extracted.

- [ ] **Step 10: Write §9 Sintesis: Strategic Fit sebagai Kerangka Master**

This is the **central paradigmatic synthesis section** — write with extra density (800–1000 words).

Sub-headings:
- **Asal Kerangka Fit** — Lawrence & Lorsch (1967), no *one best way*
- **Venkatraman (1989) Enam Perspektif Fit** — moderation, mediation, matching, gestalt, profile-deviation, covariation; explain each in 1–2 sentences
- **Miles & Snow (1978) Typology sebagai Fit-Configurational** — Defender, Prospector, Analyzer, Reactor
- **Jembatan ke Artikel 11 dan 12** — Hsieh & Chen = internal fit (strategy-HR-reward); Okebaram & Onuoha = external fit (strategy-sustainability-stakeholder); both are operationalizations of §9 principle

- [ ] **Step 11: Write §10 Kesimpulan**

Sub-headings:
- **Fit sebagai Proses Rekalibrasi Berkelanjutan**
- **Integrasi Pert. 4–7** — RBV → generic → strengthening → tailoring
- **Antisipasi Pert. 8** — international markets adds geographic dimension to fit

- [ ] **Step 12: Run the script and verify RMK DOCX**

```powershell
python "Dev Assistant/scripts/generate_submission_w7.py"
```

Open `RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 7.docx` and verify:
- All 10 sections present with sub-headings (###)
- Bold/italic formatting renders
- Figures appear inline with captions (not at end as appendix)
- No raw `{fig_xxx}` Python f-string remnants
- Indonesian PUEBI compliance, no AI-generic phrases, no Daftar Pustaka
- Page count: approx 18–25 pages

- [ ] **Step 13: Commit RMK content**

```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py" "RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 7.docx"
git commit -m "feat(w7): RMK Pertemuan 7 — TPGS Ch.8 walkthrough + Strategic Fit synthesis"
```

---

### Task 4: Author the CR Artikel 11 content constant

**Files:**
- Modify: `Dev Assistant/scripts/generate_submission_w7.py` — add `build_cr11() -> str` function
- Reference: `docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md` §5

- [ ] **Step 1: Write the CR11 header**

```markdown
# CRITICAL REVIEW — ARTIKEL 11

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Pertemuan:** 7 — *Tailoring Strategy to Fit Specific Industry and Company Situations*

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

**Artikel:** Hsieh, Y. H. & Chen, H. M. (2011). *Strategic Fit among Business Competitive Strategy, Human Resource Strategy, and Reward System.* Academy of Strategic Management Journal, 10(2): 11–32.

---
```

- [ ] **Step 2: Write §1 Identitas Artikel** (150–200 words)

Cover: full bibliographic data; AS-MJ journal context (Allied Academies, peer-reviewed, US-based, conceptual orientation); Taiwanese institutional affiliation explains Asian-firm framing; article type (conceptual-theoretical with case illustrations).

- [ ] **Step 3: Write §2 Tujuan Penelitian dan Posisi dalam Literatur** (250–300 words)

Sub-headings:
- **Pertanyaan Riset Utama**
- **Posisi dalam Rantai Literatur Strategic Fit** — Porter 1985; Schuler & Jackson 1987; Gomez-Mejia & Balkin 1992

- [ ] **Step 4: Write §3 Argumen Utama — Strategic Fit Triad** (400–500 words)

Sub-headings:
- **Komponen Triad** — business strategy ↔ HR strategy ↔ reward system
- **Logika Fit untuk Cost Leadership** — efficiency-HR + fixed/seniority reward
- **Logika Fit untuk Differentiation** — innovation-HR + variable/performance reward
- **Logika Fit untuk Focus Strategy** — hybrid adaptive HR
- **Hipotesis Konfigurasional** — Miller (1986); Doty Glick & Huber (1993); bold pivot on misalignment costs

- [ ] **Step 5: Write §4 Koneksi ke Topik Silabus** (200–250 words)

Sub-headings:
- **Triad Fit sebagai Operasionalisasi Internal Fit**
- **Linking §9 RMK ke Artikel Ini**

- [ ] **Step 6: Write §5 Kekuatan Artikel** (250–300 words)

Sub-headings:
- **Kontribusi Teoretis** — integrating two sub-literatures
- **Kejelasan Kerangka** — applicable as diagnostic
- **Relevansi Praktis bagi Manajer**

- [ ] **Step 7: Write §6 Keterbatasan dan Kelemahan** (300–400 words)

Sub-headings:
- **Sifat Konseptual Tanpa Uji Empiris Sistematis** — bold limitasi utama
- **Pengabaian Dinamika Temporal** — no dynamic-fit modeling
- **Asumsi Porter's Typology** — Kotha & Vadlamani (1995) measurement critique
- **Konteks Taiwan-Spesifik** — generalization caveat to Indonesia

- [ ] **Step 8: Write §7 Evaluasi Kritis (the dense critical core, 350–450 words)**

Sub-headings:
- **Apakah Fit Triad Benar-Benar Configurational atau Hanya Additive?** — Miller (1986) vs Venkatraman (1989); bold critique on inconsistent use
- **Masalah Endogenitas dalam Strategi-HR-Reward** — reverse causality / co-evolution problem
- **Apa yang Seharusnya Dilakukan** — fsQCA (Ragin 2008); longitudinal panel
- **Penilaian Kontribusi Orisinal** — tier-2 contribution: useful heuristic, not tested causal model

- [ ] **Step 9: Write §8 Implikasi bagi Pemahaman Manajemen Strategik** (350–450 words)

Sub-headings:
- **Implikasi Teoretis** — strengthens internal fit dimension
- **Implikasi Manajerial** — HR director at the strategy table
- **Implikasi untuk Konteks Indonesia** — Astra International triad alignment; Bank Mandiri post-merger reconfiguration; Unilever Indonesia differentiation triad; **negative case**: BUMN with differentiation strategy + bureaucratic HR-reward (PNS-style) → execution gap

- [ ] **Step 10: Write §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut** (200–250 words)

Sub-headings:
- **Pertanyaan Terbuka** — family-owned vs publicly-listed; transition periods; platform business algorithmic HR
- **Relevansi untuk Riset Indonesia** — dual-track BUMN HR system

- [ ] **Step 11: Run script, verify CR11 DOCX**

Same verification checklist as Task 3 Step 12. Target page count: 8–12 pages.

- [ ] **Step 12: Commit CR11 content**

```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py" "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 11.docx"
git commit -m "feat(w7): CR Artikel 11 (Hsieh & Chen 2011) — Strategic Fit Triad critique"
```

---

### Task 5: Author the CR Artikel 12 content constant

**Files:**
- Modify: `Dev Assistant/scripts/generate_submission_w7.py` — add `build_cr12() -> str` function
- Reference: `docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md` §6

- [ ] **Step 1: Write the CR12 header**

```markdown
# CRITICAL REVIEW — ARTIKEL 12

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Pertemuan:** 7 — *Tailoring Strategy to Fit Specific Industry and Company Situations*

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

**Artikel:** Okebaram, S. M. & Onuoha, C. E. (2018). *Implication of Strategic Fit and Sustainability on Organizational Effectiveness.* International Academic Research Conference in Vienna.

---
```

- [ ] **Step 2: Write §1 Identitas Artikel** (150–200 words)

Cover: full bibliographic data; conference paper venue tier (lower than top-tier SSCI journals); Nigerian institutional context (Federal University); article type (conceptual-review integrating sustainability + fit literatures).

- [ ] **Step 3: Write §2 Tujuan Penelitian dan Posisi dalam Literatur** (250–300 words)

Sub-headings:
- **Pertanyaan Riset**
- **Posisi Relatif terhadap Literatur Strategic Fit dan Sustainability** — Venkatraman 1989; Miles & Snow 1978; Elkington 1997; Hart 1995

- [ ] **Step 4: Write §3 Argumen Utama — Strategic Fit + Sustainability → Effectiveness** (400–500 words)

Sub-headings:
- **Konseptualisasi Strategic Fit**
- **Konseptualisasi Sustainability (Triple Bottom Line)**
- **Mekanisme Kausal yang Diajukan** — fit → legitimacy → resource access → effectiveness
- **Proposisi Utama** — bold pivot on sustainability as enabling condition, not cost trade-off; cite Porter & Kramer (2006) shared value

- [ ] **Step 5: Write §4 Koneksi ke Topik Silabus** (200–250 words)

Sub-headings:
- **Sustainability sebagai Dimensi Eksternal Fit**
- **Linking ke §9 RMK dan Artikel 11** — Article 11 = internal fit; Article 12 = external fit; both operationalize §9 principle

- [ ] **Step 6: Write §5 Kekuatan Artikel** (200–250 words)

Sub-headings:
- **Topik yang Relevan dan Aktual** — post-2015 SDG mandate, Paris Agreement
- **Integrasi Dua Aliran Literatur** — strategic fit + sustainability
- **Aksesibilitas untuk Praktisi**

- [ ] **Step 7: Write §6 Keterbatasan dan Kelemahan** (350–450 words)

Sub-headings:
- **Sifat Konseptual Tanpa Empiris** — bold limitasi utama
- **Definisi Sustainability yang Lentur** — conceptual conflation
- **Pengukuran Effectiveness yang Belum Dispecify** — vague operationalization
- **Basis Empiris Implisit Afrika** — generalization caveat to Indonesia
- **Methodological Disclosure yang Minim** — conference paper tier issue

- [ ] **Step 8: Write §7 Evaluasi Kritis (the dense critical core, 400–500 words)**

Sub-headings:
- **Apakah Sustainability dan Fit Benar-Benar Independent Dimensions?** — bold critique on double-counting (sustainability *is* fit with stakeholder expectations)
- **Eclecticism Teoretis sebagai Kelemahan** — RBV + contingency + stakeholder theory + TBL + shared value mashed without adjudication
- **Risiko *Greenwashing* Theoretical** — tautological enabling-condition claim
- **Apa yang Seharusnya Dilakukan** — operationalization with measurable indicators (carbon intensity, employee turnover, supplier diversity); multi-industry sample; theoretical adjudication
- **Penilaian Kontribusi Orisinal** — useful agenda-setting piece, weak as scholarly contribution

- [ ] **Step 9: Write §8 Implikasi bagi Pemahaman Manajemen Strategik** (400–500 words)

Sub-headings:
- **Implikasi Teoretis** — extends fit to stakeholder sustainability dimension
- **Implikasi Manajerial** — ESG as fit requirement (POJK 51/2017, impact investors, Gen Z consumers)
- **Implikasi untuk Konteks Indonesia** — Unilever Indonesia Sustainable Living Plan; Pertamina geothermal energy-transition fit; **tension case**: Adaro/Bayan coal sector misfit with global ESG capital flow; Sido Muncul herbal + community supplier; **PLN paradox**: fit with state mandate (universal electrification) vs. misfit with global climate compliance

- [ ] **Step 10: Write §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut** (200–250 words)

Sub-headings:
- **Pertanyaan Terbuka** — moderator vs mediator role; institutional voids operationalization; ESG metrics import misfit; microfoundations (board diversity + ESG-linked comp)
- **Relevansi untuk Riset Indonesia**

- [ ] **Step 11: Run script, verify CR12 DOCX**

Same checklist as Task 3 Step 12 / Task 4 Step 11. Target page count: 8–12 pages.

- [ ] **Step 12: Commit CR12 content**

```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py" "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 12.docx"
git commit -m "feat(w7): CR Artikel 12 (Okebaram & Onuoha 2018) — Fit + Sustainability critique"
```

---

### Task 6: Final verification pass on all three DOCX outputs

**Files (read-only verification):**
- `RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 7.docx`
- `Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 11.docx`
- `Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 12.docx`

- [ ] **Step 1: Re-run script idempotently**

```powershell
python "Dev Assistant/scripts/generate_submission_w7.py"
```

Expected: All three DOCX overwritten cleanly, no errors, no PyMuPDF warnings about missing anchors.

- [ ] **Step 2: Open each DOCX and run the quality checklist**

For each of the three files, verify:
- [ ] Title heading is 14pt centered bold
- [ ] Sub-headings (###) render as 12pt bold italic
- [ ] Body text is Times New Roman 12pt, line spacing 1.5
- [ ] First-line indent 1.25cm on body paragraphs
- [ ] Margins 3cm left / 2.5cm other sides
- [ ] Italic foreign terms render correctly
- [ ] Bold analytical pivots render correctly
- [ ] No raw `{fig_xxx}` Python f-string remnants
- [ ] No "TODO", "TBD", "Lorem ipsum" placeholder text
- [ ] No Daftar Pustaka section anywhere
- [ ] No AI-generic phrases: "delve into", "navigate the landscape", "in conclusion", "it is important to note"
- [ ] Inline citations in (Penulis tahun) format
- [ ] Indonesian examples are publicly verifiable corporate cases

For RMK only:
- [ ] 3–5 figures embedded inline with captions in *Gambar N. Judul (Sumber: TPGS 2021, hlm. X)* format
- [ ] Each figure has 1-line transitional intro + 2–3 sentence interpretation
- [ ] §9 (Strategic Fit synthesis) explicitly bridges to Artikel 11 and 12

- [ ] **Step 3: Cross-document consistency check**

- [ ] CR11 §4 references "internal fit"; CR12 §4 references "external fit"; RMK §9 introduces both terms
- [ ] All three documents cite Venkatraman (1989) and Lawrence & Lorsch (1967) consistently
- [ ] Pertemuan number "7" appears in all three headers (not residual "6" from copy-paste)

- [ ] **Step 4: Final commit**

If any fixes were applied in Steps 2–3:
```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py" "RMK/" "Critical Thinking of the Article/"
git commit -m "fix(w7): final verification pass — formatting + consistency"
```

If no fixes, skip this step.

- [ ] **Step 5: Mark plan complete**

```powershell
git log --oneline -10
```

Verify the W7 commits (scaffold → RMK → CR11 → CR12 → optional fix) appear in order.

---

## Acceptance Criteria

The plan is complete when:

1. Three DOCX files exist at the canonical output paths in `RMK/` and `Critical Thinking of the Article/`
2. All three pass the §6 quality checklist
3. Script `Dev Assistant/scripts/generate_submission_w7.py` is idempotent — running it twice produces identical outputs
4. Git log shows clean per-task commits
5. Spec coverage: every section in `2026-05-19-rmk-cr-pertemuan7-design.md` is reflected in the generated content
6. Strategic Fit / Contingency Theory paradigmatic synthesis is explicit in RMK §9 and bridges to both CRs §4
