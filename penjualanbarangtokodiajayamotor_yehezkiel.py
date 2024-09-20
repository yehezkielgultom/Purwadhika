# Data barang awal
barang_dijual = [
    {'No': 1, 'Nama': 'Oli Rem', 'Stok': 120, 'Harga Beli': 12000, 'Harga Jual': 12000 * 1.2},
    {'No': 2, 'Nama': 'Oli Mesin 0,8L', 'Stok': 96, 'Harga Beli': 42000, 'Harga Jual': 42000 * 1.2},
    {'No': 3, 'Nama': 'Oli Mesin 1L', 'Stok': 72, 'Harga Beli': 48000, 'Harga Jual': 48000 * 1.2},
    {'No': 4, 'Nama': 'Oli Mesin Matic 0,8L', 'Stok': 96, 'Harga Beli': 48000, 'Harga Jual': 48000 * 1.2},
    {'No': 5, 'Nama': 'Oli Mesin Matic 1L', 'Stok': 48, 'Harga Beli': 54000, 'Harga Jual': 54000 * 1.2},
    {'No': 6, 'Nama': 'Oli Mesin Sport 1L', 'Stok': 60, 'Harga Beli': 112000, 'Harga Jual': 112000 * 1.2},
    {'No': 7, 'Nama': 'Ban Dalam', 'Stok': 36, 'Harga Beli': 34000, 'Harga Jual': 34000 * 1.2},
    {'No': 8, 'Nama': 'Ban Luar', 'Stok': 24, 'Harga Beli': 180000, 'Harga Jual': 180000 * 1.2},
    {'No': 9, 'Nama': 'Kampas Cakram', 'Stok': 60, 'Harga Beli': 26000, 'Harga Jual': 26000 * 1.2},
    {'No': 10, 'Nama': 'Kampas Tromol', 'Stok': 48, 'Harga Beli': 38000, 'Harga Jual': 38000 * 1.2},
]

# Data user default
users = {
    'admin': {'password': 'admin', 'role': 'penjual'},
    'yehezkiel': {'password': 'yehezkiel', 'role': 'pembeli'}
}
attempts = 5

# Variabel untuk menyimpan total keuntungan dari penjualan
total_keuntungan = 0

# Variabel untuk menyimpan keranjang belanja pembeli
keranjang = []

# Variabel untuk menyimpan barang yang telah di-checkout
barang_terjual = []

# Variabel untuk menyimpan riwayat transaksi
riwayat_transaksi = []

# Fungsi login
def login():
    global attempts, username  # Tambahkan 'username' sebagai variabel global
    while attempts > 0:
        username = input("\nMasukkan username: ")
        password = input("Masukkan password: ")
        
        if username in users and users[username]['password'] == password:
            print(f"Login berhasil. Selamat datang, {username}!")
            return users[username]['role']
        else:
            attempts -= 1
            print(f"Login gagal. Sisa percobaan: {attempts}")
    
    print("Terlalu banyak percobaan login gagal. Program berhenti.")
    exit()

# Fungsi register untuk pembeli
def register():
    while True:
        username = input("Masukkan username: ")
        if username in users:
            print("Username sudah ada. Silakan pilih username lain.")
        elif len(username) < 6:
            print("Username minimal harus 6 karakter.")
        else:
            break
    
    while True:
        password = input("Masukkan password: ")
        if len(password) < 6:
            print("Password minimal harus 6 karakter.")
        else:
            break
    
    users[username] = {'password': password, 'role': 'pembeli'}
    print("Registrasi berhasil! Silakan login.")

# Fungsi untuk menampilkan barang
def tampilkan_barang(role):
    print("\n")
    if role == 'pembeli':
        # Tampilan untuk pembeli tanpa harga beli
        print("="*54)
        print(f"{'No':<4} {'Nama Barang':<23} {'Stok':<11} {'Harga Jual':<15}")
        print("="*54)
        for barang in barang_dijual:
            print(f"{barang['No']:<4} {barang['Nama']:<24} {barang['Stok']:<11} Rp{int(barang['Harga Jual']):<16}")
    else:
        # Tampilan untuk penjual termasuk harga beli
        print("="*70)
        print(f"{'No':<4} {'Nama Barang':<24} {'Stok':<11} {'Harga Beli':<16} {'Harga Jual':<16}")
        print("="*70)
        for barang in barang_dijual:
            print(f"{barang['No']:<4} {barang['Nama']:<24} {barang['Stok']:<12} Rp{int(barang['Harga Beli']):<14} Rp{int(barang['Harga Jual']):<15}")

