# RMK + CR Pertemuan 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate three Word documents (RMK Pert. 2, CR Artikel 1, CR Artikel 2) for MST304 Pertemuan 2 submission due 17 April 2026 18:30.

**Architecture:** Python orchestrator writes full Markdown content to temp files, creates a reference.docx Word template via python-docx, then calls Pandoc to convert each Markdown file into a styled DOCX. All code lives in `Dev Assistant/scripts/`.

**Tech Stack:** Python 3.12, python-docx 1.2.0, Pandoc (C:\Program Files\Pandoc\pandoc.exe)

---

### Task 1: Create output directories and verify toolchain

**Files:**
- Run: `Dev Assistant/scripts/` (ensure directory exists)
- Run: `course-materials/outputs/RMK/` (ensure directory exists)
- Run: `course-materials/outputs/Critical Thinking of the Article/` (ensure directory exists)

- [ ] **Step 1: Create required directories**

```bash
mkdir -p "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Dev Assistant\scripts"
mkdir -p "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Dev Assistant\temp"
mkdir -p "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\RMK"
mkdir -p "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\Critical Thinking of the Article"
```

- [ ] **Step 2: Verify pandoc is accessible**

```bash
"C:\Program Files\Pandoc\pandoc.exe" --version
```

Expected: first line `pandoc 3.x.x`

- [ ] **Step 3: Verify python-docx is installed**

```bash
python -c "import docx; print('OK', docx.__version__)"
```

Expected: `OK 1.2.0`

---

### Task 2: Create generate_submission.py

**Files:**
- Create: `Dev Assistant/scripts/generate_submission.py`

- [ ] **Step 1: Write the complete script**

Create `D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Dev Assistant\scripts\generate_submission.py` with the content in the Implementation Notes section below.

- [ ] **Step 2: Verify the file was written**

```bash
python -c "import ast, sys; ast.parse(open('Dev Assistant/scripts/generate_submission.py').read()); print('Syntax OK')"
```

Expected: `Syntax OK`

---

### Task 3: Run script and verify outputs

- [ ] **Step 1: Run the generator**

```bash
cd "D:\DZAKI\S2\Sem. 1\Manajemen Strategik"
python "Dev Assistant/scripts/generate_submission.py"
```

Expected output:
```
Created reference.docx
Generated: 01079_Dzaki Muhammad Yusfian_RMK Pert. 2.docx
Generated: 01079_Dzaki Muhammad Yusfian_Artikel 1.docx
Generated: 01079_Dzaki Muhammad Yusfian_Artikel 2.docx
All three documents generated successfully.
```

- [ ] **Step 2: Verify file sizes**

```bash
ls -lh "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\RMK\"
ls -lh "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\Critical Thinking of the Article\"
```

Expected: all three `.docx` files present, each > 20 KB.

---

### Task 4: Commit

- [ ] **Step 1: Stage and commit outputs**

```bash
cd "D:\DZAKI\S2\Sem. 1\Manajemen Strategik"
git add "Dev Assistant/scripts/generate_submission.py"
git add "course-materials/outputs/RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 2.docx"
git add "course-materials/outputs/Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 1.docx"
git add "course-materials/outputs/Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 2.docx"
git add "docs/superpowers/plans/2026-04-17-rmk-cr-pertemuan2.md"
git add "docs/superpowers/specs/2026-04-17-rmk-cr-pertemuan2-design.md"
git commit -m "feat(submission): RMK + CR Pertemuan 2 — three Word documents for 17 Apr 18:30 deadline"
```

---

## Implementation Notes — Full Script Content

See `Dev Assistant/scripts/generate_submission.py` (created in Task 2).

Content sources used:
- TPGS Ch.2 (Gamble, Peteraf & Thompson 2021)
- Altıok (2011) — Article 1 full PDF
- Mohamed et al. (2019) — Article 2 full PDF
- `Dev Assistant/content/week-02/summary/*.md`
- `Dev Assistant/content/week-02/article/*.md`
