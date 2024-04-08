#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Exercicio 01
/*
struct Pessoa{
	char nome[20];
	char email[40];
	int idade;
	float salario;
};

int main(){
	struct Pessoa p;
	
	printf("Digite o nome da pessoa: ");
	gets(p.nome);
	printf("Digite o email: ");
	gets(p.email);
	printf("Digite a idade: ");
	scanf("%d%*c",&p.idade);
	printf("Digite o salario: ");
	scanf("%f%*c",&p.salario);
	
	printf("Nome: %s \nIdade: %d\n",p.nome,p.idade);
	printf("Email: %s\n",p.email);
	printf("Salario: R$%.2f",p.salario);

	return 0;
}
*/

// Exercicio 02
/*
typedef struct{
	char nome[20];
	char email[40];
	int idade;
	float salario;
}Pessoa;
int main(){
	Pessoa p;
	
	printf("Digite o nome da pessoa: ");
	gets(p.nome);
	printf("Digite o email: ");
	gets(p.email);
	printf("Digite a idade: ");
	scanf("%d%*c",&p.idade);
	printf("Digite o salario: ");
	scanf("%f%*c",&p.salario);
	
	printf("\nNome: %s \nIdade: %d\n",p.nome,p.idade);
	printf("Email: %s\n",p.email);
	printf("Salario: R$%.2f",p.salario);
	
	return 0;
}
*/

// Exercicio 03
/*
typedef struct{
	char nome[30];
	int idade, filho;
	float altura, peso, imc;
}Pessoa;
int main(){
	Pessoa pessoa[5];
	
	int i;
	for(i=0;i<5;i++){
		printf("Pessoa %d: \n",i+1);
		printf("Nome: ");
		gets(pessoa[i].nome);
		printf("Digite a idade: ");
		scanf("%d%*c",&pessoa[i].idade);
		printf("Digite a altura: ");
		scanf("%f%*c",&pessoa[i].altura);
		printf("Digite o peso: ");
		scanf("%f%*c",&pessoa[i].peso);
		pessoa[i].imc = pessoa[i].peso / (pessoa[i].altura * pessoa[i].altura);
		printf("IMC: %.2f",pessoa[i].imc);
		printf("\n\n");
	}
	
	for(i=0;i<5;i++){
		printf("Pessoa %d:\n",i+1);
		printf("Nome: %s\n",pessoa[i].nome);
		printf("Idade: %d\n",pessoa[i].idade);
		printf("Altura: %.2fm\n",pessoa[i].altura);
		printf("Peso: %.2fkg\n",pessoa[i].peso);
		printf("IMC: %.2f\n",pessoa[i].imc);
		printf("\n");
	}
	
	return 0;
}
*/

// Exercicio 04
/*
typedef struct{
	char nome[20];
	char email[40];
	int idade;
	float salario;
}Pessoa;
	
int main(){
	
	Pessoa p;
	
	printf("Digite o nome da pessoa: ");
	gets(p.nome);
	printf("Digite o email: ");
	gets(p.email);
	printf("Digite a idade: ");
	scanf("%d%*c",&p.idade);
	printf("Digite o salario: ");
	scanf("%f%*c",&p.salario);
	
	printf("\nNome: %s \nIdade: %d\n",p.nome,p.idade);
	printf("Email: %s\n",p.email);
	printf("Salario: R$%.2f",p.salario);
	
	printf("\n\nDigite um novo email: ");
	gets(p.email);
	printf("Digite uma nova idade: ");
	scanf("%d%*c",&p.idade);
	printf("Digite um novo salario: ");
	scanf("%f%*c",&p.salario);
	
	printf("\nDados alterados:\nNome: %s \nIdade: %d\n",p.nome,p.idade);
	printf("Email: %s\n",p.email);
	printf("Salario: R$%.2f",p.salario);
	
	return 0;
}
*/

// Exercicio 05
/*
struct Endereco{
	char nomeRua[40];
	int nCasa;
};
typedef struct{
	char nome[20];
	char email[40];
	int idade;
	float salario;
	struct Endereco endereco; 
}Pessoa;
int main(){

	struct Endereco end;
	Pessoa p;
	
	printf("Digite o nome da pessoa: ");
	gets(p.nome);
	printf("Digite o email: ");
	gets(p.email);
	printf("Digite a idade: ");
	scanf("%d%*c",&p.idade);
	printf("Digite o salario: ");
	scanf("%f%*c",&p.salario);
	
	printf("Digite o nome da rua: ");
	gets(end.nomeRua);
	printf("Digite o nº da casa: ");
	scanf("%d%*c",&end.nCasa);
	
	p.endereco = end;
	
	printf("\nNome: %s \nIdade: %d\n",p.nome,p.idade);
	printf("Email: %s\n",p.email);
	printf("Salario: R$%.2f\n",p.salario);
	printf("Endereco: %s, n%d",p.endereco.nomeRua,p.endereco.nCasa);
	
	return 0;
}
*/

