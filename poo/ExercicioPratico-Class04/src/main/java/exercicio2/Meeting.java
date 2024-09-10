package exercicio2;

import java.time.Duration;
import java.time.LocalTime;

public class Meeting {
    private String description;
    private final LocalTime startTime;
    private final LocalTime endTime;

    public Meeting(String description, LocalTime startTime, LocalTime endTime) {
        this.startTime = startTime;
        this.endTime = endTime;
        this.description = description;
    }

    public LocalTime getStartTime() {
        return startTime;
    }

    public LocalTime getEndTime() {
        return endTime;
    }

    public String getDescription() {
        return description;
    }

    public long durationInMinutes(){
        return Duration.between(startTime,endTime).toMinutes();
    }
}
