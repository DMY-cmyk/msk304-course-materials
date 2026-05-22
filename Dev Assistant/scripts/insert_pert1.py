"""Insert Pertemuan 1 section into RMK Pra UTS.docx.

Idempotent: if a 'PERTEMUAN 1' Heading 1 already exists, exits with code 3
without modifying the document.
"""
from __future__ import annotations
import sys
from pathlib import Path
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = Path(__file__).resolve().parents[2]
DOCX = ROOT / "RMK Pra UTS.docx"
IMG_DIR = ROOT / "images" / "pertemuan-1"

# ===========================================================================
# CONTENT — Pertemuan 1 paragraph and table data
# ===========================================================================

PERT1_TITLE = "BAGIAN II — PERTEMUAN 1: HAKIKAT STRATEGI DAN KEUNGGULAN KOMPETITIF"

S11_HEADING = "§1.1 Pengantar & Pemetaan Bab"
S11_PARAS = [
    ("First Paragraph",
     "Pertemuan 1 merupakan gerbang konseptual seluruh mata kuliah MST304. "
     "Pada pertemuan ini, mahasiswa diperkenalkan pada silabus, pembagian tugas, "
     "dan pertanyaan paling mendasar dalam manajemen strategik: apa itu strategi, "
     "mengapa strategi penting, dan bagaimana sebuah perusahaan dapat mencapai "
     "keunggulan kompetitif yang berkelanjutan. Bab 1 dari Gamble, Peteraf, dan "
     "Thompson (2021) berjudul 'Strategy, Business Models, and Competitive "
     "Advantage' menyediakan kerangka untuk menjawab tiga pertanyaan tersebut."),
    ("Body Text",
     "Pemetaan bab dapat diringkas ke dalam lima tema yang saling terkait: "
     "(1) definisi strategi sebagai serangkaian tindakan kompetitif yang "
     "terkoordinasi; (2) hubungan antara strategi dan model bisnis sebagai logika "
     "ekonomi yang menjadikan strategi layak secara finansial; (3) keunggulan "
     "kompetitif berkelanjutan sebagai tujuan utama proses strategik; "
     "(4) kapabilitas dinamis dan evolusi strategi dari elemen deliberate, "
     "emergent, dan abandoned; serta (5) tiga uji untuk menilai apakah suatu "
     "strategi tergolong strategi yang menang. Kelima tema ini menjadi fondasi "
     "yang akan diperdalam oleh Pertemuan 2 (proses manajerial) hingga "
     "Pertemuan 7 (strategi korporat dan diversifikasi)."),
]

S12_HEADING = "§1.2 Apa Itu Strategi? — Lima Tindakan Inti"
S12_PARAS = [
    ("First Paragraph",
     "Gamble, Peteraf, dan Thompson (2021) mendefinisikan strategi sebagai "
     "serangkaian tindakan dan pendekatan bisnis terkoordinasi yang dirancang "
     "manajemen untuk menumbuhkan perusahaan, menarik dan melayani pelanggan, "
     "bersaing dengan sukses, menjalankan operasi, serta mencapai tujuan "
     "organisasional dan finansial. Strategi bukan rangkaian taktik ad hoc, "
     "melainkan keputusan-keputusan saling terkait yang membentuk pola "
     "tindakan berkelanjutan."),
    ("Body Text",
     "Penulis mengidentifikasi lima tindakan kompetitif inti yang membentuk "
     "anatomi strategi setiap perusahaan. Kelima tindakan ini memandu manajer "
     "untuk memutuskan bagaimana memposisikan organisasi terhadap pesaing, "
     "kepada siapa nilai akan ditawarkan, dengan mitra mana akan berkolaborasi, "
     "serta bagaimana mengorganisasi rantai aktivitas internal untuk "
     "menghasilkan nilai pelanggan dengan biaya yang lebih rendah atau "
     "kualitas yang lebih tinggi dibanding rival."),
    ("Body Text",
     "Tabel berikut merangkum kelima tindakan strategis tersebut beserta "
     "contoh konkretnya pada konteks perusahaan Indonesia agar pembaca "
     "dapat segera melihat aplikasi praktisnya."),
]

