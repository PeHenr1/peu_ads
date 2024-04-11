#include <stdio.h>

// Exercicio 01
/*
int main(){
	int n = 2;
	int *PN = &n;
	printf("Valor: %d // Endereco: %ld\n", *PN, (long)PN);

	return 0;
}
*/

// Exercicio 02
int tamanho(char *P){
	int cont = 0;
	while(*P != '\0'){
		P++;
		cont++;
	}
	return cont;
}
int main(){
	char c[] = "padaroca";
	printf("Tamanho da string: %d",tamanho(c));
	
	return 0;
}
