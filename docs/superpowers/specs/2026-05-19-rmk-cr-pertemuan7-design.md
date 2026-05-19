# Design Spec — RMK + CR Submission, Pertemuan 7

- **Assignment:** RMK + CR Pertemuan 7 (Tugas Manajemen Strategik Kontemporer)
- **Student:** Dzaki Muhammad Yusfian | NIM: 1125 01079
- **Course:** MST304 — Manajemen Strategik Kontemporer, STIE YKPN
- **Spec date:** 2026-05-19
- **Status:** Approved
- **Analytical depth standard:** Pert. 6 standard + paradigmatic synthesis. Strategic Fit / Contingency Theory threaded explicitly as master frame across all three documents — Venkatraman (1989) six fit perspectives, Miles & Snow (1978) typology, Lawrence & Lorsch (1967) contingency principle invoked as analytical scaffold. Rich sub-heading + bold/italic formatting throughout; 150–300 word substantive sub-sections.

---

## 1. Assignment

Buat RMK dan Critical Review untuk materi dan artikel Pertemuan 7 sesuai silabus.

**Pertemuan 7 topic:** *Tailoring Strategy to Fit Specific Industry and Company Situations* (TPGS Ch.8)

**References:**
- TPGS Ch.8 (Gamble, Peteraf & Thompson 2021) — primary textbook anchor
- Article 11: Hsieh, Y. H. & Chen, H. M. (2011), *Strategic Fit among Business Competitive Strategy, Human Resource Strategy, and Reward System*, Academy of Strategic Management Journal, 10(2): 11–32
- Article 12: Okebaram, S. M. & Onuoha, C. E. (2018), *Implication of Strategic Fit and Sustainability on Organizational Effectiveness*, International Academic Research Conference in Vienna

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

Pattern follows `generate_rmk6_enhanced.py` (figure-enabled variant): writes Markdown to `Dev Assistant/temp/`, calls pandoc with `reference.docx`, outputs DOCX to the paths in §2. Figure extraction step uses PyMuPDF (fitz) on the TPGS PDF, restricted to Ch.8 pages, exporting PNG/JPG to `Dev Assistant/temp/figures_w7/` and referenced from Markdown via standard `![caption](path)` syntax.

**Formatting:** Times New Roman 12pt body; 14pt centered bold Heading 1; 12pt bold Heading 2; 12pt bold italic Heading 3; margins 3cm / 2.5cm; line spacing 1.5; first-line indent 1.25cm. Figure captions centered, 11pt italic, format *Gambar X. Judul Gambar (Sumber: TPGS 2021, hlm. Y)*.

**Figure plan:** 3–5 figures from TPGS Ch.8 embedded inline. Target candidates (final selection during implementation):
1. Industry life-cycle stages diagram (emerging → growth → maturity → decline)
2. Strategic options matrix for fragmented industries
3. Turnaround / retrenchment decision flow
4. Strategy-situation fit summary chart
5. (Optional) Five-forces overlay per industry stage

---

## 4. Document 1 — RMK Pertemuan 7

**Header:**
```
RINGKASAN MATERI KULIAH — PERTEMUAN 7
Mata Kuliah: MST304 — Manajemen Strategik Kontemporer
Mahasiswa: Dzaki Muhammad Yusfian | NIM: 1125 01079
```

