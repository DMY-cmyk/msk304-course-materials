# Design Spec — RMK + CR Submission, Pertemuan 4

- **Assignment:** RMK + CR ke 2 (Tugas Manajemen Strategik Kontemporer)
- **Student:** Dzaki Muhammad Yusfian | NIM: 1125 01079
- **Course:** MST304 — Manajemen Strategik Kontemporer, STIE YKPN
- **Spec date:** 2026-04-23
- **Status:** Approved
- **Analytical depth standard:** Higher than Pertemuan 2 — primary-text engagement required; reach core concepts; open-minded critique; still digestible for S2 Indonesia.

---

## 1. Assignment

Buat RMK dan Critical Review untuk materi dan artikel Pertemuan 4 sesuai silabus.

**Pertemuan 4 topic:** *Evaluating a Company's Resources, Capabilities, and Competitiveness* (TPGS Ch.4 + Henry Ch.4)

**References:**
- TPGS Ch.4 (Gamble, Peteraf & Thompson 2021)
- Henry Ch.4 (Understanding Strategic Management 2021)
- Article 5: Barney (1991), *Firm Resources and Sustained Competitive Advantage*, Journal of Management, 17(1): 99–120
- Article 6: Hao Ma (2000), *Competitive Advantage and Firm Performance*, Competitiveness Review, 10(2): 15–32

---

## 2. Output Files

| # | Filename | Output Path |
|---|----------|-------------|
| 1 | `01079_Dzaki Muhammad Yusfian_RMK Pert. 4.docx` | `course-materials/outputs/RMK/` |
| 2 | `01079_Dzaki Muhammad Yusfian_Artikel 5.docx` | `course-materials/outputs/Critical Thinking of the Article/` |
| 3 | `01079_Dzaki Muhammad Yusfian_Artikel 6.docx` | `course-materials/outputs/Critical Thinking of the Article/` |

---

## 3. Generation Pipeline

**Tool:** Pandoc + Python 3.12 orchestrator (reusing reference.docx from Pertemuan 2)

**Script:** `Dev Assistant/scripts/generate_submission_w4.py`

Same flow as `generate_submission.py`: writes Markdown to `Dev Assistant/temp/`, calls pandoc with `reference.docx`, outputs DOCX to the paths in §2.

**Formatting:** Times New Roman 12pt body; 14pt centered bold Heading 1; 12pt bold Heading 2; 12pt bold italic Heading 3; margins 3cm / 2.5cm; line spacing 1.5; first-line indent 1.25cm.

---

## 4. Document 1 — RMK Pertemuan 4

**Header:** RINGKASAN MATERI KULIAH — PERTEMUAN 4 / MST304 / Dzaki Muhammad Yusfian / NIM: 1125 01079

**Sections:**
1. Pendahuluan — internal analysis as complement to external (Pertemuan 3)
2. Dari SWOT ke *Resource-Based View* — pergeseran paradigmatik
3. Analisis Sumber Daya dan Kapabilitas: Kerangka VRIN/VRIO
4. *Dynamic Capabilities* — respons terhadap lingkungan turbulen
5. Analisis *Value Chain* (Porter 1985) dan *Activity-Based Costing*
6. SWOT yang Diperdalam — dari daftar menjadi analisis strategis
7. Analisis Kekuatan Kompetitif (*Competitive Strength Assessment*)
8. Mendiagnosis Masalah Strategis yang Perlu Ditangani
9. Kesimpulan

**Content sources:** TPGS Ch.4 + Henry Ch.4 + `Dev Assistant/content/week-04/summary/*.md` (reframed as formal akademik prose) + primary articles.

**Depth standard:** Graduate-level synthesis that goes beyond textbook summary — explain *why* each framework emerged (paradigm reaction), *when* it applies, *when* it fails, and *how* it integrates with prior (Pertemuan 3) and later (Pertemuan 5) topics.

---

## 5. Document 2 — Critical Review Artikel 5 (Barney 1991)

**Article:** Jay B. Barney (1991). *Firm Resources and Sustained Competitive Advantage.* Journal of Management, 17(1): 99–120.

**Sections:**
1. Identitas Artikel
2. Tujuan Penelitian dan Posisi dalam Literatur
3. Argumen Utama — Dua Asumsi dan Empat Kriteria
4. Koneksi ke Topik Silabus (Pertemuan 4 — TPGS Ch.4)
5. Kekuatan Artikel
6. Keterbatasan dan Kelemahan
7. Evaluasi Kritis
8. Implikasi bagi Pemahaman Manajemen Strategik
9. Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut

