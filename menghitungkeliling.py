import math

def menu():
    print("\n=== Program Keliling Bangun Datar ===")
    print("1. Keliling Persegi")
    print("2. Keliling Persegi Panjang")
    print("3. Keliling Segitiga")
    print("4. Keliling Trapesium")
    print("5. Keliling Lingkaran")
    print("6. Keluar")

def keliling_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    print(f"Keliling persegi: {4 * sisi}")

def keliling_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    print(f"Keliling persegi panjang: {2 * (panjang + lebar)}")

def keliling_segitiga():
    sisi1 = float(input("Masukkan panjang sisi pertama: "))
    sisi2 = float(input("Masukkan panjang sisi kedua: "))
    sisi3 = float(input("Masukkan panjang sisi ketiga: "))
    print(f"Keliling segitiga: {sisi1 + sisi2 + sisi3}")

def keliling_trapesium():
    sisi_atas = float(input("Masukkan panjang sisi atas: "))
    sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
    sisi_kiri = float(input("Masukkan panjang sisi kiri: "))
    sisi_kanan = float(input("Masukkan panjang sisi kanan: "))
    print(f"Keliling trapesium: {sisi_atas + sisi_bawah + sisi_kiri + sisi_kanan}")

def keliling_lingkaran():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    print(f"Keliling lingkaran: {2 * math.pi * jari_jari:.2f}")

while True:
    menu()
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        keliling_persegi()
    elif pilihan == "2":
        keliling_persegi_panjang()
    elif pilihan == "3":
        keliling_segitiga()
    elif pilihan == "4":
        keliling_trapesium()
    elif pilihan == "5":
        keliling_lingkaran()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
