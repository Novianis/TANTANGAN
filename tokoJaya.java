package Java;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

class Product {
    String name;
    double price;
    int stock;

    public Product(String name, double price, int stock) {
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    public void displayProduct() {
        System.out.printf("%-15s | %-10.2f | %-5d\n", name, price, stock);
    }
}

public class tokoJaya {
    private static ArrayList<Product> products = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        initializeProducts();
        int choice;
        do {
            System.out.println("\nSelamat datang di Toko JAYA :D");
            System.out.println("\n--- Toko Sembako ---");
            System.out.println("1. Tampilkan Produk");
            System.out.println("2. Tambah Produk");
            System.out.println("3. Hapus Produk");
            System.out.println("4. Beli Produk");
            System.out.println("5. Keluar");
            System.out.print("Pilih menu: ");
            choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1 -> displayProducts();
                case 2 -> addProduct();
                case 3 -> removeProduct();
                case 4 -> buyProduct();
                case 5 -> System.out.println("Terima kasih telah berbelanja di Toko JAYA!");
                default -> System.out.println("Pilihan tidak valid!");
            }
        } while (choice != 5);
    }

    private static void initializeProducts() {
        products.add(new Product("Beras", 12000, 20));
        products.add(new Product("Gula", 15000, 15));
        products.add(new Product("Minyak", 14000, 10));
    }

    private static void displayProducts() {
        System.out.println("\nDaftar Produk:");
        System.out.printf("%-15s | %-10s | %-5s\n", "Nama", "Harga", "Stok");
        System.out.println("------------------------------------");
        for (Product product : products) {
            product.displayProduct();
        }
    }

    private static void addProduct() {
        System.out.print("Masukkan nama produk: ");
        String name = scanner.nextLine();
        System.out.print("Masukkan harga produk: ");
        double price = scanner.nextDouble();
        System.out.print("Masukkan stok produk: ");
        int stock = scanner.nextInt();
        scanner.nextLine();
        products.add(new Product(name, price, stock));
        System.out.println("Produk berhasil ditambahkan!");
    }

    private static void removeProduct() {
        displayProducts();
        System.out.print("Masukkan nomor produk yang ingin dihapus: ");
        int index = scanner.nextInt() - 1;
        if (index >= 0 && index < products.size()) {
            products.remove(index);
            System.out.println("Produk berhasil dihapus!");
        } else {
            System.out.println("Produk tidak ditemukan!");
        }
    }

    private static void buyProduct() {
        ArrayList<String> receipt = new ArrayList<>();
        int totalItemsBought = 0;
        double totalPriceBought = 0;

        while (true) {
            displayProducts();
            System.out.print("Masukkan nomor produk yang ingin dibeli: ");
            int index = scanner.nextInt() - 1;

            if (index >= 0 && index < products.size()) {
                Product product = products.get(index);
                System.out.print("Masukkan jumlah yang ingin dibeli: ");
                int quantity = scanner.nextInt();

                if (quantity <= product.stock) {
                    product.stock -= quantity;
                    double totalPrice = quantity * product.price;

                    totalItemsBought += quantity;
                    totalPriceBought += totalPrice;

                    receipt.add(String.format("%-15s %-5d %-10.2f %-10.2f", product.name, quantity, product.price, totalPrice));
                } else {
                    System.out.println("Stok tidak mencukupi!");
                }
            } else {
                System.out.println("Produk tidak ditemukan!");
            }

            System.out.print("Apakah Anda ingin membeli produk lain? (ya/tidak): ");
            scanner.nextLine();
            String answer = scanner.nextLine().trim().toLowerCase();

            if (!answer.equals("ya")) {
                break;
            }
        }

        // Input pembayaran setelah semua barang selesai dipilih
        System.out.println("Total belanja Anda: " + totalPriceBought);
        double pembayaran;
        do {
            System.out.print("Masukkan uang pembayaran: ");
            pembayaran = scanner.nextDouble();
            if (pembayaran < totalPriceBought) {
                System.out.println("Uang Anda kurang! Harap masukkan jumlah yang cukup.");
            }
        } while (pembayaran < totalPriceBought);

        // Menghitung potongan harga dan kembalian
        double potongan = totalPriceBought > 50000 ? 2700 : 0;
        double totalBayar = totalPriceBought - potongan;
        double kembali = pembayaran - totalBayar;

        // Menampilkan struk pembelian

    String DateTime = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());

        System.out.println("\n========== STRUK PEMBELIAN ==========");
        System.out.println("               TOKO JAYA              ");
        System.out.println("       Jl. BENGAWAN SOLO, Probolinggo ");
        System.out.println("=======================================");
        System.out.println("Dine In");
        System.out.println("Table MEJA             Guest 1");
        System.out.println("Date    : " + DateTime);
        System.out.println("Staff   : KASIR 1");
        System.out.printf("%-15s %-5s %-10s %-10s\n", "Nama Produk", "Jml", "Harga", "Total");
        System.out.println("----------------------------------------");
        for (String line : receipt) {
                System.out.println(line);
            }
        System.out.println("----------------------------------------");
        System.out.printf("Potongan:        Rp. %.2f\n", potongan);
        System.out.println("----------------------------------------");
        System.out.printf("Total:           Rp. %.2f\n", totalBayar);
        System.out.println("----------------------------------------");
        System.out.printf("Bayar:           Rp. %.2f\n", pembayaran);
        System.out.printf("Kembali:         Rp. %.2f\n", kembali);
        System.out.println("----------------------------------------");
        System.out.printf("Tot Item:        %d\n", totalItemsBought);
        System.out.println("Charge:          Rp. 0");
        System.out.println("----------------------------------------");
        System.out.println("BKP - Sudah termasuk PPN");
        System.out.println("Barang Tidak dapat Ditukar/Dikembalikan");
        System.out.println("========================================");
        System.out.println("Terima Kasih Atas Kunjungan Anda!");
        System.out.println("============ Sampai Jumpa! ============");
    }
}
