# -*- coding: utf-8 -*-
"""Humanized rewrite of RMK Pertemuan 4 — Evaluating a Company's Resources,
Capabilities, and Competitiveness.

Voice goal: graduate student (S2 Magister Akuntansi) writing carefully — analytical,
willing to commit to a position, but with natural rhythm. The previous draft suffered
from mechanical "Pertama / Kedua / Ketiga" lists, parallel tricolons, and the same
verb ("menyodorkan") repeated dozens of times. This version varies sentence length,
drops most em-dashes, and uses the first person where the writer is genuinely
making a judgment.
"""

H1 = "Heading 1"
H2 = "Heading 2"
H3 = "Heading 3"
N = "Normal"
B = "Body Text"

BLOCKS = [
    (H1, "RINGKASAN MATERI KULIAH"),
    (N, "Pertemuan 4: Evaluating a Company's Resources, Capabilities, and Competitiveness"),
    (B, "Mata Kuliah: Manajemen Strategik Kontemporer (MST304)"),
    (B, "Semester: II, T.A. 2025/2026"),
    (B, "Nama: Dzaki Muhammad Yusfian"),
    (B, "NIM: 1125 01079"),
    ("", ""),

    (H2, "1. Dari SWOT ke Resource-Based View: Pergeseran Cara Pandang"),
    (N,
     "Kerangka SWOT yang diwariskan oleh Learned, Christensen, Andrews, dan Guth (1965) menempatkan analisis internal sejajar dengan analisis eksternal. Tiga dekade pertama setelah kerangka itu lahir, perhatian akademisi maupun praktisi justru lari ke arah eksternal, terutama setelah Porter (1980) memformalkan model lima kekuatan. Akibatnya cukup ironis: analisis internal sering tinggal sebagai daftar bullet kekuatan dan kelemahan tanpa metode analitis yang jelas."),
    (B,
     "Kontribusi besar dari tradisi Resource-Based View (RBV) adalah menolak kedangkalan itu. Barney (1991) menunjukkan bahwa model environmental Porter dan turunannya diam-diam memakai dua asumsi: pertama, perusahaan dalam satu industri dianggap memiliki sumber daya yang relatif seragam; kedua, sumber daya dianggap dapat berpindah secara hampir sempurna di pasar faktor. Jika dua asumsi itu benar, setiap strategi yang berhasil akan langsung ditiru, dan keunggulan bersaing yang bertahan menjadi mustahil kecuali lewat hambatan industri. Padahal, justru pertanyaan inilah yang seharusnya dijelaskan oleh teori strategi: kenapa perusahaan dalam industri yang sama bisa berkinerja sangat berbeda?"),
    (B,
     "Yang dilakukan RBV adalah mengganti dua asumsi tadi. Sumber daya strategis pada dasarnya heterogen antar perusahaan, dan pergerakannya di pasar faktor bersifat imperfek. Dengan kerangka baru ini, perbedaan kinerja antar pemain dalam satu industri bukan lagi anomali yang harus dijelaskan, melainkan konsekuensi yang wajar dari heterogenitas sumber daya yang sulit dipindah."),
    (B,
     "Pergeseran ini sekaligus menjelaskan kenapa RBV dan Porter bukan dua kerangka yang saling membatalkan. Analisis eksternal memberi tahu kita kenapa industri tertentu rata-rata lebih menguntungkan dari industri lain, sementara analisis internal berbasis sumber daya menjelaskan kenapa beberapa pemain dalam satu industri bisa konsisten lebih unggul dari tetangganya. Kedua pertanyaan itu sah, dan keduanya butuh alat yang berbeda."),

    (H2, "2. Analisis Sumber Daya dan Kapabilitas: VRIN dan VRIO"),
    (N,
     "Sumbangan operasional terbesar RBV adalah empat kriteria yang awalnya dikenal dengan akronim VRIN: valuable, rare, imperfectly imitable, dan non-substitutable. Barney (1995) kemudian menyederhanakan kriteria terakhir dan menambahkan dimensi organisasi (O) sehingga lahir VRIO. Substansinya tetap sama; kerangkanya hanya menjadi lebih ringkas."),
    (B,
     "Kriteria valuable mengikat konsep sumber daya pada konteks pasar. Sebuah aset disebut bernilai kalau ia memungkinkan perusahaan menangkap peluang atau menahan ancaman di lingkungannya. Definisi ini penting karena memutus argumen bahwa keunikan teknis itu sendiri sudah cukup. Aset yang unik tetapi tidak relevan dengan peluang pasar yang tersedia adalah sunk cost, bukan sumber daya strategis. Contoh klasik yang sering dipakai: kepakaran perbaikan mesin tik di perusahaan yang tidak lagi bergerak di industri pendukung mesin tik. Dulu bernilai, sekarang tidak."),
    (B,
     "Kriteria rare berbicara tentang distribusi, bukan jumlah absolut. Sumber daya yang bernilai tetapi dimiliki banyak pesaing hanya menghasilkan competitive parity, kondisi setara, bukan keunggulan. Namun kelangkaan tidak menuntut bahwa sumber daya itu hanya dimiliki satu perusahaan. Cukup kalau jumlah pemiliknya lebih sedikit dari yang dibutuhkan untuk menciptakan dinamika kompetisi sempurna di pasar."),
    (B,
     "Kriteria imperfectly imitable adalah bagian yang membuat kerangka RBV punya kedalaman teoretis. Barney mengurai tiga sumber imperfeksi imitasi yang saling berhubungan tetapi konseptual berbeda. Yang pertama, kondisi historis unik. Sumber daya tertentu hanya bisa diakumulasi melalui jalur sejarah yang tidak dapat diulang. Reputasi Coca-Cola sebagai simbol Amerika tidak bisa dibangun ulang dari nol oleh perusahaan mana pun, karena pembangunannya butuh lebih dari satu abad dalam konteks budaya global abad ke-20. Yang kedua, ambiguitas kausal. Hubungan antara sumber daya dan keunggulan sering tidak jelas bahkan bagi perusahaan yang menikmatinya. Kalau imitator tidak tahu persis apa yang harus ditiru, imitasi otomatis sulit. Yang ketiga, kompleksitas sosial. Sumber daya tertanam di jaringan relasi, budaya, dan norma yang tidak bisa dibeli langsung. Kepercayaan antar departemen, kultur kerja yang mengendap selama beberapa dekade, dan jejaring pemasok yang dibangun melalui interaksi berulang masuk kategori ini."),
    (B,
     "Kriteria non-substitutable mengingatkan bahwa imperfeksi imitasi saja belum cukup. Sumber daya yang secara teknis tidak bisa ditiru tetap akan kehilangan nilainya kalau ada alternatif strategis yang fungsional setara. Contoh yang sering dipakai Barney sendiri menarik: tim manajemen puncak yang berkualitas tinggi (memenuhi VRI) bisa disubstitusi oleh sistem perencanaan formal yang dirancang dengan baik, kalau keduanya menghasilkan kualitas pengambilan keputusan yang setara."),
    (B,
     "Empat kriteria ini bekerja seperti saringan berurutan. Sumber daya yang tidak bernilai langsung gugur. Yang bernilai tapi umum hanya menghasilkan parity. Yang bernilai dan langka memberi keunggulan sementara. Hanya sumber daya yang memenuhi keempat syarat sekaligus yang berpeluang menjadi fondasi keunggulan bersaing yang bertahan."),

    (H2, "3. Dynamic Capabilities: Respons untuk Lingkungan yang Bergerak"),
    (N,
     "Kritik paling konstruktif terhadap RBV klasik datang dari Teece, Pisano, dan Shuen (1997) lewat kerangka dynamic capabilities. Inti kritik mereka tidak menyangkal validitas VRIN. Yang ditunjukkan adalah bahwa di lingkungan yang bergerak cepat, sumber daya VRIN hari ini bisa kehilangan relevansi dalam lima sampai sepuluh tahun. RBV klasik, karena terlalu fokus pada kondisi ekuilibrium, kurang menjelaskan bagaimana perusahaan memperbarui portofolio sumber dayanya seiring perubahan lingkungan."),
    (B,
     "Dynamic capabilities didefinisikan sebagai kemampuan perusahaan untuk mengintegrasikan, membangun, dan merekonfigurasi kompetensi internal maupun eksternal guna menghadapi perubahan lingkungan yang cepat. Teece (2007) memperhalusnya menjadi tiga kapabilitas: sensing untuk mendeteksi peluang dan ancaman baru, seizing untuk memobilisasi sumber daya menangkap peluang yang terdeteksi, dan transforming untuk merombak basis sumber daya secara berkelanjutan."),
    (B,
     "Kerangka ini punya nilai praktis yang besar bagi perusahaan yang sedang menghadapi disrupsi digital. Kasus Kodak, Nokia, dan Blockbuster menunjukkan satu pola yang sama: kepemilikan sumber daya VRIN yang dulu kuat tidak menjamin kelangsungan kalau perusahaan gagal mengembangkan kapabilitas untuk membaca dan merespons pergeseran teknologi. Di Indonesia, transisi perbankan konvensional ke perbankan digital memberikan laboratorium alami yang menarik. BCA, misalnya, mampu mempertahankan posisinya bukan semata karena franchise CASA-nya kuat, melainkan karena ia memperlihatkan kapabilitas dinamis untuk membangun BCA Mobile dan kemudian BCA Digital sebelum tekanan disrupsi memaksa perubahan dilakukan secara reaktif."),

    (H2, "4. Value Chain dan Activity-Based Costing"),
    (N,
     "Porter (1985) menyumbang kerangka yang melengkapi RBV: value chain. Kalau RBV melihat perusahaan sebagai kumpulan sumber daya, value chain melihatnya sebagai rangkaian aktivitas yang saling terkait dalam menghasilkan nilai bagi pelanggan. Aktivitas dipisah menjadi primary activities (logistik masuk, operasi, logistik keluar, pemasaran dan penjualan, pelayanan) dan support activities (infrastruktur, manajemen SDM, pengembangan teknologi, pengadaan)."),
    (B,
     "Kekuatan value chain terletak pada kemampuannya menjadikan analisis biaya dan diferensiasi sebagai latihan yang terdisiplin. Setiap aktivitas dapat dibandingkan dengan benchmark industri, sehingga manajemen tahu di mana biaya tidak kompetitif dan di mana ada celah untuk diferensiasi. TPGS menekankan bahwa analisis ini paling bermakna kalau digabungkan dengan activity-based costing, yang mengalokasikan biaya pada aktivitas spesifik dan bukan sekadar pada pusat biaya tradisional."),
    (B,
     "Hubungannya dengan RBV menjadi jelas pada titik diagnostik. Aktivitas yang biaya relatifnya rendah atau kualitasnya tinggi biasanya menunjuk ke sumber daya atau kapabilitas mendasar yang membuat aktivitas itu berjalan lebih efisien. Dengan kata lain, value chain menjadi alat untuk menemukan kandidat VRIN, bukan pengganti RBV."),

    (H2, "5. SWOT yang Diperdalam: dari Daftar ke Diagnosis"),
    (N,
     "TPGS Bab 4 menolak SWOT versi kosmetik, yaitu matriks empat kuadran yang diisi bullet point tanpa analisis lanjutan. SWOT yang berguna secara strategis dikerjakan berurutan: identifikasi kekuatan yang berdiri di atas dasar VRIN yang terbukti, kelemahan yang menghambat eksekusi strategi yang tersedia, peluang yang sebenarnya bisa dijangkau dengan kekuatan yang ada, dan ancaman yang mempertaruhkan basis sumber daya."),
    (B,
     "Langkah yang paling sering dilewatkan adalah pemetaan silang. Bagaimana kekuatan dipakai untuk mengejar peluang, bagaimana kelemahan membuka pintu bagi ancaman, dan bagaimana kekuatan dapat dipakai untuk menahan ancaman. Tanpa pemetaan silang seperti itu, SWOT hanya berhenti pada daftar deskriptif. Itu bukan diagnosis strategis, itu daftar belanja."),

    (H2, "6. Competitive Strength Assessment"),
    (N,
     "TPGS Bab 4 juga memperkenalkan teknik competitive strength assessment yang memakai pembobotan tertimbang pada faktor sukses kritis (key success factors) dalam industri. Untuk setiap faktor (kualitas produk, jangkauan distribusi, kapabilitas inovasi, struktur biaya, reputasi merek, dan seterusnya), manajemen menilai posisi perusahaan relatif terhadap pesaing utamanya pada skala numerik, lalu skor tersebut dikalikan dengan bobot."),
    (B,
     "Tekniknya sederhana, tapi disiplin yang dituntut tidak boleh diremehkan. Manajemen dipaksa mengartikulasikan tiga hal: faktor apa yang paling menentukan sukses di industri spesifiknya, di mana posisi perusahaan relatif terhadap pesaing yang konkret, dan di mana prioritas peningkatan harus diletakkan. Hasilnya adalah peta kompetitif tertimbang yang biasanya mempertajam diskusi strategis di tingkat dewan direksi karena angkanya sulit dibantah dengan pendapat saja."),

    (H2, "7. Mendiagnosis Masalah Strategis yang Harus Ditangani"),
    (N,
     "Tahap akhir analisis internal adalah menerjemahkan temuan-temuan dari langkah sebelumnya menjadi pernyataan yang jernih tentang apa yang harus ditangani oleh strategi baru. TPGS menekankan bahwa diagnosis di tahap ini harus spesifik dan dapat ditindaklanjuti. Pernyataan seperti \"perusahaan perlu meningkatkan daya saingnya\" tidak punya nilai operasional. Lebih berguna kalau ditulis sebagai, misalnya, \"perusahaan kehilangan tiga persentase pangsa pasar pada segmen X dalam tiga tahun terakhir karena jarak harga terhadap pesaing Y telah menyempit menjadi kurang dari lima persen.\""),
    (B,
     "Diagnosis yang baik mengintegrasikan analisis eksternal dari Pertemuan 3 dengan analisis internal dari Pertemuan 4. Ia menjadi jembatan ke Pertemuan 5 dan setelahnya, di mana perusahaan harus memilih strategi generik yang tepat sebagai respons."),

    (H2, "8. Kesimpulan"),
    (N,
     "Pertemuan 4 melengkapi kerangka analitis yang dibangun sejak Pertemuan 1. Dengan memahami bahwa sumber daya dan kapabilitas yang heterogen dan sulit ditiru adalah fondasi dari keunggulan bersaing yang bertahan, mahasiswa diperlengkapi dengan bahasa untuk mengurai pertanyaan klasik: kenapa perusahaan dengan produk yang mirip bisa berkinerja sangat berbeda."),
    (B,
     "Dua artikel yang menyertai pertemuan ini berbicara dari sisi yang berbeda dalam percakapan teoretis yang sama. Barney (1991) membangun kerangka RBV secara sistematis dan menyediakan bahasa operasional yang sampai hari ini masih dominan. Hao Ma (2000) datang dengan kritik meta yang tidak menolak RBV, tetapi mengingatkan bahwa keunggulan bersaing tidak otomatis berubah menjadi kinerja superior. Kedua artikel itu menanam kesadaran yang sebenarnya sederhana namun sering dilewatkan: ada bedanya antara apa yang secara struktural dimiliki perusahaan dan apa yang secara aktual diraihnya di pasar. Dalam literatur awam dua hal itu sering dipertukarkan tanpa hati-hati."),
]
