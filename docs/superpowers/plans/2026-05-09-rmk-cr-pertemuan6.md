# RMK + CR Pertemuan 6 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate three Word documents (RMK Pert. 6, CR Artikel 9, CR Artikel 10) with graduate-level analytical depth and rich sub-heading/bold/italic formatting so they function as dense reference materials.

**Architecture:** Python orchestrator (`generate_submission_w6.py`) embeds full Markdown for three documents, reuses `reference.docx` from Pertemuan 2, calls Pandoc per file. Identical pipeline to `generate_submission_w5.py` — only the three content constants change.

**Tech Stack:** Python 3.12, python-docx 1.2.0 (installed), Pandoc (`C:\Program Files\Pandoc\pandoc.exe`).

---

### Task 1: Read primary sources

**Files (read-only):**
- `Article/Artikel 9.pdf` — Teeratansirikool et al. (2013)
- `Article/Artikel 10.pdf` — Onditi (2018)
- `Dev Assistant/content/week-06/summary/*.md` — RMK content sources
- `Dev Assistant/content/week-06/article/*.md` — existing CR analyses

- [ ] Read `Article/Artikel 9.pdf` in full; capture three hypotheses (H1/H2/H3), SEM-PLS methodology, key findings, and page references for direct quotation
- [ ] Read `Article/Artikel 10.pdf` in full; capture three synthesis themes, literature covered, gaps identified, and page references
- [ ] Skim week-06 summary markdown for reusable framings (reframe into formal akademik prose — do not copy verbatim)

---

### Task 2: Create `generate_submission_w6.py`

**Files:**
- Create: `Dev Assistant/scripts/generate_submission_w6.py`
- Reference (structure only): `Dev Assistant/scripts/generate_submission_w5.py`

- [ ] **Step 1: Set pipeline boilerplate (copy from w5, update filenames only)**

```python
from pathlib import Path
import subprocess

SCRIPT_DIR   = Path(__file__).parent
PROJECT_ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
OUT_RMK      = PROJECT_ROOT / "RMK"
OUT_CR       = PROJECT_ROOT / "Critical Thinking of the Article"
TEMP         = PROJECT_ROOT / "Dev Assistant" / "temp"
REFERENCE    = SCRIPT_DIR / "reference.docx"
PANDOC       = r"C:\Program Files\Pandoc\pandoc.exe"

def pandoc(md: Path, out: Path):
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
    for name, content, out in [
        ("rmk_w6.md", RMK, OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx"),
        ("cr9.md",    CR9, OUT_CR  / "01079_Dzaki Muhammad Yusfian_Artikel 9.docx"),
        ("cr10.md",   CR10, OUT_CR / "01079_Dzaki Muhammad Yusfian_Artikel 10.docx"),
    ]:
        md = TEMP / name
        md.write_text(content, encoding="utf-8")
        pandoc(md, out)
    print("All three documents generated successfully.")
    print(f"RMK : {OUT_RMK}")
    print(f"CR  : {OUT_CR}")
```

- [ ] **Step 2: Embed `RMK` constant — Ringkasan Materi Kuliah Pertemuan 6**

Full header:
```markdown
# RINGKASAN MATERI KULIAH — PERTEMUAN 6

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer
**Topik:** *Strengthening a Company's Competitive Position: Strategic Moves, Timing, and Scope of Operations* (TPGS Ch.6 + Henry Ch.5–6)
**Mahasiswa:** Dzaki Muhammad Yusfian
**NIM:** 1125 01079
```

9 sections with rich formatting per spec §4 — each section uses ### sub-headings, **bold** for critical reasoning, *italics* for foreign terms. Minimum 2–5 sub-headings per section, each sub-section 150–300 words.

