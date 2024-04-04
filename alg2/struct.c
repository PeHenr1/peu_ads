#include <stdio.h>

// Exercicio 10


typedef struct{
	char nome[21];
	float notas[5];
}Aluno;

void calculaMedia(char name[21], float n[5]){
	int i;
	float media = 0;
	for(i=0;i<5;i++){
		media += n[i];
	}
	printf("Media do %s: %.2f\n",name,media / 5);
	
}

int main(){
	Aluno aluno[5];
	
	int i, j;
	for(i=0;i<5;i++){
		printf("Aluno %d: ",i+1);
		gets(aluno[i].nome);
		for(j=0;j<5;j++){
			printf("Nota %d: ",j+1);
			scanf("%f%*c",&aluno[i].notas[j]);
		}
		printf("\n");
	}
	
	
	for(i=0;i<5;i++){
		calculaMedia(aluno[i].nome,aluno[i].notas);
	}
	
	return 0;
}
