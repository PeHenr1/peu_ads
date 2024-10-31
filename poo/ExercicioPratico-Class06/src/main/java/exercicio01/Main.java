package exercicio01;

public class Main {
    public static void main(String[] args) {
        Zoo zoo = new Zoo();

        zoo.addAnimal("Owl");
        zoo.addAnimal("Wolf");
        zoo.addAnimal("Owl");
        zoo.addAnimal("Lion");
        zoo.addAnimal("Owl");
        zoo.addAnimal("Wolf");
        zoo.addAnimal("Owl");
        zoo.addAnimal("Lion");
        zoo.addAnimal("Wolf");
        zoo.addAnimal("Lion");

        zoo.soundOff();
    }
}
