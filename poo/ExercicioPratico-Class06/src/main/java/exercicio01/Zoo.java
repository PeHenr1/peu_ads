package exercicio01;

public class Zoo {
    private final Animal[] cages;
    private int cont;

    public Zoo() {
        this.cages = new Animal[10];
        cont = 0;
    }

    public void addAnimal(String name){
        switch (name){
           case "Owl" ->  cages[cont++] = new Owl(name);
           case "Lion" -> cages[cont++] = new Lion(name);
           case "Wolf" -> cages[cont++] = new Wolf(name);
        }
    }

    public void soundOff() {
        for (Animal animal : cages) {
            if (animal != null) {
                animal.makeSound();
                if (animal instanceof Lion) {
                    ((Lion) animal).run();
                }
                if (animal instanceof Wolf) {
                    ((Wolf) animal).run();
                }
            }
        }
    }

}
