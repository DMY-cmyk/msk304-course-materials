# RMK Pert. 6 Enhanced Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce an enhanced `RMK Pert. 6.docx` that embeds real figures/case-box images extracted from TPGS Ch.6 and covers every section of the chapter — including content missing from the existing RMK.

**Architecture:** A new standalone script `generate_rmk6_enhanced.py` uses PyMuPDF to clip four visual elements from the TPGS textbook PDF, saves them as PNGs, then builds a full enhanced-Markdown document that references those images and includes the audited Ch.6 content, and converts it to DOCX via Pandoc.

**Tech Stack:** Python 3.12, PyMuPDF (fitz) 1.27.1 (installed), Pandoc (`C:\Program Files\Pandoc\pandoc.exe`), existing `reference.docx`.

---

### Task 1: Audit TPGS Ch.6 and extract figures

**Files:**
- Create: `Dev Assistant/scripts/generate_rmk6_enhanced.py` (figure-extraction functions only in this task)

- [ ] **Step 1: Read full Ch.6 text to capture all content**

```python
import fitz

EBOOK = r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Ebook\(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf"
doc = fitz.open(EBOOK)
# Ch.6 = PDF pages 148–168 (0-indexed), reader pages 149–169
for pg in range(148, 169):
    text = doc[pg].get_text()
    print(f"=== PDF page {pg+1} ===")
    print(text[:300])
```

Run this to verify all section headings are readable and confirm page mapping before extraction.

- [ ] **Step 2: Write `extract_figures()` function**

```python
from pathlib import Path
import fitz

def extract_figures(ebook_path: str, figures_dir: Path) -> dict[str, Path]:
    """Extract Figure 6.1 and three C&C boxes from TPGS Ch.6.
    Returns dict mapping name -> saved PNG path."""
    figures_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(ebook_path)
    results = {}

    # --- Figure 6.1 (PDF page 149, 0-indexed) ---
    pg = doc[149]
    mat = fitz.Matrix(2, 2)
    hits = pg.search_for("FIGURE 6.1")
    if hits:
        # Clip from top of figure label down to bottom of page
        r = hits[0]
        clip = fitz.Rect(30, r.y0 - 5, pg.rect.width - 30, pg.rect.height - 30)
        pix = pg.get_pixmap(matrix=mat, clip=clip)
    else:
        # Fallback: render lower 55% of page
        h = pg.rect.height
        clip = fitz.Rect(30, h * 0.45, pg.rect.width - 30, h - 30)
        pix = pg.get_pixmap(matrix=mat, clip=clip)
    out = figures_dir / "figure_6_1.png"
    pix.save(str(out))
    results["figure_6_1"] = out

    # --- C&C boxes: anchor search + full-box clip ---
    cc_specs = [
        ("cc_6_1_etsy",    "CONCEPTS & CONNECTIONS 6.1", [153, 154]),
        ("cc_6_2_walmart", "CONCEPTS & CONNECTIONS 6.2", [159, 160]),
        ("cc_6_3_tesla",   "CONCEPTS & CONNECTIONS 6.3", [163, 164]),
    ]
    for name, anchor, pg_indices in cc_specs:
        clipped = False
        for pg_idx in pg_indices:
            pg = doc[pg_idx]
            hits = pg.search_for(anchor)
            if hits:
                r = hits[0]
                # Capture from anchor top to page bottom
                clip = fitz.Rect(30, r.y0 - 5, pg.rect.width - 30, pg.rect.height - 30)
                pix = pg.get_pixmap(matrix=mat, clip=clip)
                out = figures_dir / f"{name}.png"
                pix.save(str(out))
                results[name] = out
                clipped = True
                break
        if not clipped:
            # Fallback: render full first candidate page
            pg = doc[pg_indices[0]]
            pix = pg.get_pixmap(matrix=fitz.Matrix(2, 2))
            out = figures_dir / f"{name}.png"
            pix.save(str(out))
            results[name] = out

    doc.close()
    return results
```

- [ ] **Step 3: Validate extracted PNGs**

