import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.chrono.ChronoLocalDate;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Course c1 = new Course(LocalTime.of(19,0),LocalTime.of(22,30),"Objected-orientation","POO","Lucas Bueno", DayOfWeek.FRIDAY, Course.Room.C106);
        Course c2 = new Course(LocalTime.of(8,0),LocalTime.of(11,30),"Databases I","BD1","Carlão", DayOfWeek.MONDAY, Course.Room.C102);
        Course c3 = new Course(LocalTime.of(19,0),LocalTime.of(22,30),"Databases II","BD2","Silvana", DayOfWeek.WEDNESDAY, Course.Room.C104);


        Student s1 = new Student("SC363450X","Zeca",LocalDate.now());
        Student s2 = new Student("SY363450X","Lorena",LocalDate.now());
        Student s3 = new Student("SC2032030","Asdrubal Nunes",LocalDate.now());

        System.out.println(s1.getStateAsString());
        System.out.println(s2.getStateAsString());
        System.out.println(s3.getStateAsString());

        Enrollment e1 = new Enrollment(s1);
        Enrollment e2 = new Enrollment(s2);
        Enrollment e3 = new Enrollment(s3);

        System.out.println(e1.enroll(c1));
        //System.out.println(c1.getStateAsString());
        System.out.println(e1.enroll(c2));
        //System.out.println(c2.getStateAsString());
        System.out.println(e1.enroll(c3));

        System.out.println(e3.enroll(c1));
        System.out.println(e3.enroll(c3));

        System.out.println(e2.enroll(c1));

        e1.remove(c3);
        e3.conclude();

        System.out.println(e1.getStateAsString());
        System.out.println(e2.getStateAsString());
        System.out.println(e3.getStateAsString());
    }
}