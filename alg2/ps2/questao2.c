#include <stdio.h>

typedef struct{
	char nome[40];
	float nota1, nota2, media;
}Aluno;
void calculaMedia(Aluno *pv, int tam)
{
	int x;
	float soma = 0;
	for(x=0;x<tam;x++){
		soma = (pv[x].nota1 + pv[x].nota2)/2;
		pv[x].media = soma;
	}
}
int main()
{
	int quant, i;
	
	printf("Quantidade de alunos: ");
	scanf("%d%*c",&quant);
	
	Aluno aluno[quant];
	
	for(i=0;i<quant;i++){
		printf("ALUNO %d:\n",i+1);
		printf("Nome: ");
		gets(aluno[i].nome);
		printf("Nota 1: ");
		scanf("%f%*c",&aluno[i].nota1);
		printf("Nota 2: ");
		scanf("%f%*c",&aluno[i].nota2);
		printf("\n");
	}
	
	calculaMedia(aluno,quant);
	
	for(i=0;i<quant;i++){
		printf("Aluno: %s\n",aluno[i].nome);
		printf("Nota 1: %.2f\n",aluno[i].nota1);
		printf("Nota 2: %.2f\n",aluno[i].nota2);
		printf("Media: %.2f\n",aluno[i].media);
		if(aluno[i].media >= 6)
			printf("Situacao: APROVADO\n");
		else if(aluno[i].media < 4)
			printf("Situacao: REPROVADO\n");
		else
			printf("Situacao: PROVA FINAL\n");
		printf("\n");
	}
	
	return 0;
}

