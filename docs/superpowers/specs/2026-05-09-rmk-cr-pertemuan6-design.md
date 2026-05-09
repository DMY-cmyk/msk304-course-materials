# Design Spec — RMK + CR Submission, Pertemuan 6

- **Assignment:** RMK + CR ke 4 (Tugas Manajemen Strategik Kontemporer)
- **Student:** Dzaki Muhammad Yusfian | NIM: 1125 01079
- **Course:** MST304 — Manajemen Strategik Kontemporer, STIE YKPN
- **Spec date:** 2026-05-09
- **Status:** Approved
- **Analytical depth standard:** Higher than Pertemuan 5 — full primary-text engagement with both PDFs; mediation-mechanism critique for Artikel 9; cumulative-knowledge critique + gap analysis for Artikel 10; paradigmatic framing for RMK; rich sub-heading + bold/italic formatting throughout all three documents so they function as dense graduate reference materials, not thin summaries.

---

## 1. Assignment

Buat RMK dan Critical Review untuk materi dan artikel Pertemuan 6 sesuai silabus.

**Pertemuan 6 topic:** *Strengthening a Company's Competitive Position: Strategic Moves, Timing, and Scope of Operations* (TPGS Ch.6 + Henry Ch.5–6)

**References:**
- TPGS Ch.6 (Gamble, Peteraf & Thompson 2021)
- Henry Ch.5–6 (Understanding Strategic Management 2021)
- Article 9: Teeratansirikool, Siengthai, Badir & Charoenngam (2013/2014), *Competitive Strategies and Firm Performance: The Mediating Role of Performance Measurement*, International Journal of Productivity and Performance Management, 63(1/2): 168–184
- Article 10: Onditi, E.O. (2018), *Competitive Strategies and Firm Performance: A Review of Literature*, Strategic Journals, 5(4): 1869–1879

---

## 2. Output Files

| # | Filename | Output Path |
|---|----------|-------------|
| 1 | `01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx` | `RMK/` |
| 2 | `01079_Dzaki Muhammad Yusfian_Artikel 9.docx` | `Critical Thinking of the Article/` |
| 3 | `01079_Dzaki Muhammad Yusfian_Artikel 10.docx` | `Critical Thinking of the Article/` |

Output directories are root-level (canonical, per commit `afc8451`).

---

## 3. Generation Pipeline

**Tool:** Pandoc + Python 3.12 orchestrator (reusing `reference.docx` from Pertemuan 2)

**Script:** `Dev Assistant/scripts/generate_submission_w6.py`

Same flow as `generate_submission_w5.py`: writes Markdown to `Dev Assistant/temp/`, calls pandoc with `reference.docx`, outputs DOCX to the paths in §2.

**Formatting:** Times New Roman 12pt body; 14pt centered bold Heading 1; 12pt bold Heading 2; 12pt bold italic Heading 3; margins 3cm / 2.5cm; line spacing 1.5; first-line indent 1.25cm.

---

## 4. Document 1 — RMK Pertemuan 6

**Header:**
```
RINGKASAN MATERI KULIAH — PERTEMUAN 6
Mata Kuliah: MST304 — Manajemen Strategik Kontemporer
Mahasiswa: Dzaki Muhammad Yusfian | NIM: 1125 01079
```

