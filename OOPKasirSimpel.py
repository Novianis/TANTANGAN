class Makanan:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.jumlah = 0
        self.pedas_keterangan = "tidak pedas"

    def pilih_pedas(self):
        pedas = input(f"Apakah Anda Ingin {self.nama} Yang Pedas? (ya/tidak): ").lower()
        if pedas == 'ya':
            self.pilih_level_pedas()
        else:
            self.pedas_keterangan = "tidak pedas"

    def pilih_level_pedas(self):
        level = input("Pilih Level Kepedasan (1/2/3): ")
        if level in ['1', '2', '3']:
            self.pedas_keterangan = f"Level {level}"
        else:
            print("Level Tidak Valid. Memilih Level ! Secara Otomatis.")
            self.pedas_keterangan = "Level 1"

    def masukkan_jumalah_pesanan(self):
        self.jumlah = int(input(f"Berapa {self.nama} Yang Dipesan? "))

    def hitung_total(self):
        return self.harga * self.jumlah
    
    def tampilkan_pesanan(self):
        print(f"Pesanan Anda: {self.jumlah} {self.nama} {self.pedas_keterangan}")
        print(f"Total Harga Yang Harus Dibayar Adalah Rp. {self.hitung_total():,}")

class Menu:
    def __init__(self):
        self.daftar_menu = {
            "1": Makanan("Nasi Goreng", 15000),
            "2": Makanan("Mie Goreng", 12000),
            "3": Makanan("Capjay", 18000),
        }

    def tampilkan_menu(self):
        print("Pilih Menu Makanan: ")
        for key, makanan in self.daftar_menu.items():
            print(f"{key}. {makanan.nama} (Rp. {makanan.harga:,})")

    def pilih_makanan(self):
        pilihan = input("Masukkan Pilihan Makanan (1/2/3): ")
        if pilihan in self.daftar_menu:
            makanan = self.daftar_menu[pilihan]
            makanan.pilih_pedas()
            makanan.masukkan_jumalah_pesanan()
            makanan.tampilkan_pesanan()
        else:
            print("Pilihan Tidak Valid, Silahkan Coba lagi.")

def main():
        menu = Menu()
        menu.tampilkan_menu()
        menu.pilih_makanan()

if __name__ == "__main__":
    main()