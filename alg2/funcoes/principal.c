#include <stdio.h>

#include "prototipos.h"
#include "funcoes.c"

// pode fazer o principal, inicializa e funcoes tudo junto
// em um unico arquivo, separa só pra organizar

// poderia inicializar a funcao aqui "protótipo"
// dai só cria com os tipos das variaveis
	// float media(int, int);
// dai depois vc criar ela
	// float media(int n1, int n2){...}
	

//funcao do exercicio 08 (6)
float somaValores(float vetF[],int tam){
	int i;
	float soma = 0;
	for(i=0;i<tam;i++){
		soma += vetF[i];
	}
	return soma;
}


//funcao do exercicio 09 (7)
float mult(int n1,float n2){
	return n1*n2;
}

//funcao do exercicio 10 (8)
int tamanho(char texto[30]){
	int tam = strlen(texto);
	return tam;
}

//struct e funcao do exercicio 11(9)
typedef struct{
	char titulo[30];
	char autor[30];
	int ano;
}Livro;	
void imprimeDados(Livro liv){
	printf("Titulo: %s",liv.titulo);
	printf("\nAutor: %s",liv.autor);
	printf("\nAno de lancamento: %d\n",liv.ano);
}

//struct e funcao do exercicio 12(10)
struct Conta{
	int numero;
	char titular[30];
	float saldo;
};
struct Conta maiorSaldo(struct Conta c1, struct Conta c2){
	if(c1.saldo > c2.saldo)
		return c1;
	else
		return c2;
}


int main(){
	// Exercicio 01
	// mensagem();
	
	// Exercicio 02
	/*
	int a, b;
	printf("\nDigite dois numeros: ");
	scanf("%d %d%*c",&a,&b);
	soma(a, b);
	*/
	
	// Exercicio 03
	/*
	typedef char String[21];
	String t1, t2;
	printf("Digite uma palavra: ");
	gets(t1);
	printf("Digite outra palavra: ");
	gets(t2);
	concatena(t1,t2);
	*/
	
	// Exercicio 04
	/*
	int vetor[] = {1,9,3,2,4,11};
	printf("O maior valor foi: %d.\n",maiorNum(vetor));
	*/
	
	// Exercicio 05 
	/*
	int a = 3, b = 7;
	int mDois = maiorEntreDois(a, b);
	printf("O maior entre os dois %d e %d e: %d",a,b,mDois);
	*/
	
	// Exercicio 06
	/*
	float notas[] = {1.5,9.3,3.2,2.9,10};
	media(notas);
	*/
	
	// Exercicio 07
	/*
	int vetor[] = {1,9,3,2,1,11,1};
	int n = 1;
	int retorno = vezesAparece(vetor, n);
	printf("O numero %d aparece %d vezes.\n",n,retorno);
	*/
	
	// Exercicio 08 (06)
	/*
	float vetor[] = {1.5,9.5,3.5,2.5,1.0};
	float s = somaValores(vetor, 5);
	printf("A soma dos valores do vetor eh: %.2f\n",s);
	*/
	
	// Exercicio 09 (07)
	/*
	int i = 3;
	float f = 2.5;
	float r = mult(i,f);
	printf("A multiplicacao dos valores eh: %.2f\n",r);
	*/
	
	// Exercicio 10 (08)
	/*
	char str[30];
	printf("Digite uma string: ");
	gets(str);
	
	int t = tamanho(str);
	printf("O tamanho da string digitada eh: %.d\n",t);
	*/
	
	// Exercicio 11 (09)
	/*
	Livro livro = {"Heartstopper", "Alice Oseman", 2021};
	imprimeDados(livro);
	*/
	
	// Exercicio 12 (10)
	/*
	struct Conta conta1 = {123, "João", 1000.50};
	struct Conta conta2 = {456, "Maria", 500.25};
	struct Conta contaMaior = maiorSaldo(conta1, conta2);
	
	printf("Conta com maior saldo:\n");
	printf("Numero da conta: %d\n", contaMaior.numero);
	printf("Titular: %s\n", contaMaior.titular);
	printf("Saldo: %.2f\n", contaMaior.saldo);
	*/
	
	
}
