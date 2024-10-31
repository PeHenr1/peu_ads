package exercicio01_interface;

public class Owl implements Animal {
    private final String name;

    public Owl() {
        this.name = "Owl";
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void makeSound() {
        System.out.println("Pruuu Pruuu!");
    }
}
