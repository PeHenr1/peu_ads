package exercicio_figure;

public final class Circle extends Figure{
    private final double radius;

    public Circle(double x, double y, double radius){
        super(x,y);
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI*(radius*radius);
    }
}
