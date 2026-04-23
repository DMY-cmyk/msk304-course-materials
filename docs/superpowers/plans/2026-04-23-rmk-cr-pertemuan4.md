# RMK + CR Pertemuan 4 Implementation Plan

> **For agentic workers:** Execute inline via superpowers:executing-plans. Same pipeline as Pertemuan 2 submission; content is new.

**Goal:** Generate three Word documents (RMK Pert. 4, CR Artikel 5, CR Artikel 6) with graduate-level analytical depth.

**Architecture:** Python orchestrator writes full Markdown content to temp files, reuses existing `reference.docx`, calls Pandoc to convert each to DOCX. All code in `Dev Assistant/scripts/`.

**Tech Stack:** Python 3.12, python-docx 1.2.0 (installed), Pandoc (installed).

---

### Task 1: Create generate_submission_w4.py

**File:** `Dev Assistant/scripts/generate_submission_w4.py`

- [ ] Embed full Markdown content for RMK Pert. 4 (9 sections, TPGS Ch.4 synthesis)
- [ ] Embed full Markdown for CR Artikel 5 (Barney 1991) with depth angles from spec §5
- [ ] Embed full Markdown for CR Artikel 6 (Hao Ma 2000) with depth angles from spec §6
- [ ] Reuse `reference.docx` from Pertemuan 2 script
- [ ] Call pandoc for each of the three documents

### Task 2: Run and verify

- [ ] Execute: `python "Dev Assistant/scripts/generate_submission_w4.py"`
- [ ] Verify: three DOCX files exist in the correct folders, each > 25 KB

### Task 3: Commit

- [ ] `git add` the script + 3 DOCX + spec + plan
- [ ] Commit message: `feat(submission): RMK + CR Pertemuan 4 — deep analysis of Barney 1991 & Hao Ma 2000`
