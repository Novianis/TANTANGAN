package Algoritma;

import java.util.Scanner;

public class Tugas2 {

    public static int hitungFaktorial(int n) {
        if (n == 0 || n == 1) {
            return 1; // Basis kasus: faktorial 0 atau 1 adalah 1
        } else {
            return n * hitungFaktorial(n - 1); // Rekursif: n * (n-1)!
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Input dari pengguna
        System.out.print("Masukkan angka yang ingin dihitung faktorialnya: ");
        int angka = input.nextInt();

        // Validasi input tidak negatif
        if (angka < 0) {
            System.out.println("Faktorial tidak didefinisikan untuk angka negatif.");
        } else {
            // Hitung dan tampilkan hasil
            int hasil = hitungFaktorial(angka);
            System.out.println("Hasil faktorial dari " + angka + " adalah " + hasil);
        }

        input.close();
    }
}
