#include <stdio.h>
#include <math.h>



// Exercicio 06
int main(){
	float x, y, z;
	printf("Digite nº para os lados de um triângulo... \nX: ");
	scanf("%f%*c",&x);
	printf("Y: \n");
	scanf("%f%*c",&y);
	printf("Z: \n");
	scanf("%f%*c",&z);
	
	if(x+y<z && x+z<y && y+z<x){
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
		printf("Não forma um triangulo valido.\n");
	
}
