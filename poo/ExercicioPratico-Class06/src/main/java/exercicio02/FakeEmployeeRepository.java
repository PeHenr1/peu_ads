package exercicio02;

public class FakeEmployeeRepository implements Repository<String, Employee> {
    private final Employee[] employees;
    private int index;

    public FakeEmployeeRepository() {
        this.employees = new Employee[10];
        this.index = 0;
    }

    @Override
    public void save(Employee employee) {
        if (index < employees.length) {
            employees[index++] = employee;
        }
    }

    @Override
    public Employee findById(String id) {
        for (Employee employee : employees) {
            if (employee != null && employee.getId().equals(id)) {
                return employee;
            }
        }
        return null;
    }
}
