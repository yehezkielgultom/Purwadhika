Toko Dia Jaya Motor - Sistem Penjualan
Deskripsi

Sistem penjualan ini dibuat untuk mendukung aktivitas penjualan dan pembelian di Toko Dia Jaya Motor. Aplikasi ini mendukung dua peran, yaitu Penjual dan Pembeli. Penjual dapat mengelola barang, menambah, mengubah, menghapus, merestok barang, serta melihat keuntungan dan riwayat transaksi. Pembeli dapat melakukan pembelian barang, melihat keranjang, melakukan checkout, serta melihat riwayat pembelian mereka.
Fitur Utama

    Penjual:
        Menambahkan barang baru
        Mengubah data barang
        Menghapus barang
        Merestok barang
        Menghitung keuntungan dari barang yang terjual
        Menampilkan saran restok untuk barang yang hampir habis
        Melihat riwayat transaksi
    Pembeli:
        Melihat daftar barang
        Menambahkan barang ke keranjang
        Mengubah atau menghapus barang dari keranjang
        Melihat keranjang belanja
        Checkout pembelian dengan fitur diskon 10% jika pembelian barang lebih dari 12 unit per barang
        Melihat riwayat pembelian

Struktur Program

Program ini menggunakan beberapa variabel global untuk menyimpan data barang, user, keranjang belanja, dan transaksi. Fitur login digunakan untuk membedakan akses antara penjual dan pembeli. Setiap user memiliki username dan password yang harus diinput saat login.
Data Barang

Data barang disimpan dalam bentuk list yang berisi dictionary. Setiap dictionary merepresentasikan satu barang dengan informasi seperti:

    No: Nomor barang
    Nama: Nama barang
    Stok: Jumlah stok barang yang tersedia
    Harga Beli: Harga beli barang
    Harga Jual: Harga jual barang

Perhitungan Diskon dan Keuntungan

    Diskon: Diberikan diskon 10% untuk setiap barang yang dibeli lebih dari 12 unit.
    Keuntungan: Dihitung berdasarkan selisih harga jual dan harga beli (modal). Setelah diskon diterapkan, keuntungan dihitung pada harga yang sudah didiskon.

Alur Program

    Login: User login menggunakan username dan password. Program akan mengecek apakah user adalah penjual atau pembeli dan memberikan akses sesuai role.
    Penjual:
        Menambah atau mengubah barang yang dijual.
        Mengelola stok barang.
        Menghitung keuntungan berdasarkan barang yang sudah dibeli oleh pembeli.
        Melihat saran restok jika stok barang sudah hampir habis.
    Pembeli:
        Memilih barang dan menambahkannya ke keranjang.
        Melakukan checkout dan menerima diskon jika memenuhi syarat.
        Melihat riwayat transaksi pembelian.

Penghitungan Keuntungan

Keuntungan dihitung dengan formula:

    Keuntungan per barang: (Harga Jual - Harga Beli) * Jumlah Barang
    Total Uang Masuk (Kotor): Total uang yang didapatkan dari pembelian barang (setelah diskon, jika ada).
    Total Modal (Harga Beli): Total harga beli dari semua barang yang terjual.
    Total Keuntungan (Bersih): Total keuntungan bersih dari penjualan barang (Uang Masuk - Modal).

Cara Menggunakan Program

    Jalankan program dengan membuka file Python (.py) pada terminal atau IDE.
    Login sebagai admin (penjual) atau pembeli.
        Username default pembeli: yehezkiel
        Password default pembeli: yehezkiel
    Gunakan menu yang ada untuk mengelola barang atau melakukan pembelian sesuai role user.
    Setelah checkout dilakukan oleh pembeli, penjual dapat melihat laporan keuntungan dari penjualan.
