#include <stdio.h>

void altera(int *pv, int tam)
{
	int x;
	for(x=0;x<tam;x++){
		pv[x] = pv[x] * x;
	}
}

int main()
{
	int quant, i;
	
	do{
		printf("Quantidade de elementos do vetor: ");
		scanf("%d%*c",&quant);
		if(quant<=1)
			printf("Informe um valor maior que 2.\n");
	}while(quant<=1);
	
	
	int vetor[quant];
	
	for(i=0;i<quant;i++){
		printf("Elemento %d: ",i+1);
		scanf("%d%*c",&vetor[i]);
	}
	
	printf("VETOR DIGITADO: ");
	for(i=0;i<quant;i++){
		printf("%d ",vetor[i]);
	}
	
	altera(vetor, quant);
	printf("\nVETOR NOVO: ");
	for(i=0;i<quant;i++){
		printf("%d ",vetor[i]);
	}
	
	return 0;
}
