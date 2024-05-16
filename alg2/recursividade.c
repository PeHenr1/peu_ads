#include <stdio.h>

// Exercicio 01
/*
int calculaSoma(int x, int y){

	if (y == 0)
		return x;
	else
		return soma(x+1,y-1);
		
}
int main(){
		
	int a,b;
	printf("Digite dois numeros: ");
	scanf("%d %d%*c",&a, &b);		
	printf("A soma de %d + %d = %d",a,b,calculaSoma(a,b));
		
	return 0;
}
*/

// Exercicio 02
/*
int calcula(int x){
	if (x == 0){
		//printf("%d\n",x);
		return x;
	}
		
	//printf("%d + ",x);
	return x + calcula(x-1);
}
int main(){
		
	int a;
	printf("Digite um numero: ");
	scanf("%d%*c",&a);	
	printf("Soma dos numeros = %d",calcula(a));
		
	return 0;
}
*/

// Exercicio 03
/*
int potencia(int x, int y){
	if (x == 0)
		return 0;
	if (y == 1)
		return y;
	if (y == 0)
		return 1;
	
	
	return x * potencia(x,y-1);
}
int main(){
		//VERIFICAR SE A É MAIOR QUE ZERO !!corrigir
	int a, b;
	printf("Digite um numero (base): ");
	scanf("%d%*c",&a);
	printf("Digite outro numero (potencia): ");
	scanf("%d%*c",&b);	
	printf("%d elevado a %d = %d",a,b,potencia(a,b));
		
	return 0;
}
*/
