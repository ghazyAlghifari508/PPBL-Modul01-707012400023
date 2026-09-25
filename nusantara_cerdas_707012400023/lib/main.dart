import 'package:flutter/material.dart';
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
          seedColor: const Color(0xFF0D5C3A), // Nuansa Hijau Hutan Nusantara Smart City
          primary: const Color(0xFF0D5C3A),
        ),
        scaffoldBackgroundColor: const Color(0xFFF4F7F6),
        fontFamily: 'Roboto',
      ),
      home: const HalamanUtama(),
    );
  }
}
