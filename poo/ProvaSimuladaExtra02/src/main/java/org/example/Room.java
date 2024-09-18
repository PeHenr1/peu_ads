package org.example;

public class Room {
    private final int number;
    private double price;
    private boolean occupied;

    public Room(int number, double price){
        this.number = number;
        this.price = price;
        this.occupied = true;
    }

    public String asString(){
        return "Room " + number + " | $" + price + " | Occupied: " + occupied;
    }

    public double getPrice() {
        return price;
    }

    public boolean isOccupied() {
        return occupied;
    }

    public int getNumber() {
        return number;
    }
}
