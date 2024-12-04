import math

def akar_persamaan_linear(a, b):
    if a == 0:
        return "Tidak ada solusi (bukan persamaan linear)" if b != 0 else "Tak terhingga (identitas)"
    return -b / a

def akar_persamaan_kuadrat(a, b, c):
    if a == 0:
        return akar_persamaan_linear(b, c)
    diskriminan = b**2 - 4*a*c
    if diskriminan < 0:
        return "Tidak ada akar real"
    elif diskriminan == 0:
        return -b / (2 * a)
    else:
        akar1 = (-b + math.sqrt(diskriminan)) / (2 * a)
        akar2 = (-b - math.sqrt(diskriminan)) / (2 * a)
        return akar1, akar2

def akar_persamaan_kubik(a, b, c, d):
    if a == 0:
        return akar_persamaan_kuadrat(b, c, d)
    def f(x):
        return a*x**3 + b*x**2 + c*x + d
    
    x1, x2 = -1e3, 1e3  # Rentang pencarian akar
    while abs(x2 - x1) > 1e-6:
        x_mid = (x1 + x2) / 2
        if f(x1) * f(x_mid) < 0:
            x2 = x_mid
        else:
            x1 = x_mid
    return x1

def main():
    print("Pilih jenis persamaan:")
    print("1. Linear (ax + b = 0)")
    print("2. Kuadrat (ax^2 + bx + c = 0)")
    print("3. Kubik (ax^3 + bx^2 + cx + d = 0)")
    
    pilihan = int(input("Masukkan pilihan (1/2/3): "))
    
    if pilihan == 1:
        print("Persamaan Linear (ax + b = 0)")
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        print(f"Persamaan yang dibuat: ({'' if a == 1 else a}x) + ({b}) = 0")
        hasil = akar_persamaan_linear(a, b)
    elif pilihan == 2:
        print("Persamaan Kuadrat (ax^2 + bx + c = 0)")
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))
        print(f"Persamaan yang dibuat: {'' if a == 1 else a}x^2 + ({'' if b == 1 else b}x) + ({c}) = 0")
        hasil = akar_persamaan_kuadrat(a, b, c)
    elif pilihan == 3:
        print("Persamaan Kubik (ax^3 + bx^2 + cx + d = 0)")
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))
        d = float(input("Masukkan nilai d: "))
        print(f"Persamaan yang dibuat: {'' if a == 1 else a}x^3 + ({'' if b == 1 else b}x^2) + ({'' if c == 1 else c}x) + ({d}) = 0")
        hasil = akar_persamaan_kubik(a, b, c, d)
    else:
        print("Pilihan tidak valid.")
        return
    
    print(f"Hasil akar: x = {hasil}")

if __name__ == "__main__":
    main()