```python
def validate_figures(results: dict[str, Path]) -> None:
    expected = ["figure_6_1", "cc_6_1_etsy", "cc_6_2_walmart", "cc_6_3_tesla"]
    for key in expected:
        path = results.get(key)
        if not path or not path.exists():
            raise FileNotFoundError(f"Missing figure: {key}")
        size = path.stat().st_size
        if size < 10_000:
            raise ValueError(f"Figure {key} too small ({size} bytes) — likely blank clip")
        print(f"  OK {key}: {size:,} bytes")
```

Run: `python -c "from generate_rmk6_enhanced import extract_figures, validate_figures; ..."`
Expected: all four PNGs present, each > 10 KB.

---

### Task 2: Build enhanced RMK Markdown content

**Files:**
- Modify: `Dev Assistant/scripts/generate_rmk6_enhanced.py` (add `build_rmk_content()` function)

- [ ] **Step 1: Read the existing RMK content from the current w6 script as baseline**

```python
# Read the existing RMK constant from generate_submission_w6.py as starting point.
# The enhanced version RETAINS all 9 existing sections + adds missing content + image refs.
# Do not regenerate from scratch — extend the existing content.
```

- [ ] **Step 2: Write `build_rmk_content(figures_dir)` function**

The function returns the full enhanced Markdown string. Structure:

