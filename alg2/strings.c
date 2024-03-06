#include <stdio.h>
#include <string.h>

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
	
	int i, j;
	for(i=0;i<5;i++){
		printf("Digite um nome [%d]: ",i+1);
		gets(vetor[i]);
	}

	printf("\nDigite um letra: ");
	gets(letra);

	printf("\nNomes que contem a letra digitada:\n");
	for(i=0;i<5;i++){
		int tamanho = strlen(vetor[i]);
		for(j=0;j<tamanho;j++){
			char temp[2] = {vetor[i][j], '\0'}; //transforma o caracter em uma ''string''
			if(strcmp(letra, temp) == 0){
				printf("%s\n",vetor[i]);
				break;
			}
		}
	}

	return 0;
}
*/

// Exercicio 03 incompleto
/*
int main(){
	char palavra[20], invertida[20];
	
	printf("Digite uma palavra: ");
	gets(palavra);
	
	int tamanho = strlen(palavra)+1; // +1 pra ter espaço pro terminador
	int i; 
	for (i = 0; i < tamanho; i++) {
		char temp[2] = {palavra[tamanho - i - 1], '\0'};
		strcpy(invertida[i],temp);
    }
    invertida[tamanho] = '\0';
	
	printf("- %s -	\n",invertida);
	
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
