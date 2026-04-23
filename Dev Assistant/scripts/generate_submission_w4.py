#!/usr/bin/env python3
"""
generate_submission_w4.py
Generates three Word documents for MST304 Pertemuan 4 submission.
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
# DOCUMENT 1 — RMK PERTEMUAN 4
# ══════════════════════════════════════════════════════════════════════════════
RMK = """\
# RINGKASAN MATERI KULIAH

**Pertemuan 4: Evaluating a Company's Resources, Capabilities, and Competitiveness**

**Mata Kuliah:** Manajemen Strategik Kontemporer (MST304)

**Semester:** II, T.A. 2025/2026

**Nama:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Pendahuluan

Pertemuan 4 menjawab pertanyaan yang melengkapi Pertemuan 3. Jika Pertemuan 3 mengkaji lingkungan eksternal—struktur industri, tekanan kompetitif, *driving forces*, dan sinyal makro yang membentuk peta persaingan—maka Pertemuan 4 membalik kaca pembesarnya ke dalam perusahaan. Pertanyaan sentralnya sederhana namun substansial: apa yang sesungguhnya dimiliki perusahaan, seberapa bernilai kepemilikan itu dalam konteks kompetisi, dan apakah kepemilikan itu mampu menjadi fondasi bagi keunggulan yang bertahan di tengah tekanan imitasi?

Topik ini tidak dapat dipahami sebagai rutinitas audit internal. Ia merupakan inti dari sebuah pergeseran paradigmatik dalam pemikiran strategis yang terjadi pada akhir 1980-an dan awal 1990-an, ketika sejumlah ekonom dan teoretikus manajemen menolak pandangan bahwa kinerja superior perusahaan semata-mata ditentukan oleh keberuntungan memilih industri yang atraktif. Mereka menawarkan alternatif: kinerja superior lahir dari *kepemilikan sumber daya dan kapabilitas yang tidak mudah direplikasi oleh pesaing*. Pergeseran inilah yang dikenal sebagai lahirnya *resource-based view* (RBV), dengan artikel Barney (1991) sebagai manifesto intelektualnya.

Bagi mahasiswa program Magister Akuntansi, relevansi materi ini melampaui kerangka analisis strategis murni. Pemahaman tentang apa yang membuat sumber daya bernilai secara strategis berpotongan langsung dengan isu penilaian aset takberwujud, pelaporan keuangan berbasis sumber daya, dan asesmen risiko strategis dalam konteks audit. Auditor dan akuntan manajemen yang memahami kerangka VRIN akan mampu memberikan penilaian yang lebih kaya ketika berhadapan dengan akuisisi, pemeriksaan *goodwill impairment*, dan penilaian *intellectual capital*.

## 2. Dari SWOT ke *Resource-Based View*: Pergeseran Paradigmatik

Kerangka SWOT klasik (Learned, Christensen, Andrews & Guth, 1965) menempatkan analisis internal (kekuatan dan kelemahan) sejajar dengan analisis eksternal (peluang dan ancaman). Selama tiga dekade pertama kehidupan kerangka ini, praktik dominan dalam industri dan akademia bergerak ke arah analisis eksternal—terutama setelah Porter (1980) memformalkan *five forces model*. Konsekuensinya, analisis internal sering direduksi menjadi pendaftaran kekuatan dan kelemahan tanpa disiplin analitis yang memadai.

Kontribusi intelektual terpenting dari tradisi RBV adalah menolak kedangkalan itu. Barney (1991) menyatakan bahwa model lingkungan (Porter dan keturunannya) menyandarkan argumennya pada dua asumsi tersembunyi: bahwa perusahaan dalam satu industri memiliki sumber daya yang homogen, dan bahwa sumber daya dapat berpindah secara sempurna di pasar faktor. Jika kedua asumsi ini benar, maka setiap strategi yang bekerja akan segera ditiru oleh pesaing, dan keunggulan bersaing yang bertahan menjadi mustahil kecuali melalui hambatan industri. Pandangan ini, menurut Barney, menyumbat analisis yang seharusnya justru menjelaskan *mengapa perusahaan dalam industri yang sama memiliki kinerja yang sangat berbeda*.

Tradisi RBV mengganti kedua asumsi tersebut dengan asumsi baru: sumber daya strategis pada dasarnya heterogen antar perusahaan, dan pergerakannya di pasar faktor bersifat imperfek. Di bawah kedua asumsi ini, variasi kinerja dalam industri yang sama bukan lagi anomali yang harus dijelaskan—melainkan konsekuensi wajar dari heterogenitas sumber daya yang bertahan.

Pergeseran paradigmatik ini sekaligus menjelaskan mengapa RBV dan Porter tidak saling menggantikan melainkan saling melengkapi. Analisis eksternal menjelaskan mengapa beberapa industri lebih menguntungkan secara rata-rata dibandingkan industri lain; analisis internal berbasis sumber daya menjelaskan mengapa beberapa perusahaan dalam industri yang sama secara persisten mengungguli pesaingnya. Kedua pertanyaan itu sah, dan keduanya membutuhkan kerangka analisis yang berbeda.

## 3. Analisis Sumber Daya dan Kapabilitas: Kerangka VRIN/VRIO

Kontribusi operasional utama RBV adalah kerangka empat kriteria yang awalnya dikenal sebagai VRIN: *valuable*, *rare*, *imperfectly imitable*, dan *non-substitutable*. Dalam perkembangan selanjutnya, Barney (1995) menyederhanakan kriteria terakhir dan menambahkan dimensi organisasi (O) sehingga lahir VRIO. Keduanya kompatibel secara substantif.

**Valuable.** Sumber daya dikatakan bernilai apabila ia memungkinkan perusahaan memanfaatkan peluang atau menetralisir ancaman di lingkungannya. Definisi ini penting karena ia mengikat konsep sumber daya pada konteks eksternal. Sebuah aset yang secara teknis unik tetapi tidak relevan bagi peluang pasar yang tersedia adalah *sunk cost*, bukan sumber daya dalam pengertian strategis. Kasus klasik yang sering dikutip adalah kepakaran mesin tik di perusahaan yang tidak bergerak di industri pendukung mesin tik—aset ini dulu bernilai, kini tidak.

**Rare.** Sumber daya yang bernilai tetapi lazim dimiliki banyak pesaing hanya menghasilkan *competitive parity*—kondisi di mana perusahaan setara dengan pesaingnya, bukan unggul. Kelangkaan bukan sekadar kuantitas, melainkan distribusi relatif di dalam industri. Sebuah sumber daya tidak perlu dimiliki hanya oleh satu perusahaan untuk disebut langka; cukup jumlah pemiliknya lebih sedikit daripada jumlah yang diperlukan untuk menciptakan dinamika kompetisi sempurna di pasar.

**Imperfectly Imitable.** Kriteria inilah yang membuat kerangka RBV memiliki kedalaman teoretis. Barney mengidentifikasi tiga sumber imperfeksi imitasi yang saling terkait tetapi berbeda secara konseptual. *Pertama*, kondisi historis yang unik (*unique historical conditions*)—sumber daya tertentu hanya dapat diakumulasi melalui jalur historis yang tidak dapat diulang. Reputasi Coca-Cola sebagai simbol Amerika tidak dapat dibangun kembali dari nol oleh perusahaan mana pun; jalur pembangunannya membutuhkan lebih dari satu abad dalam konteks budaya global abad ke-20. *Kedua*, ambiguitas kausal (*causal ambiguity*)—hubungan antara sumber daya dan keunggulan bersaing tidak jelas, bahkan bagi perusahaan yang mengalaminya. Ketika imitator tidak tahu persis apa yang harus ditiru, imitasi menjadi sulit. *Ketiga*, kompleksitas sosial (*social complexity*)—sumber daya tertanam dalam jaringan relasi, budaya, dan norma interpersonal yang tidak dapat dibeli atau direkayasa secara langsung. Kepercayaan antar departemen, kultur kerja yang telah mengendap selama dekade, dan jejaring pemasok yang terbangun melalui interaksi berulang termasuk dalam kategori ini.

