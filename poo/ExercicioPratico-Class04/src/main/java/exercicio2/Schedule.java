package exercicio2;

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;

public class Schedule {
    private LocalDate day;
    private LocalTime startTime;
    private LocalTime endTime;
    private List <Meeting> meetings;

    public Schedule(LocalDate day, LocalTime startTime, LocalTime endTime) {
        if (startTime.isAfter(endTime)) {
            throw new IllegalArgumentException("Invalid work hours.");
        }
        this.day = day;
        this.startTime = startTime;
        this.endTime = endTime;
        this.meetings = new ArrayList<>();
    }

    public void addMeeting(Meeting meeting){
        if (meeting.getStartTime().isBefore(startTime) || meeting.getEndTime().isAfter(endTime)) {
            System.out.println("Meeting out of working hours.");
        }
        else {

            boolean hasOverlap = false;
            for (Meeting m : meetings) {
                if (meeting.getStartTime().isBefore(m.getEndTime()) && meeting.getEndTime().isAfter(m.getStartTime())) {
                    System.out.println("Not possible to add: there are meetings overlapping.");
                    hasOverlap = true;
                    break;
                }
            }
            if (!hasOverlap) {
                meetings.add(meeting);
                System.out.println("Meeting scheduled successfully!");
            }


        }
    }

    public void removeMeeting(Meeting meeting){
        meetings.remove(meeting);
        System.out.printf("\nMeeting '%s' removed successfully.%nUploading schedule...\n",meeting.getDescription());
    }

    public double percentageSpentInMeetings(){
        long totalWorkMinutes = Duration.between(startTime,endTime).toMinutes();
        long totalMeetingMinutes = 0;
        for (Meeting meeting : meetings) {
            totalMeetingMinutes += meeting.durationInMinutes();
        }

        return (double) totalMeetingMinutes / totalWorkMinutes * 100;
    }

    public String scheduleAsString(){
        StringBuilder sb = new StringBuilder();

        sb.append(String.format("\nSchedule for the day: %s%n", day));
        sb.append(String.format("Working hours: %s - %s%n", startTime, endTime));

        if (meetings.isEmpty()) {
            sb.append("No meetings scheduled.\n");
        }
        else {
            sb.append("Meetings:\n");
            meetings.forEach(meeting -> sb.append(String.format(
                    "- %s: %s - %s\n",meeting.getDescription(),meeting.getStartTime(),meeting.getEndTime())
            ));
        }

        return sb.toString();
    }


}
