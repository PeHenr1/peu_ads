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
/*
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
*/


// Exercicio 06
/*
int main(){
	float x, y, z;
	printf("Digite numero para os lados de um triangulo... \nX: ");
	scanf("%f%*c",&x);
	printf("Y: ");
	scanf("%f%*c",&y);
	printf("Z: ");
	scanf("%f%*c",&z);
	
	if(x+y>z && x+z>y && y+z>x){
		printf("Triangulo valido.\n");
		if(x==y && y==z)
			printf("Triangulo equilatero");
		else
			if(x==y || x==z || y==z)
				printf("Triangulo isosceles");
			else
				printf("Triangulo escaleno");
	}
	else
		printf("Nao forma um triangulo valido.\n");
}
*/

// Exercicio 07
/*
int main(){
	int a, b, c;
	printf("A: ");
	scanf("%d%*c",&a);
	printf("B: ");
	scanf("%d%*c",&b);
	printf("C: ");
	scanf("%d%*c",&c);
	
	
	if(a == 0)
		printf("O valor de A nao pode ser 0, saindo...");
	else
	{
		double delta = ((b*b)-(4*a*c));
		
		if (delta < 0)
			printf("Nao ha raizes...");
		else
		{
			if(delta == 0)
			{
				double x = (-1*b + 0)/(2*a); // + ou - raiz de delta = 0
				printf("Ha apenas uma raiz/x...\n");
				printf("X: %lf",x);
			}
			else
			{
				double x1 = ( (-1*b) + sqrt(delta) )/(2*a);
				double x2 = ( (-1*b) - sqrt(delta) )/(2*a);
				
				printf("Ha duas raizes...\n");
				printf("X1: %lf e X2: %lf",x1,x2);
			}
		}
	}
	
}
*/

// Exercicio 08
int main(){
	int n1, n2, opc;
	double e, r, rq1, rq2, rc1, rc2;
	
	printf("Digite um numero: ");
	scanf("%d%*c",&n1);
	printf("Digite outro numero: ");
	scanf("%d%*c",&n2);
	
	printf("\n1. Primeiro numero elevado ao segundo numero\n");
	printf("2. Raiz quadrada de cada numero\n");
	printf("3. Raiz cubica de cada numero\n");
	printf("4. Produto dos numeros\n\n");
	
	printf("Selecione uma opcao: ");
	scanf("%d%*c",&opc);
	
	switch(opc){
		case 1:
			e = pow(n1,n2);
			printf("%d elevado a %d = %lf",n1,n2,e);
			break;
		
		case 2:
			rq1 = sqrt(n1);
			rq2 = sqrt(n2);
			printf("Raiz quadrada de %d: %lf\n",n1,rq1);
			printf("Raiz quadrada de %d: %lf\n",n2,rq2);
			break;
			
		case 3:
			rc1 = cbrt(n1);
			rc2 = cbrt(n2);
			printf("Raiz cubica de %d: %lf\n",n1,rc1);
			printf("Raiz cubica de %d: %lf\n",n2,rc2);
			break;
			
		case 4:
			r = n1 * n2; 
			printf("O produto de %d x %d e: %lf\n",n1,n2,r);
			break;
			
		default:
			printf("Opcao digitado invalida");
			break;
	}	
}
