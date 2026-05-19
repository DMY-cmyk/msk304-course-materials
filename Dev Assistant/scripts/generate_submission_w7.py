"""Generate RMK Pertemuan 7 (Corporate Strategy: Diversification, Essentials
Ch.8, with embedded TPGS Ch.8 figures) plus Critical Review Artikel 11 and
Artikel 12.

Pipeline:
  1. Extract 4 figures (FIGURE 8.1-8.4) from TPGS Ch.8 via PyMuPDF.
  2. Build three Markdown content strings (RMK + CR11 + CR12).
  3. Run Pandoc per file with reference.docx -> DOCX outputs.

Source spec: docs/superpowers/specs/2026-05-19-rmk-cr-pertemuan7-design.md
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import fitz  # PyMuPDF

# ============================================================================
# PATHS
# ============================================================================
SCRIPT_DIR   = Path(__file__).parent
PROJECT_ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
EBOOK        = PROJECT_ROOT / "Ebook" / (
    "(Business professional collection) John E. Gamble_ Arthur A. Thompson_ "
    "Margaret Ann Peteraf - Essentials of Strategic Management _ "
    "The Quest for Competitive Advantage (2021).pdf"
)
OUT_RMK      = PROJECT_ROOT / "RMK"
OUT_CR       = PROJECT_ROOT / "Critical Thinking of the Article"
TEMP         = PROJECT_ROOT / "Dev Assistant" / "temp"
FIGURES_DIR  = TEMP / "ch8_figures"
REFERENCE    = SCRIPT_DIR / "reference.docx"
PANDOC       = r"C:\Program Files\Pandoc\pandoc.exe"


# ============================================================================
# PHASE 1 - FIGURE EXTRACTION
# ============================================================================
def extract_figures(ebook_path: Path, figures_dir: Path) -> dict:
    """Extract TPGS Ch.8 figures 8.1-8.4."""
    figures_dir.mkdir(parents=True, exist_ok=True)
    mat = fitz.Matrix(2, 2)
    results: dict[str, Path] = {}

    fig_specs = [
        # name, anchor text, candidate page indices (confirmed in Task 1)
        ("figure_8_1", "FIGURE 8.1", [194]),
        ("figure_8_2", "FIGURE 8.2", [195]),
        ("figure_8_3", "FIGURE 8.3", [206]),
        ("figure_8_4", "FIGURE 8.4", [210]),
    ]

    with fitz.open(str(ebook_path)) as doc:
        for name, anchor, pg_indices in fig_specs:
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
    for key in ("figure_8_1", "figure_8_2", "figure_8_3", "figure_8_4"):
        path = results.get(key)
        if not path or not path.exists():
            raise FileNotFoundError(f"Missing figure: {key}")
        size = path.stat().st_size
        if size < 10_000:
            raise ValueError(f"{key} too small: {size} bytes")
        print(f"  OK {key}: {size:,} bytes")


# ============================================================================
# PHASE 2 - MARKDOWN BUILDERS (stubs; replaced in Tasks 3-5)
# ============================================================================
def build_rmk(figures: dict) -> str:
    def fp(name: str) -> str:
        return str(figures[name]).replace("\\", "/")

    fig1 = fp("figure_8_1")
    fig2 = fp("figure_8_2")
    fig3 = fp("figure_8_3")
    fig4 = fp("figure_8_4")

    return f"""# RINGKASAN MATERI KULIAH — PERTEMUAN 7

**Mata Kuliah:** MST304 — Manajemen Strategik Kontemporer

**Topik:** *Corporate Strategy: Diversification and the Multibusiness Company* (Essentials Ch.8)

**Mahasiswa:** Dzaki Muhammad Yusfian

**NIM:** 1125 01079

---

## 1. Pendahuluan

### Dari *Single-Business* ke *Multibusiness Decision*

Tiga pertemuan terakhir membangun argumen strategi pada level satu unit bisnis. Pertemuan 4 menetapkan *resource-based view* (Barney 1991; Peteraf 1993) sebagai kerangka diagnostik untuk mengenali sumber daya bernilai, langka, sulit ditiru, dan terorganisasi. Pertemuan 5 memetakan pilihan posisi generik (Porter 1985) yang menerjemahkan sumber daya tersebut menjadi *cost leadership*, *differentiation*, atau *focus*. Pertemuan 6 menambahkan dimensi taktis: gerakan ofensif dan defensif, *timing*, serta *scope of operations* yang menjaga posisi tetap kokoh ketika pesaing bergerak. Ketiga pertemuan tersebut berputar pada satu pertanyaan inti: bagaimana memenangkan kompetisi di dalam satu industri.

Pertemuan 7 mengubah pertanyaan itu secara fundamental. Topik *Corporate Strategy: Diversification and the Multibusiness Company* (Gamble, Peteraf & Thompson 2021, Ch.8) memindahkan analisis dari *business-level strategy* ke *corporate-level strategy* — keputusan tentang industri mana saja yang harus dimasuki dan bagaimana mengelola portofolio bisnis di bawah satu payung korporasi. Pertanyaannya bukan lagi "bagaimana memenangkan pasar X" melainkan "apakah masuk ke pasar X menambah nilai bagi pemegang saham di atas dan melebihi nilai bisnis berdiri sendiri."

### Mengapa Diversifikasi Menjadi Pertanyaan Strategik

**Kompleksitas strategik berubah secara *kualitatif*, bukan sekadar kuantitatif, ketika sebuah perusahaan menjadi *multibusiness*.** Pada level satu unit bisnis, manajemen menghadapi satu set Five-Forces, satu kelompok pelanggan inti, satu kurva pengalaman. Pada level korporat terdiversifikasi, manajemen menghadapi *portofolio* lingkungan kompetitif yang masing-masing memiliki dinamika berbeda, dengan kebutuhan informasi yang berlipat: setiap industri memiliki *key success factors*, profil pesaing, dan siklus kompetitif sendiri yang harus dimonitor secara paralel oleh *top management team* yang waktunya tetap terbatas. Tanggung jawab korporat juga meluas pada tiga arena yang absen di level *single-business*: alokasi modal antar-unit (siapa mendapat investasi, siapa diminta menyerahkan kas), koordinasi lintas-divisi untuk mengaktualisasi sinergi yang dijanjikan, dan arsitektur tata kelola yang menjaga unit-unit bisnis tetap efektif tanpa dibebani biaya *headquarter* yang berlebihan. Pertanyaan yang ditangani *board* pun bergeser fundamental — bukan lagi "bagaimana kita menang di pasar X" melainkan "industri mana yang layak ditambah, mana yang harus didivestasi, dan bagaimana kombinasi portofolio menambah nilai melebihi penjumlahan unit yang berdiri sendiri." Sumber keunggulan kompetitif pun berubah: pada level bisnis, keunggulan berasal dari *value chain* internal yang lebih efisien atau lebih bernilai; pada level korporat, keunggulan harus berasal dari *parenting advantage* — kemampuan korporasi induk menambah nilai pada unit bisnis yang lebih besar daripada bila unit tersebut berdiri sendiri.

### Pertanyaan Pengarah Pertemuan 7

