#include <stdio.h>
#include <string.h> 

void mensagem(){
	printf("Ola mundo!\n");
}

void soma(int n1, int n2){
	printf("A soma dos numeros da: %d.\n",n1+n2);
}

void concatena(char text1[21], char text2[21]){	
	printf("Strings digitadas concatenadas: %s",strcat(text1,text2));
}

int maiorNum(int vet[6]){
	int i, m;
	m = vet[0];
	for(i=0;i<6;i++){
		if(vet[i] > m){
			m = vet[i];
		}
	}
	return m;
}

int maiorEntreDois(int n1, int n2){
	return n1 > n2 ? n1 : n2;
}

void media(float vetN[5]){
	int i;
	float m = 0;
	for(i=0;i<5;i++){
		m += vetN[i];
	}
	m = m/5;
	printf("Media: %.2f",m);
}

int vezesAparece(int vet[7], int num){
	int i, cont = 0;
	for(i=0;i<7;i++){
		if(vet[i] == num){
			cont++;
		}
	}
	return cont;
}


