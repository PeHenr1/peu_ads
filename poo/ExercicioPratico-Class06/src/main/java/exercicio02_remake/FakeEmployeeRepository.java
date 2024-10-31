package exercicio02_remake;

public class FakeEmployeeRepository<K, E> implements Repository<K, E>{



    @Override
    public void toSave(E e) {

    }

    @Override
    public E findById(String id) {
        for (E e : elements) {
            final Employee employee = (Employee) e;
            if (e != null && e.getId().equals(id)) {
                return employee;
            }
        }
        return null;
    }
}
