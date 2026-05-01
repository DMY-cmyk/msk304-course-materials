# RMK + CR Pertemuan 5 Implementation Plan

> **For agentic workers:** Execute inline via superpowers:executing-plans. Same pipeline as Pertemuan 4 submission; content is new.

**Goal:** Generate three Word documents (RMK Pert. 5, CR Artikel 7, CR Artikel 8) with graduate-level analytical depth — paradigmatic critique + Indonesian applications.

**Architecture:** Python orchestrator embeds full Markdown content for the three documents, reuses existing `reference.docx` from Pertemuan 2, calls Pandoc to convert each to DOCX. All code in `Dev Assistant/scripts/`.

**Tech Stack:** Python 3.12, python-docx 1.2.0 (installed), Pandoc (`C:\Program Files\Pandoc\pandoc.exe`).

---

### Task 1: Read primary sources

**Files (read-only):**
- `Article/Artikel 7.pdf` — Salavou (2015)
- `Article/Artikel 8.pdf` — Adom, Nyarko & Som (2016)
- `Dev Assistant/content/week-05/summary/*.md` — RMK content sources
- `Dev Assistant/content/week-05/article/*.md` — existing CR analyses

- [ ] Read Artikel 7.pdf in full; capture Salavou's three pergeseran with page references
- [ ] Read Artikel 8.pdf in full; capture Adom et al.'s arguments with page references
- [ ] Skim week-05 summary markdown to identify reusable framings (no copy-paste; reframe)

### Task 2: Create generate_submission_w5.py

**Files:**
- Create: `Dev Assistant/scripts/generate_submission_w5.py`

- [ ] **Step 1: Copy structure from `generate_submission_w4.py`**

Use the existing script's pipeline (REFERENCE path, OUT_RMK, OUT_CR, pandoc helper) verbatim. Only the three content constants change.

- [ ] **Step 2: Set output paths**

```python
PROJECT_ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
OUT_RMK      = PROJECT_ROOT / "RMK"
OUT_CR       = PROJECT_ROOT / "Critical Thinking of the Article"
TEMP         = PROJECT_ROOT / "Dev Assistant" / "temp"
REFERENCE    = PROJECT_ROOT / "Dev Assistant" / "scripts" / "reference.docx"
PANDOC       = r"C:\Program Files\Pandoc\pandoc.exe"
```

- [ ] **Step 3: Embed RMK Pert. 5 Markdown (9 sections)**

Sections per spec §4:
1. Pendahuluan (transisi dari Pert. 4 RBV ke Pert. 5 pilihan posisi)
2. Akar Konseptual — Porter (1980, 1985); reaksi terhadap SCP paradigm
3. Lima Strategi Generik — five-cell elaboration with logika ekonomis
4. *Stuck in the Middle* — Porter's argument + Hill (1988), Miller (1992), Campbell-Hunt (2000) critiques
5. Strategi Hybrid dan Dinamis — Treacy & Wiersema, D'Aveni, McGrath, Salavou jembatan
6. Pilihan Strategi × Lima Kekuatan — kapan tiap strategi bekerja, kapan gagal
7. Analisis Pesaing — Porter Ch.3 four-cell, strategic groups, blindspots; Adom jembatan
8. Risiko Pelaksanaan — strategy decay, imitasi, strategic drift (Johnson 1988)
9. Kesimpulan — moving baseline, integrasi Pert. 4–6

Indonesian examples to include: Indomaret–Alfamart, AirAsia, Garuda, Gojek–Grab, Indofood–Wings, BCA–Mandiri, Tokopedia–Shopee.

Header: `RINGKASAN MATERI KULIAH — PERTEMUAN 5 / MST304 / Dzaki Muhammad Yusfian / NIM: 1125 01079`

- [ ] **Step 4: Embed CR Artikel 7 Markdown (9 sections, depth angles per spec §5)**

Sections: Identitas → Tujuan & Posisi → Argumen Utama → Koneksi Silabus → Kekuatan → Keterbatasan → Evaluasi Kritis → Implikasi → Isu Diskusi.

