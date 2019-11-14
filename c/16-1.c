//Ejercicio 16.1. 
//Escribir una función que permita calcular el área de un rectángulo dada su base
//y altura.

#include<stdio.h>

int base_por_altura(int base, int altura);

int main()
{	
	int resultado;
	resultado = base_por_altura(4, 50);	
	printf("El resultado es: %d\n", resultado);
	return 0;
}

int base_por_altura(int base, int altura)
{
	return base * altura;
}