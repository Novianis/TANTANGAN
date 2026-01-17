# Fungsi untuk setiap operasi matematika
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

# Fungsi utama
def main():
    while True:
        # Menampilkan menu
        print("\n=== Kalkulator Sederhana ===")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Keluar")
        
        # Meminta pilihan dari pengguna
        pilihan = int(input("Masukkan pilihan Anda (1-5): "))

        if pilihan == 5:  # Keluar dari program
            print("Terima kasih telah menggunakan kalkulator!")
            break
        
        # Meminta dua angka dari pengguna
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        # Melakukan operasi sesuai pilihan
        if pilihan == 1:
            print(f"Hasil: {tambah(angka1, angka2)}")
        elif pilihan == 2:
            print(f"Hasil: {kurang(angka1, angka2)}")
        elif pilihan == 3:
            print(f"Hasil: {kali(angka1, angka2)}")
        elif pilihan == 4:
            if angka2 != 0:  # Pastikan tidak membagi dengan nol
                print(f"Hasil: {bagi(angka1, angka2)}")
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Menjalankan program
main()
