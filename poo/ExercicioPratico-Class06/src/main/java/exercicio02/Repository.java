package exercicio02;

public interface Repository <T, E>{
    void save(E entity);
    E findById(T type);
}
