package Algoritma;

import java.util.Scanner;

public class Tugas4 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Input jumlah deret
        System.out.print("Masukkan jumlah deret: ");
        int jumlah = input.nextInt();

        int nilai = 3; // nilai awal
        int tambah = 2; // nilai yang akan ditambahkan setiap langkah

        System.out.println("Deret angka:");
        for (int i = 0; i < jumlah; i++) {
            System.out.print(nilai + " ");
            nilai += tambah;
            tambah++; // nilai tambah bertambah 1 setiap iterasi
        }

        input.close();
    }
}
