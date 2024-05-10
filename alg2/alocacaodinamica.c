#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Exercicio 01
/*
char * concatena(char *str1, char *str2){
	int tamanho = strlen(str1) + strlen(str2);
	
	char *strCon = (char*) malloc(tamanho+1);
	
	if(strCon == NULL){
		printf("Erro ao alocar memoria\n");
		exit(1);
	}
	
	strcpy(strCon,str1);
	strcat(strCon,str2);
	
	return strCon;
}

int main(){
	char s1[20];
	char s2[20];
	
	printf("Digite o texto 1: ");
	gets(s1);
	printf("Digite o texto 2: ");
	gets(s2);
	
	char *strConcatenada = concatena(s1,s2);
	
	printf("Strings concatenadas: %s\n",strConcatenada);
		
	free(strConcatenada);
	
	return 0;
}
*/

// Exercicio 02
/*
int main(){
	int quant, i;
	
	printf("Quantas strings deseja digitar: ");
	scanf("%d%*c",&quant);
	
	char **vetor = (char**) malloc (quant * sizeof(char *));
	if(vetor == NULL){
		printf("Erro ao alocar memoria\n");
		exit(1);
	}
		
	for(i=0;i<quant;i++){
		char string[100];
		printf("STRING %d: ",i+1);
		gets(string);
		
		vetor[i] = (char *) malloc (strlen(string) + 1);
		
		if(vetor[i] == NULL){
			printf("Erro ao alocar memoria\n");
			exit(1);
		}
		
		strcpy(vetor[i], string);
	}
	
	printf("\nAs strings digitadas foram:\n");
	for(i=0;i<quant;i++){
		printf("%d: %s\n",i+1,vetor[i]);
	}
	
	// liberando memoria (nao precisa, o programa faz sozinho
	for(i=0;i<quant;i++){
		free(vetor[i]);
	}
	free(vetor);
		
	return 0;
}	
*/

// Exercicio 03
/*
char * endereco(char *p){
	char *espaco = p;
	
	//admitindo que sempre havera um espaço em branco
	while(*espaco != ' '){espaco++;}
	espaco++; //pq a segunda palavra começa após o espaço em branco
	
	int tam = strlen(espaco);
	
	char *segundaP = (char *) malloc (tam + 1);
	
	if(segundaP != NULL){
		strcpy(segundaP, espaco);
	}
	else{
		printf("Erro ao alocar memoria\n");
		exit(1);
	}
	
	return segundaP;
}

int main(){
	char input[100];
	
	printf("Digite duas palavras separadas por espaco: ");
	gets(input);
	
	char *segundap = endereco(input);
	
	printf("\nEndereco da segunda palavra: %p\n",segundap);
	printf("Segunda palavra: %s\n",segundap);
	
	free(segundap);
	
	return 0;
}
*/

// Exercicio 04
/*
void tratarErro(void * end){
	if(end == NULL){
		printf("Erro de alocacao. Saindo...\n");
		exit(1);
	}
}
char * digitarLetras(){
	int quant = 0;
	
	//vamos admitir que haverá pelo menos 1 letra
	char *string = (char *) malloc (1);
	tratarErro(string);
	
	char caractere = getchar(); //pega a primeira letra e coloca na area
	string[quant] = caractere;
	quant++;
	
	caractere = getchar();
	while(caractere != '\n'){
		string = realloc(string,quant+1);
		tratarErro(string);
		string[quant] = caractere;
		quant++;
		caractere = getchar();
	}
	
	string = realloc(string,quant+1);
	tratarErro(string);
	string[quant] = '\0';
	
	return string;
}
int main(){
	char *str = digitarLetras();
	printf("String digitada: %s",str);
	free(str);
	
	return 0;
}
*/

// Exercicio 05
/*
int *criarInteiro(){
	int *ptr = (int *) malloc (sizeof(int));
	if(ptr == NULL){
		printf("Erro de alocacao. Saindo...\n");
		exit(1);
	}
	
	printf("Digite um numero inteiro: ");
	scanf("%d%*c",ptr);
	
	return ptr;
}
int main(){
	int *intP = criarInteiro();
	printf("\nEndereco de memoria: %p\n",intP);
	printf("Conteudo: %d\n",*intP);
	free(intP);
	
	return 0;
}
*/

// Exercicio 06

typedef struct{
	char nome[100];
	float nota1, nota2;
}Aluno;
typedef struct{
	char nome[100];
	int qtdeAlunos;
	Aluno *alunos;
}Disciplina;

int main(){
	int n, i, j;
	printf("Quantas disciplinas deseja criar?: ");
	scanf("%d%*c",&n);
	
	Disciplina *disciplinas = (Disciplina *) malloc (n * sizeof(Disciplina));
	if(disciplinas == NULL){
		printf("Erro de alocacao. Saindo...\n");
		exit(1);
	}
	
	for(i=0;i<n;i++){
		printf("DISCIPLINA %d\n",i+1);
		printf("Nome: ");
		gets(disciplinas[i].nome);
		
		printf("Quantidade de alunos na disciplina - %s: ",disciplinas[i].nome);
		scanf("%d%*c",&disciplinas[i].qtdeAlunos);
		
		disciplinas[i].alunos = (Aluno *) malloc (disciplinas[i].qtdeAlunos * sizeof(Aluno));
		if(disciplinas[i].alunos == NULL){
			printf("Erro de alocacao. Saindo...\n");
			exit(1);
		}
		
		for(j=0;j<disciplinas[i].qtdeAlunos;j++){
			printf("Nome do aluno %d: ",j+1);
			gets(disciplinas[i].alunos[j].nome);
			printf("Nota 1 de %s: ",disciplinas[i].alunos[j].nome);
			scanf("%f%*c",&disciplinas[i].alunos[j].nota1);
			printf("Nota 2 de %s: ",disciplinas[i].alunos[j].nome);
			scanf("%f%*c",&disciplinas[i].alunos[j].nota2);
		}
	}
	printf("\n");
	// mostrar
	for(i=0;i<n;i++){
		printf("Disciplina: %s\n",disciplinas[i].nome);
		
		for(j=0;j<disciplinas[i].qtdeAlunos;j++){
			printf("Aluno: %s\n",disciplinas[i].alunos[j].nome);
			printf("Nota 1: %.2f\n",disciplinas[i].alunos[j].nota1);
			printf("Nota 2: %.2f\n",disciplinas[i].alunos[j].nota2);
			float media = ( disciplinas[i].alunos[j].nota1 + disciplinas[i].alunos[j].nota2 ) / 2;
			printf("Media: %.2f\n",media);
		}
		printf("\n\n");
	}
	
	// free !!ordem contraria
	for(i=0;i<n;i++){ free(disciplinas[i].alunos); }
	free(disciplinas);
	
	
	
	return 0;
}
