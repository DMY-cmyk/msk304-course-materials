"""Pertemuan 2 visual-insertion content spec.

IMAGES: each (anchor_text_prefix, img_filename, caption)
TABLES: each (anchor_text_prefix, caption, rows_list_of_tuples)
"""

CIT_FIG = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 2"
CIT_TAB = "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 2"

IMAGES = [
    ("§2.2 Lima Tahap Proses Manajemen Strategis",
     "fig_2_1.png",
     f"Gambar 2.1 — Proses Perumusan dan Eksekusi Strategi (Lima Tahap). "
     f"{CIT_FIG}, hlm. 14 (Figure 2.1)."),

    ("Pengembangan Visi Strategis, Misi, dan Nilai Inti",
     "cc_2_1.png",
     f"Gambar 2.2 — Contoh-Contoh Pernyataan Visi Strategis. "
     f"{CIT_FIG}, hlm. 17 (Concepts & Connections 2.1)."),

    ("Pengembangan Visi Strategis, Misi, dan Nilai Inti",
     "cc_2_2.png",
     f"Gambar 2.3 — TOMS Shoes: Model Bisnis Berbasis Misi. "
     f"{CIT_FIG}, hlm. 20 (Concepts & Connections 2.2)."),

    ("Penetapan Tujuan (Setting Objectives)",
     "cc_2_3.png",
     f"Gambar 2.4 — Contoh-Contoh Tujuan Perusahaan. "
     f"{CIT_FIG}, hlm. 23 (Concepts & Connections 2.3)."),

    ("Perumusan Strategi (Crafting Strategy)",
     "fig_2_2.png",
     f"Gambar 2.5 — Hirarki Pembuatan Strategi Perusahaan. "
     f"{CIT_FIG}, hlm. 26 (Figure 2.2)."),

    ("§2.3 Corporate Governance dalam Proses Strategis",
     "cc_2_4.png",
     f"Gambar 2.6 — Kegagalan Tata Kelola Perusahaan di Volkswagen. "
     f"{CIT_FIG}, hlm. 30 (Concepts & Connections 2.4)."),
]

TABLES = [
    ("§2.2 Lima Tahap Proses Manajemen Strategis",
     f"Tabel 2.1 — Faktor-Faktor yang Membentuk Keputusan dalam Proses Perumusan "
     f"dan Eksekusi Strategi. {CIT_TAB}, hlm. 14 (Table 2.1).",
     [
         ("External Considerations", "Internal Considerations"),
         ("Does sticking with the company's present strategic course present "
          "attractive opportunities for growth and profitability?",
          "Does the company have an appealing customer value proposition?"),
         ("What kind of competitive forces are industry members facing, and are "
          "they acting to enhance or weaken the company's prospects for growth "
          "and profitability?",
          "What are the company's competitively important resources and "
          "capabilities, and are they potent enough to produce a sustainable "
          "competitive advantage?"),
         ("What factors are driving industry change, and what impact will they "
          "have on the company's competitive position?",
          "Does the company have sufficient business and competitive strength "
          "to seize market opportunities and nullify external threats?"),
         ("How are industry rivals positioned, and what strategic moves are "
          "they likely to make next?",
          "Are the company's costs competitive with those of key rivals?"),
         ("What are the key factors of future competitive success, and does the "
          "industry offer good prospects for attractive profits for companies "
          "possessing those capabilities?",
          "Is the company competitively stronger or weaker than its key rivals?"),
     ]),

    ("Pengembangan Visi Strategis, Misi, dan Nilai Inti",
     f"Tabel 2.2 — Karakteristik Pernyataan Visi yang Efektif. "
     f"{CIT_TAB}, hlm. 16 (Table 2.2).",
     [
         ("Characteristic", "Description"),
         ("Graphic",
          "Paints a picture of the kind of company that management is trying "
          "to create and the market position(s) the company is striving to "
          "stake out."),
         ("Directional",
          "Is forward-looking; describes the strategic course that management "
          "has charted and the kinds of product-market-customer-technology "
          "changes that will help the company prepare for the future."),
         ("Focused",
          "Is specific enough to provide managers with guidance in making "
          "decisions and allocating resources."),
         ("Flexible",
          "Is not so focused that it makes it difficult for management to "
          "adjust to changing circumstances in markets, customer preferences, "
          "or technology."),
         ("Feasible",
          "Is within the realm of what the company can reasonably expect to "
          "achieve."),
         ("Desirable",
          "Indicates why the directional path makes good business sense."),
         ("Easy to communicate",
          "Is explainable in 5 to 10 minutes and, ideally, can be reduced to "
          "a simple, memorable slogan."),
     ]),

    ("Pengembangan Visi Strategis, Misi, dan Nilai Inti",
     f"Tabel 2.3 — Kekurangan yang Sering Muncul dalam Pernyataan Visi "
     f"Perusahaan. {CIT_TAB}, hlm. 17 (Table 2.3).",
     [
         ("Shortcoming", "Why It Matters"),
         ("Vague or incomplete",
          "Short on specifics about where the company is headed or what kind "
          "of company management is trying to create."),
         ("Not forward-looking",
          "Doesn't indicate whether or how management intends to alter the "
          "company's current product-market-customer-technology focus."),
         ("Too broad",
          "So all-inclusive that the company could head in almost any "
          "direction, pursue almost any opportunity, or enter almost any "
          "business."),
         ("Bland or uninspiring",
          "Lacks the power to motivate company personnel or inspire "
          "shareholder confidence about the company's direction."),
         ("Not distinctive",
          "Provides no unique company identity; could apply to companies in "
          "any of several industries (or at least several rivals operating "
          "in the same industry or market arena)."),
         ("Too reliant on superlatives",
          "Doesn't say anything specific about the company's strategic course "
          "beyond the pursuit of such lofty accolades as best, most "
          "successful, recognized leader, global or worldwide leader, or "
          "first choice of customers."),
     ]),

    ("Penetapan Tujuan (Setting Objectives)",
     f"Tabel 2.4 — Jenis Tujuan: Tujuan Finansial dan Tujuan Strategis. "
     f"{CIT_TAB}, hlm. 22 (Table 2.4).",
     [
         ("Financial Objectives", "Strategic Objectives"),
         ("An x percent increase in annual revenues",
          "Winning an x percent market share"),
         ("Annual increases in after-tax profits of x percent",
          "Achieving lower overall costs than rivals"),
         ("Annual increases in earnings per share of x percent",
          "Overtaking key competitors on product performance or quality or "
          "customer service"),
         ("Annual dividend increases of x percent",
          "Deriving x percent of revenues from the sale of new products "
          "introduced within the past five years"),
         ("Profit margins of x percent",
          "Having broader or deeper technological capabilities than rivals"),
         ("An x percent return on capital employed (ROCE) or return on "
          "shareholders' equity (ROE)",
          "Having a wider product line than rivals"),
         ("Increased shareholder value in the form of an upward-trending "
          "stock price",
          "Having a better-known or more powerful brand name than rivals"),
         ("Bond and credit ratings of x",
          "Having stronger national or global sales and distribution "
          "capabilities than rivals"),
         ("Internal cash flows of x dollars to fund new capital investment",
          "Consistently getting new or improved products to market ahead of "
          "rivals"),
     ]),
]
