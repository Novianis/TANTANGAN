import Phyton.Identitas as Identitas
def isi_identitas():
    print("Silakan isi identitas diri Anda:")
    
    nama = input("Nama: ")
    umur = input("Umur: ")
    alamat = input("Alamat: ")
    pekerjaan = input("Pekerjaan: ")
    
    # Menampilkan informasi yang telah dimasukkan
    print("\nIdentitas Diri Anda:")
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
    print(f"Alamat: {alamat}")
    print(f"Pekerjaan: {pekerjaan}")

# Menjalankan fungsi
isi_identitas()
