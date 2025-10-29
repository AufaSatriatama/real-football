# Catatan Tugas 7

## 1

### widget tree di flutter adalah konsep di mana sebuah widget (kayak div (yang jadi tempat untuk menaruh elemen lain)) meniru konsep tree: ada widget yang menjadi parent dan bisa memiliki anak (child widget). Hubungan bagaimana parent-child bekerja di widget tree ini sangat penting, karena menentukan bagaimana widget akan dirender dan berinteraksi satu sama lain.

## 2

### Widget-widget yang digunakan:
- MaterialApp: root dari aplikasi
- Scaffold: widget dasar yang menyediakan struktur layout dasar untuk aplikasi.
- AppBar: widget yang menampilkan bar di bagian atas layar.
- Card: widget yang menampilkan informasi dalam bentuk kartu.

## 3

### Fungsi dari widget MaterialApp: 
- Menyediakan struktur dasar untuk aplikasi Flutter.
- Mengatur tema dan gaya aplikasi secara keseluruhan.
- Mengelola routing dan navigasi antar halaman.

## 4

### Perbedaan Stateful widget dan Stateless widget:
- Stateless widget: widget yang tidak memiliki state yang berubah-ubah. Contohnya adalah Text, Icon, dll. Widget ini hanya menampilkan informasi statis.
- Stateful widget: widget yang memiliki state yang dapat berubah-ubah. Contohnya adalah Checkbox

## 5

### BuildContext adalah objek yang memberikan informasi tentang lokasi widget dalam widget tree. BuildContext digunakan untuk mengakses parent widget, tema, dan sumber daya lainnya yang terkait dengan widget tersebut. Dalam Build, kegunaannya adalah untuk membangun widget berdasarkan konteks di mana widget tersebut berada.

## 6

### Hot-reload merupakan konsep di mana perubahan pada suatu kode langsung diterapkan pada aplikasi yang sedang berjalan tanpa perlu memulai ulang aplikasi tersebut. Sedangkan, hot-restart adalah proses di mana aplikasi dimulai ulang dari awal. Perbedaannya adalah hot-reload hanya memperbarui bagian tertentu dari kode, sedangkan hot-restart memulai ulang seluruh aplikasi.