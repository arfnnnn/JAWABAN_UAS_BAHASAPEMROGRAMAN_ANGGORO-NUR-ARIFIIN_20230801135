class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Toko:
    def __init__(self):
        self.barang_list = []

    def tambah_barang(self, barang):
        self.barang_list.append(barang)

    def tampil_barang(self):
        for barang in self.barang_list:
            print(f"Nama: {barang.nama}, Harga: {barang.harga}, Stok: {barang.stok}")

    def hapus_barang(self, nama_barang):
        self.barang_list = [barang for barang in self.barang_list if barang.nama != nama_barang]

    def cari_barang(self, nama_barang):
        for barang in self.barang_list:
            if barang.nama == nama_barang:
                return barang
        return None

    def jual_barang(self, nama_barang, jumlah):
        barang = self.cari_barang(nama_barang)
        if barang:
            if barang.stok >= jumlah:
                barang.stok -= jumlah
                total_harga = barang.harga * jumlah
                print(f"Total harga: {total_harga}")
            else:
                print("Stok tidak mencukupi")
        else:
            print("Barang tidak ditemukan")

def main():
    toko = Toko()
    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Tampil Barang")
        print("3. Hapus Barang")
        print("4. Cari Barang")
        print("5. Jual Barang")
        print("6. Keluar")
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            nama = input("Masukkan nama barang: ")
            harga = int(input("Masukkan harga barang: "))
            stok = int(input("Masukkan stok barang: "))
            barang = Barang(nama, harga, stok)
            toko.tambah_barang(barang)
        elif pilihan == 2:
            toko.tampil_barang()
        elif pilihan == 3:
            nama = input("Masukkan nama barang yang akan dihapus: ")
            toko.hapus_barang(nama)
        elif pilihan == 4:
            nama = input("Masukkan nama barang yang dicari: ")
            barang = toko.cari_barang(nama)
            if barang:
                print(f"Nama: {barang.nama}, Harga: {barang.harga}, Stok: {barang.stok}")
            else:
                print("Barang tidak ditemukan")
        elif pilihan == 5:
            nama = input("Masukkan nama barang yang dijual: ")
            jumlah = int(input("Masukkan jumlah barang yang dijual: "))
            toko.jual_barang(nama, jumlah)
        elif pilihan == 6:
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
