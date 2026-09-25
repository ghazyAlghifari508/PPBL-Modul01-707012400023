import 'package:flutter/material.dart';
import 'kepala_kota.dart';
import 'panel_laporan.dart';
import 'kartu_pilar.dart';

class HalamanUtama extends StatelessWidget {
  const HalamanUtama({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF4F7F6),
      appBar: AppBar(
        title: const Text(
          'Nusantara Cerdas',
          style: TextStyle(fontWeight: FontWeight.bold, letterSpacing: 0.5),
        ),
        backgroundColor: Theme.of(context).colorScheme.primary,
        foregroundColor: Colors.white,
        centerTitle: true,
        elevation: 2,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // 1. Identitas Program & Kota (Stateless)
            const KepalaKota(),
            const SizedBox(height: 16),

            // 2. Panel Laporan Warga Hari Berjalan (Stateful)
            const PanelLaporanWarga(),
            const SizedBox(height: 20),

            // 3. Header Seksi Pilar Smart City
            Row(
              children: [
                Container(
                  width: 4,
                  height: 20,
                  decoration: BoxDecoration(
                    color: Theme.of(context).colorScheme.primary,
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
                const SizedBox(width: 8),
                const Text(
                  'Enam Pilar Smart City',
                  style: TextStyle(
                    fontSize: 17,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 0.3,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 4),
            const Text(
              'Pemantauan indikator kemajuan pilar transformasi digital',
              style: TextStyle(fontSize: 12, color: Colors.black54),
            ),
            const SizedBox(height: 10),

            // 4. Daftar 6 Pilar Smart City (Stateless)
            const KartuPilar(
              namaPilar: 'Smart Governance',
              ikon: Icons.account_balance_rounded,
              deskripsiSingkat:
                  'Penyelenggaraan tata kelola birokrasi pemerintahan berbasis digital dan transparansi publik.',
              warnaAksen: Colors.blueAccent,
            ),
            const KartuPilar(
              namaPilar: 'Smart Economy',
              ikon: Icons.trending_up_rounded,
              deskripsiSingkat:
                  'Peningkatan ekosistem ekonomi digital, UMKM cerdas, dan kemudahan investasi modal usaha.',
              warnaAksen: Colors.orange,
            ),
            const KartuPilar(
              namaPilar: 'Smart Living',
              ikon: Icons.health_and_safety_rounded,
              deskripsiSingkat:
                  'Kualitas hidup warga yang sehat, aman, nyaman, dan terfasilitasi layanan kesehatan terpadu.',
              warnaAksen: Colors.redAccent,
            ),
            const KartuPilar(
              namaPilar: 'Smart Mobility',
              ikon: Icons.directions_subway_filled_rounded,
              deskripsiSingkat:
                  'Sistem transportasi publik terintegrasi, ramah lingkungan, dan mobilitas perkotaan cerdas.',
              warnaAksen: Colors.teal,
            ),
            const KartuPilar(
              namaPilar: 'Smart Environment',
              ikon: Icons.eco_rounded,
              deskripsiSingkat:
                  'Pengelolaan lingkungan hidup berkelanjutan, energi terbarukan, dan perlindungan ruang hijau kota.',
              warnaAksen: Colors.green,
            ),
            const KartuPilar(
              namaPilar: 'Smart People',
              ikon: Icons.groups_rounded,
              deskripsiSingkat:
                  'Pemberdayaan sumber daya manusia unggul, literasi teknologi tinggi, dan masyarakat inklusif.',
              warnaAksen: Colors.purple,
            ),
            const SizedBox(height: 16),
          ],
        ),
      ),
    );
  }
}
