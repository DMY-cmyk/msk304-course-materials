# Design Spec — Pertemuan 2-7 Visuals Addition to `RMK Pra UTS.docx`

**Course:** MST304 Manajemen Strategik Kontemporer (STIE YKPN, Magister Akuntansi)
**Document target:** `RMK Pra UTS.docx`
**Date:** 2026-05-22
**Author:** Dzaki Muhammad Yusfian (NIM 1125 01079) — drafted via Claude Code brainstorming session
**Status:** Approved by user; ready for implementation plan
**Predecessor:** `2026-05-22-msk304-pertemuan-1-design.md` (validated pattern)

---

## 1. Problem Statement

After Pertemuan 1 was successfully added with 3 cropped ebook images + 2 native tables (user verdict: "It's Perfect"), the existing Pertemuan 2–7 sections in `RMK Pra UTS.docx` still contain **zero ebook visuals**. They consist entirely of prose summaries of TPGS chapters with no figures, sidebar boxes, or tables imported from the source. This creates a visual inconsistency: Pertemuan 1 looks comprehensive while Pertemuan 2–7 look text-heavy.

This spec adds, across Pertemuan 2 → 7, the same visual treatment validated on Pertemuan 1.

## 2. Scope

**In scope:**
- **33 cropped PDF images** embedded inline at 6.0″ width (`Caption`-styled paragraph below each, Indonesian text with citation): all Figures + all Concepts & Connections sidebars from TPGS Chapters 2, 3, 4, 5, 6, and 8 (Ch. 7 is skipped per syllabus — Pertemuan 7 covers Ch. 8).
- **11 native Word tables** reconstructed from TPGS ebook Tables in Ch. 2, 3, 4, and 8. Reconstructed using `python-docx` `add_table` with `Table Grid` style, bold header row, and Indonesian title-caption paragraph above. **Word tables, not cropped images**, per user requirement.
- Placement at the natural §X.N sub-section where each visual conceptually belongs (distributed, not batched at the top).
- Idempotent insertion: refuses to re-insert if target visual already present.
- Per-Pertemuan docx backup before write.

**Out of scope:**
- Re-writing or restructuring existing Pertemuan 2–7 prose.
- Adding visuals to Pertemuan 1 (already complete) or BAGIAN I / BAGIAN III (Critical Reviews).
- Touching the Master Consolidated Study Document or any Rust pipeline artifacts.
- Translating Indonesian prose; tables and image captions use English source titles with Indonesian explanatory captions.

## 3. Source Inventory (verified by PDF scan)

