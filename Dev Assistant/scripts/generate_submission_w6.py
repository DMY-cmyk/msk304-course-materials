#!/usr/bin/env python3
"""
generate_submission_w6.py
Generates three Word documents for MST304 Pertemuan 6 submission.
Reuses reference.docx created by generate_submission.py.
"""

import subprocess
import sys
from pathlib import Path

SCRIPT_DIR   = Path(__file__).resolve().parent
DEV_DIR      = SCRIPT_DIR.parent
PROJECT_ROOT = DEV_DIR.parent
TEMP_DIR     = DEV_DIR / "temp"
REFERENCE    = SCRIPT_DIR / "reference.docx"
OUT_RMK      = PROJECT_ROOT / "RMK"
OUT_CR       = PROJECT_ROOT / "Critical Thinking of the Article"
PANDOC       = r"C:\Program Files\Pandoc\pandoc.exe"


def pandoc(md: Path, out: Path):
    result = subprocess.run(
        [PANDOC, str(md), f"--reference-doc={REFERENCE}", "-o", str(out)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Pandoc error: {result.stderr}")
        sys.exit(1)
    print(f"Generated: {out.name}")


def write_md(content: str, name: str) -> Path:
    p = TEMP_DIR / name
    p.write_text(content, encoding="utf-8")
    return p


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT 1 — RMK PERTEMUAN 6
# ══════════════════════════════════════════════════════════════════════════════
RMK = r"""# RINGKASAN MATERI KULIAH — PERTEMUAN 6

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Topik:** *Strengthening a Company's Competitive Position: Strategic Moves, Timing, and Scope of Operations* (TPGS Ch.6 + Henry Ch.5–6)

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Pendahuluan

### Transisi dari Pilihan Generik ke Penguatan Posisi

Pertemuan 5 menutup pembahasan dengan pertanyaan klasifikasi: posisi generik mana yang harus diambil perusahaan agar sumber daya internalnya menghasilkan keunggulan yang tahan lama. Jawaban Porter (1985) — *low-cost provider*, *broad differentiation*, *focused low-cost*, *focused differentiation*, dan *best-cost provider* — menyediakan peta yang jelas tetapi tidak lengkap. Memilih posisi adalah keputusan awal; mempertahankan dan memperdalam posisi tersebut di tengah dinamika pesaing, perubahan teknologi, dan pergeseran preferensi konsumen adalah pekerjaan yang jauh lebih panjang dan kompleks. Pertemuan 6 mengisi celah ini dengan tiga keluarga keputusan strategik: gerakan ofensif dan defensif (*strategic moves*), strategi waktu (*timing*), serta keputusan tentang lingkup operasi (*scope of operations*).

Di sinilah perbedaan epistemologis penting muncul. Pertemuan 5 berfokus pada *content* strategi — apa yang dipilih. Pertemuan 6 bergeser ke *process* strategi — bagaimana pilihan itu dijaga, diperdalam, dan dikalibrasi. Henry (2021) menjembatani kedua orientasi ini dengan menempatkan diskusi *strategic moves* dalam konteks lima kekuatan industri yang sudah dikenal mahasiswa, sementara TPGS Ch.6 (Gamble, Peteraf & Thompson 2021) menyediakan taksonomi taktis yang lebih kaya tentang kapan dan bagaimana setiap gerakan dipilih.

### Pertanyaan Inti yang Akan Dijawab

Pertanyaan inti pertemuan ini dapat dirumuskan dalam tiga klausa yang saling terkait: **apakah serangan akan dilancarkan terhadap pesaing atau apakah posisi sendiri akan diperkuat secara defensif**, **kapan waktu masuk ke pasar atau ke segmen baru paling tepat**, dan **seberapa luas lingkup aktivitas yang harus dikerjakan sendiri oleh perusahaan dibandingkan diserahkan kepada mitra eksternal**. Ketiga pertanyaan ini bukan pilihan independen; jawaban atas satu pertanyaan akan membatasi pilihan yang masuk akal untuk dua pertanyaan lainnya. Sebuah serangan ofensif terhadap pemimpin pasar, misalnya, hanya kredibel bila perusahaan memiliki lingkup sumber daya internal yang memadai dan memilih waktu serangan yang tepat dengan kondisi makro industri.

### *The Execution Gap*: Mengapa Pilihan Strategi Saja Tidak Cukup

Salah satu temuan paling konsisten dalam literatur strategi adalah apa yang oleh Kaplan dan Norton (2001) disebut sebagai ***execution gap***: jurang antara strategi yang dirumuskan dan strategi yang benar - benar dilaksanakan. Studi empiris yang menjadi rujukan dalam *Balanced Scorecard* literatur menunjukkan bahwa hanya sekitar 10 persen dari strategi yang dirumuskan dengan baik berhasil dieksekusi dengan baik pula. Sisanya gugur bukan karena pilihan strategi yang salah, melainkan karena infrastruktur eksekusi — sistem pengukuran, *incentive*, struktur organisasi, alokasi sumber daya — tidak diselaraskan dengan strategi yang dipilih. **Pertemuan 6 bertujuan menjembatani jurang ini dengan memberikan kosakata analitis yang konkret untuk gerakan, waktu, dan lingkup, sehingga pilihan strategi generik Pertemuan 5 dapat diterjemahkan menjadi keputusan operasional yang dapat diuji dan diukur.**

---

## 2. *Offensive Strategies*

### *Frontal Attack*

Serangan frontal adalah konfrontasi langsung terhadap kekuatan utama pemimpin pasar pada dimensi yang menjadi keunggulan pemimpin tersebut. Sebuah perusahaan menyerang produk inti pesaing dengan produk substitusi yang sebanding atau lebih baik, pada harga yang sebanding atau lebih rendah, di pasar yang sama. Dalam tradisi militer yang menjadi inspirasi taksonomi ini, *frontal attack* membutuhkan superioritas sumber daya yang substansial. **Aturan Lanchester yang sering dirujuk dalam literatur pemasaran strategik menyatakan rasio superioritas sumber daya minimum 3:1** untuk peluang keberhasilan yang masuk akal — penyerang harus memiliki cadangan modal, kapasitas produksi, dan jaringan distribusi yang setidaknya tiga kali lebih besar dari yang akan digunakan dalam pertempuran terbuka. Tanpa superioritas seperti ini, *frontal attack* berisiko menjadi *attritional warfare* yang merugikan kedua belah pihak tetapi tidak pernah memberi penyerang kemenangan struktural.

Logika ekonomis di balik aturan ini sederhana: pemimpin pasar memiliki keunggulan defensif dari skala, *brand recognition*, dan kurva pengalaman. Untuk mengikis keunggulan tersebut secara langsung, penyerang harus mampu menyerap kerugian jangka pendek lebih lama dari yang dapat dilakukan pemimpin. Bila penyerang lebih kecil, pemimpin dapat sekadar menurunkan harga sebagai balasan, dan penyerang yang sumber dayanya lebih tipis akan kehabisan napas terlebih dahulu. Itulah sebabnya *frontal attack* yang berhasil dalam sejarah korporat sering dilakukan oleh perusahaan dengan akses modal yang substansial dan komitmen jangka panjang terhadap pasar yang diserang.

### *Flanking Attack*

*Flanking attack* menyerang sisi yang lemah dari posisi pesaing — segmen pasar yang dilayani secara tidak optimal, kebutuhan pelanggan yang diabaikan, atau wilayah geografis yang tidak diprioritaskan. Logika ofensif di sini adalah menghindari konfrontasi langsung dengan kekuatan pesaing dan justru mengeksploitasi celah yang tidak dijaga. *Flanking* secara empiris memiliki tingkat keberhasilan yang lebih tinggi dibandingkan *frontal attack* karena tidak memicu balasan agresif segera; pesaing yang merasa segmen yang diserang bukan inti bisnisnya cenderung lambat merespons.

Contoh Indonesia yang paling jelas adalah Gojek yang melakukan *flanking* terhadap dominasi Grab di segmen *ride-hailing* dengan masuk lebih awal ke segmen merchant melalui GoFood dan GoPay. Daripada bertarung langsung dengan Grab di harga *ride*, Gojek membangun ekosistem layanan tambahan yang menciptakan *lock-in* berbeda. Setelah ekosistem matang, posisi *ride-hailing* sendiri menjadi lebih sulit ditandingi karena pelanggan sudah terikat pada GoPay dan jaringan merchant.

### *Guerrilla Warfare*

*Guerrilla warfare* adalah serangan kecil dan terukur yang dilakukan secara konsisten di banyak titik, sering tanpa pola yang dapat diprediksi pesaing. Tujuannya bukan kemenangan struktural dalam satu pertempuran melainkan akumulasi gangguan yang menggerogoti pangsa pasar pesaing secara bertahap. Strategi ini cocok untuk perusahaan kecil yang tidak memiliki sumber daya untuk konfrontasi terbuka tetapi memiliki kelincahan operasional. Kelemahannya jelas: *guerrilla* tidak memenangkan posisi pasar yang berkelanjutan, hanya memperlambat ekspansi pesaing.

### *Preemptive Strike*

*Preemptive strike* adalah gerakan menempati posisi strategik sebelum pesaing memahaminya sebagai posisi yang berharga. Bentuknya bervariasi: mengikat pemasok kunci dengan kontrak eksklusif jangka panjang, mengakuisisi *brand* yang berpotensi menjadi pesaing di masa depan, atau menutup akses regulasi terhadap pasar baru melalui *first-mover lobbying*. **Logika *preemptive* berakar pada irreversibilitas: setelah pesaing tahu posisi tersebut berharga, biaya menempatinya akan melonjak dramatis.** Tokopedia, dalam fase ekspansi awalnya, melakukan kombinasi *preemptive* dengan *flanking* terhadap Shopee melalui program edukasi penjual yang membentuk loyalitas penjual menengah dan kecil sebelum Shopee memprioritaskan segmen tersebut.

### Kapan Menyerang vs. Kapan Mengisi Celah

**Pertanyaan kritis bukan seberapa agresif menyerang melainkan apakah perusahaan benar - benar memiliki kondisi yang memungkinkan serangan berhasil.** TPGS Ch.6 menyebut tiga prasyarat: superioritas sumber daya yang dapat dipertahankan, target yang lebih lemah daripada yang terlihat di permukaan, dan kemampuan menyerap balasan dari pesaing. Bila salah satu prasyarat ini tidak terpenuhi, alternatif yang lebih masuk akal adalah mengisi celah pasar yang tidak diperebutkan, yang dalam terminologi *Blue Ocean* (Kim & Mauborgne 2005) disebut sebagai *uncontested market space*. Banyak perusahaan Indonesia yang lebih bijak memilih jalur kedua: Kopi Kenangan tidak menyerang Starbucks dalam segmen *premium specialty* melainkan menciptakan kategori *affordable specialty coffee* dengan harga di bawah Rp 25.000.

---

## 3. *Defensive Strategies*

### *Fortify-and-Defend*

*Fortify-and-defend* adalah strategi defensif paling dasar: memperkuat posisi yang sudah dimiliki sehingga biaya menyerangnya menjadi prohibitif bagi pesaing. Bentuk konkretnya adalah investasi berkelanjutan dalam dimensi yang menjadi sumber keunggulan — *brand* untuk diferensiator, efisiensi untuk *cost leader* — sehingga setiap upaya menandingi memerlukan investasi yang tidak proporsional. **Strategi ini efektif ketika perusahaan benar - benar memimpin pasar dan memiliki kemampuan untuk terus berinvestasi pada dimensi yang menjadi sumber keunggulannya. Strategi ini gagal ketika investasi pada dimensi tersebut menjadi rutin dan tidak lagi menciptakan diferensiasi nyata bagi pelanggan**, kondisi yang dalam literatur disebut *competitive parity creep*.

### *Signaling*: Teori Kredibilitas

*Signaling* adalah pengiriman sinyal kepada pesaing tentang konsekuensi yang akan diterima bila mereka melakukan gerakan tertentu. Schelling (1960) dalam *The Strategy of Conflict* menjelaskan bahwa ancaman hanya efektif bila kredibel, dan kredibilitas dibangun dengan komitmen yang sulit dibatalkan. *Brand investment* yang masif, kontrak jangka panjang dengan distributor, atau pengumuman publik tentang investasi *capacity expansion* yang besar adalah bentuk *signaling*: bila pesaing tahu bahwa perusahaan telah menanamkan komitmen yang besar untuk mempertahankan posisinya, biaya serangan akan dipersepsikan lebih tinggi karena perusahaan tidak akan mundur. Sampoerna selama dekade 2000-an menggunakan *brand architecture* berlapis — A Mild, Sampoerna Hijau, Dji Sam Soe — sebagai sinyal kepada Gudang Garam dan Bentoel bahwa perusahaan tidak akan menyerahkan satu pun segmen tanpa pertahanan ekonomis yang substansial.

### *Mobile Defense* dan *Counteroffensive*

*Mobile defense* adalah strategi memperluas atau menggeser posisi defensif sehingga pesaing tidak dapat menarget satu titik tertentu. Perusahaan dapat melakukan *market broadening* dengan masuk ke segmen yang berdekatan, atau *market diversification* dengan masuk ke industri yang terkait. *Counteroffensive* adalah respons agresif terhadap serangan: ketika pesaing menyerang, perusahaan tidak bertahan di posisi yang diserang melainkan menyerang balik di pasar inti pesaing. Logikanya adalah ekonomi politik: bila pesaing tahu serangannya akan memicu kerusakan pada bisnis intinya sendiri, ia akan berpikir dua kali sebelum melakukan serangan.

### *Barriers to Entry* sebagai *Moat*

**Yang membedakan perusahaan dengan posisi defensif yang berkelanjutan dari yang sekadar bertahan jangka pendek adalah keberadaan *barriers to entry* yang nyata** — *moat* dalam terminologi Buffett. *Switching cost* adalah salah satu *moat* yang paling efektif. BCA dalam dua dekade terakhir membangun *moat* berbasis biaya pindah pada produk *Current Account Saving Account* (CASA): integrasi BCA mobile, jaringan ATM yang masif, dan layanan *internet banking* yang andal menciptakan biaya peralihan yang nyata bagi nasabah retail. Akibatnya, pesaing tidak dapat menyerang dengan sekadar menawarkan suku bunga lebih tinggi; mereka harus menawarkan *value proposition* yang cukup besar untuk mengatasi *switching cost*. **Pertahanan pasif yang tidak didukung *moat* struktural akan gagal dalam jangka menengah karena pesaing yang sabar dapat secara bertahap mengikis posisi yang dipertahankan.**

---

## 4. *Timing Strategies*

### Lima Mekanisme *First-Mover Advantage*

Literatur strategi mengidentifikasi lima mekanisme yang dapat membuat *first-mover* memperoleh keunggulan tahan lama. **Pertama, *learning curve***: yang masuk lebih awal memiliki lebih banyak siklus produksi, sehingga dapat menurunkan biaya per unit lebih cepat dan mengunci keunggulan biaya struktural. **Kedua, *resource pre-emption***: aktor pertama dapat mengikat sumber daya langka — lokasi prima, lisensi regulasi, mineral langka, talenta utama — sebelum pesaing menyadari nilainya. **Ketiga, *network effects***: dalam pasar yang nilainya naik dengan jumlah pengguna, *first-mover* yang berhasil mencapai *critical mass* akan sulit digusur karena pengguna baru akan memilih platform terbesar. **Keempat, *brand loyalty***: pengalaman pertama pelanggan terhadap kategori produk membentuk persepsi standar; merek pertama menjadi prototipe kategori. **Kelima, *switching-cost lock-in***: ketika pelanggan sudah menanamkan biaya non-finansial pada platform pertama (data, kebiasaan, integrasi), biaya peralihan menjadi tinggi.

### Tiga Beban *First-Mover*

**Namun *first-mover advantage* bukan determinisme; ada tiga beban yang harus ditanggung pionir.** *Pioneer costs* adalah biaya mendidik pasar tentang kategori produk baru — periklanan kategori, edukasi konsumen, lobi regulator. Pesaing yang masuk kemudian dapat *free ride* pada edukasi yang sudah dilakukan pionir. *Technological uncertainty* adalah risiko bahwa standar teknologi yang dipilih pionir ternyata bukan yang akhirnya menang di pasar; Sony Betamax versus VHS adalah contoh klasik. *Market education burden* adalah beban panjang membentuk kebiasaan pelanggan baru, yang dapat memakan waktu bertahun-tahun sebelum permintaan benar-benar matang.

### *Fast-Follower* Logic

*Fast-follower* memilih masuk segera setelah pionir tetapi sebelum pasar matang. Logika ekonomisnya adalah belajar dari kesalahan pionir, menghindari biaya edukasi pasar, dan masuk dengan produk yang lebih halus. Samsung dalam pasar *smartphone* adalah arketipe *fast-follower*: Apple membuka kategori, Samsung mengikuti dengan produk yang teknologinya berkembang cepat dan harganya lebih akomodatif. Microsoft dalam mesin pencari (Bing setelah Google) atau jaringan sosial bisnis (Microsoft Teams setelah Slack) menggunakan strategi serupa. Di Indonesia, Grab adalah *fast-follower* terhadap Gojek di *ride-hailing*; OVO adalah *fast-follower* terhadap GoPay di *e-wallet*.

### *Late-Mover* Rationality

*Late-mover* yang masuk setelah pasar matang sering dianggap akan kalah, tetapi ada kondisi rasional untuk pilihan ini. Bila perusahaan memiliki *complementary asset* yang masif (jaringan distribusi, *brand* lintas industri, akses regulasi), masuk terlambat tidak menjadi handicap. *Late-mover* juga menguntungkan ketika teknologi yang menjadi inti kategori berubah signifikan, sehingga pengalaman pionir menjadi tidak relevan — contoh klasik adalah masuknya operator telekomunikasi mobile incumbent ke pasar 5G *enterprise solutions* dimana keunggulan jaringan eksisting lebih penting daripada *first-mover advantage* di vertikal tertentu.

### Aturan Emas Timing

**Aturan emas yang dapat ditarik adalah: pilih untuk menjadi *first-mover* hanya ketika lima mekanisme keunggulan dapat diaktifkan dan tiga beban dapat diserap; pilih *fast-follower* ketika pesaing pionir dapat mengedukasi pasar untuk Anda; pilih *late-mover* hanya ketika *complementary asset* yang dimiliki cukup masif untuk mengatasi *first-mover advantage* yang sudah terkunci.** Kesalahan paling umum adalah memilih *first-mover* untuk alasan psikologis (gengsi pionir) tanpa kalkulasi mekanisme dan beban.

---

## 5. *Scope of Operations*

### *Vertical Integration*

*Vertical integration* adalah keputusan memperluas lingkup aktivitas perusahaan ke arah hulu (pemasok) atau hilir (distribusi/pelanggan). Backward integration mengamankan input kritis dan margin pemasok; forward integration mengamankan akses pelanggan dan margin distributor. Pertamina secara historis melakukan backward integration dari distribusi BBM ke kilang dan eksplorasi hulu, menciptakan kontrol penuh terhadap *value chain* energi nasional. Telkom Indonesia melakukan vertical integration di broadband — dari infrastruktur fiber, jaringan, hingga layanan *content* — sehingga *bottleneck* di salah satu lapisan dapat dikontrol langsung. Keuntungan integrasi vertikal adalah kontrol kualitas, kepastian pasokan, dan *margin capture*; biayanya adalah hilangnya fleksibilitas dan beban modal yang tinggi.

### *Strategic Outsourcing* dan Risiko *Hollowing-Out*

*Strategic outsourcing* adalah keputusan menyerahkan aktivitas tertentu kepada mitra eksternal yang lebih efisien atau lebih ahli. Logikanya adalah fokus pada *core competence* dan biarkan aktivitas non-inti dijalankan oleh pemain spesialis. **Risiko terbesar adalah *hollowing-out*: perusahaan kehilangan kapabilitas yang seharusnya menjadi sumber keunggulan jangka panjang karena aktivitas yang menumbuhkan kapabilitas itu telah dialihdayakan.** Industri elektronika konsumen Amerika dalam dekade 1990-an–2000-an adalah pelajaran klasik: ketika manufaktur perangkat keras dialihdayakan ke kontraktor Asia, kemampuan integrasi *hardware-software* yang menjadi sumber inovasi juga ikut hilang. Kapabilitas yang sudah hilang sangat sulit dibangun kembali.

### *Strategic Alliances* dan *Joint Ventures*

*Strategic alliance* adalah kerja sama formal tanpa pembentukan entitas baru, sementara *joint venture* membentuk entitas baru yang dimiliki bersama. Astra International adalah arketipe perusahaan Indonesia dengan jaringan aliansi yang ekstensif: *joint venture* dengan Honda dan Toyota di otomotif, dengan Daihatsu, dengan United Tractors di alat berat. Logika strategik aliansi adalah berbagi risiko, mengakses kapabilitas yang tidak dimiliki, dan mempercepat *time to market*. Trade-off klasik adalah antara *speed*, *control*, dan *learning*: aliansi memberi kecepatan dan akses pembelajaran tetapi mengorbankan kontrol; akuisisi memberi kontrol penuh tetapi memerlukan modal dan integrasi yang mahal.

### *Mergers & Acquisitions*

*M&A* adalah perluasan lingkup melalui pengambilalihan atau penggabungan perusahaan lain. Merger GoTo (Gojek dan Tokopedia) pada 2021 adalah contoh ekspansi lingkup yang ambisius: dua *super-app* yang saling melengkapi digabungkan untuk menciptakan ekosistem digital end-to-end. Logikanya adalah skala, sinergi, dan posisi defensif terhadap pemain global. Risiko M&A adalah eksekusi integrasi: literatur menunjukkan mayoritas merger gagal menciptakan nilai karena masalah integrasi budaya, sistem, dan insentif yang diremehkan dalam fase deal-making.

### *Transaction Cost Economics* sebagai Kerangka *Make-or-Buy*

**Williamson (1975, 1985) dengan *Transaction Cost Economics* (TCE) menyediakan kerangka analitis untuk keputusan *make-or-buy*.** Tiga variabel kunci menentukan apakah aktivitas sebaiknya diinternalkan atau dialihdayakan: *asset specificity* (seberapa khusus aset yang diperlukan untuk transaksi tersebut — semakin khusus, semakin tepat diinternalkan), *uncertainty* (semakin tinggi ketidakpastian, semakin mahal kontrak eksternal yang lengkap), dan *frequency* (semakin sering transaksi, semakin masuk akal investasi pada hubungan internal). TCE menjelaskan mengapa Pertamina menginternalkan kilang (asset specificity tinggi, frekuensi tinggi) tetapi mengalihdayakan jasa pengeboran tertentu (asset specificity sedang, kontrak dapat diatur). **TCE bukan resep kaku melainkan kerangka untuk berpikir disiplin tentang apa yang harus dimiliki dan apa yang dapat dipinjam.**

---

## 6. *Blue Ocean Strategy*

### *Value Innovation* vs. *Competitive Advantage*

*Blue Ocean Strategy* yang dikembangkan Kim dan Mauborgne (2005) menempatkan dirinya sebagai *counter-paradigm* terhadap pemikiran kompetitif Porter. Bila Porter mengasumsikan bahwa keunggulan diperoleh dengan memilih posisi dalam *trade-off* yang sudah ada (cost vs. differentiation, broad vs. focused), Kim dan Mauborgne mengusulkan ***value innovation*** sebagai strategi memecah *trade-off* itu sendiri. Inti argumennya: di pasar yang sudah jenuh (*red ocean*), perusahaan saling memperebutkan demand yang ada dan margin tergerus. Strategi yang lebih baik adalah menciptakan ruang pasar baru (*blue ocean*) di mana persaingan belum terbentuk, dengan menawarkan kombinasi nilai yang sebelumnya tidak dianggap mungkin.

### *Eliminate-Reduce-Raise-Create Grid*

Kerangka operasional *Blue Ocean* adalah ERRC grid: empat pertanyaan tentang elemen yang dapat dieliminasi, dikurangi, ditingkatkan, dan diciptakan. Cirque du Soleil adalah contoh kanonik: mengeliminasi pertunjukan binatang (yang mahal dan kontroversial), mengurangi humor klasik sirkus (yang dianggap kurang sofistikasi), meningkatkan elemen artistik dan narasi, serta menciptakan pengalaman teatrikal yang sebelumnya tidak ada dalam kategori sirkus. Hasilnya adalah kategori baru — sirkus untuk audiens dewasa yang bersedia membayar harga premium — yang tidak bersaing dengan sirkus tradisional.

### Kritik: Apakah *Blue Ocean* Berkelanjutan?

**Kritik substantif terhadap *Blue Ocean* adalah bahwa apa yang diklaim sebagai pasar baru sering hanya *first-mover red ocean* dengan label baru.** Setelah *blue ocean* terbukti menguntungkan, imitator akan masuk dan mengubahnya menjadi *red ocean* dalam waktu singkat. Cirque du Soleil sendiri menghadapi imitator dalam beberapa tahun, demikian pula JetBlue, Curves, dan kasus-kasus lain yang sering dikutip dalam buku Kim dan Mauborgne. Jika keunggulan *blue ocean* hanya bertahan selama jendela *first-mover*, apakah ia benar-benar paradigma yang berbeda dari Porter, atau hanya cara baru menyebut *first-mover* di kategori yang baru?

### *Counter-Counter-Argument*

**Pembelaan yang masuk akal adalah bahwa nilai *Blue Ocean* terletak pada *proses* inovasi nilai, bukan pada posisi permanen yang tercipta.** McGrath (2013) dengan konsep *transient advantage* menyatakan bahwa di lingkungan yang berubah cepat, tidak ada keunggulan kompetitif yang permanen; yang ada adalah rangkaian keunggulan sementara yang harus diperbarui terus. Dalam logika ini, *Blue Ocean* adalah disiplin organisasi untuk terus mencari *uncontested space* baru, bukan posisi tunggal yang akan dipertahankan selamanya. Kopi Kenangan menciptakan *quasi-blue-ocean* pada *affordable specialty coffee* di Indonesia; Ruangguru menciptakan ruang baru di *edu-tech* yang memadukan *content* digital dengan model bimbingan belajar yang sudah dikenal. Keduanya kini menghadapi kompetitor — Fore Coffee, Kopi Janji Jiwa, Kelas Pintar, Zenius — yang menunjukkan bahwa keunggulan *blue ocean* memang transient, tetapi periode *first-mover* yang dimanfaatkan untuk membangun *brand* dan ekosistem dapat menjadi modal berharga untuk pertarungan *red ocean* berikutnya.

---

## 7. *Performance Measurement* sebagai Eksekusi

### *Balanced Scorecard*: Empat Perspektif

*Balanced Scorecard* (BSC) yang dikembangkan Kaplan dan Norton (1992, 1996) adalah respons terhadap kegagalan sistem pengukuran kinerja tradisional yang terlalu didominasi indikator finansial. Empat perspektif yang diusulkan adalah *financial*, *customer*, *internal process*, dan *learning & growth*. Logika di balik empat perspektif ini bukan sekadar memperbanyak metrik melainkan mengikat kausalitas antarperspektif: investasi pada *learning & growth* menggerakkan *internal process* yang lebih baik, yang menggerakkan kepuasan *customer*, yang akhirnya menggerakkan kinerja *financial*. BSC bukan dashboard pasif melainkan kerangka manajerial yang mengarahkan keputusan investasi dan alokasi sumber daya.

### *Strategy Maps*: Mengikat Kausalitas

*Strategy maps* yang diperkenalkan Kaplan dan Norton (2001) memvisualkan rantai sebab-akibat antarperspektif. Setiap target finansial dihubungkan dengan target *customer* yang memungkinkannya, setiap target *customer* dengan proses internal yang membentuknya, dan seterusnya hingga investasi *learning & growth* yang menjadi fondasi paling dalam. Manfaat utamanya adalah membuat asumsi kausal eksplisit: bila kinerja finansial tidak tercapai, manajer dapat menelusuri ke perspektif mana asumsi yang diuji ternyata gagal. Tanpa *strategy maps*, organisasi sering mengoptimalkan satu perspektif (biasanya *financial*) dengan mengorbankan perspektif lain yang tidak terlihat.

### Mengapa *Strategic Moves* Gagal Tanpa PMS

**Argumen sentral bagian ini adalah bahwa *strategic moves* — ofensif, defensif, *timing*, *scope* — tidak akan menghasilkan kinerja yang diharapkan tanpa *performance measurement system* (PMS) yang diselaraskan dengan strategi.** Kaplan dan Norton (2001) melaporkan bukti empiris yang konsisten: perusahaan dengan strategi yang tepat tetapi PMS yang lemah secara konsisten kalah dari perusahaan dengan strategi rata-rata tetapi PMS yang excellent. Mekanismenya jelas: PMS adalah *feedback loop* yang memberi tahu manajer apakah gerakan yang dilakukan menghasilkan dampak yang diharapkan, dan apakah arah perlu dikoreksi. Tanpa *feedback loop* ini, manajer mengandalkan intuisi yang mudah salah dan bias konfirmasi yang menyembunyikan masalah.

### Jembatan ke Teeratansirikool et al. (2013)

Inilah jembatan langsung ke Artikel 9. Teeratansirikool dan kolega secara empiris menguji argumen di atas: apakah PMS memediasi hubungan antara strategi kompetitif dan kinerja perusahaan. Temuan utamanya — yang akan dikupas dalam *Critical Review* — adalah bahwa **PMS memang memediasi hubungan tersebut secara signifikan**, tetapi dengan kualifikasi yang penting: financial measures memiliki peran mediator yang lebih kuat daripada non-financial measures dalam konteks Thailand. Implikasi bagi diskusi ini: *Balanced Scorecard* yang sering diasumsikan sebagai standar emas mungkin tidak universal; konteks pasar berkembang dapat membuat *financial measures* tetap dominan sebagai mekanisme transmisi strategi ke kinerja.

---

## 8. Strategi Kompetitif dan Kinerja: Apa yang Kita Ketahui?

### Konsensus yang Kokoh

**Setelah lebih dari empat dekade riset empiris pada hubungan strategi–kinerja, ada beberapa hal yang sudah cukup kokoh sebagai konsensus.** Meta-analisis kanonik Campbell-Hunt (2000) yang mensintesis 17 studi menyimpulkan bahwa perusahaan dengan strategi yang jelas — apakah cost leadership atau differentiation — secara konsisten mengungguli perusahaan yang ambigu antara keduanya. *Stuck in the middle* yang diperingatkan Porter (1985) bukan sekadar kategorisasi teoretis melainkan kondisi yang secara empiris terdokumentasi merugikan kinerja. Ini adalah temuan yang stabil lintas industri, periode waktu, dan konteks geografis.

### Debat yang Belum Selesai

**Apa yang belum selesai adalah pertanyaan strategi mana yang lebih unggul: cost leadership atau differentiation.** Studi-studi empiris menghasilkan jawaban yang berbeda tergantung industri, periode, dan metodologi yang digunakan. Beberapa studi (Allen dan Helms 2006, Powers dan Hahn 2004) menemukan cost leadership menghasilkan kinerja yang lebih baik di sektor tertentu; studi lain (Phillips et al. 1983, Spanos et al. 2004) menemukan differentiation lebih unggul; sebagian lagi (Pertusa-Ortega et al. 2009) menemukan strategi hybrid yang menggabungkan elemen keduanya menghasilkan hasil terbaik. Yang lebih kontroversial adalah temuan Teeratansirikool et al. (2013) bahwa **dalam konteks Thailand cost leadership tidak memiliki hubungan langsung yang signifikan dengan kinerja perusahaan, sementara differentiation memiliki**. Apakah temuan ini berlaku untuk pasar berkembang lainnya, termasuk Indonesia, adalah pertanyaan terbuka.

### Peran *Moderating Variables*

**Yang semakin diakui adalah bahwa hubungan strategi–kinerja sangat dimediasi dan dimoderasi oleh variabel kontekstual.** Struktur industri, intensitas kompetisi, ukuran perusahaan, umur perusahaan, struktur kepemilikan, kondisi institusional — semua mempengaruhi seberapa kuat strategi yang sama menghasilkan kinerja. Onditi (2018) yang akan menjadi fokus *Critical Review* berikutnya secara eksplisit mengusulkan *firm characteristics* sebagai moderator yang underspecified dalam literatur sebelumnya. Implikasinya: pertanyaan "strategi mana yang lebih baik" tidak memiliki jawaban universal; jawabannya selalu *contingent* pada karakteristik perusahaan dan lingkungannya.

### Jembatan ke Onditi (2018)

Onditi (2018) memberikan sintesis literatur yang lebih luas tentang topik ini, dengan menambahkan dua perspektif teoretis yang menjadi alternatif Porter: *Resource-Based View* (RBV) dan *value disciplines* (Treacy & Wiersema 1993). RBV menempatkan sumber keunggulan pada bundel sumber daya internal yang sulit ditiru, sementara *value disciplines* mengusulkan tiga kategori — *operational excellence*, *product leadership*, *customer intimacy* — sebagai alternatif taksonomi Porter. **Kontribusi utama Onditi adalah menunjukkan bahwa pemikiran strategi kompetitif tidak monolitik; ada beberapa kerangka yang saling melengkapi.** Bagaimana ketiga kerangka ini dapat diintegrasikan dan apa konsekuensinya bagi riset Indonesia menjadi diskusi yang akan dikupas pada *Critical Review* Artikel 10.

---

## 9. Kesimpulan

### Strategi sebagai Proses Kalibrasi Berkelanjutan

Sintesis Pertemuan 6 dapat dirumuskan dalam satu kalimat: **strategi bukan keputusan satu kali yang dibuat di awal melainkan proses kalibrasi berkelanjutan yang merespons perubahan kondisi industri dan pesaing.** Ofensif, defensif, *timing*, dan *scope* adalah keluarga keputusan yang harus ditinjau ulang secara periodik karena prasyarat yang membenarkan pilihan tertentu dapat berubah. Perusahaan yang berhenti pada perumusan strategi awal dan mengabaikan kalibrasi akan tergerus oleh pesaing yang lebih lincah, sementara perusahaan yang membangun infrastruktur PMS yang baik dapat mendeteksi perubahan kondisi lebih cepat dan mengkalibrasi gerakannya secara proaktif.

### Integrasi Alur Analitik Pertemuan 4–6

Alur analitik tiga pertemuan terakhir dapat disusun sebagai rantai logis yang utuh. **Pertemuan 4 (RBV)** memetakan sumber daya dan kapabilitas internal yang menjadi dasar potensi keunggulan. **Pertemuan 5 (Generic Strategies)** menerjemahkan potensi tersebut menjadi pilihan posisi kompetitif yang konkret. **Pertemuan 6 (Strengthening Position)** memberikan kosakata untuk memperdalam, mempertahankan, dan mengkalibrasi posisi tersebut, serta sistem pengukuran yang menjadi *feedback loop* eksekusi. Ketiganya tidak dapat dilepaskan: analisis sumber daya tanpa pilihan posisi adalah introspeksi yang tidak terhubung dengan pasar; pilihan posisi tanpa penguatan dan pengukuran adalah deklarasi yang tidak akan terealisasi.

### Antisipasi Pertemuan 7

Pertemuan 7 akan menambahkan satu lapisan analitis lagi: ***corporate-level strategy*** yang menjawab pertanyaan *di mana* perusahaan akan bersaing, bukan sekadar *bagaimana* bersaing dalam industri yang dipilih. Pertanyaan-pertanyaan seperti diversifikasi, *related vs. unrelated*, *portfolio management*, dan *parenting advantage* akan masuk ke dalam diskusi. Ini adalah perluasan logis dari yang dipelajari sejauh ini: setelah memahami bagaimana memenangkan posisi dalam satu industri, langkah berikutnya adalah memutuskan di industri mana saja perusahaan harus hadir dan bagaimana sinergi antarsegmen dapat dikelola. Astra International, GoTo, dan Salim Group adalah contoh konglomerat Indonesia yang menjawab pertanyaan korporat ini dengan jawaban yang berbeda; analisis komparatifnya akan membentuk inti pembahasan minggu depan.
"""


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT 2 — CRITICAL REVIEW ARTIKEL 9
# ══════════════════════════════════════════════════════════════════════════════
CR9 = r"""# CRITICAL REVIEW — ARTIKEL 9

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Identitas Artikel

**Penulis:** Luliya Teeratansirikool, Sununta Siengthai, Yuosre Badir, Chotchai Charoenngam

**Tahun:** 2013

**Judul:** *Competitive Strategies and Firm Performance: The Mediating Role of Performance Measurement*

**Jurnal:** *International Journal of Productivity and Performance Management*, Vol. 62, Iss. 2, pp. 168–184

**Penerbit:** Emerald Group Publishing

**DOI:** 10.1108/17410401311295722

**Institusi Penulis:** School of Management, Asian Institute of Technology (AIT), Pathumthani, Thailand; School of Engineering and Technology, AIT; Faculty of Liberal Art and Management Science, Prince of Songkla University, Surat Thani, Thailand

**Tipe Riset:** Empiris kuantitatif — *cross-sectional mail survey* terhadap 561 perusahaan tercatat di Bursa Efek Thailand (SET), 101 respons (*response rate* 18 persen). Analisis dengan SPSS 11.5 menggunakan *factor analysis*, *correlation*, *regression*, dan *path analysis* berbasis *ordinary least squares* (OLS).

**Konteks Publikasi:** *International Journal of Productivity and Performance Management* (IJPPM) adalah jurnal yang berfokus pada produktivitas dan manajemen kinerja, sehingga penekanan pada *performance measurement* sebagai variabel kunci sesuai dengan agenda jurnal. Posisi penulis di AIT — sebuah institusi pascasarjana Asia yang berfokus pada teknologi dan manajemen — menjelaskan mengapa konteks empirisnya adalah perusahaan tercatat Thailand.

---

## 2. Tujuan dan Posisi dalam Literatur

### Pertanyaan Riset Utama

Tujuan eksplisit yang dirumuskan penulis adalah "*to examine the mediating role performance measurement plays in the relationship between competitive strategies and firm performance*" (Teeratansirikool et al. 2013, p. 168). Pertanyaan riset turunan yang diuji secara empiris adalah: (1) apakah strategi kompetitif berhubungan dengan kinerja perusahaan secara langsung; (2) apakah strategi kompetitif berhubungan dengan adopsi *performance measurement*; (3) apakah *performance measurement* berhubungan dengan kinerja perusahaan; dan (4) apakah hubungan strategi–kinerja bersifat tidak langsung melalui *performance measurement*. Empat pertanyaan ini diterjemahkan menjadi empat hipotesis utama (H1, H2, H3, H4) yang masing-masing memiliki sub-hipotesis untuk dua jenis strategi (cost leadership dan differentiation) dan dua jenis ukuran (financial dan non-financial).

### Posisi dalam Rantai Literatur

Penulis menempatkan kontribusinya pada celah riset yang spesifik. Mereka mengakui bahwa literatur sebelumnya — Kaplan dan Norton (1996), Neely et al. (1996), Bititci et al. (1997), Maltz et al. (2003), Gosselin (2005), Moullin (2007) — sudah menetapkan bahwa *performance measurement* berhubungan dengan kinerja perusahaan. Mereka juga mencatat bahwa sebagian literatur (Spencer et al. 2009, Joiner et al. 2009) sudah menyentuh peran mediator PMS, tetapi terbatas pada strategi spesifik (*differentiation* atau *flexible manufacturing*). **Klaim orisinalitas mereka adalah dua hal: pertama, mengintegrasikan kedua tipe strategi Porter (cost leadership dan differentiation) dalam satu model mediasi terpadu; kedua, melakukannya dalam konteks pasar berkembang Asia (Thailand) yang sebelumnya kurang terwakili dalam literatur PMS yang didominasi konteks Anglo-Saxon.** Posisi terhadap Campbell-Hunt (2000) yang merupakan meta-analisis kanonik strategi–kinerja juga eksplisit: penulis mengakui Campbell-Hunt sebagai titik referensi yang menetapkan bahwa "*the paradigm of competitive strategy is now over two decades old, [but] it has yet to prove its adequacy as a descriptive framework*" (p. 181), dan kontribusi mereka adalah bergerak melampaui taksonomi deskriptif menuju model kausal yang mengintegrasikan PMS sebagai mekanisme transmisi.

---

## 3. Argumen Utama

### H1: Strategi → Kinerja (Direct Effect)

Hipotesis pertama menyatakan ada hubungan langsung antara strategi kompetitif (cost leadership dan differentiation) dengan kinerja perusahaan. Landasan teoretisnya adalah klaim Porter (1985) bahwa "*firms that choose and implement generic strategies achieve sustained competitive advantage*" (dirujuk pada p. 170). **Hasil empiris yang dilaporkan: H1a (cost leadership → firm performance) ditolak karena koefisien path 0,12 tidak signifikan; H1b (differentiation → firm performance) didukung dengan koefisien path 0,48 signifikan pada p < 0,01** (Tabel III dan IV pada p. 177–178). Temuan ini sendiri sudah merupakan kontribusi yang menarik karena bertentangan dengan studi-studi sebelumnya seperti Powers dan Hahn (2004), Allen dan Helms (2006), serta Dess dan Davis (1984) yang menemukan asosiasi positif antara cost leadership dan kinerja.

### H2: Strategi → PMS

Hipotesis kedua menyatakan strategi kompetitif berhubungan dengan jenis dan intensitas adopsi *performance measurement*. Landasan teoretisnya merujuk pada *information processing theory* (Galbraith 1974, dikutip secara implisit) yang menyatakan bahwa perusahaan yang menjalankan strategi yang lebih kompleks memerlukan kapasitas pemrosesan informasi yang lebih besar, dan PMS adalah salah satu mekanisme tersebut. Penulis juga merujuk Miles dan Snow (1978): "*defender firms tend to use financial measures, while prospector firms prefer to use non-financial measures*" (p. 171). **Hasil yang dilaporkan: H2 didukung penuh — cost leadership dan differentiation keduanya signifikan terhubung dengan financial dan non-financial measures.** Cost leadership berhubungan dengan financial measures (β = 0,20, p < 0,05) dan non-financial measures (β = 0,31, p < 0,01); differentiation lebih kuat dengan kedua jenis ukuran (β = 0,26 dan β = 0,38, keduanya p < 0,01).

### H3: PMS → Kinerja (Direct Effect)

Hipotesis ketiga menyatakan adopsi PMS berhubungan dengan kinerja perusahaan. **Hasil yang dilaporkan menarik karena terbelah: H3a (financial measures → firm performance) didukung dengan β = 0,33 (cost leadership model) dan β = 0,23 (differentiation model), keduanya p < 0,01; H3b (non-financial measures → firm performance) ditolak karena β = 0,19 dan β = 0,03 keduanya tidak signifikan.** Temuan ini bertentangan dengan klaim Kaplan dan Norton (2001) serta Hoque (2004) bahwa "*non-financial measures are better predictor of firm performance*" (p. 179). Penulis menafsirkan: dalam konteks pasar Thailand yang menghadapi liberalisasi perdagangan, perusahaan menggunakan financial measures sebagai indikator survival yang lebih konkret.

### H3 sebagai Hipotesis yang Paling Vulnerable

**Hipotesis mediasi adalah hipotesis paling ambisius dan paling vulnerable secara metodologis.** Penulis menggunakan dekomposisi *path coefficients* untuk menghitung *direct*, *indirect*, dan *total effects*. Tabel IV (p. 178) melaporkan: untuk cost leadership, *direct effect* 0,12 (tidak signifikan), *indirect effect* via financial measures 0,06, *total effect* 0,18; untuk differentiation, *direct* 0,48, *indirect* via financial 0,06, *total* 0,54. **Penulis menyimpulkan bahwa "*the amount of total effect in all relationships is higher than direct effect. It indicates that both types of performance measures, financial and non-financial measures, mediate the relationship*" (p. 179).** Klaim ini akan menjadi sasaran kritik metodologis pada §7.

### Kerangka Path Analysis

Penulis tidak menggunakan SEM-PLS atau SEM kovariansi yang biasa dipakai untuk mediasi modern. Mereka menggunakan **OLS regression-based path analysis dengan SPSS 11.5** (p. 173, 176). Pendekatan ini lebih sederhana tetapi membatasi kemampuan menguji *full structural model* dan tidak memberikan *bootstrap confidence intervals* untuk *indirect effects* sebagaimana dianjurkan Preacher dan Hayes (2008) dalam tradisi mediasi modern. Pilihan metodologis ini akan menjadi salah satu titik kritik di bagian Evaluasi Kritis.

---

## 4. Koneksi ke Topik Silabus

### PMS sebagai Infrastruktur Eksekusi *Strategic Moves*

Artikel ini langsung berkoneksi dengan §7 RMK Pertemuan 6 yang membahas *performance measurement* sebagai eksekusi. **Argumen kunci yang dikuatkan oleh artikel ini adalah: *strategic moves* — apakah ofensif, defensif, *timing*, atau *scope* — tidak akan menghasilkan kinerja yang diharapkan tanpa infrastruktur pengukuran yang diselaraskan dengan strategi.** PMS bukan tambahan administratif melainkan mekanisme transmisi yang mengubah pilihan strategi menjadi tindakan operasional terukur. Temuan empiris Teeratansirikool et al. memberikan dukungan kuantitatif terhadap argumen kualitatif Kaplan dan Norton (2001) tentang *execution gap*.

### Mengapa Tanpa PMS, *Strategic Moves* Kehilangan *Feedback Loop*

Bila perusahaan melakukan serangan ofensif, misalnya, tanpa metrik yang melacak progres serangan tersebut, manajer tidak akan tahu apakah serangan menghasilkan dampak yang diharapkan, kapan harus menambah investasi, dan kapan harus mundur. **PMS adalah *feedback loop* yang menyediakan informasi untuk kalibrasi.** Tanpa *feedback loop*, pelaksanaan strategi mengandalkan intuisi dan bias kognitif yang oleh literatur *behavioral strategy* sudah didokumentasi sebagai sumber kegagalan strategis. Temuan Teeratansirikool bahwa *total effect* lebih besar dari *direct effect* mendukung klaim ini secara empiris: eksekusi melalui PMS menambah substansial pada dampak strategi, terutama untuk cost leadership yang *direct effect*-nya tidak signifikan. Bagi mahasiswa Magister Akuntansi, koneksi ini sangat relevan: profesi akuntansi manajemen memiliki posisi strategis untuk merancang dan mengoperasikan PMS yang kredibel, dan literatur ini menempatkan peran tersebut sebagai sumber nilai strategis, bukan sekadar fungsi pendukung.

---

## 5. Kekuatan Artikel

### Kontribusi Teoretis

**Kontribusi teoretis utama artikel ini adalah memformalkan PMS sebagai variabel mediator dalam rantai kausal strategi → kinerja**, bukan sekadar variabel kontrol atau korelat. Sebelum artikel ini, sebagian besar literatur memperlakukan PMS dan strategi sebagai dua variabel independen yang masing-masing berhubungan dengan kinerja. Teeratansirikool dan kolega mengintegrasikannya menjadi model kausal yang lebih kaya, di mana PMS menjadi *mechanism* yang menjelaskan *mengapa* strategi tertentu menghasilkan kinerja tertentu. Ini adalah pergeseran konseptual yang memperluas "*black box*" eksekusi strategi.

### Kekuatan Empiris

Sampel 101 perusahaan tercatat Thailand cukup memadai untuk *path analysis* berbasis OLS. Penulis melakukan beberapa langkah validasi yang patut dipuji: *back-translation* dari English ke Thai dan kembali untuk memastikan validitas instrumen lintas bahasa (p. 173); *pre-testing* dengan 20 CEO sebelum mailing penuh; *factor analysis* dengan rotasi varimax untuk mengkonfirmasi struktur dimensi strategi; dan pelaporan Cronbach's α untuk semua konstruk (financial measures 0,76; non-financial measures 0,91; firm performance 0,90). Reliabilitas konstruk untuk financial dan non-financial measures sangat tinggi.

### Relevansi Praktis

**Implikasi manajerial yang dirumuskan eksplisit dan operasional**: "*whether a firm chooses to pursue cost leadership or differentiation strategies, a strong emphasis on performance measurement will ensure the positive impact on firm performance*" (p. 168, abstract). Untuk manajer di pasar berkembang yang menghadapi keterbatasan sumber daya dan harus memilih investasi PMS yang prioritas, temuan bahwa financial measures memiliki efek mediasi yang dominan memberikan panduan praktis: investasi pada sistem pelaporan finansial yang baik harus didahulukan, dan investasi non-finansial sebagai pelengkap, bukan substitusi.

---

## 6. Keterbatasan dan Kelemahan

### Masalah Endogeneitas

**Masalah endogeneitas adalah keterbatasan paling serius dari artikel ini.** Hubungan yang diuji bersifat *cross-sectional*: data strategi, PMS, dan kinerja semuanya diambil pada satu titik waktu dari responden yang sama (CEO). Logika kausal yang diklaim (strategi → PMS → kinerja) tidak dapat dibedakan secara empiris dari beberapa alternatif: (1) perusahaan dengan kinerja baik mampu berinvestasi pada PMS yang lebih komprehensif (kausalitas terbalik); (2) perusahaan dengan *organizational capability* yang tinggi sama-sama mengadopsi strategi yang jelas, membangun PMS yang komprehensif, dan mencapai kinerja yang baik (variabel yang diabaikan); atau (3) ketiga variabel saling mempengaruhi dalam *feedback loop* yang tidak linier. **Penulis sendiri mengakui keterbatasan ini secara halus**: "*Future research could consider the use of longitudinal data to ascertain more clearly these causal relationships*" (p. 168, abstract; juga p. 181). Pengakuan ini jujur tetapi tidak mengurangi keterbatasan inferensi kausal pada studi *cross-sectional*.

### Keterbatasan Sampel

Sampel 101 perusahaan tercatat Thailand memiliki dua bias yang signifikan. **Pertama, *response rate* hanya 18 persen** — perusahaan yang merespons survei kemungkinan adalah yang memiliki PMS yang sudah cukup formal sehingga mampu menjawab pertanyaan teknis tentang ukuran kinerja. Ini adalah bias seleksi yang akan membesarkan estimasi hubungan PMS–kinerja. **Kedua, semua perusahaan tercatat di SET** — ini adalah perusahaan yang relatif besar, *governance* relatif formal, dan akses modal lebih baik dibandingkan UKM atau perusahaan tidak tercatat. Generalisasi ke populasi perusahaan yang lebih luas dipertanyakan, dan penulis mengakui ini secara eksplisit (p. 181): "*interpreting our results beyond that domain should be done with caution*".

### Validitas Konstruk

Pengukuran "*competitive strategy*" menggunakan tipologi Porter dengan metode *self-report* berbasis lima poin Likert. Kotha dan Vadlamani (1995, dirujuk dalam literatur PMS yang lebih luas) menunjukkan bahwa instrumen *self-report* untuk strategi memiliki masalah validitas: CEO cenderung menggambarkan strategi mereka sebagai jelas dan koheren bahkan ketika realitas operasional lebih ambigu. **Cronbach's α untuk cost leadership hanya 0,54 (p. 175)**, yang oleh penulis sendiri diakui sebagai "*slightly below 0.60*" dan dipertahankan dengan rujukan ke Nunnally dan Bernstein (1994) yang menyatakan "*α's of between 0.50 and 0.60 are generally acceptable for exploratory research*". Pertahanan ini lemah; reliabilitas konstruk yang rendah membuat *path coefficient* yang melibatkan cost leadership berisiko mengalami *attenuation bias* (estimasi underestimasi karena *measurement error*).

### *Common Method Variance*

Karena strategi, PMS, dan kinerja semua diukur melalui satu instrumen survei dari satu responden (CEO), data berisiko mengalami ***common method variance*** (CMV) — korelasi yang dihasilkan oleh metode pengukuran yang sama, bukan hubungan substantif antarvariabel. Podsakoff et al. (2003) dalam literatur metodologi menyarankan pemisahan sumber data atau Harman's single-factor test untuk mendeteksi CMV. **Artikel ini tidak melaporkan langkah-langkah untuk memitigasi atau mendeteksi CMV.** Bila CMV signifikan, sebagian dari hubungan yang dilaporkan mungkin artifak metode, bukan hubungan substantif.

---

## 7. Evaluasi Kritis

### Apakah Mediasi Terbukti atau Sekadar Diklaim?

**Inilah pertanyaan kritis paling penting.** Penulis menyimpulkan mediasi terbukti karena *total effect* lebih besar dari *direct effect*. Namun ini adalah pemahaman mediasi yang dangkal. Tradisi Baron dan Kenny (1986) menetapkan empat kondisi untuk mediasi: (1) X berhubungan dengan Y; (2) X berhubungan dengan M; (3) M berhubungan dengan Y dengan X dikontrol; (4) hubungan X–Y berkurang atau hilang ketika M dimasukkan. Tradisi modern (Preacher dan Hayes 2008) memperbaiki ini dengan *bootstrap test* untuk *indirect effect* secara langsung, yang lebih powerful dan tidak bergantung pada signifikansi *direct effect*.

Untuk cost leadership, *direct effect* tidak signifikan (0,12) dan *indirect effect via* financial measures hanya 0,06. **Apakah 0,06 signifikan secara statistik? Penulis tidak melaporkan** *bootstrap confidence interval* atau Sobel test untuk *indirect effect* — ini adalah celah metodologis yang serius. Tanpa uji formal terhadap *indirect effect*, klaim mediasi hanya didukung oleh perbandingan deskriptif antara *total* dan *direct effect*, yang tidak setara dengan inferensi statistik formal.

### Masalah *Mediation Theory*

**Masalah teoretis lebih dalam: bahkan bila mediasi dikonfirmasi secara statistik, interpretasinya tidak unik.** Mediasi parsial (yang kemungkinan ditemukan untuk differentiation: *direct* 0,48, *indirect* 0,06, total 0,54) konsisten dengan **dua interpretasi yang berbeda**:

- **Interpretasi A (yang diklaim penulis):** Differentiation menghasilkan kinerja secara langsung (direct path), dan juga melalui investasi pada PMS yang mengamplifikasi efeknya (indirect path). PMS adalah *genuine mediator*.
- **Interpretasi B (yang tidak dikecualikan):** Ada variabel laten *organizational capability* yang menggerakkan ketiganya — perusahaan dengan kapabilitas tinggi memilih differentiation, mengadopsi PMS yang lebih baik, dan mencapai kinerja yang lebih baik. PMS bukan mediator melainkan koreaksian dari penyebab umum.

**Disain *cross-sectional* tidak dapat membedakan kedua interpretasi ini.** Inilah yang oleh literatur *causal inference* (Pearl 2009) disebut sebagai *unobserved confounding* — masalah klasik yang hanya dapat diatasi dengan disain longitudinal, *instrumental variables*, atau eksperimen.

### Apa yang Seharusnya Dilakukan

Disain yang lebih ketat untuk menguji klaim mediasi memerlukan: (1) **panel longitudinal**: T1 strategi → T2 PMS → T3 kinerja, dengan kontrol untuk variabel di setiap periode; (2) ***instrumental variables***: variabel yang mempengaruhi adopsi PMS tetapi tidak langsung mempengaruhi kinerja, untuk mengisolasi efek kausal PMS; atau (3) **disain quasi-experimental**: membandingkan perusahaan yang mengalami perubahan eksogen dalam adopsi PMS (misalnya karena perubahan regulasi pelaporan) dengan yang tidak. Tidak satu pun pendekatan ini digunakan oleh penulis, dan ini bukan kritik yang tidak adil — pengakuan keterbatasan oleh penulis sendiri di bagian "*Agenda for future research*" (p. 181) menunjukkan kesadaran ini.

### Penilaian Kontribusi Orisinal

**Penilaian akhir saya: kontribusi konseptual artikel ini bernilai dan layak dipublikasi, tetapi bukti empirisnya sugestif, bukan konklusif.** Argumen mekanisme — bahwa PMS adalah jalur transmisi yang menghubungkan strategi dengan kinerja — adalah kontribusi teoretis yang substantif. Bukti empirisnya mendukung pola yang konsisten dengan argumen tersebut, tetapi tidak mengeksklusi alternatif yang sama plausibel. Untuk audiens akademik, artikel ini layak dijadikan referensi sebagai langkah pertama dalam program riset yang lebih panjang; untuk audiens praktisi, implikasi manajerialnya — investasi pada PMS yang diselaraskan dengan strategi — tetap berharga karena tidak bergantung pada interpretasi mediasi yang sempit.

---

## 8. Implikasi

### Implikasi Teoretis

Artikel ini memperluas "*black box*" eksekusi strategi dengan menempatkan PMS sebagai variabel teoretis yang dapat diukur dan diuji. **Kontribusi teoretis lebih dalam adalah memunculkan pertanyaan: apa lagi yang ada di dalam *black box* itu?** Bila PMS adalah salah satu mediator, mediator lain yang masuk akal adalah: budaya organisasi, sistem insentif, kapabilitas dinamis, *organizational ambidexterity*. Riset masa depan dapat membangun model mediasi multi-jalur yang menangkap kekayaan mekanisme eksekusi.

### Implikasi Manajerial

**Bagi manajer, implikasi langsungnya adalah: pilihan strategi yang tepat adalah syarat perlu tetapi tidak cukup.** Investasi pada arsitektur pengukuran kinerja yang diselaraskan dengan strategi adalah komplemen yang krusial. Untuk *cost leader*, ini berarti penekanan pada metrik biaya per unit, *operational efficiency ratio*, dan margin operasional. Untuk *differentiator*, ini berarti metrik yang menangkap *brand strength*, *customer satisfaction*, *innovation pipeline*, di samping ukuran finansial standar. **Temuan kontroversial bahwa financial measures tetap dominan sebagai mediator (bahkan untuk *differentiator*) menyatakan bahwa "*Balanced Scorecard*" tidak boleh diinterpretasikan sebagai pelarian dari finansial; ia adalah pelengkap, bukan substitusi.**

### Implikasi untuk Konteks Indonesia

Konteks Indonesia memiliki kemiripan struktural dengan Thailand: pasar berkembang Asia Tenggara, kombinasi BUMN dan swasta tercatat, liberalisasi perdagangan yang membuka kompetisi internasional. Beberapa kasus Indonesia yang relevan:

**Bank Mandiri** menjalani transformasi pasca-rekapitalisasi 2005–2010 dengan implementasi *Balanced Scorecard* yang ekstensif untuk menyatukan empat bank legacy yang dimerger. Dokumentasi publik (laporan tahunan dan kasus yang dipublikasikan) menunjukkan penurunan NPL dari ~25 persen menjadi ~2 persen disertai peningkatan ROE substansial. Apakah ini bukti mediasi PMS? Konsisten dengan klaim Teeratansirikool, tetapi tidak konklusif karena banyak inisiatif lain berlangsung paralel.

**Pertamina** mengalami transformasi KPI cascade pasca-reformasi sektor energi. Sistem KPI yang lebih transparan dan diturunkan ke level direktorat memungkinkan kalibrasi strategi yang lebih responsif. Namun keterbatasan struktural — dominasi *political objectives*, intervensi pemegang saham pemerintah, distorsi insentif yang berasal dari posisi BUMN — menambah kompleksitas yang model Thailand tidak tangkap.

**Telkom Indonesia** secara konsisten melaporkan implementasi *Balanced Scorecard* sebagai bagian dari sistem manajemen strategiknya. Status BUMN-nya membuat metrik politis (kontribusi terhadap target *Nawacita*, target dividen ke negara, kewajiban *universal service*) bercampur dengan metrik komersial murni. **Pertanyaan menarik untuk riset Indonesia: apakah *political KPI distortion* yang khas BUMN memutus rantai mediasi PMS–kinerja, atau justru menciptakan rantai mediasi yang berbeda di mana metrik politis berfungsi sebagai legitimacy capital yang pada gilirannya mempengaruhi kinerja?** Pertanyaan ini tidak dapat dijawab dengan instrumen Teeratansirikool yang dirancang untuk perusahaan tercatat swasta.

---

## 9. Isu untuk Diskusi Lebih Lanjut

### Pertanyaan Terbuka

Beberapa pertanyaan terbuka yang tersisa setelah membaca artikel ini patut dikembangkan dalam riset masa depan.

**Pertama, apakah PMS adalah mediator atau moderator?** Mediasi dan moderasi memiliki implikasi teoretis yang berbeda. Mediasi mengatakan PMS adalah jalur kausal antara strategi dan kinerja. Moderasi mengatakan PMS memperkuat atau memperlemah hubungan strategi–kinerja, bukan menjadi jalur. Onditi (2018) yang akan dibahas dalam *Critical Review* berikutnya secara eksplisit memperlakukan *firm characteristics* sebagai moderator. Pemilihan kerangka mediator vs. moderator harus didorong oleh teori, bukan kemudahan estimasi.

**Kedua, apakah temuan bertahan untuk UKM?** Sampel Teeratansirikool adalah perusahaan tercatat yang relatif besar dengan PMS yang sudah formal. UKM yang mendominasi struktur ekonomi Indonesia dan banyak negara berkembang lainnya mungkin tidak memiliki PMS formal. Apakah strategi tetap menghasilkan kinerja melalui PMS informal (intuisi pemilik, *gut feel*, observasi langsung), atau hubungan ini terputus untuk segmen UKM?

**Ketiga, bagaimana digitalisasi mengubah PMS?** Sistem OKR (*Objectives and Key Results*) berbasis *real-time dashboard* yang sekarang umum di perusahaan teknologi Indonesia (Gojek, Tokopedia, Bukalapak) sangat berbeda dari *Balanced Scorecard* tradisional yang menjadi rujukan Teeratansirikool. Apakah PMS digital memperkuat atau mengubah struktur mediasi yang ditemukan?

### Relevansi untuk Riset Masa Depan

**Keempat, masalah BUMN Indonesia.** Dalam konteks BUMN Indonesia, KPI yang ditetapkan oleh Kementerian BUMN sering bercampur antara target komersial dan target politis. Apakah ini memutus rantai PMS–kinerja yang ditemukan Teeratansirikool, atau justru menciptakan rantai mediasi yang berbeda? Riset eksplorasi pada BUMN energi (Pertamina, PLN), telekomunikasi (Telkom), dan infrastruktur (Wijaya Karya, Waskita) dengan disain longitudinal akan sangat berharga.

**Kelima, untuk audiens Magister Akuntansi**: pertanyaan profesi yang relevan adalah apakah akuntan manajemen yang merancang PMS memiliki insentif yang selaras dengan *strategic intent* perusahaan, atau didorong oleh tekanan compliance dan pelaporan eksternal. Bila yang terakhir, PMS yang terdokumentasi mungkin kurang berfungsi sebagai *strategic feedback loop* dan lebih berfungsi sebagai *legitimacy artifact*. Penelitian *behavioral accounting* di konteks Indonesia dapat mengisi celah ini.
"""


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT 3 — CRITICAL REVIEW ARTIKEL 10
# ══════════════════════════════════════════════════════════════════════════════
CR10 = r"""# CRITICAL REVIEW — ARTIKEL 10

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Identitas Artikel

**Penulis:** E. O. Onditi

**Tahun:** 2018

**Judul:** *Competitive Strategies and Firm Performance: A Review of Literature*

**Jurnal:** *The Strategic Journal of Business & Change Management*, Vol. 5, Issue 4, pp. 1869–1879

**ISSN:** 2312-9492 (Online), 2414-8970 (Print)

**Tanggal Diterima:** 18 Oktober 2018

**Institusi Penulis:** Lecturer in Marketing, Jaffery Institute of Professional Studies (JIPS), Mombasa, Kenya

**Tipe Riset:** *Conceptual paper* berbentuk *literature review* naratif. Tidak ada data empiris primer. Tidak ada teknik meta-analisis kuantitatif. Penulis menyusun mapping literatur, mengidentifikasi *knowledge gap*, dan mengusulkan model konseptual dengan dua hipotesis konseptual (tanpa diuji secara empiris dalam paper ini).

**Konteks Publikasi:** *Strategic Journals* adalah jurnal *open access* yang berbasis di Afrika Timur, dengan fokus pada manajemen, perubahan organisasi, dan kewirausahaan. Banyak studi yang dirujuk Onditi berasal dari konteks Kenya dan Afrika sub-Sahara, walaupun ia juga mengintegrasikan studi dari Spanyol (Spanos et al. 2004; Pertusa-Ortega et al. 2009), Yunani (Spanos), Turki (Cahit et al. 2017; Yasar 2010; Parnel & Koseoglu 2009/2010), Malaysia (Abidin et al. 2014), Nigeria (Oyedijo 2012), Argentina, Peru, dan Amerika Serikat (Parnell 2011), dan Australia.

---

## 2. Tujuan dan Posisi dalam Literatur

### Pertanyaan Riset

Tujuan eksplisit yang dirumuskan adalah untuk "*evaluate competitive strategies and firm performance through a review of existing literature*" (Onditi 2018, p. 1869, abstract). Pertanyaan riset turunan yang dapat ditarik dari struktur paper adalah: (1) kerangka teoretis apa yang mendasari hubungan strategi kompetitif dan kinerja perusahaan; (2) apa konsensus dan ketidaksepakatan yang ada dalam literatur empiris tentang efektivitas strategi generik; (3) variabel kontekstual apa yang memoderasi hubungan tersebut; dan (4) gap apa yang masih terbuka untuk riset masa depan.

### Posisi Relatif terhadap Review Sebelumnya

Onditi tidak secara eksplisit menempatkan paper ini sebagai update terhadap meta-analisis Campbell-Hunt (2000), tetapi ada beberapa rujukan implisit. Dia menyebut bahwa Porter's generic strategies "*have been linked to superior performance by Campbell – Hunt (2000)*" (p. 1872) dan kemudian membahas studi-studi post-2000 — Powers dan Hahn (2004), Allen dan Helms (2006), Pertusa-Ortega et al. (2009), Parnell (2010, 2011), Mwangi dan Ombui (2013), Kinyuira (2014), Cahit et al. (2017) — yang tidak dapat dimasukkan dalam meta-analisis 2000. **Nilai inkremental review 2018 ini adalah cakupan empiris yang lebih luas baik secara temporal maupun geografis.**

Yang membedakan Onditi dari review sebelumnya adalah dua hal. **Pertama, integrasi tiga perspektif teoretis** sebagai *theoretical perspectives* — *Resource-Based View* (RBV, Wernerfelt 1984; Barney 1991), *Capability-Based View* (KBV, Amit dan Shoemaker 1993; Teece et al. 1997), dan *Market-Based View* (MBV, Porter 1985 dengan *five forces*). **Kedua, menambahkan model *value disciplines* Treacy dan Wiersema (1993)** sebagai alternatif terhadap typology Porter — *operational excellence*, *product leadership*, *customer intimacy*. Kombinasi ini memberi gambaran yang lebih kaya daripada review yang hanya berkisar pada Porter (1980, 1985).

---

## 3. Argumen Utama

### Tema 1: Strategi Generik vs. Kinerja

**Tema pertama yang Onditi sintesis adalah bahwa strategi generik Porter secara umum memiliki efek positif pada kinerja perusahaan, tetapi efektivitas spesifik tipe strategi sangat bervariasi.** Tabel 1 paper (p. 1875) merangkum studi yang menemukan hubungan positif vs. studi yang tidak menemukan hubungan: untuk cost leadership, lima studi positif (Yamin et al. 1999, Allen dan Helms 2006, Parnell 2010, Teerantasirikool et al. 2013) versus dua negatif (Yasar 2010, Akbolat dan Isik 2012); untuk differentiation, dua positif (Parnell 2011, Teerantasirikool et al. 2013) versus dua negatif (Allen dan Helms 2006, Yosar 2010); untuk focus, dua positif (Parnell dan Koseoglu 2009, Parnell 2011) versus tiga negatif. **Tampilan tabular ini berguna sebagai *bird's-eye view* literatur, tetapi inkonsistensi temuan ini diakui Onditi sendiri sebagai sumber masalah**: "*the studies had also yielded inconsistent results on the generic strategies – firm performance relationship*" (p. 1875).

### Tema 2: Konteks Industri dan Karakteristik Perusahaan sebagai Moderator

Tema kedua adalah pengakuan bahwa hubungan strategi–kinerja sangat dimoderasi oleh konteks. Onditi mengutip studi-studi yang menemukan industry-specific findings: di sektor perbankan (Powers dan Hahn 2004), *focus strategy* mengungguli *stuck in the middle*; di sektor *quantity surveying* Malaysia (Abidin et al. 2014), differentiation lebih dipilih untuk perusahaan besar dan menghasilkan peningkatan jumlah proyek; di sektor mobile telecommunications Kenya (Arasa dan Gathinji 2014), *market focus* memberikan kontribusi terbesar; di SACCO Kenya (Kinyuira 2014), cost leadership yang dominan. Onditi mengusulkan **firm characteristics sebagai moderating variable**, dengan model konseptual yang divisualkan dalam Figure 2 (p. 1875): tiga strategi → kinerja, dimoderasi oleh firm characteristics. Dua hipotesis konseptual diajukan: H1 strategi mempengaruhi kinerja secara signifikan; H2 firm characteristics memoderasi hubungan tersebut secara signifikan. **Hipotesis ini bersifat konseptual; paper tidak mengujinya secara empiris.**

### Tema 3: Hybrid Strategies sebagai Pertanyaan Belum Selesai

Tema ketiga yang Onditi soroti adalah perdebatan tentang *hybrid strategies*. Porter (1985) mempertahankan bahwa perusahaan harus memilih satu strategi karena mengejar dua dapat berakhir di *stuck in the middle*. Tetapi studi yang lebih baru — Spanos et al. (2004) di Yunani; Pertusa-Ortega et al. (2009) di Spanyol; Oyedijo (2012) di Nigeria; Kim et al. (2004); Miller dan Dess (1993) — secara konsisten menemukan bahwa strategi hybrid yang menggabungkan elemen cost dan differentiation dapat lebih unggul daripada strategi pure. Onditi menyimpulkan: "*Hybrid strategies are the ones which combine low cost and differentiation elements and they have been shown to be viable and profitable*" (p. 1873). **Tetapi penyelesaian teoretis terhadap kontestasi Porter vs. hybrid tidak diberikan**; paper hanya melaporkan kedua sisi tanpa kerangka untuk menentukan kondisi mana yang membenarkan masing-masing posisi.

---

## 4. Koneksi ke Topik Silabus

### Validasi terhadap TPGS Ch.6

Onditi memberikan dukungan sintetik terhadap argumen TPGS Ch.6 bahwa pilihan strategi adalah keputusan struktural yang mempengaruhi kinerja. Pengakuan bahwa "*the generic strategies have been used extensively by various authors with different results*" (p. 1876) sejalan dengan diskusi RMK §8 tentang konsensus dan debat dalam literatur strategi. **Yang Onditi tambahkan dibandingkan TPGS adalah pengingat bahwa Porter bukan satu-satunya kerangka — RBV, KBV, MBV, dan *value disciplines* Treacy-Wiersema adalah alternatif yang valid dan relevan.**

### Jembatan ke Teeratansirikool (Artikel 9)

Onditi merujuk Teeratansirikool et al. (2013) sebagai salah satu studi yang menemukan hubungan positif baik untuk cost leadership maupun differentiation dengan kinerja (p. 1875, Tabel 1). **Ini adalah verifikasi independen dari Critical Review Artikel 9: temuan Teeratansirikool diintegrasikan ke dalam mapping literatur yang lebih luas dan diakui sebagai kontribusi yang sah.** Apa yang tidak diintegrasikan oleh Onditi adalah dimensi mediasi melalui PMS yang menjadi inti kontribusi Teeratansirikool. Onditi memperlakukan Teeratansirikool sebagai studi yang menunjukkan hubungan langsung strategi–kinerja, melewatkan argumen *mechanism* yang merupakan kontribusi orisinal artikel tersebut. **Ini adalah salah satu bukti bahwa kualitas sintesis Onditi cenderung deskriptif daripada analitis.**

---

## 5. Kekuatan Artikel

### Cakupan Literatur Post-2000 dan Lintas Geografi

Cakupan literatur Onditi cukup luas baik secara temporal — dari Porter (1980) hingga Cahit et al. (2017) — maupun secara geografis. Walaupun studi-studi di Kenya dominan, Onditi juga mengintegrasikan riset dari Spanyol, Yunani, Turki, Malaysia, Nigeria, Argentina, Peru, AS, dan Australia. **Ini memberi gambaran yang lebih global tentang penerapan strategi generik daripada review yang fokus pada satu wilayah geografis.**

### Aksesibilitas untuk Praktisi dan Mahasiswa

Onditi menulis dengan gaya naratif yang lugas, tanpa notasi statistik yang berat atau jargon teoretis yang ekslusif. **Untuk audiens mahasiswa pascasarjana yang baru masuk ke literatur strategi, paper ini berfungsi sebagai *entry point* yang baik**: ia menyajikan tiga perspektif teoretis (RBV, KBV, MBV) dengan ringkas, memetakan studi empiris dengan jelas, dan mengidentifikasi gap untuk riset lanjut. Aksesibilitas ini patut dihargai dalam ekosistem akademik di mana sebagian besar review level-tertinggi dipublikasikan dalam jurnal Anglo-Saxon yang berbiaya akses tinggi.

### Identifikasi Gap yang Berguna

**Onditi mengidentifikasi tiga gap riset yang berguna untuk agenda masa depan**: pertama, kebutuhan studi tentang efek strategi hybrid (yang ia sebut secara eksplisit di rekomendasi); kedua, peran karakteristik perusahaan sebagai moderator yang belum cukup dipelajari; ketiga, perlunya menguji *value discipline model* Treacy dan Wiersema sebagai alternatif framework, mengingat banyak penulis lebih memilih taksonomi Porter. Identifikasi ketiga gap ini relevan dan berpotensi menjadi pertanyaan riset Magister untuk konteks Indonesia.

---

## 6. Keterbatasan dan Kelemahan

### Kualitas Sintesis: Deskriptif vs. Analitis

**Kelemahan paling fundamental dari paper ini adalah bahwa *organizing framework*-nya bersifat deskriptif, bukan analitis.** Tiga tema yang menjadi struktur utama (strategi vs. kinerja; konteks sebagai moderator; hybrid strategies) bukanlah struktur analitis yang menjelaskan *mengapa* literatur menghasilkan temuan yang berbeda. Mereka adalah kategori untuk mengorganisasi laporan tentang *apa* yang ditemukan studi-studi tersebut. **Paper yang memetakan literatur tanpa kerangka untuk mengadjudikasi kontradiksi adalah peta jalan, bukan sintesis teoretis.** Bandingkan dengan Campbell-Hunt (2000) yang dengan meta-analisis kuantitatif memberikan effect-size estimasi yang dapat diuji statistik dan dibandingkan antarstudi.

### Basis Empiris Berat di Kenya/Afrika Timur

Walaupun Onditi mengintegrasikan studi dari banyak negara, **basis empiris yang paling sering dirujuk adalah konteks Kenya** (Mwangi dan Ombui 2013; Arasa dan Gathinji 2014; Kinyuira 2014; sebagian besar dataset di Tabel 1 berasal dari studi Kenya). Ini adalah refleksi alami dari afiliasi institusional penulis (JIPS, Mombasa, Kenya) dan jangkauan jurnal *Strategic Journals* yang Afrika-sentris. **Konsekuensinya adalah keterbatasan generalisasi**: Kenya dan negara-negara Afrika sub-Sahara memiliki struktur institusional yang berbeda dari ASEAN dan Asia Timur — *institutional voids* (Khanna dan Palepu 2000) yang berbeda, kedalaman pasar modal yang berbeda, struktur kepemilikan keluarga vs. tercatat yang berbeda. Onditi tidak melibatkan literatur *institutional economics* secara substantif, sehingga riset di konteks dengan struktur institusional yang berbeda (termasuk Indonesia) mungkin tidak terlayani sepenuhnya oleh sintesis ini.

### *Moderating Variables* yang Tertinggal

Onditi mengusulkan firm characteristics sebagai moderator, tetapi tidak mengelaborasi karakteristik mana yang penting. **Literatur strategi telah lama mengakui beberapa moderator yang spesifik: industry clock-speed (Fine 1998), firm age dan ukuran, struktur kepemilikan (state vs. private vs. family), dan kondisi institusional (Khanna dan Palepu 2000).** Tidak satu pun dari moderator ini diintegrasikan secara substantif. Hipotesis konseptual H2 yang menyatakan firm characteristics memoderasi hubungan strategi–kinerja terlalu agregat untuk diuji secara meaningful — apakah yang dimaksud "firm characteristics" adalah age, size, ownership, atau kombinasi dari ketiganya?

### Tidak Ada Meta-Analisis Kuantitatif dan Tidak Ada Engagement dengan Masalah *Measurement Artifact*

**Review naratif tanpa sintesis effect-size memiliki keterbatasan inheren.** Ia mengakui bahwa "*the empirical studies showed inconsistencies in the research findings*" (p. 1869, abstract) tetapi tidak menawarkan teknik untuk menyintesis inkonsistensi tersebut secara kuantitatif. Sebagai contoh, ia tidak dapat menjawab pertanyaan: rata-rata, seberapa kuat efek cost leadership pada kinerja? Apakah inkonsistensi temuan disebabkan oleh perbedaan ukuran sampel atau perbedaan substantif dalam konteks?

Lebih lanjut, **Onditi tidak mengangkat masalah *measurement artifact* yang penting dalam literatur strategi**: instrumen *self-report* untuk mengklasifikasikan strategi (Kotha dan Vadlamani 1995, walaupun rujukan ini tidak muncul di Onditi) memiliki validitas yang dipertanyakan. Bila instrumen tidak valid, hasil yang konsisten maupun yang konflik sama-sama dipertanyakan. Onditi tidak mengangkat masalah ini, sehingga sintesis literatur yang dilakukannya berasumsi pada validitas instrumen yang belum sepenuhnya terbukti.

---

## 7. Evaluasi Kritis

### Apakah Onditi Menyelesaikan Kontestasi atau Sekadar Melaporkannya?

**Inilah pertanyaan kritis paling penting tentang paper review.** Setelah membaca artikel sepenuhnya, jawabannya jelas: Onditi melaporkan kontestasi tetapi tidak menyelesaikannya. Ia mendokumentasi bahwa Allen dan Helms (2006) menemukan focused cost leadership terbaik, sementara Arasa dan Gathinji (2014) menemukan market focus terbaik. Ia mendokumentasi bahwa Mwangi dan Ombui (2013) menemukan cost leadership memiliki efek terbesar di rumah sakit misi Kenya, sementara differentiation memiliki efek paling kecil. **Tetapi tidak ada penjelasan teoretis tentang mengapa hasil-hasil ini berbeda.** Apakah karena perbedaan industri (perbankan vs. telekomunikasi vs. rumah sakit)? Apakah karena perbedaan ukuran perusahaan? Apakah karena perbedaan struktur kompetisi?

**Paper review yang tidak menjawab "mengapa" hanya memberikan setengah kontribusi.** Setengah lainnya — sintesis teoretis yang menjelaskan kondisi di mana setiap strategi unggul — adalah pekerjaan yang ditunda untuk riset masa depan. Sebagai *literature map*, paper ini berguna; sebagai *theoretical synthesis*, ia kurang.

### Perbandingan dengan Campbell-Hunt (2000)

**Perbandingan dengan Campbell-Hunt (2000) menyingkapkan kelemahan struktural paper Onditi.** Campbell-Hunt yang mensintesis 17 studi dengan teknik meta-analitik kuantitatif menghasilkan dua kontribusi yang Onditi tidak berikan: (1) effect-size estimasi yang dapat diuji statistik, dan (2) klasifikasi *moderator variables* yang sistematis. Onditi mencakup studi yang lebih banyak dan lebih baru, tetapi dengan teknik yang kurang ketat. **Net penilaian: paper Onditi berfungsi sebagai pelengkap (cakupan terbaru) bukan pengganti Campbell-Hunt; pembaca yang serius perlu membaca keduanya.**

### Masalah *Measurement Artifact*

Sebagian besar studi yang Onditi rujuk menggunakan instrumen *self-report* untuk mengklasifikasikan strategi perusahaan. Reliabilitas dan validitas instrumen ini bervariasi — sebagaimana terlihat di Critical Review Artikel 9 di mana Cronbach's α untuk cost leadership hanya 0,54. **Bila inkonsistensi temuan empiris sebagian disebabkan oleh ketidakkonsistenan instrumen, sintesis literatur yang tidak mengoreksi *measurement artifact* akan terus melaporkan ketidaksepakatan yang sebagian artifak metodologis.** Onditi tidak menangani masalah ini, dan ini adalah celah serius dalam *quality assurance* sintesis literaturnya.

### Penilaian Kontribusi Orisinal

**Penilaian akhir saya: kontribusi Onditi adalah sebagai *literature map* yang berguna bagi audiens praktisi dan mahasiswa, bukan sebagai sintesis teoretis yang memajukan disiplin secara substansial.** Kekuatannya adalah cakupan dan aksesibilitas; kelemahannya adalah kedalaman analitis. Untuk audiens akademik strategi senior, paper ini akan dipersepsikan sebagai *survey* yang patut dibaca dengan kesadaran keterbatasannya, bukan sebagai *seminal contribution*. Untuk audiens mahasiswa pascasarjana yang baru memasuki literatur, paper ini berfungsi sebagai *entry point* yang lebih kontemporer daripada Campbell-Hunt (2000) tetapi harus dibaca bersama dengan meta-analisis tersebut, bukan sebagai pengganti.

---

## 8. Implikasi

### Implikasi Teoretis

**Implikasi teoretis utama yang dapat ditarik adalah bahwa literatur strategi–kinerja telah mengakumulasi banyak data tetapi mengakumulasi insight terbatas, karena variabel moderator masih *underspecified*.** Bila riset masa depan ingin memajukan disiplin, fokus seharusnya bergerak dari pertanyaan "strategi mana yang lebih baik" ke pertanyaan "dalam kondisi mana strategi tertentu lebih baik". Onditi mengisyaratkan ini dengan mengusulkan firm characteristics sebagai moderator, tetapi belum mengelaborasi mana karakteristik yang penting. **Riset masa depan perlu spesifik: apakah industry clock-speed, firm size, ownership structure, ataukah institutional environment yang menjadi moderator paling penting?**

### Implikasi untuk Riset Indonesia

Untuk konteks riset Indonesia, paper Onditi memberi beberapa implikasi yang relevan. **Pertama, riset empiris longitudinal tentang strategi kompetitif → kinerja perusahaan Indonesia masih jarang.** Mayoritas studi Indonesia yang dipublikasikan adalah *cross-sectional case study* dengan disain yang kurang ketat. Ada celah untuk riset Magister/Doktor yang menggunakan data panel BEI dengan instrumen strategi yang divalidasi. Kedua, *value discipline* Treacy-Wiersema yang Onditi rekomendasikan untuk diuji belum cukup digunakan dalam riset Indonesia; ada celah untuk riset komparatif yang menggunakan kerangka ini sebagai alternatif Porter.

### Komparasi Rekam Jejak Empiris Indonesia dengan Prediksi Literatur

Beberapa kasus Indonesia yang dapat dipetakan ke prediksi literatur:

**Astra International** adalah konglomerat terdiversifikasi dengan portofolio otomotif, alat berat, agribisnis, dan jasa keuangan. **Tipe strategi Astra tidak mudah diklasifikasi dalam taksonomi Porter** — ia bukan cost leader murni karena beroperasi di banyak segmen premium, bukan differentiator murni karena efisiensi operasional adalah inti kompetisi otomotifnya, dan bukan focused karena cakupan industri sangat luas. Astra mungkin lebih cocok dipetakan ke *value disciplines* Treacy-Wiersema dengan *operational excellence* sebagai disiplin dominan (terutama di unit otomotif, tracking volume produksi dan margin tipis). **Kasus ini memvalidasi kritik Onditi bahwa Porter typology mungkin kurang fit untuk konglomerat Asia.**

**BCA** adalah differentiator yang konsisten outperform di retail banking Indonesia melalui kualitas layanan, infrastruktur digital, dan brand trust. Ini konsisten dengan tema 1 Onditi (differentiation menghasilkan kinerja superior dalam kondisi tertentu).

**Indofood** dengan portofolio mi instan dan consumer staples adalah cost leader klasik dengan skala manufaktur yang substansial dan rantai distribusi yang masif. Dominasi pasar mi instan domestik konsisten dengan prediksi cost leadership.

**Telkom Indonesia** sebagai BUMN telekomunikasi menghadapi tujuan komersial dan politik secara bersamaan. Kewajiban *universal service obligation* dan target dividen ke negara membuat pilihan strategi tidak murni komersial. **Kasus ini menggambarkan kompleksitas yang Onditi singgung tetapi tidak elaborasi: ownership structure sebagai moderator yang signifikan untuk konteks pasar berkembang dengan dominasi BUMN.**

---

## 9. Isu untuk Diskusi Lebih Lanjut

### Gap yang Paling Mendesak

Beberapa gap yang paling mendesak setelah membaca Onditi (2018):

**Pertama, dampak digitalisasi pada hubungan strategi–kinerja.** Onditi 2018 hampir tidak menyentuh ekonomi digital. Bagaimana kemunculan platform, *network effects*, dan *winner-takes-most* di pasar digital mengubah taksonomi Porter? Apakah cost leadership tetap relevan ketika *marginal cost* mendekati nol di banyak produk digital? Apakah differentiation di kategori *attention economy* berbeda strukturnya dari differentiation produk fisik? Riset post-2018 sudah mulai menjawab pertanyaan ini, dan review yang lebih baru perlu mengintegrasikannya.

**Kedua, *institutional voids* sebagai konteks strategi yang berbeda.** Khanna dan Palepu (2000) menunjukkan bahwa pasar berkembang sering mengalami *institutional voids* — kelemahan dalam pasar modal, tenaga kerja, regulasi — yang membuat konglomerat keluarga muncul sebagai bentuk organisasi yang efisien. Indonesia kaya dengan konglomerat seperti ini (Salim, Lippo, Sinar Mas, Astra). **Apakah taksonomi Porter cocok untuk perusahaan yang struktur ekonomis primernya adalah *related diversification* yang dibenarkan oleh *institutional voids*?** Onditi tidak menjawab; ini adalah agenda riset Indonesia yang substantif.

### Pertanyaan untuk Riset Mendatang

**Ketiga, Porter typology vs. Miles-Snow vs. Treacy-Wiersema: mana yang paling valid untuk konteks Indonesia?** Riset komparatif yang menerapkan ketiga taksonomi pada sampel perusahaan tercatat BEI dan membandingkan validitas konstruk akan sangat berharga. Ini adalah pertanyaan empiris yang dapat diuji dan menjadi dasar tesis Magister yang kuat.

**Keempat, microfoundations yang menerjemahkan strategi menjadi kinerja.** Teece (2007) dengan kerangka *dynamic capabilities* — sensing, seizing, transforming — menyediakan microfoundations yang tidak dimiliki framework Porter. Bagaimana rutinitas organisasi dan keputusan individu menerjemahkan strategi tipe X menjadi kinerja Y? Onditi mengakui gap ini secara implisit ketika menyebut bahwa "execution quality" adalah variabel underappreciated, tetapi tidak elaborasi. Ini adalah agenda riset yang menjembatani strategi makro dan operasional.

**Kelima, untuk audiens Magister Akuntansi**: bagaimana fungsi akuntansi manajemen dan internal control dapat menjadi instrumen empiris untuk mengukur strategi perusahaan? Bila *self-report* memiliki masalah validitas, apakah data akuntansi (struktur biaya, pola investasi R&D, *capex* per segmen) dapat menjadi proksi yang lebih objektif untuk strategi perusahaan? Riset *empirical accounting* di konteks Indonesia dapat mengisi celah validitas instrumen yang Onditi sendiri tidak angkat secara substantif.
"""


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    OUT_RMK.mkdir(parents=True, exist_ok=True)
    OUT_CR.mkdir(parents=True, exist_ok=True)

    if not REFERENCE.exists():
        print(f"ERROR: reference.docx not found at {REFERENCE}")
        print("Run generate_submission.py first to create it.")
        sys.exit(1)

    pandoc(
        write_md(RMK, "rmk_pert6.md"),
        OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx",
    )
    pandoc(
        write_md(CR9, "artikel9.md"),
        OUT_CR / "01079_Dzaki Muhammad Yusfian_Artikel 9.docx",
    )
    pandoc(
        write_md(CR10, "artikel10.md"),
        OUT_CR / "01079_Dzaki Muhammad Yusfian_Artikel 10.docx",
    )

    print("\nAll three documents generated successfully.")
    print(f"RMK : {OUT_RMK}")
    print(f"CR  : {OUT_CR}")


if __name__ == "__main__":
    main()