Empat pertanyaan menjadi pengarah seluruh pembahasan. Pertama, *kapan* sebuah perusahaan harus mempertimbangkan diversifikasi. Kedua, *tes* apa yang harus dilewati oleh setiap kandidat industri target. Ketiga, *pendekatan* mana — akuisisi, *internal development*, atau *joint venture* — yang dipilih untuk masuk. Keempat, *jenis diversifikasi* mana — *related* yang membangun *cross-business strategic fit*, atau *unrelated* yang mengandalkan *capital allocation engine* — yang dipilih sebagai logika portofolio. **Porter (1987) memberikan jawaban klasik pada pertanyaan kedua melalui tiga tes diversifikasi: *industry attractiveness test* (apakah industri target secara struktural menghasilkan *return* di atas *cost of capital*), *cost of entry test* (apakah biaya masuk tidak menggerogoti potensi profit), dan *better-off test* (apakah kombinasi bisnis di bawah satu korporasi menambah nilai melebihi penjumlahan unit yang berdiri sendiri).** Ketiganya akan diuraikan pada §3 dan menjadi *gatekeeping criteria* untuk setiap proposal diversifikasi yang serius. Konsep payung yang menyatukan keempat pertanyaan ini adalah ***strategic fit*** — diuraikan secara sistematis pada §9 sebagai kerangka master pada tiga level yang berbeda namun saling melengkapi: *cross-business fit* antar-unit bisnis di portofolio terdiversifikasi (TPGS Ch.8), *internal business fit* antara strategi kompetitif dan sistem HR-reward di dalam satu unit (Artikel 11, Hsieh & Chen 2011), dan *multi-element organizational alignment* yang mengoperasionalisasi fit melalui 4Cs Medcof pada Artikel 12 (Okebaram & Onuoha 2018).

---

## 2. Kapan Diversifikasi Menjadi Pertimbangan Strategik

### Sinyal Saturasi Bisnis Inti

Diversifikasi jarang dipertimbangkan ketika bisnis inti masih tumbuh dengan margin yang sehat. Pertimbangan ini muncul justru ketika serangkaian sinyal saturasi mulai tampak: pertumbuhan permintaan industri yang melambat di bawah pertumbuhan ekonomi makro, intensitas rivalitas yang meningkat sehingga harga turun lebih cepat daripada biaya, dan dominasi pemimpin pasar yang sudah cukup kokoh sehingga peluang merebut pangsa dengan biaya yang masuk akal menjadi sempit. Pada kondisi seperti ini, *reinvesting* seluruh kas internal kembali ke bisnis inti menghasilkan *diminishing returns*; manajemen menghadapi pilihan antara mengembalikan kas kepada pemegang saham melalui dividen dan *buyback*, atau mencari arena baru yang memberi peluang pertumbuhan dan profitabilitas lebih tinggi.

### Surplus Sumber Daya dan Kapabilitas

Pemicu kedua adalah keberadaan *excess resources* yang dapat dipindahkan ke arena baru tanpa biaya marginal yang berlebihan. Kapabilitas distribusi yang telah dibangun untuk satu lini produk dapat di-*leverage* untuk lini produk lain yang menggunakan saluran yang sama. *Brand* yang telah dipercaya pelanggan dapat di-*extend* ke kategori berdekatan dengan biaya edukasi pasar yang jauh lebih rendah dibandingkan masuk dari nol. Astra International menggunakan kombinasi keduanya: jaringan distribusi yang telah dibangun untuk otomotif Toyota dan motor Honda di-*leverage* untuk masuk ke pasar alat berat (Komatsu) dan pertanian (kelapa sawit melalui Astra Agro Lestari), sementara kapabilitas finansial *captive* yang dikembangkan untuk pembiayaan otomotif diperluas ke perbankan dan asuransi melalui Astra Credit Companies dan Asuransi Astra Buana.

### Pertumbuhan *Shareholder Value* Mensyaratkan Ekspansi

Pemicu ketiga adalah tekanan dari pasar modal sendiri. Perusahaan yang sudah mencapai *market capitalization* substansial menghadapi ekspektasi pertumbuhan absolut yang tidak dapat dicapai oleh bisnis inti yang sudah dewasa. Bila pasar saham memberi *multiple* tinggi yang mengasumsikan pertumbuhan dua digit, sementara bisnis inti hanya tumbuh seiring inflasi, maka tekanan untuk mencari arena pertumbuhan baru menjadi struktural. Sinar Mas Group memberi ilustrasi: dari basis pulp dan kertas APP, grup ini berekspansi ke properti (Sinar Mas Land), finansial (Bank Sinarmas, Sinarmas MSIG Life), dan agribisnis (Sinar Mas Agro Resources and Technology) — setiap arena baru memberi ruang pertumbuhan yang tidak mungkin dicapai bila grup tetap berpegang pada pulp dan kertas.

### Risiko Diversifikasi Prematur

**Empat pemicu di atas adalah *kondisi yang membuat diversifikasi layak dipertimbangkan*, bukan justifikasi otomatis untuk melaksanakannya.** Diversifikasi prematur — yang dilakukan sebelum bisnis inti benar-benar matang atau sebelum kapabilitas yang ditransfer benar-benar relevan untuk arena baru — adalah sumber kegagalan yang konsisten dalam sejarah korporat. Konsekuensinya tidak hanya kerugian finansial pada akuisisi yang gagal; lebih halus dan lebih merusak adalah teralihkannya perhatian manajemen senior dari bisnis inti yang masih memerlukan pendalaman. Diversifikasi bukan pertumbuhan dengan biaya berapa pun; ia adalah keputusan strategik yang harus dijustifikasi oleh tes-tes konkret yang akan dibahas pada §3.

---

## 3. Membangun *Shareholder Value*: Tiga Tes Diversifikasi

### Tes 1 — *Industry Attractiveness Test*

Tes pertama (Porter 1987) menanyakan apakah industri target secara struktural menyediakan *return on investment* di atas *cost of capital* secara berkelanjutan. Penilaiannya tidak dapat dilakukan dengan melihat profitabilitas historis pemain *incumbent* karena pemain *incumbent* sering memiliki keunggulan posisi yang belum tentu dapat direplikasi oleh pendatang baru. Analisis yang lebih kuat adalah dengan menerapkan Five-Forces (Porter 1980) pada industri target: kekuatan tawar pembeli, kekuatan tawar pemasok, ancaman masuk, ancaman substitusi, dan intensitas rivalitas. Industri yang lulus tes ini menunjukkan struktur kompetitif yang menahan margin pada level di atas *cost of capital* bagi pemain rata-rata, bukan hanya bagi pemimpin pasar yang mungkin terisolasi oleh *barriers to entry* yang tidak dapat diakses pendatang baru.

### Tes 2 — *Cost of Entry Test*

Tes kedua mengukur apakah biaya masuk ke industri target akan menggerogoti seluruh potensi profit masa depan. **Logika ekonomisnya tajam: jika seluruh ekspektasi profit yang dapat dihasilkan dari kepemilikan bisnis target sudah ter-*price-in* dalam harga akuisisi atau biaya investasi pembangunan kapasitas, maka diversifikasi tidak menciptakan nilai — ia hanya memindahkan nilai dari pemegang saham pengakuisisi ke pemegang saham target.** Premi kontrol yang umum berkisar 20–40% di atas harga pasar dalam akuisisi *publicly listed* menjadi penghalang kasar yang sering tidak disadari manajemen yang terburu-buru. Pertamina dalam ekspansi internasional ke ladang minyak Iran menghadapi kombinasi biaya entri yang tinggi (politik dan ekonomik) dan ketidakpastian eksekusi yang tidak proporsional dibandingkan ekspektasi profit — kasus yang sering dirujuk sebagai kegagalan tes cost of entry pada konteks BUMN.

### Tes 3 — *Better-Off Test*

Tes ketiga adalah yang paling dalam secara konseptual. Pertanyaannya: apakah kombinasi bisnis-bisnis di bawah satu korporasi menghasilkan kinerja gabungan yang lebih besar dibandingkan penjumlahan kinerja bila bisnis-bisnis itu berdiri sendiri? Inilah ekonomi *1 + 1 = 3* — sinergi yang harus konkret, bukan retoris. Sinergi dapat berasal dari *cross-business strategic fit* (pembahasan §6), *operational discipline transfer*, *capital allocation superiority*, atau *parenting advantage* yang berasal dari kapabilitas manajerial korporat induk. Bank Mandiri pasca-konsolidasi 1999–2005 menjadi contoh tes ketiga yang dilalui melalui rasionalisasi: penggabungan empat bank legacy (Bumi Daya, Dagang Negara, Ekspor Impor, Pembangunan Indonesia) menghasilkan efisiensi cabang, standardisasi sistem informasi, dan skala balance sheet yang memungkinkan akses pasar modal internasional pada *cost of funds* yang lebih rendah daripada yang dapat diperoleh oleh masing-masing bank legacy secara terpisah.

