# TPGS Ch. 7 — Figure/Table/Exhibit Map (verified against the PDF text layer + page graphics scan)

**Source PDF:** `TPGS-21Ed-2018-Crafting and Executing Strategy Concepts (Temu 8 - 14).pdf` (449 pp.; Ch. 7 = PDF 221–256).
Book page = PDF page − 43. Graphics scan: raster images + vector paths detected on PDF pp. 221, 225, 235, 237, 241, 251 — consistent with the inventory below. **No other FIGURE/TABLE 7.x exists in this chapter** (text-layer scan found only 7.1, 7.2 figures + 7.1 table; all body cross-references match).

## Mandatory embeds (chapter framework graphics — the "every figure/table" gate)

| ID | Item | Book p. | PDF p. | Caption anchor | Approx. region | Anchors to RMK section |
|---|---|---|---|---|---|---|
| ch7-fig-01 | **FIGURE 7.1 — The Diamond of National Competitive Advantage** (4-node diamond; Source: adapted from Porter, HBR 1990) | 182 | 225 | "FIGURE 7.1" mid-page | lower ~60% of page below the Factor Conditions paragraph | §2a Diamond Model |
| ch7-fig-02 | **FIGURE 7.2 — Three Approaches for Competing Internationally** (2×2: local responsiveness × global integration; multidomestic / transnational / global) | 194 | 237 | "FIGURE 7.2" lower page | bottom ~45% of page | §4 intro / approach choice |
| ch7-tab-01 | **TABLE 7.1 — Advantages and Disadvantages of Multidomestic, Global, and Transnational Strategies** (3 rows × adv./disadv.) | 197 | 240 | "TABLE 7.1" caption at bottom (table body above) | middle-to-bottom of page | §4d comparison |

## Boxed exhibits (Illustration Capsules — decide embed-vs-narrate in Phase 1/3)

| ID | Item | Book pp. | PDF pp. | Notes |
|---|---|---|---|---|
| ch7-ic-01 | IC 7.1 — Walgreens Boots Alliance: Entering Foreign Markets via Alliance Followed by Merger | 191–192 | 234–235 | spans page break; photo on PDF 235; content = case narrative |
| ch7-ic-02 | IC 7.2 — Four Seasons Hotels: Local Character, Global Service | 197–198 | 240–241 | full-page capsule on PDF 241 with photo |
| ch7-ic-03 | IC 7.3 — Ctrip Defends against International Rivals | 207–208 | 250–251 | full-page capsule on PDF 251 with photo |

Recommendation: capsules are case-text boxes, not framework graphics. The hard "every figure/table" gate covers Fig 7.1, Fig 7.2, Table 7.1. Capsules should be **summarized in prose** within their host sections (with page citations); optionally embedded as cropped exhibits if the user prefers — ask in Phase 1.

## Other visual elements (not embed candidates)

- Chapter opener page (PDF 221): title + Learning Objectives LO1–LO6 box — reproduce LO list as text, no crop needed.
- CORE CONCEPT margin boxes (political/economic risks p. 185; greenfield p. 190; international strategy p. 193; multidomestic p. 194; global p. 195; transnational p. 196; cross-market subsidization p. 203; deterrence p. 203–204) — definitional text; integrate into prose as bolded definitions, not images.
- Margin notes (exchange-rate pp. 187, location p. 199, alliances p. 191–192, developing-market profitability p. 205) — integrate as prose.
- Photos accompanying capsules (Getty/Bloomberg) — do NOT embed (third-party photography, no pedagogical value).

## Crop plan (for Phase 3.5)

- Render at 200–300 DPI via PyMuPDF (`page.get_pixmap(matrix=fitz.Matrix(3,3), clip=...)`) — established approach from Pert. 2–7 (`generate_submission_w7.py`).
- ch7-fig-01: clip from "FIGURE 7.1" caption y-position to bottom margin (caption sits ABOVE the diagram; include Source line at bottom).
- ch7-fig-02: clip from "FIGURE 7.2" caption to bottom margin of PDF 237.
- ch7-tab-01: caption "TABLE 7.1" is BELOW the table body on PDF 240 — clip from the "Advantages / Disadvantages" header row down through the caption line; verify no overlap with the Four Seasons IC text above.
- Target width: 5.8–6.0 in (fits A4 text column with 3 cm / 2.5 cm margins at 12 pt).
- Visual verification of every crop before commit (legible, undistorted, no clipped edges, no neighboring body text).