# Fungsi untuk menambahkan barang (penjual)
def tambah_barang():
    nama = input("Nama barang: ")
    while True:
        stok = int(input("Stok barang: "))
        if stok <= 0:
            print("Stok tidak boleh negatif atau nol.")
        else:
            break
    while True:
        harga_beli = int(input("Harga beli: "))
        if harga_beli <= 0:
            print("Harga beli tidak boleh negatif atau nol.")
        else:
            break
    harga_jual = harga_beli * 1.2
    no_baru = len(barang_dijual) + 1
    barang_dijual.append({'No': no_baru, 'Nama': nama, 'Stok': stok, 'Harga Beli': harga_beli, 'Harga Jual': harga_jual})
    print(f"{nama} berhasil ditambahkan.")

# Fungsi untuk merestok barang (penjual)
def restok_barang():
    no_barang = int(input("Masukkan nomor barang yang ingin di-restok: "))
    for barang in barang_dijual:
        if barang['No'] == no_barang:
            print(f"Barang dipilih: {barang['Nama']} (Stok saat ini: {barang['Stok']})")
            while True:
                jumlah_restok = int(input(f"Masukkan jumlah untuk restok {barang['Nama']}: "))
                if jumlah_restok <= 0:
                    print("Jumlah restok tidak boleh negatif atau nol.")
                else:
                    barang['Stok'] += jumlah_restok
                    print(f"Stok {barang['Nama']} berhasil ditambah. Stok sekarang: {barang['Stok']}")
                    break
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk mengubah barang (penjual)
def ubah_barang():
    no_barang = int(input("Masukkan nomor barang yang ingin diubah: "))
    for barang in barang_dijual:
        if barang['No'] == no_barang:
            barang['Nama'] = input("Nama barang baru: ")
            while True:
                stok_baru = int(input("Stok barang baru: "))
                if stok_baru <= 0:
                    print("Stok tidak boleh negatif atau nol.")
                else:
                    barang['Stok'] = stok_baru
                    break
            while True:
                harga_beli_baru = int(input("Harga beli baru: "))
                if harga_beli_baru <= 0:
                    print("Harga beli tidak boleh negatif atau nol.")
                else:
                    barang['Harga Beli'] = harga_beli_baru
                    barang['Harga Jual'] = harga_beli_baru * 1.2
                    break
            print(f"Barang nomor {no_barang} berhasil diubah.")
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk menghapus barang (penjual)
def hapus_barang():
    no_barang = int(input("Masukkan nomor barang yang ingin dihapus: "))
    for barang in barang_dijual:
        if barang['No'] == no_barang:
            barang_dijual.remove(barang)
            print(f"Barang nomor {no_barang} berhasil dihapus.")
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk menghitung keuntungan (penjual)
def hitung_keuntungan():
    if not barang_terjual:
        print("Belum ada barang yang di-checkout.")
        return
    
    print("\n=== Laporan Penjualan ===")
    print(f"{'Nama Barang':<20} {'Jumlah':<10} {'Harga Jual':<15} {'Keuntungan':<15}")
    print("="*60)
    
    for item in barang_terjual:
        print(f"{item['Nama']:<20} {item['Jumlah']:<10} Rp{int(item['Harga Jual']):<15} Rp{int(item['Keuntungan']):<15}")
    
    print(f"\nTotal keuntungan: Rp{int(total_keuntungan)}")

# Fungsi untuk memberikan saran restok dan notifikasi barang habis (penjual)
def saran_restock():
    print("\n=== Saran Restok dan Notifikasi Stok ===")
    barang_hampir_habis = []
    barang_habis = []

    for barang in barang_dijual:
        if barang['Stok'] == 0:
            barang_habis.append(barang)
        elif barang['Stok'] <= 12:
            barang_hampir_habis.append(barang)

    # Menampilkan notifikasi barang habis
    if barang_habis:
        print("\n=== Notifikasi Barang Habis ===")
        for barang in barang_habis:
            print(f"Barang {barang['Nama']} sudah habis. Silakan segera restok.")
    else:
        print("Tidak ada barang yang habis.")

    # Menampilkan saran restok untuk barang yang hampir habis
    if barang_hampir_habis:
        print("\n=== Barang yang Hampir Habis ===")
        for barang in barang_hampir_habis:
            print(f"{barang['Nama']} - Stok tersisa: {barang['Stok']}")
    else:
        print("Tidak ada barang yang hampir habis.")
            
# Fungsi untuk menampilkan riwayat transaksi (penjual)
def lihat_riwayat_transaksi_penjual():
    if not riwayat_transaksi:
        print("Belum ada transaksi yang dilakukan.")
        return

    print("\n=== Riwayat Transaksi ===")
    for transaksi in riwayat_transaksi:
        print(f"Pembeli: {transaksi['Pembeli']}")
        for item in transaksi['Barang']:
            print(f" - {item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(item['Harga Jual'])}")
        print(f"Total: Rp{int(transaksi['Total'])}")
        print("="*40)
        
