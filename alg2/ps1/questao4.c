#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
	int quant, i, tam = 0;
	
	do{
		printf("Digite a quantidade de strings: ");
		scanf("%d%*c",&quant);
		if(quant<=0)
			printf("Digite um numero maior que zero.\n\n");
	}while(quant<=0);
	
	char strings[quant][41];
	for(i=0;i<quant;i++){
		printf("Digite a string %d: ",i+1);
		gets(strings[i]);
		tam = tam + strlen(strings[i]);
	}
	printf("\nTotal geral de caracteres: %d\n",tam);
	
	for(i=0;i<quant;i++){
		int t = strlen(strings[i]);
		printf("Quantidade de caracteres da string %d: %d\n",i+1,t);
	}
	
	char primeira[41], ultima[41]; 
	strcpy(primeira,strings[0]);
	strcpy(ultima,strings[0]);
	
	for(i=0;i<quant;i++){
		if( strcmp(strings[i],primeira) < 0 )
			strcpy(primeira,strings[i]);
			
		if( strcmp(strings[i],ultima) > 0 )
			strcpy(ultima,strings[i]);
	}
	printf("Primeira string em ordem alfabetica: %s\n",primeira);
	printf("Ultima string em ordem alfabetica: %s\n",ultima);
	
	return 0;
}
