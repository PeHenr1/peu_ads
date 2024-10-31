package exercicio_figure;

public abstract class Figure {
    protected double x;
    protected double y;

    Figure(double x, double y){
        this.x = x;
        this.y = y;
    }

    public abstract double area();

}