**Non-substitutable.** Kriteria terakhir mengingatkan bahwa imperfeksi imitasi tidak cukup. Sumber daya yang tidak dapat ditiru secara teknis tetap akan kehilangan nilainya apabila tersedia alternatif strategis yang secara fungsional setara. Barney sendiri memberi contoh yang cerdas: sebuah tim manajemen puncak berkualitas tinggi (VRI) dapat digantikan secara substitutif oleh sistem perencanaan formal yang baik, apabila keduanya menghasilkan kualitas pengambilan keputusan yang setara.

Keempat kriteria ini bekerja sebagai filter berurutan. Sumber daya yang tidak *valuable* langsung tersingkir; yang *valuable* tapi umum hanya menghasilkan *parity*; yang *valuable* dan *rare* menghasilkan keunggulan sementara; hanya sumber daya yang memenuhi keempat kriteria secara simultan yang berpotensi menjadi fondasi keunggulan bersaing yang bertahan.

## 4. *Dynamic Capabilities*: Respons terhadap Lingkungan yang Turbulen

Kritik yang paling konstruktif terhadap RBV klasik datang dari Teece, Pisano, dan Shuen (1997) melalui kerangka *dynamic capabilities*. Inti kritik mereka tidak menyangkal validitas VRIN, tetapi menunjukkan bahwa dalam lingkungan yang bergerak cepat, sumber daya VRIN hari ini dapat menjadi tidak relevan dalam lima hingga sepuluh tahun. RBV klasik, karena fokus pada kondisi ekuilibrium, kurang menjelaskan bagaimana perusahaan memperbarui portofolio sumber dayanya seiring perubahan lingkungan.

Kerangka *dynamic capabilities* mendefinisikan kapabilitas dinamis sebagai "kemampuan perusahaan untuk mengintegrasikan, membangun, dan merekonfigurasi kompetensi internal dan eksternal guna menghadapi lingkungan yang berubah cepat." Tiga kapabilitas yang ditonjolkan oleh Teece (2007) adalah *sensing* (mendeteksi peluang dan ancaman baru), *seizing* (memobilisasi sumber daya untuk menangkap peluang yang terdeteksi), dan *transforming* (mengatur ulang basis sumber daya secara berkelanjutan).

Kerangka ini penting secara praktis bagi perusahaan di industri yang menghadapi disrupsi digital. Kasus Kodak, Nokia, dan Blockbuster menunjukkan bahwa kepemilikan sumber daya VRIN yang dulunya kuat tidak menjamin kelangsungan apabila perusahaan gagal mengembangkan kapabilitas untuk mendeteksi dan merespons pergeseran teknologis. Di konteks Indonesia, transisi perbankan konvensional ke perbankan digital memberikan laboratorium alami bagi pembelajaran ini. BCA, misalnya, mampu mempertahankan posisinya tidak semata karena franchise CASA-nya kuat (aset VRIN), melainkan karena ia menunjukkan kapabilitas dinamis untuk mengembangkan BCA Mobile dan BCA Digital sebelum tekanan disrupsi memaksa perubahan.

## 5. Analisis *Value Chain* dan *Activity-Based Costing*

Porter (1985) menyumbangkan kerangka yang komplementer terhadap RBV: *value chain*. Jika RBV melihat perusahaan sebagai kumpulan sumber daya, *value chain* melihat perusahaan sebagai kumpulan aktivitas yang saling terkait dalam menghasilkan nilai bagi pelanggan. Kerangka ini membagi aktivitas perusahaan menjadi *primary activities* (logistik masuk, operasi, logistik keluar, pemasaran dan penjualan, pelayanan) dan *support activities* (infrastruktur perusahaan, manajemen SDM, pengembangan teknologi, pengadaan).

Kekuatan *value chain* adalah kemampuannya menjadikan analisis biaya dan diferensiasi sebagai latihan yang terdisiplin. Setiap aktivitas dapat dibandingkan dengan *benchmark* industri, sehingga manajemen dapat mengidentifikasi aktivitas yang biayanya tidak kompetitif atau yang berpotensi menjadi sumber diferensiasi. TPGS menekankan bahwa analisis *value chain* paling bermakna apabila digabung dengan *activity-based costing*, yang mengalokasikan biaya ke aktivitas spesifik dan bukan sekadar ke pusat biaya tradisional.

Kaitannya dengan RBV: aktivitas yang biaya relatifnya rendah atau kualitasnya tinggi menunjuk pada kemungkinan adanya sumber daya atau kapabilitas mendasar yang memungkinkan aktivitas itu berjalan lebih efisien. Analisis *value chain* dengan demikian menjadi alat diagnostik untuk menemukan kandidat VRIN, bukan alternatif bagi RBV.

## 6. SWOT yang Diperdalam: dari Daftar menjadi Analisis Strategis

TPGS Ch.4 menolak SWOT versi kosmetik—matriks empat kuadran yang diisi dengan *bullet point* tanpa analisis lanjutan. SWOT yang berguna secara strategis adalah SWOT yang dikerjakan secara berurutan: (1) identifikasi kekuatan berbasis VRIN yang terbukti; (2) identifikasi kelemahan yang menghambat eksekusi strategi yang tersedia; (3) identifikasi peluang yang sesuai dengan kekuatan dan dapat dijangkau; (4) identifikasi ancaman yang mempertaruhkan basis sumber daya.

Langkah kritis yang sering dilewatkan adalah *pemetaan silang*: bagaimana kekuatan dapat digunakan untuk mengejar peluang, bagaimana kelemahan membuka pintu bagi ancaman, dan bagaimana kekuatan dapat melindungi dari ancaman. SWOT yang tidak menghasilkan pemetaan silang seperti itu hanya menghasilkan daftar deskriptif, bukan diagnosis strategis.

## 7. Analisis Kekuatan Kompetitif (*Competitive Strength Assessment*)

TPGS Ch.4 memperkenalkan teknik *competitive strength assessment* yang memanfaatkan pembobotan tertimbang pada faktor-faktor sukses kritis (*key success factors*) dalam industri. Untuk setiap faktor—misalnya kualitas produk, jangkauan distribusi, kapabilitas inovasi, struktur biaya, dan reputasi merek—manajemen menilai posisi perusahaan relatif terhadap pesaing utamanya pada skala numerik, kemudian mengalikan skor dengan bobot faktor.

Teknik ini sederhana tetapi disiplin analitisnya tidak boleh diremehkan. Ia memaksa manajemen mengartikulasikan (a) faktor apa yang paling menentukan sukses di industri spesifiknya, (b) bagaimana posisi perusahaan relatif terhadap pesaing konkret, dan (c) di mana prioritas peningkatan harus ditempatkan. Hasilnya adalah peta kompetitif yang tertimbang, yang mempertajam diskusi strategis di tingkat dewan direksi.

