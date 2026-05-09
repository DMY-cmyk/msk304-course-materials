"""Generate enhanced RMK Pertemuan 6 with embedded TPGS Ch.6 figures.

Pipeline:
  1. Extract Figure 6.1 + three Concepts & Connections boxes from the TPGS PDF.
  2. Build the enhanced RMK Markdown (existing 9 sections preserved + new
     content from TPGS Ch.6 + new section 10 Key Points).
  3. Run Pandoc to overwrite RMK Pert. 6 .docx.

Source spec: docs/superpowers/specs/2026-05-09-rmk6-enhanced-design.md
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import fitz  # PyMuPDF

# ════════════════════════════════════════════════════════════════════════════
# PATHS
# ════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR   = Path(__file__).parent
PROJECT_ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
EBOOK        = PROJECT_ROOT / "Ebook" / (
    "(Business professional collection) John E. Gamble_ Arthur A. Thompson_ "
    "Margaret Ann Peteraf - Essentials of Strategic Management _ "
    "The Quest for Competitive Advantage (2021).pdf"
)
OUT_RMK      = PROJECT_ROOT / "RMK"
TEMP         = PROJECT_ROOT / "Dev Assistant" / "temp"
FIGURES_DIR  = TEMP / "ch6_figures"
REFERENCE    = SCRIPT_DIR / "reference.docx"
PANDOC       = r"C:\Program Files\Pandoc\pandoc.exe"


# ════════════════════════════════════════════════════════════════════════════
# PHASE 1 — FIGURE EXTRACTION
# ════════════════════════════════════════════════════════════════════════════
def extract_figures(ebook_path: str, figures_dir: Path) -> dict:
    """Extract Figure 6.1 and three Concepts & Connections boxes from TPGS Ch.6."""
    figures_dir.mkdir(parents=True, exist_ok=True)
    mat = fitz.Matrix(2, 2)
    results: dict[str, Path] = {}

    with fitz.open(ebook_path) as doc:
        # Figure 6.1 — diagram on PDF page index 149 (reader p.150)
        pg = doc[149]
        hits = pg.search_for("FIGURE 6.1")
        if hits:
            r = hits[0]
            clip = fitz.Rect(30, r.y0 - 5, pg.rect.width - 30, pg.rect.height - 30)
            used = "anchor"
        else:
            h = pg.rect.height
            clip = fitz.Rect(30, h * 0.45, pg.rect.width - 30, h - 30)
            used = "fallback (WARNING: anchor not found)"
        pix = pg.get_pixmap(matrix=mat, clip=clip)
        out = figures_dir / "figure_6_1.png"
        pix.save(str(out))
        results["figure_6_1"] = out
        print(f"  figure_6_1: clip via {used}")

        # Concepts & Connections boxes
        cc_specs = [
            ("cc_6_1_etsy",    "CONCEPTS & CONNECTIONS 6.1", [153, 154]),
            ("cc_6_2_walmart", "CONCEPTS & CONNECTIONS 6.2", [159, 160]),
            ("cc_6_3_tesla",   "CONCEPTS & CONNECTIONS 6.3", [163, 164]),
        ]
        for name, anchor, pg_indices in cc_specs:
            clipped = False
            for pg_idx in pg_indices:
                pg = doc[pg_idx]
                hits = pg.search_for(anchor)
                if hits:
                    r = hits[0]
                    clip = fitz.Rect(30, r.y0 - 5, pg.rect.width - 30, pg.rect.height - 30)
                    pix = pg.get_pixmap(matrix=mat, clip=clip)
                    out = figures_dir / f"{name}.png"
                    pix.save(str(out))
                    results[name] = out
                    clipped = True
                    print(f"  {name}: anchor on page index {pg_idx}")
                    break
            if not clipped:
                pg = doc[pg_indices[0]]
                pix = pg.get_pixmap(matrix=mat)
                out = figures_dir / f"{name}.png"
                pix.save(str(out))
                results[name] = out
                print(f"  {name}: WARNING anchor not found, fallback full page index {pg_indices[0]}")

    return results


def validate_figures(results: dict) -> None:
    """Confirm every PNG exists and is at least 10 KB."""
    for key in ["figure_6_1", "cc_6_1_etsy", "cc_6_2_walmart", "cc_6_3_tesla"]:
        path = results.get(key)
        if not path or not path.exists():
            raise FileNotFoundError(f"Missing figure: {key}")
        size = path.stat().st_size
        if size < 10_000:
            raise ValueError(f"{key} too small: {size} bytes")
        print(f"  OK {key}: {size:,} bytes")


# ════════════════════════════════════════════════════════════════════════════
# PHASE 2 — ENHANCED RMK CONTENT
# ════════════════════════════════════════════════════════════════════════════
def build_rmk_content(figures_dir: Path) -> str:
    """Build full enhanced RMK Markdown string with embedded images."""

    def img_path(name: str) -> str:
        return str(figures_dir / name).replace("\\", "/")

    fig1    = img_path("figure_6_1.png")
    etsy    = img_path("cc_6_1_etsy.png")
    walmart = img_path("cc_6_2_walmart.png")
    tesla   = img_path("cc_6_3_tesla.png")

    return f"""# RINGKASAN MATERI KULIAH — PERTEMUAN 6

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Topik:** *Strengthening a Company's Competitive Position: Strategic Moves, Timing, and Scope of Operations* (TPGS Ch.6 + Henry Ch.5–6)

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Pendahuluan

