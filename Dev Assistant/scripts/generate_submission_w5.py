#!/usr/bin/env python3
"""
generate_submission_w5.py
Generates three Word documents for MST304 Pertemuan 5 submission.
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
# DOCUMENT 1 — RMK PERTEMUAN 5
# ══════════════════════════════════════════════════════════════════════════════
RMK = r"""# RINGKASAN MATERI KULIAH — PERTEMUAN 5

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Topik:** *The Five Generic Competitive Strategies* (TPGS Ch.5 + Henry Ch.5)

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Pendahuluan

Pertemuan 5 menjawab pertanyaan yang menjadi konsekuensi langsung dari analisis Pertemuan 3 dan Pertemuan 4. Pertemuan 3 memetakan struktur industri dan tekanan kompetitif yang membentuk lingkungan eksternal; Pertemuan 4 mengurai sumber daya dan kapabilitas yang dimiliki perusahaan secara internal melalui kerangka *resource-based view* (RBV). Pertanyaan yang menggantung dari kedua analisis itu adalah pertanyaan yang sentral bagi seluruh disiplin manajemen strategik: *bagaimana* perusahaan sebenarnya bersaing di dalam industri yang sudah dikenalnya, dan posisi kompetitif macam apa yang harus diambil agar sumber daya internalnya menghasilkan kinerja yang superior.

Pertanyaan inilah yang dijawab oleh kerangka *generic competitive strategies* yang dikembangkan Porter (1980, 1985) dan kemudian diperluas dalam tradisi TPGS menjadi lima posisi: *low-cost provider*, *broad differentiation*, *focused low-cost*, *focused differentiation*, dan *best-cost provider*. Di sisi lain, Henry (2021) menempatkan diskusi yang sama dalam konteks lima kekuatan industri dan analisis pesaing, sehingga pilihan posisi tidak terisolasi dari pemahaman struktur kompetisi yang lebih luas.

Pertemuan ini bukan sekadar latihan klasifikasi. Argumen sentralnya adalah bahwa pilihan strategi generik bukan keputusan administratif yang dapat dibalik dengan mudah; ia adalah komitmen organisasional yang membentuk arsitektur biaya, struktur diferensiasi, sistem insentif, dan budaya kerja perusahaan untuk jangka menengah. Konsekuensinya, keliru memilih atau menjalankan setengah hati pada pilihan tersebut tidak hanya menghasilkan kinerja biasa - biasa saja, melainkan dapat menempatkan perusahaan pada posisi *stuck in the middle* yang oleh Porter dijelaskan sebagai jebakan struktural.

Materi pertemuan ini juga menjadi jembatan menuju Pertemuan 6 (strategi tingkat korporat) dan Pertemuan 7 (strategi internasional). Pilihan posisi pada level *strategic business unit* (SBU) membatasi ruang gerak strategi tingkat korporat: portofolio bisnis yang dibangun di atas pilihan diferensiasi tidak dapat begitu saja ditangani dengan logika *cost leadership* di tingkat korporat tanpa konflik organisasional. Karena itu, pemahaman mendalam atas Pertemuan 5 menjadi prasyarat agar diskusi pertemuan berikutnya tidak dangkal.

## 2. Akar Konseptual: Porter sebagai Reaksi terhadap Paradigma SCP

Untuk memahami mengapa lima strategi generik dirumuskan dengan struktur tertentu, perlu ditempatkan asal usulnya dalam kerangka intelektual yang lebih besar. Porter (1980) menulis *Competitive Strategy* dalam konteks pemikiran *industrial organization economics* yang didominasi paradigma *Structure - Conduct - Performance* (SCP) warisan Mason - Bain. Paradigma SCP berargumen bahwa struktur industri (jumlah pesaing, hambatan masuk, diferensiasi produk) menentukan perilaku perusahaan (strategi penetapan harga, investasi R&D), yang pada gilirannya menentukan kinerjanya. Dalam logika ini, manajer adalah aktor pasif yang bereaksi terhadap struktur; analisis strategis hampir tereduksi menjadi diagnosis industri.

Kontribusi Porter adalah membalik logika tersebut. Ia tetap mengakui pentingnya struktur industri (yang ia formalkan sebagai *five forces*), tetapi ia memberi ruang yang besar bagi tindakan strategis perusahaan dalam membentuk posisinya di dalam struktur itu. Lima strategi generik adalah peta yang ia sodorkan untuk pilihan tindakan tersebut. Dengan demikian, Porter menempati posisi yang elegan secara intelektual: ia menggunakan kerangka *industrial organization* sebagai latar, tetapi memberi ruang agensi strategis kepada manajer yang sebelumnya tidak diakui dalam tradisi ekonomi industri murni.

Dua dimensi fundamental yang menstruktur kerangka Porter adalah cakupan pasar (*market scope*: luas atau sempit) dan sumber keunggulan (*source of competitive advantage*: biaya rendah atau diferensiasi). Salavou (2015, p. 82) menggambarkan kerangka ini dalam matriks dua kali dua yang menghasilkan empat sel klasik (cost leadership broad, differentiation broad, focus cost, focus differentiation), yang kemudian oleh TPGS diperluas dengan sel kelima yaitu *best-cost provider*. Kelima sel ini bukan sekadar kombinatorial; masing - masing memiliki logika ekonomis dan organisasional yang berbeda.

Penting dicatat bahwa pada tataran teoretis, Porter (1985) berargumen bahwa kelima posisi tersebut bersifat *mutually exclusive* di tingkat strategis: perusahaan harus memilih salah satu dan membangun seluruh konfigurasi sumber dayanya untuk mendukung pilihan itu. Argumen ini didasarkan pada keyakinan bahwa *cost leadership* dan *differentiation* menuntut konfigurasi yang bertentangan; mengejar keduanya secara simultan akan menghasilkan kompromi yang merusak keduanya. Kritik atas argumen ini, yang akan dibahas pada Bagian 4, justru menjadi pintu masuk bagi seluruh diskusi tentang strategi hybrid dan pergeseran ke kerangka *best-cost provider*.

## 3. Lima Strategi Generik: Logika Ekonomis dan Kondisi Keberhasilan

### 3.1 *Low-Cost Provider*

Strategi *low-cost provider* berusaha menghasilkan biaya per unit yang lebih rendah dari pesaing untuk produk yang dianggap setara oleh pelanggan. Logika ekonomisnya bekerja melalui dua jalur. *Pertama*, pada harga pasar yang sama, margin yang lebih besar memungkinkan investasi ulang yang memperkuat posisi biaya. *Kedua*, ketika kompetisi harga meningkat, perusahaan dengan biaya terendah dapat bertahan pada harga yang lebih rendah daripada yang dapat ditanggung pesaing. Ini menjadi pertahanan struktural yang kuat dalam industri *price - sensitive*.

Strategi ini bekerja paling baik ketika permintaan industri sensitif terhadap harga, produk relatif terstandar, biaya alih (*switching cost*) pelanggan rendah, dan skala produksi memberikan keuntungan biaya yang signifikan. Sumber keunggulan biaya berasal dari kombinasi: skala ekonomi, *learning curve*, kontrol biaya bahan baku, integrasi vertikal yang efisien, lokasi yang menguntungkan, dan teknologi proses yang lebih murah.

Kondisi kegagalan terjadi ketika: pesaing meniru struktur biaya yang sama; perubahan teknologi membuat investasi biaya yang ada menjadi *sunk cost*; pelanggan bergeser menuntut diferensiasi yang tidak dapat dipenuhi oleh pemimpin biaya. AirAsia di pasar penerbangan Asia Tenggara adalah contoh *low-cost provider* yang berhasil. Sebaliknya, Garuda Indonesia mengalami tekanan struktural justru karena mencoba mempertahankan posisi *full service* tanpa mampu menandingi struktur biaya pesaing *low-cost*.

### 3.2 *Broad Differentiation*

Strategi *broad differentiation* berusaha menyodorkan produk yang dipersepsikan unik oleh sebagian besar pelanggan dalam industri, sehingga mampu mengenakan harga premium. Logika ekonomisnya berbeda dari *cost leadership*: profitabilitas didorong oleh margin yang dihasilkan dari kemampuan harga, bukan oleh volume yang dihasilkan dari biaya rendah. Sumber diferensiasi dapat berasal dari kualitas produk, fitur inovatif, layanan pelanggan, citra merek, jaringan distribusi yang superior, atau kombinasi semua itu.

Strategi ini bekerja ketika preferensi pelanggan beragam dan tidak dapat dipuaskan oleh produk standar; ketika atribut diferensiasi sulit ditiru pesaing; dan ketika perusahaan memiliki kemampuan inovasi atau pemasaran yang kuat. Industri mobil mewah, kosmetik premium, dan jasa konsultasi profesional adalah contoh klasik di mana diferensiasi mendominasi sebagai strategi. Di sektor perbankan Indonesia, BCA dan Bank Mandiri menunjukkan dua pendekatan *broad differentiation* yang berbeda: BCA membangun diferensiasi melalui kualitas layanan, kecepatan transaksi, dan keandalan platform digital yang menjadi *gold standard* nasabah ritel kelas menengah atas; sementara Mandiri membangun diferensiasi melalui jangkauan jaringan dan integrasi layanan korporasi - ritel yang ekstensif. Kedua bank tetap mengenakan harga premium relatif terhadap pesaing meskipun keduanya bersaing dengan strategi yang berbeda dalam menghasilkan persepsi nilai pada basis pelanggan yang luas.

Risiko utama adalah *imitasi diferensiasi* yang menggerus nilai premium, dan *over - differentiation* yaitu menambahkan atribut yang tidak dihargai pelanggan tetapi menambah biaya. Risiko kedua sering terjadi pada perusahaan yang terlalu fokus pada *engineering* internal dan kehilangan kontak dengan persepsi pelanggan.

### 3.3 *Focused Low-Cost*

Strategi *focused low-cost* mengejar keunggulan biaya pada segmen pasar yang sempit. Berbeda dari *low-cost provider* yang melayani pasar luas, *focused low-cost* memilih segmen tertentu (geografis, demografis, atau atas dasar kebutuhan spesifik) dan membangun struktur biaya yang dioptimalkan untuk segmen itu. Logika ekonomisnya adalah bahwa efisiensi yang dirancang untuk segmen sempit dapat melampaui efisiensi pemain pasar luas yang harus mengakomodasi heterogenitas permintaan.

Strategi ini berhasil ketika segmen yang dipilih memiliki kebutuhan yang berbeda dari pasar luas dan ketika pesaing yang lebih besar tidak menemukan ekonomis untuk masuk ke segmen itu. AirAsia pada awal kehadirannya (1999 - 2003) menerapkan *focused low-cost* pada rute - rute tertentu di Asia Tenggara sebelum kemudian melebar ke posisi *broad low-cost* di seluruh kawasan.

### 3.4 *Focused Differentiation*

Strategi *focused differentiation* menggabungkan diferensiasi dengan fokus segmen. Perusahaan menyodorkan produk yang dipersepsikan unik bagi segmen pelanggan yang spesifik, dengan harapan bahwa kebutuhan segmen itu cukup khas sehingga pemain pasar luas tidak dapat memenuhinya secara memadai. Industri makanan organik premium, produk *halal* spesialis, dan klinik kecantikan eksklusif adalah contoh - contoh dari strategi ini.

Keberhasilan bergantung pada kemampuan mengidentifikasi segmen yang underserved, kemampuan membangun atribut diferensiasi yang relevan secara mendalam dengan kebutuhan segmen itu, dan kemampuan melindungi segmen dari serangan pemain lebih besar. Risikonya adalah segmen menjadi terlalu sempit untuk mendukung skala ekonomi minimum, atau pemain besar masuk dengan menambahkan kapabilitas yang dibutuhkan segmen itu.

### 3.5 *Best-Cost Provider*