## 8. Mendiagnosis Masalah Strategis yang Perlu Ditangani

Tahap akhir analisis internal adalah menerjemahkan temuan-temuan dari langkah sebelumnya menjadi pernyataan yang jernih tentang *apa yang harus ditangani oleh strategi baru*. TPGS menekankan bahwa diagnosis ini harus spesifik dan dapat ditindaklanjuti. Pernyataan seperti "perusahaan perlu meningkatkan daya saingnya" tidak memadai; ia perlu diganti dengan pernyataan seperti "perusahaan kehilangan 3 persentase pangsa pasar pada segmen X dalam tiga tahun terakhir karena jarak harga terhadap pesaing Y telah menyempit."

Diagnosis yang baik mengintegrasikan analisis eksternal dari Pertemuan 3 dan analisis internal dari Pertemuan 4. Ia menjadi jembatan ke Pertemuan 5 dan seterusnya, yaitu pemilihan strategi generik yang akan diangkat sebagai respons.

## 9. Kesimpulan

Pertemuan 4 melengkapi kerangka analitis yang dibangun sejak Pertemuan 1. Dengan memahami bahwa sumber daya dan kapabilitas yang heterogen dan sulit ditiru adalah fondasi dari keunggulan bersaing yang bertahan, mahasiswa diperlengkapi dengan bahasa analitis untuk mengurai mengapa perusahaan dengan produk yang mirip dapat memiliki kinerja yang jauh berbeda.

Dua artikel yang menyertai pertemuan ini mewakili dua sisi dari percakapan teoretis yang sama. Barney (1991) membangun kerangka RBV secara sistematis dan menyediakan bahasa operasional yang masih dominan hingga hari ini. Hao Ma (2000) menyodorkan kritik meta yang tidak menolak RBV, tetapi mengingatkan bahwa keunggulan bersaing tidak otomatis menghasilkan kinerja superior. Keduanya membangun kesadaran bahwa analisis strategis yang matang harus membedakan antara apa yang *secara struktural dimiliki perusahaan* dan apa yang *secara aktual diraih perusahaan di pasar*—dua hal yang dalam literatur awam sering dipertukarkan tanpa teliti.
"""


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT 2 — CRITICAL REVIEW ARTIKEL 5 (BARNEY 1991)
# ══════════════════════════════════════════════════════════════════════════════
CR5 = """\
# CRITICAL REVIEW ARTIKEL 5

**Mata Kuliah:** Manajemen Strategik Kontemporer (MST304)

**Semester:** II, T.A. 2025/2026

**Nama:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Identitas Artikel

**Judul:** *Firm Resources and Sustained Competitive Advantage*

**Penulis:** Jay B. Barney

**Institusi saat publikasi:** Texas A&M University (kemudian pindah ke Ohio State University, dan selanjutnya University of Utah)

**Publikasi:** *Journal of Management*, Vol. 17 No. 1 (1991), hlm. 99–120

**Tipe Penelitian:** Artikel konseptual/teoretis

**Catatan posisi akademik:** Artikel ini adalah salah satu karya paling berpengaruh dalam sejarah ilmu manajemen strategik, dengan jumlah sitasi yang melampaui seratus ribu. Ia menjadi rujukan kanonik bagi hampir semua karya berikutnya yang berbicara tentang keunggulan bersaing berbasis sumber daya.

## 2. Tujuan Penelitian dan Posisi dalam Literatur

Barney (1991) menulis dalam konteks intelektual yang sangat spesifik. Pada akhir 1980-an, pemikiran dominan dalam manajemen strategik—diwakili terutama oleh Porter (1980, 1985)—memfokuskan analisis pada struktur industri sebagai determinan kinerja perusahaan. Kerangka *structure-conduct-performance* yang diwarisi dari ekonomi industri Mason-Bain mengasumsikan, secara implisit, bahwa perusahaan dalam industri yang sama memiliki sumber daya yang homogen dan bahwa sumber daya strategis dapat diperdagangkan secara bebas di pasar faktor. Dari asumsi-asumsi ini mengalir implikasi besar: perusahaan yang unggul adalah perusahaan yang berhasil memosisikan dirinya dalam industri yang menguntungkan dan melindungi posisinya melalui hambatan masuk.

Tujuan Barney dalam artikel ini adalah menyodorkan alternatif paradigmatik. Ia ingin menjawab pertanyaan yang tidak terjawab dengan memadai oleh tradisi Porter: mengapa terdapat variasi kinerja yang persisten *di dalam* industri yang sama? Jawabannya mengandaikan pembalikan asumsi: sumber daya perusahaan tidak homogen, dan tidak sepenuhnya mobile di pasar faktor. Dari kedua asumsi alternatif inilah Barney membangun argumentasi bahwa keunggulan bersaing yang bertahan harus dicari pada karakteristik sumber daya internal perusahaan, bukan semata pada posisi industri.

Posisi Barney dalam literatur dengan demikian bukan sebagai penyanggah Porter, melainkan sebagai pembangun paradigma pelengkap yang mengisi ruang analitis yang ditinggalkan oleh tradisi *industrial organization*. Dalam artikelnya sendiri, Barney secara hati-hati menyatakan bahwa kedua pendekatan bersifat komplementer: analisis lingkungan menjelaskan mengapa industri tertentu menguntungkan, sementara *resource-based view* menjelaskan mengapa perusahaan tertentu dalam industri itu mengungguli pesaingnya.

## 3. Argumen Utama: Dua Asumsi dan Empat Kriteria

Arsitektur argumen Barney bertumpu pada dua pilar. Pilar pertama adalah *dua asumsi fondasional*: heterogenitas sumber daya di antara perusahaan dalam industri yang sama, dan imobilitas sumber daya di pasar faktor. Kedua asumsi ini bekerja bersama secara logis: tanpa heterogenitas, tidak mungkin ada variasi kinerja persisten; tanpa imobilitas, heterogenitas akan segera hilang ketika sumber daya berpindah tangan di pasar.

Pilar kedua adalah *empat kriteria operasional* yang mengidentifikasi sumber daya mana yang berpotensi menjadi fondasi keunggulan bersaing bertahan. Keempat kriteria tersebut—*value*, *rarity*, *imperfect imitability*, dan *non-substitutability*—kemudian dikenal sebagai VRIN. Barney menjabarkan masing-masing dengan presisi:

Sebuah sumber daya *bernilai* apabila ia memungkinkan perusahaan memanfaatkan peluang pasar atau menetralisir ancaman kompetitif. Definisi ini secara cerdik mengikat konsep sumber daya pada konteks eksternal—sebuah gerak yang mencegah RBV terperangkap dalam introspeksi murni.

Sebuah sumber daya *langka* apabila jumlah perusahaan yang memilikinya lebih sedikit dari jumlah yang diperlukan untuk menghasilkan dinamika kompetisi sempurna. Kriteria ini lebih nuansawi daripada sekadar "unik"; ia mengakui bahwa kelangkaan relatif sudah cukup.

Sebuah sumber daya *tidak sempurna untuk ditiru* karena salah satu atau kombinasi dari tiga sebab: kondisi historis yang unik, ambiguitas kausal, atau kompleksitas sosial. Ketiga sebab ini bekerja sebagai mekanisme perlindungan terhadap imitasi oleh pesaing.

Sebuah sumber daya *tidak tergantikan* apabila tidak ada sumber daya lain yang secara strategis ekivalen yang dapat digunakan pesaing untuk menghasilkan nilai yang sama. Barney menekankan bahwa substitusi tidak perlu identik; cukup setara secara fungsional.

