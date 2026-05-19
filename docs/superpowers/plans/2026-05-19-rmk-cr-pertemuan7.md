# RMK + CR Pertemuan 7 Implementation Plan (Revised 2026-05-19)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate three Word documents — RMK Pert. 7 on *Corporate Strategy: Diversification and the Multibusiness Company* (Essentials Ch.8, with all four Ch.8 figures embedded), CR Artikel 11 (Hsieh & Chen 2011), CR Artikel 12 (Okebaram & Onuoha 2018) — with graduate-level analytical depth and an explicit three-level *Strategic Fit / Contingency Theory* paradigmatic synthesis (cross-business fit / internal fit / multi-element org fit).

**Architecture:** Python orchestrator (`generate_submission_w7.py`) extends the W6-enhanced pattern: PyMuPDF figure extraction from TPGS Ch.8 (4 figures at known PDF page indices), three Markdown content builders, pandoc invocation per file with `reference.docx`. Single-script run produces all three DOCX outputs.

**Tech Stack:** Python 3.12, PyMuPDF (`fitz`), Pandoc (`C:\Program Files\Pandoc\pandoc.exe`).

**Reference documents:**
- Spec: `docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md` (REVISED)
- Prior pipeline (figure-enabled): `Dev Assistant/scripts/generate_rmk6_enhanced.py`
- Pandoc reference: `Dev Assistant/scripts/reference.docx`

**Task 1 status:** Already complete — content extraction findings inlined into Tasks 2–5 below. Helper script `Dev Assistant/scripts/find_ch8.py` was created during Task 1 (read-only utility, kept for re-running validation).

---

## Confirmed source-material facts (from Task 1 findings)

**TPGS Ch.8 (Essentials of Strategic Management, 2021)** — chapter title: *Corporate Strategy: Diversification and the Multibusiness Company*; PDF index 191–218; reader pp. 152–180.

**Figures available (all four to be embedded):**

| Key | Anchor | PDF page index | Reader page | Title |
|---|---|---|---|---|
| `figure_8_1` | FIGURE 8.1 | 194 | 156 | Strategic Themes of Multibusiness Corporation |
| `figure_8_2` | FIGURE 8.2 | 195 | 157 | Related Diversification Built upon Strategic Fit in Value Chain Activities |
| `figure_8_3` | FIGURE 8.3 | 206 | 168 | Nine-Cell Industry Attractiveness–Competitive Strength Matrix |
| `figure_8_4` | FIGURE 8.4 | 210 | 172 | Strategic & Financial Options for Allocating Diversified Company Resources |

**Article 11 (Hsieh & Chen 2011)** — Academy of Strategic Management Journal 10(2): 11–32. Conceptual paper (no empirical test). Triad: business strategy / HR strategy type (innovation-oriented, contribution-oriented, commitment-oriented) / reward type (human capital, output, position). Key citations: Porter 1980/1985; Schuler & Jackson 1987; Miles & Snow 1978; Dyer & Holder 1988; Howard & Dougherty 2004; Snow & Hrebiniak 1980; Barney 1991, Wernerfelt 1984, Peteraf 1993 (RBV).

**Article 12 (Okebaram & Onuoha 2018)** — 2018 International Academic Research Conference Vienna, pp. 194–213. **Empirical survey study** (N=212 Nigerian telco + Ecobank, Z-tests, not conceptual-only). Mechanism: Strategic fit (operationalized via Medcof 1997 4Cs: Capability/Compatibility/Commitment/Control) → org design + employee relations + info exchange → effectiveness. Three null hypotheses tested, all rejected at p < .001. **Key absences (critique points):** does not cite Venkatraman 1989, Lawrence & Lorsch 1967, Elkington 1997, Hart 1995, Porter & Kramer 2006. Uses "sustainability" loosely to mean *sustained competitive advantage* (Porter 1985), not triple bottom line.

---

### Task 1: ~~Read primary sources and locate TPGS Ch.8~~ — COMPLETE

