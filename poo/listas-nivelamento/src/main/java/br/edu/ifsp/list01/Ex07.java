package br.edu.ifsp.list01;

import java.util.Scanner;

/*
    Um motorista de Uber estipula o preço de uma determinada viagem dada a quantidade de quilômetros percorrida.
    Para viagens de até X km, é cobrado um valor R$ V1 por km. Acima de X km, é cobrado o valor R$ V2.
    Faça um programa que leia X, V1, V2 e a quantidade de quilômetros A da viagem e imprima o valor total
    com duas casas decimais.

    Exemplos de entrada e saída:
    Entrada    	Saídal
    100         75.00
    1.50
    1.25
    50
    Entrada    	Saída
    100         187.50
    1.50
    1.25
    150
*/
public class Ex07 {

    public static void main(String[] args) {
        //Leia o input
        Scanner scanner = new Scanner(System.in);
        //Crie uma variável do tipo deste arquivo. Exemplo: Ex02 ex = new Ex02();
        int distance = scanner.nextInt();
        double priceOne = scanner.nextDouble();
        double priceTwo = scanner.nextDouble();
        double travelKm = scanner.nextDouble();
        //Crie uma variável do tipo deste arquivo. Exemplo: Ex02 ex = new Ex02();
        Ex07 ex07 = new Ex07();
        //Escreva o resultado da chamada do método compute() aqui
        System.out.println(ex07.compute(distance,priceOne,priceTwo,travelKm));
    }

    double compute(int x, double v1, double v2, double a) {
        if(a > x){ return (a * v2); }
        return (a * v1);
    }
}
