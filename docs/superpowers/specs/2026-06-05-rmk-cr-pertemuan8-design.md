# Design Spec — RMK Pertemuan 8 + Critical Review Artikel 13 & 14 (MST304, Temu 8)

**Date:** 2026-06-05 · **Student:** Dzaki Muhammad Yusfian (NIM 01079) · **Status:** Approved (Phase 1, all four decisions on recommended defaults)

## Deliverables (exact filenames)

| Doc | Path |
|---|---|
| RMK | `RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx` |
| CR Artikel 13 | `Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 13.docx` |
| CR Artikel 14 | `Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 14.docx` |

## Phase-1 decisions (locked)

| # | Decision | Choice |
|---|---|---|
| 1 | Chapter source | **C&E 21e** — `TPGS-21Ed-2018-Crafting and Executing Strategy Concepts (Temu 8 - 14).pdf`, Ch. 7, book pp. 178–210 (PDF 221–253; book = PDF − 43). ONLY source for RMK body. Citations as *hlm. X* (book page). |
| 2 | Template & pipeline | **Reuse Pert. 2–7 conventions**: A4 · Times New Roman 12 pt · 1.5 spacing · H1 14 pt centered bold, H2 12 pt bold, H3 12 pt bold italic · margins 3 cm / 2.5 cm · first-line indent 1.25 cm · captions centered 11 pt italic · academic Bahasa Indonesia (English terms italic on first use) · figures ~6.0 in wide · Markdown → Pandoc 3.9 + `Dev Assistant/scripts/reference.docx`; figures via PyMuPDF (documented Python exception to Rust default). |
| 3 | Output destination | Repo convention (`RMK/`, `Critical Thinking of the Article/`). No `output/` dir. |
| 4 | Illustration Capsules | **Narrate in prose** with page citations; embedded images framework-only. |

**Artikel-14 AI-use notice (flagged & acknowledged):** EBSCO copyright page prohibits AI/ML use of content. Handling: human-authored-style review — summarize/critique in own words, proper citation, no extended verbatim passages, article figures embedded only as attributed exhibits.

## Hard gates (Phase 5 validation)

1. **Figure gate (RMK):** Gambar 7.1 (Diamond, hlm. 182), Gambar 7.2 (Tiga Pendekatan, hlm. 194), Tabel 7.1 (hlm. 197) — each embedded, captioned (*Gambar/Tabel N. Judul (Sumber: TPGS 21e, 2018, hlm. X)*), legible, undistorted, in-margin, adjacent to its explanation.
2. **Concept gate (RMK):** every entry in `analysis/ch7-concept-inventory.md` §1–§9 has a home section.
3. **Review gate:** each CR covers summary → framing/method → findings → critical appraisal → explicit Ch.7 linkage → implications; genuinely critical; Ch.7 linkage syllabus-mandated.
4. **Format gate:** the locked template values, identity block (NIM 01079 + name) on p. 1 of each doc, opens in Word/LibreOffice.
5. **Faithfulness:** no invented pages/content; RMK body uses ONLY Ch. 7; each CR only its article (+ Ch.7 for linkage).

## Document blueprints

### RMK Pert. 8 — "Strategi Bersaing di Pasar Internasional" (11 sections)

Section order mirrors the chapter. Per section: concepts owned (book pp.), required figure anchors. Content detail lives in `analysis/ch7-concept-inventory.md`; the section plan in `analysis/build-input.md`.

0. **Cover/Pendahuluan** — identity block; LO1–LO6; positioning.
1. **Mengapa Perusahaan Memasuki Pasar Internasional** (179–180) — 5 motives + suppliers-follow-customers.
2. **Kompleksitas Lintas Negara & Model Diamond** (181–183) — 5 complexity drivers; 4 Diamond factors; 3 managerial uses. ⟨**Gambar 7.1**⟩
3. **Keunggulan Lokasi, Kebijakan Pemerintah & Risiko Kurs** (183–187) — location advantages; pro/anti-business policies; political vs economic risk (CORE CONCEPT); exchange-rate worked example (real/euro) + weak/strong-currency logic.
4. **Perbedaan Demografis, Kultural & Pasar** (187–188) — taste examples; customize-vs-standardize tension (bridge to §6).
5. **Lima Opsi Strategi Memasuki Pasar Asing** (188–193) — export / licensing / franchising / subsidiary (acquisition vs greenfield) / alliances-JV with benefits & risks; investment-risk-control gradient; IC 7.1 Walgreens narrated.
6. **Tiga Pendekatan Strategi Internasional** (193–198) — international-strategy def.; multidomestic / global / transnational (defs, fit conditions, drawbacks); IC 7.2 Four Seasons narrated. ⟨**Gambar 7.2**, **Tabel 7.1**⟩
7. **Operasi Internasional & Keunggulan Kompetitif** (199–202) — concentrate-vs-disperse; sharing/transferring R&C (Disney walkthrough, Philips caveat); cross-border coordination.
8. **Manuver Strategis Lintas Batas** (202–204) — profit sanctuaries; cross-market subsidization; dumping/WTO; defensive deterrence & mutual restraint.
9. **Bersaing di Pasar Negara Berkembang** (204–206) — BRIC stakes; 4 options (Unilever Wheel, Honeywell, Suzuki, Home Depot); patience.
10. **Bertahan Melawan Raksasa Global** (206–208) — 5 local-company defenses; IC 7.3 Ctrip narrated.
11. **Sintesis** — integrative read-through; cross-check against Key Points (209–210).

