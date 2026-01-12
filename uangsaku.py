# Program Manajemen Uang Saku
# Dibuat untuk membantu pelajar mengatur keuangan

print("=== PROGRAM MANAJEMEN UANG SAKU ===")

uang_saku = float(input("Masukkan uang saku kamu (Rp): "))
pengeluaran = []

while True:
    print("\n1. Tambah pengeluaran")
    print("2. Lihat total pengeluaran")
    print("3. Lihat sisa uang")
    print("4. Rekomendasi menabung")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Nama pengeluaran: ")
        jumlah = float(input("Jumlah (Rp): "))
        pengeluaran.append(jumlah)
        print("Pengeluaran berhasil ditambahkan.")

    elif pilihan == "2":
        total = sum(pengeluaran)
        print(f"Total pengeluaran: Rp {total}")

    elif pilihan == "3":
        total = sum(pengeluaran)
        sisa = uang_saku - total
        print(f"Sisa uang kamu: Rp {sisa}")

    elif pilihan == "4":
        total = sum(pengeluaran)
        sisa = uang_saku - total
        tabungan = sisa * 0.2
        print(f"Disarankan menabung: Rp {tabungan}")

    elif pilihan == "5":
        print("Terima kasih sudah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid!")
