package exercicio_employee;

import java.time.LocalDate;

public abstract sealed class Employee permits FullTimeEmployee, PerHourEmployee{
    private final String id;
    protected final String name;
    protected final String jobTitle;
    protected final LocalDate dateOfEmployment;

    public Employee(String id, String name, String jobTitle, LocalDate dateOfEmployment) {
        this.id = id;
        this.name = name;
        this.jobTitle = jobTitle;
        this.dateOfEmployment = dateOfEmployment;
    }

    public abstract double salary();

    @Override
    public String toString() {
        return "[" + id + "] " + name + " | " + jobTitle + " | " + dateOfEmployment;

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
    public LocalDate getDateOfEmployment() {
        return dateOfEmployment;
    }

}
