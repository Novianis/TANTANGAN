package Algoritma;

public class Tugas6 {

    public static void main(String[] args) {
        // Data array yang diberikan
        int[] data = { 27, 80, 8, 46, 16, 12, 50 };

        // Selection Sort dari kanan ke kiri
        for (int i = data.length - 1; i > 0; i--) {
            int minIndex = 0;

            // Cari indeks elemen terkecil dari 0 sampai i
            for (int j = 1; j <= i; j++) {
                if (data[j] < data[minIndex]) {
                    minIndex = j;
                }
            }

            // Tukar elemen terkecil dengan elemen di posisi i
            int temp = data[i];
            data[i] = data[minIndex];
            data[minIndex] = temp;
        }

        // Menampilkan hasil pengurutan
        System.out.println("Deret data setelah diurutkan secara ascending (kanan ke kiri):");
        for (int num : data) {
            System.out.print(num + " ");
        }
    }
}
