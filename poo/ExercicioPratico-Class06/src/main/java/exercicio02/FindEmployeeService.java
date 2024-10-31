package exercicio02;

public class FindEmployeeService {
    private final Repository<String, Employee> employeeRepository;

    public FindEmployeeService(Repository<String, Employee> employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    public Employee findById(String id) {
        return employeeRepository.findById(id);
    }
}