**Format standard (critical):** Every section uses sub-headings (###) to break content into 2–5 analytical sub-angles. Bold for key concept definitions, critical reasoning pivots, "why this matters" moments. Italics for all foreign terms first use per section. Each sub-section 150–300 words of substantive analysis. Figures embedded inline at logical reading positions, each preceded by a 1-line scene-setter and followed by 2–3 sentence interpretation (not bare image dumps).

### §1 Pendahuluan
Sub-headings: **Dari Pemilihan Strategi ke Penyesuaian Situasional**, **Mengapa Satu Strategi Generik Tidak Universal**, **Pertanyaan Pengarah Pertemuan 7**
- Transisi Pert. 6 (penguatan posisi) → Pert. 7 (pencocokan strategi dengan kondisi industri & posisi perusahaan)
- Bold pivot: strategi tanpa konteks adalah *template*, bukan keputusan — pencocokan situasional adalah inti seni manajemen strategik
- Bridge ke *strategic fit* sebagai konsep payung yang akan disintesiskan di §9

### §2 Strategi pada *Emerging Industries*
Sub-headings: **Karakteristik Industri Baru**, **Risiko Dominant-Design Race**, **Pilihan Strategis: Pioneer vs. Fast Follower**, **Indonesian Examples**
- Definisi industri *emerging*: ketidakpastian teknologi, ketiadaan standar dominan, segmen pelanggan belum stabil
- Bold reasoning: kapan menjadi pioneer rasional (network-effect markets, learning-curve steep) vs. kapan late-mover wajar (high technological uncertainty)
- Anderson & Tushman (1990) *dominant design* dynamics
- Indonesian: Gojek di on-demand transport (pioneer); Tokopedia di e-commerce era awal; eFishery di aquatech *emerging*

### §3 Strategi pada *Rapidly Growing Industries*
Sub-headings: **Logika Share-Grab**, **Capacity Pre-emption**, **Brand-Building dalam Jendela Pertumbuhan**, **Bahaya Over-Expansion**
- Bold pivot: pertumbuhan industri menciptakan jendela sempit untuk mengunci pangsa pasar — kegagalan menangkap pertumbuhan = kehilangan permanen
- Capacity pre-emption sebagai komitmen kredibel (Ghemawat 1991, *Commitment*)
- Trade-off: kecepatan vs. profitabilitas jangka pendek
- Indonesian: Shopee menggusur Lazada di growth phase e-commerce; BCA mobile banking capacity pre-emption; Mixue rapid expansion di F&B affordable

### §4 Strategi pada *Maturing Industries*
Sub-headings: **Tanda-Tanda Maturitas**, **Konsolidasi dan Shake-Out**, **Cost Discipline sebagai Default**, **Differentiation Refresh sebagai Counter-Strategy**, **Indonesian Examples**
- Demand growth melambat, capacity exceeds demand, intensitas persaingan harga meningkat
- Bold critique: perusahaan yang gagal menyesuaikan dari growth mindset ke efficiency mindset paling sering menjadi target akuisisi atau bangkrut
- Differentiation refresh — Apple di smartphone, Coca-Cola di minuman ringan
- Indonesian: Indomie *premium variant* expansion; Aqua diferensiasi vs. private label; Telkomsel cost discipline di mature voice market

### §5 Strategi pada *Stagnant or Declining Industries*
Sub-headings: **Tiga Pilihan Utama**, **Harvest vs. Niche vs. End-Game**, **Porter's Declining Industry Framework**, **Indonesian Examples**
- Harvest strategy: maksimalkan cash flow dengan minim investasi
- Niche strategy: identifikasi segmen yang tetap menguntungkan (Hambrick 1985)
- End-game: keluar dengan timing optimal
- Bold reasoning: kunci adalah *honesty* — banyak perusahaan menolak menerima decline phase dan menghancurkan nilai dengan investasi defensif yang tidak rasional
- Indonesian: industri rokok kretek (Sampoerna niche premium); industri media cetak (Kompas niche quality vs. Tempo digital pivot); industri taksi konvensional (Blue Bird hybrid digital reposition)

### §6 Strategi pada *Turbulent / High-Velocity Industries*
Sub-headings: **Definisi Hypercompetition (D'Aveni 1994)**, **Dynamic Capabilities Framework (Teece 1997)**, **Real-Options Reasoning**, **Indonesian Examples**
- Industri di mana keunggulan kompetitif erosi cepat (D'Aveni 1994; McGrath 2013 *transient advantage*)
- Dynamic capabilities: sense, seize, transform (Teece, Pisano & Shuen 1997)
- Real-options reasoning (McGrath & MacMillan 2000): investasi tahap-bertahap dengan opsi keluar
- Indonesian: industri fintech P2P (OVO/Dana/GoPay adaptasi cepat); industri ride-hailing post-pandemi; e-commerce flash-sale wars

### §7 Strategi pada *Fragmented Industries*
Sub-headings: **Penyebab Fragmentasi**, **Pilihan: Konsolidasi vs. Spesialisasi**, **Geographic Specialization**, **Indonesian Examples**
- Penyebab struktural: low entry barriers, diseconomies of scale, taste heterogeneity, regulasi lokal
- Konsolidasi play: McDonald's di fragmented quick-service; Starbucks di kopi specialty
- Geographic specialization: bertumbuh dalam segmen lokal sebelum nasional
- Indonesian: Alfamart/Indomaret consolidating fragmented retail; Kopi Kenangan/Janji Jiwa geographic-then-national; warung digitalization (Mitra Bukalapak)

### §8 Strategi untuk *Runner-Up*, *Weak-Position*, dan *Crisis-Ridden* Companies
Sub-headings: **Strategi untuk Runner-Up**, **Strategi untuk Weak-Position**, **Turnaround Sequencing untuk Crisis-Ridden**, **Indonesian Examples**
- Runner-up: vacant-niche, specialist, growth-via-acquisition, distinctive-image
- Weak-position: abandon, harvest, retrench, turnaround — pilihan tergantung kelayakan dan urgensi
- Turnaround sequencing (Hofer 1980; Pearce & Robbins 1993): stabilisasi → restrukturisasi → revitalisasi
- Bold critique: turnaround yang lompat ke revitalisasi sebelum stabilisasi hampir selalu gagal
- Indonesian: Garuda Indonesia restrukturisasi (post-PKPU 2022); Telkomsel runner-up shift to dominant; Bank Mandiri post-1998 turnaround sequencing

### §9 Sintesis: *Strategic Fit* sebagai Kerangka Master
Sub-headings: **Asal Kerangka Fit (Lawrence & Lorsch 1967)**, **Venkatraman (1989) Enam Perspektif Fit**, **Miles & Snow (1978) Typology sebagai Fit-Configurational**, **Jembatan ke Artikel 11 dan 12**
- Lawrence & Lorsch (1967) contingency: tidak ada *one best way*; struktur dan strategi harus cocok dengan lingkungan
- Venkatraman (1989) enam perspektif: fit as moderation, mediation, matching, gestalt, profile-deviation, covariation — masing-masing implikasi metodologis berbeda
- Miles & Snow (1978) tipologi (Defender, Prospector, Analyzer, Reactor) sebagai operasionalisasi configurational fit
- Bold synthesis: setiap pilihan di §2–§8 sesungguhnya pelaksanaan prinsip fit pada level berbeda — fit antara strategi dengan tahap industri, fit antara strategi dengan posisi kompetitif, fit antara strategi dengan kapabilitas internal
- Hsieh & Chen (Artikel 11): fit antara strategi bisnis–HR–reward (internal fit)
- Okebaram & Onuoha (Artikel 12): fit antara strategi–sustainability (external fit)

### §10 Kesimpulan
Sub-headings: **Fit sebagai Proses Rekalibrasi Berkelanjutan**, **Integrasi Pert. 4–7**, **Antisipasi Pert. 8 (Internasional)**
- Synthesis: fit bukan kondisi statis — perubahan tahap industri, masuknya kompetitor, atau pergeseran kapabilitas internal memerlukan rekalibrasi terus-menerus
- Integration chain: RBV (Pert. 4) → strategi generik (Pert. 5) → penguatan posisi (Pert. 6) → pencocokan situasional (Pert. 7)
- Forward link: Pert. 8 menambahkan dimensi geografis — fit antara strategi dengan konteks pasar internasional

---

## 5. Document 2 — Critical Review Artikel 11 (Hsieh & Chen 2011)

**Article:** Hsieh, Y. H. & Chen, H. M. (2011). *Strategic Fit among Business Competitive Strategy, Human Resource Strategy, and Reward System.* Academy of Strategic Management Journal, 10(2): 11–32.

**Format standard:** Same as RMK — sub-headings (###) within every section, bold for analytical pivots, italics for foreign terms. §7 Evaluasi Kritis dan §8 Implikasi dense (250–350 words each).

### §1 Identitas Artikel
Full bibliographic data; Academy of Strategic Management Journal context (Allied Academies, US-based peer-reviewed journal, conceptual orientation); authors' institutional affiliation (Taiwanese academic context — explains Asian-firm empirical framing); article type (theoretical-conceptual with Taiwanese case illustrations).

### §2 Tujuan Penelitian dan Posisi dalam Literatur
Sub-headings: **Pertanyaan Riset Utama**, **Posisi dalam Rantai Literatur Strategic Fit**
- Research question: bagaimana fit antara strategi kompetitif bisnis, strategi HR, dan reward system mempengaruhi keunggulan kompetitif?
- Gap yang diisi: literatur sebelumnya membahas strategy–HR fit (Schuler & Jackson 1987) atau HR–reward fit (Gomez-Mejia & Balkin 1992) secara terpisah; Hsieh & Chen menyatukan keduanya dalam *triad fit*
- Posisi terhadap Porter (1985) generic strategies; Schuler & Jackson (1987) strategic HRM; Gomez-Mejia & Balkin (1992) compensation strategy

### §3 Argumen Utama — *Strategic Fit Triad*
Sub-headings: **Komponen Triad**, **Logika Fit untuk Cost Leadership**, **Logika Fit untuk Differentiation**, **Logika Fit untuk Focus Strategy**, **Hipotesis Konfigurasional**
- Triad: business competitive strategy ↔ HR strategy ↔ reward system
- Cost leadership → efficiency-oriented HR (tight job design, behavior-based control) → fixed/seniority-based reward
- Differentiation → innovation-oriented HR (broad job design, results-based control) → variable/performance-based reward
- Focus → adaptive hybrid HR → mixed reward configuration
- Bold pivot: misalignment di salah satu sudut triad menghasilkan tension yang menekan kinerja — example, differentiation strategy + cost-based HR + fixed reward = innovation paralysis
- Configurational hypothesis: yang penting bukan elemen tunggal melainkan kesesuaian *seluruh* konfigurasi (Miller 1986; Doty, Glick & Huber 1993)

### §4 Koneksi ke Topik Silabus (Pertemuan 7 — TPGS Ch.8)
Sub-headings: **Triad Fit sebagai Operasionalisasi Internal Fit**, **Linking §9 RMK ke Artikel Ini**
- Triad Hsieh & Chen mengkonkretisasi konsep *internal fit* yang disinggung TPGS Ch.8 ketika membahas pencocokan strategi dengan kapabilitas organisasi
- Jembatan analitis: pilihan strategi pada industri tertentu (§2–§8 RMK) memerlukan konfigurasi HR-reward yang konsisten — strategi tanpa dukungan sistem HR-reward menjadi *paper strategy*

### §5 Kekuatan Artikel
Sub-headings: **Kontribusi Teoretis**, **Kejelasan Kerangka**, **Relevansi Praktis bagi Manajer**
- Kontribusi teoretis genuine: menggabungkan dua sub-literatur (strategy–HR fit dan HR–reward fit) menjadi triad terpadu
- Framework yang clear dan applicable — manajer dapat melakukan diagnostic check
- Relevansi praktis: implikasi langsung untuk desain sistem kompensasi yang mendukung strategi
- Bold appreciation: tipologi configurational membuat trade-off eksplisit, bukan pseudo-universal advice

### §6 Keterbatasan dan Kelemahan
Sub-headings: **Sifat Konseptual Tanpa Uji Empiris Sistematis**, **Pengabaian Dinamika Temporal**, **Asumsi Porter's Typology**, **Konteks Taiwan-Spesifik**
- **Limitasi utama:** artikel bersifat konseptual dengan ilustrasi kasus Taiwan — tidak ada uji statistik formal dengan sampel besar dan ukuran validated; thus, prediksi configurational fit tetap proposisi, bukan finding
- Tidak memodelkan dynamic-fit problem: bagaimana triad menyesuaikan ketika strategi berubah dari cost leadership ke differentiation (transition cost dan path dependency tidak dibahas)
- Bergantung penuh pada tipologi Porter — Kotha & Vadlamani (1995) telah menunjukkan keterbatasan measurement Porter's typology; jika tipologi anchor lemah, triad yang dibangun di atasnya juga rentan
- Konteks Taiwan firms (medium-sized, family-business heavy, Confucian culture) — generalisasi ke konteks Indonesia (post-colonial, state-corporatist, mixed-ownership) tidak otomatis

### §7 Evaluasi Kritis
Sub-headings: **Apakah Fit Triad Benar-Benar Configurational atau Hanya Additive?**, **Masalah Endogenitas dalam Strategi-HR-Reward**, **Apa yang Seharusnya Dilakukan**, **Penilaian Kontribusi Orisinal**
- **Critique inti:** Hsieh & Chen mengklaim configurational fit (Miller 1986 sense) tetapi argumentasi mereka kadang slip ke additive fit (Venkatraman 1989) — perbedaannya konsekuensial: configurational mengasumsikan equifinality dan non-linearity, additive tidak. Artikel tidak konsisten menjelaskan mana yang dimaksud.
- Endogenitas: perusahaan yang memilih differentiation cenderung memiliki manajer dengan preferensi HR fleksibel sejak awal — strategi dan sistem HR co-evolve, bukan strategi → HR → reward dalam urutan linear. Artikel tidak mengatasi reverse causality.
- Apa yang seharusnya: configurational empirical test dengan cluster analysis atau set-theoretic methods (Ragin 2008 fsQCA); longitudinal panel untuk memisahkan sebab-akibat
- Penilaian: kontribusi teoretis valid dan berguna untuk pedagogi, tetapi sebagai *predictive theory* artikel ini di tier 2 — useful heuristic, bukan tested causal model

### §8 Implikasi bagi Pemahaman Manajemen Strategik
Sub-headings: **Implikasi Teoretis**, **Implikasi Manajerial**, **Implikasi untuk Konteks Indonesia**
- Theoretical: memperkuat *internal fit* sebagai dimensi yang tidak boleh diabaikan dalam analisis strategi — strategi sukses adalah strategi yang seluruh sistem internal mendukung
- Managerial: HR director dan compensation committee harus diundang ke meja strategi, bukan sekedar implementer downstream
- Indonesian: **Astra International** triad fit antara diversified strategy + HR rotation across business units + KPI-based variable reward; **Bank Mandiri** post-merger triad reconfiguration (cost leadership pada retail + standardized HR + cost-control reward); **Unilever Indonesia** differentiation + talent-development HR + long-term performance reward; **kasus negatif** — BUMN dengan strategy differentiation tetapi HR-reward birokratik (PNS-style) menghasilkan execution gap yang konsisten

### §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut
Sub-headings: **Pertanyaan Terbuka**, **Relevansi untuk Riset Indonesia**
- Apakah triad fit berlaku universal atau berbeda di konteks family-owned vs. publicly-listed firm?
- Bagaimana triad menyesuaikan dalam transisi strategi (transformasi digital, ESG pivot)?
- Indonesia-specific: apakah dual-track HR system di BUMN (PNS-style + market-style) merusak triad fit secara struktural?
- Apakah platform-business model (Gojek, Tokopedia) memerlukan triad keempat: HR-reward-algorithmic-management fit?

---

## 6. Document 3 — Critical Review Artikel 12 (Okebaram & Onuoha 2018)

**Article:** Okebaram, S. M. & Onuoha, C. E. (2018). *Implication of Strategic Fit and Sustainability on Organizational Effectiveness.* International Academic Research Conference in Vienna.

**Format standard:** Same as CR11 and RMK — sub-headings within every section, bold for analytical pivots, italics for foreign terms. Especially dense in §7 and §8.

### §1 Identitas Artikel
Full bibliographic data; venue context (International Academic Research Conference in Vienna — conference paper, peer review tier lower than top journals); authors' Nigerian institutional affiliation (Federal University context — explains Nigerian/African empirical anchoring); article type (conceptual-review dengan integrasi sustainability literature).

### §2 Tujuan Penelitian dan Posisi dalam Literatur
Sub-headings: **Pertanyaan Riset**, **Posisi Relatif terhadap Literatur Strategic Fit dan Sustainability**
- Research question: bagaimana strategic fit dan sustainability secara bersama-sama mempengaruhi *organizational effectiveness*?
- Gap yang diklaim: literatur strategic fit (Venkatraman 1989, Miles & Snow 1978) dan sustainability (Elkington 1997 triple bottom line, Hart 1995 natural-resource-based view) jarang diintegrasikan
- Posisi: extending RBV + contingency theory dengan dimensi sustainability sebagai *external fit* dengan stakeholder environment yang berubah

### §3 Argumen Utama — *Strategic Fit + Sustainability → Effectiveness*
Sub-headings: **Konseptualisasi Strategic Fit**, **Konseptualisasi Sustainability (Triple Bottom Line)**, **Mekanisme Kausal yang Diajukan**, **Proposisi Utama**
- Strategic fit: alignment antara strategi, struktur, lingkungan (mengutip Venkatraman dan Lawrence & Lorsch)
- Sustainability: economic + social + environmental dimensions (Elkington 1997)
- Causal mechanism (diklaim): fit dengan stakeholder expectations → legitimasi → akses sumber daya → effectiveness
- Bold pivot: artikel mengklaim sustainability bukan tradeoff cost tetapi *enabling condition* untuk fit jangka panjang — argumen yang sejalan dengan Porter & Kramer (2006) *shared value*

### §4 Koneksi ke Topik Silabus (Pertemuan 7 — TPGS Ch.8)
Sub-headings: **Sustainability sebagai Dimensi Eksternal Fit**, **Linking ke §9 RMK dan Artikel 11**
- TPGS Ch.8 membahas pencocokan strategi dengan kondisi industri — Okebaram & Onuoha menambah dimensi: strategi juga harus cocok dengan stakeholder sustainability expectations
- Jembatan analitis: Artikel 11 fokus internal fit (strategy-HR-reward), Artikel 12 fokus external fit (strategy-sustainability-stakeholder) — kedua dimensi sama-sama operasionalisasi prinsip fit di §9 RMK

### §5 Kekuatan Artikel
Sub-headings: **Topik yang Relevan dan Aktual**, **Integrasi Dua Aliran Literatur**, **Aksesibilitas untuk Praktisi**
- Topik aktual (ESG era, post-2015 SDG mandate, Paris Agreement implications for corporate strategy)
- Integrasi strategic fit + sustainability cukup berani — banyak penulis memilih satu aliran
- Bahasa accessible dan kerangka yang dapat dipahami praktisi tanpa background teori organisasi

### §6 Keterbatasan dan Kelemahan
Sub-headings: **Sifat Konseptual Tanpa Empiris**, **Definisi Sustainability yang Lentur**, **Pengukuran Effectiveness yang Belum Dispecify**, **Basis Empiris Implisit Afrika**, **Methodological Disclosure yang Minim**
- **Limitasi utama:** conference paper conceptual, tidak ada uji empiris formal — proposisi tetap proposisi
- Definisi sustainability lentur: kadang environmental-focused, kadang economic-focused, kadang social-focused — konflasi konseptual yang merusak kejelasan testable hypothesis
- *Organizational effectiveness* didefinisikan vague — apakah financial performance? stakeholder satisfaction? survival? legitimasi? Tanpa operasionalisasi clear, klaim kausal tidak bisa diverifikasi
- Empirical base (citations) berat ke African context — generalisasi ke konteks Indonesia (institutional voids berbeda, regulator structure berbeda) tidak otomatis
- Metodologi disclosure minim — sebagai conference paper, standar peer review lebih rendah daripada SSCI journal

### §7 Evaluasi Kritis
Sub-headings: **Apakah Sustainability dan Fit Benar-Benar Independent Dimensions?**, **Eclecticism Teoretis sebagai Kelemahan**, **Risiko *Greenwashing* Theoretical**, **Apa yang Seharusnya Dilakukan**, **Penilaian Kontribusi Orisinal**
- **Critique inti:** artikel mengasumsikan sustainability sebagai dimensi terpisah dari strategic fit, padahal sustainability itu sendiri *adalah* contoh fit (dengan stakeholder expectations dan regulasi). Memisahkan keduanya menciptakan double-counting konseptual.
- Eclecticism teoretis: meminjam dari RBV, contingency, stakeholder theory, triple-bottom-line, shared value — tanpa adjudikasi kapan satu teori menggantikan lainnya. Hasilnya: framework yang terdengar komprehensif tetapi tidak menghasilkan testable, falsifiable predictions.
- *Greenwashing* theoretical risk: ketika sustainability dilekatkan ke segalanya sebagai *enabling condition*, klaim menjadi tautologis — sustainability baik untuk perusahaan karena perusahaan yang baik adalah sustainable.
- Apa yang seharusnya: operasionalisasi sustainability ke dalam indikator measurable (carbon intensity, employee turnover, supplier diversity), uji empiris dengan multi-industry sample, dan adjudikasi teoretis eksplisit (kapan sustainability moderates fit, kapan mediates, kapan substitutes)
- Penilaian: artikel useful sebagai *agenda-setting piece* untuk diskusi kelas, lemah sebagai *contribution* di scholarly hierarchy

### §8 Implikasi bagi Pemahaman Manajemen Strategik
Sub-headings: **Implikasi Teoretis**, **Implikasi Manajerial**, **Implikasi untuk Konteks Indonesia**
- Theoretical: memperluas konsep fit ke dimensi stakeholder sustainability — extension yang logis dari Lawrence & Lorsch (1967) ke era post-shareholder-primacy
- Managerial: ESG bukan lagi opsi PR — telah menjadi *fit requirement* dengan modal asing (impact investors), regulator (POJK 51/2017), dan konsumen Gen Z
- Indonesian: **Unilever Indonesia** sustainability-fit (Sustainable Living Plan, supplier inclusion); **Pertamina** geothermal long-horizon fit dengan transisi energi nasional; **kasus tension** — industri batu bara Indonesia (Adaro, Bayan) menghadapi misfit struktural dengan global ESG capital flow; **Sido Muncul** sustainability-fit di herbal medicine + community supplier model; **PLN** menghadapi tension antara mandate kelistrikan universal dan transisi energi — illustrasi konkret bahwa fit dengan satu stakeholder (pemerintah/publik) dapat misfit dengan stakeholder lain (impact investor, climate compliance)

### §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut
Sub-headings: **Pertanyaan Terbuka**, **Relevansi untuk Riset Indonesia**
- Apakah sustainability fit moderates atau mediates strategy → performance relationship? (different empirical implications)
- Bagaimana negara dengan institutional voids (Khanna & Palepu 2000) — Indonesia, Nigeria, India — operationalize sustainability fit ketika regulator dan stakeholder structure berbeda dari OECD?
- Apakah ESG metrics yang diimpor (MSCI, Sustainalytics) menciptakan misfit struktural antara strategi domestik dan global capital expectation?
- Microfoundation: apakah board diversity dan ESG-linked compensation cukup untuk menghasilkan substantive sustainability fit, atau hanya symbolic compliance?

---

## 7. Writing Quality Requirements

- Indonesian akademik; PUEBI/KBBI compliant
- Foreign/English terms italicized on first use per section; Indonesian gloss where useful
- **Rich formatting throughout all three documents:** ### sub-headings within every major section; **bold** for key concept definitions, analytical pivots, critical reasoning conclusions; *italics* for foreign terms
- Each sub-section 150–300 words of substantive analysis — not a label followed by one sentence
- No hyphen ("-") as sentence/clause connector; reduplication `kata - kata` style (with spaces) per user preference
- No Daftar Pustaka; inline citations only: (Penulis tahun) or "menurut Penulis (tahun, p. X)"
- Primary-text engagement: direct paraphrase and short quotations with page references from both PDFs and TPGS Ch.8
- No AI-generic phrases ("delve into", "navigate the landscape", "in conclusion", "it is important to note")
- Scholarly voice: senior-analyst Indonesian academic, direct claims, evidence-grounded critiques
- Indonesian examples from publicly verifiable corporate histories only

---

## 8. Figure Embedding Specification (RMK only)

- **Source:** TPGS Ch.8 PDF pages, extracted via PyMuPDF (fitz)
- **Output format:** PNG, 200 DPI minimum, RGB
- **Storage:** `Dev Assistant/temp/figures_w7/figure_NN.png`
- **Caption format:** *Gambar N. Judul deskriptif (Sumber: TPGS 2021, Ch.8, hlm. X)*
- **Placement:** After the sub-section that introduces the concept; preceded by a transitional sentence ("Konfigurasi tahap industri dapat dilihat pada Gambar N…") and followed by 2–3 sentences interpreting the figure
- **Selection criteria:** Choose figures that add visual value not redundant with prose — life-cycle progression, decision-flow charts, matrices. Avoid pure-text tables that pandoc can render natively.

---

## 9. Out of Scope

- Daftar Pustaka (explicitly excluded, consistent with all prior pertemuan)
- HTML outputs (separate MSK304 spec)
- Articles from other pertemuan
- Henry textbook chapters (user-confirmed: TPGS Ch.8 only for this Pertemuan)
- Visual companion / browser mockups (text-only assignment)