# Fungsi untuk menambah barang ke keranjang (pembeli)
def tambah_ke_keranjang():
    tampilkan_barang('pembeli')
    no_barang = int(input("Masukkan nomor barang yang ingin dibeli: "))
    for barang in barang_dijual:
        if barang['No'] == no_barang:
            while True:
                jumlah = int(input("Masukkan jumlah barang yang ingin dibeli: "))
                if jumlah <= 0:
                    print("Jumlah barang tidak boleh negatif atau nol.")
                elif jumlah > barang['Stok']:
                    print(f"Stok tidak mencukupi. Stok saat ini: {barang['Stok']}.")
                else:
                    break
            keranjang.append({'No': no_barang, 'Nama': barang['Nama'], 'Jumlah': jumlah, 'Harga': barang['Harga Jual']})
            print(f"{barang['Nama']} sebanyak {jumlah} berhasil ditambahkan ke keranjang.")
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk mengubah atau menghapus barang dari keranjang (pembeli)
def ubah_atau_hapus_keranjang():
    if not keranjang:
        print("Keranjang Anda kosong.")
        return
    
    # Menampilkan barang di keranjang
    print("\n=== Keranjang Belanja ===")
    for index, item in enumerate(keranjang, 1):
        print(f"{index}. {item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(item['Jumlah'] * item['Harga'])}")
    
    try:
        pilihan = int(input("Masukkan nomor barang yang ingin diubah atau dihapus dari keranjang: "))
        if 1 <= pilihan <= len(keranjang):
            barang_dipilih = keranjang[pilihan - 1]
            print(f"Barang dipilih: {barang_dipilih['Nama']} (Jumlah: {barang_dipilih['Jumlah']})")

            # Cari stok asli dari barang yang dipilih
            barang_asli = next((b for b in barang_dijual if b['No'] == barang_dipilih['No']), None)
            if barang_asli:
                stok_tersedia = barang_asli['Stok']

                # Menanyakan apakah user ingin mengubah atau menghapus barang
                aksi = input("Apakah Anda ingin mengubah jumlah (u) atau menghapus barang (h)? (u/h): ").lower()

                if aksi == 'u':
                    while True:
                        jumlah_baru = int(input(f"Masukkan jumlah baru untuk {barang_dipilih['Nama']} (maksimal {stok_tersedia}): "))
                        if jumlah_baru <= 0:
                            print("Jumlah harus lebih dari 0.")
                        elif jumlah_baru > stok_tersedia:
                            print(f"Jumlah tidak boleh melebihi stok yang tersedia. Stok saat ini: {stok_tersedia}.")
                        else:
                            barang_dipilih['Jumlah'] = jumlah_baru
                            print(f"Jumlah {barang_dipilih['Nama']} berhasil diubah menjadi {jumlah_baru}.")
                            break
                elif aksi == 'h':
                    keranjang.pop(pilihan - 1)
                    print(f"Barang {barang_dipilih['Nama']} berhasil dihapus dari keranjang.")
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Barang tidak ditemukan dalam daftar stok.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Input tidak valid, silakan masukkan nomor yang benar.")

# Fungsi untuk melihat keranjang belanja (pembeli)
def lihat_keranjang():
    if not keranjang:
        print("Keranjang kosong.")
        return
    print("\n=== Keranjang Belanja ===")
    total_harga = 0
    for item in keranjang:
        print(f"{item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(item['Jumlah'] * item['Harga'])}")
        total_harga += item['Jumlah'] * item['Harga']
    print(f"Total harga: Rp{int(total_harga)}")

