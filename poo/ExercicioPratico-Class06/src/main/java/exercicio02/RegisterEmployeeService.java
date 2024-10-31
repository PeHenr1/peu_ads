package exercicio02;

public class RegisterEmployeeService{
    private final Repository<String, Employee> employeeRepository;

    public RegisterEmployeeService(Repository<String, Employee> employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    public void register(Employee employee) {
        if (employeeRepository.findById(employee.getId()) == null) {
            employeeRepository.save(employee);
        }
    }
}
