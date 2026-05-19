# Design Spec — RMK + CR Submission, Pertemuan 7

- **Assignment:** RMK + CR Pertemuan 7 (Tugas Manajemen Strategik Kontemporer)
- **Student:** Dzaki Muhammad Yusfian | NIM: 1125 01079
- **Course:** MST304 — Manajemen Strategik Kontemporer, STIE YKPN
- **Spec date:** 2026-05-19
- **Revised:** 2026-05-19 — scope reconciled with actual textbook (Essentials of Strategic Management 2021, 9-chapter abridged edition); Article 11 and Article 12 citations/mechanisms corrected against PDF contents
- **Status:** Approved (revised)
- **Analytical depth standard:** Pert. 6 standard + paradigmatic synthesis. Strategic Fit / Contingency Theory threaded as master frame across all three documents — operating at three levels: (1) **cross-business fit** in diversified corporations (TPGS Ch.8); (2) **internal fit** between strategy, HR, and reward (Hsieh & Chen, Artikel 11); (3) **multi-element organizational fit** via 4Cs framework (Okebaram & Onuoha, Artikel 12). Rich sub-heading + bold/italic formatting throughout; 150–300 word substantive sub-sections.

---

## 1. Assignment

Buat RMK dan Critical Review untuk materi dan artikel Pertemuan 7 sesuai silabus.

**Topik Pertemuan 7 (Essentials edition):** *Corporate Strategy: Diversification and the Multibusiness Company* (Essentials of Strategic Management Ch.8)

**Note on chapter mapping:** Silabus mencantumkan "TPGS 8" untuk Pertemuan 7 dengan label topik *Tailoring Strategy to Fit Specific Industry and Company Situations* (yang merupakan judul Ch.8 dalam edisi penuh *Crafting & Executing Strategy*). Edisi yang dimiliki mahasiswa adalah *Essentials of Strategic Management* (Gamble, Peteraf & Thompson 2021) — versi ringkas 9-bab di mana Ch.8 adalah *Corporate Strategy: Diversification and the Multibusiness Company*. RMK menggunakan konten Ch.8 yang aktual tersedia. Tema *strategic fit* tetap menjadi benang merah karena Ch.8 versi Essentials membangun argumen utamanya pada cross-business strategic fit dan economies of scope — sejalan dengan tema strategic fit yang menjadi fokus Artikel 11 dan Artikel 12.

**References:**
- TPGS Ch.8 (Gamble, Peteraf & Thompson 2021), *Essentials of Strategic Management: The Quest for Competitive Advantage*, 7th ed., McGraw-Hill — primary textbook anchor
- Article 11: Hsieh, Y. H. & Chen, H. M. (2011), *Strategic Fit among Business Competitive Strategy, Human Resource Strategy, and Reward System*, Academy of Strategic Management Journal, 10(2): 11–32
- Article 12: Okebaram, S. M. & Onuoha, C. E. (2018), *Implication of Strategic Fit and Sustainability on Organizational Effectiveness*, The 2018 International Academic Research Conference in Vienna, pp. 194–213

---

## 2. Output Files

| # | Filename | Output Path |
|---|----------|-------------|
| 1 | `01079_Dzaki Muhammad Yusfian_RMK Pert. 7.docx` | `RMK/` |
| 2 | `01079_Dzaki Muhammad Yusfian_Artikel 11.docx` | `Critical Thinking of the Article/` |
| 3 | `01079_Dzaki Muhammad Yusfian_Artikel 12.docx` | `Critical Thinking of the Article/` |

Output directories are root-level (canonical, consistent with Pert. 2–6).

---

## 3. Generation Pipeline

**Tool:** Pandoc + Python 3.12 orchestrator (reusing `reference.docx` from Pert. 2)

**Script:** `Dev Assistant/scripts/generate_submission_w7.py`

Pattern follows `generate_rmk6_enhanced.py` (figure-enabled variant): writes Markdown to `Dev Assistant/temp/`, calls pandoc with `reference.docx`, outputs DOCX to the paths in §2. Figure extraction step uses PyMuPDF (fitz) on the TPGS PDF, restricted to Ch.8 pages (PDF index 191–218), exporting PNG to `Dev Assistant/temp/ch8_figures/` and referenced from Markdown via standard `![caption](path)` syntax.

**Formatting:** Times New Roman 12pt body; 14pt centered bold Heading 1; 12pt bold Heading 2; 12pt bold italic Heading 3; margins 3cm / 2.5cm; line spacing 1.5; first-line indent 1.25cm. Figure captions centered, 11pt italic, format *Gambar X. Judul Gambar (Sumber: TPGS 2021, hlm. Y)*.

**Figures to extract (4 total — all available figures in Essentials Ch.8):**

| Key | Anchor text | PDF page index | Reader page | Description |
|---|---|---|---|---|
| `figure_8_1` | FIGURE 8.1 | 194 | 156 | Strategic Themes of Multibusiness Corporation (Related vs Unrelated Diversification) |
| `figure_8_2` | FIGURE 8.2 | 195 | 157 | Related Diversification Built upon Strategic Fit in Value Chain Activities |
| `figure_8_3` | FIGURE 8.3 | 206 | 168 | Nine-Cell Industry Attractiveness–Competitive Strength Matrix |
| `figure_8_4` | FIGURE 8.4 | 210 | 172 | Strategic & Financial Options for Allocating Diversified Company Resources |

---

## 4. Document 1 — RMK Pertemuan 7

**Topik:** *Corporate Strategy: Diversification and the Multibusiness Company* (Essentials Ch.8)

**Header:**
```
RINGKASAN MATERI KULIAH — PERTEMUAN 7
Mata Kuliah: MST304 — Manajemen Strategik Kontemporer
Mahasiswa: Dzaki Muhammad Yusfian | NIM: 1125 01079
```