**Format standard:** ### sub-headings (2–5 analytical sub-angles per section); bold for key definitions/pivots; italics for foreign terms; each figure preceded by a 1-line transition and followed by 2–3 sentence interpretation; sections 150–300+ words of substantive analysis each.

### CR Artikel 13 — Kostruba & Kostruba (2025)

Skeleton (7 §): bibliographic ID & purpose → framing & method → findings → critical appraisal → linkage to TPGS Ch.7 → implications & verdict (+ cover identity).
**Embedded exhibits:** Figure 2 (F∩N=G — required by the formal critique), Figure 3 (international marketing environment), Table 3 (strategy groups). Figure 1, Figure 4, Tables 1/2/4 summarized in prose. Captions attribute: *(Sumber: Kostruba & Kostruba, 2025, hlm. X)*.
**Appraisal must include:** method opacity (Google/Scholar, no protocol); F∩N=G incoherence (∩ vs union); Table-1/Table-2 labeling slip; dated evidence (CPI 2015); untested conceptual model; strengths — fiscal specificity (German coffee tax → green-coffee arbitrage), size-contingent prescriptions, timeliness, Hofstede + legal-systems integration.
**Ch.7 linkage:** motives ↔ §1; entry-mode taxonomies (Tables 3–4) ↔ five TPGS options; environment/Hofstede ↔ §2c/2e; inverted emerging-market perspective ↔ §7–8; Diamond (Gambar 7.1) as the missing home-country-advantage lens for Ukraine.

### CR Artikel 14 — Gregory, Li & Solanki (2026)

Same skeleton. **Embedded exhibits:** Figure 1 (3 clusters / 7 imperatives), Figure 2 (Cisco workflow), Figure 3 (IKEA SEA), Table 2 (RQ/H1–H16). Table 1 summarized in prose.
**Appraisal must include:** evidence base = one public panel, n=3 tech-leaning executives; curated-narrative risk; unverified practitioner numbers (82%, 2×, +30%, +40%); method-label stacking (reflexive TA + Gioia) with thin audit trail; Insight-Paper genre — hypotheses generated not tested (Table 2 = strongest artifact); strengths — currency (EU AI Act, EO 14110), mechanism-level cases, triangulation, agenda value.
**Ch.7 linkage:** AI shifts the feasible frontier of the transnational approach (Gambar 7.2/Tabel 7.1); Cisco mini-hatcheries ↔ concentrate-vs-disperse + cross-border coordination (§5); brand/capability transfer ↔ §5b; regulatory fragmentation ↔ §2c; platform localization ↔ §7; IKEA SEA ↔ Four Seasons (IC 7.2) parallel.

## Figure extraction (Phase 3.5)

PyMuPDF, `Matrix(3,3)` ≈ 300 DPI (216 dpi min acceptable at Matrix(3,3) for these page sizes), anchor-text search → clip → PNG → `Dev Assistant/temp/pert8_figures/`.

| ID | Anchor | PDF page (1-based) | Clip strategy |
|---|---|---|---|
| ch7_figure_7_1 | "FIGURE 7.1" | 225 (TPGS PDF) | caption-y to bottom margin (caption above diagram; include Source line) |
| ch7_figure_7_2 | "FIGURE 7.2" | 237 | caption-y to bottom margin |
| ch7_table_7_1 | "TABLE 7.1" | 240 | caption BELOW table — clip from "Advantages" header row through caption; avoid IC text above |
| art13_figure_2 | "Figure 2: Interconnection" | 11 (Artikel 13 PDF) | figure region above caption |
| art13_figure_3 | "Figure 3: Relationship" | 12 | figure region below caption line |
| art13_table_3 | "Table 3: Characteristics" | 15 | table body incl. header |
| art14_figure_1 | "Figure 1. Strategic Imperatives" | 3 (Artikel 14 PDF) | full-width figure above caption |
| art14_figure_2 | "Figure 2. Cisco" | 5 | figure region |
| art14_figure_3 | "Figure 3. Case Study" | 6 | figure region |
| art14_table_2 | "Table 2. Research Questions" | 7 | full-page table |

Each crop visually verified (legible, undistorted, no neighbor text) before authoring; bbox overrides applied where anchor-relative clip misfires (per validated Pert. 2–7 practice).

## Pipeline & verification

- Generator: `Dev Assistant/scripts/generate_submission_w8.py` (pattern: `generate_submission_w7.py`) — extract figures → build 3 Markdown strings → Pandoc + reference.docx → 3 docx.
- Verifier: `Dev Assistant/scripts/verify_pert8.py` — asserts: file opens; A4 page size; TNR 12 pt body; 1.5 spacing; identity block present; figure count & captions; concept-coverage keyword checklist per RMK section; CR rubric sections present; Ch.7-linkage section present in both CRs.
- Validation report: `analysis/pert8-validation.md` (concept table, figure checklist, rubric checklist, format checklist).
- Git: work directly on `main` (prior-pert convention); commits per phase.

## Voice & depth contract

Professor-led S2 exposition: explain (what/why/how/significance), interpret every figure and framework, connect sections into one argument; reviews genuinely critical (evaluate rigor, validity, generalizability, gaps — not descriptive summary); no padding; no plagiarism — all prose original Indonesian academic writing.
