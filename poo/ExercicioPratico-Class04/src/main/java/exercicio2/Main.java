package exercicio2;

import java.time.LocalDate;
import java.time.LocalTime;

public class Main {
    public static void main(String[] args) {
        Schedule schedule = new Schedule(LocalDate.now(), LocalTime.of(9, 0), LocalTime.of(17, 0));

        Meeting meeting1 = new Meeting("Project Meeting", LocalTime.of(10, 0), LocalTime.of(11, 0));
        Meeting meeting2 = new Meeting("Marketing Meeting", LocalTime.of(12, 0), LocalTime.of(13, 30));
        Meeting meeting3 = new Meeting("ADS Client Meeting", LocalTime.of(16, 0), LocalTime.of(17, 0));

        schedule.addMeeting(meeting1);
        schedule.addMeeting(meeting2);
        schedule.addMeeting(meeting3);

        System.out.println(schedule.scheduleAsString());

        System.out.printf("Percentage of time spent in meetings: %.2f%%%n", schedule.percentageSpentInMeetings());

        schedule.removeMeeting(meeting2);

        System.out.println(schedule.scheduleAsString());
        System.out.printf("Percentage of time spent in meetings: %.2f%%%n", schedule.percentageSpentInMeetings());
    }

}