### Pertemuan 2 ← TPGS Chapter 2 (PDF pp. 53–75)
**Figures (2):** Figure 2.1 (Strategy Formulation, Strategy Execution Process) p. 55; Figure 2.2 (A Company's Strategy-Making Hierarchy) p. 67.
**Tables (4):** Table 2.1 (Factors Shaping Decisions) p. 55; Table 2.2 (Vision Statement Characteristics) p. 57; Table 2.3 (Vision Shortcomings) p. 57; Table 2.4 (Objectives types) p. 64.
**Concepts & Connections (4):** C&C 2.1 (Vision examples) p. 58; C&C 2.2 (TOMS Shoes mission) p. 61; C&C 2.3 (Company objectives) p. 64; C&C 2.4 (Volkswagen governance failure) p. 71.

### Pertemuan 3 ← TPGS Chapter 3 (PDF pp. 76–103)
**Figures (7):** 3.1 (PESTEL macro-environment); 3.2 (Five Forces); 3.3 (Buyer Bargaining Power factors); 3.4 (Substitutes); 3.5 (Supplier Bargaining Power); 3.6 (Threat of Entry); 3.7 (Competitive Rivalry).
**Tables (3):** Table 3.1 (Six PESTEL components) p. 79; Table 3.2 (Driving Forces) p. 93; Table 3.3 (Key Success Factors) p. 99.
**Concepts & Connections (1):** C&C 3.1 (industry analysis example) p. 96.

### Pertemuan 4 ← TPGS Chapter 4 (PDF pp. 104–126)
**Figures (2):** Figure 4.1 (Resource & capability appraisal); Figure 4.2 (Representative Value Chain).
**Tables (2):** Table 4.2 (SWOT factors) p. 111; Table 4.3 (Competitive strength assessment) p. 120.
**Concepts & Connections (1):** C&C 4.1 (resource-capability example) p. 114.

### Pertemuan 5 ← TPGS Chapter 5 (PDF pp. 127–148)
**Figures (3):** Figure 5.1 (Generic strategies matrix); Figure 5.2 (Cost Drivers); Figure 5.3 (Value Drivers).
**Tables (0):** none in Ch. 5.
**Concepts & Connections (4):** C&C 5.1 (Vanguard) p. 133; C&C 5.2 p. 142; C&C 5.3 p. 143; C&C 5.4 (American Giant) p. 145.

### Pertemuan 6 ← TPGS Chapter 6 (PDF pp. 149–169)
**Figures (1):** Figure 6.1 (Offensive options).
**Tables (0):** none in Ch. 6.
**Concepts & Connections (3):** C&C 6.1 p. 154; C&C 6.2 (Walmart horizontal acquisition) p. 160; C&C 6.3 p. 164.

### Pertemuan 7 ← TPGS Chapter 8 (PDF pp. 191–218)
**Figures (4):** Figure 8.1; Figure 8.2; Figure 8.3 (Nine-Cell Industry Attractiveness–Competitive Strength Matrix) p. 207; Figure 8.4 (Chief Strategic & Financial Options for Diversified Companies) p. 211.
**Tables (2):** Table 8.1 (Industry Attractiveness scoring) p. 203; Table 8.2 p. 206.
**Concepts & Connections (1):** C&C 8.1 (Kraft-Heinz merger) p. 198.

**Grand total:** 19 Figures + 14 Concepts & Connections = **33 images** to crop. Plus **11 Word tables** to reconstruct.

## 4. Placement Map (visual → existing §X.N sub-section)

The plan inserts at the **paragraph at the end of the chosen sub-section's prose, before the next H2/H3 begins** (i.e., visuals appear at the bottom of their conceptually anchored sub-section).

### Pertemuan 2
| Sub-section anchor | Visuals |
|---|---|
| §2.2 Pengembangan Visi Strategis | Table 2.2, Table 2.3, C&C 2.1, C&C 2.2 |
| §2.2 Penetapan Tujuan | Table 2.4, C&C 2.3 |
| §2.2 Perumusan Strategi | Figure 2.2 |
| §2.2 (intro paragraph of "Lima Tahap") | Figure 2.1, Table 2.1 |
| §2.3 Corporate Governance | C&C 2.4 |

### Pertemuan 3
| Sub-section anchor | Visuals |
|---|---|
| §3.2 Q1 — PESTEL | Figure 3.1, Table 3.1 |
| §3.3 Q2 — Five Forces | Figure 3.2, 3.3, 3.4, 3.5, 3.6, 3.7 |
| §3.4 Q3 — Driving Forces | Table 3.2 |
| §3.6 Q5 — Competitor moves OR §3.8 Industry Attractiveness | C&C 3.1, Table 3.3 |

### Pertemuan 4
| Sub-section anchor | Visuals |
|---|---|
| §4.3 Q2 — Sumber Daya & VRIN | Figure 4.1, C&C 4.1 |
| §4.4 Analisis SWOT | Table 4.2 |
| §4.5 Q3 — Rantai Nilai | Figure 4.2 |
| §4.6 Competitive Strength Assessment | Table 4.3 |

### Pertemuan 5
| Sub-section anchor | Visuals |
|---|---|
| §5.1 Pengantar & Dua Faktor | Figure 5.1 |
| §5.2 Low-Cost Provider | Figure 5.2, C&C 5.1 |
| §5.3 Broad Differentiation | Figure 5.3, C&C 5.2, C&C 5.3 |
| §5.5 Best-Cost Provider | C&C 5.4 |

### Pertemuan 6
| Sub-section anchor | Visuals |
|---|---|
| §6.2 Strategi Ofensif | Figure 6.1, C&C 6.1 |
| §6.5 Horizontal M&A | C&C 6.2 |
| §6.5 Strategic Alliances | C&C 6.3 |

### Pertemuan 7
| Sub-section anchor | Visuals |
|---|---|
| §7.1 Pengantar (single → multibusiness) | Figure 8.1, Figure 8.2 |
| §7.4 Mode Masuk Akuisisi | C&C 8.1 |
| §7.6 Six-Step Procedure | Figure 8.3, Table 8.1, Table 8.2 |
| §7.7 Empat Pilihan Strategis | Figure 8.4 |

## 5. Technical Approach

### 5.1 Image extraction
- One extractor script: `Dev Assistant/scripts/extract_pert_2_7_images.py`.
- Reuses the explicit-bbox-override pattern validated in Pertemuan 1. Each of the 33 targets is a tuple `(pdf_page_index_0based, output_filename, explicit_crop_or_None, output_subdir)`.
- For Figures and C&C sidebars where the caption marker reliably anchors a wide block, use `None` → heuristic. For known-narrow-seed cases (label-above-figure), specify `(x0, y0, x1, y1)` measured directly from page block layout.
- Output written to `images/pertemuan-N/<label>.png` per Pertemuan subdirectory.

### 5.2 Table reconstruction
- One inserter script (see §5.3) builds 11 native Word tables using the table content extracted from each PDF table's text blocks.
- Each table specified as a Python list-of-lists in the script (rows × cells).
- Header row bolded; `Table Grid` style; auto-fit column widths.
- Each table preceded by an Indonesian title-caption paragraph in `Caption` style: `"Tabel X.Y — [Indonesian title]. Sumber: Gamble, Peteraf, Thompson (2021), Ch. N, hlm. P (Table X.Y)."`
- For tables whose source content is bulleted lists (e.g., Table 4.2 SWOT factors), reconstruct as a 4-row Word table with one cell per quadrant.

### 5.3 Document insertion
- One inserter script: `Dev Assistant/scripts/insert_pert_2_7_visuals.py`.
- Iterates through 6 Pertemuan blocks; per Pertemuan, walks its placement map and inserts visuals at the resolved anchor paragraph.
- Anchor resolution: locate the anchor sub-section heading by text match (e.g., `find_anchor(doc, "§2.2 Pengembangan Visi")`), then walk forward to find the **last paragraph before the next H2 or H3**; insert immediately after that paragraph.
- Image insertion reuses the validated `insert_image_before(...)` helper from Pertemuan 1's script.
- Idempotency: before inserting any visual, check whether a `Caption`-styled paragraph already mentions the visual's label (e.g., `"Gambar 2.1"` or `"Tabel 2.1"`) — if found, skip.

### 5.4 Caption convention
- All captions in Indonesian.
- Figures: `"Gambar [PertN.SeqM] — [Indonesian title translated from ebook]. Sumber: Gamble, Peteraf, Thompson (2021), Ch. N, hlm. P (Figure X.Y)."` Use a per-Pertemuan running counter so figures within Pertemuan 2 are `Gambar 2.1, 2.2, ...` regardless of TPGS label.
- C&C sidebars: same convention but referenced as `(Concepts & Connections X.Y)`.
- Tables: `"Tabel [PertN.SeqM] — [Indonesian title]. Sumber: ... (Table X.Y)."`.

### 5.5 File outputs
| Path | Role |
|---|---|
| `Dev Assistant/scripts/extract_pert_2_7_images.py` | Extracts 33 PNGs to `images/pertemuan-2..7/` |
| `Dev Assistant/scripts/insert_pert_2_7_visuals.py` | Inserts 33 images + 11 native tables into the docx |
| `Dev Assistant/scripts/verify_pert_2_7.py` | Acceptance verification script |
| `images/pertemuan-2/*.png` through `images/pertemuan-7/*.png` | 33 cropped PNG files (300 DPI) |
| `RMK Pra UTS.PRE-PERT-2-7.docx` | Backup taken before any write |

## 6. Risk Register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Page indices off by one for some figures | Medium | Source inventory in §3 lists explicit PDF pages; verification step inspects each output PNG width to detect narrow-seed mis-crops (matches Pert 1 fix). |
| Anchor sub-section text doesn't match exactly | Medium | Use prefix-match (`startswith`) and verify each anchor resolves before insert; abort with descriptive error if any anchor is missing. |
| Some Figures have only label text + image (no caption block); seed heuristic fails | Medium | Explicit bbox override per problematic target; pattern proven on Pert 1's Figure 1.1. |
| Word file becomes too large with 33 PNGs at 300 DPI | Low | 33 × ~300 KB ≈ 10 MB extra. Acceptable for a class document. |
| Idempotency check fires false positive (same caption text exists elsewhere) | Low | Use compound check: caption paragraph text matches AND paragraph is in `Caption` style AND located inside the correct Pertemuan block. |
| Reconstructed Word tables don't match ebook fidelity exactly | Medium | Tables reproduced from PDF text content; minor formatting differences acceptable. Critical: column structure and row order must match. |
| User wants tables as images instead | Low | User explicitly requested Word table formatting for tables. Re-confirm at spec review gate. |
| Reading or editing the docx between runs corrupts state | Low | Backup at `RMK Pra UTS.PRE-PERT-2-7.docx`; idempotent inserter can be re-run safely. |

## 7. Acceptance Criteria

1. Document opens cleanly in Microsoft Word (no corruption warning).
2. Inline image count grows from 3 (current, Pert 1 only) → **36** (3 + 33 new).
3. Native table count grows from 4 (current) → **15** (4 + 11 new).
4. Each new image has a `Caption`-styled paragraph immediately below it that begins with `"Gambar "`.
5. Each new table has a `Caption`-styled paragraph immediately above it that begins with `"Tabel "`.
6. No image is inserted twice (idempotency).
7. No regression in Pertemuan 1 visuals (still 3 images + 2 tables, captions intact).
8. `verify_pert_2_7.py` exits 0 with PASS message including counts.
9. Final file size of `RMK Pra UTS.docx` stays under 25 MB.

## 8. Decomposition into Implementation Tasks

The implementation plan (next step) should organize work as:
1. **Task A:** Backup docx + scaffold extractor/inserter/verifier scripts + create 6 image directories.
2. **Task B:** Implement `extract_pert_2_7_images.py` with all 33 targets; run; visually spot-check at least one image per Pertemuan; commit.
3. **Task C–H:** **Six independent Pertemuan-insertion tasks**, one per Pertemuan (2, 3, 4, 5, 6, 7). Each task adds that Pertemuan's visuals and tables, runs the verifier in incremental-mode for just that Pertemuan, and commits. Failures in one Pertemuan do not block others.
4. **Task I:** Final `verify_pert_2_7.py` full-document pass; commit if PASS.

This per-Pertemuan decomposition reduces blast radius — if Pertemuan 5's tables have a quirk, it doesn't block Pertemuan 2-4's commits.

## 9. Out-of-Scope Decisions (Recorded)

- **Translation of full ebook table text into Indonesian:** Out of scope. Tables retain English ebook content; only the title-caption above each table is Indonesian. Rationale: tables convey definitions that are recognized terms (PESTEL, SWOT, VRIN) — translating risks fidelity loss.
- **Adding visuals to Pertemuan 8-14:** Out of scope (this document is `RMK Pra UTS` — pre-UTS only).
- **Updating BAGIAN I synthesis sections to reference new visuals:** Out of scope. The §1.5 Tabel Integrasi remains as-is.

---

**Next step:** invoke `superpowers:writing-plans` to produce the step-by-step implementation plan.
