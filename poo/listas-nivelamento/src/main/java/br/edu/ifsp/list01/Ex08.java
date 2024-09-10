package br.edu.ifsp.list01;

import java.util.Scanner;

/*
    Alan quer comprar limões para fazer uma limonada. Próximo da sua casa há um mercadinho que vende limões da seguinte
    forma: O primeiro limão é vendido por C centavos, o segundo por C − 1 centavos, o terceiro por C − 2 e assim
    por diante até o menor valor de 1 centavo. Por exemplo, se C = 3 e Alan quiser comprar *5* limões, o preço total
    será 3 + 2 + 1 + 1 + 1 = 8.

    Faça um programa que leia dois inteiros *N* e *C* que indicam respectivamente o número de limões e o valor em
    centavos do primeiro limão. Em seguida imprima o valor total em centavos.

    ### Exemplos de entrada e saída:

    | Entrada  | Saída  |
    | -------  | ------ |
    | 5 3      | 8      |
    | 3 3      | 6      |

    Fonte: Adaptado de https://neps.academy/problem/193
    => Exercício gentilmente cedido pelos profs. Jorge Cutigi e Adenilso Simão (ICMC/USP)
*/
public class Ex08 {

    public static void main(String[] args) {
        //Leia o input
        Scanner scanner = new Scanner(System.in);
        //Crie uma variável do tipo deste arquivo. Exemplo: Ex02 ex = new Ex02();
        int quantity = scanner.nextInt();
        int price = scanner.nextInt();
        //Crie uma variável do tipo deste arquivo. Exemplo: Ex02 ex = new Ex02();
        Ex08 ex08 = new Ex08();
        //Escreva o resultado da chamada do método compute() aqui
        System.out.println(ex08.compute(quantity,price));
    }

    int compute(int n, int c) {
        int total = 0, cont = 0;
        while (n != 0) {
            if ( (c-cont) != 1) {
                total += (c-cont);
                cont++;
                n--;
                continue;
            }
            total += (c-cont);
            n--;
        }
        return total;
    }
}
