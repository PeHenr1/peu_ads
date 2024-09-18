package br.edu.ifsp.game;

import br.edu.ifsp.deck.Card;

public class Player {
    private final String name;
    private int score;
    private Card[] cards;
    private int numberOfCards;

    public Player(String name){
        this.name = name;
        this.numberOfCards = 0;
    }

    public void setCards(Card[] cards) {
        this.cards = cards;
        this.numberOfCards = 3;
    }

    public Card chooseCard(){
        return cards[--numberOfCards];
    }

    public void incrementScore(){
        score++;
    }

    public String getName() {
        return name;
    }

    public int getScore() {
        return score;
    }
}
