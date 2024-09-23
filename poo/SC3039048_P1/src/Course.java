import java.time.DayOfWeek;
import java.time.LocalTime;

public class Course {
    private static int idCounter = 1;

    private final int id;
    private final LocalTime startTime;
    private final LocalTime endTime;
    private final String name;
    private final String code;
    private final String professor;
    private final DayOfWeek dayOfWeek;
    enum Room {C102,C104,C105,C106,C107,C209};
    private final Room room;

    public Course(LocalTime startTime, LocalTime endTime, String name, String code, String professor, DayOfWeek dayOfWeek, Room room){
        this.id = idCounter++;
        this.name = name != null ? name : "Default";
        this.code = code != null ? code : "Default";
        this.professor = professor != null ? professor : "Unknown";
        this.dayOfWeek = dayOfWeek != null ? dayOfWeek : DayOfWeek.MONDAY;
        this.room = room != null ? room : Room.C102;
        this.startTime = startTime != null ? startTime : LocalTime.of(9, 0);
        this.endTime = endTime != null ? endTime : LocalTime.of(10, 0);
    }

    public int getWeeklyDurationInMinutes(){
        return 210; //considerando aulas padrao das 19h as 22h30 uma vez por semana
    }

    public String getStateAsString(){
        return "| id = " + id + " | " + name + " (" + code + ") | " + dayOfWeek + " | Start = " + startTime + " | End = " + endTime + " | " + professor + " | Room = " + room;
    }

    public LocalTime getStartTime() {
        return startTime;
    }

    public LocalTime getEndTime() {
        return endTime;
    }

    public DayOfWeek getDayOfWeek() {
        return dayOfWeek;
    }
}