Content per section:
1. **Pendahuluan** — transisi Pert. 5 → Pert. 6; pertanyaan inti; sub-heading: the execution gap
2. **Offensive Strategies** — frontal attack, flanking, guerrilla, preemptive; kapan menyerang vs. mengisi celah; bold: resource-superiority rule; Indonesia: Tokopedia vs. Shopee; Gojek flanking Grab
3. **Defensive Strategies** — fortify-and-defend, signaling (credibility theory, Schelling 1960), mobile defense, counteroffensive; bold: kapan passive defense gagal; Indonesia: Sampoerna brand architecture; BCA CASA moat
4. **Timing Strategies** — 5 FMA mechanisms (learning curve, resource pre-emption, network effects, brand loyalty, switching-cost lock-in) each analyzed; 3 FMD (pioneer costs, technological uncertainty, market education burden); fast-follower logic (Samsung vs. Apple; Microsoft vs. Netscape); Indonesia: Gojek first-mover; Grab fast-follower; OVO fast-follower e-wallet
5. **Scope of Operations** — vertical integration (backward/forward), outsourcing (hollowing-out risk), alliances & JV, M&A; Williamson (1975) TCE make-or-buy; Indonesia: Pertamina backward integration; Astra International alliance network; GoTo merger; Telkom vertical integration
6. **Blue Ocean Strategy** — Kim & Mauborgne (2005) value innovation; ERRC grid; bold: critique (blue ocean = first-mover red ocean?); counter-counter-argument linking to McGrath transient advantage; Indonesia: Kopi Kenangan; Ruangguru
7. **Performance Measurement sebagai Eksekusi** — BSC 4 perspectives; strategy maps; bold: execution gap evidence (Kaplan & Norton empirical); jembatan ke Teeratansirikool; Indonesia: Bank Mandiri BSC; Pertamina KPI cascade
8. **Strategi Kompetitif dan Kinerja** — what is settled (Campbell-Hunt 2000); what is contested; moderating variables; jembatan ke Onditi; Indonesia: BCA differentiation; Indomaret cost leadership
9. **Kesimpulan** — strategy as continuous calibration; integration chain Pert. 4–6 (RBV → generik → penguatan); forward to Pert. 7 corporate-level

- [ ] **Step 3: Embed `CR9` constant — Critical Review Artikel 9 (Teeratansirikool et al. 2013)**

Full header:
```markdown
# CRITICAL REVIEW — ARTIKEL 9

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer
**Mahasiswa:** Dzaki Muhammad Yusfian
**NIM:** 1125 01079

## 1. Identitas Artikel

**Penulis:** Luliya Teeratansirikool, Sununta Siengthai, Yuosre Badir, Chotchai Charoenngam
**Tahun:** 2013/2014
**Judul:** *Competitive Strategies and Firm Performance: The Mediating Role of Performance Measurement*
**Jurnal:** International Journal of Productivity and Performance Management, Vol. 63, Issue 1/2, pp. 168–184
**Institusi:** Asian Institute of Technology, Thailand
**Tipe Riset:** Empiris kuantitatif — SEM-PLS dengan data 117 perusahaan tercatat di Thailand (SET)
```

9 sections with rich formatting per spec §5:
1. Identitas (as above)
2. Tujuan & Posisi — research question; gap filled (strategy→performance previously treated as direct; paper argues indirect via PMS); position relative to Kaplan & Norton (1992, 1996), Neely et al. (1995), Bourne et al. (2000)
3. Argumen Utama — H1 (strategy→PMS, grounded in information processing theory / Galbraith 1974); H2 (PMS→performance, grounded in BSC lineage); H3 (mediation claim, most ambitious and most vulnerable); SEM-PLS rationale
4. Koneksi Silabus — PMS as execution infrastructure for TPGS Ch.6 strategic moves; without PMS alignment, strategic moves lose feedback loop
5. Kekuatan — genuine theoretical contribution (PMS in causal chain); adequate SEM-PLS sample; practical implications for PMS-strategy co-design
6. Keterbatasan — endogeneity problem (most important: firms good at strategy both build better PMS AND perform better — common-cause problem); Thailand-only SET sample; construct validity of strategy operationalization; cross-sectional causal-direction problem; common method variance
7. Evaluasi Kritis — Baron & Kenny (1986) vs. bootstrapping (Preacher & Hayes) mediation criteria; core critique: partial mediation is consistent with both "PMS is genuine mediator" AND "common organizational capability drives both" — paper cannot distinguish; what longitudinal/IV design would have been needed; net assessment
8. Implikasi — theoretical (PMS in causal chain); managerial (strategy+measurement co-design); Indonesian: Bank Mandiri BSC post-recapitalization; Pertamina KPI cascade under energy reform; state-ownership KPI distortion problem
9. Isu Diskusi — PMS mediator vs. moderator distinction; SME applicability; digital OKR dashboarding; Indonesian SOE political KPI problem

- [ ] **Step 4: Embed `CR10` constant — Critical Review Artikel 10 (Onditi 2018)**

