package exercicio01_interface;


import java.util.ArrayList;
import java.util.List;

public class Zoo {
    private List<Animal> animals;

    public Zoo() {
        this.animals = new ArrayList<>();
    }

    public void addAnimal(Animal animal) {
        animals.add(animal);
    }

    public void soundOff() {
        for (Animal animal : animals) {
            System.out.println(animal.getName() + " says: ");
            animal.makeSound();

            if (animal instanceof Runnable) {
                ((Runnable) animal).run();
            }
        }
    }
}
