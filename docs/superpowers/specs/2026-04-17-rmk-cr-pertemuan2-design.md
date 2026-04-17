# Design Spec — RMK + CR Submission, Pertemuan 2

- **Assignment:** RMK + CR ke 1 (Tugas Manajemen Strategik Kontemporer)
- **Deadline:** Jumat, 17 April 2026, 18:30
- **Student:** Dzaki Muhammad Yusfian | NIM: 1125 01079
- **Course:** MST304 — Manajemen Strategik Kontemporer, STIE YKPN
- **Spec date:** 2026-04-17
- **Status:** Approved

---

## 1. Assignment

From `Tugas Pert 1.jpeg`:
> "Buat Ringkasan Materi Kuliah Dan Reviu Kritis Materi Dan Artikel Pertemuan 2 Sesuai Silabus."

**Pertemuan 2 topic (from syllabus):** *The Managerial Process of Crafting and Executing Strategy*
**References:** TPGS Ch.2 + Article 1 (Altıok 2011) + Article 2 (Mohamed et al. 2019)

---

## 2. Output Files

| # | Filename | Output Path |
|---|----------|-------------|
| 1 | `01079_Dzaki Muhammad Yusfian_RMK Pert. 2.docx` | `course-materials/outputs/RMK/` |
| 2 | `01079_Dzaki Muhammad Yusfian_Artikel 1.docx` | `course-materials/outputs/Critical Thinking of the Article/` |
| 3 | `01079_Dzaki Muhammad Yusfian_Artikel 2.docx` | `course-materials/outputs/Critical Thinking of the Article/` |

---

## 3. Generation Pipeline

**Tool:** Pandoc (installed at `C:\Program Files\Pandoc\pandoc.exe`) + Python 3.12 orchestrator

**Script location:** `Dev Assistant/scripts/generate_submission.py`

**Flow:**
1. Script writes three Markdown files to `Dev Assistant/temp/`
2. Script writes `Dev Assistant/scripts/reference.docx` (Word template) via python-docx
3. Script calls `pandoc <input.md> --reference-doc=reference.docx -o <output.docx>` for each
4. Outputs land in the paths specified in §2

**Formatting spec (reference.docx):**
- Font: Times New Roman 12pt body; 14pt bold Heading 1; 12pt bold Heading 2
- Margins: 3cm left/top, 2.5cm right/bottom
- Line spacing: 1.5
- First-line paragraph indent: 1.25cm
- Header: course name + student name (right-aligned)

---

## 4. Document 1 — RMK Pertemuan 2

**Header block:** RINGKASAN MATERI KULIAH — PERTEMUAN 2 / MST304 / Dzaki Muhammad Yusfian / NIM: 1125 01079

**Sections:**
1. Pendahuluan
2. Proses Manajerial Pembuatan dan Eksekusi Strategi: Tinjauan Umum
3. Tahap 1 — Visi Strategis, Misi, dan Nilai Inti
4. Tahap 2 — Penetapan Tujuan
5. Tahap 3 — Perumusan Strategi: Tiga Level
6. Tahap 4 — Implementasi dan Eksekusi Strategi
7. Tahap 5 — Evaluasi dan Penyesuaian
8. Tata Kelola Perusahaan (*Corporate Governance*)
9. Kesimpulan

**Content source:** `Dev Assistant/content/week-02/summary/*.md` (all 5 files)

**Writing standard:** Indonesian akademik; PUEBI/KBBI; foreign terms italicized; no AI-generic phrasing; reads as a serious graduate-level lecture summary written by a reflective student-researcher.

---

## 5. Document 2 — Critical Review Artikel 1 (Altıok 2011)

**Article:** Pınar Altıok (2011). *Applicable Vision, Mission and the Effects of Strategic Management on Crisis Resolve.* Procedia Social and Behavioral Sciences, 24, 61–71.

**Header block:** CRITICAL REVIEW ARTIKEL 1 / MST304 / Dzaki Muhammad Yusfian / NIM: 1125 01079

**Sections:**
1. Identitas Artikel
2. Tujuan Penelitian
3. Argumen Utama
4. Koneksi ke Topik Silabus (Pertemuan 2 — TPGS Ch.2)
5. Kekuatan Artikel
6. Keterbatasan dan Kelemahan
7. Evaluasi Kritis
8. Implikasi bagi Pemahaman Manajemen Strategik
9. Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut

**Content source:** `Dev Assistant/content/week-02/article/01-altiok-vision-crisis.md` + full article PDF (read)

**Critical stance:** Evaluate Altıok's conceptual paper honestly — acknowledge its contribution (applicable vision as crisis-resolve capability) while pressing on the absence of empirical testing, weak operationalization, and Turkish-context generalizability limits.

---

## 6. Document 3 — Critical Review Artikel 2 (Mohamed et al. 2019)

**Article:** Mohamed, F., Nusari, M., Ameen, A., Raju, V., & Bhaumik, A. (2019). *Towards a Better Understanding of the Relationship between Strategy Formulation (Vision, Mission, and Goals) and Organizational Performance.* Test Engineering and Management, 81, 1987–1994.

**Header block:** CRITICAL REVIEW ARTIKEL 2 / MST304 / Dzaki Muhammad Yusfian / NIM: 1125 01079

**Sections:** Same 9 sections as Document 2.

**Content source:** `Dev Assistant/content/week-02/article/02-mohamed-vm-performance.md` + full article PDF (read)

**Critical stance:** Acknowledge the PLS-SEM empirical rigor and public-sector extension while pressing on cross-sectional causality limits, single-context generalizability, self-reported performance bias, and the gap between measuring VMG *presence* vs. Altıok's *applicability* quality.

---

## 7. Writing Quality Requirements

- Indonesian akademik; PUEBI and KBBI compliant
- Foreign/English terms italicized on first use per section
- No hyphen (-) as sentence connector
- No generic AI-sounding phrasing; natural scholarly voice
- Graduate-level: synthesis over summary, critical judgment over description
- Lecturer perspective: write as if you understand what strong submissions look like from the other side of the desk

---

## 8. Out of Scope

- Daftar Pustaka (explicitly excluded by user)
- Slide decks
- HTML outputs (covered by separate MSK304 spec)
- Articles 3–4 (Pertemuan 3 assignment, not due today)