### Transisi dari Pilihan Generik ke Penguatan Posisi

Pertemuan 5 menutup pembahasan dengan pertanyaan klasifikasi: posisi generik mana yang harus diambil perusahaan agar sumber daya internalnya menghasilkan keunggulan yang tahan lama. Jawaban Porter (1985) — *low-cost provider*, *broad differentiation*, *focused low-cost*, *focused differentiation*, dan *best-cost provider* — menyediakan peta yang jelas tetapi tidak lengkap. Memilih posisi adalah keputusan awal; mempertahankan dan memperdalam posisi tersebut di tengah dinamika pesaing, perubahan teknologi, dan pergeseran preferensi konsumen adalah pekerjaan yang jauh lebih panjang dan kompleks. Pertemuan 6 mengisi celah ini dengan tiga keluarga keputusan strategik: gerakan ofensif dan defensif (*strategic moves*), strategi waktu (*timing*), serta keputusan tentang lingkup operasi (*scope of operations*).

Di sinilah perbedaan epistemologis penting muncul. Pertemuan 5 berfokus pada *content* strategi — apa yang dipilih. Pertemuan 6 bergeser ke *process* strategi — bagaimana pilihan itu dijaga, diperdalam, dan dikalibrasi. Henry (2021) menjembatani kedua orientasi ini dengan menempatkan diskusi *strategic moves* dalam konteks lima kekuatan industri yang sudah dikenal mahasiswa, sementara TPGS Ch.6 (Gamble, Peteraf & Thompson 2021) menyediakan taksonomi taktis yang lebih kaya tentang kapan dan bagaimana setiap gerakan dipilih.

![*Gambar 6.1 — Strategi untuk Memperkuat Posisi Kompetitif Perusahaan*]({fig1})

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.111*

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

### Memilih Basis Serangan Kompetitif (TPGS Ch.6, p.151)

TPGS mengidentifikasi enam basis yang dapat dipilih sebuah perusahaan ketika memutuskan menyerang pesaing:

1. **Keunggulan biaya** — menyerang dengan harga lebih rendah ketika pesaing tidak dapat menandingi struktur biaya
2. **Segmen pembeli yang kurang terlayani** (*underserved buyer segments*) — mengisi kebutuhan yang diabaikan pemain dominan
3. **Celah kualitas, layanan, atau fitur** — menawarkan produk yang lebih baik di dimensi yang diabaikan pesaing
4. **Inovasi produk atau proses** — melompati generasi teknologi pesaing dengan *leapfrog innovation*
5. **Kesenjangan kesadaran merek** — membangun *brand* di pasar di mana pemimpin memiliki kelemahan reputasi
6. **Celah distribusi** — memasuki saluran distribusi yang belum dimanfaatkan pesaing utama

