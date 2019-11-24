/* Ejercicio 16.7. Implementar la función void strcpy(const char *origen, char *destino) que
copia la cadena origen en la dirección de memoria apuntada por destino . Asumir que destino
apunta a un arreglo de caracteres con espacio suficiente ( strlen(origen) + 1 ).
*/

#include<stdio.h>

void str_cpy(const char *origen, char *destino){
	*destino = *origen[1];
	printf("Se copió correctamente %s\n", destino);
}

int main(){
	char destino[256];
	int max = 255;
	char cadena[max];
	fgets(cadena, max, stdin);
	str_cpy(cadena, destino);
	return 0;
}