Kontribusi teoretis terpenting dari Barney bukan sekadar menyediakan daftar kriteria, tetapi mendefinisikan *sustained competitive advantage* sebagai konsep ekuilibrium. Menurutnya, keunggulan bersaing dikatakan bertahan bukan karena ia berlangsung untuk durasi kalender tertentu, melainkan karena upaya pesaing untuk menduplikasinya telah berhenti—dan tetap demikian. Definisi ini elegan secara analitis karena ia memindahkan perdebatan dari perhitungan waktu yang arbitrer ke pertanyaan tentang kondisi kesetimbangan kompetitif.

## 4. Koneksi ke Topik Silabus (Pertemuan 4 — TPGS Ch.4)

Artikel Barney adalah teks induk bagi seluruh analisis internal yang diajarkan dalam TPGS Ch.4. Semua konsep yang digunakan dalam Ch.4—identifikasi sumber daya yang bernilai, penilaian kelangkaan dan imitasi, asesmen kekuatan kompetitif—secara intelektual turun dari kerangka yang dibangun Barney. Tanpa membaca Barney dalam bentuk aslinya, mahasiswa hanya akan belajar *cara menggunakan* VRIN tetapi tidak memahami *mengapa kerangka itu valid secara teoretis*.

Asumsi heterogenitas dan imobilitas, yang sering dilewatkan dalam aplikasi praktis Ch.4, merupakan premis kritikal. Apabila seorang praktisi berasumsi bahwa sumber daya strategis mobile dan homogen—misalnya ketika memperlakukan "talenta digital" sebagai komoditas yang dapat direkrut bebas—maka aplikasinya terhadap kerangka VRIN akan menjadi dangkal atau sesat.

Di sisi lain, pemahaman atas artikel Barney juga membantu mahasiswa menempatkan tempat RBV di dalam ekosistem teori yang lebih luas. Karya-karya penting seperti *dynamic capabilities* (Teece, Pisano & Shuen 1997), *knowledge-based view* (Grant 1996), *relational view* (Dyer & Singh 1998), dan *microfoundations of capabilities* (Felin & Foss 2005) adalah respons intelektual terhadap Barney. Tanpa landasan pada teks asli, mahasiswa tidak dapat mengikuti percakapan teoretis yang terus berlangsung dalam literatur kontemporer.

## 5. Kekuatan Artikel

Kekuatan pertama yang patut disorot adalah **kejelasan arsitektur argumen**. Barney menata argumennya dengan disiplin logis yang eksemplar: ia mulai dari asumsi, turun ke definisi, lanjut ke implikasi, dan menutup dengan aplikasi pada tiga studi kasus (*strategic planning*, *information processing systems*, dan *positive reputation*). Struktur ini memudahkan pembaca mengikuti rantai nalar dan mengidentifikasi titik-titik di mana ia mungkin ingin setuju atau tidak.

Kekuatan kedua adalah **bahasa operasional yang ringkas namun presisi**. Sebelum Barney, klaim bahwa "perusahaan unggul karena sumber dayanya unik" sering dikemukakan tanpa disiplin analitis. Dengan menyodorkan empat kriteria yang dapat diuji secara terstruktur, Barney mengubah kosakata strategis menjadi alat yang dapat digunakan dalam diskusi manajerial yang serius. Singkatan VRIN (dan kemudian VRIO) bukan sekadar kemudahan mnemonik; ia adalah protokol analisis.

Kekuatan ketiga adalah **definisi ekuilibrium dari sustained competitive advantage**. Dengan mengikat konsep ini pada kondisi berhentinya upaya duplikasi, Barney menghindari perangkap yang sering dialami literatur lain: berdebat tentang berapa tahun "bertahan" harus berarti. Definisi ekuilibriumnya memindahkan fokus ke pertanyaan struktural tentang kondisi kompetisi, yang jauh lebih bermanfaat secara analitis.

Kekuatan keempat adalah **pengangkatan pentingnya sumber daya tacit dan sosial-kompleks**. Dengan memasukkan kompleksitas sosial sebagai salah satu sumber imperfeksi imitasi, Barney memberi ruang teoretis yang sah bagi aset-aset yang sulit dikodifikasi—budaya perusahaan, relasi antarmanajer, kepercayaan pemasok, jejaring distribusi yang berlangsung selama dekade. Ini membuka pintu bagi perkembangan *knowledge-based view* dan teori pembelajaran organisasional pada tahun-tahun berikutnya.

## 6. Keterbatasan dan Kelemahan

**Pertama, problem tautologi.** Kritik paling substansial datang dari Priem dan Butler (2001). Mereka menunjuk pada kecenderungan definisi Barney berubah menjadi tautologi operasional. Pernyataan "sumber daya yang VRIN menghasilkan keunggulan bersaing yang bertahan" dalam praktik sering dibalik menjadi alat diagnosis *post hoc*: kita menyimpulkan bahwa sebuah sumber daya adalah VRIN *karena* kita mengamati keunggulan bersaing yang bertahan. Logika seperti ini membuat klaim Barney menjadi sulit dibantah secara empiris (*non-falsifiable*), yang merupakan masalah mendasar dalam sebuah proposisi teoretis.

**Kedua, paradoks ambiguitas kausal.** Konsep *causal ambiguity* yang ditawarkan Barney sebagai sumber imperfeksi imitasi mengandung ketegangan yang menarik. Agar ambiguitas kausal berfungsi sebagai pelindung, bahkan perusahaan yang beruntung memiliki sumber daya tersebut harus *tidak sepenuhnya memahami* mengapa ia unggul. Jika ia paham, maka pengetahuan itu cepat atau lambat akan terdifusi melalui pergerakan manajer atau studi sistematis oleh pesaing. Ini menempatkan manajemen pada posisi epistemologis yang janggal: mereka tidak seharusnya terlalu paham akan sumber kesuksesannya sendiri. Konsekuensinya: pengembangan sumber daya yang sengaja berbasis ambiguitas kausal hampir mustahil secara logis.

**Ketiga, karakter statis dari kerangka.** Barney membangun argumennya dalam kerangka ekuilibrium, yang secara implisit mengasumsikan lingkungan stabil. Di lingkungan yang bergerak cepat—industri teknologi digital, *fintech*, platform berbasis algoritma—sumber daya VRIN hari ini dapat menjadi usang dalam hitungan tahun. RBV klasik tidak memiliki instrumen analitis untuk menjelaskan bagaimana perusahaan memperbarui basis sumber dayanya. Kerangka *dynamic capabilities* dari Teece et al. (1997) dikembangkan persis untuk mengisi kesenjangan ini, sebuah pengakuan implisit atas keterbatasan RBV klasik.

**Keempat, kurang perhatian pada akuisisi sumber daya.** Peteraf (1993) menunjukkan bahwa RBV Barney terutama mengulas apa yang terjadi *setelah* perusahaan memiliki sumber daya VRIN, tetapi kurang mendalami proses *bagaimana sumber daya itu diakuisisi*. Peteraf mengembangkan gagasan *ex ante limits to competition*—kondisi bahwa biaya akuisisi sumber daya tidak boleh menelan seluruh *rent* ekonomi yang akan dihasilkan nanti. Tanpa mempertimbangkan harga akuisisi, analisis VRIN dapat menyesatkan; sebuah sumber daya VRIN yang dibeli dengan harga yang sudah mencerminkan seluruh nilai masa depannya tidak akan menghasilkan *rent* bagi pembelinya.

