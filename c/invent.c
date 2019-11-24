/*
 *The idea of this program is to practice before the last exam of ALGO1.
 *Escribir en C una función que pida al usuario que ingrese una cadena y la imprima invertida.
 */


#include<stdio.h>
#include<string.h>
#define largo_max 255

void cadena_invertida(){
	char cadena[largo_max];
	char invertida[largo_max];
	fgets(cadena, largo_max, stdin);
	//printf("La cadena: %s\n", cadena);
	int longitud_cadena = strlen(cadena) - 1;
	for(int i = 0; cadena[i] != '\0'; i++){
		invertida[i] = cadena[longitud_cadena - i]; 
	}
	printf("%s\n", invertida);	
}

int main(){
	cadena_invertida(); 
	return 0;
}