```python
def build_rmk_content(figures_dir: Path) -> str:
    fig1   = str(figures_dir / "figure_6_1.png").replace("\\", "/")
    etsy   = str(figures_dir / "cc_6_1_etsy.png").replace("\\", "/")
    walmart = str(figures_dir / "cc_6_2_walmart.png").replace("\\", "/")
    tesla  = str(figures_dir / "cc_6_3_tesla.png").replace("\\", "/")

    return f"""# RINGKASAN MATERI KULIAH — PERTEMUAN 6

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer
**Topik:** *Strengthening a Company's Competitive Position: Strategic Moves, Timing, and Scope of Operations* (TPGS Ch.6 + Henry Ch.5–6)
**Mahasiswa:** Dzaki Muhammad Yusfian
**NIM:** 1125 01079

---

## 1. Pendahuluan

[... existing §1 content ...]

![*Gambar 6.1 — Strategi untuk Memperkuat Posisi Kompetitif Perusahaan*]({fig1})

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.111*

---

## 2. *Offensive Strategies*

[... existing §2 content with sub-headings ...]

### Memilih Basis Serangan Kompetitif

**Enam basis serangan** yang diidentifikasi TPGS Ch.6 (p.151):
1. **Keunggulan biaya** — menyerang dengan harga lebih rendah ketika pesaing tidak dapat menandingi struktur biaya
2. **Segmen pembeli yang kurang terlayani** — fokus pada kebutuhan yang diabaikan pesaing dominan
3. **Celah kualitas, layanan, atau fitur** — mengisi gap yang ada di penawaran pesaing
4. **Inovasi produk/proses** — melompati generasi teknologi pesaing
5. **Kesenjangan kesadaran merek** — membangun brand di pasar di mana pemimpin lemah secara reputasi
6. **Celah distribusi** — memasuki saluran distribusi yang belum digarap pesaing

### Memilih Pesaing yang Akan Diserang

**Tiga target utama** per TPGS Ch.6 (p.152):
- **Pemimpin pasar yang rentan**: penyerang yang cocok ketika pemimpin lalai atau memiliki kelemahan struktural
- **Perusahaan *runner-up***: target lebih mudah dengan sumber daya lebih terbatas
- **Menghindari *strong fighters***: perusahaan dengan kas dalam, kemampuan bertahan, dan kemauan membalas — menyerang mereka berisiko tinggi

[... continue all sub-sections ...]

---

## 3. *Defensive Strategies*

[... existing §3 content ...]

### Memblokir Jalur yang Terbuka bagi Penantang

Per TPGS Ch.6 (p.154), taktik pemblokiran konkret:
- Memperluas lini produk untuk menutup celah yang dapat dieksploitasi penantang
- Memperkenalkan model ekonomi dan premium untuk menutup rentang harga
- Mempertahankan hubungan kuat dengan dealer/distributor melalui insentif eksklusif
- Menawarkan program loyalitas pembeli untuk meningkatkan *switching costs*
- Membangun kapasitas cadangan untuk merespons serangan dengan cepat

### Memberi Sinyal Bahwa Pembalasan Sangat Mungkin

**Credibility theory** (Schelling 1960) mensyaratkan bahwa ancaman harus **kredibel** — artinya, biaya tidak membalas harus lebih tinggi dari biaya membalas. TPGS Ch.6 (p.154) mengidentifikasi empat sinyal yang efektif:
- Pengumuman publik tentang niat mempertahankan posisi
- Menyamakan atau melampaui pemotongan harga pesaing segera
- Membangun *war chest* kas dan surat berharga yang tampak dari luar
- Menyerang balik di pasar asal pesaing (*cross-parry*)

---

## 4. *Timing Strategies*

[... existing §4 content ...]

### Kerangka Pengambilan Keputusan: *Early Mover* vs. *Late Mover*

TPGS Ch.6 (p.156) menyediakan kerangka keputusan eksplisit:

**Faktor yang mendukung masuk lebih awal (*early entry*):**
- Kurva belajar yang curam — pengalaman awal menghasilkan keunggulan biaya permanen
- Pra-emosi sumber daya langka (lokasi, bahan baku, talenta)
- *Network effects* — nilai meningkat seiring pertambahan pengguna
- *Switching costs* tinggi — pelanggan awal terkunci
- Preferensi merek yang terbentuk kuat

**Faktor yang mendukung masuk lebih lambat (*late entry*):**
- Menghindari biaya perintisan (*pioneering costs*) — edukasi pasar, kesalahan generasi pertama
- Belajar dari kesalahan *early mover* secara gratis
- *Free-ride* pada edukasi pasar yang sudah dilakukan
- Melompati teknologi generasi pertama ke yang lebih baik
- Pelanggan sudah teredukasi dan siap membeli

---

## 5. *Scope of Operations*

[... existing §5 content ...]

### *Horizontal Merger and Acquisition Strategies*

[... existing M&A content ...]

#### Mengapa M&A Sering Gagal Memenuhi Ekspektasi

TPGS Ch.6 (p.159) mengidentifikasi **lima penyebab utama kegagalan M&A**:
1. **Melebih-estimasi sinergi** — integrasi lebih sulit dari proyeksi; penghematan biaya tidak terealisasi penuh
2. **Kesulitan integrasi** — sistem IT, proses operasi, dan budaya tidak mudah digabungkan
3. ***Culture clash*** — perbedaan nilai dan cara kerja yang tidak terselesaikan
4. **Membayar premi terlalu tinggi** — *winner's curse* dalam proses lelang akuisisi
5. **Gangguan manajemen** — eksekutif terlalu fokus pada integrasi, mengabaikan bisnis inti

**Pelajaran untuk manajer Indonesia:** Akuisisi Lippo Group vs. berbagai entitas, GoTo merger (Gojek–Tokopedia) — integrasi teknologi dan budaya perusahaan adalah tantangan nyata yang sering diabaikan dalam euforia pengumuman akuisisi.

![*Concepts & Connections 6.2 — Ekspansi Walmart ke E-Commerce melalui Akuisisi Horizontal*]({walmart})

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.121*

### *Vertical Integration Strategies*

[... existing vertical integration content ...]

#### Empat Keunggulan Integrasi Vertikal (TPGS p.161–162)

1. **Memperkuat keunggulan kompetitif dan diferensiasi** — kontrol atas proses hulu/hilir memungkinkan kualitas konsisten
2. **Mengurangi ketergantungan pada pemasok yang kuat** — eliminasi *supplier power* dalam Five Forces
3. **Mengurangi ketergantungan pada pembeli yang kuat** — kepemilikan saluran distribusi sendiri
4. **Membangun *barriers to entry*** — biaya dan kompleksitas untuk menduplikasi rantai vertikal terintegrasi sangat tinggi

#### Tiga Kelemahan Integrasi Vertikal (TPGS p.163)

1. **Meningkatkan investasi modal dan risiko bisnis** — semakin banyak rantai yang dimiliki, semakin besar eksposur terhadap siklus industri
2. **Membatasi fleksibilitas** — sulit beralih pemasok atau pembeli jika teknologi berubah
3. **Mungkin tidak kompetitif secara biaya** — operasi internal yang tidak efisien bisa lebih mahal dari spesialis eksternal

![*Concepts & Connections 6.3 — Strategi Integrasi Vertikal Tesla*]({tesla})

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.125*

### *Strategic Alliances and Partnerships*

[... existing alliance content ...]

#### Mengapa Aliansi Strategis Gagal (TPGS p.166)

TPGS Ch.6 mengidentifikasi **lima penyebab kegagalan aliansi**:
1. **Tujuan yang berubah seiring waktu** — apa yang diinginkan mitra awalnya berevolusi; kepentingan tidak lagi selaras
2. **Hilangnya sensitivitas kompetitif** — berbagi informasi proprietary menciptakan risiko transfer pengetahuan kepada pesaing
3. ***Free-riding*** — satu pihak mendapat manfaat lebih dari kontribusinya
4. **Ketidakpercayaan dari berbagi pengetahuan** — setelah IP dibagikan, sulit dilindungi kembali
5. **Koordinasi lintas budaya yang sulit** — perbedaan sistem manajemen, bahasa, dan ekspektasi

#### Bahaya Mengandalkan Aliansi untuk Kapabilitas Esensial

**Risiko "pengosongan kapabilitas" (*hollowing out*)** adalah yang paling berbahaya jangka panjang: jika sebuah perusahaan terus-menerus bergantung pada aliansi untuk kapabilitas inti, ia kehilangan kemampuan untuk membangun kembali kapabilitas tersebut secara internal ketika aliansi berakhir (TPGS p.167). **Pelajaran:** aliansi boleh digunakan untuk *akses* kapabilitas, tetapi tidak boleh menggantikan *pembangunan* kapabilitas.

---

## 6. *Blue Ocean Strategy*

[... existing §6 content ...]

![*Concepts & Connections 6.1 — Strategi Blue Ocean Etsy dalam Penjualan Kerajinan Tangan Daring*]({etsy})

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.115*

---

## 7. *Performance Measurement* sebagai Eksekusi

[... existing §7 content ...]

---

## 8. Strategi Kompetitif dan Kinerja: Apa yang Kita Ketahui?

[... existing §8 content ...]

---

## 9. Kesimpulan

[... existing §9 content ...]

---

## 10. Poin-Poin Kunci (TPGS Ch.6)

*Ringkasan resmi dari Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.128*

**LO6-1 — Strategi Ofensif dan Defensif:**
- Serangan kompetitif paling efektif menargetkan kelemahan pesaing, bukan kekuatan mereka
- Strategi defensif bertujuan menurunkan risiko serangan, melemahkan dampaknya, atau mendorong penantang menyerang pesaing lain
- *Signaling* yang kredibel dapat mencegah serangan sebelum dimulai

**LO6-2 — Timing Strategis:**
- Keunggulan *first-mover* paling kuat ketika: kurva belajar curam, *network effects* signifikan, *switching costs* tinggi, dan loyalitas merek terbentuk awal
- *Late-mover* menguntungkan ketika: teknologi masih berevolusi cepat, biaya perintisan tinggi, dan pasar belum siap

**LO6-3 — Cakupan Operasi:**
- M&A horizontal memperkuat posisi pasar tetapi sering gagal karena estimasi sinergi yang berlebihan dan kesulitan integrasi
- Integrasi vertikal memberikan kendali rantai nilai tetapi meningkatkan risiko modal dan mengurangi fleksibilitas
- *Outsourcing* meningkatkan fokus pada kompetensi inti tetapi mengandung risiko *hollowing out* kapabilitas esensial

**LO6-4 — Aliansi dan Kemitraan:**
- Aliansi paling efektif untuk akses cepat ke teknologi, pasar, atau kapabilitas yang akan mahal dan lama jika dibangun sendiri
- Aliansi gagal karena tujuan yang berubah, ketidakpercayaan, *free-riding*, dan kesulitan koordinasi lintas budaya
- Bahaya terbesar: bergantung pada aliansi untuk kapabilitas yang seharusnya dibangun secara internal

**LO6-5 — Sintesis Manajerial:**
- Tidak ada satu formula untuk memperkuat posisi kompetitif — pilihan ofensif/defensif/timing/scope harus disesuaikan dengan situasi industri, posisi relatif, dan sumber daya perusahaan
- Eksekusi strategis memerlukan pengukuran kinerja yang selaras — pilihan strategic moves yang tepat masih gagal tanpa sistem umpan balik yang efektif
"""
```