// Exercicio 06
/*
typedef struct{
	char nomeRua[40];
	int nCasa;
}Endereco;

typedef struct{
	char nome[20];
	char email[40];
	int idade;
	float salario;
	Endereco endereco; 
}Pessoa;

int main(){
	Pessoa p[5];
	
	int i;
	for(i=0;i<5;i++){
		printf("Pessoa %d: \n",i+1);
		printf("Nome: ");
		gets(p[i].nome);
		printf("Digite o email: ");
		gets(p[i].email);
		printf("Digite a idade: ");
		scanf("%d%*c",&p[i].idade);
		printf("Digite o salario: ");
		scanf("%f%*c",&p[i].salario);
		printf("Digite o nome da rua: ");
		gets(p[i].endereco.nomeRua);
		printf("Digite o nº da casa: ");
		scanf("%d%*c",&p[i].endereco.nCasa);
		printf("\n");
	}
	
	for(i=0;i<5;i++){
		printf("Pessoa %d:\n",i+1);
		printf("Nome: %s\n",p[i].nome);
		printf("Email: %s\n",p[i].email);
		printf("Idade: %d\n",p[i].idade);
		printf("Salario: R&%.2f\n",p[i].salario);
		printf("Endereço: %s, n%d",p[i].endereco.nomeRua,p[i].endereco.nCasa);
		printf("\n\n");
	}	
	return 0;
}
*/

// Exercicio 07
/*
typedef struct{
	char nome[21];
	int idade;
}Pessoa;

int main(){
	Pessoa p[5];
	
	int i;
	for(i=0;i<5;i++){
		printf("Pessoa %d: \n",i+1);
		printf("Nome: ");
		gets(p[i].nome);
		printf("Digite a idade: ");
		scanf("%d%*c",&p[i].idade);
		printf("\n");
	}
	int auxId, j;
	char auxNo[21];

	for(i=0;i<5;i++){
		for(j=0;j<5;j++){
			if( p[i].idade < p[j].idade ){
				auxId = p[j].idade;
				p[j].idade = p[i].idade;
				p[i].idade = auxId;
				
				strcpy(auxNo,p[j].nome);
				strcpy(p[j].nome,p[i].nome);
				strcpy(p[i].nome,auxNo);
			}
		}
	}
	
	printf("\n CRESCENTE \n");
	for(i=0;i<5;i++){
		printf("Pessoa %d: \n",i+1);
		printf("Nome: %s\n",p[i].nome);
		printf("Idade: %d\n\n",p[i].idade);
	}
	return 0;
}
*/

// Exercicio 08
/*
typedef struct{
	char nome[21];
	int idade;
}Pessoa;

int main(){
	Pessoa p[5];
	
	int i;
	for(i=0;i<5;i++){
		printf("Pessoa %d: \n",i+1);
		printf("Nome: ");
		gets(p[i].nome);
		printf("Digite a idade: ");
		scanf("%d%*c",&p[i].idade);
		printf("\n");
	}
	
	
	int n, flag = 0;
	printf("Idade a ser pesquisada: ");
	scanf("%d%*c",&n);
	
	for(i=0;i<5;i++){
		if(p[i].idade == n){
			printf("%s tem essa idade.\n",p[i].nome);
			flag = 1;
		}
	}
	if(!flag){
		printf("Ninguem tem essa idade.\n");
	}
	
	return 0;
}
*/

// Exercicio 09
/*
typedef struct{
	char titulo[41];
	int ano;
}Livro;

int main(){
	Livro estante[3][3];

	int i, j;
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			printf("Titulo do livro %d da estante %d: ", i+1,j+1);
			gets(estante[i][j].titulo);
			printf("Ano de lancamento deste livro: ");
			scanf("%d%*c",&estante[i][j].ano);
			printf("\n");
		}
	}
	
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			printf("%s - %d | ",estante[i][j].titulo,estante[i][j].ano);
		}
		printf("\n");
	}

	return 0;
}
*/

// Exercicio 10
/*
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
*/