### Mengapa Lulus Ketiga Tes Sulit

**Porter (1987) dalam studi historisnya terhadap 33 perusahaan besar AS antara 1950 dan 1986 menemukan bahwa lebih dari setengah akuisisi besar yang mereka lakukan didivestasi dalam beberapa tahun setelah akuisisi.** Temuan ini bukan anekdot, melainkan pola sistematik yang menunjukkan bahwa sinergi yang dijanjikan dalam *acquisition prospectus* jarang terealisasi dalam praktik. Penyebabnya berlapis: ekspektasi yang dibangun oleh *investment banker* untuk memuluskan transaksi, premi kontrol yang dibayar terlalu tinggi karena auction dynamics, integrasi pasca-merger yang menghadapi resistensi budaya organisasional, dan kapabilitas manajerial yang ternyata tidak dapat ditransfer karena terikat pada konteks bisnis asal. Implikasinya praktis: setiap proposal diversifikasi yang serius harus diuji oleh ketiga tes Porter secara eksplisit, dengan analisis yang skeptik terhadap angka sinergi yang diajukan oleh proponennya.

---

## 4. Pendekatan Diversifikasi

### *Acquisition* — Trade-off Kecepatan vs. Harga

Akuisisi adalah pendekatan tercepat untuk memasuki industri baru. Perusahaan target sudah memiliki posisi pasar, kapabilitas operasional, jaringan distribusi, dan basis pelanggan yang dapat diintegrasikan ke dalam portofolio pengakuisisi tanpa harus dibangun dari nol. Kecepatan ini berharga ketika industri target memiliki *window of opportunity* yang sempit — pertumbuhan tinggi yang akan menarik banyak pendatang baru, regulasi yang dapat berubah, atau *first-mover advantage* yang dapat hilang. Namun trade-off-nya adalah harga: premi kontrol 20–40% di atas harga pasar publik, biaya integrasi yang sering melebihi proyeksi awal, dan risiko *cultural mismatch* yang dapat merusak nilai kapabilitas yang diakuisisi. Indofood mengakuisisi Bogasari untuk mengintegrasikan rantai pasok tepung terigu yang menjadi *input* utama bisnis mie instan, dan kemudian Indolakto untuk masuk ke segmen susu cair dengan *brand* yang sudah dikenal — keduanya akuisisi yang lulus tes *better-off* karena sinergi *value chain* yang konkret dan terukur.

### *Internal Development* — Trade-off Lebih Murah tapi Lambat

*Internal development* membangun bisnis baru dari nol menggunakan sumber daya internal perusahaan. Pendekatan ini secara nominal lebih murah karena tidak ada premi kontrol yang dibayar; perusahaan hanya mengeluarkan biaya pembangunan kapasitas, pengembangan produk, dan akuisisi pelanggan. Namun biaya tersembunyi sering substansial: waktu yang dibutuhkan untuk membangun *brand recognition*, kurva belajar yang harus dilalui sebelum operasi mencapai efisiensi pemain *incumbent*, dan risiko kegagalan eksekusi yang tinggi pada industri yang manajemen senior tidak miliki pengalaman mendalam. Internal development paling masuk akal ketika industri target masih dalam tahap pertumbuhan awal sehingga *first-mover* tidak terlalu dirugikan, ketika perusahaan memiliki kapabilitas yang sangat *transferable* dari bisnis inti, atau ketika tidak ada target akuisisi yang menarik pada harga yang masuk akal.

### *Joint Venture* — Sharing Risk and Capabilities

*Joint venture* berbagi risiko investasi dan akses kapabilitas mitra. Pendekatan ini paling cocok ketika industri target memerlukan kombinasi kapabilitas yang tidak dimiliki sepenuhnya oleh satu pihak, atau ketika risiko proyek terlalu besar untuk ditanggung sendiri. *JV* juga menjadi pendekatan default ketika regulasi mengharuskan partisipasi mitra lokal — sebagaimana berlaku pada banyak sektor hulu di Indonesia. Pertamina dan ENI bekerja sama pada blok-blok migas tertentu untuk berbagi modal eksplorasi yang besar dan risiko geologis yang signifikan, sementara masing-masing pihak menyumbangkan kapabilitas yang berbeda (akses regulasi domestik dari Pertamina, kapabilitas teknis eksplorasi dari ENI). Kelemahan *JV* adalah kompleksitas tata kelola dan potensi konflik kepentingan ketika strategi jangka panjang masing-masing pihak mulai berbeda.

### Kriteria Pemilihan Pendekatan

**Pilihan antara akuisisi, *internal development*, dan *joint venture* tidak dapat dilakukan dalam abstraksi — ia tergantung pada empat dimensi konkret yang harus dievaluasi secara bersama.** Pertama, urgensi waktu: bila *window of opportunity* sempit, akuisisi lebih masuk akal. Kedua, ketersediaan target akuisisi pada harga yang masuk akal: bila tidak ada target atau harga sudah *bid up* oleh pesaing, *internal development* atau *JV* menjadi alternatif. Ketiga, *gap* kapabilitas: bila perusahaan kekurangan kapabilitas kunci dan tidak ada cara cepat memperolehnya, *JV* dengan mitra yang memiliki kapabilitas tersebut sering optimal. Keempat, profil risiko: *internal development* menanggung risiko kegagalan teknologi dan pasar; akuisisi menanggung risiko integrasi dan premi yang dibayar; *JV* menanggung risiko *partner alignment*. GoTo (Gojek + Tokopedia 2021) adalah ilustrasi modern pendekatan *merger-of-equals* yang menggabungkan kapabilitas transport, *commerce*, dan *payment* dalam satu platform — bukan akuisisi murni dan bukan *JV* murni, melainkan konsolidasi setara yang mencerminkan urgensi konsolidasi platform-business model Indonesia.

![*Gambar 1. Strategic Themes of Multibusiness Corporation (Related vs Unrelated Diversification)*]({fig1})

*Sumber: Gamble, Peteraf & Thompson (2021), Essentials of Strategic Management, Ch.8, hlm. 156*

Gambar 1 menunjukkan dua tema strategis utama yang dapat dipilih oleh perusahaan terdiversifikasi. Pilihan ini menjadi kerangka untuk seluruh pembahasan diversifikasi berikutnya — apakah membangun portofolio bisnis yang saling berbagi nilai-rantai (*related*) atau portofolio bisnis yang independen secara operasional (*unrelated*).

---

## 5. Pilihan Jalur: Diversifikasi *Related* vs. *Unrelated*

### *Related Diversification* — Logika *Cross-Business Strategic Fit*

*Related diversification* didefinisikan oleh keberadaan kesamaan substantif di antara aktivitas-rantai-nilai bisnis-bisnis dalam portofolio. Kesamaan tersebut dapat berasal dari teknologi yang berbagi *core know-how*, rantai pasok yang berbagi pemasok atau infrastruktur logistik, kapabilitas pemasaran dan distribusi yang melayani basis pelanggan yang sama, atau *brand* yang dapat di-*leverage* lintas kategori produk. **Klaim ekonomik dari *related diversification* adalah bahwa kesamaan ini menciptakan *economies of scope* — penurunan biaya per unit atau peningkatan diferensiasi yang berasal dari *sharing* aktivitas atau sumber daya lintas bisnis (Panzar & Willig 1981; Teece 1980).** Logika ini berbeda dari *economies of scale* yang berasal dari volume dalam satu lini produk; *economies of scope* berasal dari pemanfaatan satu sumber daya untuk beberapa lini produk yang berbeda.

### *Unrelated Diversification* — Logika *Portfolio Risk Management*

