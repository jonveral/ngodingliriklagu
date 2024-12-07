def menu():
    print("\n=== Program Matematika Sederhana ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

def penjumlahan():
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    print(f"Hasil penjumlahan: {a + b}")

def pengurangan():
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    print(f"Hasil pengurangan: {a - b}")

def perkalian():
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    print(f"Hasil perkalian: {a * b}")

def pembagian():
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    if b != 0:
        print(f"Hasil pembagian: {a / b}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")

while True:
    menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        penjumlahan()
    elif pilihan == "2":
        pengurangan()
    elif pilihan == "3":
        perkalian()
    elif pilihan == "4":
        pembagian()
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