**Important:** The `[... existing §X content ...]` placeholders in the template above represent where the full content from the existing `generate_submission_w6.py` RMK constant must be inserted verbatim. The implementer must:
1. Read the `RMK` constant from `Dev Assistant/scripts/generate_submission_w6.py`
2. Insert each section's full content at the corresponding placeholder
3. Then add the new content (basis of attack, why M&A fails, vertical integration advantages/disadvantages, failed alliances, hollowing-out risk, Key Points §10) at the specified positions
4. Insert image references at the correct positions

---

### Task 3: Wire up main block and run

**Files:**
- Modify: `Dev Assistant/scripts/generate_rmk6_enhanced.py` (add pipeline + main block)

- [ ] **Step 1: Add pipeline constants and main block**

```python
from pathlib import Path
import subprocess

SCRIPT_DIR   = Path(__file__).parent
PROJECT_ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
EBOOK        = PROJECT_ROOT / "Ebook" / "(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf"
OUT_RMK      = PROJECT_ROOT / "RMK"
TEMP         = PROJECT_ROOT / "Dev Assistant" / "temp"
FIGURES_DIR  = TEMP / "ch6_figures"
REFERENCE    = SCRIPT_DIR / "reference.docx"
PANDOC       = r"C:\Program Files\Pandoc\pandoc.exe"

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
    if not REFERENCE.exists():
        raise FileNotFoundError(f"reference.docx not found at {REFERENCE}")
    if not EBOOK.exists():
        raise FileNotFoundError(f"TPGS ebook not found at {EBOOK}")

    print("Extracting figures from TPGS Ch.6...")
    results = extract_figures(str(EBOOK), FIGURES_DIR)
    validate_figures(results)

    print("Building enhanced RMK content...")
    content = build_rmk_content(FIGURES_DIR)

    md_path = TEMP / "rmk_w6_enhanced.md"
    md_path.write_text(content, encoding="utf-8")

    out_path = OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx"
    pandoc(md_path, out_path)
    print(f"Enhanced RMK size: {out_path.stat().st_size:,} bytes")
    print("Done.")
```

