package exercicio_figure;

public final class Triangle extends Figure {
    private final double a;
    private final double b;
    private final double c;

    public Triangle(double x, double y, double a, double b, double c){
        super(x,y);
        this.a = a;
        this.b = b;
        this.c = c;
    }

    @Override
    public double area() {
        double s = (a + b + c) / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}