// Exercicio 11
/*
typedef struct{
	int codigo, dependentes;
	char cargo[41], nome[41];
	float salario;
}Funcionario;

void menu(){
	printf("\n1 - Cadastrar um funcionario\n");
	printf("2 - Consultar dados de um funcionario\n");
	printf("3 - Imprimir todos os funcionarios\n");
	printf("4 - Alterar dados de um funcionario\n");
	printf("0 - Encerrar\n");
}

int main(){
	menu();
	int quant = 100,i;
	char consultar[41];
	Funcionario funcionario[quant];
	int opc, livre = 0;
	printf("\nOpcao: ");
	scanf("%d%*c",&opc);
	while(opc != 0){
		switch(opc){
			case 1:
				if(livre < quant){
					printf("\nCodigo (numerico): ");
					scanf("%d%*c",&funcionario[livre].codigo);
					printf("Nome: ");
					gets(funcionario[livre].nome);
					printf("Cargo: ");
					gets(funcionario[livre].cargo);
					printf("Numero dependentes: ");
					scanf("%d%*c",&funcionario[livre].dependentes);
					printf("Salario: ");
					scanf("%f%*c",&funcionario[livre].salario);
					printf("Funcionario cadastrado!\n\n");
					livre++;
				}
				else{
					printf("Limite de cadastramento alcancado!\n\n");
				}
				break;
			case 2:
				printf("Funcionario que deseja consultar: ");
				gets(consultar);
				int flag = 0;
				for(i=0;i<quant;i++){
					if(strcmp(consultar,funcionario[i].nome) == 0){
						flag = 1;
						printf("\nDADOS DO FUNCIONARIO: %s\n",consultar);
						printf("Codigo: %d\n",funcionario[i].codigo);
						printf("Cargo: %s\n",funcionario[i].cargo);
						printf("Numero dependentes: %d\n",funcionario[i].dependentes);
						printf("Salario: %.2f\n",funcionario[i].salario);				
					}
				}
				if(!flag){
					printf("Funcionario nao encontrado.\n");
				}
				break;
			
			case 3:
				printf("\nTODOS OS FUNCIONARIOS:\n");
				for(i=0;i<livre;i++){
					printf("Codigo: %d\n",funcionario[i].codigo);
					printf("Nome: %s\n",funcionario[i].nome);
					printf("Cargo: %s\n",funcionario[i].cargo);
					printf("Numero dependentes: %d\n",funcionario[i].dependentes);
					printf("Salario: %.2f\n\n",funcionario[i].salario);				
				}
				break;
			
			case 4:
				printf("Funcionario que deseja alterar dados: ");
				gets(consultar);
				flag = 0;
				for(i=0;i<quant;i++){
					if(strcmp(consultar,funcionario[i].nome) == 0){
						flag = 1;
						printf("\nALTERAR DADOS DO FUNCIONARIO: %s\n",consultar);
						printf("\nNovo Codigo (numerico): ");
						scanf("%d%*c",&funcionario[i].codigo);
						printf("Novo Nome: ");
						gets(funcionario[i].nome);
						printf("Novo Cargo: ");
						gets(funcionario[i].cargo);
						printf("Novo Numero dependentes: ");
						scanf("%d%*c",&funcionario[i].dependentes);
						printf("Novo Salario: ");
						scanf("%f%*c",&funcionario[i].salario);
						printf("Dados atualizados!\n\n");				
					}
				}
				if(!flag){
					printf("Funcionario nao encontrado.\n");
				}
				break;
			
			default:
				printf("Valor digitado invalido.\n");
				break;
		}
		menu();
		printf("\nOpcao: ");
		scanf("%d%*c",&opc);
	}
	
	return 0;
}
*/

// Exercicio 12
/*
typedef struct{
	float salario;
	int idade, nFilhos;
	char sexo[2];
}Habitante;
int main(){
	int quant = 4, i;
	Habitante habitante[quant];
	
	for(i=0;i<quant;i++){
		printf("HABITANTE %d: \n",i+1);
		printf("Idade: ");
		scanf("%d%*c",&habitante[i].idade);
		printf("Sexo (F/M): ");
		gets(habitante[i].sexo);
		printf("Numero de filhos: ");
		scanf("%d%*c",&habitante[i].nFilhos);
		printf("Salario: ");
		scanf("%f%*c",&habitante[i].salario);
		printf("\n");
	}
	
	float mSal = 0, mFil = 0;
	float maiorS = habitante[0].salario, menorS = habitante[0].salario;
	int indMaior = 0, indMenor = 0, mulher = 0;
	float percent = 0;
	for(i=0;i<quant;i++){
		mSal = mSal + habitante[i].salario;
		mFil = mFil + habitante[i].nFilhos;
		
		if(habitante[i].salario > maiorS){
			maiorS = habitante[i].salario;
			indMaior = i;
		}
		if(habitante[i].salario < menorS){
			menorS = habitante[i].salario;
			indMenor = i;
		}
		
		if (strcmp(habitante[i].sexo,"F") == 0){
			mulher++;
			if(habitante[i].salario > 1500){
				percent++;
			}
		}
	}
	
	mSal = mSal/quant;
	mFil = mFil/quant;
	printf("Media salarial dos habitantes: R$%.2f\n",mSal);
	printf("Numero medio de filhos: %.1f\n",mFil);
	printf("Maior salario: Habitante %d - R$%.2f\n",indMaior+1,maiorS);
	printf("Menor salario: Habitante %d - R$%.2f\n",indMenor+1,menorS);
	percent = (percent/mulher)*100;
	printf("Percentual de mulheres com salario maior que R$1500: %.1f por cento",percent);

	return 0;
}
*/