S12_TABLE = [
    ("Tindakan Strategis", "Contoh Indonesia"),
    ("Positioning vs Rivals",
     "Bank BCA memposisikan diri sebagai bank transaksi premium dengan "
     "jaringan ATM dan layanan mobile-banking terluas di segmen ritel "
     "menengah-atas, berbeda dari BRI yang fokus segmen mikro."),
    ("Differentiation",
     "Indomilk dan Ultrajaya berdiferensiasi melalui klaim 'susu segar' "
     "vs susu UHT dengan rasa khas, menghindari head-to-head pada "
     "kategori susu bubuk yang didominasi Frisian Flag dan Dancow."),
    ("Geographic & Customer Scope",
     "Indofood beroperasi di 80+ pasar global melalui produk Indomie, "
     "sementara Wings Food fokus pada Asia Tenggara dan pasar domestik "
     "Indonesia."),
    ("Partnerships & Alliances",
     "GoTo terbentuk dari merger Gojek dan Tokopedia (2021) untuk "
     "mengintegrasikan transportasi, e-commerce, dan fintech ke dalam "
     "satu super-app — strategi kemitraan skala besar."),
    ("Value-Chain Configuration",
     "Astra International menjalankan integrasi vertikal di otomotif "
     "(Toyota, Daihatsu, Isuzu) dan keuangan (Astra Credit Companies, "
     "Federal International Finance), menutup loop dari produksi hingga "
     "pembiayaan konsumen."),
]

S13_HEADING = "§1.3 Strategi vs Model Bisnis"
S13_PARAS = [
    ("First Paragraph",
     "Strategi dan model bisnis adalah dua konsep yang sering disamakan "
     "namun secara substantif berbeda. Strategi menjawab pertanyaan 'bagaimana "
     "kita bersaing dan menang?' Model bisnis menjawab pertanyaan 'bagaimana "
     "kita menghasilkan uang dari strategi tersebut?' Gamble et al. menyebut "
     "model bisnis sebagai logika ekonomi yang menjelaskan bagaimana strategi "
     "akan menghasilkan pendapatan yang melebihi biaya."),
    ("Body Text",
     "Model bisnis memiliki dua pilar utama. Pertama, Customer Value Proposition "
     "(CVP) — bagaimana perusahaan akan memberikan nilai kepada pelanggan dengan "
     "harga yang mereka anggap menarik. Kedua, Profit Formula — bagaimana "
     "perusahaan menghasilkan pendapatan yang cukup besar untuk menutup biaya "
     "dan memberikan margin laba memadai. Sebuah strategi yang brilian tetap "
     "akan gagal apabila model bisnis pendukungnya tidak menghasilkan profit "
     "formula yang berkelanjutan."),
    ("Body Text",
     "Contoh klasik yang digunakan Gamble et al. adalah industri radio Amerika "
     "Serikat dengan tiga model bisnis kontras: Pandora dengan model "
     "freemium+iklan, SiriusXM dengan model langganan satelit berbayar, dan "
     "radio siaran terestrial dengan model iklan murni. Strategi mereka untuk "
     "menarik pendengar boleh sama (konten musik), tetapi profit formula yang "
     "berbeda menentukan struktur biaya, sumber pendapatan, dan keberlanjutan "
     "masing-masing. Gambar berikut menyajikan perbandingan tersebut sebagaimana "
     "dimuat dalam buku referensi."),
]
S13_IMG = ("cc_1_1.png",
           "Gambar 1.1 — Pandora, SiriusXM, dan Over-the-Air Broadcast Radio: "
           "Tiga Model Bisnis yang Kontras. "
           "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 1, hlm. 6 (Concepts & Connections 1.1).")

