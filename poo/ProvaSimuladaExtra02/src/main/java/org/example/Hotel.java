package org.example;

import java.time.LocalDate;

public class Hotel {
    private final String name;
    private final Room[] rooms;
    private final Reservation[] reservations;
    private int countReservations;

    public Hotel(String name, Room[] rooms){
        this.name = name;
        this.rooms = rooms;
        this.reservations = new Reservation[10];
        this.countReservations = 0;
    }

    public Reservation makeReservation(Guest guest, int roomNumber, LocalDate checkin, LocalDate checkout){
        for (Room r : rooms){
            r.asString();
        }
        Room room = new Room();
        for (int i = 0; i < rooms.length; i++) {
            if (rooms[i].getNumber() == roomNumber) {
                room = rooms[i];
                break;
            }
        }
        if (guest == null || !isAvailableAt(room, checkin, checkout)) return null;

        room.setOccupied(true);
        return reservations[countReservations++] = new Reservation(guest, room, checkin, checkout);
    }

    private boolean isAvailableAt(Room room, LocalDate checkin, LocalDate checkout){
        Room[] availableRooms = getRoomsAvailableAt(checkin);
        /*
        for (Room available : availableRooms) {
            if (room == available){
                return true;
            }
        }
        return false;
         */
        for (Room available : availableRooms) {
            for (int i = 0; i < countReservations; i++) {
                Reservation reservation = reservations[i];

                if (reservation.getRoom().getNumber() == available.getNumber()) {
                    if (!(checkout.isBefore(reservation.getCheckin()) || checkin.isAfter(reservation.getCheckout().minusDays(1)))) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public Reservation cancelReservation(String reservationId){

        for (int i = 0; i < reservations.length; i++){
            if(reservations[i].getId().equals(reservationId)){
                Reservation canceledReservation = reservations[i];
                for (int j = i; j < reservations.length-1; j++) {
                    reservations[j] = reservations[j + 1];
                }
                canceledReservation.getRoom().setOccupied(false);
                return canceledReservation;
            }
        }
        return null;
    }

    public Room[] getRoomsAvailableAt(LocalDate date){
        int countRoomsAvailable = 0;
        Room[] availableRooms = new Room[rooms.length];

        for (Room room : rooms) {
            boolean available = true;
            for (int i = 0; i < countReservations; i++) {
                if (reservations[i].getRoom().getNumber() == room.getNumber() && reservations[i].isReservedAt(date,room)) {
                    available = false;
                    break;
                }
            }
            if (available) {
                availableRooms[countRoomsAvailable++] = room;
            }
        }
        return availableRooms;
    }
}
