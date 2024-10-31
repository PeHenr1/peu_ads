package exercicio01;

abstract class Animal {
    private final String name;

    public Animal(String name){
        this.name = name;
    }

    public abstract void makeSound();
}
