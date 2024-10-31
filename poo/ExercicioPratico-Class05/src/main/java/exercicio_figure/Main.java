package exercicio_figure;

public class Main {
    public static void main(String[] args) {
        Circle circle = new Circle(0, 0, 5);
        System.out.println("Area of Circle: " + circle.area());

        Rectangle rectangle = new Rectangle(4, 6);
        System.out.println("Area of Rectangle: " + rectangle.area());

        Triangle triangle = new Triangle(0, 0, 3, 4, 5);
        System.out.println("Area of Triangle: " + triangle.area());
    }
}
