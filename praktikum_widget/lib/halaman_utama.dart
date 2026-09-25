import 'package:flutter/material.dart';
import 'profil_card.dart';
import 'penghitung_suka.dart';

class HalamanUtama extends StatelessWidget {
  const HalamanUtama({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF2F4F8),
      appBar: AppBar(
        title: const Text('Praktikum Widget Flutter'),
        backgroundColor: Colors.teal,
        foregroundColor: Colors.white,
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const ProfilCard(
              nama: 'Ghazy Nabil Alghfari',
              nim: '707012400023',
              prodi: 'D4 Sistem Informasi Kota Cerdas (D4SIKC)',
            ),
            const SizedBox(height: 20),
            const Text(
              'Statistik Interaksi',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            const PenghitungSuka(),
            const SizedBox(height: 20),
            Row(
              children: const [
                Expanded(
                  child: KotakInfo(
                    judul: 'Widget',
                    nilai: '3',
                    warna: Colors.indigo,
                  ),
                ),
                SizedBox(width: 12),
                Expanded(
                  child: KotakInfo(
                    judul: 'Berkas',
                    nilai: '4',
                    warna: Colors.teal,
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class KotakInfo extends StatelessWidget {
  const KotakInfo({
    super.key,
    required this.judul,
    required this.nilai,
    required this.warna,
  });

  final String judul;
  final String nilai;
  final Color warna;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 20),
      alignment: Alignment.center,
      decoration: BoxDecoration(
        color: warna.withOpacity(0.1),
        border: Border.all(color: warna),
        borderRadius: BorderRadius.circular(10),
      ),
      child: Column(
        children: [
          Text(
            nilai,
            style: TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
              color: warna,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            judul,
            style: TextStyle(fontSize: 13, color: warna),
          ),
        ],
      ),
    );
  }
}