*Unrelated diversification* memilih jalur yang sebaliknya: bisnis-bisnis dalam portofolio tidak memiliki kesamaan *value-chain* yang substansial. Nilai yang diciptakan tidak berasal dari *economies of scope*, melainkan dari *capital allocation* yang superior, *operational discipline* yang dapat ditransfer secara generik, dan *financial engineering* yang memanfaatkan akses pasar modal yang lebih murah pada level korporat dibandingkan pada level bisnis terpisah. Berkshire Hathaway menjadi arketipe model ini: portofolio bisnisnya mencakup asuransi, kereta api, energi, makanan, ritel — tidak ada *value-chain* yang dapat di-*leverage* lintas bisnis, namun nilai yang konsisten diciptakan oleh disiplin *capital allocation* yang dipraktikkan Warren Buffett selama beberapa dekade. *Unrelated diversification* juga sering dijustifikasi oleh argumen *risk diversification* — dengan portofolio bisnis di industri yang siklusnya tidak sinkron, volatilitas *earnings* korporat secara agregat menjadi lebih rendah.

### Bukti Empiris: Mana yang Lebih Berkinerja

Bukti empiris dari literatur strategi memberi jawaban yang condong tetapi tidak absolut. **Rumelt (1974, 1982) dalam studi seminal terhadap *Fortune 500* menunjukkan bahwa perusahaan dengan strategi *related-constrained diversification* secara rata-rata memiliki *ROA* dan *shareholder return* yang superior dibandingkan perusahaan *unrelated*.** Markides & Williamson (1994) memperkuat temuan ini dengan menunjukkan bahwa keunggulan *related* berasal terutama dari transfer kapabilitas — bukan dari sekadar berbagi aktivitas fisik — dan paling signifikan pada perusahaan yang aktif mengeksploitasi *strategic asset* yang dapat ditransfer. Namun *kondisional* ini penting: keunggulan *related* terealisasi hanya ketika manajemen secara aktif mengeksploitasi fit melalui koordinasi lintas-divisi yang efektif. Bila koordinasi tidak terjadi, *related diversification* hanya mewarisi biaya kompleksitas tanpa manfaat sinergi.

### *Indonesian Examples*

Konteks Indonesia menyediakan ilustrasi kedua jalur. Astra International adalah contoh *related diversification* yang sukses: bisnis-bisnisnya — otomotif (Toyota Astra Motor, Astra Honda Motor), alat berat (United Tractors), agribisnis (Astra Agro Lestari), dan finansial (Astra Credit Companies, Asuransi Astra Buana) — terhubung melalui *value-chain matchups* di distribusi, *captive financing*, dan *brand* Astra yang menjadi *trust anchor* lintas kategori. Sinar Mas Group dan Salim Group lebih dekat ke *unrelated diversification*: portofolio bisnis melintasi pulp & paper, properti, finansial, agribisnis, dan makanan, tanpa *value-chain* yang konsisten dapat di-*leverage* — nilai yang diciptakan lebih banyak berasal dari *capital allocation* dan akses pasar modal yang dimiliki induk. GoTo menjadi contoh hibrida modern: *related platform fit* antara transport (Gojek), *commerce* (Tokopedia), dan *payment* (GoPay) memungkinkan *cross-platform* data dan *user funnel* yang menjadi sumber sinergi yang spesifik untuk model bisnis platform.

---

## 6. Diversifikasi ke Bisnis *Related*: *Strategic Fit* dan *Economies of Scope*

### Definisi *Strategic Fit* di Level Korporat

*Strategic fit* pada level korporat didefinisikan sebagai kondisi di mana aktivitas-rantai-nilai dari bisnis-bisnis yang berbeda memiliki cukup kesamaan untuk memungkinkan transfer sumber daya, *sharing* aktivitas, atau *cross-leverage* kapabilitas dengan biaya marginal yang rendah. Definisi ini perlu dibaca dengan presisi: fit tidak berarti bisnis-bisnis terlihat mirip pada level produk akhir; fit berarti bahwa pada satu atau beberapa tahap *value chain* — yang dirumuskan Porter (1985) sebagai rangkaian aktivitas primer (logistik masuk, operasi, logistik keluar, pemasaran, layanan) dan aktivitas pendukung (infrastruktur, HR, teknologi, pengadaan) — bisnis-bisnis tersebut menggunakan aktivitas, sumber daya, atau kapabilitas yang serupa sehingga ada peluang ekonomik untuk berbagi atau memindahkan. **Distinksi konseptual yang sering dilewatkan: fit-sebagai-*operational-overlap* (dua bisnis menggunakan pabrik atau gudang fisik yang sama) berbeda secara fundamental dari fit-sebagai-*strategic-resource-transfer* (kapabilitas R&D, *brand equity*, atau *organizational know-how* dari satu bisnis dapat dimanfaatkan oleh bisnis lain).** Bentuk kedua sering lebih bernilai karena melibatkan *intangible assets* yang sulit ditiru pesaing. Fit pada level korporat juga berbeda dari fit pada *single-business*: pada bisnis tunggal, fit yang dibahas adalah *internal alignment* antara strategi, struktur, dan sistem dalam satu unit; pada level korporat, fit melintasi unit-unit yang otonom. Toyota Astra Motor dan Astra Honda Motor memproduksi produk akhir yang berbeda (mobil vs. sepeda motor), namun keduanya berbagi *distribution backbone* Astra, *captive financing* dari Astra Credit Companies, dan *brand trust* Astra di mata konsumen Indonesia — itulah fit yang substantif.

### Empat Tipe *Cross-Business Value-Chain Fit*

TPGS Ch.8 mengidentifikasi empat tipe *value-chain fit* yang menjadi sumber *economies of scope*. **Pertama, *supply chain fit*** — bisnis-bisnis berbagi pemasok yang sama, infrastruktur logistik yang sama, atau *input* yang sama sehingga dapat mengkonsolidasi pembelian dan menurunkan biaya per unit melalui skala pembelian agregat; Indofood mengintegrasikan Bogasari sebagai pemasok terigu *captive* untuk lini mie instan, kecap, dan makanan ringan sehingga seluruh portofolio mendapat *input* dengan harga internal yang stabil. **Kedua, *R&D dan teknologi fit*** — bisnis-bisnis berbagi platform teknologi inti sehingga investasi R&D dapat di-amortisasi pada beberapa lini produk dan inovasi pada satu bisnis dapat di-*spillover* ke bisnis lain; Honda mengaplikasikan kapabilitas *small-engine engineering* yang sama untuk mobil, sepeda motor, generator, dan mesin pertanian. **Ketiga, *manufacturing fit*** — bisnis-bisnis berbagi proses produksi, fasilitas, atau kapabilitas kualitas, sehingga *learning curve* dan *capacity utilization* dapat dimaksimalkan; Toyota Production System dan disiplin *lean manufacturing* yang dikembangkan untuk lini mobil ditransfer ke lini *forklift* Toyota Industries tanpa membangun kapabilitas baru dari nol. **Keempat, *sales/marketing/distribusi/brand fit*** — bisnis-bisnis berbagi saluran distribusi, *brand equity*, atau basis pelanggan sehingga biaya akuisisi pelanggan dan biaya pemasaran dapat di-*spread* lintas beberapa lini produk; Unilever Indonesia menggunakan jaringan distribusi tunggal yang menjangkau 800 ribu *outlet* untuk membawa produk personal care, *home care*, dan *food & beverage* secara bersama, sehingga biaya logistik per SKU lebih rendah daripada bila masing-masing kategori membangun jaringan terpisah.

### *Economies of Scope* vs. *Economies of Scale*

