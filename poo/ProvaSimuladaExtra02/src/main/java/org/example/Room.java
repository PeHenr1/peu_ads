package org.example;

public class Room {
    private int number;
    private double price;
    private boolean occupied;

    public Room(int number, double price){
        this.number = number;
        this.price = price;
    }

    public Room() {
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

    public void setOccupied(boolean occupied) {
        this.occupied = occupied;
    }


}
