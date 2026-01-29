package Algoritma;

import java.util.Scanner;

public class Tugas1 {

    // Fungsi rekursif untuk menghitung pangkat
    public static int hitungPangkat(int basis, int eksponen) {
        if (eksponen == 0) {
            return 1;
        } else {
            return basis * hitungPangkat(basis, eksponen - 1);
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Input dari pengguna
        System.out.print("Masukkan angka yang ingin dipangkatkan: ");
        int basis = input.nextInt();

        System.out.print("Masukkan nilai pangkat: ");
        int eksponen = input.nextInt();

        // Panggil fungsi dan tampilkan hasil
        int hasil = hitungPangkat(basis, eksponen);
        System.out.println("Hasil dari " + basis + "^" + eksponen + " adalah " + hasil);

        input.close();
    }
}