TPGS menambahkan posisi kelima yang tidak ada secara eksplisit dalam taksonomi Porter 1980: *best-cost provider*. Posisi ini adalah hybrid yang menyodorkan produk dengan atribut diferensiasi yang relevan pada harga yang lebih rendah daripada pemain *broad differentiation*. Logikanya bukan sekadar kompromi melainkan integrasi: perusahaan membangun efisiensi biaya pada aktivitas yang tidak dilihat pelanggan (logistik, prokuremen, proses produksi standar) sambil mengalokasikan sumber daya pada aktivitas yang dilihat pelanggan (kualitas produk inti, layanan, *touchpoint* tertentu).

Indomaret dan Alfamart di Indonesia adalah contoh paradigmatik *best-cost provider*. Keduanya membangun skala distribusi yang efisien (struktur biaya rendah) sekaligus menyodorkan kenyamanan lokasi, keseragaman pengalaman, dan jam operasional yang lebih baik dari warung tradisional (atribut diferensiasi yang relevan untuk konsumen urban). Hasilnya bukan sekadar memenangkan kompetisi melawan ritel modern lain; mereka menggantikan ekosistem warung tradisional dengan struktur ritel yang berbeda.

Eksistensi *best-cost provider* sebagai posisi yang sah secara strategis sebenarnya merupakan pengakuan implisit dari TPGS bahwa argumen *mutually exclusive* Porter klasik perlu direvisi. Pengakuan inilah yang menjadi titik tolak diskusi Salavou (2015) dan literatur strategi hybrid yang akan dibahas pada Bagian 5.

## 4. *Stuck in the Middle*: Argumen Porter dan Tantangan Empiris

Argumen *stuck in the middle* (Porter 1980, 1985) menyatakan bahwa perusahaan yang mencoba menjalankan *cost leadership* dan *differentiation* secara simultan akan gagal pada keduanya. Logikanya bertumpu pada klaim bahwa kedua strategi menuntut konfigurasi sumber daya, struktur organisasi, dan budaya yang bertentangan. *Cost leadership* membutuhkan kontrol biaya ketat, standar produk, sistem produksi yang efisien, dan budaya disiplin operasional. *Differentiation* membutuhkan investasi pada kualitas, inovasi, layanan, dan budaya yang menghargai eksperimen dan responsif terhadap pelanggan. Mengejar keduanya, dalam logika Porter, akan menghasilkan organisasi yang setengah hati pada keduanya.

Empat dekade penelitian empiris menyodorkan tantangan yang signifikan terhadap argumen tersebut. *Pertama*, Hill (1988) mengangkat kritik teoretis yang tajam: argumen bahwa biaya dan diferensiasi *mutually exclusive* mengabaikan kenyataan bahwa diferensiasi tertentu (misalnya kualitas yang lebih tinggi) dapat justru *menurunkan* biaya jangka panjang melalui pengurangan tingkat cacat produk, retensi pelanggan, dan pengurangan biaya garansi. Hill menunjukkan bahwa pada industri tertentu, terutama yang memiliki struktur biaya bersifat *learning - based*, biaya dan diferensiasi dapat saling memperkuat.

*Kedua*, Miller (1992) dalam *The Generic Strategy Trap* memberikan kritik yang lebih luas. Argumennya adalah bahwa pada lingkungan industri yang dinamis, spesialisasi pada satu strategi generik justru dapat menjadi *trap* karena perusahaan kehilangan fleksibilitas untuk merespons pergeseran preferensi pelanggan dan tekanan kompetitif. Miller menunjukkan bukti empiris bahwa perusahaan yang menggabungkan elemen dari beberapa strategi generik sering memiliki kinerja yang lebih baik daripada yang murni mengikuti satu strategi.

*Ketiga*, Campbell-Hunt (2000) menerbitkan meta - analisis 17 studi empiris atas kerangka Porter yang menjadi *landmark* dalam diskusi ini. Temuan utamanya adalah bahwa bukti empiris atas argumen *strategic purity* Porter tidak konsisten; sebagian besar studi justru menunjukkan bahwa kombinasi strategi (*hybrid*) sering menghasilkan kinerja yang lebih baik daripada strategi murni. Salavou (2015, p. 85) mengutip meta - analisis Campbell-Hunt sebagai titik balik dalam literatur strategi: setelah 2000, fokus penelitian bergeser dari menguji *purity* ke memetakan tipologi *hybrid*.

Pengakuan atas batas *stuck in the middle* tidak berarti argumen Porter sepenuhnya dibatalkan. Salavou (2015) mencatat bahwa *stuck in the middle* tetap merupakan kondisi nyata; bedanya, ia bukan konsekuensi otomatis dari mengejar kombinasi strategi, melainkan konsekuensi dari ketidakmampuan organisasi untuk membangun konfigurasi yang koheren bagi kombinasi yang dipilih. Dalam pembacaan ini, *stuck in the middle* menjadi simptom dari eksekusi yang gagal, bukan dari pilihan strategis yang salah.

## 5. Strategi Hybrid dan Dinamis: Respons terhadap Porter

Bagian ini menjadi jembatan substantif menuju Artikel 7 (Salavou 2015) yang akan diulas dalam *critical review* terpisah. Argumen sentral literatur pasca - Porter adalah bahwa lingkungan kompetisi modern menuntut respons yang lebih kompleks daripada pilihan biner antara *cost leadership* dan *differentiation*.

Treacy dan Wiersema (1995) menyodorkan tipologi paralel yang menjadi rujukan banyak praktisi: *value disciplines* yang terdiri dari *operational excellence*, *product leadership*, dan *customer intimacy*. Meskipun struktur dasarnya berbeda dari Porter, argumen Treacy dan Wiersema tetap menempatkan *fokus* sebagai prinsip strategis: perusahaan harus unggul pada salah satu disiplin dan memenuhi *threshold* minimum pada disiplin lainnya. Perdebatan tentang apakah Treacy dan Wiersema sebenarnya menambahkan dimensi baru atau hanya mereformulasi Porter menjadi tema yang penting; Salavou (2015) cenderung memperlakukannya sebagai paralel typologi, bukan kerangka yang sepenuhnya baru.

D'Aveni (1994) dalam *Hypercompetition* mengangkat argumen yang lebih radikal: pada industri yang turbulen, keunggulan bersaing yang bertahan menjadi mustahil. Perusahaan harus mengantisipasi bahwa setiap keunggulan akan terkikis dengan cepat melalui imitasi atau disrupsi, dan strategi yang efektif adalah membangun urutan keunggulan sementara secara berkelanjutan. McGrath (2013) memperluas argumen ini menjadi *transient advantage* yang berargumen bahwa siklus hidup strategi (*strategy lifecycle*) menjadi lebih pendek; perusahaan yang berhasil adalah yang membangun kapabilitas untuk *meluncurkan*, *memanen*, dan *meninggalkan* strategi secara bergiliran. Salavou (2015) tidak menyebut McGrath dalam bibliografinya, sebuah keterbatasan yang patut dicatat ketika argumennya tentang pergeseran *static - to - dynamic* dievaluasi.

Brandenburger dan Nalebuff (1996) menyumbang konsep *coopetition* yang menjadi penting di era platform: kompetisi dan kerjasama dapat berlangsung simultan antara aktor yang sama. Google dan Apple bersaing pada *mobile operating system* tetapi berkolaborasi pada standar web; Samsung adalah pemasok komponen iPhone sekaligus pesaing langsung Apple di pasar *smartphone*. Pertanyaan yang perlu didiskusikan adalah apakah *coopetition* bersifat menggantikan kerangka Porter atau hanya melengkapinya sebagai dimensi *complementor* yang sebenarnya sudah diantisipasi dalam *Five Forces* yang diperluas (Brandenburger dan Nalebuff sendiri menamakannya *Value Net*).

Konteks Indonesia menyodorkan ilustrasi yang relevan. Tokopedia dan Shopee secara berkala menggeser keseimbangan antara biaya dan diferensiasi di bawah tekanan platform: fase awal didominasi subsidi agresif yang mendekati logika *low-cost* untuk akuisisi pengguna, lalu bergeser ke fokus margin dengan penekanan pada diferensiasi fitur (*live commerce*, *social commerce*, *fulfillment* yang lebih cepat) ketika kompetisi modal semakin terbatas. Pergeseran semacam ini menunjukkan bahwa pada industri platform, posisi strategis bukanlah pilihan permanen; ia menjadi rangkaian konfigurasi *hybrid* yang berevolusi seiring tahap pendewasaan industri dan tekanan modal.

Implikasi praktis dari literatur ini bagi mahasiswa adalah tiga: *pertama*, kerangka lima strategi generik tetap berguna sebagai titik referensi awal, tetapi tidak boleh diperlakukan sebagai kotak yang harus dipilih satu lalu ditutup; *kedua*, eksekusi strategi hybrid menuntut konfigurasi organisasional yang lebih kompleks daripada eksekusi strategi murni, dan kegagalannya sering bukan pada pilihan melainkan pada disain organisasi; *ketiga*, di lingkungan turbulen, strategi yang dianut hari ini harus diasumsikan sebagai *baseline* yang akan bergeser, bukan posisi statis yang harus dipertahankan.

## 6. Pilihan Strategi dan Lima Kekuatan Industri

Pilihan strategi generik tidak terlepas dari struktur industri di mana perusahaan beroperasi. Henry (2021) menekankan bahwa kerangka *five forces* (Porter 1979) berfungsi sebagai diagnostik untuk mengevaluasi kapan tiap strategi generik bekerja dan kapan gagal. Bagian ini mensistematiskan interaksi tersebut.

*Low-cost provider* bekerja paling baik ketika kekuatan tawar pembeli tinggi (sehingga mereka responsif terhadap harga), produk industri relatif terstandar, dan kompetisi internal cenderung pada harga. Sebaliknya, strategi ini gagal ketika produk industri sulit distandarkan, *switching cost* pelanggan tinggi, dan basis pelanggan menghargai diferensiasi. Industri komoditas kelas - kelas seperti baja batang, semen, dan tepung terigu memberikan kondisi yang menguntungkan; industri jasa profesional dan barang mewah cenderung memberikan kondisi yang menyulitkan.

*Broad differentiation* bekerja paling baik ketika preferensi pelanggan beragam, persepsi kualitas dapat dikomunikasikan secara meyakinkan, dan biaya alih pelanggan moderat hingga tinggi. Strategi ini gagal ketika basis pelanggan menjadi homogen di sekitar harga, ketika atribut diferensiasi mudah ditiru, dan ketika *substitusi* dari industri lain menggerus daya tawar produk industri. Industri *fast - moving consumer goods* (FMCG) dengan loyalitas merek yang kuat menjadi ladang yang subur; industri *commodity SaaS* memberikan tantangan struktural pada strategi ini.

*Focused* (baik *low-cost* maupun *differentiation*) bekerja paling baik ketika segmen yang dipilih memiliki kebutuhan yang berbeda secara meaningful dari pasar luas, dan ketika pemain pasar luas tidak menemukan ekonomis untuk menyalibang segmen itu. Strategi ini gagal ketika perbedaan kebutuhan segmen menyusut, ketika pemain besar membangun kapabilitas untuk melayani segmen tanpa kompromi pada bisnis utamanya, atau ketika segmen menjadi terlalu kecil untuk mendukung skala minimum.

*Best-cost provider* bekerja paling baik ketika basis pelanggan menghargai kualitas tertentu tetapi tidak bersedia membayar premium penuh dari *broad differentiation*. Strategi ini paling rentan ditekan dari dua arah: pemain *low-cost* murni dapat menggerus dari sisi harga, sementara pemain *broad differentiation* dapat menggerus dari sisi nilai. Karena itu, eksekusi *best-cost provider* yang berhasil hampir selalu membutuhkan kombinasi skala (untuk efisiensi biaya) dengan kemampuan operasional yang kuat (untuk konsistensi atribut diferensiasi).

