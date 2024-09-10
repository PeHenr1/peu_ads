package org.example;

public class Player {
    private String name;
    private int number;
    private String position;
    private boolean isFielded;

    public Player(String name, int number, String position) {
        this.name = name;
        this.number = number;
        this.position = position;
        this.isFielded = false;
    }

    public String getName(){
        return name;
    }

    public void setFielded(boolean fielded) {
        this.isFielded = fielded;
    }

    public boolean isFielded() {
        return isFielded;
    }

    public String getStateAsString() {
        return name + ", " + number + ", " + position + "', isFielded=" + isFielded;
    }
}