**Kelima basis ini bukan pilihan eksklusif** — perusahaan yang sukses sering menggabungkan dua atau tiga basis sekaligus, misalnya menyerang dengan keunggulan biaya pada segmen yang kurang terlayani melalui saluran distribusi yang belum dimanfaatkan pesaing.

### Memilih Pesaing yang Akan Diserang (TPGS Ch.6, p.152)

Setelah basis serangan dipilih, pertanyaan berikutnya adalah pesaing mana yang menjadi target. TPGS membedakan tiga kategori target:

- **Pemimpin pasar yang rentan**: efektif ketika pemimpin lalai, memiliki kelemahan produk/layanan, atau tidak merespons perubahan pasar. Tanda-tanda kerentanan termasuk profitabilitas yang menurun, pelanggan yang tidak puas, dan investasi *brand* yang mulai meredup.
- **Perusahaan *runner-up***: target yang lebih mudah karena sumber daya lebih terbatas dan posisi lebih lemah. Menyerang *runner-up* sering memberikan kemenangan yang lebih cepat dan memperkuat posisi penyerang sebelum berhadapan dengan pemimpin.
- **Menghindari *strong fighters***: perusahaan dengan kas dalam, kapasitas produksi cadangan, dan kemauan membalas. **Menyerang *strong fighter* hampir selalu berakhir mahal tanpa hasil**, karena pesaing tipe ini memiliki kemauan dan kemampuan untuk merespons dengan kerusakan resiprokal yang substansial.

### Kapan Menyerang vs. Kapan Mengisi Celah

**Pertanyaan kritis bukan seberapa agresif menyerang melainkan apakah perusahaan benar - benar memiliki kondisi yang memungkinkan serangan berhasil.** TPGS Ch.6 menyebut tiga prasyarat: superioritas sumber daya yang dapat dipertahankan, target yang lebih lemah daripada yang terlihat di permukaan, dan kemampuan menyerap balasan dari pesaing. Bila salah satu prasyarat ini tidak terpenuhi, alternatif yang lebih masuk akal adalah mengisi celah pasar yang tidak diperebutkan, yang dalam terminologi *Blue Ocean* (Kim & Mauborgne 2005) disebut sebagai *uncontested market space*. Banyak perusahaan Indonesia yang lebih bijak memilih jalur kedua: Kopi Kenangan tidak menyerang Starbucks dalam segmen *premium specialty* melainkan menciptakan kategori *affordable specialty coffee* dengan harga di bawah Rp 25.000.

---

## 3. *Defensive Strategies*

### *Fortify-and-Defend*

*Fortify-and-defend* adalah strategi defensif paling dasar: memperkuat posisi yang sudah dimiliki sehingga biaya menyerangnya menjadi prohibitif bagi pesaing. Bentuk konkretnya adalah investasi berkelanjutan dalam dimensi yang menjadi sumber keunggulan — *brand* untuk diferensiator, efisiensi untuk *cost leader* — sehingga setiap upaya menandingi memerlukan investasi yang tidak proporsional. **Strategi ini efektif ketika perusahaan benar - benar memimpin pasar dan memiliki kemampuan untuk terus berinvestasi pada dimensi yang menjadi sumber keunggulannya. Strategi ini gagal ketika investasi pada dimensi tersebut menjadi rutin dan tidak lagi menciptakan diferensiasi nyata bagi pelanggan**, kondisi yang dalam literatur disebut *competitive parity creep*.

### Memblokir Jalur yang Terbuka bagi Penantang (TPGS Ch.6, p.154)

TPGS memberi taksonomi konkret tentang bagaimana operasionalisasi *fortify-and-defend*, yaitu dengan secara aktif menutup jalur yang terbuka bagi penantang potensial:

- **Memperluas lini produk** untuk menutup celah yang dapat dieksploitasi penantang
- **Memperkenalkan model ekonomi dan premium** untuk menutup rentang harga yang kosong
- **Mempertahankan hubungan kuat dengan dealer dan distributor** melalui insentif eksklusif jangka panjang
- **Menawarkan program loyalitas pembeli** yang meningkatkan *switching costs*
- **Membangun kapasitas cadangan** untuk dapat merespons serangan dengan cepat dan agresif

Logika di balik kelima taktik ini sama: **mengurangi jumlah celah yang dapat dimanfaatkan pesaing**, sehingga setiap calon penantang harus menanggung biaya masuk yang substansial sebelum bahkan dapat memulai serangan.

### *Signaling*: Teori Kredibilitas

*Signaling* adalah pengiriman sinyal kepada pesaing tentang konsekuensi yang akan diterima bila mereka melakukan gerakan tertentu. Schelling (1960) dalam *The Strategy of Conflict* menjelaskan bahwa ancaman hanya efektif bila kredibel, dan kredibilitas dibangun dengan komitmen yang sulit dibatalkan. *Brand investment* yang masif, kontrak jangka panjang dengan distributor, atau pengumuman publik tentang investasi *capacity expansion* yang besar adalah bentuk *signaling*: bila pesaing tahu bahwa perusahaan telah menanamkan komitmen yang besar untuk mempertahankan posisinya, biaya serangan akan dipersepsikan lebih tinggi karena perusahaan tidak akan mundur. Sampoerna selama dekade 2000-an menggunakan *brand architecture* berlapis — A Mild, Sampoerna Hijau, Dji Sam Soe — sebagai sinyal kepada Gudang Garam dan Bentoel bahwa perusahaan tidak akan menyerahkan satu pun segmen tanpa pertahanan ekonomis yang substansial.

### Memberi Sinyal Bahwa Pembalasan Sangat Mungkin (TPGS Ch.6, p.154)

Per *credibility theory* (Schelling 1960): ancaman pembalasan hanya efektif jika **kredibel** — artinya, biaya *tidak* membalas harus lebih tinggi dari biaya membalas. TPGS mengidentifikasi empat sinyal yang efektif dalam praktik:

- **Pengumuman publik** tentang niat mempertahankan posisi dengan tegas, sehingga setiap kemunduran akan menjadi kerugian reputasi yang nyata
- **Segera menyamakan atau melampaui pemotongan harga pesaing**, sehingga penantang tidak dapat mengakumulasi pangsa dari taktik harga jangka pendek
- **Membangun *war chest* kas dan surat berharga yang tampak dari luar** — sinyal bahwa perusahaan siap secara finansial untuk *price war* berkepanjangan
- ***Cross-parry*** — menyerang balik di pasar asal pesaing, sehingga pesaing harus menimbang risiko kerusakan pada bisnis intinya sendiri sebelum melancarkan serangan

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

### Kerangka Keputusan: *Early Mover* vs. *Late Mover* (TPGS Ch.6, p.156)

TPGS memberikan kerangka keputusan eksplisit untuk membantu manajer memutuskan kapan harus masuk lebih awal dan kapan menunda.

**Faktor pendukung masuk lebih awal (*early entry*):**

- Kurva belajar yang curam — keunggulan biaya permanen dari akumulasi pengalaman
- Pra-emosi sumber daya langka (lokasi, bahan baku, talenta teknis)
- *Network effects* — nilai platform meningkat seiring pertambahan pengguna awal
- *Switching costs* yang terbentuk kuat — pelanggan pertama cenderung bertahan
- Preferensi merek yang terbentuk sebelum pesaing masuk

**Faktor pendukung masuk lebih lambat (*late entry*):**

- Menghindari biaya perintisan (*pioneering costs*) — edukasi pasar, kesalahan generasi awal
- Belajar dari kesalahan *early mover* tanpa menanggung biayanya
- *Free-ride* pada edukasi pasar yang sudah dilakukan *early mover*
- Melompati teknologi generasi pertama ke generasi berikutnya
- Pasar yang sudah teredukasi dan siap membeli dalam skala lebih besar