**Kelima, reduksi organisasi menjadi kumpulan sumber daya.** Kritik yang lebih halus datang dari tradisi teori organisasi (Donaldson 1990). Barney cenderung memperlakukan perusahaan sebagai kontainer bagi sumber daya, tanpa secara memadai menangani bagaimana struktur organisasi, proses pengambilan keputusan, dan politik internal membentuk cara sumber daya itu diterjemahkan ke dalam tindakan. Pengenalan "O" (organizational support) dalam versi VRIO-nya pada 1995 adalah tanggapan parsial, tetapi kritik teori organisasi terhadap asumsi atomistik RBV tetap relevan.

## 7. Evaluasi Kritis

Menimbang kekuatan dan kelemahan di atas, posisi yang adil adalah mengakui kontribusi Barney sebagai landmark intelektual sekaligus mencatat bahwa kerangka yang ia bangun adalah *starting point*, bukan *endpoint*. Tiga pengamatan kritis layak ditekankan.

**Pertama**, masalah tautologi tidak sepenuhnya mendiskualifikasi Barney. Barney dalam respons-respons selanjutnya berargumen bahwa VRIN dapat diuji secara empiris apabila sumber daya diidentifikasi *ex ante* (melalui analisis struktural independen) dan kemudian diuji secara prediktif terhadap kinerja. Dalam praktiknya, penelitian empiris RBV memang berhasil mendemonstrasikan korelasi antara kepemilikan sumber daya VRI dan kinerja superior (misalnya studi-studi pada industri farmasi, teknologi informasi, dan jasa keuangan). Namun kehati-hatian metodologis tetap diperlukan: peneliti harus menghindari operasionalisasi sirkular.

**Kedua**, kritik tentang ambiguitas kausal menunjuk pada problem yang mendalam tetapi tidak fatal. Apabila kita menerima bahwa ambiguitas kausal adalah fenomena probabilistik—bukan semua-atau-tidak-sama-sekali—maka argumen Barney masih berfungsi. Manajemen dapat *sebagian* memahami sumber kesuksesannya tanpa harus sepenuhnya memahaminya, dan kompleksitas sistem tetap mempertahankan bagian yang tidak terjangkau oleh imitator. Penafsiran ini lebih dapat dipertahankan daripada versi kuat yang dibangun dalam teks asli.

**Ketiga**, keterbatasan dalam lingkungan dinamis telah direspons dengan baik oleh literatur berikutnya. Kerangka *dynamic capabilities* tidak menggantikan RBV tetapi melengkapinya: perusahaan perlu memiliki sumber daya VRIN *dan* kapabilitas untuk memperbarui basis sumber dayanya. Pembacaan modern RBV karena itu jarang berhenti pada Barney (1991) saja; ia dibaca bersama Teece et al. (1997), Eisenhardt & Martin (2000), dan Helfat et al. (2007).

Satu pengamatan tambahan yang perlu dibuka: Barney cenderung bersikap seolah-olah sumber daya adalah sesuatu yang *dimiliki* oleh perusahaan. Perspektif kontemporer, terutama dari *relational view* (Dyer & Singh 1998) dan *ecosystem perspective* (Jacobides et al. 2018), menunjukkan bahwa banyak sumber daya strategis yang berharga sesungguhnya *dibagi* dalam jaringan mitra, pemasok, dan pelanggan. Dalam era platform dan ekosistem digital, batas perusahaan menjadi kabur; model RBV yang berpusat pada batas perusahaan mungkin memerlukan revisi konseptual yang lebih jauh.

## 8. Implikasi bagi Pemahaman Manajemen Strategik

**Pertama**, artikel Barney menyediakan kosakata analitis yang dibutuhkan untuk diskusi strategi yang matang. Setiap pernyataan bahwa sebuah perusahaan "memiliki keunggulan" harus diuji dengan empat pertanyaan: apakah sumber daya yang dimaksud bernilai dalam konteks pasar saat ini, langka dibandingkan pesaing, sulit ditiru, dan tidak tergantikan? Disiplin bertanya seperti ini menghindarkan diskusi strategis dari retorika kosong.

**Kedua**, bagi manajer Indonesia, kerangka Barney berguna untuk mendiagnosis kandidat keunggulan bersaing di perusahaan. Contoh yang layak dibahas: *customer deposit franchise* BCA—tabungan berbiaya rendah yang terakumulasi selama dekade melalui kombinasi kepercayaan publik, jaringan cabang, dan efek *switching cost*—memenuhi keempat kriteria VRIN dengan cukup jelas. Sebaliknya, klaim bahwa "budaya inovasi" adalah keunggulan bersaing tanpa adanya proses sistematis R&D, eksperimen, dan *scaling* biasanya tidak lulus uji imperfeksi imitasi.

**Ketiga**, bagi auditor dan akuntan manajemen, kerangka ini memberi dasar konseptual untuk menilai aset takberwujud secara lebih disiplin. Pengujian *impairment* *goodwill* pasca-akuisisi, misalnya, akan lebih bermakna apabila didahului oleh analisis VRIN terhadap sumber daya strategis yang menjadi basis *goodwill* itu. Apabila sumber daya strategis tidak lagi bernilai atau telah kehilangan imperfeksi imitasinya, indikasi *impairment* menjadi lebih kuat.

**Keempat**, implikasi bagi kebijakan publik juga tidak sepele. Perdebatan tentang *holding BUMN* dan restrukturisasi badan usaha negara di Indonesia dapat diperjelas dengan pertanyaan VRIN: apa sumber daya strategis yang sesungguhnya dimiliki oleh BUMN tertentu, apakah sumber daya itu bertahan di pasar bebas, dan apakah konsolidasi holding memperkuat atau justru mengencerkan basis sumber daya itu?

## 9. Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut

**Pertama**, seberapa jauh kerangka RBV yang dikembangkan untuk perusahaan-perusahaan di ekonomi maju 1991 masih relevan untuk perusahaan Indonesia pada 2026, ketika struktur pasar tenaga kerja, pasar modal, dan pasar teknologi sangat berbeda? Apakah asumsi imobilitas sumber daya, misalnya, berlaku dengan cara yang sama ketika pasar talenta digital di Jakarta bersifat sangat cair dan lintas perusahaan?

**Kedua**, bagaimana seharusnya konsep "sumber daya" diperluas dalam era ekosistem dan platform? Ketika sebuah perusahaan seperti GoTo atau Tokopedia bersandar pada jaringan mitra (driver, *merchant*, mitra logistik) yang tidak secara hukum dimiliki, apakah jaringan itu dapat disebut sumber daya perusahaan dalam pengertian Barney? Jika tidak, bagaimana kita menganalisis keunggulan bersaing yang secara jelas berada di wilayah ini?

**Ketiga**, dalam konteks BUMN Indonesia, seberapa banyak "keunggulan" yang dimiliki BUMN adalah produk dari proteksi regulasi (hak monopoli, tarif khusus, *mandatory assignment*) dibandingkan produk dari sumber daya VRIN yang sesungguhnya? Pertanyaan ini sangat praktis untuk evaluasi kebijakan privatisasi dan restrukturisasi BUMN—dan juga secara konseptual memperluas kerangka Barney ke wilayah yang jarang ia sentuh sendiri.
"""


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT 3 — CRITICAL REVIEW ARTIKEL 6 (HAO MA 2000)
# ══════════════════════════════════════════════════════════════════════════════
CR6 = """\
# CRITICAL REVIEW ARTIKEL 6

