#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Exercicio 01
/*
int main(){
	int n = 2;
	int *PN = &n; 
	// PN recebe o endereço de n
	// *PN recebe é o conteudo do endereço em PN 
	printf("Valor: %d // Endereco: %ld\n", *PN, (long)PN);

	return 0;
}
*/

// Exercicio 02
/*
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
	printf("Tamanho da string '%s' e: %d",c,tamanho(c));
	
	return 0;
}
*/

// Exercicio 03 
/*
int soma(int *pa, int tam){
	int s = 0, i;
	for(i=0;i<tam;i++){
		s += pa[i];     
		// *pa é o ponteiro do primeiro elemento 
		// pa é o endereço do elemento
		// p[i] é o elemento 
	}
	return s;
}
int main(){
	int array[] = {1,2,3,4,5};
	int tamanho = 5;
	int r = soma(array,tamanho);   //passando o numero vc ja recebe o endereço inicial do array
	
	printf("A soma dos elementos eh: %d.",r);

	return 0;
}
*/

// Exercicio 04
/*
int  * maiorN(int *pa, int tam){
	int i, pos = 0;
	for(i=0;i<tam;i++){
		if(pa[i] > pa[pos])
			pos = i	;
	}
	return &pa[pos]; //retorna o ENDEREÇO DE MEMORIA onde ta o maior valor
}
int main(){
	int array[] = {10,5,88,2,3};
	int tamanho = 5;
	
	int *maior = maiorN(array,tamanho); //armazena o endereço  
	printf("O maior elemento do array eh: %d.",*maior); //mostra o valor no endereço 
	
	return 0;	
}
*/

// Exercicio 05
/*
char * maiuscula(char *pa, int tam){
	int i;
	
	for(i=0;i<tam;i++){
		if( isupper(pa[i]) )
			return &pa[i];
	}

	return NULL;
}
int main(){
	char text[] = "bom dia princesa pOr favoR sente na glock";
	int tamanho = strlen(text);
	
	char *maiusc = maiuscula(text, tamanho);	
	printf("A primeira letra maiuscula eh: '%c'.",*maiusc);
	
	return 0;
}
*/

// Exercicio 08
/*
void inverso(int *pa, int tam){
	int i;
	for(i = tam-1; i>=0 ;i--){
		printf("%d ",*(pa+i));
	}
}
int main(){
	int vetor[] = {1,2,3,4,5};
	int tamanho = 5;
	inverso(vetor,tamanho);
	
	return 0;
}
*/
