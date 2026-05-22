"""Pertemuan 4 visual-insertion content spec."""

CIT_FIG = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 4"
CIT_TAB = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 4"

IMAGES = [
    ("§4.3 Q2 — Sumber Daya, Kapabilitas, dan Uji VRIN",
     "fig_4_1.png",
     f"Gambar 4.1 — Identifikasi Sumber Daya dan Kapabilitas Perusahaan. "
     f"{CIT_FIG}, hlm. 72 (Figure 4.1)."),

    ("§4.3 Q2 — Sumber Daya, Kapabilitas, dan Uji VRIN",
     "cc_4_1.png",
     f"Gambar 4.2 — Contoh Identifikasi Sumber Daya dan Kapabilitas pada "
     f"Perusahaan. {CIT_FIG}, hlm. 73 (Concepts & Connections 4.1)."),

    ("§4.5 Q3 — Daya Saing Struktur Biaya & Proposisi Nilai Pelanggan",
     "fig_4_2.png",
     f"Gambar 4.3 — Rantai Nilai Representatif untuk Sebuah Industri. "
     f"{CIT_FIG}, hlm. 75 (Figure 4.2)."),
]

TABLES = [
    ("§4.4 Analisis SWOT",
     f"Tabel 4.1 — Faktor-Faktor yang Perlu Dipertimbangkan dalam Mengidentifikasi "
     f"Kekuatan, Kelemahan, Peluang, dan Ancaman Perusahaan. "
     f"{CIT_TAB}, hlm. 70 (Table 4.2).",
     [
         ("Potential Internal Strengths & Competitive Capabilities",
          "Potential Internal Weaknesses & Competitive Deficiencies"),
         ("Core competencies in key areas",
          "No clear strategic direction"),
         ("A strong financial condition; ample financial resources to grow "
          "the business",
          "No well-developed or proven core competencies"),
         ("Strong brand-name image / company reputation",
          "A weak balance sheet; burdened with too much debt"),
         ("Economies of scale and/or learning and experience-curve advantages "
          "over rivals",
          "Higher overall unit costs relative to those of key competitors"),
         ("Other cost advantages over rivals (proprietary technology, "
          "input-cost advantages, capacity utilization)",
          "Missing some key skills or competencies; lack of management depth"),
         ("Attractive customer base",
          "Subpar profitability"),
         ("Technology / innovation skills; important patents",
          "Plagued with internal operating problems or obsolete facilities"),
         ("Product innovation capabilities",
          "Too narrow a product line relative to rivals"),
         ("Proven capabilities in improving production processes",
          "Weak brand image or reputation"),
         ("Good supply chain management capabilities",
          "Weaker dealer network than key rivals"),
         ("Good customer service capabilities",
          "Behind on product quality, R&D, and/or technological know-how"),
         ("Better product quality relative to rivals",
          "In the wrong strategic group"),
         ("Wide geographic coverage and/or strong global distribution",
          "Losing market share"),
         ("Alliances/joint ventures that provide access to valuable "
          "technology / competencies / attractive geographic markets",
          "Lack the financial resources to fund promising strategic "
          "initiatives"),
         ("Potential Market Opportunities",
          "Potential External Threats to Future Profitability"),
         ("Meeting demand of fast-growing market segments",
          "Increasing intensity of competition among industry rivals — may "
          "squeeze profit margins"),
         ("Expanding the company's product line to meet a broader range of "
          "customer needs",
          "Slowdowns in market growth"),
         ("Using existing skills/know-how to enter new product lines or new "
          "businesses",
          "Likely entry of potent new competitors"),
         ("Online sales / e-commerce growth",
          "Loss of sales to substitute products"),
         ("Integrating forward or backward",
          "Growing bargaining power of customers or suppliers"),
         ("Falling trade barriers in attractive foreign markets",
          "A shift in buyer needs / tastes away from industry's product"),
         ("Acquiring rival firms or companies with attractive technological "
          "expertise / capabilities",
          "Adverse demographic changes that threaten to curtail demand"),
         ("Entering into alliances or joint ventures to expand the firm's "
          "market coverage or boost its competitive capability",
          "Adverse economic conditions / recession"),
         ("Openings to exploit emerging new technologies",
          "Costly new regulatory requirements"),
         ("Openings to extend the company's brand name or reputation to new "
          "geographic areas",
          "Tightening credit conditions / rising borrowing costs"),
     ]),

    ("§4.6 Q4 — Competitive Strength Assessment",
     f"Tabel 4.2 — Penilaian Kekuatan Kompetitif Tertimbang Sederhana. "
     f"{CIT_TAB}, hlm. 80 (Table 4.3).",
     [
         ("Key Success Factor / Strength Measure", "Weight",
          "ABC Co. Rating / Score", "Rival 1 Rating / Score",
          "Rival 2 Rating / Score"),
         ("Quality / product performance", "0.10",
          "8 / 0.80", "5 / 0.50", "1 / 0.10"),
         ("Reputation / image", "0.10",
          "8 / 0.80", "7 / 0.70", "1 / 0.10"),
         ("Manufacturing capability", "0.10",
          "2 / 0.20", "10 / 1.00", "5 / 0.50"),
         ("Technological skills", "0.05",
          "10 / 0.50", "1 / 0.05", "3 / 0.15"),
         ("Dealer network / distribution capability", "0.05",
          "9 / 0.45", "4 / 0.20", "5 / 0.25"),
         ("New-product innovation capability", "0.05",
          "9 / 0.45", "4 / 0.20", "5 / 0.25"),
         ("Financial resources", "0.10",
          "5 / 0.50", "10 / 1.00", "3 / 0.30"),
         ("Relative cost position", "0.30",
          "5 / 1.50", "10 / 3.00", "1 / 0.30"),
         ("Customer service capabilities", "0.15",
          "5 / 0.75", "7 / 1.05", "1 / 0.15"),
         ("Sum of weights", "1.00", "", "", ""),
         ("Overall weighted competitive strength rating", "",
          "5.95", "7.70", "2.10"),
     ]),
]
