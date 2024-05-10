#include <stdio.h>

void maiorMenor(int m[][4], int *maior, int *menor)
{
	int i,j;
	*maior = m[0][0];
	*menor = m[0][0];
	
	for(i=0;i<3;i++){
		for(j=0;j<4;j++){
			if(m[i][j] > *maior){
				*maior = m[i][j];
			} 
			if(m[i][j] < *menor){
				*menor = m[i][j];
			}
		}
	}	
}
int main()
{
	int i ,j;
	
	int matriz[3][4];
	printf("Digite os valores para a matriz 3x4:\n");
	for(i=0;i<3;i++){
		for(j=0;j<4;j++){
			printf("Posicao [%d][%d]: ",i,j);
			scanf("%d%*c",&matriz[i][j]);
		}
	}
	
	int maior, menor;
	maiorMenor(matriz, &maior, &menor);
	
	printf("MATRIZ 3x4:\n");
	for(i=0;i<3;i++){
		for(j=0;j<4;j++){
			printf("%d ",matriz[i][j]);
		}
		printf("\n");
	}
	
	printf("\nMaior valor: %d\n",maior);
	printf("\nMenor valor: %d\n",menor);
	
	return 0;
}