Findings inlined above and into Tasks 2–5. Helper script: `Dev Assistant/scripts/find_ch8.py`. No further action needed for this task.

---

### Task 2: Create `generate_submission_w7.py` — boilerplate + figure extraction

**Files:**
- Create: `Dev Assistant/scripts/generate_submission_w7.py`
- Reference (structure only): `Dev Assistant/scripts/generate_rmk6_enhanced.py`

- [ ] **Step 1: Write the file header, imports, and path constants**

```python
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
```

- [ ] **Step 2: Write the figure extraction function (concrete page indices)**

```python
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
```

- [ ] **Step 3: Write the pandoc helper**

```python
def pandoc(md: Path, out: Path) -> None:
    result = subprocess.run(
        [PANDOC, str(md), f"--reference-doc={REFERENCE}", "-o", str(out)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    print(f"Generated: {out.name}")
```

- [ ] **Step 4: Write the main entry**

```python
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
```

- [ ] **Step 5: Add temporary stub builders for smoke-test**

Add directly above the `if __name__ == "__main__":` block:

```python
def build_rmk(figures: dict) -> str:
    return "# RMK Pert. 7 placeholder\n\nPlaceholder body.\n"

def build_cr11() -> str:
    return "# CR Artikel 11 placeholder\n\nPlaceholder body.\n"

def build_cr12() -> str:
    return "# CR Artikel 12 placeholder\n\nPlaceholder body.\n"
```

- [ ] **Step 6: Smoke-test the boilerplate**

```powershell
python "Dev Assistant/scripts/generate_submission_w7.py"
```

Expected: Three DOCX files appear with placeholder content; four PNG figures saved to `Dev Assistant/temp/ch8_figures/`. Verify each PNG is > 10 KB by checking file sizes. Then DELETE the three stub builder functions — they will be replaced by the real builders in Tasks 3–5.

- [ ] **Step 7: Commit the boilerplate**

```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py"
git commit -m "feat(w7): scaffold generator script with TPGS Ch.8 figure extraction"
```

---

### Task 3: Author `build_rmk(figures)` content — Diversification + Strategic Fit

**Files:**
- Modify: `Dev Assistant/scripts/generate_submission_w7.py` — replace `build_rmk` stub with full implementation
- Reference: `docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md` §4

**Approach:** `build_rmk(figures)` takes the figures dict and returns a Markdown string. Build the string via f-string with embedded figure paths converted to forward-slash form.

- [ ] **Step 1: Replace stub with real signature and figure path setup**

```python
def build_rmk(figures: dict) -> str:
    def fp(name: str) -> str:
        return str(figures[name]).replace("\\", "/")

    fig1 = fp("figure_8_1")
    fig2 = fp("figure_8_2")
    fig3 = fp("figure_8_3")
    fig4 = fp("figure_8_4")

    return f"""# RINGKASAN MATERI KULIAH — PERTEMUAN 7

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Topik:** *Corporate Strategy: Diversification and the Multibusiness Company* (Essentials Ch.8)

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---
"""
```

- [ ] **Step 2: Write §1 Pendahuluan (3 sub-headings, 600–800 words)**

Sub-headings:
- **Dari Single-Business ke Multibusiness Decision** — bridge Pert. 4–6 → Pert. 7
- **Mengapa Diversifikasi Menjadi Pertanyaan Strategik** — bold pivot: kualitatif change
- **Pertanyaan Pengarah Pertemuan 7** — preview §9 strategic fit synthesis

- [ ] **Step 3: Write §2 Kapan Diversifikasi Menjadi Pertimbangan Strategik**

Sub-headings: **Sinyal Saturasi Bisnis Inti**, **Surplus Sumber Daya dan Kapabilitas**, **Pertumbuhan Shareholder Value Mensyaratkan Ekspansi**, **Risiko Diversifikasi Prematur**
- Indonesian: Astra International otomotif → heavy equipment + agribusiness + finansial; Sinar Mas pulp&paper → property + finansial + agribisnis

- [ ] **Step 4: Write §3 Membangun Shareholder Value — Tiga Tes Diversifikasi**

