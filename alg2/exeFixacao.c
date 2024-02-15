#include <stdio.h>
#include <math.h>

// Exercício 01
/*
int main(){
	printf("%d", 1 > 2);
	printf("\n%d", 3 == 2);
	printf("\n%d", 3 >= 2);
	printf("\n%d", 'a' < 'b');
	printf("\n%d", '1' == '1');
	printf("\n%d", 'j' != 'j');
}
*/

// Exercicio 02
/*
int main(){
	int a=1, b=2, c=3;
	printf("Os numeros sao: %d %d %d\n", a, b, c);
}
*/

// Exercicio 03
/*
int main(){
	int x = 1, y = 10;
	printf("%d",x+++y);
}
*/

// Exercicio 04
/*
int main(){
	int j = 3, k;
	k = j == 3; // K receve 0 ou 1, pois "verifica" se o j==3 é T ou F
	printf("%d",k);
}
*/

// Exercicio 05
int main(){
	printf("Arredondar pra cima: %lf\n", ceil(3.2));
	printf("Arredondar pra baixo: %lf\n", floor(3.2));
	
	int n1;
	printf("\nDigite um numero: ");
	scanf("%d%*c",&n1);
	printf("Raiz quadrada do nº digitado: %lf\n", sqrt(n1));
	
	int n2;
	printf("\nDigite um numero: ");
	scanf("%d%*c",&n2);
	printf("Raiz cubica do nº digitado: %lf\n", cbrt(n2));
	
	printf("\nCos de um angulo de 2 radianos: %lf\n",cos(2));
	printf("Sin de um angulo de 2 radianos: %lf\n",sin(2));
	printf("Tan de um angulo de 2 radianos: %lf\n",tan(2));
	
	printf("\nLog de 100 na base 10: %lf\n", log10(100));
	printf("Log de 2.718281828459 na base e: %lf\n", log(2.718281828459)); //numero euler
	
	int x, y;
	printf("\nX: ");
	scanf("%d%*c",&x);
	printf("Y: ");
	scanf("%d%*c",&y);
	printf("X elevado a Y: %lf\n", pow(x,y));
	
	printf("Valor de PI: %lf\n\n", M_PI);
	
	//modf
	double X = 3.14;
	double Y;
	double Z = modf(X, &Y);
	printf("X = %lf | Y = %lf | Z = %lf \n",X, Y, Z); // Z recebe o resto e Y a parte inteira
	
}