Depth angles: paradigm-shift framing (Porter mutually exclusive vs. hybrid empirics — Hill, Miller, Campbell-Hunt); static-to-dynamic (Teece, D'Aveni, McGrath); coopetition (Brandenburger & Nalebuff); Treacy & Wiersema parallel typology; orisinalitas critique; methodological limits.

Indonesian applications: Indomaret–Alfamart hybrid, GoTo merger as coopetition→integration, AirAsia focused→broad shift, Tokopedia–Shopee transient advantage.

- [ ] **Step 5: Embed CR Artikel 8 Markdown (9 sections, depth angles per spec §6)**

Same 9 sections.

Depth angles: epistemic-utility shift (acquisition→sense-making→prediction); cognitive-strategy critique (Zajac & Bazerman, Porac & Thomas, Reger & Huff); Porter Ch.3 four-cell with focus on assumptions; Fleisher & Bensoussan toolkit; African field-evidence generalizability; central critique that Adom et al. answer a strawman.

Indonesian applications: BCA vs Mandiri monitoring, Indofood reading Wings, e-commerce price-tracking, Garuda's pre-AirAsia blindspot.

- [ ] **Step 6: Use the same `pandoc(md, out)` helper from w4 script**

```python
def pandoc(md: Path, out: Path):
    result = subprocess.run(
        [PANDOC, str(md), f"--reference-doc={REFERENCE}", "-o", str(out)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    print(f"Generated: {out.name}")
```

- [ ] **Step 7: Main block writes 3 temp .md files and converts each**

```python
if __name__ == "__main__":
    TEMP.mkdir(parents=True, exist_ok=True)
    OUT_RMK.mkdir(parents=True, exist_ok=True)
    OUT_CR.mkdir(parents=True, exist_ok=True)
    for name, content, out in [
        ("rmk_w5.md", RMK, OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 5.docx"),
        ("cr7.md",    CR7, OUT_CR  / "01079_Dzaki Muhammad Yusfian_Artikel 7.docx"),
        ("cr8.md",    CR8, OUT_CR  / "01079_Dzaki Muhammad Yusfian_Artikel 8.docx"),
    ]:
        md = TEMP / name
        md.write_text(content, encoding="utf-8")
        pandoc(md, out)
    print("All three documents generated successfully.")
```

- [ ] **Step 8: Verify syntax**

```bash
python -c "import ast; ast.parse(open('Dev Assistant/scripts/generate_submission_w5.py', encoding='utf-8').read()); print('OK')"
```

Expected: `OK`

### Task 3: Run and verify outputs

- [ ] **Step 1: Execute the script**

```bash
python "Dev Assistant/scripts/generate_submission_w5.py"
```

Expected:
```
Generated: 01079_Dzaki Muhammad Yusfian_RMK Pert. 5.docx
Generated: 01079_Dzaki Muhammad Yusfian_Artikel 7.docx
Generated: 01079_Dzaki Muhammad Yusfian_Artikel 8.docx
All three documents generated successfully.
```

- [ ] **Step 2: Verify all three files exist with size > 25 KB**

```bash
python -c "from pathlib import Path; root=Path(r'D:\DZAKI\S2\Sem. 1\Manajemen Strategik'); files=[root/'RMK'/'01079_Dzaki Muhammad Yusfian_RMK Pert. 5.docx', root/'Critical Thinking of the Article'/'01079_Dzaki Muhammad Yusfian_Artikel 7.docx', root/'Critical Thinking of the Article'/'01079_Dzaki Muhammad Yusfian_Artikel 8.docx']; [print(f.name, f.stat().st_size) for f in files]"
```

Expected: each size ≥ 25000 bytes.

### Task 4: Commit

- [ ] **Step 1: Stage script + 3 DOCX + spec + plan**

```bash
git add "Dev Assistant/scripts/generate_submission_w5.py" \
        "RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 5.docx" \
        "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 7.docx" \
        "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 8.docx" \
        "docs/superpowers/plans/2026-05-01-rmk-cr-pertemuan5.md"
```

- [ ] **Step 2: Commit**

```
feat(submission): RMK + CR Pertemuan 5 — Salavou 2015 & Adom et al. 2016, hybrid/dynamic/coopetition critique
```
