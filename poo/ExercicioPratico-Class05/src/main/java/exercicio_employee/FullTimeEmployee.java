package exercicio_employee;

import java.time.LocalDate;

public final class FullTimeEmployee extends Employee {
    private final double monthlySalary;

    public FullTimeEmployee(String id, String name, String jobTitle, LocalDate dateOfEmployment, double monthlySalary) {
        super(id, name, jobTitle, dateOfEmployment);
        this.monthlySalary = monthlySalary;
    }

    @Override
    public double salary() {
        return monthlySalary;
    }

    @Override
    public String toString() {
        return String.format(
                "FullTimeEmployee: %s | Monthly Salary: $%.2f",
                super.toString(), salary()
        );
    }
}
