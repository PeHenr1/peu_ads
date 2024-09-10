package org.example;

public class Main {
    public static void main(String[] args) {
        Team myTeam = new Team("Tigers", "New York", "John Doe");

        Player player1 = new Player("Alice", 1, "Forward");
        Player player2 = new Player("Bob", 2, "Midfielder");
        Player player3 = new Player("Charlie", 3, "Defender");
        Player player4 = new Player("David", 4, "Goalkeeper");
        Player player5 = new Player("Eve", 5, "Forward");

        myTeam.addPlayer(player1);
        myTeam.addPlayer(player2);
        myTeam.addPlayer(player3);
        myTeam.addPlayer(player4);
        myTeam.addPlayer(player5);

        player1.setFielded(true);
        player2.setFielded(true);
        player3.setFielded(true);

        System.out.println("Before substitution:\n");

        myTeam.setCaptain(player1);
        System.out.println("Captain: " + myTeam.getCaptain().getName());

        Player[] fieldedPlayers = myTeam.getFieldedPlayers();
        System.out.println("\nFielded players:");
        for (Player player : fieldedPlayers) {
            System.out.println(player.getStateAsString());
        }

        Player[] outfieldedPlayers = myTeam.getOutfieldedPlayers();
        System.out.println("\nOutfielded players:");
        for (Player player : outfieldedPlayers) {
            System.out.println(player.getStateAsString());
        }

        myTeam.substitute(player5, player1);

        System.out.println("\n\nAfter substitution:\n");

        myTeam.setCaptain(player3);
        System.out.println("Captain: " + myTeam.getCaptain().getName());

        fieldedPlayers = myTeam.getFieldedPlayers();
        outfieldedPlayers = myTeam.getOutfieldedPlayers();

        System.out.println("\nFielded players:");
        for (Player player : fieldedPlayers) {
            System.out.println(player.getStateAsString());
        }

        System.out.println("\nOutfielded players:");
        for (Player player : outfieldedPlayers) {
            System.out.println(player.getStateAsString());
        }
    }
}