Perbedaan antara *economies of scope* dan *economies of scale* sering dicampur, padahal mekanismenya berbeda dan implikasi strategiknya berbeda pula. **Mekanisme *economies of scale*: biaya per unit menurun ketika volume satu lini produk meningkat** — biaya tetap (pabrik, lini produksi, R&D dasar) di-*spread* pada output yang lebih besar, *learning curve* mendorong efisiensi, dan kekuatan tawar terhadap pemasok meningkat dengan volume. Contoh konkret: pabrik semen Tonasa yang memproduksi 4 juta ton per tahun memiliki biaya tetap per ton substansial lebih rendah daripada pabrik yang memproduksi 1 juta ton — biaya kapital, biaya energi tetap, dan biaya overhead pabrik di-*amortise* pada volume yang lebih besar. **Mekanisme *economies of scope*: biaya per unit menurun ketika satu sumber daya digunakan bersama oleh beberapa lini produk yang berbeda.** Panzar & Willig (1981) dalam kerangka *production economics* memformalkan kondisi ini sebagai *subadditivity* dari fungsi biaya. Contoh konkret: jaringan distribusi Unilever yang awalnya dibangun untuk sabun digunakan bersama oleh sampo, pasta gigi, es krim, dan kecap — biaya distribusi per kategori jauh lebih rendah dibandingkan bila masing-masing membangun jaringan dari nol. Teece (1980) memperluas argumen ini dengan menunjukkan bahwa *intangible assets* — kapabilitas R&D, *brand*, *organizational know-how* — sering memiliki karakteristik *public goods* dalam batas perusahaan: penggunaannya untuk satu lini produk tidak mengurangi ketersediaannya untuk lini produk lain, sehingga sumber *economies of scope* yang paling sulit ditiru pesaing berasal justru dari aset tak berwujud, bukan dari fasilitas fisik bersama.

### Bagaimana *Related Diversification* Menciptakan Keunggulan Kompetitif

**Keunggulan kompetitif yang berasal dari *related diversification* tidak otomatis — ia terealisasi hanya ketika manajemen secara aktif mengeksploitasi fit melalui koordinasi lintas-divisi yang efektif.** Banyak perusahaan terdiversifikasi memiliki potensi sinergi pada peta organisasi tetapi gagal mengeksploitasinya karena unit-unit bisnis dijalankan sebagai *silo* independen dengan *transfer pricing* yang menghambat *sharing*, *incentive system* yang menghargai kinerja unit individual lebih dari kinerja portofolio, dan struktur *headquarter* yang tidak memiliki kapabilitas mengarahkan koordinasi yang substansial. TPGS *Concepts & Connections 8.1* (hlm. 159) memberi ilustrasi merger Kraft–Heinz 2015 yang dirancang dengan asumsi fit dalam pengadaan, distribusi, dan *brand portfolio management* di kategori *consumer staples*. Kasus ini menunjukkan bahwa fit secara teori dapat menjadi sumber sinergi, tetapi eksekusi pasca-merger yang ditangani 3G Capital dengan disiplin biaya yang ekstrem juga menunjukkan bahwa fit perlu diaktualisasi melalui *operational discipline* yang konkret — bukan hanya melalui *deal logic*. Astra Group memberikan contoh aktualisasi yang sistematis di Indonesia: *cross-business fit* antara Toyota Astra Motor, Astra Honda Motor, Astra International (distribusi), dan Astra Credit Companies (*captive financing*) dieksploitasi melalui Astra Management System yang membangun standar manajerial, mobilitas talenta lintas-divisi, dan *capital allocation* sentral yang menjadi *parenting advantage* riil. BCA dan Djarum Group menunjukkan bentuk berbeda: *brand trust* lintas-bisnis dan akses pelanggan korporat yang sama menjadi *relationship asset* yang lintas-leverage; sementara GoTo mengeksploitasi fit *cross-platform* dengan mendorong *cross-selling* dari GoFood merchant ke Tokopedia *seller* dan dari Gojek *user* ke GoPay *wallet*.

![*Gambar 2. Cross-Business Value-Chain Strategic Fit*]({fig2})

*Sumber: Gamble, Peteraf & Thompson (2021), Essentials of Strategic Management, Ch.8, hlm. 157*

Gambar 2 adalah visualisasi paling penting dari konsep *strategic fit* di level korporat — peta yang menunjukkan di mana *value-chain matchups* antar-bisnis dapat menjadi sumber *economies of scope*. Inilah jembatan analitis yang akan dirujuk kembali pada §9 untuk menghubungkan Ch.8 dengan Artikel 11 (*internal fit*) dan Artikel 12 (*multi-element organizational fit*).

---

## 7. Diversifikasi ke Bisnis *Unrelated*: Logika *Conglomerate*

### Mengapa Perusahaan Memilih *Unrelated Diversification*

*Unrelated diversification* dipilih bukan karena manajemen tidak memahami logika fit, melainkan karena ada kondisi yang membuat jalur ini menjadi pilihan yang masuk akal. Motivasi yang paling sering muncul adalah *portfolio risk diversification* — kepemilikan bisnis di industri yang siklusnya tidak sinkron menurunkan volatilitas *earnings* korporat secara agregat. Motivasi kedua adalah *opportunistic acquisition* — kesempatan membeli aset berkualitas pada harga *distressed* yang muncul di industri yang sama sekali berbeda dari bisnis inti tetapi terlalu menarik untuk dilewatkan. Motivasi ketiga adalah *capital allocation engine* — perusahaan dengan kapabilitas manajerial yang dapat mengevaluasi peluang investasi dengan disiplin yang lebih tinggi daripada pasar modal eksternal dapat menciptakan nilai dengan mengalokasikan kas internal lintas bisnis yang tidak terkait. Motivasi keempat adalah *cyclicality smoothing* untuk perusahaan yang bisnis intinya sangat siklikal sehingga akses pasar modal pada titik bawah siklus menjadi mahal.

### Bagaimana *Unrelated Diversification* Menciptakan Nilai

**Pada jalur *unrelated*, sumber nilai harus berasal dari *parenting advantage* yang murni manajerial — bukan dari *value-chain fit* yang konkret.** Berkshire Hathaway memberikan model paling jelas: nilai diciptakan melalui *superior capital allocation* yang dipraktikkan Warren Buffett dan Charlie Munger selama lima dekade, dengan disiplin *valuation* yang menolak pembayaran premi berlebih, *operational autonomy* yang dipertahankan untuk manajemen unit bisnis akuisisi, dan akses *cost of funds* yang lebih rendah karena akses ke *float* asuransi yang dapat di-*deploy* sebagai kapital investasi. Mekanisme lain adalah *operational discipline transfer* — kapabilitas manajerial generik (sistem kontrol biaya, *talent development*, *risk management*) yang dapat diaplikasikan secara konsisten lintas industri tanpa memerlukan kesamaan *value chain*. *Financial engineering* — strukturisasi modal, *hedging*, dan optimasi pajak pada level korporat — adalah sumber nilai ketiga yang dapat dieksploitasi oleh konglomerat dengan akses pasar modal yang lebih luas dibandingkan unit bisnis individual.

### Tiga Jebakan *Unrelated Diversification*

Tiga jebakan secara konsisten menjerat konglomerat yang tidak hati-hati. **Pertama, *demanding managerial requirements*** — *top management* harus menguasai dinamika banyak industri yang sangat berbeda, dan kapabilitas menguasai semuanya secara mendalam adalah langka. Akibatnya, sebagian besar konglomerat terpaksa mendelegasikan keputusan strategik ke unit bisnis tanpa kemampuan korporat melakukan *quality control* yang substantif. **Kedua, *limited competitive advantage potential*** — tanpa *value-chain fit*, satu-satunya sumber keunggulan adalah *parenting advantage*, dan *parenting advantage* yang murni manajerial sulit dipertahankan dalam jangka panjang karena dapat ditiru atau dilampaui oleh konglomerat lain yang memperbaiki kapabilitas manajerialnya. **Ketiga, *risk reduction* yang sering ilusi** — pemegang saham dapat melakukan diversifikasi sendiri lebih efisien melalui pasar modal dengan membeli saham beberapa perusahaan terpisah; diversifikasi pada level korporat justru menambah biaya kompleksitas tanpa menambah manfaat diversifikasi risiko yang tidak dapat diperoleh pemegang saham secara mandiri.

### *Misguided Reasons*

