#include <stdio.h>

typedef struct{
	char nome[40];
	float nota1, nota2, media;
}Aluno;
Aluno * maiorMedia(Aluno *pv, int tam){
	int x;
	Aluno *m = &pv[0];
	for(x=1;x<tam;x++){
		if(pv[x].media > m->media)
			m = &pv[x];
	}
	// AQUI EU RETORNO O PONTEIRO
	// return *m;
	
	//AQUI EU RETORNO O ENDEREÇO DE MEMORIA
	return m;
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
		float soma = (aluno[i].nota1 + aluno[i].nota2)/2;
		aluno[i].media = soma;
	}
	
	//AQUI EU RECEBO O PONTEIRO 
	//Aluno maior = maiorMedia(aluno,quant);
	//AQUI EU RECEBO O ENDEREÇO DE MEMORIA
	Aluno *maior = maiorMedia(aluno,quant);
	
	printf("\nAluno com maior media: \n");
	printf("Nome: %s\n",maior->nome);
	printf("Nota 1: %.2f\n",maior->nota1);
	printf("Nota 2: %.2f\n",maior->nota2);
	printf("Media: %.2f\n",maior->media);
	
	return 0;
}

