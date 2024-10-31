package org.example;

import java.util.*;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Map<String, Integer> strings = new TreeMap<>();
        while(!scanner.nextLine().isBlank()){
            String string = scanner.nextLine();
            strings.put(string, (strings.get(string) == null ? 0 : strings.get(string)) + 1);
        }

        /*System.out.println("\nTodas as palavras digitadas:");
        for (String palavra : strings.keySet()) {
            System.out.println(palavra);
        }*/

        System.out.println("\nPalavras sem repetição e em ordem alfabética:");
        for (String palavra : strings.keySet()) {
            System.out.println(palavra);
        }

        /*System.out.println("\nFrequência de cada palavra:");
        for (Map.Entry<String, Integer> entry : strings.entrySet()) {
            System.out.println(STR."\{entry.getKey()}: \{entry.getValue()}");
        }*/
    }
}