package br.edu.ifsp;

import br.edu.ifsp.game.Game;
import br.edu.ifsp.game.Player;

public class Principal {
    public static void main(String[] args) {
        final Player seanDiaz = new Player("Sean");
        final Player finnMcNamara = new Player("Finn");
        final Game game = new Game(seanDiaz, finnMcNamara);
        while (!game.isDone()){
            game.play();
        }
        System.out.println("Game winner: " + game.getWinner().getName());
    }
}