**Mata Kuliah:** Manajemen Strategik Kontemporer (MST304)

**Semester:** II, T.A. 2025/2026

**Nama:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Identitas Artikel

**Judul:** *Competitive Advantage and Firm Performance*

**Penulis:** Hao Ma

**Institusi saat publikasi:** Bryant College, Smithfield, Rhode Island (sebelumnya University of Illinois at Urbana-Champaign, doktoral di University of Texas at Austin)

**Publikasi:** *Competitiveness Review: An International Business Journal*, Vol. 10 No. 2 (2000), hlm. 15–32

**Tipe Penelitian:** Artikel konseptual berbasis tinjauan literatur, diarahkan pada klarifikasi konstruk teoretis

## 2. Tujuan Penelitian dan Posisi dalam Literatur

Hao Ma menulis artikel ini dengan kesadaran bahwa istilah *competitive advantage* telah menjadi salah satu kata yang paling banyak digunakan dalam literatur manajemen strategik, sekaligus salah satu yang paling longgar didefinisikan. Dua tradisi dominan pada pergantian milenium—pendekatan struktural (Porter) dan *resource-based view* (Barney, Wernerfelt, Rumelt)—sama-sama menggunakan istilah ini sebagai inti argumennya, tetapi keduanya cenderung memperlakukannya secara bergantian dengan *firm performance*. Konsekuensinya, pertanyaan inti ilmu manajemen strategik—yaitu "mengapa perusahaan berbeda dalam kinerjanya"—menjadi sirkular karena variabel independen dan variabel dependennya tidak dapat dibedakan secara operasional.

Tujuan Hao Ma adalah memulihkan disiplin konseptual: memisahkan *competitive advantage* dari *firm performance* sebagai dua konstruk yang berbeda, dan kemudian mengeksplorasi secara sistematis bagaimana keduanya berhubungan. Ia merumuskan tiga observasi sebagai landasan argumen: (1) keunggulan bersaing tidak sama dengan kinerja superior; (2) keunggulan bersaing adalah istilah relasional yang mensyaratkan titik referensi; (3) keunggulan bersaing bersifat kontekstual dan tidak dapat dinilai terlepas dari situasi kompetitifnya.

Posisi Hao Ma dalam literatur adalah sebagai kritikus yang konstruktif, bukan penyanggah paradigma. Ia tidak menolak RBV atau pendekatan struktural; ia menolak penggunaannya yang serampangan. Artikelnya adalah ajakan untuk kebersihan konseptual—sebuah kontribusi yang, meski sering disepelekan dalam literatur aplikatif, memiliki dampak metodologis yang signifikan.

## 3. Argumen Utama: Tiga Observasi dan Kerangka Relasional

Argumen Hao Ma berbentuk spiral menurun dari tesis umum ke kerangka operasional. Spiral pertama membuka dengan tiga observasi fondasional. Pertama, keunggulan bersaing dan kinerja perusahaan adalah dua konstruk yang berbeda: keunggulan bersaing adalah karakteristik struktural yang menunjuk pada posisi relatif, sementara kinerja adalah hasil yang terealisasi dan dapat diukur. Keduanya dihubungkan oleh rantai kausal yang panjang dan rawan kegagalan.

Kedua, keunggulan bersaing bersifat relasional. Pernyataan "perusahaan A memiliki keunggulan bersaing" tidak bermakna tanpa titik referensi yang eksplisit: unggul dibandingkan siapa, pada dimensi apa. Hao Ma mendefinisikan ulang *competitive advantage* sebagai "*the differential between two competitors on any conceivable dimension that allows one to better create customer value than the other*"—diferensial antara dua pesaing pada dimensi apa pun yang memungkinkan salah satunya menghasilkan nilai pelanggan yang lebih baik. Definisi ini mengikat keunggulan bersaing pada tiga elemen yang harus disebutkan: *against whom*, *on what*, dan *for whom*.

Ketiga, keunggulan bersaing bersifat kontekstual. Apa yang merupakan kekuatan dalam satu konteks kompetitif dapat menjadi kelemahan dalam konteks yang berbeda. Hao Ma mengutip Grant (1998) yang menyodorkan contoh Michael Eisner di Walt Disney: apakah ia kekuatan atau kelemahan perusahaan? Jawabannya tergantung konteks—sebagai pemimpin visioner yang menggerakkan kebangkitan Disney, ia adalah kekuatan; sebagai eksekutif yang bermasalah secara kesehatan dan gagal mengatur suksesi, ia menjadi risiko. Kontekstualitas ini membuat penilaian keunggulan bersaing selalu situasional.

Spiral kedua turun ke pembedaan antara *discrete competitive advantage* dan *compound competitive advantage*. Keunggulan diskret adalah keuntungan pada satu dimensi spesifik—lokasi yang lebih strategis, teknologi yang lebih canggih, brand yang lebih kuat. Keunggulan komposit adalah kombinasi beberapa keunggulan diskret yang bekerja secara integratif. Hao Ma menggunakan Wal-Mart sebagai ilustrasi: keunggulan biaya Wal-Mart adalah komposit dari lokasi, teknologi informasi, sistem gudang dan transportasi, serta budaya korporat—semua bekerja bersama. Keunggulan diskret yang terisolasi, menurutnya, terlalu jauh dari kinerja pada rantai kausal; hubungan mereka dengan kinerja akan dihimpit oleh faktor-faktor *noise* sepanjang rantai.

Spiral ketiga turun ke tiga skenario hubungan antara keunggulan bersaing dan kinerja. Skenario pertama adalah yang klasik: keunggulan bersaing menghasilkan kinerja superior. Skenario kedua, yang oleh Hao Ma dianggap paling sering diabaikan literatur, adalah keunggulan bersaing *tanpa* kinerja superior. Skenario ketiga, yang juga sering dilupakan, adalah kinerja superior *tanpa* keunggulan bersaing.

Pada skenario kedua, Hao Ma mengidentifikasi empat sub-situasi. Pertama, keunggulan diskret yang gagal berkembang menjadi keunggulan komposit. Kedua, keunggulan besar yang tidak sepenuhnya dieksploitasi—contoh ikoniknya adalah Xerox PARC yang mengembangkan *graphic user interface* tetapi gagal membawanya ke pasar komersial sehingga Apple dan Microsoft yang menuai. Ketiga, kombinasi keunggulan yang tidak tepat—Apple pada awal 1990-an unggul dalam inovasi dan diferensiasi tetapi tidak mampu membangun keunggulan biaya dan standar industri, sehingga tergilas Microsoft. Keempat, pengorbanan keunggulan yang dilakukan secara sadar karena pertimbangan strategis lain—Microsoft memberikan perlakuan istimewa bagi AOL untuk memenangkan *browser war*, mengorbankan posisi MSN dalam proses itu.

Pada skenario ketiga, Hao Ma menunjuk pada sumber-sumber kinerja superior yang bersifat *non-market*: regulasi pemerintah yang menciptakan monopoli artifisial, keberuntungan yang bersifat satu-kali, kejutan lingkungan yang merugikan pesaing lebih dari perusahaan fokal, dan *lag* waktu dari *goodwill* pelanggan yang mengembangkan *residual benefit* bahkan setelah keunggulan aktualnya memudar. Semua faktor ini dapat menghasilkan kinerja superior yang tidak dapat dikaitkan dengan keunggulan bersaing dalam pengertian analitis yang ketat.

