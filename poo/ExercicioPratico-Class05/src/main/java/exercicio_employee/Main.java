package exercicio_employee;

import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        Employee e1 = new FullTimeEmployee("X-0001","James Carter","Admin Officer", LocalDate.of(2001,9,11),3500);
        Employee e2 = new PerHourEmployee("X-0002","Robert Calvins","Assistant", LocalDate.of(2021,3,31),20,5);

        System.out.println(e1);
        System.out.println(e2);

        System.out.println(e1.getId());
        System.out.println(e1.getName());
        System.out.println(e1.getJobTitle());
        System.out.println(e1.getDateOfEmployment());
        System.out.println(e1.salary());
    }
}
