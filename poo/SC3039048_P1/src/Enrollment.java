import java.time.DayOfWeek;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Enrollment {
    private static int idCounter = 1;

    private int id;
    private LocalDateTime enrollmentTime;
    private LocalDateTime conclusionTime;
    private boolean concluded;
    private final Student student;
    private final Course[] courses;
    private int countCourses;

    private static final Course DEFAULT_COURSE = new Course(null, null, "Default Course", "Default", "Unknown", DayOfWeek.MONDAY, Course.Room.C102);

    public Enrollment(Student student){
        this.id = idCounter++;
        this.student = student;
        this.countCourses = 0;

        if (!isValidStudent(student)) {
            this.courses = new Course[1];
            this.courses[countCourses++] = DEFAULT_COURSE;
            this.concluded = true;
        }
        else {
            this.courses = new Course[7];
            this.concluded = false;
            this.enrollmentTime = LocalDateTime.now();
        }


    }

    public boolean enroll(Course course){
        if (concluded) return false;

        int totalMinutes = 0;
        for (int i = 0; i < countCourses; i++) {
            totalMinutes += courses[i].getWeeklyDurationInMinutes();
        }

        if (totalMinutes > 1320) return false;

        for (int i = 0; i < countCourses; i++) {
            Course existingCourse = courses[i];
            if (existingCourse.getDayOfWeek() == course.getDayOfWeek()) {
                if ((course.getStartTime().isBefore(existingCourse.getEndTime()) && course.getEndTime().isAfter(existingCourse.getStartTime()))) {
                    return false;
                }
            }
        }

        if (countCourses < courses.length) {
            courses[countCourses] = course;
            countCourses++;
            return true;
        }
        return false;
    }

    public void remove(Course course){
        if (!concluded){
            for (int i = 0; i < countCourses; i++) {
                if (course == courses[i]){
                    for (int j = i; j < countCourses-1; j++) {
                        courses[j] = courses[j + 1];
                    }
                    courses[countCourses - 1] = null;
                    countCourses--;
                    break;
                }
            }
        }
    }

    public String getStateAsString(){
        if (!concluded) return "Enrollment not concluded!";
        if (!isValidStudent(student)) return "Invalid Enrollment";

        DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        DateTimeFormatter timeFormatter = DateTimeFormatter.ofPattern("HH:mm:ss");

        StringBuilder sb = new StringBuilder()
                .append("===============================================\n")
                .append(student.getStateAsString()).append("\n")
                .append("Enrollment Time: ")
                .append(enrollmentTime.format(dateFormatter)).append(" ")
                .append(enrollmentTime.format(timeFormatter)).append("\n")
                .append("-----------------------------------------------\n")
                .append("Courses:\n");
        for (int i = 0; i < countCourses; i++){
            sb.append(courses[i].getStateAsString()).append("\n");
        }
        sb.append("===============================================");

        return sb.toString();
    }

    public void conclude() {
        if (!concluded) {
            setConcluded(true);
            this.conclusionTime = LocalDateTime.now();
        }
    }

    public void setConcluded(boolean concluded) {
        this.concluded = concluded;
    }

    private boolean isValidStudent(Student student) {
        return student != null && !student.getId().equals("SC000000X");
    }


}