S14_HEADING = "§1.4 Keunggulan Kompetitif yang Berkelanjutan"
S14_PARAS = [
    ("First Paragraph",
     "Tujuan akhir dari proses strategik bukanlah sekadar bersaing, melainkan "
     "mencapai keunggulan kompetitif (competitive advantage) — yaitu kemampuan "
     "menghasilkan imbal hasil di atas rata-rata industri secara konsisten. "
     "Lebih spesifik lagi, Gamble et al. menekankan keunggulan kompetitif yang "
     "berkelanjutan (sustainable competitive advantage, SCA): keunggulan yang "
     "bertahan dalam jangka panjang menghadapi upaya rival untuk menirunya."),
    ("Body Text",
     "Empat sumber utama SCA yang dibahas di Bab 1 adalah: (1) keunggulan biaya "
     "rendah yang sulit ditandingi rival; (2) diferensiasi produk atau jasa "
     "berdasarkan atribut yang dihargai pelanggan dan sulit ditiru; (3) fokus "
     "ceruk yang menciptakan kedalaman keahlian pada segmen sempit; dan "
     "(4) kapabilitas internal — kombinasi sumber daya, proses, dan kompetensi "
     "yang langka, sulit ditiru, dan sulit disubstitusi. Keempat sumber ini "
     "akan diperdalam lebih lanjut pada Pertemuan 4 (Resource-Based View) dan "
     "Pertemuan 5 (Strategi Generik Porter)."),
    ("Body Text",
     "Ilustrasi paradigmatik dalam Bab 1 adalah Apple Inc. — perusahaan yang "
     "membangun SCA bertingkat melalui kombinasi desain produk premium, "
     "ekosistem hardware-software-services terintegrasi (iPhone, App Store, "
     "iCloud, Apple Music), dan loyalitas merek yang menghasilkan margin "
     "lebih tinggi dibandingkan rival mana pun di industri smartphone. Sidebar "
     "berikut merangkum strategi Apple sebagaimana dijelaskan oleh Gamble et al."),
]
S14_IMG = ("cc_1_2.png",
           "Gambar 1.2 — Strategi Apple Inc. dan Kesuksesannya di Pasar. "
           "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 1, hlm. 7–8 (Concepts & Connections 1.2).")

S15_HEADING = "§1.5 Kapabilitas Dinamis & Evolusi Strategi"
S15_PARAS = [
    ("First Paragraph",
     "Kapabilitas dinamis (dynamic capabilities) adalah kemampuan organisasi "
     "untuk mengintegrasikan, membangun, dan mengonfigurasi ulang kompetensi "
     "internal maupun eksternal untuk merespons lingkungan yang berubah cepat. "
     "Gamble et al. menempatkannya sebagai sumber SCA yang paling dalam karena "
     "ia bukan aset statis melainkan kapasitas untuk terus memperbarui aset."),
    ("Body Text",
     "Konsekuensi langsung dari kapabilitas dinamis adalah bahwa strategi "
     "tidaklah statis. Strategi yang benar-benar dijalankan oleh perusahaan "
     "(realized strategy) merupakan perpaduan dari dua aliran. Pertama, "
     "deliberate strategy elements — inisiatif terencana yang menjadi bagian "
     "rencana strategis formal manajemen. Kedua, emergent strategy elements — "
     "respons reaktif yang tidak terencana terhadap perubahan kondisi pasar, "
     "manuver pesaing, atau peluang baru yang muncul. Beberapa elemen "
     "deliberate akan gugur di pasar dan menjadi abandoned strategy elements."),
    ("Body Text",
     "Gambar berikut, diadaptasi langsung dari Bab 1 buku referensi, "
     "mengilustrasikan bagaimana strategi yang direalisasikan terbentuk dari "
     "perpaduan dinamis antara elemen yang direncanakan dan elemen yang "
     "muncul tak terencana. Ini menjadi alasan mendasar mengapa perumusan "
     "strategi merupakan 'work in progress' — bukan peristiwa satu kali."),
]
S15_IMG = ("fig_1_1.png",
           "Gambar 1.3 — Strategi Perusahaan sebagai Perpaduan Inisiatif Terencana "
           "dan Penyesuaian Reaktif Tak Terencana. "
           "Sumber: Gamble, Peteraf, Thompson (2021), Ch. 1, hlm. 9 (Figure 1.1).")