## 4. Koneksi ke Topik Silabus (Pertemuan 4 — TPGS Ch.4)

Artikel Hao Ma berfungsi sebagai *pengaman intelektual* terhadap pembacaan naif atas TPGS Ch.4. Di banyak bagian Ch.4, penulis menggunakan *competitive advantage* dan *superior performance* secara bergantian, mengikuti praktik umum literatur strategi. Tanpa sensitivitas yang diberikan Hao Ma, mahasiswa dapat jatuh ke dalam penyederhanaan: memetakan sumber daya VRIN, menyimpulkan bahwa perusahaan memiliki keunggulan bersaing, lalu langsung meramalkan kinerja superior.

Hao Ma memaksa diskursus yang lebih hati-hati. Untuk setiap analisis VRIN yang selesai, pertanyaan lanjutan harus diajukan: apakah keunggulan struktural yang teridentifikasi benar-benar diterjemahkan menjadi kinerja, atau adakah mediator yang mencegah terjemahan itu? Apakah perusahaan berhasil mengeksploitasi keunggulannya, atau justru membiarkannya sebagai potensi yang tidak diaktualisasikan? Pertanyaan-pertanyaan ini mengubah analisis strategis dari latihan deskriptif menjadi diagnosis yang siap tindakan.

Di sisi lain, artikel ini juga memperkaya pemahaman tentang Pertemuan 5 yang akan datang—tentang *generic competitive strategies*. Pilihan antara *cost leadership* dan *differentiation* pada Porter dapat dibaca ulang dengan mata yang telah dilatih Hao Ma: apakah strategi generik itu menciptakan keunggulan diskret atau keunggulan komposit? Apakah pesaing memiliki *critical combination* yang tepat? Apakah konteks industri memungkinkan penerjemahan itu ke kinerja?

## 5. Kekuatan Artikel

Kekuatan utama Hao Ma adalah **kejernihan diagnostik**. Ia mengidentifikasi masalah tautologi dalam literatur strategi dengan ketepatan yang menyegarkan. Ketika keunggulan bersaing dan kinerja digunakan sebagai sinonim, pernyataan "perusahaan yang unggul berkinerja lebih baik" kehilangan nilai informatif—ia menjadi pernyataan definisional. Hao Ma mengartikulasikan masalah ini secara eksplisit dan menyediakan solusi konseptual yang elegan.

Kekuatan kedua adalah **definisi operasional yang lebih tepat**. Dengan memperkenalkan konsep *reference point* (*against whom*, *on what*, *for whom*) Hao Ma mengubah pernyataan tentang keunggulan bersaing dari klaim global yang kabur menjadi klaim terbatas yang dapat diuji. Analis yang menggunakan kerangka ini akan dituntut untuk menyebutkan pesaing pembanding, dimensi kompetisi, dan pelanggan yang dilayani—sebuah disiplin yang membuat analisisnya lebih kuat.

Kekuatan ketiga adalah **pembedaan diskret-komposit**. Konsep ini memberikan alat untuk membedakan mengapa beberapa perusahaan dengan keunggulan yang tampak jelas gagal berkinerja superior. Jawabannya sering adalah: mereka memiliki keunggulan diskret tetapi gagal mengintegrasikannya menjadi keunggulan komposit. Ini adalah wawasan yang praktis dan sering terabaikan.

Kekuatan keempat adalah **kerangka skenario yang lengkap**. Dengan memetakan tiga skenario—keunggulan dengan kinerja, keunggulan tanpa kinerja, kinerja tanpa keunggulan—Hao Ma menggambarkan peta lengkap hubungan antara kedua konstruk. Terutama skenario "keunggulan tanpa kinerja" menjadi penting karena ia menjelaskan banyak kasus yang membingungkan dalam praktik: mengapa Xerox, Apple awal, atau EMI—yang secara teknologi unggul—tidak menuai panen finansial yang setara.

Kekuatan kelima adalah **pengakuan atas sumber-sumber kinerja non-pasar**. Dengan mengakui bahwa regulasi, keberuntungan, dan kejutan lingkungan dapat menghasilkan kinerja tanpa keunggulan bersaing dalam arti analitis, Hao Ma membuka ruang diskusi yang relevan untuk konteks pasar yang sangat diatur seperti Indonesia, di mana posisi-posisi istimewa BUMN dan proteksi regulatif adalah bagian kenyataan ekonomi.

## 6. Keterbatasan dan Kelemahan

**Pertama, ketiadaan pengujian empiris.** Seperti Barney, Hao Ma menulis artikel konseptual yang tidak didukung data. Kerangka tiga skenario, pembedaan diskret-komposit, dan daftar mediator yang mengganggu terjemahan keunggulan ke kinerja—semua ini adalah proposisi teoretis yang belum diuji secara empiris oleh Hao Ma sendiri. Penelitian selanjutnya perlu mengoperasionalisasi kerangka ini dan mengujinya pada data kinerja perusahaan dalam konteks yang beragam.

**Kedua, terminologi yang tidak konsisten diadopsi.** Istilah-istilah yang diajukan Hao Ma—*discrete vs. compound advantage*, *reference point*, *four sub-situations of advantage without performance*—tidak menjadi standar dalam literatur berikutnya. Sebagian disebabkan oleh sifat jurnal publikasinya (*Competitiveness Review* tidak memiliki visibilitas akademik setingkat *Strategic Management Journal*), sebagian karena penelitian selanjutnya memilih kerangka operasional yang berbeda.

**Ketiga, kurang pendalaman pada mediator.** Hao Ma mengidentifikasi adanya mediator antara keunggulan dan kinerja—eksekusi, faktor eksogen, *strategic capture* oleh *stakeholder* internal—tetapi tidak mengelaborasinya secara sistematis. Literatur *strategy execution* (Hrebiniak 2005; Kaplan & Norton 2005) dan literatur *rent appropriation* (Coff 1999) menyumbang elaborasi yang lebih kaya, tetapi Hao Ma sendiri tidak mengintegrasikannya.

**Keempat, asumsi dua-aktor.** Definisi operasional Hao Ma membangun keunggulan bersaing sebagai perbandingan sepasang pesaing. Dalam pasar dengan banyak aktor dan struktur persaingan yang kompleks (seperti pasar *platform* multi-sisi), pendekatan dua-aktor ini tidak memadai. Hao Ma sendiri mengakui keterbatasan ini tetapi tidak mengembangkan kerangka yang lebih kaya untuk banyak aktor.

**Kelima, logika sirkular dalam argumen "kinerja tanpa keunggulan".** Ketika Hao Ma mengklaim bahwa regulasi dapat menghasilkan kinerja tanpa keunggulan, definisi yang ia gunakan untuk keunggulan bersaing menjadi krusial. Apabila kita mendefinisikan keunggulan bersaing secara luas (termasuk keunggulan *political*/non-pasar), maka semua kasus kinerja superior akan kembali dapat diatribusikan ke semacam keunggulan. Hao Ma sebenarnya mengakui ambiguitas ini—dan memilih definisi yang lebih sempit—tetapi argumennya mengandung fleksibilitas definisi yang berpotensi menjadi sumber kritik.

## 7. Evaluasi Kritis

