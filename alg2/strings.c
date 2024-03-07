#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Exercicio 01
/*
int main(){
	char vetor[5][20];
	
	int i, j;
	for(i=0;i<5;i++){
		printf("Digite um nome [%d]: ",i+1);
		gets(vetor[i]);
	}
	
	char aux[20];
	
	for(i=0;i<5;i++){

		for(j=0;j<5;j++){
			
			if( strcmp(vetor[i],vetor[j]) < 0 ){
				strcpy(aux,vetor[j]);
				strcpy(vetor[j],vetor[i]);
				strcpy(vetor[i],aux);
			}
		}
	}
	
	printf("\n CRESCENTE \n");
	for(i=0;i<5;i++){
		printf("Nome %d: %s\n",i+1,vetor[i]);
	}
	
	return 0;
}
*/

// Exercicio 02
/*
int main(){
	char vetor[5][20], letra[2];
	
	int i, j, flag = 0;
	for(i=0;i<5;i++){
		printf("Digite um nome [%d]: ",i+1);
		gets(vetor[i]);
	}

	printf("\nDigite um letra: ");
	gets(letra);

	for(i=0;i<5;i++){
		int tamanho = strlen(vetor[i]);
		for(j=0;j<tamanho;j++){
			char temp[2] = {vetor[i][j], '\0'}; //transforma o caracter em uma ''string''
			if(strcmp(letra, temp) == 0){
				printf("- %s\n",vetor[i]);
				flag = 1;
				break;
			
			}
		}
	}
	if(!flag) 
		printf("Letra nao encontrada!");


	return 0;
}
*/

// Exercicio 03 
/*
int main(){
	char palavra[20], invertida[20];
	int i, tamanho, destino; 
	
	
	printf("Digite uma palavra: ");
	gets(palavra);
	tamanho = strlen(palavra); 
	
	for(i=0; i<tamanho;i++ ){
		destino = (tamanho-1) - i;
		invertida[destino] = palavra[i];
	}
    invertida[tamanho] = '\0';
	printf("Original: %s\nInvertida: %s\n",palavra,invertida);
	
	if( strcmp(palavra,invertida) == 0 )
		printf("Palindromo!!!");
	else
		printf("Nao e palindromo!!!");
		
	
	return 0;
}
*/

// Exercicio 04
/*
int main()
{
	char nome[20];
	int cont = 0, i = 0;
	
	printf("Digite um nome: ");
	gets(nome);
	
	while(cont != 4){
		if( isspace(nome[i]) == 0 ){
			printf("%c",nome[i]);
			cont++;
		}
		else
			printf("%c",nome[i]);
		i++;
	}
	return 0;
}
*/

// Exercicio 05
/*
int main()
{
	char nome[20];
	int i, tam = 0;
	
	printf("Digite um nome: ");
	gets(nome);
	int tamanho = strlen(nome);
	
	for(i=0;i<tamanho;i++)
		if( isspace(nome[i]) == 0 )
			tam++;

	printf("O nome digitado tem %d letras",tam);
		
	return 0;
}
*/

// Exercicio 06
/*
int main(){
	char nome[20];
	char sobrenome[20];
	char completo[40];
	int i, tam = 0;
	
	printf("Digite um nome: ");
	gets(nome);
	printf("Digite um sobrenome: ");
	gets(sobrenome);
	
	strcpy(completo,nome);
	strcat(completo," ");
	strcat(completo,sobrenome);
		
	printf("\nNome completo: %s\n",completo);	
	
	int tamanho = strlen(completo);
	for(i=0;i<tamanho;i++)
		if( isspace(completo[i]) == 0 )
			tam++;

	printf("O nome digitado tem %d letras\n",tam);
	printf("Primeiro letra do nome: %c\n",completo[0]);
	printf("Ultima letra do nome: %c\n",completo[tamanho-1]);
	
	return 0;
}
*/

// Exercicio 07
/*
int main(){
	char nome[40];
	int i;
	
	printf("Digite um nome: ");
	gets(nome);
	int tamanho = strlen(nome);
	
	for(i=0;i<tamanho;i++){
		nome[i] = tolower(nome[i]);
	}
	printf("\nNome minusculo: %s\n",nome);
	
	for(i=0;i<tamanho;i++){
		nome[i] = toupper(nome[i]);
	}
	printf("\nNome maiusculo: %s\n",nome);
	
	return 0;
}
*/