**Aturan praktis dari kerangka ini**: semakin banyak faktor pendukung *early entry* yang aktif di industri tertentu, semakin tinggi kerugian menunggu; sebaliknya, semakin banyak faktor *late entry* yang aktif, semakin tinggi kerugian terburu-buru masuk.

### Aturan Emas Timing

**Aturan emas yang dapat ditarik adalah: pilih untuk menjadi *first-mover* hanya ketika lima mekanisme keunggulan dapat diaktifkan dan tiga beban dapat diserap; pilih *fast-follower* ketika pesaing pionir dapat mengedukasi pasar untuk Anda; pilih *late-mover* hanya ketika *complementary asset* yang dimiliki cukup masif untuk mengatasi *first-mover advantage* yang sudah terkunci.** Kesalahan paling umum adalah memilih *first-mover* untuk alasan psikologis (gengsi pionir) tanpa kalkulasi mekanisme dan beban.

---

## 5. *Scope of Operations*

### *Vertical Integration*

*Vertical integration* adalah keputusan memperluas lingkup aktivitas perusahaan ke arah hulu (pemasok) atau hilir (distribusi/pelanggan). Backward integration mengamankan input kritis dan margin pemasok; forward integration mengamankan akses pelanggan dan margin distributor. Pertamina secara historis melakukan backward integration dari distribusi BBM ke kilang dan eksplorasi hulu, menciptakan kontrol penuh terhadap *value chain* energi nasional. Telkom Indonesia melakukan vertical integration di broadband — dari infrastruktur fiber, jaringan, hingga layanan *content* — sehingga *bottleneck* di salah satu lapisan dapat dikontrol langsung. Keuntungan integrasi vertikal adalah kontrol kualitas, kepastian pasokan, dan *margin capture*; biayanya adalah hilangnya fleksibilitas dan beban modal yang tinggi.

