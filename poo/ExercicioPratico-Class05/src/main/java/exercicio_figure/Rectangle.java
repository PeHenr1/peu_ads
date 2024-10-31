package exercicio_figure;

public final class Rectangle extends Figure {
    private final double width;
    private final double length;

    public Rectangle(double x, double y){
        super(x,y);
        this.width = x;
        this.length = y;
    }

    @Override
    public double area() {
        return width*length;
    }
}
