# Design Spec — RMK + CR Submission, Pertemuan 5

- **Assignment:** RMK + CR ke 3 (Tugas Manajemen Strategik Kontemporer)
- **Student:** Dzaki Muhammad Yusfian | NIM: 1125 01079
- **Course:** MST304 — Manajemen Strategik Kontemporer, STIE YKPN
- **Spec date:** 2026-05-01
- **Status:** Approved
- **Analytical depth standard:** Higher than Pertemuan 4 — paradigmatic positioning of Porter's generic strategies, engagement with hybrid/dynamic/coopetition critiques, integration with cognitive-strategy literature on competitor blindspots; primary-text engagement required; still digestible for S2 Indonesia.

---

## 1. Assignment

Buat RMK dan Critical Review untuk materi dan artikel Pertemuan 5 sesuai silabus.

**Pertemuan 5 topic:** *The Five Generic Competitive Strategies* (TPGS Ch.5 + Henry Ch.5)

**References:**
- TPGS Ch.5 (Gamble, Peteraf & Thompson 2021)
- Henry Ch.5 (Understanding Strategic Management 2021)
- Article 7: Helen Salavou (2015), *Competitive Strategies and Their Shift to the Future*, European Business Review, 27(1): 80–99
- Article 8: Adom, Nyarko & Som (2016), *Competitor Analysis in Strategic Management: Is It a Worthwhile Managerial Practice in Contemporary Times?*, Journal of Resources Development and Management, 24: 116

---

## 2. Output Files

| # | Filename | Output Path |
|---|----------|-------------|
| 1 | `01079_Dzaki Muhammad Yusfian_RMK Pert. 5.docx` | `RMK/` |
| 2 | `01079_Dzaki Muhammad Yusfian_Artikel 7.docx` | `Critical Thinking of the Article/` |
| 3 | `01079_Dzaki Muhammad Yusfian_Artikel 8.docx` | `Critical Thinking of the Article/` |

Output directories are root-level (canonical, per commit `afc8451`).

---

## 3. Generation Pipeline

**Tool:** Pandoc + Python 3.12 orchestrator (reusing `reference.docx` from Pertemuan 2)

**Script:** `Dev Assistant/scripts/generate_submission_w5.py`

Same flow as `generate_submission_w4.py`: writes Markdown to `Dev Assistant/temp/`, calls pandoc with `reference.docx`, outputs DOCX to the paths in §2.

**Formatting:** Times New Roman 12pt body; 14pt centered bold Heading 1; 12pt bold Heading 2; 12pt bold italic Heading 3; margins 3cm / 2.5cm; line spacing 1.5; first-line indent 1.25cm.

---

## 4. Document 1 — RMK Pertemuan 5

**Header:** RINGKASAN MATERI KULIAH — PERTEMUAN 5 / MST304 / Dzaki Muhammad Yusfian / NIM: 1125 01079

