package exercicio02_remake;

public interface Repository<K, E> {
    void toSave(E entity);
    E findEntityById(K key);
}
