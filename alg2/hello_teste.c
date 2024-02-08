#include <stdio.h>

/*
 * int main() {
	float var;
	
	for(var = 0.0; var < 15; var = var + 0.7){
		printf("%f\n", var );
	}
	
	return 0;
}
*/

int main() {
	int idade;
	float salario;
	double x;
	
	char nome[10];  

	printf("Digite uma idade: ");
	scanf("%d%*c", &idade);
	printf("Digite um salario: ");
	scanf("%f%*c", &salario);
	printf("Digite um valor para X: ");
	scanf("%lf%*c", &x);
	
	printf("Digite um nome: \n");
	gets(nome);
	
	printf("Idade: %d \n", idade);
	printf("Salario: %f \n", salario);
	printf("x: %lf \n", x);
	printf("Nome: %s \n", nome);

	return 0;
}