S16_HEADING = "§1.6 Tiga Uji Strategi yang Menang"
S16_PARAS = [
    ("First Paragraph",
     "Bagaimana cara mengetahui apakah suatu strategi tergolong strategi yang "
     "menang? Gamble et al. menjawabnya dengan kerangka tiga uji (Three Tests "
     "of a Winning Strategy) yang menjadi pegangan diagnostik bagi manajer "
     "maupun pengamat eksternal."),
    ("Body Text",
     "Ketiga uji tersebut harus dipenuhi secara bersamaan. Kegagalan pada "
     "salah satu uji menjadi sinyal bahwa strategi memerlukan revisi. Tabel "
     "berikut merangkum esensi ketiga uji dan pertanyaan probing yang dapat "
     "diajukan pada konteks perusahaan Indonesia."),
]

S16_TABLE = [
    ("Uji", "Pertanyaan Inti", "Probing Konteks Indonesia"),
    ("Fit Test",
     "Apakah strategi cocok dengan situasi internal, eksternal, dan dinamika "
     "perubahan?",
     "Apakah strategi Tokopedia masih cocok pasca-merger menjadi GoTo, "
     "ketika dinamika kompetitif Shopee mengintensifkan perang harga?"),
    ("Competitive Advantage Test",
     "Apakah strategi menghasilkan keunggulan kompetitif yang berkelanjutan?",
     "Apakah cost-leadership Pertamina di pasar BBM domestik berkelanjutan "
     "ketika energi terbarukan menggerus permintaan BBM fosil?"),
    ("Performance Test",
     "Apakah strategi menghasilkan kinerja finansial dan strategis yang "
     "superior?",
     "Apakah ROE BCA yang konsisten di atas 20% mencerminkan strategi "
     "transactional-banking yang sehat, bukan sekadar siklus suku bunga?"),
]

S17_HEADING = "§1.7 Indonesian Flagship — BCA Lulus Tiga Uji"
S17_PARAS = [
    ("First Paragraph",
     "Untuk menjangkar konsep Pertemuan 1 ke realita pasar Indonesia, "
     "Bank Central Asia (BCA) dipilih sebagai flagship case. BCA adalah salah "
     "satu perusahaan Indonesia yang paling konsisten mendemonstrasikan "
     "kelulusan ketiga uji strategi Gamble et al. dalam kurun dua dekade "
     "terakhir, sebagaimana terlihat dari laporan tahunan (AR) dan keterbukaan "
     "informasi di BEI (IDX)."),
    ("Body Text",
     "Pada uji kecocokan (Fit Test), strategi BCA sebagai bank transaksi "
     "premium dengan jaringan ATM, mobile banking, dan layanan transfer cepat "
     "sangat cocok dengan profil pasar Indonesia: kelas menengah yang "
     "berkembang pesat, tingkat penetrasi rekening yang masih tumbuh, dan "
     "preferensi pelanggan terhadap kemudahan transaksi. Ketika industri "
     "perbankan bergerak ke digitalisasi, BCA telah membangun stack teknologi "
     "transaksi yang sulit ditandingi rival dalam waktu singkat."),
    ("Body Text",
     "Pada uji keunggulan kompetitif (Competitive Advantage Test), BCA "
     "memiliki basis CASA (current account-savings account) terbesar di antara "
     "bank-bank swasta Indonesia, yang menghasilkan biaya dana paling rendah "
     "di kelompoknya. Hal ini diterjemahkan menjadi net interest margin yang "
     "konsisten di kisaran tinggi dan return on equity yang berada di "
     "kelompok atas industri perbankan nasional. Keunggulan ini bersifat "
     "berkelanjutan karena dibangun di atas kepercayaan transaksional yang "
     "terakumulasi selama lebih dari empat dekade."),
    ("Body Text",
     "Pada uji kinerja (Performance Test), laporan tahunan dan publikasi BEI "
     "menunjukkan BCA secara konsisten membukukan laba bersih multi-triliun "
     "rupiah per tahun dengan rasio non-performing loan yang rendah, sementara "
     "valuasi pasar (rasio price-to-book) memberikan premium yang "
     "mencerminkan keyakinan investor terhadap keberlanjutan strategi. "
     "Catatan: angka-angka spesifik yang dirujuk dalam analisis ini bersumber "
     "dari laporan tahunan dan keterbukaan IDX yang tersedia publik; ketika "
     "data spesifik tidak dapat dipastikan, deskripsi bersifat kualitatif "
     "untuk menjaga integritas analitis."),
]

