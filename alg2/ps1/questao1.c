#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
	char palavra[40];
	int tamanho, i;
	int pontuacao, p;
	
	printf("Digite uma palavra: ");
	gets(palavra);
	
	while(1){
		pontuacao = 0;
		tamanho = strlen(palavra);
		for(i=0;i<tamanho;i++){
			palavra[i] = toupper(palavra[i]);
		}
		
		if ( strcmp(palavra,"FIM") == 0 ){
			break;
		}
		else{
			for(i=0;i<tamanho;i++){
				p = -1;
				switch (palavra[i]){
					case 'A':
					case 'E':
					case 'I':
					case 'O':
					case 'U':
					case 'L':
					case 'N':
					case 'S':
					case 'T':
					case 'R':
						p = 1;
						break;
					case 'D':
					case 'G':
						p = 2;
						break;
					case 'B':
					case 'C':
					case 'M':
					case 'P':
						p = 3;
						break;
					case 'F':
					case 'H':
					case 'V':
					case 'W':
					case 'Y':
						p = 4;
						break;
					case 'K':
						p = 5;
						break;
					case 'J':
					case 'X':
						p = 8;
						break;
					case 'Q':
					case 'Z':
						p = 10;
						break;
					default:
						printf("Letra invalida: %c\n", palavra[i]);
						break;
				}
				if(p == -1){
					break;
				}
				pontuacao = pontuacao + p;
			}
		}
		if (p != -1) {
			printf("Pontuacao total da palavra: %d\n",pontuacao);  
		}
		printf("\nDigite uma palavra: ");
		gets(palavra);
	}
	
	
	return 0;
}
