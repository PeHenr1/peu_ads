#include <stdio.h>

/*
int main(){
	int i;
	
	for (i=0; i<=20; i++)
	{
		if(i >= 8 && i <= 14 )
		{
			printf("Nao vou exibir...\n");
			continue; //pula o print e vai direto pra proxima repetição
		}
		
		printf("Valode de i: %d\n",i);
	}
}
*/

// Exercicio 01
/*
int main(){
	int time = 1;
	float mediaAltura, oitenta;
	do{
		printf("\nTIME %d:\n",time);
		int menorD = 0;
		float mediaIdade = 0;
		
		int jogador;
		for(jogador = 0; jogador < 2; jogador++){
			int idade = 0;
			float peso = 0, altura = 0;
			
			printf("Idade: ");
			scanf("%d%*c",&idade);
			printf("Peso: ");
			scanf("%f%*c",&peso);
			printf("Altura (m): ");
			scanf("%f%*c",&altura);
			printf("\n");
			
			if(idade < 18){
				menorD += 1;
			}
			
			mediaIdade += idade;
			mediaAltura += altura;
			
			if(peso > 80){
				oitenta += 1;
			}
		}
		printf("Ha %d jogadores menores de 18 anos nesse time.\n",menorD);
		
		mediaIdade = mediaIdade/2;
		printf("Idade media do time: %f\n",mediaIdade);
		
		time++;
	}while(time<=2);
	
	mediaAltura = mediaAltura/4;
	printf("\nAltura media entre os times: %f\n",mediaAltura);
	
	oitenta = (oitenta/4)*100;
	printf("Porcentagem de alunos com +80kg: %f \n",oitenta);	
}
*/


// Exercicio 02
// FOR
/*
int main(){
	int num, div, flag;
	printf("Digite um número maior que 1: ");
	scanf("%d%*c",&num);

	if(num == 2)
		printf("2 eh um número primo!\n");
	else{
		flag = 0;
		
		for(div=2; div<num; div++){
			if(num % div == 0)
				flag = 1;
		}
		
		if(flag == 0)
			printf("%d e um numero primo\n",num);
		else
			printf("%d nao e um numero primo\n",num);
	}
	return 0;
}
*/

//WHILE
/*
int main(){
	int num, div, flag;
	printf("Digite um número maior que 1: ");
	scanf("%d%*c",&num);

	if(num == 2)
		printf("2 eh um número primo!\n");
	else{
		flag = 0;
		div = 2;
		
		while(div < num){
			if(num % div == 0)
				flag = 1;
			div++;
		}
		
		if(flag == 0)
			printf("%d e um numero primo\n",num);
		else
			printf("%d nao e um numero primo\n",num);
	}
	return 0;
}
*/

//DO...WHILE
/*
int main(){
	int num, div, flag;
	printf("Digite um número maior que 1: ");
	scanf("%d%*c",&num);

	if(num == 2)
		printf("2 eh um número primo!\n");
	else{
		flag = 0;
		div = 2;
		
		do{
			if(num % div == 0)
				flag = 1;
			div++;
		}while(div != num);
		
		if(flag == 0)
			printf("%d e um numero primo\n",num);
		else
			printf("%d nao e um numero primo\n",num);
	}
	return 0;
}
*/

// Exercicio 03
/*
int main(){
	int i = 1;
	do{
		printf("TABUADA DO %d:\n",i);
		int m;
		for(m=1; m <= 10; m++){
			printf("%d x %d = %d\n",i,m,i*m);
		}
		i++;
		printf("\n");
	}while(i<=10);	
}
*/

// Exercicio 04
/*
int main(){
	int n, f = 1;
	printf("Digite um numero inteiro: ");
	scanf("%d%*c",&n);
	
	if(n > 0){
		while(n != 0){
			f = f * n;
			n--;
		}
		printf("Fatorial do numero digitado: %d",f);	
	}
	else
		printf("Ignorar-lo-ei...");
}
*/

// Exercicio 05
/*
int main(){
	int mSeis = 0, meio = 0, mQuatro = 0;
	float n ;
	
	printf("Digite uma nota: ");
	do{
		scanf("%f%*c",&n);
		
		if(n >= 6){
			mSeis++;
		}
		else{
			if(n < 4){
				mQuatro++;
			}
			else{
				meio++;
			}
		}
		
		printf("Digite uma nota: ");
	}while(n >= 0);
	
	printf("\nDas notas digitadas:\n");
	printf("%d sao maiores ou iguais a 6\n",mSeis);
	printf("%d estao entre 4 e 6\n",meio);
	printf("%d sao menores que 4\n",mQuatro);
}
*/

// Exercicio 06
/*
int main(){
	int n;
	int num=1, den=1, i;
	float valor, soma;
	printf("Digite um numero inteiro: ");
	scanf("%d%*c",&n);
	
	printf("S = ");
	for(i=0; i < n; i++){

		if(i != n-1)
			printf("%d/%d + ",num,den);
			
		else
			printf("%d/%d ",num,den);
			
			
		valor = (float) num/den;
		soma += valor;
		
		num++;
		den+=2;
	}
	printf("= %f",soma);
	return 0;
}
*/

// Exercicio 07
/*
int main(){
	int n;
	int Fi=0, ant=1, antant=0;
	
	printf("Digite um numero inteiro: ");
	scanf("%d%*c",&n);
	
	if(n > 0){
		while(n != 0){
			Fi = Fi + antant;
			antant = ant;
			ant = Fi;
			n--;
			printf("%d ",Fi);
		}
	}
	else{
		printf("Numero digitado invalido!");
	}
	return 0;
}
*/
