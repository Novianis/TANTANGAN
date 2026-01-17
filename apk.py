import json

def tampilkan_k3lh():
    print("\n[PANDUAN KESELAMATAN - K3LH]")
    print("- Gunakan aplikasi dengan jujur dan bertanggung jawab.")
    print("- Jangan mencantumkan informasi sensitif secara sembarangan.")
    print("- Jika menemukan barang berbahaya, segera laporkan ke pihak berwenang.\n")

class Laporan:
    def __init__(self, nama_barang, lokasi, deskripsi):
        self.nama_barang = nama_barang
        self.lokasi = lokasi
        self.deskripsi = deskripsi

    def to_dict(self):
        return {
            "nama_barang": self.nama_barang,
            "lokasi": self.lokasi,
            "deskripsi": self.deskripsi
        }

class LaporanHilang(Laporan):
    def __init__(self, nama_barang, lokasi, deskripsi, kontak):
        super().__init__(nama_barang, lokasi, deskripsi)
        self.kontak = kontak

    def to_dict(self):
        data = super().to_dict()
        data["tipe"] = "hilang"
        data["kontak"] = self.kontak
        return data

class LaporanDitemukan(Laporan):
    def __init__(self, nama_barang, lokasi, deskripsi, penemu_nama, penemu_kelas):
        super().__init__(nama_barang, lokasi, deskripsi)
        self.penemu_nama = penemu_nama
        self.penemu_kelas = penemu_kelas
        self.status_diambil = False
        self.diambil_oleh = ""
        self.pesan = ""

    def tandai_diambil(self, diambil_oleh, pesan):
        self.status_diambil = True
        self.diambil_oleh = diambil_oleh
        self.pesan = pesan

    def to_dict(self):
        data = super().to_dict()
        data["tipe"] = "ditemukan"
        data["penemu_nama"] = self.penemu_nama
        data["penemu_kelas"] = self.penemu_kelas
        data["status_diambil"] = self.status_diambil
        data["diambil_oleh"] = self.diambil_oleh
        data["pesan"] = self.pesan
        return data

# fungsi json
def simpan_ke_file(data, filename="apalah.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def muat_dari_file(filename="apalah.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return []

# menu
def tambah_laporan_hilang(data):
    print("\n[Tambah Laporan Barang Hilang]")
    nama = input("Nama barang: ")
    lokasi = input("Lokasi hilang: ")
    deskripsi = input("Deskripsi barang: ")
    kontak = input("Kontak pelapor: ")
    laporan = LaporanHilang(nama, lokasi, deskripsi, kontak)
    data.append(laporan.to_dict())
    print("✅ Laporan barang hilang ditambahkan.")

def tambah_laporan_ditemukan(data):
    print("\n[Tambah Laporan Barang Ditemukan]")
    nama = input("Nama barang: ")
    lokasi = input("Lokasi ditemukan: ")
    deskripsi = input("Deskripsi barang: ")
    penemu_nama = input("Nama penemu: ")
    penemu_kelas = input("Kelas penemu: ")
    laporan = LaporanDitemukan(nama, lokasi, deskripsi, penemu_nama, penemu_kelas)
    data.append(laporan.to_dict())
    print("✅ Laporan barang ditemukan ditambahkan.")

def tampilkan_semua(data):
    print("\n[Semua Laporan]")
    if not data:
        print("Tidak ada laporan.")
        return
    for i, item in enumerate(data, 1):
        print(f"\n[{i}] {item['tipe'].upper()} - {item['nama_barang']}")
        print(f"Lokasi: {item['lokasi']}")
        print(f"Deskripsi: {item['deskripsi']}")
        if item["tipe"] == "hilang":
            print(f"Kontak: {item['kontak']}")
        elif item["tipe"] == "ditemukan":
            print(f"Penemu: {item['penemu_nama']} (Kelas {item['penemu_kelas']})")
            if item.get("status_diambil"):
                print(f"✅ Sudah diambil oleh: {item.get('diambil_oleh')}")
                print(f"📩 Pesan untuk penemu: {item.get('pesan')}")

def cari_barang(data):
    print("\n[Cari Barang]")
    kata_kunci = input("Masukkan nama barang yang dicari: ").lower()
    hasil = [item for item in data if kata_kunci in item['nama_barang'].lower()]
    if hasil:
        print(f"\nDitemukan {len(hasil)} hasil:")
        for item in hasil:
            print(f"- [{item['tipe']}] {item['nama_barang']} di {item['lokasi']}")
            if item['tipe'] == 'hilang':
                print(f"  Kontak: {item['kontak']}")
            elif item['tipe'] == 'ditemukan':
                print(f"  Penemu: {item['penemu_nama']} (Kelas {item['penemu_kelas']})")
                if item.get("status_diambil"):
                    print(f"  ✅ Sudah diambil oleh: {item['diambil_oleh']}")
                    print(f"  📩 Pesan: {item['pesan']}")
    else:
        print("❌ Barang tidak ditemukan.")

def pengambilan_barang(data):
    print("\n[Pengambilan Barang Ditemukan]")
    nama_dicari = input("Masukkan nama barang yang diambil: ").lower()
    ditemukan = False
    for item in data:
        if item["tipe"] == "ditemukan" and nama_dicari == item["nama_barang"].lower():
            if item.get("status_diambil"):
                print("⚠️ Barang ini sudah ditandai sebagai diambil.")
                return
            diambil_oleh = input("Nama pemilik yang mengambil: ")
            pesan = input("Pesan untuk penemu barang: ")
            item["status_diambil"] = True
            item["diambil_oleh"] = diambil_oleh
            item["pesan"] = pesan
            print("✅ Barang berhasil ditandai telah diambil.")
            ditemukan = True
            break
    if not ditemukan:
        print("❌ Barang ditemukan tidak ditemukan atau belum dilaporkan.")

def main():
    data = muat_dari_file()
    while True:
        print("\n=== APLIKASI PENEMUAN BARANG HILANG ===")
        print("1. Tambah laporan barang hilang")
        print("2. Tambah laporan barang ditemukan")
        print("3. Lihat semua laporan")
        print("4. Cari barang")
        print("5. Panduan K3LH")
        print("6. Catat pengambilan barang ditemukan")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_laporan_hilang(data)
        elif pilihan == "2":
            tambah_laporan_ditemukan(data)
        elif pilihan == "3":
            tampilkan_semua(data)
        elif pilihan == "4":
            cari_barang(data)
        elif pilihan == "5":
            tampilkan_k3lh()
        elif pilihan == "6":
            pengambilan_barang(data)
        elif pilihan == "0":
            simpan_ke_file(data)
            print("📁 Data disimpan. Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")

main()
