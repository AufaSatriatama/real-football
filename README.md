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

# Catatan Tugas 8

## 1. 

### Navigator.push: digunakan untuk menavigasi ke halaman baru dengan menambahkan halaman baru ke tumpukan navigasi. Kalau Navigator.pushReplacement: digunakan untuk menavigasi ke halaman baru dengan menggantikan halaman saat ini di tumpukan navigasi. Kuncinya ada di 'mengganti' dan 'menambahkan'

## 2.

### Kita dapat memanfaatkan hirarki widget dengan menempatkan widget yang ingin kita akses di atas widget yang membutuhkan akses tersebut. Misalnya, jika kita ingin mengakses data dari widget A di widget B, kita bisa menempatkan widget A sebagai parent dari widget B. Dengan begitu, widget B dapat mengakses data dari widget A melalui BuildContext.

## 3.

### Kelebihan menggunakan Padding: 
- Memberikan ruang di sekitar widget, sehingga tampilan menjadi lebih rapi dan teratur.
- Mencegah widget saling bertumpukan atau terlalu berdekatan yang dapat mengganggu pengalaman pengguna.
- Memudahkan dalam mengatur layout dan posisi widget dalam tampilan.

### Kelebihan menggunakan SingleChildScrollView:
- Memungkinkan konten yang melebihi batas layar untuk di-scroll, sehingga semua konten dapat diakses oleh pengguna.
- Mudah digunakan untuk membuat tampilan yang responsif, terutama pada perangkat dengan ukuran layar yang berbeda-beda

## 4.

### Kita bisa menggunakan warna hijau karena sesuai dengan branding sebagai toko yang menjual jersey sepak bola

# Catatan Tugas 9

## 1

### Kita perlu membuat model dart saat mengambil atau mengirim data JSON karena dengan model dart kita bisa memastikan bahwa data yang kita terima atau kirim sesuai dengan struktur yang diharapkan.Jika kita langsung memetakan Map<String, dynamic> tanpa model, kita mungkin menghadapi masalah seperti kesulitan dalam validasi tipe, potensi null-safety issues, dan kesulitan dalam maintainability kode karena struktur data tidak jelas.

## 2

### Package http digunakan untuk melakukan permintaan HTTP (seperti GET, POST, PUT, DELETE) ke server dari aplikasi Flutter kayak di webdev sebelumnya. CookieRequest digunakan untuk mengelola sesi dan autentikasi dengan menyimpan dan mengirim cookie secara otomatis selama permintaan HTTP. Perbedaan kedua ini adalah http lebih fokus pada komunikasi HTTP umum (crud), sedangkan CookieRequest lebih fokus pada manajemen sesi dan autentikasi user menggunakan cookie.

## 3

### instance CookieRequest disebarkan ke semua komponen flutter agar semua widget dalam aplikasi dapat mengakses instance CookieRequest yang sama. Hal ini penting untuk menjaga konsistensi sesi dan autentikasi di seluruh aplikasi, sehingga user tidak perlu login berulang kali saat berpindah halaman atau melakukan permintaan HTTP.

## 4

### Agar django dapat berkomunikasi dengan flutter, kita perlu mengatur beberapa hal di sisi django:
- Mengaktifkan CORS (Cross-Origin Resource Sharing) agar aplikasi flutter dapat mengakses API django.
- Membuat endpoint API di django yang dapat diakses oleh aplikasi flutter.
- Menggunakan format data yang sesuai (seperti JSON) untuk pertukaran data antara django dan flutter.

### Kita perlu menambahkan 10.0.2.2 pada ALLOWED_HOSTS karena 10.0.2.2 adalah alamat IP yang digunakan oleh emulator Android untuk mengakses localhost di mesin host. Dengan menambahkannya ke ALLOWED_HOSTS, kita mengizinkan permintaan dari emulator ke server django yang berjalan di localhost. CORS dan pengaturan SameSite/cookie juga penting untuk memastikan bahwa permintaan dari aplikasi flutter diizinkan oleh server django (saat autentikasi). Izin akses android juga perlu diatur agar aplikasi flutter dapat melakukan permintaan jaringan. Jika tidak diatur, permintaan dari aplikasi flutter ke server django mungkin akan diblokir.

## 5

### Setelah user menginput, data dikirim ke django melalui endpoint API yang telah dibuat. Django kemudian memproses data tersebut, melakukan validasi, dan menyimpan data ke database jika valid. Setelah itu, django mengirimkan respons kembali ke aplikasi flutter, yang dapat berupa konfirmasi sukses atau pesan error jika ada masalah dengan data yang dikirimkan. setelah itu, data json kita olah agar lebih mudah dibaca oleh pengguna.

## 6

### Mekanisme login, register, dan logout pada aplikasi flutter dengan backend django menggunakan CookieRequest adalah sebagai berikut:
- Register: User mengisi formulir pendaftaran di aplikasi flutter. Data tersebut dikirim ke endpoint register di django. Django memproses data, membuat user baru, dan mengirimkan respons kembali ke flutter.
- Login: User mengisi formulir login di aplikasi flutter. Data login dikirim ke endpoint login di django. Jika kredensial valid, django mengirimkan cookie sesi kembali ke flutter melalui CookieRequest.
- Logout: Saat user memilih untuk logout, aplikasi flutter mengirimkan permintaan logout ke endpoint

### Saat sudah login, CookieRequest menyimpan cookie sesi yang diterima dari django. Pengguna kemudian dapat mengakses aplikasi.

## 7

### Cara implementasi setiap fitur yang ada di checklist

#### 1. Kita jalankan python manage.py runserver di terminal untuk menjalankan server django. Jika aman, kita bisa pastikan kalau django sudah berjalan di localhost:8000

#### 2. Kita buat fngsi register di flutter yang mengirim data user baru ke endpoint register di django. Setelah itu, kita buat form register di flutter yang memanggil fungsi register tersebut.

#### 3. Kita buat fungsi login di flutter yang mengirim data login user ke endpoint login di django. Setelah itu, kita buat form login di flutter yang memanggil fungsi login tersebut.

#### 4. mengintegrasikan antara django dan flutter di login / register bisa dilakukan dengan melakukan pemanggilan API dari flutter ke django.

#### 5. Kita buat model sesuai yang kita inginkan, setelah itu kita bisa menggunakan `https://app.quicktype.io/` untuk mengenerate model dart dari json yang kita dapat dari django.

#### 6. Kita bisa panggil semua data yang tersedia, lalu ditampilkan di listview.builder di flutter.

#### 7. Pertama tama, kita bikin dulu path yang menghubungkan produk dengan id tertentu, lalu di flutter kita buat fungsi yang memanggil endpoint tersebut dengan mengirimkan id produk yang diinginkan. Setelah itu, kita tampilkan detail produk di halaman baru.

#### 8. Di setiap model, ada atribut user yang dapat kita bandingkan dengan user yang sedang login. Jika sesuai, kita tampilkan produk yang ia telah olah.


