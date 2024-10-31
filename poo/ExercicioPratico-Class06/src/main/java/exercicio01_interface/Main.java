package exercicio01_interface;

public class Main {
    public static void main(String[] args) {
        Zoo zoo = new Zoo();

        Animal lion = new Lion();
        Animal owl = new Owl();
        Animal wolf = new Wolf();

        zoo.addAnimal(lion);
        zoo.addAnimal(owl);
        zoo.addAnimal(wolf);

        zoo.soundOff();
    }
}
