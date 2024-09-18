package br.edu.ifsp.game;

import br.edu.ifsp.deck.Card;
import br.edu.ifsp.deck.Deck;

public class Hand {
    private Card vira;
    private final Player player1;
    private final Player player2;
    private final Round[] rounds;
    private int numberOfRounds;

    public Hand(Player player1, Player player2){
        this.player1 = player1;
        this.player2 = player2;
        this.rounds = new Round[3];
        dealCards(player1,player2);
    }

    private void dealCards(Player player1, Player player2) {
        final Deck deck = new Deck();
        deck.shuffle();
        vira = deck.takeOne();
        player1.setCards(deck.take(3));
        player2.setCards(deck.take(3));
    }

    public void playRound(){
        final Card card1 = player1.chooseCard();
        final Card card2 = player2.chooseCard();
        final Round round = new Round(player1.getName(), card1, player2.getName(), card2, vira);
        System.out.println("Round result: " + (round.getWinner() != null ? round.getWinner() : "DRAW"));
        rounds[numberOfRounds++] = round;
    }

    public boolean isDone(){
        if (numberOfRounds < 2) return false;
        if (numberOfRounds == 3) return true;

        String winnerRound1 = rounds[0].getWinner();
        String winnerRound2 = rounds[1].getWinner();

        if (wonBothRounds(winnerRound1, winnerRound2)) return true;
        if (drewTwice(winnerRound1, winnerRound2)) return false;
        return drewOnce(winnerRound1, winnerRound2);
    }

    private boolean drewOnce(String winnerRound1, String winnerRound2) {
        return winnerRound1 == null || winnerRound2 == null;
    }

    private boolean drewTwice(String winnerRound1, String winnerRound2) {
        return winnerRound1 == null && winnerRound2 == null;
    }

    private boolean wonBothRounds(String winnerRound1, String winnerRound2) {
        return winnerRound1 != null && winnerRound1.equals(winnerRound2);
    }

    public String getWinner(){
        if (!isDone()) return null;
        String winnerRound1 = getRoundResult(0);
        String winnerRound2 = getRoundResult(1);
        String winnerRound3;

        if (rounds[2] == null) winnerRound3 = null;
        else winnerRound3 = getRoundResult(2);

        if (!winnerRound1.equals("DRAW") && winnerRound1.equals(winnerRound2))
            return winnerRound1;
        if (!winnerRound1.equals("DRAW") && winnerRound2.equals("DRAW"))
            return winnerRound1;
        if (winnerRound1.equals(winnerRound3) && !"DRAW".equals(winnerRound1)) {
            return winnerRound1;
        }
        if (!winnerRound2.equals("DRAW")) return winnerRound2;
        if (!"DRAW".equals(winnerRound3)) return winnerRound3;
        return null;
    }

    private String getRoundResult(int roundNumber) {
        return rounds[roundNumber].getWinner() != null ?
                rounds[roundNumber].getWinner()
                : "DRAW";
    }
}