Sub-headings: **Tes 1 — Industry Attractiveness Test**, **Tes 2 — Cost of Entry Test**, **Tes 3 — Better-Off Test**, **Mengapa Lulus Ketiga Tes Sulit**
- Cite Porter (1987) tiga tes original
- Indonesian: Pertamina-Iran kasus cost-of-entry; Bank Mandiri konsolidasi 4 bank legacy as better-off test passed

- [ ] **Step 5: Write §4 Pendekatan Diversifikasi**

Sub-headings: ***Acquisition***, ***Internal Development***, ***Joint Venture***, **Kriteria Pemilihan Pendekatan**
- Indonesian: Indofood akuisisi Bogasari/Indolakto; GoTo merger; Pertamina-Eni JV

Insert after §4:
```python
f"""

![*Gambar 1. Strategic Themes of Multibusiness Corporation (Related vs Unrelated Diversification)*]({fig1})

*Sumber: Gamble, Peteraf & Thompson (2021), Essentials of Strategic Management, Ch.8, hlm. 156*

Gambar 1 menunjukkan dua tema strategis utama yang dapat dipilih oleh perusahaan terdiversifikasi. Pilihan ini menjadi kerangka untuk seluruh pembahasan diversifikasi berikutnya — apakah membangun portofolio bisnis yang saling berbagi nilai-rantai (related) atau portofolio bisnis yang independen secara operasional (unrelated).

"""
```

- [ ] **Step 6: Write §5 Pilihan Jalur: Related vs Unrelated**

Sub-headings: ***Related Diversification* — Logika Cross-Business Strategic Fit**, ***Unrelated Diversification* — Logika Portfolio Risk Management**, **Bukti Empiris**, **Indonesian Examples**
- Cite Rumelt (1974, 1982), Markides & Williamson (1994), Panzar & Willig (1981), Teece (1980)
- Indonesian: Astra (related), Sinar Mas/Salim (unrelated), GoTo (related platform fit)

- [ ] **Step 7: Write §6 Diversifikasi ke Bisnis Related — Strategic Fit & Economies of Scope**

This is a central conceptual section — 700–900 words. Sub-headings: **Definisi Strategic Fit di Level Korporat**, **Empat Tipe Cross-Business Value-Chain Fit**, ***Economies of Scope* vs. *Economies of Scale***, **Bagaimana Related Diversification Menciptakan Keunggulan Kompetitif**

Insert after §6:
```python
f"""

![*Gambar 2. Cross-Business Value-Chain Strategic Fit*]({fig2})

*Sumber: Gamble, Peteraf & Thompson (2021), Essentials of Strategic Management, Ch.8, hlm. 157*

Gambar 2 adalah visualisasi paling penting dari konsep *strategic fit* di level korporat — peta yang menunjukkan di mana value-chain matchups antar-bisnis dapat menjadi sumber economies of scope. Inilah jembatan analitis yang akan dirujuk kembali pada §9 untuk menghubungkan Ch.8 dengan Artikel 11 (internal fit) dan Artikel 12 (multi-element organizational fit).

"""
```

- Cite Kraft–Heinz example (TPGS Concepts & Connections 8.1, hlm. 159)
- Indonesian: Astra cross-business fit (Toyota Astra + AHM + Astra distribution + ACC financial); BCA-Djarum; GoTo cross-platform

- [ ] **Step 8: Write §7 Diversifikasi ke Bisnis Unrelated — Logika Conglomerate**

Sub-headings: **Mengapa Perusahaan Memilih Unrelated**, **Bagaimana Unrelated Menciptakan Nilai**, **Tiga Jebakan Unrelated Diversification**, **Misguided Reasons**
- Reference Berkshire Hathaway capital allocation model
- Indonesian: Salim Group post-1998 forced deleveraging; Bakrie Group re-focus pressure

- [ ] **Step 9: Write §8 Evaluasi Strategi Perusahaan Terdiversifikasi — 6 Langkah**

