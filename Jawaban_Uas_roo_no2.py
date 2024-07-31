def luas_segiempat(sisi):
    return sisi ** 2

def keliling_segiempat(sisi):
    return 4 * sisi

def luas_persegipanjang(panjang, lebar):
    return panjang * lebar

def keliling_persegipanjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_lingkaran(radius):
    return 3.14 * radius ** 2

def keliling_lingkaran(radius):
    return 2 * 3.14 * radius

def menu():
    print("Pilih Bangun Datar:")
    print("1. Segi Empat")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    pilihan = int(input("Masukkan pilihan: "))
    return pilihan

def main():
    pilihan = menu()
    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi: "))
        print("Luas Segi Empat:", luas_segiempat(sisi))
        print("Keliling Segi Empat:", keliling_segiempat(sisi))
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        print("Luas Persegi Panjang:", luas_persegipanjang(panjang, lebar))
        print("Keliling Persegi Panjang:", keliling_persegipanjang(panjang, lebar))
    elif pilihan == 3:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi1 = float(input("Masukkan panjang sisi 1: "))
        sisi2 = float(input("Masukkan panjang sisi 2: "))
        sisi3 = float(input("Masukkan panjang sisi 3: "))
        print("Luas Segitiga:", luas_segitiga(alas, tinggi))
        print("Keliling Segitiga:", keliling_segitiga(sisi1, sisi2, sisi3))
    elif pilihan == 4:
        radius = float(input("Masukkan jari-jari: "))
        print("Luas Lingkaran:", luas_lingkaran(radius))
        print("Keliling Lingkaran:", keliling_lingkaran(radius))
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
