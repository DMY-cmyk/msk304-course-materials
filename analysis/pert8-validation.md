# Pert. 8 Validation Report

**Date:** 2026-06-05 · **Spec:** `docs/superpowers/specs/2026-06-05-rmk-cr-pertemuan8-design.md`

## Automated gates — 33/33 PASS (`Dev Assistant/scripts/verify_pert8.py`)

Per document (rmk / cr13 / cr14): file exists · A4 210×297 mm · identity NIM 01079 · identity name · Normal font Times New Roman · Normal 12 pt · line spacing 1.5 · embedded image count (3/3/4) · image widths within text column (≤6.11 in) · concept-keyword coverage (0 missing).

## Render verification (Word COM → PDF → visual inspection)

- All three open cleanly in Microsoft Word and export to PDF without warnings.
- RMK Pert. 8: 17 pages · CR Artikel 13: 7 pages · CR Artikel 14: 8 pages.
- Figures legible, undistorted, within margins, captioned (*Gambar/Tabel N. … (Sumber: …, hlm. X)*), each adjacent to its explanation with 1-line transition before and interpretation after.
- Typography verified visually: TNR 12 body, 1.5 spacing, justified, 1.25 cm first-line indent, H1/H2/H3 hierarchy, bold pivots, italic foreign terms.

## RMK figure checklist (hard gate)

| Exhibit | Source page | Anchor section | Embedded | Width |
|---|---|---|---|---|
| Gambar 7.1 — Diamond of National Competitive Advantage | hlm. 182 | §2 Kompleksitas & Model Diamond | ✅ | 5.8 in |
| Gambar 7.2 — Tiga Pendekatan Bersaing Internasional | hlm. 194 | §4 Strategi Internasional | ✅ | 5.8 in |
| Tabel 7.1 — Keunggulan/Kelemahan Tiga Strategi | hlm. 197 | §4 (setelah transnasional) | ✅ | 5.8 in |

Chapter scan confirmed NO other FIGURE/TABLE 7.x exists in TPGS C&E 21e Ch. 7. Illustration Capsules 7.1 (Walgreens), 7.2 (Four Seasons), 7.3 (Ctrip) narrated in prose per locked Phase-1 decision.

## RMK concept coverage (concept → section)

| Inventory § | Concepts | RMK section |
|---|---|---|
| §1 | 5 motives + suppliers-follow-customers | §1 |
| §2a | Diamond 4 faktor + 3 kegunaan manajerial | §2 |
| §2b–2d | Lokasi, kebijakan pemerintah, political vs economic risk, risiko kurs (contoh real/euro + logika dolar) | §3 |
| §2e | Perbedaan demografis-kultural + kustomisasi vs standardisasi | §4 |
| §3 | 5 opsi masuk + gradien risiko-kendali + IC 7.1 Walgreens | §5 |
| §4 | Multidomestik/global/transnasional + Tabel 7.1 + IC 7.2 Four Seasons | §6 |
| §5 | Konsentrasi vs dispersi; transfer R&C (Disney, Philips); koordinasi lintas batas | §7 |
| §6 | Profit sanctuaries; cross-market subsidization; dumping/WTO; deterensi & mutual restraint | §8 |
| §7 | BRIC; 4 opsi (Unilever Wheel, Honeywell, Suzuki, Home Depot); kesabaran profitabilitas | §9 |
| §8 | 5 strategi bertahan + IC 7.3 Ctrip | §10 |
| §9 | Key Points | §11 Sintesis |

(RMK section numbering: dokumen memakai §1–§9 dengan §Pendahuluan dan §Sintesis; pemetaan di atas merujuk urutan isi.)

## Critical-review rubric checklist

| Dimension | CR13 | CR14 |
|---|---|---|
| Identitas bibliografis & tujuan | ✅ §1 | ✅ §1 |
| Kerangka teoretis & metode | ✅ §2 | ✅ §2 |
| Temuan utama | ✅ §3 (3 exhibits) | ✅ §3 (4 exhibits) |
| Penilaian kritis (kekuatan + kelemahan + keseimbangan) | ✅ §4 (method opacity, F∩N=G, labeling slip, dated CPI, untested model) | ✅ §4 (n=3 panel, curated narrative, unverified numbers, label stacking, genre limits) |
| Keterkaitan eksplisit dengan TPGS Bab 7 (syllabus-mandated) | ✅ §5 (5 mappings + Diamond as missing lens) | ✅ §5 (5 mappings + transnational-frontier thesis) |
| Implikasi & penilaian akhir | ✅ §6 | ✅ §6 |

## Artikel-14 AI-use notice compliance

EBSCO notice flagged in Phase 1 and acknowledged. CR14 is analytic paraphrase throughout with proper citation; no extended verbatim passages; the article's own figures embedded only as attributed exhibits, as a student citing the source would.

## Format-rule checklist (locked Phase 1)

| Rule | rmk | cr13 | cr14 |
|---|---|---|---|
| A4 | ✅ | ✅ | ✅ |
| Margins 30/25/30/25 mm | ✅ | ✅ | ✅ |
| Times New Roman 12 pt body | ✅ | ✅ | ✅ |
| Line spacing 1.5 | ✅ | ✅ | ✅ |
| First-line indent 1.25 cm | ✅ | ✅ | ✅ |
| Identity block p. 1 (Dzaki Muhammad Yusfian, NIM 01079) | ✅ | ✅ | ✅ |
| Academic Bahasa Indonesia, English terms italic | ✅ | ✅ | ✅ |
| Filename exact | ✅ | ✅ | ✅ |

## Deliverables

- `RMK/01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx` (412 KB, 17 pp.)
- `Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 13.docx` (231 KB, 7 pp.)
- `Critical Thinking of the Article/01079_Dzaki Muhammad Yusfian_Artikel 14.docx` (1,4 MB, 8 pp.)

Regeneration: `python "Dev Assistant/scripts/extract_pert8_figures.py"` → `python "Dev Assistant/scripts/build_pert8.py"` → `python "Dev Assistant/scripts/verify_pert8.py"`.
