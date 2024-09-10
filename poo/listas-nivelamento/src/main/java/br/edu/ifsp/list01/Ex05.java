package br.edu.ifsp.list01;

import java.util.Locale;
import java.util.Scanner;

/*
    A avenida principal da cidade de Algoritmopolis possui limite de velocidade de L km/h.
    Se o motorista ultrapassar essa velocidade, é aplicado uma multa de R$ M, mais R$ A
    por cada km acima do limite. Faça um programa que leia o limite L, o valor da multa M,
    o valor adicional A e a velocidade V captada pelo radar e informe o valor total da multa.
    Considere L e V sempre como números inteiros. Apresente a resposta com duas casas decimais.

    Exemplos de entrada e saída:
    Entrada	    Saída
    60          200.00
    150.00
    10.00
    65

    Entrada	    Saída
    60          0.00
    150.00
    10.00
    50
*/
public class Ex05 {

    public static void main(String[] args) {
        //Leia o input
        Scanner scanner = new Scanner(System.in);
        //Crie uma variável do tipo deste arquivo. Exemplo: Ex02 ex = new Ex02();
        int limit = scanner.nextInt();
        double penalty = scanner.nextDouble();
        double additional = scanner.nextDouble();
        int speed = scanner.nextInt();
        //Crie uma variável do tipo deste arquivo. Exemplo: Ex02 ex = new Ex02();
        Ex05 ex05 = new Ex05();
        //Escreva o resultado da chamada do método compute() aqui
        System.out.println(ex05.compute(limit,penalty,additional,speed));
    }

    String compute(int L, double m, double a, int v) {
        double haveToPay = 0;
        if(v > L){
            haveToPay = m;
            v -= L;
            while(v > 0){
                haveToPay += a;
                v--;
            }
            return String.format(Locale.US, "%.2f", haveToPay);
        }
        return "0.00";


    }
}
