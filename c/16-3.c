/*
 Ejercicio 16.3. Escribir una función que reciba un arreglo de números y 
 la cantidad de elementos, y devuelva el promedio.
 */

#include<stdio.h>

int numero = 5;
int arreglo[] = {19, 10, 8, 17, 9};

int promedio_array(int arreglo[], int n){
	int i;
	int suma;
	for (i = 0; i != n; i++) {
		suma = suma + arreglo[i];
	}
	return suma / n;
}

int main(){
	int promedio = promedio_array(arreglo, numero);
	printf("El promedio de el arreglo es: %d\n", promedio);
	return 0;
}
