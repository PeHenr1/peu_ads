package br.edu.ifsp.list01;

import java.sql.SQLOutput;
import java.util.Scanner;

/*
    Você está na Austrália treinando cangurus para se locomoverem em linha reta. Você quer saber se dois cangurus
    estarão na mesma posição em um deter0minado tempo, dado a posição inicial de cada canguru e qual a distância que
    eles saltam. Como você sabe programar muito bem, você decidiu fazer um programa para isso. Seu programa deve ler:
     - A posição inicial X1 e a distância do pulo V1 do primeiro canguru.
     - A posição inicial X2 e a distância do pulo V2 do segundo canguru.

    Após isso, seu programa deve imprimir SIM se os dois cangurus se encontrarão no mesmo ponto e NAO caso eles
    nunca se encontrem.

    Por exemplo, o primeiro canguru começa em X1 = 2 e tem uma distância do pulo de V1 = 1. O segundo canguru começa
    em X2 = 1 e tem uma distância de pulo de V2 = 2. Após um pulo ambos estarão no ponto *3*, portanto a respota é SIM.

    ### Exemplos de entrada e saída:

    | Entrada    | Saída  |
    | -------    | ------ |
    | 0  3  4  2 | SIM    |
    | 0  2  5  3 | NAO    |

    Fonte: Adaptado de https://www.hackerrank.com/challenges/kangaroo/problem

    => Exercício gentilmente cedido pelos profs. Jorge Cutigi e Adenilso Simão (ICMC/USP)
*/
public class Ex10 {
    public static void main(String[] args) {
        //Leia o input
        Scanner scanner = new Scanner(System.in);
        int posicaoInicialUm = scanner.nextInt();
        int distanciaPuloUm = scanner.nextInt();
        int posicaoInicialDois = scanner.nextInt();
        int distanciaPuloDois = scanner.nextInt();
        //Crie uma variável do tipo deste arquivo. Exemplo: Ex02 ex = new Ex02();
        Ex10 ex10 = new Ex10();
        //Escreva o resultado da chamada do método compute() aqui
        System.out.println(ex10.compute(posicaoInicialUm,distanciaPuloUm,posicaoInicialDois,distanciaPuloDois));
    }

    /*
    essa logica nao funcionou apenas para o teste 14 4 98 2
    String compute(int x1, int v1, int x2, int v2) {
        for (int i = 0; i < (v1*v2); i++) {
            if(x1 == x2){
                return "SIM";
            }
            x1 += v1;
            x2 += v2;
        }
        return "NAO";
    }

    //LOGICA MINHA CORRIGIDA
    String compute(int x1, int v1, int x2, int v2) {
        // Se as posições iniciais são iguais, já retornamos SIM
        if (x1 == x2) {
            return "SIM";
        }

        // Loop para simular os saltos
        while ((v1 > v2 && x1 < x2) || (v1 < v2 && x1 > x2)) {
            x1 += v1;
            x2 += v2;

            // Verifica se as posições coincidem após o salto
            if (x1 == x2) {
                return "SIM";
            }
        }

        // Se não encontrarem, retorna NAO
        return "NAO";
    }
    */

    /*
        Verificação Matemática
        Para determinar se os cangurus vão se encontrar, a melhor abordagem é usar uma verificação matemática:

        Condição de Encontro:

        Os cangurus se encontrarão em um ponto t se suas posições forem iguais: x1 + t * v1 == x2 + t * v2.
        Simplificando: (x1 - x2) == t * (v2 - v1).
        Portanto, os cangurus se encontrarão se (x1 - x2) for divisível por (v2 - v1) e (v1 != v2).
        Outros Cenários:

        Se v1 == v2, os cangurus só podem se encontrar se x1 == x2 desde o início.
        Se (v1 > v2 && x1 < x2) ou (v1 < v2 && x1 > x2), eles nunca se encontrarão.
*/

    String compute(int x1, int v1, int x2, int v2) {
        if (v1 == v2) {
            return (x1 == x2) ? "SIM" : "NAO";
        }

        if ((x2 - x1) % (v1 - v2) == 0 && (x2 - x1) / (v1 - v2) > 0) {
            return "SIM";
        }

        return "NAO";
    }







}