Dua kasus Indonesia memperjelas interaksi pilihan strategi dengan lima kekuatan industri. Gojek dan Grab membentuk duopoli *multi - sided platform* di mana pilihan strategi keduanya dibentuk oleh tekanan kompetisi internal yang ekstrem dan kekuatan tawar driver dan merchant yang signifikan; keduanya menggabungkan elemen *low-cost* (subsidi tarif untuk pengguna) dengan elemen diferensiasi (ekosistem layanan terintegrasi mulai dari transportasi, logistik, hingga finansial) sebagai respons atas struktur industri yang menuntut skala dan keragaman layanan secara bersamaan. Sementara itu, persaingan Indofood dengan Wings Group pada kategori mie instan dan kopi instan dibentuk oleh dua kekuatan struktural sekaligus: kekuatan tawar pembeli melalui *modern trade* (Indomaret, Alfamart, supermarket) yang menekan margin produsen, dan tekanan substitusi dari kategori *ready - to - eat* dan *ready - to - drink* yang berkembang. Kedua produsen menjawab tekanan ini dengan posisi yang berbeda dalam matriks Porter: Indofood memilih *broad differentiation* yang ditopang merek dan jaringan distribusi kuat, sementara Wings Group memilih posisi yang lebih dekat ke *best-cost provider* dengan harga lebih terjangkau pada kualitas yang setara.

Integrasi dengan analisis Pertemuan 3 ini mempertegas bahwa pilihan strategi generik bukan keputusan internal yang dapat diambil terlepas dari struktur industri. Mengabaikan struktur akan menghasilkan strategi yang secara internal koheren tetapi secara eksternal tidak fit dengan realitas kompetitif.

## 7. Analisis Pesaing sebagai Prasyarat Pilihan Strategis

Bagian ini menjadi jembatan menuju Artikel 8 (Adom, Nyarko & Som 2016) yang akan diulas terpisah. Argumen sentralnya adalah bahwa pilihan strategi generik mensyaratkan pemahaman yang akurat tentang pesaing - pesaing di dalam industri.

Porter (1980) Bab 3 *Competitive Strategy* menyodorkan kerangka empat sel untuk analisis pesaing: *future goals* (apa yang ingin dicapai pesaing dalam jangka menengah), *current strategy* (strategi yang sedang dijalankan), *assumptions* (asumsi pesaing tentang industri dan dirinya sendiri), dan *capabilities* (kapabilitas yang dimiliki pesaing). Empat sel ini bekerja sebagai diagnostik yang lengkap karena mengintegrasikan dimensi sekarang (*current strategy*, *capabilities*) dengan dimensi yang membentuk respons masa depan (*future goals*, *assumptions*).

Sel *assumptions* adalah yang paling sulit dipenuhi dan, ironisnya, paling bernilai. Sebagian besar manajer dapat mengumpulkan informasi tentang strategi yang sedang dijalankan pesaing (dari laporan tahunan, pengumuman, pemberitaan); sebagian dapat memetakan kapabilitas pesaing (dari analisis produk, pengamatan operasi, *benchmarking*); sebagian lebih kecil dapat menebak tujuan jangka menengah pesaing (dari pernyataan publik manajemen, alokasi modal). Namun pemetaan asumsi pesaing tentang dirinya dan industrinya membutuhkan latihan empati strategis yang langka. Padahal, sel inilah yang membuka prediksi respons: bagaimana pesaing akan bereaksi terhadap langkah strategis kita bergantung pada apa yang mereka asumsikan tentang situasi.

Porac dan Thomas (1990) memperluas analisis pesaing dengan konsep *strategic groups* dan *managerial cognition*. Argumennya adalah bahwa manajer membentuk *cognitive maps* tentang siapa pesaingnya dan bagaimana mereka beroperasi, dan peta ini sering tidak sepenuhnya sesuai dengan realitas industri yang lebih luas. Sebuah *strategic group* terbentuk ketika beberapa perusahaan memiliki kombinasi strategi yang serupa; manajer cenderung memperhatikan pesaing dalam grup yang sama dan mengabaikan yang di luar. Konsekuensinya, perubahan strategis yang berasal dari luar *strategic group* sering luput dari radar.

Zajac dan Bazerman (1991) melalui *Blind Spots in Industry and Competitor Analysis* menyumbang kritik kognitif yang penting. Argumen utamanya adalah bahwa manajer secara sistematis salah membaca pesaing karena tiga bias: *overconfidence* dalam analisisnya sendiri, *illusion of control* yang membuat mereka menganggap respons pesaing dapat dikendalikan, dan *neglect of competitor reasoning* yaitu kegagalan untuk mempertimbangkan bahwa pesaing memiliki proses penalaran strategis yang berbeda. Reger dan Huff (1993) memperdalam ini dengan studi empiris yang menunjukkan bahwa peta kompetitif yang dibentuk manajer sering terlalu sempit dan menutup mata terhadap ancaman yang berasal dari luar peta tersebut.

Implikasi penting dari literatur kognitif ini adalah bahwa kelemahan analisis pesaing kontemporer bukan terutama pada *kekurangan data* (yang menjadi fokus Adom et al. 2016), melainkan pada *bias dalam interpretasi data*. Di era *big data*, perusahaan tidak kekurangan informasi tentang pesaing; yang sulit adalah membaca informasi itu tanpa perangkap kognitif. Pertemuan ini menyiapkan mahasiswa untuk membaca Adom et al. dengan kritis: argumen mereka tentang nilai *competitor analysis* benar, tetapi mereka tidak cukup mendalami pertanyaan yang lebih penting yaitu mengapa *competitor analysis* sering gagal meskipun datanya tersedia.

## 8. Risiko dan Jebakan Pelaksanaan

Pilihan strategi generik adalah satu hal; menjalankannya secara konsisten selama bertahun - tahun adalah hal lain. Bagian ini mengangkat risiko - risiko sistemik yang muncul pada fase eksekusi.

*Strategy decay* mengacu pada erosi bertahap dari kekuatan strategi karena kombinasi imitasi pesaing, perubahan teknologi, dan pergeseran preferensi pelanggan. Sebuah strategi *low-cost* yang dibangun di atas skala produksi yang efisien dapat terkikis ketika teknologi produksi baru menurunkan *minimum efficient scale* dan memungkinkan pesaing kecil masuk dengan biaya yang setara. Sebuah strategi *differentiation* yang dibangun di atas merek dan kualitas dapat terkikis ketika pesaing membangun merek dan kualitas yang setara, lalu menggerus dengan harga yang lebih rendah.

Imitasi cepat menjadi semakin signifikan di era digital. McGrath (2013) berargumen bahwa siklus hidup strategi telah menyusut dari belasan tahun pada era industri menjadi tiga sampai lima tahun pada banyak industri kontemporer. Konsekuensinya, perusahaan yang membangun strategi dengan asumsi durasi panjang akan mengalami kejutan ketika imitasi datang lebih cepat. Strategi yang sustainable di era ini bukan strategi yang kebal imitasi, melainkan strategi yang dirancang untuk berevolusi sebelum imitasi menjadi tekanan dominan.

*Strategic drift* (Johnson 1988) adalah risiko yang paling berbahaya karena bersifat gradual. Drift terjadi ketika perusahaan secara bertahap menyesuaikan strategi dalam langkah - langkah kecil yang masing - masing tampak rasional, tetapi secara kumulatif menjauhkan posisi strategis dari yang relevan dengan industri. Garuda Indonesia pada periode 1999 - 2003 adalah contoh klasik: setiap penyesuaian dilakukan dalam respons terhadap tekanan jangka pendek, tetapi tidak ada respons sistematis terhadap kemunculan *low-cost carriers* yang akhirnya menggeser struktur permintaan secara permanen. Ketika krisis akhirnya menjadi nyata pada pertengahan dekade 2000-an, pilihan strategis Garuda telah terbatas oleh akumulasi drift bertahun - tahun.

Sinyal kapan strategi perlu di - *shift* mencakup: penurunan margin yang konsisten meskipun harga relatif stabil; hilangnya pangsa pasar pada segmen yang sebelumnya dominan; munculnya pesaing baru dengan model bisnis yang berbeda; pergeseran preferensi pelanggan yang teramati melalui survei dan data perilaku. Manajemen yang melihat satu sinyal dapat mengabaikan; manajemen yang melihat tiga atau lebih sinyal yang konsisten dan memilih untuk tidak bertindak cenderung sedang mengalami *strategic drift* yang kemudian akan terbayar mahal.

## 9. Kesimpulan

Pilihan strategi generik bukan sekadar kategori klasifikatoris; ia adalah komitmen organisasional yang membentuk arsitektur perusahaan untuk jangka menengah. Lima posisi yang dirumuskan oleh tradisi Porter - TPGS (*low-cost provider*, *broad differentiation*, *focused low-cost*, *focused differentiation*, *best-cost provider*) menjadi titik referensi yang berguna untuk diskusi strategis, tetapi dengan tiga kualifikasi penting.

*Pertama*, lima posisi tersebut bukan kotak yang *mutually exclusive* secara mutlak. Bukti empiris empat dekade terakhir, terutama meta - analisis Campbell-Hunt (2000) dan literatur hybrid yang dirangkum Salavou (2015), menunjukkan bahwa strategi hybrid yang dieksekusi dengan baik sering menghasilkan kinerja yang lebih baik daripada strategi murni. Argumen *stuck in the middle* tetap relevan sebagai diagnosis kegagalan eksekusi, bukan sebagai larangan a priori atas kombinasi strategi.

