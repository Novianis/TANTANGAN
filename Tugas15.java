package ArrayDanArrayList;

import java.util.ArrayList;
import java.util.Arrays;

public class Tugas15 {
    public static void main(String[] args) {
        ArrayList<Integer> dataAngka = new ArrayList<>(Arrays.asList(10, 20, 30, 40, 50));

        System.out.println("Isi ArrayList:");
        for (int angka : dataAngka) {
            System.out.println(angka);
        }
    }
}
