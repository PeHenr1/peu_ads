package br.edu.ifsp.list02;

import java.util.Arrays;
import java.util.Scanner;

public class Ex03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leitura dos 5 números inteiros não repetidos em uma única linha
        int[] firstFive = new int[5];
        for (int i = 0; i < 5; i++) {
            firstFive[i] = scanner.nextInt();
        }

        // Criação de um array para os outros números a serem processados
        int[] otherInts = new int[10];
        System.arraycopy(firstFive, 0, otherInts, 0, 5);

        // Criação da instância da classe e chamada do método compute
        Ex03 ex03 = new Ex03();
        String result = ex03.compute(firstFive, otherInts);
        System.out.println(result);
    }

    String compute(int[] firstFive, int[] otherInts) {
        int[] newArray = new int[10];
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < firstFive.length; i++) {
            newArray[i] = firstFive[i];
        }
        int tamanho = 5;
        while (tamanho > 0 && tamanho <10) {
            if (otherInts.length < 1) {
                output.append("Erro");
                break;
            }
            for (int j = 0; j < otherInts.length; j++) {
                for (int i = 0; i < tamanho; i++) {
                    output.append(newArray[i]);
                    if (i < tamanho - 1) {
                        output.append(" ");
                    }
                }
                if (contains(newArray, tamanho, otherInts[j])) {
                    int index = indexOf(newArray, tamanho, otherInts[j]);
                    for (int k = index; k < tamanho - 1; k++) {
                        newArray[k] = newArray[k + 1];
                    }
                    tamanho--;
                } else {
                    newArray[tamanho] = otherInts[j];
                    tamanho++;
                }
                if(tamanho >0&&tamanho<11)output.append("\n");
                if(tamanho == 10){
                    for (int i = 0; i < tamanho; i++) {
                        output.append(newArray[i]);
                        if (i < tamanho - 1) {
                            output.append(" ");
                        }
                    }
                }
            }
        }
        return output.toString();
    }

    private static boolean contains(int[] conjunto, int tamanho, int num) {
        for (int i = 0; i < tamanho; i++) {
            if (conjunto[i] == num) {
                return true;
            }
        }
        return false;
    }

    private static int indexOf(int[] conjunto, int tamanho, int num) {
        for (int i = 0; i < tamanho; i++) {
            if (conjunto[i] == num) {
                return i;
            }
        }
        return -1;
    }



}
