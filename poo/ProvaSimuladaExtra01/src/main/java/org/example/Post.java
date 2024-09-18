package org.example;

import java.time.LocalDate;

public class Post {
    private UserAccount account;
    private String quote;
    private LocalDate date;
    private int claps;
    private int boos;
    private final int id;
    private static int idCounter = 0;

    public Post(UserAccount account, String quote){
        this.id = ++idCounter;
        this.account = account;
        this.quote = quote;
        this.date = LocalDate.now();
        this.claps = 0;
        this.boos = 0;
    }

    public String show(){
        return "[" + date + "] " + account.getUserName() + " says \"" + quote + "\" | Claps: " + claps + " | Boos: " + boos;
    }

    public void clap(){
        claps++;
    }

    public void boo(){
        boos++;
    }

    public int getId() {
        return id;
    }
}