**Format standard (critical):** Every section uses sub-headings (###) to break content into 2–5 analytical sub-angles. Bold for key concept definitions, critical reasoning pivots, and "why this matters" moments. Italics for all foreign terms first use per section. Each sub-section is 150–300 words of substantive analysis — the document functions as a compact graduate-level analytical handbook, not a bullet-point summary.

**Sections:**

### §1 Pendahuluan
- Transisi dari Pert. 5 (pilihan strategi generik) ke Pert. 6 (penguatan posisi kompetitif)
- Pertanyaan inti: *bagaimana* mempertahankan dan memperdalam keunggulan setelah posisi dipilih
- Sub-heading: mengapa pilihan strategi saja tidak cukup — the execution gap

### §2 *Offensive Strategies*
Sub-headings: *Frontal Attack*, *Flanking Attack*, *Guerrilla Warfare*, *Preemptive Strike*, **Kapan Menyerang vs. Mengisi Celah**
- Logika ekonomis di balik setiap tipe serangan
- Bold reasoning: kapan menyerang pemimpin pasar menguntungkan vs. kapan itu bunuh diri
- Kondisi yang memungkinkan serangan frontal berhasil (resource superiority ≥ 3:1 — Sun Tzu derivation)
- Indonesian examples: Tokopedia menyerang Shopee dengan program seller education; Gojek flanking Grab di segmen merchant

### §3 *Defensive Strategies*
Sub-headings: *Fortify-and-Defend*, *Signaling*, *Mobile Defense*, *Counteroffensive*, **Hubungan dengan Barriers to Entry**
- Credibility theory of signaling — mengapa ancaman yang tidak kredibel gagal (Schelling 1960)
- Bold reasoning: kapan bertahan aktif lebih baik daripada passive defense
- Switching costs dan customer lock-in sebagai defensive moat
- Indonesian examples: Sampoerna mempertahankan posisi premium dengan brand architecture; BCA defensive di CASA via switching-cost moat

### §4 *Timing Strategies*
Sub-headings: **Lima Mekanisme First-Mover Advantage**, **Tiga Beban First-Mover**, *Fast-Follower Logic*, *Late-Mover Rationality*, **Aturan Emas Timing**
- Five FMA mechanisms: learning curve, resource pre-emption, network effects, brand loyalty, switching-cost lock-in — masing-masing dianalisis kondisi necessary
- Three FMD: pioneer costs, technological uncertainty (backing wrong standard), market education burden
- Bold: kondisi kapan fast-follower mengalahkan pioneer (Samsung vs. Apple; Microsoft vs. Netscape)
- Late-mover rationality: Google+ (late mover yang gagal) vs. Google entering search (fast second)
- Indonesian examples: Gojek sebagai first-mover ride-hailing Indonesia; Grab sebagai fast-follower; OVO sebagai fast-follower di e-wallet

### §5 *Scope of Operations*
Sub-headings: *Vertical Integration* (Backward/Forward), *Strategic Outsourcing*, *Strategic Alliances & Joint Ventures*, *Mergers & Acquisitions*, **Transaction Cost Economics sebagai Kerangka Make-or-Buy**
- Williamson (1975) TCE: asset specificity, uncertainty, frequency — kapan internalisasi efisien
- Bold: the "hollowing out" risk of over-outsourcing (strategic capabilities cannot be rebuilt once lost)
- Alliance vs. acquisition trade-off: speed vs. control vs. learning
- Indonesian examples: Pertamina backward integration hulu; Astra International alliance network (Honda, Toyota JV); GoTo merger sebagai scope expansion; Telkom Group vertical integration di broadband

### §6 *Blue Ocean Strategy*
Sub-headings: **Value Innovation vs. Competitive Advantage**, *Eliminate-Reduce-Raise-Create Grid*, **Kritik: Apakah Blue Ocean Berkelanjutan?**, **Counter-Counter-Argument**
- Kim & Mauborgne (2005) sebagai counter-paradigm terhadap Porter: *value innovation* memecah trade-off cost vs. differentiation
- ERRC grid analysis dengan contoh konkret
- Bold critique: blue ocean sering first-mover red ocean dengan label baru — setelah imitasi masuk, apa yang tersisa?
- Counter-counter: blue ocean value is in the *process* of innovation, not permanent position — sesuai dengan McGrath's transient advantage logic
- Indonesian examples: Kopi Kenangan sebagai quasi-blue-ocean (affordable specialty coffee); Ruangguru menciptakan ruang baru di edu-tech

### §7 *Performance Measurement* sebagai Eksekusi
Sub-headings: *Balanced Scorecard* (Kaplan & Norton 1992, 1996), *Strategy Maps*, **Mengapa Strategic Moves Gagal Tanpa PMS**, **Jembatan ke Teeratansirikool et al. (2013)**
- BSC empat perspektif: financial, customer, internal process, learning & growth
- Strategy maps: linking cause-effect chain dari learning → process → customer → financial
- Bold: the execution gap — firms with correct strategy and poor measurement consistently underperform firms with average strategy and excellent measurement (Kaplan & Norton empirical evidence)
- Indonesian examples: Bank Mandiri BSC transformation 2005–2010; Pertamina KPI cascade

### §8 Strategi Kompetitif dan Kinerja: Apa yang Kita Ketahui?
Sub-headings: **Konsensus yang Kokoh**, **Debat yang Belum Selesai**, **Peran Moderating Variables**, **Jembatan ke Onditi (2018)**
- What is settled: strategy clarity → better performance than ambiguity (Campbell-Hunt 2000)
- What is contested: which generic strategy type performs best (industry-contingent)
- Moderators: industry structure, firm size, institutional environment
- Indonesian empirical record: BCA differentiation outperforming; Indomaret cost leadership winning

### §9 Kesimpulan
Sub-headings: **Strategi sebagai Proses Kalibrasi Berkelanjutan**, **Integrasi Alur Pert. 4–6**, **Antisipasi Pert. 7**
- Synthesis: offensive/defensive/timing/scope tidak dipilih sekali — harus dikalibrasi ulang seiring perubahan lingkungan
- Integration chain: RBV (Pert. 4) → pilihan generik (Pert. 5) → penguatan posisi + eksekusi + pengukuran (Pert. 6)
- Forward link: corporate-level strategy (Pert. 7) adds another layer — *where* to compete, not just *how*

---

## 5. Document 2 — Critical Review Artikel 9 (Teeratansirikool et al. 2013)

**Article:** Teeratansirikool, Siengthai, Badir & Charoenngam (2013/2014). *Competitive Strategies and Firm Performance: The Mediating Role of Performance Measurement.* International Journal of Productivity and Performance Management, 63(1/2): 168–184.

**Format standard:** Same as RMK — sub-headings (###) within every section, bold for analytical pivots and critique conclusions, italics for foreign terms. §7 Evaluasi Kritis and §8 Implikasi especially dense (200–350 words each). Every section functions as a mini-analysis, not a label + one sentence.

**Sections and depth angles:**

### §1 Identitas Artikel
Full bibliographic data, context of publication (IJPPM focus: productivity and performance management — explains why PMS angle dominates), authors' institutional affiliation (AIT Thailand — explains empirical context).

### §2 Tujuan Penelitian dan Posisi dalam Literatur
Sub-headings: **Pertanyaan Riset Utama**, **Posisi dalam Rantai Literatur**
- Research question: does PMS mediate the strategy→performance link?
- Gap being filled: prior literature treated strategy→performance as direct; Teeratansirikool argues the link is *indirect* via PMS implementation quality
- Position relative to Kaplan & Norton (1992, 1996), Neely et al. (1995), Bourne et al. (2000)

### §3 Argumen Utama — Tiga Hipotesis
Sub-headings: **H1: Strategi Kompetitif → PMS**, **H2: PMS → Kinerja Perusahaan**, **H3: PMS sebagai Mediator**, **Kerangka SEM-PLS**
- H1: firms with clearer strategy invest more in comprehensive PMS — theoretically grounded in *information processing theory* (Galbraith 1974)
- H2: comprehensive PMS → superior performance — grounded in Kaplan & Norton BSC lineage
- H3: mediation claim — the most ambitious and most vulnerable hypothesis
- SEM-PLS methodology rationale and its key assumptions

### §4 Koneksi ke Topik Silabus (Pertemuan 6 — TPGS Ch.6)
Sub-headings: **PMS sebagai Infrastruktur Eksekusi Strategic Moves**, **Linking §7 RMK ke Artikel Ini**
- How PMS enables (or constrains) the offensive/defensive/timing moves discussed in TPGS Ch.6
- Without PMS alignment, even the best strategic move loses its feedback loop

### §5 Kekuatan Artikel
Sub-headings: **Kontribusi Teoretis**, **Kekuatan Empiris**, **Relevansi Praktis**
- Genuine theoretical contribution: bringing PMS into the strategy→performance causal chain as mediator (not just correlate)
- Empirical: SEM-PLS on 117 Thai listed companies — adequate for mediation testing
- Practical: direct implications for how managers should design PMS to reinforce strategy

### §6 Keterbatasan dan Kelemahan
Sub-headings: **Masalah Endogeneitas**, **Keterbatasan Sampel**, **Validitas Konstruk**, **Common Method Variance**
- **Endogeneity problem (most important):** firms that execute strategy well *both* build better PMS *and* perform better — is PMS the cause of performance or a co-effect of general organizational capability? The paper does not rule this out with instrumental variables or longitudinal design
- Thailand-only sample: SET-listed firms, relatively large, formal governance — not representative of SMEs or non-publicly-listed firms
- Construct validity: "competitive strategy" operationalized with Porter's three types via self-report — known measurement problems (Kotha & Vadlamani 1995)
- Cross-sectional design: cannot establish causal direction

### §7 Evaluasi Kritis
Sub-headings: **Apakah Mediasi Terbukti atau Sekadar Diklaim?**, **Masalah Mediation Theory**, **Apa yang Seharusnya Dilakukan**, **Penilaian Kontribusi Orisinal**
- Baron & Kenny (1986) mediation criteria vs. modern bootstrapping (Preacher & Hayes) — which did the paper use and does it matter?
- **Core critique:** partial mediation (which the paper likely found) is consistent with *both* "PMS is a genuine mediator" AND "there's a common cause (organizational capability) driving both PMS adoption and performance." The paper cannot distinguish between these two interpretations without a longitudinal or experimental design.
- What should have been done: longitudinal panel (T1 strategy → T2 PMS → T3 performance); or use of instrumental variables; or qualitative case comparison
- Net assessment: the mechanism argument is theoretically valuable and practically important; the empirical proof is suggestive but not conclusive

### §8 Implikasi bagi Pemahaman Manajemen Strategik
Sub-headings: **Implikasi Teoretis**, **Implikasi Manajerial**, **Implikasi untuk Konteks Indonesia**
- Theoretical: adds PMS to the causal chain between strategy and performance — expands the "black box" of strategy execution
- Managerial: choosing the right strategy is necessary but not sufficient; measurement architecture must be co-designed with strategy
- Indonesian: Bank Mandiri's BSC-based transformation (post-recapitalization 2005–2010 — documented public case); Pertamina KPI cascade under energy sector reform; Telkom Indonesia performance management maturity — do these Indonesian cases support or complicate the Thai findings? State-ownership introduces political KPI distortion that the Thai model does not account for.

### §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut
Sub-headings: **Pertanyaan Terbuka**, **Relevansi untuk Riset Masa Depan**
- Is PMS a mediator or a moderator? (different theoretical implications)
- Does the mediation hold for SMEs without formal PMS infrastructure?
- How does digital performance dashboarding (real-time OKR systems) change the PMS→performance link?
- Indonesia-specific: do state-owned enterprises' politically-influenced KPIs break the mediation?

---

## 6. Document 3 — Critical Review Artikel 10 (Onditi 2018)

**Article:** Onditi, E.O. (2018). *Competitive Strategies and Firm Performance: A Review of Literature.* Strategic Journals, 5(4): 1869–1879. Literature review.

**Format standard:** Same as CR9 and RMK — sub-headings within every section, bold for analytical pivots, italics for foreign terms. Especially dense in §7 and §8–9.

**Sections and depth angles:**

### §1 Identitas Artikel
Full bibliographic data; Strategic Journals context (relatively newer African-based management journal); Onditi's institutional affiliation.

### §2 Tujuan Penelitian dan Posisi dalam Literatur
Sub-headings: **Pertanyaan Riset**, **Posisi Relatif terhadap Review Sebelumnya**
- What cumulative knowledge exists on competitive strategy → firm performance?
- Position relative to Campbell-Hunt (2000) meta-analysis (most rigorous prior synthesis); Dess & Davis (1984); Hambrick (1983)
- Why another review in 2018: covers post-2000 empirical studies that Campbell-Hunt (2000) couldn't include

### §3 Argumen Utama — Tiga Tema Sintesis
Sub-headings: **Tema 1: Strategi Generik vs. Kinerja**, **Tema 2: Konteks Industri sebagai Moderator**, **Tema 3: Implementasi dan Eksekusi**
- What the literature has settled: strategy clarity beats ambiguity; Porter's typology remains the dominant organizing framework
- Industry as moderator: differentiation performs better in high-clock-speed industries; cost leadership performs better in commodity markets
- Execution quality as underappreciated variable: strategy type alone explains limited variance in performance

### §4 Koneksi ke Topik Silabus (Pertemuan 6 — TPGS Ch.6)
- How Onditi's synthesis validates TPGS Ch.6's argument: choosing strategy moves without measuring execution leads to performance gaps
- Link to Teeratansirikool (Artikel 9): Onditi's "execution quality" theme provides theoretical context for why PMS mediates

### §5 Kekuatan Artikel
Sub-headings: **Cakupan Literatur Post-2000**, **Aksesibilitas untuk Praktisi**, **Identifikasi Gap**
- Covers empirical studies from 2000–2017 not in Campbell-Hunt
- Written accessibly — useful for practitioners and students
- Clearly identifies gaps: non-Western contexts, digital disruption, micro-level mechanisms

### §6 Keterbatasan dan Kelemahan
Sub-headings: **Kualitas Sintesis: Deskriptif vs. Analitis**, **Masalah Straw-Man yang Berulang**, **Basis Empiris Afrika-Berat**, **Moderating Variables yang Tertinggal**
- **Core weakness:** organizing framework is descriptive — three themes are categories, not an analytical structure. Onditi reports what studies found without adjudicating why they conflict. Campbell-Hunt (2000) is more methodologically rigorous at 40% of Onditi's length.
- Africa-heavy empirical base: Kenyan, Ghanaian, Nigerian context studies dominate → limits generalizability to East Asia, ASEAN, institutional void contexts (Khanna & Palepu 2000)
- Missing moderators: industry clock-speed (Fine 1998); firm age; institutional voids; ownership structure (state vs. private)
- No meta-analytic technique: narrative review without effect-size synthesis

### §7 Evaluasi Kritis
Sub-headings: **Apakah Onditi Menyelesaikan Kontestasi atau Melaporkannya?**, **Perbandingan dengan Campbell-Hunt (2000)**, **Masalah "Measurement Artifact"**, **Penilaian Kontribusi Orisinal**
- **Central critique:** Onditi's synthesis quality is limited — he accurately reports that studies conflict but does not offer a theoretical framework to explain *why*. A review that says "results are mixed depending on context" without specifying which contexts and why is incomplete.
- Campbell-Hunt (2000) comparison: 17 studies, quantitative meta-analysis, effect-size weighting — more rigorous despite smaller corpus. Onditi's value is breadth (post-2000 coverage), not analytical depth.
- Measurement artifact problem: Kotha & Vadlamani (1995) showed that "strategy type" as measured by survey instruments may not capture real strategic positioning — this undermines studies that find clear strategy→performance links *and* studies that don't
- Net assessment: useful literature map, weak theoretical synthesis; should be read alongside Campbell-Hunt, not instead of it

### §8 Implikasi bagi Pemahaman Manajemen Strategik
Sub-headings: **Implikasi Teoretis**, **Implikasi untuk Riset Indonesia**, **Komparasi Rekam Jejak Empiris Indonesia dengan Prediksi Literatur**
- Theoretical: the strategy→performance literature has accumulated much data but limited cumulative insight — because moderating variables are underspecified
- Indonesian research gap: almost no rigorous empirical studies on competitive strategy → performance for Indonesian firms using validated constructs and longitudinal design
- Indonesian corporate cases: Astra International (diversified conglomerate — what strategy "type" is this and does it fit Porter's typology?); BCA (differentiation outperforming in retail banking — consistent with Onditi's theme 1); Indofood cost leadership in consumer staples (consistent); Telkom Indonesia under state-ownership political objectives (complicates the strategy→performance link)

### §9 Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut
Sub-headings: **Gap yang Paling Penting**, **Pertanyaan untuk Riset Mendatang**
- How does digital disruption change the strategy–performance link? (Onditi's 2018 review barely touches this)
- Do Indonesian institutional voids create a different strategy–performance relationship than developed markets?
- Is the Porter typology still the right measurement framework, or do newer typologies (Miles & Snow, Treacy & Wiersema) produce more valid measurements?
- Microfoundations: what organizational routines and individual decisions actually translate strategy type into performance?

---

## 7. Writing Quality Requirements

- Indonesian akademik; PUEBI/KBBI compliant
- Foreign/English terms italicized on first use per section; Indonesian gloss where useful
- **Rich formatting throughout all three documents:** ### sub-headings within every major section; **bold** for key concept definitions, analytical pivots, critical reasoning conclusions; *italics* for foreign terms
- Each sub-section 150–300 words of substantive analysis — not a label followed by one sentence
- No hyphen ("-") as sentence/clause connector; reduplication `kata - kata` style (with spaces) per user preference
- No Daftar Pustaka; inline citations only: (Penulis tahun) or "menurut Penulis (tahun, p. X)"
- Primary-text engagement: direct paraphrase and short quotations with page references from both PDFs
- No AI-generic phrases ("delve into", "navigate the landscape", "in conclusion", "it is important to note")
- Scholarly voice: senior-analyst Indonesian academic, direct claims, evidence-grounded critiques
- Indonesian examples from publicly verifiable corporate histories only

---

## 8. Out of Scope

- Daftar Pustaka (explicitly excluded, consistent with all prior pertemuan)
- HTML outputs (separate MSK304 spec)
- Articles from other pertemuan
