# Menghitung Volume Kerucut

def vkerucut():
    phi = 3.14
    r = float(input("Masukkan jari-jari: "))
    t = float(input("Masukkan tinggi: "))

    s = (r ** 2 + t ** 2) ** 0.5  
    volume = (1/3) * phi * r ** 2 * t

    print(f"Volume kerucut: {volume:.2f}")

vkerucut()

# Menghitung Luas Permukaan Kerucut

def LPkerucut():
    phi = 3.14
    r = float(input("Masukkan jari-jari: "))
    t = float(input("Masukkan tinggi: "))
    
    s = (r ** 2 + t ** 2) ** 0.5
    luas = phi * r * (r + s)
    
    print(f"Luas permukaan kerucut: {luas:.2f}")

LPkerucut()

# Menghitung Luas Alas Kerucut

def LAkerucut():
    phi = 3.14 
    r = float(input("Masukkan jari-jari alas (r): "))

    luas_alas = phi * r ** 2
    
    print(f"Luas alas kerucut: {luas_alas:.2f}")

LAkerucut()

# Menghitung Luas Alas Kerucut

def GPkerucut():
    r = float(input("Masukkan jari-jari alas (r): "))
    t = float(input("Masukkan tinggi kerucut (t): "))
    
    s = (r ** 2 + t ** 2) ** 0.5
    
    print(f"Garis pelukis kerucut: {s:.2f}")

GPkerucut()

# Menghitung Luas Alas Kerucut

def LSkerucut():
    phi = 3.14  
    r = float(input("Masukkan jari-jari alas (r): "))
    t = float(input("Masukkan tinggi kerucut (t): "))
    
    s = (r ** 2 + t ** 2) ** 0.5
    
    luas_selimut = phi * r * s
    
    print(f"Luas selimut kerucut: {luas_selimut:.2f}")

LSkerucut()

# Menghitung Tinggi Kerucut
def Tkerucut():
    r = float(input("Masukkan jari-jari alas (r): "))
    s = float(input("Masukkan garis pelukis (s): "))
    
    if s > r:
        t = (s ** 2 - r ** 2) ** 0.5
        print(f"Tinggi kerucut: {t:.2f}")
    else:
        print("Garis pelukis harus lebih besar dari jari-jari.")

Tkerucut()

# Menghitung Jari Jari Kerucut

def Jkerucut():
    t = float(input("Masukkan tinggi kerucut (t): "))
    s = float(input("Masukkan garis pelukis (s): "))
    
    if s > t:
        r = (s ** 2 - t ** 2) ** 0.5
        print(f"Jari-jari alas kerucut: {r:.2f}")
    else:
        print("Garis pelukis harus lebih besar dari tinggi kerucut.")

Jkerucut()

# Menghitung Keliling Alas Kerucut

def KAkerucut():
    phi = 3.14
    r = float(input("Masukkan jari-jari alas (r): "))
    
    keliling = 2 * phi * r
    
    print(f"Keliling alas kerucut: {keliling:.2f}")

KAkerucut()

# Menghitung Sudut Puncak Kerucut

def SPkerucut():
    phi = 3.14
    r = float(input("Masukkan jari-jari alas (r): "))
    h = float(input("Masukkan tinggi kerucut (h): "))
    
    sudut = (r / h)
    print(f"Tan dari sudut puncak kerucut: {sudut:.2f}")

SPkerucut()

# Menghitung Sudut Alas Kerucut

def SAkerucut():
    r = float(input("Masukkan jari-jari alas (r): "))
    h = float(input("Masukkan tinggi kerucut (h): "))
    
    if r == 0:
        raise ValueError("Jari-jari tidak boleh nol.")

    tan_theta = h / r
    theta = 0
    increment = 0.0001
    
    while theta <= 90:
        if tan(theta) >= tan_theta:
            break
        theta += increment
    
    print(f'Sudut alas kerucut: {theta:.2f} derajat')

def tan(theta):
    return (theta * 3.14 / 180) 

SAkerucut()