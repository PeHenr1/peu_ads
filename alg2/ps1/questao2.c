#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
	int quant, i;
	float media;
	
	
	
	do{
		printf("Digite a quantidade de estudantes: ");
		scanf("%d%*c",&quant);
		
		if(quant<=0){
			printf("Quantidade invalida. Digite um numero maior que zero.\n");
		}
	}while(quant<=0);

	float notas[quant];
	
	for(i=0;i<quant;i++){
				
		do{
			printf("Digite a nota do estudante %d: ",i+1);
			scanf("%f%*c",&notas[i]);
		
			if(notas[i] > 10 || notas[i] < 0){
				printf("Nota invalida. Digite uma nota entre 0 e 10.\n");
			}
		}while(notas[i] > 10 || notas[i] < 0);
		
		media = media + notas[i];
	}
	
	media = media/quant;
	printf("As notas digitadas foram: ");
	for(i=0;i<quant;i++){
		printf("%.1f ",notas[i]);
	}
	printf("\nA media das notas e: %.1f",media);
	
	return 0;
}
