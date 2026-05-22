# Design Spec — Pertemuan 1 Addition to `RMK Pra UTS.docx`

**Course:** MST304 Manajemen Strategik Kontemporer (STIE YKPN, Magister Akuntansi, Semester II TA 2025/2026)
**Document target:** `RMK Pra UTS.docx`
**Date:** 2026-05-22
**Author:** Dzaki Muhammad Yusfian (NIM 1125 01079) — drafted via Claude Code brainstorming session
**Status:** Approved by user; awaiting written-spec review before implementation plan

---

## 1. Problem Statement

`RMK Pra UTS.docx` currently consolidates Pertemuan 2–7 of MST304 plus 12 Critical Reviews and a Sintesis & Integrasi section. **Pertemuan 1 is missing.** Per the syllabus (`Silabus MSK TA 2025-2026.pdf`, page 6), Pertemuan 1 covers:

- Penjelasan Silabus dan Pembagian Tugas
- **What Is Strategy and Why Is It Important?**
- Group arrangement and assignment
- Reference: **TPGS Chapter 1** — Gamble, Peteraf, Thompson (2021) *Essentials of Strategic Management* 7th Ed., Ch. 1 "Strategy, Business Models, and Competitive Advantage" (PDF pp. 41–52)

Pertemuan 1 has **no articles assigned** in the syllabus. The Pertemuan 1 RMK must therefore stand on TPGS Ch. 1 alone (no §X.N "Integrasi dengan Artikel Pendukung" subsection) — replaced by an Indonesian flagship anchor case study.

## 2. Scope

**In scope:**
1. Insert a new `BAGIAN II — PERTEMUAN 1: HAKIKAT STRATEGI DAN KEUNGGULAN KOMPETITIF` section between BAGIAN I (Sintesis) and the existing `BAGIAN II — PERTEMUAN 2`.
2. Compose §1.1 through §1.8 with depth matching Pertemuan 2–7 (~32–38 paragraphs).
3. Embed **3 cropped PNG images** from TPGS Ch. 1, rendered at 300 DPI from the source PDF, with locked 6.0-inch inline width.
4. Light update to BAGIAN I §1.1 title and an inserted transitional paragraph so cross-references stay coherent.

**Out of scope:**
- Do **NOT** rewrite the existing matrices and tables in BAGIAN I (Approach 3 rejected in brainstorming).
- Do **NOT** add new Critical Reviews (no articles for Pertemuan 1).
- Do **NOT** touch Pertemuan 2–7 sections except for the single BAGIAN I §1.1 title update.

## 3. Insertion Strategy

- **Location:** Immediately after paragraph index 38 (end of BAGIAN I) and before paragraph index 39 (`BAGIAN II — PERTEMUAN 2: PROSES MANAJERIAL...`).
- **Mechanism:** Use `python-docx` to construct new paragraphs and insert via the underlying `_element` XML model (`element.addprevious(...)` against the Pertemuan 2 heading).
- **Style reuse:** New paragraphs use the same styles already present in the document — `Heading 1`, `Heading 2`, `Heading 3`, `First Paragraph`, `Body Text`. No new styles introduced.
- **Image placement:** Each image is in its own paragraph centered horizontally, with a `Caption`-styled paragraph beneath it bearing the figure label and source citation.

## 4. Section-by-Section Outline

### §1.1 Pengantar & Pemetaan Bab
- Course opener: positions Pertemuan 1 as the conceptual gateway for the entire MST304 curriculum.
- Explains that this Pertemuan combines **silabus orientation + group assignment + TPGS Chapter 1**.
- Frames the five sub-themes from TPGS Ch. 1 that the rest of the section will unpack.
- 1 `Heading 2` + 2 paragraphs (`First Paragraph` + `Body Text`).

### §1.2 Apa Itu Strategi? — Lima Tindakan Inti
- Defines strategy per Gamble et al.: a coordinated set of competitive moves and business approaches to grow, attract customers, compete, conduct operations, and achieve performance goals.
- Unpacks the five core strategic actions: (1) positioning vs rivals, (2) differentiation, (3) geographic & customer scope, (4) partnerships & alliances, (5) value-chain configuration.
- **Native Word table** (5 rows × 2 cols) summarising the five actions with Indonesian-context examples.
- 1 `Heading 2` + 3 paragraphs + 1 table.