# Fungsi checkout (pembeli)
def checkout():
    global total_keuntungan
    if not keranjang:
        print("Keranjang belanja Anda kosong.")
        return

    total_harga = 0
    total_item = 0
    transaksi = {'Pembeli': username, 'Barang': [], 'Total': 0}

    # Tampilkan detail barang yang akan di-checkout dalam format tabel
    print("\n=== Detail Barang yang Akan Di-checkout ===")
    print(f"{'No':<3} {'Nama Barang':<17} {'Jumlah':<9} {'Harga Satuan':<18} {'Total':<14} {'Diskon':<9} {'Harga Akhir':<15}")
    print("="*90)

    for idx, item in enumerate(keranjang, 1):
        barang = next((b for b in barang_dijual if b['No'] == item['No']), None)
        
        if barang and barang['Stok'] >= item['Jumlah']:
            harga_total_item = item['Jumlah'] * barang['Harga Jual']
            harga_setelah_diskon = harga_total_item
            diskon = 0

            # Hitung diskon jika jumlah barang lebih dari 12
            if item['Jumlah'] > 12:
                diskon = harga_total_item * 0.1
                harga_setelah_diskon = harga_total_item - diskon

            total_harga += harga_setelah_diskon
            total_item += item['Jumlah']
            
            print(f"{idx:<3} {barang['Nama']:<19} {item['Jumlah']:<8} Rp{int(barang['Harga Jual']):<14} Rp{int(harga_total_item):<12} Rp{int(diskon):<8} Rp{int(harga_setelah_diskon):<14}")
            
            # Hitung keuntungan
            keuntungan_per_item = (barang['Harga Jual'] - barang['Harga Beli']) * item['Jumlah']
            total_keuntungan += keuntungan_per_item

            # Simpan barang yang di-checkout dalam transaksi
            transaksi['Barang'].append({
                'Nama': barang['Nama'],
                'Jumlah': item['Jumlah'],
                'Harga Jual': barang['Harga Jual'],
                'Diskon': diskon
            })

    print("="*90)
    print(f"{'Total barang     :'} {total_item}")
    print(f"{'Total harga akhir:'} Rp{int(total_harga)}")
    
    
    # Konfirmasi sebelum melanjutkan checkout
    konfirmasi = input("Apakah Anda yakin ingin melanjutkan checkout? (y/n): ").lower()
    if konfirmasi != 'y':
        print("Checkout dibatalkan.")
        return

    # Jika konfirmasi yes, update stok dan simpan transaksi
    for item in keranjang:
        barang = next((b for b in barang_dijual if b['No'] == item['No']), None)
        if barang:
            barang['Stok'] -= item['Jumlah']

    # Menyimpan total harga dalam transaksi
    transaksi['Total'] = total_harga
    riwayat_transaksi.append(transaksi)

    print(f"Total belanja Anda adalah: Rp{int(total_harga)}")
    keranjang.clear()  # Kosongkan keranjang setelah checkout
    
# Fungsi untuk menampilkan riwayat transaksi (pembeli)
def lihat_riwayat_transaksi_pembeli():
    transaksi_pembeli = [transaksi for transaksi in riwayat_transaksi if transaksi['Pembeli'] == username]
    
    if not transaksi_pembeli:
        print("Anda belum melakukan transaksi.")
        return
    
    print("\n=== Riwayat Pembelian ===")
    for transaksi in transaksi_pembeli:
        for item in transaksi['Barang']:
            print(f" - {item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(item['Harga Jual'])}")
        print(f"Total: Rp{int(transaksi['Total'])}")
        print("="*40)

# Fungsi untuk role penjual
def menu_penjual():
    while True:
        print("\nMenu Penjual:")
        print("1. Tampilkan Barang")
        print("2. Tambah Barang Baru")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Hitung Keuntungan")
        print("6. Saran Restok")
        print("7. Restok Barang")
        print("8. Lihat Riwayat Transaksi")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_barang('penjual')
        elif pilihan == '2':
            tambah_barang()
        elif pilihan == '3':
            ubah_barang()
        elif pilihan == '4':
            hapus_barang()
        elif pilihan == '5':
            hitung_keuntungan()
        elif pilihan == '6':
            saran_restock()
        elif pilihan == '7':
            restok_barang() 
        elif pilihan == '8':
            lihat_riwayat_transaksi_penjual()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi untuk role pembeli
def menu_pembeli():
    while True:
        print("\nMenu Pembeli:")
        print("1. Tampilkan Barang")
        print("2. Tambah Barang ke Keranjang")
        print("3. Ubah atau Hapus Barang di Keranjang")
        print("4. Lihat Keranjang")
        print("5. Checkout")
        print("6. Lihat Riwayat Pembelian")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_barang('pembeli')
        elif pilihan == '2':
            tambah_ke_keranjang()
        elif pilihan == '3':
            ubah_atau_hapus_keranjang()
        elif pilihan == '4':
            lihat_keranjang()
        elif pilihan == '5':
            checkout()
        elif pilihan == '6':
            lihat_riwayat_transaksi_pembeli()  # Melihat riwayat pembelian
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid.")

# Program utama
def main():
    print("\nSelamat datang di Toko Dia Jaya Motor!")
    while True:
        print("\n1. Login")
        print("2. Register")
        print("0. Keluar")
        pilihan = input("\nPilih menu: ")
        
        if pilihan == '1':
            role = login()
            if role == 'penjual':
                menu_penjual()
            elif role == 'pembeli':
                menu_pembeli()
        elif pilihan == '2':
            register()
        elif pilihan == '0':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()