#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
	int i, j, alunos, disciplinas;
	
	do{
		printf("Quantidade de alunos: ");
		scanf("%d%*c",&alunos);
		
		if(alunos<=0)
			printf("Invalido... Digite um numero maior que zero.\n");
			
	}while(alunos<=0);
	
	do{
		printf("Quantidade de disciplinas: ");
		scanf("%d%*c",&disciplinas);
		
		if(disciplinas<=0)
			printf("Invalido... Digite um numero maior que zero.\n");
			
	}while(disciplinas<=0);
	
	float matriz[alunos][disciplinas];
	
	// cria array
	for(i=0;i<alunos;i++){
		for(j=0;j<disciplinas;j++){
			do{
				printf("Digite as notas do aluno %d na disciplina %d: ",i+1,j+1);
				scanf("%f%*c",&matriz[i][j]);
				
				if (matriz[i][j] < 0 || matriz[i][j] > 10) {
                    printf("Nota inválida. Digite uma nota entre 0 e 10.\n");
                }
			}while(matriz[i][j]<=0);
		}
		printf("\n");
	}
	
	//calcula media alunos
	printf("\nMedias dos alunos: \n");
	for(i=0;i<alunos;i++){
		float mediaAluno = 0;
		for(j=0;j<disciplinas;j++){
			mediaAluno += matriz[i][j];
		}
		mediaAluno = mediaAluno/disciplinas;
		printf("Aluno %d: %.2f\n",i+1,mediaAluno);
	}
	
	//calcula media disciplinas
	printf("\nMedias das disciplinas: \n");
	for(j=0;j<disciplinas;j++){
		float mediaDisc = 0;
		for(i=0;i<alunos;i++){
			mediaDisc += matriz[i][j];
		}
		mediaDisc = mediaDisc/alunos;
		printf("Disciplina %d: %.2f\n",j+1,mediaDisc);
	}
	
	return 0;
}
