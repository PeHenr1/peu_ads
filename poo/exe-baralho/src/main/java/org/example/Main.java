package org.example;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Deck deck = new Deck();
        final Card[] cards = deck.takeMany(10);
        for (Card card : cards) {
            System.out.println(card.asString());
        }

    }
}