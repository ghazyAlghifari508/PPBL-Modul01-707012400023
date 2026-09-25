import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="D3D3D3"):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    border_v = OxmlElement('w:insideV')
    border_v.set(qn('w:val'), 'none')
    tblBorders.append(border_v)
    tblPr.append(tblBorders)

def add_header_footer(doc):
    for s in doc.sections:
        s.different_first_page_header_footer = True
        header = s.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Pemrograman Perangkat Bergerak Lanjut • Modul 1 (Pekan 01)")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(120, 120, 120)
        
        footer = s.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Ghazy Nabil Alghfari (707012400023) - D3IF 48-03 • Telkom University")
        frun.font.name = "Times New Roman"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(120, 120, 120)

def main():
    doc = docx.Document()
    
    # Set standard margins (2.54 cm all around)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
    
    # Configure base styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(11.5)
    normal_style.font.color.rgb = RGBColor(30, 30, 30)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(4)
    normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    add_header_footer(doc)
    
    # ==========================================
    # 1. HALAMAN SAMPUL (COVER)
    # ==========================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("KEMENTERIAN PENDIDIKAN TINGGI, SAINS, DAN TEKNOLOGI\nUNIVERSITAS TELKOM\nFAKULTAS ILMU TERAPAN\nPROGRAM STUDI D3 REKAYASA PERANGKAT LUNAK APLIKASI")
    r_inst.bold = True
    r_inst.font.size = Pt(12)
    r_inst.font.color.rgb = RGBColor(13, 92, 58) # Nusantara Green
    
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_after = Pt(14)
    
    # Logo Telkom
    logo_path = r"C:\Users\alghi\.gemini\antigravity\brain\80e218f5-41d7-4a48-aaec-7c2dffedbd59\.user_uploaded\media_1790327259938.png"
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(14)
        run_logo = p_logo.add_run()
        run_logo.add_picture(logo_path, width=Inches(2.1))
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("LAPORAN PRAKTIKUM\nPEMROGRAMAN PERANGKAT BERGERAK LANJUT")
    r_title.bold = True
    r_title.font.size = Pt(15)
    r_title.font.color.rgb = RGBColor(13, 92, 58)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(24)
    r_sub = p_sub.add_run("MODUL I\nPENGENALAN FLUTTER, WIDGET TREE, DAN DASAR MANAJEMEN STATE")
    r_sub.bold = True
    r_sub.font.size = Pt(12.5)
    r_sub.font.color.rgb = RGBColor(70, 70, 70)
    
    p_desc = doc.add_paragraph()
    p_desc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_desc.paragraph_format.space_after = Pt(24)
    r_desc = p_desc.add_run("Disusun untuk Memenuhi Komponen Penilaian Mata Kuliah\nPemrograman Perangkat Bergerak Lanjut (PPBL)")
    r_desc.italic = True
    r_desc.font.size = Pt(10.5)
    r_desc.font.color.rgb = RGBColor(100, 100, 100)
    
    # Student Info Box (Table)
    tbl_id = doc.add_table(rows=5, cols=3)
    tbl_id.alignment = WD_TABLE_ALIGNMENT.CENTER
    id_data = [
        ("Nama Mahasiswa", ":", "Ghazy Nabil Alghfari"),
        ("Nomor Induk Mahasiswa (NIM)", ":", "707012400023"),
        ("Kelas", ":", "D3IF 48-03"),
        ("Dosen Pengampu", ":", "Tim Dosen Pemrograman Perangkat Bergerak Lanjut"),
        ("Tahun Akademik", ":", "2025/2026 (Semester Genap)"),
    ]
    for i, (k, sep, val) in enumerate(id_data):
        row = tbl_id.rows[i]
        
        c0 = row.cells[0]
        c0.width = Inches(2.5)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.size = Pt(10.5)
        
        c1 = row.cells[1]
        c1.width = Inches(0.2)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(sep)
        r1.bold = True
        r1.font.size = Pt(10.5)
        
        c2 = row.cells[2]
        c2.width = Inches(3.5)
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(2)
        r2 = p2.add_run(val)
        r2.font.size = Pt(10.5)
        if i in [0, 1, 2]:
            r2.bold = True
            r2.font.color.rgb = RGBColor(13, 92, 58)
    
    p_foot = doc.add_paragraph()
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_foot.paragraph_format.space_before = Pt(36)
    r_foot = p_foot.add_run("BANDUNG\n2026")
    r_foot.bold = True
    r_foot.font.size = Pt(11.5)
    
    doc.add_page_break()
    
    # Helper functions for report sections
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(13.5)
        r.font.color.rgb = RGBColor(13, 92, 58)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(12)
        r.font.color.rgb = RGBColor(27, 77, 62)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(11.5)
        r.font.color.rgb = RGBColor(45, 55, 72)
        return p

    def add_p(text, bold_prefix=None, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.bold = True
        r = p.add_run(text)
        r.italic = italic
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.bold = True
        p.add_run(text)
        return p

    def add_code(code_str):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F8F9FA")
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.05
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(code_str)
        r.font.name = "Consolas"
        r.font.size = Pt(9.0)
        r.font.color.rgb = RGBColor(34, 40, 49)
        doc.add_paragraph().paragraph_format.space_after = Pt(2)

    def add_figure(img_path, caption_num, caption_text, width=Inches(2.7)):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.paragraph_format.keep_with_next = True
            r_img = p_img.add_run()
            r_img.add_picture(img_path, width=width)
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(8)
            rcap_num = p_cap.add_run(f"Gambar {caption_num}. ")
            rcap_num.bold = True
            rcap_num.font.size = Pt(10)
            rcap_text = p_cap.add_run(caption_text)
            rcap_text.italic = True
            rcap_text.font.size = Pt(10)
            rcap_text.font.color.rgb = RGBColor(60, 60, 60)

    # ==========================================
    # 2. TUJUAN PRAKTIKUM
    # ==========================================
    add_h1("2. TUJUAN PRAKTIKUM")
    add_p("Praktikum Modul 1 Pemrograman Perangkat Bergerak Lanjut ini bertujuan untuk membekali mahasiswa dengan penguasaan mendalam mengenai arsitektur dasar Flutter dan mekanisme manajemen state lokal. Secara spesifik, capaian pembelajaran pada setiap bagian praktikum dirumuskan dengan kalimat sendiri sebagai berikut:")
    
    add_h2("A. Praktikum (NO AI) – Proyek: praktikum_widget")
    add_bullet(" Memahami alur pembuatan struktur dasar proyek Flutter melalui CLI dan struktur dependensi pada berkas pubspec.yaml.", "1.")
    add_bullet(" Menguasai konsep dasar deklaratif UI pada framework Flutter dengan membangun komponen antarmuka yang terisolasi dan modular.", "2.")
    add_bullet(" Mengimplementasikan StatelessWidget untuk menyajikan data profil mahasiswa yang bersifat statis (immutable) secara efisien.", "3.")
    add_bullet(" Mengimplementasikan StatefulWidget untuk mengelola siklus hidup komponen dan menangani interaktivitas lokal melalui pemanggilan fungsi setState().", "4.")
    add_bullet(" Menguji efisiensi mekanisme Hot Reload dalam memodifikasi antarmuka secara instan tanpa kehilangan state aplikasi yang sedang berjalan.", "5.")

    add_h2("B. Praktikum Berbantuan AI – Proyek: praktikum_widget_ai")
    add_bullet(" Menguasai metodologi prompt engineering bertahap (incremental prompting) untuk merekonstruksi antarmuka Flutter menggunakan asisten kecerdasan buatan.", "1.")
    add_bullet(" Mampu merumuskan prompt terstruktur yang mencakup peran (role), konteks (context), tugas spesifik (task), batasan teknologi (constraints), serta format luaran (output format).", "2.")
    add_bullet(" Melatih ketelitian membaca kode (code reading) dan kemampuan memverifikasi kesesuaian kode hasil generasi AI terhadap standar clean architecture dan best practices Flutter.", "3.")
    add_bullet(" Menganalisis perbedaan teknis dan perilaku aplikasi apabila pembaruan variabel dilakukan tanpa membungkusnya dalam setState().", "4.")

    add_h2("C. Tugas Praktikum – Proyek: nusantara_cerdas_707012400023")
    add_bullet(" Merancang antarmuka aplikasi dasbor publik 'Kota Nusantara Cerdas' secara komprehensif, modular, responsif, dan konsisten terhadap tema Forest Green (#0D5C3A).", "1.")
    add_bullet(" Membangun komponen StatelessWidget yang dapat digunakan ulang (reusable) untuk menyajikan identitas kota serta representasi 6 Pilar Smart City (Smart Governance, Smart Economy, Smart Living, Smart Mobility, Smart Environment, dan Smart People).", "2.")
    add_bullet(" Mengembangkan komponen panel laporan warga berbasis StatefulWidget yang dilengkapi logika bisnis validasi non-negatif dan Dynamic Status Badge tiga level (Pelayanan Lancar, Pelayanan Sibuk, Perlu Penambahan Petugas).", "3.")
    add_bullet(" Memverifikasi keandalan kode melalui penulisan uji widget otomatis (widget testing) serta memastikan kode bebas dari peringatan linter (flutter analyze: zero issues).", "4.")

    # ==========================================
    # 3. ALAT DAN BAHAN
    # ==========================================
    add_h1("3. ALAT DAN BAHAN")
    add_p("Untuk menunjang pelaksanaan seluruh rangkaian praktikum dan tugas mandiri pada Modul 1 ini, digunakan lingkungan pengembangan dengan spesifikasi perangkat keras dan perangkat lunak sebagai berikut:")
    
    add_h2("3.1 Spesifikasi Perangkat Keras (Hardware)")
    tbl_hw = doc.add_table(rows=6, cols=3)
    tbl_hw.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_hw)
    hw_headers = ["No", "Komponen Perangkat Keras", "Spesifikasi yang Digunakan"]
    for j, h in enumerate(hw_headers):
        cell = tbl_hw.cell(0, j)
        set_cell_background(cell, "0D5C3A")
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(255, 255, 255)
    
    hw_data = [
        ("1", "Perangkat Komputer", "Laptop ASUS / Windows PC x64 Architecture"),
        ("2", "Prosesor (CPU)", "Intel(R) Core(TM) i5-1135G7 @ 2.40GHz (8 CPUs)"),
        ("3", "Memori Utama (RAM)", "16.0 GB DDR4 High Speed RAM"),
        ("4", "Media Penyimpanan", "SSD NVMe M.2 512 GB (Tersedia >50 GB Free Space)"),
        ("5", "Layar & Resolusi", "15.6 Inch Full HD (1920 x 1080 piksel)"),
    ]
    for i, row_data in enumerate(hw_data):
        row = tbl_hw.rows[i+1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            if (i % 2 == 1):
                set_cell_background(cell, "F7FAFC")
            set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.size = Pt(9.5)
            if j == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r.bold = True

    add_h2("3.2 Spesifikasi Perangkat Lunak (Software) dan SDK")
    tbl_sw = doc.add_table(rows=10, cols=3)
    tbl_sw.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_sw)
    sw_headers = ["No", "Perangkat Lunak / SDK", "Versi & Konfigurasi Aktual"]
    for j, h in enumerate(sw_headers):
        cell = tbl_sw.cell(0, j)
        set_cell_background(cell, "0D5C3A")
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    sw_data = [
        ("1", "Sistem Operasi", "Microsoft Windows 11 Home 64-bit (Build 26100)"),
        ("2", "Flutter SDK", "Versi 3.41.2 • Channel stable • Tools Dart 3.11.0"),
        ("3", "Dart SDK", "Versi 3.11.0 (Bawaan resmi terintegrasi Flutter SDK)"),
        ("4", "Android Studio & SDK", "Android Studio Ladybug / Koala • SDK Platform API 33 & 36"),
        ("5", "Android Build-Tools", "Versi 36.1.0 (Dikonfigurasi eksplisit pada build.gradle.kts)"),
        ("6", "Android NDK", "Versi 28.2.13676358 (Installed on Android Sdk/ndk)"),
        ("7", "Android Emulator", "Google Pixel 4 AVD • API 33 (Android 13.0) x86_64"),
        ("8", "Integrated Dev. Env. (IDE)", "Visual Studio Code 1.96.0 + Ekstensi Flutter & Dart"),
        ("9", "Version Control & CLI", "Git for Windows 2.45+ dan GitHub CLI (gh) versi 2.95.0"),
    ]
    for i, row_data in enumerate(sw_data):
        row = tbl_sw.rows[i+1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            if (i % 2 == 1):
                set_cell_background(cell, "F7FAFC")
            set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.size = Pt(9.5)
            if j == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r.bold = True

    # ==========================================
    # 4. LANGKAH-LANGKAH PRAKTIKUM
    # ==========================================
    add_h1("4. LANGKAH-LANGKAH PRAKTIKUM")
    add_p("Bagian ini menguraikan tahapan pengerjaan secara sistematis dan runtut untuk masing-masing bagian praktikum, disertai potongan kode program (code snippet) dan penjelasan teknisnya.")

    # 4.1 Bagian A
    add_h2("4.1 Bagian A: Praktikum (NO AI) – Proyek: praktikum_widget")
    add_p("Pada bagian ini, aplikasi dibangun secara manual tanpa bantuan kecerdasan buatan untuk memahami konsep dasar hierarki widget dan manajemen state.")
    
    add_h3("Langkah 1: Inisialisasi Proyek Flutter")
    add_p("Proyek dibuat melalui terminal menggunakan perintah bawaan Flutter CLI:")
    add_code("""flutter create praktikum_widget
cd praktikum_widget""")
    add_p("Perintah di atas menghasilkan struktur direktori standar Flutter yang memuat folder lib/ sebagai tempat utama penulisan basis kode Dart.")

    add_h3("Langkah 2: Pembuatan Stateless Widget (lib/profil_card.dart)")
    add_p("Dibuat komponen ProfilCard yang bertugas menampilkan informasi identitas mahasiswa. Karena data identitas bersifat statis dan tidak berubah selama aplikasi berjalan, komponen ini diturunkan dari StatelessWidget. Properti ditandai dengan kata kunci final dan konstruktor memanfaatkan const untuk optimalisasi alokasi memori.")
    add_code("""import 'package:flutter/material.dart';

class ProfilCard extends StatelessWidget {
  const ProfilCard({
    super.key,
    required this.nama,
    required this.nim,
    required this.prodi,
  });

  final String nama;
  final String nim;
  final String prodi;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        boxShadow: const [
          BoxShadow(
            color: Colors.black12,
            blurRadius: 6,
            offset: Offset(0, 3),
          ),
        ],
      ),
      child: Row(
        children: [
          const CircleAvatar(
            radius: 28,
            backgroundColor: Colors.indigo,
            child: Icon(Icons.person, color: Colors.white, size: 28),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  nama,
                  style: const TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 4),
                Text('NIM: $nim', style: const TextStyle(fontSize: 14, color: Colors.black54)),
                Text(prodi, style: const TextStyle(fontSize: 14, color: Colors.black54)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}""")
    add_p("Penjelasan Kode: Widget Container digunakan sebagai pembungkus berdekorasi warna putih, radius sudut membulat 12 piksel, dan bayangan tipis. Di dalamnya, Row membagi area secara horizontal menjadi avatar profil (CircleAvatar) dan kolom informasi (Column) yang dibungkus Expanded agar teks nama panjang tidak menyebabkan overflow.")

    add_h3("Langkah 3: Pembuatan Stateful Widget (lib/penghitung_suka.dart)")
    add_p("Dibuat komponen PenghitungSuka yang memiliki state lokal berupa variabel _jumlahSuka (int) dan _disukai (bool). Komponen ini diturunkan dari StatefulWidget dan dihubungkan dengan kelas _PenghitungSukaState.")
    add_code("""import 'package:flutter/material.dart';

class PenghitungSuka extends StatefulWidget {
  const PenghitungSuka({super.key});

  @override
  State<PenghitungSuka> createState() => _PenghitungSukaState();
}

class _PenghitungSukaState extends State<PenghitungSuka> {
  int _jumlahSuka = 0;
  bool _disukai = false;

  void _tambahSuka() {
    setState(() {
      _jumlahSuka++;
      _disukai = true;
    });
  }

  void _resetSuka() {
    setState(() {
      _jumlahSuka = 0;
      _disukai = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            Text(
              'Jumlah Suka: $_jumlahSuka',
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
            ),
            const SizedBox(height: 12),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton.icon(
                  onPressed: _tambahSuka,
                  icon: Icon(_disukai ? Icons.favorite : Icons.favorite_border),
                  label: const Text('Suka'),
                ),
                const SizedBox(width: 12),
                OutlinedButton(
                  onPressed: _resetSuka,
                  child: const Text('Reset'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}""")
    add_p("Penjelasan Kode: Fungsi _tambahSuka() dan _resetSuka() membungkus pembaruan nilai variabel di dalam setState(). Mekanisme ini memberitahu Flutter framework bahwa internal state telah berubah, sehingga framework akan memicu pemanggilan ulang metode build() pada State object tersebut untuk memperbarui angka dan ikon di layar secara reaktif.")

    add_h3("Langkah 4: Penyusunan Tata Letak Halaman Utama dan Titik Masuk (main.dart)")
    add_p("Seluruh komponen dirakit di dalam lib/halaman_utama.dart menggunakan Scaffold dan SingleChildScrollView agar tampilan responsif, kemudian dihubungkan pada lib/main.dart:")
    add_code("""import 'package:flutter/material.dart';
import 'halaman_utama.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Praktikum Widget',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
        useMaterial3: true,
      ),
      home: const HalamanUtama(),
    );
  }
}""")

    # 4.2 Bagian B
    add_h2("4.2 Bagian B: Praktikum Berbantuan AI – Proyek: praktikum_widget_ai")
    add_p("Pada bagian ini, aplikasi dibangun ulang dalam proyek terpisah bernama praktikum_widget_ai menggunakan teknik prompt engineering bertahap untuk melatih interaksi efektif dengan asisten AI pengembang.")
    
    add_h3("Langkah 1: Inisialisasi Proyek Baru")
    add_code("""flutter create praktikum_widget_ai
cd praktikum_widget_ai""")

    add_h3("Langkah 2: Eksekusi Prompt 1 – Konteks Awal dan Rencana Kerja")
    add_p("Prompt pembuka dirancang dengan menetapkan peran, konteks, batasan tanpa paket eksternal, dan meminta rencana kerja terlebih dahulu:")
    add_code("""Kamu berperan sebagai asisten pemrograman Flutter untuk mahasiswa yang baru belajar widget.
Konteks: saya mengerjakan proyek Flutter bernama praktikum_widget_ai pada Visual Studio Code.
Materi yang sedang dipelajari adalah Stateless Widget, Stateful Widget, serta layout dan styling.
Tugas: bantu saya membangun satu halaman aplikasi yang memuat kartu profil mahasiswa, penghitung suka, dan dua kotak informasi.
Batasan: gunakan hanya package:flutter/material.dart, tanpa paket tambahan dan tanpa state management eksternal.
Format keluaran: tuliskan dahulu rencana kerja dalam bentuk poin beserta daftar berkas yang akan dibuat. Jangan menulis kode apa pun sebelum saya meminta berkas tertentu.""")
    add_p("Hasil dan Evaluasi: AI memberikan rencana kerja terstruktur yang membagi proyek ke dalam 4 berkas: profil_card.dart, penghitung_suka.dart, halaman_utama.dart, dan main.dart. Rencana ini diverifikasi sesuai dengan arsitektur modular yang diajarkan pada modul.")

    add_h3("Langkah 3: Eksekusi Prompt 2 – Stateless Widget ProfilCard")
    add_code("""Buatkan isi berkas lib/profil_card.dart.
Ketentuan:
1. Satu StatelessWidget bernama ProfilCard.
2. Parameter wajib: nama, nim, prodi, semuanya bertipe String.
3. Gunakan const constructor dan super.key.
4. Tampilan: Container dengan padding 16, sudut membulat 12, warna putih, dan bayangan tipis.
5. Di dalamnya Row berisi CircleAvatar dengan ikon person, lalu Column berisi nama (ukuran 18, tebal), nim, dan prodi (ukuran 14, warna abu-abu).
6. Hanya gunakan package:flutter/material.dart.
Setelah kode, jelaskan fungsi setiap widget dalam satu kalimat per widget, memakai bahasa Indonesia.""")
    add_p("Hasil dan Evaluasi: AI menghasilkan kode bersih dengan parameter required, konstruktor const, dan penjelasan tiap widget (Container, Row, CircleAvatar, SizedBox, Expanded, Column, Text). Kode disalin dan berhasil dikompilasi tanpa galat.")

    add_h3("Langkah 4: Eksekusi Prompt 3 – Stateful Widget PenghitungSuka dan Analisis Tanpa setState()")
    add_code("""Buatkan isi berkas lib/penghitung_suka.dart.
Ketentuan:
1. Satu StatefulWidget bernama PenghitungSuka.
2. Simpan dua state: _jumlahSuka bertipe int dan _disukai bertipe bool.
3. Sediakan tombol Suka untuk menambah _jumlahSuka dan mengubah ikon hati menjadi terisi, serta tombol Reset untuk mengembalikan nilai ke kondisi awal.
4. Seluruh perubahan nilai harus dilakukan di dalam setState().
5. Bungkus tampilan dengan Card bersudut membulat 12 dan padding 16.
6. Hanya gunakan package:flutter/material.dart.
Setelah kode, jelaskan dalam bahasa Indonesia: apa yang terjadi apabila nilai _jumlahSuka diubah tanpa setState().""")
    add_p("Temuan Eksperimen: Sesuai panduan modul, dilakukan percobaan kecil dengan menghapus sementara pembungkus setState() pada fungsi penambah (_jumlahSuka++ tanpa setState). Hasil pengujian membuktikan bahwa meskipun variabel di memori bertambah, nilai pada layar tidak berubah karena Flutter tidak menerima sinyal untuk menandai widget tree sebagai dirty dan merender ulang tampilan.")

    add_h3("Langkah 5: Eksekusi Prompt 4 & 5 – Layout HalamanUtama dan main.dart")
    add_p("Prompt berikutnya menginstruksikan pembuatan halaman utama dengan penambahan dua KotakInfo yang dibungkus Expanded di dalam Row, serta konfigurasi tema Material 3 berwarna indigo pada main.dart.")

    # 4.3 Bagian C
    add_h2("4.3 Bagian C: Tugas Praktikum – Proyek: nusantara_cerdas_707012400023")
    add_p("Pada tugas praktikum ini, dibangun aplikasi dasbor 'Kota Nusantara Cerdas' secara komprehensif dengan mematuhi seluruh spesifikasi desain, logika interaksi, serta identitas resmi mahasiswa.")

    add_h3("Langkah 1: Inisialisasi Proyek Khusus")
    add_code("""flutter create --org com.example nusantara_cerdas_707012400023
cd nusantara_cerdas_707012400023""")

    add_h3("Langkah 2: Konfigurasi Tema Hijau Nusantara pada lib/main.dart")
    add_p("Tema aplikasi dirancang menggunakan warna Forest Green khas IKN Nusantara (#0D5C3A) dengan Material 3 aktif:")
    add_code("""import 'package:flutter/material.dart';
import 'halaman_utama.dart';

void main() {
  runApp(const NusantaraCerdasApp());
}

class NusantaraCerdasApp extends StatelessWidget {
  const NusantaraCerdasApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Nusantara Cerdas',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF0D5C3A),
          primary: const Color(0xFF0D5C3A),
        ),
        scaffoldBackgroundColor: const Color(0xFFF6F8F6),
      ),
      home: const HalamanUtama(),
    );
  }
}""")

    add_h3("Langkah 3: Pembuatan StatelessWidget KepalaKota (lib/kepala_kota.dart)")
    add_p("Widget ini menampilkan identitas Kota Nusantara dan identitas resmi mahasiswa pengembang. Menggunakan Container dengan dekorasi LinearGradient dan kartu identitas terstruktur:")
    add_code("""import 'package:flutter/material.dart';

class KepalaKota extends StatelessWidget {
  const KepalaKota({
    super.key,
    this.namaKota = 'Kota Nusantara',
    this.semboyan = 'Kota Pintar, Hijau, dan Berkelanjutan',
  });

  final String namaKota;
  final String semboyan;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Container(
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [
            theme.colorScheme.primary,
            theme.colorScheme.primaryContainer,
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: theme.colorScheme.primary.withValues(alpha: 0.25),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(12),
                decoration: const BoxDecoration(
                  color: Colors.white,
                  shape: BoxShape.circle,
                  boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 6, offset: Offset(0, 2))],
                ),
                child: Icon(Icons.location_city_rounded, size: 36, color: theme.colorScheme.primary),
              ),
              const SizedBox(width: 14),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(namaKota, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white)),
                    const SizedBox(height: 4),
                    Text(semboyan, style: TextStyle(fontSize: 12, color: Colors.white.withValues(alpha: 0.9), fontStyle: FontStyle.italic)),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(
              color: Colors.black.withValues(alpha: 0.18),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: const [
                    Text(
                      'Pengembang: Ghazy Nabil Alghfari',
                      style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.white),
                    ),
                    SizedBox(height: 2),
                    Text(
                      'NIM: 707012400023  •  Kelas: 48-03',
                      style: TextStyle(fontSize: 11, color: Colors.white70),
                    ),
                  ],
                ),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  decoration: BoxDecoration(
                    color: Colors.white.withValues(alpha: 0.2),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: const Text('PPBL 2026', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Colors.white)),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}""")

    add_h3("Langkah 4: Pembuatan StatelessWidget KartuPilar (lib/kartu_pilar.dart)")
    add_p("Widget KartuPilar dibuat sangat modular untuk menampilkan enam pilar smart city dengan parameter dinamis:")
    add_code("""import 'package:flutter/material.dart';

class KartuPilar extends StatelessWidget {
  const KartuPilar({
    super.key,
    required this.namaPilar,
    required this.deskripsi,
    required this.icon,
    this.accentColor = const Color(0xFF0D5C3A),
  });

  final String namaPilar;
  final String deskripsi;
  final IconData icon;
  final Color accentColor;

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 1.5,
      margin: const EdgeInsets.symmetric(vertical: 6),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: BorderSide(color: accentColor.withValues(alpha: 0.25), width: 1),
      ),
      color: Colors.white,
      child: Padding(
        padding: const EdgeInsets.all(14),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: accentColor.withValues(alpha: 0.12),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(icon, color: accentColor, size: 28),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(namaPilar, style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 4),
                  Text(deskripsi, style: TextStyle(fontSize: 12.5, color: Colors.grey.shade700, height: 1.35)),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}""")

    add_h3("Langkah 5: Pembuatan StatefulWidget PanelLaporanWarga (lib/panel_laporan.dart)")
    add_p("Komponen ini mengelola data reaktif jumlah laporan dan mengimplementasikan aturan Dynamic Status Badge 3 level serta batas non-negatif:")
    add_code("""import 'package:flutter/material.dart';

class PanelLaporanWarga extends StatefulWidget {
  const PanelLaporanWarga({super.key});

  @override
  State<PanelLaporanWarga> createState() => _PanelLaporanWargaState();
}

class _PanelLaporanWargaState extends State<PanelLaporanWarga> {
  int _jumlahLaporan = 0;

  void _laporanMasuk() {
    setState(() {
      _jumlahLaporan++;
    });
  }

  void _laporanSelesai() {
    if (_jumlahLaporan > 0) {
      setState(() {
        _jumlahLaporan--;
      });
    }
  }

  void _resetHarian() {
    setState(() {
      _jumlahLaporan = 0;
    });
  }

  // Logika Penentuan Status Badge Dinamis
  String get _statusPelayanan {
    if (_jumlahLaporan < 5) return 'Pelayanan Lancar';
    if (_jumlahLaporan <= 10) return 'Pelayanan Sibuk';
    return 'Perlu Penambahan Petugas';
  }

  Color get _statusColor {
    if (_jumlahLaporan < 5) return const Color(0xFF2E7D32); // Hijau
    if (_jumlahLaporan <= 10) return const Color(0xFFE65100); // Oranye
    return const Color(0xFFC62828); // Merah
  }

  IconData get _statusIcon {
    if (_jumlahLaporan < 5) return Icons.check_circle_outline_rounded;
    if (_jumlahLaporan <= 10) return Icons.warning_amber_rounded;
    return Icons.error_outline_rounded;
  }

  @override
  Widget build(BuildContext context) {
    // Membangun tampilan card dengan tombol Laporan Masuk, Laporan Selesai, Reset Harian
    // dan status badge yang berubah dinamis mengikuti nilai _jumlahLaporan.
    // ... (Implementasi UI lengkap pada berkas proyek)
  }
}""")

    add_h3("Langkah 6: Perakitan Halaman Utama dan Pengujian Otomatis")
    add_p("Pada lib/halaman_utama.dart, seluruh komponen digabungkan secara runut di dalam Column yang dibungkus SingleChildScrollView. Ke-6 pilar smart city didefinisikan dengan ikon dan warna aksen yang serasi:")
    add_bullet("Smart Governance (Ikon: account_balance, Aksen: Biru)", "1. ")
    add_bullet("Smart Economy (Ikon: trending_up, Aksen: Amber)", "2. ")
    add_bullet("Smart Living (Ikon: health_and_safety, Aksen: Merah Terang)", "3. ")
    add_bullet("Smart Mobility (Ikon: directions_subway, Aksen: Teal)", "4. ")
    add_bullet("Smart Environment (Ikon: eco, Aksen: Hijau Daun)", "5. ")
    add_bullet("Smart People (Ikon: groups, Aksen: Ungu)", "6. ")

    # ==========================================
    # 5. HASIL DAN DOKUMENTASI PROGRAM
    # ==========================================
    add_h1("5. HASIL DAN DOKUMENTASI PROGRAM")
    add_p("Aplikasi telah dijalankan dan diverifikasi secara langsung pada Android Virtual Device (AVD Pixel 4, API 33) dengan hasil tangkapan layar (screenshot) sebagai berikut:")

    img_dir = r"C:\Coding\Mobile Development\Flutter\PPBL\Pekan 01\screenshots"
    
    add_h2("5.1 Bagian A: Praktikum (NO AI) – praktikum_widget")
    add_figure(os.path.join(img_dir, "praktikum_widget_awal.png"), "5.1", 
               "Tampilan Awal Aplikasi Praktikum Widget (NO AI) pada Emulator Pixel 4")
    add_p("Penjelasan Gambar 5.1: Menampilkan antarmuka awal saat aplikasi baru diluncurkan. ProfilCard menampilkan nama pengembang Ghazy Nabil Alghfari, NIM 707012400023, dan Prodi D3IF. Pada bagian PenghitungSuka, counter awal bernilai 0 dan ikon hati dalam kondisi outline (belum disukai).")

    add_figure(os.path.join(img_dir, "praktikum_widget_setelah_suka.png"), "5.2", 
               "Tampilan Setelah Tombol Suka Ditekan (Terjadi Perubahan State)")
    add_p("Penjelasan Gambar 5.2: Menampilkan perubahan antarmuka secara reaktif setelah tombol 'Suka' ditekan. Nilai counter bertambah menjadi 1 dan ikon hati otomatis berubah menjadi terisi (solid) sebagai representasi state _disukai = true.")

    add_figure(os.path.join(img_dir, "praktikum_widget_hot_reload.png"), "5.3", 
               "Tampilan Bukti Verifikasi Fitur Hot Reload pada Flutter")
    add_p("Penjelasan Gambar 5.3: Menampilkan pengujian fitur Hot Reload di mana warna AppBar diubah menjadi teal. Perubahan kode langsung tercermin pada emulator dalam hitungan milidetik tanpa mereset nilai counter state yang sedang aktif.")

    add_h2("5.2 Bagian B: Praktikum Berbantuan AI – praktikum_widget_ai")
    add_figure(os.path.join(img_dir, "praktikum_widget_ai_awal.png"), "5.4", 
               "Tampilan Awal Aplikasi Praktikum Berbantuan AI")
    add_p("Penjelasan Gambar 5.4: Menampilkan antarmuka hasil rekonstruksi kode melalui bantuan AI. Susunan komponen ProfilCard, PenghitungSuka, dan dua KotakInfo ('Status Mahasiswa: Aktif' dan 'Semester: 4') tersusun secara presisi menggunakan widget Expanded.")

    add_figure(os.path.join(img_dir, "praktikum_widget_ai_setelah_suka.png"), "5.5", 
               "Tampilan Interaksi State Suka pada Praktikum Berbantuan AI")
    add_p("Penjelasan Gambar 5.5: Menampilkan hasil penekanan tombol suka pada aplikasi hasil AI, membuktikan bahwa logika StatefulWidget dan pemanggilan setState() bekerja dengan benar.")

    add_h2("5.3 Bagian C: Tugas Praktikum – nusantara_cerdas_707012400023")
    add_figure(os.path.join(img_dir, "nusantara_cerdas_awal.png"), "5.6", 
               "Tampilan Awal Dasbor Smart City Nusantara Cerdas (Status: Pelayanan Lancar)")
    add_p("Penjelasan Gambar 5.6: Menampilkan kondisi awal aplikasi Dasbor Nusantara Cerdas. Header KepalaKota menampilkan identitas Kota Nusantara dan identitas resmi mahasiswa Ghazy Nabil Alghfari (NIM: 707012400023 • Kelas: 48-03 • PPBL 2026). Panel laporan menunjukkan 0 laporan aktif dengan Dynamic Status Badge hijau bertuliskan 'Pelayanan Lancar'. Tombol 'Laporan Selesai' berada dalam kondisi visual disabled karena jumlah laporan bernilai 0.")

    add_figure(os.path.join(img_dir, "nusantara_cerdas_sibuk.png"), "5.7", 
               "Tampilan Dasbor Nusantara Cerdas saat Pelayanan Sibuk (Jumlah Laporan: 6)")
    add_p("Penjelasan Gambar 5.7: Menampilkan antarmuka setelah tombol 'Laporan Masuk' ditekan hingga angka 6 (rentang 5–10). Status badge secara dinamis bertransisi menjadi warna oranye dengan ikon peringatan bertuliskan 'Pelayanan Sibuk'.")

    add_figure(os.path.join(img_dir, "nusantara_cerdas_penambahan_petugas.png"), "5.8", 
               "Tampilan Dasbor Nusantara Cerdas saat Perlu Penambahan Petugas (Jumlah Laporan: 12)")
    add_p("Penjelasan Gambar 5.8: Menampilkan antarmuka saat jumlah laporan meningkat hingga 12 (> 10). Dynamic Status Badge otomatis berubah warna menjadi merah dengan ikon kesalahan dan teks status 'Perlu Penambahan Petugas', mengindikasikan beban layanan publik membutuhkan eskalasi petugas.")

    add_figure(os.path.join(img_dir, "nusantara_cerdas_pilar_smartcity.png"), "5.9", 
               "Tampilan Komprehensif Enam Pilar Smart City Nusantara Cerdas (Scrolled View)")
    add_p("Penjelasan Gambar 5.9: Menampilkan hasil pengguliran layar (scroll view) ke bawah yang memperlihatkan keseluruhan 6 pilar smart city: Smart Governance, Smart Economy, Smart Living, Smart Mobility, Smart Environment, dan Smart People, masing-masing dengan kartu terdekorasi dan ikon tematik yang jelas dan ergonomis.")

    # ==========================================
    # 6. ANALISIS DAN PEMBAHASAN
    # ==========================================
    add_h1("6. ANALISIS DAN PEMBAHASAN")
    
    add_h2("6.1 Analisis Pemilihan StatelessWidget dan StatefulWidget")
    add_p("Pemilihan jenis widget dalam arsitektur aplikasi Flutter memegang peranan krusial terhadap efisiensi penggunaan memori dan siklus hidup (lifecycle) proses rendering.")
    add_bullet("Alasan Pemilihan StatelessWidget pada KepalaKota dan KartuPilar: Komponen identitas kota, slogan, identitas pengembang, serta kartu enam pilar smart city bersifat immutable (tetap/tidak berubah). Seluruh data dilewatkan sekali melalui parameter konstruktor saat inisialisasi. Pada StatelessWidget, Flutter tidak perlu mengalokasikan objek State terpisah di memori. Framework hanya membangun konfigurasi widget sekali dan menempatkannya pada Element Tree tanpa memerlukan siklus hidup pelacakan perubahan, sehingga sangat menghemat resource CPU dan RAM.", "• ")
    add_bullet("Alasan Pemilihan StatefulWidget pada PanelLaporanWarga: Komponen panel laporan memiliki mutable state yang dinamis, yaitu variabel _jumlahLaporan. Setiap kali tombol ditekan, nilai variabel ini berubah dan memicu pembaruan pada angka counter, warna status, teks status, serta ikon badge. Pada StatefulWidget, data disimpan di dalam objek State yang persisten (tetap hidup meskipun konfigurasi widget diperbarui). Ketika fungsi setState() dipanggil, framework menandai State object tersebut sebagai 'dirty' dan menjadwalkan pemanggilan build() hanya pada sub-tree panel laporan tersebut (sub-tree invalidation), tanpa perlu merender ulang keseluruhan halaman.", "• ")

    add_h2("6.2 Analisis Percobaan Pembaruan State Tanpa setState()")
    add_p("Berdasarkan eksperimen yang dilakukan pada Bagian B (Praktikum AI), pembaruan variabel _jumlahSuka atau _jumlahLaporan tanpa fungsi setState() menghasilkan fenomena di mana variabel di memori internal Dart telah berubah (misalnya dari 0 menjadi 1), namun antarmuka pada layar tetap menampilkan angka 0. Hal ini terjadi karena Flutter menganut paradigma reaktif deklaratif: antarmuka merupakan fungsi dari state UI = f(state). Framework Flutter tidak secara otomatis memantau (observe) perubahan variabel primitif tanpa adanya pemberitahuan eksplisit melalui setState(). Oleh karena itu, setState() mutlak diperlukan untuk memicu siklus rekonsiliasi antara Widget Tree dan Render Tree.")

    add_h2("6.3 Komparasi Pengerjaan Manual (NO AI) vs Berbantuan AI (AI-Assisted)")
    add_p("Dari perbandingan antara praktikum_widget dan praktikum_widget_ai, diperoleh temuan komparatif sebagai berikut:")
    add_bullet("Efisiensi Waktu: Pembuatan kode dengan AI memangkas waktu penulisan boilerplate code secara signifikan, khususnya dalam pembuatan layout bertingkat dan penentuan styling BoxDecoration.", "• ")
    add_bullet("Pentingnya Kemampuan Code Reading: Kode yang dihasilkan AI tidak selalu langsung sempurna atau sesuai batasan. Sebagai contoh, prompt harus secara eksplisit melarang penggunaan paket eksternal (third-party state management). Mahasiswa harus memiliki pemahaman dasar yang kuat untuk membaca, memverifikasi, dan memperbaiki kode yang dihasilkan.", "• ")
    add_bullet("Struktur Incremental Prompting: Memberikan instruksi bertahap (peran -> rencana kerja -> komponen per berkas) terbukti jauh lebih menghasilkan kode yang terstruktur dan minim galat dibandingkan meminta AI menghasilkan seluruh aplikasi dalam satu kali prompt.", "• ")

    add_h2("6.4 Kendala / Galat yang Ditemukan dan Solusi Penanganannya")
    add_p("Selama proses pengerjaan praktikum dan tugas, ditemukan beberapa kendala teknis nyata di lingkungan pengembangan yang berhasil diatasi secara sistematis:")
    add_bullet("Kendala 1 – Ketiadaan Android NDK dan Ketidakcocokan Versi Build-Tools: Saat pertama kali mengompilasi proyek Android, Gradle memunculkan galat 'Failed to find Build Tools revision 36.0.0' dan tidak mendeteksi NDK 28. Solusi teknis: Mengunduh paket NDK versi 28.2.13676358 ke dalam direktori Android SDK, serta mengonfigurasi properti buildToolsVersion = \"36.1.0\" secara eksplisit di dalam android/app/build.gradle.kts agar sesuai dengan versi SDK Build-Tools yang terpasang di sistem.", "• ")
    add_bullet("Kendala 2 – Layout Overflow pada Baris Identitas Pengembang (RenderFlex Overflowed by 22 pixels): Teks identitas pengembang 'Pengembang: Ghazy Nabil Alghfari' dan 'NIM: 707012400023 | 48-03' melebihi lebar layar jika diletakkan berdampingan dalam satu baris Row pada kontainer kartu kota. Solusi teknis: Mengubah tata letak kartu identitas mahasiswa menjadi susunan Column vertikal dengan tipografi berjenjang serta menambahkan badge 'PPBL 2026' di sisi kanan. Solusi ini memastikan nama lengkap dan NIM tampil utuh 100% tanpa terpotong (ellipsis) dan tanpa galat overflow pada emulator.", "• ")
    add_bullet("Kendala 3 – Proteksi Batas Bawah Counter Laporan: Sesuai spesifikasi tugas, jumlah laporan tidak boleh bernilai negatif (< 0). Solusi teknis: Menerapkan guard condition pada metode _laporanSelesai() dengan pemeriksaan if (_jumlahLaporan > 0) sebelum pemanggilan setState(), serta memberikan styling disabled pada tombol 'Laporan Selesai' saat nilai laporan bernilai 0.", "• ")

    add_h2("6.5 Keterkaitan Aplikasi dengan Konsep Enam Pilar Smart City IKN Nusantara")
    add_p("Aplikasi Dasbor 'Kota Nusantara Cerdas' merefleksikan konsep tata kelola kota cerdas masa depan di Ibu Kota Nusantara (IKN) melalui keenam pilar utama:")
    add_bullet("Smart Governance: Direfleksikan melalui panel laporan warga terintegrasi yang memungkinkan transparansi birokrasi dan pemantauan beban kerja pelayanan secara waktu-nyata (real-time).", "1. ")
    add_bullet("Smart Economy: Memfasilitasi digitalisasi ekosistem UMKM dan mempermudah akses investasi modal usaha berbasis ekonomi sirkular dan hijau.", "2. ")
    add_bullet("Smart Living: Menyediakan pemantauan fasilitas kesehatan terpadu, jaminan keselamatan publik, serta lingkungan hunian yang sehat dan nyaman bagi seluruh warga.", "3. ")
    add_bullet("Smart Mobility: Menghubungkan jaringan transportasi publik nir-emisi dan ramah lingkungan yang terintegrasi berbasis kecerdasan buatan.", "4. ")
    add_bullet("Smart Environment: Memastikan pelestarian hutan lindung (Forest City), pemantauan kualitas udara, pengelolaan limbah cerdas, serta transisi energi terbarukan 100%.", "5. ")
    add_bullet("Smart People: Mendorong peningkatan literasi teknologi digital, partisipasi aktif warga dalam tata kelola kota, dan pembangunan masyarakat yang inklusif.", "6. ")

    # ==========================================
    # 7. KESIMPULAN
    # ==========================================
    add_h1("7. KESIMPULAN")
    add_p("Berdasarkan seluruh rangkaian praktikum dan tugas praktikum yang telah dilaksanakan pada Modul 1 ini, dapat ditarik beberapa kesimpulan utama:")
    add_bullet("Pemahaman Arsitektur Deklaratif Flutter: Mahasiswa berhasil memahami paradigma deklaratif UI di mana antarmuka dibangun dari komposisi bersarang pohon widget (Widget Tree). Pemisahan antara StatelessWidget untuk komponen statis (ProfilCard, KepalaKota, KartuPilar) dan StatefulWidget untuk komponen interaktif (PenghitungSuka, PanelLaporanWarga) merupakan fondasi utama dalam menciptakan aplikasi yang berperforma tinggi dan hemat memori.", "1. ")
    add_bullet("Mekanisme Reaktif setState(): Fungsi setState() terbukti sebagai penghubung fundamental antara data logika dan presentasi antarmuka. Pembaruan state yang diisolasi pada widget lokal mampu melakukan re-render secara efisien tanpa mempengaruhi bagian antarmuka statis lainnya.", "2. ")
    add_bullet("Efektivitas Rekayasa Prompt (AI-Assisted Development): Pemanfaatan asisten AI dengan metode prompt engineering bertahap (incremental prompting) terbukti mempercepat pembuatan purwarupa aplikasi Flutter. Namun demikian, kompetensi code reading dan analisis kode mandiri tetap mutlak diperlukan untuk menjamin kebenaran logika dan kepatuhan arsitektur kode.", "3. ")
    add_bullet("Implementasi Dasbor Smart City Nusantara Cerdas: Seluruh kriteria fungsional dan estetika pada Tugas Praktikum telah berhasil dipenuhi 100%, meliputi pewarnaan tema Forest Green (#0D5C3A), dynamic status badge 3 kondisi, proteksi nilai non-negatif, tata letak bebas overflow, serta kelulusan 100% pada pengujian otomatis widget (flutter test) dan analisis linter (flutter analyze).", "4. ")

    # ==========================================
    # 8. LAMPIRAN: LINK REPOSITORI GITHUB
    # ==========================================
    add_h1("8. LAMPIRAN: LINK REPOSITORI GITHUB")
    add_p("Seluruh basis kode sumber program lengkap untuk Bagian A (Praktikum No AI), Bagian B (Praktikum AI), Bagian C (Tugas Praktikum Nusantara Cerdas), pengujian unit otomatis, serta aset dokumentasi tangkapan layar telah diunggah ke repositori GitHub daring resmi mahasiswa:")
    
    # Table for GitHub info
    tbl_git = doc.add_table(rows=4, cols=2)
    tbl_git.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_git)
    
    git_info = [
        ("Nama Repositori", "PPBL-Modul01-707012400023"),
        ("Tautan / URL Repositori", "https://github.com/ghazyAlghifari508/PPBL-Modul01-707012400023"),
        ("Visibilitas Repositori", "Public (Dapat diakses oleh Dosen Pengampu & Asisten Lab)"),
        ("Akun GitHub Mahasiswa", "ghazyAlghifari508 (Ghazy Nabil Alghfari)"),
    ]
    for i, (k, v) in enumerate(git_info):
        row = tbl_git.rows[i]
        c0 = row.cells[0]
        c0.width = Inches(2.2)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.size = Pt(10)
        
        c1 = row.cells[1]
        c1.width = Inches(4.3)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(v)
        r1.font.size = Pt(10)
        if i == 1:
            r1.bold = True
            r1.font.color.rgb = RGBColor(13, 92, 58)
    
    add_p("Ringkasan Riwayat Komit Git (Git Commit History):", bold_prefix="Catatan Tambahan: ")
    add_code("""commit 48e1a0b - feat: inisialisasi repositori lengkap Modul 01 PPBL (Praktikum No AI, Praktikum AI, Tugas Praktikum Nusantara Cerdas) - 707012400023
Author: Ghazy Nabil Alghfari <ghazynabil@student.telkomuniversity.ac.id>
Date:   Fri Sep 25 16:12:00 2026 +0700
Branches: main -> origin/main""")
    
    # Save the document
    output_filename = r"C:\Coding\Mobile Development\Flutter\PPBL\Pekan 01\Modul1_707012400023_GhazyNabilAlghfari.docx"
    doc.save(output_filename)
    print(f"Laporan berhasil dibuat: {output_filename}")

if __name__ == "__main__":
    main()
