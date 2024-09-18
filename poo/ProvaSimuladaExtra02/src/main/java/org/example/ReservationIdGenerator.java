package org.example;

import java.time.LocalDateTime;

public class ReservationIdGenerator {
    private static int sequencialNumber = 10000;

    private ReservationIdGenerator() {
        throw new UnsupportedOperationException("This is a utility class and cannot be instantiated.");
    }

    public static String generateReservationId(){
        LocalDateTime now = LocalDateTime.now();

        String seconds = String.format("%02d",now.getSecond());
        String minutes = String.format("%02d",now.getMinute());

        return String.format("HT%s-%s-%s-%05d", seconds, minutes, seconds, ++sequencialNumber);
    }

}
