package org.example;

import java.util.ArrayList;
import java.util.List;

public class Team {
    private String name;
    private String baseLocation;
    private String coachName;
    private List<Player> players;
    private Player captain;

    public Team(String name, String baseLocation, String coachName) {
        this.name = name;
        this.baseLocation = baseLocation;
        this.coachName = coachName;
        this.players = new ArrayList<>(18);
        this.captain = null;
    }

    public String getName() {
        return name;
    }
    public String getBaseLocation() {
        return baseLocation;
    }
    public String getCoachName() {
        return coachName;
    }
    public Player getCaptain() {
        return captain;
    }

    public void addPlayer(Player player) {
        if (players.size() < 18) {
            players.add(player);
        } else {
            System.out.println("The team is complete");
        }
    }

    public void removePlayer(Player player) {
        players.remove(player);
        if (captain == player) {
            captain = null;
        }
    }

    public void substitute(Player substitute, Player starter) {
        if (starter.isFielded() && !substitute.isFielded()) {
            starter.setFielded(false);
            substitute.setFielded(true);

            System.out.println("\nSubstitution: " + substitute.getName() + " in, " + starter.getName() + " out.");
        }
        else {
            System.out.println("\nSubstitution failed: Ensure the starter is fielded and the substitute is not fielded.");
        }
    }

    public void setCaptain(Player captain) {
        if (players.contains(captain)) {
            this.captain = captain;
        }
    }

    /*
    public Player[] getFieldedPlayers() {
    return players.stream()
            .filter(Player::isFielded)
            .toArray(Player[]::new);
    }

     */
    public Player[] getFieldedPlayers() {
        int count = 0;

        for (Player player : players) {
            if (player.isFielded()) {
                count++;
            }
        }

        Player[] fieldedPlayers = new Player[count];
        int index = 0;

        for (Player player : players) {
            if (player.isFielded()) {
                fieldedPlayers[index] = player;
                index++;
            }
        }

        return fieldedPlayers;
    }

    /*
    public Player[] getOutfieldedPlayers() {
    return players.stream()
            .filter(player -> !player.isFielded())
            .toArray(Player[]::new);
    }
    */
    public Player[] getOutfieldedPlayers() {
        int count = 0;

        for (Player player : players) {
            if (!player.isFielded()) {
                count++;
            }
        }

        Player[] outfieldedPlayers = new Player[count];
        int index = 0;

        for (Player player : players) {
            if (!player.isFielded()) {
                outfieldedPlayers[index] = player;
                index++;
            }
        }

        return outfieldedPlayers;
    }
}