**TPGS Ch.8 secara eksplisit mengidentifikasi *misguided reasons* yang sering mendorong diversifikasi tetapi merusak nilai pemegang saham.** Ego manajemen senior yang ingin membangun "kerajaan" yang lebih besar dari perusahaan tunggal yang sudah mereka jalankan. Kompensasi yang dikaitkan dengan ukuran perusahaan (revenue, total assets) bukan dengan *return on invested capital*, sehingga manajemen memiliki insentif perbesar perusahaan walaupun marjinal *return* atas akuisisi tambahan negatif. *Defensive empire-building* yang dilakukan untuk membuat perusahaan terlalu besar atau terlalu kompleks untuk diakuisisi sehingga manajemen petahana mempertahankan posisinya. Indonesia menyediakan ilustrasi paska-krisis 1998: Salim Group yang dipaksa melakukan *deleveraging* substansial setelah ekspansi *unrelated* yang agresif menghasilkan struktur utang yang tidak dapat dipertahankan ketika rupiah melemah dan suku bunga melonjak. Bakrie Group menghadapi tekanan *re-focus* yang mirip pada dekade berikutnya — kasus konsisten dengan jebakan *over-diversification* yang dibahas dalam TPGS Ch.8.

---

## 8. Mengevaluasi Strategi Perusahaan Terdiversifikasi: Kerangka 6-Langkah

### Langkah 1: *Industry Attractiveness Assessment*

Langkah pertama adalah menilai daya tarik struktural setiap industri di mana perusahaan terdiversifikasi memiliki kehadiran. Penilaian dilakukan dengan menggabungkan beberapa dimensi: kekuatan kompetitif Porter Five-Forces (intensitas rivalitas, kekuatan tawar pembeli dan pemasok, ancaman masuk, ancaman substitusi), pertumbuhan pasar yang diharapkan, volatilitas profitabilitas historis, dan kemampuan industri menyediakan *return* di atas *cost of capital* secara berkelanjutan. Tujuan penilaian ini adalah memberi peringkat industri-industri dalam portofolio sehingga manajemen korporat memiliki dasar objektif untuk mengalokasikan sumber daya secara diferensial. Industri yang menunjukkan struktur kompetitif yang terkikis atau pertumbuhan yang stagnan menjadi kandidat untuk divestasi atau *harvest*; industri dengan daya tarik tinggi menjadi prioritas untuk investasi tambahan.

### Langkah 2: *Business-Unit Competitive Strength*

Langkah kedua menilai posisi kompetitif setiap unit bisnis di dalam industrinya. Dimensi penilaian mencakup pangsa pasar relatif, posisi biaya relatif terhadap pesaing, kekuatan *brand* dan basis pelanggan, *capability fit* terhadap *key success factors* industri, dan kemampuan unit menghasilkan *cash flow* yang menutupi kebutuhan investasinya sendiri. Penilaian ini memberi peringkat unit-unit bisnis dari yang paling kuat (kandidat untuk investasi *grow and build*) hingga yang paling lemah (kandidat untuk divestasi). Penggabungan Langkah 1 dan Langkah 2 menghasilkan matriks dua dimensi — *industry attractiveness* di satu sumbu, *competitive strength* di sumbu lain — yang menjadi alat analitis paling penting untuk evaluasi portofolio.

![*Gambar 3. Nine-Cell Industry Attractiveness–Competitive Strength Matrix*]({fig3})

*Sumber: Gamble, Peteraf & Thompson (2021), Essentials of Strategic Management, Ch.8, hlm. 168*

Gambar 3 adalah alat analitis pokok yang digunakan untuk memetakan unit-unit bisnis di dalam portofolio terdiversifikasi. Setiap bisnis ditempatkan sebagai *bubble* berdasarkan *industry attractiveness* (sumbu vertikal) dan *competitive strength* (sumbu horizontal). Ukuran *bubble* merepresentasikan *revenue*, sedangkan posisi diagonal menentukan rekomendasi alokasi sumber daya — *grow and build* pada diagonal kanan-atas, *defend and maintain* di tengah, kandidat divestasi di kiri-bawah.

### Langkah 3: *Strategic Fit Across Businesses*

Langkah ketiga mengidentifikasi *value-chain matchups* antar-unit-bisnis yang dapat menjadi sumber sinergi konkret. Pertanyaan analitis: di tahap *value chain* mana — pengadaan, R&D, manufaktur, distribusi, pemasaran, layanan pasca-jual — bisnis-bisnis dalam portofolio memiliki kesamaan yang dapat menjadi *resource transfer*, *activity sharing*, atau *cross-leverage* kapabilitas? Penilaian fit harus konkret, bukan retoris: setiap klaim sinergi harus didukung oleh mekanisme spesifik dan estimasi penghematan biaya atau peningkatan *revenue* yang dapat diukur. Tanpa fit yang konkret pada Langkah 3, *related diversification strategy* tidak terjustifikasi — perusahaan sebaiknya beralih ke logika *unrelated* dengan ekspektasi nilai yang berbeda.

### Langkah 4: *Resource Fit*

Langkah keempat menanyakan apakah portofolio yang ada menuntut sumber daya yang lebih besar — finansial dan manajerial — daripada yang dapat disediakan oleh perusahaan induk. *Financial resource fit* memeriksa apakah *cash flow* yang dihasilkan oleh unit-unit yang sudah matang cukup untuk mendanai kebutuhan investasi unit-unit yang sedang tumbuh, tanpa mengandalkan akses pasar modal eksternal yang mahal. *Managerial resource fit* memeriksa apakah *top management team* memiliki *bandwidth* dan kapabilitas untuk mengelola seluruh portofolio dengan kualitas yang konsisten — termasuk perhatian, ekspertise industri-spesifik, dan kemampuan koordinasi lintas-divisi. Portofolio yang gagal pada *resource fit* harus dirasionalisasi melalui divestasi unit-unit yang tidak fit dengan kapabilitas korporat induk.

### Langkah 5: *Ranking* dan *Resource Allocation*

Langkah kelima menggabungkan output Langkah 1–4 menjadi *ranking* unit-unit bisnis berdasarkan kelayakan investasi dan prioritas strategik. Unit yang berada di kuadran *attractive industry + strong competitive position* mendapat klasifikasi *grow and build* — investasi tambahan untuk memperkuat posisi. Unit di kuadran *moderate attractiveness + medium strength* mendapat *defend and maintain* — investasi sekadar untuk mempertahankan posisi. Unit di kuadran *unattractive industry + weak position* menjadi kandidat divestasi atau *harvest* — *cash flow* yang dihasilkan dialihkan ke unit-unit dengan prospek lebih baik. Disiplin *ranking* ini adalah inti *parenting advantage*: korporasi induk menciptakan nilai dengan mengalokasikan sumber daya lebih disiplin daripada yang dapat dilakukan pasar modal eksternal.

### Langkah 6: *Crafting New Strategic Moves*

Langkah keenam menerjemahkan analisis ke dalam keputusan-keputusan strategik konkret untuk masa depan. Pilihan strategik utama meliputi: investasi tambahan untuk memperkuat unit yang ada, akuisisi baru untuk menambah unit yang melengkapi portofolio, *internal start-up* untuk membangun unit baru di industri yang menjanjikan, atau divestasi unit-unit yang tidak lulus *resource fit* atau *strategic fit*. Pilihan finansial pada level korporat juga harus dievaluasi: apakah kelebihan kas dialokasikan ke dividen, *buyback*, atau *paydown* utang. Keputusan ini bersifat *trade-off* eksplisit antara *re-investing in businesses* dan *returning cash to shareholders* — pertanyaan klasik *corporate finance* yang pada perusahaan terdiversifikasi menjadi keputusan strategik di level *board*.

![*Gambar 4. Strategic & Financial Options for Allocating Diversified Company Resources*]({fig4})

*Sumber: Gamble, Peteraf & Thompson (2021), Essentials of Strategic Management, Ch.8, hlm. 172*

Gambar 4 mengoperasionalkan Langkah 6: pilihan-pilihan strategis (*invest to strengthen*, akuisisi, *internal start-up*, *pay down debt*) dan pilihan finansial (dividen, *buyback*, *cash reserve*) yang dapat dipilih perusahaan terdiversifikasi. *Trade-off* antara keduanya — *re-investing in businesses* vs. *returning cash to shareholders* — adalah pertanyaan klasik *corporate finance* yang menjadi keputusan strategik di level *board*.

