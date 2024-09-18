package br.edu.ifsp.game;

public class Game {
    private final Player player1;
    private final Player player2;
    private final Hand[] hands;
    private int numberOfHands;

    public Game(Player player1, Player player2){
        this.player1 = player1;
        this.player2 = player2;
        hands = new Hand[30];
        hands[0] = new Hand(player1,player2);
        numberOfHands++;
    }

    public void play(){
        if(isDone()) return;
        Hand currentHand = hands[numberOfHands - 1];
        if (currentHand.isDone()){
            computeResult(currentHand);
            currentHand = prepareNewHand();
        }
        currentHand.playRound();
    }

    private void computeResult(Hand currentHand) {
        final String winner = currentHand.getWinner();
        if(player1.getName().equals(winner)) player1.incrementScore();
        else if (player2.getName().equals(winner)) player2.incrementScore();
        System.out.println("Hand winner: " + (winner != null ? winner : "DRAW"));
    }

    private Hand prepareNewHand() {
        Hand currentHand = new Hand(player1, player2);
        hands[numberOfHands++] = currentHand;
        return currentHand;
    }

    public boolean isDone(){
        return player1.getScore() == 12 || player2.getScore() == 12;
    }

    public Player getWinner(){
        if(!isDone()) return null;
        if(player1.getScore() == 12) return player1;
        return player2;
    }
}
