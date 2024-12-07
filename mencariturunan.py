import sympy as sp

def menu():
    print("\n=== Program Mencari Turunan ===")
    print("1. Turunan Fungsi")
    print("2. Keluar")

def hitung_turunan():
    # Mendefinisikan simbol x
    x = sp.symbols('x')
    
    # Meminta input dari pengguna untuk fungsi
    fungsi = input("Masukkan fungsi dalam bentuk ekspresi (contoh: x**2 + 3*x + 2): ")
    
    # Mengubah string menjadi ekspresi matematika
    fungsi = sp.sympify(fungsi)
    
    # Menghitung turunan dari fungsi
    turunan = sp.diff(fungsi, x)
    
    print(f"Turunan dari fungsi {fungsi} adalah: {turunan}")

while True:
    menu()
    pilihan = input("Pilih menu (1-2): ")

    if pilihan == "1":
        hitung_turunan()
    elif pilihan == "2":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
