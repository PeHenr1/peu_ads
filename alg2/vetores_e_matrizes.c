#include <stdio.h>

// Exercicio 01
/*
int main(){
	// usuario que deveria fazer os input
	int vetor[8] = {8,-2,3,1,-5,7,-14,10};
	int posit[8] = { 0 };
	int negat[8] = { 0 };
	
	int fimV = 7, fimP = 7, fimN = 7;
	int livreP = 0, livreN = 0;
	
	int i;
	for(i=0;i <= fimV; i++){
		if(vetor[i] > 0){
			if(livreP <= fimP){
				posit[livreP] = vetor[i];
				livreP++;
			}
			
		}
		else{
			if(livreN <= fimN){
				negat[livreN] = vetor[i];
				livreN++;
			}
		}
	}
	
	printf("Vetor inicial: ");
	for(i=0; i<fimV; i++)
		printf("%d ", vetor[i]);
	
	printf("\nVetor positivos: ");
	for(i=0; i<livreP; i++)
		printf("%d ", posit[i]);
	
	printf("\nVetor negativos: ");
	for(i=0; i<livreN; i++)
		printf("%d ", negat[i]);
	
}
*/

// Exercicio 02
/*int main(){
	int a[10] = {8,3,1,7,10,12,77,100,33,54};
	int b[10] = {-2,-5,-14,5,6,12,17,20,66,16};
	int c[20] = { 0 };
	
	int livreC = 0, fim = 9, fimC = 19, i;
	
	for(i=0;i <= fim; i++){
		if(livreC <= fimC){
			c[livreC] = a[i];
			livreC++;
			c[livreC] = b[i];
			livreC++;
		}
	}
	
	printf("Vetor A: ");
	for(i=0; i<fim; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\nVetor B: ");
	for(i=0; i<fim; i++)
	{
		printf("%d ", b[i]);
	}	
	printf("\nVetor C: ");
	for(i=0; i<fimC; i++)
	{
		printf("%d ", c[i]);
	}
}
*/

// Exercicio 03
/*
int main(){
	int i, j;
	int matriz[3][3] ;
	
	for(i = 0; i < 3;i++){
		for(j = 0; j < 3; j++){
			printf("Digite o valor da linha %d e coluna %d: ",i,j);
			scanf("%d%*c",&matriz[i][j]);
		}
	}
	
	printf("\n");
	for(i = 0; i < 3;i++){
		for(j = 0; j < 3; j++){
			printf("%d ",matriz[i][j]);
		}
		printf("\n");
	}
	
	int flag = 0;
	for(i = 0; i < 3;i++){
		for(j = 0; j < 3; j++){
			if(matriz[i][j] != matriz[j][i] ){
				flag = 1;
			}
		}
	}
	if(flag)
		printf("A matriz nao e simetrica");
	else
		printf("A matriz e simetrica");
}
*/

//Exercicio 04
int main(){
	int n, i, j;
	
	printf("Numero de linhas e colunas: \n");
	scanf("%d%*c",&n);
	
	int v[n][n];
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			printf("Digite o valor da linha %d e coluna %d: ",i,j);
			scanf("%d%*c",&v[i][j]);
		}
	}
	
	printf("\n");
	for(i = 0; i < n;i++){
		for(j = 0; j < n; j++){
			printf("%d ",v[i][j]);
		}
		printf("\n");
	}
}