*Kedua*, lima posisi tersebut bukan posisi statis. Pada lingkungan kompetisi yang turbulen, perusahaan harus memperlakukan pilihan strategi sebagai *moving baseline* yang akan bergeser seiring perubahan struktur industri, teknologi, dan preferensi pelanggan. Kerangka *dynamic capabilities* (Teece, Pisano & Shuen 1997), *hypercompetition* (D'Aveni 1994), dan *transient advantage* (McGrath 2013) menyediakan bahasa untuk memikirkan pergeseran strategis sebagai kapabilitas, bukan sebagai kegagalan.

*Ketiga*, pilihan strategi generik mensyaratkan analisis pesaing yang disiplin, dan literatur kognitif (Zajac & Bazerman 1991; Porac & Thomas 1990; Reger & Huff 1993) mengingatkan bahwa kelemahan utama analisis pesaing kontemporer adalah bias kognitif, bukan kekurangan data. Pemahaman ini akan menjadi kunci ketika membaca Adom et al. (2016) secara kritis pada *critical review* terpisah.

Integrasi dengan Pertemuan 4 (RBV) dan antisipasi terhadap Pertemuan 6 (strategi tingkat korporat) menjadikan Pertemuan 5 sebagai sentral kerangka mata kuliah. Sumber daya VRIN yang dipetakan pada Pertemuan 4 menjadi bahan baku bagi pilihan strategi generik; pilihan strategi generik di tingkat SBU menjadi konstrain bagi keputusan portofolio di tingkat korporat. Tanpa pemahaman yang jernih atas Pertemuan 5, diskusi pertemuan berikutnya akan dangkal pada level taksonomi tanpa logika ekonomis yang memadai.
"""


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT 2 — CRITICAL REVIEW ARTIKEL 7 (SALAVOU 2015)
# ══════════════════════════════════════════════════════════════════════════════
CR7 = r"""# CRITICAL REVIEW — ARTIKEL 7

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

## 1. Identitas Artikel

**Judul:** *Competitive Strategies and Their Shift to the Future*

**Penulis:** Helen E. Salavou (Department of Business Administration, Athens University of Economics and Business, Greece)

**Publikasi:** *European Business Review*, Vol. 27 No. 1 (2015), pp. 80–99

**DOI:** 10.1108/EBR-04-2013-0073

**Tipe Penelitian:** Artikel konseptual berbasis tinjauan literatur (*general review*), dengan dukungan tabulasi 15 studi empiris pasca - 2000 atas strategi hybrid

**Catatan posisi:** Salavou menulis artikel ini dalam tradisi literatur strategi yang melanjutkan perdebatan empat dekade tentang validitas dan ketahanan kerangka Porter (1980). Artikel termasuk dalam kategori *theoretical synthesis* dan tidak menyodorkan data empiris baru; nilainya terletak pada pemetaan ulang argumen.

## 2. Tujuan Penelitian dan Posisi dalam Literatur

Salavou (2015) menulis artikel ini dengan dua tujuan eksplisit yang ia rumuskan pada bagian abstrak dan pendahuluan. *Pertama*, ia ingin memberikan tinjauan komprehensif atas tradisi strategi kompetitif sejak Porter (1980), dengan fokus khusus pada pergeseran konseptual yang muncul setelah meta - analisis Campbell-Hunt (2000). *Kedua*, ia ingin mengangkat isu konseptual yang menurutnya belum cukup dibahas dalam literatur, yaitu bagaimana strategi hybrid harus dipahami secara teoretis, bukan sekadar dicatat secara empiris.

Posisi Salavou dalam literatur dapat dipahami sebagai jembatan antara tradisi Porter klasik dan tradisi *hybrid strategies* yang berkembang sejak akhir 1980-an. Ia tidak menyangkal nilai kerangka Porter; sebaliknya ia mempertahankan kerangka itu sebagai titik referensi sambil memperluasnya untuk mengakomodasi temuan empiris yang menunjukkan keterbatasan argumen *strategic purity*. Salavou (2015, p. 80) menulis bahwa "the era in which combining competitive strategies was synonymous with stuck-in-the-middle alternatives has been left behind, and the era in which hybrid strategies suggest the most attractive choices, at least in some circumstances, has already begun." Pernyataan ini mencerminkan posisi yang ia ambil: bukan revolusi paradigmatik, melainkan revisi kerangka untuk mencerminkan realitas empiris yang terakumulasi.

Konteks intelektual artikel ini juga penting untuk dipertimbangkan. Salavou menulis dari Eropa, di mana literatur strategi memiliki kecenderungan yang lebih reseptif terhadap pendekatan dimensional (versus taksonomik Porter) dan lebih banyak melakukan studi empiris yang multi - sektoral. Konteks ini terlihat dalam Tabel V artikel (Salavou 2015, p. 91 - 94), yang merangkum 15 studi pasca - 2000 di mana sebagian besar dilakukan di negara - negara Eropa (Spanyol, Yunani, Austria, Portugal). Pengaruh konteks geografis ini perlu dibaca kritis: temuan empiris yang dikumpulkan Salavou mungkin tidak generalisable ke konteks Asia atau Amerika Utara dengan derajat yang sama.

## 3. Argumen Utama: Tiga Pergeseran Konseptual

Argumen sentral Salavou bertumpu pada pemetaan tiga pergeseran konseptual yang menurutnya menstrukturkan evolusi literatur strategi kompetitif sejak 1980. Meskipun ia tidak secara eksplisit menamakan ketiganya sebagai "tiga pergeseran" dalam artikelnya, struktur argumennya dapat direkonstruksi dengan rapi ke dalam kategori - kategori berikut.

### 3.1 Dari *Mutually Exclusive* ke *Hybrid*

Pergeseran pertama yang dikupas Salavou (2015, p. 84 - 85) adalah pergeseran dari logika *strategic purity* Porter yang menempatkan *low-cost*, *differentiation*, dan *focus* sebagai pilihan yang saling eksklusif, ke pengakuan bahwa strategi hybrid (kombinasi dari beberapa dimensi generik) merupakan pilihan yang sah dan sering lebih unggul. Salavou mengutip Hill (1988) sebagai kritik teoretis pertama yang serius, Miller (1992) tentang *generic strategy trap*, dan Campbell-Hunt (2000) sebagai meta - analisis yang menjadi titik balik. Tabel V artikel merangkum 15 studi pasca - 2000 yang mendukung argumen bahwa strategi hybrid sering menghasilkan kinerja yang lebih baik daripada strategi murni.

Salavou (2015, p. 89 - 90) memperluas diskusi ini dengan menyodorkan tipologi 16 jenis strategi hybrid berdasarkan kombinasi tiga dimensi Porter (*low-cost*, *differentiation*, *focus*). Tipologi ini, yang ia tampilkan dalam Tabel IV, menunjukkan bahwa pilihan hybrid bukan tunggal melainkan keluarga konfigurasi. Sebagian dari konfigurasi tersebut menekankan satu dimensi tinggi dengan dua dimensi rata - rata, sebagian menekankan dua dimensi tinggi, dan sebagian (*hybrid type 1*) menekankan ketiga dimensi tinggi secara simultan. Pendekatan dimensional ini, yang Salavou ambil dari Pertusa-Ortega et al. (2009) dan Spanos et al. (2004), menjadi alternatif terhadap pendekatan taksonomik Porter.

### 3.2 Dari *Static* ke *Dynamic*

Pergeseran kedua menyangkut waktu. Porter (1980, 1985) memperlakukan pilihan strategi generik sebagai pilihan yang relatif stabil setelah dipilih. Salavou (2015, p. 90) berargumen bahwa pada lingkungan kompetisi modern, "strategies combining low costs and differentiation elements would be most appropriate in periods of hypercompetition" - kutipan dari Miller (1992) yang ia gunakan untuk mendukung argumennya. Implikasinya adalah bahwa pilihan strategi tidak dapat dipahami terlepas dari dinamika lingkungan; pada periode hyperkompetisi, strategi hybrid menjadi lebih appropriate karena memberi fleksibilitas yang dibutuhkan untuk merespons perubahan.

Argumen ini dapat dihubungkan dengan kerangka *dynamic capabilities* (Teece, Pisano & Shuen 1997) dan *hypercompetition* (D'Aveni 1994), meskipun Salavou tidak melakukan integrasi yang substansial dengan literatur tersebut. Kelemahan signifikan adalah bahwa Salavou tidak mengutip McGrath (2013) tentang *transient advantage* yang sebenarnya menjadi formulasi paling jernih dari pergeseran *static - to - dynamic* dalam literatur strategi kontemporer. Mengingat artikel Salavou dipublikasikan pada 2015 dan buku McGrath terbit pada 2013, kelalaian ini bukan masalah ketersediaan melainkan pilihan editorial.

### 3.3 Dari *Competitive* ke *Cooperative*

Pergeseran ketiga, meskipun tidak dieksplisitkan dalam artikel Salavou seintens dua pergeseran sebelumnya, dapat direkonstruksi dari pernyataannya tentang perubahan lingkungan kompetisi pasca - 2000. Pada Bab Diskusi (Salavou 2015, p. 95) ia mengakui bahwa "the global challenge of today is how scholars will revise theory to better capture reality." Pengakuan implisit ini membuka pintu pada literatur *coopetition* (Brandenburger & Nalebuff 1996) yang memperluas Five Forces dengan dimensi *complementor*, dan literatur *platform economics* yang menempatkan kompetisi dan kerjasama sebagai dimensi simultan.

Sayangnya Salavou tidak melibatkan literatur *coopetition* secara eksplisit. Brandenburger dan Nalebuff (1996) dan tradisi *Value Net* tidak muncul dalam bibliografi artikelnya. Pergeseran ke *cooperative* dengan demikian tetap menjadi tema yang implisit dan kurang dikembangkan, padahal di era platform yang menjadi konteks dominan kompetisi kontemporer, dimensi ini menjadi krusial.

## 4. Koneksi ke Topik Silabus (Pertemuan 5 — TPGS Ch.5)

Artikel Salavou berfungsi sebagai pelengkap kritis terhadap pembahasan TPGS Ch.5. TPGS sendiri sebenarnya sudah mengakui *best-cost provider* sebagai posisi kelima yang sah, di luar empat sel klasik Porter. Pengakuan ini, jika dibaca dalam terang argumen Salavou, sebenarnya merupakan akomodasi diam terhadap literatur hybrid: TPGS sudah meninggalkan logika *strategic purity* Porter klasik, meskipun tidak secara eksplisit menyatakan hal itu. Salavou (2015) memberi mahasiswa kerangka teoretis untuk membaca pengakuan TPGS tersebut secara reflektif: posisi *best-cost provider* bukan tambahan ad - hoc, melainkan konsekuensi logis dari pergeseran paradigmatik yang sudah berlangsung sejak Hill (1988).

Lebih jauh, artikel Salavou mengingatkan mahasiswa bahwa lima strategi generik yang diajarkan dalam TPGS bukan kerangka final. Tabel IV Salavou menunjukkan bahwa di luar lima posisi tersebut, ada 16 tipe strategi hybrid yang teoretis mungkin berdasarkan kombinasi tiga dimensi Porter. Kerangka lima strategi generik dengan demikian sebaiknya diperlakukan sebagai *titik masuk pedagogis*, bukan sebagai peta lengkap atas ruang strategis yang tersedia bagi perusahaan.

Koneksi yang lebih substantif adalah bahwa argumen Salavou tentang *strategic shift* memberi konteks intelektual bagi diskusi tentang *dynamic capabilities* yang akan muncul lagi dalam Pertemuan 9 (TPGS Ch.10 - 12 tentang strategi pembaruan dan transformasi). Dengan membaca Salavou, mahasiswa diperlengkapi untuk memahami bahwa pilihan strategi pada Pertemuan 5 tidak terpisah dari kemampuan untuk mengubahnya; keduanya adalah dua sisi dari satu kapabilitas strategis yang lebih fundamental.

## 5. Kekuatan Artikel

**Pertama, kejelasan kerangka pemetaan literatur.** Salavou berhasil meringkas tradisi tiga dekade penelitian strategi kompetitif ke dalam kerangka yang dapat dipahami dengan jelas. Pergeseran dari *strategic purity* ke *hybridization* dipetakan dengan rapi, didukung oleh tabulasi studi empiris yang sistematis (Tabel I tentang studi yang mendukung *purity* hingga 2000, Tabel V tentang studi yang mendukung *hybrid* sejak 2000). Kerangka ini memudahkan pembaca, terutama mahasiswa, untuk mengikuti perdebatan teoretis yang kompleks.

**Kedua, pengakuan bahwa *stuck-in-the-middle* berbeda dari *hybrid*.** Salavou (2015, p. 85) secara eksplisit menarik garis pembeda yang sering kabur dalam literatur: "stuck-in-the-middle strategies reflect a firm's unwillingness to make choices about how to compete (Pertusa-Ortega et al., 2009) or a non-competitive advantage with high costs and low differentiation. To further mark this difference, researchers claim that a stuck-in-the-middle strategy is by definition a particular underdeveloped form of a hybrid strategy." Pembedaan ini penting secara konseptual karena mengakhiri kebingungan yang berlangsung sejak Porter (1985): mengejar hybrid bukan otomatis menjadi *stuck in the middle*; *stuck in the middle* adalah bentuk hybrid yang gagal dieksekusi.

**Ketiga, sumbangan tipologi 16 jenis hybrid.** Tabel IV (Salavou 2015, p. 89) menyajikan tipologi yang dapat digunakan oleh peneliti dan praktisi untuk mendiagnosis konfigurasi strategi yang spesifik. Tipologi ini lebih kaya dari pengelompokan biner *purity vs hybrid* dan memberi alat untuk pembedaan yang lebih halus.

**Keempat, kepekaan terhadap konteks geografis.** Salavou secara eksplisit mengakui bahwa bukti empiris yang ia kumpulkan terkonsentrasi di Eropa, dan bahwa konteks Amerika Utara serta Asia mungkin memberikan pola yang berbeda. Kepekaan ini, meskipun tidak diteruskan ke analisis komparatif yang mendalam, menunjukkan kesadaran metodologis yang patut diapresiasi.

**Kelima, kontribusi pada agenda penelitian.** Pada Bab Diskusi, Salavou (2015, p. 95 - 96) merumuskan tiga arah penelitian masa depan: pengembangan kerangka konseptual untuk hybrid yang lebih *fine - grained*, integrasi tipologi dengan kerangka teori yang sudah ada, dan pemetaan hubungan kontingensi antara strategi dan kinerja. Agenda ini berguna untuk peneliti yang hendak melanjutkan tradisi.

## 6. Keterbatasan dan Kelemahan

**Pertama, ketiadaan data empiris baru.** Salavou (2015) adalah *literature review* murni; tidak ada survei, studi kasus, atau analisis data sekunder yang baru. Untuk publikasi pada jurnal seperti *European Business Review*, format ini lazim, tetapi membatasi klaim kausal yang dapat ditarik. Pernyataan bahwa "strategi hybrid sering lebih unggul" tetap merupakan rangkuman dari studi - studi yang sebagiannya menggunakan metodologi yang berbeda, ukuran kinerja yang berbeda, dan konteks industri yang berbeda. Salavou tidak melakukan meta - analisis kuantitatif yang akan memberikan klaim ini fondasi statistik yang lebih kuat daripada Campbell-Hunt (2000).

**Kedua, kelalaian bibliografis yang signifikan.** Tiga absensi yang patut dicatat. *Pertama*, McGrath (2013) tentang *transient advantage* tidak muncul dalam bibliografi, padahal buku ini menjadi formulasi paling jernih dari argumen *static - to - dynamic* yang Salavou angkat. *Kedua*, Brandenburger dan Nalebuff (1996) tentang *coopetition* dan *Value Net* tidak ada, padahal pergeseran *competitive - to - cooperative* yang Salavou implisit angkat membutuhkan dialog dengan literatur ini. *Ketiga*, literatur *platform economics* (Rochet & Tirole 2003; Eisenmann, Parker & Van Alstyne 2006) yang menjadi konteks dominan kompetisi kontemporer tidak terlibat. Akumulasi tiga kelalaian ini mengindikasikan bahwa Salavou bekerja dalam tradisi literatur strategi yang lebih sempit daripada yang ia klaim.

**Ketiga, kontribusi orisinalitas terbatas.** Pertanyaan yang patut diajukan adalah: apakah "shift" yang didokumentasikan Salavou merupakan kemajuan teoretis yang genuine, ataukah label akademis untuk apa yang sudah dilakukan praktisi selama dua dekade? Banyak observasi Salavou sudah didokumentasikan lebih awal di literatur lain. Treacy dan Wiersema (1995) sudah menyodorkan tipologi paralel (*operational excellence*, *product leadership*, *customer intimacy*) yang secara substantif setara dengan apa yang Salavou rangkum sebagai hybrid. Pertusa-Ortega et al. (2009) dan Spanos et al. (2004) sudah memetakan pendekatan dimensional yang menjadi tulang punggung tipologi 16 hybrid Salavou. Kontribusi orisinal Salavou terletak pada sintesis, bukan pada penemuan baru.

**Keempat, pengakuan terbatas atas Treacy dan Wiersema.** Mengingat similaritas substantif antara value disciplines Treacy dan Wiersema dengan hybrid strategies Salavou, pengakuan terhadap tradisi tersebut sangat minim dalam artikel. Treacy dan Wiersema disebut hanya sekali pada halaman 96, dalam konteks "future work should place any competitive strategy ... within a specified theoretical context (March, 1991; Treacy and Wiersema, 1997)." Ini terkesan superficial. Pertanyaan yang seharusnya diajukan oleh Salavou: dalam hal apa tipologi 16 hybrid - nya menambahkan dimensi baru yang tidak ada dalam tipologi tiga value disciplines Treacy dan Wiersema? Pertanyaan ini tidak dijawab.

**Kelima, generalisasi prematur dari konteks Eropa.** Sebagian besar studi yang Salavou rangkum dilakukan di negara - negara Eropa atau pada pasar Eropa. Klaim umum bahwa "hybrid menjadi pilihan yang lebih unggul" mungkin tidak sepenuhnya berlaku pada konteks Amerika Utara (di mana kompetisi sektor teknologi sering didominasi oleh *winner - take - all dynamics* yang menyukai strategi murni *differentiation* atau *cost leadership*) atau pada pasar - pasar berkembang seperti Indonesia (di mana struktur pasar masih sering didominasi oleh proteksi regulatif yang membentuk pilihan strategis secara berbeda).

**Keenam, ketiadaan pembahasan eksekusi.** Salavou (2015) bekerja terutama pada level konseptual; ia tidak banyak membahas tantangan eksekusi strategi hybrid. Padahal, kritik utama Porter (1985) terhadap hybrid bukan pada tataran konseptual (apakah hybrid mungkin) melainkan pada tataran organisasional (apakah hybrid dapat dieksekusi tanpa konflik internal). Tanpa membahas tantangan eksekusi, argumen Salavou tetap berada pada level kemungkinan, bukan kelaikan praktis.

## 7. Evaluasi Kritis

Posisi yang adil terhadap Salavou (2015) adalah mengakui kontribusinya sebagai *bridge work* yang berguna sambil mencatat batas - batas argumennya. Tiga pengamatan kritis layak ditekankan.

*Pertama*, kontribusi terbesar Salavou sebenarnya adalah memetakan secara sistematis bahwa literatur strategi kompetitif telah bergeser dari logika *purity* ke *hybridization*. Pemetaan ini bermanfaat bagi pembaca yang membutuhkan orientasi cepat atas perdebatan tiga dekade. Namun pemetaan bukan klaim teoretis; Salavou tidak menambahkan teori baru, ia menyusun ulang teori yang ada. Ini tidak merendahkan nilai artikelnya, tetapi mengkalibrasi ekspektasi pembaca.

*Kedua*, klaim bahwa strategi hybrid sering lebih unggul perlu dibaca dengan kehati - hatian metodologis. Studi - studi yang Salavou rangkum menggunakan ukuran kinerja yang heterogen (ROA, ROE, *gross margin*, ukuran subjektif), populasi yang berbeda (manufaktur, jasa, lintas - sektor), dan konteks industri yang sangat beragam. Generalisasi bahwa "hybrid mengungguli purity" tidak dapat dibangun secara meyakinkan dari rangkuman ini saja; klaim tersebut membutuhkan meta - analisis kuantitatif yang lebih ketat. Salavou sendiri mengakui keterbatasan ini secara implisit ketika ia menyebut bahwa hybrid lebih unggul "at least in some circumstances" (p. 80).

*Ketiga*, pertanyaan yang lebih penting daripada *apakah* hybrid lebih unggul adalah *kapan* hybrid lebih unggul dan *kapan* purity lebih unggul. Pertanyaan kontingensi ini sebenarnya muncul di literatur (Miller 1988, Beal 2000) tetapi tidak diangkat sebagai inti diskusi oleh Salavou. Pembaca yang menutup artikel ini tanpa pertanyaan kontingensi yang tegas akan terjebak pada generalisasi yang menyederhanakan: bahwa hybrid selalu lebih baik. Padahal kondisi industri tertentu (komoditas dengan biaya pengalihan rendah, segmen sangat *price - sensitive*) tetap mendukung *low-cost provider* murni.

*Keempat*, satu kritik tambahan tentang format. Artikel Salavou banyak bersandar pada tabulasi studi sebelumnya tanpa analisis kritis individual atas masing - masing studi. Tabel V yang merangkum 15 studi pasca - 2000 disajikan secara deskriptif (penulis, metode, temuan utama) tanpa pengamatan tentang kelemahan metodologis spesifik atau ketidakkonsistenan antar studi. Ini membuat tabulasi tampak otoritatif lebih dari yang seharusnya: pembaca cenderung mengakumulasi kesan bahwa "ada banyak bukti", padahal sebagian dari bukti tersebut mungkin saling bertentangan jika diuraikan secara teliti.

## 8. Implikasi bagi Pemahaman Manajemen Strategik

**Pertama**, untuk mahasiswa Magister Akuntansi, Salavou memberi orientasi penting bahwa kerangka strategi kompetitif telah bergeser dari taksonomi statis ke pendekatan dimensional. Implikasinya bagi praktik akuntansi manajemen adalah bahwa pengukuran kinerja strategis tidak dapat lagi mengandalkan pengelompokan biner (cost vs differentiation), melainkan harus mengakomodasi kombinasi dimensi yang lebih halus. Sistem KPI yang dirancang untuk mengukur strategi *low-cost* murni akan miss representasi pada perusahaan yang menjalankan *best-cost provider*.

**Kedua**, bagi auditor strategis dan analis investasi, kerangka Salavou memperlengkapi kemampuan untuk mendiagnosis posisi kompetitif perusahaan dengan lebih akurat. Pertanyaan yang pernah terjawab dengan "perusahaan ini mengejar diferensiasi" sekarang dapat dipertajam menjadi "perusahaan ini mengejar kombinasi *innovation differentiation* dan *cost efficiency* dengan profil yang menyerupai hybrid type 4 menurut tipologi Salavou." Dengan demikian, evaluasi kelayakan strategis menjadi lebih *fine - grained*.

**Ketiga**, dalam konteks Indonesia, beberapa contoh paradigmatik dapat dibaca melalui kerangka Salavou. *Indomaret dan Alfamart* sebagai *best-cost provider* yang dibangun di atas kombinasi efisiensi distribusi (*low-cost* element) dan kenyamanan lokasi serta keseragaman pengalaman (*differentiation* element). Keduanya bukan *stuck in the middle* karena keduanya berhasil membangun konfigurasi sumber daya yang konsisten untuk mendukung kombinasi tersebut. Hasilnya adalah penggantian struktural ekosistem warung tradisional, bukan sekadar peningkatan pangsa pasar pada ritel modern.

*GoTo* (merger Gojek - Tokopedia 2021) sebagai contoh kompleks yang memperlihatkan bahwa pergeseran *competitive - to - cooperative* (yang Salavou tidak gali secara mendalam) dapat berkembang lebih jauh menjadi integrasi penuh. Sebelum merger, Gojek dan Tokopedia sudah berkolaborasi dalam beberapa dimensi (pembayaran melalui GoPay, integrasi logistik) sambil bersaing pada beberapa dimensi lain. Merger menjadi formalisasi dari *coopetition* yang sudah ada secara informal. Pertanyaan yang relevan dengan kerangka Salavou: apakah ini coopetition yang berhasil, atau eliminasi pesaing yang dibungkus sebagai kerjasama? Jawabannya membutuhkan analisis struktur pasar pasca - merger yang berada di luar cakupan artikel.

*AirAsia* di Asia Tenggara sebagai contoh *dynamic shift* yang menggambarkan argumen Salavou tentang *static - to - dynamic*. AirAsia memulai sebagai *focused low-cost* pada rute - rute spesifik di Malaysia, lalu memperluas menjadi *broad low-cost* yang mencakup seluruh kawasan Asia Tenggara. Pergeseran ini bukan sekadar ekspansi geografis melainkan perubahan posisi strategis: dari segmen sempit ke segmen luas, dengan kapabilitas yang berbeda. AirAsia menjadi contoh eksekusi pergeseran strategis yang relatif berhasil di pasar yang menantang.

*Tokopedia, Shopee, dan Lazada* dalam dinamika e - commerce Indonesia sebagai laboratorium *transient advantage* (McGrath 2013) yang Salavou sebenarnya tidak gali. Ketiga platform secara berkala menggeser kombinasi strategi: subsidi agresif untuk akuisisi pengguna, lalu transisi ke fokus margin, lalu eksperimen *live commerce* dan *social commerce*. Setiap fase membawa profil strategis yang berbeda, dan tidak satu pun yang dapat dipertahankan untuk periode panjang. Konteks ini mengilustrasikan bahwa argumen *static - to - dynamic* Salavou perlu diperluas dengan literatur McGrath untuk menjadi diagnostik yang utuh.

## 9. Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut

**Pertama**, sejauh mana argumen Salavou tentang superioritas strategi hybrid dapat digeneralisasi ke konteks pasar berkembang seperti Indonesia? Bukti empiris yang Salavou kumpulkan sebagian besar berasal dari pasar Eropa yang memiliki karakteristik berbeda (regulasi yang lebih matang, basis pelanggan yang lebih homogen secara pendapatan, infrastruktur logistik yang lebih efisien). Pada konteks Indonesia di mana pasar masih segmentasi yang kuat dan logistik masih menjadi *bottleneck*, apakah kombinasi strategi hybrid akan menghasilkan superioritas kinerja yang serupa, atau justru *focused* murni (low-cost atau differentiation) lebih realistis sebagai pilihan strategis bagi banyak perusahaan?

**Kedua**, bagaimana seharusnya kerangka Salavou diintegrasikan dengan literatur *coopetition* dan *platform economics* yang ia abaikan? Pada industri *digital ecosystem* yang menjadi konteks dominan kompetisi kontemporer, batas perusahaan menjadi kabur dan pilihan strategis sering melibatkan koalisi temporer dengan pesaing nominal. Apakah tipologi 16 hybrid Salavou dapat diperluas untuk mengakomodasi dimensi *coopetition*, atau dibutuhkan kerangka yang sepenuhnya baru?

**Ketiga**, dalam konteks BUMN Indonesia di mana sebagian besar pilihan strategis dibatasi oleh mandat regulatif (kewajiban layanan publik, akses ke pembiayaan pemerintah, hak eksklusif sektor strategis), apakah kerangka strategi hybrid Salavou masih relevan? Atau pilihan strategis BUMN sebenarnya berada di ruang yang berbeda dari yang Salavou modelkan, di mana faktor regulatif mendominasi dimensi kompetitif murni?

**Keempat**, pertanyaan metodologis yang patut diajukan: jika strategi hybrid memang sering lebih unggul pada banyak konteks, mengapa logika *strategic purity* tetap memiliki daya tarik akademis dan praktis yang persisten? Jawaban yang spekulatif tetapi menarik adalah bahwa *strategic purity* lebih mudah diajarkan, dikomunikasikan, dan dieksekusi karena memberi disiplin organisasional yang jelas. Hybrid menuntut *judgment* dan *trade-off* yang halus yang sulit diinstitusionalisasi. Pertanyaan yang patut menjadi tesis: apakah perusahaan yang berhasil menjalankan hybrid sebenarnya memiliki kapabilitas organisasional yang langka, dan apakah itu menjelaskan mengapa hybrid, meskipun secara konseptual unggul, tidak menjadi standar industri?
"""


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT 3 — CRITICAL REVIEW ARTIKEL 8 (ADOM, NYARKO & SOM 2016)
# ══════════════════════════════════════════════════════════════════════════════
CR8 = r"""# CRITICAL REVIEW — ARTIKEL 8

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

## 1. Identitas Artikel

**Judul:** *Competitor Analysis in Strategic Management: Is It a Worthwhile Managerial Practice in Contemporary Times?*

**Penulis:** Alex Yaw Adom, Israel Kofi Nyarko, Gladys Narki Kumi Som (Department of Management & Public Administration, Central University, Accra, Ghana)

**Publikasi:** *Journal of Resources Development and Management*, Vol. 24 (2016), p. 116

**Tipe Penelitian:** Tinjauan literatur integratif (*integrative literature review*) dengan elemen interpretasi pribadi penulis berdasarkan konteks praktik di Afrika

**Catatan posisi:** Artikel ini termasuk kategori *general review* yang berfungsi sebagai sintesis pedagogis bagi praktisi dan mahasiswa, bukan kontribusi teoretis baru. Diterbitkan pada jurnal yang relatif kurang dikenal secara akademis (*Journal of Resources Development and Management* tidak terindeks di Scopus atau Web of Science), sehingga jangkauan dan dampak akademisnya terbatas.

## 2. Tujuan Penelitian dan Posisi dalam Literatur

Adom, Nyarko dan Som (2016) merumuskan tujuan artikel mereka secara eksplisit pada bagian abstrak: "to establish the relevance or otherwise of competitor analysis as a strategic management practice in modern business competition." Pertanyaan inti yang diajukan adalah apakah analisis pesaing tetap menjadi praktik manajerial yang *worthwhile* di era kontemporer yang ditandai dengan banjir informasi dan kemajuan teknologi *big data*. Pertanyaan ini, jika dibaca secara harfiah, sebenarnya bersifat hampir retoris: tidak ada literatur serius yang berargumen bahwa analisis pesaing tidak relevan. Dengan demikian, framing "is it worthwhile" agak bersifat *straw man* yang akan dikupas pada Bagian 7.

Posisi Adom et al. dalam literatur adalah sebagai sintesis ulang dari tradisi *competitor analysis* yang sudah panjang. Mereka membangun argumen di atas tiga lapisan literatur. *Lapisan pertama* adalah Porter (1980) Bab 3 yang menyodorkan kerangka empat sel klasik untuk analisis pesaing (*future goals*, *current strategy*, *assumptions*, *capabilities*); meskipun Adom et al. tidak menyebut empat sel ini secara eksplisit, struktur diskusi mereka mengikuti logikanya. *Lapisan kedua* adalah literatur *competitive intelligence* yang dikembangkan oleh Fleisher dan Bensoussan (2003, 2007) yang menjadi rujukan utama mereka. *Lapisan ketiga* adalah literatur praktis seperti Kotler dan Armstrong (2009), Hoque (2006), dan David (2011) yang menjadi sumber tipologi pesaing dan teknik praktis yang mereka rangkum.

Konteks geografis penulis (Ghana, Afrika Sub - Sahara) memberi warna pada artikel meskipun tidak secara eksplisit dieksplorasi. Asumsi - asumsi yang implisit dalam diskusi mereka mencerminkan konteks pasar yang berbeda dari Eropa atau Amerika Utara. *Pertama*, akses informasi tentang pesaing di Ghana cenderung lebih terbatas; ini menjelaskan mengapa Adom et al. (2016, p. 117) menekankan tantangan pengumpulan data yang sebenarnya kurang relevan di pasar dengan disclosure yang ketat. *Kedua*, ukuran pasar yang relatif kecil di Ghana menjadikan analisis pesaing lebih terkonsentrasi pada beberapa pemain dominan, berbeda dari pasar besar dengan banyak pemain *fragmented*. Ketidakseimbangan kontekstual ini perlu menjadi pertimbangan ketika klaim - klaim umum mereka diaplikasikan pada konteks Indonesia atau Asia Tenggara yang lebih luas.

## 3. Argumen Utama: Worthwhile dengan Pergeseran Peran

Argumen sentral Adom et al. adalah bahwa analisis pesaing tetap *worthwhile* sebagai praktik manajerial kontemporer, tetapi dengan pergeseran peran yang substantif. Mereka menyusun argumen ini dalam empat dimensi yang dapat direkonstruksi sebagai berikut.

### 3.1 Pergeseran dari Akuisisi Informasi ke *Sense - Making*

Argumen pertama (Adom et al. 2016, p. 117 - 118) adalah bahwa pada era pra - internet, tantangan utama analisis pesaing adalah *memperoleh* informasi yang sulit, mahal, dan sering tidak lengkap. Pada era kontemporer, informasi tentang pesaing tersedia berlimpah melalui laporan tahunan, *disclosure* publik, pemberitaan media, *social media*, riset industri komersial, dan bahkan *big data analytics*. Tantangan yang berubah adalah *sense - making*: bagaimana memaknai informasi yang melimpah, memilih mana yang relevan, dan membangun narasi koheren tentang strategi pesaing dari potongan - potongan data.

Argumen ini secara substantif benar dan sejalan dengan perkembangan praktik *competitive intelligence* yang Fleisher dan Bensoussan (2007) dokumentasikan. Namun Adom et al. tidak mengembangkan implikasi epistemologis dari pergeseran ini. Pergeseran dari akuisisi ke *sense - making* mengubah profil keterampilan yang dibutuhkan dalam organisasi: dari kapabilitas pengumpulan data (pekerjaan analis junior) menuju kapabilitas interpretasi pola dan prediksi respons (pekerjaan analis senior dengan latar belakang industri yang dalam). Implikasi ini tidak diangkat secara eksplisit, padahal sangat relevan untuk diskusi tentang struktur tim *competitor intelligence* di organisasi modern.

### 3.2 Pergeseran dari *Ad - Hoc* ke Sistematis

Argumen kedua (Adom et al. 2016, p. 117) adalah bahwa banyak perusahaan masih menjalankan analisis pesaing secara *ad - hoc* yaitu pada saat ada isu atau proyek spesifik. Adom et al. mengadvokasi pendekatan sistematis: proses yang ditentukan, frekuensi yang ditentukan, *ownership* yang jelas. Argumen ini sejalan dengan tradisi profesionalisasi *competitive intelligence* yang dikembangkan oleh *Strategic and Competitive Intelligence Professionals* (SCIP) sejak akhir 1980-an. Pendekatan sistematis menghasilkan *intelligence* yang konsisten, dapat diaudit, dan terintegrasi dengan proses pengambilan keputusan strategis.

Pengembangan argumen ini terbatas pada artikel. Adom et al. tidak melibatkan literatur SCIP secara substansial; mereka tidak membahas *Code of Ethics* SCIP yang menjadi rujukan profesi *competitive intelligence*. Mereka juga tidak membahas *24 techniques of competitor intelligence* yang Fleisher dan Bensoussan (2007) sajikan sebagai *toolkit* yang lengkap. Akibatnya, advokasi mereka untuk pendekatan sistematis kekurangan substansi operasional: *bagaimana* sistem yang sistematis itu dirancang dan dijalankan tetap tidak terjawab.

### 3.3 Pergeseran dari Deskriptif ke Prediktif

Argumen ketiga (Adom et al. 2016, p. 119 - 120) adalah bahwa analisis pesaing kontemporer harus bergerak dari deskripsi ("apa yang pesaing lakukan sekarang") ke prediksi ("apa yang pesaing akan lakukan berikutnya" dan "bagaimana pesaing akan merespons pilihan strategis kita"). Argumen ini sejalan dengan penekanan Porter (1980) Bab 3 pada kemampuan memprediksi *competitive response*. Adom et al. mengutip kerangka empat sel Porter secara implisit ketika membahas pentingnya memahami "competitor's existing strategies and objectives" (sel *current strategy* dan *future goals*), "competitor's major strengths and weaknesses" (sel *capabilities*), dan "predicting competitor's future moves" (sel *assumptions* dalam terminologi Porter).

Yang absen dari diskusi adalah pengakuan eksplisit bahwa sel *assumptions*, yaitu sel yang paling sulit dipenuhi tetapi paling bernilai, adalah *the* sel yang paling membuka *response prediction*. Memprediksi respons pesaing membutuhkan pemahaman tentang *bagaimana* pesaing memahami industri dan dirinya sendiri. Tanpa pemetaan asumsi pesaing, prediksi respons hanya menjadi proyeksi linier dari perilaku masa lalu, yang sering keliru pada momen - momen disrupsi.

### 3.4 Penegasan Nilai Kompetitif Profiling

Argumen keempat (Adom et al. 2016, p. 122 - 123) menyajikan teknik *Competitor Profile Matrix* (CPM) dari Zimmerer et al. (2008) sebagai alat kunci untuk *competitor profiling* sistematis. CPM memetakan pesaing pada *Key Success Factors* (KSF) yang dibobot tertimbang, dengan skor 1 - 4 yang mencerminkan *major weakness* hingga *major strength*. Hasil akhir adalah skor tertimbang yang membandingkan posisi kompetitif perusahaan fokal dengan pesaing utamanya.

Adom et al. menyertakan tabel ilustratif (Tabel 1, p. 121) di mana perusahaan A mendapat skor 2.80, sementara pesaing 1 mendapat 3.10 dan pesaing 2 mendapat 2.65. Ilustrasi ini sederhana tetapi cukup untuk menunjukkan bagaimana CPM bekerja sebagai diagnostik. Mereka juga menyertakan teknik *competitor array* yang Gordon (1989) kembangkan, yang strukturnya serupa CPM dengan variasi pada penyajian visual.

Diskusi tentang CPM dan *competitor array* tetap pada level pengantar. Adom et al. tidak membahas batas - batas kedua teknik tersebut: subjektivitas dalam pemilihan KSF, ketidakstabilan bobot pada lingkungan turbulen, dan risiko *false precision* yang muncul ketika skor kuantitatif disajikan tanpa kerangka pertimbangan kualitatif yang memadai. Untuk artikel yang berfungsi sebagai sintesis pedagogis, kekurangan diskusi kritis ini mengurangi nilainya sebagai alat pembelajaran.

## 4. Koneksi ke Topik Silabus (Pertemuan 5 — TPGS Ch.5)

Artikel Adom et al. berfungsi sebagai pelengkap bagi diskusi pilihan strategi generik dalam TPGS Ch.5. Argumen yang menjadi jembatan adalah bahwa pilihan strategi generik (low - cost provider, broad differentiation, focused, best-cost provider) tidak dapat diambil tanpa pemahaman akurat tentang pesaing - pesaing di dalam industri. *Strategic groups* yang dibentuk oleh pesaing membatasi ruang manuver perusahaan; respons yang diantisipasi dari pesaing menentukan apakah pilihan strategi tertentu dapat dipertahankan atau akan terkikis cepat.

Kontribusi Adom et al. bagi mahasiswa adalah memperkenalkan *toolkit* praktis (CPM, *competitor array*, tipologi pesaing) yang dapat digunakan sebagai *prasyarat operasional* sebelum pemilihan strategi generik. TPGS Ch.5 sendiri membahas pilihan strategi generik dengan fokus pada konfigurasi internal yang mendukung tiap pilihan; Adom et al. menambahkan dimensi eksternal yang melengkapi: bagaimana mengukur posisi kompetitif relatif terhadap pesaing.

Namun ada keterbatasan signifikan dalam koneksi ini. Adom et al. tidak melibatkan literatur kognitif *competitor analysis* (Zajac & Bazerman 1991; Porac & Thomas 1990; Reger & Huff 1993) yang menjadi kritik paling tajam terhadap teknik - teknik kuantitatif seperti CPM. Literatur kognitif berargumen bahwa kelemahan utama analisis pesaing kontemporer bukan pada *kekurangan data* (yang menjadi fokus Adom et al.) melainkan pada *bias dalam interpretasi data*. Tanpa melibatkan literatur ini, koneksi Adom et al. ke TPGS Ch.5 menjadi terbatas pada level teknik tanpa kedalaman epistemologis yang memadai.

## 5. Kekuatan Artikel

**Pertama, kepraktisan untuk audiens praktisi.** Artikel ditulis dengan bahasa yang aksesibel dan menyertakan ilustrasi konkret (Tabel 1 CPM, Tabel 2 *competitor array*) yang dapat langsung digunakan oleh manajer dan mahasiswa. Untuk konteks pembaca yang membutuhkan orientasi cepat atas teknik *competitor analysis*, artikel ini berfungsi dengan baik sebagai pengantar.

**Kedua, integrasi tipologi pesaing yang berguna.** Adom et al. (2016, p. 118 - 119) menyajikan tipologi Kotler dan Armstrong (2009) yang mengelompokkan pesaing menjadi *brand competitors*, *industry competitors*, *form competitors*, dan *generic competitors*. Mereka juga menambahkan tipologi *direct - indirect - future competitors*. Tipologi ini berguna untuk memperluas radar manajer di luar pesaing langsung yang biasa terlihat. Contoh yang mereka berikan tentang Sea Ray (kapal cepat) sebagai pesaing tidak langsung Corvette (mobil sport) untuk segmen *young men* dengan disposable income menarik karena memperlihatkan bagaimana batas industri dapat kabur.

**Ketiga, pengakuan atas dimensi etika.** Adom et al. (2016, p. 125) menyebut isu etika dalam pengumpulan informasi pesaing: "information obtained illegally (as a result of activities such as theft, blackmail, or eavesdropping) cannot, or, at least, should not, be used as its use is unethical as well as illegal." Pengakuan ini, meskipun singkat, penting karena mengingatkan bahwa *competitive intelligence* memiliki batas etik. Konteks profesional SCIP sebenarnya memberikan kerangka etika yang lebih komprehensif, tetapi Adom et al. hanya menyentuh isu ini secara superficial.

**Keempat, keterbukaan terhadap dimensi *root - level* vs *fruit - level*.** Adom et al. (2016, p. 117 - 118) mengutip Giget (1988) tentang analogi pohon di mana produk akhir (*fruit*) adalah manifestasi visible dari kompetensi inti (*root*) yang tidak terlihat. Mereka mengembangkan implikasi: analisis pesaing yang hanya fokus pada produk akhir akan miss representasi atas sumber daya dan kapabilitas yang menjadi fondasi produk tersebut. Wawasan ini, yang sebenarnya konsisten dengan kerangka VRIN dari Pertemuan 4, layak diapresiasi.

**Kelima, pengakuan atas ketidaklengkapan informasi.** Pada bagian akhir, Adom et al. (2016, p. 127) mengakui bahwa "tracking merely the visible 'fruit-level' and overlooking the 'root-level' sources of a rival firm's competitiveness may provide only a transient view of the actual strengths or weaknesses of that firm. Instead of over-relying on the analyses of markets entered and products manufactured, attention should be shifted to the less-emphasized skill base and organizational factors." Pengakuan ini menjadi *takeaway* yang berguna bagi pembaca yang sering jatuh pada kesalahan memetakan kompetisi hanya pada level produk.

## 6. Keterbatasan dan Kelemahan

**Pertama, framing pertanyaan yang bersifat *straw man*.** Pertanyaan inti artikel "is it a worthwhile managerial practice in contemporary times?" sebenarnya tidak diperdebatkan secara serius dalam literatur akademis. Tidak ada peneliti atau praktisi terkemuka yang berargumen bahwa analisis pesaing tidak *worthwhile* di era kontemporer. Dengan demikian, jawaban "ya, tetap worthwhile" yang menjadi simpulan artikel bukan *finding* yang signifikan; ia adalah konfirmasi atas konsensus yang sudah ada. Pertanyaan yang lebih bermakna adalah *bagaimana* praktik analisis pesaing harus berubah, dan artikel ini hanya menyentuh permukaan pertanyaan tersebut.

**Kedua, ketiadaan kontribusi teoretis baru.** Artikel adalah *literature review* yang merangkum sumber - sumber sekunder. Tidak ada konsep baru, tidak ada kerangka diagnostik baru, tidak ada hipotesis yang diuji. Semua argumen yang Adom et al. ajukan sudah ada di literatur sebelumnya, sering dengan formulasi yang lebih kuat dan diintegrasikan secara lebih sistematis. Untuk artikel yang dipublikasikan pada 2016, kontribusi orisinalitas yang terbatas ini menjadi kelemahan signifikan.

**Ketiga, kelalaian atas literatur kognitif.** Ini adalah kritik paling serius. Adom et al. tidak melibatkan literatur kognitif *competitor analysis* yang merupakan kritik paling tajam terhadap pendekatan tradisional. *Blind Spots in Industry and Competitor Analysis* dari Zajac dan Bazerman (1991) bahkan dikutip dalam artikel mereka (p. 124, dalam konteks *capacity expansion*) tetapi argumen utamanya tentang *systematic biases* dalam interpretasi pesaing tidak dikembangkan. Porac dan Thomas (1990) tentang *managerial cognition and competitive groups* tidak ada dalam bibliografi. Reger dan Huff (1993) tentang *strategic groups as cognitive constructions* juga absen.

Akumulasi kelalaian ini berarti Adom et al. tidak pernah secara serius mempertimbangkan kemungkinan bahwa kelemahan analisis pesaing kontemporer bukan pada *kekurangan data atau teknik* (yang menjadi fokus mereka) melainkan pada *bias kognitif dalam interpretasi*. Manajer di era *big data* tidak kekurangan informasi tentang pesaing; yang sulit adalah membaca informasi itu tanpa perangkap kognitif seperti *overconfidence*, *illusion of control*, dan *neglect of competitor reasoning* yang Zajac dan Bazerman dokumentasikan. Argumen yang lebih kuat tentang nilai *competitor analysis* kontemporer akan menggabungkan dimensi epistemologi kognitif ini dengan dimensi teknik yang Adom et al. sajikan.

**Keempat, keterbatasan engagement dengan Fleisher dan Bensoussan toolkit.** Adom et al. mengutip Fleisher dan Bensoussan (2003, 2007) sebagai rujukan utama, tetapi tidak mengembangkan toolkit 24 teknik yang Fleisher dan Bensoussan tawarkan. Teknik - teknik seperti *Win/Loss Analysis*, *Driving Forces Analysis*, *Customer Segmentation Analysis*, *Indications and Warning Analysis*, dan *Cognitive Mapping* tidak disinggung. Artikel akan jauh lebih kaya jika mengupas beberapa teknik ini secara mendalam, terutama yang relevan untuk kondisi era *big data*.

**Kelima, generalizability bukti lapangan Afrika.** Sebagian klaim Adom et al. tentang tantangan praktis (akses informasi terbatas, kultur informal dalam *competitive intelligence*, ukuran pasar yang menyulitkan formalisasi sistem) mencerminkan konteks Ghana atau Afrika Sub - Sahara yang lebih luas. Klaim - klaim ini tidak otomatis berlaku untuk pasar dengan informasi tebal seperti Indonesia (di mana laporan tahunan publik, regulator OJK / BEI yang mewajibkan disclosure, dan media bisnis yang aktif menyediakan data berlimpah) atau pasar dengan *disclosure* ketat seperti Singapura atau Hong Kong. Generalisasi prematur perlu dihindari ketika argumen mereka diaplikasikan pada konteks Asia Tenggara.

**Keenam, ketiadaan diskusi tentang cost - benefit *competitor intelligence* sistem.** Sistem *competitor intelligence* yang sistematis mahal: sumber daya manusia spesialis, infrastruktur informasi, integrasi dengan proses pengambilan keputusan strategis. Adom et al. mengadvokasi sistem yang sistematis tetapi tidak membahas pada kondisi apa biaya tidak sebanding dengan manfaat. Untuk perusahaan kecil dan menengah (UKM) di pasar berkembang, pertanyaan ini sangat relevan: apakah CPM dan teknik formal lain layak diinvestasikan, atau intelijen informal yang ditempelkan pada peran manajemen umum sudah cukup?

**Ketujuh, keterbatasan metodologis.** Sebagai *literature review integratif*, artikel tidak menggunakan protokol sistematis (PRISMA, *systematic review*) yang akan memberi jaminan komprehensif atas literatur yang dirangkum. Pemilihan sumber tampak ad - hoc, dengan beberapa rujukan yang sudah berusia tiga dekade (Porter 1980, Oxenfeldt & Schwartz 1981, Giget 1988) dan beberapa yang lebih kontemporer (David 2011, Bygrave & Zacharakis 2011) tanpa argumen tentang prinsip pemilihan. Untuk publikasi akademis, ketiadaan protokol ini menjadi kelemahan metodologis.

## 7. Evaluasi Kritis

Posisi yang adil terhadap Adom, Nyarko & Som (2016) adalah mengakui artikel ini sebagai sintesis pedagogis yang berfungsi dengan baik untuk audiens praktisi awal sambil mencatat batas - batas kontribusinya bagi literatur akademis. Empat pengamatan kritis layak ditekankan.

*Pertama*, framing pertanyaan "is it worthwhile" perlu dibaca sebagai kelemahan retorika. Tidak ada lawan bicara yang benar - benar berargumen bahwa analisis pesaing tidak worthwhile. Dengan demikian, struktur argumen mereka mendirikan *straw man*: posisi yang akan dikalahkan tetapi yang sebenarnya tidak diperdebatkan. Pertanyaan yang lebih substantif, yaitu *bagaimana* analisis pesaing harus berubah, *apa* yang menjadi *bottleneck* utama dalam praktik, dan *siapa* yang harus melakukannya, hanya disentuh permukaan.

*Kedua*, argumen pergeseran *dari akuisisi ke sense - making* adalah benar tetapi tidak orisinal. Pergeseran ini sudah didokumentasikan dengan formulasi yang lebih kuat oleh Fleisher dan Bensoussan (2007) dalam *Business and Competitive Analysis* yang menjadi rujukan kanonik literatur *competitive intelligence*. Adom et al. tidak menambahkan dimensi baru pada argumen ini; mereka hanya merangkum dengan kata - kata mereka sendiri.

*Ketiga*, kelalaian atas literatur kognitif adalah kelemahan teoretis paling serius. *Competitor analysis* yang efektif di era *big data* membutuhkan dua kapabilitas yang bersifat komplementer: *kapabilitas akuisisi dan organisasi data* (yang menjadi fokus Adom et al.) dan *kapabilitas interpretasi yang debiased* (yang luput dari pembahasan mereka). Tanpa pertimbangan eksplisit terhadap dimensi kedua, advokasi mereka untuk sistem yang lebih sistematis dapat menyesatkan: sistem yang dirancang dengan baik untuk mengumpulkan dan mengorganisasi data tetap akan menghasilkan kesimpulan yang bias jika manajer yang menafsirkannya beroperasi di bawah perangkap kognitif yang sistematis.

*Keempat*, generalisasi dari konteks Afrika ke konteks global perlu dilakukan dengan kehati - hatian. Beberapa klaim Adom et al. yang tampak universal sebenarnya konteks - bound. Misalnya, pernyataan bahwa "smaller companies cannot afford to conduct competitor analysis" (p. 119) lebih realistis untuk UKM di Ghana yang memiliki margin tipis dan akses terbatas ke layanan profesional dibandingkan UKM di Indonesia yang dapat memanfaatkan platform riset komersial seperti Frost & Sullivan, Statista, atau riset internal *bank syariah* yang sering tersedia secara publik.

Satu pengamatan tambahan tentang struktur artikel: meskipun panjang (12 halaman), distribusi konten tidak proporsional. Bagian Pendahuluan dan *Integrative Literature* (bagian 1 - 2) menjadi mayoritas artikel; bagian Diskusi yang seharusnya menjadi inti analisis kritis hanya menempati dua halaman dan didominasi oleh ringkasan ulang argumen sebelumnya tanpa pengamatan baru yang substantif. Kesan keseluruhan adalah bahwa artikel berfungsi lebih sebagai *literature catalog* daripada *critical synthesis*.

## 8. Implikasi bagi Pemahaman Manajemen Strategik

**Pertama**, untuk mahasiswa Magister Akuntansi, Adom et al. memperkenalkan teknik - teknik praktis (CPM, *competitor array*, tipologi pesaing) yang dapat berguna dalam analisis kompetitif yang sering menjadi bagian dari *audit strategis* atau *due diligence* akuisisi. Pemahaman atas teknik - teknik ini dapat memperkaya kemampuan akuntan manajemen untuk berpartisipasi dalam diskusi strategis di tingkat manajemen senior, di luar peran tradisional yang berfokus pada angka - angka keuangan.

**Kedua**, bagi auditor strategis dan analis investasi di Indonesia, kerangka Adom et al. (sebagaimana diperkaya dengan literatur kognitif yang mereka abaikan) memberi alat untuk mendiagnosis kekuatan analisis pesaing pada perusahaan target. Pertanyaan diagnostik yang relevan: apakah perusahaan memiliki proses *competitor intelligence* yang sistematis ataukah ad - hoc? Apakah informasi pesaing diintegrasikan ke dalam keputusan strategis ataukah hanya dirangkum dalam laporan tahunan tanpa konsekuensi tindakan? Apakah ada kapabilitas interpretasi yang debiased ataukah analisis dipenuhi *overconfidence* manajemen?

**Ketiga**, beberapa contoh paradigmatik dari konteks Indonesia dapat dibaca melalui kerangka kritis ini. *BCA dan Bank Mandiri* memiliki fungsi *strategic intelligence* yang mature; keduanya memonitor pesaing satu sama lain dan terhadap pemain lain (BNI, BRI, bank digital) secara sistematis. Perbedaan kecepatan respons pada pengembangan layanan digital menunjukkan bahwa *kualitas interpretasi* berbeda meskipun *kualitas data* mungkin setara. BCA cenderung lebih agile pada peluncuran fitur digital; ini mengindikasikan bahwa proses dari *intelligence* ke *decision* lebih singkat. Pertanyaan yang relevan: apakah perbedaan ini berasal dari kualitas analisis pesaing, kualitas pengambilan keputusan, atau kombinasi keduanya?

*Indofood* dalam analisis pergerakan Wings Group pada kategori kopi instan (Top Coffee vs Indocafe) dan mie instan (Mie Sedaap vs Indomie) memberikan contoh *competitor analysis* yang melibatkan dimensi distribusi, bukan sekadar produk. Wings Group secara historis kuat pada distribusi *general trade* (warung kelontong, *minimarket* tradisional) yang menjadi backbone pasar Indonesia; tantangan kompetitif Indofood bukan hanya pada produk tetapi pada akses jaringan distribusi. *Competitor analysis* yang efektif dalam konteks ini harus menggali aktivitas distribusi (*value chain* level) yang sering tidak terungkap dalam laporan tahunan.

*E - commerce price - tracking otomatis* (Tokopedia, Shopee, Lazada) mengilustrasikan pergeseran dari analisis manual ke analisis terotomasi. Platform - platform ini secara harian memantau harga pesaing pada produk - produk *fast - moving* dan menyesuaikan penetapan harga sendiri secara dinamis. Pada level ini, *competitor analysis* menjadi proses yang terotomasi pada level data; namun keputusan strategis yang lebih besar (struktur subsidi, prioritas kategori, model fulfillment) tetap *human - mediated*. Pengamatan ini mengonfirmasi kerangka Adom et al. tentang pergeseran dari akuisisi ke *sense - making*: data tersedia berlimpah dan terotomasi, tetapi sense - making yang menentukan strategi tetap menjadi domain manajer senior.

*Garuda Indonesia pada periode pra - AirAsia (1999 - 2003)* adalah contoh klasik *competitor blindspot* dalam terminologi Zajac dan Bazerman (1991). Garuda pada periode itu memperlakukan AirAsia sebagai pesaing kelas bawah yang tidak akan mempengaruhi segmen *full - service* yang menjadi pasar utamanya. Asumsi ini, pada saat itu tampak rasional karena *full - service* dan *low - cost* secara struktural berbeda dalam preferensi pelanggan dan basis biaya. Namun asumsi ini tidak mengantisipasi bahwa *low - cost carriers* akan menggeser ekspektasi harga seluruh industri, termasuk segmen *full - service*. Konsekuensinya, Garuda terlambat menyesuaikan struktur biaya dan segmen pelayanannya, dan kerusakan struktural yang terjadi membutuhkan dekade untuk dipulihkan. Kasus ini adalah ilustrasi bagaimana *competitor analysis* yang fokus pada data (*current strategy*, *capabilities*) tanpa menggali asumsi pesaing dapat menyesatkan secara fatal.

## 9. Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut

**Pertama**, dalam era *big data* dan *machine learning*, sejauh mana analisis pesaing dapat diotomatisasi dan sejauh mana ia tetap menjadi domain *judgment* manusia? Platform e - commerce sudah menjalankan *price tracking* otomatis dengan algoritma penyesuaian dinamis. Bank menggunakan *natural language processing* untuk memonitor *disclosure* regulator atas pesaing. Pertanyaan yang muncul: apakah otomasi ini mengurangi kebutuhan akan analisis manusia, ataukah ia hanya menggeser fokus manusia ke dimensi yang tidak dapat diotomatisasi (*assumptions*, *intent*, *strategic narrative*)? Adom et al. tidak membahas pertanyaan ini secara substantif; ini menjadi ruang penelitian yang menjanjikan.

**Kedua**, bagaimana *competitor analysis* harus dirancang untuk perusahaan kecil dan menengah (UKM) yang tidak memiliki sumber daya untuk fungsi *strategic intelligence* yang formal? Adom et al. mengakui bahwa "smaller companies cannot afford to conduct competitor analysis" tetapi tidak mengembangkan alternatif. Apakah ada kerangka *minimal viable competitor intelligence* yang dapat dijalankan dengan sumber daya terbatas? Apakah teknologi *low - cost* (*Google Alerts*, *social media monitoring* gratis, *industry forums*) dapat menggantikan sebagian fungsi sistem yang formal? Pertanyaan ini sangat relevan untuk konteks Indonesia di mana mayoritas pelaku usaha adalah UKM.

**Ketiga**, dalam konteks BUMN Indonesia yang sebagian beroperasi sebagai *quasi - monopoly* atau dalam segmen yang dilindungi regulasi, apa peran *competitor analysis* yang sebenarnya? Pesaing utama BUMN sering bukan perusahaan lain di Indonesia melainkan dinamika kebijakan pemerintah, perubahan regulasi, dan ekspektasi *stakeholder* politik. Apakah kerangka *competitor analysis* tradisional perlu diperluas dengan dimensi *stakeholder analysis* dan *regulatory intelligence* untuk konteks ini? Pertanyaan ini patut menjadi tesis yang menarik di bidang manajemen strategik publik.

**Keempat**, pertanyaan epistemologis yang lebih dalam: jika *competitor analysis* sering gagal karena bias kognitif dalam interpretasi (sebagaimana literatur Zajac & Bazerman menunjukkan), apa intervensi organisasional yang efektif untuk mengurangi bias tersebut? Apakah *red team analysis*, *war games*, dan *devil's advocate processes* yang Fleisher dan Bensoussan diskusikan benar - benar efektif, ataukah ia hanya menggeser bias dari satu lapisan organisasi ke lapisan lain? Apakah keragaman tim analis (gender, latar belakang industri, masa kerja) mengurangi *blind spots*? Pertanyaan ini mengangkat dimensi *behavioral strategy* yang menjadi cabang literatur strategi yang berkembang pesat tetapi tidak terlibat dalam artikel Adom et al.

**Kelima**, satu pertanyaan praktis untuk audiens mahasiswa Magister Akuntansi: bagaimana akuntan manajemen dan auditor dapat berkontribusi pada *competitor analysis* di luar peran tradisional? Akuntan memiliki akses ke data biaya yang detail, struktur margin pesaing yang dapat diestimasi dari laporan keuangan publik, dan *tracking* indikator finansial yang sering luput dari analis non - keuangan. Bagaimana kapabilitas finansial - analitis ini dapat diintegrasikan dengan *competitor intelligence* yang lebih luas, dan apa yang dapat dipelajari akuntan dari literatur *competitive intelligence* yang sebenarnya sangat aplikatif untuk profesi mereka?
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
        write_md(RMK, "rmk_pert5.md"),
        OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 5.docx",
    )
    pandoc(
        write_md(CR7, "artikel7.md"),
        OUT_CR / "01079_Dzaki Muhammad Yusfian_Artikel 7.docx",
    )
    pandoc(
        write_md(CR8, "artikel8.md"),
        OUT_CR / "01079_Dzaki Muhammad Yusfian_Artikel 8.docx",
    )

    print("\nAll three documents generated successfully.")
    print(f"RMK : {OUT_RMK}")
    print(f"CR  : {OUT_CR}")


if __name__ == "__main__":
    main()
