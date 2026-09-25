import 'package:flutter/material.dart';

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
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
      ),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            Text(
              'Jumlah Suka: $_jumlahSuka',
              style: const TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w600,
              ),
            ),
            const SizedBox(height: 12),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton.icon(
                  onPressed: _tambahSuka,
                  icon: Icon(
                    _disukai ? Icons.favorite : Icons.favorite_border,
                  ),
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
}