**Format standard (critical):** Every section uses sub-headings (###) to break content into 2–5 analytical sub-angles. Bold for key concept definitions, critical reasoning pivots, "why this matters" moments. Italics for all foreign terms first use per section. Each sub-section 150–300 words of substantive analysis. Figures embedded inline at logical reading positions, each preceded by a 1-line transitional intro and followed by 2–3 sentence interpretation (not bare image dumps).

### §1 Pendahuluan
Sub-headings: **Dari Single-Business ke Multibusiness Decision**, **Mengapa Diversifikasi Menjadi Pertanyaan Strategik**, **Pertanyaan Pengarah Pertemuan 7**
- Transisi Pert. 4–6 (single-business strategy: RBV → generic strategy → strengthening position) → Pert. 7 (corporate-level strategy: portfolio of businesses)
- Bold pivot: kompleksitas strategik berubah secara *kualitatif* ketika perusahaan menjadi multibusiness — pertanyaan bergeser dari "bagaimana menang dalam satu industri" ke "industri mana saja yang harus dimasuki dan bagaimana mengelola portofolio tersebut"
- Bridge ke *strategic fit* sebagai konsep payung yang akan disintesiskan di §9 — fit antar-bisnis adalah test utama legitimasi diversifikasi

### §2 Kapan Diversifikasi Menjadi Pertimbangan Strategik
Sub-headings: **Sinyal Saturasi Bisnis Inti**, **Surplus Sumber Daya dan Kapabilitas**, **Pertumbuhan Shareholder Value Mensyaratkan Ekspansi**, **Risiko Diversifikasi Prematur**
- Saturasi pasar inti (low growth, intense rivalry, dominasi pemimpin yang kokoh)
- Excess cash + transferable capabilities → tekanan untuk re-deploy
- Bold reasoning: diversifikasi bukan target sendiri — harus menambah nilai melebihi standalone businesses
- Indonesian: Astra International dari otomotif ke heavy equipment + agribusiness + finansial; Sinar Mas dari pulp & paper ke property + finansial + agribisnis

### §3 Membangun *Shareholder Value*: Tiga Tes Diversifikasi
Sub-headings: **Tes 1 — *Industry Attractiveness Test***, **Tes 2 — *Cost of Entry Test***, **Tes 3 — *Better-Off Test***, **Mengapa Lulus Ketiga Tes Sulit**
- Industry attractiveness test: industri target harus menyediakan ROI di atas cost of capital secara berkelanjutan (Porter 1987)
- Cost of entry test: biaya masuk tidak boleh menggerogoti seluruh potensi profit masa depan
- Better-off test: kombinasi corporate-business harus menghasilkan kinerja gabungan lebih besar daripada penjumlahan standalone — *1 + 1 = 3* economics
- Bold critique: banyak akuisisi gagal lulus tes ketiga karena "synergy" yang dijanjikan tidak terealisasi (Porter 1987 menunjukkan >50% akuisisi besar di-divest dalam beberapa tahun)
- Indonesian: kasus akuisisi BUMN seperti Pertamina-Iran (gagal cost of entry test); Bank Mandiri konsolidasi 4 bank legacy (lulus better-off test melalui rasionalisasi)

### §4 Pendekatan Diversifikasi
Sub-headings: ***Acquisition* — Trade-off Kecepatan vs. Harga***, ***Internal Development* — Trade-off Lebih Murah tapi Lambat***, ***Joint Venture* — Sharing Risk and Capabilities***, **Kriteria Pemilihan Pendekatan**
- Acquisition: tercepat memasuki industri baru tetapi sering bayar premium (control premium 20–40%)
- Internal development: lebih murah secara nominal tetapi memerlukan waktu, biaya pembelajaran, dan risiko kegagalan eksekusi yang signifikan
- JV/strategic alliance: berbagi risiko investasi dan akses kapabilitas mitra; cocok ketika industri baru memerlukan kapabilitas yang tidak dimiliki dan terlalu mahal untuk dibangun sendiri
- Bold reasoning: pilihan pendekatan tergantung kompleksitas industri target, urgensi waktu, dan kapabilitas yang dimiliki vs. yang dibutuhkan
- Indonesian: Indofood akuisisi (Bogasari, Indolakto); GoTo merger (Gojek + Tokopedia sebagai JV-like consolidation); Pertamina-Eni JV di blok migas

Insert **Gambar 1 — Strategic Themes of Multibusiness Corporation (FIGURE 8.1)** here.

### §5 Pilihan Jalur: Diversifikasi *Related* vs. *Unrelated*
Sub-headings: ***Related Diversification* — Logika Cross-Business Strategic Fit**, ***Unrelated Diversification* — Logika Portfolio Risk Management**, **Bukti Empiris: Mana yang Lebih Berkinerja**, **Indonesian Examples**
- Related: bisnis-bisnis berbagi nilai-rantai yang dapat di-leverage (R&D, supply chain, distribusi, brand) — *economies of scope* (Panzar & Willig 1981; Teece 1980)
- Unrelated: bisnis-bisnis tidak berbagi nilai-rantai berarti — value creation harus berasal dari capital allocation superiority, financial engineering, atau operational discipline lintas industri
- Bold pivot: empirical research (Rumelt 1974, 1982; Markides & Williamson 1994) menunjukkan related diversification rata-rata superior dalam ROA dan shareholder return — meskipun *kondisional* pada eksekusi strategic fit yang baik
- Indonesian: Astra (related — value-chain fit di otomotif + heavy equipment + agribisnis melalui distribusi & finansial); Sinar Mas / Salim Group (unrelated — capital allocation logic); GoTo (related — platform fit antara transport + commerce + payment)

### §6 Diversifikasi ke Bisnis *Related*: *Strategic Fit* dan *Economies of Scope*
Sub-headings: **Definisi *Strategic Fit* di Level Korporat**, **Empat Tipe Cross-Business Value-Chain Fit**, ***Economies of Scope* vs. *Economies of Scale***, **Bagaimana Related Diversification Menciptakan Keunggulan Kompetitif**

This is a **central conceptual section** — write with extra density (700–900 words).

- *Strategic fit* di level korporat: kondisi di mana aktivitas-rantai-nilai dari bisnis-bisnis berbeda memiliki cukup kesamaan untuk memungkinkan transfer sumber daya, sharing aktivitas, atau cross-leverage kapabilitas dengan biaya marginal rendah
- Empat tipe value-chain fit (TPGS Ch.8): (1) supply chain fit; (2) R&D dan teknologi fit; (3) manufacturing fit; (4) sales/marketing/distribusi/brand fit
- Economies of scope: penurunan biaya per unit karena sharing aktivitas atau sumber daya lintas bisnis — berbeda dari economies of scale yang berasal dari volume dalam satu lini produk
- Bold reasoning: keunggulan kompetitif dari related diversification tidak otomatis — terealisasi hanya bila manajemen secara aktif mengeksploitasi fit melalui koordinasi lintas-divisi yang efektif
- Cite Kraft–Heinz merger illustration dari TPGS *Concepts & Connections 8.1* (p.159) sebagai contoh fit yang dieksekusi
- Indonesian: Astra Group cross-business fit (Toyota Astra + Astra Honda Motor + Astra International distribution + Astra Credit Companies finansial); BCA + Djarum Group financial-real-estate fit; GoTo cross-platform fit (GoFood merchant base → Tokopedia seller acquisition)

Insert **Gambar 2 — Cross-Business Value-Chain Strategic Fit (FIGURE 8.2)** here.

### §7 Diversifikasi ke Bisnis *Unrelated*: Logika *Conglomerate*
Sub-headings: **Mengapa Perusahaan Memilih *Unrelated Diversification***, **Bagaimana Unrelated Diversification Menciptakan Nilai**, **Tiga Jebakan *Unrelated Diversification***, **Mengapa *Misguided Reasons* Sering Mendorong Diversifikasi**
- Motivasi: portfolio risk diversification, opportunistic acquisition, capital allocation engine, cyclicality smoothing
- Sumber nilai potensial: superior capital allocation (Berkshire Hathaway model), operational discipline transfer, financial engineering
- Tiga jebakan: (1) demanding managerial requirements (top management harus menguasai dinamika banyak industri); (2) limited competitive advantage potential (tanpa value-chain fit, *parenting advantage* harus murni manajerial); (3) pursuit of risk reduction yang sering ilusi karena pemegang saham dapat diversifikasi sendiri lebih efisien melalui pasar modal
- Bold critique: *misguided reasons* — ego manajemen, kompensasi-by-size, defensive empire-building — sering menyamar sebagai strategic logic
- Indonesian: kompleksitas Salim Group post-1998 deleveraging (forced divestiture menunjukkan jebakan over-diversification); Bakrie Group sebagai contoh konglomerasi yang menghadapi tekanan re-focus

### §8 Mengevaluasi Strategi Perusahaan Terdiversifikasi: Kerangka 6-Langkah
Sub-headings: **Langkah 1: *Industry Attractiveness Assessment***, **Langkah 2: *Business-Unit Competitive Strength***, **Langkah 3: *Strategic Fit Across Businesses***, **Langkah 4: *Resource Fit***, **Langkah 5: *Ranking dan Resource Allocation***, **Langkah 6: *Crafting New Strategic Moves***

- Langkah 1: industry attractiveness scoring (Porter Five-Forces + market growth + profit volatility + strategic alignment + resource requirement)
- Langkah 2: business-unit competitive strength scoring (market share, cost position, brand, capability fit)
- Langkah 3: cross-business strategic fit assessment — mengidentifikasi di mana value-chain matchups menghasilkan resource transfer, cost sharing, atau cross-leverage
- Langkah 4: resource fit — apakah portofolio menuntut lebih dari yang dapat disediakan oleh sumber daya finansial dan manajerial
- Langkah 5: ranking dan priority — *grow and build* untuk attractive + strong; *defend & maintain* untuk attractive + medium; divestment candidates untuk unattractive + weak
- Langkah 6: strategic moves — invest more, retrench, restructure, divest

Insert **Gambar 3 — Nine-Cell Industry Attractiveness–Competitive Strength Matrix (FIGURE 8.3)** here, with interpretation of bubble plot ranking and Indonesian application example.

Insert **Gambar 4 — Strategic & Financial Resource Allocation Options (FIGURE 8.4)** here, with interpretation of strategic vs financial options trade-off.

### §9 Sintesis: *Strategic Fit* sebagai Kerangka Master di Tiga Level

This is the **central paradigmatic synthesis section** — write with extra density (900–1100 words).

Sub-headings: **Asal Kerangka Fit dan Contingency Theory**, **Tiga Level Strategic Fit dalam Pertemuan 7**, **Venkatraman (1989) Enam Perspektif Fit**, **Miles & Snow (1978) Typology dan Equifinality (Doty et al. 1993)**, **Jembatan Eksplisit ke Artikel 11 dan 12**

- Lawrence & Lorsch (1967) contingency: *no one best way* — struktur, strategi, dan sistem harus cocok dengan lingkungan internal dan eksternal
- **Level 1 — Cross-business fit (TPGS Ch.8):** fit antar-unit-bisnis di dalam perusahaan terdiversifikasi melalui value-chain matchups dan economies of scope
- **Level 2 — Internal business fit (Artikel 11):** fit antara strategi kompetitif bisnis, HR strategy, dan reward system di dalam satu unit bisnis
- **Level 3 — Organizational alignment fit (Artikel 12):** fit antara strategic fit (operationalisasi via 4Cs Medcof 1997: Capability, Compatibility, Commitment, Control) dan elemen-elemen desain organisasi (struktur, employee relations, information exchange)
- Venkatraman (1989) enam perspektif: fit as moderation, mediation, matching, gestalt, profile-deviation, covariation — masing-masing implikasi metodologis berbeda
- Miles & Snow (1978) typology (Defender, Prospector, Analyzer, Reactor) sebagai operasionalisasi *configurational fit* — Doty, Glick & Huber (1993) menambahkan *equifinality* yang menjadi salah satu pilar teoretis Artikel 12
- Nadler & Tushman (1980) definisi fit yang dipakai Artikel 12: *the degree to which the needs, demands, goals, objectives, and structures of one component match*
- Bold synthesis: setiap analisis di §2–§8 sesungguhnya pelaksanaan prinsip fit pada level yang berbeda — fit antara strategi diversifikasi dengan kondisi industri (test 1), fit antara biaya entri dengan kapabilitas (test 2), fit antara bisnis baru dengan portofolio existing (test 3)
- Hsieh & Chen (Artikel 11) memberi taksonomi internal fit yang konkret: differentiation → innovation-oriented HR → human capital reward; cost leadership → contribution-oriented HR → output reward; focus → commitment-oriented HR → position reward
- Okebaram & Onuoha (Artikel 12) memperluas konsep fit ke kerangka 4Cs dan menguji efeknya secara empiris pada 212 responden di Nigeria — keterbatasan metodologisnya kuat tetapi proposisi konseptualnya melengkapi Artikel 11 dengan dimensi organisasional yang lebih luas

### §10 Kesimpulan
Sub-headings: **Fit sebagai Proses Rekalibrasi Berkelanjutan di Setiap Level**, **Integrasi Pert. 4–7**, **Antisipasi Pert. 8 (Internasional)**
- Synthesis: corporate-level fit (Pert. 7) menambahkan dimensi cross-business pada konsep fit yang telah dibangun di Pert. 4–6
- Integration chain: RBV (Pert. 4) → strategi generik (Pert. 5) → penguatan posisi (Pert. 6) → corporate diversification (Pert. 7)
- Forward link: Pert. 8 menambahkan dimensi geografis — fit antara strategi korporat dengan konteks pasar internasional

---

## 5. Document 2 — Critical Review Artikel 11 (Hsieh & Chen 2011)

**Article:** Hsieh, Y. H. & Chen, H. M. (2011). *Strategic Fit among Business Competitive Strategy, Human Resource Strategy, and Reward System.* Academy of Strategic Management Journal, 10(2): 11–32.

**Format standard:** Same as RMK — sub-headings (###) within every section, bold for analytical pivots, italics for foreign terms. §7 Evaluasi Kritis dan §8 Implikasi dense (250–350 words each).

### §1 Identitas Artikel
Full bibliographic data; Academy of Strategic Management Journal context (Allied Academies, US-based peer-reviewed journal, conceptual orientation, ranked B/C tier in major business journal lists); authors' institutional affiliation (Tamkang University, Taiwan — explains Asian-firm conceptual framing); article type (**konseptual/literature-review murni** — tidak ada uji empiris, hanya proposisi configurational); penerbit Dreamcatchers Group LLC.

### §2 Tujuan Penelitian dan Posisi dalam Literatur
Sub-headings: **Pertanyaan Riset Utama**, **Posisi dalam Rantai Literatur Strategic Fit**
- Research question: bagaimana fit antara strategi kompetitif bisnis (generic strategies Porter), strategi HR, dan reward system mendukung kinerja organisasi dan keunggulan kompetitif?
- Gap yang diisi: literatur strategy-HRM (Schuler & Jackson 1987; Miles & Snow 1978, 1984; Dyer & Holder 1988) dan literatur HR-reward (Howard & Dougherty 2004; Gross & Friedman 2004; Armstrong & Brown 2005) berkembang relatif terpisah. Hsieh & Chen menyatukan keduanya ke dalam *triad fit* terpadu.
- Posisi terhadap Porter (1980, 1985) generic strategies; Schuler & Jackson (1987) strategic HRM typology (cost-reduction/innovation/quality-enhancement); Miles & Snow (1978) defender-prospector; Snow & Hrebiniak (1980) fit definition; RBV (Wernerfelt 1984, Barney 1991, Peteraf 1993)

### §3 Argumen Utama — *Strategic Fit Triad*
Sub-headings: **Komponen Triad yang Sebenarnya**, **Logika Fit untuk *Differentiation***, **Logika Fit untuk *Overall Cost Leadership***, **Logika Fit untuk *Focus***, **Hipotesis Konfigurasional**

Triad sebagaimana didefinisikan Hsieh & Chen (Tabel 1, hlm. 26):
- **Komponen 1 — Business competitive strategy:** Porter (1980, 1985) — differentiation, overall cost leadership, focus
- **Komponen 2 — HR strategy type:** Innovation-oriented, Contribution-oriented, Commitment-oriented (taksonomi yang dibangun penulis dari sintesis Schuler & Jackson 1987, Miles & Snow 1978, Dyer & Holder 1988)
- **Komponen 3 — Reward system type:** Human capital reward, Output reward, Position reward (taksonomi Howard & Dougherty 2004)

Tiga proposisi konfigurasional utama:
1. **Differentiation → Innovation-oriented HR → Human capital reward** (intrinsic): R&D, engineer, professional sebagai target; kriteria skill, knowledge, innovation, adaptability
2. **Overall cost leadership → Contribution-oriented HR → Output reward** (extrinsic): on-line producer, sales personnel sebagai target; kriteria performance, productivity, growth, profit
3. **Focus → Commitment-oriented HR → Position reward** (both intrinsic and extrinsic): managers, directors, senior staff sebagai target; kriteria title, seniority, responsibility, status

Bold pivot: argument konfigurasional Hsieh & Chen menyatakan bahwa misalignment di satu sudut triad menghasilkan tension yang menekan kinerja — *differentiation strategy + contribution-oriented HR + output reward* akan menghasilkan *innovation paralysis* karena reward fokus pada output jangka pendek bukan inovasi jangka panjang.

### §4 Koneksi ke Topik Silabus (Pertemuan 7)
Sub-headings: **Triad Fit sebagai Operasionalisasi *Internal Fit***, **Linking ke §9 RMK ke Artikel Ini**
- TPGS Ch.8 membahas *cross-business strategic fit* di level korporat — Hsieh & Chen mengkonkretisasi konsep fit pada level *intra-business* (di dalam satu unit bisnis)
- Jembatan analitis: bahkan setelah corporate-level menentukan diversifikasi yang lulus tiga tes (§3 RMK), setiap unit bisnis tetap memerlukan internal fit strategi-HR-reward agar eksekusi business-level berjalan — Hsieh & Chen menyediakan kosakata untuk diagnosis fit internal tersebut

### §5 Kekuatan Artikel
Sub-headings: **Kontribusi Teoretis: Integrasi Dua Aliran Literatur**, **Kejelasan Kerangka untuk Aplikasi Manajerial**, **Akar Teoretis yang Solid**
- Kontribusi teoretis genuine: menyatukan literatur strategy-HRM (Schuler & Jackson lineage) dengan literatur HR-reward (Howard & Dougherty taxonomy) yang sebelumnya berkembang terpisah
- Framework dapat dipakai sebagai *diagnostic tool* — manajer dapat memeriksa apakah strategi bisnisnya konsisten dengan tipe HR dan reward system yang diterapkan
- Bold appreciation: tipologi konfigurasional membuat trade-off eksplisit dan dapat-diuji — berbeda dari rekomendasi HR "best practice" yang sering bebas-konteks

### §6 Keterbatasan dan Kelemahan
Sub-headings: **Sifat Konseptual Tanpa Uji Empiris**, **Pengabaian Dinamika Temporal**, **Ketergantungan pada Porter's Typology**, **Konteks Kultural Tidak Dibahas**, **Tidak Ada Diskusi Reverse Causality**
- **Limitasi utama (diakui penulis sendiri pada Kesimpulan hlm. 27):** artikel sepenuhnya konseptual — proposisi belum diuji statistik. Authors menutup dengan "Future research should make greater effort to integrate theoretical and empirical data to verify the practicability of this framework."
- Tidak memodelkan *dynamic-fit problem*: bagaimana triad menyesuaikan ketika strategi bertransisi dari cost leadership ke differentiation; transition cost dan path dependency tidak dibahas
- Ketergantungan penuh pada tipologi Porter — Kotha & Vadlamani (1995) telah menunjukkan keterbatasan measurement validitas Porter's generic strategies; bila tipologi anchor lemah, triad yang dibangun di atasnya juga rentan
- Implisit Taiwanese context (institusi penulis, tetapi tidak ada diskusi kultural) — generalisasi ke Indonesia (post-colonial, state-corporatist, mixed-ownership, Pancasila-based labor relations) tidak otomatis
- Tidak membahas potensi reverse causality: perusahaan dengan HR fleksibel dan reward variable mungkin *memilih* differentiation karena memang memiliki kapabilitas, bukan karena strategi differentiation menentukan HR

### §7 Evaluasi Kritis
Sub-headings: **Apakah Fit Triad Benar-Benar *Configurational* atau Hanya *Additive*?**, **Masalah Operasionalisasi: Bagaimana Mengukur Triad-Misalignment?**, **Apa yang Seharusnya Dilakukan**, **Penilaian Kontribusi Orisinal**
- **Critique inti:** Hsieh & Chen mengklaim konfigurasi (Miller 1988; Doty et al. 1993 sense — *equifinality* dengan non-linearitas) tetapi argumentasi sering slip ke fit *aditif* (Venkatraman 1989) — perbedaannya konsekuensial: konfigurasi mengasumsikan bahwa *seluruh* konfigurasi yang penting, additive mengizinkan substitusi parsial antar elemen
- Operasionalisasi: artikel tidak menjelaskan bagaimana praktisi atau peneliti mengukur "fit" yang dimaksud — apakah dengan deviation score, gestalt clustering, atau qualitative case-comparison?
- Apa yang seharusnya: configurational empirical test dengan cluster analysis (Ketchen et al. 1997) atau set-theoretic methods (Ragin 2008 fsQCA); longitudinal panel untuk memisahkan sebab-akibat antara strategi → HR → reward
- Penilaian: kontribusi teoretis valid sebagai *agenda-setting framework* dan berguna untuk pedagogi MBA/MAk; sebagai *predictive theory* artikel berada di tier 2 — useful heuristic dengan janji empiris yang belum ditebus

### §8 Implikasi bagi Pemahaman Manajemen Strategik
Sub-headings: **Implikasi Teoretis**, **Implikasi Manajerial**, **Implikasi untuk Konteks Indonesia**
- Theoretical: memperkuat *internal fit* sebagai dimensi yang tidak boleh diabaikan dalam analisis strategi — strategi sukses adalah strategi yang seluruh sistem internal mendukungnya secara konsisten
- Managerial: HR director dan compensation committee harus diundang ke meja strategi, bukan sekedar implementer downstream — pesan langsung dari Hsieh & Chen ke senior management
- Indonesian: **Astra International** triad fit antara diversified-related strategy + HR rotation across business units + KPI-based variable reward (Astra Management System); **Bank Mandiri** post-merger triad reconfiguration 2005–2010 (cost leadership pada retail banking + standardized HR + cost-control reward dengan KPI cascade BSC); **Unilever Indonesia** differentiation + innovation-HR (Unilever Future Leaders Program) + long-term performance reward; **kasus negatif** — BUMN dengan strategi differentiation tetapi HR-reward birokratik (struktur kepangkatan PNS-style + reward berbasis golongan) menghasilkan *execution gap* yang konsisten

### §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut
Sub-headings: **Pertanyaan Terbuka**, **Relevansi untuk Riset Indonesia**
- Apakah triad fit berlaku universal atau berbeda di konteks family-owned vs. publicly-listed firm?
- Bagaimana triad menyesuaikan dalam transisi strategi (transformasi digital, ESG pivot, M&A integration)?
- Indonesia-specific: apakah dual-track HR system di BUMN (PNS-style + market-style) merusak triad fit secara struktural?
- Apakah platform-business model (Gojek, Tokopedia, Shopee) memerlukan triad keempat: HR-reward-*algorithmic-management* fit (gig workers, dynamic pricing, algorithmic performance scoring)?

---

## 6. Document 3 — Critical Review Artikel 12 (Okebaram & Onuoha 2018)

**Article:** Okebaram, S. M. & Onuoha, C. E. (2018). *Implication of Strategic Fit and Sustainability on Organizational Effectiveness.* The 2018 International Academic Research Conference in Vienna, pp. 194–213.

**Format standard:** Same as CR11 and RMK — sub-headings within every section, bold for analytical pivots, italics for foreign terms. Especially dense in §7 and §8.

### §1 Identitas Artikel
Full bibliographic data; venue context (International Academic Research Conference in Vienna — conference paper venue, tier lower than top-quartile SSCI journals, peer review process less rigorous); authors' Nigerian institutional context (Okebaram dari Michael Okpara University of Agriculture; Onuoha dari University of Science and Technology Enugu — explains Nigerian-firm empirical anchoring); article type (**empirical study** dengan survey design + Z-test — bukan murni konseptual seperti banyak conference papers). Catatan penting: penulis menggunakan data "Field Survey 2014" untuk paper 2018 — undisclosed empirical lag empat tahun.

### §2 Tujuan Penelitian dan Posisi dalam Literatur
Sub-headings: **Pertanyaan Riset dan Tiga Hipotesis Null**, **Posisi dalam Literatur Strategic Fit**
- Research question: bagaimana implikasi strategic fit (operasionalisasi via Medcof 1997 *4Cs*) terhadap *organizational effectiveness* melalui tiga jalur — organization design, employee relations, dan information exchange?
- Tiga hipotesis null yang diuji: (H₀1) Strategic organization design tidak meningkatkan organizational effectiveness; (H₀2) Strategic fit tidak mempertahankan employee relations untuk meningkatkan effectiveness; (H₀3) Strategic fit tidak meningkatkan information exchange untuk meningkatkan effectiveness — ketiganya ditolak (Z = 5.342, 5.677, 5.745; p < .001)
- Posisi terhadap literatur: Porter (1985) sustained competitive advantage; Nadler & Tushman (1980) fit definition; Miles & Snow (1978) typology; Doty, Glick & Huber (1993) configurational theories dan equifinality; Zajac, Kraatz & Bresser (2000) dynamic fit; Medcof (1997) 4Cs framework; Shelton (1988) M&A strategic fit; Ireland, Hitt & Vaidyanath (2002) alliance management

### §3 Argumen Utama — *Strategic Fit + 4Cs* terhadap Organizational Effectiveness
Sub-headings: **Konseptualisasi Strategic Fit (Nadler & Tushman 1980)**, **Kerangka *4Cs* Medcof (1997)**, **Mekanisme Kausal yang Diuji**, **Temuan Empiris**

- Strategic fit didefinisikan dari Nadler & Tushman (1980): *the degree to which the needs, demands, goals, objectives, and structures of one component match* — penulis menambahkan: *strategic fit expresses the degree to which an organization is matching its resources and capabilities with the opportunities in the external environment* (hlm. 195)
- Kerangka **4Cs Medcof (1997):** *Capability, Compatibility, Commitment, Control* — sebagai operasionalisasi strategic fit dalam konteks M&A/strategic alliance dan organizational design
- Mekanisme kausal yang diajukan dan diuji: Strategic fit (4Cs) → tiga jalur organisasional (organization design, employee relations, information exchange) → organizational effectiveness / sustained competitive advantage
- Temuan empiris: ketiga jalur signifikan (Z-test menolak null pada p < .001); kesimpulan penulis (hlm. 210): *organizations can achieve synergy and sustain their organizational effectiveness by integrating the element of 4Cs capability, compatibility, commitment and control with the appropriate organization design, good employee relations and effective information exchange*
- Bold note: judul artikel mencantumkan *sustainability* tetapi konseptualisasi penulis sebenarnya merujuk pada *sustained competitive advantage* (Porter 1985) — bukan *triple bottom line* (Elkington 1997) atau *natural-resource-based view* (Hart 1995). Penggunaan istilah ini longgar dan potensial menyesatkan pembaca

### §4 Koneksi ke Topik Silabus (Pertemuan 7)
Sub-headings: **4Cs sebagai Operasionalisasi Strategic Fit di Level Multibusiness/Alliance**, **Linking ke §9 RMK dan Artikel 11**
- TPGS Ch.8 membahas cross-business strategic fit di level korporat — Okebaram & Onuoha menyediakan operasionalisasi yang lebih granular melalui 4Cs (terutama relevan untuk M&A dan alliance, di mana strategic fit menentukan post-integration success)
- Jembatan analitis: Artikel 11 fokus pada internal fit (strategy-HR-reward di dalam satu unit bisnis); Artikel 12 fokus pada multi-element organizational alignment (4Cs + org design + employee relations + info exchange) — kedua dimensi sama-sama operasionalisasi prinsip fit di §9 RMK pada level yang berbeda

### §5 Kekuatan Artikel
Sub-headings: **Topik yang Relevan secara Manajerial**, **Operasionalisasi via 4Cs**, **Uji Empiris (Berbeda dari Banyak Conference Papers)**
- Topik relevan: M&A failure rates 50–60% (Bamford, Gomes-Casseres & Robinson 2004, dikutip oleh penulis) — kebutuhan kerangka diagnostik fit yang konkret untuk praktisi
- Operasionalisasi via 4Cs (Medcof 1997) memberikan kerangka yang aplikatif untuk diagnostic check pre-merger atau pre-alliance
- Uji empiris dengan N=212 (di atas threshold Yamane untuk populasi 450) — meningkatkan kontribusi di atas conference paper konseptual rata-rata

### §6 Keterbatasan dan Kelemahan
Sub-headings: **Definisi *Sustainability* yang Longgar dan Berpotensi Menyesatkan**, **Empirical Lag Empat Tahun yang Tidak Diungkapkan**, **Metodologi Statistik yang Diragukan**, **Tidak Ada Validitas/Reliabilitas Konstruk**, **Basis Empiris Nigeria-Spesifik**, **Methodological Disclosure yang Minim**
- **Limitasi paling kritis:** istilah *sustainability* dalam judul tidak pernah didefinisikan secara eksplisit dalam kerangka *triple bottom line* (Elkington 1997) atau natural-resource-based view (Hart 1995) — penulis tampaknya menggunakan *sustainability* untuk merujuk *sustained competitive advantage* (Porter 1985). Bila pembaca mengharapkan diskusi environmental/social sustainability, judul menyesatkan
- Empirical lag: data "Field Survey 2014" digunakan untuk conference paper 2018 — empat tahun tidak diungkap; perubahan industri telekomunikasi dan perbankan Nigeria 2014–2018 substansial dan tidak diakomodasi
- Z-test pada mean Likert score adalah praktik statistik yang meragukan; Kolmogorov-Smirnov yang digunakan menguji normalitas distribusi, bukan hipotesis tentang means — ada konflasi metodologi
- Tidak ada disclosure Cronbach alpha, construct validity, factor structure untuk 4Cs; uji statistik tanpa validasi konstruk = "garbage in, garbage out"
- Basis empiris: tiga operator telekomunikasi (MTN, Airtel, Etisalat) + satu bank (Ecobank) di Nigeria — generalisasi terbatas pada satu negara, dua sektor terkonsentrasi
- Profil demografis responden tidak dilaporkan — mustahil menilai keterwakilan sampel

### §7 Evaluasi Kritis
Sub-headings: **Konflasi *Sustainability* dan *Sustained Competitive Advantage***, **Eclecticism Teoretis sebagai Kelemahan**, **Klaim Kausal Berlebihan dari Survei Cross-Sectional**, **Gap Literatur: Yang Seharusnya Dikutip tapi Tidak**, **Apa yang Seharusnya Dilakukan**, **Penilaian Kontribusi Orisinal**

- **Critique inti #1 — sustainability/SCA conflation:** judul artikel menjanjikan analisis sustainability tetapi konten membahas sustained competitive advantage. **Bila penulis memang bermaksud TBL sustainability, artikel ini gagal mengkonseptualisasi maupun mengoperasionalisasi dimensi tersebut.** Bila penulis memang membahas SCA, judul seharusnya tidak menggunakan istilah *sustainability* yang sudah memiliki makna teknis spesifik dalam literatur manajemen strategik post-Elkington (1997).
- Eclecticism teoretis: meminjam dari Porter (1985), Miles & Snow (1978), Nadler & Tushman (1980), Medcof (1997), Doty et al. (1993), Zajac et al. (2000), Shelton (1988), Hoffmann (2007), Day (2000), Grant (2007) — tanpa adjudikasi kapan satu teori menggantikan yang lain. Hasilnya: framework yang terdengar komprehensif tetapi tidak menghasilkan testable predictions yang spesifik
- Klaim kausal berlebihan: survey cross-sectional dengan Z-test pada Likert means tidak dapat membangun causation — penulis menyimpulkan bahwa fit *menyebabkan* effectiveness, padahal data hanya menunjukkan *asosiasi*. Reverse causality (perusahaan yang efektif lebih mampu mencapai fit) maupun common cause (organizational maturity menyebabkan keduanya) tidak diuji
- **Gap literatur yang signifikan:** artikel tidak mengutip Venkatraman (1989) "The Concept of Fit in Strategy Research" — kontribusi konseptual paling penting dalam literatur strategic fit dalam tiga dekade terakhir. Tidak mengutip Lawrence & Lorsch (1967) — induk kerangka contingency. Tidak mengutip Elkington (1997) — padahal sustainability ada di judul. Tidak mengutip Hart (1995) atau Porter & Kramer (2006) — kontribusi penting untuk sustainability-as-strategy. Bila ada satu test paling parsimonious untuk kualitas tinjauan pustaka, artikel ini gagal: penulis tidak menemukan atau tidak menggunakan literatur fundamental
- Apa yang seharusnya dilakukan: definisi eksplisit *sustainability*; uji structural equation modeling dengan validated constructs untuk 4Cs; longitudinal design untuk menguji causation; multi-industry, multi-country sample; integrasi eksplisit dengan literatur strategic fit klasik (Venkatraman, Lawrence & Lorsch)
- Penilaian: artikel useful sebagai *agenda-setting piece* dalam konteks Nigerian management research dan sebagai bahan diskusi kelas (Sociology of Management Research) tentang bagaimana paper conference dengan eksekusi metodologis yang terbatas tetap dapat mengangkat topik penting. Sebagai *scholarly contribution*, terlalu banyak limitasi metodologis untuk membuat klaim kausal yang dipublikasikan dapat dipertahankan

### §8 Implikasi bagi Pemahaman Manajemen Strategik
Sub-headings: **Implikasi Teoretis**, **Implikasi Manajerial**, **Implikasi untuk Konteks Indonesia**

- Theoretical: artikel *seharusnya* menjadi extension dari Lawrence & Lorsch (1967) ke era post-shareholder-primacy dengan dimensi stakeholder dan sustainability — tetapi gagal karena eksekusi konseptual dan metodologis terbatas. **Pelajaran teoretis:** kerangka fit memerlukan operasionalisasi yang konsisten dan empirical anchor yang valid; hanya istilah "fit" tidak cukup untuk membentuk kontribusi
- Managerial: meskipun artikel terbatas, message bahwa M&A dan alliance memerlukan 4Cs diagnostic check (Medcof 1997) tetap valid sebagai praktis. Bagi praktisi M&A, *pre-deal due diligence* yang mencakup keempat C (capability fit, compatibility, commitment, control) lebih kuat daripada due diligence finansial murni
- Indonesian: **Bank Mandiri** post-merger 4Cs integration (empat bank legacy: Bank Bumi Daya, Bank Dagang Negara, Bank Ekspor Impor, Bank Pembangunan Indonesia) — capability fit assessed via portfolio rationalization; compatibility via cultural integration; commitment via senior leadership alignment; control via centralized risk management; **Astra International acquisition track record** (Astra Daihatsu Motor, AHM, KOMATSU partnership) — konsisten dengan 4Cs framework; **GoTo merger** (Gojek + Tokopedia 2021) — Indonesia's largest fit test, dengan compatibility challenges yang tetap menjadi pertanyaan empiris; **kasus tension** — industri batu bara Indonesia (Adaro, Bayan) menghadapi misfit struktural dengan global ESG capital flow (kasus di mana *sustainability sebenarnya — TBL Elkington 1997* relevan, bukan sekedar *sustained advantage* sebagaimana didefinisikan Okebaram & Onuoha)

### §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut
Sub-headings: **Pertanyaan Terbuka**, **Relevansi untuk Riset Indonesia**
- Bila kita memisahkan *sustainability* (Elkington TBL) dari *sustained competitive advantage* (Porter), bagaimana keduanya berinteraksi dalam praktik korporat?
- Apakah 4Cs Medcof (1997) dapat dioperasionalisasi dengan konstruk yang divalidasi melalui SEM/CFA — atau apakah konsep ini terlalu lentur untuk pengukuran formal?
- Indonesia-specific: bagaimana institutional voids (Khanna & Palepu 2000) — pasar modal yang belum dalam, regulasi yang fragmented, kontrak yang sulit ditegakkan — mempengaruhi 4Cs assessment dalam M&A Indonesia?
- Microfoundation: apakah board diversity, ESG-linked compensation, dan stakeholder engagement structures cukup untuk menghasilkan substantive sustainability fit, atau hanya symbolic compliance?

---

## 7. Writing Quality Requirements

- Indonesian akademik; PUEBI/KBBI compliant
- Foreign/English terms italicized on first use per section; Indonesian gloss where useful
- **Rich formatting throughout all three documents:** ### sub-headings within every major section; **bold** for key concept definitions, analytical pivots, critical reasoning conclusions; *italics* for foreign terms
- Each sub-section 150–300 words of substantive analysis — not a label followed by one sentence
- No hyphen ("-") as sentence/clause connector; reduplication `kata - kata` style (with spaces) per user preference
- No Daftar Pustaka; inline citations only: (Penulis tahun) or "menurut Penulis (tahun, hlm. X)"
- Primary-text engagement: direct paraphrase and short quotations with page references from both PDFs and TPGS Ch.8
- No AI-generic phrases ("delve into", "navigate the landscape", "in conclusion", "it is important to note")
- Scholarly voice: senior-analyst Indonesian academic, direct claims, evidence-grounded critiques
- Indonesian examples from publicly verifiable corporate histories only
- **Citation accuracy:** for Artikel 11 and Artikel 12, only cite authors actually cited in the original paper. For comparative reference (Venkatraman 1989, Lawrence & Lorsch 1967, Elkington 1997, etc. — citations that exist in classical literature but NOT in Artikel 12), use these as *external critical reference points* clearly marked as "literature gap yang seharusnya diakui penulis" — do not attribute these to the original author.

---

## 8. Figure Embedding Specification (RMK only)

- **Source:** TPGS Ch.8 PDF pages, extracted via PyMuPDF (fitz)
- **Output format:** PNG, 200 DPI minimum, RGB
- **Storage:** `Dev Assistant/temp/ch8_figures/figure_8_N.png`
- **Caption format:** *Gambar N. Judul deskriptif (Sumber: TPGS 2021, Ch.8, hlm. X)*
- **Placement:** After the sub-section that introduces the concept; preceded by a transitional sentence (e.g., "Pendekatan diversifikasi yang utama divisualisasikan pada Gambar 1…") and followed by 2–3 sentences interpreting the figure
- **Selection (final 4 figures):** All 4 available figures in Essentials Ch.8 — Figure 8.1, 8.2, 8.3, 8.4 — embedded inline as detailed in §3

---

## 9. Out of Scope

- Daftar Pustaka (explicitly excluded, consistent with all prior pertemuan)
- HTML outputs (separate MSK304 spec)
- Articles from other pertemuan
- Henry textbook chapters (user-confirmed: TPGS Ch.8 only for this Pertemuan)
- Visual companion / browser mockups (text-only assignment)
- TBL/sustainability deep-dive (Artikel 12 does not invoke this framework; critique it for *not* doing so rather than synthesizing one)
- Empirical re-analysis of Artikel 12 dataset (critique methodology, do not attempt to validate it)
