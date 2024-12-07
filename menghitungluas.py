import math

def menu():
    print("\n=== Program Luas Bangun Datar ===")
    print("1. Luas Persegi")
    print("2. Luas Persegi Panjang")
    print("3. Luas Segitiga")
    print("4. Luas Trapesium")
    print("5. Luas Lingkaran")
    print("6. Keluar")

def luas_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    print(f"Luas persegi: {sisi**2}")

def luas_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    print(f"Luas persegi panjang: {panjang * lebar}")

def luas_segitiga():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    print(f"Luas segitiga: {0.5 * alas * tinggi}")

def luas_trapesium():
    sisi_atas = float(input("Masukkan panjang sisi atas: "))
    sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
    tinggi = float(input("Masukkan tinggi trapesium: "))
    luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    print(f"Luas trapesium: {luas:.2f}")

def luas_lingkaran():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    print(f"Luas lingkaran: {math.pi * jari_jari**2:.2f}")

while True:
    menu()
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        luas_persegi()
    elif pilihan == "2":
        luas_persegi_panjang()
    elif pilihan == "3":
        luas_segitiga()
    elif pilihan == "4":
        luas_trapesium()
    elif pilihan == "5":
        luas_lingkaran()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
