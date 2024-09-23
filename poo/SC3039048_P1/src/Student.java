import java.time.LocalDate;

public class Student {
    private final String id;
    private final String name;
    private final LocalDate admissionDate;

    public Student(String id, String name, LocalDate admissionDate){
        if (!id.matches("SC\\d{6}[0-9X]")) {
            this.id = "SC000000X";
            this.name = "Default";
            this.admissionDate = LocalDate.now();
        }
        else {
            this.id = id;
            this.name = name;
            this.admissionDate = admissionDate;
        }

    }

    public int getSemester(){
        return LocalDate.now().getYear() - admissionDate.getYear();
    }

    public String getStateAsString(){
        return id + " | " + name + " | Admission date = " + admissionDate;
    }


    public String getId() {
        return id;
    }
}