- [ ] **Step 2: Verify syntax**

```bash
python -c "import ast; ast.parse(open(r'D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Dev Assistant\scripts\generate_rmk6_enhanced.py', encoding='utf-8').read()); print('Syntax OK')"
```

Expected: `Syntax OK`

- [ ] **Step 3: Run the script**

```bash
python "Dev Assistant/scripts/generate_rmk6_enhanced.py"
```

Expected output:
```
Extracting figures from TPGS Ch.6...
  OK figure_6_1: XX,XXX bytes
  OK cc_6_1_etsy: XX,XXX bytes
  OK cc_6_2_walmart: XX,XXX bytes
  OK cc_6_3_tesla: XX,XXX bytes
Building enhanced RMK content...
Generated: 01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx
Enhanced RMK size: XX,XXX bytes
Done.
```

- [ ] **Step 4: Verify output size > 50 KB**

```bash
python -c "from pathlib import Path; f=Path(r'D:\DZAKI\S2\Sem. 1\Manajemen Strategik\RMK\01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx'); print(f.name, f.stat().st_size, 'bytes')"
```

Expected: size > 50,000 bytes (images add significant weight over the existing 37 KB).

---

### Task 4: Commit

- [ ] **Step 1: Stage deliverables**

```bash
git add "Dev Assistant/scripts/generate_rmk6_enhanced.py" ^
        "RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx"
```

- [ ] **Step 2: Commit**

```bash
git commit -m "feat(submission): RMK Pert. 6 enhanced — TPGS Ch.6 full audit + Figure 6.1 + C&C 6.1/6.2/6.3 images"
```
