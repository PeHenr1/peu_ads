package exercicio01_interface;


public class Lion implements Runnable {
    private final String name;

    public Lion() {
        this.name = "Lion";
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void makeSound() {
        System.out.println("Rrrrrwaarrr!");
    }

    @Override
    public void run() {
        System.out.println("Lion is running!");
    }
}
