#!/usr/bin/env python3
"""
generate_submission.py
Generates three Word documents for MST304 Pertemuan 2 submission.
Dev Assistant/scripts/generate_submission.py
"""

import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ── Paths ──────────────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).resolve().parent
DEV_DIR      = SCRIPT_DIR.parent
PROJECT_ROOT = DEV_DIR.parent
TEMP_DIR     = DEV_DIR / "temp"
REFERENCE    = SCRIPT_DIR / "reference.docx"
OUT_RMK      = PROJECT_ROOT / "course-materials" / "outputs" / "RMK"
OUT_CR       = PROJECT_ROOT / "course-materials" / "outputs" / "Critical Thinking of the Article"
PANDOC       = r"C:\Program Files\Pandoc\pandoc.exe"


# ── Reference template ─────────────────────────────────────────────────────────
def create_reference():
    doc = Document()
    for sec in doc.sections:
        sec.top_margin    = Cm(3)
        sec.bottom_margin = Cm(2.5)
        sec.left_margin   = Cm(3)
        sec.right_margin  = Cm(2.5)

    n = doc.styles["Normal"]
    n.font.name  = "Times New Roman"
    n.font.size  = Pt(12)
    n.paragraph_format.line_spacing       = Pt(18)
    n.paragraph_format.first_line_indent  = Cm(1.25)
    n.paragraph_format.space_after        = Pt(6)

    h1 = doc.styles["Heading 1"]
    h1.font.name  = "Times New Roman"
    h1.font.size  = Pt(14)
    h1.font.bold  = True
    h1.font.color.rgb = RGBColor(0, 0, 0)
    h1.paragraph_format.alignment         = WD_ALIGN_PARAGRAPH.CENTER
    h1.paragraph_format.first_line_indent = Cm(0)
    h1.paragraph_format.space_before      = Pt(0)
    h1.paragraph_format.space_after       = Pt(6)

    h2 = doc.styles["Heading 2"]
    h2.font.name  = "Times New Roman"
    h2.font.size  = Pt(12)
    h2.font.bold  = True
    h2.font.color.rgb = RGBColor(0, 0, 0)
    h2.paragraph_format.first_line_indent = Cm(0)
    h2.paragraph_format.space_before      = Pt(12)
    h2.paragraph_format.space_after       = Pt(4)

    h3 = doc.styles["Heading 3"]
    h3.font.name   = "Times New Roman"
    h3.font.size   = Pt(12)
    h3.font.bold   = True
    h3.font.italic = True
    h3.font.color.rgb = RGBColor(0, 0, 0)
    h3.paragraph_format.first_line_indent = Cm(0)
    h3.paragraph_format.space_before      = Pt(8)
    h3.paragraph_format.space_after       = Pt(4)

    doc.save(str(REFERENCE))
    print("Created reference.docx")