**Sections:**
1. Pendahuluan — dari analisis internal (Pert. 4 / RBV) ke pilihan posisi kompetitif (Pert. 5); pertanyaan inti *bagaimana* perusahaan bersaing dalam industri tertentu
2. Akar Konseptual — Porter (1980, 1985) sebagai reaksi terhadap *Structure–Conduct–Performance* paradigm; dua dimensi fundamental (cakupan pasar × sumber keunggulan)
3. Lima Strategi Generik — *low-cost provider*, *broad differentiation*, *focused low-cost*, *focused differentiation*, *best-cost provider* — beserta logika ekonomis dan kondisi keberhasilan masing-masing
4. *Stuck in the Middle* — argumen Porter tentang ketidakcocokan struktural antara cost dan differentiation, dan tantangan empiris (Hill 1988; Miller 1992; Campbell-Hunt 2000 meta-analysis)
5. Strategi Hybrid dan Dinamis — respons terhadap Porter; *value disciplines* (Treacy & Wiersema 1995); *temporary advantage* (D'Aveni 1994; McGrath 2013); jembatan ke Salavou (2015)
6. Pilihan Strategi dan Lima Kekuatan Industri — kapan tiap strategi bekerja, kapan gagal; integrasi dengan analisis Pertemuan 3
7. Analisis Pesaing sebagai Prasyarat Pilihan — kerangka Porter Ch.3 (future goals, current strategy, assumptions, capabilities); *strategic groups* (Porac & Thomas 1990); *competitor blindspots* (Zajac & Bazerman 1991; Reger & Huff 1993); jembatan ke Adom et al. (2016)
8. Risiko dan Jebakan Pelaksanaan — *strategy decay*, imitasi cepat, *strategic drift* (Johnson 1988); sinyal kapan strategi perlu di-*shift*
9. Kesimpulan — pilihan generik tetap menjadi titik referensi yang kuat, tetapi harus dipahami sebagai *moving baseline*, bukan posisi statis; integrasi dengan Pert. 4 (RBV) dan antisipasi Pert. 6 (strategi tingkat korporat)

**Content sources:** TPGS Ch.5 + Henry Ch.5 + `Dev Assistant/content/week-05/summary/*.md` (reframed as formal akademik prose) + Artikel 7 dan 8 PDF.

**Depth standard:** Graduate-level synthesis — paradigmatic positioning (Porter sebagai reaksi terhadap SCP industrial economics; hybrid sebagai reaksi terhadap Porter), bukan ringkasan textbook; setiap framework dijelaskan *kapan* berlaku, *kapan* gagal, dan *bagaimana* berinteraksi dengan topik sebelum/sesudah.

---

## 5. Document 2 — Critical Review Artikel 7 (Salavou 2015)

**Article:** Helen Salavou (2015). *Competitive Strategies and Their Shift to the Future.* European Business Review, 27(1): 80–99.

**Sections:**
1. Identitas Artikel
2. Tujuan Penelitian dan Posisi dalam Literatur
3. Argumen Utama — Tiga Pergeseran (mutually exclusive → hybrid; static → dynamic; competitive → cooperative)
4. Koneksi ke Topik Silabus (Pertemuan 5 — TPGS Ch.5)
5. Kekuatan Artikel
6. Keterbatasan dan Kelemahan
7. Evaluasi Kritis
8. Implikasi bagi Pemahaman Manajemen Strategik
9. Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut

**Depth angles to hit in the CR:**
- **Paradigm-shift framing:** Porter's *mutually exclusive* logic — cost dan differentiation menuntut konfigurasi organisasi dan rantai nilai yang bertentangan — versus bukti empiris hybrid sejak akhir 1980-an. Hill (1988) sebagai kritik teoretis pertama; Miller (1992) tentang *strategic specialization vs combination*; Campbell-Hunt (2000) meta-analysis 17 studi yang menunjukkan kombinasi sering lebih baik daripada murni.
- **Static-to-dynamic:** Salavou's argument bahwa di lingkungan turbulen perusahaan harus *shift* lebih sering. Hubungkan dengan *dynamic capabilities* (Teece, Pisano, Shuen 1997), *hypercompetition* (D'Aveni 1994), dan *transient advantage* (McGrath 2013). Salavou tidak menyebut McGrath — sebuah keterbatasan bibliografis yang bermakna.
- **Competitive-to-cooperative:** *coopetition* (Brandenburger & Nalebuff 1996), platform economics, ecosystem boundaries. Diskusikan apakah coopetition sebenarnya konsisten dengan kerangka Porter (sebagai bentuk *complementor* yang kelima dalam Five Forces) atau benar-benar menggantikannya.
- **Treacy & Wiersema (1995) sebagai typologi paralel:** *operational excellence*, *product leadership*, *customer intimacy*. Apakah Salavou sebenarnya hanya re-labeling atau menambahkan dimensi baru?
- **Critique central:** Apakah "shift" yang didokumentasikan Salavou adalah kemajuan teoretis, atau label akademis untuk apa yang sudah praktisi lakukan selama dua dekade? Banyak observasi Salavou terdokumentasi lebih awal di literatur lain — kontribusi orisinalitasnya terbatas.
- **Methodological limit:** literature review tanpa data empiris baru; tidak ada uji proposisi; sintesis bersifat narratif. Untuk jurnal kelas European Business Review ini lazim, tetapi membatasi klaim kausal.
- **Indonesian applications:**
  - Indomaret–Alfamart sebagai *best-cost hybrid* (skala efisiensi + lokasi-konvenien sebagai diferensiator) — konsisten dengan Salavou's hybrid argument.
  - Gojek–Tokopedia merger (2021) sebagai contoh ekstrem coopetition yang kemudian terintegrasi (GoTo) — pertanyaan apakah ini coopetition atau eliminasi pesaing.
  - AirAsia transisi dari *focused low-cost* ke *broad low-cost* di pasar Asia — contoh dynamic shift Salavou.
  - Tokopedia–Shopee dynamic adjustment (subsidi, fitur, model fulfillment) di bawah tekanan platform — contoh *transient advantage* McGrath, bukan posisi statis.

---

## 6. Document 3 — Critical Review Artikel 8 (Adom, Nyarko & Som 2016)

**Article:** Alex Yaw Adom, Israel Kofi Nyarko, Gladys Narki Kumi Som (2016). *Competitor Analysis in Strategic Management: Is It a Worthwhile Managerial Practice in Contemporary Times?* Journal of Resources Development and Management, 24: 116.

