package org.example;

import java.time.LocalDate;
import java.time.Period;

public class Reservation {
    private final String id;
    private LocalDate checkin;
    private LocalDate checkout;
    private final Room room;
    private final Guest guest;

    public Reservation(Guest guest, Room room, LocalDate checkin, LocalDate checkout){
        this.id = ReservationIdGenerator.generateReservationId();
        this.checkin = checkin;
        this.checkout = checkout;
        this.guest = guest;
        this.room = room;
    }

    public double getPrice(){
        return Period.between(checkin,checkout).getDays() * room.getPrice();
    }

    public boolean isReservedAt(LocalDate date, Room room){
        return this.room == room && !date.isBefore(checkin) && !date.isAfter(checkout) && room.isOccupied();
    }

    public String asString(){
        //return "Reservation " + id + "  Room number: " + room.getNumber() + "%nGuest Name: " + guest.getName() + "";

        return "------------------------------------------------------------\n" +
                String.format("Reservation: %s\t\tRoom number: %d\n", id, room.getNumber()) +
                String.format("Guest name: %s\t\tSSN: %s\t\tE-mail: %s\n", guest.getName(), guest.getSsn(), guest.getEmail()) +
                String.format("Check-in: %s\t\tCheck-out: %s\n", checkin, checkout) +
                String.format("Number of days: %d\t\tRoom price: %.2f\n", Period.between(checkin, checkout).getDays(), room.getPrice()) +
                String.format("TOTAL: $%.2f;\n", getPrice()) +
                "------------------------------------------------------------";
    }

    public LocalDate getCheckin() {
        return checkin;
    }

    public LocalDate getCheckout() {
        return checkout;
    }

    public String getId() {
        return id;
    }

    public Room getRoom() {
        return room;
    }
}
