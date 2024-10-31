package exercicio01_interface;

public class Wolf implements Runnable {
    private final String name;

    public Wolf() {
        this.name = "Wolf";
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void makeSound() {
        System.out.println("Auuuuuu!");
    }

    @Override
    public void run(){
        System.out.println("Wolf is running!");
    }
}
