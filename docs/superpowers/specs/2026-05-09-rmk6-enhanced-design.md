# Design Spec — RMK Pert. 6 Enhanced (TPGS Ch.6 Full Audit + Figures)

- **Student:** Dzaki Muhammad Yusfian | NIM: 1125 01079
- **Course:** MST304 — Manajemen Strategik Kontemporer, STIE YKPN
- **Spec date:** 2026-05-09
- **Status:** Approved
- **Purpose:** Audit the existing RMK Pert. 6 against TPGS Ch.6 full text, add all missing content, and embed real figures/diagrams/case-box images extracted from the textbook PDF.

---

## 1. Source

**Textbook:** `Ebook/(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf`

**Chapter:** Chapter 6 — *Strengthening a Company's Competitive Position: Strategic Moves, Timing, and Scope of Operations*
**PDF pages (0-indexed):** 148–168 (reader pages 149–169)
**TOC page 149:** confirmed as Ch.6 opener (reader p.110 in book pagination)

---

## 2. Output

**Script:** `Dev Assistant/scripts/generate_rmk6_enhanced.py` (new file — does NOT touch `generate_submission_w6.py`)

**Output file:** `RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx` (overwrites existing 37 KB version)

**Expected size:** 50–70 KB (images add ~5–10 KB each on top of existing 37 KB text)

---

## 3. Phase 1 — Figure Extraction (PyMuPDF 1.27.1)

**Library:** `fitz` (PyMuPDF) — confirmed installed at v1.27.1

**Output directory:** `Dev Assistant/temp/ch6_figures/` (created by script if absent)

**Resolution:** `fitz.Matrix(2, 2)` — 2× scale for crisp rendering in Word documents

### Figures to extract

| Filename | PDF page (0-indexed) | Content | Extraction method |
|----------|---------------------|---------|-------------------|
| `figure_6_1.png` | 149 (reader p.150) | **Figure 6.1** — "Strategies to Strengthen a Company's Competitive Approaches" hub diagram | Locate anchor text "FIGURE 6.1" via `page.search_for()`, expand bounding rect downward to capture full diagram, clip and render at 2× |
| `cc_6_1_etsy.png` | 153–154 (reader p.154–155) | **C&C 6.1** — Etsy's Blue Ocean Strategy in Online Retailing | Locate "CONCEPTS & CONNECTIONS 6.1" anchor, capture full box region spanning the section (may span two pages — render each and stack or capture from page containing the box header) |
| `cc_6_2_walmart.png` | 159–160 (reader p.160–161) | **C&C 6.2** — Walmart's Expansion into E-Commerce via Horizontal Acquisition | Same anchor-search approach for "CONCEPTS & CONNECTIONS 6.2" |
| `cc_6_3_tesla.png` | 163–164 (reader p.164–165) | **C&C 6.3** — Tesla's Vertical Integration Strategy | Same anchor-search approach for "CONCEPTS & CONNECTIONS 6.3" |

**Fallback:** If anchor-based clipping fails for any figure (bounding rect too small or anchor not found), fall back to rendering the full page(s) containing that figure as PNG. Log which approach was used.

**Validation:** After extraction, verify each PNG file exists and is > 10 KB. Raise error if any is missing or suspiciously small (< 5 KB = likely blank clip).

---

## 4. Phase 2 — Content Audit: Missing Sections from TPGS Ch.6

The existing RMK Pert. 6 covers the topic broadly but misses these specific TPGS Ch.6 sections that must be added:

### Within §2 Offensive Strategies (add after existing content)
- **Choosing the Basis for Competitive Attack** (TPGS p.151): 6 attack bases — cost advantage, underserved buyer segments, quality/service/features gaps, innovation, brand/name recognition gaps, distribution gaps. Bold the condition under which each basis is viable.
- **Choosing Which Rivals to Attack** (TPGS p.152): attack vulnerable market leaders (when they are complacent or have weaknesses), attack runner-up firms (easier targets), avoid strong counter-fighters (firms with deep pockets and willingness to retaliate).

### Within §3 Defensive Strategies (add after existing content)
- **Blocking the Avenues Open to Challengers** (TPGS p.154): broaden product line to close gaps, introduce economy/premium models to cover price bands, maintain strong dealer/distributor relationships, offer loyalty incentives to buyers, build inventory/capability to respond fast.
- **Signaling Challengers That Retaliation Is Likely** (TPGS p.154): public announcements of intent to defend, matching/beating competitor price cuts, building war chests of cash, pursuing challengers in their home markets.

