package exercicio02;

import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        Repository<String, Employee> repository = new FakeEmployeeRepository();

        RegisterEmployeeService registerService = new RegisterEmployeeService(repository);
        FindEmployeeService findService = new FindEmployeeService(repository);

        Employee emp1 = new Employee("001", "Alice", "Desenvolvedora", 5000, LocalDate.of(2020, 5, 10));
        Employee emp2 = new Employee("002", "Bob", "Designer", 4000, LocalDate.of(2018, 3, 20));

        registerService.register(emp1);
        registerService.register(emp2);

        registerService.register(emp1);

        Employee foundEmployee = findService.findById("001");
        if (foundEmployee != null) {
            System.out.println("Empregado encontrado: " + foundEmployee.getName() + ", Bônus: " + foundEmployee.calculateBonus());
        }

        findService.findById("003");
    }
}

