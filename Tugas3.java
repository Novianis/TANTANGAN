package Algoritma;

import java.util.Scanner;

public class Tugas3 {

    // Fungsi rekursif untuk menghitung bilangan Fibonacci ke-n
    public static int fibonacci(int n) {
        if (n == 0) {
            return 0; // Basis kasus pertama
        } else if (n == 1) {
            return 1; // Basis kasus kedua
        } else {
            return fibonacci(n - 1) + fibonacci(n - 2); // Rekursif
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Input dari pengguna
        System.out.print("Masukkan jumlah deret Fibonacci yang ingin ditampilkan: ");
        int jumlah = input.nextInt();

        System.out.println("Deret Fibonacci sebanyak " + jumlah + " angka:");

        // Cetak deret Fibonacci
        for (int i = 0; i < jumlah; i++) {
            System.out.print(fibonacci(i) + " ");
        }

        input.close();
    }
}