### Within §4 Timing (enhance existing content)
- **Deciding Whether to Be an Early Mover or Late Mover** (TPGS p.156): the explicit TPGS decision framework — factors favoring early entry (big learning advantage, lock-in of scarce resources, network effects, switching costs, brand preference) vs. factors favoring late entry (avoid pioneering costs, learn from early movers' mistakes, free-ride on market education, leapfrog first-generation technology).

### Within §5 Scope — Horizontal M&A (add sub-section)
- **Why Mergers and Acquisitions Sometimes Fail** (TPGS p.159): overestimating synergies, integration difficulties, culture clash, paying too much premium, distracting management from core business. Bold the most common failure mode.

### Within §5 Scope — Vertical Integration (expand existing sub-section)
- **Four Advantages of Vertical Integration** (TPGS p.161–162): (1) adds to competitive strength/differentiation, (2) reduces vulnerability to powerful suppliers, (3) reduces vulnerability to powerful buyers, (4) builds barriers to entry.
- **Three Disadvantages of Vertical Integration** (TPGS p.163): (1) increases capital investment and business risk, (2) restricts flexibility in changing suppliers/buyers, (3) may not be cost-competitive if in-house operations are less efficient than outside specialists.

### Within §5 Scope — Alliances (expand existing sub-section)
- **Failed Strategic Alliances** (TPGS p.166): diverging objectives over time, loss of competitive sensitivity, partner free-riding, mistrust from sharing proprietary knowledge, difficulty coordinating across cultures.
- **Strategic Dangers of Relying on Alliances for Essential Resources** (TPGS p.167): the "hollowing out" risk — if a firm consistently relies on alliances for core capabilities, it may lose the ability to rebuild those capabilities internally when the alliance ends.

### New §10 — Poin-Poin Kunci (TPGS Key Points, p.167)
Add a 10th section rendering the official TPGS Key Points as formatted Markdown bullet list:
- LO6-1: offensive vs. defensive strategic moves
- LO6-2: first mover / fast follower / late mover timing
- LO6-3: strategic benefits and risks of expanding scope (horizontal M&A, vertical integration, outsourcing, alliances)
- LO6-4: when alliances and cooperative partnerships work
- LO6-5: strategic management takeaways

---

## 5. Phase 3 — Image Placement in Markdown

Images inserted at the following natural positions in the Markdown content:

| Image | Placement location | Caption |
|-------|--------------------|---------|
| `figure_6_1.png` | After §1 Pendahuluan opening paragraph, before §2 | `*Gambar 6.1 — Strategi untuk Memperkuat Posisi Kompetitif Perusahaan (Sumber: TPGS Ch.6, p.111)*` |
| `cc_6_1_etsy.png` | Within §6 Blue Ocean, after the ERRC Grid sub-heading | `*Concepts & Connections 6.1 — Strategi Blue Ocean Etsy dalam Penjualan Kerajinan Tangan Daring (Sumber: TPGS Ch.6, p.115)*` |
| `cc_6_2_walmart.png` | Within §5 Scope, after Horizontal M&A sub-heading | `*Concepts & Connections 6.2 — Ekspansi Walmart ke E-Commerce melalui Akuisisi Horizontal (Sumber: TPGS Ch.6, p.121)*` |
| `cc_6_3_tesla.png` | Within §5 Scope, after Vertical Integration sub-heading | `*Concepts & Connections 6.3 — Strategi Integrasi Vertikal Tesla (Sumber: TPGS Ch.6, p.125)*` |

**Markdown syntax:**
```markdown
![*Gambar 6.1 — Strategi untuk Memperkuat Posisi Kompetitif Perusahaan*](../temp/ch6_figures/figure_6_1.png)

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.111*
```

**Path note:** The Markdown temp file is written to `Dev Assistant/temp/rmk_w6_enhanced.md`. The image paths must be relative to that temp file, resolving to `Dev Assistant/temp/ch6_figures/figure_6_1.png`. Alternatively use absolute paths in the Markdown to avoid resolution issues.

---

## 6. Pipeline

```python
EBOOK = PROJECT_ROOT / "Ebook" / "(Business professional collection) John E. Gamble_ ..."
FIGURES_DIR = TEMP / "ch6_figures"

# Step 1: extract figures
extract_figure_6_1(EBOOK, FIGURES_DIR)
extract_cc_box(EBOOK, "CONCEPTS & CONNECTIONS 6.1", 153, FIGURES_DIR / "cc_6_1_etsy.png")
extract_cc_box(EBOOK, "CONCEPTS & CONNECTIONS 6.2", 159, FIGURES_DIR / "cc_6_2_walmart.png")
extract_cc_box(EBOOK, "CONCEPTS & CONNECTIONS 6.3", 163, FIGURES_DIR / "cc_6_3_tesla.png")

# Step 2: build enhanced Markdown with image refs
md_content = build_rmk_enhanced(FIGURES_DIR)

# Step 3: write temp .md and convert via pandoc
md_path = TEMP / "rmk_w6_enhanced.md"
md_path.write_text(md_content, encoding="utf-8")
pandoc(md_path, OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx")
```

---

## 7. Writing Standards (same as existing RMK Pert. 6)

- Indonesian akademik; PUEBI/KBBI; foreign terms italicized
- ### sub-headings in every section; **bold** for analytical pivots; *italics* for foreign terms
- No " - " as clause connector; reduplication `kata - kata` style
- No Daftar Pustaka; inline citations only
- New content from TPGS Ch.6 cited as (Gamble, Thompson & Peteraf 2021, p.X)
- Image captions in Indonesian, source credited

---

## 8. Out of Scope

- CR Artikel 9 and CR Artikel 10 (untouched — already committed)
- `generate_submission_w6.py` (untouched)
- Henry Ch.5–6 ebook
- Other pertemuan chapters
