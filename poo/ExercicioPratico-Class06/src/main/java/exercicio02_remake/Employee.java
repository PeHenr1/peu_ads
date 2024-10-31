package exercicio02_remake;

import java.time.LocalDate;

public class Employee {
    private final String id;
    private final String name;
    private final String jobTitle;
    private final double salary;
    private final LocalDate dateOfEmployment;

    public Employee(String id, String name, String jobTitle, double salary, LocalDate dateOfEmployment){
        this.id = id;
        this.name = name;
        this.jobTitle = jobTitle;
        this.salary = salary;
        this.dateOfEmployment = dateOfEmployment;
    }

    public double getYearsOfService(){
        return LocalDate.now().getYear() - dateOfEmployment.getYear();
    }

    public double calculateBonus(){
        return salary * 0.1 * getYearsOfService();
    }

    public String getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    public String getJobTitle() {
        return jobTitle;
    }
    public double getSalary() {
        return salary;
    }
    public LocalDate getDateOfEmployment() {
        return dateOfEmployment;
    }

}