S18_HEADING = "§1.8 Sintesis Pertemuan 1 dan Jembatan ke Pertemuan 2"
S18_PARAS = [
    ("First Paragraph",
     "Pertemuan 1 menegaskan bahwa strategi bukan sekadar pernyataan tujuan "
     "yang terdengar bagus, melainkan jawaban operasional terhadap pertanyaan "
     "'bagaimana kita bersaing dan menang?' Strategi yang baik memadukan "
     "lima tindakan inti — positioning, diferensiasi, ruang lingkup, kemitraan, "
     "dan konfigurasi rantai nilai — dengan model bisnis yang menghasilkan "
     "profit formula berkelanjutan, sehingga menghasilkan keunggulan kompetitif "
     "yang lulus tiga uji: fit, competitive advantage, dan performance. "
     "Kapabilitas dinamis menjamin strategi terus berevolusi melalui interaksi "
     "antara elemen deliberate dan emergent."),
    ("Body Text",
     "Pemahaman ini membuka jalan ke Pertemuan 2 yang akan mengoperasionalkan "
     "wawasan konseptual Pertemuan 1 ke dalam proses manajerial lima tahap: "
     "pengembangan visi-misi-nilai inti, penetapan tujuan, perumusan strategi, "
     "implementasi dan eksekusi, serta evaluasi dan pengendalian. Pertemuan 1 "
     "menjawab 'apa itu strategi'; Pertemuan 2 mengajarkan 'bagaimana proses "
     "menyusun dan menjalankan strategi tersebut'."),
]

BAGIAN_I_BRIDGE = (
    "Pertemuan 1 berfungsi sebagai gerbang konseptual yang mendahului alur "
    "naratif induk: ia mengenalkan definisi strategi, hubungan strategi dengan "
    "model bisnis, sumber-sumber keunggulan kompetitif yang berkelanjutan, "
    "evolusi strategi dari elemen deliberate dan emergent, serta tiga uji "
    "strategi yang menang. Konsep-konsep tersebut menjadi fondasi yang akan "
    "diisi konten metodologis dan empiris oleh Pertemuan 2 hingga 7."
)

# ===========================================================================
# HELPERS
# ===========================================================================

def already_inserted(doc) -> bool:
    """Idempotency check — true if a Heading 1 already contains 'PERTEMUAN 1'."""
    for p in doc.paragraphs:
        if p.style.name == "Heading 1" and "PERTEMUAN 1" in p.text.upper():
            return True
    return False


def insert_paragraph_before(anchor_paragraph, style_name: str, text: str, doc):
    """Insert a paragraph with given style+text immediately before anchor.

    Uses python-docx high-level API: append to body, then move the XML element
    via addprevious. This avoids any style-name vs style-id confusion.
    """
    new_p = doc.add_paragraph(text, style=style_name)
    new_p_el = new_p._element
    new_p_el.getparent().remove(new_p_el)
    anchor_paragraph._element.addprevious(new_p_el)
    return new_p


