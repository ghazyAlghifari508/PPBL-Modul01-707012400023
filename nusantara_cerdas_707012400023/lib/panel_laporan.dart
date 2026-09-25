import 'package:flutter/material.dart';

class PanelLaporanWarga extends StatefulWidget {
  const PanelLaporanWarga({super.key});

  @override
  State<PanelLaporanWarga> createState() => _PanelLaporanWargaState();
}

class _PanelLaporanWargaState extends State<PanelLaporanWarga> {
  int _jumlahLaporan = 0;

  // Logika penambahan laporan (+1)
  void _laporanMasuk() {
    setState(() {
      _jumlahLaporan++;
    });
  }

  // Logika pengurangan laporan (-1, tidak boleh kurang dari 0)
  void _laporanSelesai() {
    if (_jumlahLaporan > 0) {
      setState(() {
        _jumlahLaporan--;
      });
    }
  }

  // Logika reset ke 0
  void _resetHarian() {
    setState(() {
      _jumlahLaporan = 0;
    });
  }

  // Mendapatkan status teks pelayanan
  String get _statusPelayanan {
    if (_jumlahLaporan < 5) {
      return 'Pelayanan Lancar';
    } else if (_jumlahLaporan <= 10) {
      return 'Pelayanan Sibuk';
    } else {
      return 'Perlu Penambahan Petugas';
    }
  }

  // Mendapatkan warna indikator status
  Color get _warnaStatus {
    if (_jumlahLaporan < 5) {
      return Colors.green.shade600;
    } else if (_jumlahLaporan <= 10) {
      return Colors.orange.shade700;
    } else {
      return Colors.red.shade700;
    }
  }

  // Mendapatkan ikon indikator status
  IconData get _ikonStatus {
    if (_jumlahLaporan < 5) {
      return Icons.check_circle_rounded;
    } else if (_jumlahLaporan <= 10) {
      return Icons.warning_amber_rounded;
    } else {
      return Icons.error_outline_rounded;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 3,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
      ),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            Row(
              children: [
                const Icon(Icons.assignment_outlined, color: Colors.blueGrey),
                const SizedBox(width: 8),
                const Expanded(
                  child: Text(
                    'Panel Laporan Warga',
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                TextButton.icon(
                  onPressed: _resetHarian,
                  icon: const Icon(Icons.refresh, size: 16),
                  label: const Text('Reset Harian'),
                  style: TextButton.styleFrom(
                    foregroundColor: Colors.blueGrey,
                    visualDensity: VisualDensity.compact,
                    padding: const EdgeInsets.symmetric(horizontal: 4),
                  ),
                ),
              ],
            ),
            const Divider(height: 20),
            // Tampilan Angka Penghitung
            Text(
              '$_jumlahLaporan',
              style: TextStyle(
                fontSize: 48,
                fontWeight: FontWeight.bold,
                color: Theme.of(context).colorScheme.primary,
              ),
            ),
            const Text(
              'Total Laporan Aktif Hari Ini',
              style: TextStyle(fontSize: 13, color: Colors.black54),
            ),
            const SizedBox(height: 12),
            // Badge Status Pelayanan
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
              decoration: BoxDecoration(
                color: _warnaStatus.withValues(alpha: 0.12),
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: _warnaStatus, width: 1.2),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(_ikonStatus, size: 18, color: _warnaStatus),
                  const SizedBox(width: 6),
                  Text(
                    _statusPelayanan,
                    style: TextStyle(
                      fontSize: 13,
                      fontWeight: FontWeight.w600,
                      color: _warnaStatus,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 18),
            // Tombol Kontrol
            Row(
              children: [
                Expanded(
                  child: ElevatedButton.icon(
                    onPressed: _laporanMasuk,
                    icon: const Icon(Icons.add),
                    label: const Text('Laporan Masuk'),
                    style: ElevatedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(vertical: 12),
                      backgroundColor: Theme.of(context).colorScheme.primary,
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: OutlinedButton.icon(
                    onPressed: _jumlahLaporan > 0 ? _laporanSelesai : null,
                    icon: const Icon(Icons.done_all),
                    label: const Text('Laporan Selesai'),
                    style: OutlinedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(vertical: 12),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                      ),
                    ),
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
