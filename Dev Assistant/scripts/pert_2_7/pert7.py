"""Pertemuan 7 visual-insertion content spec."""

CIT_FIG = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 8"
CIT_TAB = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 8"

IMAGES = [
    ("§7.1 Pengantar — Dari Single-Business ke Multibusiness",
     "fig_8_1.png",
     f"Gambar 7.1 — Tujuan Membangun Perusahaan Multibisnis Melalui "
     f"Diversifikasi. {CIT_FIG}, hlm. 154 (Figure 8.1)."),

    ("§7.1 Pengantar — Dari Single-Business ke Multibusiness",
     "fig_8_2.png",
     f"Gambar 7.2 — Tiga Tes untuk Menilai Daya Tarik Langkah Diversifikasi. "
     f"{CIT_FIG}, hlm. 155 (Figure 8.2)."),

    ("§7.4 Mode Masuk Diversifikasi",
     "cc_8_1.png",
     f"Gambar 7.3 — Merger Kraft Foods dengan H. J. Heinz: Studi Kasus "
     f"Akuisisi Diversifikasi. {CIT_FIG}, hlm. 158 (Concepts & Connections 8.1)."),

    ("§7.6 Mengevaluasi Strategi Perusahaan Terdiversifikasi (Six-Step Procedure)",
     "fig_8_3.png",
     f"Gambar 7.4 — Matriks Sembilan-Sel: Daya Tarik Industri vs Kekuatan "
     f"Kompetitif. {CIT_FIG}, hlm. 166 (Figure 8.3)."),

    ("§7.7 Empat Pilihan Strategis Pasca-Evaluasi",
     "fig_8_4.png",
     f"Gambar 7.5 — Pilihan Strategis dan Finansial Utama untuk Mengalokasikan "
     f"Sumber Daya Keuangan Perusahaan Terdiversifikasi. "
     f"{CIT_FIG}, hlm. 170 (Figure 8.4)."),
]

TABLES = [
    ("§7.6 Mengevaluasi Strategi Perusahaan Terdiversifikasi (Six-Step Procedure)",
     f"Tabel 7.1 — Perhitungan Skor Daya Tarik Industri yang Tertimbang. "
     f"{CIT_TAB}, hlm. 162 (Table 8.1).",
     [
         ("Industry Attractiveness Measure", "Importance / Weight",
          "Industry A Rating / Score", "Industry B Rating / Score",
          "Industry C Rating / Score", "Industry D Rating / Score"),
         ("Market size and projected growth rate", "0.10",
          "8 / 0.80", "5 / 0.50", "2 / 0.20", "3 / 0.30"),
         ("Intensity of competition", "0.25",
          "8 / 2.00", "7 / 1.75", "3 / 0.75", "2 / 0.50"),
         ("Emerging opportunities and threats", "0.10",
          "2 / 0.20", "9 / 0.90", "4 / 0.40", "5 / 0.50"),
         ("Cross-industry strategic fit", "0.20",
          "8 / 1.60", "4 / 0.80", "8 / 1.60", "2 / 0.40"),
         ("Resource requirements", "0.10",
          "5 / 0.50", "8 / 0.80", "2 / 0.20", "6 / 0.60"),
         ("Seasonal and cyclical influences", "0.05",
          "8 / 0.40", "5 / 0.25", "10 / 0.50", "5 / 0.25"),
         ("Social, political, regulatory, and environmental factors", "0.05",
          "7 / 0.35", "7 / 0.35", "7 / 0.35", "7 / 0.35"),
         ("Industry profitability", "0.10",
          "5 / 0.50", "10 / 1.00", "3 / 0.30", "3 / 0.30"),
         ("Industry uncertainty and business risk", "0.05",
          "5 / 0.25", "7 / 0.35", "10 / 0.50", "1 / 0.05"),
         ("Sum of importance weights", "1.00", "", "", "", ""),
         ("Weighted overall industry attractiveness scores", "",
          "6.60", "6.70", "4.80", "3.25"),
     ]),

    ("§7.6 Mengevaluasi Strategi Perusahaan Terdiversifikasi (Six-Step Procedure)",
     f"Tabel 7.2 — Penilaian Kekuatan Kompetitif untuk Bisnis-Bisnis dalam "
     f"Perusahaan Terdiversifikasi. {CIT_TAB}, hlm. 164 (Table 8.2).",
     [
         ("Competitive Strength Measure", "Importance / Weight",
          "Business A Rating / Score", "Business B Rating / Score",
          "Business C Rating / Score", "Business D Rating / Score"),
         ("Relative market share", "0.15",
          "10 / 1.50", "1 / 0.15", "6 / 0.90", "2 / 0.30"),
         ("Costs relative to competitors' costs", "0.20",
          "7 / 1.40", "2 / 0.40", "5 / 1.00", "3 / 0.60"),
         ("Ability to match or beat rivals on key product attributes", "0.05",
          "9 / 0.45", "4 / 0.20", "8 / 0.40", "4 / 0.20"),
         ("Brand image and reputation", "0.10",
          "9 / 0.90", "2 / 0.20", "7 / 0.70", "5 / 0.50"),
         ("Other competitively valuable capabilities", "0.15",
          "7 / 1.05", "2 / 0.30", "5 / 0.75", "3 / 0.45"),
         ("Benefits from strategic fit with sister businesses", "0.20",
          "8 / 1.60", "4 / 0.80", "8 / 1.60", "2 / 0.40"),
         ("Bargaining leverage with suppliers/buyers; access to alliances",
          "0.05", "9 / 0.45", "3 / 0.15", "7 / 0.35", "4 / 0.20"),
         ("Profitability relative to competitors", "0.10",
          "5 / 0.50", "1 / 0.10", "4 / 0.40", "4 / 0.40"),
         ("Sum of importance weights", "1.00", "", "", "", ""),
         ("Overall weighted competitive strength scores", "",
          "7.85", "2.30", "6.10", "3.05"),
     ]),
]