### §1.3 Strategi vs Model Bisnis
- Clarifies the relationship: strategy is the *quest* for competitive advantage; business model is the *economic logic* that makes the strategy financially viable.
- Two business-model pillars: **Customer Value Proposition** and **Profit Formula**.
- Uses TPGS's Pandora vs SiriusXM vs OTA Broadcast Radio contrast.
- **Embedded image:** `CONCEPTS & CONNECTIONS 1.1` sidebar (PDF pp. 45–46) cropped at 300 DPI.
- 1 `Heading 2` + 3 paragraphs + 1 cropped image + caption.

### §1.4 Keunggulan Kompetitif yang Berkelanjutan
- Defines competitive advantage (above-average industry returns) and **sustainable** competitive advantage (durable against rivals' efforts to copy).
- Four sources of SCA: low-cost, differentiation, focused-niche, capabilities-based.
- TPGS Apple case as illustration.
- **Embedded image:** `CONCEPTS & CONNECTIONS 1.2` sidebar (PDF p. 47) cropped at 300 DPI.
- 1 `Heading 2` + 3 paragraphs + 1 cropped image + caption.

### §1.5 Kapabilitas Dinamis & Evolusi Strategi
- Capabilities-based view: why dynamic capabilities are the deepest source of SCA.
- **Deliberate + Emergent → Realized Strategy** framework (per Gamble's reading of Mintzberg).
- Why strategy is "a work in progress, not a one-time event."
- **Embedded image:** `FIGURE 1.1` (PDF p. 48) cropped at 300 DPI — the diagram showing Deliberate Strategy Elements + Emergent Strategy Elements → Realized Business Strategy, minus Abandoned strategy elements.
- 1 `Heading 2` + 3 paragraphs + 1 cropped image + caption.

### §1.6 Tiga Uji Strategi yang Menang
- The Three Tests:
  1. **Fit Test** — internal/external/dynamic consistency
  2. **Competitive Advantage Test** — produces durable advantage
  3. **Performance Test** — yields superior financial & strategic results
- **Native Word table** (3 rows × 3 cols: Test name | What it asks | Indonesian-context probe).
- 1 `Heading 2` + 2 paragraphs + 1 table.

### §1.7 Indonesian Flagship — BCA (Bank Central Asia) Lulus Tiga Uji
- BCA used as the flagship case (not previously used in Pert 2–7 which favoured Astra/GoTo/Indofood).
- **Fit:** BCA's transaction-banking strategy fits Indonesia's underbanked-yet-digitalizing middle class.
- **Competitive Advantage:** Largest CASA base in Indonesia, lowest cost-of-funds among private banks; sustained NIM > 5%; ROE consistently top-decile (>20%).
- **Performance:** 2024 net income ~Rp54T (per AR/IDX); P/B premium ~5x signals durable market belief in the strategy.
- Embeds the three-test framework concretely.
- Includes the standard anti-fabrication disclosure banner (data-point types cited: AR/IDX).
- 1 `Heading 2` + 4 paragraphs (1 `First Paragraph` + 3 `Body Text`).

### §1.8 Sintesis Pertemuan 1 dan Jembatan ke Pertemuan 2
- Close-out: strategy is a unified, evolving, capability-grounded answer to *how we compete and win*.
- Hand-off paragraph: §1.8 ends where §2.1 begins — by introducing the 5-stage managerial process that operationalizes the strategic thinking introduced in Pertemuan 1.
- 1 `Heading 2` + 2 paragraphs (1 `First Paragraph` + 1 `Body Text`).

**Estimated total:** 8 sub-section headings, ~24 body paragraphs, 2 native tables, 3 embedded cropped images with captions ≈ **35–38 paragraphs of new content**.

## 5. Image Rendering Specification

| # | Source | PDF page (1-indexed) | Crop region | Output | Word inline width |
|---|---|---|---|---|---|
| 1 | CONCEPTS & CONNECTIONS 1.1 | p. 45 (Pandora/SiriusXM/OTA box) | Full sidebar bounding box | PNG, 300 DPI | 6.0 in |
| 2 | CONCEPTS & CONNECTIONS 1.2 | p. 47 (Apple Inc. sidebar) | Full sidebar bounding box | PNG, 300 DPI | 6.0 in |
| 3 | FIGURE 1.1 | p. 48 | Figure block (~y=500–660 in PDF coordinates) + caption text below | PNG, 300 DPI | 6.0 in |

**Render method:** `PyMuPDF` (`fitz`) `page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72), clip=rect)`.

**Crop discovery:** Use `page.get_text("dict")["blocks"]` to find the text block beginning with `CONCEPTS & CONNECTIONS 1.1` / `1.2` / `FIGURE 1.1`, then union the bounding box of all blocks belonging to the sidebar / figure including its visual frame, with a 12pt padding margin.

**Storage:** Save PNGs into `images/pertemuan-1/` under the project root (gitignored from cache via standard rules; the docx embeds them as binary so the PNG files are not needed after build).

**No-stretch guarantee:** Embed via `paragraph.add_run().add_picture(path, width=Inches(6.0))` — locks width; height auto-computed from source aspect ratio. No floating positioning, no anchor-to-text-box. Page text frame in default Letter/A4 portrait with 1" margins comfortably accommodates 6.0" inline.

**Caption style:** Each image is followed by a `Caption`-styled paragraph: `"Gambar 1.X — [judul]. Sumber: Gamble, Peteraf, Thompson (2021), Ch.1, p.[N]."`

## 6. BAGIAN I Touch-Up

- Locate paragraph index 6: `§1.1 Alur Naratif Induk (Pertemuan 2 → 7)`.
- Rewrite as: `§1.1 Alur Naratif Induk (Pertemuan 1 → 7)`.
- Insert one new `Body Text` paragraph immediately after the existing prose of §1.1 noting that Pertemuan 1 introduces the conceptual scaffold (strategy, business model, sustainable competitive advantage, three tests) on which Pertemuan 2's managerial process is built.
- No other BAGIAN I edits.

## 7. Indonesian-Context Anchoring Rules

Same rules already enforced in Pert 2–7 sections:
- Every data point must cite the **document type** (AR = Annual Report, IDX = Indonesia Stock Exchange filing, OJK = Otoritas Jasa Keuangan, IR = Investor Relations, Sustainability Report).
- Use descriptive language when exact figures are not defensibly available.
- Include a disclosure banner sentence in §1.7 stating that all BCA-specific data points are sourced from publicly available AR / IDX disclosures.

## 8. Acceptance Criteria

1. `RMK Pra UTS.docx` opens cleanly in Microsoft Word with no corruption warnings.
2. The new `BAGIAN II — PERTEMUAN 1` section appears between BAGIAN I and the existing PERTEMUAN 2 section.
3. All 8 sub-section headings (§1.1 through §1.8) render with `Heading 2` style.
4. All 3 embedded images render at 6.0" inline width, no stretching/cropping inside Word.
5. Each image has a `Caption`-styled paragraph below it with the figure label and citation.
6. The two native Word tables (§1.2 five-actions; §1.6 three-tests) render with consistent column widths.
7. BAGIAN I §1.1 title reads "(Pertemuan 1 → 7)".
8. Document total paragraph count grows by approximately 35–38 (from 959 to ~995–998).
9. Document total table count grows by 2 (from 2 to 4).
10. No regression to Pertemuan 2–7 content — paragraph indices for §2.1 onward will shift, but the textual content is byte-identical.

## 9. Risk Register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Image stretches in Word due to mis-set anchor | Low | Use inline `add_picture` with explicit `width=Inches(6.0)`; no `width`+`height` double-set. |
| Crop box misses part of the sidebar frame | Medium | Render a debug preview PNG first; visually verify before final insert. |
| Mid-document XML insertion corrupts docx | Low | Operate on a copy; validate via re-open + paragraph count after each write. |
| BCA data figures drift from current AR | Low | Cite ranges and document-type labels rather than precise figures; include disclosure banner. |
| `python-docx` style name mismatch ('Body Text' vs 'BodyText') | Low | Read existing styles from the document and reuse exact names already present. |

## 10. Out-of-Scope Decisions (Recorded for Future Reference)

- **Rust pipeline integration:** The Rust `dev-assistant` pipeline produces HTML, not docx. Pertemuan 1 in this document is a Word-native addition only; no Rust changes are required.
- **Master Consolidated Study Document:** Separate artifact at `01079_..._Master Consolidated Study Document.docx`. Not in scope for this task.
- **Rerun of brainstorming for any other Pertemuan:** All other Pertemuan are already present; this spec covers Pertemuan 1 only.

---

**Next step after spec approval:** invoke `superpowers:writing-plans` skill to produce the step-by-step implementation plan.
