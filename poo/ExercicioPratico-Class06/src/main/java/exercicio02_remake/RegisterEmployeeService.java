package exercicio02_remake;

public abstract class RegisterEmployeeService{
    private final Repository<String, Employee> employeeRepository;

    protected RegisterEmployeeService(Repository<String, Employee> employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    public abstract void register(Employee e);
}