# ── Pandoc helper ──────────────────────────────────────────────────────────────
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
# DOCUMENT 1 — RMK PERTEMUAN 2
# ══════════════════════════════════════════════════════════════════════════════
RMK = """\
# RINGKASAN MATERI KULIAH

**Pertemuan 2: The Managerial Process of Crafting and Executing Strategy**

**Mata Kuliah:** Manajemen Strategik Kontemporer (MST304)

**Semester:** II, T.A. 2025/2026

**Nama:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Pendahuluan

Pertemuan kedua mata kuliah Manajemen Strategik Kontemporer meletakkan kerangka kerja mendasar yang akan menjadi pijakan seluruh pembahasan sepanjang semester. Jika Pertemuan 1 membahas hakikat strategi, yakni *apa itu strategi dan mengapa ia penting*, maka Pertemuan 2 menjawab pertanyaan yang lebih operasional: bagaimana strategi dirancang dan dilaksanakan dalam sebuah organisasi?

Gamble, Peteraf, dan Thompson (2021) mengemas jawaban atas pertanyaan ini dalam sebuah proses manajerial yang terdiri dari lima tahap yang saling terkait dan bersifat iteratif. Kelima tahap tersebut—mulai dari pengembangan visi strategis hingga evaluasi dan penyesuaian kinerja—bukan sekadar langkah prosedural, melainkan cerminan cara berpikir manajerial yang sistematis dan adaptif. Di samping itu, bab ini juga memperkenalkan konsep *corporate governance* sebagai mekanisme pengawasan yang memastikan proses strategi tidak menyimpang dari kepentingan para pemangku kepentingan.

Relevansi topik ini bagi mahasiswa program Magister Akuntansi terletak pada kenyataan bahwa pemahaman atas proses strategi bukan semata kebutuhan manajer puncak. Akuntan manajemen, auditor internal, dan analis keuangan yang memahami cara strategi dirancang dan dieksekusi akan mampu memberikan kontribusi yang jauh lebih bermakna dibandingkan mereka yang hanya memahami angka tanpa konteks strategis di baliknya.

## 2. Proses Manajerial Pembuatan dan Eksekusi Strategi: Tinjauan Umum

TPGS (Gamble et al., 2021) menyajikan lima tahap proses manajerial sebagai kerangka utama pemikiran strategis. Kelima tahap tersebut adalah: (1) mengembangkan visi strategis (*developing a strategic vision*), (2) menetapkan tujuan (*setting objectives*), (3) merumuskan strategi (*crafting a strategy*), (4) mengimplementasikan dan mengeksekusi strategi (*implementing and executing the strategy*), serta (5) mengevaluasi dan menyesuaikan arah berdasarkan kinerja aktual (*monitoring developments, evaluating performance, and making adjustments*).

Satu hal yang perlu ditekankan sejak awal adalah bahwa proses ini tidak bersifat linier. Umpan-balik dari tahap kelima dapat memicu revisi mendasar pada tahap pertama atau ketiga. Ketika kinerja aktual menyimpang dari target, manajer tidak serta-merta hanya memperbaiki eksekusi. Mereka mungkin perlu mempertanyakan apakah visi yang ditetapkan masih relevan, atau apakah asumsi lingkungan yang mendasari strategi masih valid. Sifat iteratif inilah yang membuat proses strategi berbeda dari perencanaan bisnis konvensional.

Konsep *deliberate strategy* dan *emergent strategy* yang dikembangkan oleh Mintzberg relevan di sini. Strategi yang dirumuskan secara sadar pada Tahap 3 merupakan *deliberate strategy*; namun, dalam proses eksekusi di Tahap 4, sering kali muncul pola-pola baru yang tidak direncanakan. Manajer yang efektif tidak sekadar mengeksekusi rencana, tetapi juga peka terhadap sinyal-sinyal *emergent* yang layak diintegrasikan ke dalam arah strategis organisasi.

Selain itu, TPGS menekankan bahwa strategi bukan hak eksklusif manajemen puncak. Setiap manajer pada setiap tingkatan organisasi membuat pilihan-pilihan yang secara kumulatif membentuk strategi. Pemahaman atas kerangka lima tahap ini membantu seluruh lapisan manajerial menyelaraskan keputusan mereka dengan arah strategis organisasi secara keseluruhan.

## 3. Tahap 1 — Visi Strategis, Misi, dan Nilai Inti

### 3.1 Visi Strategis

Visi strategis (*strategic vision*) adalah gambaran spesifik, masuk akal, dan menginspirasi mengenai posisi dan keadaan organisasi dalam lima hingga sepuluh tahun ke depan. Visi bukan sekadar slogan motivasional; ia adalah peta jalan yang memberi arah pada pengambilan keputusan di semua tingkatan organisasi.

TPGS mengidentifikasi tujuh kriteria visi yang efektif: *graphic* (mampu membentuk citra mental yang jelas), *directional* (memberi arahan pada keputusan), *focused* (cukup spesifik untuk memandu prioritas), *flexible* (dapat disesuaikan dengan perubahan lingkungan), *feasible* (realistis dan dapat dicapai), *desirable* (menarik bagi para pemangku kepentingan), dan *easy to communicate* (dapat dijelaskan secara ringkas).

Altıok (2011) memperkaya pemahaman tentang visi strategis dengan memperkenalkan konsep *applicable vision*, yaitu visi yang tidak hanya diformulasikan secara tertulis, tetapi benar-benar dimiliki bersama oleh seluruh anggota organisasi. Visi yang *applicable* memiliki tiga karakteristik tambahan: ia dibentuk melalui partisipasi seluruh karyawan, menciptakan loyalitas dan motivasi menuju tujuan tunggal, serta cukup jelas untuk mengarahkan pengambilan keputusan di tingkat operasional. Menurut Altıok, visi yang tidak *applicable* hanyalah slogan yang justru berbahaya saat krisis, karena organisasi akan kehilangan kompas bersama justru ketika kompas itu paling dibutuhkan.

Contoh relevan dari konteks Indonesia: ketika BCA merumuskan ulang visinya setelah krisis moneter 1998, dari "bank swasta terbesar" menjadi "bank transaksional pilihan utama masyarakat Indonesia", perubahan itu bukan sekadar pergantian kata. Ia mencerminkan pembelajaran mendalam dari krisis dan menjadi pijakan transformasi operasional yang kemudian menempatkan BCA sebagai bank dengan basis nasabah transaksional terluas di Indonesia.

### 3.2 Pernyataan Misi

Pernyataan misi (*mission statement*) menjelaskan identitas organisasi saat ini: siapa kita, apa yang kita lakukan, dan mengapa kita ada. Berbeda dari visi yang berorientasi masa depan, misi berorientasi masa kini dan memberi panduan pada keputusan operasional sehari-hari. Misi yang efektif menjawab tiga pertanyaan: pelanggan atau pemangku kepentingan apa yang dilayani, kebutuhan apa yang dipenuhi, dan bagaimana organisasi memenuhi kebutuhan tersebut.

Pernyataan misi yang terlalu umum, seperti "menjadi perusahaan terbaik di industrinya", gagal menjalankan fungsi panduan ini karena tidak membedakan satu organisasi dari yang lain dan tidak memberi arah keputusan konkret.

### 3.3 Nilai Inti

Nilai inti (*core values*) adalah prinsip-prinsip perilaku yang bersifat *non-negotiable*, yaitu kompas moral yang berlaku bahkan ketika pelaksanaannya berbiaya tinggi. Nilai-nilai ini berfungsi sebagai pagar yang mencegah organisasi melenceng dari karakter dasarnya saat menghadapi tekanan kompetitif atau finansial yang intens.

Di Indonesia, beberapa contoh nilai inti yang konsisten dikomunikasikan antara lain Catur Dharma Astra, nilai AKHLAK yang ditetapkan Kementerian BUMN sebagai standar bagi seluruh perusahaan negara, serta nilai BCA SMART. Nilai-nilai inti hanya bermakna jika tercermin dalam perilaku nyata, bukan sekadar tertera dalam laporan tahunan.

### 3.4 Integrasi Visi, Misi, dan Nilai Inti

Ketiga elemen ini harus selaras dan saling menguatkan: visi menarik organisasi ke masa depan, misi memberi landasan pada identitas masa kini, dan nilai inti menyediakan pagar perilaku sepanjang perjalanan. Ketidakselarasan antara ketiganya, yang disebut *strategic dissonance*, menghasilkan konflik internal yang melemahkan kohesi organisasi dan pada akhirnya menurunkan kinerja. Contoh klasik Indonesia adalah BUMN yang memiliki visi "menjadi perusahaan kelas dunia" namun nilai inti yang bersifat birokratis dan menolak pengambilan risiko, sebuah kombinasi yang menjadikan ekspansi internasional tidak lebih dari wacana tahunan.

## 4. Tahap 2 — Penetapan Tujuan

Tujuan (*objectives*) adalah target terukur yang menerjemahkan visi abstrak menjadi *milestone* konkret. TPGS membedakan dua kategori tujuan yang sama-sama tidak dapat diabaikan.

**Tujuan finansial** (*financial objectives*) mencakup target-target yang berkaitan dengan kesehatan ekonomi organisasi: pertumbuhan pendapatan, margin laba, imbal hasil ekuitas, dan struktur modal. Tujuan finansial memastikan kelangsungan jangka pendek organisasi.

**Tujuan strategis** (*strategic objectives*) mencakup target yang berkaitan dengan posisi kompetitif dan kapabilitas jangka panjang: pangsa pasar, loyalitas pelanggan, kapasitas inovasi, dan pengembangan sumber daya manusia. Tujuan strategis memastikan organisasi terus membangun relevansi di masa depan, tidak hanya mengoptimalkan posisi saat ini.

Kaplan dan Norton (1992) dalam kerangka *Balanced Scorecard*, yang akan dibahas mendalam pada Pertemuan 11, mengingatkan bahwa organisasi yang hanya mengukur tujuan finansial cenderung mengorbankan investasi strategis demi angka triwulanan. Penetapan tujuan strategis yang kuat adalah antidot terhadap patologi jangka pendek ini.

Tujuan yang efektif memiliki dua horizon waktu: **jangka pendek** (satu tahun) untuk menegakkan disiplin eksekusi, dan **jangka panjang** (tiga hingga lima tahun) untuk mempertahankan fokus strategis saat kinerja jangka pendek berfluktuasi.

## 5. Tahap 3 — Perumusan Strategi: Tiga Level

Strategi tidak dirumuskan pada satu level. TPGS dan Henry (2021) membedakan tiga level strategi yang saling terkait dan harus selaras satu sama lain.

**Strategi tingkat korporat** (*corporate-level strategy*) adalah pilihan mengenai portofolio bisnis: ke industri mana perusahaan akan masuk atau keluar, apakah melalui pertumbuhan organik, akuisisi, atau divestasi. Strategi ini relevan bagi perusahaan diversifikasi seperti Astra International, Salim Group, dan Djarum Group yang mengelola berbagai unit bisnis di industri berbeda. Topik ini akan dibahas mendalam pada Pertemuan 9.

**Strategi tingkat bisnis** (*business-level strategy*) adalah pilihan mengenai cara bersaing dalam satu industri tertentu: apakah melalui kepemimpinan biaya (*cost leadership*), diferensiasi (*differentiation*), atau fokus pada ceruk tertentu (*focused*). Setiap unit bisnis dalam sebuah konglomerat memiliki strategi tingkat bisnis yang berbeda-beda. Kerangka Lima Strategi Generik Porter akan menjadi fokus Pertemuan 5.

**Strategi tingkat fungsional** (*functional-level strategy*) adalah pilihan operasional per departemen, mencakup pemasaran, operasi, sumber daya manusia, keuangan, dan teknologi informasi, yang mendukung strategi tingkat bisnis. Keselarasan antara strategi fungsional dan strategi bisnis adalah prasyarat eksekusi yang efektif; ketidakselarasan di antara keduanya menciptakan *functional silos* yang saling melemahkan satu sama lain.

*Strategic alignment*, yaitu keselarasan antara ketiga level ini, adalah salah satu tantangan terbesar manajemen. Pilihan korporat membatasi pilihan bisnis, dan pilihan bisnis membatasi pilihan fungsional. Ketidakselarasan di antara level-level ini adalah penyebab paling umum mengapa strategi yang tampak solid di atas kertas gagal ketika dieksekusi.

## 6. Tahap 4 — Implementasi dan Eksekusi Strategi

Strategi yang paling brilian sekalipun tidak menghasilkan apa pun tanpa eksekusi yang efektif. TPGS Ch.2 mengidentifikasi lima elemen pokok dalam implementasi strategi yang perlu dikelola secara terintegrasi.

**Pertama, alokasi sumber daya secara strategis.** Anggaran, talenta, modal, dan teknologi harus dialokasikan selaras dengan prioritas strategis, bukan secara merata atau berdasarkan inersia historis. Kesalahan umum yang disebut "*strategic peanut butter*" terjadi ketika sumber daya disebar tipis ke semua inisiatif sehingga tidak ada satu pun yang memiliki massa kritis untuk berhasil.

**Kedua, kebijakan dan prosedur** operasional harus mendukung, bukan menghalangi, eksekusi strategi. Kebijakan yang terlalu birokratis dapat mematikan inisiatif yang justru dibutuhkan untuk mengeksekusi strategi inovatif.

**Ketiga, penerapan *best practices*** dan perbaikan berkelanjutan melalui metodologi seperti *Six Sigma*, Lean, TQM, dan *benchmarking* membantu organisasi mempertahankan standar eksekusi yang kompetitif. Altıok (2011) mencatat bahwa TQM merupakan salah satu instrumen paling efektif dalam menghadapi krisis karena ia membangun kapasitas adaptasi organisasi secara sistematis.

**Keempat, sistem informasi dan operasi** yang andal, mencakup ERP, CRM, *data warehouse*, dan *dashboard* KPI, memungkinkan manajer memantau apakah strategi sedang berjalan sesuai rencana. Tanpa infrastruktur data yang memadai, tahap evaluasi menjadi mustahil.

**Kelima, budaya dan kepemimpinan** adalah penentu akhir keberhasilan eksekusi. Budaya organisasi berfungsi sebagai *amplifier* sekaligus peredam strategi: budaya yang mendukung akuntabilitas, *empowerment*, dan transparansi kinerja akan mempercepat eksekusi, sementara budaya yang birokratis dan berorientasi *blame* akan menghambatnya.

## 7. Tahap 5 — Evaluasi dan Penyesuaian

Tahap kelima menutup lingkaran proses dengan menyediakan mekanisme umpan-balik yang memungkinkan organisasi belajar dari kinerja aktual. Tiga pertanyaan kunci perlu dijawab secara berkala.

**Pertama**, apakah kinerja aktual memenuhi target yang ditetapkan? Ini pertanyaan retrospektif yang berbasis data finansial dan strategis.

**Kedua**, apakah asumsi lingkungan yang mendasari strategi masih valid? Perubahan teknologi, regulasi, atau perilaku konsumen dapat membuat strategi yang dulu tepat menjadi tidak relevan. Jika asumsi berubah, strategi di Tahap 3 perlu direvisi secara substantif.

**Ketiga**, apakah kapabilitas organisasi memadai untuk mengeksekusi strategi? Jika eksekusi terhambat oleh kekurangan talenta, sistem yang tidak memadai, atau budaya yang tidak kondusif, tindakan korektif di Tahap 4 diperlukan sebelum masalah berkembang lebih jauh.

Sifat iteratif proses ini, di mana umpan-balik dari Tahap 5 dapat memicu revisi di Tahap 1, 3, atau 4, adalah apa yang membuat manajemen strategis berbeda dari perencanaan bisnis konvensional. Organisasi yang unggul secara strategis adalah organisasi yang membangun kemampuan belajar dari kinerja aktualnya secara konsisten dan jujur.

## 8. Tata Kelola Perusahaan (*Corporate Governance*)

Di luar lima tahap proses, TPGS Ch.2 menempatkan *corporate governance* sebagai pilar yang tidak kurang pentingnya. Tata kelola perusahaan adalah kerangka mekanisme pengawasan yang memastikan manajemen tidak menyimpang dari kepentingan pemegang saham dan pemangku kepentingan yang lebih luas.

Indonesia menganut sistem dewan dua tingkat (*two-tier board*): **Dewan Komisaris** menjalankan fungsi pengawasan, sementara **Dewan Direksi** bertanggung jawab atas eksekusi strategi. Regulasi OJK mewajibkan setidaknya 30% dari anggota Dewan Komisaris berstatus komisaris independen, dimaksudkan untuk menjaga objektivitas pengawasan. Komite Audit berada di bawah Dewan Komisaris dan mengawasi keandalan pelaporan keuangan.

Kegagalan tata kelola di Indonesia memberikan pelajaran yang sangat mahal. Kasus Jiwasraya, dengan kerugian investasi sekitar Rp16 triliun yang terungkap pada 2020, dan kasus Asabri dengan kerugian sekitar Rp22 triliun pada 2021, menunjukkan bahwa ketersediaan dokumen visi-misi formal tidak cukup. Dibutuhkan mekanisme kontrol yang efektif untuk memaksa kepatuhan terhadap arah strategis yang telah ditetapkan. Kasus Garuda Indonesia pada 2019 hingga 2020, di mana rekayasa pengakuan pendapatan berlangsung tanpa terdeteksi oleh auditor eksternal, menegaskan bahwa tata kelola yang lemah dapat menggoyahkan bahkan perusahaan dengan merek yang sangat kuat.

Bagi mahasiswa akuntansi, implikasi ini sangat langsung: auditor internal dan akuntan manajemen yang memahami tata kelola strategis akan lebih mampu mengidentifikasi sinyal-sinyal peringatan dini sebelum krisis tata kelola berkembang menjadi skandal yang merugikan publik.

## 9. Kesimpulan

Pertemuan 2 membangun fondasi konseptual yang akan digunakan sepanjang semester. Lima tahap proses manajerial, yakni visi, tujuan, strategi, eksekusi, dan evaluasi, bukan rutinitas administratif melainkan cerminan cara organisasi membuat pilihan-pilihan yang bermakna di tengah ketidakpastian. Tata kelola yang efektif adalah penjaga agar pilihan-pilihan tersebut tetap selaras dengan kepentingan pemangku kepentingan.

Dua artikel empiris yang menyertai pertemuan ini memperkuat pemahaman teoretis dengan perspektif yang saling melengkapi. Altıok (2011) menekankan bahwa visi yang *applicable* adalah kapabilitas, bukan dokumen, yang menentukan ketahanan organisasi. Mohamed et al. (2019) menyediakan bukti kuantitatif bahwa investasi dalam formulasi strategi yang formal menghasilkan kinerja yang lebih baik secara statistis signifikan. Bersama-sama, keduanya menegaskan bahwa fondasi strategi yang kuat bukan sekadar kemewahan manajerial, melainkan kebutuhan yang mendasar dan terukur.
"""


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT 2 — CRITICAL REVIEW ARTIKEL 1 (ALTIOK 2011)
# ══════════════════════════════════════════════════════════════════════════════
CR1 = """\
# CRITICAL REVIEW ARTIKEL 1

**Mata Kuliah:** Manajemen Strategik Kontemporer (MST304)

**Semester:** II, T.A. 2025/2026

**Nama:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Identitas Artikel

**Judul:** *Applicable Vision, Mission and the Effects of Strategic Management on Crisis Resolve*

**Penulis:** Pınar Altıok

**Institusi:** Beykent University, Business Administration Program, Istanbul, Turki

**Publikasi:** *Procedia Social and Behavioral Sciences*, Vol. 24 (2011), hlm. 61–71

**Forum:** 7th International Strategic Management Conference

**Tipe Penelitian:** Artikel konseptual (*conceptual paper*)

## 2. Tujuan Penelitian

Artikel Altıok (2011) memiliki satu tujuan utama: menelaah secara konseptual bagaimana visi dan misi yang *applicable*, dalam artian benar-benar dapat diterapkan dan dimiliki bersama, mempengaruhi kemampuan organisasi untuk bertahan dan menyelesaikan krisis. Secara implisit, artikel ini juga menjawab pertanyaan diagnostik yang relevan: mengapa banyak perusahaan yang memiliki pernyataan visi dan misi formal tetap gagal ketika menghadapi tekanan krisis yang sesungguhnya?

Altıok berangkat dari premis bahwa dalam dunia yang makin terhubung dan *volatile* akibat globalisasi serta perkembangan teknologi informasi, krisis bukan lagi peristiwa langka melainkan komponen struktural dari dinamika bisnis modern. Oleh karena itu, kesiapan menghadapi krisis bukan lagi pilihan strategis, melainkan prasyarat kelangsungan organisasi.

## 3. Argumen Utama

Altıok membangun argumennya melalui tujuh bagian yang berurutan dan saling mendukung. Inti argumennya dapat diringkas sebagai berikut: visi yang sekadar ditulis sebagai slogan, tanpa dimiliki bersama (*shared*), tanpa memotivasi tindakan nyata, dan tanpa memandu pengambilan keputusan di level operasional, tidak memiliki nilai strategis yang sesungguhnya. Hanya visi yang *applicable* yang mampu berfungsi sebagai kompas organisasi saat krisis, ketika tekanan eksternal dan internal memuncak secara bersamaan.

Kontribusi utama Altıok adalah konsep *applicable vision*, yang ia definisikan sebagai visi yang: (a) dibentuk melalui partisipasi seluruh karyawan, bukan hanya manajemen puncak; (b) menciptakan loyalitas dan motivasi yang mengarahkan seluruh anggota organisasi pada satu tujuan bersama; dan (c) cukup konkret untuk mengarahkan pengambilan keputusan di tingkat operasional.

Altıok juga menghubungkan *applicable vision* dengan dua konsep pendukung yang penting. Pertama, konsep *learning organization* dari Peter Senge, di mana visi yang *applicable* menjadi prasyarat pembelajaran kolektif karena pembelajaran membutuhkan arah yang disepakati bersama. Kedua, *transformational leadership*, di mana pemimpin transformasional berperan sebagai agen yang tidak hanya memformulasikan visi, tetapi juga mengajak seluruh anggota organisasi untuk sungguh-sungguh memilikinya.

## 4. Koneksi ke Topik Silabus (Pertemuan 2 — TPGS Ch.2)

Artikel Altıok terhubung langsung dengan Tahap 1 proses manajerial dalam TPGS Ch.2, yakni pengembangan visi strategis. TPGS sendiri menetapkan tujuh kriteria visi yang efektif, termasuk *feasible* dan *desirable*. Altıok menambahkan dimensi yang lebih dalam: visi tidak hanya harus layak dan menarik, tetapi harus benar-benar *dimiliki* oleh seluruh organisasi, bukan sekadar ditetapkan oleh puncak hierarki.

Di sini Altıok melengkapi perspektif TPGS yang cenderung normatif, yaitu apa yang *seharusnya* ada dalam sebuah visi yang baik, dengan perspektif proses, yakni bagaimana visi itu seharusnya *dikonstruksi* agar memiliki kekuatan selama krisis. Dengan demikian, artikel ini memperkaya pemahaman Tahap 1 tanpa bertentangan dengan kerangka yang telah dibangun TPGS.

Dalam konteks *corporate governance* yang juga dibahas di TPGS Ch.2, *applicable vision* memiliki implikasi langsung. Dewan komisaris dan manajemen yang tidak dapat mengartikulasikan visi perusahaan secara konsisten dan koheren kepada semua lapisan organisasi sesungguhnya sedang mengekspos organisasi pada risiko krisis tata kelola yang lebih dalam dari yang terlihat di permukaan.

## 5. Kekuatan Artikel

**Pertama, kejelasan dan sistematika argumen.** Altıok menyusun argumennya secara logis dan berurutan, membawa pembaca dari premis (dunia makin *volatile*) ke diagnosis (banyak visi tidak *applicable*) hingga ke rekomendasi (*applicable vision* sebagai kapabilitas krisis). Alur ini memudahkan pembaca memahami posisi teoretis penulis tanpa harus bergulat dengan terminologi yang terlalu teknis.

**Kedua, jembatan antara dua tradisi literatur.** Altıok berhasil mengintegrasikan literatur manajemen strategis, yang diwakili oleh Thompson & Strickland dan Wheelen & Hunger, dengan literatur manajemen krisis yang diwakili oleh Augustine dan Pauchant, dalam satu kerangka konseptual yang koheren. Kontribusi ini tidak trivial karena dua tradisi tersebut jarang disintesiskan secara eksplisit dalam satu tulisan.

**Ketiga, relevansi manajerial yang tinggi.** Tulisan ini bukan sekadar akademis; ia menawarkan panduan praktis yang dapat digunakan oleh manajer dalam mendiagnosis kelemahan visi organisasi mereka dan memahami mengapa visi yang tampak kuat di atas kertas bisa runtuh ketika tekanan datang.

## 6. Keterbatasan dan Kelemahan

**Pertama, ketiadaan data empiris.** Ini adalah keterbatasan yang paling mendasar. Altıok mengklaim bahwa visi yang *applicable* meningkatkan ketahanan organisasi terhadap krisis, tetapi klaim sebab-akibat ini tidak diuji secara empiris. Artikel ini adalah *conceptual paper*, bukan studi empiris. Tanpa pengujian, klaim tersebut tetap berstatus proposisi teoretis yang menarik, namun belum terbukti.

**Kedua, ketiadaan operasionalisasi.** Bagaimana mengukur apakah sebuah visi benar-benar *applicable*? Altıok tidak menyediakan instrumen pengukuran atau indikator operasional. Akibatnya, seorang manajer yang membaca artikel ini tidak memiliki cara sistematis untuk menilai apakah visi organisasinya sudah atau belum memenuhi kriteria *applicable*.

**Ketiga, keterbatasan konteks geografis.** Beberapa contoh dan referensi dalam artikel ini bersumber dari krisis ekonomi Turki dan literatur berbahasa Turki yang tidak dapat diakses secara luas oleh pembaca internasional. Generalisasi ke konteks Asia Tenggara, termasuk Indonesia, memerlukan kehati-hatian yang serius.

**Keempat, definisi krisis yang terlalu luas.** Altıok mendefinisikan krisis sebagai "ketegangan tak-terduga yang mengancam nilai, tujuan, dan asumsi yang ada." Definisi ini terlalu inklusif karena mencakup krisis finansial global, bencana alam, gangguan rantai pasok, dan skandal reputasi sekaligus, sehingga tidak membantu membedakan jenis intervensi visi yang paling efektif untuk masing-masing tipe krisis.

## 7. Evaluasi Kritis

Altıok (2011) menulis pada saat yang tepat, yakni sesaat setelah krisis finansial global 2008, dan menjawab pertanyaan yang sangat relevan: mengapa krisis tersebut membuat banyak perusahaan kolaps meski mereka memiliki dokumen visi dan misi yang tampak solid? Jawabannya logis dan meyakinkan secara konseptual: visi yang hanya berupa dokumen formal tidak memiliki daya ikat ketika organisasi dihantam tekanan eksternal yang ekstrem.

Namun, terdapat satu kelemahan argumen yang cukup mendasar yang perlu dicermati. Altıok tidak mempertimbangkan kemungkinan bahwa hubungan kausalitas berjalan sebaliknya. Bisa jadi, organisasi yang memiliki kepemimpinan kuat dan budaya yang sehat, dua kondisi anteseden yang ia sendiri bahas, adalah yang akhirnya menghasilkan visi *applicable*, bukan sebaliknya. Dengan kata lain, visi *applicable* mungkin lebih merupakan *symptom* dari organisasi yang sehat daripada *cause*-nya.

Di samping itu, artikel ini tidak membahas batasan konsep secara kritis. Apakah ada kondisi di mana visi yang *applicable* justru menghambat adaptasi? Penelitian tentang *strategic inertia* (Leonard-Barton, 1992) menunjukkan bahwa kapabilitas inti yang terlalu kuat dapat menjadi *core rigidities* yang menghalangi perubahan. Visi yang terlalu kuat dimiliki bersama berpotensi menciptakan resistensi terhadap *pivot* strategis yang sebenarnya diperlukan ketika lanskap industri berubah secara fundamental.

Terlepas dari keterbatasan ini, artikel Altıok tetap merupakan kontribusi konseptual yang berguna, khususnya sebagai pengantar ke diskusi yang lebih komprehensif tentang hubungan antara visi, budaya, dan ketahanan organisasi.

## 8. Implikasi bagi Pemahaman Manajemen Strategik

**Pertama**, formulasi visi bukan sekadar latihan dokumentasi. Proses pembentukannya, seberapa inklusif dan seberapa partisipatif, menentukan seberapa dalam visi itu tertanam dalam budaya organisasi. Implikasi ini relevan bagi manajer yang bertanggung jawab atas proses perencanaan strategis karena cara visi dibentuk sama pentingnya dengan isi visi itu sendiri.

**Kedua**, investasi dalam komunikasi dan internalisasi visi adalah investasi dalam ketahanan organisasi jangka panjang. Perusahaan yang mengalokasikan sumber daya untuk memastikan bahwa seluruh karyawan memahami dan menginternalisasi visi tidak sekadar melakukan aktivitas HR; mereka sedang membangun kapabilitas menghadapi krisis yang tidak terlihat di neraca tetapi sangat nyata nilainya.

**Ketiga**, bagi auditor internal dan akuntan manajemen, pertanyaan tentang seberapa *applicable* visi organisasi seharusnya menjadi bagian dari asesmen risiko tata kelola. Organisasi dengan visi yang tidak tertanam secara kultural memiliki risiko *strategic drift* yang lebih tinggi, dan risiko ini layak masuk dalam peta risiko organisasi.

## 9. Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut

**Pertama**, apakah visi yang *applicable* selalu menguntungkan, atau apakah ada titik di mana visi yang terlalu kuat justru menghambat adaptasi strategis yang diperlukan? Kasus-kasus perusahaan yang gagal karena terlalu terikat pada identitas lamanya, seperti Kodak dan Blockbuster, layak diperbandingkan dengan argumen Altıok untuk menghasilkan pemahaman yang lebih bernuansa.

**Kedua**, bagaimana mengoperasionalisasi konsep "visi yang *applicable*" dalam konteks organisasi publik Indonesia, seperti BUMN atau instansi pemerintah, di mana tata kelola kepegawaian dan sistem insentif sangat berbeda dari sektor swasta? Apakah kerangka Altıok perlu dimodifikasi secara substansial untuk konteks ini?

**Ketiga**, apakah ketiadaan data empiris merupakan kelemahan fundamental yang mendiskualifikasi klaim Altıok, atau apakah proposisi konseptual yang kuat tetap bernilai tinggi meskipun belum teruji secara empiris? Debat tentang batas antara *conceptual contribution* yang sahih dan spekulasi akademis yang tidak terverifikasi merupakan pertanyaan epistemologis penting dalam ilmu manajemen.
"""


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT 3 — CRITICAL REVIEW ARTIKEL 2 (MOHAMED ET AL. 2019)
# ══════════════════════════════════════════════════════════════════════════════
CR2 = """\
# CRITICAL REVIEW ARTIKEL 2

**Mata Kuliah:** Manajemen Strategik Kontemporer (MST304)

**Semester:** II, T.A. 2025/2026

**Nama:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Identitas Artikel

**Judul:** *Towards a Better Understanding of the Relationship between Strategy Formulation (Vision, Mission, and Goals) and Organizational Performance*

**Penulis:** Fatin Mohamed, Mohammed Nusari, Ali Ameen, Valliappan Raju, Amiya Bhaumik

**Institusi:** Lincoln University College, Selangor, Malaysia

**Publikasi:** *Test Engineering and Management*, Vol. 81 (2019), hlm. 1987–1994

**Tipe Penelitian:** Empiris kuantitatif, *cross-sectional*, PLS-SEM

## 2. Tujuan Penelitian

Mohamed et al. (2019) memiliki tujuan yang relatif jelas: menguji secara empiris apakah ketiga komponen utama formulasi strategi, yakni visi (*vision*), misi (*mission*), dan tujuan (*goals*), memiliki hubungan yang positif dan signifikan dengan kinerja organisasi (*organizational performance*). Studi ini dilakukan di lingkungan Abu Dhabi Police (ADP), Uni Emirat Arab, sebagai representasi organisasi sektor publik yang memiliki tantangan tata kelola dan performa yang berbeda secara mendasar dari perusahaan swasta.

Konteks pemilihan lokasi studi menarik untuk dicermati: sebagian besar penelitian tentang hubungan formulasi strategi dan kinerja selama ini didominasi oleh konteks perusahaan swasta di negara-negara maju. Mohamed et al. berupaya mengisi kesenjangan tersebut dengan menguji hubungan yang sama di konteks sektor publik di kawasan Arab yang karakteristik institusional dan kulturalnya berbeda secara signifikan.

## 3. Argumen Utama

Tiga hipotesis paralel yang diajukan dalam studi ini adalah sebagai berikut:

**H1:** Formulasi strategi berupa visi berpengaruh positif terhadap kinerja organisasi.

**H2:** Formulasi strategi berupa misi berpengaruh positif terhadap kinerja organisasi.

**H3:** Formulasi strategi berupa tujuan berpengaruh positif terhadap kinerja organisasi.

Ketiga hipotesis diuji menggunakan *Partial Least Squares Structural Equation Modeling* (PLS-SEM) dengan perangkat lunak SmartPLS 3.0. Data dikumpulkan dari 423 responden melalui kuesioner dengan skala Likert lima poin. Hasil pengujian menunjukkan ketiga hipotesis didukung: visi, misi, dan tujuan masing-masing berpengaruh positif dan signifikan terhadap kinerja organisasi, dengan R² sebesar 0,41, artinya formulasi strategi menjelaskan 41% variansi kinerja organisasi.

Argumen inti Mohamed et al. adalah bahwa formulasi strategi yang jelas dan terstruktur bukan sekadar formalitas administratif, melainkan prediktor signifikan kinerja organisasi bahkan di lingkungan sektor publik yang umumnya dianggap kurang berorientasi strategi dibandingkan sektor swasta.

## 4. Koneksi ke Topik Silabus (Pertemuan 2 — TPGS Ch.2)

Artikel ini berkaitan langsung dengan Tahap 1 dan Tahap 2 proses manajerial dalam TPGS Ch.2: pengembangan visi strategis dan penetapan tujuan. Jika TPGS bersifat normatif dalam menetapkan bagaimana seharusnya visi dan tujuan dibentuk, maka Mohamed et al. memberikan validasi empiris atas pertanyaan apakah benar bahwa formulasi visi, misi, dan tujuan yang baik berhubungan dengan kinerja yang lebih tinggi.

Temuan Mohamed et al. memperkuat argumen normatif TPGS dengan bukti kuantitatif yang konkret. Bagi mahasiswa yang mungkin skeptis terhadap relevansi praktis "latihan perencanaan strategis", artikel ini menyediakan data yang berbicara langsung: 41% variansi kinerja dapat dijelaskan hanya oleh kualitas formulasi visi, misi, dan tujuan organisasi.

Artikel ini juga relevan dengan diskusi tentang *corporate governance* dalam TPGS Ch.2. Jika formulasi strategi memang berdampak signifikan pada kinerja, maka tata kelola yang buruk dalam proses formulasi strategi, termasuk visi yang dibentuk tanpa partisipasi bermakna atau tujuan yang ditetapkan tanpa hubungan dengan realitas kapabilitas organisasi, bukan sekadar masalah administratif melainkan risiko kinerja yang nyata dan terukur.

## 5. Kekuatan Artikel

**Pertama, desain metodologis yang cermat.** Penggunaan PLS-SEM adalah pilihan yang tepat untuk model dengan konstruk laten multi-indikator dan ukuran sampel yang tidak terlalu besar. Peneliti melakukan uji reliabilitas (Cronbach's *alpha* > 0,7; *composite reliability* > 0,7) dan validitas (AVE > 0,5; *discriminant validity* melalui kriteria Fornell-Larcker) secara sistematis sebelum menguji model struktural. Prosedur ini memastikan bahwa konstruk yang diukur benar-benar mencerminkan fenomena yang ingin dipahami.

**Kedua, kontribusi pada generalizability.** Sebagian besar penelitian tentang hubungan VMG (*vision-mission-goals*) dan kinerja berbasis perusahaan swasta di negara maju. Mohamed et al. menguji hubungan yang sama di konteks sektor publik di kawasan Arab dengan karakteristik kultural dan institusional yang berbeda, dan menemukan hubungan yang tetap signifikan. Ini memperluas rentang aplikabilitas temuan dalam literatur manajemen strategis.

**Ketiga, model paralel yang bernilai kontribusi.** Beberapa model sebelumnya mengasumsikan hubungan hierarkis linier: Visi → Misi → Goals → Performance. Mohamed et al. menguji model di mana ketiga komponen secara simultan dan mandiri mempengaruhi kinerja, dan menemukan bahwa ketiganya memiliki kontribusi independen yang signifikan. Temuan ini menyiratkan bahwa kualitas masing-masing komponen formulasi strategi memiliki nilai tambah tersendiri.

## 6. Keterbatasan dan Kelemahan

**Pertama, desain *cross-sectional* dan masalah kausalitas.** Keterbatasan paling mendasar: desain *cross-sectional* hanya mengukur hubungan pada satu titik waktu dan tidak dapat membuktikan kausalitas. Apakah formulasi strategi yang baik menyebabkan kinerja yang lebih tinggi, atau apakah organisasi yang berkinerja tinggi memiliki lebih banyak sumber daya dan kapasitas untuk memoles pernyataan visi-misi-tujuan mereka? Pertanyaan penting ini tidak dapat dijawab oleh desain yang digunakan.

**Kedua, kinerja yang diukur secara *self-reported*.** Kinerja organisasi diukur melalui persepsi responden menggunakan skala Likert, bukan melalui data objektif seperti anggaran yang terealisasi, tingkat kejahatan yang turun, atau indikator kepuasan publik. Risiko *common-method bias*, di mana responden yang menilai tinggi visi organisasi cenderung juga menilai tinggi kinerja organisasi, tidak dapat sepenuhnya dikontrol.

**Ketiga, konteks tunggal yang sangat spesifik.** Satu organisasi, satu industri, satu negara, pada satu titik waktu. Seberapa jauh temuan ini dapat digeneralisasi ke konteks BUMN Indonesia, perusahaan manufaktur swasta di Asia Tenggara, atau lembaga pendidikan tinggi? Generalisasi memerlukan replikasi yang serius di berbagai konteks.

**Keempat, operasionalisasi konstruk yang terbatas.** Visi, misi, dan tujuan diukur melalui persepsi responden tentang keberadaan dan kejelasannya, bukan tentang kualitas substantif dokumen tersebut. Ini berarti Mohamed et al. dan Altıok (2011) sesungguhnya mengukur fenomena yang berbeda: Mohamed et al. mengukur *apakah* visi-misi-tujuan ada dan dipersepsikan jelas, sementara Altıok membahas *seberapa applicable* visi tersebut. Keduanya saling melengkapi tetapi tidak identik, dan perbedaan ini penting untuk dipahami.

## 7. Evaluasi Kritis

Mohamed et al. (2019) memberikan kontribusi yang bermakna dengan menyediakan bukti kuantitatif dalam konteks yang relatif jarang diteliti. Namun, beberapa pertanyaan kritis layak diajukan secara serius.

R² sebesar 0,41 terkesan impresif, tetapi angka ini tidak membuktikan bahwa "formulasi strategi yang baik menyebabkan kinerja yang lebih tinggi." Dalam konteks desain *cross-sectional*, koefisien ini hanya menunjukkan asosiasi, bukan kausalitas. Bisa jadi, Abu Dhabi Police sebagai institusi yang mendapat prioritas anggaran tinggi dari pemerintah UEA telah terlebih dahulu memiliki sumber daya yang memungkinkan mereka membangun sistem perencanaan yang lebih serius, dan sistem perencanaan yang serius tersebut kemudian menghasilkan persepsi kinerja yang lebih baik.

Pilihan konteks juga layak dipertanyakan. Abu Dhabi Police adalah organisasi paramiliter dengan hierarki yang sangat kuat dan rekrutmen berbasis loyalitas institusional. Dalam konteks seperti ini, responden mungkin enggan memberikan penilaian negatif terhadap visi atau kinerja organisasi mereka karena tekanan sosial (*social desirability bias*). Kondisi ini berbeda secara mendasar dari lingkungan korporat swasta di mana responden lebih bebas memberikan penilaian kritis.

Ketiadaan variabel moderator juga merupakan kelemahan yang signifikan. Hubungan antara formulasi strategi dan kinerja hampir pasti dimoderasi oleh faktor-faktor seperti ukuran organisasi, usia organisasi, tingkat turbulensi lingkungan, dan kualitas kepemimpinan. Mengabaikan moderator-moderator ini menghasilkan model yang terlalu simplistis untuk memberikan panduan manajerial yang kaya.

Terlepas dari keterbatasan tersebut, artikel Mohamed et al. tetap menjadi salah satu studi empiris yang paling sering dikutip dalam konteks hubungan VMG-kinerja di sektor publik kawasan Arab, sebuah posisi yang mencerminkan nilai kontribusinya meski keterbatasan metodologisnya perlu selalu diingat.

## 8. Implikasi bagi Pemahaman Manajemen Strategik

**Pertama**, artikel ini memperkuat argumen bahwa investasi waktu manajerial dalam formulasi visi, misi, dan tujuan yang serius bukan pemborosan. Ia memiliki korelasi yang terukur dengan kinerja organisasi. Implikasi ini relevan bagi manajer yang skeptis terhadap proses perencanaan strategis yang dianggap terlalu abstrak atau memakan waktu.

**Kedua**, temuan ini memiliki implikasi khusus bagi reformasi tata kelola BUMN Indonesia. Program transformasi AKHLAK yang diluncurkan Kementerian BUMN pada 2020, yang antara lain memperkuat formulasi visi dan nilai inti BUMN, dapat diinterpretasikan melalui lensa artikel ini sebagai langkah yang memiliki dasar empiris, bukan sekadar latihan *rebranding*. Namun, perlu diingat bahwa Mohamed et al. hanya mengukur keberadaan dan kejelasan visi, bukan kualitas *applicability*-nya dalam pengertian Altıok.

**Ketiga**, bagi peneliti di bidang akuntansi manajemen, artikel ini membuka ruang penelitian yang menarik: apakah kualitas sistem pengendalian manajemen, termasuk BSC, KPI, dan sistem pelaporan kinerja, memediasi hubungan antara formulasi strategi dan kinerja aktual? Pertanyaan ini sangat relevan untuk agenda penelitian tesis di program Magister Akuntansi.

## 9. Isu untuk Didebatkan dan Didiskusikan Lebih Lanjut

**Pertama**, jika R² sebesar 0,41 menunjukkan bahwa formulasi strategi menjelaskan 41% variansi kinerja, apa yang menjelaskan 59% sisanya? Apakah faktor-faktor tersebut lebih mudah dikontrol oleh manajer, atau justru lebih sulit? Diskusi ini penting agar mahasiswa tidak mengambil kesimpulan berlebihan dari temuan statistik dan memahami bahwa formulasi strategi adalah satu variabel dalam ekosistem manajemen yang kompleks.

**Kedua**, bagaimana hasil Mohamed et al. harus diinterpretasikan di konteks organisasi Indonesia yang sangat beragam, mulai dari konglomerat keluarga seperti Salim Group yang visi strategisnya sangat terpusat pada pemegang saham mayoritas, hingga BUMN multi-stakeholder seperti PLN yang harus menyeimbangkan tujuan komersial dengan mandat publik? Apakah hubungan VMG-kinerja berlaku secara seragam di seluruh konteks tersebut, atau apakah pola hubungannya berbeda secara mendasar?

**Ketiga**, Altıok (2011) dan Mohamed et al. (2019) secara bersama-sama menyiratkan bahwa visi yang baik adalah kondisi yang diperlukan (*necessary*) untuk kinerja tinggi. Tetapi apakah ia juga kondisi yang mencukupi (*sufficient*)? Kasus-kasus perusahaan dengan visi yang kuat namun kinerja yang buruk menantang kita untuk mempertanyakan apa yang hilang dari kerangka yang dibangun oleh kedua artikel ini.
"""


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    OUT_RMK.mkdir(parents=True, exist_ok=True)
    OUT_CR.mkdir(parents=True, exist_ok=True)

    create_reference()

    pandoc(
        write_md(RMK, "rmk_pert2.md"),
        OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 2.docx",
    )
    pandoc(
        write_md(CR1, "artikel1.md"),
        OUT_CR / "01079_Dzaki Muhammad Yusfian_Artikel 1.docx",
    )
    pandoc(
        write_md(CR2, "artikel2.md"),
        OUT_CR / "01079_Dzaki Muhammad Yusfian_Artikel 2.docx",
    )

    print("\nAll three documents generated successfully.")
    print(f"RMK : {OUT_RMK}")
    print(f"CR  : {OUT_CR}")


if __name__ == "__main__":
    main()
