# MST304 — RMK Pertemuan 8 + Critical Reviews (Artikel 13 & 14)

## Task (Temu 8 — TPGS Ch. 7, "Strategies for Competing in International Markets")

Produce THREE submission-ready Word documents, from scratch:

1. `01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx` — complete RMK of TPGS Ch. 7 with **every chapter figure/table embedded inline** beside its explanation (cropped from PDF, sized to fit).
2. `01079_Dzaki Muhammad Yusfian_Artikel 13.docx` — Critical Review of Kostruba & Kostruba (2025), *Strategies for Companies to Enter International Markets*, Sci. Annals of the Danube Delta Institute 16(2), 154–175. Must link back to Ch. 7.
3. `01079_Dzaki Muhammad Yusfian_Artikel 14.docx` — Critical Review of Gregory, Li & Solanki (2026), *Executive Insights in the Age of AI and Global Disruption*, J. of International Marketing 34(1), 34–46. Must link back to Ch. 7.

**Student identity (every document, first page):** Dzaki Muhammad Yusfian — NIM 01079. Never lose this.

## Source paths (ACTUAL, differs from master-prompt `sources/` tree)

| Source | Actual path |
|---|---|
| TPGS Ch. 7 (RMK body — ONLY source) | `TPGS-21Ed-2018-Crafting and Executing Strategy Concepts (Temu 8 - 14).pdf` (repo root) |
| Artikel 13 | `Article/Artikel 13.pdf` |
| Artikel 14 | `Article/Artikel 14.pdf` |
| Syllabus (Pasca UTS) | `Silabus MSK TA 2025-2026-efg (Pasca UTS).pdf` (repo root) |

## Output convention

Repo convention from Pert. 2–7: RMK → `RMK/`, reviews → `Critical Thinking of the Article/`.
Master prompt says `output/`. **Confirm destination in Phase 1.** Filenames are fixed verbatim (above).

## Format rules (proposed defaults — LOCK in Phase 1, then they are gates)

Established convention from Pert. 2–7 (see `docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md`):
A4 · 1.5 line spacing · Times New Roman 12 pt body · H1 14 pt centered bold · margins 3 cm / 2.5 cm · first-line indent 1.25 cm · figure captions centered 11 pt italic (*Gambar N. Judul (Sumber: …, hlm. X)*) · academic Bahasa Indonesia with English technical terms preserved.

## Hard requirements

- **Every** TPGS Ch. 7 figure/table/diagram embedded in the RMK, captioned, in-margin, adjacent to its explanation. Build figure inventory in Phase 0 — do NOT hardcode figure numbers.
- Every Ch. 7 concept covered (Phase 0 concept inventory is the completeness baseline).
- Each review: summary → framing/method → findings → critical appraisal → explicit Ch. 7 linkage → implications; genuinely critical, S2 depth, professor-led voice.
- **Artikel 14 notice:** its copyright page restricts AI/ML use. Approach: human-style critical review with proper citation — summarize/critique in own words, NO extended verbatim reproduction, embed its figures only as attributed exhibits. Flag to user in Phase 1.
- Faithfulness: no invented page numbers or content; RMK body uses ONLY Ch. 7.

## Tooling (validated across Pert. 2–7)

- Figure extraction: PyMuPDF (`fitz`) anchor-search → clip → PNG (200–300 DPI). See `Dev Assistant/scripts/generate_submission_w7.py`.
- DOCX build: Markdown → Pandoc 3.9 (`C:\Program Files\Pandoc\pandoc.exe`) with `Dev Assistant/scripts/reference.docx`.
- Master prompt proposes a Rust-default pipeline; Rust toolchain available (cargo 1.94, poppler 24.04). Resolve Rust-vs-established-Python in Phase 1 (docx authoring is the documented Python exception either way).

## Phase sequence (master prompt — execute in order)

0. Ingestion audit → `analysis/` (ch7-concept-inventory, ch7-figure-map, artikel13-brief, artikel14-brief, syllabus-context, build-input)
1. Brainstorming + Visual Companion previews (4 classes: font, figure placement, section layout, review skeleton) → `specs/deliverables-spec.md`; lock format rules; flag Artikel-14 notice
2. Git worktree + scaffold
3. Content plan → `plans/build-plan.md`; 3.5 Extract & crop figures → `content/figures/` + manifest
4. Section-by-section authoring (rubric-first), two-stage review
5. Validate (coverage + figures + format) → `output/VALIDATION-REPORT.md`; deliver
