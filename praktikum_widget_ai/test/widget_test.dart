import 'package:flutter_test/flutter_test.dart';
import 'package:praktikum_widget_ai/main.dart';

void main() {
  testWidgets('Memeriksa render HalamanUtama dan interaksi Suka', (WidgetTester tester) async {
    await tester.pumpWidget(const MyApp());

    // Memastikan judul dan identitas awal tampil
    expect(find.text('Praktikum Widget Flutter'), findsOneWidget);
    expect(find.text('Ghazy Nabil Alghfari'), findsOneWidget);
    expect(find.text('Jumlah Suka: 0'), findsOneWidget);

    // Menekan tombol Suka
    await tester.tap(find.text('Suka'));
    await tester.pump();

    // Verifikasi penambahan jumlah suka
    expect(find.text('Jumlah Suka: 1'), findsOneWidget);

    // Menekan tombol Reset
    await tester.tap(find.text('Reset'));
    await tester.pump();

    // Verifikasi kembali ke 0
    expect(find.text('Jumlah Suka: 0'), findsOneWidget);
  });
}
