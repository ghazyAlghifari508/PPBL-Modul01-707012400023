import 'package:flutter_test/flutter_test.dart';
import 'package:nusantara_cerdas_707012400023/main.dart';

void main() {
  testWidgets('Uji Dasbor Smart City Nusantara Cerdas dan Panel Laporan', (WidgetTester tester) async {
    await tester.pumpWidget(const NusantaraCerdasApp());

    // 1. Verifikasi Elemen Statis
    expect(find.text('Nusantara Cerdas'), findsOneWidget);
    expect(find.text('Kota Nusantara'), findsOneWidget);
    expect(find.text('Smart Governance'), findsOneWidget);
    expect(find.text('Smart Economy'), findsOneWidget);
    expect(find.text('Smart Living'), findsOneWidget);
    expect(find.text('Smart Mobility'), findsOneWidget);
    expect(find.text('Smart Environment'), findsOneWidget);
    expect(find.text('Smart People'), findsOneWidget);

    // 2. Verifikasi State Awal Panel Laporan
    expect(find.text('0'), findsOneWidget);
    expect(find.text('Pelayanan Lancar'), findsOneWidget);

    // 3. Uji Tombol Laporan Masuk (+1 per tap) hingga 5 (Status: Pelayanan Sibuk)
    for (int i = 0; i < 5; i++) {
      await tester.tap(find.text('Laporan Masuk'));
      await tester.pump();
    }
    expect(find.text('5'), findsOneWidget);
    expect(find.text('Pelayanan Sibuk'), findsOneWidget);

    // 4. Tambah hingga 11 laporan (> 10 -> Status: Perlu Penambahan Petugas)
    for (int i = 0; i < 6; i++) {
      await tester.tap(find.text('Laporan Masuk'));
      await tester.pump();
    }
    expect(find.text('11'), findsOneWidget);
    expect(find.text('Perlu Penambahan Petugas'), findsOneWidget);

    // 5. Uji Tombol Laporan Selesai (-1) kembali ke rentang 5-10
    await tester.tap(find.text('Laporan Selesai'));
    await tester.pump();
    expect(find.text('10'), findsOneWidget);
    expect(find.text('Pelayanan Sibuk'), findsOneWidget);

    // 6. Uji Tombol Reset Harian
    await tester.tap(find.text('Reset Harian'));
    await tester.pump();
    expect(find.text('0'), findsOneWidget);
    expect(find.text('Pelayanan Lancar'), findsOneWidget);
  });
}