---

## 9. Sintesis: *Strategic Fit* sebagai Kerangka Master di Tiga Level

### Asal Kerangka *Fit* dan *Contingency Theory*

Konsep *strategic fit* berakar pada *contingency theory* yang dirumuskan Lawrence dan Lorsch (1967) dalam karya seminal *Organization and Environment*. Riset asli mereka membandingkan perusahaan-perusahaan dalam industri *high-tech* (plastik) yang menghadapi lingkungan turbulen — perubahan teknologi cepat, ketidakpastian permintaan tinggi — dengan perusahaan-perusahaan dalam industri kontainer yang menghadapi lingkungan stabil dengan teknologi matang dan permintaan dapat diprediksi. Dua konsep yang mereka rumuskan menjadi pijakan literatur fit berikutnya: ***differentiation*** sebagai derajat unit-unit fungsional dalam organisasi mengembangkan orientasi, struktur, dan *time horizon* yang berbeda untuk menangani sub-lingkungan masing-masing; dan ***integration*** sebagai mekanisme koordinasi (komite, liaison, *cross-functional teams*) yang menyatukan unit-unit yang ter-*differentiated* tersebut. **Temuan empirisnya: perusahaan berkinerja tinggi di industri plastik memiliki *differentiation* tinggi yang diimbangi *integration* yang juga tinggi; perusahaan berkinerja tinggi di industri kontainer memiliki *differentiation* rendah dengan integrasi yang lebih formal.** Argumen inti contingency theory yang lahir dari sini adalah *no one best way*: superioritas struktur dan strategi tergantung pada fit dengan kondisi lingkungan. Galbraith (1973), Mintzberg (1979), dan Donaldson (2001) memperluas kerangka ini, menjadikan contingency theory sebagai *paradigm* dominan di organization theory hingga *resource-based view* muncul sebagai komplemen pada 1990-an. Implikasi pedagogiknya: pertanyaan yang benar bukan "strategi apa yang terbaik" melainkan "strategi apa yang fit untuk kondisi ini."

### Tiga Level *Strategic Fit* dalam Pertemuan 7

Pertemuan 7 mengintegrasikan kerangka fit pada tiga level analisis yang saling melengkapi. **Level 1 — *cross-business fit* (TPGS Ch.8)** menanyakan fit antar-unit-bisnis di dalam perusahaan terdiversifikasi: di mana *value-chain matchups* dapat menjadi sumber *economies of scope*. Pembahasan §6 dan Gambar 2 memberi taksonomi konkret tipe-tipe fit ini. **Level 2 — *internal business fit* (Artikel 11, Hsieh & Chen 2011)** menanyakan fit di dalam satu unit bisnis antara strategi kompetitif, *human resource strategy*, dan *reward system*. Hsieh & Chen mengajukan tiga konfigurasi konkret: *differentiation* harus didukung *innovation-oriented HR* dan *human capital reward*; *cost leadership* didukung *contribution-oriented HR* dan *output reward*; *focus* didukung *commitment-oriented HR* dan *position reward*. **Level 3 — *organizational alignment fit* (Artikel 12, Okebaram & Onuoha 2018)** menanyakan fit multi-elemen antara *strategic fit* yang dioperasionalisasi melalui 4Cs Medcof (1997) — *Capability, Compatibility, Commitment, Control* — dan elemen-elemen desain organisasi seperti struktur, *employee relations*, dan *information exchange*. Ketiga level ini bukan substitusi melainkan komplemen: keputusan korporat pada Level 1 menentukan konteks; eksekusi pada Level 2 dan Level 3 menentukan apakah keputusan korporat menghasilkan kinerja yang dijanjikan.

### Venkatraman (1989) Enam Perspektif *Fit*

**Venkatraman (1989) dalam *The Concept of Fit in Strategy Research* memberikan kontribusi metodologis paling penting pada literatur fit dalam tiga dekade terakhir dengan mengidentifikasi enam perspektif fit yang masing-masing memiliki implikasi pengukuran berbeda.** *Fit as moderation* — variabel ketiga (fit) mengubah *slope* hubungan antara strategi dan kinerja; diuji melalui interaksi statistik. *Fit as mediation* — fit adalah variabel antara yang menghubungkan strategi dengan kinerja; strategi memengaruhi kinerja *melalui* fit, bukan langsung. *Fit as matching* — fit didefinisikan sebagai *theoretical correspondence* antara dua dimensi tanpa referensi langsung pada kriteria kinerja; pengukurannya berupa selisih atau jarak antar-dimensi. *Fit as gestalt* — fit adalah konfigurasi keseluruhan yang koheren secara internal; bukan dimensi individual yang penting melainkan pola lintas banyak dimensi yang membentuk *type* yang utuh. *Fit as profile-deviation* — fit diukur sebagai jarak deviasi dari profil ideal yang ditetapkan secara teoretis atau empiris (semakin dekat ke ideal, semakin tinggi fit). *Fit as covariation* — fit didefinisikan sebagai *internal consistency* dari pola lintas indikator yang dapat divalidasi melalui *factor analysis* atau *structural equation modeling*. Setiap perspektif menghasilkan strategi pengukuran dan asumsi statistik yang berbeda; klaim fit yang tidak mengkonkretkan perspektif yang dipakai sering kabur secara metodologis dan rentan terhadap kritik *operationalization ambiguity*.

### Miles & Snow (1978) Typology dan *Equifinality* (Doty et al. 1993)

Miles dan Snow (1978) menyediakan tipologi *configurational* yang menjadi rujukan pedagogis paling konsisten dalam literatur strategi. Empat tipe — *Defender*, *Prospector*, *Analyzer*, *Reactor* — masing-masing merupakan paket lengkap strategi, struktur, dan proses yang konsisten secara internal. *Defender* memilih segmen pasar yang stabil dan membangun efisiensi struktural; *Prospector* terus mencari peluang produk dan pasar baru dengan struktur yang fleksibel; *Analyzer* adalah hibrida yang menjaga inti *defender* sambil melakukan ekspansi terbatas; *Reactor* tidak memiliki strategi yang konsisten dan secara empiris berkinerja paling buruk. Doty, Glick dan Huber (1993) memperluas tipologi ini dengan prinsip ***equifinality*** — beberapa konfigurasi yang berbeda dapat menghasilkan kinerja superior secara setara, asalkan masing-masing konfigurasi memiliki *internal consistency* yang tinggi. **Operasionalisasi prinsip ini: jalur *Defender* (segmen stabil + struktur efisien + sistem kontrol biaya yang ketat) dan jalur *Prospector* (eksplorasi pasar baru + struktur organik + sistem reward berbasis inovasi) dapat sama-sama menghasilkan *high performance*, walaupun pilihan elemen strategik dan organisasionalnya berlawanan secara substantif.** Yang menentukan bukan jalur mana yang dipilih, melainkan apakah elemen-elemen di sepanjang jalur tersebut konsisten satu sama lain — fit internal antara strategi, struktur, sistem HR, dan kontrol manajemen. Prinsip *equifinality* secara langsung mendasari argumentasi Okebaram & Onuoha (Artikel 12) bahwa beberapa konfigurasi 4Cs Medcof (*Capability*, *Compatibility*, *Commitment*, *Control*) yang dipasangkan dengan *organization design*, *employee relations*, dan *information exchange* yang berbeda dapat menghasilkan *organizational effectiveness* yang setara — argumen yang membebaskan praktisi dari pencarian "satu konfigurasi terbaik" yang sia-sia.

### Jembatan Eksplisit ke Artikel 11 dan 12

