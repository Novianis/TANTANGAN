package Algoritma;

public class Tugas5 {

    public static void main(String[] args) {
        // Data array yang sudah diberikan
        int[] data = { 27, 80, 8, 46, 16, 12, 50 };

        // Proses pengurutan menggunakan Bubble Sort
        for (int i = 0; i < data.length - 1; i++) {
            for (int j = 0; j < data.length - 1 - i; j++) {
                if (data[j] > data[j + 1]) {
                    // Tukar elemen jika tidak urut
                    int temp = data[j];
                    data[j] = data[j + 1];
                    data[j + 1] = temp;
                }
            }
        }

        // Menampilkan array setelah diurutkan
        System.out.println("Deret data setelah diurutkan secara ascending:");
        for (int i = 0; i < data.length; i++) {
            System.out.print(data[i] + " ");
        }
    }
}
