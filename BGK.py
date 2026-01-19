import random

# Menampilkan selamat datang
print("Selamat datang di permainan Batu, Gunting, Kertas!")
print("Pilihan Anda adalah:")
print("1. Batu")
print("2. Gunting")
print("3. Kertas")

# Fungsi utama permainan
def main():
    pilihan = ["Batu", "Gunting", "Kertas"]
    try:
        # Meminta pilihan pemain
        pemain = int(input("Masukkan pilihan Anda (1-3): "))
        if pemain < 1 or pemain > 3:
            print("Pilihan tidak valid. Masukkan angka 1, 2, atau 3.")
            return
        
        kamu = pilihan[pemain - 1]
        komputer = random.choice(pilihan)

        # Menampilkan pilihan
        print(f"Anda memilih: {kamu}")
        print(f"Komputer memilih: {komputer}")

        # Menentukan pemenang
        if kamu == komputer:
            print("Hasil: Seri!")
        elif (kamu == "Batu" and komputer == "Gunting") or \
             (kamu == "Gunting" and komputer == "Kertas") or\
             (kamu == "Kertas" and komputer == "Batu"):
            print("Hasil: Anda menang!")
        else:
            print("Hasil: Komputer menang!")
    except ValueError:
        print("Mohon masukkan angka yang valid.")

# Memulai permainan
if __name__ == "__main__":
    main()