Hsieh dan Chen (Artikel 11) mengoperasionalisasi *internal fit* dengan presisi yang dapat langsung diterapkan di unit bisnis. Triad mereka — *business competitive strategy* × *HR strategy type* × *reward system type* — menyediakan kerangka diagnostik konkret: *differentiation* yang dipasangkan dengan *contribution-oriented HR* dan *output reward* akan menghasilkan *innovation paralysis* karena sistem reward menekan inisiatif inovasi jangka panjang; *cost leadership* yang dipasangkan dengan *innovation-oriented HR* dan *human capital reward* akan menghasilkan *cost discipline failure* karena talenta yang dikembangkan menuntut otonomi dan *reward variable* yang tidak konsisten dengan disiplin biaya. Artikel ini berbasis konseptual penuh (belum diuji empiris), sehingga proposisinya berdiri sebagai *agenda-setting framework* untuk riset selanjutnya. Okebaram dan Onuoha (Artikel 12) bekerja pada Level 3 dengan operasionalisasi *strategic fit* melalui 4Cs Medcof (1997) dan tiga jalur organisasional (organization design, *employee relations*, *information exchange*) yang diuji secara empiris pada N=212 responden dari empat perusahaan Nigerian (tiga operator telekomunikasi dan satu bank). Temuan empirisnya — ketiga jalur signifikan pada p<0,001 — memperkuat klaim fit pada level organisasional, walaupun konsep akhir yang dicapai sesungguhnya adalah *sustained competitive advantage* (Porter 1985), bukan *sustainability* dalam pengertian *triple bottom line* (Elkington 1997) sebagaimana judul artikelnya dapat memberi kesan.

Nadler dan Tushman (1980) memberi definisi fit yang dipakai eksplisit oleh Okebaram & Onuoha: *"the degree to which the needs, demands, goals, objectives, and structures of one component match."* Definisi ini bersifat multi-element dan multi-direksional — fit bukan kondisi pasif melainkan hasil proses *alignment* aktif antara komponen-komponen organisasi. Ketiga level fit yang dibahas Pertemuan 7 — *cross-business*, *intra-business*, dan *organizational alignment* — masing-masing adalah aplikasi konkret dari definisi Nadler & Tushman pada *scope of analysis* yang berbeda. **Sintesis paradigmatik Pertemuan 7 adalah bahwa setiap analisis di §2–§8 sesungguhnya pelaksanaan prinsip fit pada level yang berbeda: fit antara strategi diversifikasi dengan kondisi industri (Tes 1 Porter); fit antara biaya entri dengan kapabilitas yang dimiliki (Tes 2); fit antara bisnis baru dengan portofolio yang sudah ada (Tes 3); fit antar-unit-bisnis melalui *value-chain matchups* (§6); dan fit antara *resource demand* dan *resource supply* di level korporat (Langkah 4 evaluasi).** Strategic fit bukan sekadar konsep dalam Ch.8 — ia adalah kerangka master yang menyatukan keseluruhan logika strategi pada Pertemuan 7.

---

## 10. Kesimpulan

### *Fit* sebagai Proses Rekalibrasi Berkelanjutan di Setiap Level

Pemahaman *strategic fit* sebagai kondisi statis adalah kesalahan kategori. Fit pada level apa pun — *cross-business*, *internal business*, *organizational alignment* — adalah hasil proses kalibrasi berkelanjutan terhadap perubahan lingkungan eksternal, evolusi kapabilitas internal, dan pergeseran prioritas pemegang kepentingan. Zajac, Kraatz dan Bresser (2000) menamai dimensi temporal ini ***dynamic fit*** — pengakuan bahwa konfigurasi yang fit pada satu titik waktu dapat menjadi *misfit* pada titik waktu berikutnya bila salah satu elemen yang menjadi penopang fit berubah. Implikasinya bagi praktisi: evaluasi portofolio terdiversifikasi (Kerangka 6-Langkah §8) tidak dapat dilakukan sebagai latihan satu kali; ia harus menjadi ritual periodik yang menguji kembali asumsi fit pada setiap titik waktu yang relevan.

### Integrasi Pert. 4–7

Empat pertemuan terakhir membentuk arsitektur strategi yang konsisten secara internal. **Pertemuan 4** menyediakan kerangka diagnostik melalui *resource-based view*: identifikasi sumber daya VRIO. **Pertemuan 5** menerjemahkan sumber daya menjadi posisi generik Porter — *cost leadership*, *differentiation*, *focus*. **Pertemuan 6** menambahkan dimensi taktis untuk mempertahankan posisi tersebut: *strategic moves*, *timing*, *scope of operations*. **Pertemuan 7** memindahkan analisis dari level satu bisnis ke level korporat: keputusan diversifikasi, evaluasi portofolio, dan koordinasi lintas-bisnis. Konsep yang menjembatani keempat pertemuan adalah *fit* — fit antara sumber daya dan posisi generik (Pertemuan 4 ke 5), fit antara posisi generik dan taktik penguatan (Pertemuan 5 ke 6), fit antara strategi bisnis dan strategi korporat (Pertemuan 6 ke 7). Sintesis Pertemuan 7 melalui kerangka tiga level *strategic fit* — *cross-business*, *internal business*, *organizational alignment* — menjadi titik tertinggi pengintegrasian konseptual yang dapat dicapai dalam paruh pertama kurikulum.

### Antisipasi Pert. 8 (Internasional)

Pertemuan 8 akan menambahkan dimensi *geographic* pada kerangka fit yang sudah dibangun. Pertanyaan barunya: ketika perusahaan melintasi batas-batas negara, *fit* antar-bisnis dalam portofolio yang dianalisis pada Ch.8 harus diperluas menjadi *fit* antara strategi korporat dan konteks pasar internasional yang heterogen — preferensi konsumen yang berbeda, struktur kompetitif yang berbeda, regulasi yang berbeda, dan dinamika institusional yang berbeda. *Strategic fit* tetap menjadi konsep payung; yang berubah adalah dimensi dan kompleksitas lingkungan yang harus di-*match*. Kontinuitas konseptual ini menjadi alasan mengapa investasi dalam memahami kerangka fit secara mendalam pada Pertemuan 7 akan memudahkan pemahaman strategi internasional pada Pertemuan 8.
"""



def build_cr11() -> str:
    return "# CR Artikel 11 placeholder\n\nPlaceholder body.\n"


def build_cr12() -> str:
    return "# CR Artikel 12 placeholder\n\nPlaceholder body.\n"


# ============================================================================
# PHASE 3 - PANDOC
# ============================================================================
def pandoc(md: Path, out: Path) -> None:
    result = subprocess.run(
        [PANDOC, str(md), f"--reference-doc={REFERENCE}", "-o", str(out)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    print(f"Generated: {out.name}")


# ============================================================================
# MAIN
# ============================================================================
if __name__ == "__main__":
    TEMP.mkdir(parents=True, exist_ok=True)
    OUT_RMK.mkdir(parents=True, exist_ok=True)
    OUT_CR.mkdir(parents=True, exist_ok=True)
    if not REFERENCE.exists():
        raise FileNotFoundError(f"reference.docx not found at {REFERENCE}")

    print("Phase 1: Extracting TPGS Ch.8 figures...")
    figures = extract_figures(EBOOK, FIGURES_DIR)
    validate_figures(figures)

    print("Phase 2: Building markdown and running pandoc...")
    rmk_md  = build_rmk(figures)
    cr11_md = build_cr11()
    cr12_md = build_cr12()

    for name, content, out in [
        ("rmk_w7.md",  rmk_md,  OUT_RMK / "01079_Dzaki Muhammad Yusfian_RMK Pert. 7.docx"),
        ("cr11.md",    cr11_md, OUT_CR  / "01079_Dzaki Muhammad Yusfian_Artikel 11.docx"),
        ("cr12.md",    cr12_md, OUT_CR  / "01079_Dzaki Muhammad Yusfian_Artikel 12.docx"),
    ]:
        md = TEMP / name
        md.write_text(content, encoding="utf-8")
        pandoc(md, out)
    print("All three documents generated successfully.")
    print(f"RMK : {OUT_RMK}")
    print(f"CR  : {OUT_CR}")
