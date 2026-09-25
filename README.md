# Pemrograman Perangkat Bergerak Lanjut (PPBL) - Modul 01

**Pengenalan Flutter, Widget Tree, dan Dasar Manajemen State**

---

## 👤 Identitas Mahasiswa
* **Nama:** Ghazy Nabil Alghfari
* **NIM:** 707012400023
* **Kelas:** D3IF 48-03
* **Program Studi:** D3 Rekayasa Perangkat Lunak Aplikasi (RPLA)
* **Fakultas:** Fakultas Ilmu Terapan (FIT)
* **Institusi:** Universitas Telkom
* **Tahun Akademik:** Semester Genap 2025/2026

---

## 📁 Struktur Direktori Repositori

```text
Pekan 01/
├── praktikum_widget/                  # A. Praktikum (NO AI)
│   ├── lib/
│   │   ├── main.dart
│   │   ├── greeting_card.dart         # StatelessWidget
│   │   └── counter_card.dart          # StatefulWidget
│   └── test/
│       └── widget_test.dart
├── praktikum_widget_ai/               # B. Praktikum Berbantuan AI
│   ├── lib/
│   │   ├── main.dart
│   │   ├── greeting_card.dart         # StatelessWidget
│   │   └── counter_card.dart          # StatefulWidget
│   └── test/
│       └── widget_test.dart
├── nusantara_cerdas_707012400023/     # C. Tugas Praktikum (Smart City Nusantara)
│   ├── lib/
│   │   ├── main.dart
│   │   ├── halaman_utama.dart         # Scaffold & SingleChildScrollView
│   │   ├── kepala_kota.dart           # StatelessWidget Identitas Kota & Mahasiswa
│   │   ├── kartu_pilar.dart           # StatelessWidget 6 Pilar Smart City
│   │   └── panel_laporan.dart         # StatefulWidget Counter & Dynamic Status Badge
│   └── test/
│       └── widget_test.dart
├── screenshots/                       # Bukti Tangkapan Layar Eksekusi Emulator
└── README.md
```

---

## 🚀 Ringkasan Proyek

### A. Praktikum (NO AI) - `praktikum_widget`
* Implementasi konsep dasar Flutter dengan membuat `StatelessWidget` (`GreetingCard`) dan `StatefulWidget` (`CounterCard`).
* Memahami siklus hidup widget, mekanisme `setState()`, serta interaksi penambahan jumlah "Suka" / counter.

### B. Praktikum (AI) - `praktikum_widget_ai`
* Membangun ulang aplikasi widget dengan teknik *prompt engineering* bertahap menggunakan bantuan AI.
* Menganalisis efektivitas, perbandingan kode, dan akurasi implementasi widget tree berbasis instruksi prompt terstruktur.

### C. Tugas Praktikum - `nusantara_cerdas_707012400023`
* Dasbor interaktif pilar *smart city* Kota Nusantara Cerdas dengan arsitektur modular:
  * **Header Kota & Pengembang:** Memuat identitas Kota Nusantara dan identitas resmi mahasiswa (Ghazy Nabil Alghfari, 707012400023, 48-03).
  * **Panel Laporan Warga:** Mengelola laporan warga harian secara reaktif:
    * Tombol *Laporan Masuk* (menambah laporan).
    * Tombol *Laporan Selesai* (mengurangi laporan dengan proteksi batas non-negatif $\ge 0$).
    * Tombol *Reset Harian* (mengembalikan nilai ke 0).
    * **Dynamic Status Badge**:
      * `< 5`: Pelayanan Lancar (Hijau)
      * `5 - 10`: Pelayanan Sibuk (Oranye)
      * `> 10`: Perlu Penambahan Petugas (Merah)
  * **Enam Pilar Smart City:** Smart Governance, Smart Economy, Smart Living, Smart Mobility, Smart Environment, dan Smart People.

---

## 📸 Tangkapan Layar Eksekusi

Semua tangkapan layar eksekusi tersimpan lengkap di dalam folder [`screenshots/`](./screenshots/).

---

## 🛠️ Cara Menjalankan Aplikasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/ghazyAlghifari508/PPBL-Modul01-707012400023.git
   cd PPBL-Modul01-707012400023
   ```
2. Pilih proyek yang ingin dijalankan (misal Tugas Praktikum):
   ```bash
   cd nusantara_cerdas_707012400023
   flutter pub get
   flutter run
   ```
3. Menjalankan pengujian otomatis:
   ```bash
   flutter test
   ```