Full header:
```markdown
# CRITICAL REVIEW — ARTIKEL 10

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer
**Mahasiswa:** Dzaki Muhammad Yusfian
**NIM:** 1125 01079

## 1. Identitas Artikel

**Penulis:** E. O. Onditi
**Tahun:** 2018
**Judul:** *Competitive Strategies and Firm Performance: A Review of Literature*
**Jurnal:** Strategic Journals, Vol. 5, Issue 4, pp. 1869–1879
**Tipe Riset:** Literature review (narasi) tanpa meta-analisis kuantitatif
```

9 sections with rich formatting per spec §6:
1. Identitas (as above)
2. Tujuan & Posisi — cumulative knowledge question; position relative to Campbell-Hunt (2000) meta-analysis; Dess & Davis (1984); Hambrick (1983); why 2018 review adds value (post-2000 empirical coverage)
3. Argumen Utama — Theme 1 (generic strategies vs. performance: clarity beats ambiguity); Theme 2 (industry context as moderator); Theme 3 (implementation and execution quality as underappreciated variable)
4. Koneksi Silabus — validates TPGS Ch.6 argument; Onditi's execution theme links to Teeratansirikool mediation argument
5. Kekuatan — post-2000 coverage; practitioner accessibility; gap identification
6. Keterbatasan — descriptive not analytical synthesis (core weakness); Africa-heavy empirical base (Kenya, Ghana, Nigeria → limited ASEAN/East Asia generalizability); Khanna & Palepu (2000) institutional voids not engaged; Fine (1998) industry clock-speed absent; no effect-size meta-analysis; measurement artifact problem (Kotha & Vadlamani 1995) not addressed
7. Evaluasi Kritis — central critique: Onditi accurately reports conflict but does not adjudicate why studies conflict; Campbell-Hunt (2000) comparison (more rigorous at 40% length); measurement artifact problem undermines both confirming and disconfirming studies; straw-man framing; net assessment: useful literature map, weak theoretical synthesis
8. Implikasi — theoretical (strategy→performance literature has data but limited cumulative insight — moderators underspecified); Indonesian research gap (almost no rigorous empirical studies on Indonesian firms with validated constructs and longitudinal design); Indonesian cases vs. global predictions: Astra International (diversified conglomerate — what strategy type?); BCA differentiation; Indofood cost leadership; Telkom under state-ownership objectives
9. Isu Diskusi — digital disruption's effect on strategy–performance link; Indonesian institutional voids as research context; Porter typology vs. Miles & Snow vs. Treacy & Wiersema validity; microfoundations (Teece 2007)

- [ ] **Step 5: Verify Python syntax**

```bash
python -c "import ast; ast.parse(open(r'D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Dev Assistant\scripts\generate_submission_w6.py', encoding='utf-8').read()); print('Syntax OK')"
```

Expected: `Syntax OK`

---

### Task 3: Run script and verify outputs

- [ ] **Step 1: Execute the script**

```bash
python "Dev Assistant/scripts/generate_submission_w6.py"
```

Expected:
```
Generated: 01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx
Generated: 01079_Dzaki Muhammad Yusfian_Artikel 9.docx
Generated: 01079_Dzaki Muhammad Yusfian_Artikel 10.docx
All three documents generated successfully.
RMK : D:\DZAKI\S2\Sem. 1\Manajemen Strategik\RMK
CR  : D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Critical Thinking of the Article
```

- [ ] **Step 2: Verify all three files exist and each > 25 KB**

```bash
python -c "
from pathlib import Path
root = Path(r'D:\DZAKI\S2\Sem. 1\Manajemen Strategik')
files = [
    root / 'RMK' / '01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx',
    root / 'Critical Thinking of the Article' / '01079_Dzaki Muhammad Yusfian_Artikel 9.docx',
    root / 'Critical Thinking of the Article' / '01079_Dzaki Muhammad Yusfian_Artikel 10.docx',
]
for f in files:
    size = f.stat().st_size if f.exists() else 'MISSING'
    print(f.name, ':', size)
"
```

Expected: all three files present, each ≥ 25000 bytes.

---

### Task 4: Commit

- [ ] **Step 1: Stage all deliverables**

```bash
git add "Dev Assistant/scripts/generate_submission_w6.py" ^
        "RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx" ^
        "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 9.docx" ^
        "Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 10.docx" ^
        "docs/superpowers/plans/2026-05-09-rmk-cr-pertemuan6.md"
```

- [ ] **Step 2: Commit**

```bash
git commit -m "feat(submission): RMK + CR Pertemuan 6 — Teeratansirikool 2013 & Onditi 2018, PMS mediation & strategy-performance synthesis"
```