def insert_table_before(anchor_paragraph, rows_data, doc):
    """Build a table with rows_data (list of tuples) and insert before anchor.

    First row is treated as header.
    """
    n_cols = len(rows_data[0])
    n_rows = len(rows_data)
    tbl = doc.add_table(rows=n_rows, cols=n_cols)
    tbl.style = "Table Grid"
    for r_idx, row in enumerate(rows_data):
        for c_idx, cell_text in enumerate(row):
            cell = tbl.rows[r_idx].cells[c_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(cell_text)
            if r_idx == 0:
                run.bold = True
    tbl_el = tbl._element
    tbl_el.getparent().remove(tbl_el)
    anchor_paragraph._element.addprevious(tbl_el)


def insert_image_before(anchor_paragraph, img_path: Path, caption: str, doc):
    """Insert centered image paragraph + caption paragraph before anchor."""
    tmp_p = doc.add_paragraph()
    tmp_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    tmp_p.add_run().add_picture(str(img_path), width=Inches(6.0))
    tmp_p_el = tmp_p._element
    tmp_p_el.getparent().remove(tmp_p_el)
    anchor_paragraph._element.addprevious(tmp_p_el)

    cap_p = doc.add_paragraph(caption, style="Caption")
    cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap_p_el = cap_p._element
    cap_p_el.getparent().remove(cap_p_el)
    anchor_paragraph._element.addprevious(cap_p_el)


def find_anchor(doc, marker_text: str):
    for p in doc.paragraphs:
        if p.text.strip().startswith(marker_text):
            return p
    return None


# ===========================================================================
# MAIN
# ===========================================================================

def main() -> int:
    if not DOCX.exists():
        print(f"target docx not found: {DOCX}", file=sys.stderr)
        return 1
    doc = Document(DOCX)
    if already_inserted(doc):
        print("PERTEMUAN 1 already present — refusing to insert again", file=sys.stderr)
        return 3

    anchor = find_anchor(doc, "BAGIAN II — PERTEMUAN 2")
    if anchor is None:
        print("anchor not found: 'BAGIAN II — PERTEMUAN 2'", file=sys.stderr)
        return 4

    insert_paragraph_before(anchor, "Heading 1", PERT1_TITLE, doc)

    insert_paragraph_before(anchor, "Heading 2", S11_HEADING, doc)
    for style, text in S11_PARAS:
        insert_paragraph_before(anchor, style, text, doc)

    insert_paragraph_before(anchor, "Heading 2", S12_HEADING, doc)
    for style, text in S12_PARAS:
        insert_paragraph_before(anchor, style, text, doc)
    insert_table_before(anchor, S12_TABLE, doc)

    insert_paragraph_before(anchor, "Heading 2", S13_HEADING, doc)
    for style, text in S13_PARAS:
        insert_paragraph_before(anchor, style, text, doc)
    img_name, caption = S13_IMG
    insert_image_before(anchor, IMG_DIR / img_name, caption, doc)

    insert_paragraph_before(anchor, "Heading 2", S14_HEADING, doc)
    for style, text in S14_PARAS:
        insert_paragraph_before(anchor, style, text, doc)
    img_name, caption = S14_IMG
    insert_image_before(anchor, IMG_DIR / img_name, caption, doc)

    insert_paragraph_before(anchor, "Heading 2", S15_HEADING, doc)
    for style, text in S15_PARAS:
        insert_paragraph_before(anchor, style, text, doc)
    img_name, caption = S15_IMG
    insert_image_before(anchor, IMG_DIR / img_name, caption, doc)

    insert_paragraph_before(anchor, "Heading 2", S16_HEADING, doc)
    for style, text in S16_PARAS:
        insert_paragraph_before(anchor, style, text, doc)
    insert_table_before(anchor, S16_TABLE, doc)

    insert_paragraph_before(anchor, "Heading 2", S17_HEADING, doc)
    for style, text in S17_PARAS:
        insert_paragraph_before(anchor, style, text, doc)

    insert_paragraph_before(anchor, "Heading 2", S18_HEADING, doc)
    for style, text in S18_PARAS:
        insert_paragraph_before(anchor, style, text, doc)

    bagian_i_11 = find_anchor(doc, "§1.1 Alur Naratif Induk")
    if bagian_i_11 is not None:
        bagian_i_11.text = "§1.1 Alur Naratif Induk (Pertemuan 1 → 7)"
        for run in bagian_i_11.runs:
            run.bold = True
        bagian_i_12 = find_anchor(doc, "§1.2 Matriks Arus Teoritis")
        if bagian_i_12 is not None:
            insert_paragraph_before(bagian_i_12, "Body Text", BAGIAN_I_BRIDGE, doc)
        else:
            print("warning: §1.2 anchor not found — bridge paragraph skipped",
                  file=sys.stderr)
    else:
        print("warning: BAGIAN I §1.1 anchor not found — title not updated",
              file=sys.stderr)

    doc.save(DOCX)
    print(f"saved: {DOCX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
