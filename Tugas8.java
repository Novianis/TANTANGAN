package Algoritma;

import java.util.ArrayList;
import java.util.Scanner;

public class Tugas8 {

    // Method untuk melakukan selection sort descending
    public static void selectionSortDescending(ArrayList<Integer> data) {
        int n = data.size();

        for (int i = 0; i < n - 1; i++) {
            int maxIndex = i;

            // Cari elemen terbesar dari i hingga akhir list
            for (int j = i + 1; j < n; j++) {
                if (data.get(j) > data.get(maxIndex)) {
                    maxIndex = j;
                }
            }

            // Tukar elemen terbesar dengan posisi i
            int temp = data.get(i);
            data.set(i, data.get(maxIndex));
            data.set(maxIndex, temp);
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Input jumlah data
        System.out.print("Masukkan jumlah data: ");
        int jumlah = input.nextInt();

        // Buat ArrayList untuk menampung data
        ArrayList<Integer> dataList = new ArrayList<>();

        // Input nilai-nilai data
        System.out.println("Masukkan " + jumlah + " angka:");
        for (int i = 0; i < jumlah; i++) {
            System.out.print("Data ke-" + (i + 1) + ": ");
            int nilai = input.nextInt();
            dataList.add(nilai);
        }

        // Panggil method untuk mengurutkan secara descending
        selectionSortDescending(dataList);

        // Tampilkan hasil setelah diurutkan
        System.out.println("Data setelah diurutkan secara descending:");
        for (int nilai : dataList) {
            System.out.print(nilai + " ");
        }

        input.close();
    }
}