![*Gambar 6.2 — Concepts & Connections 6.3: Tesla's Vertical Integration Strategy*]({tesla})

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.124*

### Empat Keunggulan Integrasi Vertikal (TPGS Ch.6, p.161–162)

TPGS menyusun empat keunggulan strategik integrasi vertikal yang menjelaskan mengapa perusahaan seperti Tesla bersedia menanggung beban modal yang tinggi:

1. **Memperkuat diferensiasi dan keunggulan kompetitif** — kontrol atas proses hulu/hilir memungkinkan konsistensi kualitas yang sulit ditiru pesaing
2. **Mengurangi ketergantungan pada pemasok yang kuat** — eliminasi *supplier bargaining power* dalam analisis Five Forces
3. **Mengurangi ketergantungan pada pembeli yang kuat** — kepemilikan saluran distribusi sendiri menghilangkan *leverage* pembeli besar
4. **Membangun *barriers to entry*** — biaya dan kompleksitas menduplikasi rantai vertikal terintegrasi sangat tinggi bagi calon pendatang baru

### Tiga Kelemahan Integrasi Vertikal (TPGS Ch.6, p.163)

Sebagai penyeimbang, TPGS juga menyebut tiga kelemahan struktural yang membuat integrasi vertikal tidak selalu pilihan optimal:

1. **Meningkatkan investasi modal dan risiko bisnis** — semakin banyak rantai yang dimiliki, semakin besar eksposur terhadap siklus industri secara keseluruhan
2. **Membatasi fleksibilitas strategis** — sulit beralih pemasok atau pembeli jika teknologi atau pasar berubah arah
3. **Mungkin tidak kompetitif secara biaya** — operasi internal yang tidak mencapai skala minimum menjadi lebih mahal daripada menggunakan spesialis eksternal

**Kesimpulan praktis**: integrasi vertikal masuk akal hanya ketika empat keunggulan secara nyata dapat diaktifkan dan tiga kelemahan dapat diserap — bukan sekadar ketika kontrol penuh atas rantai nilai terdengar menarik.

### *Strategic Outsourcing* dan Risiko *Hollowing-Out*

*Strategic outsourcing* adalah keputusan menyerahkan aktivitas tertentu kepada mitra eksternal yang lebih efisien atau lebih ahli. Logikanya adalah fokus pada *core competence* dan biarkan aktivitas non-inti dijalankan oleh pemain spesialis. **Risiko terbesar adalah *hollowing-out*: perusahaan kehilangan kapabilitas yang seharusnya menjadi sumber keunggulan jangka panjang karena aktivitas yang menumbuhkan kapabilitas itu telah dialihdayakan.** Industri elektronika konsumen Amerika dalam dekade 1990-an–2000-an adalah pelajaran klasik: ketika manufaktur perangkat keras dialihdayakan ke kontraktor Asia, kemampuan integrasi *hardware-software* yang menjadi sumber inovasi juga ikut hilang. Kapabilitas yang sudah hilang sangat sulit dibangun kembali.

### *Strategic Alliances* dan *Joint Ventures*

*Strategic alliance* adalah kerja sama formal tanpa pembentukan entitas baru, sementara *joint venture* membentuk entitas baru yang dimiliki bersama. Astra International adalah arketipe perusahaan Indonesia dengan jaringan aliansi yang ekstensif: *joint venture* dengan Honda dan Toyota di otomotif, dengan Daihatsu, dengan United Tractors di alat berat. Logika strategik aliansi adalah berbagi risiko, mengakses kapabilitas yang tidak dimiliki, dan mempercepat *time to market*. Trade-off klasik adalah antara *speed*, *control*, dan *learning*: aliansi memberi kecepatan dan akses pembelajaran tetapi mengorbankan kontrol; akuisisi memberi kontrol penuh tetapi memerlukan modal dan integrasi yang mahal.

### Mengapa Aliansi Strategis Gagal (TPGS Ch.6, p.166)

TPGS mengidentifikasi **lima penyebab kegagalan aliansi**:

1. **Tujuan yang berubah seiring waktu** — kepentingan mitra yang awalnya selaras berevolusi ke arah yang berbeda
2. **Hilangnya sensitivitas kompetitif** — berbagi informasi *proprietary* menciptakan risiko transfer pengetahuan kepada pesaing
3. ***Free-riding*** — satu pihak mendapat manfaat lebih besar dari kontribusinya; asimetri ini merusak kepercayaan
4. **Ketidakpercayaan dari berbagi pengetahuan** — setelah IP dibagikan, sulit dilindungi kembali jika aliansi putus
5. **Koordinasi lintas budaya yang sulit** — perbedaan sistem manajemen, bahasa, dan ekspektasi menciptakan friksi operasional

### Bahaya Mengandalkan Aliansi untuk Kapabilitas Esensial (TPGS Ch.6, p.167)

**Risiko "pengosongan kapabilitas" (*hollowing out*)** adalah yang paling berbahaya dalam jangka panjang. TPGS memperingatkan: jika perusahaan secara konsisten mengandalkan aliansi untuk kapabilitas inti, perusahaan tersebut secara bertahap kehilangan kemampuan untuk membangun kembali kapabilitas itu secara internal ketika aliansi berakhir. **Prinsip**: aliansi boleh digunakan untuk *akses* kapabilitas secara cepat, tetapi tidak boleh menggantikan *pembangunan* kapabilitas internal jangka panjang.

### *Mergers & Acquisitions*

*M&A* adalah perluasan lingkup melalui pengambilalihan atau penggabungan perusahaan lain. Merger GoTo (Gojek dan Tokopedia) pada 2021 adalah contoh ekspansi lingkup yang ambisius: dua *super-app* yang saling melengkapi digabungkan untuk menciptakan ekosistem digital end-to-end. Logikanya adalah skala, sinergi, dan posisi defensif terhadap pemain global. Risiko M&A adalah eksekusi integrasi: literatur menunjukkan mayoritas merger gagal menciptakan nilai karena masalah integrasi budaya, sistem, dan insentif yang diremehkan dalam fase deal-making.

![*Gambar 6.3 — Concepts & Connections 6.2: Walmart's Acquisition of Jet.com*]({walmart})

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.120*

### Mengapa M&A Sering Gagal Memenuhi Ekspektasi (TPGS Ch.6, p.159)

TPGS mengidentifikasi **lima penyebab utama kegagalan M&A**:

1. **Melebih-estimasi sinergi** (*overestimating synergies*) — integrasi lebih sulit dari proyeksi; penghematan biaya tidak terealisasi penuh dalam praktik — **faktor paling umum**
2. **Kesulitan integrasi operasional** — sistem IT, proses kerja, dan struktur organisasi tidak mudah digabungkan tanpa gangguan kinerja
3. ***Culture clash*** — perbedaan nilai, gaya manajemen, dan cara kerja yang tidak terselesaikan menciptakan friksi jangka panjang
4. **Membayar premi terlalu tinggi** — *winner's curse* dalam proses lelang akuisisi kompetitif
5. **Gangguan fokus manajemen** — eksekutif terlalu fokus pada integrasi, mengabaikan ancaman dan peluang di bisnis inti

### *Transaction Cost Economics* sebagai Kerangka *Make-or-Buy*

**Williamson (1975, 1985) dengan *Transaction Cost Economics* (TCE) menyediakan kerangka analitis untuk keputusan *make-or-buy*.** Tiga variabel kunci menentukan apakah aktivitas sebaiknya diinternalkan atau dialihdayakan: *asset specificity* (seberapa khusus aset yang diperlukan untuk transaksi tersebut — semakin khusus, semakin tepat diinternalkan), *uncertainty* (semakin tinggi ketidakpastian, semakin mahal kontrak eksternal yang lengkap), dan *frequency* (semakin sering transaksi, semakin masuk akal investasi pada hubungan internal). TCE menjelaskan mengapa Pertamina menginternalkan kilang (asset specificity tinggi, frekuensi tinggi) tetapi mengalihdayakan jasa pengeboran tertentu (asset specificity sedang, kontrak dapat diatur). **TCE bukan resep kaku melainkan kerangka untuk berpikir disiplin tentang apa yang harus dimiliki dan apa yang dapat dipinjam.**

---

## 6. *Blue Ocean Strategy*

### *Value Innovation* vs. *Competitive Advantage*

*Blue Ocean Strategy* yang dikembangkan Kim dan Mauborgne (2005) menempatkan dirinya sebagai *counter-paradigm* terhadap pemikiran kompetitif Porter. Bila Porter mengasumsikan bahwa keunggulan diperoleh dengan memilih posisi dalam *trade-off* yang sudah ada (cost vs. differentiation, broad vs. focused), Kim dan Mauborgne mengusulkan ***value innovation*** sebagai strategi memecah *trade-off* itu sendiri. Inti argumennya: di pasar yang sudah jenuh (*red ocean*), perusahaan saling memperebutkan demand yang ada dan margin tergerus. Strategi yang lebih baik adalah menciptakan ruang pasar baru (*blue ocean*) di mana persaingan belum terbentuk, dengan menawarkan kombinasi nilai yang sebelumnya tidak dianggap mungkin.

### *Eliminate-Reduce-Raise-Create Grid*

![*Gambar 6.4 — Concepts & Connections 6.1: Etsy's Blue Ocean Strategy*]({etsy})

*Sumber: Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6, p.114*

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

---

## 10. Poin-Poin Kunci — TPGS Ch.6

*Ringkasan resmi dari Gamble, Thompson & Peteraf (2021), Essentials of Strategic Management, Ch.6*

### LO6-1 — Strategi Ofensif dan Defensif

- **Serangan kompetitif** paling efektif menargetkan kelemahan pesaing, bukan kekuatan mereka
- Pilihan basis serangan: keunggulan biaya, segmen yang kurang terlayani, celah kualitas/fitur, inovasi, kesenjangan merek, atau celah distribusi
- **Strategi defensif** bertujuan menurunkan risiko serangan, melemahkan dampaknya, atau mendorong penantang menyerang pesaing lain — bukan menghilangkan serangan sepenuhnya
- *Signaling* yang kredibel dapat mencegah serangan sebelum dimulai

### LO6-2 — Timing Strategis

- Keunggulan *first-mover* paling kuat ketika: kurva belajar curam, *network effects* signifikan, *switching costs* tinggi, dan loyalitas merek terbentuk awal
- *Late-mover* menguntungkan ketika: teknologi masih berevolusi, biaya perintisan tinggi, dan pasar belum matang
- Tidak ada jawaban universal — konteks industri dan sumber daya perusahaan menentukan pilihan optimal

### LO6-3 — Cakupan Operasi

- **M&A horizontal** memperkuat posisi pasar tetapi sering gagal karena estimasi sinergi berlebihan dan kesulitan integrasi budaya
- **Integrasi vertikal** memberikan kendali rantai nilai tetapi meningkatkan risiko modal dan mengurangi fleksibilitas
- ***Outsourcing*** meningkatkan fokus pada kompetensi inti tetapi mengandung risiko *hollowing out* kapabilitas esensial
- **Aliansi dan JV** cocok untuk akses cepat ke teknologi atau pasar baru — tetapi tidak boleh menggantikan pembangunan kapabilitas internal

### LO6-4 — Aliansi dan Kemitraan

- Aliansi paling efektif untuk akses cepat ke teknologi, pasar, atau kapabilitas yang akan mahal dan lama jika dibangun sendiri
- Aliansi gagal karena tujuan yang berubah, ketidakpercayaan, *free-riding*, dan kesulitan koordinasi lintas budaya
- Bahaya terbesar: bergantung pada aliansi untuk kapabilitas yang seharusnya dibangun secara internal (*hollowing out*)

### LO6-5 — Sintesis Manajerial

- Tidak ada formula tunggal untuk memperkuat posisi kompetitif — pilihan ofensif/defensif/timing/*scope* harus disesuaikan dengan situasi industri, posisi relatif, dan sumber daya perusahaan
- Pilihan *strategic moves* yang tepat masih gagal tanpa sistem pengukuran kinerja yang selaras
- **Strategi bukan pilihan statis** — harus dikalibrasi terus seiring perubahan lingkungan kompetitif
"""


# ════════════════════════════════════════════════════════════════════════════
# PHASE 3 — PIPELINE
# ════════════════════════════════════════════════════════════════════════════
def pandoc(md: Path, out: Path) -> None:
    """Run pandoc to convert Markdown to DOCX using reference style."""
    result = subprocess.run(
        [PANDOC, str(md), f"--reference-doc={REFERENCE}", "-o", str(out)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    print(f"Generated: {out.name}")


if __name__ == "__main__":
    TEMP.mkdir(parents=True, exist_ok=True)
    OUT_RMK.mkdir(parents=True, exist_ok=True)
    if not REFERENCE.exists():
        raise FileNotFoundError(f"reference.docx not found at {REFERENCE}")
    if not EBOOK.exists():
        raise FileNotFoundError(f"TPGS ebook not found at {EBOOK}")

    print("Extracting figures from TPGS Ch.6...")
    results = extract_figures(str(EBOOK), FIGURES_DIR)
    print("Validating figures...")
    validate_figures(results)

    print("Building enhanced RMK content...")
    content = build_rmk_content(FIGURES_DIR)

    md_path = TEMP / "rmk_w6_enhanced.md"
    md_path.write_text(content, encoding="utf-8")
    print(f"Markdown written: {md_path.name} ({md_path.stat().st_size:,} bytes)")

    out_path = OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 6.docx"
    pandoc(md_path, out_path)
    print(f"Enhanced RMK size: {out_path.stat().st_size:,} bytes")
    print("Done.")
