/*
Ejercicio 16.10. Implementar una función que reciba una cadena de texto y luego imprima la
cadena enmarcada entre asteriscos ( * ). Asumir que la cadena no contiene ningún caracter \n .
Por ejemplo, si se recibe la cadena "Lenguaje C" , debe imprimir:

		**************
		* Lenguaje C *
		**************
*/

#include<stdio.h>
#include<string.h>

char cadena[255];

void imprimir_entre_asteriscos(char cadena[])
{
	int longitud_cadena = strlen(cadena);
	for(int i = 0; i < longitud_cadena + 3; i++){
		printf("*");
	}
	printf("\n");
	for(int i = 0; i < longitud_cadena; i++){
		if(i == 0){
			printf("* ");
		}
		if(i == longitud_cadena - 1){
			printf(" *");
		}
		printf("%c", cadena[i]);
	}

	for(int i = 0; i < longitud_cadena + 3; i++){
		printf("*");
	}
	printf("\n");
}

int main()
{
	fgets(cadena, 255, stdin);
	imprimir_entre_asteriscos(cadena);
	return 0;
}