Sub-headings: **Langkah 1 Industry Attractiveness**, **Langkah 2 Business-Unit Competitive Strength**, **Langkah 3 Strategic Fit Across Businesses**, **Langkah 4 Resource Fit**, **Langkah 5 Ranking dan Resource Allocation**, **Langkah 6 Crafting New Strategic Moves**

Insert after Langkah 2:
```python
f"""

![*Gambar 3. Nine-Cell Industry Attractiveness–Competitive Strength Matrix*]({fig3})

*Sumber: Gamble, Peteraf & Thompson (2021), Essentials of Strategic Management, Ch.8, hlm. 168*

Gambar 3 adalah alat analitis pokok yang digunakan untuk memetakan unit-unit bisnis di dalam portofolio terdiversifikasi. Setiap bisnis ditempatkan sebagai bubble berdasarkan industry attractiveness (sumbu vertikal) dan competitive strength (sumbu horizontal). Ukuran bubble merepresentasikan revenue, sedangkan posisi diagonal menentukan rekomendasi alokasi sumber daya — *grow and build* pada diagonal kanan-atas, *defend and maintain* di tengah, kandidat divestasi di kiri-bawah.

"""
```

Insert after Langkah 6:
```python
f"""

![*Gambar 4. Strategic & Financial Options for Allocating Diversified Company Resources*]({fig4})

*Sumber: Gamble, Peteraf & Thompson (2021), Essentials of Strategic Management, Ch.8, hlm. 172*

Gambar 4 mengoperasionalkan Langkah 6: pilihan-pilihan strategis (invest to strengthen, akuisisi, internal start-up, pay down debt) dan pilihan finansial (dividen, buyback, cash reserve) yang dapat dipilih perusahaan terdiversifikasi. Trade-off antara keduanya — re-investing in businesses vs. returning cash to shareholders — adalah pertanyaan klasik corporate finance yang menjadi keputusan strategik di level board.

"""
```

- [ ] **Step 10: Write §9 Sintesis: Strategic Fit sebagai Kerangka Master di Tiga Level**

The **central paradigmatic synthesis section** — write with extra density (900–1100 words).

Sub-headings: **Asal Kerangka Fit dan Contingency Theory**, **Tiga Level Strategic Fit dalam Pertemuan 7**, **Venkatraman (1989) Enam Perspektif Fit**, **Miles & Snow (1978) Typology dan Equifinality (Doty et al. 1993)**, **Jembatan Eksplisit ke Artikel 11 dan 12**

- Lawrence & Lorsch (1967) contingency — *no one best way*
- Level 1: Cross-business fit (TPGS Ch.8)
- Level 2: Internal business fit (Artikel 11: strategy → HR type → reward type)
- Level 3: Organizational alignment fit (Artikel 12: 4Cs → org design + employee relations + info exchange)
- Venkatraman (1989) six perspectives: moderation/mediation/matching/gestalt/profile-deviation/covariation
- Miles & Snow typology + Doty et al. (1993) equifinality
- Nadler & Tushman (1980) fit definition (used by Artikel 12)

- [ ] **Step 11: Write §10 Kesimpulan**

Sub-headings: **Fit sebagai Proses Rekalibrasi Berkelanjutan di Setiap Level**, **Integrasi Pert. 4–7**, **Antisipasi Pert. 8 (Internasional)**

- [ ] **Step 12: Close the triple-quoted f-string with `"""`**

- [ ] **Step 13: Run the script and verify RMK DOCX**

```powershell
python "Dev Assistant/scripts/generate_submission_w7.py"
```

