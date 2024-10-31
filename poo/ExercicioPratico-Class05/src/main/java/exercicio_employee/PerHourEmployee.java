package exercicio_employee;

import java.time.LocalDate;

public final class PerHourEmployee extends Employee {
    private final double hourlyRate;
    private final int workedHour;

    public PerHourEmployee(String id, String name, String jobTitle, LocalDate dateOfEmployment, double hourlyRate, int workedHour) {
        super(id, name, jobTitle, dateOfEmployment);
        this.hourlyRate = hourlyRate;
        this.workedHour = workedHour;
    }

    @Override
    public double salary() {
        return workedHour * hourlyRate;
    }

    @Override
    public String toString() {
        return String.format(
                "PerHourEmployee: %s | Daily Salary: $%.2f (Worked Hours: %d Hourly Rate: $%.2f)",
                super.toString(), salary(), workedHour, hourlyRate
        );
    }
}
