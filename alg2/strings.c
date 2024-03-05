#include <stdio.h>
#include <string.h>

// Exercicio 01
int main(){
	char vetor[3][20];
	
	int i, j;
	for(i=0;i<3;i++){
		printf("Digite um nome [%d]: ",i+1);
		gets(vetor[i]);
	}
	
	char aux[20];
	
	for(i=0;i<3;i++){

		for(j=0;j<3;j++){
			
			if( strcmp(vetor[i],vetor[j]) < 0 ){
				strcpy(aux,vetor[j]);
				strcpy(vetor[j],vetor[i]);
				strcpy(vetor[i],aux);
	
			}
			
		}
	
	}
	
	printf("\n CRESCENTE \n");
	for(i=0;i<3;i++){
		printf("Nome %d: %s\n",i+1,vetor[i]);
	}
	
	
	
	
	
	
	
	return 0;
}