Open `RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 7.docx` and verify:
- All 10 sections present with sub-headings (###)
- Bold/italic formatting renders
- 4 figures appear inline with captions in correct positions
- No raw `{fig1}` Python f-string remnants
- Indonesian PUEBI compliance, no AI-generic phrases, no Daftar Pustaka
- Page count: approx 20–28 pages

- [ ] **Step 14: Commit RMK content**

```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py" "RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 7.docx"
git commit -m "feat(w7): RMK Pertemuan 7 — Corporate Strategy Diversification + Strategic Fit synthesis"
```

---

### Task 4: Author `build_cr11()` content — Hsieh & Chen 2011

**Files:**
- Modify: `Dev Assistant/scripts/generate_submission_w7.py` — replace `build_cr11` stub
- Reference: `docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md` §5

- [ ] **Step 1: Write the function signature and header**

```python
def build_cr11() -> str:
    return """# CRITICAL REVIEW — ARTIKEL 11

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Pertemuan:** 7 — *Corporate Strategy: Diversification and the Multibusiness Company*

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

**Artikel:** Hsieh, Y. H. & Chen, H. M. (2011). *Strategic Fit among Business Competitive Strategy, Human Resource Strategy, and Reward System.* Academy of Strategic Management Journal, 10(2): 11–32.

---
"""
```

- [ ] **Step 2: Write §1 Identitas Artikel** (150–200 words)

Cover: full bibliographic data; ASMJ context (Allied Academies, US-based, conceptual orientation, B/C-tier journal); affiliation (Tamkang University, Taiwan); article type — **murni konseptual/literature-review, tidak ada uji empiris**; penerbit Dreamcatchers Group LLC.

- [ ] **Step 3: Write §2 Tujuan Penelitian dan Posisi dalam Literatur** (250–300 words)

Sub-headings: **Pertanyaan Riset Utama**, **Posisi dalam Rantai Literatur Strategic Fit**
- Position relative to: Porter 1980/1985; Schuler & Jackson 1987; Miles & Snow 1978/1984; Snow & Hrebiniak 1980; Howard & Dougherty 2004; Dyer & Holder 1988; RBV (Wernerfelt 1984, Barney 1991, Peteraf 1993)

- [ ] **Step 4: Write §3 Argumen Utama — Strategic Fit Triad** (450–550 words)

Sub-headings: **Komponen Triad yang Sebenarnya**, **Logika Fit untuk *Differentiation***, **Logika Fit untuk *Overall Cost Leadership***, **Logika Fit untuk *Focus***, **Hipotesis Konfigurasional**

State the actual triad from Tabel 1 (hlm. 26):
- Differentiation → Innovation-oriented HR → Human capital reward (intrinsic)
- Cost leadership → Contribution-oriented HR → Output reward (extrinsic)
- Focus → Commitment-oriented HR → Position reward (both)

Include at least 2 direct short quotations with page references:
- (hlm. 11) "A strategic fit between a business strategy and a human resource strategy can help retain and motivate employees and translate into organizational performance and competitive advantage."
- (hlm. 17) "Successful strategy execution requires the creation of a 'fit' based on the interaction between external dependencies and internal capabilities (Snow & Hrebiniak, 1980)."

Bold pivot: misalignment example — differentiation + contribution-oriented HR + output reward = innovation paralysis.

- [ ] **Step 5: Write §4 Koneksi ke Topik Silabus (Pertemuan 7)** (200–250 words)

Sub-headings: **Triad Fit sebagai Operasionalisasi Internal Fit**, **Linking ke §9 RMK ke Artikel Ini**

- [ ] **Step 6: Write §5 Kekuatan Artikel** (250–300 words)

Sub-headings: **Kontribusi Teoretis: Integrasi Dua Aliran Literatur**, **Kejelasan Kerangka untuk Aplikasi Manajerial**, **Akar Teoretis yang Solid**

- [ ] **Step 7: Write §6 Keterbatasan dan Kelemahan** (350–450 words)

Sub-headings: **Sifat Konseptual Tanpa Uji Empiris** (cite penulis's own admission hlm. 27), **Pengabaian Dinamika Temporal**, **Ketergantungan pada Porter's Typology** (Kotha & Vadlamani 1995 measurement critique), **Konteks Kultural Tidak Dibahas** (Taiwan implicit), **Tidak Ada Diskusi Reverse Causality**

- [ ] **Step 8: Write §7 Evaluasi Kritis (dense critical core, 400–500 words)**

Sub-headings: **Apakah Fit Triad Benar-Benar Configurational atau Hanya Additive?**, **Masalah Operasionalisasi**, **Apa yang Seharusnya Dilakukan**, **Penilaian Kontribusi Orisinal**

- Configurational vs additive distinction (Miller 1988; Doty et al. 1993 sense vs Venkatraman 1989 additive)
- Operationalization: no measurement guidance provided
- What should have been done: cluster analysis (Ketchen et al. 1997); fsQCA (Ragin 2008); longitudinal panel
- Assessment: tier-2 contribution — useful heuristic, empirical promise unfulfilled

- [ ] **Step 9: Write §8 Implikasi bagi Pemahaman Manajemen Strategik** (350–450 words)

Sub-headings: **Implikasi Teoretis**, **Implikasi Manajerial**, **Implikasi untuk Konteks Indonesia**

Indonesian examples (named in spec):
- Astra International triad fit (Astra Management System, KPI-based variable reward)
- Bank Mandiri post-merger 2005–2010 (cost leadership retail + standardized HR + cost-control reward + BSC KPI cascade)
- Unilever Indonesia (differentiation + Unilever Future Leaders Program + LTI)
- **Negative case:** BUMN with differentiation strategy + bureaucratic HR-reward (PNS-style, golongan-based) → execution gap

- [ ] **Step 10: Write §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut** (200–250 words)

Sub-headings: **Pertanyaan Terbuka**, **Relevansi untuk Riset Indonesia**

- Family-owned vs publicly-listed
- Transitional strategies (digital transformation, ESG pivot)
- BUMN dual-track HR
- Platform business algorithmic management — fourth element to the triad?

- [ ] **Step 11: Close the triple-quoted string with `"""`**

- [ ] **Step 12: Run script, verify CR11 DOCX**

Same verification checklist as Task 3. Target page count: 8–12 pages.

- [ ] **Step 13: Commit CR11 content**

```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py" "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 11.docx"
git commit -m "feat(w7): CR Artikel 11 (Hsieh & Chen 2011) — Strategic Fit Triad critique"
```

---

### Task 5: Author `build_cr12()` content — Okebaram & Onuoha 2018

**Files:**
- Modify: `Dev Assistant/scripts/generate_submission_w7.py` — replace `build_cr12` stub
- Reference: `docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md` §6

- [ ] **Step 1: Write the function signature and header**

```python
def build_cr12() -> str:
    return """# CRITICAL REVIEW — ARTIKEL 12

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Pertemuan:** 7 — *Corporate Strategy: Diversification and the Multibusiness Company*

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

**Artikel:** Okebaram, S. M. & Onuoha, C. E. (2018). *Implication of Strategic Fit and Sustainability on Organizational Effectiveness.* The 2018 International Academic Research Conference in Vienna, pp. 194–213.

---
"""
```

- [ ] **Step 2: Write §1 Identitas Artikel** (180–220 words)

Cover: bibliographic data; conference venue tier; Nigerian institutional context (Michael Okpara University of Agriculture; University of Science and Technology Enugu); article type — **empirical survey study with Z-tests**, NOT conceptual-only; flag the Field Survey 2014 → Paper 2018 lag as a methodological disclosure issue.

- [ ] **Step 3: Write §2 Tujuan Penelitian dan Posisi dalam Literatur** (300–350 words)

Sub-headings: **Pertanyaan Riset dan Tiga Hipotesis Null**, **Posisi dalam Literatur Strategic Fit**

State all 3 hypotheses with Z-test results (Z = 5.342, 5.677, 5.745; p < .001). Position relative to: Porter 1985; Nadler & Tushman 1980; Miles & Snow 1978; Doty Glick & Huber 1993; Zajac Kraatz & Bresser 2000; Medcof 1997; Shelton 1988.

- [ ] **Step 4: Write §3 Argumen Utama — Strategic Fit + 4Cs → Org Effectiveness** (450–550 words)

Sub-headings: **Konseptualisasi Strategic Fit (Nadler & Tushman 1980)**, **Kerangka 4Cs Medcof (1997)**, **Mekanisme Kausal yang Diuji**, **Temuan Empiris**

Direct quotation from hlm. 195:
> "Fit is defined as 'the degree to which the needs, demands, goals, objectives and structures of one component' (Nadler and Tushman, 1980). This conceptualization implies that high level of strategic fit is advantageous; therefore, an organization's fit should be maximized."

Direct quotation from hlm. 210 (Conclusion):
> "Based on the research outcome, we conclude that the organizations can achieve synergy and sustain their organizational effectiveness by integrating the element of 4Cs capability, compatibility, commitment and control with the appropriate organization design, good employee relations and effective information exchange."

**Bold note:** judul artikel mencantumkan *sustainability* tetapi konseptualisasi penulis sebenarnya merujuk pada *sustained competitive advantage* (Porter 1985) — bukan triple bottom line atau natural-resource-based view. Inilah celah konseptual yang harus dieksplorasi di §6 dan §7.

- [ ] **Step 5: Write §4 Koneksi ke Topik Silabus (Pertemuan 7)** (200–250 words)

Sub-headings: **4Cs sebagai Operasionalisasi Strategic Fit di Level Multibusiness/Alliance**, **Linking ke §9 RMK dan Artikel 11**

- [ ] **Step 6: Write §5 Kekuatan Artikel** (200–250 words)

Sub-headings: **Topik yang Relevan secara Manajerial**, **Operasionalisasi via 4Cs**, **Uji Empiris (Berbeda dari Banyak Conference Papers)**

Note M&A failure rates 50–60% (Bamford, Gomes-Casseres & Robinson 2004, dikutip oleh penulis).

- [ ] **Step 7: Write §6 Keterbatasan dan Kelemahan** (450–550 words)

Sub-headings (all critical):
- **Definisi Sustainability yang Longgar dan Berpotensi Menyesatkan** — bold limitasi utama: judul memakai *sustainability* tapi konsep yang dibahas adalah *sustained competitive advantage*
- **Empirical Lag Empat Tahun yang Tidak Diungkapkan** — Field Survey 2014 → Paper 2018
- **Metodologi Statistik yang Diragukan** — Z-test pada Likert means; K-S menguji normalitas, bukan hipotesis means
- **Tidak Ada Validitas/Reliabilitas Konstruk** — no Cronbach alpha, no CFA
- **Basis Empiris Nigeria-Spesifik** — 3 telco + 1 bank, one country, two sectors
- **Methodological Disclosure yang Minim** — no demographic profile, no missing data discussion

- [ ] **Step 8: Write §7 Evaluasi Kritis (the densest section, 500–600 words)**

Sub-headings (all critical):
- **Konflasi Sustainability dan Sustained Competitive Advantage** — bold core critique
- **Eclecticism Teoretis sebagai Kelemahan** — Porter + Miles & Snow + Nadler & Tushman + Medcof + Doty + Zajac + Shelton + Hoffmann + Day + Grant mashed without adjudication
- **Klaim Kausal Berlebihan dari Survei Cross-Sectional** — Z-test on Likert ≠ causation
- **Gap Literatur: Yang Seharusnya Dikutip tapi Tidak** — explicit list of absent citations: Venkatraman 1989, Lawrence & Lorsch 1967, Elkington 1997, Hart 1995, Porter & Kramer 2006
- **Apa yang Seharusnya Dilakukan** — explicit sustainability definition; SEM with validated 4Cs constructs; longitudinal design; multi-industry, multi-country sample; integration with classical fit literature
- **Penilaian Kontribusi Orisinal** — useful agenda-setting + classroom discussion piece; weak as scholarly contribution

- [ ] **Step 9: Write §8 Implikasi bagi Pemahaman Manajemen Strategik** (450–550 words)

Sub-headings: **Implikasi Teoretis**, **Implikasi Manajerial**, **Implikasi untuk Konteks Indonesia**

Indonesian examples (named in spec):
- Bank Mandiri post-merger 4Cs integration (4 bank legacy: BBD, BDN, BankExim, Bapindo)
- Astra International acquisition track (Astra Daihatsu, AHM, KOMATSU partnership)
- GoTo merger (Gojek + Tokopedia 2021) — Indonesia's largest fit test
- **Tension case:** Adaro/Bayan coal sector misfit with global ESG capital flow (this is where Elkington 1997 sustainability is relevant — and where Okebaram & Onuoha's framework fails)

- [ ] **Step 10: Write §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut** (250–300 words)

Sub-headings: **Pertanyaan Terbuka**, **Relevansi untuk Riset Indonesia**

- Sustainability (Elkington TBL) vs sustained advantage (Porter)
- 4Cs operationalization via SEM/CFA
- Institutional voids (Khanna & Palepu 2000) effect on 4Cs assessment in Indonesian M&A
- Microfoundations: board diversity, ESG-linked comp, stakeholder engagement

- [ ] **Step 11: Close the triple-quoted string with `"""`**

- [ ] **Step 12: Run script, verify CR12 DOCX**

Same verification checklist as Tasks 3–4. Target page count: 10–14 pages (more critique density than CR11).

- [ ] **Step 13: Commit CR12 content**

```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py" "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 12.docx"
git commit -m "feat(w7): CR Artikel 12 (Okebaram & Onuoha 2018) — 4Cs + sustainability conflation critique"
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

Expected: All three DOCX overwritten cleanly, no errors, no PyMuPDF warnings about missing figure anchors.

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
- [ ] No fabricated citations — Article 11 cites only authors actually in its reference list; Article 12 cites only authors actually in its reference list (Venkatraman, Lawrence & Lorsch, Elkington, Hart, Porter & Kramer must NOT be attributed to Okebaram & Onuoha — only used as external critical reference points marked as such)

For RMK only:
- [ ] 4 figures embedded inline with captions in *Gambar N. Judul (Sumber: TPGS 2021, hlm. X)* format
- [ ] Each figure has 1-line transitional intro + 2–3 sentence interpretation
- [ ] §9 (Strategic Fit synthesis) explicitly bridges to Artikel 11 and 12 at three levels
- [ ] Topic title in header is "Corporate Strategy: Diversification and the Multibusiness Company" (NOT "Tailoring Strategy")

- [ ] **Step 3: Cross-document consistency check**

- [ ] CR11 §4 references "internal fit"; CR12 §4 references "multi-element organizational fit" / "4Cs"; RMK §9 introduces and ties together all three levels (cross-business / internal / 4Cs)
- [ ] All three documents consistently treat Article 12's "sustainability" as conflated with "sustained advantage" — not as TBL
- [ ] Pertemuan number "7" appears in all three headers (not residual "6" from copy-paste)
- [ ] RMK header topic matches spec §1 ("Corporate Strategy: Diversification and the Multibusiness Company")

- [ ] **Step 4: Final commit (if fixes applied)**

If any fixes were applied in Steps 2–3:
```powershell
git add "Dev Assistant/scripts/generate_submission_w7.py" "RMK/" "Critical Thinking of the Article/"
git commit -m "fix(w7): final verification pass — formatting + consistency"
```

If no fixes, skip this step.

- [ ] **Step 5: Verify git log**

```powershell
git log --oneline -12
```

Verify the W7 commits (scaffold → RMK → CR11 → CR12 → optional fix) appear in order alongside the spec/plan commits.

---

## Acceptance Criteria

The plan is complete when:

1. Three DOCX files exist at the canonical output paths in `RMK/` and `Critical Thinking of the Article/`
2. All three pass the §6 quality checklist (including no-fabricated-citations check)
3. Script `Dev Assistant/scripts/generate_submission_w7.py` is idempotent — running it twice produces identical outputs
4. Git log shows clean per-task commits
5. Spec coverage: every section in `2026-05-19-rmk-cr-pertemuan7-design.md` is reflected in the generated content
6. Three-level Strategic Fit / Contingency Theory paradigmatic synthesis is explicit in RMK §9 and bridges to both CRs §4 with no citation fabrication
