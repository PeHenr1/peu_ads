package org.example;

import java.time.LocalDate;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Room[] rooms = {
                new Room(101, 300),
                new Room(102, 350),
                new Room(103, 400),
                new Room(104, 300),
                new Room(105, 500)
        };
        Hotel hotel = new Hotel("Reservation.com",rooms);

        Guest guest1 = new Guest("12345", "John Wick", "johnwick@email.com");
        Guest guest2 = new Guest("67890", "Jane Doe", "guest2@email.com");

        Reservation res1 = hotel.makeReservation(guest1, 101, LocalDate.of(2024, 3, 27), LocalDate.of(2024, 3, 28));
        System.out.println(res1.asString());

        Reservation res2 = hotel.makeReservation(guest2, 105, LocalDate.of(2024, 10, 15), LocalDate.of(2024, 10, 20));
        System.out.println(res2.asString());

        Reservation cancelled = hotel.cancelReservation(res1.asString().split(",")[0].split(":")[1].trim());
        System.out.println(cancelled);
    }
}