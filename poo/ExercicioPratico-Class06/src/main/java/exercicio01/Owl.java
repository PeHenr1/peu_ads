package exercicio01;

class Owl extends Animal {
    public Owl(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println("Pruuu Pruuu!");
    }
}