Nilai permanen artikel Hao Ma terletak pada *pemisahan konseptual antara keunggulan dan kinerja*, dan ini adalah kontribusi yang bertahan meski terminologi spesifiknya tidak diadopsi luas. Kesadaran bahwa keunggulan bersaing struktural tidak otomatis menjadi kinerja telah masuk ke dalam praktik analisis strategis yang matang, meski sering tanpa atribusi langsung ke Hao Ma.

Tiga pengamatan kritis perlu ditekankan untuk memperkaya apresiasi atas artikel ini.

**Pertama**, kerangka Hao Ma mengundang pembacaan kritis terhadap banyak analisis strategis yang populer di kalangan praktisi Indonesia. Klaim seperti "BUMN ini memiliki keunggulan bersaing" atau "perusahaan keluarga itu unggul di pasar" sering tidak disertai spesifikasi titik referensi. Unggul dibandingkan siapa—pesaing swasta domestik, pesaing multinasional, atau pesaing BUMN lain di sektor yang sama? Pada dimensi apa—biaya, jangkauan, pelayanan, kepatuhan regulasi? Tanpa menjawab pertanyaan-pertanyaan itu, klaim keunggulan hanyalah retorika.

**Kedua**, pembedaan diskret-komposit menyediakan diagnosis yang berguna untuk perusahaan yang "kehilangan keunggulan." Banyak perusahaan Indonesia yang dalam dekade terakhir kehilangan posisinya—Garuda Indonesia, Carrefour Indonesia, Nokia secara global, Kodak—sesungguhnya tidak kehilangan *semua* keunggulan diskret mereka sekaligus. Mereka gagal mengintegrasikan keunggulan-keunggulan yang tersisa menjadi keunggulan komposit yang relevan bagi konteks kompetitif yang baru. Garuda, misalnya, tetap memiliki beberapa keunggulan diskret (*slot* bandara, status *flag carrier*, tenaga pilot yang terlatih) tetapi gagal mengintegrasikannya dengan struktur biaya yang efisien dan tata kelola yang sehat.

**Ketiga**, skenario "kinerja tanpa keunggulan" sangat relevan untuk konteks pasar Indonesia yang sangat diatur. Banyak BUMN yang secara finansial berkinerja memadai berkat posisi regulatif yang istimewa—mandat layanan publik yang disertai kompensasi, hak eksklusif pada sektor-sektor strategis, dan akses ke pembiayaan pemerintah. Apabila analisis strategis berhenti pada kinerja finansial sebagai *bukti* keunggulan, kita akan keliru membaca kekuatan BUMN itu. Pertanyaan Hao Ma—apakah kinerja ini akan bertahan jika proteksi regulatif dicabut?—adalah pertanyaan yang harus diajukan oleh analis, regulator, dan pembuat kebijakan secara disiplin.

Satu kritik tambahan yang perlu diangkat secara terbuka: Hao Ma mengakhiri artikelnya dengan pertanyaan epistemologis yang menggantung—apabila kinerja adalah variabel dependen akhir dalam ilmu manajemen strategik, mengapa kita memerlukan konstruk *competitive advantage* sebagai variabel perantara? Pertanyaan ini, meski cerdas, tidak dijawab dalam artikelnya sendiri. Pembacaan yang bijak adalah memperlakukan pertanyaan itu sebagai undangan untuk penelitian lanjutan, bukan sebagai sanggahan terhadap seluruh bangunan teori yang telah dibangun.

## 8. Implikasi bagi Pemahaman Manajemen Strategik

**Pertama**, artikel ini mengubah cara analisis strategis yang serius dilakukan. Setiap pernyataan tentang keunggulan bersaing harus disertai spesifikasi titik referensi, dimensi, dan konteks. Pernyataan yang tidak memenuhi syarat itu dapat diidentifikasi sebagai retorika dan dipersilakan keluar dari diskusi analitis.

**Kedua**, bagi manajer dan konsultan strategis, kerangka Hao Ma mendorong diagnosis yang lebih tajam atas perusahaan yang "mengalami stagnasi." Pertanyaan yang tepat bukan "apa yang salah dengan perusahaan ini?" melainkan "pada transisi mana dalam rantai keunggulan-kinerja terdapat kebocoran—pada pengembangan dari diskret ke komposit, pada eksploitasi keunggulan, pada kombinasi yang kurang lengkap, atau pada faktor eksogen yang tidak dapat dikendalikan?"

**Ketiga**, bagi auditor dan akuntan manajemen, kerangka ini memperjelas pembedaan antara *operating performance* dan *structural advantage*—dua hal yang dalam laporan keuangan sering menyatu tetapi analitis berbeda. Perusahaan yang berkinerja baik karena kejutan pasar sementara atau regulasi yang menguntungkan memiliki profil risiko yang berbeda dari perusahaan yang berkinerja baik karena sumber daya VRIN yang bertahan.

**Keempat**, bagi pembuat kebijakan, kerangka ini relevan untuk evaluasi kebijakan proteksi industri. Jika proteksi regulatif menghasilkan kinerja tanpa membangun keunggulan bersaing yang sejati, maka pencabutan proteksi akan mengekspos perusahaan pada kinerja yang merosot tajam. Kebijakan liberalisasi yang matang karena itu harus memperhitungkan perbedaan antara dua jenis kinerja ini.

## 9. Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut

**Pertama**, apakah kerangka keunggulan bersaing yang berpusat pada perusahaan individual (baik versi Barney maupun Hao Ma) masih memadai dalam era ekosistem dan platform? GoTo, Tokopedia, dan Shopee di Indonesia beroperasi dalam jaringan yang melibatkan mitra *driver*, *merchant*, logistik, dan keuangan. Keunggulan mereka sering bersifat jaringan, bukan atribut perusahaan tunggal. Bagaimana kerangka Hao Ma diterjemahkan ke konteks ini?

**Kedua**, dalam industri yang sangat diatur seperti perbankan Indonesia, pembedaan antara *structural advantage* dan *regulatory capture* sering kabur. Apakah CASA franchise BCA adalah keunggulan VRIN yang sejati, atau sebagian di antaranya adalah produk sejarah regulasi perbankan nasional yang memberi keuntungan struktural pada bank-bank tertentu? Pertanyaan ini tidak semata akademis; ia relevan untuk evaluasi *resilience* BCA dalam skenario liberalisasi perbankan yang lebih lanjut.

**Ketiga**, bagaimana seharusnya perusahaan mengalokasikan perhatian manajerial antara upaya *memperluas keunggulan bersaing* dan upaya *meningkatkan terjemahan keunggulan ke kinerja*? Kerangka Hao Ma menyiratkan bahwa keduanya adalah aktivitas yang berbeda, dengan jalur manajerial yang berbeda. Apakah ada bukti empiris tentang bagaimana perusahaan yang sukses menyeimbangkan keduanya? Pertanyaan ini layak menjadi pertanyaan penelitian tesis di bidang manajemen strategik maupun akuntansi manajemen.
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
        write_md(RMK, "rmk_pert4.md"),
        OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 4.docx",
    )
    pandoc(
        write_md(CR5, "artikel5.md"),
        OUT_CR / "01079_Dzaki Muhammad Yusfian_Artikel 5.docx",
    )
    pandoc(
        write_md(CR6, "artikel6.md"),
        OUT_CR / "01079_Dzaki Muhammad Yusfian_Artikel 6.docx",
    )

    print("\nAll three documents generated successfully.")
    print(f"RMK : {OUT_RMK}")
    print(f"CR  : {OUT_CR}")


if __name__ == "__main__":
    main()