**Depth angles to hit in the CR:**
- The **philosophical shift** from Porter's IO-economics paradigm (homogeneous-mobile resources, industry-structure-drives-performance) to RBV's (heterogeneous-immobile resources, firm-idiosyncratic-endowments-drive-performance).
- The **equilibrium definition** of sustained competitive advantage — not calendar-time, but the cessation of duplication efforts. Why this is both elegant and problematic.
- **Three sources of imperfect imitability** — unique historical conditions (path dependence), causal ambiguity (Lippman & Rumelt), social complexity (Dierickx & Cool). Why social complexity is the most defensible while causal ambiguity contains a paradox.
- **The Priem & Butler (2001) tautology critique**: VRIN-as-definition vs. VRIN-as-prediction. Barney's response and its partial success.
- **The causal ambiguity paradox**: for causal ambiguity to sustain advantage, even the advantaged firm must not fully understand why it is successful. This creates an uncomfortable epistemological position.
- **Extensions and critiques**: dynamic capabilities (Teece, Pisano, Shuen 1997), the knowledge-based view (Grant 1996), the relational view (Dyer & Singh 1998), and how they respond to RBV's static character.
- **Indonesian application**: what passes VRIN legitimately (BCA's CASA franchise — path-dependent social relationship), what doesn't pass (generic "innovation" slogans), and what case evidence shows about the stickiness of VRIN resources under disruption (e.g., why Gudang Garam's brand-distribution asset still holds partial advantage despite cukai pressure).

---

## 6. Document 3 — Critical Review Artikel 6 (Hao Ma 2000)

**Article:** Hao Ma (2000). *Competitive Advantage and Firm Performance.* Competitiveness Review: An International Business Journal, 10(2): 15–32.

**Sections:** Same 9 sections as Document 2.

**Depth angles to hit in the CR:**
- The **tautology diagnosis**: when competitive advantage is used as a surrogate for superior performance, the statement "firms with competitive advantage outperform" becomes definitional and non-falsifiable. Hao Ma's contribution is primarily conceptual hygiene.
- **Three core observations**: (1) CA ≠ performance, (2) CA is relational (requires reference point: against whom, on what), (3) CA is context-specific (fit with environment matters).
- **Discrete vs. compound competitive advantage**: the causal chain is Discrete CA → Compound CA → Performance, with leakage at every transition. Discrete advantage alone is too remote from performance to reliably predict it.
- **Four scenarios where CA does not yield superior performance**: (i) discrete advantage fails to compound, (ii) advantage exists but is not fully exploited (Xerox PARC / GUI), (iii) advantages present but wrong combination (Apple vs. Microsoft, early 1990s), (iv) intentional sacrifice (Microsoft giving AOL preferential treatment for strategic reasons).
- **Superior performance without competitive advantage**: governmental regulation, luck, environmental shock, time-lag of customer goodwill. All raise the question of whether CA is even the right dependent variable.
- **Epistemological depth**: Hao Ma's final move — if performance is the ultimate DV, we must justify why we need CA as an intermediate construct. This question is unresolved and important.
- **Indonesian application**: classic cases of Indonesian firms that have structural advantage but disappointing performance (Garuda Indonesia: flag carrier slot + brand, but cost and governance failures) — and firms that have stellar performance without sustainable advantage (BUMN under regulatory protection with near-monopoly position).

---

## 7. Writing Quality Requirements

- Indonesian akademik; PUEBI/KBBI compliant
- Foreign/English terms italicized on first use per section; Indonesian gloss provided where useful
- No hyphen ("-") as sentence connector; reduplication forms (*kupu - kupu*) use spaced hyphen style per user preference
- No generic AI-sounding phrasing; scholarly voice that reads naturally
- Engagement with primary text (both articles read in full) — direct paraphrase and occasional short quotations with page references where the original phrasing carries force
- Conceptual synthesis over narrative summary; every critique grounded in either textual evidence or cited secondary critic (Priem & Butler, Teece, Peteraf, Grant)
- Indonesian examples drawn from publicly verifiable corporate histories, not fabricated figures

---

## 8. Out of Scope

- Daftar Pustaka (explicitly excluded by user preference, consistent with Pertemuan 2 submission)
- HTML outputs (covered by separate MSK304 spec)
- Articles from other pertemuan