**Sections:** Same 9 sections as Document 2.

**Depth angles to hit in the CR:**
- **Epistemic-utility critique:** pertanyaan inti artikel — di era big data, apakah competitor analysis formal masih bernilai? Adom et al. menjawab "ya, tapi peran berubah". Bottleneck telah bergeser dari *information acquisition* ke *sense-making* dan *prediction*. Kerangka Porter (1980 Ch.3) tetap relevan tetapi sel "asumsi pesaing" justru menjadi paling under-utilized — manajer mudah mengumpulkan fakta, sulit memetakan keyakinan pesaing.
- **Cognitive-strategy literature sebagai kritik terdalam:** ini sudut yang Adom et al. tidak masuki secara serius dan menjadi keterbatasan utama. *Competitor blindspots* (Zajac & Bazerman 1991) — manajer secara sistematis salah membaca pesaing karena bias overconfidence, illusion of control, dan gagal mempertimbangkan reasoning pesaing. *Managerial cognition and competitive groups* (Porac & Thomas 1990; Reger & Huff 1993) — manajer membentuk *cognitive maps* tentang siapa pesaingnya, dan peta itu sering sempit dan keliru. Implikasi: masalah bukan *kekurangan data* (yang Adom et al. fokuskan) melainkan *interpretasi yang bias* (yang luput dari pembahasan).
- **Porter (1980 Ch.3) framework empat sel:** future goals, current strategy, assumptions, capabilities. Diskusikan mengapa sel "assumptions" paling sulit dan paling bernilai — karena merupakan satu-satunya sel yang membuka *response prediction*.
- **Fleisher & Bensoussan (2007) toolkit:** 24 teknik competitor intelligence; ethics (SCIP code); profesionalisasi praktik. Adom et al. tidak melibatkan literatur ini secara mendalam — kelemahan yang signifikan untuk paper bertema *contemporary practice*.
- **Bukti lapangan Afrika:** apa yang generalisable, apa yang context-bound. Konteks pasar Ghana (akses informasi terbatas, ukuran pasar relatif kecil, governance challenges) tidak otomatis berlaku untuk pasar dengan informasi tebal seperti Indonesia atau pasar dengan disclosure ketat seperti Singapura.
- **Critique central:** apakah paper ini kontribusi teoretis genuine atau literature review dengan light empirical garnish? Argumennya benar tetapi tidak orisinal; framing "is it worthwhile" agak straw-man — tidak ada literatur serius yang berargumen competitor analysis tidak worthwhile, sehingga "ya tetap worthwhile" bukanlah finding yang signifikan. Yang akan lebih bernilai: *bagaimana* praktiknya harus berubah, dan paper ini hanya menyentuh permukaan tersebut.
- **Indonesian applications:**
  - BCA vs Bank Mandiri competitor monitoring — keduanya memiliki *strategic intelligence* function; perbedaan tampak di kecepatan respons produk (BCA cenderung lebih agile di digital banking).
  - Indofood membaca pergerakan Wings Group pada kategori kopi instan dan mie — contoh competitor analysis yang melibatkan distribusi (bukan sekadar produk).
  - E-commerce price-tracking otomatis (Tokopedia, Shopee, Lazada) — competitor analysis terotomasi pada level data, tetapi keputusan strategi tetap human-mediated.
  - Garuda Indonesia's failure to track LCC entrants pre-AirAsia (1999–2003) — contoh klasik *competitor blindspot* (Garuda mengasumsikan segmen full-service tidak akan terdisrupsi); konsisten dengan Zajac & Bazerman.

---

## 7. Writing Quality Requirements

- Indonesian akademik; PUEBI/KBBI compliant
- Foreign/English terms italicized on first use per section; Indonesian gloss provided where useful
- No hyphen ("-") as sentence connector; reduplication forms (`kupu - kupu`) use spaced hyphen style per user preference
- No generic AI-sounding phrasing; scholarly voice that reads naturally
- Engagement with primary text (both articles read in full) — direct paraphrase and occasional short quotations with page references where the original phrasing carries force
- Conceptual synthesis over narrative summary; every critique grounded in either textual evidence or cited secondary critic (Hill, Miller, Campbell-Hunt, Treacy & Wiersema, Brandenburger & Nalebuff, McGrath, D'Aveni, Zajac & Bazerman, Porac & Thomas, Reger & Huff, Fleisher & Bensoussan, Porter)
- Indonesian examples drawn from publicly verifiable corporate histories, not fabricated figures

---

## 8. Out of Scope

- Daftar Pustaka (explicitly excluded by user preference, consistent with Pertemuan 2 and 4 submissions)
- HTML outputs (covered by separate MSK304 spec)
- Articles from other pertemuan
