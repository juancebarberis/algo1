/*
Ejercicio 16.9. Implementar una función que reciba un mensaje y dos números enteros min y
max . La función debe pedir al usuario que ingrese un número entero entre min y max (inclusive)
y devolverlo. Si el usuario ingresa un valor inválido se le debe informar y pedir que ingrese un
nuevo valor, repitiendo hasta que ingrese un número válido.
*/

#include<stdio.h>
#include<stdlib.h>

#define mensaje "Hola, por favor ingrese su edad. Debe ser mayor que:"
#define min 18
#define max 100

void verficar_edad(char texto[], int minimo, int maximo){
	printf("%s %d\n", texto, min);	//Mensaje inicial.
	char entrada[255];
	while(atoi(entrada) < min || atoi(entrada) > max){
		printf("Ingrese un valor válido:");
		fgets(entrada, 255, stdin);
	}
	printf("Gracias, su edad ha quedado registrada como: %s\n", entrada);
}

int main(){
	verficar_edad(mensaje, min, max);
	return 0;
}