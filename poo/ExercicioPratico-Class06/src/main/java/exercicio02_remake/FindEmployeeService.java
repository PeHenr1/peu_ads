package exercicio02_remake;

public abstract class FindEmployeeService {
    private final Repository<String, Employee> employeeRepository;

    public FindEmployeeService(Repository<String, Employee> employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    public abstract void findById(String id);
}
